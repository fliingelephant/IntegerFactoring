#!/usr/bin/env sage

import argparse
import hashlib
import json
from collections import Counter, defaultdict, deque
from math import prod
from pathlib import Path

from sage.all import Integer, factor


parser = argparse.ArgumentParser()
parser.add_argument("--input", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

public = json.loads(args.input.read_text())
N = int(public["N"])
B = int(public["B"])

stream = []
seen_residues = set()
for seed in range(2, int(public["n"]) + 1):
    seen_residues.add(seed)
    w = pow(seed, -1, N)
    stream.append(
        {
            "raw_index": len(stream),
            "c": seed,
            "w": w,
            "P": seed * w,
            "kind": "initial_seed",
            "family": f"seed:{seed}",
            "orientation": "seed",
        }
    )

for active_index, pair in enumerate(public["active_pairs"]):
    u, v = (int(pair[0]), int(pair[1]))
    u_power = 1
    v_power = 1
    for exponent in range(B + 1):
        for orientation, c in (
            ("u_power_times_v", u_power * v % N),
            ("u_times_v_power", u * v_power % N),
        ):
            if c in seen_residues:
                continue
            seen_residues.add(c)
            w = pow(c, -1, N)
            stream.append(
                {
                    "raw_index": len(stream),
                    "c": c,
                    "w": w,
                    "P": c * w,
                    "kind": "feedback_trajectory",
                    "family": f"{active_index}:{u}:{v}",
                    "orientation": orientation,
                }
            )
        u_power = u_power * u % N
        v_power = v_power * v % N

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

supports = []
factor_counts = []
largest_prime_bits = Counter()
for ordinal, record in enumerate(relations, 1):
    decomposition = [(int(p), int(e)) for p, e in factor(Integer(record["P"]))]
    assert prod(p**e for p, e in decomposition) == int(record["P"])
    support = [p for p, e in decomposition if e % 2]
    supports.append(support)
    factor_counts.append(len(decomposition))
    largest_prime_bits[max(p for p, _ in decomposition).bit_length()] += 1
    if ordinal % 1_000 == 0:
        print(f"factored={ordinal}/{len(relations)}", flush=True)

all_primes = sorted({p for support in supports for p in support})
row_index = {p: index for index, p in enumerate(all_primes)}
signatures = [int(sum(1 << row_index[p] for p in support)) for support in supports]


def rank_of(columns):
    pivots = {}
    for column in columns:
        value = signatures[column]
        while value:
            pivot = (value & -value).bit_length() - 1
            prior = pivots.get(pivot)
            if prior is None:
                pivots[pivot] = value
                break
            value = value.__xor__(prior)
    return len(pivots)


prime_members = defaultdict(list)
for column, support in enumerate(supports):
    for p in support:
        prime_members[p].append(column)


def peel(candidate_columns):
    active = set(candidate_columns)
    degrees = {
        p: sum(column in active for column in members)
        for p, members in prime_members.items()
    }
    queue = deque(sorted(p for p, degree in degrees.items() if degree == 1))
    removed = []
    while queue:
        p = queue.popleft()
        if degrees[p] != 1:
            continue
        column = next((column for column in prime_members[p] if column in active), None)
        if column is None:
            raise AssertionError("degree-one row has no active column")
        active.remove(column)
        removed.append(column)
        for q in supports[column]:
            degrees[q] -= 1
            if degrees[q] == 1:
                queue.append(q)
    core = sorted(active)
    core_rows = sorted(p for p, degree in degrees.items() if degree > 0)
    assert all(degrees[p] >= 2 for p in core_rows)
    return core, core_rows, removed, degrees


def component_sizes(columns):
    active = set(columns)
    if not active:
        return []
    unseen = set(active)
    sizes = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        size = 0
        while queue:
            column = queue.popleft()
            size += 1
            for p in supports[column]:
                for neighbor in prime_members[p]:
                    if neighbor in unseen:
                        unseen.remove(neighbor)
                        queue.append(neighbor)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def summarize(columns):
    columns = sorted(columns)
    column_set = set(columns)
    core, core_rows, removed, degrees = peel(columns)
    rank = rank_of(columns)
    core_rank = rank_of(core)
    active_rows = [
        p for p in all_primes if any(column in column_set for column in prime_members[p])
    ]
    row_degrees = Counter(
        sum(column in column_set for column in prime_members[p]) for p in active_rows
    )
    core_row_degrees = Counter(degrees[p] for p in core_rows)
    return {
        "columns": len(columns),
        "row_count": len(active_rows),
        "rank": rank,
        "nullity": len(columns) - rank,
        "initial_degree_one_rows": row_degrees[1],
        "peeled_columns": len(removed),
        "core_columns": len(core),
        "core_rows": len(core_rows),
        "core_rank": core_rank,
        "core_nullity": len(core) - core_rank,
        "kernel_preserved": len(columns) - rank == len(core) - core_rank,
        "row_degree_histogram": {
            int(degree): int(count) for degree, count in sorted(row_degrees.items())
        },
        "core_row_degree_histogram": {
            int(degree): int(count)
            for degree, count in sorted(core_row_degrees.items())
        },
        "core_component_sizes": component_sizes(core),
        "core_columns_zero_based": core,
    }


full_columns = list(range(len(relations)))
prefix_columns = [
    column for column, record in enumerate(relations) if int(record["raw_index"]) < 5_616
]
full = summarize(full_columns)
prefix = summarize(prefix_columns)

selected = [
    int(value)
    for value in public["decoder"]["first_useful_certificate"][
        "selected_columns_zero_based"
    ]
]
assert len(selected) == 166
assert set(selected).issubset(set(full["core_columns_zero_based"]))

full_core_set = set(full["core_columns_zero_based"])
core_provenance = Counter(relations[column]["kind"] for column in full_core_set)
core_families = Counter(relations[column]["family"] for column in full_core_set)
core_orientations = Counter(relations[column]["orientation"] for column in full_core_set)

result = {
    "status": "PASS",
    "role": "factor-assisted full-pool parity-core diagnosis",
    "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
    "N": N,
    "raw_relation_count": len(stream),
    "unique_relation_count": len(relations),
    "parity_prime_count": len(all_primes),
    "zero_signature_columns": sum(signature == 0 for signature in signatures),
    "full": full,
    "raw_prefix_5616": prefix,
    "public_166_circuit_entirely_in_full_core": True,
    "public_166_selected_columns_zero_based": selected,
    "full_core_provenance_counts": dict(sorted(core_provenance.items())),
    "full_core_family_counts": dict(sorted(core_families.items())),
    "full_core_orientation_counts": dict(sorted(core_orientations.items())),
    "relation_distinct_prime_factor_count_histogram": dict(
        sorted(Counter(factor_counts).items())
    ),
    "largest_prime_factor_bitlength_histogram": dict(sorted(largest_prime_bits.items())),
}

# Keep the main output compact. The explicit core column lists are hashed and
# counted, then removed from the JSON.
for label in ("full", "raw_prefix_5616"):
    columns = result[label].pop("core_columns_zero_based")
    result[label]["core_columns_sha256"] = hashlib.sha256(
        ",".join(map(str, columns)).encode()
    ).hexdigest()

args.output.write_text(json.dumps(result, indent=2, sort_keys=True, default=int) + "\n")
print("status=PASS")
print(
    f"full rows={full['row_count']} columns={full['columns']} "
    f"rank={full['rank']} nullity={full['nullity']}"
)
print(
    f"full core rows={full['core_rows']} columns={full['core_columns']} "
    f"rank={full['core_rank']} nullity={full['core_nullity']}"
)
print(
    f"prefix core rows={prefix['core_rows']} columns={prefix['core_columns']} "
    f"rank={prefix['core_rank']} nullity={prefix['core_nullity']}"
)
