# F108 final narrow re-audit

## Verdict: PASS

The corrected `DESIGN.md` and `RESULT.md` match the independent hostile-audit
evidence. No further mathematical, numerical, or scope correction is needed.

## Corrected artifact pins

```text
db3531a92180c051fac08ba10bdb79ebaf2d2756cac560effa646b6ebc4a62dc  DESIGN.md
5c912207a12fb3d561423d5d5e6cd71c4b685a7d6a9f572dc868d29ef8f47dbc  RESULT.md
```

The executable and fixed output are unchanged:

```text
0be579050066d9bc79e4bf5192a606989958fef2531420fb83984de925e1e8de  analyze_public_carry_coverage.py
2427d36129ecac0de8e735d972f641dbdb2c22d885c28d1502ba0ff9411340c5  OUTPUT.json
```

## Exact set equality: PASS

The corrected claim is the exact equality of distinct nonzero mask sets, not
only equality of their spans:

\[
\{m_j:S_E(q_j)\text{ is nonsquare}\}
=
\{r_p:p\mid E,\ r_p\ne0\}.
\]

This is the theorem proved in `AUDIT.md`. Gcd saturation includes the complete
`p`-power of a terminal block exactly when `p|E`. A supported part is
nonsquare exactly when an exposed prime has odd valuation. That prime's row
is the block mask. Both inclusions hold mask by mask.

The fixed replay agrees: 194 exposed prime rows merge to 191 distinct masks
for the eight raw trajectories, and 203 merge to 200 for all 54 trajectories.
The public construction returns exactly those 191 and 200 mask sets.

## Raw and circuit-local scope: PASS

The corrected text now says that the 1,840 and 15,935 exposure integers are
raw-batch exposures. It also says that the adjacent raw values need not both
be selected circuit columns. This matches the audit.

The circuit-local paragraph is exact:

| Scope | Selected adjacent pairs | Exposure integers | Rank |
|---|---:|---:|---:|
| Eight represented trajectories | 34 | 34 | 54 |
| All 54 trajectories | 82 | 82 | 54 |

After two-zero duplicates are excluded, each counted local pair has exactly
one zero carry. Thus “34/82 exposure events” and “34/82 exposure integers”
are equivalent for this fixed replay.

The corrected conclusion is also exact: raw exposure spans the rank-165
circuit, while selected-to-selected local carry does not.

## F99 second carry: PASS

For the F99 family,

\[
w_e=N-\frac{N-1}{2^e}.
\]

Therefore

\[
2w_{e+1}-w_e=N.
\]

The second carry is one. The first carry is zero because
`c_(e+1)=2*c_e`. Hence every nonduplicate transition exposes only the
power-of-two endpoint. The exposed row space has rank at most one, while the
private `q_e` rows give full rank `T`. The corrected wording states all of
these facts and does not enlarge the F99 boundary.

## Total-input-bitlength complexity: PASS

The corrected claim is polynomial in the total explicit bit length of the
endpoint batch and exposure list. This is the correct input measure.

- Each nontrivial P66 refinement decreases total logarithmic value mass by at
  least one, so the number of refinements and work entries is polynomial.
- If the exposure list has total bit length `H`, its product has `O(H)` bits.
- Every successful saturation division at least halves its remaining block.
- Gcd, exact division, integer square root, and `GF(2)` rank have polynomial
  bit cost.

The additional `poly(log N)` statement is correctly conditional on the
declared C2T lists having polynomial size. The fixed lists have 54 times 784
transitions, so they meet that condition.

## Final status

All four requested corrections are present and accurate:

1. exact mask-set equality;
2. raw-batch versus circuit-local scope, counts, and ranks;
3. the F99 second-carry identity; and
4. the total-explicit-input-bitlength complexity qualification.

Verdict: **PASS**.
