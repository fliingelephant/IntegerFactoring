# F276 V2 blind reconstruction

## Protocol and authenticated input

This reconstruction was made from the V2 statement alone. Before this file
was sealed, no F276 proof, self-audit, hostile audit, provenance file, V1
claim text, or conversation-derived claim text was read.

Authenticated input:

- `V2_STATEMENT.md` SHA-256:
  `bea005ed8c16878fdb334c12e01f55b4b6569294662e274121e8d1b396f65fea`.
- `V2_FROZEN.sha256` SHA-256:
  `c7af4315d87f4e99a223cf6a30406a71288a55b7a3d3c835cd41aac0cff3f6e8`.

Both computed hashes equal the supplied hashes. The checksum manifest binds
the authenticated statement hash to `V2_STATEMENT.md`.

No numerical search, remote computation, or substantive computer algebra was
used.

## Verdict

**PASS.** All stated algebraic theorems and both positive controls reconstruct
from first principles. The endpoint conclusions also have the stated limited
scope. In particular, the statement does not turn the absence of a supplied
endpoint evaluator or signal law into an impossibility theorem.

Two implementation cautions are essential but do not change the verdict:

1. The rational conjugation in Theorem E can introduce denominators. A modular
   use must audit them.
2. The `c=0` reduction is only a reduction to constant powers and weighted
   sums. It is not a universal failure of the `SIGNAL` condition.

## 1. Ordered products and cocycles

With the rightmost factor acting first, splitting an interval at `y` gives

\[
 A(z-1)\cdots A(y)\;A(y-1)\cdots A(x)=P(y,z)P(x,y),
\]

so the order in the cocycle law is correct.

### Theorem A

Let the entries of `P` be written over a common polynomial denominator. Since
`K` has characteristic zero, it is infinite. Choose `t in K` such that
specializing the first argument to `t` does not annihilate that denominator
or the numerator of `det P`. Only finitely many `t` are excluded: a nonzero
polynomial in two variables can become the zero polynomial in the second
variable at only finitely many values of the first variable.

Set

\[
 G(T)=P(t,T)\in\operatorname{GL}_d(K(T)).
\]

In the cocycle identity, substitute the three arguments `(t,X,Y)`. This gives

\[
 P(X,Y)P(t,X)=P(t,Y).
\]

The second factor is invertible over `K(X)`. Hence

\[
 P(X,Y)=P(t,Y)P(t,X)^{-1}=G(Y)G(X)^{-1}.
\]

Conversely,

\[
 G(Z)G(Y)^{-1}G(Y)G(X)^{-1}=G(Z)G(X)^{-1},
\]

and the diagonal value is the identity. Thus every rational two-endpoint
cocycle is exactly a rational gauge.

Hostile checks:

- Poles do not invalidate the rational identity. They restrict numerical
  specializations and therefore belong to the denominator audit.
- Fixing a base point is valid because characteristic zero makes `K`
  infinite.
- The proof uses rationality critically. A length state, digit state, floor,
  or semilinear operation is not forced into this form.
- No cost bound for constructing or evaluating `G` follows from the identity.

### Theorem B

Put `C=H_1`. Taking `s=1` in the semigroup law gives

\[
 H_{r+1}=CH_r.
\]

Starting from `H_0=I`, induction gives `H_m=C^m`. The reverse order in the
stated law causes no problem. It is the order produced by adjacent interval
composition, and all length states are powers of the same matrix.

At length one,

\[
 A(X)=P(X,X+1)=G(X+1)CG(X)^{-1}.
\]

Multiplication over `m` adjacent steps cancels every intermediate gauge and
gives

\[
 \Pi_A(a,m)=G(a+m)C^mG(a)^{-1}.
\]

It remains to justify the determinant conclusion. Let

\[
 g(X)=\det G(X),\qquad \delta=\det C.
\]

If `det A(X)=1`, then

\[
 \frac{g(X+1)}{g(X)}\delta=1.
\]

For every nonzero rational function, the quotient `g(X+1)/g(X)` tends to
`1` at infinity, or equivalently has leading-term ratio `1`. Therefore
`delta=1`, and `g(X+1)=g(X)`. A nonconstant rational function cannot be
periodic under translation by `1` in characteristic zero. Any finite pole
would generate infinitely many translated poles. With no finite poles the
function is a polynomial, and a periodic polynomial is constant. Thus

