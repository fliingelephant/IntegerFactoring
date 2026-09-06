# Proof of F216

## 1. Square-class normalization

Let `d` be the odd residue in `{1,3,5,7}` equal to `N modulo 8`. Since every
such `d` is its own inverse modulo `8`,

\[
Nd^{-1}\equiv1\pmod8.
\]

An odd unit modulo `2^t` is a square if and only if it is `1 modulo 8`.
Hence one can construct an odd `a` with

\[
a^2\equiv Nd^{-1}\pmod {2^t}.
\]

This construction is public. One may lift one square-root bit at a time.
For `u=av`,

\[
u+Nu^{-1}
\equiv av+da^2(av)^{-1}
=a(v+dv^{-1})\pmod {2^t}.
\]

Both multiplication by `a` and `v -> av` are bijections. Therefore

\[
W_t(N)=aW_t(d).
\]

It remains to determine the four representative images.

## 2. The classes `d=3` and `d=7`

For every odd `u`, one has `u^{-1}=u modulo 8`. Therefore

\[
u+3u^{-1}\equiv4\pmod8,
\qquad
u+7u^{-1}\equiv0\pmod8.
\]

These give the two required containments.

Conversely, let `s=4k` with `k` odd. The congruence

\[
u+3u^{-1}\equiv s\pmod {2^t}
\]

is equivalent to

\[
(u-2k)^2\equiv4k^2-3\pmod {2^t}.
\]

The right side is `1 modulo 8`, so it has an odd square root modulo `2^t`.
This supplies an odd `u`. Hence every residue `4 modulo 8` occurs.

Similarly, if `s=8k`, then

\[
u+7u^{-1}\equiv s\pmod {2^t}
\]

is equivalent to

\[
(u-4k)^2\equiv16k^2-7\pmod {2^t}.
\]

Again the right side is `1 modulo 8`, so every multiple of `8` occurs.
Counting the two arithmetic progressions proves

\[
|W_t(3)|=|W_t(7)|=2^{t-3}.
\]

## 3. The class `d=5`

Direct evaluation on the eight odd classes modulo `16` gives

\[
u+5u^{-1}\equiv6\text{ or }26\pmod {32}.
\]

The value is unchanged when `u` is replaced by `u+16`, so this checks all
odd classes modulo `32` and proves containment.

For the converse, write `s=2v`, where `v` is congruent to `3` or `-3`
modulo `16`. Completing the square gives

\[
u+5u^{-1}\equiv s\pmod {2^t}
\iff
(u-v)^2\equiv v^2-5\pmod {2^t}.
\]

Now

\[
v^2-5=4R,
\qquad R\equiv1\pmod8.
\]

Choose `z` with `z^2=R modulo 2^{t-2}` and put `u=v+2z`. This `u` is odd
and satisfies the displayed congruence. Thus both residue classes occur, and

\[
|W_t(5)|=2\cdot2^{t-5}=2^{t-4}.
\]

## 4. The ramified class `d=1`

First restrict to `u=1 modulo 4`. The identity

\[
u+u^{-1}-2=\frac{(u-1)^2}{u}
\tag{1}
\]

shows that the image is `2 modulo 16`. If the right side of (1) is zero
modulo `2^t`, it contributes the single image value `2`.

Otherwise put

\[
b=v_2(u-1)\ge2,
\qquad 2b<t,
\]

and write the right side of (1) as `2^{2b}w` with `w` odd modulo
`2^{t-2b}`. If `b=2`, then `u=5 modulo 8`, and therefore

\[
w\equiv5\pmod8.
\]

If `b>=3`, then `u=1 modulo 8`, and

\[
w\equiv1\pmod8.
\]

The congruences are interpreted after reduction when fewer than three bits
of `w` remain.

Every displayed value also occurs. To see this, lift a prescribed finite
`w` to an odd 2-adic integer in the same class and put `z=2^{2b}w`. The
quadratic equation

\[
u^2-(2+z)u+1=0
\]

has discriminant

\[
z(z+4)=2^{2b+2}w(1+2^{2b-2}w).
\]

For `b=2`, the odd part is `5*5=1 modulo 8`. For `b>=3`, its two factors
are both `1 modulo 8`. In either case the odd part is a 2-adic square. The
quadratic formula therefore gives an odd 2-adic root `u=1 modulo 4`, whose
reduction modulo `2^t` realizes the prescribed value.

Replacement of `u` by `-u` negates the trace. Hence the `u=-1 modulo 4`
branch is `-W_t^+(1)`. The two branches are disjoint because they are `2`
and `14 modulo 16`, respectively. This proves the stated disjoint-union
description.

For `k=t-2b`, the number of odd residues in one prescribed class modulo
`2^{min(3,k)}` is

\[
2^{\max(k-3,0)}.
\]

Thus

\[
|W_t(1)|=
2\left(
1+\sum_{b=2}^{\lfloor(t-1)/2\rfloor}
2^{\max(t-2b-3,0)}
\right).
\tag{2}
\]

If `t` is even, summing the geometric progression in (2) gives

\[
|W_t(1)|=(2^{t-4}+8)/3.
\]

If `t` is odd, it gives

\[
|W_t(1)|=(2^{t-4}+10)/3.
\]

Both formulas imply `|W_t(1)|=2^t/48+O(1)` and, in fact,
`|W_t(1)|>=2^t/48`.

## 5. Consequence for the beta-two trace projection

The other three square classes have densities `1/8`, `1/16`, and `1/8`.
Square-class normalization preserves cardinality. Therefore, for every odd
`N`,

\[
|W_t(N)|\ge2^t/48.
\]

At `t=n/4-polylog(n)`, this is exponential in `n`. The theorem concerns
the projected trace image only. The parameter `u`, interval order, and
nonlinear integer operations are not represented by this cardinality and
remain outside its scope.

