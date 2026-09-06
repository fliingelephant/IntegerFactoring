# F142 blind reconstruction

## Provenance and verdict

- Sole mathematical input: `STATEMENT.md`.
- Verified statement SHA-256:
  `0049f74a635b7da7f288460ddbaf8e6669eb329073e8164b0834e74d3e4c1a1e`.
- No proof, audit, manifest, F141 proof/audit, durable ledger, computer
  algebra, or numerical experiment was read or used.
- Final report SHA-256: supplied externally in the task handoff after this
  file is closed. A file cannot contain its own ordinary SHA-256 digest
  without changing that digest.

**Verdict.** The internal linear-algebra and exact-root claims reconstruct.
They are correct under the relation-ledger convention implicit in the
statement: every retained old exact relation is a positive integer congruent
to \(1\pmod N\), and every quantity inverted modulo \(N\) is a unit. The
phrase \(D_\ell=A_\ell+B_\ell\) is a parity-column identity, not an integer
identity. The exact identity behind it is

\[
A_\ell B_\ell=D_\ell w_\ell^2.
\]

The claims about what F141 proves, and the assertion that no theorem in the
frozen source forces a cycle, are source-comparison claims. They cannot be
independently audited under the required blind boundary. The abstract forest
constructed here does prove the narrower internal claim: row reuse alone does
not force nullity.

## 1. Ambient square-class space and the three columns

Work in

\[
V=\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2,
\]

written additively over \(\mathbb F_2\). Thus \([xy]=[x]+[y]\) and
\([z^2]=0\).

From

\[
A_\ell=c_\ell w_\ell,
\qquad
B_\ell=q\ell^2w_\ell,
\]

one gets directly

\[
[A_\ell]=\gamma_\ell+h_\ell,
\qquad
[B_\ell]=a+h_\ell.
\]

If \(H\) has columns \(h_\ell\), the lifted matrix therefore is

\[
B=H+a\mathbf1^{\mathsf T}.
\]

The added matrix has rank at most one. Applying
\(\operatorname{rank}(X+Y)\leq\operatorname{rank}X+
\operatorname{rank}Y\) in both directions gives

\[
\left|\operatorname{rank}B-
\operatorname{rank}H\right|\leq1.
\]

By the defining inverse relation, \(c_\ell w_\ell\equiv1\pmod N\), while
\(c_\ell\equiv q\ell^2\pmod N\). Hence

\[
q\ell^2w_\ell\equiv1\pmod N,
\qquad
\ell^2w_\ell\equiv q^{-1}\pmod N.
\]

This proves the supplied congruence, but it is only a congruence. It imposes
no linear dependency among the square-class columns.

## 2. Bridge replacement

Define the exact bridge representative

\[
D_\ell=q\ell^2c_\ell.
\]

Its square class and supplied root are

\[
[D_\ell]=a+\gamma_\ell,
\qquad
D_\ell\equiv c_\ell^2\pmod N.
\]

At the parity-column level,

\[
[A_\ell]+[B_\ell]
=(\gamma_\ell+h_\ell)+(a+h_\ell)
=a+\gamma_\ell=[D_\ell].
\]

At the exact-integer level,

\[
A_\ell B_\ell
=(c_\ell w_\ell)(q\ell^2w_\ell)
=D_\ell w_\ell^2.
\]

Thus replacing a lifted column by its sum with its retained matched
canonical column is an invertible binary column operation. The discarded
exact factor is a known square, so exact roots can also be transported.
This proves that the fresh \(h_\ell\)-row disappears from incremental rank
once the matched canonical column is in the old ledger.

The condition \(\gcd(q,w_\ell)=1\) contains no condition on
\(\gcd(q,c_\ell)\). Consequently, a prime row in \(a=[q]\) can also occur in
\(\gamma_\ell=[c_\ell]\) and cancel in \([D_\ell]\). Counting that row in
the uncontracted lifted columns is therefore not a valid relative-rank
argument.

## 3. Exact relative-rank gate

Let \(C=\operatorname{colspan}(M_0)\), and let \(x\neq0\) select bridge
columns. Their sum is

\[
\sum_\ell x_\ell[D_\ell]
=\Gamma x+(\mathbf1^{\mathsf T}x)a.
\]

It extends to an old/new dependency exactly when this sum belongs to the old
span. Therefore the exact gate is

\[
\Gamma x+t(x)a\in C,
\qquad t(x)=\mathbf1^{\mathsf T}x.
\]

Passing to \(V/C\) gives

\[
\overline\Gamma x=t(x)\overline a.
\]

If \(a\in C\), then \(\overline a=0\), so the gate reduces to
\(\overline\Gamma x=0\). In general the quotient bridge matrix is
\(\overline\Gamma+\overline a\mathbf1^{\mathsf T}\), a rank-at-most-one
perturbation of \(\overline\Gamma\). Its rank can change by at most one.
Arbitrarily many occurrences of the same \(q\)-row therefore do not, by
themselves, imply a growing kernel.

### Owner contraction

