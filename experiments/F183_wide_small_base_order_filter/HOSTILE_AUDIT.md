# F183 hostile audit

## Verdict

**PASS — no theorem-level defect found.**

I verified the frozen inputs before auditing them:

- `STATEMENT.md`: `1505042cdb44c0ef000c70638e53be12f2a07b160c5f9c3adddac543f0e4c67d`
- `PROOF.md`: `291ecb0f8e45dea06833ee287fd44b591dc108a7f57fc8e92173ef5a95a2616f`

The result is a conditional QP postprocessor for the F181 rough branch. It
does not prove an all-input factoring algorithm. The word “hard” in the
last branch has exactly the quantified meaning in (11) of the statement;
it does not assert a general factoring lower bound.

No mathematical computation was used. This is a proof-only audit.

## Imported interface and quantifiers

The proof needs only the following F181 rough-branch data. The public value
\(w\) is a unit, and for every maximal hidden prime-power component
\(R_j=p_j^{\alpha_j}\),

\[
g_j=\operatorname{ord}_{R_j}(w)>1,\qquad
\gcd(g_j,N)=1,\qquad P^-(g_j)>T.
\]

These are exactly the F181 guarantees. F181 in turn imports from P160 a
public unit whose nontrivial local orders are coprime to \(N\), so the
prime-power argument below does not assume squarefreeness. F181 permits any
fixed integer-valued numerical QP cap. Therefore, for fixed
\(c,d,C\geq1\), it can be instantiated with a cap satisfying
\(T\geq L+1\), together with any earlier lower bounds required by P160.
There is no circular choice of \(T\): \(K\) and \(L\) depend only on \(n\)
and the fixed constants.

The complexity claim is uniform in \(N\) for each fixed choice of
\(c,d,C\). It does not quantify over those constants as part of the input.

## Exact primary filtering

Fix \(\ell^e\parallel g_j\). Since an element order modulo
\(R_j\) is less than \(R_j\),

\[
\ell^e\leq g_j<N<2^n,
\]

and hence \(e<n\). For each menu base \(a\), there are exactly two ways
for \(\ell\) to divide \(C_a\):

1. \(\ell\mid a\); or
2. \(a\) is a unit modulo \(\ell\) and \(\ell\mid a^k-1\) for some
   \(1\leq k\leq K\).

The second condition is equivalent to
\(\operatorname{ord}_\ell(a)\leq K\): divisibility for a listed \(k\)
implies that the order divides \(k\), and an order at most \(K\) appears
itself among the listed exponents. Thus the proof identifies the prime
support of \(P\) exactly, not only in one direction.

If \(\ell\mid P\), then

\[
v_\ell(P^n)=n v_\ell(P)\geq n>e,
\]

so the complete \(\ell^e\)-primary part of \(g_j\) is removed. If
\(\ell\nmid P\), none of it is removed. The order-of-a-power formula
therefore gives exactly \(h_j\); partial primary survival is impossible.

On the actual F181 input, every \(\ell\mid g_j\) satisfies
\(\ell>T\geq L+1\), while \(2\leq a\leq L+1\). Hence
\(\ell\nmid a\) automatically. Including the factor \(a\) in \(C_a\)
does not change the rough-input branch, but it makes the stated general
prime-support equivalence valid.

## Arbitrary odd composites and hidden prime powers

For \(R_j=p_j^{\alpha_j}\), reduction

\[
(\mathbb Z/R_j\mathbb Z)^\times\longrightarrow
(\mathbb Z/p_j\mathbb Z)^\times
\]

has a \(p_j\)-group kernel. The order \(h_j\) divides \(g_j\), and
\(p_j\nmid g_j\). Thus the kernel meets \(\langle z\rangle\) trivially,
so reduction is injective on that subgroup. Consequently,

\[
z\equiv1\pmod {p_j}
\iff z\equiv1\pmod {R_j}
\iff h_j=1.
\]

This rules out the dangerous case in which a gcd contains only a proper
power of a hidden rational prime. The gcd \(H\) is exactly a product of a
subset of the maximal components \(R_j\). It is therefore either \(1\),
\(N\), or a proper factor. This remains valid when \(N\) itself is a prime
power; in that case only the first two possibilities can occur.

