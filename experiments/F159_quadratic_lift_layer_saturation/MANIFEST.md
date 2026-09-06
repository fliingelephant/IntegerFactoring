# F159 manifest

- Date: 2026-08-11
- Current version: V2 corrected proof-only candidate with an exact finite
  certificate
- Durable ledgers: not edited
- Closest result: F158 certified quadratic-lift win--win
- Exact root theorem: a fully scanned fixed quadratic-root layer gives a
  factor, no new root coset, or one common local/global index-two coset
- Compact theorem: a certified common-order cyclic layer is aligned by at
  most two exponent candidates per root
- Odd-order qualification: every root residue is a public power of `g` or
  its public negative, so only its canonical integer encoding can be new
- Exact refinement screen: for a released block `d`,
  `gcd(d^M-1,N)` classifies its membership in the two old local order-`M`
  subgroups
- Corrected boundary: the root theorem does not bound generators released
  by factor-free integer refinement
- Finite certificate: `N=341`, where canonical reduction from the old
  square part `467` to `126` splits `70` into `14*5`, expands the named
  subgroup by global index 15 with local indices 1 and 3, and then gives
  `gcd(14^5-1,341)=11`
- Computation: exact finite arithmetic, a bounded hostile-audit scratch
  search, and a small exhaustive self-check of the post-refinement screen;
  no asymptotic experiment
- Explicit nonclaim: no useful-refinement density, all-input source,
  progress law, recursion bound, or factoring algorithm

## Frozen V1 failure history

V1 incorrectly transferred the root-generated index-two saturation law to
the full F154/F156 feedback layer. Its hostile audit produced an exact
counterexample: canonical integer refinement can release generators outside
the root-generated subgroup.

The original V1 manifest is preserved byte-identically as
`V1_MANIFEST.md`.

- `STATEMENT.md`:
  `053d6deaffaf8343d691b89caaef54b8b8edae34cb652eb95050446e82e70674`
- `PROOF.md`:
  `56062f93e0e78df1ddabae2175e05079b13990b2128bca0c4d381b5b133d8f3c`
- `V1_MANIFEST.md`:
  `64af5e9cac3c325f8fcd6c4d429a113b9671796b49b3f3b0e2003a4b6639b14f`
- `HOSTILE_AUDIT_FAILED.md`:
  `af97aa6aa2224551b969f21dbb107d3a6d986b073fd2582955c8aef2daca288a`

All four frozen V1 artifacts remain byte-identical.

## V2 correction

- `V2_STATEMENT.md`:
  `53584b0152b3eeca7dd37ded6707596ee763e48d7d6c55bb4b335a1ef4c8415f`
- `V2_PROOF.md`:
  `527343a68b58a1331f02566c90c1368b7d747e17716c64e1ec7064fe1dab1918`
- `V2_SELF_AUDIT.md`:
  `204aaaa64fc6a991cb0661f2462673c6a5fca7c50d9a865ababef0ef9a497f62`

V2 keeps the valid V1 root-layer and compact-alignment theorems. It makes
the residue subgroup and the named integer subgroup separate objects. It
adds the exact post-refinement local-membership screen and the complete
`N=341` finite capability certificate. It also records that the odd-order
root residues in that certificate are public powers, so the gain is purely
in their canonical integer representations.

Self-audit passed.

- Fresh hostile re-audit: PASS
- `V2_HOSTILE_REAUDIT.md` SHA-256:
  `2f21fd6f4453d5c05f3e2602c6f6e7dee0f5ba52e73be5821afd268d64fdcf80`
- Independent V2 statement-only reconstruction: PASS
- `V2_BLIND_RECONSTRUCTION.md` SHA-256:
  `35c4ad3c5bf6f4030fb0dff19d885f417e2d1378171f7d9d2d6d5ce4317c3541`
- Review qualification: complete refinement also names `9` and retains the
  old square block `467`, but both lie in `<14,5>` modulo `341`; the stated
  refined subgroup and its local indices are unchanged.
