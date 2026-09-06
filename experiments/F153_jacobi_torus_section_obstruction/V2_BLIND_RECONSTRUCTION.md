# F153 V2 blind reconstruction

## Protocol and verdict

The SHA-256 digest of `V2_STATEMENT.md` is

```text
6bba6be5b6f8dd9f2a4810f7182fbc400029cc5026b55224809835a186123b3a
```

This reconstruction uses only that statement. It does not use another F153
file or an external proof, audit, manifest, or ledger.

The local-order arguments and all scalar and torus identities are correct.
Formula (3a) has a quotient-notation defect described below. The
operation-specific negative conclusion is also correct: none of the listed
operations forces a second, incompatible decorated lift. The text needs
four small repairs to be literally exact:

1. The quotient of two sections in (3a) must be written with an inverse, or
   the text must first define a normalization in which the product denotes
   that quotient.
2. The split-side sentence in Theorem 5 is exact for an algebraic coordinate
   splitting, but not for an arbitrary abstract isomorphism of finite cyclic
   point groups. It must state which kind of isomorphism it means.
3. The last paragraph of Theorem 5 cannot classify an unspecified function
   of an ordinary element as non-homomorphic. It can only say that no
   homomorphism, and hence no order transfer, follows without an additional
   proof.
4. The full biquadratic algebra is a natural universal algebra for the two
   named quadratic coordinates. The preceding results do not prove that it
   is the unique or absolutely smallest live algebra.

The historical attributions to P55, P57, F151, and F152 are not mathematical
consequences of the supplied statement and are not certified by this blind
reconstruction.

## 1. Local structure

For an odd prime `r` not dividing `D`, let

\[
\chi_r(D)=\left(\frac D r\right).
\]

If `chi_r(D)=1`, choose `d^2=D` in `F_r`. Evaluation at `w=d` and
`w=-d` identifies

\[
\mathbf F_r[w]/(w^2-D)\simeq \mathbf F_r\times\mathbf F_r,
\]

with conjugation exchanging the factors. Its norm-one group is therefore
isomorphic to `F_r^times` and has order `r-1`.

If `chi_r(D)=-1`, the quadratic algebra is `F_{r^2}`. The involution
`w mapsto -w` is the Frobenius involution, and the kernel of the norm to
`F_r` has order `r+1`. Consequently, in both cases,

\[
|T_D(\mathbf F_r)|=r-\chi_r(D).                                      \tag{L1}
\]

These groups are cyclic. In particular, their cardinalities are also their
exponents.

The CRT gives

\[
T_D(\mathbf Z/N\mathbf Z)
 \simeq T_D(\mathbf F_p)\times T_D(\mathbf F_q).                      \tag{L2}
\]

It also gives

\[
R_N=\{a\in R^\times:a^2=1\}
 \simeq \{\pm1\}\times\{\pm1\}.                                   \tag{L3}
\]

The diagonal pair is a global sign. Either nondiagonal pair is a non-global
root of one. If `a` is nondiagonal, one of `gcd(a-1,N)` and `gcd(a+1,N)` is
`p`, and the other is `q`.

## 2. Discriminant words and section freedom

For every `i`, quadratic-character multiplicativity gives

\[
\left(\frac{D_i^{e_i}}p\right)=\epsilon(D_i)^{e_i},
\qquad
\left(\frac{D_i^{e_i}}q\right)=(-\epsilon(D_i))^{e_i}.
\]

Multiplying over `i` proves

\[
\left(\frac Fp\right)=\eta,
\qquad
\left(\frac Fq\right)=(-1)^\delta\eta.                              \tag{2.1}
\]

Negative exponents cause no issue because every `D_i` is a unit and a
quadratic character takes values in `{+1,-1}`.

The three stated consequences follow immediately.

- Equal local square classes have equal quadratic characters, hence equal
  `eta`.
- If `F` is a square modulo `N`, both characters in (2.1) are `1`. Thus
  `eta=1` and `(-1)^delta=1`, so `delta=0`.
- A quadratic character is constant on each local square class. It cannot
  distinguish two representatives or two chosen roots inside that class.

This proves only a statement about base square classes. It says nothing
about which one of the four CRT roots a coordinate mechanism selects.

The section statement is the standard kernel lemma, but its exact formula
needs the quotient notation. Let

\[
1\longrightarrow K\longrightarrow G\mathop{\longrightarrow}^{\pi}W
\longrightarrow1
\]

be the relevant abelian lift extension, with
`K isomorphic to R_N/{+1,-1}`. If `h_1,h_2:W to G` are homomorphic sections
of the same `pi`, define

