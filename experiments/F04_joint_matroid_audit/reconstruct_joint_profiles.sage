#!/usr/bin/env sage
"""Fresh joint-field reconstruction and low-tail Pluecker-support audit.

For each shift, construct H_a once over Z/NZ, hash that global coefficient
vector, and copy that same vector into both local matrices.  For P11, the
first A columns form a basis over both fields.  Normalize the 11 remaining
columns by that basis and exhaust all maximal minors using one or two tail
columns.
"""

import argparse
import hashlib
import json
from pathlib import Path
import time


FAMILY = "F04_joint_matroid_audit"
INSTANCES = {
    "P14": {
        "N": ZZ(79403),
        "p": ZZ(271),
        "q": ZZ(293),
        "r": 269,
        "shift_bound": 266,
    },
    "P11": {
        "N": ZZ(20000000499999937),
        "p": ZZ(100000007),
        "q": ZZ(199999991),
        "r": 2953,
        "shift_bound": 2942,
    },
}


def encoded_row(values):
    return json.dumps(values, separators=(",", ":")).encode("ascii")


def matrix_row_sha256(input_matrix):
    aggregate = hashlib.sha256()
    row_hashes = []
    for row_index in range(input_matrix.nrows()):
        encoded = encoded_row([int(value) for value in input_matrix[row_index]])
        row_hashes.append(hashlib.sha256(encoded).hexdigest())
        aggregate.update(len(encoded).to_bytes(8, "big"))
        aggregate.update(encoded)
    return aggregate.hexdigest(), row_hashes


