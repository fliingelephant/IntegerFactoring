# Blind reconstruction of the direct Gauss-ranked FacRoot involution

Input: `STATEMENT.md`

Input SHA-256: `d672ba5f54f299aeb169692ebdcbd6e13f3690a600ec2d303344bd12a200dfa8`

This reconstruction uses only the candidate statement. It does not use a
candidate proof, report, implementation, ledger, or paper.

## Verdict

All stated conclusions reconstruct. In particular, the use of every residue,
including nonunits, is compatible with the composite-modulus Gauss parity
argument. The ranking and selection procedures are uniform polynomial-bit-time
algorithms and do not factor `N`. The final alternating-path argument gives only
an `O(d) = O(N)` evaluation bound; it does not give a polynomial- or
quasipolynomial-time factoring algorithm.

## 1. Composite-modulus Gauss parity

For `1 <= y <= h`, write

    rep(a y) = s_y pi(y),

where `s_y` is in `{+1,-1}` and `pi(y)` is in `{1,...,h}`. Multiplication by the
unit `a` permutes the nonzero residue classes. It also commutes with negation.
Consequently, `pi` is a permutation of `{1,...,h}`.

Let `M_a` be multiplication by `a` on all of `Z/NZ`, including zero. Order the
nonzero residues in the pairs `{y,-y}`. In the coordinates `(y,e)` with
`e in {+1,-1}`, the map is

    (y,e) -> (pi(y), e s_y).

The permutation of the `h` two-element blocks has sign `sgn(pi)^2=1`. Within a
block, the two elements are exchanged exactly when `s_y=-1`. Since zero is
fixed,

    sgn(M_a) = product_y s_y = (-1)^k,

where `k` is the number of `y` for which `rep(a y)<0`.

We now reconstruct Zolotarev's sign identity for an arbitrary odd composite
modulus:

    sgn(M_a on Z/NZ) = Jacobi(a,N).                 (1)

First let the modulus be an odd prime `p`. In `F_p`, the Vandermonde product of
the ordered list `a*0,a*1,...,a*(p-1)` is both `sgn(M_a)` times the original
Vandermonde product and `a^(p(p-1)/2)` times that product. The Vandermonde
product is nonzero. Euler's criterion therefore gives

    sgn(M_a) = a^((p-1)/2) = Legendre(a,p) in F_p.

Both sides are integers in `{+1,-1}`, so the equality holds as an equality of
signs.

For `p^e`, reduce `Z/p^e Z` modulo `p^(e-1)`. Each fiber has odd size `p`. A
permutation of the base lifts with sign equal to its base sign raised to the
fiber size, hence with the same sign. In coordinates on any one fiber,
multiplication by `a` is an affine permutation

    z -> a z + c  on F_p.

Translation has sign `+1`: a nonzero translation is a `p`-cycle, and `p` is
odd. Thus each fiber map has sign `Legendre(a,p)`. There are `p^(e-1)` fibers,
an odd number. If `sigma_e(a)` is the sign modulo `p^e`, this proves

    sigma_e(a) = sigma_(e-1)(a) Legendre(a,p)
               = Legendre(a,p)^e.

Finally, factor `N` mathematically as `product_j p_j^e_j` and apply the Chinese
remainder theorem. For permutations `sigma` and `tau` on finite sets `X` and
`Y`, respectively,

    sgn(sigma x tau) = sgn(sigma)^|Y| sgn(tau)^|X|.

All CRT factor sizes are odd, so their signs multiply. This proves (1), because
`product_j Legendre(a,p_j)^e_j` is `Jacobi(a,N)`. This factorization is only a
proof device. None of the algorithms below uses it.

It remains to identify `k` with `K(h)`. Write `a y=qN+r`, where
`1 <= r <= N-1`; the endpoints are excluded because `a` is a unit and
`1 <= y < N`. Then

    floor((a y+h)/N) - floor(a y/N) = floor((r+h)/N).

As `N=2h+1`, this is one exactly when `h+1 <= r <= 2h`, equivalently when
`rep(a y)<0`. Hence `k=K(h)`. The assumption `Jacobi(a,N)=+1` and (1) imply
that `K(h)` is even.

There are `h-K(h)` values `y` with `rep(a y)>0`. Therefore

    L = h-K(h),
    |D| = h+1+L = N-K(h) = d.

Since `N` is odd and `K(h)` is even, `d` is odd.

## 2. Closure and involution property of F

For a nonzero residue representative `x`, define the three signs

    alpha(x) = sign(x),
    beta(x)  = sign(rep(a x)),
    gamma(x) = sign(rep(x^(-1)))

