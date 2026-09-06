# F143 manifest — Cayley-cycle order boundary

## Promoted proof-only boundary

F143 tests a proposed Cayley-graph continuation of the F141 squared-anchor
lift.  Its exact conclusions are:

- public vertices satisfy
  \(v_z=v_{z'}\) exactly when \(2(z-z')\) lies in the modular relation
  lattice;
- an allowed formal bridge cycle with signed displacement \(\delta\) has
  normalized root \(\Phi(\delta)\);
- the same root is available directly from the public vertex collision, so
  the bridge cycle adds no factor signal beyond that collision;
- zero-displacement commutation diamonds have logical bridge products with
  root \(+1\); nondegenerate ones are exact dependencies, while degenerate
  ones can collapse to zero;
- the complete formal Cayley-cycle image is the 2-torsion subgroup of the
  generated modular group;
- in one fixed squared-anchor star, two wrapped residue endpoints share
  only primes below the fourth power of the anchor cap; and
- after removing that public factor base, every endpoint selected by a
  bridge-only arithmetic dependency must have a square residual.

Arithmetic hypercycles outside formal endpoint incidence are not fully
closed.  In particular, cancellation against arbitrary old columns remains
open.

This is a source-specific refinement of P71, not an all-input selector and
not a factoring algorithm.

## Frozen hashes

| Artifact | SHA-256 |
|---|---|
| STATEMENT.md | bc9a9e399c03bff991cc85920eb6c0218276b1d05d0788b82461b39030b1a35a |
| PROOF.md | 7c2784202f2a42200b126b54262c5d202ad86a0c2d1cc35931ddf52322ad86c2 |
| HOSTILE_AUDIT.md | 834facda506ed2995c46a17e1212c1896fbc69d7c969f043fb7003a05c4a2c74 |
| BLIND_RECONSTRUCTION.md | 52f1f2506b9c74eff93389655ccddb3a4323fe732ead56aecc987690392d331c |

## Evidence and scope

No research computation was used.  The cycle result is conditional on each
graph edge being a legal F141 word position.  A canonical residue is not
automatically a named block.  Global exact-value deletion is handled at the
actual canonical/lifted relation level, before the conceptual bridge change.

The fixed-star result concerns bridge-only dependencies.  It does not
control the full F142 relative kernel after arbitrary old columns are
allowed.

The hostile audit passed.  A fresh statement-only blind reconstruction also
passed.  The reconstruction clarified that the displayed vertex set is a
coset of the square subgroup, that \(-1\) need not lie in the generated
subgroup, and that repeated logical edges must be reduced modulo two.  These
are interpretation details and do not change the frozen theorem.

F143 is promoted as P130.  No cross-family audit, human audit, or
publication-level literature review has run.
