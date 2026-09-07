#!/usr/bin/env python3
"""Finite diagnostics for F339 algebra and continued-fraction identities."""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import resource
import signal
import statistics
import sys
import time
import traceback


ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT_DIR = ROOT / "experiments" / "F339_coupled_rank_sources"
ALGEBRA = EXPERIMENT_DIR / "ALGEBRA.md"
ALGEBRA_STATEMENT = EXPERIMENT_DIR / "ALGEBRA_STATEMENT_ONLY.md"
CONTINUED_FRACTIONS = EXPERIMENT_DIR / "CONTINUED_FRACTIONS.md"
F337_DIR = ROOT / "experiments" / "F337_random_rank_gaps"
F337_SOURCE = F337_DIR / "random_rank_gaps.py"
SEARCH_SOURCE = EXPERIMENT_DIR / "coupling_search.py"

ALGEBRA_SHA256 = "f16d505b234b039a85016f0c84fdb53deb02098d42692f38dbe7cd12b0d26abd"
ALGEBRA_STATEMENT_SHA256 = (
    "afc08f373adabe1f79314fa1d15666ac0d553e4226748d8b2ca6cf67d9ac4df6"
)
CONTINUED_FRACTIONS_SHA256 = (
    "5e427539c31eb7924fed1448714d51e247d75b16f623f2ba7ccfc5c0f4522e77"
)
F337_SOURCE_SHA256 = (
    "187e35a09f704ce29bdce7c42820a23551801cb835a80fc32575f4732e4e08e1"
)
SEARCH_SOURCE_SHA256 = (
    "c7cedb00a566b850a265dfd7312810166b2c54ee21bc7c027d38bc26a5d51c6c"
)
F337_OUTPUT_HASHES = {
    209: "0041fbac4fa65c00656256869eb2078757aa72f0514f6ba4e2d9c0a2e8e79bf3",
    1333: "4bd39bef4c29dccb42f16c5fc49619d7e21cc14926a8f4b1e96ad1bafa231722",
    10807: "080d11ce2ab306e065c7eb07a0d7f01b838187b15c1818f2ad8618109fd36756",
}
SEARCH_OUTPUT_HASHES = {
    209: "4a3d2e903bbdcb1aa0093c2a7f0ee88614dd701f6a62c163228e1688b8244693",
    1333: "c96951980193b42c13e3d38425bb704a12e861abaea551e12d23ec7d7ba22bee",
    10807: "3ebbe726e93e95e53626a72217fadee84a665a6b47a682f64f7a21b8b90d840a",
}

ROUTE = "route:F31"
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 256 * 1024 * 1024
RUN_PROGRESS = {}


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


def require(condition, check, **context):
    if condition:
        return
    anomaly = {"check": check, **context}
    if "first_anomaly" not in RUN_PROGRESS:
        RUN_PROGRESS["first_anomaly"] = anomaly
    raise ArithmeticError(json.dumps(anomaly, sort_keys=True))


def add_counts(target, source):
    for key, value in source.items():
        if key.startswith("maximum_"):
            target[key] = max(target[key], value)
        else:
            target[key] += value


def fraction_record(value):
    value = Fraction(value)
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "exact": str(value),
        "decimal": float(value),
    }


def fraction_from_record(record):
    return Fraction(record["numerator"], record["denominator"])


def canonical_cf_sum(numerator, denominator):
    require(
        0 < numerator < denominator
        and math.gcd(numerator, denominator) == 1,
        "invalid_cf_input",
        numerator=numerator,
        denominator=denominator,
    )
    left, right = denominator, numerator
    digits = []
    while right:
        quotient, remainder = divmod(left, right)
        digits.append(quotient)
        left, right = right, remainder
    require(
        digits[-1] >= 2,
        "noncanonical_cf_tail",
        numerator=numerator,
        denominator=denominator,
        digits=digits,
    )
    return sum(digits), digits


def charged_gcd(value, modulus, counters, category):
    counters["gcd_calls"] += 1
    counters[category + "_gcd_calls"] += 1
    counters["maximum_gcd_operand_bits"] = max(
        counters["maximum_gcd_operand_bits"],
        abs(value).bit_length(),
        modulus.bit_length(),
    )
    left, right = abs(value), modulus
    divisions = 0
    while right:
        left, right = right, left % right
        divisions += 1
    counters["gcd_euclidean_divisions"] += divisions
    counters[category + "_gcd_euclidean_divisions"] += divisions
    return left


def charged_inverse(value, modulus, counters, category):
    counters["modular_inversion_calls"] += 1
    counters[category + "_modular_inversion_calls"] += 1
    old_r, current_r = modulus, value % modulus
    old_s, current_s = 0, 1
    divisions = 0
    while current_r:
        quotient = old_r // current_r
        old_r, current_r = current_r, old_r - quotient * current_r
        old_s, current_s = current_s, old_s - quotient * current_s
        divisions += 1
    require(
        old_r == 1,
        "inverse_of_nonunit",
        value=value,
        modulus=modulus,
    )
    counters["modular_inverse_euclidean_divisions"] += divisions
    counters[category + "_modular_inverse_euclidean_divisions"] += divisions
    return old_s % modulus


def factorization(value):
    factors = {}
    remaining = value
    prime = 3
    while prime * prime <= remaining:
        while remaining % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            remaining //= prime
        prime += 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def orbit_state(modulus, multiplier, t):
    residues = [multiplier * index % modulus for index in range(t + 1)]
    require(
        len(set(residues)) == t + 1,
        "orbit_not_distinct",
        N=modulus,
        a=multiplier,
        t=t,
    )
    sorted_residues = sorted(residues)
    rank_by_residue = {
        residue: rank for rank, residue in enumerate(sorted_residues)
    }
    ranks = [rank_by_residue[residue] for residue in residues]
    positive = [
        (residues[index], index) for index in range(1, t + 1)
    ]
    alpha, u = min(positive)
    maximum_residue, v = max(positive)
    beta = modulus - maximum_residue
    return {
        "residues": residues,
        "ranks": ranks,
        "alpha": alpha,
        "beta": beta,
        "u": u,
        "v": v,
        "m": t + 1,
        "L": u + v,
        "d": u + v - (t + 1),
    }


def phase_prefixes(L, u, m):
    prefixes = []
    for phase in range(L):
        values = [0]
        for step in range(L):
            values.append(
                values[-1] + int((phase + step * u) % L >= m)
            )
        prefixes.append(values)
    return prefixes