\[
 \det C=1,\qquad \det G(X)\in K^*.
\]

Hostile checks:

- The determinant conclusion would fail without rationality. Exponential or
  semilinear gauges can have a nontrivial constant shift ratio.
- The conclusion applies only when the length state separates exactly as in
  the hypothesis. Scale-dependent or digit-dependent composition is outside
  the proof.
- `C^m` can contain useful arithmetic information. The theorem classifies it
  as constant powering; it does not prove that such information cannot be a
  factoring signal.

## 2. The two positive controls

### Rational factorial lift

The factors are diagonal and commute, so

\[
 \Pi_A(1,B)=\operatorname{diag}\left(\prod_{k=1}^B k,
 \prod_{k=1}^B k^{-1}\right)
 =\operatorname{diag}(B!,(B!)^{-1}).
\]

For `N=pq` with `p<q`,

\[
 p<\sqrt{pq}<q.
\]

Hence `p<=B<q`. The prime `p` divides `B!`, while `q` does not, and therefore

\[
 \gcd(B!,N)=p.
\]

But the transition at `X=p` contains `p^{-1}` modulo `N`, which does not
exist. The endpoint expression also asks for `(B!)^{-1}`, which does not
exist. Computing either denominator gcd exposes `p`; skipping the audit makes
the proposed modular matrix product undefined.

In dimension one, determinant one forces the only transition to be `1`.
Thus dimension two is minimal for this rational determinant-one example.
The control is a factorial signal paired with a forbidden reciprocal, not a
valid unit-denominator evaluator.

### Constant Jordan/binomial alias

Since `J^{H+1}=0`, the ordinary binomial theorem gives

\[
 (I+J)^B=\sum_{j=0}^{H}\binom BjJ^j.
\]

The `(1,H+1)` entry of `J^j` is zero except when `j=H`, when it is one. Thus
the displayed entry equals `binom(B,H)`.

Write `B=p+s`. As above, `B>=p` and `B<q<2p`, so `0<=s<p` and `H<p`.
The stronger bound `q<2p` gives

\[
 B<\sqrt2\,p.
\]

For every prime `p>=2`, this implies `s<=p-2`. Hence

\[
 s<\left\lfloor\frac{p+s}{2}\right\rfloor=H.
\]

This also directly holds in the endpoint case `p=2`, where `s=0` and `H=1`.
Consequently

\[
 0\le s<H<p<q.
\]

In base `p`, `B` has digits `(1,s)` and `H` has digits `(0,H)`. Lucas's
theorem gives

\[
 \binom BH\equiv \binom10\binom sH=0\pmod p.
\]

Since `B<q`, every factorial in the formula for `binom(B,H)` is a unit modulo
`q`; therefore the binomial coefficient is nonzero modulo `q`. It follows
that

\[
 \gcd\!\left(\binom BH,N\right)=p.
\]

Balanced semiprimes have `B=Theta(sqrt(N))`, so `H+1=Theta(sqrt(N))`, which
is `2^{Theta(log N)}`. The explicit Jordan state is exponential in the input
bit length. Asking for only its corner entry removes the explicit matrix but
leaves exactly the remote central-binomial evaluation problem. No
numerical-quasipolynomial evaluator for that scalar follows from the matrix
identity.

Hostile checks:

- The signal law includes the smallest balanced case `N=6`.
- The proof that `q` does not divide the binomial coefficient uses primality
  and `B<q`, not a heuristic size comparison.
- Constant powering alone does not make a growing-dimensional state small.
- The argument establishes a missing evaluator, not an evaluator lower bound.

## 3. Polynomial unimodularity

### Theorem C

Let

\[
 v=U(X)e_1,\qquad w=U(X+1)e_1.
\]

Both vectors are unimodular: their coordinates generate the unit ideal,
because each is a column of an invertible matrix over `R`. The matrix `A` is
also invertible over `R`, so `Av` is unimodular.

Even if the scalar in the displayed equation were initially interpreted in
the fraction field, unimodularity of `w` first forces it into `R`. Indeed,
there is a row `ell` over `R` with `ell w=1`, and

\[
 \lambda=\ell(Av)\in R.
\]

Now

\[
 R=I(Av)=I(\lambda w)=\lambda I(w)=\lambda R.
\]

