#!/usr/bin/env python3
"""Registered semantic comparison of F165-D01 and F165-R04 sequences.

This source does not import or execute either F165 implementation. It reads
their frozen outputs, translates the richer R04 transcript into the sequence
semantics committed by D01, and checks the complete ordered corpus and every
base/level snapshot. It also reconstructs ledger metadata, feedback
candidates, parity decompositions, and deterministic selected-column bases
from the published R04 transcript.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
from typing import Any


EXPERIMENT_ID = "F165-R05"
EXPECTED_INPUT_SHA256 = {
    "search.py": "2a7852f8438003f0db1dd49b7721d02ae2c1cfcea8b114f1e58cc69b74f04427",
    "OUTPUT.json": "94ca36ee995819d384e260d50213105b58c3b91377b3a8e51ba155fa7b218dcc",
    "RESULT.md": "04ff14f6f0664073565c36370308c610569518f84fbd005b8ad3f835edd717d3",
    "MANIFEST.md": "df609f058087c0632e48f2d88192c8abca9d59032d8ad008ca1d74e9dbf8c50c",
    "V2_BLIND_STATEMENT.md": "1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd",
    "f165_r04_v2_blind_reconstruct.py": "a3b1a94440d3e6e580bccc6efe189a73a86adc366c4e617acc06a5a56377b42f",
    "f165_r04_v2_blind_output.json": "f29dddd1893c81cde798425cacc40da0c619b1260a9763793973bb016881a56d",
    "f165_r04_v2_blind_run.log": "da45648fe4dc2aaa8299564d2c85b47be3369e79d6c9d74e40aebed2944f8a9c",
    "F165_R04_BLIND_RECONSTRUCTION.md": "dfcf023c8d9a011e758bdb36183b3351083ffc78bb98197f08b196ef18a5c321",
    "F165_R04_V2_FIXED_DEPTH_PROOF_DRAFT.md": "39a36e862162d405d15943f59995010c1471e6af8baef6e2b7b9d7f984a9b380",
}
SEQUENCE_NAMES = ("candidate", "exact_value", "block", "selected_column")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def d01_unsigned_bytes(value: int) -> bytes:
    if value < 0:
        raise ValueError("D01 sequence integers must be nonnegative")
    size = max(1, (value.bit_length() + 7) // 8)
    return value.to_bytes(size, "big")


def d01_integer_sequence_hash(values: list[int]) -> str:
    digest = hashlib.sha256()
    for value in values:
        encoded = d01_unsigned_bytes(value)
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
    digest.update(len(values).to_bytes(8, "big"))
    return digest.hexdigest()


def d01_candidate_hash(candidates: list[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for candidate in candidates:
        support = candidate["basis_support"]
        payload = [
            len(support),
            support[0] + 1,
            support[1] + 1 if len(support) == 2 else 0,
            candidate["z"],
            candidate["w"],
            candidate["A"],
            candidate["gcd_minus"],
            candidate["gcd_plus"],
        ]
        for value in payload:
            encoded = d01_unsigned_bytes(value)
            digest.update(len(encoded).to_bytes(8, "big"))
            digest.update(encoded)
    return digest.hexdigest()


def r04_unsigned_bytes(value: int) -> bytes:
    if value < 0:
        raise ValueError("R04 canonical integers must be nonnegative")
    return value.to_bytes((value.bit_length() + 7) // 8, "big")


def r04_canonical_bytes(value: Any) -> bytes:
    if value is None:
        return b"N"
    if value is True:
        return b"T"
    if value is False:
        return b"F"
    if isinstance(value, int):
        encoded = r04_unsigned_bytes(value)
        return b"I" + len(encoded).to_bytes(8, "big") + encoded
    if isinstance(value, str):
        encoded = value.encode("utf-8")
        return b"S" + len(encoded).to_bytes(8, "big") + encoded
    if isinstance(value, (list, tuple)):
        return (
            b"L"
            + len(value).to_bytes(8, "big")
            + b"".join(r04_canonical_bytes(item) for item in value)
        )
    if isinstance(value, dict):
        keys = sorted(value)
        return (
            b"D"
            + len(keys).to_bytes(8, "big")
            + b"".join(
                r04_canonical_bytes(key) + r04_canonical_bytes(value[key])
                for key in keys
            )
        )
    raise TypeError(type(value).__name__)


def r04_sequence_hash(sequence: Any) -> str:
    return hashlib.sha256(r04_canonical_bytes(sequence)).hexdigest()


def integer_nth_root(value: int, exponent: int) -> int:
    low = 1
    high = 1 << ((value.bit_length() + exponent - 1) // exponent)
    while low + 1 < high:
        middle = (low + high) // 2
        if pow(middle, exponent) <= value:
            low = middle
        else:
            high = middle
    return low


def is_perfect_power(value: int) -> bool:
    for exponent in range(2, value.bit_length() + 1):
        root = integer_nth_root(value, exponent)
        if pow(root, exponent) == value:
            return True
    return False


class Audit:
    def __init__(self) -> None:
        self.counts: Counter[str] = Counter()
        self.examples: list[dict[str, Any]] = []

    def equal(self, category: str, path: str, expected: Any, actual: Any) -> None:
        if expected == actual:
            return
        self.counts[category] += 1
        if len(self.examples) < 128:
            self.examples.append(
                {
                    "category": category,
                    "path": path,
                    "expected": expected,
                    "actual": actual,
                }
            )

    def true(self, category: str, path: str, condition: bool, actual: Any) -> None:
        if condition:
            return
        self.counts[category] += 1
        if len(self.examples) < 128:
            self.examples.append(
                {
                    "category": category,
                    "path": path,
                    "expected": True,
                    "actual": actual,
                }
            )


def compare_entries(
    audit: Audit,
    category: str,
    path: str,
    expected: list[Any],
    actual: list[Any],
) -> None:
    audit.equal(category, f"{path}.length", len(expected), len(actual))
    for index, (expected_item, actual_item) in enumerate(zip(expected, actual)):
        audit.equal(category, f"{path}[{index}]", expected_item, actual_item)


def expected_selected_sequence(
    audit: Audit,
    path: str,
    modulus: int,
    ledger: list[dict[str, Any]],
    blocks: list[int],
) -> list[dict[str, Any]]:
    for index, block in enumerate(blocks):
        audit.true(
            "block_semantics",
            f"{path}.blocks[{index}].greater_than_one",
            block > 1,
            block,
        )
        audit.true(
            "block_semantics",
            f"{path}.blocks[{index}].unit_mod_N",
            math.gcd(block, modulus) == 1,
            math.gcd(block, modulus),
        )
        audit.true(
            "block_semantics",
            f"{path}.blocks[{index}].not_perfect_power",
            not is_perfect_power(block),
            block,
        )
        for right, other in enumerate(blocks[index + 1 :], start=index + 1):
            common = math.gcd(block, other)
            audit.true(
                "block_semantics",
                f"{path}.blocks[{index},{right}].coprime",
                common == 1,
                common,
            )

    columns: list[dict[str, Any]] = []
    for record_index, record in enumerate(ledger):
        value = record["A"]
        if value <= 1:
            continue
        bits = 0
        parity_blocks: list[int] = []
        parity_product = 1
        for row, block in enumerate(blocks):
            remainder = value
            exponent = 0
            while remainder % block == 0:
                remainder //= block
                exponent += 1
            if exponent % 2:
                bits |= 1 << row
                parity_blocks.append(block)
                parity_product *= block
        quotient, remainder = divmod(value, parity_product)
        square_part = math.isqrt(quotient)
        audit.true(
            "selected_semantics",
            f"{path}.record[{record_index}].parity_divides_A",
            remainder == 0,
            remainder,
        )
        audit.true(
            "selected_semantics",
            f"{path}.record[{record_index}].square_quotient",
            square_part * square_part == quotient,
            quotient,
        )
        lift = record["root"] * pow(square_part, -1, modulus) % modulus
        audit.equal(
            "selected_semantics",
            f"{path}.record[{record_index}].lift_square",
            parity_product % modulus,
            pow(lift, 2, modulus),
        )
        columns.append(
            {
                "record_index": record_index,
                "A": value,
                "bits": bits,
                "parity_blocks": parity_blocks,
                "square_part": square_part,
                "lift": lift,
            }
        )

    pivots: dict[int, int] = {}
    selected: list[dict[str, Any]] = []
    for column in columns:
        vector = column["bits"]
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = vector
                selected.append(
                    {
                        "basis_index": len(selected),
                        "record_index": column["record_index"],
                        "A": column["A"],
                        "parity_blocks": column["parity_blocks"],
                        "square_part": column["square_part"],
                        "lift": column["lift"],
                    }
                )
                break
            vector ^= pivots[pivot]
    return selected


def expected_feedback_candidates(
    audit: Audit,
    path: str,
    modulus: int,
    level: int,
    basis: list[dict[str, Any]],
    ledger: list[dict[str, Any]],
    record_by_value: dict[int, int],
) -> list[dict[str, Any]]:
    supports = [(index,) for index in range(len(basis))]
    supports.extend(
        (left, right)
        for left in range(len(basis))
        for right in range(left + 1, len(basis))
    )
    candidates: list[dict[str, Any]] = []
    layer = f"level_{level}"
    for attempt_index, support in enumerate(supports):
        if len(support) == 1:
            residue = basis[support[0]]["lift"]
        else:
            left = basis[support[0]]
            right = basis[support[1]]
            residue = left["lift"] * right["lift"] % modulus
            common_blocks = sorted(
                set(left["parity_blocks"]).intersection(right["parity_blocks"])
            )
            for block in common_blocks:
                residue = residue * pow(block, -1, modulus) % modulus
        inverse = pow(residue, -1, modulus)
        value = residue * inverse
        gcd_minus = math.gcd(residue - inverse, modulus)
        gcd_plus = math.gcd(residue + inverse, modulus)
        old_index = record_by_value.get(value)
        if old_index is None:
            disposition = "new"
            duplicate_status = None
            record_by_value[value] = len(ledger)
            ledger.append(
                {
                    "A": value,
                    "root": 1,
                    "occurrences": 1,
                    "first_layer": layer,
                    "layer_counts": {layer: 1},
                }
            )
        else:
            disposition = "duplicate"
            old = ledger[old_index]
            ratio = pow(old["root"], -1, modulus)
            duplicate_status = (
                "global_plus"
                if ratio == 1
                else "global_minus"
                if ratio == modulus - 1
                else "non_global"
            )
            old["occurrences"] += 1
            old["layer_counts"][layer] = old["layer_counts"].get(layer, 0) + 1
        candidate = {
            "attempt_index": attempt_index,
            "basis_support": list(support),
            "record_indices": [basis[index]["record_index"] for index in support],
            "z": residue,
            "w": inverse,
            "A": value,
            "gcd_minus": gcd_minus,
            "gcd_plus": gcd_plus,
            "disposition": disposition,
            "duplicate_ratio_status": duplicate_status,
        }
        audit.true(
            "candidate_semantics",
            f"{path}.candidate[{attempt_index}].relation_mod_N",
            value % modulus == 1,
            value % modulus,
        )
        candidates.append(candidate)
    return candidates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    if args.output.exists():
        raise SystemExit(f"refusing to overwrite output: {args.output}")

    observed_inputs = {
        name: sha256_file(directory / name) for name in EXPECTED_INPUT_SHA256
    }
    if observed_inputs != EXPECTED_INPUT_SHA256:
        payload = {
            "experiment_id": EXPERIMENT_ID,
            "status": "FAIL",
            "first_mismatch": {
                "category": "frozen_input_hash",
                "path": "EXPECTED_INPUT_SHA256",
                "expected": EXPECTED_INPUT_SHA256,
                "actual": observed_inputs,
            },
        }
        with args.output.open("x", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
        return 1

    d01 = json.loads((directory / "OUTPUT.json").read_text())
    r04 = json.loads((directory / "f165_r04_v2_blind_output.json").read_text())
    audit = Audit()
    audit.equal("artifact_status", "D01.status", "PASS", d01.get("status"))
    audit.equal(
        "artifact_status",
        "R04.replay_status",
        "STATED_FINITE_CLAIMS_MATCH",
        r04.get("replay_status"),
    )
    audit.equal(
        "corpus",
        "corpus_sha256",
        d01.get("corpus_sha256"),
        r04.get("corpus_sha256"),
    )
    audit.equal("corpus", "pairs", d01.get("corpus_pairs"), r04.get("pairs"))
    d01_instances = d01["instances"]
    r04_instances = r04["results"]
    audit.equal("corpus", "instance_count", len(d01_instances), len(r04_instances))

    comparison_counts: Counter[str] = Counter()
    normalized: dict[str, list[Any]] = {name: [] for name in SEQUENCE_NAMES}
    r04_stages: list[tuple[int, str, dict[str, Any]]] = []

    for corpus_index, (d01_entry, r04_entry) in enumerate(
        zip(d01_instances, r04_instances)
    ):
        d01_public = d01_entry["public"]
        modulus = d01_public["N"]
        prefix = f"instances[{corpus_index}].N={modulus}"
        audit.equal("corpus", f"{prefix}.corpus_index", corpus_index, d01_entry["corpus_index"])
        audit.equal("corpus", f"{prefix}.R04.N", modulus, r04_entry["N"])
        audit.equal("corpus", f"{prefix}.n", d01_public["base"]["n"], r04_entry["n"])

        ledger: list[dict[str, Any]] = []
        record_by_value: dict[int, int] = {}
        expected_base_candidates: list[dict[str, Any]] = []
        for candidate_index, c in enumerate(range(2, r04_entry["n"] + 2)):
            unit_gcd = math.gcd(c, modulus)
            audit.equal(
                "candidate_semantics",
                f"{prefix}.base.c={c}.unit_gcd",
                1,
                unit_gcd,
            )
            inverse = pow(c, -1, modulus)
            value = c * inverse
            old_index = record_by_value.get(value)
            if old_index is None:
                disposition = "new"
                duplicate_status = None
                record_by_value[value] = len(ledger)
                ledger.append(
                    {
                        "A": value,
                        "root": 1,
                        "occurrences": 1,
                        "first_layer": "base",
                        "layer_counts": {"base": 1},
                    }
                )
            else:
                disposition = "duplicate"
                duplicate_status = "global_plus"
                ledger[old_index]["occurrences"] += 1
                ledger[old_index]["layer_counts"]["base"] += 1
            expected_base_candidates.append(
                {
                    "candidate_index": candidate_index,
                    "c": c,
                    "w": inverse,
                    "A": value,
                    "root": 1,
                    "disposition": disposition,
                    "duplicate_ratio_status": duplicate_status,
                }
            )

        stages = [
            (
                "base",
                d01_public["base"]["decoder"],
                r04_entry["base"],
                expected_base_candidates,
            )
        ]
        previous_selected: list[dict[str, Any]] | None = None
        for stage_index in range(3):
            if stage_index > 0:
                level = stage_index
                expected_candidates = expected_feedback_candidates(
                    audit,
                    f"{prefix}.level_{level}",
                    modulus,
                    level,
                    previous_selected or [],
                    ledger,
                    record_by_value,
                )
                stages.append(
                    (
                        f"level_{level}",
                        d01_public["levels"][level - 1]["union_decoder"],
                        r04_entry["levels"][level - 1],
                        expected_candidates,
                    )
                )

            stage_name, d01_summary, r04_summary, expected_candidates = stages[stage_index]
            stage_path = f"{prefix}.{stage_name}"
            snapshot = r04_summary["snapshot"]
            r04_stages.append((modulus, stage_name, snapshot))
            sequences = snapshot["sequences"]
            compare_entries(
                audit,
                "candidate_sequence",
                f"{stage_path}.candidate",
                expected_candidates,
                sequences["candidate"],
            )
            comparison_counts["candidate_entries"] += len(expected_candidates)

            expected_exact = [
                {
                    "record_index": index,
                    "A": record["A"],
                    "root": record["root"],
                    "occurrences": record["occurrences"],
                    "first_layer": record["first_layer"],
                    "layer_counts": dict(record["layer_counts"]),
                }
                for index, record in enumerate(ledger)
            ]
            compare_entries(
                audit,
                "exact_value_sequence",
                f"{stage_path}.exact_value",
                expected_exact,
                sequences["exact_value"],
            )
            comparison_counts["exact_value_entries"] += len(expected_exact)
            blocks = sequences["block"]
            comparison_counts["block_entries"] += len(blocks)
            expected_selected = expected_selected_sequence(
                audit, stage_path, modulus, ledger, blocks
            )
            compare_entries(
                audit,
                "selected_column_sequence",
                f"{stage_path}.selected_column",
                expected_selected,
                sequences["selected_column"],
            )
            comparison_counts["selected_column_entries"] += len(expected_selected)
            previous_selected = expected_selected

            for name in SEQUENCE_NAMES:
                audit.equal(
                    "r04_hash_integrity",
                    f"{stage_path}.hashes.{name}",
                    r04_sequence_hash(sequences[name]),
                    snapshot["hashes"][name],
                )
            value_only = {
                "candidate": [item["A"] for item in sequences["candidate"]],
                "exact_value": [item["A"] for item in sequences["exact_value"]],
                "block": list(blocks),
                "selected_column": [
                    item["A"] for item in sequences["selected_column"]
                ],
            }
            for name in SEQUENCE_NAMES:
                audit.equal(
                    "r04_hash_integrity",
                    f"{stage_path}.value_only_hashes.{name}",
                    r04_sequence_hash(value_only[name]),
                    snapshot["value_only_hashes"][name],
                )

            if stage_name != "base":
                d01_level = d01_public["levels"][stage_index - 1]
                audit.equal(
                    "candidate_sequence",
                    f"{stage_path}.D01_candidate_sha256",
                    d01_candidate_hash(expected_candidates),
                    d01_level["candidate_sha256"],
                )
                comparison_counts["D01_candidate_hashes"] += 1
            exact_values = [record["A"] for record in ledger]
            audit.equal(
                "exact_value_sequence",
                f"{stage_path}.D01_exact_value_sha256",
                d01_integer_sequence_hash(exact_values),
                d01_summary["exact_value_sha256"],
            )
            audit.equal(
                "block_sequence",
                f"{stage_path}.D01_block_sha256",
                d01_integer_sequence_hash(blocks),
                d01_summary["block_sha256"],
            )
            selected_indices = [item["record_index"] for item in expected_selected]
            audit.equal(
                "selected_column_sequence",
                f"{stage_path}.D01_selected_column_sha256",
                d01_integer_sequence_hash(selected_indices),
                d01_summary["selected_column_sha256"],
            )
            comparison_counts["D01_exact_value_hashes"] += 1
            comparison_counts["D01_block_hashes"] += 1
            comparison_counts["D01_selected_column_hashes"] += 1

            active_columns = sum(record["A"] > 1 for record in ledger)
            r04_status = r04_summary["normalized_root_status"]
            audit.equal(
                "decoder_summary",
                f"{stage_path}.rows",
                d01_summary["rows"],
                r04_summary["rows"],
            )
            audit.equal(
                "decoder_summary",
                f"{stage_path}.columns",
                d01_summary["columns"],
                r04_summary["columns"],
            )
            audit.equal(
                "decoder_summary",
                f"{stage_path}.R04_active_columns",
                active_columns,
                r04_summary["columns"],
            )
            audit.equal(
                "decoder_summary",
                f"{stage_path}.rank",
                d01_summary["rank"],
                r04_summary["rank"],
            )
            audit.equal(
                "decoder_summary",
                f"{stage_path}.nullity",
                d01_summary["nullity"],
                r04_summary["nullity"],
            )
            audit.equal(
                "decoder_summary",
                f"{stage_path}.global_plus",
                d01_summary["global_plus_elimination_roots"],
                r04_status["global_plus"],
            )
            audit.equal(
                "decoder_summary",
                f"{stage_path}.global_minus",
                d01_summary["global_minus_elimination_roots"],
                r04_status["global_minus"],
            )
            audit.equal(
                "decoder_summary",
                f"{stage_path}.non_global",
                d01_summary["non_global_elimination_roots"],
                r04_status["non_global"],
            )
            audit.equal(
                "decoder_summary",
                f"{stage_path}.selected_basis_columns",
                d01_summary["selected_basis_columns"],
                len(expected_selected),
            )
            normalized["candidate"].append([modulus, stage_name, expected_candidates])
            normalized["exact_value"].append([modulus, stage_name, expected_exact])
            normalized["block"].append([modulus, stage_name, blocks])
            normalized["selected_column"].append(
                [modulus, stage_name, expected_selected]
            )

    for name in SEQUENCE_NAMES:
        expected_aggregate = r04_sequence_hash(
            [
                [modulus, stage, snapshot["sequences"][name]]
                for modulus, stage, snapshot in r04_stages
            ]
        )
        audit.equal(
            "r04_hash_integrity",
            f"aggregate_sequence_hashes.{name}",
            expected_aggregate,
            r04["aggregate_sequence_hashes"][name],
        )
        expected_value_only = r04_sequence_hash(
            [
                [modulus, stage, snapshot["value_only_hashes"][name]]
                for modulus, stage, snapshot in r04_stages
            ]
        )
        audit.equal(
            "r04_hash_integrity",
            f"aggregate_value_only_hashes.{name}",
            expected_value_only,
            r04["aggregate_value_only_hashes"][name],
        )

    mismatch_total = sum(audit.counts.values())
    payload = {
        "experiment_id": EXPERIMENT_ID,
        "status": "PASS" if mismatch_total == 0 else "FAIL",
        "claim_scope": (
            "semantic equality of the complete ordered D01/R04 candidate, "
            "exact-value, block, and selected-column sequences, plus adjacent "
            "decoder-summary consistency; finite artifacts only"
        ),
        "frozen_input_sha256": observed_inputs,
        "instances_compared": min(len(d01_instances), len(r04_instances)),
        "stages_compared": len(r04_stages),
        "comparison_counts": dict(comparison_counts),
        "normalized_sequence_sha256": {
            name: r04_sequence_hash(sequence) for name, sequence in normalized.items()
        },
        "mismatch_total": mismatch_total,
        "mismatch_counts": dict(audit.counts),
        "first_mismatch": audit.examples[0] if audit.examples else None,
        "mismatch_examples": audit.examples,
        "limitations": [
            "Cryptographic equality checks the frozen finite transcripts only.",
            "This run proves no unbounded success or complexity theorem.",
            "The fixed-depth proof is audited separately from this computation.",
        ],
    }
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(
        json.dumps(
            {
                "event": "comparison_complete",
                "status": payload["status"],
                "mismatch_total": mismatch_total,
                "first_mismatch": payload["first_mismatch"],
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return int(mismatch_total != 0)


if __name__ == "__main__":
    raise SystemExit(main())
