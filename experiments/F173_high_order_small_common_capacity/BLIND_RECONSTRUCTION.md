# F173 blind reconstruction

## Audit boundary and verdict

- Expected SHA-256 of STATEMENT.md:
  0dd00f380a3aa5ddf83dbbedbe10942565b0da2ef786223c80a1fe9c08c60296.
- Observed SHA-256:
  0dd00f380a3aa5ddf83dbbedbe10942565b0da2ef786223c80a1fe9c08c60296.
- The hashes match.
- This reconstruction used only STATEMENT.md inside the F173 directory.
- No experimental or numerical computation was used. The only machine operation
  was the required file-hash verification.

**Verdict: verified.** The family exists, all stated ordinary and torus
screens reach their hard-cap branches, all three common-order channels stay
bounded by constants, and the stated scope restrictions are necessary and
correct.

## 1. Construction of the prime family

I use the following standard form of Linnik's theorem. There are absolute
constants \(K>0\) and \(L\geq 1\) such that every reduced residue class
\(a\pmod M\) contains a prime at most \(K M^L\).

Let \(X\) tend to infinity. By Bertrand's postulate, choose distinct odd
primes

\[
 X<r<2X,\qquad 2X<u<4X.
\]

Choose the simultaneous residue class

\[
 p\equiv13\pmod {168},\qquad
 p\equiv1\pmod r,\qquad
 p\equiv-1\pmod u.
\tag{A1}
\]

The moduli are pairwise coprime for large \(X\). The CRT class is reduced:
\(13\) is coprime to \(168\), and \(1,-1\) are units modulo \(r,u\).
Linnik therefore supplies a prime \(p\) in this class with

\[
 p\leq K(168ru)^L\leq K_1X^{2L}.
\tag{A2}
\]

Also \(p>r,u\). The first assertion follows from \(p\equiv1\pmod r\).
For the second, a positive prime below \(u\) that is \(-1\pmod u\) would be
\(u-1\), an even integer larger than two.

Again by Bertrand's postulate, choose

\[
 2p<s<4p,\qquad 4p<t<8p
\tag{A3}
\]

with \(s,t\) prime. Put

\[
 M_0=\operatorname{lcm}(p-1,p+1)=\frac{p^2-1}{2}.
\]

Now impose

\[
 \begin{aligned}
 q&\equiv7 &&\pmod {p-1},\\
 q&\equiv3 &&\pmod {p+1},\\
 q&\equiv1 &&\pmod s,\\
 q&\equiv-1&&\pmod t.
 \end{aligned}
\tag{A4}
\]

The first two congruences are compatible because their residues agree modulo
\(\gcd(p-1,p+1)=2\). The primes \(s,t\) exceed \(p+1\), so they are coprime
to \(M_0\) and to one another.

It remains important that this CRT class is reduced. From
\(p\equiv13\pmod {168}\),

\[
 p\equiv6\pmod7,\qquad p\equiv1\pmod3.
\]

Consequently

\[
 \gcd(7,p-1)=1,\qquad \gcd(3,p+1)=1.
\]

Thus the first two residues are units on \(M_0\), and the last two are units
modulo \(s,t\). Linnik applies to the reduced class modulo \(M_0st\) and
gives a prime \(q\) with

\[
 q\leq K(M_0st)^L<K(16p^4)^L=K_2p^{4L}.
\tag{A5}
\]

Since \(q\equiv1\pmod s\) and \(q\ne1\), one has
\(q>s>2p\). In particular \(p<q\), as required.

### The four shifted gcds

The fixed congruence \(p\equiv13\pmod {168}\) gives

\[
 6\mid p-1,\qquad v_2(p-1)=2,\qquad v_2(p+1)=1.
\tag{A6}
\]

Using (A4),

\[
\begin{aligned}
\gcd(p-1,q-1)&=\gcd(p-1,6)=6,\\
\gcd(p-1,q+1)&=\gcd(p-1,8)=4,\\
\gcd(p+1,q-1)&=\gcd(p+1,2)=2,\\
\gcd(p+1,q+1)&=\gcd(p+1,4)=2.
\end{aligned}
\tag{A7}
\]

