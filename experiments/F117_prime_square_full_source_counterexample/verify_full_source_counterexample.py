#!/usr/bin/env python3
"""Exact full-F116-source check for a prime-square counterexample."""

from __future__ import annotations

import hashlib
import json
import math
import struct
import sys
import time
from pathlib import Path


sys.dont_write_bytecode = True

P = 1_000_000_007
N = P * P


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


def integer_nth_root(value: int, exponent: int) -> int:
    low = 1 << ((value.bit_length() - 1) // exponent)
    high = 1 << ((value.bit_length() + exponent - 1) // exponent)
    while low + 1 < high:
        middle = (low + high) // 2
        if pow(middle, exponent) <= value:
            low = middle
        else:
            high = middle
    return low


_power_cache: dict[int, tuple[int, int]] = {}


def maximal_perfect_power(value: int) -> tuple[int, int]:
    cached = _power_cache.get(value)
    if cached is not None:
        return cached
    for exponent in range(value.bit_length() - 1, 1, -1):
        base = integer_nth_root(value, exponent)
        if pow(base, exponent) == value:
            result = (base, exponent)
            _power_cache[value] = result
            return result
    result = (value, 1)
    _power_cache[value] = result
    return result


def deterministic_gcd_basis(
    values: list[int],
) -> list[tuple[int, dict[int, int]]]:
    stack = [(value, {index: 1}) for index, value in enumerate(values) if value > 1]
    basis: list[tuple[int, dict[int, int]]] = []
    while stack:
        value, signature = stack.pop()
        if value == 1:
            continue
        base, exponent = maximal_perfect_power(value)
        if exponent > 1:
            value = base
            signature = {
                index: multiplicity * exponent
                for index, multiplicity in signature.items()
            }
        for index, (other_value, other_signature) in enumerate(basis):
            common = math.gcd(value, other_value)
            if common == 1:
                continue
            basis.pop(index)
            if value == other_value:
                merged = signature.copy()
                for endpoint, multiplicity in other_signature.items():
                    merged[endpoint] = merged.get(endpoint, 0) + multiplicity
                stack.append((value, merged))
            else:
                stack.extend(
                    [
                        (common, signature),
                        (value // common, signature),
                        (common, other_signature),
                        (other_value // common, other_signature),
                    ]
                )
            break
        else:
            basis.append((value, signature))
    basis.sort(key=lambda item: item[0])
    return basis


def hash_pairs(pairs: list[tuple[int, int]]) -> str:
    digest = hashlib.sha256()
    for left, right in pairs:
        digest.update(left.to_bytes(8, "big"))
        digest.update(right.to_bytes(8, "big"))
    return digest.hexdigest()


def main() -> int:
    started = time.monotonic()
    output_path = Path(__file__).resolve().parent / "OUTPUT.json"
    n = N.bit_length()
    bound = n * n

    if not is_prime_by_trial_division(P):
        raise AssertionError("P is not prime")
    if P % 4 != 3 or N != P * P:
        raise AssertionError("prime-square metadata is inconsistent")
    trial_nonunits = [
        value for value in range(2, bound + 1) if math.gcd(value, N) != 1
    ]
    if trial_nonunits:
        raise AssertionError(f"trial-hard check failed: {trial_nonunits}")
    print(
        f"prime-square input: P={P} N={N} n={n} B={bound}; "
        "primality and trial-hardness are exact",
        flush=True,
    )

    seed_endpoints: list[int] = []
    for seed in range(2, n + 1):
        seed_endpoints.extend((seed, pow(seed, -1, N)))
    basis = deterministic_gcd_basis(seed_endpoints)
    blocks = [block for block, _ in basis]
    if any(
        math.gcd(blocks[left], blocks[right]) != 1
        for left in range(len(blocks))
        for right in range(left + 1, len(blocks))
    ):
        raise AssertionError("seed basis is not pairwise coprime")
    reconstructed = [1] * len(seed_endpoints)
    for block, signature in basis:
        if maximal_perfect_power(block)[1] != 1:
            raise AssertionError("seed basis contains a perfect power")
        if math.gcd(block, N) != 1:
            raise AssertionError("seed basis contains a nonunit")
        for endpoint, multiplicity in signature.items():
            reconstructed[endpoint] *= pow(block, multiplicity)
    if reconstructed != seed_endpoints:
        raise AssertionError("seed basis does not reconstruct the endpoints")

    frozen_pairs: list[tuple[int, int]] = []
    for seed_index in range(n - 1):
        left_endpoint = 2 * seed_index
        right_endpoint = left_endpoint + 1
        support = [
            block
            for block, signature in basis
            if signature.get(left_endpoint, 0)
            + signature.get(right_endpoint, 0)
            > 0
        ]
        if not support:
            raise AssertionError("seed relation has empty basis support")
        frozen_pairs.append((support[0], 1 if len(support) == 1 else support[1]))
    print(
        f"seed basis blocks={len(basis)} frozen_pairs={len(frozen_pairs)}",
        flush=True,
    )

    source_hash = hashlib.sha256()
    attempts = 0
    next_progress = 1_000_000
    screen_counts = {
        "minus_unit": 0,
        "minus_improper": 0,
        "minus_proper": 0,
        "plus_unit": 0,
        "plus_improper": 0,
        "plus_proper": 0,
    }
    nonunit_screens: list[dict[str, int | str]] = []

    def attempt(
        residue: int,
        kind: int,
        pair_index: int,
        exponent: int,
        orientation: int,
    ) -> None:
        nonlocal attempts, next_progress
        if not 1 <= residue < N or math.gcd(residue, N) != 1:
            raise AssertionError(f"attempted residue {residue} is not a canonical unit")
        attempts += 1
        source_hash.update(
            struct.pack(">BIHBQ", kind, pair_index, exponent, orientation, residue)
        )

        residue_mod_p = residue % P
        if residue_mod_p in (1, P - 1):
            divisor = math.gcd(residue * residue - 1, N)
            classification = "improper" if divisor == N else "proper"
            screen_counts[f"minus_{classification}"] += 1
            nonunit_screens.append(
                {
                    "attempt": attempts,
                    "kind": kind,
                    "pair_index": pair_index,
                    "exponent": exponent,
                    "orientation": orientation,
                    "residue": residue,
                    "sign": "minus",
                    "gcd": divisor,
                    "classification": classification,
                }
            )
        else:
            screen_counts["minus_unit"] += 1

        if (residue_mod_p * residue_mod_p + 1) % P == 0:
            divisor = math.gcd(residue * residue + 1, N)
            classification = "improper" if divisor == N else "proper"
            screen_counts[f"plus_{classification}"] += 1
            nonunit_screens.append(
                {
                    "attempt": attempts,
                    "kind": kind,
                    "pair_index": pair_index,
                    "exponent": exponent,
                    "orientation": orientation,
                    "residue": residue,
                    "sign": "plus",
                    "gcd": divisor,
                    "classification": classification,
                }
            )
        else:
            screen_counts["plus_unit"] += 1

        if attempts >= next_progress:
            print(f"progress attempts={attempts}", flush=True)
            next_progress += 1_000_000

    for seed_index, seed in enumerate(range(2, n + 1)):
        attempt(seed, 0, seed_index, 0, 0)
    seed_attempts = attempts

    for pair_index, (left, right) in enumerate(frozen_pairs):
        left_power = 1
        right_power = 1
        for exponent in range(bound + 1):
            attempt((left_power * right) % N, 1, pair_index, exponent, 0)
            attempt((left * right_power) % N, 1, pair_index, exponent, 1)
            left_power = (left_power * left) % N
            right_power = (right_power * right) % N
    frozen_attempts = attempts - seed_attempts
    print(f"frozen layer complete: attempts={frozen_attempts}", flush=True)

    menu_start = attempts
    menu_pair_count = 0
    for left in range(2, n):
        for right in range(left + 1, n + 1):
            left_power = 1
            right_power = 1
            for exponent in range(bound + 1):
                attempt((left_power * right) % N, 2, menu_pair_count, exponent, 0)
                attempt((left * right_power) % N, 2, menu_pair_count, exponent, 1)
                left_power = (left_power * left) % N
                right_power = (right_power * right) % N
            menu_pair_count += 1
    menu_attempts = attempts - menu_start

    expected_frozen_attempts = (n - 1) * 2 * (bound + 1)
    expected_menu_pairs = (n - 1) * (n - 2) // 2
    expected_menu_attempts = expected_menu_pairs * 2 * (bound + 1)
    expected_attempts = (n - 1) + expected_frozen_attempts + expected_menu_attempts
    if (
        frozen_attempts != expected_frozen_attempts
        or menu_pair_count != expected_menu_pairs
        or menu_attempts != expected_menu_attempts
        or attempts != expected_attempts
    ):
        raise AssertionError("full-source enumeration count is inconsistent")
    if screen_counts["minus_proper"] or screen_counts["plus_proper"]:
        raise AssertionError(f"proper direct screen found: {nonunit_screens}")

    elapsed = time.monotonic() - started
    result = {
        "status": "PASS",
        "counterexample": {
            "p": P,
            "N": N,
            "N_equals_p_squared": N == P * P,
            "p_prime_by_complete_trial_division": True,
            "p_mod_4": P % 4,
            "bit_length": n,
            "bound": bound,
            "trial_gcd_range": [2, bound],
            "trial_nonunit_count": len(trial_nonunits),
        },
        "seed_basis": {
            "endpoint_count": len(seed_endpoints),
            "block_count": len(basis),
            "pairwise_coprime": True,
            "perfect_power_free": True,
            "exact_endpoint_reconstruction": True,
            "frozen_pair_count": len(frozen_pairs),
            "frozen_pair_sha256": hash_pairs(frozen_pairs),
            "frozen_pairs": [[left, right] for left, right in frozen_pairs],
        },
        "full_source": {
            "seed_attempts": seed_attempts,
            "frozen_attempts": frozen_attempts,
            "menu_pair_count": menu_pair_count,
            "menu_attempts": menu_attempts,
            "total_attempts": attempts,
            "all_attempt_sequence_sha256": source_hash.hexdigest(),
            "deduplication_note": (
                "Every attempted occurrence was screened. This is stronger than "
                "F116, which skips a duplicate before screening it."
            ),
        },
        "direct_sign_screens_over_all_attempt_occurrences": screen_counts,
        "nonunit_sign_screens": nonunit_screens,
        "proved_decoder_obstruction": (
            "For odd prime p, x^2 = 1 (mod p^2) implies x = +1 or -1 "
            "(mod p^2), because gcd(x-1,x+1) divides 2. Hence every "
            "normalized root of every exact-value dependency is global."
        ),
        "dependency_scope": (
            "The obstruction does not assert that the exact-value kernel is "
            "zero or nonzero. It proves that any dependency that exists has "
            "global normalized root."
        ),
        "elapsed_seconds": elapsed,
    }
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        f"PASS full source: attempts={attempts} proper_screens=0 "
        f"elapsed_seconds={elapsed:.6f}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
