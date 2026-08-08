#!/usr/bin/env python3
"""Bounded exhaustive audit of the F105 parity-core equivalence."""

from __future__ import annotations

import itertools
import json
import math
from functools import cache


MASK_BITS = 3
VALUES = tuple(range(2, 13))
ONE_STEP_VALUES = tuple(range(2, 17))


@cache
def factorization(n: int) -> tuple[tuple[int, int], ...]:
    factors: list[tuple[int, int]] = []
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent:
            factors.append((p, exponent))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def omega(n: int) -> int:
    return sum(exponent for _, exponent in factorization(n))


def parity_rows(records: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    rows: dict[int, int] = {}
    for value, mask in records:
        for prime, exponent in factorization(value):
            rows.setdefault(prime, 0)
            if exponent & 1:
                rows[prime] ^= mask
    return tuple(rows[prime] for prime in sorted(rows))


def public_rows(state: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    return tuple(
        mask
        for value, mask in state
        if math.isqrt(value) ** 2 != value
    )


def refinements(
    state: tuple[tuple[int, int], ...],
) -> tuple[tuple[tuple[int, int], ...], ...]:
    next_states: set[tuple[tuple[int, int], ...]] = set()
    old_potential = sum(omega(value) for value, _ in state)
    for left in range(len(state)):
        x, s = state[left]
        for right in range(left + 1, len(state)):
            y, t = state[right]
            divisor = math.gcd(x, y)
            if divisor == 1:
                continue
            records = [
                record
                for index, record in enumerate(state)
                if index not in (left, right)
            ]
            if s ^ t:
                records.append((divisor, s ^ t))
            if x // divisor > 1:
                records.append((x // divisor, s))
            if y // divisor > 1:
                records.append((y // divisor, t))
            next_state = tuple(sorted(records))
            assert sum(omega(value) for value, _ in next_state) < old_potential
            next_states.add(next_state)
    return tuple(sorted(next_states))


@cache
def terminal_states(
    state: tuple[tuple[int, int], ...],
) -> frozenset[tuple[tuple[int, int], ...]]:
    next_states = refinements(state)
    if not next_states:
        return frozenset((state,))
    terminals: set[tuple[tuple[int, int], ...]] = set()
    for next_state in next_states:
        terminals.update(terminal_states(next_state))
    return frozenset(terminals)


def kernel(rows: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        vector
        for vector in range(1 << MASK_BITS)
        if all((row & vector).bit_count() % 2 == 0 for row in rows)
    )


@cache
def peel_endpoints(rows: tuple[int, ...], active: int) -> frozenset[int]:
    forced = {
        restricted
        for row in rows
        if (restricted := row & active).bit_count() == 1
    }
    if not forced:
        return frozenset((active,))
    endpoints: set[int] = set()
    for column in forced:
        endpoints.update(peel_endpoints(rows, active ^ column))
    return frozenset(endpoints)


def components(rows: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    adjacency = [set() for _ in range(MASK_BITS)]
    for row in rows:
        support = [column for column in range(MASK_BITS) if row >> column & 1]
        for column in support:
            adjacency[column].update(support)
    unseen = set(range(MASK_BITS))
    result: list[tuple[int, ...]] = []
    while unseen:
        stack = [min(unseen)]
        component: set[int] = set()
        while stack:
            column = stack.pop()
            if column in component:
                continue
            component.add(column)
            stack.extend(adjacency[column] - component)
        unseen -= component
        result.append(tuple(sorted(component)))
    return tuple(result)


one_step_checks = 0
unequal_positive_valuation_checks = 0
for x, y in itertools.product(ONE_STEP_VALUES, repeat=2):
    divisor = math.gcd(x, y)
    for s, t in itertools.product(range(1 << MASK_BITS), repeat=2):
        before = parity_rows(((x, s), (y, t)))
        after_records: list[tuple[int, int]] = []
        if divisor == 1:
            if s:
                after_records.append((x, s))
            if t:
                after_records.append((y, t))
        else:
            if s ^ t:
                after_records.append((divisor, s ^ t))
            if x // divisor > 1 and s:
                after_records.append((x // divisor, s))
            if y // divisor > 1 and t:
                after_records.append((y // divisor, t))
        after_by_prime = dict(
            zip(
                sorted({p for value, _ in ((x, s), (y, t)) for p, _ in factorization(value)}),
                before,
                strict=True,
            )
        )
        actual: dict[int, int] = {prime: 0 for prime in after_by_prime}
        for value, mask in after_records:
            for prime, exponent in factorization(value):
                if exponent & 1:
                    actual[prime] ^= mask
        assert actual == after_by_prime
        one_step_checks += 1
        for prime in after_by_prime:
            alpha = dict(factorization(x)).get(prime, 0)
            beta = dict(factorization(y)).get(prime, 0)
            if alpha and beta and alpha != beta:
                unequal_positive_valuation_checks += 1


record_types = tuple(
    (value, mask)
    for value in VALUES
    for mask in range(1 << MASK_BITS)
)
batch_checks = 0
terminal_schedule_checks = 0
max_terminal_states = 0
for size in range(4):
    for raw_records in itertools.combinations_with_replacement(record_types, size):
        state = tuple(sorted(record for record in raw_records if record[1]))
        hidden_rows = parity_rows(raw_records)
        hidden_nonzero = frozenset(row for row in hidden_rows if row)
        hidden_kernel = kernel(hidden_rows)
        hidden_peels = peel_endpoints(tuple(sorted(hidden_rows)), (1 << MASK_BITS) - 1)
        assert len(hidden_peels) == 1
        hidden_components = components(hidden_rows)
        terminals = terminal_states(state)
        max_terminal_states = max(max_terminal_states, len(terminals))
        for terminal in terminals:
            assert all(
                math.gcd(terminal[left][0], terminal[right][0]) == 1
                for left in range(len(terminal))
                for right in range(left + 1, len(terminal))
            )
            rows = public_rows(terminal)
            assert frozenset(rows) == hidden_nonzero
            assert kernel(rows) == hidden_kernel
            public_peels = peel_endpoints(tuple(sorted(rows)), (1 << MASK_BITS) - 1)
            assert len(public_peels) == 1
            assert public_peels == hidden_peels
            assert components(rows) == hidden_components
            terminal_schedule_checks += 1
        batch_checks += 1


literal_zero_row_witness = ((4, 1),)
literal_zero_hidden_rows = parity_rows(literal_zero_row_witness)
literal_zero_public_rows = public_rows(literal_zero_row_witness)
assert literal_zero_hidden_rows == (0,)
assert literal_zero_public_rows == ()

nonprogress_coprime_pair = ((2, 1), (3, 2))
assert math.gcd(nonprogress_coprime_pair[0][0], nonprogress_coprime_pair[1][0]) == 1

print(
    json.dumps(
        {
            "status": "PASS",
            "mask_bits": MASK_BITS,
            "batch_values": [VALUES[0], VALUES[-1]],
            "maximum_batch_size": 3,
            "one_step_values": [ONE_STEP_VALUES[0], ONE_STEP_VALUES[-1]],
            "one_step_checks": one_step_checks,
            "unequal_positive_valuation_checks": unequal_positive_valuation_checks,
            "batch_checks": batch_checks,
            "terminal_schedule_checks": terminal_schedule_checks,
            "maximum_distinct_terminal_states_for_one_batch": max_terminal_states,
            "properties": [
                "per-prime parity invariant, including zero masks",
                "strict potential decrease for every eligible refinement",
                "all refinement schedules terminate pairwise-coprime",
                "distinct nonzero public rows equal distinct nonzero hidden rows",
                "kernel equality with zero and duplicate rows retained on hidden side",
                "all peeling orders have one endpoint and both presentations agree",
                "column-incidence components agree, including isolated columns",
            ],
            "wording_boundaries": {
                "zero_row_witness": {
                    "input": literal_zero_row_witness,
                    "hidden_rows_if_not_omitted": literal_zero_hidden_rows,
                    "public_rows": literal_zero_public_rows,
                },
                "coprime_selection_nonprogress_witness": nonprogress_coprime_pair,
            },
        },
        indent=2,
        sort_keys=True,
    )
)
