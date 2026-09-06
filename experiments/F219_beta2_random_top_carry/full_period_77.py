#!/usr/bin/env python3

import argparse
import json
import math
from collections import Counter

import sympy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    r_symbol = sympy.symbols("r")
    a_polynomial = sympy.prod(77 * r_symbol - j for j in range(1, 9)) / math.factorial(8)
    h_polynomial = sympy.cancel((a_polynomial - 1 + 11 * r_symbol) / 77)

    records = []
    all_zero_empty = True
    period_checks = 0
    for t in range(4, 17):
        modulus = 1 << t
        period = 1 << (t + 3)
        h_fibres = Counter()
        g_fibres = Counter()
        for r in range(1, period, 2):
            h = (math.comb(77 * r - 1, 8) - 1 + 11 * r) // 77
            h_shift = (
                math.comb(77 * (r + period) - 1, 8) - 1 + 11 * (r + period)
            ) // 77
            assert (h_shift - h) % modulus == 0
            period_checks += 1
            residue = h % modulus
            h_fibres[residue] += 1
            g_fibres[residue * pow(r, -1, modulus) % modulus] += 1
        all_zero_empty &= h_fibres[0] == 0 and g_fibres[0] == 0
        records.append(
            {
                "t": t,
                "modulus": modulus,
                "period": period,
                "sample_count": period // 2,
                "h_image_size": len(h_fibres),
                "g_image_size": len(g_fibres),
                "h_zero_count": h_fibres[0],
                "g_zero_count": g_fibres[0],
                "h_max_fibre": max(h_fibres.values()),
                "g_max_fibre": max(g_fibres.values()),
            }
        )

    final = records[-1]
    if all_zero_empty:
        verdict = "full_period_zero_kill"
    elif (
        final["h_max_fibre"] * 64 <= final["sample_count"]
        and final["g_max_fibre"] * 64 <= final["sample_count"]
        and final["h_image_size"] >= 64
        and final["g_image_size"] >= 64
    ):
        verdict = "full_period_spreading"
    elif (
        final["h_max_fibre"] * 16 > final["sample_count"]
        or final["g_max_fibre"] * 16 > final["sample_count"]
    ):
        verdict = "full_period_atom_lead"
    else:
        verdict = "mixed"

    result = {
        "experiment": "F219-D02",
        "verdict": verdict,
        "h_polynomial": str(sympy.factor(h_polynomial)),
        "h_derivative": str(sympy.factor(sympy.diff(h_polynomial, r_symbol))),
        "period_checks": period_checks,
        "records": records,
    }
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
