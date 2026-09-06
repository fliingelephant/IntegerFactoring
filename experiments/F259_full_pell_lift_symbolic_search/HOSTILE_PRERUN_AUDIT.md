# F259-D01 hostile pre-run audit

Verdict: **FAIL — DO NOT LAUNCH**

Audit method: static inspection only. I did not compile or execute
`symbolic_search.cpp`. I did not use the remote host, run a self-test or
benchmark, or open any discovery or held-out cohort.

## Frozen-artifact authentication

All requested hashes match the local bytes.

```text
PASS  PREREGISTRATION.md  0b162d3f0b8c653483a3b92e5106b2b60b7066fa464366e9654163182198a014
PASS  ALGEBRA.md           7f5c1679816eb57e9810ce112f93c97ed0edef136f710f22d91596287e0cefb8
PASS  symbolic_search.cpp  2b8c941782cfa10aeb3598a558c6a9008a9a98534933ca58c4e94d628be9a145
PASS  remote_run.sh        77be4b41f8d414819bc0137f723309804e63fc193556f0e5c1520b7b7fd83e45
PASS  FROZEN.sha256        f876baafab99508e900b3fea8d65a5416118e756eb9dd5987d79786f1d101ead
```

The three additional entries inside `FROZEN.sha256` also match:

```text
PASS  SELF_TEST.md         678999e8f58703a569da5d68df7a5fc12933a5aff15a213b80706ff2a078b434
PASS  BENCHMARK.md         f3b59bc0f1cc5c3f568a38517f390028f26c7575b728514fa84b0d74b6bcbc24
PASS  FAILED_SELF_TEST.md  2d0325d849ea1c5915f78d653b57807b612f4af3d50e15e112f858b00e8a301e
```

## Decisive blockers

1. **Families 20 and 22 are not the frozen carry families when the first
   carry `c` is zero.** The frozen family-20 atom is exactly
   `D*c*(2*z+c*N)`, hence it is zero when `c=0`
   (`PREREGISTRATION.md:102-110`). The source substitutes the integer `1`
   (`symbolic_search.cpp:825-828`). This changes the required zero count into
   a unit count. More importantly, the frozen family-22 brackets
   `3*z+c*N` and `B_(5|h,j)` remain defined when `c=0`; the source emits no
   core atom at all unless `c!=0` (`symbolic_search.cpp:839-845`). It also
   suppresses target-15 route sums and differences if either core was omitted
   (`symbolic_search.cpp:848-850`). Omitting those generally nonunit brackets
   changes family products and therefore changes the 255 P205 words.

2. **The identity miner uses a different feature basis from the frozen
   description.** Each scalar coordinate of the displayed cocycle has six
   additive terms, so the two coordinates supply 12 scalar terms. Source
   columns 0--11 are those terms, but columns 12--15 are the additional
   products
   `cij.a*cjk.b`, `-cij.b*cjk.a`, `cij.a*cjk.a`, and `cij.b*cjk.b`
   (`symbolic_search.cpp:501-512`). Those four products do not appear in the
   preregistered cocycle expression (`PREREGISTRATION.md:142-158`). Thus the
   asserted rank-14/nullity-2 result is for an augmented 12+4 basis, not for
   “the 16 scalar monomials ... that appear” in the frozen expression. The
   packet is internally inconsistent about the identity universe it claims
   to exhaust.

3. **The claimed typed-DAG canonicalization is not implemented.** The source
   has 22 static schema strings and hard-coded arithmetic calls, but no typed
   expression nodes, scoped DAG, normalizer, or survivor canonicalization.
   `mine_identities` checks only the two RREF basis vectors and returns a status
   string (`symbolic_search.cpp:533-617`); it does not enumerate all ternary
   coefficient candidates or canonicalize word nodes. Public powers of `N`
   are stripped without a decoy counter, so they cannot be reported as the
   preregistration requires (`PREREGISTRATION.md:118-133`). The 255-word set
   is constructed unchanged regardless of which identities were recovered.

4. **Some public cleanup factors lose their required certificate.** A proper
   `gcd(D,N)` and a proper grammar-atom gcd set `first_certificate`, but proper
   gcds from a nonunit supplied root, an exact-square row, or a repeated `y`
   only increment `cleanup_events` and discard the divisor and scope
   (`symbolic_search.cpp:635-670`). The TSV can therefore contain
   `cleanup_events>0` with an empty `first_certificate`, while the frozen
   output requires first certificates (`PREREGISTRATION.md:227-233`). These
   certificates cannot be reconstructed from the output because the screened
   row coordinates are not emitted.

5. **The runner does not enforce absolute F258 nonoverlap.** Its one-time
   process check recognizes the known F258 production command, but it matches
   only two argument patterns and occurs before compilation and the unbounded
   self-test (`remote_run.sh:8-16`). There is no second check immediately
   before production and no lock or monitor. An F258 process started after the
   check, or an invocation without the expected summary argument, can overlap
   F259, contrary to `PREREGISTRATION.md:260-261`.

