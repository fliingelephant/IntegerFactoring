#!/usr/bin/env sage
"""Compare all P11 maximal-minor supports with one or two tail columns."""

import argparse
import hashlib
import json
from pathlib import Path
import time


N = ZZ(20000000499999937)
P = ZZ(100000007)
Q = ZZ(199999991)
R = 2953
A = 2942


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def projective_keys(normalized, left, right):
    keys = []
    for row_index in range(A):
        x_value = normalized[row_index, left]
        y_value = normalized[row_index, right]
        if not x_value and not y_value:
            keys.append(None)
        elif not y_value:
            keys.append(("infinity",))
        else:
            keys.append(("finite", int(x_value / y_value)))
    return keys


def nonzero_pair_counts(left_keys, right_keys):
    def unequal_nonnull_count(keys):
        counts = {}
        nonnull_count = 0
        for key in keys:
            if key is not None:
                nonnull_count += 1
                counts[key] = counts.get(key, 0) + 1
        return binomial(nonnull_count, 2) - sum(binomial(count, 2) for count in counts.values())

    left_nonzero = unequal_nonnull_count(left_keys)
    right_nonzero = unequal_nonnull_count(right_keys)
    left_counts = {}
    right_counts = {}
    joint_counts = {}
    joint_row_count = 0
    for left_key, right_key in zip(left_keys, right_keys):
        if left_key is not None and right_key is not None:
            joint_row_count += 1
            left_counts[left_key] = left_counts.get(left_key, 0) + 1
            right_counts[right_key] = right_counts.get(right_key, 0) + 1
            joint_counts[(left_key, right_key)] = joint_counts.get((left_key, right_key), 0) + 1
    both_nonzero = (
        binomial(joint_row_count, 2)
        - sum(binomial(count, 2) for count in left_counts.values())
        - sum(binomial(count, 2) for count in right_counts.values())
        + sum(binomial(count, 2) for count in joint_counts.values())
    )
    return int(left_nonzero), int(right_nonzero), int(both_nonzero)


def first_zero_here_nonzero_other(here_keys, other_keys):
    other_representatives = {}
    for row_index, key in enumerate(other_keys):
        if key is not None and key not in other_representatives:
            other_representatives[key] = row_index
    if len(other_representatives) >= 2:
        for row_index, here_key in enumerate(here_keys):
            other_key = other_keys[row_index]
            if here_key is None and other_key is not None:
                for candidate_key, candidate_index in other_representatives.items():
                    if candidate_key != other_key:
                        return tuple(sorted((row_index, candidate_index)))

    here_groups = {}
    for row_index, key in enumerate(here_keys):
        if key is not None:
            here_groups.setdefault(key, []).append(row_index)
    for rows in here_groups.values():
        representatives = {}
        for row_index in rows:
            other_key = other_keys[row_index]
            if other_key is not None and other_key not in representatives:
                representatives[other_key] = row_index
                if len(representatives) == 2:
                    return tuple(sorted(representatives.values()))
    return None


