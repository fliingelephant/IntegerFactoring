# F153 V3 hostile audit — PASS

## Verdict

**PASS.** The four defects found by the V2 statement-only reconstruction are
repaired exactly. I also rechecked the inherited character, torus, Cayley,
quadratic-algebra, relative-norm, and group-order arguments. Under the stated
distinct-odd-semiprime and unit hypotheses, I found no remaining mathematical
or scope error.

This remains an operation-specific boundary. It is not a factoring algorithm,
a quasipolynomial source theorem, or a lower bound against all coordinate
algorithms.

## Frozen inputs

The requested SHA-256 hashes match:

- `V3_STATEMENT.md`:
  `91886c70c39496dc0519ab4928f7234a263539eb235a863c7ac8bbe21c50d8a0`;
- `V3_PROOF.md`:
  `f86807ae0bff8b4557f24da18c17b6729e4cb78895b22f6987f8a77efc17447d`.

I read the V2 blind reconstruction and both V3 frozen inputs in full. I did
not modify a frozen input or a durable ledger.

## 1. The four V2 defects are repaired

1. **Section quotient.** V3 uses

   \[
   k(v)=h_1(v)h_2(v)^{-1}.
   \]

   Both sections project to the same `v`, so this quotient lies in the
   root-of-one kernel. Since the extension is abelian and the sections are
   homomorphisms, `k` is a homomorphism. The raw product notation from V2 is
   gone.

2. **Split-side isomorphism.** V3 says only that the standard algebraic
   coordinate splitting of `A_D` uses a square root of `D`. It explicitly
   disclaims the stronger statement for an arbitrary abstract isomorphism of
   finite cyclic groups.

3. **Unspecified parameter map.** V3 no longer labels every map
   `t=f(alpha)` as non-homomorphic. It states the valid conclusion: without a
   separate homomorphism or order proof, ordinary large order gives no torus
   order theorem for that map.

4. **Biquadratic minimality.** V3 calls the full biquadratic algebra a natural
   universal algebra containing the two named quadratic coordinates. It
   expressly makes no unique or absolute-minimality claim.

These are wording and scope repairs. They do not alter the proved identities.

## 2. Discriminant character and section freedom

For a discriminant word `F=prod_i D_i^(e_i)`, multiplicativity of the
Legendre symbol gives

\[
\left(\frac Fp\right)=\eta,
\qquad
\left(\frac Fq\right)=(-1)^\delta\eta.
\]

Negative exponents are valid because every `D_i` is a unit. Equal local
square classes have equal character values. If `F` is a square modulo `N`,
then `eta=1` and `delta=0`.

V3 correctly stops at this base-character statement. It does not infer a
unique supplied root or decorated section. For a distinct odd semiprime, a
nonzero value of the section quotient in
`R_N/{+1,-1}` is represented by a nondiagonal square root of one, so its two
sign gcds factor `N`.

The `N=15`, `q_1=19` model checks exactly:

\[
2^2\equiv7^2\equiv19\pmod {15},
\qquad
2\cdot7\cdot19^{-1}\equiv11\pmod {15},
\]

and `gcd(11-1,15)=5`, `gcd(11+1,15)=3`.

## 3. Signed-gap exponent identities

The local torus orders are

\[
m_p=p-\epsilon,
\qquad
m_q=q+\epsilon,
\]

and direct expansion gives

\[
m_pm_q=N-1-\epsilon(q-p).
\]

The product and half-product are multiples of both local orders because
`m_p` and `m_q` are even. Thus, for every torus point,

\[
U^{N-1}=U^{\epsilon g},
\qquad
U^{(N-1)/2}=U^{\epsilon g/2}.
\]

No generator assumption is used. A second universal division by two through
the same proof would require `4` to divide `m_p`, `m_q`, and `g`. The first
two conditions imply `g=-2 epsilon modulo 4`, so the third fails. V3 limits
this obstruction to the direct universal exponent-division argument.

## 4. Cayley halving

On the stated unit branch, the Cayley law gives

\[
U_D(s)^2=U_D(t)
\iff
Dt s^2-2s+t=0.
\]

Its discriminant is `4(1-Dt^2)`. The substitutions

\[
r=1-Dts,
\qquad
s_\pm=\frac{1\pm r}{Dt}
\]

are correct. The two globally opposite roots select halves differing by the
global torus element `-1`. Two roots with a mixed CRT sign have a nondiagonal
root-of-one quotient and already expose a factor. The nonunit cases are left
to gcd screens, with no success claim.

## 5. Product discriminants and relative norms

For `F=DE`, both local characters equal
`eta=epsilon(D)epsilon(E)`. The local orders are `p-eta` and `q-eta`, and

\[
(p-\eta)(q-\eta)
=N-1-\eta(p+q-2\eta).
\]

Therefore every `W in T_F` obeys

\[
W^{N-1}=W^{\eta(p+q-2\eta)}.
\]

The two signs give the displayed exponents `p+q-2` and `-(p+q+2)`.

For a conjugation-preserving map `A_D -> A_E`, writing the image of `w_D`
as `a+bw_E` forces `a=0` and `b^2E=D`. Such a unit `b` exists modulo `N`
exactly when the two hidden orientations agree. This proves the stated
isomorphism criterion.

In the rank-four algebra, the three sign involutions have fixed rings
`A_D`, `A_E`, and `A_{DE}`. Applying them to `UV` gives exactly

\[
\operatorname{Nm}_{B/A_D}(UV)=U^2,
\quad
\operatorname{Nm}_{B/A_E}(UV)=V^2,
\quad
\operatorname{Nm}_{B/A_{DE}}(UV)=1.
\]

V3 correctly restricts this classification to these relative norms.

## 6. Ordinary high order

On a nonsplit local component, the source and target group orders are
`r-1` and `r+1`. The image of any homomorphism has order dividing both, and
therefore at most two. This proves the stated homomorphic-transfer boundary.
It does not cover an independently justified non-homomorphic coordinate map
or a torus-native high-order construction.

The Kummer calculation is also correct under the named nondegeneracy
conditions:

\[
x^2-1=\left(\frac{\alpha-\alpha^{-1}}2\right)^2,
\qquad
y^2=D^{-1}(x^2-1).
\]

The missing `y` exists only on the split local side, while the retained
Chebyshev relations in `x` do not contain `D`.

## Final scope

The exact negative result is narrow: the displayed word, exponent-halving,
Cayley-halving, isomorphism, relative-norm, Kummer, and homomorphic-transfer
operations do not force two incompatible decorated lifts. The result does
not exclude another full-coordinate invariant, a lift modulo `N^2`, a
resultant, determinant, derivative, metric rule, or another torus-native
source. A fresh statement-only reconstruction is appropriate.
