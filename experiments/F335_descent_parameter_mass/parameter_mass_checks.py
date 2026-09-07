#!/usr/bin/env python3
"""F335: exact bounded checks for continued-fraction and descent mass formulas."""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time
import traceback


HERE = Path(__file__).resolve().parent
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 100 * 1024 * 1024


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def require(condition, witness):
    if not condition:
        raise AssertionError(json.dumps(witness, sort_keys=True))


def continued_fraction(a, n):
    numerator, denominator = n, a
    digits = []
    triples = []
    older_p, older_q = 1, 0
    previous_p, previous_q = 0, 1
    index = 1
    while denominator:
        digit, remainder = divmod(numerator, denominator)
        signed = a * previous_q - n * previous_p
        positive_remainder = abs(signed)
        require(
            positive_remainder > 0,
            {
                "check": "positive_cf_remainder",
                "n": n,
                "a": a,
                "index": index,
                "digit": digit,
                "p": previous_p,
                "q": previous_q,
                "signed": signed,
            },
        )
        require(
            signed == (positive_remainder if index % 2 else -positive_remainder),
            {
                "check": "signed_cf_remainder",
                "n": n,
                "a": a,
                "index": index,
                "signed": signed,
                "absolute": positive_remainder,
            },
        )
        digits.append(digit)
        triples.append(
            {
                "digit": digit,
                "p_before": previous_p,
                "q_before": previous_q,
                "signed_remainder": signed,
                "remainder": positive_remainder,
            }
        )
        current_p = digit * previous_p + older_p
        current_q = digit * previous_q + older_q
        older_p, previous_p = previous_p, current_p
        older_q, previous_q = previous_q, current_q
        numerator, denominator = denominator, remainder
        index += 1
    require(
        previous_p == a and previous_q == n and digits[-1] >= 2,
        {
            "check": "canonical_cf_terminal",
            "n": n,
            "a": a,
            "digits": digits,
            "final_convergent": [previous_p, previous_q],
        },
    )
    return digits, triples


def harmonic_numbers(limit):
    values = [Fraction(0)]
    for value in range(1, limit + 1):
        values.append(values[-1] + Fraction(1, value))
    return values


