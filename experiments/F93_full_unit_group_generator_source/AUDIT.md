# Hostile proof-only audit: PASS with two wording corrections

The audited RESULT.md has SHA-256
a198049a27b409516926c716b3ea281c95b430cd6c3382abc3de0a3a4ee764c5,
which matches the pinned value.

The exact finite-abelian generation formula, universal positive constant,
all-input factor-or-generate source, semiprime three-sample bound,
factor-bearing-unit construction, feedback subgroup interpretation, and
promise-decoder reduction are correct.

Two statements need precise wording:

1. Exact uniform sampling from a general interval using fair bits has
   expected polynomial random-bit cost, not a finite worst-case bit bound,
   unless uniform bounded-integer sampling is taken as a primitive.
2. The theorem does not prove that recovering an exponent vector is
   classically hard. It proves only that no recovery algorithm or public word
   is supplied. “Can be classically hard” should be presented as motivation,
   not as a proved lower bound.

Neither correction changes the source theorem or the expected-polynomial
Las Vegas reduction.

## 1. Exact generation formula for a finite abelian group

Let

\[
H=\prod_{\ell\mid |H|}H_\ell
\]

be the Sylow decomposition. A uniform element of \(H\) has independent
uniform Sylow coordinates. For each prime \(\ell\), multiplication by
\(\ell\) is an automorphism on every Sylow component other than
\(H_\ell\), so

\[
H/\ell H\simeq H_\ell/\ell H_\ell
\simeq\mathbb F_\ell^{r_\ell}.
\]

For a finite abelian \(\ell\)-group, a set generates the group exactly when
its image generates the Frattini quotient \(H_\ell/\ell H_\ell\). Thus
\(d\) uniform elements generate \(H_\ell\) exactly when the corresponding
\(r_\ell\times d\) matrix over \(\mathbb F_\ell\) has full row rank.

The number of ordered full-row-rank matrices is

\[
(\ell^d-1)(\ell^d-\ell)\cdots
(\ell^d-\ell^{r_\ell-1}).
\]

After division by the total \(\ell^{dr_\ell}\), the probability is

\[
\prod_{i=0}^{r_\ell-1}(1-\ell^{i-d}).
\]

Generation events for different Sylow components depend on independent
coordinates. Therefore the exact full-group probability is

\[
\boxed{
\prod_{\ell\mid |H|}
\prod_{i=0}^{r_\ell-1}(1-\ell^{i-d})
}.
\]

This also handles a trivial Sylow component, which contributes no factor,
and the trivial group, whose empty product is one.

## 2. The universal constant is strictly positive

For every prime \(\ell\) and \(k\geq2\),

\[
0<\ell^{-k}\leq\frac14.
\]

The elementary bound

\[
-\log(1-u)\leq\frac{u}{1-u}\leq\frac43u
\qquad(0\leq u\leq1/4)
\]

gives

\[
\sum_{\ell}\sum_{k=2}^{\infty}
-\log(1-\ell^{-k})
\leq
\frac43
\sum_{\ell}\sum_{k=2}^{\infty}\ell^{-k}.
\]

Also,

\[
\sum_{\ell}\sum_{k=2}^{\infty}\ell^{-k}
=\sum_{\ell}\frac1{\ell(\ell-1)}
<
\sum_{m=2}^{\infty}\frac1{m(m-1)}
=1.
\]

The logarithmic series converges, so the infinite product defining \(c_0\)
is positive, with the stated strict bound

\[
c_0>e^{-4/3}.
\]

Now assume \(|H|<2^n\). Since

\[
|H/\ell H|=\ell^{r_\ell}\leq|H|<2^n
\]

and \(\ell\geq2\), one has \(r_\ell\leq n-1\). With \(d=n\), every factor in
the exact formula is

\[
1-\ell^{-k}\qquad(k=n-i\geq2).
\]

The finite probability product contains only a subset of the factors in
\(c_0\). Omitting factors in \((0,1)\) increases a product, so the
probability is at least \(c_0\). The corollary is correct.

## 3. The all-input factor-or-generate batch

Assume \(N\geq2\), as is implicit in a factoring input, and set

\[
n=\lceil\log_2(N+1)\rceil.
\]

Then \(N<2^n\), while

\[
|G_N|=\varphi(N)<N.
\]

The set \(\{1,\ldots,N-1\}\) contains each nonzero residue exactly once.
Conditioning a uniform sample from this set on being a unit therefore gives
the exact uniform distribution on \(G_N\). Because the samples are
independent and the conditioning event is a product of one-sample events,
an all-unit batch remains a product of independent uniform unit
distributions.

If a sample is not a unit, then

\[
1<\gcd(a_i,N)\leq a_i<N,
\]

so the gcd is automatically a proper factor. Let

\[
\alpha=\frac{\varphi(N)}{N-1}.
\]

The probability of an all-unit batch is \(\alpha^n\). Conditioned on that
event, Corollary 2 gives a generating list with probability at least \(c_0\).
Thus

\[
\Pr(\text{factor or full generating list})
\geq
1-\alpha^n+\alpha^n c_0
=1-\alpha^n(1-c_0)
\geq c_0.
\]

No independence mistake or missing conditioning factor occurs.

There are \(O(\log N)\) samples and gcds. Each successful bounded-integer
draw and gcd has polynomial bit cost. With fair random bits, exact sampling
can be implemented by rejection from
\(\lceil\log_2(N-1)\rceil\)-bit strings; each attempt succeeds with
probability greater than one half. Its random-bit and running-time cost is
therefore expected \(O(\log N)\) per sample, with an exponentially decaying
tail but no finite worst-case bound. The candidate's later
expected-polynomial Las Vegas claim is unaffected.

