# Blind reconstruction proof

## Scope and notation

Assume that the modulus is a positive odd integer. The nonempty case has
`N >= 3`. For a unit `c` in `1,...,N-1`, write `w(c)` for its least positive
inverse and

```text
P(c) = c*w(c) = 1 + kappa(c)*N.
```

Inversion is an involution: `w(w(c))=c`. Let `C_N` be the set of distinct
integer values `P(c)>1`. Thus, `C_N` is an exact-value projection, not a set
of inverse orbits.

For the kernel statements, let `A` be the binary valuation matrix. Its
columns are the values in `C_N`, its rows are all primes that divide those
values, and

```text
A[r,P] = v_r(P) mod 2.
```

A private row is a nonzero row of degree one.

## 1. Universal row-degree bound

Fix a prime `r`. Let

```text
D_r = {P in C_N : v_r(P) is odd}.
```

For each `P in D_r`, at least one inverse endpoint that realizes `P` is
divisible by `r`. Indeed, choose any `c` with `P(c)=P`. Since `r` divides
`c*w(c)`, Euclid's lemma gives `r | c` or `r | w(c)`. Both endpoints belong
to `1,...,N-1` and both realize the same exact value.

For each `P in D_r`, choose the least divisible endpoint among all endpoint
representations of `P`, and call it `phi(P)`. Then

```text
phi : D_r -> {r, 2r, ..., floor((N-1)/r)*r}.
```

This map is injective. If `phi(P)=phi(Q)=x`, the inverse of `x` is unique, so

```text
P = x*w(x) = Q.
```

Consequently,

```text
degree(r) = |D_r| <= floor((N-1)/r).
```

This argument does not assume that an exact product determines an inverse
orbit. For example, at `N=11`, the two inverse orbits `{2,6}` and `{3,4}`
both give the exact product `12`. The injection is defined on the projected
exact values. A duplicate representation therefore never creates another
domain element, and an endpoint cannot be assigned to two different exact
values.

## 2. Large rows are private

If `r>(N-1)/2`, then

```text
floor((N-1)/r) <= 1.
```

Thus, a present row has degree exactly one and is private in the complete
canonical universe `C_N`.

Here a source extension means adding more inverse endpoints for the same
fixed modulus, followed by exact-value projection. Such an extension is a
subset extension inside `C_N`. It cannot add a second odd column in this
row. Adding another representation of the existing exact value also does
not add a column. Hence a present private row stays private in every such
extension. This statement does not cover values outside the complete
canonical universe or a change of modulus.

## 3. Exact carry facts

The integer `kappa(c)` is nonnegative because `c*w(c)>=1`. Also,

```text
kappa(c) = (c*w(c)-1)/N < c*w(c)/N < c,
```

because `w(c)<N`. By symmetry, `kappa(c)<w(c)`. Therefore

```text
0 <= kappa(c) < min(c,w(c)).
```

Reducing `1+kappa(c)N=c*w(c)` modulo `c` gives

```text
kappa(c)N = -1 mod c.
```

For `c>=2`, multiplication by the inverse of `N` modulo `c` gives

```text
kappa(c) = -N^(-1) mod c.
```

The preceding bound puts `kappa(c)` in `0,...,c-1`, so it is the unique
representative in that interval. At `c=1`, `w(1)=1` and `kappa(1)=0`.
Standard number-theory notation does not define an inverse modulo `1`; the
display also covers `c=1` only if the unique residue modulo `1` is explicitly
declared to be `0`.

## 4. The seed-2 construction

Let `q>2` be prime and set `N=2q-1`. The modulus is odd, and

```text
2q = N+1 = 1 mod N.
```

Since `1<=q<N`, the least positive inverse of `2` is `q`. Hence

```text
P(2)=2q=N+1,   kappa(2)=1.
```

Because `q>2`, `v_q(2q)=1`. Moreover,

```text
q > q-1 = (N-1)/2.
```

Section 2 now shows that the `q` row is private in the complete canonical
universe.

The endpoint sign screens for this seed are

```text
gcd(q-2,N) and gcd(q+2,N).
```

Euclid's algorithm gives

