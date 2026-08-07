import gzip
import hashlib
import json
import math
import random
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
CANDIDATE = HERE.parent / "F43_inverse_quotient_descent_kill"
OUTPUT = HERE / "output" / "F43-A01.json"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_gzip_payload(path):
    digest = hashlib.sha256()
    with gzip.open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def proper(value, modulus):
    return 1 < value < modulus


def trace(modulus, start, full=False, max_steps=None):
    states = [start]
    steps = []
    first_direct = None
    first_extended = None

    while max_steps is None or len(steps) < max_steps:
        u = states[-1]
        state_gcd = math.gcd(u, modulus)
        if proper(state_gcd, modulus):
            if first_direct is None:
                first_direct = {
                    "state_index": len(states) - 1,
                    "ticket": "state_gcd",
                    "divisor": state_gcd,
                }
            if first_extended is None:
                first_extended = {
                    "step_index": len(steps),
                    "ticket": "state_gcd",
                    "divisor": state_gcd,
                }
            terminal = "nonunit"
            break
        if u == 1:
            terminal = "one"
            break

        inverse = pow(u, -1, modulus)
        carry = (u * inverse - 1) // modulus
        carry_gcd = math.gcd(carry, modulus)
        state_minus = math.gcd(u - 1, modulus)
        state_plus = math.gcd(u + 1, modulus)
        inverse_minus = math.gcd(u - inverse, modulus)
        inverse_plus = math.gcd(u + inverse, modulus)
        square_minus = math.gcd(u * u - 1, modulus)
        assert inverse_minus == square_minus

        tickets = (
            ("carry_gcd", carry_gcd),
            ("state_minus_one_gcd", state_minus),
            ("state_plus_one_gcd", state_plus),
            ("inverse_minus_gcd", inverse_minus),
            ("inverse_plus_gcd", inverse_plus),
        )
        if first_extended is None:
            for label, divisor in tickets:
                if proper(divisor, modulus):
                    first_extended = {
                        "step_index": len(steps),
                        "ticket": label,
                        "divisor": divisor,
                    }
                    break
        if first_direct is None and proper(carry_gcd, modulus):
            first_direct = {
                "state_index": len(states),
                "ticket": "carry_gcd",
                "divisor": carry_gcd,
            }

        steps.append(
            {
                "u": u,
                "v": inverse,
                "k": carry,
                "carry_gcd": carry_gcd,
                "state_minus_one_gcd": state_minus,
                "state_plus_one_gcd": state_plus,
                "inverse_minus_gcd": inverse_minus,
                "inverse_plus_gcd": inverse_plus,
                "square_minus_one_gcd": square_minus,
                "farey_gap_numerator": 1,
                "farey_gap_denominator": modulus * inverse,
            }
        )
        states.append(carry)
    else:
        terminal = "step_cap"

    result = {
        "u0": start,
        "states": states,
        "carry_sequence": [step["k"] for step in steps],
        "steps": steps,
        "depth": len(steps),
        "terminal": terminal,
        "first_direct_hit": first_direct,
        "first_extended_hit": first_extended,
    }
    if full:
        return result
    return first_direct, first_extended, len(steps), terminal


def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return number == divisor
        divisor += 1 if divisor == 2 else 2
    return True


def next_prime(number):
    while not is_prime(number):
        number += 1
    return number


def fraction_record(numerator, denominator):
    return {
        "numerator": numerator,
        "denominator": denominator,
        "decimal": numerator / denominator,
    }


