# F206 manifest

## Frozen candidate files

- `STATEMENT.md`
  - SHA-256: `a35bfc475cb068bab78cb3f12bae605492ab22f4b208b6c809f7692f1cd4805c`
- `PROOF.md`
  - SHA-256: `e617d242fe213e9ea5ec691493e7694c2550ab6a559a7eaf4eeee1f8aa2464cc`
- `SELF_AUDIT.md`
  - SHA-256: `18e5587a679fff757973472a981216c4840d52f3426c2d3b8d327f968342d413`
- `PROVENANCE.md`
  - SHA-256: `1fc45be8d749462991ae699313c38d1555c073767cfe1241d6071d79223b7429`

## Evidence class

Frozen proof-only candidate. No mathematical computation was run. Hashing is
used only to freeze the text. No durable registry, proved ledger, failed
ledger, or progress ledger was changed.

## Highest-risk claims to audit

1. The Lambert asymptotic. Check the Mellin residues at `s=1,0,-1,-2` and
   the sign in the binary relation at the cusp one-half.
2. The semisimple vector cusp lemma. Check the transported fixed projection,
   the unique zero-mode power `y^(-k)`, and the need for semisimple parabolic
   monodromy and ordinary meromorphic cusp expansions.
3. The Mellin reflection. Recompute the conductor powers and the tangent
   factor directly from the zeta and beta functional equations.
4. The matrix scope. Check that the claim excludes only the natural pure
   two-kernel constant-matrix Fricke law and fixed finite rational Mellin
   repairs, not arbitrary vector-valued or nonholomorphic completions.
5. The Whittaker circularity. Check that an archimedean kernel change leaves
   the Dirichlet coefficients `A(n),A^vee(n)` intact and that
   `A^vee(N)=chi(N)A(N)` at every odd target.
6. The algorithmic scope. Reject any reading of dense `Theta(N)` truncation
   as a general coefficient-complexity lower bound.

## Required reviews

1. Recompute all four content hashes before reading the packet.
2. Run a fresh hostile audit of the frozen statement and proof.
3. If that audit passes, run a fresh strict statement-only reconstruction.
4. Promote only after both reviews pass and all frozen hashes are rechecked.
