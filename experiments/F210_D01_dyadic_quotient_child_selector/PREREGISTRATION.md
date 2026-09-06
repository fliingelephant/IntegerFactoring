# F210-D01 preregistration — live dyadic quotient-child selector

## Status

This packet is frozen for root-agent review before registration or launch.
It has not run locally or remotely. It makes no theorem claim.

## Closest prior route and material difference

The closest numerical route is F205-D01. F205 factors the two root-level
integers

`(N-1)/2` and `N-floor(sqrt(N))^2`

once per input. It then searches scalar decision stumps and a fixed power
bank. F210-D01 does not repeat that experiment. It follows the *true P175
reciprocal prefix* through every live dyadic stage. At each stage it factors
the four exact branch-relative quotient integers defined below. Its selector
menu is branch-equivariant. It compares the two candidate-lift transcripts
instead of fitting thresholds to root-level scalar features.

The closest proof route is P179. P179 defines the two product-compatible
next quotient states and proves that they can coalesce. F210-D01 adds the two
crossed-lift odd quotients. It asks whether the complete factorizations of
all four public integers give a deterministic next-bit rule or a direct gcd
transition on the finite cohorts.

## Fixed promise and granted state

Every input is a balanced squarefree semiprime

`N=p*q`, with `p<q<2*p` and `N == 3 mod 4`.

At stage `t>=1`, put `m=2^t`. The experiment is granted the correct public
state

`u = p^(-1) mod m`, with `1 <= u < m`.

The hidden factors can generate `u` and the target next bit. After this
grant, the public constructor accepts only `(N,t,u)`.

The two reciprocal lifts are

`u_j=u+j*m`, for `j in {0,1}`.

For each lift, the public constructor computes canonical odd residues modulo
`2*m`:

`x_j = u_j^(-1) mod 2*m`,

`y_j = N*u_j mod 2*m`.

Thus `x_j*y_j == N mod 2*m`. Define the two compatible quotient children

`K_j = (N-x_j*y_j)/(2*m)`.

The other reciprocal lift gives the crossed residue. Define

`H_j = (N-x_j*y_(1-j))/m`.

The crossed product is congruent to `N+m mod 2*m`, so every `H_j` is an odd
integer. The stage range below ensures that all four quotients are positive.
Exactly one `j` equals

`(p^(-1) mod 2*m - u)/m`.

This target is the next P175 reciprocal bit.

The source checks every displayed divisibility, parity, positivity, and
coprimality identity before it factors a child. A failed identity aborts the
run. These checks use no target bit.

## Fixed stage range and recursion cohorts

Let `n=N.bit_length()` and

`t_terminal=(n-1)//4`.

The experiment evaluates every stage

`1 <= t < t_terminal`.

This is the chain needed to reach the quarter-length P175 terminal. Put

`eta=1/8` and `t_safe=ceil(n/8)`.

The rows are separated before rule selection:

- `early_unsafe`: `t<t_safe`;
- `late_safe`: `t>=t_safe`.

For a late row, each quotient is below `N/m`. Hence its bit length is at
most `(1-eta)*n+O(1)`. Factoring all four children has fixed branching and
fixed-ratio contraction. It is compatible with numerical-QP recursion if
the enclosing routine is valid on arbitrary smaller integers.

For an early row, the four calls can all have `n-O(t)` bits. F210-D01 makes
no QP recursion claim for that cohort. Early rows are discovery evidence
only. This separation is fixed before the run. The experiment does not
misapply the valid one-child recurrence

`T(n) <= T(n-1)+QP(n)`.

## Fixed input cohorts

The random generator is byte-for-byte specified in the frozen source. It is
the same deterministic generator used by F205-D01. This permits paired
comparison with a prefix of the F205 cohorts without reusing F205 features.

- Training: 2,000 accepted inputs. The smaller factor has 12 through 17
  bits. Seed: `20501`.
- Holdout: 1,000 accepted inputs. The smaller factor has 18 through 23 bits.
  Seed: `20502`.
- Small counterexample scan: all accepted prime pairs with `p<=500`.

Acceptance uses only the balanced-semiprime promise and `N mod 4 == 3`.
It does not filter by prefix, next bit, factorization pattern, action result,
or cohort size. The train and holdout factor-bit ranges are disjoint. All
stages from one `N` remain in the same split.

The source hashes each ordered pair list and emits the hashes before child
construction starts.

## Public child factorizations

For each stage, `public_stage(N,t,u)` computes `x_0,x_1,y_0,y_1`, the four
quotients, and complete SymPy factorizations of

`K_0,K_1,H_0,H_1`.

For each child it records the exact value, bit length, `omega`, `Omega`,
divisor count, radical, Euler phi, Carmichael lambda, smallest prime factor,
largest prime factor, and the counts of support primes in the four odd
classes modulo eight.

For candidate `j`, the fixed branch score vector also records:

- the sum, maximum, and product of the `K_j` and `H_j` versions of each
  multiplicative statistic;
- `gcd(K_j,H_j)`, `gcd(rad(K_j),rad(H_j))`, and support intersection size;
- the same three overlap values between `K_j` and `H_(1-j)`;
- the Euclidean quotient and remainder of the larger of `K_j,H_j` by the
  smaller;
- exact gcds of `x_j`, `y_j`, `x_j-y_j`, and `x_j+y_j` with the two child
  radicals; and
- the fixed modular-action transcript below.

