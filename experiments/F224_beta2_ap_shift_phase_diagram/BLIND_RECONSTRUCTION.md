# F224 blind reconstruction

## Authentication and verdict

**STATEMENT SHA-256:** `cd9ac0c208c7d62a1c486fd94f63cdd6851dd924a85bf4fa42527f0c36b9f745`

**Verdict: PASS.** The AP-Fermat count, the AP pullback and maximum-atom
bound, the phase theorem, and the certificate for `N=187` all reconstruct
from the statement. No experimental output is used.

## 1. AP-Fermat scan

Because `p` is a unit modulo `L`, so is `s`. Hence

\[
u\equiv Ns^{-1}\equiv pqs^{-1}\equiv q\pmod L.
\]

Let `g=gcd(2,L)` and `m=L/g`. The congruence

\[
2A\equiv s+u\pmod L
\]

is soluble because `s+u` is congruent to the even integer `p+q`; after
division by `g`, its coefficient is invertible modulo `m`. It therefore
defines exactly one computable class modulo `m`. The integer

\[
A_*=(p+q)/2
\]

belongs to this class.

Let `A_0` be its first member not below `sqrt(N)`. Then
`A_*=A_0+km` for some nonnegative integer `k`. Moreover,

\[
\begin{aligned}
A_*-\sqrt N
 &=\frac{p+q-2\sqrt{pq}}2\\
 &=\frac{(q-p)^2}{2(\sqrt p+\sqrt q)^2}
 <\frac{d^2}{8p}.
\end{aligned}
\]

The number of tested values, including `A_*`, is consequently

\[
k+1\le 1+\frac{A_*-\sqrt N}{m}
 <1+\frac{g d^2}{8pL}
 \le 1+\frac{d^2}{4pL}.
\]

At `A_*`,

\[
A_*^2-N=(d/2)^2,
\]

so the scan returns `A_*-d/2=p` and `A_*+d/2=q`. Any earlier square
also gives an exact integer decomposition `(A-B)(A+B)=N`; exact
multiplication and the inequalities `1<A-B<A+B<N` verify a returned
factor.

All scanned integers have `O(n)` bits. Modular inversion, integer square
roots, squaring, square testing, and verification have polynomial bit
cost. Thus `d^2/(pL)=QP(n)` gives a deterministic numerical-QP terminal.
For balanced inputs, `N^(1/4)=Theta(p^(1/2))`. The AP terminal asks only
for `L` on the scale `d^2/p`, whereas the quoted gap-independent scale
asks for `L` on the scale `p^(1/2)`. The first is strictly smaller when
`d=o(p^(3/4))`, so the claimed strict separation of thresholds is real.

## 2. Local pullbacks

For a prime `ell` not dividing `r`, put

\[
R_\ell=\mathbb F_\ell[X]/(X^r-1).
\]

The Frobenius map is an automorphism of this ring: it permutes the `r`
coordinates because multiplication by `ell` permutes the residue classes
modulo `r`. Define

\[
D_{e,\ell,x}=(X+x)^e-X^e-x^e\in R_\ell.
\]

Then

\[
E_x\bmod p=D_{q,p,x}^{,p},\qquad
E_x\bmod q=D_{p,q,x}^{,q}.
\]

Thus Frobenius only permutes the raw coefficients. It also preserves the
degree of the gcd with `X^r-1`, hence preserves local nullity.

### 2.1 Raw coefficients over `F_p`

Since `q=p+d`, Frobenius in characteristic `p` gives

\[
\begin{aligned}
D_{q,p,x}
={}&(X^p+x)(X+x)^d-X^{p+d}-x^{d+1}\\
={}&\sum_{k=0}^{d-1}{d\choose k}X^{p+k}x^{d-k}
 +\sum_{k=1}^{d}{d\choose k}X^kx^{d-k+1}.
\end{aligned}
\]

Every cyclic coordinate is a polynomial in `x` of degree at most `d`.
Every coordinate is nonzero. Indeed, `d>r` makes the residues of the
first sum cover every coordinate. Terms of the same `x` degree can meet
only in the displayed adjacent pair; if their `X` residues also meet,
their coefficient is

\[
{d\choose k}+{d\choose k+1}={d+1\choose k+1}\not\equiv0\pmod p,
\]

