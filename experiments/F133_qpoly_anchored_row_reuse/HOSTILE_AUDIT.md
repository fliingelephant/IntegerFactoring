# F133 hostile audit — anchored feedback row reuse

## Verdict

**PASS.** The frozen theorem is correct as stated. The audit found no
counterexample, missing valuation case, invalid asymptotic estimate, or hidden
factoring assumption.

The result is only a source-side row-reuse theorem. It does not prove a binary
dependency, a non-global square root, or an integer-factoring algorithm.

## Frozen input

The audit read `STATEMENT.md`, `PROOF.md`, and `MANIFEST.md` in full before it
tested any claim. It did not edit those files.

- `STATEMENT.md` SHA-256:
  `b4848b22ea324421282dcfbbef9afc28576d2ea8233f8256a03b0797e1ea1bb7`
- `PROOF.md` SHA-256:
  `44e85f1914ba600a86288fb9961ff5b295dd1e0839d14493c8a6f38f83077cec`
- `MANIFEST.md` SHA-256:
  `ec876597bc2e41ab22032e69503d4c2b2d394afe7ca16b533a16051eec649844`

The hashes were checked again after the audit. They did not change.

## Audit protocol

The audit used the following hostile sequence.

1. Reconstruct the canonical-inverse identity without using the supplied
   derivation.
2. Split the proof into all possible cases for (v_r(w)).
3. Try to defeat the conclusion with repeated exact values and global
   first-occurrence deduplication.
4. Recompute every elementary constant in the primorial bound at the endpoint
   (n=64), and check the required monotonicity for all larger (n).
5. Recompute the carry-bucket count and its strict inequalities.
6. Check the adaptive transcript recurrence against the actual F130 and F132
   source rules, including direct screens and duplicate endpoint
   presentations.
7. Search finite configurations that satisfy the strong product hypothesis,
   with special tests for all three valuation cases.

The proof verdict does not depend on the finite checks.

## Exact mathematical checks

### 1. Canonical anchored-carry identity

For an eligible prime (ell), multiplication by (N) is invertible modulo
(ell). Thus there is one digit (A_ellin[0,ell-1]) such that

\[
w+NA_\ell\equiv0\pmod\ell.
\]

The strict hypothesis (q<N/B), with (ellle B), gives

\[
0<\ell q<N.
\]

Also,

\[
0<w+NA_\ell\le (N-1)+N(\ell-1)=N\ell-1.
\]

Therefore

\[
z_\ell=\frac{w+NA_\ell}{\ell}
\]

is an integer in ([1,N-1]). Direct multiplication gives

\[
(\ell q)z_\ell=q(w+NA_\ell)\equiv qw\equiv1\pmod N.
\]

Hence (z_ell) is the canonical inverse of (ell q), and

\[
P_N(\ell q)=q(w+NA_\ell).
\]

The equivalence (A_ell=0\iffell\mid w) is exact. For fixed (q,w,N),
the last displayed integer is strictly increasing in (A_ell). Thus two
different digits cannot give the same exact value.

### 2. All (r)-adic cases

Let (r>B) be prime and let (v_r(q)) be odd. Since (q) is a unit modulo
(N), (r\nmid N).

If (r\mid w), then every observed nonzero digit satisfies
(0<A_ell<B<r). Consequently,

\[
w+NA_\ell\not\equiv0\pmod r,
\qquad
v_r(w+NA_\ell)=0.
\]

If (r\nmid w), there is one residue

\[
A_*\equiv-wN^{-1}\pmod r
\]

that can give positive (r)-adic valuation. Every observed digit is already
in ([0,B)subset[0,r)). Thus every observed digit other than (A_*) has
valuation zero. This remains valid when the valuation at (A_*) is
(2,3,4,ldots); the proof never assumes squarefreeness.

For each fixed digit (A), the product of all eligible anchor primes in that
digit bucket divides (w+NA). Therefore:

