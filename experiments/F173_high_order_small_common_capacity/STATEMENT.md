# F173 candidate — large local order and large quotient capacity can coexist with constant common order

## Status and scope

This is a proof-only interface obstruction. It is not a factoring lower bound.
It is not a claim about which element the deterministic Harvey--Hittmeir
algorithm returns.

The result separates three types of information.

1. A certificate

   \[
   \operatorname{ord}_N(a)>D
   \]

   gives only a lower bound on one global order.
2. A capped factor-first scan can strengthen this to large order in every
   hidden component and large quotient capacity in every hidden component.
3. A supplied exact global order, with its complete factorization, is much
   stronger. Its prime-divisor screens either factor the input or certify one
   exact common local order.

There is an infinite trial-hard semiprime family on which the first two types
of information are simultaneously as large as possible for this framework,
while every ordinary or Jacobi-minus-one torus common order is bounded by an
absolute constant. Thus a large-order output and a P154/F170 capacity return
cannot be substituted for an exact common-order state.

The family is intentionally unbalanced. The high-order elements and torus
points below are supplied existence witnesses. Their construction uses the
hidden factors. The theorem therefore blocks an inference from the stated
interface data. It does not block a source from selecting a more useful
element or factoring while it constructs one.

## Fixed quasipolynomial bound

Put

\[
n=\lceil\log_2(N+1)\rceil
\]

and fix

\[
Q(n)=2^{C(\log_2(n+1))^k}
\tag{1}
\]

for constants \(C>0\) and \(k\ge1\), independent of \(N\). Use the
integer scan cap and Harvey--Hittmeir target \(D\) by

\[
T(n)=\lfloor Q(n)\rfloor,
\qquad D=T(n).
\tag{1a}
\]

For all sufficiently large members of the family constructed below, every
displayed large prime is greater than \(4Q(n)\).

## The semiprime family

There are infinitely many pairs of odd primes \(p<q\) with \(q>2p\) for
which

\[
\gcd(p-1,q-1)=6,
\tag{2}
\]

\[
\gcd(p-1,q+1)\in\{2,4\},
\qquad
\gcd(p+1,q-1)=2,
\tag{3}
\]

and

\[
\gcd(p+1,q+1)\in\{2,4\}.
\tag{4}
\]

In addition, there are distinct odd primes \(r,u,s,t\) such that

\[
r\mid p-1,
\qquad
u\mid p+1,
\qquad
s\mid q-1,
\qquad
t\mid q+1,
\tag{5}
\]

and one absolute constant \(c>0\) such that

\[
\boxed{r,u,s,t\ge 2^{cn}.}
\tag{6}
\]

Consequently both factors exceed every fixed polynomial in \(n\) after a
finite prefix.

## Ordinary high-order witness

Let \(N=pq\) be a sufficiently large member. Choose primitive roots in the
two hidden fields and combine them by CRT to obtain a supplied unit \(a\)
such that

\[
\operatorname{ord}_p(a)=p-1,
\qquad
\operatorname{ord}_q(a)=q-1.
\tag{7}
\]

Grant the ordinary updater its maximal possible exact common-order state
\((g,6)\). Thus \(g\) has exact order six in both hidden fields.

Let

\[
\Lambda_T=\operatorname{lcm}(1,2,\ldots,T(n)).
\]

Then all of the following claims hold.

1. The absolute screen is hard:

   \[
   \gcd(a^{\Lambda_T}-1,N)=1.
   \tag{8}
   \]

2. Every capped relative-order screen is hard:

   \[
   \gcd(a^{6e}-1,N)=1
   \qquad(1\le e\le T(n)).
   \tag{9}
   \]

3. The quotient fingerprint \(a^6\) has local orders

   \[
   \frac{p-1}{6},
   \qquad
   \frac{q-1}{6}.
   \tag{10}
   \]

   Hence a P154 breadth-first table with cap \(T(n)\) stores \(T(n)+1\)
   values that are distinct in both hidden fields. It returns only the
   capacity certificate

   \[
   |\langle g,a\rangle_p|,
   |\langle g,a\rangle_q|
   \ge 6(T(n)+1).
   \tag{11}
   \]

4. Every equality, inverse-equality, and signed pair-product screen in the
   short power bank

   \[
   \{a^e:-T(n)\le e\le T(n)\}
   \]

   is null, apart from a literal global equality.

5. The public signed \(N\pm1\) screens, and their multipliers through the
   cap, are null:

   \[
   \gcd(a^{j(N-1)}\pm1,N)
   =\gcd(a^{j(N+1)}\pm1,N)=1
   \quad(1\le j\le T(n)).
   \tag{12}
   \]

