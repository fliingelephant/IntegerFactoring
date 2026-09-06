# F139 manifest

## Outcome

Value-dependent multi-block packing has one exact positive effect. If a
public word \(q<N/B\) contains several large odd rows, then all but at most
\(|\mathcal R_B(q)|\) occupied nonzero carry digits preserve all those rows
simultaneously. With two rows globally private to different owners in the
full old ledger, every such common-good value is also safe from global exact-
value deduplication.

The source operation is public and quasipolynomial conditional on a product
\(q<N/B\) existing. No theorem forces even two qualifying blocks to fit.

Simultaneous preservation does not force a rank defect. An abstract
multi-parent peelable incidence system remains full rank. The registered selected canonical
certificate at \(N=989\) packs rows \(11,17\), passes the packed base screen
and every integer-anchor screen through \(B=5\), preserves both rows in all
three nonzero digits, and still gives a rank-six, zero-kernel parity matrix
that peels completely.

The two rows are degree one only in the registered frozen two-column selected
ledger. The certificate makes no degree claim about the complete F26-Q
ledger or complete canonical universe. It is not a complete-source
obstruction or a factoring result.

## Candidate hashes after the first hostile-audit repair

| File | SHA-256 |
|---|---|
| `STATEMENT.md` | `a01cd50a749a61d70aefac9b50fca91e4a87332ef882c343fccc07009b75f27b` |
| `PROOF.md` | `8a41448676a1df5850fe90cc144bbca23a0513a36b9ac7e974a6b5de80de1a60` |
| `PREREGISTRATION.md` | `00f6a456d2e8207a31a91c32a9de0894fb9c11be9da2a0cd9f0207d4a87ac3c0` |
| `PRE_RUN_PINS.md` | `858e7694f115cecd84aba80ee19e076dc725456e86ae0de6e2f69bd460744510` |
| `verify.sage` | `d0cb52305d9ab1f75ec02f4b67fcbc1fae520b6dc424175aac077dbb940ea376` |
| `OUTPUT.json` | `4cda0f1af6adf29f73fc7e5f0d0d74f85ca4b331c02e8cbabe61b97a7c0778ba` |
| `RUN.log` | `4cda0f1af6adf29f73fc7e5f0d0d74f85ca4b331c02e8cbabe61b97a7c0778ba` |

The authoritative output has status `PASS`; every named check is true.

## Preserved failed certificate

The first selected witness at \(N=667\) was invalidated before freeze. Its
packed word has

\[
\gcd(133+331,667)=29.
\]

The original preregistration omitted that base screen. Its arithmetically
passing output therefore does not test the intended no-factor branch.

| File | SHA-256 |
|---|---|
| `EXPLORATORY_SEARCH_NOTE.md` | `6a039862b516ada639a265c468815bd90004f5cb20bd1f826b7c6a989174bc3c` |
| `FAILED_CERTIFICATE_667.md` | `e53d29d8d65975e2078639fd31045c6a1521e3bcef0b75056efd9254c0677a63` |
| `PREREGISTRATION_667_FAILED.md` | `80db48b2d87ccbdfe2d9661d89a0af97fb9769e55809c66d6122dd04c34a0ae7` |
| `verify_667_failed.sage` | `c3505d410cc2b8fb5af4f775bd18b43e3befdfff768a0b8df51c0057e1e9636f` |
| `OUTPUT_667_FAILED_SCOPE.json` | `0d970ec25d509a310dfc2a26295933e16427692419f9a61fb0c48c918a464a30` |
| `FAILED_RUNS_667.md` | `865f14f84a5642c79c7abc879adebb8f39fab4f45132dfd9eecd679665602d13` |

The two output-only JSON serialization failures from the rejected run and all
of their revision pins remain in the directory. Sage-generated `.sage.py`
files are execution by-products and are not evidence.

## Audit status

The first hostile audit preserved two local statement defects in
`HOSTILE_AUDIT_FAILED.md`: the anchor eligibility condition was undefined,
and one displayed sum lacked its TeX backslash. Both defects are repaired in
the current statement. The fresh hostile re-audit passed. The first blind
reconstruction then passed every theorem and certificate, with two
terminology qualifications: define \(\iota_N\) locally and avoid using
“hyperforest” in the Berge-incidence sense. The current statement and proof
make only those wording repairs. They await a fresh hostile re-audit and
statement-only reconstruction. The final hostile re-audit passed; the fresh
blind reconstruction also passed. The result is promoted as P127/C132/X78.
It has not passed a cross-family audit, a human audit, or a publication-level
literature review.

| Review artifact | SHA-256 |
|---|---|
| `HOSTILE_AUDIT_FAILED.md` | `489219eb892a494657567db76576548231932d2a02e28fa70cf3c6da7b9c176c` |
| `HOSTILE_REAUDIT.md` | `d5ac87c39e8f9c54b2ec458ee2219fe7aee308916aadf3dba38953cf4b7c4693` |
| `BLIND_RECONSTRUCTION.md` | `7439660188994eedb47ef21a230dab2bb34b95d2af01b3890ac3155e2ae0f80c` |
| `HOSTILE_REAUDIT_V2.md` | `c8495d43e50ed83400ea6956116ccc2f242478ae7b52caf0ca2fa63f68f31a9c` |
| `BLIND_RECONSTRUCTION_V2.md` | `d4c85ce6a31bbfefb4815a757a8c2daf312f9109e4b4ae7be439a687b48192ff` |
