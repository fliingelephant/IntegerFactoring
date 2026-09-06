#!/usr/bin/env python3
"""Frozen 600-second runner for the F165-R05 semantic sequence audit."""

from __future__ import annotations

import hashlib
import os
import signal
import subprocess
import sys
from pathlib import Path


TIMEOUT_SECONDS = 600
SOURCE_SHA256 = "2dcb4e871b890c16c575f2c0168295c757e40187b514a0d1c223a7034f85e397"
INPUT_SHA256 = {
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
    "BLIND_PRELAUNCH_FAILED.md": "5acd76f4dface996e91d8a650ab5d507ea965a97a82015e5cda9a787a3a92374",
    "F165_R02_FAILURE.md": "9fe1950843427f04311df0be2cefd878b197b2e8ecf335b66014782d733d9efc",
    "F165_R02_PROOF_HASH_PROVENANCE.md": "8cad01061c02a2443f5622364d885729a779eae03f02338af5de491d3ab3588e",
    "BLIND_RECONSTRUCTION_FAILED.md": "dfb9cfeb7b13f7d97a8ab981f6a655dee48d5a3e53bdecc0355bbaf0beb17217",
}

EXPERIMENT_DIR = Path(__file__).resolve().parent
REPOSITORY = EXPERIMENT_DIR.parent.parent
SOURCE = EXPERIMENT_DIR / "f165_r05_sequence_compare.py"
LOG = EXPERIMENT_DIR / "f165_r05_sequence_compare_run.log"
OUTPUT = EXPERIMENT_DIR / "f165_r05_sequence_compare_output.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    observed_source = sha256_file(SOURCE)
    if observed_source != SOURCE_SHA256:
        raise SystemExit(
            f"source hash mismatch: {observed_source} != {SOURCE_SHA256}"
        )
    observed_inputs = {
        name: sha256_file(EXPERIMENT_DIR / name) for name in INPUT_SHA256
    }
    if observed_inputs != INPUT_SHA256:
        raise SystemExit(
            f"frozen input hash mismatch: {observed_inputs} != {INPUT_SHA256}"
        )
    if LOG.exists():
        raise SystemExit(f"refusing to overwrite log: {LOG}")
    if OUTPUT.exists():
        raise SystemExit(f"refusing to overwrite output: {OUTPUT}")

    command = [sys.executable, str(SOURCE), "--output", str(OUTPUT)]
    with LOG.open("xb") as log:
        header = (
            f"experiment_id=F165-R05\n"
            f"repository={REPOSITORY}\n"
            f"source={SOURCE}\n"
            f"source_sha256={observed_source}\n"
            f"input_sha256={observed_inputs}\n"
            f"timeout_seconds={TIMEOUT_SECONDS}\n"
            f"output={OUTPUT}\n"
            f"command={' '.join(command)}\n"
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

        process = subprocess.Popen(
            command,
            cwd=REPOSITORY,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        try:
            return_code = process.wait(timeout=TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            log.write(f"timeout_after_seconds={TIMEOUT_SECONDS}\n".encode("utf-8"))
            log.flush()
            return 124
        log.write(f"return_code={return_code}\n".encode("utf-8"))
        log.flush()

    if not OUTPUT.is_file():
        raise SystemExit(f"comparison returned without output: {OUTPUT}")
    return return_code


if __name__ == "__main__":
    raise SystemExit(main())
