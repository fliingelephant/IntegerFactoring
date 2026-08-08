# F111 Monotone-Extension Hostile Audit

## Verdict

**PASS, with an exact finite boundary.** All three proposed consequences are
correct after two qualifications:

1. Monotonicity applies to the existence of a useful dependency. A chosen
   kernel basis need not persist after extension.
2. The fixed pair schedule `(2,3),(2,4)` was selected after observing these
   experiments. It is constant-size program text, not per-input advice, but
   the result remains a post-selected fixed-instance success.

No candidate file was changed. This audit validates a consequence. It does not
promote the existing F111 certificate replay into the new algorithm.

## Evidence status

The promoted evidence is `MONOTONE_EXTENSION_verifier.py`, executed by
`MONOTONE_EXTENSION_run_with_timeout.py` with a 300-second hard timeout. The
final run returned `PASS` with exit code zero in 127.876129 seconds. Its full
JSON result and run transcript are `MONOTONE_EXTENSION_OUTPUT.json` and
`MONOTONE_EXTENSION_RUN.log`.

The earlier 128.887923-second refinement and 0.442453-second kernel diagnostic
were ad hoc inline computations. They had no named source, hard timeout, log,
or output, so they are preliminary and unpromoted. A first named dry run also
passed in 126.696825 seconds. It was not promoted because this audit then
corrected the relation-value bit bound and added explicit coordinate digests.
There were no failed hard-timeout runs.

## 1. Exact-value monotonicity

Let the first-occurrence exact-value decoder retain the distinct nonunit values

\[
P_1,\ldots,P_m.
\]

Appending more source records cannot remove or replace any of these columns.
A later repeated exact value is discarded. A later new value is appended as a
new column. Thus the extended parity matrix has the form

\[
M'=[M\;A].
\]

