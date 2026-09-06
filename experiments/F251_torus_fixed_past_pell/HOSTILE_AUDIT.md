# F251 hostile audit

## Verdict

**PASS.** The stated fixed-past Pell count and its conditional sampling
consequences reconstruct from the frozen statement. The proof is uniform in
the size and squarefree kernel of the fixed integer `P`. It does not extend to
a decoder that selects a past subset after it sees the fresh row.

No numerical evidence and no external result are needed for this verdict.

## Authentication

The audit authenticated every frozen file before reconstruction. The task's
`SELF` and `MANIFEST` labels correspond to the on-disk files `SELF_AUDIT.md`
and `MANIFEST.md`.

| Frozen file | SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `2fce8c0126d1454c68a39068ab28b8fda95cc3f270a1d83d7cd758a66c50c5e6` | match |
| `PROOF.md` | `3948902e35ae73e3a1cdcf68e1674f7be83e468911027c77bd9cb98c294ac707` | match |
| `SELF_AUDIT.md` | `e9284e54d6fcf6d39f03176caea3bbd0a327ba8cecbd49df060edb93365b3c25` | match |
| `PROVENANCE.md` | `1b3b912f24e20c875986b52d9018eab23f0b99603369ec44340a9ffc7cdf1a78` | match |
| `MANIFEST.md` | `a357bd3f97766b4651fc8c151ffc4d294e3723f0b6ebb2bf48dc8752572f2e11` | match |

## Independent reconstruction

### 1. Squarefree reduction, including `y=0`

Write the unique decomposition

\[
P=au^2
\]

with positive squarefree `a`. If

\[
au^2(1+Dy^2)=R^2,
\]

then prime valuations give `u | R`. Put `R=uw`. The equality becomes

\[
w^2=a(1+Dy^2).
\]

Every prime dividing squarefree `a` divides `w`, so `a | w`. With `w=av`,
division by `a` gives

\[
av^2-Dy^2=1.
\]

Conversely, this equation gives

\[
P(1+Dy^2)=a^2u^2v^2=(auv)^2.
\]

Thus the reduction is an equivalence, not only a necessary condition. We can
take `v>0`. For `y=0`, the equation is `av^2=1`, so it contributes exactly
one row when `a=1` and no row otherwise. This case is included in the later
monotone chain.

### 2. The quotient is integral

Set `K=aD` and associate to a solution

\[
\alpha_y=av+y\sqrt K.
\]

Its norm is `a`. For two solutions with `y_2>y_1`, direct division by this
common norm gives

\[
\frac{\alpha_{y_2}}{\alpha_{y_1}}
=av_1v_2-Dy_1y_2+(v_1y_2-v_2y_1)\sqrt K.
\]

Both coefficients are integers. Explicitly, before division by `a`, the
constant coefficient is

\[
a(av_1v_2-Dy_1y_2)
\]

and the `sqrt(K)` coefficient is

\[
a(v_1y_2-v_2y_1).
\]

Therefore division by `a` is exact in both coefficients. This is the step
that rules out multiple unrelated generalized-Pell seed classes.

### 3. Signs and the square-`K` case

After positive normalization,

\[
\frac{\alpha_y}{\sqrt a}
=\sqrt{1+Dy^2}+y\sqrt D
\]

is strictly increasing in `y`. Hence the quotient above has real value
larger than one. Its conjugate is its positive reciprocal. If the quotient
is `s+t sqrt(K)`, these two facts give `s>1` and `t>0`. Integrality then gives
`s>=2` and `t>=1`.

If `K=k^2` is an integer square, then

\[
(s-kt)(s+kt)=1.
\]

Both factors are positive integers. They must both equal one. This forces
`s=1` and `t=0`, contrary to two distinct increasing solutions. Therefore
square `K` permits at most one canonical coordinate. This argument also
covers the degenerate real quadratic algebra; it does not assume that
`Q(sqrt(K))` is a field.

### 4. Uniform lower growth

If `K` is not a square, then `K>=2`. Consecutive solution ratios satisfy

\[
s+t\sqrt K\ge 2+\sqrt K\ge 2+\sqrt2=\Lambda.
\]

