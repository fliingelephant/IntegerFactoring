# Blind reconstruction of F172

## Input integrity and verdict

The SHA-256 digest of `STATEMENT.md` is

```text
d2ff244f1fb28e00ba262fdb89cd5a23b7b75954586bfb998ffd188db4a8ed9f
```

**Verdict: valid as stated, subject to its explicit common-order scope.**

The construction, the four shifted-gcd bounds, the torus-order bounds, the
constant lcm bound, and the bit-length claim all follow. The important scope
condition is that an order is required to be the same exact order in both
local groups. The proof does not bound the global order of an arbitrary CRT
element when its two local orders are different. This is consistent with the
statement's exact boundary.

No mathematical computation was used.

## 1. Factorization data and the CRT class

Let (p>3) be prime with (p\equiv1\pmod 3), and write

\[
p^2-1=2^u3^vM,\qquad \gcd(M,6)=1.
\]

Since (3\mid p-1), we have (v\geq1). Since (p) is odd, (p^2\equiv1
\pmod 8), so (u\geq3), although only the displayed factorization is
needed for most of the proof.

The moduli (8,p,3^v,M) are pairwise coprime:

- (p) is odd and (p\ne3);
- (p\nmid p^2-1), hence (p\nmid 3^vM);
- (M) is coprime to (6), hence to both (8) and (3^v).

Each prescribed residue is a unit for its modulus:

\[
\gcd(3,8)=\gcd(1,p)=\gcd(4,3^v)=\gcd(2,M)=1.
\]

Thus CRT gives a unique class (a_p\pmod {H_p}), where

\[
H_p=8p3^vM,
\]

and this class is reduced. If (M=1), the fourth component is vacuous and
the same conclusion holds.

Linnik's theorem therefore applies to this progression. In its uniform
form, there are absolute constants (C,L_0) such that the progression
contains a prime (q) with

\[
q\le C H_p^{L_0}=H_p^{O(1)}.
\]

This establishes both the existence of (q) and the claimed absoluteness of
the exponent and implicit constants.

## 2. Why (q>2p)

The congruence (q\equiv1\pmod p) gives

\[
q=1+kp
\]

for an integer (k). Positivity and primality of (q) rule out (k\le0).
Both (p) and (q\equiv3\pmod8) are odd, so (kp=q-1) is even and (k)
is even.

If (k=2), then, because (p\equiv1\pmod3),

\[
q=2p+1\equiv0\pmod3.
\]

But (q\equiv4\pmod{3^v}) implies (q\equiv1\pmod3). This is a
contradiction. Hence the positive even integer (k) is at least (4), and
in particular (q>2p).

## 3. Odd parts of all four shifted gcds

Every odd prime divisor of either (p-1) or (p+1) divides (3^vM).

First consider a prime \(\ell\mid M\). The congruence (q\equiv2\pmod M)
gives

\[
q-1\equiv1\pmod\ell,
\qquad
q+1\equiv3\pmod\ell.
\]

Because \(\ell\ne3\), it divides neither (q-1) nor (q+1). Thus no odd
prime from (M) occurs in any shifted gcd.

For the prime (3), the congruence (q\equiv4\pmod{3^v}) gives

\[
3\mid q-1,
\qquad
3\nmid q+1.
\]

The common power of (3) in (p^2-1) and (q-1) is exactly (3). If
(v=1), this follows because (p^2-1) itself has only one factor of (3).
If (v\ge2), then (q-1\equiv3\pmod{3^v}), so
(v_3(q-1)=1). Moreover (p\equiv1\pmod3), so (3\mid p-1) and
(3\nmid p+1). Consequently:

- the odd part of (gcd(p-1,q-1)) is exactly (3);
- the other three shifted gcds have odd part (1).

This also checks the edge case (v=1), where the residue (4\pmod3) does
not by itself determine (v_3(q-1)), but the exponent available from
(p^2-1) already limits the gcd to one factor of (3).

## 4. Two-adic parts and the four gcds

From (q\equiv3\pmod8),

