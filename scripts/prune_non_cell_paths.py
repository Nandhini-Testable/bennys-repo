#!/usr/bin/env python
"""Remove upstream tool corpora if they appear on the branch root.

Those trees are not part of this evaluation cell. They inflate git-churn and
taxonomy evidence (Test Case Maintenance, lint drill-down) without helping the
29 wired tools, which use packages/domain, tests/, and tools/ runners only.
"""
from __future__ import print_function

import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAMES = (
    "Tool Triggering (Tool Github Test data)",
    "Tool Triggering (Synthetic Data)",
    "Tool Clean (Synthetic Data)",
    "Tool Invalid (Synthetic Data)",
)


def main():
    removed = []
    for name in NAMES:
        path = os.path.join(ROOT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
            removed.append(name)
    if removed:
        print("prune_non_cell_paths: removed", ", ".join(removed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