```text
gcd(q-2,2q-1) = gcd(q-2,3),
gcd(q+2,2q-1) = gcd(q+2,5).
```

If `q=1 mod 30`, then `q-2=-1 mod 3` and `q+2=3 mod 5`.
Both gcds are therefore one.

Dirichlet's theorem supplies infinitely many prime values
`q=1 mod 30`, because `gcd(1,30)=1`. It says nothing here about the
factorization of the shifted number `2q-1`. In particular, it does not say
that `2q-1` is composite, semiprime, squarefree, or trial-hard.

The exact additional statement needed for the proposed infinite trial-hard
semiprime family is:

> There are infinitely many primes `q=1 mod 30` for which
> `2q-1=p_q*ell_q`, where `p_q` and `ell_q` are distinct primes and both are
> larger than `bit_length(2q-1)^2`.

This proof does not assert that statement.

## 5. Finite witness

### Exact arithmetic

Direct integer arithmetic gives

```text
1,000,289 * 2,000,309 = 2,000,887,089,301,
(2,000,887,089,301+1)/2 = 1,000,443,544,651.
```

Also,

```text
2^40 = 1,099,511,627,776
    < 2,000,887,089,301
    < 2,199,023,255,552 = 2^41.
```

Thus `n=41` and `n^2=1681`.

### Deterministic primality certificates

The primality proof uses the following Lucas criterion.

Let the complete factorization of `m-1` be
`product(s_i^e_i)`, where all `s_i` are already proved prime. If an integer
`a` satisfies

```text
a^(m-1) = 1 mod m
gcd(a^((m-1)/s_i)-1,m) = 1 for every distinct s_i,
```

then `m` is prime. To see this, let `t` be any prime divisor of `m`. The
order of `a mod t` divides `m-1`, but it does not divide `(m-1)/s_i` for any
`s_i`. Its order is therefore exactly `m-1`. Hence `m-1 | t-1`, so `t>=m`.
Since `t|m`, it follows that `t=m`.

Here is a complete recursive certificate. In the last column, an entry
`s:u/g` means

```text
u = a^((m-1)/s) mod m,
g = gcd(u-1,m).
```

For every row, direct repeated-squaring also gives
`a^(m-1) mod m = 1`. Every displayed `g` is `1`. The factorizations are
exact integer identities. The rows are in dependency order, starting from
the elementary prime `2`, so the criterion proves every listed `m` without
a probable-prime assumption.

| `m` | complete factorization of `m-1` | `a` | `s:u/g` |
|---:|:---|---:|:---|
| 3 | `2` | 2 | `2:2/1` |
| 5 | `2^2` | 2 | `2:4/1` |
| 7 | `2*3` | 3 | `2:6/1, 3:2/1` |
| 11 | `2*5` | 2 | `2:10/1, 5:4/1` |
| 17 | `2^4` | 3 | `2:16/1` |
| 31 | `2*3*5` | 3 | `2:30/1, 3:25/1, 5:16/1` |
| 41 | `2^3*5` | 6 | `2:40/1, 5:10/1` |
| 71 | `2*5*7` | 7 | `2:70/1, 5:54/1, 7:45/1` |
| 109 | `2^2*3^3` | 6 | `2:108/1, 3:63/1` |
| 127 | `2*3^2*7` | 3 | `2:126/1, 3:107/1, 7:4/1` |
| 3,049 | `2^3*3*127` | 11 | `2:3048/1, 3:2516/1, 127:3041/1` |
| 3,907 | `2*3^2*7*31` | 2 | `2:3906/1, 3:3844/1, 7:739/1, 31:3105/1` |
| 6,977 | `2^6*109` | 3 | `2:6976/1, 109:288/1` |
| 12,197 | `2^2*3049` | 2 | `2:12196/1, 3049:16/1` |
| 15,629 | `2^2*3907` | 2 | `2:15628/1, 3907:16/1` |
| 31,259 | `2*15629` | 2 | `2:31258/1, 15629:4/1` |
| 1,000,289 | `2^5*31259` | 3 | `2:1000288/1, 31259:738861/1` |
| 2,000,309 | `2^2*41*12197` | 2 | `2:2000308/1, 41:1579998/1, 12197:1076834/1` |
| 2,846,617 | `2^3*3*17*6977` | 5 | `2:2846616/1, 3:1157594/1, 17:320266/1, 6977:2160777/1` |
| 1,000,443,544,651 | `2*3^2*5^2*11*71*2846617` | 2 | `2:1000443544650/1, 3:885083396895/1, 5:753034618318/1, 11:686054863760/1, 71:86885813629/1, 2846617:471804960390/1` |

