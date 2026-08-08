#!/usr/bin/env python3
"""Factor-free carry-coverage replay for the fixed F98 circuit."""

from __future__ import annotations

import hashlib
import json
import math
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PUBLIC_PATH = ROOT / "experiments/F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parity_coprime_basis(initial_entries: list[tuple[int, int]]):
    stable: list[tuple[int, int]] = []
    work = [(value, mask) for value, mask in initial_entries if value > 1 and mask]
    refinements = 0
    gcd_tests = 0
    while work:
        value, mask = work.pop()
        for index, (old_value, old_mask) in enumerate(stable):
            gcd_tests += 1
            common = math.gcd(value, old_value)
            if common == 1:
                continue
            stable.pop(index)
            refinements += 1
            for new_value, new_mask in (
                (common, mask ^ old_mask),
                (value // common, mask),
                (old_value // common, old_mask),
            ):
                if new_value > 1 and new_mask:
                    work.append((new_value, new_mask))
            break
        else:
            stable.append((value, mask))

    product = 1
    for value, _ in stable:
        assert math.gcd(value, product) == 1
        product *= value
    return stable, refinements, gcd_tests


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def exposure_product(
    modulus: int,
    bound: int,
    keys: list[tuple[int, int, int, str]],
):
    exposures: list[int] = []
    two_zero = 0
    no_zero = 0
    c_zero = 0
    w_zero = 0
    for _, u_value, v_value, orientation in keys:
        if orientation == "u_power_times_v":
            multiplier = u_value
            fixed = v_value
        else:
            multiplier = v_value
            fixed = u_value
        states = []
        power = 1
        for _ in range(bound + 1):
            c_value = power * fixed % modulus
            states.append((c_value, pow(c_value, -1, modulus)))
            power = power * multiplier % modulus
        for exponent in range(bound):
            c_value, w_value = states[exponent]
            next_c, next_w = states[exponent + 1]
            c_numerator = multiplier * c_value - next_c
            w_numerator = multiplier * next_w - w_value
            assert c_numerator % modulus == 0
            assert w_numerator % modulus == 0
            first = c_numerator // modulus
            second = w_numerator // modulus
            assert 0 <= first < multiplier
            assert 0 <= second < multiplier
            if first == 0 and second == 0:
                two_zero += 1
                assert c_value * w_value == next_c * next_w
                continue
            if first == 0:
                exposures.append(c_value)
                c_zero += 1
            if second == 0:
                exposures.append(next_w)
                w_zero += 1
            if first != 0 and second != 0:
                no_zero += 1
    return math.prod(exposures), {
        "oriented_trajectories": len(keys),
        "transitions": len(keys) * bound,
        "exposure_integers": len(exposures),
        "c_zero_transitions": c_zero,
        "w_zero_transitions": w_zero,
        "two_zero_transitions_excluded": two_zero,
        "no_zero_transitions": no_zero,
    }


def exposed_rows(blocks: list[tuple[int, int]], exposure: int):
    rows = []
    saturation_gcds = 0
    supported_blocks = 0
    for value, mask in blocks:
        remaining = value
        supported = 1
        while True:
            common = math.gcd(remaining, exposure)
            saturation_gcds += 1
            if common == 1:
                break
            supported *= common
            remaining //= common
        assert supported * remaining == value
        if supported > 1:
            supported_blocks += 1
        root = math.isqrt(supported)
        if root * root != supported:
            rows.append(mask)
    return rows, {
        "supported_terminal_blocks": supported_blocks,
        "nonsquare_supported_blocks": len(rows),
        "distinct_exposed_row_masks": len(set(rows)),
        "saturation_gcds": saturation_gcds,
        "rank": gf2_rank(rows),
    }


def main() -> None:
    started = time.monotonic()
    public = json.loads(PUBLIC_PATH.read_text())
    modulus = int(public["N"])
    bound = int(public["B"])
    certificate = public["decoder"]["first_useful_certificate"]
    records = certificate["witness_records"]
    assert len(records) == certificate["support"] == 166

    entries = []
    for column, record in enumerate(records):
        assert int(record["c"]) * int(record["w"]) == int(record["P"])
        assert int(record["P"]) % modulus == 1
        entries.append((int(record["c"]), 1 << column))
        entries.append((int(record["w"]), 1 << column))
    blocks, refinements, gcd_tests = parity_coprime_basis(entries)
    full_rows = []
    square_blocks = 0
    for value, mask in blocks:
        root = math.isqrt(value)
        if root * root == value:
            square_blocks += 1
        else:
            full_rows.append(mask)
    full_rank = gf2_rank(full_rows)

    represented_keys = sorted(
        {
            (
                int(record["provenance"]["active_relation_index_zero_based"]),
                int(record["provenance"]["u"]),
                int(record["provenance"]["v"]),
                str(record["provenance"]["orientation"]),
            )
            for record in records
            if record["provenance"]["kind"] == "feedback_trajectory"
        }
    )
    all_keys = []
    for active_index, (u_value, v_value) in enumerate(public["active_pairs"]):
        all_keys.append((active_index, int(u_value), int(v_value), "u_power_times_v"))
        all_keys.append((active_index, int(u_value), int(v_value), "u_times_v_power"))

    represented_product, represented_stats = exposure_product(
        modulus, bound, represented_keys
    )
    represented_rows, represented_coverage = exposed_rows(blocks, represented_product)
    all_product, all_stats = exposure_product(modulus, bound, all_keys)
    all_rows, all_coverage = exposed_rows(blocks, all_product)

    exact_product = math.prod(int(record["P"]) for record in records)
    exact_root = math.isqrt(exact_product)
    assert exact_root * exact_root == exact_product
    root_modulus = exact_root % modulus
    root_gcds = [math.gcd(root_modulus - 1, modulus), math.gcd(root_modulus + 1, modulus)]

    result = {
        "status": "PASS",
        "role": "factor-free public carry-coverage replay of the fixed F98 circuit",
        "input": {
            "path": str(PUBLIC_PATH.relative_to(ROOT)),
            "sha256": sha256_file(PUBLIC_PATH),
            "N": modulus,
            "bit_length": modulus.bit_length(),
            "bound": bound,
            "columns": len(records),
        },
        "public_refinement": {
            "terminal_blocks": len(blocks),
            "square_terminal_blocks": square_blocks,
            "nonsquare_row_masks": len(full_rows),
            "distinct_nonsquare_row_masks": len(set(full_rows)),
            "rank": full_rank,
            "nullity": len(records) - full_rank,
            "refinements": refinements,
            "gcd_tests": gcd_tests,
        },
        "represented_trajectory_coverage": {
            **represented_stats,
            **represented_coverage,
            "equals_full_rank": represented_coverage["rank"] == full_rank,
            "exposure_product_bits": represented_product.bit_length(),
        },
        "all_round_one_coverage": {
            **all_stats,
            **all_coverage,
            "equals_full_rank": all_coverage["rank"] == full_rank,
            "exposure_product_bits": all_product.bit_length(),
        },
        "public_root_check": {
            "root_mod_N": root_modulus,
            "gcds": root_gcds,
        },
        "forbidden_operations_used": [],
        "elapsed_seconds": time.monotonic() - started,
    }
    assert full_rank == 165
    assert represented_coverage["rank"] == 165
    assert all_coverage["rank"] == 165
    assert sorted(root_gcds) == [10267, 19727]
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
