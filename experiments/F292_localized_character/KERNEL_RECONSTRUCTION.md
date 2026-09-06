# Blind reconstruction of one quadratic-Gauss/Cauchy kernel

## Status and scope

**Status: reconstructed.** Conditional only on the declared Hiary theorem, the
stated single-kernel claim is correct. The construction below handles negative
`a,b,c,s`, `a=0`, `b=0`, every nonunit reduction, all even-modulus parity
cases, exact pole removability, and certified absolute error. It neither sums
all `m` or `ell` terms nor factors `m` or `D`.

The sole mathematical input was
`experiments/F292_localized_character/KERNEL_STATEMENT_ONLY.md`, with verified
SHA-256

```
314695ff8f987a46eb8d90f1f9be4a6deb646bde324379b94a902971e957116b
```

No claim is made here for a sum over many outer indices or for several Cauchy
denominators.

## 1. Rational reduction

Put `g=gcd(b,m)` and `ell=m/g`, with positive gcd conventions. For every
integer `z`,

```
e_m(b z)^ell = 1.
```

Thus, as a polynomial identity in `t`,

```
(1-t^ell)/(1-t e_m(bz))
    = sum_{n=0}^{ell-1} t^n e_m(bzn).
```

After multiplication by `e_m(az^2+cz)` and summation over `z`, this gives

```
P(t) = sum_{n=0}^{ell-1} t^n G(a,c+bn;m),
F(t) = P(t)/(1-t^ell).
```

These are rational identities, so they also prove the asserted continuation
at removable points.

Let `x=rho-1` and define

```
q_k = [x^k] P(t0(1+x))
    = sum_{n=0}^{ell-1} binom(n,k) t0^n G(a,c+bn;m),                 (1)
```

where `binom(n,k)=0` for `k>n`. Only `q_0,...,q_J` are needed away from a pole,
and only `q_0,...,q_{J+1}` at a pole. The next section computes all of them
without enumerating `n`.

## 2. All complete-Gauss zero and nonunit cases

Set

```
d = gcd(a,m),   M=m/d,   a1=a/d.
```

The standard imprimitive reduction is

```
G(a,C;m) = 0                         if d does not divide C,
G(a,C;m) = d G(a1,C/d;M)             if d divides C.                (2)
```

Here `gcd(a1,M)=1`. For primitive quadratic coefficient, completing the square
gives the following exhaustive table. In the table, `C=c+bn`; the congruence
in the third column is exactly the condition for a nonzero value. All modular
inverses exist under the displayed hypotheses.

| Case | Constant factor `H` | Allowed `n` | Remaining phase `psi(n)` in `G=H e(psi(n))` |
|---|---:|---|---|
| `M=1` | `d` | `bn = -c (mod d)` | `0` |
| odd `M>1` | `d G(a1,0;M)` | `bn = -c (mod d)` | `-u ((c+bn)/d)^2/M`, `u=(4a1)^{-1} mod M` |
| `4` divides `M` | `d G(a1,0;M)` | `bn = -c (mod 2d)` | `-u ((c+bn)/(2d))^2/M`, `u=a1^{-1} mod M` |
| `M=2` | `2d` | `bn = d-c (mod 2d)` | `0` |
| `M=2Mo>2`, `Mo` odd | `2d G(a2,0;Mo)` | `bn = d-c (mod 2d)` | `-u (v(c+bn)/d)^2/Mo`, where `v=2^{-1} mod Mo`, `a2=v a1 mod Mo`, and `u=(4a2)^{-1} mod Mo` |

Here `e(y)=exp(2*pi*i*y)`. For completeness, the primitive identities behind
the even rows are

```
G(A,B;M) = 0                                      (4|M, B odd),
G(A,2C;M) = e_M(-A^{-1}C^2) G(A,0;M)              (4|M),
G(A,B;2Mo) = 0                                    (B even),
G(A,B;2Mo) = 2 G(vA,vB;Mo)                        (B odd),
```

where `A` is coprime to the even modulus. For odd modulus,

```
G(A,B;M)=e_M(-(4A)^{-1}B^2)G(A,0;M).
```

This proves both every zero in the table and the absence of any unlisted
zeros.

Each allowed condition has the form

