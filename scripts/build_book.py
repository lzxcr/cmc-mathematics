#!/usr/bin/env python3
"""Assemble the chronological catalog without rewriting mathematical source."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
from booklib import ROOT, HEADING, load_book, method_texts, inline, render


def markdown_chapter(path: Path, targets: set[str] | dict[str, str] | None = None) -> str:
    text = path.read_text(encoding='utf-8').strip()
    title, _, body = text.partition('\n')
    if not title.startswith('# '):
        raise ValueError(f'{path}: 缺少章标题')
    parts = []
    cursor = 0
    for heading in HEADING.finditer(text):
        parts.append(render(text[cursor:heading.start()], targets))
        command = {1:'chapter', 2:'section', 3:'subsection'}[len(heading[1])]
        parts.append('\\' + command + '{' + inline(heading[2], targets) + '}')
        if heading[3]:
            parts.append(r'\label{' + heading[3] + '}')
            parts.append(r'\hypertarget{' + heading[3] + '}{}')
        cursor = heading.end()
    parts.append(render(text[cursor:], targets))
    return '\n\n'.join(parts)


def paper_caption(slug: str) -> str:
    if re.search(r'-(?:hi|high)$', slug):
        return '高年级组'
    if re.search(r'-(?:lo|low)$', slug):
        return '低年级组'
    if slug.endswith('-fill'):
        return '填空题专题'
    if slug.endswith('-geom'):
        return '解析几何专题'
    return '试题与参考解答'


def build(out: Path, only: set[str]) -> dict:
    book = load_book()
    known = {c['id'] for p in book['parts'] for c in p['chapters']}
    if only - known:
        raise ValueError('未知场次：' + ', '.join(sorted(only - known)))
    targets = {'exam:' + c['id']: '' for p in book['parts'] for c in p['chapters'] if not only or c['id'] in only}
    targets.update({'pr:' + i['id']: '' for p in book['parts'] for c in p['chapters'] if not only or c['id'] in only for i in c['items']})
    for path in [ROOT/'src/frontmatter.md']:
        targets.update({m[3]: '' for m in HEADING.finditer(path.read_text()) if m[3]})
    for _, text in method_texts():
        targets.update({m[3]: 'methods.pdf' for m in HEADING.finditer(text) if m[3]})
    out.parent.mkdir(parents=True, exist_ok=True)
    standard = out.stem == 'book'
    chapter_dir = out.parent / ('chapters' if standard else out.stem + '-chapters')
    chapter_dir.mkdir(exist_ok=True)
    stats = dict(parts=0, chapters=0, sources=0, problems=0,
                 solutions=0, remarks=0, origins=0)
    master = [r'''% !TEX program = lualatex
% Generated: edit src/book.json, src/problems/, src/frontmatter.md or src/layout.tex.
\input{src/layout.tex}
\begin{document}
\SynapticMakeTitle
\SynapticFrontMatter
\input{build/frontmatter.tex}
\input{src/credits.tex}
\SynapticBookContents
\SynapticMainMatter
\setcounter{secnumdepth}{-1}''']
    # All include paths are relative to the documented project-root working directory.
    def include(path: Path, text: str):
        path.write_text(text.rstrip() + '\n', encoding='utf-8')
        master.append(r'\input{' + Path(os.path.relpath(path, ROOT)).as_posix() + '}')
    front = out.parent / ('frontmatter.tex' if standard else out.stem + '-frontmatter.tex')
    front.write_text(markdown_chapter(ROOT/'src/frontmatter.md', targets) + '\n', encoding='utf-8')
    master[0] = master[0].replace('build/frontmatter.tex', Path(os.path.relpath(front, ROOT)).as_posix())
    index = []
    selected_sources = set()
    for part in book['parts']:
        chapters = [c for c in part['chapters'] if not only or c['id'] in only]
        if not chapters:
            continue
        master.append(r'\part{' + inline(part['title']) + '}')
        stats['parts'] += 1
        for chapter in chapters:
            stats['chapters'] += 1
            tex = [r'\chapter{' + inline(chapter['title']) + '}',
                   r'\label{exam:' + chapter['id'] + '}',
                   r'\hypertarget{exam:' + chapter['id'] + '}{}']
            for note in chapter['notes']:
                prefix = paper_caption(note['paper']) + '：' if part['id'] == 'finals' else ''
                tex.append(r'{\small\color{syn-muted-text}' + render(prefix + note['text'], targets) + r'\par}')
            for item in chapter['items']:
                title = f"题 {item['number']}" + {'all':'', 'low':'（低年级组）', 'high':'（高年级组）'}[item['audience']]
                tex.append(r'\BookProblem{' + inline(title) + '}{' + item['id'] + '}')
                for kind, env, count in [('题目','synproblem','problems'), ('解答','synsolution','solutions'), ('评注','synremark','remarks')]:
                    if kind in item['blocks']:
                        heading = title if kind == '题目' else kind
                        tex.append(r'\begingroup\SynapticStatementTitle{' + inline(heading) + '}\n' +
                                   r'\begin{' + env + '}\n' + render(item['blocks'][kind], targets) + '\n' +
                                   r'\end{' + env + r'}\endgroup')
                        stats[count] += 1
                tex.append(r'\BookProblemEnd')
                stats['origins'] += len(item['origins'])
                selected_sources.update(o['paper'] for o in item['origins'])
                index.append({'part': part['title'], 'chapter': chapter['title'], 'chapter_id': chapter['id'],
                              'number': item['number'], 'id': item['id'], 'audience': item['audience'],
                              'path': str(item['path'].relative_to(ROOT)), 'origins': item['origins']})
            include(chapter_dir/(chapter['id']+'.tex'), '\n\n'.join(tex))
    master.append(r'\end{document}')
    stats['sources'] = len(selected_sources)
    out.write_text('\n\n'.join(master) + '\n', encoding='utf-8')
    report = {'stats': stats, 'missing': []}
    out.with_suffix('.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    index_name = 'problem-index.json' if standard else out.stem + '-problem-index.json'
    out.with_name(index_name).write_text(json.dumps(index, ensure_ascii=False, indent=2)+'\n')
    # A newly assembled source must not inherit a previous PDF's passing report.
    verification_name = 'verification.json' if standard else out.stem + '-verification.json'
    out.with_name(verification_name).unlink(missing_ok=True)
    if standard:
        out.with_name('cross-volume-verification.json').unlink(missing_ok=True)
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, default=ROOT/'build/book.tex')
    ap.add_argument('--only', default='', help='场次 id，以逗号分隔，例如 preliminary-11,finals-07')
    args = ap.parse_args()
    try:
        print(json.dumps(build(args.out.resolve(), set(filter(None, args.only.split(',')))), ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError) as error:
        ap.exit(1, f'{error}\n')

if __name__ == '__main__':
    raise SystemExit(main())
