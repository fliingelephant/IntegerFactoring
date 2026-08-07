# F58 focused hostile whole-proof audit

## Artifact and verdict

**Candidate:**
`experiments/F58_generic_gcdfree_square_decoder_kill/RESULT.md`

**Pinned SHA-256:**
`f883fdb8a85678a2046f4e03716aaf9485b291d09ba7f1ddea6f949f5045a431`

**Verdict: FAIL AS WRITTEN.**

The mathematical decoder is correct. I found no counterexample to Theorems
1--3, including the multiset refinement, the exact parity kernel, the root
homomorphism, or basis-only factor detection for arbitrary odd, possibly
nonsquarefree, $N$.

The exact artifact nevertheless fails for two repairable reasons:

1. Its claim that P01 is the closest prior result is false. The gcd-free-basis
   infrastructure is standard, and F56 is the closest project result. The
   candidate must separate known infrastructure from the project synthesis.
2. The final complexity sentence must include the bit length of $N$. With the
   candidate's notation, the decoder is polynomial in $L+\log N$, not in $L$
   alone.

Neither defect invalidates the decoder theorem after correction. The first is
an attribution and novelty-boundary defect. The second is a complexity-
parameter defect with an immediate correction. Under PROMPT.md, prose-only
attribution repairs do not need a new mathematical audit. The corrected total
input-length bound should be checked during reconstruction.

No research computation was used in this audit.

## 1. The multiset refinement invariant passes

Interpret "two entries" as two distinct multiset occurrences. For one input
coordinate $i$, replacing $(x,\alpha)$ and $(y,\beta)$ by

\[
(d,\alpha+\beta),\qquad(x/d,\alpha),\qquad(y/d,\beta),
\quad d=\gcd(x,y),
\]

preserves the represented value because

\[
d^{\alpha_i+\beta_i}(x/d)^{\alpha_i}(y/d)^{\beta_i}
=x^{\alpha_i}y^{\beta_i}.
\]

Dropping an output whose integer part is $1$ is harmless.

The two high-risk degeneracies are valid:

- If $x=y$, then $d=x=y$. The two quotients are $1$, and the one retained
  entry is $(x,\alpha+\beta)$. This exactly merges the occurrences.
- If $x\mid y$, then $d=x$. The replacement is
  $(x,\alpha+\beta)$ and $(y/x,\beta)$. It preserves the invariant even when
  $x$ and $y/x$ still share a factor; a later refinement separates it.

Different outputs can have the same integer part. They remain distinct
multiset occurrences and are merged by a later iteration. No special case is
needed.

## 2. The valuation potential proves termination without factoring

The potential

\[
\Phi=\sum_p\sum_{(b,w)}v_p(b)^2
\]

is only a proof device. The algorithm does not evaluate it and does not need
the prime factors.

For a prime in the selected gcd, let the two valuations be $r\ge s>0$.
The refinement changes its contribution from $r^2+s^2$ to

\[
s^2+(r-s)^2,
\]

so the decrease is

\[
r^2+s^2-s^2-(r-s)^2=s(2r-s)\ge1.
\]

For a prime outside the gcd, one selected valuation is zero, and its
contribution is unchanged. Hence each actual refinement lowers the
nonnegative integer $\Phi$ by at least one.

Initially,

\[
\sum_p v_p(a_i)^2
\le \left(\sum_p v_p(a_i)\right)^2
\le (\log_2 a_i)^2.
\]

Summing over $i$ gives $\Phi_0\le L^2$. Therefore at most $L^2$
refinements occur. This is a symbolic polynomial bound and does not hide a
factorization oracle.

## 3. Entry, exponent, and intermediate-size bounds pass

Each refinement removes two entries and inserts at most three, so the entry
count is at most $m+L^2$. Every new integer part divides one of the selected
integer parts. Thus basis values never grow and have at most $L$ bits.

For every stored pair $(b,w)$ and coordinate $i$, the invariant shows that
$b^{w_i}$ divides $a_i$. Since $b\ge2$,

\[
0\le w_i\le\log_2 a_i.
\]

There are polynomially many exponent-vector entries, and each exponent has
polynomial bit length. A full rescan has $O(L^4)$ pairs, and there are
$O(L^2)$ rescans. Thus the stated $O(L^6)$ gcd-test count is valid. The
candidate's deliberately loose $O(L^{10})$ bit bound is safe after accounting
for the $m$-coordinate exponent updates.

For a selected subset, its product has at most the sum of the input bit
lengths. Every factor built during the positive-root formula divides that
root, and monotone multiplication need never exceed the final root. Therefore
the exact root has polynomial bit length. Integer square tests, binary
exponentiation, multiplication, and binary linear algebra are all polynomial
in the explicit integer-list length.

## 4. A square/nonsquare flag per coprime composite basis element is enough

This is the main high-risk algebraic clause, and it passes.

Let

\[
a_i=\prod_j g_j^{e_{ij}}
\]

