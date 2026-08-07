# Inverse-pair endpoint parity

## Setup

Let

\[
U_N=\{u\in\{1,\ldots,N-1\}:\gcd(u,N)=1\},
\]

and let \(\iota(u)\) be the member of \(U_N\) congruent to \(u^{-1}\pmod N\). Since \(\iota^2\) is the identity, its orbits have size one or two. A size-one orbit is a label \(z\) such that

\[
z=\iota(z),\qquad z^2\equiv1\pmod N.
\]

Call an occurrence \((z,z)\) a loop. Treat repeated submitted pairs as distinct occurrences.

Fix any realized finite batch, adaptive or not, and a selected subset \(S\) of its occurrences. For each label \(u\), let \(n_u(S)\) be the number of selected endpoints labeled \(u\). The formal endpoint-parity condition is

\[
n_u(S)\equiv0\pmod2\quad\text{for every }u.
\]

Therefore the visible product is the exact integer square

\[
P(S)=\prod_{j\in S}a_jb_j
     =\prod_{u\in U_N}u^{n_u(S)}
     =X(S)^2,
\qquad
X(S)=\prod_{u\in U_N}u^{n_u(S)/2}.
\]

Also, every submitted pair satisfies \(a_jb_j\equiv1\pmod N\). Hence

\[
X(S)^2=P(S)\equiv1\pmod N.
\]

Adaptivity does not affect this argument: it applies pointwise after the finite batch has been realized.

## Orbit-by-orbit decoding

Consider first a two-element inversion orbit \(\{u,v\}\), where \(v=\iota(u)\ne u\). Every occurrence supported on this orbit has one endpoint labeled \(u\) and one labeled \(v\), irrespective of its orientation. If \(m\) such occurrences are selected, then

\[
n_u(S)=n_v(S)=m.
\]

Formal endpoint parity forces \(m=2k\). This orbit's contribution to the integer root, reduced modulo \(N\), is

\[
u^{m/2}v^{m/2}=(uv)^k\equiv1.
\]

Thus every two-element inversion orbit contributes exactly \(1\) to \(X(S)\bmod N\).

For a fixed point \(z=\iota(z)\), each selected loop \((z,z)\) adds two occurrences of the label \(z\). It therefore satisfies endpoint parity by itself. If \(\ell_z\) copies of that loop are selected, its contribution to the root is \(z^{\ell_z}\). Consequently

\[
X(S)\equiv\prod_{z\in L_{\rm loop}}z^{\ell_z}\pmod N,
\]

where \(L_{\rm loop}\) is the set of self-inverse labels actually submitted as loops. In particular,

\[
X(S)\bmod N\in H:=\langle z:z\in L_{\rm loop}\rangle\le U_N.
\]

Since every generator has square \(1\), only the parity of each \(\ell_z\) matters. Products of loops can produce a root that was not itself a submitted label. For example, modulo \(15\), both \(4\) and \(14\) are self-inverse, while

\[
4\cdot14\equiv11\pmod{15}.
\]

Thus selecting the loops \((4,4)\) and \((14,14)\) gives the new root value \(11\), even though the only submitted loop labels were \(4\) and \(14\). This is exactly why the conclusion is membership in the generated subgroup, not membership in the submitted set.

Repeated nonloop pairs have a different behavior. In the endpoint multigraph, two parallel occurrences between \(u\) and \(\iota(u)\) form a length-two cycle vector over \(\mathbb F_2\); any even collection of parallel occurrences is a sum of such vectors. These are genuine vectors in the formal cycle space. But a selection of \(2k\) such edges decodes to

\[
(u\iota(u))^k\equiv1\pmod N.
\]

The inversion involution has no orbit of length greater than two, so nonloop components contain only two vertices and parallel edges. Their formal cycle vectors cannot produce a nontrivial decoded root.

## Direct screening of every loop

Let \(z\) be any submitted loop label. Then \(z^2\equiv1\pmod N\), so

\[
N\mid(z-1)(z+1).
\]

Compute

\[
d_-:=\gcd(z-1,N),\qquad d_+:=\gcd(z+1,N).
\]

Because \(N\) is odd, \(\gcd(z-1,z+1)\mid2\) implies that no prime divisor of \(N\) divides both factors. More precisely, if \(p^e\mathrel\Vert N\), then \(p^e\) divides exactly one of \(z-1\) and \(z+1\): it must divide at least one because it divides their product, and the odd prime \(p\) cannot divide both. Thus each complete prime-power divisor of \(N\) is assigned to exactly one of \(d_-\) and \(d_+\), and

