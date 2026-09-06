# Hostile audit of the F172 candidate

## Verdict

**PASS, in the narrow stated scope.** I found no mathematical defect in the
frozen statement or proof. The construction gives an infinite unbalanced
trial-hard semiprime family with constant ambient capacity for exact common
orders in the ordinary multiplicative groups and in every quadratic
norm-one torus orientation.

This is not a factoring lower bound. In particular, an attempted update can
still factor through unequal local orders, unequal quotient fingerprints, or
another mismatch screen.

The audited frozen files have the exact SHA-256 hashes recorded in
MANIFEST.md:

- STATEMENT.md:
  d2ff244f1fb28e00ba262fdb89cd5a23b7b75954586bfb998ffd188db4a8ed9f;
- PROOF.md:
  b23989a19a23653dab9946dca55888384a2c4493184878a3dfac68ec9c067a21;
- SELF_AUDIT.md:
  2ac2410cdedfeafc98d997bac7a3c7cae11e8613f34a34dd2e920d8d0410bf9d.

No computation was used.

## Kill attempts

### 1. CRT compatibility and reducedness

Write

\[
p^2-1=2^u3^vM,
\qquad \gcd(M,6)=1.
\]

The four moduli $8,p,3^v,M$ are pairwise coprime: $p>3$ is prime,
$p\nmid p^2-1$, and the factors $3^v$ and $M$ have had their two- and
three-parts separated. The prescribed residues $3,1,4,2$ are units modulo
their respective moduli. The CRT therefore gives one reduced class modulo

\[
H_p=8p3^vM.
\]

The case $M=1$ only removes a vacuous component. It creates no exception.

### 2. Linnik quantifiers, size, and the lower bound on $q$

The standard form of Linnik's theorem has absolute constants $c,L_0$,
independent of both the modulus and the reduced class. It therefore supplies
a prime in the constructed class with

\[
q\le cH_p^{L_0}.
\]

Since $q\equiv1\pmod p$, positivity gives $q=1+tp$ with $t\ge0$.
The value $t=0$ gives $1$, and $t=1$ gives the even integer $p+1>2$.
Neither is prime. Thus $t\ge2$ and $q>2p$. This also proves that the two
hidden primes are distinct. No prime-in-a-short-interval theorem is used.

### 3. The full odd-prime attack on all four shifted gcds

Every prime $\ell\ge5$ dividing either $p-1$ or $p+1$ divides $M$.
The condition $q\equiv2\pmod M$ gives

\[
q-1\equiv1\pmod\ell,
\qquad q+1\equiv3\pmod\ell.
\]

Hence $\ell$ divides neither relevant shifted factor of $q$. This excludes
all odd common primes at least five in each of

\[
\gcd(p-1,q-1),\quad
\gcd(p-1,q+1),\quad
\gcd(p+1,q-1),\quad
\gcd(p+1,q+1).
\]

The argument needs only divisibility modulo $\ell$, but the CRT condition in
fact controls the full $\ell$-power contained in $M$.

### 4. Every three-adic case

Because $p\equiv1\pmod3$, the full three-part $3^v$ of $p^2-1$ lies in
$p-1$, while $3\nmid p+1$.

If $v=1$, then $v_3(p-1)=1$, and $q\equiv4\equiv1\pmod3$, so the
common three-part of $p-1$ and $q-1$ is exactly $3$, regardless of any
higher valuation of $q-1$. If $v\ge2$, then

\[
q-1\equiv3\pmod{3^v},
\]

which gives $v_3(q-1)=1$. Thus the common three-part is again exactly
$3$. Also $q\equiv1\pmod3$, so $3\nmid q+1$. No other shifted gcd has
a three-part.

### 5. Every two-adic case

The condition $q\equiv3\pmod8$ gives

\[
v_2(q-1)=1,
\qquad v_2(q+1)=2.
\]

Since $p$ is odd, both $p-1$ and $p+1$ are even. Combining these facts
with Sections 3 and 4 gives exactly

