# Proof of F276 V2

The mathematical proofs are unchanged from frozen V1. V2 narrows only the
search disposition of the reducible affine branch. The reduction to constant
powering is proved below; no universal failure of a separate constant-power
signal is asserted.

## 1. Rational endpoint cocycles

Choose `x_0 in K` at which the finitely many denominators needed below do
not vanish. This is possible because `K` has characteristic zero and is
infinite. Define

\[
 G(Y)=P(x_0,Y).
\tag{25}
\]

Substitute `(X,Y,Z)=(x_0,X,Y)` in the cocycle identity. It gives

\[
 P(X,Y)P(x_0,X)=P(x_0,Y).
\tag{26}
\]

The matrices are generically invertible, so

\[
 P(X,Y)=P(x_0,Y)P(x_0,X)^{-1}=G(Y)G(X)^{-1}.
\tag{27}
\]

Conversely, direct cancellation proves

\[
 G(Z)G(Y)^{-1}G(Y)G(X)^{-1}=G(Z)G(X)^{-1}.
\]

This proves Theorem A. If a rational candidate is initially asserted only
on all integer endpoint triples outside its poles, clearing denominators
gives polynomial identities on a Zariski-dense subset of characteristic
zero. The same rational identity follows.

## 2. Separable length states

Set `C=H_1`. Equation (6) with `s=1` gives

\[
 H_{m+1}=H_1H_m=CH_m.
\]

Starting from `H_0=I`, induction gives `H_m=C^m`. Substituting `y=X+1`
in (5) proves (8). Multiplying adjacent steps, or substituting `y=a+m`,
proves (9).

Now assume `det A(X)=1`. Put

\[
 r(X)=\det G(X),\qquad \gamma=\det C.
\]

Taking determinants in (8) gives

\[
 1=\gamma\frac{r(X+1)}{r(X)}.
\tag{28}
\]

For every nonzero rational function, `r(X+1)/r(X)` tends to one at
infinity. Therefore `gamma=1`. Equation (28) then says

\[
 r(X+1)=r(X).
\tag{29}
\]

A characteristic-zero rational function with period one is constant. One
proof is to note that a finite pole would generate infinitely many
translated poles; hence there are no finite poles and `r` is a polynomial.
A nonconstant polynomial cannot be periodic because its first forward
difference has one smaller degree and is nonzero. Thus `r in K^*`, proving
(10).

Constant determinant does not make every entry of `G` denominator-free. A
modular use of (9) still requires every inverse represented in the chosen
normal form to exist. If an endpoint denominator has proper gcd with `N`,
that gcd is already a factor. If its gcd is `N`, the displayed inverse is
undefined and supplies no residue. Cancellation is valid only after an
explicit denominator-free normal form is exhibited.

## 3. The rational factorial control

Every matrix in (11) has determinant one in `Q(X)`. The factors commute, so

\[
 \begin{aligned}
 \Pi_A(1,B)
 &=\prod_{k=1}^{B}
   \begin{pmatrix}k&0\\0&k^{-1}\end{pmatrix}\\
 &=\begin{pmatrix}\prod_{k=1}^{B}k&0\\
                   0&\prod_{k=1}^{B}k^{-1}
   \end{pmatrix},
 \end{aligned}
\]

which is (12).

From `p<q` one has `p<=B<q`. Therefore exactly one of `p,q` divides `B!`,
and

\[
 \gcd(B!,N)=p.
\]

But the individual factor with `k=p` contains `p^{-1}`. The same nonunit is
present in `(B!)^{-1}`. Thus the proposed determinant-one lift has paired
the factor-bearing scalar with an inverse that is undefined modulo `N`.

Finally, `SL_1` contains only the scalar one, so dimension two is minimal
for this rational determinant-one construction.

## 4. The Jordan/binomial control

For the nilpotent Jordan shift, `J^{H+1}=0`. The ordinary binomial theorem
therefore gives (14), and only `J^H` contributes to entry `(1,H+1)`.

Write `B=p+s`. We first verify the range used in the statement. The balanced
inequalities imply

\[
 p\leq B<q<2p,
\tag{30}
\]

so `0<=s<p`. Also `pq<2p^2`, hence `B<sqrt(2)p`. This gives `p>B/sqrt(2)`.
For even `B`, it immediately implies `s=B-p<B/2=H`.

For odd `B=2H+1`, the only way to have `s>=H` is `p<=H+1`. Since
`p>B/2`, this forces `p=H+1` and `B=2p-1`. But for every odd prime
`p>=3`,

\[
 (2p-1)^2>2p^2>pq,
\]

contradicting `B^2<=pq`. Thus `s<H` also in the odd case. Clearly `H<p`
and `B<q`.

In base `p`, `B` has digits `(1,s)` and `H` has digits `(0,H)`. Lucas's
theorem gives

\[
 \binom BH\equiv\binom10\binom sH=0\pmod p.
\tag{31}
\]

Because `0<=H<=B<q`, none of the integers in the factorial formula for
`binom(B,H)` is divisible by `q`; consequently the binomial coefficient is
nonzero modulo `q`. Equation (15) follows.

