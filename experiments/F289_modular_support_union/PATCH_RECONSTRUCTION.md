# Independent reconstruction of the patch claims

The only research input used here is `PATCH_STATEMENT_ONLY.md`, whose checked
SHA256 is
`89487b6b7d852efa9c43b7f6dfd3ae6915e37a24683d0e5583edc9875cd395e3`.

All congruences below are modulo \(M=2^k\), except in the explicitly stated
\(M=1\) case of Claim 3. Division by an odd integer means multiplication by
its inverse modulo \(M\).

## 1. The affine cover

The claim is true for every stated \(k\geq 1\).

First observe the following affine inverse identity. For every integer \(a\),

\[
 \begin{aligned}
 &u^{-1}+a\bigl((u+s)^{-1}-u^{-1}\bigr)-(u+as)^{-1}\\
 &\qquad={-a(a-1)s^2\over u(u+s)(u+as)}.
 \end{aligned}
\]

All three factors in the denominator are odd. Also, \(a(a-1)\) is even.
Thus the numerator on the right is divisible by \(2^{2h+1}\). The definition
\(h=\max(1,\lfloor k/2\rfloor)\) gives

\[
 k\leq 2h+1.
\]

Indeed, for \(k=1\) this is immediate; for even \(k\geq2\), the right side is
\(k+1\); and for odd \(k\geq3\), it is \(k\). Consequently,

\[
 (u+as)^{-1}\equiv
 u^{-1}+a\bigl((u+s)^{-1}-u^{-1}\bigr) \pmod M.       \tag{1}
\]

Multiplication by \(N\) turns (1) into

\[
 N(u+as)^{-1}\equiv v+a\delta\pmod M.                 \tag{2}
\]

Now take \((x,y)\in S\). Since \(xy\equiv N\pmod M\), and \(N\) is odd,
both \(x\) and \(y\) are odd. There is therefore a unique odd representative
\(u\in[1,s)\) of \(x\bmod s\), and a unique integer \(a\) such that
\(x=u+as\). The odd integer \(x\) is invertible modulo \(M\), so

\[
 y\equiv Nx^{-1}\equiv v+a\delta\pmod M
\]

by (2). Hence \(y=v+a\delta+bM\) for some integer \(b\), and the point lies
in the translate indexed by \(u\).

Conversely, a point in that translate has
\(x=u+as\) and \(y\equiv v+a\delta\pmod M\). Equation (2) then gives
\(xy\equiv N\pmod M\). Intersecting with the three stated inequalities gives
exactly the corresponding part of \(S\).

The union is disjoint because its index \(u\) is the unique representative
of \(x\bmod s\) in the specified range. Since \(s=2^h\), there are exactly
\(s/2=2^{h-1}\) odd representatives in \([1,s)\). The two columns

\[
 \begin{pmatrix}s\\ \delta\end{pmatrix},\qquad
 \begin{pmatrix}0\\ M\end{pmatrix}
\]

have determinant \(sM\), independently of the value of \(\delta\).

There are no exceptional small moduli. The cases for which \(h=1\) are:

* \(M=2\): there is only \(u=1\), with \(v=1\) and \(\delta=0\). The
  translate consists of the odd coordinate pairs before the inequalities are
  imposed.
* \(M=4\): again \(u=1\), with \(v\equiv N\) and
  \(\delta\equiv2N\equiv2\pmod4\).
* \(M=8\): again \(u=1\), with \(v\equiv N\) and
  \(\delta\equiv2N\pmod8\). Thus
  \(y\equiv N+2Na\pmod8\), as required for \(x=1+2a\).

These are also covered by the divisibility argument above. Claim 1 does not
state an \(M=1\) case; that case is introduced separately in Claim 3.

## 2. Higher differences

Both assertions are true, with the usual convention
\(\Delta_s f(u)=f(u+s)-f(u)\).

The rational identity

\[
 \Delta_s^d {1\over u}
 = {(-1)^d d!s^d\over\prod_{i=0}^d(u+is)}             \tag{3}
\]

holds whenever its denominators are defined. It follows by induction. The
case \(d=1\) is the subtraction of two fractions. If the right side for
order \(d\) is denoted by \(F_d(u)\), then subtracting \(F_d(u)\) from
\(F_d(u+s)\) introduces the numerator
\(u-(u+(d+1)s)=-(d+1)s\), which gives the order-\(d+1\) formula.

