# F268-D02 independent hostile pre-run audit

# Verdict: FAIL

frozen_manifest_sha256: 31e05f0f310ff6f0b37421ccf68634bf57bce65cb708074408dec96b7801561b

## Authentication

- The SHA-256 of the exact `FROZEN.sha256` bytes is the coordinator-supplied
  digest above.
- All eleven entries in that manifest authenticate.
- `PROVENANCE.md` therefore authenticates as frozen input.
- The immutable D01 `FROZEN.sha256` bytes hash to
  `b99d47d7ba7a01c456a0b755a5e77f42a237be73ffd6ea422e38d03b076a1cc9`,
  and every D01 manifest entry authenticates.
- D01 `SELF_AUDIT_FAIL.md` hashes to
  `8ab91efa95e1aa20f0985f80c28790340987d4b61f3bbb662707587a4b2642c2`.
- The D01 packet directory contains only its ten frozen inputs, its manifest,
  and `SELF_AUDIT_FAIL.md`. It contains no corpus, binary, log, preflight,
  selection, evidence, label-audit, or result artifact.
- D02 `label_audit.cpp` directly includes `<tuple>` at line 10, before its
  `std::tie` use at lines 206--208. Static comparison against D01 finds the
  header repair and packet/output version changes in the C++ and runner.
  `FAMILY_SYNTAX.tsv` is byte-identical. The other changes are D02 headings,
  version/provenance text, hashes, and the new frozen provenance file.

## Decisive cohort failure

The frozen cohort constructor does not implement the frozen attempt law.

`PREREGISTRATION.md` fixes: `Prime requests have 200,000 candidates.` The
marker constructor instead calls

```text
random_prime_class(rng, bits, 24, 13, 128)
random_prime_class(rng, bits, 72, 11, 128)
```

at `corpus.cpp` lines 285--286. These explicit arguments override the
function's 200,000-candidate default. Each marker prime request therefore has
only 128 candidates. This is not only an implementation detail: it changes
which of the 4,096 registered pair attempts reach the marker tests and can
change every marker cell and declared shortfall. The generated corpus would
not be the preregistered finite cohort. Gate 9 fails.

The repair requires a new frozen packet. Changing the two caps after seeing
any generated corpus is not permitted.

## Independent runner failure

The all-F265-process launch condition is not enforced. `remote_run.sh`
`refuse_overlap` matches only an F265-D01/D02 command containing `search` or
`remote_run`, plus `f265_search`. A visible standalone process such as
`f265_corpus`, `f265_label_audit`, an F265 validator, or an F265 compiler does
not match. Thus the runner can compile or launch while an F265 process is
active, contrary to the frozen precondition that every F265 process has
ended. The external precondition remains mandatory, but the claimed runner
gate is incomplete. Gate 10 fails independently.

## Static checks that survived

No source was compiled or executed, no corpus was generated, no remote was
accessed, and no future output was inspected. The following checks do not
cure the failures above.

- For odd `N` and a canonical unit `a`, each of the five exponents is positive,
  even, and coprime to `N`. Hence `U_E(a)` is a unit in `[1,N^2)`, `Y_E(a)` is
  a unit in `[1,N)`, and `Y_E(a)^2 = U_E(a) (mod N)`.
- Direct expansion modulo `N^2` gives the stated multiplication, inverse,
  power, and complement congruences. Exact divisibility and signs match the
  C++ paths. Their unit multipliers give the claimed gcd equalities. Only the
  scalar `U` rows enter P66.
- If `u=gx`, `v=gy`, and `g=gcd(u,v)`, then `x,y` are coprime and `uv` is a
  square exactly when both are squares. The positive root is `g*s*t`. The
  source tests every singleton and unordered pair before decoding.
- The bank chronology fixes all rows after stage 1, completes stages 2--4,
  completes the low-support scan, retains useful low-support certificates,
  inserts only verified global signs into the decoy span, authenticates P66,
  and emits residual relations only on the no-useful branch. Later P66 and
  evidence rejections preserve completed useful low-support evidence.
- The gcd-free refinement preserves exact row exponent vectors and ends in
  pairwise-coprime blocks. Square blocks contribute no parity equation.
  Nonsquare blocks contribute one. Kernel construction, the low-span quotient,
  exact roots, supplied roots, normalized roots, signed gcds, and frozen
  template predicates are independently reconstructed by replay.
- The scalar canonical-section source is distinct on its stated finite scope
  from the listed principal-lift, inverse-quotient/torus, polynomial, matrix,
  elliptic, quadratic-form, decoder-only, and inverse-endpoint routes. The
  packet does not claim an asymptotic factoring theorem.
- The twelve families implement the advertised 20/24 discovery and 45/48
  heldout row tiers. The syntax table advertises 45/48 maxima. All complete
  low-support tests remain inside each eligible bank.
- Search `Case` contains only public fields. Bank evaluation uses `N`, split,
  frozen syntax, and public gcd outcomes. Discovery ranking consumes arithmetic
  `BankResult` statistics without shape, factor bits, factors, markers, or
  labels. Heldout authenticates the family syntax, selection bytes, embedded
  discovery digest, both rank orders, and both selected rank prefixes before
  evaluation. Labels are separate mode-0600 outputs and enter only after
  heldout and public replay.
- Apart from the attempt-law failure above, the constructors and post-run
  label checks enforce deterministic 64-bit primality, exact factor bits,
  distinct balanced primes, global modulus uniqueness in generation,
  nonconsecutive neighbors, safe-safe factors, shifted marker gcds, four
  distinct marker primes, primitive-root tests, and explicit shortfalls.
- With all marker rows, the exact maximum is 3,440 banks, 110,224 row powers
  and singleton tests, 1,942,040 unordered pair bundles, 15,536,320 stage-3
  pair gcds, and 1,942,040 support-two tests. Also,
  `2369895 / 3316.220420 = 714.6373581524475...`; the compiled rounded rate is
  `714.637358152448`, and its twice-safety floor is about 5,435.036324 seconds.
  The gate takes the maximum of the pair-scaled, task-scaled, and empirical
  projections, adds twice corpus-generation wall time, and applies the stated
  wall, RSS, live-memory, output, zero-reject, and completed-48-row conditions.
- The preflight statically invokes real source construction, row powers, eight
  stage-3 gcds per pair, every low-support test, P66, quotienting,
  serialization, and replay. It checks the recorded count identities.
- The frozen self-tests cover SHA-256, both row tiers, unique row keys, useful
  and global low-support dispositions, preservation after resource rejection,
  a support-three relation, carry algebra, P66 decoding, and selection
  re-ranking. The runner has no Python command or source dependency.

Because a frozen cohort law and an independent launch gate fail, this packet
does not authorize compilation, corpus generation, preflight, discovery, or
heldout execution.