6. The public \((N-1)\)-power has coprime local orders

   \[
   A=\frac{p-1}{6},
   \qquad
   B=\frac{q-1}{6},
   \qquad
   \gcd(A,B)=1.
   \tag{13}
   \]

   Both contain an exponential prime component. Uniform powers hit exactly
   one identity axis with density

   \[
   \frac1A+\frac1B-\frac2{AB}
   \le \frac1r+\frac1s
   =2^{-\Omega(n)}.
   \tag{14}
   \]

Thus the ordinary channel has high local order, high quotient capacity, a
full coprime-order rectangle after the public power, and exponentially small
direct axis density. Its largest exact common-order state still has order at
most six.

## Two Jacobi-minus-one torus witnesses

For each \(\epsilon\in\{+1,-1\}\), choose a unit discriminant
\(D_\epsilon\) with

\[
\left(\frac{D_\epsilon}{p}\right)=\epsilon,
\qquad
\left(\frac{D_\epsilon}{q}\right)=-\epsilon.
\tag{15}
\]

Its Jacobi symbol is minus one. The local norm-one groups have orders

\[
R_{p,\epsilon}=p-\epsilon,
\qquad
R_{q,\epsilon}=q+\epsilon.
\tag{16}
\]

Choose local primitive torus points and combine their two coordinates by CRT
to obtain a supplied global point \(U_\epsilon\) with these exact local
orders.

Put

\[
b_+=\gcd(p-1,q+1)\in\{2,4\},
\qquad
b_-=\gcd(p+1,q-1)=2.
\tag{17}
\]

Grant each torus updater its maximal exact common-order state of order
\(b_\epsilon\). Then the torus analogues of (8)--(12) hold:

- the absolute \(\Lambda_T\) screen is one;
- every relative return through \(T(n)\) is one;
- the fingerprint \(U_\epsilon^{b_\epsilon}\) has local orders

  \[
  \frac{R_{p,\epsilon}}{b_\epsilon},
  \qquad
  \frac{R_{q,\epsilon}}{b_\epsilon},
  \tag{18}
  \]

  both larger than \(T(n)\);
- capped coefficient-equality search returns only capacity;
- the signed short-power screens and every signed
  \(j(N\pm1)\) screen for \(1\le j\le T(n)\) are null.

Every torus equality and identity screen here uses the F170 joint-coordinate
test. For points \(X=x_0+x_1w\) and \(Y=y_0+y_1w\), this means

\[
\gcd(N,x_0-y_0,x_1-y_1),
\]

and the analogous joint gcd against \(\pm1\). No claim is made that each
one-coordinate gcd is one.

The two local orders in (18) are coprime. For \(\epsilon=+1\), they retain
the large primes \(r,t\). For \(\epsilon=-1\), they retain \(u,s\).
The direct identity-axis density is therefore \(2^{-\Omega(n)}\) in both
torus channels.

## Consequence for the dual ordinary/torus updater

Every exact ordinary common order divides six. Every exact
Jacobi-minus-one torus common order divides four in one orientation and two
in the other. Even if the updater receives maximal exact states in all three
channels,

\[
\boxed{
\operatorname{lcm}(A_{\rm ordinary},B_+,B_-)\le12.
}
\tag{19}
\]

This is exponentially below the F170 terminal threshold
\(\sqrt N/Q(n)\). At the same time, every supplied high-order witness sends
the QP factor-first and quotient-closure decoders to their hard-capacity
branches.

Therefore

\[
\boxed{
\text{large local order + large local quotient capacity}
\not\Rightarrow
\text{a useful exact common-order modulus}.
}
\tag{20}
\]

The implication fails even with simultaneous ordinary and both
Jacobi-minus-one torus channels.

## Why a factored exact order is different

For the ordinary witness, the exact global order is

\[
m=\operatorname{lcm}(p-1,q-1)
=\frac{(p-1)(q-1)}6.
\tag{21}
\]

If \(m\) and its complete factorization are supplied, the prime-divisor
screen at \(r\) gives

\[
\gcd(a^{m/r}-1,N)=q.
\tag{22}
\]

The analogous screen at the large prime present on only one torus side also
factors \(N\). Thus F173 does not obstruct P150 or the exact-order branch of
an instrumented Harvey--Hittmeir run. It obstructs only the replacement of a
factored exact order by a lower-bound certificate or a capacity lower bound.

## Exact exclusions

F173 does not prove any of the following claims.

- The deterministic Harvey--Hittmeir algorithm outputs the displayed
  witness on this family.
- A QP algorithm cannot use the actual integer residue or torus coordinates
  in another way.
- Cross-discriminant algebra, canonical integer refinement, retained exact
  relations, or normalized-root decoding is inert.
- Every QP exponent menu is null.
- Balanced semiprimes have the same obstruction.
- Integer factoring requires super-QP time.

The theorem closes one interface inference only: high-order and capacity
certificates do not themselves supply the exact modulus required by the
factor-first lcm construction or the F170 CRT terminal rule.
