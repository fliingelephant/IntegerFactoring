# F56 fresh hostile re-audit after the first-audit corrections

## Artifact and verdict

**Candidate:** experiments/F56_clustered_inverse_relation_decoder/RESULT.md

**Pinned SHA-256:**
5fc697fe596b37b973813004a2463f5a234dc56c6be5f44a88d094a4a1b124d5

**Verdict: PASS.**

The corrected theorem is mathematically sound. Keeping one representative
from every nonempty equal-index class preserves the complete set of
modular-root images of exact square subsets. The distinct-index difference
theorem, discard rule, parity-kernel representation, homomorphism, basis-only
test, completion-fibre law, and stated complexity bounds all pass.

The result is ready for a strict proof-blind reconstruction under PROMPT.md.
It is not a factoring algorithm. It gives an exact implicit source law and a
complete decoder for a polynomial-width relation batch. It gives no all-input
theorem that such a batch contains a useful relation.

No research computation was used in this audit.

## 1. The repaired duplicate-index lemma passes

Fix one value

\[
A=Nk+1\equiv1\pmod N
\]

that occurs several times. Let an exact square subset select this value $t$
times. Remove selected copies in pairs until only $t\bmod2$ copies remain.
Each removed pair divides the selected product by $A^2$. If $X$ is its
positive square root, the new positive root is $X/A$. Modulo $N$,

\[
X/A\equiv X\pmod N,
\]

because $A\equiv1\pmod N$. Removing all such selected pairs preserves exact
squareness and the decoded modular root.

The resulting subset uses at most one copy from every class. It is available
in the batch that keeps one representative from each nonempty class.
Conversely, each subset of the one-representative batch is available in the
original batch by selecting one corresponding copy. Thus the two batches
have exactly the same modular-root images from exact square subsets.

This includes the prior counterexample. If $N=15$ and two copies of $k=1$
are present, then $A=16$. Keeping one representative preserves the useful
singleton root $4$. Reducing the available multiplicity modulo two would
delete both copies and would be false. The corrected candidate does not make
that error.

This lemma concerns relation values only. Two occurrences of the same
$Nk+1$ can carry different displayed factorizations. Such extra chronology
is outside this decoder, as the candidate states.

## 2. The completion-fibre law passes

Let $u\in U_N$. Let $v$ be its least positive inverse modulo $N$. Suppose

\[
D_N(u)=k.
\]

Then $uv=Nk+1$. If $k\ge1$, the inequalities $v<N$ and $u<N$ give
$u>k$ and $v>k$. For example, $Nk+1=uv<uN$ implies $k<u$. Thus $u$
is counted by

\[
f_N(k)=\#\{u:k<u<N,\ u\mid Nk+1\}.
\]

Conversely, suppose $k<u<N$ and $u\mid Nk+1$. Put

\[
v=\frac{Nk+1}{u}.
\]

The inequality $k<u$ gives $v<N$, while

\[
Nk+1-ku=k(N-u)+1>0
\]

gives $v>k\ge1$. Every common divisor of $u$ and $N$ divides $Nk+1$,
so $\gcd(u,N)=1$. Therefore $v$ is the canonical inverse of $u\bmod N$,
and $D_N(u)=k$. This proves

\[
D_N^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\]

For $k=0$, positivity gives $uv=1$, so $u=v=1$. Hence, for uniform
$U\in U_N$,

\[
\Pr(D_N(U)=k)=\frac{f_N(k)}{\varphi(N)}
\]

for $k\ge1$, and the zero atom is $1/\varphi(N)$. These fibres partition
$U_N$, so there is no normalization gap.

The sampler does not need to evaluate $f_N(k)$. A public draw from
$\{1,\ldots,N-1\}$, followed by a gcd screen, either already gives a proper
factor or, on the unit branch, is exactly uniform on $U_N$. Modular inversion
and the exact quotient then give the stated conditional sample. The source
law does not hide factorization or a weighted-sampling oracle.

## 3. Atom and independent-clustering bounds pass

For $1\le k<N$,

\[
f_N(k)\le\tau(Nk+1)\le\Delta_N,
\qquad
\Delta_N=\max_{1\le m<N^2}\tau(m).
\]

The same upper bound holds for the zero atom because $\Delta_N\ge1$.
Summing over a set of $h$ indices gives

\[
\Pr(D_N(U)\in I)\le\frac{h\Delta_N}{\varphi(N)}.
\]

For a fixed value of $K_i$, at most $2H+1$ values of an independent $K_j$
satisfy $|K_i-K_j|\le H$. Conditioning on $K_i$, applying the atom bound,
and taking a union bound over pairs gives

\[
\Pr(\exists i<j:|K_i-K_j|\le H)
\le
\binom T2\frac{(2H+1)\Delta_N}{\varphi(N)}.
\]

