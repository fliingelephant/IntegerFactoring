# F273 V2 manifest — frozen additive correction

## Status

F273 V2 is an additive corrected proof-only candidate with an author
self-audit. Fresh V2 hostile and strict V2 statement-only audits are
pending. No outside-family or human audit has run.

No source code, compilation, benchmark, local research computation, remote
computation, cohort, dataset, or empirical result belongs to V2. No durable
ledger was edited.

## Immutable V1 artifacts and audits

| V1 artifact | SHA-256 |
|---|---|
| STATEMENT.md | cdc099e0a74b5d2510ac4d9b88cf965f0ef797e6bcc428ac855c3f74daec5079 |
| PROOF.md | 09978512f2e66768628df481380e059e3d6c90fc0010e5007db249322b723dc2 |
| SELF_AUDIT.md | 66218b417fa92037526d4d7b9b40a06638fd7ae7f578d5ec3176d886039a49dd |
| PROVENANCE.md | 4595033097f3b66b3b1a12e4fce1dc339bf58fbc8f1e31bcbd40cf21c34a784c |
| MANIFEST.md | 2b33fdd0d8921bccf613ef360e92dd7a604b06133de09bf8c91d944678e41786 |
| FROZEN.sha256 | bbfce77ead51db2d540d665ed620840894a317f1c96102c62a5ef8315e6df88c |
| HOSTILE_AUDIT.md | a8ff865f43d29e5af1c8956bd2c1bcb65fbf53f97339da024db4e8f2a35e0cb6 |
| BLIND_RECONSTRUCTION.md | 9bc7775fd05ec20c9f78923043857504a5795fef03966893d16535ae7a50cda9 |

The V1 hostile audit passed. The V1 blind reconstruction failed as written.
V2 preserves both records.

## Frozen V2 mathematical artifacts

| V2 artifact | SHA-256 |
|---|---|
| V2_STATEMENT.md | 95cf55e02dd02322de2c78f95dfa6ddecae7c783fd152f7c00a64de511bf96b4 |
| V2_PROOF.md | a91f2cdf97c26ac95010594383a299c3450527b98c8219638bef02d98ce28d99 |
| V2_SELF_AUDIT.md | 7bd76f3914495df1684564b69744a5b9a66a2ecfc332edd92398d3f9f7ac13b8 |
| V2_PROVENANCE.md | 13a4be4ef7772ba1230a4847cd6c938c1c711a2c8cad53a1f0b71712456613c5 |

These four hashes freeze the V2 mathematical content. The hash of this
manifest and all five V2 file hashes are recorded in V2_FROZEN.sha256.

## Exact corrections

1. V2 distinguishes the last diagonal determinantal divisor
   \(\Delta_B=B!\) from the last Smith invariant
   \(d_B=\operatorname{lcm}(1,\ldots,B)\).
2. It proves
   \(\Delta_{B-1}=B!/\operatorname{lcm}(1,\ldots,B)\).
3. It states that both \(\Delta_B\) and \(d_B\) have gcd \(p\) with the
   balanced semiprime, while proving no evaluation reduction between them.
4. V2 distinguishes the exact base-frontier count
   \(2^{t+1}-1\) from the complete memoized cross-resultant DAG count
   \(2^{t+2}-t-3\).
5. It propagates the exact distinction through standalone
   cross-resultants and the full literal discriminant/resultant DAG.

## Retained theorem contents

V2 also retains the proved child-zero ideal, independent-leaf dependency,
rank-defect, discriminant, superfactorial, cross-resultant recurrence,
telescoping, balanced-gcd, and literal asymptotic resource statements.

## Exact exclusions

V2 proves no general circuit lower bound, interval-product evaluator lower
bound, affine-identity lower bound, characteristic-specific lower bound,
succinct-matrix lower bound, equivalence of the diagonal factorial and lcm
gates, numerical-quasipolynomial evaluator, integer-factoring algorithm, or
empirical claim.

Any mathematical change to a V2 theorem file requires a new version, new
hashes, and fresh audits.
