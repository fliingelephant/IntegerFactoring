# F149 V2 hostile re-audit — PASS

## Verdict

**PASS.**  The V2 statement repairs the only fatal error found in V1.  The
reused proof proves the repaired statement.  I found no false theorem,
counting error, density error, deduplication failure, or certificate error.

The result remains a fixed-center uniform-source boundary.  It proves no
all-input hitting law, no forced arithmetic cycle, and no factoring
algorithm.

## Frozen inputs

I read the complete V2 statement, reused proof, preserved V1 statement,
failed V1 audit, and manifest.  Their SHA-256 hashes are:

- `V2_STATEMENT.md`:
  `8e116d027dd5ecfe14f789fd301e9a6f4cf3b62e402fa2575cfc34406aa4d4dd`;
- `PROOF.md`:
  `08cd204330f47429f20e747a1c8bad9a7084ec5de9249a8e5e755f55e305da0e`;
- preserved `STATEMENT.md`:
  `25af29ad09343eef88d7652f988b4ebd2f982e0d17ec6a0de867982c7e660738`;
- `HOSTILE_AUDIT_FAILED.md`:
  `e461d3984a77e4873f0bbcfdc5c6fa2de6bf8d2ea3b30fa9d45534942ac81346`;
- `MANIFEST.md`:
  `31be9a4703733184e9f1d5126f8f3b64d13419b7642f05c00684b9a5c3196044`.

The two requested frozen hashes match exactly.  A direct V1-to-V2 diff has
only the V2 title and the intended self-loop repair: `h >= 1` becomes
`h >= 0`, followed by the correct statement that usefulness forces
`h >= 1`.

## V1 failure is fully repaired

The failed audit used

\[
N=77,\qquad q=2,\qquad \alpha=S=3.
\]

Here the self-loop is exact, but

\[
\alpha^2-S^2=0.
\]

V2 now permits `h=0` and classifies this case as the global root `+1`.
The reused proof already derives `h >= 0` and separately excludes `h=0`
only under usefulness.  Thus there is no remaining statement/proof mismatch.

## Canonicalization and singleton theorem

Since `a = alpha (mod N)`, the canonical endpoint `c`, its inverse `w`,
every divisibility test on `c`, and every exact containment residual are
unchanged.  Also

\[
[L_a]=[qw],
\qquad
L_aL_\alpha=(qa\alpha w)^2,
\]

and

\[
qa\alpha w\equiv q\alpha^2c^{-1}\equiv1\pmod N.
\]

Thus the raw squared anchor changes neither the binary square class nor the
normalized root class once its residue is fixed.

For the actual P128 values,

\[
CL_a=a^2w^2(qc).
\]

Multiplication by the nonzero square `a^2 w^2` cannot change whether a
positive integer is a square.  Therefore the product is a square exactly
when `qc=s^2`.  Its positive root is `R=aws`, and reduction gives

\[
R\equiv s(q\alpha)^{-1}\pmod N.
\]

Multiplication by the unit `q alpha` proves both exact gcd identities

\[
\gcd(R\pm1,N)=\gcd(s\pm q\alpha,N).
\]

Also `s^2 = qc = q^2 alpha^2 (mod N)`.  Hence the normalized root is useful
exactly when the corresponding local signs are mixed.  This is precisely an
ordinary congruence of squares.

## Positive self-containment

Put `z=[alpha^2]_N` and write

\[
c=qz-kN,
\qquad
0\le k=\left\lfloor\frac{qz}{N}\right\rfloor<q.
\]

If `q` divides `c`, then `q` divides `kN`.  Since `q` is a unit modulo `N`,
`q` divides `k`, and the displayed range forces `k=0`.  This proves

\[
q\mid c\quad\Longleftrightarrow\quad qz<N,
\]

with residual `T=z`.  On this branch, `qc=q^2z`, so the singleton closes
exactly when `z=S^2<N/q`.

The normalized root is `S alpha^{-1}`.  Multiplication by the unit `alpha`
gives the stated factor tests `gcd(alpha-S,N)` and `gcd(alpha+S,N)`.
Since `alpha^2 = S^2 (mod N)` and `0<S^2<N`,

\[
\alpha^2-S^2=hN
\]

has `h >= 0`.  If `h=0`, positivity forces `alpha=S`, so the root is `+1`.
Therefore usefulness implies `h >= 1`.  V2 does not claim the false
converse: a positive `h` can still accompany the global root `-1`.

## Exact semiprime counts

Let `N=p*ell` for distinct odd primes and write uniquely `q=du^2`, with
`d` squarefree.  A canonical unit endpoint satisfies `qc=s^2` exactly when

\[
c=dv^2,
\qquad
dv^2<N,
\qquad
\gcd(v,N)=1.
\]

For each such positive `v`, the endpoint equation is

\[
(u\alpha)^2\equiv v^2\pmod N.
\]

