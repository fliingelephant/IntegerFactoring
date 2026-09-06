# F283 — named evaluator boundaries for the shifted normalized difference

## Status and scope

F283 is a proof-only candidate. It studies the exact evaluator left open by
P230/F282. It gives no evaluator, factoring algorithm, numerical search, or
general lower bound.

Let

\[
 N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor,
\]

where \(p,q\) are distinct odd primes. First test \(\gcd(B,N)\). On the
unresolved branch, write

\[
 B=p+s,\qquad q=B+h.
\]

The P230 geometry gives

\[
 s\ge1,\qquad h\ge s+2,\qquad p\ge2s+3,
 \qquad p<B<q<2p<2B.
\tag{1}
\]

For an integer shift \(a\), the target is

\[
 F_B(a)=\frac{\Delta^B X^{2B}|_{X=a}}{B!}
       =h_B(a,a+1,\ldots,a+B).
\tag{2}
\]

The division in (2) is exact over \(\mathbb Z\). It is not modular
division. P230 proves that \(q\mid F_B(a)\) for every \(a\), while a uniform
shift avoids divisibility by \(p\) with probability above one half. F283
only audits proposed ways to evaluate (2).

## 1. The exact generalized-Stirling endpoint

Define

\[
 G_a(n,k)=[a,a+1,\ldots,a+k]X^n
          =h_{n-k}(a,a+1,\ldots,a+k)
\tag{3}
\]

for \(0\le k\le n\). Then

\[
 \boxed{F_B(a)=G_a(2B,B).}
\tag{4}
\]

The connection coefficients satisfy

\[
 X^n=\sum_{k=0}^nG_a(n,k)(X-a)_{\underline{k}},
\tag{5}
\]

and

\[
 G_a(n+1,k)=G_a(n,k-1)+(a+k)G_a(n,k).
\tag{6}
\]

For every nonnegative integer \(a=r\), (3) is the usual \(r\)-Stirling
number

\[
 G_r(n,k)=
 \left\{\begin{matrix}n+r\\k+r\end{matrix}\right\}_r.
\tag{7}
\]

The polynomial identity (3), not the combinatorial restriction \(r\ge0\),
is the relevant definition for arbitrary sampled shifts.

Two exact generating functions are

\[
 G_a(n,k)=\frac{n!}{k!}[z^n]e^{az}(e^z-1)^k
\tag{8}
\]

and, for fixed \(B\),

\[
 \sum_{d\ge0}G_a(B+d,B)t^d
 =\prod_{j=0}^{B}(1-(a+j)t)^{-1}.
\tag{9}
\]

Equations (3), (6), (8), and (9) are exact aliases. Their literal endpoint
computations have a range or coefficient extraction of characteristic size.

## 2. Minimal size of the canonical linear coefficient state

Work over \(K=\mathbb Q(a)\), and put

\[
 u_d=h_d(a,a+1,\ldots,a+B).
\]

The reduced rational generating function of \((u_d)_{d\ge0}\) is exactly

\[
 U_B(t)=\frac1{\prod_{j=0}^{B}(1-(a+j)t)}.
\tag{10}
\]

Its denominator has \(B+1\) distinct uncancelled linear factors over
\(K\). Therefore:

1. the minimal homogeneous constant-coefficient recurrence over \(K\) for
   the full sequence \((u_d)\) has order \(B+1\); and
2. every linear constant-matrix realization over \(K\) which generates the
   full sequence has dimension at least \(B+1\).

The same mode count survives every fixed-radix decimation. For fixed
integers \(r\ge1\) and \(c\ge0\), the sequence

\[
 (u_{rd+c})_{d\ge0}
\tag{11}
\]

also has minimal constant-coefficient recurrence order \(B+1\) over
\(K\). Thus taking even, odd, or repeated radix subsequences does not shrink
the canonical linear coefficient state.

There is also a canonical \((B+1)\)-dimensional constant matrix for the
generalized-Stirling recurrence. With indices \(0,\ldots,B\), let

\[
 M_B(a)_{k,k}=a+k\quad(0\le k\le B),
 \qquad M_B(a)_{k,k-1}=1\quad(1\le k\le B)
\tag{12}
\]

and let all other entries be zero. Then

\[
 F_B(a)=e_B^{\mathsf T}M_B(a)^{2B}e_0.
\tag{13}
\]

Binary powering makes the exponent cheap only after the matrix is given.
The canonical matrix has characteristic-size dimension. The minimality
claim concerns the full coefficient sequence in (10). It does not rule out
a tailored construction which targets only \(u_B\), uses nonlinear state,
or places hard-to-compute data directly in a small matrix entry.

## 3. Translation and block composition are full-width in the named state

For every integer or indeterminate \(c\), translation gives

\[
 \boxed{
 F_B(a+c)=\sum_{j=0}^{B}
 \binom{2B}{B-j}c^{B-j}h_j(a,a+1,\ldots,a+B).}
\tag{14}
\]

