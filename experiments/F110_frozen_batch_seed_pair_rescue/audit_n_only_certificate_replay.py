#!/usr/bin/env python3
"""N-only replay of the seven fixed F110 traces and certificates.

The candidate output supplies fixed public advice: N, the declared stopping
point, and six dependency supports.  This executable ignores the published
prime factors.  It regenerates every retained relation with modular arithmetic,
reconstructs the initial basis with gcd/perfect-power splitting, and verifies
the six exact-square certificates and the seventh direct gcd.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CANDIDATE_OUTPUT = HERE / "OUTPUT.json"
EXPECTED_OUTPUT_SHA256 = "87b339efc536763aac40e04a39878f56cb36a49e64d9af492f3196de9a601458"


def exact_nth_root(value: int, exponent: int) -> int | None:
    low = 1
    high = 1 << ((value.bit_length() + exponent - 1) // exponent + 1)
    while low + 1 < high:
        middle = (low + high) // 2
        powered = middle**exponent
        if powered < value:
            low = middle
        elif powered > value:
            high = middle
        else:
            return middle
    return low if low**exponent == value else None


def primitive_root(value: int) -> tuple[int, int]:
    for exponent in range(value.bit_length(), 1, -1):
        root = exact_nth_root(value, exponent)
        if root is not None:
            return root, exponent
    return value, 1


def factor_free_basis(endpoint_values: list[int]) -> list[tuple[int, dict[int, int]]]:
    pending = [
        (value, {endpoint: 1})
        for endpoint, value in enumerate(endpoint_values)
        if value > 1
    ]
    basis: list[tuple[int, dict[int, int]]] = []
    while pending:
        value, signature = pending.pop()
        if value == 1:
            continue
        root, power = primitive_root(value)
        if power > 1:
            value = root
            signature = {endpoint: power * exponent for endpoint, exponent in signature.items()}
        for position, (old_value, old_signature) in enumerate(basis):
            common = math.gcd(value, old_value)
            if common == 1:
                continue
            basis.pop(position)
            if value == old_value:
                merged = dict(signature)
                for endpoint, exponent in old_signature.items():
                    merged[endpoint] = merged.get(endpoint, 0) + exponent
                pending.append((value, merged))
            else:
                pending.extend(
                    (
                        (common, signature),
                        (value // common, signature),
                        (common, old_signature),
                        (old_value // common, old_signature),
                    )
                )
            break
        else:
            basis.append((value, signature))
    basis.sort(key=lambda item: item[0])
    reconstructed = [1] * len(endpoint_values)
    for position, (block, signature) in enumerate(basis):
        assert primitive_root(block)[1] == 1
        assert all(math.gcd(block, old_block) == 1 for old_block, _ in basis[:position])
        for endpoint, exponent in signature.items():
            reconstructed[endpoint] *= block**exponent
    assert reconstructed == endpoint_values
    return basis


def frozen_pairs_from_initial(records: list[dict[str, object]]) -> tuple[list[tuple[int, int]], int]:
    endpoints = [
        int(value)
        for record in records
        for value in (record["c"], record["w"])
    ]
    basis = factor_free_basis(endpoints)
    pairs = []
    for relation_index in range(len(records)):
        support = [
            block
            for block, signature in basis
            if signature.get(2 * relation_index, 0)
            + signature.get(2 * relation_index + 1, 0)
            > 0
        ]
        assert support
        pairs.append((support[0], 1) if len(support) == 1 else (support[0], support[1]))
    return pairs, len(basis)


class PublicTrace:
    def __init__(self, modulus: int):
        self.modulus = modulus
        self.records: list[dict[str, object]] = []
        self.seen_residues: set[int] = set()
        self.attempted = 0
        self.duplicate_residues = 0

    def retain(self, c: int, provenance: dict[str, object]) -> dict[str, object] | None:
        self.attempted += 1
        if c in self.seen_residues:
            self.duplicate_residues += 1
            return None
        self.seen_residues.add(c)
        w = pow(c, -1, self.modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, self.modulus)
            if 1 < divisor < self.modulus:
                return {
                    "factor": divisor,
                    "method": f"direct_endpoint_{sign}",
                    "c": c,
                    "w": w,
                    "provenance": provenance,
                }
        self.records.append(
            {
                "c": c,
                "w": w,
                "P": c * w,
                "provenance": provenance,
            }
        )
        return None

    def run_complete_pair(self, u: int, v: int, bound: int, kind: str, pair_index: int) -> None:
        for exponent in range(bound + 1):
            candidates = (
                ("u_power_times_v", pow(u, exponent, self.modulus) * v % self.modulus),
                ("u_times_v_power", u * pow(v, exponent, self.modulus) % self.modulus),
            )
            for orientation, c in candidates:
                direct = self.retain(
                    c,
                    {
                        "kind": kind,
                        "pair_index_zero_based": pair_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
                assert direct is None


def kind_counts(records: list[dict[str, object]], indices: list[int]) -> dict[str, int]:
    return dict(
        sorted(Counter(str(records[index]["provenance"]["kind"]) for index in indices).items())
    )


def verify_exact_certificate(
    modulus: int,
    records: list[dict[str, object]],
    declared: dict[str, object],
) -> dict[str, object]:
    selected = [int(index) for index in declared["relation_indices_zero_based"]]
    assert selected == sorted(set(selected))
    assert selected and selected[-1] < len(records)
    product = math.prod(int(records[index]["P"]) for index in selected)
    root = math.isqrt(product)
    assert root * root == product
    root_modulus = root % modulus
    minus = math.gcd(root - 1, modulus)
    plus = math.gcd(root + 1, modulus)
    raw_counts = kind_counts(records, selected)
    raw_crosses = (
        raw_counts.get("frozen_seed_basis_pair", 0) > 0
        and raw_counts.get("nonadaptive_seed_pair", 0) > 0
    )
    assert root_modulus == declared["root_mod_N"]
    assert minus == declared["gcd_root_minus_one_N"]
    assert plus == declared["gcd_root_plus_one_N"]
    assert raw_counts == declared["kind_counts"]
    assert 1 < minus < modulus or 1 < plus < modulus

    multiplicities = Counter(int(records[index]["P"]) for index in selected)
    first_occurrence = {}
    for index, record in enumerate(records):
        first_occurrence.setdefault(int(record["P"]), index)
    canonical_indices = sorted(
        first_occurrence[relation_value]
        for relation_value, multiplicity in multiplicities.items()
        if relation_value != 1 and multiplicity % 2 == 1
    )
    canonical_product = math.prod(int(records[index]["P"]) for index in canonical_indices)
    canonical_root = math.isqrt(canonical_product)
    assert canonical_root * canonical_root == canonical_product
    canonical_minus = math.gcd(canonical_root - 1, modulus)
    canonical_plus = math.gcd(canonical_root + 1, modulus)
    canonical_counts = kind_counts(records, canonical_indices)
    canonical_crosses = (
        canonical_counts.get("frozen_seed_basis_pair", 0) > 0
        and canonical_counts.get("nonadaptive_seed_pair", 0) > 0
    )
    assert canonical_root % modulus == root_modulus
    assert canonical_minus == minus and canonical_plus == plus
    assert len(canonical_indices) == len(
        {int(records[index]["P"]) for index in canonical_indices}
    )

    trajectory_keys = {
        (
            records[index]["provenance"]["kind"],
            records[index]["provenance"].get("u"),
            records[index]["provenance"].get("v"),
            records[index]["provenance"].get("pair_index_zero_based"),
        )
        for index in selected
        if records[index]["provenance"]["kind"] != "initial_seed"
    }
    assert len(trajectory_keys) == declared["distinct_nonseed_trajectory_keys"]
    return {
        "raw_support": len(selected),
        "raw_distinct_exact_values": len(multiplicities),
        "raw_repeated_exact_value_occurrences": len(selected) - len(multiplicities),
        "raw_max_exact_value_multiplicity": max(multiplicities.values()),
        "raw_kind_counts": raw_counts,
        "raw_crosses_layer_boundary": raw_crosses,
        "canonical_exact_deduplicated_support": len(canonical_indices),
        "canonical_kind_counts": canonical_counts,
        "canonical_crosses_layer_boundary": canonical_crosses,
        "canonical_root_mod_N": canonical_root % modulus,
        "gcd_root_minus_one_N": canonical_minus,
        "gcd_root_plus_one_N": canonical_plus,
        "proper_factor": minus if 1 < minus < modulus else plus,
        "selected_index_sha256": hashlib.sha256(
            json.dumps(selected, separators=(",", ":")).encode()
        ).hexdigest(),
        "canonical_index_sha256": hashlib.sha256(
            json.dumps(canonical_indices, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    candidate_bytes = CANDIDATE_OUTPUT.read_bytes()
    assert hashlib.sha256(candidate_bytes).hexdigest() == EXPECTED_OUTPUT_SHA256
    candidate = json.loads(candidate_bytes)
    failures: list[str] = []
    case_results = []

    for published in candidate["cases"]:
        modulus = int(published["N"])
        n = modulus.bit_length()
        bound = n * n
        assert published["n"] == n and published["bound"] == bound
        assert all(math.gcd(trial, modulus) == 1 for trial in range(2, bound + 1))

        trace = PublicTrace(modulus)
        for seed in range(2, n + 1):
            direct = trace.retain(seed, {"kind": "initial_seed", "seed": seed})
            assert direct is None
        frozen_pairs, basis_count = frozen_pairs_from_initial(trace.records)
        published_pairs = [tuple(pair) for pair in published["first_layer"]["pairs"]]
        if frozen_pairs != published_pairs:
            failures.append(f"N={modulus}: N-only initial basis gives different pairs")
        for pair_index, (u, v) in enumerate(frozen_pairs):
            trace.run_complete_pair(u, v, bound, "frozen_seed_basis_pair", pair_index)
        if len(trace.records) != published["first_layer"]["relations"]:
            failures.append(f"N={modulus}: N-only first-layer relation count differs")
        first_layer_relation_count = len(trace.records)

        target_attempts = int(published["candidate_residues_attempted"])
        direct_at_stop = None
        stop_metadata = None
        menu_attempted = 0
        reached_target = False
        for v in range(3, n + 1):
            menu_attempted += 1
            for exponent in range(bound + 1):
                candidates = (
                    ("u_power_times_v", pow(2, exponent, modulus) * v % modulus),
                    ("u_times_v_power", 2 * pow(v, exponent, modulus) % modulus),
                )
                for orientation, c in candidates:
                    provenance = {
                        "kind": "nonadaptive_seed_pair",
                        "pair_index_zero_based": menu_attempted - 1,
                        "u": 2,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    }
                    direct = trace.retain(c, provenance)
                    if direct is not None and trace.attempted != target_attempts:
                        failures.append(f"N={modulus}: unexpected earlier direct factor")
                    if trace.attempted == target_attempts:
                        direct_at_stop = direct
                        stop_metadata = provenance
                        reached_target = True
                        break
                if reached_target:
                    break
            if reached_target:
                break
        assert reached_target and stop_metadata is not None

        if [2, stop_metadata["v"]] != published["successful_pair"]:
            failures.append(f"N={modulus}: target attempt is not in the published pair")
        if menu_attempted != published["seed_pair_menu_attempted"]:
            failures.append(f"N={modulus}: u=2 prefix position differs")
        if len(trace.records) != published["relations_at_stop"]:
            failures.append(f"N={modulus}: retained relation count differs")
        if trace.duplicate_residues != published["duplicate_residues"]:
            failures.append(f"N={modulus}: residue duplicate count differs")

        certificate = None
        if published["factor_method"] == "retained_parity_dependency":
            if direct_at_stop is not None:
                failures.append(f"N={modulus}: parity stop is a direct factor in N-only replay")
            certificate = verify_exact_certificate(
                modulus, trace.records, published["dependency_provenance"]
            )
            if not certificate["raw_crosses_layer_boundary"]:
                failures.append(f"N={modulus}: raw certificate does not cross layers")
            if not certificate["canonical_crosses_layer_boundary"]:
                failures.append(f"N={modulus}: canonical exact-deduplicated certificate does not cross layers")
        else:
            if direct_at_stop is None:
                failures.append(f"N={modulus}: declared direct stop has no direct gcd")
            else:
                if direct_at_stop["method"] != published["factor_method"]:
                    failures.append(f"N={modulus}: direct method differs")
                if direct_at_stop["factor"] != published["factor"]:
                    failures.append(f"N={modulus}: direct factor differs")

        all_products = [int(record["P"]) for record in trace.records]
        first_products = all_products[:first_layer_relation_count]
        prefix_pairs = [(2, v) for v in range(3, n + 1)]
        case_results.append(
            {
                "N": modulus,
                "n": n,
                "bound": bound,
                "factor_method": published["factor_method"],
                "factor": published["factor"],
                "public_initial_basis_block_count": basis_count,
                "public_frozen_pairs_match": frozen_pairs == published_pairs,
                "frozen_pair_entry_count": len(frozen_pairs),
                "distinct_frozen_pairs": len(set(frozen_pairs)),
                "first_layer_raw_relations": first_layer_relation_count,
                "first_layer_unique_nonunit_exact_values": len(
                    {value for value in first_products if value != 1}
                ),
                "full_raw_relations": len(trace.records),
                "full_unique_nonunit_exact_values": len(
                    {value for value in all_products if value != 1}
                ),
                "successful_pair": published["successful_pair"],
                "u2_prefix_position": menu_attempted,
                "u2_prefix_schedule_sha256": hashlib.sha256(
                    json.dumps(prefix_pairs, separators=(",", ":")).encode()
                ).hexdigest(),
                "stop_provenance": stop_metadata,
                "direct_factor_at_stop": direct_at_stop,
                "certificate": certificate,
                "residue_attempts": trace.attempted,
                "duplicate_residues": trace.duplicate_residues,
                "complexity_counts": {
                    "initial_attempts": n - 1,
                    "frozen_attempt_upper_bound": 2 * (n - 1) * (bound + 1),
                    "narrow_u2_menu_attempt_upper_bound": 2 * (n - 2) * (bound + 1),
                    "stored_all_pairs_menu_attempt_upper_bound": (
                        (n - 1) * (n - 2) * (bound + 1)
                    ),
                },
            }
        )

    parity_cases = [row for row in case_results if row["certificate"] is not None]
    all_raw_cross = all(row["certificate"]["raw_crosses_layer_boundary"] for row in parity_cases)
    all_canonical_cross = all(
        row["certificate"]["canonical_crosses_layer_boundary"] for row in parity_cases
    )
    result = {
        "status": "PASS" if not failures else "FAIL",
        "replay": "fixed-certificate N-only replay; published p and q fields ignored",
        "candidate_output_sha256": EXPECTED_OUTPUT_SHA256,
        "allowed_operations": [
            "exact integer arithmetic",
            "modular exponentiation",
            "modular inverse",
            "gcd",
            "exact perfect-power tests",
            "integer square root",
        ],
        "forbidden_operations_used": [],
        "claims": {
            "all_seven_traces_regenerated": len(case_results) == 7,
            "all_traces_stop_in_u2_prefix": all(row["successful_pair"][0] == 2 for row in case_results),
            "six_raw_parity_certificates_cross_layers": len(parity_cases) == 6 and all_raw_cross,
            "six_canonical_exact_deduplicated_certificates_cross_layers": (
                len(parity_cases) == 6 and all_canonical_cross
            ),
            "seventh_is_direct": len(case_results) == 7
            and case_results[-1]["direct_factor_at_stop"] is not None,
            "certificate_verification_is_factor_free": True,
            "certificate_discovery_is_factor_free": False,
            "all_input_success_claim": False,
        },
        "cases": case_results,
        "failures": failures,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
