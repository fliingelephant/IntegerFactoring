# F72 — a relation quotient escapes the order-three endpoint trap

## Status

Proof-only candidate. No research computation was used. This artifact has not
yet passed a hostile audit or proof-blind reconstruction.

## 1. Result

The order-three endpoint trap is not closed under feeding a relation quotient.
There is an explicit infinite family on which:

1. endpoint products, arbitrary occurrence amplification, canonical reduction,
   canonical inversion, gcd refinement, perfect-power extraction, the direct
   screens, and the complete square decoder remain trapped in one old block;
2. the public quotient of the seed relation is outside that endpoint source;
3. feeding this quotient creates one exact-square relation;
4. its positive root splits \(N\) immediately.

The family can make every prime factor of both the old block and \(N\) exceed
any prescribed bound. Thus no fixed trial-division prepass explains the
escape.

This is a special-family mechanism theorem. It does not give an all-input
sampler or a general factoring algorithm.

## 2. Family and factorization

Let \(s\ge2\) be even. Put

\[
c=3s^2-1,
\qquad
N=c^2+c+1.
\]

Then

\[
N=9s^4-3s^2+1
=(3s^2-3s+1)(3s^2+3s+1). \tag{1}
\]

Write

\[
A=3s^2-3s+1,
\qquad
B=3s^2+3s+1.
\]

Both factors are odd, greater than one, and congruent to \(1\pmod3\).
Their common divisors divide \(B-A=6s\). Since
\(\gcd(A,s)=\gcd(B,s)=1\), and neither factor is divisible by \(2\) or
\(3\), one has

\[
\gcd(A,B)=1. \tag{2}
\]

Thus \(N=AB\) is an odd composite with two coprime nontrivial factors.
Also \(c\equiv2\pmod3\), so \(3\nmid N\).

## 3. Endpoint-only feedback remains trapped

The seed relation is

\[
c\cdot c^2=c^3=1+(c-1)N. \tag{3}
\]

For every prime power \(p^a\Vert N\), the residue of \(c\) has exact order
three. Its order divides three by (3). If \(c\equiv1\pmod p\), then
\(N\equiv3\pmod p\), which would force \(p=3\). This is impossible.

Hence

\[
\langle c\rangle=\{1,c,c^2\}\pmod N \tag{4}
\]

contains no direct sign separator. The displayed integers are their canonical
representatives.

The endpoint list \(c,c^2\) has the one-block gcd-free basis \(\{c\}\).
If \(c\) is not a perfect power, exact perfect-power preprocessing does not
split this block. Every authorized endpoint product is a power of \(c\).
Canonical reduction gives only \(1,c,c^2\); a nontrivial inverse relation
repeats (3). Retaining an oversized raw power gives a relation value
\(c^{3t}\).

Gcd refinement of these powers creates no second block. Every direct sign,
difference, and inverse-pair discriminant screen is trivial or global. For
every rational-square product of relation values, the exponent of \(c\) in
its positive root is divisible by three. The root is therefore \(1\pmod N\),
and the full square-decoder image is \(\{1\}\).

This is the endpoint-only trap. The next section changes the authorized data.

## 4. The quotient-fed relation is an exact square

The public quotient in (3) is

\[
q_0=\frac{c^3-1}{N}=c-1. \tag{5}
\]

Feed \(g=q_0=c-1\) as a new state. Since \(c\equiv2\pmod3\), the integer

\[
w=\frac{c^2-1}{3}
\]

is its canonical inverse modulo \(N\). It satisfies \(1<w<N\). Using
\((c+1)/3=s^2\),

\[
gw
=\frac{(c-1)(c^2-1)}3
=(c-1)^2s^2
=R^2, \tag{6}
\]

where

\[
R=s(c-1)=3s^3-2s.
\]

The new quotient is also explicit:

\[
R^2=1+(s^2-1)N. \tag{7}
\]

The root has opposite local signs because