with the $g_j$ pairwise coprime. For a subset vector $c$, put

\[
E_j=\sum_i c_i e_{ij}.
\]

If $g_j$ is a square, then $g_j^{E_j}$ is always a square. If $g_j$ is not a
square, at least one prime has odd valuation in $g_j$. Then $g_j^{E_j}$ is a
square exactly when $E_j$ is even. Because no prime divides two different
$g_j$, another basis element cannot cancel this odd valuation.

Consequently,

\[
Mc=0
\quad\Longleftrightarrow\quad
\prod_i a_i^{c_i}\text{ is an integer square}.
\]

The algorithm does not need to identify the odd-valuation prime inside a
nonsquare composite $g_j$. An exact integer square test of $g_j$ is enough.

For $Mc=0$, the formula

\[
R(c)=
\prod_{g_j\text{ square}}(\sqrt{g_j})^{E_j}
\prod_{g_j\text{ nonsquare}}g_j^{E_j/2}
\]

is exactly the positive integer square root. It uses no hidden prime
factorization.

## 5. Inputs 1, duplicates, and prime powers pass

- An input $a_i=1$ creates no refinement entry. Its matrix column is zero.
  The singleton product and root are both $1$.
- Equal input integers are distinct multiset occurrences initially. The
  refinement adds their exponent columns. Two copies of a nonsquare value
  produce equal parity columns, so their pair is detected. Two copies of a
  square value each have a zero column, and their singleton and pair roots are
  also computed correctly.
- A composite basis value such as a prime power needs no internal
  factorization. If it is nonsquare, any odd outer exponent leaves at least
  one odd prime valuation. If it is square, every outer exponent is harmless.
- Positivity is needed. The candidate correctly excludes zero. Its example
  shows why square-product subsets with zero would not be a vector space.

## 6. The exact-root map is a homomorphism

For kernel vectors $c,d$, exact positivity gives

\[
R(c)R(d)
=R(c\oplus d)\prod_{i:c_i=d_i=1}a_i.
\]

If every $a_i\equiv1\pmod N$, reduction modulo $N$ gives

\[
R(c)R(d)\equiv R(c\oplus d)\pmod N.
\]

Also $R(c)^2\equiv1\pmod N$. Hence

\[
\rho:c\longmapsto R(c)\bmod N
\]

is a group homomorphism from $\ker M$ to the roots of $1$ modulo $N$.
There is no cancellation assumption in this step; the discarded overlap
factor is explicitly $1$ modulo $N$.

## 7. An arbitrary kernel basis detects every non-global image

Let $B$ be any vector-space basis of $\ker M$. If every $b\in B$ has
$\rho(b)\in\{1,-1\}$, then the subgroup generated by the basis images is
contained in $\{1,-1\}$. Since $B$ generates the complete kernel, every
kernel vector then has global image $1$ or $-1$.

The contrapositive proves the candidate's claim: if one exact square subset
has a non-global root, every kernel basis contains at least one vector whose
root is non-global. Testing only basis vectors loses no useful image.

## 8. Odd nonsquarefree moduli pass

Write

\[
N=\prod_t p_t^{\alpha_t}
\]

with distinct odd primes $p_t$. If $x^2\equiv1\pmod{p_t^{\alpha_t}}$, then
$p_t^{\alpha_t}$ divides $(x-1)(x+1)$. The gcd of these two factors divides
$2$, so the complete odd prime power divides one factor. Thus $x$ is $1$ or
$-1$ on each complete prime-power component.

A root that is not globally $1$ or globally $-1$ uses both signs. Therefore

\[
\gcd(x-1,N)
\quad\text{and}\quad
\gcd(x+1,N)
\]

select two nonempty proper sets of complete prime-power components. Both are
proper nontrivial divisors. This covers repeated prime factors. For an odd
prime power there is no non-global root, so the theorem's premise is false and
the decoder makes no false factor claim.

## 9. The total complexity parameter needs one correction

Theorem 1 and exact-root construction are polynomial in

\[
L=m+\sum_i\left\lceil\log_2(a_i+1)\right\rceil.
\]

Theorem 3 also reads $N$ and computes gcds with $N$. Its total bit bound must
therefore be stated as polynomial in

\[
L+n,\qquad n=\left\lceil\log_2(N+1)\right\rceil.
\]

The all-one edge case makes this necessary. Take $m=1$ and $a_1=1$ while
$N$ is an arbitrary large odd integer. Then $L=2$ is fixed, but even reading
$N$ and computing the displayed gcds costs as a function of $n$, not as a
function of $L$ alone.

This is not a superpolynomial intermediate-value defect. It is a missing
input parameter in lines 230--232. Replacing "polynomial in the explicit
list length" by "polynomial in $L+n$" repairs it. In the inverse-quotient
application, each nontrivial $a_i=Nk_i+1$ already has $O(n)$ bits, but the
theorem should still state its full input measure.

