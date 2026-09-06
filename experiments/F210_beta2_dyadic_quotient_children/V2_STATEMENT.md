# F210 V2: dyadic quotient siblings are half-translated, with a conditional common-order bridge

Status: frozen proof-only candidate, repaired after the V1 hostile audit.

## Scope and imported interfaces

Assume

\[
N=pq,
\qquad p<q<2p,
\tag{1}
\]

where \(p,q\) are distinct odd primes. Let

\[
n=\lceil\log_2(N+1)\rceil.
\tag{2}
\]

F210 V2 imports three promoted interfaces.

1. P179 supplies the dyadic quotient state and proves the basic positivity
   and coprimality properties recalled below.
2. P183 proves that one decrement spine may carry a numerical-QP number of
   fixed-ratio side children.
3. P172 gives a numerical-QP factoring terminal from a fully known common
   local order \(e\), coprime to \(N\), when
   \(N^{1/4}/e\) is numerical QP.

F210 V2 gives exact formulas for the two P179 quotient children, identifies
an odd-local half-translation between them, and gives one conditional
positive use of their complete factorizations. It does not give a guaranteed
child selector or a factoring algorithm.

## Dyadic quotient state

Let

\[
m=2^t,
\qquad t\ge1,
\qquad 2m<p,
\tag{3}
\]

and grant a correct reciprocal prefix

\[
u\equiv p^{-1}\pmod m.
\tag{4}
\]

Let \(r,c\in\{1,3,\ldots,m-1\}\) be the canonical residues

\[
r\equiv u^{-1}\equiv p\pmod m,
\qquad
c\equiv Nu\equiv q\pmod m.
\tag{5}
\]

Put

\[
K={N-rc\over m},
\qquad
\delta=K\bmod2.
\tag{6}
\]

For \(a\in\{0,1\}\), define

\[
b_a=a\mathbin{\mathsf{xor}}\delta,
\qquad
r_a=r+am,
\qquad
c_a=c+b_am,
\tag{7}
\]

and

\[
h=2m,
\qquad
K_a={N-r_ac_a\over h}.
\tag{8}
\]

Exactly one \(a\) is the next bit of the smaller factor. Both \(K_a\) are
public positive integers satisfying

\[
K_a<{N\over2m},
\qquad
\gcd(K_a,N)=1.
\tag{9}
\]

The question is whether the complete factorizations of both \(K_0,K_1\)
select that bit.

## Theorem 1: exact siblings, coalescence, and common support

If \(\delta=0\), then

\[
\begin{array}{c|c|c|c}
a&r_a&c_a&K_a\\ \hline
0&r&c&K/2\\
1&r+m&c+m&(K-r-c-m)/2.
\end{array}
\tag{10}
\]

If \(\delta=1\), then

\[
\begin{array}{c|c|c|c}
a&r_a&c_a&K_a\\ \hline
0&r&c+m&(K-r)/2\\
1&r+m&c&(K-c)/2.
\end{array}
\tag{11}
\]

Consequently, with

\[
D=K_0-K_1,
\tag{12}
\]

one has

\[
D=
\begin{cases}
(r+c+m)/2,&\delta=0,\\[1mm]
(c-r)/2,&\delta=1.
\end{cases}
\tag{13}
\]

The children coalesce exactly when

\[
\boxed{K_0=K_1\iff \delta=1\text{ and }r=c.}
\tag{14}
\]

This includes the first stage \(t=1\), \(m=2\), \(N\equiv3\pmod4\),
where

\[
K_0=K_1={N-3\over4}.
\tag{15}
\]

Put

\[
g=\gcd(K_0,K_1).
\tag{16}
\]

Outside coalescence,

\[
g=\gcd(K_0,|D|)=\gcd(K_1,|D|),
\tag{17}
\]

so every common prime-power support lies in the explicit difference, with

\[
0<D<{3m\over2}\quad(\delta=0),
\qquad
0<|D|<{m\over2}\quad(\delta=1).
\tag{18}
\]

The full joint child modulus is exactly

\[
\boxed{
L=\operatorname{lcm}(K_0,K_1)={K_0K_1\over g}.}
\tag{19}
\]