Therefore `lambda` is a unit of `R`. The units of `K[X]` are `K^*`, and the
units of `Z[X]` are `+1` and `-1`.

Hostile checks:

- The direct-summand hypothesis is doing the work. If the moving vector does
  not extend to a unimodular polynomial frame, its coordinate ideal can hide
  a nonunit.
- A rational change of frame can move the nonunit into a denominator. That
  denominator and the cost of constructing the frame must then be audited.
- The theorem concerns an invariant line with a scalar multiplier. It does
  not forbid one selected coordinate of a general moving state from acquiring
  a factor.

### Theorem D

Every coordinate of `Mv` is an `R`-linear combination of coordinates of
`v`, so `I(Mv)` is contained in `I(v)`. Apply the same argument to `M^{-1}`
and `Mv` to get the reverse containment. Hence

\[
 I(Mv)=I(v).
\]

Over the integers, equality of coordinate ideals is equality of coordinate
gcds up to the usual positive normalization. Products of determinant-one
integer matrices are invertible over the integers, so they preserve this
gcd. Applying the result to standard basis vectors proves that every column
is primitive; applying it to the transpose proves the same for rows.

This is only a global obstruction. For example,

\[
 \begin{pmatrix}p&1\\p-1&1\end{pmatrix}
\]

has determinant one and has a selected entry divisible by `p`, while its
first column remains primitive. Thus a selected-entry signal is compatible
with Theorem D.

The determinant, adjugate, and Cayley-Hamilton identities are universal
matrix relations. If one extracts a scalar residue that vanishes for every
determinant-one matrix, its gcd with `N` is `N`, not a proper factor. A useful
signal must instead be asymmetric between the hidden prime factors.

## 4. Affine `SL_2` normal form

### Theorem E: classification

The constant term of `det(C+XD)=1` gives `det C=1`, so
`C in SL_2(Z)` and `C^{-1}` is integral. Put `B_0=C^{-1}D`. Then

\[
 A(X)=C(I+XB_0)
\]

and

\[
 1=\det(I+XB_0)
   =1+X\operatorname{tr}B_0+X^2\det B_0.
\]

Comparison of coefficients gives `tr B_0=0` and `det B_0=0`.
Cayley-Hamilton for a two-by-two matrix now gives `B_0^2=0`.

If `D` is nonzero, then `B_0` is a nonzero rank-one nilpotent matrix over
`Q`. Choose a vector `u` in its image and a vector `v` with `B_0v=u`.
In the basis `(u,v)`, its matrix is `E_12`. This proves the constant rational
normalization.

The rational basis change preserves determinant one, but it need not be
unimodular over `Z`. Any modular implementation must audit the denominators
in the basis and in the conjugated coefficients.

### Theorem E: recurrence

After normalization,

\[
 \widetilde C(I+kE_{12})
 =\begin{pmatrix}a&ak+b\\c&ck+d\end{pmatrix}.
\]

Thus

\[
 y_{k+1}=cx_k+(ck+d)y_k.
\]

At the next step,

\[
 y_{k+2}=cx_{k+1}+(c(k+1)+d)y_{k+1}.
\]

The first-coordinate update and `ad-bc=1` give

\[
 \begin{aligned}
 cx_{k+1}
 &=acx_k+(ack+bc)y_k\\
 &=a y_{k+1}+(bc-ad)y_k\\
 &=a y_{k+1}-y_k.
 \end{aligned}
\]

Substitution yields

\[
 y_{k+2}=(ck+a+c+d)y_{k+1}-y_k.
\]

No division by `c` was used, so the formula also covers `c=0`.

### The `c=0` boundary

When `c=0`, the matrix `C` is upper triangular and preserves the nilpotent
line `span(e_1)`. The recurrence coefficient becomes the constant `a+d`.
More explicitly, for an interval starting at `r`, write

\[
 M_k=\begin{pmatrix}a&ak+b\\0&d\end{pmatrix}.
\]

Then

\[
 M_{r+m-1}\cdots M_r
 =\begin{pmatrix}a^m&u_m\\0&d^m\end{pmatrix},
\]

where

\[
 u_m=\sum_{j=0}^{m-1}a^{m-1-j}\bigl(a(r+j)+b\bigr)d^j.
\]

