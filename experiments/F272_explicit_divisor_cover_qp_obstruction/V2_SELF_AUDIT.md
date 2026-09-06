# F272 V2 author self-audit

## Status

This is an author self-audit of V2. It does not replace a fresh hostile audit
or V2 statement-only reconstruction.

## Blind-report corrections

1. **Saturation corrected.** At \((1/3,1/3)\), V2 states
   \(\alpha+2\beta=1\) and \(\alpha+\beta=2/3>1/2\). It calls only the
   first inequality saturated.

2. **Time/output normalization corrected.** Exact inequalities use
   \(F_{\rm out}\), the number of literal output bits. Time uses a fixed
   bit-machine write-rate constant \(C_0\) and concludes
   \(KF_{\rm time}\geq\vartheta_2(X)/C_0=\Omega(X)\). No hidden
   normalization makes the constant one.

3. **Uniqueness removed.** V2 calls the interval-product evaluator one
   precise sufficient interface. It explicitly leaves other succinct,
   adaptive, compressed, and unrelated mechanisms open.

4. **Equivalence removed.** The one-way reduction proves the evaluator
   factoring-hard. V2 states that no reverse reduction and no equivalence
   theorem is proved.

5. **External claims scoped.** The named He--Sahai AP theorem and
   Umans--Wang algorithmic consequence are isolated as external literature
   claims. V2 proves only its elementary conditional substitutions and
   scope distinctions.

## Core theorem checks

6. **Set, multiset, and duplicates.** \(D\) is the set of distinct positive
   absolute differences. Repeated ordered pairs only increase explicit
   output. Replacing multisets by supports preserves all differences and can
   only reduce displayed cardinality.

7. **Signs and zero.** Absolute value preserves positive divisibility. Zero
   is excluded before coverage or factorization; admitting it would make the
   cover condition vacuous. The value one has zero log mass and causes no
   defect.

8. **Prime mass.** Every prime at most \(X\) divides one \(d\), hence the
   primorial divides \(\prod_{d\in D}d\). This proves the logarithmic mass
   bound even when one value carries many required primes.

9. **Expanded length.** A positive \(L\)-bit integer is below \(2^L\).
   Signed \(B\)-bit endpoints have nonzero differences below \(2^{B+1}\).

10. **QP conversion.** A fixed quasipolynomial in
    \(n_X=\Theta(\log X)\) is \(X^{o(1)}\). A fixed product of three such
    bounds cannot reach \(\vartheta_2(X)=\Omega(X)\).

11. **Explicit factor output.** Every required prime name occurs in at
    least one complete output. Literal per-pair outputs give (11). A shared
    dictionary changes that output contract and is handled only through an
    aggregate charged-bit statement.

12. **Prime-pair inequality.** Each value contains at most \(h\) distinct
    band primes. Each pair has product at most \(X\). Repeated coverage
    gives the correct lower incidence inequality. No rank-one intersection
    property is used.

13. **Exponent bookkeeping.** Prime mass gives
    \(1\leq\alpha+2\beta\); pair incidence gives
    \(1\leq2\alpha+2\beta\); fixed-machine output time gives
    \(1\leq\gamma+2\beta\). Fixed constants do not affect exponents.

14. **Prime separation.** Separation gives distinct binary codewords and
    at most one all-zero word. Every other prime name must appear in the
    explicit factor outputs, proving the mass bound after subtracting at
    most \(\log_2X\).

15. **Interval refinement.** When the root gcd is \(N\), the maintained
    interval product is divisible by \(N\). A child gcd of one keeps that
    invariant in the other child; a child gcd of \(N\) keeps it in that
    child. A singleton cannot satisfy the invariant. Therefore a proper gcd
    appears on the one path.

16. **Complete-factorization cost.** Every returned divisor is proper.
    The complete recursion tree has \(O(\log N)\) nontrivial factor nodes
    because its leaves are integers at least two whose product is \(N\).
    Multiplying one fixed quasipolynomial root bound by this polynomial
    factor remains quasipolynomial.

## Remaining risks and exact exclusions

The highest-risk points for fresh audit are the fixed-machine output
contract, the height translation under positive Umans--Wang sets, and the
one-path interval invariant. V2 proves no general circuit lower bound, no
higher-rank one-third refutation, no interval evaluator, no reverse
factoring reduction, and no top-level factoring algorithm.

