# F272 V2 manifest — frozen corrected proof packet

## Status

F272 V2 is an additive corrected proof-only candidate with an author
self-audit. No V2 hostile audit, blind reconstruction, outside-family audit,
human audit, or computation has run. No durable ledger is edited by this
packet.

## Immutable inputs

| V1 artifact | SHA-256 |
|---|---|
| `STATEMENT.md` | `103722d5cf46884678867fd093e1ce5bcef9d57a797275c0f0e3c262615d67d0` |
| `PROOF.md` | `687a55e2a64a0fb1190c220d83b69253f7d0aa84d7475cc495ff09e986ee2bcc` |
| `SELF_AUDIT.md` | `54d73eb7048181986fb728c418871e5215ac1d3aa1da2d64dfad76d59414cde1` |
| `PROVENANCE.md` | `48faeb1dc13ccd1edd7c7467a1d0e3bec2297c76c813458868ba4c60f4107c1a` |
| `MANIFEST.md` | `0c3a6a79173f889a479a395896f70d314a328cd7de08c125b5dca08a9fb619b8` |
| `BLIND_RECONSTRUCTION.md` | `4be8415b7dd33e26a8a75f893b7a89d99d763ad2ce7ee3f0f72fe1f3665c9500` |

## V2 theorem files

| V2 artifact | SHA-256 |
|---|---|
| `V2_STATEMENT.md` | `1b6c52624e5f957b2814f5e3e98572612e7cf9312b167ed117e01dddf0d4abb5` |
| `V2_PROOF.md` | `671c6810a753791fa7c08e3c8eec89b68a0b9fa64fc129d7263130a2b19b67d8` |
| `V2_SELF_AUDIT.md` | `bac1638fd459b0bd3d5b3f8dc0dd022e92a1e50afbcb0ab7cafdfccc3458ada7` |
| `V2_PROVENANCE.md` | `32c5e939f057b9c449b5df6fd1fcdfcadd43d4e66c10fad843d82ec172568616` |

These four hashes freeze the V2 mathematical content. The hash of this
manifest and the immutable-input hashes are recorded in
`V2_FROZEN.sha256`.

## Exact corrections

1. Only \(\alpha+2\beta\geq1\) is saturated at \((1/3,1/3)\).
2. Fixed-machine time lower bounds retain the write-rate constant and use
   \(\Omega\) notation.
3. The interval-product hierarchy is one sufficient interface, not the
   unique surviving route.
4. The interval evaluator is factoring-hard under the proved one-way
   reduction; no reverse reduction or equivalence is claimed.
5. Set/multiset, duplicate, sign, zero, dictionary, and external-citation
   scopes are explicit.

## Exclusions

V2 proves no circuit lower bound, higher-rank one-third refutation,
interval-product evaluator, reverse reduction, equivalence theorem, or
integer-factoring algorithm.
