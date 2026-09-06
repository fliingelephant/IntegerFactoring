# F261-D02 V2 fresh hostile pre-run audit

## Verdict

**PASS.** The authenticated V2 packet repairs every decisive V1 failure and
is internally consistent as a frozen, theorem-only finite experiment. No
blocking mismatch was found among the algebra, preregistration, source,
runner, and prelaunch manifest.

This is a static verdict only. I did not compile or execute the source, run a
self-test or benchmark, generate a cohort, or write experiment output. The
mandatory target gates remain unexecuted. This verdict does not promote the
packet, prove a small-carry law, execute the factor bank, or imply an
all-input factoring algorithm.

## Authentication and freshness

I computed all five requested SHA-256 values before reading the V2 files.
They match exactly.

| Artifact | SHA-256 | Result |
|---|---|---|
| `V2_ALGEBRA.md` | `e9894455ae9cfed71a984591c88cc3b45d23a885f3c60216ca0bfdc267792e8d` | PASS |
| `V2_PREREGISTRATION.md` | `0b65705c4135b0e653c5cef0221d7725f1ea354468b897160a75409f916dd68b` | PASS |
| `V2_search.cpp` | `ad3827f82e1b350c5887ba2094f5be8d360a2e858090c6a9dd25558b81e1d095` | PASS |
| `V2_remote_run.sh` | `310a4377270408848c2035b88df5bf7166cd5eb1d9f8102bce8ca5df74bf74ae` | PASS |
| `V2_PRELAUNCH_MANIFEST.md` | `1bfe3849ee1ba307d3ae5cf251c3d717468b6cb8e5f811dcd2fdb14113ce2432` | PASS |

I read `AGENTS.md` and `PROMPT.md` before reconstructing the packet. I did
not read any prior F261 audit or blind reconstruction until after reaching
the independent PASS above. The post-conclusion provenance check is recorded
below. This audit file's own hash is reported with the handoff because a file
cannot contain its own SHA-256.

## V1 FAIL repairs

### 1. No-prefix endpoint: PASS

The theorem and preregistration now define `R=1` and `a=b=0`, with all
congruences interpreted in the unique class modulo one. `prefix_data`
returns before calling `inverse_power_two`, and the self-test observes that
the inverse branch was not entered. The nontrivial `R>=2` branch still uses
the odd factor prefix and verifies its public companion against the hidden
label. Thus equations (7)--(10) and the no-prefix
`O(U^3+C U^2)` bound have a literal implementation.

### 2. Predictor ranking: PASS

The frozen third key is the lower order statistic at index
`floor((L-1)/2)`. `lower_median_key` implements this exact integer rule, and
`better_score` compares it only after the minimum cell fraction and total
train hits. The minimum fractions are compared by exact cross products.
For the 798 train rows, the selected entry is index 398. Monotonicity of
`log2(1+x)` makes this the same order statistic after the stated transform;
there is no floating-point or even-sample ambiguity. The self-test contains
an even-list witness whose lower-median order differs from the V1 two-middle
raw mean. Predictor selection uses only factor sizes through 40 bits, and
the heldout cells are reported only after that selection.

### 3. Product surrogate: PASS

The prose and source both use

```text
K0=floor((u*floor(sqrt(N))+B/2)/B).
```

The same `public_sqrt_center` function is used by the predictor and the
common-center diagnostic. The exact regression
`N=11009,B=128,u=19,K0=15` is in the self-test, together with a check that
the real-square-root alternative lies across the rounding boundary.

### 4. Worker-aware projection: PASS

The runner fixes or load-reduces one worker count, passes that exact count to
`--preflight`, and later passes the same count to the full run. Preflight
computes a one-worker scan projection, divides it by `0.75*workers`, adds the
serial generator projection, and rejects totals above 14,400 seconds. The
self-test checks the 1-, 2-, and 8-worker values. The old fixed-four-worker
projection is absent.

