# F206 manifest

## Family

F206: joint half-child recursion and inverse-torsor boundary.

## Closest prior work and material difference

- P165 proves that the single decrement child `(N-1)/2` is QP-safe.
- P180 proves that the square-gap child is roughly half-size and that its
  direct congruence, principal-norm, genus, and ramified-class routes do not
  force an orientation.
- F205-D01 tests a fixed numerical family using both complete child
  factorizations.

F206 supplies the missing mixed recursion theorem and the exact joint local
normal form. Its new obstruction is inversion symmetry, not insufficient
contraction.

## Frozen contents

- `STATEMENT.md`: candidate theorem statement and scope.
- `PROOF.md`: proof.
- `SELF_AUDIT.md`: author-only audit.
- `MANIFEST.md`: provenance and scope.

Frozen SHA-256 hashes:

- statement:
  `0035fd01b9e1eacf188da8fbf1659f034b226c779a295b3e8e35a08387fc8783`;
- proof:
  `27e7a594811f8d7830b36e1b346e5e7f367676168ae8961733e68baefece79fe`;
- self-audit:
  `260f10c387f852777e6cdcee205c14be9dbe05c57a37ff2159446084e7e09d11`.

## Computation

None. F206 is proof-only. F205-D01 is a separate finite experiment and is not
used to prove an unbounded F206 claim.

## Status

Self-audited. No hostile audit, blind reconstruction,
cross-family audit, human audit, or publication-level literature review has
run.

## Exact remaining gap

Construct a QP non-inversion-invariant integer statistic from the two child
factorizations, or evaluate the P179 twisted divisor selector. The packet does
not supply such a postprocessor and does not extend the recursion accounting
to unbalanced inputs with two independent near-size children.