def projective_keys(normalized, left, right):
    keys = []
    for row_index in range(normalized.nrows()):
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
        nonnull = [key for key in keys if key is not None]
        counts = {}
        for key in nonnull:
            counts[key] = counts.get(key, 0) + 1
        return binomial(len(nonnull), 2) - sum(binomial(count, 2) for count in counts.values())

    left_nonzero = unequal_nonnull_count(left_keys)
    right_nonzero = unequal_nonnull_count(right_keys)
    joint_rows = [
        (left_key, right_key)
        for left_key, right_key in zip(left_keys, right_keys)
        if left_key is not None and right_key is not None
    ]
    left_counts = {}
    right_counts = {}
    joint_counts = {}
    for left_key, right_key in joint_rows:
        left_counts[left_key] = left_counts.get(left_key, 0) + 1
        right_counts[right_key] = right_counts.get(right_key, 0) + 1
        joint_counts[(left_key, right_key)] = joint_counts.get((left_key, right_key), 0) + 1
    both_nonzero = (
        binomial(len(joint_rows), 2)
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


def local_profile(local_matrix, shift_bound):
    prefix = local_matrix.matrix_from_columns(range(shift_bound))
    determinant_started = time.monotonic()
    determinant = prefix.det()
    determinant_seconds = time.monotonic() - determinant_started
    if determinant:
        rank = shift_bound
        pivots = list(range(shift_bound))
        rank_seconds = 0.0
    else:
        rank_started = time.monotonic()
        rank = local_matrix.rank()
        pivots = list(local_matrix.pivots())
        rank_seconds = time.monotonic() - rank_started
    return prefix, {
        "canonical_prefix_determinant": int(determinant),
        "canonical_prefix_determinant_nonzero": bool(determinant),
        "full_matrix_rank": int(rank),
        "lexicographic_pivot_columns": pivots,
        "determinant_seconds": determinant_seconds,
        "rank_seconds_after_zero_determinant": rank_seconds,
    }


def audit_p11_tail_minors(local_matrices, prefixes, prefix_determinants, parameters):
    shift_bound = parameters["shift_bound"]
    r = parameters["r"]
    fields = {key: local_matrices[key].base_ring() for key in ("p", "q")}
    normalized = {}
    solve_seconds = {}
    for key in ("p", "q"):
        solve_started = time.monotonic()
        tail = local_matrices[key].matrix_from_columns(range(shift_bound, r))
        normalized[key] = prefixes[key].solve_right(tail)
        solve_seconds[key] = time.monotonic() - solve_started
        assert prefixes[key] * normalized[key] == tail

    normalized_hashes = {}
    normalized_row_hashes = {}
    one_tail_zero_positions = {}
    for key in ("p", "q"):
        normalized_hashes[key], normalized_row_hashes[key] = matrix_row_sha256(normalized[key])
        one_tail_zero_positions[key] = [
            [row_index, tail_index]
            for row_index in range(shift_bound)
            for tail_index in range(r - shift_bound)
            if not normalized[key][row_index, tail_index]
        ]
    one_tail_zero_sets = {
        key: {tuple(position) for position in positions}
        for key, positions in one_tail_zero_positions.items()
    }

    tail_pair_summaries = []
    first_separator = None
    total_p_zero_q_nonzero = 0
    total_q_zero_p_nonzero = 0
    for left in range(r - shift_bound):
        for right in range(left + 1, r - shift_bound):
            keys_p = projective_keys(normalized["p"], left, right)
            keys_q = projective_keys(normalized["q"], left, right)
            p_nonzero, q_nonzero, both_nonzero = nonzero_pair_counts(keys_p, keys_q)
            p_zero_q_nonzero = q_nonzero - both_nonzero
            q_zero_p_nonzero = p_nonzero - both_nonzero
            total_p_zero_q_nonzero += p_zero_q_nonzero
            total_q_zero_p_nonzero += q_zero_p_nonzero
            tail_pair_summaries.append({
                "tail_local_indices": [left, right],
                "tail_global_columns": [shift_bound + left, shift_bound + right],
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
                    "tail_global_columns": [shift_bound + left, shift_bound + right],
                    "zero_field": zero_field,
                }

    if first_separator is not None:
        row_i, row_j = first_separator["removed_prefix_columns"]
        tail_u, tail_v = first_separator["tail_local_indices"]
        sign = -1 if (row_i + row_j + 1) % 2 else 1
        selected_columns = [
            column for column in range(shift_bound)
            if column not in (row_i, row_j)
        ] + first_separator["tail_global_columns"]
        local_two_by_two = {}
        formula_determinants = {}
        direct_determinants = {}
        direct_seconds = {}
        for key in ("p", "q"):
            minor = (
                normalized[key][row_i, tail_u] * normalized[key][row_j, tail_v]
                - normalized[key][row_i, tail_v] * normalized[key][row_j, tail_u]
            )
            local_two_by_two[key] = int(minor)
            formula = fields[key](sign) * fields[key](prefix_determinants[key]) * minor
            formula_determinants[key] = int(formula)
            direct_started = time.monotonic()
            direct = local_matrices[key].matrix_from_columns(selected_columns).det()
            direct_seconds[key] = time.monotonic() - direct_started
            direct_determinants[key] = int(direct)
            assert direct == formula
        global_residue = int(crt(
            ZZ(direct_determinants["p"]),
            ZZ(direct_determinants["q"]),
            parameters["p"],
            parameters["q"],
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
            "global_maximal_minor_gcd_with_N": int(gcd(global_residue, parameters["N"])),
        })

    return {
        "normalization": "C_l = B_l^(-1) T_l for the common first-A-column basis B and 11-column tail T",
        "tail_column_count": r - shift_bound,
        "solve_seconds": solve_seconds,
        "normalized_matrix_sha256": normalized_hashes,
        "normalized_row_sha256": normalized_row_hashes,
        "one_tail": {
            "minor_count_per_field": shift_bound * (r - shift_bound),
            "p_zero_count": len(one_tail_zero_positions["p"]),
            "q_zero_count": len(one_tail_zero_positions["q"]),
            "p_zero_q_nonzero_positions": sorted(one_tail_zero_sets["p"] - one_tail_zero_sets["q"]),
            "q_zero_p_nonzero_positions": sorted(one_tail_zero_sets["q"] - one_tail_zero_sets["p"]),
        },
        "two_tail": {
            "tail_pair_count": binomial(r - shift_bound, 2),
            "minor_count_per_field": binomial(r - shift_bound, 2) * binomial(shift_bound, 2),
            "p_zero_q_nonzero_count": total_p_zero_q_nonzero,
            "q_zero_p_nonzero_count": total_q_zero_p_nonzero,
            "tail_pair_summaries": tail_pair_summaries,
            "first_separator": first_separator,
        },
        "unscanned_tail_orders": [3, r - shift_bound],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", choices=sorted(INSTANCES), required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    parameters = INSTANCES[args.instance]
    assert parameters["N"] == parameters["p"] * parameters["q"]
    started = time.monotonic()

    residue_ring = Integers(parameters["N"])
    polynomial_ring = PolynomialRing(residue_ring, "x")
    x = polynomial_ring.gen()
    modulus = x**parameters["r"] - 1
    fields = {"p": GF(parameters["p"]), "q": GF(parameters["q"])}
    local_matrices = {
        key: matrix(field, parameters["shift_bound"], parameters["r"])
        for key, field in fields.items()
    }
    global_matrix_hash = hashlib.sha256()
    global_row_hashes = []
    raw_local_zero_counts = {"p": 0, "q": 0}
    raw_global_nonunit_count = 0
    construction_started = time.monotonic()

    for row_index, shift in enumerate(range(1, parameters["shift_bound"] + 1)):
        error = (
            power_mod(x + residue_ring(shift), parameters["N"], modulus)
            - x**(parameters["N"] % parameters["r"])
            - residue_ring(shift)
        ) % modulus
        coefficients = [int(error[index]) for index in range(parameters["r"])]
        encoded = encoded_row(coefficients)
        global_row_hashes.append(hashlib.sha256(encoded).hexdigest())
        global_matrix_hash.update(len(encoded).to_bytes(8, "big"))
        global_matrix_hash.update(encoded)
        raw_global_nonunit_count += sum(gcd(value, parameters["N"]) != 1 for value in coefficients)
        for key in ("p", "q"):
            raw_local_zero_counts[key] += sum(value % parameters[key] == 0 for value in coefficients)
            local_matrices[key][row_index] = vector(fields[key], coefficients)
        if (row_index + 1) % 100 == 0 or row_index + 1 == parameters["shift_bound"]:
            print(
                f"family={FAMILY} instance={args.instance} "
                f"joint_rows={row_index + 1}/{parameters['shift_bound']}",
                flush=True,
            )
    construction_seconds = time.monotonic() - construction_started

    prefixes = {}
    profiles = {}
    for key in ("p", "q"):
        prefixes[key], profiles[key] = local_profile(local_matrices[key], parameters["shift_bound"])
        profiles[key]["characteristic"] = int(parameters[key])
        profiles[key]["raw_local_zero_count"] = int(raw_local_zero_counts[key])

    prefix_crt = int(crt(
        ZZ(profiles["p"]["canonical_prefix_determinant"]),
        ZZ(profiles["q"]["canonical_prefix_determinant"]),
        parameters["p"],
        parameters["q"],
    ))
    tail_audit = None
    if args.instance == "P11":
        assert profiles["p"]["canonical_prefix_determinant_nonzero"]
        assert profiles["q"]["canonical_prefix_determinant_nonzero"]
        tail_audit = audit_p11_tail_minors(
            local_matrices,
            prefixes,
            {
                "p": profiles["p"]["canonical_prefix_determinant"],
                "q": profiles["q"]["canonical_prefix_determinant"],
            },
            parameters,
        )

    source_path = Path(__file__).resolve()
    output = {
        "approach_family": FAMILY,
        "instance": args.instance,
        "inputs": {
            "N": int(parameters["N"]),
            "p": int(parameters["p"]),
            "q": int(parameters["q"]),
            "r": parameters["r"],
            "shift_start": 1,
            "shift_stop": parameters["shift_bound"],
        },
        "joint_global_construction": "each H_a is formed once in (Z/NZ)[X]/(X^r-1), then the same coefficient vector is assigned to both local rows in the same loop iteration",
        "matrix_shape": [parameters["shift_bound"], parameters["r"]],
        "canonical_prefix_shape": [parameters["shift_bound"], parameters["shift_bound"]],
        "global_matrix_sha256": global_matrix_hash.hexdigest(),
        "global_row_sha256": global_row_hashes,
        "raw_global_nonunit_count": int(raw_global_nonunit_count),
        "local_profiles": profiles,
        "global_prefix_determinant_mod_N_from_CRT": prefix_crt,
        "global_prefix_determinant_gcd_with_N": int(gcd(prefix_crt, parameters["N"])),
        "p11_tail_audit": tail_audit,
        "construction_seconds": construction_seconds,
        "elapsed_seconds": time.monotonic() - started,
        "source": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
    }
    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2, default=int) + "\n", encoding="utf-8")
    print(json.dumps({
        "instance": args.instance,
        "global_matrix_sha256": output["global_matrix_sha256"],
        "local_ranks": [profiles["p"]["full_matrix_rank"], profiles["q"]["full_matrix_rank"]],
        "prefix_determinants": [profiles["p"]["canonical_prefix_determinant"], profiles["q"]["canonical_prefix_determinant"]],
        "tail_separator": None if tail_audit is None else tail_audit["two_tail"]["first_separator"],
        "elapsed_seconds": output["elapsed_seconds"],
    }, sort_keys=True), flush=True)


main()
