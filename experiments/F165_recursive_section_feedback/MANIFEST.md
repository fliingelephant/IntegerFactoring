# F165-D01 manifest

## Status

The sole preregistered authoritative run passed. The level-two-only target was
not found. The finite state-growth observations are candidate evidence. The
fixed-depth cost theorem is a proof-only candidate. Neither has entered the
verification cadence.

## Frozen registration

- `REGISTRATION.json`:
  `b3bbfc3e8f3acf45c9adc66a0c2444312b4ce279d001e73d5e415f495844fd22`
- Pre-run `FAILED_RUNS.md` hash pinned by the registration:
  `ed44de769f8b53361768ea1199d9c3ba610d7cb5e2e3dffb0ef0b1bdb63a5ca8`
- Post-run `FAILED_RUNS.md` records that there were no failures. Its current
  hash is listed below.
- The corpus rule was frozen by the local source hash and registration
  parameters. The pre-run corpus hash field was deliberately `null`, so no
  corpus-generation program ran before the authoritative workflow. The
  authoritative corpus hash is
  `bd1d2987d2eaa6d3cfda3fceea72fbd471592a659137df26ae05a3d86cec7fb3`.

## Current file hashes

| File | SHA-256 |
|---|---|
| `QUESTION.md` | `45b42964446c5103c6bb1d81992451a7d4a21f2a8c4f7b7bc62bd03150ca4805` |
| `DESIGN.md` | `ea115dfa9b1a49e5371f758f91743278f02bc6a5d6ec7316c49db18bdad5ef57` |
| `FAILED_RUNS.md` | `106807965c5320841746cc200c1b552d6f96e3cac4e8349a0b99372d252b3f60` |
| `search.py` | `2a7852f8438003f0db1dd49b7721d02ae2c1cfcea8b114f1e58cc69b74f04427` |
| `run_with_timeout.py` | `5530b2604cf3e4029fb8afbd8c72711a0558a5739727cd166b12dd931c4c26ea` |
| `REGISTRATION.json` | `b3bbfc3e8f3acf45c9adc66a0c2444312b4ce279d001e73d5e415f495844fd22` |
| `OUTPUT.json` | `94ca36ee995819d384e260d50213105b58c3b91377b3a8e51ba155fa7b218dcc` |
| `RUN.log` | `4a71dda9953162013810938b0c41556aff6988b44b592e546bddaf78d4b90c9f` |
| `RESULT.md` | `04ff14f6f0664073565c36370308c610569518f84fbd005b8ad3f835edd717d3` |
| `COST_THEOREM.md` | `af7a30f062a178e4f4a77a6c41f552de0ef3817e542395907ef074857777f995` |

## Upstream pins

The registration pins `PROMPT.md`, both F152 V2 interface files, both F156
V2 interface files, and the reused F157 factor-free decoder source. The
authoritative workflow checked these hashes before the corpus scan.

## Evidence boundary

- Public analysis receives only `N`.
- Public candidate selection uses no factor of `N`.
- Disclosed `p,q` classify public divisors only after analysis.
- Every reported positive certificate passed an N-only replay.
- No finite observation is presented as an all-input theorem.
