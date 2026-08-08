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
candidate = json.loads(args.candidate_output.read_text())
N = int(public["N"])
B = int(public["B"])
certificate = public["decoder"]["first_useful_certificate"]
records = certificate["witness_records"]
raw_indices = [int(value) for value in certificate["selected_raw_indices_zero_based"]]
selected_columns = [int(value) for value in certificate["selected_columns_zero_based"]]

assert N == 202_537_109
assert B == 784
assert certificate["support"] == 166
assert len(records) == len(raw_indices) == len(selected_columns) == 166
assert len(set(raw_indices)) == len(set(selected_columns)) == 166


# Reconstruct the entire public first-occurrence record stream from the
# certificate's public active-pair list, then check every selected raw record.
stream = []
seen = set()
for seed in range(2, int(public["n"]) + 1):
    assert seed not in seen
    seen.add(seed)
    w = pow(seed, -1, N)
    stream.append({
        "c": seed,
        "w": w,
        "P": seed * w,
        "provenance": {"kind": "initial_seed", "seed": seed},
    })

for active_index, pair in enumerate(public["active_pairs"]):
    u, v = (int(pair[0]), int(pair[1]))
    for exponent in range(B + 1):
        for orientation, c in (
            ("u_power_times_v", pow(u, exponent, N) * v % N),
            ("u_times_v_power", u * pow(v, exponent, N) % N),
        ):
            if c in seen:
                continue
            seen.add(c)
            w = pow(c, -1, N)
            stream.append({
                "c": c,
                "w": w,
                "P": c * w,
                "provenance": {
                    "kind": "feedback_trajectory",
                    "round": 1,
                    "active_relation_index_zero_based": active_index,
                    "u": u,
                    "v": v,
                    "exponent": exponent,
                    "orientation": orientation,
                },
            })

assert len(stream) == int(public["retained_relation_count"]) == 12_549
for raw_index, record in zip(raw_indices, records):
    assert stream[raw_index] == record

# Reconstruct the exact-value deduplication and selected-column map.
unique_stream = []
seen_products = set()
for raw_index, record in enumerate(stream):
    P = int(record["P"])
    if P == 1 or P in seen_products:
        continue
    seen_products.add(P)
    unique_stream.append((raw_index, record))
assert len(unique_stream) == int(public["decoder"]["unique_relation_count"]) == 9_414
for column, raw_index, record in zip(selected_columns, raw_indices, records):
    assert unique_stream[column][0] == raw_index
    assert unique_stream[column][1] == record


# Validate and factor each selected exact relation independently.
factorizations = []
parity_supports = []
odd_prime_only_supports = []
all_factor_supports = []
products = []
for record in records:
    c = int(record["c"])
    w = int(record["w"])
    P = int(record["P"])
    assert 1 <= c < N and 1 <= w < N
    assert pow(c, -1, N) == w
    assert c * w == P and P % N == 1
    decomposition = [(int(prime), int(exponent)) for prime, exponent in factor(P)]
    assert prod(prime**exponent for prime, exponent in decomposition) == P
    factorizations.append(decomposition)
    parity = [prime for prime, exponent in decomposition if exponent % 2]
    parity_supports.append(parity)
    odd_prime_only_supports.append([prime for prime in parity if prime != 2])
    all_factor_supports.append([prime for prime, _ in decomposition])
    products.append(P)

assert len(set(products)) == 166


def matrix_summary(supports):
    primes = sorted({prime for support in supports for prime in support})
    matrix = Matrix(
        GF(2),
        len(primes),
        len(supports),
        lambda row, column: int(primes[row] in supports[column]),
    )
    rank = int(matrix.rank())
    nullity = matrix.ncols() - rank
    all_columns = sum(matrix.column(column) for column in range(matrix.ncols()))
    row_degrees = [sum(int(value) for value in matrix.row(row)) for row in range(matrix.nrows())]
    column_degrees = [
        sum(int(value) for value in matrix.column(column))
        for column in range(matrix.ncols())
    ]

    neighbors = [set() for _ in supports]
    prime_columns = defaultdict(list)
    for column, support in enumerate(supports):
        for prime in support:
            prime_columns[prime].append(column)
    for columns in prime_columns.values():
        for left in columns:
            neighbors[left].update(right for right in columns if right != left)

    unseen = set(range(len(supports)))
    component_sizes = []
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
        component_sizes.append(size)

    return {
        "primes": primes,
        "matrix": matrix,
        "rank": rank,
        "nullity": nullity,
        "all_column_dependency": all_columns == 0,
        "row_degrees": row_degrees,
        "column_degrees": column_degrees,
        "component_sizes": sorted(component_sizes, reverse=True),
    }


