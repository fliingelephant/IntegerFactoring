#!/usr/bin/env python3

import argparse
import hashlib
import json
from math import comb, gcd
from pathlib import Path
import time


P14 = {
    "N": 79403,
    "p": 271,
    "q": 293,
    "r": 269,
    "A": 266,
    "hash": "170e8b80ca1c4e6a5f335c376a4a8ebd3c95c782f2b9d74da1d4ab9cd3f997d7",
    "ranks": [23, 266],
    "dets": [0, 30],
    "crt": 71815,
    "gcd": 271,
    "zeros": [65191, 1],
    "nonunits": 65192,
}
P11 = {
    "N": 20000000499999937,
    "p": 100000007,
    "q": 199999991,
    "r": 2953,
    "A": 2942,
    "hash": "85c4bcda5ff5d0f23117721a503fedb77e3a84b9d708a3ceb0f7bed1673c6f53",
    "ranks": [2942, 2942],
    "dets": [56136614, 132391112],
    "crt": 16315256998204520,
    "gcd": 1,
    "zeros": [0, 0],
    "nonunits": 0,
}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def crt_pair(left, right, left_modulus, right_modulus):
    multiplier = ((right - left) * pow(left_modulus, -1, right_modulus)) % right_modulus
    return (left + left_modulus * multiplier) % (left_modulus * right_modulus)


