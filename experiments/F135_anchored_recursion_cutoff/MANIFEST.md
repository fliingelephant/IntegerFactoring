# F135 manifest

## Claim

An unreduced nonzero-digit P121 arm cannot recursively feed its complete new
endpoint back into P121:

\[
z_\ell>N/B,
\qquad
P_N(z_\ell)=P_N(\ell q).
\]

Distinct-digit reciprocal endpoints also inherit the F134 overlap bound.
The same-digit endpoint ledger gives a release/exhaustion/width trichotomy:
either it releases reciprocal-side residual blocks below \(N/B\), the
reciprocal residual is exhausted by anchor powers, or one covered large row
occurs in \(\Omega(n^3/\log n)\) distinct values. An abstract
quasipolynomial forest shows that this stronger multiplicity still does not
force a dependency. A fixed CRT family realizes a selected canonical forest
of depth two, but does not control the growing complete source.

## Relation to prior work in this repository

- P120 separates relation novelty, row reuse, peeling survival, and root
  usefulness.
- P121 forces polynomial multiplicity of covered odd large-prime rows.
- F134 proves the one-star large-prime overlap obstruction.
- F135 locates the next recursive gate: endpoint release, cross-star or old
  overlap, or wrapped/powered feedback. It does not weaken the positive P121
  theorem and does not close the feedback route.

## Files and hashes

The hashes below cover the frozen theorem and proof. The manifest omits its
own hash to avoid self-reference.

| File | SHA-256 | Role |
|---|---|---|
| STATEMENT.md | b03002c70c97e38506f6e0c4fc4585e4e5268ec59c2b3557f8f3600dd837ef02 | Exact cutoff, release trichotomy, abstract forest, selected CRT family, and scope |
| PROOF.md | 646e667edea22eb586cf069c6efdfdd8198132e00372d47e7ae882208d91a7a2 | Proofs, constants, CRT construction, and arithmetic verification |
| HOSTILE_REAUDIT_V3.md | d0c7c8a0a3192be884d92e644f824bacdc7f769ec26f3c66844254bebe000870 | Passing hostile re-audit of the corrected frozen theorem and proof |
| BLIND_RECONSTRUCTION_V4.md | a24cc841627f0abfa9192f5d6a58b6b4bcdfcf0d090b54a0a16704cc78c1b5bc | Passing statement-only independent reconstruction |

## Evidence class

Proof only. No broad computation, corpus search, or hidden-factor search is
registered as evidence. The CRT family is proved from exact congruences and
primes in fixed arithmetic progressions.

The frozen first version failed both hostile audit and blind reconstruction.
The second frozen version failed a new hostile re-audit. All failure records
are preserved. The corrected frozen version passed a fresh hostile re-audit
and a fresh statement-only blind reconstruction. It is eligible for narrow
promotion. It is not a closure theorem, a complete-source obstruction, or a
factoring algorithm.