def check_continued_fractions(limit):
    started = time.perf_counter()
    counts = Counter()
    maximum_digit_sum = None
    harmonic = harmonic_numbers(limit)
    per_n = []
    for n in range(3, limit + 1, 2):
        all_digits = []
        digit_sum_total = 0
        units = 0
        for a in range(1, n):
            if math.gcd(a, n) != 1:
                continue
            units += 1
            digits, triples = continued_fraction(a, n)
            complement_digits, _ = continued_fraction(n - a, n)
            inverse = pow(a, -1, n)
            inverse_digits, _ = continued_fraction(inverse, n)
            digit_sum = sum(digits)
            require(
                digit_sum == sum(complement_digits) == sum(inverse_digits),
                {
                    "check": "digit_sum_symmetry",
                    "n": n,
                    "a": a,
                    "inverse": inverse,
                    "S_a": digit_sum,
                    "S_complement": sum(complement_digits),
                    "S_inverse": sum(inverse_digits),
                },
            )
            counts["digit_sum_symmetry_checks"] += 1
            digit_sum_total += digit_sum
            all_digits.extend(digits)
            if maximum_digit_sum is None or digit_sum > maximum_digit_sum["S"]:
                maximum_digit_sum = {
                    "n": n,
                    "a": a,
                    "inverse": inverse,
                    "digits": digits,
                    "S": digit_sum,
                }
            for index, triple in enumerate(triples, 1):
                product = (
                    triple["digit"]
                    * triple["q_before"]
                    * triple["remainder"]
                )
                require(
                    product <= n,
                    {
                        "check": "digit_product_bound",
                        "n": n,
                        "a": a,
                        "index": index,
                        "triple": triple,
                        "product": product,
                    },
                )
                require(
                    (
                        a * triple["q_before"]
                        - n * triple["p_before"]
                    )
                    == triple["signed_remainder"],
                    {
                        "check": "digit_signed_congruence",
                        "n": n,
                        "a": a,
                        "index": index,
                        "triple": triple,
                    },
                )
                counts["digit_triple_checks"] += 1

            h = (n - 1) // 2
            q_count = 0
            for t in range(n):
                if t:
                    residue = a * t % n
                    q_count += int(1 <= residue <= h)
                require(
                    abs(2 * q_count - t) <= 10 * digit_sum,
                    {
                        "check": "prefix_discrepancy",
                        "n": n,
                        "a": a,
                        "t": t,
                        "Q": q_count,
                        "S": digit_sum,
                        "discrepancy": 2 * q_count - t,
                    },
                )
                counts["prefix_discrepancy_checks"] += 1

        require(
            Fraction(digit_sum_total)
            <= 2 * n * harmonic[n] * harmonic[n],
            {
                "check": "total_digit_sum_bound",
                "n": n,
                "sum_S": digit_sum_total,
                "right_numerator": (
                    2 * n * harmonic[n] * harmonic[n]
                ).numerator,
                "right_denominator": (
                    2 * n * harmonic[n] * harmonic[n]
                ).denominator,
            },
        )
        counts["total_digit_sum_checks"] += 1
        threshold_checks = 0
        maximum_ratio = Fraction(0)
        for threshold in range(1, n + 1):
            observed = sum(digit >= threshold for digit in all_digits)
            right = (
                Fraction(2 * n, threshold)
                * harmonic[n // threshold]
            )
            require(
                Fraction(observed) <= right,
                {
                    "check": "large_digit_tail_bound",
                    "n": n,
                    "threshold": threshold,
                    "observed": observed,
                    "right_numerator": right.numerator,
                    "right_denominator": right.denominator,
                },
            )
            if right:
                maximum_ratio = max(maximum_ratio, Fraction(observed) / right)
            threshold_checks += 1
            counts["large_digit_tail_checks"] += 1
        per_n.append(
            {
                "n": n,
                "units": units,
                "digit_occurrences": len(all_digits),
                "sum_digit_sums": digit_sum_total,
                "threshold_checks": threshold_checks,
                "maximum_tail_bound_ratio": {
                    "numerator": maximum_ratio.numerator,
                    "denominator": maximum_ratio.denominator,
                },
            }
        )
    return {
        "counts": dict(counts),
        "maximum_digit_sum": maximum_digit_sum,
        "per_n": per_n,
        "walltime_seconds": time.perf_counter() - started,
    }


def direct_Q(n, multiplier, t):
    h = (n - 1) // 2
    return sum(
        1 <= multiplier * y % n <= h
        for y in range(1, t + 1)
    )


def least_prime_factor(n):
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 2
    return n


def descent_sequence(n, multiplier):
    h = (n - 1) // 2
    current = h
    rows = []
    while True:
        q = direct_Q(n, multiplier, current)
        other = current - q
        values = [current]
        if q:
            values.append(q)
        if other:
            values.append(other)
        factor = next(
            (
                divisor
                for value in values
                for divisor in (math.gcd(value, n),)
                if 1 < divisor < n
            ),
            None,
        )
        rows.append(
            {
                "t": current,
                "Q": q,
                "other": other,
                "unordered_children": sorted((q, other)),
                "factor": factor,
            }
        )
        if factor is not None or current <= 1 or q in (0, current):
            return rows
        current = min(q, other)


def check_small_multiplier_descent(limit):
    started = time.perf_counter()
    counts = Counter()
    maximum_residual = None
    returned_factors = Counter()
    for n in range(3, limit + 1, 2):
        h = (n - 1) // 2
        p_min = least_prime_factor(n)
        for multiplier in range(1, min(h, 12) + 1):
            if math.gcd(multiplier, n) != 1:
                continue
            rows = descent_sequence(n, multiplier)
            complement_rows = descent_sequence(n, n - multiplier)
            require(
                [row["t"] for row in rows]
                == [row["t"] for row in complement_rows]
                and [row["unordered_children"] for row in rows]
                == [
                    row["unordered_children"]
                    for row in complement_rows
                ],
                {
                    "check": "complement_descent_symmetry",
                    "n": n,
                    "A": multiplier,
                    "rows": rows,
                    "complement_rows": complement_rows,
                },
            )
            counts["complement_sequence_checks"] += 1
            residual = -multiplier
            factor_returned = None
            for index, row in enumerate(rows):
                t, q, other = row["t"], row["Q"], row["other"]
                quotient, ordinary_remainder = divmod(multiplier * t, n)
                indicator = int(ordinary_remainder <= h)
                coefficient = -quotient if indicator else quotient + 1
                error = (
                    2 * multiplier * q
                    - indicator * 2 * multiplier * t
                    - coefficient * n
                )
                require(
                    abs(error) <= 2 * multiplier * (quotient + 1),
                    {
                        "check": "affine_error_bound",
                        "n": n,
                        "A": multiplier,
                        "index": index,
                        "t": t,
                        "Q": q,
                        "k": quotient,
                        "r": ordinary_remainder,
                        "I": indicator,
                        "c": coefficient,
                        "e": error,
                    },
                )
                residual_q = indicator * residual + error
                residual_other = (1 - indicator) * residual - error
                require(
                    residual_q % n == 2 * multiplier * q % n
                    and residual_other % n
                    == 2 * multiplier * other % n,
                    {
                        "check": "child_residual_congruence",
                        "n": n,
                        "A": multiplier,
                        "index": index,
                        "row": row,
                        "R": residual,
                        "R_q": residual_q,
                        "R_other": residual_other,
                    },
                )
                for child_name, child, child_residual in (
                    ("Q", q, residual_q),
                    ("other", other, residual_other),
                ):
                    if child > 0:
                        require(
                            0 < abs(child_residual)
                            <= 5 * multiplier * multiplier,
                            {
                                "check": "positive_child_residual_bound",
                                "n": n,
                                "A": multiplier,
                                "index": index,
                                "child_name": child_name,
                                "child": child,
                                "residual": child_residual,
                                "row": row,
                            },
                        )
                        counts["positive_child_residual_checks"] += 1
                        if (
                            maximum_residual is None
                            or abs(child_residual)
                            > maximum_residual["absolute_residual"]
                        ):
                            maximum_residual = {
                                "n": n,
                                "A": multiplier,
                                "index": index,
                                "child_name": child_name,
                                "child": child,
                                "residual": child_residual,
                                "absolute_residual": abs(child_residual),
                                "bound": 5 * multiplier * multiplier,
                            }
                counts["affine_error_checks"] += 1
                counts["child_congruence_checks"] += 1
                if row["factor"] is not None:
                    factor_returned = row["factor"]
                    returned_factors[str(factor_returned)] += 1
                    break
                if t <= 1 or q in (0, t):
                    break
                selected_is_q = q <= other
                next_t = q if selected_is_q else other
                next_residual = (
                    residual_q if selected_is_q else residual_other
                )
                next_quotient = multiplier * next_t // n
                require(
                    next_quotient <= quotient // 2,
                    {
                        "check": "quotient_halving",
                        "n": n,
                        "A": multiplier,
                        "index": index,
                        "k": quotient,
                        "next_t": next_t,
                        "k_next": next_quotient,
                    },
                )
                residual = next_residual
                counts["quotient_halving_checks"] += 1
            if p_min > 5 * multiplier * multiplier:
                require(
                    factor_returned is None,
                    {
                        "check": "least_prime_exclusion",
                        "n": n,
                        "A": multiplier,
                        "least_prime": p_min,
                        "bound": 5 * multiplier * multiplier,
                        "factor": factor_returned,
                        "rows": rows,
                    },
                )
                counts["least_prime_exclusion_checks"] += 1
            counts["descent_instances"] += 1
    return {
        "counts": dict(counts),
        "returned_factor_histogram": dict(returned_factors),
        "maximum_child_residual": maximum_residual,
        "walltime_seconds": time.perf_counter() - started,
    }


def primes_in_interval(lower, upper):
    values = []
    for candidate in range(max(2, lower), upper + 1):
        if candidate == 2:
            values.append(candidate)
            continue
        if candidate % 2 == 0:
            continue
        if all(
            candidate % divisor
            for divisor in range(3, math.isqrt(candidate) + 1, 2)
        ):
            values.append(candidate)
    return values


def ceil_fraction(value):
    return -((-value.numerator) // value.denominator)


def direct_menu(n, scale, defect):
    center = Fraction(n - 1, scale)
    lower = max(1, ceil_fraction(center - defect))
    upper = (center + Fraction(defect, 2)).numerator // (
        center + Fraction(defect, 2)
    ).denominator
    return range(lower, upper + 1)


def p_eligible_formula(p, q, scale, defect):
    residue = q % scale
    return (
        q >= scale and p * residue - 1 <= scale * defect
    ) or (
        2 * p * (scale - residue) + 2 <= scale * defect
    )


def scales_for(n, h, defect):
    exponent = 2
    while True:
        scale = 1 << exponent
        upper = Fraction(n - 1, scale) + Fraction(defect, 2)
        if upper < h:
            return
        yield scale
        exponent += 1


def check_dyadic_eligibility():
    started = time.perf_counter()
    counts = Counter()
    summaries = []
    for h in (16, 32, 64, 128):
        primes = primes_in_interval(h, 2 * h)
        for defect in (1, 2, 4, 8):
            if not defect < h / 2:
                continue
            ordered_eligible = 0
            unordered_factor_pairs = 0
            for p in primes:
                for q in primes:
                    n = p * q
                    pair_eligible = False
                    for scale in scales_for(n, h, defect):
                        formula = p_eligible_formula(p, q, scale, defect)
                        menu = direct_menu(n, scale, defect)
                        direct = any(value % p == 0 for value in menu)
                        require(
                            formula == direct,
                            {
                                "check": "dyadic_p_eligibility",
                                "H": h,
                                "D": defect,
                                "p": p,
                                "q": q,
                                "N": n,
                                "scale": scale,
                                "residue": q % scale,
                                "formula": formula,
                                "direct": direct,
                                "menu": [menu.start, menu.stop - 1],
                            },
                        )
                        pair_eligible = pair_eligible or formula
                        counts["ordered_prime_scale_checks"] += 1
                    ordered_eligible += int(pair_eligible)
            for p_index, p in enumerate(primes):
                for q in primes[p_index:]:
                    n = p * q
                    factor_bearing = False
                    for scale in scales_for(n, h, defect):
                        factor_bearing = factor_bearing or any(
                            1 < math.gcd(value, n) < n
                            for value in direct_menu(n, scale, defect)
                        )
                    unordered_factor_pairs += int(factor_bearing)
                    counts["unordered_prime_pair_checks"] += 1

            per_p_integer_counts = {}
            for p in primes:
                eligible_q = 0
                for q in range(h, 2 * h + 1):
                    n = p * q
                    if any(
                        p_eligible_formula(p, q, scale, defect)
                        for scale in scales_for(n, h, defect)
                    ):
                        eligible_q += 1
                per_p_integer_counts[str(p)] = eligible_q
                counts["integer_cofactor_checks"] += h + 1
            max_count = max(per_p_integer_counts.values())
            maximizing_primes = [
                int(p)
                for p, value in per_p_integer_counts.items()
                if value == max_count
            ]
            summaries.append(
                {
                    "H": h,
                    "D": defect,
                    "primes": primes,
                    "ordered_prime_pairs": len(primes) ** 2,
                    "ordered_pairs_with_p_eligible": ordered_eligible,
                    "unordered_prime_pairs": len(primes) * (len(primes) + 1) // 2,
                    "unordered_pairs_with_any_factor_menu": unordered_factor_pairs,
                    "integer_q_counts_by_p": per_p_integer_counts,
                    "maximum_eligible_integer_q_count": max_count,
                    "maximizing_primes": maximizing_primes,
                }
            )
    return {
        "counts": dict(counts),
        "summaries": summaries,
        "walltime_seconds": time.perf_counter() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    source_hash = sha256(Path(__file__))
    design_hash = sha256(HERE / "DESIGN.md")
    running = {
        "status": "running",
        "experiment": "F335_descent_parameter_mass",
        "family": "route:F31",
        "limit": arguments.limit,
        "source_sha256": source_hash,
        "design_sha256": design_hash,
    }
    write_json(arguments.status, running)
    try:
        continued_fractions = check_continued_fractions(arguments.limit)
        small_multiplier_descent = check_small_multiplier_descent(
            arguments.limit
        )
        dyadic_eligibility = check_dyadic_eligibility()
        payload = {
            **running,
            "status": "passed",
            "continued_fractions": continued_fractions,
            "small_multiplier_descent": small_multiplier_descent,
            "dyadic_eligibility": dyadic_eligibility,
            "scope": (
                "Exact bounded formula checks only. Factors are used only "
                "after public gcd outputs as validation labels. No finite "
                "count is promoted to an asymptotic mass law."
            ),
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 100 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "family",
                "limit",
                "source_sha256",
                "design_sha256",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        write_json(arguments.status, status)
        print(
            json.dumps(
                {
                    "event": "passed",
                    **status,
                    "continued_fraction_counts": continued_fractions["counts"],
                    "descent_counts": small_multiplier_descent["counts"],
                    "dyadic_counts": dyadic_eligibility["counts"],
                },
                sort_keys=True,
            ),
            flush=True,
        )
    except BaseException as exception:
        failure = {
            **running,
            "status": "failed",
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        print(json.dumps({"event": "failed", **failure}, sort_keys=True), flush=True)
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
