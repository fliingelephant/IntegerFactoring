# F23 kill-first result: canonical small-degree isogeny neighbors

**Status:** candidate, proof-only kill-first result. No computation was run.

**Classification:** method failure for the natural fixed-small-degree mechanism consisting of (i) special CM `j`-data, (ii) the coarse modular polynomial alone, and (iii) either a public fixed orientation or a public-exponent imitation of local Frobenius. This is not an impossibility theorem for every isogeny construction.

## Closest prior route and material difference

The closest prior routes are:

- F03/P05--P08: a low-degree polynomial can expose a factor once its local gcd degrees differ, but a cycle-sign mismatch is only a Jacobi-minus-one promise, uniform linear probes are exponentially sparse, and replacing the two local Frobenius exponents by `N` can erase the mismatch.
- F05/P09: a true geometric rank mismatch need not survive blind substitution of `N` for the unknown local characteristic.

The present route differs materially because the polynomial is the modular polynomial

\[
\Phi_\ell(j,Y),
\]

and a root is intended to represent a degree-\(\ell\) isogeny neighbor. This introduces a new distinction absent from the two closest routes:

1. a root of the **coarse** `j`-polynomial;
2. an actual cyclic subgroup or isogeny over the base;
3. a choice of one branch of that level structure.

At special CM points these three notions separate. The coarse polynomial can have an easy public root which does not represent a descended isogeny over a local field. Once the requested output is strengthened enough to be an actual CRT-inconsistent cyclic subgroup, it is already a factor witness.

## 1. Exact fixed-\(\ell=2\) CM identities

Use the classical normalization

\[
\begin{aligned}
\Phi _2(X,Y)={}&X^3+Y^3-X^2Y^2
+1488XY(X+Y)-162000(X^2+Y^2)\\
&+40773375XY+8748000000(X+Y)
-157464000000000.
\end{aligned}
\]

Direct substitution and expansion give the two integer identities

\[
\Phi _2(0,Y)=(Y-54000)^3
\tag{1}
\]

and

\[
\Phi _2(1728,Y)
=(Y-1728)(Y-287496)^2.
\tag{2}
\]

Thus the two most natural rational CM values already have completely public, characteristic-independent coarse neighbor values:

- at `j=0` there is only one coarse neighbor value, with multiplicity three;
- at `j=1728` there is a public simple value and a public double value.

Outside the finite, explicitly known set of primes dividing the constants and the root differences, their distinct-root patterns do not depend on the unknown prime factor of `N`.

There is an analogous \(\ell=3\) warning at the other extra-automorphism point:

\[
\Phi _3(0,Y)=Y(Y+12288000)^3
\tag{3}
\]

in the classical normalization. The ramified CM self-neighbor is the public root `0` and the other three geometric kernels collapse to one coarse `j`-value. Hence increasing from \(\ell=2\) to \(\ell=3\) does not repair the loss of level structure at this first special point.

## 2. The fine \(2\)-isogeny data on the `j=1728` twist family

Let `R=\mathbb Z/N\mathbb Z` with `2A` a unit, and consider

\[
E_A:y^2=x^3+Ax.
\tag{4}
\]

Every such curve has `j(E_A)=1728` and has the public order-two point

\[
P_0=(0,0).
\]

The other geometric order-two points have \(x\)-coordinates satisfying

\[
Q_A(T)=T^2+A=0.
\tag{5}
\]

The quotient by \(\langle P_0\rangle\) has a model

\[
y^2=x^3-4Ax
\]

and again has `j=1728`. If `s^2=-A`, translate `x=u+s`. The cubic becomes

\[
u^3+3su^2-2Au.
\]

The standard degree-two quotient formula for

\[
y^2=u^3+au^2+bu
\]

is

\[
y^2=u^3-2au^2+(a^2-4b)u.
\]

With `a=3s` and `b=-2A`, its `j`-invariant is `287496`. This also proves the branch interpretation of (2):

- the public kernel `x=0` maps to the simple root `1728`;
- the two nonzero geometric kernels map to the double root `287496`.

The double coarse root need not correspond to an isogeny defined over the ground field. In odd characteristic, a cyclic subgroup of order two descends if and only if its unique nonidentity point descends. Hence the double branch descends over \(\mathbb F_r\) exactly when

\[
\left(\frac{-A}{r}\right)=1.
\tag{6}
\]

Nevertheless `287496` remains a literal root of the coarse polynomial (2) in every good characteristic. The modular polynomial has therefore forgotten the descent datum needed by the proposed mechanism.