\[
k(x)=h_1(x)h_2(x)^{-1}.                                               \tag{2.2}
\]

Then `pi(k(x))=1`, so `k(x)` lies in `K`, and commutativity shows that `k`
is a homomorphism. A nonzero value in `R_N/{+1,-1}` is represented by a
nondiagonal root and factors `N` by (L3). Thus common orientation does not
imply equal sections.

If the notation `h_1h_2` in (3a) was intended after identifying every
kernel element with its inverse, this convention must be stated. For raw
square-root lifts, the inverse is essential. Indeed, for roots `a^2=b^2=q`,

\[
ab^{-1}=abq^{-1},                                                      \tag{2.3}
\]

which is exactly the normalization used in (3b).

For the example, modulo `15`,

\[
2^2\equiv7^2\equiv19\equiv4,
\qquad
2\cdot7\cdot19^{-1}\equiv11.
\]

Also `11^2=121=1 mod 15`, while

\[
\gcd(11-1,15)=5,
\qquad
\gcd(11+1,15)=3.
\]

The example therefore proves the claimed abstract non-uniqueness. It does
not construct a source, as the statement correctly notes.

## 3. The direct exponent identities and the unique universal division by two

For the Jacobi-minus-one discriminant `D`, its local characters are
`epsilon` at `p` and `-epsilon` at `q`. By (L1), the local torus orders are

\[
m_p=p-\epsilon,
\qquad
m_q=q+\epsilon.
\]

Direct multiplication gives

\[
m_pm_q=(p-\epsilon)(q+\epsilon)
=N-1-\epsilon(q-p)=N-1-\epsilon g.                                   \tag{3.1}
\]

For `U=(U_p,U_q)`, the exponent `m_pm_q` is a multiple of each local group
order. Hence `U^(m_pm_q)=1`. Rearranging (3.1) proves

\[
U^{N-1}=U^{\epsilon g}.                                                \tag{3.2}
\]

Both `m_p` and `m_q` are even. Thus `m_pm_q/2` remains a multiple of both:

\[
\frac{m_pm_q}{2}=m_p\frac{m_q}{2}=m_q\frac{m_p}{2}.
\]

Since `g` is even, division of (3.1) by two gives integral exponents and
proves, for every `U`,

\[
U^{(N-1)/2}=U^{\epsilon g/2}.                                         \tag{3.3}
\]

This uses the full local group orders, so it needs no generator hypothesis.
The left side is a deterministic global exponentiation. Its square is
`U^(N-1)`, but the computation supplies no independently chosen local sign.

For the same direct proof after division by `2^k`, universal validity for
all local points would require

\[
m_p\mid\frac{m_pm_q}{2^k},
\qquad
m_q\mid\frac{m_pm_q}{2^k}.
\]

Because the local groups are cyclic, these conditions are necessary as well
as sufficient. They imply

\[
2^k\mid m_p,
\qquad
2^k\mid m_q.                                                          \tag{3.4}
\]

For every `k>=2`, (3.4) implies modulo four

\[
p\equiv\epsilon,
\qquad
q\equiv-\epsilon,
\qquad
g=q-p\equiv-2\epsilon\not\equiv0\pmod4.                              \tag{3.5}
\]

Thus `g/2^k` is not integral. The direct exponent-division proof has exactly
one universal factor of two. This conclusion is deliberately limited to
that proof; it is not a theorem against all possible halving operations.

## 4. Cayley halving

Whenever all displayed inverses exist, direct multiplication gives the
Cayley law

\[
U_D(a)U_D(b)=U_D\!\left(\frac{a+b}{1+Dab}\right).                     \tag{4.1}
\]

Therefore

\[
U_D(s)^2=U_D(t)
\quad\Longleftrightarrow\quad
t=\frac{2s}{1+Ds^2}
\quad\Longleftrightarrow\quad
Dt s^2-2s+t=0.                                                        \tag{4.2}
\]

The quadratic discriminant is

\[
(-2)^2-4(Dt)t=4(1-Dt^2)=4z_D(t).                                     \tag{4.3}
\]

If `s` satisfies (4.2), then

\[
\begin{aligned}
(1-Dts)^2-(1-Dt^2)
 &=Dt\bigl(Dts^2-2s+t\bigr)\\
 &=0.
\end{aligned}
\]

Thus `r=1-Dts` is a root of `z_D(t)`. Conversely, the quadratic formula,
using that `Dt` is a unit, gives

\[
s_\pm=\frac{1\pm r}{Dt}.                                              \tag{4.4}
\]

The association reverses the displayed sign because
`1-Dt s_+=-r` and `1-Dt s_-=r`; the unordered pair is exactly as stated.

