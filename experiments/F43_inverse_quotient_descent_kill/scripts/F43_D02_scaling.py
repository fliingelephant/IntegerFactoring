import json
import math
import random
from pathlib import Path


RUN = "F43-D02"
FAMILY = "F26"
TARGET_BITS = [8, 10, 12, 14, 16, 18]
SAMPLES_PER_INPUT = 50_000
MAX_STEPS = 10_000
SEED = 0xF43D02
OUTPUT = Path(__file__).resolve().parent.parent / "output" / f"{RUN}.json"


def is_prime(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime(n):
    candidate = max(2, n)
    if candidate == 2:
        return 2
    candidate |= 1
    while not is_prime(candidate):
        candidate += 2
    return candidate


def proper(d, n):
    return 1 < d < n


def descent(n, start):
    u = start
    depth = 0
    direct = False
    extended = False
    first_extended_ticket = None

    while depth < MAX_STEPS:
        state_gcd = math.gcd(u, n)
        if proper(state_gcd, n):
            direct = True
            extended = True
            if first_extended_ticket is None:
                first_extended_ticket = "state_gcd"
            return direct, extended, depth, "nonunit", first_extended_ticket
        if u == 1:
            return direct, extended, depth, "one", first_extended_ticket

        v = pow(u, -1, n)
        k = (u * v - 1) // n
        assert 0 <= k < u
        assert u * v - n * k == 1

        tickets = (
            ("carry_gcd", math.gcd(k, n)),
            ("state_minus_one_gcd", math.gcd(u - 1, n)),
            ("state_plus_one_gcd", math.gcd(u + 1, n)),
            ("inverse_minus_gcd", math.gcd(u - v, n)),
            ("inverse_plus_gcd", math.gcd(u + v, n)),
        )
        if proper(tickets[0][1], n):
            direct = True
        if not extended:
            for label, divisor in tickets:
                if proper(divisor, n):
                    extended = True
                    first_extended_ticket = label
                    break

        u = k
        depth += 1

    return direct, extended, depth, "step_cap", first_extended_ticket


def sample_unit(rng, n):
    while True:
        u = rng.randrange(1, n)
        if math.gcd(u, n) == 1:
            return u


master = random.Random(SEED)
records = []
for target_bits in TARGET_BITS:
    p = next_prime(1 << target_bits)
    q = next_prime(p + 2)
    n = p * q
    rng = random.Random(master.getrandbits(64))

    direct_count = 0
    extended_count = 0
    max_depth = 0
    terminal_counts = {}
    ticket_counts = {}
    for _ in range(SAMPLES_PER_INPUT):
        start = sample_unit(rng, n)
        direct, extended, depth, terminal, ticket = descent(n, start)
        direct_count += int(direct)
        extended_count += int(extended)
        max_depth = max(max_depth, depth)
        terminal_counts[terminal] = terminal_counts.get(terminal, 0) + 1
        if ticket is not None:
            ticket_counts[ticket] = ticket_counts.get(ticket, 0) + 1

    input_bits = (n + 1).bit_length()
    offset_cap = min(n - 1, input_bits * input_bits)
    offset_direct = 0
    offset_extended = 0
    offset_max_depth = 0
    offset_terminals = {}
    for c in range(1, offset_cap + 1):
        direct, extended, depth, terminal, _ = descent(n, n - c)
        offset_direct += int(direct)
        offset_extended += int(extended)
        offset_max_depth = max(offset_max_depth, depth)
        offset_terminals[terminal] = offset_terminals.get(terminal, 0) + 1

    records.append(
        {
            "target_bits": target_bits,
            "N": n,
            "input_bits": input_bits,
            "p": p,
            "q": q,
            "q_over_p": q / p,
            "sample_count": SAMPLES_PER_INPUT,
            "uniform_unit_direct_count": direct_count,
            "uniform_unit_direct_rate": direct_count / SAMPLES_PER_INPUT,
            "uniform_unit_extended_count": extended_count,
            "uniform_unit_extended_rate": extended_count / SAMPLES_PER_INPUT,
            "sample_max_depth": max_depth,
            "sample_terminal_counts": dict(sorted(terminal_counts.items())),
            "first_extended_ticket_counts": dict(sorted(ticket_counts.items())),
            "offset_cap": offset_cap,
            "offset_direct_count": offset_direct,
            "offset_extended_count": offset_extended,
            "offset_max_depth": offset_max_depth,
            "offset_terminal_counts": dict(sorted(offset_terminals.items())),
        }
    )

payload = {
    "run": RUN,
    "family": FAMILY,
    "disposition": "finite seeded discovery only; not asymptotic evidence",
    "seed": SEED,
    "target_bits": TARGET_BITS,
    "samples_per_input": SAMPLES_PER_INPUT,
    "max_steps": MAX_STEPS,
    "records": records,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(
    json.dumps(
        {
            "output": str(OUTPUT),
            "rates": [
                {
                    "p": row["p"],
                    "q": row["q"],
                    "direct": row["uniform_unit_direct_rate"],
                    "extended": row["uniform_unit_extended_rate"],
                    "offset_extended": row["offset_extended_count"],
                    "offset_cap": row["offset_cap"],
                    "max_depth": row["sample_max_depth"],
                }
                for row in records
            ],
        },
        sort_keys=True,
    )
)
