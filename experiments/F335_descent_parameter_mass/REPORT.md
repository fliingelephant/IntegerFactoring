# Count-descent parameter mass

**Family:** route:F31

Status: the frozen statement was promoted as P250 after complete independent
reconstruction and root comparison. No QP factoring algorithm and no external
novelty claim. The separate rational-input mechanism remains unpromoted.

## Main result

The fixed-denominator average question has a positive elementary answer:
the CF digit sum has mean at most 4*(N/phi(N))*H_N^2 over Jacobi-positive
units. A public O((log N)^3) cutoff therefore retains at least half of
those inputs, and gives simultaneous bounded count defects. Stronger CF
distribution results already exist in the literature; this proof is kept
for its explicit, self-contained, all-cutoff scope.

Abundant small defects do not supply abundant factors. For p,q in [H,2H],
fixed-h windows of width D can find a p-multiple only on O(log D) dyadic
scales, and at most 32*D*(1+floor(log_2(8D))) integer cofactors q are
eligible for each fixed p. Taking D=floor(sqrt H) and retaining the whole
large-defect tail gives a numerical-power upper bound on factor probability
for the literal uniform-source policy. Fresh multipliers add only the
explicit query-count and generation terms. Uniform and inverse starts
have their own marginal start-window bound, so their correlation with the
multiplier is not silently discarded.

The frozen conclusion concerns only the listed count screens, min descent,
and uniform sources. It does not rule out cheaply generated biased
parameters, other count sources, branching, extra screens, or root outputs.

## Deliberate large defects

A separate exact invariant shows that a small numerical multiplier A cannot
factor an input whose least prime divisor exceeds 5*A^2 through this fixed-h
descent. Each screened count is represented modulo N by a nonzero integer
residual of that size after multiplying by 2A. This conclusion has no
uniform-source assumption.

Small modular inverses behave differently despite identical CF digit sums.
The separate unpromoted RATIONAL_INPUTS.md derives a periodic sign word for
a=b^(-1), and a triangular-wave count profile for a=r/b mod N. Odd b>=3
produces a stable rational contraction, with all discrete iterates within
O(b+r) of its public orbit. This supplies a direct orbit-window control and
a concrete experiment design. No factor-hitting law is asserted. Large
numerical r,b make that menu large and are not excluded by the cheap-menu
observation.

## Verification handoff

- Frozen statement: STATEMENT_ONLY.md.
- Complete author proof: PROOF.md.
- Complete independent proof: RECONSTRUCTION.md.
- Root scope comparison and promotion decision: ROOT_COMPARISON.md.
- Separate author mechanism: RATIONAL_INPUTS.md.
- Finite-check specification: DESIGN.md. The persistent Sol owns its source,
  preflight, timeout, logs, JSON, and the later check-status update below.
- Sources and exact external dependency: SOURCES.md. The Rosser--Schoenfeld
  prime count is used only to produce infinitely many balanced inputs.

Frozen statement SHA-256:
75c092beacf63c7dda9681be4fd54ae208d2fc0188586a80e6b2ab3b69d9e6c9.
Author proof SHA-256:
5a698ed631ff8fcd8ed55fc195af008284c7f42d60b83c3de405f2e671b326cc.
Final independent reconstruction SHA-256:
33125e52d1c184fda0f9a8f3bb952d081daac794ce43762eb349607a6c48d6c1.
Separate rational note SHA-256:
902783b080450fe422b50ec2a51e173203092c0cd1f3d4474320e98bc9a54e3f.

## Finite checks

The exact checker passed its pilot through odd `N <= 51` and its planned scale
through odd `N <= 301`, with no counterexample. The scale run made 18,484
digit-sum symmetry checks, 89,804 digit-triple checks, 22,800 large-digit tail
checks, 3,722,060 prefix-discrepancy checks, and 150 total-digit-sum checks.
It also made 3,816 affine-error and 3,816 child-congruence checks, 1,453
complement-sequence checks, 284 least-prime exclusion checks, 6,570 positive
child-residual checks, and 2,363 quotient-halving checks. The bounded dyadic
tables made 16,427 integer-cofactor, 18,951 ordered prime-scale, and 1,625
unordered prime-pair checks.

The scale run took 1.462 seconds and peaked at 26,017,792 bytes RSS. These are
finite formula checks only. Factors enter only after public gcd outputs as
validation labels, and the results do not establish an asymptotic parameter
mass. Evidence: `parameter_mass_checks.py`, `pilot_output.json`,
`pilot_status.json`, `pilot_run.log`, `scale_output.json`, `scale_status.json`,
and `scale_run.log`. The source SHA-256 is
`ae73a41d02021a3ed33363018ef5119d5a32df758f31bd01ea1397be2d35d0e3`;
the frozen design SHA-256 is
`31d064afd59474ec747869e04f542850289bf179976e653944897d1053f4fd85`.
