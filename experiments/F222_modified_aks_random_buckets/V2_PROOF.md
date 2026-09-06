# Proof of F222 V2

## 1. Frobenius reduction

Put

\[
h_{m,a}(X)=(X+a)^m-X^m-a^m.
\]

In characteristic `p` and `q`, respectively,

\[
E_a=h_{q,a}^p\pmod p,
\qquad
E_a=h_{p,a}^q\pmod q.
\tag{1}
\]

Because `gcd(r,pq)=1`, either Frobenius power permutes the `r` cyclic
coefficient positions.  It is therefore enough to study `h_(q,a)` modulo
`p` and `h_(p,a)` modulo `q`.

## 2. Every `p`-local cyclic coefficient is a nonzero degree-`d` polynomial

In characteristic `p`, use `q=p+d` and Frobenius to get

\[
h_{q,a}(X)
=X^p\bigl((X+a)^d-X^d\bigr)
+a\bigl((X+a)^d-a^d\bigr).
\tag{2}
\]

Expanding by powers of `a` gives

\[
h_{q,a}(X)=
\sum_{e=1}^d a^e
\left[
\binom de X^{q-e}
+\binom d{e-1}X^{d-e+1}
\right].
\tag{3}
\]

All displayed binomial coefficients are nonzero modulo `p` because `d<p`.
The two exponents paired at a fixed `e` differ by `p-1`.

If `p` is not `1 mod r`, the two terms at one `a`-degree enter distinct
cyclic positions.  Distinct values of `e` have distinct `a`-degrees, so
they cannot cancel as polynomials.  Since `d>r`, the first family of `d`
consecutive exponents visits every cyclic position.

If `p` is `1 mod r`, the paired terms enter the same cyclic position and
their coefficient is

\[
\binom de+\binom d{e-1}=\binom{d+1}e.
\tag{4}
\]

This is nonzero modulo `p` because `d+1<p`.  Again, `d>r` visits every
position.  Thus every cyclic coefficient is a nonzero polynomial in `a` of
degree at most `d`.

Each has at most `d` roots in `F_p`.  A union bound over all `r` positions
proves (S2).  The final Frobenius permutation in (1) does not change it.

## 3. Clearing the `q`-local negative power

First note directly that every cyclic coefficient of `h_(p,a)` modulo `q`
is nonzero as a polynomial.  Before cyclic reduction,

\[
h_{p,a}(X)=
\sum_{j=1}^{p-1}\binom pj a^{p-j}X^j.
\tag{5}
\]

No `binom(p,j)` vanishes modulo the larger prime `q`.  Within one cyclic
position, different `j` give different powers of `a`, so there is no
polynomial cancellation.  Since `p-1>r`, the range `1<=j<=p-1` visits every
position.  Denote these nonzero coefficient polynomials by `v_k(a)`.  They
have degree at most `p-1=q-d-1`.

Work in

\[
R_q=\mathbb F_q[X]/(X^r-1).
\]

For a unit shift, `(X+a)^q=X^q+a` and `p=q-d`.  Multiplying the definition of
`h_(p,a)` by `a^(d-1)(X+a)^d` gives

\[
a^{d-1}(X+a)^dh_{p,a}=K_a,
\tag{6}
\]

where

\[
K_a=
a^{d-1}(X^q+a)
-a^{d-1}X^p(X+a)^d
-(X+a)^d.
\tag{7}
\]

The last term uses

\[
a^{d-1}a^p=a^{q-1}=1.
\]

Define

\[
J_a=X^{r-1}-aX^{r-2}+\cdots+(-a)^{r-1},
\qquad
D(a)=1-(-a)^r.
\tag{8}
\]

Then in `R_q`,

\[
(X+a)J_a=D(a).
\tag{9}
\]

When `D(a)` is nonzero, equations (6)--(9) give

\[
a^{d-1}D(a)^dh_{p,a}=K_aJ_a^d.
\tag{10}
\]

The degree in `a` of `K_a` is at most `2d-1`, while that of `J_a^d` is at
most `d(r-1)`.  Therefore every cyclic coefficient `W_k(a)` on the right of
(10) has degree at most

\[
d(r+1)-1.
\tag{11}
\]

