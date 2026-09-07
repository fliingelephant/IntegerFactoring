# Root integration: restart cost and adaptive scale invariance

**Family:** route:F29

Status: elementary root-derived identities and interpretation of the
retained experiments. No quasipolynomial success or runtime theorem.

## The finite public protocol has a weak Las Vegas wrapper

For a promised composite N, repeat independent capped attempts. An attempt's
first probe is an ordinary uniform residue x, because its parameter list is
empty. If p is the least prime divisor, the N/p-1 nonzero multiples of p
already give

    Pr(success in an attempt) >= (N/p-1)/N >= 1/(2p).

No statement about a later adaptive distribution is needed for this bound.
It covers prime powers as well as squarefree composites. With B public
probes, the attempt uses at most B(B-1)/2 modular multiplications, B gcds,
and expected O(B*bitlength(N)) fair bits. Independent repetition therefore
has finite expected cost at most O(p*B^2*poly(bitlength(N))). Every accepted
factor is verified. Handling primes and recursive factorization must still
be included in a complete algorithm.

Thus the unresolved issue is a sufficiently strong improvement over this
weak bound, including the actual work of evaluating the growing circuit.
It is not a missing almost-sure-termination argument on composite inputs.
The later radical-shadow argument in RADICAL_SHADOW.md also bypasses
prime-power population analysis for a sufficiently strong squarefree success
contract. The field growth and its quasipolynomial cost remain unproved.

## Cumulative hazard is a weaker target than large one-step root mass

Use ANALYSIS.md's forced-unit chain on a squarefree semiprime. At state j
write h_j for the factor hazard after full-zero retries and z_j for the
raw full-zero probability. Suppose an event of forced-chain probability
at least delta supplies T well-defined states with

    sum_(j<T) h_j >= lambda,       z_j <= 1-epsilon for all j<T.

Conditioning on a forced path, its no-factor probability is the product
of (1-h_j), hence at most exp(-lambda). With K raw probes per stage,
capped-reset coupling and a union bound therefore give

    actual success >= delta*(1-exp(-lambda))-T*(1-epsilon)^K.

The attempt costs O(K*T^2*poly(bitlength(N))) under the retained circuit
evaluation. Inverse-quasipolynomial delta, epsilon, and lambda may suffice;
neither a constant per-probe probability nor a constant root mass is needed.
This is a sufficient contract, not a proved property of the current chain.
It also does not extend the field coupling to prime powers automatically.

## Unit normalization does not change this adaptive process

Suppose two coupled protocols use the same seeds and, at some stage,
their current functions satisfy G(x)=c H(x) modulo N with c a unit.
Their gcd classifications agree. If a=H(seed) is an accepted unit root,
the corresponding root is ca for G, and

    G(x)(G(x)-ca)=c^2 H(x)(H(x)-a) modulo N.

Induction proves equality of every factor/unit/full-zero classification,
including finite reset decisions. Multiplying the output after an update
by any further public unit preserves the coupling. The same fact holds
for the fiber guard because differences scale by that unit.

In particular, the normalized update

    (H(x)/a)*(H(x)/a-1)

has exactly the same discovery law as the retained update, under a suitable
unit scaling of the next state. Over a field, root mass, support size, and
collision energy are also unchanged by this scaling. Normalizing the new
root to one is therefore not a new sampler or growth mechanism here.
This says nothing about translations, different root-selection laws,
auxiliary states, or maps outside this exact coupled transformation.

## What the measured costs establish

The initial same-probe cap favors the adaptive protocol's success fraction:
one adaptive H evaluation costs its current depth, while one rho iteration
costs three modular multiplications. RHO_WORK_REPORT.md supplies the needed
separate comparison under a public multiplication budget, preserving the
original censored data.

At the largest balanced input, the 32 work-matched rho trials and all 32
adaptive trials succeeded. The mean multiplication counts were about 38,759
and 408,299, respectively; the gcd counts were about 12,920 and 860. These
are finite sample costs, not expected-runtime theorems or an asymptotic
comparison. A fewer-gcd result alone does not establish a speedup.

One testable heuristic is that early nonzero collision energy grows roughly
linearly in accepted depth divided by p. Its cumulative zero-mass drift
would then be quadratic in depth divided by p, and cumulative probe hazard
cubic. This predicts about p^(1/3) adaptive probes but p^(2/3) multiplication
work under depth-linear evaluation, rather than a quasipolynomial algorithm.
The six preselected balanced scale inputs are summarized descriptively in
scaling_summary.py/json and scaling_summary_verified.log. The first summary
attempt used the wrong exact dataset label and stopped at its six-case
assertion before fitting; its source, log, and status are retained separately.
A finite fitted exponent does not prove this
heuristic, rule out a later regime, or supply an all-input bound.

The guard experiment never rejected a global-equality proposal. Its data
therefore do not demonstrate useful overshoot control. The exact guard law
in ANALYSIS.md and the finite cost measurements answer different questions.

The remaining mechanism would need useful growth per total evaluation cost,
or a cheaper representation/evaluation of the adaptive maps. Increasing
formal degree, normalizing units, or conditioning away difficult trials does
not supply that improvement.
