# F10/X11 hostile audit: corrected cubic automorphism theorem

## Verdict

The central order-3 theorem passes. The local classification, exact counts and probabilities, discriminant/Jacobi criterion including characteristic 3, coefficient equations, determinant criterion, selective-gcd argument, reverse construction, fixed-degree bit complexity, geometric ranks, rational descent, and the `N=15` and `N=35` certificates are correct.

One quantifier must be narrowed. A solver for the Jacobi-recognizable **order-3** promise is Las Vegas polynomial-time equivalent to factoring distinct odd semiprimes. For **order 2**, the report proves only an instancewise equivalence on an already-promised input: every valid nonidentity involution factors that input, and known factors construct one. The constant probability of an order-2 mismatch does not by itself permit calls to a promise-only solver, because the mismatch is not recognized by the discriminant/Jacobi bit and the solver has no required behavior or running time off promise.

The geometric calculation also supports only a precise rank obstruction: invariants depending solely on geometric nonemptiness or geometric degree/rank cannot distinguish the three local types. It is not a theorem that every possible resultant, subresultant, projection, or elimination invariant fails.

## Narrowest corrected theorem

Let `k=F_l`, let `f(T)=T^3+uT^2+vT+w` be squarefree, and let `E=k[T]/(f)`. Let `(111)`, `(12)`, and `(3)` denote its three possible factor-degree patterns. For `r=2,3`, write

`S_r(E)={sigma in Aut_k(E): sigma^r=id}`.

Then:

1. The local groups and order loci are

   | type | `Aut_k(E)` | `|S_2(E)|` | `|S_3(E)|` |
   |---|---:|---:|---:|
   | `(111)` | `S_3` | 4 | 3 |
   | `(12)` | `C_2` | 2 | 1 |
   | `(3)` | `C_3` | 1 | 3 |

2. Among monic squarefree cubics over `F_l`, the exact type probabilities are

   `P_l(111)=(l-2)/(6l)`, `P_l(12)=1/2`, and `P_l(3)=(l+1)/(3l)`.

3. Let `N=pq` for distinct odd primes and sample the three nonleading coefficients uniformly modulo `N`. Conditional on squarefreeness modulo both primes, the order-3 mismatch probability is `1/2`, while the order-2 mismatch probability is

   `(4pq+p+q-2)/(9pq)>4/9`.

   The raw probabilities are

   `P_raw(order-3 mismatch)=(p-1)(q-1)/(2pq)`

   and

   `P_raw(order-2 mismatch)=(p-1)(q-1)(4pq+p+q-2)/(9p^2q^2)`.

4. If the discriminant `Delta` is a unit modulo `N`, then

   `Jacobi(Delta,N)=-1`

   exactly when the order-3 existence pattern differs across `p` and `q`. Hence rejection sampling produces a certified order-3 promise with raw probability `(p-1)(q-1)/(2pq)` and expected cost at most `15/4` samples. A proper `gcd(Delta,N)` already factors `N`; `gcd(Delta,N)=N` is rejected.

5. On an order-3 promised instance, every globally nonidentity `sigma` with `sigma^3=id` exposes a factor through one of

   `gcd(a,N)`, `gcd(b-1,N)`, `gcd(c,N)`,

   where `sigma(X)=a+bX+cX^2`. Conversely, known factors construct such a `sigma` in expected polynomial time in `log N`. Therefore the certified order-3 promise search is Las Vegas polynomial-time equivalent to distinct-odd-semiprime factoring.

6. On an order-2 promised instance—exactly one local type is `(3)`—the identical gcd conclusion and reverse construction hold for a globally nonidentity involution. This gives factoring hardness on every promised input and a factoring-to-construction algorithm. It does **not**, without an additional off-promise guarantee, give a promise-preserving reduction from arbitrary semiprime factoring to the order-2 promise problem.

7. After base change to an algebraic closure, the schemes `S_3` and `S_2` have geometric ranks 3 and 4 for every factorization type. Their rational-point counts are respectively `(3,1,3)` and `(4,2,1)` for types `(111),(12),(3)`. This remains true in characteristic 3.

These statements obstruct only the natural cubic order-filter construction. They do not rule out other fixed-degree rings, richer certificates, or a different canonization/descent mechanism.

## Proof audit

### Local automorphisms