No numeric threshold is learned for these features.

## Fixed public action bank

The action bank is evaluated independently for candidate zero and candidate
one. It never receives `p`, `q`, or the target bit.

For branch `j`, its bases are the distinct residues modulo `N` from

`2,3,5,x_j,y_j,K_j,H_j,rad(K_j),rad(H_j)`

and the four smallest plus four largest primes in
`support(K_j) union support(H_j)`.

Its exponents are the distinct positive integers from

`K_j,H_j,rad(K_j),rad(H_j),phi(K_j),phi(H_j),`

`lambda(K_j),lambda(H_j),gcd(lambda(K_j),lambda(H_j)),`

`lcm(lambda(K_j),lambda(H_j))`,

plus `K_j/ell` and `H_j/ell` for the two smallest plus two largest support
primes `ell` that divide the relevant child.

For every base, it first tests `gcd(base,N)` and `gcd(base-1,N)` and
`gcd(base+1,N)`. For every base/exponent pair, it computes the public residue
`z=base^exponent mod N` and tests `gcd(z-1,N)` and `gcd(z+1,N)`.

The complete transcript records the number of proper-factor hits, up to the
first 16 proper-factor certificates, global `+1` and `-1` returns,
nontrivial returns, the first certificate in the fixed iteration order, and
the minimum exponent bit length for each return type. Any proper factor is
checked by exact division of `N`. Rows with any proper-factor action are
excluded from selector training because the action has already solved that
parent.

## Frozen selector menu

The selector menu contains no decision tree, regression, neural model, or
learned numeric threshold.

For every named scalar in the branch score vector, it contains these two
oriented rules:

- choose the candidate with the smaller value;
- choose the candidate with the larger value.

Ties choose candidate zero for the first orientation and candidate one for
the flipped orientation. The menu also contains two orientations of these
fixed lexicographic signatures:

1. the ordered factorization signatures of `(K_j,H_j)`;
2. the ordered union-support signature;
3. the full action-count signature; and
4. the concatenation of all three signatures.

Finally, fixed public baselines use the bits `N[t]`, `N[t+1]`, `u[t-1]`,
the parity of `t`, and which candidate has the smaller `abs(x_j-y_j)` or
the smaller `x_j+y_j`. Both prediction orientations are present.
Constant-zero and constant-one baselines are also present.

Training selects one rule separately for `early_unsafe` and `late_safe` by
maximum balanced accuracy. A canonical JSON encoding breaks ties
lexicographically. The rule is then frozen before its disjoint holdout rows
are scored. The source also reports each selected rule by stage, but it does
not select a different rule per stage.

## Preregistered interpretation

For each recursion cohort, the selected holdout rule receives one verdict:

- zero errors: `finite_exact_selector_candidate`;
- at least one error and balanced accuracy at least 0.60:
  `correlation_lead`;
- balanced accuracy below 0.55: `fixed_menu_null`;
- otherwise: `weak_inconclusive`.

Any error is an exact counterexample to universality of the selected rule.
Finite perfection is not an unbounded theorem.

The direct action bank receives a separate holdout verdict in each recursion
cohort:

- no failures: `finite_exact_action_candidate`;
- at least one failure and success rate at least 0.10: `action_lead`;
- success rate below 0.05: `fixed_action_null`;
- otherwise: `weak_inconclusive`.

Any failure refutes universality of the exact action bank. A positive action
is already a factor certificate and is not treated as a prediction.

The primary constructive outcome requires one of these events on the
`late_safe` holdout cohort:

1. a finite exact action candidate; or
2. a finite exact branch selector whose selected branch is then the only
   recursively retained quotient state.

Even such an outcome remains a finite lead until a proof supplies the
unbounded rule and the full recursion invariant. No early-cohort outcome is
called a QP construction.

## Outputs and preserved counterexamples

The result JSON and compressed JSONL preserve:

- every public stage record and hidden audit label;
- pair-list hashes and exact row counts;
- action success and failure counts by stage and recursion cohort;
- the selected rules, train and holdout metrics, and the top 20 training
  rules with their holdout scores;
- the smallest action-bank failure in each recursion cohort;
- the smallest error of each selected rule;
- every quotient coalescence `K_0==K_1` and every crossed coalescence
  `H_0==H_1`; and
- all invariant-check failures, which abort rather than being discarded.

Hidden `p,q` appear only in the pair generator, `hidden_label`, and audit
output. They never enter `public_stage`, child factorization, feature
construction, action construction, rule prediction, or public row
eligibility.

## Remote budget

- Family and run ID: `F210-D01`.
- Remote alias: `seetacloud`.
- Remote directory: `/root/IntegerFactoring_F210/F210-D01`.
- Runtime: `/root/miniconda3/bin/python` with SymPy.
- Timeout: 1,800 seconds.
- Concurrency: one Python process and no workers.
- Address-space cap: 8 GiB.
- Expected runtime: 4 to 12 minutes on the previously observed host.
- Expected peak memory: below 2 GiB.
- Expected output: below 150 MiB compressed and below 1 GiB temporary or
  uncompressed data.

The runner performs read-only CPU, load, memory, disk, runtime, and package
checks. It aborts when one-minute load exceeds twice the CPU count, available
memory is below 16 GiB, or free disk is below 5 GiB. It verifies the frozen
source hash before execution. No workflow substitution, retry, truncation,
or post-launch source change is allowed.
