#!/usr/bin/env python3
"""Authoritative driver for the F14-M02 mixed-handed finite certificate.

The enumeration implementation is the preserved F14-M01 source.  This driver
records hashes of both itself and that dependency.  The run is finite evidence
only; every unbounded statement in RESULT.md is proved symbolically.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from F14_M01_exact_sections import summarize


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--inputs", nargs="+", required=True, type=int)
    args = parser.parse_args()
    source = Path(__file__)
    dependency = source.with_name("F14_M01_exact_sections.py")
    payload = {
        "family": "F14",
        "run": "F14-M02",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "enumeration_dependency": str(dependency),
        "enumeration_dependency_sha256": hashlib.sha256(dependency.read_bytes()).hexdigest(),
        "normalization": "lexicographically least doubled coordinate tuple",
        "results": [summarize(value) for value in args.inputs],
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"run": "F14-M02", "status": "completed", "inputs": args.inputs}))


if __name__ == "__main__":
    main()