Choose an old spanning family consisting of owners
\(v_1,\ldots,v_s\) and the remaining columns \(W\). At private pivot
\(p_i\), assume that \(v_i\) is the unique old owner and that every bridge
under consideration has entry one. For a selected bridge vector \(x\), its
entry at every such pivot is \(t(x)\). The pivot equations force the
coefficient of every \(v_i\) to be \(t(x)\).

After deleting the pivot rows, solvability is therefore equivalent to

\[
\widehat D x+t(x)\sum_{i=1}^s\widehat v_i
\in\operatorname{colspan}(\widehat W),
\]

or, column by column,

\[
\sum_\ell x_\ell
\left(\widehat D_\ell+
\sum_{i=1}^s\widehat v_i\right)
\in\operatorname{colspan}(\widehat W).
\]

This is exactly the asserted owner contraction. If a bridge lacks one of
the pivots because \(a\) and \(\gamma_\ell\) cancel there, the forced owner
coefficient is no longer uniformly \(t(x)\). One must use the actual
incidence vector, equivalently the general gate above.

## 4. Standalone exact root

For a dependency

\[
M_0y+t(x)a+Hx=0,
\]

let \(S=\{\ell:x_\ell=1\}\). The square class of

\[
Q=P_0(y)q^{|S|}\prod_{\ell\in S}w_\ell
\]

is exactly the left side of that equation. It is zero, so the positive
integer \(Q\) is an exact square. The selected exact lifted product is

\[
P_0(y)\prod_{\ell\in S}B_\ell
=\left(\prod_{\ell\in S}\ell\right)^2Q.
\]

Its positive root is consequently

\[
R=\left(\prod_{\ell\in S}\ell\right)\sqrt Q.
\]

Each old relation and each \(B_\ell\) is congruent to one modulo \(N\), so
\(R^2\equiv1\pmod N\). This proves that \(R\) is a modular square root of
one. Nothing in the congruence decides whether \(R\equiv\pm1\pmod N\).

## 5. Bridge exact root and compatibility with replacement

If \(P_0(y)\prod_{\ell\in S}D_\ell\) is an exact square, then

\[
\rho(y,x)=
\sqrt{P_0(y)\prod_{\ell\in S}D_\ell}
\left(\prod_{\ell\in S}c_\ell\right)^{-1}
\pmod N
\]

is defined because every \(c_\ell\) is a unit. Squaring and using
\(P_0(y)\equiv1\) and \(D_\ell\equiv c_\ell^2\pmod N\) gives
\(\rho(y,x)^2\equiv1\pmod N\).

It remains to check that the parity-column replacement preserves this
normalized root, including overlap with selected canonical columns. First
suppose each lifted column has its own indexed matched canonical column. Let
\(e_\ell\) be the original selection bit of \(A_\ell\). When
\(x_\ell=1\), the bridge basis toggles that bit.

- If \(e_\ell=0\), the bridge product contains \(A_\ell D_\ell\) where the
  original product contains \(B_\ell\). Their ratio is \(c_\ell^2\), which
  is removed by the normalizing factor \(c_\ell^{-1}\).
- If \(e_\ell=1\), the bridge product contains \(D_\ell\) where the
  original product contains \(A_\ell B_\ell\). Their ratio is
  \(w_\ell^{-2}\). After normalization, the remaining ratio of roots is
  \((c_\ell w_\ell)^{-1}=A_\ell^{-1}\equiv1\pmod N\).

Thus the bridge root and the original canonical-plus-lifted root are the
same modulo \(N\), up to the unavoidable sign choice for a square root. If
several lifted columns share one deduplicated canonical column, its bit is
toggled by the parity of that group. Temporarily treating the repeated
toggles as ordinary multiplication inserts only even powers of the exact
canonical relation. Their roots are powers of \(A_\ell\equiv1\pmod N\), so
the same modular-root conclusion follows.

## 6. Forest and subdivided-star obstruction

When each endpoint is one atomic row, a bridge column
\(e_{q_i}+e_{c_i}\) is the binary incidence column of an edge. A kernel
vector selects an edge set of even degree at every vertex. This is exactly
the binary cycle space. A forest has no nonempty even-degree edge set, so
its incidence columns are independent.

In particular, a fixed-\(q\) star with a private residue row at each leaf is
a forest and has full column rank, no matter how many times its central row
occurs.

Before bridge contraction, take independent atomic rows
\(a,\gamma_i,h_i\). The columns

\[
A_i=\gamma_i+h_i,
\qquad
B_i=a+h_i
\]

are the edges \(\gamma_i-h_i-a\) of a subdivided star. Directly, each
private \(\gamma_i\)-row first forces the coefficient of \(A_i\) to zero,
and then the \(h_i\)-row forces the coefficient of \(B_i\) to zero. Hence
all \(2m\) columns are independent. This gives an exact abstract
countermodel to any inference from common-row multiplicity alone.

For non-atomic endpoint vectors, each bridge column is a binary hyperedge.
The kernel condition remains even incidence in every surviving quotient
row. This is precisely the general gate in Section 3, not an ordinary graph
cycle criterion.

