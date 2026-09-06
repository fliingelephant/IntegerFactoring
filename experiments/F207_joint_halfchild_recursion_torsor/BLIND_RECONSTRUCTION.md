# Blind reconstruction of F207

## Provenance and verdict

This reconstruction used only the repository-root `PROMPT.md` and this
experiment's `STATEMENT.md`. Before reading the statement, its SHA-256 hash
was verified as

```text
d3ca187a62f3706749cbe3f0083c25dccf7b82b21edf3c514377b2cc839c0774
```

**Verdict: PASS.** The three stated theorems follow, with the exact-square
subcase made explicit below. The result is a conditional recursion theorem
and a local-information obstruction. It is not the all-input factoring
algorithm required by the root prompt.

## 1. The decrement spine recurrence

Fix (0<\rho<1). Suppose that, outside a fixed base range,

\[
 T(n)\le T(n-1)+Q(n)T(r(n))+Q(n),
 \qquad
 r(n)\le \lceil\rho n\rceil+c,
\]

where (T\ge 0), (Q) is nondecreasing, and

\[
 1\le Q(n)\le 2^{C(\log_2(n+1))^k}
\]

for fixed (C>0) and integer (k\ge1).

Choose a fixed number (\alpha) with (\rho<\alpha<1), for example
(\alpha=(1+\rho)/2). Since

\[
 \lceil\rho m\rceil+c\le \rho m+c+1,
\]

the base range can be enlarged to a fixed (b\ge1) such that

\[
 r(m)\le \lfloor\alpha m\rfloor<m
 \quad\text{for all }m>b.
\]

This absorbs the additive (O(1)) in the side-child size; no asymptotic
assumption about it is being suppressed.

Define the monotone envelope

\[
 S(n)=\max_{0\le j\le n}T(j),
 \qquad W(n)=S(n)+1,
 \qquad A=S(b).
\]

For (b<j\le n), telescope the one-step recurrence down the unique
decrement spine:

\[
\begin{aligned}
T(j)
&\le T(b)+\sum_{m=b+1}^{j}Q(m)\bigl(T(r(m))+1\bigr)\\
&\le T(b)+jQ(j)\bigl(S(\lfloor\alpha j\rfloor)+1\bigr)\\
&\le A+nQ(n)W(\lfloor\alpha n\rfloor).
\end{aligned}
\]

The same last bound also dominates the fixed base values after increasing
the fixed constant. Consequently,

\[
 W(n)\le (A+2)nQ(n)W(\lfloor\alpha n\rfloor)
 \qquad(n>b).
\]

Let (n_0=n) and (n_{i+1}=\lfloor\alpha n_i\rfloor), and stop at the
first (h) for which (n_h\le b). Since (n_i\le\alpha^i n),

\[
 h=O(\log(n+1)),
\]

where the implied constant depends only on (\alpha). Iteration gives the
coarse but sufficient estimate

\[
 W(n)
 \le W(b)\bigl((A+2)nQ(n)\bigr)^h.
\]

Put (L=\log_2(n+1)). Because (k\ge1),

\[
 \log_2\bigl((A+2)nQ(n)\bigr)
 \le C_1L^k
\]

for a fixed (C_1). Multiplying this by (h=O(L)) proves that a fixed
(D) exists with

\[
 \log_2 W(n)\le D L^{k+1}.
\]

Thus

\[
 \boxed{T(n)\le 2^{D(\log_2(n+1))^{k+1}}}.
\]

This proof accounts for both additive terms: the (+c) in the side-child
size is absorbed when (\alpha) is chosen, and the additive (+Q(n)) work
is the (+1) inside the telescoped summand.

If there are a fixed number of side children, all of size at most
(\rho n+O(1)), their sum replaces (T(r(n))) by a fixed multiple of the
same monotone envelope. Multiplying (Q) by a fixed constant preserves its
quasipolynomial form. A quasipolynomial number or weight of such calls can
likewise be included in (Q). A quasipolynomial postprocessor is absorbed
by the additive term.

## 2. Application to the balanced recursion geometry

Let

\[
 n=\lceil\log_2(N+1)\rceil,
 \qquad K=(N-1)/2.
\]

Since (N+1\le2^n),

\[
 K+1=(N+1)/2\le2^{n-1}.
\]

Therefore (K) has at most (n-1) bits. This is the sole near-size child
and forms the decrement spine.

For (B=\lfloor\sqrt N\rfloor) and (E=N-B^2),

\[
 0\le E<(B+1)^2-B^2=2B+1\le2\sqrt N+1.
\]

Hence (E) has at most (n/2+O(1)) bits. If (N=pq) with
(p<q<2p), then (p<\sqrt N) and (q<2\sqrt N). Both (p) and (q)
also have at most (n/2+O(1)) bits.

Thus a recursion node that factors (K), factors (E), and recursively
completes the two balanced parent-output factors has one child of size at
most (n-1) and a fixed number of children of size at most
(n/2+O(1)). The preceding theorem bounds this recursion by a numerical
quasipolynomial whenever its remaining work is quasipolynomial.