def reconstruct_d01():
    primes = [number for number in range(3, 512) if is_prime(number)]
    inputs = []
    for index, p in enumerate(primes):
        for q in primes[index + 1 :]:
            modulus = p * q
            if modulus > 511:
                break
            if modulus >= 15:
                inputs.append((modulus, p, q))
    inputs.sort()

    records = []
    for modulus, p, q in inputs:
        starts = [u for u in range(1, modulus) if math.gcd(u, modulus) == 1]
        traces = [trace(modulus, u, full=True) for u in starts]
        groups = defaultdict(list)
        for item in traces:
            groups[tuple(item["carry_sequence"])].append(item["u0"])
        direct = sum(item["first_direct_hit"] is not None for item in traces)
        extended = sum(item["first_extended_hit"] is not None for item in traces)
        direct_divisors = {str(p): 0, str(q): 0}
        extended_tickets = defaultdict(int)
        for item in traces:
            if item["first_direct_hit"] is not None:
                direct_divisors[str(item["first_direct_hit"]["divisor"])] += 1
            if item["first_extended_hit"] is not None:
                extended_tickets[item["first_extended_hit"]["ticket"]] += 1

        input_bits = modulus.bit_length()
        offset_cap = min(modulus - 1, input_bits * input_bits)
        offset_traces = [
            (offset, trace(modulus, modulus - offset, full=True))
            for offset in range(1, offset_cap + 1)
        ]
        max_depth = max(item["depth"] for item in traces)
        records.append(
            {
                "N": modulus,
                "p": p,
                "q": q,
                "bit_length_n": input_bits,
                "unit_count": len(starts),
                "uniform_unit_direct_success": fraction_record(direct, len(starts)),
                "uniform_unit_extended_success": fraction_record(extended, len(starts)),
                "direct_first_divisor_counts": direct_divisors,
                "extended_first_ticket_counts": dict(sorted(extended_tickets.items())),
                "max_depth": max_depth,
                "max_depth_starts": [
                    item["u0"] for item in traces if item["depth"] == max_depth
                ],
                "carry_transcript_distinct_count": len(groups),
                "max_carry_transcript_multiplicity": max(map(len, groups.values())),
                "offset_menu": {
                    "definition": "c=1,...,min(N-1,n^2), start u=N-c",
                    "offset_cap": offset_cap,
                    "direct_hit_offsets": [
                        offset
                        for offset, item in offset_traces
                        if item["first_direct_hit"] is not None
                    ],
                    "extended_hit_offsets": [
                        offset
                        for offset, item in offset_traces
                        if item["first_extended_hit"] is not None
                    ],
                    "max_depth": max(item["depth"] for _, item in offset_traces),
                },
            }
        )

    min_direct = min(
        records,
        key=lambda row: row["uniform_unit_direct_success"]["numerator"]
        / row["uniform_unit_direct_success"]["denominator"],
    )
    min_extended = min(
        records,
        key=lambda row: row["uniform_unit_extended_success"]["numerator"]
        / row["uniform_unit_extended_success"]["denominator"],
    )
    max_depth_record = max(records, key=lambda row: row["max_depth"])
    summary = {
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
        "offset_menus_with_no_extended_success": [
            row["N"] for row in records if not row["offset_menu"]["extended_hit_offsets"]
        ],
    }
    return records, summary