when `x` is a unit. Because `a` is a unit, none of the quantities whose sign is
used is zero. The definition of `D` is equivalently

    x in D  iff  x>0, or x<0 and beta(x)<0.          (2)

Indeed, for `x=-y<0`, `rep(a y)>0` is equivalent to `rep(a x)<0`.

The cases `0 <-> 1` are closed in `D` and square to the identity. Every nonzero
nonunit is fixed before an inverse is requested, so this case is also closed
and involutive. It remains to consider a unit `x != 1`.

### First unit branch

Suppose `x>0` and `w=rep(x^(-1))>0`. Then `w` is in `D`. Its inverse has
representative `x>0`, so the first branch applies to `w` and returns `x`.
Also, `w != 1`, since otherwise `x=1`.

### Second unit branch

Suppose `beta(x)<0` and `gamma(x)<0`, and put

    z = rep(a^(-1) x^(-1)).

The defining congruences give

    rep(a z)      = rep(x^(-1)),
    rep(z^(-1))   = rep(a x).

Both representatives on the right are negative. If `z>0`, membership in `D`
is automatic; if `z<0`, the first equality and (2) give membership. Thus the
second branch is closed. At `z`, both its `beta` and `gamma` signs are negative,
so the same branch applies and returns

    rep(a^(-1) z^(-1)) = x.

The element `z` cannot be `1`, because `rep(z^(-1))=rep(a x)<0`.

### Remaining unit branch

Suppose first that `x>0`. Failure of the first branch gives `gamma(x)<0`.
Failure of the second branch then gives `beta(x)>0`. For `z=-x`, both relevant
signs reverse:

    z<0, beta(z)<0, gamma(z)>0.

Thus `z` belongs to `D` by (2), satisfies neither of the first two branch
conditions, and the remaining branch sends it back to `x`.

Suppose instead that `x<0`. Membership in `D` gives `beta(x)<0`. The first
branch is unavailable, and failure of the second branch gives
`gamma(x)>0`. Now `z=-x>0` is in `D` and has

    beta(z)>0, gamma(z)<0.

Again neither earlier branch applies, and the remaining branch returns `x`.

The branches are disjoint because the first requires `gamma>0` and the second
requires `gamma<0`. This proves that `F` is a well-defined involution on `D`.

## 3. Fixed-point decoder

Neither zero nor one is fixed. A fixed nonzero nonunit `x` yields

    gcd(x,N),

which is greater than one and less than `N`, since `0<|x|<N`.

Now let `x` be a unit fixed in the first unit branch. Then

    x^2 = 1 mod N.

The branch has `x>0`, and `x != 1`. Thus `gcd(x-1,N)<N`. If this gcd were one,
then `x-1` could be cancelled from `(x-1)(x+1)=0 mod N`, giving
`x=-1 mod N`. This is impossible for the positive representative
`1 < x <= h`. Hence `gcd(x-1,N)` is a proper nontrivial divisor.

If `x` is fixed in the second unit branch, then

    x = a^(-1) x^(-1) mod N,

so `a x^2=1 mod N`. Therefore `rep(x^(-1))` is a square root of `a` modulo
`N`.

The remaining branch cannot have a unit fixed point: `x=-x mod N` would imply
`x=0 mod N`, because `N` is odd.

The decoder uses a gcd, extended Euclid, modular multiplication, comparisons,
and the displayed branch tests. All have deterministic running time polynomial
in `log N`. It does not factor `N` as a subroutine.

## 4. Exact rank, floor sums, and selection

The summand in `K(t)` was shown above to be the indicator of
`rep(a y)<0`. Hence

    Q(t) = t-K(t)

is exactly the number of accepted values `y <= t`, where accepted means
`rep(a y)>0`. In particular, `L=Q(h)`.

Among negative elements of `D`, increasing signed order corresponds to
decreasing `y`: the elements before `-y` are exactly the accepted `u>y`.
Their number is `L-Q(y)`. All `L` negative elements precede the nonnegative
elements. Thus the stated map

    R(-y) = L-Q(y),
    R(x)  = L+x  for x>=0

is exactly the increasing-order, zero-based rank bijection from `D` to
`{0,...,d-1}`.

Here is an explicit Euclidean floor-sum algorithm. For nonnegative `n,a,b` and
positive `m`, let

    S(n,m,a,b) = sum_(i=0)^(n-1) floor((a i+b)/m).

The following loop returns `S` exactly. All divisions are Euclidean divisions
with nonnegative quotient and remainder.

