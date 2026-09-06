# F149 manifest — compact large-anchor boundary

## Purpose

F149 tests the compact numerically large-anchor sector left open by P131.
It asks whether raw anchor magnitude can itself create a new P128 bridge
square class or containment signal.

## Artifact type

Proof-only candidate.  No computation was registered or run.

## Files

- `STATEMENT.md` — frozen V1 candidate statement.  It is preserved because
  its first hostile audit failed.
- `PROOF.md` — direct proof of canonicalization, singleton closure,
  self-containment, the semiprime count, and the certificate.  The proof
  already states the correct `h >= 0` result and is reused unchanged by V2.
- `HOSTILE_AUDIT_FAILED.md` — preserved V1 hostile audit and counterexample.
- `V2_STATEMENT.md` — narrow corrected candidate statement.  It changes the
  self-loop multiple to `h >= 0` and states that usefulness forces `h >= 1`.
- `V2_HOSTILE_REAUDIT.md` — passing fresh hostile review of V2.
- `V2_BLIND_RECONSTRUCTION.md` — passing statement-only independent
  reconstruction of V2.

Frozen V1 SHA-256 hashes:

- `STATEMENT.md`:
  `25af29ad09343eef88d7652f988b4ebd2f982e0d17ec6a0de867982c7e660738`;
- `PROOF.md`:
  `08cd204330f47429f20e747a1c8bad9a7084ec5de9249a8e5e755f55e305da0e`;
- `HOSTILE_AUDIT_FAILED.md`:
  `e461d3984a77e4873f0bbcfdc5c6fa2de6bf8d2ea3b30fa9d45534942ac81346`.

Frozen V2 inputs for fresh review:

- `V2_STATEMENT.md`:
  `8e116d027dd5ecfe14f789fd301e9a6f4cf3b62e402fa2575cfc34406aa4d4dd`;
- unchanged `PROOF.md`:
  `08cd204330f47429f20e747a1c8bad9a7084ec5de9249a8e5e755f55e305da0e`.
- `V2_HOSTILE_REAUDIT.md`:
  `8d4ecd2eaccdfc9fe89677e6678e77eb4100ee91a6409ac228b36c79366933ab`;
- `V2_BLIND_RECONSTRUCTION.md`:
  `844505799fb6a3ca04a4690547feb8aa9ae63f036f08133d185a4f123463dbda`.

No `V2_PROOF.md` is needed.  The original proof already derives
`alpha^2-S^2=h'N` with `h' >= 0` and separately proves that a useful root
excludes `h'=0`.

## Candidate conclusion

- Every endpoint and containment residual depends only on the anchor residue
  modulo (N).
- A squared anchor contributes no parity to the lifted P128 column.
- One canonical-plus-lifted position closes exactly when
  (q[q\alpha^2]_N) is an integer square.  This is an ordinary congruence
  of squares.
- On an odd semiprime, useful singleton anchor residues have exact density
  (2V_d/\varphi(N)=O(N^{-1/2})).  Quasipolynomially many uniform-marginal
  trials remain negligible.
- A compact-word source could still be factor-correlated.  Multi-relation
  arithmetic closure also remains open.
- The (N=77) example is a conditional source-semantic certificate, not a
  surviving run of the complete preprocessing.

## Review state

The frozen V1 statement failed its first hostile audit because it asserted
`h >= 1` for every exact self-loop square.  The audit supplied the valid
global-root counterexample `N=77`, `q=2`, `a=alpha=S=3`, for which `h=0`.

V2 repairs only that claim and reuses the already-correct proof.  It passed a
fresh hostile audit and a statement-only blind reconstruction.  It is
promoted as P135.  No cross-family audit, human audit, or publication-level
literature review has run.
