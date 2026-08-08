#!/usr/bin/env python3
"""Independent Sage-backed hostile verifier for F109.

This executable does not import either F109 implementation code or the pinned
F98 factor-assisted implementation.  Sage/Pari supplies endpoint
factorization.  The queue, gcd-free block grouping, GF(2) elimination, root
tests, and isolated controls are reimplemented here.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import time

from sage.all import ZZ
from sage.env import SAGE_VERSION


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
F98_SOURCE = ROOT / "experiments/F98_multiseed_presentation_closure_kill/search_factor_assisted.py"
CANDIDATE_OUTPUT = HERE / "OUTPUT.json"
CASES = [
    (41011, 79043, (2, 13)),
    (80107, 159899, (3, 5)),
    (80363, 159631, (2, 7)),
    (80687, 159319, (2, 7)),
    (80779, 159199, (2, 13)),
    (80803, 159179, (2, 5)),
    (320107, 639839, (2, 13)),
]
CANDIDATE_PINS = {
    "DESIGN.md": "1780f158b0a0b53812b12cbca39eddfc3038f28e1b320b88e82f900c76f85ae4",
    "FAILED_RUNS.md": "aaaa7d3f21ff245d7dfcaa0fa79baa2ed7ba1344c9baf5df96b9af7648f09ab2",
    "OUTPUT.json": "ce23482d464dee551f3b585dedd803d3af24753592c4b639f5ee796b05d9e356",
    "RESULT.md": "e19e656156fbd170ccdc1209516d513abdc486b27df52bdfe023303f64c82d7b",
    "RUN.log": "4432bcf455c6f74d018452cdc56255095c47481253bc5bac458c5c64c262aa9d",
    "RUN_FAILED_R01_ASSERTED_ISOLATED_SUCCESS.log": "f0e9d8281b1b07f97d9e2d005f9959461bcbff4f6822b5c20cbc2fbd6c44f0c6",
    "RUN_MANIFEST.md": "76e3fc6d6a25d89b7ad67825a5ade79a2a7c05702603d972ef0d5beb6984b08b",
    "run_with_timeout.py": "05749e3626f600edeac67c6fe50e69dfe3a2a41792a9a2d0f7043bbe48041fb5",
    "test_recursive_rescue.py": "a223723f2bfef64a97ff7a14532627927d11870e9965b40a96b05c89f27b612e",
}
F98_PIN = "cbf50afc19a387ee58dffa9b0cca9a4ac2e732265c1b841cb535907cce364479"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class FactorCache:
    def __init__(self) -> None:
        self.values: dict[int, dict[int, int]] = {1: {}}

    def __call__(self, value: int) -> dict[int, int]:
        result = self.values.get(value)
        if result is None:
            result = {int(prime): int(exponent) for prime, exponent in ZZ(value).factor()}
            assert math.prod(prime**exponent for prime, exponent in result.items()) == value
            self.values[value] = result
        return result


class ParityDecoder:
    """Incremental column elimination with an explicit dependency basis."""

    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.prime_rows: dict[int, int] = {}
        self.pivots: dict[int, tuple[int, int]] = {}
        self.factors: list[dict[int, int]] = []
        self.provenance: list[dict[str, object]] = []
        self.dependencies = 0
        self.roots = Counter()
        self.factor: int | None = None
        self.factor_support: list[int] | None = None
        self.factor_root: int | None = None
        self.factor_gcds: tuple[int, int] | None = None

    def add(self, factors: dict[int, int], provenance: dict[str, object]) -> None:
        parity = 0
        for prime, exponent in sorted(factors.items()):
            row = self.prime_rows.setdefault(prime, len(self.prime_rows))
            if exponent & 1:
                parity ^= 1 << row

        relation = len(self.factors)
        self.factors.append(factors)
        self.provenance.append(provenance)
        combination = 1 << relation
        reduced = parity
        while reduced:
            pivot = reduced.bit_length() - 1
            known = self.pivots.get(pivot)
            if known is None:
                self.pivots[pivot] = (reduced, combination)
                return
            reduced ^= known[0]
            combination ^= known[1]

        self.dependencies += 1
        exponents: dict[int, int] = {}
        support: list[int] = []
        remaining = combination
        while remaining:
            bit = remaining & -remaining
            index = bit.bit_length() - 1
            support.append(index)
            for prime, exponent in self.factors[index].items():
                exponents[prime] = exponents.get(prime, 0) + exponent
            remaining ^= bit

        root = 1
        for prime, exponent in exponents.items():
            assert exponent % 2 == 0
            root = root * pow(prime, exponent // 2, self.modulus) % self.modulus
        minus = math.gcd(root - 1, self.modulus)
        plus = math.gcd(root + 1, self.modulus)
        if root == 1:
            self.roots["plus_one"] += 1
        elif root == self.modulus - 1:
            self.roots["minus_one"] += 1
        elif 1 < minus < self.modulus or 1 < plus < self.modulus:
            self.roots["non_global"] += 1
            self.factor = minus if 1 < minus < self.modulus else plus
            self.factor_support = support
            self.factor_root = root
            self.factor_gcds = (minus, plus)
        else:
            raise AssertionError("a square dependency gave neither a global root nor a factor")

    def certificate(self) -> dict[str, object]:
        rank = len(self.pivots)
        assert rank + self.dependencies == len(self.factors)
        return {
            "columns": len(self.factors),
            "rank": rank,
            "kernel_dimension": self.dependencies,
            "basis_roots": {
                "plus_one": self.roots["plus_one"],
                "minus_one": self.roots["minus_one"],
                "non_global": self.roots["non_global"],
            },
        }


def factor_relation(cache: FactorCache, c: int, w: int) -> tuple[dict[int, int], dict[int, int], dict[int, int]]:
    c_factors = cache(c)
    w_factors = cache(w)
    relation_factors = dict(c_factors)
    for prime, exponent in w_factors.items():
        relation_factors[prime] = relation_factors.get(prime, 0) + exponent
    return c_factors, w_factors, relation_factors


def public_supports(records: list[dict[str, object]]) -> list[list[int]]:
    """Reconstruct the finest primitive endpoint-signature blocks."""
    signatures: dict[int, list[tuple[int, int]]] = {}
    for relation, record in enumerate(records):
        for side, factors in enumerate((record["c_factors"], record["w_factors"])):
            endpoint = 2 * relation + side
            for prime, exponent in factors.items():
                signatures.setdefault(prime, []).append((endpoint, exponent))

    groups: dict[tuple[tuple[int, int], ...], list[tuple[int, int]]] = {}
    for prime, signature in signatures.items():
        content = math.gcd(*(exponent for _, exponent in signature))
        primitive = tuple((endpoint, exponent // content) for endpoint, exponent in signature)
        groups.setdefault(primitive, []).append((prime, content))

    blocks: list[tuple[int, set[int]]] = []
    for primitive, prime_contents in groups.items():
        common_content = math.gcd(*(content for _, content in prime_contents))
        block = math.prod(prime ** (content // common_content) for prime, content in prime_contents)
        blocks.append((block, {endpoint // 2 for endpoint, _ in primitive}))
    blocks.sort(key=lambda item: item[0])

    supports: list[list[int]] = [[] for _ in records]
    for block, relations in blocks:
        for relation in relations:
            supports[relation].append(block)
    return supports


def row_rank(records: list[dict[str, object]]) -> tuple[int, int]:
    masks: dict[int, int] = {}
    for column, record in enumerate(records):
        for prime, exponent in record["relation_factors"].items():
            if exponent & 1:
                masks[prime] = masks.get(prime, 0) ^ (1 << column)
    distinct = {mask for mask in masks.values() if mask}
    pivots: dict[int, int] = {}
    for original in distinct:
        value = original
        while value:
            pivot = value.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = value
                break
            value ^= known
    return len(pivots), len(distinct)


def first_round_certificate(modulus: int, records: list[dict[str, object]]) -> dict[str, object]:
    unique: list[dict[str, object]] = []
    seen_products: set[int] = set()
    zeros = 0
    duplicates = 0
    for record in records:
        product = int(record["P"])
        if product == 1:
            zeros += 1
        elif product in seen_products:
            duplicates += 1
        else:
            seen_products.add(product)
            unique.append(record)

    decoder = ParityDecoder(modulus)
    for record in unique:
        decoder.add(record["relation_factors"], record["provenance"])
        assert decoder.factor is None
    rank, distinct_rows = row_rank(unique)
    certificate = decoder.certificate()
    assert rank == certificate["rank"]
    certificate.update(
        {
            "raw_relations": len(records),
            "zero_products": zeros,
            "duplicate_products": duplicates,
            "unique_products": len(unique),
            "distinct_nonzero_prime_masks": distinct_rows,
        }
    )
    return certificate


def run_recursive(modulus: int, cache: FactorCache) -> dict[str, object]:
    n = modulus.bit_length()
    bound = n * n
    assert all(math.gcd(trial, modulus) == 1 for trial in range(2, bound + 1))
    decoder = ParityDecoder(modulus)
    records: list[dict[str, object]] = []
    seen: set[int] = set()
    first_round: dict[str, object] | None = None
    completed_rounds: list[dict[str, object]] = []
    processed_pairs: list[tuple[int, int]] = []

    def retain(c: int, provenance: dict[str, object]) -> dict[str, object] | None:
        if c in seen:
            return None
        seen.add(c)
        w = pow(c, -1, modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, modulus)
            if 1 < divisor < modulus:
                return {
                    "kind": "direct",
                    "factor": divisor,
                    "method": f"direct_endpoint_{sign}",
                    "c": c,
                    "w": w,
                    "provenance": provenance,
                }
        c_factors, w_factors, relation_factors = factor_relation(cache, c, w)
        decoder.add(relation_factors, provenance)
        records.append(
            {
                "c": c,
                "w": w,
                "P": c * w,
                "c_factors": c_factors,
                "w_factors": w_factors,
                "relation_factors": relation_factors,
                "provenance": provenance,
                "expanded": False,
                "nonzero": any(exponent & 1 for exponent in relation_factors.values()),
            }
        )
        if decoder.factor is not None:
            return {"kind": "dependency", "factor": decoder.factor, "method": "retained_parity_dependency"}
        return None

    for seed in range(2, n + 1):
        assert retain(seed, {"kind": "initial_seed", "seed": seed}) is None

    for round_index in range(1, n + 1):
        supports = public_supports(records)
        active: list[tuple[int, dict[str, object]]] = []
        for relation, record in enumerate(records):
            if not record["expanded"] and record["nonzero"]:
                record["expanded"] = True
                active.append((relation, record))
                if len(active) == n:
                    break
        assert active

        round_start_relations = len(records)
        round_start_dependencies = decoder.dependencies
        pair_rows: list[dict[str, object]] = []
        for relation, record in active:
            support = supports[relation]
            assert support
            pair = (support[0], 1) if len(support) == 1 else (support[0], support[1])
            prior_pair_count = processed_pairs.count(pair)
            processed_pairs.append(pair)
            pair_start_relations = len(records)
            pair_start_dependencies = decoder.dependencies
            pair_repeats = 0
            attempted = 0
            for exponent in range(bound + 1):
                for orientation, c in (
                    ("u_power_times_v", pow(pair[0], exponent, modulus) * pair[1] % modulus),
                    ("u_times_v_power", pair[0] * pow(pair[1], exponent, modulus) % modulus),
                ):
                    attempted += 1
                    before_seen = len(seen)
                    result = retain(
                        c,
                        {
                            "kind": "feedback_trajectory",
                            "round": round_index,
                            "active_relation_index_zero_based": relation,
                            "u": pair[0],
                            "v": pair[1],
                            "exponent": exponent,
                            "orientation": orientation,
                        },
                    )
                    pair_repeats += len(seen) == before_seen
                    if result is None:
                        continue

                    pair_row = {
                        "pair": list(pair),
                        "active_relation_index_zero_based": relation,
                        "active_relation_provenance": record["provenance"],
                        "prior_processed_pair_occurrences": prior_pair_count,
                        "attempted_candidates": attempted,
                        "repeated_candidates": pair_repeats,
                        "new_relations": len(records) - pair_start_relations,
                        "new_dependencies": decoder.dependencies - pair_start_dependencies,
                    }
                    pair_rows.append(pair_row)
                    success: dict[str, object] = {
                        "kind": result["kind"],
                        "c": result.get("c", c),
                        "w": result.get("w", pow(c, -1, modulus)),
                        "provenance": result.get("provenance", records[-1]["provenance"]),
                    }
                    if result["kind"] == "dependency":
                        assert decoder.factor_support is not None and decoder.factor_gcds is not None
                        source_counts = Counter()
                        pair_counts = Counter()
                        support_residues = []
                        for index in decoder.factor_support:
                            provenance = decoder.provenance[index]
                            if provenance["kind"] == "initial_seed":
                                source_counts["initial_seed"] += 1
                            else:
                                source_counts[f"feedback_round_{provenance['round']}"] += 1
                                pair_counts[f"{provenance['u']},{provenance['v']}"] += 1
                            support_residues.append(records[index]["c"])
                        success.update(
                            {
                                "dependency_support": len(decoder.factor_support),
                                "dependency_relation_indices_zero_based": decoder.factor_support,
                                "root_mod_N": decoder.factor_root,
                                "gcd_root_minus_one_N": decoder.factor_gcds[0],
                                "gcd_root_plus_one_N": decoder.factor_gcds[1],
                                "support_source_counts": dict(sorted(source_counts.items())),
                                "support_pair_counts": dict(sorted(pair_counts.items())),
                                "support_residues": support_residues,
                            }
                        )
                    else:
                        success["gcd"] = result["factor"]

                    return {
                        "status": "feedback_factor",
                        "factor": result["factor"],
                        "factor_method": result["method"],
                        "factor_dependency_size": len(decoder.factor_support or []),
                        "round": round_index,
                        "relations": len(records),
                        "dependencies": decoder.dependencies,
                        "global_dependencies": decoder.roots["plus_one"] + decoder.roots["minus_one"],
                        "trigger_pair": list(pair),
                        "trigger_pair_members_are_initial_seed_values": all(2 <= value <= n for value in pair),
                        "first_round": first_round,
                        "completed_rounds": completed_rounds,
                        "success_round_processed_pairs": pair_rows,
                        "all_processed_pair_count": len(processed_pairs),
                        "distinct_processed_pair_count": len(set(processed_pairs)),
                        "success": success,
                    }

            pair_rows.append(
                {
                    "pair": list(pair),
                    "active_relation_index_zero_based": relation,
                    "active_relation_provenance": record["provenance"],
                    "prior_processed_pair_occurrences": prior_pair_count,
                    "attempted_candidates": attempted,
                    "repeated_candidates": pair_repeats,
                    "new_relations": len(records) - pair_start_relations,
                    "new_dependencies": decoder.dependencies - pair_start_dependencies,
                }
            )

        if round_index == 1:
            first_round = first_round_certificate(modulus, records)
        completed_rounds.append(
            {
                "round": round_index,
                "active": len(active),
                "new_relations": len(records) - round_start_relations,
                "new_dependencies": decoder.dependencies - round_start_dependencies,
                "pair_sequence": [row["pair"] for row in pair_rows],
                "distinct_pairs": len({tuple(row["pair"]) for row in pair_rows}),
                "zero_new_relation_pairs": sum(row["new_relations"] == 0 for row in pair_rows),
                "repeated_pair_occurrences": sum(row["prior_processed_pair_occurrences"] > 0 for row in pair_rows),
            }
        )

    raise AssertionError("the declared recursive run reached its round cap")


def run_isolated(modulus: int, pair: tuple[int, int], cache: FactorCache) -> tuple[dict[str, object], set[int]]:
    n = modulus.bit_length()
    bound = n * n
    decoder = ParityDecoder(modulus)
    records: list[dict[str, object]] = []
    seen: set[int] = set()
    attempted = 0
    repeated = 0
    retained = 0

    def retain(c: int, provenance: dict[str, object]) -> dict[str, object] | None:
        nonlocal attempted, repeated, retained
        attempted += 1
        if c in seen:
            repeated += 1
            return None
        seen.add(c)
        w = pow(c, -1, modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, modulus)
            if 1 < divisor < modulus:
                return {
                    "channel": f"direct_{sign}",
                    "factor": divisor,
                    "c": c,
                    "w": w,
                    "provenance": provenance,
                }
        c_factors, w_factors, relation_factors = factor_relation(cache, c, w)
        decoder.add(relation_factors, provenance)
        records.append(
            {
                "c": c,
                "w": w,
                "P": c * w,
                "c_factors": c_factors,
                "w_factors": w_factors,
                "relation_factors": relation_factors,
                "provenance": provenance,
            }
        )
        retained += 1
        if decoder.factor is not None:
            return {"channel": "retained_parity_dependency", "factor": decoder.factor}
        return None

    for seed in range(2, n + 1):
        assert retain(seed, {"kind": "initial_seed", "seed": seed}) is None
    for exponent in range(bound + 1):
        for orientation, c in (
            ("u_power_times_v", pow(pair[0], exponent, modulus) * pair[1] % modulus),
            ("u_times_v_power", pair[0] * pow(pair[1], exponent, modulus) % modulus),
        ):
            provenance = {
                "kind": "fixed_pair_trajectory",
                "u": pair[0],
                "v": pair[1],
                "exponent": exponent,
                "orientation": orientation,
            }
            result = retain(c, provenance)
            if result is not None:
                return (
                    {
                        "status": "factor",
                        "n": n,
                        "bound": bound,
                        "pair": list(pair),
                        "attempted": attempted,
                        "repeated": repeated,
                        "retained": retained,
                        "dependencies": decoder.dependencies,
                        "global_dependencies": decoder.roots["plus_one"] + decoder.roots["minus_one"],
                        "basis_roots": decoder.certificate()["basis_roots"],
                        "result": result,
                    },
                    seen,
                )

    rank, distinct_rows = row_rank(records)
    matrix = decoder.certificate()
    assert rank == matrix["rank"]
    assert matrix["basis_roots"]["non_global"] == 0
    return (
        {
            "status": "null",
            "n": n,
            "bound": bound,
            "pair": list(pair),
            "attempted": attempted,
            "repeated": repeated,
            "retained": retained,
            "dependencies": decoder.dependencies,
            "global_dependencies": decoder.roots["plus_one"] + decoder.roots["minus_one"],
            "basis_roots": matrix["basis_roots"],
            "rank": rank,
            "distinct_nonzero_prime_masks": distinct_rows,
            "complete_basis_spans_kernel": matrix["rank"] + matrix["kernel_dimension"] == retained,
        },
        seen,
    )


def candidate_projection(case: dict[str, object]) -> dict[str, object]:
    recursive = case["recursive"]
    isolated = case["isolated_final_pair"]
    result = {
        "recursive": {
            key: recursive[key]
            for key in (
                "status",
                "factor",
                "factor_method",
                "factor_dependency_size",
                "round",
                "relations",
                "dependencies",
                "causal_pair",
                "round_summaries",
            )
        },
        "isolated": {
            key: isolated[key]
            for key in (
                "status",
                "n",
                "bound",
                "pair",
                "attempted",
                "repeated",
                "retained",
                "dependencies",
                "global_dependencies",
            )
        },
    }
    if "result" in isolated:
        result["isolated"]["result"] = isolated["result"]
    return result


def independent_projection(recursive: dict[str, object], isolated: dict[str, object]) -> dict[str, object]:
    isolated_projection = {
        key: isolated[key]
        for key in (
            "status",
            "n",
            "bound",
            "pair",
            "attempted",
            "repeated",
            "retained",
            "dependencies",
            "global_dependencies",
        )
    }
    if "result" in isolated:
        isolated_projection["result"] = isolated["result"]
    return {
        "recursive": {
            "status": recursive["status"],
            "factor": recursive["factor"],
            "factor_method": recursive["factor_method"],
            "factor_dependency_size": recursive["factor_dependency_size"],
            "round": recursive["round"],
            "relations": recursive["relations"],
            "dependencies": recursive["dependencies"],
            "causal_pair": recursive["trigger_pair"],
            "round_summaries": [
                {key: row[key] for key in ("round", "active", "new_relations", "new_dependencies")}
                for row in recursive["completed_rounds"]
            ],
        },
        "isolated": isolated_projection,
    }


def main() -> None:
    started = time.monotonic()
    actual_pins = {name: sha256(HERE / name) for name in CANDIDATE_PINS}
    assert actual_pins == CANDIDATE_PINS
    assert sha256(F98_SOURCE) == F98_PIN
    candidate = json.loads(CANDIDATE_OUTPUT.read_text())
    expected_cases = {int(case["N"]): case for case in candidate["cases"]}
    output_cases = []

    for p, q, expected_pair in CASES:
        case_started = time.monotonic()
        modulus = p * q
        n = modulus.bit_length()
        bound = n * n
        assert bool(ZZ(p).is_prime()) and bool(ZZ(q).is_prime())
        assert p != q and p > bound and q > bound
        g = math.gcd(p - 1, q - 1)
        A = (p - 1) // g
        B = (q - 1) // g
        assert math.gcd(A * B, modulus - 1) == 1

        cache = FactorCache()
        recursive = run_recursive(modulus, cache)
        assert tuple(recursive["trigger_pair"]) == expected_pair
        assert recursive["factor"] in (p, q)
        assert recursive["first_round"] is not None
        first_round = recursive["first_round"]
        assert first_round["kernel_dimension"] > 0
        assert first_round["basis_roots"] == {
            "plus_one": first_round["kernel_dimension"],
            "minus_one": 0,
            "non_global": 0,
        }

        isolated, isolated_seen = run_isolated(modulus, expected_pair, cache)
        if modulus == CASES[-1][0] * CASES[-1][1]:
            assert isolated["status"] == "factor"
            assert isolated["result"]["channel"] == "direct_minus"
            assert isolated["result"]["factor"] in (p, q)
        else:
            assert isolated["status"] == "null"
            assert isolated["dependencies"] == isolated["global_dependencies"]
            assert isolated["basis_roots"]["non_global"] == 0
            support_residues = recursive["success"]["support_residues"]
            outside = [residue for residue in support_residues if residue not in isolated_seen]
            recursive["success"]["support_residues_outside_isolated_menu_count"] = len(outside)
            recursive["success"]["support_residues_outside_isolated_menu_first"] = outside[:8]
            del recursive["success"]["support_residues"]
            assert outside

        expected_projection = candidate_projection(expected_cases[modulus])
        actual_projection = independent_projection(recursive, isolated)
        assert actual_projection == expected_projection, (modulus, actual_projection, expected_projection)
        output_cases.append(
            {
                "p": p,
                "q": q,
                "N": modulus,
                "n": n,
                "B": bound,
                "trial_hard": True,
                "stable_certificate": {"g": g, "A": A, "B": B, "gcd_AB_N_minus_1": 1},
                "final_pair_is_numeric_subset_of_initial_seed_range": recursive[
                    "trigger_pair_members_are_initial_seed_values"
                ],
                "first_round_exact_value_deduplicated": first_round,
                "recursive": {key: value for key, value in recursive.items() if key != "first_round"},
                "isolated_final_pair": isolated,
                "candidate_projection_exact_match": True,
                "factored_endpoint_cache_size": len(cache.values) - 1,
                "elapsed_seconds": time.monotonic() - case_started,
            }
        )

    six = output_cases[:-1]
    seventh = output_cases[-1]
    result = {
        "status": "PASS",
        "verdict": "candidate observations verified; interpretation must remain finite, factor-assisted, and queue-order-specific",
        "independence": {
            "candidate_code_imported": False,
            "pinned_f98_code_imported": False,
            "endpoint_factorization_backend": f"SageMath {SAGE_VERSION} / Pari",
            "gf2_implementation": "independent incremental column elimination plus independent row-rank cross-checks",
        },
        "pins": {
            "candidate_artifacts": actual_pins,
            "pinned_f98_factor_assisted_source": {"path": str(F98_SOURCE.relative_to(ROOT)), "sha256": F98_PIN},
            "audit_source_sha256": sha256(Path(__file__).resolve()),
        },
        "cases": output_cases,
        "aggregate": {
            "case_count": len(output_cases),
            "all_first_round_kernel_bases_nonempty_and_plus_one": all(
                case["first_round_exact_value_deduplicated"]["kernel_dimension"] > 0
                and case["first_round_exact_value_deduplicated"]["basis_roots"]["plus_one"]
                == case["first_round_exact_value_deduplicated"]["kernel_dimension"]
                for case in output_cases
            ),
            "all_recursive_runs_factor": all(case["recursive"]["status"] == "feedback_factor" for case in output_cases),
            "six_isolated_pair_batches_null": all(case["isolated_final_pair"]["status"] == "null" for case in six),
            "six_isolated_complete_kernel_bases_global": all(
                case["isolated_final_pair"]["dependencies"]
                == case["isolated_final_pair"]["global_dependencies"]
                and case["isolated_final_pair"]["complete_basis_spans_kernel"]
                for case in six
            ),
            "six_successful_dependencies_use_residues_outside_isolated_menu": all(
                case["recursive"]["success"]["support_residues_outside_isolated_menu_count"] > 0
                for case in six
            ),
            "seventh_isolated_pair_directly_factors": seventh["isolated_final_pair"]["status"] == "factor",
            "all_trigger_pair_values_in_initial_seed_range": all(
                case["final_pair_is_numeric_subset_of_initial_seed_range"] for case in output_cases
            ),
            "all_trigger_pairs_first_processed_at_success": all(
                case["recursive"]["success_round_processed_pairs"][-1]["prior_processed_pair_occurrences"] == 0
                for case in output_cases
            ),
            "all_candidate_projections_exact_match": all(case["candidate_projection_exact_match"] for case in output_cases),
        },
        "scope": {
            "factor_assisted": True,
            "finite_cases_only": True,
            "queue_order": "FIFO by retained relation index; the active batch is frozen at round start; invariance under other queue, pair, exponent, or orientation orders was not tested",
            "no_factor_free_promotion_claim": True,
        },
        "elapsed_seconds": time.monotonic() - started,
    }
    assert all(result["aggregate"].values())
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