Equations (17)--(19) are arithmetic identities. They do not say that
factoring the private support of either child is uninformative.

## Theorem 2: the two quotient curves differ by a half-translation

Put

\[
\sigma=(-1)^\delta
\tag{20}
\]

and define

\[
F_a(P,Q)=hPQ+c_aP+r_aQ-K_a.
\tag{21}
\]

Then the following identity holds in
\(\mathbb Z[1/2][P,Q]\):

\[
\boxed{
F_1\left(P-{1\over2},Q-{\sigma\over2}\right)=F_0(P,Q).}
\tag{22}
\]

Equivalently, for

\[
A_a=
\begin{pmatrix}
r_a&h\\
-K_a&c_a
\end{pmatrix},
\qquad \det A_a=N,
\tag{23}
\]

one has

\[
\boxed{
A_1=
\begin{pmatrix}1&0\\ \sigma/2&1\end{pmatrix}
A_0
\begin{pmatrix}1&0\\ 1/2&1\end{pmatrix}.}
\tag{24}
\]

For every ring in which two is a unit, (22) gives a public affine
isomorphism between the two solution curves. In the physical coordinates

\[
X=hP+r_a,
\qquad
Y=hQ+c_a,
\tag{25}
\]

both equations become the same integer equation

\[
\boxed{XY=N.}
\tag{26}
\]

In particular, for every odd modulus \(s\), translation by the two displayed
halves gives a bijection between the two congruence solution sets. Therefore
every statistic that depends only on the odd-local solution scheme up to
affine coordinate change is identical for the two children. This includes
point counts, singularity and multiplicity data, coordinate-free Frobenius
data, and the genus or class data of this abstract split curve. Any
elimination invariant computed after aligning the coordinates also agrees;
the aligned equations are literally identical.

The factorization of one child does give prime-power moduli. For every odd
prime power \(\ell^e\mid K_a\), all of \(N,r_a,c_a\) are units modulo
\(\ell^e\), and

\[
N\equiv r_ac_a\pmod {\ell^e},
\tag{27}
\]

so every multiplicative character obeys

\[
\chi(N)=\chi(r_a)\chi(c_a).
\tag{28}
\]

There is also the public scaled square root

\[
\boxed{
r_a^2\equiv
N\,r_ac_a^{-1}\pmod {\ell^e}.}
\tag{29}
\]

Equations (27)--(29) hold for both children. They do not force an unscaled
square root of \(N\), and they do not prove that raw Jacobi or higher-residue
statistics of the two different child factorizations agree.

The prime two does not rescue finite lift feasibility. Because \(t\ge1\),
the modulus \(h=2^{t+1}\) is defined with \(t+1\ge2\). For every
\(s\ge t+1\), let \(\mathcal S_a(s)\) be the ordered pairs modulo \(2^s\)
satisfying

\[
XY=N,
\qquad
X\equiv r_a\pmod h,
\qquad
Y\equiv c_a\pmod h.
\tag{30}
\]

Then

\[
\boxed{|\mathcal S_0(s)|=|\mathcal S_1(s)|=2^{s-t-1}.}
\tag{31}
\]

Thus finite \(2\)-adic existence and multiplicity also do not select the
child. The surviving exact distinction is the **nontrivial balanced integer
point**: the true chart, and only the true chart, has an integer point whose
physical coordinates satisfy

\[
\boxed{1<X<\sqrt N<Y<N,\qquad XY=N.}
\tag{31a}
\]

That point is \((p,q)\). In a coalesced state the other chart can contain
the swapped nontrivial point \((q,p)\), which reverses the strict orientation
in (31a). A false chart can also contain a trivial endpoint such as
\((1,N)\) or \((N,1)\); those endpoints are excluded by (31a). No claim is
made that the true chart is the only chart with any integer point, or with an
integer point satisfying only \(X<\sqrt N<Y\). Detecting (31a) is an
Archimedean or exact integer operation, not an odd-local curve invariant.

## Theorem 3: exact conditional order-stripping bridge

Define the two fully factored public exponents

