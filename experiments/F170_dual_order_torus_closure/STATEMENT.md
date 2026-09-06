# F170 candidate — dual ordinary/torus order closure and CRT termination

## Status and scope

This is a proof-only candidate for hostile audit. It is not a factoring
algorithm and it is not an all-input source theorem.

P154 gives a complete capped quotient updater for ordinary units. P140
proves that a Jacobi-minus-one discriminant has opposite split/nonsplit
orientations at the two hidden primes, but that the tested direct maps do
not transfer ordinary high order into the nonsplit torus. The result below
does not make that transfer. It keeps one ordinary common-order state and
one torus common-order state as separate public objects.

The torus quotient updater has the same abstract outcomes as P154. The new
arithmetic fact is that the two exact common orders are almost coprime:

\[
 A\mid N-1,\qquad B\mid N+1,\qquad \gcd(A,B)\mid2.
\]

Their least common multiple can therefore grow nearly as their product. A
large enough least common multiple gives a deterministic
quasipolynomial search for a hidden factor. This is a conditional dual-source
progress theorem. No current source is proved to cause one useful closure or
growth event per round.

## 1. Input objects

Let

\[
 N=pq,\qquad 3\le p<q,
\]

where (p,q) are distinct odd primes. Put (R=\mathbb Z/N\mathbb Z).

Let (D\in R^\times) have Jacobi symbol (-1), and define

\[
 A_D=R[w]/(w^2-D),
 \qquad
 T_D(R)=\{a+bw:a^2-Db^2=1\}.
\]

Write

\[
 \epsilon=\left(\frac Dp\right)\in\{+1,-1\}.
\]

Then ((D/q)=-\epsilon). The two local torus groups are cyclic and have
orders

\[
 |T_D(\mathbf F_p)|=p-\epsilon,
 \qquad
 |T_D(\mathbf F_q)|=q+\epsilon.
\tag{1}
\]

The public state contains two exact common-order certificates.

1. An ordinary state ((g,A)), with the complete factorization of (A),
   such that (g) has exact order (A) modulo both (p) and (q).
2. A torus state ((G,B)), with the complete factorization of (B), such
   that (G) has exact order (B) in both local groups in (1).

It also contains a frozen public list (U_1,\ldots,U_t\in T_D(R)), with
complete word provenance, and a quotient cap (C\). Every denominator and
every claimed unit is screened by gcd before use.

Both states can always start at the public element (-1). Then

\[
 A=B=2.
\tag{2}
\]

## 2. The dual orders are orthogonal

Every valid pair of states satisfies

\[
 \boxed{A\mid N-1,\qquad B\mid N+1,\qquad \gcd(A,B)\mid2.}
\tag{3}
\]

More precisely,

\[
 p\equiv q\equiv1\pmod A,
\tag{4}
\]

and

\[
 p\equiv\epsilon\pmod B,
\qquad
 q\equiv-\epsilon\pmod B.
\tag{5}
\]

Put

\[
 h=\gcd(A,B),\qquad L=\operatorname{lcm}(A,B)=\frac{AB}{h}.
\tag{6}
\]

For each sign (e\in\{+1,-1\}), the generalized CRT system

\[
 x\equiv1\pmod A,
 \qquad
 x\equiv e\pmod B
\tag{7}
\]

is consistent and gives one public residue class modulo (L). The hidden
prime (p) belongs to the class with (e=\epsilon). This remains correct
when (A) and (B) are even: then (h=2) after the initialization (2),
and both differences (1-e) are divisible by (h).

There are also orientation-free sum congruences

\[
 \boxed{p+q\equiv2\pmod A,
 \qquad p+q\equiv0\pmod B.}
\tag{8}
\]

They define one public residue class modulo (L). For the gap
(\gamma=q-p),

\[
 \boxed{\gamma\equiv0\pmod A,
 \qquad \gamma\equiv-2\epsilon\pmod B.}
\tag{9}
\]

Thus (9) supplies two public gap classes and an independent verifier. The
sum class (8) is sharper for a balanced semiprime because it does not branch
on the hidden orientation.

## 3. Exact CRT factor threshold

Let (Q(n)\ge1) be a fixed quasipolynomial function of

\[
 n=\lceil\log_2(N+1)\rceil.
\]

### 3.1 Arbitrary distinct semiprimes

Enumerate the two classes (7) in the interval

\[
 3\le x<\sqrt N.
\]

There are at most

\[
 2\left(\frac{\sqrt N}{L}+1\right)
\tag{10}
\]

candidates. The actual smaller prime (p) is one of them. Testing
(\gcd(x,N)) therefore factors (N). In particular, if

\[
 L\ge\frac{\sqrt N}{Q(n)},
\tag{11}
\]

this is a deterministic quasipolynomial factor algorithm from the supplied
two states.

### 3.2 Balanced semiprimes

Assume additionally (q<2p), and put (S=p+q). Then

\[
 2\sqrt N<S<\frac3{\sqrt2}\sqrt N.
\tag{12}
\]

Enumerate the single CRT class (8) in this interval. Its width is

\[
 c_0\sqrt N,
 \qquad
 c_0=\frac3{\sqrt2}-2<\frac18.
\]

There are at most

\[
 \frac{c_0\sqrt N}{L}+1
\tag{13}
\]

candidates. For each candidate (S), test whether

\[
 \Delta=S^2-4N
\]

is a nonnegative square. If it is, the two integers

\[
 \frac{S-\sqrt\Delta}{2},
 \qquad
 \frac{S+\sqrt\Delta}{2}
\]

