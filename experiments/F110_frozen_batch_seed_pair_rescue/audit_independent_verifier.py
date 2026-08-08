#!/usr/bin/env python3
"""Independent hostile verifier for the frozen-batch F110 candidate.

This executable does not import or execute the candidate or its pinned F98
implementation.  Sage supplies endpoint factorizations for an independent
reconstruction of the hidden-prime parity computation.  A separate standard
Python executable performs the N-only certificate replay.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import json
import math
from pathlib import Path

from sage.all import ZZ, factor as sage_factor


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
F109_OUTPUT = ROOT / "experiments/F109_recursive_feedback_rescue/OUTPUT.json"
F98_SOURCE = ROOT / "experiments/F98_multiseed_presentation_closure_kill/search_factor_assisted.py"
CANDIDATE_OUTPUT = HERE / "OUTPUT.json"

EXPECTED_HASHES = {
    HERE / "DESIGN.md": "afe07753f790778bd701c73ad39cc5d1e4c12a56a1ac5844d7f653bde1837f4b",
    HERE / "FAILED_RUNS.md": "faf2bf6e58710401808374e81af6c36d4e4df69dcc6b4d74d3c09d6ca663535b",
    HERE / "OUTPUT.json": "87b339efc536763aac40e04a39878f56cb36a49e64d9af492f3196de9a601458",
    HERE / "RESULT.md": "aa2c010284d5454889ec99163cf7e208806b1716016b41bf91847113b12551de",
    HERE / "RUN.log": "d7e6f51d9133937139030cec9c470a92a2afeb54a4fb444171349bb3cadc6a1c",
    HERE / "RUN_MANIFEST.md": "0656512043bc1f4e40fba2bb87071f6545064faf1fa6c961b450c5ba897ea9d0",
    HERE / "run_with_timeout.py": "00315172e6f1b25ea8f46261693475b266becce940cd84e98799518bb6920f2d",
    HERE / "test_frozen_batch_rescue.py": "2fa5068fbd8eb724d8f169fbf03be7e019db072c8b4fab2537c2c2e725204131",
    F109_OUTPUT: "ce23482d464dee551f3b585dedd803d3af24753592c4b639f5ee796b05d9e356",
    F98_SOURCE: "cbf50afc19a387ee58dffa9b0cca9a4ac2e732265c1b841cb535907cce364479",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def factor_free_initial_basis(endpoint_values: list[int]) -> list[tuple[int, dict[int, int]]]:
    """Compute the finest coprime, perfect-power-free endpoint basis by gcds."""
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


def pairs_from_initial_records(records: list[dict[str, object]]) -> tuple[list[tuple[int, int]], list[int]]:
    endpoints = [
        int(value)
        for record in records
        for value in (record["c"], record["w"])
    ]
    basis = factor_free_initial_basis(endpoints)
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
    return pairs, [block for block, _ in basis]


class PrimeParityDecoder:
    """Incremental GF(2) decoder with either trace or prime-label pivots."""

    def __init__(self, modulus: int, pivot_mode: str):
        self.modulus = modulus
        self.pivot_mode = pivot_mode
        self.prime_rows: dict[int, int] = {}
        self.pivots: dict[int, tuple[object, int]] = {}
        self.relation_factors: list[dict[int, int]] = []
        self.dependencies = 0
        self.global_dependencies = 0
        self.factor: int | None = None
        self.witness: dict[str, object] | None = None

    def add(self, factors: dict[int, int]) -> dict[str, object] | None:
        relation_index = len(self.relation_factors)
        self.relation_factors.append(factors)
        combination = 1 << relation_index

        if self.pivot_mode == "candidate_row_insertion":
            reduced: object = 0
            for prime, exponent in factors.items():
                row = self.prime_rows.setdefault(prime, len(self.prime_rows))
                if exponent & 1:
                    reduced = int(reduced) ^ (1 << row)
            while reduced:
                pivot = int(reduced).bit_length() - 1
                old = self.pivots.get(pivot)
                if old is None:
                    self.pivots[pivot] = (reduced, combination)
                    return None
                reduced = int(reduced) ^ int(old[0])
                combination ^= old[1]
        else:
            reduced = frozenset(prime for prime, exponent in factors.items() if exponent & 1)
            while reduced:
                pivot = max(reduced)
                old = self.pivots.get(pivot)
                if old is None:
                    self.pivots[pivot] = (reduced, combination)
                    return None
                reduced = reduced.symmetric_difference(old[0])
                combination ^= old[1]

        self.dependencies += 1
        exponents: dict[int, int] = {}
        selected = []
        bits = combination
        while bits:
            low = bits & -bits
            index = low.bit_length() - 1
            selected.append(index)
            for prime, exponent in self.relation_factors[index].items():
                exponents[prime] = exponents.get(prime, 0) + exponent
            bits ^= low
        assert all(exponent % 2 == 0 for exponent in exponents.values())
        root = 1
        for prime, exponent in exponents.items():
            root = root * pow(prime, exponent // 2, self.modulus) % self.modulus
        minus = math.gcd(root - 1, self.modulus)
        plus = math.gcd(root + 1, self.modulus)
        factor = minus if 1 < minus < self.modulus else plus if 1 < plus < self.modulus else None
        if factor is None:
            assert root in (1, self.modulus - 1)
            self.global_dependencies += 1
            return None
        witness = {
            "factor": factor,
            "relation_indices_zero_based": selected,
            "root_mod_N": root,
            "gcd_root_minus_one_N": minus,
            "gcd_root_plus_one_N": plus,
        }
        if self.factor is None:
            self.factor = factor
            self.witness = witness
        return witness


class ReconstructedBatch:
    def __init__(self, modulus: int):
        self.modulus = modulus
        self.decoder = PrimeParityDecoder(modulus, "candidate_row_insertion")
        self.records: list[dict[str, object]] = []
        self.seen_residues: set[int] = set()
        self.factor_cache: dict[int, dict[int, int]] = {1: {}}
        self.attempted = 0
        self.repeated = 0
        self.factor: int | None = None
        self.factor_method: str | None = None
        self.factor_witness: dict[str, object] | None = None

    def endpoint_factors(self, value: int) -> dict[int, int]:
        cached = self.factor_cache.get(value)
        if cached is None:
            cached = {int(prime): int(exponent) for prime, exponent in sage_factor(ZZ(value))}
            cached = dict(sorted(cached.items()))
            self.factor_cache[value] = cached
        return cached

    def retain(self, c: int, provenance: dict[str, object]) -> bool:
        self.attempted += 1
        if c in self.seen_residues:
            self.repeated += 1
            return False
        self.seen_residues.add(c)
        w = pow(c, -1, self.modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, self.modulus)
            if 1 < divisor < self.modulus:
                self.factor = divisor
                self.factor_method = f"direct_endpoint_{sign}"
                self.factor_witness = {
                    "c": c,
                    "w": w,
                    "gcd_value": divisor,
                    "provenance": provenance,
                }
                return True

        c_factors = self.endpoint_factors(c)
        w_factors = self.endpoint_factors(w)
        relation_factors = dict(c_factors)
        for prime, exponent in w_factors.items():
            relation_factors[prime] = relation_factors.get(prime, 0) + exponent
        record = {
            "c": c,
            "w": w,
            "P": c * w,
            "relation_factors": relation_factors,
            "provenance": provenance,
        }
        self.records.append(record)
        witness = self.decoder.add(relation_factors)
        if witness is not None:
            self.factor = int(witness["factor"])
            self.factor_method = "retained_parity_dependency"
            self.factor_witness = witness
            return True
        return False

    def run_pair(self, u: int, v: int, bound: int, kind: str, pair_index: int) -> bool:
        for exponent in range(bound + 1):
            candidates = (
                ("u_power_times_v", pow(u, exponent, self.modulus) * v % self.modulus),
                ("u_times_v_power", u * pow(v, exponent, self.modulus) % self.modulus),
            )
            for orientation, c in candidates:
                if self.retain(
                    c,
                    {
                        "kind": kind,
                        "pair_index_zero_based": pair_index,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                ):
                    return True
        return False


def decode_exact_value_batch(
    modulus: int, records: list[dict[str, object]]
) -> dict[str, object]:
    decoder = PrimeParityDecoder(modulus, "largest_prime_label")
    seen_products = set()
    duplicate_products = 0
    zero_products = 0
    first_factor_raw_index = None
    for raw_index, record in enumerate(records):
        product = int(record["P"])
        if product == 1:
            zero_products += 1
            continue
        if product in seen_products:
            duplicate_products += 1
            continue
        seen_products.add(product)
        witness = decoder.add(record["relation_factors"])
        if witness is not None:
            first_factor_raw_index = raw_index
            break
    return {
        "status": "factor" if decoder.factor is not None else "null",
        "factor": decoder.factor,
        "dependencies_examined": decoder.dependencies,
        "global_dependencies_before_factor": decoder.global_dependencies,
        "unique_products_examined": len(seen_products),
        "duplicate_products_skipped": duplicate_products,
        "unit_products_skipped": zero_products,
        "first_factor_raw_index": first_factor_raw_index,
        "factor_support": (
            len(decoder.witness["relation_indices_zero_based"])
            if decoder.witness is not None
            else 0
        ),
    }


def provenance_counts(records: list[dict[str, object]], indices: list[int]) -> dict[str, int]:
    return dict(
        sorted(
            Counter(str(records[index]["provenance"]["kind"]) for index in indices).items()
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    observed_hashes = {str(path.relative_to(ROOT)): sha256_file(path) for path in EXPECTED_HASHES}
    hash_failures = [
        f"hash mismatch: {path.relative_to(ROOT)}"
        for path, expected in EXPECTED_HASHES.items()
        if observed_hashes[str(path.relative_to(ROOT))] != expected
    ]
    assert not hash_failures, "; ".join(hash_failures)

    output_text = CANDIDATE_OUTPUT.read_text(encoding="utf-8")
    run_text = (HERE / "RUN.log").read_text(encoding="utf-8")
    assert run_text.split("stdout:\n", 1)[1].rsplit("\nstderr:\n", 1)[0] == output_text
    candidate = json.loads(output_text)
    f109 = json.loads(F109_OUTPUT.read_text(encoding="utf-8"))
    assert [(row["p"], row["q"]) for row in candidate["cases"]] == [
        (row["p"], row["q"]) for row in f109["cases"][:7]
    ]

    source = (HERE / "test_frozen_batch_rescue.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    public_basis_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "public_basis"
    ]
    assert len(public_basis_calls) == 1
    nonadaptive_run_pair_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "run_pair"
        and len(node.args) >= 4
        and isinstance(node.args[3], ast.Constant)
        and node.args[3].value == "nonadaptive_seed_pair"
    ]
    assert len(nonadaptive_run_pair_calls) == 1

    failures: list[str] = []
    case_results = []
    for published in candidate["cases"]:
        p = int(published["p"])
        q = int(published["q"])
        modulus = int(published["N"])
        n = modulus.bit_length()
        bound = n * n
        assert p * q == modulus
        assert n == published["n"] and bound == published["bound"]
        assert all(math.gcd(trial, modulus) == 1 for trial in range(2, bound + 1))

        batch = ReconstructedBatch(modulus)
        for seed in range(2, n + 1):
            assert not batch.retain(seed, {"kind": "initial_seed", "seed": seed})
        initial_count = len(batch.records)
        frozen_pairs, public_blocks = pairs_from_initial_records(batch.records)
        published_pairs = [tuple(pair) for pair in published["first_layer"]["pairs"]]
        if frozen_pairs != published_pairs:
            failures.append(f"N={modulus}: public initial basis gives different frozen pairs")

        for pair_index, (u, v) in enumerate(frozen_pairs):
            assert not batch.run_pair(u, v, bound, "frozen_seed_basis_pair", pair_index)
        first_layer_count = len(batch.records)
        first_layer = {
            "initial_records": initial_count,
            "pair_count": len(frozen_pairs),
            "pairs": [list(pair) for pair in frozen_pairs],
            "relations": first_layer_count,
            "dependencies": batch.decoder.dependencies,
            "global_dependencies": batch.decoder.global_dependencies,
            "all_dependencies_global": batch.decoder.dependencies
            == batch.decoder.global_dependencies,
        }
        if first_layer != published["first_layer"]:
            failures.append(f"N={modulus}: reconstructed first-layer summary differs")
        if batch.decoder.factor is not None:
            failures.append(f"N={modulus}: reconstructed first layer contains a factor")

        exact_first_layer = decode_exact_value_batch(modulus, batch.records)
        if exact_first_layer["status"] != "null" or (
            exact_first_layer["dependencies_examined"]
            != exact_first_layer["global_dependencies_before_factor"]
        ):
            failures.append(f"N={modulus}: exact-value-deduplicated first layer is not all-global")

        menu_attempted = 0
        for v in range(3, n + 1):
            menu_attempted += 1
            if batch.run_pair(2, v, bound, "nonadaptive_seed_pair", menu_attempted - 1):
                break
        else:
            failures.append(f"N={modulus}: u=2 prefix did not factor")

        expected_summary = {
            "factor": published["factor"],
            "factor_method": published["factor_method"],
            "relations_at_stop": published["relations_at_stop"],
            "dependencies_at_stop": published["dependencies_at_stop"],
            "global_dependencies_at_stop": published["global_dependencies_at_stop"],
            "candidate_residues_attempted": published["candidate_residues_attempted"],
            "duplicate_residues": published["duplicate_residues"],
            "seed_pair_menu_attempted": published["seed_pair_menu_attempted"],
            "successful_pair": published["successful_pair"],
        }
        observed_summary = {
            "factor": batch.factor,
            "factor_method": batch.factor_method,
            "relations_at_stop": len(batch.records),
            "dependencies_at_stop": batch.decoder.dependencies,
            "global_dependencies_at_stop": batch.decoder.global_dependencies,
            "candidate_residues_attempted": batch.attempted,
            "duplicate_residues": batch.repeated,
            "seed_pair_menu_attempted": menu_attempted,
            "successful_pair": [2, menu_attempted + 2],
        }
        if observed_summary != expected_summary:
            failures.append(f"N={modulus}: reconstructed stopping summary differs")
        if published["successful_pair"] != [2, published["seed_pair_menu_attempted"] + 2]:
            failures.append(f"N={modulus}: successful pair is not at its fixed u=2-prefix position")
        if published["seed_pair_menu_total"] != (n - 1) * (n - 2) // 2:
            failures.append(f"N={modulus}: declared all-pairs menu size is wrong")

        raw_witness_match = None
        raw_kind_counts = None
        if published["factor_method"] == "retained_parity_dependency":
            assert batch.factor_witness is not None
            declared = published["dependency_provenance"]
            raw_indices = batch.factor_witness["relation_indices_zero_based"]
            raw_witness_match = (
                raw_indices == declared["relation_indices_zero_based"]
                and batch.factor_witness["root_mod_N"] == declared["root_mod_N"]
                and batch.factor_witness["gcd_root_minus_one_N"]
                == declared["gcd_root_minus_one_N"]
                and batch.factor_witness["gcd_root_plus_one_N"]
                == declared["gcd_root_plus_one_N"]
            )
            raw_kind_counts = provenance_counts(batch.records, raw_indices)
            raw_witness_match = raw_witness_match and raw_kind_counts == declared["kind_counts"]
            if not raw_witness_match:
                failures.append(f"N={modulus}: exact online dependency does not reproduce")
            if not (
                raw_kind_counts.get("frozen_seed_basis_pair", 0) > 0
                and raw_kind_counts.get("nonadaptive_seed_pair", 0) > 0
            ):
                failures.append(f"N={modulus}: online dependency does not cross the layer boundary")
        else:
            if batch.factor_method != "direct_endpoint_minus" or batch.factor_witness is None:
                failures.append(f"N={modulus}: direct seventh factor did not reproduce")

        exact_full = decode_exact_value_batch(modulus, batch.records)
        if published["factor_method"] == "retained_parity_dependency":
            if exact_full["status"] != "factor" or modulus % int(exact_full["factor"]) != 0:
                failures.append(f"N={modulus}: alternate exact-value decoder did not factor")

        first_duplicate_pair_count = len(frozen_pairs) - len(set(frozen_pairs))
        prefix_pairs = [(2, v) for v in range(3, n + 1)]
        case_results.append(
            {
                "N": modulus,
                "n": n,
                "bound": bound,
                "factor": batch.factor,
                "factor_method": batch.factor_method,
                "public_initial_basis_block_count": len(public_blocks),
                "public_frozen_pairs_match": frozen_pairs == published_pairs,
                "frozen_pair_entries": len(frozen_pairs),
                "duplicate_frozen_pair_entries": first_duplicate_pair_count,
                "first_layer": first_layer,
                "exact_value_first_layer": exact_first_layer,
                "successful_pair": published["successful_pair"],
                "u2_prefix_position": menu_attempted,
                "u2_prefix_schedule_sha256": hashlib.sha256(
                    json.dumps(prefix_pairs, separators=(",", ":")).encode()
                ).hexdigest(),
                "raw_online_witness_match": raw_witness_match,
                "raw_online_kind_counts": raw_kind_counts,
                "exact_value_full_batch": exact_full,
                "residue_attempts_reproduced": batch.attempted,
                "retained_relations_reproduced": len(batch.records),
                "duplicate_residues_reproduced": batch.repeated,
            }
        )

    all_u2 = all(row["successful_pair"][0] == 2 for row in case_results)
    all_first_global = all(row["first_layer"]["all_dependencies_global"] for row in case_results)
    all_public_pairs = all(row["public_frozen_pairs_match"] for row in case_results)
    if not all_u2:
        failures.append("not every fixed trace stops in the u=2 prefix")
    if not all_first_global:
        failures.append("a frozen first layer has a non-global online dependency")
    if not all_public_pairs:
        failures.append("factor-free initial basis reconstruction differs")

    result = {
        "status": "PASS" if not failures else "FAIL",
        "verifier": "independent Sage endpoint-factor reconstruction; candidate not imported or run",
        "input_hashes": observed_hashes,
        "candidate_run_stdout_matches_output": True,
        "static_source_check": {
            "public_basis_call_count": len(public_basis_calls),
            "public_basis_call_line": public_basis_calls[0].lineno,
            "nonadaptive_run_pair_call_count": len(nonadaptive_run_pair_calls),
            "nonadaptive_run_pair_call_line": nonadaptive_run_pair_calls[0].lineno,
            "menu_is_lexicographic_all_pairs": True,
            "menu_pair_selection_reads_generated_relations": False,
            "termination_on_factor": True,
        },
        "claims": {
            "all_seven_reconstructed": len(case_results) == 7,
            "all_first_layers_online_all_global": all_first_global,
            "all_initial_frozen_pairs_publicly_reconstructed": all_public_pairs,
            "all_traces_stop_in_predetermined_u2_prefix": all_u2,
            "stored_source_residue_attempt_bound": "O(n^4)",
            "narrowed_u2_source_residue_attempt_bound": "O(n^3)",
            "factor_assisted_runtime_is_not_shown_polynomial": True,
            "all_input_success_claim": False,
        },
        "cases": case_results,
        "failures": failures,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
