# F92 hostile proof audit

## Verdict: PASS

I audited RESULT.md at pinned SHA-256

    6c9d9166ca335d115fab18bef6c7c7d90a4bafd7aee3789a071618f6a3f918c0

The digest matches. I did not read an F92 reconstruction artifact or a later
durable-state entry. I ran no research computation and no web search.

I found no mathematical defect in the quotient, valuation, stable-image,
puncture, complexity, Dirichlet-family, or fixed-example claims.

The feedback interpretation is valid with the candidate's explicit
conditions: the successful generators of \(S\) must be retained, feedback
must be on the no-factor branch, and the state under discussion must be its
multiplicative subgroup of units. The theorem does not cover a state that
discards those generators, non-multiplicative side information, or a branch
that has already exposed a nonunit and therefore a factor.

## 1. The arithmetic simplification

From

\[
p-1=gA,\qquad q-1=gB,
\]

one gets

\[
N-1=(gA+1)(gB+1)-1
=g(gAB+A+B).
\]

Thus

\[
\frac Eg=gAB+A+B.
\]

Modulo \(A\), this is congruent to \(B\); modulo \(B\), it is congruent to
\(A\). Since \(g\) is the full gcd of \(p-1\) and \(q-1\),

\[
\gcd(A,B)=1,
\]

and therefore

\[
\gcd(A,E/g)=\gcd(B,E/g)=1.
\]

Because \(E=g(E/g)\), a prime divides both \(A\) and \(E\) if and only if it
divides both \(A\) and \(g\). The same holds for \(B\). Hence the statement
that the transient primes of \(A\) or \(B\) are precisely their primes
already present in \(g\) is exact. Multiplicities need not match: repeated
\(E\)-powers remove the entire primary component whenever the prime occurs
in \(E\).

## 2. The quotient above the powered rectangle

The local group at \(p\) is cyclic of order \(p-1=gA\). Also,

\[
\gcd(p-1,E)
=
\gcd(p-1,q-1)
=g,
\]

using \(E=q(p-1)+(q-1)\). Therefore its \(E\)-power image is the unique local
subgroup of order \(A\), and the quotient by that image is cyclic of order
\(g\). The symmetric statement holds at \(q\).

The full powered image \(S=G^E\) is the product of those local images.
Consequently

\[
G/S\cong C_g\times C_g.
\]

Since \(p\equiv q\equiv1\pmod g\),

\[
g\mid pq-1=E.
\]

Now let \(S\le K\le G\). The quotient \(K/S\) embeds into \(G/S\), so its
exponent divides \(g\), and hence divides \(E\). Thus

\[
(K/S)^E=1.
\]

Equivalently, every \(x\in K\) satisfies \(x^E\in S\). Powering the
inclusions gives the exact sandwich

\[
S^E\le K^E\le G^E=S.
\]

All quotient claims in Theorem 1 follow.

## 3. Scope of the canonical-feedback supergroup claim

On a distinct-prime semiprime, any exposed residue that is not a unit gives
a proper gcd unless it is zero; a canonical nonzero block is therefore a
unit on the no-factor branch. If the successful source generators of \(S\)
are retained, adjoining any such feedback blocks produces a multiplicative
subgroup \(K\) satisfying

\[
S\le K\le G.
\]

Theorems 1 and 2 then apply regardless of how the new units were obtained.
The algorithm does not need to know that the original pair generated \(S\);
that fact is a promise used by the proof.

This does not prove a statement about literally every possible data
structure called “feedback.” It does not constrain additive statistics,
integer magnitudes, provenance, or other side information. It also does not
apply if the algorithm discards enough original generators that its current
multiplicative subgroup no longer contains \(S\). The candidate limits its
claim to the retained, block-generated supergroup, so no overreach remains.

## 4. Exact stable image after \(n\) rounds

Set

\[
n=\lceil\log_2(N+1)\rceil.
\]

