#!/usr/bin/env python3
"""Run all required source checks; every failure blocks the build."""
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parent.parent
for command in ([sys.executable, 'scripts/test_pipeline.py'],
                [sys.executable, 'scripts/check_sources.py'],
                [sys.executable, 'scripts/build_book.py'],
                [sys.executable, 'scripts/build_methods.py']):
    result = subprocess.run(command, cwd=ROOT)
    if result.returncode:
        raise SystemExit(result.returncode)
print('全部源文件检查通过；下一步运行 make pdf 编译并检查成品。')
