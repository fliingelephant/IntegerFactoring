# F145 V2 hostile audit — PASS

## Frozen inputs

I audited only the revised proof-only candidate:

- `V2_STATEMENT.md`:
  `9b7b5b21b65222be8a522163e4686dca7a232c94b87645d062dc017088eee18e`;
- `V2_PROOF.md`:
  `435877c8bb5fbf6791f280bd7e9e4bd8d5764e66e16971138cda4491287effc8`.

Both hashes matched before the audit. I did not modify either frozen file.
I used no research computation.

I also read the V1 hostile audit and the failed V1 statement-only
reconstruction. The latter found one precise scope defect: V1 inferred an
exponentially small total Krylov-rank mismatch probability without bounding
the algebra rank.

## Verdict

**PASS.** V2 repairs the V1 defect exactly. I found no false theorem,
missing hypothesis, or quasipolynomial complexity overclaim in the revised
candidate.

F145 remains a boundary theorem. It is not a factoring algorithm, and it is
not a lower bound against general finite-algebra algorithms. Its probability
bounds require fresh uniform probes. Its Frobenius result assumes that the
genuine glued local Frobenius matrix is already supplied and that the two
local splitting partitions differ.

## 1. The V1 defect is repaired

V2 first states the per-probe bound

\[
\Pr[\operatorname{rank}K(a_p)\ne\operatorname{rank}K(a_q)]
\le d(d-1)(1/p+1/q).
\]

It then states, separately and explicitly, that for \(M\) conditionally
fresh probes,

\[
\Pr[\text{some mismatch}]
\le M d(d-1)(1/p+1/q),
\]

and imposes

\[
M d^2=2^{o(n)},
\qquad
\min(p,q)=2^{\Omega(n)}.
\]

These conditions imply

\[
M d(d-1)(1/p+1/q)=2^{-\Omega(n)}.
\]

The V1 counterexample used \(d\asymp\sqrt p\). It no longer satisfies the
new rank condition: already \(d^2\asymp p=2^{\Omega(n)}\). Conversely, if
both \(M\) and the represented rank \(d\) are quasipolynomial in \(n\),
then \(Md^2=2^{(\log n)^{O(1)}}=2^{o(n)}\). Thus the revised inference is
both sufficient and scoped to the intended explicit-algebra regime.

## 2. Uniform nonunits

For a finite-dimensional commutative unital algebra \(A/\mathbb F_r\), an
element is a unit exactly when its image in \(A/\operatorname{Jac}(A)\) is
a unit. Equal quotient-fibre sizes give

\[
\Pr[a\notin A^\times]
=1-\prod_i(1-r^{-e_i})
\le\sum_i r^{-e_i}
\le d/r.
\]

The nilpotent radical therefore adds no probability beyond that of the
fixed semisimple quotient. This is the precise meaning of the statement's
nilpotent sentence; it is not a comparison between arbitrary algebras of
the same dimension.

For a finite free algebra over \(\mathbb Z/N\mathbb Z\), CRT makes a
uniform element into independent uniform local elements. Multiplication by
the element is singular exactly when the element is a nonunit. Hence a
proper determinant gcd occurs exactly when one local element, but not the
other, is a nonunit. This gives the stated exact probability and union
bound. Conditional freshness is sufficient because the same bound holds
after conditioning on each prior transcript.

## 3. Etale monogenicity and Krylov ranks

Write

\[
A\simeq\prod_e(\mathbb F_{r^e})^{m_e},
\qquad \sum_e e m_e=d<r.
\]

There are enough pairwise distinct degree-\(e\) irreducible polynomials to
label the \(m_e\) copies. For \(e=1\), this follows from \(m_1<r\). For
\(e\ge2\), the proof correctly bounds the elements in proper subfields and
gets \(I_r(e)\ge r/e>m_e\). Choosing one root for each component gives an
element whose component minimal polynomials are distinct and whose total
minimal-polynomial degree is \(d\). It generates the algebra.

The discriminant

\[
\Delta(a)=\prod_{i<j}(\sigma_i(a)-\sigma_j(a))^2
\]

