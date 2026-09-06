# Blind reconstruction of F204

## Protocol and verdict

The frozen statement was hashed before it was opened. Its SHA-256 hash was

`020717143764c86138c4ac0d211924884330385c2d7a578c1e1c4a540c2f5929`.

This reconstruction used only `PROMPT.md` and the frozen F204 `STATEMENT.md`.
It used no numerical experiment.

**Verdict: PASS.** All four named boundary claims reconstruct from the stated
definitions and hypotheses. The scalar modularity result is a necessary cusp
test only. The final result is not a factoring algorithm and is not a lower
bound against mechanisms outside the named scope.

## 1. Definitions and the coefficient's factoring role

Let

\[
 \chi(d)=0\quad(2\mid d),\qquad
 \chi(d)=1\quad(d\equiv1\pmod4),\qquad
 \chi(d)=-1\quad(d\equiv3\pmod4),
\]

and put

\[
 A(n)=\sum_{d\mid n}d\chi(d),\qquad
 L(q)=\sum_{n\ge1}A(n)q^n,
\]

\[
 P(q)=\prod_{a\ge1}(1-q^a)^{\chi(a)}
     =\frac{(q;q^4)_\infty}{(q^3;q^4)_\infty}.
\]

The product is well-defined coefficientwise as a formal series in
`1+q Q[[q]]`, and it converges without zeros for `|q|<1`.

For completeness, suppose that `N=pq`, where `p` and `q` are distinct odd
primes. Since the divisor sum of the multiplicative function `d chi(d)` is
multiplicative,

\[
 A(N)=(1+p\chi(p))(1+q\chi(q)).
\]

Write `epsilon_p=chi(p)`, `epsilon_q=chi(q)`, and
`delta=chi(N)=epsilon_p epsilon_q`, which is known from `N mod 4`. Then

\[
 D:=A(N)-1-\delta N=\epsilon_p p+\epsilon_q q.
\]

If `delta=1`, then `|D|=p+q`. If `delta=-1`, then
`|D|=|p-q|` and

\[
 p+q=\sqrt{D^2+4N}.
\]

In either case, `p` and `q` are recovered as the roots of
`X^2-(p+q)X+N`. Thus exact evaluation of `A(N)` does factor the stated
odd-distinct-semiprime target. Balance is not needed for this algebraic
recovery. The arguments below do not provide that evaluation.

## 2. Logarithmic derivative and the exact binary norm

Formal logarithms give

\[
 \begin{aligned}
 -q\frac{d}{dq}\log P(q)
 &= -q\frac{d}{dq}
    \sum_{a\ge1}\chi(a)\log(1-q^a)\\
 &=\sum_{a\ge1}\sum_{m\ge1}a\chi(a)q^{am}\\
 &=\sum_{n\ge1}\left(\sum_{a\mid n}a\chi(a)\right)q^n
 =L(q).
 \end{aligned}
\]

Only odd `a` contribute. Hence

\[
 \begin{aligned}
 P(q)P(-q)
 &=\prod_{a\ge1}
   \bigl((1-q^a)(1+q^a)\bigr)^{\chi(a)}\\
 &=\prod_{a\ge1}(1-q^{2a})^{\chi(a)}
 =P(q^2).
 \end{aligned}
\]

Applying `-q d/dq` to its logarithm gives

\[
 L(q)+L(-q)=2L(q^2).
\]

At an even power `q^{2n}`, this says `2A(2n)=2A(n)`. At an odd
power both sides vanish. Therefore the identity is exactly

\[
 A(2n)=A(n).
\]

### Complete formal freedom at odd indices

Let `R` be a commutative rational algebra, let
`G(q) in 1+qR[[q]]`, and write

\[
 \log G(q)=\sum_{m\ge1}g_mq^m.
\]

The formal logarithm is a homomorphism from multiplication in
`1+qR[[q]]` to addition in `qR[[q]]`. Consequently,

\[
 G(q)G(-q)=G(q^2)
\]

is equivalent to

\[
 \sum_{m\ge1}(1+(-1)^m)g_mq^m
 =\sum_{m\ge1}g_mq^{2m}.
\]

The odd coefficients impose `0=0`, while the coefficient of `q^{2n}` is

\[
 2g_{2n}=g_n.
\]

Conversely, these relations make the logarithms equal, and formal
exponentiation recovers the product identity. Thus one may choose every
`g_r` for odd `r` independently, after which

\[
 g_{2^v r}=2^{-v}g_r\qquad(r\text{ odd},\ v\ge0)
\]

is forced and is the only constraint. Iterating the binary norm therefore
never creates an equation that determines a coefficient on an odd orbit.

## 3. Scalar modularity in the binary orbit

Set `q=e^{2 pi i tau}` and

\[
 F_{a,b,\alpha}(\tau)
 =e^{2\pi i\alpha\tau}P(q)^aP(-q)^b,
 \qquad a,b\in\mathbb Z,\quad\alpha\in\mathbb R.
\]

