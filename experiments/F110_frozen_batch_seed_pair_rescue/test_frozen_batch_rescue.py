#!/usr/bin/env python3
"""Test a frozen first layer plus a nonadaptive menu of small seed pairs."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[2]
F98_SOURCE = ROOT / "experiments/F98_multiseed_presentation_closure_kill/search_factor_assisted.py"
F109_OUTPUT = ROOT / "experiments/F109_recursive_feedback_rescue/OUTPUT.json"
EXPECTED_F98_SHA256 = "cbf50afc19a387ee58dffa9b0cca9a4ac2e732265c1b841cb535907cce364479"
EXPECTED_F109_SHA256 = "ce23482d464dee551f3b585dedd803d3af24753592c4b639f5ee796b05d9e356"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(F98_SOURCE) == EXPECTED_F98_SHA256
assert sha256_file(F109_OUTPUT) == EXPECTED_F109_SHA256
SPEC = importlib.util.spec_from_file_location("f110_pinned_f98", F98_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import pinned F98 source")
F98 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F98)


class FrozenBatch:
    def __init__(self, modulus: int):
        self.modulus = modulus
        self.decoder = F98.PrimeDecoder(modulus)
        self.records: list[dict[str, object]] = []
        self.seen: set[int] = set()
        self.factor_cache: dict[int, dict[int, int]] = {1: {}}
        self.attempted = 0
        self.repeated = 0

    def retain(self, c: int, provenance: dict[str, object]) -> bool:
        self.attempted += 1
        if c in self.seen:
            self.repeated += 1
            return False
        self.seen.add(c)
        w = pow(c, -1, self.modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, self.modulus)
            if 1 < divisor < self.modulus:
                self.decoder.factor = divisor
                self.decoder.factor_method = f"direct_endpoint_{sign}"
                self.decoder.factor_dependency_size = 0
                self.decoder.factor_witness = {
                    "provenance": provenance,
                    "c": c,
                    "w": w,
                    "gcd_value": divisor,
                }
                return True

        c_factors = self.factor_cache.get(c)
        if c_factors is None:
            c_factors = F98.factor_u64(c)
            self.factor_cache[c] = c_factors
        w_factors = self.factor_cache.get(w)
        if w_factors is None:
            w_factors = F98.factor_u64(w)
            self.factor_cache[w] = w_factors
        relation_factors = dict(c_factors)
        for prime, exponent in w_factors.items():
            relation_factors[prime] = relation_factors.get(prime, 0) + exponent
        self.decoder.add(relation_factors)
        self.records.append(
            {
                "c": c,
                "w": w,
                "c_factors": c_factors,
                "w_factors": w_factors,
                "provenance": provenance,
            }
        )
        return self.decoder.factor is not None

    def run_pair(self, u: int, v: int, bound: int, kind: str, pair_index: int) -> bool:
        for exponent in range(bound + 1):
            for orientation, c in (
                ("u_power_times_v", pow(u, exponent, self.modulus) * v % self.modulus),
                ("u_times_v_power", u * pow(v, exponent, self.modulus) % self.modulus),
            ):
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

    def dependency_provenance(self) -> dict[str, object] | None:
        witness = self.decoder.factor_witness
        if self.decoder.factor_method != "retained_parity_dependency" or witness is None:
            return None
        indices = witness["relation_indices_zero_based"]
        provenances = [self.records[index]["provenance"] for index in indices]
        kind_counts = Counter(provenance["kind"] for provenance in provenances)
        trajectory_keys = {
            (
                provenance["kind"],
                provenance.get("u"),
                provenance.get("v"),
                provenance.get("pair_index_zero_based"),
            )
            for provenance in provenances
            if provenance["kind"] != "initial_seed"
        }
        return {
            "relation_indices_zero_based": indices,
            "kind_counts": dict(sorted(kind_counts.items())),
            "distinct_nonseed_trajectory_keys": len(trajectory_keys),
            "root_mod_N": witness["root_mod_N"],
            "gcd_root_minus_one_N": witness["gcd_root_minus_one_N"],
            "gcd_root_plus_one_N": witness["gcd_root_plus_one_N"],
        }


def run_case(p: int, q: int) -> dict[str, object]:
    modulus = p * q
    n = modulus.bit_length()
    bound = n * n
    for trial in range(2, bound + 1):
        divisor = math.gcd(trial, modulus)
        assert not 1 < divisor < modulus

    batch = FrozenBatch(modulus)
    for seed in range(2, n + 1):
        assert not batch.retain(seed, {"kind": "initial_seed", "seed": seed})

    initial_records = len(batch.records)
    _, supports = F98.public_basis(batch.records)
    frozen_pairs: list[tuple[int, int]] = []
    for support in supports:
        if len(support) == 1:
            frozen_pairs.append((support[0], 1))
        else:
            frozen_pairs.append((support[0], support[1]))

    for pair_index, (u, v) in enumerate(frozen_pairs):
        assert not batch.run_pair(u, v, bound, "frozen_seed_basis_pair", pair_index)

    first_layer = {
        "initial_records": initial_records,
        "pair_count": len(frozen_pairs),
        "pairs": [list(pair) for pair in frozen_pairs],
        "relations": len(batch.records),
        "dependencies": batch.decoder.dependencies,
        "global_dependencies": batch.decoder.global_dependencies,
        "all_dependencies_global": batch.decoder.dependencies == batch.decoder.global_dependencies,
    }
    assert first_layer["all_dependencies_global"]

    menu_pairs_attempted = 0
    successful_pair = None
    for u in range(2, n + 1):
        for v in range(u + 1, n + 1):
            pair_index = menu_pairs_attempted
            menu_pairs_attempted += 1
            if batch.run_pair(u, v, bound, "nonadaptive_seed_pair", pair_index):
                successful_pair = [u, v]
                break
        if successful_pair is not None:
            break

    return {
        "p": p,
        "q": q,
        "N": modulus,
        "n": n,
        "bound": bound,
        "status": "factor" if batch.decoder.factor is not None else "null",
        "factor": batch.decoder.factor,
        "factor_method": batch.decoder.factor_method,
        "factor_dependency_size": batch.decoder.factor_dependency_size,
        "first_layer": first_layer,
        "seed_pair_menu_total": (n - 1) * (n - 2) // 2,
        "seed_pair_menu_attempted": menu_pairs_attempted,
        "successful_pair": successful_pair,
        "relations_at_stop": len(batch.records),
        "dependencies_at_stop": batch.decoder.dependencies,
        "global_dependencies_at_stop": batch.decoder.global_dependencies,
        "candidate_residues_attempted": batch.attempted,
        "duplicate_residues": batch.repeated,
        "dependency_provenance": batch.dependency_provenance(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-cap", type=int, default=7)
    args = parser.parse_args()
    assert 1 <= args.case_cap <= 7
    f109 = json.loads(F109_OUTPUT.read_text())
    cases = [(row["p"], row["q"]) for row in f109["cases"][: args.case_cap]]
    started = time.monotonic()
    results = []
    for p, q in cases:
        case_started = time.monotonic()
        result = run_case(p, q)
        result["elapsed_seconds"] = time.monotonic() - case_started
        results.append(result)
    output = {
        "status": "PASS" if all(row["status"] == "factor" for row in results) else "FAIL",
        "role": "factor-assisted bounded nonadaptive control; N-only replay required",
        "case_cap": args.case_cap,
        "pinned_inputs": {
            str(F98_SOURCE.relative_to(ROOT)): sha256_file(F98_SOURCE),
            str(F109_OUTPUT.relative_to(ROOT)): sha256_file(F109_OUTPUT),
        },
        "cases": results,
        "all_first_layers_have_only_global_dependencies": all(
            row["first_layer"]["all_dependencies_global"] for row in results
        ),
        "all_frozen_nonadaptive_batches_factor": all(row["status"] == "factor" for row in results),
        "all_parity_witnesses_cross_the_layer_boundary": all(
            row["factor_method"] != "retained_parity_dependency"
            or (
                row["dependency_provenance"]["kind_counts"].get("frozen_seed_basis_pair", 0) > 0
                and row["dependency_provenance"]["kind_counts"].get("nonadaptive_seed_pair", 0) > 0
            )
            for row in results
        ),
        "elapsed_seconds": time.monotonic() - started,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
