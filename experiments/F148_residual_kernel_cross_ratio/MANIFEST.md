# F148 manifest — residual-kernel cross-ratio closure

## Final status

Promoted proof-only result. The V3 registered finite certificate passed the
local replay. The frozen statement then passed an independent hostile audit
and a statement-only blind reconstruction. This is a conditional decoder and
source target, not a factoring algorithm.

## Frozen candidate

- `STATEMENT.md`
  `8d790d05d8161444684d109ad16c3cc1f2be453dcc04638a8d8a10406b78cc35`
- `PROOF.md`
  `92542fe2f91fbdb26311112bef799f0f0f7d02d22ca161b34d1ca2fcf082e405`

## V3 registered computation

- `V3_PREREGISTRATION.md`
  `b4763cb8971062fe11536f5c43242b93ab565bfb10f4838003a3876121e3fc78`
- `search_v3.py`
  `8ab73be57082ff5f0bedf47cb23d41991f120987d01a1af79776fff5a0ac3f0a`
- `V3_OUTPUT.json`
  `e00b51b16aadd378abe33b4f6c3a57e49e9983e0a1c6a9086b8e6c856571e379`

The replay returned the pinned `N=745` certificate. `git diff --check`
passed for the artifact folder.

## Independent reviews

- `HOSTILE_AUDIT.md`
  `08403d4008e36336980ba43ae9d0e5ed90a632409cd63b645492c33f2f94dba7`
- `BLIND_RECONSTRUCTION.md`
  `ed74340c81c32390c9121f5cb33c28ab92b0cbf5463a83a239cd04beb1585a03`

Both reviews passed. The hostile audit also found a limitation of the finite
certificate: for `N=745`, the cross-center congruence
`57^2 == 92^2 (mod N)` already factors `N`. Thus the certificate validates
the F148 formulas but does not isolate them from every simpler
congruence-of-squares screen. No frozen claim says otherwise.

## Preserved rejected discovery rounds

V1 found a valid arithmetic cross ratio but duplicated the canonical exact
value and used a wrong normalized-root evaluator.

- `PREREGISTRATION.md`
  `27341e3be7dda2b6bbab862d449de99e4277057a44e4400157a1b2814afa49cb`
- `search.py`
  `0d33c8cbbb3821bbc05818f5a720f5081d18ae8d2f2a627518937ece4f64d481`
- `V1_SEARCH_RESULT.md`
  `624211288ebf2498c1957c27c7f0d717b83e953318f5e5d730baeba9764050cd`

V2 corrected both issues but its first canonical column was already an exact
square with a useful non-global root.

- `V2_PREREGISTRATION.md`
  `c18077d8d671e4bceb0297beadb151b2ee1fe1e91c47655b9589181bc64dec78`
- `search_v2.py`
  `2eb0f97574370de313a68f0ad7eda12f2ba25e7d4ee971e611dfc8d831c2e3c9`
- `V2_SEARCH_RESULT.md`
  `03f495fba1dc128d7433f64e35710dfc79d22072c4fde866fcd881d9fa10e581`

## Scope

The candidate proves an exact conditional metric theorem and a conditional
quasipolynomial amortization corollary. It does not force the source cycles,
small residual products, or slope diversity. It is not an all-input
factoring algorithm.
