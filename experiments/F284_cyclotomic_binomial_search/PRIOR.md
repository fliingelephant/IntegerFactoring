# F284 prior-work retrieval: specialized cyclotomic and q-binomial evaluation

## Purpose and retrieval method

This note records only the closest existing repository material for the
question: can a specialized cyclotomic or Gaussian/q-binomial identity give a
compact evaluator or a factor-asymmetric residue outside the old generic
q-factorial state models?

The release research reader was queried for `Gaussian binomial`, `q-binomial`,
`q-Lucas`, `root of unity`, `cyclotomic`, `Pochhammer`, `factorial evaluator`,
`divided difference`, `normalized difference`, `Lucas's theorem`, and
`Stirling`. Relevant heads and bodies were then opened individually. Historical
status labels below are reported metadata, not a new correctness audit.

No record contained the exact phrases `Gaussian binomial`, `Gaussian
coefficient`, `Gaussian polynomial`, or `q-Lucas`. The only explicit
`q-binomial` hit was the formal shifted-state calculation in the F14 torus
q-factorial packet. This search result does not prove that no equivalent idea
occurs under different notation.

## 1. Torus q-factorial evaluator: P20, P21, and F14

Exact sources:

- `{ kind = "record", path = "PROVED.md", id = "P20" }`
- `{ kind = "record", path = "PROVED.md", id = "P21" }`
- `{ kind = "file", path = "experiments/F14_torus_qfactorial_evaluator/RESULT.md" }`
- `{ kind = "file", path = "experiments/F14_torus_qfactorial_audit/RESULT.md" }`
- `{ kind = "file", path = "experiments/F14_torus_qfactorial_reconstruct/RESULT.md" }`

P20 defines

\[
S_m(a)=\prod_{d=1}^{m-1}(1-a^d)^{m-d}.
\]

It records an exact conditional reduction: a uniform evaluator for
`S_m(a) mod N` with cost polynomial in `log N + log m` gives an all-input
classical Las Vegas polynomial-time factorer. The evaluator itself is not
supplied.

P21/F14 establish boundaries only for named representations:

1. A positive product of binomials `1-a^L` that realizes the exact order
   threshold over every finite field must contain every exponent in
   `(M/2,M]`, hence at least `ceil(M/2)` distinct exponents.
2. The literal two-child q-Pochhammer addition law reaches `M` singleton
   leaves.
3. Explicit dense shift-capable coefficient states have linear or quadratic
   width in the block length.
4. Literal constant-work-per-equal-floor cyclotomic grouping has at least
   `2 floor(sqrt(M))-1` groups, and an unweighted group product loses the
   nonconstant weights.
5. A nonzero characteristic-zero polynomial vanishing at all roots of unity
   of order at most `M` has large degree.

The hostile audit makes the key scope correction for F284: formal coefficient
counts do not bound a sparse representation after specializing the base and
modulus, and nonconstant cyclotomic weights do not rule out a succinct
division-free weighted aggregate. P21 proves no arithmetic-circuit or general
evaluation-time lower bound. Sums, rational functions with audited
denominators, characteristic-dependent identities, specialized cancellations,
and other circuits remain outside the result. Therefore a genuinely
specialized q-Lucas or root-of-unity evaluation is not excluded merely by F14.

## 2. Ordinary Lucas/binomial factor asymmetry: P215

Exact sources:

- `{ kind = "record", path = "PROVED.md", id = "P215" }`
- `{ kind = "file", path = "experiments/F249_shifted_binomial_threshold_gate/STATEMENT.md" }`

On the balanced distinct-odd-semiprime promise, write

\[
N=pq,\quad p<q<2p,\quad B=\lfloor\sqrt N\rfloor,\quad
H=\lfloor B/2\rfloor,\quad s=B-p.
\]

P215 records the ordinary-Lucas identity

\[
\binom{rN+c-1}{B}\equiv rq\binom{c-1}{s}\pmod N
\]

after screening `gcd(r,N)`, for `1 <= c <= H`. Consequently the endpoint
`c=H` has gcd `q` with `N`, provided the coefficient residue can be evaluated.
The record explicitly does not provide a numerical-QP evaluator. It relates
the endpoint to the central-binomial or upper-half factorial gate and leaves a
new composite-modulus evaluator as the exact gap.

This is the closest existing Lucas specialization. It is ordinary Lucas, not
q-Lucas, and it gives no prior negative result about Gaussian binomial
coefficients at roots of unity.

## 3. A specialized root-of-unity norm exists, but only as an unaudited candidate

Exact source:

- `{ kind = "file", path = "experiments/F204_beta2_qproduct_fastforward_boundary/STATEMENT.md" }`

F204 is labeled a frozen proof-only candidate awaiting hostile audit. It studies
the different infinite product

\[
P(q)=\frac{(q;q^4)_\infty}{(q^3;q^4)_\infty}.
\]

For an odd prime `ell`, a primitive `ell`-th root `zeta`, and
`epsilon=chi(ell)`, it states

