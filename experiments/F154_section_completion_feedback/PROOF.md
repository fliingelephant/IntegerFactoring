# Proof of the F154 section-completion theorem

## 1. A public lift of the quotient section

The decorated group \(E_Q(N)\) is an \(\mathbf F_2\)-vector space. Choose a
basis \(b_1,\ldots,b_d\) of \(W\) from the retained parity vectors. For each
basis vector, keep one actual decorated lift \(e_i\) from the transcript.
Define

\[
\widetilde h\left(\sum_i\lambda_i b_i\right)
=
\mathop{\star}_i e_i^{\lambda_i}.
\tag{15}
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
\tag{16}
\]

The identity maps to \((0,1)\), so \(z_0=1\).

## 2. Exact completion records

Let \(s_v\) be the least positive inverse of \(z_v\). Then

\[
s_vz_v\equiv1\pmod N.
\]

Squaring and using (16) gives

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
deduplication first compares their decorated lifts. The no-factor
hypothesis makes their quotient global. Removing the duplicate is therefore
algebraically inert, while occurrence and presentation metadata can remain.

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
\tag{17}
\]

Modulo \(N\), the positive root in (12) is

\[
z_v^{-1}z_w^{-1}z_{v+w}^{-1}z_{v+w}^2C(v,w)
=
\frac{z_{v+w}C(v,w)}{z_vz_w}
=1
\]

by (17).

## 5. Complexity

Binary enumeration of \(W\) produces \(2^d\) vectors. Starting from the
basis lifts, one can compute every \(z_v\) by modular star-products. Each
inverse \(s_v\) costs polynomial time in \(n\).

The integer \(Q(v)\) uses at most \(\Lambda_Q\) bits, and \(s_v<N\). Hence
\(P_v=s_v^2Q(v)\) has at most \(2n+\Lambda_Q+O(1)\) bits. Generation, exact
factor-presentation storage, gcd-free refinement, binary elimination, and
normalized-root decoding are polynomial in the total explicit output
length. This proves (14) and the stated quasipolynomial specialization.

## 6. Scope of the feedback statement

The factors \(s_v\) are publicly known integers, but they need not occur in
the old named generator basis. Joint gcd-free refinement can therefore split
old composite blocks or add blocks from the new inverse representatives.
This is an integer-presentation change. Equations (9)--(11) prove that it is
not a new modular lift.

Whether such blocks become legal future source generators is an algorithm
definition, not a consequence of the group theorem. Even when they do, this
proof gives no lower bound on refinement, no descent or termination
potential, and no reason for the next canonical relation to disagree with
the section. The claimed gain is therefore exactly the conditional
grammar-level opportunity stated in Section 5, and no more.
