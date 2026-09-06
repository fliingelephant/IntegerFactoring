# F272 V2 provenance and boundary comparison

## Immutable V1 and blind reconstruction

V2 is an additive correction. It does not modify the V1 packet or its blind
statement-only reconstruction.

The blind reconstruction authenticated V1 `STATEMENT.md` at

`103722d5cf46884678867fd093e1ce5bcef9d57a797275c0f0e3c262615d67d0`

and is preserved at `BLIND_RECONSTRUCTION.md`, SHA-256

`4be8415b7dd33e26a8a75f893b7a89d99d763ad2ce7ee3f0f72fe1f3665c9500`.

It independently reconstructed the prime-mass, explicit-output,
prime-pair, exponent, prime-separation, and interval-sufficiency arguments.
It rejected four literal V1 claims. V2 corrects all four as listed in
`V2_STATEMENT.md` and `V2_SELF_AUDIT.md`.

## Closest prior local route

The closest local route is F171/P157,
`experiments/F171_carry_difference_cover_full_rank_boundary`. It proves
that complete small-prime coverage of selected canonical-inverse carry rows
can coexist with a full-rank parity matrix because every selected column has
a private prime row.

F272 differs materially. It does not study carry rows, square-class parity,
normalized roots, or a selected relation bank. It gives rank-free
information/output lower bounds for positive divisor covers and static
prime-separating gcd banks. F171 is context only, not a premise.

## Primary literature and citation scope

1. Chris Umans and Siki Wang, *A number-theoretic conjecture implying faster
   algorithms for polynomial factorization and integer factorization*,
   arXiv:2511.10851v1 (2025),
   <https://arxiv.org/abs/2511.10851>.

   The relevant external items are their divisor conjectures, the elementary
   prime-mass condition, the Strong Prefactored Conjecture, Theorem 5.5, and
   the addition-sequence extension. F272 V2 re-proves the prime-mass
   inequality in its exact notation. It treats Theorem 5.5 as an imported
   literature claim.

2. Xinjie He and Amit Sahai, *Refuting a Conjecture of Umans and Wang on
   Arithmetic-Progression Divisor Covers*, arXiv:2608.06681v1 (2026),
   <https://arxiv.org/abs/2608.06681>.

   Their external theorem gives the one-dimensional AP bound quoted in
   (20), and their scope remark excludes an automatic rank-two conclusion.
   F272 V2 does not derive this paper's theorem and does not use it to claim
   a higher-rank obstruction.

## Other local boundaries

- P172/F195 gives a published \(N^{1/4}/M\) common-congruence terminal and
  leaves the beta-two mixed high-order branch open. F272 V2 neither uses nor
  strengthens it.
- P174/F197 gives exact factorial gcd identities and records the exponential
  scale of named explicit block and published baby-step/giant-step methods.
  It is the closest local boundary to the sufficient interval-product
  interface.
- P184/F208 relocates one beta-two selector to a signed divisor shell and
  proves no compressed evaluator. F272 V2 likewise proves no circuit lower
  bound, but its output obstruction is independent.

## Mathematical dependencies proved or standard

The internal proof uses:

1. unique factorization and coprimality of distinct primes;
2. the standard Chebyshev lower bound \(\vartheta(X)=\Omega(X)\);
3. the prime number theorem for the optional sharp asymptotic and the fixed
   square-root-band count; and
4. elementary binary-code and incidence counting.

The main rank-free QP obstruction needs only items 1 and 2. No unproved
number-theoretic conjecture, factoring oracle, order oracle, computation,
dataset, or heuristic distribution assumption is used.

## Exact contribution and exclusions

F272 V2 does not claim the elementary Umans--Wang prime-mass inequality as
new. Its project-level contribution is the exact QP-in-\(\log X\)
consequence, the explicit-prefactor output obstruction for succinct huge
values, the prime-pair bound, the prime-separating relaxation, and the clean
separation between expanded/output models and modular evaluators.

It does not refute the Strong \((1/3,1/3)\)-Divisor Conjecture, fixed-rank
GAPs at that scale, short addition sequences, succinct modular circuits,
adaptive gcd banks, compressed decoders, or unrelated factoring algorithms.
It gives one sufficient factoring-hard interval interface, not a unique
escape and not an equivalence theorem. It supplies no top-level factoring
algorithm.

