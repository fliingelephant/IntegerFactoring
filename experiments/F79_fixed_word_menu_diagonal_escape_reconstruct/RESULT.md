# PASS

The SHA-256 of `STATEMENT.md` is
`ccb4db80e17d96ecf1f19681170f0981eb559461ef5dc1a86bbc3fc7b2738212`,
as required.

## 1. Reduction of a menu pair to one forbidden value

Fix \(L\) and fix \(S\subseteq\mathbb F_L^2\) before choosing \(z\). For one
pair \((A,B)\in S\),

\[
Az+Bg=(Ar+B,As+B).
\]

If \(A=0\), both coordinates equal \(B\). Such a pair never gives exactly one
zero coordinate. If \(A\ne0\), put

\[
t(A,B)=-B/A.
\]

Then

\[
Az+Bg=A(r-t(A,B),s-t(A,B)).
\]

For distinct \(r,s\), this word has exactly one zero coordinate if and only if
exactly one of \(r,s\) equals \(t(A,B)\). Since \(r\ne s\), this is equivalent
to saying that at least one of \(r,s\) equals \(t(A,B)\).

Define the set of dangerous values

\[
D=\{-B/A:(A,B)\in S,\ A\ne0\}.
\]

It has size at most \(|S|\le L-3\). The set

\[
\mathbb F_L^\times\setminus D
\]

therefore has at least

\[
(L-1)-(L-3)=2
\]

elements. This remains true if \(0\in D\), because removing zero does not
remove a member of \(\mathbb F_L^\times\). Choose distinct

\[
r,s\in\mathbb F_L^\times\setminus D.
\]

Every pair in \(S\) with \(A=0\) is harmless, and every pair with \(A\ne0\)
has its dangerous value in \(D\). Thus no declared word has exactly one zero
coordinate. This proves condition 5.

## 2. The four structural conditions

With \(g=(1,1)\),

\[
H=\langle g\rangle=\{(u,u):u\in\mathbb F_L\}.
\]

An element of \(H\) has either two zero coordinates or no zero coordinate.
This proves condition 1. The choice \(r,s\ne0\) proves condition 2.

The two column vectors \(g\) and \(z\) have determinant

\[
\det\begin{pmatrix}1&r\\1&s\end{pmatrix}=s-r\ne0.
\]

They form a basis of \(\mathbb F_L^2\), so

\[
\langle H,z\rangle=\mathbb F_L^2.
\]

This proves condition 3. The full space contains, for example, \((1,0)\) and
\((0,1)\), which proves condition 4. All five requested conditions therefore
hold simultaneously.

## 3. Exactness of the \(L-3\) universal bound

The bound is sharp as a guarantee for every menu of a stated cardinality.
Choose any \(u\in\mathbb F_L^\times\), and set

\[
S_0=\{(1,-t):t\in\mathbb F_L^\times\setminus\{u\}\}.
\]

Then \(|S_0|=L-2\). For any distinct nonzero \(r,s\), they cannot both equal
\(u\). At least one, say \(r\), lies in the displayed dangerous-value set.
The menu pair \((1,-r)\) then gives

\[
z-rg=(0,s-r),
\]

which has exactly one zero coordinate. Hence no admissible \(r,s\) avoids
this particular menu of size \(L-2\).

This sharpness concerns a cardinality-only guarantee. A particular larger
menu can still be avoidable when many residue pairs give the same value
\(-B/A\), or when they have \(A=0\).

## 4. Finite-menu consequences

Let a predeclared integer menu contain \(T(n)\) exponent pairs. Reduce all
pairs modulo \(L\) and discard duplicates. Its residue menu has at most
\(T(n)\) elements. If the odd prime \(L\) satisfies

\[
L>T(n)+2,
\]

then integrality gives \(T(n)\le L-3\). The theorem applies, so the complete
predeclared menu is avoidable in this model.

For a nonnegative integer \(E(n)\), the full integer coefficient box

\[
|A|,|B|\le E(n)
\]

contains exactly

\[
K=(2E(n)+1)^2
\]

integer pairs. Reduction modulo \(L\) can only identify pairs, so there are at
most \(K\) distinct residue pairs. The strict integer inequality

\[
L>(2E(n)+1)^2+2=K+2
\]

is exactly what implies \(K\le L-3\). Hence one choice of \(z\) avoids every
word in the full box.

For a fixed union of explicit schedules, first reduce every scheduled pair
modulo \(L\), take the union, and remove duplicates. If its total number \(K\)
of distinct residue pairs satisfies \(K\le L-3\), it is one allowed menu and
the same proof applies. Bounds for the schedules separately cannot be used
separately: the theorem needs the bound on their union. If \(K>L-3\), this
cardinality theorem supplies no universal guarantee, although an individual
union can still be avoidable when its dangerous values collapse. Thus the
stated condition describes the scope of the finite-menu guarantee, not a
necessary condition for every individual menu.

## 5. Quantifier order

The proved order is

\[
\forall L\quad\forall S\text{ fixed with }|S|\le L-3
\quad\exists(r,s).
\]

The choice of \((r,s)\), and hence \(z\), can depend on \(S\). The result does
not produce one \(z\) that avoids all later menus. This distinction is
essential. After seeing \(z=(r,s)\), a selector can choose the single pair

\[
(A,B)=(1,-r),
\]

and obtain \((0,s-r)\). Thus even a one-word menu selected after \(z\) defeats
the avoidance property. The theorem consequently does not cover adaptive or
value-dependent selection.

## 6. Negative-sign scope in an odd-order realization

In an integer local unit group that can realize a coordinate copy of \(C_L\)
with odd \(L>2\), the local element \(-1\) is a nonidentity element of order
two. An odd-order subgroup cannot contain it, by Lagrange's theorem. A
2-primary local unit group cannot supply the required odd prime-order
coordinate copy, so it does not create an exception to this realization.

Therefore each modeled coordinate subgroup contains the multiplicative
identity, which corresponds to additive zero, but it does not contain local
\(-1\). Within this odd-order model, the positive test can target a zero
coordinate, while the negative test has no local \(-1\) target. The negative
sign adds no target inside the modeled group. This is a scope statement about
the realization; it is not a claim about a larger ambient group that also has
even-order elements.

## 7. Remaining scope

The argument covers only a fixed finite set of linear words \(Az+Bg\) over
\(\mathbb F_L\). It does not model any of the following operations:

- a menu chosen after inspection of \(z\);
- an adaptive or value-dependent word selector;
- quotient-fibre processing or integer-refinement operations;
- square-class decoding; or
- a canonical-inverse integer realization.

Those operations can use information or structure that is absent from the
two-dimensional fixed-word model. No conclusion about them follows from this
proof.

Finally, the construction is existential and abstract. It gives neither an
encoded hard-input family nor a reduction or resource lower bound against
algorithms. It also constructs no integer to factor and supplies no method
that finds a factor. It proves neither a computational lower bound nor a
factoring algorithm.