\[
\begin{aligned}
\gcd(p-1,q-1)&=6,\\
\gcd(p-1,q+1)&=2^{\min(v_2(p-1),2)}\in\{2,4\},\\
\gcd(p+1,q-1)&=2,\\
\gcd(p+1,q+1)&=2^{\min(v_2(p+1),2)}\in\{2,4\}.
\end{aligned}
\]

This exhausts both possibilities for the two-parts of $p-1$ and $p+1$.

### 6. Ordinary and torus common-order bounds

An ordinary unit with exact order $A$ in both hidden fields satisfies

\[
A\mid p-1,
\qquad A\mid q-1,
\]

and hence $A\mid6$.

For a unit discriminant $D$, let
$\epsilon_r=(D/r)$. The quadratic norm-one group over
$\mathbf F_r$ is cyclic of order $r-\epsilon_r$: it is the split torus of
order $r-1$ when $\epsilon_r=1$, and the norm-one subgroup of
$\mathbf F_{r^2}^{\times}$, of order $r+1$, when $\epsilon_r=-1$.
Therefore any torus point with the same exact order $B$ in both local
components obeys

\[
B\mid\gcd(p-\epsilon_p,q-\epsilon_q).
\]

The four orientation bounds are respectively $6$, at most $4$, $2$,
and at most $4$. Jacobi-minus-one discriminants use only the two mixed
orientations, whose bounds are at most $4$ and $2$. This reasoning covers
every unit discriminant, not only one selected discriminant.

### 7. Combined capacity

Keeping arbitrarily many common-order elements does not evade the bounds.
Within one cyclic local group, the least common multiple of their orders
still divides its ambient shifted gcd. Across the ordinary state and all
four torus orientations, every possible combined exact-order modulus divides

\[
\operatorname{lcm}(6,4,2)=12.
\]

Thus the claimed bound $\operatorname{lcm}(A,B_+,B_-)\le12$ is valid even
if the source attains every available common-order subgroup.

### 8. Infinitude, input length, and trial hardness

Dirichlet's theorem gives infinitely many primes $p\equiv1\pmod3$. For
each such $p$, the construction gives $q>2p$. The smaller prime factor of
$N=pq$ is therefore $p$, so distinct choices of $p$ give distinct
semiprimes.

The odd part $3^vM$ of $p^2-1$ is less than $p^2$, and hence

\[
H_p<8p^3,
\qquad q\le c(8p^3)^{L_0}=p^{O(1)}.
\]

Together with $q>2p$, this yields

\[
2\log_2p+O(1)\le\log_2N
\le(3L_0+1)\log_2p+O(1).
\]

For $n=\lceil\log_2(N+1)\rceil$, it follows that
$\log p=\Theta(n)$. Thus $p=2^{\Theta(n)}$, and $q>p$; both factors
eventually exceed $n^C$ for every fixed $C$. The family is trial-hard.
The proof makes no balanced-family claim, and $q>2p$ explicitly makes the
displayed family unbalanced.

### 9. The quasipolynomial threshold

For fixed constants $C,k$, let

\[
Q(n)=2^{C(\log_2(n+1))^k}.
\]

Then $\log_2Q(n)=o(n)$, while
$\log_2\sqrt N=\Theta(n)$. Consequently

\[
12<\frac{\sqrt N}{Q(n)}
\]

for every sufficiently large member of the family. Constant common-order
capacity cannot reach the F170 terminal CRT threshold.

### 10. Exact scope

The candidate blocks only an all-input termination proof based on monotone
growth of exact common orders. It does not say that an updater returns a
no-growth result. A discrepancy between the hidden components can still
produce a proper gcd while the updater checks an order, equality, quotient,
or alignment condition. The result also says nothing against canonical
integer relations, carries, square-root decoders, or another non-order
source. I found no scope leak into a general factoring lower bound.

## Nonfatal editorial issue

Proof Section 5 renders one comparison as
$2\log_2p+O(1)le\log_2N$; the intended relation is plainly $\le$, and the
preceding and following inequalities prove it. This is a typography defect,
not a mathematical gap.