It has exactly four unit solutions: independent signs modulo `p` and
`ell`.  Two are global signs and two are mixed signs.  Distinct positive
`v` values give distinct canonical integers `d v^2`, so their solution
sets do not overlap.  The useful count is therefore exactly `2V_d`.

For self-containment, each admissible `S` gives the equation

\[
\alpha^2\equiv S^2\pmod N.
\]

The same four-sign argument gives exactly two useful anchors.  Distinct
positive `S` values give distinct endpoints `qS^2<N`.  Hence the useful
self-loop count is exactly `2W_q`.

The density estimates are also correct.  We have

\[
V_d<\sqrt{N/d}
\]

and, for distinct odd primes,

\[
\frac{\varphi(N)}{N}
=\left(1-\frac1p\right)\left(1-\frac1\ell\right)
\ge\frac{8}{15}>\frac12.
\]

These imply the two inequalities in (11).  The identical estimate with
`W_q<sqrt(N/q)` proves (12).

With the standard convention that `n` is the input bit length, every fixed
center has singleton probability less than `4/sqrt(N)`.  Thus

\[
\Pr[\text{any hit}]
\le \frac{4M}{\sqrt N}
=2^{-n/2+o(n)}
\]

for `M=2^polylog(n)`, without independence.  The fixed-center scope matters:
uniform anchor marginals alone would not justify the same claim if the
center could correlate with the current anchor.  V2 explicitly fixes `q`
before stating the count, so it does not make that stronger claim.

## Deduplication, collisions, and cycles

The singleton survives global exact-value deduplication whenever it can be
useful.  If `C=L_a`, then `c=qa^2<N`.  This forces `a=alpha`, the positive
square root is the repeated value itself, and its normalized root is
`C=1 (mod N)`.  Therefore a useful singleton has two distinct exact values.
If either value equals an occurrence retained elsewhere, replacing the
occurrence does not change the exact integer product or its positive root.

This conclusion is only about deduplication of the actual exact values
`C` and `L_a`.  It does not authorize deleting equal transformed bridge
integers that carry different supplied roots.  That separate P129 metadata
rule remains intact.

If `alpha^2=beta^2 (mod N)`, then
`theta=alpha*beta^(-1)` is a square root of one.  For odd `N`, every prime
power dividing `N` divides exactly one of `theta-1` and `theta+1`.  A
non-global sign pattern therefore gives proper factors through both sign
gcds.  The global cases are exactly the two P71 signs.

For a directed containment-cycle collection, multiplying

\[
q_e\alpha_e^2\equiv q_{e+1}T_e\pmod N
\]

around the cycles cancels all centers.  If the residual product is `S^2`,
then

\[
A_0^2\equiv S^2\pmod N,
\qquad
\rho=A_0S^{-1}\pmod N.
\]

A declared public word for `S` turns this into twice a public exponent-vector
difference, which is the P71 half-relation target.  Without such a word, it
is the ordinary integer square-class closure retained by P128/P129.  Raw
anchor magnitude changes neither case.

## Finite certificate

For `N=77`, `q=2`, and `a=25`, direct recomputation gives

\[
[a^2]_{77}=9,
\qquad
[2a^2]_{77}=18,
\qquad
w=30.
\]

The endpoint screens are

\[
\gcd(18-30,77)=1,
\qquad
\gcd(18+30,77)=1.
\]

The two exact values and their root are

\[
C=540,
\qquad
L_a=37500,
\qquad
CL_a=4500^2.
\]

Finally,

\[
4500\equiv34\pmod{77},
\qquad
\gcd(34-1,77)=11,
\qquad
\gcd(34+1,77)=7.
\]

The same-residue identities `2*3^2=18` and
`2*5^4=1250=18 (mod 77)` are correct.  The certificate is a valid strict
source-semantic capability witness.  The statement correctly disclaims a
surviving full preprocessing run and any mechanism beyond P71/P128.

## Independent exhaustive stress check

I also ran an independent SageMath counterexample search.  It found zero
failures in:

- all 660,950 unit triples `(N,q,alpha)` with odd `3 <= N < 180`;
- 1,982,850 raw clones `a=alpha+kN` for `k=0,1,2`;
- all 49,788 singleton-square cases in that domain;
- all 9,123 exact-value coincidences `C=L_a` in that domain;
- all 19,316 ordered squared-residue collisions in that domain;
- all 9,383 unit-center cases for distinct odd primes
  `3 <= p < ell < 32`, checking both exact counts and all density bounds;
- the complete displayed `N=77` certificate tuple.

The exhaustive search is supporting evidence, not a replacement for the
algebraic checks above.

## Scope conclusion

Every V2 theorem and the reused proof pass.  The comparison with
P71, P114, and P128--P131 is consistent with those promoted boundaries.
F149 V2 removes raw numerical anchor magnitude as an independent singleton
or containment signal.  It leaves exactly the stated open channels: a
nonuniform residue source or a multi-relation arithmetic closure.

This re-audit does not supply the still-required statement-only blind
reconstruction, cross-family audit, human audit, or literature review.
