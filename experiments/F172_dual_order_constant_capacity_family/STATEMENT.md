# F172 candidate — an infinite constant-capacity family for dual common orders

## Status and scope

This is a proof-only candidate. It is not a factoring lower bound and it is
not a counterexample to the F170 factor-or-growth updater.

F170 keeps an ordinary element of one exact order in both hidden fields and a
Jacobi-minus-one torus element of one exact order in both local tori. This
candidate shows that the state-growth branch of that design cannot be an
all-input terminal mechanism. There are infinitely many trial-hard
semiprimes on which the largest possible ordinary common order is at most
six and every quadratic norm-one torus common order is at most six. For the
opposite local orientations produced by a Jacobi-minus-one discriminant, the
torus bound is at most four.

The family is intentionally unbalanced. No balanced-family claim is made.

## The construction

Let $p>3$ be any prime with

\[
p\equiv1\pmod3.
\]

Write

\[
p^2-1=2^u3^vM,
\qquad \gcd(M,6)=1.
\]

Here $v\ge1$. Put

\[
H_p=8p3^vM.
\]

Use the Chinese remainder theorem to define one reduced residue class
$a_p\pmod{H_p}$ by

\[
\begin{aligned}
a_p&\equiv3\pmod8,\\
a_p&\equiv1\pmod p,\\
a_p&\equiv4\pmod{3^v},\\
a_p&\equiv2\pmod M.
\end{aligned}
\tag{1}
\]

When $M=1$, omit the last congruence. Linnik's theorem supplies a prime

\[
q\equiv a_p\pmod{H_p}
\tag{2}
\]

with $q\le H_p^{O(1)}$. The constants in this bound are absolute.

Set $N=pq$. Then $q>2p$, and

\[
\boxed{\gcd(p-1,q-1)=6,}
\tag{3}
\]

\[
\boxed{\gcd(p-1,q+1)\in\{2,4\},}
\tag{4}
\]

\[
\boxed{\gcd(p+1,q-1)=2.}
\tag{5}

The remaining shifted gcd also satisfies

\[
\boxed{\gcd(p+1,q+1)\in\{2,4\}.}
\tag{5a}

As $p$ ranges through the infinitely many primes $1\pmod3$, this gives
infinitely many distinct semiprimes.

## Exact consequence for ordinary and torus states

Let an ordinary unit have exact order $A$ modulo both $p$ and $q$. Then

\[
A\mid\gcd(p-1,q-1)=6.
\tag{6}

Let $D$ be any unit and put
$\epsilon_p=(D/p)$ and $\epsilon_q=(D/q)$. If a norm-one torus point has
exact order $B$ in both local tori, then

\[
B\mid
\begin{cases}
6,&(\epsilon_p,\epsilon_q)=(+1,+1),\\
4,&(\epsilon_p,\epsilon_q)=(+1,-1),\\
2,&(\epsilon_p,\epsilon_q)=(-1,+1),\\
4,&(\epsilon_p,\epsilon_q)=(-1,-1).
\end{cases}
\tag{7}

For Jacobi symbol $-1$, only the two mixed rows occur. Therefore, even if an
algorithm keeps ordinary and torus states for every discriminant orientation
and reaches the full available common orders,

\[
\boxed{\operatorname{lcm}(A,B_+,B_-)\le12.}
\tag{8}

In particular, the F170 dual modulus $L=\operatorname{lcm}(A,B)$ is at most
twelve on this family. It cannot reach the F170 terminal threshold
$\sqrt N/Q(n)$ for any fixed quasipolynomial $Q$ and all sufficiently large
members of the family.

## Size and trial-hardness

Since

\[
H_p<8p^3,
\]

Linnik's theorem gives $q=p^{O(1)}$. Also $q>2p$. Hence, for

\[
n=\lceil\log_2(N+1)\rceil,
\]

we have

\[
\log p=\Theta(n),
\qquad
p=2^{\Theta(n)}.
\tag{9}

Thus both prime factors exceed $n^C$ for every fixed $C$ after a finite
prefix. The family is trial-hard in the bit length.

## Exact boundary

This theorem blocks only a universal argument that repeated exact
common-order growth in ordinary and quadratic norm-one groups must eventually
make the dual CRT modulus large. On this family there is no such ambient
common-order capacity.

It does not block a source from factoring $N$ while trying to align local
orders, compare quotient fingerprints, or process a capacity mismatch. It
does not obstruct non-order canonical-integer, carry, relation, or root
decoders. It is not a lower bound for factoring.