Here \(u+is\) is odd for every integer \(i\), because \(u\) is odd and
\(s\) is even. We may therefore reduce (3) modulo \(M\) and multiply it by
\(N\). This proves

\[
 \Delta_s^d f(u)
 \equiv {(-1)^d d!Ns^d\over\prod_{i=0}^d(u+is)}
 \pmod M.
\]

For the global polynomial assertion, put

\[
 g(j)=N(u+sj)^{-1}\pmod M.
\]

Apply the proved identity with \(u+sj\) in place of \(u\). Every denominator
is still odd, while the numerator has 2-adic valuation

\[
 rd+v_2(d!)
\]

because \(N\) is odd. Under the stated condition this is at least \(k\), so

\[
 \Delta^d g(j)=0\pmod M                                      \tag{4}
\]

for every integer \(j\).

Let \(c_t=\Delta^t g(0)\in\mathbb Z/M\mathbb Z\), and define the
binomial-polynomial sequence

\[
 P(j)=\sum_{t=0}^{d-1}c_t\binom jt.                         \tag{5}
\]

The binomial coefficient is an integer for every integer \(j\), including
negative \(j\), so (5) is well-defined modulo \(M\). The standard Newton
identity shows that \(P(j)=g(j)\) for \(j=0,\ldots,d-1\), and
\(\Delta\binom jt=\binom j{t-1}\) gives \(\Delta^dP=0\).

For completeness, equality also holds at every negative integer; this does
not require division in \(\mathbb Z/M\mathbb Z\). The difference
\(D=g-P\) satisfies

\[
 \sum_{i=0}^d(-1)^{d-i}\binom diD(j+i)=0.                   \tag{6}
\]

It vanishes at \(0,\ldots,d-1\). Equation (6) first determines all later
values because the coefficient of \(D(j+d)\) is \(1\), and then determines
all earlier values because the coefficient of \(D(j)\) is \((-1)^d\).
Both are units modulo \(M\). Thus \(D(j)=0\) for every integer \(j\), which
proves the exact scope claimed in the statement.

In particular, \(d=1\) says the sequence is constant when \(r\geq k\), and
\(d=2\) says it is affine when \(2r+1\geq k\). The latter is the finite
difference form of the affine identity used in Claim 1. There is no small
\(k\) exception, and the possible noninvertibility of \(d!\) causes no
problem: the proof multiplies by \(d!\) and never divides by it.

## 3. The constant-accuracy reduction

The mathematical assertion is true, including \(M=1\), and the constant
\(101/100\) has enough strict slack.

Choose a nontrivial factorization

\[
 N=pq,\qquad 3\leq p\leq q.
\]

Such a factorization exists because \(N\) is odd and composite. Set

\[
 \alpha=\log_2(q/p),\qquad j_* = \lfloor\alpha+1/2\rfloor.
\]

Then \(j_*\geq0\), and \(\alpha<\log_2N<n\) implies \(j_*\leq n\). Hence
this normal occurs among the queries. For this query write

\[
 a=2^{j_*},\qquad b=1,\qquad t={ap\over q}.
\]

Nearest-integer rounding gives

\[
 2^{-1/2}\leq t\leq2^{1/2}.                                \tag{7}
\]

The factor point \((p,q)\) belongs to \(S\), so, with
\(L=ap+q\),

\[
 \operatorname{OPT}_{j_*}\leq L.
\]

Let \((x,y)=Q_{j_*}\) be the supplied point and put \(\rho=101/100\).
Weighted AM-GM and the approximation guarantee give

\[
 \begin{aligned}
 xy
 &\leq{(ax+by)^2\over4ab}\\
 &\leq \rho^2{L^2\over4ab}\\
 &=\rho^2N{(1+t)^2\over4t}.                                \tag{8}
 \end{aligned}
\]

On the interval (7), the last factor is maximized at an endpoint, and

\[
 \max { (1+t)^2\over4t}
 ={4+3\sqrt2\over8}
 <{29\over28},                                             \tag{9}
\]

where the strict inequality follows from \(\sqrt2<10/7\). Therefore

