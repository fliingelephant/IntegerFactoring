# F153 V3 blind reconstruction

## Source boundary and verdict

I used only `V3_STATEMENT.md` among the F153 artifacts. Its SHA-256 is

```text
91886c70c39496dc0519ab4928f7234a263539eb235a863c7ac8bbe21c50d8a0
```

The algebraic claims in Theorems 1--5 are correct for distinct odd primes
`p<q`. In particular, the product-discriminant identity

\[
W^{N-1}=W^{\eta(p+q-2\eta)}
\]

is exact in both the all-split and all-nonsplit cases. The conclusions are
operation-specific. They do not prove that an orientation character uniquely
determines a decorated section, and they do not give a lower bound against
other coordinate algorithms.

Two semantic qualifications are useful:

1. Equation (3a) implicitly needs a common **abelian** extension whose kernel
   is `R_N/{\pm1}`. Under that intended setup, the equation is correct. A
   nonzero value is literally a nonzero coset; either representative is a
   non-global root of one and factors `N`.
2. A lone square root of a public value does not generally factor `N`. The
   Cayley and cross-discriminant arguments become factor-bearing when two
   available choices differ in exactly one CRT component. This is the
   comparison used in the statement.

Claims about what P55, P57, F151, or F152 previously proved, and the historical
claim that a formula was not previously recorded, cannot be authenticated in a
statement-only reconstruction. The formulas attributed to those results are
proved independently below.

## 1. CRT and the local torus order

For a unit `X` and an odd prime `r`, let

\[
\chi_r(X)=\left(\frac Xr\right).
\]

The local algebra is

\[
A_{X,r}=\mathbf F_r[w]/(w^2-X).
\]

If `\chi_r(X)=1`, choose `a^2=X`. The map

\[
x+yw\longmapsto (x+ay,x-ay)
\]

identifies `A_{X,r}` with `\mathbf F_r\times\mathbf F_r`; conjugation swaps
the two factors. Its norm-one group is `{(u,u^{-1})}`, so it is cyclic of
order `r-1`.

If `\chi_r(X)=-1`, the algebra is `\mathbf F_{r^2}`. Conjugation is the
Frobenius automorphism, and its norm-one kernel has order

\[
\frac{r^2-1}{r-1}=r+1.
\]

Thus, uniformly,

\[
|T_X(\mathbf F_r)|=r-\chi_r(X). \tag{A}
\]

CRT gives

\[
A_X\simeq A_{X,p}\times A_{X,q},\qquad
T_X\simeq T_X(\mathbf F_p)\times T_X(\mathbf F_q). \tag{B}
\]

It also gives

\[
R_N:=\{u\in R^\times:u^2=1\}
 \simeq \{\pm1\}\times\{\pm1\}. \tag{C}
\]

The diagonal pair `(1,1)` and `(-1,-1)` are the global signs. Either other
pair is a mixed root. If, for example, `u=(1,-1)`, then

\[
\gcd(u-1,N)=p,\qquad \gcd(u+1,N)=q, \tag{D}
\]

with the two factors interchanged for `u=(-1,1)`.

## 2. Discriminant words give one character

For every `D_i` of Jacobi symbol `-1`,

\[
\chi_p(D_i)=\epsilon(D_i),\qquad
\chi_q(D_i)=-\epsilon(D_i).
\]

Legendre symbols are multiplicative, including on negative powers of units.
Therefore, for `F=\prod_iD_i^{e_i}`,

\[
\chi_p(F)
=\prod_i\epsilon(D_i)^{e_i}
=\eta,
\]

and

\[
\chi_q(F)
=\prod_i(-\epsilon(D_i))^{e_i}
=(-1)^{\sum_i e_i}\eta
=(-1)^\delta\eta.
\]

This proves (3).

If two words represent the same square class at `p`, their `p`-Legendre
symbols, hence their `\eta` values, agree. The same conclusion follows from
equality of the full pair of local square classes. Equality only at `q` would
not determine `\eta` unless the parities `\delta` also agree. If a word is a
unit square modulo `N`, both local characters are `1`. Equation (3) then gives
`\eta=1` and `(-1)^\delta=1`, so `\delta=0`.

"One character" means that every word orientation is an evaluation of the
same homomorphism from local square classes to `{\pm1}`. It does not mean that
the values on different discriminants are all equal. More importantly, a
character value identifies a square class, not a chosen square root or a
chosen coordinate lift.

## 3. Why the decorated section is not unique

The section statement can be reconstructed abstractly. Let

\[
1\longrightarrow K\longrightarrow G\overset{\pi}{\longrightarrow}W
\longrightarrow1,
\qquad K=R_N/\{\pm1\}, \tag{E}
\]

be the common abelian extension in which the coordinate lifts live. If
`h_1,h_2:W\to G` are homomorphic sections of `\pi`, then

