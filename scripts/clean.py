#!/usr/bin/env python3
"""Remove generated files while keeping finished PDFs."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent


def clean_build(directory: Path) -> None:
    if not directory.is_dir() or directory.is_symlink():
        return
    for path in directory.iterdir():
        if path.is_symlink():
            path.unlink()
        elif path.is_file() and path.suffix.lower() == '.pdf':
            continue
        elif path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()


if __name__ == '__main__':
    clean_build(ROOT/'build')
    shutil.rmtree(ROOT/'scripts/__pycache__', ignore_errors=True)
    print('已清理构建中间文件，保留 PDF 成品。')
