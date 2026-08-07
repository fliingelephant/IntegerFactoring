# F58 — Generic gcd-free exact square-relation decoder

**Status:** promoted as P66 after a mandatory kill-first test, a failed first
audit, a passing fresh whole-artifact re-audit, and strict proof-blind
reconstruction. The first audit accepted the mathematical decoder but required
a prior-art correction and the full $L+\log N$ complexity measure. The final
version also states the audit-derived congruence-pair generalization.

**Verdict:** the proposed decoder survives the kill-first test. A deterministic
polynomial-bit algorithm can compute a gcd-free basis without factoring its
basis elements. The resulting parity kernel is exactly the set of integer
square subsets. Given known unit congruences $x_i^2\equiv a_i\pmod N$, testing
only a basis of that kernel detects a factor whenever any square subset gives a
non-global congruence of squares.

This is a decoder theorem.  It does not prove that a useful square subset exists
in any particular sample list.

## Prior art and project-level difference

Gcd-free bases, also called coprime bases, are established infrastructure.
Bach and Shallit, *Algorithmic Number Theory, Volume 1*, Section 4.8 (1996),
give gcd-free-basis algorithms and earlier references. Daniel J. Bernstein,
"Factoring into coprimes in essentially linear time," *Journal of Algorithms*
54 (2005), 1--30, DOI `10.1016/j.jalgor.2004.04.009`, gives a substantially
faster algorithm. Detecting multiplicative relations with such bases is also
standard. The refinement below is only a simple polynomial-time proof vehicle.

Inside this project, the closest prior result is F56/P65. It decodes exact
square relations in a short cluster of values $Nk_i+1$ by using their small
public differences. The result here removes that localization premise: it
computes a complete coordinate system for any explicit polynomial-size list.
The project synthesis is the combination of the known gcd-free basis, exact
square tests of its coprime blocks, exact root construction, and the proof that
an arbitrary parity-kernel basis is complete for modular factor extraction.
No publication-level novelty is claimed for that synthesis without a dedicated
literature review.

P01 remains the relevant barrier theorem. The construction here does not
compress square-class rank and does not force a relation. Its coordinate map
has exactly the true rank, so it meets P01 with equality.

## Theorem 1 — a gcd-free basis is computable without factoring

Let $a_1,\ldots,a_m$ be positive integers.  There is a deterministic
polynomial-bit algorithm that produces integers $g_1,\ldots,g_s>1$ and
nonnegative integers $e_{ij}$ such that

\[
\gcd(g_j,g_k)=1\quad(j\ne k),
\qquad
a_i=\prod_{j=1}^s g_j^{e_{ij}}.
\]

The algorithm uses gcd, exact division, comparison, and addition of known
exponents.  It never factors a $g_j$.

### Refinement algorithm

Maintain a multiset of pairs $(b,w)$, where $b>1$ and
$w=(w_1,\ldots,w_m)\in\mathbb Z_{\ge0}^m$, with the invariant

\[
a_i=\prod_{(b,w)} b^{w_i}\qquad(1\le i\le m).
\]

Initially insert $(a_i,\mathbf e_i)$ for each $a_i>1$.  Inputs equal to $1$
need no entry.  While two entries $(x,\alpha)$ and $(y,\beta)$ have
$d=\gcd(x,y)>1$, remove them and insert the following entries when their
integer part is larger than $1$:

\[
(d,\alpha+\beta),\qquad
(x/d,\alpha),\qquad
(y/d,\beta).
\]

For every input coordinate $i$, this replacement is valid because

\[
x^{\alpha_i}y^{\beta_i}
=d^{\alpha_i+\beta_i}(x/d)^{\alpha_i}(y/d)^{\beta_i}.
\]

It also handles $x=y$ and $x\mid y$ without a special mathematical case.
At termination, the remaining integer parts are pairwise coprime and give the
required $g_j$ and exponent columns.

### Termination and size bound

For the proof only, write $v_p(b)$ for a prime valuation and define

\[
\Phi=\sum_p\sum_{(b,w)}v_p(b)^2.
\]

Suppose the selected entries have $p$-valuations $r,s>0$, and assume
$r\ge s$.  After refinement, their contributions become

\[
s^2+(r-s)^2.
\]

The old contribution was $r^2+s^2$, so it decreases by

\[
s(2r-s)\ge1.
\]

Valuations for primes outside the gcd do not change.  Hence each refinement
decreases the nonnegative integer $\Phi$ by at least $1$.  If

