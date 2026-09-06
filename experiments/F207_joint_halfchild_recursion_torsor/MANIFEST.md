# F207 manifest

## Family

F207: joint half-child recursion and inverse-torsor boundary.

## Closest prior work and material difference

- P165 proves that the single decrement child `(N-1)/2` is QP-safe.
- P180 proves that the square-gap child is roughly half-size and that its
  direct congruence, principal-norm, genus, and ramified-class routes do not
  force an orientation.
- F205-D01 tests a fixed numerical family using both complete child
  factorizations.

F207 supplies the missing mixed recursion theorem and the exact joint local
normal form. Its new obstruction is inversion symmetry, not insufficient
contraction.

## Frozen contents

- `STATEMENT.md`: candidate theorem statement and scope.
- `PROOF.md`: proof.
- `SELF_AUDIT.md`: author-only audit.
- `MANIFEST.md`: provenance and scope.

Frozen SHA-256 hashes:

- statement:
  `d3ca187a62f3706749cbe3f0083c25dccf7b82b21edf3c514377b2cc839c0774`;
- proof:
  `692c011c170e81251faa4ae590c2b927ed2ecd0b21c4c5d2d4f715aeee101484`;
- self-audit:
  `7e86ad7e9174180912ee7cf6510a6d212c95961cf2f5655bb7ebaaea2b263a57`.

## Computation

None. F207 is proof-only. F205-D01 is a separate finite experiment and is not
used to prove an unbounded F207 claim.

## Status

Self-audited. No hostile audit, blind reconstruction,
cross-family audit, human audit, or publication-level literature review has
run.

## Exact remaining gap

Construct a QP non-inversion-invariant integer statistic from the two child
factorizations, or evaluate the P179 twisted divisor selector. The packet does
not supply such a postprocessor and does not extend the recursion accounting
to unbalanced inputs with two independent near-size children.
