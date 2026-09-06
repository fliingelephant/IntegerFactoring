# F267 manifest — frozen proof packet

## Status

F267 is frozen as a proof-only boundary-collapse theorem derived from the
authenticated F263-D02 V2 result. It contains no new production search or
empirical claim. Fresh hostile and strict statement-only audits are pending.

## Frozen artifacts

| Artifact | SHA-256 |
|---|---|
| `STATEMENT.md` | `feff0a8b5dfd254cba265c9378106520c4fed718bbff3d507112c59a367045ee` |
| `PROOF.md` | `f6e95ae5d8a27828cfd4802cdc587f2bba2b2e94d50f523d42b559ef14e4fac3` |
| `SELF_AUDIT.md` | `55ca0cc6fa901b62d63faec38256812e8e4fd0cb88a352ee59a5ce405e561893` |

Any mathematical change to these files requires a new version and new
hashes.

## Exact contents

The packet proves:

1. closed integer formulas for F263's shifted `u1`, `v1`, `jet_det02`,
   `transfer_f0`, `transfer_r0`, and `transfer_det01` candidates;
2. four reflection mechanisms at the left and right public query edges;
3. the exact near-square rigidity implication
   `s^2<p => q-p=2(s+1)`;
4. one-Fermat-trial factorization under that implication;
5. direct public-offset domination of the same boundary mechanisms without
   the small-offset condition; and
6. exact correspondence between the four mechanisms and all six finite
   non-direct `s` sets in the authenticated F263 held-out result.

## Exclusions

The packet does not prove:

- a converse classification of zeros of any candidate;
- exhaustive coverage outside the frozen F263 query bank;
- a lower bound or a numerical-quasipolynomial block evaluator;
- an impossibility theorem for other symbolic grammars; or
- an all-input factoring algorithm.

## F263 provenance

The finite pattern statements are tied to these existing authenticated
artifacts:

| Artifact | SHA-256 |
|---|---|
| `../F263_hypergeometric_evaluator_symbolic_search/V2_FROZEN.sha256` | `2a41fb0ca76955522843fdc0b15c69b1b2d811a3ac79021b0518bf6da9224271` |
| `../F263_hypergeometric_evaluator_symbolic_search/V2_symbolic_search.cpp` | `05c0b87a453eb3c2c40c01bf058b0559a6ff2e9b943d16ddcf68d147b1f4c827` |
| `../F263_hypergeometric_evaluator_symbolic_search/V2_RESULT_AUDIT.md` | `320427df65f9d45f63cfaf4ad93194fe7e09cc499b4bd6d86b9a5ad7fb92b976` |
| `../F263_hypergeometric_evaluator_symbolic_search/V2_REMOTE_RUN/output/F263-D02.heldout.rows.tsv` | `58b1e1ebde26af9ccdca43449fafff6d1737c932ceb2c3f9849571919c0f10a1` |
| `../F263_hypergeometric_evaluator_symbolic_search/V2_REMOTE_RUN/output/F263-D02.heldout.summary.json` | `95bb89d57c6a45cc964c70ec57db7c95f8fc5e0dfcd96d5e3df4c005559f46cb` |

## Methods

The proof uses rising-factorial reflection, division-free telescoping of
upper-triangular transfer products, the two inequalities defining
`floor(sqrt(N))`, parity of an odd-prime gap, and the first Fermat
difference-of-squares trial. The proof does not depend on any unrecorded
numerical check.
