#!/usr/bin/env python3
"""No-stop F122 scan of the exact F116/F118 source on the F120 witness."""

from __future__ import annotations

import argparse
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


def write_json(path: Path, payload: dict[str, object]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


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
            if signature.get(left_endpoint, 0) + signature.get(right_endpoint, 0) > 0
        ]
        if not support:
            raise AssertionError("empty seed support")
        pairs.append((support[0], 1 if len(support) == 1 else support[1]))

    digest = hashlib.sha256()
    for left, right in pairs:
        digest.update(struct.pack(">QQ", left, right))
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


@lru_cache(maxsize=300_000)
def factor_integer(value: int) -> tuple[tuple[int, int], ...]:
    if value == 1:
        return ()
    factors = tuple((int(prime), int(exponent)) for prime, exponent in ZZ(value).factor())
    if math.prod(prime**exponent for prime, exponent in factors) != value:
        raise AssertionError("endpoint factorization does not reconstruct")
    return factors


class CompleteRootDecoder:
    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.pivots: dict[int, tuple[frozenset[int], int, bool]] = {}
        self.dependencies = 0
        self.eliminations = 0
        self.maximum_reduced_support = 0
        self.private_basis_dependencies = 0
        self.root_histogram: dict[int, int] = {}
        self.first_root_class: dict[str, dict[str, int | bool]] = {}
        self.basis_hash = hashlib.sha256()

    def add(
        self,
        factors: dict[int, int],
        column_index: int,
        contains_private: bool,
    ) -> None:
        parity = {prime for prime, exponent in factors.items() if exponent & 1}
        half_root = 1
        for prime, exponent in factors.items():
            half_root = half_root * pow(prime, exponent // 2, self.modulus) % self.modulus
        self.maximum_reduced_support = max(self.maximum_reduced_support, len(parity))

        while parity:
            pivot = max(parity)
            known = self.pivots.get(pivot)
            if known is None:
                self.pivots[pivot] = (frozenset(parity), half_root, contains_private)
                return
            known_parity, known_half_root, known_private = known
            common = parity.intersection(known_parity)
            half_root = half_root * known_half_root % self.modulus
            for prime in common:
                half_root = half_root * prime % self.modulus
            parity.symmetric_difference_update(known_parity)
            contains_private ^= known_private
            self.eliminations += 1
            self.maximum_reduced_support = max(self.maximum_reduced_support, len(parity))

        if pow(half_root, 2, self.modulus) != 1:
            raise AssertionError("zero parity did not produce a square root of one")
        self.dependencies += 1
        if contains_private:
            self.private_basis_dependencies += 1
        self.root_histogram[half_root] = self.root_histogram.get(half_root, 0) + 1
        if half_root == 1:
            root_class = "plus_global"
        elif half_root == self.modulus - 1:
            root_class = "minus_global"
        else:
            root_class = "non_global"
        self.basis_hash.update(
            struct.pack(">QQ?", column_index, half_root, contains_private)
        )
        if root_class not in self.first_root_class:
            self.first_root_class[root_class] = {
                "column_index": column_index,
                "root": half_root,
                "gcd_root_minus_one": math.gcd(half_root - 1, self.modulus),
                "gcd_root_plus_one": math.gcd(half_root + 1, self.modulus),
                "contains_private_column": contains_private,
            }

    def snapshot(self, columns: int) -> dict[str, object]:
        rank = len(self.pivots)
        plus = self.root_histogram.get(1, 0)
        minus = self.root_histogram.get(self.modulus - 1, 0)
        non_global = self.dependencies - plus - minus
        return {
            "columns": columns,
            "rank": rank,
            "nullity": columns - rank,
            "fundamental_basis_dependencies": self.dependencies,
            "basis_count_matches_nullity": self.dependencies == columns - rank,
            "root_histogram": {
                str(root): count for root, count in sorted(self.root_histogram.items())
            },
            "plus_global_basis_roots": plus,
            "minus_global_basis_roots": minus,
            "non_global_basis_roots": non_global,
            "normalized_root_quotient_image_dimension": 1 if non_global else 0,
            "first_root_class": self.first_root_class,
            "private_basis_dependencies": self.private_basis_dependencies,
            "all_basis_dependencies_exclude_private": self.private_basis_dependencies == 0,
            "basis_stream_sha256": self.basis_hash.hexdigest(),
            "eliminations": self.eliminations,
            "maximum_reduced_support": self.maximum_reduced_support,
        }


def peak_rss() -> dict[str, int | str]:
    return {
        "ru_maxrss_raw": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "platform": sys.platform,
        "unit": "bytes on macOS; KiB on Linux",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    corpus = json.loads(Path(args.corpus).read_text())
    output_path = Path(args.output)
    modulus = int(corpus["N"])
    n = int(corpus["n"])
    bound = int(corpus["B"])
    private_prime = int(corpus["private_prime"])
    private_exact_value = int(corpus["private_exact_value"])
    expected_attempts = int(corpus["expected_attempts"])
    started = time.monotonic()

    if modulus != int(corpus["p"]) * int(corpus["ell"]):
        raise AssertionError("corpus factorization mismatch")
    if modulus.bit_length() != n or bound != n * n:
        raise AssertionError("corpus size mismatch")
    if 2 * private_prime != modulus + 1:
        raise AssertionError("private-prime identity mismatch")
    if not bool(ZZ(private_prime).is_prime(proof=True)):
        raise AssertionError("private row is not prime")

    seen_residues: set[int] = set()
    seen_exact_values: set[int] = set()
    decoder = CompleteRootDecoder(modulus)
    attempt_hash = hashlib.sha256()
    retained_hash = hashlib.sha256()
    direct_event_hash = hashlib.sha256()
    direct_events: list[dict[str, object]] = []
    private_row_columns: list[int] = []
    private_column_index: int | None = None
    attempts = 0
    residue_duplicates = 0
    unique_units = 0
    exact_duplicates = 0
    unit_exact_values_removed = 0
    retained_columns = 0
    residue_screen_proper = 0
    endpoint_minus_proper = 0
    endpoint_plus_proper = 0

    def state(phase: str, completed_pairs: int, total_pairs: int, status: str) -> dict[str, object]:
        return {
            "status": status,
            "phase": phase,
            "completed_pairs": completed_pairs,
            "total_pairs": total_pairs,
            "N": modulus,
            "n": n,
            "B": bound,
            "attempts": attempts,
            "expected_attempts": expected_attempts,
            "unique_residues": len(seen_residues),
            "residue_duplicates": residue_duplicates,
            "unique_units": unique_units,
            "distinct_nonunit_exact_values": retained_columns,
            "exact_value_duplicates": exact_duplicates,
            "unit_exact_values_removed": unit_exact_values_removed,
            "direct_screens": {
                "residue_proper": residue_screen_proper,
                "endpoint_minus_proper": endpoint_minus_proper,
                "endpoint_plus_proper": endpoint_plus_proper,
                "proper_event_count": len(direct_events),
                "events": direct_events,
                "event_stream_sha256": direct_event_hash.hexdigest(),
            },
            "private_column": {
                "prime": private_prime,
                "exact_value": private_exact_value,
                "column_index": private_column_index,
                "odd_row_column_indices": private_row_columns,
                "observed_row_degree": len(private_row_columns),
            },
            "decoder": decoder.snapshot(retained_columns),
            "attempt_stream_sha256": attempt_hash.hexdigest(),
            "retained_exact_stream_sha256": retained_hash.hexdigest(),
            "factor_cache": {
                "hits": factor_integer.cache_info().hits,
                "misses": factor_integer.cache_info().misses,
                "current_size": factor_integer.cache_info().currsize,
                "maximum_size": factor_integer.cache_info().maxsize,
            },
            "peak_rss": peak_rss(),
            "elapsed_seconds": time.monotonic() - started,
        }

    def checkpoint(phase: str, completed_pairs: int, total_pairs: int) -> None:
        write_json(output_path, state(phase, completed_pairs, total_pairs, "RUNNING"))

    def record_direct(
        method: str,
        divisor: int,
        residue: int,
        inverse: int | None,
        provenance: dict[str, int | str],
    ) -> None:
        event = {
            "event_index": len(direct_events),
            "method": method,
            "factor": divisor,
            "cofactor": modulus // divisor,
            "residue": residue,
            "inverse": inverse,
            "provenance": provenance,
        }
        direct_events.append(event)
        direct_event_hash.update((json.dumps(event, sort_keys=True) + "\n").encode())

    def attempt(
        residue: int,
        kind: int,
        pair_index: int,
        left: int,
        right: int,
        exponent: int,
        orientation: int,
    ) -> None:
        nonlocal attempts, residue_duplicates, unique_units, exact_duplicates
        nonlocal unit_exact_values_removed, retained_columns, private_column_index
        nonlocal residue_screen_proper, endpoint_minus_proper, endpoint_plus_proper

        attempt_index = attempts
        attempts += 1
        attempt_hash.update(
            struct.pack(">BIQQIBQ", kind, pair_index, left, right, exponent, orientation, residue)
        )
        if residue in seen_residues:
            residue_duplicates += 1
            return
        seen_residues.add(residue)
        provenance: dict[str, int | str] = {
            "attempt_index_zero_based": attempt_index,
            "kind": ("seed", "frozen_seed_basis_pair", "nonadaptive_seed_pair")[kind],
            "pair_index_zero_based": pair_index,
            "u": left,
            "v": right,
            "exponent": exponent,
            "orientation": orientation,
        }

        common = math.gcd(residue, modulus)
        if common != 1:
            if not 1 < common < modulus:
                raise AssertionError("canonical residue is zero modulo N")
            residue_screen_proper += 1
            record_direct("direct_residue_gcd", common, residue, None, provenance)
            return

        unique_units += 1
        inverse = pow(residue, -1, modulus)
        minus = math.gcd(residue - inverse, modulus)
        if 1 < minus < modulus:
            endpoint_minus_proper += 1
            record_direct("direct_endpoint_minus", minus, residue, inverse, provenance)
        plus = math.gcd(residue + inverse, modulus)
        if 1 < plus < modulus:
            endpoint_plus_proper += 1
            record_direct("direct_endpoint_plus", plus, residue, inverse, provenance)

        exact_value = residue * inverse
        if exact_value == 1:
            unit_exact_values_removed += 1
            return
        if exact_value in seen_exact_values:
            exact_duplicates += 1
            return
        seen_exact_values.add(exact_value)

        factors = dict(factor_integer(residue))
        for prime, multiplicity in factor_integer(inverse):
            factors[prime] = factors.get(prime, 0) + multiplicity
        if math.prod(prime**multiplicity for prime, multiplicity in factors.items()) != exact_value:
            raise AssertionError("combined endpoint factors do not reconstruct exact value")

        column_index = retained_columns
        retained_columns += 1
        retained_hash.update(
            f"{column_index}:{residue}:{inverse}:{exact_value}\n".encode()
        )
        contains_private = exact_value == private_exact_value
        if contains_private:
            if private_column_index is not None:
                raise AssertionError("private exact value retained twice")
            private_column_index = column_index
        if factors.get(private_prime, 0) & 1:
            private_row_columns.append(column_index)
        decoder.add(factors, column_index, contains_private)

    for seed_index, seed in enumerate(range(2, n + 1)):
        attempt(seed, 0, seed_index, seed, 1, 0, 0)
    checkpoint("seeds_complete", n - 1, n - 1)

    frozen_pairs, basis_summary = frozen_seed_pairs(modulus, n)
    if len(frozen_pairs) != int(corpus["expected_frozen_pairs"]):
        raise AssertionError("frozen pair count mismatch")
    for pair_index, (left, right) in enumerate(frozen_pairs):
        left_power = 1
        right_power = 1
        for exponent in range(bound + 1):
            attempt(left_power * right % modulus, 1, pair_index, left, right, exponent, 0)
            attempt(left * right_power % modulus, 1, pair_index, left, right, exponent, 1)
            left_power = left_power * left % modulus
            right_power = right_power * right % modulus
        if pair_index % 5 == 0 or pair_index + 1 == len(frozen_pairs):
            checkpoint("frozen", pair_index + 1, len(frozen_pairs))

    menu_pair_count = (n - 1) * (n - 2) // 2
    if menu_pair_count != int(corpus["expected_menu_pairs"]):
        raise AssertionError("menu pair count mismatch")
    menu_index = 0
    for left in range(2, n):
        for right in range(left + 1, n + 1):
            left_power = 1
            right_power = 1
            for exponent in range(bound + 1):
                attempt(left_power * right % modulus, 2, menu_index, left, right, exponent, 0)
                attempt(left * right_power % modulus, 2, menu_index, left, right, exponent, 1)
                left_power = left_power * left % modulus
                right_power = right_power * right % modulus
            menu_index += 1
            if menu_index % 10 == 0 or menu_index == menu_pair_count:
                checkpoint("all_pairs", menu_index, menu_pair_count)

    if attempts != expected_attempts or menu_index != menu_pair_count:
        raise AssertionError("complete source attempt count mismatch")
    if private_column_index != 0:
        raise AssertionError("seed-2 exact value is not column zero")
    if private_row_columns != [private_column_index]:
        raise AssertionError("private row is not singleton in the exact matrix")
    final_decoder = decoder.snapshot(retained_columns)
    if not final_decoder["basis_count_matches_nullity"]:
        raise AssertionError("fundamental basis is incomplete")
    if not final_decoder["all_basis_dependencies_exclude_private"]:
        raise AssertionError("a dependency contains the universe-private column")

    final = state("complete", menu_pair_count, menu_pair_count, "COMPLETE")
    final["basis"] = basis_summary
    final["checks"] = {
        "source_complete": True,
        "global_residue_first_occurrence": True,
        "global_exact_value_first_occurrence": True,
        "positive_half_root_convention": True,
        "private_row_singleton": True,
        "all_dependencies_exclude_private": True,
        "factor_assisted_hidden_prime_rows": True,
    }
    decoder_result = final["decoder"]
    direct_count = final["direct_screens"]["proper_event_count"]
    root_factors = decoder_result["non_global_basis_roots"] > 0
    final["verdict"] = {
        "CLOSE": decoder_result["nullity"] > 0,
        "ROOT": root_factors,
        "direct_factor_present": direct_count > 0,
        "feedback_gate": "CLOSED" if direct_count > 0 or root_factors else "OPEN",
        "reason": (
            "direct screen or non-global complete-basis root already factors"
            if direct_count > 0 or root_factors
            else "no direct screen and zero normalized-root image"
        ),
    }
    write_json(output_path, final)
    print(
        json.dumps(
            {
                "status": final["status"],
                "attempts": attempts,
                "columns": retained_columns,
                "rank": decoder_result["rank"],
                "nullity": decoder_result["nullity"],
                "non_global_basis_roots": decoder_result["non_global_basis_roots"],
                "direct_events": direct_count,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
