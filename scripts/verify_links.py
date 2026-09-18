#!/usr/bin/env python3
"""Verify real PDF named destinations, including links between the two volumes."""
from pathlib import Path
import json
from pypdf import PdfReader
from booklib import ROOT


def verify(directory: Path) -> dict:
    readers = {name: PdfReader(directory/name) for name in ('book.pdf','methods.pdf')}
    targets = {name: set(reader.named_destinations) for name, reader in readers.items()}
    errors = []
    remote = 0
    for name, reader in readers.items():
        for page_number, page in enumerate(reader.pages, 1):
            for ref in page.get('/Annots', []):
                action = ref.get_object().get('/A')
                if not action or action.get('/S') != '/GoToR':
                    continue
                remote += 1
                file = action.get('/F')
                if not isinstance(file, str):
                    file = file.get('/F') if file else None
                destination = action.get('/D')
                if file not in targets or not isinstance(destination, str) or destination not in targets[file]:
                    errors.append(f'{name}:{page_number}: 无效跨卷目标 {file}#{destination}')
    return dict(errors=errors, external_links=remote,
                pages={name:len(reader.pages) for name,reader in readers.items()},
                verdict='fail' if errors else 'pass')


if __name__ == '__main__':
    result = verify(ROOT/'build')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    (ROOT/'build/cross-volume-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    raise SystemExit(bool(result['errors']))