\[
d(w)=h_1(w)h_2(w)^{-1}
\]

lies in `K`, because `\pi(d(w))=w w^{-1}=1`. Since `G` is abelian,

\[
d(w_1w_2)=d(w_1)d(w_2),
\]

so `d:W\to R_N/{\pm1}` is a homomorphism. This proves the intended content of
(3a).

For `N=pq`, (C) shows that this quotient has two elements. Its nonidentity
element is the class of the two mixed roots. Thus a nonzero section quotient
does not merely witness distinct sections: a representative and (D) recover
the two factors.

The `N=15` example is exact. Since `19\equiv4\pmod {15}`,

\[
2^2\equiv7^2\equiv19\pmod {15}.
\]

Also `19^{-1}\equiv4\pmod {15}`, and hence

\[
2\cdot7\cdot19^{-1}\equiv2\cdot7\cdot4\equiv11\pmod {15}.
\]

Then `11^2\equiv1\pmod {15}`, while

\[
\gcd(11-1,15)=5,
\qquad
\gcd(11+1,15)=3.
\]

The example proves nonuniqueness of the possible section over a fixed square
class. It does not construct two sections from an allowed public source.

## 4. The one universal direct exponent halving

Fix a Jacobi-minus-one `D` and put `\epsilon=\chi_p(D)`. Its local characters
are `\epsilon` at `p` and `-\epsilon` at `q`. By (A), the local torus orders
are

\[
m_p=p-\epsilon,
\qquad
m_q=q+\epsilon.
\]

With `g=q-p`, direct expansion gives

\[
m_pm_q
=(p-\epsilon)(q+\epsilon)
=N-1-\epsilon g. \tag{F}
\]

For `U=(U_p,U_q)\in T_D`, the exponent `m_pm_q` kills both components.
Consequently

\[
U^{N-1-\epsilon g}=1,
\]

which is equivalent to (6).

Both `m_p` and `m_q` are even. Therefore `m_pm_q/2` is still divisible by
each local order, and it also kills every `U`. Dividing (F) by two gives

\[
U^{(N-1)/2}=U^{\epsilon g/2},
\]

which proves (7) without assuming that `U` is a generator. Its left side is
a globally computed square root of `U^{N-1}`. No second square root is
produced.

The limitation on repeated direct division is also exact. For
`m_pm_q/2^k` to kill **every** local torus element, cyclicity and (A) require

\[
m_p\mid \frac{m_pm_q}{2^k}
\quad\hbox{and}\quad
m_q\mid \frac{m_pm_q}{2^k}.
\]

These conditions are equivalent to

\[
2^k\mid m_q
\quad\hbox{and}\quad
2^k\mid m_p. \tag{G}
\]

The displayed right-hand exponent would additionally require `2^k\mid g`.
For `k\ge2`, (G) implies

\[
p\equiv\epsilon\pmod4,
\qquad
q\equiv-\epsilon\pmod4,
\]

and hence

\[
g=q-p\equiv-2\epsilon\not\equiv0\pmod4.
\]

Thus the three requirements cannot hold. The statement correctly rules out a
universal **iteration of this exponent-division proof**. It does not rule out
an input-specific identity or a different halving mechanism.

## 5. Cayley halving

For clean parameters, multiplication of Cayley points gives

\[
U_D(a)U_D(b)
=U_D\!\left(\frac{a+b}{1+Dab}\right).
\]

The Cayley chart is injective wherever its denominators are units. Setting
`a=b=s` therefore yields

\[
U_D(s)^2=U_D(t)
\iff
t=\frac{2s}{1+Ds^2}
\iff
Dt s^2-2s+t=0.
\]

The quadratic discriminant is `4(1-Dt^2)=4z_D(t)`, proving (9)--(10).

If `s` solves the quadratic and `r=1-Dts`, then

\[
\begin{aligned}
r^2
&=1-2Dts+D^2t^2s^2\\
&=1-2Dts+Dt(2s-t)\\
&=1-Dt^2
=z_D(t).
\end{aligned}
\]

Conversely, if `r^2=z_D(t)` and `Dt` is a unit, the two roots of the
quadratic are

\[
s_\pm=\frac{1\pm r}{Dt}.
\]

Their product is `s_+s_-=1/D`. For every clean nonzero `s`, direct
simplification gives

\[
U_D\!\left(\frac1{Ds}\right)=-U_D(s).
\]

It follows that

\[
U_D(s_-)=-U_D(s_+). \tag{H}
\]

Thus the globally opposite roots `r` and `-r` give the same half modulo the
global torus sign. They cannot create a section disagreement.

If two available roots `r,r'` differ in exactly one CRT component, then
`u=r'r^{-1}` is a mixed root of one. Equation (D) factors `N` immediately.
Hence a **second**, mixed branch is already factor-bearing relative to the
first branch. This comparison qualification is essential; one isolated root
of `z_D(t)` need not factor `N`.

