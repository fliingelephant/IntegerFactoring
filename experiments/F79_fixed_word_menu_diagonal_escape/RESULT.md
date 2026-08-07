# F79 — every fixed sublinear word menu can miss a maximal one-generator correlation break

**Status:** proof-only candidate. No research computation was run. This is an
abstract group-level obstruction to predeclared exponent menus. It is not an
integer feedback family, an adaptive-selector lower bound, or a factoring
algorithm.

## 1. Closest prior result and material difference

P81 shows that one fixed post-refinement state is solved by a small
support-two exponent menu. P83 shows that separator existence does not imply
large uniform density. F78 gives the exact projection-kernel transition and
shows that uniform old-subgroup blinding remains sparse.

The present candidate asks whether a **predeclared finite exponent list** can
replace uniform sampling after a one-generator correlation break. It gives an
exact negative answer in the diagonal cyclic model, even when the old
subgroup has a public generator and the enlarged subgroup is the full local
product.

## 2. The menu-avoidance theorem

Let \(L>2\) be prime. Write \(C_L\) additively and identify it with
\(\mathbb F_L\). Let

\[
S\subseteq\mathbb F_L^2
\]

be any exponent menu with

\[
|S|\le L-3.
\tag{1}
\]

The menu may depend on \(L\), but it must be fixed before the new generator
is chosen. A pair \((A,B)\in S\) denotes the support-two word

\[
A z+B g.
\]

### Theorem 1

There are distinct nonzero \(r,s\in\mathbb F_L\) such that, for

\[
g=(1,1),
\qquad
H=\langle g\rangle
 =\{(t,t):t\in\mathbb F_L\},
\qquad
z=(r,s),
\]

all of the following hold.

1. \(H\) has no positive separator.
2. \(z\) is not a positive separator.
3. The extension is maximal:

   \[
   \langle H,z\rangle=\mathbb F_L^2.
   \]

4. The enlarged group contains positive separators.
5. No word in the prescribed menu is a positive separator:

   \[
   A z+B g
   \quad\text{is not a positive separator for every }(A,B)\in S.
   \tag{2}
   \]

### Proof

For each menu pair with \(A\ne0\), define its forbidden value

\[
f(A,B)=-B/A\in\mathbb F_L.
\]

Let

\[
F=\{f(A,B):(A,B)\in S,\ A\ne0\}.
\]

Then \(|F|\le |S|\le L-3\). Hence
\(\mathbb F_L\setminus F\) contains at least three elements. At most one of
them is zero, so it contains two distinct nonzero elements. Choose these as
\(r,s\).

The diagonal \(H\) has no element with exactly one zero coordinate. Since
\(r,s\ne0\), the new generator \(z\) is also not a separator.

The two generators form the matrix

\[
\begin{pmatrix}
1&r\\
1&s
\end{pmatrix},
\]

whose determinant is \(s-r\ne0\). They therefore generate all of
\(\mathbb F_L^2\), which contains \((0,1)\) and hence contains positive
separators.

Finally,

\[
A z+B g=(Ar+B,As+B).
\tag{3}
\]

If \(A=0\), the two coordinates in (3) are equal, so the word is not a
positive separator. If \(A\ne0\), the first coordinate can be zero only when
\(r=f(A,B)\), and the second can be zero only when \(s=f(A,B)\). Both choices
were excluded. Thus neither coordinate is zero, and (2) follows. \(\square\)

## 3. Polynomial-menu consequence

Let the external input length be \(n\), and let a proposed rule prescribe at
most \(T(n)\) exponent pairs before seeing the correlation-breaking
generator. Whenever an odd prime \(L>T(n)+2\) is used in the model, Theorem 1
chooses a maximal extension missed by every prescribed word.

In particular, a fixed box

\[
|A|\le E(n),
\qquad
|B|\le E(n)
\]

has at most \((2E(n)+1)^2\) residue pairs and can be avoided when
\(L>(2E(n)+1)^2+2\). The same conclusion applies to any fixed union of
polynomially many explicit exponent schedules, including bounded integers,
powers of two, or least-common-multiple exponents.

This is stronger than saying that uniform density can be small. The menu can
miss **every** separator even though the extension is the full product and
the new generator itself breaks the old diagonal correlation.

## 4. Relation to sign gcds

The theorem is stated for the positive identity target. It can model
subgroups of odd order inside local unit groups. In such a realization the
local element \(-1\), which has order two, is outside both local subgroups.
Therefore the negative sign test adds no target inside the modeled enlarged
subgroup.

This observation is group-theoretic only. No bounded-size semiprime
realization, canonical-inverse integer split, or factor-free construction of
the displayed generators is claimed.

## 5. Exact scope and algorithmic consequence

The quantifier order is essential:

\[
\text{menu first}\quad\longrightarrow\quad\text{new generator second}.
\]

The result covers literal exponent boxes and other input-independent
schedules. It does not cover:

* a menu chosen after inspecting the numerical representative of \(z\);
* value-dependent CRT beams;
* quotient-fibre gcd searches;
* adaptive integer refinement;
* square-class closure and complete decoding; or
* an algorithm that learns a cancellation exponent from additional
  structure.

Thus the result does not close feedback. It removes one proposed shortcut:
the fixed small-exponent menu that happens to solve P81's \(N=4033\) state
cannot be promoted to a universal group-theoretic guarantee.

Together with F78, it points to a narrower live target. A successful feedback
algorithm must use numerical, quotient, or refinement data to choose its
words **after** it sees the new integer representation. Merely expanding the
subgroup and applying a fixed polynomial word catalogue is insufficient in
the diagonal model.
