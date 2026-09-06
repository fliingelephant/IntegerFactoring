# F262-D01 hostile pre-run audit

## Verdict

**FAIL. Do not launch discovery or held-out cohorts from this frozen packet.**

The exact polynomial carry algebra is sound. The frozen executable is not the
preregistered experiment. It replaces the nullspace miner with hard-coded
rank controls, leaves two mandatory translation families empty, builds a
different capped candidate universe, cannot report candidate results by local
cycle scope, omits discovery ranking and lead gates, and does not enforce all
resource and output gates.

This verdict is static. I did not compile or execute `symbolic_search.cpp`, run
the shell runner, use the remote host, generate a cohort, or inspect a cohort.

## Frozen-artifact authentication

All supplied hashes match the local bytes.

```text
PASS  ALGEBRA.md             6b6c57cb6d1435f4121a90ab8c0fef1b833d73d72fa6875941228ba582bcd832
PASS  PREREGISTRATION.md     df6d4383fc76a8e37ef65068e057245334dc6d58489035c35dd4937f0971f78f
PASS  symbolic_search.cpp    d21828bef2196188daa50dfa65875de0de67ddd0a0b7302c290ee939d8b854c6
PASS  remote_run.sh          d406bff3baed85228580a35fafa98927c86dce6400bf67d9409a1004dd945e1d
PASS  PRELAUNCH_MANIFEST.md  08e0c36e9ffb10270c101af95aef93b808c1ecd9b71a8c22c08e6a31e2c3dba2
PASS  FROZEN.sha256          cf4cbc12c25bf44cae3f68ed9c1ed672fcea645f9462c52a177628f0ddcc0ce9
```

`shasum -a 256 -c FROZEN.sha256` also authenticates all eight listed
artifacts. The three additional entries are:

```text
PASS  FAILED_COMPILE.md      964b319db85205a95520eae5361cfcfae84a75283294d40176ccf4cda3f91e44
PASS  BUILD.md               5339b335cb2b6e0dec5a066f740a1d736e37317a92f9157d931046b4d6497d96
PASS  VALIDATION_PENDING.md  fcf0ba4c7dbdbb4c1f0b2d11284b8d99a1f652dc373ef3fdaeebcf66ef3c0982
```

## Decisive blockers

### 1. The modular-nullspace miner is not implemented

The preregistration requires 96 moduli `1000003+2t`, an RREF nullspace basis,
sparse `{-1,0,1}` reconstruction, exact authentication on 64 disjoint
moduli, and insertion of any new authenticated identity before candidate
construction.

The source instead fixes `N=1000000007` for all 96 training samples
(`symbolic_search.cpp:633-651`). `rref_rank` returns only a rank. The code
checks hard-coded expected relations and a lower bound on nullity
(`symbolic_search.cpp:603-631`). It never constructs a nullspace basis,
enumerates sparse coefficient vectors, canonicalizes reconstructed identities,
or creates a family from a new identity. The 64 held-back samples check only
the already-known associator and multiplicativity formulas; they do not test
translation (`symbolic_search.cpp:657-667`).

The required order is also reversed. `main` constructs and canonicalizes the
candidate list first, generates every semiprime task second, and calls the
identity routine third (`symbolic_search.cpp:708-721`). Thus a mined identity
could not enter the frozen candidate list even if the routine found one.

### 2. The advertised 48-family static layer is incomplete

Families 46 and 47 receive no atom anywhere in `process_polynomial`.
`translation_self_test` computes a raw translated high digit and an exact
canonical difference, then discards both (`symbolic_search.cpp:671-676`). It
does not populate `translation_raw_decoy` or
`translation_canonical_control`. The promised canonical source fingerprint
and transported-basis grouping are absent.

Other explicit coverage claims also fail:

- Family 14 emits minors of `(K,k)` and `(k,H)`, but omits all `(K,H)` minors
  (`symbolic_search.cpp:500-502`). This is not all two-minors of the three
  carry columns.
- Family 10 emits one fixed top-left `(d-1)` determinant per polynomial, not
  the cofactors of the lift windows (`symbolic_search.cpp:493-495`).
- Family 43 emits only the full Krylov determinant, despite the registered
  `multiplication_krylov_minors` scope (`symbolic_search.cpp:462-464`).

The source therefore cannot support the claim that the fixed static layer is
exhaustive over its registered scopes.

### 3. Candidate canonicalization and the capped DAG differ from the freeze

The freeze requires syntax-sorted children for commutative nodes. The source
orders children by family number, not by normalized syntax
(`symbolic_search.cpp:543-562`). For example, it places
`low_coeff_control` before `lift_coeff_C`, although their syntax strings sort
in the opposite order. This changes the hashes used to choose the 8,192
triples and 4,096 quadruples, so it changes the capped candidate universe.

The second canonicalization also does not evaluate static expressions on 32
public synthetic odd moduli. It assigns independent SplitMix residues directly
to every family sum and product, then evaluates them modulo the two fingerprint
primes (`symbolic_search.cpp:590-600`). These assignments are not outputs of
the polynomial source and cannot discover aliases forced by that source.

Finally, because the identity routine runs after this step and returns only a
rank string, authenticated mined families can never participate in the DAG.

