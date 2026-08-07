from sage.all import Integer, ceil, gcd, inverse_mod, log, prime_range

import json
from collections import defaultdict
from pathlib import Path


FAMILY = "F26"
RUN = "F43-D01"
N_MIN = 15
N_MAX = 511
OFFSET_EXPONENT = 2
OUTPUT = Path(__file__).resolve().parent.parent / "output" / "F43-D01.json"


def proper_divisor(d, N):
    return 1 < d < N


def descent_trace(N, u0):
    states = [u0]
    steps = []
    first_direct_hit = None
    first_extended_hit = None

    while True:
        u = states[-1]
        state_gcd = int(gcd(u, N))
        if proper_divisor(state_gcd, N):
            if first_direct_hit is None:
                first_direct_hit = {
                    "state_index": len(states) - 1,
                    "ticket": "state_gcd",
                    "divisor": state_gcd,
                }
            if first_extended_hit is None:
                first_extended_hit = {
                    "step_index": len(steps),
                    "ticket": "state_gcd",
                    "divisor": state_gcd,
                }
            terminal = "nonunit"
            break
        if u == 1:
            terminal = "one"
            break

        v = int(inverse_mod(u, N))
        numerator = u * v - 1
        assert numerator % N == 0
        k = numerator // N

        assert 0 <= k < u
        assert 1 <= v < N
        assert u * v - k * N == 1
        assert k * N % u == u - 1
        assert (u * v - k * N) * 1 == 1

        carry_gcd = int(gcd(k, N))
        state_minus_one_gcd = int(gcd(u - 1, N))
        state_plus_one_gcd = int(gcd(u + 1, N))
        inverse_minus_gcd = int(gcd(u - v, N))
        inverse_plus_gcd = int(gcd(u + v, N))
        square_minus_one_gcd = int(gcd(u * u - 1, N))
        assert inverse_minus_gcd == square_minus_one_gcd

        tickets = [
            ("carry_gcd", carry_gcd),
            ("state_minus_one_gcd", state_minus_one_gcd),
            ("state_plus_one_gcd", state_plus_one_gcd),
            ("inverse_minus_gcd", inverse_minus_gcd),
            ("inverse_plus_gcd", inverse_plus_gcd),
        ]
        if first_extended_hit is None:
            for label, divisor in tickets:
                if proper_divisor(divisor, N):
                    first_extended_hit = {
                        "step_index": len(steps),
                        "ticket": label,
                        "divisor": divisor,
                    }
                    break
        if first_direct_hit is None and proper_divisor(carry_gcd, N):
            first_direct_hit = {
                "state_index": len(states),
                "ticket": "carry_gcd",
                "divisor": carry_gcd,
            }

        steps.append(
            {
                "u": u,
                "v": v,
                "k": int(k),
                "carry_gcd": carry_gcd,
                "state_minus_one_gcd": state_minus_one_gcd,
                "state_plus_one_gcd": state_plus_one_gcd,
                "inverse_minus_gcd": inverse_minus_gcd,
                "inverse_plus_gcd": inverse_plus_gcd,
                "square_minus_one_gcd": square_minus_one_gcd,
                "farey_gap_numerator": 1,
                "farey_gap_denominator": N * v,
            }
        )
        states.append(k)

    return {
        "u0": u0,
        "states": states,
        "carry_sequence": [int(step["k"]) for step in steps],
        "steps": steps,
        "depth": len(steps),
        "terminal": terminal,
        "first_direct_hit": first_direct_hit,
        "first_extended_hit": first_extended_hit,
    }


def fraction_record(numerator, denominator):
    return {
        "numerator": int(numerator),
        "denominator": int(denominator),
        "decimal": float(numerator / denominator),
    }


primes = [int(p) for p in prime_range(3, N_MAX + 1)]
semiprimes = []
for i, p in enumerate(primes):
    for q in primes[i + 1 :]:
        N = p * q
        if N > N_MAX:
            break
        if N >= N_MIN:
            semiprimes.append((N, p, q))
semiprimes.sort()

