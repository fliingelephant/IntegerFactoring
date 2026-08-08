#!/usr/bin/env sage -python
"""Proof-blind exact verifier for the F100 reconstruction statement.

Inputs are restricted to RECONSTRUCTION_STATEMENT.md and the pinned F98
PUBLIC_REPLAY_OUTPUT.json.  All factorizations and derived structures are
recomputed here with Sage exact arithmetic.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import hashlib
import json
import math
from pathlib import Path
import sys

from sage.all import GF, Integer, matrix, proof


HERE = Path(__file__).resolve().parent
STATEMENT = HERE / "RECONSTRUCTION_STATEMENT.md"
REPLAY = HERE.parent / "F98_multiseed_presentation_closure_kill" / "PUBLIC_REPLAY_OUTPUT.json"
SOURCE = Path(__file__).resolve()

EXPECTED_REPLAY_SHA256 = "ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab"
EXPECTED_N = 202_537_109
EXPECTED_ROW_HISTOGRAM = Counter(
    {
        2: 167,
        4: 31,
        6: 9,
        8: 7,
        10: 3,
        12: 1,
        14: 1,
        16: 1,
        18: 1,
        20: 1,
        22: 1,
        28: 1,
        32: 1,
        34: 1,
        44: 1,
        52: 1,
        62: 1,
        80: 1,
    }
)
EXPECTED_COLUMN_HISTOGRAM = Counter({3: 6, 4: 13, 5: 36, 6: 41, 7: 37, 8: 22, 9: 10, 11: 1})
EXPECTED_FAMILIES = Counter(
    {
        (9, 11, 36_824_929): 15,
        (11, 13, 124_638_221): 10,
        (12, 2, 5): 54,
        (15, 2, 17): 53,
        (25, 3, 17): 33,
    }
)
EXPECTED_TRAJECTORIES = Counter(
    {
        (9, 11, 36_824_929, "u_power_times_v"): 15,
        (11, 13, 124_638_221, "u_power_times_v"): 10,
        (12, 2, 5, "u_power_times_v"): 32,
        (12, 2, 5, "u_times_v_power"): 22,
        (15, 2, 17, "u_power_times_v"): 38,
        (15, 2, 17, "u_times_v_power"): 15,
        (25, 3, 17, "u_power_times_v"): 15,
        (25, 3, 17, "u_times_v_power"): 18,
    }
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gf2_rank(bit_columns: list[int]) -> int:
    """Return exact GF(2) column rank for integer bit-vector columns."""
    pivots: dict[int, int] = {}
    for original in bit_columns:
        value = original
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def graph_summary(row_supports: dict[int, list[int]], removed_prime: int | None = None) -> dict[str, object]:
    vertex_count = 166
    adjacency = [set() for _ in range(vertex_count)]
    edges: set[tuple[int, int]] = set()
    for prime, support in row_supports.items():
        if prime == removed_prime:
            continue
        for left, right in combinations(support, 2):
            edge = (left, right) if left < right else (right, left)
            edges.add(edge)
            adjacency[left].add(right)
            adjacency[right].add(left)

    unseen = set(range(vertex_count))
    component_sizes: list[int] = []
    while unseen:
        start = min(unseen)
        stack = [start]
        unseen.remove(start)
        size = 0
        while stack:
            vertex = stack.pop()
            size += 1
            for neighbor in adjacency[vertex]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
        component_sizes.append(size)
    component_sizes.sort(reverse=True)
    return {
        "removed_prime": removed_prime,
        "edge_count": len(edges),
        "component_sizes": component_sizes,
        "connected": component_sizes == [vertex_count],
    }


def counter_rows(counter: Counter[tuple]) -> list[dict[str, object]]:
    rows = []
    for key, count in sorted(counter.items()):
        if len(key) == 3:
            index, u, v = key
            rows.append({"active_index_zero_based": index, "u": u, "v": v, "count": count})
        else:
            index, u, v, orientation = key
            rows.append(
                {
                    "active_index_zero_based": index,
                    "u": u,
                    "v": v,
                    "orientation": orientation,
                    "count": count,
                }
            )
    return rows


def main() -> None:
    proof.all(True)
    print("F100 proof-blind verifier: Sage exact arithmetic with proof=True", file=sys.stderr)
    print(
        "runner=DOT_SAGE=/private/tmp/RECONSTRUCT_F100_SAGE "
        "/opt/homebrew/bin/timeout --verbose 300s /usr/local/bin/sage -python",
        file=sys.stderr,
    )
    print(f"statement_sha256={sha256(STATEMENT)}", file=sys.stderr)
    print(f"source_sha256={sha256(SOURCE)}", file=sys.stderr)

    replay_hash = sha256(REPLAY)
    assert replay_hash == EXPECTED_REPLAY_SHA256
    with REPLAY.open("r", encoding="utf-8") as handle:
        replay = json.load(handle)

    assert replay["N"] == EXPECTED_N
    records = replay["decoder"]["first_useful_certificate"]["witness_records"]
    assert len(records) == 166
    N = EXPECTED_N

    values: list[int] = []
    factorizations: list[dict[str, object]] = []
    odd_prime_sets: list[set[int]] = []
    aggregate_exponents: Counter[int] = Counter()

    for column, record in enumerate(records):
        assert set(record) == {"P", "c", "w", "provenance"}
        P = int(record["P"])
        c = int(record["c"])
        w = int(record["w"])
        assert 1 <= c < N
        assert 1 <= w < N
        assert P == c * w
        assert P % N == 1
        assert math.gcd(c, N) == 1
        assert w == pow(c, -1, N)

        factor_pairs = [(int(prime), int(exponent)) for prime, exponent in Integer(P).factor()]
        assert all(Integer(prime).is_prime(proof=True) for prime, _ in factor_pairs)
        assert math.prod(prime**exponent for prime, exponent in factor_pairs) == P
        odd_primes = {prime for prime, exponent in factor_pairs if exponent % 2 == 1}
        for prime, exponent in factor_pairs:
            aggregate_exponents[prime] += exponent

        values.append(P)
        odd_prime_sets.append(odd_primes)
        factorizations.append(
            {
                "column_zero_based": column,
                "P": P,
                "c": c,
                "w": w,
                "factors": [[prime, exponent] for prime, exponent in factor_pairs],
                "odd_primes": sorted(odd_primes),
            }
        )

    assert len(set(values)) == 166

    row_primes = sorted(set().union(*odd_prime_sets) | {2})
    assert len(row_primes) == 230
    row_supports = {
        prime: [column for column, odd_primes in enumerate(odd_prime_sets) if prime in odd_primes]
        for prime in row_primes
    }
    column_masks = []
    row_index = {prime: index for index, prime in enumerate(row_primes)}
    for odd_primes in odd_prime_sets:
        mask = 0
        for prime in odd_primes:
            mask |= 1 << row_index[prime]
        column_masks.append(mask)

    parity_matrix = matrix(
        GF(2),
        [[1 if prime in odd_prime_sets[column] else 0 for column in range(166)] for prime in row_primes],
    )
    sage_rank = int(parity_matrix.rank())
    bit_rank = gf2_rank(column_masks)
    assert sage_rank == bit_rank == 165
    assert parity_matrix.nrows() == 230 and parity_matrix.ncols() == 166
    assert all(len(support) % 2 == 0 for support in row_supports.values())
    delete_ranks = [gf2_rank(column_masks[:column] + column_masks[column + 1 :]) for column in range(166)]
    assert delete_ranks == [165] * 166

    row_histogram = Counter(len(support) for support in row_supports.values())
    column_degrees = [len(odd_primes) for odd_primes in odd_prime_sets]
    column_histogram = Counter(column_degrees)
    assert row_histogram == EXPECTED_ROW_HISTOGRAM
    assert column_histogram == EXPECTED_COLUMN_HISTOGRAM
    assert len(row_supports[2]) == 80
    assert [prime for prime, support in row_supports.items() if len(support) == 80] == [2]
    assert sum(map(len, row_supports.values())) == sum(column_degrees)

    full_graph = graph_summary(row_supports)
    no_two_graph = graph_summary(row_supports, removed_prime=2)
    assert full_graph["connected"] is True
    assert no_two_graph["connected"] is True

    kind_counts: Counter[str] = Counter()
    family_counts: Counter[tuple[int, int, int]] = Counter()
    trajectory_counts: Counter[tuple[int, int, int, str]] = Counter()
    provenance_formula_checks = 0
    for record in records:
        provenance = record["provenance"]
        kind = provenance["kind"]
        kind_counts[kind] += 1
        if kind == "initial_seed":
            assert provenance == {"kind": "initial_seed", "seed": 11}
            assert record["c"] == provenance["seed"]
            continue

        assert kind == "feedback_trajectory"
        assert set(provenance) == {
            "active_relation_index_zero_based",
            "exponent",
            "kind",
            "orientation",
            "round",
            "u",
            "v",
        }
        assert provenance["round"] == 1
        index = int(provenance["active_relation_index_zero_based"])
        exponent = int(provenance["exponent"])
        u = int(provenance["u"])
        v = int(provenance["v"])
        orientation = provenance["orientation"]
        assert exponent >= 1
        assert 1 <= u < N and 1 <= v < N
        if orientation == "u_power_times_v":
            regenerated_c = pow(u, exponent, N) * v % N
        elif orientation == "u_times_v_power":
            regenerated_c = u * pow(v, exponent, N) % N
        else:
            raise AssertionError(f"unknown orientation: {orientation}")
        assert regenerated_c == record["c"]
        provenance_formula_checks += 1
        family_counts[(index, u, v)] += 1
        trajectory_counts[(index, u, v, orientation)] += 1

    assert kind_counts == Counter({"feedback_trajectory": 165, "initial_seed": 1})
    assert family_counts == EXPECTED_FAMILIES
    assert trajectory_counts == EXPECTED_TRAJECTORIES
    assert provenance_formula_checks == 165

    total_product = math.prod(values)
    positive_root = math.isqrt(total_product)
    assert positive_root * positive_root == total_product
    assert all(exponent % 2 == 0 for exponent in aggregate_exponents.values())
    factor_root = math.prod(prime ** (exponent // 2) for prime, exponent in aggregate_exponents.items())
    assert factor_root == positive_root
    root_mod_N = positive_root % N
    gcd_minus = math.gcd(positive_root - 1, N)
    gcd_plus = math.gcd(positive_root + 1, N)
    assert root_mod_N == 132_013_085
    assert gcd_minus == 19_727
    assert gcd_plus == 10_267
    assert gcd_minus * gcd_plus == N
    assert Integer(gcd_minus).is_prime(proof=True)
    assert Integer(gcd_plus).is_prime(proof=True)

    row_data = [
        {"prime": prime, "degree": len(row_supports[prime]), "support_zero_based": row_supports[prime]}
        for prime in row_primes
    ]
    matrix_encoding = json.dumps(row_data, separators=(",", ":"), sort_keys=True).encode()
    factor_encoding = json.dumps(factorizations, separators=(",", ":"), sort_keys=True).encode()

    result = {
        "verdict": "PASS",
        "input": {
            "N": N,
            "statement_sha256": sha256(STATEMENT),
            "replay_sha256": replay_hash,
            "source_sha256": sha256(SOURCE),
            "witness_record_count": len(records),
        },
        "presentations": {
            "all_exact_products": True,
            "all_canonical_inverses": True,
            "distinct_P_count": len(set(values)),
        },
        "factorization": {
            "engine": "Sage Integer.factor with proof.all(True), followed by exact reconstruction and prime checks",
            "record_count": len(factorizations),
            "factorizations_sha256": hashlib.sha256(factor_encoding).hexdigest(),
            "records": factorizations,
        },
        "matrix": {
            "rows": parity_matrix.nrows(),
            "columns": parity_matrix.ncols(),
            "sage_rank": sage_rank,
            "independent_bit_rank": bit_rank,
            "nullity": parity_matrix.ncols() - sage_rank,
            "all_columns_sum_to_zero": True,
            "delete_one_ranks": delete_ranks,
            "all_delete_one_ranks_165": True,
            "row_degree_histogram": {str(key): value for key, value in sorted(row_histogram.items())},
            "column_degree_histogram": {str(key): value for key, value in sorted(column_histogram.items())},
            "prime_2_degree": len(row_supports[2]),
            "matrix_rows_sha256": hashlib.sha256(matrix_encoding).hexdigest(),
            "row_data": row_data,
        },
        "graphs": {"all_rows": full_graph, "without_prime_2": no_two_graph},
        "provenance": {
            "kind_counts": dict(sorted(kind_counts.items())),
            "feedback_formula_checks": provenance_formula_checks,
            "families": counter_rows(family_counts),
            "trajectories": counter_rows(trajectory_counts),
        },
        "root": {
            "aggregate_factor_exponents_all_even": True,
            "positive_root": str(positive_root),
            "positive_root_decimal_digits": len(str(positive_root)),
            "positive_root_sha256": hashlib.sha256(str(positive_root).encode()).hexdigest(),
            "root_mod_N": root_mod_N,
            "gcd_root_minus_one_N": gcd_minus,
            "gcd_root_plus_one_N": gcd_plus,
            "gcd_factors_are_prime": True,
        },
        "scope": {
            "factor_assisted_diagnosis_only": True,
            "public_algorithm_step": False,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("VERDICT PASS", file=sys.stderr)


if __name__ == "__main__":
    main()
