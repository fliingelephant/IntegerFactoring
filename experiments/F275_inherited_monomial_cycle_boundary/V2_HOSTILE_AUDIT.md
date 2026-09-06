# F275 V2 fresh hostile proof audit

## Verdict: PASS

The canonical-carrier repair closes the sole V1 blocker. The repaired size
claim, Theorem A, Theorem B, and the reduced-complement/F270 scope boundary
are correct under the stated hypotheses. I found no counterexample.

## Authentication and method

I first computed the SHA-256 of `V2_FROZEN.sha256`. It was exactly

```text
fb8e508c100bc81cf1105ba7be09162df7d73eb7a5ef704b3a687b3567b1a372
```

I then verified every entry in that authenticated ledger. All six entries
passed before I read the claims:

```text
a9bd86b4e4515f133c3c2d7711c530d334749675e0aa75eb8bc7547f3ad0f0da  V2_STATEMENT.md
9c0ec169e6402114a0546fca5506985ff6cec6250f7f5cc73081aa946063623f  V2_PROOF.md
ac564d1bc1f8dc1f12584c38ddbf8c1b2e8ef676cab54f4ce42fe51990bdc812  V2_PROVENANCE.md
3826990dda888a5c3f681e40b0cd60a520adaec5c8a79929e8083246ad920ac2  V2_MANIFEST.md
6c3cebe4f34bdb439dabb9cc50990bb68d0250ae552ea5087dd4e57dc057aa9d  FROZEN.sha256
a839f1bd62ca2671882c6dba0270de9f901aad9f0d52e2de888f38ca196743a2  HOSTILE_AUDIT.md
```

The imported V1 root therefore remains pinned at
`6c3cebe4f34bdb439dabb9cc50990bb68d0250ae552ea5087dd4e57dc057aa9d`.
I also verified every entry inside that V1 ledger. The imported hostile audit
remains pinned at
`a839f1bd62ca2671882c6dba0270de9f901aad9f0d52e2de888f38ca196743a2`,
and its literal verdict remains `FAIL`.

I used no remote work and no numerical search. I made no substantive
computation. I did not modify a frozen byte or a ledger.

## Canonical construction repair

Construction (8) now requires

\[
 1\le d<N,\qquad \gcd(d,N)=1,
\]

and retains a unit label `y`. Thus `d^{-1}` exists modulo `N`, and

\[
 T_y(d)=[y^2d^{-1}]_N
\]

is a unit in the exact integer range `1<=T_y(d)<N`. Both factors are
positive and at most `N-1`. Hence

\[
 1\le dT_y(d)\le (N-1)^2<N^2.
\]

The root calculation is unchanged and valid:

\[
 dT_y(d)\equiv d(y^2d^{-1})\equiv y^2\pmod N.
\]

This excludes the V1 counterexample `N=3`, `d=10`, `y=1` because `d=10`
is not canonical. The repair is sufficient for the claimed uniform row
bound.

## General graph-carrier separation

The new bound is attached only to the one-edge constructor (8). The general
graph setup still permits every vertex carrier `d_v` to be an arbitrary
positive unit. Its exact edge row is still `A_e=d_ud_v`. Such a row can
exceed `N^2`, but neither graph theorem claims otherwise.

For an Eulerian edge set `C`, direct endpoint counting gives

\[
 \prod_{e\in C}A_e
 =\prod_v d_v^{\deg_C(v)}
 =\left(\prod_vd_v^{\deg_C(v)/2}\right)^2.
\]

This calculation uses positivity, unit status, and even degree. It uses no
carrier-size hypothesis. V2 therefore does not silently restrict Theorem B
or the general graph carrier space.

## Exact monomial pullback and root compatibility

For a transformed relation, write

\[
 z_i=\sum_jc_jM_{ji}=2h_i+d_i,
 \qquad d_i\in\{0,1\}.
\]

Then the exact product is

\[
 \prod_jA_j^{c_j}
 =\left(Q\prod_i a_i^{h_i}\right)^2\prod_i a_i^{d_i}.
\]