\[
R-1=(s-1)B,
\qquad
R+1=(s+1)A. \tag{8}
\]

Moreover,

\[
\gcd(s-1,A)=1,
\qquad
\gcd(s+1,B)=1.
\]

Together with (2), this gives the exact factor extraction

\[
\boxed{\gcd(R-1,N)=B,\qquad \gcd(R+1,N)=A.} \tag{9}
\]

Thus one non-endpoint quotient changes the algorithmic state and escapes a
source that arbitrary endpoint occurrence amplification cannot escape.

## 5. Earlier screens can be forced to fail

Assume that no prime at most \(13\) divides \(N\). The direct screens on
\(g=c-1\) fail:

\[
\gcd(g+1,N)=\gcd(c,N)=1,
\]

while any common divisor of \(g-1=c-2\) and \(N\) divides \(7\). The same
holds for \(w\), because \(gw\equiv1\pmod N\).

The inverse-pair difference screen also fails because it reduces to
\(\gcd(g^2-1,N)\).

Put \(d=g-w\). Then

\[
d^2+4\equiv(g+w)^2\pmod N.
\]

Here \(w=s^2g\), so

\[
g+w=g(s^2+1).
\]

The factor \(g\) is a unit modulo \(N\), and every common divisor of
\(s^2+1\) and \(N=9s^4-3s^2+1\) divides \(13\). Therefore the discriminant
screen also returns \(1\). The exact-square screen in (6) is the first
successful declared screen.

## 6. Infinite robust subfamily

Fix \(B\ge13\). Choose a prime

\[
\ell>B,
\qquad
\ell\equiv1\pmod {12}.
\]

Then \(3\) is a quadratic residue modulo \(\ell\). Choose a root
\(r\pmod\ell\) of \(3r^2-1\). Its derivative \(6r\) is nonzero modulo
\(\ell\), so exactly one lift of \(r\) modulo \(\ell^2\) remains a root
modulo \(\ell^2\). Choose a different lift \(a\). Thus

\[
3a^2-1\equiv0\pmod\ell,
\qquad
3a^2-1\not\equiv0\pmod{\ell^2}. \tag{10}
\]

Let \(M_B\) be the product of all primes at most \(B\). The Chinese remainder
theorem gives an infinite arithmetic progression of integers \(s\) satisfying

\[
s\equiv0\pmod {M_B},
\qquad
s\equiv a\pmod{\ell^2}. \tag{11}
\]

Every such \(s\) is even. For each prime \(q\le B\),

\[
c\equiv-1\pmod q,
\qquad
A\equiv B\equiv1\pmod q.
\]

Therefore every prime factor of \(c\) and \(N=AB\) exceeds \(B\). Equation
(10) gives \(v_\ell(c)=1\), so \(c\) is not a perfect power. The endpoint
trap in Section 3 survives trial division through \(B\) and perfect-power
preprocessing, while the quotient-fed square in Section 4 still factors
\(N\).

Taking one larger \(B\) at each stage gives a sequence with growing least
prime factors on both the old block and the target modulus.

## 7. Exact scope

The source operation is the important change:

\[
\text{old endpoint block }c
\quad\longrightarrow\quad
\text{relation quotient }c-1.
\]

The quotient is public and polynomial-time computable from the seed relation,
but it is not an endpoint block or a power of one. It creates new integer
structure and an exact square on this family.

The family is deliberately manufactured. It is recognizable from
\(4N-3=(2c+1)^2\) and \((c+1)/3=s^2\). Equations (1) and (8) are an
explicit algebraic factorization, so no publication-level novelty is claimed
for the identity without a literature review.

The result does not show that arbitrary relation quotients have factor bias.
It does not provide a selector for general \(N\), an inverse-polynomial
success law, or a polynomial-time factoring algorithm for unrestricted odd
composites. It proves only that non-endpoint quotient feedback is a real
escape operation and that the endpoint trap does not extend to it.
