# Blind reconstruction of HALF-BOX COUNT modulo eight

## Scope and verdict

This reconstruction uses only `STATEMENT_ONLY.md` and the two declared black
boxes P238 and P242. It does not use a candidate proof, implementation, ledger,
or an earlier carry-transport derivation.

The claims are correct. In particular, the formulas handle arbitrary positive
odd `N`, including the negative values that can occur among the integers
`q_N(u)`. The floor-sum work needed for `J_nu` has an explicit Euclidean
recurrence below, so it does not hide an enumeration of the `R/2` odd points.

The SHA-256 of the input statement used for this reconstruction is

```text
c9c611f8148a365866a08212270731465d2d4244985b8610ffbcfee3be4f2fbe
```

## 1. The count is a binomial carry sum

Let `S` be the canonical odd residues in `[1,R)`. For `u in S`, write
`v=v_u` and `q=q_N(u)`, so

```text
u v = N + R q.
```

Let `x` be the canonical residue of `N/u` modulo `2R`. If `q` is even, then
`uv = N (mod 2R)`, hence `x=v`. If `q` is odd, then

```text
u(v+R) = N + R(q+u) = N (mod 2R),
```

because both `q` and `u` are odd. Hence `x=v+R`. Therefore

```text
C(N,2R) = #{u in S : q_N(u) is even}.
```

For every integer `q`, including every negative integer,

```text
1_(q even) = 1-q+2*binom(q,2)-4*binom(q,3)  (mod 8).       (1)
```

This needs no nonnegative-binomial convention. If the polynomial on the
right is `p(q)`, the polynomial identities

```text
binom(q+2,2)-binom(q,2) = 2q+1,
binom(q+2,3)-binom(q,3) = q^2
```

give

```text
p(q+2)-p(q) = -4q(q-1) = 0 (mod 8).
```

The values at `q=0,1` are `1,0`, so (1) follows for all integers by moving in
steps of two. Summing (1) gives the master identity

```text
C(N,2R) = phi-H_N+2B_N-4A_N  (mod 8).                     (2)
```

Thus only `H_N mod 8`, `B_N mod 4`, and `A_N mod 2` are needed.

## 2. The constants H_1 and B_1

For this section, put `N=nu=1`. Write

```text
v = u^(-1) mod R in [1,R),
q(u) = (uv-1)/R.
```

Consider the commuting involutions

```text
iota(u)=v,                 eta(u)=R-u.
```

They generate orbits on `S`. We have `q(iota(u))=q(u)`. Also the inverse of
`R-u` is `R-v`, and direct multiplication gives

```text
q(R-u) = q(u)+d,            d=R-u-v.                       (3)
```

Since `uv=1 (mod 4)`, the odd residues `u` and `v` are equal modulo four.
Consequently

```text
d = 2 (mod 4).                                                  (4)
```

There is no solution to `u^2=-1 (mod R)`, because odd squares are `1 mod 8`.
The involution `eta` also has no fixed point, since that would give
`u=R/2`, which is not odd.
The fixed points of `iota` are exactly the four roots of `u^2=1 (mod R)`:

```text
1, R-1, 1+R/2, R/2-1.                                         (5)
```

For an odd `u`, exactly one of `u-1` and `u+1` has 2-adic valuation one.
Thus `2^k | (u-1)(u+1)` forces the other factor to be divisible by
`2^(k-1)`, which gives precisely the four residues in (5).
All other orbits therefore have four elements

```text
{u,v,R-u,R-v}.
```

There are

```text
g = (phi-4)/4 = R/8-1                                         (6)
```

such orbits.

On a four-element orbit, the contribution to `H_1 mod 4` is

```text
2q+2(q+d) = 4q+2d = 0 (mod 4)
```

by (4). At the four fixed points (5), the `q` values are

```text
0, R-2, R/4+1, R/4-1.
```

Their sum is `R+R/2-2 = 2 (mod 4)`. Hence

```text
H_1 = 2 (mod 4).                                               (7)
```