- the zero bucket has product at most (w<N);
- a nonzero bucket has product below (NB);
- if all eligible digits were zero or the one possibly bad digit (A_*),
  then (G_B(N,q)<N^2B).

This contradicts the theorem's product hypothesis. Hence a nonzero even
valuation digit exists.

### 3. Deduplicated row degree

The three exhaustive cases are:

1. (r\nmid w): the unary value is odd in row (r), and one distinct
   nonzero good-digit value is also odd.
2. (r\mid w) with even (v_r(w)): the unary value is odd, and one distinct
   nonzero-digit value is odd.
3. (r\mid w) with odd (v_r(w)): the unary value is even. If there were
   zero or only one distinct nonzero digit, the eligible-prime product would
   be at most (w), or below (w(w+NA)<N^2B). Thus there are at least two
   distinct nonzero digits. Both give odd row entries.

Different digits give different exact integers. If either integer occurred
in an older ledger, its first copy is already retained. If it did not occur,
the current scan retains it. Global exact-value deduplication therefore
cannot reduce the certified degree below two.

### 4. Uniform primorial cutoff

The binomial-coefficient argument correctly gives

\[
\psi(x)\ge(x-1)\log2-\log(x+1).
\]

The identity

\[
\psi(x)-\vartheta(x)
=\sum_{k=2}^{\lfloor\log_2x\rfloor}\vartheta(x^{1/k})
\]

and the elementary estimate (artheta(y)le ylog y) give

\[
\psi(x)-\vartheta(x)
\le\frac{\sqrt{x}(\log x)^2}{\log2}.
\]

At (x=n^3), (nge64), the discarded prime-power term is strictly below

\[
9\frac{145}{100}\left(\frac{13}{25}\right)^2\frac{n^3}{8}
=\frac{220545}{500000}n^3.
\]

The claimed lower bound reduces to

\[
891n^3>100000n+69000.
\]

It holds at (n=64), and its margin increases. The auxiliary functions
((\log n)/\sqrt n) and ((\log n)/n) are decreasing in the full declared
range. Thus

\[
\vartheta(n^3)>\frac6{25}n^3>4n\log2.
\]

Since (N<2^n), the full primorial is greater than (N^4). If (X) is the
product of the primes at most (n^3) that divide (Nq), then

\[
X\le\operatorname{rad}(Nq)\le Nq<\frac{N^2}{n^3}.
\]

Dividing by (X) proves

\[
G_{n^3}(N,q)>N^2n^3.
\]

No prime number theorem is used.

### 5. More than (n^2/4) good digits

Let (g) count distinct good nonzero digits. There is one zero bucket,
(g) good buckets, and at most one bad nonzero bucket. Therefore

\[
G_{n^3}(N,q)<N(Nn^3)^{g+1}.
\]

Combining this with the retained primorial mass gives

\[
g>
\frac{(6/25)n^3+3\log n-3n\log2}
     {n\log2+3\log n}-1.
\]

For (nge64), the stated rational estimates give

\[
g>\frac{48n^2-599}{179}>\frac{n^2}{4}.
\]

The last inequality is equivalent to (13n^2>2396), which holds throughout
the declared range. Every counted digit gives a different exact value with
odd total (r)-valuation.

### 6. Conditional quasipolynomial cost

Every current block divides a retained unit endpoint. Thus it is a unit and
is below (N). If (M_t) is the number of current blocks and (Lambda_t)
is the total endpoint bit length, one copy of every block divides the endpoint
product. Hence

\[
M_t\le\Lambda_t.
\]

One anchored round appends at most (2M_tE) endpoints of at most (n) bits,
so

\[
\Lambda_{t+1}\le(1+2nE)\Lambda_t.
\]

With (T=L^2), (E=2^{L^2}), and the conditional F130/F132 initial bound,

\[
\log_2\Lambda_T
\le O(L^4)+T\log_2(1+2nE)
=O(L^4).
\]