are verified factors. Hence the exact condition

\[
 L\ge\frac{c_0\sqrt N}{Q(n)}
\tag{14}
\]

gives at most (Q(n)+1) candidates. The simpler sufficient condition

\[
 L\ge\frac{\sqrt N}{8Q(n)}
\tag{15}
\]

has the same deterministic quasipolynomial conclusion.

## 4. Capped torus quotient closure

Write (H_r=\langle G\bmod r\rangle\) for (r\in\{p,q\}), and

\[
 K_r=\langle H_r,U_1,\ldots,U_t\rangle,
 \qquad
 Q_r=K_r/H_r.
\]

For a torus word (U), use (U^B) as its quotient fingerprint. Run the
P154 breadth-first closure on

\[
 F=\langle U_1^B,\ldots,U_t^B\rangle\le T_D(R).
\tag{16}
\]

Represent a torus point by its two coefficients. Before accepting a new
fingerprint (Y=y_0+y_1w), compare it with every stored
(Z=z_0+z_1w) through

\[
 \gcd(N,y_0-z_0,y_1-z_1).
\tag{17}
\]

Stop on a proper gcd, on complete closure, or after storing (C+1)
globally distinct fingerprints.

Exactly one of the following outcomes occurs.

1. A proper value in (17), or in a factor-first order screen, factors (N).
2. The table closes at size (\kappa\le C). Then

   \[
   Q_p\cong F\cong Q_q,
   \qquad
   |Q_p|=|Q_q|=\kappa.
   \tag{18}
   \]

   A stored generator of (F), with its public word provenance, and the
   Harvey--Hittmeir/P154 primary construction give a factor or a new torus
   state of exact common order

   \[
   \boxed{B'=B\kappa.}
   \tag{19}
   \]

   If (\kappa>1), this is strict torus-order growth. If (\kappa=1), it
   certifies only synchronized local membership. Hidden-log alignment is
   optional for the state update and is still needed for full global
   relation recovery.
3. The search stores (C+1) fingerprints. Then

   \[
   |Q_p|,|Q_q|\ge C+1,
   \qquad
   |K_p|,|K_q|\ge B(C+1).
   \tag{20}
   \]

   This is only a capacity lower bound.

After (19), recompute (L'=\operatorname{lcm}(A,B')) and apply Section 3.
The ordinary P154 updater can be used symmetrically to replace (A) by an
exact larger common order.

## 5. Monotone dual-order potential

Initialize both channels by (2). On every no-factor branch, the two exact
orders remain even. Equation (3) then gives

\[
 \gcd(A,B)=2,
 \qquad
 L=\frac{AB}{2}.
\tag{21}
\]

If an ordinary closure replaces (A) by (A\kappa), or a torus closure
replaces (B) by (B\kappa), where (\kappa>1), then the new exact state
still satisfies (21). Therefore

\[
 \boxed{L'=\kappa L.}
\tag{22}
\]

The initialization at order two is necessary for this literal statement.
If one channel starts at order one and only acquires the factor two already
present in the other channel, that strict order growth need not grow (L).

Starting from (L=2), (k) strict factor-or-growth events give

\[
 L\ge2^{k+1}.
\]

Thus (O(n)) strict events force the threshold (11), or the stronger
balanced threshold (14), and then factor (N). If every source round, every
closure table, every provenance word, and the complete retained transcript
has quasipolynomial bit length, (O(n)) rounds preserve quasipolynomial
total cost.

This is conditional. The result does not prove that a source supplies a
strict event in any round.

## 6. Capacity does not supply an order modulus

The inequality (20) cannot replace an exact common order in (3)--(9). A
capacity lower bound does not give one integer that divides both local group
orders.

There is a clean public balanced example. Let

\[
 N=143=11\cdot13,
 \qquad D=5,
 \qquad t=40.
\]

The Jacobi symbol of (D) is (-1). The clean Cayley point

\[
 U_D(t)=\frac{1+tw}{1-tw}=31+136w\pmod {143}
\tag{23}
\]

has local order (5) modulo (11) and local order (7) modulo (13).
Start from the torus identity state (B=1), use the one-block list
([U_D(t)]), and set (C=3). The four fingerprints

\[
 1,U,U^2,U^3
\]

are distinct in both local groups. Every comparison (17) is therefore one,
and the updater returns the capacity branch. But the two generated local
groups have coprime orders (5) and (7). They contain no nontrivial common
order state.

More generally, if an integer (m>C) divides both local torus orders, CRT
can place an order-(m) point in both local groups. The first (C+1) powers
then have identical equality patterns and give the capacity branch without
a factor. For odd (m), the point is not (-1), so it also has a clean
public Cayley parameter. Jacobi orientation alone does not exclude this
synchronized cyclic obstruction.

## 7. Exact conclusion

The torus quotient closure itself is not stronger than P154. It is the same
cyclic-group argument with two-coordinate equality gcds.

The nontrivial gain comes from retaining the ordinary and torus states
separately. Their exact orders divide (N-1) and (N+1), so their least
common multiple grows almost multiplicatively and eventually gives a CRT
factor search. This avoids the homomorphic transfer blocked by P140.

The missing theorem is still source-side. A positive all-input result must
force a factor, an exact closure with strict common-order growth, or another
event that prevents indefinite inert and capacity branches. P147 proves one
public quasipolynomial feedback factor path on one fixed input. It does not
supply a torus-native all-input source or the repeated growth law required
here.
