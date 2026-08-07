# F56 fresh hostile whole-proof audit

## Artifact and verdict

**Candidate:** `experiments/F56_clustered_inverse_relation_decoder/RESULT.md`

**Pinned SHA-256:**
`f32310a0fae8bf0d5994575b5b46d42b0bd508094d98037f454ce6265301c3cf`

**Verdict: FAIL AS WRITTEN.**

The main distinct-index theorem is correct. The completion-biased law, the
short-interval square-class representation, and the basis-only decoder all
survive this audit. However, the claimed repeated-index preprocessing is
false. It can delete the only useful relation and then certify a false
negative. This is a theorem-level error because Section 3 claims completeness
for batches after this preprocessing.

There is also one scope error in the final section: support on the public
difference set is necessary for a clustered square relation, but it is not
equivalent to the existence of a useful parity dependency. The factoring
requirement must be stated only for this decoder, not for factoring in
general.

No research computation was used in this audit.

## 1. Decisive error: batch multiplicities cannot be reduced modulo two

Lines 220--224 say to reduce repeated-index multiplicities modulo two before
running the decoder. This is false as a preprocessing operation on the
available batch.

Take

\[
N=15,
\qquad k_1=k_2=1,
\qquad A_1=A_2=Nk_i+1=16.
\]

The original two-copy batch contains the singleton subset \(\{1\}\). Its
product is

\[
A_1=16=4^2,
\]

and its modular root factors \(N\):

\[
\gcd(4-1,15)=3.
\]

Reducing the batch multiplicity \(2\) modulo two deletes both copies. The
resulting empty batch has no kernel vector that returns \(4\). The decoder
would therefore miss a useful relation that existed in the submitted batch.

The sentence about deleting a pair proves only a statement about an already
chosen subset. If a chosen subset contains two identical copies, deleting
that selected pair changes its square root by

\[
A_i\equiv1\pmod N.
\]

It does not permit deleting all copies from the available batch before the
subset is chosen. With two available copies, a subset can still select one of
them.

The exact repair is simple: replace every nonempty repeated-index class by
**one representative**, independent of whether its batch multiplicity is odd
or even. For any chosen subset, reduce the number selected from that class
modulo two. A selected pair contributes \(A_i^2\), and its positive square
root contributes \(A_i\equiv1\pmod N\). Thus every original subset has the
same modular-root image as a subset of the one-representative batch. Conversely,
every subset of the one-representative batch is available in the original
batch by choosing one copy from each selected class.

This repair preserves the set of modular-root images. Reduction of the
*available multiplicity* modulo two does not.

## 2. The reverse-fibre sampling law passes

For \(1\le k<N\), P62 gives

\[
D_N^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\]

Every divisor in this set is automatically a unit modulo \(N\), because it
divides \(Nk+1\), which is coprime to \(N\). Its complementary divisor is
also the least positive inverse and lies strictly between \(k\) and \(N\).
Therefore the fibre size is exactly \(f_N(k)\), and uniform \(U\in U_N\)
gives

\[
\Pr(D_N(U)=k)=\frac{f_N(k)}{\varphi(N)}.
\]

The zero fibre is also exact. If \(D_N(u)=0\), then \(uv=1\) over the
positive integers, so \(u=v=1\). Hence

\[
f_N(0)=1,
\qquad
\Pr(D_N(U)=0)=\frac1{\varphi(N)}.
\]

These fibres partition \(U_N\), so the stated law is normalized. No hidden
evaluation of the weights is required to sample it.

## 3. Atom and independent-clustering bounds pass

For \(k\ge1\),

\[
f_N(k)\le \tau(Nk+1)\le\Delta_N,
\]

and the same bound holds at zero because \(\Delta_N\ge\tau(1)=1\).
Therefore a set of \(h\) indices has probability at most

\[
\frac{h\Delta_N}{\varphi(N)}.
\]

For each independent pair \((K_i,K_j)\), condition on \(K_i\). At most
\(2H+1\) values of \(K_j\) satisfy \(|K_i-K_j|\le H\). The atom bound and
a union bound over pairs give exactly

\[
\Pr(\exists i<j:|K_i-K_j|\le H)
\le
\binom T2\frac{(2H+1)\Delta_N}{\varphi(N)}.
\]

For balanced distinct semiprimes, \(\varphi(N)=\Theta(N)\), while the
standard divisor bound gives \(\Delta_N=N^{o(1)}\). Thus polynomially many
independent samples and polynomial interval width have negligible cluster
probability. The candidate correctly excludes dependent trajectory tails and
all other statistics from this conclusion.

## 4. Difference confinement and valuation multiplicities pass

For distinct indices,

