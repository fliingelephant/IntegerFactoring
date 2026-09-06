# F226 result

## Mathematical result

The packet proves a positive source theorem and an exact boundary.

1. The top-bit child `N-2^(n-1)` is one valid fixed-ratio recursive child,
   but its factorization does not force APR orbit acceptance.
2. For `m=floor(n/2)`, a uniform odd multiplier makes
   `uN mod 2^m` exactly uniform odd.  All nested binary prefixes are
   half-size recursive children.  QP many refreshed banks, including all
   auxiliary `ell-1` factorizations, have a solved QP recursion.
3. The complete multiplier ensemble is exactly the odd double factorial,
   independent of `N`; a fixed prime is sampled with probability essentially
   `1/ell` per full child and at most `(m+4)/ell` per prefix bank.
4. Locally accepted order-`h` primes divide the hidden common cyclotomic gcd
   `gcd(p^h-1,q^h-1)`.  A common exponent-`i` set divides `N^i-p` and has at
   most `n max(1,i)` bits of total squarefree support.
5. A polylogarithmic block can enumerate every squarefree divisor under a
   QP cap.  It therefore turns a terminal-size compatible hidden subproduct
   into a genuine verified Las Vegas attempt, without an APR selection
   oracle.  The cap is exceeded with an explicitly bounded probability.
   In particular, if `p-1` or `q-1` has a QP-sized squarefree divisor that
   closes the beta-two terminal gap, one full child gives a verified factor
   with inverse-QP probability at least `1/(4Q)` for a public QP bound
   `d<=Q`.
6. The bank does not randomize the forced local anchor `N`.  Orbit acceptance
   remains `p in <N mod ell>`, and exponent classes must satisfy generalized
   CRT across primes.
7. The exact affine hyperbola model gives terminal compatible-orbit
   probability at most `|I|/phi(S)`.  For QP `|I|` and
   `S>=N^(1/4)/QP`, this is `2^(-Omega(n))`.  This rejects only the generic
   uniform-orientation justification, not the multiplier distribution on
   adversarial integers.
8. More strongly for this source, compatible support exposed above any
   cutoff `Y` has expected log weight at most `QP/Y`.  The cutoff can be
   chosen numerical QP to dominate any proposed inverse-QP tail, while all
   primes below it can be deterministically enumerated.  One terminal-size
   small-order prime is exponentially unlikely.

The remaining all-input requirement is now a precise integer statement: a
uniform harmonic-mass lower bound for a compatible hidden support
`N^i-p`, or a new factor/carry transition when the scalar APR/orbit test
rejects.  The safe-prime-shift model shows why smoothness cannot be assumed.

The candidate is self-audited.  It needs a fresh hostile audit and then a
statement-only reconstruction before promotion.

## Finite guidance

- D06: 7,212 recursion-safe deterministic lower-half banks; 6,415 reach the
  ideal-oracle quarter threshold, 797 fail, and 54 have no accepted prime.
- Smallest exact zero-acceptance witness:
  `333859=563*593`, with distinct children `3` and `35=5*7`.
- D08: exact enumeration of every random multiplier on the 54 zero rows,
  still granting hidden local labels.  Success ranges from `330/512` to
  `0.951416015625`, with mean `0.8218157733`.

The finite pattern is favorable but cannot supply the missing uniform
inverse-QP theorem.  Individual auxiliary orders are artificially small in
this 19–29-bit cohort.

## Run history

- D01: Sage cache sandbox failure before mathematics.
- D02: Python/Sage integer-method mismatch before the first row.
- D03: linear discrete-log scan did not complete under the orchestration
  call; no result artifact.
- D04: completed upper-half discovery scan.  Its pooled construction is
  recursion-unsafe.  The 111 MiB JSON was losslessly replaced by a 4.7 MiB
  gzip file; `gzip -d` recovers the exact original bytes.
- D05: completed mathematics, then emitted invalid partial JSON because Sage
  integers were not serializable in the final summary.
- D06: serialization-only repair; valid deterministic lower-half result.
- D07: valid exact numerators, but rational display fields were converted to
  zero.
- D08: postprocessing-only repair of the D07 rate fields.
