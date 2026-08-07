# F92 — feedback cannot change the stable \(N-1\)-powered core

**Status:** proof-only candidate. No research computation, hostile audit,
proof-blind reconstruction, cross-family audit, human audit, or literature
audit has run. This is a structural boundary for the feedback route. It is
not an axis decoder or a factoring algorithm.

## 1. Closest prior route and material difference

P95 proves that one \(N-1\) power sends any supplied subgroup to a full
rectangle with coprime local orders. P97 proves that two exact bare-\(N\)
samples generate the full powered rectangle with constant probability for a
distinct odd semiprime.

The present result asks what feedback can still change after that P97 source
has succeeded. It proves that every feedback supergroup has the same stable
image under repeated \(N-1\) powers. Thus feedback can add transient
shared-order information and useful unpowered integer representatives, but
it cannot alter the stable coprime-order core through the existing
\(N-1\)-power or puncture bank.

## 2. Setup

Let

\[
N=pq
\]

for distinct odd primes. Put

\[
E=N-1,
\qquad
g=\gcd(p-1,q-1),
\qquad
A=\frac{p-1}{g},
\qquad
B=\frac{q-1}{g},
\]

and

\[
G=(\mathbb Z/N\mathbb Z)^\times,
\qquad
S=G^E.
\]

For a positive integer \(r\), let

\[
r_{\perp E}
\]

denote the largest divisor of \(r\) coprime to \(E\). Define

\[
A_*=A_{\perp E},
\qquad
B_*=B_{\perp E}.
\]

P97 gives

\[
S\cong C_A\times C_B,
\qquad
\gcd(A,B)=1.
\]

Let \(T\le G\) be the CRT product of the unique local subgroups of orders
\(A_*\) and \(B_*\). Thus

\[
T\cong C_{A_*}\times C_{B_*}.
\]

There is also a useful exact simplification:

\[
\boxed{
\gcd(A,E/g)=\gcd(B,E/g)=1.
}
\tag{1}
\]

Indeed,

\[
\frac Eg=gAB+A+B,
\]

whose reductions modulo \(A\) and \(B\) are respectively \(B\) and \(A\).
Thus the transient primes in \(A\) or \(B\) are precisely primes already
present in the shared factor \(g\).

## 3. The feedback quotient is public-annihilated

### Theorem 1

The quotient left above the full powered rectangle is

\[
\boxed{G/S\cong C_g\times C_g.}
\]

In particular, \(g\mid E\). For every subgroup

\[
S\le K\le G,
\]

one has

\[
\boxed{K/S\le C_g\times C_g}
\]

and

\[
\boxed{(K/S)^E=1.}
\]

Also,

\[
\boxed{S^E\le K^E\le S.}
\]

### Proof

The identity

\[
E=q(p-1)+(q-1)
\]

gives

\[
\gcd(p-1,E)=\gcd(p-1,q-1)=g.
\]

The other local identity is symmetric. The \(E\)-power image in the cyclic
group of order \(p-1=gA\) is therefore its unique subgroup of order \(A\);
the local quotient has order \(g\). The \(q\)-side has quotient order \(g\)
as well. CRT gives the first boxed isomorphism. Since \(g\) divides both
\(p-1\) and \(q-1\), it divides \(pq-1=E\).

Every \(K/S\) is a subgroup of \(G/S\). For \(x\in K\), the residue \(x^E\)
lies in \(G^E=S\), so \(E\) annihilates the quotient. Finally, \(S\le K\le
G\) and functoriality of a power image give

\[
S^E\le K^E\le G^E=S.
\]

\(\square\)

This theorem applies after any canonical feedback refinement on the
no-factor branch. Every exposed integer block is then a unit, and retaining
the P97 generators makes its block-generated subgroup a \(K\) with
\(S\le K\le G\).

## 4. Every feedback supergroup has the same stable powered image

### Theorem 2

Let

\[
n=\lceil\log_2(N+1)\rceil.
\]

For every subgroup \(K\) with \(S\le K\le G\),

\[
\boxed{K^{E^n}=T.}
\]

Equivalently, all such feedback supergroups converge to the same stable
rectangle. The two local stable orders are \(A_*,B_*\), which remain
coprime.

### Proof

For a cyclic group of order \(r\), the image under the \(E^n\)-power map has
order

\[
\frac{r}{\gcd(r,E^n)}.
\]

For every prime \(\ell\), the valuation \(v_\ell(p-1)\) is at most \(n-1\).
If \(\ell\mid E\), then \(v_\ell(E^n)\ge n\), so the power removes the full
\(\ell\)-primary component. If \(\ell\nmid E\), that component survives
unchanged. Hence

\[
G^{E^n}\cong C_{A_*}\times C_{B_*}=T.
\]

The same valuation argument starting from the local orders \(A,B\) gives

\[
S^{E^n}=T.
\]

Powering the inclusions \(S\le K\le G\) now gives the subgroup sandwich

\[
T=S^{E^n}\le K^{E^n}\le G^{E^n}=T.
\]

Therefore \(K^{E^n}=T\). Since \(A_*\mid A\) and \(B_*\mid B\), their gcd
is one. \(\square\)

