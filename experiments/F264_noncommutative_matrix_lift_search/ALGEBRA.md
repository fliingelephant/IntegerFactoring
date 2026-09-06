# F264-D01 exact algebra and certificate rules

## Canonical matrix section

For an odd public integer `N`, let `[x]_N` be the least residue in
`{0,...,N-1}`. Apply it entrywise to matrices. For integer 2-by-2 matrices
`X,Y`, define

```text
z_XY = [X Y]_N,
K_N(X,Y) = (X Y-z_XY)/N.
```

Every entry of the numerator is exactly divisible by `N`. This is an integer
identity, not a coefficient congruence. Split the first carry again:

```text
k_N(X,Y) = [K_N(X,Y)]_N,
H_N(X,Y) = (K_N(X,Y)-k_N(X,Y))/N.
```

The implementation checks both divisions.

If `R` is the canonical representative modulo `N^2`, define

```text
r=[R]_N,    C=(R-r)/N.
```

Again the division is exact entrywise.

## Noncommutative associator

Put `z_uv=[uv]_N` and `z_vw=[vw]_N`. Associativity gives the exact ordered
matrix identity

```text
K(z_uv,w) + K(u,v) w = K(u,z_vw) + u K(v,w).
```

Replacing every `K` by `k+N H` shows that

```text
E = k(z_uv,w)+k(u,v)w-k(u,z_vw)-u k(v,w)
```

is exactly divisible by `N`, with

```text
E/N = -H(z_uv,w)-H(u,v)w+H(u,z_vw)+uH(v,w).
```

The order of all four products is part of the type. Commuting the factors is
not an allowed canonicalization.

## Determinant and Cayley--Hamilton lift quotients

Every source word is a product of exact determinant-one integer generators.
Its canonical representative `R` modulo `N^2` therefore satisfies

```text
det(R)-1 = 0 (mod N^2).
```

Thus `(det(R)-1)/N^2` is an exact public integer. For a 2-by-2 integer matrix,

```text
R^2-tr(R)R+det(R)I=0
```

exactly. Hence

```text
(R^2-tr(R)R+I)/N^2
```

is an exact integer matrix. It is a lift quotient; the unquotiented
Cayley--Hamilton residual modulo `N^2` is a global decoy.

## Commutators and Fricke carry

For a determinant-one residue matrix `R` modulo `N^2`, its adjugate is its
inverse modulo `N^2`. Define the ordered group commutator

```text
[A,B] = A B adj(A) adj(B)  (mod N^2).
```

For `x=tr(A)`, `y=tr(B)`, `z=tr(AB)`, the Fricke identity in `SL_2` is

```text
tr([A,B]) = x^2+y^2+z^2-x*y*z-2.
```

Canonical representatives therefore give an exact integer numerator

```text
F = tr([A,B])-x^2-y^2-z^2+x*y*z+2
```

divisible by `N^2`. `F/N^2` is the Fricke lift carry. `F mod N^2=0` is a
global character decoy and is never a word factor.

Trace cyclicity, `tr(W)=tr(W^-1)`, determinant multiplicativity, and
conjugacy invariance of trace and determinant are also global decoys.

## Minors and resultants

For ordered four-vectors `u,v`, every 2-minor is

```text
Delta_ij(u,v)=u_i*v_j-u_j*v_i,  0<=i<j<4.
```

For typed pairs `(s,p)` and `(t,q)`, the quadratic resultant template is

```text
Res2((s,p),(t,q))=(p-q)^2+(s-t)*(s*q-t*p).
```

This is the resultant of `X^2-sX+p` and `X^2-tX+q`, up to the fixed sign
convention above. Family determinants and finite differences use ordinary
integer addition and multiplication. Only explicitly named `N` or `N^2`
quotients may divide.

## Split certificate and exact common order

Let `G` be a determinant-one public matrix modulo `N` and

```text
Delta=tr(G)^2-4 det(G) (mod N).
```

The frozen root proposals are

```text
G00-G11, G01+G10, G01-G10,
C00-C11, C01+C10, C01-C10,
tr(C), and the matching public-conjugate coordinate differences.
```

Accept a proposal `s` only after exact modular verification

```text
s^2=Delta (mod N),   gcd(s,N)=1.
```

For every prime `r|N`, the characteristic polynomial then has two distinct
roots in `F_r`. Thus `G` is diagonalizable over `F_r`, and its order divides
`r-1`.

Let fully factored `A` satisfy `G^A=I mod N`. Starting at `m=A`, consider
each prime factor repeatedly. For `e=m/ell`, let

```text
g=gcd(N, all four entries of G^e-I).
```

If `g=N`, replace `m` by `e`. If `1<g<N`, output the factor. If `g=1`, no
hidden prime component returned, so retain that `ell`. At termination and in
the no-factor branch, `m` is the exact order in every hidden prime component.
Together with the split certificate this proves `m|r-1` for all `r|N`.
Unrelated accepted `m` values may be accumulated by lcm as in P197.

The conjugated diagonal controls have a known split root, but their order is
the scalar order of `u`; they are tagged `cyclic_control` and excluded from a
claim of noncommutative progress.

## N-primitive words and P205

For a nonzero exact atom `a`, define its public primitive part by repeatedly
dividing by `N` while exact division is possible. Its gcd with `N` is unchanged
after all global `N` powers are removed, except that the excluded zero atom
would otherwise produce the false word zero.

Family products and synthesized expressions can be evaluated modulo any
positive modulus. Modular evaluation preserves the gcd with that modulus. In
particular, for P205 residuals `s_p,s_q`, the residues of `V^n` determine
`gcd(V^n,s_p)` and `gcd(V^n,s_q)` exactly. Factor labels are permitted only in
this final scoring function.
