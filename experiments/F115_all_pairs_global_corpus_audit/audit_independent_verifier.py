#!/usr/bin/env python3
"""Independent Sage-backed audit of the combined F112/F113/F114 claim.

No candidate implementation is imported.  This verifier reconstructs the
F104 corpus, replays all 100 frozen-plus-(2,v) cases, and continues the 14
nulls through the complete lexicographic all-seed-pair menu.
"""

from __future__ import annotations

from collections import Counter
import gc
import hashlib
import json
import math
from pathlib import Path
import sys
import time

from sage.all import ZZ
from sage.env import SAGE_VERSION


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
F104_DIR = ROOT / "experiments/F104_all_input_peeling_counterexample"
F112_DIR = ROOT / "experiments/F112_frozen_two_v_global_root_stress"
F113_DIR = ROOT / "experiments/F113_all_seed_pairs_n46_rescue"
F114_DIR = ROOT / "experiments/F114_all_seed_pairs_n50_rescue"
F110_SOURCE = ROOT / "experiments/F110_frozen_batch_seed_pair_rescue/test_frozen_batch_rescue.py"
F112_OUTPUT = F112_DIR / "OUTPUT_FAILED_20260808T025244Z_CLAIM.json"
F113_OUTPUT = F113_DIR / "OUTPUT.json"
F114_OUTPUT = F114_DIR / "OUTPUT.json"
EXCLUDED_F104 = "PRIME_SCAN_320K_640K_WIDE_OUTPUT.json"

