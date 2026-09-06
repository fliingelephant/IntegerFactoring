# F142 manifest — squared-anchor rank and root gate

## Frozen proof-only candidate

F142 assumes the frozen F141 source and makes no source change.

Its exact conclusions are:

- the standalone lifted matrix is a rank-one perturbation of the inverse
  endpoint parity matrix;
- relative to the matched canonical ledger, every lifted column is
  equivalent to the bridge square class \([q]+[c_\ell]\);
- the relative dependency gate is
  \(\Gamma x+t(x)a\in\operatorname{colspan}(M_0)\);
- a bridge forest can remain full rank;
- an exact endpoint cycle closes, and its normalized root is the product of
  its public anchors.

Thus F141 advances row reuse but does not by itself force final rank.  The
remaining gate is a cycle or hypercycle in the bridge incidence quotient,
followed by a non-global normalized root.

## Frozen hashes

| Artifact | SHA-256 |
|---|---|
| STATEMENT.md | 0049f74a635b7da7f288460ddbaf8e6669eb329073e8164b0834e74d3e4c1a1e |
| PROOF.md | 4f257c6425f81926459b6acba3d401af2024c5d9394889150bcb9fa148f7dc4e |

## Evidence and scope

No computation was used.  No actual infinite forest family or forced
adaptive cycle is claimed.  The forest is an exact abstract square-class
obstruction showing that the proved F141 row facts alone do not imply rank
closure.

## Verification state

The frozen proof-only candidate passed both required checks.

| Artifact | SHA-256 | Result |
|---|---|---|
| HOSTILE_AUDIT.md | d79807b7c91e0f1e4148665160e3e4bd422ca10b6af31ad1c8d892a7114fc3a9 | PASS as claimed; bridge, rank, forest, cycle, and normalized-root formulas survived hostile review |
| BLIND_RECONSTRUCTION.md | 2e48402b73781d9779c271566f0548eddbade68052c033f5eed8b9d27d58d498 | PASS from the frozen statement only; odd-input preprocessing and matched-canonical-ledger scope were made explicit |

The result is verifier-backed and can be promoted. It has no cross-family,
human, or publication-level literature audit.