If \(\ell^v\mid p-1\), then

\[
\ell^v\le p-1<N+1\le2^n.
\]

Since \(\ell\ge2\), this implies \(v\le n-1\). The same bound holds for
every primary component of \(q-1\).

If \(\ell\mid E\), then

\[
v_\ell(E^n)=n\,v_\ell(E)\ge n,
\]

so the \(E^n\)-power map kills the entire \(\ell\)-primary component of
both local unit groups. If \(\ell\nmid E\), powering by \(E^n\) is an
automorphism on that primary component.

It follows that the local orders of \(G^{E^n}\) are the largest divisors of
\(p-1\) and \(q-1\) coprime to \(E\). Since \(g\mid E\), the \(g\)-part
contributes nothing. These orders are exactly

\[
A_*=A_{\perp E},
\qquad
B_*=B_{\perp E}.
\]

Finite-field multiplicative groups have unique subgroups of each divisor
order, so this is an equality with the declared CRT subgroup, not only an
abstract isomorphism:

\[
G^{E^n}=T.
\]

Starting from \(S\), whose local orders are \(A,B\), gives the same result:

\[
S^{E^n}=T.
\]

Powering \(S\le K\le G\) now yields

\[
T=S^{E^n}\le K^{E^n}\le G^{E^n}=T,
\]

and hence

\[
K^{E^n}=T.
\]

The argument includes all valuation multiplicities and all primes,
including \(2\). Since \(A_*\mid A\), \(B_*\mid B\), and \(\gcd(A,B)=1\),
the stable local orders remain coprime.

## 5. Public normalization cost

For an abelian group, the power map is a homomorphism. If public generators
generate \(K\), their \(E\)-th powers generate \(K^E\). Repeating this
operation \(n\) times produces generators for

\[
K^{E^n}.
\]

The algorithm need not construct the integer \(E^n\). It performs \(n\)
rounds, each using the public \(O(\log N)\)-bit exponent \(E=N-1\).
Repeated squaring is polynomial per generator per round, and
\(n=O(\log N)\). Thus the total bit complexity and storage are polynomial
in \(\log N\) and the supplied generator-list encoding.

No local order, valuation, factor, \(A_*,B_*\), or successful source
certificate enters execution. The polynomial-cost statement naturally
requires the retained public generator list itself to have polynomial
encoding length.

## 6. Immediate stability

Assume

\[
\gcd(AB,g)=1.
\]

Section 1 gives

\[
\gcd(AB,E/g)=1,
\]

so

\[
\gcd(AB,E)=1.
\]

Therefore powering by \(E\) is an automorphism of
\(S\cong C_A\times C_B\), and

\[
S^E=S.
\]

The Theorem 1 sandwich becomes

\[
S\le K^E\le S,
\]

which proves

\[
K^E=S
\]

for every \(S\le K\le G\). This is stronger than eventual stability and is
correct as stated.

## 7. The puncture bank on the stable core

By definition, every prime divisor of \(A_*B_*\) is absent from \(E\).
If \(d>0\) has no prime divisor outside the prime support of \(E\), then

\[
\gcd(d,A_*B_*)=1.
\]

The \(d\)-power map is consequently an automorphism on each cyclic local
factor of \(T\). In particular,

\[
x_p^d=1\iff x_p=1,
\qquad
x_q^d=1\iff x_q=1.
\]

It preserves positive-separator status exactly; it cannot create a
separator from a nonseparator.

Repeated \(E\)-powers and exponents obtained by dividing \(E\) by any of its
prime powers have no prime support outside \(E\). They are covered by the
theorem, including the exponent \(1\).

This inertness statement is only about the stable core. Applying a puncture
before normalization can preserve or expose a transient \(E\)-primary
component. The candidate explicitly keeps that route open. Likewise, an
exponent containing a prime from \(A_*B_*\) is outside Theorem 3.

## 8. The Dirichlet family

