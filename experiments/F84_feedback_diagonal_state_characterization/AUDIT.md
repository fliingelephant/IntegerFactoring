# PASS

The audited candidate has SHA-256

~~~text
7a53ba1df08ad90c54e034fe23712587563f764fcaf1efb3e4a8445103a4319d
~~~

which matches the pinned digest.

I found no false equivalence, count, cancellation statement, or numerical
claim. The scope is mathematically accurate. There is one important
provenance qualification: substantial parts of the candidate directly
restate P84. That is not a correctness defect because the candidate makes no
novelty claim, but those parts cannot be counted as a new projection-kernel
theorem.

## 1. Exhaustive failure and the graph equivalences

For a unit \(x=(x_p,x_q)\), the gcd \(\gcd(x-1,N)\) is proper exactly when
one, but not both, of \(x_p,x_q\) equals \(1\). Thus condition 1 says exactly
that \(H\) has no nonidentity element in either projection kernel.

The kernel of \(H\to H_p\) consists of the elements \((1,y)\in H\).
Condition 1 makes this kernel trivial, and the same holds at \(q\).
Projection onto the image is automatically surjective, so both projections
are isomorphisms. Their composition gives the asserted isomorphism
\(\varphi:H_p\to H_q\) and the graph description.

Conversely, either the two injective projections or the graph description
forbids a nonidentity projection-kernel element. Conditions 1--3 are
therefore equivalent.

An isomorphism preserves element orders, proving condition 4 from the graph
description. Conversely, if every \(x\in H\) has equal local orders, then an
element in one projection kernel has local order \(1\) there and hence order
\(1\) in the other component. It is the identity. Both projections are
injective, so condition 4 implies conditions 1--3. No cyclicity assumption
on \(H\) is used or needed.

### Negative signs

If \(x_p=-1\), its local order is \(2\). Equal local orders force \(x_q\) to
have order \(2\). Since an odd prime field has the unique order-two element
\(-1\), one gets \(x_q=-1\). The converse is symmetric. Hence a negative
sign can occur in both components or neither, and no negative direct gcd is
proper. This also validates the candidate's use of positive failure alone
to characterize exhaustive two-sign failure.

## 2. Why graph states synchronize every prime-saturation kernel

For the F83 construction, every saturation root has the form

\[
R_\ell(c)=\prod_j q_j^{n_j(c)}\pmod N
\]

with integer exponents and blocks \(q_j\in Q\). It is therefore an element
of \(H=\langle Q\rangle\); the root extraction does not select an arbitrary
\(\ell\)-th root outside \(H\).

If \(H\) is the graph of \(\varphi\), every such root satisfies

\[
R_\ell(c)_q=\varphi(R_\ell(c)_p).
\]

An isomorphism maps identity to identity and only identity to identity.
Thus

\[
R_\ell(c)_p=1\iff R_\ell(c)_q=1
\]

for every \(c\), every relation list for which the F83 map is defined, and
every prime \(\ell\). Hence

\[
K_{p,\ell}=K_{q,\ell}.
\]

This proof does not depend on \(\ell\) being small. A polynomial bound on
\(\ell\) is relevant only to executable menu cost, exactly as the candidate
states.

The conclusion is restricted correctly to identity-target saturation. It
does not say that the two nonidentity character values are equal after
arbitrary hidden identifications, nor does it cover a different decoder
target.

## 3. Fixed-prime decoder failure without a graph

For one \(\ell\), the F83 completeness theorem gives success exactly when
the two identity kernels differ. Thus complete decoder failure is exactly

\[
K_{p,\ell}=K_{q,\ell}.
\]

After identifying a nontrivial local root group with the additive group of
\(\mathbb F_\ell\), a local character is a linear functional. Equal kernels
mean either both functionals are zero or both are nonzero scalar multiples:
two nonzero linear functionals define the same hyperplane exactly when they
are proportional. This includes \(V_\ell=\{0\}\), where both functionals
are zero.

Kernel equality on the separate spaces \(V_\ell\) supplies no injectivity
statement for the ambient projections of \(H\). The candidate does not
reverse this implication.

### Finite-menu counterexample

For \(N=35\) and \(Q=\{2\}\),

