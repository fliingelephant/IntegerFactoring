# Proof of the F154 V2 section-completion theorem

## 1. A public lift of the quotient section

The decorated group \(E_Q(N)\) is an \(\mathbf F_2\)-vector space. Choose a
basis \(b_1,\ldots,b_d\) of \(W\) from the retained parity vectors. For each
basis vector, keep one actual decorated lift \(e_i\) from the transcript.
Define

\[
\widetilde h\left(\sum_i\lambda_i b_i\right)
=
\mathop{\star}_i e_i^{\lambda_i}.
\tag{19}
\]

This is a public homomorphism. Its first coordinate is the input vector, and
its quotient agrees with \(h\) on the basis. Uniqueness of the quotient
section therefore makes it a lift of \(h\) on all of \(W\). Write

\[
\widetilde h(v)=(v,z_v).
\]

Every \(z_v\) is a unit and satisfies

\[
z_v^2\equiv Q(v)\pmod N.
\tag{20}
\]

The identity maps to \((0,1)\), so \(z_0=1\).

## 2. Exact completion records

Let \(s_v\) be the least positive inverse of \(z_v\). Then

\[
s_vz_v\equiv1\pmod N.
\]

Squaring and using (20) gives

\[
s_v^2Q(v)\equiv s_v^2z_v^2\equiv1\pmod N.
\]

Thus \(P_v\) is an exact positive relation with supplied modular root \(1\).
Its decorated lift is

\[
\left(v,1\cdot s_v^{-1}\right)
=(v,z_v)
=\widetilde h(v).
\]

Suppose \(P_v=P_w\). Their rational square classes are respectively
\([Q(v)]\) and \([Q(w)]\). Pairwise coprimality and nonsquareness of the
\(q_j\) make the map \(v\mapsto[Q(v)]\) injective. Hence \(v=w\). This proves
pairwise distinctness.

For \(v=0\), \(z_0=s_0=1\) and \(P_0=1\). For \(v\ne0\), \(Q(v)\) is not a
rational square, while \(s_v^2\) is a square. Therefore \(P_v\ne1\), and
positivity gives \(P_v>1\).

## 3. All completion dependencies have root \(+1\)

For a selector \(S\subseteq W\), the rational square class of the selected
product is

\[
\left[\prod_{v\in S}P_v\right]
=
\left[Q\left(\sum_{v\in S}v\right)\right].
\]

Squareclass independence proves (10).

If the sum is zero, the star-product of the decorated lifts is

\[
\mathop{\star}_{v\in S}\widetilde h(v)
=
\widetilde h(0)
=(0,1).
\]

The second coordinate is exactly the normalized root of the selected
integer square. It is therefore \(+1\), proving (11).

For a mixed old/completion dependency, replace each old decorated lift by
the corresponding value of \(\widetilde h\). Because both represent the same
quotient section, each replacement changes the product only by an element
of the global-sign subgroup. The completion product itself lies on
\(\widetilde h\). A zero-parity mixed product therefore has only a global
root. Hence the useful normalized-root image does not increase.

If an exact completion value equals an old exact value, supplied-root-aware
deduplication first compares their decorated lifts. A non-global quotient
already gives a factor. On the no-factor branch, their quotient is global,
so removing one algebraic copy preserves the current useful normalized-root
image. This does not authorize loss of occurrence, presentation, or
provenance metadata when a later grammar is allowed to observe that data.

## 4. Triple identity

Exact multiplication gives

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2.
\]

Therefore

\[
\begin{aligned}
P_vP_wP_{v+w}
&=s_v^2s_w^2s_{v+w}^2Q(v)Q(w)Q(v+w)\\
&=\left(
s_vs_ws_{v+w}Q(v+w)C(v,w)
\right)^2.
\end{aligned}
\]

The homomorphism law in \(E_Q(N)\) says

\[
z_vz_wC(v,w)^{-1}=z_{v+w}.
\tag{21}
\]

Modulo \(N\), the positive root in (12) is

\[
z_v^{-1}z_w^{-1}z_{v+w}^{-1}z_{v+w}^2C(v,w)
=
\frac{z_{v+w}C(v,w)}{z_vz_w}
=1
\]

