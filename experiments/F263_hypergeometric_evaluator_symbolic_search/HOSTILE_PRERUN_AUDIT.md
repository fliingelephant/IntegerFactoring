# F263-D01 hostile pre-run audit

## Decision

**FAIL. Do not launch discovery or held-out cohorts from this frozen packet.**

The algebraic gate and the numerical candidate formulas are sound on the
promised balanced-semiprime rows. However, the executable does not implement
the preregistered public query bank, symbolic acceptance rules, dependency-cost
audit, or generator guarantees. The pre-freeze benchmark therefore does not
authenticate the registered experiment.

## Frozen input authentication

All supplied hashes match. `shasum -a 256 -c FROZEN.sha256` also authenticates
all 17 entries in the manifest.

```text
PREREGISTRATION.md  69cd40a40d2501fe4e9a48eaa6ef63abdcc1c947fa0ce72682907f5a36afb8c9
ALGEBRA.md           595c615bdc75b5b966999c5e1908d508e4bba8d4be4caa7abacb2474f547843b
symbolic_search.cpp  35a303ee01290313538f8d20e456fbacb46bd091a15f3b2cc93fba5ad367ba52
remote_run.sh        443f10b3f14b51528abb95b845802f51190f99af61595c0588d6aae82c6512b4
FROZEN.sha256        95eb34870050009cd281b2d27413cf5a52688d3345a21e62d19fba0aa6bd3e5f
```

## Blocking failures

### 1. The public query bank uses the factor-bit label, not `bitlength(N)`

The preregistration defines `n=bitlength(N)`. At `symbolic_search.cpp:732`,
the program instead calls `queries(domain, in.bits, ...)`, where `in.bits` is
the declared factor size. For the frozen benchmark,

```text
p = 2^60 - 93, q = 2^60 - 33, bitlength(pq) = 120,
```

but the query constructor receives 60. Thus it uses the `60` and `60^2`
length scales instead of `120` and `120^2`. This is not the frozen bank in
`PREREGISTRATION.md:111-136`. The factor size is publicly recoverable on these
exact-bit balanced cohorts, but that fact does not make the two frozen banks
equal. It also means cohort metadata participates in bank construction before
the advertised label-only verification stage.

### 2. The symbolic search and recurrence acceptance are not the frozen search

- Both modular nullspaces are computed, but only the `P1` basis is rescaled and
  authenticated (`symbolic_search.cpp:510,527-528`). The `P2` basis is never
  searched.
- The sparse search stores one combination per 128-bit digest
  (`symbolic_search.cpp:512-525`). It does not store the full modular column
  vector or all members of an equal-sum class. Consequently it does not search
  every normalized support-at-most-four relation as registered; later members
  of one class are compared only with the first member.
- The dyadic miner uses only `affine_product(4,2,...)`
  (`symbolic_search.cpp:464-495`). It does not authenticate against both affine
  families as required by `PREREGISTRATION.md:102-106`.
- The dyadic miner returns only `0` or `1`. It does not retain each recurrence,
  its order, degree, coefficient height, or dependency class. Adjacent
  recurrence output also omits height and dependency class.

The frozen self-test result `dyadic=0` avoids a current false positive. It does
not repair the false-null search coverage or the missing acceptance logic.

### 3. Dependency-cost classification is absent

The source contains no representation of `descriptor`, `short_scan`,
`recursive_merge`, `oracle_block`, or `full_scan`. It also does not implement
or report the five registered non-operational controls and their exact costs.
The shortcut classifier at `symbolic_search.cpp:542-545` only asks whether the
rendered relation contains `P.` and lacks `L.` or `R.`. It does not check for
one unit-coefficient parent target, operational remaining terms, or a bounded
expanded dependency DAG. Therefore a future nonzero `shortcuts` value would
not satisfy the registered shortcut definition.

### 4. Frozen cohort caps and invariants are not enforced on all paths

- The consecutive-prime path recursively changes `salt` when the next prime
  crosses the bit boundary (`symbolic_search.cpp:761`). It has no per-row cap
  and replaces the attempted row instead of aborting.
- The safe-safe path retries equality once, but does not reject or abort if the
  third deterministic safe prime still equals `p`
  (`symbolic_search.cpp:760,763-764`). Thus `p<q` and distinctness are not
  enforced by the production generator on that path.
- The self-test checks a separate `accepts_pair` predicate, but production
  `make_row` does not call that predicate. The test therefore does not close
  these paths.

The deterministic arithmetic, literal hash, exact factor bit construction,
bounded-capacity predicate, duplicate-modulus set, and Miller-Rabin bases are
otherwise stable.

### 5. The resource projection and runner do not close the protocol gaps

The code contains 848 discovery rows and 1,152 held-out rows, not the 1,536 and
2,016 claimed in `BENCHMARK.md:35`. That overcount is conservative for the
implemented program. However, the benchmark used the smaller factor-bit query
bank, so it does not measure the registered bank. The projected time and leaf
count cannot authenticate that bank.

The runner does pass shell syntax checks and has an initial full-manifest gate,
overlap checks before each phase, eight-thread selection, a shared four-hour
deadline, and a 4 GiB virtual-memory limit. The following gates remain weaker
than the frozen prose:

- The 1 GiB output limit is checked only after both phases and only on
  `out_dir`; it is not an applied write limit.
- The selection checksum is created from the just-written file and immediately
  recomputed from that same file. The executable receives no expected digest,
  and `read_selection` validates only 64 distinct known names, not the exact
  file bytes, ranks, or score fields.
- Neither the executable nor the runner evaluates the four registered finite
  lead conditions. Held-out output contains scores for the complete bank and
  only marks the selected names.

## Checks that pass

- **Exact algebra, parity, and endpoints: PASS.** The inequalities imply the
  unique central numerator index `(p-1)/2` and shifted denominator index
  `B-p`. The central and shifted scan domains include the unresolved endpoints.
  The even and odd central-binomial formulas and the `B=p` cleanup case agree
  with the implementation.
- **Numerical candidate grammar: PASS.** The catalog has exactly 148 syntax
  types: 74 per family. The six jets, minors, resultants, six transfer entries,
  transfer determinants, projections, product hashes, adjacent observables,
  Smith-style divisors, and cross-block observables match the registered count.
  Their arithmetic is division-free modulo `N` before gcd extraction.
- **Gcd state handling on promised rows: PASS.** Proper and saturated gcds are
  distinguished, and a later proper gcd overrides an earlier saturated value.
  Public cleanup gcds exit before numerical evaluation. The prose says a gcd
  equal to `N` aborts, while the source falls through, but this branch is
  unreachable for `B` and `H+1` on the promised rows.
- **Static frozen checks: PASS with one local limitation.** Both shell scripts
  pass `bash -n`, and all manifest entries authenticate. A local C++ syntax
  check could not run because this Mac lacks the Boost.Multiprecision headers;
  no substitute compiler workflow was used. The authenticated target artifact
  records a successful compile of this exact source with the frozen flags.

## Scope

This audit read `AGENTS.md` and `PROMPT.md`. It used only local, read-only
static checks and small exact rederivations. It did not run a cohort, invoke the
remote host, edit a frozen file, or edit a durable-state ledger.
