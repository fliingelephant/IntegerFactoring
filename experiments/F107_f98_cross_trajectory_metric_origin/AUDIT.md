# F107 hostile audit

## Verdict: FAIL as written

The stored computation reproduces exactly under its actual rules. The stated
trajectory semantics and the origin claim do not.

The independent verifier completed 7,698 checks with no verifier failure. It
matched `OUTPUT.json`, all comparable R01 fields, both run logs, both pinned
input hashes, and all ten hashes in the candidate manifest. It imported and
executed neither candidate source file.

The candidate fails for four reasons:

1. It counts the initial seed as an oriented feedback trajectory.
2. Its carry rule requires one endpoint type for a full interval. It misses
   valid prime-specific chains that switch between `c` and `w`.
3. Its selected-selected carry scope is not an origin-complete scope. Raw
   adjacent carry exposure already spans the full fixed circuit.
4. “Metric” is only a negative residual label. The data do not establish a
   metric mechanism, randomness, rarity, causation, or factor correlation.

The title “mostly a metric integer effect” and the phrase “metric presentation
effect” therefore overstate the result.

## What reproduces

Under the candidate's actual nine source buckets, including `seed:11`, every
stored R02 number is correct:

| Row class | Rows | Rank | Components |
|---|---:|---:|---|
| All parity-prime rows | 230 | 165 | `[166]` |
| More than one source bucket | 175 | 163 | `[166]` |
| Any non-base source pair | 175 | 163 | `[166]` |
| No base-inherited source pair | 170 | 158 | `[164, 1, 1]` |
| Non-base and no uniform-endpoint carry touch | 151 | 143 | 19; largest 148 |
| No base pair and no uniform-endpoint carry touch | 150 | 142 | 21; largest 146 |

The source-bucket pair counts are 15 base-inherited and 724 non-base. The
base-touched primes are `2, 3, 5, 11, 17`. There are 84 non-base primes above
784. The maximum is 2,814,499.

These are source-bucket statistics. They are not strict feedback-trajectory
statistics.

## Strict feedback trajectories

The certificate contains eight feedback-oriented trajectories and one initial
seed. Prime 1451 occurs only at columns 0 and 148. Column 0 is the seed. Column
148 is in one feedback trajectory. This row does not span feedback
trajectories.

Prime 11 shows the second effect. The candidate's only base pair for 11 is the
seed `11` paired with active relation 9, whose public base is also 11. After
the seed is removed, prime 11 has no base-inherited feedback-trajectory pair.

The strict reconstruction is:

| Row class | Rows | Rank | Components |
|---|---:|---:|---|
| At least two feedback-oriented trajectories | 174 | 163 | `[166]` |
| Any base-inherited trajectory pair | 4 | 4 | 39; largest 128 |
| Any non-base trajectory pair | 174 | 163 | `[166]` |
| Non-base pairs and no base pair | 170 | 159 | `[164, 1, 1]` |
| Non-base and no mixed-endpoint selected carry touch | 149 | 141 | 21; largest 146 |
| No base pair and no mixed-endpoint selected carry touch | 149 | 141 | 21; largest 146 |

The strict pair counts are 14 base-inherited and 707 non-base. The strict base
primes are `2, 3, 5, 17`. There are 83 strict non-base primes above 784.

All distinct public base values are pairwise coprime. Thus, on this fixed
input, the candidate's exact-shared-base test gives the same result as testing
whether distinct base values share a prime factor. This fact does not make the
residual class a positive explanation.

The component values above use complete prime-row supports. A graph made only
from strict non-base occurrence edges has components `[165, 1]`; the isolated
column is the seed. Therefore “connects all 166 columns” is valid for the
selected row-support hypergraph, not for the strict cross-trajectory edge
graph.

## Missed selected carry chains

The candidate recognizes only an interval whose `c` carries are all zero or
whose `w` carries are all zero. A prime-specific exact path can switch endpoint
type at an intermediate relation.

| Prime | Columns | Exponents | Exact zero-carry sequence |
|---:|---:|---:|---|
| 3 | 120 to 122 | 686 to 688 | `c, w` |
| 3 | 155 to 158 | 657 to 663 | `w, w, c, c, c, w` |
| 17 | 73 to 75 | 693 to 696 | `c, w, w` |

For prime 17, the exact shared values are 96,703,888, 83,254,746, and
41,627,373. Each is divisible by 17. The candidate rejects the path only
because the endpoint type changes.

| Carry-touched class | Rows | Rank | Components | Prime-labelled edges |
|---|---:|---:|---|---:|
| Uniform endpoint | 74 | 71 | `[163, 2, 1]` | 109 |
| Prime-specific mixed endpoint | 75 | 72 | `[163, 2, 1]` | 112 |

Under the candidate's nine-bucket semantics, mixed-endpoint exclusion leaves
150 non-base rows of rank 142, with largest component 146. Under strict
feedback semantics, it leaves 149 rows of rank 141, with largest component
146.

