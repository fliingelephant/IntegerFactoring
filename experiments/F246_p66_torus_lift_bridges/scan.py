#!/usr/bin/env python3
"""Preregistered F246 finite scan.

The source and decoder use public arithmetic only.  Hidden primes are used
only to build and label the fixed verifier cohort.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import resource
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path


COHORT_SEED = "F246-p66-live-bridges-cohort-v1"
SOURCE_SEED = "F246-p66-live-bridges-source-v1"
TRAIN_BITS = (20, 24, 28)
HELDOUT_BITS = (32, 36, 40)
INPUTS_PER_BIT = 8
SIGNED_D = (-1, 2, 3, 5, 7, 11)
TORUS_SAMPLES_PER_D = 32
LIFT_BASES = 192
MAX_SOURCE_ATTEMPTS = 4096
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
        self.rejections = 0

    def word(self) -> int:
        payload = f"{self.label}:{self.counter}".encode()
        self.counter += 1
        return int.from_bytes(hashlib.sha256(payload).digest(), "big")

    def below(self, modulus: int) -> int:
        require(modulus > 0, "random modulus must be positive")
        limit = (1 << 256) - ((1 << 256) % modulus)
        while True:
            value = self.word()
            if value < limit:
                return value % modulus
            self.rejections += 1


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
    start = low + stream.below(span)
    start |= 1
    candidate = start
    while True:
        if is_prime_64(candidate):
            return candidate
        candidate += 2
        if candidate >= low + span:
            candidate = low | 1
        require(candidate != start, "prime search wrapped without a prime")


def make_cohort(bit_lengths: tuple[int, ...], split: str) -> list[dict[str, int | str]]:
    cohort = []
    seen: set[int] = set()
    for bits in bit_lengths:
        require(bits % 2 == 0, "frozen target lengths must be even")
        pair_counter = 0
        while sum(1 for row in cohort if row["bits"] == bits) < INPUTS_PER_BIT:
            p = prime_from_hash(
                f"{COHORT_SEED}:{split}:{bits}:{pair_counter}:p", bits // 2
            )
            q = prime_from_hash(
                f"{COHORT_SEED}:{split}:{bits}:{pair_counter}:q", bits // 2
            )
            pair_counter += 1
            p, q = sorted((p, q))
            modulus = p * q
            if p == q or q >= 2 * p or modulus.bit_length() != bits or modulus in seen:
                continue
            seen.add(modulus)
            cohort.append(
                {
                    "split": split,
                    "bits": bits,
                    "index_within_bits": sum(1 for row in cohort if row["bits"] == bits),
                    "N": modulus,
                    "verifier_p": p,
                    "verifier_q": q,
                }
            )
    return cohort


def jacobi(a: int, modulus: int) -> int:
    require(modulus > 0 and modulus % 2 == 1, "Jacobi modulus must be positive and odd")
    a %= modulus
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if modulus % 8 in (3, 5):
                result = -result
        a, modulus = modulus, a
        if a % 4 == modulus % 4 == 3:
            result = -result
        a %= modulus
    return result if modulus == 1 else 0


def pair_mul(left: tuple[int, int], right: tuple[int, int], d0: int, modulus: int) -> tuple[int, int]:
    x, y = left
    z, t = right
    return ((x * z + d0 * y * t) % modulus, (x * t + y * z) % modulus)


def pair_pow(base: tuple[int, int], exponent: int, d0: int, modulus: int) -> tuple[tuple[int, int], int]:
    result = (1, 0)
    current = base
    multiplications = 0
    while exponent:
        if exponent & 1:
            result = pair_mul(result, current, d0, modulus)
            multiplications += 1
        exponent >>= 1
        if exponent:
            current = pair_mul(current, current, d0, modulus)
            multiplications += 1
    return result, multiplications


def signed_screens(point: tuple[int, int], modulus: int) -> tuple[int, int]:
    x, y = point
    return math.gcd(modulus, x - 1, y), math.gcd(modulus, x + 1, y)


def miller_chain(
    base: tuple[int, int], exponent: int, d0: int, modulus: int
) -> tuple[int | None, dict[str, int]]:
    odd = exponent
    valuation = 0
    while odd % 2 == 0:
        valuation += 1
        odd //= 2
    point, multiplications = pair_pow(base, odd, d0, modulus)
    screens = 0
    for stage in range(valuation + 1):
        plus, minus = signed_screens(point, modulus)
        screens += 2
        for divisor in (plus, minus):
            if proper(divisor, modulus):
                return divisor, {
                    "stages_tested": stage + 1,
                    "screen_gcds": screens,
                    "pair_multiplications": multiplications,
                }
        if stage < valuation:
            point = pair_mul(point, point, d0, modulus)
            multiplications += 1
    return None, {
        "stages_tested": valuation + 1,
        "screen_gcds": screens,
        "pair_multiplications": multiplications,
    }


def generate_public_sources(modulus: int, bits: int, input_label: str) -> tuple[list[dict[str, object]], dict[str, object]]:
    """Generate sources from N only.  Hidden factors are not parameters."""
    start_wall = time.perf_counter_ns()
    start_cpu = time.process_time_ns()
    records: list[dict[str, object]] = []
    events: Counter[str] = Counter()
    costs: Counter[str] = Counter()
    torus_attempts_by_d: dict[str, int] = {}

    for signed_d in SIGNED_D:
        d0 = signed_d % modulus
        d_gcd = math.gcd(d0, modulus)
        costs["public_gcds"] += 1
        if proper(d_gcd, modulus):
            events["discriminant_direct_factor"] += 1
            continue
        require(d_gcd == 1, "frozen discriminant unexpectedly vanishes globally")
        j = jacobi(d0, modulus)
        require(j in (-1, 1), "unit discriminant has zero Jacobi symbol")
        stream = HashStream(f"{SOURCE_SEED}:{input_label}:torus:{signed_d}")
        accepted = 0
        attempts = 0
        while accepted < TORUS_SAMPLES_PER_D:
            attempts += 1
            require(attempts <= MAX_SOURCE_ATTEMPTS, "torus source attempt cap exceeded")
            a = stream.below(modulus)
            b = stream.below(modulus)
            coefficient_gcd = math.gcd(modulus, a, b)
            costs["public_gcds"] += 1
            if proper(coefficient_gcd, modulus):
                events["torus_coefficient_direct_factor"] += 1
                continue
            if coefficient_gcd == modulus:
                events["torus_global_zero_reject"] += 1
                continue
            nu = (a * a - d0 * b * b) % modulus
            norm_gcd = math.gcd(nu, modulus)
            costs["public_gcds"] += 1
            if proper(norm_gcd, modulus):
                events["torus_norm_direct_factor"] += 1
                continue
            if norm_gcd == modulus:
                events["torus_global_nonunit_reject"] += 1
                continue
            inv_nu = pow(nu, -1, modulus)
            costs["modular_inverses"] += 1
            u = ((a * a + d0 * b * b) * inv_nu % modulus, 2 * a * b * inv_nu % modulus)
            require((u[0] * u[0] - d0 * u[1] * u[1]) % modulus == 1, "Hilbert--90 norm check failed")
            accepted += 1

            mode_exponents = (
                ("raw", 1),
                ("p208_w1", modulus - j),
                ("p209", modulus * modulus - 1),
            )
            for mode, exponent in mode_exponents:
                if mode == "raw":
                    point = u
                    power_multiplications = 0
                else:
                    point, power_multiplications = pair_pow(u, exponent, d0, modulus)
                    costs["torus_power_calls"] += 1
                    costs["torus_pair_multiplications"] += power_multiplications
                plus, minus = signed_screens(point, modulus)
                costs["public_gcds"] += 2
                if proper(plus, modulus):
                    events[f"torus_{mode}_Gplus_direct_factor"] += 1
                    continue
                if proper(minus, modulus):
                    events[f"torus_{mode}_Gminus_direct_factor"] += 1
                    continue
                if plus == modulus:
                    events[f"torus_{mode}_global_plus_return"] += 1
                    factor, chain_cost = miller_chain(u, exponent, d0, modulus)
                    costs["miller_screen_gcds"] += chain_cost["screen_gcds"]
                    costs["miller_pair_multiplications"] += chain_cost["pair_multiplications"]
                    if factor is not None:
                        require(modulus % factor == 0, "Miller output is not a divisor")
                        events[f"torus_{mode}_miller_factor"] += 1
                    else:
                        events[f"torus_{mode}_miller_null"] += 1
                    continue
                if minus == modulus:
                    events[f"torus_{mode}_global_minus_return"] += 1
                    continue
                require(plus == minus == 1, "signed screen classification is incomplete")
                x, y = point
                value = 1 + d0 * y * y
                root_gcd = math.gcd(x, modulus)
                costs["public_gcds"] += 1
                if proper(root_gcd, modulus):
                    events[f"torus_{mode}_root_direct_factor"] += 1
                    continue
                require(root_gcd == 1, "torus supplied root vanishes globally")
                require(pow(x, 2, modulus) == value % modulus, "torus known-root congruence failed")
                records.append(
                    {
                        "id": f"torus:{signed_d}:{mode}:{accepted - 1}",
                        "arm": "torus",
                        "D": signed_d,
                        "mode": mode,
                        "value": value,
                        "root": x,
                        "flags": [],
                    }
                )
                events[f"torus_{mode}_admitted"] += 1
        torus_attempts_by_d[str(signed_d)] = attempts
        costs["hash_words"] += stream.counter
        costs["hash_rejections"] += stream.rejections

    lift_stream = HashStream(f"{SOURCE_SEED}:{input_label}:lift")
    accepted_bases = 0
    lift_attempts = 0
    while accepted_bases < LIFT_BASES:
        lift_attempts += 1
        require(lift_attempts <= MAX_SOURCE_ATTEMPTS, "lift source attempt cap exceeded")
        base = lift_stream.below(modulus)
        divisor = math.gcd(base, modulus)
        costs["public_gcds"] += 1
        if proper(divisor, modulus):
            events["lift_base_direct_factor"] += 1
            continue
        if divisor == modulus:
            events["lift_zero_reject"] += 1
            continue
        accepted_bases += 1
        for mode, exponent in (("nm1", modulus - 1), ("n2m1", modulus * modulus - 1)):
            value = pow(base, exponent, modulus * modulus)
            root = pow(base, exponent // 2, modulus)
            costs["scalar_modular_power_calls"] += 2
            require(value > 0, "unit lift must be a positive residue")
            require(pow(root, 2, modulus) == value % modulus, "lift known-root congruence failed")
            root_gcd = math.gcd(root, modulus)
            costs["public_gcds"] += 1
            require(root_gcd == 1, "unit lift supplied root is not a unit")
            plus = math.gcd(value - 1, modulus)
            minus = math.gcd(value + 1, modulus)
            costs["public_gcds"] += 2
            if proper(plus, modulus):
                events[f"lift_{mode}_Gplus_direct_factor"] += 1
                continue
            if proper(minus, modulus):
                events[f"lift_{mode}_Gminus_direct_factor"] += 1
                continue
            flags = []
            if plus == modulus:
                events[f"lift_{mode}_global_plus_return"] += 1
                flags.append("global_plus_return")
                root_minus = math.gcd(root - 1, modulus)
                root_plus = math.gcd(root + 1, modulus)
                costs["public_gcds"] += 2
                if proper(root_minus, modulus) or proper(root_plus, modulus):
                    factor = root_minus if proper(root_minus, modulus) else root_plus
                    require(modulus % factor == 0, "lift root screen is not a divisor")
                    events[f"lift_{mode}_root_miller_factor"] += 1
                    continue
                events[f"lift_{mode}_root_miller_null"] += 1
            if minus == modulus:
                events[f"lift_{mode}_global_minus_return"] += 1
                flags.append("global_minus_return")
            records.append(
                {
                    "id": f"lift:{mode}:{accepted_bases - 1}",
                    "arm": "lift",
                    "mode": mode,
                    "value": value,
                    "root": root,
                    "flags": flags,
                }
            )
            events[f"lift_{mode}_admitted"] += 1
    costs["hash_words"] += lift_stream.counter
    costs["hash_rejections"] += lift_stream.rejections
    source_wall = time.perf_counter_ns() - start_wall
    source_cpu = time.process_time_ns() - start_cpu
    direct_factor_count = sum(count for name, count in events.items() if name.endswith("direct_factor"))
    miller_factor_count = sum(count for name, count in events.items() if name.endswith("miller_factor"))
    return records, {
        "bits": bits,
        "events": dict(sorted(events.items())),
        "costs": dict(sorted(costs.items())),
        "torus_attempts_by_D": torus_attempts_by_d,
        "lift_attempts": lift_attempts,
        "admitted_rows": len(records),
        "direct_factor_events": direct_factor_count,
        "miller_factor_events": miller_factor_count,
        "any_predecoder_factor": direct_factor_count + miller_factor_count > 0,
        "wall_ns": source_wall,
        "cpu_ns": source_cpu,
    }


def factor_free_rows(values: list[int]) -> tuple[list[int], dict[str, int]]:
    pending = [(value, 1 << index) for index, value in enumerate(values) if value > 1]
    stable: list[tuple[int, int]] = []
    stats = Counter()
    stats["initial_entries"] = len(pending)
    while pending:
        value, mask = pending.pop()
        stats["pops"] += 1
        if value <= 1 or mask == 0:
            stats["discarded_unit_or_zero_mask"] += 1
            continue
        for position, (old_value, old_mask) in enumerate(stable):
            stats["gcd_scans"] += 1
            divisor = math.gcd(value, old_value)
            if divisor == 1:
                continue
            stable.pop(position)
            stats["refinements"] += 1
            pending.extend(
                (
                    (divisor, mask ^ old_mask),
                    (value // divisor, mask),
                    (old_value // divisor, old_mask),
                )
            )
            break
        else:
            stable.append((value, mask))
            stats["max_stable"] = max(stats["max_stable"], len(stable))
        stats["max_pending"] = max(stats["max_pending"], len(pending))
    stable.sort()
    for index, (value, mask) in enumerate(stable):
        require(mask != 0, "stable fragment has zero mask")
        require(all(math.gcd(value, other) == 1 for other, _ in stable[:index]), "fragments are not coprime")
    rows = []
    for value, mask in stable:
        root = math.isqrt(value)
        if root * root == value:
            stats["square_fragments_removed"] += 1
        else:
            rows.append(mask)
    unique_rows = sorted(set(rows))
    stats["stable_fragments"] = len(stable)
    stats["nonsquare_fragment_rows"] = len(rows)
    stats["duplicate_rows_removed"] = len(rows) - len(unique_rows)
    stats["unique_parity_rows"] = len(unique_rows)
    return unique_rows, dict(sorted(stats.items()))


def kernel_basis(rows: list[int], column_count: int) -> tuple[int, list[int]]:
    pivots: dict[int, int] = {}
    for source_row in sorted(set(row for row in rows if row)):
        row = source_row
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
        require(all((row & vector).bit_count() % 2 == 0 for row in rows), "kernel vector check failed")
        basis.append(vector)
    require(len(pivots) + len(basis) == column_count, "rank-nullity failed")
    return len(pivots), basis


def support_indices(vector: int) -> list[int]:
    support = []
    while vector:
        bit = vector & -vector
        support.append(bit.bit_length() - 1)
        vector ^= bit
    return support


def decode_bank(name: str, records: list[dict[str, object]], modulus: int, any_predecoder_factor: bool) -> dict[str, object]:
    start_wall = time.perf_counter_ns()
    start_cpu = time.process_time_ns()
    for record in records:
        value = int(record["value"])
        root = int(record["root"])
        require(value > 0, "P66 value must be positive")
        require(math.gcd(root, modulus) == 1, "P66 root must be a unit")
        require(pow(root, 2, modulus) == value % modulus, "P66 row root mismatch")
    rows, refine_stats = factor_free_rows([int(record["value"]) for record in records])
    rank, basis = kernel_basis(rows, len(records))
    non_global = 0
    classes = Counter()
    certificates = []
    normalized_roots = {1}
    for basis_index, vector in enumerate(basis):
        indices = support_indices(vector)
        product = 1
        supplied = 1
        for index in indices:
            product *= int(records[index]["value"])
            supplied = supplied * int(records[index]["root"]) % modulus
        positive_root = math.isqrt(product)
        require(positive_root * positive_root == product, "P66 kernel product is not a square")
        positive_mod = positive_root % modulus
        require(pow(positive_mod, 2, modulus) == pow(supplied, 2, modulus), "P66 roots do not square alike")
        minus = math.gcd((positive_mod - supplied) % modulus, modulus)
        plus = math.gcd((positive_mod + supplied) % modulus, modulus)
        rho = positive_mod * pow(supplied, -1, modulus) % modulus
        require(pow(rho, 2, modulus) == 1, "normalized root is not 2-torsion")
        normalized_roots.add(min(rho, modulus - rho))
        if rho == 1:
            classes["+1"] += 1
        elif rho == modulus - 1:
            classes["-1"] += 1
        else:
            classes["non_global"] += 1
            non_global += 1
            require(proper(minus, modulus) and proper(plus, modulus), "non-global root did not split semiprime")
            require(modulus % minus == modulus % plus == 0, "P66 gcd output is not a divisor")
            if len(certificates) < 3:
                support_ids = [str(records[index]["id"]) for index in indices]
                support_payload = json.dumps(support_ids, separators=(",", ":")).encode()
                certificates.append(
                    {
                        "basis_index": basis_index,
                        "vector_hex": hex(vector),
                        "support": len(indices),
                        "support_ids_first_12": support_ids[:12],
                        "support_ids_sha256": hashlib.sha256(support_payload).hexdigest(),
                        "positive_root_mod_N": positive_mod,
                        "supplied_root_mod_N": supplied,
                        "normalized_root_mod_N": rho,
                        "gcd_R_minus_X": minus,
                        "gcd_R_plus_X": plus,
                    }
                )
    wall_ns = time.perf_counter_ns() - start_wall
    cpu_ns = time.process_time_ns() - start_cpu
    return {
        "name": name,
        "columns": len(records),
        "parity_rows": len(rows),
        "rank": rank,
        "kernel_dimension": len(basis),
        "basis_root_classes": dict(sorted(classes.items())),
        "non_global_basis_root_hits": non_global,
        "normalized_root_image_size_on_basis": len(normalized_roots),
        "strict_screen_free_hit": non_global > 0 and not any_predecoder_factor,
        "certificates": certificates,
        "refinement": refine_stats,
        "wall_ns": wall_ns,
        "cpu_ns": cpu_ns,
    }


def frozen_banks(records: list[dict[str, object]]) -> list[tuple[str, list[dict[str, object]]]]:
    banks = []
    for signed_d in SIGNED_D:
        for mode in ("raw", "p208_w1", "p209"):
            banks.append(
                (
                    f"torus_D{signed_d}_{mode}",
                    [row for row in records if row["arm"] == "torus" and row["D"] == signed_d and row["mode"] == mode],
                )
            )
    for mode in ("raw", "p208_w1", "p209"):
        banks.append((f"torus_mode_{mode}", [row for row in records if row["arm"] == "torus" and row["mode"] == mode]))
    for signed_d in SIGNED_D:
        banks.append((f"torus_D{signed_d}_all_modes", [row for row in records if row["arm"] == "torus" and row["D"] == signed_d]))
    banks.append(("torus_all", [row for row in records if row["arm"] == "torus"]))
    for mode in ("nm1", "n2m1"):
        banks.append((f"lift_{mode}", [row for row in records if row["arm"] == "lift" and row["mode"] == mode]))
    banks.append(("lift_all", [row for row in records if row["arm"] == "lift"]))
    banks.append(("grand_union", list(records)))
    require(len(banks) == 32, "frozen bank count changed")
    return banks


def analyze_input(meta: dict[str, int | str]) -> dict[str, object]:
    modulus = int(meta["N"])
    records, source = generate_public_sources(
        modulus, int(meta["bits"]), f"{meta['split']}:{meta['bits']}:{meta['index_within_bits']}:{modulus}"
    )
    banks = [decode_bank(name, bank, modulus, bool(source["any_predecoder_factor"])) for name, bank in frozen_banks(records)]
    strict_banks = [bank["name"] for bank in banks if bank["strict_screen_free_hit"]]
    any_decoder_banks = [bank["name"] for bank in banks if bank["non_global_basis_root_hits"] > 0]
    return {
        "meta": meta,
        "source": source,
        "banks": banks,
        "any_decoder_hit": bool(any_decoder_banks),
        "decoder_hit_banks": any_decoder_banks,
        "strict_screen_free_hit": bool(strict_banks),
        "strict_hit_banks": strict_banks,
    }


def summarize(results: list[dict[str, object]], prereg_sha256: str, scan_sha256: str) -> dict[str, object]:
    split_summary = {}
    for split in ("train", "heldout"):
        selected = [row for row in results if row["meta"]["split"] == split]
        bit_counts = Counter()
        hit_bits = Counter()
        decoder_inputs = 0
        strict_inputs = 0
        direct_events = 0
        miller_events = 0
        bank_hits = Counter()
        strict_bank_hits = Counter()
        for row in selected:
            bits = int(row["meta"]["bits"])
            bit_counts[bits] += 1
            decoder_inputs += int(bool(row["any_decoder_hit"]))
            strict_inputs += int(bool(row["strict_screen_free_hit"]))
            if row["strict_screen_free_hit"]:
                hit_bits[bits] += 1
            direct_events += int(row["source"]["direct_factor_events"])
            miller_events += int(row["source"]["miller_factor_events"])
            bank_hits.update(row["decoder_hit_banks"])
            strict_bank_hits.update(row["strict_hit_banks"])
        split_summary[split] = {
            "inputs": len(selected),
            "inputs_by_bits": dict(sorted(bit_counts.items())),
            "inputs_with_any_decoder_hit": decoder_inputs,
            "inputs_with_strict_screen_free_hit": strict_inputs,
            "strict_hits_by_bits": dict(sorted(hit_bits.items())),
            "direct_factor_events": direct_events,
            "miller_factor_events": miller_events,
            "decoder_hit_input_counts_by_bank": dict(sorted(bank_hits.items())),
            "strict_hit_input_counts_by_bank": dict(sorted(strict_bank_hits.items())),
        }
    heldout = split_summary["heldout"]
    covered_lengths = len(heldout["strict_hits_by_bits"])
    if heldout["inputs_with_strict_screen_free_hit"] >= 3 and covered_lengths >= 2:
        interpretation = "strong finite signal"
    elif heldout["inputs_with_strict_screen_free_hit"] >= 1:
        interpretation = "weak finite signal"
    else:
        interpretation = "null finite signal"
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return {
        "experiment": "F246_p66_torus_lift_bridges",
        "preregistration_sha256": prereg_sha256,
        "scan_sha256": scan_sha256,
        "parameters": {
            "train_bits": TRAIN_BITS,
            "heldout_bits": HELDOUT_BITS,
            "inputs_per_bit": INPUTS_PER_BIT,
            "signed_D": SIGNED_D,
            "torus_samples_per_D": TORUS_SAMPLES_PER_D,
            "lift_bases": LIFT_BASES,
            "bank_count": 32,
        },
        "splits": split_summary,
        "heldout_interpretation": interpretation,
        "process_max_rss_platform_units": usage.ru_maxrss,
        "python": sys.version,
        "pid": os.getpid(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--prereg-sha256", required=True)
    args = parser.parse_args()
    require(sys.version_info >= (3, 11), "Python 3.11 or newer is required")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    script_path = Path(__file__).resolve()
    actual_prereg = sha256_file(script_path.with_name("PREREGISTRATION.md"))
    require(actual_prereg == args.prereg_sha256, "preregistration hash mismatch")
    scan_hash = sha256_file(script_path)
    all_results = []
    for split, bit_lengths, filename in (
        ("train", TRAIN_BITS, "TRAIN.jsonl"),
        ("heldout", HELDOUT_BITS, "HELDOUT.jsonl"),
    ):
        cohort = make_cohort(bit_lengths, split)
        require(len(cohort) == len(bit_lengths) * INPUTS_PER_BIT, "cohort size mismatch")
        with (args.output_dir / filename).open("w", encoding="utf-8") as handle:
            for input_index, meta in enumerate(cohort):
                result = analyze_input(meta)
                all_results.append(result)
                handle.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
                handle.flush()
                print(
                    f"{split} {input_index + 1}/{len(cohort)} Nbits={meta['bits']} "
                    f"rows={result['source']['admitted_rows']} direct={result['source']['direct_factor_events']} "
                    f"miller={result['source']['miller_factor_events']} "
                    f"decoder={int(result['any_decoder_hit'])} strict={int(result['strict_screen_free_hit'])}",
                    flush=True,
                )
    summary = summarize(all_results, actual_prereg, scan_hash)
    (args.output_dir / "SUMMARY.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
