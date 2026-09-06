# F248 — Exact boundaries for two live P66 source arms

## Status

Proof-only candidate.  No numerical experiment was used.

This packet studies two proposed sources for the factor-free P66 parity
decoder:

1. scalar lifts modulo \(N^2\), with a supplied square root modulo \(N\);
2. norm-one torus values \(1+D y^2\), with the torus coordinate \(x\) as a
   supplied square root modulo \(N\).

The results below close the most direct one-row, duplicate-row, and
inverse-pair channels on a named hard family.  They do **not** close a
general dependency between distinct rows.  Even an unrelated nonduplicate
two-row pair is outside the negative results.

## Common notation

Let

\[
N=pq,
\]

where \(p\ne q\) are odd primes, and put \(M=N^2\).  Let

\[
n=\lceil\log_2(N+1)\rceil.
\]

All integer representatives are least nonnegative or least positive
representatives, as specified below.

For an even integer \(E\) with \(\gcd(E,N)=1\), define

\[
g_p=\gcd(E,p-1),\qquad g_q=\gcd(E,q-1),\qquad K=g_pg_q.
\]

The P66 one-row screen for an exact integer square \(V=s^2\), supplied with a
known root \(x\bmod N\), tests

\[
\gcd(s-x,N),\qquad \gcd(s+x,N).
\]

It succeeds exactly when \(s/x\) is a non-global square root of \(1\bmod N\).

## Theorem A — Uniform full-lift square law

Choose \(A\) uniformly from \((\mathbb Z/M\mathbb Z)^\times\), and define

\[
L=[A^E]_M\in\{1,\ldots,M-1\},
\qquad
x=[A^{E/2}]_N.
\]

Then

\[
\Pr[L\text{ is an exact integer square}]\le \frac{K}{N}.
\]

Condition on a fixed square output \(L=s^2\).  The supplied roots are uniform
on a coset of the image of the \(E/2\)-power map on the kernel of the
\(E\)-power map.  On the local side \(r\in\{p,q\}\), this image is

\[
\{\pm1\}
\quad\Longleftrightarrow\quad
v_2(E)\le v_2(r-1),
\]

and is \(\{1\}\) otherwise.  Hence, if at least one local side is active,
exactly half of the preimages of that fixed square output give a non-global
normalized root and factor \(N\).

On the P209 four-marker family:

- for \(E=N-1\), \(K=4\), the square-output probability is at most \(4/N\),
  and the conditional factor probability is exactly \(1/2\);
- for \(E=N^2-1\), \(K=24\), so the square-output probability is at most
  \(24/N\); the preceding conditional half law does not apply because both
  local kernel-root images are trivial.

Thus a quasipolynomial bank of independent full lifts has negligible direct
one-row success on this family.

## Theorem B — Principal-lift exact law and exact second-root equivalence

Fix a unit \(a\bmod N\), fix one integer lift \(a_0\), and vary the complete
principal fibre

\[
A_t=a_0+tN\pmod{N^2},\qquad t\bmod N.
\]

Write

\[
[A_t^E]_{N^2}=r+Nh_t,
\qquad
r=[a^E]_N,
\qquad
x=[a^{E/2}]_N.
\]

Then

\[
h_t=h_0+Ea^{E-1}t\pmod N.
\]

The slope is a unit, so the \(N\) lift digits are all distinct.  Exactly four
members of the fibre are exact integer squares.  Exactly two of those four
squares have a non-global normalized root relative to \(x\).  Therefore

\[
\Pr_t([A_t^E]_{N^2}\text{ is an exact square})=\frac4N,
\qquad
\Pr_t(\text{one-row P66 factor})=\frac2N.
\]

More strongly, locating either successful square digit is equivalent to
finding a second, mixed square root of \(r\bmod N\):

- a successful square \(s^2\) gives a factor from \(\gcd(s\pm x,N)\);
- given the factorization of \(N\), CRT constructs the two mixed roots and
  hence the two successful digits.

The free principal-lift coordinate does not make the task easier than the
second-square-root problem.  The fixed canonical section \(t=0\) remains open:
there is no proved upper bound or lower bound for a factor-correlated bias
toward the two successful digits.

### Fixed-past extension

Let \(P>0\) be any value fixed before the fresh lift parameter is sampled.
Assume \(\gcd(P,N)=1\), and let \(X\) be a known unit with

