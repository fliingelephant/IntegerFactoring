#!/usr/bin/env python3
"""Factor-aware audit of already-frozen RECONSTRUCT_public artifacts.

This file is deliberately separate from RECONSTRUCT_public.py.  It is created
and run only after RECONSTRUCT_FREEZE.sha256 fixes the public source, output,
and log.  Unlike the public replay, this audit may use the factors exposed by
the final public gcds and may test their primality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import signal
import sys
from pathlib import Path


N = 202_537_109
P = 10_267
Q = 19_727


class HardTimeout(RuntimeError):
    pass


def is_prime_by_trial_division(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--timeout-seconds", type=int, default=60)
    args = parser.parse_args()

    def timeout_handler(_signum: int, _frame: object) -> None:
        raise HardTimeout(f"hard timeout after {args.timeout_seconds} seconds")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, args.timeout_seconds)
    lines: list[str] = []
    failures: list[str] = []

    def record(message: str) -> None:
        print(message)
        lines.append(message)

    def require(condition: bool, message: str) -> None:
        if not condition:
            failures.append(message)

    try:
        manifest_path = args.directory / "RECONSTRUCT_FREEZE.sha256"
        manifest: dict[str, str] = {}
        for line in manifest_path.read_text(encoding="utf-8").splitlines():
            digest, filename = line.split(maxsplit=1)
            manifest[filename] = digest
        actual_hashes = {
            filename: file_sha256(args.directory / filename) for filename in manifest
        }
        require(actual_hashes == manifest, "a frozen public artifact hash changed")
        record(f"freeze hashes verified={actual_hashes == manifest}")

        public = json.loads((args.directory / "RECONSTRUCT_public.json").read_text(encoding="utf-8"))
        require(public["status"] == "PASS", "public replay status is not PASS")
        require(public["claim_failures"] == [], "public replay has claim failures")
        require(public["source_sha256"] == manifest["RECONSTRUCT_public.py"], "embedded source hash differs")

        require(P * Q == N, "reported proper gcds do not multiply to N")
        require(is_prime_by_trial_division(P), f"{P} is not prime")
        require(is_prime_by_trial_division(Q), f"{Q} is not prime")
        record(f"factor audit: {N}={P}*{Q}; both factors prime=True")

        decoder = public["decoder"]
        diagnostic = public["diagnostic"]
        main_matches = [
            vector
            for vector in decoder["useful_kernel_vectors"]
            if vector["support"] == 166
            and vector["root_mod_N"] == 132_013_085
            and vector["gcd_minus"] == Q
            and vector["gcd_plus"] == P
        ]
        require(len(main_matches) == 1, "main witness is not unique in the reported matching class")

        online = diagnostic["first_useful"]
        require(online["ordinal"] == 5_616, "online witness ordinal differs")
        require(online["distinct_support"] == 166, "online witness support differs")
        require(online["root_mod_N"] == 70_524_024, "online witness residue differs")
        require(online["gcd_minus"] == P and online["gcd_plus"] == Q, "online gcds differ")

        residues = {
            "main": (132_013_085, Q, P),
            "online": (70_524_024, P, Q),
        }
        crt_audit: dict[str, dict[str, int]] = {}
        for label, (root, minus_expected, plus_expected) in residues.items():
            minus = math.gcd(root - 1, N)
            plus = math.gcd(root + 1, N)
            require(pow(root, 2, N) == 1, f"{label} residue is not a square root of 1")
            require(minus == minus_expected and plus == plus_expected, f"{label} CRT signs differ")
            crt_audit[label] = {
                "root_mod_N": root,
                "square_mod_N": pow(root, 2, N),
                "gcd_minus": minus,
                "gcd_plus": plus,
                "root_mod_P": root % P,
                "root_mod_Q": root % Q,
            }
        record(f"CRT audit={json.dumps(crt_audit, sort_keys=True)}")

        require(public["trial_screen"]["proper_hits"] == [], "trial screen contains a factor")
        require(public["seeds"]["proper_sign_hits"] == [], "a seed sign screen contains a factor")
        require(public["trajectories"]["proper_sign_hits"] == [], "a trajectory sign screen contains a factor")
        require(
            diagnostic["small_support_useful_dependencies"]
            == {"support_1": 0, "support_2": 0, "support_3": 0},
            "small-support useful dependency reported",
        )

        result = {
            "status": "PASS" if not failures else "FAIL",
            "failures": failures,
            "freeze_hashes": actual_hashes,
            "factorization": {
                "N": N,
                "P": P,
                "Q": Q,
                "product_verified": P * Q == N,
                "P_prime": is_prime_by_trial_division(P),
                "Q_prime": is_prime_by_trial_division(Q),
            },
            "main_matching_vectors": main_matches,
            "online_witness": online,
            "crt_audit": crt_audit,
        }
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        record(f"strict audit result={result['status']}; failures={len(failures)}")
        args.log.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return 0 if not failures else 1
    except HardTimeout as error:
        record(f"strict audit result=FAIL; {error}")
        args.log.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return 124
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


if __name__ == "__main__":
    sys.exit(main())