This lower bound is valid although it is not sharp for every `K`. It is
independent of `a`, `P`, and the number of prime factors of either integer.

### 5. Count and endpoint check

List the represented coordinates as

\[
0\le y_1<\cdots<y_m<Y.
\]

The consecutive ratios telescope, so

\[
\Lambda^{m-1}
\le \frac{\alpha_{y_m}}{\alpha_{y_1}}
=\frac{\sqrt{1+Dy_m^2}+y_m\sqrt D}
       {\sqrt{1+Dy_1^2}+y_1\sqrt D}.
\]

The denominator is at least one. Since `y_m<Y`, the ratio is strictly less
than

\[
\sqrt{1+DY^2}+Y\sqrt D\le 1+2Y\sqrt D.
\]

Taking logarithms gives the claimed bound

\[
m\le 1+\left\lfloor
\frac{\log(1+2Y\sqrt D)}{\log(2+\sqrt2)}
\right\rfloor.
\]

The floor is safe also when the logarithmic ratio is an integer, because
the preceding endpoint inequality is strict. The square-`K` case has
`m<=1` and also satisfies this bound.

### 6. Modular roots and clean-torus probability

Because `P` and every admitted `A_y` are units modulo `N`, `Xx_y` is a unit
and is a supplied square root of `PA_y`. For an integer square `R^2=PA_y`,

\[
\zeta_y=R(Xx_y)^{-1}\pmod N
\]

satisfies `zeta_y^2=1 mod N`. Replacing `R` by `-R` only applies a global
sign. It cannot change a mixed root into a global root. Since `N=pq` with
distinct odd primes, a root other than the two global roots yields a proper
factor through `gcd(zeta_y-1,N)` or `gcd(zeta_y+1,N)`.

For a fresh conditional coordinate law with maximum atom `mu`, a successful
set of at most `B(D,Y)` coordinates has mass at most `mu B(D,Y)`. The past
may determine `P` arbitrarily, but it must determine `P` before sampling the
fresh coordinate.

For two independent rows, condition on the first row. Its positive integer
`A_z` and supplied root `x_z` give the fixed data `P=A_z` and `X=x_z` for
the second row. At most `B(D,N)` second coordinates work. This proves
`B(D,N)/|mathcal Y|` for a uniform coordinate set.

For uniform points, each successful second coordinate lifts to at most `c`
points. The bound is therefore `c B(D,N)/H`. On the raw norm-one torus, a
fixed `y mod N` leaves the congruence

\[
x^2\equiv1+Dy^2\pmod N.
\]

It has at most two roots modulo each of `p` and `q`, hence at most four by
CRT. Thus `c=4` is valid. The stated powered-image consequence is
conditional on its explicit fibre bound `c=2`.

The diagonal event causes no exception: `A_y^2` is always a square, but
`B(D,N)>=1`, so its collision probability is already inside the bound.
A union bound over the `binom(T,2)` unordered pairs then gives the bank
estimate. If `T=2^{polylog(n)}`, `B=n^{O(1)}`, and `H=2^{Omega(n)}`, its
value is `2^{-Omega(n)}` because every fixed polylogarithm is `o(n)`.

## Exact limitation

The proof supports these uses:

1. A product and its modular square root are fixed from the past. One fresh
   row is then sampled.
2. Two rows are sampled independently. Conditioning fixes either row before
   the other is counted.
3. A prescribed adaptive sequence uses the one-step conditional bound at
   each step, followed by a union bound when needed.

The proof does not give one simultaneous bound for all past subset products.
After a fresh row is visible, a decoder can choose among exponentially many
past products. Conditioning on a product selected with knowledge of that
fresh row would reverse the required quantifiers. The proof also gives no
bound for a retrospectively selected product of three or more rows. The
frozen statement declares both limitations correctly.

## Hostile conclusion

The squarefree reduction is reversible. The divisibility by `u` and then by
`a` is exact. The ratio coefficients are integral. Square `K`, `y=0`, the
growth constant, the endpoint floor, diagonal pairs, root normalization,
and raw-torus fibres all pass reconstruction. No claim crosses the
fixed-past/fresh-row boundary. The packet is suitable for a separate strict
statement-only reconstruction gate.
