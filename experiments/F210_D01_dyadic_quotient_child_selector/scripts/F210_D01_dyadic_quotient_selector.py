#!/usr/bin/env python3
"""F210-D01: preregistered live dyadic quotient-child selector search.

Hidden p and q generate only the promised reciprocal prefix and audit label.
The public constructor accepts exactly (N, t, u). It constructs and factors
K_0, K_1, H_0, H_1 and runs every public action without hidden factors.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import random
import sys
import time
from collections import Counter
from pathlib import Path

import sympy
from sympy import factorint, nextprime, primerange


RUN_ID = "F210-D01"
ETA_NUMERATOR = 1
ETA_DENOMINATOR = 8
TRAIN_SEED = 20501
HOLDOUT_SEED = 20502


def factorization_value(factors):
    value = 1
    for prime, exponent in factors.items():
        value *= prime**exponent
    return value


def radical(factors):
    return math.prod(factors) if factors else 1


def phi_from_factors(factors):
    value = 1
    for prime, exponent in factors.items():
        value *= (prime - 1) * prime ** (exponent - 1)
    return value


def lambda_from_factors(factors):
    value = 1
    for prime, exponent in factors.items():
        if prime == 2 and exponent >= 3:
            component = 2 ** (exponent - 2)
        else:
            component = (prime - 1) * prime ** (exponent - 1)
        value = math.lcm(value, component)
    return value


def factor_stats(value, factors):
    primes = sorted(factors)
    stats = {
        "value": value,
        "bit_length": value.bit_length(),
        "omega": len(primes),
        "Omega": sum(factors.values()),
        "tau": math.prod(exponent + 1 for exponent in factors.values()),
        "rad": radical(factors),
        "phi": phi_from_factors(factors),
        "lambda": lambda_from_factors(factors),
        "smallest_prime": primes[0] if primes else 1,
        "largest_prime": primes[-1] if primes else 1,
    }
    for residue in (1, 3, 5, 7):
        stats[f"support_mod8_{residue}"] = sum(
            1 for prime in primes if prime % 8 == residue
        )
    return stats


def extremes(values, count):
    ordered = sorted(set(values))
    if len(ordered) <= 2 * count:
        return ordered
    return ordered[:count] + ordered[-count:]


def unique_named(entries):
    seen = set()
    output = []
    for name, value in entries:
        value = int(value)
        if value in seen:
            continue
        seen.add(value)
        output.append((name, value))
    return output


def branch_actions(N, branch, x, y, K, H, factor_K, factor_H, stats_K, stats_H):
    support = sorted(set(factor_K) | set(factor_H))
    selected_support = extremes(support, 4)
    bases = unique_named([
        ("2", 2),
        ("3", 3),
        ("5", 5),
        ("x", x),
        ("y", y),
        ("K", K),
        ("H", H),
        ("radK", stats_K["rad"]),
        ("radH", stats_H["rad"]),
        *[(f"support.{prime}", prime) for prime in selected_support],
    ])

    exponents = [
        ("K", K),
        ("H", H),
        ("radK", stats_K["rad"]),
        ("radH", stats_H["rad"]),
        ("phiK", stats_K["phi"]),
        ("phiH", stats_H["phi"]),
        ("lambdaK", stats_K["lambda"]),
        ("lambdaH", stats_H["lambda"]),
        ("gcdLambda", math.gcd(stats_K["lambda"], stats_H["lambda"])),
        ("lcmLambda", math.lcm(stats_K["lambda"], stats_H["lambda"])),
    ]
    for prime in extremes(factor_K, 2):
        exponents.append((f"K/{prime}", K // prime))
    for prime in extremes(factor_H, 2):
        exponents.append((f"H/{prime}", H // prime))
    exponents = unique_named((name, value) for name, value in exponents if value > 0)

    proper = []
    proper_count = 0
    first_certificate = None
    direct_tests = 0
    power_tests = 0
    plus_global = 0
    minus_global = 0
    neither_global = 0
    minimum_plus_exponent_bits = 0
    minimum_minus_exponent_bits = 0

    def retain_factor(factor, certificate):
        nonlocal first_certificate, proper_count
        if 1 < factor < N:
            assert N % factor == 0
            proper_count += 1
            entry = {"factor": factor, **certificate}
            if first_certificate is None:
                first_certificate = entry
            if len(proper) < 16:
                proper.append(entry)

    for base_name, base_value in bases:
        base = base_value % N
        for shift in (0, -1, 1):
            direct_tests += 1
            factor = math.gcd(base + shift, N)
            retain_factor(factor, {
                "kind": "direct_gcd",
                "branch": branch,
                "base": base_name,
                "shift": shift,
            })

        for exponent_name, exponent in exponents:
            power_tests += 1
            residue = pow(base, exponent, N)
            minus_factor = math.gcd(residue - 1, N)
            plus_factor = math.gcd(residue + 1, N)
            retain_factor(minus_factor, {
                "kind": "power_minus_gcd",
                "branch": branch,
                "base": base_name,
                "exponent": exponent_name,
            })
            retain_factor(plus_factor, {
                "kind": "power_plus_gcd",
                "branch": branch,
                "base": base_name,
                "exponent": exponent_name,
            })
            exponent_bits = exponent.bit_length()
            if minus_factor == N:
                minus_global += 1
                if minimum_minus_exponent_bits == 0:
                    minimum_minus_exponent_bits = exponent_bits
                else:
                    minimum_minus_exponent_bits = min(
                        minimum_minus_exponent_bits, exponent_bits
                    )
            if plus_factor == N:
                plus_global += 1
                if minimum_plus_exponent_bits == 0:
                    minimum_plus_exponent_bits = exponent_bits
                else:
                    minimum_plus_exponent_bits = min(
                        minimum_plus_exponent_bits, exponent_bits
                    )
            if minus_factor == 1 and plus_factor == 1:
                neither_global += 1

    return {
        "base_count": len(bases),
        "exponent_count": len(exponents),
        "direct_tests": direct_tests,
        "power_tests": power_tests,
        "proper_factor_count": proper_count,
        "stored_proper_factors": proper,
        "first_certificate": first_certificate,
        "minus_global": minus_global,
        "plus_global": plus_global,
        "neither_global": neither_global,
        "minimum_minus_exponent_bits": minimum_minus_exponent_bits,
        "minimum_plus_exponent_bits": minimum_plus_exponent_bits,
    }


def public_stage(N, t, u):
    """Construct one stage from public N, t, and the granted prefix u."""
    n = N.bit_length()
    m = 1 << t
    modulus = 2 * m
    assert N > 1 and N & 1
    assert 1 <= t < (n - 1) // 4
    assert 1 <= u < m and u & 1

    lifts = [u, u + m]
    x = [pow(lift, -1, modulus) for lift in lifts]
    y = [(N * lift) % modulus for lift in lifts]
    assert len(set(x)) == 2 and len(set(y)) == 2
    assert all(value & 1 for value in x + y)
    assert all((x[j] * y[j] - N) % modulus == 0 for j in (0, 1))

    K = []
    H = []
    for j in (0, 1):
        compatible_numerator = N - x[j] * y[j]
        crossed_numerator = N - x[j] * y[1 - j]
        assert compatible_numerator > 0
        assert crossed_numerator > 0
        assert compatible_numerator % modulus == 0
        assert crossed_numerator % m == 0
        K.append(compatible_numerator // modulus)
        H.append(crossed_numerator // m)
        assert H[j] & 1

    assert all(0 < value < N // m + 1 for value in K + H)
    assert all(math.gcd(value, N) == 1 for value in K + H)

    factor_K = []
    factor_H = []
    stats_K = []
    stats_H = []
    for j in (0, 1):
        factors_k = {int(p): int(e) for p, e in factorint(K[j]).items()}
        factors_h = {int(p): int(e) for p, e in factorint(H[j]).items()}
        assert factorization_value(factors_k) == K[j]
        assert factorization_value(factors_h) == H[j]
        factor_K.append(factors_k)
        factor_H.append(factors_h)
        stats_K.append(factor_stats(K[j], factors_k))
        stats_H.append(factor_stats(H[j], factors_h))

    actions = []
    for j in (0, 1):
        actions.append(branch_actions(
            N, j, x[j], y[j], K[j], H[j],
            factor_K[j], factor_H[j], stats_K[j], stats_H[j],
        ))

    score_metrics = [
        "value", "bit_length", "omega", "Omega", "tau", "rad", "phi",
        "lambda", "smallest_prime", "largest_prime", "support_mod8_1",
        "support_mod8_3", "support_mod8_5", "support_mod8_7",
    ]
    scores = [{}, {}]
    for j in (0, 1):
        for child_name, stats in (("K", stats_K[j]), ("H", stats_H[j])):
            for metric in score_metrics:
                scores[j][f"{child_name}.{metric}"] = stats[metric]
        for metric in score_metrics:
            left = stats_K[j][metric]
            right = stats_H[j][metric]
            scores[j][f"pair.sum.{metric}"] = left + right
            scores[j][f"pair.max.{metric}"] = max(left, right)
            scores[j][f"pair.product.{metric}"] = left * right

        same_support = set(factor_K[j]) & set(factor_H[j])
        cross_support = set(factor_K[j]) & set(factor_H[1 - j])
        scores[j]["same.gcd_value"] = math.gcd(K[j], H[j])
        scores[j]["same.gcd_rad"] = math.gcd(stats_K[j]["rad"], stats_H[j]["rad"])
        scores[j]["same.support_intersection"] = len(same_support)
        scores[j]["cross.gcd_value"] = math.gcd(K[j], H[1 - j])
        scores[j]["cross.gcd_rad"] = math.gcd(
            stats_K[j]["rad"], stats_H[1 - j]["rad"]
        )
        scores[j]["cross.support_intersection"] = len(cross_support)

        smaller = min(K[j], H[j])
        larger = max(K[j], H[j])
        quotient, remainder = divmod(larger, smaller)
        scores[j]["euclid.quotient"] = quotient
        scores[j]["euclid.remainder"] = remainder
        scores[j]["euclid.remainder_bit_length"] = remainder.bit_length()
        scores[j]["euclid.K_less_H"] = int(K[j] < H[j])
        scores[j]["xy.abs_difference"] = abs(x[j] - y[j])
        scores[j]["xy.sum"] = x[j] + y[j]

        expressions = {
            "x": x[j],
            "y": y[j],
            "x_minus_y": x[j] - y[j],
            "x_plus_y": x[j] + y[j],
        }
        for expression_name, expression in expressions.items():
            scores[j][f"support_gcd.K.{expression_name}"] = math.gcd(
                abs(expression), stats_K[j]["rad"]
            )
            scores[j][f"support_gcd.H.{expression_name}"] = math.gcd(
                abs(expression), stats_H[j]["rad"]
            )

        for action_name in (
            "base_count", "exponent_count", "direct_tests", "power_tests",
            "proper_factor_count", "minus_global", "plus_global",
            "neither_global", "minimum_minus_exponent_bits",
            "minimum_plus_exponent_bits",
        ):
            scores[j][f"action.{action_name}"] = actions[j][action_name]

    factorization_signatures = []
    union_signatures = []
    action_signatures = []
    for j in (0, 1):
        factorization_signatures.append([
            sorted([prime, exponent] for prime, exponent in factor_K[j].items()),
            sorted([prime, exponent] for prime, exponent in factor_H[j].items()),
        ])
        union = Counter(factor_K[j])
        union.update(factor_H[j])
        union_signatures.append(sorted([prime, exponent] for prime, exponent in union.items()))
        action_signatures.append([
            actions[j]["minus_global"],
            actions[j]["plus_global"],
            actions[j]["neither_global"],
            actions[j]["minimum_minus_exponent_bits"],
            actions[j]["minimum_plus_exponent_bits"],
            actions[j]["base_count"],
            actions[j]["exponent_count"],
        ])

    signatures = {
        "factorization": factorization_signatures,
        "union_support": union_signatures,
        "action": action_signatures,
        "combined": [
            [factorization_signatures[j], union_signatures[j], action_signatures[j]]
            for j in (0, 1)
        ],
    }
    baselines = {
        "constant_zero": 0,
        "N_bit_t": (N >> t) & 1,
        "N_bit_t_plus_1": (N >> (t + 1)) & 1,
        "u_top_bit": (u >> (t - 1)) & 1,
        "t_parity": t & 1,
        "candidate_with_smaller_xy_gap": int(abs(x[1] - y[1]) < abs(x[0] - y[0])),
        "candidate_with_smaller_xy_sum": int(x[1] + y[1] < x[0] + y[0]),
    }
    action_factor = next(
        (
            action["first_certificate"]
            for action in actions
            if action["first_certificate"] is not None
        ),
        None,
    )
    t_safe = (n + ETA_DENOMINATOR - 1) // ETA_DENOMINATOR
    return {
        "N": N,
        "n": n,
        "t": t,
        "m": m,
        "u": u,
        "t_terminal": (n - 1) // 4,
        "t_safe": t_safe,
        "recursion_cohort": "late_safe" if t >= t_safe else "early_unsafe",
        "x": x,
        "y": y,
        "K": K,
        "H": H,
        "factor_K": factor_K,
        "factor_H": factor_H,
        "stats_K": stats_K,
        "stats_H": stats_H,
        "actions": actions,
        "action_factor": action_factor,
        "scores": scores,
        "signatures": signatures,
        "baselines": baselines,
        "K_coalesces": K[0] == K[1],
        "H_coalesces": H[0] == H[1],
    }


def hidden_label(public, p, q):
    """Attach the target only after the public transcript is complete."""
    m = public["m"]
    u = public["u"]
    next_inverse = pow(p, -1, 2 * m)
    target = (next_inverse - u) // m
    assert target in (0, 1)
    assert public["x"][target] == p % (2 * m)
    assert public["y"][target] == q % (2 * m)
    certificate = public["action_factor"]
    if certificate is not None:
        assert certificate["factor"] in (p, q)
    return {"p": p, "q": q, "target_next_inverse_bit": target}


def generate_inputs(count, bit_low, bit_high, seed):
    """The deterministic F205-D01 generator, retained verbatim in logic."""
    rng = random.Random(seed)
    seen = set()
    output = []
    attempts = 0
    while len(output) < count:
        attempts += 1
        bits = bit_low + (len(output) % (bit_high - bit_low + 1))
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
        output.append((p, q))
    return output, attempts


def pair_list_hash(pairs):
    digest = hashlib.sha256()
    for p, q in pairs:
        digest.update(f"{p}:{q}\n".encode("ascii"))
    return digest.hexdigest()


def predict(record, rule):
    public = record["public"]
    if rule["kind"] == "score_compare":
        values = [public["scores"][j][rule["feature"]] for j in (0, 1)]
        raw = int(values[1] < values[0])
    elif rule["kind"] == "signature_compare":
        values = public["signatures"][rule["signature"]]
        raw = int(values[1] < values[0])
    elif rule["kind"] == "baseline":
        raw = int(public["baselines"][rule["feature"]])
    else:
        raise ValueError(f"unknown rule kind: {rule['kind']}")
    return raw ^ rule["flip"]


def accuracy_metrics(records, rule):
    predictions = []
    labels = []
    errors = []
    for record in records:
        prediction = predict(record, rule)
        label = record["label"]["target_next_inverse_bit"]
        predictions.append(prediction)
        labels.append(label)
        if prediction != label:
            errors.append({
                "N": record["public"]["N"],
                "t": record["public"]["t"],
                "u": record["public"]["u"],
                "p": record["label"]["p"],
                "q": record["label"]["q"],
                "prediction": prediction,
                "label": label,
            })
    correct = sum(a == b for a, b in zip(predictions, labels))
    recalls = []
    for label_value in (0, 1):
        indices = [index for index, label in enumerate(labels) if label == label_value]
        recalls.append(
            sum(predictions[index] == label_value for index in indices) / len(indices)
            if indices else 0.0
        )
    return {
        "n": len(records),
        "accuracy": correct / len(records) if records else 0.0,
        "balanced_accuracy": sum(recalls) / 2,
        "label_ones": sum(labels),
        "errors": len(errors),
        "smallest_error": min(errors, key=lambda row: (row["N"], row["t"])) if errors else None,
        "stored_errors": sorted(errors, key=lambda row: (row["N"], row["t"]))[:25],
    }


def train_rule_menu(records):
    if not records:
        raise ValueError("empty selector training cohort")
    score_names = sorted(records[0]["public"]["scores"][0])
    baseline_names = sorted(records[0]["public"]["baselines"])
    signature_names = sorted(records[0]["public"]["signatures"])
    candidates = []
    for feature in score_names:
        for flip in (0, 1):
            candidates.append({"kind": "score_compare", "feature": feature, "flip": flip})
    for signature in signature_names:
        for flip in (0, 1):
            candidates.append({"kind": "signature_compare", "signature": signature, "flip": flip})
    for feature in baseline_names:
        for flip in (0, 1):
            candidates.append({"kind": "baseline", "feature": feature, "flip": flip})

    scored = []
    for rule in candidates:
        metrics = accuracy_metrics(records, rule)
        key = json.dumps(rule, sort_keys=True, separators=(",", ":"))
        scored.append((metrics["balanced_accuracy"], key, rule, metrics))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return scored


def selector_verdict(metrics):
    if metrics["errors"] == 0:
        return "finite_exact_selector_candidate"
    if metrics["balanced_accuracy"] >= 0.60:
        return "correlation_lead"
    if metrics["balanced_accuracy"] < 0.55:
        return "fixed_menu_null"
    return "weak_inconclusive"


def action_verdict(records):
    successes = sum(record["public"]["action_factor"] is not None for record in records)
    failures = len(records) - successes
    rate = successes / len(records) if records else 0.0
    if failures == 0 and records:
        verdict = "finite_exact_action_candidate"
    elif rate >= 0.10:
        verdict = "action_lead"
    elif rate < 0.05:
        verdict = "fixed_action_null"
    else:
        verdict = "weak_inconclusive"
    failed = [record for record in records if record["public"]["action_factor"] is None]
    smallest_failure = None
    if failed:
        record = min(failed, key=lambda row: (row["public"]["N"], row["public"]["t"]))
        smallest_failure = {
            "N": record["public"]["N"],
            "p": record["label"]["p"],
            "q": record["label"]["q"],
            "t": record["public"]["t"],
            "u": record["public"]["u"],
            "K": record["public"]["K"],
            "H": record["public"]["H"],
            "factor_K": record["public"]["factor_K"],
            "factor_H": record["public"]["factor_H"],
        }
    return {
        "n": len(records),
        "successes": successes,
        "failures": failures,
        "success_rate": rate,
        "verdict": verdict,
        "smallest_failure": smallest_failure,
    }


def selected_rule_report(train_records, holdout_records):
    if not train_records:
        return {
            "status": "not_applicable_no_training_survivors",
            "menu_size": 0,
            "selected_rule": None,
            "train": None,
            "holdout": None,
            "holdout_verdict": "not_applicable",
            "holdout_by_stage": {},
            "top_twenty_by_train": [],
        }
    trained = train_rule_menu(train_records)
    best_rule = trained[0][2]
    train_metrics = trained[0][3]
    if not holdout_records:
        return {
            "status": "not_applicable_no_holdout_survivors",
            "menu_size": len(trained),
            "selected_rule": best_rule,
            "train": train_metrics,
            "holdout": None,
            "holdout_verdict": "not_applicable",
            "holdout_by_stage": {},
            "top_twenty_by_train": [],
        }
    holdout_metrics = accuracy_metrics(holdout_records, best_rule)
    stages = sorted(set(record["public"]["t"] for record in holdout_records))
    by_stage = {}
    for t in stages:
        subset = [record for record in holdout_records if record["public"]["t"] == t]
        by_stage[str(t)] = accuracy_metrics(subset, best_rule)
    top_twenty = []
    for _, _, rule, metrics in trained[:20]:
        top_twenty.append({
            "rule": rule,
            "train": metrics,
            "holdout": accuracy_metrics(holdout_records, rule),
        })
    return {
        "status": "scored",
        "menu_size": len(trained),
        "selected_rule": best_rule,
        "train": train_metrics,
        "holdout": holdout_metrics,
        "holdout_verdict": selector_verdict(holdout_metrics),
        "holdout_by_stage": by_stage,
        "top_twenty_by_train": top_twenty,
    }


def evaluate_pairs(pairs, split, rows_handle):
    records = []
    pair_stage_counts = Counter()
    start = time.time()
    for pair_index, (p, q) in enumerate(pairs, 1):
        N = p * q
        n = N.bit_length()
        terminal = (n - 1) // 4
        for t in range(1, terminal):
            m = 1 << t
            u = pow(p, -1, m)
            public = public_stage(N, t, u)
            label = hidden_label(public, p, q)
            record = {"split": split, "public": public, "label": label}
            records.append(record)
            pair_stage_counts[public["recursion_cohort"]] += 1
            rows_handle.write((json.dumps(record, sort_keys=True) + "\n").encode("utf-8"))
        if pair_index % 100 == 0:
            print(json.dumps({
                "event": "progress",
                "split": split,
                "pairs_completed": pair_index,
                "pairs_total": len(pairs),
                "stage_rows": len(records),
                "elapsed_seconds": round(time.time() - start, 3),
            }), flush=True)
    return records, dict(pair_stage_counts)


def summarize_coalescence(records):
    output = {}
    for name in ("K_coalesces", "H_coalesces"):
        matching = [record for record in records if record["public"][name]]
        smallest = None
        if matching:
            record = min(matching, key=lambda row: (row["public"]["N"], row["public"]["t"]))
            smallest = {
                "N": record["public"]["N"],
                "p": record["label"]["p"],
                "q": record["label"]["q"],
                "t": record["public"]["t"],
                "u": record["public"]["u"],
                "K": record["public"]["K"],
                "H": record["public"]["H"],
            }
        output[name] = {"count": len(matching), "smallest": smallest}
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--rows", required=True)
    parser.add_argument("--train-count", type=int, default=2000)
    parser.add_argument("--holdout-count", type=int, default=1000)
    parser.add_argument("--small-p-limit", type=int, default=500)
    args = parser.parse_args()

    output_path = Path(args.output)
    rows_path = Path(args.rows)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows_path.parent.mkdir(parents=True, exist_ok=True)
    run_start = time.time()
    source_path = Path(__file__).resolve()
    source_sha = hashlib.sha256(source_path.read_bytes()).hexdigest()

    train_pairs, train_attempts = generate_inputs(
        args.train_count, 12, 17, TRAIN_SEED
    )
    holdout_pairs, holdout_attempts = generate_inputs(
        args.holdout_count, 18, 23, HOLDOUT_SEED
    )
    small_pairs = []
    for p_value in primerange(3, args.small_p_limit + 1):
        p = int(p_value)
        for q_value in primerange(p + 1, 2 * p):
            q = int(q_value)
            if (p * q) % 4 == 3:
                small_pairs.append((p, q))

    pair_hashes = {
        "train": pair_list_hash(train_pairs),
        "holdout": pair_list_hash(holdout_pairs),
        "small_exhaustive": pair_list_hash(small_pairs),
    }
    print(json.dumps({
        "event": "start",
        "run_id": RUN_ID,
        "source_sha256": source_sha,
        "python": sys.version,
        "sympy": sympy.__version__,
        "arguments": vars(args),
        "pair_hashes": pair_hashes,
    }, sort_keys=True), flush=True)

    with gzip.open(rows_path, "wb", compresslevel=6) as rows_handle:
        train, train_stage_counts = evaluate_pairs(train_pairs, "train", rows_handle)
        holdout, holdout_stage_counts = evaluate_pairs(holdout_pairs, "holdout", rows_handle)
        small, small_stage_counts = evaluate_pairs(
            small_pairs, "small_exhaustive", rows_handle
        )

    selector_reports = {}
    action_reports = {}
    for recursion_cohort in ("early_unsafe", "late_safe"):
        train_all = [
            record for record in train
            if record["public"]["recursion_cohort"] == recursion_cohort
        ]
        holdout_all = [
            record for record in holdout
            if record["public"]["recursion_cohort"] == recursion_cohort
        ]
        train_primary = [
            record for record in train_all
            if record["public"]["action_factor"] is None
        ]
        holdout_primary = [
            record for record in holdout_all
            if record["public"]["action_factor"] is None
        ]
        selector_reports[recursion_cohort] = selected_rule_report(
            train_primary, holdout_primary
        )
        selector_reports[recursion_cohort]["train_rows_before_action_exit"] = len(train_all)
        selector_reports[recursion_cohort]["holdout_rows_before_action_exit"] = len(holdout_all)
        action_reports[recursion_cohort] = {
            "train": action_verdict(train_all),
            "holdout": action_verdict(holdout_all),
        }

    all_records = train + holdout + small
    action_kinds = Counter()
    for record in all_records:
        certificate = record["public"]["action_factor"]
        if certificate is not None:
            action_kinds[certificate["kind"]] += 1

    result = {
        "run_id": RUN_ID,
        "status": "completed",
        "finite_evidence_only": True,
        "source_sha256": source_sha,
        "runtime_versions": {"python": sys.version, "sympy": sympy.__version__},
        "fixed_parameters": {
            "eta": [ETA_NUMERATOR, ETA_DENOMINATOR],
            "stage_rule": "1 <= t < (N.bit_length()-1)//4",
            "train_seed": TRAIN_SEED,
            "holdout_seed": HOLDOUT_SEED,
            "train_factor_bits": [12, 17],
            "holdout_factor_bits": [18, 23],
            "train_count": len(train_pairs),
            "holdout_count": len(holdout_pairs),
            "small_p_limit": args.small_p_limit,
            "small_pair_count": len(small_pairs),
        },
        "generation": {
            "train_attempts": train_attempts,
            "holdout_attempts": holdout_attempts,
            "pair_hashes": pair_hashes,
            "stage_rows": {
                "train": len(train),
                "holdout": len(holdout),
                "small_exhaustive": len(small),
            },
            "stage_cohort_counts": {
                "train": train_stage_counts,
                "holdout": holdout_stage_counts,
                "small_exhaustive": small_stage_counts,
            },
        },
        "public_action_bank": {
            "reports": action_reports,
            "first_certificate_kinds_all_rows": dict(action_kinds),
        },
        "selectors": selector_reports,
        "coalescence": summarize_coalescence(all_records),
        "interpretation": {
            "late_safe_only_for_qp": True,
            "early_rows_are_diagnostic_only": True,
            "factor_four_children_early_is_not_claimed_qp": True,
            "one_child_decrement_recursion_remains_valid": True,
            "finite_perfection_is_not_a_theorem": True,
        },
        "elapsed_seconds": round(time.time() - run_start, 3),
    }
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "event": "complete",
        "output": str(output_path),
        "rows": str(rows_path),
        "elapsed_seconds": result["elapsed_seconds"],
        "selector_verdicts": {
            cohort: report["holdout_verdict"]
            for cohort, report in selector_reports.items()
        },
        "action_verdicts": {
            cohort: report["holdout"]["verdict"]
            for cohort, report in action_reports.items()
        },
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
