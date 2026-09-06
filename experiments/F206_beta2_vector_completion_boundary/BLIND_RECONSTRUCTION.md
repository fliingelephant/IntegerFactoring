# F206 blind reconstruction: vector-completion boundary

## Blindness record

This reconstruction used only the repository-root `PROMPT.md` and this
experiment's `STATEMENT.md`. Before either file was opened, the SHA-256 hash
of `STATEMENT.md` was checked and found to be

```text
a35bfc475cb068bab78cb3f12bae605492ab22f4b208b6c809f7692f1cd4805c
```

No proof, audit, provenance, manifest, ledger, or prior proof message was
used.

Write \(\beta(s)=L(s,\chi_4)\). Thus \(\chi_4(a)=0\) for even \(a\), and
\(\chi_4(a)=1\) or \(-1\) according as \(a\equiv1\) or \(3\pmod4\).

## 1. The Lambert identity and the radial asymptotics

Absolute convergence for \(|q|<1\) permits logarithmic differentiation:

\[
\begin{aligned}
-q\frac{d}{dq}\log P(q)
&=\sum_{a\geq1}\chi_4(a)\frac{a q^a}{1-q^a}\\
&=\sum_{a,m\geq1}a\chi_4(a)q^{am}\\
&=\sum_{n\geq1}\left(\sum_{a\mid n}a\chi_4(a)\right)q^n
=L(q).
\end{aligned}
\]

### 1.1. The product at \(q=e^{-t}\)

Put \(Q=e^{-4t}\). The product can be written as

\[
P(e^{-t})=\frac{(Q^{1/4};Q)_\infty}{(Q^{3/4};Q)_\infty}.
\]

The \(Q\)-gamma identity

\[
(Q^x;Q)_\infty
=(1-Q)^{1-x}\frac{(Q;Q)_\infty}{\Gamma_Q(x)}
\]

therefore gives

\[
P(e^{-t})=(1-Q)^{1/2}
\frac{\Gamma_Q(3/4)}{\Gamma_Q(1/4)}.
\]

As \(Q\uparrow1\), \(\Gamma_Q(x)\to\Gamma(x)\), and
\(1-e^{-4t}\sim4t\). Hence

\[
\boxed{
P(e^{-t})\sim
2\frac{\Gamma(3/4)}{\Gamma(1/4)}\sqrt t.}
\]

For \(x\in(0,1)\), all relevant products converge absolutely and

\[
\begin{aligned}
P(-x)
&=\prod_{a\geq1}(1+x^a)^{\chi_4(a)}\\
&=\prod_{a\geq1}
\left(\frac{1-x^{2a}}{1-x^a}\right)^{\chi_4(a)}
=\frac{P(x^2)}{P(x)}.
\end{aligned}
\]

Using the first asymptotic twice, with \(x=e^{-t}\), yields

\[
\boxed{P(-e^{-t})=\frac{P(e^{-2t})}{P(e^{-t})}\longrightarrow\sqrt2.}
\]

### 1.2. The two Lambert expansions

For \(c>2\), Mellin inversion gives

\[
L(e^{-t})=\frac1{2\pi i}\int_{(c)}
\Gamma(s)\zeta(s)\beta(s-1)t^{-s}\,ds.
\]

The special values needed when the contour is moved left are

\[
\beta(0)=\frac12,\qquad
\beta(-1)=0,\qquad
\beta(-2)=-\frac12,\qquad
\beta(-3)=0.
\]

They follow directly from

\[
\beta(u)=4^{-u}\bigl(\zeta(u,1/4)-\zeta(u,3/4)\bigr)
\]

and \(\zeta(-m,a)=-B_{m+1}(a)/(m+1)\). In particular,
\(B_2(1/4)=B_2(3/4)\),
\(B_3(1/4)=3/64=-B_3(3/4)\), and
\(B_4(1/4)=B_4(3/4)\).

The pole of \(\zeta(s)\) at \(s=1\) has residue one, so the residue there
is \(\beta(0)t^{-1}=1/(2t)\). The apparent pole at \(s=0\) is canceled by
\(\beta(-1)=0\). At \(s=-1\), the residue is

\[
\operatorname*{Res}_{s=-1}
\Gamma(s)\zeta(s)\beta(s-1)t^{-s}
=(-1)\left(-\frac1{12}\right)\left(-\frac12\right)t
=-\frac{t}{24}.
\]

