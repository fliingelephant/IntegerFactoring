#!/usr/bin/env python3
"""Proof-blind, factor-free replay of RECONSTRUCTION_STATEMENT.md.

The arithmetic input is N alone.  This file deliberately does not import or
call a factorization or primality routine.  Its only integer-decomposition
operations are gcd splits and exact integer-root tests.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import signal
import sys
import time
from bisect import bisect_left, insort
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


N = 202_537_109
DIAGNOSTIC_PREFIX = 5_616


class HardTimeout(RuntimeError):
    pass


class TeeLogger:
    def __init__(self, path: Path):
        self.file = path.open("w", encoding="utf-8")

    def log(self, message: str) -> None:
        line = f"[{time.strftime('%Y-%m-%dT%H:%M:%S%z')}] {message}"
        print(line, flush=True)
        print(line, file=self.file, flush=True)

    def close(self) -> None:
        self.file.close()


@dataclass(frozen=True)
class Relation:
    c: int
    w: int
    value: int
    origin: str


class GcdBasis:
    """A refinement DAG whose active leaves are pairwise coprime."""

    def __init__(self) -> None:
        self.values: list[int] = []
        self.children: list[tuple[int, ...] | None] = []
        self.node_by_value: dict[int, int] = {}
        self.active_values: list[int] = []
        self.active_node_by_value: dict[int, int] = {}
        self.gcd_tests = 0

    def node(self, value: int) -> int:
        if value == 1:
            raise ValueError("1 is not a basis node")
        node = self.node_by_value.get(value)
        if node is None:
            node = len(self.values)
            self.node_by_value[value] = node
            self.values.append(value)
            self.children.append(None)
        return node

    def _activate(self, node: int) -> None:
        value = self.values[node]
        if value in self.active_node_by_value:
            return
        insort(self.active_values, value)
        self.active_node_by_value[value] = node

    def _deactivate(self, node: int) -> None:
        value = self.values[node]
        if value not in self.active_node_by_value:
            return
        index = bisect_left(self.active_values, value)
        if index == len(self.active_values) or self.active_values[index] != value:
            raise AssertionError("active-basis index mismatch")
        self.active_values.pop(index)
        del self.active_node_by_value[value]

    def _split(self, node: int, child_values: tuple[int, ...]) -> None:
        if self.children[node] is not None:
            raise AssertionError("attempted to split an internal node")
        if math.prod(child_values) != self.values[node]:
            raise AssertionError("inexact gcd-basis split")
        child_nodes = tuple(self.node(value) for value in child_values if value != 1)
        if any(self.values[child] >= self.values[node] for child in child_nodes):
            raise AssertionError("nondecreasing refinement edge")
        self._deactivate(node)
        self.children[node] = child_nodes

    def insert_value(self, value: int) -> int | None:
        if value == 1:
            return None
        node = self.node(value)
        self._insert_node(node)
        return node

    def _insert_node(self, node: int) -> None:
        children = self.children[node]
        if children is not None:
            for child in children:
                self._insert_node(child)
            return

        x = self.values[node]
        if x in self.active_node_by_value:
            return

        for b in tuple(self.active_values):
            self.gcd_tests += 1
            g = math.gcd(x, b)
            if g == 1:
                continue

            b_node = self.active_node_by_value[b]
            if g == x:
                self._split(b_node, (x, b // x))
                self._insert_node(node)
                self._insert_node(self.node(b // x))
                return
            if g == b:
                self._split(node, (b, x // b))
                self._insert_node(self.node(x // b))
                return

            self._split(b_node, (g, b // g))
            self._split(node, (g, x // g))
            self._insert_node(self.node(g))
            self._insert_node(self.node(b // g))
            self._insert_node(self.node(x // g))
            return

        self._activate(node)

    def normalize_perfect_powers(self) -> int:
        split_count = 0
        while True:
            changed = False
            for value in tuple(self.active_values):
                root, exponent = maximal_exact_root(value)
                if exponent == 1:
                    continue
                node = self.active_node_by_value[value]
                self._split(node, (root,) * exponent)
                self._insert_node(self.node(root))
                split_count += 1
                changed = True
                break
            if not changed:
                return split_count

    def exponent_counter(self, root_node: int | None) -> Counter[int]:
        if root_node is None:
            return Counter()

        @lru_cache(maxsize=None)
        def expand(node: int) -> tuple[tuple[int, int], ...]:
            children = self.children[node]
            if children is None:
                return ((node, 1),)
            counter: Counter[int] = Counter()
            for child in children:
                counter.update(dict(expand(child)))
            return tuple(sorted(counter.items()))

        return Counter(dict(expand(root_node)))

    def verify(self, original_values: list[int]) -> dict[str, int | bool]:
        prefix_product = 1
        for value in self.active_values:
            if math.gcd(prefix_product, value) != 1:
                raise AssertionError("final basis is not pairwise coprime")
            prefix_product *= value

        for value in set(original_values):
            if value == 1:
                continue
            counter = self.exponent_counter(self.node_by_value[value])
            reconstructed = math.prod(
                self.values[node] ** exponent for node, exponent in counter.items()
            )
            if reconstructed != value:
                raise AssertionError("endpoint reconstruction failed")

        return {
            "pairwise_coprime": True,
            "distinct_endpoints_reconstructed": len(set(original_values)),
            "gcd_tests": self.gcd_tests,
        }


def exact_kth_root(value: int, exponent: int) -> int | None:
    low = 1
    high = 1 << ((value.bit_length() + exponent - 1) // exponent)
    while low <= high:
        middle = (low + high) // 2
        power = middle**exponent
        if power == value:
            return middle
        if power < value:
            low = middle + 1
        else:
            high = middle - 1
    return None


def maximal_exact_root(value: int) -> tuple[int, int]:
    for exponent in range(value.bit_length(), 1, -1):
        root = exact_kth_root(value, exponent)
        if root is not None:
            return root, exponent
    return value, 1


def proper_gcd(value: int, modulus: int) -> tuple[bool, int]:
    divisor = math.gcd(value, modulus)
    return 1 < divisor < modulus, divisor


def sign_gcds(c: int, w: int, modulus: int) -> tuple[int, int, bool]:
    minus = math.gcd(abs(c - w), modulus)
    plus = math.gcd(c + w, modulus)
    return minus, plus, (1 < minus < modulus or 1 < plus < modulus)


def root_evidence(values: list[int], relation_indices: list[int], modulus: int) -> dict[str, int | str]:
    product = math.prod(values[index] for index in relation_indices)
    root = math.isqrt(product)
    if root * root != product:
        raise AssertionError("kernel vector product is not an exact square")
    minus = math.gcd(root - 1, modulus)
    plus = math.gcd(root + 1, modulus)
    return {
        "support": len(relation_indices),
        "root_mod_N": root % modulus,
        "gcd_minus": minus,
        "gcd_plus": plus,
        "exact_root_decimal_digits": len(str(root)),
        "exact_root_sha256": hashlib.sha256(str(root).encode()).hexdigest(),
    }


def bit_indices(bits: int) -> list[int]:
    indices: list[int] = []
    while bits:
        least = bits & -bits
        indices.append(least.bit_length() - 1)
        bits ^= least
    return indices


def kernel_basis_lowest_pivot(signatures: list[int]) -> tuple[int, list[int]]:
    pivots: dict[int, tuple[int, int]] = {}
    kernel: list[int] = []
    for column, original_signature in enumerate(signatures):
        signature = original_signature
        combination = 1 << column
        while signature:
            pivot = (signature & -signature).bit_length() - 1
            prior = pivots.get(pivot)
            if prior is None:
                pivots[pivot] = (signature, combination)
                break
            signature ^= prior[0]
            combination ^= prior[1]
        if signature == 0:
            kernel.append(combination)
    return len(pivots), kernel


def normalized_distinct_values(combination: int, relations: list[Relation]) -> list[int]:
    odd_values: set[int] = set()
    while combination:
        least = combination & -combination
        relation = relations[least.bit_length() - 1]
        if relation.value != 1:
            if relation.value in odd_values:
                odd_values.remove(relation.value)
            else:
                odd_values.add(relation.value)
        combination ^= least
    return sorted(odd_values)


def evidence_for_exact_values(values: list[int], modulus: int) -> dict[str, int | str]:
    product = math.prod(values)
    root = math.isqrt(product)
    if root * root != product:
        raise AssertionError("diagnostic dependency is not an exact square")
    return {
        "distinct_support": len(values),
        "root_mod_N": root % modulus,
        "gcd_minus": math.gcd(root - 1, modulus),
        "gcd_plus": math.gcd(root + 1, modulus),
        "exact_root_decimal_digits": len(str(root)),
        "exact_root_sha256": hashlib.sha256(str(root).encode()).hexdigest(),
    }


def useful(evidence: dict[str, int | str], modulus: int) -> bool:
    return any(1 < int(evidence[key]) < modulus for key in ("gcd_minus", "gcd_plus"))


def run_replay(logger: TeeLogger) -> dict[str, object]:
    started = time.monotonic()
    n = N.bit_length()
    bound = n * n
    logger.log(f"public input N={N}; n={n}; B={bound}")

    trial_proper: list[tuple[int, int]] = []
    for t in range(2, bound + 1):
        divisor = math.gcd(t, N)
        if 1 < divisor < N:
            trial_proper.append((t, divisor))
    logger.log(f"trial screen complete; proper hits={len(trial_proper)}")

    seed_relations: list[Relation] = []
    seed_sign_proper: list[dict[str, int]] = []
    seen_seed_presentations: set[tuple[int, int]] = set()
    for seed in range(2, n + 1):
        divisor = math.gcd(seed, N)
        if 1 < divisor < N:
            seed_sign_proper.append({"seed": seed, "gcd": divisor})
            continue
        inverse = pow(seed, -1, N)
        presentation = (seed, inverse)
        if presentation in seen_seed_presentations:
            continue
        minus, plus, is_proper = sign_gcds(seed, inverse, N)
        if is_proper:
            seed_sign_proper.append(
                {"seed": seed, "inverse": inverse, "gcd_minus": minus, "gcd_plus": plus}
            )
            continue
        seen_seed_presentations.add(presentation)
        seed_relations.append(Relation(seed, inverse, seed * inverse, f"seed:{seed}"))
    logger.log(
        f"seed stage complete; retained={len(seed_relations)}; proper sign hits={len(seed_sign_proper)}"
    )

    seed_basis = GcdBasis()
    seed_endpoints = [endpoint for relation in seed_relations for endpoint in (relation.c, relation.w)]
    seed_nodes = {value: seed_basis.insert_value(value) for value in seed_endpoints}
    seed_power_splits = seed_basis.normalize_perfect_powers()
    seed_verify = seed_basis.verify(seed_endpoints)
    for block in seed_basis.active_values:
        _, exponent = maximal_exact_root(block)
        if exponent != 1:
            raise AssertionError("seed basis contains a perfect power")

    seed_pairs: list[tuple[int, int]] = []
    seed_pair_details: list[dict[str, object]] = []
    for relation in seed_relations:
        exponents = seed_basis.exponent_counter(seed_nodes[relation.c])
        exponents.update(seed_basis.exponent_counter(seed_nodes[relation.w]))
        parity_support = [
            seed_basis.values[node]
            for node, exponent in exponents.items()
            if exponent & 1
        ]
        if not parity_support:
            continue
        # "Nonzero modulo two" is the column-eligibility condition.  The
        # subsequent unqualified "support" is the support of the full
        # exponent column, so blocks with positive even exponent remain
        # eligible as u or v.
        support = sorted(
            seed_basis.values[node] for node, exponent in exponents.items() if exponent
        )
        u = support[0]
        v = support[1] if len(support) > 1 else 1
        seed_pairs.append((u, v))
        seed_pair_details.append(
            {
                "seed": relation.c,
                "u": u,
                "v": v,
                "full_support_size": len(support),
                "parity_support_size": len(parity_support),
            }
        )
        if len(seed_pairs) == n:
            break
    logger.log(
        f"seed basis complete; blocks={len(seed_basis.active_values)}; "
        f"perfect-power splits={seed_power_splits}; trajectory pairs={len(seed_pairs)}"
    )

    # A seed presentation has already processed its oriented seed residue.
    processed_residues = {relation.c for relation in seed_relations}
    trajectory_relations: list[Relation] = []
    trajectory_sign_proper: list[dict[str, int]] = []
    for pair_ordinal, (u, v) in enumerate(seed_pairs, 1):
        u_power = 1
        v_power = 1
        for exponent in range(bound + 1):
            candidates = ((u_power * v) % N, (u * v_power) % N)
            for arm, c in enumerate(candidates, 1):
                if c in processed_residues:
                    continue
                processed_residues.add(c)
                inverse = pow(c, -1, N)
                minus, plus, is_proper = sign_gcds(c, inverse, N)
                if is_proper:
                    trajectory_sign_proper.append(
                        {
                            "pair": pair_ordinal,
                            "exponent": exponent,
                            "arm": arm,
                            "residue": c,
                            "gcd_minus": minus,
                            "gcd_plus": plus,
                        }
                    )
                    continue
                trajectory_relations.append(
                    Relation(c, inverse, c * inverse, f"trajectory:{pair_ordinal}:{exponent}:{arm}")
                )
            u_power = (u_power * u) % N
            v_power = (v_power * v) % N
        logger.log(
            f"trajectory pair {pair_ordinal}/{len(seed_pairs)} complete; "
            f"new retained total={len(trajectory_relations)}"
        )

    all_relations = seed_relations + trajectory_relations
    logger.log(
        f"trajectory stage complete; new={len(trajectory_relations)}; "
        f"all residues={len(all_relations)}; proper sign hits={len(trajectory_sign_proper)}"
    )

    decoder_relations: list[Relation] = []
    relation_by_value: dict[int, Relation] = {}
    removed_ones = 0
    removed_duplicates = 0
    for relation in all_relations:
        if relation.value == 1:
            removed_ones += 1
            continue
        if relation.value in relation_by_value:
            removed_duplicates += 1
            continue
        relation_by_value[relation.value] = relation
        decoder_relations.append(relation)
    logger.log(
        f"decoder dedup complete; columns={len(decoder_relations)}; "
        f"P=1 removed={removed_ones}; repeated values removed={removed_duplicates}"
    )

    joint_basis = GcdBasis()
    decoder_endpoints = [endpoint for relation in decoder_relations for endpoint in (relation.c, relation.w)]
    endpoint_nodes: dict[int, int | None] = {}
    for ordinal, endpoint in enumerate(decoder_endpoints, 1):
        endpoint_nodes[endpoint] = joint_basis.insert_value(endpoint)
        if ordinal % 2_000 == 0:
            logger.log(
                f"joint refinement endpoints={ordinal}/{len(decoder_endpoints)}; "
                f"active blocks={len(joint_basis.active_values)}"
            )
    joint_verify = joint_basis.verify(decoder_endpoints)
    square_blocks = [value for value in joint_basis.active_values if math.isqrt(value) ** 2 == value]
    nonsquare_blocks = [value for value in joint_basis.active_values if math.isqrt(value) ** 2 != value]
    row_by_node = {
        joint_basis.active_node_by_value[value]: row for row, value in enumerate(nonsquare_blocks)
    }

    @lru_cache(maxsize=None)
    def node_parity(node: int) -> int:
        children = joint_basis.children[node]
        if children is None:
            row = row_by_node.get(node)
            return 0 if row is None else 1 << row
        parity = 0
        for child in children:
            parity ^= node_parity(child)
        return parity

    signatures: list[int] = []
    for relation in decoder_relations:
        signatures.append(
            node_parity(endpoint_nodes[relation.c]) ^ node_parity(endpoint_nodes[relation.w])
        )
    logger.log(
        f"joint basis complete; blocks={len(joint_basis.active_values)}; "
        f"square blocks={len(square_blocks)}; nonsquare rows={len(nonsquare_blocks)}"
    )

    rank, kernel = kernel_basis_lowest_pivot(signatures)
    if len(kernel) != len(signatures) - rank:
        raise AssertionError("rank-nullity failed")
    decoder_values = [relation.value for relation in decoder_relations]
    useful_kernel_vectors: list[dict[str, int | str]] = []
    kernel_support_histogram: Counter[int] = Counter()
    for basis_ordinal, combination in enumerate(kernel, 1):
        indices = bit_indices(combination)
        evidence = root_evidence(decoder_values, indices, N)
        kernel_support_histogram[len(indices)] += 1
        if useful(evidence, N):
            evidence["basis_ordinal"] = basis_ordinal
            useful_kernel_vectors.append(evidence)
    logger.log(
        f"kernel complete; rank={rank}; dimension={len(kernel)}; "
        f"useful basis vectors={len(useful_kernel_vectors)}"
    )

    signature_by_value = {relation.value: signature for relation, signature in zip(decoder_relations, signatures)}
    diagnostic_relations = all_relations[:DIAGNOSTIC_PREFIX]
    diagnostic_signatures = [
        0 if relation.value == 1 else signature_by_value[relation.value]
        for relation in diagnostic_relations
    ]
    pivots: dict[int, tuple[int, int]] = {}
    first_useful: dict[str, int | str] | None = None
    dependent_count = 0
    for column, original_signature in enumerate(diagnostic_signatures):
        signature = original_signature
        combination = 1 << column
        while signature:
            pivot = (signature & -signature).bit_length() - 1
            prior = pivots.get(pivot)
            if prior is None:
                pivots[pivot] = (signature, combination)
                break
            signature ^= prior[0]
            combination ^= prior[1]
        if signature != 0:
            continue
        dependent_count += 1
        distinct_values = normalized_distinct_values(combination, diagnostic_relations)
        evidence = evidence_for_exact_values(distinct_values, N)
        if useful(evidence, N):
            evidence["ordinal"] = column + 1
            evidence["occurrence_support"] = combination.bit_count()
            first_useful = evidence
            break
    logger.log(
        f"online diagnostic complete; prefix={len(diagnostic_relations)}; "
        f"dependencies tested through first useful={dependent_count}; first={first_useful}"
    )

    distinct_diagnostic_values = sorted(
        {relation.value for relation in diagnostic_relations if relation.value != 1}
    )
    diagnostic_value_signatures = [signature_by_value[value] for value in distinct_diagnostic_values]
    indices_by_signature: dict[int, list[int]] = {}
    for index, signature in enumerate(diagnostic_value_signatures):
        indices_by_signature.setdefault(signature, []).append(index)

    small_support_candidates = Counter()
    small_support_useful = Counter()
    for index in indices_by_signature.get(0, []):
        evidence = evidence_for_exact_values([distinct_diagnostic_values[index]], N)
        small_support_candidates[1] += 1
        if useful(evidence, N):
            small_support_useful[1] += 1

    for group in indices_by_signature.values():
        for left_position, left in enumerate(group):
            for right in group[left_position + 1 :]:
                evidence = evidence_for_exact_values(
                    [distinct_diagnostic_values[left], distinct_diagnostic_values[right]], N
                )
                small_support_candidates[2] += 1
                if useful(evidence, N):
                    small_support_useful[2] += 1

    diagnostic_count = len(distinct_diagnostic_values)
    for left in range(diagnostic_count):
        left_signature = diagnostic_value_signatures[left]
        for middle in range(left + 1, diagnostic_count):
            target = left_signature ^ diagnostic_value_signatures[middle]
            for right in indices_by_signature.get(target, []):
                if right <= middle:
                    continue
                evidence = evidence_for_exact_values(
                    [
                        distinct_diagnostic_values[left],
                        distinct_diagnostic_values[middle],
                        distinct_diagnostic_values[right],
                    ],
                    N,
                )
                small_support_candidates[3] += 1
                if useful(evidence, N):
                    small_support_useful[3] += 1
    logger.log(
        f"small-support diagnostic complete; distinct values={diagnostic_count}; "
        f"candidates={dict(small_support_candidates)}; useful={dict(small_support_useful)}"
    )

    elapsed = time.monotonic() - started
    source_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "public_input": {"N": N, "n": n, "B": bound},
        "source_sha256": source_sha256,
        "elapsed_seconds": elapsed,
        "trial_screen": {"proper_hits": trial_proper},
        "seeds": {
            "retained": len(seed_relations),
            "proper_sign_hits": seed_sign_proper,
            "basis_blocks": len(seed_basis.active_values),
            "basis_values": seed_basis.active_values,
            "perfect_power_splits": seed_power_splits,
            "basis_verification": seed_verify,
            "pairs": seed_pair_details,
        },
        "trajectories": {
            "new_first_occurrence_relations": len(trajectory_relations),
            "processed_residue_count_including_seeds": len(processed_residues),
            "proper_sign_hits": trajectory_sign_proper,
        },
        "all_relations": len(all_relations),
        "decoder": {
            "P_equals_1_removed": removed_ones,
            "repeated_exact_values_removed": removed_duplicates,
            "distinct_nonzero_columns": len(decoder_relations),
            "joint_basis_blocks": len(joint_basis.active_values),
            "square_blocks_omitted": len(square_blocks),
            "nonsquare_rows": len(nonsquare_blocks),
            "basis_verification": joint_verify,
            "rank": rank,
            "kernel_dimension": len(kernel),
            "kernel_basis_policy": "seed/trajectory column order; lowest numbered nonzero row pivot",
            "kernel_support_histogram": dict(sorted(kernel_support_histogram.items())),
            "useful_kernel_vectors": useful_kernel_vectors,
        },
        "diagnostic": {
            "requested_prefix": DIAGNOSTIC_PREFIX,
            "actual_prefix": len(diagnostic_relations),
            "online_policy": "lowest numbered nonzero row pivot",
            "dependent_columns_tested_through_first_useful": dependent_count,
            "first_useful": first_useful,
            "distinct_exact_values": diagnostic_count,
            "small_support_square_dependencies": {
                "support_1": small_support_candidates[1],
                "support_2": small_support_candidates[2],
                "support_3": small_support_candidates[3],
            },
            "small_support_useful_dependencies": {
                "support_1": small_support_useful[1],
                "support_2": small_support_useful[2],
                "support_3": small_support_useful[3],
            },
        },
    }


def validate_claim(result: dict[str, object]) -> list[str]:
    failures: list[str] = []

    def expect(label: str, actual: object, expected: object) -> None:
        if actual != expected:
            failures.append(f"{label}: expected {expected!r}, got {actual!r}")

    public_input = result["public_input"]
    seeds = result["seeds"]
    trajectories = result["trajectories"]
    decoder = result["decoder"]
    diagnostic = result["diagnostic"]
    assert isinstance(public_input, dict)
    assert isinstance(seeds, dict)
    assert isinstance(trajectories, dict)
    assert isinstance(decoder, dict)
    assert isinstance(diagnostic, dict)

    expect("n", public_input["n"], 28)
    expect("B", public_input["B"], 784)
    expect("trial proper hits", result["trial_screen"], {"proper_hits": []})
    expect("seed relations", seeds["retained"], 27)
    expect("seed sign hits", seeds["proper_sign_hits"], [])
    expect("trajectory relations", trajectories["new_first_occurrence_relations"], 12_522)
    expect("trajectory sign hits", trajectories["proper_sign_hits"], [])
    expect("all relations", result["all_relations"], 12_549)
    expect("removed P=1", decoder["P_equals_1_removed"], 1)
    expect("removed repeated P", decoder["repeated_exact_values_removed"], 3_134)
    expect("decoder columns", decoder["distinct_nonzero_columns"], 9_414)
    expect("nonsquare rows", decoder["nonsquare_rows"], 11_015)
    expect("rank", decoder["rank"], 8_926)
    expect("kernel dimension", decoder["kernel_dimension"], 488)

    useful_vectors = decoder["useful_kernel_vectors"]
    assert isinstance(useful_vectors, list)
    matching_main = [
        vector
        for vector in useful_vectors
        if vector["support"] == 166
        and vector["root_mod_N"] == 132_013_085
        and vector["gcd_minus"] == 19_727
        and vector["gcd_plus"] == 10_267
    ]
    if not matching_main:
        failures.append("no kernel-basis vector matches the declared 166-value main witness")

    first_useful = diagnostic["first_useful"]
    expected_diagnostic = {
        "ordinal": 5_616,
        "distinct_support": 166,
        "root_mod_N": 70_524_024,
        "gcd_minus": 10_267,
        "gcd_plus": 19_727,
    }
    if not isinstance(first_useful, dict):
        failures.append("online diagnostic found no useful dependency")
    else:
        for key, expected in expected_diagnostic.items():
            expect(f"diagnostic {key}", first_useful.get(key), expected)

    expect(
        "small-support useful dependencies",
        diagnostic["small_support_useful_dependencies"],
        {"support_1": 0, "support_2": 0, "support_3": 0},
    )
    return failures


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--timeout-seconds", type=int, default=1_800)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = TeeLogger(args.log)

    def timeout_handler(_signum: int, _frame: object) -> None:
        raise HardTimeout(f"hard timeout after {args.timeout_seconds} seconds")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, args.timeout_seconds)
    try:
        result = run_replay(logger)
        failures = validate_claim(result)
        result["claim_failures"] = failures
        result["status"] = "PASS" if not failures else "FAIL"
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        logger.log(f"strict result={result['status']}; failures={len(failures)}")
        for failure in failures:
            logger.log(f"FAIL: {failure}")
        return 0 if not failures else 1
    except HardTimeout as error:
        logger.log(f"FAIL: {error}")
        return 124
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        logger.close()


if __name__ == "__main__":
    sys.exit(main())