### 4. Candidate cycle labels are not local cycle labels

Static atoms retain a correct per-polynomial `mismatch` counter. Candidate
summaries do not. One pair of sum/product accumulators combines atoms from all
cycle-match and cycle-mismatch polynomials (`symbolic_search.cpp:375-389,
684-688`). The aggregate then calls every candidate test and hit a mismatch
test or hit whenever the input contains at least one mismatch polynomial
(`symbolic_search.cpp:727`). A hit can come from a match polynomial, a
mismatch polynomial, or an interaction between both groups. The reported
candidate mismatch rate therefore is not the registered conditional rate on
cycle-mismatch polynomial scopes.

The hidden partitions do not alter candidate construction or gcd arithmetic.
That isolation passes. The later label attribution does not.

### 5. Discovery ranking and frozen lead interpretation are absent

There is no implementation of the five-key discovery ranking. Candidate JSON
is emitted only in candidate-ID order (`symbolic_search.cpp:728-730`). It does
not also report discovery rank. The program never applies the held-out
16-input, three-size, safe-safe, and two-polynomial-degree lead rule, and it
never checks that a synthesized candidate beats every constituent family.

The output cannot repair this after the run. Candidate hits have no polynomial
degree or polynomial identifier. Family summaries combine discovery and
held-out inputs. The per-input anomaly file also omits polynomial scope. Thus
the two-degree condition and constituent-family comparison cannot be
reconstructed from the declared outputs.

The JSON also contains no exact aggregate-hash fields. The only in-program
candidate checksum is a 64-bit, order-dependent per-input hit checksum
(`symbolic_search.cpp:682,688`). Runner file hashes are not the registered
candidate aggregate hashes.

### 6. The resource and output gates are weaker than the frozen protocol

`VALIDATION_PENDING.md` requires the runner to reject the run unless the
printed runtime, memory, and output projections all pass. The runner parses
only the runtime projection (`remote_run.sh:28-32`). It never parses or checks
`projected_peak_mib`, `projected_tsv_mib`, or `projected_json_mib`. The memory
number printed by the benchmark is a source literal, not a measurement
(`symbolic_search.cpp:718`).

The 4 GiB address-space limit applies only to the cohort command. Self-test
and benchmark run without it (`remote_run.sh:23-26,49-54`). The post-run size
check covers each TSV separately, after it has already been written. It does
not check the JSON or the combined uncompressed output
(`remote_run.sh:59-68`). The pre-run byte formula is asserted without deriving
an upper bound from the maximum anomaly-row count and syntax length.

The preregistration also says measured benchmark results will appear in
`BENCHMARK.md`. No such artifact exists, and the frozen runner writes only a
log file.

## Checks that pass

- **Exact carry algebra: PASS.** Monic reduction is canonical. The full
  associator has the correct four terms and signs. Substituting `K=k+NH`
  proves exact coefficientwise divisibility of the digit residual by `N`.
  The source checks the full zero and both exact divisions before using the
  quotients (`symbolic_search.cpp:318-337,522-531`).
- **Exponent-lift quotient: PASS.** The source uses the canonical product lift,
  subtracts `K` and both cross terms, and performs checked exact division by
  `N`. Self-test mode also compares all ten products with direct exponentiation
  (`symbolic_search.cpp:498-516`).
- **Translation algebra: PASS; implementation coverage: FAIL.** The signs in
  `f(X-t)`, `X-t`, and inverse transport by `X -> X+t` are correct. Full
  residues are transported before comparison. The failure is the missing
  registered atoms, fingerprints, and held-back translation authentication.
- **Polynomial source and cleanup: PASS.** The loops create four recipes for
  every degree 2 through 5 and five elements `X+s`. Discriminant gcds are
  handled as cleanup or skip before scoring. Multiplication matrices,
  characteristic coefficients, resultants, and the public `N`-primitive gcd
  operation use exact integer arithmetic.
- **Cycle reconstruction: PASS.** For a surviving squarefree polynomial, the
  code computes the degrees of `gcd(f,X^(r^k)-X)` and applies the correct
  divisor recurrence. Hidden factors enter only this verifier path and the
  final certificate labels, not candidate values.
- **Cohort generation: PASS, conditional on termination.** Exact factor bit
  length, primality, `p<q<2p`, safe-prime structure, pair uniqueness, the
  16-bit safe-safe reduction, and the total count 5,280 are enforced. The
  candidate list is fixed before cohort generation.
- **Runner core controls: PASS.** The initial eight-entry manifest check,
  conflict checks, production thread count, `nice 15`, 14,400-second cohort
  timeout, production 4 GiB limit, and nonzero exit propagation are present.
  The prelaunch manifest correctly states that execution validation is still
  pending.

## Scope and disposition

I read `AGENTS.md` and `PROMPT.md` and audited the authenticated algebra,
preregistration, C++ source, runner, manifest, build record, and pending-gate
record. I used only local read-only inspection, hash checks, and exact symbolic
rederivation. I edited no frozen artifact and no durable-state ledger.

The exact frozen packet must be invalidated before execution. Repair requires
a new source/preregistration/hash set, not a post-run interpretation change.