CANDIDATE_PINS = {
    "experiments/F110_frozen_batch_seed_pair_rescue/test_frozen_batch_rescue.py": "2fa5068fbd8eb724d8f169fbf03be7e019db072c8b4fab2537c2c2e725204131",
    "experiments/F112_frozen_two_v_global_root_stress/DESIGN.md": "b27316ffe98f84830802abd018ef6a5f0e902d1a7d399d8dd727befeef61fec1",
    "experiments/F112_frozen_two_v_global_root_stress/FAILED_RUNS.md": "fe98ec27dc6635b645bfe18e775337d4586681ae7b722cc8a59033a7e47681ab",
    "experiments/F112_frozen_two_v_global_root_stress/OUTPUT_FAILED_20260808T025244Z_CLAIM.json": "1c5bc0c9078f2424134790f410f15b9ed10f2fefc92e87b7e59121096602ee96",
    "experiments/F112_frozen_two_v_global_root_stress/RESULT.md": "cf41d85d1a97f72449107d8823b203b6e3139c3a912b34518ffd76b76645efaf",
    "experiments/F112_frozen_two_v_global_root_stress/RUN_FAILED_20260808T024838Z_EXIT_1.log": "e94e192901fc46f338b09da8e843bdf4dc313ed4ab01500f3e78c20fb7502fa5",
    "experiments/F112_frozen_two_v_global_root_stress/RUN_FAILED_20260808T025244Z_CLAIM.log": "f8db33c5b976d635f8b48bf81f85b4901d9704ef94502c516ac88fa1d964cc49",
    "experiments/F112_frozen_two_v_global_root_stress/RUN_MANIFEST.md": "e9eac88c6df2f29a90e9b5d51a7774430b4847fa5d107bb152e1df558f5a994a",
    "experiments/F112_frozen_two_v_global_root_stress/run_with_timeout.py": "1599eae0247456b13491031c7a2fb338b422da45f73c0e79d0ddcc598db52a20",
    "experiments/F112_frozen_two_v_global_root_stress/stress_frozen_two_v.py": "3eb11e927f3b376db890fe46a9b528af1b40229b1cbf83185994dc336e9a4acf",
    "experiments/F113_all_seed_pairs_n46_rescue/DESIGN.md": "53638547a451884c9e10b448362c10dde15962c69aa6bf7e9f72b01bbc4a0b5c",
    "experiments/F113_all_seed_pairs_n46_rescue/FAILED_RUNS.md": "51eaaea476702216bb5cf3c067de2cf8ec8a6aab398577959ae967144d58c857",
    "experiments/F113_all_seed_pairs_n46_rescue/OUTPUT.json": "3a35acf0bc1815e41607b7ac60902b45eb0763bd04b84d77da3e397855f41edb",
    "experiments/F113_all_seed_pairs_n46_rescue/RESULT.md": "2e84a7a9af7ec1180eb21e43195299b7cdb5f6c3b825a40f79cf67fb1107d7a6",
    "experiments/F113_all_seed_pairs_n46_rescue/RUN.log": "1c8538eb1ddd63e39619aedede2f7036c9707b4e8096f7599ec2fbd5214ad4fe",
    "experiments/F113_all_seed_pairs_n46_rescue/RUN_MANIFEST.md": "35d9051a288ae00909e4e276615241231179f71de9a9cac7abdf2037c9aa23b5",
    "experiments/F113_all_seed_pairs_n46_rescue/run_with_timeout.py": "375199b0d4cbcee9b8a514511e09f580f9e86a8e327087c3727424654f960b91",
    "experiments/F113_all_seed_pairs_n46_rescue/test_all_seed_pairs.py": "c254ba6ec5b8bcc1ce816b60865ae0bce0cd9725aee2bdee1144acd03df290ab",
    "experiments/F114_all_seed_pairs_n50_rescue/DESIGN.md": "9c269e4e72473956e7fbacef0dd27632354cf54cdff4c1694a1e584e042912e1",
    "experiments/F114_all_seed_pairs_n50_rescue/FAILED_RUNS.md": "dd69c3396c420aa387260cb706ce51f2a518b4a0f0dc4cfcbe91f959a1c28d5c",
    "experiments/F114_all_seed_pairs_n50_rescue/OUTPUT.json": "e63cd04be683e2f64ad2c49e1ffe2bcb7c8094aa9520a4a299e9def968f6f4f6",
    "experiments/F114_all_seed_pairs_n50_rescue/RESULT.md": "ab3ea8da963d1741a25568c519cf49f4969ea09d94a9829501d6f2da7c5afb0d",
    "experiments/F114_all_seed_pairs_n50_rescue/RUN.log": "6266bfda2cadd379dba1821c7b70d635dd574536a6a25cf341fec7fd19df3f7d",
    "experiments/F114_all_seed_pairs_n50_rescue/RUN_FAILED_20260808T025529Z_EXIT_1.log": "4ad9522199e5c4e6b7227aa7e3fca9282363d4ed17a40194a6936d71b5689516",
    "experiments/F114_all_seed_pairs_n50_rescue/RUN_MANIFEST.md": "0201d5391e88e0ab92c17685ce4c456c52a79fe3dd754068f34de2b44d510295",
    "experiments/F114_all_seed_pairs_n50_rescue/run_with_timeout.py": "3c3ce288bd6c37f1655f6484c9af0f09bae1060862acae6d222db3ee6b1f8eb9",
    "experiments/F114_all_seed_pairs_n50_rescue/test_all_seed_pairs_n50.py": "4ff3be00160bd2a7a7d1a3b5e1245c118b6a8f2219f9b1b63401265b50f25cb5",
}


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


# kind, pair index, u, v, exponent, orientation, seed
Provenance = tuple[str, int, int, int, int, str, int]


class ParityDecoder:
    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.prime_rows: dict[int, int] = {}
        self.pivots: dict[int, tuple[int, int]] = {}
        self.factors: list[dict[int, int]] = []
        self.provenance: list[Provenance] = []
        self.dependencies = 0
        self.global_dependencies = 0
        self.factor: int | None = None
        self.factor_method: str | None = None
        self.factor_support: list[int] | None = None
        self.factor_root: int | None = None
        self.factor_gcds: tuple[int, int] | None = None

    def add(self, factors: dict[int, int], provenance: Provenance) -> None:
        parity = 0
        for prime, exponent in factors.items():
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
        if root in (1, self.modulus - 1):
            self.global_dependencies += 1
            return
        if not (1 < minus < self.modulus or 1 < plus < self.modulus):
            raise AssertionError("non-global square root did not expose a factor")
        self.factor = minus if 1 < minus < self.modulus else plus
        self.factor_method = "retained_parity_dependency"
        self.factor_support = support
        self.factor_root = root
        self.factor_gcds = (minus, plus)


