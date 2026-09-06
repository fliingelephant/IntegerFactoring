# F222 V2 self-audit

## Verdict

The V2 proof passes this internal audit.  It is a scoped exponential
obstruction for fresh uniform shifts.  It is not an all-input factoring
lower bound.

## Algebra checks

1. The homogeneous subtraction is `-a^N`, so the local Frobenius form is
   exactly `h_(q,a)^p` and `h_(p,a)^q`.
2. Frobenius permutes cyclic positions only because `gcd(r,pq)=1`.
3. In the `p`-local expansion, the two terms at `a^e` differ in exponent by
   `p-1`.  If they collide modulo `r`, Pascal combines them to
   `binom(d+1,e)`.
4. The premise `d<p-1` is needed in that collision case.  It excludes
   vanishing modulo `p`.
5. The range `d>r` makes every `p`-local bucket nonzero and is also the strict
   inequality needed in the `q-1-r > p-1` root contradiction.
6. Every `q`-local direct coefficient polynomial is nonzero because
   `q>p`, the powers of `a` are distinct, and `p-1>r` visits every bucket.
7. The inverse identity is `(X+a)J=1-(-a)^r` after imposing `X^r=1`.
8. The common exceptional set has at most `r` shifts.  It is counted once,
   not once per coefficient.
9. The degree bound is `(2d-1)+d(r-1)=d(r+1)-1`.
10. The global coefficient-factor event is only bounded above by a local-zero
    union.  Equality is not asserted.

## Nullity checks

1. The old premise `p>d^2+1` was sufficient but unnecessary.  The only bad
   congruence is `d^2=1 mod p`.
2. An even prime gap with `d<p-1` is neither `1` nor `p-1`, so the local
   polynomial cannot vanish identically.
3. `X^r-1` is squarefree locally because `gcd(r,pq)=1`; shared roots and
   positive local nullity agree.
4. The coefficient and nullity probabilities are added only by a union bound.

## Infinite-family checks

1. The external theorem used is Baker--Harman--Pintz Theorem 1, not a
   conjectural prime-gap model.
2. Applying it near `p+p^(3/5)` puts the whole short interval strictly above
   `p` because `3/5>0.525`.
3. The resulting gap is both upper and lower `Theta(p^(3/5))`.
4. Balance and `d<p-1` hold for all sufficiently large members.
5. Numerical-QP values are `p^o(1)`, so every sampled `r_i` is eventually
   below `d`.
6. Adaptivity is allowed only before the fresh uniform shift.  Conditioning
   restores the one-trial law; no independence across trials is assumed.

## Scope checks

The result does not cover biased shifts, fixed-shift random points, joint
processing of nonzero values, adaptive elimination across shifts, or an
`r` selected from the same shift.  These exclusions are explicit.

F222-D01 is finite discovery evidence only.  No finite observation is used
to prove the unbounded theorem.