is a nonzero polynomial over \(\mathbb F_r\) of total degree
\(d(d-1)\). A generator witnesses nonvanishing. If \(\Delta(a)\ne0\),
multiplication by \(a\) has \(d\) distinct geometric eigenvalues, so the
minimal polynomial has degree \(d\) and the Krylov matrix is full rank.
Schwartz--Zippel gives the displayed bound, with the stated minimum making
it harmless when the degree is at least \(r\).

A local-rank mismatch implies that at least one local Krylov matrix is not
full. The union bounds (8) and (8a) therefore hold even when the two etale
algebras have different factor-degree partitions. The theorem does not
claim control of intermediate elimination entries or other invariants when
the two final ranks agree.

## 4. Genuine Frobenius

On one field factor \(\mathbb F_{r^e}\), a normal basis makes absolute
Frobenius an \(e\)-cycle. Its characteristic polynomial is \(T^e-1\).
Products of field factors give

\[
H_\lambda(T)=\prod_{e\in\lambda}(T^e-1).
\]

Cyclotomic multiplicities recover the number of parts divisible by each
integer, and downward subtraction recovers every part multiplicity. Thus
\(\lambda\mapsto H_\lambda\) is injective over \(\mathbb Z[T]\).

Every coefficient of \(H_\lambda\) has absolute value at most \(2^d\).
If two partitions differ, one coefficient difference is a nonzero integer
of absolute value at most \(2^{d+1}\). The hypothesis
\(p,q>2^{d+1}\) prevents that difference from disappearing in either
local characteristic. Enumerating candidate partitions and taking gcds of
coefficient differences therefore exposes a factor from a supplied genuine
glued map.

There are \(\exp(O(\sqrt d))\) partitions of \(d\). A division-free
characteristic polynomial and all partition tests are quasipolynomial when
\(d=(\log n)^{O(1)}\). Given the factors, local modular powering followed
by coefficientwise CRT constructs the genuine map. No step claims that the
public \(N\)-power map constructs it.

## 5. Monomial powers

The nonzero group of \(\mathbb F_{r^e}\) is cyclic of order \(r^e-1\).
It gives exactly

\[
1+\gcd(E-1,r^e-1)
\]

fixed points, including zero.

Because \(r\) is prime here, additive maps are exactly the linearized
polynomial functions. Reducing a positive exponent to
\(1,\ldots,r^e-1\) preserves the function at zero and on nonzero inputs.
The unique polynomial representative of degree below \(r^e\) is a single
monomial. It is linearized exactly when its exponent is one of
\(1,r,\ldots,r^{e-1}\). This proves the additivity criterion, including
the cases \(e=1\) and \(\mathbb F_2\).

The reductions for \(E=N^k\) are exact:

\[
N^k\equiv q^k\pmod{p-1},
\]

and, when \(e\mid k\),

\[
N^k\equiv q^k\pmod{p^e-1}.
\]

The statement correctly presents these as hidden order conditions. It does
not infer that an adaptive exponent menu cannot hit them.

## 6. Binomial jets

For \(1\le k<p\), one has \(\gcd(k,N)=1\), and

\[
k\binom Nk=N\binom{N-1}{k-1}
\]

implies \(N\mid\binom Nk\). At \(k=p\), the identity

\[
\binom{pq}{p}=q\binom{pq-1}{p-1}
\]

shows divisibility by \(q\), while Lucas's theorem gives

\[
\binom{pq}{p}\equiv q\not\equiv0\pmod p.
\]

Thus the gcd is exactly \(q\). On a balanced semiprime,
\(p=2^{\Omega(n)}\), while every quasipolynomial numerical cutoff is
\(2^{o(n)}\). Such a truncation remains below \(p\) for all sufficiently
large inputs.

The theorem expressly does not cover large binary-encoded indices or a
compressed evaluator for a large interval.

## Residual scope

The eight exclusions in the statement are necessary and accurate. In
particular, F145 does not cover biased sources, same-sample adaptive
polynomials, joint decoding of typical nonzero values, nonmonomial succinct
maps, adaptive order hitting, characteristic-scale algebra rank, or matrix
information other than final Krylov rank.

A fresh statement-only reconstruction is still required by the project
protocol before promotion.
