# F132 manifest

This directory contains a proof-only kill-first audit of bounded-round unary
all-block feedback.

Status: promoted after a preserved failed hostile audit, a passing fresh
hostile re-audit, and an independent proof-blind reconstruction. The initial
cost attack failed; the corrected cost theorem survives. The same artifact
disproves universal parity reuse and universal 2-core progress. It proves no
all-input progress law and no factoring theorem.

Files:

- `STATEMENT.md` — exact cost theorem, row law, and four certificates.
- `PROOF.md` — self-contained proofs and arithmetic verification.
- `HOSTILE_AUDIT_FAILED.md` — preserved first hostile-audit failure and the
  required corrections.
- `HOSTILE_REAUDIT.md` — fresh hostile re-audit of the corrected statement.
- `BLIND_RECONSTRUCTION.md` — independent reconstruction from the statement
  alone.

No registered research computation supports the result. The numerical
examples are exact certificates verified in the proof and independently
recomputed. One hostile audit failed the first wording and is preserved. No
cross-family audit, human audit, or publication-level literature review has
run.

SHA-256:

- `STATEMENT.md`:
  `41331f37531a2303dc7c372cbabe49110450b4b2e080800c842c62fb84d79a64`
- `PROOF.md`:
  `da1d333a4dd87745013f56bd17fc04a06b08f29cd09258be65071ec77afae56b`
- `HOSTILE_AUDIT_FAILED.md`:
  `fdbf9cb7078a19b8287e6357e245a4ab2d98b559a47802aeba2ee150f8398e24`
- `HOSTILE_REAUDIT.md`:
  `a0e690209182053993e3b1b4634856dd7b5ef433c4db8de8f5cd97d7ded21938`
- `BLIND_RECONSTRUCTION.md`:
  `25f237a201152aad8e211a89b31887301ea02b8bf354d5700f1dc371f3ac7c80`
