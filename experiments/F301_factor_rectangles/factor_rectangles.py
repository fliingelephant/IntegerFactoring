#!/usr/bin/env python3
"""Exact public-rectangle factoring pilot with a numerical reference oracle."""

from __future__ import annotations

import csv
import json
import math
import random
import resource
import signal
import sys
import time
import traceback
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


BASE = Path(__file__).resolve().parent
FIXED_PRIMES = (2, 3, 5, 7, 11, 13)
RATIO = Fraction(17, 16)
SEED = 30120260907
ALARM_SECONDS = 60


@dataclass(frozen=True)
class Box:
    grid_index: int
    x_lo: int
    x_hi: int
    y_lo: int
    y_hi: int


class ReferenceEmpty:
    """Deliberately numerical existence oracle for odd N."""

    def __init__(self) -> None:
        self.queries = 0
        self.enumerated_x = 0
        self.empty_queries = 0
        self.nonempty_queries = 0
        self.max_x_scanned_in_query = 0

    def empty(self, n: int, modulus: int, box: Box) -> bool:
        assert n & 1
        self.queries += 1
        scanned = 0
        x = box.x_lo | 1
        while x <= box.x_hi:
            scanned += 1
            self.enumerated_x += 1
            y = n * pow(x, -1, modulus) % modulus
            if box.y_lo <= y <= box.y_hi:
                self.nonempty_queries += 1
                self.max_x_scanned_in_query = max(
                    self.max_x_scanned_in_query, scanned
                )
                return False
            x += 2
        self.empty_queries += 1
        self.max_x_scanned_in_query = max(self.max_x_scanned_in_query, scanned)
        return True


