#!/usr/bin/env python3
"""Record Sage matrix backends and advertised determinant/rank interfaces."""

import inspect
import json
import os
from pathlib import Path

from sage.all import GF, matrix


payload = {}
for prime in (271, 293, 100000007, 199999991):
    sample = matrix(GF(prime), [[1, 2], [3, 5]])
    payload[str(prime)] = {
        "class": str(type(sample)),
        "det_signature": str(inspect.signature(sample.det)),
        "rank_signature": str(inspect.signature(sample.rank)),
        "echelonize_signature": str(inspect.signature(sample.echelonize)),
        "solve_right_signature": str(inspect.signature(sample.solve_right)),
        "det_doc": inspect.getdoc(sample.det),
    }

run_dir = Path(os.environ["F04_RECONSTRUCT_RUN_DIR"])
(run_dir / "sage_matrix_interfaces.json").write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(payload, sort_keys=True))
