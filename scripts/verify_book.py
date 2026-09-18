#!/usr/bin/env python3
"""Check final labels and compilation diagnostics, including missing glyphs and overflow."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re


def read_tex_tree(path: Path, active: set[Path] | None = None) -> str:
    """Read explicit local inputs as TeX sees them from the project root."""
    active = active or set()
    path = path.resolve()
    if path in active:
        raise ValueError(f'循环 TeX 输入：{path}')
    active.add(path)
    text = path.read_text()
    # Comments may mention old labels or inputs; they are not document content.
    text = re.sub(r'(?<!\\)%[^\n]*', '', text)
    def include(match):
        child = Path(match[1])
        if not child.suffix:
            child = child.with_suffix('.tex')
        if not child.is_absolute() and not child.exists():
            child = path.parent / child
        return read_tex_tree(child, active)
    text = re.sub(r'\\(?:input|include)\{([^{}]+)\}', include, text)
    active.remove(path)
    return text


def verify(tex_path: Path, log_path: Path) -> dict:
    text = read_tex_tree(tex_path)
    log = log_path.read_text(errors='replace')
    errors = []
    labels = [s for s in re.findall(r'\\label\{([^}]+)\}', text) if '#' not in s]
    labels += ['pr:' + s for s in re.findall(r'\\BookProblem\{[^{}]*\}\{([^{}]+)\}', text)]
    duplicates = [s for s, n in Counter(labels).items() if n > 1]
    if duplicates:
        errors.append('重复标签：' + ', '.join(duplicates))
    targets = re.findall(r'\\(?:ref|pageref)\{([^}]+)\}', text)
    targets += re.findall(r'\\hyperref\[([^]]+)\]', text)
    absent = sorted(set(targets) - set(labels))
    if absent:
        errors.append('缺少引用目标：'+', '.join(absent))
    checks = {
        '编译错误': r'^!|^.*?:\d+: (?:LaTeX|Package|Undefined control sequence|Missing)',
        '缺字形': r'Missing character:',
        '重复引用或 PDF 锚点': r'multiply defined|duplicate destination',
        '未完成交叉引用': r'undefined references|Reference .* undefined|Rerun to get cross-references right|Rerun to get /PageLabels|Rerun to get outlines right|rerunfilecheck Warning: File .* has changed',
    }
    for label, pattern in checks.items():
        count = len(re.findall(pattern, log, re.M))
        if count:
            errors.append(f'{label}：{count}')
    if 'Output written on' not in log:
        errors.append('编译未产出 PDF')
    overfull = re.findall(r'Overfull \\[hv]box \(([^)]+)\).*?(?:at lines? ([\d-]+))?', log)
    if overfull:
        errors.append(f'版面溢出：{len(overfull)}')
    return {'errors': errors, 'labels': len(labels), 'references': len(targets), 'overfull': len(overfull), 'verdict': 'fail' if errors else 'pass'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--tex', type=Path, default=Path('build/book.tex'))
    ap.add_argument('--log', type=Path, default=Path('build/book.log'))
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    report = verify(args.tex, args.log)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    name = 'verification.json' if args.tex.stem == 'book' else args.tex.stem + '-verification.json'
    args.tex.with_name(name).write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    return bool(report['errors'])

if __name__ == '__main__':
    raise SystemExit(main())
