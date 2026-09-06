#!/usr/bin/env python3
"""Frozen sequential 600-second runner for F165-R06."""

from __future__ import annotations

import hashlib
import os
import signal
import subprocess
import sys
import time
from pathlib import Path


TIMEOUT_SECONDS = 600
FROZEN_SHA256 = {
    "search.py": "2a7852f8438003f0db1dd49b7721d02ae2c1cfcea8b114f1e58cc69b74f04427",
    "OUTPUT.json": "94ca36ee995819d384e260d50213105b58c3b91377b3a8e51ba155fa7b218dcc",
    "RESULT.md": "04ff14f6f0664073565c36370308c610569518f84fbd005b8ad3f835edd717d3",
    "MANIFEST.md": "df609f058087c0632e48f2d88192c8abca9d59032d8ad008ca1d74e9dbf8c50c",
    "V2_BLIND_STATEMENT.md": "1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd",
    "f165_r04_v2_blind_reconstruct.py": "a3b1a94440d3e6e580bccc6efe189a73a86adc366c4e617acc06a5a56377b42f",
    "f165_r04_v2_blind_timeout_runner.py": "0c539e36369d308c71d96b09cd4aac60fcc908cf801d7044631306c75f6d301b",
    "f165_r04_v2_blind_output.json": "f29dddd1893c81cde798425cacc40da0c619b1260a9763793973bb016881a56d",
    "f165_r04_v2_blind_run.log": "da45648fe4dc2aaa8299564d2c85b47be3369e79d6c9d74e40aebed2944f8a9c",
    "F165_R04_BLIND_RECONSTRUCTION.md": "dfcf023c8d9a011e758bdb36183b3351083ffc78bb98197f08b196ef18a5c321",
    "F165_R04_V2_FIXED_DEPTH_PROOF_DRAFT.md": "39a36e862162d405d15943f59995010c1471e6af8baef6e2b7b9d7f984a9b380",
    "f165_r05_sequence_compare.py": "2dcb4e871b890c16c575f2c0168295c757e40187b514a0d1c223a7034f85e397",
    "f165_r05_sequence_compare_timeout_runner.py": "477fb932338c873cdb60f1ffd5fab576bd75592e8db260d343f0ad1a3ca5c1a4",
    "F165_R05_SEQUENCE_COMPARISON_PREREGISTRATION_DRAFT.md": "92d0a3e49df9967598c8c512a1edbff3ed8720b91bd8cd1b0e502948eb058bfd",
    "f165_r05_sequence_compare_output.json": "9b61f73aa8b860ae6741b868edc1acaf309ce57f75e895c8a71dc3b637fba080",
    "f165_r05_sequence_compare_run.log": "efa73913905e03c2b89c330eee8aa6103c8c5d64506f21c1a57b4645b28211b1",
    "F165_R05_SEQUENCE_COMPARISON_FAILURE.md": "ef36a2c90a556d6d917ac9087c066487ca51fd3161a7b6b1bdf67d4431d0cc97",
    "f165_r06_v2_reconstruct.py": "252123931d35856febfd93c07c8e22072564bf6310d75093d5eb169a07f09838",
    "f165_r06_sequence_compare.py": "fa2742f2562f2288f7c93114fb4f02d1a6691ab920c46b62fbae23dfd4285c7b",
    "F165_R06_EXPECTED_OUTPUTS.json": "f4b066fbb1580a67846538c2381e9b7a377ad00225b9116fa3aaffa709eb1c68",
    "F165_R06_SOURCE_PROVENANCE.md": "14e0f62f90205f5a26f9215cdc175b3bf5b365e81c3ba45721069b403d0d0589",
    "BLIND_PRELAUNCH_FAILED.md": "5acd76f4dface996e91d8a650ab5d507ea965a97a82015e5cda9a787a3a92374",
    "F165_R02_FAILURE.md": "9fe1950843427f04311df0be2cefd878b197b2e8ecf335b66014782d733d9efc",
    "F165_R02_PROOF_HASH_PROVENANCE.md": "8cad01061c02a2443f5622364d885729a779eae03f02338af5de491d3ab3588e",
    "BLIND_RECONSTRUCTION_FAILED.md": "dfb9cfeb7b13f7d97a8ab981f6a655dee48d5a3e53bdecc0355bbaf0beb17217",
}

