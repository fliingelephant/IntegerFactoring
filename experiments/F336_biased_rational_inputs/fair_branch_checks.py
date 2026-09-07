#!/usr/bin/env python3
"""Exact small-input comparison of fair and minimum count branches."""

import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
SOURCE = Path(__file__).resolve()
F334 = HERE.parent / "F334_count_descent" / "count_descent.py"
EXPECTED = "cb93f160d57b2a3285551cbd268e732917e3062a90eb8ca62df843f581be1e24"
if hashlib.sha256(F334.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("frozen F334 source changed")
sys.path.insert(0, str(F334.parent))
from count_descent import CountOracle  # noqa: E402


def compare(modulus, multiplier):
    oracle = CountOracle(modulus, multiplier)
    checked = 0

    @lru_cache(None)
    def visit(t):
        nonlocal checked
        if t <= 1:
            zero = (Fraction(0),) * 5
            return zero, zero, 0
        # Coordinates: success probability, queries, Q calls, gcd calls, bits.
        local = [0, 1, 0, 1, 0]
        divisor = math.gcd(t, modulus)
        children = None
        if 1 < divisor < modulus:
            local[0] = 1
        else:
            q = oracle.Q(t)
            local[2] = 1
            if modulus <= 51:
                exact = sum(1 <= multiplier * y % modulus <= oracle.h
                            for y in range(1, t + 1))
                assert q == exact, (modulus, multiplier, t, q, exact)
                checked += 1
            for child in (q, t - q):
                if child:
                    local[3] += 1
                    divisor = math.gcd(child, modulus)
                    if 1 < divisor < modulus:
                        assert modulus % divisor == 0
                        local[0] = 1
            if not local[0] and q and t - q:
                children = (q, t - q)
        if children is None:
            terminal = tuple(map(Fraction, local))
            return terminal, terminal, 1
        left, right = (visit(child) for child in children)
        fair = tuple(Fraction(local[i]) + (left[0][i] + right[0][i]) / 2
                     for i in range(5))
        fair = (*fair[:4], fair[4] + 1)
        chosen = left if children[0] <= children[1] else right
        minimum = tuple(Fraction(local[i]) + chosen[1][i] for i in range(5))
        return fair, minimum, 1 + max(left[2], right[2])

    initial = (modulus - 1) // 2
    fair, minimum, maximum = visit(initial)
    upper = (initial - 1).bit_length() + 1
    assert fair[1] <= upper, (modulus, multiplier, fair[1], upper)
    assert 0 <= fair[0] <= 1 and minimum[0] in (0, 1)
    if minimum[0]:
        assert fair[0] > 0
    return fair, minimum, maximum, visit.cache_info().currsize, checked


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, required=True)
    parser.add_argument("--label", choices=("pilot", "scale"), required=True)
    parser.add_argument("--worker", action="store_true")
    args = parser.parse_args()
    prefix = HERE / f"fair_branch_{args.label}"
    started = time.monotonic()
    if not args.worker:
        command = [sys.executable, str(SOURCE), "--max-n", str(args.max_n),
                   "--label", args.label, "--worker"]
        with prefix.with_suffix(".log").open("w") as log:
            try:
                run = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                     timeout=30, check=False)
                code = run.returncode
            except subprocess.TimeoutExpired:
                code = "external_timeout"
        status = {"command": command, "exit_code": code,
                  "walltime_seconds": time.monotonic() - started,
                  "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                  "F334_source_sha256": EXPECTED,
                  "internal_timeout_seconds": 28, "external_timeout_seconds": 30}
        prefix.with_name(prefix.name + "_status.json").write_text(
            json.dumps(status, indent=2, sort_keys=True) + "\n")
        print(json.dumps(status, sort_keys=True))
        sys.exit(0 if code == 0 else 1)
    signal.alarm(28)
    rows, witnesses = [], []
    totals = {"moduli": 0, "unit_parameters": 0, "memoized_states": 0,
              "brute_count_checks": 0, "rescued_parameters": 0}
    for modulus in range(9, args.max_n + 1, 2):
        # Input-class labels are used only to select this finite control set.
        if all(modulus % d for d in range(3, math.isqrt(modulus) + 1, 2)):
            continue
        units = 0
        fair_sum = [Fraction(0)] * 5
        min_sum = [Fraction(0)] * 5
        rescued = 0
        maximum_path = 0
        for multiplier in range(1, modulus):
            if math.gcd(multiplier, modulus) != 1:
                continue
            fair, minimum, maximum, states, checked = compare(modulus, multiplier)
            units += 1
            totals["memoized_states"] += states
            totals["brute_count_checks"] += checked
            fair_sum = [x + y for x, y in zip(fair_sum, fair)]
            min_sum = [x + y for x, y in zip(min_sum, minimum)]
            maximum_path = max(maximum_path, maximum)
            if not minimum[0] and fair[0]:
                rescued += 1
                if len(witnesses) < 16:
                    witnesses.append({"N": modulus, "a": multiplier,
                                      "fair_success": str(fair[0]),
                                      "fair_expected_queries": str(fair[1]),
                                      "minimum_success": 0,
                                      "maximum_path_queries": maximum})
        profiles = {}
        for name, values in (("fair", fair_sum), ("minimum", min_sum)):
            means = [value / units for value in values]
            profiles[name] = {
                key: {"exact": str(value), "decimal": float(value)}
                for key, value in zip(("success_probability", "queries", "Q_calls",
                                       "gcd_calls", "branch_bits"), means)}
            profiles[name]["queries_per_success"] = (
                str(values[1] / values[0]) if values[0] else None)
            profiles[name]["gcd_calls_per_success"] = (
                str(values[3] / values[0]) if values[0] else None)
        rows.append({"N": modulus, "unit_parameters": units, "profiles": profiles,
                     "rescued_parameters": rescued,
                     "maximum_path_queries": maximum_path})
        totals["moduli"] += 1
        totals["unit_parameters"] += units
        totals["rescued_parameters"] += rescued
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rss_bytes = rss if sys.platform == "darwin" else rss * 1024
        if rss_bytes > 512 * 1024 * 1024:
            raise MemoryError("declared 512 MiB budget exceeded")
    result = {"family": "route:F31", "max_n": args.max_n,
              "scope": "Exact conditional uniform-unit laws on listed odd composites; generation excluded.",
              "screen_convention": "As F334: screen both positive children before returning their factor set.",
              "cost_scope": "Declared query, floor-sum-call, gcd-call and branch-bit counts, not bit time.",
              "totals": totals, "witnesses": witnesses, "moduli": rows,
              "walltime_seconds": time.monotonic() - started, "peak_rss_bytes": rss_bytes,
              "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              "F334_source_sha256": EXPECTED}
    prefix.with_suffix(".json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"totals": totals, "walltime_seconds": result["walltime_seconds"],
                      "peak_rss_bytes": rss_bytes}, sort_keys=True))


if __name__ == "__main__":
    main()