\[
H_a=hK_a=N-r_ac_a.
\tag{32}
\]

Given the complete factorizations of \(K_0,K_1\), the factorizations of
\(H_0,H_1\) and of

\[
G=\gcd(H_0,H_1)=h\gcd(K_0,K_1)=hg
\tag{33}
\]

are known. Let \(w\) be any public unit modulo \(N\). Compute

\[
d_a=\gcd(w^{H_a}-1,N).
\tag{34}
\]

A proper \(d_a\) factors \(N\). If

\[
d_0=d_1=N,
\tag{35}
\]

then \(w^G=1\pmod N\). Factor-first stripping of the known factorization of
\(G\) returns either a proper factor of \(N\) or a fully known exact common
local order

\[
e=\operatorname{ord}_p(w)=\operatorname{ord}_q(w),
\qquad e\mid G.
\tag{36}
\]

Moreover,

\[
\gcd(e,N)=1.
\tag{37}
\]

If there is a fixed numerical-QP bound \(Q\) such that

\[
{N^{1/4}\over e}\le Q(n),
\tag{38}
\]

then P172 factors \(N\) in numerical-QP time.

The exact common-root content of the two exponent polynomials is

\[
\boxed{
\gcd_{\mathbb Z[X]}(X^{H_0}-1,X^{H_1}-1)=X^G-1.}
\tag{39}
\]

Their ordinary resultant is zero because they always share \(X-1\).
Equation (39), not that zero resultant, is the exact common-order datum.

This theorem is a positive bridge, but it is conditional. Neither a proper
gcd in (34), the simultaneous return (35), nor the large order threshold
(38) is guaranteed. An asymmetric pair \((d_0,d_1)=(N,1)\) or \((1,N)\)
is a public feature, but F210 V2 proves no fixed relation between its
direction and the true child.

## Theorem 4: both-child factorization is recursion-safe only at late stages

For every state with \(t\ge1\) and every child,

\[
K_a<{N\over2^{t+1}}<2^{n-t-1}.
\tag{40}
\]

Fix \(\eta>0\). If

\[
t\ge\eta n-O(1),
\tag{41}
\]

then each child has at most

\[
(1-\eta)n+O(1)
\tag{42}
\]

input bits. Consequently, a postprocessor which makes a numerical-QP
number of calls to factor both children at stages satisfying (41), in
addition to at most one \((n-1)\)-bit spine call, obeys a recurrence of the
P183 form

\[
T(n)\le T(n-1)
+Q(n)T((1-\eta)n+O(1))+Q(n),
\tag{43}
\]

and is numerical QP.

At the P175 precision

\[
t=\left\lfloor{\log_2N\over4}\right\rfloor
-(\log n)^{O(1)},
\tag{44}
\]

the two children have at most \(3n/4+(\log n)^{O(1)}\) bits, so any fixed
\(\rho>3/4\) covers them for all sufficiently large inputs.

This accounting does not manufacture the granted prefix in (4), select a
child, or justify factoring both siblings at the early stages \(t=o(n)\).
There they can both have \(n-o(n)\) bits, and an early binary recursion tree
is outside P183. A single recursive chain with
\(T(n)\le T(n-1)+Q(n)\) remains valid; the problem is to construct that
chain.

## Exact remaining gate

F210 V2 closes the following direct mechanisms only:

1. common child support outside the explicit difference \(D\);
2. odd-local affine-invariant curve, point-count, Frobenius, genus, and
   aligned-elimination distinctions;
3. finite \(2\)-adic lift existence or multiplicity; and
4. the claim that the two fully factored exponents contain common-root
   information beyond \(G=hg\).

It leaves open:

1. a guaranteed selector from raw prime-support, Jacobi, higher-residue,
   exact-order, or other asymmetric statistics of the two factorizations;
2. an adaptive base that forces the order-stripping bridge to terminate;
3. an algorithmic test for the nontrivial balanced point (31a), or another
   integral or Archimedean bounded-point test for one quotient chart;
4. class-group constructions tied to a new integral order rather than the
   abstract odd-local curve; and
5. a globally nested one-spine construction that reaches the recursion-safe
   late range.

