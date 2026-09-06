# Hostile audit of F242

## Verdict

**PASS.**  The frozen statement is correct in its stated scope.  The exact
formula is for the clean powered phase.  Proper gcd exits are extra verified
successes.  The packet does not supply the missing quasipolynomial word.

## Authentication

I authenticated the supplied files before reading their contents.  The
observed SHA-256 values were

```text
e3364b88dbf11b4a1b53daeeaa629e6c22d97de58615a146a671c616ac2c7123  STATEMENT.md
8b6217f246b4f7462a619322256c4e474e90ad6a1204dceccbe831dc0dd21719  PROOF.md
a4a0d42552c75143ed86b53d94130e163d005c1f9c18fabbc49147074566eb36  SELF_AUDIT.md
4de0646c0e0ccf0f364ca7ce22416a44af4496f57f74aed1fd533e7dbefd47b6  PROVENANCE.md
8954d70255041168f931e40b5f824d8f67c23b1ec2af72b2cb16d5ab74114b55  MANIFEST.md
```

All five values agree with the externally supplied hashes.

## 1. Reconstruction of the shifted common factor

Fix one hidden orientation and write

\[
 m_p=p-\epsilon_p,\qquad m_q=q-\epsilon_q,
 \qquad J=\epsilon_p\epsilon_q.
\]

Modulo `m_p`, the equality `p=epsilon_p` gives

\[
 N-J\equiv \epsilon_p(q-\epsilon_q)
          =\epsilon_p m_q\pmod {m_p}.
\]

Therefore

\[
 \gcd(N-J,m_p)=\gcd(m_p,m_q)=d.
\]

The symmetric identity holds at `q`.  This argument uses neither hidden
sign individually in the public exponent nor a factorization of `N-J`.
Only their public product `J=(D/N)` occurs.

Put `N-J=dA` and `m_p=ds_p`.  Dividing the preceding gcd identity by `d`
shows `gcd(A,s_p)=1`.  Hence, for `E=(N-J)W`,

\[
 \gcd(E,m_p)=d\gcd(W,s_p).
\]

The same formula holds at `q`.  This remains valid when `d` and `s_p`
share prime factors.  No unspoken pairwise-coprimality with `d` is needed.
It follows that the kernel fractions of the two local power maps are

\[
 {\gcd(E,m_i)\over m_i}
 = {1\over s_i/\gcd(s_i,W)}={1\over r_i}.
\]

This proves the shifted residual factorization exactly.

## 2. Reconstruction of the full-torus sampler

For a hidden prime `r`, reduction of the public algebra gives

\[
 A_D(\mathbb F_r)=\mathbb F_r[w]/(w^2-D).
\]

An element `z` is a unit exactly when its norm is nonzero.  Thus the public
test `gcd(A^2-DB^2,N)=1` certifies the only inverse used in the
normalization.  The formula

\[
 {z\over\bar z}={z^2\over z\bar z}
\]

then gives the two displayed coefficients of `U`.  After this step, the
pair multiplication rule is ordinary multiplication in the quotient
algebra and uses no division.

I checked the two local fibre counts separately.

* In the split case, choose a proof-only square root of `D`.  The algebra is
  `F_r x F_r`, conjugation swaps the factors, and
  `(x,y)` maps to `(x/y,y/x)`.  Each target `(t,t^-1)` has the `r-1`
  preimages `(ty,y)`, with `y` nonzero.
* In the nonsplit case, the algebra is `F_(r^2)` and conjugation is the
  `r`-power map.  The map is `z -> z^(1-r)`.  Its kernel is `F_r^*`, of
  size `r-1`, and its image has size `r+1`.  This is the full norm-one
  subgroup.

Thus both algebra types have constant fibres, and both signed identity
points occur.  The construction has no Cayley-chart omission.

CRT sends a uniform coefficient pair modulo `N` to independent uniform
local algebra elements.  The clean event is the product of the two local
unit events.  Conditioning on that product preserves local independence.
The two constant-fibre maps then give independent uniform points in the
two full local tori.

The screens cover all denominator failures:

