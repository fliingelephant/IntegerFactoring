import json
import math
import random
from pathlib import Path


RUN = "F43-D03"
FAMILY = "F26"
EXHAUSTIVE_N_MIN = 3
EXHAUSTIVE_N_MAX = 4095
RANDOM_BITS = (16, 24, 32, 48)
RANDOM_MODULI_PER_BITS = 50
RANDOM_UNITS_PER_MODULUS = 2_000
SEED = 0xF43D03
OUTPUT = Path(__file__).resolve().parent.parent / "output" / f"{RUN}.json"


def descent(n, u):
    inverse = pow(u, -1, n)
    carry = (u * inverse - 1) // n
    assert u * inverse - n * carry == 1
    assert 0 <= carry < u
    return carry


def inspect(n, u, summary, violations):
    k = descent(n, u)
    if k <= 1 or math.gcd(k, n) != 1:
        return
    ell = descent(n, k)
    summary["eligible_pairs"] += 1
    if summary["max_twice_second_over_start"] is None:
        summary["max_twice_second_over_start"] = {
            "numerator": 2 * ell,
            "denominator": u,
            "N": n,
            "u": u,
            "first": k,
            "second": ell,
        }
    else:
        old = summary["max_twice_second_over_start"]
        if 2 * ell * old["denominator"] > old["numerator"] * u:
            summary["max_twice_second_over_start"] = {
                "numerator": 2 * ell,
                "denominator": u,
                "N": n,
                "u": u,
                "first": k,
                "second": ell,
            }
    if 2 * ell > u:
        summary["strict_violations"] += 1
        if len(violations) < 100:
            violations.append({"N": n, "u": u, "first": k, "second": ell})
    elif 2 * ell == u:
        summary["equalities"] += 1


summary = {
    "eligible_pairs": 0,
    "strict_violations": 0,
    "equalities": 0,
    "max_twice_second_over_start": None,
}
violations = []

for n in range(EXHAUSTIVE_N_MIN, EXHAUSTIVE_N_MAX + 1):
    for u in range(2, n):
        if math.gcd(u, n) == 1:
            inspect(n, u, summary, violations)

rng = random.Random(SEED)
random_records = []
for bits in RANDOM_BITS:
    bit_summary = {
        "bits": bits,
        "moduli": 0,
        "sampled_units": 0,
        "eligible_pairs": 0,
        "strict_violations": 0,
    }
    before_eligible = summary["eligible_pairs"]
    before_violations = summary["strict_violations"]
    for _ in range(RANDOM_MODULI_PER_BITS):
        n = rng.randrange(1 << (bits - 1), 1 << bits) | 1
        bit_summary["moduli"] += 1
        accepted = 0
        while accepted < RANDOM_UNITS_PER_MODULUS:
            u = rng.randrange(2, n)
            if math.gcd(u, n) != 1:
                continue
            accepted += 1
            inspect(n, u, summary, violations)
        bit_summary["sampled_units"] += accepted
    bit_summary["eligible_pairs"] = summary["eligible_pairs"] - before_eligible
    bit_summary["strict_violations"] = summary["strict_violations"] - before_violations
    random_records.append(bit_summary)

payload = {
    "run": RUN,
    "family": FAMILY,
    "disposition": "finite counterexample search only; no unbounded contraction or depth claim",
    "conjecture": "if u and D_N(u) are units and D_N(u)>1, then 2*D_N(D_N(u))<=u",
    "exhaustive_scope": {
        "N_min": EXHAUSTIVE_N_MIN,
        "N_max": EXHAUSTIVE_N_MAX,
        "starts": "every u in {2,...,N-1} with gcd(u,N)=1",
    },
    "random_scope": {
        "seed": SEED,
        "bit_lengths": RANDOM_BITS,
        "moduli_per_bit_length": RANDOM_MODULI_PER_BITS,
        "units_per_modulus": RANDOM_UNITS_PER_MODULUS,
    },
    "summary": summary,
    "first_violations": violations,
    "random_records": random_records,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(json.dumps({"output": str(OUTPUT), "summary": summary}, sort_keys=True))