## 7. Exact endpoint cycle

Assume

\[
c_i=[q_i\ell_i^2]_N=q_{i+1},
\qquad q_{k+1}=q_1.
\]

Then

\[
\prod_{i=1}^kD_i
=\prod_i q_i\ell_i^2q_{i+1}
=\left(\prod_iq_i\ell_i\right)^2.
\]

The positive exact root is \(\prod_iq_i\ell_i\). The supplied modular root
is \(\prod_i c_i=\prod_iq_i\). Dividing gives

\[
\rho=\prod_i\ell_i\pmod N.
\]

Also, multiplying \(q_{i+1}=c_i\equiv q_i\ell_i^2\pmod N\) around the
cycle and cancelling the unit \(\prod_iq_i\) gives

\[
\left(\prod_i\ell_i\right)^2\equiv1\pmod N.
\]

A non-global root \(r\not\equiv+1,-1\pmod N\) always gives a proper
nontrivial divisor through \(\gcd(r-1,N)\). Conversely, for the standard
odd factoring modulus, the global roots give only the trivial gcds, so the
stated gate is exact. If even \(N\) is allowed, the word "exactly" needs the
usual preprocessing qualification: the global root \(-1\) can expose the
already-trivial factor \(2\) through \(\gcd(r-1,N)\). The cycle and root
formulas themselves do not need oddness.

## 8. Squareclass-match cycle

Now assume only matching endpoint square classes, represented exactly by

\[
c_i=d_ir_i^2,
\qquad q_{i+1}=d_is_i^2.
\]

The bridge classes still cancel cyclically because
\([c_i]=[q_{i+1}]\). Moreover,

\[
\begin{aligned}
\prod_iD_i
&=\left(\prod_i\ell_i\right)^2
  \left(\prod_iq_i c_i\right)\\
&=\left(\prod_i\ell_i d_i r_i s_i\right)^2,
\end{aligned}
\]

where cyclic indexing gives \(\prod_iq_i=\prod_iq_{i+1}\). Dividing its
positive root by
\(\prod_i c_i=\prod_i d_i r_i^2\) yields

\[
\rho=
\prod_i\ell_i s_i r_i^{-1}\pmod N.
\]

The inverses exist because \(c_i\) and \(q_{i+1}\) are units, so their
factors \(d_i,r_i,s_i\) are units modulo \(N\). Multiplying

\[
q_{i+1}=c_i(s_i/r_i)^2
\equiv q_i\ell_i^2(s_i/r_i)^2\pmod N
\]

around the cycle also verifies \(\rho^2\equiv1\pmod N\).

## 9. Deduplication and canonical-ledger scope

The relative-rank conclusion has a precise scope.

1. The old span must contain a matched canonical column for every lifted
   column to which the bridge replacement is applied. One retained
   canonical column can serve several lifted columns with the same canonical
   residue; the basis map toggles that old column by the parity of their
   selected coefficients.
2. All rank and kernel statements concern the actual retained, indexed
   column family. If a pipeline deduplicates equal residues, equal exact
   relations, or equal parity columns, the gate must be applied after that
   choice, or the removed multiplicities must remain explicit. These three
   notions of equality are not interchangeable for exact-root bookkeeping.
3. Canonicalization gives the exact representative
   \(c_\ell=[q\ell^2]_N\). Within a fixed \(q\)-block, if two anchors give
   the same \(c_\ell\), they also give the same \(w_\ell\) and canonical
   relation \(A_\ell\), while their lifted exact integers differ by the
   visible square multipliers \(\ell^2\). Their parity columns can therefore
   coincide even though their supplied exact roots use different anchors.
4. If the matched canonical column is absent from the retained old ledger,
   the standalone identity \(B=H+a\mathbf1^{\mathsf T}\) remains valid, but
   the relative bridge gate is not justified for that column.

Accordingly, after matched canonical retention, the incremental parity
content is exactly the bridge family \([q]+[c_\ell]\). A successful
dependency still needs two independent facts: an even-incidence selection
in the quotient by the old span, and a normalized root from that selection
which is not globally \(\pm1\). The forest construction proves that the
first fact does not follow from repeated \(q\)-rows alone. The congruence
formulas prove that the second fact does not follow from parity alone.

## Claim ledger

| Statement component | Blind result |
|---|---|
| Three column identities and rank bound | Reconstructed |
| Inverse-cofactor congruence | Reconstructed |
| Bridge parity equivalence and supplied root | Reconstructed |
| Relative-rank quotient gate | Reconstructed |
| Multi-owner contraction | Reconstructed under its stated private-pivot incidence hypothesis |
| Standalone exact root | Reconstructed under the relation-ledger congruence invariant |
| Bridge normalized root and basis compatibility | Reconstructed |
| Forest and subdivided-star obstruction | Reconstructed |
| Exact endpoint-cycle root | Reconstructed |
| Squareclass-match-cycle root | Reconstructed |
| Composite-endpoint hypergraph formulation | Reconstructed |
| F141 source-comparison assertions | Not auditable within the mandated blind boundary |
