#!/usr/bin/env python3
"""Validate the book catalog, complete provenance and mathematics before compilation."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import subprocess
from booklib import ROOT, HEADING, INTERNAL_LINK, math_spans, prose_without_tokens


def link_issues(texts: list[tuple[str, str]], targets: set[str]) -> list[str]:
    """Check source links before TeX, including duplicate explicit heading anchors."""
    errors = []
    definitions = {target: '目录' for target in targets}
    for path, text in texts:
        for heading in HEADING.finditer(text):
            anchor = heading[3]
            if not anchor:
                continue
            if anchor in definitions:
                errors.append(f'{path}: 重复锚点 {anchor}（已在 {definitions[anchor]} 定义）')
            definitions[anchor] = path
    for path, text in texts:
        for link in INTERNAL_LINK.finditer(prose_without_tokens(text)):
            if link[2] not in definitions:
                errors.append(f'{path}: 缺少内部链接目标 {link[2]}')
    return errors


def math_issues(text: str) -> list[str]:
    issues = []
    prose = prose_without_tokens(text)
    if re.search(r'(?<!\\)\$|(?<!\\)\\[\[\]]', prose):
        issues.append('数学定界符未配对')
    for start, _, formula, _ in math_spans(text):
        line = text[:start].count('\n') + 1
        stack = []
        depth = 0
        for token in re.findall(r'\\(?:begin|end)\{[^}]+\}|\\.|[{}]', formula):
            if token.startswith(r'\begin{'):
                stack.append(token[7:-1])
            elif token.startswith(r'\end{'):
                env = token[5:-1]
                if not stack or stack.pop() != env:
                    issues.append(f'第 {line} 行：环境错配 {env}')
            elif token == '{':
                depth += 1
            elif token == '}':
                depth -= 1
                if depth < 0:
                    issues.append(f'第 {line} 行：多余闭花括号')
        if stack or depth:
            issues.append(f'第 {line} 行：环境或花括号未封闭')
        if re.search(r'\\begin\{(?:equation|align|gather|multline)\*?\}', formula):
            issues.append(f'第 {line} 行：显示公式内嵌顶层环境')
        if re.search(r'[_^]\s*\\(?:math(?:bb|bf|rm|it|sf|tt|cal|frak)|sym[a-z]+)\b', formula):
            issues.append(f'第 {line} 行：上下标中的字体命令须整体加花括号')
    return issues


def source_location(paper: str) -> tuple[str, int, int, str]:
    """Infer edition and audience from provenance, never from a topic alias."""
    match = re.fullmatch(r'fin(\d+)-(hi|high|lo|low|all|fill|geom)', paper)
    if match:
        group = {'hi':'high', 'high':'high', 'lo':'low', 'low':'low', 'all':'all'}.get(match[2], 'topic')
        return 'finals', int(match[1]), 0, group
    match = re.fullmatch(r'ch\d+-(\d+)th-A(?:-makeup(2)?)?', paper)
    if match:
        sitting = 2 if match[2] else 1 if '-makeup' in paper else 0
        return 'preliminary', int(match[1]), sitting, 'all'
    match = re.fullmatch(r'pre(\d+)-math', paper)
    if match:
        return 'preliminary', int(match[1]), 0, 'all'
    raise ValueError(f'无法识别来源编号：{paper}')


def catalog_issues(book: dict) -> list[str]:
    """Check identity, order, complete provenance and on-disk catalog coverage."""
    from booklib import PROBLEM_ID
    errors = []
    base = book['path'].parent
    sources = book['sources']
    if [part.get('id') for part in book['parts']] != ['preliminary', 'finals']:
        errors.append('分部必须按初赛 preliminary、决赛 finals 排列且各出现一次')
    locations = {}
    for paper, metadata in sources.items():
        try:
            locations[paper] = source_location(paper)
        except ValueError as error:
            errors.append(str(error))
        if not isinstance(metadata, dict) or not isinstance(metadata.get('title'), str) or not metadata['title'].strip():
            errors.append(f'{paper}: 来源须有非空 title')
    chapter_ids = set()
    problem_ids = set()
    problem_paths = set()
    index_paths = set()
    origins_seen = {}
    source_numbers = {}
    stems_seen = {}
    for part in book['parts']:
        part_id = part.get('id')
        order = []
        if not isinstance(part.get('title'), str) or not part['title'].strip():
            errors.append(f'{part_id}: 缺少分部标题')
        for chapter in part['chapters']:
            cid = chapter.get('id')
            edition = chapter.get('edition')
            year = chapter.get('year')
            match = re.fullmatch(r'(preliminary|finals)-(\d+)(?:-makeup(2)?)?', cid or '')
            if not match or match[1] != part_id or int(match[2]) != edition:
                errors.append(f'{cid}: 章编号、分部与届数不一致')
                sitting = 0
            else:
                sitting = 2 if match[3] else 1 if '-makeup' in cid else 0
            if part_id == 'finals' and sitting:
                errors.append(f'{cid}: 决赛不应带初赛补赛标记')
            if type(edition) is not int or edition <= 0 or type(year) is not int or year < 1900:
                errors.append(f'{cid}: 届数和年份须为有效整数')
            else:
                order.append((edition, sitting))
            if cid in chapter_ids:
                errors.append(f'重复章编号：{cid}')
            chapter_ids.add(cid)
            if not isinstance(chapter.get('title'), str) or not chapter['title'].strip():
                errors.append(f'{cid}: 缺少章标题')
            if chapter['index_path'] in index_paths:
                errors.append(f'{cid}: 重复列入 index.json')
            index_paths.add(chapter['index_path'])
            if not chapter['items']:
                errors.append(f'{cid}: 空章')
            for note in chapter['notes']:
                if not isinstance(note, dict) or not isinstance(note.get('text'), str) or not note['text'].strip() or note.get('paper') not in sources:
                    errors.append(f'{cid}: 卷首说明必须保留有效来源和非空正文')
                elif locations.get(note['paper'], ())[:3] != (part_id, edition, sitting):
                    errors.append(f'{cid}: 卷首说明来源属于另一届或场次')
            item_order = []
            for item in chapter['items']:
                key = item.get('id')
                valid_id = isinstance(key, str) and PROBLEM_ID.fullmatch(key)
                if not valid_id:
                    errors.append(f'{cid}: 无效永久题号 {key!r}')
                elif key in problem_ids:
                    errors.append(f'重复永久题号：{key}')
                problem_ids.add(str(key))
                if item['path'] in problem_paths:
                    errors.append(f'{key}: 同一单题文件被目录重复使用')
                problem_paths.add(item['path'])
                if item.get('audience') not in ('all', 'low', 'high'):
                    errors.append(f'{key}: audience 只能为 all、low、high')
                provenance = item.get('origins')
                if not isinstance(provenance, list) or not provenance:
                    errors.append(f'{key}: 缺少出处 origins')
                    continue
                groups = set()
                origin_keys = set()
                for origin in provenance:
                    if not isinstance(origin, dict) or not isinstance(origin.get('paper'), str) or type(origin.get('number')) is not int or origin['number'] < 1:
                        errors.append(f'{key}: 无效出处 {origin!r}')
                        continue
                    paper, number = origin['paper'], origin['number']
                    origin_key = f'{paper}:{number}'
                    if origin_key in origins_seen:
                        errors.append(f'{origin_key}: 出处或别名重复，分别指向 {origins_seen[origin_key]} 与 {key}')
                    origins_seen[origin_key] = key
                    origin_keys.add(origin_key)
                    source_numbers.setdefault(paper, set()).add(number)
                    if paper not in sources:
                        errors.append(f'{key}: 出处 {paper} 不在 sources.json 中')
                        continue
                    location = locations.get(paper)
                    if location is not None:
                        if location[:3] != (part_id, edition, sitting):
                            errors.append(f'{key}: 出处 {paper} 属于另一分部、届数或场次')
                        if location[3] != 'topic':
                            groups.add(location[3])
                if key not in origin_keys:
                    errors.append(f'{key}: 永久题号须保留在自身 origins 中')
                expected = 'all' if part_id == 'preliminary' or groups == {'low', 'high'} else next(iter(groups)) if len(groups) == 1 else None
                if expected is None:
                    errors.append(f'{key}: 只有专题别名，无法确定实际参赛组别')
                elif item.get('audience') != expected:
                    errors.append(f'{key}: audience={item.get("audience")} 与实际组别 {expected} 不符；专题别名不决定组别')
                if valid_id:
                    item_order.append((0 if item.get('audience') == 'all' else 1, int(key.rsplit(':', 1)[1]), {'all':0, 'low':1, 'high':2}.get(item.get('audience'), 9), key))
                stem = re.sub(r'\s+|\\(?:left|right)\b', '', item['blocks']['题目'])
                if len(stem) >= 40:
                    if stem in stems_seen:
                        errors.append(f'{key} 与 {stems_seen[stem]} 题干完全相同，应合并出处')
                    stems_seen[stem] = key
            if item_order != sorted(item_order):
                errors.append(f'{cid}: 题目须按共同题在前、专属原题号递增及同号低在高前排列')
        if order != sorted(order) or len(order) != len(set(order)):
            errors.append(f'{part_id}: 届数必须递增，同届补赛紧随正赛且场次不可重复')
    if set(source_numbers) != set(sources):
        unused = sorted(set(sources) - set(source_numbers))
        unknown = sorted(set(source_numbers) - set(sources))
        errors.append(f'来源覆盖不完整：未使用 {unused}，未知 {unknown}')
    for paper, numbers in source_numbers.items():
        if numbers != set(range(1, max(numbers) + 1)):
            errors.append(f'{paper}: 出处题号不连续，可能遗漏题目或别名')
        metadata = sources.get(paper, {})
        expected = metadata.get('problem_numbers') if isinstance(metadata, dict) else None
        if expected is None:
            errors.append(f'{paper}: 缺少来源 problem_numbers 出处清单')
        elif (not isinstance(expected, list) or any(type(n) is not int or n < 1 for n in expected) or len(expected) != len(set(expected)) or set(expected) != numbers):
            errors.append(f'{paper}: origins 与来源 problem_numbers 清单不一致')
    actual_files = {p.resolve() for p in (base/'problems').rglob('*.md')}
    actual_indexes = {p.resolve() for p in (base/'problems').rglob('index.json')}
    if actual_files != problem_paths:
        errors.append('单题目录与文件不一致：' + ', '.join(str(p.relative_to(base)) for p in sorted(actual_files ^ problem_paths)))
    if actual_indexes != index_paths:
        errors.append('章目录与 index.json 文件不一致')
    return errors


def check_sources(paths: list[Path] | None = None, katex: bool = True, catalog: Path | None = None) -> tuple[list[str], dict]:
    from booklib import load_book, load_problem, iter_problems
    errors = []
    formulas = []
    notes = []
    texts = []
    report = {'papers':0, 'chapters':0, 'problems':0, 'solutions':0, 'comments':0, 'origins':0}
    if paths is None:
        try:
            book = load_book(catalog)
            errors.extend(catalog_issues(book))
        except (ValueError, OSError, TypeError, KeyError) as error:
            return [str(error)], {**report, 'formulas':0, 'editorial_notes':[]}
        rows = list(iter_problems(book))
        report.update(papers=len(book['sources']), chapters=sum(len(p['chapters']) for p in book['parts']), problems=len(rows), solutions=len(rows), comments=sum('评注' in item['blocks'] for _,_,item in rows), origins=sum(len(item['origins']) for _,_,item in rows))
        frontmatter = book['path'].parent/'frontmatter.md'
        try:
            front = frontmatter.read_text()
            if not re.match(r'\A# [^\n]+\n', front):
                errors.append(f'{frontmatter}: 序言缺少章标题')
            texts.append(('frontmatter.md', front))
        except OSError as error:
            errors.append(str(error))
        for _, chapter, item in rows:
            texts.append((str(item['path'].relative_to(book['path'].parent)), item['path'].read_text()))
        for part in book['parts']:
            for chapter in part['chapters']:
                for number, note in enumerate(chapter['notes'], 1):
                    if isinstance(note, dict) and isinstance(note.get('text'), str):
                        texts.append((f'{chapter["id"]}:卷首说明{number}', note['text']))
        targets = {'pr:' + item['id'] for _, _, item in rows}
        targets.update('exam:' + c['id'] for p in book['parts'] for c in p['chapters'])
        if catalog is None:
            from booklib import method_texts
            try:
                texts.extend(method_texts())
            except (ValueError, OSError, KeyError) as error:
                errors.append(str(error))
        errors.extend(link_issues(texts, targets))
    else:
        for path in paths:
            try:
                text = path.read_text()
                blocks = load_problem(path)
                report['problems'] += 1
                report['solutions'] += 1
                report['comments'] += '评注' in blocks
                texts.append((str(path), text))
            except (ValueError, OSError) as error:
                errors.append(str(error))
    for label, text in texts:
        if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', text):
            errors.append(f'{label}: 含有非法控制字符')
        errors.extend(f'{label}: {issue}' for issue in math_issues(text))
        if re.search(r'\\(?:ref|hyperref|label)\b', prose_without_tokens(text)):
            errors.append(f'{label}: 正文引用须使用 Markdown 链接与标题锚点，不可写裸 TeX 引用命令')
        if '原文未收录解答' in text:
            errors.append(f'{label}: 存在未完成解答')
        for start, _, formula, display in math_spans(text):
            formulas.append({'id':f'{label}:{text[:start].count(chr(10))+1}', 'tex':formula, 'display':display})
        for number, line in enumerate(text.splitlines(), 1):
            if any(word in line for word in ('存疑', '无法确定', '待核', '缺失', '不能恢复', '题干订正', '校订：')):
                notes.append({'source':f'{label}:{number}', 'text':line})
    if katex:
        result = subprocess.run(['node', str(ROOT/'tools/katex_check.js')], input=json.dumps({'items':formulas}), text=True, capture_output=True)
        if result.returncode:
            errors.append('KaTeX 未能运行：'+result.stderr.strip())
        else:
            for row in json.loads(result.stdout)['results']:
                if not row['ok']:
                    errors.append(row['id']+': '+row['error'])
    return errors, {**report, 'formulas':len(formulas), 'editorial_notes':notes}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--problem', action='append', type=Path, help='检查指定单题文件')
    ap.add_argument('--catalog', type=Path, help='使用指定 book.json，默认 src/book.json')
    ap.add_argument('--no-katex', action='store_true')
    args = ap.parse_args()
    if args.problem and args.catalog:
        ap.error('--catalog 与 --problem 不可同时使用')
    errors, report = check_sources(args.problem, not args.no_katex, args.catalog)
    for error in errors:
        print(error)
    print(f"检查 {report['chapters']} 章、{report['problems']} 道题、{report['origins']} 个出处、{report['formulas']} 个公式；{len(errors)} 个错误。")
    if not args.problem:
        (ROOT/'build').mkdir(exist_ok=True)
        (ROOT/'build/source-check.json').write_text(json.dumps({'errors':errors, **report}, ensure_ascii=False, indent=2)+'\n')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
