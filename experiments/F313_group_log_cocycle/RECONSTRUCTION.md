# Independent reconstruction of the group-log formulas

Input: `STATEMENT_ONLY.md`

Input SHA-256: `48af5e43fad1e06e651bc627d3e20ddfe10ca633c92c0b49d233bea4c63eaa1b`

This reconstruction used only the statement above and ordinary integer
arithmetic.  Algebra involving the bits `eta`, `gamma`, `p`, `d`, or
`r_j` is over `F_2` whenever the displayed line is marked modulo two.
Ordinary integer sums are identified explicitly.

## 1. Lift notation and a carry identity

Put

```text
h_j = 5^j mod M in [1,M),
C_j = 5^j mod 2M in [1,2M).
```

Thus `C_j = h_j + M eta_j`.  The elementary valuation identity

```text
v_2(5^(2^t) - 1) = t+2
```

follows by induction from squaring (or from the usual two-adic lifting
identity).  It gives the following facts.

* The order of `5` modulo `M` is `L`.
* The residues `h_j`, for `j mod L`, are exactly the odd residues that are
  `1 mod 4`.
* `5^L = 1+M mod 2M`.

For `0 <= a,j < L`, let

```text
r = a+j mod L,
c_a(j) = floor((a+j)/L).
```

The last fact shows that the high `M`-bit of `5^(a+j) mod 2M` is
`eta_r+c_a(j)`.  Comparing this with

```text
C_a C_j
  = h_a h_j + M(eta_a h_j + eta_j h_a) + M^2 eta_a eta_j
```

gives

```text
p_a(j) := floor(h_a h_j/M) mod 2
        = eta_(a+j) + eta_j + eta_a + c_a(j).                 (1)
```

Here and below, subscripts of `eta` are reduced modulo `L`.  Define

```text
d_a(j) = eta_(a+j) + eta_j + c_a(j),                          (2)
```

so that `p_a(j)=d_a(j)+eta_a`.  Since `L` is even and `c_a` has exactly
`a` ones,

```text
sum_j d_a(j) = a mod 2,
sum_j p_a(j) = a mod 2.                                      (3)
```

The sign in the coordinates does not change (1).  Indeed,

```text
floor((M-h_a)h_j/M) = h_j-1-floor(h_a h_j/M),
```

and `h_j-1` is even.  Also, for the canonical representative
`A=(-1)^sigma_A h_a mod M`,

```text
(A-1)/2 = sigma_A mod 2,                                     (4)
```

because `h_a=1 mod 4` and `M=0 mod 8`.

## 2. The circular convolution and `gamma`

For any `r mod L`, set

```text
G(r) = sum_j eta_j eta_(r-j).
```

The involution `j -> r-j` cancels every non-fixed pair in `F_2`.  If `r`
is odd, it has no fixed point.  If `r` is even, its two fixed points are
`r/2` and `r/2+L/2`.  Therefore

```text
G(r) = gamma_r.                                               (5)
```

This proves directly why the four `gamma` terms occur in Claim 1.

## 3. Reconstruction of `K` modulo four

Write `f_A(w)=floor(Aw/M)`.  Pair the term indexed by `w=h_j` with the
term indexed by `M-h_j`.  Their inverses are `h_(-j)` and `M-h_(-j)`.
If

```text
x = f_A(h_j),
y = f_B(h_(-j)),
```

then the pair in `K(A,B)` is

```text
xy + (A-1-x)(B-1-y).
```

It is even.  After division by two, (4) gives

```text
pair/2 = xy + sigma_A y + sigma_B x mod 2.
```

The omitted product `(A-1)(B-1)/2` is even.  Summing and using (3),

```text
K(A,B)/2
  = sum_j p_a(j)p_b(-j) + sigma_A b + sigma_B a.               (6)
```

It remains to evaluate the convolution.  From `p_a=d_a+eta_a` and (3),

```text
sum_j p_a(j)p_b(-j)
  = sum_j d_a(j)d_b(-j) + b eta_a + a eta_b.                  (7)
```

Expand the first sum using (2).  Its four `eta eta` terms are, by (5),

```text
gamma_(a+b) + gamma_a + gamma_b + gamma_0.                    (8)
```

The mixed carry terms vanish.  In detail, `c_b(-j)` is supported on
`j=1,...,b`, while `c_a(j)` is supported on
`j=L-a,...,L-1`.  The mixed sum is

```text
sum_(j=1..b) (eta_(a+j)+eta_j)
  + sum_(j=1..a) (eta_(b+j)+eta_j).
```

If `P(n)=sum_(j=1..n) eta_j` for the periodic extension of `eta`, the two
lines are respectively

```text
P(a+b)+P(a)+P(b),
P(a+b)+P(b)+P(a),
```

so their sum is zero.  Finally, the supports of `c_a(j)` and `c_b(-j)`
intersect in exactly

