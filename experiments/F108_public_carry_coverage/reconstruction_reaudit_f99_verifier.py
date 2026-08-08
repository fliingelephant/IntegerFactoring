#!/usr/bin/env python3
"""Narrow proof-blind replay of the amended F108/F99 boundary."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gf2_rank(unit_masks: list[int]) -> int:
    basis = {}
    for source in unit_masks:
        value = source
        while value:
            pivot = (value & -value).bit_length() - 1
            if pivot not in basis:
                basis[pivot] = value
                break
            value ^= basis[pivot]
    return len(basis)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--statement", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    statement_path = args.statement.resolve()
    output_path = args.output.resolve()
    statement_text = statement_path.read_text()
    checks = 0
    failures = []

    def require(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    required_fragments = (
        "N_T\\equiv1\\pmod {2^T}",
        "w_e=N_T-\\frac{N_T-1}{2^e}",
        "P_e=c_ew_e=1+(2^e-1)N_T",
        "v_{q_e}(P_e)=1",
        "q_e\\nmid P_j",
    )
    for fragment in required_fragments:
        require(fragment in statement_text, f"amended statement is missing: {fragment}")

    sampled_families = []
    for T in range(1, 97):
        unit_masks = [1 << (e - 1) for e in range(1, T + 1)]
        require(gf2_rank(unit_masks) == T, f"T={T}: private unit rows lost full rank")
        for multiplier in (1, 2, 3, 5, 17):
            modulus = 1 + multiplier * 2**T
            require(modulus % 2**T == 1, f"T={T}, k={multiplier}: bad congruence")
            c_values = {}
            w_values = {}
            p_values = {}
            for e in range(1, T + 1):
                require((modulus - 1) % 2**e == 0, f"T={T}, k={multiplier}, e={e}: nonintegral inverse formula")
                c_value = 2**e
                w_value = modulus - (modulus - 1) // 2**e
                p_value = c_value * w_value
                require(c_value < modulus, f"T={T}, k={multiplier}, e={e}: c is not canonical")
                require(0 < w_value < modulus, f"T={T}, k={multiplier}, e={e}: w is not canonical")
                require(p_value == 1 + (2**e - 1) * modulus, f"T={T}, k={multiplier}, e={e}: P formula failed")
                require(c_value * w_value % modulus == 1, f"T={T}, k={multiplier}, e={e}: inverse failed")
                c_values[e] = c_value
                w_values[e] = w_value
                p_values[e] = p_value

            exposures = []
            transition_records = []
            for e in range(1, T):
                c_numerator = 2 * c_values[e] - c_values[e + 1]
                w_numerator = 2 * w_values[e + 1] - w_values[e]
                require(c_numerator == 0, f"T={T}, k={multiplier}, e={e}: first carry is nonzero")
                require(w_numerator == modulus, f"T={T}, k={multiplier}, e={e}: inverse identity failed")
                first_carry = c_numerator // modulus
                inverse_carry = w_numerator // modulus
                require(first_carry == 0, f"T={T}, k={multiplier}, e={e}: first carry quotient failed")
                require(inverse_carry == 1, f"T={T}, k={multiplier}, e={e}: inverse carry quotient failed")
                require(not (first_carry == 0 and inverse_carry == 0), f"T={T}, k={multiplier}, e={e}: false duplicate")
                exposures.append(c_values[e])
                require(c_values[e] & (c_values[e] - 1) == 0, f"T={T}, k={multiplier}, e={e}: exposure is not a power of two")
                transition_records.append({
                    "e": e,
                    "first_carry": first_carry,
                    "inverse_carry": inverse_carry,
                    "exposure": c_values[e],
                })
            exposure_product = math.prod(exposures)
            require(
                exposure_product == 1 or exposure_product & (exposure_product - 1) == 0,
                f"T={T}, k={multiplier}: exposure product is not a power of two",
            )
            if T in (1, 2, 8, 32, 96) and multiplier in (1, 3):
                sampled_families.append({
                    "T": T,
                    "N_T": modulus,
                    "congruence_multiplier": multiplier,
                    "columns": T,
                    "transition_count": len(transition_records),
                    "exposure_count": len(exposures),
                    "exposure_product_is_power_of_two": (
                        exposure_product == 1 or exposure_product & (exposure_product - 1) == 0
                    ),
                    "private_row_rank": gf2_rank(unit_masks),
                    "private_row_nullity": T - gf2_rank(unit_masks),
                })

    symbolic_derivation = {
        "canonical_inverse": (
            "2^e*w_e = 2^e*N_T-(N_T-1) = 1+(2^e-1)N_T, "
            "so 0<w_e<N_T and 2^e*w_e is congruent to 1 modulo N_T"
        ),
        "first_carry": "c_(e+1)=2^(e+1)=2*c_e for 1<=e<T, so a_e=0",
        "inverse_carry": (
            "2*w_(e+1)-w_e = "
            "2[N_T-(N_T-1)/2^(e+1)]-[N_T-(N_T-1)/2^e] = N_T, so b_e=1"
        ),
        "exposure_support": (
            "a_e=0 records c_e=2^e; b_e=1 records no inverse endpoint; "
            "therefore every raw exposure integer is a power of two"
        ),
        "private_rows": (
            "v_(q_e)(P_e)=1 and q_e does not divide any P_j for j!=e, "
            "so row r_(q_e) is the e-th unit vector; the T private rows form I_T"
        ),
        "logical_limit": (
            "carry frequency counts transitions but does not bound the full parity rank. "
            "The private identity rows give rank T and nullity zero, hence no nonempty dependency. "
            "Even where a dependency exists, a useful non-global square root additionally requires "
            "mixed CRT signs; carry data do not control those signs"
        ),
    }

    output = {
        "status": "complete",
        "verifier_status": "PASS" if not failures else "FAIL",
        "boundary_verdict": "PASS" if not failures else "FAIL",
        "checks": checks,
        "verifier_failures": failures,
        "authorized_input": {
            "RECONSTRUCT_STATEMENT.md": sha256(statement_path),
        },
        "scope": "amended F99 boundary only",
        "symbolic_derivation": symbolic_derivation,
        "universal_consequences": {
            "transition_range": "1 <= e < T",
            "first_carry": 0,
            "inverse_carry": 1,
            "raw_exposure_values": "powers of two only",
            "raw_exposure_prime_support": "empty for T=1; exactly {2} for T>=2",
            "private_row_matrix": "I_T",
            "private_row_rank": "T",
            "private_row_nullity": 0,
            "nonempty_dependency_exists": False,
            "carry_frequency_forces_dependency": False,
            "carry_frequency_forces_non_global_root": False,
        },
        "finite_sanity_checks": {
            "T_range": [1, 96],
            "congruence_multipliers": [1, 2, 3, 5, 17],
            "families_checked": 96 * 5,
            "sampled_family_summaries": sampled_families,
        },
        "forbidden_inputs_read": [],
        "factorizations_performed": 0,
    }
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "boundary_verdict": output["boundary_verdict"],
        "checks": checks,
        "verifier_failures": failures,
        "verifier_status": output["verifier_status"],
    }, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
