# F240 V2 frozen manifest

## Status

V1 is preserved unchanged in `STATEMENT.md`, `PROOF.md`, `SELF_AUDIT.md`,
`PROVENANCE.md`, and `MANIFEST.md`.  `HOSTILE_AUDIT.md` is also preserved
unchanged.  The audit returned **FAIL** because the allowed true tuple at
`B=N-1,u=1` has `a=b=0,c=1,T=0`; its recovery polynomial is identically
zero.

V2 repairs only this defect.  Every direct decoder and direct-factor-bank
claim now requires nonnegative centers with `(a,b)!=(0,0)`.  The decoder
skips the two-zero-center tuple.  The proof separately checks the safe
`a=0<b` case, the impossible true `a>0,b=0` case, simultaneous zero centered
residues, a zero discriminant, and the round-half-up negative endpoint.

- Type: proof-only candidate.
- Status: self-audited; fresh hostile re-audit and blind reconstruction
  pending.
- Numerical computation: none.
- Durable ledger edits: none.

## Frozen V1 predecessor hashes

| Artifact | SHA-256 |
|---|---|
| `STATEMENT.md` | `a9e57ccf65bcc793bccf844fb74216742acaecabe77d4e34ec9946ffb98015b9` |
| `PROOF.md` | `d8a1df081ee5c8c52a4515c1f0370486a8546a3a4589dce3bd76732fa0a76015` |
| `SELF_AUDIT.md` | `a7ac335219c52fb61f881eddfbc26fde16f2f7bff32fa5cd2a968b46fa8e24c2` |
| `PROVENANCE.md` | `521b31b7e210516311427ada75b6a719997ca76df9c71d9f35a8d990bc097361` |
| `MANIFEST.md` | `99affe0665add866d18b15bf2583cca8cba2a45327645849cce06c96be446caa` |
| `HOSTILE_AUDIT.md` | `4cd1acc3f3fdfe387a9c016c64602baebe81156463bf01ae40726df6f1c9e7be` |

## Frozen V2 hashes

| Artifact | SHA-256 |
|---|---|
| `V2_STATEMENT.md` | `d74ea1c31f24a59b643dc38d69326be553bc3944ef80cee4f72a7a2e607e9914` |
| `V2_PROOF.md` | `1a4bb957465f2bceb0ce3166df5f1c56d7ece68af36a4a5f9cafa426aa3dd758` |
| `V2_SELF_AUDIT.md` | `010610012643682a422e61eb37d3bc7c9230463ba2695f3795cbee6c141581e2` |
| `V2_PROVENANCE.md` | `c1e515dd9efd3925c63b0aa2991a9ec87367ba5d29b07be1aad5c6d740fd53da` |

## Review gate

1. Fresh hostile re-audit of the four frozen V2 artifacts.
2. Fresh statement-only reconstruction after the re-audit passes.
3. No durable-ledger promotion before both checks pass.
