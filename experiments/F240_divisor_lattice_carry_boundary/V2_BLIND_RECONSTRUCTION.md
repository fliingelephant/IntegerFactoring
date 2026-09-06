# F240 V2 blind end-to-end reconstruction

**Verdict:** PASS.

**Authenticated statement SHA-256:**
`d74ea1c31f24a59b643dc38d69326be553bc3944ef80cee4f72a7a2e607e9914`.

This reconstruction uses the declared round-half-up convention.  Let

\[
N=pq,\qquad p<q,
\]

where `p` and `q` are distinct odd primes.  Put

\[
n=\lceil\log _2(N+1)\rceil,\qquad M=N-1,
\qquad H_B=M/B
\]

for every positive divisor `B` of `M`.

## 1. Generalized centered-carry identity

Fix an integer `u>=1`.  Define

\[
a=\left\lfloor {up\over B}+{1\over2}\right\rfloor,
\qquad
b=\left\lfloor {uq\over B}+{1\over2}\right\rfloor,
\]

and

\[
x=up-aB,\qquad y=uq-bB.
\]

For any real `z` and `r=floor(z+1/2)`, one has

\[
r-\tfrac12\le z<r+\tfrac12.
\]

Applying this to `up/B` and `uq/B` gives

\[
-{B\over2}\le x,y<{B\over2}.
\tag{1.1}
\]

This also records the half-tie convention exactly.  If
`up/B=k+1/2`, the selected center is `a=k+1`, and the residue is
`x=-B/2`.  Thus the lower endpoint is included and the upper endpoint is
excluded.

Expand the product of the residues:

\[
\begin{aligned}
xy-u^2
&=(up-aB)(uq-bB)-u^2\\
&=u^2(N-1)-uB(aq+bp)+abB^2\\
&=B\bigl(u^2H_B-u(aq+bp)+abB\bigr).
\end{aligned}
\tag{1.2}
\]

Hence

\[
c={xy-u^2\over B}
\tag{1.3}
\]

is an integer.  If

\[
T=aq+bp,
\tag{1.4}
\]

then (1.2) gives the public carry formula

\[
T={u^2H_B+abB-c\over u}.
\tag{1.5}
\]

In particular, the quotient on the right is an integer for a true tuple.
Direct substitution now gives

\[
bp^2-Tp+aN
=bp^2-(aq+bp)p+apq=0.
\]

Thus `p` is a root of

\[
bX^2-TX+aN=0.
\tag{1.6}
\]

Its discriminant is

\[
\begin{aligned}
T^2-4abN
&=(aq+bp)^2-4abpq\\
&=(aq-bp)^2.
\end{aligned}
\tag{1.7}
\]

This proves all algebraic identities and the perfect-square property.

### Safe direct decoder

A public tuple is checked as follows.

1. Check `B>0`, `B | M`, `u>=1`, `a,b>=0`, and `(a,b)!=(0,0)`.
2. Compute the numerator in (1.5).  Reject unless it is divisible by `u`.
   Set `T` to the resulting integer.
3. If `b>0`, compute
   \(\Delta=T^2-4abN\).  Reject unless `Delta` is nonnegative and is an
   integer square.  For both signs, test whether
   \[
   X={T\mathbin\pm\sqrt\Delta\over2b}
   \]
   is an integer.  Return it only if `1<X<N` and `X | N`.
4. If `b=0`, the nondegeneracy gate gives `a>0`.  Reject if `T=0`.
   Otherwise test `X=aN/T`, again requiring integrality, `1<X<N`, and
   `X | N`.

Every returned value is therefore a verified proper divisor of `N`, even
when the guessed tuple is false.  For a true tuple, `a,b>=0` follows at once
from the positive arguments of the two floor functions.  Moreover,

\[
b=0\quad\Longrightarrow\quad {uq\over B}<\tfrac12
\quad\Longrightarrow\quad {up\over B}<\tfrac12
\quad\Longrightarrow\quad a=0.
\tag{1.8}
\]

