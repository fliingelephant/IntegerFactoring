# F248 V2 manifest

## Freeze

- Date: 2026-08-13
- Status: proof-only candidate; self-audited; fresh hostile and strict
  statement-only audits required.
- Numerical work: none.
- Durable ledgers edited: none.

## Repair decision

V1's general theorems were sound, but its strict statement-only
reconstruction failed because several family-specific corollaries depended
on definitions outside the statement. V2 takes the narrow repair:

- remove every family-specific constant, marker, orientation, and exponent
  grammar;
- retain Theorems A--G in fully defined general form;
- state quasipolynomial-bank consequences only under the explicit conditions
  \(K=2^{o(n)}\), \(H=2^{\Omega(n)}\), or \(H'=2^{\Omega(n)}\).

V2 does not construct inputs satisfying the conditional size hypotheses. It
does not bound a general nonduplicate multirow exact-square relation.

## Frozen V2 hashes

- `V2_STATEMENT.md`:
  `57ea62c39ce0e04b4a271135e613eabdcf79a32dd5df85dc692effb6dc8d8504`
- `V2_PROOF.md`:
  `0d292831f42bb515d298c26846c7c912cddbf07682b7b63564e9ff2fce3c46f8`
- `V2_SELF_AUDIT.md`:
  `8e35ea5f0ea84ba8c02b848acc4fb1a1dbb53dd5c404c9929ae78975b0795297`
- `V2_PROVENANCE.md`:
  `302e9ffa432c73cda9ced650e2cc3e6ab309e4f5846777b0880fa5903e48ef6a`

## Preserved V1 and audit hashes

The following files were not edited during the V2 repair.

- `STATEMENT.md`:
  `3f45f82829715678e2950dc07c80296e4c3f8230baf9d34bc84d5e2381bd3621`
- `PROOF.md`:
  `d7c2a349784046cd3b3cb8a285c173db06409bfde69894c061244f2d9db1c263`
- `SELF_AUDIT.md`:
  `13f5dfe0213cba44f5242467b1e4ebc3966a34546bbe8212783dbb79a8987240`
- `PROVENANCE.md`:
  `e4eac22617cf6e56cdd1ef90d65a1fc0337059eacfeb7ae3cc3e904eaff0259b`
- `MANIFEST.md`:
  `4a100390362d1f446142c149329f4f4be7a07ad4f215501c69afcb41954fa1f5`
- `HOSTILE_AUDIT.md`:
  `9321ec03a26e1d0ddc5f29dee2874b6498b9a0d0b0bb542c58b4d0f8b2e7c142`
- `BLIND_RECONSTRUCTION.md`:
  `0a4ec2ec1627026dd01c4936a8f3cc71831dd3cd043fbdb8d5c87dc0f8a5ef22`
