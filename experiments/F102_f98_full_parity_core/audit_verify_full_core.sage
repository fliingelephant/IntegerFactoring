#!/usr/bin/env sage

import argparse
import hashlib
import heapq
import json
from collections import Counter, defaultdict, deque
from math import prod
from pathlib import Path

from sage.all import Integer, factor


parser = argparse.ArgumentParser()
parser.add_argument("--input", type=Path, required=True)
parser.add_argument("--candidate-output", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

public = json.loads(args.input.read_text())
reported = json.loads(args.candidate_output.read_text())
N = int(public["N"])
bound = int(public["B"])
input_hash = hashlib.sha256(args.input.read_bytes()).hexdigest()

assert N == 202_537_109
assert input_hash == "ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab"
assert reported["input_sha256"] == input_hash


# Independently regenerate the full first-occurrence stream.
stream = []
seen_residues = set()
for seed in range(2, int(public["n"]) + 1):
    assert seed not in seen_residues
    seen_residues.add(seed)
    inverse = pow(seed, -1, N)
    stream.append({
        "raw_index": len(stream),
        "c": seed,
        "w": inverse,
        "P": seed * inverse,
        "kind": "initial_seed",
        "family": f"seed:{seed}",
        "orientation": "seed",
    })

for active_index, pair in enumerate(public["active_pairs"]):
    u, v = int(pair[0]), int(pair[1])
    for exponent in range(bound + 1):
        for orientation, residue in (
            ("u_power_times_v", pow(u, exponent, N) * v % N),
            ("u_times_v_power", u * pow(v, exponent, N) % N),
        ):
            if residue in seen_residues:
                continue
            seen_residues.add(residue)
            inverse = pow(residue, -1, N)
            stream.append({
                "raw_index": len(stream),
                "c": residue,
                "w": inverse,
                "P": residue * inverse,
                "kind": "feedback_trajectory",
                "family": f"{active_index}:{u}:{v}",
                "orientation": orientation,
            })

assert len(stream) == int(public["retained_relation_count"]) == 12_549

relations = []
seen_values = set()
for record in stream:
    value = int(record["P"])
    if value == 1 or value in seen_values:
        continue
    seen_values.add(value)
    relations.append(record)
assert len(relations) == int(public["decoder"]["unique_relation_count"]) == 9_414


# Factor every distinct exact value and reconstruct the prime-parity columns.
supports = []
factor_count_histogram = Counter()
largest_prime_bits = Counter()
for ordinal, record in enumerate(relations, 1):
    value = int(record["P"])
    assert int(record["c"]) * int(record["w"]) == value
    assert value % N == 1
    decomposition = [(int(prime), int(exponent)) for prime, exponent in factor(Integer(value))]
    assert prod(prime**exponent for prime, exponent in decomposition) == value
    support = [prime for prime, exponent in decomposition if exponent % 2]
    supports.append(support)
    factor_count_histogram[len(decomposition)] += 1
    largest_prime_bits[max(prime for prime, _ in decomposition).bit_length()] += 1
    if ordinal % 1_000 == 0:
        print(f"audit_factored={ordinal}/{len(relations)}", flush=True)

parity_primes = sorted({prime for support in supports for prime in support})
prime_index = {prime: index for index, prime in enumerate(parity_primes)}
signatures = [sum(1 << prime_index[prime] for prime in support) for support in supports]
assert len(parity_primes) == 11_034
assert all(signature != 0 for signature in signatures)

prime_members = defaultdict(list)
for column, support in enumerate(supports):
    for prime in support:
        prime_members[prime].append(column)


# Use highest-bit Gaussian elimination, unlike the candidate's lowest-bit
# implementation.
def binary_rank(columns):
    pivots = {}
    for column in columns:
        value = int(signatures[column])
        while value:
            pivot = value.bit_length() - 1
            prior = pivots.get(pivot)
            if prior is None:
                pivots[pivot] = value
                break
            value = value.__xor__(prior)
    return len(pivots)


# Peel with a min-prime or max-prime priority. Equality of both results is an
# independent order-sensitivity check.
def peel(columns, reverse=False):
    active = set(columns)
    degrees = {
        prime: sum(column in active for column in members)
        for prime, members in prime_members.items()
    }
    heap = []
    for prime, degree in degrees.items():
        if degree == 1:
            heapq.heappush(heap, -prime if reverse else prime)

    removed = []
    while heap:
        item = heapq.heappop(heap)
        prime = -item if reverse else item
        if degrees[prime] != 1:
            continue
        column = next(column for column in prime_members[prime] if column in active)
        active.remove(column)
        removed.append(column)
        for incident_prime in supports[column]:
            degrees[incident_prime] -= 1
            if degrees[incident_prime] == 1:
                heapq.heappush(
                    heap, -incident_prime if reverse else incident_prime
                )

    core = sorted(active)
    core_rows = sorted(prime for prime, degree in degrees.items() if degree > 0)
    assert all(degrees[prime] >= 2 for prime in core_rows)
    return core, core_rows, removed, degrees


def component_sizes(columns):
    unseen = set(columns)
    sizes = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        size = 0
        while queue:
            column = queue.popleft()
            size += 1
            for prime in supports[column]:
                for neighbor in prime_members[prime]:
                    if neighbor in unseen:
                        unseen.remove(neighbor)
                        queue.append(neighbor)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def core_hash(columns):
    return hashlib.sha256(",".join(map(str, columns)).encode()).hexdigest()


def summarize(columns):
    columns = sorted(columns)
    column_set = set(columns)
    core_min, core_rows, removed, final_degrees = peel(columns, reverse=False)
    core_max, reverse_rows, reverse_removed, reverse_degrees = peel(
        columns, reverse=True
    )
    assert core_min == core_max
    assert core_rows == reverse_rows
    assert len(removed) == len(reverse_removed)
    assert all(final_degrees[prime] == reverse_degrees[prime] for prime in parity_primes)

    active_rows = [
        prime
        for prime in parity_primes
        if any(column in column_set for column in prime_members[prime])
    ]
    row_histogram = Counter(
        sum(column in column_set for column in prime_members[prime])
        for prime in active_rows
    )
    core_histogram = Counter(final_degrees[prime] for prime in core_rows)
    rank = binary_rank(columns)
    core_rank = binary_rank(core_min)
    nullity = len(columns) - rank
    core_nullity = len(core_min) - core_rank
    assert nullity == core_nullity
    assert rank - core_rank == len(removed)

    return {
        "columns": len(columns),
        "row_count": len(active_rows),
        "rank": rank,
        "nullity": nullity,
        "initial_degree_one_rows": row_histogram[1],
        "peeled_columns": len(removed),
        "core_columns": len(core_min),
        "core_rows": len(core_rows),
        "core_rank": core_rank,
        "core_nullity": core_nullity,
        "kernel_preserved": True,
        "row_degree_histogram": {
            int(degree): int(count) for degree, count in sorted(row_histogram.items())
        },
        "core_row_degree_histogram": {
            int(degree): int(count) for degree, count in sorted(core_histogram.items())
        },
        "core_component_sizes": component_sizes(core_min),
        "core_columns_sha256": core_hash(core_min),
        "core_columns_zero_based": core_min,
        "opposite_peel_orders_agree": True,
    }


full = summarize(range(len(relations)))
prefix_columns = [
    column
    for column, record in enumerate(relations)
    if int(record["raw_index"]) < 5_616
]
prefix = summarize(prefix_columns)

selected = [
    int(column)
    for column in public["decoder"]["first_useful_certificate"][
        "selected_columns_zero_based"
    ]
]
assert len(selected) == 166
assert set(selected).issubset(set(full["core_columns_zero_based"]))

full_core = set(full["core_columns_zero_based"])
provenance_counts = Counter(relations[column]["kind"] for column in full_core)
family_counts = Counter(relations[column]["family"] for column in full_core)
orientation_counts = Counter(relations[column]["orientation"] for column in full_core)


def normalize_histogram(histogram):
    return {int(key): int(value) for key, value in histogram.items()}


# Compare every reported summary value and histogram.
for label, independent in (("full", full), ("raw_prefix_5616", prefix)):
    candidate = reported[label]
    for key in (
        "columns",
        "row_count",
        "rank",
        "nullity",
        "initial_degree_one_rows",
        "peeled_columns",
        "core_columns",
        "core_rows",
        "core_rank",
        "core_nullity",
        "kernel_preserved",
        "core_component_sizes",
        "core_columns_sha256",
    ):
        assert candidate[key] == independent[key]
    assert normalize_histogram(candidate["row_degree_histogram"]) == independent[
        "row_degree_histogram"
    ]
    assert normalize_histogram(candidate["core_row_degree_histogram"]) == independent[
        "core_row_degree_histogram"
    ]

assert reported["N"] == N
assert reported["raw_relation_count"] == len(stream) == 12_549
assert reported["unique_relation_count"] == len(relations) == 9_414
assert reported["parity_prime_count"] == len(parity_primes) == 11_034
assert reported["zero_signature_columns"] == 0
assert reported["public_166_circuit_entirely_in_full_core"] is True
assert reported["public_166_selected_columns_zero_based"] == selected
assert reported["full_core_provenance_counts"] == dict(sorted(provenance_counts.items()))
assert reported["full_core_family_counts"] == dict(sorted(family_counts.items()))
assert reported["full_core_orientation_counts"] == dict(sorted(orientation_counts.items()))
assert normalize_histogram(reported["relation_distinct_prime_factor_count_histogram"]) == dict(
    sorted(factor_count_histogram.items())
)
assert normalize_histogram(reported["largest_prime_factor_bitlength_histogram"]) == dict(
    sorted(largest_prime_bits.items())
)

feedback_families = [family for family in family_counts if not family.startswith("seed:")]
seed_families = [family for family in family_counts if family.startswith("seed:")]
assert len(feedback_families) == 8
assert seed_families == ["seed:11", "seed:2", "seed:27"] or set(seed_families) == {
    "seed:2", "seed:11", "seed:27"
}
assert provenance_counts == Counter({"feedback_trajectory": 1_778, "initial_seed": 3})
assert orientation_counts == Counter({
    "u_power_times_v": 1_138,
    "u_times_v_power": 640,
    "seed": 3,
})

result = {
    "status": "PASS",
    "input_sha256": input_hash,
    "full": {key: value for key, value in full.items() if key != "core_columns_zero_based"},
    "raw_prefix_5616": {
        key: value for key, value in prefix.items() if key != "core_columns_zero_based"
    },
    "public_166_entirely_in_full_core": True,
    "full_core_provenance_counts": dict(sorted(provenance_counts.items())),
    "full_core_family_count_excluding_seeds": len(feedback_families),
    "full_core_orientation_counts": dict(sorted(orientation_counts.items())),
}
args.output.write_text(json.dumps(result, indent=2, sort_keys=True, default=int) + "\n")
print("status=PASS")
print(
    f"full={full['columns']}x{full['row_count']} "
    f"rank={full['rank']} nullity={full['nullity']} "
    f"core={full['core_columns']}x{full['core_rows']}"
)
print(
    f"prefix={prefix['columns']}x{prefix['row_count']} "
    f"rank={prefix['rank']} nullity={prefix['nullity']} "
    f"core={prefix['core_columns']}x{prefix['core_rows']}"
)