Consequently every true tuple that survives `(a,b)!=(0,0)` has `b>0`.
Equations (1.6) and (1.7) then ensure that the quadratic branch enumerates
`p`.

The excluded endpoint is genuine.  At `B=M` and `u=1`, both `p` and `q`
are less than `M/2`.  Indeed,

\[
M-2q=q(p-2)-1>0,
\qquad
M-2p=p(q-2)-1>0.
\]

Thus

\[
a=b=0,\qquad x=p,\qquad y=q,
\qquad c={pq-1\over M}=1,
\qquad T=0.
\tag{1.9}
\]

Equation (1.6) is then the zero polynomial.  It contains no factor
information, so the nondegeneracy gate is necessary.

The remaining endpoint cases are safe.

- If a true tuple has `a=0<b`, then `T=bp`, and (1.6) is
  \[
  bX(X-p)=0.
  \]
  Its roots are `0` and `p`; the proper-factor check selects `p`.
- A true nondegenerate tuple cannot have `b=0`, by (1.8).  The linear branch
  is still needed to make arbitrary guessed banks safe.
- Zero residues cause no loss of validity.  At `B=1`, specifically,
  \[
  a=up,\quad b=uq,\quad x=y=0,\quad T=2uN,
  \]
  and (1.6) becomes
  \[
  uq(X-p)^2=0.
  \tag{1.10}
  \]
  The root `p` is repeated, and the decoder still returns it.

### Carry-size implications

From (1.1), `|y|<=B/2`.  Therefore, for `X>=0`,

\[
|x|\le X
\quad\Longrightarrow\quad
|c|={|xy-u^2|\over B}
\le {X\over2}+{u^2\over B}.
\tag{1.11}
\]

Conversely, let `C>=0` and suppose `|c|<=C`.  The carry identity gives

\[
|xy|=|u^2+cB|\le u^2+CB.
\]

If either residue is zero, the desired result is immediate.  Otherwise,
with `r=min(|x|,|y|)`, one has `r^2<=|xy|`.  Hence

\[
|c|\le C
\quad\Longrightarrow\quad
\min(|x|,|y|)\le\sqrt{u^2+CB}.
\tag{1.12}
\]

This is only a square-root-scale bound.  When `B` has exponentially large
numerical value in the input bit length, the right side can also have
exponentially large numerical value.  A short carry alone therefore does
not place a centered residue in a numerical-quasipolynomial window.

## 2. The guaranteed zero-carry divisor

Define

\[
d=\gcd(p-1,q-1),\qquad
s_p={p-1\over d},\qquad s_q={q-1\over d}.
\]

Since

\[
M=pq-1=(p-1)(q-1)+(p-1)+(q-1)
=d\bigl(ds_ps_q+s_p+s_q\bigr),
\tag{2.1}
\]

`d` is a divisor of `M`.  Both primes are odd, so `d` is even and `d>=2`.

Take `B=d` and `u=1`.  If `d>=4`, then

\[
{p\over d}=s_p+{1\over d},\qquad
{q\over d}=s_q+{1\over d},
\]

where `0<1/d<1/2`.  Thus round-half-up gives

\[
a=s_p,qquad b=s_q,qquad x=y=1,qquad c=0.
\tag{2.2}
\]

If `d=2`, both fractional parts equal exactly `1/2`.  The declared tie
rule moves each center upward:

\[
a=s_p+1,qquad b=s_q+1,qquad x=y=-1,qquad c=0.
\tag{2.3}
\]

This proves that the divisor lattice contains a carry-zero radix.  It also
shows exactly what remains hidden there: its center indices are the two
P205 residuals, with the forced additive offset `+1` only when `d=2`.
The equality `c=0` does not identify which public divisor is `d` and does
not bound either residual.

For every real `R>=1`, positivity of `d` gives the exact equivalence

\[
s_p\le R
\quad\Longleftrightarrow\quad
d\ge {p-1\over R},
\tag{2.4}
\]

