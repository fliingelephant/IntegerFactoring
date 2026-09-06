# F166 final manifest

## Outcome

- Promoted result: `P150`
- Progress entry: `C157`
- Classification: exact proof-only refinement of F161/P148
- Main result: hidden-log alignment is not needed to construct the next
  certified common-order state after an F161 common return.
- Boundary: alignment is still needed for its extra factor channel, global
  subgroup equality, exact relation rows, and F164 rank-volume accounting.
- No source theorem and no factoring algorithm are claimed.

## Frozen candidate files

- `STATEMENT.md`:
  `5b245ddc902f300b89dab11c61d06dfffb2deef09d01182f4f8e6f7cce608615`
- `PROOF.md`:
  `bba045350ed11b8756d11c233d909f4f14a0225b19b5d7bab74296ced04ec4a6`
- `MANIFEST.md`:
  `dcf533a603c5d94124f33bfb4d1dbeb62e45b023ccd423e9c6f316e4b1b8b116`

## Review chain

- The first `HOSTILE_AUDIT.md` has SHA-256
  `95fa74a0cee818b28fd333f273d2cc4befc7f3e6c9d47c9afab23841ea91bc83`.
  It reached the correct mathematical verdict, but it included an
  unregistered finite check and is not used as evidence.
- `HOSTILE_AUDIT_FAILED.md` preserves that workflow failure with SHA-256
  `b4159cabb3392ee363494083171205f3a2ae943be227c18878600483406bf4b9`.
- The fresh proof-only `V2_HOSTILE_AUDIT.md` passed with SHA-256
  `f97e6bc0bd80c7ee19b0d83a951e8de716e7055db5261c0e45b4d2190659c1fe`.
- The independent statement-only `BLIND_RECONSTRUCTION.md` proved the
  result with SHA-256
  `756275ebc55c14df7b091edfbd5e4c32afa26c585c978684f7f70111fd2304ce`.

The blind reconstruction notes two harmless wording qualifications. The
screen `gcd(m,N)` is redundant under the exact F161 inputs. Smoothness is
inherited from the incoming F161 state; known factorization and the
quasipolynomial cost do not depend on that wording.

No computation is used as mathematical evidence for promotion. No
prior-art novelty review or human audit has run.
