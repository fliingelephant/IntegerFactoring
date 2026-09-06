# Proof of F206

## 1. Radial asymptotics of the product

Put `q=e^(-t)` and `Q=q^4=e^(-4t)`. The q-gamma identity

\[
 \Gamma_Q(x)
 =(1-Q)^{1-x}\frac{(Q;Q)_\infty}{(Q^x;Q)_\infty}
\]

gives

\[
 P(e^{-t})
 =(1-Q)^{1/2}\frac{\Gamma_Q(3/4)}{\Gamma_Q(1/4)}.
\]

As `t` tends to zero, `Gamma_Q(x)` tends to `Gamma(x)` and
`1-Q` is asymptotic to `4t`. Hence

\[
 P(e^{-t})\sim
 2\frac{\Gamma(3/4)}{\Gamma(1/4)}\sqrt t.
\]

F204 proved the exact binary norm

\[
 P(q)P(-q)=P(q^2).
\]

It follows that

\[
 P(-e^{-t})=\frac{P(e^{-2t})}{P(e^{-t})}\longrightarrow\sqrt2.
\]

The constants are finite and nonzero.

## 2. Radial asymptotics of the Lambert series

Write `beta(s)=L(s,chi_4)`. Since

\[
 \sum_{n\geq1}\frac{A(n)}{n^s}
 =\zeta(s)\beta(s-1),
\]

Mellin inversion gives, initially on a right half-plane,

\[
 L(e^{-t})
 =\frac1{2\pi i}\int_{(c)}
   \Gamma(s)\zeta(s)\beta(s-1)t^{-s}\,ds.
\]

Shift the contour to the left. At `s=1`, the pole of zeta has residue one
and `beta(0)=1/2`, so the residue is `1/(2t)`. At `s=0`, the pole of Gamma
is cancelled by the trivial zero `beta(-1)=0`. At `s=-1`,

\[
 \mathop{\rm Res}_{s=-1}\Gamma(s)=-1,
 \qquad \zeta(-1)=-\frac1{12},
 \qquad \beta(-2)=-\frac12.
\]

The resulting residue is `-t/24`. At `s=-2`, the Gamma pole is cancelled
by the trivial zeros. The next possible term has order `t^3`. Standard
vertical-strip bounds after the contour shift therefore give

\[
 L(e^{-t})=\frac1{2t}-\frac{t}{24}+O(t^3).
\]

Logarithmically differentiating the binary norm gives

\[
 L(q)+L(-q)=2L(q^2).
\]

At `q=e^(-t)`, this yields

\[
 \begin{aligned}
 L(-e^{-t})
 &=2L(e^{-2t})-L(e^{-t})\\
 &=-\frac{t}{8}+O(t^3).
 \end{aligned}
\]

Finally put `t=2 pi y`. At `tau=iy`, the three functions have powers
`y^(1/2)`, `y^(1/2)`, and `y^(-1)`, respectively. At
`tau=1/2+iy`, the substitution `q -> -q` exchanges the two product factors,
inverts `R`, and gives the powers `y^0`, `y^(-1/2)`, and `y^1`.

## 3. The semisimple vector cusp lemma

Fix a rational cusp `r` and a scaling matrix `sigma_r`. Under the stated
semisimple monodromy hypothesis, diagonalization of the parabolic action
gives a finite sum of ordinary eigen-expansions

\[
 (F|_k\sigma_r)(\tau)
 =\sum_\lambda\sum_{n\geq n_0(\lambda)}
   v_{\lambda,n}
   \exp\!\left(\frac{2\pi i(n+\lambda)\tau}{w_r}\right),
\]

with a finite principal part and no powers of `tau` multiplying the Fourier
modes. Apply the fixed projection transported through `sigma_r`.

As `tau=r+iy` tends radially to the cusp, the scaled imaginary part is a
positive constant times `1/y`. A surviving negative local exponent produces
exponential growth in `1/y`. A surviving positive exponent produces
exponential decay. If the first surviving exponent is zero, undoing the
weight-`k` slash contributes exactly a nonzero constant times `y^(-k)`.
There is no other polynomial power because semisimplicity excludes logarithmic
Fourier terms.

Thus every nonzero, nonexponential projected radial asymptotic has power
`-k`. Comparing the two cusp powers in each row of the table proves the
three claimed impossibilities. For `L`, even one cusp would force `k=1`
while the other would force `k=-1`. The corresponding contradictions for
`P` and `R` are equally immediate.

## 4. The transposed coefficient is the same odd-index selector

Define

\[
 A^\vee(n)=\sum_{d\mid n}d\chi(n/d).
\]

If `n` is odd, then every divisor `d` is odd and

\[
 \chi(n/d)=\chi(n)\chi(d),
\]

because `chi(d)^2=1`. Therefore

\[
 A^\vee(n)
 =\chi(n)\sum_{d\mid n}d\chi(d)
 =\chi(n)A(n).
\]

The sign is computable from `n mod 4`. No hidden orientation has changed.

The convolution definitions give the Dirichlet products