Assume that this nonzero function is a scalar meromorphic modular form of
one real weight `k`, with a multiplier system, on a finite-index subgroup of
`SL_2(Z)`, and that after a scaling matrix it has a usual meromorphic Fourier
expansion at every rational cusp. We prove that `a=b`.

### Radial behavior at `1` and `-1`

For `q=e^{-t}` and `Q=q^4=e^{-4t}`, the standard `Q`-gamma identity gives

\[
 \begin{aligned}
 P(e^{-t})
 &=\frac{(Q^{1/4};Q)_\infty}{(Q^{3/4};Q)_\infty}\\
 &=(1-Q)^{1/2}
   \frac{\Gamma_Q(3/4)}{\Gamma_Q(1/4)}.
 \end{aligned}
\]

As `Q` increases to `1`, `Gamma_Q(x)` tends to `Gamma(x)`. Hence, for a
nonzero constant `C`,

\[
 P(e^{-t})=C t^{1/2}(1+o(1)).
\]

The binary norm now gives the behavior at `-1` without another asymptotic
calculation:

\[
 P(-e^{-t})=\frac{P(e^{-2t})}{P(e^{-t})}
            =\sqrt2\,(1+o(1)).
\]

Put `t=2 pi y`. At the finite cusp `0`, where `tau=iy`, these formulas yield

\[
 \log|F_{a,b,\alpha}(iy)|=\frac a2\log y+O(1).
\]

At the finite cusp `1/2`, where `tau=1/2+iy`, they yield

\[
 \log|F_{a,b,\alpha}(1/2+iy)|=\frac b2\log y+O(1).
\]

The exponential prefactor has modulus `e^{-2 pi alpha y}` at both cusps, so
it contributes only `O(y)` to these logarithms.

### Universal power at a finite modular cusp

Let `f` be any nonzero scalar meromorphic modular form satisfying the stated
hypotheses, and let `r` be a finite rational cusp. Choose a scaling matrix
`sigma` with `sigma(infinity)=r`. If `z=sigma^{-1}(r+iy)`, then

\[
 \operatorname{Im}z\asymp y^{-1},\qquad
 |j(\sigma,z)|\asymp y^{-1}.
\]

The first nonzero term of the meromorphic Fourier expansion of
`f|_k sigma` gives, as `y` decreases to zero,

\[
 \log|f(r+iy)|=\frac{c_r}{y}-k\log y+O(1)
\]

for a cusp-dependent real constant `c_r`. Poles merely permit `c_r` to have
the opposite sign from a zero. The coefficient of `log y` is always `-k`;
this is the scalar weight factor and is independent of the cusp.

Comparison with the radial behavior above first forces `c_0=c_{1/2}=0` and
then gives

\[
 \frac a2=-k=\frac b2.
\]

Therefore

\[
 a=b.
\]

Taking `(a,b)=(1,0)` proves that `P(q)` itself cannot satisfy the scalar
modularity hypothesis. The same argument applies to any proposed scalar
generalized-eta or Siegel-unit identification that has the stated ordinary
cusp expansions.

Finally,

\[
 -q\frac{d}{dq}\log\bigl(P(q)^aP(-q)^b\bigr)
 =aL(q)+bL(-q).
\]

For odd `N`, the coefficient of `q^N` is `(a-b)A(N)`. Thus retaining the
target requires `a != b`, which contradicts the necessary modular cusp test.
Every monomial that survives the test has `a=b` and deletes every odd target
coefficient. Nothing here proves that a surviving monomial is modular.

## 4. Parity, the infinite two-kernel, and the Mahler obstruction

Modulo two, every odd `d` has `d chi(d)=1`, while every even `d` contributes
zero. Therefore

\[
 A(n)\equiv \#\{d:d\mid n,\ d\text{ odd}\}\pmod2.
\]

The number of divisors of a positive integer is odd exactly when that integer
is a square. It follows that

\[
 A(n)\equiv1\pmod2
 \quad\Longleftrightarrow\quad
 \operatorname{oddpart}(n)\text{ is a square}.
\]

Let `c(0)=0` and `c(n)=A(n) mod 2` for `n>=1`. For every `e>=3`, the
two-kernel contains

\[
 c_e(n):=c(2^e n+1),\qquad n\ge0.
\]

Because `2^e n+1` is odd, `c_e(n)=1` exactly when `2^e n+1` is a square.
The four solutions of

\[
 x^2\equiv1\pmod{2^e}\qquad(e\ge3)
\]

are

\[
 x\equiv 1,-1,1+2^{e-1},-1+2^{e-1}\pmod{2^e}.
\]

Thus the smallest positive representative larger than `1` is
`2^{e-1}-1`. Consequently the first `n>0` for which `c_e(n)=1` is

\[
 n_e=\frac{(2^{e-1}-1)^2-1}{2^e}=2^{e-2}-1.
\]

These first-occurrence positions are different for every `e`. Hence the
two-kernel is infinite. By the finite-kernel characterization of automatic
sequences, `c` is not two-automatic.

Now suppose, for contradiction, that

\[
 R_{-1}(q)+\sum_{i=0}^sR_i(q)L(q^{2^i})=0,
 \qquad R_i(q)\in\mathbb Q(q),
\]