The excluded cases do not support a probability claim. A nonunit scalar or
norm can be passed to `gcd(\cdot,N)`; this may give a factor, a trivial gcd, or
show that the displayed Cayley point is outside the chart. The case `t=0`
gives the identity and is degenerate.

## 6. The product-discriminant identity

Let `F=DE` and `\eta=\epsilon(D)\epsilon(E)`. At `p`,

\[
\chi_p(F)=\epsilon(D)\epsilon(E)=\eta.
\]

At `q`, both signs reverse, so

\[
\chi_q(F)=(-\epsilon(D))(-\epsilon(E))=\eta.
\]

Thus the two local torus orders for `T_F` are

\[
p-\eta,
\qquad
q-\eta.
\]

Their product

\[
K=(p-\eta)(q-\eta)
=N+1-\eta(p+q) \tag{I}
\]

kills every `W\in T_F`. On the other hand,

\[
(N-1)-\eta(p+q-2\eta)
=N+1-\eta(p+q)
=K,
\]

because `\eta^2=1`. Therefore

\[
\boxed{W^{N-1}=W^{\eta(p+q-2\eta)}}.
\]

For `\eta=1`, the right exponent is `p+q-2`. For `\eta=-1`, it is
`-(p+q+2)`. Negative powers are valid because `W` is a unit. This independently
verifies the claimed `F=DE` specialization, including the sign in the
all-nonsplit branch.

The identity is tautological in the same precise sense as (6): its exponent
difference is a public-unknown product of the two local group orders. It does
not reveal `\eta` or `p+q`, and knowing `p+q` would already factor `N` through
the roots of `X^2-(p+q)X+N`.

## 7. Conjugation-preserving cross-discriminant maps

Let `\varphi:A_D\to A_E` be an `R`-algebra map that commutes with conjugation.
Write

\[
\varphi(w_D)=a+bw_E.
\]

Since `\varphi(-w_D)=\overline{\varphi(w_D)}`, one has

\[
-a-bw_E=a-bw_E.
\]

As `2` is a unit in `R`, this forces `a=0`. The defining relation then gives

\[
D=\varphi(w_D)^2=b^2E,
\]

or `b^2=DE^{-1}`. Such a map is an isomorphism exactly when `b` is a unit;
the displayed equation already makes it a unit. Conversely, any such `b`
defines the claimed isomorphism. This proves (15) and the asserted form of
the map.

The local character of `DE^{-1}` at both primes is
`\epsilon(D)\epsilon(E)`. Hence it has a square root modulo `N` exactly when
`\epsilon(D)=\epsilon(E)`. The maps defined by `b` and `-b` differ by global
conjugation. If `b'` is another root not equal to `\pm b`, then `b'b^{-1}` is
a mixed root of one and factors `N` by (D). Again, it is the comparison of two
non-globally-equivalent choices that carries the factor.

## 8. The three relative norms

In

\[
B=R[w_D,w_E]/(w_D^2-D,w_E^2-E),
\]

let `\sigma_D` flip `w_D` and fix `w_E`, and let `\sigma_E` flip `w_E` and
fix `w_D`. The nontrivial automorphism of `B/A_D` is `\sigma_E`; that of
`B/A_E` is `\sigma_D`. The product `w_Dw_E` squares to `F=DE`, and the
subalgebra `A_F=R[w_Dw_E]` is fixed by `\sigma_D\sigma_E`.

For `U\in T_D` and `V\in T_E`, commutativity and the norm-one equations give

\[
\begin{aligned}
\operatorname{Nm}_{B/A_D}(UV)
  &=(UV)(U\overline V)=U^2,\\
\operatorname{Nm}_{B/A_E}(UV)
  &=(UV)(\overline U V)=V^2,\\
\operatorname{Nm}_{B/A_F}(UV)
  &=(UV)(\overline U\,\overline V)=1.
\end{aligned}
\]

This proves (17), including over the composite base ring: the algebras are
finite free and the displayed involutions are the relevant quadratic norm
involutions. These three particular projections return only an old point
squared or the identity. Nothing in the calculation classifies other
functions of the four biquadratic coordinates.

## 9. Homomorphic transfer and the Kummer boundary

If `D` is nonsquare modulo an odd prime `r`, (A) gives

\[
|\mathbf F_r^\times|=r-1,
\qquad
|T_D(\mathbf F_r)|=r+1.
\]

For a group homomorphism

\[
\phi:\mathbf F_r^\times\to T_D(\mathbf F_r),
\]

the image order divides both group orders. Therefore it divides

\[
\gcd(r-1,r+1)=2.
\]

No element can retain large ordinary multiplicative order on the nonsplit
side through such a homomorphism. On the split side, the explicit coordinate
decomposition in Section 1 uses a choice `a^2=D`. This is a statement about
that algebraic coordinate splitting, not about the abstract existence of an
isomorphism between two cyclic groups of order `r-1`.

