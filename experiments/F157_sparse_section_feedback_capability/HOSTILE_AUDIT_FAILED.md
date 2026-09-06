# F157-D01 hostile audit — FAIL as written

## Verdict

**FAIL as written.** The registered computation, certificate, finite nulls,
hashes, and factor-assisted index all pass. `RESULT.md` then makes a material
scope error. It says that there is no public method to locate the successful
pair and asks for a public quasipolynomial selector. The pinned F156 source
already gives that method: enumerate the public support-two pairs and run the
public gcd screens.

The exact disposition is:

- **PASS — registered evidence.** The unchanged authoritative workflow
  replayed inside the 900-second limit. Every non-time output field and every
  deterministic log line matched. All 65 indexed candidates passed an
  independent public arithmetic check. The four reported support-two nulls
  follow from the complete factor-assisted partition proved below.
- **FAIL — claim boundary.** Factor assistance is needed only for the fast
  registered implementation. It is not needed for a public quasipolynomial
  locator. F157 gives a public quasipolynomial factor path on the fixed
  `N=3241632473`. It gives no all-input success theorem, density law,
  polynomial-time method, or public locator known to meet the 900-second
  experimental limit.

I did not modify a frozen artifact, `MANIFEST.md`, `REGISTRY.md`, or a durable
ledger. No project rule requires the manifest to hash this audit, so I left it
unchanged.

## Artifact integrity and registration

I read and hash-scanned all 1,354 files that existed in the directory before
this report. Eleven were top-level experiment artifacts. The other 1,343 were
generated Sage or Python cache files: 1,341 files under `.sage_runtime` and two
under `__pycache__`. No cache file is registered evidence.

All six preregistered hashes match `REGISTRATION.json`:

| Frozen file | SHA-256 |
|---|---|
| `DESIGN.md` | `7f9d7504bd285b6b32497f783d8a9f28609373e73437030e03bcd54877e6ec10` |
| `FAILED_RUNS.md` | `b3baf7db5c2ae7fee6d5db75b9666394d8d02f45cc553566ea81cb17b5fecb75` |
| `INPUT.json` | `ca227228ed692e3895b0f4d4407b14b5000c0f0ec4134aff394b211791cb2009` |
| `QUESTION.md` | `d8790ab6a23597b28b949405547f4cfd8d1187602fcf1f2ad591439022a53f56` |
| `run_with_timeout.py` | `560096b0689690f082e7eabd8c8cbb6d955f83da79fa05003f535f5f510b8999` |
| `search.py` | `1f9bf511a8a0d5783dfcbca891d7e4022e158382395b3925cb38241ee2d6cb69` |

All seven upstream pins in `INPUT.json` also match:

| Pin | SHA-256 |
|---|---|
| `F111_RECONSTRUCT_INPUT.json` | `8622024473bd602d1d4928fad959099db1ae463e9bd736b7b6ec59fbb99c3f61` |
| `F111_RECONSTRUCT_LAYER_decoder_v1.py` | `b8435179093f9121d7ab9ca6c5949e7816351c34cc85d4973cbc65bae6ae80f8` |
| `F111_RECONSTRUCT_LAYER_decoder_v2.py` | `12a24643fa9df6b8ad03106d9a562b823b4029223cf2a26f1c5e75ab23f6f3e2` |
| `F118_OUTPUT.json` | `6c8571ef2e851d5cec1c31314887f35932a22ef1de10dcff7e7b40a0cfa572bf` |
| `F118_scan_full_source.py` | `07be2d7b124fc4470de568b559a7918d0111802c69d2cfbe144fdccbcb7ec75c` |
| `F156_PROOF.md` | `4024a5d8732ffec5dea0711498bf77e0accfc079868fecc82ace56c91243169d` |
| `F156_STATEMENT.md` | `d426df6c293fd835c85260b14fb6ddd57a99ff812a4c7b9a74b084318ed34527` |

The registered post-run hashes also match the manifest:

- `REGISTRATION.json`:
  `0c056554d8e0a5fcfe8ff7b2d2149936daaef6f3f1a6fb56c71d2712d4d7f6b5`;
- `OUTPUT.json`:
  `f07dc61d14a1f3ba16d980796529e7a06794d3b4b296481f12eca8270e151e29`;
- `RUN.log`:
  `97db534706b7e074843270548d0535368f22eaa784f227f0def711dc8f7f356a`;
- `RESULT.md`:
  `48914a43303d61f70a69afbc7eca5679c64267ebb25d4b8f5418ec4c96e02904`.

The F157-D01 registry row agrees with the registration. It names the same
runner, source, five inputs, 900-second limit, output files, finite-evidence
scope, and factor-assisted support-two indexing. I verified that every
disclosed `p` and `q` is prime, distinct, and has product `N`.

## Authoritative replay

I copied the registered files into an isolated `/tmp` repository mirror and
linked the seven pinned upstream files read-only. I then ran the unchanged
`run_with_timeout.py` with SageMath 10.9, Python 3.14.3, and gmpy2 2.3.0.
This preserved the authoritative workspace files.

The replay passed in 165.508371 seconds. Its internal output time was
164.913555 seconds. The authoritative run passed in 167.386987 seconds. Both
runs stayed below 900 seconds.

After removing only `elapsed_seconds` fields, the replay JSON was exactly
equal to `OUTPUT.json`. After removing only the measured runner time, every
deterministic result line in the replay log was exactly equal to `RUN.log`.
Thus every recorded source, refinement, decoder, support, index, hash, and
candidate count reproduced.

A separate audit checker first encountered Sage's unwritable default cache.
I reran the same checker with `DOT_SAGE` in the isolated `/tmp` directory. It
then passed. This was an audit-environment failure, not an experiment run.

## Counts and finite outcomes

The independent checker recomputed every displayed pair count as
`r*(r-1)/2`, recomputed every null count, and checked the recorded list
lengths and summary totals.

| `N` | Rank `r` | Public blocks | Support-one scanned / hits | Support-two pairs | Candidates / proper hits / false | Null pairs |
|---:|---:|---:|---:|---:|---:|---:|
| 3,241,632,473 | 11,874 | 13,284 | 11,874 / 0 | 70,490,001 | 65 / 65 / 0 | 70,489,936 |
| 204,800,061,759,986,701 | 106,937 | 134,359 | 106,937 / 0 | 5,717,707,516 | 0 / 0 / 0 | 5,717,707,516 |
| 204,800,066,879,973,329 | 80,446 | 100,507 | 80,446 / 0 | 3,235,739,235 | 0 / 0 / 0 | 3,235,739,235 |
| 204,800,093,759,919,353 | 65,005 | 82,445 | 65,005 / 0 | 2,112,792,510 | 0 / 0 / 0 | 2,112,792,510 |
| 204,800,123,199,900,673 | 91,979 | 115,799 | 91,979 / 0 | 4,230,022,231 | 0 / 0 / 0 | 4,230,022,231 |
| **Total** | **356,241** | **446,394** | **356,241 / 0** | **15,366,751,493** | **65 / 65 / 0** | **15,366,751,428** |

The old ranks and nullities match the pins on all five inputs. Every old
direct screen is nonproper. Every old dependency root is global. The
support-one scan is complete and null.

I also checked all 446,394 terminal blocks with an independent perfect-power
predicate. None is an unextracted perfect power. Thus the fixed corpus does
not hit the gap between the source's finite odd-exponent list and the pinned
F156 maximal-perfect-power convention.

## First public certificate and all 65 hits

I rebuilt the first F111 ledger and factor-free basis in isolation. Basis
indices `(253,9723)` select source columns `(253,9729)`. Their common block
indices are `(0,1,23)`, with public values `(2,3,89)`. Therefore

\[
C=2\cdot3\cdot89=534.
\]