def reconstruct_d02():
    seed = 0xF43D02
    master = random.Random(seed)
    records = []
    for target_bits in (8, 10, 12, 14, 16, 18):
        p = next_prime(1 << target_bits)
        q = next_prime(p + 2)
        modulus = p * q
        rng = random.Random(master.getrandbits(64))
        direct_count = 0
        extended_count = 0
        max_depth = 0
        terminal_counts = defaultdict(int)
        ticket_counts = defaultdict(int)
        for _ in range(50_000):
            while True:
                start = rng.randrange(1, modulus)
                if math.gcd(start, modulus) == 1:
                    break
            direct, extended, depth, terminal = trace(
                modulus, start, max_steps=10_000
            )
            direct_count += direct is not None
            extended_count += extended is not None
            max_depth = max(max_depth, depth)
            terminal_counts[terminal] += 1
            if extended is not None:
                ticket_counts[extended["ticket"]] += 1

        input_bits = (modulus + 1).bit_length()
        offset_cap = min(modulus - 1, input_bits * input_bits)
        offset_direct = 0
        offset_extended = 0
        offset_max_depth = 0
        offset_terminals = defaultdict(int)
        for offset in range(1, offset_cap + 1):
            direct, extended, depth, terminal = trace(
                modulus, modulus - offset, max_steps=10_000
            )
            offset_direct += direct is not None
            offset_extended += extended is not None
            offset_max_depth = max(offset_max_depth, depth)
            offset_terminals[terminal] += 1

        records.append(
            {
                "target_bits": target_bits,
                "N": modulus,
                "input_bits": input_bits,
                "p": p,
                "q": q,
                "q_over_p": q / p,
                "sample_count": 50_000,
                "uniform_unit_direct_count": direct_count,
                "uniform_unit_direct_rate": direct_count / 50_000,
                "uniform_unit_extended_count": extended_count,
                "uniform_unit_extended_rate": extended_count / 50_000,
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
    return records


def reconstruct_d03():
    summary = {
        "eligible_pairs": 0,
        "strict_violations": 0,
        "equalities": 0,
        "max_twice_second_over_start": None,
    }
    violations = []

    def inspect(modulus, start):
        inverse = pow(start, -1, modulus)
        first = (start * inverse - 1) // modulus
        if first <= 1 or math.gcd(first, modulus) != 1:
            return
        second_inverse = pow(first, -1, modulus)
        second = (first * second_inverse - 1) // modulus
        summary["eligible_pairs"] += 1
        old = summary["max_twice_second_over_start"]
        if old is None or 2 * second * old["denominator"] > old["numerator"] * start:
            summary["max_twice_second_over_start"] = {
                "numerator": 2 * second,
                "denominator": start,
                "N": modulus,
                "u": start,
                "first": first,
                "second": second,
            }
        if 2 * second > start:
            summary["strict_violations"] += 1
            if len(violations) < 100:
                violations.append(
                    {"N": modulus, "u": start, "first": first, "second": second}
                )
        elif 2 * second == start:
            summary["equalities"] += 1

    for modulus in range(3, 4096):
        for start in range(2, modulus):
            if math.gcd(start, modulus) == 1:
                inspect(modulus, start)

    rng = random.Random(0xF43D03)
    random_records = []
    for bits in (16, 24, 32, 48):
        before_eligible = summary["eligible_pairs"]
        before_violations = summary["strict_violations"]
        for _ in range(50):
            modulus = rng.randrange(1 << (bits - 1), 1 << bits) | 1
            accepted = 0
            while accepted < 2_000:
                start = rng.randrange(2, modulus)
                if math.gcd(start, modulus) != 1:
                    continue
                accepted += 1
                inspect(modulus, start)
        random_records.append(
            {
                "bits": bits,
                "moduli": 50,
                "sampled_units": 100_000,
                "eligible_pairs": summary["eligible_pairs"] - before_eligible,
                "strict_violations": summary["strict_violations"] - before_violations,
            }
        )
    return summary, violations, random_records


declared_hashes = {
    "RESULT.md": "bab9cdfcb657d67c8a7043efdd0c02ab748f76ff00bd6a246bc5f473b03ec83e",
    "RUN_MANIFEST.md": "87c33325bd8a5fbeb6e5a3bd83ba49b334b76febd961518db3f7b2927ad0d0e6",
    "logs/F43-D01-attempt2.log": "7ce024fb4d5072e7dd129a021923a16f607acc97e083973995ac7d8c5d06bef2",
    "output/F43-D01-attempt2-partial.json": "7a2c7e1df11985ae624a4806a2639c900b5440b5920a759c88115fb880945775",
    "logs/F43-D01-attempt3.log": "e5768ac8c5dd935ed3fa270356796579b1b09c18101e44987949888c240e1525",
    "output/F43-D01-attempt3-full.json.gz": "f0c841388ef87ffae82d70daa566e1f64d354ad20c1288690fc3ea902d2eed79",
    "scripts/F43_D01_scan.sage": "8a132c7121774f382f66847f288f667160151b8465e66c4e5442778f0e73341c",
    "run_F43_D01.sh": "6dd64c20d583848abbbe7fcb625cfd94a1989433167fac08e1bc6bf76cb1e2dd",
    "logs/F43-D01.log": "e5768ac8c5dd935ed3fa270356796579b1b09c18101e44987949888c240e1525",
    "output/F43-D01.json": "167970dfbb2ed60f489ebac16c59e7448564feb6c2191c31bbac204437bb7fef",
    "scripts/F43_D02_scaling.py": "6663207572401d6080ff4e593919adc7b0e625d17bd0b4413200aaf2e4e8d00a",
    "run_F43_D02.sh": "199fbea000e34cd1ba1f45158892edd8e15d9eb95495d56cc28f5b63bc1962a8",
    "logs/F43-D02.log": "0a77ec99f2db2781cef35fa9fb0e1ef7a7cdedcf288d382c871de413cd7d1ae3",
    "output/F43-D02.json": "d44bfe7e6f39c23fb01c8eed0bddd9d61d8428c637a74e9ac20680f903369e78",
    "scripts/F43_D03_two_step_contraction.py": "9d5fabddf846ee23fbc0294d4bb0a9cee2b403cb649ac1579cfb8a7703d21529",
    "run_F43_D03.sh": "8a102aaff0a68e8bcfc31e1dadd8ee5a3fb0887e4f6e6d9d10f1a86ad9f5738d",
    "logs/F43-D03.log": "55718f818862bda90f5bfa12c31cbe2ae9dac8d61ff4c4c0f17a7e2d74a5e4d8",
    "output/F43-D03.json": "3fde9b23d46830c288c8feb3cae55f7ddca9cc8976cb47c60860b7ac4b43541e",
}
hash_audit = {}
for relative, expected in declared_hashes.items():
    actual = sha256(CANDIDATE / relative)
    hash_audit[relative] = {
        "expected": expected,
        "actual": actual,
        "match": actual == expected,
    }

with (CANDIDATE / "output/F43-D01.json").open(encoding="utf-8") as handle:
    d01 = json.load(handle)
with gzip.open(
    CANDIDATE / "output/F43-D01-attempt3-full.json.gz", "rt", encoding="utf-8"
) as handle:
    d01_full = json.load(handle)
with (CANDIDATE / "output/F43-D02.json").open(encoding="utf-8") as handle:
    d02 = json.load(handle)
with (CANDIDATE / "output/F43-D03.json").open(encoding="utf-8") as handle:
    d03 = json.load(handle)

d01_records, d01_summary = reconstruct_d01()
d02_records = reconstruct_d02()
d03_summary, d03_violations, d03_random = reconstruct_d03()

full_projection = []
for row in d01_full["records"]:
    offset_traces = row["offset_menu"]["traces"]
    full_projection.append(
        {
            key: row[key]
            for key in (
                "N",
                "p",
                "q",
                "bit_length_n",
                "unit_count",
                "uniform_unit_direct_success",
                "uniform_unit_extended_success",
                "direct_first_divisor_counts",
                "extended_first_ticket_counts",
                "max_depth",
                "max_depth_starts",
                "carry_transcript_distinct_count",
                "max_carry_transcript_multiplicity",
            )
        }
    )
    full_projection[-1]["offset_menu"] = {
        "definition": row["offset_menu"]["definition"],
        "offset_cap": row["offset_menu"]["offset_cap"],
        "direct_hit_offsets": [
            item["offset"]
            for item in offset_traces
            if item["trace"]["first_direct_hit"] is not None
        ],
        "extended_hit_offsets": [
            item["offset"]
            for item in offset_traces
            if item["trace"]["first_extended_hit"] is not None
        ],
        "max_depth": max(item["trace"]["depth"] for item in offset_traces),
    }

checks = {
    "all_declared_hashes_match": all(row["match"] for row in hash_audit.values()),
    "only_declared_hash_mismatch_is_failed_partial": [
        path for path, row in hash_audit.items() if not row["match"]
    ]
    == ["output/F43-D01-attempt2-partial.json"],
    "attempt3_decompressed_hash_matches_manifest": sha256_gzip_payload(
        CANDIDATE / "output/F43-D01-attempt3-full.json.gz"
    )
    == "92af2cee0e33aabdd70f8ee4a4007a7abfbe613473cf231a84fb9a2f5a8b35e2",
    "d01_reconstruction_matches_compact_records": d01_records == d01["records"],
    "d01_reconstruction_matches_summary": d01_summary == d01["summary"],
    "d01_full_projection_matches_compact": full_projection == d01["records"],
    "d01_full_summary_matches_compact": d01_full["summary"] == d01["summary"],
    "d02_reconstruction_matches_records": d02_records == d02["records"],
    "d03_reconstruction_matches_summary": d03_summary == d03["summary"],
    "d03_reconstruction_matches_first_violations": d03_violations
    == d03["first_violations"],
    "d03_reconstruction_matches_random_records": d03_random == d03["random_records"],
}

payload = {
    "run": "F43-A01",
    "disposition": "hostile artifact audit; finite checks support only finite claims",
    "hash_audit": hash_audit,
    "checks": checks,
    "d01_summary": d01_summary,
    "d02_rates": [
        {
            "p": row["p"],
            "q": row["q"],
            "direct": row["uniform_unit_direct_rate"],
            "extended": row["uniform_unit_extended_rate"],
            "offset_extended": row["offset_extended_count"],
            "offset_cap": row["offset_cap"],
            "max_depth": row["sample_max_depth"],
        }
        for row in d02_records
    ],
    "d03_summary": d03_summary,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(json.dumps({"checks": checks, "output": str(OUTPUT)}, sort_keys=True))