## 3. Exact factoring equivalence of an inconsistent fine branch

The following promise problem is the precise natural branch-selection task.

### Selective \(2\)-neighbor promise

The input is

\[
N=pq,
\]

where `p` and `q` are distinct odd primes, together with a unit `A mod N` such that

\[
\left(\frac{-A}{N}\right)=-1.
\tag{7}
\]

Return an `R`-valued cyclic subgroup of `E_A[2]` different from the public subgroup in at least one CRT component. In the model (4), equivalently return

\[
u(u^2+A)=0\pmod N,
\qquad u\not\equiv0\pmod N.
\tag{8}
\]

### Theorem

Solving this promise in Las Vegas polynomial time is randomized-polynomial-time equivalent to factoring distinct odd semiprimes.

### Proof: a selective neighbor gives a factor

Because `A` is a unit and the Jacobi symbol is negative, the two Legendre symbols in (6) are opposite. Relabel so that `Q_A` is irreducible over \(\mathbb F_p\) and split over \(\mathbb F_q\).

Over \(\mathbb F_p\), the only root of

\[
T(T^2+A)
\]

is `0`. Therefore every output satisfying (8) obeys

\[
u\equiv0\pmod p,
\qquad
u\not\equiv0\pmod q.
\]

Consequently

\[
\gcd(u,N)=p.
\tag{9}
\]

The output is efficiently checked by (8), and the gcd has deterministic polynomial bit complexity.

If the oracle instead returns the codomain `j` together with a verifiable descended isogeny, then its local values are `1728` on the nonsplit side and `287496` on the selected nonzero side. Hence

