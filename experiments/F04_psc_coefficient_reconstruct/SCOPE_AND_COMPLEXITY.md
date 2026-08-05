# Exact scope and bit-complexity relevance

## What is certified

The result is exact for the single supplied integer

`N=20000000499999937=100000007*199999991`,

the single modulus `X^2953-1`, and exactly the 2,942 integer shifts
`1<=a<=2942`.  It certifies the literal coefficient vectors, their unit status,
both field degree chains, and—through the field theorem—the stated count of
nonzero determinants.  The theorem in `THEOREM.md` is not finite: it applies
to arbitrary fields and arbitrary nonzero `F,G` of degrees `m>n`.

The generator uses the supplied factorization.  In characteristic `p`, it
computes

`(X+a)^N=(X^p+a)^q`,

and similarly modulo `q`, then reconstructs each unique residue modulo `N` by
CRT.  This is exact arithmetic in the global quotient, not a probabilistic
test.  The complete global coefficient file is closed before the verifier
opens it and reduces its entries to either field.

## Cost of this finite run

Let `A` be the number of shifts and `r` the quotient degree.  Global generation
uses `2A` binary polynomial powers, with `O(log p+log q)` cyclic polynomial
multiplications per shift, followed by `Ar` CRT reconstructions.  The actual
artifact stores `Ar=8,687,726` coefficients of at most 55 bits in 69,513,632
bytes including headers.

For a normal candidate chain, each Euclidean quotient has degree one.  The
verifier computes its two coefficients exactly and updates `k` remainder
coefficients at degree `k`.  A complete field chain therefore costs

`sum_(k=1)^(r-1) O(k)=O(r^2)`

field operations, and all chains cost `O(2Ar^2)` field operations and
`O(Ar+r)` stored words.  In a bit model, each field operation has cost
polynomial in `log p` or `log q`; using schoolbook integer arithmetic gives the
coarse bound `O(Ar^2 (log N)^2)` for this verification phase.  FLINT uses
word-sized exact modular arithmetic here.  These are verification costs, not
the cost of computing all determinant matrices.

## What this cannot establish

The finite certificate assumes the factors `p,q`; it does not discover them.
It concerns one 55-bit `N`, and `A` and `r` are fixed numerical parameters.
No relation bounding analogous parameters by a uniform polynomial in the
input bit length has been proved here.  Hence the successful timings, the
fixed-instance operation count, and even the unbounded determinant theorem do
not imply a Las Vegas factoring algorithm, an expected polynomial runtime, or
any claim for other integers or shifts.