It remains to prove that no `W_k` is the zero polynomial.  If one were zero,
then (10) would force `v_k(a)=0` for every unit `a` with `D(a)!=0`.  The
polynomial `D` has at most `r` roots, so this would give at least `q-1-r`
roots of `v_k`.  But

\[
q-1-r>q-d-1=p-1
\tag{12}
\]

because `d>r`, contradicting the degree bound and nonvanishing proved after
(5).  Thus every `W_k` is nonzero.

For a unit `a`, some `v_k(a)` can vanish only if `D(a)=0` or some
`W_k(a)=0`.  There are at most `r` common exceptional roots of `D` and at
most `d(r+1)-1` roots for each of the `r` polynomials `W_k`.  Hence the total
number of unit shifts with any zero local coefficient is at most

\[
r+r\bigl(d(r+1)-1\bigr)=rd(r+1).
\tag{13}
\]

This proves (S3), again unchanged by the final Frobenius permutation.

## 4. Proper coefficient gcds

A uniform unit modulo `N` has independent uniform reductions in
`F_p^times` and `F_q^times`.  A global coefficient has a proper gcd with
`N` only if it is zero in at least one local field.  The union of the two
events bounded in (S2)--(S3) therefore proves (S4).  This implication can be
strict because a coefficient zero in both fields has gcd `N`, not a factor.

## 5. Sharpening the local-nullity premise

For an `r`th root `xi` in an algebraic closure of `F_p`, equation (2) gives
`h_(q,a)(xi)` as a degree-at-most-`d` polynomial in `a`.  Its coefficients
at `a^d` and `a` are

\[
\xi(\xi^{p-1}+d),
\qquad
\xi^d(d\xi^{p-1}+1).
\tag{14}
\]

If both vanished, then `d^2=1 mod p`.  The gap `d` is even and (S1) gives
`2<=d<=p-2`.  The only solutions to `x^2=1` in `F_p` are `1` and `p-1`, so
this is impossible.  Every root `xi` therefore accepts at most `d` local
shifts.  A union bound over the `r` distinct roots gives

\[
\Pr(\nu_p(a,r)>0)\le {rd\over p-1}.
\tag{15}
\]

The original F222 denominator-clearing argument modulo `q` gives a nonzero
polynomial of degree `2d-1` for every `xi`, plus at most one excluded shift.
Thus

\[
\Pr(\nu_q(a,r)>0)\le {2rd\over q-1}.
\tag{16}
\]

Equations (15)--(16) prove (S5).  The resultant is zero modulo a hidden
prime exactly when the corresponding local polynomials share a root, so a
proper resultant gcd is contained in this union.  Adding (S4) and (S5)
gives (S6).

## 6. Constructing the intermediate-gap family

Baker--Harman--Pintz, *The Difference Between Consecutive Primes, II*,
Proceedings of the London Mathematical Society 83 (2001), Theorem 1,
proves that for every sufficiently large real `x`, the interval

\[
[x-x^{0.525},x]
\]

contains a prime.  Its DOI is `10.1112/plms/83.3.532`.

Let `p` run through unbounded odd primes and set

\[
x_p=p+\lfloor p^{3/5}\rfloor.
\]

For sufficiently large `p`, the lower endpoint satisfies

\[
x_p-x_p^{0.525}>p.
\tag{17}
\]

Choose a prime `q` in the guaranteed interval.  Then

\[
p^{3/5}-O(p^{0.525})\le q-p\le p^{3/5},
\tag{18}
\]

so `d=Theta(p^(3/5))`.  Also `p<q<2p` and `d<p-1` for all sufficiently
large `p`.  This gives infinitely many balanced semiprimes satisfying (S1)
for every numerical-QP `r` once `n` is large.

## 7. Adaptive fresh-shift bank

Condition on the complete transcript before trial `i`.  Its chosen `r_i` is
then fixed, and the next local shifts are independent and uniform.  Equation
(S6) applies conditionally.  A conditional union bound over all trials gives
(S9).

On the family in Section 6,

\[
p=2^{n/2+O(1)},
\qquad
{d\over p}=p^{-2/5+o(1)}=2^{-n/5+o(n)}.
\tag{19}
\]

A numerical-QP trial count and numerical-QP moduli make the remaining sum
`2^{o(n)}`.  Multiplying by (19) proves (S8).

