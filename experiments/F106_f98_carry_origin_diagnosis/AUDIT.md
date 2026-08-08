# F106 hostile audit

## Verdict: FAIL as written

The candidate computation is reproducible under its narrow classification.
The broader carry-origin interpretation is not.

The independent verifier completed 32,503 checks with no verifier failure. It
matched every stored R02 statistic, every comparable R01 statistic, both
pinned input hashes, both run logs, and all ten hashes in the candidate
manifest. It did not import or run the candidate code.

The candidate fails for four exact reasons:

1. Its carry-chain rule misses a valid prime-specific chain that switches
   from a `c` overlap to a `w` overlap.
2. Its count of 175 rows that span oriented trajectories treats the initial
   seed as an oriented trajectory.
3. Its count of 230 “odd-prime rows” includes the row for prime 2.
4. Its rank and component interpretation mixes exact carry edges with all
   unexplained occurrences in each carry-touched prime row.

The valid result is narrower: 74 parity-prime rows, including prime 2, have
at least one **uniform-endpoint chain between two selected odd-support
columns**. Their complete row supports have rank 71 and components
`[163, 2, 1]`. This is a carry-touched row upper bound. It is not a complete
classification of exact local carry paths or of carry exposure in the F98
round-one batch.

## Independent reconstruction

The verifier rebuilt the 166-column certificate from the two pinned JSON
inputs. It checked each exact product, modular inverse, provenance formula,
factor product, factor primality, endpoint valuation, and parity support. It
then rebuilt all 230 prime-parity rows.

The implementation is materially different from the candidate:

- GF(2) elimination uses sets, symmetric difference, and lowest pivots.
- Component calculation builds explicit adjacency sets and uses BFS.
- Carry chains use every step of the canonical trajectory for exponents
  `0..784`. They do not use scaled endpoint equality as the primary test.
- Provenance is checked against the modular power formula and the active pair.

The complete per-prime classification is in `AUDIT_OUTPUT.json`. Its canonical
SHA-256 is:

```text
5f41883d2796f8d4932db639c0f126aabdbf26c781c11a1dcf2b4c8f365e47ee
```

SageMath 10.9 independently checked the key dense GF(2) ranks:

```text
all=165
narrow_carry=71
narrow_no_carry=145
mixed_carry=72
odd_only=165
pure_edges=50
```

## What reproduces exactly

Under the candidate rule, the independent results are:

| Class | Rows | Rank | Components |
|---|---:|---:|---|
| All parity-prime rows | 230 | 165 | `[166]` |
| Uniform-chain touched | 74 | 71 | `[163, 2, 1]` |
| No uniform-chain edge | 156 | 145 | 19; largest 148 |
| Carry-connected rows | 50 | 47 | 119; largest 5 |
| Candidate cross buckets | 175 | 163 | `[166]` |
| One candidate bucket | 55 | 52 | 114; largest 7 |
| Prime at most 784 | 95 | 95 | `[166]` |
| Prime above 784 | 135 | 132 | 29; largest 51 |

The stepwise reconstruction also matches all candidate chain counts:

```text
consecutive selected pairs       31
c-zero only                      16
w-zero only                      14
neither                           1
both zero                         0
uniform-endpoint selected pairs  51
c chains                         28
w chains                         23
```

The stepwise and scaled-endpoint tests agree on all selected pairs. Thus the
candidate code correctly implements its own uniform-endpoint definition.

## Falsifier 1: mixed-endpoint carry path

Prime 17 gives a counterexample to the claimed carry-chain coverage. Consider
the `u_power_times_v` trajectory for active relation 12, with multiplier 2.
The parity row for 17 contains selected columns 73 and 75 at exponents 693
and 696. The exact consecutive path is:

| Step | Zero carry | Forced shared value |
|---|---|---:|
| 693 to 694 | `c` | 96,703,888 |
| 694 to 695 | `w` | 83,254,746 |
| 695 to 696 | `w` | 41,627,373 |

Prime 17 divides all three values. At selected column 74, exponent 694, it
divides both endpoints. Its total valuation in that relation is two. The
prime is therefore absent from that parity-row column, but it still bridges
the two odd-parity occurrences through exact consecutive carry overlaps.

The candidate rejects this path because the full interval has neither all
`c` carries zero nor all `w` carries zero. A prime-specific transitive closure
also finds two new edges for prime 3. The corrected selected-column results
are:

| Class | Rows | Rank | Largest component |
|---|---:|---:|---:|
| Mixed-endpoint carry touched | 75 | 72 | 163 |
| No mixed-endpoint carry path | 155 | 144 | 146 |

This does not make carry rows sufficient. It does falsify the claim that the
51 uniform intervals cover all chains of exact consecutive carry overlaps.

