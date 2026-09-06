# Proof of the F228 quotient/carry APR-source candidate

## 1. Size and recurrence

Since `B=2^floor(n/2)` and `N<2^n`,

\[
0\le Q_u<{uN\over B}<u2^{\lceil n/2\rceil}.
\]

Adding a shift of magnitude at most `C(n)` gives

\[
\operatorname{bits}(A_{u,c})
\le \lceil n/2\rceil+
O(\log(U(n)+C(n)+2)).
\]

The additive term is `(log n)^O(1)=o(n)`.  Hence, for all sufficiently
large `n`, every positive child has at most `2n/3` bits.  Every prime factor
`ell` of a child and its descendant `ell-1` obey the same bound.

There are numerical-QP many `(u,c)` pairs.  The number of prime occurrences
in a complete factorization is at most the sum of the child bit lengths, so
one node produces only numerical-QP many recursive calls.  A recurrence

\[
T(n)\le H(n)T(2n/3)+H(n),
\qquad H(n)=2^{(\log n)^{O(1)}},
\]

has depth `O(log n)`.  The logarithm of the product of its branching factors
is a sum of `O(log n)` polylogarithmic terms and is still
`(log n)^O(1)`.  This proves the recursion-size claim.  It is a cost theorem
conditional on recursive correctness for arbitrary children.

For the carry identity, substitute `N=KB+S` into `uN`:

\[
uN=\left(uK+\left\lfloor{uS\over B}\right\rfloor\right)B
 +\left(uS-B\left\lfloor{uS\over B}\right\rfloor\right).
\]

Uniqueness of Euclidean division proves (4).  If `uS<B`, the floor is zero.

## 2. Direct gcd and common-primary collapse

Because `N` is odd, `B` is a unit modulo `N`.  Multiplying the shifted
quotient by `B` gives

\[
B A_{u,c}=uN-R_u+cB.
\tag{19}
\]

Therefore

\[
\gcd(A_{u,c},N)
=\gcd(BA_{u,c},N)
=\gcd(R_u-cB,N),
\]

which proves (5), including negative defects after taking absolute values
inside a gcd.

Let `d` be odd and divide `N-1`.  Then `B` is a unit modulo `d` and
`N=1 mod d`.  Reducing (19) modulo `d` gives

\[
BA_{u,c}\equiv u-R_u+cB\pmod d.
\]

Taking gcds proves (6).  Every prime divisor `r` of `N` is one modulo
`D_N`; hence their product with multiplicity, namely `N`, is one modulo
`D_N`.  Thus `D_N|N-1`, and (8) follows after taking the odd part.

If a primary certificate says `ell^e|r-1` for every rational prime `r|N`,
then `ell^e|D_N`.  If the certificate was stripped from the factored
exponent `A_{u,c}`, it also has `ell^e|A_{u,c}`.  Equation (8) puts the same
block in `u-R_u+cB`.  This proves the capacity statement.  It does not say
that the defect is an annihilator or that factoring it alone certifies the
block.

## 3. Inverse lift and compatible support

Let `ell|A_{u,c}` pass the gcd screen.  Then `ell` does not divide `N`, and
`B` is a unit modulo `ell`.  Equation (19) gives

\[
uN\equiv R_u-cB=a\pmod\ell.
\]

When `ell` does not divide `u`, division proves (10).  Raising (10) to the
`i`th power proves

\[
N^i\equiv a^iu^{-i}\pmod\ell,
\]

and hence (11).  The case `i=0` is the ordinary convention that both
zeroth powers are one.

Since `q=Np^{-1}`, the condition `p=N^i` gives `q=N^(1-i)`.  At `i=0`,
substitution of `N=a/u` gives (12).  At `i>=1`, it gives

\[
q=(u/a)^{i-1}\pmod\ell,
\]

which is (13).  These implications reverse, so the displayed laws are
equivalences.

The integer in (14) can vanish at `i=1` only when `p=a/u`, which publicly
reveals the factor.  It does not vanish for `i=0`.  For `i>=2`, equality
would give a rational `i`th root of the prime `p`, which is impossible by
prime valuations.  Away from the direct recovery, it is therefore a genuine
hidden nonzero integer.

Independently of (14), every compatible prime divides `N^i-p`.  This is
nonzero for all `i>=0`: it is `1-p` at zero and is positive from `i=1`
onward.  The squarefree product of all such primes divides its absolute
value.  For `i=0` its logarithm is below `n`; for `i>=1`,

\[
0<N^i-p<N^i,
\]

so its binary logarithm is below `ni`.  This proves (15).

## 4. Uniform-shift tail

Fix `Q_u` and a prime `ell`.  Among `W` consecutive integers, a single
residue class modulo `ell` occurs at most `W/ell+1` times.  The condition

\[
\ell\mid Q_u+c
\]

is exactly one such residue class for `c`.  Division by `W` proves (16).
For `K` independent shifts, a union bound gives capture probability at most

\[
K(1/\ell+1/W).
\]

For compatible primes `ell>Y`, this is at most
`K(1/Y+1/W)`.  Weighted linearity of expectation and (15) give (17).
Summing over `0<=i<T` and using

\[
\sum_{i=0}^{T-1}\max(1,i)\le T^2
\]

gives total expected large-prime log mass at most the numerator of (18).
If one exponent captures at least `Delta`, the total is at least `Delta`.
Markov's inequality proves (18).

A sieve enumerates all primes through a numerical-QP cutoff `Y` in
numerical-QP bit complexity.  Enlarging the numerical-QP quantities `Y`
and `W` by a further numerical-QP factor makes the right side of (18) as
small as any fixed inverse-QP target.  This proves the stated dominance
boundary for uniform shifts only.

## 5. Finite-run interpretation

For distinct safe primes `p=2P+1` and `q=2Q+1`, the primes `P,Q` are
distinct.  Therefore

\[
\gcd(p-1,q-1)=2.
\]

The odd common-primary part is exactly one on every searched row.

D01 and D02 counted a trial only after the frozen `omega<=20` divisor cap.
D03 computed the compatible product before applying caps and then reported
the cap-20, cap-40, and cap-64 projections separately.  Its cap-20 column
matches D02 row by row.  The largest observed `omega` was below 40 at all
three scales, so cap 40 equals the no-cap count.  Thus the D02 capped-zero
rows cannot be described as hidden-subset source failures.  No finite count
is used in Sections 1--4.