def public_boxes(n: int) -> tuple[int, list[Box], int]:
    """Generate the public exact-rational 17/16 grid."""
    modulus = 1 << ((n // 8).bit_length() - 1)
    root = math.isqrt(n)
    length = Fraction(16, 1)
    boxes: list[Box] = []
    grid_index = 0
    max_rational_bits = 5
    while length.numerator**2 <= n * length.denominator**2:
        right = RATIO * length
        x_lo = max(17, (length.numerator + length.denominator - 1) // length.denominator)
        x_hi = min(root, right.numerator // right.denominator)
        lower_y = Fraction(n, 1) / right
        upper_y = Fraction(n, 1) / length
        y_lo = max(1, (lower_y.numerator + lower_y.denominator - 1) // lower_y.denominator)
        y_hi = min(modulus - 1, upper_y.numerator // upper_y.denominator)
        if x_lo <= x_hi and y_lo <= y_hi:
            boxes.append(Box(grid_index, x_lo, x_hi, y_lo, y_hi))
        max_rational_bits = max(
            max_rational_bits,
            length.numerator.bit_length(),
            length.denominator.bit_length(),
            right.numerator.bit_length(),
            right.denominator.bit_length(),
            lower_y.numerator.bit_length(),
            lower_y.denominator.bit_length(),
            upper_y.numerator.bit_length(),
            upper_y.denominator.bit_length(),
        )
        length = right
        grid_index += 1
    return modulus, boxes, max_rational_bits


def factor_public(n: int, capture_trace: bool = False) -> tuple[list[int], ReferenceEmpty, dict]:
    """Factor using only fixed divisions, public boxes, and Empty answers."""
    oracle = ReferenceEmpty()
    stats = {
        "recursive_calls": 0,
        "box_lists": 0,
        "boxes_generated": 0,
        "initial_box_queries": 0,
        "bisection_queries": 0,
        "prime_declarations": 0,
        "max_rational_bits": 0,
        "events": [],
        "trace": [],
    }

    def recurse(value: int) -> list[int]:
        stats["recursive_calls"] += 1
        for prime in FIXED_PRIMES:
            if value == prime:
                return [prime]
            if value % prime == 0:
                return [prime] + recurse(value // prime)

        modulus, boxes, rational_bits = public_boxes(value)
        stats["box_lists"] += 1
        stats["boxes_generated"] += len(boxes)
        stats["max_rational_bits"] = max(stats["max_rational_bits"], rational_bits)
        stats["events"].append((value, modulus, boxes))
        if not boxes:
            stats["prime_declarations"] += 1
            return [value]

        selected = None
        for box in boxes:
            is_empty = oracle.empty(value, modulus, box)
            stats["initial_box_queries"] += 1
            if capture_trace:
                stats["trace"].append(
                    {
                        "value": value,
                        "stage": "public_box",
                        "grid_index": box.grid_index,
                        "x": [box.x_lo, box.x_hi],
                        "y": [box.y_lo, box.y_hi],
                        "empty": is_empty,
                    }
                )
            if not is_empty:
                selected = box
                break
        if selected is None:
            stats["prime_declarations"] += 1
            return [value]

        x_lo, x_hi = selected.x_lo, selected.x_hi
        while x_lo < x_hi:
            middle = (x_lo + x_hi) // 2
            left = Box(selected.grid_index, x_lo, middle, selected.y_lo, selected.y_hi)
            is_empty = oracle.empty(value, modulus, left)
            stats["bisection_queries"] += 1
            if capture_trace:
                stats["trace"].append(
                    {
                        "value": value,
                        "stage": "bisect_left",
                        "x": [x_lo, middle],
                        "y": [selected.y_lo, selected.y_hi],
                        "empty": is_empty,
                    }
                )
            if is_empty:
                x_lo = middle + 1
            else:
                x_hi = middle

        if value % x_lo:
            raise AssertionError(f"singleton {x_lo} does not divide {value}")
        if not 1 < x_lo < value:
            raise AssertionError(f"singleton {x_lo} is not proper for {value}")
        return recurse(x_lo) + recurse(value // x_lo)

    factors = sorted(recurse(n))
    assert stats["initial_box_queries"] + stats["bisection_queries"] == oracle.queries
    return factors, oracle, stats


def trial_factor(n: int) -> list[int]:
    """Independent elementary verification factorization."""
    factors: list[int] = []
    divisor = 2
    value = n
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors.append(divisor)
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append(value)
    return factors


def is_prime_trial(n: int) -> bool:
    return len(trial_factor(n)) == 1


def audit_events(events: list[tuple[int, int, list[Box]]], exhaustive_pairs: bool) -> dict:
    audited_boxes = 0
    composite_events = 0
    covered_composites = 0
    boundary_hits = 0
    for value, modulus, boxes in events:
        assert modulus & (modulus - 1) == 0
        for box in boxes:
            audited_boxes += 1
            assert 1 <= box.x_lo <= box.x_hi < modulus
            assert 1 <= box.y_lo <= box.y_hi < modulus
            assert box.x_lo * box.y_lo > value - modulus
            assert box.x_hi * box.y_hi < value + modulus
            if exhaustive_pairs:
                for x in range(box.x_lo, box.x_hi + 1):
                    for y in range(box.y_lo, box.y_hi + 1):
                        if (x * y - value) % modulus == 0:
                            assert x * y == value

        labels = trial_factor(value)
        if len(labels) > 1:
            composite_events += 1
            small = labels[0]
            large = value // small
            matches = [
                box
                for box in boxes
                if (
                    box.x_lo <= small <= box.x_hi
                    and box.y_lo <= large <= box.y_hi
                )
                or (
                    box.x_lo <= large <= box.x_hi
                    and box.y_lo <= small <= box.y_hi
                )
            ]
            assert matches
            covered_composites += 1
            if any(
                small in (box.x_lo, box.x_hi) or large in (box.y_lo, box.y_hi)
                for box in matches
            ):
                boundary_hits += 1
    return {
        "audited_boxes": audited_boxes,
        "composite_events": composite_events,
        "covered_composites": covered_composites,
        "boundary_hits": boundary_hits,
    }


def random_prime(rng: random.Random, low: int, high: int, excluded: set[int]) -> int:
    while True:
        candidate = rng.randrange(low | 1, high + 1, 2)
        if candidate not in excluded and is_prime_trial(candidate):
            return candidate


def build_random_cases(rng: random.Random) -> list[tuple[str, int]]:
    limit = (1 << 24) - 1
    cases: list[tuple[str, int]] = []
    used: set[int] = set()

    while len(cases) < 30:
        value = rng.randint(2, limit)
        if value not in used:
            used.add(value)
            cases.append(("random_integer", value))

    while len(cases) < 60:
        value = random_prime(rng, 1 << 15, limit, used)
        used.add(value)
        cases.append(("prime", value))

    while len(cases) < 90:
        prime = random_prime(rng, 17, 4000, set())
        value = prime * prime
        if value <= limit and value not in used:
            used.add(value)
            cases.append(("repeated_factor", value))

    while len(cases) < 120:
        small = random_prime(rng, 17, 251, set())
        large = random_prime(rng, max(4099, 16 * small + 1), limit // small, set())
        value = small * large
        if value not in used:
            used.add(value)
            cases.append(("unbalanced", value))
    return cases


def random_fixed_clean(rng: random.Random, bits: int) -> int:
    while True:
        value = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        if all(value % prime for prime in FIXED_PRIMES):
            return value


def build_large_pairs(rng: random.Random) -> list[tuple[int, str, int, int]]:
    cases: list[tuple[int, str, int, int]] = []
    for bits in (32, 64, 128, 256, 512):
        counts = {"balanced": 3, "unbalanced": 3, "repeated": 2}
        for label, count in counts.items():
            made = 0
            while made < count:
                if label == "balanced":
                    a = random_fixed_clean(rng, bits // 2)
                    b = random_fixed_clean(rng, bits // 2)
                elif label == "unbalanced":
                    a_bits = max(5, bits // 4)
                    a = random_fixed_clean(rng, a_bits)
                    b = random_fixed_clean(rng, bits - a_bits + 1)
                else:
                    a = random_fixed_clean(rng, bits // 2)
                    b = a
                a, b = sorted((a, b))
                if (a * b).bit_length() != bits or a < 17:
                    continue
                cases.append((bits, label, a, b))
                made += 1
    return cases


def write_csv(name: str, fieldnames: list[str], rows: list[dict]) -> None:
    with (BASE / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def run() -> dict:
    started = time.perf_counter()
    rng = random.Random(SEED)
    trace_inputs = {289, 323, 4093}
    small_rows: list[dict] = []
    small_totals = {
        "cases": 0,
        "prime": 0,
        "composite": 0,
        "even": 0,
        "repeated_factor": 0,
        "unbalanced": 0,
        "queries": 0,
        "enumerated_x": 0,
        "audited_boxes": 0,
        "composite_events": 0,
        "covered_composites": 0,
        "boundary_hits": 0,
    }
    representative_traces: dict[str, list[dict]] = {}

    for n in range(2, 4097):
        expected = trial_factor(n)
        actual, oracle, stats = factor_public(n, n in trace_inputs)
        assert actual == expected
        audit = audit_events(stats["events"], True)
        is_prime = len(expected) == 1
        repeated = len(set(expected)) < len(expected)
        unbalanced = len(expected) > 1 and expected[-1] >= 8 * expected[0]
        small_totals["cases"] += 1
        small_totals["prime" if is_prime else "composite"] += 1
        small_totals["even"] += n % 2 == 0
        small_totals["repeated_factor"] += repeated
        small_totals["unbalanced"] += unbalanced
        small_totals["queries"] += oracle.queries
        small_totals["enumerated_x"] += oracle.enumerated_x
        for key in ("audited_boxes", "composite_events", "covered_composites", "boundary_hits"):
            small_totals[key] += audit[key]
        if stats["trace"]:
            representative_traces[str(n)] = stats["trace"]
        small_rows.append(
            {
                "n": n,
                "bits": n.bit_length(),
                "expected": "*".join(map(str, expected)),
                "actual": "*".join(map(str, actual)),
                "oracle_queries": oracle.queries,
                "enumerated_x": oracle.enumerated_x,
                "boxes_generated": stats["boxes_generated"],
                "bisection_queries": stats["bisection_queries"],
            }
        )

    random_rows: list[dict] = []
    random_totals = {
        "cases": 0,
        "queries": 0,
        "enumerated_x": 0,
        "audited_boxes": 0,
        "composite_events": 0,
        "covered_composites": 0,
        "boundary_hits": 0,
        "categories": {},
    }
    for category, n in build_random_cases(rng):
        expected = trial_factor(n)
        actual, oracle, stats = factor_public(n)
        assert actual == expected
        audit = audit_events(stats["events"], False)
        random_totals["cases"] += 1
        random_totals["queries"] += oracle.queries
        random_totals["enumerated_x"] += oracle.enumerated_x
        random_totals["categories"][category] = random_totals["categories"].get(category, 0) + 1
        for key in ("audited_boxes", "composite_events", "covered_composites", "boundary_hits"):
            random_totals[key] += audit[key]
        random_rows.append(
            {
                "category": category,
                "n": n,
                "bits": n.bit_length(),
                "expected": "*".join(map(str, expected)),
                "actual": "*".join(map(str, actual)),
                "oracle_queries": oracle.queries,
                "enumerated_x": oracle.enumerated_x,
                "boxes_generated": stats["boxes_generated"],
                "max_rational_bits": stats["max_rational_bits"],
            }
        )

    large_rows: list[dict] = []
    large_totals = {
        "cases": 0,
        "covered": 0,
        "oracle_queries": 0,
        "boxes_generated": 0,
        "max_box_count": 0,
        "max_rational_bits": 0,
    }
    for bits, label, a, b in build_large_pairs(rng):
        n = a * b
        modulus, boxes, rational_bits = public_boxes(n)
        matches = [
            box
            for box in boxes
            if (
                box.x_lo <= a <= box.x_hi and box.y_lo <= b <= box.y_hi
            )
            or (
                box.x_lo <= b <= box.x_hi and box.y_lo <= a <= box.y_hi
            )
        ]
        assert matches
        for box in boxes:
            assert 1 <= box.x_lo <= box.x_hi < modulus
            assert 1 <= box.y_lo <= box.y_hi < modulus
            assert box.x_lo * box.y_lo > n - modulus
            assert box.x_hi * box.y_hi < n + modulus
        match = matches[0]
        large_totals["cases"] += 1
        large_totals["covered"] += 1
        large_totals["boxes_generated"] += len(boxes)
        large_totals["max_box_count"] = max(large_totals["max_box_count"], len(boxes))
        large_totals["max_rational_bits"] = max(large_totals["max_rational_bits"], rational_bits)
        large_rows.append(
            {
                "bits": bits,
                "label": label,
                "n": n,
                "a": a,
                "b": b,
                "modulus": modulus,
                "box_count": len(boxes),
                "match_grid_index": match.grid_index,
                "match_x_lo": match.x_lo,
                "match_x_hi": match.x_hi,
                "match_y_lo": match.y_lo,
                "match_y_hi": match.y_hi,
                "oracle_queries": 0,
            }
        )

    assert random_totals["categories"] == {
        "random_integer": 30,
        "prime": 30,
        "repeated_factor": 30,
        "unbalanced": 30,
    }
    assert large_totals["cases"] == large_totals["covered"] == 40
    assert large_totals["oracle_queries"] == 0

    write_csv(
        "small_exhaustive.csv",
        [
            "n",
            "bits",
            "expected",
            "actual",
            "oracle_queries",
            "enumerated_x",
            "boxes_generated",
            "bisection_queries",
        ],
        small_rows,
    )
    write_csv(
        "random_cases.csv",
        [
            "category",
            "n",
            "bits",
            "expected",
            "actual",
            "oracle_queries",
            "enumerated_x",
            "boxes_generated",
            "max_rational_bits",
        ],
        random_rows,
    )
    write_csv(
        "large_coverage.csv",
        [
            "bits",
            "label",
            "n",
            "a",
            "b",
            "modulus",
            "box_count",
            "match_grid_index",
            "match_x_lo",
            "match_x_hi",
            "match_y_lo",
            "match_y_hi",
            "oracle_queries",
        ],
        large_rows,
    )

    runtime = time.perf_counter() - started
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result = {
        "status": "complete",
        "seed": SEED,
        "parameters": {
            "ratio": "17/16",
            "fixed_primes": list(FIXED_PRIMES),
            "small_range": [2, 4096],
            "random_cases": 120,
            "random_max_bits": 24,
            "large_bits": [32, 64, 128, 256, 512],
            "large_cases_per_bits": 8,
            "alarm_seconds": ALARM_SECONDS,
        },
        "small": small_totals,
        "random": random_totals,
        "large_coverage": large_totals,
        "representative_traces": representative_traces,
        "runtime_seconds": runtime,
        "peak_rss_bytes": peak_rss,
        "scope": "The Empty oracle enumerates odd x values; it is not a candidate succinct algorithm.",
    }
    (BASE / "output.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def alarm_handler(_signum: int, _frame: object) -> None:
    raise TimeoutError(f"source alarm after {ALARM_SECONDS} seconds")


def main() -> int:
    (BASE / "status.json").write_text(
        json.dumps({"status": "running", "seed": SEED}) + "\n", encoding="utf-8"
    )
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(ALARM_SECONDS)
    try:
        result = run()
    except BaseException as error:
        signal.alarm(0)
        failure = {
            "status": "failed",
            "seed": SEED,
            "error_type": type(error).__name__,
            "error": str(error),
        }
        (BASE / "status.json").write_text(
            json.dumps(failure, indent=2) + "\n", encoding="utf-8"
        )
        traceback.print_exc()
        return 1
    signal.alarm(0)
    (BASE / "status.json").write_text(
        json.dumps(
            {
                "status": "complete",
                "seed": SEED,
                "runtime_seconds": result["runtime_seconds"],
                "peak_rss_bytes": result["peak_rss_bytes"],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": result["status"],
                "small_cases": result["small"]["cases"],
                "random_cases": result["random"]["cases"],
                "large_coverage_cases": result["large_coverage"]["cases"],
                "oracle_queries": result["small"]["queries"]
                + result["random"]["queries"],
                "enumerated_x": result["small"]["enumerated_x"]
                + result["random"]["enumerated_x"],
                "runtime_seconds": result["runtime_seconds"],
                "peak_rss_bytes": result["peak_rss_bytes"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