The explicit Jordan state has `H+1` basis vectors. Since
`B=2^{Theta(log N)}`, this dimension is exponential in the input bit length.
If the matrix is represented implicitly and only its corner entry is
requested, (14) identifies that request exactly with evaluating
`binom(B,H) mod N`. No cost improvement follows from changing its name to a
matrix-power entry.

## 5. Unimodular direct-summand multipliers

Define

\[
 M(X)=U(X+1)^{-1}A(X)U(X).
\tag{32}
\]

Because `U` is invertible over the polynomial ring, its determinant is a
unit and is constant in `X`. Therefore

\[
 \det M(X)=1.
\tag{33}
\]

Equation (16) says that the first column of `M` is

\[
 (\lambda,0,\ldots,0)^T.
\]

Expansion of the determinant along that column gives

\[
 1=\lambda(X)\det M_{[2..d],[2..d]}(X).
\tag{34}
\]

Thus `lambda` has a multiplicative inverse in `R`; it is a unit. The units
of `K[X]` are the nonzero constants and the units of `Z[X]` are `+1,-1`.
This proves Theorem C.

If a proposed moving frame is invertible only over `K(X)`, equation (32)
uses its rational inverse. A nonunit determinant or an entry denominator of
that frame is then part of the construction. Theorem C does not replace its
required modular unit audit.

## 6. Coordinate ideals and global identities

Every coordinate of `Mv` is an `R`-linear combination of the coordinates
of `v`, so

\[
 I(Mv)\subseteq I(v).
\]

Apply the same argument to `v=M^{-1}(Mv)` to get the reverse inclusion.
This proves (18).

For `R=Z`, the positive generator of the coordinate ideal is the coordinate
gcd, so it is preserved. If `P in SL_d(Z)`, a row of `P^{-1}` has dot
product one with the corresponding column of `P`; hence that column is
primitive. The row statement follows by transposition.

Determinant multiplicativity proves `det Pi_A=1`. The adjugate identity and
Cayley-Hamilton are polynomial identities over the integers, so reducing
them modulo either hidden prime gives the same zero. Taking a gcd of such a
global zero with `N` returns `N`.

## 7. Affine `SL_2` normal form

Expand the determinant polynomial:

\[
 \det(C+XD)
 =\det C
 +X\operatorname{tr}(\operatorname{adj}(C)D)
 +X^2\det D.
\tag{35}
\]

It is identically one. Hence

\[
 \det C=1,
 \qquad
 \operatorname{tr}(C^{-1}D)=0,
 \qquad
 \det(C^{-1}D)=0.
\tag{36}
\]

Since `C in SL_2(Z)`, its inverse is integral, so `B_0=C^{-1}D` is an
integer matrix. Cayley-Hamilton for `B_0` gives

\[
 B_0^2-(\operatorname{tr}B_0)B_0+(\det B_0)I=0.
\]

Both scalar coefficients vanish, proving `B_0^2=0` and (21).

If `B_0` is nonzero, it has rank one and one nilpotent Jordan block. A
constant rational basis therefore puts it in the form `E_12`. Conjugate
`C` by the same basis and write it as in (22).

From (23),

\[
 \begin{aligned}
 x_{k+1}&=a x_k+(ak+b)y_k,\\
 y_{k+1}&=c x_k+(ck+d)y_k.
 \end{aligned}
\tag{37}
\]

At the next step,

\[
 y_{k+2}=c x_{k+1}+(c(k+1)+d)y_{k+1}.
\tag{38}
\]

Use the first equation of (37) and
`c x_k=y_{k+1}-(ck+d)y_k`. The coefficient of `y_k` becomes

\[
 -ad+bc=-1,
\]

while the coefficient of `y_{k+1}` becomes `ck+a+c+d`. This proves (24).

If `c=0`, the matrix `C` preserves the line spanned by `e_1`, which is also
the image and kernel of `E_12`. Every step is upper triangular. Its diagonal
is a constant power, and its upper entry is a geometric-weighted affine sum;
standard doubling of a constant augmented state evaluates it with
`O(log m)` ring operations. This is the reducible constant-power/sum branch.

If `c!=0`, (24) has a genuinely varying affine coefficient. The proof has
only transformed the ordered product into an exact second-order recurrence.
It has not evaluated its remote term.

## 8. Holonomic does not mean fast-forwarded

Fix a row covector `ell`. For `0<=j<=d`, form

\[
 L_j(X)=\ell A(X+j-1)\cdots A(X),
 \qquad L_0(X)=\ell.
\tag{39}
\]

These are `d+1` vectors in the `d`-dimensional vector space `K(X)^d`.
They have a nontrivial dependence

\[
 \sum_{j=0}^{d}q_j(X)L_j(X)=0.
\tag{40}
\]

For any solution `v_{k+1}=A(k)v_k`, substitute `X=k` and multiply by
`v_k`. The scalar outputs `u_k=ell v_k` obey the corresponding rational-
coefficient recurrence. Clearing denominators gives a polynomial-
coefficient recurrence.

This derivation is algebraic only. Straight recurrence evaluation still
uses one update per index, and a generic balanced product tree has one leaf
per index. F276 makes no lower-bound claim against a special identity, but a
recurrence certificate alone supplies no numerical-quasipolynomial endpoint
algorithm.

