# F248 V2 — Self-contained boundaries for two exact-square source arms

## Status and scope

This is a proof-only candidate. No numerical experiment was used.

The packet studies two ways to supply a positive integer \(V\) together with
a known square root \(x\bmod N\):

1. scalar powers reduced modulo \(N^2\);
2. norm-one torus rows \(1+D_0y^2\).

If \(V=s^2\) is an exact integer square, the two gcds

\[
\gcd(s-x,N),\qquad \gcd(s+x,N)
\]

factor \(N\) exactly when \(s/x\bmod N\) is a mixed square root of one.
The results below bound several direct ways to obtain such a square. They do
not bound a general product of distinct rows.

This revision contains no named-family or marker transfer. Every asymptotic
bank conclusion is conditional on explicit parameters in this statement.

## Common notation

Let

\[
N=pq,
\]

where \(p\ne q\) are odd primes. Put \(M=N^2\) and

\[
n=\lceil\log_2(N+1)\rceil.
\]

For a unit \(z\bmod m\), let \([z]_m\in\{1,\ldots,m-1\}\) denote its least
positive representative.

Let \(E\) be a positive even integer with \(\gcd(E,N)=1\), and define

\[
g_p=\gcd(E,p-1),\qquad
g_q=\gcd(E,q-1),\qquad
K=g_pg_q.
\]

A square root of one modulo \(N\) is **global** if its CRT signs are
\((1,1)\) or \((-1,-1)\). It is **mixed** if its signs are \((1,-1)\) or
\((-1,1)\).

## Theorem A — Uniform full-lift square law

Choose \(A\) uniformly from \((\mathbb Z/M\mathbb Z)^\times\), and define

\[
L=[A^E]_M,
\qquad
x=[A^{E/2}]_N.
\]

Then

\[
\Pr[L\text{ is an exact integer square}]\le \frac K N.
\]

Condition on a fixed square output \(L=s^2\) that is in the image. The
supplied roots are uniform on a coset of the image of

\[
z\longmapsto z^{E/2}\pmod N
\]

from the kernel of the \(E\)-power map modulo \(N^2\). On a local side
\(r\in\{p,q\}\), this image is

\[
\{1,-1\}
\quad\Longleftrightarrow\quad
v_2(E)\le v_2(r-1),
\]

and it is \(\{1\}\) otherwise. If at least one local side has image
\(\{1,-1\}\), exactly one half of the preimages of the fixed square output
have a mixed normalized root and factor \(N\).

## Theorem B — Principal-lift exact law

Fix a unit \(a\bmod N\), fix one integer lift \(a_0\), and vary

\[
A_t=a_0+tN\pmod{N^2},\qquad t\bmod N.
\]

Write

\[
[A_t^E]_{N^2}=r+Nh_t,
\qquad
r=[a^E]_N,
\qquad
x=[a^{E/2}]_N,
\]

with \(0\le h_t<N\). Then

\[
h_t=h_0+Ea^{E-1}t\pmod N.
\]

The map \(t\mapsto h_t\) is a bijection. Exactly four members of the fibre
are exact integer squares. Exactly two of those four have a mixed normalized
root relative to \(x\). Thus, for uniform \(t\bmod N\),

\[
\Pr([A_t^E]_{N^2}\text{ is an exact square})=\frac4N,
\qquad
\Pr(\text{the square factors }N)=\frac2N.
\]

Finding either useful square digit is polynomial-time equivalent to finding
a mixed second square root of \(r\bmod N\). A useful square gives such a root.
Given the factorization of \(N\), CRT constructs both mixed roots and both
useful digits.

### Fixed-past extension

Let \(P>0\) be fixed before a fresh uniform \(t\bmod N\) is sampled. Assume
\(\gcd(P,N)=1\), and suppose a unit \(X\bmod N\) is supplied with

\[
X^2\equiv P\pmod N.
\]

