# F108 — public carry-coverage diagnostic

## Question

Can the factor-assisted raw-carry observation from F106 be stated and tested
without factoring any endpoint or relation value?  If it can, does carry
coverage itself force a square relation?

## Public input

Take a frozen batch of endpoint pairs

\[
(c_i,w_i),\qquad c_iw_i\equiv1\pmod N,
\]

and let column \(i\) represent the exact relation value \(c_iw_i\).  Also
take a public list of exposure integers.  For a canonical trajectory, an
exposure integer is the endpoint forced to divide two distinct retained
relation values by a zero carry.  A transition for which both carries vanish
is excluded when first-occurrence deduplication retains only one relation
value.

Let \(E\) be the product of the exposure integers.  A hidden prime row is
called carry exposed when its prime divides \(E\).

## Factor-free construction

Apply the P66/P106 gcd refinement to the endpoint entries

\[
(c_i,e_i),(w_i,e_i),
\]

where \(e_i\) is the unit column mask.  This gives pairwise-coprime terminal
integer blocks \((q_j,m_j)\).

For each terminal block, compute its \(E\)-supported part without factoring:

```text
t = q_j
s = 1
while gcd(t,E) > 1:
    d = gcd(t,E)
    s = s*d
    t = t/d
```

The loop takes at most \(\lfloor\log_2 q_j\rfloor\) iterations.  Keep the row
mask \(m_j\) exactly when \(s\) is not an integer square.

The theorem to prove is that the set of distinct kept public masks is exactly
the set of distinct unavailable nonzero prime-parity masks whose primes divide
\(E\).  Thus carry coverage, its rank, and whether it spans the full relation
row space are public polynomial-time properties of a frozen batch.  The bit
cost is polynomial in the total explicit bit length of the endpoint batch and
the exposure list.  It is polynomial in \(\log N\) when those lists have the
declared C2T polynomial size.

## Fixed tests

1. Replay the public F98 batch and its public 166-column useful circuit.
   Reconstruct the raw zero-carry exposure list from the eight represented
   oriented trajectories.  Test whether the public carry-exposed row span has
   rank 165, equal to the full circuit rank.  These are raw exposures anywhere
   in the eight trajectories.  The adjacent raw relation values need not both
   be columns of the selected circuit.
2. Repeat with all 54 round-one trajectories.
3. Separately restrict to carry transitions whose two relation values are both
   selected circuit columns.  This circuit-local rank must not be confused
   with raw-batch exposure rank.
4. Apply the theorem to the P104/F99 private-row family.  There every
   transition in \(c_e=2^e\) has a zero first carry, but the forced shared
   endpoints contain only the prime 2.  The constructed private primes must
   keep the full row rank at \(T\), while the carry-exposed span has rank at
   most one.

## Falsifiers and scope

The public theorem fails if an exposed hidden row is absent from the kept
mask span or if a kept mask is not supplied by an exposed hidden row.

The fixed F98 conclusion fails if the public exposed rank is below 165.  The
F99 boundary fails if carry exposure spans its private-row matrix.

Even a passing F98 replay is only a mechanism diagnosis.  It does not prove
that every input has full carry coverage, a relation dependency, or a
non-global normalized root.