This is exactly a constant-power expression plus geometric-weighted
degree-one sums. The formula also covers the repeated-ratio cases without
requiring division by `a-d`.

When `c` is nonzero, the recurrence operator has a genuinely nonconstant
affine coefficient. This normal form neither supplies a fast remote evaluator
nor rules one out. Special initial states can still degenerate, and special
coefficient choices can still have extra structure. Therefore no universal
`ENDPOINT`, `SIGNAL`, or impossibility conclusion follows for this branch.

Hostile checks:

- `D=0` is already a constant-matrix system. The rational normalization is
  asserted only for `D!=0`.
- The distinction `c=0` versus `c!=0` is intrinsic after choosing the
  nilpotent normal form: it says whether `C` preserves the kernel/image line
  of the rank-one nilpotent.
- The classification uses both dimension two and affine dependence. Higher
  degree, higher dimension, and several shears in one step are not reduced by
  this argument.
- The easy branch is not a signal failure. It moves the remaining question
  into the separate constant-power lane.

## 5. Holonomic certificate and endpoint boundary

Consider a fixed rational system `z_{n+1}=A(n)z_n` and one scalar coordinate
`y_n=e_i^Tz_n`. Relative to `z_n`, the `d+1` shifted values are obtained from
the row covectors

\[
 e_i^T,\ e_i^TA(n),\ e_i^TA(n+1)A(n),\ldots,
 e_i^TA(n+d-1)\cdots A(n).
\]

These are `d+1` vectors in a `d`-dimensional vector space over `K(n)`, so
they are linearly dependent over `K(n)`. Applying that relation to `z_n`
gives a rational-coefficient scalar recurrence whose order is at most `d`.
The identity is valid away from its rational poles; modular use again
requires a denominator audit.

This proof is a certificate of recurrence order only. Sequential evaluation
still performs one update per index. A generic product tree still constructs
all leaves. Linear dependence supplies neither a remote endpoint formula nor
a complexity improvement. Conversely, this observation is not a lower bound
against a special fast evaluator.

The five endpoint labels are logically separate:

- `LOCAL` controls construction of one transition.
- `STATE` controls the size and operations of the chosen representation.
- `ENDPOINT` requires an independent fast evaluation method at remote length.
- `UNIT` makes every modular division valid or turns a failed division into a
  certified factor.
- `SIGNAL` requires an exact asymmetric law for all intended inputs.

The factorial lift passes the scalar signal check but fails `UNIT`. The
Jordan lift has an exact signal but its explicit state is exponential, and
the implicit version merely restates the missing scalar endpoint evaluator.
A fixed-order recurrence can pass `LOCAL` while failing to supply `ENDPOINT`.
A universal determinant identity fails to give a proper-factor `SIGNAL`.

## 6. Final adversarial scope audit

The reconstructed implications justify rejecting a search whose only basis
is one of the following:

- a rational two-endpoint cocycle;
- an exactly separable length law;
- a nonunit multiplier on a polynomial unimodular direct-summand line;
- a common factor in every coordinate under unimodular transport; or
- the mere reduction of the affine `c=0` branch.

Each premise has already reduced respectively to a gauge, constant powering,
a unit, a preserved global ideal, or a constant-power weighted sum. A search
could still be justified by a new exact signal law and a separate endpoint
algorithm. Those are additional inputs, not consequences of the five
mechanisms.

Nothing reconstructed here proves a lower bound for arbitrary
determinant-one systems. It also does not cover nonlinear or semilinear
states, digit or Frobenius recurrences, adaptive computation, implicit large
Jordan states, the generic affine continuant, higher polynomial degree,
higher dimension, or multiple shears per step. It supplies no factoring
algorithm and no empirical claim.

The generic affine recurrence remains an open mathematical lane. Finite
divisibility samples would test the `SIGNAL` condition only on those samples.
Without an independently specified numerical-quasipolynomial endpoint
operation, they would not establish the required resource-bearing
construction.

## Sealed blind conclusion

The authenticated V2 statement is internally correct under its stated
hypotheses. Its exclusions are scoped to the mechanisms it proves. The two
positive controls demonstrate that exact divisibility alone is insufficient:
one must also pass state size, endpoint cost, and modular-unit checks. The
`c=0` affine branch is correctly left open to separately justified
constant-power signals, and the `c!=0` branch is correctly left open rather
than declared impossible.
