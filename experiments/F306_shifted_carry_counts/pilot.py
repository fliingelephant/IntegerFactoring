#!/usr/bin/env python3
"""Exact finite evidence for the shifted binomial-carry count bridge."""

import json
import math
from pathlib import Path
import random
import resource
import signal
import sys
import time

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parent / "F301_factor_rectangles"))
import factor_rectangles as reference


def carry_sum(n, modulus, c, d):
    total = 0
    for u in range(1, modulus, 2):
        v = n * pow(u, -1, modulus) % modulus
        x = u + modulus * (u < c)
        y = v + modulus * (v < d)
        q = (x * y - n) // modulus
        total += q * (q - 1) // 2
    return total % modulus


def carry_count(n, modulus, a, b, c, d):
    contrast = (
        carry_sum(n, modulus, b, d)
        - carry_sum(n, modulus, a, d)
        - carry_sum(n, modulus, b, c)
        + carry_sum(n, modulus, a, c)
    ) % modulus
    return contrast * pow(n - modulus // 2, -1, modulus) % modulus


class CarryEmpty(reference.ReferenceEmpty):
    def empty(self, n, modulus, box):
        self.queries += 1
        self.enumerated_x += 4 * (modulus // 2)
        self.max_x_scanned_in_query = max(
            self.max_x_scanned_in_query, 4 * (modulus // 2)
        )
        count = carry_count(
            n, modulus, box.x_lo, box.x_hi + 1,
            box.y_lo, box.y_hi + 1,
        )
        if count:
            self.nonempty_queries += 1
        else:
            self.empty_queries += 1
        return count == 0


def run():
    started = time.monotonic()
    rng = random.Random(30620260907)
    rectangle_checks = 0
    general_cases = []
    for k in range(2, 12):
        modulus = 1 << k
        for n in (1, 8 * modulus + 1, 8 * modulus + 3,
                  9 * modulus + 1, 16 * modulus**2 + 3):
            graph = [(u, n * pow(u, -1, modulus) % modulus)
                     for u in range(1, modulus, 2)]
            boxes = [(0, modulus, 0, modulus), (0, 0, 0, modulus),
                     (0, modulus, modulus, modulus),
                     (0, 2, 0, modulus), (1, modulus, 1, modulus)]
            for _ in range(19):
                a, b = sorted((rng.randrange(modulus + 1),
                               rng.randrange(modulus + 1)))
                c, d = sorted((rng.randrange(modulus + 1),
                               rng.randrange(modulus + 1)))
                boxes.append((a, b, c, d))
            for a, b, c, d in boxes:
                exact = sum(a <= u < b and c <= v < d for u, v in graph)
                got = carry_count(n, modulus, a, b, c, d)
                assert got == exact, (k, n, a, b, c, d, exact, got)
                rectangle_checks += 1
            general_cases.append({"k": k, "N": n, "rectangles": len(boxes)})

    reference.ReferenceEmpty = CarryEmpty
    factor_cases = []
    public_rectangle_checks = 0
    for n in (2, 17, 289, 323, 361, 391, 437, 493, 527, 551, 589,
              667, 899, 997, 1009, 1147, 1517, 1763, 2017, 2021, 2491):
        factors, oracle, stats = reference.factor_public(n)
        assert factors == reference.trial_factor(n), (n, factors)
        assert math.prod(factors) == n
        factor_cases.append({"N": n, "factors": factors,
                             "rectangle_calls": oracle.queries,
                             "B_calls": 4 * oracle.queries,
                             "reference_units": oracle.enumerated_x})
        if n >= 289:
            modulus, boxes, _ = reference.public_boxes(n)
            for box in boxes:
                got = carry_count(n, modulus, box.x_lo, box.x_hi + 1,
                                  box.y_lo, box.y_hi + 1)
                expected = sum(
                    n % u == 0 and box.y_lo <= n // u <= box.y_hi
                    for u in range(box.x_lo | 1, box.x_hi + 1, 2)
                )
                assert got == expected, (n, box, got, expected)
                public_rectangle_checks += 1

    n, modulus = 289, 32
    corners = {f"{c},{d}": carry_sum(n, modulus, c, d)
               for c in (17, 18) for d in (17, 18)}
    contrast = (corners["18,18"] - corners["17,18"]
                - corners["18,17"] + corners["17,17"]) % modulus
    carry_square_sum = 0
    for u in range(1, modulus, 2):
        v = n * pow(u, -1, modulus) % modulus
        q = ((u + modulus * (u < 2)) * v - n) // modulus
        carry_square_sum += q * q
    assert carry_square_sum % 2 == 1
    assert contrast == 17
    assert contrast * pow(n - modulus // 2, -1, modulus) % modulus == 1
    assert contrast * pow(n, -1, modulus) % modulus == 17

    return {
        "status": "passed",
        "scope": "Finite reference checks only; B enumerates the inverse graph.",
        "rectangle_checks": rectangle_checks,
        "public_rectangle_checks": public_rectangle_checks,
        "general_cases": general_cases,
        "factor_cases": factor_cases,
        "guard_witness": {"N": n, "M": modulus, "box": [17, 18, 17, 18],
                          "B_corners": corners, "contrast_mod_M": contrast,
                          "correct_count": 1, "omitting_half_modulus": 17,
                          "Q2_at_c2_d0": carry_square_sum},
        "elapsed_seconds": time.monotonic() - started,
        "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "timeout_seconds": 30,
    }


if __name__ == "__main__":
    signal.alarm(30)
    result = run()
    text = json.dumps(result, indent=2) + "\n"
    with (BASE / "output.json").open("x") as out:
        out.write(text)
    print(text, end="")