The number of positions, every refinement, and the final P66 basis-root test
are polynomial in this explicit transcript. Replacing (E) by (E^2) in
the per-block menu changes only the constant in the (O(L^4)) exponent.

The bound uses the fixed (T=L^2) round cap. It does not apply to an
unbounded fixed-point iteration.

## Direct-screen and composition checks

- The source screens (gcd(a,N)) before inversion. A proper result already
  factors (N). On the surviving branch, both (a) and every current block
  are units.
- Both sign screens on the new canonical endpoint pair run before exact-value
  deduplication. Thus a duplicate exact relation can still factor through its
  new endpoint presentation, as required by the corrected F132 boundary.
- All endpoint presentations remain in the refinement transcript even when
  their exact relation value is a duplicate.
- On a completed no-factor scan, Theorems 2--4 give the stated retained-row
  conclusion. If an implementation halts earlier on a proper screen, it has
  already achieved the stronger outcome of finding a factor.
- For (nge64), the capped bank
  (1\le a\le\min(E,N-1)) contains the full range through (n^3). For the
  optional (B=E) use, the hypothesis (q<N/E) itself implies (E<N/2),
  so the cap cannot remove a needed anchor.
- The F133 complexity claim is explicitly conditional on the declared F130
  and F132 transcript bounds. It does not silently promote either source to
  a successful factoring algorithm.

## Independent finite diagnostics

These checks were audit diagnostics. The proof above is the authoritative
evidence.

An exhaustive integer search used (B=20,21,22). For each (B), it searched
all (N) up to the largest value allowed by
(G_B(N,q)\le\prod_{ell\le B}\ell), all admissible (q), and every odd
prime row (r>B) in (q). It recomputed each canonical inverse, carry digit,
exact value, and (r)-adic parity. The numbers of configurations satisfying
the strict product hypothesis were:

| (B) | checked configurations |
|---:|---:|
| 20 | 74 |
| 21 | 49 |
| 22 | 31 |

All 154 configurations retained at least two distinct odd-(r) exact values.

The audit also checked one exact representative of each valuation case:

| case | (N) | (B) | (q=r) | (w=iota_N(q)) | product check |
|---|---:|---:|---:|---:|---:|
| (r\nmid w) | 503 | 20 | 23 | 175 | (9{,}699{,}690>5{,}060{,}180) |
| odd (v_r(w)) | 577 | 20 | 23 | 276 | (9{,}699{,}690>6{,}658{,}580) |
| even (v_r(w)) | 993 | 30 | 31 | (961=31^2) | (2{,}156{,}564{,}410>29{,}581{,}470) |

Finally, at the lower uniform boundary, the audit used

\[
n=64,quad B=262144,quad
N=9223372036854775967,quad q=r=262147.
\]

The hypotheses (q<N/B) and (gcd(q,N)=1) hold. The complete eligible-prime
scan found 22,998 eligible anchors and 20,960 distinct good nonzero digits.
This is greater than the required (n^2/4=1024).

## Non-blocking wording notes

Two optional clarifications can make later summaries harder to misread. They
are not corrections to a false theorem.

1. In an operational restatement, use “either any declared gcd screen returns
   a factor, or the completed ledger has the stated row degree.” This wording
   includes the initial (gcd(a,N)) screen.
2. When invoking the (n^3) cutoff, state explicitly why the
   `min(E,N-1)` cap still contains the required prime subbank.

## Exact scope

F133 proves that a large prime occurring oddly in a sufficiently small
dynamic block cannot remain a private prime-parity row after the full public
anchor scan. It also proves that this adaptive source fits inside the declared
quasipolynomial budget.

It does not cover large wrapped blocks, blocks with only small odd rows,
large primes occurring only to even order, or later degree-one peeling
cascades. Row degree at least two does not imply a binary kernel. A binary
kernel does not imply a non-global normalized root. Therefore this audit does
not certify an all-input factoring theorem.