### 5. Diagnostic and operational boundary: PASS

Every true-carry cap column is named `oracle_hit_*`; first hits use
`first_oracle_*`; summary cell successes use `oracle_hits_n2`. The summary
also emits

```text
executes_factor_bank=false
oracle_hit_semantics=hidden_label_true_carry_not_executed_factor_bank.
```

The preregistration explicitly groups all hidden-label carry, center, rank,
and inverse-window measurements as oracle diagnostics. Operational prefix
data are limited to `(N,B,H,R,a,b,n)` after `a` is supplied. The terminal
flag and bank upper bounds use public quantities. No hidden diagnostic is
described as an executed factorization.

## Theorem and source reconstruction

### Exact centered-carry theorem: PASS

Separate round-half-up centers give residues in `[-B/2,B/2)`, including the
documented negative half-tie. From `N=1+B*H`, direct expansion gives

```text
c=(x*y-u^2)/B,
u*T=u^2*H+Kp*Kq*B-c,
T=Kp*q+Kq*p.
```

Substitution gives the quadratic
`Kq*X^2-T*X+Kp*N=0` and discriminant
`(Kp*q-Kq*p)^2`. The stated quadratic, linear, zero-center, integrality, and
exact-division verification rules are sound. The public factor endpoints
and their rounded center intervals follow from
`sqrt(N/2)<p<sqrt(N)<q<sqrt(2N)` and match `center_intervals` and
`bank_bound` exactly.

For a supplied dyadic prefix, reducing the trace gives
`T=Kp*b+Kq*a (mod R)`. The interval obtained from `c=A-u*T` contains at
most `1+floor(2C/(uR))` values in one residue class. Multiplying by the exact
public center-interval cardinalities and summing through `U` gives the
implemented upper bound and the stated
`O(U^3+C*U^2/R)` asymptotic bound.

For odd `u` and `R>=2`, the inverse-map construction has exactly `B/R`
centered candidates. The signed `z` endpoints, odd-step public permutation,
true-point inclusion check, carry integrality, complete-versus-sampled mode,
and zero sentinel agree with the preregistration.

All frozen magnitudes fit their declared integer types: products and trace
numerators stay within signed 128-bit range on the 60-bit-factor schedule;
candidate bounds and theory-scale values use `cpp_int`.

### Direct-`T` scope: PASS

`bank_bound` evaluates only the theorem's cardinality upper bound. It does
not enumerate center pairs, residue-compatible `T` values, discriminants,
roots, or candidate divisors. `carry_point` computes the hidden true trace
only to check scan invariants. Decoder arithmetic occurs only in the small
self-test. `EXECUTES_FACTOR_BANK` is false. Thus no cohort field is a bank
hit, and the source matches the theorem-only scope.

## Cohorts, diagnostics, and output

### Frozen cohorts and caps: PASS

The factor sizes, exact-bit prime tests, balance and zero-defect filters,
train/heldout split, SplitMix tags, cohort predicates, and cell sizes match
the preregistration. The four per-cell caps are exactly 20,000,000,
50,000,000, 20,000,000, and 200,000,000. Exhausting a cap throws instead of
substituting a cohort. A global ordered prime-pair set skips repeated moduli,
and the final task-count assertion requires 1,368 distinct rows. The edge
stream uses the stated restricted odd interval and is described as a modulo
map, not as exactly uniform. The separate consecutive-prime audit enumerates
all eligible adjacent pairs for factor bit lengths 8 through 22 and does not
enter training or heldout scores.

The scan reports all three multiplier minima, all four oracle cap counts and
first hits, cell maxima with exact factor witnesses, predictor outcomes,
terminal flags, and both exact bank bounds. The inverse study chooses one
worst `U3` row per factor-size/cohort cell and writes all three nontrivial
prefix studies. The fixed rank primes, monomial sets, raw-rank convention,
half-tie convention, and valuation sentinel agree across prose and source.