For `B_1`, a four-element orbit contributes

```text
2 * (binom(q,2)+binom(q+d,2)).
```

The identity

```text
binom(q+d,2)-binom(q,2) = dq+binom(d,2)
```

and (4) show that the expression in parentheses is odd: `d` is even, while
`binom(d,2)` is odd for `d=2 mod 4`. Thus every four-element orbit contributes
`2 mod 4`.

For `R=8`, there are no four-element orbits. The four fixed-point `q` values
are `0,6,3,1`, and their binomial sum is `18 = 2 mod 4`.

For `R>=16`, the integer `g=2^(k-3)-1` in (6) is odd, so the four-element
orbits contribute `2 mod 4`. Put `s=R/4`, which is then divisible by four.
The fixed-point contribution is

```text
binom(R-2,2)+binom(s+1,2)+binom(s-1,2)
  = 3 + (s^2-s+1)
  = 0 (mod 4).
```

Therefore, uniformly for every `k>=3`,

```text
B_1 = 2 (mod 4).                                               (8)
```

## 3. Cubic binomial parity, including negative q_N

For every integer `q`,

```text
binom(q+4,3)-binom(q,3) = 2q^2+4q+4,
```

which is even. Evaluation at `q=0,1,2,3` therefore gives the all-integer rule

```text
binom(q,3) is odd  iff  q=3 (mod 4).                           (9)
```

Now use the involution on `S`

```text
tau(u) = nu*u^(-1) mod R in [1,R).
```

It satisfies `tau(tau(u))=u`, and `q_N(tau(u))=q_N(u)`. Every nonfixed pair
therefore cancels in `A_N mod 2`. A fixed point is exactly a solution of

```text
u^2 = nu (mod R).                                              (10)
```

The squaring map on the odd residue group modulo `2^k` has the four-element
kernel (5). Its image has `2^(k-3)` elements. Every odd square is `1 mod 8`,
and there are exactly `2^(k-3)` such residues, so its image is precisely the
set of residues equal to one modulo eight. Thus (10) has no solution unless
`nu=1 mod 8`, and it has exactly four solutions when `nu=1 mod 8`.

Assume first that `k>=4` and `nu=1 mod 8`. Choose one root `a` with
`1<=a<R/2`, and put

```text
t=(a^2-nu)/R.
```

The four roots are

```text
a, R-a, a+R/2, R/2-a.
```

For these roots, the four values `(u^2-nu)/R mod 4` are

```text
t, t+2, t+a, t-a,                                             (11)
```

because `R/4=0 mod 4`. Since `a` is odd, (11) contains every residue modulo
four exactly once. Since

```text
q_N(u) = (u^2-nu)/R-ell
```

at a fixed point, subtracting `ell` only permutes those four residues. Exactly
one fixed point has `q_N(u)=3 mod 4`.

For `k=3`, the condition forces `nu=1`; at `u=1,3,5,7`, the values
`(u^2-1)/8` are `0,1,3,6`, again all four residues modulo four. The same
conclusion follows after subtracting `ell`.

Combining this with (9) proves

```text
A_N = 1 (mod 2)  iff  N=1 (mod 8),                            (12)
```

because `N=nu mod 8` when `R` is divisible by eight. This proof explicitly
covers negative `q_N(u)`.

## 4. B_nu from P242 and degree-two floor sums

Let `w` run over the canonical odd residues, let `u_w` be its canonical
inverse modulo `R`, and put

```text
f(w)=floor(nu*w/R),        r_w=nu*w-R*f(w).
```

The integer `r_w` is the canonical odd residue of `nu*w`. For `u=u_w`, it is
therefore `v_u`. Using `w*u_w=1+R*q_1(w)` gives the exact transport identity

```text
q_nu(u_w) = nu*q_1(w)-u_w*f(w).                               (13)
```

The map `w -> u_w` permutes `S`, so expansion of
`2B_nu=sum_w(q_nu(u_w)^2-q_nu(u_w))` yields

