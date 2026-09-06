# F202 candidate manifest

Status: frozen proof-only candidate.  No numerical search was run, and no
durable ledger was edited.

## Frozen files

- `STATEMENT.md`:
  `266e527434b5c6b9f3a680b0ea31498cd8f55411d1ec75a459f4d8bd21587719`
- `PROOF.md`:
  `7a7227718561de054330a1ae29c128e20e1bff477125370856376fcb7759e8cf`
- `SELF_AUDIT.md`:
  `9b0d0eb4db936359b15b6b4f8dc1502c44eb4c39679bed1597691ea61319f5cd`

## Purpose

F202 tests a fresh integer-specific beta-two route.  It recursively factors
the canonical half-bit-size child

\[
E=N-\lfloor\sqrt N\rfloor^2
\]

and asks whether the resulting exact prime support selects the hidden
factor orientation.

The candidate proves:

1. the one-child recursion has the valid bound
   \(T(n)\leq T(n-1)+Q(n)\);
2. product and discriminant consistency modulo divisors of \(E\) accept
   every unit candidate factor residue;
3. the mixed-root ideal class is a square and is invisible to genus
   characters;
4. a second factor-bearing principal norm exists only on the special branch
   where that square class is principal; and
5. \(N=2627\), \(E=26=2\cdot13\) is an exact certificate where the second
   principal norm and the ramified-form composition both fail.

## Imported context

- P26 is the closest literal trace-wheel boundary.  F202 adds the fully
  factored canonical modulus \(E\) and proves the exact factor-residue
  identity for every divisor of it.
- P27 is the closest imaginary class-group ambiguity boundary.  F202 uses
  the smaller discriminant \(-4E\), whose factorization is recursively
  available, and identifies the remaining class as a square inside the
  principal genus.
- P175 is used only for the statement that a quarter-minus-polylog prefix of
  \(p^{-1}\) is a QP terminal.

## Exact scope exclusions

F202 does not prove a lower bound for arbitrary algorithms given
`factor(E)`.  It does not exclude nonlocal auxiliary moduli, interval
filtering in the \(d\)-coordinate, compressed computation in the full
proper class group, Archimedean size statistics, or direct selection of the
P175 reciprocal prefix.  It supplies no all-input factorization algorithm.
