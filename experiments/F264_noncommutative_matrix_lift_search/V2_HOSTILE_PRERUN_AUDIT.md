# F264-D02 V2 fresh hostile pre-run audit

Verdict: **FAIL — DO NOT LAUNCH**

Audit method: static inspection only. I did not compile or execute
`V2_symbolic_search.cpp` or `V2_remote_run.sh`. I did not open a cohort or use
the remote host. Dynamic target validation remains unopened.

## Frozen-artifact authentication

I computed every digest before reading the corresponding frozen artifact.
Every V2 digest and every preserved V1/FAIL-audit digest matches the local
bytes.

```text
PASS  V2_ALGEBRA.md              894ca1338c5cc7ce74e8bf60dbf987f2566928bdbe2a9e6d6542d02d969e98a5
PASS  V2_PREREGISTRATION.md      973727b78b07c7f9a455cb002b010c4f423ebeae9d6f4c3788d053aa7cad6d46
PASS  V2_symbolic_search.cpp     bf47d8d973433c645489ca5ce094b32eee7afa1f352b31e814354b0b42f8718d
PASS  V2_remote_run.sh           696219d0615bbb6f7a4da2bad1db8bf2aad699271ace25f63264de7c9d218e3b
PASS  V2_FAILED_LOCAL_COMPILE.md 9bdd657ab552353de158dc60b8e25688ccaf0101e28a4b3eb66a48469dc4d2a4
PASS  V2_VALIDATION_PENDING.md   9b6c7042ea0c7698c39a7654aac772e6a36c299153842625ba6b83030f90c852
PASS  V2_AUDIT_REQUEST.md        9bb70a1b0829f31187370a01b0c12dee18f31798af3eeb0f032904f8848336a6
PASS  V2_STATIC_VALIDATION.md    b1e2665027f874f42e3d29c95693ac636ef8c439fce37e4a29e42bba16360c97
PASS  V2_PRELAUNCH_MANIFEST.md   e1a2442589ec276d4c6c5fd4afd8c4c4522f6bd9f4165eea79b9555c673044
PASS  V2_FROZEN.sha256           52cb03a726c0ba26c79ad215971b6f72ec72199c50dac22f062f8016356255e0

PASS  ALGEBRA.md                 d15b020f26d5daaff1debfb57b765c5305264466f5882cae451acc62b513d52f
PASS  PREREGISTRATION.md         200926250aeb1a7a9839f8a50e0fdc6c8ab211254ad61aed229bacc6048f650b
PASS  symbolic_search.cpp        5fb4e172b9edb441e211b276e13ccabc810f657d9f44fcc8f728a3e157f73c0e
PASS  remote_run.sh              1fdaa2648797731b87d04a229003c05ad467bea14bb64efcc494fc4ce69adb0c
PASS  PRELAUNCH_MANIFEST.md      507ecd4c5c56d44867b0f34ca9262b7df5bb4d6450cd8121791d4912cb39e522
PASS  FROZEN.sha256              23d7aa6bd72f9cb7cf66b63ea9680fbd3adabcd4b543150929b249d8b0a2bb22
PASS  HOSTILE_PRERUN_AUDIT.md    f00fee9eac5fb71c9403d0f3a39b8cbf0bb0eb5682d6776f5eca1d26e21e3c9c
```

## Decisive blockers

1. **The smooth-order scope is not unambiguously frozen.** The scope section
   says that every listed cap is *per profile*, including `16 main words + 2
   controls` (`V2_PREREGISTRATION.md:104-116`). The source instead selects
   eight main words and one cyclic control per profile
   (`V2_symbolic_search.cpp:31,1162-1178`), or 16 main words and two controls
   globally. Its two schedules therefore give 36 trials. The later hot-loop
   forecast also says 36 (`V2_PREREGISTRATION.md:380-383`), so the document
   contradicts itself. Under the literal per-profile scope, the source omits
   half the main words and half the controls. Under the source/global scope,
   the preregistered per-profile claim is false. A hostile audit cannot choose
   one interpretation after freeze.

2. **An order trial does not check all 14 root proposals as requested.** V2
   constructs the correct 14-element vector, but
   `check_split_certificate` returns on the first proposal that supplies a
   proper gcd or a unit square root (`V2_symbolic_search.cpp:878-897`). Thus an
   early accepted proposal prevents the remaining proposals from being
   evaluated. A unit square root is already a valid split certificate, so
   this does not invalidate that certificate. It does invalidate the stricter
   frozen search-coverage claim that every order trial checks all 14 original
   and conjugate proposals (`V2_AUDIT_REQUEST.md:13-15` and
   `V2_PREREGISTRATION.md:270-275`).

3. **The frozen report-validation gate does not validate named decoys or the
   exact schema.** The preregistration promises validation of exact row counts,
   all 2,541 TSV columns, JSON dimensions, named decoys, and split labels
   (`V2_PREREGISTRATION.md:391-398`). The Python gate checks only the TSV
   column *count* and split value. It never compares the header with the 2,541
   frozen field names. It checks only that `decoy_summaries` has length ten,
   not that the ten names are the frozen names, unique, or nonzero. It accepts
   any candidate dimension above 11,000 rather than the exact described
   dimension (`V2_remote_run.sh:187-206`). Therefore a wrong or permuted
   schema and ten duplicate/misnamed decoys can pass the claimed gate.