\[
X^2\equiv P\pmod N.
\]

Among the \(N\) principal-lift rows \(B_t=[A_t^E]_{N^2}\), at most two values
of \(t\) can make \(PB_t\) an exact integer square with a non-global
normalized root relative to the supplied root \(Xx\).  Therefore a fresh
uniform lift parameter has the history-wise bound

\[
\Pr_t(PB_t\text{ is a useful exact square}\mid P,\text{ past})\le\frac2N.
\]

This holds for an arbitrary fixed past product \(P\); it does not require
\(P\) itself to be an integer square.  It does not bound a complete P66
kernel that can select among exponentially many past subsets after seeing
the fresh row.

## Theorem C — Canonical scalar duplicates

For canonical bases \(a,b\in\{1,\ldots,N-1\}\) that are units, put

\[
u(a)=[a^E]_{N^2}.
\]

For independent uniform bases,

\[
\Pr[u(a)=u(b)]\le \frac{K}{\varphi(N)}.
\]

If a duplicate has supplied roots \(x_a,x_b\), then \(x_a/x_b\) is a square
root of \(1\bmod N\).  A non-global ratio factors \(N\).

On P209, the per-pair bounds are \(4/\varphi(N)\) for \(E=N-1\) and
\(24/\varphi(N)\) for \(E=N^2-1\).  A quasipolynomial bank therefore has no
duplicate with probability \(1-2^{-\Omega(n)}\).

## Theorem D — Reciprocal-output square-pair bound

For one scalar output

\[
u=[a^E]_{M},
\]

let

\[
v=[u^{-1}]_M=[a^{-E}]_M
\]

be its least positive reciprocal output modulo \(M\).  This is a statement
about the reciprocal of the output modulo \(M\).  It is **not** a statement
about first replacing \(a\) by its canonical inverse modulo \(N\) and then
lifting that new base.

If

\[
uv=R^2
\]

as an exact integer identity, then \(R\) is one of the four square roots of
\(1\bmod M\).  The number of possible successful output values \(u\) is at
most

\[
\sum_{R^2=1\bmod M}\tau(R^2)=2^{o(n)}.
\]

Each fixed output has at most \(K\) canonical base preimages.  On P209, the
probability of this exact two-row square event is \(2^{-n+o(n)}\).  A
quasipolynomial bank is negligible.  If the normalized root is mixed, it
factors \(N\); global roots are decoys.

The analogous pair built from the canonical inverse base modulo \(N\) is not
covered by this theorem.

## Torus notation

Fix a public unit \(D\bmod N\), and let \(D_0=[D]_N\in\{1,\ldots,N-1\}\).
The norm-one torus is

\[
T_D(N)=\{(x,y):x^2-Dy^2=1\bmod N\}.
\]

For a point with \(x\) a unit, define the P66 row

\[
A_y=1+D_0y^2,
\qquad
A_y\equiv x^2\pmod N,
\]

where \(y\in\{0,\ldots,N-1\}\) is canonical.

For \(r\in\{p,q\}\), let

\[
m_r=r-\left(\frac Dr\right),
\qquad
z_r=1+\left(\frac{-D}{r}\right)\in\{0,2\}.
\]

Here \(m_r\) is the local torus order and \(z_r\) counts its points with
\(x=0\).  The clean raw point set has size

\[
H=(m_p-z_p)(m_q-z_q).
\]

## Theorem E — Raw torus one-row and duplicate bounds

Let \((x,y)\) be uniform in the clean raw torus set.

Define

\[
B_D(N)=1+
\left\lfloor
\frac{\log(2N\sqrt{D_0}+1)}{\log(2\sqrt{D_0})}
\right\rfloor.
\]

when \(D_0\) is not an integer square, and define \(B_D(N)=1\) when
\(D_0\) is an integer square.  In the square case, \(A_y\) is an exact square
only for \(y=0\), where \(A_y=1\).  In all cases, at most
\(B_D(N)=O(n)\) canonical \(y\)-values make \(A_y\) an exact
integer square, and

\[
\Pr[A_y\text{ exact square}]\le \frac{4B_D(N)}H.
\]

For two independent clean points, exact equality of the integer rows is
equivalent to equality of their canonical \(y\)-coordinates.  Every admitted
\(y\) has four global \(x\)-values.  Therefore

