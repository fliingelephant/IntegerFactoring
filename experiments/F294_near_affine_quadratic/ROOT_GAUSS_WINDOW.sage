"""Exact CyclotomicField checks for the retained-window and Cauchy identities.

One Sage process, 30-second alarm, estimated peak memory below 600 MB.
"""

import json
import random
import resource
import signal
import sys
import time
from pathlib import Path


ALARM_SECONDS = 30
SEED = 202609070402
OUTPUT_PATH = Path(__file__).with_name("ROOT_GAUSS_WINDOW_sage_output.json")
LOG_PATH = Path(__file__).with_name("ROOT_GAUSS_WINDOW_sage_run.log")


def direct_window_count(r, u0, gamma, D):
    m = 1 << r
    q = m * m
    c = m // 2
    A = 1 + q // 2
    return sum(
        (u0 * ((A * w + c * w * w) % q)) % q < q // 2
        and (D + gamma * ((-A * w + c * w * w) % q)) % q < q // 2
        for w in range(q)
    )


def window_formula(r, u0, gamma, D, field_data):
    m = 1 << r
    q = m * m
    K, zeta, eta = field_data
    odds = range(1, q, 2)
    hats = {a: 4 / (1 - zeta ** (-a)) for a in odds}
    gauss = {}
    total = K(0)
    survivors = 0
    for b in odds:
        v = (b * gamma) % m
        if v not in gauss:
            gauss[v] = sum(eta ** (v * x * x) for x in range(m))
        inverse = inverse_mod(v, m)
        for a in odds:
            difference = a * u0 - b * gamma
            if difference % (2 * m):
                continue
            survivors += 1
            j = difference // (2 * m)
            S = m * gauss[v] * eta ** ((-j * j * inverse) % m)
            total += hats[a] * hats[b] * zeta ** (b * D) * S
    value = K(q) / 4 + total / (4 * q * q)
    direct = direct_window_count(r, u0, gamma, D)
    difference = value - K(direct)
    return {
        "r": r,
        "q": q,
        "u0": u0,
        "gamma": gamma,
        "D": D,
        "direct_count": direct,
        "surviving_frequency_pairs": survivors,
        "match": difference == 0,
        "difference": "0" if difference == 0 else str(difference),
    }


def cauchy_check(r, u0, gamma, D, b0, z, field_data):
    m = 1 << r
    q = m * m
    K, zeta, eta = field_data
    d = (gamma * inverse_mod(u0, q)) % q
    A0 = zeta ** (-d * b0 - 2 * m * z)
    B0 = zeta ** (-b0)
    lhs = sum(
        eta ** (t * D)
        / ((1 - A0 * eta ** (-d * t)) * (1 - B0 * eta ** (-t)))
        for t in range(m)
    )
    rhs = (
        K(m)
        / ((1 - A0 ** m) * (1 - B0 ** m))
        * sum(
            A0 ** i * B0 ** ((D - d * i) % m)
            for i in range(m)
        )
    )
    difference = lhs - rhs
    return {
        "r": r,
        "q": q,
        "u0": u0,
        "gamma": gamma,
        "d": int(d),
        "D": D,
        "b0": b0,
        "z": z,
        "match": difference == 0,
        "difference": "0" if difference == 0 else str(difference),
    }


def main():
    signal.alarm(ALARM_SECONDS)
    started = time.monotonic()
    rng = random.Random(int(SEED))
    fields = {}
    for r in (3, 4):
        m = 1 << r
        q = m * m
        K = CyclotomicField(q)
        zeta = K.gen()
        fields[r] = (K, zeta, zeta ** m)

    window_inputs = [
        (3, 1, 45, 13),
        (3, 3, 15, 25),
        (3, 5, 7, 0),
        (4, 1, 109, 230),
        (4, 7, 235, 142),
        (4, 13, 241, 31),
    ]
    window_rows = [
        window_formula(r, u0, gamma, D, fields[r])
        for r, u0, gamma, D in window_inputs
    ]

    cauchy_rows = []
    for u0, gamma in ((1, 1), (1, 45), (3, 15), (5, 7)):
        for b0 in range(1, 8, 2):
            for z in range(4):
                D = (u0 + gamma + b0 + 3 * z) % 8
                cauchy_rows.append(
                    cauchy_check(3, u0, gamma, D, b0, z, fields[3])
                )
    for _ in range(12):
        u0 = rng.randrange(256) | 1
        gamma = rng.randrange(256) | 1
        D = rng.randrange(256)
        b0 = rng.randrange(16) | 1
        z = rng.randrange(8)
        cauchy_rows.append(
            cauchy_check(4, u0, gamma, D, b0, z, fields[4])
        )

    window_mismatches = [row for row in window_rows if not row["match"]]
    cauchy_mismatches = [row for row in cauchy_rows if not row["match"]]
    elapsed = time.monotonic() - started
    max_rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    max_rss_bytes = max_rss_raw if sys.platform == "darwin" else max_rss_raw * 1024
    status = (
        "passed"
        if not window_mismatches and not cauchy_mismatches
        else "formula_mismatch"
    )
    output = {
        "experiment": "ROOT_GAUSS_WINDOW_SAGE",
        "seed": SEED,
        "status": status,
        "window_checks": window_rows,
        "window_mismatches": window_mismatches,
        "cauchy_checks": len(cauchy_rows),
        "cauchy_mismatches": cauchy_mismatches,
        "cauchy_representatives": cauchy_rows[:8] + cauchy_rows[-4:],
        "elapsed_seconds": elapsed,
        "max_rss_bytes": max_rss_bytes,
        "source_alarm_seconds": ALARM_SECONDS,
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, default=int) + "\n")
    LOG_PATH.write_text(
        "\n".join(
            [
                "experiment=ROOT_GAUSS_WINDOW_SAGE",
                f"seed={SEED}",
                f"window_checks={len(window_rows)}",
                f"window_mismatches={len(window_mismatches)}",
                f"cauchy_checks={len(cauchy_rows)}",
                f"cauchy_mismatches={len(cauchy_mismatches)}",
                f"elapsed_seconds={elapsed:.6f}",
                f"max_rss_bytes={max_rss_bytes}",
                f"status={status}",
            ]
        )
        + "\n"
    )
    signal.alarm(0)
    print(
        json.dumps(
            {
                "status": status,
                "window_checks": len(window_rows),
                "window_mismatches": len(window_mismatches),
                "cauchy_checks": len(cauchy_rows),
                "cauchy_mismatches": len(cauchy_mismatches),
                "elapsed_seconds": elapsed,
                "max_rss_bytes": max_rss_bytes,
            },
            indent=2,
            default=int,
        )
    )


main()