Among the \(N\) rows \(B_t=[A_t^E]_{N^2}\), at most two values of \(t\) make
\(PB_t\) an exact integer square whose normalized root relative to \(Xx\) is
mixed. Hence the conditional probability is at most \(2/N\), for every fixed
past.

This is a one-fresh-row statement. It does not bound a subset chosen from an
exponential collection after the fresh row is known. It also gives no bound
for the fixed canonical section \(t=0\).

## Theorem C — Canonical scalar duplicates

Choose independent uniform units \(a,b\bmod N\), represented in
\(\{1,\ldots,N-1\}\), and put

\[
u(a)=[a^E]_{N^2}.
\]

Then

\[
\Pr[u(a)=u(b)]\le \frac K{\varphi(N)}.
\]

For a duplicate, the supplied-root ratio

\[
[a^{E/2}]_N[b^{E/2}]_N^{-1}\pmod N
\]

is a square root of one. It factors \(N\) exactly when it is mixed.

## Theorem D — Reciprocal-output square-pair bound

Choose a uniform canonical unit \(a\in\{1,\ldots,N-1\}\), and put

\[
u=[a^E]_M,
\qquad
v=[u^{-1}]_M.
\]

Let

\[
\mathcal R_M=
\{R\in\{1,\ldots,M-1\}:R^2\equiv1\pmod M\},
\qquad
S_M=\sum_{R\in\mathcal R_M}\tau(R^2).
\]

Then

\[
\Pr[uv\text{ is an exact integer square}]
\le \frac{KS_M}{\varphi(N)}.
\]

There are four members of \(\mathcal R_M\), and \(S_M=2^{o(n)}\). If the
exact root is mixed modulo \(N\), it factors \(N\). A global root is a decoy.

This theorem concerns the reciprocal of the **output** modulo \(N^2\). It
does not concern first replacing \(a\) by its canonical inverse modulo \(N\)
and then powering that new integer base.

## Torus notation

Fix a unit \(D\bmod N\), and let \(D_0=[D]_N\in\{1,\ldots,N-1\}\). Define

\[
T_D(N)=\{(x,y):x^2-Dy^2=1\pmod N\}.
\]

A point is **clean** when \(x\) is a unit modulo \(N\). For a clean point,
use the canonical coordinate \(y\in\{0,\ldots,N-1\}\) and define

\[
A_y=1+D_0y^2.
\]

The supplied square root of \(A_y\bmod N\) is \(x\).

For \(r\in\{p,q\}\), put

\[
m_r=r-\left(\frac Dr\right),
\qquad
z_r=1+\left(\frac{-D}{r}\right)\in\{0,2\},
\]

and

\[
H=(m_p-z_p)(m_q-z_q).
\]

Thus \(H\) is the number of clean global torus points.

Define

\[
B_D(N)=1
\]

when \(D_0\) is an integer square. Otherwise define

\[
B_D(N)=1+
\left\lfloor
\frac{\log(2N\sqrt{D_0}+1)}{\log(2\sqrt{D_0})}
\right\rfloor.
\]

Uniformly for \(1\le D_0<N\), one has \(B_D(N)=O(n)\).

## Theorem E — Raw torus one-row and duplicate laws

Choose a point uniformly from the \(H\) clean torus points. Then

\[
\Pr[A_y\text{ is an exact integer square}]
\le \frac{4B_D(N)}H.
\]

For two independent uniform clean points,

\[
\Pr[A_{y_1}=A_{y_2}]=\frac4H,
\qquad
\Pr[\text{duplicate with mixed supplied-root ratio}]=\frac2H.
\]

## Theorem F — Powered torus one-row and duplicate laws

Fix a positive public exponent \(W\). Power a uniform torus point by \(W\).
On the local side \(r\in\{p,q\}\), the image subgroup has order

\[
\rho_r=\frac{m_r}{\gcd(m_r,W)}.
\]

