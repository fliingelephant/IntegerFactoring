#!/usr/bin/env python3
"""Full finite DFT scan of h and lambda histograms by gcd category."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np


PAIRS = [
    (5, 7),
    (7, 11),
    (11, 13),
    (13, 17),
    (17, 19),
    (29, 31),
    (41, 43),
    (59, 61),
    (101, 103),
    (137, 139),
    (211, 223),
]


def spectrum(values: list[int], modulus: int) -> dict[str, object]:
    counts = np.bincount(np.asarray(values, dtype=np.int64), minlength=modulus)
    magnitudes = np.abs(np.fft.fft(counts) / len(values))
    categories: dict[str, list[tuple[float, int]]] = {
        "gcd_1": [],
        "gcd_p": [],
        "gcd_q": [],
    }
    p = next(divisor for divisor in range(2, math.isqrt(modulus) + 1) if modulus % divisor == 0)
    q = modulus // p
    for frequency in range(1, modulus):
        divisor = math.gcd(frequency, modulus)
        if divisor == 1:
            categories["gcd_1"].append((float(magnitudes[frequency]), frequency))
        elif divisor == p:
            categories["gcd_p"].append((float(magnitudes[frequency]), frequency))
        elif divisor == q:
            categories["gcd_q"].append((float(magnitudes[frequency]), frequency))
        else:
            raise AssertionError((frequency, divisor))
    summary = {}
    for category, rows in categories.items():
        magnitude, frequency = max(rows, default=(0.0, 0))
        summary[category] = {
            "max_magnitude": magnitude,
            "frequency": frequency,
            "frequency_gcd": math.gcd(frequency, modulus),
        }
    public_cutoff = max(1, math.ceil(math.log2(modulus)) ** 2)
    public_rows = [
        (float(magnitudes[frequency]), frequency)
        for frequency in range(1, min(modulus, public_cutoff + 1))
        if math.gcd(frequency, modulus) == 1
    ]
    magnitude, frequency = max(public_rows, default=(0.0, 0))
    summary["small_public_frequencies"] = {
        "cutoff": public_cutoff,
        "max_magnitude": magnitude,
        "frequency": frequency,
    }
    return summary


def inspect(p: int, q: int) -> dict[str, object]:
    modulus = p * q
    hs = []
    lambdas = []
    for a in range(1, modulus):
        if math.gcd(a, modulus) != 1:
            continue
        lifted = pow(a, modulus, modulus * modulus)
        x = lifted % modulus
        h = lifted // modulus
        hs.append(h)
        lambdas.append(h * pow(x, -1, modulus) % modulus)
    return {
        "p": p,
        "q": q,
        "N": modulus,
        "h": spectrum(hs, modulus),
        "lambda": spectrum(lambdas, modulus),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    report = {
        "run": "F51-D05",
        "status": "PASS",
        "scope": "finite discovery/certificate only",
        "numpy_version": np.__version__,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "pairs": [inspect(p, q) for p, q in PAIRS],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "output": str(output), "pairs": len(PAIRS)}))


if __name__ == "__main__":
    main()