\[
\prod_{j=0}^{\ell-1}P(\zeta^j q)
=\frac{P(q^\ell)^{1+\ell\epsilon}}
       {P(q^{\ell^2})^\epsilon}.
\]

Its logarithmic derivative gives a local Euler recurrence for the associated
coefficient. At a target index `N`, contraction occurs only when `ell` divides
`N`, where `gcd(ell,N)` already factors the input; otherwise it relates the
target to a larger index. This is relevant as a concrete root-of-unity norm,
but it is not a Gaussian-binomial result, not an evaluator, and not verified
enough to use as a premise.

## 4. Normalized divided differences and lift boundaries

Exact sources:

- `{ kind = "record", path = "PROVED.md", id = "P224" }`
- `{ kind = "record", path = "PROVED.md", id = "P227" }`
- `{ kind = "record", path = "PROVED.md", id = "P230" }`
- `{ kind = "record", path = "PROVED.md", id = "P231" }`
- `{ kind = "file", path = "experiments/F274_characteristic_shift_transfer_boundary/STATEMENT.md" }`
- `{ kind = "file", path = "experiments/F277_integer_valued_difference_boundary/STATEMENT.md" }`
- `{ kind = "file", path = "experiments/F283_shifted_normalized_difference_evaluator_boundary/STATEMENT.md" }`

P224/F274 prove that an order-`B` forward difference of an
integer-coefficient polynomial contains the exact integer factor `B!`. This
does not cover integer-valued rational polynomials such as `binom(X,B)`, and it
is not an evaluator lower bound.

P227/F277 address that excluded integer-valued seam. A high difference shifts
Newton coefficients, while

\[
\frac{\Delta^B X^m(0)}{B!}
=\left\{\begin{matrix}m\\B\end{matrix}\right\}
\]

is a remote Stirling coefficient. Short-side binomial quotients are
factor-first; the long-side remote binomial/Stirling range remains open. F277
explicitly proves no general classification of Lucas or Kummer constructions
and no lower bound for integer-valued-polynomial or canonical-division
circuits.

P230 is a conditional random-shift splitter inspected by the root as background.
P231/F283 show only that the immediate lift of the raw difference to `N^2`,
followed by exact division by `N`, removes the guaranteed prime multiplier.
They explicitly leave a different higher-lift decoder and a compressed
restricted-domain exact-division decoder open. Thus a proposed cyclotomic or
q-binomial lift must explain what factor-asymmetric information survives its
normalization; it is not excluded solely because the immediate `N^2` lift
fails.

## 5. Fast factorial and interval-product interfaces

Exact sources:

- `{ kind = "record", path = "PROVED.md", id = "P221" }`
- `{ kind = "record", path = "PROVED.md", id = "P223" }`

P221 leaves open a uniform evaluator

\[
(a,b,d)\longmapsto\prod_{j=a}^{b}j\pmod d
\]

with quasipolynomial cost in `log b + log d`. Such an evaluator is already a
factoring-hard interface on the balanced core. P223 closes only four explicit
symbolic grammars: algebraically independent child-product summaries, one
Smith/determinant presentation, a rising-factorial discriminant, and one
literal dyadic cross-resultant recursion. It explicitly leaves
characteristic-dependent identities, adaptive algorithms, special affine
transitions, succinct matrix methods, and general circuits open.

## Historical workflow prose

F274, F277, and F283 contain statements such as “no larger C++ search is
justified” inside their named grammars. Under the current repository policy,
these are historical decisions, not current instructions. Their mathematical
content applies only to the stated models. They do not prohibit the specialized
cyclotomic/q-binomial question posed for F284.

## Proven Sage launch pattern

The most practical retained Sage wrapper located is:

- `experiments/F04_psc_reconstruct/run_with_timeout.py`
- run record: `experiments/F04_psc_reconstruct/RUN_MANIFEST.md`

Its command interface is:

```sh
python3 experiments/F04_psc_reconstruct/run_with_timeout.py \
  --run-id <ID> \
  --timeout-seconds <SECONDS> \
  --log <LOG_PATH> \
  --status <STATUS_JSON> \
  -- sage <SCRIPT.sage> <ARGS...>
```

The wrapper creates a separate process group, records the exact command, UTC
times, duration, timeout flag, exit code, disposition, and log SHA-256, sends
`SIGTERM` on timeout, and escalates to `SIGKILL` after five seconds. It sets the
correct Sage state variable `DOT_SAGE`; the retained F04 copy uses
`/private/tmp/f04_psc_reconstruct_sage`. A future F284 wrapper should use its
own packet-specific directory rather than reuse that hard-coded path. Historical
notes record that `SAGE_DOT_SAGE` was ignored and that the default Sage cache
could be unwritable.

Recorded successful Sage runs through this wrapper include:

- `global_discovery.sage`: 66.404 seconds, timeout 900 seconds, exit 0;
- `local_certificate.sage`: 3.977 seconds, timeout 600 seconds, exit 0; and
- the non-authoritative `probe_exact.sage` replay: 3.039 seconds, timeout 60
  seconds, exit 0.

No Sage or research computation was launched while preparing this note.