\[
 \sum_{n\geq1}\frac{A(n)}{n^s}
 =\zeta(s)\beta(s-1),
 \qquad
 \sum_{n\geq1}\frac{A^\vee(n)}{n^s}
 =\zeta(s-1)\beta(s).
\]

Termwise Mellin integration of `exp(-2 pi n y)` then proves

\[
 \mathcal M_A(s)
 =\Gamma(s)(2\pi)^{-s}\zeta(s)\beta(s-1)
\]

and

\[
 \mathcal M_\vee(s)
 =\Gamma(s)(2\pi)^{-s}\zeta(s-1)\beta(s).
\]

## 5. Exact functional-equation constant

Use

\[
 \zeta(s)
 =2^s\pi^{s-1}\sin\!\left(\frac{\pi s}{2}\right)
  \Gamma(1-s)\zeta(1-s)
\]

and the completed beta functional equation

\[
 \left(\frac4\pi\right)^{(u+1)/2}
 \Gamma\!\left(\frac{u+1}{2}\right)\beta(u)
 =
 \left(\frac4\pi\right)^{(2-u)/2}
 \Gamma\!\left(\frac{2-u}{2}\right)\beta(1-u).
\]

Set `u=s-1`. Dividing `M_A(s)` by `M_vee(2-s)` gives

\[
 \frac{\Gamma(s)}{\Gamma(2-s)}
 (2\pi)^{2-2s}
 \frac{\zeta(s)}{\zeta(1-s)}
 \frac{\beta(s-1)}{\beta(2-s)}.
\]

Substitution of the two functional equations reduces this to

\[
 \frac{2^{3-2s}}\pi
 \Gamma\!\left(\frac{s+1}{2}\right)
 \Gamma\!\left(\frac{1-s}{2}\right)
 \sin\!\left(\frac{\pi s}{2}\right).
\]

The reflection identity

\[
 \Gamma\!\left(\frac{s+1}{2}\right)
 \Gamma\!\left(\frac{1-s}{2}\right)
 =\frac\pi{\cos(\pi s/2)}
\]

proves

\[
 \mathcal M_A(s)
 =2^{3-2s}\tan\!\left(\frac{\pi s}{2}\right)
  \mathcal M_\vee(2-s).
\]

Replacing `s` by `2-s` and solving for `M_vee(s)` gives

\[
 \mathcal M_\vee(s)
 =-2^{1-2s}\cot\!\left(\frac{\pi s}{2}\right)
  \mathcal M_A(2-s).
\]

Multiplying both components by `2^s` yields the displayed matrix `J(s)`.

No fixed basis change can make this reflection matrix constant. If `S` is
fixed and invertible, constancy of `S J(s) S^(-1)` would imply constancy of
`J(s)` itself. But its upper-right entry is `2 tan(pi s/2)`. More
invariantly, for generic `s_1,s_2`, the matrices `J(s_1)` and `J(s_2)` do
not commute, whereas scalar multiples of one fixed reflection matrix do.
This proves the stated boundary for the natural pure two-kernel Fricke law.

## 6. Why finite rational repairs fail

The Mellin transform changes an Euler derivative `y d/dy` into multiplication
by `-s`, up to the usual vanishing boundary terms. An Euler antiderivative
divides by an affine function of `s`. A finite period polynomial contributes
only finitely many polar terms after regularized Mellin transformation.
Thus any fixed finite-depth diagonal repair in this model supplies rational
functions of `s` and finitely many exceptional poles.

For example, after nonzero rational diagonal multipliers `u(s),v(s)`, the
upper-right reflection entry becomes

\[
 2\frac{u(s)}{v(2-s)}\tan\!\left(\frac{\pi s}{2}\right).
\]

It cannot be constant: a nonzero rational function has only finitely many
zeros and poles, while tangent has infinitely many alternating zeros and
poles. Finitely many additive polar terms do not change this multiplicative
obstruction. This is the exact finite-depth Eichler/differential scope of the
claim.

## 7. Why the natural Whittaker repair is circular

The quotient

\[
 \tan\!\left(\frac{\pi s}{2}\right)
 =\frac{
 \Gamma((1+s)/2)\Gamma((1-s)/2)}{
 \Gamma(s/2)\Gamma(1-s/2)}
\]

shows how an infinite gamma-factor normalization can constantize the
archimedean reflection. Under inverse Mellin transform, this replaces the
exponential test kernel by a Whittaker or Bessel-type kernel. It does not
alter either Dirichlet series. The resulting two global sums retain the form

\[
 \sum_{n\geq1}A(n)W_A(ny),
 \qquad
 \sum_{n\geq1}A^\vee(n)W_\vee(ny)
\]

for corresponding archimedean kernels. The arithmetic amplitude at index
`n` is unchanged.

At an odd semiprime target `N`, the dual amplitude is exactly
`chi(N)A(N)`. The character sign is public. Hence extraction of either
amplitude is polynomial-time equivalent to extraction of the other, and by
F203 to factoring the target. The functional equation transforms the entire
kernel sum and has no coefficient map from `N` to a smaller integer.

This is an exact circularity statement for the natural Mellin/Whittaker pair.
It is not a lower bound against a completion with genuinely new arithmetic
coefficients or an adaptive integer-specific decoder.