def generic_algebra_checks(limit):
    totals = Counter()
    by_modulus = {}
    for modulus in range(3, limit + 1, 2):
        units = 0
        before_cases = totals["states"]
        before_discrepancy = totals["phase_prefix_checks"]
        for multiplier in range(1, modulus):
            if math.gcd(multiplier, modulus) != 1:
                continue
            units += 1
            S_a, _ = canonical_cf_sum(multiplier, modulus)
            for t in range(1, modulus):
                RUN_PROGRESS.update(
                    {
                        "phase": "generic_algebra",
                        "N": modulus,
                        "a": multiplier,
                        "t": t,
                    }
                )
                state = orbit_state(modulus, multiplier, t)
                alpha = state["alpha"]
                beta = state["beta"]
                u = state["u"]
                L = state["L"]
                m = state["m"]
                d = state["d"]
                require(
                    math.gcd(u, L) == 1
                    and math.gcd(alpha, alpha + beta) == 1,
                    "cf_pairs_not_reduced",
                    N=modulus,
                    a=multiplier,
                    t=t,
                )
                S_rotation, _ = canonical_cf_sum(u, L)
                S_gaps, _ = canonical_cf_sum(alpha, alpha + beta)
                require(
                    S_rotation + S_gaps == S_a + 2,
                    "cf_sum_conservation",
                    N=modulus,
                    a=multiplier,
                    t=t,
                    S_u_L=S_rotation,
                    S_gap=S_gaps,
                    S_a_N=S_a,
                )
                require(
                    S_rotation <= S_a,
                    "cf_rotation_sum_bound",
                    N=modulus,
                    a=multiplier,
                    t=t,
                    S_u_L=S_rotation,
                    S_a_N=S_a,
                )
                totals["cf_conservation_checks"] += 1
                totals["cf_rotation_sum_total"] += S_rotation
                totals["cf_source_sum_total"] += S_a

                prefixes = phase_prefixes(L, u, m)
                for phase in range(L):
                    for q in range(L):
                        deleted = prefixes[phase][q]
                        discrepancy = abs(deleted * L - q * d)
                        require(
                            discrepancy <= 5 * S_rotation * L,
                            "rotation_discrepancy_bound",
                            N=modulus,
                            a=multiplier,
                            t=t,
                            phase=phase,
                            q=q,
                            deleted=deleted,
                            discrepancy_numerator=discrepancy,
                            bound_numerator=5 * S_rotation * L,
                        )
                        require(
                            discrepancy <= 5 * S_a * L,
                            "source_discrepancy_bound",
                            N=modulus,
                            a=multiplier,
                            t=t,
                            phase=phase,
                            q=q,
                            discrepancy_numerator=discrepancy,
                            bound_numerator=5 * S_a * L,
                        )
                        totals["phase_prefix_checks"] += 1
                        totals["maximum_discrepancy_numerator"] = max(
                            totals["maximum_discrepancy_numerator"],
                            discrepancy,
                        )

                b = beta - alpha
                q = b % L
                expected_q = modulus * pow(u, -1, L) % L
                require(
                    q == expected_q,
                    "N_linked_q_identity",
                    N=modulus,
                    a=multiplier,
                    t=t,
                    q=q,
                    expected=expected_q,
                )
                if q == 0:
                    totals["fifth_q_zero_states"] += 1
                else:
                    c = q * u % L
                    require(
                        c == modulus % L,
                        "N_linked_physical_shift",
                        N=modulus,
                        a=multiplier,
                        t=t,
                        c=c,
                        expected=modulus % L,
                    )
                    s = min(q, L - q)
                    Q = modulus // L
                    H_limit = min(d, Q)
                    menu = {
                        value
                        for deleted in range(H_limit + 1)
                        for value in (s - deleted, m - s + deleted)
                        if 1 <= s - deleted < m
                    }
                    for index in range(m):
                        endpoint = (index + c) % L
                        if endpoint >= m:
                            totals["fifth_rejected_pairs"] += 1
                            continue
                        if q > L / 2:
                            start, finish = endpoint, index
                        else:
                            start, finish = index, endpoint
                        H = prefixes[start][s]
                        D = (state["ranks"][finish] - state["ranks"][start]) % m
                        require(
                            D == s - H,
                            "fifth_retained_displacement",
                            N=modulus,
                            a=multiplier,
                            t=t,
                            index=index,
                            H=H,
                            D=D,
                            s=s,
                        )
                        require(
                            H <= Q and H <= d,
                            "fifth_deleted_visit_bound",
                            N=modulus,
                            a=multiplier,
                            t=t,
                            index=index,
                            H=H,
                            Q=Q,
                            d=d,
                        )
                        ordinary_difference = (
                            state["ranks"][endpoint] - state["ranks"][index]
                        )
                        require(
                            abs(ordinary_difference) in menu,
                            "fifth_short_menu_containment",
                            N=modulus,
                            a=multiplier,
                            t=t,
                            index=index,
                            difference=ordinary_difference,
                            menu=sorted(menu),
                        )
                        j = modulus // L + int(index + c >= L)
                        require(
                            endpoint - index == modulus - j * L,
                            "physical_index_identity",
                            N=modulus,
                            a=multiplier,
                            t=t,
                            index=index,
                            endpoint=endpoint,
                            j=j,
                        )
                        physical_difference = (
                            state["residues"][endpoint]
                            - state["residues"][index]
                        ) % modulus
                        require(
                            physical_difference == j * b % modulus,
                            "physical_residue_identity",
                            N=modulus,
                            a=multiplier,
                            t=t,
                            index=index,
                            observed=physical_difference,
                            expected=j * b % modulus,
                        )
                        totals["fifth_accepted_pairs"] += 1
                        totals["maximum_fifth_H"] = max(
                            totals["maximum_fifth_H"], H
                        )
                    totals["fifth_nonzero_states"] += 1
                    totals["maximum_fifth_menu_size"] = max(
                        totals["maximum_fifth_menu_size"], len(menu)
                    )
                totals["states"] += 1
        by_modulus[str(modulus)] = {
            "units": units,
            "states": totals["states"] - before_cases,
            "phase_prefix_checks": (
                totals["phase_prefix_checks"] - before_discrepancy
            ),
        }
        totals["moduli"] += 1
        totals["unit_parameters"] += units
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("generic algebra check exceeded 256 MiB")
    return {
        "limit": limit,
        "scope": "Every odd N, every unit a, every 1<=t<N, and every phase k,q.",
        "totals": dict(sorted(totals.items())),
        "by_modulus": by_modulus,
    }


