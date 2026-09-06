# F175 repaired hostile re-audit — PASS

## Verdict

**PASS.** The repaired statement, proof, and self-audit establish the claimed
singleton-cut function rank

\[
2^{K-1}
\]

over every prime field `F_r` with `r>2^(K-1)`. The functional ROABP lower
bound is valid in every variable order for arbitrary univariate layer
functions, including nonuniform functions that depend on `r`, a surrounding
composite modulus `N`, or other public parameters. All four repairs requested
by the initial hostile audit are present and correct. I found no remaining
mathematical or scope defect.

This is an exact representation-width result. It is not a time lower bound
and does not extend to the models excluded by the statement.

## Frozen inputs and hashes

I read the repaired files and the preserved initial hostile audit in full. I
did not edit them or any durable ledger. Their SHA-256 hashes at re-audit time
were:

- `STATEMENT.md`:
  `5119a4ba746b40b17f4b1a886fb660ef0463803298c281b36c529b7e55116bfe`;
- `PROOF.md`:
  `eddfc89e8b3e3284e023a07ecff5874f012626d44cc117935368ba9e9c73b0d5`;
- `SELF_AUDIT.md`:
  `a3a8ce7f4c083b349cc9b4d186a68e859c7df72f639709f37941c83fde60f984`;
- preserved initial `HOSTILE_AUDIT.md`:
  `edadacf4b177955199d367f05f5ed01724e6f31cbdb962883ba5658b32e8a169`.

No experimental computation was used.

## 1. The four requested repairs

1. **Cube-Laplacian normalization.** The repaired self-audit now says that
   the reduced-norm description uses the factor-of-two normalization and
   that the standard direction-weighted cube Laplacian has nonzero spectral
   product

   \[
   2^{2^K-1}Q_K.
   \]

   This is exact: for the usual element
   `A=sum_i X_i(1-g_i)`, the character indexed by nonempty `S` has eigenvalue
   `2 L_S`. There are `2^K-1` such characters. Dividing `A` by two gives
   eigenvalues `L_S` over the stated odd-characteristic fields.

2. **No resultant optimality claim.** The repaired text calls
   `2^(K/2+O(1))` the scale of the verified two-block construction. It says
   only that the naive recursive multiblock construction retains a large
   final combine step. It then expressly denies any optimality theorem for
   resultants, norms, modular composition, or determinants. This matches the
   initial audit's required scope.

3. **Individual-degree clarification.** The proof now explicitly records

   \[
   \deg_{Y_i} C_t\le d<r.
   \]

   This is the needed condition for passing from polynomial independence to
   independence of finite-field functions.

4. **Tree-leaf restriction.** The statement now requires each variable to
   occur only at its designated leaf and requires that leaf to have one
   incident bond. The proof uses exactly this condition when cutting that
   bond. It makes no claim for a tensor network that reuses a variable in
   other tensors.

## 2. Fresh check of the rank theorem

Across `X_1 | X_{-1}`, the factorization

\[
Q_K(x,Y)=Q_{K-1}(Y)
\prod_{S\subseteq[K-1]}(x+L_S(Y))
\]

is exact. The empty-set form is zero, so the expansion contains exactly the
`d` powers `x^d,...,x`, with coefficient polynomials

\[
C_t(Y)=Q_{K-1}(Y)e_t(Y),\qquad 0\le t\le d-1.
\]

For lexicographic order `Y_1>...>Y_(K-1)`, the nonzero forms with least index
`i` form a group of size `c_i=2^(K-1-i)`. Greedily filling these groups gives
the leading monomial of `e_t`. All full groups are forced, and the one
possible partial group contributes exactly `binom(c_i,u)`. A lower term
decreases the exponent of the earliest affected variable, and no later
group can restore it. Thus no uncounted term can cancel this coefficient.

