import json
import math
from pathlib import Path


RUN = "F54-D01"
FAMILY = "F29"
BAD_PRIME_MAX = 509
PAIR_PRIME_MAX = 79
TRAJECTORY_STEPS = 8
OUTPUT = Path(__file__).resolve().parent.parent / "output" / f"{RUN}.json"


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def five_is_nonsquare(p):
    return p != 5 and pow(5, (p - 1) // 2, p) == p - 1


bad_primes = [
    p for p in range(3, BAD_PRIME_MAX + 1) if is_prime(p) and five_is_nonsquare(p)
]

baseline_failures = []
scaled_failures = []
for p in bad_primes:
    target = {0, 1}
    preimage = {x for x in range(p) if x * (x - 1) % p in target}
    if preimage != target:
        baseline_failures.append(
            {"p": p, "preimage": sorted(preimage), "target": sorted(target)}
        )

    for c in range(1, p):
        inverse_c = pow(c, -1, p)
        scaled_target = {0, c}
        scaled_preimage = {
            x
            for x in range(p)
            if x * (x - c) * inverse_c % p in scaled_target
        }
        conjugacy_holds = all(
            (c * (y * (y - 1))) % p
            == ((c * y) * (c * y - c) * inverse_c) % p
            for y in range(p)
        )
        if scaled_preimage != scaled_target or not conjugacy_holds:
            scaled_failures.append(
                {
                    "p": p,
                    "c": c,
                    "preimage": sorted(scaled_preimage),
                    "target": sorted(scaled_target),
                    "conjugacy_holds": conjugacy_holds,
                }
            )
            break


pair_primes = [p for p in bad_primes if p <= PAIR_PRIME_MAX]
pair_failures = []
pair_records = []
for i, p in enumerate(pair_primes):
    for q in pair_primes[i + 1 :]:
        n = p * q
        successes = 0
        for start in range(n):
            x = start
            hit = False
            for _ in range(TRAJECTORY_STEPS + 1):
                for ticket in (x, x - 1):
                    divisor = math.gcd(ticket, n)
                    if 1 < divisor < n:
                        hit = True
                        break
                if hit:
                    break
                x = x * (x - 1) % n
            successes += int(hit)
        predicted = 2 * p + 2 * q - 6
        pair_records.append(
            {"p": p, "q": q, "N": n, "successes": successes, "predicted": predicted}
        )
        if successes != predicted:
            pair_failures.append(pair_records[-1])


payload = {
    "run": RUN,
    "family": FAMILY,
    "disposition": (
        "finite exact cross-check only; the unbounded basin closure and infinite "
        "balanced family require symbolic proof"
    ),
    "declared_scope": {
        "bad_prime_max": BAD_PRIME_MAX,
        "pair_prime_max": PAIR_PRIME_MAX,
        "trajectory_steps": TRAJECTORY_STEPS,
        "bad_prime_condition": "5 is a quadratic nonresidue modulo p",
    },
    "bad_prime_count": len(bad_primes),
    "bad_primes": bad_primes,
    "baseline_failures": baseline_failures,
    "scaled_parameters_checked": sum(p - 1 for p in bad_primes),
    "scaled_failures": scaled_failures,
    "semiprime_pairs_checked": len(pair_records),
    "pair_failures": pair_failures,
    "pair_records": pair_records,
}

OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "run": RUN,
    "bad_prime_count": len(bad_primes),
    "scaled_parameters_checked": payload["scaled_parameters_checked"],
    "semiprime_pairs_checked": len(pair_records),
    "baseline_failures": len(baseline_failures),
    "scaled_failures": len(scaled_failures),
    "pair_failures": len(pair_failures),
}, sort_keys=True))