def half_menu_data(modulus, multiplier):
    t = (modulus - 1) // 2
    inverse = pow(multiplier, -1, modulus)
    r = min(inverse, modulus - inverse)
    orientation = 1 if multiplier * r % modulus == 1 else -1
    require(
        orientation == 1 or multiplier * r % modulus == modulus - 1,
        "centered_inverse_orientation",
        N=modulus,
        a=multiplier,
        r=r,
    )
    s0 = t // r
    state = orbit_state(modulus, multiplier, t)
    if orientation == 1:
        expected = {
            "alpha": 1,
            "u": r,
            "beta": s0 + 1,
            "v": modulus - (s0 + 1) * r,
        }
    else:
        expected = {
            "beta": 1,
            "v": r,
            "alpha": s0 + 1,
            "u": modulus - (s0 + 1) * r,
        }
    for key, value in expected.items():
        require(
            state[key] == value,
            "half_extremum_formula",
            N=modulus,
            a=multiplier,
            r=r,
            key=key,
            observed=state[key],
            expected=value,
        )
    require(
        abs(state["beta"] - state["alpha"]) == s0
        and state["L"] == modulus - s0 * r,
        "half_quotient_L_formula",
        N=modulus,
        a=multiplier,
        r=r,
        s0=s0,
        L=state["L"],
    )

    if r == 1:
        require(
            multiplier in (1, modulus - 1),
            "r_one_multiplier",
            N=modulus,
            a=multiplier,
        )
        s = 1
        arguments = [1, 0, 1, -1]
        gcds = [math.gcd(value, modulus) for value in arguments]
        require(
            not any(1 < divisor < modulus for divisor in gcds),
            "r_one_actual_menu_factor",
            N=modulus,
            a=multiplier,
            raw_quotient=s0,
            gcds=gcds,
        )
        return {
            "r": r,
            "orientation": orientation,
            "raw_quotient": s0,
            "actual_s": s,
            "r_one_special": True,
            "arguments": arguments,
            "gcds": gcds,
            "factors": [],
            "residuals": None,
            "state": state,
        }

    s = s0
    q = (state["beta"] - state["alpha"]) % state["L"]
    centered_s = min(q, state["L"] - q)
    require(
        centered_s == s,
        "half_centered_jump_quotient",
        N=modulus,
        a=multiplier,
        r=r,
        q=q,
        centered=centered_s,
        quotient=s,
    )
    arguments = [s, s - 1, 2 * s - 1, 2 * s - 3]
    R = modulus - 2 * r * s
    require(
        R % 2 == 1 and 1 <= R < 2 * r,
        "half_residual_range",
        N=modulus,
        a=multiplier,
        r=r,
        s=s,
        R=R,
    )
    residuals = [R, R + 2 * r, R + r, R + 3 * r]
    require(
        max(residuals) < 5 * r,
        "half_residual_bound",
        N=modulus,
        a=multiplier,
        r=r,
        residuals=residuals,
    )
    gcds = [math.gcd(value, modulus) for value in arguments]
    residual_gcds = [math.gcd(value, modulus) for value in residuals]
    require(
        gcds == residual_gcds,
        "half_four_gcd_residual_identity",
        N=modulus,
        a=multiplier,
        r=r,
        s=s,
        arguments=arguments,
        residuals=residuals,
        gcds=gcds,
        residual_gcds=residual_gcds,
    )
    return {
        "r": r,
        "orientation": orientation,
        "raw_quotient": s0,
        "actual_s": s,
        "r_one_special": False,
        "arguments": arguments,
        "gcds": gcds,
        "factors": sorted(
            {divisor for divisor in gcds if 1 < divisor < modulus}
        ),
        "residuals": residuals,
        "state": state,
    }


def composite_class(factors):
    exponents = list(factors.values())
    if len(factors) == 1:
        return "prime_power"
    if any(exponent > 1 for exponent in exponents):
        return "nonsquarefree_multiple_primes"
    if len(factors) == 2:
        return "distinct_semiprime"
    return "squarefree_multiple_primes"


