# F156 manifest

- Date: 2026-08-11
- Type: proof-only source-and-cost candidate
- Computation: none
- Durable ledgers: not edited
- Closest results: P118, P120, P138, F154
- Main change: sparse combinations of relation-basis lifts, not sparse words
  in named integer blocks
- Cost: deterministic \(2^{O((\log n)^6)}\)
- Recursion control: feedback-ledger relations never enter a later section
  basis
- Exact nonclaim: no all-input direct-screen, refinement, rank, or
  non-global-root law
- Review status: V2 passed a fresh hostile re-audit and an independent
  statement-only reconstruction

## Version history

### V1 — frozen source and reviews

- `STATEMENT.md` SHA-256:
  `d426df6c293fd835c85260b14fb6ddd57a99ff812a4c7b9a74b084318ed34527`
- `PROOF.md` SHA-256:
  `4024a5d8732ffec5dea0711498bf77e0accfc079868fecc82ace56c91243169d`
- `HOSTILE_AUDIT.md` SHA-256:
  `ae02391b77c67856bea5c46bb0629c1ba9212d5fa94065b02406e295e59d20b8`
- `BLIND_RECONSTRUCTION.md` SHA-256:
  `519966e69e08d9a5692427e4641530fd3d38d67f28fee9c99d36c297404e0d5c`
- V1 files and reviews remain byte-identical.

### V2 — minimal identity repair

- Change: state that the nonempty scan enumerates every nonzero section
  vector. The omitted identity has `v=0`, `z=w=1`, and is inert for direct
  screens, endpoint refinement, exact-value retention, and the F154
  refinement channel.
- Stage order: complete the ordinary frozen P118 scan, then the section scan,
  then apply one joint refinement.
- Algebra, complexity, source grammar, and nonclaim scope are unchanged.
- `V2_STATEMENT.md` SHA-256:
  `71b640469c0f57440d8e290b63af411eb33ee08b08c814413b5a04fff1c7d3dc`
- `V2_PROOF.md` SHA-256:
  `37e80fc0600eeb5a178f9e31c1f68f17b29ba3ed8837dcb5e391be0d6e5ef685`
- `V2_HOSTILE_REAUDIT.md` SHA-256:
  `5c5edb2f48f851c71cdb4656cc8aed71004c6ec011286bc1b4d809ce96034c96`
- `V2_BLIND_RECONSTRUCTION.md` SHA-256:
  `19691cfefa8e718b96befe20220f57fd8fdcde1d2a2340368d5739be423a58d3`
- V2 is the promoted version. It proves a deterministic
  `2^{O((log n)^6)}` source construction and no universal success law.