with at least one `R_i`, `i>=0`, nonzero. Clear the common rational-function
denominator and all rational scalar denominators. This gives

\[
 P_{-1}(q)+\sum_{i=0}^sP_i(q)L(q^{2^i})=0,
 \qquad P_i(q)\in\mathbb Z[q].
\]

Let `2^v` be the largest common power of two dividing the coefficients of
all `P_i` with `i>=0`. Since every coefficient of `L` is integral, the
identity implies that every coefficient of `P_{-1}` is also divisible by
`2^v`. Divide the full identity by this power. After reduction modulo two,
at least one coefficient polynomial multiplying an iterate remains nonzero.

Let

\[
 C(q)=\sum_{n\ge0}c(n)q^n\in\mathbb F_2[[q]].
\]

In characteristic two,

\[
 C(q^{2^i})=C(q)^{2^i}.
\]

The reduced identity is therefore

\[
 \overline P_{-1}(q)
 +\sum_{i=0}^s\overline P_i(q)C(q)^{2^i}=0.
\]

This is a nonzero polynomial equation for `C(q)` over `F_2(q)`: the powers
of its indeterminate are distinct, and at least one coefficient with
positive power is nonzero. Hence `C(q)` is algebraic over `F_2(q)`. Christol's
theorem would then make `c` two-automatic, contradicting its infinite
two-kernel. No such homogeneous or inhomogeneous linear base-two Mahler
equation exists.

## 5. Norms over an odd-prime root orbit

Let `ell` be an odd prime, let `zeta` be a primitive `ell`-th root of unity,
and set `epsilon=chi(ell)`. For a fixed `a`,

\[
 \prod_{j=0}^{\ell-1}(1-\zeta^{ja}q^a)
 =\begin{cases}
   1-q^{\ell a},&\ell\nmid a,\\
   (1-q^a)^\ell,&\ell\mid a.
  \end{cases}
\]

It follows that

\[
 \begin{aligned}
 \prod_{j=0}^{\ell-1}P(\zeta^jq)
 &=\prod_{\ell\nmid a}(1-q^{\ell a})^{\chi(a)}
   \prod_{\ell\mid a}(1-q^a)^{\ell\chi(a)}.
 \end{aligned}
\]

The first product is

\[
 \frac{P(q^\ell)}{P(q^{\ell^2})^\epsilon},
\]

because `chi(ell b)=epsilon chi(b)`. The second product is
`P(q^ell)^{ell epsilon}`. Hence

\[
 \prod_{j=0}^{\ell-1}P(\zeta^jq)
 =\frac{P(q^\ell)^{1+\ell\epsilon}}
        {P(q^{\ell^2})^\epsilon}.
\]

Logarithmic differentiation of the left side gives the root filter

\[
 \sum_{j=0}^{\ell-1}L(\zeta^jq)
 =\ell\sum_{k\ge1}A(\ell k)q^{\ell k}.
\]

On the right side it gives

\[
 \ell(1+\ell\epsilon)L(q^\ell)
 -\epsilon\ell^2L(q^{\ell^2}).
\]

Equating the coefficient of `q^{ell k}` and dividing by `ell` proves

\[
 A(\ell k)
 =(1+\ell\epsilon)A(k)
 -\epsilon\ell\,\mathbf 1_{\ell\mid k}A(k/\ell).
\]

This is precisely the local Euler recurrence. For a composite target `N`, a
fixed public `ell` yields smaller arguments only if `ell` divides `N`; then
`gcd(ell,N)` already reveals the factor (in the stated semiprime scope,
`ell` is a proper factor). If `ell` does not divide `N`, setting `k=N` gives

\[
 A(\ell N)=(1+\ell\epsilon)A(N),
\]

which connects the target only to a larger index.

## 6. Exact scope of the boundary

The reconstruction establishes only these four named facts:

1. The binary norm and its logarithmic derivative are an exact parity filter,
   with complete freedom on every odd logarithmic orbit.
2. Within scalar monomials in `P(q)` and `P(-q)`, the ordinary finite-index
   modular cusp hypotheses force `a=b`, which deletes odd coefficients.
3. `L` satisfies no fixed finite linear base-two Mahler equation over
   `Q(q)`.
4. A fixed odd-prime root norm reproduces the local Euler recurrence and
   supplies no hidden-factor contraction.

The obstruction is loss of information at the same odd node, not excessive
recursion depth. If another construction supplied one strictly smaller child
with quasipolynomial local work, then

\[
 T(n)\le T(n-1)+\operatorname{QP}(n)
\]

would still be quasipolynomial, since summing at most `n` monotone QP terms
only multiplies the bound by `n`.

Nothing proved here excludes arbitrary algorithms, nonlinear or
nonholomorphic functional equations, vector-valued modular objects,
QP-growing section state, or adaptive one-child integer decoders. In
particular, the result supplies neither a coefficient evaluator nor the
classical Las Vegas quasipolynomial-time factoring algorithm required by the
top-level prompt.
