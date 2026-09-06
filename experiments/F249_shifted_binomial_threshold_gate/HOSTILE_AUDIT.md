# F249 hostile audit

## Verdict

**PASS.**  I independently reconstructed the range bounds, the Lucas/CRT
congruence for arbitrary positive `r`, the exact gcd threshold, the floor-safe
success probability, the unique recurrence singularity, the central-binomial
complement, both product-cancellation descriptions, and the rank-one carry
relation.  I found no promotion-blocking defect.

The complexity conclusions also survive at their stated scope.  They are
boundaries for named representations.  They are not a lower bound against a
new succinct coefficient evaluator, and they are not a factoring algorithm.
I wrote only this audit.  I did not change a frozen input or a durable ledger.

## Frozen-input authentication

I recomputed all five requested SHA-256 digests before reviewing content.  The
expected and observed values agree exactly:

| File | SHA-256 |
|---|---|
| `STATEMENT.md` | `2b6594484dcb394b58126398d9944ab3e6aa18f8bc2d62e462dcc6e3c18db825` |
| `PROOF.md` | `8938898cf8118ddcee1b4831468c7f6a62a4928c35688abe61ace52ca8bd9865` |
| `SELF_AUDIT.md` | `8c87a7a24d47ae874dba6398c6eb621e93b7aebb137379ee1d00d329153a4634` |
| `PROVENANCE.md` | `21ae6042acf6a9a4c84838e8f3f972069c956d4a011c91fb57c4ef550e115f85` |
| `MANIFEST.md` | `71d68b618d42a069c3eccd262e312659a4b5015ed928a3d293ff0311d4810a81` |

The requested names `SELF` and `MANIFEST` correspond to `SELF_AUDIT.md` and
`MANIFEST.md` in the packet.

## 1. Public ranges and floor endpoints

The promise gives

\[
p^2<pq<2p^2,
\]

so

\[
p\le B=\lfloor\sqrt N\rfloor<\sqrt2p<2p.
\]

Also `B<q`, because `sqrt(pq)<q`.  Hence

\[
0\le s=B-p<p,\qquad H=\lfloor B/2\rfloor<p.
\]

For every integer `B>=3`,

\[
B/\sqrt2>\lceil B/2\rceil.
\]

The odd case `B=2k+1` reduces after squaring to `2k^2>1`, including
the endpoint `B=3`.  Therefore

\[
p>\lceil B/2\rceil,
\qquad
s=B-p<\lfloor B/2\rfloor=H.
\]

Distinct odd primes give `N>=15`, so `B>=3` and `H>=1`.  Thus all strict
endpoints in the statement are valid.  In particular, `c=H` is always on
the successful side of the threshold.

## 2. Lucas/CRT law for arbitrary `r`

Fix `r>=1` and `1<=c<=H`.  Modulo `q`, write

\[
rN+c-1=q(rp)+(c-1).
\]

Because `c-1<B<q` and the lower index `B` is one base-`q` digit, Lucas's
theorem gives

\[
C_{r,c}\equiv\binom{c-1}{B}=0\pmod q.
\]

Modulo `p`, use `B=p+s` and

\[
rN+c-1=p(rq)+(c-1),
\qquad 0\le s<p,quad c-1<p.
\]

Recursive Lucas expansion is important when `rq>=p`.  The low digits give
`binom(c-1,s)`.  The next lower digit is one, and all later lower digits are
zero, so the remaining Lucas product is exactly `rq mod p`.  Hence

\[
C_{r,c}\equiv rq\binom{c-1}{s}\pmod p.
\]

The integer on the right is zero modulo `q`.  CRT therefore proves the exact
packet congruence

\[
C_{r,c}\equiv rq\binom{c-1}{s}\pmod{pq}
\]

for every positive `r`, with no size restriction on `r`.

If `c<=s`, the local binomial is zero by convention and `N|C_{r,c}`.  If
`c>s`, then

\[
0\le s\le c-1<p,
\]

so `binom(c-1,s)` is nonzero modulo `p`.  After the declared
`gcd(r,N)=1` screen, the residue is nonzero modulo `p` and zero modulo `q`.
This reconstructs the exact gcd law.  Since `H>s`, the endpoint returns `q`.

