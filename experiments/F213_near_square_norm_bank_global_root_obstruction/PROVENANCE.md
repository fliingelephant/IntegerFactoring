# F213 provenance

## Namespace

Before creation, a repository-wide search found no F213 entry or experiment
directory.

## Source question

The proposed integer-specific family takes QP-many public multipliers
\(a\), forms

\[
r_a=\lfloor a\sqrt N\rfloor,
\quad E_a=a^2N-r_a^2,
\quad F_a=(r_a+1)^2-a^2N,
\]

recursively factors the smaller norms, and applies a QS/CFRAC-style parity
matrix. The question was whether cardinality plus complete recursive norm
factorization forces a dependency with a non-global root.

F213 arose from a kill-first audit. On the exact no-carry family
\(N=s^2+1\), all lower norms collapse to squares \(E_a=a^2\). The adjacent
norms can then be assigned distinct valuation-one private primes by CRT.
This makes the complete parity kernel explicit and forces its normalized
root image to be \(\{1,-1\}\).

## Closest prior routes and material difference

- P180/F202 studies the single canonical square gap
  \(N-\lfloor\sqrt N\rfloor^2\). It proves that recursively factoring that
  child is safe but leaves a principal-genus orientation gate. F213 instead
  treats a growing multiplier bank, adds the adjacent norms, and gives an
  exact private-row parity obstruction.
- P183/F207 proves the correct one-spine-plus-fixed-ratio-side-call QP
  recurrence and an inversion-torsor boundary for two factored children.
  F213 fully accepts that recurrence. Its failure occurs after the child
  factorizations, in the parity kernel and normalized-root image.
- F01/X01 gives a generic rank obstruction for exact compression of
  arbitrary square classes. F213 does not invoke genericity. It constructs
  the exact integer-specific columns and proves their full kernel.

The material new point is the conjunction of:

1. exact floor identities for every public \(a=1,\ldots,M\);
2. a CRT construction giving every optional \(F_a\) its own valuation-one
   prime row;
3. a proof of the entire parity kernel; and
4. a proof that every surviving dependency has global normalized root.

## Correction made during the hostile pre-freeze audit

An initial sketch asserted that all private primes could be chosen with
\(O(\log M)\) bits and concluded \(n=\Theta(M\log M)\). That requires a
prime-density theorem and was not justified by the sketch.

The frozen proof instead uses only repeated applications of Bertrand's
postulate. The private primes grow through disjoint dyadic intervals. The
proved size is

\[
\Omega(M^2)\leq n\leq O(M^2\log M),
\]

which still gives a polynomial bank
\(2M=n^{1/2+o(1)}\). The frozen packet makes no short-interval
prime-density claim.

## Mathematical dependencies

The only named theorem is Bertrand's postulate. The remaining ingredients
are elementary:

- a prime divisor of an integer greater than one;
- the criterion that \(-1\) is a quadratic residue modulo an odd prime only
  for primes congruent to one modulo four;
- uniqueness of a simple-root lift modulo a prime square;
- the Chinese remainder theorem; and
- valuation parity over the rational primes.

No factoring theorem, distribution heuristic, or smoothness hypothesis is
used in the obstruction.

## Computation and evidence

No mathematical computation, finite search, random sampling, local
experiment, or remote experiment was performed. Hashing is used only to
freeze the proof text.

## Ledger policy

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, or inspiration file is edited by this packet.
