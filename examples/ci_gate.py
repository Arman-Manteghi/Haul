#!/usr/bin/env python3
"""Run Haul as a local, offline secrets-exposure gate.

Install first: pip install haul-scanner
Run in a project checkout: python examples/ci_gate.py

Haul scans only the given working tree in this example and never prints secret
values. Findings rated High or Critical cause a non-zero exit status.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    executable = shutil.which("haul")
    if executable is None:
        print("Haul is not installed. Run: pip install haul-scanner", file=sys.stderr)
        return 64

    project = Path.cwd()
    command = [
        executable,
        "--only",
        "dotenv,sensitive-files",
        "--min-severity",
        "high",
        "--fail-on",
        "high",
        "-f",
        "terminal",
        "-q",
        str(project),
    ]
    return subprocess.run(command, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
