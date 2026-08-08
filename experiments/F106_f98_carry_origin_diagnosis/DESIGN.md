# F106 — carry-origin diagnosis of the F98 circuit

## Question

Does the 166-column F98 circuit obtain most of its rank and connectivity from
exact consecutive canonical-carry overlaps, or from shared prime factors that
are not explained by those local carry identities?

## Exact carry identity

For one trajectory `c_e = [r^e v]_N`, put `w_e = c_e^{-1}` in the canonical
integer range. Then

```text
c_(e+1) = r c_e - a_e N,
r w_(e+1) = w_e + b_e N,
```

with public carries `0 <= a_e,b_e < r`. If `a_e = 0`, consecutive relations
share the exact endpoint `c_e`. If `b_e = 0`, they share the exact endpoint
`w_(e+1)`. If both carries vanish, the two exact relation values are equal
and first-occurrence deduplication removes one.

## Method

Use the pinned F98 public certificate and the pinned F100 factor-assisted
factorizations. Reconstruct every odd-prime row of the 166-column circuit.
Classify a repeated prime row as carry-explained only when consecutive
records in the same oriented trajectory have a zero carry and the prime
actually divides the forced shared endpoint.

Measure row counts, binary ranks, and column-graph components for:

- rows with at least one carry-explained adjacency;
- rows whose occurrence graph is connected by such adjacencies;
- rows with no carry-explained adjacency;
- rows confined to one oriented trajectory;
- rows spanning trajectories; and
- small versus larger primes at the public bound `n^2`.

## Falsifiers

The carry explanation is strong only if carry rows alone retain rank 165 and
connect all 166 columns. It is weak if non-carry or cross-trajectory rows are
needed for most of the rank or for global connectivity.

## Scope

This is a factor-assisted diagnosis of one fixed circuit. It cannot prove a
frequency law or an all-input algorithm.
