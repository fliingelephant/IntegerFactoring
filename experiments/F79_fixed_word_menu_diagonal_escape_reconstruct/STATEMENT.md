# F79 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the candidate proof,
its hostile audit, C82 in the progress notes, or any later proof artifact.

Let \(L>2\) be prime, write \(C_L\) additively as \(\mathbb F_L\), and let

\[
S\subseteq\mathbb F_L^2,
\qquad
|S|\le L-3.
\]

The menu \(S\) may depend on \(L\), but it is fixed before the new generator
below is chosen. A pair \((A,B)\) represents the word \(Az+Bg\).

Prove or refute that there are distinct nonzero
\(r,s\in\mathbb F_L\) such that, with

\[
g=(1,1),
\qquad
H=\langle g\rangle,
\qquad
z=(r,s),
\]

all of the following hold:

1. \(H\) contains no element with exactly one zero coordinate.
2. \(z\) does not have exactly one zero coordinate.
3. \(\langle H,z\rangle=\mathbb F_L^2\).
4. The enlarged group contains elements with exactly one zero coordinate.
5. For every \((A,B)\in S\), the word \(Az+Bg\) does not have exactly one
   zero coordinate.

Then derive the exact finite-menu consequences:

* every predeclared menu of \(T(n)\) exponent pairs is avoidable in this
  model when an odd prime \(L>T(n)+2\) is used;
* the full integer box \(|A|,|B|\le E(n)\) is avoidable when
  \(L>(2E(n)+1)^2+2\), after reduction modulo \(L\); and
* any fixed union of explicit schedules is covered only when its total
  number of distinct residue pairs satisfies the same finite-menu bound.

Finally, check the following scope claims:

* an odd-order realization inside local unit groups contains no local
  \(-1\), so the negative sign adds no target inside the modeled group;
* the quantifier order is menu first, generator second;
* the result does not cover a menu chosen after inspecting \(z\), an
  adaptive or value-dependent selector, quotient-fibre or integer-refinement
  operations, square-class decoding, or a canonical-inverse integer
  realization; and
* it proves neither a computational lower bound nor a factoring algorithm.
