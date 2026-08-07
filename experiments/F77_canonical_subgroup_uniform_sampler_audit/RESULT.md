# F77 hostile audit — canonical subgroup sampler and separator density

## Verdict: PASS

I audited
`experiments/F77_canonical_subgroup_uniform_sampler/RESULT.md` at SHA-256

```text
7fd5bbec5485da405ecd71869f8caee2a7daa950e7eca1815f9f7de6b943449d
```

The hash matches the requested artifact. This was a proof-only audit. I ran
no research computation.

The sampler theorem, both sign-density formulas, the conditional Las Vegas
consequence, and the abstract density example are correct. The sampler does
not need the generator orders. The argument does not supply the generators
from \(N\), prove a density lower bound, realize the abstract example as an
integer family, or prove an all-input factoring algorithm.

The additive total-variation estimate in the candidate is enough
asymptotically. For completeness, Section 3 below proves a stronger
pointwise estimate. It removes any possible concern about small \(n\).

## 1. Near-uniform sampling without known orders

Let \(t_j=\operatorname{ord}_N(q_j)\). Since \(q_j\) is a unit,
\(t_j\) divides the size of the unit group and therefore \(t_j<N\leq 2^n\).
The algorithm does not compute or use \(t_j\); the orders occur only in the
proof.

Write \(M=a_jt_j+b_j\), with \(0\leq b_j<t_j\). Reduction of a uniform
integer in \(\{0,\ldots,M-1\}\) modulo \(t_j\) gives \(b_j\) residues with
\(a_j+1\) preimages and \(t_j-b_j\) residues with \(a_j\) preimages. Its
exact total-variation distance from uniform is

\[
\frac{b_j(t_j-b_j)}{Mt_j}
\leq \frac{t_j}{4M}
\leq \frac{t_j}{2M}.
\]

Total variation for a product of independent coordinates is at most the sum
of the coordinate distances. Also,

\[
M=2^{3n}2^{\lceil\log_2(s+1)\rceil}
\geq 2^{3n}(s+1).
\]

Hence the candidate's bound is valid:

\[
\sum_j\frac{t_j}{2M}
<\frac{s2^n}{2\,2^{3n}(s+1)}
<2^{-2n}.
\]

The map

\[
\prod_j\mathbb Z/t_j\mathbb Z\longrightarrow H,
\qquad(e_j)_j\longmapsto\prod_jq_j^{e_j}
\]

is a surjective homomorphism. Every fibre is a coset of its kernel, so exact
uniform input pushes forward to exact uniform output on \(H\). A deterministic
map cannot increase total variation. Taking the canonical integer
representative after this map does not change the distribution on group
elements. This proves Theorem 1.

Uniform sampling from a range of size \(M=2^L\) uses exactly \(L\) fair bits
per exponent. Modular repeated squaring uses polynomially many operations on
polynomial-bit integers. The stated \(O(s(n+\log s))\) random-bit bound and
polynomial bit-cost bound in \(s+n\) are therefore correct. No rejection
sampler, group-order computation, factorization, or hidden advice is used.

## 2. Exact positive, negative, and overlap counts

Assume \(N=pq\), where \(p\) and \(q\) are distinct odd primes. For uniform
\(X\in H\), the set \(X\equiv1\pmod p\) is the kernel of the projection
\(H\to H_p\), so it has probability \(1/|H_p|\). The analogous probability
at \(q\) is \(1/|H_q|\). Their intersection is the single identity of \(H\),
with probability \(1/|H|\). A proper positive-sign gcd occurs on the
symmetric difference. Thus

\[
\delta_+=\frac1{|H_p|}+\frac1{|H_q|}-\frac2{|H|}.
\]

For the negative sign, a fibre over \(-1\) is empty unless \(-1\) lies in the
projection image. When it is nonempty, it is one coset of the projection
kernel. The two local \(-1\) fibres intersect only in the unique global
element \(-1\pmod N\), and only when that element lies in \(H\). Therefore

