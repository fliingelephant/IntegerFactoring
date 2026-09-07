# Independent reconstruction of Claims A and B

Input: `RECONSTRUCTION_STATEMENT.md`

Input SHA256: `fab176d71fdcfa9983a8e6710242d404491b78b5a12c2decfbfda32a9c585954`

This reconstruction treats SUPPORT as the declared exact oracle. It makes no
claim about `support.py`, Algorithm 2, or the cited implementation results.

## Scope qualification

Claim B requires that `N` be composite. This is forced both by the phrase
"arbitrary composites" in the frozen statement and by the requested outcome:
for prime `N` there is no nontrivial factor point, so the literal assertion for
all integers `N >= 4` would be false. The proof below covers every composite
`N >= 4`, including prime powers, squares, and arbitrarily unbalanced
factorizations.

Throughout, a lower support normal `(lambda,1)` means minimization of

    f_lambda(x,y) = lambda*x + y.

## Preliminary facts

The real region `x,y > 0`, `xy >= N` is the epigraph of the strictly convex
function `N/x`. At `P=(p,q)`, where `pq=N`, the normal `lambda=q/p` uniquely
minimizes `f_lambda` on this real region. Indeed,

    (q/p)*x + y >= 2*sqrt((q/p)*x*y) >= 2q,

and equality forces `xy=N` and `(q/p)*x=y`, hence `(x,y)=(p,q)`.
Consequently, `P` is a vertex of the integer lower hull. Since `p,q >= 2`, it
is not either endpoint `(1,N)` or `(N,1)`, so it has the stated neighbors.

Every finite vertex of the lower hull has both coordinates at most `N`.
Points with first coordinate greater than `N` are dominated by `(N,1)`, and
points with second coordinate greater than `N` are dominated by `(1,N)`.
In particular,

    q+k <= N,    p+H <= N.                                      (1)

## Claim A

The edge `LP` has equality normal `lambda_plus=k/h`, and the edge `PR` has
equality normal `lambda_minus=K/H`. The interior of the normal cone at a
vertex consists exactly of the normals strictly between its two edge
normals. Thus, once `lambda_minus < lambda_plus` is established, every

    lambda_minus < lambda < lambda_plus

uniquely exposes `P`. This conclusion concerns the entire hull, not only the
two neighbor comparisons.

Membership of `L` and `R` in `S`, together with `pq=N`, gives

    (p-h)(q+k) >= pq,
    (p+H)(q-K) >= pq.

Each inequality has two useful rearrangements:

    k/h >= q/(p-h),       k/h >= (q+k)/p,                        (2)
    K/H <= q/(p+H),       K/H <= (q-K)/p.                        (3)

The second inequality in (2) is strict above `q/p`, and the second inequality
in (3) is strict below `q/p`. Hence

    lambda_minus < q/p < lambda_plus.                            (4)

Set

    r = lambda_plus/lambda_minus = k*H/(h*K),
    delta = r-1 > 0.

Using the first inequalities in (2)--(3) and then the second ones gives

    delta >= (h+H)/(p-h),
    delta >= (k+K)/(q-K).

Equivalently,

    delta*p >= r*h + H,
    delta*q >= r*K + k.

After multiplication and substitution of `r=kH/(hK)`,

    delta^2*N
      >= (r*h+H)(r*K+k)
       = r*(h+H)*(k+K).                                        (5)

The integer

    d = k*H-h*K

is positive by (4), so `d >= 1` and `delta=d/(hK)`. Multiplying (5) by
`delta` yields

    N*delta^3
      >= d*r*(1+H/h)*(1+k/K).                                  (6)

Put `a=H/h` and `b=k/K`. Then `ab=r`, and AM-GM gives

    (1+a)(1+b)
      = 1+a+b+ab
      >= (1+sqrt(r))^2
      >= 4*sqrt(r).

Since `d >= 1` and `r>1`, (6) implies

    N*(lambda_plus/lambda_minus-1)^3
      >= 4*d*r^(3/2)
      >= 4.

This proves Claim A without any balance assumption on `p` and `q`.

## Claim B

Assume now that `N` is composite, and choose any factorization `N=pq` with
`p,q >= 2`. Write

    A = lambda_minus,
    B = lambda_plus,
    t = N^(-1/3),
    c = 4^(1/3),
    M = Rgrid = 2^(4n).

By Claim A, `delta=B/A-1 >= c*t`. Since `N >= 4`, `c*t <= 1`. Therefore

    delta_0 = min(delta,1) >= c*t.                               (7)

The open interval

    J = (A, A*(1+delta_0))

is contained in `(A,B)`. It is also wholly inside the sampled range. In
fact, (1) and positivity give

    A = K/H > 1/N > 2^(-n),
    B = k/h < N < 2^n.                                          (8)

Partition the positive line into the half-open binary cells

    C_e = [2^e,2^(e+1)).

Let `2^e <= A < 2^(e+1)`. Because `delta_0 <= 1`, `J` meets at most `C_e`
and `C_(e+1)`. If their ordinary intersection lengths are `x` and `y`, with
an absent piece assigned length zero, then

    x+y = A*delta_0.

Normalize each length by the left endpoint of its cell. The sum of the two
normalized lengths is at least

    x/2^e + y/2^(e+1)
      >= (x+y)/2^(e+1)
      >= delta_0/2.

Thus one allowed cell has normalized intersection length at least

    ell >= delta_0/4.                                           (9)

The cell is allowed because (8) places every nonempty part of `J` in an
octave with `-n <= e <= n-1`.

Inside `C_e`, the sampled points are

    2^e*(1+u/M),    u=0,...,M-1.

An interval of normalized length `ell` contains at least `M*ell-1` points of
this mesh, regardless of whether either endpoint is a mesh point. Applying
this to the open interval `J` is precisely what excludes ties. From (7)--(9),
the number `m` of successful values of `u` for the selected exponent obeys

    m >= M*c*t/4 - 1.                                           (10)

It remains to check the one-point rounding loss exactly. Since `n` is the bit
length of `N`, `N < 2^n`; and `N >= 4` gives `n >= 3`. Hence

    M*t = 2^(4n)*N^(-1/3)
        > 2^(11n/3)
        >= 2^11.

Also `c>3/2`, because `(3/2)^3<4`. Therefore

    (c-1)*M*t/4 > 1,

so (10) gives the stronger bound

    m > M*t/4.                                                   (11)

There are exactly `2n*M` equally likely pairs `(e,u)`. Every one of the `m`
pairs counted in (11) has its normal strictly inside `(A,B)`. Claim A then
makes `P` the unique oracle answer, so the oracle tie convention is irrelevant.
Consequently,

    Pr[nontrivial factor point]
      >= m/(2n*M)
       > 1/(8*n*N^(1/3)),

which implies the stated weak lower bound.

The half-open cells also settle powers-of-two at octave boundaries: `2^e`
appears once as `u=0`, while the preceding cell has no `u=M`. Open endpoints
of the normal interval are never counted. The argument applies unchanged
when a neighbor is `(1,N)` or `(N,1)`, when `p=q`, and when one factor is `2`.