The equivalence claim is correctly limited to the promised gcd-output
function.  That function returns `q`, so it factors `N`; conversely, a
factorization identifies `q`.  The packet does not claim that a factorization
fast-forwards the complete residue `C_{1,H} mod N`.

## 3. Exact Las Vegas accounting

Exactly `H-s` shifts in `{1,...,H}` satisfy `c>s`.  Thus the success
probability is `(H-s)/H`.

For the lower bound, `sqrt(2)<3/2` and `B<sqrt(2)p` give

\[
p>2B/3,\qquad 3s<B.
\]

If `B=2H`, then `3s<2H`.  If `B=2H+1`, integrality gives `3s<=2H`.
In both cases `s<=2H/3`, so the probability is at least `1/3`.  Independent
repetition therefore has expected cost at most three oracle calls.

The exceptional case is complete.  If `s=0`, then `B=p`, so the public gcd
`gcd(N,B)` already factors `N`; all sampled shifts also return `q`.  The
packet does not apply its internal-edge product theorem to this case.

## 4. Recurrence and its unique singular edge

The adjacent-binomial identity gives, over the integers,

\[
(rN+c-B)C_{r,c+1}=(rN+c)C_{r,c}.
\]

For `1<=c<=H-1`, `c<p`, hence `gcd(N,rN+c)=1`.  For the denominator,

\[
\gcd(N,rN+c-B)=\gcd(N,B-c).
\]

Here `0<B-c<B<q` and `B-c<2p`.  A nontrivial gcd is therefore possible
only when `B-c=p`, or `c=s`.  If `s>=1`, then `s<H` places this edge inside
the recurrence range, and

\[
rN+s-B=rN-p=p(rq-1)
\]

has gcd exactly `p` with `N`, since `rq-1=-1 mod q`.  If `s=0`, the edge is
`c=0` and the elementary `gcd(N,B)` exit applies.  No other edge is omitted.

## 5. Central-binomial complement

The denominator `H!` in `K_B=binom(B,H)` is a unit modulo `N`.  Its
numerator interval is

\[
B-H+1,\ldots,B.
\]

It contains `p=B-s` because `s<=H-1`.  It contains `p` only once because
`B<2p`, and it contains no multiple of `q` because `B<q`.  Therefore

\[
\gcd(N,K_B)=p.
\]

Together with the endpoint law, this gives

\[
\gcd(N,C_{1,H})=q=N/\gcd(N,K_B).
\]

For odd `B=2H+1`, the colloquial interval `H+1,...,B` has one more term
than the exact numerator interval `H+2,...,B`.  The range proof gives
`H+1<p`, so this term is a unit modulo `N`.  The packet correctly claims
equal factor-bearing gcds, not equality of the two integer products.

## 6. Denominator product and hidden cancellation

For `s>=1`, reduction modulo `N` and the substitution `j=B-c` give

\[
D_r\equiv(-1)^{H-1}
\prod_{j=B-H+1}^{B-1}j\pmod N.
\]

The interval contains `p=B-s`: `s>=1` gives the upper endpoint and
`s<=H-1` gives the lower endpoint.  It contains no second multiple of `p`
and no multiple of `q`.  Therefore `gcd(N,D_r)=p` exactly.

The defining quotient has the same obstruction.  Since `p<=B<2p` and
`B<q`,

\[
B!=pU
\]

with `U` a unit modulo `N`.  In

\[
P_{r,c}=\prod_{j=1}^{B}(rN+c-j),
\]

the index `j=c` contributes `rN`.  After removing it, another zero modulo
`p` can occur only at `j=c+p`; it is present exactly when `c+p<=B`, or
`c<=s`.  A second zero modulo `q` is impossible because `B<q`.  Thus the
remaining product is a unit exactly for `c>s`, and has the stated extra
`p`-factor exactly for `c<=s`.  Exact integer division by `pU` cancels a
hidden factor, while modular inversion of `B!` is unavailable.

The recurrence denominator product is also

\[
\frac{(B-1)!}{(B-H)!}.
\]

Its lower factorial is a unit because `B-H=ceil(B/2)<p`.  This confirms
that recurrence fast-forward has reproduced the upper-half factorial gate.

## 7. Multiplier and rank-one checks