If \(H=1\), every \(h_j\) is nontrivial. Its prime support is contained in
that of \(g_j\), so it is \(T\)-rough and exceeds \(T\). The exact filter
then gives, for every \(\ell\mid h_j\) and every listed base \(a\), both
\(\ell\nmid a\) and \(\operatorname{ord}_\ell(a)>K\). All quantifiers in
the hard-descendant branch follow.

## The \(H=N\) factor-first synchronization

If \(H=N\), then every \(h_j=1\). Exact primary filtering shows that every
prime power in every \(g_j\) is covered by \(P^n\), with sufficient
valuation, so \(g_j\mid P^n\) for all \(j\).

During stripping, maintain the invariant \(g_j\mid M\) for every \(j\).
For a prime \(r\mid M\), apply the same prime-power injectivity argument to
\(w^{M/r}\), whose order is still coprime to every prime dividing \(N\).
It gives the exact classification

\[
D_r=N \iff (\forall j)\ g_j\mid M/r,
\]

\[
D_r=1 \iff (\forall j)\ g_j\nmid M/r,
\]

and any mixture is a proper factor. Thus an \(N\)-valued test safely
removes one copy of \(r\), while a one-valued test proves that every local
order uses the full current \(r\)-adic valuation of \(M\).

Later removal of another prime cannot invalidate a previous one-valued
test: the later candidate \(M/r\) only becomes a divisor of the exponent
already rejected by every local order. At termination, every prime left in
\(M\) occurs to its full current valuation in every \(g_j\); every prime
removed completely from \(M\) occurs in none. Hence

\[
g_j=M\qquad(1\leq j\leq s).
\]

This proves exact common order, not merely a common multiple. Moreover,
\(M=g_j\geq P^-(g_j)>T\). The returned state is the original F181 unit
\(w\) together with the surviving factored integer \(M\), so the proof does
not mistake the identity descendant \(z\) for a large-order element.

## Duplicate valuations and complete factorization

Trial division gives the full factorization of every \(C_a\). Summing
valuations for the same rational prime, both within a single \(C_a\) and
across different bases, gives

\[
v_r(P)=\sum_{a=2}^{L+1}v_r(C_a)
\]

exactly. The factorization of \(P^n\) then has valuation
\(n v_r(P)\). The stripping loop removes copies one at a time, so repeated
factors are neither collapsed nor silently lost. No pairwise-coprimality
assumption on the \(C_a\) is present or needed.

## Uniform deterministic QP bounds

For every listed base,

\[
\log_2 C_a
\leq \log_2 a+\sum_{k=1}^K k\log_2 a
=O(K^2\log L).
\]

Exhaustive trial division through \(\sqrt{C_a}\), including polynomial
integer-division overhead, therefore costs
\(2^{O(K^2\log L)}\) bit operations. Multiplication by the \(L\) menu
entries preserves the form \(2^{(\log n)^{O(1)}}\), because \(K\) is
polylogarithmic in \(n\) and \(L=2^{(\log n)^{O(1)}}\).

The complete product has

\[
\log_2P=O(LK^2\log L),
\]

and the explicitly represented exponent \(P^n\) has
\(O(nLK^2\log L)\) bits. Both lengths are QP in the input bit length
\(n\). Product construction, integer powering, and binary modular powering
are polynomial in these lengths and remain QP.

Finally, the number of stripping attempts is at most the total prime
multiplicity of \(P^n\), which is at most \(\log_2(P^n)\). Every tested
exponent has no more than that many bits. This also gives a uniform QP
bound for the complete factor-first stage.

## Final assessment

The attacks on partial primary deletion, non-squarefree gcd behavior,
unequal local orders, repeated annihilator factors, trial-factorization
cost, and quantifier scope do not produce a counterexample. The three
terminal results are exhaustive under the stated F181 premise:

\[
\boxed{
\text{factor}\ \lor\
\text{factored exact common local order above }T\ \lor\
\text{nontrivial }T\text{-rough descendant satisfying every small-base bound}
}.
\]

**Exact verdict: PASS — no theorem-level defect found.**