and the same statement holds with `q`.  Also `d<=p-1`.  Therefore the
contrapositive is exact:

> If no divisor of `M` lies in
> \(\bigl[(p-1)/R,\,p-1\bigr]\), then `s_p>R`.

The converse test cannot use an arbitrary divisor from this window.  Such
a divisor need not equal `d`.  For example, take `p=7`, `q=11`, and `R=2`.
Then `M=76`, `d=2`, and `s_p=3>2`, while the divisor `4` lies in the window
`[3,6]`.  Finally, (2.4) controls only the numerical magnitude of a
residual.  It gives no conclusion about the sizes of its prime factors or
about smoothness.

## 3. Exact saturation in the divisor-only multiplicative grammar

Consider a word

\[
W=\prod_{j=1}^{J}B_j^{e_j},
\qquad B_j\mid M,\quad e_j\ge0,
\tag{3.1}
\]

and allow gcd, lcm, and exact integer division of such words.  Every prime
in any resulting integer divides `M`.  This follows directly from prime
valuations: a product adds valuations, gcd takes their minimum, lcm takes
their maximum, and exact division can only decrease them.

For `i` equal to `p` or `q`, define

\[
s_i^{\perp M}
=\prod_{\substack{\ell^e\parallel s_i\\ \ell\nmid M}}\ell^e.
\tag{3.2}
\]

If `ell` does not divide `M`, then `v_ell(W)=0`.  Thus every full primary
part `ell^e || s_i` outside the support of `M` survives division by
`gcd(s_i,W)`.  Consequently

\[
s_i^{\perp M}\mid {s_i\over\gcd(s_i,W)}.
\tag{3.3}
\]

This lower bound is attained by one public word, simultaneously for both
residuals:

\[
W_*=M^n.
\tag{3.4}
\]

Indeed, the definition of `n` implies `N<2^n`, and `s_i<i<N`.  Hence, for
every prime `ell`,

\[
v_\ell(s_i)<n.
\tag{3.5}
\]

For each `ell | M`,

\[
v_\ell(W_*)=n v_\ell(M)\ge n>v_\ell(s_i).
\]

For each `ell` outside `M`, the valuation in `W_*` is zero.  The gcd with
`W_*` therefore removes exactly the `M`-supported primary parts of `s_i`,
and

\[
{s_i\over\gcd(s_i,W_*)}=s_i^{\perp M}.
\tag{3.6}
\]

Since `M<N<2^n`, the binary length of `M^n` is at most `n^2`.  The word can
be produced by ordinary exponentiation from public `M`; it does not require
the factorization of `K=M/2` or even the factorization of `M`.  Thus no
enumeration of divisors and no multiplicative reuse of them can improve
the residual beyond (3.6).  Such operations can increase exponents on
primes already in `M`, but they cannot add the missing prime support.

The same valuation proof gives the baseline extension.  If a public
positive integer `L` is allowed and all permitted word primes lie in the
support of `ML`, define the exterior part using primes not dividing `ML`.
Then every word leaves that exterior part, while

\[
(ML)^n
\]

absorbs every primary part of `s_i` whose prime divides `ML`.  Its bit
length is `O(n(log M+log L))`; no polynomial-size claim is implied for an
arbitrarily large `L`.  For an integer `R>=1`, choosing `L=R!` absorbs all
primary parts on primes at most `R`.  The parts that remain outside the
combined support are precisely those on primes `ell>R` for which
`ell` does not divide `M`.  Divisor-lattice multiplication cannot affect
them.

This proves an optimum only for the stated grammar.  Addition,
subtraction, divisor differences, shifted divisors, modular residues, and
the carry child `u^2+cB` are outside it.

## 4. The additive-selector boundary

The carry equation itself is

\[
xy=u^2+cB.
\tag{4.1}
\]

If the center `a` and signed residue `x` are recovered, their defining
identity gives

\[
aB+x-u=up-u=u(p-1)>0.
\tag{4.2}
\]

