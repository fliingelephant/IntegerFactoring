# F152 manifest

- Date: 2026-08-11
- Type: proof-only candidate
- Computation: none
- Durable ledgers: not edited
- Intended closest results: P66, P108, P129, P134
- Main new boundary: factor, extend a public decorated section, or agree with it
- Explicit nonclaim: no quasipolynomial source theorem and no factoring algorithm

## V1 preserved failure history

- Candidate statement: `STATEMENT.md`
- Candidate proof: `PROOF.md`
- Hostile audit: `HOSTILE_AUDIT.md`, PASS
- Statement-only reconstruction: `BLIND_RECONSTRUCTION.md`, FAIL
- Failure: pairwise coprimality did not exclude square blocks, so `ker A`
  was not necessarily the complete integer-square kernel. V1 also omitted a
  supplied-root-aware deduplication rule and layer-membership preservation.

Hashes:

- `STATEMENT.md`:
  `db35d6381867052c876b69111c7b5409030e117501cccec2be12c45c8642a4e4`
- `PROOF.md`:
  `6f7c113eaca89455a22ce3b5d791bc56b7fb98d3520564dbf0b412d56d0f4beb`
- `HOSTILE_AUDIT.md`:
  `9868e66136483f68e303cac606eed385acb2326c8dc28d9a8a3409b480ec9ca3`
- `BLIND_RECONSTRUCTION.md`:
  `440e88465e931cc78f3eee795f056579e015a970b221743d56b50569acf46dcb`

## V2 promoted theorem

- Candidate statement: `V2_STATEMENT.md`
- Candidate proof: `V2_PROOF.md`
- Repair: require independent exact square classes, give a root-aware
  exact-value deduplication rule, retain all occurrence and layer metadata,
  and call the finite certificate a two-row illustration.
- Review status: fresh hostile re-audit passed; fresh statement-only blind
  reconstruction passed with the precise qualification that one source can
  already violate the section through an internal circuit. Two named sources
  are a useful presentation, not a logical necessity.

Hashes:

- `V2_STATEMENT.md`:
  `3f5b232d6bdeb9ca6a70cecd2bdfc0e1307406de3f84a23c953c59323fcfc78e`
- `V2_PROOF.md`:
  `46b45cc752f5524670431cd288b5b5baa6cb246d1f536f447e095e85a3824c67`
- `V2_HOSTILE_REAUDIT.md`:
  `bd6f32a0c5c9d431ab1864df6050ef5a69874c26fe3b3962f31df4c889dc170d`
- `V2_BLIND_RECONSTRUCTION.md`:
  `0ae27e94baf3f67baded253fbd642b23ba318cc671e67b7098fa1acccdb36c0b`

## Durable promotion

- Promoted as `P138` in `PROVED.md`.
- Recorded as `C145` in `notes/Progress.md`.
- No computation was used.
