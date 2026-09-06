# F267 proof — F263 shifted-boundary collapse

## 1. Balanced geometry

Since `q>p`, one has `sqrt(N)>p`, hence `B>=p` and `s>=0`. Also
`q<2p` gives

\[
 B\le\sqrt{pq}<\sqrt2p<2p.
\]

Thus `H<p` and `s=B-p<B/2`.
For even `B`, the integer inequality `s<B/2` directly gives `s<H`.
For odd `B`, it first gives `s<=H`. Equality would imply
`B=2p-1`, but

\[
 (2p-1)^2-2p^2=2(p-1)^2-1>0
\]

for the odd prime `p>=3`, contradicting `B<sqrt(2)p`. Hence `s<H`
in both parities. Finally `B<sqrt(N)<q`. This proves (1). If `s=0`,
then `B=p` and `gcd(B,N)=p`.

On the unresolved branch `s>=1`. Because `s<H=floor(B/2)`, one also has

\[
 p=B-s\ge s+2.
\tag{1.1}
\]

In particular, `s` and `s+1` are nonzero modulo `p`.

## 2. Product-jet formulas

For any integer `x`, expand

\[
 R_L(x+X)=\prod_{j=0}^{L-1}(x+j+X).
\]

Taylor's formula for a polynomial gives its first three coefficients as

\[
 R_L(x),\qquad R_L'(x),\qquad {R_L''(x)\over2}.
\]

The last quotient is an integer because it is the coefficient of `X^2` in
an integer polynomial. Taking `x=a` for the `u` factors and `x=a-B` for
the `v` factors proves (3), and the `2 x 2` determinant proves (4).

## 3. Transfer formulas over the integers

Put

\[
 A_i=a+i,\qquad C_i=a-B+i=A_i-B.
\]

The upper-right entry of the forward unit-weight product is

\[
 F_0=\sum_{i=0}^{L-1}
 \left(\prod_{j<i}A_j\right)
 \left(\prod_{j>i}C_j\right).
\tag{3.1}
\]

Replacing the `C_i` by `A_i` one at a time telescopes, so

\[
 R_L(a)-R_L(a-B)=\sum_i(A_i-C_i)
 \left(\prod_{j<i}A_j\right)
 \left(\prod_{j>i}C_j\right)=BF_0.
\]

Replacing them in the opposite order gives the same formula for the
reverse entry `G_0`. This proves (5) without division.

For forward weights `1` and `c+1`, their difference is `c`. Hence

\[
 F_1-F_0=\sum_{i=0}^{L-1}Q_i,
 \qquad
 Q_i=\left(\prod_{j\le i}A_j\right)
     \left(\prod_{j>i}C_j\right).
\tag{3.2}
\]

Set `Q_{-1}=R_L(a-B)`. Since `C_i=A_i-B`,

\[
 (B+1)Q_i=(A_i+1)Q_i-A_iQ_{i-1}.
\]

Summing this identity telescopes to

\[
 (B+1)(F_1-F_0)=(a+L)R_L(a)-aR_L(a-B).
\tag{3.3}
\]

Both forward transfer matrices have upper-left entry `R_L(a)`. Their
two-row determinant is therefore `D_01=R_L(a)(F_1-F_0)`. Multiplying
(3.3) by `R_L(a)` proves (6).

## 4. Left-edge boundary zeros

The rising factorial has the reflection identity

\[
 R_L(1-L-X)=(-1)^L R_L(X).
\tag{4.1}
\]

Since `L` is even,

\[
 R_L(-L)=R_L(1)=L!,\qquad
 R_L''(-L)=R_L''(1).
\tag{4.2}
\]

Take the left-edge block `a=1`.

If `s=L+1`, then `B=p+s` gives

\[
 a-B\equiv1-s=-L\pmod p.
\]

Equations (4), (4.2) make `jet_det02` zero modulo `p`. Equations (5) and
(4.2) give `BF_0=BG_0=0` modulo `p`. Here `B` is a unit modulo `p`
because `B\equiv s` and `0<s<p`; therefore `F_0=G_0=0` modulo `p`.

If `s=L+2`, then

\[
 a-B\equiv-L-1\pmod p,
\]

and, because `L` is even,

\[
 R_L(-L-1)=(L+1)!,\qquad R_L(1)=L!.
\]

The parenthesis on the right of (6) is thus

\[
 (L+1)L!-(L+1)!=0\pmod p.
\]

By (1.1), `B+1\equiv s+1` is nonzero modulo `p`. Hence
`D_01=0` modulo `p`.