```text
B_nu = nu^2*B_1 + ((nu^2-nu)/2)*H_1
       + K_nu/2 - nu*T_R(nu),                                 (14)

K_nu = sum_w (u_w^2*f(w)^2+u_w*f(w)).
```

Each summand of `K_nu` is even. Moreover, every odd residue is its own inverse
modulo eight. Hence

```text
u_w=w (mod 8),       u_w^2=1 (mod 8),
K_nu=J_nu (mod 8).                                             (15)
```

Each summand `f(w)^2+w*f(w)` of `J_nu` is also even, because it is
`f(w)^2+f(w) mod 2`. Therefore the canonical residue `j in {0,2,4,6}` of
`J_nu mod 8` can be divided by two, and `j/2` is the well-defined value of
`J_nu/2 mod 4`.

Insert (7), (8), and (15) into (14). Since `nu` is odd,

```text
nu^2*B_1 = 2 (mod 4),
((nu^2-nu)/2)*H_1 = nu*(nu-1) (mod 4).
```

P242 supplies the last term of (14) modulo four. Consequently

```text
b_nu = 2+nu*(nu-1)+J_nu/2-nu*T_R(nu)  (mod 4)
     = B_nu (mod 4).                                           (16)
```

### An explicit Euclidean recurrence for J_nu

No odd-point loop is required. For integers `n>=0`, `m>0`, and `a,b>=0`,
define the exact moment triple

```text
M(n;a,b,m) = (F,G,K),
y_x = floor((a*x+b)/m),       0<=x<n,
F=sum_x y_x,   G=sum_x y_x^2,   K=sum_x x*y_x.
```

Let

```text
X1=n(n-1)/2,        X2=n(n-1)(2n-1)/6.
```

First perform Euclidean quotient extraction

```text
a=q*m+a0,     b=s*m+b0,       0<=a0,b0<m.
```

If `M(n;a0,b0,m)=(F0,G0,K0)`, then the exact identities from
`y_x=q*x+s+z_x` are

```text
F = q*X1+s*n+F0,
G = q^2*X2+s^2*n+G0+2*q*s*X1+2*q*K0+2*s*F0,
K = q*X2+s*X1+K0.                                             (17)
```

It remains to handle `0<=a,b<m`. If `n=0`, `a=0`, or

```text
h=floor((a*(n-1)+b)/m)
```

is zero, the triple is zero. Otherwise, for `1<=t<=h`, let

```text
x_t=ceil((m*t-b)/a).
```

Counting the thresholds `y_x>=t` gives

```text
F = n*h-sum_t x_t,
G = n*h^2-sum_t (2t-1)*x_t,
K = h*X1-sum_t x_t(x_t-1)/2.                                 (18)
```

For `j=0,...,h-1`,

```text
x_(j+1) = floor((m*j+(m+a-1-b))/a).
```

Thus one recursive call

```text
M(h; m, m+a-1-b, a) = (F',G',K')
```

provides

```text
sum_t x_t=F',       sum_t t*x_t=K'+F',       sum_t x_t^2=G'.
```

Substitution in (18) gives

```text
F = n*h-F',
G = n*h^2-2*(K'+F')+F',
K = h*X1-(G'-F')/2.                                           (19)
```

The last division is exact term by term because `x_t^2-x_t` is even. After
the quotient extraction (17), the recursive modulus in (19) is `a<m`.
Hence this is the Euclidean algorithm and has `O(log m)` reciprocal steps.

The odd-index moments follow by subtracting the even indices. If

```text
(F1,G1,K1)=M(R; nu,0,R),
(F2,G2,K2)=M(R/2; nu,0,R/2),
```

then

```text
J_nu = G1+K1-G2-2*K2.                                         (20)
```

Indeed, at an even index `w=2x`,
`floor(nu*w/R)=floor(nu*x/(R/2))`. The recurrence can keep all moments exact;
they have `O(k)` bits here. Reducing (20) modulo eight at the end supplies the
required precision. Exact evaluation also avoids every modular division by
two or six in the polynomial sums.

