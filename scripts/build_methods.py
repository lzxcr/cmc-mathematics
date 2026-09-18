#!/usr/bin/env python3
"""Build the standalone methods volume and its cross-volume destination index."""
from pathlib import Path
import json
import os
from booklib import ROOT, HEADING, load_book, load_methods, method_texts, inline
from build_book import markdown_chapter


def build(out: Path = ROOT/'build/methods.tex') -> dict:
    book = load_methods()
    problems = load_book()
    targets = {'pr:' + i['id']: 'book.pdf' for p in problems['parts'] for c in p['chapters'] for i in c['items']}
    targets.update({'exam:' + c['id']: 'book.pdf' for p in problems['parts'] for c in p['chapters']})
    for _, text in method_texts(book):
        targets.update({m[3]: '' for m in HEADING.finditer(text) if m[3]})
    out.parent.mkdir(parents=True, exist_ok=True)
    directory = out.parent/'methods-chapters'
    directory.mkdir(exist_ok=True)
    tex = [r'''% !TEX program = lualatex
% Generated from src/methods/book.json.
\input{src/layout.tex}
\SynapticTitle{数学竞赛的方法与结构}
\SynapticShortTitle{数学竞赛的方法与结构}
\SynapticHeader{分析估计\quad ·\quad 代数结构\quad ·\quad 应用}
\SynapticSubtitle{内篇与外篇\quad ·\quad 从余项控制到结构理论}
\SynapticSubject{数学竞赛备考方法与理论}
\setcounter{tocdepth}{1}
\begin{document}
\SynapticMakeTitle
\SynapticFrontMatter''']
    def include(path, content):
        path.write_text(content.rstrip()+'\n')
        tex.append(r'\input{' + Path(os.path.relpath(path, ROOT)).as_posix() + '}')
    include(directory/'frontmatter.tex', markdown_chapter(book['path'].parent/'frontmatter.md', targets))
    tex.append(r'\input{src/credits.tex}')
    tex += [r'\SynapticBookContents', r'\SynapticMainMatter', r'\setcounter{secnumdepth}{0}']
    for part in book['parts']:
        tex.append(r'\part{' + inline(part['title']) + '}')
        for chapter in part['chapters']:
            include(directory/(chapter['id']+'.tex'), markdown_chapter(chapter['path'], targets))
    tex.append(r'\end{document}')
    out.write_text('\n\n'.join(tex)+'\n')
    stats = dict(parts=len(book['parts']), chapters=sum(len(p['chapters']) for p in book['parts']),
                 anchors=sum(not v for v in targets.values()), external_targets=sum(bool(v) for v in targets.values()))
    out.with_suffix('.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
    out.with_name('methods-verification.json').unlink(missing_ok=True)
    out.with_name('cross-volume-verification.json').unlink(missing_ok=True)
    return stats


if __name__ == '__main__':
    print(json.dumps(build(),ensure_ascii=False,indent=2))