This proves (2)--(4), in fact with the definite values \(6,4,2,2\).
The remaining congruences give

\[
 r\mid p-1,\quad u\mid p+1,\quad
 s\mid q-1,\quad t\mid q+1.
\tag{A8}
\]

The four primes are distinct: \(r,u<p<s<t\), using their defining intervals
and the observations after (A2).

### Exponential size in the input length

Combining (A2) and (A5) gives

\[
 q\leq K_3X^{8L^2}.
\tag{A9}
\]

Hence \(r,u\geq c_0q^{1/(8L^2)}\). Conversely, (A5) gives
\(p\geq c_1q^{1/(4L)}\), so (A3) gives the same type of power lower bound
for \(s,t\). Thus, for some absolute \(\delta>0\) and \(c_2>0\),

\[
 r,u,s,t\geq c_2q^\delta.
\tag{A10}
\]

For \(N=pq\), \(p<q\) implies \(N+1<q^2\). Therefore

\[
 n=\lceil\log_2(N+1)\rceil<2\log_2q+1.
\]

After reducing the constant to absorb the fixed factor in (A10), there is
an absolute \(c>0\) such that, for all sufficiently large \(X\),

\[
 r,u,s,t\geq2^{cn}.
\tag{A11}
\]

Taking \(X\to\infty\) makes \(p>r>X\) unbounded, so this gives infinitely
many distinct pairs. Since

\[
 \log_2 Q(n)=C(\log_2(n+1))^k=o(n),
\]

(A11) also gives \(r,u,s,t>4Q(n)\geq4T(n)\) after a finite prefix.
Finally \(p>r\) and \(q>s\), so both hidden factors exceed every fixed
polynomial in \(n\). This proves all size and trial-hardness assertions.

## 2. A screen lemma

The repeated screen arguments use one elementary fact. Let \(z\) generate a
cyclic group of even order \(M\), and let an odd prime
\(\ell\mid M\) satisfy \(\ell>4T\).

1. \(M\nmid\Lambda_T\), because every prime divisor introduced by
   \(\operatorname{lcm}(1,\ldots,T)\) is at most \(T\).
2. If \(b\mid M\) and \(\ell\nmid b\), then
   \(\operatorname{ord}(z^b)=M/b\), which is larger than \(T\).
3. If \(z^d=1\), then \(\ell\mid d\). If \(z^d=-1\), then
   \(M\mid2d\), and the oddness of \(\ell\) again gives \(\ell\mid d\).
4. If \(\ell\nmid E\), then \(z^{jE}\ne\pm1\) for
   \(1\leq j\leq T\), because either sign would force
   \(\ell\mid jE\).

A comparison of two products of powers from the bank
\(\{z^e:-T\leq e\leq T\}\) reduces to \(z^d=\pm1\) with
\(|d|\leq4T\). The lemma rules out every nonzero such \(d\). For the plus
equality, \(d=0\) is a literal global equality; for the minus equality,
\(d=0\) is impossible over an odd field. This covers equality,
inverse-equality, and signed pair-product tests at once.

## 3. The ordinary channel

The groups \(\mathbb F_p^*\) and \(\mathbb F_q^*\) are cyclic. Choose local
primitive roots and combine them by CRT. The resulting unit \(a\pmod N\)
satisfies

\[
 \operatorname{ord}_p(a)=p-1,\qquad
 \operatorname{ord}_q(a)=q-1.
\tag{A12}
\]

Since both local group orders are divisible by six, local elements of exact
order six also combine to a global state \(g\) of exact order six on both
sides. Conversely, every exact order shared by the two sides divides
\(\gcd(p-1,q-1)=6\). Thus this state is maximal.

The global order of \(a\) is at least \(p-1>r>T=D\), so it supplies the
claimed large-order certificate.

### Absolute, relative, and capacity screens

The prime \(r>T\) divides \(p-1\), while \(s>T\) divides \(q-1\). Neither
local order can divide \(\Lambda_T\). Hence neither hidden prime divides
\(a^{\Lambda_T}-1\), and

