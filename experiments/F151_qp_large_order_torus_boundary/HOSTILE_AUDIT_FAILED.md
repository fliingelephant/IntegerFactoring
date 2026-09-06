# F151 hostile audit — FAIL

## Frozen inputs

I audited the complete proof-only candidate with the expected hashes:

- `STATEMENT.md`:
  `eaa960c2e3e9ee594ec714d58d2a69af0ea2e1c818c89524cbd154aef2935acb`;
- `PROOF.md`:
  `0cc9660bc00f668c5f14f34ac684fa916e0acd4e05c59108b8a9864c761dcefd`;
- pre-audit `MANIFEST.md`:
  `5e79c7fdbfdd6c36487bb14ff421b4455a1eef636c1b668a0a0b677c852ee5c8`.

All hashes matched before the audit. I read all three files. I did not modify
the frozen statement, proof, or manifest.

I also checked the two external black boxes against their primary sources:

- Harvey--Hittmeir,
  [arXiv:2601.11131v2](https://arxiv.org/abs/2601.11131), Theorem 1.1;
- Pilatte,
  [arXiv:2404.16450v2](https://arxiv.org/abs/2404.16450), Corollary 1.5
  and Theorem 3.18.

## Verdict

**FAIL.** The four displayed mathematical theorems are correct under their
stated hypotheses. The frozen statement nevertheless draws one false,
unqualified conclusion from Theorems 1 and 2: it says that carry effects are
the only possible progress source for the short power bank. Large local order
only excludes the explicitly listed low-exponent collisions. It does not
exclude a factor-bearing collision at a larger exponent or a different
decoder applied to the same public element.

This is a scope failure, not a defect in the large-order upgrade, the Pilatte
count, or the torus algebra. A corrected statement needs a fresh hostile
audit.

## Fatal issue — local collision freedom does not make carries exclusive

After (7), the frozen statement says:

> The large-order theorem does not control these carry effects. They are the
> only possible source of progress for this short power bank.

The title and the sentence after Theorem 1 also say, without a defined
restricted decoder model, that the source is not a factor signal or is not
factor-correlated. The proved order condition does not imply these claims.

Here is a complete counterexample to the exclusivity statement. Take

\[
N=77=7\cdot11,\qquad B=4,\qquad \alpha=3.
\]

Then

\[
\operatorname{ord}_7(3)=6,
\qquad
\operatorname{ord}_{11}(3)=5,
\qquad
\operatorname{ord}_{77}(3)=30.
\]

Thus all local and global orders exceed `B`. The complete upgrade scan is
null:

\[
\gcd(3^e-1,77)=1
\qquad(1\le e\le4).
\]

The short bank has only `e=1`. Its canonical inverse is `w_1=26`, and both
stated inverse-pair screens are null:

\[
\gcd(3-26,77)=\gcd(3+26,77)=1.
\]

But the same public bank element gives

\[
\gcd(c_1^5-1,77)
=\gcd(3^5-1,77)
=11.
\]

This factor comes from a component-order mismatch at an exponent outside the
certified collision-free window. It does not require the integer
factorization, shared factors, or parity closure of `P_1=c_1w_1`.

The example does not show a general factoring algorithm. It shows that the
proved hypotheses cannot support the word "only." The minimal repair is to
say:

- the four listed collision channels are null in the certified window; and
- carry/refinement effects are the remaining channels **inside the specific
  canonical-exact-value decoder studied here**.

The statement must leave larger exponents and other value-dependent decoders
open. The title should similarly say that the factor signal remains
unresolved, not that there is no factor signal.

## Claims that survived the hostile check

### 1. Harvey--Hittmeir and the all-component upgrade

The cited Theorem 1.1 has exactly the required input range
`N >= 3`, `1 <= B < N-1`. It returns a nontrivial divisor or a unit of order
greater than `B`. Its stated bit cost is

\[
O\!\left(
\frac{B^{1/2}\log B}{(\log\log B)^{1/2}}\log N
\right).
\]

This agrees with the frozen proof. For
`B=2^((log n)^O(1))`, both this call and the added `B` modular-power/gcd
scan have quasipolynomial cost.

Let `r` be any rational prime divisor of `N`. If
`ord_r(alpha)=e <= B`, then `r` divides
`gcd(alpha^e-1,N)`. If that gcd were all of `N`, then
`ord_N(alpha) <= e <= B`, contrary to the Harvey--Hittmeir output. Hence the
scan returns a proper divisor. On the surviving branch every residue-field
order exceeds `B`. This remains correct for repeated prime factors. It makes
no claim about each prime-power order.

### 2. Every displayed short-bank gcd

For distinct `e,f <= floor(B/4)`, divisibility by a prime component in the
four screens from (5) would force one of

\[
\alpha^{|e-f|}=1,
\quad
\alpha^{2|e-f|}=1,
\quad
\alpha^{e+f}=1,
\quad
\alpha^{2(e+f)}=1.
\]

Every positive exponent here is at most `B`. This contradicts the local
order bound. The same argument gives (6): after multiplication by the unit
`c_e`, its two signs reduce to `c_e^2-1` and `c_e^2+1`; a local zero would
force order dividing `2e` or `4e`, again at most `B`. Thus all gcd formulas
in Theorem 2 are correct.

### 3. Pilatte's dimension, norm, and catalogue count

Pilatte's Corollary 1.5 takes

\[
d=\lceil\sqrt{\log N}\rceil,
\qquad
X=d^{10^3d},
\]

and samples `d` primes independently and uniformly, with replacement, from
the primes at most `X` that do not divide `N`. With high probability, the
resulting full relation lattice has a basis with Euclidean norms
`exp(O(d))`. Theorem 3.18 gives the explicit general bound
`<< exp(42(d+r))`; Corollary 1.5 is its `r=0` case.

For a fixed radius `R=exp(Cd)` large enough to cover that promised norm
bound, the integer ball is contained in `[-R,R]^d` and contains the integer
box of coordinate radius `floor(R/sqrt(d))`. Therefore its number of integer
points is

\[
\exp(\Theta(d^2))=\exp(\Theta(n)).
\]

The frozen brute-force catalogue count is correct. It is only a count for
enumerating the complete ball. It is not a lower bound against a structured
sampler, and the frozen statement correctly says so. Pilatte gives no
polylogarithmic support guarantee.

### 4. Jacobi-torus and Kummer splice

For each hidden odd prime `r`, local order greater than `B >= 4` gives
`alpha != +/-1 (mod r)`. Hence

\[
x^2-1
=\left(\frac{\alpha-\alpha^{-1}}2\right)^2
\]

is a nonzero square modulo `r`. Since inversion does not change a quadratic
character,

\[
\left(\frac{\Delta^{-1}(x^2-1)}r\right)
=\left(\frac\Delta r\right).
\]

Jacobi symbol `-1` gives opposite local Legendre symbols, so the fixed
equation `x^2-Delta*y^2=1` has a `y` in exactly the split component and no
global `y modulo N`. In the split component, a square root `s^2=Delta`
gives

\[
y=\frac{\alpha-\alpha^{-1}}{2s},
\qquad x+ys=\alpha,
\qquad x-ys=\alpha^{-1}.
\]

The Chebyshev identity also gives

\[
T_m(x)=\frac{\alpha^m+\alpha^{-m}}2
\]

for every nonnegative integer `m`. If the statement wants all integers
`m`, it should define the harmless extension `T_{-m}=T_m`; standard
Chebyshev polynomials are normally indexed by nonnegative integers. This is
a notation repair, not a second mathematical failure.

The theorem correctly closes only the fixed-`x` direct splice. It does not
close other torus coordinates or decoders.

## Scope conclusion

The candidate contains three sound and useful boundaries:

1. a QP procedure can upgrade global order to large order in every hidden
   residue field;
2. Pilatte's known dense norm ball is exponentially large to enumerate in
   full; and
3. the direct scalar-to-Jacobi-torus Kummer projection removes `Delta` from
   its Chebyshev orbit.

What it does **not** prove is that the certified power source has no factor
signal outside the listed short screens. Replace that exclusivity claim by a
decoder-specific statement, define or restrict the Chebyshev index, freeze a
new version, and repeat both reviews.