\[
 \rho^2{(1+t)^2\over4t}
 <{10201\over10000}{29\over28}
 ={295829\over280000}
 <{17\over16}.                                             \tag{10}
\]

Let \(M\) be the largest nonnegative integral power of two at most \(N/8\).
It exists because \(N\geq9\). Its maximality gives

\[
 M\leq N/8<2M,
 \quad\text{and hence}\quad M>N/16.                        \tag{11}
\]

Combining (8)--(11) yields

\[
 N\leq xy<{17N\over16}<N+M.                               \tag{12}
\]

Feasibility also says \(xy\equiv N\pmod M\). Thus
\(xy=N+\ell M\) for a nonnegative integer \(\ell\), and (12) forces
\(\ell=0\). Hence \(xy=N\).

It remains to exclude the two trivial factor points. By (7),

\[
 \rho L=\rho q(1+t)
 <{101\over100}{17\over7}q
 ={1717\over700}q
 <3q\leq N.                                                \tag{13}
\]

Both \((1,N)\) and \((N,1)\) have objective value at least \(N\), because
\(a,b\geq1\). But the supplied point has objective at most
\(\rho\operatorname{OPT}_{j_*}\leq\rho L<N\). It can therefore be neither
trivial point. Thus \(x>1\) and \(y>1\).

The \(M=1\) cases need no separate assumption about modular inverses or the
affine cover. For the stated range of odd composites they are \(N=9\) and
\(N=15\). Congruence modulo one is vacuous, and (12) reads
\(N\leq xy<N+1\), which still forces the integer product to equal \(N\).
For \(M=2\) and every larger allowed power of two, the same next-congruence-
class argument applies verbatim.

### Bit-cost interpretation

There are \(2n+1=O(n)\) queries. Each coordinate of a normal is either \(1\)
or a power of two no larger than \(2^n\), so its ordinary binary encoding has
at most \(n+1=O(n)\) bits. The parameters \(N\) and \(M\) also have \(O(n)\)
bits and give a succinct description of \(S\).

The returned coordinates cannot hide an excessive output cost. Since
\((1,N)\in S\), for every query

\[
 a_jx_j+b_jy_j
 \leq\rho\operatorname{OPT}_j
 \leq\rho(a_j+b_jN).
\]

Here \(a_j,b_j\leq2^n\), \(N<2^n\), and both weights are at least one.
Consequently \(x_j\) and \(y_j\) each have \(O(n)\) bits. Feasibility and
the equality \(x_jy_j=N\) can therefore be checked with polynomially many
bit operations.

If one optimizer call has bit cost \(T(n)\), the literal total bound supplied
by this reduction is

\[
 O\bigl(nT(n)+\operatorname{poly}(n)\bigr).                 \tag{14}
\]

Thus the statement's wording "\(QP(n)\) total cost" is correct under the
usual convention that \(QP\) denotes the quasi-polynomial complexity class,
which is closed under polynomial factors. If `QP(n)` instead names one fixed
numerical bound without that closure convention, the exact conclusion is
(14), not literally the same function `QP(n)`.

This cost conclusion also presumes that the optimizer receives the succinct
instance \((N,M,a_j,b_j)\), or an equivalent \(O(n)\)-bit description of
\(S\). Explicitly listing the \(2^{h-1}\) affine translates from Claim 1 is
not an \(O(n)\)-size encoding. The conditional reduction itself does not
need that listing. As the statement says, none of these arguments constructs
such an optimizer or proves its cost bound.

## Verdicts

1. **Claim 1 follows exactly as stated for every \(k\geq1\).** Its small
   moduli \(M=2,4,8\) have no exceptions. The claimed count, disjointness,
   and determinant are exact.
2. **Claim 2 follows exactly as stated for every \(d,r\geq1\) and all integer
   \(j\).** The valuation condition is sufficient, and no division by the
   nonunit \(d!\) is used.
3. **Claim 3 follows exactly at approximation factor \(101/100\), including
   the vacuous-congruence case \(M=1\).** The algorithmic statement is a
   conditional reduction. Its literal call accounting is (14); calling that
   `QP(n)` uses the standard complexity-class convention and a succinct
   encoding of \(S\).
