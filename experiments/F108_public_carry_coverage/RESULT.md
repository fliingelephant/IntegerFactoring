# F108 — public carry coverage is computable, but carry alone does not force closure

**Status:** audited theorem with one completed factor-free fixed replay.  The
hostile audit and corrected narrow re-audit passed.  The proof-blind replay
proved the general theorem and every fixed F98 claim.  Its original statement
failed only because the F99 formula was omitted; the amended self-contained
boundary then passed a fresh proof-blind re-audit.

## General theorem candidate

Let \((q_j,m_j)\) be the pairwise-coprime terminal blocks from P66/P106
refinement of a frozen endpoint batch.  Let \(E\) be the product of any
public exposure integers.  For a terminal block \(q_j\), let

\[
S_E(q_j)
\]

be the largest divisor of \(q_j\) supported on primes dividing \(E\).  It is
computed by repeated gcd and exact division as specified in `DESIGN.md`.

Then the following equality of sets of distinct nonzero masks holds:

\[
\boxed{
\{m_j:S_E(q_j)\text{ is nonsquare}\}
=
\{r_p:p\mid E,\ r_p\ne0\}.
}
\]

Here \(r_p\) is the unavailable parity row of prime \(p\) across the relation
columns.

For a prime \(p\mid q_j\), P106 gives

\[
r_p=(v_p(q_j)\bmod2)m_j.
\]

Repeated gcd saturation puts the complete prime power
\(p^{v_p(q_j)}\) into \(S_E(q_j)\) exactly when \(p\mid E\).  Therefore
\(S_E(q_j)\) is nonsquare exactly when at least one exposed prime in that
block supplies the nonzero row \(m_j\).  This proves the displayed equality.
The loop and every square test have bit cost polynomial in the total explicit
input and exposure-list bit length.  For the declared C2T lists, this is
polynomial in \(\log N\).

## Fixed public replay

The executable received the pinned public F98 output.  It used its public
166-relation certificate and no relation factorization.  Public refinement
gave 227 distinct nonsquare row masks with rank 165 and nullity one.

The eight represented oriented trajectories contain 1,840 public **raw-batch**
carry exposure integers after 541 two-zero duplicates are excluded.  The two
adjacent raw values need not both be selected circuit columns.  Gcd saturation
marks 191 distinct public row masks.  They already have rank 165.  Thus their
row span equals the complete circuit row span and determines the same unique
dependency.

All 54 round-one trajectories contain 15,935 exposure integers after 6,008
two-zero duplicates are excluded.  They mark 200 distinct public row masks,
again with rank 165.  The public root check reproduces

\[
R=132013085\pmod N,
\qquad
(\gcd(R-1,N),\gcd(R+1,N))=(19727,10267).
\]

The factor-assisted counts are 194 and 203 prime rows.  The smaller public
counts 191 and 200 merge prime rows with equal masks.  Their ranks agree, as
the theorem predicts.

This is not a selected-to-selected local-carry statement.  If exposure is
restricted to transitions whose two relation values both occur in the
166-column circuit, only 34 exposure events arise in the eight represented
trajectories, or 82 when all round-one trajectories are offered.  The exposed
row span then has rank 54, not 165.  The full-rank result uses the larger raw
batch as an exposure reservoir.

This property cannot hold on all canonical trajectories.  In the F99
private-row family, \(c_e=2^e<N\), so every adjacent step has zero first
carry.  Its canonical inverses satisfy

\[
2w_{e+1}-w_e=N,
\]

so the second carry is one and the relation values are not removed as
two-zero duplicates.  Every forced shared endpoint is a power of 2.  Hence the
carry-exposed row span has rank at most one.  The constructed prime \(q_e\)
is private to column \(e\), so the complete \(T\)-column matrix has rank
\(T\).  Maximal local carry exposure therefore does not force one dependency.

The run completed in 0.15 seconds under a 180-second hard timeout.  Runtime is
only reproducibility evidence.

## Meaning

This makes one part of the feedback mechanism public.  The algorithm can
measure whether exact carry reuse covers all parity constraints.  It does not
need the hidden factorization of the relation values.

It also states the remaining source gap precisely.  A successful all-input
theorem must prevent private rows such as the F99 rows, and it must make at
least one resulting square root non-global.  Carry frequency by itself is not
enough.