At \(s=-2\), the pole of \(\Gamma(s)\) is canceled by
\(\zeta(-2)=0\) (and also by \(\beta(-3)=0\)). The next possible residue
has order \(t^3\). Standard vertical-strip bounds for \(\zeta\) and
\(\beta\), together with the exponential decay of \(\Gamma\), justify a
shift past \(s=-3\). Its residue and the new contour are \(O(t^3)\). Thus

\[
\boxed{L(e^{-t})=\frac1{2t}-\frac{t}{24}+O(t^3).}
\]

If \(q(t)=\pm e^{-t}\), then \(q'(t)=-q(t)\), so

\[
\frac{d}{dt}\log P(q(t))=L(q(t)).
\]

Differentiating \(P(-e^{-t})=P(e^{-2t})/P(e^{-t})\) gives the exact
identity

\[
L(-e^{-t})=2L(e^{-2t})-L(e^{-t}).
\]

The positive-radial expansion now gives

\[
\boxed{L(-e^{-t})=-\frac{t}{8}+O(t^3).}
\]

### 1.3. Cusp powers

For \(\tau=iy\), set \(t=2\pi y\), so \(q=e^{-t}\). For
\(\tau=1/2+iy\), one has \(q=-e^{-t}\). The results above give

\[
\begin{array}{c|cc}
&\tau\to0&\tau\to1/2\\ \hline
P(q)&y^{1/2}&y^0\\
R(q)=P(q)/P(-q)&y^{1/2}&y^{-1/2}\\
L(q)&y^{-1}&y^1.
\end{array}
\]

For the middle entry at \(1/2\), note explicitly that

\[
R(-e^{-t})=\frac{P(-e^{-t})}{P(e^{-t})}\asymp t^{-1/2}.
\]

All six leading constants are nonzero: the gamma values are finite and
positive, the limiting value at the negative radius is \(\sqrt2\), and the
leading Lambert constants are \(1/2\) and \(-1/8\).

## 2. The semisimple vector cusp lemma

Let \(r=a/c\) be a finite rational cusp, in lowest terms, and choose a
scaling matrix

\[
\sigma=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad ad-bc=1.
\]

If \(\tau=r+iy\), direct calculation gives

\[
z=\sigma^{-1}\tau=-\frac dc+\frac{i}{c^2y},
\qquad
cz+d=\frac{i}{cy}.
\]

Let \(F_\sigma=F|_k\sigma\), including any fixed basis change used to
diagonalize the cusp monodromy. The assumed ordinary meromorphic Puiseux
expansion has, in every coordinate, the form

\[
\sum_{\lambda\in S}v_\lambda e^{2\pi i\lambda z/h},
\]

where \(S\) is discrete and bounded below, and only finitely many
\(\lambda\) are negative. The absence of a parabolic Jordan block is what
excludes factors that are polynomials in \(z\), equivalently logarithmic
Fourier terms.

After applying a fixed linear functional and restricting to
\(\Re z=-d/c\), combine all terms with the same exponent and select the
least exponent with a nonzero combined coefficient. A negative exponent
gives exponential growth as \(y\downarrow0\). A positive exponent gives
exponential decay. Exponent zero gives a nonzero constant plus an
exponentially small error. These exhaust the possibilities because the
principal part is finite and the exponents are discrete.

The inverse slash relation contributes

\[
(cz+d)^k=\left(\frac{i}{cy}\right)^k=C_{\sigma,k}y^{-k},
\qquad C_{\sigma,k}\ne0.
\]

Consequently, if

\[
(\ell F)(r+iy)\sim Cy^\alpha,
\qquad C\ne0,
\]

and this behavior is neither exponentially growing nor exponentially
decaying, the local Fourier exponent must be zero. It follows that

\[
\boxed{\alpha=-k.}
\]

The weight \(k\) is fixed, so the same polynomial exponent must occur at
every rational cusp where such an asymptotic is nonzero. The two exponents
for each row of the table are different:

\[
\frac12\ne0,\qquad
\frac12\ne-\frac12,\qquad
-1\ne1.
\]

Therefore no fixed projection of a finite-dimensional meromorphic
vector-valued modular form satisfying the stated semisimple cusp hypothesis
can equal \(P\), \(R\), or \(L\).

This proof uses both parts of the hypothesis. A nonholomorphic correction
can change the radial power of a holomorphic part. A parabolic Jordan block
can create powers of \(z\), hence powers of \(1/y\) or logarithmic local
terms. Neither case is covered by the lemma.

## 3. The dual coefficients and the exact Mellin reflection

### 3.1. The same-index coefficient identity

If \(n\) is odd, every divisor \(d\mid n\) is odd. Complete
multiplicativity of \(\chi_4\) and \(\chi_4(d)^2=1\) give

\[
\chi_4(n/d)=\chi_4(n)\chi_4(d).
\]

Thus

\[
\boxed{
A^\vee(n)=\sum_{d\mid n}d\chi_4(n/d)
=\chi_4(n)\sum_{d\mid n}d\chi_4(d)
=\chi_4(n)A(n).}
\]

This is an identity at the same index \(n\).

### 3.2. Dirichlet and Mellin products

For \(\Re s>2\), absolute convergence permits rearrangement:

\[
\begin{aligned}
\sum_{n\geq1}\frac{A(n)}{n^s}
&=\sum_{d,m\geq1}\frac{d\chi_4(d)}{(dm)^s}
=\zeta(s)\beta(s-1),\\
\sum_{n\geq1}\frac{A^\vee(n)}{n^s}
&=\sum_{d,m\geq1}\frac{d\chi_4(m)}{(dm)^s}
=\zeta(s-1)\beta(s).
\end{aligned}
\]

Termwise Mellin integration, using

\[
\int_0^\infty e^{-2\pi ny}y^{s-1}\,dy
=\Gamma(s)(2\pi n)^{-s},
\]

gives

\[
\boxed{
\mathcal M_A(s)=\Gamma(s)(2\pi)^{-s}\zeta(s)\beta(s-1),}
\]

\[
\boxed{
\mathcal M_\vee(s)=\Gamma(s)(2\pi)^{-s}\zeta(s-1)\beta(s).}
\]

The formulas also define their meromorphic continuations.

### 3.3. Reflection and its constants

Use the completed functional equations

\[
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=\pi^{-(1-s)/2}\Gamma((1-s)/2)\zeta(1-s)
\]

and, for the primitive odd character of conductor four,

\[
\left(\frac4\pi\right)^{(u+1)/2}
\Gamma((u+1)/2)\beta(u)
=
\left(\frac4\pi\right)^{(2-u)/2}
\Gamma((2-u)/2)\beta(1-u).
\]

With \(u=s-1\), these yield

\[
\frac{\zeta(s)}{\zeta(1-s)}
=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}
\]