### Self-tests: PASS statically

The self-test covers every named V2 repair: the `R=1` branch, exact lower
median and V1-distinguishing witness, floor-square-root product regression,
worker-dependent 75-percent projection, oracle schema, and false bank
execution constant. It also checks a nontrivial prefix, half ties, negative
carries, prefix congruences, signed residue counts, the quadratic
discriminant and integral-root endpoint, the linear endpoint, and monomial
counts. These checks are present but remain unexecuted in this audit.

### Runner and validation gates: PASS statically

The runner records host resources, refuses a detected F258/F259/F260
process before compilation, requires at least 8 GiB available memory and
5 GiB free disk, reduces workers under its frozen high-load rule, compiles
the authenticated V2 source as C++17, runs the self-test, and runs preflight
with the actual worker count. Preflight requires a nonzero separately tagged
60-bit generator hit for every cohort, including safe-safe, before applying
the 14,400-second projection gate. The full run uses `nice -n 15`, a
14,400-second timeout, at most eight workers, and a 4 GiB virtual-memory
limit. The runner rejects output at or above 1 GiB and hashes all four
declared output artifacts.

The output paths and experiment identifier are consistently `F261-D02`.
The summary preserves the selected predictor names separately from all
diagnostic cell results, so only train-selected predictors can be interpreted
as heldout leads. The per-size, per-cohort records are sufficient to apply
the frozen persistence and baseline gates. Exact bank bounds and terminal
flags remain separate from oracle carry successes. Finite successes,
failures, ranks, and inverse-map samples are explicitly barred from
asymptotic interpretation.

## Post-conclusion V1 provenance check

Only after the independent verdict did I read the preserved V1 failure
record. Its four decisive defects are exactly the no-prefix inverse
convention, median rule, product-surrogate center, and fixed-four-worker
projection; its required interpretation repair is the oracle-hit versus
factor-bank boundary. The V2 checks above address all five. The three V1
secondary exactness issues are also repaired: modulo mapping is not called
uniform, the zero-valuation sentinel is frozen, and surrogate ranks are
called raw ranks.

All preserved hashes in `V2_PRELAUNCH_MANIFEST.md` match:

| V1 artifact | SHA-256 |
|---|---|
| `ALGEBRA.md` | `df27b6557ac2fe2ae29a495241c66741e864f8d667237f04855aa82f499aa67f` |
| `PREREGISTRATION.md` | `ae0e04eb7b1593795560eae3444c753ed07c4e4c0758c41386562fb72779c7f1` |
| `search.cpp` | `9af35178e041b3d02f4bf33134b451b9fe938cf8235ae450fb8df7f0027b1e6d` |
| `remote_run.sh` | `07fd9d53c1e2f08b647b24272908f1487ed1ba38657e7aef1a196d4f389137f3` |
| `PRELAUNCH_MANIFEST.md` | `110aee72fd78731f354643ccbc9517784e3ee28a8ea5c454069d9e959a6f70e8` |
| `HOSTILE_AUDIT_THEOREM.md` | `a2b628035202ae57e9ee2169bc70e4ba329a8057c9cb176a8757ba0c6a2b9558` |
| `FRESH_HOSTILE_AUDIT.md` | `f05fb46595c6b5ec5b277fba5e0ac938a63a5d1a42fc2d2606b70cf8f91a1a71` |
| `BLIND_RECONSTRUCTION_THEOREM.md` | `0ea8459bd471791d11888e4a14b6fadd1c50ed4305b501c660bbb1a80f5f6e22` |

## Disposition

The frozen V2 packet may proceed to its mandatory target-side validation
sequence once F258, F259, and F260 are absent. Any hash mismatch or failed
self-test, generator benchmark, projection, resource, timeout, or output gate
must abort this hash set. A dynamic PASS would still be finite diagnostic
evidence only.