\[
A_i-A_j=N(k_i-k_j),
\qquad
\gcd(A_i,N)=1.
\]

It follows that

\[
\gcd(A_i,A_j)=\gcd(A_i,|k_i-k_j|).
\]

Now suppose \(\prod_{i\in S}A_i\) is a square. Fix \(i\in S\) and a prime
\(\ell\) whose valuation in \(A_i\) is odd. The total valuation in the
selected product is even, so

\[
\sum_{j\in S\setminus\{i\}}v_\ell(A_j)
\]

is odd. In particular, at least one other selected value has positive odd
valuation at \(\ell\). The gcd identity then makes \(\ell\) divide the
corresponding public index difference. Doing this for every distinct prime in
the squarefree kernel proves

\[
\operatorname{sf}(A_i)
\mid
\prod_{j\in S\setminus\{i\}}|k_i-k_j|.
\]

This proof correctly handles arbitrary valuation multiplicities. It does not
assume that a shared prime occurs only once. For a singleton, the product on
the right is \(1\), so the statement is exactly that \(A_i\) has trivial
squarefree kernel, or equivalently that \(A_i\) is a square.

If the distinct indices have diameter at most \(H\), every prime in a
selected squarefree kernel is at most \(H\). This is a necessary condition
for every exact square relation.

## 5. The distinct-index decoder passes

After all primes \(\ell\le H\) are divided out of \(A_i\), let the cofactor
be \(R_i\). If \(R_i\) is not a square, it has a prime greater than \(H\)
to odd valuation. Section 4 shows that such an index cannot occur in any
square-product subset of a distinct-index batch. The discard step is therefore
complete.

Conversely, for every retained index write \(R_i=s_i^2\). A kernel vector
for the small-prime exponent parities makes each total exponent even. Hence

\[
X(c)=
\prod_i s_i^{c_i}
\prod_{\ell\le H}
\ell^{\frac12\sum_i c_i e_{i,\ell}}
\]

is the exact positive integer square root of the selected product. Every
\(A_i\) is \(1\bmod N\), so \(X(c)^2\equiv1\pmod N\).

This proves both directions for distinct indices:

- every exact square-product subset survives the discard and gives a parity
  kernel vector;
- every parity kernel vector gives an exact integer square product.

The decoder therefore represents all exact square-product subsets of the
distinct batch. It does not assert that a nonzero kernel exists or that its
root is useful.

## 6. The homomorphism and basis-only test pass

Binary addition is symmetric difference. For kernel vectors \(c,d\), the
indices selected twice contribute one extra factor \(A_i\) to the product of
the two positive square roots. Therefore

\[
X(c)X(d)
=X(c+d)\prod_{i:c_i=d_i=1}A_i
\equiv X(c+d)\pmod N.
\]

Thus \(c\mapsto X(c)\bmod N\) is a homomorphism. The two global roots
\(\{1,-1\}\) form a subgroup. If every basis image lies in this subgroup,
then every kernel image lies in it. Hence any nontrivial image forces at least
one basis vector to have a nontrivial image. Testing a basis is sufficient;
enumerating all kernel vectors is unnecessary.

For odd

\[
N=\prod_r p_r^{\alpha_r},
\]

every root of \(1\) is independently \(1\) or \(-1\) modulo each prime
power. This follows because \(p_r^{\alpha_r}\mid(X-1)(X+1)\) and the two
factors have no common odd prime divisor. A root that is not globally
\(\pm1\) has mixed signs across distinct prime-power components. Its two gcds
with \(X-1\) and \(X+1\) therefore expose complementary proper factors.
For an odd prime power, no nontrivial root exists, so the implication remains
valid. The candidate's extraction statement correctly includes repeated
prime powers.

## 7. Bit complexity passes after fixing the width schedule

Each \(A_i=Nk_i+1\) has \(O(\log N)\) bits. A sieve up to \(H\), trial
division by all primes up to \(H\), exact square-root tests, binary linear
algebra on at most \(m\) by \(\pi(H)\) bits, modular exponentiation, and gcd
computations all use time polynomial in \(m+H+\log N\). The exponent sums in
the definition of \(X(c)\) also have polynomial bit length. The algorithm
does not factor the remaining large square cofactors.

To support the phrase “one uniform deterministic polynomial-time algorithm,”
Section 4 should fix an explicit computable width, for example
\(H(n)=n^C\) for one fixed constant \(C\), where \(n=\lceil\log_2N\rceil\).
The current phrase “fix \(H=\operatorname{poly}(\log N)\)” describes the
correct complexity regime but does not itself select one uniform schedule.
This is a specification repair, not a mathematical obstruction.

## 8. The small-state pool and the exact example pass

For every factor-free state \(2\le u\le\min(H,N-1)\), P62 gives