Let \(z'_r\in\{0,2\}\) count its points with \(x=0\). Condition on the
powered global point being clean, and put

\[
H'=(\rho_p-z'_p)(\rho_q-z'_q).
\]

Assume

\[
\gcd(\rho_p,\rho_q)=1.
\]

Then

\[
\Pr[A_y\text{ is an exact integer square}]
\le \frac{2B_D(N)}{H'}.
\]

If both local image orders are odd, equal \(y\)-coordinates imply the same
powered point, so a duplicate supplies no second root. If exactly one local
image order is even, then

\[
\Pr[\text{two independent clean powered points form a useful duplicate}]
=\frac1{H'}.
\]

No lower bound for \(H'\) is asserted for an arbitrary exponent \(W\).

## Theorem G — Torus inverse-point identity

For a clean point with \(1\le y<N\), its inverse has canonical coefficient
\(N-y\). Put

\[
C=1-D_0y(N-y).
\]

Then

\[
\boxed{A_yA_{N-y}=C^2+D_0N^2},
\qquad
C\equiv x^2\pmod N.
\]

If \(A_yA_{N-y}=R^2\), then

\[
(R-C)(R+C)=D_0N^2.
\]

At most \(2\tau(D_0N^2)\) nonzero canonical \(y\)-values produce an exact
square. Therefore, for a uniform clean raw point,

\[
\Pr[y\ne0\text{ and }A_yA_{N-y}\text{ is square}]
\le \frac{8\tau(D_0N^2)}H.
\]

Under the powered hypotheses of Theorem F,

\[
\Pr[y\ne0\text{ and }A_yA_{N-y}\text{ is square}]
\le \frac{4\tau(D_0N^2)}{H'}.
\]

Here \(\tau(D_0N^2)=2^{o(n)}\). The normalized exact root \(R/C\bmod N\)
is a square root of one and factors \(N\) exactly when mixed. The excluded
case \(y=0\) is the global decoy \(A_0^2=1\).

## Conditional bank corollary

Let \(T=T(n)\). Union bounds give all of the following.

- \(T\) uniform full scalar lifts have one-row square probability at most
  \(TK/N\).
- \(T\) adaptive principal-lift stages, each with its past product fixed
  before its fresh uniform lift coordinate, have useful-closure probability
  at most \(2T/N\).
- \(T\) independent uniform canonical scalar bases have duplicate
  probability at most \(\binom T2K/\varphi(N)\). Their \(T\) reciprocal-output
  pairs have square probability at most \(TKS_M/\varphi(N)\).
- \(T\) independent uniform clean raw torus points have one-row probability
  at most \(4TB_D(N)/H\), useful-duplicate probability at most
  \(2\binom T2/H\), and inverse-pair probability at most
  \(8T\tau(D_0N^2)/H\).
- Under Theorem F, the corresponding powered bounds are
  \(2TB_D(N)/H'\), zero or \(\binom T2/H'\) for a useful duplicate, and
  \(4T\tau(D_0N^2)/H'\) for an inverse pair.

In particular, suppose

\[
T=2^{(\log n)^{O(1)}},\qquad K=2^{o(n)},
\]

and suppose \(H=2^{\Omega(n)}\), or \(H'=2^{\Omega(n)}\) for the applicable
torus claim. Then every applicable displayed bank probability is
\(2^{-\Omega(n)}\). These are conditional consequences. This packet does not
construct a family for which the hypotheses hold.

## Exact boundary

The packet controls only these rigid events:

1. one exact-square row;
2. an exact duplicate row;
3. a scalar output paired with its reciprocal modulo \(N^2\);
4. a torus point paired with its inverse;
5. one fresh principal lift against one product fixed before that lift.

It does not control an unrelated nonduplicate pair, a mixed scalar-torus
relation, an adaptively selected subset of many past rows, a general
multirow integer-prime parity dependency, the fixed canonical lift section,
or the canonical-inverse-base pair. It gives no all-input factoring
algorithm and no unconditional quasipolynomial success or failure theorem.