The Lucas/CRT formula directly gives

\[
C_{r,c}\equiv rC_{1,c}\pmod N.
\]

After the gcd screen, `r` is a public unit.  The threshold and singular edge
are independent of `r`.

I also reconstructed the integrality and the congruence behind the carry
claim.  Put

\[
A_r=(-1)^B\binom{rN-1}{B}.
\]

Modulo `q`, Lucas gives `A_r=1`.  Modulo `p`, recursive Lucas gives

\[
\binom{rN-1}{B}
\equiv \binom{p-1}{s}\binom{rq-1}{1}
\equiv(-1)^s(rq-1)\pmod p.
\]

Because `p` is odd and `B=p+s`, multiplication by `(-1)^B` gives
`A_r=1-rq mod p`.  The integer `1-rq` is also `1 mod q`, so CRT proves

\[
A_r\equiv1-rq\pmod N.
\]

Consequently `h_r=(A_r-(1-rq))/N` is an integer.  From

\[
A_r-1=Nh_r-rq
\]

and the invertibility of odd `N` modulo `2^t`, one obtains

\[
z_{r,t}\equiv h_r-rp^{-1}\pmod{2^t}.
\]

Subtracting `r` times the `r=1` equation yields exactly

\[
h_r-rh_1\equiv z_{r,t}-rz_{1,t}\pmod{2^t}.
\]

Thus the asserted modular family has one hidden coordinate `p^{-1}`.  This
does not claim that exact integer carries are freely available; the packet
explicitly leaves their evaluation or biased sampling open.

## 8. Named algorithm and literature scopes

I checked the two literature-dependent boundaries against primary papers.

- Bostan, Gaudry, and Schost, *Linear Recurrences with Polynomial
  Coefficients and Application to Integer Factorization and Cartier--Manin
  Operator*, gives a baby-step/giant-step selected-term cost quasi-linear in
  the square root of the index.  Its theorem is over a commutative ring under
  explicit unit assumptions for the small interpolation integers.  This
  supports the packet's `H^(1/2+o(1))` named-method scale; it does not supply
  a polylogarithmic-in-`H` route through the factor-bearing rational
  denominator.

- Bostan, Christol, and Dumas, *Fast Computation of the Nth Term of an
  Algebraic Series over a Finite Prime Field*, arXiv:1602.00545, assumes a
  known prime field `F_p`.  It obtains logarithmic dependence on the remote
  index with preprocessing whose cost grows polynomially, and in the final
  algorithm quasi-linearly, with the characteristic.  Its construction uses
  base-`p` section operators and prime-field Frobenius.  It therefore does not
  transfer as stated to `Z/NZ`, whose characteristic is composite, or to a
  hidden field `F_p` at numerical-QP cost when `p=2^Theta(log N)`.

The algebraic-series identities themselves are exact:

\[
K_{2H}=\binom{2H}{H}=[x^H](1-4x)^{-1/2},
\]

and

\[
K_{2H+1}=\frac{2H+1}{H+1}\binom{2H}{H}.
\]

Here `H+1<p`; the numerator `2H+1=B` can be a nonunit only in the already
screened branch `B=p`.  On the unresolved branch the multiplier is a unit.
The recurrence

\[
(k+1)a_{k+1}=2(2k+1)a_k
\]

has unit denominators through `k=H-1`.  It has one `p`-bearing numerator at
`k=(p-1)/2` and no `q`-bearing numerator.  This is the same gate in a new
representation.

Finally, literal Vandermonde uses `H+1=Theta(sqrt N)` terms.  Exact CRT
reconstruction from auxiliary prime fields needs `Theta(H)` modulus bits
because the central coefficient has `Theta(H)` bits.  Residues modulo a
coprime auxiliary product smaller than the coefficient do not determine its
residue modulo `N`.  These observations validate the packet's route-specific
boundaries without implying a general circuit lower bound.

## Scope conclusion

F249 supplies a correct constant-density shifted factor oracle *conditional
on* remote coefficient evaluation.  Its deterministic endpoint is already
the complementary central-binomial factor gate.  The unresolved task is the
same one the packet states: find a numerical-QP evaluator or divisibility test
that avoids materializing the factor-bearing product.  No claim in the frozen
packet exceeds that scope.
