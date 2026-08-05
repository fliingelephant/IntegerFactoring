# F10-autkill: fixed-degree cubic automorphism kill test

## Narrow conclusion

For a squarefree cubic, the proposed order-2 and order-3 local asymmetries are real and occur with constant probability. The missing algorithmic step is not the size of an automorphism base: under the clean order-asymmetry promises, finding any nonidentity order-filtered automorphism is Las Vegas polynomial-time equivalent to factoring the semiprime. Ordinary resultants or quotient-rank tests do not remove this step, because all three factorization types have the same geometric automorphism locus; they differ only in which geometric automorphisms descend to the local finite field.

This is a narrow obstruction to the natural cubic order-filter implementation of B1, not an impossibility theorem for all fixed-degree ring-automorphism constructions.

## Local classification and probabilities

Let `k=F_l`, let `f` be a monic squarefree cubic, and let `E=k[X]/(f)`. Over an algebraic closure, `E` is three points and its geometric automorphism group is `S_3`. Arithmetic Frobenius acts on those points by a permutation `pi` whose cycle type is the factorization type of `f`. Therefore

`Aut_k(E) = C_{S_3}(pi)`,

so the three cases are

| factorization type | Frobenius cycle | local automorphism group | nonidentity involutions | nonidentity order-3 elements |
|---|---|---|---:|---:|
| `(111)` | identity | `S_3` | 3 | 2 |
| `(12)` | transposition | `C_2` | 1 | 0 |
| `(3)` | 3-cycle | `C_3` | 0 | 2 |

The exact counts of monic squarefree cubics over `F_l` are

`#(111)=l(l-1)(l-2)/6`, `#(12)=l^2(l-1)/2`, and `#(3)=(l^3-l)/3`.

After division by the total `l^2(l-1)`, their conditional probabilities are

`P_l(111)=(l-2)/(6l)`, `P_l(12)=1/2`, and `P_l(3)=(l+1)/(3l)`.

For independently uniform coefficients modulo `N=pq`, conditional on squarefreeness at both primes:

- order-3 existence differs with probability exactly `1/2`;
- order-2 existence differs with probability

  `(4pq+p+q-2)/(9pq) > 4/9`.

For odd `l`, the quadratic character of the discriminant is the sign of the Frobenius permutation. Thus `(Delta/l)=-1` exactly in type `(12)`. A unit cubic discriminant has Jacobi symbol `-1` exactly when order-3 existence differs across `p` and `q`. A raw random monic cubic reaches this promise with probability

`(p-1)(q-1)/(2pq)`,

so the expected number of raw samples is at most `15/4` for distinct odd primes. A proper gcd of the discriminant already factors `N`; a discriminant vanishing at both primes can simply be rejected.

Therefore a solver for the order-3 automorphism promise would factor every distinct-odd-semiprime by a Las Vegas reduction with constant expected sampling overhead. Merely generating or recognizing the opposite local order pattern is easy; constructing the selective automorphism is the full remaining task.

## Exact coefficient equations

Write

`f(T)=T^3+uT^2+vT+w`, `R=A[X]/(f)`, `A=Z/NZ`, and `y=a+bX+cX^2`.

Reduction by `X^3=-uX^2-vX-w` gives `y^2=D_0+D_1X+D_2X^2`, where

`D_0=a^2-2wbc+uwc^2`,

`D_1=2ab-2vbc+(uv-w)c^2`,

`D_2=b^2+2ac-2ubc+(u^2-v)c^2`.

Writing `y^3=E_0+E_1X+E_2X^2`, exact multiplication gives

`E_0=aD_0-w(bD_2+cD_1)+uwcD_2`,

`E_1=aD_1+bD_0-v(bD_2+cD_1)+(uv-w)cD_2`,

`E_2=aD_2+bD_1+cD_0-u(bD_2+cD_1)+(u^2-v)cD_2`.

The substitution `sigma(X)=y` defines an `A`-algebra endomorphism exactly when

`E_0+uD_0+va+w=0`,

`E_1+uD_1+vb=0`,

`E_2+uD_2+vc=0` modulo `N`.

The matrix with columns `1,y,y^2` has determinant

`J=bD_2-cD_1=b^3-2ub^2c+(u^2+v)bc^2-(uv-w)c^3`.

The endomorphism is an automorphism exactly when `J` is a unit, equivalently `gcd(J,N)=1`; as a polynomial system this can be written with one extra variable `z` and equation `zJ-1=0`.

For the order constraints, put