\[
\gcd(2-1,35)=1,\qquad \gcd(2+1,35)=1.
\]

With no relation columns, \(V_\ell=\mathbb F_\ell^0=\{0\}\) for every
\(\ell\). The support-two menu is empty and every saturation decoder fails.
Nevertheless,

\[
2^3=8,\qquad \gcd(8-1,35)=7.
\]

Also,

\[
\operatorname{ord}_5(2)=4,\qquad
\operatorname{ord}_7(2)=3,
\]

so the subgroup cannot be a graph. The counterexample is valid.

It is deliberately degenerate on the saturation side because the relation
list is empty. It refutes the claimed logical implication for arbitrary
declared relation lists, but it does not claim that a nonempty or complete
relation source would also miss this example. The candidate's stated scope
does not overreach this evidence.

## 4. Residue-neutral refinement

If \(g,w\in H\), then adjoining their residues does not enlarge \(H\),
regardless of the additional relation \(gw=1\). If every old block is a
product of refined descendants, its residue lies in the subgroup generated
by those descendants. Hence \(H\le K\).

The reverse containment does not follow. From a product \(uv\in H\), one
cannot infer either \(u\in H\) or \(v\in H\). Thus the claimed mechanism is
an integer-presentation effect, not residue growth from the endpoints
themselves. The candidate asserts possibility, not inevitability.

## 5. Quotient indices and the exact separator count

For \(H\le K\), projection induces surjections

\[
K/H\longrightarrow K_p/H_p,
\qquad
K/H\longrightarrow K_q/H_q.
\]

Their source has order \(c\), and their targets have orders \(a,b\).
Therefore \(a\mid c\) and \(b\mid c\).

Since the old graph has

\[
|H|=|H_p|=|H_q|=h,
\]

one has

\[
|K|=ch,\qquad |K_p|=ah,\qquad |K_q|=bh.
\]

The two unquotiented projection kernels consequently have sizes
\(c/a\) and \(c/b\). Apart from their shared identity, they are disjoint.
Removing that identity from each gives exactly

\[
\left(\frac ca-1\right)+\left(\frac cb-1\right)
=\frac ca+\frac cb-2
\]

positive separators.

This count vanishes exactly when \(c/a=c/b=1\), or \(c=a=b\). That is also
equivalent to both quotient projections being injective and to both
unquotiented projections on \(K\) being injective. Hence all four conditions
in Theorem 3 are equivalent, and the exact break condition is

\[
c>a\quad\text{or}\quad c>b.
\]

Lockstep growth with \(c=a=b>1\) really does preserve a graph. Projection
growth alone is not enough.

## 6. The one-overlap cancellation statement

From

\[
B=uv,\qquad g=uz,\qquad B,g\in H,
\]

one gets in the unit group

\[
v=Bu^{-1},\qquad z=gu^{-1}.
\]

Thus, under the explicit assumption that no other refinement supplies an
independent coset,

\[
K=\langle H,u\rangle.
\]

The quotient is cyclic, generated by \(uH\). Its global order is \(c\), and
the two projected coset orders are \(a,b\). Each element has a unique form
\(u^ty\), with \(0\le t<c\) and \(y\in H\).

If \(a\mid t\), then \(u_p^t\in H_p\). Because \(H\to H_p\) is an
isomorphism, exactly one \(y\in H\) has

\[
y_p=u_p^{-t}.
\]

The product \(u^ty\) has \(p\)-component \(1\). If also its \(q\)-component
were \(1\), it would be the global identity, which by uniqueness would force
\(c\mid t\). Hence for \(0<t<c\) it is a positive separator. The same
argument applies at \(q\).

This proves the candidate's “cancel locally before return globally”
interpretation. It is an existence and uniqueness statement. It does not
make \(a,b,c\) or the cancelling element public.

## 7. Phase-only quotient pattern

If \(a=b=1\), then

\[
K_p=H_p,\qquad K_q=H_q.
\]

If also \(c>1\), the global pairing subgroup has enlarged inside the same
rectangle \(H_p\times H_q\). The exact count becomes

\[
c+c-2=2c-2.
\]

This does not contradict synchronized raw orders of \(u\): raw orders govern
the pure powers \(u^E\), whereas \(a,b\) govern when a power lands in an old
local image and can be cancelled by an old element. The candidate keeps
these notions distinct.