\[
\Pr[A_{y_1}=A_{y_2}]=\frac4H,
\qquad
\Pr[\text{duplicate with mixed root ratio}]=\frac2H.
\]

On P209, \(H=2^{\Omega(n)}\).  Quasipolynomial one-row and duplicate banks are
negligible.

## Theorem F — Powered torus one-row and duplicate bounds

Power a uniform torus point by a public exponent.  Let the two local image
subgroups have coprime orders \(r_p,r_q\).  Remove points with \(x=0\), and let
\(z'_p,z'_q\in\{0,2\}\) count such points in the two image subgroups.  The
clean powered image has size

\[
H'=(r_p-z'_p)(r_q-z'_q).
\]

Every admitted global \(y\) has fibre size at most two.  Hence

\[
\Pr[A_y\text{ exact square}]\le \frac{2B_D(N)}{H'}.
\]

If both \(r_p,r_q\) are odd, equal \(y\) implies the same powered point, so a
duplicate supplies no new root.  If exactly one local image order is even,
then every admitted global \(y\) has two points, and the two distinct points
have a mixed root ratio.  In that case

\[
\Pr[\text{useful duplicate}]=\frac1{H'}.
\]

For the P208/P209 square exponent \(N^2-1\), the residual image orders in each
P209 orientation are coprime and each retains an exponential private marker.
The same conclusion holds for the numerical-QP signed-power grammar covered
by P209.  In these cases \(H'=2^{\Omega(n)}\), and a quasipolynomial bank is
negligible.  This marker conclusion is not asserted for an arbitrary public
powering exponent.

## Theorem G — Torus inverse-point identity and bound

For \(1\le y<N\), the inverse torus point has canonical coefficient \(N-y\).
Put

\[
C=1-D_0y(N-y).
\]

Then the exact identity

\[
\boxed{
A_yA_{N-y}=C^2+D_0N^2
}
\]

holds, and \(C\equiv x^2\pmod N\).

If \(A_yA_{N-y}=R^2\), then

\[
(R-C)(R+C)=D_0N^2.
\]

Consequently at most \(2\tau(D_0N^2)=2^{o(n)}\) canonical \(y\)-values can
produce an exact square.  The raw clean probability is at most

\[
\frac{8\tau(D_0N^2)}H,
\]

and the powered coprime-image probability is at most

\[
\frac{4\tau(D_0N^2)}{H'}.
\]

The raw bound is \(2^{-\Omega(n)}\) on P209.  The powered bound is
\(2^{-\Omega(n)}\) in the P208/P209 square-exponent and covered signed-power
cases specified in Theorem F.  Both remain negligible after
quasipolynomial repetition.
The normalized root \(R/C\bmod N\) is a square root of \(1\); it factors when
it is non-global.

## Exact boundary

These theorems rigorously remove the following simple bridges on P209:

- one exact-square row;
- a repeated exact row;
- the scalar modulo-\(N^2\) reciprocal-output pair;
- a torus point paired with its inverse.

They do not remove:

1. a nonduplicate dependency between unrelated scalar-lift rows, including
   an unrelated two-row pair;
2. a nonduplicate dependency between unrelated torus rows, including an
   unrelated two-row pair;
3. dependencies that mix the two source arms;
4. the possible factor-correlated bias of the fixed canonical lift section
   \(t=0\);
5. the canonical-inverse-base pair modulo \(N\), which is different from the
   reciprocal-output pair modulo \(N^2\).

P209 controls source-group sizes through its private order markers.  It does
not control the ordinary prime-factor parity rows of general products of
distinct integers \(A_y\) or \([a^E]_{N^2}\).  Therefore it is not a
route-killer for the full P66 decoder.

## Research meaning

The positive fact is exact: whenever one of these sources yields an integer
square with a second normalized root, factoring is immediate.  The negative
fact is also exact: all currently exposed one-row, duplicate, and inverse-pair
ways to obtain such a square are exponentially sparse on P209.

The surviving problem is narrow.  A useful P66 bridge must use a genuinely
nonduplicate integer relation outside the named reciprocal and inverse-point
pairs, or prove a special bias in the canonical section.  This packet gives
no all-input factoring algorithm and no quasipolynomial success theorem.