\[
 \gcd(a^{\Lambda_T}-1,N)=1.
\]

Put

\[
 A=\frac{p-1}{6},\qquad B=\frac{q-1}{6}.
\tag{A13}
\]

The primes \(r,s\) are larger than three, so \(r\mid A\) and \(s\mid B\).
Because six divides each local order,

\[
 \operatorname{ord}_p(a^6)=A,\qquad
 \operatorname{ord}_q(a^6)=B.
\tag{A14}
\]

Both orders exceed \(T\). Thus \(a^{6e}\ne1\) in either hidden field for
\(1\leq e\leq T\), proving every gcd in (9) is one. The \(T+1\) powers

\[
 1,a^6,a^{12},\ldots,a^{6T}
\]

are distinct in both hidden fields. Since \(a\) itself generates each local
multiplicative group,

\[
 |\langle g,a\rangle_p|=p-1=6A\geq6(T+1),\qquad
 |\langle g,a\rangle_q|=q-1=6B\geq6(T+1).
\tag{A15}
\]

Thus a search stopped after those \(T+1\) values can return capacity but no
collision or relative order. This proves (10)--(11) and the stated
hard-capacity branch.

The screen lemma, with \(r\) on the \(p\)-side and \(s\) on the \(q\)-side,
also proves the complete short-bank assertion. Any nonliteral equality,
inverse equality, or signed pair-product equality would require a nonzero
exponent of absolute value at most \(4T\) to equal \(1\) or \(-1\) on at
least one local side. This is impossible. Literal equalities occur on both
sides and return \(N\), not a factor.

### The signed public powers

Reduction of \(N\pm1\) modulo each local order and (A7) gives

\[
\begin{array}{c|cc}
 &N-1&N+1\\ \hline
\gcd(p-1,\,\mathord\cdot)&6&4\\
\gcd(q-1,\,\mathord\cdot)&6&2
\end{array}
\tag{A16}
\]

For example,
\(\gcd(p-1,N-1)=\gcd(p-1,q-1)\), and the other entries follow in the
same way. The large prime \(r\mid p-1\) and the large prime
\(s\mid q-1\) divide none of \(N-1,N+1\). The screen lemma therefore gives

\[
 a^{j(N-1)}\ne\pm1\pmod p,\pmod q,
 \qquad
 a^{j(N+1)}\ne\pm1\pmod p,\pmod q
\]

for \(1\leq j\leq T\). This proves every gcd in (12) is one, including
the plus-sign cases.

### Coprime rectangle and density

The local order formula for a power and (A16) give

\[
 \operatorname{ord}_p(a^{N-1})=A,\qquad
 \operatorname{ord}_q(a^{N-1})=B.
\tag{A17}
\]

Moreover,

\[
 \gcd(A,B)=\frac{\gcd(p-1,q-1)}6=1.
\tag{A18}
\]

Over one full period \(AB\), the exponent is on the \(p\)-identity axis
exactly \(B\) times and on the \(q\)-identity axis exactly \(A\) times. The
two axes meet once. Hence the fraction on exactly one axis is

\[
 \frac{B-1+A-1}{AB}
 =\frac1A+\frac1B-\frac2{AB}
 \leq\frac1r+\frac1s
 =2^{-\Omega(n)}.
\tag{A19}
\]

This proves (13)--(14) and all ordinary-channel claims.

## 4. The two Jacobi-minus-one torus channels

For each \(\epsilon\in\{+1,-1\}\), select a nonzero quadratic
residue/nonresidue modulo \(p\) with symbol \(\epsilon\), and one modulo
\(q\) with symbol \(-\epsilon\). CRT combines them into a unit
\(D_\epsilon\pmod N\). Its Jacobi symbol is \(-1\).

For a prime \(v\), the norm-one group associated with a unit discriminant
\(D\) is cyclic of order

\[
 v-\left(\frac Dv\right).
\]

In the split case it is isomorphic to \(\mathbb F_v^*\); in the nonsplit
case it is the kernel of the norm map
\(\mathbb F_{v^2}^*\to\mathbb F_v^*\). Therefore the two local orders are

