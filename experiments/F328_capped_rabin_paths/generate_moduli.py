#!/usr/local/bin/sage -python
"""Generate the retained balanced-semiprime labels for F328 with Sage."""

import argparse
import hashlib
import json
from pathlib import Path
import random
import resource
import signal
import sys
import time
import traceback

from sage.all import Integer
from sage.env import SAGE_VERSION


TARGET_BITS = (20, 28, 36, 44, 60, 92)
MODULI_PER_SCALE = 2
SEED = 32820260907
INTERNAL_TIMEOUT_SECONDS = 25
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def derived_seed(*parts):
    raw = ":".join(str(part) for part in (SEED, *parts)).encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:16], "big")


def generate_prime(bit_length, seed, forbidden):
    generator = random.Random(seed)
    attempts = 0
    while True:
        attempts += 1
        candidate = (3 << (bit_length - 2)) | generator.getrandbits(bit_length - 2) | 1
        prime = Integer(candidate).next_prime(proof=True)
        if prime.nbits() != bit_length or int(prime) in forbidden:
            continue
        assert prime.is_prime(proof=True)
        return int(prime), attempts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--log", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()
    source_path = Path(__file__)
    source_hash = sha256(source_path)
    log_path = Path(arguments.log)
    log_path.write_text("")

    def log(event, **values):
        with log_path.open("a") as stream:
            stream.write(json.dumps({"event": event, **values}, sort_keys=True) + "\n")

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 25-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F328_capped_rabin_paths",
        "mode": "generate_moduli",
        "seed": SEED,
        "source_sha256": source_hash,
    }
    write_json(arguments.status, running)
    log("start", **running)
    try:
        used_primes = set()
        moduli = []
        for target_bits in TARGET_BITS:
            prime_bits = target_bits // 2
            for instance_index in range(MODULI_PER_SCALE):
                labels = {}
                generation = {}
                for role in ("p", "q"):
                    seed = derived_seed("prime", target_bits, instance_index, role)
                    prime, attempts = generate_prime(prime_bits, seed, used_primes)
                    used_primes.add(prime)
                    labels[role] = prime
                    generation[role] = {
                        "seed": seed,
                        "candidate_stream_attempts": attempts,
                    }
                p, q = labels["p"], labels["q"]
                n = p * q
                assert p != q
                assert n.bit_length() == target_bits
                row = {
                    "modulus_id": f"b{target_bits}_i{instance_index}",
                    "target_bits": target_bits,
                    "actual_bits": n.bit_length(),
                    "n": n,
                    "p_offline": p,
                    "q_offline": q,
                    "prime_bits": [p.bit_length(), q.bit_length()],
                    "balance_ratio": max(p, q) / min(p, q),
                    "generation": generation,
                }
                moduli.append(row)
                log(
                    "modulus_generated",
                    modulus_id=row["modulus_id"],
                    target_bits=target_bits,
                    actual_bits=row["actual_bits"],
                    peak_rss_bytes=peak_rss_bytes(),
                )
                if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                    raise MemoryError("peak RSS exceeded 512 MiB")

        payload = {
            "status": "passed",
            "experiment": "F328_capped_rabin_paths",
            "mode": "generate_moduli",
            "seed": SEED,
            "target_bits": TARGET_BITS,
            "moduli_per_scale": MODULI_PER_SCALE,
            "prime_generation": (
                "For each role, Python's seeded PRNG supplies a candidate with "
                "the top two bits and low bit set. Sage Integer.next_prime with "
                "proof=True supplies and certifies the next prime. Independent "
                "derived seeds identify every scale, instance, and prime role."
            ),
            "label_scope": (
                "p_offline and q_offline are retained input labels. They may "
                "validate the generated modulus but never enter the arithmetic solver."
            ),
            "sage_version": SAGE_VERSION,
            "moduli": moduli,
            "source_sha256": source_hash,
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "mode",
                "seed",
                "source_sha256",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        write_json(arguments.status, status)
        log("passed", **status)
    except BaseException as exception:
        failure = {
            **running,
            "status": "failed",
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        log("failed", **failure)
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
