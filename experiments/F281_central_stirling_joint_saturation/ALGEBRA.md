# F281-D01 algebra — central Stirling joint saturation

## 1. Exact question

For `s >= 1`, put

\[
 A_s=\left\{\begin{matrix}2s+1\\s\end{matrix}\right\},
 \qquad
 B_s=\left\{\begin{matrix}2s+1\\s-1\end{matrix}\right\}.
\]

F281-D01 tests the following precise conjecture.

> Every prime divisor of `gcd(A_s,B_s)` is at most `2s+1`.

This is a prime-support statement. It does not assert that the gcd divides
`(2s+1)!`, its square-free kernel, or `lcm(1,...,2s+1)`. Those stronger
statements contain valuation claims that do not follow from the question.

## 2. Complete homogeneous form

Let

\[
 H_k(t)=\prod_{j=1}^{k}(1-jt)^{-1}
       =\sum_{d\geq 0}h_d(1,\ldots,k)t^d.
\]

The ordinary generating function for Stirling numbers gives

\[
 \left\{\begin{matrix}n\\k\end{matrix}\right\}
 =h_{n-k}(1,\ldots,k).
\]

Therefore

\[
 A_s=h_{s+1}(1,\ldots,s),
 \qquad
 B_s=h_{s+2}(1,\ldots,s-1).
\]

The last-variable recurrence is

\[
 h_d(1,\ldots,s)=h_d(1,\ldots,s-1)
                  +s h_{d-1}(1,\ldots,s).
\]

It follows that

\[
 h_{s+2}(1,\ldots,s)=B_s+sA_s.
\]

Hence, over any field, the target joint zero is exactly

\[
 \boxed{h_{s+1}(1,\ldots,s)=h_{s+2}(1,\ldots,s)=0.}
\tag{1}
\]

## 3. Complement to adjacent first-kind coefficients

Let `p > 2s+1` be prime. Write

\[
 p=2s+1+2h,
 \qquad h\geq1,
 \qquad r=p-s-1=s+2h.
\]

In `F_p[t]`,

\[
 \prod_{a=1}^{p-1}(1-at)=1-t^{p-1}.
\]

For every degree below `p-1`, complementing the variables and replacing
`p-j` by `-j` gives

\[
 h_d(1,\ldots,s)\equiv e_d(1,\ldots,r)\pmod p.
\tag{2}
\]

Write `c(n,k)` for the unsigned Stirling number of the first kind, so

\[
 x(x+1)\cdots(x+n-1)=\sum_k c(n,k)x^k.
\]

Since

\[
 \prod_{j=1}^{r}(x+j)
   =\sum_{k=0}^{r}c(r+1,k+1)x^k,
\]

equations (1) and (2) give the exact equivalence

\[
 \boxed{
 p\mid A_s,B_s
 \iff
 c(s+2h+1,2h)\equiv c(s+2h+1,2h-1)\equiv0\pmod p.}
\tag{3}
\]

Lane B computes the two coefficients indexed by the polynomial degrees
`2h` and `2h-1` in the rising factorial. If it instead removes the leading
factor `x`, the corresponding degrees are `2h-1` and `2h-2`. The source uses
the direct `c(n,k)` recurrence, so no shifted-degree convention enters its
test.

## 4. A discarded false reparameterization

The target in (1) must not be replaced by

\[
 h_{2h-2}(1,\ldots,s)=h_{2h-1}(1,\ldots,s)=0.
\tag{4}
\]

Equation (4) is false as an equivalent target. For `s=3`, `p=43`, and
`h=18`,

\[
 A_3=301\equiv0\pmod{43},
 \qquad B_3\equiv20\pmod{43},
\]

while

\[
 h_{34}(1,2,3)\equiv13,
 \qquad h_{35}(1,2,3)\equiv36\pmod{43}.
\]

The self-test requires these four residues. This is a negative test against
reintroducing the discarded reduction.

There is a valid norm identity. If `m=(p-1)/2` and `s=m-h`, then, through
degrees below `p-1`,

\[
 H_s(t)H_s(-t)
 =\prod_{i=1}^{h}\left(1-(i-\tfrac12)^2t^2\right)\pmod p.
\tag{5}
\]

Identity (5) does not move the two target degrees `s+1,s+2` to the two
degrees in (4). F281-D01 tests (5), but never uses it to select a candidate.

## 5. Finite differences and the fixed-divisor seam

Put `m=s-1`, `n=2m+3`, and

\[
 P_m(x)=\Delta^m x^{2m+3}.
\]

Then

\[
 P_m(0)=m!B_s,
 \qquad
 P_m(1)-P_m(0)=(m+1)!A_s.
\tag{6}
\]

The centered reflection is

\[
 P_m(-m-x)=(-1)^{m+1}P_m(x).
\tag{7}
\]

For `p>2s+1`, the factorials in (6) are units modulo `p`. Thus a target
joint zero is also equivalent to `P_m(0)=P_m(1)=0 (mod p)`. Reflection adds
the roots `-m` and `-m-1`, but the degree is `m+3`; root counting alone gives
no contradiction.

Define the tail fixed divisor

\[
 \Delta_{n,m}=\gcd_{m\leq k\leq n}
                  k!\left\{\begin{matrix}n\\k\end{matrix}\right\}
\]

and the two-entry scaled gcd

\[
 G_s=\gcd\left(m!B_s,(m+1)!A_s\right).
\]

The divisibility `Delta_{n,m} | G_s` is immediate. A proof that
`G_s/Delta_{n,m}` has no prime above `n` would prove the target conjecture.
No such prefix-to-tail identity is known in this packet.

The stronger empirical guess

\[
 G_s/\Delta_{n,m}\mid 2s
\]

is already false. At `s=73`, the ratio is

\[
 1679=23\cdot73,
\]

which does not divide `146`. The source records this boolean only as a
refuted diagnostic. It also records the weaker large-prime support residual
of the ratio. Neither value is a gate or a proof input.

## 6. Exact certificate semantics

### Lane A

The second-kind recurrence

\[
 S(n,k)=kS(n-1,k)+S(n-1,k-1)
\]

computes exact GMP integers. For each registered `s`, Lane A forms
`g=gcd(A_s,B_s)` and removes every rational prime at most `2s+1` to
exhaustion. If the residual `R` is above one, then

\[
 R\mid A_s,
 \qquad R\mid B_s,
 \qquad \gcd(R,\operatorname{lcm}(1,\ldots,2s+1))=1.
\]

Every prime factor of `R` is therefore above `2s+1`. Factoring `R` is not
needed. The serialized witness is independently replayed with the original
second-kind inclusion-exclusion formula modulo `R`; `s!` and `(s-1)!` are
invertible because of the support gcd.

### Lane B

The exact recurrence

\[
 c(n,k)=c(n-1,k-1)+(n-1)c(n-1,k)
\]

is maintained through degree `2H`. At row `n=s+2h+1`, FLINT tests
`p=2s+2h+1` for primality. The source reduces the two exact coefficients in
(3) modulo `p`. A joint zero is replayed through the original second-kind
inclusion-exclusion formula for `A_s` and `B_s`, not through the complement
identity.

Either lane stops after its first exact counterexample. This bounds witness
output. A completed null search is finite evidence only. It is not a proof of
the conjecture.
