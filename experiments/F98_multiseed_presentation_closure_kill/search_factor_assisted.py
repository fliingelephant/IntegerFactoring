#!/usr/bin/env python3
"""Factor-assisted discovery search for an F98 C2T counterexample.

This file is only an input finder and hostile over-approximation. It uses
prime factorization of public relation products to give the decoder a fully
prime-refined parity matrix. A final candidate must be replayed by a separate
factorization-free executable.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path


def primes_through(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [i for i, flag in enumerate(sieve) if flag]


def is_prime_u64(value: int) -> bool:
    if value < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if value % p == 0:
            return value == p
    odd = value - 1
    shift = 0
    while odd % 2 == 0:
        odd //= 2
        shift += 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        x = pow(base, odd, value)
        if x in (1, value - 1):
            continue
        for _ in range(shift - 1):
            x = x * x % value
            if x == value - 1:
                break
        else:
            return False
    return True


def pollard_divisor(value: int) -> int:
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % p == 0:
            return p
    constant = 1
    while True:
        x = 2
        y = 2
        divisor = 1
        while divisor == 1:
            x = (x * x + constant) % value
            y = (y * y + constant) % value
            y = (y * y + constant) % value
            divisor = math.gcd(abs(x - y), value)
        if divisor != value:
            return divisor
        constant += 1


def factor_u64(value: int) -> dict[int, int]:
    primes: list[int] = []
    stack = [value]
    while stack:
        current = stack.pop()
        if current == 1:
            continue
        if is_prime_u64(current):
            primes.append(current)
            continue
        divisor = pollard_divisor(current)
        stack.extend((divisor, current // divisor))
    result: dict[int, int] = {}
    for p in primes:
        result[p] = result.get(p, 0) + 1
    return dict(sorted(result.items()))


def stable(p: int, q: int) -> bool:
    g = math.gcd(p - 1, q - 1)
    a = (p - 1) // g
    b = (q - 1) // g
    return math.gcd(a * b, p * q - 1) == 1


class PrimeDecoder:
    def __init__(self, modulus: int):
        self.modulus = modulus
        self.prime_rows: dict[int, int] = {}
        self.pivots: dict[int, tuple[int, int]] = {}
        self.relation_factors: list[dict[int, int]] = []
        self.dependencies = 0
        self.global_dependencies = 0
        self.factor: int | None = None
        self.factor_method: str | None = None
        self.factor_dependency_size: int | None = None
        self.factor_witness: dict[str, object] | None = None

    def add(self, factors: dict[int, int]) -> None:
        parity = 0
        for p, exponent in factors.items():
            row = self.prime_rows.setdefault(p, len(self.prime_rows))
            if exponent & 1:
                parity ^= 1 << row
        relation_index = len(self.relation_factors)
        self.relation_factors.append(factors)
        combination = 1 << relation_index
        reduced = parity
        while reduced:
            pivot = reduced.bit_length() - 1
            old = self.pivots.get(pivot)
            if old is None:
                self.pivots[pivot] = (reduced, combination)
                return
            reduced ^= old[0]
            combination ^= old[1]
        self.dependencies += 1
        exponents: dict[int, int] = {}
        bits = combination
        while bits:
            low = bits & -bits
            index = low.bit_length() - 1
            for p, exponent in self.relation_factors[index].items():
                exponents[p] = exponents.get(p, 0) + exponent
            bits ^= low
        root = 1
        for p, exponent in exponents.items():
            if exponent & 1:
                raise AssertionError("Parity elimination returned a nonsquare.")
            root = root * pow(p, exponent // 2, self.modulus) % self.modulus
        minus = math.gcd(root - 1, self.modulus)
        plus = math.gcd(root + 1, self.modulus)
        if 1 < minus < self.modulus:
            self.factor = minus
        elif 1 < plus < self.modulus:
            self.factor = plus
        else:
            self.global_dependencies += 1
        if self.factor is not None:
            self.factor_method = "retained_parity_dependency"
            self.factor_dependency_size = combination.bit_count()
            self.factor_witness = {
                "relation_indices_zero_based": [
                    index
                    for index in range(len(self.relation_factors))
                    if (combination >> index) & 1
                ],
                "root_mod_N": root,
                "gcd_root_minus_one_N": minus,
                "gcd_root_plus_one_N": plus,
            }


def public_basis(records: list[dict[str, object]]) -> tuple[list[int], list[list[int]]]:
    """Recover the exact finest gcd/perfect-power basis from endpoint factors.

    Factorization is used only to accelerate discovery. Grouping by primitive
    endpoint-valuation signature gives the same blocks available from exact
    gcd splitting and exact perfect-power extraction.
    """
    signatures: dict[int, list[tuple[int, int]]] = {}
    for relation_index, record in enumerate(records):
        for side, factors in enumerate((record["c_factors"], record["w_factors"])):
            endpoint_index = 2 * relation_index + side
            for p, exponent in factors.items():
                signatures.setdefault(p, []).append((endpoint_index, exponent))

    groups: dict[tuple[tuple[int, int], ...], list[tuple[int, int]]] = {}
    for p, signature in signatures.items():
        content = 0
        for _, exponent in signature:
            content = math.gcd(content, exponent)
        primitive = tuple((index, exponent // content) for index, exponent in signature)
        groups.setdefault(primitive, []).append((p, content))

    basis_records = []
    for primitive, prime_contents in groups.items():
        common_content = 0
        for _, content in prime_contents:
            common_content = math.gcd(common_content, content)
        block = 1
        for p, content in prime_contents:
            block *= p ** (content // common_content)
        endpoint_exponents = {
            endpoint_index: common_content * exponent
            for endpoint_index, exponent in primitive
        }
        basis_records.append((block, endpoint_exponents))
    basis_records.sort(key=lambda item: item[0])

    supports: list[list[int]] = []
    for relation_index in range(len(records)):
        left = 2 * relation_index
        right = left + 1
        support = [
            block
            for block, endpoint_exponents in basis_records
            if endpoint_exponents.get(left, 0) + endpoint_exponents.get(right, 0) > 0
        ]
        supports.append(support)
    return [block for block, _ in basis_records], supports


def run_overpowered_c2t(modulus: int) -> dict[str, object]:
    n = modulus.bit_length()
    bound = n * n
    for t in range(2, bound + 1):
        d = math.gcd(t, modulus)
        if 1 < d < modulus:
            return {"status": "trial_factor", "factor": d, "n": n, "B": bound}

    decoder = PrimeDecoder(modulus)
    records: list[dict[str, object]] = []
    seen_residues: set[int] = set()
    factor_cache: dict[int, dict[int, int]] = {1: {}}

    def endpoint_factors(value: int) -> dict[int, int]:
        cached = factor_cache.get(value)
        if cached is None:
            cached = factor_u64(value)
            factor_cache[value] = cached
        return cached

    def retain(c: int, provenance: dict[str, object]) -> None:
        if c in seen_residues:
            return
        seen_residues.add(c)
        w = pow(c, -1, modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            direct = math.gcd(difference, modulus)
            if 1 < direct < modulus:
                decoder.factor = direct
                decoder.factor_method = f"direct_endpoint_{sign}"
                decoder.factor_dependency_size = 0
                decoder.factor_witness = {
                    "provenance": provenance,
                    "c": c,
                    "w": w,
                    "gcd_value": direct,
                }
                return
        product = c * w
        c_factors = endpoint_factors(c)
        w_factors = endpoint_factors(w)
        relation_factors = dict(c_factors)
        for p, exponent in w_factors.items():
            relation_factors[p] = relation_factors.get(p, 0) + exponent
        before = decoder.dependencies
        decoder.add(relation_factors)
        records.append(
            {
                "c": c,
                "w": w,
                "P": product,
                "c_factors": c_factors,
                "w_factors": w_factors,
                "relation_factors": relation_factors,
                "provenance": provenance,
                "expanded": False,
                "nonzero": any(e & 1 for e in relation_factors.values()),
                "dependent_when_added": decoder.dependencies > before,
            }
        )

    for seed in range(2, n + 1):
        retain(seed, {"kind": "initial_seed", "seed": seed})
        if decoder.factor is not None:
            return {
                "status": "initial_factor",
                "factor": decoder.factor,
                "factor_method": decoder.factor_method,
                "factor_dependency_size": decoder.factor_dependency_size,
                "factor_witness": decoder.factor_witness,
                "n": n,
                "B": bound,
            }

    round_records = []
    for round_index in range(1, n + 1):
        _, supports = public_basis(records)
        active: list[tuple[int, dict[str, object]]] = []
        for relation_index, record in enumerate(records):
            if not record["expanded"] and record["nonzero"]:
                record["expanded"] = True
                active.append((relation_index, record))
                if len(active) == n:
                    break
        if not active:
            return {
                "status": "queue_fixed_point",
                "n": n,
                "B": bound,
                "relations": len(records),
                "dependencies": decoder.dependencies,
                "global_dependencies": decoder.global_dependencies,
                "rounds": round_records,
            }
        start_relations = len(records)
        start_dependencies = decoder.dependencies
        active_pairs = []
        for relation_index, record in active:
            support = supports[relation_index]
            if len(support) == 1:
                u, v = support[0], 1
            else:
                u, v = support[:2]
            active_pairs.append([u, v])
            for exponent in range(bound + 1):
                candidates = (
                    ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                    ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
                )
                for orientation, c in candidates:
                    retain(
                        c,
                        {
                            "kind": "feedback_trajectory",
                            "round": round_index,
                            "active_relation_index_zero_based": relation_index,
                            "u": u,
                            "v": v,
                            "exponent": exponent,
                            "orientation": orientation,
                        },
                    )
                    if decoder.factor is not None:
                        return {
                            "status": "feedback_factor",
                            "factor": decoder.factor,
                            "factor_method": decoder.factor_method,
                            "factor_dependency_size": decoder.factor_dependency_size,
                            "factor_witness": decoder.factor_witness,
                            "n": n,
                            "B": bound,
                            "round": round_index,
                            "relations": len(records),
                            "dependencies": decoder.dependencies,
                            "active_pairs": active_pairs,
                            "rounds": round_records,
                        }
        round_records.append(
            {
                "round": round_index,
                "active": len(active),
                "new_relations": len(records) - start_relations,
                "new_dependencies": decoder.dependencies - start_dependencies,
                "active_pairs": active_pairs,
            }
        )
    return {
        "status": "round_cap_null",
        "n": n,
        "B": bound,
        "relations": len(records),
        "dependencies": decoder.dependencies,
        "global_dependencies": decoder.global_dependencies,
        "rounds": round_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-min", type=int, required=True)
    parser.add_argument("--prime-max", type=int, required=True)
    parser.add_argument("--pair-cap", type=int, required=True)
    parser.add_argument("--pairs-per-p", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.monotonic()
    factor_primes = primes_through(max(args.prime_max, 1000))
    candidates = [
        p for p in factor_primes if args.prime_min <= p <= args.prime_max and p > 3
    ]
    tested = 0
    stable_tested = 0
    trace = []
    counterexample = None

    def write_checkpoint(status: str) -> None:
        checkpoint = {
            "experiment": "F98_multiseed_presentation_closure_kill",
            "role": "factor-assisted discovery only",
            "status": status,
            "bounds": vars(args) | {"output": str(args.output)},
            "pairs_tested": tested,
            "stable_pairs_tested": stable_tested,
            "counterexample": counterexample,
            "trace": trace,
            "elapsed_seconds": time.monotonic() - started,
        }
        temporary = args.output.with_suffix(args.output.suffix + ".tmp")
        temporary.write_text(json.dumps(checkpoint, indent=2, sort_keys=True) + "\n")
        temporary.replace(args.output)

    for i, p in enumerate(candidates):
        q_indices = [len(candidates) - 1 - i - offset for offset in range(args.pairs_per_p)]
        for q_index in q_indices:
            if q_index <= i:
                continue
            q = candidates[q_index]
            if tested >= args.pair_cap:
                break
            modulus = p * q
            n = modulus.bit_length()
            if p <= n * n:
                continue
            tested += 1
            if not stable(p, q):
                continue
            stable_tested += 1
            result = run_overpowered_c2t(modulus)
            trace.append({"p": p, "q": q, "N": modulus, "result": result})
            if result["status"] in {"round_cap_null", "queue_fixed_point"}:
                counterexample = trace[-1]
                write_checkpoint("counterexample")
                break
            write_checkpoint("running_checkpoint")
        if counterexample is not None or tested >= args.pair_cap:
            break
    write_checkpoint("counterexample" if counterexample is not None else "cap_complete")
    output = json.loads(args.output.read_text())
    print(f"pairs_tested={tested}")
    print(f"stable_pairs_tested={stable_tested}")
    print(f"counterexample={counterexample}")
    print(f"elapsed_seconds={output['elapsed_seconds']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