\[
 R_{p,\epsilon}=p-\epsilon,\qquad
 R_{q,\epsilon}=q+\epsilon.
\tag{A20}
\]

Choose a generator on each local side and combine both coordinates by CRT.
This gives the claimed global primitive point \(U_\epsilon\).

By (A7),

\[
 b_+=\gcd(p-1,q+1)=4,\qquad
 b_-=\gcd(p+1,q-1)=2.
\tag{A21}
\]

Local elements of exact order \(b_\epsilon\) combine into a global exact
common-order state. Every common order must divide the gcd in (A21), so the
states are maximal.

For later use, the large primes retained on the two sides are

\[
\begin{array}{c|cc}
\epsilon& p\text{-side}&q\text{-side}\\ \hline
+1&r\mid p-1&t\mid q+1\\
-1&u\mid p+1&s\mid q-1.
\end{array}
\tag{A22}
\]

All four primes exceed \(4T\) and are coprime to \(b_\epsilon\).

### Absolute, relative, capacity, and short-bank screens

Apply the screen lemma on the two local cyclic groups using (A22). Neither
local order divides \(\Lambda_T\), so the absolute joint-coordinate identity
gcd is one. Also

\[
 \operatorname{ord}_p(U_\epsilon^{b_\epsilon})
   =\frac{R_{p,\epsilon}}{b_\epsilon},\qquad
 \operatorname{ord}_q(U_\epsilon^{b_\epsilon})
   =\frac{R_{q,\epsilon}}{b_\epsilon}.
\tag{A23}
\]

Each quotient order contains its designated large prime and is therefore
larger than \(T\). This proves every relative return through the cap is one.
It also makes the first \(T+1\) fingerprint powers distinct in both local
groups. Since \(U_\epsilon\) is locally primitive, each generated local
group has at least \(b_\epsilon(T+1)\) elements. Thus coefficient equality
finds no collision and reaches only its capacity return.

Every short-bank equality or signed product comparison reduces in the group
to \(U_\epsilon^d=\pm1\) with \(|d|\leq4T\). The screen lemma proves that
all nonliteral screens are null on both local sides.

### The signed public powers

The complete local gcd table is

\[
\begin{array}{c|c|cc|c}
\epsilon&\text{local order}&
 \gcd(\text{order},N-1)&\gcd(\text{order},N+1)&
 \text{large prime}\\ \hline
+1&p-1&6&4&r\\
+1&q+1&2&4&t\\
-1&p+1&2&2&u\\
-1&q-1&6&2&s
\end{array}
\tag{A24}
\]

For instance, modulo \(q+1\) one has \(q\equiv-1\), so the two entries in
that row are respectively
\(\gcd(q+1,p+1)=2\) and \(\gcd(q+1,p-1)=4\).
All other entries follow from the same reduction and (A7).

The large prime in the final column divides neither public exponent. The
screen lemma now proves

\[
 U_\epsilon^{j(N-1)}\ne\pm1,
 \qquad
 U_\epsilon^{j(N+1)}\ne\pm1
\]

on either local side for every \(1\leq j\leq T\). Hence all stated signed
joint-coordinate gcds are one.

### Why the joint-coordinate qualification is exact

Write a torus point as \(X=x_0+x_1w\). Over a hidden prime, \(X=Y\) if and
only if both coordinates agree. Consequently

\[
 \gcd(N,x_0-y_0,x_1-y_1)
\]

contains exactly those hidden primes at which the two points agree. The
same statement holds against \(+1=(1,0)\) and \(-1=(-1,0)\). The group
arguments above rule out simultaneous coordinate equality on either local
side. They do not rule out an accidental equality of only one coordinate.
Thus the statement's restriction to the joint-coordinate test is both
sufficient and necessary; no one-coordinate claim has been smuggled into
the proof.

### Coprimality and density

Since \(b_\epsilon\) is the full gcd of the two orders in (A20),

\[
 \gcd\left(
 \frac{R_{p,\epsilon}}{b_\epsilon},
 \frac{R_{q,\epsilon}}{b_\epsilon}
 \right)=1.
\tag{A25}
\]

