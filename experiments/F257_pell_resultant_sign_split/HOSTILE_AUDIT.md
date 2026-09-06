# F257 hostile audit

## Verdict

**PASS, with one harmless runtime-wording qualification.** All four supplied
SHA-256 digests match. The odd-prime-power sign split, exact two-adic
correction, signed resultant divisibilities, orbit formulas, one-sided
Jacobi-minus-one gcd ticket, factor-free refinement, and root-sign boundary
all reconstruct from the frozen statement.

If a trial succeeds with probability at least `1/Q(n)`, geometric repetition
has expected trial count **at most** `Q(n)`, not necessarily exactly `Q(n)`.
The statement's phrase "has expected `Q(n)` trials" is valid only in the usual
upper-bound sense. This does not affect the conditional Las Vegas conclusion.

The packet proves no success-probability lower bound, no useful dependency
law, no cross-discriminant sign split, and no factoring algorithm.

## Authentication

I computed each digest before using the file as evidence. The task's `SELF`
label denotes `SELF_AUDIT.md`.

| Frozen file | Supplied and computed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `de5c6833d7a5af14b144188b24cfa0c6e4734d5699824689baeed0bb45b2aa8a` | match |
| `PROOF.md` | `f5d1efbc4a61d67fe2cb4c68de7b96ceec281d144b1a899dd5eb8d737f99ab73` | match |
| `SELF_AUDIT.md` | `7ff1899f338f6079886fe827ab4fba35d5b40820b22d65e13df1b20d8bd0932f` | match |
| `MANIFEST.md` | `fddab20a0f5e40095c1beb2635b3c9f0b9771fe8a759efbbd5dea4d9889aabe3` | match |

The self-audit and manifest were checked for consistency, but were not used
as mathematical evidence.

## Independent reconstruction

### 1. Canonical carry identities

From `T_h=y_h+k_hN`, direct cancellation gives

\[
T_i k_j-T_j k_i=y_i k_j-y_j k_i
=\frac{T_jy_i-T_iy_j}{N}.
\]

Also `S_h^2=1+DT_h^2` gives
`S_h^2 = 1+Dy_h^2 mod N`. Thus the public unit screen makes each supplied
`x_h` a unit square root of `A_h` modulo `N`, exactly as claimed.

### 2. Full odd split and the factor at two

Set `A=1+Dy_i^2`, `u=y_i-y_j`, and `v=y_i+y_j`. Since
`gcd(A,D)=1` and `A_j-A_i=-Duv`,

\[
d=\gcd(A_i,A_j)=\gcd(A,uv).
\]

Hence `d_-` and `d_+` divide `d`. For an odd prime `ell | A`, `ell` cannot
divide both `u` and `v`: otherwise it divides `u+v=2y_i`, contrary to
`gcd(A,y_i)=1`. Therefore, with `a=v_ell(A)`, `b=v_ell(u)`, and
`c=v_ell(v)`, one of `b,c` is zero and

\[
v_\ell(d)=\min(a,b+c)=\min(a,b)+\min(a,c).
\]

This proves the coprime odd-part product and places every shared odd prime
power, to its full shared exponent, in exactly one coordinate-sign channel.

At two, the three relevant valuations are exactly

\[
v_2(d)=\min(a,b+c),\qquad
v_2(\operatorname{lcm}(d_-,d_+))
=\max\{\min(a,b),\min(a,c)\}.
\]

If `u,v` are not both even, these agree. If `y_i,y_j` are both even, `A` is
odd. In the only remaining case, `D,y_i,y_j` are odd, one of `b,c` is one,
and the other is at least two. The difference is then one exactly when
`v_2(A) >= b+c`. This reconstructs the stated formula and exact criterion
for `eta`. Moreover `gcd(A,u,v)` has no odd divisor and cannot contain
`4`, so `gcd(d_-,d_+)` is `1` or `2`.

The counterexample is exact:

\[
(D,y_i,y_j)=(7,1,3),\qquad (d,d_-,d_+)=(8,2,4).
\]

Thus the packet correctly rejects an unqualified full-integer lcm identity.

### 3. Resultant allocation and orbit identities

The two roots of `1+D(T_h-k_hX)^2` differ only by the two signs of a square
root of `-1/D`. Evaluating the other quadratic at those roots, or expanding
the quadratic resultant, gives

\[
\operatorname{Res}_X(f_i,f_j)
=D^2\bigl(D\Delta^2+(k_i-k_j)^2\bigr)
      \bigl(D\Delta^2+(k_i+k_j)^2\bigr).
\]

For `r=k_i-k_j` and `s=k_i+k_j`, the determinant has both forms

\[
\Delta=-y_ir+k_iu=y_is-k_iv.
\]

Consequently

\[
Q_-=A_i r^2+Dk_i u(k_i u-2y_i r),
\]