\[
L=m+\sum_i\left\lceil\log_2(a_i+1)\right\rceil
\]

is a conservative input-length measure, then

\[
\Phi_0
=\sum_i\sum_p v_p(a_i)^2
\le \sum_i(\log_2 a_i)^2
\le L^2.
\]

Thus there are at most $L^2$ refinements.  Each refinement increases the
number of entries by at most one, so there are at most $m+L^2$ entries.
Every integer part remains a divisor of an earlier integer part and therefore
has at most $L$ bits.  The invariant and $b\ge2$ give

\[
0\le w_i\le\log_2 a_i,
\]

so all exponent columns also have polynomial size.

A direct implementation can scan all current pairs after each refinement.
It performs $O(L^6)$ gcd tests on $O(L)$-bit integers.  Ordinary Euclidean
gcd, exact division, and the exponent-column updates therefore give, for
example, a conservative $O(L^{10})$ bit bound.  The exponent is not intended
to be sharp; the important point is that it is fixed and independent of the
unknown prime factors.

## Theorem 2 — the parity kernel is exact

Integer-square-test every $g_j$.  Let $J$ be the indices for which $g_j$
is not a perfect square.  Form the binary matrix

\[
M_{j i}=e_{ij}\bmod2\qquad(j\in J,\ 1\le i\le m).
\]

Then, for every $c\in\mathbb F_2^m$,

\[
Mc=0
\quad\Longleftrightarrow\quad
\prod_{i=1}^m a_i^{c_i}
\text{ is an integer square}.
\]

**Proof.**  Put $E_j=\sum_i c_i e_{ij}$, as an ordinary nonnegative
integer.  Pairwise coprimality means that every rational prime occurs in at
most one $g_j$.  If $g_j$ is a square, then $g_j^{E_j}$ is a square for
all $E_j$.  If $g_j$ is not a square, it has at least one odd prime
valuation.  Therefore $g_j^{E_j}$ is a square exactly when $E_j$ is even.
No prime valuation can cancel against another basis element.  This gives the
equivalence.  \(\square\)

This test does not require the prime factorization of a nonsquare composite
$g_j$.  It needs only its exact square-test result.

For any $c\in\ker M$, its exact positive root is also computable without
factoring.  Let $h_j=\sqrt{g_j}$ for square basis elements.  Then

\[
R(c)=
\prod_{j\notin J} h_j^{E_j}
\prod_{j\in J} g_j^{E_j/2}.
\]

The root has at most half the bit length of the selected product.  That length
is at most the sum of the input lengths.  Binary exponentiation and integer
multiplication therefore keep the complete computation polynomial in $L$.

## Theorem 3 — testing a kernel basis is complete for useful congruences

Let $N\ge3$ be odd. For each $i$, suppose a known unit $x_i\bmod N$ satisfies

\[
x_i^2\equiv a_i\pmod N.
\]

For $c\in\mathbb F_2^m$, define

\[
X(c)=\prod_i x_i^{c_i}\pmod N.
\]

Compute any binary basis $c^{(1)},\ldots,c^{(r)}$ of $\ker M$. For each
basis vector, compute the exact positive root $R(c^{(t)})$ above and test

\[
\gcd(R(c^{(t)})-X(c^{(t)}),N),
\qquad
\gcd(R(c^{(t)})+X(c^{(t)}),N).
\]

If some square subset $c\in\ker M$ has

\[
R(c)\not\equiv X(c),-X(c)\pmod N,
\]

then one of these tests on a kernel-basis vector returns a proper nontrivial
divisor of $N$.

**Proof.**  For $c,d\in\ker M$, let $c\oplus d$ denote binary addition.
Taking positive square roots in

\[
\left(\prod_i a_i^{c_i}\right)
\left(\prod_i a_i^{d_i}\right)
=
\left(\prod_i a_i^{(c\oplus d)_i}\right)
\left(\prod_{i:c_i=d_i=1}a_i\right)^2
\]

gives

\[
R(c)R(d)
=R(c\oplus d)\prod_{i:c_i=d_i=1}a_i.
\]

Also,

\[
X(c)X(d)
\equiv
X(c\oplus d)\prod_{i:c_i=d_i=1}a_i
\pmod N.
\]

All overlap factors are units because $a_i\equiv x_i^2\pmod N$ and every
$x_i$ is a unit. Hence

\[
\rho(c)=R(c)X(c)^{-1}\bmod N
\]