On balanced distinct semiprimes, $\varphi(N)=\Theta(N)$. The standard
maximal-order divisor bound gives $\Delta_N=N^{o(1)}$. The zero atom gives a
matching lower exponent scale, so the maximum atom can correctly be written
$N^{-1+o(1)}$. If $T$ and $H$ are polynomial in $\log N$, the pair bound is
$N^{-1+o(1)}$. This conclusion is limited to independent first-step samples
and simple short clusters. It says nothing about dependent descent tails or
other statistics.

## 4. Difference confinement passes

For distinct $k_i,k_j$, put $A_i=Nk_i+1$. Then

\[
A_i-A_j=N(k_i-k_j),
\qquad
\gcd(A_i,N)=1.
\]

It follows that

\[
\gcd(A_i,A_j)
=\gcd(A_i,N(k_i-k_j))
=\gcd(A_i,|k_i-k_j|).
\]

Suppose $\prod_{i\in S}A_i$ is a square. Fix $i\in S$. If a prime $\ell$
has odd valuation in $A_i$, the sum of its valuations in the other selected
values is odd. Thus at least one other selected $A_j$ has positive
$\ell$-valuation. The gcd identity gives $\ell\mid|k_i-k_j|$. Doing this
for each prime in the squarefree kernel gives

\[
\operatorname{sf}(A_i)
\mid
\prod_{\substack{j\in S\\j\ne i}}|k_i-k_j|.
\]

This argument remains valid when valuations exceed one. In a singleton
subset, the right side is $1$, so the statement says exactly that $A_i$ is
a square. If the index diameter is at most $H$, each prime in every selected
squarefree kernel is at most $H$.

Distinctness is essential. The candidate applies the one-representative
reduction before this argument, so it never applies the identity to a zero
difference.

## 5. The discard rule and exact kernel representation pass

After complete trial division by all primes $\ell\le H$, write

\[
A_i=R_i\prod_{\ell\le H}\ell^{e_{i,\ell}}.
\]

All prime factors of $R_i$ exceed $H$. If $R_i$ is not a square, it contains
such a prime to odd valuation. Difference confinement proves that this index
cannot occur in any square-product subset. The discard is complete.

For each retained index, write $R_i=s_i^2$. A binary selection vector $c$
gives a square product exactly when

\[
\sum_i c_i e_{i,\ell}\equiv0\pmod2
\]

for every $\ell\le H$. Thus the parity kernel represents all and only the
exact square subsets of the retained distinct batch. Its positive root is

\[
X(c)=
\prod_i s_i^{c_i}
\prod_{\ell\le H}
\ell^{\frac12\sum_i c_i e_{i,\ell}}.
\]

Because every $A_i\equiv1\pmod N$,

\[
X(c)^2\equiv1\pmod N.
\]

This proves both directions. The decoder does not factor the remaining large
square cofactor. It only uses an exact integer square-root test.

## 6. The homomorphism and basis-only detection pass

For kernel vectors $c,d$, binary addition is symmetric difference. The
indices selected twice contribute one extra full factor $A_i$ to the product
of the two positive roots. Exactly over the integers,

\[
X(c)X(d)
=X(c+d)\prod_{i:c_i=d_i=1}A_i.
\]

Reducing modulo $N$ gives

\[
X(c)X(d)\equiv X(c+d)\pmod N.
\]

Thus $c\mapsto X(c)\bmod N$ is a group homomorphism from the binary kernel
to the roots of $1$. If every basis image is globally $1$ or $-1$, every
kernel image lies in the same two-element subgroup. Conversely, if any
dependency has a nontrivial image, at least one basis vector has a nontrivial
image. A basis-only test is complete.

For odd $N$, the candidate's gcd extraction is exact. A root not globally
$\pm1$ has different signs on at least two prime-power components. A gcd with
$X-1$ or $X+1$ gives a proper factor. The implication also holds for even
$N\ge2$: if $X\not\equiv\pm1\pmod N$, both gcds are less than $N$, and they
cannot both be $1$ because $N\mid(X-1)(X+1)$. At least one is a proper
nontrivial divisor.

## 7. Bit complexity and the width schedule pass

Because $1\le k_i<N$, each $A_i=Nk_i+1$ is less than $N^2$ and has
$O(\log N)$ bits. Each of the following has cost polynomial in
$m+H+\log N$:

- sieve construction and the prime list through $H$;
- all trial divisions and recorded exponents;
- exact square-root tests for the $R_i$;
- binary linear algebra on the $m$-by-$\pi(H)$ parity matrix;
- exponent sums for each basis root;
- modular exponentiation, products, and gcd computations.

The decoder reduces products modulo $N$. It need not materialize a large
selected product. Even an unreduced product has $O(m\log N)$ bits. The bound
therefore includes intermediate bit lengths.

