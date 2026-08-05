# F12 elliptic-collision reconstruction

**Status:** self-audited proof-blind reconstruction.  
**Verdict:** every assertion in the corrected bare statement survives, with
the evaluator-to-factoring result explicitly conditional on the hypothesized
polylogarithmic exact evaluator.

## 1. Division-polynomial collision product

Let

`E: y^2=x^3+A x+B`

be nonsingular over a field of characteristic different from 2 and 3.  Use
the standard division polynomials `psi_n`, with `psi_(-n)=-psi_n`, and

`phi_n=x psi_n^2-psi_(n+1)psi_(n-1)`.

The standard addition identity is

`psi_(u+v)psi_(u-v)=psi_(u+1)psi_(u-1)psi_v^2-psi_(v+1)psi_(v-1)psi_u^2`.

For `1<=i<j`, substituting the definition of `phi` and using
`psi_(i-j)=-psi_(j-i)` gives the polynomial identity

`phi_i psi_j^2-phi_j psi_i^2=psi_(i+j)psi_(j-i)`.

It is an identity before evaluation and therefore does not divide by a
possibly vanishing denominator.  Multiplying it over all pairs proves

`C_m=prod_(1<=i<j<=m)(phi_i psi_j^2-phi_j psi_i^2)`

`   =prod_(1<=i<j<=m) psi_(i+j)psi_(j-i)`.

For an affine point `P` of finite order `t`, the projective multiplication
formula gives

`psi_k(P)=0 iff [k]P=O iff t divides k`.

Every factor index on the right lies between 1 and `2m-1`, so a zero factor
implies `t<=2m-1`.  Conversely:

* if `t<=m-1`, choose `(i,j)=(1,t+1)`, whose difference is `t`;
* if `m<=t<=2m-1`, choose positive `i<j<=m` with `i+j=t`: take
  `(1,t-1)` when `t<=m+1`, and `(t-m,m)` otherwise.

The small cases `t=1,2` are already covered by differences (an affine point
cannot in fact have order one).  Hence, for `m>=3`,

`C_m(P)=0 iff t<=2m-1`.

Likewise all denominator polynomials `psi_1(P),...,psi_m(P)` are nonzero iff
no positive multiple of `t` occurs at most `m`, equivalently iff `t>m`.

## 2. Universal Hasse obstruction at `N=10403`, `m=101`

Let `N=101*103` and let a global short Weierstrass curve have discriminant a
unit modulo `N`.  Any global affine point reduces to affine points over both
fields.  Hasse gives the integer bounds

`#E(F_101)<=floor(102+2 sqrt(101))=122`,

`#E(F_103)<=floor(104+2 sqrt(103))=124`.

The order of either reduced point is at most the corresponding group order,
and both bounds are at most `2m-1=201`.  The criterion above therefore forces

`C_101(P)=0 mod 101` and `C_101(P)=0 mod 103`

for every such curve and point.  Thus the global value is zero modulo `N` and
its gcd with `N` is `N`, never a proper factor.  This conclusion is universal
for the stated fixed `N,m`, not a heuristic about random curves.

For a candidate curve with integer discriminant `Delta`, first compute
`g=gcd(Delta,N)`.  A value `1<g<N` is already a valid factor.  A value `g=N`
only says the curve is bad at every prime component and supplies no split; it
must be retried.  Only `g=1` enters the good-reduction argument.  No claim of a
proper factor is made from a full gcd.

## 3. Denominator-clean explicit certificate

For

`E: y^2=x^3+x+5`, `P=(5461,5889) mod 10403`,

the global curve equation holds and

`Delta=-16(4+27*25)=-10864`, `gcd(Delta,10403)=1`.

The exact retained certificate is:

| Field | Reduced point | `#E(F_p)` | Point order `t` | First lexicographic collision | Colliding points |
| --- | --- | ---: | ---: | --- | --- |
| `F_101` | `(7,31)` | 112 | 112 | `(11,101)` | `(69,38)` and `(69,63)` |
| `F_103` | `(2,18)` | 106 | 106 | `(5,101)` | `(40,44)` and `(40,59)` |

In each row the two `y`-coordinates are negatives, so the equality of
`x`-coordinates is `[i]P=-[j]P`; the sums `i+j` are respectively 112 and 106.
The point orders exceed `m=101`, so every `psi_1(P),...,psi_101(P)` is
nonzero.  The collision factor is instead `psi_112(P)` or `psi_106(P)`, making
the certificate denominator-clean.  There are respectively 45 and 48
colliding pairs in the full range; the stated pairs are the first in `(i,j)`
lexicographic order.

The primary program used repeated exact group addition and direct point
counting.  A separate source used double-and-add, checked order minimality and
the absence of every earlier collision, and passed.  Exact values are in
`outputs/finite_certificate.json` and `outputs/audit.json`.

## 4. Vandermonde product and exact order test

For any commutative ring,

`D_m(a)=prod_(0<=i<j<m)(a^i-a^j)`.

Factoring `a^i` from the `(i,j)` term gives total exponent

`sum_(i=0)^(m-2) i(m-1-i)=m(m-1)(m-2)/6=binom(m,3)`.

For a fixed difference `d=j-i`, there are `m-d` pairs.  Therefore

`D_m(a)=a^binom(m,3) S_m(a)`,

`S_m(a)=prod_(d=1)^(m-1)(1-a^d)^(m-d)`.