parity = matrix_summary(parity_supports)
odd_only = matrix_summary(odd_prime_only_supports)
all_factors = matrix_summary(all_factor_supports)

assert len(parity["primes"]) == 230
assert parity["rank"] == 165 and parity["nullity"] == 1
assert parity["all_column_dependency"]
assert all(degree > 0 and degree % 2 == 0 for degree in parity["row_degrees"])
assert all(degree > 0 for degree in parity["column_degrees"])

# Rank n-1 plus the all-column dependency proves a circuit. Check all 166
# one-column deletions as a redundant direct minimality test.
for omitted in range(166):
    columns = [column for column in range(166) if column != omitted]
    assert parity["matrix"].matrix_from_columns(columns).rank() == 165

parity_row_histogram = dict(sorted(Counter(parity["row_degrees"]).items()))
parity_column_histogram = dict(sorted(Counter(parity["column_degrees"]).items()))
assert parity_row_histogram == {2: 167, 4: 31, 6: 9, 8: 7, 10: 3, 12: 1,
                                14: 1, 16: 1, 18: 1, 20: 1, 22: 1, 28: 1,
                                32: 1, 34: 1, 44: 1, 52: 1, 62: 1, 80: 1}
assert parity_column_histogram == {3: 6, 4: 13, 5: 36, 6: 41, 7: 37,
                                   8: 22, 9: 10, 11: 1}
assert parity["component_sizes"] == [166]

# Check every summary field emitted by the candidate for this matrix.
assert candidate["certificate_size"] == 166
assert candidate["distinct_exact_values"] == 166
assert candidate["odd_prime_row_count"] == len(parity["primes"])
assert candidate["rank"] == parity["rank"]
assert candidate["nullity"] == parity["nullity"]
assert candidate["is_binary_matroid_circuit"] is True
assert {int(key): int(value) for key, value in candidate["row_degree_histogram"].items()} == parity_row_histogram
assert {int(key): int(value) for key, value in candidate["column_degree_histogram"].items()} == parity_column_histogram
assert candidate["relation_support_graph_component_sizes"] == parity["component_sizes"]
assert candidate["degree_two_row_fraction"] == 167 / 230
assert len(candidate["relation_factorizations"]) == 166
for reported, P, decomposition, support in zip(
    candidate["relation_factorizations"], products, factorizations, parity_supports
):
    assert int(reported["P"]) == P
    assert [[int(prime), int(exponent)] for prime, exponent in reported["factors"]] == [
        [prime, exponent] for prime, exponent in decomposition
    ]
    assert [int(prime) for prime in reported["odd_support"]] == support


# Recompute pair counts and provenance without using the candidate source.
pairwise_parity_intersections = 0
pairwise_odd_prime_intersections = 0
pairwise_integer_gcds = 0
for left in range(166):
    for right in range(left + 1, 166):
        if set(parity_supports[left]).intersection(parity_supports[right]):
            pairwise_parity_intersections += 1
        if set(odd_prime_only_supports[left]).intersection(odd_prime_only_supports[right]):
            pairwise_odd_prime_intersections += 1
        if gcd(products[left], products[right]) > 1:
            pairwise_integer_gcds += 1
assert pairwise_parity_intersections == int(candidate["pairwise_odd_support_intersections"])
assert pairwise_integer_gcds == int(candidate["pairwise_nontrivial_integer_gcds"])

kind_counts = Counter()
orientation_counts = Counter()
family_counts = Counter()
oriented_trajectory_counts = Counter()
for record in records:
    source = record["provenance"]
    kind_counts[source["kind"]] += 1
    if source["kind"] == "feedback_trajectory":
        index = int(source["active_relation_index_zero_based"])
        u = int(source["u"])
        v = int(source["v"])
        orientation = source["orientation"]
        assert [u, v] == [int(value) for value in public["active_pairs"][index]]
        orientation_counts[orientation] += 1
        family_counts[(index, u, v)] += 1
        oriented_trajectory_counts[(index, u, v, orientation)] += 1