Over an algebraic closure, the finite étale algebra `E` becomes three labeled points. Its geometric automorphism group is `S_3`. If arithmetic Frobenius permutes the points by `pi`, a geometric permutation descends to `k` exactly when it commutes with `pi`. Thus

`Aut_k(E)=C_{S_3}(pi)`.

The Frobenius cycle types are exactly `(111)`, `(12)`, and `(3)`, whose centralizers are `S_3`, `C_2`, and `C_3`. Counting elements whose order divides 2 or 3 gives the table above. This proof applies in every characteristic for which `f` is squarefree, including characteristic 3.

### Exact counts and probabilities

The number of split cubics with three distinct roots is `binom(l,3)`. A type-`(12)` cubic is a choice of one linear root and one monic irreducible quadratic, giving

`l(l^2-l)/2=l^2(l-1)/2`.

The standard irreducible-polynomial count gives `(l^3-l)/3` irreducible cubics. Their sum is `l^2(l-1)`, the total number of monic squarefree cubics. Division gives the three conditional probabilities.

For order 3, the local positive types `(111)` and `(3)` together have conditional probability `1/2`; type `(12)` also has probability `1/2`. The exclusive-or probability across independent reductions is therefore `1/2`. Raw, each side of this dichotomy has probability `(l-1)/(2l)`, giving `(p-1)(q-1)/(2pq)`.

For order 2, local existence has conditional probability `(2l-1)/(3l)` and failure, type `(3)`, has probability `(l+1)/(3l)`. Taking the exclusive-or across `p,q` yields

`(4pq+p+q-2)/(9pq)`.

Multiplying by the probability `(p-1)(q-1)/(pq)` of squarefreeness at both primes gives the raw formula in the theorem.

At `l=3`, the exact raw counts are

| type | `(111)` | `(12)` | `(3)` | nonsquarefree |
|---|---:|---:|---:|---:|
| count among 27 cubics | 1 | 9 | 8 | 9 |

so the conditional probabilities are `1/18,1/2,4/9`. For the smallest pair `(p,q)=(3,5)`, the authoritative audit obtains

- order 3: conditional `1/2`, raw `4/15`, expected raw trials `15/4`;
- order 2: conditional `22/45`, raw `176/675`.

### Discriminant and Jacobi symbol, including `l=3`

Let `r_1,r_2,r_3` be the geometric roots and `V=prod_{i<j}(r_i-r_j)`. For odd `l`, Frobenius gives

`V^l=sign(pi)V`.

Since `Delta=V^2` and `V` is nonzero for a squarefree cubic,

`Delta^((l-1)/2)=V^(l-1)=sign(pi)`.

Thus the Legendre symbol of `Delta` is `-1` exactly for the transposition type `(12)`. This argument is valid at `l=3`; no division by 3 occurs. For `N=pq` and unit `Delta`, the Jacobi symbol is the product of the two local signs, so it is `-1` exactly when one and only one side is type `(12)`, which is exactly the order-3 mismatch.

The expected-trial upper bound follows from

`2pq/((p-1)(q-1)) <= 2*3*5/(2*4)=15/4`,

because distinct odd primes have smallest possible pair `3,5` and the expression decreases as either prime grows.

### Coefficient equations and invertibility

Let `A=Z/NZ`, `R=A[X]/(f)`, and `y=a+bX+cX^2`. Reduction by `X^3=-uX^2-vX-w` gives `y^2=D_0+D_1X+D_2X^2`, with

`D_0=a^2-2wbc+uwc^2`,

`D_1=2ab-2vbc+(uv-w)c^2`,

`D_2=b^2+2ac-2ubc+(u^2-v)c^2`.

Writing `y^3=E_0+E_1X+E_2X^2` gives

`E_0=aD_0-w(bD_2+cD_1)+uwcD_2`,

`E_1=aD_1+bD_0-v(bD_2+cD_1)+(uv-w)cD_2`,

`E_2=aD_2+bD_1+cD_0-u(bD_2+cD_1)+(u^2-v)cD_2`.

The substitution `X -> y` is an endomorphism exactly when

`E_0+uD_0+va+w=0`,

`E_1+uD_1+vb=0`,

`E_2+uD_2+vc=0`.

Its `A`-linear matrix has columns `1,y,y^2`; hence its determinant is

`J=bD_2-cD_1`

` =b^3-2ub^2c+(u^2+v)bc^2-(uv-w)c^3`.

