#!/usr/bin/env python3
"""Deterministic F120 search for one trial-hard semiprime REUSE falsifier."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from sage.all import ZZ


def next_proven_prime(value: int) -> int:
    candidate = value if value & 1 else value + 1
    while not bool(ZZ(candidate).is_prime(proof=True)):
        candidate += 2
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registration", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    registration = json.loads(Path(args.registration).read_text())
    p = next_proven_prime(int(registration["p_start"]))
    ell = next_proven_prime(int(registration["ell_start"]))
    trace = hashlib.sha256()
    found: dict[str, object] | None = None

    for ordinal in range(1, int(registration["pair_cap"]) + 1):
        modulus = p * ell
        bit_length = modulus.bit_length()
        trial_bound = bit_length * bit_length
        private_prime = (modulus + 1) // 2
        trace.update(f"{ordinal}:{p}:{ell}:{modulus}:{private_prime}\n".encode())
        if (
            modulus % 4 == 1
            and p != ell
            and p > trial_bound
            and ell > trial_bound
            and bool(ZZ(private_prime).is_prime(proof=True))
        ):
            found = {
                "ordinal": ordinal,
                "p": p,
                "ell": ell,
                "N": modulus,
                "bit_length": bit_length,
                "trial_bound": trial_bound,
                "private_prime": private_prime,
                "seed": 2,
                "seed_inverse": private_prime,
                "exact_value": modulus + 1,
                "carry": 1,
                "checks": {
                    "p_proven_prime": bool(ZZ(p).is_prime(proof=True)),
                    "ell_proven_prime": bool(ZZ(ell).is_prime(proof=True)),
                    "private_proven_prime": bool(
                        ZZ(private_prime).is_prime(proof=True)
                    ),
                    "distinct_semiprime": p != ell and p * ell == modulus,
                    "trial_hard": min(p, ell) > trial_bound,
                    "inverse_identity": 2 * private_prime == modulus + 1,
                    "large_row": 2 * private_prime > modulus - 1,
                },
            }
            break
        p = next_proven_prime(p + 2)
        ell = next_proven_prime(ell + 2)

    payload = {
        "status": "FOUND" if found is not None else "CAP_NO_CANDIDATE",
        "registration": registration,
        "pairs_tested": ordinal,
        "candidate_trace_sha256": trace.hexdigest(),
        "candidate": found,
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": payload["status"], "pairs_tested": ordinal}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
