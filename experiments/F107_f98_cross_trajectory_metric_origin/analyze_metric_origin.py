#!/opt/homebrew/bin/python3
import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
F98 = ROOT / "experiments/F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json"
F100 = ROOT / "experiments/F100_f98_dependency_structure/OUTPUT.json"
OUTPUT = Path(__file__).resolve().with_name("OUTPUT.json")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rank(rows):
    pivots = {}
    for row in rows:
        value = row
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def components(rows, width):
    parent = list(range(width))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            parent[y] = x

    incident = set()
    for mask in rows:
        support = []
        value = mask
        while value:
            bit = value & -value
            support.append(bit.bit_length() - 1)
            value ^= bit
        if support:
            incident.update(support)
            for column in support[1:]:
                union(support[0], column)
    sizes = Counter(find(column) for column in incident)
    return sorted(list(sizes.values()) + [1] * (width - len(incident)), reverse=True)


def key(record):
    provenance = record["provenance"]
    if provenance["kind"] == "initial_seed":
        return ("seed", provenance["seed"])
    return (
        "trajectory",
        provenance["active_relation_index_zero_based"],
        provenance["u"],
        provenance["v"],
        provenance["orientation"],
    )


def bases(record):
    provenance = record["provenance"]
    if provenance["kind"] == "initial_seed":
        return {provenance["seed"]}
    return {provenance["u"], provenance["v"]}


def multiplier(record):
    provenance = record["provenance"]
    return provenance["u"] if provenance["orientation"] == "u_power_times_v" else provenance["v"]


def main():
    public = json.loads(F98.read_text())
    assisted = json.loads(F100.read_text())
    records = public["decoder"]["first_useful_certificate"]["witness_records"]
    factorizations = assisted["relation_factorizations"]
    if len(records) != 166 or len(factorizations) != 166:
        raise AssertionError("Pinned certificate changed.")

    prime_masks = defaultdict(int)
    for column, (record, factorization) in enumerate(zip(records, factorizations)):
        if record["P"] != factorization["P"]:
            raise AssertionError("Pinned order mismatch.")
        product = 1
        for prime, exponent in factorization["factors"]:
            product *= prime**exponent
            if exponent & 1:
                prime_masks[prime] |= 1 << column
        if product != record["P"]:
            raise AssertionError("Bad pinned factorization.")
    if rank(prime_masks.values()) != 165 or any(mask.bit_count() & 1 for mask in prime_masks.values()):
        raise AssertionError("Pinned circuit invariant failed.")

    columns_by_key = defaultdict(list)
    for column, record in enumerate(records):
        columns_by_key[key(record)].append(column)

    carry_rows = set()
    for trajectory, columns in columns_by_key.items():
        if trajectory[0] != "trajectory":
            continue
        ordered = sorted((records[column]["provenance"]["exponent"], column) for column in columns)
        for left_position, (left_exponent, left) in enumerate(ordered):
            for right_exponent, right in ordered[left_position + 1 :]:
                scale = multiplier(records[left]) ** (right_exponent - left_exponent)
                shared = []
                if records[right]["c"] == scale * records[left]["c"]:
                    shared.append(records[left]["c"])
                if records[left]["w"] == scale * records[right]["w"]:
                    shared.append(records[right]["w"])
                if not shared:
                    continue
                for prime, mask in prime_masks.items():
                    if (mask >> left) & 1 and (mask >> right) & 1 and any(value % prime == 0 for value in shared):
                        carry_rows.add(prime)

    row_classes = {}
    pair_counts = Counter()
    for prime, mask in prime_masks.items():
        occurrence_keys = sorted({key(records[column]) for column in range(166) if (mask >> column) & 1}, key=repr)
        base_pairs = 0
        metric_pairs = 0
        for left_index, left in enumerate(occurrence_keys):
            for right in occurrence_keys[left_index + 1 :]:
                common = bases(records[columns_by_key[left][0]]) & bases(records[columns_by_key[right][0]])
                if any(value % prime == 0 for value in common):
                    base_pairs += 1
                    pair_counts["base_inherited"] += 1
                else:
                    metric_pairs += 1
                    pair_counts["metric"] += 1
        row_classes[prime] = {
            "mask": mask,
            "trajectory_keys": len(occurrence_keys),
            "base_cross_pairs": base_pairs,
            "metric_cross_pairs": metric_pairs,
            "carry": prime in carry_rows,
        }

    predicates = {
        "all": lambda p, d: True,
        "carry": lambda p, d: d["carry"],
        "cross_any": lambda p, d: d["trajectory_keys"] > 1,
        "base_cross_any": lambda p, d: d["base_cross_pairs"] > 0,
        "base_cross_only": lambda p, d: d["base_cross_pairs"] > 0 and d["metric_cross_pairs"] == 0,
        "metric_cross_any": lambda p, d: d["metric_cross_pairs"] > 0,
        "metric_cross_only": lambda p, d: d["metric_cross_pairs"] > 0 and d["base_cross_pairs"] == 0,
        "metric_cross_no_carry": lambda p, d: d["metric_cross_pairs"] > 0 and not d["carry"],
        "metric_cross_only_no_carry": lambda p, d: d["metric_cross_pairs"] > 0 and d["base_cross_pairs"] == 0 and not d["carry"],
        "carry_or_base_cross": lambda p, d: d["carry"] or d["base_cross_pairs"] > 0,
        "neither_carry_nor_base_cross": lambda p, d: not d["carry"] and d["base_cross_pairs"] == 0,
    }
    stats = {}
    for name, predicate in predicates.items():
        rows = [data["mask"] for prime, data in row_classes.items() if predicate(prime, data)]
        row_rank = rank(rows)
        stats[name] = {
            "rows": len(rows),
            "rank": row_rank,
            "nullity": 166 - row_rank,
            "components": components(rows, 166),
        }

    output = {
        "status": "complete",
        "role": "factor-assisted fixed-circuit diagnosis",
        "input_hashes": {str(F98.relative_to(ROOT)): sha256(F98), str(F100.relative_to(ROOT)): sha256(F100)},
        "columns": 166,
        "prime_rows": len(prime_masks),
        "rank": rank(prime_masks.values()),
        "cross_key_pair_counts_with_row_multiplicity": dict(pair_counts),
        "category_stats": stats,
        "metric_cross_prime_min": min(prime for prime, data in row_classes.items() if data["metric_cross_pairs"]),
        "metric_cross_prime_max": max(prime for prime, data in row_classes.items() if data["metric_cross_pairs"]),
        "metric_cross_primes_above_784": sum(prime > 784 and data["metric_cross_pairs"] > 0 for prime, data in row_classes.items()),
        "base_cross_primes": sorted(prime for prime, data in row_classes.items() if data["base_cross_pairs"]),
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
