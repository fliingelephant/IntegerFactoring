#!/usr/bin/env python3

import argparse
import json
import math
from collections import Counter


def primes_to(limit):
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]
    for d in range(2, math.isqrt(limit) + 1):
        if sieve[d]:
            sieve[d * d : limit + 1 : d] = [False] * (
                (limit - d * d) // d + 1
            )
    return [d for d, prime in enumerate(sieve) if prime]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    primes = primes_to(193)
    records = []
    identity_checks = 0
    for p in primes:
        if not 5 <= p <= 97 or p == 2:
            continue
        for q in primes:
            if not p < q < 2 * p:
                continue
            n = p * q
            b = math.isqrt(n)
            for t in range(4, 12):
                modulus = 1 << t
                h_fibres = Counter()
                g_fibres = Counter()
                p_inverse = pow(p, -1, modulus)
                n_inverse = pow(n, -1, modulus)
                for r in range(1, modulus, 2):
                    a = (-1 if b & 1 else 1) * math.comb(r * n - 1, b)
                    numerator = a - (1 - r * q)
                    assert numerator % n == 0
                    h = numerator // n
                    h_residue = h % modulus
                    g_residue = h_residue * pow(r, -1, modulus) % modulus
                    z = (a - 1) * n_inverse % modulus
                    assert (h_residue - z - r * p_inverse) % modulus == 0
                    identity_checks += 1
                    h_fibres[h_residue] += 1
                    g_fibres[g_residue] += 1

                h_max = max(h_fibres.values())
                g_max = max(g_fibres.values())
                records.append(
                    {
                        "N": n,
                        "p": p,
                        "q": q,
                        "B": b,
                        "t": t,
                        "sample_count": modulus // 2,
                        "h_image_size": len(h_fibres),
                        "g_image_size": len(g_fibres),
                        "h_zero_count": h_fibres[0],
                        "g_zero_count": g_fibres[0],
                        "h_max_fibre": h_max,
                        "g_max_fibre": g_max,
                        "h_first_max_residue": min(
                            value for value, count in h_fibres.items() if count == h_max
                        ),
                        "g_first_max_residue": min(
                            value for value, count in g_fibres.items() if count == g_max
                        ),
                    }
                )

    summaries = []
    for t in range(4, 12):
        rows = [row for row in records if row["t"] == t]
        sample_count = 1 << (t - 1)
        fields = [
            "h_image_size",
            "g_image_size",
            "h_zero_count",
            "g_zero_count",
            "h_max_fibre",
            "g_max_fibre",
        ]
        summary = {"t": t, "input_count": len(rows), "sample_count": sample_count}
        for field in fields:
            minimum = min(rows, key=lambda row: (row[field], row["N"]))
            maximum = max(rows, key=lambda row: (row[field], -row["N"]))
            summary[field + "_min"] = minimum[field]
            summary[field + "_min_at"] = [minimum["N"], minimum["p"], minimum["q"]]
            summary[field + "_max"] = maximum[field]
            summary[field + "_max_at"] = [maximum["N"], maximum["p"], maximum["q"]]
        summaries.append(summary)

    final_rows = [row for row in records if row["t"] == 11]
    fixed_residues = set.intersection(
        *[
            {
                row["h_first_max_residue"],
                row["g_first_max_residue"],
            }
            for row in final_rows
        ]
    )
    universal_atom = bool(fixed_residues) and all(
        row["h_max_fibre"] >= row["sample_count"] // 16
        and row["g_max_fibre"] >= row["sample_count"] // 16
        for row in final_rows
    )
    spreading = all(
        row["h_max_fibre"] <= row["sample_count"] // 16
        and row["g_max_fibre"] <= row["sample_count"] // 16
        and row["h_image_size"] >= 16
        and row["g_image_size"] >= 16
        for row in final_rows
    )
    verdict = (
        "exact_universal_atom_lead"
        if universal_atom
        else "spreading_lead" if spreading else "mixed"
    )
    result = {
        "experiment": "F219-D01",
        "verdict": verdict,
        "identity_checks": identity_checks,
        "fixed_residue_intersection": sorted(fixed_residues),
        "summaries": summaries,
        "records": records,
    }
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps({key: result[key] for key in result if key != "records"}, indent=2))


if __name__ == "__main__":
    main()
