# F175 self-audit and positive-route check

**Status:** self-audited candidate. A fresh hostile audit and a statement-only
reconstruction are still required.

## 1. Checks on the theorem

- The empty subset is present only in the second product of (1.1). Its form
  is zero, so the constant coefficient in `x` vanishes and there are exactly
  `d` displayed nonzero coefficient candidates.
- The characteristic assumption is `r>d`, not only `char(F)>2`. It both
  preserves the greedy binomial leading coefficients and makes `Q_K` a
  canonical finite-field polynomial in each variable.
- The proof uses the first variable in an arbitrary ROABP order. Symmetry of
  `Q_K` makes the lower bound independent of the order.
- The layer functions are arbitrary finite-field functions. Thus the theorem
  does not rely on a degree bound for an N-dependent exponentiation inside
  one layer.
- The result is a width lower bound. A QP algorithm could revisit variables,
  branch, use a global determinant, or compute a different local-zero
  observable. Those cases remain open.

## 2. Moore and characteristic-dependent identities

In characteristic two, the Moore determinant factors as the product of all
nonzero Boolean linear forms. The hidden factors in P34 have odd
characteristic. The direct integer lift changes sums to differences already
at `K=2`:

\[
 xy(y-x)\ne xy(x+y).
\]

It therefore neither evaluates `Q_K` nor preserves its zero set. A genuine
local `p`-Frobenius on an extension algebra needs the hidden characteristic,
which is the P132 gate. Substituting public powers such as `N^i` produces
cross-exponent generalized Vandermonde matrices, not Moore matrices. Their
rank can reveal special hidden-order mismatches, but no all-prime or
constant-mass theorem follows.

This does not exclude a different small determinant. The ROABP theorem
cannot exclude one: determinant expansion can have exponential read-once
width while numeric determinant evaluation is polynomial.

## 3. Kronecker norms, resultants, and modular composition

The P34 product is the reduced norm of a sparse element in the Boolean group
algebra after the standard factor-of-two normalization. Equivalently, the
standard direction-weighted cube Laplacian has nonzero spectral product

\[
 2^{2^K-1}Q_K.
\]

The literal algebra has dimension `2^K`. The verified two-block
resultant construction has `2^{K/2+O(1)}` scale. A naive recursive
multiblock construction does not by itself remove the final large combine
step. This is an observation about that construction, not an optimality
theorem for resultants, norms, or modular composition.

F175 rules out only a bounded-state contraction that exposes one variable at
a time or one variable per tensor leaf. It does not prove a lower bound for
all resultant, norm, modular-composition, or determinant algorithms.

## 4. Geometric and q-Pochhammer weights

A geometric pool has the form

\[
 \prod_{j=0}^{T-1}(X-a g^j).
\]

It collapses to `X^T-a^T` when the powers of `g` form the full group of
`T`-th roots. Locally this requires a large known divisor of `r-1`, or an
equivalent order certificate. Without it, the usual doubling recurrence has
two shifted children and retains `T` leaves. This is the P20/P21 order gate,
not a P34 evaluator.

## 5. Additive characters and exact root counts

If a hidden prime `r` and a primitive additive character were available, the
number of zero subset sums would be

\[
 Z_r=\frac1r\sum_{t\in\mathbb F_r}
       \prod_{i=1}^K(1+\chi_t(a_i)).
\]

The exact formula has `r` modes. For nontrivial random `t` and uniform
weights, the character sum over all `T=2^K` subsets has second moment `T`:
distinct Boolean incidence vectors give orthogonal characters. Thus naive
QP-mode Monte Carlo does not provide an exact zero count or a Las Vegas gcd
certificate. F175 proves an exponential width bound only when such a
character expansion exactly equals `Q_K`; it does not prove a general
sampling lower bound.

## 6. Gcd-only and random-input escapes

P34 needs only a proper gcd on random inputs. An evaluator can therefore be
weaker than a uniform exact computation of `Q_K`. A characteristic-dependent
function can also have the same finite-field zero set without being the
integer union polynomial. Branching on a nonunit denominator can itself
factor the modulus. None of these possibilities is covered.

The strongest warranted conclusion is narrow: QP rescaling does not rescue
the exact Boolean product through a one-pass functional state, a bounded-bond
one-variable tensor representation, or an exact separated character sum.
The general P34 evaluator and alternative pooled observables remain live.
