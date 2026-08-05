#!/usr/bin/env sage
"""Benchmark one factor-free global row construction in the cyclic ring."""

import hashlib
import json
import os
import time
from pathlib import Path


N = 20000000499999937
r = 2953
a = 1

started = time.monotonic()
base = Integers(N)
polynomials = PolynomialRing(base, "X")
X = polynomials.gen()
modulus = X**r - 1
residue = power_mod(X + a, N, modulus) - power_mod(X, N, modulus) - a
residue = residue.mod(modulus)
coefficients = [int(residue[i]) for i in range(r)]
elapsed = time.monotonic() - started
payload = {
    "N": int(N),
    "r": int(r),
    "a": int(a),
    "elapsed_seconds": float(elapsed),
    "nonzero": int(sum(value != 0 for value in coefficients)),
    "coefficient_sha256": hashlib.sha256(
        b"".join(value.to_bytes(8, "little") for value in coefficients)
    ).hexdigest(),
    "first_16": coefficients[:16],
}
run_dir = Path(os.environ["F04_RECONSTRUCT_RUN_DIR"])
(run_dir / "result.json").write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(payload, sort_keys=True))
