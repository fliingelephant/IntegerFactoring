# F260-D01 hostile pre-run audit

Verdict: **FAIL — DO NOT LAUNCH**

This was a static audit. I did not compile or execute `search.cpp`, invoke
`remote_run.sh`, use the remote host, generate a corpus, or inspect a cohort.

## Frozen-artifact authentication

All five requested SHA-256 values match the local bytes exactly.

```text
PASS  ALGEBRA.md             09691b4f5d005a330b85952dd9bfe4a0b93c2e5de7c23832d53572d4db5700a2
PASS  PREREGISTRATION.md     3b9c13374e38cba1394e9528fccb5ab623a6164829a3394f434f6b81acf38714
PASS  search.cpp             d4263fb8ceef91caecc4480ee3b49d8cd670b6ff34bb0920d8469c47ddf7e44e
PASS  remote_run.sh          7215ee1d9e34ee34146ca8ed992e96c582defc0cfd7b40bba39a91b78e98d103
PASS  PRELAUNCH_MANIFEST.md  7087694e8019280675f660eae88eec88620f33ffca323d29b180c33100d13d05
```

The target-check files listed in `PRELAUNCH_MANIFEST.md` also match their
listed hashes. This authenticates the disclosed historical checks. It does
not validate the final `search.cpp`: those checks used source hash
`905001a2...`, not the frozen final hash `d4263fb8...`.

## Decisive blockers

### 1. The factored and dyadic scores are not the frozen scores

The `M=1` factor-or-growth expression in `score_factored` is sound. The rest
of the registered score is not implemented (`search.cpp:878-938`).

- The source does not record the direct-factor probability or the local order
  distribution. It does not score the program's previously certified smooth
  state or the hostile state `M=gcd(p-1,q-1)`.
- It computes `expected_log_gain`, but discards it. It never reaches
  `Metrics`, an aggregate, an output, or a ranking key.
- Lines 918-935 call the probability of any new primary beyond `2^t`
  `dyadic`. This is not equation (7). The source never computes `J`, `L`,
  `L'`, `Phi`, or the distribution of `Delta Phi`; it averages three
  factor-or-growth probabilities instead.
- A factored program's primary score is only `f.progress`. It does not take
  the frozen maximum with the normalized expected dyadic-potential channel.

These defects change discovery orders 1 and 4 and invalidate all reported
factored-program meanings.

### 2. An unused quadratic primary loop defeats the resource projection

For every prime in a smooth annihilator, lines 911-915 multiply the equality
probabilities for every other prime. This is quadratic in the number of
primes, although the resulting expected log gain is discarded.

At a 63- or 64-bit discovery input, `lcm(1,...,n^3)` contains on the order of
23,000 primes. The source therefore performs on the order of 500 million
inner multiplications for that one factored program and one row, and over
`10^12` such operations across the largest discovery size. The authenticated
public benchmark never calls `score_factored`; the historical self-test calls
it on only one small row. Thus neither check supports the registered
30--180-minute projection or the four-hour gate. The production resource
qualification fails before execution.

### 3. P205 and collision reporting/ranking are incomplete or different

The core two-primary formula in `miller_probability` matches P205. The frozen
P205/collision experiment around it does not (`search.cpp:741-832,947-1001`).

- Word output retains neither `H(W)`, the two residuals, nor improvement over
  `(N-1)^n`.
- `captured_fraction` scores all prime powers of `s_p` and `s_q`. It does not
  remove the complete primary support already captured by the baseline
  `(N-1)^n`. Thus it is not the captured mass of the remaining P205 residual.
- It computes only the minimum normalized captured fraction. It does not
  retain the exact `kappa_ell`, captured log mass, or the registered joint
  inclusion--exclusion score from joint residue buckets.
- The pair score loops over all `m^2` ordered pairs, including `i=j` and
  equal-valued pairs, maps each such pair to `Delta=1`, and divides by `m^2`
  (`search.cpp:817-831`). The frozen score is the average over distinct-pair
  words (`i!=j` and `z_i!=z_j`). This changes both the sequence primary score
  and discovery order 3.

Direct scalar hits are reduced to a count. The factor, input, scalar syntax,
and exact certificate are discarded.

### 4. The exact frozen selection rule is not implemented

The preregistration takes the literal top eight under each of four orders,
deduplicates their union, and only then fills from order 1. `add_top` instead
increments `added` only when a program was not selected by an earlier order
(`search.cpp:1087-1107`). Each later order therefore skips overlaps and scans
past rank 8 until it contributes eight *new* programs. With enough programs,
this forces 32 entries before the registered order-1 fill and admits ranks
9 and below from orders 2--4. This is a different deterministic selection.