An endomorphism of the free rank-three `A`-module `R` is invertible exactly when `J` is a unit, equivalently `gcd(J,N)=1`. The inverse-variable equation `zJ-1=0` represents the same open condition algebraically.

Put

`Q_0=a+ab+cD_0`, `Q_1=b^2+cD_1`, `Q_2=bc+cD_2`.

Then `sigma^2(X)=Q_0+Q_1X+Q_2X^2`, so, after the endomorphism and unit-determinant conditions,

`sigma^2=id` iff `Q_0=0,Q_1=1,Q_2=0`.

Likewise

`sigma^3=id`

iff

`Q_0+aQ_1+D_0Q_2=0`,

`bQ_1+D_1Q_2=1`,

`cQ_1+D_2Q_2=0`.

For prime `r=2` or `3`, these order-dividing equations plus `(a,b,c)!=(0,1,0)` imply exact order `r`. The nonidentity condition alone would not suffice without the endomorphism, invertibility, and order equations.

The audit derived these identities by polynomial remainder and matrix determinant, then compared every fully expanded expression in canonical `R06.json`. Every equality passed.

### Why every promised output exposes a gcd

CRT gives

`R = R_p x R_q`.

For the order-3 promise, suppose the `p`-side is type `(12)`. Its automorphism group is `C_2`, so its only solution of `sigma^3=id` is the identity. A globally nonidentity solution is therefore identity modulo `p` and nonidentity modulo `q`. In the basis `1,X,X^2`, this says

`a=0, b-1=0, c=0 mod p`,

while at least one of these three differences is nonzero modulo `q`. The gcd of that difference with `N` is exactly `p`. Swapping `p,q` gives the other orientation. This proves all coefficientwise gcd claims, including the fact that some individual gcds may be `N` and should be skipped.

For the order-2 promise, the type-`(3)` side has group `C_3` and only the identity satisfies `sigma^2=id`; the same proof applies.

### Reverse construction and bit complexity

Given `p,q`, factor the fixed cubic over each local field and classify its type.

- Order 3: use identity on the `(12)` side. On a `(3)` side, `X -> X^l mod f` is the nonidentity field Frobenius of exact order 3. On a `(111)` side, choose a 3-cycle of the three roots and interpolate the unique polynomial of degree at most 2 realizing that permutation.
- Order 2: use identity on the `(3)` side. On a `(12)` side, local Frobenius fixes the linear factor and swaps the two quadratic roots, so it is the required involution. On a `(111)` side, interpolate a transposition.

CRT-lift the three image coefficients. Fixed-degree finite-field factorization is Las Vegas expected polynomial time in `log l`; Frobenius powering takes `O(log l)` fixed-degree ring multiplications; interpolation uses a constant number of field operations; and CRT is polynomial in `log N`. The claimed expected bit complexity is therefore correct.

The characteristic-3 audit gives explicit constructions:

| type and polynomial over `F_3` | construction | image of `X` |
|---|---|---|
| `(111)`, `X^3-X` | interpolated 3-cycle | `1+X` |
| `(111)`, `X^3-X` | interpolated transposition | `1-X` |
| `(12)`, `X^3+X` | Frobenius | `-X` |
| `(3)`, `X^3-X+1` | Frobenius | `2+X` |

The first and fourth maps have order 3; the second and third have order 2.

### Geometric rank and rational descent

The automorphism **scheme** becomes the constant six-point `S_3` scheme after an algebraic closure, with Galois action by conjugation by `pi`. The order-dividing-3 subset is

`{id,(123),(132)}`,

and the order-dividing-2 subset is the identity plus the three transpositions. Their conjugation-orbit degrees are:

| type | order-dividing 3 | order-dividing 2 |
|---|---|---|
| `(111)` | `1+1+1` | `1+1+1+1` |
| `(12)` | `1+2` | `1+1+2` |
| `(3)` | `1+1+1` | `1+3` |

The sums give constant geometric ranks 3 and 4. The number of degree-one orbits gives rational-point counts `(3,1,3)` and `(4,2,1)`.

There is no characteristic-3 exception. A constant finite group scheme is étale even when its number of points is divisible by the characteristic. The order loci are unions of its geometric components, not copies of the nonreduced group scheme `mu_3`. Independently, A04 formed the coefficient ideals with `zJ-1`, computed dimension zero, and found radical quotient dimensions 3 and 4 for characteristic-3 representatives of all three types:

