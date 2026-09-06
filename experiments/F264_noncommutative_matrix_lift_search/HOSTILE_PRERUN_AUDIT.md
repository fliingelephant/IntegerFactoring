# F264-D01 hostile pre-run audit

Verdict: **FAIL — DO NOT LAUNCH**

Audit method: static inspection only. I did not compile or execute
`symbolic_search.cpp`. I did not use the remote host or open any cohort.

## Frozen-artifact authentication

All supplied hashes match the local bytes.

```text
PASS  ALGEBRA.md             d15b020f26d5daaff1debfb57b765c5305264466f5882cae451acc62b513d52f
PASS  PREREGISTRATION.md     200926250aeb1a7a9839f8a50e0fdc6c8ab211254ad61aed229bacc6048f650b
PASS  symbolic_search.cpp    5fb4e172b9edb441e211b276e13ccabc810f657d9f44fcc8f728a3e157f73c0e
PASS  remote_run.sh          1fdaa2648797731b87d04a229003c05ad467bea14bb64efcc494fc4ce69adb0c
PASS  PRELAUNCH_MANIFEST.md  507ecd4c5c56d44867b0f34ca9262b7df5bb4d6450cd8121791d4912cb39e522
PASS  FROZEN.sha256          23d7aa6bd72f9cb7cf66b63ea9680fbd3adabcd4b543150929b249d8b0a2bb22
```

The three additional entries inside `FROZEN.sha256` also match:

```text
PASS  FAILED_LOCAL_COMPILE.md  4900434a984982b633432109ced9442aeb7ce56eb2416a1a61699f3c300d7d94
PASS  BUILD.md                 048b13da29065f5ba4382d9cc532b62b5e4dc3d4a11d47d798cac6bf0e3161f2
PASS  VALIDATION_PENDING.md    34ce12494d4735b6d60c573a11d6cdde901fbf16c18565655cb8a294331413a6
```

## Decisive blockers

1. **The frozen self-test must fail.** In `ternary_nulls`, base-three digit
   `1` maps to coefficient `0`. Therefore code
   `(3^cols-1)/2` represents the all-zero vector. It lies in the loop range,
   has `first == 0`, survives the `first < 0` filter, and is appended as a
   null vector for every matrix (`symbolic_search.cpp:1065-1093`). The code
   then requires exactly one null vector and requires it to be a nonzero
   frozen relation (`symbolic_search.cpp:1130-1136`). Thus
   `mine_identities()` cannot pass, and `remote_run.sh` must stop at
   `--self-test` before the benchmark (`remote_run.sh:31-35`). This conclusion
   does not depend on cohort data.

2. **The frozen algebra contains a false gcd claim.** `ALGEBRA.md:171-174`
   says that removing exact powers of `N` leaves `gcd(a,N)` unchanged. For
   `N=15` and `a=45`, the primitive part is `3`, while the gcd changes from
   `15` to `3`. Primitive cleanup can be useful, but this stated invariant is
   false and cannot authenticate the scoring rule as written.

3. **Family 10 is not the frozen family.** The preregistration requires
   two-minors among `K`, `C_parent`, and `C_word`
   (`PREREGISTRATION.md:121-125`). The source emits only one minor of `K` and
   `C_word`; it never uses `C_parent` (`symbolic_search.cpp:764-785`). This
   changes the static atom universe.

4. **The nullspace control has the wrong associator feature matrix in addition
   to the fatal zero-vector bug.** The frozen control calls for six ordered
   scalar summands (`PREREGISTRATION.md:185-199`): the two matrix products
   each expand into two ordered coordinate products. The source aggregates
   those products and builds only four columns (`symbolic_search.cpp:1117-1124`),
   then authenticates a four-coefficient relation. It is not the frozen
   nullspace search.

5. **The split-root proposal set is incomplete.** `ALGEBRA.md:134-140`
   freezes seven entry/lift proposals plus the matching public-conjugate
   coordinate differences. `split_root_proposals` returns only the seven
   entry/lift proposals (`symbolic_search.cpp:712-715`). The order certificate
   therefore does not search the frozen proposal set.

6. **Sparse scope selection is not the frozen priority construction.** The
   preregistration freezes a SplitMix64 priority of complete word, pair, or
   triple scopes (`PREREGISTRATION.md:89-108`). Word caps are scored by vector
   ordinal rather than the complete word scope (`symbolic_search.cpp:673-687`).
   Pair and triple caps repeatedly sample indices from an attempt counter until
   a set fills (`symbolic_search.cpp:730-758`); they do not rank the complete
   scopes. Pair/triple coordinate hashes likewise omit length, profile, and
   other complete-scope fields (`symbolic_search.cpp:842,871`). These choices
   freeze a different candidate universe.

