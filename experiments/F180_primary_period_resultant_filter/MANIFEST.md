# F180 manifest

Status: V1 failed strict statement-only reconstruction because it did not
define the input-length parameter. V2 is a narrow self-contained repair;
fresh hostile re-audit passed and fresh statement-only reconstruction is
pending.

Files:

- `STATEMENT.md`
- `PROOF.md`
- `SELF_AUDIT.md`
- `MANIFEST.md`

The candidate depends on the verifier-backed P160/F178 hard-branch
interface. It makes no all-input factoring claim. No computation was run and
no durable ledger was edited by the artifact itself.

Frozen SHA-256 hashes:

- `STATEMENT.md`: `9ae4beb80683a7b7e61c82a91891e2e1f849ac96d498f3570519bfbebb9b1f29`
- `PROOF.md`: `ef703570255ba10a68e034ba1d0434648f1411b2ef61f8a2bd3f0287a4117dd4`
- `SELF_AUDIT.md`: `c45905be68c99d1070cbfc3c6ddd46a5f2b53dbc7e3377cbf66c8b3f3b6efb1c`

The fresh hostile audit passed. Its report is `HOSTILE_AUDIT.md`, SHA-256
`84f7c2383b23f37c7dff192d092922a124f6a40a065e0881cb57fdfb3f8ea428`.

The strict V1 statement-only reconstruction failed and is preserved as
`BLIND_RECONSTRUCTION.md`, SHA-256
`dee5b1543c89313a45340dcefb6e2d4706564d955b57211a41b780862e83a0f4`.
Its only theorem defect was that V1 never tied `n` to `N`; it supplied an
exact counterexample under the literal unconstrained reading. V2 adds
`n=ceil(log2(N+1))` and otherwise preserves the theorem.

V2 frozen inputs:

- `V2_STATEMENT.md`: `8bf8e7ca10a0d58f8548bd88605d015b87fa62f41208e542075cf83951aa6a3c`
- reused `PROOF.md`: `ef703570255ba10a68e034ba1d0434648f1411b2ef61f8a2bd3f0287a4117dd4`
- reused `SELF_AUDIT.md`: `c45905be68c99d1070cbfc3c6ddd46a5f2b53dbc7e3377cbf66c8b3f3b6efb1c`

The V2 hostile re-audit passed. Its report is `V2_HOSTILE_REAUDIT.md`,
SHA-256
`6916e9f91c13856c4254b6bc8a47c2c41bfe424c14d9574bfa80ab136401c72f`.
