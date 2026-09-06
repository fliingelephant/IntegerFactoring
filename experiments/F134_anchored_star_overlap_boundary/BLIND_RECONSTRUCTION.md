# F134 blind reconstruction

## Verdict

**PASS, with a source-scope qualification.**

I reconstructed the result from `STATEMENT.md` only. I did not read the
proof, manifest, audit files, ledgers, or any other F134 artifact.

Frozen input:

```text
STATEMENT.md
SHA-256 40354e169ef8632c206bd653819b3d0d117c670f134e18ff2f4558bc191c9483
```

The four theorems are correct. All three numerical certificates are exact.
The stated boundary is also correct: the result controls one fixed star. It
does not control retained old columns or later stars.

The source-scope qualification is important:

- Certificate A is valid in the broader exact-value/all-block setting. Its
  useful arm is not a literal small-prime F133 arm based at `q=18`.
- Certificate B's new arm is algebraically a literal F133 arm with multiplier
  `ell=3`. With the displayed threshold `B=1`, however, it is not in an
  `ell <= B` scan. It becomes a literal bounded arm when the scan bound is at
  least 3. The successful dependency also uses an old retained relation.
- Certificate C is valid in the broader exact-value/all-block setting. Its
  first nonzero arm is not a literal small-prime F133 arm based at `q=16`.
  The next value is a unary relation based at the newly exposed block 19.

These qualifications do not invalidate F134. The setup explicitly permits
any canonical endpoint presentation of the exact value. They only limit how
the examples can be advertised as instances of the literal unreduced F133
source grammar.

## Independent proof of Theorem 1

For distinct `i,j`,

\[
H_j-H_i=N(A_j-A_i).
\]

Also,

\[
\gcd(H_i,N)=\gcd(w+NA_i,N)=\gcd(w,N)=1.
\]

Therefore

\[
\begin{aligned}
\gcd(H_i,H_j)
&=\gcd(H_i,H_j-H_i)\\
&=\gcd(H_i,N(A_j-A_i))\\
&=\gcd(H_i,A_j-A_i).
\end{aligned}
\]

The digits are distinct, so `A_j-A_i` is nonzero. Hence

\[
\gcd(H_i,H_j)\leq |A_j-A_i|\leq B.
\]

Thus a prime greater than `B` divides at most one arm. It follows directly
that the integers `sf_{>B}(H_i)` are pairwise coprime.

## Independent proof of Theorem 2

Valuation parity is additive under multiplication. Since `P_i=qH_i`,

\[
p_i=a+h_i.
\]

For a selector `x`, with `t(x)=sum_i x_i` in `F_2`,

\[
Mx=\sum_i x_i p_i
=t(x)a+\sum_i x_i h_i.
\]

Thus

\[
x\in\ker M
\iff
\sum_i x_i h_i=t(x)a.
\]

Project this equality to primes greater than `B`. Theorem 1 says that the
large-prime supports of the selected `H_i` are disjoint. The left side is
therefore represented by the squarefree integer

\[
\prod_{i:x_i=1}\operatorname{sf}_{>B}(H_i).
\]

The right side is represented by 1 when `t(x)=0`, and by
`sf_{>B}(q)` when `t(x)=1`. Both representatives are squarefree. Equal parity
vectors therefore give the exact integer equality

\[
\prod_{i:x_i=1}\operatorname{sf}_{>B}(H_i)
=
\operatorname{sf}_{>B}(q)^{t(x)}.
\]

For even support, the right side is 1. Pairwise coprimality and positivity
then force every selected large squarefree part to equal 1. For odd support,
the selected pairwise-coprime parts form a partition of `sf_{>B}(q)`. If
`sf_{>B}(q)=1`, the same conclusion as in the even case holds for both
parities.

Finally, the restriction of the linear map `t` to `K=ker M` has rank zero or
one. Its kernel is `K_even`. If an odd vector `x_0` exists, every odd vector
is uniquely `x_0+z` with `z in K_even`. This proves the two-coset formula.

## Independent proof of Theorem 3

Let `r>B`. Suppose `v_r(q)` is even and `v_r(H_i)` is odd. Theorem 1 says
that `r` divides no other `H_j`. Hence the `r`-coordinate of `p_i=a+h_i` is
one, while the same coordinate of every other `p_j` is zero. This row has
degree one. Any kernel vector must have `x_i=0`.

Now let `x in K_even`. The anchor term cancels because `t(x)=0`, so

\[
\sum_i x_i h_i=0.
\]

If `sf_{>B}(H_i)>1`, choose a prime `r>B` that occurs oddly in `H_i`.
Theorem 1 says that it occurs in no other arm vector. The `r`-coordinate of
the last equality forces `x_i=0`. This proves

\[
K_{\rm even}\subseteq
\{x:x_i=0\text{ if }\operatorname{sf}_{>B}(H_i)>1\}.
\]

This argument needs prime rows only for the proof. A complete joint
gcd-free refinement groups primes that have the same valuation data across
all inputs. Parity on these coprime blocks therefore gives the same exact
square-product kernel. It does not require integer factorization.

If `B` is quasipolynomial, trial division through `B` is also within
quasipolynomial work. After all factors at most `B` are removed, the
remaining cofactor is a square exactly when `sf_{>B}(H_i)=1`.