* `gcd(D,N)` handles a singular discriminant before the algebra is used.
* `gcd(N,A,B)` detects a zero element in either local algebra.
* The norm gcd also detects every split zero divisor and the zero element
  in a nonsplit field.
* A proper gcd is already a verified factor.  A gcd equal to `N` is only a
  rejection.  An inverse is attempted only after the norm gcd is one.

For one hidden prime, the exact clean density is

\[
 {(r-1)(r-\epsilon_r)\over r^2}
 =\left(1-{1\over r}\right)
  \left(1-{\epsilon_r\over r}\right).
\]

It is at least `4/9`.  The global clean probability is therefore at least
`16/81`.  Early proper gcd exits can only shorten the procedure.  The
claimed bound of `81/16` on the expected number of coefficient pairs is
valid.

## 3. Reconstruction of the exact powered law

The local tori are cyclic of orders `m_p` and `m_q`.  The preceding kernel
calculation and the exact sampler give independent return events with
probabilities `alpha_p=1/r_p` and `alpha_q=1/r_q`.

If exactly one component returns to `+1`, the joint-coordinate `G_+`
screen returns exactly the corresponding hidden prime.  If neither returns,
that screen is one and the specified trial stops.  If both return, it is
`N` and the square chain starts.  Therefore the exactly-one-return atoms
contribute

\[
 \alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p).
\]

Write `E=2^v u`, with `u` odd, and `e_i=v_2(m_i)`.  Conditional on local
return, the point is uniform in the power-map kernel.  Its two-primary
coordinate is consequently uniform in the unique subgroup of size

\[
 2^{h_i},\qquad h_i=\min(e_i,v).
\]

The odd part is killed by the `u`-power.  The `u`-power is an automorphism
on the two-primary part, so it preserves exact two-power order.

For a uniform element of `C_(2^h)`, let `K` satisfy
`ord(x)=2^K`.  Direct counting gives

\[
 \Pr(K=0)=2^{-h},\qquad
 \Pr(K=j)=2^{j-1-h}\quad(1\le j\le h).
\]

This handles unequal kernel sizes.  If the two values of `K` differ, the
smaller-order component reaches `+1` while the other has not, so a joint
screen yields a proper factor.  If they agree, both components reach the
unique `-1` and then `+1` at the same stages.  Before those stages neither
is a signed identity.  Every screen is then one or `N`.  Thus the chain
succeeds exactly when the two order exponents differ.

For `a=min(h_p,h_q)` and `b=max(h_p,h_q)`, the failure probability is

\[
 \sum_{j=0}^a \Pr_a(K=j)\Pr_b(K=j)
 ={4^a+2\over3\,2^{a+b}}.
\]

Both `a` and `b` are at least one because `m_p`, `m_q`, and `N-J` are
even.  The failure expression is largest at `b=a`, where it is at most
`1/2`.  Therefore `mu_(a,b)>=1/2`.

Adding the global-return contribution gives exactly

\[
 S=\alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q.
\]

The elementary two-case comparison in the packet correctly proves

\[
 S\ge \mu_{a,b}\max(\alpha_p,\alpha_q)
  \ge {1\over2\min(r_p,r_q)}.
\]

This is exact for the specified clean powered phase.  The algorithm does
not claim to count factors that a different Miller chain might obtain on
the neither-return atom.

## 4. Four orientations and a rejection nuance

Uniform units modulo `p` have each Legendre sign with probability `1/2`,
and the same is true modulo `q`.  CRT makes the two signs independent.
Therefore a uniform unit `D modulo N` gives all four orientations with
probability `1/4`.  The public Jacobi symbol reveals only their product.

For a fixed word `W`, the clean powered law depends on `D` only through
the two signs.  Under the hierarchical clean experiment

1. sample a uniform unit `D`, and
2. for that fixed `D`, sample a clean algebra unit,

the orientation weights remain exactly `1/4`.  Averaging the clean laws
therefore gives

\[
 {1\over4}\sum_\epsilon S_\epsilon
 \ge {1\over8\min_\epsilon R_\epsilon}.
\]