\[
\gcd(j'-1728,N)
\]

or

\[
\gcd(j'-287496,N)
\]

is a proper factor after the finite known bad primes have been removed.

### Proof: factors construct a selective neighbor

Given `p,q`, determine which side splits using the Legendre symbols. On the split side, compute a square root of `-A` by a standard Las Vegas finite-field square-root algorithm. CRT-combine that nonzero root with `0` on the nonsplit side. This gives (8). All numbers have `O(log N)` bits and the work is polynomial in `log N`.

### Reduction from arbitrary distinct odd semiprimes

Given an arbitrary `N=pq` with distinct odd primes, sample uniform `A mod N`. A proper gcd `gcd(A,N)` already factors. Conditional on `A` being a unit, the two local signs \(\left(\frac{-A}{p}\right)\) and \(\left(\frac{-A}{q}\right)\) are independent fair bits, so (7) occurs with probability `1/2`. Invoke the promise solver only then.

The raw probability of reaching the promise without an earlier factor is

\[
\frac{(p-1)(q-1)}{2pq},
\]

which is bounded below by a positive absolute constant for odd `p,q`. Random-bit generation, Jacobi symbols, verification, CRT, square roots in the converse, and gcds all have polynomial bit complexity. Thus the expected number of trials is constant.

This is exactly the quadratic Jacobi-sign bottleneck of P07, now expressed as the descent of a nonpublic \(2\)-isogeny. The isogeny language supplies no cheaper branch-selection step.

## 4. Why the coarse modular-polynomial root problem is too weak

Equation (2) gives two pure public roots in `R`:

\[
j'_0=1728,
\qquad
j'_1=287496.
\]

Therefore an algorithm asked only for **some** root of

\[
\Phi _2(1728,Y)=0\pmod N
\]

can always return a public integer constant. It learns nothing about `A`, even though the twist `E_A` controls whether the corresponding nonzero kernels descend locally.

In particular:

- symmetric information about the root multiset is public and synchronized;
- distinct-root counts of the coarse specialization do not equal counts of rational cyclic subgroups;
- a pure occurrence of the double root need not come with an isogeny over the base;
- requiring an actual isogeny or kernel restores the missing information, but Section 3 shows that the inconsistent output is already factoring-equivalent.

This closes the most literal interpretation “compute one root of \(\Phi_\ell\) and call it a canonical isogeny neighbor.”

## 5. Exact good-prime certificate at `N=143`

The distinction above is visible without any bad characteristic or root collision. Set

\[
N=143=11\cdot13,
\qquad
A=1,
\qquad
E:y^2=x^3+x.
\]

Both reductions are good. The polynomial `T^2+1` is irreducible modulo `11` and split modulo `13`. Thus there is one rational \(2\)-isogeny kernel modulo `11` and three modulo `13`.

The two roots in (2) remain distinct in both fields:

\[
1728\equiv12\pmod {143},
\qquad
287496\equiv66\pmod {143}.
\]

A factor-assisted mixed kernel is

\[
u=44,
\]

because `u=0 mod 11` and `u=5 mod 13`, while `5^2=-1 mod 13`. Indeed

\[
44(44^2+1)=85228=596\cdot143.
\]

It immediately exposes

\[
\gcd(44,143)=11.
\]

The corresponding mixed coarse neighbor is `j'=1 mod 143`: locally it is the simple root modulo `11` and the double root modulo `13`. Therefore

\[
\gcd(1-12,143)=11,
\qquad
\gcd(1-66,143)=13.
\tag{10}
\]

By contrast, the pure public value `66` is a root of the modular polynomial on both sides, even though its nonzero \(2\)-isogeny does not descend modulo `11`.

## 6. Public exponent `N` does not supply the missing Frobenius orientation

The same `N=143,A=1` example gives an exact obstruction to the natural exponent replacement. In the quadratic kernel algebra

\[
S_r=\mathbb F_r[T]/(T^2+1),
\]

one has `T^4=1`. Since `143=3 mod 4`,

\[
T^{143^i}-T=
\begin{cases}
-2T,&i\text{ odd},\\
0,&i\text{ even}
\end{cases}
\tag{11}
\]

over both local components.

The true local Frobenius tests at the first step differ:

\[
T^{11}-T=-2T
\quad\text{in }S_{11},
\qquad
T^{13}-T=0
\quad\text{in }S_{13}.
\tag{12}
\]

Thus the local rational-kernel mismatch is genuine, but every profile obtained by replacing the unknown characteristic powers with `N^i` is synchronized. Any canonicalization rule which sees the residual \(2\)-torsion only through the sequence (11) fails on this good-prime example.

This is the isogeny-neighbor incarnation of P06, not a new factoring algorithm.

## 7. Generic fixed-degree roots: symmetry versus a section

For fixed prime \(\ell\), the map

\[
X_0(\ell)\longrightarrow X(1)
\]

has generic degree `\ell+1` and is connected. Equivalently,

\[
\Phi_\ell(X,Y)
\]

is irreducible in \(\mathbb Q(X)[Y]\). Therefore there is no rational function `R(X) in \mathbb Q(X)` satisfying

\[
\Phi_\ell(X,R(X))=0.
\tag{13}
\]

So a fixed division-free formula, or a fixed rational formula using only inversions certified to be units, cannot select a generic isogeny neighbor: such a formula would be a rational section and would contradict irreducibility.

This statement is deliberately narrow. A bit algorithm may use input-dependent branching, exponent `N`, or other nonalgebraic operations, so (13) is not a lower bound against every polynomial-time algorithm. But the two most immediate escapes do not solve the problem:

- exponent `N` can erase the relevant local Frobenius data, as (11)--(12) show;
- branching on which local factorization type or root occurs is exactly the unknown CRT localization step.

For a generic specialization, the coefficients of \(\Phi_\ell(j,Y)\) provide only elementary symmetric functions of the neighbors. Its discriminant can expose a factor only when roots collide in one local component. For fixed \(\ell\), away from finitely many characteristics the discriminant is a fixed nonzero polynomial of bounded degree in `j`. A uniform random `j` therefore lands on a discriminant zero with probability at most

\[
O_\ell(1/p+1/q)
\]

on `N=pq`, exponentially small on balanced inputs. Deliberately solving the discriminant equation is a new root-selection problem, not a consequence of symmetric data.

Local root counts and factorization types are Frobenius fixed-point data on \(\mathbb P^1(\mathbb F_\ell)\). Computing them separately is the F03 problem. For \(\ell=2\) with one public kernel, the remaining factor is quadratic and the only first splitting bit is exactly (7). For larger fixed \(\ell\), resolvents may retain more cycle information, but no factor-free CRT localization follows merely from their symmetric coefficients.

## 8. CM orientation does not manufacture a factor orientation

Let \(\mathcal O_D\) be an imaginary-quadratic order and assume first that \(\ell\) does not divide its conductor. Horizontal \(\ell\)-isogenies correspond to invertible \(\mathcal O_D\)-ideals of norm \(\ell\):

- if \(\left(\frac D\ell\right)=-1\), there is no horizontal branch;
- if it is `0`, there is one ramified branch;
- if it is `+1`, there are two conjugate branches.

In the split case, orienting the two branches means choosing one of the two primes of \(\mathcal O_D\) above \(\ell\), equivalently one of the two roots of the public norm congruence modulo the fixed small \(\ell\). The data `D,\ell` are part of the construction. Hence the **ideal-class label** is public and the same label acts at every good prime factor of `N`. It is not an orientation of `p` versus `q`.

For class number greater than one, the starting CM point may reduce through different conjugate embeddings in the two CRT components. Applying the same ideal class can then give conjugate-looking outputs. That equivariance alone supplies neither a public reference branch nor a zero divisor. Constructing the initial mixed CM root, canonically comparing its conjugates, or using the class action to localize an embedding would be materially new and is not ruled out here.

If \(\ell\) divides the conductor, the ascending edge is distinguished by the known order inclusion when the CM order itself is supplied; the descending edges remain an automorphism/class-group orbit. Again, a characteristic-zero choice is synchronized. Asking the reduction Frobenius to choose among the orbit makes the rule depend on the unknown local prime.

At a good reduction prime `r`, ordinary versus supersingular behavior and rational descent are governed by the Frobenius of `r`. A mismatch between `p` and `q` can have constant density, but:

- its abelian quadratic shadow is a Kronecker/Jacobi sign promise;
- choosing the corresponding local branch requires the separate local sign or Frobenius class;
- CRT-combining different choices produces a zero divisor as in Section 3.

For primes dividing \(\ell D\), at inseparable characteristics, or at primes where special CM roots coalesce, there are only finitely many public exceptional primes when `D,\ell` are fixed. Trial division or \(\gcd(N,\ell D C)\) handles them; they cannot yield an all-input factoring theorem. Supersingular extra endomorphisms and the extra automorphisms at `j=0,1728` create more root collisions and descent ambiguity, not a canonical factor orientation.

## 9. Terminal extraction and all-input scope

Every successful inconsistent-neighbor representation considered here contains a coefficient which is equal to a public branch in exactly one CRT component. In the usual integer-coordinate or rational-map representation, the certified extraction is a gcd with `N`. The isogeny degree is the fixed number \(\ell\), so it cannot itself equal an unknown prime factor. No direct non-gcd divisor output emerges from this mechanism.

The promise equivalence in Section 3 covers distinct odd semiprimes and is enough to block the claimed cheap selector: the route already hides factoring on that restricted class. It supplies no handling of:

- prime powers or repeated factors;
- even inputs;
- arbitrary products with more than two prime factors;
- primes and correctness of a complete recursion.

A genuine selector with an all-composite success theorem could be wrapped in the standard verified splitting recursion, but no such selector was constructed here. The natural fixed-CM modular-polynomial mechanism fails before the all-input analysis begins.

## 10. Exact conclusion and retry criterion

The natural mechanism is exhausted in the following precise sense:

1. At the standard small CM points, the coarse fixed-\(\ell\) neighbor values are public and synchronized; equations (1)--(3) are exact certificates.
2. The coarse modular polynomial can report a root even when the associated isogeny does not descend. Root-finding alone is therefore too weak.
3. A public CM ideal orientation is global and synchronized, not factor-selective.
4. An actually descended CRT-inconsistent \(2\)-neighbor is randomized-polynomial-time factoring-equivalent on a Jacobi-recognizable promise.
5. Replacing local Frobenius by exponent `N` can erase the mismatch even at good primes.
6. A fixed rational generic selector would be a nonexistent rational section of \(X_0(\ell)\to X(1)\).

A retry is materially new only if it supplies at least one of:

- a fully specified factor-free selector for **fine** level structure, not merely a root of the coarse modular polynomial, together with a proof that it does not assume the local Frobenius or an equivalent root oracle;
- an \(N\)-dependent orientation invariant not reducible to a Jacobi/cycle-type promise and not erased by the opposite-factor exponent;
- a nonalgebraic generic-selection mechanism escaping the no-section argument, with inverse-polynomial separation and uniform bit complexity;
- a genuinely non-gcd representation whose output norm or integer invariant is proved to be a proper factor;
- complete treatment of ordinary, vertical, horizontal, ramified, supersingular, prime-power, repeated-factor, even, and arbitrary-composite cases.

Merely evaluating \(\Phi_2(0,Y)\), \(\Phi_2(1728,Y)\), or \(\Phi_3(0,Y)\); selecting a public CM ideal above fixed \(\ell\); returning any coarse root; or using `N` in place of the local Frobenius is not a materially new retry.