def half_orbit_checks(limit):
    totals = Counter()
    semiprime_bounds = []
    rational_classes = defaultdict(Counter)
    rational_examples = defaultdict(list)
    r_one_raw_quotient_examples = []
    per_modulus = {}
    for modulus in range(3, limit + 1, 2):
        RUN_PROGRESS.update({"phase": "half_orbit", "N": modulus})
        units = [a for a in range(1, modulus) if math.gcd(a, modulus) == 1]
        menu_cache = {}
        r_one = 0
        successes = 0
        for multiplier in units:
            data = half_menu_data(modulus, multiplier)
            menu_cache[multiplier] = data
            totals["unit_formula_checks"] += 1
            totals["four_menu_gcd_checks"] += 4
            r_one += data["r_one_special"]
            successes += bool(data["factors"])
            if data["r_one_special"]:
                raw_s = data["raw_quotient"]
                raw_arguments = [
                    raw_s,
                    raw_s - 1,
                    2 * raw_s - 1,
                    2 * raw_s - 3,
                ]
                raw_factors = sorted(
                    {
                        divisor
                        for divisor in (
                            math.gcd(value, modulus)
                            for value in raw_arguments
                        )
                        if 1 < divisor < modulus
                    }
                )
                totals["r_one_raw_quotient_different_source_checks"] += 1
                totals[
                    "r_one_raw_quotient_different_source_factor_parameters"
                ] += bool(raw_factors)
                if raw_factors and len(r_one_raw_quotient_examples) < 12:
                    r_one_raw_quotient_examples.append(
                        {
                            "N": modulus,
                            "a": multiplier,
                            "raw_s": raw_s,
                            "raw_arguments": raw_arguments,
                            "raw_factors": raw_factors,
                            "actual_source_s": 1,
                            "actual_source_factors": [],
                        }
                    )
        totals["unit_parameters"] += len(units)
        totals["r_one_unit_parameters"] += r_one
        totals["menu_success_unit_parameters"] += successes

        factors = factorization(modulus)
        is_prime = factors == {modulus: 1}
        if len(factors) == 2 and set(factors.values()) == {1}:
            primes = sorted(factors)
            centered_units = [
                r
                for r in range(1, (modulus - 1) // 2 + 1)
                if math.gcd(r, modulus) == 1
            ]
            require(
                2 * len(centered_units) == len(units),
                "centered_unit_denominator",
                N=modulus,
                centered=len(centered_units),
                phi=len(units),
            )
            actual_by_prime = {}
            bounds = {}
            successful_union = set()
            for prime in primes:
                count = 0
                for r in centered_units:
                    if r == 1:
                        continue
                    s = ((modulus - 1) // 2) // r
                    arguments = [s, s - 1, 2 * s - 1, 2 * s - 3]
                    argument_gcds = [
                        math.gcd(value, modulus) for value in arguments
                    ]
                    if any(
                        1 < divisor < modulus and divisor % prime == 0
                        for divisor in argument_gcds
                    ):
                        count += 1
                        successful_union.add(r)
                        require(
                            5 * r > prime and 2 * s >= prime,
                            "semiprime_success_size_conditions",
                            N=modulus,
                            prime=prime,
                            r=r,
                            s=s,
                        )
                        inverse_two = pow(2, -1, prime)
                        require(
                            s % prime
                            in {
                                0,
                                1,
                                inverse_two,
                                3 * inverse_two % prime,
                            },
                            "semiprime_success_residue_class",
                            N=modulus,
                            prime=prime,
                            r=r,
                            s=s,
                        )
                bound = 4 * (
                    (5 * modulus) // (2 * prime * prime) + 1
                ) * (
                    (2 * modulus) // (prime * prime) + 1
                )
                require(
                    count <= bound,
                    "semiprime_B_bound",
                    N=modulus,
                    prime=prime,
                    actual=count,
                    bound=bound,
                )
                actual_by_prime[str(prime)] = count
                bounds[str(prime)] = bound
                totals["semiprime_prime_bounds"] += 1
            probability = Fraction(len(successful_union), len(centered_units))
            probability_bound = min(
                Fraction(1),
                Fraction(2 * sum(bounds.values()), len(units)),
            )
            require(
                probability <= probability_bound,
                "semiprime_probability_bound",
                N=modulus,
                actual=str(probability),
                bound=str(probability_bound),
            )
            semiprime_bounds.append(
                {
                    "N": modulus,
                    "primes": primes,
                    "centered_unit_denominator": len(centered_units),
                    "actual_successful_r": len(successful_union),
                    "actual_by_prime": actual_by_prime,
                    "B_by_prime": bounds,
                    "actual_probability": fraction_record(probability),
                    "probability_bound": fraction_record(probability_bound),
                }
            )
            totals["distinct_semiprimes"] += 1

        if not is_prime:
            least_prime = min(factors)
            height = least_prime // 5
            category = composite_class(factors)
            local = Counter()
            local["moduli"] = 1
            local["height"] = height
            local["nonsquarefree"] = int(any(e > 1 for e in factors.values()))
            for x in range(1, height + 1):
                for y in range(1, height + 1):
                    local["candidate_pairs"] += 1
                    divisor_x = math.gcd(x, modulus)
                    if divisor_x > 1:
                        local["numerator_generation_exits"] += 1
                        continue
                    divisor_y = math.gcd(y, modulus)
                    if divisor_y > 1:
                        local["denominator_generation_exits"] += 1
                        continue
                    multiplier = x * pow(y, -1, modulus) % modulus
                    data = menu_cache[multiplier]
                    require(
                        not data["factors"],
                        "bounded_rational_height_factor",
                        N=modulus,
                        factorization=factors,
                        P=least_prime,
                        H=height,
                        x=x,
                        y=y,
                        a=multiplier,
                        r=data["r"],
                        factors=data["factors"],
                    )
                    local["accepted_unit_pairs"] += 1
                    local["r_one_pairs"] += data["r_one_special"]
                    if len(rational_examples[category]) < 4:
                        rational_examples[category].append(
                            {
                                "N": modulus,
                                "factorization": factors,
                                "P": least_prime,
                                "H": height,
                                "x": x,
                                "y": y,
                                "a": multiplier,
                                "r": data["r"],
                            }
                        )
            add_counts(rational_classes[category], local)
            totals["odd_composites"] += 1
            totals["guard_candidate_pairs"] += local["candidate_pairs"]
            totals["guard_accepted_unit_pairs"] += local["accepted_unit_pairs"]
            totals["guard_numerator_generation_exits"] += local[
                "numerator_generation_exits"
            ]
            totals["guard_denominator_generation_exits"] += local[
                "denominator_generation_exits"
            ]

        per_modulus[str(modulus)] = {
            "units": len(units),
            "r_one_units": r_one,
            "menu_success_units": successes,
            "factorization_validation_label": factors,
        }
        totals["moduli"] += 1
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("half-orbit check exceeded 256 MiB")

    require(
        rational_classes["prime_power"]["accepted_unit_pairs"] > 0,
        "prime_power_guard_coverage_missing",
        classes={
            key: dict(value) for key, value in rational_classes.items()
        },
    )
    if limit >= 511:
        require(
            rational_classes[
                "nonsquarefree_multiple_primes"
            ]["accepted_unit_pairs"] > 0,
            "nonsquarefree_guard_coverage_missing",
            classes={
                key: dict(value) for key, value in rational_classes.items()
            },
        )
    return {
        "limit": limit,
        "scope": (
            "Every unit a on every odd N in range. Factorization is used only "
            "for semiprime and bounded-height validation labels."
        ),
        "totals": dict(sorted(totals.items())),
        "semiprime_bounds": semiprime_bounds,
        "bounded_rational_height": {
            "classes": {
                key: dict(sorted(value.items()))
                for key, value in sorted(rational_classes.items())
            },
            "examples": dict(sorted(rational_examples.items())),
        },
        "r_one_raw_quotient_different_source": {
            "scope": (
                "Diagnostic only. These raw-s0 tests are never credited to "
                "the actual centered s=1 source."
            ),
            "examples": r_one_raw_quotient_examples,
        },
        "by_modulus": per_modulus,
    }


def stable_json_sha256(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def rank_map_sha256(ranks):
    digest = hashlib.sha256()
    for index, rank in enumerate(ranks):
        digest.update(f"{index},{rank};".encode())
    return digest.hexdigest()


def gcd_control(values, modulus, category, deduplicate):
    grouped = {}
    for label, value in values:
        canonical = abs(value)
        grouped.setdefault(canonical, []).append(label)
    if deduplicate:
        ordered = [
            (canonical, sorted(labels))
            for canonical, labels in sorted(grouped.items())
        ]
    else:
        ordered = [
            (abs(value), [label]) for label, value in values
        ]
    counters = Counter()
    rows = []
    for argument, labels in ordered:
        divisor = charged_gcd(argument, modulus, counters, category)
        factor = divisor if 1 < divisor < modulus else None
        if factor is not None:
            require(
                modulus % factor == 0,
                "control_factor_not_divisor",
                N=modulus,
                argument=argument,
                factor=factor,
            )
            counters["factor_verification_divisions"] += 1
        rows.append(
            {
                "argument": argument,
                "source_labels": labels,
                "gcd": divisor,
                "factor": factor,
            }
        )
    return {
        "raw_arguments": len(values),
        "tested_arguments": len(rows),
        "rows": rows,
        "factors": sorted(
            {row["factor"] for row in rows if row["factor"] is not None}
        ),
        "success": any(row["factor"] is not None for row in rows),
        "operation_counts": dict(sorted(counters.items())),
    }


def short_rank_menu(modulus, state):
    m = state["m"]
    L = state["L"]
    d = state["d"]
    q = (state["beta"] - state["alpha"]) % L
    if q == 0:
        return {
            "status": "q_zero_failure",
            "q": 0,
            "s": None,
            "Q": modulus // L,
            "H_limit": None,
            "raw_arguments": 0,
            "tested_arguments": 0,
            "rows": [],
            "factors": [],
            "success": False,
            "operation_counts": {},
        }
    s = min(q, L - q)
    Q = modulus // L
    H_limit = min(d, Q)
    values = []
    for deleted in range(H_limit + 1):
        D = s - deleted
        if 1 <= D < m:
            values.append((f"D:h={deleted}", D))
            values.append((f"m-D:h={deleted}", m - D))
    result = gcd_control(values, modulus, "short_menu", True)
    result.update(
        {
            "status": "evaluated",
            "q": q,
            "s": s,
            "Q": Q,
            "H_limit": H_limit,
        }
    )
    require(
        result["tested_arguments"] <= 2 * (H_limit + 1),
        "short_menu_size",
        N=modulus,
        L=L,
        m=m,
        q=q,
        tested=result["tested_arguments"],
        bound=2 * (H_limit + 1),
    )
    return result


def load_frozen_cases(modulus):
    f337_path = F337_DIR / f"full_N{modulus}_output.json"
    search_path = EXPERIMENT_DIR / f"search_N{modulus}_output.json"
    require(
        sha256(f337_path) == F337_OUTPUT_HASHES[modulus],
        "F337_output_hash",
        N=modulus,
    )
    require(
        sha256(search_path) == SEARCH_OUTPUT_HASHES[modulus],
        "search_output_hash",
        N=modulus,
    )
    f337_data = json.loads(f337_path.read_text())
    search_data = json.loads(search_path.read_text())
    require(
        f337_data["status"] == "passed"
        and search_data["status"] == "passed"
        and len(f337_data["cases"]) == len(search_data["cases"]) == 1,
        "frozen_case_status",
        N=modulus,
    )
    return (
        f337_data["cases"][0],
        search_data["cases"][0],
        {
            "F337_path": str(f337_path),
            "F337_sha256": F337_OUTPUT_HASHES[modulus],
            "search_path": str(search_path),
            "search_sha256": SEARCH_OUTPUT_HASHES[modulus],
        },
    )


def fifth_rule_from_cell(cell):
    matches = [
        rule for rule in cell["rules"]
        if rule["rule"] == "q_gap_difference"
    ]
    require(
        len(matches) == 1,
        "missing_fifth_rule",
        t=cell["t"],
        t_scale=cell["t_scale"],
    )
    return matches[0]


def reproduce_fifth_rule(modulus, state, frozen_rule):
    q = (state["beta"] - state["alpha"]) % state["L"]
    require(
        q == frozen_rule["q"],
        "fifth_q_frozen_mismatch",
        N=modulus,
        q=q,
        frozen=frozen_rule["q"],
    )
    if q == 0:
        require(
            frozen_rule["proposal_status"] == "zero_jump_failure"
            and frozen_rule["accepted_starts"] == 0
            and frozen_rule["factor_starts"] == 0,
            "fifth_q_zero_frozen_status",
            N=modulus,
            rule=frozen_rule,
        )
        return {
            "q": 0,
            "accepted_starts": 0,
            "rejected_starts": state["m"],
            "factor_starts": 0,
            "factor_histogram": {},
        }

    L = state["L"]
    m = state["m"]
    u = state["u"]
    c = q * u % L
    inverse_u = pow(u, -1, L)
    base_deleted = [
        int((step * u) % L >= m) for step in range(L)
    ]
    doubled_prefix = [0]
    for value in base_deleted + base_deleted:
        doubled_prefix.append(doubled_prefix[-1] + value)
    s = min(q, L - q)
    Q = modulus // L
    accepted = 0
    factors = Counter()
    for index in range(m):
        endpoint = (index + c) % L
        if endpoint >= m:
            continue
        accepted += 1
        difference = state["ranks"][endpoint] - state["ranks"][index]
        divisor = math.gcd(difference, modulus)
        if 1 < divisor < modulus:
            factors[divisor] += 1
        if q > L / 2:
            start, finish = endpoint, index
        else:
            start, finish = index, endpoint
        rotation_phase = inverse_u * start % L
        H = (
            doubled_prefix[rotation_phase + s]
            - doubled_prefix[rotation_phase]
        )
        D = (state["ranks"][finish] - state["ranks"][start]) % m
        require(
            D == s - H and H <= min(state["d"], Q),
            "frozen_fifth_H_bound",
            N=modulus,
            q=q,
            index=index,
            H=H,
            D=D,
            s=s,
            d=state["d"],
            Q=Q,
        )
    observed_histogram = {str(key): value for key, value in sorted(factors.items())}
    require(
        accepted == frozen_rule["accepted_starts"]
        and m - accepted == frozen_rule["rejected_starts"]
        and sum(factors.values()) == frozen_rule["factor_starts"]
        and observed_histogram == frozen_rule["factor_histogram"],
        "fifth_rule_array_reproduction",
        N=modulus,
        q=q,
        accepted=accepted,
        frozen_accepted=frozen_rule["accepted_starts"],
        factors=observed_histogram,
        frozen_factors=frozen_rule["factor_histogram"],
    )
    return {
        "q": q,
        "accepted_starts": accepted,
        "rejected_starts": m - accepted,
        "factor_starts": sum(factors.values()),
        "factor_histogram": observed_histogram,
    }


def menu_total_counts(parameter_counts, setup_counts, menu_counts):
    totals = Counter()
    add_counts(totals, parameter_counts)
    add_counts(totals, setup_counts)
    totals["jump_integer_subtractions"] += 1
    totals["jump_modular_reductions"] += 1
    totals["quotient_integer_divisions"] += 1
    add_counts(totals, menu_counts)
    return dict(sorted(totals.items()))


def half_quotient_control(modulus, multiplier, generation_counts):
    counts = Counter()
    inverse = charged_inverse(
        multiplier, modulus, counts, "half_source"
    )
    r = min(inverse, modulus - inverse)
    counts["centered_inverse_comparisons"] += 1
    if r == 1:
        counts["r_one_special_branches"] += 1
        total = Counter(generation_counts)
        add_counts(total, counts)
        return {
            "status": "r_one_special_failure",
            "r": 1,
            "raw_quotient": (modulus - 1) // 2,
            "actual_s": 1,
            "raw_quotient_four_tests_executed": False,
            "menu": {
                "raw_arguments": 0,
                "tested_arguments": 0,
                "rows": [],
                "factors": [],
                "success": False,
                "operation_counts": {},
            },
            "algorithm_operation_counts": dict(sorted(total.items())),
        }
    counts["quotient_integer_divisions"] += 1
    t = (modulus - 1) // 2
    s = t // r
    values = [
        ("s", s),
        ("s-1", s - 1),
        ("2s-1", 2 * s - 1),
        ("2s-3", 2 * s - 3),
    ]
    menu = gcd_control(values, modulus, "half_four_menu", False)
    add_counts(counts, menu["operation_counts"])
    total = Counter(generation_counts)
    add_counts(total, counts)
    return {
        "status": "evaluated",
        "r": r,
        "raw_quotient": s,
        "actual_s": s,
        "raw_quotient_four_tests_executed": True,
        "menu": menu,
        "algorithm_operation_counts": dict(sorted(total.items())),
    }


def frozen_source_checks(pilot):
    moduli = (209,) if pilot else (209, 1333, 10807)
    records = []
    source_artifacts = []
    totals = Counter()
    for modulus in moduli:
        f337_case, search_case, artifact = load_frozen_cases(modulus)
        source_artifacts.append(artifact)
        search_parameters = {
            row["attempt_id"]: row for row in search_case["parameters"]
        }
        for parameter in f337_case["parameters"]:
            attempt_index = int(parameter["attempt_id"].split(":")[1])
            if pilot and attempt_index >= 2:
                continue
            search_parameter = search_parameters.get(parameter["attempt_id"])
            require(
                search_parameter is not None,
                "missing_search_parameter",
                attempt_id=parameter["attempt_id"],
            )
            require(
                search_parameter["frozen_parameter_sha256"]
                == stable_json_sha256(parameter),
                "frozen_parameter_digest",
                attempt_id=parameter["attempt_id"],
            )
            base = {
                "attempt_id": parameter["attempt_id"],
                "modulus": modulus,
                "policy": parameter["policy"],
                "policy_kind": parameter["policy_kind"],
                "gamma": parameter["gamma"],
                "parameters": parameter["parameters"],
                "source_seeds": parameter["source_seeds"],
                "source_ranges": parameter["source_ranges"],
                "generation_operation_counts": parameter[
                    "generation_operation_counts"
                ],
                "generation_factors": parameter["generation_factors"],
                "frozen_parameter_sha256": stable_json_sha256(parameter),
            }
            if parameter["status"] == "generation_factor":
                require(
                    search_parameter["status"] == "generation_factor"
                    and parameter["generation_factors"]
                    == search_parameter["generation_factors"],
                    "generation_record_mismatch",
                    attempt_id=parameter["attempt_id"],
                )
                for factor in parameter["generation_factors"]:
                    require(
                        1 < factor < modulus and modulus % factor == 0,
                        "generation_factor_invalid",
                        attempt_id=parameter["attempt_id"],
                        factor=factor,
                    )
                records.append(
                    {
                        **base,
                        "status": "generation_factor",
                        "a": None,
                        "t_scale": None,
                        "source_attempt_denominator": 1,
                    }
                )
                totals["generation_factor_records"] += 1
                continue

            require(
                parameter["status"] == search_parameter["status"] == "unit"
                and parameter["a"] == search_parameter["a"],
                "unit_parameter_mismatch",
                attempt_id=parameter["attempt_id"],
            )
            multiplier = parameter["a"]
            search_cells = {
                (cell["t_scale"], cell["t"]): cell
                for cell in search_parameter["cells"]
            }
            for source_cell in parameter["cells"]:
                if source_cell["t_scale"] not in ("eighth", "half"):
                    continue
                key = (source_cell["t_scale"], source_cell["t"])
                search_cell = search_cells.get(key)
                require(
                    search_cell is not None,
                    "missing_search_cell",
                    attempt_id=parameter["attempt_id"],
                    key=key,
                )
                state = orbit_state(modulus, multiplier, source_cell["t"])
                extrema = source_cell["extrema"]
                for source_key, state_key in (
                    ("alpha", "alpha"),
                    ("beta", "beta"),
                    ("u", "u"),
                    ("v", "v"),
                    ("m", "m"),
                    ("u_plus_v", "L"),
                ):
                    require(
                        extrema[source_key] == state[state_key],
                        "F337_array_extremum",
                        attempt_id=parameter["attempt_id"],
                        t_scale=source_cell["t_scale"],
                        key=source_key,
                        frozen=extrema[source_key],
                        direct=state[state_key],
                    )
                require(
                    rank_map_sha256(state["ranks"])
                    == search_cell["rank_map_sha256"],
                    "search_rank_map_digest",
                    attempt_id=parameter["attempt_id"],
                    t_scale=source_cell["t_scale"],
                )
                S_a, _ = canonical_cf_sum(multiplier, modulus)
                S_rotation, _ = canonical_cf_sum(state["u"], state["L"])
                S_gaps, _ = canonical_cf_sum(
                    state["alpha"], state["alpha"] + state["beta"]
                )
                require(
                    S_rotation + S_gaps == S_a + 2,
                    "frozen_cell_cf_conservation",
                    attempt_id=parameter["attempt_id"],
                    t_scale=source_cell["t_scale"],
                )

                frozen_rule = fifth_rule_from_cell(search_cell)
                reproduced = reproduce_fifth_rule(
                    modulus, state, frozen_rule
                )
                short_menu = short_rank_menu(modulus, state)
                require(
                    not reproduced["factor_starts"]
                    or short_menu["success"],
                    "short_menu_does_not_cover_fifth",
                    attempt_id=parameter["attempt_id"],
                    t_scale=source_cell["t_scale"],
                    factor_starts=reproduced["factor_starts"],
                    menu=short_menu,
                )
                if source_cell["t_scale"] == "half":
                    require(
                        short_menu["q"] == 0 or short_menu["Q"] == 1,
                        "half_Q_not_one",
                        attempt_id=parameter["attempt_id"],
                        Q=short_menu["Q"],
                    )
                    quotient = half_quotient_control(
                        modulus,
                        multiplier,
                        parameter["generation_operation_counts"],
                    )
                    require(
                        quotient["menu"]["success"] == short_menu["success"]
                        and quotient["menu"]["factors"]
                        == short_menu["factors"],
                        "half_quotient_short_menu_mismatch",
                        attempt_id=parameter["attempt_id"],
                        quotient=quotient["menu"],
                        rank_menu=short_menu,
                    )
                    if quotient["r"] == 1:
                        totals["frozen_r_one_cells"] += 1
                else:
                    require(
                        short_menu["q"] == 0 or short_menu["Q"] <= 7,
                        "eighth_Q_bound",
                        attempt_id=parameter["attempt_id"],
                        Q=short_menu["Q"],
                    )
                    quotient = None

                total_counts = menu_total_counts(
                    parameter["generation_operation_counts"],
                    source_cell["setup_operation_counts"],
                    short_menu["operation_counts"],
                )
                basic_t = bool(
                    source_cell["controls"]["factor_at_t"]
                    or source_cell["controls"]["factor_at_t_plus_one"]
                )
                record = {
                    **base,
                    "status": "unit_cell",
                    "a": multiplier,
                    "t": source_cell["t"],
                    "t_scale": source_cell["t_scale"],
                    "source_attempt_denominator": 1,
                    "endpoint_start_denominator": state["m"],
                    "continued_fraction": {
                        "S_a_N": S_a,
                        "S_u_L": S_rotation,
                        "S_gap": S_gaps,
                    },
                    "extrema": {
                        key: state[key]
                        for key in ("alpha", "beta", "u", "v", "m", "L", "d")
                    },
                    "fifth_coupling": {
                        **reproduced,
                        "proposal_status": frozen_rule["proposal_status"],
                        "unconditional_factor_probability": frozen_rule[
                            "unconditional_factor_probability"
                        ],
                        "acceptance_probability": frozen_rule[
                            "acceptance_probability"
                        ],
                        "expected_algorithm_operation_counts": frozen_rule[
                            "expected_algorithm_operation_counts"
                        ],
                    },
                    "short_rank_menu": {
                        **short_menu,
                        "algorithm_operation_counts": total_counts,
                    },
                    "half_quotient_menu": quotient,
                    "basic_controls": {
                        "t_or_t_plus_one_factor": basic_t,
                        "fifth_eleven_value_factor": frozen_rule[
                            "basic_direct_control_factor"
                        ],
                    },
                }
                records.append(record)
                totals["unit_cells"] += 1
                totals["half_cells"] += source_cell["t_scale"] == "half"
                totals["eighth_cells"] += source_cell["t_scale"] == "eighth"
                totals["q_zero_cells"] += short_menu["status"] == "q_zero_failure"
                totals["short_menu_success_cells"] += short_menu["success"]
                totals["fifth_positive_cells"] += bool(
                    reproduced["factor_starts"]
                )
                totals["basic_t_control_cells"] += basic_t
                totals["basic_eleven_control_cells"] += frozen_rule[
                    "basic_direct_control_factor"
                ]
                totals["maximum_short_menu_arguments"] = max(
                    totals["maximum_short_menu_arguments"],
                    short_menu["tested_arguments"],
                )
        totals["source_moduli"] += 1
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("frozen-source check exceeded 256 MiB")

    summaries = summarize_frozen_records(records)
    expected_parameters = 14 if pilot else 168
    expected_cells = None if pilot else 306
    source_records = len(
        {
            record["attempt_id"] for record in records
        }
    )
    require(
        source_records == expected_parameters,
        "source_record_coverage",
        pilot=pilot,
        observed=source_records,
        expected=expected_parameters,
    )
    if expected_cells is not None:
        require(
            totals["unit_cells"] == expected_cells,
            "frozen_cell_coverage",
            observed=totals["unit_cells"],
            expected=expected_cells,
        )
    return {
        "scope": (
            "First two N=209 indices from every source law."
            if pilot
            else "All frozen F337 source records and every half/eighth unit cell."
        ),
        "source_artifacts": source_artifacts,
        "totals": dict(sorted(totals.items())),
        "summaries": summaries,
        "records": records,
    }


def summarize_frozen_records(records):
    generation_by_policy = defaultdict(list)
    unit_by_key = defaultdict(list)
    for record in records:
        if record["status"] == "generation_factor":
            generation_by_policy[record["policy"]].append(record)
        else:
            unit_by_key[
                (record["modulus"], record["policy"], record["t_scale"])
            ].append(record)
    output = []
    for key, unit_rows in sorted(unit_by_key.items()):
        modulus, policy, t_scale = key
        generation_rows = [
            row for row in generation_by_policy[policy]
            if row["modulus"] == modulus
        ]
        attempts = len(unit_rows) + len(generation_rows)
        unit_menu_successes = sum(
            row["short_rank_menu"]["success"] for row in unit_rows
        )
        menu_successes = len(generation_rows) + unit_menu_successes
        unit_quotient_successes = (
            sum(
                row["half_quotient_menu"]["menu"]["success"]
                for row in unit_rows
            )
            if t_scale == "half"
            else None
        )
        quotient_successes = (
            len(generation_rows) + unit_quotient_successes
            if unit_quotient_successes is not None
            else None
        )
        coupling_probability_sum = Fraction(len(generation_rows))
        coupling_expected_counts = defaultdict(Fraction)
        menu_counts = Counter()
        quotient_counts = Counter()
        for row in generation_rows:
            add_counts(menu_counts, row["generation_operation_counts"])
            for operation, value in row["generation_operation_counts"].items():
                if not operation.startswith("maximum_"):
                    coupling_expected_counts[operation] += Fraction(value)
            if t_scale == "half":
                add_counts(quotient_counts, row["generation_operation_counts"])
        for row in unit_rows:
            coupling_probability_sum += fraction_from_record(
                row["fifth_coupling"]["unconditional_factor_probability"]
            )
            for operation, value in row["fifth_coupling"][
                "expected_algorithm_operation_counts"
            ].items():
                coupling_expected_counts[operation] += fraction_from_record(value)
            add_counts(
                menu_counts,
                row["short_rank_menu"]["algorithm_operation_counts"],
            )
            if t_scale == "half":
                add_counts(
                    quotient_counts,
                    row["half_quotient_menu"]["algorithm_operation_counts"],
                )
        output.append(
            {
                "modulus": modulus,
                "policy": policy,
                "t_scale": t_scale,
                "source_attempts": attempts,
                "generation_factor_attempts": len(generation_rows),
                "unit_cells": len(unit_rows),
                "distinct_unit_parameters": len(
                    {row["a"] for row in unit_rows}
                ),
                "duplicate_unit_parameters": len(unit_rows)
                - len({row["a"] for row in unit_rows}),
                "q_zero_cells": sum(
                    row["short_rank_menu"]["status"] == "q_zero_failure"
                    for row in unit_rows
                ),
                "r_one_cells": sum(
                    row["half_quotient_menu"] is not None
                    and row["half_quotient_menu"]["r"] == 1
                    for row in unit_rows
                ),
                "unit_short_menu_successes": unit_menu_successes,
                "standalone_short_menu_total_successes": menu_successes,
                "short_menu_success_rate": fraction_record(
                    Fraction(menu_successes, attempts)
                ),
                "unit_half_quotient_successes": unit_quotient_successes,
                "standalone_half_quotient_total_successes": quotient_successes,
                "half_quotient_success_rate": (
                    fraction_record(Fraction(quotient_successes, attempts))
                    if quotient_successes is not None
                    else None
                ),
                "fifth_coupling_source_probability": fraction_record(
                    coupling_probability_sum / attempts
                ),
                "fifth_positive_unit_cells": sum(
                    row["fifth_coupling"]["factor_starts"] > 0
                    for row in unit_rows
                ),
                "basic_t_control_cells": sum(
                    row["basic_controls"]["t_or_t_plus_one_factor"]
                    for row in unit_rows
                ),
                "basic_eleven_control_cells": sum(
                    row["basic_controls"]["fifth_eleven_value_factor"]
                    for row in unit_rows
                ),
                "short_menu_algorithm_operation_totals": dict(
                    sorted(menu_counts.items())
                ),
                "short_menu_cost_per_success": (
                    {
                        operation: fraction_record(
                            Fraction(value, menu_successes)
                        )
                        for operation, value in sorted(menu_counts.items())
                        if value and not operation.startswith("maximum_")
                    }
                    if menu_successes
                    else None
                ),
                "half_quotient_algorithm_operation_totals": (
                    dict(sorted(quotient_counts.items()))
                    if t_scale == "half"
                    else None
                ),
                "half_quotient_cost_per_success": (
                    {
                        operation: fraction_record(
                            Fraction(value, quotient_successes)
                        )
                        for operation, value in sorted(
                            quotient_counts.items()
                        )
                        if value and not operation.startswith("maximum_")
                    }
                    if quotient_successes
                    else None
                ),
                "fifth_coupling_expected_operation_totals": {
                    operation: fraction_record(value)
                    for operation, value in sorted(
                        coupling_expected_counts.items()
                    )
                },
                "fifth_coupling_cost_per_success": (
                    {
                        operation: fraction_record(
                            value / coupling_probability_sum
                        )
                        for operation, value in sorted(
                            coupling_expected_counts.items()
                        )
                        if value
                    }
                    if coupling_probability_sum
                    else None
                ),
            }
        )
    return output


def validate_dependencies():
    expected = {
        ALGEBRA: ALGEBRA_SHA256,
        ALGEBRA_STATEMENT: ALGEBRA_STATEMENT_SHA256,
        CONTINUED_FRACTIONS: CONTINUED_FRACTIONS_SHA256,
        F337_SOURCE: F337_SOURCE_SHA256,
        SEARCH_SOURCE: SEARCH_SOURCE_SHA256,
    }
    for path, expected_hash in expected.items():
        require(
            sha256(path) == expected_hash,
            "dependency_hash",
            path=str(path),
            expected=expected_hash,
            observed=sha256(path),
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("pilot", "identities", "frozen", "aggregate"),
        required=True,
    )
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    arguments = parser.parse_args()
    validate_dependencies()
    started = time.perf_counter()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F339_coupled_rank_sources",
        "route": ROUTE,
        "mode": arguments.mode,
        "source_sha256": sha256(Path(__file__)),
    }
    write_json(arguments.status, running)
    try:
        if arguments.mode == "pilot":
            payload = {
                "status": "passed",
                "experiment": "F339_coupled_rank_sources",
                "route": ROUTE,
                "mode": "pilot",
                "generic": generic_algebra_checks(11),
                "half_orbit": half_orbit_checks(51),
                "frozen_sources": frozen_source_checks(True),
            }
        elif arguments.mode == "identities":
            payload = {
                "status": "passed",
                "experiment": "F339_coupled_rank_sources",
                "route": ROUTE,
                "mode": "identities",
                "generic": generic_algebra_checks(31),
                "half_orbit": half_orbit_checks(511),
            }
        elif arguments.mode == "frozen":
            payload = {
                "status": "passed",
                "experiment": "F339_coupled_rank_sources",
                "route": ROUTE,
                "mode": "frozen",
                "frozen_sources": frozen_source_checks(False),
            }
        else:
            identity_path = EXPERIMENT_DIR / "algebra_identities_output.json"
            frozen_path = EXPERIMENT_DIR / "algebra_frozen_output.json"
            identity = json.loads(identity_path.read_text())
            frozen = json.loads(frozen_path.read_text())
            require(
                identity["status"] == frozen["status"] == "passed",
                "aggregate_input_status",
            )
            require(
                identity["source_sha256"]
                == frozen["source_sha256"]
                == sha256(Path(__file__)),
                "aggregate_source_hash",
            )
            payload = {
                "status": "passed",
                "experiment": "F339_coupled_rank_sources",
                "route": ROUTE,
                "mode": "aggregate",
                "identity_output": {
                    "path": str(identity_path),
                    "sha256": sha256(identity_path),
                },
                "frozen_output": {
                    "path": str(frozen_path),
                    "sha256": sha256(frozen_path),
                },
                "generic": identity["generic"],
                "half_orbit": identity["half_orbit"],
                "frozen_sources": frozen["frozen_sources"],
            }
        signal.alarm(0)
        payload.update(
            {
                "source_sha256": sha256(Path(__file__)),
                "dependency_sha256": {
                    "ALGEBRA": ALGEBRA_SHA256,
                    "ALGEBRA_STATEMENT_ONLY": ALGEBRA_STATEMENT_SHA256,
                    "CONTINUED_FRACTIONS": CONTINUED_FRACTIONS_SHA256,
                    "F337_source": F337_SOURCE_SHA256,
                    "coupling_search_source": SEARCH_SOURCE_SHA256,
                },
                "first_anomaly": RUN_PROGRESS.get("first_anomaly"),
                "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
                "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
                "memory_limit_bytes": MEMORY_LIMIT_BYTES,
                "walltime_seconds": time.perf_counter() - started,
                "peak_rss_bytes": peak_rss_bytes(),
            }
        )
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("algebra check exceeded 256 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "route",
                "mode",
                "source_sha256",
                "first_anomaly",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        write_json(arguments.status, status)
        print(json.dumps({"event": "passed", **status}), flush=True)
    except TimeoutError as exception:
        signal.alarm(0)
        censored = {
            **running,
            "status": "censored",
            "censor_reason": "internal_timeout",
            "exception": str(exception),
            "progress": RUN_PROGRESS,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, censored)
        write_json(arguments.status, censored)
        print(json.dumps({"event": "censored", **censored}), flush=True)
    except BaseException as exception:
        signal.alarm(0)
        failed = {
            **running,
            "status": "failed",
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "progress": RUN_PROGRESS,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failed)
        write_json(arguments.status, failed)
        print(json.dumps({"event": "failed", **failed}), flush=True)
        raise


if __name__ == "__main__":
    main()