The balance condition is essential to this accounting. On an arbitrary
input, a small factor can leave a cofactor with (n-O(1)) bits. That
cofactor and (K) are then two independent near-size recursive children.
The resulting recurrence can have the shape

\[
 T(n)\le2T(n-1)+\cdots,
\]

which the one-spine theorem does not bound by a quasipolynomial. In
particular, this argument does not turn a balanced-branch postprocessor into
an all-input factoring algorithm.

## 3. Constructing the joint CRT root

Let (N>1) be odd and set

\[
 B=\lfloor\sqrt N\rfloor,
 \qquad K=(N-1)/2,
 \qquad E=N-B^2.
\]

First compute (d=\gcd(E,N)). If (1<d<N), this is already a proper
factor. If (d=N), then (E=0): indeed (0\le E<N), so (N\mid E)
forces (E=0). In that case (N=B^2), and the exact integer square root
(B) is a proper divisor. This is the exact-square subcase implicit in the
square-gap exit. Hence it remains to consider

\[
 \gcd(E,N)=1.
\]

Also

\[
 \gcd(K,N)=1,
\]

because any common divisor divides (N-2K=1). Given complete
factorizations of (K) and (E), form

\[
 M=\operatorname{lcm}(K,E).
\]

It follows immediately that

\[
 \gcd(M,N)=1.
\]

For each prime power (\ell^a\Vert M), let
(a=\max(v_\ell(K),v_\ell(E))) and prescribe

\[
 R_\ell\equiv
 \begin{cases}
 1\pmod{\ell^a},&v_\ell(K)\ge v_\ell(E),\\
 B\pmod{\ell^a},&v_\ell(E)>v_\ell(K).
 \end{cases}
\]

In the first case, (\ell^a\mid K), so

\[
 N=2K+1\equiv1=R_\ell^2\pmod{\ell^a}.
\]

In the second case, (\ell^a\mid E=N-B^2), so

\[
 N\equiv B^2=R_\ell^2\pmod{\ell^a}.
\]

The prime-power moduli are pairwise coprime. The Chinese remainder theorem
therefore constructs a unique (R\pmod M) satisfying all local
prescriptions, and

\[
 \boxed{R^2\equiv N\pmod M}.
\]

Since (N) is a unit modulo (M), this congruence also makes (R) a unit
modulo (M).

This construction has deterministic polynomial bit complexity in the bit
length of (N). The supplied child factorizations directly give all prime
powers and valuations. Their lists can be merged to form the lcm. Moreover,
(M\le KE), so (M) has (O(n)) bits. Integer square root, gcd, modular
reduction, extended gcd, and CRT on (O(n))-bit integers all take
polynomial bit complexity. No further factoring operation is hidden in the
construction.

## 4. The inverse torsor and its size

Write

\[
 U=(\mathbb Z/M\mathbb Z)^\times.
\]

For every (u\in U), define

\[
 (x,y)=(Ru,Ru^{-1}).
\]

Then

\[
 xy=R^2\equiv N\pmod M.
\]

Conversely, suppose that (x,y\in U) and (xy\equiv N\pmod M). Since
(R\in U), the value

\[
 u=R^{-1}x
\]

is uniquely determined. Then (x=Ru), and

\[
 y\equiv Nx^{-1}\equiv R^2(Ru)^{-1}=Ru^{-1}\pmod M.
\]

Thus the map is a bijection and

\[
 \boxed{(x,y)=(Ru,Ru^{-1}),\qquad u\in U}
\]

is the exact normal form of every product-consistent ordered unit pair.
There are exactly (\lvert U\rvert=\varphi(M)) such pairs.

For completeness, the stated elementary lower bound holds for every
positive integer (m). From (m=\prod p^a),

\[
 \frac{\varphi(m)^2}{m}
 =\prod_{p^a\Vert m}p^{a-2}(p-1)^2.
\]

The factor for (p^a=2) is (1/2). Every other prime-power factor is at
least (1): for (2^a) with (a\ge2) it is (2^{a-2}), and for odd
(p) it is already greater than (1) when (a=1) and only increases with
(a). Hence

\[
 \varphi(m)^2\ge m/2,
 \qquad
 \varphi(m)\ge\sqrt{m/2}.
\]

Since (M\ge K=(N-1)/2),

\[
 \boxed{\varphi(M)\ge\sqrt{M/2}\ge\frac{\sqrt{N-1}}2}.
\]

Thus the exact local state is not a short list: in terms of the input bit
length it can contain exponentially many product-consistent orientations.

## 5. Discriminant and inversion symmetry

For a torsor point,

\[
 x+y=R(u+u^{-1}).
\]

Using (R^2\equiv N\pmod M),

\[
\begin{aligned}
(x+y)^2-4N
&\equiv R^2\bigl((u+u^{-1})^2-4\bigr)\\
&=R^2(u-u^{-1})^2\pmod M.
\end{aligned}
\]

Therefore