In the first case the support is `1,...,L` and `s=L+1`; in the second it
is the same support and `s=L+2`. Both are strictly non-direct.

## 5. Right-edge `u1` boundary zeros

Take `a=H-L`. Suppose first that `s=L+1`. Since `p` and `s` are odd,
`B=p+s` is even, so `B=2H`. Therefore

\[
 p=B-s=2H-L-1.
\tag{5.1}
\]

If instead `s=L+2`, then `s` is even, `B` is odd, and `B=2H+1`. Again

\[
 p=B-s=2H-L-1.
\tag{5.2}
\]

For the `L` factors `t_j=a+j`, pair `j` with `L-1-j`. Equations
(5.1)--(5.2) give

\[
 t_j+t_{L-1-j}=2a+L-1=p.
\]

Modulo `p`, the polynomial

\[
 \prod_{j=0}^{L-1}(X+t_j)
\]

is therefore a product of `L/2` even quadratics
`(X+t_j)(X-t_j)`. Its coefficient of `X` is zero. By (3), this
coefficient is `u1=R_L'(a)`. Thus `p` divides `shifted.u1` in both
boundary cases.

Condition (7) is exactly the condition that the singular index lies to the
left of this support. It affects the non-direct label, not the congruence.

## 6. Near-square rigidity

Write `d=q-p`, which is a positive even integer. Since `B=p+s`, the lower
floor-square inequality is

\[
 B^2\le pq
 \quad\Longleftrightarrow\quad
 p(d-2s)\ge s^2.
\tag{6.1}
\]

If `s^2<p`, then (6.1), positivity of `d`, and parity give

\[
 d\ge2s+2.
\tag{6.2}
\]

The upper floor-square inequality is

\[
 pq<(B+1)^2
 \quad\Longleftrightarrow\quad
 p(d-2s-2)<(s+1)^2.
\tag{6.3}
\]

The integer inequality `s^2<p` gives `p>=s^2+1`, and hence

\[
 2p\ge2s^2+2\ge(s+1)^2.
\tag{6.4}
\]

If `d>=2s+4`, then the left side of (6.3) is at least `2p`, contrary to
(6.3)--(6.4). Therefore `d<=2s+2`, which together with (6.2) proves

\[
 d=2s+2.
\]

It follows that

\[
 {p+q\over2}=p+s+1=B+1.
\]

Since distinct primes make `N` nonsquare, `ceil(sqrt(N))=B+1`. Direct
expansion now gives

\[
 (B+1)^2-N=(s+1)^2,
\]

and the first Fermat trial returns (10).

## 7. Right-edge `v1` boundary zeros

Retain `a=H-L` and `s^2<p`, so Section 6 gives
`q=p+2(s+1)`.

If `s=L-1`, then `B` is even and `B=2H`. Thus

\[
 p=2H-L+1,\qquad q=2H+L+1.
\]

If `s=L`, then `B` is odd and `B=2H+1`. Thus

\[
 p=2H+1-L,\qquad q=2H+L+3.
\]

For `t_j=a-B+j`, pair `j` with `L-1-j`. In the two cases respectively,

\[
 t_j+t_{L-1-j}
 =2H-2B-L-1=-q.
\]

Modulo `q`, the polynomial `\prod_j(X+t_j)` is again a product of even
quadratics. Its linear coefficient is zero. Equation (3) identifies that
coefficient with `v1=R_L'(a-B)`, proving the two `v1` rows.

As in Section 5, (7) makes the support non-direct. The congruence also
holds if the equation `q=p+2(s+1)` is assumed directly instead of derived
from `s^2<p`.

## 8. Collapse of the finite F263 pattern

The F263 result audit authenticates the six complete `s` sets reproduced
in the statement. Substitution shows that each set is exactly one of the
four boundary mechanisms above at a registered left- or right-edge
power-of-two block. The held-out factors satisfy

\[
 s\le95,\qquad p\ge551426102609,
\]

so `s^2<p` holds on every consecutive-prime row. Section 6 proves the
reported identity `B+1=(p+q)/2` without using the cohort generator's
consecutive-prime label.

For a hypothetical modulus outside the frozen data, the same mechanism is
still not a new conditional source. Its boundary hypothesis makes
`s` one of four public offsets from `L`, so `p=B-s` is directly testable.
When `s^2<p`, the stronger one-Fermat-trial collapse applies. When
`s^2>=p`, the direct public descriptor remains. No distributional or
asymptotic claim is needed.
