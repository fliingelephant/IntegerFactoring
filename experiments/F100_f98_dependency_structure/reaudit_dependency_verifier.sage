#!/usr/bin/env sage

import argparse
import json
from collections import Counter, defaultdict, deque
from math import gcd, isqrt, prod
from pathlib import Path

from sage.all import GF, Matrix, factor


parser = argparse.ArgumentParser()
parser.add_argument("--input", type=Path, required=True)
parser.add_argument("--candidate-output", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

public = json.loads(args.input.read_text())
reported = json.loads(args.candidate_output.read_text())
N = int(public["N"])
certificate = public["decoder"]["first_useful_certificate"]
records = certificate["witness_records"]

assert N == 202_537_109
assert len(records) == certificate["support"] == 166
assert len({int(record["P"]) for record in records}) == 166


# Factor and validate every selected exact relation without importing F100.
decompositions = []
supports = []
values = []
for record in records:
    c = int(record["c"])
    w = int(record["w"])
    P = int(record["P"])
    assert 1 <= c < N and 1 <= w < N
    assert pow(c, -1, N) == w
    assert c * w == P and P % N == 1

    source = record["provenance"]
    if source["kind"] == "initial_seed":
        assert c == int(source["seed"])
    else:
        assert source["kind"] == "feedback_trajectory"
        assert int(source["round"]) == 1
        u = int(source["u"])
        v = int(source["v"])
        exponent = int(source["exponent"])
        if source["orientation"] == "u_power_times_v":
            assert c == pow(u, exponent, N) * v % N
        else:
            assert source["orientation"] == "u_times_v_power"
            assert c == u * pow(v, exponent, N) % N

    decomposition = [(int(prime), int(exponent)) for prime, exponent in factor(P)]
    assert prod(prime**exponent for prime, exponent in decomposition) == P
    support = [prime for prime, exponent in decomposition if exponent % 2]
    decompositions.append(decomposition)
    supports.append(support)
    values.append(P)


parity_primes = sorted({prime for support in supports for prime in support})
matrix = Matrix(
    GF(2),
    len(parity_primes),
    len(records),
    lambda row, column: int(parity_primes[row] in supports[column]),
)
rank = int(matrix.rank())
nullity = matrix.ncols() - rank
assert len(parity_primes) == 230
assert rank == 165 and nullity == 1
assert sum(matrix.column(column) for column in range(matrix.ncols())) == 0

# Directly confirm that every one-column deletion is independent.
for omitted in range(166):
    kept = [column for column in range(166) if column != omitted]
    assert matrix.matrix_from_columns(kept).rank() == 165

row_degrees = [sum(int(value) for value in matrix.row(row)) for row in range(matrix.nrows())]
column_degrees = [
    sum(int(value) for value in matrix.column(column))
    for column in range(matrix.ncols())
]
row_histogram = dict(sorted(Counter(row_degrees).items()))
column_histogram = dict(sorted(Counter(column_degrees).items()))
assert row_histogram == {2: 167, 4: 31, 6: 9, 8: 7, 10: 3, 12: 1,
                         14: 1, 16: 1, 18: 1, 20: 1, 22: 1, 28: 1,
                         32: 1, 34: 1, 44: 1, 52: 1, 62: 1, 80: 1}
assert column_histogram == {3: 6, 4: 13, 5: 36, 6: 41, 7: 37,
                            8: 22, 9: 10, 11: 1}
assert row_degrees[parity_primes.index(2)] == 80


def component_sizes(selected_supports):
    neighbors = [set() for _ in selected_supports]
    prime_columns = defaultdict(list)
    for column, support in enumerate(selected_supports):
        for prime in support:
            prime_columns[prime].append(column)
    for columns in prime_columns.values():
        for left in columns:
            neighbors[left].update(right for right in columns if right != left)

    unseen = set(range(len(selected_supports)))
    sizes = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        size = 0
        while queue:
            node = queue.popleft()
            size += 1
            for neighbor in neighbors[node]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
        sizes.append(size)
    return sorted(sizes, reverse=True)


components = component_sizes(supports)
odd_prime_components = component_sizes([
    [prime for prime in support if prime != 2] for support in supports
])
assert components == odd_prime_components == [166]


# Recompute provenance at both family and oriented-trajectory granularity.
kind_counts = Counter()
orientation_counts = Counter()
family_counts = Counter()
oriented_counts = Counter()
for record in records:
    source = record["provenance"]
    kind_counts[source["kind"]] += 1
    if source["kind"] == "feedback_trajectory":
        family = (
            int(source["active_relation_index_zero_based"]),
            int(source["u"]),
            int(source["v"]),
        )
        orientation = source["orientation"]
        family_counts[family] += 1
        orientation_counts[orientation] += 1
        oriented_counts[family + (orientation,)] += 1

expected_families = Counter({
    (9, 11, 36_824_929): 15,
    (11, 13, 124_638_221): 10,
    (12, 2, 5): 54,
    (15, 2, 17): 53,
    (25, 3, 17): 33,
})
expected_oriented = Counter({
    (9, 11, 36_824_929, "u_power_times_v"): 15,
    (11, 13, 124_638_221, "u_power_times_v"): 10,
    (12, 2, 5, "u_power_times_v"): 32,
    (12, 2, 5, "u_times_v_power"): 22,
    (15, 2, 17, "u_power_times_v"): 38,
    (15, 2, 17, "u_times_v_power"): 15,
    (25, 3, 17, "u_power_times_v"): 15,
    (25, 3, 17, "u_times_v_power"): 18,
})
assert kind_counts == Counter({"feedback_trajectory": 165, "initial_seed": 1})
assert orientation_counts == Counter({"u_power_times_v": 110, "u_times_v_power": 55})
assert family_counts == expected_families
assert oriented_counts == expected_oriented
assert len(family_counts) == 5 and len(oriented_counts) == 8


# Recompute exact square root and factor extraction.
total = prod(values)
root = isqrt(total)
assert root * root == total
root_gcds = [gcd(root - 1, N), gcd(root + 1, N)]
assert root % N == 132_013_085
assert root_gcds == [19_727, 10_267]


# Check every corrected output field and reject the old misnamed keys.
assert "odd_prime_row_count" not in reported
assert "pairwise_odd_support_intersections" not in reported
assert "trajectory_counts" not in reported
assert reported["parity_prime_row_count"] == 230
assert reported["rank"] == rank and reported["nullity"] == nullity
assert reported["is_binary_matroid_circuit"] is True
assert reported["distinct_exact_values"] == reported["certificate_size"] == 166
assert {int(key): int(value) for key, value in reported["row_degree_histogram"].items()} == row_histogram
assert {int(key): int(value) for key, value in reported["column_degree_histogram"].items()} == column_histogram
assert reported["degree_two_row_fraction"] == 167 / 230
assert reported["relation_support_graph_component_sizes"] == components
assert reported["pairwise_parity_support_intersections"] == 7_583
assert reported["pairwise_nontrivial_integer_gcds"] == 11_358
assert reported["root_mod_N"] == root % N
assert reported["root_gcds"] == root_gcds
assert reported["provenance_counts"] == dict(sorted(kind_counts.items()))
assert reported["orientation_counts"] == dict(sorted(orientation_counts.items()))
assert reported["active_pair_family_counts"] == {
    f"{index}:{u}:{v}": count
    for (index, u, v), count in sorted(family_counts.items())
}
assert reported["oriented_trajectory_counts"] == {
    f"{index}:{u}:{v}:{orientation}": count
    for (index, u, v, orientation), count in sorted(oriented_counts.items())
}

assert len(reported["relation_factorizations"]) == 166
for entry, P, decomposition, support in zip(
    reported["relation_factorizations"], values, decompositions, supports
):
    assert int(entry["P"]) == P
    assert [[int(prime), int(exponent)] for prime, exponent in entry["factors"]] == [
        [prime, exponent] for prime, exponent in decomposition
    ]
    assert [int(prime) for prime in entry["odd_valuation_support"]] == support
    assert "odd_support" not in entry


result = {
    "status": "PASS",
    "certificate_size": 166,
    "distinct_values": len(set(values)),
    "parity_prime_rows_including_2": len(parity_primes),
    "prime_2_row_degree": row_degrees[parity_primes.index(2)],
    "rank": rank,
    "nullity": nullity,
    "all_single_column_deletions_independent": True,
    "component_sizes": components,
    "component_sizes_without_prime_2": odd_prime_components,
    "active_pair_family_count": len(family_counts),
    "oriented_trajectory_count": len(oriented_counts),
    "root_mod_N": root % N,
    "root_gcds": root_gcds,
    "corrected_output_keys": "PASS",
}
args.output.write_text(json.dumps(result, indent=2, sort_keys=True, default=int) + "\n")
print("status=PASS")
print(f"rows={len(parity_primes)} rank={rank} nullity={nullity}")
print(f"families={len(family_counts)} oriented_trajectories={len(oriented_counts)}")