EXPERIMENT_DIR = Path(__file__).resolve().parent
REPOSITORY = EXPERIMENT_DIR.parent.parent
RECONSTRUCTION_SOURCE = EXPERIMENT_DIR / "f165_r06_v2_reconstruct.py"
COMPARISON_SOURCE = EXPERIMENT_DIR / "f165_r06_sequence_compare.py"
RECONSTRUCTION_OUTPUT = EXPERIMENT_DIR / "f165_r06_v2_reconstruct_output.json"
COMPARISON_OUTPUT = EXPERIMENT_DIR / "f165_r06_sequence_compare_output.json"
LOG = EXPERIMENT_DIR / "f165_r06_run.log"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def terminate(process: subprocess.Popen[bytes]) -> None:
    os.killpg(process.pid, signal.SIGTERM)
    try:
        process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.wait()


def run_stage(
    label: str,
    command: list[str],
    log,
    deadline: float,
) -> int:
    log.write((f"stage_begin={label}\ncommand={' '.join(command)}\n").encode("utf-8"))
    log.flush()
    process = subprocess.Popen(
        command,
        cwd=REPOSITORY,
        stdout=log,
        stderr=subprocess.STDOUT,
        start_new_session=True,
    )
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        terminate(process)
        log.write((f"stage_timeout={label}\n").encode("utf-8"))
        log.flush()
        return 124
    try:
        return_code = process.wait(timeout=remaining)
    except subprocess.TimeoutExpired:
        terminate(process)
        log.write((f"stage_timeout={label}\n").encode("utf-8"))
        log.flush()
        return 124
    log.write((f"stage_return_code={label}:{return_code}\n").encode("utf-8"))
    log.flush()
    return return_code


def main() -> int:
    observed = {
        name: sha256_file(EXPERIMENT_DIR / name) for name in FROZEN_SHA256
    }
    if observed != FROZEN_SHA256:
        raise SystemExit(f"frozen input hash mismatch: {observed} != {FROZEN_SHA256}")
    for path in (LOG, RECONSTRUCTION_OUTPUT, COMPARISON_OUTPUT):
        if path.exists():
            raise SystemExit(f"refusing to overwrite result path: {path}")

    reconstruction_command = [
        sys.executable,
        str(RECONSTRUCTION_SOURCE),
        "--output",
        str(RECONSTRUCTION_OUTPUT),
    ]
    comparison_command = [
        sys.executable,
        str(COMPARISON_SOURCE),
        "--output",
        str(COMPARISON_OUTPUT),
    ]
    with LOG.open("xb") as log:
        header = (
            "experiment_id=F165-R06\n"
            f"repository={REPOSITORY}\n"
            f"frozen_sha256={observed}\n"
            f"timeout_seconds_total={TIMEOUT_SECONDS}\n"
            f"reconstruction_output={RECONSTRUCTION_OUTPUT}\n"
            f"comparison_output={COMPARISON_OUTPUT}\n"
            "estimated_peak_memory_mib=256\n"
            "process_and_memory_audit=performed_externally_by_root_before_authorization\n"
        )
        log.write(header.encode("utf-8"))
        log.flush()
        preflight = ["vm_stat"]
        log.write((f"preflight_command={' '.join(preflight)}\n").encode("utf-8"))
        completed = subprocess.run(
            preflight,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        log.write(completed.stdout + b"\n")
        log.flush()

        deadline = time.monotonic() + TIMEOUT_SECONDS
        return_code = run_stage(
            "reconstruction", reconstruction_command, log, deadline
        )
        if return_code != 0:
            return return_code
        if not RECONSTRUCTION_OUTPUT.is_file():
            log.write(b"missing_reconstruction_output\n")
            log.flush()
            return 2

        return_code = run_stage("comparison", comparison_command, log, deadline)
        if return_code != 0:
            return return_code
        if not COMPARISON_OUTPUT.is_file():
            log.write(b"missing_comparison_output\n")
            log.flush()
            return 3
        log.write(b"workflow_status=PASS\n")
        log.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
