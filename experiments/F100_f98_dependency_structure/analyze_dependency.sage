#!/usr/bin/env sage

import argparse
import json
from collections import Counter, defaultdict, deque
from math import gcd, isqrt, prod
from pathlib import Path

from sage.all import GF, Matrix, factor


parser = argparse.ArgumentParser()
parser.add_argument("--input", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

data = json.loads(args.input.read_text())
N = int(data["N"])
certificate = data["decoder"]["first_useful_certificate"]
records = certificate["witness_records"]
assert len(records) == 166
assert len({int(record["P"]) for record in records}) == 166

factorizations = []
parity_supports = []
all_prime_supports = []
for record in records:
    value = int(record["P"])
    decomposition = [(int(prime), int(exponent)) for prime, exponent in factor(value)]
    assert prod(prime**exponent for prime, exponent in decomposition) == value
    factorizations.append(decomposition)
    parity_supports.append([prime for prime, exponent in decomposition if exponent % 2])
    all_prime_supports.append([prime for prime, _ in decomposition])

parity_primes = sorted({prime for support in parity_supports for prime in support})
matrix = Matrix(
    GF(2),
    len(parity_primes),
    len(records),
    lambda row, column: int(parity_primes[row] in parity_supports[column]),
)
rank = int(matrix.rank())
nullity = len(records) - rank
assert sum(matrix.column(index) for index in range(len(records))) == 0
assert rank == len(records) - 1
assert nullity == 1

row_degrees = [sum(int(value) for value in matrix.row(row)) for row in range(matrix.nrows())]
column_degrees = [sum(int(value) for value in matrix.column(column)) for column in range(matrix.ncols())]
assert all(degree > 0 and degree % 2 == 0 for degree in row_degrees)
assert all(degree > 0 for degree in column_degrees)

relation_neighbors = [set() for _ in records]
prime_to_columns = defaultdict(list)
for column, support in enumerate(parity_supports):
    for prime in support:
        prime_to_columns[prime].append(column)
for columns in prime_to_columns.values():
    for left in columns:
        relation_neighbors[left].update(right for right in columns if right != left)

components = []
unseen = set(range(len(records)))
while unseen:
    start = min(unseen)
    queue = deque([start])
    unseen.remove(start)
    component = []
    while queue:
        node = queue.popleft()
        component.append(node)
        for neighbor in relation_neighbors[node]:
            if neighbor in unseen:
                unseen.remove(neighbor)
                queue.append(neighbor)
    components.append(sorted(component))

pairwise_parity_intersections = 0
pairwise_integer_gcds = 0
for left in range(len(records)):
    left_parity = set(parity_supports[left])
    left_value = int(records[left]["P"])
    for right in range(left + 1, len(records)):
        if left_parity.intersection(parity_supports[right]):
            pairwise_parity_intersections += 1
        if gcd(left_value, int(records[right]["P"])) > 1:
            pairwise_integer_gcds += 1

root = isqrt(prod(int(record["P"]) for record in records))
assert root * root == prod(int(record["P"]) for record in records)

provenance = Counter()
orientation = Counter()
trajectory = Counter()
oriented_trajectory = Counter()
for record in records:
    source = record["provenance"]
    provenance[source["kind"]] += 1
    if source["kind"] == "feedback_trajectory":
        orientation[source["orientation"]] += 1
        trajectory[
            (
                int(source["active_relation_index_zero_based"]),
                int(source["u"]),
                int(source["v"]),
            )
        ] += 1
        oriented_trajectory[
            (
                int(source["active_relation_index_zero_based"]),
                int(source["u"]),
                int(source["v"]),
                source["orientation"],
            )
        ] += 1

result = {
    "status": "PASS",
    "role": "factor-assisted structural diagnosis of the fixed F98 certificate",
    "N": N,
    "certificate_size": len(records),
    "distinct_exact_values": len({int(record["P"]) for record in records}),
    "parity_prime_row_count": len(parity_primes),
    "rank": rank,
    "nullity": nullity,
    "is_binary_matroid_circuit": rank == len(records) - 1 and all(
        sum(int(value) for value in matrix.row(row)) % 2 == 0
        for row in range(matrix.nrows())
    ),
    "row_degree_histogram": dict(sorted(Counter(row_degrees).items())),
    "column_degree_histogram": dict(sorted(Counter(column_degrees).items())),
    "degree_two_row_fraction": (
        sum(degree == 2 for degree in row_degrees) / len(row_degrees)
        if row_degrees else 0
    ),
    "relation_support_graph_component_sizes": sorted(
        (len(component) for component in components), reverse=True
    ),
    "pairwise_parity_support_intersections": pairwise_parity_intersections,
    "pairwise_nontrivial_integer_gcds": pairwise_integer_gcds,
    "root_mod_N": root % N,
    "root_gcds": [gcd(root - 1, N), gcd(root + 1, N)],
    "provenance_counts": dict(sorted(provenance.items())),
    "orientation_counts": dict(sorted(orientation.items())),
    "active_pair_family_counts": {
        f"{index}:{u}:{v}": count
        for (index, u, v), count in sorted(trajectory.items())
    },
    "oriented_trajectory_counts": {
        f"{index}:{u}:{v}:{orientation}": count
        for (index, u, v, orientation), count in sorted(oriented_trajectory.items())
    },
    "relation_factorizations": [
        {
            "P": int(record["P"]),
            "factors": decomposition,
            "odd_valuation_support": parity_support,
        }
        for record, decomposition, parity_support in zip(
            records, factorizations, parity_supports
        )
    ],
}
args.output.write_text(json.dumps(result, indent=2, sort_keys=True, default=int) + "\n")
print("status=PASS")
print(f"rows={len(parity_primes)} rank={rank} nullity={nullity}")
print(f"components={result['relation_support_graph_component_sizes']}")
print(f"degree_two_row_fraction={result['degree_two_row_fraction']:.6f}")