def has_machine_envelope(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 2:
        return False
    try:
        first = json.loads(lines[0])
        last = json.loads(lines[-1])
    except json.JSONDecodeError:
        return False
    return first.get("event") == "start" and last.get("event") == "finish"


def verify_source(record):
    source = Path(record["source"])
    assert source.exists()
    assert sha256(source) == record["source_sha256"]


def verify_status(path, disposition, timed_out, exit_code):
    status = json.loads(path.read_text())
    assert status["disposition"] == disposition
    assert status["timed_out"] is timed_out
    assert status["exit_code"] == exit_code
    log = Path(status["log"])
    assert sha256(log) == status["log_sha256"]
    assert has_machine_envelope(log)
    if disposition == "completed":
        assert status["duration_seconds"] < status["timeout_seconds"]
    if timed_out:
        assert status["duration_seconds"] >= status["timeout_seconds"]
    return status


parser = argparse.ArgumentParser()
parser.add_argument("--p14-fresh", required=True)
parser.add_argument("--p14-status", required=True)
parser.add_argument("--p11-certificate", required=True)
parser.add_argument("--p11-certificate-status", required=True)
parser.add_argument("--p-solve", required=True)
parser.add_argument("--p-solve-status", required=True)
parser.add_argument("--q-solve", required=True)
parser.add_argument("--q-solve-status", required=True)
parser.add_argument("--tail-support", required=True)
parser.add_argument("--tail-support-status", required=True)
parser.add_argument("--a02-status", required=True)
parser.add_argument("--a03-status", required=True)
parser.add_argument("--a04-status", required=True)
parser.add_argument("--reference-root", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
started = time.monotonic()
paths = {
    name: Path(value).resolve()
    for name, value in vars(args).items()
    if name not in ("output", "reference_root")
}
reference_root = Path(args.reference_root).resolve()

statuses = {
    "A01": verify_status(paths["p14_status"], "completed", False, 0),
    "A02": verify_status(paths["a02_status"], "timed_out", True, -15),
    "A03": verify_status(paths["a03_status"], "failed", False, 1),
    "A04": verify_status(paths["a04_status"], "failed", False, 1),
    "A05": verify_status(paths["p11_certificate_status"], "completed", False, 0),
    "A06": verify_status(paths["p_solve_status"], "completed", False, 0),
    "A07": verify_status(paths["q_solve_status"], "completed", False, 0),
    "A08": verify_status(paths["tail_support_status"], "completed", False, 0),
}

p14 = json.loads(paths["p14_fresh"].read_text())
verify_source(p14)
assert p14["inputs"] == {
    "N": P14["N"], "p": P14["p"], "q": P14["q"], "r": P14["r"],
    "shift_start": 1, "shift_stop": P14["A"],
}
assert p14["global_matrix_sha256"] == P14["hash"]
assert p14["raw_global_nonunit_count"] == P14["nonunits"]
assert [p14["local_profiles"][key]["full_matrix_rank"] for key in ("p", "q")] == P14["ranks"]
assert [p14["local_profiles"][key]["canonical_prefix_determinant"] for key in ("p", "q")] == P14["dets"]
assert [p14["local_profiles"][key]["raw_local_zero_count"] for key in ("p", "q")] == P14["zeros"]
assert p14["global_prefix_determinant_mod_N_from_CRT"] == P14["crt"]
assert p14["global_prefix_determinant_gcd_with_N"] == P14["gcd"]
assert crt_pair(*P14["dets"], P14["p"], P14["q"]) == P14["crt"]
assert gcd(P14["crt"], P14["N"]) == P14["gcd"]

reference_files = {
    "P14_p": reference_root / "output" / "R01_P14_mod_271.json",
    "P14_q": reference_root / "output" / "R02_P14_mod_293.json",
    "P14_compare": reference_root / "output" / "R03_P14_comparison.json",
    "P11_p": reference_root / "output" / "R04_P11_mod_100000007.json",
    "P11_q": reference_root / "output" / "R05_P11_mod_199999991.json",
    "P11_compare": reference_root / "output" / "R06_P11_comparison.json",
    "audit": reference_root / "output" / "R07_audit.json",
}
reference = {key: json.loads(path.read_text()) for key, path in reference_files.items()}
for key in ("P14_p", "P14_q", "P14_compare", "P11_p", "P11_q", "P11_compare", "audit"):
    verify_source(reference[key])
assert p14["global_row_sha256"] == reference["P14_p"]["global_row_sha256"]
assert p14["global_row_sha256"] == reference["P14_q"]["global_row_sha256"]
assert reference["P14_compare"]["same_global_matrix_verified"]
assert reference["P14_compare"]["local_ranks"] == P14["ranks"]
assert reference["P14_compare"]["local_prefix_determinants"] == P14["dets"]

certificate = json.loads(paths["p11_certificate"].read_text())
verify_source(certificate)
assert certificate["stage"] == "P11-joint-build-recovery-certificate-v2"
assert certificate["inputs"] == {
    "N": P11["N"], "p": P11["p"], "q": P11["q"], "r": P11["r"],
    "shift_start": 1, "shift_stop": P11["A"],
}
assert certificate["producer_disposition"]["run_id"] == "A03"
assert certificate["producer_disposition"]["mathematical_computation_failure"] is False
assert certificate["failed_v1_certificate"]["run_id"] == "A04"
assert certificate["failed_v1_certificate"]["authoritative"] is False
for item in (certificate["producer_disposition"], certificate["failed_v1_certificate"]):
    assert sha256(Path(item["source"])) == item["source_sha256"]
    assert sha256(Path(item["status"])) == item["status_sha256"]
    assert sha256(Path(item["log"])) == item["log_sha256"]
assert certificate["global_matrix_sha256"] == P11["hash"]
assert certificate["global_row_sha256"] == reference["P11_p"]["global_row_sha256"]
assert certificate["global_row_sha256"] == reference["P11_q"]["global_row_sha256"]
assert certificate["raw_global_nonunit_count"] == P11["nonunits"]
assert certificate["raw_local_zero_counts"] == {"p": 0, "q": 0}
assert certificate["prefix_determinants"] == {"p": P11["dets"][0], "q": P11["dets"][1]}
assert certificate["local_full_ranks"] == {"p": P11["A"], "q": P11["A"]}
assert certificate["lexicographic_column_basis"] == [0, P11["A"] - 1]
assert certificate["global_prefix_determinant_mod_N_from_CRT"] == P11["crt"]
assert certificate["global_prefix_determinant_gcd_with_N"] == P11["gcd"]
assert crt_pair(*P11["dets"], P11["p"], P11["q"]) == P11["crt"]
assert gcd(P11["crt"], P11["N"]) == P11["gcd"]
for key in ("p", "q"):
    artifact = certificate["matrix_artifacts"][key]
    artifact_path = Path(artifact["path"])
    assert artifact_path.stat().st_size == artifact["bytes"]
    assert sha256(artifact_path) == artifact["sha256"]
assert reference["P11_compare"]["same_global_matrix_verified"]
assert reference["P11_compare"]["local_ranks"] == P11["ranks"]
assert reference["P11_compare"]["local_prefix_determinants"] == P11["dets"]

solves = {
    "p": json.loads(paths["p_solve"].read_text()),
    "q": json.loads(paths["q_solve"].read_text()),
}
for key, characteristic, determinant in (
    ("p", P11["p"], P11["dets"][0]),
    ("q", P11["q"], P11["dets"][1]),
):
    solve = solves[key]
    verify_source(solve)
    assert solve["inputs"]["characteristic"] == characteristic
    assert solve["prefix_determinant"] == determinant
    assert solve["normalized_shape"] == [P11["A"], P11["r"] - P11["A"]]
    assert solve["exact_product_verification"]
    assert solve["normalized_zero_positions"] == []
    assert solve["matrix_artifact"]["sha256"] == certificate["matrix_artifacts"][key]["sha256"]
    normalized_path = Path(solve["normalized_artifact"]["path"])
    assert normalized_path.stat().st_size == solve["normalized_artifact"]["bytes"]
    assert sha256(normalized_path) == solve["normalized_artifact"]["sha256"]

tail = json.loads(paths["tail_support"].read_text())
verify_source(tail)
assert tail["one_tail"] == {
    "minor_count_per_field": P11["A"] * 11,
    "p_zero_count": 0,
    "p_zero_q_nonzero_positions": [],
    "q_zero_count": 0,
    "q_zero_p_nonzero_positions": [],
}
assert tail["two_tail"]["tail_pair_count"] == comb(11, 2)
assert tail["two_tail"]["minor_count_per_field"] == comb(11, 2) * comb(P11["A"], 2)
assert tail["two_tail"]["p_zero_q_nonzero_count"] == 0
assert tail["two_tail"]["q_zero_p_nonzero_count"] == 2
assert tail["unscanned_tail_orders"] == [3, 11]
nonzero_pair_summaries = [
    record for record in tail["two_tail"]["tail_pair_summaries"]
    if record["p_zero_q_nonzero_count"] or record["q_zero_p_nonzero_count"]
]
assert nonzero_pair_summaries == [
    {
        "tail_local_indices": [2, 6], "tail_global_columns": [2944, 2948],
        "p_zero_q_nonzero_count": 0, "q_zero_p_nonzero_count": 1,
    },
    {
        "tail_local_indices": [3, 10], "tail_global_columns": [2945, 2952],
        "p_zero_q_nonzero_count": 0, "q_zero_p_nonzero_count": 1,
    },
]
separator = tail["two_tail"]["first_separator"]
assert separator["removed_prefix_columns"] == [423, 2336]
assert separator["tail_local_indices"] == [2, 6]
assert separator["tail_global_columns"] == [2944, 2948]
assert separator["selected_column_count"] == P11["A"]
assert separator["replacement_sign"] == 1
assert separator["zero_field"] == "q"
assert separator["normalized_two_by_two_determinants"] == {"p": 67899852, "q": 0}
assert separator["maximal_minor_formula_determinants"] == {"p": 15564403, "q": 0}
assert separator["maximal_minor_direct_determinants"] == {"p": 15564403, "q": 0}
assert (P11["dets"][0] * 67899852) % P11["p"] == 15564403
assert (P11["dets"][1] * 0) % P11["q"] == 0
separator_crt = crt_pair(15564403, 0, P11["p"], P11["q"])
assert separator_crt == separator["global_maximal_minor_mod_N_from_CRT"] == 2473353088699106
assert gcd(separator_crt, P11["N"]) == separator["global_maximal_minor_gcd_with_N"] == P11["q"]
for key, item in tail["source_artifacts"].items():
    assert sha256(Path(item["path"])) == item["sha256"]

reference_audit = reference["audit"]
for artifact in reference_audit["artifacts"].values():
    artifact_path = Path(artifact["path"])
    assert artifact_path.stat().st_size == artifact["bytes"]
    assert sha256(artifact_path) == artifact["sha256"]
reference_logs = sorted((reference_root / "logs").glob("*.log"))
assert len(reference_logs) == 7
reference_log_envelopes = {str(path): has_machine_envelope(path) for path in reference_logs}
assert not any(reference_log_envelopes.values())
assert not (reference_root / "status").exists()
manifest_text = (reference_root / "RUN_MANIFEST.md").read_text()
assert manifest_text.count("timeout ") >= 7
assert "There were no failed runs" in manifest_text

result = {
    "audit_passed": True,
    "candidate_verdict": "correct for the explicitly listed row-matroid, one-axis prefix, lexicographic-basis, and canonical-prefix-minor profiles; false under any extension to equality of the complete column matroids or maximal Pluecker supports",
    "P14_fresh": {
        "global_matrix_sha256": p14["global_matrix_sha256"],
        "local_ranks": P14["ranks"],
        "prefix_determinants": P14["dets"],
        "prefix_crt": P14["crt"],
        "prefix_gcd": P14["gcd"],
    },
    "P11_fresh": {
        "global_matrix_sha256": certificate["global_matrix_sha256"],
        "all_global_row_hashes_match_both_reference_runs": True,
        "local_ranks": P11["ranks"],
        "prefix_determinants": P11["dets"],
        "prefix_crt": P11["crt"],
        "prefix_gcd": P11["gcd"],
        "all_raw_global_entries_units": True,
        "matrix_artifacts": certificate["matrix_artifacts"],
    },
    "P11_low_tail_Pluecker_scan": {
        "one_tail_minor_count_per_field": tail["one_tail"]["minor_count_per_field"],
        "one_tail_zero_support_mismatches": 0,
        "two_tail_minor_count_per_field": tail["two_tail"]["minor_count_per_field"],
        "two_tail_zero_support_mismatches": 2,
        "explicit_direct_separator": separator,
        "unscanned_tail_orders": tail["unscanned_tail_orders"],
    },
    "invariants_actually_killed_by_P11": [
        "complete row matroid on the 2942 fixed shift rows",
        "all row-prefix ranks",
        "all full-row column-prefix ranks",
        "lexicographically first column basis",
        "the canonical first-2942-column maximal minor zero/nonzero test",
        "raw-entry gcd scan",
    ],
    "not_killed": [
        "complete column matroid (explicitly different)",
        "complete maximal Pluecker support (explicitly different)",
        "the fixed family of all two-tail exchanges from the canonical basis (it factors this P11 input)",
        "two-dimensional prefix-rectangle ranks",
        "maximal minors with 3 through 11 tail columns",
        "a uniform theorem for a richer globally computable minor family",
    ],
    "failed_runs_retained_and_non_authoritative": {
        run_id: {
            "disposition": statuses[run_id]["disposition"],
            "timed_out": statuses[run_id]["timed_out"],
            "exit_code": statuses[run_id]["exit_code"],
            "status": str({"A02": paths["a02_status"], "A03": paths["a03_status"], "A04": paths["a04_status"]}[run_id]),
        }
        for run_id in ("A02", "A03", "A04")
    },
    "reference_timeout_provenance": {
        "manifest_names_timeout_commands_and_exit_zero": True,
        "retained_per_run_status_artifacts": False,
        "retained_logs_with_machine_readable_start_finish_envelopes": False,
        "conclusion": "the numerical artifacts are reproducible, but the retained candidate artifacts do not independently prove that the manifest timeout wrappers ran or exited as stated",
        "log_envelopes": reference_log_envelopes,
    },
    "authoritative_fresh_runs": {
        run_id: {
            "disposition": statuses[run_id]["disposition"],
            "timeout_seconds": statuses[run_id]["timeout_seconds"],
            "duration_seconds": statuses[run_id]["duration_seconds"],
            "log_sha256": statuses[run_id]["log_sha256"],
        }
        for run_id in ("A01", "A05", "A06", "A07", "A08")
    },
    "artifact_sha256": {str(path): sha256(path) for path in paths.values()},
    "source": str(Path(__file__).resolve()),
    "source_sha256": sha256(Path(__file__).resolve()),
    "elapsed_seconds": time.monotonic() - started,
}
output_path = Path(args.output).resolve()
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "audit_passed": result["audit_passed"],
    "candidate_verdict": result["candidate_verdict"],
    "P14": result["P14_fresh"],
    "P11_separator": result["P11_low_tail_Pluecker_scan"]["explicit_direct_separator"],
    "elapsed_seconds": result["elapsed_seconds"],
}, sort_keys=True))