6. **The output and resource gates are incomplete.** The 4 GiB limit,
   `nice 15`, and four-hour timeout cover only the production executable.
   The mandatory self-test has no timeout, memory limit, or niceness, and gzip
   also runs outside the four-hour interval (`remote_run.sh:15-35`). The 1 GiB
   check happens after generation and checks only the TSV; it excludes the
   summary JSON and logs. There is no successful-exit row-count check, JSON
   parse check, or stream-close check before the manifest is accepted. This is
   weaker than the frozen “own output” limit and preservation requirement.

7. **Cohort retry exhaustion does not bound prime generation.** The outer
   per-row attempt loop aborts at one million attempts, but `random_prime` and
   `random_safe_prime` each contain an inner unbounded loop
   (`symbolic_search.cpp:180-200,411-424`). The production timeout can reject a
   stalled run, but it does not make the deterministic 7,040-row construction
   itself bounded.

8. **Reporting does not fully implement the frozen aggregation/ranking
   contract.** The TSV preserves per-input family counts and all residual
   pairs, and the JSON correctly aggregates word scores. It does not aggregate
   family atom/direct-gcd counts by split, size, and cohort. Discovery
   “description length” is the length of a short family-name label, not the
   normalized expression syntax (`symbolic_search.cpp:1104-1130`). Cohort
   labels are also emitted as `neighbor` and `safe`, rather than the frozen
   `consecutive` and `safe-safe` names. These do not alter the raw arithmetic,
   but they change the frozen reporting layer.

## Algebra and 22-family audit

The row quotient identities, tangent identities, two multiplication carries,
quadratic resultant, same-`D` resultant factorization, and both Taylor
curvature formulas are correct. All explicit `N` and `N^2` divisions used by
the source have exact-divisibility assertions. Public `N`-primitive
normalization matches `ALGEBRA.md`.

```text
01 PASS  row_ell
02 PASS  row_k_control
03 PASS  row_tangent_minus
04 PASS  row_tangent_plus
05 PASS  row_norm_defects (both atoms)
06 PASS  original_q_minus
07 PASS  original_q_plus
08 PASS  multiplication_carry (a and b)
09 PASS  carry_norm_minus
10 PASS  carry_norm_plus
11 PASS  lift_determinants
12 PASS  vector_determinants (all 10 pair determinants)
13 PASS  lift_resultant_minus
14 PASS  lift_resultant_plus
15 PASS  carry_resultants (8 signed factors per retained edge)
16 PASS  cross_lift_resultants (lift/lift and tangent/tangent)
17 PASS  collision_minus (all five frozen row features)
18 PASS  collision_plus (all five frozen row features)
19 PASS  triple_determinants (4 linear + 4 affine + 1 carry affine)
20 FAIL  first_carry_control substitutes 1 for the frozen zero atom
21 PASS  second_carry_full with checked exact N^2 division
22 FAIL  second_carry_core and route atoms are omitted when c=0
```

## Word grammar, scopes, cohorts, and scores

- **PASS:** The base-product construction has exactly
  `1+22+binom(22,2)+1=255` words. It raises each base to
  `n=bitlength(N)` modulo `s_p,s_q`, preserving both exact gcds.
- **PASS:** `H=max(gp/sp,gq/sq)`, strict-input selection, means, interpolated
  median/90th/99th loss quantiles, baseline-improvement counts, and saturation
  counts are implemented correctly. Every raw row contains all 255 gcd pairs.
- **PASS:** Same-`D` edge patterns, sum-window checks, set deduplication,
  SplitMix64 ranking, and the 256-per-`D` cap match. Triple patterns, the
  repaired sum-window check, independent priority tag, deduplication, and the
  64-per-`D` cap match. Cross-`D` same-index pairs and all valid `{3,5}` carry
  compositions are traversed.
- **PASS:** Accepted cohort pairs have the declared prime bit lengths,
  `p<q<2p`, safe-safe structure, and uniqueness across all cohorts at a fixed
  size. The frozen counts sum to 7,040 if the inner generators terminate.

## Resource projection and historical self-test

The static largest-input insertion bound in the preregistration is consistent
with the source:

```text
rows:         3,840 * 6        =  23,040
pairs:        2,048 * 37       =  75,776
triples:        512 * 9        =   4,608
compositions: 3,840 * 12       =  46,080
cross-D:        480 * C(8,2)*2 =  26,880
total                              176,384
```

The exact word-score projection is `7,040*255=1,795,200`. The documented
slowest benchmark extrapolation, `7040*4.953039/8`, is about 4,359 seconds
(72.6 minutes), so the stated 1.2--3 hour envelope is arithmetically
consistent before shared-host overhead. These estimates do not repair the
runner-gate defects above.

`FAILED_SELF_TEST.md` describes a pre-freeze out-of-bounds read of
`raw[i+j+k]`. The frozen source now requires `i+j+k<=4*n` before constructing
the triple and then uses that checked target (`symbolic_search.cpp:749-813`).
The historical defect is therefore repaired in this version. The current
self-test is still a weak grammar gate: it requires only a positive total atom
count, not the documented exact count or nonempty/exact counts for all 22
families (`symbolic_search.cpp:945-964`). I did not rerun it.

The authenticated frozen packet fails because its identity universe and two
base families do not match the preregistration, with independent certificate,
firewall, and gate defects. No frozen artifact or durable ledger was edited by
this audit.