Every prime divisor of `binom(c_i,u)` is at most `c_i<d<r`. Hence every
`e_t` is nonzero in `F_r[Y]`. Since `Q_(K-1)` is nonzero in the polynomial
domain, every `C_t` is nonzero. Their distinct homogeneous degrees
`d-1+t` make them polynomially linearly independent.

The individual degree of `Q_K` in each variable is `d`. Coefficient
extraction therefore gives `deg_(Y_i) C_t<=d<r`, so these polynomials are
already canonical finite-field representatives. Their polynomial
independence is consequently also function independence on
`F_r^(K-1)`. Likewise, `x,x^2,...,x^d` are independent functions on `F_r`
because `d<r`.

The evaluation matrix is the product of the two evaluation factors built
from these function families. Both factors have column rank `d`, so their
product has rank exactly `d`, not merely at most `d`. Symmetry gives the same
rank across every singleton cut.

## 3. Functional and nonuniform layers

Cutting any functional ROABP immediately after its first variable gives

\[
f(x,Y)=\sum_{h=1}^{w}f_h(x)g_h(Y).
\]

Its singleton-cut matrix therefore has rank at most `w`. This pointwise
argument places no degree, uniformity, or circuit-size condition on the
univariate layer functions. Exact equality with `Q_K` forces `w>=d`.

The optional polynomial reduction is also sound. Each arbitrary function
`F_r -> F_r` has one interpolant of degree at most `r-1`. Because each input
variable occurs in only one layer, matrix-product expansion never multiplies
two interpolants in the same variable. The resulting multivariate
representative has individual degree at most `r-1` and is canonical.

Dependence on a composite modulus causes no loophole. For a model originally
defined over `Z/NZ`, fix one lift in `Z/NZ` for each element of a hidden field
`F_r`, restrict every input to these lifts, and reduce every layer modulo
`r`. Each layer becomes an arbitrary function `F_r -> F_r`, the width is
unchanged, and exact equality on all modular inputs reduces to exact equality
with `Q_K` on all of `F_r^K`. This reduction does not apply to a branch that
finds a nonunit and exits with a factor, which the statement excludes.

## 4. Model inclusions and exclusions

The four inclusions follow from the same singleton separation:

- a one-pass state update linear in the current state is a product of
  input-dependent transition matrices;
- a tensor train is the same matrix-product representation;
- cutting the sole bond of a designated single-variable tree leaf gives at
  most the bond dimension many singleton-separated terms;
- every exact singleton-separated expansion, including a sum of products of
  one-variable characters, has at least the singleton matrix rank many
  terms. Allowing character values in a field extension does not lower the
  rank of a matrix over `F_r`.

These arguments do not include nonlinear or implicitly encoded state,
variable reuse, a general tree tensor with variables in internal tensors, or
a general global circuit.

Every stated exclusion is warranted. In particular, the theorem does not
bound general arithmetic circuits, fast manipulation of an implicit
exponential state, general determinants or related global formulas,
data-dependent branching and nonunit screens, alternative local-zero
observables, algorithms correct only on sampled inputs, characteristic-
dependent constructions outside the read-once model, or gcd-only detectors.
The displayed `K=2` Moore comparison is also exact in every odd
characteristic: the third zero lines `y=x` and `y=-x` are distinct. It rejects
only that direct characteristic-two lift.

## 5. P34 specialization

With `T=2^K` and the P34 promise `p<q<2p`,

\[
T\le \frac{\lfloor\sqrt N\rfloor}{8}
 <\frac{\sqrt2}{8}p<p<q.
\]

Thus both hidden prime characteristics satisfy `r>T>d=T/2`. Also
`floor(sqrt(N))/16<T`, so `d=2^(Theta(n))` for
`n=ceil(log_2(N+1))`. Every fixed quasipolynomial width
`2^(C(log_2(n+1))^k)` is `2^o(n)`, and therefore is smaller than the required
width for large `n`.

This last comparison remains only a width separation for the named exact
one-pass and singleton-separated models. It does not close the general P34
quasipolynomial evaluator or any of the explicitly excluded routes.
