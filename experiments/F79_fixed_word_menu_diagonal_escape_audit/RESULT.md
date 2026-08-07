# F79 hostile audit — fixed word menus in the diagonal model

## Verdict: PASS

I audited
`experiments/F79_fixed_word_menu_diagonal_escape/RESULT.md` at SHA-256

```text
1182b0088dcf105324c929d622dc0c63952dbbf00951659ca27e725a3784566e
```

The hash matches the requested artifact. This was a proof-only audit. I ran
no research computation.

The theorem, its menu-size corollary, and its negative-sign observation are
correct. The result has the exact quantifier order

\[
\forall S\quad\exists z=z(S)\quad\forall(A,B)\in S.
\]

It does not give one \(z\) that defeats all menus, and it does not cover a
menu selected after \(z\) is known. It also does not realize the abstract
groups through canonical integer feedback. The candidate states all of these
limits.

## 1. Quantifier order

Fix a prime \(L>2\). The menu \(S\subseteq\mathbb F_L^2\) may depend on
\(L\), but it is fixed before \(r,s\), and hence before \(z=(r,s)\), are
chosen. The proof then constructs \(r,s\) from the complement of the
menu-dependent forbidden set. Thus the proved statement is

\[
\text{for every predeclared }S\text{ of size at most }L-3,
\text{ there is an avoiding }z.
\]

No quantifier is reversed in the proof.

This order is essential. If the two CRT coordinates \(r,s\) are visible
before the menu is chosen, then the single word

\[
z-rg=(0,s-r)
\]

is a positive separator. Equivalently, the adaptive pair
\((A,B)=(1,-r)\) succeeds. This does not refute F79 because the candidate
explicitly excludes menus chosen after inspecting \(z\), adaptive
value-dependent beams, and algorithms that learn a cancellation exponent.

The theorem also does not produce a single hard generator for every small
menu. A different menu can require a different avoiding choice of \(r,s\).

## 2. Forbidden-ratio count

For a word \(Az+Bg\) with \(A\neq0\), a zero in either coordinate occurs
exactly when the corresponding coordinate of \(z\) equals

\[
f(A,B)=-B/A.
\]

Each menu pair with \(A\neq0\) contributes at most one forbidden field
element. Repeated ratios only reduce the count, so

\[
|F|\leq |\{(A,B)\in S:A\neq0\}|\leq|S|\leq L-3.
\]

The complement has at least three elements. Since a field has only one zero,
the complement contains at least two distinct nonzero elements. They can be
chosen as \(r,s\).

For \(A\neq0\), neither coordinate

\[
Ar+B,\qquad As+B
\]

can then vanish. For \(A=0\), both coordinates equal \(B\): either both are
zero or both are nonzero. In neither case is the word a positive separator.
This covers every menu pair, including \((0,0)\).

The bound \(L-3\) is used correctly. With only two complement elements, one
could be zero and there might be only one allowed nonzero coordinate, so the
proof really needs the displayed three-element complement for this simple
construction.

## 3. Old state, new generator, and maximal generation

The diagonal subgroup

\[
H=\{(t,t):t\in\mathbb F_L\}
\]

has no element with exactly one zero coordinate. The chosen \(z=(r,s)\)
also has no zero coordinate because \(r,s\neq0\).

Using \(g=(1,1)\) and \(z=(r,s)\) as columns gives

\[
\begin{pmatrix}
1&r\\
1&s
\end{pmatrix}.
\]

Its determinant is \(s-r\), which is nonzero by construction. Since \(L\)
is prime, \(\mathbb F_L\) is a field and the two columns form a basis.
Therefore

\[
\langle H,z\rangle=\mathbb F_L^2.
\]

The enlarged group contains \((0,1)\) and many other positive separators.
Thus the construction simultaneously has a maximal extension, a
nonseparator new generator, and no separator in the prescribed menu. The
determinant argument is exact and does not assume an unproved cyclic-group
identity.

## 4. Polynomial menu and exponent-box corollaries

Let a rule output at most \(T(n)\) exponent pairs. If the odd prime \(L\)
satisfies

\[
L>T(n)+2,
\]

then, because the quantities are integers,
\(T(n)\leq L-3\). Reducing the exponent pairs modulo \(L\) can only merge
menu entries. Theorem 1 therefore applies.

The integer box

\[
|A|\leq E(n),\qquad |B|\leq E(n)
\]

contains \((2E(n)+1)^2\) integer pairs when \(E(n)\) is an integer, and at
most that many distinct residue pairs modulo \(L\). The condition

\[
L>(2E(n)+1)^2+2
\]

puts the reduced menu within the theorem's bound. Large exponents,
collisions modulo \(L\), and exponents divisible by \(L\) cause no problem;
collisions shrink the menu, and \(A=0\) residue pairs are harmless diagonal
words.

The same reasoning covers any predeclared union only when its total number
of distinct residue pairs is within the stated bound. The candidate's
reference to polynomially many explicit schedules is correctly read in this
finite-menu sense. It does not prove that an unspecified schedule with
exponentially many entries is avoidable.

The external parameter \(n\) has no asserted arithmetic relation to an
integer modulus here. The corollary is conditional on using a prime
\(L>T(n)+2\) in the abstract model. It does not construct a semiprime whose
local subgroup order has that value.

## 5. Negative sign in an odd-order realization

Suppose the two copies of \(C_L\) are realized as local unit subgroups of
order \(L\), with \(L\) odd. In an odd-prime field, the local element
\(-1\) has exact order two. Lagrange's theorem therefore excludes \(-1\)
from each order-\(L\) local subgroup.

Every element of the modeled enlarged group has both local components inside
those order-\(L\) subgroups. Hence no component can equal \(-1\), and the
negative sign gcd has no target inside this modeled group. The statement is
correct.

This is conditional group theory, not a realization theorem. F79 does not
construct the local embeddings, a semiprime of controlled bit length, or
public CRT generators without knowing the factors.

## 6. Exact scope

The result is about the two-generator linear word menu

\[
\{Az+Bg:(A,B)\in S\}
\]

in an abstract diagonal \(C_L\times C_L\) model. It does not cover:

- a menu that depends on the numerical or hidden-coordinate data of \(z\);
- an adaptive procedure that learns a forbidden ratio;
- words generated after integer gcd refinement;
- quotient-fibre searches or canonical inverse arithmetic;
- square-class closure and exact-root decoding; or
- a canonical integer block split realizing the adversarial \(z\).

In particular, the proof chooses \(z\) after seeing the menu. A real
canonical feedback rule chooses \(z\) from \(N\) and its integer transcript;
F79 supplies no reason that this output can be adversarially varied over the
needed field pairs. No abstract-to-integer inference is made.

The theorem therefore refutes only a universal guarantee for a predeclared
small exponent catalogue in this model. It is not an adaptive-selector lower
bound, an integer family, a factoring obstruction, or a factoring algorithm.
The candidate states this boundary correctly. Its references to P81, P83,
and F78 are historical context and were not re-audited here.
