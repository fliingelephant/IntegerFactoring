#!/usr/bin/env python3
"""Memory-bounded factor-assisted discovery for the first F116 case."""

from __future__ import annotations

import argparse
from array import array
from collections import Counter
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time

from sage.all import ZZ


ROOT = Path(__file__).resolve().parents[2]
F115_SOURCE = ROOT / "experiments/F115_all_pairs_global_corpus_audit/audit_independent_verifier.py"
EXPECTED_F115_SHA256 = "bfca59151b428d41631ee445892a42b77d35bd41e468cea111cbd97a97e9626a"
P = 80_000_059
Q = 159_999_943
N = 12_800_004_879_996_637


class SparseDagDecoder:
    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.pivots: dict[int, tuple[frozenset[int], int, int]] = {}
        self.left = array("q")
        self.right = array("q")
        self.dependencies = 0
        self.global_dependencies = 0
        self.eliminations = 0
        self.maximum_reduced_support = 0

    def add(self, factors: dict[int, int], relation_index: int) -> dict[str, object] | None:
        parity = {prime for prime, exponent in factors.items() if exponent & 1}
        half_root = 1
        for prime, exponent in factors.items():
            half_root = half_root * pow(prime, exponent // 2, self.modulus) % self.modulus
        expression = -relation_index - 1
        self.maximum_reduced_support = max(self.maximum_reduced_support, len(parity))
        while parity:
            pivot = max(parity)
            known = self.pivots.get(pivot)
            if known is None:
                self.pivots[pivot] = (frozenset(parity), expression, half_root)
                return None
            known_parity, known_expression, known_half_root = known
            common = parity.intersection(known_parity)
            half_root = half_root * known_half_root % self.modulus
            for prime in common:
                half_root = half_root * prime % self.modulus
            parity.symmetric_difference_update(known_parity)
            self.left.append(expression)
            self.right.append(known_expression)
            expression = len(self.left) - 1
            self.eliminations += 1
            self.maximum_reduced_support = max(self.maximum_reduced_support, len(parity))

        self.dependencies += 1
        if half_root in (1, self.modulus - 1):
            self.global_dependencies += 1
            return None
        minus = math.gcd(half_root - 1, self.modulus)
        plus = math.gcd(half_root + 1, self.modulus)
        if not (1 < minus < self.modulus or 1 < plus < self.modulus):
            raise AssertionError("non-global dependency did not expose a factor")

        active_nodes = bytearray(len(self.left))
        support: set[int] = set()

        def toggle(reference: int) -> None:
            if reference < 0:
                column = -reference - 1
                if column in support:
                    support.remove(column)
                else:
                    support.add(column)
            else:
                active_nodes[reference] ^= 1

        toggle(expression)
        for node in range(len(self.left) - 1, -1, -1):
            if active_nodes[node]:
                toggle(self.left[node])
                toggle(self.right[node])
        return {
            "root_mod_N": half_root,
            "gcd_root_minus_one_N": minus,
            "gcd_root_plus_one_N": plus,
            "support_indices_zero_based": sorted(support),
        }


def factor_integer(value: int) -> dict[int, int]:
    factors = {int(prime): int(exponent) for prime, exponent in ZZ(value).factor()}
    if math.prod(prime**exponent for prime, exponent in factors.items()) != value:
        raise AssertionError("Sage factorization does not reconstruct endpoint")
    return factors


def merge_factors(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    result = left.copy()
    for prime, exponent in right.items():
        result[prime] = result.get(prime, 0) + exponent
    return result


def write_output(path: Path, value: dict[str, object]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    source_hash = hashlib.sha256(F115_SOURCE.read_bytes()).hexdigest()
    assert source_hash == EXPECTED_F115_SHA256
    spec = importlib.util.spec_from_file_location("f116_sparse_pinned_f115", F115_SOURCE)
    assert spec is not None and spec.loader is not None
    f115 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f115)

    assert P * Q == N and bool(ZZ(P).is_prime()) and bool(ZZ(Q).is_prime())
    n = N.bit_length()
    bound = n * n
    assert n == 54 and P > bound and Q > bound
    decoder = SparseDagDecoder(N)
    seen: set[int] = set()
    attempted = 0
    repeated = 0
    retained = 0
    direct_witness = None
    seed_records = []

    def retain(residue: int) -> dict[str, object] | None:
        nonlocal attempted, repeated, retained, direct_witness
        attempted += 1
        if residue in seen:
            repeated += 1
            return None
        seen.add(residue)
        inverse = pow(residue, -1, N)
        for sign, difference in (("minus", residue - inverse), ("plus", residue + inverse)):
            divisor = math.gcd(difference, N)
            if 1 < divisor < N:
                direct_witness = {
                    "source_index_zero_based": retained,
                    "c": residue,
                    "w": inverse,
                    "sign": sign,
                    "gcd": divisor,
                }
                return direct_witness
        c_factors = factor_integer(residue)
        w_factors = factor_integer(inverse)
        result = decoder.add(merge_factors(c_factors, w_factors), retained)
        retained += 1
        return result

    for seed in range(2, n + 1):
        before = retained
        result = retain(seed)
        assert result is None and retained == before + 1
        seed_records.append((factor_integer(seed), factor_integer(pow(seed, -1, N))))
    supports = f115.public_supports(seed_records)
    frozen_pairs = [
        (support[0], 1) if len(support) == 1 else (support[0], support[1])
        for support in supports
    ]
    for u, v in frozen_pairs:
        for exponent in range(bound + 1):
            assert retain(pow(u, exponent, N) * v % N) is None
            assert retain(u * pow(v, exponent, N) % N) is None
    frozen_summary = {
        "retained_relations": retained,
        "dependencies": decoder.dependencies,
        "global_dependencies": decoder.global_dependencies,
        "all_dependencies_global": decoder.dependencies == decoder.global_dependencies,
        "pair_count": len(frozen_pairs),
        "pairs": [list(pair) for pair in frozen_pairs],
        "attempted_residues": attempted,
        "duplicate_residues": repeated,
    }
    assert frozen_summary["all_dependencies_global"]
    write_output(
        args.output,
        {
            "status": "RUNNING_AFTER_FROZEN",
            "case": {"p": P, "q": Q, "N": N, "n": n, "bound": bound},
            "frozen": frozen_summary,
            "decoder": {
                "pivot_count": len(decoder.pivots),
                "dag_node_count": len(decoder.left),
                "eliminations": decoder.eliminations,
            },
            "elapsed_seconds": time.monotonic() - started,
        },
    )

    witness = None
    successful_pair = None
    menu_attempted = 0
    for u in range(2, n + 1):
        for v in range(u + 1, n + 1):
            menu_attempted += 1
            for exponent in range(bound + 1):
                witness = retain(pow(u, exponent, N) * v % N)
                if witness is None:
                    witness = retain(u * pow(v, exponent, N) % N)
                if witness is not None:
                    successful_pair = (u, v)
                    break
            if witness is not None:
                break
        if witness is not None:
            break
    assert witness is not None and direct_witness is None and successful_pair is not None
    support = list(witness["support_indices_zero_based"])
    selection_summary = {
        "status": "RUNNING_FACTOR_FREE_SUPPORT_REPLAY",
        "case": {"ordinal": 3, "p": P, "q": Q, "N": N, "n": n, "bound": bound},
        "frozen": frozen_summary,
        "menu": {
            "total_pairs": (n - 1) * (n - 2) // 2,
            "attempted_pairs": menu_attempted,
            "successful_pair": list(successful_pair),
        },
        "source_at_stop": {
            "retained_relations": retained,
            "attempted_residues": attempted,
            "duplicate_residues": repeated,
        },
        "decoder": {
            "pivot_count": len(decoder.pivots),
            "dag_node_count": len(decoder.left),
            "eliminations": decoder.eliminations,
            "maximum_reduced_parity_support": decoder.maximum_reduced_support,
            "dependencies": decoder.dependencies,
            "global_dependencies": decoder.global_dependencies,
        },
        "factor_assisted_witness": witness,
        "elapsed_seconds": time.monotonic() - started,
    }
    write_output(args.output, selection_summary)

    del decoder, seen, seed_records
    gc.collect()
    support_set = set(support)
    replay_seen: set[int] = set()
    replay_retained = 0
    exact_product = 1
    provenance_counts: Counter[str] = Counter()
    appended_pairs: set[tuple[int, int]] = set()

    def replay(residue: int, kind: str, pair: tuple[int, int] | None) -> bool:
        nonlocal replay_retained, exact_product
        if residue in replay_seen:
            return False
        replay_seen.add(residue)
        inverse = pow(residue, -1, N)
        if replay_retained in support_set:
            exact_product *= residue * inverse
            provenance_counts[kind] += 1
            if kind == "nonadaptive_seed_pair" and pair is not None:
                appended_pairs.add(pair)
        replay_retained += 1
        return replay_retained == retained

    reached = False
    for seed in range(2, n + 1):
        reached = replay(seed, "initial_seed", None)
        if reached:
            break
    if not reached:
        for u, v in frozen_pairs:
            for exponent in range(bound + 1):
                reached = replay(pow(u, exponent, N) * v % N, "frozen_seed_basis_pair", (u, v))
                if not reached:
                    reached = replay(u * pow(v, exponent, N) % N, "frozen_seed_basis_pair", (u, v))
                if reached:
                    break
            if reached:
                break
    if not reached:
        for u in range(2, n + 1):
            for v in range(u + 1, n + 1):
                for exponent in range(bound + 1):
                    reached = replay(pow(u, exponent, N) * v % N, "nonadaptive_seed_pair", (u, v))
                    if not reached:
                        reached = replay(u * pow(v, exponent, N) % N, "nonadaptive_seed_pair", (u, v))
                    if reached:
                        break
                if reached:
                    break
            if reached:
                break
    assert reached and replay_retained == retained
    root = math.isqrt(exact_product)
    assert root * root == exact_product
    root_residue = root % N
    gcds = [math.gcd(root_residue - 1, N), math.gcd(root_residue + 1, N)]
    assert root_residue == int(witness["root_mod_N"])
    assert gcds == [int(witness["gcd_root_minus_one_N"]), int(witness["gcd_root_plus_one_N"])]
    product_bytes = exact_product.to_bytes((exact_product.bit_length() + 7) // 8, "big")
    root_bytes = root.to_bytes((root.bit_length() + 7) // 8, "big")
    output = {
        **selection_summary,
        "status": "PASS",
        "role": "factor-assisted discovery with exact factor-free support replay; proof-blind replay required",
        "pinned_source": {str(F115_SOURCE.relative_to(ROOT)): source_hash},
        "factor_free_support_replay": {
            "support_size": len(support),
            "source_indices_zero_based": support,
            "source_indices_sha256": hashlib.sha256(
                json.dumps(support, separators=(",", ":")).encode()
            ).hexdigest(),
            "provenance_kind_counts": dict(sorted(provenance_counts.items())),
            "distinct_appended_pairs": len(appended_pairs),
            "exact_product_bit_length": exact_product.bit_length(),
            "exact_product_unsigned_big_endian_sha256": hashlib.sha256(product_bytes).hexdigest(),
            "positive_root_bit_length": root.bit_length(),
            "positive_root_unsigned_big_endian_sha256": hashlib.sha256(root_bytes).hexdigest(),
            "root_mod_N": root_residue,
            "gcd_root_minus_one_N": gcds[0],
            "gcd_root_plus_one_N": gcds[1],
        },
        "elapsed_seconds": time.monotonic() - started,
    }
    write_output(args.output, output)
    print(json.dumps({"status": "PASS", "elapsed_seconds": output["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