```text
max(0,a+b-L+1)
```

indices.  Combining (6)--(8) proves

```text
K(A,B)/2
  = max(0,a+b-L+1) + b eta_a + a eta_b
    + gamma_0 + gamma_a + gamma_b + gamma_(a+b)
    + sigma_B a + sigma_A b                                  mod 2.
```

The pairing also proves that `K(A,B)` is even.

### Raw positive arguments

Let `A=A0+M alpha` and `B=B0+M beta`.  Exact expansion gives

```text
K(A,B) = K(A0,B0)
       + alpha U(B0) + beta U(A0) + alpha beta V,              (9)

U(A) = sum_w u(w) f_A(w),
V    = sum_w w u(w).
```

For `h=h_j`, `v=h_(-j)`, and `x=f_A(h)`, a paired contribution to `U(A)`
is

```text
v x + (M-v)(A-1-x).
```

It is even, and its half is `x+sigma_A mod 2`.  Hence (3) and evenness of
`L` give

```text
U(A)/2 = a mod 2.                                             (10)
```

A paired contribution to `V` is

```text
h v + (M-h)(M-v) = 2hv + M(M-h-v).
```

Its half is odd modulo two.  There are `L` pairs, and `L` is even, so

```text
V/2 = 0 mod 2.                                                (11)
```

Equations (9)--(11) add `alpha*b+beta*a` to `K/2 mod 2` and give no
`alpha*beta` term.  They also show directly that the raw `K` remains even.

## 4. Reconstruction of canonical `T` modulo four

Again take `h=h_j` and `v=h_(-j)`, and put

```text
q_j = (hv-1)/M,
Delta_j = M-h-v.
```

For the negative member of the pair,

```text
q(M-h) = q_j+Delta_j.
```

The integer `Delta_j` is even, and

```text
Delta_j/2 = 1 mod 2,                                         (12)
```

because `h=v=1 mod 4` and `M=0 mod 8`.

Let `N` have coordinates `(sigma,a)`, put `n=N-1`, and set
`x=f_N(h)`.  The paired contribution to `T(N)` is

```text
v q_j x + (M-v)(q_j+Delta_j)(n-x).
```

Reducing this expression modulo four, dividing the resulting even
quantity by two, and using (12) and `n/2=sigma mod 2` gives

```text
pair/2 = (q_j+1)x + sigma q_j mod 2.                           (13)
```

In particular, every pair is even, so canonical `T(N)` is even.

The parity of `q_j` is also explicit.  In `C_j C_(-j)`, the exponent sum
is zero for `j=0` and is `L` otherwise.  Since `5^L=1+M mod 2M`, comparison
with `hv=1+M q_j` gives

```text
q_j = 1_(j != 0) + eta_j + eta_(-j).                          (14)
```

Consequently,

```text
sum_j q_j = 1 mod 2,
r_j := q_j+1 = 1_(j=0) + eta_j + eta_(-j).                    (15)
```

The bit `d_a(j)` has a direct interpretation.  If

```text
Q_j = floor(C_a h_j/M),
```

then `Q_j mod 2=d_a(j)`.  Moreover,

```text
Q_j - 2 floor(C_a h_j/(2M))
```

is the canonical bit `Q_j mod 2`.  The `h_j` are a permutation of the
integers `1+4j` in `[1,M)`.  Therefore the ordinary integer in Claim 2 is
exactly

```text
D = sum_j d_a(j),                                             (16)
```

where each `d_a(j)` on the right is represented by `0` or `1`.  Equation
(3) now proves that `D-a` is even.

Since `p_a=d_a+eta_a`, equations (13)--(16) give

```text
T(N)/2 = sigma + eta_a + sum_j r_j d_a(j) mod 2.              (17)
```

It remains to express the last sum through `D`.  Write

```text
E = sum_j eta_j,
A_a = sum_j eta_j eta_(j+a),
B_a = sum_j c_a(j)(eta_(j+a)+eta_j).
```

For three bits `X,Y,Z`, their xor as an ordinary zero-or-one integer is

```text
X+Y+Z - 2(XY+XZ+YZ) + 4XYZ.
```

Apply this to (2) and sum.  Using `sum c_a=a` gives

```text
(D-a)/2 = E + A_a + B_a mod 2.                               (18)
```

On the other hand, expand `sum r_j d_a(j)` with (15).  Since
`d_a(0)=eta_a`, equation (5) gives

```text
sum_j r_j d_a(j)
  = eta_a + A_a + gamma_a + E + gamma_0
    + sum_j c_a(j)(eta_j+eta_(-j)).                           (19)
```

On the support `j=L-a,...,L-1` of `c_a`,

```text
sum eta_(-j) = sum_(t=1..a) eta_t,
sum eta_(j+a) = sum_(t=0..a-1) eta_t.
```

Their sum is `eta_a`, since `eta_0=0`.  Comparing (18) and (19) therefore
yields