\[
1\le D_N(u)<u\le H.
\]

After keeping one representative of each resulting index, the values lie in
a public interval of diameter at most \(H\). The distinct-index decoder
therefore applies. The construction is deterministic and polynomial-time for
an explicit polynomial width schedule.

The \(N=15\) example is exact:

\[
2^{-1}\equiv8\pmod {15},
\qquad
D_{15}(2)=1,
\qquad
15\cdot1+1=16=4^2,
\]

and \(\gcd(4-1,15)=3\). It proves only one successful instance. The
candidate correctly states that it is not a success theorem.

The same decoder can be applied to distinct successor states in a late
descent interval. The chronology supplies \(Nk_i+1=u_i v_i\), but this
decoder does not use those factorizations. No hit probability or polynomial
trajectory-depth claim follows.

## 9. The “equivalently” sentence is too strong

Lines 269--273 say that a factoring result needs a useful parity dependency
and then call it equivalent to manufacturing enough values whose squarefree
kernels are supported on the public difference set.

These are not equivalent. Difference support is necessary for an exact
square dependency, but it is not sufficient. The parity vectors of many
supported squarefree kernels can still be linearly independent. A dependency
can also decode only to \(1\) or \(-1\), which gives no factor.

The correct conclusion is narrower:

> To turn this clustered decoder into a factoring algorithm, one must prove
> that a polynomial-size, polynomial-width pool contains an efficiently
> represented dependency with a nontrivial modular root often enough. Support
> on public differences is one necessary structural condition for such a
> dependency.

This is a requirement for this decoder route. It is not a necessary form for
all possible factoring algorithms.

## 10. Comparison with P01, P62, and corrected F55

### P01

P01 blocks a lower-rank universally sound linear sketch for arbitrary square
classes. F56 does not contradict it. F56 first proves that its special
short-interval generators have no odd prime support above \(H\) inside a
true dependency. It then keeps the complete parity data for every prime up to
\(H\). This is structural rank control for a special family, not generic
compression. F56 must retain the short-interval and exact-generator premises.

### P62

P62 supplies the exact fibres, strict descent, and values

\[
u_i v_i=Nu_{i+1}+1.
\]

F56 neither improves the promoted \(N^{1/2+o(1)}\) worst-case depth bound nor
proves a useful tail occurs. It gives a conditional decoder once a
polynomial-width batch is available. F26 remains open.

### Corrected F55

The corrected F55 artifact has SHA-256
`028d41a7db2f4600964aeb24a9547bd614f080a84ec438f09fbf14fd78d86c07`.
It proves that formal endpoint-label parity on inverse pairs has no new
factoring power after direct self-loop screening. It explicitly leaves true
integer square-class parity open.

F56 works in that open arithmetic layer. Its columns are the square classes
of the integers \(Nk_i+1\), not the formal endpoint-incidence columns. The
\(N=15\) singleton is exactly the kind of arithmetic relation that F55 leaves
open. F56 does not reopen or contradict F55.

## 11. Scope exclusions that pass

The candidate correctly does **not** claim any of the following:

- that a useful parity dependency exists on all inputs;
- that independent completion-biased samples form short clusters;
- that a dependent descent tail has the independent sampling law;
- that the descent has polynomial depth;
- that the decoder finds every factor or every useful relation from richer
  endpoint factorizations;
- that a lattice, continued-fraction, large-prime, hidden-period, HSP, or
  stabilizer method is closed;
- that Shor's circuit is classically simulatable;
- that F26 is closed;
- that the result is a factoring algorithm or a factoring lower bound.

The sentence at lines 238--241 is correctly conditional: for the stated
distinct small-state pool, the basis decoder returns a factor if that pool
contains an exact square subset with a nontrivial root. It does not promise
that the condition occurs.

## 12. Required repair before re-audit

1. Replace multiplicity-mod-two preprocessing with one-representative
   deduplication, and prove preservation of all modular-root images.
2. Restrict the completeness theorem to distinct indices until that repaired
   deduplication lemma has been stated.
3. Replace the false “equivalently” claim with the necessary-but-not-sufficient
   difference-support condition.
4. State that the remaining success requirement belongs to this clustered
   decoder route, not to factoring algorithms in general.
5. Fix the pervasive inline-math delimiters such as `(u\in U_N)` so the
   artifact renders its formulas as mathematics.
6. For the concrete uniform algorithm, select an explicit computable
   polynomial width schedule.

After these repairs, the narrow result is nontrivial: it gives an exact biased
source law and a complete polynomial-time arithmetic square decoder for
distinct values in a polynomial-width index interval. It still supplies no
all-input useful-relation theorem and no factoring algorithm.