## Raw-batch origin test

The selected-pair test asks whether two selected odd-support columns have a
carry path. It does not ask whether a circuit prime is exposed by an exact
carry anywhere in the generated F98 batch.

The verifier reconstructed every exponent from 0 through 784. It scanned raw
adjacent states. It excluded a step when both carries were zero, because its
two endpoint products are equal and first-occurrence deduplication removes the
second relation.

| Raw scope | Carry-exposed rows | Rank | Components | Unexposed rows | Unexposed rank |
|---|---:|---:|---|---:|---:|
| Eight trajectories represented in the certificate | 194 | 165 | `[166]` | 36 | 36 |
| All 54 round-one oriented trajectories | 203 | 165 | `[166]` | 27 | 27 |

After full raw exposure is excluded, only 25 strict non-base cross rows remain.
They have rank 25 and 139 components; the largest component has size 4.

Raw exposure does not prove that a particular cross-trajectory pair came from
a carry. It does prove that the selected-selected exclusion cannot support an
origin-level contrast in which carry is small and “metric” is dominant. Under
the broader origin scope, carry-touched rows already span and connect the full
fixed circuit.

## Meaning of “metric”

The candidate's operational rule is exact:

> A trajectory-key pair is residual when no exact public base integer shared
> by the two keys is divisible by the row prime.

Nothing in this rule defines a metric space or a probability model. The fixed
certificate was selected because it is the first useful dependency. It is not
an unconditioned sample. The audit found no statistic about randomness,
rarity, independence, or correlation with the nontrivial factors of `N`.
Every row prime is coprime to `N`; the factor-assisted input factors the
relation products, not `N`.

The candidate correctly says that “metric” does not mean random and gives no
asymptotic law. Those disclaimers pass. The positive phrases “metric integer
effect” and “metric presentation effect” do not pass. Absence of one base
mechanism is not evidence for a distinct causal mechanism.

Rank is also not an additive origin allocation. For the strict 149-row set
with no base pair and no mixed selected carry touch:

```text
neutral subset rank                 141
81-row complement rank              78
full rank                           165
span intersection dimension          54
neutral marginal over complement     87
complement marginal over neutral     24
```

Thus, “rank 141” means only that the complete supports of those selected rows
span a 141-dimensional subspace.

## Required correction

Use one of these provenance scopes:

- Keep all stored numbers and rename “trajectory” to “source bucket.” State
  that the ninth bucket is the initial seed.
- Use strict feedback trajectories and replace the affected counts and ranks
  with the strict values above.

Also make these changes:

- Call the candidate carry class “uniform-endpoint selected-pair carry
  touched,” or use the prime-specific mixed-endpoint rule.
- State that selected-pair carry is not an origin-complete exclusion. Include
  the raw-batch result if the claim concerns origin.
- Replace “metric” with “non-base-inherited integer overlap.” If “metric” is
  retained, define it as an audit-local residual label only.
- Report row-subset ranks and row-support components as exact linear-algebra
  facts. Do not call them additive causal shares.

The following narrow statement passes:

> In the fixed F98 certificate at `N = 202537109`, 174 parity-prime rows occur
> in at least two of the eight feedback-oriented trajectories. Every such row
> has at least one trajectory pair with no exact shared public base divisible
> by its prime. The 170 rows with no base-inherited trajectory pair have rank
> 159. After excluding prime rows touched by a prime-specific mixed-endpoint
> carry path between selected odd-support columns, 149 rows remain and have
> rank 141. Their complete row-support graph has largest component 146.

This statement is factor-assisted and finite-circuit only. It does not assign
origin, probability, asymptotic frequency, factor correlation, or algorithmic
power.

## Independent reconstruction

The verifier checked every factor product and factor primality. It checked
`P = c*w`, `c*w = 1 mod N`, every modular trajectory formula, every inverse,
all parity supports, both pinned hashes, and all candidate artifact hashes.
It then rebuilt all 230 rows.

The implementation differs materially from the candidate:

- Rows are sets. GF(2) elimination uses symmetric difference and lowest
  pivots.
- Components use explicit adjacency sets and graph traversal.
- Carry paths use every canonical trajectory step, not scaled selected
  endpoints as the primary test.
- The raw scan reconstructs all 54 round-one oriented trajectories.

The full per-prime support, pair classification, carry edges, and raw exposure
witnesses are in `AUDIT_OUTPUT.json`. The canonical SHA-256 of the 230-row
classification is:

```text
efcf562c11bccf1058e261414d5e311adb7effbea887400a0fc796ab1742833d
```

## Preserved failed audit attempts

No verifier attempt failed. The named timeout runner preserves any future
timeout, invalid output, or verifier failure as a timestamped
`AUDIT_FAILED_*` JSON and log pair. It promotes only a successful verifier run
to `AUDIT_OUTPUT.json` and `AUDIT_RUN.log`.
