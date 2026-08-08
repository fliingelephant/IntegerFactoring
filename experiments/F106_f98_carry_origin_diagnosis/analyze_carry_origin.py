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
N = 202_537_109


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rank(rows, width):
    pivots = {}
    for value in rows:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in pivots:
                x ^= pivots[pivot]
            else:
                pivots[pivot] = x
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
        columns = []
        x = mask
        while x:
            bit = x & -x
            columns.append(bit.bit_length() - 1)
            x ^= bit
        if columns:
            incident.update(columns)
            for column in columns[1:]:
                union(columns[0], column)
    sizes = Counter(find(column) for column in incident)
    isolated = width - len(incident)
    return sorted(list(sizes.values()) + [1] * isolated, reverse=True)


def valuation(value, prime):
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def trajectory_key(record):
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


def multiplier(record):
    provenance = record["provenance"]
    if provenance["orientation"] == "u_power_times_v":
        return provenance["u"]
    return provenance["v"]


def main():
    public = json.loads(F98.read_text())
    diagnosis = json.loads(F100.read_text())
    certificate = public["decoder"]["first_useful_certificate"]
    records = certificate["witness_records"]
    factorizations = diagnosis["relation_factorizations"]
    if len(records) != 166 or len(factorizations) != 166:
        raise AssertionError("Pinned certificate length changed.")

    prime_masks = defaultdict(int)
    endpoint_parity = []
    for column, (record, factorization) in enumerate(zip(records, factorizations)):
        if record["P"] != factorization["P"] or record["c"] * record["w"] != record["P"]:
            raise AssertionError("Pinned record/factorization mismatch.")
        local = {}
        product = 1
        for prime, exponent in factorization["factors"]:
            product *= prime**exponent
            c_parity = valuation(record["c"], prime) & 1
            w_parity = valuation(record["w"], prime) & 1
            if (c_parity ^ w_parity) != (exponent & 1):
                raise AssertionError("Endpoint parity mismatch.")
            local[prime] = {"c": c_parity, "w": w_parity}
            if exponent & 1:
                prime_masks[prime] |= 1 << column
        if product != record["P"]:
            raise AssertionError("Incomplete pinned factorization.")
        endpoint_parity.append(local)

    if any(mask.bit_count() % 2 for mask in prime_masks.values()):
        raise AssertionError("The selected all-column vector is not a dependency.")

    by_trajectory = defaultdict(dict)
    for column, record in enumerate(records):
        provenance = record["provenance"]
        if provenance["kind"] == "feedback_trajectory":
            by_trajectory[trajectory_key(record)][provenance["exponent"]] = column

    carry_edges_by_prime = defaultdict(set)
    carry_state_counts = Counter()
    consecutive_selected_pairs = 0
    duplicate_zero_carry_pairs = 0
    for key, exponent_columns in by_trajectory.items():
        for exponent, left in exponent_columns.items():
            if exponent + 1 not in exponent_columns:
                continue
            right = exponent_columns[exponent + 1]
            consecutive_selected_pairs += 1
            left_record = records[left]
            right_record = records[right]
            r = multiplier(left_record)
            c_zero = right_record["c"] == r * left_record["c"]
            w_zero = left_record["w"] == r * right_record["w"]
            carry_state_counts[f"c_zero={int(c_zero)},w_zero={int(w_zero)}"] += 1
            if c_zero and w_zero:
                duplicate_zero_carry_pairs += 1
                if left_record["P"] != right_record["P"]:
                    raise AssertionError("Two zero carries did not duplicate P.")
            shared_values = []
            if c_zero:
                shared_values.append(left_record["c"])
            if w_zero:
                shared_values.append(right_record["w"])
            for prime, mask in prime_masks.items():
                if not ((mask >> left) & 1 and (mask >> right) & 1):
                    continue
                if any(value % prime == 0 for value in shared_values):
                    carry_edges_by_prime[prime].add((left, right))

    carry_chain_selected_pairs = 0
    carry_chain_state_counts = Counter()
    for key, exponent_columns in by_trajectory.items():
        ordered = sorted(exponent_columns.items())
        for left_position, (left_exponent, left) in enumerate(ordered):
            for right_exponent, right in ordered[left_position + 1 :]:
                r = multiplier(records[left])
                scale = r ** (right_exponent - left_exponent)
                c_chain = records[right]["c"] == scale * records[left]["c"]
                w_chain = records[left]["w"] == scale * records[right]["w"]
                if not (c_chain or w_chain):
                    continue
                carry_chain_selected_pairs += 1
                carry_chain_state_counts[f"c_chain={int(c_chain)},w_chain={int(w_chain)}"] += 1
                shared_values = []
                if c_chain:
                    shared_values.append(records[left]["c"])
                if w_chain:
                    shared_values.append(records[right]["w"])
                for prime, mask in prime_masks.items():
                    if not ((mask >> left) & 1 and (mask >> right) & 1):
                        continue
                    if any(value % prime == 0 for value in shared_values):
                        carry_edges_by_prime[prime].add((left, right))

    row_data = {}
    for prime, mask in sorted(prime_masks.items()):
        occurrence = [column for column in range(166) if (mask >> column) & 1]
        keys = {trajectory_key(records[column]) for column in occurrence}
        edges = carry_edges_by_prime[prime]
        parent = {column: column for column in occurrence}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for left, right in edges:
            x = find(left)
            y = find(right)
            if x != y:
                parent[y] = x
        carry_connected = bool(edges) and len({find(column) for column in occurrence}) == 1
        row_data[prime] = {
            "mask": mask,
            "degree": len(occurrence),
            "trajectory_count": len(keys),
            "carry_edge_count": len(edges),
            "carry_connected": carry_connected,
        }

    n = N.bit_length()
    bound = n * n
    categories = {
        "all": lambda p, data: True,
        "small_at_most_n_squared": lambda p, data: p <= bound,
        "large_above_n_squared": lambda p, data: p > bound,
        "has_carry_edge": lambda p, data: data["carry_edge_count"] > 0,
        "carry_connected": lambda p, data: data["carry_connected"],
        "no_carry_edge": lambda p, data: data["carry_edge_count"] == 0,
        "one_trajectory": lambda p, data: data["trajectory_count"] == 1,
        "cross_trajectory": lambda p, data: data["trajectory_count"] > 1,
        "large_cross_trajectory": lambda p, data: p > bound and data["trajectory_count"] > 1,
    }
    category_stats = {}
    for name, predicate in categories.items():
        selected = [data["mask"] for prime, data in row_data.items() if predicate(prime, data)]
        category_stats[name] = {
            "rows": len(selected),
            "rank": rank(selected, 166),
            "nullity": 166 - rank(selected, 166),
            "components": components(selected, 166),
        }

    row_classes = Counter()
    for prime, data in row_data.items():
        row_classes[
            (
                "small" if prime <= bound else "large",
                "carry" if data["carry_edge_count"] else "noncarry",
                "cross" if data["trajectory_count"] > 1 else "local",
            )
        ] += 1

    output = {
        "status": "complete",
        "role": "factor-assisted finite diagnosis",
        "N": N,
        "n": n,
        "public_bound": bound,
        "input_hashes": {str(F98.relative_to(ROOT)): sha256(F98), str(F100.relative_to(ROOT)): sha256(F100)},
        "columns": 166,
        "prime_rows": len(prime_masks),
        "full_rank": rank(list(prime_masks.values()), 166),
        "full_nullity": 166 - rank(list(prime_masks.values()), 166),
        "consecutive_selected_pairs": consecutive_selected_pairs,
        "carry_state_counts": dict(sorted(carry_state_counts.items())),
        "two_zero_carry_selected_pairs": duplicate_zero_carry_pairs,
        "carry_chain_selected_pairs": carry_chain_selected_pairs,
        "carry_chain_state_counts": dict(sorted(carry_chain_state_counts.items())),
        "row_class_counts": {"|".join(key): value for key, value in sorted(row_classes.items())},
        "category_stats": category_stats,
        "largest_prime": max(prime_masks),
        "largest_no_carry_prime": max(prime for prime, data in row_data.items() if not data["carry_edge_count"]),
        "degree_two_rows": sum(data["degree"] == 2 for data in row_data.values()),
        "degree_two_with_carry_edge": sum(data["degree"] == 2 and data["carry_edge_count"] for data in row_data.values()),
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
