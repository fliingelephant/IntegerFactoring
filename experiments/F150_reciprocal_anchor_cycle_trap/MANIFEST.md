# F150 manifest — reciprocal-anchor containment-cycle trap

## Type and history

Proof-only candidate. No research computation was used.

The original statement and proof were frozen, then failed their first
hostile audit on two domain defects. They remain preserved without edits.
The narrow V2 repair is in `V2_STATEMENT.md` and `V2_PROOF.md`.

## Closest results and material difference

- P129 gives the general bridge-cycle rank and normalized-root gate.
- P130 classifies formal squared-action cycles and root-1 commutation
  diamonds.
- P131 gives the square-root-scale lower bound for wrapped positive cycles.
- F150 isolates positive reciprocal-anchor two-cycles, proves that their two
  residuals must be the same exact integer, and proves that their normalized
  root is always \(+1\).

## Claims

1. Every legal positive two-cycle whose anchors are the opposite centers has
   synchronized residuals.
2. Its two P128 bridge values have an exact square product.
3. Its normalized root is global \(+1\).
4. On the odd branch, the public selector \(q=\lceil N/a\rceil\) for an
   integer \(a\) with \(1<a<\sqrt N\) either finds a divisor immediately
   or constructs this decoy cycle.

V2 restricts the trap theorem to the odd branch after the ordinary parity
screen, requires integer \(a\), uses the established P128/P131 normalized-
root orientation, and states the exact scope of first-occurrence deletion.

## Exclusions

No claim is made for nonreciprocal anchors, cycles of length at least three,
hypercycles through old columns, signed presentations, or branches already
resolved by parity, endpoint-gcd, or sign screens.

## Verification state

The original frozen candidate failed its hostile audit. V2 passed a fresh
hostile re-audit and a fresh statement-only blind reconstruction. It is
promoted as P137.

## Exact artifact hashes

Original frozen artifacts:

- `STATEMENT.md`:
  `485396a4df33ab8b708b35de12f018489f942e783f1d680c3c4c2bccb6c23435`;
- `PROOF.md`:
  `a9d94ec57fae30ae4a6e0084d9558dfc52721f1e5607af38a201dedc6ec5cd68`;
- original pre-audit `MANIFEST.md`:
  `e272cfaf1e8482629c76779d83c46bed5880735789dff1c690aa38dc6741bb67`;
- `HOSTILE_AUDIT_FAILED.md`:
  `3405daaec86ca8853c1b4441b5e3514e25e05caeb5c8f66b23cd7ef6404f55e0`.

Narrow V2 repair:

- `V2_STATEMENT.md`:
  `04725f9125976998d482663774cfcd11a17f215c953bc81be701bad6e318d7ee`;
- `V2_PROOF.md`:
  `5afe0be2bf8526064b421384c27452fc393f88cc88cd47a07e52f7cb3a03ec66`.
- `V2_HOSTILE_REAUDIT.md`:
  `7563e1680eb7facebbd2b1be75dcc8205f40a300435d6bc89c3ab4d154a0451b`;
- `V2_BLIND_RECONSTRUCTION.md`:
  `c6ab916b5381eee61f36d52b520f65e88b6650fa584659410e3baf30e397e996`.