records = []
for N, p, q in semiprimes:
    unit_starts = [u for u in range(1, N) if gcd(u, N) == 1]
    unit_traces = [descent_trace(N, u) for u in unit_starts]

    carry_groups = defaultdict(list)
    for trace in unit_traces:
        carry_groups[tuple(trace["carry_sequence"])].append(trace["u0"])
    direct_successes = sum(t["first_direct_hit"] is not None for t in unit_traces)
    extended_successes = sum(t["first_extended_hit"] is not None for t in unit_traces)
    direct_divisor_counts = {str(p): 0, str(q): 0}
    extended_ticket_counts = defaultdict(int)
    for trace in unit_traces:
        if trace["first_direct_hit"] is not None:
            direct_divisor_counts[str(trace["first_direct_hit"]["divisor"])] += 1
        if trace["first_extended_hit"] is not None:
            extended_ticket_counts[trace["first_extended_hit"]["ticket"]] += 1

    n = int(ceil(log(Integer(N + 1), 2)))
    offset_cap = min(N - 1, n ** OFFSET_EXPONENT)
    offset_traces = []
    for c in range(1, offset_cap + 1):
        trace = descent_trace(N, N - c)
        offset_traces.append({"offset": c, "trace": trace})

    offset_direct_hits = [
        item["offset"]
        for item in offset_traces
        if item["trace"]["first_direct_hit"] is not None
    ]
    offset_extended_hits = [
        item["offset"]
        for item in offset_traces
        if item["trace"]["first_extended_hit"] is not None
    ]

    records.append(
        {
            "N": N,
            "p": p,
            "q": q,
            "bit_length_n": n,
            "unit_count": len(unit_starts),
            "uniform_unit_direct_success": fraction_record(direct_successes, len(unit_starts)),
            "uniform_unit_extended_success": fraction_record(extended_successes, len(unit_starts)),
            "direct_first_divisor_counts": direct_divisor_counts,
            "extended_first_ticket_counts": dict(sorted(extended_ticket_counts.items())),
            "max_depth": max(t["depth"] for t in unit_traces),
            "max_depth_starts": [
                t["u0"]
                for t in unit_traces
                if t["depth"] == max(s["depth"] for s in unit_traces)
            ],
            "carry_transcript_distinct_count": len(carry_groups),
            "max_carry_transcript_multiplicity": max(len(v) for v in carry_groups.values()),
            "offset_menu": {
                "definition": "c=1,...,min(N-1,n^2), start u=N-c",
                "offset_cap": offset_cap,
                "direct_hit_offsets": offset_direct_hits,
                "extended_hit_offsets": offset_extended_hits,
                "max_depth": max(item["trace"]["depth"] for item in offset_traces),
            },
        }
    )

min_direct = min(
    records,
    key=lambda row: (
        row["uniform_unit_direct_success"]["numerator"]
        / row["uniform_unit_direct_success"]["denominator"]
    ),
)
min_extended = min(
    records,
    key=lambda row: (
        row["uniform_unit_extended_success"]["numerator"]
        / row["uniform_unit_extended_success"]["denominator"]
    ),
)
max_depth_record = max(records, key=lambda row: row["max_depth"])
offset_all_fail = []
for row in records:
    if not row["offset_menu"]["extended_hit_offsets"]:
        offset_all_fail.append(row["N"])

payload = {
    "run": RUN,
    "family": FAMILY,
    "scope": {
        "semiprimes": "all N=pq with distinct odd primes p<q and 15<=N<=511",
        "N_min": N_MIN,
        "N_max": N_MAX,
        "offset_menu": "c=1,...,min(N-1,n^2), where n=ceil(log2(N+1)); start at N-c",
        "uniform_source": "every u in {1,...,N-1} with gcd(u,N)=1",
        "tickets": [
            "gcd(current,N)",
            "gcd(carry,N)",
            "gcd(u-1,N)",
            "gcd(u+1,N)",
            "gcd(u-v,N)",
            "gcd(u+v,N)",
            "gcd(u^2-1,N)=gcd(u-v,N)",
        ],
        "transcript_collision": "two starts have identical complete carry sequences",
    },
    "disposition": "compact finite exact discovery/certificate only; full attempt-3 trajectories are preserved in the manifest archive",
    "semiprime_count": len(records),
    "summary": {
        "minimum_uniform_direct_success": {
            "N": min_direct["N"],
            "value": min_direct["uniform_unit_direct_success"],
        },
        "minimum_uniform_extended_success": {
            "N": min_extended["N"],
            "value": min_extended["uniform_unit_extended_success"],
        },
        "largest_observed_depth": {
            "N": max_depth_record["N"],
            "depth": max_depth_record["max_depth"],
            "starts": max_depth_record["max_depth_starts"],
        },
        "offset_menus_with_no_extended_success": offset_all_fail,
    },
    "records": records,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True, default=int)
    handle.write("\n")

print(json.dumps({"output": str(OUTPUT), "summary": payload["summary"]}, sort_keys=True))