by (21).

## 5. Complexity

Binary enumeration of \(W\) produces \(2^d\) vectors. Starting from the
basis lifts, one can compute every \(z_v\) by modular star-products. Each
inverse \(s_v\) costs polynomial time in \(n\).

The integer \(Q(v)\) uses at most \(\Lambda_Q\) bits, and \(s_v<N\). Hence
\(P_v=s_v^2Q(v)\) has at most \(2n+\Lambda_Q+O(1)\) bits. Generation, exact
factor-presentation storage, gcd-free refinement, binary elimination, and
normalized-root decoding are polynomial in the total explicit output
length. This proves (14) and the stated quasipolynomial specialization.

The compact decoder computes a basis of the parity kernel and the image of
the normalized-root map on that basis. It need not enumerate all kernel
elements. The explicit transcript-size hypothesis includes the binary
encodings of the \(q_j\), and therefore includes \(\Lambda_Q\).

## 6. Exact interface scope

The factors \(s_v\) are publicly known integers. They need not be distinct,
and they need not be absent from the old named generator basis. Joint
gcd-free refinement can nevertheless split old composite blocks or add
blocks from the newly computed inverse representatives. This is an
integer-presentation change. Equations (9)--(11) prove that it is not a new
modular lift.

For the feedback statement, impose this interface:

> A future grammar can observe completion data only through blocks newly
> named by joint gcd-free refinement of the old endpoints and the \(s_v\).

Under this restriction, if refinement names no new block, or if the grammar
excludes all such blocks as generators, this refinement-mediated feedback
channel is inert. No theorem here restricts an arbitrary grammar that can
read the raw \(s_v\), the \(P_v\), their count, or their provenance.

## 7. The \(N=77\) refinement and subgroup certificate

Take \(N=77\), \(q_1=4706\), and one old retained record

\[
T_1=q_1=1^2q_1
\]

with supplied modular root \(\alpha_1=3\). The required checks are

\[
4706=61\cdot77+9,
\qquad
3^2\equiv9\equiv4706\pmod{77}.
\]

Also \(\gcd(4706,77)=1\). The integer \(4706\) is not a square because its
2-adic valuation is one. The one nonzero parity column has zero parity
kernel, so this transcript is on the no-factor section branch. Its actual
decorated lift is \(((1),3)\). Hence

\[
z_{(1)}=3,
\qquad
s_{(1)}=26,
\qquad
3\cdot26=1+77.
\]

The completion record is \(P_{(1)}=26^2\cdot4706\), and it has supplied root
\(1\) as required. Joint refinement sees

\[
\gcd(26,4706)=26,
\qquad
4706=26\cdot181,
\qquad
\gcd(26,181)=1.
\]

It therefore replaces one named block by two proper coprime named blocks.

The subgroup growth is also exact. The old block has residue \(9\) modulo
\(77\). Its orders modulo \(7\) and \(11\) are \(3\) and \(5\), so its order
modulo \(77\) is \(15\). The new block \(26\) has residues \(5\) and \(4\).
Their orders are \(6\) and \(5\), so the order of \(26\) modulo \(77\) is
\(30\). Therefore

\[
\langle9\rangle
\subsetneq
\langle9,26\rangle.
\]

This is strict growth of the named-block-generated subgroup. It is not
growth of the group of all publicly computable residues: \(26\) is already
the public inverse of \(3\). It also does not factor \(77\).

## 8. No success law

Whether newly named blocks become legal future generators is an algorithm
definition, not a consequence of the group theorem. Even when they do, this
proof gives no lower bound on refinement, no descent or termination
potential, and no reason for the next canonical relation to disagree with
the section.

Once \(\widetilde h\) is enumerated, the algorithm can refine the integers
\(s_v\) directly. The exact records \(P_v\) are a decoder-inert relation
ledger for that public inverse list. They are not the cause of the
refinement opportunity.

The claimed gain is therefore one conditional, refinement-mediated
grammar-level opportunity. F154 proves no forced refinement, later
disagreement, iteration bound, or factoring algorithm.