```text
FloorSum(n,m,a,b):
    ans = 0
    loop:
        qa, a = divmod(a,m)
        qb, b = divmod(b,m)
        ans += qa*n*(n-1)/2 + qb*n

        Y = a*n+b
        if Y < m:
            return ans

        n, b = divmod(Y,m)
        m, a = a, m
```

To verify the nontrivial step, assume after normalization that
`0<a<m`, `0<=b<m`, and write `a n+b=q m+r`. When `q>0`, count the lattice
points under the line first by `i` and then by the positive height `j`. For
`1<=j<=q`, reverse the order with `k=q-j`. The number of allowed `i` is

    n-ceil((m j-b)/a) = floor((m k+r)/a).

Summing gives the exact transposition identity

    S(n,m,a,b) = S(q,a,m,r),

which is the final three assignments in the loop. If `a=0`, then `Y=b<m` and
the algorithm has already returned. Successive transpositions perform the
Euclidean algorithm on the modulus and coefficient, so there are `O(log m)`
iterations. The intermediate values have polynomially many bits. Thus this is
a deterministic polynomial-bit-time algorithm.

The needed prefix count is

    K(t) = S(t,N,a,a+h) - S(t,N,a,a),                (3)

because the index `i=0,...,t-1` corresponds to `y=i+1`. Formula (3) computes
`Q(t)`, `L`, and `d` without factoring.

For inverse rank, if `i>=L`, return `x=i-L`. If `i<L`, put `k=L-i` and find the
least `y in [1,h]` with `Q(y)>=k` by binary search. The function `Q` is
nondecreasing, starts at zero, ends at `L`, and each increment is either zero
or one. Therefore the selected `y` is accepted and satisfies `Q(y)=k`; return
`-y`. Binary search makes `O(log N)` calls to (3), so both rank and inverse rank
run in deterministic time polynomial in `log N`.

Computing `F` uses only polynomial-bit-time gcd, extended-Euclidean, modular,
and sign operations. It follows that

    G = R composed_with F composed_with R^(-1)

is a uniform polynomial-bit-time involution on the explicit odd interval
`{0,...,d-1}`. A fixed point of `G` maps through `R^(-1)` to a fixed point of
`F`, and Section 3 decodes it to a proper divisor of `N` or a square root of
`a`. This is the claimed direct FacRoot-to-Lonely reduction. No auxiliary
parameter is used.

## 5. The two auxiliary matchings and the finite path bound

Let `r0=L`, the rank of `x=0`.

For the first matching, delete `L` from the ordered interval. Since `d` is odd,
the remaining list has even length. More explicitly, for `i != L` define

    c(i) = i      if i<L,       and c(i)=i-1 if i>L,
    u(j) = j      if j<L,       and u(j)=j+1 if j>=L.

Then

    A(L)=L,
    A(i)=u(c(i) XOR 1)  for i != L.

The compressed indices run from zero through `d-2`; because their count is
even, XOR with one pairs consecutive indices and stays in range. Hence this
`A` is an involution with the unique fixed point `L`. Its evaluation uses only
integer comparisons and additions on `O(log N)`-bit integers.

For the second matching, set

    A(i) = (2L-i) mod d.

This is an involution. A fixed point obeys `2(i-L)=0 mod d`. Since `d` is odd,
two is invertible modulo `d`, so the unique fixed point is again `L`. This
matching is also locally computable in polynomial bit time.

For either choice, form the two-colored multigraph on `{0,...,d-1}` whose
nonloop edges are the two-cycles of `G` and `A`. Every vertex other than an
`A`-fixed or `G`-fixed vertex has one edge of each color. The vertex `r0` has no
`A` edge. It does have a `G` edge, because

    G(r0) = R(F(0)) = R(1) = L+1 != L.

The connected component of `r0` is therefore a finite alternating path. Its
other endpoint cannot be another `A`-fixed vertex, because `r0` is the unique
one. Thus the other endpoint is fixed by `G`.

Starting at `r0`, evaluate `G`, then `A`, then `G`, and so on. Stop when a `G`
evaluation returns its input. The walk visits no vertex twice before stopping;
otherwise its component would contain a cycle attached to the degree-one
endpoint `r0`. The component has at most `d` vertices, so at most `d-1` moving
edge evaluations plus the final fixed-point check are required. This is an
`O(d)` local-evaluation bound.

Because `d` can be of order `N`, this last bound is exponential in the input
bit length in general. It is only the asserted finite-path guarantee and gives
no shorter factoring bound.