The two roots of (4.2) satisfy `s_+s_-=1/D`. A direct Cayley calculation
then gives

\[
U_D(s_-)=-U_D(s_+).                                                    \tag{4.5}
\]

Hence replacing `r` by the globally opposite root `-r` changes the chosen
half by the scalar torus point `-1` in both CRT components. This is a global
sign, not a factor.

On the clean branch, `z_D(t)` is a unit because it is the norm of
`1-tw_D`. If two roots `r,r'` of `z_D(t)` have opposite signs at exactly one
hidden prime, then

\[
a=r'r^{-1}\in R_N
\]

is nondiagonal. Equation (L3) factors `N` before a comparison of the torus
halves can add information. This proves the claimed synchronized-versus-
mixed dichotomy.

For `t=0`, `U_D(t)=1`. If `t` or a required norm denominator is a nonunit,
a gcd with `N` is the correct boundary screen. That gcd can also be `N`, so
the statement correctly makes no success-probability claim.

## 5. Product discriminants, algebra isomorphisms, and relative norms

Let `F=DE` and `eta=epsilon(D)epsilon(E)`. At `p`,

\[
\chi_p(F)=\chi_p(D)\chi_p(E)=\eta,
\]

while at `q`,

\[
\chi_q(F)=(-\epsilon(D))(-\epsilon(E))=\eta.
\]

Thus the two local orders of `T_F` are

\[
n_p=p-\eta,
\qquad
n_q=q-\eta.
\]

For every `W in T_F`, `W^(n_pn_q)=1`, and

\[
\begin{aligned}
n_pn_q
 &=(p-\eta)(q-\eta)\\
 &=N-\eta(p+q)+1\\
 &=(N-1)-\eta(p+q-2\eta).
\end{aligned}                                                         \tag{5.1}
\]

Therefore

\[
W^{N-1}=W^{\eta(p+q-2\eta)}.                                         \tag{5.2}
\]

The two sign cases are exactly

\[
\eta=1:\quad W^{N-1}=W^{p+q-2},
\]

and

\[
\eta=-1:\quad W^{N-1}=W^{-(p+q+2)}.
\]

Negative exponents are valid because `W` is a unit. Equivalently, the
differences of the two exponents are `(p-1)(q-1)` in the first case and
`(p+1)(q+1)` in the second. This proves the requested `F=DE` exponent
identity, including both signs.

Now let `Phi:A_D to A_E` be an `R`-algebra map commuting with conjugation.
Write

\[
\Phi(w_D)=a+bw_E.
\]

Commutation with conjugation gives
`a-bw_E=-a-bw_E`, hence `2a=0`. Since `N` is odd, `a=0`. Preservation of
the defining relation then gives

\[
D=\Phi(w_D)^2=b^2E.                                                    \tag{5.3}
\]

Because `D` and `E` are units, `b` is a unit. Conversely, a unit satisfying
`b^2=DE^(-1)` defines the stated isomorphism, with inverse
`w_E mapsto b^(-1)w_D`. This proves (15).

The ratio `DE^(-1)` has character `eta` at both hidden primes. A unit modulo
`N` is a square exactly when it is a square at both CRT primes. Hence the
required `b` exists exactly when `eta=1`, equivalently when
`epsilon(D)=epsilon(E)`. Replacing `b` by `-b` composes the isomorphism with
global conjugation. Comparing any two roots whose quotient is nondiagonal
factors `N`; merely naming one root as “mixed” without a comparison is not
an additional operation.

Embed `A_F` into `B` by `w_F=w_Dw_E`. The involutions fixing `A_D`, `A_E`,
and `A_F` respectively are

\[
(w_D,w_E)\mapsto(w_D,-w_E),
\quad
(w_D,w_E)\mapsto(-w_D,w_E),
\quad
(w_D,w_E)\mapsto(-w_D,-w_E).
\]

Since `bar U=U^(-1)` and `bar V=V^(-1)`, multiplication by each relative
conjugate gives

\[
\begin{aligned}
\operatorname{Nm}_{B/A_D}(UV)
  &=(UV)(U\bar V)=U^2,\\
\operatorname{Nm}_{B/A_E}(UV)
  &=(UV)(\bar U V)=V^2,\\
\operatorname{Nm}_{B/A_F}(UV)
  &=(UV)(\bar U\bar V)=1.
\end{aligned}                                                         \tag{5.4}
\]

Thus these three relative norms return only an old point squared or the
identity. This calculation says nothing about a non-norm function of the
four coordinates, nor about higher lifts, derivatives, traces, or
resultants.

## 6. Homomorphic transfer of ordinary order