There is one wording-sensitive point worth preserving.  In the executable
sampler, a proper norm gcd ends the algorithm before a clean point is
reached.  Conditional only on those runs that reach the powered phase, the
orientation weights need not remain `1/4`, because the probability of an
early factor can depend on the orientation.  This does not weaken the
displayed Las Vegas lower bound.  For every fixed `D`, if `c_D` is the
per-attempt clean probability and `f_D` the per-attempt proper-factor
probability, the success probability before the next choice of `D` is

\[
 {f_D+c_D S_D\over f_D+c_D}\ge S_D.
\]

Averaging this pointwise inequality over the initially uniform `D` gives
at least the same `1/4` average.  Thus early exits add success even though
they can bias the conditional law of powered phases.  By contrast,
discarding `D` after every nonunit coefficient pair would directly weight
orientations by their unequal split and nonsplit clean densities.  The
packet correctly excludes that procedure.

The `(+,+)` row has local orders `p-1,q-1` and reproduces P205 exactly.
The other rows replace one or both orders by `p+1,q+1`.  Nothing in the
averaging argument forces any one residual to be small.

## 5. P158 boundary and scope

I checked the cited P158 statement.  On that family,

\[
 \gcd(p-1,q-1)=6,
\]

and the other three shifted gcds lie in `{2,4}`.  Hence every shifted common
part is at most six.  With `W=1`, each residual on the smaller side is at
least `(p-1)/6`.  Since `log p=Theta(log N)` on the family,
`R_epsilon=2^Theta(log N)` in all four rows.  Formula `S<=alpha_p+alpha_q`
then gives exponentially small clean success.  The zero-divisor exits are
also `O(1/p)` per constant expected sampler stage.  The claimed obstruction
to a quasipolynomial number of bare `W=1` orientation trials follows.

This argument does not obstruct a word that absorbs a shifted residual.
It also does not analyze a word that depends materially on the full value
of `D`.  The packet states both exclusions.

The bit-cost claim is conditional and correct.  Every public coefficient
has `O(log N)` bits.  The exponent has `O(log N+log W)` bits.  Binary
powering, the square chain, Jacobi symbols, certified inversion, and gcds
are polynomial in that bit length.  A success probability at least
`1/(2R)` gives at most `2R` expected clean powered trials.  Thus the stated
numerical-quasipolynomial cost follows when both `log W` and `R` have that
size.  The packet does not charge for constructing `W`, because it does not
construct one.

The proof is restricted to distinct odd semiprimes.  It does not cover
prime powers or general composites.  It requires a fixed public word for
the four-orientation average.  It gives no all-input bound on a shifted
residual and no all-input factoring algorithm.

## 6. Counterexample search

I attacked the following edge cases directly:

* split algebras with nonzero zero divisors;
* nonsplit algebras and both signed identity points;
* `d` sharing a prime with one residual quotient;
* `r_p=1` or `r_q=1`;
* the smallest possible two-primary kernel `h_i=1`;
* unequal values of `h_p` and `h_q`;
* all four Legendre orientations;
* words with extra powers of two; and
* early coefficient and norm gcd exits.

No counterexample survived the exact calculations above.

As a diagnostic after the algebraic reconstruction, I exhaustively checked
1,148 small fixed `(p,q,D,W)` cases, using the distinct prime pairs
`(3,5)`, `(3,7)`, `(3,11)`, `(5,7)`, `(5,11)`, and `(7,11)`, every unit
`D`, and the words `1,2,3,5,6,7,10`.  Enumeration of all clean coefficient
pairs found constant global Hilbert--90 fibre sizes and matched the exact
rational value of `S` in every case.  This finite check is not used as a
proof.

## Final assessment

The exact shifted-order identity, the factor-free full-torus sampler, the
unequal-kernel Miller law, and the fixed-word four-orientation reduction all
survive hostile reconstruction.  The remaining core problem is exactly the
one the packet leaves open: construct a public quasipolynomial-bit word that
absorbs enough of at least one ordinary or shifted residual on every input.

