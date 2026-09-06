# F261-D01 hostile audit of the exact theorem

## Authentication and verdict

**Verdict: PASS.**

The audited bytes are `ALGEBRA.md` with SHA-256

```text
df27b6557ac2fe2ae29a495241c66741e864f8d667237f04855aa82f499aa67f
```

This equals the hash in `PRELAUNCH_MANIFEST.md`.  The other frozen packet
hashes also matched before the audit.  This audit did not compile code,
generate a cohort, or run F261-D01.

Two scope qualifications do not change the verdict:

1. At the no-prefix endpoint `R=1`, read (6) as the unique trivial residue
   pair `a=b=0`.  This avoids relying on a software convention for an
   inverse modulo one.
2. The X85 maximum is a frozen exhaustive-enumeration attribution, not a
   consequence of the algebra.  This audit replayed the exact witnesses and
   checked the attribution against the frozen X85 diagnosis.  It did not
   rerun that old exhaustive enumeration.

## 1. Input size, `B`, and positive centers — PASS

From `n=ceil(log2(N+1))`,

```text
2^(n-1) <= N <= 2^n-1.
```

If `n=2m`, then `N>=B^2/2`; if `n=2m+1`, then `N>=B^2`.
The balance condition gives `p>sqrt(N/2)`, hence `p>B/2` in both cases.
Thus `q>p>B/2`, and every true round-half-up center is positive for
`u>=1`.

Also `q<sqrt(2N)<2B` in both parity cases, and `p<q`.  Therefore the
stronger public coarse bound `1<=Kp,Kq<=2u` holds.  The stated `3u` bound
is safe.

## 2. Public factor and center intervals — PASS

The inequalities

```text
sqrt(N/2) < p < sqrt(N) < q < sqrt(2N)
```

follow respectively from `q<2p`, `p<q`, and `q<2p`.  Since the variables
are integers, they imply exactly the four displayed inclusive factor
bounds in Section 2.  Round-half-up is monotone, so (5) contains both true
centers.

For fixed `u`, the exact center cardinalities are

```text
dp(u) = floor((u*p_+ + B/2)/B) - floor((u*p_- + B/2)/B) + 1,
dq(u) = floor((u*q_+ + B/2)/B) - floor((u*q_- + B/2)/B) + 1.
```

They are positive because each interval contains its true center.  The
coarse bound above gives `dp(u),dq(u)<=2u`, so each is `O(u)` with an
absolute constant.

## 3. Half ties — PASS

For odd `p` and `B=2^m`, a tie is the congruence

```text
u*p = B/2 (mod B).
```

Every odd multiplier of `B/2` is congruent to `B/2` modulo `B`.
Multiplication by the odd inverse of `p` therefore proves
`u=B/2 (mod B)`.  The converse is immediate.  At a tie, the displayed
floor formula increments the quotient and leaves centered residue `-B/2`,
as claimed.  The same proof applies to `q`.

The regression row `p=101,q=109,B=128,u=64` gives `x=y=-64` under the
literal rule.  The phrase "in this packet" is important: this is not the
smallest source-family example.  For example, `p=11,q=19,B=16,u=8` is a
smaller valid zero-defect half-tie row.

## 4. Carry, weighted trace, and divisibility — PASS

Substituting `N=1+BH` in the expanded centered product gives

```text
xy-u^2 = 0 (mod B),
u^2 H = Kp*Kq*B + Kp*y + Kq*x + c.
```

Thus (1) is integral.  Independently expanding
`u(Kp*q+Kq*p)` and eliminating the cross terms gives

```text
u*T = u^2*H + Kp*Kq*B - c.
```

This proves (2), including divisibility by `u`.  Substitution of either
factor proves (3), and direct expansion proves the square identity (4).

## 5. Decoder and zero-center endpoints — PASS

When `Kq>0`, a nonnegative square discriminant is not enough by itself;
the decoder must also require divisibility of `T+delta` or `T-delta` by
`2Kq`.  The instruction to test integral roots and then test exact proper
divisors supplies both checks.  The endpoint `Kp=0,Kq>0` remains inside
this quadratic case; its roots are `0` and, when integral, `T/Kq`.

