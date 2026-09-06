#!/usr/bin/env python3
"""Frozen F258-D01 direct Pell-resultant ticket scan."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import multiprocessing as mp
import resource
import sys
import time
from collections import Counter


D_MENU = (2, 3, 5, 6, 7, 10, 11, 13)
FACTOR_BITS = (12, 16, 20, 24, 28, 32, 40, 48, 56, 60)
RANDOM_PER_BITS = 4096
NEIGHBOR_PER_BITS = 1024
SAFE_PER_BITS = 1024
SAFE_12_BITS = 128
WINDOW_MULTIPLIER = 12
MAX_INDEX = WINDOW_MULTIPLIER * 120
COHORT_SEED = "F258-direct-ticket-cohort-v1"
MR_BASES_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
PELL: dict[int, list[tuple[int, int]]] = {}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def proper(g: int, n: int) -> bool:
    return 1 < g < n


def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d & 1 == 0:
        d >>= 1
        s += 1
    for a in MR_BASES_64:
        if a % n == 0:
            continue
        x = pow(a % n, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


class HashStream:
    def __init__(self, label: str):
        self.label = label
        self.counter = 0

    def below(self, modulus: int) -> int:
        limit = (1 << 256) - ((1 << 256) % modulus)
        while True:
            payload = f"{self.label}:{self.counter}".encode()
            self.counter += 1
            value = int.from_bytes(hashlib.sha256(payload).digest(), "big")
            if value < limit:
                return value % modulus


def prime_from_hash(label: str, bits: int) -> int:
    low = 1 << (bits - 1)
    high = 1 << bits
    stream = HashStream(label)
    start = (low + stream.below(high - low)) | 1
    value = start
    while True:
        if is_prime_64(value):
            return value
        value += 2
        if value >= high:
            value = low | 1
        require(value != start, "prime search wrapped")


def safe_prime_from_hash(label: str, bits: int) -> int:
    low_r = 1 << (bits - 2)
    high_r = 1 << (bits - 1)
    stream = HashStream(label)
    start = (low_r + stream.below(high_r - low_r)) | 1
    r = start
    while True:
        p = 2 * r + 1
        if is_prime_64(r) and is_prime_64(p):
            return p
        r += 2
        if r >= high_r:
            r = low_r | 1
        require(r != start, "safe-prime search wrapped")


def next_prime_same_bits(p: int, bits: int) -> int | None:
    high = 1 << bits
    q = p + 2
    while q < high:
        if is_prime_64(q):
            return q
        q += 2
    return None


def make_cohorts() -> list[dict[str, int | str]]:
    tasks: list[dict[str, int | str]] = []
    for bits in FACTOR_BITS:
        seen_at_bits: set[int] = set()
        specs = (
            ("random", RANDOM_PER_BITS),
            ("neighbor", NEIGHBOR_PER_BITS),
            ("safe", SAFE_12_BITS if bits == 12 else SAFE_PER_BITS),
        )
        for cohort, count in specs:
            accepted = 0
            counter = 0
            while accepted < count:
                label = f"{COHORT_SEED}:{cohort}:{bits}:{counter}"
                counter += 1
                if cohort == "safe":
                    p = safe_prime_from_hash(label + ":p", bits)
                    q = safe_prime_from_hash(label + ":q", bits)
                elif cohort == "neighbor":
                    p = prime_from_hash(label + ":p", bits)
                    q = next_prime_same_bits(p, bits)
                    if q is None:
                        continue
                else:
                    p = prime_from_hash(label + ":p", bits)
                    q = prime_from_hash(label + ":q", bits)
                p, q = sorted((p, q))
                n = p * q
                if p == q or q >= 2 * p or n in seen_at_bits:
                    continue
                seen_at_bits.add(n)
                tasks.append(
                    {
                        "factor_bits": bits,
                        "cohort": cohort,
                        "index": accepted,
                        "p": p,
                        "q": q,
                    }
                )
                accepted += 1
    require(len(tasks) == 60544, "frozen task count")
    return tasks


def fundamental_pell(disc: int) -> tuple[int, int]:
    a0 = math.isqrt(disc)
    require(a0 * a0 != disc, "nonsquare Pell discriminant")
    m = 0
    den = 1
    a = a0
    p_prev, p = 1, a
    q_prev, q = 0, 1
    while p * p - disc * q * q != 1:
        m = den * a - m
        den = (disc - m * m) // den
        a = (a0 + m) // den
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev
    return p, q


def build_pell() -> dict[int, list[tuple[int, int]]]:
    table: dict[int, list[tuple[int, int]]] = {}
    for disc in D_MENU:
        fs, ft = fundamental_pell(disc)
        rows = [(1, 0)]
        s, t = 1, 0
        for _ in range(MAX_INDEX):
            s, t = fs * s + disc * ft * t, ft * s + fs * t
            require(s * s - disc * t * t == 1, "Pell recurrence")
            rows.append((s, t))
        table[disc] = rows
    return table


def jacobi(a: int, n: int) -> int:
    require(n > 0 and n & 1, "positive odd Jacobi modulus")
    a %= n
    result = 1
    while a:
        while a & 1 == 0:
            a >>= 1
            if n & 7 in (3, 5):
                result = -result
        a, n = n, a
        if a & 3 == 3 and n & 3 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def cleanup_rows(n: int, disc: int, limit: int) -> tuple[list[tuple[int, int, int, int]], int]:
    rows: list[tuple[int, int, int, int]] = []
    first_by_y: dict[int, int] = {}
    early = 0
    factor = math.gcd(disc, n)
    if factor != 1:
        return rows, int(proper(factor, n))
    for index in range(1, limit + 1):
        s, t = PELL[disc][index]
        k, y = divmod(t, n)
        x = s % n
        root_gcd = math.gcd(x, n)
        if root_gcd != 1:
            early += int(proper(root_gcd, n))
            continue
        value = 1 + disc * y * y
        require(x * x % n == value % n, "supplied root")
        integer_root = math.isqrt(value)
        if integer_root * integer_root == value:
            early += int(proper(math.gcd(integer_root - x, n), n))
            early += int(proper(math.gcd(integer_root + x, n), n))
            continue
        if y in first_by_y:
            old_x = first_by_y[y]
            early += int(proper(math.gcd(x - old_x, n), n))
            early += int(proper(math.gcd(x + old_x, n), n))
            continue
        first_by_y[y] = x
        if k > 0:
            rows.append((index, k, y, k % n))
    for left, right in zip(rows, rows[1:]):
        require(left[1] <= right[1], "monotone Pell quotients")
    return rows, early


def legendre_minus_d(disc: int, prime: int) -> int:
    value = pow((-disc) % prime, (prime - 1) // 2, prime)
    require(value in (1, prime - 1), "unit Legendre value")
    return 1 if value == 1 else -1


def process_input(task: dict[str, int | str]) -> dict[str, object]:
    p = int(task["p"])
    q = int(task["q"])
    n = p * q
    bits = n.bit_length()
    limit = WINDOW_MULTIPLIER * bits
    require(limit <= MAX_INDEX, "Pell table limit")
    require(p < q < 2 * p and is_prime_64(p) and is_prime_64(q), "labelled input")
    eligible: dict[str, int] = {}
    hits: dict[str, int] = {}
    early_count = 0
    selected_d = 0
    first_ticket: dict[str, object] | None = None

    for disc in D_MENU:
        for sign in ("minus", "plus"):
            eligible[f"{disc}:{sign}"] = 0
            hits[f"{disc}:{sign}"] = 0
        if jacobi(-disc, n) != -1:
            continue
        selected_d += 1
        rows, early = cleanup_rows(n, disc, limit)
        early_count += early
        lp = legendre_minus_d(disc, p)
        lq = legendre_minus_d(disc, q)
        require(lp * lq == -1, "Jacobi/Legendre consistency")
        split_prime = p if lp == 1 else q

        def test_pair(left: tuple[int, int, int, int], right: tuple[int, int, int, int], sign: str, a: int) -> None:
            nonlocal first_ticket
            key = f"{disc}:{sign}"
            require(a > 0 and 2 * a * a < n, "ticket size condition")
            eligible[key] += 1
            delta_mod = (left[2] * right[3] - right[2] * left[3]) % n
            q_mod = (a * a + disc * delta_mod * delta_mod) % n
            g = math.gcd(q_mod, n)
            require(g in (1, split_prime), "one-sided ticket theorem")
            if g == 1:
                return
            hits[key] += 1
            if first_ticket is None:
                first_ticket = {
                    "D": disc,
                    "sign": sign,
                    "i": left[0],
                    "j": right[0],
                    "a": a,
                    "delta_mod_N": delta_mod,
                    "Q_mod_N": q_mod,
                    "factor": g,
                }

        left_edge = 0
        for j in range(len(rows)):
            while left_edge < j:
                gap = rows[j][1] - rows[left_edge][1]
                if 2 * gap * gap < n:
                    break
                left_edge += 1
            for i in range(left_edge, j):
                gap = rows[j][1] - rows[i][1]
                if gap > 0:
                    test_pair(rows[i], rows[j], "minus", gap)

        for j in range(1, len(rows)):
            smallest = rows[0][1] + rows[j][1]
            if 2 * smallest * smallest >= n:
                break
            for i in range(j):
                total = rows[i][1] + rows[j][1]
                if 2 * total * total >= n:
                    break
                test_pair(rows[i], rows[j], "plus", total)

    total_hits = sum(hits.values())
    return {
        **task,
        "N": n,
        "N_bits": bits,
        "split": "discovery" if int(task["factor_bits"]) <= 32 else "heldout",
        "selected_D": selected_d,
        "cleanup_factor_events": early_count,
        "eligible": eligible,
        "hits": hits,
        "any_hit": total_hits > 0,
        "strict_hit": total_hits > 0 and early_count == 0,
        "first_ticket": first_ticket,
    }


def self_test() -> None:
    global PELL
    PELL = build_pell()
    require(is_prime_64(11) and is_prime_64(13) and not is_prime_64(143), "primality")
    require(jacobi(-2, 143) == -1, "Jacobi example")
    require(math.gcd(1 + 2 * 4 * 4, 77) == 11, "one-sided Q example")
    sample = process_input({"factor_bits": 4, "cohort": "selftest", "index": 0, "p": 11, "q": 13})
    require(sample["N"] == 143 and sample["selected_D"] > 0, "public source self-test")
    for disc in D_MENU:
        if jacobi(-disc, 143) != -1:
            continue
        rows, _ = cleanup_rows(143, disc, WINDOW_MULTIPLIER * (143).bit_length())
        minus = 0
        plus = 0
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                minus += int(2 * (rows[j][1] - rows[i][1]) ** 2 < 143)
                plus += int(2 * (rows[j][1] + rows[i][1]) ** 2 < 143)
        require(sample["eligible"][f"{disc}:minus"] == minus, "minus enumeration")
        require(sample["eligible"][f"{disc}:plus"] == plus, "plus enumeration")
    print("SELF_TEST_PASS N=143")


def run(workers: int, summary_path: str, rows_path: str) -> None:
    global PELL
    started = time.perf_counter()
    PELL = build_pell()
    tasks = make_cohorts()
    generation_seconds = time.perf_counter() - started
    strata: dict[tuple[int, str, int, str], Counter] = {}
    global_counts = Counter()
    certificates: list[dict[str, object]] = []
    completed = 0
    scan_started = time.perf_counter()

    with gzip.open(rows_path, "wt", encoding="utf-8") as row_file:
        context = mp.get_context("fork")
        with context.Pool(processes=workers) as pool:
            for record in pool.imap(process_input, tasks, chunksize=4):
                row_file.write(json.dumps(record, sort_keys=True) + "\n")
                completed += 1
                global_counts["inputs"] += 1
                global_counts["cleanup_inputs"] += int(record["cleanup_factor_events"] > 0)
                global_counts["hit_inputs"] += int(record["any_hit"])
                global_counts["strict_hit_inputs"] += int(record["strict_hit"])
                for disc in D_MENU:
                    for sign in ("minus", "plus"):
                        key = f"{disc}:{sign}"
                        stratum = (int(record["factor_bits"]), str(record["cohort"]), disc, sign)
                        counter = strata.setdefault(stratum, Counter())
                        counter["inputs"] += 1
                        counter["eligible_pairs"] += int(record["eligible"][key])
                        counter["ticket_pairs"] += int(record["hits"][key])
                        counter["hit_inputs"] += int(record["hits"][key] > 0)
                        counter["strict_hit_inputs"] += int(record["hits"][key] > 0 and record["cleanup_factor_events"] == 0)
                        global_counts["eligible_pairs"] += int(record["eligible"][key])
                        global_counts["ticket_pairs"] += int(record["hits"][key])
                if record["first_ticket"] is not None and len(certificates) < 128:
                    certificates.append(record)
                if completed % 256 == 0 or completed == len(tasks):
                    elapsed = time.perf_counter() - scan_started
                    print(
                        f"progress={completed}/{len(tasks)} elapsed={elapsed:.1f}s rate={completed/elapsed:.2f}/s "
                        f"eligible={global_counts['eligible_pairs']} tickets={global_counts['ticket_pairs']}",
                        file=sys.stderr,
                        flush=True,
                    )

    scan_seconds = time.perf_counter() - scan_started
    summaries = []
    for key in sorted(strata):
        counter = strata[key]
        summaries.append(
            {
                "factor_bits": key[0],
                "cohort": key[1],
                "D": key[2],
                "sign": key[3],
                **dict(counter),
            }
        )
    output = {
        "experiment": "F258-D01",
        "workers": workers,
        "generation_seconds": generation_seconds,
        "scan_seconds": scan_seconds,
        "peak_rss_kib_parent_plus_children": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        + resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        "global": dict(global_counts),
        "summaries": summaries,
        "certificates": certificates,
    }
    with open(summary_path, "w", encoding="utf-8") as handle:
        json.dump(output, handle, sort_keys=True, indent=2)
        handle.write("\n")
    print(json.dumps({"status": "PASS", **dict(global_counts), "scan_seconds": scan_seconds}, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--summary")
    parser.add_argument("--rows")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    require(1 <= args.workers <= 8, "workers 1..8")
    require(args.summary is not None and args.rows is not None, "output paths required")
    run(args.workers, args.summary, args.rows)


if __name__ == "__main__":
    main()