For the Kummer coordinate

\[
x=\frac{\alpha+\alpha^{-1}}2,
\]

put `c=(\alpha-\alpha^{-1})/2`. Then

\[
x^2-1=c^2.
\]

A torus lift `x+yw_D` of norm one would need

\[
y^2=\frac{x^2-1}{D}=\frac{c^2}{D}. \tag{J}
\]

When `D` is a square, a lift is obtained using a choice of `\sqrt D`. When
`D` is nonsquare and `c\ne0`, (J) has no solution in `\mathbf F_r`. The
degenerate cases `\alpha=\pm1` give `c=0`. Meanwhile

\[
\frac{\alpha^n+\alpha^{-n}}2=T_n(x)
\]

depends only on the Chebyshev recurrence and contains no `D`. This proves the
claimed loss of discriminant orientation at the Kummer coordinate level.

For an unrelated prescription `t=f(\alpha)`, homomorphicity would require a
separate identity such as

\[
f(\alpha\beta)
=\frac{f(\alpha)+f(\beta)}{1+D f(\alpha)f(\beta)}
\]

on the clean Cayley chart. Merely writing down `f` proves neither that identity
nor its negation. Without a homomorphism or an independent order analysis, the
order of `\alpha` supplies no order result for `U_D(f(\alpha))`.

## 10. Audit of the operation-specific conclusion

The proved boundary is the following.

| Direct operation | Exact output or obstruction | What remains open |
|---|---|---|
| Multiplicative discriminant words | One quadratic character on square classes | Extra coordinate or lift data |
| Divide the local-order product exponent | One universal division by `2` | Other or input-specific halving rules |
| Cayley doubling inversion | The global `\pm r` pair gives halves differing by global `-1` | A second root class, which factors when compared |
| Conjugation-preserving `A_D\simeq A_E` | Exists only for equal orientations; global `\pm b` is conjugation | A second root class, which factors when compared |
| Product followed by a quadratic relative norm | `U^2`, `V^2`, or `1` | Any non-norm function of full biquadratic coordinates |
| Homomorphic ordinary-to-nonsplit transfer | Image order at most `2` | Nonhomomorphic maps with a separate order theorem, or torus-native constructions |

This table is a classification of the listed operations, not of all
coordinate algorithms. In particular, traces, resultants, derivatives,
determinants, lifts modulo `N^2`, metric rules, and other non-norm invariants
are untouched. The proof uses the two-prime CRT and the exact local field
orders, so it does not establish the same statement for arbitrary composite
inputs.

## 11. The four conspicuous V3 quotient/scope wordings

Because prior versions were outside the permitted source boundary, revision
history cannot identify which four sentences were edited. The four
conspicuous quotient/scope repairs in the supplied statement are all sound:

1. **Section quotient.** The correct kernel after forgetting global sign is
   `R_N/{\pm1}`, not `R_N`. With the implicit common abelian extension made
   explicit, (3a) is valid. A nonzero quotient class has mixed-root
   representatives.
2. **One direct halving only.** The modulo-four contradiction rules out an
   iterated universal *direct exponent division*. It does not rule out every
   conceivable halving algorithm.
3. **No conclusion from `t=f(\alpha)` alone.** An arbitrary coordinate
   prescription is not proved homomorphic or nonhomomorphic merely by being
   written in terms of a high-order ordinary element. Its law and its image
   order require separate proofs.
4. **Biquadratic algebra is a gate, not a minimality theorem.** `B` is the
   natural tensor-product algebra containing both quadratic coordinates, so
   it is a valid universal place to test cross-coordinate invariants. The norm
   calculation does not prove that `B` is the unique or smallest possible
   live algebra.

The nearby qualifier about split-side coordinate roots is also correct: the
standard explicit splitting uses `\sqrt D`, while this says nothing about
what data an abstract cyclic-group isomorphism must use.

## Final determination

The candidate survives blind mathematical reconstruction. Its positive
content is a set of exact identities and exact failures for six named direct
operations. Its negative content is deliberately narrow. The `N=15` example
shows that equal orientation does not force equal decorated sections, while
the quotient calculation shows why two actually supplied incompatible
sections would factor `N`.

The remaining gate is therefore logically consistent: one must construct a
second coordinate lift not fixed by the character, or extract factor-correlated
information from a non-norm invariant. No theorem in the statement proves
that such a construction exists, that the biquadratic algebra is minimal, or
that all coordinate algorithms face the listed obstructions.

The phrases that a torus-native procedure "would be new" and that large order
would "remove collisions" are not self-contained theorem claims. Novelty needs
comparison with external work, and collision removal needs a specified map and
exponent range. Neither phrase is needed for any proved obstruction above.
