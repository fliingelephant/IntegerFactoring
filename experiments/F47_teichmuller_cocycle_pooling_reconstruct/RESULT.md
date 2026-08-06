PASS

# Proof-blind reconstruction

## Provenance

This reconstruction uses only the bare theorem package in the assignment and standard algebra/number theory. I did not read, list, hash, inspect, or otherwise access either `experiments/F47_teichmuller_cocycle_pooling_kill/` or `experiments/F47_teichmuller_cocycle_pooling_audit/`. I did not seek a candidate-proof summary or inspect another agent's proof output. I used neither web access nor a finite computation, and I changed no canonical durable-state file.

## 1. The lift, the carry, and the normalized cocycle

Write \(\langle r\rangle_M\) for the unique representative of \(r\bmod M\) in \(\{0,\ldots,M-1\}\). If \(u' = u+kN\), then
\[
(u+kN)^N-u^N
=N u^{N-1}kN+\sum_{j=2}^N\binom Nj u^{N-j}(kN)^j
\equiv0\pmod {N^2}.
\]
Thus
\[
A:G_N\longrightarrow (\mathbb Z/N^2\mathbb Z)^\times,
\qquad A(a)=u^N\pmod {N^2}
\]
is independent of the integer representative \(u\) of \(a\). Its values are units. If \(a,b\) are represented by \(u,v\), well-definedness applied to a representative of \(ab\) gives
\[
A(ab)=(uv)^N=u^Nv^N=A(a)A(b)\pmod {N^2},
\]
so \(A\) is a group homomorphism.

Let \(A(a)\) now denote its canonical integer representative modulo \(N^2\), and write uniquely
\[
A(a)=x(a)+Nh(a),\qquad 0\leq x(a),h(a)<N.
\]
Reduction of the homomorphism shows that \(x:G_N\to G_N\) is a homomorphism (with canonical representatives used when writing integer formulas). Put
\[
x=x(a),\quad y=x(b),\quad z=\langle xy\rangle_N,
\quad c(x,y)=\frac{xy-z}{N}.
\]
Multiplication of the two canonical decompositions gives
\[
A(a)A(b)
\equiv z+N\bigl(c(x,y)+xh(b)+yh(a)\bigr)\pmod {N^2}.
\]
Because \(x(ab)=z\), comparison with \(A(ab)=z+Nh(ab)\) proves the exact claimed congruence
\[
\boxed{h(ab)\equiv c(x(a),x(b))+x(a)h(b)+x(b)h(a)\pmod N.}
\]

All of \(x,y,z\) are units modulo \(N\). Define
\[
\lambda(a)=h(a)x(a)^{-1},
\qquad
\kappa(x,y)=c(x,y)\langle xy\rangle_N^{-1}
\quad\text{in }\mathbb Z/N\mathbb Z.
\]
Multiplying the preceding formula by \(z^{-1}=(xy)^{-1}\) gives, with no action term,
\[
\boxed{\lambda(ab)=\lambda(a)+\lambda(b)+
\kappa(x(a),x(b))\pmod N.}
\]

The signs can also be seen directly from the canonical section. Let \(s(x)\) be the canonical integer \(x\), viewed as a unit modulo \(N^2\). Then
\[
s(x)s(y)=s(z)\bigl(1+N\kappa(x,y)\bigr)\pmod {N^2},
\qquad
A(a)=s(x(a))\bigl(1+N\lambda(a)\bigr)\pmod {N^2}.
\]
The factor set therefore enters with the displayed **plus** sign.

The normalization and inverse specialization are as follows. One has
\[
x(1)=1,\quad h(1)=\lambda(1)=0,
\quad \kappa(1,x)=\kappa(x,1)=0.
\]
For canonical \(x=x(a)\), let \(\bar x=\langle x^{-1}\rangle_N\). Then
\[
x(a^{-1})=\bar x,qquad
c(x,\bar x)=\frac{x\bar x-1}{N},qquad
\kappa(x,\bar x)=c(x,\bar x),
\]
because \(\langle x\bar x\rangle_N=1\). Hence
\[
\boxed{\lambda(a^{-1})=-\lambda(a)-\kappa(x,\bar x)\pmod N.}
\]
Equivalently,
\[
0\equiv c(x,\bar x)+x h(a^{-1})+\bar x h(a)\pmod N,
\]
and at section level
\[
s(x)^{-1}=s(\bar x)\bigl(1-N\kappa(x,\bar x)\bigr)\pmod {N^2}.
\]

For the cocycle identity, take canonical units \(x,y,w\), and set
\[
z=\langle xy\rangle_N,qquad
u=\langle yw\rangle_N,qquad
r=\langle xyw\rangle_N.
\]
Associating the ordinary integer product \(xyw\) in the two ways gives the exact carry identity
\[
w,c(x,y)+c(z,w)=x,c(y,w)+c(x,u).
\]
Multiplication modulo \(N\) by \(r^{-1}\), using
\(r\equiv zw\equiv xu\pmod N\), yields
\[
\boxed{
\kappa(x,y)+\kappa(\langle xy\rangle_N,w)
=\kappa(y,w)+\kappa(x,\langle yw\rangle_N)
\pmod N.}
\]
This is the normalized section \(2\)-cocycle identity with all four arguments interpreted via canonical representatives. (The carry, and hence \(\kappa\), is also symmetric in its two inputs, although symmetry is not needed.)

## 2. Occurrence-labelled multiplicative graphs

Let the vertex-occurrence set be \(V_0\). A label \(v\in V_0\) carries a class \(a_v\in G_N\). For every edge occurrence \(e=(t;s,m)\), assume the genuine base-class identity
\[
a_t=a_sa_m\quad\text{in }G_N.
\]
Define the integer matrix row by collecting roles in the same column:
\[
B_{e,v}=\mathbf 1_{v=t}-\mathbf 1_{v=s}-\mathbf 1_{v=m}.
\]
Thus, for example, two negative roles on the same occurrence produce \(-2\), while coincident positive and negative roles cancel. No special treatment of loops or repetitions is needed. Put
\[
\lambda_v=\lambda(a_v),
\qquad
\kappa_e=\kappa(x(a_s),x(a_m)).
\]
Applying the normalized product formula edge by edge proves the literal global identity
\[
\boxed{B\lambda=\kappa\quad\text{over }\mathbb Z/N\mathbb Z.}
\]

Consequently:

1. The full linear residual \(B\lambda-\kappa\), every component of it, and every linear combination of its components are zero modulo \(N\).
2. If \(q^TB=0\) over \(\mathbb Z/N\mathbb Z\) (in particular, if an integer cycle vector is a left syzygy), then
   \[
   q^T\kappa=q^TB\lambda=0\pmod N.
   \]
   The same statement holds after reduction to every prime field below.
3. The entire augmented consistency problem \(By=\kappa\), and hence every subsystem or linear image used by a linear consistency test, has the global witness \(y=\lambda\). (The solution need not be unique.) This is stronger than merely passing a necessary rank test over a field.
4. For every prime \(p\mid N\), reduction gives \(B_p\lambda_p=\kappa_p\) over \(\mathbb F_p\). Therefore \(\kappa_p\) lies in the column space of \(B_p\), and exactly
   \[
   \boxed{\operatorname{rank}_{\mathbb F_p}[B_p\mid\kappa_p]
   =\operatorname{rank}_{\mathbb F_p}B_p.}
   \]

The last equality compares a matrix only with its own augmentation over the **same** field. It implies neither equality of \(\operatorname{rank}B_p\) for different primes nor anything about integer minors or Smith data. Also, a modular residual being zero says only that an integer representative of it is divisible by \(N\); its quotient by \(N\) is not controlled here.

Occurrence labels remain distinct even when their public \(x\)-values collide. They may be identified on the strength of an \(x\)-collision only after the descent property in the next section has been proved for that \(N\).

## 3. Exact descent classification

Say that descent holds for \(N\) if there is a function on \(x(G_N)\) whose value at \(x(a)\) is \(A(a)\) for every \(a\in G_N\). Equivalently,
\[
\forall a,b\in G_N,qquad x(a)=x(b)\Longrightarrow A(a)=A(b)\pmod {N^2}.
\]
Because \(A=x+Nh\) is the unique canonical decomposition, this is equivalent to \(h\), and hence \(\lambda\), being determined by \(x\) on all unit inputs.

### 3.1 CRT localization

Fix \(p^e\Vert N\), and write \(N=p^e m\) with \(p\nmid m\). For a local unit \(u\bmod p^e\), define
\[
A_{p,e}(u)=\widetilde u^{,N}\pmod {p^{2e}},
\qquad
x_{p,e}(u)=\widetilde u^{,N}\pmod {p^e},
\]
where \(\widetilde u\) is any integer lift. These are well-defined: changing the lift by \(kp^e\) makes the linear binomial term divisible by \(p^{v_p(N)+e}=p^{2e}\), and every higher term is also divisible by \(p^{2e}\). Under CRT, global \(A\) and \(x\) are exactly the tuples of these local maps. Thus local determining formulas combine uniquely modulo \(N^2\), while any local same-\(x\), different-\(A\) pair can be held equal to \(1\) at all other prime-power components and lifted by CRT to a global counterexample.

### 3.2 Odd prime powers

First suppose \(e=1\), so \(N=pm\). For \(r\in\mathbb F_p^\times\), let \(\tau_p(r)\in(\mathbb Z/p^2\mathbb Z)^\times\) be its Teichmüller lift: the unique lift satisfying \(\tau_p(r)^{p-1}=1\pmod {p^2}\). Equivalently,
\[
\tau_p(r)=\widetilde r^{,p}\pmod {p^2}
\]
for any lift \(\widetilde r\) of \(r\). For a local input \(u\),
\[
A_{p,1}(u)=u^{pm}=(u^m)^p
=\tau_p(u^m\bmod p)
=\boxed{\tau_p(x_{p,1}(u))}\pmod {p^2},
\]
where Frobenius gives \(u^{pm}\equiv u^m\pmod p\). Hence every squarefree odd component descends, even if the power map on its residue field is not injective.

Now let \(e\ge2\). In \(\mathbb Z_p^\times\), write uniquely
\[
u=\omega(u)\exp L(u),
\qquad \omega(u)\in\mu_{p-1},\quad L(u)\in p\mathbb Z_p.
\]
Modulo an input precision \(p^e\), the principal logarithmic coordinate is
\(L(u)\bmod p^e\). Since \(m\) is a \(p\)-adic unit,
\[
u^N=\omega(u)^N\exp\bigl(p^e mL(u)\bigr).
\]
The exponential factor is \(1\pmod {p^e}\), so \(x_{p,e}\) erases the entire principal coordinate and retains only \(\omega(u)^N\bmod p^e\). Modulo \(p^{2e}\), however, multiplication by \(p^em\) is an isomorphism
\[
p\mathbb Z_p/p^e\mathbb Z_p
\xrightarrow{\ \sim\ }
p^{e+1}\mathbb Z_p/p^{2e}\mathbb Z_p.
\]
The odd-prime logarithm and exponential are isomorphisms on the corresponding principal-unit quotients. Therefore, for each fixed Teichmüller coordinate, the principal coordinate erased by \(x_{p,e}\) is retained **bijectively** by \(A_{p,e}\bmod p^{2e}\).

A symbolic witness is already supplied by
\[
u_0=1,qquad u_1=1+p.
\]
Indeed \(x_{p,e}(u_0)=x_{p,e}(u_1)=1\), while
\[
v_p\bigl((1+p)^N-1\bigr)
=v_p\bigl(N\log(1+p)\bigr)=e+1<2e,
\]
so their \(A_{p,e}\)-values differ modulo \(p^{2e}\). There is no exception at \(p=3\): the explicit pair is \(1\) and \(4\), and the same valuation is \(e+1\) for every \(e\ge2\).

### 3.3 The prime \(2\)

Let \(2^e\Vert N\), so \(N=2^em\) with \(m\) odd.

* If \(e=1\), every local unit is odd and \(u^{2m}\equiv1\pmod4\). Thus \(x_{2,1}=1\pmod2\) and \(A_{2,1}=1\pmod4\). In particular, the case \(2\Vert N\) descends.
* If \(e=2\), every odd \(u\) satisfies \(u^4\equiv1\pmod {16}\). Hence \(x_{2,2}=1\pmod4\) and \(A_{2,2}=1\pmod {16}\). This case also descends.
* If \(e\ge3\), use the unique decomposition
  \[
  u=\varepsilon(u)\exp L(u),
  \qquad \varepsilon(u)\in\{\pm1\},\quad L(u)\in4\mathbb Z_2,
  \]
  where \(\log:1+4\mathbb Z_2\to4\mathbb Z_2\) is an isomorphism. The even exponent kills \(\varepsilon\), and
  \[
  x_{2,e}(u)=1\pmod {2^e},
  \qquad
  A_{2,e}(u)=\exp(2^emL(u))\pmod {2^{2e}}.
  \]
  Multiplication by \(2^em\) is an isomorphism
  \[
  4\mathbb Z_2/2^e\mathbb Z_2
  \xrightarrow{\ \sim\ }
  2^{e+2}\mathbb Z_2/2^{2e}\mathbb Z_2.
  \]
  Thus \(A_{2,e}\) kills the sign but retains the signless principal coordinate bijectively, whereas \(x_{2,e}\) erases it.

At the boundary \(e=3\), both displayed quotients already have two elements; they are not trivial. Concretely, \(1\) and \(5\) have the same \(x\)-value, while
\[
v_2(5^N-1)=v_2(N\log5)=e+2<2e,
\]
so their \(A\)-values differ modulo \(2^{2e}\). For \(e=3\), this is the strict inequality \(5<6\).

### 3.4 Global equivalence

If the odd part of \(N\) is squarefree and \(8\nmid N\), every odd local component has \(e=1\) and is recovered by
\[
A(a)\bmod p^2=\tau_p(x(a)\bmod p),
\]
while the possible \(2\)-component is either absent, \(1\pmod4\) when \(2\Vert N\), or \(1\pmod {16}\) when \(4\Vert N\). CRT therefore determines one and only one \(A(a)\bmod N^2\) from \(x(a)\bmod N\), and then determines \(h(a)\).

Conversely, if some odd \(p^e\Vert N\) has \(e\ge2\), use the local pair \(1,1+p\); if \(2^e\Vert N\) has \(e\ge3\), use \(1,5\). Put both inputs equal to \(1\) at every other CRT component. The resulting global units have identical \(x\)-values modulo \(N\) and different \(A\)-values modulo \(N^2\). Hence
\[
\boxed{
A\text{ (equivalently }h\text{) is determined by }x\text{ on all units}
\iff
\text{the odd part of }N\text{ is squarefree and }8\nmid N.}
\]

## 4. Uniform bit complexity and unit boundary

Let \(n=\lceil\log_2(N+1)\rceil\). For each of \(V\) unit-labelled vertices, binary modular exponentiation computes \(a^N\bmod N^2\) using \(O(n)\) multiplications of \(O(n)\)-bit words (the modulus has at most \(2n\) bits). Schoolbook multiplication therefore costs \(O(n^3)\) per vertex. Canonical reduction, extraction of \(h=(A-x)/N\), and an extended-Euclidean inverse of \(x\bmod N\) cost at most \(O(n^2)\) additional bit operations and are absorbed in that bound. Store \(x^{-1}\) for every vertex.

For each genuine edge, checking \(a_t=a_sa_m\bmod N\), forming the exact product \(x_sx_m\), reducing it to \(z\), obtaining
\(c=(x_sx_m-z)/N\), multiplying by the stored \(z^{-1}=x_t^{-1}\), and evaluating the linear residual all cost \(O(n^2)\) under schoolbook arithmetic. Thus, conditional on a factor-free relation generator that supplies only polynomially many genuine labelled relations, construction of all vertex values and edge data/residuals costs uniformly
\[
\boxed{O(Vn^3+En^2).}
\]
This is an evaluation bound conditional on that generator; it is not a claim that the relations factor \(N\), nor that factoring was used to generate them.

The definitions of \(x^{-1}\), \(\lambda\), and \(\kappa\) are used only for units. At an external sampling boundary, first compute \(d=\gcd(a,N)\). If \(d=1\), admit the input. If \(1<d<N\), a proper factor has already been found and the multiplicative-graph procedure stops on that outcome. If \(d=N\), reject and retry. Products of admitted units remain units. No nonunit is silently passed into an inverse or into the claimed identities.

## 5. Exact scope

Nothing above decides or exploits ranks of \(B\) across different CRT fields, its minors or Smith data, additive or other nonmultiplicative relations, nonlinear graph/transcript statistics, engineered bases outside this exact linear decoder, inversion of a power map, higher integer quotients after a residual is known divisible by \(N\), noncanonical extra lift data, inverse-polynomial statistical separation, arbitrary-composite recursive schemes, or all-input factorization. Those directions remain open and are not consequences of the cocycle identity or the descent classification.