and

\[
\frac{\beta(s-1)}{\beta(2-s)}
=\left(\frac4\pi\right)^{(3-2s)/2}
\frac{\Gamma((3-s)/2)}{\Gamma(s/2)}.
\]

Therefore

\[
\frac{\mathcal M_A(s)}{\mathcal M_\vee(2-s)}
=(2\pi)^{2-2s}\frac{\Gamma(s)}{\Gamma(2-s)}
\frac{\zeta(s)}{\zeta(1-s)}
\frac{\beta(s-1)}{\beta(2-s)}.
\]

The powers outside the gamma quotient combine to \(2^{5-4s}\). The
duplication and reflection formulas give

\[
\frac{\Gamma(s)}{\Gamma(2-s)}
\frac{\Gamma((1-s)/2)\Gamma((3-s)/2)}{\Gamma(s/2)^2}
=2^{2s-2}\tan\left(\frac{\pi s}{2}\right).
\]

It follows, first where both sides are regular and then everywhere by
meromorphic continuation, that

\[
\boxed{
\mathcal M_A(s)=2^{3-2s}\tan\left(\frac{\pi s}{2}\right)
\mathcal M_\vee(2-s).}
\]

Replace \(s\) by \(2-s\) and use
\(\tan(\pi-\pi s/2)=-\tan(\pi s/2)\). The inverse relation is

\[
\mathcal M_\vee(s)
=-2^{1-2s}\cot\left(\frac{\pi s}{2}\right)
\mathcal M_A(2-s).
\]

For

\[
\widetilde{\mathcal M}(s)
=2^s\binom{\mathcal M_A(s)}{\mathcal M_\vee(s)},
\]

the two relations become