When `Kq=0,Kp>0`, (3) is exactly `-T*X+Kp*N=0`, so the stated linear
candidate `Kp*N/T` is correct when `T` is nonzero and divides the numerator.
If `T=0`, no solution exists.  When both centers are zero, `-T*X=0`
either has only the useless root zero or is an identity, so rejection is
correct.  None of these zero-center cases can be a true tuple in the
canonical balanced source because both true centers are positive.

## 6. Prefix congruences — PASS

For `R>=2`, `a` is odd and invertible.  Zero defect gives `N=1 (mod R)`,
so

```text
b = N*a^(-1) = q (mod R).
```

Reducing the integer trace gives (7).  Multiplying (7) by `u` and using
`c=A-uT` gives (8).  Conversely, cancellation of the integer factor `u`
from divisibility by `uR` recovers (7).  The term `Kp*Kq*B` cannot be
discarded unless the additional condition `u | B/R` holds.

For `R=1`, all congruences are tautologies when `a=b=0`; this is the
no-prefix convention stated in the verdict qualification.

## 7. Direct-`T` enumeration and candidate count — PASS

The cap `|c|<=C` and identity `c=A-uT` give exactly interval (9).
Reconstructing `c` from an enumerated integer `T` makes divisibility by `u`
automatic, including when `A-C` is negative.

Two members of one residue class modulo `R` are separated by at least `R`.
The real width of the interval before rounding is `2C/u`.  Hence one class
contains at most

```text
1 + floor(2C/(uR))
```

integers.  The exact frozen upper bound is therefore

```text
sum_(1<=u<=U) dp(u)*dq(u)*(1+floor(2C/(uR))).
```

Using `dp(u),dq(u)<=2u` bounds this by

```text
4*sum u^2 + (8C/R)*sum u = O(U^3 + C*U^2/R).
```

The `R=1` and `uR>2C` specializations follow.  A hostile exhaustive check
over signed small interval endpoints, including empty intervals, agreed
with (10); this check is supporting evidence, not part of the proof.

## 8. One-dimensional inverse map — PASS

For `R>=2` and odd `u`, both `up` and `x=up-KpB` are odd, so `x` is a unit
modulo `B`.  Equation (1) gives (12).  Because `R|B`, the true residue also
satisfies `x=ua (mod R)`, which yields (13).

The half-open centered interval has length `B` and `R|B`.  Every residue
class modulo `R` therefore occurs exactly `B/R` times, proving the claimed
number of `z` values.  Each candidate `x` is odd.  Its inverse exists, the
centered representative `y(x)` is unique in `[-B/2,B/2)`, and
`xy(x)-u^2` is divisible by `B`.  The true `(x,y,c)` is one of these map
points.  The map is a diagnostic superset; the theorem does not claim that
every point comes from a factorization.

## 9. X85 repair rows — PASS with the stated provenance qualification

Exact replay at `B=4194304,u=1` gives:

```text
p=3105539, q=6201259:
  Kp=1, Kq=1, x=-1088765, y=2006955, c=-520969.

p=3162347, q=6318019:
  exact Kp=1, Kq=2, x=-1031957, y=-2070589, c=509443;
  forced Kp=Kq=1 gives y=2123715 and c=-522514.
```

Both pairs consist of primes, satisfy `p<q<2p`, have 45-bit products, and
satisfy `B|(N-1)`.  Thus the witness values, signs, and distinct-center
labels are correct.  The frozen X85 diagnosis records `520969` as the
independently exhaustive distinct-nearest-center maximum and `522514` as
the mislabelled forced-common-center maximum.  No claim about the old
maximum is inferred from these two rows alone.

## Boundary of this PASS

The audit proves only the elementary identities, enclosures, decoder, and
candidate-count theorem in the authenticated file.  It does not supply the
prefix `a`, prove a small carry, prove useful inverse-map density, or promote
finite F261 data to an asymptotic factoring result.