The last four relevant rows prove deterministically that

```text
p   = 1,000,289,
ell = 2,000,309,
r   = 1,000,443,544,651
```

are prime.

### Semiprime and seed properties

The primes `p` and `ell` are odd and distinct. Hence `N=p*ell` is an odd
distinct semiprime. Unique factorization also shows that it is not a perfect
power: its two prime exponents are both one, whereas all prime exponents in
an `e`-th power with `e>=2` are divisible by `e`.

Both factors exceed the trial threshold:

```text
1,000,289 > 1681,   2,000,309 > 1681.
```

Since `N=2r-1` and `r` is prime, Section 4 applies. The seed `2` has inverse
`r`, exact value `N+1=2r`, carry one, and `v_r(N+1)=1`. Its `r` row is private
in the complete exact-value universe.

Finally,

```text
r = 30*33,348,118,155 + 1.
```

Thus the sign-screen calculation in Section 4 applies and gives

```text
gcd(r-2,N)=1,   gcd(r+2,N)=1.
```

These are the two null endpoint sign screens.

## 6. Kernel and positive-root consequences

Suppose row `rho` is private and its unique `1` is in column `P_*`. For any
binary dependency `x in ker(A)`, the `rho` row equation is simply

```text
x[P_*] = 0.
```

Let `A'` be obtained by deleting row `rho` and column `P_*`. Restriction to
the remaining coordinates maps `ker(A)` into `ker(A')`. Conversely, if
`x' in ker(A')`, extend it by setting the deleted coordinate to zero. The
private row is then satisfied, and every other row is unchanged because the
deleted column has coefficient zero in the extended vector. Hence

```text
ker(A)  <-->  ker(A')
```

is a coordinate-preserving bijection.

For a dependency with selected surviving columns `S`, all prime valuations
in

```text
M_S = product(P for P in S)
```

are even. Thus `M_S=Y_S^2` for a unique positive integer `Y_S`. Also each
`P=1 mod N`, so `Y_S^2=1 mod N`. The kernel bijection selects exactly the
same set `S` on both sides. It therefore preserves the integer `M_S`, its
positive exact root `Y_S`, and the residue class `Y_S mod N`. No dependency
ever used `P_*` in the first place.

## 7. Separation of conclusions

For the finite witness, the seed-2 column has coefficient zero in every
binary dependency. Therefore `REUSE` is false if `REUSE` denotes the claim
that this seed column can occur in a binary dependency. This is the precise
self-contained content of the label.

One private row gives no conclusion about closure among the remaining
columns. At the level of binary matrices, both of the following are
compatible with a private first row:

```text
[1 0]        has trivial kernel.
[0 1]

[1 0 0]      has dependency (0,1,1).
[0 1 1]
```

Thus the private row only removes its one coordinate. It neither proves nor
disproves `CLOSE` for the surviving matrix.

Likewise, parity closure only proves `Y^2=1 mod N`; it does not determine the
root class. For example, with `N=15`, the canonical exact value `16` has
positive root `4`, a nontrivial square root of one modulo `15`, while the
canonical exact value `196` has positive root `14=-1 mod 15`. Both columns
have even valuation vectors by themselves. Hence closure can produce either
a useful nontrivial root class or a trivial one. No `ROOT` conclusion follows
from a private row, and no nontrivial-`ROOT` conclusion follows from closure
alone.

The labels `REUSE`, `CLOSE`, and `ROOT` are not formally defined in the
reconstruction statement. The conclusions above state the exact linear and
number-theoretic facts that can be certified without importing unstated
definitions.