If (x\in\ker M), then ((x,0)\in\ker M'). Its exact product and positive
square root are unchanged. Therefore a useful dependency remains useful.

This does not imply that an elimination routine returns the same vector in its
new kernel basis. Let

\[
\bar\rho:\ker M'\to R/\{\pm1\}
\]

be the root map modulo global sign. It is linear. If the embedded old
dependency has nonzero image, every complete basis of (ker M') contains at
least one vector with nonzero image. Otherwise every linear combination of the
basis would have global root. Thus testing every basis root is independent of
pivot order and does not require the old support as advice.

**Claim 1 passes as an existence statement.** It fails if interpreted as
monotonicity of basis vectors, pivot positions, or displayed support.

## 2. Full fixed trajectory

The named factor-free verifier ran both appended pairs through every exponent
(0\le e\le n^2=1024). It regenerated the frozen source first and then used
the fixed order `(2,3),(2,4)`, exponent order, and orientation order. It used
the certificate stop only after full generation to audit the old prefix. The
stop did not control generation or decoding.

The original 15,383 relations are the exact prefix of the full relation
sequence. The full source statistics are:

| Quantity | Value |
| --- | ---: |
| Total source positions | 67,681 |
| Full appended positions | 4,100 |
| Retained relations | 15,884 |
| Duplicate residues | 51,797 |
| Unit exact values removed | 1 |
| Repeated exact values removed | 2,921 |
| Unique nonunit exact values | 12,962 |
| Prefix columns preserved in place | 12,569 |
| New columns after the prefix | 393 |

Pair `(2,3)` makes 2,050 attempts and retains no new residue. Full pair `(2,4)`
makes 2,050 attempts and retains 1,533 residues. Continuing beyond the F111
stop adds 501 retained records and 393 new unique nonunit exact values.

The first-occurrence decoder verified that all 12,569 prefix columns are the
initial coordinate block of the 12,962-column full matrix. The full retained
stream digest is
`660b6b8333fd46e3b0d60dc1b72a353371982dc2de3fad490e04dd18b32f2684`.
The deduplicated column-stream digest is
`68afa804f4a4ed6d49dd5127b7f05e972c85efdd9d97b771688a1cf61117594b`.

There are 31,768 endpoint direct screens over the full retained source. Exactly
31,767 give gcd one. One frozen screen has (c=w=1), so its minus gcd is (N).
No direct screen gives a proper divisor. Thus the full run reaches the parity
decoder without an earlier direct factor. A uniform implementation can return
immediately if any trial, invertibility, or endpoint screen does give a proper
gcd. All 1,023 trial screens also gave gcd one.

The complete factor-free decoder was also run on all 12,962 full-source
columns. It did not read the published 363 indices or known factors. It gave:

```text
parity rank                    = 12,923
kernel dimension               = 39
basis roots +1                 = 25
basis roots -1                 = 4
basis roots non-global         = 10
full root-image size/rank       = 4 / 2
root image modulo global sign   = 2 / 1
```

The full root image is

\[
\{1,1{,}058{,}780{,}986,2{,}182{,}851{,}487,N-1\}.
\]

For the independently computed non-global root
(r=1{,}058{,}780{,}986),

\[
r^2\equiv1\pmod N,
\quad
\gcd(r-1,N)=79{,}043,
\quad
\gcd(r+1,N)=41{,}011.
\]

The gcds multiply to (N). They were computed from the root. They were not
inputs to the replay.

In the promoted run, factor-free gcd refinement took 127.295570 seconds.
Binary kernel construction plus all 39 exact-product, integer-root, and
root-map tests took 0.384688 seconds. The verifier stored all 39 basis vectors
and root results. The refinement made 1,808,779,225 gcd tests and 87,979
splits. These are diagnostic measurements, not an asymptotic bound.

**Claim 2 passes.** The stop at 15,383 is needed to describe the original F111
certificate, but it is not needed by the full fixed-source algorithm.

## 3. Uniform polynomial-bit-time algorithm

The consequence defines one uniform (N)-input algorithm:

1. Set (n=\lceil\log_2(N+1)\rceil) and (B=n^2).
2. Apply trial gcd screens through (B).
3. Generate initial seeds `2..n`. Handle a noninvertible residue by gcd.
4. Compute the initial public gcd/perfect-power basis.
5. Run every derived frozen trajectory through exponents `0..B`.
6. Run the fixed appended pairs `(2,3),(2,4)` through exponents `0..B`.
7. Apply both endpoint direct gcd screens to each first retained residue.
8. Remove units and repeated exact relation values by first occurrence.
9. Compute a complete square-class kernel with a gcd-free basis.
10. Test the exact product, positive square root, and terminal gcds for every
    kernel-basis vector.

The program does not contain (N)'s factors, the 15,383 stop, or the 363
indices. Frozen pairs are computed from (N)'s initial endpoints. The appended
pairs are fixed constants. A deterministic sort or balanced map can implement
first-occurrence exact-value deduplication without a hash-table assumption.

### Source size

There are at most (n-1) frozen pair entries. The number of residue positions
is at most

\[
(n-1)+2(n-1)(n^2+1)+4(n^2+1)=O(n^3).
\]

For this (n=32), the bound is attained as 67,681 scheduled positions. Trial,
invertibility, and direct screens add only a polynomial number of gcd calls.
Modular exponentiation uses exponents at most (n^2).

### Integer size

Every retained endpoint is less than (N). Hence every exact relation value
satisfies

\[
P=cw<N^2
\]

and has at most (2n) bits. If (m=O(n^3)) values occur, the product for
one dependency has (O(mn)=O(n^4)) bits. Its exact integer square root has the
same polynomial bit bound. Exact multiplication, `isqrt`, modular reduction,
and gcd are polynomial in these sizes.

For this input, the maximum relation-value bit length is 64 and the maximum
tested basis-product bit length is 25,801.

### Decoder time and space

The audited gcd-free refinement uses gcd and exact division. On each split,
the sum of the binary logarithms of all pending and stable values decreases by
at least one. Its initial value is (O(mn)). Thus it makes only polynomially many
splits. Each pending value scans a polynomial-size stable list, so the number
of gcd tests is also polynomial. Exact perfect-power tests remove square
fragments without prime factorization. The resulting parity matrix has
polynomially many rows and columns. GF(2) elimination on polynomial-length bit
masks is polynomial.

The kernel has at most (m=O(n^3)) basis vectors. Testing each vector from
scratch uses at most (m) exact relation values and (O(n^4))-bit products.
Even the direct (O(m^2)) multiplication schedule remains polynomial. Storing
the complete matrix, kernel masks, and products also uses polynomial space.

Thus this is a uniform polynomial-bit-time algorithm. On the fixed F111 input,
the complete decoder has ten non-global basis roots and returns a proper factor.

**Claim 3 passes for this algorithm and this fixed input.** The result is more
than a fixed-certificate replay because the algorithm computes the complete
kernel and needs no dependency support. It is less than an all-input factoring
theorem because useful-root existence was proved only for this (N).

## Hidden-advice and theorem boundary

The following points cannot be removed from the statement:

- `(2,4)` was chosen after factor-assisted experiments. Hardcoding it is
  constant-size, input-independent program design, so the resulting program is
  uniform. It does not make the empirical choice unselected or universal.
- The original 363-index certificate is not used. The full decoder finds a
  useful basis root under its own pivot order.
- The original post-selected stop is not used. The algorithm runs both fixed
  appended trajectories to completion. The named verifier reads the stop only
  after generation to compare the preserved prefix with pinned prior evidence.
- First-occurrence exact-value deduplication is essential to the coordinate
  statement. Other deduplication or provenance conventions need a new audit.
- “Factor-free decoder” means no general integer-factorization or primality
  call. It still uses gcd-based integer splitting, exact perfect-power
  extraction, and terminal gcd factor extraction.
- The actual Python refinement has a large constant cost. Its measured runtime
  is not by itself a complexity proof. The bit-size and operation-count bounds
  above supply the polynomial claim.
- The algorithm is uniform only when formulated as an (N)-input procedure.
  The existing F111 files remain fixed-instance evidence and were not edited
  into such an executable.

The narrowest valid conclusion is:

> The fixed, no-stop source consisting of initial seeds, all public frozen
> trajectories, and complete `(2,3),(2,4)` trajectories has a useful exact-
> value dependency for (N=3{,}241{,}632{,}473). A uniform complete factor-free
> decoder finds a non-global kernel-basis root in polynomial bit time. No
> certificate indices, stop advice, or factors are required. This proves
> success on this input only.