\[
v_2(q-1)=1,
\qquad
v_2(q+1)=2.
\]

Since (p) is odd, both (p-1) and (p+1) are even. Exactly one has
2-adic valuation (1), and the other has valuation at least (2).
Combining this with the odd-part analysis gives

\[
\gcd(p-1,q-1)=2\cdot3=6,
\]

\[
\gcd(p+1,q-1)=2,
\]

and

\[
\gcd(p-1,q+1)=2^{\min(v_2(p-1),2)}\in\{2,4\},
\]

\[
\gcd(p+1,q+1)=2^{\min(v_2(p+1),2)}\in\{2,4\}.
\]

More precisely, the two gcds involving (q+1) are correlated: one is (2)
and the other is (4). If (p\equiv1\pmod4), they are respectively (4)
and (2); if (p\equiv3\pmod4), they are respectively (2) and (4).
The weaker set-valued claims in the statement therefore hold.

## 5. Infinitude and distinctness

Dirichlet's theorem gives infinitely many primes (p\equiv1\pmod3). For
each such (p), choose a prime (q) supplied above. Since (q>2p), (p)
is the smaller prime factor of (N=pq). If two constructed semiprimes were
equal, unique factorization and the fact that (p) is the smaller factor
would force their values of (p) to be equal. Thus the infinitely many
choices of (p) produce infinitely many distinct semiprimes.

## 6. Ordinary common orders

The group of units modulo a prime (r) has order (r-1). If one ordinary
unit has exact order (A) modulo both (p) and (q), Lagrange's theorem
gives

\[
A\mid p-1,
\qquad
A\mid q-1.
\]

Hence

\[
A\mid\gcd(p-1,q-1)=6.
\]

The equality of the two local exact orders is essential here. An arbitrary
unit modulo (N) can have different local orders (A_p,A_q), and its order
modulo (N) is (operatorname{lcm}(A_p,A_q)), which this argument does not
bound by (6).

## 7. Quadratic norm-one torus orders

Let (r) be either (p) or (q), let (D) be a unit modulo (r), and put
(epsilon_r=(D/r)\in\{+1,-1\}). The quadratic etale algebra determined by
(D) is split when (epsilon_r=+1) and is the field
(\mathbb F_{r^2}) when (epsilon_r=-1).

- In the split case, its norm-one group is isomorphic to
  (\mathbb F_r^\times) and has order (r-1).
- In the nonsplit case, the norm map
  (\mathbb F_{r^2}^\times\to\mathbb F_r^\times) is surjective, so its
  kernel has order ((r^2-1)/(r-1)=r+1).

Thus the local norm-one torus has order

\[
r-\epsilon_r.
\]

If a torus point has the same exact order (B) in both local tori, then

\[
B\mid\gcd(p-\epsilon_p,q-\epsilon_q).
\]

The four gcd results therefore imply

\[
\begin{array}{c|c|c}
(\epsilon_p,\epsilon_q)&
\gcd(p-\epsilon_p,q-\epsilon_q)&\text{consequence}\\ \hline
(+1,+1)&6&B\mid6\\
(+1,-1)&\{2,4\}&B\mid4\\
(-1,+1)&2&B\mid2\\
(-1,-1)&\{2,4\}&B\mid4.
\end{array}
\]

In the set-valued rows, writing (B\mid4) is valid even when the actual gcd
is (2).

For the squarefree semiprime (N=pq) and unit (D), the Jacobi symbol is

\[
\left(\frac DN\right)
=\left(\frac Dp\right)\left(\frac Dq\right)
=\epsilon_p\epsilon_q.
\]

Therefore Jacobi symbol (-1) permits exactly the two mixed orientations.
Their common-order capacities divide (4) and (2), respectively.

## 8. The constant lcm capacity

For the ordinary state, (A\mid6). For the two Jacobi-minus-one torus
orientations, one common order divides (4), and the other divides (2).
Consequently

\[
\operatorname{lcm}(A,B_+,B_-)
\mid\operatorname{lcm}(6,4,2)=12.
\]

