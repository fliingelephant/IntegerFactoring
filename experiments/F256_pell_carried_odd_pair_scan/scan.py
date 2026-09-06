#!/usr/bin/env python3
"""Preregistered F256 carried odd-multiple Pell pair scan."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import resource
import sys
import time
from collections import Counter
from pathlib import Path


EXPERIMENT = "F256_pell_carried_odd_pair_scan"
COHORT_SEED = "F256-pell-carried-odd-pair-cohort-v1"
TRAIN_BITS = (20, 24, 28, 32)
HELDOUT_BITS = (36, 40, 44, 48)
INPUTS_PER_BIT = 128
D_MENU = (2, 3, 5, 6, 7, 10, 11, 13)
ODD_MULTIPLIERS = (3, 5, 7, 9)
WINDOW_MULTIPLIER = 12
MR_BASES_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def proper(divisor: int, modulus: int) -> bool:
    return 1 < divisor < modulus


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


class HashStream:
    def __init__(self, label: str):
        self.label = label
        self.counter = 0

    def below(self, modulus: int) -> int:
        limit = (1 << 256) - ((1 << 256) % modulus)
        while True:
            payload = f"{self.label}:{self.counter}".encode()
            self.counter += 1
            value = int.from_bytes(hashlib.sha256(payload).digest(), "big")
            if value < limit:
                return value % modulus


def is_prime_64(value: int) -> bool:
    if value < 2:
        return False
    for small in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % small == 0:
            return value == small
    odd = value - 1
    shift = 0
    while odd % 2 == 0:
        shift += 1
        odd //= 2
    for base in MR_BASES_64:
        if base % value == 0:
            continue
        residue = pow(base, odd, value)
        if residue in (1, value - 1):
            continue
        for _ in range(shift - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def prime_from_hash(label: str, bits: int) -> int:
    low = 1 << (bits - 1)
    span = 1 << (bits - 1)
    stream = HashStream(label)
    start = (low + stream.below(span)) | 1
    candidate = start
    while True:
        if is_prime_64(candidate):
            return candidate
        candidate += 2
        if candidate >= low + span:
            candidate = low | 1
        require(candidate != start, "prime search wrapped")


def make_cohort(bit_lengths: tuple[int, ...], split: str) -> list[dict[str, int | str]]:
    cohort: list[dict[str, int | str]] = []
    seen: set[int] = set()
    for bits in bit_lengths:
        accepted = 0
        counter = 0
        while accepted < INPUTS_PER_BIT:
            p = prime_from_hash(f"{COHORT_SEED}:{split}:{bits}:{counter}:p", bits // 2)
            q = prime_from_hash(f"{COHORT_SEED}:{split}:{bits}:{counter}:q", bits // 2)
            counter += 1
            p, q = sorted((p, q))
            modulus = p * q
            if p == q or q >= 2 * p or modulus.bit_length() != bits or modulus in seen:
                continue
            seen.add(modulus)
            cohort.append(
                {
                    "split": split,
                    "bits": bits,
                    "index_within_bits": accepted,
                    "N": modulus,
                    "verifier_p": p,
                    "verifier_q": q,
                }
            )
            accepted += 1
    return cohort


def fundamental_pell(discriminant: int) -> tuple[int, int]:
    root = math.isqrt(discriminant)
    require(root * root != discriminant, "Pell discriminant must be nonsquare")
    m = 0
    denominator = 1
    a = root
    numerator_prev, numerator = 1, a
    denominator_prev, denominator_cf = 0, 1
    while numerator * numerator - discriminant * denominator_cf * denominator_cf != 1:
        m = denominator * a - m
        denominator = (discriminant - m * m) // denominator
        a = (root + m) // denominator
        numerator_prev, numerator = numerator, a * numerator + numerator_prev
        denominator_prev, denominator_cf = denominator_cf, a * denominator_cf + denominator_prev
    return numerator, denominator_cf


def pell_sequences(limit: int) -> dict[int, list[tuple[int, int]]]:
    result = {}
    for discriminant in D_MENU:
        fundamental_s, fundamental_t = fundamental_pell(discriminant)
        sequence = [(1, 0)]
        exact_s, exact_t = 1, 0
        for _ in range(limit):
            exact_s, exact_t = (
                exact_s * fundamental_s + discriminant * exact_t * fundamental_t,
                exact_s * fundamental_t + exact_t * fundamental_s,
            )
            require(exact_s * exact_s - discriminant * exact_t * exact_t == 1, "Pell recurrence failed")
            sequence.append((exact_s, exact_t))
        result[discriminant] = sequence
    return result


def odd_multiple_polynomials(discriminant: int, multiplier: int, y: int) -> tuple[int, int]:
    require(multiplier > 0 and multiplier % 2 == 1, "positive odd multiplier required")
    norm_square = 1 + discriminant * y * y
    f_value = 0
    g_value = 0
    half = (multiplier - 1) // 2
    for r in range(half + 1):
        f_value += (
            math.comb(multiplier, 2 * r + 1)
            * discriminant**r
            * y ** (2 * r + 1)
            * norm_square ** ((multiplier - 2 * r - 1) // 2)
        )
        g_value += (
            math.comb(multiplier, 2 * r)
            * discriminant**r
            * y ** (2 * r)
            * norm_square ** ((multiplier - 2 * r - 1) // 2)
        )
    require(norm_square * g_value * g_value == 1 + discriminant * f_value * f_value, "polynomial norm failed")
    return f_value, g_value


def cleanup_rows(
    modulus: int, bits: int, sequences: dict[int, list[tuple[int, int]]]
) -> tuple[dict[int, dict[int, dict[str, int]]], dict[str, object]]:
    retained_by_d: dict[int, dict[int, dict[str, int]]] = {}
    counts = Counter()
    direct_factor_count = 0
    direct_factor_certificates = []
    limit = WINDOW_MULTIPLIER * bits
    for discriminant in D_MENU:
        retained: dict[int, dict[str, int]] = {}
        first_by_y: dict[int, dict[str, int]] = {}
        for index in range(1, limit + 1):
            exact_s, exact_t = sequences[discriminant][index]
            counts["generated"] += 1
            counts["prewrap" if exact_t < modulus else "postwrap"] += 1
            y = exact_t % modulus
            x = exact_s % modulus
            value = 1 + discriminant * y * y
            root_gcd = math.gcd(x, modulus)
            if root_gcd != 1:
                counts["nonunit_root_removed"] += 1
                if proper(root_gcd, modulus):
                    direct_factor_count += 1
                    if len(direct_factor_certificates) < 8:
                        direct_factor_certificates.append(
                            {"kind": "root_gcd", "D": discriminant, "j": index, "factor": root_gcd}
                        )
                else:
                    require(root_gcd == modulus, "invalid root gcd")
                    counts["globally_nonunit_root_removed"] += 1
                continue
            require(pow(x, 2, modulus) == value % modulus, "supplied root failed")
            integer_root = math.isqrt(value)
            if integer_root * integer_root == value:
                minus = math.gcd((integer_root - x) % modulus, modulus)
                plus = math.gcd((integer_root + x) % modulus, modulus)
                if proper(minus, modulus) or proper(plus, modulus):
                    factor = minus if proper(minus, modulus) else plus
                    direct_factor_count += 1
                    if len(direct_factor_certificates) < 8:
                        direct_factor_certificates.append(
                            {"kind": "singleton_square", "D": discriminant, "j": index, "factor": factor}
                        )
                else:
                    require((minus, plus) in ((modulus, 1), (1, modulus)), "singleton root class invalid")
                counts["singleton_square_removed"] += 1
                continue
            if y in first_by_y:
                old = first_by_y[y]
                minus = math.gcd((x - old["root"]) % modulus, modulus)
                plus = math.gcd((x + old["root"]) % modulus, modulus)
                if proper(minus, modulus) or proper(plus, modulus):
                    factor = minus if proper(minus, modulus) else plus
                    direct_factor_count += 1
                    if len(direct_factor_certificates) < 8:
                        direct_factor_certificates.append(
                            {"kind": "duplicate_coordinate", "D": discriminant, "j": index, "factor": factor}
                        )
                else:
                    require((minus, plus) in ((modulus, 1), (1, modulus)), "duplicate root class invalid")
                counts["duplicate_y_removed"] += 1
                continue
            record = {"j": index, "y": y, "value": value, "root": x}
            retained[index] = record
            first_by_y[y] = record
            counts["retained"] += 1
        retained_by_d[discriminant] = retained
        counts[f"D{discriminant}_retained"] = len(retained)
    return retained_by_d, {
        "counts": dict(sorted(counts.items())),
        "direct_factor_event_count": direct_factor_count,
        "direct_factor_certificates": direct_factor_certificates,
        "any_cleanup_factor": direct_factor_count > 0,
    }


def analyze_pairs(
    modulus: int,
    bits: int,
    retained_by_d: dict[int, dict[int, dict[str, int]]],
    any_cleanup_factor: bool,
) -> dict[str, object]:
    total = Counter()
    by_d: dict[str, Counter] = {str(discriminant): Counter() for discriminant in D_MENU}
    by_multiplier: dict[str, Counter] = {str(multiplier): Counter() for multiplier in ODD_MULTIPLIERS}
    dependency_certificates = []
    non_global_certificates = []
    limit = WINDOW_MULTIPLIER * bits

    def increment(key: str, discriminant: int, multiplier: int) -> None:
        total[key] += 1
        by_d[str(discriminant)][key] += 1
        by_multiplier[str(multiplier)][key] += 1

    for discriminant in D_MENU:
        retained = retained_by_d[discriminant]
        for multiplier in ODD_MULTIPLIERS:
            for index in range(1, limit // multiplier + 1):
                increment("index_pairs", discriminant, multiplier)
                target_index = multiplier * index
                if index not in retained or target_index not in retained:
                    continue
                left = retained[index]
                right = retained[target_index]
                require(left["y"] != right["y"], "retained coordinates must be distinct")
                increment("admissible_pairs", discriminant, multiplier)
                f_value, g_value = odd_multiple_polynomials(discriminant, multiplier, left["y"])
                require(f_value % modulus == right["y"], "odd multiple coordinate mismatch")
                require(left["root"] * (g_value % modulus) % modulus == right["root"], "odd multiple root mismatch")
                carry, remainder = divmod(f_value - right["y"], modulus)
                require(remainder == 0 and carry >= 0, "invalid canonical carry")
                if carry == 0:
                    increment("uncarried_pairs", discriminant, multiplier)
                    continue
                increment("carried_pairs", discriminant, multiplier)
                left_value = left["value"]
                right_value = right["value"]
                carry_factor = discriminant * carry * (2 * right["y"] + carry * modulus)
                require(left_value * g_value * g_value - right_value == modulus * carry_factor, "carry identity failed")
                divisor = math.gcd(left_value, right_value)
                require(divisor == math.gcd(left_value, carry_factor), "carry gcd identity failed")
                increment("d_eq_1" if divisor == 1 else "d_gt_1", discriminant, multiplier)
                left_quotient = left_value // divisor
                right_quotient = right_value // divisor
                require(math.gcd(left_quotient, right_quotient) == 1, "quotients not coprime")
                left_root = math.isqrt(left_quotient)
                right_root = math.isqrt(right_quotient)
                left_square = left_root * left_root == left_quotient
                right_square = right_root * right_root == right_quotient
                if left_square:
                    increment("left_quotient_square", discriminant, multiplier)
                if right_square:
                    increment("right_quotient_square", discriminant, multiplier)
                if left_square != right_square:
                    increment("exactly_one_quotient_square", discriminant, multiplier)
                product = left_value * right_value
                product_root = math.isqrt(product)
                dependency = left_square and right_square
                require((product_root * product_root == product) == dependency, "square classification failed")
                if not dependency:
                    continue
                increment("square_dependencies", discriminant, multiplier)
                exact_root = divisor * left_root * right_root
                require(exact_root == product_root, "dependency root mismatch")
                supplied_root = left["root"] * right["root"] % modulus
                require(math.gcd(supplied_root, modulus) == 1, "supplied pair root not a unit")
                require(pow(exact_root, 2, modulus) == pow(supplied_root, 2, modulus), "modular root mismatch")
                normalized = exact_root % modulus * pow(supplied_root, -1, modulus) % modulus
                require(pow(normalized, 2, modulus) == 1, "normalized root not 2-torsion")
                minus = math.gcd((exact_root - supplied_root) % modulus, modulus)
                plus = math.gcd((exact_root + supplied_root) % modulus, modulus)
                if normalized == 1:
                    root_class = "+1"
                    require((minus, plus) == (modulus, 1), "+1 gcd class invalid")
                elif normalized == modulus - 1:
                    root_class = "-1"
                    require((minus, plus) == (1, modulus), "-1 gcd class invalid")
                else:
                    root_class = "non_global"
                    require(proper(minus, modulus) and proper(plus, modulus), "non-global root did not split")
                    increment("non_global_dependencies", discriminant, multiplier)
                    if not any_cleanup_factor:
                        increment("strict_screen_free_non_global", discriminant, multiplier)
                increment(f"root_class_{root_class}", discriminant, multiplier)
                certificate = {
                    "D": discriminant,
                    "h": multiplier,
                    "j": index,
                    "target_j": target_index,
                    "y": left["y"],
                    "target_y": right["y"],
                    "carry": carry,
                    "A": left_value,
                    "A_prime": right_value,
                    "H": carry_factor,
                    "d": divisor,
                    "left_quotient_root": left_root,
                    "right_quotient_root": right_root,
                    "positive_product_root": exact_root,
                    "supplied_root_mod_N": supplied_root,
                    "normalized_root_mod_N": normalized,
                    "root_class": root_class,
                    "gcd_R_minus_X": minus,
                    "gcd_R_plus_X": plus,
                }
                if len(dependency_certificates) < 5:
                    dependency_certificates.append(certificate)
                if root_class == "non_global" and len(non_global_certificates) < 5:
                    non_global_certificates.append(certificate)
    return {
        "counts": dict(sorted(total.items())),
        "by_D": {key: dict(sorted(value.items())) for key, value in by_d.items()},
        "by_multiplier": {key: dict(sorted(value.items())) for key, value in by_multiplier.items()},
        "dependency_certificates": dependency_certificates,
        "non_global_certificates": non_global_certificates,
        "any_dependency": total["square_dependencies"] > 0,
        "any_non_global": total["non_global_dependencies"] > 0,
        "strict_screen_free_non_global": total["strict_screen_free_non_global"] > 0,
    }


def analyze_input(
    meta: dict[str, int | str], sequences: dict[int, list[tuple[int, int]]]
) -> dict[str, object]:
    start_wall = time.perf_counter_ns()
    start_cpu = time.process_time_ns()
    modulus = int(meta["N"])
    retained_by_d, source = cleanup_rows(modulus, int(meta["bits"]), sequences)
    pairs = analyze_pairs(modulus, int(meta["bits"]), retained_by_d, bool(source["any_cleanup_factor"]))
    return {
        "meta": meta,
        "source": source,
        "pairs": pairs,
        "wall_ns": time.perf_counter_ns() - start_wall,
        "cpu_ns": time.process_time_ns() - start_cpu,
    }


def add_counter(target: Counter, values: dict[str, int]) -> None:
    for key, value in values.items():
        target[key] += value


def summarize_group(rows: list[dict[str, object]]) -> dict[str, object]:
    counts = Counter()
    by_d = {str(discriminant): Counter() for discriminant in D_MENU}
    by_multiplier = {str(multiplier): Counter() for multiplier in ODD_MULTIPLIERS}
    for row in rows:
        add_counter(counts, row["pairs"]["counts"])
        for key, value in row["pairs"]["by_D"].items():
            add_counter(by_d[key], value)
        for key, value in row["pairs"]["by_multiplier"].items():
            add_counter(by_multiplier[key], value)
    return {
        "inputs": len(rows),
        "inputs_with_cleanup_factor": sum(bool(row["source"]["any_cleanup_factor"]) for row in rows),
        "inputs_with_dependency": sum(bool(row["pairs"]["any_dependency"]) for row in rows),
        "inputs_with_non_global": sum(bool(row["pairs"]["any_non_global"]) for row in rows),
        "inputs_with_strict_screen_free_non_global": sum(
            bool(row["pairs"]["strict_screen_free_non_global"]) for row in rows
        ),
        "counts": dict(sorted(counts.items())),
        "by_D": {key: dict(sorted(value.items())) for key, value in by_d.items()},
        "by_multiplier": {key: dict(sorted(value.items())) for key, value in by_multiplier.items()},
    }


def summarize(results: list[dict[str, object]], prereg_hash: str, algebra_hash: str, scan_hash: str) -> dict[str, object]:
    splits = {}
    for split in ("train", "heldout"):
        selected = [row for row in results if row["meta"]["split"] == split]
        split_summary = summarize_group(selected)
        split_summary["by_bits"] = {
            str(bits): summarize_group([row for row in selected if row["meta"]["bits"] == bits])
            for bits in (TRAIN_BITS if split == "train" else HELDOUT_BITS)
        }
        splits[split] = split_summary
    heldout = splits["heldout"]
    strict_bits = sum(
        group["inputs_with_strict_screen_free_non_global"] > 0 for group in heldout["by_bits"].values()
    )
    if heldout["inputs_with_strict_screen_free_non_global"] >= 4 and strict_bits >= 2:
        interpretation = "strong finite signal"
    elif heldout["inputs_with_strict_screen_free_non_global"]:
        interpretation = "weak finite signal"
    elif heldout["inputs_with_dependency"]:
        interpretation = "global-only finite structure"
    else:
        interpretation = "null finite signal"
    return {
        "experiment": EXPERIMENT,
        "preregistration_sha256": prereg_hash,
        "algebra_sha256": algebra_hash,
        "scan_sha256": scan_hash,
        "parameters": {
            "train_bits": TRAIN_BITS,
            "heldout_bits": HELDOUT_BITS,
            "inputs_per_bit": INPUTS_PER_BIT,
            "D_menu": D_MENU,
            "odd_multipliers": ODD_MULTIPLIERS,
            "window_multiplier": WINDOW_MULTIPLIER,
        },
        "splits": splits,
        "heldout_interpretation": interpretation,
        "process_max_rss_platform_units": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "python": sys.version,
    }


def self_test() -> None:
    for discriminant in D_MENU:
        sequence = pell_sequences(36)[discriminant]
        for multiplier in ODD_MULTIPLIERS:
            for y in range(12):
                odd_multiple_polynomials(discriminant, multiplier, y)
            for index in range(1, 36 // multiplier + 1):
                source_s, source_t = sequence[index]
                target_s, target_t = sequence[multiplier * index]
                f_value, g_value = odd_multiple_polynomials(discriminant, multiplier, source_t)
                require(f_value == target_t and source_s * g_value == target_s, "exact Pell multiple failed")
    for left in range(1, 80):
        for right in range(1, 80):
            divisor = math.gcd(left, right)
            a = left // divisor
            b = right // divisor
            classified = math.isqrt(a) ** 2 == a and math.isqrt(b) ** 2 == b
            product = left * right
            require(classified == (math.isqrt(product) ** 2 == product), "pair classification self-test failed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--prereg-sha256", required=True)
    parser.add_argument("--algebra-sha256", required=True)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    require(sys.version_info >= (3, 11), "Python 3.11 or newer required")
    base = Path(__file__).parent
    prereg_hash = sha256_file(base / "PREREGISTRATION.md")
    algebra_hash = sha256_file(base / "ALGEBRA.md")
    require(prereg_hash == args.prereg_sha256, "preregistration hash mismatch")
    require(algebra_hash == args.algebra_sha256, "algebra hash mismatch")
    if args.self_test:
        self_test()
        print("SELF_TEST_PASS")
        return 0
    require(args.output_dir is not None, "output directory required")
    scan_hash = sha256_file(Path(__file__))
    sequences = pell_sequences(WINDOW_MULTIPLIER * max(HELDOUT_BITS))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for split, bit_lengths, filename in (
        ("train", TRAIN_BITS, "TRAIN.jsonl"),
        ("heldout", HELDOUT_BITS, "HELDOUT.jsonl"),
    ):
        cohort = make_cohort(bit_lengths, split)
        with (args.output_dir / filename).open("w", encoding="utf-8") as handle:
            for index, meta in enumerate(cohort):
                result = analyze_input(meta, sequences)
                results.append(result)
                handle.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
                handle.flush()
                print(
                    f"{split} {index + 1}/{len(cohort)} bits={meta['bits']} "
                    f"pairs={result['pairs']['counts'].get('carried_pairs', 0)} "
                    f"deps={result['pairs']['counts'].get('square_dependencies', 0)} "
                    f"non_global={result['pairs']['counts'].get('non_global_dependencies', 0)}",
                    flush=True,
                )
    summary = summarize(results, prereg_hash, algebra_hash, scan_hash)
    (args.output_dir / "SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