assert kind_counts == Counter({"feedback_trajectory": 165, "initial_seed": 1})
assert orientation_counts == Counter({"u_power_times_v": 110, "u_times_v_power": 55})
assert family_counts == Counter({
    (9, 11, 36_824_929): 15,
    (11, 13, 124_638_221): 10,
    (12, 2, 5): 54,
    (15, 2, 17): 53,
    (25, 3, 17): 33,
})
assert len(oriented_trajectory_counts) == 8
assert candidate["provenance_counts"] == dict(sorted(kind_counts.items()))
assert candidate["orientation_counts"] == dict(sorted(orientation_counts.items()))
assert candidate["trajectory_counts"] == {
    f"{index}:{u}:{v}": count
    for (index, u, v), count in sorted(family_counts.items())
}


# Reconstruct the exact square root and factor extraction.
total_product = prod(products)
root = isqrt(total_product)
assert root * root == total_product
assert root % N == 132_013_085
root_gcds = [gcd(root - 1, N), gcd(root + 1, N)]
assert root_gcds == [19_727, 10_267]
assert prod(root_gcds) == N
assert int(candidate["root_mod_N"]) == root % N
assert [int(value) for value in candidate["root_gcds"]] == root_gcds

prime_two_row_degree = parity["row_degrees"][parity["primes"].index(2)]

result = {
    "status": "PASS",
    "certificate": {
        "size": 166,
        "distinct_values": len(set(products)),
        "root_mod_N": root % N,
        "root_gcds": root_gcds,
        "raw_stream_size": len(stream),
        "unique_relation_stream_size": len(unique_stream),
    },
    "prime_valuation_parity_matrix_including_2": {
        "row_count": len(parity["primes"]),
        "rank": parity["rank"],
        "nullity": parity["nullity"],
        "circuit": True,
        "all_single_column_deletions_independent": True,
        "row_degree_histogram": parity_row_histogram,
        "column_degree_histogram": parity_column_histogram,
        "degree_two_rows": sum(degree == 2 for degree in parity["row_degrees"]),
        "component_sizes": parity["component_sizes"],
        "prime_2_row_degree": prime_two_row_degree,
    },
    "odd_primes_only_parity_matrix": {
        "row_count": len(odd_only["primes"]),
        "rank": odd_only["rank"],
        "nullity": odd_only["nullity"],
        "all_column_dependency": odd_only["all_column_dependency"],
        "row_degree_histogram": dict(sorted(Counter(odd_only["row_degrees"]).items())),
        "column_degree_histogram": dict(sorted(Counter(odd_only["column_degrees"]).items())),
        "degree_two_rows": sum(degree == 2 for degree in odd_only["row_degrees"]),
        "component_sizes": odd_only["component_sizes"],
    },
    "all_factor_support_graph": {
        "component_sizes": all_factors["component_sizes"],
    },
    "pair_counts": {
        "parity_prime_intersections_including_2": pairwise_parity_intersections,
        "odd_prime_only_parity_intersections": pairwise_odd_prime_intersections,
        "nontrivial_integer_gcds": pairwise_integer_gcds,
    },
    "provenance": {
        "kind_counts": dict(sorted(kind_counts.items())),
        "orientation_counts": dict(sorted(orientation_counts.items())),
        "active_pair_family_counts": {
            f"{index}:{u}:{v}": count
            for (index, u, v), count in sorted(family_counts.items())
        },
        "active_pair_family_count": len(family_counts),
        "oriented_trajectory_count": len(oriented_trajectory_counts),
        "oriented_trajectory_counts": {
            f"{index}:{u}:{v}:{orientation}": count
            for (index, u, v, orientation), count in sorted(oriented_trajectory_counts.items())
        },
    },
}

args.output.write_text(json.dumps(result, indent=2, sort_keys=True, default=int) + "\n")
print("status=PASS")
print(f"parity_rows={len(parity['primes'])} rank={parity['rank']} nullity={parity['nullity']}")
print(f"odd_prime_only_rows={len(odd_only['primes'])} rank={odd_only['rank']} nullity={odd_only['nullity']}")
print(f"families={len(family_counts)} oriented_trajectories={len(oriented_trajectory_counts)}")