## Falsifier 2: provenance classification

Prime 1451 occurs at columns 0 and 148. Column 0 is the initial seed. Column
148 is in exactly one feedback-oriented trajectory:

```text
(round 1, active relation 25, u_times_v_power)
```

The candidate counts the seed as a second trajectory. Therefore 175 is the
count of provenance buckets, not the count of rows spanning multiple oriented
trajectories.

The strict results are:

| Scope | Rows | Rank | Components |
|---|---:|---:|---|
| Multiple feedback-oriented trajectories, all parity primes | 174 | 163 | `[166]` |
| Same, odd primes only | 173 | 162 | `[166]` |
| Same and prime above 784 | 83 | 83 | 78 components; largest 25 |

The qualitative cross-trajectory signal remains strong. The stated counts of
175 and 84 do not have the stated provenance meaning.

## Falsifier 3: “odd-prime” rows

The 230 rows include prime 2. Its row has degree 80. It is carry touched and
spans eight candidate provenance buckets.

There are 229 literal odd-prime rows. They still have rank 165 and connect all
166 columns. Under the candidate carry rule, the odd-prime-only carry subset
has 73 rows, rank 70, and components `[162, 2, 1, 1]`. The small odd-prime
subset has 94 rows and rank 94.

The main full-rank conclusion survives removal of prime 2. The row counts and
the phrase “odd-prime rows” do not.

## Falsifier 4: carry-edge connectivity and rank attribution

The candidate component list `[163, 2, 1]` uses the complete supports of all
74 carry-touched rows. Most support incidences are not carry edges:

```text
row support occurrences                     576
occurrences incident to a carry edge         212
within-row column-pair slots                9464
prime-labelled exact carry edges              109
carry-touched but not carry-connected rows     24
```

All 24 non-connected carry-touched rows are cross-trajectory rows. Their
unexplained support occurrences create most of the apparent global
connectivity.

The graph made only from the 51 distinct exact carry pairs has rank 50 and
116 components. Its three largest components have sizes 5, 5, and 5. Thus
`[163, 2, 1]` is a row-discovery upper bound. It is not the connectivity of
the exact carry links themselves.

The rank numbers are also not additive. The uniform carry-touched span and
the no-carry span intersect in dimension 51:

```text
carry-touched span rank               71
no-carry span rank                   145
intersection dimension               51
carry marginal over no-carry span     20
no-carry marginal over carry span     94
```

The sentence that carry identities “supply 71 of 165 row-rank units” is not
a canonical rank attribution. The exact numerical statement is that the
complete supports of carry-touched rows span a 71-dimensional subspace.

## Raw-batch scope test

The candidate requires both odd-support endpoints to be in the 166-column
certificate. That is not a carry-origin test for the full F98 batch.

The audit scanned every adjacent exponent in the round-one trajectories. It
excluded two-zero pairs because first-occurrence deduplication removes the
second equal relation value. It then used the same factor-assisted row rule:
if any distinct local pair exposes prime `p`, include the complete circuit
row for `p`.

| Raw scope | Exposed rows | Rank | Components |
|---|---:|---:|---|
| Eight oriented trajectories represented in the certificate | 194 | 165 | `[166]` |
| All 54 round-one oriented trajectories | 203 | 165 | `[166]` |

This is not a factor-free algorithmic result. It uses the F100 prime labels.
It shows only that the candidate conclusion changes when “origin” means
carry exposure anywhere in the generated F98 batch. Under that meaning,
carry-exposed rows already span and connect the full fixed circuit.

## Exact valid scope

The following statement passes:

> For the fixed F98 certificate at `N = 202537109`, classify a parity-prime
> row, including prime 2, as touched when two selected odd-support columns in
> one oriented trajectory have an interval with all `c` carries zero or all
> `w` carries zero. Count the initial seed as its own provenance bucket. Use
> the complete support of every touched row for rank and components. Under
> this definition, 74 rows have rank 71 and components `[163, 2, 1]`; the 156
> untouched rows have rank 145 and 19 components.

This fixed-input statement does not cover mixed-endpoint paths, strict
feedback-oriented provenance, pure carry-edge connectivity, raw-batch carry
exposure, frequency, asymptotics, or an all-input factoring algorithm.

## Preserved failed audit attempts

Two audit implementation attempts are preserved:

- `AUDIT_FAILED_20260808T014849Z_SCOPE_BUG.*` labelled an eight-trajectory
  scan as the full round-one scan.
- `AUDIT_FAILED_20260808T015050Z_DUPLICATE_FILTER.*` applied the two-zero
  duplicate filter to the 54-trajectory scan but not to its eight-trajectory
  comparison.

Neither failed attempt is evidence against the candidate. The authoritative
runner now applies the declared scope and duplicate rule consistently.
