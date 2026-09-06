#!/usr/bin/env python3
import argparse
import hashlib
import json
from math import gcd
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("--limit", type=int, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

sieve = bytearray(b"\x01") * (args.limit + 1)
sieve[:2] = b"\x00\x00"
for a in range(2, int(args.limit**0.5) + 1):
    if sieve[a]:
        sieve[a * a : args.limit + 1 : a] = b"\x00" * (
            (args.limit - a * a) // a + 1
        )
primes = [a for a in range(2, args.limit + 1) if sieve[a]]

windows = ((1.0, 1.08), (1.25, 1.35), (1.50, 1.65))
pairs = []
for p in primes:
    if p < 101:
        continue
    for lo, hi in windows:
        q = next(
            (
                r
                for r in primes
                if max(p + 1, int(lo * p + 0.999999999)) <= r <= int(hi * p)
                and r < 2 * p
                and (p * r) % 4 == 3
            ),
            None,
        )
        if q is not None:
            pairs.append((p, q, lo, hi))

rows = []
for p, q, lo, hi in pairs:
    rp = sum((pow(x + 1, q, p) - pow(x, q, p) - 1) % p == 0 for x in range(p))
    rq = sum((pow(x + 1, p, q) - pow(x, p, q) - 1) % q == 0 for x in range(q))
    numerator = rp * (q - rq) + rq * (p - rp)
    denominator = p * q
    rows.append(
        {
            "p": p,
            "q": q,
            "window": [lo, hi],
            "gap": q - p,
            "common_predecessor": gcd(p - 1, q - 1),
            "roots_mod_p": rp,
            "roots_mod_q": rq,
            "xor_numerator": numerator,
            "xor_denominator": denominator,
            "xor_probability": numerator / denominator,
        }
    )

rows.sort(key=lambda row: (-row["xor_probability"], row["p"], row["q"]))
source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
payload = {
    "run_id": "F221-D01",
    "limit": args.limit,
    "source_sha256": source_hash,
    "pair_count": len(rows),
    "max_xor_probability": rows[0]["xor_probability"] if rows else None,
    "min_xor_probability": rows[-1]["xor_probability"] if rows else None,
    "max_root_ratio_p": max((row["roots_mod_p"] / row["p"] for row in rows), default=None),
    "max_root_ratio_q": max((row["roots_mod_q"] / row["q"] for row in rows), default=None),
    "top_40": rows[:40],
}
args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps(payload, indent=2, sort_keys=True))