\[
 \boxed{(x+y)^2-4N\equiv R^2(u-u^{-1})^2\pmod M}.
\]

The right side is the explicit square
([R(u-u^{-1})]^2). Hence both the product congruence and the
square-discriminant congruence accept every point of the inverse torsor.

Swapping the ordered factors gives

\[
 (Ru,Ru^{-1})\longmapsto(Ru^{-1},Ru),
\]

so factor swap is exactly

\[
 \boxed{u\longmapsto u^{-1}}.
\]

If (\chi:U\to\{\pm1\}) is any quadratic character, then

\[
 \chi(u^{-1})=\chi(u)^{-1}=\chi(u).
\]

Every symmetric ring expression in (x,y) is unchanged under the same
swap. Thus product, discriminant-square, quadratic-character, and symmetric
ring interfaces cannot distinguish the two orientations. This is a claim
about those interfaces only. Most torsor points need not be actual integer
factor pairs, and the theorem does not rule out an integer-size test, exact
division, a nonsymmetric Archimedean statistic, or a nonquadratic operation.

## 6. Predetermined support-prime Jacobi signs

Continue under the standing assumption (\gcd(E,N)=1), and now assume

\[
 N\equiv3\pmod4.
\]

Let (\ell) be an odd prime dividing (KE). It is coprime to (N): this
follows from (\gcd(K,N)=1) if (\ell\mid K), and from the standing
assumption if (\ell\mid E). Quadratic reciprocity for the Jacobi symbol
gives

\[
 \left(\frac{\ell}{N}\right)
 =(-1)^{\frac{\ell-1}{2}\frac{N-1}{2}}
  \left(\frac{N}{\ell}\right).
\]

Since (N\equiv3\pmod4), the integer ((N-1)/2) is odd. It remains only
to evaluate the Legendre symbol on the right.

If (\ell\mid K), then (N=2K+1\equiv1\pmod\ell), and therefore

\[
 \left(\frac{N}{\ell}\right)=1.
\]

If (\ell\mid E), then (N\equiv B^2\pmod\ell). Also
(\ell\nmid B), because otherwise (\ell\mid E) and (\ell\mid B)
would imply (\ell\mid N), contrary to (\gcd(E,N)=1). Hence (B^2)
is a nonzero square modulo (\ell), and again

\[
 \left(\frac{N}{\ell}\right)=1.
\]

In both cases,

\[
 \boxed{
 \left(\frac{\ell}{N}\right)
 =(-1)^{(\ell-1)/2}
 =\chi_4(\ell)}.
\]

The sign is therefore determined solely by the public residue of (\ell)
modulo (4). Products and prime powers supported on the supplied odd child
primes have Jacobi signs determined by the same public data. These signs
cannot supply a bit that selects which hidden orientation contains the
factor congruent to (1\pmod4).

The scope is exact: this calculation concerns odd primes in the support of
(KE). It says nothing about adaptive primes outside that support, symbols
with an unknown factor as denominator, higher-order characters, or
noncharacter information.

## 7. Genus-character consequence

In the stated class-group formulation, let the two mixed orientations be
represented by (C^2) and (C^{-2}). A genus character is a homomorphism

\[
 \gamma:\mathrm{Cl}\longrightarrow\{\pm1\}.
\]

Therefore

\[
 \gamma(C^2)=\gamma(C)^2=1,
 \qquad
 \gamma(C^{-2})=\gamma(C)^{-2}=1.
\]

For any fixed auxiliary class (A),

\[
 \gamma(AC^2)=\gamma(A)=\gamma(AC^{-2}).
\]

This holds for every genus character, so the two orientations have the same
genus vector even after composition with a fixed auxiliary class. Complete
factorization of (K) does not repair this quadratic genus gate.

Again, this conclusion is limited to genus characters, which are
quadratic. It does not identify the two classes under the full class group,
and it does not exclude nonquadratic class-group navigation.

## 8. Exact conclusion

The balanced recursion geometry is compatible with quasipolynomial total
work: one near-size decrement spine can carry quasipolynomially weighted
fixed-ratio side recursion. The factorizations of (K) and (E) also give,
in deterministic polynomial bit complexity, a joint modulus (M) and a
root (R^2\equiv N\pmod M).

Their complete joint product state is nevertheless the full inversion
torsor

\[
 \{(Ru,Ru^{-1}):u\in(\mathbb Z/M\mathbb Z)^\times\},
\]

whose size is at least (\sqrt{N-1}/2). Product, square-discriminant,
quadratic-character, support-prime Jacobi, symmetric-ring, and genus-vector
tests all preserve inversion. Closing a factoring postprocessor therefore
requires information outside the proved interface, such as a nonsymmetric
integer-size or exact-division statistic, a nonquadratic full-class-group
operation with a quasipolynomial rule, an adaptive factor-free transition,
or an integer-specific selector of the type named in the statement.

Nothing here proves that such a selector exists, and the unbalanced
two-near-child recurrence remains outside the theorem. Accordingly F207 is
valid partial progress but does not meet the root prompt's top-level success
criterion.
