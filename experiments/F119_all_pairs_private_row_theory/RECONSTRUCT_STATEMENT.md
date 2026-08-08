# Proof-blind reconstruction statement: cross-pair private-row family

## Isolation

Read only this statement. Do not read another F119 file, `PROVED.md`,
`FAILED.md`, `REGISTRY.md`, or `notes/Progress.md`. Do not search the project
for a proof or construction.

Write only new files in this directory whose names start with `RECONSTRUCT_`.
State every failed proof route. Pin the statement and final artifacts with
SHA-256. This is a proof-only task. Do not run a computation unless it is
necessary; if one is necessary, register its source, timeout, log, output,
and failures before using it as evidence.

## Definitions

Let (N>1). For a unit (1\leq c<N), let (w) be its least positive inverse
modulo (N), and define

\[
P_N(c)=cw=1+\kappa_N(c)N.
\]

For a finite set (K) of distinct nonzero carries, make one binary column for
each (1+kN), (k\in K). A prime row contains the parity of its valuation in
these values. A row is private if it is one in exactly one selected column.

For bit length (n), the fixed all-pairs menu contains both residues
([u^e v]_N) and ([u v^e]_N) for every (2\leq u<v\leq n) and
(0\leq e\leq n^2). It uses first occurrence by canonical residue and then
first occurrence by positive exact value.

## Claims to reconstruct

### A. Exact carry laws

For distinct carries (k,\ell), prove

\[
\gcd(1+kN,1+\ell N)
=\gcd(1+kN,|k-\ell|)
=\gcd(1+\ell N,|k-\ell|).
\]

For every prime (r\nmid N), prove that (r\mid1+kN) holds in one residue
class of (k\pmod r). Deduce these two consequences for a carry set of
diameter (D):

1. row (r) has degree at most (1+\lfloor D/r\rfloor);
2. if column (k) has no private odd-valuation row, then
   \[
   \operatorname{sf}(1+kN)\mid\prod_{\ell\in K,\ell\ne k}|k-\ell|,
   \]
   where `sf` is the product of primes with odd valuation.

### B. Infinite cross-pair submatrix

Prove that, for every sufficiently large integer (t), there is an odd
distinct-semiprime, non-perfect-power input (N_t), with bit length (n_t),
and (M_t=t(t-1)=\Theta(n_t/\log n_t)) distinct positive exact values from
the exponent-two all-pairs menu such that:

1. each selected value has a distinct prime of valuation one that divides no
   other selected value;
2. the selected square-class columns are linearly independent;
3. both factors of (N_t) exceed (n_t^2);
4. at each named exponent-two attempt (c=a^2b), both endpoint sign gcds are
   one.

The named residue (c) can have appeared earlier in the source; then its
endpoints are unchanged. A different earlier residue can also have the same
exact value. The value-based private-row claim survives exact-value
deduplication, but do not claim that the sign screens of such a different
representative are covered by item 4.

You may use the prime number theorem, Bertrand's postulate, the Chinese
remainder theorem, Dirichlet's theorem, and Linnik's theorem as named
established results. Give all size bounds needed to keep the bases and
exponent inside the fixed menu.

### C. Boundary

Do not claim a full-source obstruction. The protected rows need only remain
private inside the selected submatrix. Other seed, frozen, or all-pairs
columns can reuse them. Do not claim the absence of an earlier direct factor.

State exact sufficient missing conditions for:

1. stable private rows after the complete source;
2. a nonzero exact square dependency;
3. a non-global square root that factors (N).

Do not claim publication novelty or an arbitrary-input factoring algorithm.
