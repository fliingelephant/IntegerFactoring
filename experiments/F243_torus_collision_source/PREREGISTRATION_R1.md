# F243-R1 preregistration — exact C++ scan and bounded carry pilot

## Relation to the frozen F243 preregistration

The first preregistration did not name an execution runtime or specify the
aggregate buckets for its Monte Carlo clauses.  It remains unchanged and no
data scan was run under it.  This file freezes run `F243-R1` before any
input statistic is computed.

## Runtime and resource cap

Use one C++20 process on `ssh seetacloud`.  Do not install a new runtime.
Use exact `uint64_t`, signed `__int128`, and unsigned `__int128` arithmetic.
Floating point may format final ratios only.  It may not select an input,
classify an event, factor an integer, or compare a threshold.

The prime range gives

- `p,q < 2^14`,
- `N < 2^28`,
- `N^2-1 < 2^56`,
- every divisor and gcd-law weight is below `2^56`,
- every squared weight and probability denominator is below `2^112`, and
- multiplication by a target prime below `2^15` remains below `2^127`.

Use `__int128` for every product that can exceed `2^63`.  Pell coefficients
are computed only modulo a target prime.  Their distinctness over the
integers follows from the proved strict increase of `T_k(N)` for `N>1`;
the verifier does not materialize the exponentially long coefficients.
Before the full scan, time the first 100 hashed semiprimes.  Continue only
if the extrapolated wall time is below 30 minutes and peak RSS is below
2 GiB.  Otherwise stop without changing the run and report the resource
failure.

## Exact input selection

Use the input sets and SHA-256 ordering from `PREREGISTRATION.md`.  Implement
the SHA-256 ordering literally.  A hidden factor may label a target but may
not define a source.

## Exact scan

Run clauses 1--4 from `PREREGISTRATION.md` on every frozen target.  Cache a
box-source histogram by `(ell,B)` because the same-discriminant determinant
and trace-resultant identities remove `D` algebraically.  Count residue
frequencies in `O(B^2)` time and derive pair counts from the frequencies;
do not enumerate all pairs of samples.

For the Pell source, use exponent support `{0,...,T-1}`.  Compute its exact
pair-coordinate collision from `ord_ell(N+w)` and its exact trace collision
by direct modular frequency counts.  Exclude equal exponents.  The integer
trace values `T_k(N)` are strictly increasing, so there are no further exact
integer-equality atoms.

For the gcd-divisor law, compute each exact weight
`Pr(Z=d)=phi((N^2-1)/d)/(N^2-1)` by divisor enumeration from the verifier's
factorization.  Subtract the full exact-integer equality mass, not only a
uniform-object atom.

## Monte Carlo buckets

For each bit length `b in {25,26,27,28}` that occurs, choose the first input
of bit length `b` in the frozen SHA-256 order.  Run 200,000 accepted pairs
per public Jacobi sign and source.  Seed a xoshiro256** generator by SHA-256
of the run seed, bit length, Jacobi sign, source tag, and fixed
discriminant.  Rejection sampling uses fresh generator words.

The sources are:

1. raw unit discriminants in `{1,...,N-1}` conditioned on Jacobi sign;
2. the two canonical coefficients of the accepted Hilbert--90 point modulo
   `N`, represented in `{0,...,N-1}`, for each unit fixed discriminant
   `D in {-1,2,3,5,N-1,N+1}`; and
3. the determinant of two canonical Hilbert--90 coefficient pairs.

For a scalar coordinate, count an event only when its two canonical integer
values differ and agree modulo `ell`.  For a determinant, replace an exact
integer zero by one before testing divisibility.  Report Wilson intervals
only as descriptive diagnostics.  The counts, not the intervals, define the
data.

## Frozen output and interpretation

Write one machine-readable TSV plus a concise Markdown report.  Include all
summaries frozen in `PREREGISTRATION.md`, the input SHA-256 digest, runtime,
peak RSS, and exact counts for every Monte Carlo row.

The original interpretation rules and thresholds remain unchanged.  In
particular, the carry pilot can suggest a source but cannot establish an
asymptotic lower bound.