\[
\delta_-=
\frac{\epsilon_p}{|H_p|}
+\frac{\epsilon_q}{|H_q|}
-\frac{2\epsilon}{|H|}.
\]

The candidate also handles the overlap correctly by refusing to add these
two formulas as disjoint probabilities. More explicitly, the intersection
of the positive- and negative-success sets consists only of the mixed-sign
CRT elements

\[
(1,-1)\quad\text{and}\quad(-1,1)
\]

that happen to lie in \(H\). If their membership indicators are
\(\eta_{+-}\) and \(\eta_{-+}\), then

\[
\Pr(S_+\cap S_-)=\frac{\eta_{+-}+\eta_{-+}}{|H|},
\]

so the two-sign success density is
\(\delta_++\delta_--(\eta_{+-}+\eta_{-+})/|H|\). The candidate makes no
incorrect combined-density claim.

## 3. Conditional Las Vegas claim, including small \(n\)

The additive total-variation bound gives actual sign-success probability at
least \(\delta_\pm-2^{-2n}\). This is inverse polynomial for all sufficiently
large \(n\) under the stated premise. There is also a direct stronger bound
that covers every small \(n\).

For one coordinate, every residue has probability at least \(a_j/M\).
Relative to uniform modulo \(t_j\), this is at least

\[
\frac{a_jt_j}{M}
=1-\frac{b_j}{M}
\geq1-\frac{t_j}{M}.
\]

Consequently every exponent vector has probability at least

\[
\prod_j\left(1-\frac{t_j}{M}\right)
\geq1-\sum_j\frac{t_j}{M}
>1-2^{-2n}
\]

times its probability under the exact uniform product law. Summing this
pointwise inequality over the preimage of any event in \(H\) gives

\[
\Pr_{\rm sampler}(X\in A)
\geq(1-2^{-2n})\Pr_{\rm unif(H)}(X\in A).
\]

Thus if either \(\delta_+\) or \(\delta_-\) is at least \(n^{-c}\), one trial
succeeds with probability at least
\((1-2^{-2n})n^{-c}\), for every \(N\geq3\). Testing both signs can only
increase this probability. Independent trials therefore have polynomial
expected count, and the probability of never succeeding is zero. A reported
proper gcd is checked by exact division, so the algorithm never returns a
false factor. The conditional Las Vegas statement is valid.

Its bit-cost is polynomial in \(s+n\), with the extra fixed factor \(n^c\)
in expectation. To use this as an \(N\)-only polynomial-time factoring
algorithm, a surrounding construction would still have to produce a
polynomial-size generator list and prove the density premise. F77 does not
claim either result.

## 4. Abstract density example

Let \(C_L=\langle a\rangle\) have even order \(L\), and interpret
\(-1=a^{L/2}\). The diagonal subgroup generated by \((a,a)\) has order
\(L\). Its intersection with the order-two subgroup generated by
\((1,-1)\) is trivial: equality would require one common power of \(a\) to
be both \(1\) and \(-1\). Hence

\[
H=\langle(a,a),(1,-1)\rangle
\]

has order \(2L\). Each projection is all of \(C_L\), so Theorem 2 gives

\[
\delta_+=\frac1L+\frac1L-\frac2{2L}=\frac1L.
\]

Direct counting agrees: the two positive separators are \((1,-1)\) and
\((-1,1)\), among \(2L\) elements. Thus the example correctly separates
existence of a separator from its density under uniform subgroup sampling.

The example is explicitly abstract. It does not assert an infinite family
of moduli, a factor-free construction of the displayed generators, or a
hardness result for sparse-word selection. The later sentence about an
exponential realizable local order is conditional, and the final section
again states that no all-input density theorem or factoring algorithm has
been proved. No realizability or all-input claim is smuggled into F77.

## Scope not certified by this audit

The references to P78/F75 and the statement about that fixed historical
state are not needed for F77's proofs and were not re-audited here. This
audit certifies the pinned theorem and its stated scope, not those external
historical records.