class Batch:
    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.decoder = ParityDecoder(modulus)
        self.cache = FactorCache()
        self.seen: set[int] = set()
        self.residues: list[int] = []
        self.attempted = 0
        self.repeated = 0
        self.direct_witness: dict[str, object] | None = None

    def retain(self, c: int, provenance: Provenance) -> bool:
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
                self.direct_witness = {
                    "c": c,
                    "w": w,
                    "gcd": divisor,
                    "provenance": provenance,
                }
                return True
        relation_factors = dict(self.cache(c))
        for prime, exponent in self.cache(w).items():
            relation_factors[prime] = relation_factors.get(prime, 0) + exponent
        self.decoder.add(relation_factors, provenance)
        self.residues.append(c)
        return self.decoder.factor is not None

    def run_pair(self, u: int, v: int, bound: int, kind: str, pair_index: int) -> bool:
        for exponent in range(bound + 1):
            for orientation, c in (
                ("u_power_times_v", pow(u, exponent, self.modulus) * v % self.modulus),
                ("u_times_v_power", u * pow(v, exponent, self.modulus) % self.modulus),
            ):
                provenance: Provenance = (kind, pair_index, u, v, exponent, orientation, 0)
                if self.retain(c, provenance):
                    return True
        return False

    def compact_provenance(self) -> dict[str, object] | None:
        if self.decoder.factor_method != "retained_parity_dependency":
            return None
        assert self.decoder.factor_support is not None and self.decoder.factor_gcds is not None
        provenances = [self.decoder.provenance[index] for index in self.decoder.factor_support]
        kinds = Counter(provenance[0] for provenance in provenances)
        keys = {
            (provenance[0], provenance[2], provenance[3], provenance[1])
            for provenance in provenances
            if provenance[0] != "initial_seed"
        }
        return {
            "kind_counts": dict(sorted(kinds.items())),
            "distinct_nonseed_trajectory_keys": len(keys),
            "root_mod_N": self.decoder.factor_root,
            "gcd_root_minus_one_N": self.decoder.factor_gcds[0],
            "gcd_root_plus_one_N": self.decoder.factor_gcds[1],
        }

    def support_audit(self, successful_pair: tuple[int, int]) -> dict[str, object]:
        assert self.decoder.factor_support is not None
        provenances = [self.decoder.provenance[index] for index in self.decoder.factor_support]
        nonseed = [provenance for provenance in provenances if provenance[0] != "initial_seed"]
        actual_pair_menus = {(row[0], row[2], row[3]) for row in nonseed}
        indexed_pair_menus = {(row[0], row[2], row[3], row[1]) for row in nonseed}
        orientations = {(row[0], row[2], row[3], row[5]) for row in nonseed}
        appended_pairs = {(row[2], row[3]) for row in nonseed if row[0] == "nonadaptive_seed_pair"}
        successful_count = sum(
            row[0] == "nonadaptive_seed_pair" and (row[2], row[3]) == successful_pair
            for row in provenances
        )
        return {
            "support": len(provenances),
            "kind_counts": dict(sorted(Counter(row[0] for row in provenances).items())),
            "distinct_indexed_pair_menu_keys": len(indexed_pair_menus),
            "distinct_actual_pair_menu_keys": len(actual_pair_menus),
            "distinct_orientation_keys": len(orientations),
            "distinct_appended_pairs": len(appended_pairs),
            "successful_pair_support_relations": successful_count,
            "support_relations_outside_successful_pair": len(provenances) - successful_count,
            "crosses_frozen_and_appended_layers": (
                any(row[0] == "frozen_seed_basis_pair" for row in provenances)
                and any(row[0] == "nonadaptive_seed_pair" for row in provenances)
            ),
        }