```text
sum_j r_j d_a(j) = gamma_0 + gamma_a + (D-a)/2 mod 2.
```

Substitution in (17) proves Claim 2:

```text
T(N)/2
  = sigma + gamma_0 + gamma_a + eta_a + (D-a)/2              mod 2.
```

## 5. Uniform polynomial-bit algorithms

No step below enumerates the `M/2` units.

### Coordinates

For a canonical odd `A`, set `sigma=0` and `h=A` if `A=1 mod 4`; set
`sigma=1` and `h=M-A` otherwise.  Then `h=1 mod 4`.

Recover `a` one bit at a time.  Initially `a=0` and `x=1`.  At stage
`t=0,...,k-3`, maintain

```text
x = 5^a mod M,
0 <= a < 2^t,
x = h mod 2^(t+2).
```

Compare `x` and `h` modulo `2^(t+3)`.  If they differ, replace

```text
a <- a+2^t,
x <- x * (5^(2^t) mod M) mod M.
```

The multiplier is `1+2^(t+2) mod 2^(t+3)`, so it flips exactly the next
bit and preserves the invariant.  Successive multipliers are obtained by
modular squaring.  The final `a` is the unique value in `[0,L)`.

This uses `O(k)` modular multiplications on `O(k)`-bit integers.  With
schoolbook arithmetic, its bit cost is `O(k^3)` and its space use is
`O(k)` bits.

### `eta` and `gamma`

For any `j mod L`, binary modular exponentiation computes

```text
C_j = powmod(5,j,2M)
```

in `O(k)` multiplications of `O(k)`-bit integers.  Return `eta_j=0` if
`C_j<M`, and `1` otherwise.  For `gamma_r`, first reduce `r mod L`.  Return
zero if `r` is odd.  Otherwise return

```text
eta_(r/2) + eta_(r/2+L/2) mod 2.
```

Each requested `eta` or `gamma` costs `O(k^3)` bit operations and `O(k)`
space with schoolbook arithmetic.  Only a constant number is requested by
either formula.

### The two floor sums

Use the standard Euclidean floor-sum routine

```text
FloorSum(n,m,A,B) = sum_(j=0..n-1) floor((A*j+B)/m).

answer = 0
repeat:
    if A >= m:
        answer += n*(n-1)/2 * floor(A/m)
        A %= m
    if B >= m:
        answer += n * floor(B/m)
        B %= m
    y = A*n+B
    if y < m:
        return answer
    n = floor(y/m)
    B = y mod m
    swap(A,m)
```

The two sums in `D` are

```text
S1 = FloorSum(L, M,  4C, C),
S2 = FloorSum(L, 2M, 4C, C),
D  = S1-2S2.
```

The routine is the Euclidean algorithm in floor-sum form, so it has
`O(k)` iterations.  Its operands and exact accumulator have `O(k)` bits
(the accumulator needs at most a constant multiple of `k` bits).  Thus
the two exact sums cost `O(k^3)` bit operations and `O(k)` space with
schoolbook multiplication and division.  Computing only `D mod 4` is also
valid: the proved parity guard makes `(D-a)/2 mod 2` the half of
`(D-a) mod 4`, which is either zero or two.

For canonical inputs, compute the displayed right-hand side and return
twice that bit as the residue modulo four.  For raw `K`, reduction modulo
`M`, extraction of `alpha mod 2` and `beta mod 2`, and the correction in
Section 3 complete the algorithm.  If the raw input bit lengths are
`n_A,n_B`, a conservative bound is

```text
O((k+n_A+n_B)^3) bit operations
```

and linear space in `k+n_A+n_B`.  The analogous canonical `T` bound is
`O((k+n_N)^3)`.  These bounds include input reduction and are deliberately
loose fixed polynomials.

## 6. Optional raw-`T` corollary

This section uses P238 only for the declared black-box value
`Q0=sum_w q(w) mod 4`.

For `N=N0+M ell`, exact expansion gives

```text
T(N)-T(N0) = ell sum_w mu(w)w
            = ell sum_w (q(w)+M q(w)^2)
            = ell Q0 mod 4,
```

because `u(w)w=1+M q(w)` and `M=0 mod 4`.

The correction is safe to divide by two modulo two.  Indeed, pairing
`w=h` with `M-h` gives

```text
q(h)+q(M-h) = 2q(h)+M-h-u(h),
```

which is even.  Hence `Q0` is an even residue modulo four, and so is
`ell*Q0`.  Thus the optional quotient correction is unambiguously

```text
(ell*Q0 mod 4)/2 mod 2.
```

## 7. Independent finite check

A direct, independent exhaustive check for `k=3,...,8` compared both
formulas with the defining sums for every canonical odd input (and every
canonical pair for `K`).  It also checked evenness and the `D-a` parity
guard.  All cases passed.  This finite check is supplementary and is not
used in the proof.
