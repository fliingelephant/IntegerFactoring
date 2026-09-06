# F206 candidate — ordinary vector completion fails, while the natural Whittaker pair is circular

## Status and scope

This is a frozen proof-only candidate awaiting hostile audit. It starts from
the fixed `m=2` selector of F203 and the scalar q-product boundary of F204.
It tests the next named route: a finite-dimensional vector-valued, Eichler,
or nonholomorphic completion of the q-product or its logarithmic derivative.

The result has two parts.

1. A fixed projection of an ordinary finite-dimensional meromorphic
   vector-valued modular form with semisimple cusp monodromy cannot equal the
   q-product, its anti-invariant ratio, or its Lambert logarithmic derivative.
2. The natural two-kernel Mellin completion has an unavoidable trigonometric
   archimedean factor. A Whittaker correction can absorb that factor, but it
   pairs the target coefficient only with its public character multiple at
   the same index. It supplies no smaller public arithmetic state.

This is not a lower bound against arbitrary vector-valued, mock, quantum, or
nonholomorphic constructions. It supplies no coefficient evaluator and no
factoring algorithm.

Let `chi=chi_4`, and define

\[
 A(n)=\sum_{d\mid n}d\chi(d),\qquad
 L(q)=\sum_{n\geq1}A(n)q^n,
\]

and

\[
 P(q)=\prod_{a\geq1}(1-q^a)^{\chi(a)}
     =\frac{(q;q^4)_\infty}{(q^3;q^4)_\infty}.
\]

Thus `L(q)=-q d(log P)/dq`. Put

\[
 R(q)=\frac{P(q)}{P(-q)}.
\]

Exact evaluation of `A(N)` factors every distinct odd semiprime `N`, by
F203. F206 studies only proposed ways to fast-forward this coefficient.

## 1. Exact radial data

As `t` tends to zero through positive values,

\[
 \boxed{
 P(e^{-t})\sim
 2\frac{\Gamma(3/4)}{\Gamma(1/4)}\sqrt t,
 \qquad
 P(-e^{-t})\longrightarrow\sqrt2.}
\]

The Lambert series has the sharper expansions

\[
 \boxed{
 L(e^{-t})=\frac1{2t}-\frac{t}{24}+O(t^3),
 \qquad
 L(-e^{-t})=-\frac{t}{8}+O(t^3).}
\]

For `q=exp(2 pi i tau)`, the radial powers at the rational cusps zero and
one-half are therefore

| function | cusp zero | cusp one-half |
|---|---:|---:|
| `P(q)` | `y^(1/2)` | `y^0` |
| `R(q)` | `y^(1/2)` | `y^(-1/2)` |
| `L(q)` | `y^(-1)` | `y^1` |

Every displayed leading constant is nonzero.

## 2. Ordinary semisimple vector modularity boundary

Use the following precise hypothesis. Let `V` be finite-dimensional, let
`rho` be a finite-dimensional representation on a finite-index subgroup of
`SL_2(Z)`, and let `F:H -> V` be a meromorphic vector-valued modular form of
one fixed real weight `k`. At every rational cusp, assume the parabolic
monodromy is semisimple and, after a scaling matrix and diagonalization, each
coordinate has an ordinary meromorphic Puiseux Fourier expansion with a
finite principal part. In particular, there are no logarithmic Fourier terms
from a parabolic Jordan block.

For any fixed linear functional `ell` on `V`, a nonzero radial asymptotic

\[
 (\ell F)(r+iy)\sim C y^\alpha
 \qquad(C\ne0)
\]

which is neither exponentially growing nor exponentially decaying must have

\[
 \boxed{\alpha=-k.}
\]

The exponent is the same at every rational cusp where such a polynomial
asymptotic occurs. The table above therefore proves:

\[
 \boxed{
 \text{No fixed projection }\ell F\text{ can equal }P(q),\ R(q),
 \text{ or }L(q).}
\]

This excludes an exact component or fixed projection of an ordinary
semisimple meromorphic vector-valued modular form. It does not exclude a
holomorphic part whose nonholomorphic correction changes the cusp powers,
nor nonsemisimple logarithmic cusp data.

## 3. Exact dual kernel and its Mellin reflection

Define the transposed divisor sum

\[
 A^\vee(n)=\sum_{d\mid n}d\chi(n/d),\qquad
 L^\vee(q)=\sum_{n\geq1}A^\vee(n)q^n.
\]