parser = argparse.ArgumentParser()
parser.add_argument("--build-summary", required=True)
parser.add_argument("--p-solve", required=True)
parser.add_argument("--q-solve", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
started = time.monotonic()
summary_paths = {
    "build": Path(args.build_summary).resolve(),
    "p": Path(args.p_solve).resolve(),
    "q": Path(args.q_solve).resolve(),
}
summaries = {key: json.loads(path.read_text()) for key, path in summary_paths.items()}
assert summaries["build"]["prefix_determinants"] == {"p": 56136614, "q": 132391112}
assert summaries["build"]["prefix_determinant_nonzero_both"]
assert summaries["p"]["inputs"]["characteristic"] == int(P)
assert summaries["q"]["inputs"]["characteristic"] == int(Q)

normalized = {}
local_matrices = {}
for key in ("p", "q"):
    normalized_path = Path(summaries[key]["normalized_artifact"]["path"])
    matrix_path = Path(summaries[key]["matrix_artifact"]["path"])
    assert sha256(normalized_path) == summaries[key]["normalized_artifact"]["sha256"]
    assert sha256(matrix_path) == summaries[key]["matrix_artifact"]["sha256"]
    assert summaries[key]["matrix_artifact"]["sha256"] == summaries["build"]["matrix_artifacts"][key]["sha256"]
    normalized[key] = load(str(normalized_path))
    assert normalized[key].dimensions() == (A, R - A)
    local_matrices[key] = load(str(matrix_path))
    assert local_matrices[key].dimensions() == (A, R)
    print(f"stage=load field={key}", flush=True)

one_tail_zero_sets = {
    key: {
        (row_index, tail_index)
        for row_index in range(A)
        for tail_index in range(R - A)
        if not normalized[key][row_index, tail_index]
    }
    for key in ("p", "q")
}
tail_pair_summaries = []
first_separator = None
total_p_zero_q_nonzero = 0
total_q_zero_p_nonzero = 0
for left in range(R - A):
    for right in range(left + 1, R - A):
        keys_p = projective_keys(normalized["p"], left, right)
        keys_q = projective_keys(normalized["q"], left, right)
        p_nonzero, q_nonzero, both_nonzero = nonzero_pair_counts(keys_p, keys_q)
        p_zero_q_nonzero = q_nonzero - both_nonzero
        q_zero_p_nonzero = p_nonzero - both_nonzero
        total_p_zero_q_nonzero += p_zero_q_nonzero
        total_q_zero_p_nonzero += q_zero_p_nonzero
        tail_pair_summaries.append({
            "tail_local_indices": [left, right],
            "tail_global_columns": [A + left, A + right],
            "p_zero_q_nonzero_count": p_zero_q_nonzero,
            "q_zero_p_nonzero_count": q_zero_p_nonzero,
        })
        if first_separator is None and (p_zero_q_nonzero or q_zero_p_nonzero):
            if p_zero_q_nonzero:
                removed = first_zero_here_nonzero_other(keys_p, keys_q)
                zero_field = "p"
            else:
                removed = first_zero_here_nonzero_other(keys_q, keys_p)
                zero_field = "q"
            assert removed is not None
            first_separator = {
                "removed_prefix_columns": list(removed),
                "tail_local_indices": [left, right],
                "tail_global_columns": [A + left, A + right],
                "zero_field": zero_field,
            }
    print(f"stage=support-scan first_tail={left}/{R - A - 2}", flush=True)

if first_separator is not None:
    row_i, row_j = first_separator["removed_prefix_columns"]
    tail_u, tail_v = first_separator["tail_local_indices"]
    sign = -1 if (row_i + row_j + 1) % 2 else 1
    selected_columns = [
        column for column in range(A) if column not in (row_i, row_j)
    ] + first_separator["tail_global_columns"]
    local_two_by_two = {}
    formula_determinants = {}
    direct_determinants = {}
    direct_seconds = {}
    for key in ("p", "q"):
        field = local_matrices[key].base_ring()
        local_two_by_two[key] = int(
            normalized[key][row_i, tail_u] * normalized[key][row_j, tail_v]
            - normalized[key][row_i, tail_v] * normalized[key][row_j, tail_u]
        )
        formula_determinants[key] = int(
            field(sign)
            * field(summaries["build"]["prefix_determinants"][key])
            * field(local_two_by_two[key])
        )
        direct_started = time.monotonic()
        direct_determinants[key] = int(
            local_matrices[key].matrix_from_columns(selected_columns).det()
        )
        direct_seconds[key] = time.monotonic() - direct_started
        assert direct_determinants[key] == formula_determinants[key]
        print(
            f"stage=direct-minor field={key} value={direct_determinants[key]}",
            flush=True,
        )
    global_residue = int(crt(
        ZZ(direct_determinants["p"]), ZZ(direct_determinants["q"]), P, Q
    ))
    first_separator.update({
        "selected_column_order": "all prefix columns except the two removed, then the two tail columns in increasing order",
        "selected_column_count": len(selected_columns),
        "replacement_sign": sign,
        "normalized_two_by_two_determinants": local_two_by_two,
        "maximal_minor_formula_determinants": formula_determinants,
        "maximal_minor_direct_determinants": direct_determinants,
        "direct_determinant_seconds": direct_seconds,
        "global_maximal_minor_mod_N_from_CRT": global_residue,
        "global_maximal_minor_gcd_with_N": int(gcd(global_residue, N)),
    })

source_path = Path(__file__).resolve()
output = {
    "approach_family": "F04_joint_matroid_audit",
    "stage": "P11-low-tail-Pluecker-support-v1",
    "normalization": "C_l = B_l^(-1) T_l for the common first-A-column basis B and 11-column tail T",
    "one_tail": {
        "minor_count_per_field": A * (R - A),
        "p_zero_count": len(one_tail_zero_sets["p"]),
        "q_zero_count": len(one_tail_zero_sets["q"]),
        "p_zero_q_nonzero_positions": sorted(one_tail_zero_sets["p"] - one_tail_zero_sets["q"]),
        "q_zero_p_nonzero_positions": sorted(one_tail_zero_sets["q"] - one_tail_zero_sets["p"]),
    },
    "two_tail": {
        "tail_pair_count": int(binomial(R - A, 2)),
        "minor_count_per_field": int(binomial(R - A, 2) * binomial(A, 2)),
        "p_zero_q_nonzero_count": total_p_zero_q_nonzero,
        "q_zero_p_nonzero_count": total_q_zero_p_nonzero,
        "tail_pair_summaries": tail_pair_summaries,
        "first_separator": first_separator,
    },
    "unscanned_tail_orders": [3, R - A],
    "source_artifacts": {
        key: {"path": str(path), "sha256": sha256(path)}
        for key, path in summary_paths.items()
    },
    "elapsed_seconds": time.monotonic() - started,
    "source": str(source_path),
    "source_sha256": sha256(source_path),
}
output_path = Path(args.output).resolve()
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(
    json.dumps(output, indent=2, sort_keys=True, default=int) + "\n",
    encoding="utf-8",
)
print(json.dumps({
    "stage": output["stage"],
    "one_tail_zero_counts": [output["one_tail"]["p_zero_count"], output["one_tail"]["q_zero_count"]],
    "two_tail_mismatch_counts": [total_p_zero_q_nonzero, total_q_zero_p_nonzero],
    "first_separator": first_separator,
    "elapsed_seconds": output["elapsed_seconds"],
}, sort_keys=True, default=int), flush=True)