7. **Units are silently removed from the synthesized atom sums.** The frozen
   grammar forms `S_f` and `P_f` from each family's atoms and only explicitly
   excludes the zero atom from products. The source returns on `abs(value)==1`
   before updating either accumulator (`symbolic_search.cpp:561-581`). Omitting
   a unit from a product is gcd-neutral up to sign, but omitting `+1` or `-1`
   from `S_f` changes synthesized expressions and their gcd outcomes.

8. **Required order and P205 results are not recorded.** The preregistration
   requires the accumulated certified lcm and its new bits
   (`PREREGISTRATION.md:216-236`). Output retains only its bit length
   (`symbolic_search.cpp:1303-1319,1336-1339`), so the claimed common-order
   certificate cannot be reconstructed. The P205 core correctly constructs
   467 modular words, but output does not record an exact baseline-improvement
   quantity. The JSON reduces it to the predicate
   `gp > baseline.gp || gq > baseline.gq`
   (`symbolic_search.cpp:1350-1366`). Raw row gcds permit later recomputation,
   but that is not the frozen recorded score or the preregistered median-loss
   interpretation.

9. **The cohort firewall is weaker than frozen.** The packet requires a process
   check before validation and before each data split
   (`PREREGISTRATION.md:314-317`). The runner checks once before both self-test
   and benchmark, then once before one combined discovery/held-out execution
   (`remote_run.sh:31-35,52-61`). It neither rechecks before the benchmark nor
   has a boundary check before held-out work. An incompatible job that starts
   after either check can overlap F264.

10. **Retry and resource bounds are incomplete.** Prime generation, safe-prime
    generation, cohort filling, and pair/triple filling all contain unbounded
    retry loops (`symbolic_search.cpp:187-201,220-245,730-758`). Uniqueness and
    balance are checked for accepted cohorts, but there is no deterministic
    retry-exhaustion gate. The outer timeout can invalidate a run; it does not
    prove construction reaches 5,280 inputs. The 4 GiB limit applies only to
    production, not self-test or benchmark, and the 1 GiB check happens only
    after production and counts `out_dir` but not logs
    (`remote_run.sh:32-35,56-69`). This does not implement the stated runner-wide
    memory and uncompressed-output limits.

11. **Global-decoy accounting and conjugation controls are incomplete.** The
    packet says all named exact zeros are counted separately and that ordered
    coordinate and carry features are reported in both conjugate bases
    (`PREREGISTRATION.md:147-150,203-205`). Per-input code counts associator,
    inverse-trace, and conjugacy checks. The one-time identity miner covers
    trace cycle, Fricke, and Cayley--Hamilton, but determinant multiplicativity
    is absent and the output does not provide the frozen separate accounting.
    The conjugation control emits only selected coordinate differences and
    emits no carry features in both bases (`symbolic_search.cpp:811-824`).

## Checks that did pass

- **PASS:** Canonical matrix multiplication carries, second carries, lift
  divisions, the ordered associator, its sign, and its exact quotient match
  `ALGEBRA.md` and use checked exact division.
- **PASS:** The determinant, unit Cayley--Hamilton, and Fricke numerators are
  the named `N^2` quotients and are checked for exact divisibility.
- **PASS:** The quadratic resultant implementation is exactly
  `(p-q)^2+(s-t)(s*q-t*p)`. The synthesized pair and triple determinant
  formulas otherwise match the frozen formulas.
- **PASS:** Conditional on a global return, the prime-by-prime order stripping
  logic is correct: `g=N` deletes a prime, a proper gcd factors `N`, and in a
  no-factor branch `g=1` retains the required prime. The split implication
  itself is valid for odd `N` once an invertible discriminant root is verified.
- **PASS:** Reduced noncommutative word enumeration has lengths 1 through 7,
  forbids adjacent inverse letters, preserves multiplication order, and gives
  `4*(1+3+...+3^6)=4,372` words per profile and 8,744 per input.
- **PASS:** The core P205 templates have count
  `1+30+binom(30,2)+1=467`, use `n=bitlength(N)`, and evaluate `V^n` modulo
  `s_p,s_q`, which preserves the two gcds. Factor labels enter after the public
  atom/candidate pass.
- **PASS:** Accepted cohort rows enforce the declared factor bit length,
  primality, `p<q<2p`, safe-safe structure, and pair uniqueness across cohorts
  at a fixed size. The fixed counts sum to 5,280 if the unbounded generators
  terminate.

Because blocker 1 alone makes the mandatory first validation fail, and
blockers 2-11 show independent algebra/specification/workflow drift, the
authenticated frozen packet must be invalidated without execution. No frozen
artifact or durable ledger was edited by this audit.
