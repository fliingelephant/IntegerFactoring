# F239 preregistration: binary quotient-spine word source

## Purpose and evidence boundary

This scan tests a public integer-word source for the F238 residuals.  It is
for exact finite counterexample search and conjecture discovery.  A finite
scan will not prove an asymptotic all-input theorem or counterfamily.

No F239 numerical computation has run before this preregistration.  Existing
frozen F236 and F237 outputs were read only to define the comparison rows.
Any follow-up family search or changed bound requires a new preregistration.

## Endpoint qualification and frozen word

For every row, put

\[
 N=pq,\qquad n=\lceil\log_2(N+1)\rceil,
 \qquad K_j=\left\lfloor\frac{N}{2^j}\right\rfloor.
\]

The literal proposed range `1<=j<=n` has `K_n=0`, because `N<2^n`.
Therefore its product is zero.  It is outside the F238 premise `W>=1`, and
`v_2((N-1)W)` is undefined.  The scan will verify and report this endpoint
on every row, but it will not treat the zero product as a valid word.

The primary nonzero quotient-spine word is frozen as

\[
 W_{\rm bin}^+
 =\prod_{j=1}^{n-1}K_j^n.                            \tag{R1}
\]

The endpoint `K_(n-1)=1` is retained.  It is harmless.  No quotient,
exponent, or index will be added after the scan starts.

Also put

\[
 R_j=N-2^jK_j=N\bmod 2^j,
\]

and use deterministic round-half-up to define the signed centered suffix

\[
 C_j=N-2^j\left\lfloor\frac{N+2^{j-1}}{2^j}\right\rfloor,
 \qquad -2^{j-1}\le C_j<2^{j-1}.
\]

Freeze the three base words as

\[
 W_{\rm rem}=\prod_{\substack{1\le j\le n\\R_j\ne0}}R_j^n,
 \qquad
 W_{\rm ctr}=\prod_{\substack{1\le j\le n\\C_j\ne0}}|C_j|^n. \tag{R2}
\]

Test all seven nonempty menus formed from these three words:

\[
 W_{\rm bin}^+,\ W_{\rm rem},\ W_{\rm ctr},\
 W_{\rm bin}^+W_{\rm rem},\
 W_{\rm bin}^+W_{\rm ctr},\
 W_{\rm rem}W_{\rm ctr},\
 W_{\rm bin}^+W_{\rm rem}W_{\rm ctr}.                \tag{R3}
\]

For the odd inputs in this scan every `R_j` and `C_j` is nonzero.  The
explicit exclusions fix the boundary for possible later comparison with
even integers; they do not change this domain.  The endpoints are retained:
`R_1=1`, `R_n=N`, `C_1=-1`, and `C_n=N-2^n`.

## Residuals and exact incidence

Put

\[
 d=\gcd(p-1,q-1),\qquad
 s_p=(p-1)/d,\qquad s_q=(q-1)/d.
\]

For every prime power `ell^a || s_p` or `ell^a || s_q`, record every index
`j` for which `ell | K_j`, every index for which `ell | R_j`, and every
index for which `ell | C_j`.  Since `ell^a<N<2^n`, one has `a<n`; hence the
exponent `n` saturates the full prime power as soon as one incidence occurs.
The exact remaining quotient residual is therefore

\[
 r_i=\prod_{\substack{\ell^a\parallel s_i\\
              \ell\nmid K_j\ \text{for all }1\le j<n}}
       \ell^a.                                        \tag{R4}
\]

Define the residual for each menu in (R3) by retaining exactly the prime
powers whose prime misses every factor list present in that menu.

For each incidence calculation, the program will cross-check all three
equivalent conditions

\[
 \ell\mid K_j,
\]

\[
 N\bmod(\ell2^j)<2^j,
\]

and, on the `p` side,

\[
 q\equiv N\bmod2^j\pmod\ell,
\]

with `p` and `q` exchanged on the `q` side.  It will abort on a mismatch.
For remainder incidence it will directly cross-check

\[
 \ell\mid R_j
 \quad\Longleftrightarrow\quad
 (N\bmod2^j)\bmod\ell=0.
\]

For centered incidence it will directly cross-check `ell | C_j` against
the round-half-up formula above and against the piecewise reduction of
`R_j` into the displayed centered interval.  It will also compute all seven
words modulo `s_i` by modular powering and check that the gcd residuals
equal the prime-incidence constructions.

## Frozen exact domains

### A. Named comparison rows

Evaluate these rows first:

1. the F236 combined-word worst row
   `(p,q)=(4190987,4243619)`;
2. the F236 cubic-carry worst row
   `(p,q)=(3565721,6646697)`;
3. the F237 certified row
   `(p,q)=(15187245471009208343,26569391171797958567)`.

For the F237 row, use the frozen certified residual factorizations.  Check
all three incidence lists by direct integer arithmetic.  Do not rerun a
probable-prime test or infer primality from a library call.

### B. Complete F236 zero-defect domain

Enumerate every pair of distinct odd primes

\[
 3\le p<2^{22},\qquad p<q<2p,
\]

for which, with `B=2^floor(n/2)`, one has `B | N-1`.  Generate candidates
as in F236 and directly check primality, balance, bit length, and zero
defect.  The count must equal the frozen F236 count `34,463`; abort if it
does not.

### C. Broad balanced-semiprime domain

Enumerate every pair of distinct odd primes

\[
 3\le p<2^{16},\qquad p<q<2p.
\]

There is no zero-defect or equal-valuation filter.  Generate all primes
below `2^17` by a deterministic sieve, enumerate the displayed pairs, and
factor `p-1` and `q-1` exactly with the sieve table.

## Frozen outputs

For each named row, report:

- `N,n,d,s_p,s_q` and their complete factorizations;
- all quotient, positive-remainder, and centered-remainder hit indices for
  every residual prime;
- for every menu in (R3), `r_p,r_q,min(r_p,r_q)`;
- the exact comparison with the relevant published F236/F237 residual;
- the bit lengths of all base and combined words, computed as sums of factor
  bit lengths without materializing a word.

For domains B and C, report:

- the exact number of rows by input bit length;
- for every menu in (R3), the maximum of `min(r_p,r_q)` globally and by
  input bit length;
- every global record setter and the twenty worst rows, ordered first by
  decreasing `min(r_p,r_q)` and then by increasing `N`;
- exact counts and fractions for each menu with `min(r_p,r_q)` equal to one
  and at most `n`, `n^2`, and `n^3`;
- exact counts for all eight quotient/remainder/centered incidence masks,
  together with first-hit indices;
- for each worst row, the complete residual factorizations and all hit
  indices.

The report will separate exact identities, finite scan facts, heuristics,
and unresolved asymptotic claims.  It will not promote a finite worst row
to an infinite counterfamily.

## Implementation, resources, and stopping rule

The implementation will use exact unsigned integer arithmetic for domains B
and C.  It will use arbitrary-precision integer arithmetic for the three
named rows.  No word in (R3) will be materialized.

Before either a local or SSH run, record CPU count, load, memory, swap, and
free disk.  Use one low-priority process.  Estimate peak memory and runtime
from the sieve bound and row count before launch.  The broad scan is capped
at `p<2^16`; the zero-defect scan is capped at `p<2^22`.  Stop after these
domains and the three named rows.  Do not enlarge a bound based on observed
results.
