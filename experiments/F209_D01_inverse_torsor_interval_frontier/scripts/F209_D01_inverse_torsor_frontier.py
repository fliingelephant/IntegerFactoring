#!/usr/bin/env python3
"""F209-D01: exact F207 inverse-torsor interval frontier.

The public constructor accepts only N. Hidden p,q values are passed only to
the dataset generator and the post-construction label/audit function.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import random
import statistics
import sys
import time
from pathlib import Path

import sympy
from sympy import factorint, nextprime, primerange


RUN_ID = "F209-D01"
TRAIN_SEED = 20501
HOLDOUT_SEED = 20502
WORK_PROXY_POWER = 4


def ceil_div(a, b):
    return -((-a) // b)


def odd_count(lo, hi):
    if lo > hi:
        return 0
    first = lo if lo & 1 else lo + 1
    return 0 if first > hi else (hi - first) // 2 + 1


def odd_progression(residue, modulus, lo, hi):
    """Exact odd integers in [lo,hi] congruent to residue modulo modulus.

    Return (first,last,step,count), or None for the empty set.
    """
    residue %= modulus
    if modulus & 1:
        step = 2 * modulus
        base = residue if residue & 1 else residue + modulus
    else:
        if not residue & 1:
            return None
        step = modulus
        base = residue
    first = base + ceil_div(lo - base, step) * step
    if first > hi:
        return None
    last = base + ((hi - base) // step) * step
    return (first, last, step, (last - first) // step + 1)


def factor_dict(value):
    return {int(p): int(e) for p, e in factorint(value).items()}


def merge_max(f, g):
    return {p: max(f.get(p, 0), g.get(p, 0)) for p in set(f) | set(g)}


def value_from_factorization(f):
    value = 1
    for p, e in f.items():
        value *= p**e
    return value


def phi_from_factorization(f):
    value = 1
    for p, e in f.items():
        value *= (p - 1) * p ** (e - 1)
    return value


def incremental_crt(left, left_modulus, right, right_modulus):
    if left_modulus == 1:
        return right % right_modulus
    step = ((right - left) * pow(left_modulus, -1, right_modulus)) % right_modulus
    return (left + left_modulus * step) % (left_modulus * right_modulus)


def batch_inverses(values, modulus):
    if not values:
        return []
    prefix = [1]
    product = 1
    for value in values:
        product = product * value % modulus
        prefix.append(product)
    inverse_product = pow(product, -1, modulus)
    out = [0] * len(values)
    for index in range(len(values) - 1, -1, -1):
        out[index] = inverse_product * prefix[index] % modulus
        inverse_product = inverse_product * values[index] % modulus
    return out


def encode_branch(u, payload):
    x, y, pp, qp = payload
    return [u, x, y, list(pp), list(qp)]


def frontier_digest(frontier):
    digest = hashlib.sha256()
    ordered = sorted(frontier)
    for u in ordered:
        digest.update(
            json.dumps(encode_branch(u, frontier[u]), separators=(",", ":")).encode()
        )
        digest.update(b"\n")
    sample_keys = ordered[:8]
    if len(ordered) > 8:
        sample_keys += ordered[-8:]
    return digest.hexdigest(), [encode_branch(u, frontier[u]) for u in sample_keys]


def public_factor_covariates(K, E, M, fK, fE, components):
    largest_index, largest = max(enumerate(components), key=lambda item: item[1][0])
    largest_power, _, _, _, _ = largest
    return {
        "omega_K": len(fK),
        "omega_E": len(fE),
        "omega_M": len(components),
        "log2_M": math.log2(M),
        "log2_gcd_KE": math.log2(max(1, math.gcd(K, E))),
        "largest_component_log_fraction": math.log2(largest_power) / math.log2(M),
        "largest_component_position_fraction": (largest_index + 1) / len(components),
        "K_dominant_components": sum(source == "K" for _, _, _, source, _ in components),
        "E_dominant_components": sum(source == "E" for _, _, _, source, _ in components),
        "tied_components": sum(source == "tie" for _, _, _, source, _ in components),
        "largest_exponent_M": max(exponent for _, _, exponent, _, _ in components),
    }


def build_public_geometry(N, max_p_representatives):
    """Construct the complete declared frontier using N only."""
    B = math.isqrt(N)
    K = (N - 1) // 2
    E = N - B * B
    gcd_en = math.gcd(E, N)
    fK = factor_dict(K)
    fE = factor_dict(E)
    base = {
        "N": N,
        "n": N.bit_length(),
        "B": B,
        "K": K,
        "E": E,
        "gcd_EN": gcd_en,
        "factor_K": fK,
        "factor_E": fE,
    }
    if 1 < gcd_en < N:
        base.update({
            "status": "public_easy_gcdE",
            "public_factor": gcd_en,
            "M": None,
            "R": None,
            "factor_M": None,
            "components": [],
            "covariates": None,
            "stages": [],
            "summary": None,
        })
        return base, []

    fM = merge_max(fK, fE)
    M = value_from_factorization(fM)
    components = []
    for prime, exponent in fM.items():
        power = prime**exponent
        k_exp = fK.get(prime, 0)
        e_exp = fE.get(prime, 0)
        if k_exp > e_exp:
            source = "K"
            local_root = 1
        elif e_exp > k_exp:
            source = "E"
            local_root = B % power
        else:
            source = "tie"
            local_root = 1
        components.append((power, prime, exponent, source, local_root))
    components.sort(key=lambda row: (row[0], row[1]))

    p_bounds = (math.isqrt(N // 2) + 1, B)
    q_bounds = (B + 1, math.isqrt(2 * N - 1))
    p_representatives = odd_count(*p_bounds)
    if p_representatives > max_p_representatives:
        raise RuntimeError(
            f"P representative cap exceeded for N={N}: "
            f"{p_representatives}>{max_p_representatives}"
        )

    old_modulus = 1
    root = 0
    frontier = {0: None}
    frontier_history = []
    stages = []
    torsor_size = 1
    total_iterations = 0
    first_global_unique = None
    first_public_decode = None
    public_decode_factor = None

    for depth, (power, prime, exponent, source, local_root) in enumerate(components, 1):
        modulus = old_modulus * power
        root = incremental_crt(root, old_modulus, local_root, power)
        assert root * root % modulus == N % modulus
        phi_component = (prime - 1) * prime ** (exponent - 1)
        torsor_size *= phi_component
        previous_width = len(frontier)
        potential_children = previous_width * phi_component

        if potential_children <= p_representatives:
            mode = "crt_expand"
            inverse_old = pow(old_modulus, -1, power) if old_modulus != 1 else 0
            candidates = []
            for parent in sorted(frontier):
                for local_u in range(1, power):
                    if local_u % prime == 0:
                        continue
                    if old_modulus == 1:
                        child = local_u
                    else:
                        lift = ((local_u - parent) * inverse_old) % power
                        child = parent + old_modulus * lift
                    candidates.append(child)
            generator_iterations = potential_children
            assert len(candidates) == potential_children
        else:
            mode = "small_interval_scan"
            inverse_root = pow(root, -1, modulus)
            parent_keys = set(frontier)
            candidate_set = set()
            first_p = p_bounds[0] if p_bounds[0] & 1 else p_bounds[0] + 1
            for representative in range(first_p, p_bounds[1] + 1, 2):
                if math.gcd(representative, modulus) != 1:
                    continue
                child = representative % modulus * inverse_root % modulus
                if child % old_modulus in parent_keys:
                    candidate_set.add(child)
            candidates = sorted(candidate_set)
            generator_iterations = p_representatives

        total_iterations += generator_iterations
        p_live = []
        p_payloads = []
        for u in candidates:
            x = root * u % modulus
            p_progression = odd_progression(x, modulus, *p_bounds)
            if p_progression is not None:
                p_live.append(u)
                p_payloads.append((x, p_progression))

        inverses_x = batch_inverses([row[0] for row in p_payloads], modulus)
        next_frontier = {}
        q_live_width = 0
        for u, (x, p_progression), inverse_x in zip(p_live, p_payloads, inverses_x):
            y = N * inverse_x % modulus
            q_progression = odd_progression(y, modulus, *q_bounds)
            if q_progression is None:
                continue
            q_live_width += 1
            if not (
                p_progression[0] * q_progression[0]
                <= N
                <= p_progression[1] * q_progression[1]
            ):
                continue
            next_frontier[u] = (x, y, p_progression, q_progression)

        p_live_width = len(p_live)
        live_width = len(next_frontier)
        assert live_width > 0
        digest, sample = frontier_digest(next_frontier)

        decoded_factor = None
        if live_width == 1:
            if first_global_unique is None:
                first_global_unique = depth
            only_payload = next(iter(next_frontier.values()))
            pp = only_payload[2]
            qp = only_payload[3]
            if pp[3] == 1 and qp[3] == 1 and pp[0] * qp[0] == N:
                decoded_factor = pp[0]
                if first_public_decode is None:
                    first_public_decode = depth
                    public_decode_factor = decoded_factor

        stage = {
            "depth": depth,
            "component": {
                "prime": prime,
                "exponent": exponent,
                "power": power,
                "source": source,
                "local_root": local_root,
            },
            "modulus": modulus,
            "root": root,
            "torsor_size_phi_modulus": torsor_size,
            "previous_frontier_width": previous_width,
            "algebraic_children": potential_children,
            "generator_mode": mode,
            "generator_iterations": generator_iterations,
            "generated_unique_candidates": len(candidates),
            "p_live_width": p_live_width,
            "q_live_width": q_live_width,
            "live_frontier_width": live_width,
            "pruned_by_p_interval": potential_children - p_live_width,
            "pruned_by_q_interval": p_live_width - q_live_width,
            "pruned_by_product_interval": q_live_width - live_width,
            "pruned_total": potential_children - live_width,
            "frontier_sha256": digest,
            "frontier_sample": sample,
            "public_singleton_product_factor": decoded_factor,
        }
        stages.append(stage)
        frontier_history.append(set(next_frontier))
        frontier = next_frontier
        old_modulus = modulus

    assert old_modulus == M
    assert root * root % M == N % M
    assert torsor_size == phi_from_factorization(fM)
    n = N.bit_length()
    proxy = n**WORK_PROXY_POWER
    max_frontier = max(stage["live_frontier_width"] for stage in stages)
    max_iterations = max(stage["generator_iterations"] for stage in stages)
    summary = {
        "p_bounds": list(p_bounds),
        "q_bounds": list(q_bounds),
        "odd_p_representatives": p_representatives,
        "max_frontier_width": max_frontier,
        "max_generator_iterations": max_iterations,
        "total_generator_iterations": total_iterations,
        "first_global_unique_depth": first_global_unique,
        "first_public_decode_depth": first_public_decode,
        "public_decode_factor": public_decode_factor,
        "final_frontier_width": len(frontier),
        "work_proxy": proxy,
        "frontier_within_proxy": max_frontier <= proxy,
        "iterations_within_proxy": max_iterations <= proxy,
        "both_within_proxy": max_frontier <= proxy and max_iterations <= proxy,
    }
    base.update({
        "status": "torsor",
        "public_factor": None,
        "M": M,
        "R": root,
        "factor_M": fM,
        "components": [
            {
                "power": power,
                "prime": prime,
                "exponent": exponent,
                "source": source,
                "local_root": local_root,
            }
            for power, prime, exponent, source, local_root in components
        ],
        "covariates": public_factor_covariates(K, E, M, fK, fE, components),
        "stages": stages,
        "summary": summary,
    })
    return base, frontier_history


def hidden_audit(public, frontier_history, p, q):
    """Label an already constructed public frontier; never mutate it."""
    if public["status"] == "public_easy_gcdE":
        return {
            "p": p,
            "q": q,
            "next_inverse_bit": (pow(p, -1, 4) >> 1) & 1,
            "easy_factor_matches": public["public_factor"] in (p, q),
            "true_branch_survives_all": None,
            "first_orbit_orientation_depth": None,
            "first_orbit_orientation_modulus_bits": None,
            "public_decode_matches": None,
        }

    first_orientation = None
    first_orientation_bits = None
    true_survives = True
    stage_labels = []
    for stage, frontier in zip(public["stages"], frontier_history):
        modulus = stage["modulus"]
        root = stage["root"]
        inverse_root = pow(root, -1, modulus)
        true_u = p % modulus * inverse_root % modulus
        swapped_u = q % modulus * inverse_root % modulus
        true_live = true_u in frontier
        swapped_live = swapped_u in frontier
        true_survives &= true_live
        oriented = true_u != swapped_u and true_live and not swapped_live
        if oriented and first_orientation is None:
            first_orientation = stage["depth"]
            first_orientation_bits = modulus.bit_length()
        stage_labels.append({
            "depth": stage["depth"],
            "true_u": true_u,
            "swapped_u": swapped_u,
            "self_inverse_orbit": true_u == swapped_u,
            "true_live": true_live,
            "swapped_live": swapped_live,
            "oriented": oriented,
        })

    decoded = public["summary"]["public_decode_factor"]
    return {
        "p": p,
        "q": q,
        "next_inverse_bit": (pow(p, -1, 4) >> 1) & 1,
        "easy_factor_matches": None,
        "true_branch_survives_all": true_survives,
        "first_orbit_orientation_depth": first_orientation,
        "first_orbit_orientation_modulus_bits": first_orientation_bits,
        "public_decode_matches": decoded in (p, q) if decoded is not None else False,
        "stage_labels": stage_labels,
    }


def generate_inputs(count, bit_low, bit_high, seed):
    rng = random.Random(seed)
    seen = set()
    out = []
    attempts = 0
    while len(out) < count:
        attempts += 1
        bits = bit_low + (len(out) % (bit_high - bit_low + 1))
        start = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        p = int(nextprime(start))
        if p.bit_length() != bits:
            continue
        q_start = p + 2 + rng.randrange(max(2, p - 3))
        q = int(nextprime(q_start))
        if not (p < q < 2 * p):
            continue
        N = p * q
        if N % 4 != 3 or N in seen:
            continue
        seen.add(N)
        out.append((p, q))
    return out, attempts


def exact_small_inputs(limit):
    out = []
    for p_value in primerange(3, limit + 1):
        p = int(p_value)
        for q_value in primerange(p + 1, 2 * p):
            q = int(q_value)
            if p * q % 4 == 3:
                out.append((p, q))
    return out


def pair_digest(pairs):
    digest = hashlib.sha256()
    for p, q in pairs:
        digest.update(f"{p},{q}\n".encode())
    return digest.hexdigest()


def average_tie_ranks(values):
    order = sorted(range(len(values)), key=lambda index: values[index])
    ranks = [0.0] * len(values)
    position = 0
    while position < len(order):
        end = position + 1
        while end < len(order) and values[order[end]] == values[order[position]]:
            end += 1
        rank = (position + 1 + end) / 2
        for index in order[position:end]:
            ranks[index] = rank
        position = end
    return ranks


def pearson(left, right):
    if len(left) < 2:
        return None
    mean_left = statistics.fmean(left)
    mean_right = statistics.fmean(right)
    centered_left = [value - mean_left for value in left]
    centered_right = [value - mean_right for value in right]
    denominator = math.sqrt(
        sum(value * value for value in centered_left)
        * sum(value * value for value in centered_right)
    )
    if denominator == 0:
        return None
    return sum(a * b for a, b in zip(centered_left, centered_right)) / denominator


def spearman(left, right):
    return pearson(average_tie_ranks(left), average_tie_ranks(right))


def outcome_values(record):
    public = record["public"]
    labels = record["labels"]
    summary = public["summary"]
    component_count = len(public["components"])
    orientation_depth = labels["first_orbit_orientation_depth"]
    orientation_bits = labels["first_orbit_orientation_modulus_bits"]
    return {
        "log2_1p_max_frontier": math.log2(1 + summary["max_frontier_width"]),
        "log2_1p_max_generator_iterations": math.log2(
            1 + summary["max_generator_iterations"]
        ),
        "normalized_orientation_depth": (
            orientation_depth / component_count if orientation_depth is not None else 1.0
        ),
        "normalized_orientation_modulus_bits": (
            orientation_bits / public["M"].bit_length()
            if orientation_bits is not None
            else 1.0
        ),
    }


def correlations(records):
    primary = [record for record in records if record["public"]["status"] == "torsor"]
    if not primary:
        return {}
    covariate_names = sorted(primary[0]["public"]["covariates"])
    outcome_names = sorted(outcome_values(primary[0]))
    result = {}
    for covariate in covariate_names:
        left = [record["public"]["covariates"][covariate] for record in primary]
        for outcome in outcome_names:
            right = [outcome_values(record)[outcome] for record in primary]
            result[f"{covariate}__{outcome}"] = spearman(left, right)
    return result


def compact_record(record):
    return record


def evaluate_pairs(pairs, cohort, rows_handle, max_p_representatives):
    records = []
    start = time.time()
    for index, (p, q) in enumerate(pairs, 1):
        N = p * q
        public, history = build_public_geometry(N, max_p_representatives)
        labels = hidden_audit(public, history, p, q)
        record = {"cohort": cohort, "public": public, "labels": labels}
        records.append(record)
        rows_handle.write(
            (json.dumps(compact_record(record), sort_keys=True) + "\n").encode()
        )
        if index % 100 == 0:
            print(json.dumps({
                "event": "progress",
                "cohort": cohort,
                "completed": index,
                "total": len(pairs),
                "elapsed_seconds": round(time.time() - start, 3),
            }), flush=True)
    return records


def smallest_record(records, predicate):
    matches = [record for record in records if predicate(record)]
    if not matches:
        return None
    record = min(matches, key=lambda row: row["public"]["N"])
    return {
        "cohort": record["cohort"],
        "N": record["public"]["N"],
        "p": record["labels"]["p"],
        "q": record["labels"]["q"],
        "factor_K": record["public"]["factor_K"],
        "factor_E": record["public"]["factor_E"],
        "factor_M": record["public"]["factor_M"],
        "summary": record["public"]["summary"],
        "labels": record["labels"],
    }


def cohort_summary(records):
    primary = [record for record in records if record["public"]["status"] == "torsor"]
    easy = [record for record in records if record["public"]["status"] != "torsor"]
    integrity_failures = [
        record for record in primary
        if not record["labels"]["true_branch_survives_all"]
        or record["public"]["summary"]["final_frontier_width"] != 1
        or not record["labels"]["public_decode_matches"]
    ]
    within = [record for record in primary if record["public"]["summary"]["both_within_proxy"]]
    return {
        "rows": len(records),
        "primary_torsor_rows": len(primary),
        "public_easy_rows": len(easy),
        "integrity_failures": len(integrity_failures),
        "both_within_n4": len(within),
        "both_within_n4_rate": len(within) / len(primary) if primary else None,
        "max_observed_frontier": max(
            (record["public"]["summary"]["max_frontier_width"] for record in primary),
            default=None,
        ),
        "max_observed_generator_iterations": max(
            (record["public"]["summary"]["max_generator_iterations"] for record in primary),
            default=None,
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--rows", required=True)
    parser.add_argument("--train-count", type=int, default=256)
    parser.add_argument("--holdout-count", type=int, default=64)
    parser.add_argument("--small-p-limit", type=int, default=1000)
    parser.add_argument("--max-p-representatives", type=int, default=2_000_000)
    args = parser.parse_args()

    output_path = Path(args.output)
    rows_path = Path(args.rows)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows_path.parent.mkdir(parents=True, exist_ok=True)
    run_start = time.time()
    print(json.dumps({
        "event": "start",
        "run_id": RUN_ID,
        "python": sys.version,
        "sympy": sympy.__version__,
        "arguments": vars(args),
    }), flush=True)

    train_pairs, train_attempts = generate_inputs(
        args.train_count, 12, 17, TRAIN_SEED
    )
    holdout_pairs, holdout_attempts = generate_inputs(
        args.holdout_count, 18, 23, HOLDOUT_SEED
    )
    small_pairs = exact_small_inputs(args.small_p_limit)
    frozen_pairs = [(5, 7), (17, 31), (37, 71), (53, 67)]

    dataset_identity = {
        "paired_train": {
            "count": len(train_pairs),
            "attempts": train_attempts,
            "seed": TRAIN_SEED,
            "bits": [12, 17],
            "pair_sha256": pair_digest(train_pairs),
        },
        "paired_holdout": {
            "count": len(holdout_pairs),
            "attempts": holdout_attempts,
            "seed": HOLDOUT_SEED,
            "bits": [18, 23],
            "pair_sha256": pair_digest(holdout_pairs),
        },
        "small_exhaustive": {
            "count": len(small_pairs),
            "p_limit": args.small_p_limit,
            "pair_sha256": pair_digest(small_pairs),
        },
        "frozen_witnesses": {
            "count": len(frozen_pairs),
            "pair_sha256": pair_digest(frozen_pairs),
        },
    }
    print(json.dumps({"event": "datasets", "identity": dataset_identity}), flush=True)

    with gzip.open(rows_path, "wb", compresslevel=6) as rows_handle:
        train = evaluate_pairs(
            train_pairs, "paired_train", rows_handle, args.max_p_representatives
        )
        holdout = evaluate_pairs(
            holdout_pairs, "paired_holdout", rows_handle, args.max_p_representatives
        )
        small = evaluate_pairs(
            small_pairs, "small_exhaustive", rows_handle, args.max_p_representatives
        )
        frozen = evaluate_pairs(
            frozen_pairs, "frozen_witnesses", rows_handle, args.max_p_representatives
        )

    all_records = train + holdout + small + frozen
    random_union = train + holdout
    summaries = {
        "paired_train": cohort_summary(train),
        "paired_holdout": cohort_summary(holdout),
        "small_exhaustive": cohort_summary(small),
        "frozen_witnesses": cohort_summary(frozen),
        "all": cohort_summary(all_records),
    }
    integrity_failures = summaries["all"]["integrity_failures"]
    holdout_rate = summaries["paired_holdout"]["both_within_n4_rate"]
    all_primary = [r for r in all_records if r["public"]["status"] == "torsor"]
    all_strong = all(r["public"]["summary"]["both_within_proxy"] for r in all_primary)
    if integrity_failures:
        classification = "integrity_failure"
    elif all_strong:
        classification = "strong_finite_geometry_lead"
    elif holdout_rate is not None and holdout_rate >= 0.95:
        classification = "partial_geometry_lead"
    else:
        classification = "declared_proxy_null"

    corr = {
        "paired_train": correlations(train),
        "paired_holdout": correlations(holdout),
        "paired_random_union": correlations(random_union),
        "small_exhaustive": correlations(small),
    }
    structural_leads = []
    for key, train_value in corr["paired_train"].items():
        holdout_value = corr["paired_holdout"].get(key)
        if train_value is None or holdout_value is None:
            continue
        if abs(train_value) >= 0.50 and abs(holdout_value) >= 0.50 and train_value * holdout_value > 0:
            structural_leads.append({
                "pair": key,
                "train_rho": train_value,
                "holdout_rho": holdout_value,
            })

    result = {
        "run_id": RUN_ID,
        "status": "completed",
        "finite_evidence_only": True,
        "material_difference": "exact F207 CRT branch geometry and Archimedean interval pruning; no F205 scalar rule",
        "runtime_versions": {"python": sys.version, "sympy": sympy.__version__},
        "arguments": vars(args),
        "dataset_identity": dataset_identity,
        "cohorts": summaries,
        "classification": classification,
        "work_proxy": "n^4",
        "correlations": corr,
        "structural_correlation_leads": structural_leads,
        "smallest_observed": {
            "integrity_failure": smallest_record(
                all_records,
                lambda r: r["public"]["status"] == "torsor" and (
                    not r["labels"]["true_branch_survives_all"]
                    or r["public"]["summary"]["final_frontier_width"] != 1
                    or not r["labels"]["public_decode_matches"]
                ),
            ),
            "frontier_exceeds_n4": smallest_record(
                all_records,
                lambda r: r["public"]["status"] == "torsor"
                and not r["public"]["summary"]["frontier_within_proxy"],
            ),
            "generator_iterations_exceed_n4": smallest_record(
                all_records,
                lambda r: r["public"]["status"] == "torsor"
                and not r["public"]["summary"]["iterations_within_proxy"],
            ),
        },
        "elapsed_seconds": round(time.time() - run_start, 3),
    }
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "event": "complete",
        "output": str(output_path),
        "rows": str(rows_path),
        "elapsed_seconds": result["elapsed_seconds"],
        "classification": classification,
        "integrity_failures": integrity_failures,
    }), flush=True)


if __name__ == "__main__":
    main()