4. **The firewall, memory, output, and deadline do not cover every executable
   stage.** `run_monitored` correctly wraps compile, self-test, benchmark,
   describe, both split processes, both Python validations, and compression.
   However, initial checksum authentication, all `grep`/`sed`/`awk` report
   parsing, the final byte check, and the EXIT-manifest hashing run outside
   `run_monitored` (`V2_remote_run.sh:18-42,150-176,218-229`). The EXIT trap
   writes `logs/F264-D02.manifest` only after the final 1 GiB check, with no
   subsequent size check. The final PASS path also has no
   `SECONDS <= deadline` assertion after compression, and the EXIT trap is
   outside the shared deadline. This is weaker than the audit request's
   every-executable-stage firewall and the frozen every-stage output/shared
   four-hour contract. It permits a nominal PASS whose final owned bytes or
   completion time exceed the stated limit.

Any one of blockers 1, 3, or 4 is sufficient to reject the immutable launch
packet. Blocker 2 independently rejects the exact root-coverage claim. No
target validation should begin from these bytes.

## Reconstructed V1 repairs that pass static inspection

- **PASS:** `ternary_nulls` now rejects `first == 0`, so the base-three
  all-zero vector is discarded. First-sign normalization retains one member
  of each nonzero sign pair. The five hard-coded relations and ranks match the
  algebra contract (`V2_symbolic_search.cpp:1297-1388`). The frozen independent
  integer transcript reports exactly the same five ranks and relations. This
  remains subject to the unopened target self-test.
- **PASS:** The associator matrix uses six separate ordered scalar columns.
  Its row/column indices expand both matrix products without commutation or
  aggregation (`V2_symbolic_search.cpp:1352-1364`).
- **PASS:** Family 10 emits three projected minors for every word step:
  `(K,C_parent)`, `(K,C_word)`, and `(C_parent,C_word)`
  (`V2_symbolic_search.cpp:945-955`). The self-test freezes the resulting
  count.
- **PASS:** `split_root_proposals` contains the seven original and seven
  conjugate forms (`V2_symbolic_search.cpp:866-879`). Exact per-input and
  aggregate lcms are serialized as decimal integers. The row output uses
  `max(0,bit_length(lcm)-1)` and also records the lcm bit length
  (`V2_symbolic_search.cpp:1645-1652,1849-1862`). This does not cure blocker 2.
- **PASS:** V2 explicitly preserves the `N=15,a=45` counterexample to gcd
  invariance. Zero is removed before primitive division. Units are counted and
  then included in sums, products, and exact P205 atom streams
  (`V2_symbolic_search.cpp:613-641,1484-1493`).
- **PASS:** Word scopes rank every word with complete public word data. Pair
  and triple scopes use bounded coprime affine permutations of exact
  combinatorial ranks, with no refill collision. Their coordinate hashes
  include the complete selected tuple (`V2_symbolic_search.cpp:781-841,
  1028-1080`). The independent frozen transcript covers the unranking formulas.
  The separate smooth-order ambiguity is blocker 1.
- **PASS:** Prime starts, odd prime scans, safe-prime calls, consecutive-prime
  scans, cohort filling, public-unit searches, and scope-step searches all
  have explicit finite caps (`V2_symbolic_search.cpp:185-277,740-759,798-816`).
- **PASS:** Ten named decoy counters exist and are incremented separately.
  Original and conjugate `r,C,K,k,H` streams have separate per-type counts and
  hashes, and family 30 has five separately emitted difference types
  (`V2_symbolic_search.cpp:41-45,600-657,957-999,1002-1026,1082-1107`). The
  executable output is correct here; blocker 3 concerns the runner's claimed
  validation of that output.
- **PASS:** P205 is label-separated from `process_public`; it emits 467 rows,
  exact residual gcds, checked integer baseline multipliers, integer
  residual loss, fixed lower-median cells, improvement/saturation counts, and
  the literal held-out margin/growth predicate
  (`V2_symbolic_search.cpp:1190-1211,1240-1278,1750-1798`).
- **PASS:** Each profile verifies that its public unit upper/lower generators
  do not commute modulo `N`. Ordered words and carry families retain matrix
  coordinates, so the main source is not only a trace or cyclic control
  (`V2_symbolic_search.cpp:723-777,919-1108`). Cyclic order results remain in
  a separate lcm.
- **PASS:** Public source construction and all word, pair, triple, order, and
  candidate selection functions receive `N`, profile data, fixed tags, and
  fixed seeds, not `p`, `q`, cohort labels, or discovery outcomes. Factors are
  first used by `score_p205` after the public result is complete
  (`V2_symbolic_search.cpp:1190-1211,1436-1468`). The held-out lead constants
  are literal source constants and are not discovery-selected.

## Other checks

- The exact carry divisions, determinant quotient, unit Cayley--Hamilton
  quotient, Fricke quotient, resultant sign, and associator quotient agree
  with `V2_ALGEBRA.md`.
- The order-stripping logic is valid conditional on a global return: `g=N`
  removes a prime, a proper gcd factors `N`, and `g=1` retains that prime. A
  successful unit split root therefore certifies that the resulting common
  local order divides both hidden `r-1` values.
- Accepted cohort rows enforce primality, declared factor bit length,
  `p<q<2p`, safe-safe structure, and pair uniqueness. The fixed split totals
  are 2,208 and 3,072 if every bounded generator terminates.
- The typed expression DAG implements the frozen unary, pair, resultant, and
  triple formulas. Candidate construction and public scoring do not use a
  factor-labelled beam.

The authenticated packet is still **DO NOT LAUNCH**. I edited no frozen V1 or
V2 artifact and no durable ledger.