The selection firewall is also incomplete. `read_selection` reads only 32
numeric IDs (`search.cpp:1166-1182`). It does not check the SHA-256, syntax,
fingerprint, discovery aggregates, uniqueness, or the operational/oracle
flags. The runner creates a digest from the just-produced file, immediately
rehashes that same file, and never passes the digest to held-out execution
(`remote_run.sh:41-57`). Consequently the held-out executable cannot enforce
the required verified manifest and can accept duplicate or oracle IDs.

### 5. Required per-size output and all strong-lead gates are absent

`Aggregate` has only three cohort cells. `evaluate_corpus` ignores
`CorpusRow.bits` (`search.cpp:1008-1058`). Discovery and held-out output are
therefore pooled across all bit sizes, contrary to the required
program/split/bit-size/cohort rows.

The output cannot reconstruct any frozen strong-lead test: it has no
per-size median `-log2(score)`, no per-size hostile event count, no exact
certified-growth events, and no all-four-size safe-safe/consecutive result.
It also lacks exact direct-gcd certificates and residual-primary collision
explanations. No code evaluates or gates the strong-lead or collision-anomaly
criteria. A post-run interpretation cannot repair these omissions.

### 6. The hypergeometric operational boundary and canonicalization fail

`binomial_ratio` itself uses short signed interval products and never forms a
central binomial coefficient. That part passes. The operational grammar does
not respect the frozen boundary. All six generic sequence transforms are
applied to `hyper_p`, `hyper_q`, and the determinant sequences, including
numerator-only sums/differences and unchecked Euclidean quotient/remainder
operations (`search.cpp:419-445,461-484,568-575`). These are broader than the
registered reduced endpoints, adjacent cross-multiplied expressions, and
checked exact divisions. The preregistration's later “all 21 families” clause
conflicts with its explicit hypergeometric restriction; the source chooses
the broader clause, so the operational set is not certifiable as frozen.

Canonicalization is also only partial. Sequence and word candidates use
synthetic fingerprints, but every factored candidate receives a hard-coded
triple rather than a fingerprint evaluated on the 24 public synthetic inputs
(`search.cpp:632-638`). The advertised exact-value/provenance normalization
and general typed normalizer are absent. These defects affect grammar identity
and the selection manifest.

### 7. Oracle separation is not complete

The normal discovery selector filters the six recursive-oracle programs out,
which passes. They are nevertheless mixed into the ordinary discovery
aggregate rather than receiving the registered separate diagnostic ranking.
More importantly, the held-out loader does not recheck `operational` or
`oracle`, so the weak manifest boundary can admit them. The unconditional
32-program separation is therefore not enforced end to end.

### 8. Runner, output, and final-source validation gates are insufficient

- The runner never authenticates the five frozen hashes before compilation or
  production. It records hashes only after both phases.
- It checks incompatible experiment IDs once, before compilation. It does not
  recheck immediately before discovery or held-out generation.
- The 1 GiB check occurs only after both phases and covers `out_dir`, not the
  preserved logs. It cannot “abort before 1 GiB” as frozen.
- Output streams and expected row counts are not checked before the final
  manifest is accepted.
- The historical target compile/self-test used the earlier source. The runner
  does compile and self-test again, as the manifest requires, but it does not
  first authenticate the final source and the self-test never exercises
  `select_programs` or the disclosed fill repair. The final-source
  qualification therefore remains pending and is not a sufficient launch
  gate.

## Cohort audit

Conditional on generator termination, the accepted rows enforce exact factor
bit length, primality, `p<q<2p`, safe-safe structure, consecutive-prime
structure, and global modulus distinctness. The frozen counts are implemented:
8,960 discovery rows, 24,576 held-out rows, and 33,536 total rows, including
exactly 256 safe-safe rows at 16 discovery bits.

Retry exhaustion is not complete. The outer cohort loop has a 50,000,000-call
cap, but `random_prime`, `random_safe_prime`, and `next_prime` contain
internally unbounded searches (`search.cpp:127-151,677-700`). The outer cap
does not bound those searches.

## Disposition

The authenticated packet is not the frozen experiment described by its own
algebra and preregistration. The scoring and selection defects change the
mathematical ranking. The missing per-size and certificate outputs make the
registered lead criteria unrecoverable. The quadratic annihilator loop also
invalidates the production resource forecast.

Invalidate this packet before any corpus generation. Repair requires a new
source, preregistration reconciliation, validation record, and hash set. No
frozen artifact or durable-state ledger was edited by this audit.