\[
\gcd(d_-,d_+)=1,qquad d_-d_+=N.
\]

There are now only two cases.

1. Both sides receive at least one prime-power divisor. Then \(1<d_-<N\) and \(1<d_+<N\), so either gcd is a proper factor of \(N\).
2. All prime-power divisors go to one side. Then that gcd is \(N\), and \(z\equiv1\pmod N\) or \(z\equiv-1\pmod N\). The other gcd is \(1\).

This proof does not assume that \(N\) is squarefree. In particular, for an odd prime power \(N=p^e\), the whole power \(p^e\) must divide one of \(z-1\) and \(z+1\), so every self-inverse unit is already globally \(+1\) or \(-1\).

Screen each distinct submitted loop label in this way. If any screen returns a proper gcd, it factors \(N\). On the branch where no screen returns a proper factor, every submitted loop label is globally \(+1\) or \(-1\) modulo \(N\). The orbit formula then gives, for every formal pool,

\[
X(S)\equiv\prod_z(\pm1)^{\ell_z}\equiv\pm1\pmod N.
\]

Thus pooling cannot reveal a new nontrivial square root of \(1\) after the individual loop screens. Any mixed-sign CRT root was already exposed by its own loop screen; on the no-factor branch, products of screened loops remain globally \(\pm1\). In this precise formal endpoint-parity mechanism, pooling adds no factoring information after direct loop screening.

## Formal parity versus actual integer squares

Let \(L\) be the finite set of endpoint labels in the batch, and let the batch have \(m\) pair occurrences. Define the endpoint incidence matrix

\[
C\in\mathbb F_2^{L\times m},\qquad
C_{u,j}=\#\{\text{endpoints of occurrence }j\text{ labeled }u\}\pmod2.
\]

A nonloop column has a \(1\) at each of its two labels. A loop column is zero because its two equal endpoints cancel modulo \(2\). A subset is represented by its indicator vector \(s\in\mathbb F_2^m\), and its endpoint-count parity vector is \(Cs\). Therefore

\[
\text{formal endpoint-parity pooling}=\ker C.
\]

Let \(\mathcal P\) be the finite set of rational primes dividing at least one label in \(L\). Define the rational prime-valuation parity map

\[
V:\mathbb F_2^L\longrightarrow\mathbb F_2^{\mathcal P},
\qquad
(Ve)_p=\sum_{u\in L}e_u\,v_p(u)\pmod2.
\]

For a selection \(s\), the parity of every rational prime valuation in its visible integer product is exactly \(VCs\). A positive integer is a square exactly when all of its prime valuations are even. Hence

\[
\text{true integer-square pooling}=\ker(VC).
\]

It follows immediately that

\[
\ker C\subseteq\ker(VC),
\]

and the inclusion can be strict because distinct endpoint labels can represent the same rational square class.

For the required example, take \(N=15\) and the single pair \((2,8)\). It is an inverse pair because

\[
2\cdot8=16\equiv1\pmod{15}.
\]

The single selection has odd endpoint count at label \(2\) and at label \(8\), so it is not in \(\ker C\). But

\[
2\cdot8=16=4^2,
\]

so it is in \(\ker(VC)\): equivalently, \(v_2(2)+v_2(8)=1+3\equiv0\pmod2\). Its root is \(4\), and

\[
\gcd(4-1,15)=3
\]

is a proper factor (also \(\gcd(4+1,15)=5\)). This successful arithmetic square-class relation lies outside formal endpoint parity, exactly as the strict kernel inclusion predicts.

Conceptually, this is consistent with the generic no-compression rank fact for arbitrary square classes: if a square-class map has rank \(r\) over \(\mathbb F_2\), a lossless linear representation of arbitrary such classes needs \(r\) independent coordinates. Here the arithmetic map is \(VC\), whereas \(C\) records the finer syntactic condition that each label occur evenly. The possible strict inequality between their ranks, or equivalently the possible strict inclusion between their kernels, is why endpoint labels must not be identified with rational square classes.

The result is deliberately limited to formal endpoint-parity pools of canonical inverse pairs and their square-root-of-one output. It makes no claim about arithmetic square-class pooling, smoothness, chronological quotient equations, lattices, HSP/Shor, stabilizer methods, nonlinear graph constructions, or factoring in general.

**Verdict: SUCCESS.** Formal endpoint parity reduces every nonloop inversion orbit to \(1\); all remaining outputs come from submitted loops, and direct screening either factors \(N\) or reduces every such output to global \(\pm1\).