Because `p-1=ds_p`, the public integer in (4.2) is divisible by all of
`s_p`.  Placing it in a P205 word absorbs that residual completely.
Likewise,

\[
bB+y-u=u(q-1)>0
\tag{4.3}
\]

absorbs all of `s_q`.  Therefore an explicit candidate bank that is
guaranteed to contain one correct pair `(a,x)` or `(b,y)` gives a valid
P205 word: include the positive integer from every candidate pair, so the
correct one occurs among its factors.

There is a separate direct route.  For each public `B,u`, combine candidate
banks for `a`, `b`, and `c`, and apply the decoder from Section 1.  A fixed
product of quasipolynomial bank cardinalities is quasipolynomial.  If the
correct tuple has `(a,b)!=(0,0)`, its combination returns `p`; false and
degenerate combinations are harmless.  The bit cost of either bank claim
is polynomial in the total explicit encoding length.  Thus a running-time
claim also requires the bank entries, not only their count, to have a
quasipolynomial total encoding length.

Factoring the right side of (4.1) does not, by itself, select `x`.  When
`u^2+cB` is nonzero, `x` is one signed divisor of that integer, but a
factored integer can have super-quasipolynomially many divisors in its bit
length.  To see this without an asymptotic divisor theorem, let `z_k` be the
product of the first `k` primes.  Its complete factorization is explicit
and it has `2^k` positive divisors.  Bertrand's postulate gives
`p_j<=2^j` for the `j`-th prime, so the bit length of `z_k` is `O(k^2)`.
For every fixed `C,r`,

\[
2^k>2^{C(\log_2(\operatorname{bits}(z_k)+1))^r}
\]

for all sufficiently large `k`.  Exhaustive divisor enumeration therefore
does not have a numerical-quasipolynomial bound merely because the input is
factored.

If `u^2+cB=0`, the public equation says `xy=0`.  This case can be split into
the two branches `x=0` and `y=0`; when the corresponding center is
available, (4.2) or (4.3), or direct division of `aB=up` or `bB=uq`, handles
that branch.  The case does not justify enumerating divisors of zero and
does not reveal the missing center by itself.

The divisor-count example is an enumeration obstruction, not a hardness
result.  A semiprime-specific rule could still select the correct signed
divisor of (4.1) without listing all divisors.

Finally, suppose literally that `u=a=1` and `|p-B|<=X`.  Then

\[
x=p-B.
\]

Scanning all signed offsets `z` with `|z|<=X` and testing `B+z` for proper
range and exact divisibility already finds `p`.  If `X` is numerical
quasipolynomial in `n`, this is a quasipolynomial direct factor bank.  It
does not need a carry computation or a P205 residual argument.  The open
case must instead obtain useful additive support without already scanning
a hidden factor-sized offset.

## 5. Exact scope of the result

The reconstruction proves the following boundary.

1. Every divisor radix `B | N-1` has the centered-carry identities in
   Section 1, with a safe direct decoder after the exact nondegeneracy gate.
2. The hidden divisor `d=gcd(p-1,q-1)` is a carry-zero radix.  Its centers
   are exactly the P205 residuals, apart from the forced `+1` at the unique
   half-tie case `d=2`.
3. In the divisor-only multiplicative grammar, `(N-1)^n` is the exact
   support-saturated optimum and has `O(n^2)` bits.
4. The remaining possible gain is additive.  It requires a rule that
   selects a correct center and signed residue, selects both centers and a
   usable carry at a nondegenerate tuple, selects the correct signed divisor
   of the carry child without exhaustive enumeration, or proves an
   all-input or inverse-quasipolynomial additive-support law.

This is a theorem for distinct odd semiprimes under a grant of the complete
factorization of `(N-1)/2`.  It is not an all-input factoring algorithm.
It supplies no quasipolynomial selector, no centered-carry distribution
law, no residual-smoothness law, and no lower bound against algorithms
outside the narrow multiplicative grammar.  These limitations prevent the
result from resolving the root factoring prompt, but they do not affect the
validity or sharpness of the stated boundary.