If `D` is nonsquare over `F_r`, (L1) gives

\[
|\mathbf F_r^\times|=r-1,
\qquad
|T_D(\mathbf F_r)|=r+1.
\]

For a group homomorphism
`phi:F_r^times to T_D(F_r)`, the image is both a quotient of the source and
a subgroup of the target. Lagrange's theorem therefore gives

\[
|\operatorname{im}\phi|\mid(r-1),
\qquad
|\operatorname{im}\phi|\mid(r+1),
\]

and hence

\[
|\operatorname{im}\phi|\mid\gcd(r-1,r+1)=2.                          \tag{6.1}
\]

No element of order greater than two can survive in the nonsplit local
component under a homomorphism. This is the exact theorem. It does not, by
itself, prohibit a global CRT map from retaining order in the split
component while collapsing the nonsplit component; such a map would need
additional data and would not solve the orientation problem.

On a split component, choosing `d` with `d^2=D` gives the algebraic
coordinate isomorphism

\[
\lambda_d(\alpha)
=\frac{\alpha+\alpha^{-1}}2
 +\frac{\alpha-\alpha^{-1}}{2d}w_D.                                  \tag{6.2}
\]

Thus a standard algebraic splitting depends on a choice of square root of
`D`. The unqualified claim that every abstract isomorphism of the two finite
cyclic point groups “needs” that root is stronger than (6.1) and should not
be asserted.

Writing

\[
x=\frac{\alpha+\alpha^{-1}}2
\]

gives

\[
x^2-1=\left(\frac{\alpha-\alpha^{-1}}2\right)^2.                       \tag{6.3}
\]

A torus coordinate `x+yw_D` must satisfy `x^2-Dy^2=1`, so recovering `y`
from this ordinary `x` requires division by a square root of `D` on a split
component. On a nonsplit component, no such `y` exists unless
`alpha=+1` or `alpha=-1`. Moreover,

\[
\frac{\alpha^n+\alpha^{-n}}2=T_n(x),
\]

and the Chebyshev recurrence for `T_n` contains no `D`. The public Kummer
coordinate therefore loses the discriminant orientation exactly as
claimed.

The sentence “choosing `t` as a function of `alpha` is another
non-homomorphic map” is not literally valid without specifying that
function. For example, on the split chart `alpha != -1`,

\[
t(\alpha)=\frac{\alpha-1}{d(\alpha+1)}                                \tag{6.4}
\]

makes `U_D(t(alpha))=lambda_d(alpha)` and extends projectively to a
homomorphism. The valid order statement is instead:

> Choosing `t=f(alpha)` does not by itself prove that the resulting map is a
> homomorphism. Without a separate homomorphism or order argument, an
> ordinary order certificate implies no torus-order theorem.

Together with (6.1), this preserves the intended obstruction without the
categorical overstatement.

## 7. Exact scope

The proved result is operation-specific.

- Discriminant multiplication exposes only the single local quadratic
  character and word parity.
- Direct division of the exponent identity works universally once, and not
  twice.
- Opposite global Cayley roots give halves differing by global `-1`; a
  relative mixed choice is already factor-bearing.
- A conjugation-preserving cross-discriminant isomorphism requires the two
  orientations to agree, and relative mixed roots are already
  factor-bearing.
- The three direct relative norms discard the cross-coordinate data.
- A homomorphism into a nonsplit local torus has image of order at most two.

None of these facts makes a decorated section unique. They only show that
the operations just listed do not force a second section. The quotient
lemma in (2.2) leaves exactly the advertised possibility: a new coordinate
mechanism can preserve the orientation character and still differ by a
nonzero element of `R_N/{+1,-1}`.

The calculations do not establish a lower bound for all coordinate
algorithms. They do not cover a non-norm biquadratic invariant, a
resultant, determinant, derivative, trace construction, lift modulo `N^2`,
metric selection rule, or another coordinate operation. They also use the
CRT decomposition for two distinct odd primes throughout and therefore do
not extend the result to arbitrary composite inputs.

Finally,

\[
B=A_D\otimes_R A_E
\]

is the universal `R`-algebra containing both named quadratic generators,
so it is a natural next place to inspect simultaneous coordinates before
relative norm. Equations (5.2)--(5.4) do not prove an absolute minimality
claim. The exact minimal wording repair is:

> Theorem 4 identifies a natural universal algebra for that test: the full
> biquadratic coordinates before relative norm.

With the repairs in Sections 2, 6, and 7, the statement's core conclusion
is proved. No repair to the Jacobi formulas, either exponent identity, the
Cayley equations, the cross-discriminant criterion, the norm identities, or
the nonsplit image bound is needed.