Section 4 fixes

\[
n=\lceil\log_2(N+1)\rceil,
\qquad
H(n)=n^C
\]

for one integer constant $C\ge1$ chosen independently of $N$. This is a
uniform polynomial schedule. The small-state pool has at most $H(n)-1$
inputs. Every gcd, modular inverse, exact quotient, and decoder operation has
polynomial bit cost. The upper limit $\min(H(n),N-1)$ handles small inputs.

For a unit state $u\ge2$, the equality $D_N(u)=0$ would force $uv=1$.
This is impossible. Hence

\[
1\le k=D_N(u)<u\le H(n).
\]

After deduplication, these indices are distinct and lie in an interval of
diameter less than $H(n)$. The decoder hypotheses hold.

## 8. Edge cases pass

- **Duplicate indices:** the one-representative lemma handles them exactly.
- **Singletons:** a singleton survives exactly when $A_i$ is a square. Its
  zero parity column then gives its exact root.
- **The zero fibre:** $k=0$ occurs only at $u=1$, gives $Nk+1=1$, and has
  only the trivial root. Excluding it loses no factor.
- **Prime inputs:** no nontrivial root of $1$ exists.
- **Odd prime powers:** their only roots of $1$ are $\pm1$, so no useful
  dependency image can occur.
- **Repeated prime factors:** the proof uses integer valuations and does not
  assume that $N$ is squarefree.
- **Even inputs:** the fibre and decoder identities remain valid. Any
  nontrivial root gives a proper gcd as proved above.
- **$N=15$:** $u=2$, $v=8$, $k=1$, and $Nk+1=16=4^2$. The root gives
  $\gcd(4-1,15)=3$.

## 9. Relation to P01, P62, and P64 passes

P01 blocks universally sound rank compression for arbitrary square classes.
F56 does not compress arbitrary inputs. It first proves that a true
dependency among short-interval generators cannot have odd prime support
above $H$. It discards generators that cannot participate and retains the
complete parity data for all primes through $H$. This is within P01's
structured-family exclusion.

P62 supplies the exact reverse fibres, strict descent, and relations

\[
u_i v_i=Nu_{i+1}+1.
\]

F56 gives a conditional decoder for a short interval. It does not improve
P62's $N^{1/2+o(1)}$ worst-case depth. It does not prove that a
polynomial-width tail is reached soon or that such a tail contains a useful
dependency.

P64 closes formal parity of repeated inverse-pair endpoint labels. F56 uses
the rational-prime valuation parity of the integer values $Nk_i+1$. The
$N=15$ singleton is an arithmetic square relation outside P64. There is no
contradiction or reopening of P64.

The candidate still calls this prior result the corrected F55 candidate in
two introductory sentences. It is now promoted as P64. Those references
should be updated before promotion of F56. This is a stale status label only.
It does not change the theorem or require another mathematical audit.

## 10. Scope and exact remaining gap

The corrected candidate states that public-difference support is necessary
but not sufficient. This is correct. Supported parity columns can remain
independent. A dependency can also map only to $1$ or $-1$.

The opening sentence of Section 5 is local to the clustered-decoder route,
as shown by its context and the next sentence. For maximum clarity, “A
factoring result now needs” should become “To turn this clustered decoder
into a factoring algorithm, one must”. This is a scope-clarity edit, not a
mathematical correction.

The result does not prove any of the following:

- a useful dependency exists for every input;
- the completion bias is correlated with an unknown factor;
- independent samples form a short cluster;
- a dependent descent reaches a useful tail in polynomial time;
- the relation-value kernel represents all information in richer trajectories;
- a lattice, continued-fraction, partial-relation, hidden-period, HSP, or
  stabilizer decoder fails;
- F26 is closed;
- a classical polynomial-time factoring algorithm or a lower bound.

The exact remaining lemma for this route is an all-input useful-relation law.
A polynomial-size, polynomial-width pool produced from bare $N$ must contain
a dependency with a nontrivial modular root often enough to give polynomial
expected time. F56 proves the evaluator after such a pool exists. It does not
prove that the pool exists.

## 11. Reconstruction readiness

All mathematical repairs required by the first audit are present and pass:

1. one-representative deduplication preserves every modular-root image;
2. difference confinement is used only after indices are distinct;
3. the nonsquare-cofactor discard is complete;
4. the parity kernel represents every remaining exact square subset;
5. the root map is a homomorphism, so a basis-only test is complete;
6. $H(n)=n^C$ is a fixed uniform polynomial schedule;
7. public-difference support is necessary, not equivalent or sufficient;
8. no all-input success theorem is claimed.

The candidate is ready for proof-blind reconstruction. The two recommended
wording updates in Sections 9 and 10 are editorial. They do not alter the
statement proved here.
