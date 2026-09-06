# F134 manifest

## Claim

One anchored star has an exact overlap obstruction:

\[
\gcd(w+NA_i,w+NA_j)\le B
\qquad(i\ne j).
\]

Thus different arms cannot share a prime larger than the carry range. In the
even star kernel, every selected arm must have a \(B\)-smooth squarefree
kernel. The full star kernel has at most one additional odd anchor coset.

This is a pruning theorem only. It does not close retained or multi-round
feedback. The exact certificates show all relevant boundaries:

- \(N=25\): the odd anchor coset can evade smoothness and give global root
  \(-1\);
- \(N=143\): one nonsmooth nonzero-carry arm closes usefully against an old
  retained relation;
- \(N=49\): a row private in one star becomes an anchor in the next round.

## Relation to prior work in this repository

- P117 gives the cross-layer quotient and relative-root accounting.
- P120 separates row reuse, 2-core survival, and root usefulness.
- F133 forces old-row reuse under its small-block and anchor-product
  hypotheses.
- F134 analyzes the fresh rows inside the resulting fixed anchored star. It
  does not replace or strengthen the F133 source theorem.

## Files and hashes

| File | SHA-256 | Role |
|---|---|---|
| STATEMENT.md | 40354e169ef8632c206bd653819b3d0d117c670f134e18ff2f4558bc191c9483 | Exact theorem, three certificates, and scope |
| PROOF.md | ca9fb0dc855fb032258908854e20f85da9851ba0777a5461382438f2839e5f3a | Proof and exact arithmetic verification |
| HOSTILE_AUDIT.md | 1f434232f2bb2f2658a693d59552c3ae6d0f5b33f3bb35071a65d6db94a79ef9 | Independent hostile audit and strict fresh-cofactor scope |
| BLIND_RECONSTRUCTION.md | b0419abf326a4d590edbd05c13ce500e3f76c88751cba6b2790d5a16cf59ad34 | Independent reconstruction from the statement alone |

The manifest omits its own hash to avoid self-reference.

## Evidence class

Promoted after a passing hostile audit and an independent proof-blind
reconstruction. No empirical or hidden-factor search is registered as
evidence. The displayed arithmetic certificates were independently
re-evaluated.

The overlap theorem concerns the fresh cofactors `H_i`, not the full values
`P_i=qH_i`. Certificates A and C belong to the broader exact-value/all-block
model; they are not literal small-prime F133 arms. Certificate B becomes a
literal arm with anchor 3, but its useful closure is cross-layer. No
cross-family audit, human audit, or publication-level literature review has
run.