Hence the displayed lcm is at most (12). The same upper bound remains true
even if states from all four torus orientations, or arbitrarily many
discriminants in those orientations, are included: every such order divides
one of (6,4,2), and adjoining more divisors of these numbers cannot enlarge
the lcm beyond (12).

In particular, a dual modulus (L=\operatorname{lcm}(A,B)) assembled from
one ordinary common order and one torus common order satisfies (L\le12).
Again, this is a common-order statement; it does not bound a modulus built
from unequal local orders by taking their global lcm.

## 9. Size and trial-hardness

From the defining factorization,

\[
3^vM=\frac{p^2-1}{2^u}<p^2.
\]

Therefore

\[
H_p=8p3^vM<8p^3.
\]

Linnik's bound now gives (q=p^{O(1)}), with a uniform absolute exponent.
Together with (q>2p), this yields constants (c_1,c_2>0) such that, for
all sufficiently large constructed members,

\[
c_1\log p\le \log N\le c_2\log p.
\]

For

\[
n=\lceil\log_2(N+1)\rceil,
\]

the ceiling changes this only by an additive constant. Hence

\[
\log p=\Theta(n),
\qquad
p=2^{\Theta(n)}.
\]

Since (q>2p), both prime factors are exponential in (n). Equivalently,
for every fixed (C), only finitely many constructed members can have either
factor at most (n^C). This proves trial-hardness in the stated bit-length
sense.

Under the standard meaning of a fixed quasipolynomial,
(Q(n)=\exp((\log n)^{O(1)})=2^{o(n)}). Also

\[
\sqrt N>\sqrt2\,p=2^{\Theta(n)}.
\]

It follows that

\[
\frac{\sqrt N}{Q(n)}\longrightarrow\infty
\]

along the family. In particular it eventually exceeds (12), while the
dual common-order modulus never does. Thus that modulus cannot reach the
stated terminal threshold for any fixed quasipolynomial (Q).

## 10. Counterexample and quantifier audit

The following possible failure points do not invalidate the theorem:

1. **CRT reducedness.** It holds componentwise because the four CRT residues
   are units and the moduli are pairwise coprime.
2. **A too-small Linnik prime.** The simultaneous congruences force the
   multiplier in (q=1+kp) to be a positive even integer other than (2),
   so every prime in the progression, not merely a selected least prime,
   satisfies (q>2p).
3. **An omitted odd factor in a shifted gcd.** Every odd divisor available
   from (p^2-1) lies in (3^vM). The residue modulo (M) removes all odd
   primes other than (3), and the residue modulo (3^v) places exactly one
   common factor (3) only in the ((p-1,q-1)) pair.
4. **A two-adic leak.** The residue (q\equiv3\pmod8) fixes the valuations
   of (q-1) and (q+1) at (1) and (2), so no shifted gcd has a larger
   power of (2) than claimed.
5. **A reversed torus orientation.** The local order is (r-epsilon_r):
   square (D) gives (r-1), and nonsquare (D) gives (r+1). This matches
   all four rows.
6. **Accumulating many constant orders.** Every available common order is a
   divisor of (6), (4), or (2); their lcm, even across many states, is
   a divisor of (12).
7. **Confusing (p) with the input bit length.** The Linnik upper bound is
   needed in addition to (q>2p). Together they make (n=\Theta(\log p)),
   which is what turns (p) and (q) into superpolynomial functions of
   (n).
8. **Overstating balance.** The proof gives (2p<q\le p^{O(1)}). It does not
   prove a bounded ratio (q/p), nor does it prove that (q/p\to\infty).
   Thus “intentionally unbalanced” can only mean that no balanced-family
   guarantee is being asserted.
9. **Overstating the obstruction.** The argument rules out only universal
   termination from growth of exact common-order capacity. It does not rule
   out factoring during alignment, extracting information from unequal local
   capacities, or using non-order information. It is therefore neither a
   factoring lower bound nor a counterexample to a factor-or-growth routine
   whose other branch can succeed.

With these scope restrictions retained, no counterexample or quantifier
failure is present.
