# The exponent derivative does not supply a new quadratic-carry equation

**Status:** root-derived dependency of the proposed precision-lifting route.
No general impossibility result. This note does not replace the proved
mod-M-squared constructor or rule out a different higher-precision method.

The attempted next step was to vary the exponent in the computable L_j,
then use its derivative at zero to recover a quadratic carry statistic.
The derivative has an exact symmetry that prevents this particular
extraction from adding an independent equation.

Write log_adic for the 2-adic unit logarithm, defined by(1/2)log(u^2),
and put ell_u=log_adic(u), lambda=log_adic(N), phi=M/2. For a formal
variable t define

    A(t)=sum_(u in U_M) exp(t*ell_u),
    L(t)=N/[M*t] * [A(t)-exp(t*lambda)*A(-t)].

The numerator vanishes at t=0. For even integer exponents approaching zero
2-adically, L(t) agrees with the universal power-sum expression in F303.
Its value at zero is

    L(0)=N/M * [2*log_adic(Pi_M)-phi*log_adic(N)].

Direct substitution gives the exact formal identity

    L(-t)=exp(-t*lambda)*L(t).                         (1)

Consequently exp(-t*lambda/2)*L(t) is even, and

    L'(0)=(lambda/2)*L(0).                            (2)

More explicitly,

    exp(-t*lambda/2)*L(t)
      =(2N/M)*sum_(r>=0) t^(2r)/(2r+1)!
                    *sum_u(ell_u-lambda/2)^(2r+1).   (3)

This entire centered derivative family consists of ordinary marginal log
moments. Taking the odd derivative does not produce a new joint carry
statistic. The same cancellation occurs if one first expands L_j into its
Q_(j,h) carry terms and then differentiates: the apparent Q_(0,2) terms
cancel after using the u/v involution.

This is a statement about the proposed derivative equation, not a claim
that the full known input or all possible identities cannot determine the
next precision digit. The unresolved Q_(j,2)/2 bank in F303 remains a
concrete target for other operations.

## A target-modulus witness

For the actual input N=289 with M=32 (the largest power of two at mostN/8),
the canonical inverse graph has

    S11=4688, sum q_u=2, sum q_u^2=1090,
    (sum q_u^2)/2 modM=1,
    e2(q)=(2^2-1090)/2=-543=1 mod32.

Thus its quadratic-carry correction is nonzero. Nevertheless the residual
L'(0)-(log_adic(N)/2)*L(0) vanishes exactly by(2). A proposed extraction that
treats that residual as the missing independent quadratic statistic would
give the wrong answer on this input.

## Exact finite-difference checks

The retained pilot uses M=8,16,32,64 and N=8M+1,8M+3,9M+1,9M+5.
Let B=k+8 and delta=2^(k+8). It computes L(delta),L(-delta) from the
universal power-sum formula with all division guard bits, and compares

    [L(delta)-L(-delta)]/(2delta) mod2^B

with(log_adic(N)/2)*L(0). The original inverse graph is enumerated only as
a small independent reference for the carry statistics and S11.

The finite-difference error is controlled: since ell_u is divisible by4 and
lambda/2 by2, the coefficients of L(t) have valuation at least2-k by(3)
and v2(j!)<=j-1 for j>=1. The central-difference remainder therefore has
valuation at least2*v2(delta)+2-k>B. Working precision6k+64, including
guard bits before divisions by M and delta, is more than sufficient for
these comparisons. The output retains actual q-square corrections
separately from the identically dependent derivative residual.

All16 symmetry and guarded derivative checks passed. The quadratic carry
and e2 residues were nonzero on15 inputs. All16 third-digit reconstructions
matched the exact S11. For N=289,M=32, dropping the quadratic correction
gave3664; adding its1024 contribution recovered4688.

The source, JSON, log, and completion status are exponent_derivative.py,
exponent_derivative.json, exponent_derivative.log, and
exponent_derivative.status. The pure-integer run used a30-second alarm,
took0.0036seconds, and measured17,350,656bytes peak RSS. Preflight reported
70% available memory and load2.11/2.03/2.00, with no competing numerical
process. No finite-difference tail was silently treated as an Archimedean
error estimate.