\[
\boxed{
\widetilde{\mathcal M}(s)=J(s)\widetilde{\mathcal M}(2-s),\qquad
J(s)=
\begin{pmatrix}
0&2\tan(\pi s/2)\\
-\tfrac12\cot(\pi s/2)&0
\end{pmatrix}.}
\]

As a consistency check, \(J(s)J(2-s)=I\).

### 3.4. No constant Fricke matrix for the exponential pair

The displayed matrix is not constant. A fixed basis change \(B\) sends it
to \(BJ(s)B^{-1}\). If that expression were constant, multiplication by
\(B^{-1}\) and \(B\) would make \(J(s)\) constant, which is impossible.

One can also rule out a different constant matrix law for the actual pair,
not only a constant conjugate of \(J\). Suppose

\[
\widetilde{\mathcal M}(s)=K\widetilde{\mathcal M}(2-s)
\]

for a constant matrix \(K=(k_{ij})\). Put \(u=2-s\). Comparing the first
row with the proved reflection gives

\[
k_{11}\widetilde{\mathcal M}_A(u)
+k_{12}\widetilde{\mathcal M}_\vee(u)
=-2\tan(\pi u/2)\widetilde{\mathcal M}_\vee(u).
\]

If \(k_{11}=0\), this would make a nonconstant tangent function constant.
If \(k_{11}\ne0\), it would imply

\[
\frac{\widetilde{\mathcal M}_A(u)}
{\widetilde{\mathcal M}_\vee(u)}
=\frac{-2\tan(\pi u/2)-k_{12}}{k_{11}}.
\]

For real \(u\to+\infty\), the quotient on the left tends to one because
each absolutely convergent Dirichlet product tends to one. Along
\(u=4m+1/2\), the tangent is one. Along \(u=4m+3/2\), it is minus one.
The two right-hand limits cannot both equal one. Hence no constant \(K\)
exists. In the stated conductor normalization, the two pure exponential
kernels therefore do not have an ordinary constant-matrix Fricke law.

## 4. Why finite rational repairs do not remove the obstruction

Let \(E=y\,d/dy\). Up to boundary terms,

\[
\mathcal M[Ef](s)=-s\mathcal M[f](s).
\]

A finite number of Euler derivatives multiplies a Mellin transform by a
polynomial in \(s\). A finite number of Euler antiderivatives divides by
such polynomials. Integration constants and finite period polynomials add
only finitely many monomial terms. Their regularized Mellin transforms have
only finitely many poles. Thus a finite-depth diagonal differential or
Eichler repair can change the homogeneous Mellin multipliers only by
rational functions of \(s\), apart from finitely many polar terms.

The function \(\tan(\pi s/2)\) has zeros at every even integer and poles at
every odd integer. The function \(\cot(\pi s/2)\) has the reverse divisor.
A nonzero rational function has only finitely many zeros and poles on the
Riemann sphere. It can cancel only finitely many members of either infinite
alternating divisor. Finitely many additive polar terms do not change this
conclusion away from their finite support.

Therefore no repair made from finitely many Euler derivatives,
antiderivatives, and period-polynomial terms can turn the displayed
two-kernel scattering factors into constants. This is exactly a
finite-depth statement in the diagonal Mellin model. It says nothing about
an arbitrary nonpolynomial quantum cocycle.

## 5. A nonlocal kernel repair exists, but it is arithmetically circular

Define

\[
D(s)=\Gamma(s/2)\Gamma(1-s/2),\qquad
N(s)=\Gamma((1+s)/2)\Gamma((1-s)/2).
\]

Euler's reflection formula gives

\[
D(s)=\frac{\pi}{\sin(\pi s/2)},\qquad
N(s)=\frac{\pi}{\cos(\pi s/2)},\qquad
\boxed{\tan(\pi s/2)=\frac{N(s)}{D(s)}}.
\]

It also gives

\[
D(2-s)=D(s),\qquad N(2-s)=-N(s).
\]

This permits an explicit archimedean absorption. Set

\[
U_A(s)=D(s)\widetilde{\mathcal M}_A(s),\qquad
U_\vee(s)=-N(s)\widetilde{\mathcal M}_\vee(s).
\]

Substitution in the two rows of the reflection law gives the constant
system

\[
\boxed{
\binom{U_A(s)}{U_\vee(s)}
=
\begin{pmatrix}0&2\\[2pt]1/2&0\end{pmatrix}
\binom{U_A(2-s)}{U_\vee(2-s)}.}
\]