\[
Q_+=A_i s^2+Dk_i v(k_i v-2y_i s).
\]

These identities prove the full integer divisibilities `d_- | Q_-` and
`d_+ | Q_+`. They do not prove either converse, and the statement does not
claim one.

For two powers in one Pell orbit, substitute

\[
S_iS_j-DT_iT_j=S_{j-i},\qquad
S_iS_j+DT_iT_j=S_{i+j}
\]

into the expansions of `(k_iS_j-k_jS_i)^2` and
`(k_iS_j+k_jS_i)^2`. The residual constants are respectively
`(k_i-k_j)^2` and `(k_i+k_j)^2`, and the remaining quadratic term is
`D(T_i k_j-T_j k_i)^2`. This yields both displayed orbit formulas with the
claimed signs and indices.

### 4. One-sided hidden-prime ticket

The unit screen and Jacobi value `(-D/N)=-1` make `-D` a square at exactly
one of `p,q`. At the nonsplit prime, a zero of

\[
Q_\sigma=a_\sigma^2+D\Delta^2
\]

with nonzero `Delta` would make `-D` a square. If `Delta=0`, a zero forces
`a_sigma=0`. Thus a nonsplit zero requires both quantities to vanish modulo
that prime.

From `p<q<2p` and `N=pq`, both hidden primes exceed `sqrt(N/2)`. The strict
public bound `0<|a_sigma|<sqrt(N/2)` therefore prevents `a_sigma` from
vanishing at either hidden prime. The nonsplit prime cannot divide
`Q_sigma`, so the gcd is exactly one of `1` and the split prime and can never
be `N`.

At the split prime, any `w` with `w^2=-D` gives

\[
Q_\sigma=(a_\sigma-w\Delta)(a_\sigma+w\Delta),
\]

which proves the exact union of the two success congruences. A nontrivial
gcd is therefore always a certified factor. Repetition is polynomial only
under the explicitly assumed inverse-quasipolynomial event probability; no
such probability is derived.

### 5. Factor-free refinement

For a materialized bank, every signed gcd, odd part, resultant factor, and
gcd with `N` uses polynomially many exact integer operations on integers of
polynomial bit length. Refining a gcd-free P66 basis by every signed gcd
preserves its exact exponent data. The odd coprimality proved above separates
opposite pair labels. Repeating this for all pairs gives each final odd block
a uniform public label for every incident pair. The factor at two is retained
separately. Further gcd splitting does not change the binary parity kernel,
so the complete integer square-class kernel remains computable without
factoring the row values.

This label records congruences at rational divisors of exact row integers.
The normalized root `R(x_ix_j)^{-1} mod N` lives instead modulo the hidden
factors of `N`; there is no map from the former data to the latter sign.

### 6. Odd-multiple sign and the two certificates

For odd `h`, expansion of the Pell multiplication polynomial shows that
every term of `F_{h,D}(Y)` except its final term contains `1+DY^2`. Hence,
at every odd `ell | 1+Dy^2`,

\[
F_{h,D}(y)\equiv D^{(h-1)/2}y^h
\equiv(-1)^{(h-1)/2}y\pmod\ell.
\]

Thus clean odd multiples enter the minus channel for `h=1 mod 4` and the
plus channel for `h=3 mod 4`. The norm identity

\[
1+DF_{h,D}(Y)^2=(1+DY^2)G_{h,D}(Y)^2
\]

also makes the positive exact product root equal to the supplied root
product modulo `N` in the uncarried case. Its normalized root is therefore
`+1`, independently of the coordinate channel.

The global example checks exactly. For `D=2,N=13859`,

\[
19601^2-2\cdot13860^2=1,
\]

so the canonical coordinate is one. The fifth-multiple polynomials give
`F_{5,2}(1)=109` and `G_{5,2}(1)=89`, with `109<N`. Therefore

\[
A_6=3,\qquad A_{30}=23763=3\cdot89^2,
\]

the shared factor `3` is in the minus channel, and the exact root `267`
equals the supplied-root product modulo `N`.

The contrast also checks exactly. For `N=143`, the supplied roots satisfy

\[
17^2\equiv3,qquad 5^2\equiv23763\pmod {143}.
\]

The exact product is again the square `267^2`, and the same shared factor
`3` divides `1-109`. But

\[
\gcd(267-17\cdot5,143)=13,
\qquad
\gcd(267+17\cdot5,143)=11.
\]

Thus its normalized root is mixed. The plus-coordinate cleanup
`gcd(1+109,143)=11` also confirms the packet's warning that this is not a
screen-free algorithmic hit. The two examples prove only the declared
non-determination of normalized-root sign.

## Scope check

`SELF_AUDIT.md` and `MANIFEST.md` accurately summarize the proved content
and exclusions. No empirical, probability, cross-discriminant, or complete
factoring conclusion is smuggled into the frozen packet. I changed no frozen
artifact and wrote only this audit.