All \(B+1\) coefficients in (14) are nonzero over characteristic zero.
Thus one base value \(F_B(a)\) does not translate a random shift. The
literal translated complete-homogeneous state has width \(B+1\).

Two shorter shift identities are

\[
 F_B(-B-a)=(-1)^BF_B(a)
\]

and

\[
 F_B(a+1)-F_B(a)
 =(B+1)h_{B-1}(a,a+1,\ldots,a+B+1).
\]

The reflection does not reduce the index \(B\). The first-difference law
leaves the target family and starts a ladder of neighboring degrees and
node counts. Neither identity evaluates a base value.

A uniform residue remains uniform after \(a\mapsto ua+c\) when
\(\gcd(u,N)=1\). Public unit-affine changes, including the reflection, keep
the P230 sampling law. Replacing the sampled shift by one fixed shift does
not.

Put

\[
 H_{L,a}(t)=\prod_{j=0}^{L}(1-(a+j)t)^{-1}.
\tag{15}
\]

Its denominator is an ordinary rising-factorial expression:

\[
 \prod_{j=0}^{L}(1-(a+j)t)
 =(-t)^{L+1}(a-t^{-1})^{\overline{L+1}}.
\]

The ordinary Pochhammer duplication law is the same two-child parity split
given below. It is not a one-child geometric \(q\)-product powering law.

Splitting a consecutive interval gives

\[
 H_{L_1+L_2+1,a}(t)
 =H_{L_1,a}(t)H_{L_2,a+L_1+1}(t).
\tag{16}
\]

The coefficient of degree \(d\) in (16) is the full convolution

\[
 \sum_{i=0}^{d}[t^i]H_{L_1,a}(t)
                    [t^{d-i}]H_{L_2,a+L_1+1}(t).
\tag{17}
\]

At \(d=B\), (17) has \(B+1\) literal summands.

The even--odd split is also exact. For \(m\ge0\),

\[
 H_{2m,a}(t)
 =H_{m,a/2}(2t)H_{m-1,(a+1)/2}(2t),
\tag{18}
\]

where the second factor is one when \(m=0\), and

\[
 H_{2m+1,a}(t)
 =H_{m,a/2}(2t)H_{m,(a+1)/2}(2t).
\tag{19}
\]

Since \(N\) is odd, division by two is unit-safe modulo \(N\). However,
the target coefficient still uses the central convolution (17). Direct
recursion through (18) or (19) has two different affine children and
linear total leaf count. These statements concern the displayed coefficient
state and direct recursion only. They do not rule out an unknown aggregation
invariant.

## 4. Divided-power addition chains cross the hidden nonunit

Over \(\mathbb Q[X]\), define the divided difference operator

\[
 \mathcal D_k=\frac{\Delta^k}{k!}.
\]

For all \(m,n\ge0\),

\[
 \boxed{
 \mathcal D_m\mathcal D_n
 =\binom{m+n}{m}\mathcal D_{m+n}.}
\tag{20}
\]

Consider a monotone binary addition chain which starts from index one, uses
only positive earlier indices, never exceeds \(B\), and ends at \(B\).
At the first generated index \(k\ge p\), write \(k=m+n\). Then

\[
 m,n<p,\qquad p\le k\le B<q<2p,
\]

and

\[
 \boxed{\gcd\!\left(\binom{k}{m},N\right)=p.}
\tag{21}
\]

The same conclusion holds for one finite-arity composition whose positive
input indices are all below \(p\) and whose sum first reaches \(k\ge p\):
the multinomial structure constant contains \(p\) exactly once and no
\(q\).

Thus a literal normalized addition chain reaches a factor-bearing exact
division at its first crossing of \(p\). Computing that structure constant
modulo \(N\) already exposes \(p\) by a gcd. Postponing all normalization
leaves the unnormalized endpoint

\[
 \Delta^B X^{2B}|_{X=a}=B!F_B(a)\equiv0\pmod N.
\tag{22}
\]

This is a boundary for monotone divided-power composition. It says nothing
about addition--subtraction chains, a custom exact-quotient decoder, or an
unrelated arithmetic circuit.

## 5. The guaranteed \(q\)-zero is universal interval content

The coefficient of every power of the shift is

\[
 \boxed{
 [a^k]F_B(a)=\binom{2B}{k}
 \left\{\begin{matrix}2B-k\\B\end{matrix}\right\},
 \qquad 0\le k\le B.}
\tag{23}
\]

In particular,

\[
 [a^B]F_B(a)=\binom{2B}{B}.
\tag{24}
\]

Let

\[
 P_B=\prod_{\substack{r\ \mathrm{prime}\\B+1<r<2B}}r.
\tag{25}
\]

For every prime in (25), every integer shift satisfies

\[
 F_B(a)\equiv0\pmod r.
\tag{26}
\]

Because \(\deg_aF_B=B<r\), equation (26) implies coefficientwise
divisibility. Hence