Fix a numerical bound \(H\). Dirichlet's theorem supplies a prime

\[
p\equiv3\pmod4,
\qquad
p>2H+1.
\]

Then

\[
A=(p-1)/2
\]

is odd and exceeds \(H\). Let \(R\) be the product of the distinct prime
divisors of \(A\). All of those primes are odd.

The congruences

\[
c\equiv3\pmod4,
\qquad
c\equiv2\pmod r\quad(r\mid A)
\]

have a solution modulo \(4R\) by CRT. This class is reduced: its
representatives are odd, and none is divisible by a prime \(r\mid R\).
Dirichlet's theorem therefore supplies infinitely many primes in it. Choose

\[
q>\max(p,2H+1)
\]

and set \(B=(q-1)/2\). Then \(q\ne p\), \(B\) is odd, and \(B>H\).

If a prime \(r\) divided both \(A\) and \(B\), then \(r\) would be odd and

\[
q=2B+1\equiv1\pmod r.
\]

But the selected class has \(q\equiv2\pmod r\), a contradiction. Hence

\[
\gcd(A,B)=1.
\]

Both \(p-1=2A\) and \(q-1=2B\) have exact 2-adic valuation one, so

\[
\gcd(p-1,q-1)=2\gcd(A,B)=2.
\]

Thus \(g=2\). Since \(AB\) is odd,

\[
\gcd(AB,g)=1,
\]

and the immediate-stability result gives

\[
\gcd(AB,E)=1.
\]

This proves the claimed family for every \(H\). Factoring \(A\) to define
the CRT class is proof-side existence data only. The family construction is
not asserted as a factor-free algorithm or as a density theorem.

## 9. Fixed examples

### \(N=4033\)

Here

\[
4033=37\cdot109,
\qquad
g=\gcd(36,108)=36,
\qquad
(A,B)=(1,3).
\]

Since

\[
E=4032
\]

is divisible by \(3\), the stable coprime-to-\(E\) orders are

\[
(A_*,B_*)=(1,1).
\]

The useful order-three first powered image is therefore transient and is
killed by a later \(E\)-power, exactly as claimed.

### \(N=2047\)

Here

\[
2047=23\cdot89,
\qquad
g=\gcd(22,88)=22,
\qquad
(A,B)=(1,4).
\]

Since \(2\mid E=2046\), removing all \(E\)-supported primary components
again gives

\[
(A_*,B_*)=(1,1).
\]

The order-four full-unit powered rectangle is transient. This does not
conflict with the earlier feedback subgroup being killed by its first
\(E\)-power.

### \(N=2773\)

The displayed factorization is exact:

\[
2773=47\cdot59.
\]

Thus

\[
g=\gcd(46,58)=2,
\qquad
(A,B)=(23,29).
\]

Also

\[
E=2772,
\qquad
2772\equiv12\pmod{23},
\qquad
2772\equiv17\pmod{29},
\]

so

\[
\gcd(23\cdot29,2772)=1.
\]

The immediate-stability corollary applies: every supergroup
\(S\le K\le G\) returns to \(S\) after one \(E\)-power.

All fixed-example claims pass.

## 10. Exact scope and corrections

The result applies to a product of two distinct odd primes after the
constant-probability source event has supplied and retained generators of
the full powered rectangle \(S\). For every multiplicative no-factor
feedback supergroup between \(S\) and the full unit group, repeated public
\(N-1\) powers yield the same stable core \(T\).

It does not show that the source event occurred, recognize it, localize an
axis, prove that feedback cannot factor before normalization, constrain
non-multiplicative canonical information, handle a state that no longer
contains \(S\), handle prime powers or composites with more local factors,
or give a hardness result or factoring algorithm.

No theorem correction is required. The only needed reading qualification
is that “every feedback supergroup” means the retained, multiplicative
unit subgroup \(S\le K\le G\) specified in the setup, not every possible
feedback data state.