## 5. Correction from nu to the full input N

For every `u`,

```text
q_N(u)=q_nu(u)-ell,       H_N=H_nu-phi*ell.                    (21)
```

The all-integer identity

```text
binom(q-ell,2)=binom(q,2)-ell*q+binom(ell+1,2)
```

therefore gives

```text
B_N = B_nu-ell*H_nu+phi*binom(ell+1,2)
    = B_nu-ell*H_N+phi*ell*(1-ell)/2.                          (22)
```

The final factor is an integer, and `phi=2^(k-1)` is divisible by four.
Consequently

```text
B_N = b_nu-ell*H_N (mod 4).                                   (23)
```

This is the required correction for the complete input, with no restriction
on the size or residue of `ell`.

## 6. H_N from the product

The map `u -> v_u` permutes `S`. Hence

```text
P_R^2 = product_u (u*v_u)
      = product_u (N+R*q_N(u)).
```

Since `R>=8`, every term containing at least two factors `R` is divisible by
`R^2`, hence by `8R`. Expanding only the surviving terms gives

```text
P_R^2 = N^phi+R*N^(phi-1)*H_N (mod 8R).                        (24)
```

Let `M=8R`, obtain `P_R mod M` from P238, and compute

```text
d = (P_R^2-N^phi mod M) in {0,...,M-1}.
```

Equation (24) proves that this canonical residue is divisible by `R`. Division
of (24) by `R` is then a congruence modulo eight. Since `N` is odd,
`N^(phi-1)` is invertible modulo eight, so

```text
H_N = (d/R)*N^(1-phi) (mod 8).                                (25)
```

The negative exponent in (25) means the odd modular inverse of
`N^(phi-1) mod 8`; it is not integer exponentiation with a negative exponent.

## 7. Final formula, guards, and bit complexity

Substitute (12), (16), (23), and (25) into (2):

```text
C(N,2R) = phi-H_N+2*(b_nu-ell*H_N)
          -4*1_(N=1 mod 8)                         (mod 8).
```

A uniform algorithm is therefore:

1. Check the system-boundary conditions `k>=3`, `N>0`, and `N` odd. Set
   `R=2^k`, `phi=R/2`, `nu=N mod R`, and `ell=(N-nu)/R`. Oddness guarantees
   that `nu` is a canonical odd integer in `[1,R)`, which is the domain needed
   by P242.
2. Evaluate the two exact moment triples in (20), reduce `J_nu` to its
   canonical residue modulo eight, check that it is even, and only then divide
   it by two modulo four.
3. Call P242 once for `T_R(nu) mod 4` and compute `b_nu` from (16).
4. Call P238 once modulo `2^(k+3)=8R`, namely at `k+3` bits of 2-adic
   precision. Square its result modulo `8R`, compute the canonical difference
   `d` in (25), check `R | d`, divide, and multiply by the odd inverse modulo
   eight.
5. Reduce `ell` modulo four where it multiplies `H_N`, evaluate the displayed
   final formula, and return its canonical residue in `{0,...,7}`.

The divisions by `R` and by two are guarded by proved divisibility. The
inverse is guarded by the input condition that `N` is odd. The exact divisions
inside the floor recurrence are ordinary integer identities.

P238 is called at `k+3` bits of 2-adic precision. P242 is called only at its
declared canonical input and only modulo four. Modular exponentiation of
`N^phi mod 8R` uses an exponent with `O(k)` bits and `O(k)` modular squarings;
the base is first reduced modulo `8R`. The Euclidean moment recurrence has
`O(k)` steps and uses integers with `O(k)` bits. Decomposing and reducing `N`
costs polynomial time in its binary length. Thus the total bit complexity is
polynomial in `k` and `log N` under the two declared black-box bounds.

No step evaluates the `R/2` graph points, computes an arbitrary interval
count, calls an exact-count or emptiness oracle, or factors an integer.