\[
 \boxed{P_B\mid\operatorname{content}(F_B).}
\tag{27}
\]

On the unresolved balanced-semiprime branch, \(q\) lies in the interval
in (25), while \(p\) does not. Also

\[
 v_p\binom{2B}{B}=0,
 \qquad
 v_q\binom{2B}{B}=1.
\tag{28}
\]

It follows that

\[
 \boxed{
 \gcd(P_B,N)=q,
 \qquad
 \gcd(\operatorname{content}(F_B),N)=q.}
\tag{29}
\]

Thus explicit interval-primorial evaluation, content extraction, or leading
coefficient evaluation is already a deterministic factor gate. The leading
coefficient is the known central-binomial gate. This does not prove that an
arbitrary black-box evaluator for \(F_B(a)\) must expose its content as an
intermediate value.

If \(C_B=\operatorname{content}(F_B)\), then both
\(F_B/P_B\) and \(F_B/C_B\) are nonzero polynomials modulo \(q\). Dividing
out the interval content therefore removes the guaranteed \(q\)-zero. To
recover the P230 splitter, a computation must restore a factor-bearing
content multiplier or obtain a different asymmetric observable.

## 6. The immediate \(N\)-adic quotient loses the guaranteed factor

On the unresolved branch, write

\[
 B!=pU,
 \qquad F_B(a)=qV_B(a).
\tag{30}
\]

Here \(U\) is a unit modulo \(N\), and \(V_B(a)\in\mathbb Z[a]\). The raw
difference is

\[
 D_B(a)=B!F_B(a)=NUV_B(a).
\tag{31}
\]

Suppose a proposed lift computes \(D_B(a)\bmod N^2\). Exact division of
its canonical residue by \(N\) gives only

\[
 \frac{D_B(a)}N\equiv UV_B(a)\pmod N.
\tag{32}
\]

The right side has no guaranteed prime divisor of \(N\). Modulo \(p\), it
is a unit multiple of the nonzero P230 shift polynomial. Modulo \(q\), it
is also a nonzero polynomial, because the leading coefficient of
\(F_B/q\) is a \(q\)-unit by (28). There are shifts for which (32) is a
unit modulo \(N\).

Thus the operation “lift the raw difference to \(N^2\), divide by \(N\),
then take a gcd” is not a splitter. This does not rule out a different
higher-lift decoder. Such a decoder must explain how it restores the
specific \(q\)-multiplier removed in (32), without using a hidden factor or
a nonunit inverse.

The literal faithful quotient uses modulus \(NB!\): from
\(D_B(a)\bmod NB!\), exact division by \(B!\) returns \(F_B(a)\bmod N\).
But this modulus has \(\Theta(B\log B)\) bits. Also
\(\gcd(B!\bmod N,N)=p\). This is not a numerical-QP normalization route.
It does not exclude a compressed decoder which never materializes \(B!\),
its residue, or the modulus \(NB!\).

## 7. Search disposition

The exact identities above do not justify a finite symbolic or numerical
search inside any of these named grammars:

1. the \(B+1\)-term divided-difference or Stirling sum;
2. a coefficient vector of length \(B+1\);
3. interval or even--odd block convolution;
4. monotone normalized divided-power addition chains;
5. raw unnormalized differences modulo \(N\);
6. explicit interval primorial, content, factorial, or central-binomial
   evaluation;
7. a canonical constant-matrix or constant-coefficient recurrence state;
8. the immediate \(N^2\)-quotient recovery; or
9. generic baby-step/giant-step or holonomic endpoints with
   \(B^{1/2+o(1)}\) work;
10. exact integer materialization, whose value at \(a=0\) already has
    characteristic-size output; or
11. a local full-field or Frobenius collapse supplied with the hidden
    characteristic \(p\) or \(q\).

Item 9 records the cost of the named published endpoint, not a lower bound
against every holonomic algorithm.

Finite pattern matching in these families can only rediscover identities
whose literal state, convolution, product, or division is already
characteristic-size or factor-bearing.

A future synthesis proposal needs an explicit operation outside this scope.
Before a run, it must give an exact path to
\(\exp(\operatorname{polylog}\log B)\) work and state, accept an arbitrary
public sampled shift, use only public unit-safe operations or return a
verified factor at a failed inversion, and prove that its endpoint is
factor-asymmetric rather than the raw zero in (22). A one-child nonlinear
or adaptive law is not excluded, but no such law is supplied here.

## Exact exclusions

F283 proves no:

1. numerical-QP evaluator for \(F_B(a)\bmod N\);
2. arithmetic-circuit or modular-evaluator lower bound;
3. lower bound for nonlinear, adaptive, branching, or noncanonical states;
4. general Mahler nonexistence theorem;
5. reduction from arbitrary evaluation to content extraction;
6. impossibility of a custom restricted-domain exact-division decoder;
7. all-input factoring theorem; or
8. new empirical result or new literature claim.