For an old matrix `M_0`, the full dependency equation is instead

\[
M_0y+a t(x)+\sum_i x_i h_i=0.
\]

An old combination can cancel a row that is private only inside the new
star. Thus the theorem cannot delete the cross-layer escape.

## Independent proof of Theorem 4

Equation (1) gives

\[
P_i-P_j=qN(A_i-A_j).
\]

The digits are distinct, so the exact values are distinct inside one star.

Suppose a value `P` duplicates an earlier column. In the matrix with both
copies, the new kernel direction selects the two equal columns. Its exact
product is `P^2`, so its positive square root is `P`. Since every retained
value is 1 modulo `N`, this direction has normalized root `+1`.

More explicitly, any dependency using one copy can use the other copy with
the same exact product. A dependency using both copies can remove both; its
root changes by a factor `P`, which is 1 modulo `N`. Hence deleting one
exact-value copy does not change the normalized-root image.

This conclusion concerns exact-value columns. A different endpoint
presentation can expose new gcd-free blocks. Keeping that presentation-level
feedback is compatible with deleting the duplicate exact-value column.

## Independent check of Certificate A

The canonical inverse identity is

\[
18\cdot7=126=1+5\cdot25.
\]

For digits 0 and 1,

\[
H_0=7,\qquad H_1=32,\qquad \gcd(7,32)=1,
\]

and

\[
P_0=126,\qquad P_1=18\cdot32=576=24^2=1+23\cdot25.
\]

The four sign gcds are, in the displayed order,

\[
1,\ 25,\ 25,\ 1.
\]

Thus none is proper. The one-column dependency on `P_1` is odd.
Here

\[
\operatorname{sf}_{>1}(H_1)=2
=\operatorname{sf}_{>1}(q),
\]

so the large parity cancels through the common anchor. The root is
`24=-1 mod 25`, and is global.

Source scope: the interesting presentation is `(24,24)`. It is not of the
literal form `(ell*q,H_1/ell)` for an integer `ell`: `24/18` is not an
integer. Also, every divisor `ell>1` of 32 makes `ell*q>=36>N`; `ell=1`
leaves the second endpoint 32 greater than `N`. Thus this arm belongs to the
broader exact-value/all-block setting, not the literal small-prime F133
source based at `q=18`.

## Independent check of Certificate B

The identities are

\[
28\cdot46=1288=1+9\cdot143,
\]

\[
H_0=46,\qquad H_1=189,\qquad \gcd(46,189)=1,
\]

and

\[
P_1=28\cdot189=84\cdot63=5292
=1+37\cdot143=3\cdot42^2.
\]

The old value satisfies

\[
P_*=102\cdot136=13872
=1+97\cdot143=3\cdot68^2.
\]

Each of the six named sign gcds equals 1. Also,

\[
P_1P_*=(3\cdot42\cdot68)^2=8568^2,
\]

with

\[
\gcd(8568-1,143)=13,
\qquad
\gcd(8568+1,143)=11.
\]

Finally, `189=3^3*7`, so `sf_{>1}(H_1)=21`. The anchor
`28=2^2*7` cancels 7. The old relation cancels the remaining odd row 3.

Source scope: the new arm has the literal multiplier `ell=3` because

\[
84=3q<N,\qquad 189=3\cdot63.
\]

It is therefore an algebraic F133 arm. It is not in an `ell<=B` scan with
the displayed `B=1`. A scan bound at least 3 includes it. The factorization
step itself is cross-layer because `P_*` is an old retained value, not an arm
of this star.

## Independent check of Certificate C

The first canonical inverse identity is

\[
16\cdot46=736=1+15\cdot49.
\]

For digit 1,

\[
H_1=95=5\cdot19,
\]

and

\[
P_1=16\cdot95=38\cdot40=1520=1+31\cdot49.
\]

The next unary relation is

\[
19\cdot31=589=1+12\cdot49.
\]

Each of the six named sign gcds equals 1. The values 1520 and 589 are
distinct. Both contain 19 to odd valuation. Thus the 19-row has degree one
in the first star and degree at least two after the next round. No square
dependency follows from this fact alone.

Source scope: no divisor `ell` of `H_1=95` gives both literal endpoints
`ell*q<N` and `H_1/ell<N`. For `ell=1`, the second endpoint is 95. For
`ell>=5`, the first endpoint is at least 80. The presentation `(38,40)` also
does not have `38=ell*q`. Thus the first nonzero arm is broader
exact-value/all-block feedback. The later `(19,31)` value is a unary
relation after the new block 19 is exposed.

## Final scope check

The proof uses the cancellation

\[
H_i-H_j=N(A_i-A_j)
\]

for one fixed `q,w`. For two different anchors, the difference contains the
extra term `w_q-w_{q'}`. The gcd bound does not transfer.

The result therefore proves only this local boundary:

\[
\text{one star cannot share unrelated primes greater than B between arms.}
\]

It leaves all stated escapes open. In particular, it gives no success
probability, no closure theorem, no rule that forces a non-global root, and
no factoring algorithm.

## Machine arithmetic check

I independently evaluated all displayed products, carries, sign gcds,
root gcds, distinctness claims, and 19-adic parity claims with Python 3.
The check returned:

```text
ALL CERTIFICATE ARITHMETIC PASSED
```
