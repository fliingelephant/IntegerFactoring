#!/usr/bin/env python3
"""Run the five remaining registered F116 cases under per-case hard timeouts."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / "stress_sparse_dag_registered_case.py"
OUTPUT = HERE / "SPARSE_DAG_REMAINING_OUTPUT.json"
LOG = HERE / "SPARSE_DAG_REMAINING_RUN.log"
TIMEOUT_SECONDS = 600
CASES = [
    (4, 80_000_069, 159_999_941),
    (6, 80_000_087, 159_999_907),
    (7, 80_000_111, 159_999_899),
    (9, 80_000_153, 159_999_881),
    (13, 80_000_273, 159_999_761),
]


def main() -> int:
    prior_output = HERE / "SPARSE_DAG_REMAINING_OUTPUT_FAILED_20260808T045242Z_ENV.json"
    prior_log = HERE / "SPARSE_DAG_REMAINING_RUN_FAILED_20260808T045242Z_ENV.log"
    if (
        OUTPUT.exists()
        and json.loads(OUTPUT.read_text()).get("status") == "FAIL"
        and not prior_output.exists()
    ):
        OUTPUT.replace(prior_output)
        if LOG.exists():
            LOG.replace(prior_log)

    started_all = time.monotonic()
    summaries: list[dict[str, object]] = []
    log_sections: list[str] = []
    overall_pass = True
    for ordinal, p, q in CASES:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        attempt = HERE / f"SPARSE_DAG_CASE_{ordinal:02d}_ATTEMPT_{stamp}.json"
        final = HERE / f"SPARSE_DAG_CASE_{ordinal:02d}_OUTPUT.json"
        command = [
            "/usr/local/bin/sage",
            "-python",
            str(SOURCE),
            "--ordinal",
            str(ordinal),
            "--p",
            str(p),
            "--q",
            str(q),
            "--output",
            str(attempt),
        ]
        started = time.monotonic()
        environment = os.environ.copy()
        environment["DOT_SAGE"] = str(HERE / ".sage_runtime")
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        try:
            completed = subprocess.run(
                command,
                cwd=ROOT,
                env=environment,
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                check=False,
            )
            elapsed = time.monotonic() - started
            timed_out = False
            stdout = completed.stdout
            stderr = completed.stderr
            returncode = completed.returncode
        except subprocess.TimeoutExpired as error:
            elapsed = time.monotonic() - started
            timed_out = True
            stdout = error.stdout or ""
            stderr = error.stderr or ""
            returncode = 124

        parsed = json.loads(attempt.read_text()) if attempt.exists() else {"status": "NO_OUTPUT"}
        passed = not timed_out and returncode == 0 and parsed.get("status") == "PASS"
        summary: dict[str, object] = {
            "ordinal": ordinal,
            "p": p,
            "q": q,
            "N": p * q,
            "hard_timeout_seconds": TIMEOUT_SECONDS,
            "elapsed_seconds": elapsed,
            "timed_out": timed_out,
            "returncode": returncode,
            "status": "PASS" if passed else "FAIL",
        }
        if passed:
            attempt.replace(final)
            summary.update({
                "output": final.name,
                "output_sha256": hashlib.sha256(final.read_bytes()).hexdigest(),
                "successful_pair": parsed["menu"]["successful_pair"],
                "attempted_pairs": parsed["menu"]["attempted_pairs"],
                "retained_relations": parsed["source_at_stop"]["retained_relations"],
                "support_size": parsed["factor_free_support_replay"]["support_size"],
                "root_mod_N": parsed["factor_free_support_replay"]["root_mod_N"],
                "gcd_root_minus_one_N": parsed["factor_free_support_replay"]["gcd_root_minus_one_N"],
                "gcd_root_plus_one_N": parsed["factor_free_support_replay"]["gcd_root_plus_one_N"],
            })
        else:
            overall_pass = False
            reason = "TIMEOUT" if timed_out else f"EXIT_{returncode}"
            failed_output = HERE / f"SPARSE_DAG_CASE_{ordinal:02d}_FAILED_{stamp}_{reason}.json"
            failed_output.write_text(attempt.read_text() if attempt.exists() else json.dumps(parsed) + "\n")
            if attempt.exists():
                attempt.unlink()
            summary["failed_output"] = failed_output.name
            summary["failed_output_sha256"] = hashlib.sha256(failed_output.read_bytes()).hexdigest()
        summaries.append(summary)
        log_sections.append(
            f"ordinal={ordinal}\ncommand={json.dumps(command)}\n"
            f"timeout_seconds={TIMEOUT_SECONDS}\nelapsed_seconds={elapsed:.6f}\n"
            f"timed_out={str(timed_out).lower()}\nreturncode={returncode}\n"
            f"stdout:\n{stdout}\nstderr:\n{stderr}\n"
        )

    result = {
        "status": "PASS" if overall_pass else "FAIL",
        "role": "factor-assisted completion of the preregistered F116 corpus",
        "source": SOURCE.name,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "hard_timeout_seconds_per_case": TIMEOUT_SECONDS,
        "case_count": len(CASES),
        "factor_cases": sum(row["status"] == "PASS" for row in summaries),
        "null_or_failed_cases": [row["N"] for row in summaries if row["status"] != "PASS"],
        "cases": summaries,
        "elapsed_seconds": time.monotonic() - started_all,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    LOG.write_text("\n".join(log_sections))
    print(json.dumps({
        "status": result["status"],
        "factor_cases": result["factor_cases"],
        "null_or_failed_cases": result["null_or_failed_cases"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, sort_keys=True))
    return 0 if overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
