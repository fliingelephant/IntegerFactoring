# F157-D01 V2 manifest

- Date: 2026-08-11
- Version: V2 narrow claim-boundary correction
- Status: frozen for fresh independent hostile re-audit
- Computation: no new experiment run; V2 reuses the frozen V1 evidence
- Durable ledgers: not edited
- Arithmetic change: none
- Scope correction: exhaustive public support-two enumeration is already the
  F156 quasipolynomial locator; disclosed factors only accelerate the
  registered finite run
- Remaining theory: an all-input success or progress law and useful-pair
  density
- Remaining implementation problem: a public selector substantially faster
  than exhaustive enumeration
- Exact nonclaim: no all-input success, density, polynomial-time factoring,
  or 900-second public exhaustive replay claim

## Frozen V1 evidence

The original `MANIFEST.md` remains byte-identical. `V1_MANIFEST.md` is a
byte-identical archival copy.

| V1 file | SHA-256 | Role |
|---|---|---|
| `DESIGN.md` | `7f9d7504bd285b6b32497f783d8a9f28609373e73437030e03bcd54877e6ec10` | preregistered design |
| `FAILED_RUNS.md` | `b3baf7db5c2ae7fee6d5db75b9666394d8d02f45cc553566ea81cb17b5fecb75` | preregistered failure history |
| `INPUT.json` | `ca227228ed692e3895b0f4d4407b14b5000c0f0ec4134aff394b211791cb2009` | preregistered corpus and pins |
| `QUESTION.md` | `d8790ab6a23597b28b949405547f4cfd8d1187602fcf1f2ad591439022a53f56` | preregistered question |
| `run_with_timeout.py` | `560096b0689690f082e7eabd8c8cbb6d955f83da79fa05003f535f5f510b8999` | preregistered 900-second runner |
| `search.py` | `1f9bf511a8a0d5783dfcbca891d7e4022e158382395b3925cb38241ee2d6cb69` | preregistered source |
| `REGISTRATION.json` | `0c056554d8e0a5fcfe8ff7b2d2149936daaef6f3f1a6fb56c71d2712d4d7f6b5` | machine-readable registration |
| `OUTPUT.json` | `f07dc61d14a1f3ba16d980796529e7a06794d3b4b296481f12eca8270e151e29` | authoritative output |
| `RUN.log` | `97db534706b7e074843270548d0535368f22eaa784f227f0def711dc8f7f356a` | authoritative run log |
| `RESULT.md` | `48914a43303d61f70a69afbc7eca5679c64267ebb25d4b8f5418ec4c96e02904` | frozen V1 result; scope failed |
| `MANIFEST.md` | `e14072aa78d0922480bf097e91884f8f5c774e9d8f8375250bb4ca59c435ebc2` | frozen original V1 manifest |
| `V1_MANIFEST.md` | `e14072aa78d0922480bf097e91884f8f5c774e9d8f8375250bb4ca59c435ebc2` | byte-identical V1 manifest archive |

All registered V1 arithmetic artifacts remain byte-identical. V2 does not
replace or reinterpret an arithmetic field in `OUTPUT.json`.

## Frozen upstream pins

| Pin | SHA-256 |
|---|---|
| `F111_RECONSTRUCT_INPUT.json` | `8622024473bd602d1d4928fad959099db1ae463e9bd736b7b6ec59fbb99c3f61` |
| `F111_RECONSTRUCT_LAYER_decoder_v1.py` | `b8435179093f9121d7ab9ca6c5949e7816351c34cc85d4973cbc65bae6ae80f8` |
| `F111_RECONSTRUCT_LAYER_decoder_v2.py` | `12a24643fa9df6b8ad03106d9a562b823b4029223cf2a26f1c5e75ab23f6f3e2` |
| `F118_OUTPUT.json` | `6c8571ef2e851d5cec1c31314887f35932a22ef1de10dcff7e7b40a0cfa572bf` |
| `F118_scan_full_source.py` | `07be2d7b124fc4470de568b559a7918d0111802c69d2cfbe144fdccbcb7ec75c` |
| `F156_PROOF.md` | `4024a5d8732ffec5dea0711498bf77e0accfc079868fecc82ace56c91243169d` |
| `F156_STATEMENT.md` | `d426df6c293fd835c85260b14fb6ddd57a99ff812a4c7b9a74b084318ed34527` |

## Frozen V1 hostile-audit failure

The V1 hostile audit passed all integrity, replay, certificate, aggregate,
and factor-assisted index checks. It failed the artifact as written because
`RESULT.md` denied a public quasipolynomial locator that the pinned F156
source already supplies.

The original report remains byte-identical. The canonical failed-history
name is a byte-identical archival copy.

| Failure-history file | SHA-256 |
|---|---|
| `HOSTILE_AUDIT.md` | `e897bc1ead3989703f1b9d9d1e46e5fec91194ffdfe751891cd41d8803683b5e` |
| `HOSTILE_AUDIT_FAILED.md` | `e897bc1ead3989703f1b9d9d1e46e5fec91194ffdfe751891cd41d8803683b5e` |

V1's exact failure was limited to two claim-boundary sentences. It did not
invalidate the 65 positive certificates, the four finite nulls, the
no-false-candidate result, or any registered count.

## Frozen V2 correction

| V2 file | SHA-256 |
|---|---|
| `V2_RESULT.md` | `a6278bc71959396e7dbb745c2dbce18f2a4c1df0fffc5c8b5cd09c9daf87b3d4` |

`V2_RESULT.md` preserves every V1 arithmetic and count claim. It makes four
precise corrections and qualifications:

1. The public F156 source already enumerates every support-two pair because
   `D=L^2=36` on all five fixed inputs.
2. The exhaustive public pair scan remains quasipolynomial because the
   public basis has quasipolynomial size.
3. The disclosed factors are an acceleration for the registered 900-second
   classification. They are not necessary for public quasipolynomial
   location on the fixed positive input.
4. What remains open is an all-input success or progress theorem, a density
   law, and a practical public selector substantially faster than exhaustive
   enumeration.

No V2 statement says that exhaustive public enumeration completes in 900
seconds. No V2 statement promotes the fixed positive certificate to an
all-input factoring result.

## Fresh-review boundary

V2 awaits a fresh independent hostile re-audit. The re-audit must treat
`V2_RESULT.md` as the corrected claim surface and must use the frozen V1
arithmetic artifacts as its evidence. It must also retain
`HOSTILE_AUDIT_FAILED.md` as failure history.

This manifest does not hash itself. Its SHA-256 is supplied externally at
freeze time for the fresh reviewer.
