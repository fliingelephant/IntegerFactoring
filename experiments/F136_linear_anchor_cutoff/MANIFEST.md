# F136 manifest

## Claim

The elementary primorial bound already supports a linear anchor cutoff
\(B=\lceil12n\rceil\). Every odd row above \(B\) in every unit block below
\(N/B\) is forced to lose privacy. The same-digit presentation source either
releases a new reciprocal-side residual block below \(N/B\), exhausts that
residual, or creates \(\Omega(n/\log n)\) distinct columns on each covered
row. Composition with the earlier all-block source is now stated as an
explicit conditional corollary.

## Relation to prior work

- P121 proves a stronger multiplicity bound at the smaller block region
  \(q<N/n^3\).
- P122 blocks within-star sharing of unrelated fresh large rows.
- F135 proves the endpoint recursion cutoff and expanding-forest boundary.
- F136 widens the positive row-reuse region. It does not solve closure.

## Candidate files after the blind-scope clarification

| File | SHA-256 | Role |
|---|---|---|
| STATEMENT.md | e17c70e87c87d0893814ffb503f636087e60a373e31e06659ef524d1f8561c49 | Self-contained arithmetic theorem and conditional composition statement |
| PROOF.md | ecb2a92c7c382473ec0466f8dc544d7118e6ac160f927df9e7d0e31f11eb0655 | Elementary proof and corrected explicit conditional cost argument |

The first passing hostile audit and the failed blind reconstruction apply to
the earlier statement/proof hashes recorded inside those reports. Their
SHA-256 hashes are
`f3c15a327f5bc52ad391e167b4ebd3b96723467000595ad955847572ece4259f`
and
`f61d9ec1056565c44960166c8d1d9369f26762f42c205938df96804c635d34a3`.
The first hostile re-audit of the self-contained version found one false
monotonic-gap sentence. Its preserved report has SHA-256
`6f972b9db8094bc6210bc92aab7e0b8055ad22f4f0ed0616234cdf8eb682b2c9`.

## Evidence class

Proof only. The rational inequality at \(x=2^{18}\) was checked exactly, but
no empirical or hidden-factor search is used as evidence.

The first frozen version passed hostile audit but failed strict blind
reconstruction because its algorithmic terms and imported cost theorem were
not self-contained. The first re-audit of the self-contained version then
found one false proof sentence while confirming the theorem. Both failures
are preserved. The second strict blind reconstruction passed in the intended
large-input regime and requested two explicit conventions: the empty bucket
product and the inherited threshold on the width inequality. The current
statement adds only those conventions. The final hostile re-audit and fresh
statement-only reconstruction both passed.

| Final review | SHA-256 |
|---|---|
| `HOSTILE_REAUDIT_V3.md` | `2890e4c66634f110778e6828860704182f9286c3bda08d17641a4cdfe6db4b6d` |
| `BLIND_RECONSTRUCTION_V3.md` | `c8d55ef91e7f5de000541e94414ea9fd774dadaca213f80750fe9bfc73bd434f` |

## Final status

Promoted as P126/C131. No cross-family audit, human audit, or
publication-level literature review has run. The result is a source-side
row-reuse theorem and a conditional composition statement. It is not a
rank-closure theorem, a normalized-root theorem, or a factoring algorithm.