`Q_0=a+ab+cD_0`, `Q_1=b^2+cD_1`, `Q_2=bc+cD_2`.

Then `sigma^2(X)=Q_0+Q_1X+Q_2X^2`, so `sigma^2=1` is exactly

`Q_0=0`, `Q_1=1`, `Q_2=0`.

Likewise `sigma^3=1` is exactly

`Q_0+aQ_1+D_0Q_2=0`,

`bQ_1+D_1Q_2=1`,

`cQ_1+D_2Q_2=0`.

For prime order 2 or 3, inequality of `(a,b,c)` from `(0,1,0)` makes the order exact. The exhaustive artifact also contains the fully expanded equations.

## Factoring equivalence of the natural search problem

Let `N=pq` be a product of distinct odd primes, and suppose `f` has unit discriminant.

For the order-3 promise, assume exactly one local type is `(12)`. On that side `Aut=C_2`, so the only automorphism satisfying `sigma^3=1` is the identity. Any globally nonidentity solution therefore satisfies

`a=0`, `b-1=0`, `c=0`

modulo exactly that prime, while at least one of those three differences is nonzero modulo the other prime. Taking the three gcds with `N` and skipping `1` and `N` returns a factor. Verification and extraction use only a constant number of ring operations and gcds on `O(log N)`-bit integers.

Conversely, the factors let one factor the fixed cubic over each local field in expected polynomial bit complexity. Use the identity on the `(12)` side. On a `(3)` side, `X -> X^l mod f` is a nonidentity order-3 Frobenius; on a `(111)` side, interpolate a 3-cycle of the roots. CRT-lift the three coefficients. This is Las Vegas polynomial in `log N` because the degree is fixed. Hence this order-3 automorphism search and factoring are mutually reducible on the promise.

The order-2 promise is analogous: if exactly one local type is `(3)`, its `C_3` automorphism group has no nonidentity involution, so every global nonidentity involution is component-selective and exposes a gcd. Given the factors, use an involution on the `(12)` or `(111)` side and identity on the `(3)` side.

## Why resultants do not supply the missing descent

Over an algebraic closure, the order-dividing-3 locus is always the same three-point set `{1,(123),(132)}`. Frobenius conjugation fixes all three points for types `(111)` and `(3)`, but a transposition swaps the two nonidentity cycles in type `(12)`, leaving only the identity rational. Its finite etale coordinate algebra has geometric rank 3 in every case.

Similarly, the order-dividing-2 locus is always the same four-point set consisting of the identity and the three transpositions. Its geometric rank is 4 in every case; the numbers of rational points are 4, 2, and 1 for types `(111)`, `(12)`, and `(3)`.

Consequently, intrinsic quotient-algebra ranks and resultants or subresultants that test only geometric nonemptiness or degree see no factorization-type drop. A nongeneric coordinate projection can have accidental collisions, but the local type supplies no guaranteed geometric degree mismatch. Elimination can produce a constant-degree modular root problem; selecting a local rational point, or mixing the identity component at one prime with a nonidentity component at the other, is precisely the hidden CRT-idempotent problem. A procedure that performs this descent is already a factoring procedure by the gcd argument above.

## Small-base counterexamples

The image of `X` is indeed a base of size one, but it ranges over `|R|=N^3=2^{Theta(log N)}` values. Base size gives uniqueness after an image is known; it does not enumerate the image. Even a constant-size automorphism group can be sparsely hidden in an exponential ambient set.

The smallest distinct-odd-semiprime audit used `N=15` and the lexicographically first found example `f=X^3+X+1`. Its types are `(12)` modulo 3 and `(3)` modulo 5. There are exactly 6 automorphisms among 3375 coefficient tuples. The nonidentity order-3 images are

`X -> 6+X+9X^2` and `X -> 9+13X+6X^2`,

and their coefficient differences from the identity expose the factor 3.

Away from characteristics 2 and 3, `N=35` and `f=X^3+2` give types `(12)` modulo 5 and `(3)` modulo 7. There are exactly 6 automorphisms among 42875 coefficient tuples. The two nonidentity order-3 maps are simply

`X -> 11X` and `X -> 16X`.

For a scalar image, the equations reduce to `b^3=1 mod 35`. Both nontrivial roots satisfy `gcd(b-1,35)=5`. Thus even after special structure shrinks the ambient search from `N^3` tuples to `N` scalars, locating a nontrivial root is already factoring-equivalent.

The named source, all failed and successful runs, logs, and outputs are recorded in `RUN_MANIFEST.md`.