is defined. Its square is $1\bmod N$, and the two overlap identities show that
it is a group homomorphism from $\ker M$ to the square roots of $1\bmod N$.
If every kernel-basis vector mapped into the global subgroup
$\{1,-1\}$, then every vector in the kernel would map into that subgroup.
The assumed useful $c$ proves that at least one basis vector has a
non-global root.

For odd $N=\prod_t p_t^{\alpha_t}$, every root of $1$ modulo each odd prime
power is $1$ or $-1$: the prime power divides one of the two factors
$x-1,x+1$, whose gcd divides $2$. A non-global root therefore uses both
signs across the prime-power components. Multiplication by the unit $X(c)$
shows that the two displayed gcds collect the two nonempty proper groups of
components. Both are proper nontrivial divisors.
\(\square\)

Gaussian elimination, exact-root construction, and at most $2m$ final gcds
are polynomial in

\[
L+n,\qquad n=\left\lceil\log_2(N+1)\right\rceil.
\]

Together with Theorem 1, this is a deterministic polynomial-bit decoder. The
special case $x_i=1$ is exactly the earlier hypothesis $a_i\equiv1\pmod N$.

## Adversarial edge cases

- **Zero:** positivity is essential. With the list $(0,2)$, the subsets
  $\{0\}$ and $\{0,2\}$ have square product $0$, but their symmetric
  difference $\{2\}$ does not.  Thus square subsets are not a vector space
  when zero is allowed. The unit congruence $x_i^2\equiv a_i\pmod N$ implies
  $\gcd(a_i,N)=1$, but positivity remains an explicit input condition.
- **One:** an input equal to $1$ has a zero matrix column.  Its singleton is
  correctly recognized as a square, with root $1$.
- **Duplicates:** duplicate entries are valid.  Refinement merges their shared
  support through exponent-column addition.  Selecting two equal entries gives
  the expected square relation, whose root is the repeated integer.
- **Prime powers and mixed composite basis elements:** no prime factorization is
  used.  Pairwise coprimality prevents cross-basis cancellation.  A nonsquare
  basis element raised to an odd exponent stays nonsquare because at least one
  of its prime valuations is odd.
- **Prime or prime-power $N$:** there is no non-global square root of $1$
  for odd prime powers.  The completeness statement then has a false premise
  and the decoder returns no improper claim.
- **Repeated factors and arbitrary odd $N$:** the proof groups complete odd
  prime-power components, so repeated factors cause no gap.  Every returned gcd
  is checked directly and divides $N$.
- **Bit lengths:** the basis values never grow.  Any constructed exact root has
  at most the bit length of the product of a subset of the explicit inputs.
  Thus neither refinement nor root construction hides an exponential output.
- **Nonunit witnesses:** Theorem 3 requires unit $x_i$. If an application
  supplies a nonunit residue, it first computes $\gcd(x_i,N)$. A proper gcd is
  already a factor. A gcd of $1$ verifies the unit premise. A gcd of $N$ does
  not enter the homomorphism claim.

## Why this does not contradict P01

For each nonsquare $g_j$, choose a prime that has odd valuation in $g_j$.
That prime divides no other basis element.  Therefore the classes of the
nonsquare $g_j$ are independent square-class coordinates.  The columns of
$M$ are exactly the coordinates of the input classes in this basis.  Hence

\[
\operatorname{rank}M
=\operatorname{rank}([a_1],\ldots,[a_m]).
\]

There is no rank reduction.  Adaptive gcd refinement discovers the exact
finite-list coordinate system; it does not manufacture a dependence and does
not factor an isolated hard basis element.  For a single nonsquare integer,
the algorithm simply returns that integer as one basis element and finds no
relation.

## Consequence and remaining gap

The short-interval or difference-smoothness premise is not needed for exact
decoding of an explicit relation list.  It can still be useful for proving that
relations exist, but it is not a decoder requirement.

For the inverse-quotient route, one can feed any polynomial-size explicit list
$a_i=Nk_i+1$ directly to this decoder with $x_i=1$. For an ordinary
congruence-of-squares method, one can instead use its known pairs
$x_i^2\equiv a_i\pmod N$. The unresolved task is still source-side: prove that
a list computable from bare $N$, with polynomial total bit length, contains a
square subset whose normalized root $R(c)X(c)^{-1}$ is non-global modulo $N$,
with a sufficient all-input success law. This candidate supplies no such law
and is not a factoring algorithm by itself.

No computation was used in this proof-only test.
