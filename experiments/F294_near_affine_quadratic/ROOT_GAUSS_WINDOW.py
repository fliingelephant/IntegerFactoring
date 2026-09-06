"""Exact coefficient-array checks for the supplied ROOT_GAUSS_WINDOW sum.

The coefficient basis is Z[X]/(X^(q/2)+1), the cyclotomic polynomial for
q a power of two. One process, 20-second alarm, estimated below 100 MB.
"""

import json
import random
import resource
import signal
import sys
import time
from pathlib import Path


ALARM_SECONDS = 20
SEED = 202609070401
OUTPUT_PATH = Path(__file__).with_name("ROOT_GAUSS_WINDOW_output.json")
LOG_PATH = Path(__file__).with_name("ROOT_GAUSS_WINDOW_run.log")


def root_array(q, terms):
    half = q // 2
    coefficients = [0] * half
    for exponent, coefficient in terms:
        residue = exponent % q
        if residue < half:
            coefficients[residue] += coefficient
        else:
            coefficients[residue - half] -= coefficient
    return coefficients


def direct_sum_array(r, u0, gamma, a, b):
    m = 1 << r
    q = m * m
    c = m // 2
    A = 1 + q // 2
    linear = a * u0 - b * gamma
    quadratic = a * u0 + b * gamma
    return root_array(
        q,
        (
            (A * linear * w + c * quadratic * w * w, 1)
            for w in range(q)
        ),
    )


def claimed_sum_array(r, u0, gamma, a, b):
    m = 1 << r
    q = m * m
    difference = a * u0 - b * gamma
    if difference % (2 * m):
        return [0] * (q // 2), False
    j = difference // (2 * m)
    v = b * gamma
    shift = -j * j * pow(v, -1, m)
    return root_array(
        q,
        ((m * (v * x * x + shift), m) for x in range(m)),
    ), True


def check_case(r, u0, gamma, a, b):
    direct = direct_sum_array(r, u0, gamma, a, b)
    claimed, survives = claimed_sum_array(r, u0, gamma, a, b)
    nonzero = [(index, value) for index, value in enumerate(direct) if value]
    return {
        "match": direct == claimed,
        "survives": survives,
        "direct_nonzero_coefficients": len(nonzero),
        "direct_l1_norm": sum(abs(value) for _, value in nonzero),
        "first_direct_terms": nonzero[:8],
    }


def main():
    signal.alarm(ALARM_SECONDS)
    started = time.monotonic()
    rng = random.Random(SEED)
    groups = []
    mismatches = []
    representatives = []

    for r in (3, 4):
        m = 1 << r
        q = m * m
        checked = 0
        surviving = 0
        for a in range(1, q, 2):
            for b in range(1, q, 2):
                result = check_case(r, 1, 1, a, b)
                checked += 1
                surviving += result["survives"]
                if not result["match"]:
                    mismatches.append(
                        {
                            "r": r,
                            "u0": 1,
                            "gamma": 1,
                            "a": a,
                            "b": b,
                            **result,
                        }
                    )
                elif len(representatives) < 8 and (
                    result["survives"] or a == 1 and b == 3
                ):
                    representatives.append(
                        {
                            "r": r,
                            "u0": 1,
                            "gamma": 1,
                            "a": a,
                            "b": b,
                            **result,
                        }
                    )
        groups.append(
            {
                "r": r,
                "q": q,
                "mode": "all odd frequency pairs with u0=gamma=1",
                "checked": checked,
                "surviving": surviving,
            }
        )

    for r, samples in ((5, 256), (6, 128), (7, 32)):
        m = 1 << r
        q = m * m
        checked = 0
        surviving = 0
        for _ in range(samples):
            u0 = rng.randrange(q) | 1
            gamma = rng.randrange(q) | 1
            a = rng.randrange(q) | 1
            b = rng.randrange(q) | 1
            result = check_case(r, u0, gamma, a, b)
            checked += 1
            surviving += result["survives"]
            if not result["match"]:
                mismatches.append(
                    {
                        "r": r,
                        "u0": u0,
                        "gamma": gamma,
                        "a": a,
                        "b": b,
                        **result,
                    }
                )
            elif len(representatives) < 14 and result["survives"]:
                representatives.append(
                    {
                        "r": r,
                        "u0": u0,
                        "gamma": gamma,
                        "a": a,
                        "b": b,
                        **result,
                    }
                )
        forced_surviving = 16
        for _ in range(forced_surviving):
            u0 = rng.randrange(q) | 1
            gamma = rng.randrange(q) | 1
            b = rng.randrange(q) | 1
            target = b * gamma * pow(u0, -1, 2 * m) % (2 * m)
            a = target + 2 * m * rng.randrange(m // 2)
            result = check_case(r, u0, gamma, a, b)
            assert result["survives"]
            checked += 1
            surviving += 1
            if not result["match"]:
                mismatches.append(
                    {
                        "r": r,
                        "u0": u0,
                        "gamma": gamma,
                        "a": a,
                        "b": b,
                        **result,
                    }
                )
        groups.append(
            {
                "r": r,
                "q": q,
                "mode": "seeded random odd parameter quadruples plus forced surviving pairs",
                "checked": checked,
                "surviving": surviving,
                "forced_surviving": forced_surviving,
            }
        )

    elapsed = time.monotonic() - started
    max_rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    max_rss_bytes = max_rss_raw if sys.platform == "darwin" else max_rss_raw * 1024
    output = {
        "experiment": "ROOT_GAUSS_WINDOW",
        "seed": SEED,
        "status": "passed" if not mismatches else "formula_mismatch",
        "coefficient_ring": "Z[X]/(X^(q/2)+1)",
        "groups": groups,
        "checks": sum(group["checked"] for group in groups),
        "surviving_checks": sum(group["surviving"] for group in groups),
        "mismatches": mismatches,
        "representatives": representatives,
        "elapsed_seconds": elapsed,
        "max_rss_bytes": max_rss_bytes,
        "source_alarm_seconds": ALARM_SECONDS,
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2) + "\n")
    LOG_PATH.write_text(
        "\n".join(
            [
                "experiment=ROOT_GAUSS_WINDOW",
                f"seed={SEED}",
                f"checks={output['checks']}",
                f"surviving_checks={output['surviving_checks']}",
                f"mismatches={len(mismatches)}",
                f"elapsed_seconds={elapsed:.6f}",
                f"max_rss_bytes={max_rss_bytes}",
                f"status={output['status']}",
            ]
        )
        + "\n"
    )
    signal.alarm(0)
    print(
        json.dumps(
            {
                "status": output["status"],
                "checks": output["checks"],
                "surviving_checks": output["surviving_checks"],
                "mismatches": len(mismatches),
                "elapsed_seconds": elapsed,
                "max_rss_bytes": max_rss_bytes,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
