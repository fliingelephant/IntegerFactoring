# F272 manifest — frozen proof packet

## Status

F272 is a proof-only candidate with an author self-audit. No hostile audit,
blind reconstruction, outside-family audit, human audit, or computation has
run. No durable ledger is edited by this packet.

## Frozen files

| File | SHA-256 |
|---|---|
| `STATEMENT.md` | `103722d5cf46884678867fd093e1ce5bcef9d57a797275c0f0e3c262615d67d0` |
| `PROOF.md` | `687a55e2a64a0fb1190c220d83b69253f7d0aa84d7475cc495ff09e986ee2bcc` |
| `SELF_AUDIT.md` | `54d73eb7048181986fb728c418871e5215ac1d3aa1da2d64dfad76d59414cde1` |
| `PROVENANCE.md` | `48faeb1dc13ccd1edd7c7467a1d0e3bec2297c76c813458868ba4c60f4107c1a` |

These four hashes freeze the mathematical packet. Any later mathematical
change requires a new version and new hashes.

## Exact claims

1. An \(X\)-divisor difference cover obeys the rank-free prime-mass bound
   \(ML>\vartheta_2(X)\).
2. QP cardinality and QP expanded bit length in \(\log X\) are therefore
   impossible, for every rank.
3. QP cardinality and uniform QP explicit prefactor output are impossible
   even for succinct huge values.
4. Fixed-band prime pairs obey the exact incidence inequality (13).
5. The necessary Umans--Wang exponent conditions are
   \(\alpha+2\beta\geq1\) and \(\alpha+\beta\geq1/2\).
6. Static prime-separating banks obey the explicit output bound (21).
7. Rank two and higher remain open at the one-third exponent point; the
   surviving QP-facing seam is a succinct product/refinement evaluator, not
   another explicit GAP cover.

## Exclusions

The packet proves no circuit lower bound, no higher-rank one-third
refutation, no interval-factorial evaluator, no exponent improvement, and
no integer-factoring algorithm.