The executable normalization is polynomially bounded. Raise every public
generator to \(E\), repeat this \(n\) times, and retain the resulting
generators. Each modular power uses an \(O(n)\)-bit exponent, and there are
\(n\) rounds. No hidden order or factor is used.

### Immediate-stability corollary

If

\[
\gcd(AB,g)=1,
\]

then (1) gives

\[
\gcd(AB,E)=1,
\qquad
T=S.
\]

In this case, for every \(S\le K\le G\),

\[
\boxed{K^E=S.}
\]

Thus one \(N-1\) power already erases every feedback expansion and returns
the exact original P97 rectangle.

## 5. The existing puncture bank is inert on the stable core

### Theorem 3

Let \(d>0\) have no prime divisor outside those of \(E\). Then

\[
\gcd(d,A_*B_*)=1.
\]

Consequently, the map

\[
x\longmapsto x^d
\]

is an automorphism of \(T\). It preserves both coordinate identity tests:

\[
x_p^d=1\iff x_p=1,
\qquad
x_q^d=1\iff x_q=1.
\]

Thus it cannot turn a nonseparator in \(T\) into a separator.

### Proof

The definition of \(A_*,B_*\) removes every prime dividing \(E\). Hence any
\(E\)-smooth \(d\) is coprime to both stable local orders. Powering by a
unit exponent modulo a finite cyclic order is an automorphism, and the
identity equivalences follow. \(\square\)

This covers every repeated \(N-1\) power and every puncture obtained by
removing prime powers from \(N-1\). Such exponents can decode transient
\(E\)-primary components, but they do not change the stable hard rectangle.

## 6. Stable two-large-order cases exist without a number-theoretic promise

### Theorem 4

For every numerical bound \(H\), there are distinct odd primes \(p,q\) for
which

\[
g=2,
\qquad
A>H,
\qquad
B>H,
\qquad
\gcd(AB,E)=1.
\]

Thus both local orders can be arbitrarily large while the P97 rectangle is
already stable after its first construction.

### Proof

Choose a prime

\[
p\equiv3\pmod4,
\qquad
p>2H+1,
\]

and put \(A=(p-1)/2\). Such primes exist by Dirichlet's theorem. The integer
\(A\) is odd and exceeds \(H\). Let \(R\) be the product of the distinct
prime divisors of \(A\).

By CRT, choose a reduced residue class \(c\pmod{4R}\) satisfying

\[
c\equiv3\pmod4,
\qquad
c\equiv2\pmod r
\quad\text{for every prime }r\mid A.
\]

Dirichlet's theorem supplies infinitely many primes in this class. Choose
one such prime \(q>\max(p,2H+1)\), and put \(B=(q-1)/2\). Then \(B\) is odd
and exceeds \(H\).

If a prime \(r\) divided both \(A\) and \(B\), then \(q\equiv1\pmod r\),
contrary to \(q\equiv2\pmod r\). Hence \(\gcd(A,B)=1\). Because both
\(p-1=2A\) and \(q-1=2B\) have exact 2-adic valuation one,

\[
\gcd(p-1,q-1)=2.
\]

Thus \(g=2\). Since \(AB\) is odd, \(\gcd(AB,g)=1\), and the
immediate-stability corollary gives \(\gcd(AB,E)=1\). \(\square\)

This existence proof uses the prime divisors of \(A\) only to select a
family. It is not an executable factoring step and gives no input-length
density bound.

## 7. Meaning for the feedback route

The theorem does not invalidate canonical feedback. It separates its two
possible effects.

1. Feedback can change the unpowered subgroup \(K\) by exposing integer
   blocks outside \(S\).
2. Feedback can create a useful transient component whose order uses primes
   dividing \(E\).
3. Feedback cannot change \(T\) through repeated \(E\)-power normalization.

Therefore an all-input continuation must do at least one of the following:

- factor from a transient component before it is killed;
- use canonical integer information to localize an axis without only
  applying \(E\)-smooth powers;
- manufacture a public exponent with a prime divisor from one hidden stable
  order; or
- add a non-power decoder that separates the two stable identity kernels.

The third item is order information and cannot be assumed. The theorem makes
no hardness claim about the other items.

The retained examples lie outside the stable hard case. At \(N=4033\),
\((A,B)=(1,3)\) and \(3\mid E\), so the useful order-three image is
transient. At \(N=2047\), \((A,B)=(1,4)\) and \(2\mid E\), so that powered
rectangle is transient as well. These examples verify real operations, but
they do not test feedback against two large stable local orders.

A small exact stable example is

\[
N=2773=47\cdot59,
\qquad
g=2,
\qquad
(A,B)=(23,29).
\]

Here \(\gcd(23\cdot29,2772)=1\), so every feedback supergroup containing
the P97 rectangle returns to that same rectangle after one \(N-1\) power.

## 8. Exact scope

This result is conditional on the P97 pair actually generating \(S\), a
constant-probability event that the algorithm need not recognize in a
Las Vegas reduction. It treats distinct odd semiprimes only. It gives no
axis-localization rule, no feedback progress law, no factoring algorithm,
and no computational lower bound.
