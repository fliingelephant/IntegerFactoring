#!/usr/bin/env python3
"""Preregistered F250 canonical Pell/P66 hypercycle scan."""

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


COHORT_SEED = "F250-pell-p66-hypercycle-cohort-v1"
TRAIN_BITS = (20, 24, 28, 32)
HELDOUT_BITS = (36, 40, 44, 48)
INPUTS_PER_BIT = 16
D_MENU = (2, 3, 5, 6, 7, 10, 11, 13)
WINDOW_MULTIPLIER = 4
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


def factor_free_rows(values: list[int]) -> tuple[list[int], dict[str, int]]:
    pending = [(value, 1 << index) for index, value in enumerate(values) if value > 1]
    stable: list[tuple[int, int]] = []
    stats = Counter()
    while pending:
        value, mask = pending.pop()
        if value <= 1 or mask == 0:
            continue
        for position, (old_value, old_mask) in enumerate(stable):
            stats["gcd_scans"] += 1
            divisor = math.gcd(value, old_value)
            if divisor == 1:
                continue
            stable.pop(position)
            stats["refinements"] += 1
            pending.extend(
                ((divisor, mask ^ old_mask), (value // divisor, mask), (old_value // divisor, old_mask))
            )
            break
        else:
            stable.append((value, mask))
    stable.sort()
    for index, (value, mask) in enumerate(stable):
        require(mask != 0, "zero terminal mask")
        require(all(math.gcd(value, other) == 1 for other, _ in stable[:index]), "non-coprime fragments")
    rows = []
    for value, mask in stable:
        root = math.isqrt(value)
        if root * root != value:
            rows.append(mask)
        else:
            stats["square_fragments_removed"] += 1
    unique = sorted(set(rows))
    stats["stable_fragments"] = len(stable)
    stats["unique_parity_rows"] = len(unique)
    return unique, dict(sorted(stats.items()))


def kernel_basis(rows: list[int], column_count: int) -> tuple[int, list[int]]:
    pivots: dict[int, int] = {}
    for source in sorted(set(row for row in rows if row)):
        row = source
        while row:
            pivot = (row & -row).bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    basis = []
    for free in range(column_count):
        if free in pivots:
            continue
        vector = 1 << free
        for pivot in sorted(pivots, reverse=True):
            if (pivots[pivot] & vector).bit_count() & 1:
                vector ^= 1 << pivot
        require(all((row & vector).bit_count() % 2 == 0 for row in rows), "kernel check failed")
        basis.append(vector)
    require(len(pivots) + len(basis) == column_count, "rank-nullity failed")
    return len(pivots), basis


def support_indices(vector: int) -> list[int]:
    result = []
    while vector:
        bit = vector & -vector
        result.append(bit.bit_length() - 1)
        vector ^= bit
    return result


def decode_bank(name: str, records: list[dict[str, int]], modulus: int, earlier_factor: bool) -> dict[str, object]:
    start_wall = time.perf_counter_ns()
    start_cpu = time.process_time_ns()
    rows, refine = factor_free_rows([row["value"] for row in records])
    rank, basis = kernel_basis(rows, len(records))
    classes = Counter()
    certificates = []
    for basis_index, vector in enumerate(basis):
        product = 1
        supplied = 1
        indices = support_indices(vector)
        for index in indices:
            product *= records[index]["value"]
            supplied = supplied * records[index]["root"] % modulus
        positive = math.isqrt(product)
        require(positive * positive == product, "kernel product not square")
        reduced = positive % modulus
        require(pow(reduced, 2, modulus) == pow(supplied, 2, modulus), "root mismatch")
        minus = math.gcd((reduced - supplied) % modulus, modulus)
        plus = math.gcd((reduced + supplied) % modulus, modulus)
        rho = reduced * pow(supplied, -1, modulus) % modulus
        require(pow(rho, 2, modulus) == 1, "normalized root not 2-torsion")
        if rho == 1:
            classes["+1"] += 1
        elif rho == modulus - 1:
            classes["-1"] += 1
        else:
            classes["non_global"] += 1
            require(proper(minus, modulus) and proper(plus, modulus), "mixed root did not factor")
            if len(certificates) < 3:
                ids = [records[index]["id"] for index in indices]
                certificates.append(
                    {
                        "basis_index": basis_index,
                        "support": len(ids),
                        "support_ids": ids,
                        "positive_root_mod_N": reduced,
                        "supplied_root_mod_N": supplied,
                        "normalized_root_mod_N": rho,
                        "gcd_R_minus_X": minus,
                        "gcd_R_plus_X": plus,
                    }
                )
    non_global = classes["non_global"]
    return {
        "name": name,
        "columns": len(records),
        "parity_rows": len(rows),
        "rank": rank,
        "kernel_dimension": len(basis),
        "basis_root_classes": dict(sorted(classes.items())),
        "non_global_basis_root_hits": non_global,
        "strict_screen_free_hit": non_global > 0 and not earlier_factor,
        "certificates": certificates,
        "refinement": refine,
        "wall_ns": time.perf_counter_ns() - start_wall,
        "cpu_ns": time.process_time_ns() - start_cpu,
    }


def generate_rows(modulus: int, bits: int) -> tuple[list[dict[str, int]], dict[str, object]]:
    records: list[dict[str, int]] = []
    by_d: dict[int, list[dict[str, int]]] = {}
    counts = Counter()
    direct_factors = []
    tangent = Counter()
    tangent_certificates = []
    source_start_wall = time.perf_counter_ns()
    source_start_cpu = time.process_time_ns()
    for discriminant in D_MENU:
        fundamental_s, fundamental_t = fundamental_pell(discriminant)
        require(fundamental_s * fundamental_s - discriminant * fundamental_t * fundamental_t == 1, "bad unit")
        exact_s, exact_t = 1, 0
        first_wrap = None
        first_retained_by_y: dict[int, dict[str, int]] = {}
        retained: list[dict[str, int]] = []
        for index in range(WINDOW_MULTIPLIER * bits + 1):
            require(exact_s * exact_s - discriminant * exact_t * exact_t == 1, "Pell recurrence failed")
            if first_wrap is None and exact_t >= modulus:
                first_wrap = index
            counts["generated"] += 1
            counts["prewrap" if exact_t < modulus else "postwrap"] += 1
            y = exact_t % modulus
            x = exact_s % modulus
            value = 1 + discriminant * y * y
            if index == 0:
                counts["trivial_j0_removed"] += 1
            else:
                root_gcd = math.gcd(x, modulus)
                if proper(root_gcd, modulus):
                    direct_factors.append({"kind": "root_gcd", "D": discriminant, "j": index, "factor": root_gcd})
                else:
                    require(root_gcd == 1, "global nonunit root")
                    require(pow(x, 2, modulus) == value % modulus, "supplied root failed")
                    integer_root = math.isqrt(value)
                    if integer_root * integer_root == value:
                        minus = math.gcd((integer_root - x) % modulus, modulus)
                        plus = math.gcd((integer_root + x) % modulus, modulus)
                        if proper(minus, modulus) or proper(plus, modulus):
                            direct_factors.append(
                                {"kind": "singleton_square", "D": discriminant, "j": index, "factor": minus if proper(minus, modulus) else plus}
                            )
                        else:
                            require((minus, plus) in ((modulus, 1), (1, modulus)), "singleton root class invalid")
                        counts["singleton_square_removed"] += 1
                    elif y in first_retained_by_y:
                        old = first_retained_by_y[y]
                        minus = math.gcd((x - old["root"]) % modulus, modulus)
                        plus = math.gcd((x + old["root"]) % modulus, modulus)
                        if proper(minus, modulus) or proper(plus, modulus):
                            direct_factors.append(
                                {"kind": "duplicate_coordinate", "D": discriminant, "j": index, "factor": minus if proper(minus, modulus) else plus}
                            )
                        else:
                            require((minus, plus) in ((modulus, 1), (1, modulus)), "duplicate root class invalid")
                        counts["duplicate_y_removed"] += 1
                    else:
                        record = {"id": f"D{discriminant}:j{index}", "D": discriminant, "j": index, "y": y, "value": value, "root": x}
                        first_retained_by_y[y] = record
                        retained.append(record)
                        records.append(record)
                        counts["retained"] += 1
            exact_s, exact_t = (
                exact_s * fundamental_s + discriminant * exact_t * fundamental_t,
                exact_s * fundamental_t + exact_t * fundamental_s,
            )
        require(first_wrap is not None, "frozen Pell window never wrapped")
        coordinates = {row["y"]: row for row in retained}
        for left_index, left in enumerate(retained):
            for right in retained[left_index + 1 :]:
                denominator = 1 - discriminant * left["y"] * right["y"]
                numerator = left["y"] + right["y"]
                if denominator == 0 or numerator % denominator:
                    continue
                target = abs(numerator // denominator)
                if target >= modulus:
                    continue
                if target == 0 or target in (left["y"], right["y"]):
                    tangent["zero_or_repeated"] += 1
                elif target not in coordinates:
                    tangent["new_absent"] += 1
                else:
                    tangent["new_present"] += 1
                    third = coordinates[target]
                    product = left["value"] * right["value"] * third["value"]
                    square = math.isqrt(product)
                    tangent["present_product_square" if square * square == product else "present_product_nonsquare"] += 1
                    if square * square == product:
                        supplied = left["root"] * right["root"] * third["root"] % modulus
                        divisor = math.gcd((square - supplied) % modulus, modulus)
                        other = math.gcd((square + supplied) % modulus, modulus)
                        if proper(divisor, modulus) or proper(other, modulus):
                            tangent["present_non_global"] += 1
                            if len(tangent_certificates) < 3:
                                tangent_certificates.append(
                                    {"D": discriminant, "ids": [left["id"], right["id"], third["id"]], "factor": divisor if proper(divisor, modulus) else other}
                                )
        by_d[discriminant] = retained
        counts[f"D{discriminant}_retained"] = len(retained)
        counts[f"D{discriminant}_first_wrap_j"] = first_wrap
    return records, {
        "counts": dict(sorted(counts.items())),
        "direct_factor_events": direct_factors,
        "any_predecoder_factor": bool(direct_factors),
        "tangent": dict(sorted(tangent.items())),
        "tangent_certificates": tangent_certificates,
        "by_d": by_d,
        "wall_ns": time.perf_counter_ns() - source_start_wall,
        "cpu_ns": time.process_time_ns() - source_start_cpu,
    }


def analyze_input(meta: dict[str, int | str]) -> dict[str, object]:
    modulus = int(meta["N"])
    records, source = generate_rows(modulus, int(meta["bits"]))
    by_d = source.pop("by_d")
    banks = [decode_bank(f"D{discriminant}", by_d[discriminant], modulus, bool(source["any_predecoder_factor"])) for discriminant in D_MENU]
    banks.append(decode_bank("all_D", records, modulus, bool(source["any_predecoder_factor"])))
    return {
        "meta": meta,
        "source": source,
        "banks": banks,
        "any_decoder_hit": any(bank["non_global_basis_root_hits"] for bank in banks),
        "strict_screen_free_hit": any(bank["strict_screen_free_hit"] for bank in banks),
    }


def summarize(results: list[dict[str, object]], prereg_hash: str, scan_hash: str) -> dict[str, object]:
    summaries = {}
    for split in ("train", "heldout"):
        selected = [row for row in results if row["meta"]["split"] == split]
        hit_bits = Counter()
        bank_hits = Counter()
        strict_bank_hits = Counter()
        direct_inputs = 0
        tangent_events = Counter()
        for row in selected:
            direct_inputs += int(bool(row["source"]["any_predecoder_factor"]))
            tangent_events.update(row["source"]["tangent"])
            if row["strict_screen_free_hit"]:
                hit_bits[int(row["meta"]["bits"])] += 1
            for bank in row["banks"]:
                if bank["non_global_basis_root_hits"]:
                    bank_hits[bank["name"]] += 1
                if bank["strict_screen_free_hit"]:
                    strict_bank_hits[bank["name"]] += 1
        summaries[split] = {
            "inputs": len(selected),
            "inputs_with_predecoder_factor": direct_inputs,
            "inputs_with_any_decoder_hit": sum(bool(row["any_decoder_hit"]) for row in selected),
            "inputs_with_strict_screen_free_hit": sum(bool(row["strict_screen_free_hit"]) for row in selected),
            "strict_hits_by_bits": dict(sorted(hit_bits.items())),
            "decoder_hit_inputs_by_bank": dict(sorted(bank_hits.items())),
            "strict_hit_inputs_by_bank": dict(sorted(strict_bank_hits.items())),
            "tangent_events": dict(sorted(tangent_events.items())),
        }
    heldout = summaries["heldout"]
    if heldout["inputs_with_strict_screen_free_hit"] >= 4 and len(heldout["strict_hits_by_bits"]) >= 2:
        interpretation = "strong finite signal"
    elif heldout["inputs_with_strict_screen_free_hit"]:
        interpretation = "weak finite signal"
    else:
        interpretation = "null finite signal"
    return {
        "experiment": "F250_pell_p66_hypercycle",
        "preregistration_sha256": prereg_hash,
        "scan_sha256": scan_hash,
        "parameters": {
            "train_bits": TRAIN_BITS,
            "heldout_bits": HELDOUT_BITS,
            "inputs_per_bit": INPUTS_PER_BIT,
            "D_menu": D_MENU,
            "window_multiplier": WINDOW_MULTIPLIER,
            "banks_per_input": len(D_MENU) + 1,
        },
        "splits": summaries,
        "heldout_interpretation": interpretation,
        "process_max_rss_platform_units": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "python": sys.version,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--prereg-sha256", required=True)
    args = parser.parse_args()
    require(sys.version_info >= (3, 11), "Python 3.11 or newer required")
    prereg_hash = sha256_file(Path(__file__).with_name("PREREGISTRATION.md"))
    require(prereg_hash == args.prereg_sha256, "preregistration hash mismatch")
    scan_hash = sha256_file(Path(__file__))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for split, bit_lengths, filename in (
        ("train", TRAIN_BITS, "TRAIN.jsonl"),
        ("heldout", HELDOUT_BITS, "HELDOUT.jsonl"),
    ):
        cohort = make_cohort(bit_lengths, split)
        with (args.output_dir / filename).open("w", encoding="utf-8") as handle:
            for index, meta in enumerate(cohort):
                result = analyze_input(meta)
                results.append(result)
                handle.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
                handle.flush()
                print(
                    f"{split} {index + 1}/{len(cohort)} bits={meta['bits']} "
                    f"rows={result['source']['counts']['retained']} "
                    f"direct={int(result['source']['any_predecoder_factor'])} "
                    f"decoder={int(result['any_decoder_hit'])} strict={int(result['strict_screen_free_hit'])}",
                    flush=True,
                )
    summary = summarize(results, prereg_hash, scan_hash)
    (args.output_dir / "SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

