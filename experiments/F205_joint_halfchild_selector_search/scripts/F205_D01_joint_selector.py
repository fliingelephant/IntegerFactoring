#!/usr/bin/env python3
"""F205-D01: preregistered joint K/E selector discovery search.

Every public feature is constructed in public_record(N), which has no access
to p or q. Hidden factors enter only through hidden_labels and certificate
verification after public construction is complete.
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

import numpy as np
import sympy
from sympy import factorint, kronecker_symbol, nextprime, primerange


RUN_ID = "F205-D01"


def merge_factorizations(f, g, mode="max"):
    keys = set(f) | set(g)
    if mode == "max":
        return {p: max(f.get(p, 0), g.get(p, 0)) for p in keys}
    return {p: f.get(p, 0) + g.get(p, 0) for p in keys}


def integer_from_factorization(f):
    out = 1
    for p, e in f.items():
        out *= p**e
    return out


def phi_from_factorization(f):
    out = 1
    for p, e in f.items():
        out *= (p - 1) * p ** (e - 1)
    return out


def lambda_from_factorization(f):
    out = 1
    for p, e in f.items():
        if p == 2 and e >= 3:
            part = 2 ** (e - 2)
        else:
            part = (p - 1) * p ** (e - 1)
        out = math.lcm(out, part)
    return out


def sigma_from_factorization(f):
    out = 1
    for p, e in f.items():
        out *= (p ** (e + 1) - 1) // (p - 1)
    return out


def twisted_sigma_chi4(f):
    out = 1
    for p, e in f.items():
        if p == 2:
            continue
        chi = 1 if p % 4 == 1 else -1
        out *= sum((chi * p) ** j for j in range(e + 1))
    return out


def v2_or_cap(x, cap=128):
    if x == 0:
        return cap
    x = abs(x)
    return (x & -x).bit_length() - 1


def crt_square_root_from_children(N, B, fK, fE):
    fM = merge_factorizations(fK, fE, "max")
    x = 0
    modulus = 1
    for prime in sorted(fM):
        power = prime ** fM[prime]
        root = 1 if fK.get(prime, 0) >= fE.get(prime, 0) else B % power
        step = ((root - x) * pow(modulus, -1, power)) % power
        x += modulus * step
        modulus *= power
        x %= modulus
    assert x * x % modulus == N % modulus
    return x, modulus, fM


def add_factor_features(prefix, f, binary, numeric):
    primes = sorted(f)
    omega = len(primes)
    big_omega = sum(f.values())
    value = integer_from_factorization(f)
    largest = primes[-1] if primes else 1
    smallest = primes[0] if primes else 1
    numeric[f"{prefix}.omega"] = omega
    numeric[f"{prefix}.Omega"] = big_omega
    numeric[f"{prefix}.largest_log2"] = math.log2(largest)
    numeric[f"{prefix}.largest_fraction_log"] = math.log2(largest) / max(1.0, math.log2(value))
    numeric[f"{prefix}.smallest_log2"] = math.log2(smallest)
    binary[f"{prefix}.omega_parity"] = omega & 1
    binary[f"{prefix}.Omega_parity"] = big_omega & 1
    binary[f"{prefix}.squarefree"] = int(omega == big_omega)
    for residue in (1, 3, 5, 7):
        count = sum(1 for p in primes if p % 8 == residue)
        binary[f"{prefix}.has_p8_{residue}"] = int(count > 0)
        binary[f"{prefix}.count_p8_{residue}_parity"] = count & 1
        numeric[f"{prefix}.count_p8_{residue}"] = count
    for residue in (1, 3, 5, 7):
        binary[f"{prefix}.smallest_p8_{residue}"] = int(smallest % 8 == residue)
        binary[f"{prefix}.largest_p8_{residue}"] = int(largest % 8 == residue)


def arithmetic_values(f):
    value = integer_from_factorization(f)
    radical = math.prod(f) if f else 1
    return {
        "value": value,
        "rad": radical,
        "phi": phi_from_factorization(f),
        "lambda": lambda_from_factorization(f),
        "sigma": sigma_from_factorization(f),
        "Achi4": twisted_sigma_chi4(f),
    }


def add_integer_residue_features(name, value, binary):
    binary[f"{name}.negative"] = int(value < 0)
    binary[f"{name}.zero"] = int(value == 0)
    for modulus in (4, 8, 16):
        residue = value % modulus
        for r in range(modulus):
            binary[f"{name}.mod{modulus}.{r}"] = int(residue == r)


def child_support_primes(fK, fE):
    primes = sorted(set(fK) | set(fE))
    if len(primes) <= 24:
        return primes
    return primes[:12] + primes[-12:]


def public_transition_bank(N, B, K, E, M, R, fK, fE, fM, vals):
    support = child_support_primes(fK, fE)
    expression_pairs = [
        ("2", 2), ("3", 3), ("5", 5), ("B", B), ("K", K),
        ("E", E), ("M", M), ("R", R),
    ]
    for child in ("K", "E", "M"):
        for key in ("rad", "phi", "lambda", "sigma", "Achi4"):
            expression_pairs.append((f"{child}.{key}", vals[child][key]))
    expression_pairs.extend([
        ("K.Achi4-E.Achi4", vals["K"]["Achi4"] - vals["E"]["Achi4"]),
        ("K.Achi4+E.Achi4", vals["K"]["Achi4"] + vals["E"]["Achi4"]),
        ("K.sigma-E.sigma", vals["K"]["sigma"] - vals["E"]["sigma"]),
        ("K.phi-E.phi", vals["K"]["phi"] - vals["E"]["phi"]),
        ("R-B", R - B), ("R+B", R + B),
    ])
    expression_pairs.extend((f"support_prime.{p}", p) for p in support)

    seen_bases = set()
    bases = []
    for name, value in expression_pairs:
        residue = value % N
        if residue not in seen_bases:
            seen_bases.add(residue)
            bases.append((name, residue))

    fNm1 = dict(fK)
    fNm1[2] = fNm1.get(2, 0) + 1
    exponent_pairs = [
        ("N-1", N - 1), ("K", K), ("E", E), ("M", M),
    ]
    for child in ("K", "E", "M"):
        for key in ("rad", "phi", "lambda"):
            exponent_pairs.append((f"{child}.{key}", vals[child][key]))
    for p in sorted(fNm1):
        exponent_pairs.append((f"(N-1)/{p}", (N - 1) // p))
    for child, value, factors in (("E", E, fE), ("M", M, fM)):
        for p in sorted(factors):
            exponent_pairs.append((f"{child}/{p}", value // p))

    seen_exponents = set()
    exponents = []
    for name, value in exponent_pairs:
        if value > 0 and value not in seen_exponents:
            seen_exponents.add(value)
            exponents.append((name, value))

    global_returns = 0
    max_common_order = 1
    for base_name, base in bases:
        g = math.gcd(base, N)
        if 1 < g < N:
            return {
                "factor": g,
                "certificate": {"kind": "base_gcd", "base": base_name},
                "global_returns": global_returns,
                "max_common_order": max_common_order,
            }
        for shift in (-1, 1):
            g = math.gcd((base + shift) % N, N)
            if 1 < g < N:
                return {
                    "factor": g,
                    "certificate": {"kind": "base_shift_gcd", "base": base_name, "shift": shift},
                    "global_returns": global_returns,
                    "max_common_order": max_common_order,
                }

        z_nm1 = pow(base, N - 1, N)
        g = math.gcd(z_nm1 - 1, N)
        if 1 < g < N:
            return {
                "factor": g,
                "certificate": {"kind": "Nminus1_gcd", "base": base_name},
                "global_returns": global_returns,
                "max_common_order": max_common_order,
            }
        g = math.gcd(z_nm1 + 1, N)
        if 1 < g < N:
            return {
                "factor": g,
                "certificate": {"kind": "Nminus1_plus_gcd", "base": base_name},
                "global_returns": global_returns,
                "max_common_order": max_common_order,
            }

        if z_nm1 == 1:
            global_returns += 1
            order = N - 1
            for prime, multiplicity in sorted(fNm1.items()):
                for _ in range(multiplicity):
                    candidate = order // prime
                    h = math.gcd(pow(base, candidate, N) - 1, N)
                    if 1 < h < N:
                        return {
                            "factor": h,
                            "certificate": {
                                "kind": "factor_first_strip",
                                "base": base_name,
                                "prime": prime,
                                "exponent": candidate,
                            },
                            "global_returns": global_returns,
                            "max_common_order": max_common_order,
                        }
                    if h == N:
                        order = candidate
                    else:
                        break
            assert pow(base, order, N) == 1
            max_common_order = max(max_common_order, order)

        for exponent_name, exponent in exponents:
            z = pow(base, exponent, N)
            for sign in (-1, 1):
                h = math.gcd(z + sign, N)
                if 1 < h < N:
                    return {
                        "factor": h,
                        "certificate": {
                            "kind": "power_gcd",
                            "base": base_name,
                            "exponent": exponent_name,
                            "sign": sign,
                        },
                        "global_returns": global_returns,
                        "max_common_order": max_common_order,
                    }

    return {
        "factor": None,
        "certificate": None,
        "global_returns": global_returns,
        "max_common_order": max_common_order,
    }


def second_mixed_norm_representation(N, B, E):
    limit = math.isqrt(N // E)
    for y in range(1, limit + 1):
        remainder = N - E * y * y
        if remainder < 0:
            break
        x = math.isqrt(remainder)
        if x * x != remainder:
            continue
        if x == B and y == 1:
            continue
        if math.gcd(y, N) != 1:
            continue
        root = x * pow(y, -1, N) % N
        g = math.gcd(root - B, N)
        if 1 < g < N:
            return {"x": x, "y": y, "root": root, "factor": g}
        g = math.gcd(root + B, N)
        if 1 < g < N:
            return {"x": x, "y": y, "root": root, "factor": g}
    return None


def public_record(N):
    """Construct public features from N and the two complete child factors."""
    B = math.isqrt(N)
    K = (N - 1) // 2
    E = N - B * B
    fK = {int(p): int(e) for p, e in factorint(K).items()}
    fE = {int(p): int(e) for p, e in factorint(E).items()}
    R, M, fM = crt_square_root_from_children(N, B, fK, fE)
    vals = {
        "K": arithmetic_values(fK),
        "E": arithmetic_values(fE),
        "M": arithmetic_values(fM),
    }
    assert vals["K"]["value"] == K
    assert vals["E"]["value"] == E
    assert vals["M"]["value"] == M

    binary = {}
    numeric = {}
    integers = {
        "N": N, "B": B, "K": K, "E": E, "M": M, "R": R,
        "gcdKE": math.gcd(K, E),
        "gcdBm1K": math.gcd(B - 1, K),
        "gcdBp1K": math.gcd(B + 1, K),
        "gcdBm1E": math.gcd(B - 1, E),
        "gcdBp1E": math.gcd(B + 1, E),
    }
    for child in ("K", "E", "M"):
        for key, value in vals[child].items():
            integers[f"{child}.{key}"] = value
    integers.update({
        "Achi4.diff": vals["K"]["Achi4"] - vals["E"]["Achi4"],
        "Achi4.sum": vals["K"]["Achi4"] + vals["E"]["Achi4"],
        "sigma.diff": vals["K"]["sigma"] - vals["E"]["sigma"],
        "phi.diff": vals["K"]["phi"] - vals["E"]["phi"],
    })
    for name, value in integers.items():
        add_integer_residue_features(name, value, binary)

    add_factor_features("K", fK, binary, numeric)
    add_factor_features("E", fE, binary, numeric)
    add_factor_features("M", fM, binary, numeric)

    numeric.update({
        "E_over_B": E / B,
        "M_over_K": M / K,
        "R_over_M": R / M,
        "gcdKE_log2": math.log2(max(1, math.gcd(K, E))),
        "gcdBm1K_log2": math.log2(max(1, math.gcd(B - 1, K))),
        "gcdBp1K_log2": math.log2(max(1, math.gcd(B + 1, K))),
        "gcdBm1E_log2": math.log2(max(1, math.gcd(B - 1, E))),
        "gcdBp1E_log2": math.log2(max(1, math.gcd(B + 1, E))),
        "K.phi_ratio": vals["K"]["phi"] / K,
        "E.phi_ratio": vals["E"]["phi"] / E,
        "M.phi_ratio": vals["M"]["phi"] / M,
        "v2_Achi4_diff": v2_or_cap(vals["K"]["Achi4"] - vals["E"]["Achi4"]),
        "v2_Achi4_sum": v2_or_cap(vals["K"]["Achi4"] + vals["E"]["Achi4"]),
        "v2_sigma_diff": v2_or_cap(vals["K"]["sigma"] - vals["E"]["sigma"]),
    })
    binary["omega.K_gt_E"] = int(len(fK) > len(fE))
    binary["largest.K_gt_E"] = int(max(fK) > max(fE))
    binary["Achi4.K_gt_E"] = int(vals["K"]["Achi4"] > vals["E"]["Achi4"])
    binary["absAchi4.K_gt_E"] = int(abs(vals["K"]["Achi4"]) > abs(vals["E"]["Achi4"]))

    split = inert = ramified = jacobi_minus = 0
    split_log = inert_log = 0.0
    for prime in sorted(fK):
        if prime == 2 or E % prime == 0:
            ramified += 1
            continue
        symbol = int(kronecker_symbol(-E, prime))
        if symbol == 1:
            split += 1
            split_log += math.log2(prime)
        elif symbol == -1:
            inert += 1
            inert_log += math.log2(prime)
        if int(kronecker_symbol(prime, N)) == -1:
            jacobi_minus += 1
    numeric.update({
        "K.split_count": split,
        "K.inert_count": inert,
        "K.ramified_count": ramified,
        "K.split_log2": split_log,
        "K.inert_log2": inert_log,
        "K.jacobi_minus_count": jacobi_minus,
    })
    binary.update({
        "K.has_split": int(split > 0),
        "K.has_inert": int(inert > 0),
        "K.has_ramified": int(ramified > 0),
        "K.split_parity": split & 1,
        "K.inert_parity": inert & 1,
        "K.jacobi_minus_parity": jacobi_minus & 1,
        "K.has_jacobi_minus": int(jacobi_minus > 0),
    })

    gcd_en = math.gcd(E, N)
    transition = public_transition_bank(N, B, K, E, M, R, fK, fE, fM, vals)
    mixed_norm = None if gcd_en != 1 else second_mixed_norm_representation(N, B, E)
    return {
        "N": N,
        "B": B,
        "K": K,
        "E": E,
        "M": M,
        "R": R,
        "factor_K": fK,
        "factor_E": fE,
        "factor_M": fM,
        "gcd_EN": gcd_en,
        "binary": binary,
        "numeric": numeric,
        "transition": transition,
        "mixed_norm": mixed_norm,
    }


def hidden_labels(public, p, q):
    """Use hidden factors only for labels and post-construction evaluation."""
    N = public["N"]
    B = public["B"]
    K = public["K"]
    E = public["E"]
    support = set(public["factor_K"]) | set(public["factor_E"]) | {2}
    d = p + q - 2 * B
    fd = {int(r): int(e) for r, e in factorint(d).items()}
    next_bit = (pow(p, -1, 4) >> 1) & 1
    chi_p = 1 if p % 4 == 1 else -1
    chi_q = 1 if q % 4 == 1 else -1
    twisted_core = p * chi_p + q * chi_q
    full_twisted = 1 - N + twisted_core
    common_capacity = math.gcd(p - 1, q - 1)
    supported_common = 1
    remaining = common_capacity
    for prime in sorted(support):
        while remaining % prime == 0:
            supported_common *= prime
            remaining //= prime
    transition_factor = public["transition"]["factor"]
    if transition_factor is not None:
        assert transition_factor in (p, q)
    mixed = public["mixed_norm"]
    if mixed is not None:
        assert mixed["factor"] in (p, q)
    return {
        "p": p,
        "q": q,
        "next_inverse_bit": next_bit,
        "chi4_p": chi_p,
        "twisted_core": twisted_core,
        "full_twisted_A_N": full_twisted,
        "d": d,
        "factor_d": fd,
        "d_supported_by_2KE": all(r in support for r in fd),
        "common_order_capacity": common_capacity,
        "supported_common_part": supported_common,
        "K_has_split_prime": bool(public["binary"]["K.has_split"]),
        "mixed_class_principal": mixed is not None,
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


def accuracy_metrics(records, rule):
    predictions = []
    labels = []
    errors = []
    for record in records:
        if rule["kind"] == "binary":
            raw = int(record["public"]["binary"][rule["feature"]])
        else:
            raw = int(record["public"]["numeric"][rule["feature"]] > rule["threshold"])
        pred = raw ^ rule["flip"]
        label = record["labels"]["next_inverse_bit"]
        predictions.append(pred)
        labels.append(label)
        if pred != label:
            errors.append({
                "N": record["public"]["N"],
                "p": record["labels"]["p"],
                "q": record["labels"]["q"],
                "prediction": pred,
                "label": label,
            })
    n = len(labels)
    correct = sum(a == b for a, b in zip(predictions, labels))
    per_class = []
    for label in (0, 1):
        indices = [i for i, value in enumerate(labels) if value == label]
        per_class.append(sum(predictions[i] == label for i in indices) / len(indices) if indices else 0.0)
    return {
        "n": n,
        "accuracy": correct / n if n else 0.0,
        "balanced_accuracy": sum(per_class) / 2,
        "label_ones": sum(labels),
        "errors": len(errors),
        "smallest_error": min(errors, key=lambda row: row["N"]) if errors else None,
        "stored_errors": sorted(errors, key=lambda row: row["N"])[:25],
    }


def train_rules(records):
    if not records:
        raise ValueError("empty training cohort")
    binary_names = sorted(records[0]["public"]["binary"])
    numeric_names = sorted(records[0]["public"]["numeric"])
    rules = []
    for name in binary_names:
        values = [int(r["public"]["binary"][name]) for r in records]
        if min(values) == max(values):
            continue
        for flip in (0, 1):
            rule = {"kind": "binary", "feature": name, "flip": flip}
            score = accuracy_metrics(records, rule)
            rules.append((score["balanced_accuracy"], json.dumps(rule, sort_keys=True), rule, score))
    for name in numeric_names:
        values = np.asarray([float(r["public"]["numeric"][name]) for r in records])
        for quantile in (0.10, 0.25, 0.50, 0.75, 0.90):
            threshold = float(np.quantile(values, quantile))
            if np.all(values <= threshold) or np.all(values > threshold):
                continue
            for flip in (0, 1):
                rule = {
                    "kind": "stump",
                    "feature": name,
                    "quantile": quantile,
                    "threshold": threshold,
                    "flip": flip,
                }
                score = accuracy_metrics(records, rule)
                rules.append((score["balanced_accuracy"], json.dumps(rule, sort_keys=True), rule, score))
    rules.sort(key=lambda item: (-item[0], item[1]))
    return rules


def compact_public(public):
    return {
        "N": public["N"], "B": public["B"], "K": public["K"],
        "E": public["E"], "M": public["M"], "R": public["R"],
        "factor_K": public["factor_K"], "factor_E": public["factor_E"],
        "factor_M": public["factor_M"], "gcd_EN": public["gcd_EN"],
        "binary": public["binary"], "numeric": public["numeric"],
        "transition": public["transition"], "mixed_norm": public["mixed_norm"],
    }


def evaluate_pairs(pairs, cohort, rows_handle):
    records = []
    transition_kinds = Counter()
    start = time.time()
    for index, (p, q) in enumerate(pairs, 1):
        N = p * q
        public = public_record(N)
        labels = hidden_labels(public, p, q)
        record = {"cohort": cohort, "public": public, "labels": labels}
        records.append(record)
        if public["transition"]["certificate"]:
            transition_kinds[public["transition"]["certificate"]["kind"]] += 1
        rows_handle.write((json.dumps({
            "cohort": cohort,
            "public": compact_public(public),
            "labels": labels,
        }, sort_keys=True) + "\n").encode())
        if index % 250 == 0:
            print(json.dumps({
                "event": "progress", "cohort": cohort, "completed": index,
                "total": len(pairs), "elapsed_seconds": round(time.time() - start, 3),
            }), flush=True)
    return records, transition_kinds


def certificate_row(record):
    return {
        "N": record["public"]["N"],
        "p": record["labels"]["p"],
        "q": record["labels"]["q"],
        "B": record["public"]["B"],
        "K": record["public"]["K"],
        "E": record["public"]["E"],
        "M": record["public"]["M"],
        "factor_K": record["public"]["factor_K"],
        "factor_E": record["public"]["factor_E"],
        "transition": record["public"]["transition"],
        "mixed_norm": record["public"]["mixed_norm"],
        "labels": record["labels"],
    }


def smallest(records, predicate):
    matches = [record for record in records if predicate(record)]
    return certificate_row(min(matches, key=lambda record: record["public"]["N"])) if matches else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--rows", required=True)
    parser.add_argument("--train-count", type=int, default=5000)
    parser.add_argument("--holdout-count", type=int, default=2500)
    parser.add_argument("--small-p-limit", type=int, default=1000)
    args = parser.parse_args()

    output_path = Path(args.output)
    rows_path = Path(args.rows)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows_path.parent.mkdir(parents=True, exist_ok=True)
    run_start = time.time()
    print(json.dumps({
        "event": "start", "run_id": RUN_ID, "python": sys.version,
        "sympy": sympy.__version__, "numpy": np.__version__,
        "arguments": vars(args),
    }), flush=True)

    train_pairs, train_attempts = generate_inputs(args.train_count, 12, 17, 20501)
    holdout_pairs, holdout_attempts = generate_inputs(args.holdout_count, 18, 23, 20502)
    small_pairs = []
    for p_value in primerange(3, args.small_p_limit + 1):
        p = int(p_value)
        for q_value in primerange(p + 1, 2 * p):
            q = int(q_value)
            N = p * q
            if N % 4 == 3:
                small_pairs.append((p, q))

    with gzip.open(rows_path, "wb", compresslevel=6) as rows_handle:
        train, train_kinds = evaluate_pairs(train_pairs, "train", rows_handle)
        holdout, holdout_kinds = evaluate_pairs(holdout_pairs, "holdout", rows_handle)
        small, small_kinds = evaluate_pairs(small_pairs, "small_exhaustive", rows_handle)
        frozen, frozen_kinds = evaluate_pairs([(37, 71)], "frozen_2627", rows_handle)

    primary_train = [r for r in train if r["public"]["gcd_EN"] == 1 and r["public"]["transition"]["factor"] is None]
    primary_holdout = [r for r in holdout if r["public"]["gcd_EN"] == 1 and r["public"]["transition"]["factor"] is None]
    trained = train_rules(primary_train)
    best_rule = trained[0][2]
    best_train = trained[0][3]
    best_holdout = accuracy_metrics(primary_holdout, best_rule)
    top_rules = []
    for _, _, rule, train_score in trained[:20]:
        top_rules.append({
            "rule": rule,
            "train": {k: v for k, v in train_score.items() if k not in ("stored_errors",)},
            "holdout": accuracy_metrics(primary_holdout, rule),
        })

    all_records = train + holdout + small + frozen
    result = {
        "run_id": RUN_ID,
        "status": "completed",
        "finite_evidence_only": True,
        "runtime_versions": {
            "python": sys.version,
            "sympy": sympy.__version__,
            "numpy": np.__version__,
        },
        "generation": {
            "train_count": len(train), "train_attempts": train_attempts,
            "holdout_count": len(holdout), "holdout_attempts": holdout_attempts,
            "small_exhaustive_count": len(small),
            "train_factor_bits": [12, 17], "holdout_factor_bits": [18, 23],
            "train_seed": 20501, "holdout_seed": 20502,
        },
        "cohorts": {
            "primary_train": len(primary_train),
            "primary_holdout": len(primary_holdout),
            "train_public_easy_gcdE": sum(r["public"]["gcd_EN"] != 1 for r in train),
            "holdout_public_easy_gcdE": sum(r["public"]["gcd_EN"] != 1 for r in holdout),
            "train_bank_success": sum(r["public"]["transition"]["factor"] is not None for r in train),
            "holdout_bank_success": sum(r["public"]["transition"]["factor"] is not None for r in holdout),
            "transition_certificate_kinds": {
                "train": dict(train_kinds), "holdout": dict(holdout_kinds),
                "small": dict(small_kinds), "frozen": dict(frozen_kinds),
            },
        },
        "selector": {
            "number_of_predeclared_oriented_rules": len(trained),
            "selected_rule": best_rule,
            "train": best_train,
            "holdout": best_holdout,
            "top_twenty_by_train": top_rules,
            "qualification": "Any error refutes universality of the exact rule. Finite perfection would remain discovery evidence only.",
        },
        "rates": {
            "d_supported_by_2KE": sum(r["labels"]["d_supported_by_2KE"] for r in all_records) / len(all_records),
            "K_has_split_prime": sum(r["labels"]["K_has_split_prime"] for r in all_records) / len(all_records),
            "mixed_class_principal": sum(r["labels"]["mixed_class_principal"] for r in all_records if r["public"]["gcd_EN"] == 1) /
                max(1, sum(r["public"]["gcd_EN"] == 1 for r in all_records)),
            "ordinary_common_capacity_le_2": sum(r["labels"]["common_order_capacity"] <= 2 for r in all_records) / len(all_records),
        },
        "smallest_observed": {
            "fixed_bank_failure": smallest(all_records, lambda r: r["public"]["gcd_EN"] == 1 and r["public"]["transition"]["factor"] is None),
            "d_support_failure": smallest(all_records, lambda r: not r["labels"]["d_supported_by_2KE"]),
            "no_K_split_prime": smallest(all_records, lambda r: not r["labels"]["K_has_split_prime"]),
            "no_second_mixed_norm": smallest(all_records, lambda r: r["public"]["gcd_EN"] == 1 and not r["labels"]["mixed_class_principal"]),
            "ordinary_common_capacity_le_2": smallest(all_records, lambda r: r["labels"]["common_order_capacity"] <= 2),
        },
        "frozen_2627": certificate_row(frozen[0]),
        "elapsed_seconds": round(time.time() - run_start, 3),
    }
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "event": "complete", "output": str(output_path), "rows": str(rows_path),
        "elapsed_seconds": result["elapsed_seconds"],
        "selected_holdout_accuracy": best_holdout["accuracy"],
        "selected_holdout_errors": best_holdout["errors"],
    }), flush=True)


if __name__ == "__main__":
    main()