## 10. P01 is met with equality, not contradicted

For each nonsquare $g_j$, choose for proof purposes a prime whose valuation in
$g_j$ is odd. Pairwise coprimality ensures that this prime occurs in no other
$g_k$. Therefore the square classes of the nonsquare $g_j$ are linearly
independent in $\mathbb Q^\times/(\mathbb Q^\times)^2$.

The $i$-th column of $M$ is exactly the coordinate vector of $[a_i]$ in this
independent family. Hence

\[
\operatorname{rank}M
=\operatorname{rank}([a_1],\ldots,[a_m]).
\]

F58 does not compress the true square-class rank and does not manufacture a
dependency. It meets P01's lower bound with equality. There is no
contradiction.

## 11. Attribution and novelty boundary must be repaired

The statement in lines 15--22 that P01 is the closest prior result is not
acceptable.

Theorem 1 is known gcd-free-basis, also called coprime-base, infrastructure.
Relevant prior sources include:

- Eric Bach and Jeffrey Shallit, *Algorithmic Number Theory, Volume 1*,
  Section 4.8 (1996). That section gives gcd-free-basis algorithms and records
  earlier work by Bach, Driscoll, and Shallit.
- Daniel J. Bernstein, "Factoring into coprimes in essentially linear time,"
  *Journal of Algorithms* 54 (2005), 1--30,
  DOI `10.1016/j.jalgor.2004.04.009`. It computes a coprime base and the
  exponent representations using gcd, exact division, multiplication, and
  equality testing. The candidate's simple refinement is slower but remains
  a valid polynomial implementation of known infrastructure.

The use of coprime bases to detect multiplicative relations is also a known
application. The exact parity-kernel observation in Theorem 2 is an elementary
specialization of that infrastructure, not a new factoring primitive by
itself.

Inside this project, F56 is much closer than P01. F56 already proves an exact
square-relation decoder for a clustered list of values $Nk_i+1$. F58 removes
F56's short-interval and small-prime trial-division restriction by replacing
that partial coordinate system with a complete gcd-free basis. The project
synthesis worth recording is therefore:

1. use known gcd-free-basis infrastructure on the complete explicit relation
   list;
2. retain one parity row for each nonsquare coprime block;
3. construct exact roots without factoring those blocks; and
4. use the root-image homomorphism to prove that testing an arbitrary kernel
   basis is complete.

I did not establish that item 4 is absent from prior literature. The candidate
must not claim publication-level novelty for it without a dedicated literature
review. It can safely claim a strictly stronger and simpler project decoder
than F56, with the source-side useful-relation law still missing.

## 12. The theorem has a useful, nonblocking generalization

The restriction $a_i\equiv1\pmod N$ is correct, so its narrow form does not
fail. It can be generalized to ordinary congruence-of-squares pairs.

Assume each positive $a_i$ comes with a known unit $x_i\bmod N$ such that

\[
x_i^2\equiv a_i\pmod N.
\]

For a square subset $c$, define

\[
X(c)=\prod_i x_i^{c_i}\pmod N,
\qquad
\sigma(c)=R(c)X(c)^{-1}\pmod N.
\]

Then $\sigma(c)^2=1$. For kernel vectors $c,d$, the overlap formulas are

\[
R(c)R(d)=R(c\oplus d)\prod_{i:c_i=d_i=1}a_i
\]

and

\[
X(c)X(d)
\equiv X(c\oplus d)\prod_{i:c_i=d_i=1}a_i\pmod N.
\]

The overlap product is a unit, so division proves

\[
\sigma(c)\sigma(d)=\sigma(c\oplus d).
\]

Thus the same arbitrary-basis argument applies. If any dependency has
$R(c)\not\equiv\pm X(c)\pmod N$, one kernel-basis vector does too, and

\[
\gcd(R(c)-X(c),N),
\qquad
\gcd(R(c)+X(c),N)
\]

extract a factor for odd $N$. If an $x_i$ is not a unit, a direct gcd screen
can already expose a factor in the proper-gcd case; otherwise the generalized
homomorphism should explicitly retain the unit hypothesis.

The original theorem is the special case $x_i=1$. This strengthening is more
natural for standard congruence-of-squares algorithms, but omitting it is not
a defect in the narrower correct theorem.

## 13. Exact remaining gap

F58 is a decoder, not a source theorem. Given any polynomial-total-bit list of
explicit values $a_i=Nk_i+1$, it can find every exact square dependency and
test a complete generating set of their modular-root images in deterministic
polynomial time.

It does not prove that a list computable from bare $N$ contains any dependency.
It also does not prove that a dependency has a non-global root, or that such a
list is produced with inverse-polynomial probability for every composite
$N$. The missing all-input useful-relation law remains the factoring-hard
source-side step.

After the attribution boundary and the $L+n$ complexity measure are repaired,
the mathematical theorem is ready for proof-blind reconstruction.