```
b n = T (mod Q).
```

Compute `h=gcd(b,Q)`. If `h` does not divide `T`, every term in (1) is zero.
Otherwise put `L=Q/h`. If `L=1`, take `n0=0`; otherwise use extended Euclid to
find the unique `n0` in `[0,L-1]` satisfying the congruence. The allowed
indices in `[0,ell-1]` are exactly

```
n=n0+Lr,   0 <= r <= R=floor((ell-1-n0)/L).                         (3)
```

If `n0>ell-1`, the set is empty. This also covers `b=0`; then the applicable
congruence either fails or has `L=1`. In the empty case, all the `q_k` are
exactly zero.

On (3), the exponent

```
s n/D + psi(n)
```
is an exact rational quadratic polynomial

```
gamma0 + alpha r + beta r^2  (mod 1).                              (4)
```

For a nonconstant row of the table, write its phase as
`-u(y0+y1*r)^2/N`. Then explicitly

```
gamma0 = s*n0/D - u*y0^2/N,
alpha  = s*L/D  - 2*u*y0*y1/N,
beta   =             -u*y1^2/N.                                   (5)
```

The choice of `L` makes `y1` an integer in every row. In a constant-phase row,
use `gamma0=s*n0/D`, `alpha=s*L/D`, and `beta=0`. Reduce `alpha,beta` exactly
to `[0,1)` by integer modular arithmetic.

It follows that

```
q_k = H e(gamma0)
      sum_{r=0}^R binom(n0+Lr,k)e(alpha*r+beta*r^2).                (6)
```

Expand, over the rationals,

```
binom(n0+Lr,k)=sum_{j=0}^k w_{k,j} r^j.
```

The coefficients follow successively from the falling-factorial product, so
all expansions through degree `N` cost polynomially many operations on
integers of `O(N(log m+log(N+1)))` bits. Compute once the moments

```
S_j(R;alpha,beta)=sum_{r=0}^R r^j e(alpha*r+beta*r^2),  0<=j<=N.  (7)
```

For `R>0`, Hiary returns the normalized value `R^{-j}S_j`; multiplication by
the exact integer `R^j` recovers (7). For `R=0`, the one term is direct. Thus
(6) uses `O(N)` Hiary calls and polynomially many exact arithmetic operations.

The complete factors in `H` also require no long sum. For `G(a1,0;M)` call
Hiary with `K=M-1`, `j=0`, `alpha=0`, `beta=a1/M`. For
`G(a2,0;Mo)` use `K=Mo-1` in the same way. These moduli exceed one in the rows
where the calls occur. The `M=1` and `M=2` rows are already explicit.

If `k>=ell`, set `q_k=0` directly. Consequently, even `J>=ell` does not cause
an enumeration of the kernel indices.

## 3. Exact pole test and exact removability

The pole test is the integer divisibility test

```
t0^ell=1  iff  D divides s*ell.                                    (8)
```

Suppose (8) holds. Put

```
r0 = s*ell/D  (an integer),
b0 = b/g.
```

Then `t0=e_ell(r0)` and `gcd(b0,ell)=1` (with the trivial modulus-one case
handled directly). The inner geometric sum at `t0` is `ell` precisely when

```
b0*z = -r0 (mod ell).
```

Let `z0` be its unique solution in `[0,ell-1]`; take `z0=0` when `ell=1`.
The full solution set modulo `m` is `z=z0+ell*k`, `0<=k<g`. Hence

```
A=P(t0)/ell
 = e_m(a*z0^2+c*z0) G(a*ell,2*a*z0+c;g).                           (9)
```

Formula (9) decides `A=0` without numerical comparison. For a general
`G(U,V;q)`, put `delta=gcd(U,q)`. It is zero if `delta` does not divide `V`.
Otherwise put `q1=q/delta` and `V1=V/delta`. The reduced sum is nonzero
exactly in the following cases:

```
q1 odd (including q1=1);
q1 = 0 (mod 4) and V1 is even;
q1 = 2 (mod 4) and V1 is odd.                                     (10)
```

