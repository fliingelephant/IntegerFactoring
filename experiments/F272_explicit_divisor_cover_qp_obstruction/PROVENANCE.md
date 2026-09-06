# F272 provenance and boundary comparison

## Closest prior local route

The closest local route is F171/P157,
`experiments/F171_carry_difference_cover_full_rank_boundary`. It proves
that complete small-prime coverage of selected canonical-inverse carry rows
can coexist with a full-rank parity matrix because every selected column has
a private prime row.

F272 differs materially. It does not study carry rows, square-class parity,
normalized roots, or a selected relation bank. It gives rank-free
information/output lower bounds for positive divisor covers and static
prime-separating gcd banks. F171 is context only and is not a premise.

## Primary literature

1. Chris Umans and Siki Wang, *A number-theoretic conjecture implying
   faster algorithms for polynomial factorization and integer
   factorization*, arXiv:2511.10851v1 (2025),
   <https://arxiv.org/abs/2511.10851>.

   Relevant items are Definitions/Conjectures 3.1--3.3, the elementary
   prime-mass condition \(\alpha\geq1-2\beta\), the Strong Prefactored
   Conjecture 5.1, Theorem 5.5, and the addition-sequence extension in
   Section 7. F272 restates the prime-mass argument in the exact QP input
   scale, adds the explicit output lower bound, records a rank-free
   prime-pair inequality, and separates expanded length from succinct
   modular evaluation.

2. Xinjie He and Amit Sahai, *Refuting a Conjecture of Umans and Wang on
   Arithmetic-Progression Divisor Covers*, arXiv:2608.06681v1 (2026),
   <https://arxiv.org/abs/2608.06681>.

   Their theorem gives the one-dimensional AP bound (18). Their Remark 4.2
   explicitly limits the result to the AP version and notes that the
   at-most-one-intersection argument does not follow for rank two. F272
   preserves that boundary.

## Other local boundaries

- P172/F195 gives a published \(N^{1/4}/M\) common-congruence terminal and
  leaves the beta-two mixed high-order branch open. F272 neither uses nor
  strengthens it.
- P174/F197 proves exact factorial gcd identities and records the
  exponential scale of named explicit block and published
  baby-step/giant-step factorial methods. It is the closest boundary to the
  succinct interval-product seam in F272.
- P184/F208 relocates one beta-two selector to a signed divisor shell and
  proves no compressed evaluator. F272 likewise proves no circuit lower
  bound, but its cover-output obstruction is otherwise independent.

## Mathematical dependencies

The proof uses only:

1. unique factorization and pairwise coprimality of distinct primes;
2. the standard Chebyshev lower bound \(\vartheta(X)=\Omega(X)\);
3. the prime number theorem for the stated asymptotics and fixed
   square-root-band count; and
4. elementary counting of binary codewords and prime-pair incidences.

The main rank-free QP obstruction needs only items 1 and 2. No unproved
number-theoretic conjecture, factoring oracle, order oracle, computation,
dataset, or heuristic distribution assumption is used.

## Exact novelty and exclusions

F272 does not claim the elementary Umans--Wang prime-mass inequality as a
new theorem. Its new project-level contribution is the exact consequence
for quasipolynomial cardinality and expanded bit length, the explicit
prefactor-output obstruction even for succinct huge values, and the
prime-separating relaxation.

It does not refute the Strong \((1/3,1/3)\)-Divisor Conjecture, fixed-rank
GAPs at that scale, short addition sequences at that scale, succinct
modular product circuits, adaptive gcd banks, or all classical QP factoring
algorithms. It supplies no top-level factoring algorithm.