The new factors are genuinely nonlocal kernel factors, not rational
finite-depth factors. For example, on their fundamental strips,

\[
D(s)=\int_0^\infty\frac{2}{1+x^2}x^{s-1}\,dx,
\qquad
N(s)=\int_0^\infty\frac{2x}{1+x^2}x^{s-1}\,dx.
\]

They can therefore be implemented by multiplicative Mellin convolution,
or equivalently by the corresponding Whittaker-type archimedean kernels.

Such a convolution changes only the kernel. If

\[
f(y)=\sum_{n\geq1}a(n)\phi(ny)
\]

and

\[
(h*_\times f)(y)=\int_0^\infty h(x)f(y/x)\frac{dx}{x},
\]

then, in a common convergence strip and subsequently by continuation,

\[
(h*_\times f)(y)
=\sum_{n\geq1}a(n)(h*_\times\phi)(ny).
\]

The index \(n\) and coefficient \(a(n)\) do not change. Hence the two
corrected components still carry \(A(n)\) and \(A^\vee(n)\).

At every odd target \(N\),

\[
[n=N]\text{ in the dual component}
=A^\vee(N)=\chi_4(N)A(N).
\]

The sign \(\chi_4(N)\) is public and computable from \(N\bmod4\). Since it
is \(\pm1\), either amplitude determines the other with constant arithmetic
overhead. The repair has moved an archimedean gamma factor. It has not moved
the hidden arithmetic information to a smaller index.

For completeness, this equivalence is exact in the distinct odd semiprime
selector setting. If \(N=pq\), then

\[
A(N)=(1+p\chi_4(p))(1+q\chi_4(q)).
\]

If \(N\equiv1\pmod4\), the two prime characters agree. When \(A(N)>N\),
\(p+q=A(N)-N-1\). When \(A(N)<N\),
\(p+q=N+1-A(N)\). The two primes are then the roots of
\(X^2-(p+q)X+N\). If \(N\equiv3\pmod4\), label the prime congruent to one
modulo four as \(p\) and the other as \(q\). Then

\[
p-q=A(N)+N-1,
\qquad
p+q=\sqrt{(p-q)^2+4N},
\]

which again recovers both primes. Exact integer square root and the final
verification take polynomial bit complexity. Because
\(A(N)=\chi_4(N)A^\vee(N)\), access to the repaired dual amplitude at the
same index is factoring-equivalent to access to the original amplitude.

The Mellin reflection acts on the full kernel sum. The substitution
\(s\mapsto2-s\) is not a map \(N\mapsto N'\) on Fourier indices. It gives
no smaller public child and no remote-coefficient recurrence. Directly
forming either Lambert series through \(q^N\) touches or stores
\(\Theta(N)\) coefficient positions. Since the input length is
\(\Theta(\log N)\), this cost is exponential in the input length and is not
quasipolynomial in that length.

## 6. Exact scope of the result

The proved exclusions are limited to the following objects.

1. The cusp argument excludes an exact component or fixed projection of an
   ordinary finite-dimensional meromorphic vector-valued modular form of
   one fixed weight, with semisimple parabolic monodromy and finite
   meromorphic Puiseux principal parts.
2. The Mellin argument excludes a constant Fricke matrix for the displayed
   pair of pure exponential Lambert kernels.
3. The repair argument excludes only finite-depth diagonal combinations of
   Euler derivatives, Euler antiderivatives, and finite period-polynomial
   terms.
4. The circularity argument applies to the natural two-component
   Whittaker or Mellin-convolution repair that retains the coefficient
   sequences \(A\) and \(A^\vee\).

It does not exclude nonsemisimple vector forms with logarithmic cusp data,
a mock or nonholomorphic completion with a genuinely new arithmetic shadow,
nonpolynomial quantum cocycles, state dimension growing
quasipolynomially with the input length, nonlinear arithmetic identities,
or adaptive integer-specific decoders that exhibit a smaller public child.

In particular, this result is not a lower bound against all vector-valued
or nonholomorphic methods. It is not a coefficient evaluator and is not a
factoring algorithm. A positive continuation must give an explicit
quasipolynomial remote-coefficient recurrence or an explicit smaller public
arithmetic state. Merely placing \(A(N)\) in the \(N\)-th amplitude of a
completed object does not evaluate it.