If the left side is an integer square, the last positive integer is a
rational square and therefore an integer square. This proves that
`d=M^Tc` lies in the old exact square-class kernel. Taking positive integer
roots and dividing by the inherited modular root gives exactly

\[
 R_c\left(\prod_jX_j^{c_j}\right)^{-1}
 \equiv \left(\prod_j\varepsilon_j^{c_j}\right)\rho_a(d)
 \pmod N.
\]

All divisions are valid. The old rows are units. Since each
`A_j=s_j^2\prod_i a_i^{M_{ji}}` is a unit, each `s_j` is also a unit. Zero
exponents, repeated values, and empty supports do not change the argument.
The positive-root convention fixes the integer sign.

When `M^Tc=0`, the old product and root are both one, so the new normalized
root is a global sign. When `M^Tc` is nonzero, the relation can retain an old
useful root. The theorem does not misclassify that branch as structural.

For an arbitrary supplied row root `X_j`, let `Z_j` be its inherited root.
The ratio `eta_j=X_jZ_j^{-1}` satisfies `eta_j^2=1 mod N`. Multiplication by
the unit `Z_j` preserves both signed gcds. Because `N` is odd, a non-global
involution splits the prime-power divisors of `N` between `eta_j-1` and
`eta_j+1`, so a signed gcd is proper. If no proper gcd occurs, `eta_j` is
exactly `+1` or `-1 mod N`. The proof therefore screens compatibility; it
does not assume it.

## Even-cycle signs and gcd identities

On a simple even cycle, the even and odd edge sets are the two perfect
matchings. Each matching product is exactly

\[
 R=\prod_i d_{v_i}.
\]

Consequently

\[
 R\equiv P_0^2\equiv P_1^2\pmod N,
 \qquad X=P_0P_1.
\]

Since both alternating products are units,

\[
 RX^{-1}\equiv P_0P_1^{-1}\equiv P_1P_0^{-1}\pmod N.
\]

The second equality has the correct sign and direction: the first ratio
squares to one, so it equals its inverse. Also,

\[
 R-X\equiv P_0(P_0-P_1)\pmod N,
 \qquad
 R+X\equiv P_0(P_0+P_1)\pmod N.
\]

Unit multiplication and replacement by a congruent integer preserve the
gcd with `N`. Thus both claimed exact gcd equalities follow. Changing the
cycle start, orientation, or parity convention only swaps `P_0,P_1` or
negates a difference. It does not change the two gcd tests. The proof uses
the two perfect matchings and correctly makes no label-only claim for odd
cycles.

## Reduced complements and F270

The unreduced product

\[
 P_E(a)=U_E(a)U_E(N-a)
\]

is an exact monomial in two operand rows, with their inherited product root.
Theorem A applies to relations made by that exact operation.

The reduced row instead satisfies only

\[
 C_E(a)=[P_E(a)]_{N^2},
 \qquad P_E(a)=C_E(a)+\lambda N^2,
 \qquad \lambda\ge0.
\]

For `lambda>0`, the additive reduction does not preserve operand prime
incidence. Theorem A therefore gives no general rank, pivot, or root-image
conclusion for that construction. This is an operation-level boundary. It
does not exclude an accidental numerical equality or relation involving a
reduced row.

The inspected F270-D03 grammar imports the original canonical scalar rows
`U_E(b)` and rebuilds one block system from their cross-family union. It does
not generate `C_E(a)` by reduced complement multiplication. Cross-family
prime sharing can remove private pivots and create a relation even when each
separate bank has full rank. Such a relation is not forced into the
structural kernel of an inherited monomial map. F275 therefore proves no
success or failure result for F270, as stated.

## Scope conclusion

V2 repairs only construction (8). It does not impose canonical size on the
general graph carriers. It does not extend the even-cycle formula to odd
cycles. It proves no carrier-kernel classification, canonical-section lower
bound, probability law, runtime law, F270 disposition, or factoring
algorithm. The frozen V2 claims pass within these boundaries.