For \(\epsilon=+1\), these quotients retain \(r,t\). For
\(\epsilon=-1\), they retain \(u,s\). Applying the count in (A19), with
the corresponding pair of quotient orders, gives an exactly-one-axis
density bounded respectively by

\[
 \frac1r+\frac1t
 \quad\text{or}\quad
 \frac1u+\frac1s.
\]

Both bounds are \(2^{-\Omega(n)}\). This proves every torus-order,
capacity, screen, and density claim.

## 5. The simultaneous common-order ceiling

Every exact ordinary common order divides \(6\). Every exact common order
in the \(+1\) torus orientation divides \(4\), and every one in the
\(-1\) orientation divides \(2\). Therefore, even for maximal states,

\[
 \operatorname{lcm}(A_{\rm ordinary},B_+,B_-)
 \mid\operatorname{lcm}(6,4,2)=12.
\tag{A26}
\]

On the other hand, from the definition of \(n\), for all large \(n\),

\[
 \log_2\frac{\sqrt N}{Q(n)}
 \geq \frac{n-2}{2}-C(\log_2(n+1))^k
 =\Omega(n).
\tag{A27}
\]

Thus the terminal threshold is exponentially larger than twelve. Sections
3 and 4 simultaneously show that every supplied high-order witness passes
through all capped factor-first screens without a factor and fills every
quotient table through its cap. The family therefore realizes both sides of
the claimed separation:

\[
 \text{large local order and capped quotient capacity}
 \not\Rightarrow
 \text{a large exact common-order modulus}.
\]

## 6. Why a factored exact order escapes the obstruction

Equations (A13) and (A18) give

\[
 m=\operatorname{lcm}(p-1,q-1)=6AB
   =\frac{(p-1)(q-1)}6.
\tag{A28}
\]

Write \(A=rH\). Since \(\gcd(A,B)=1\), \(r\nmid B\). Then

\[
 \frac mr=6HB.
\]

This exponent is divisible by \(q-1=6B\), but it is not divisible by
\(p-1=6rH\). Since \(a\) is primitive on both sides,

\[
 \gcd(a^{m/r}-1,N)=q.
\tag{A29}
\]

The torus argument is identical. If the local orders are
\(bC,bE\) with \(\gcd(C,E)=1\), and a large prime
\(\ell\mid C\) occurs only on the first side, then the exact global order is
\(bCE\). Dividing it by \(\ell\) leaves a multiple of the second local
order but not of the first. The joint-coordinate identity gcd therefore
returns the second hidden prime.

Complete factorization of the exact global order exposes \(r\), or the
corresponding one-sided torus prime, and makes this prime-divisor screen
available. A lower-bound certificate and a capped capacity certificate do
not expose that exponent. Hence the exact-order branch is not obstructed.

More generally, the statement's introductory exact-order dichotomy is
valid. If \(m\) is an exact global order, then for every prime
\(\ell\mid m\), the gcd at exponent \(m/\ell\) cannot be \(N\), since that
would contradict exactness of \(m\). A nontrivial gcd factors \(N\). If all
such gcds are one, both local orders contain the full prime-power part of
\(m\) for every prime divisor of \(m\), so both local orders equal \(m\).
The screens then certify an exact common local order.

## 7. Scope check

The proof is existential and uses \(p,q\) to select primitive roots,
primitive torus points, discriminants, and CRT combinations. It makes no
claim that a deterministic source returns those witnesses, or that their
construction hides the factors from the constructor.

The argument controls only the listed absolute, relative, short-bank, and
\(j(N\pm1)\) menus through \(T(n)\), plus the quotient-capacity consequence.
It says nothing about arbitrary quasipolynomial exponent menus or other uses
of the actual residue and coordinates. It contains no analysis of
cross-discriminant algebra, integer refinement, retained relations, or
normalized-root decoding. The construction explicitly has \(q>2p\), so it
does not establish a balanced-semiprime analogue. Finally, an interface
counterexample is not a time lower bound for factoring.

These observations verify every exact exclusion in the statement and show
that its conclusion is precisely an interface non-implication, not a
factoring lower bound or an algorithm-output claim.