because `d+1<p`. Each of the `r` coordinates therefore has at most `d`
roots. The union of raw-coefficient exceptional residues over `F_p` has
size at most `rd`.

### 2.2 Raw coefficients over `F_q`

Write `P=X` in `R_q` and let `T_x=P+x`, the multiplication operator by
`X+x`. For a nonzero `x`, define

\[
C_x=x^{d-1}T_x^dD_{p,q,x}.
\]

Since `p=q-d`, `T_x^q=P^q+x`, and `x^{p+d-1}=x^{q-1}=1`, this has the
low-degree form

\[
C_x=x^{d-1}(P^q+x-P^pT_x^d)-T_x^d.
\]

Its coordinates have degree at most `2d-1`. Put

\[
A_x=\sum_{h=0}^{r-1}(-1)^h x^{r-1-h}P^h,
\qquad
\Delta_x=x^r-(-1)^r.
\]

Then `A_xT_x=Delta_x`. For `Delta_x != 0`, a coordinate of
`D_{p,q,x}` vanishes exactly when the corresponding coordinate of

\[
U_x=A_x^dC_x

=A_x^d(x^{d-1}P^q+x^d)
-\Delta_x^d(x^{d-1}P^p+1)
\]

vanishes. Every coordinate of `U_x` has degree at most

\[
d(r-1)+(2d-1)=d(r+1)-1.
\]

For completeness, none of these coordinate polynomials is zero. If
`0<=j<r`, the highest-degree term in the `P^j` coordinate of `A_x^d` is

\[
(-1)^j{d+j-1\choose j}x^{d(r-1)-j}.
\]

These coefficients are nonzero modulo `q`, since their upper indices are
less than `q`. In the `j=p mod r` coordinate, the term
`-Delta_x^d x^(d-1)P^p` has a unique highest degree. For
`j` different from `0` and `p mod r`, the two possible leading terms
have different degrees unless `q=1 mod r`; in that exceptional alignment
their sum has nonzero coefficient

\[
(-1)^j{d+j-2\choose j}.
\]

In coordinate zero, the leading terms of `x^dA_x^d` and `-Delta_x^d`
cancel. A unique next term remains unless `q=1 mod r`; in that alignment
the tied coefficient is

\[
(-1)^r{d+r-2\choose r}\ne0\pmod q.
\]

This proves the required nonvanishing in all cases.

There are at most `r` singular values satisfying `Delta_x=0`. Away from
them, a union bound over the `r` nonzero coordinate polynomials gives at
most `r(d(r+1)-1)` exceptional residues. Including the singular values
gives

\[
r(d(r+1)-1)+r=rd(r+1)
\]

raw-coefficient exceptional residues over `F_q`.

### 2.3 Resultant and local-nullity residues

Over `F_p`, fix an `r`th root of unity `zeta`. After putting
`z=x/zeta` and `a=zeta^(p-1)`, the value of `D_{q,p,x}`, divided by the
nonzero factor `zeta^(d+1)`, is

\[
a((1+z)^d-1)+z(1+z)^d-z^{d+1}.
\]

This has degree at most `d` and is not the zero polynomial. If it were
zero, its coefficients of `z` and `z^d` would give

\[
ad+1=0,\qquad a+d=0,
\]

and hence `d^2=1 mod p`, impossible for `2<d<p-1`. Each of the `r`
roots of unity therefore contributes at most `d` exceptional `x`
values. The local-nullity exceptional set over `F_p` has size at most
`rd`.

Over `F_q`, when `zeta+x != 0`, local vanishing of `D_{p,q,x}` is
equivalent to vanishing of `C_x(zeta)`. This is a nonzero polynomial in
`x` of degree `2d-1`: its leading coefficient is `-zeta^p`. Thus the
`r` roots of unity contribute at most `r(2d-1)` values. The singular
values `x=-zeta` have union of size at most `r`. Hence the corresponding
bound over `F_q` is

\[
r(2d-1)+r=2rd.
\]

Since `X^r-1` is squarefree in both characteristics, a resultant is zero
modulo a local prime exactly when the associated local nullity is
positive. Thus these two bounds cover every resultant/local-nullity
activation.

## 3. Pullback to the integer cell and the maximum-atom bound