| type | representative | rank / rational points for `sigma^3=id` | rank / rational points for `sigma^2=id` |
|---|---|---:|---:|
| `(111)` | `X^3-X` | `3 / 3` | `4 / 4` |
| `(12)` | `X^3+X` | `3 / 1` | `4 / 2` |
| `(3)` | `X^3-X+1` | `3 / 3` | `4 / 1` |

Therefore quotient rank or geometric nonemptiness alone cannot see the local type. The arithmetic information lies in the Frobenius descent orbits.

## Independent finite certificates

### `N=35`

The fresh source independently searched coefficient triples, found `(u,v,w)=(0,0,2)` lexicographically first for the requested `(12)/(3)` orientation, and enumerated images by direct polynomial substitution and basis determinants. It did not use the canonical multiplication code.

For `f=X^3+2`, `Delta=-108` is a unit modulo 35. The local types are `(12)` modulo 5 and `(3)` modulo 7, with local automorphism counts 2 and 3. Exactly six global automorphisms occur:

| image coefficients `(a,b,c)` | order | `(gcd(a,35),gcd(b-1,35),gcd(c,35))` |
|---|---:|---|
| `(0,1,0)` | 1 | `(35,35,35)` |
| `(0,11,0)` | 3 | `(35,5,35)` |
| `(0,15,28)` | 2 | `(35,7,7)` |
| `(0,16,0)` | 3 | `(35,5,35)` |
| `(0,25,28)` | 6 | `(35,1,7)` |
| `(0,30,28)` | 6 | `(35,1,7)` |

The scalar cube roots modulo 35 are exactly `1,11,16`. Thus both nonidentity order-3 maps `X -> 11X` and `X -> 16X` expose 5 through `gcd(b-1,35)`.

### `N=15`

The fresh source also recovered `(u,v,w)=(0,1,1)` as the lexicographically first requested orientation. It found six automorphisms. The unique order-2 image `(5,11,0)` exposes 5, while the order-3 images `(6,1,9)` and `(9,13,6)` expose 3. This independently confirms every small-example gcd claim.

## Scope leaks and required wording changes

1. **Order-2 promise equivalence.** The order-2 mismatch predicate, “exactly one local type is `(3)`,” is not determined by the discriminant/Jacobi sign. Constant raw or conditional density does not authorize calls to an algorithm whose correctness or running time is guaranteed only on promised inputs. The safe statement is the instancewise result in item 6 of the theorem. A full randomized factoring reduction would additionally require a total polynomial-time routine with controlled off-promise behavior, or a separately proved promise-preserving/dovetailed reduction.

2. **Resultants and elimination.** Constant geometric rank refutes only tests that depend solely on geometric nonemptiness or degree/rank. It does not quantify over every resultant, subresultant, coordinate projection, or elimination construction. The report's qualified sentence at `REPORT.md:120` is sound; the broader shorthand “ordinary resultants do not remove this step” at `REPORT.md:5` should be read only in that qualified sense.

3. **“Same geometric locus.”** The three order loci are geometrically isomorphic after choosing a labeling of the roots. They are not literally the same embedded coefficient locus for different polynomials `f`. Only the abstract ranks and permutation sets are type-independent.

4. **Projection universality.** The claim that no nongeneric projection can give a guaranteed mismatch is plausible from the twisting picture but is not formalized or proved for a specified class of projections. What is proved is that the intrinsic full-scheme ranks do not drop.

5. **Scalar `N=35` language.** The `N=35` enumeration is a finite certificate, not by itself a uniform complexity equivalence for every scalar cube-root problem. Uniform factor extraction holds on the separate promise that a nontrivial cube root is identity at exactly one prime component. The general coefficientwise order-3 theorem supplies the relevant uniform statement.

No other scope leak or algebraic error was found. In particular, characteristic 3 requires no exclusion, the identity is correctly included in `sigma^3=id`, global nonidentity correctly forces selectivity under either exact mismatch promise, and every displayed coefficient and probability formula passed.

## Reproducibility

The authoritative named source is `audit_cubic_automorphisms.sage`; the decisive output is `output/A04.json`; the exact command, timeout, log, hashes, one failed-run disposition, and superseded successful runs are in `RUN_MANIFEST.md`.