The two public lifts are `1620816237` and `2549408872`. Applying the public
star law gives

```text
z = 3183314832
w = z^(-1) mod N = 205056
z^2 mod N = 1509286823
gcd(z - w, N) = gcd(z^2 - 1, N) = 41011
gcd(z + w, N) = gcd(z^2 + 1, N) = 1
N / 41011 = 79043
```

This verifies the certificate without using a hidden CRT orientation.

For every one of the 65 reported hits, I independently checked:

- the basis pair is ordered, in range, and unique;
- `z*w = 1 mod N` and `z^2 = q_mod_N mod N`;
- both reported gcds and both dense-screen gcd identities;
- at least one reported gcd is a proper factor;
- `C` is a unit, and `C=1` when the recorded intersection is empty.

Exactly 63 pairs expose `41011`, and two expose `79043`. Re-encoding the 65
sorted pair keys gives
`ef54beec77babbcd82ea9e9833c24216bf4e6ac4603811c6a8abb160e15eca3d`,
the registered candidate hash.

## Factor-assisted index

The index's completeness and no-false-candidate claims are correct for the
five disclosed distinct-prime semiprimes.

For a pair `(i,j)`, let `C` be the product of its common public blocks. The
pair screen modulo a disclosed prime `r` has sign `epsilon` exactly when

\[
Q_j=\epsilon C^2/Q_i\pmod r.
\]

Every common block has degree one, light degree from 2 through 256, or heavy
degree above 256. A degree-one block cannot be common to a pair.

- If a pair has a common light block, the light pass enumerates it once. Its
  owner is its least common light block. The pass computes its complete
  intersection and both local screen values.
- Otherwise its common blocks are all heavy. For the left record, the heavy
  pass enumerates the exact intersection as one subset. It rejects records
  with a common light block and checks the exact heavy intersection.
- The joint local lookup retains a sign only when the equality holds modulo
  exactly one of `p` and `q`. For `N=pq`, that condition is exactly a proper
  gcd. Equality modulo both primes gives only the improper gcd `N` and is
  excluded.

These cases are disjoint and cover every unordered pair. The replay retained
65 candidates. Direct public reconstruction accepted all 65. It retained no
false candidate. The same complete partition retained no candidate on the
other four inputs, so their finite support-two null counts are valid.

This proof does not make the registered discovery factor-free. The factors
choose the small subset that is replayed. The certificates themselves and
their gcd verification are public.

## Material scope error in `RESULT.md`

The following two claims are false as written:

> It does not give a public method to locate the successful pair.

> The remaining source-side problem is to replace the disclosed
> factor-assisted index with a public quasipolynomial selector.

The pinned F156 statement sets

\[
L=\lceil\log_2(n+1)\rceil,\qquad D=L^2,
\]

and explicitly enumerates every nonempty relation-basis subset of size at
most `D`. Here `n` is 32 or 58, so `L=6` and `D=36`. Every support-two pair
is already in the declared public menu.

F156 also proves `r <= 2^{O(L^4)}` and a total public source cost of
`2^{O(L^6)}`. A direct lexicographic scan of all `r*(r-1)/2` pairs is
therefore quasipolynomial. It uses only the public basis lifts, the star law,
modular inversion, and gcd. It can stop at pair `(253,9723)` on the positive
fixed input. The disclosed factors only accelerate the registered finite
run from a 70,490,001-pair public scan to 65 public replays.

The correct boundary is narrower:

- F157 does not implement a factor-free locator known to finish within 900
  seconds, or a public selector asymptotically smaller than exhaustive F156
  enumeration.
- F157 does not prove that any support layer succeeds on a new input. It
  gives no all-input success law, useful-pair density, or polynomial-time
  factoring algorithm.
- The remaining source theorem is an all-input progress or success law. It
  is not the existence of a public quasipolynomial locator on this fixed
  positive input.

The arithmetic artifacts need no correction. `RESULT.md` needs this scope
repair before the complete F157-D01 artifact can pass.