## 8. Independent check of the F82 indices

The factorization is correct:

\[
23\cdot89=2047,
\]

and both factors are prime.

Modulo \(23\),

\[
11^2\equiv6,\qquad
11^8\equiv8,\qquad
11^{10}\equiv2,\qquad
11^{11}\equiv-1.
\]

Modulo \(89\),

\[
11^2\equiv32,\qquad
11^4\equiv45,\qquad
11^8\equiv67,\qquad
11^{10}\equiv8,\qquad
11^{11}\equiv-1.
\]

Fermat's theorem then gives

\[
\operatorname{ord}_{23}(11)
=\operatorname{ord}_{89}(11)
=22.
\]

Thus \(H_0=\langle11\rangle\) is a graph of size \(22\).

The stated endpoint values also check:

\[
11^4\equiv312\pmod{2047},
\qquad
11^7\equiv1778\pmod{2047},
\]

and

\[
1778\cdot1735=1507\cdot2047+1.
\]

Hence \(1735\) is the canonical inverse of \(1778\). The integer overlap is

\[
\gcd(1778,312)=2,
\]

so the exposed block is indeed \(u=2\).

Since

\[
2^{11}=2048=1+2047,
\]

the local order of \(2\) is \(11\) modulo both primes. The block is not in
\(H_0\): if it were, the product

\[
2\cdot11=22
\]

would lie in the old graph, but it is \(-1\) modulo \(23\) and is not
\(-1\) modulo \(89\). This contradicts negative-sign synchronization in
\(H_0\).

The coset \(2H_0\) is nonidentity and has order dividing the prime \(11\).
Therefore

\[
c=11.
\]

Modulo \(23\), the old projection has order \(22\), so it is all of
\(\mathbb F_{23}^{\times}\) and already contains \(2\). Thus \(a=1\).

Modulo \(89\), the old projection has order \(22\). The cyclic group
\(\mathbb F_{89}^{\times}\) has a unique subgroup of order \(11\), and that
subgroup lies in every subgroup of order \(22\). Since \(2\) has order
\(11\), it lies in \(H_{0,q}\), giving \(b=1\).

Therefore

\[
c=11,\qquad a=b=1,
\]

and the exact positive-separator count is

\[
11+11-2=20.
\]

The displayed word \(22\) is a negative separator because

\[
\gcd(22+1,2047)=\gcd(23,2047)=23.
\]

All numerical and index claims in Section 8 are correct.

## 9. Relation to P84

The candidate is not a wholly new projection-kernel theorem.

* The opening implication “no positive separator implies injective local
  projections and a graph” is already the starting observation of P84.
* Theorem 3, including \(a\mid c\), \(b\mid c\), the count
  \(c/a+c/b-2\), and the break criterion \(c>a\) or \(c>b\), is a direct
  restatement of P84.
* Corollary 4's cyclic extension, exponent classes, and unique old
  cancellation elements also directly restate P84's one-block split.

The equal-order and negative-sign formulations are immediate graph
corollaries. The synchronization of every prime-saturation identity kernel
combines the graph property with the later F83/P89 root decoder. The
\(c=11,a=b=1\) calculation is a specialization to the F82/P88 phase witness.

This provenance does not make the candidate false. It does mean that the
quotient count and one-overlap theorem cannot be presented as novelty beyond
P84. The candidate avoids that error by explicitly making no literature
novelty claim.

## 10. Scope audit

The scope distinctions are exact:

* Exhaustive subgroup failure is stronger than failure of a finite direct
  menu.
* Graph structure forces all identity-target saturation roots to
  synchronize, but decoder failure on selected root spaces does not imply a
  graph.
* Residue-neutral endpoints do not enlarge \(H\); integer refinement can
  expose factors outside it.
* A graph break proves that a separator exists in \(K\), not that a public
  finite menu, a small-prime relation space, or an efficient selector reaches
  it.
* The quotient indices and cancellation elements are hidden
  characterizations, not public computations.
* The F82 word is a fixed canonical-integer realization, not an all-input
  source law.

The candidate claims no probability law, computational lower bound,
literature novelty, general useful-split guarantee, or factoring algorithm.
No correction is required.