For every odd `n`, multiplicativity gives

\[
 \boxed{A^\vee(n)=\chi(n)A(n).}
\]

Let

\[
 \mathcal M_A(s)=\int_0^\infty L(e^{-2\pi y})y^{s-1}\,dy,
 \qquad
 \mathcal M_\vee(s)=\int_0^\infty L^\vee(e^{-2\pi y})y^{s-1}\,dy,
\]

initially in their half-planes of absolute convergence and then by
meromorphic continuation. Their exact Dirichlet products are

\[
 \mathcal M_A(s)
 =\Gamma(s)(2\pi)^{-s}\zeta(s)\,L(s-1,\chi),
\]

\[
 \mathcal M_\vee(s)
 =\Gamma(s)(2\pi)^{-s}\zeta(s-1)\,L(s,\chi).
\]

The zeta and primitive `chi_4` functional equations give

\[
 \boxed{
 \mathcal M_A(s)
 =2^{3-2s}\tan\!\left(\frac{\pi s}{2}\right)
  \mathcal M_\vee(2-s).}
\]

Equivalently, after the conductor normalization

\[
 \widetilde{\mathcal M}(s)
 =2^s\begin{pmatrix}\mathcal M_A(s)\\ \mathcal M_\vee(s)\end{pmatrix},
\]

the natural reflection is

\[
 \boxed{
 \widetilde{\mathcal M}(s)
 =J(s)\widetilde{\mathcal M}(2-s),\qquad
 J(s)=
 \begin{pmatrix}
 0&2\tan(\pi s/2)\\
 -\tfrac12\cot(\pi s/2)&0
 \end{pmatrix}.}
\]

The matrix `J(s)` is not constant and no fixed change of basis makes it
constant. Thus the two pure exponential Lambert kernels do not themselves
have the constant-matrix Fricke law of an ordinary vector-valued modular
form.

## 4. Finite-depth repairs and the natural Whittaker circularity

In the diagonal Mellin model, a finite number of Euler derivatives,
Euler antiderivatives, and finite period-polynomial corrections changes a
component by rational functions of `s` and finitely many polar terms. Such a
repair cannot remove `tan(pi s/2)` or `cot(pi s/2)`, which have infinitely
many alternating poles and zeros. This closes the fixed finite-depth
Eichler/differential repair of the displayed two exponential kernels. It is
not a statement about arbitrary nonpolynomial quantum cocycles.

A nonholomorphic Whittaker or Mellin-convolution correction can absorb the
trigonometric factor. Indeed,

\[
 \tan\!\left(\frac{\pi s}{2}\right)
 =\frac{
 \Gamma((1+s)/2)\Gamma((1-s)/2)}{
 \Gamma(s/2)\Gamma(1-s/2)}.
\]

But such a correction changes only the archimedean kernel. The arithmetic
Fourier coefficients remain `A(n)` and `A^vee(n)`. At every odd target,

\[
 [n=N]\text{ in the dual component}
 =A^\vee(N)=\chi(N)A(N),
\]

where the sign `chi(N)` is public. For the semiprime target, the natural
dual amplitude is therefore factoring-equivalent to the original amplitude
at the same index. The reflection transforms a global kernel sum; it does
not send `N` to a smaller public index.

Consequently, this natural finite-dimensional nonholomorphic completion does
not provide the required QP coefficient recurrence or one-child arithmetic
contraction. Direct dense truncation of either Lambert series through
`q^N` stores `Theta(N)` coefficient positions, which is exponential in the
input length `log N`.

## 5. Exact boundary

Ordinary semisimple vector modularity is incompatible with the exact cusp
powers. The natural two-kernel functional equation has a nonconstant
trigonometric reflection matrix. Finite rational Mellin repairs do not remove
it. A Whittaker repair can remove it only by retaining the same hidden
coefficient, up to a public sign, in the dual component at the same index.

The result leaves open:

- nonsemisimple vector-valued forms with essential logarithmic cusp data;
- mock or nonholomorphic completions with an additional arithmetic shadow;
- genuinely nonpolynomial quantum cocycles;
- vector dimension or state growing quasipolynomially with `log N`;
- nonlinear arithmetic identities; and
- adaptive integer-specific decoders that produce a smaller public child.

Any positive continuation must exhibit the smaller public arithmetic state
or a QP remote-coefficient recurrence explicitly. Naming a completion whose
`N`-th Fourier amplitude is `A(N)` does not evaluate the selector.