def public_supports(seed_records: list[tuple[dict[int, int], dict[int, int]]]) -> list[list[int]]:
    signatures: dict[int, list[tuple[int, int]]] = {}
    for relation, (c_factors, w_factors) in enumerate(seed_records):
        for side, factors in enumerate((c_factors, w_factors)):
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
        common = math.gcd(*(content for _, content in prime_contents))
        block = math.prod(prime ** (content // common) for prime, content in prime_contents)
        blocks.append((block, {endpoint // 2 for endpoint, _ in primitive}))
    blocks.sort(key=lambda item: item[0])
    supports: list[list[int]] = [[] for _ in seed_records]
    for block, relations in blocks:
        for relation in relations:
            supports[relation].append(block)
    return supports


def qualifies(row: dict[str, object]) -> bool:
    result = row.get("result", {})
    roots = result.get("matrix", {}).get("public_kernel_basis_roots", {})
    return (
        result.get("status") == "round_complete"
        and roots.get("basis_size", 0) > 0
        and roots.get("non_global_count") == 0
        and roots.get("global_minus") == 0
        and roots.get("global_plus") == roots.get("basis_size")
    )


def reconstruct_corpus() -> dict[str, object]:
    selected: dict[int, dict[str, object]] = {}
    used_hashes: dict[str, str] = {}
    qualifying_rows = 0
    for path in sorted(F104_DIR.glob("*OUTPUT.json")):
        if path.name == EXCLUDED_F104:
            continue
        data = json.loads(path.read_text())
        if data.get("status") == "running":
            continue
        used = False
        for row in data.get("trace", []):
            if not qualifies(row):
                continue
            used = True
            qualifying_rows += 1
            modulus = int(row["N"])
            p = int(row["p"])
            q = int(row["q"])
            n = modulus.bit_length()
            bound = n * n
            assert p * q == modulus
            assert bool(ZZ(p).is_prime()) and bool(ZZ(q).is_prime())
            assert p > bound and q > bound
            g = math.gcd(p - 1, q - 1)
            assert math.gcd(((p - 1) // g) * ((q - 1) // g), modulus - 1) == 1
            roots = row["result"]["matrix"]["public_kernel_basis_roots"]
            assert row["result"]["matrix"]["nullity"] == roots["basis_size"]
            selected[modulus] = {
                "p": p,
                "q": q,
                "N": modulus,
                "source_file": path.name,
                "first_round_kernel_basis_size": roots["basis_size"],
            }
        if used:
            used_hashes[str(path.relative_to(ROOT))] = sha256(path)

    excluded_path = F104_DIR / EXCLUDED_F104
    excluded = json.loads(excluded_path.read_text())
    excluded_cases = {int(row["N"]) for row in excluded.get("trace", []) if qualifies(row)}
    return {
        "cases": [selected[modulus] for modulus in sorted(selected)],
        "used_hashes": used_hashes,
        "qualifying_rows_before_distinct_dedup": qualifying_rows,
        "duplicate_qualifying_rows": qualifying_rows - len(selected),
        "excluded_running_file": EXCLUDED_F104,
        "excluded_file_status": excluded.get("status"),
        "excluded_qualifying_completed_rows": len(excluded_cases),
        "excluded_overlap_with_selected": len(excluded_cases & set(selected)),
        "excluded_additional_distinct_cases": len(excluded_cases - set(selected)),
    }


def assert_fields(actual: dict[str, object], expected: dict[str, object], fields: tuple[str, ...]) -> None:
    for field in fields:
        assert actual[field] == expected[field], (field, actual[field], expected[field])


def replay_case(
    case: dict[str, object],
    expected_f112: dict[str, object],
    expected_all_pairs: dict[str, object] | None,
) -> tuple[dict[str, object], dict[str, object] | None]:
    p = int(case["p"])
    q = int(case["q"])
    modulus = p * q
    n = modulus.bit_length()
    bound = n * n
    batch = Batch(modulus)
    seed_records: list[tuple[dict[int, int], dict[int, int]]] = []
    for seed in range(2, n + 1):
        provenance: Provenance = ("initial_seed", -1, 0, 0, 0, "", seed)
        assert not batch.retain(seed, provenance)
        inverse = pow(seed, -1, modulus)
        seed_records.append((batch.cache(seed), batch.cache(inverse)))
    initial_records = len(batch.residues)
    supports = public_supports(seed_records)
    frozen_pairs = [
        (support[0], 1) if len(support) == 1 else (support[0], support[1])
        for support in supports
    ]
    for pair_index, (u, v) in enumerate(frozen_pairs):
        assert not batch.run_pair(u, v, bound, "frozen_seed_basis_pair", pair_index)
    first_layer = {
        "initial_records": initial_records,
        "pair_count": len(frozen_pairs),
        "pairs": [list(pair) for pair in frozen_pairs],
        "relations": len(batch.residues),
        "dependencies": batch.decoder.dependencies,
        "global_dependencies": batch.decoder.global_dependencies,
        "all_dependencies_global": batch.decoder.dependencies == batch.decoder.global_dependencies,
    }
    assert first_layer["all_dependencies_global"]

    all_pair_mode = expected_all_pairs is not None
    successful_pair = None
    appended_attempted = 0
    appended_kind = "nonadaptive_seed_pair" if all_pair_mode else "nonadaptive_two_v_pair"
    for v in range(3, n + 1):
        pair_index = appended_attempted
        appended_attempted += 1
        if batch.run_pair(2, v, bound, appended_kind, pair_index):
            successful_pair = [2, v]
            break

    f112_result = {
        **case,
        "n": n,
        "bound": bound,
        "status": "factor" if batch.decoder.factor is not None else "null",
        "factor": batch.decoder.factor,
        "factor_method": batch.decoder.factor_method,
        "factor_dependency_size": len(batch.decoder.factor_support or []) if batch.decoder.factor is not None else None,
        "successful_pair": successful_pair,
        "appended_pairs_attempted": appended_attempted,
        "appended_pair_cap": n - 2,
        "initial_records": initial_records,
        "frozen_pair_count": len(frozen_pairs),
        "first_layer_relations": first_layer["relations"],
        "first_layer_dependencies": first_layer["dependencies"],
        "first_layer_global_dependencies": first_layer["global_dependencies"],
        "relations_at_stop": len(batch.residues),
        "dependencies_at_stop": batch.decoder.dependencies,
        "global_dependencies_at_stop": batch.decoder.global_dependencies,
        "candidate_residues_attempted": batch.attempted,
        "duplicate_residues": batch.repeated,
        "dependency_provenance": batch.compact_provenance(),
    }
    f112_fields = (
        "p", "q", "N", "source_file", "first_round_kernel_basis_size", "n", "bound",
        "status", "factor", "factor_method", "factor_dependency_size", "successful_pair",
        "appended_pairs_attempted", "appended_pair_cap", "initial_records", "frozen_pair_count",
        "first_layer_relations", "first_layer_dependencies", "first_layer_global_dependencies",
        "relations_at_stop", "dependencies_at_stop", "global_dependencies_at_stop",
        "candidate_residues_attempted", "duplicate_residues", "dependency_provenance",
    )
    assert_fields(f112_result, expected_f112, f112_fields)

    summary = {
        "N": modulus,
        "n": n,
        "status": f112_result["status"],
        "factor": f112_result["factor"],
        "factor_method": f112_result["factor_method"],
        "successful_pair": f112_result["successful_pair"],
        "first_round_kernel_basis_size": case["first_round_kernel_basis_size"],
        "candidate_projection_exact_match": True,
    }
    if not all_pair_mode:
        return summary, None

    assert batch.decoder.factor is None
    assert appended_attempted == n - 2
    menu_attempted = appended_attempted
    for u in range(3, n + 1):
        for v in range(u + 1, n + 1):
            pair_index = menu_attempted
            menu_attempted += 1
            if batch.run_pair(u, v, bound, "nonadaptive_seed_pair", pair_index):
                successful_pair = [u, v]
                break
        if batch.decoder.factor is not None:
            break
    assert batch.decoder.factor is not None and successful_pair is not None
    provenance = batch.compact_provenance()
    assert provenance is not None
    all_pair_result = {
        "p": p,
        "q": q,
        "N": modulus,
        "n": n,
        "bound": bound,
        "status": "factor",
        "factor": batch.decoder.factor,
        "factor_method": batch.decoder.factor_method,
        "factor_dependency_size": len(batch.decoder.factor_support or []),
        "first_layer": first_layer,
        "seed_pair_menu_total": (n - 1) * (n - 2) // 2,
        "seed_pair_menu_attempted": menu_attempted,
        "successful_pair": successful_pair,
        "relations_at_stop": len(batch.residues),
        "dependencies_at_stop": batch.decoder.dependencies,
        "global_dependencies_at_stop": batch.decoder.global_dependencies,
        "candidate_residues_attempted": batch.attempted,
        "duplicate_residues": batch.repeated,
        "dependency_provenance": provenance,
    }
    all_pair_fields = (
        "p", "q", "N", "n", "bound", "status", "factor", "factor_method",
        "factor_dependency_size", "first_layer", "seed_pair_menu_total",
        "seed_pair_menu_attempted", "successful_pair", "relations_at_stop",
        "dependencies_at_stop", "global_dependencies_at_stop",
        "candidate_residues_attempted", "duplicate_residues", "dependency_provenance",
    )
    assert_fields(all_pair_result, expected_all_pairs, all_pair_fields)
    support = batch.support_audit(tuple(successful_pair))
    assert support["crosses_frozen_and_appended_layers"]
    assert support["successful_pair_support_relations"] > 0
    assert support["support_relations_outside_successful_pair"] > 0
    assert support["distinct_actual_pair_menu_keys"] > 1
    assert support["distinct_appended_pairs"] > 1
    assert support["distinct_indexed_pair_menu_keys"] == provenance["distinct_nonseed_trajectory_keys"]
    return summary, {
        "N": modulus,
        "n": n,
        "factor": batch.decoder.factor,
        "successful_pair": successful_pair,
        "menu_attempted": menu_attempted,
        "support_audit": support,
        "candidate_projection_exact_match": True,
    }


def main() -> None:
    started = time.monotonic()
    actual_pins = {relative: sha256(ROOT / relative) for relative in CANDIDATE_PINS}
    assert actual_pins == CANDIDATE_PINS
    f112 = json.loads(F112_OUTPUT.read_text())
    f113 = json.loads(F113_OUTPUT.read_text())
    f114 = json.loads(F114_OUTPUT.read_text())
    corpus = reconstruct_corpus()
    cases = corpus.pop("cases")
    assert len(cases) == 100
    assert corpus["qualifying_rows_before_distinct_dedup"] == 101
    assert corpus["duplicate_qualifying_rows"] == 1
    assert corpus["excluded_qualifying_completed_rows"] == 86
    assert corpus["excluded_overlap_with_selected"] == 24
    assert corpus["excluded_additional_distinct_cases"] == 62
    assert corpus["used_hashes"] == f112["input_hashes"]
    expected_f112 = {int(row["N"]): row for row in f112["cases"]}
    assert cases == [
        {
            "p": row["p"],
            "q": row["q"],
            "N": row["N"],
            "source_file": row["source_file"],
            "first_round_kernel_basis_size": row["first_round_kernel_basis_size"],
        }
        for row in f112["cases"]
    ]
    all_pair_candidates = {int(row["N"]): row for row in f113["cases"] + f114["cases"]}
    assert set(all_pair_candidates) == {int(row["N"]) for row in f112["cases"] if row["status"] == "null"}

    f112_replays = []
    all_pair_replays = []
    for ordinal, case in enumerate(cases, 1):
        modulus = int(case["N"])
        summary, all_pair = replay_case(
            case,
            expected_f112[modulus],
            all_pair_candidates.get(modulus),
        )
        f112_replays.append(summary)
        if all_pair is not None:
            all_pair_replays.append(all_pair)
        print(f"completed={ordinal}/100 N={modulus} status={summary['status']}", file=sys.stderr, flush=True)
        gc.collect()

    statuses = Counter(row["status"] for row in f112_replays)
    methods = Counter(row["factor_method"] for row in f112_replays if row["status"] == "factor")
    nulls = [row for row in f112_replays if row["status"] == "null"]
    assert statuses == {"factor": 86, "null": 14}
    assert methods == {"retained_parity_dependency": 67, "direct_endpoint_minus": 12, "direct_endpoint_plus": 7}
    assert Counter(row["n"] for row in nulls) == {46: 7, 50: 7}
    assert len(all_pair_replays) == 14
    assert all(row["candidate_projection_exact_match"] for row in f112_replays + all_pair_replays)

    pair_positions = {
        "unordered_seed_pairs": "(n-1)(n-2)/2",
        "positions_per_pair": "2(n^2+1)",
        "all_pair_positions": "(n-1)(n-2)(n^2+1)",
        "asymptotic_positions": "Theta(n^4)",
        "frozen_first_layer_positions": "2(n-1)(n^2+1) = Theta(n^3)",
    }
    result = {
        "status": "FAIL_AS_WRITTEN_PASS_CORRECTED",
        "verdict": (
            "all per-case finite observations reproduce, but F112's authoritative direct_factor_cases=33 field is false; "
            "the corrected split is 67 parity, 19 direct, 14 null"
        ),
        "independence": {
            "candidate_implementation_imported": False,
            "endpoint_factorization_backend": f"SageMath {SAGE_VERSION} / Pari",
            "all_100_f112_cases_replayed": True,
            "all_14_all_pair_cases_replayed": True,
        },
        "pins": {
            "candidate_artifacts": actual_pins,
            "audit_source_sha256": sha256(Path(__file__).resolve()),
        },
        "corpus": corpus | {
            "selected_distinct_cases": len(cases),
            "candidate_case_list_exact_match": True,
        },
        "f112": {
            "factor_cases": statuses["factor"],
            "null_cases": statuses["null"],
            "parity_factor_cases": methods["retained_parity_dependency"],
            "direct_minus_cases": methods["direct_endpoint_minus"],
            "direct_plus_cases": methods["direct_endpoint_plus"],
            "direct_factor_cases_corrected": methods["direct_endpoint_minus"] + methods["direct_endpoint_plus"],
            "candidate_direct_factor_cases_field": f112["direct_factor_cases"],
            "candidate_direct_factor_cases_field_valid": False,
            "null_bit_lengths": dict(sorted(Counter(row["n"] for row in nulls).items())),
            "cases": f112_replays,
        },
        "all_pairs": {
            "factor_cases": len(all_pair_replays),
            "all_parity_dependencies": all(
                all_pair_candidates[row["N"]]["factor_method"] == "retained_parity_dependency"
                for row in all_pair_replays
            ),
            "all_exact_supports_cross_layers": all(
                row["support_audit"]["crosses_frozen_and_appended_layers"] for row in all_pair_replays
            ),
            "no_exact_support_is_a_single_successful_pair_artifact": all(
                row["support_audit"]["support_relations_outside_successful_pair"] > 0
                and row["support_audit"]["distinct_actual_pair_menu_keys"] > 1
                for row in all_pair_replays
            ),
            "cases": all_pair_replays,
        },
        "source_bound": pair_positions,
        "scope": {
            "factor_assisted_decoder": True,
            "candidate_factors_used_for_corpus_certification_and_result_check": True,
            "fixed_lexicographic_order": True,
            "global_residue_deduplication_first_provenance_wins": True,
            "finite_selected_corpus_only": True,
            "excluded_running_wide_file_has_additional_qualifying_rows": True,
            "factor_free_promotion": False,
        },
        "elapsed_seconds": time.monotonic() - started,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