The width of `I_N` is less than

\[
\sqrt N-\sqrt{N/2}< (\sqrt2-1)p<p.
\]

Therefore reduction of its integers modulo `p` is injective; reduction
modulo `q` is injective as well. Also `x<q`, and the only multiple of a
factor in the interval is the target `x=p`.

The number of off-target integers that can activate a channel is at most

\[
\underbrace{rd}_{p\text{ raw}}
+\underbrace{rd(r+1)}_{q\text{ raw}}
+\underbrace{rd}_{p\text{ nullity}}
+\underbrace{2rd}_{q\text{ nullity}}
=rd(r+5).
\]

Restricting to the AP cell can only decrease this count. If every atom of
a law `mu` has mass at most `eta`, the union of these off-target values
and the one exact target has probability at most

\[
(1+rd(r+5))\eta.
\]

For the uniform law, `eta=1/H`, which gives the stated exact bound. The
same argument is pointwise in all previously exposed history. It
therefore applies conditionally whenever the stage's `r` and law are
fixed before the fresh draw; summing the conditional bounds proves the
adaptive-bank claim.

## 4. Phase theorem

Let the Fermat cap be `B(n)`, with numerical-QP size. If the AP scan does
not reach `A_*`, its actual number of tests exceeds `B(n)`. The bound in
Section 1 then gives, for sufficiently large inputs and up to an absolute
constant,

\[
L<\frac{d^2}{pB(n)}.
\]

The length of the balanced interval `I_N` is `Theta(p)`. On this failure
branch the last inequality also makes `p/L` tend to infinity, so standard
AP counting gives

\[
H=\Theta(p/L).
\]

For one uniform stage, Section 3 gives probability `O(d r^2/H)`. A
numerical-QP number of trials with numerical-QP choices of `r` therefore
has total probability

\[
QP(n)\frac{dL}{p}.
\]

This remains valid for adaptive stages by the conditional bound already
proved. On inserting the consequence of Fermat failure and absorbing all
numerical-QP factors,

\[
\Pr(\text{any bank success})
\le QP(n)\frac{d^3}{p^2}.
\]

If `d<=p^(2/3-epsilon)`, then

\[
\frac{d^3}{p^2}\le p^{-3\epsilon}.
\]

Balancedness gives `log p=Theta(n)`, whereas a numerical-QP factor has
logarithm only `poly(log n)`. Consequently

\[
QP(n)p^{-3\epsilon}=2^{-\Omega(n)}.
\]

Thus either the AP-Fermat terminal succeeds within its cap, or the full
modified-AKS bank has exponentially small success probability.

For `d=Theta(p^(3/5))`, take `epsilon=1/15`; then
`2/3-epsilon=3/5` and

\[
d^3/p^2=Theta(p^{-1/5}),
\]

which reconstructs the stated specialization. Independently of the
bibliographic attribution to P193, existence of infinitely many such
prime pairs follows, for example, from the standard prime-in-short-
interval theorem with exponent `0.525`: for a large prime `p`, apply it
at `y=p+p^(3/5)` to obtain a prime
`q in [y-y^0.525,y]`, so `q-p=Theta(p^(3/5))` and `q<2p`.

## 5. Exact certificate for `N=187`

Here

\[
\left\lceil\sqrt{187/2}\right\rceil=10,
\qquad \left\lfloor\sqrt{187}\right\rfloor=13,
\]

so `I_N={10,11,12,13}` and its odd cell is `{11,13}`. The first point is
the exact factor. At `x=13`, the listed coefficient pairs use the order
`(constant, X)`. Their root evaluations are

\[
(9+3,9-3)=(1,6)\pmod {11},
\]

and

\[
(4+1,4-1)=(5,3)\pmod {17}.
\]

Each of the two raw coefficients is nonzero modulo both local primes, so
every raw coefficient gcd with `187` is `1`. Since the characteristics
are odd, `X^2-1` has the two distinct roots `1` and `-1`; both evaluations
are nonzero over each local field. Both local nullities are therefore
zero. The resultant is, up to a unit, the product of the two evaluations,
which is nonzero modulo both `11` and `17`; its gcd with `187` is `1`.
Thus `13` is not useful in either channel, and the AP cell contains no
off-target useful shift.
