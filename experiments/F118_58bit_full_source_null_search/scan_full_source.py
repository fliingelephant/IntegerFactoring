#!/usr/bin/env python3
"""Registered factor-assisted 58-bit search over the complete F116 source."""

from __future__ import annotations

import argparse
from array import array
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import resource
import struct
import sys
import time

from sage.all import ZZ


sys.dont_write_bytecode = True
MASK64 = (1 << 64) - 1
MAX_LOAD_NUMERATOR = 7
MAX_LOAD_DENOMINATOR = 10


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, payload: dict[str, object]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def first_prime_at_least(value: int) -> int:
    candidate = value if value & 1 else value + 1
    while not bool(ZZ(candidate).is_prime(proof=True)):
        candidate += 2
    return candidate


def last_prime_at_most(value: int) -> int:
    candidate = value if value & 1 else value - 1
    while not bool(ZZ(candidate).is_prime(proof=True)):
        candidate -= 2
    return candidate


def next_prime(value: int) -> int:
    return first_prime_at_least(value + 1)


def previous_prime(value: int) -> int:
    return last_prime_at_most(value - 1)


def integer_nth_root(value: int, exponent: int) -> int:
    low = 1 << ((value.bit_length() - 1) // exponent)
    high = 1 << ((value.bit_length() + exponent - 1) // exponent)
    while low + 1 < high:
        middle = (low + high) // 2
        if pow(middle, exponent) <= value:
            low = middle
        else:
            high = middle
    return low


@lru_cache(maxsize=4096)
def maximal_perfect_power(value: int) -> tuple[int, int]:
    for exponent in range(value.bit_length() - 1, 1, -1):
        base = integer_nth_root(value, exponent)
        if pow(base, exponent) == value:
            return base, exponent
    return value, 1


def deterministic_gcd_basis(
    values: list[int],
) -> list[tuple[int, dict[int, int]]]:
    stack = [(value, {index: 1}) for index, value in enumerate(values) if value > 1]
    basis: list[tuple[int, dict[int, int]]] = []
    while stack:
        value, signature = stack.pop()
        if value == 1:
            continue
        base, exponent = maximal_perfect_power(value)
        if exponent > 1:
            value = base
            signature = {
                endpoint: multiplicity * exponent
                for endpoint, multiplicity in signature.items()
            }
        for index, (other, other_signature) in enumerate(basis):
            divisor = math.gcd(value, other)
            if divisor == 1:
                continue
            basis.pop(index)
            if value == other:
                merged = signature.copy()
                for endpoint, multiplicity in other_signature.items():
                    merged[endpoint] = merged.get(endpoint, 0) + multiplicity
                stack.append((value, merged))
            else:
                stack.extend(
                    [
                        (divisor, signature),
                        (value // divisor, signature),
                        (divisor, other_signature),
                        (other // divisor, other_signature),
                    ]
                )
            break
        else:
            basis.append((value, signature))
    basis.sort(key=lambda item: item[0])
    return basis


def frozen_seed_pairs(modulus: int, n: int) -> tuple[list[tuple[int, int]], dict[str, object]]:
    endpoints: list[int] = []
    for seed in range(2, n + 1):
        endpoints.extend((seed, pow(seed, -1, modulus)))
    basis = deterministic_gcd_basis(endpoints)
    blocks = [block for block, _ in basis]
    if any(
        math.gcd(blocks[left], blocks[right]) != 1
        for left in range(len(blocks))
        for right in range(left + 1, len(blocks))
    ):
        raise AssertionError("seed basis is not pairwise coprime")
    reconstructed = [1] * len(endpoints)
    for block, signature in basis:
        if maximal_perfect_power(block)[1] != 1:
            raise AssertionError("seed basis contains a perfect power")
        for endpoint, multiplicity in signature.items():
            reconstructed[endpoint] *= pow(block, multiplicity)
    if reconstructed != endpoints:
        raise AssertionError("seed basis does not reconstruct endpoints")
    pairs: list[tuple[int, int]] = []
    for seed_index in range(n - 1):
        left_endpoint = 2 * seed_index
        right_endpoint = left_endpoint + 1
        support = [
            block
            for block, signature in basis
            if signature.get(left_endpoint, 0)
            + signature.get(right_endpoint, 0)
            > 0
        ]
        if not support:
            raise AssertionError("empty seed support")
        pairs.append((support[0], 1 if len(support) == 1 else support[1]))
    digest = hashlib.sha256()
    for left, right in pairs:
        digest.update(left.to_bytes(8, "big"))
        digest.update(right.to_bytes(8, "big"))
    return pairs, {
        "endpoint_count": len(endpoints),
        "block_count": len(basis),
        "pair_count": len(pairs),
        "pair_sha256": digest.hexdigest(),
        "pairs": [[left, right] for left, right in pairs],
        "pairwise_coprime": True,
        "perfect_power_free": True,
        "exact_endpoint_reconstruction": True,
    }


class CompactSeen:
    def __init__(self, maximum_items: int) -> None:
        required = (maximum_items * MAX_LOAD_DENOMINATOR + MAX_LOAD_NUMERATOR - 1) // MAX_LOAD_NUMERATOR
        capacity = 1
        while capacity < required:
            capacity <<= 1
        self.slots = array("Q", [0]) * capacity
        self.mask = capacity - 1
        self.count = 0
        self.maximum_probe = 0

    @staticmethod
    def mixed(value: int) -> int:
        value = (value + 0x9E3779B97F4A7C15) & MASK64
        value = ((value ^ (value >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
        value = ((value ^ (value >> 27)) * 0x94D049BB133111EB) & MASK64
        return value ^ (value >> 31)

    def add(self, value: int) -> bool:
        if value == 0:
            raise AssertionError("zero cannot be stored in the canonical-unit table")
        index = self.mixed(value) & self.mask
        probe = 0
        while True:
            old = self.slots[index]
            if old == 0:
                self.slots[index] = value
                self.count += 1
                self.maximum_probe = max(self.maximum_probe, probe)
                return True
            if old == value:
                self.maximum_probe = max(self.maximum_probe, probe)
                return False
            index = (index + 1) & self.mask
            probe += 1

    def summary(self) -> dict[str, int | float]:
        return {
            "capacity_slots": len(self.slots),
            "payload_bytes": len(self.slots) * self.slots.itemsize,
            "items": self.count,
            "load_factor": self.count / len(self.slots),
            "maximum_probe": self.maximum_probe,
        }


@lru_cache(maxsize=200_000)
def factor_integer(value: int) -> tuple[tuple[int, int], ...]:
    if value == 1:
        return ()
    factors = tuple((int(prime), int(exponent)) for prime, exponent in ZZ(value).factor())
    if math.prod(prime**exponent for prime, exponent in factors) != value:
        raise AssertionError("endpoint factorization does not reconstruct")
    return factors


class RootImageDecoder:
    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.pivots: dict[int, tuple[frozenset[int], int]] = {}
        self.dependencies = 0
        self.global_plus = 0
        self.global_minus = 0
        self.non_global = 0
        self.eliminations = 0
        self.maximum_reduced_support = 0

    def add(self, factors: dict[int, int]) -> dict[str, int | str] | None:
        parity = {prime for prime, exponent in factors.items() if exponent & 1}
        half_root = 1
        for prime, exponent in factors.items():
            half_root = half_root * pow(prime, exponent // 2, self.modulus) % self.modulus
        self.maximum_reduced_support = max(self.maximum_reduced_support, len(parity))
        while parity:
            pivot = max(parity)
            known = self.pivots.get(pivot)
            if known is None:
                self.pivots[pivot] = (frozenset(parity), half_root)
                return None
            known_parity, known_half_root = known
            common = parity.intersection(known_parity)
            half_root = half_root * known_half_root % self.modulus
            for prime in common:
                half_root = half_root * prime % self.modulus
            parity.symmetric_difference_update(known_parity)
            self.eliminations += 1
            self.maximum_reduced_support = max(self.maximum_reduced_support, len(parity))

        self.dependencies += 1
        if pow(half_root, 2, self.modulus) != 1:
            raise AssertionError("dependency invariant did not produce a root of one")
        if half_root == 1:
            self.global_plus += 1
            return None
        if half_root == self.modulus - 1:
            self.global_minus += 1
            return None
        self.non_global += 1
        minus = math.gcd(half_root - 1, self.modulus)
        plus = math.gcd(half_root + 1, self.modulus)
        if not (1 < minus < self.modulus and 1 < plus < self.modulus):
            raise AssertionError("non-global semiprime root did not split both signs")
        return {
            "method": "factor_assisted_normalized_root",
            "root_mod_N": half_root,
            "gcd_root_minus_one_N": minus,
            "gcd_root_plus_one_N": plus,
        }

    def snapshot(self, retained: int) -> dict[str, int]:
        rank = len(self.pivots)
        if self.dependencies != retained - rank:
            raise AssertionError("online dependencies do not equal nullity")
        return {
            "columns": retained,
            "rank": rank,
            "kernel_nullity": self.dependencies,
            "global_plus_basis_roots": self.global_plus,
            "global_minus_basis_roots": self.global_minus,
            "non_global_basis_roots": self.non_global,
            "normalized_root_quotient_image_dimension": 1 if self.non_global else 0,
            "eliminations": self.eliminations,
            "maximum_reduced_parity_support": self.maximum_reduced_support,
        }


def peak_rss() -> dict[str, int | str]:
    return {
        "ru_maxrss_raw": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "platform": sys.platform,
        "unit": "bytes on macOS; KiB on Linux",
    }


def scan_case(
    p: int,
    q: int,
    ordinal: int,
    progress_callback,
) -> dict[str, object]:
    started = time.monotonic()
    modulus = p * q
    n = modulus.bit_length()
    bound = n * n
    frozen_attempt_limit = (n - 1) * 2 * (bound + 1)
    menu_pair_count = (n - 1) * (n - 2) // 2
    menu_attempt_limit = menu_pair_count * 2 * (bound + 1)
    full_attempt_limit = (n - 1) + frozen_attempt_limit + menu_attempt_limit
    seen = CompactSeen(full_attempt_limit)
    decoder = RootImageDecoder(modulus)
    all_attempt_hash = hashlib.sha256()
    retained_hash = hashlib.sha256()
    attempts = 0
    duplicates = 0
    retained = 0
    witness: dict[str, object] | None = None
    factor_integer.cache_clear()
    maximal_perfect_power.cache_clear()

    def metrics(phase: str, completed_pairs: int, total_pairs: int) -> dict[str, object]:
        return {
            "phase": phase,
            "completed_pairs": completed_pairs,
            "total_pairs": total_pairs,
            "attempts": attempts,
            "unique_residues": seen.count,
            "duplicates": duplicates,
            "retained_relations": retained,
            "decoder": decoder.snapshot(retained),
            "seen_table": seen.summary(),
            "factor_cache": {
                "hits": factor_integer.cache_info().hits,
                "misses": factor_integer.cache_info().misses,
                "current_size": factor_integer.cache_info().currsize,
                "maximum_size": factor_integer.cache_info().maxsize,
            },
            "all_attempt_prefix_sha256": all_attempt_hash.copy().hexdigest(),
            "retained_prefix_sha256": retained_hash.copy().hexdigest(),
            "peak_rss": peak_rss(),
            "elapsed_seconds": time.monotonic() - started,
        }

    def attempt(
        residue: int,
        kind: int,
        pair_index: int,
        left: int,
        right: int,
        exponent: int,
        orientation: int,
    ) -> dict[str, object] | None:
        nonlocal attempts, duplicates, retained
        attempts += 1
        all_attempt_hash.update(
            struct.pack(">BIIBQ", kind, pair_index, exponent, orientation, residue)
        )
        if not seen.add(residue):
            duplicates += 1
            return None
        provenance = {
            "kind": ("seed", "frozen_seed_basis_pair", "nonadaptive_seed_pair")[kind],
            "pair_index_zero_based": pair_index,
            "u": left,
            "v": right,
            "exponent": exponent,
            "orientation": orientation,
        }
        common = math.gcd(residue, modulus)
        if common != 1:
            if 1 < common < modulus:
                return {
                    "method": "direct_residue_gcd",
                    "factor": common,
                    "residue": residue,
                    "provenance": provenance,
                }
            raise AssertionError("canonical residue is zero modulo N")
        inverse = pow(residue, -1, modulus)
        for sign, difference in (("minus", residue - inverse), ("plus", residue + inverse)):
            divisor = math.gcd(difference, modulus)
            if 1 < divisor < modulus:
                return {
                    "method": f"direct_endpoint_{sign}",
                    "factor": divisor,
                    "residue": residue,
                    "inverse": inverse,
                    "provenance": provenance,
                }
        factors = dict(factor_integer(residue))
        for prime, multiplicity in factor_integer(inverse):
            factors[prime] = factors.get(prime, 0) + multiplicity
        relation_index = retained
        retained_hash.update(
            struct.pack(">QQQ", relation_index, residue, inverse)
        )
        retained += 1
        root_witness = decoder.add(factors)
        if root_witness is None:
            return None
        return root_witness | {
            "relation_index_zero_based": relation_index,
            "residue": residue,
            "inverse": inverse,
            "provenance": provenance,
        }

    for seed_index, seed in enumerate(range(2, n + 1)):
        witness = attempt(seed, 0, seed_index, seed, 1, 0, 0)
        if witness is not None:
            raise AssertionError("trial-hard seed layer produced a factor")

    frozen_pairs, basis_summary = frozen_seed_pairs(modulus, n)
    for pair_index, (left, right) in enumerate(frozen_pairs):
        left_power = 1
        right_power = 1
        for exponent in range(bound + 1):
            witness = attempt(
                left_power * right % modulus,
                1,
                pair_index,
                left,
                right,
                exponent,
                0,
            )
            if witness is None:
                witness = attempt(
                    left * right_power % modulus,
                    1,
                    pair_index,
                    left,
                    right,
                    exponent,
                    1,
                )
            if witness is not None:
                break
            left_power = left_power * left % modulus
            right_power = right_power * right % modulus
        if pair_index % 5 == 0 or witness is not None or pair_index + 1 == len(frozen_pairs):
            progress_callback(
                ordinal,
                metrics("frozen", pair_index + 1, len(frozen_pairs)),
            )
        if witness is not None:
            return {
                "ordinal": ordinal,
                "p": p,
                "q": q,
                "N": modulus,
                "n": n,
                "B": bound,
                "selected": False,
                "status": "frozen_factor",
                "basis": basis_summary,
                "witness": witness,
                "frozen": metrics("frozen_stopped", pair_index + 1, len(frozen_pairs)),
                "elapsed_seconds": time.monotonic() - started,
            }

    if attempts != (n - 1) + frozen_attempt_limit:
        raise AssertionError("frozen source attempt count is incomplete")
    frozen = metrics("frozen_complete", len(frozen_pairs), len(frozen_pairs))
    if decoder.dependencies == 0:
        return {
            "ordinal": ordinal,
            "p": p,
            "q": q,
            "N": modulus,
            "n": n,
            "B": bound,
            "selected": False,
            "status": "frozen_kernel_zero",
            "basis": basis_summary,
            "frozen": frozen,
            "elapsed_seconds": time.monotonic() - started,
        }
    if decoder.non_global:
        raise AssertionError("non-global frozen root was not returned as a witness")

    menu_index = 0
    for left in range(2, n):
        for right in range(left + 1, n + 1):
            left_power = 1
            right_power = 1
            for exponent in range(bound + 1):
                witness = attempt(
                    left_power * right % modulus,
                    2,
                    menu_index,
                    left,
                    right,
                    exponent,
                    0,
                )
                if witness is None:
                    witness = attempt(
                        left * right_power % modulus,
                        2,
                        menu_index,
                        left,
                        right,
                        exponent,
                        1,
                    )
                if witness is not None:
                    break
                left_power = left_power * left % modulus
                right_power = right_power * right % modulus
            if menu_index % 5 == 0 or witness is not None or menu_index + 1 == menu_pair_count:
                progress_callback(
                    ordinal,
                    metrics("menu", menu_index + 1, menu_pair_count),
                )
            if witness is not None:
                return {
                    "ordinal": ordinal,
                    "p": p,
                    "q": q,
                    "N": modulus,
                    "n": n,
                    "B": bound,
                    "selected": True,
                    "status": "full_source_factor",
                    "basis": basis_summary,
                    "frozen": frozen,
                    "successful_pair": [left, right],
                    "menu_pairs_completed_or_started": menu_index + 1,
                    "menu_pair_total": menu_pair_count,
                    "witness": witness,
                    "full_source_at_stop": metrics("menu_stopped", menu_index + 1, menu_pair_count),
                    "elapsed_seconds": time.monotonic() - started,
                }
            menu_index += 1

    if attempts != full_attempt_limit or menu_index != menu_pair_count:
        raise AssertionError("full source did not finish exactly")
    final = metrics("full_source_complete", menu_pair_count, menu_pair_count)
    if final["decoder"]["normalized_root_quotient_image_dimension"] != 0:
        raise AssertionError("completed null has nonzero root image")
    return {
        "ordinal": ordinal,
        "p": p,
        "q": q,
        "N": modulus,
        "n": n,
        "B": bound,
        "selected": True,
        "status": "full_source_null",
        "basis": basis_summary,
        "frozen": frozen,
        "menu_pairs_completed_or_started": menu_index,
        "menu_pair_total": menu_pair_count,
        "full_source": final,
        "elapsed_seconds": time.monotonic() - started,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    started = time.monotonic()
    spec = json.loads(arguments.spec.read_text())
    required = {
        "family",
        "p_start_inclusive",
        "q_start_inclusive",
        "pair_cap",
        "selected_cap",
        "required_bit_length",
        "require_distinct_primes",
        "require_trial_hard",
        "require_p98_stable",
        "selection_rule",
        "candidate_order",
        "full_source",
        "decoder",
        "hard_timeout_seconds",
    }
    if set(spec) != required:
        raise AssertionError("corpus specification fields changed")

    trace: list[dict[str, object]] = []
    selected: list[dict[str, object]] = []
    current_progress: dict[str, object] | None = None
    source_path = Path(__file__).resolve()
    payload: dict[str, object] = {
        "status": "RUNNING",
        "role": "registered factor-assisted full-source null search",
        "factor_assisted_boundary": (
            "known input factors certify the corpus; Sage/Pari endpoint "
            "factorization supplies P106-equivalent hidden prime rows; no "
            "factor-free support is recovered"
        ),
        "spec": spec,
        "pins": {
            str(arguments.spec): sha256_file(arguments.spec),
            str(source_path): sha256_file(source_path),
        },
        "trace": trace,
        "selected": selected,
    }

    def checkpoint(ordinal: int, progress: dict[str, object]) -> None:
        nonlocal current_progress
        current_progress = {"candidate_ordinal": ordinal} | progress
        payload.update(
            {
                "status": "RUNNING",
                "trace": trace,
                "selected": selected,
                "current_progress": current_progress,
                "elapsed_seconds": time.monotonic() - started,
            }
        )
        write_json(arguments.output, payload)

    write_json(arguments.output, payload | {"elapsed_seconds": 0.0})
    p = first_prime_at_least(int(spec["p_start_inclusive"]))
    q = last_prime_at_most(int(spec["q_start_inclusive"]))
    null_case: dict[str, object] | None = None

    for ordinal in range(1, int(spec["pair_cap"]) + 1):
        modulus = p * q
        n = modulus.bit_length()
        bound = n * n
        gcd_orders = math.gcd(p - 1, q - 1)
        left_order = (p - 1) // gcd_orders
        right_order = (q - 1) // gcd_orders
        stability_gcd = math.gcd(left_order * right_order, modulus - 1)
        certification = {
            "ordinal": ordinal,
            "p": p,
            "q": q,
            "N": modulus,
            "p_prime_proved": bool(ZZ(p).is_prime(proof=True)),
            "q_prime_proved": bool(ZZ(q).is_prime(proof=True)),
            "distinct_primes": p != q,
            "not_perfect_power": p != q,
            "n": n,
            "B": bound,
            "trial_hard": p > bound and q > bound,
            "p98_stability": {
                "g": gcd_orders,
                "A": left_order,
                "B": right_order,
                "gcd_AB_N_minus_1": stability_gcd,
                "stable": stability_gcd == 1,
            },
        }
        eligible = (
            certification["p_prime_proved"]
            and certification["q_prime_proved"]
            and certification["distinct_primes"]
            and certification["not_perfect_power"]
            and n == int(spec["required_bit_length"])
            and certification["trial_hard"]
            and certification["p98_stability"]["stable"]
        )
        certification["eligible"] = eligible
        if eligible:
            result = scan_case(p, q, ordinal, checkpoint)
            row = certification | {"source_result": result}
            trace.append(row)
            if result["selected"]:
                selected.append(result)
                if result["status"] == "full_source_null":
                    null_case = result
        else:
            trace.append(certification | {"source_result": None})
        payload.update(
            {
                "trace": trace,
                "selected": selected,
                "current_progress": None,
                "elapsed_seconds": time.monotonic() - started,
            }
        )
        write_json(arguments.output, payload)
        if null_case is not None or len(selected) == int(spec["selected_cap"]):
            break
        p = next_prime(p)
        q = previous_prime(q)

    if null_case is not None:
        status = "NULL_FOUND"
        null_input = {
            "status": "FROZEN_FULL_SOURCE_NULL",
            "p": null_case["p"],
            "q": null_case["q"],
            "N": null_case["N"],
            "n": null_case["n"],
            "B": null_case["B"],
            "corpus_ordinal": null_case["ordinal"],
            "source_sha256": sha256_file(source_path),
            "corpus_spec_sha256": sha256_file(arguments.spec),
            "full_source_result": null_case,
        }
        write_json(source_path.parent / "NULL_INPUT.json", null_input)
    elif len(selected) == int(spec["selected_cap"]):
        status = "CAP_COMPLETE_NO_NULL"
    else:
        status = "SELECTION_SHORTFALL"

    payload.update(
        {
            "status": status,
            "candidate_pairs_recorded": len(trace),
            "selected_count": len(selected),
            "null_case": null_case,
            "trace": trace,
            "selected": selected,
            "current_progress": None,
            "peak_rss": peak_rss(),
            "elapsed_seconds": time.monotonic() - started,
        }
    )
    write_json(arguments.output, payload)
    print(
        json.dumps(
            {
                "status": status,
                "candidate_pairs_recorded": len(trace),
                "selected_count": len(selected),
                "null_found": null_case is not None,
                "elapsed_seconds": payload["elapsed_seconds"],
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return 0 if status in {"NULL_FOUND", "CAP_COMPLETE_NO_NULL"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