## 4. Three samples for a distinct odd semiprime

For \(N=pq\) with distinct odd primes,

\[
G_N\simeq C_{p-1}\times C_{q-1}.
\]

Every Sylow subgroup is a product of at most two cyclic groups, so
\(r_\ell\in\{0,1,2\}\). Substituting \(d=3\) into the exact formula gives

\[
\prod_{\ell:r_\ell=1}(1-\ell^{-3})
\prod_{\ell:r_\ell=2}
(1-\ell^{-3})(1-\ell^{-2}).
\]

For a prime of rank zero, both factors are omitted; for rank one, the
\((1-\ell^{-2})\) factor is omitted. Since omitted factors lie in
\((0,1)\), the actual finite product is at least

\[
\prod_{\ell\ {\rm prime}}
(1-\ell^{-2})(1-\ell^{-3})
=\frac1{\zeta(2)\zeta(3)}.
\]

This is a positive absolute constant. Repeated prime powers in \(p-1\) or
\(q-1\) do not increase the generator rank beyond two; the Frattini quotient
already accounts for them.

Applying the same conditioning calculation to three raw nonzero residues
gives

\[
1-\alpha^3+\alpha^3
\frac1{\zeta(2)\zeta(3)}
\geq
\frac1{\zeta(2)\zeta(3)}.
\]

Thus the semiprime factor-or-generate statement is correct.

## 5. The full unit group is factor-bearing for every composite

### Prime powers

Let \(N=p^e\) with \(e\geq2\). The integer

\[
x=1+p
\]

is a unit modulo \(p^e\), and

\[
\gcd(x-1,N)=\gcd(p,p^e)=p.
\]

This is nontrivial and proper. It includes \(p=2\), so the later
power-of-two sentence is redundant but correct.

### At least two distinct prime divisors

Choose an odd exact prime-power component \(p^e\Vert N\). Such a component
exists unless \(N\) is a power of two, already handled above. Put

\[
M=N/p^e.
\]

The two moduli \(p^e,M\) are coprime and \(M>1\). CRT supplies a residue
\(x\) satisfying

\[
x\equiv-1\pmod{p^e},
\qquad
x\equiv1\pmod M.
\]

It is a unit in both components and hence modulo \(N\). Since \(p\) is odd,

\[
p\nmid x-1.
\]

Therefore

\[
\gcd(x-1,N)=M,
\]

which is nontrivial and proper. This covers composites with an even
prime-power component and at least one odd component as well as odd
composites.

All composite cases are covered. The proof is existential and does not
publicly construct \(x\) without the hidden factorization.

## 6. Feedback interpretation

Condition on an all-unit batch satisfying

\[
\langle a_1,\ldots,a_n\rangle=G_N.
\]

Every later residue that is a unit modulo \(N\) already belongs to this
generated subgroup. On a no-factor canonical-refinement branch, factors of
integer endpoints that are units are themselves units: a divisor of an
integer coprime to \(N\) is also coprime to \(N\). Hence feedback cannot
strictly enlarge the abstract residue subgroup on this conditioned batch.

There is also a short existential representation bound. If a feedback
residue \(x\) is represented by

\[
x=\prod_i a_i^{e_i},
\]

each exponent can be reduced modulo
\(\operatorname{ord}(a_i)\leq|G_N|<N\). With
\(n=O(\log N)\), the complete exponent vector has
\(O((\log N)^2)\) bits.

What does not follow is an efficient public method to recover that vector.
The theorem proves an existence statement and supplies no word-recovery
algorithm. The candidate's phrase “can be classically hard to recover”
should not be read as a proved complexity lower bound.

The listed accessibility gains remain valid: feedback can expose a named
integer, a gcd-free block, relation provenance, or a direct decoder input
even when its residue was already an unknown word in the full-group
generators.

## 7. Promise-decoder reduction

Suppose there is one polynomial \(P\) such that, on every list generating
\(G_N\), the promised procedure returns a verified proper factor with
probability at least \(1/P(\log N)\). Assume, as the candidate does, that
its work is polynomially bounded on every list and that all other outcomes
are explicit failure.

Run fresh factor-or-generate batches. A nonunit sample directly returns a
verified factor. On an all-unit batch, run the procedure without attempting
to recognize whether the list generates \(G_N\).

Let \(F\) be the event that the batch directly finds a factor and \(J\) the
event that it produces a full generating list. Theorem 3 proves

\[
\Pr(F\cup J)\geq c_0.
\]

On \(F\), success probability is one; on \(J\), it is at least
\(1/P(\log N)\). Therefore one iteration succeeds with probability at least

\[
\frac{\Pr(F)+\Pr(J)}{P(\log N)}
\geq
\frac{c_0}{P(\log N)}.
\]

The procedure's polynomial cap on non-generating lists prevents an
unpromised batch from hanging. Fresh repetition has geometric expected
iteration count \(O(P(\log N)/c_0)\). Exact sampling has expected polynomial
cost, and every returned factor is verified. The result is a classical
Las Vegas expected-polynomial factorer for every composite \(N\).

The reduction neither recognizes the generating-list promise nor supplies
the missing factor-localization procedure.

## 8. Scope judgment

The source theorem is correct and genuinely applies to every composite
\(N\). It supplies a constant-probability public generator list for the full
unit group, or an immediate factor. It does not localize a factor-bearing
element, compute group orders, recover exponent words, solve a hidden
subgroup problem, or prove a factoring algorithm without the promised
decoder.

Verdict: **PASS**, with the two wording corrections stated at the start.