If `a` is a unit of order `t` in `F_l`, a factor `1-a^d` vanishes exactly
when `t` divides `d`.  Such a `d` occurs in `1,...,m-1` exactly when
`t<=m-1`.  Hence

`S_m(a)=0 in F_l iff t<=m-1`.

## 5. Conditional evaluator-to-factoring theorem

Assume a uniform exact algorithm

`Eval(N,a,m)=S_m(a) mod N`

with worst-case bit cost `T(log N+log m)`, where `T` is polynomial.  Then
complete classical Las Vegas polynomial-time factoring follows.

### Preprocessing and the decisive root

At every recursive node, remove powers of two, use a deterministic
polynomial-time primality test for prime leaves, and detect perfect powers by
exact integer `k`th roots for `2<=k<=bitlength(N)`.  If `N=b^e`, recursively
factor `b` and multiply all resulting exponents by `e`.  These are exact
polynomial-bit operations.

It remains to split an odd composite `N` that is not a perfect power.  Write
its unknown factorization with multiplicity as

`N=prod_i p_i^(e_i)`, `s=sum_i e_i`,

and let `p_min<p_max` be its smallest and largest distinct prime factors.  The
multiset of `s` prime factors has geometric mean `N^(1/s)`.  It is at least
`p_min` and strictly below `p_max`, because the factors are not all equal.
Thus

`p_min <= m_s=floor(N^(1/s)) < p_max`.

Although `s` is unknown, `2<=s<=bitlength(N)`, so scan every
`k=2,...,bitlength(N)` with the exactly computed
`m_k=floor(N^(1/k))`.  The decisive `k=s` is included.

### One randomized trial

Choose `a` uniformly from `0,...,N-1`, using rejection sampling from random
bits.  First compute `gcd(a,N)`: return it if proper, retry if it is `N`, and
otherwise `a` is a unit modulo every prime factor.  For every scanned `k`,
compute

`u_k=Eval(N,a,m_k)` and `g_k=gcd(u_k,N)`,

returning any proper gcd.

At `k=s`, Fermat's theorem gives

`ord_(p_min)(a)<=p_min-1<=m_s-1`,

so `S_(m_s)(a)=0 mod p_min`.  If the residue of `a` modulo `p_max` is
primitive, then

`ord_(p_max)(a)=p_max-1>=m_s`,

so `S_(m_s)(a)!=0 mod p_max`.  The gcd is consequently proper.  This remains
true with repeated prime powers: the gcd need only contain one positive power
of `p_min`, while it contains no `p_max`.

If a primitive residue modulo `p_max` happens to be divisible by another
prime factor of `N`, the initial gcd already succeeds.  Thus every sampled
integer whose reduction modulo `p_max` is primitive is a successful trial.

### Elementary probability bound

For an integer `t`, list its `r` distinct prime divisors increasingly as
`q_1,...,q_r`.  Since `q_i>=i+1` and `x/(x-1)` decreases,

`t/phi(t)=prod_(q|t) q/(q-1) <= prod_(i=1)^r (i+1)/i=r+1`.

Also `t>=2^r`, so `r<=log_2 t`.  Therefore

`phi(t)/t >= 1/(1+log_2 t)`.

With `t=p_max-1`, uniform reduction modulo `p_max` makes the success
probability at least

`phi(p_max-1)/p_max >= 1/(2(1+bitlength(N)))`.

Independent retries therefore terminate almost surely in expected `O(n)`
trials, using expected polynomially many random bits.  Every returned divisor
is checked by exact gcd and division, so the algorithm is Las Vegas.

### Bit complexity and complete recursion

One trial makes `O(n)` evaluator calls on inputs of `O(n)` bits, plus exact
integer roots, gcds, sampling, and verification of polynomial bit cost.  With
`O(n)` expected trials, one proper split costs

`O(n^2 T(O(n)) + poly(n))`.

Recursing on the two verified factors preserves multiplicities even when they
are not coprime.  The binary split tree has at most `O(n)` internal nodes,
because the number of prime leaves counted with multiplicity is at most
`log_2 N`.  Perfect-power compression adds only polynomial preprocessing and
does not add evaluator-based split nodes.  A coarse complete-factorization
bound is therefore

`O(n^3 T(O(n)) + poly(n))`.

Prime leaves are proved prime, all factor products and exponents are verified,
and the argument covers primes, evens, prime powers, repeated factors, and
arbitrary composites.

## 6. What is not supplied

No polylogarithmic evaluator is constructed here.  The direct recurrence

`P_d=P_(d-1)(1-a^d)`, `S_(d+1)=S_d P_d`

with powers updated successively computes `S_m` in `O(m)` iterations.  That is
not polynomial in `log m` when `m` is large, but it is also not a lower bound
against another exact algorithm.

Likewise

`S_m(a)=(-1)^binom(m,2) prod_(e=1)^(m-1) Phi_e(a)^E_e`,

where, for `h=floor((m-1)/e)`,

`E_e=h m-e h(h+1)/2`,

is only a cyclotomic identity.  Displaying it does not evaluate its `m-1`
factors in time polynomial in `log m`.  The conditional factoring theorem is
therefore exact, but the required evaluator remains an explicit missing
algorithm.

## Scope

The elliptic result is an unconditional identity plus a fixed-input universal
obstruction and a checked finite certificate.  The Vandermonde/order result is
unconditional.  The factoring result is a conditional reduction from a
uniform exact polylogarithmic evaluator; it is not an unconditional factoring
algorithm and does not infer such an evaluator from the linear recurrence or
the cyclotomic display.