All other cases are zero. Tests (8)--(10) use only multiplication, gcd,
division, parity, and extended Euclid. If nonzero, the numerical value in (9)
is obtained by one `j=0`, `K=g-1` Hiary call with
`alpha=(2*a*z0+c)/g` and `beta=(a*ell)/g`, followed by multiplication by
`e_m(a*z0^2+c*z0)`; reduce both phases modulo one. The case `g=1` is direct.
If zero, return the exact complex number zero.

Since `1-rho^ell` has a simple zero at `rho=1`, (9) also proves that `A=0` is
equivalent to exact removability.

## 4. Taylor and Laurent recurrences

### Nonpole

Let `lambda=t0^ell` and

```
d_0=1-lambda,
d_r=-lambda*binom(ell,r)  (1<=r<=ell),
d_r=0                     (r>ell).
```

The Taylor coefficients are obtained in order from

```
B_j = (q_j-sum_{r=1}^j d_r B_{j-r})/d_0,  0<=j<=J.                (11)
```

### Pole

Now `lambda=1`. Write `f_{-1}=-A` and `f_j=B_j`. Since
`A/(1-rho)=-A/x`, multiplication by `1-(1+x)^ell` gives

```
B_j = (q_{j+1}
       -sum_{r=2}^{min(ell,j+2)} d_r f_{j+1-r})/d_1,
d_r=-binom(ell,r),   d_1=-ell,   0<=j<=J.                          (12)
```

For `j=0`, (12) is exactly

```
B_0=((ell-1)P(t0)/2-t0*P'(t0))/ell,
```

because `q_0=P(t0)=ell*A` and `q_1=t0*P'(t0)`.

## 5. Certified precision and bit complexity

All phases in (4)--(5) are stored first as exact reduced rationals. No
cyclotomic field is constructed. When a `Q`-bit dyadic phase is supplied to a
Hiary call, perturbing both phases by at most `2^{-Q}` changes its normalized
moment by at most

```
2*pi*(R+1)*(R+R^2)*2^{-Q}.                                        (13)
```

Indeed `r^j/R^j<=1`. To recover the unnormalized `S_j` to error `2^{-W}`, ask
for normalized error at most `2^{-W}R^{-j}` and take

```
Q >= W + (j+3)ceil(log2(R+1)) + O(1).                             (14)
```

The same bound with `j=0` supplies the complete Gauss factors and (9).

The theorem's error is not treated as bare `epsilon`. For a desired normalized
error `2^{-L}`, choose

```
epsilon = 2^{-C(L+log2(K+2)+log2(j+2)+1)^2},                      (15)
```

where the fixed effective constant `C` depends only on the declared
`A1,kappa1`. Then `A1*nu^kappa1*epsilon <= 2^{-L}`. Moreover
`nu=(j+1)log(K/epsilon)` remains polynomial in `j,L,log(K+1)`, and the declared
`A3*nu^2` working-bit bound remains polynomial. Rational phase preparation to
(14), arbitrary-precision exponentials, and logarithms therefore also have
polynomial bit cost.

For the final propagation, use certified complex balls. The elementary bounds

```
|q_k| <= m*ell^(k+1),
|1-lambda| >= 4/D   when lambda != 1
```

(the second follows from separation of distinct roots of unity) show that a
working precision

```
W = p + O((J+2)(log(m+1)+log(D+1)+log(J+2)+1))                   (16)
```

suffices for (11)--(12), including errors in `lambda`, the complete factors,
the moments, and their polynomial combinations. The hidden constant can be
made fixed by the displayed magnitude and recurrence bounds. Alternatively,
increase ball precision geometrically until every requested output radius is
at most `2^{-p}`; (16) bounds the number and size of these repetitions.

There are `O(J)` Hiary calls and polynomially many operations on numbers with
polynomially many bits. Euclidean gcd, modular inverse, Jacobi/Gauss parity
tests, exact binomial generation, and all recurrences have polynomial bit
cost. This proves the claimed deterministic bound in the bit lengths of
`m,D,a,b,c,s` and in the numerical values `J,p`.

There is one wording point. A literal bound polynomial in the ordinary binary
encoding lengths of `J` and `p` is impossible because the output alone has
order `J*p` bits. The statement explicitly says that `J` and `p` themselves
are counted. Under that output-sensitive (pseudopolynomial-in-their-binary-
encoding) reading, there is no remaining quantifier or bit-cost gap.
