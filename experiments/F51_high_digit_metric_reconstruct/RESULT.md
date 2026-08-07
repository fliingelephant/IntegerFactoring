# Strict proof-blind reconstruction: the high digit of \(a^N \bmod N^2\)

## 1. Statement and conventions

Let \(p,q\) be primes such that

\[
3\le p<q<2p,
\qquad p\ne q,
\qquad N=pq.
\]

Write

\[
U_N=(\mathbb Z/N\mathbb Z)^*,
\qquad \phi(N)=(p-1)(q-1).
\]

For an integer \(y\) and a positive integer \(m\), \([y]_m\) denotes the representative of \(y\bmod m\) in \(\{0,\ldots,m-1\}\). Let \(a\) be uniform on \(U_N\), and define

\[
A=[a^N]_{N^2},\qquad x=[a^N]_N,
\qquad A=x+Nh,
\qquad 0\le h<N,
\]

and

\[
\lambda=[h x^{-1}]_N.
\]

Here \(x\in U_N\), so its inverse exists. The value \(A\) depends only on the residue class of \(a\bmod N\): for every integer \(t\), the binomial theorem gives

\[
(a+tN)^N\equiv a^N\pmod {N^2}.
\]

For a prime \(r\) and an integer \(u\) with \(r\nmid u\), define the Fermat quotient

\[
Q_r(u)=\frac{u^{r-1}-1}{r}\pmod r.
\]

This is a residue in \(\mathbb F_r\). It depends on \(u\bmod r^2\), not only on \(u\bmod r\).

All probability statements below quantify over fresh, mutually independent uniform choices of \(a\), unless stated otherwise.

## 2. The low digit is exactly uniform

The map

\[
T:U_N\longrightarrow U_N,\qquad T(a)=a^N
\]

is a permutation. Under CRT, it is the product of the power maps on \(\mathbb F_p^*\) and \(\mathbb F_q^*\). On the first component,

\[
\gcd(N,p-1)=1:
\]

neither \(p\) nor the larger prime \(q\) divides \(p-1\). On the second component, \(q\nmid q-1\), and \(p\nmid q-1\). Indeed, if \(p\mid q-1\), then \(0<q-1<2p\) forces \(q-1=p\), but then \(q=p+1\) is an even integer greater than \(2\), not a prime. Thus \(\gcd(N,q-1)=1\). Raising to the \(N\)-th power is therefore an automorphism on both cyclic local groups.

Consequently,

\[
\Pr(x=u)=\frac1{\phi(N)}\quad(u\in U_N),
\]

and the probability is zero for \(u\notin U_N\). In particular, \(x\) is exactly uniform on \(U_N\), not merely close to uniform.

The permutation also makes \(h\) a well-defined function of \(x\): there is a unique \(a\bmod N\) mapping to each \(x\in U_N\).

## 3. Exact local Fermat-quotient laws

Because \(A\equiv a^{pq}\pmod {p^2}\), Euler's theorem modulo \(p^2\) gives

\[
A^{p-1}\equiv a^{pq(p-1)}\equiv1\pmod {p^2}.
\]

Using \(A=x+pqh\) and expanding modulo \(p^2\),

\[
0\equiv Q_p(x)+(p-1)q h x^{p-2}
  \equiv Q_p(x)-q h x^{-1}\pmod p.
\]

The identical argument modulo \(q^2\) gives the second law. Hence

\[
\boxed{q\lambda\equiv Q_p(x)\pmod p},
\qquad
\boxed{p\lambda\equiv Q_q(x)\pmod q}.
\]

Equivalently, the local high digits are

\[
\boxed{h\equiv xq^{-1}Q_p(x)\pmod p},
\qquad
\boxed{h\equiv xp^{-1}Q_q(x)\pmod q}.
\]

Thus, if

\[
\alpha_p=[xq^{-1}Q_p(x)]_p,
\qquad
\alpha_q=[xp^{-1}Q_q(x)]_q,
\]

then \(h\) is exactly the unique integer in \([0,N)\) satisfying

\[
h\equiv\alpha_p\pmod p,
\qquad h\equiv\alpha_q\pmod q.
\]

For example, with the CRT idempotents

\[
e_p=q[q^{-1}]_p,
\qquad e_q=p[p^{-1}]_q,
\]

the exact canonical formula is

\[
h=[\alpha_p e_p+\alpha_q e_q]_N.
\]

Likewise, \(\lambda\) is the CRT combination of

\[
\lambda\equiv q^{-1}Q_p(x)\pmod p,
\qquad
\lambda\equiv p^{-1}Q_q(x)\pmod q.
\]

No factor-free evaluation claim follows from these CRT formulas: their local moduli are the unknown factors.

## 4. Exact conditional local distributions

The basic shift identity is, for every prime \(r\), every \(r\nmid u\), and every integer \(t\),

\[
Q_r(u+tr)\equiv Q_r(u)-t u^{-1}\pmod r.
\]

It follows by expanding \((u+tr)^{r-1}\) modulo \(r^2\).

### 4.1 The \(q\)-coordinate

Fix \(s\in\{1,\ldots,q-1\}\). Every integer \(x\in[0,N)\) with \(x\equiv s\pmod q\) has a unique form

\[
x=s+kq,qquad 0\le k\le p-1.
\]

Exactly one index \(\kappa_p(s)\in\{0,\ldots,p-1\}\) makes \(p\mid s+kq\). Conditional on \(x\equiv s\pmod q\), the index \(k\) is exactly uniform on

\[
K_s=\{0,\ldots,p-1\}\setminus\{\kappa_p(s)\},
\]

which has \(p-1\) elements. The shift identity and the local formulas give

\[
Q_q(s+kq)\equiv Q_q(s)-ks^{-1}\pmod q,
\]

\[
h(s+kq)\equiv p^{-1}\bigl(sQ_q(s)-k\bigr)\pmod q,
\]

and

\[
\lambda(s+kq)\equiv
p^{-1}\bigl(Q_q(s)-ks^{-1}\bigr)\pmod q.
\]

Each displayed expression is injective as a function of \(k\in K_s\), because \(p-1<q\) and the coefficient of \(k\) is nonzero modulo \(q\). Therefore, conditional on any fixed nonzero \(s=x\bmod q\), each of

\[
Q_q(x),\quad h\bmod q,\quad \lambda\bmod q
\]

is uniform on an explicitly described support of exactly \(p-1\) residues.

### 4.2 The \(p\)-coordinate

Fix \(r\in\{1,\ldots,p-1\}\). Write

\[
x=r+\ell p,qquad 0\le \ell\le q-1.
\]

Exactly one \(\ell\) makes \(q\mid x\), so the conditional sample space has \(q-1\) elements. The corresponding formulas are

\[
Q_p(r+\ell p)\equiv Q_p(r)-\ell r^{-1}\pmod p,
\]

\[
h(r+\ell p)\equiv q^{-1}\bigl(rQ_p(r)-\ell\bigr)\pmod p,
\]

and

\[
\lambda(r+\ell p)\equiv
q^{-1}\bigl(Q_p(r)-\ell r^{-1}\bigr)\pmod p.
\]

Because \(0\le\ell<q<2p\), each residue \(\ell\bmod p\) occurs at most twice. Removing one index cannot increase that multiplicity. Thus every conditional point mass in each of these three \(p\)-local distributions is at most \(2/(q-1)\).

### 4.3 Point-mass consequences

Let \(Z\) denote either \(h\) or \(\lambda\), using its canonical value in \([0,N)\). Averaging the conditional bounds gives, for every residue \(c\),

\[
\boxed{\Pr(Z\equiv c\pmod q)\le\frac1{p-1}},
\qquad
\boxed{\Pr(Z\equiv c\pmod p)\le\frac2{q-1}}.
\]

In particular, for every exact integer \(t\in[0,N)\),

\[
\boxed{\Pr(Z=t)\le\frac1{p-1}}.
\]

This is a point-mass bound. It is not a statement that \(h\), \(\lambda\), or either local distribution is globally uniform.

The conditional result is slightly stronger. For any family of sets \(C_s\subseteq\mathbb Z/q\mathbb Z\) with \(|C_s|\le L\),

\[
\Pr\bigl(Z\bmod q\in C_{x\bmod q}\bigr)
\le \min\left\{1,\frac L{p-1}\right\}.
\]

This mathematical conditioning uses the factor \(q\). It is not a factor-free algorithm.

## 5. Sparse tests and gcd tests

Define

\[
\beta_q=\frac1{p-1},
\qquad
\beta_p=\frac2{q-1},
\qquad
\beta=\beta_p+\beta_q<\frac3{p-1}.
\]

All choices of menus, offsets, and bands in this section must be fixed independently of the current sample. They may be chosen in advance, or nonanticipatingly from previous independent samples. The same bounds also hold conditionally for a current menu that depends only on the local base residue specified in Section 4 and not on its current lift index. They do not hold for an unrestricted function of the current full \(x\), \(a\), or \(h\).

### 5.1 Exact-value menus

For independent \(Z_1,\ldots,Z_m\), where every \(Z_i\) is either the corresponding \(h_i\) or \(\lambda_i\), let \(S_i\subseteq[0,N)\) be an exact-value menu. Then

\[
\Pr\bigl(\exists i:Z_i\in S_i\bigr)
\le
\min\left\{1,\frac{\sum_i|S_i|}{p-1}\right\}.
\]

Thus a total of \(L\) exact guesses has success probability at most \(L/(p-1)\). For comparison, an exact menu for \(x\), or for \(A\), has point mass exactly \(1/\phi(N)\) on its support, because \(a\mapsto x\) is a permutation and \(x\) already identifies \(A\)'s source.

### 5.2 Exact collisions

For two independent copies,

\[
\Pr(Z_1=Z_2)
\le \Pr(Z_1\equiv Z_2\pmod q)
=\sum_{c\bmod q}\Pr(Z\equiv c\pmod q)^2
\le\frac1{p-1}.
\]

Therefore

\[
\Pr(\text{some exact collision among }Z_1,\ldots,Z_m)
\le \min\left\{1,\binom m2\frac1{p-1}\right\}.
\]

### 5.3 Direct gcd tests

For every fixed integer offset \(c\),

\[
\Pr\bigl(p\mid Z-c\bigr)\le\beta_p,
\qquad
\Pr\bigl(q\mid Z-c\bigr)\le\beta_q.
\]

Hence

\[
\Pr\bigl(1<\gcd(N,Z-c)<N\bigr)\le\beta.
\]

The same upper bound remains valid if the event \(\gcd(N,Z-c)=N\) is included. For \(R\) fixed or nonanticipating direct gcd tests, the union bound gives

\[
\Pr(\text{some test returns a nontrivial factor})
\le\min\{1,R\beta\}.
\]

In particular this covers \(c=0\), for both \(h\) and \(\lambda\). By contrast, \(\gcd(N,x)=\gcd(N,A)=1\) deterministically.

### 5.4 Pairwise-difference gcd tests

Independence and the local point-mass bounds give

\[
\Pr\bigl(p\mid Z_i-Z_j\bigr)\le\beta_p,
\qquad
\Pr\bigl(q\mid Z_i-Z_j\bigr)\le\beta_q.
\]

Thus

\[
\Pr\bigl(1<\gcd(N,Z_i-Z_j)<N\bigr)\le\beta,
\]

and testing every pair among \(m\) samples has success probability at most

\[
\min\left\{1,\binom m2\beta\right\}.
\]

An exact equality \(Z_i=Z_j\) returns \(N\), not a proper factor; including it above only makes the upper bound larger. For the low digits themselves, exact CRT uniformity gives the sharper bounds

\[
\Pr(p\mid x_i-x_j)=\frac1{p-1},
\qquad
\Pr(q\mid x_i-x_j)=\frac1{q-1}.
\]

### 5.5 Thin integer bands

A precise sparse-band statement is as follows. For sample \(i\), let \(B_i\subseteq[0,N)\) contain at most \(W_i\) admissible integer high digits. A usual interval band of inclusive half-width \(w_i\) has \(W_i\le 2\lfloor w_i\rfloor+1\). Then

\[
\mathbb E\sum_{i=1}^m\mathbf 1_{\{Z_i\in B_i\}}
\le\frac{\sum_iW_i}{p-1},
\]

and

\[
\Pr(\exists i:Z_i\in B_i)
\le\min\left\{1,\frac{\sum_iW_i}{p-1}\right\}.
\]

This also covers a family \(B_{i,s}\) indexed by \(s=x_i\bmod q\), provided every such band contains at most \(W_i\) exact integers. This is the rigorous meaning of a P51-style thin integer band available from the bare statement.

Let

\[
n=\lfloor\log_2N\rfloor+1
\]

be the input bit length. Balance gives

\[
p^2<N<2p^2,
\qquad
p>\sqrt{N/2}\ge 2^{(n-2)/2}.
\]

If all \(m\) bands have integer width at most \(W\), then success probability at least \(\delta>0\) is possible only if

\[
\boxed{mW\ge\delta(p-1)
>\delta\bigl(2^{(n-2)/2}-1\bigr)}.
\]

Therefore, with \(m\le\operatorname{poly}(n)\), the required absolute integer width is

\[
W=\Omega\!\left(\frac{2^{n/2}}{\operatorname{poly}(n)}\right),
\]

and with \(W\le\operatorname{poly}(n)\), the required sample count has the same exponential scale. More generally, any polynomial total number of menu entries, collision pairs, or gcd tests has probability

\[
2^{-n/2+O(\log n)}
\]

under the applicable bound.

The word “width” here means the number of exact integer values admitted. An arbitrary dense set, or a band whose center uses the current full sample and tracks \(h(x)\), is outside this statement.

## 6. Reflection and the exact mean

Since \(N\) is odd, \((-a)^N=-a^N\). If \(A=x+Nh\), then the canonical residue for the input \(-a\bmod N\) is

\[
N^2-A=(N-x)+N(N-1-h).
\]

The input \(-a\) is the unique preimage of \(N-x\), because the power map is a permutation. Hence

\[
\boxed{h(N-x)=N-1-h(x)}.
\]

The involution \(x\mapsto N-x\) has no fixed point because \(N\) is odd. It preserves the uniform distribution on \(U_N\). Therefore the distribution of \(h\) satisfies

\[
\Pr(h=t)=\Pr(h=N-1-t),
\]

and

\[
\boxed{\mathbb E[h]=\frac{N-1}{2}}.
\]

This symmetry and mean do not imply uniformity or concentration.

## 7. Exact Parseval consequence

Let \(Z\) be either \(h\) or \(\lambda\), let

\[
\mu(t)=\Pr(Z=t),\qquad 0\le t<N,
\]

and use the unnormalized Fourier transform

\[
\widehat\mu(k)=\sum_{t=0}^{N-1}\mu(t)e^{2\pi i kt/N}
=\mathbb E[e^{2\pi i kZ/N}].
\]

Parseval is the exact identity

\[
\boxed{
\frac1N\sum_{k=0}^{N-1}|\widehat\mu(k)|^2
=\sum_{t=0}^{N-1}\mu(t)^2
=\Pr(Z=Z')},
\]

where \(Z'\) is an independent copy. The point-mass result implies

\[
\sum_t\mu(t)^2\le\frac1{p-1}.
\]

Let \(K\) be uniform on \(U_N\). Restricting the nonnegative Parseval sum to unit frequencies gives

\[
\mathbb E_K|\widehat\mu(K)|^2
\le
B_N,
\qquad
B_N:=\frac{N}{\phi(N)(p-1)}
=\frac{pq}{(p-1)^2(q-1)}.
\]

Since \(p\ge3\) and \(q\ge5\),

\[
B_N\le\frac{15}{8(p-1)}=2^{-n/2+O(1)}.
\]

For \(\varepsilon>0\), define the set of heavy unit frequencies

\[
E_\varepsilon=\{k\in U_N:|\widehat\mu(k)|\ge\varepsilon\}.
\]

Then

\[
\frac{|E_\varepsilon|}{\phi(N)}
\le\min\left\{1,\frac{B_N}{\varepsilon^2}\right\}.
\]

For \(J\) independently uniform unit frequencies \(K_1,\ldots,K_J\), the exact hit probability and its Parseval upper bound are

\[
\Pr(\exists j:K_j\in E_\varepsilon)
=1-\left(1-\frac{|E_\varepsilon|}{\phi(N)}\right)^J
\le\min\left\{1,\frac{JB_N}{\varepsilon^2}\right\}.
\]

Thus polynomially many independently uniform unit frequencies are unlikely to find an inverse-polynomial-heavy coefficient: if \(J=\operatorname{poly}(n)\) and \(\varepsilon^{-1}=\operatorname{poly}(n)\), the upper bound is \(2^{-n/2+O(\log n)}\).

### The raw empirical mean

For \(T\ge1\), take iid copies \(Z_1,\ldots,Z_T\), independent of \(K\), and define only the raw empirical mean

\[
M_T(K)=\frac1T\sum_{i=1}^T e^{2\pi i KZ_i/N}.
\]

For fixed \(k\), the exact second moment is

\[
\mathbb E|M_T(k)|^2
=\frac1T+\frac{T-1}{T}|\widehat\mu(k)|^2.
\]

Therefore

\[
\boxed{
\Pr\bigl(|M_T(K)|\ge\eta\bigr)
\le
\min\left\{1,
\frac{T^{-1}+(1-T^{-1})B_N}{\eta^2}
\right\}.}
\]

For \(J\) unit frequencies, independent of the sample vector and each uniform, a union bound multiplies the right-hand expression before the outer truncation by \(J\). The same sample vector may be reused for all frequencies; independence among the empirical means is not needed for that union bound.

This displayed estimate concerns the raw empirical mean \(M_T\) only. Its \(1/T\) term is sampling noise. It is not a bound for arbitrary estimators, adaptive searches, or exact coefficient evaluation. A polynomial \(T\) can make the raw-noise term small at an inverse-polynomial threshold only when its degree is large enough; for example, a sufficient condition for a union-bound contribution at most \(\delta\) is \(T\ge J/(\delta\eta^2)\).

## 8. Why a local-isolating frequency already factors \(N\)

For the additive character \(t\mapsto e^{2\pi i kt/N}\), a frequency that isolates one CRT coordinate is nonzero modulo one prime and zero modulo the other. Concretely,

\[
k=pu, q\nmid u
\quad\Longrightarrow\quad
e^{2\pi i kt/N}=e^{2\pi iut/q},
\]

and \(\gcd(k,N)=p\). Similarly, \(k=qu\) with \(p\nmid u\) depends only on \(t\bmod p\), and \(\gcd(k,N)=q\). The zero frequency has gcd \(N\) and is trivial.

Thus any nontrivial local-isolating frequency already exposes a proper factor through one Euclidean gcd. Uniform unit frequencies deliberately exclude these frequencies.

## 9. Fair-bit and bit-operation costs

Let \(n=\lfloor\log_2N\rfloor+1\), and let \(M(n)\) denote the bit cost of multiplying \(n\)-bit integers.

### Exact uniform sampling

Draw \(n\) independent fair bits to obtain \(R\in\{0,\ldots,2^n-1\}\). Accept iff \(R<N\) and \(\gcd(R,N)=1\). Every unit is accepted with the same probability, so the accepted output is exactly uniform. The acceptance probability is

\[
\rho=\frac{\phi(N)}{2^n}
=\frac{N}{2^n}\left(1-\frac1p\right)
\left(1-\frac1q\right)
\ge\frac12\cdot\frac23\cdot\frac45
=\frac4{15}.
\]

Hence one exact unit sample uses

\[
\mathbb E[\text{trials}]=\rho^{-1}\le\frac{15}{4},
\qquad
\mathbb E[\text{fair bits}]=\frac n\rho\le\frac{15n}{4}.
\]

The probability of needing more than \(t\) trials is at most \((11/15)^t\). Exact rejection sampling has no finite worst-case fair-bit bound. A hard cutoff must either report failure or introduce bias. The same costs apply independently to sampling a uniform unit frequency. For \(m\) inputs and \(J\) frequencies, the expected fair-bit cost is at most \(15(m+J)n/4\).

A rejected candidate with a proper nontrivial gcd already factors \(N\). The theorem's sample laws concern the accepted uniform units.

### Arithmetic per high-digit sample

Binary modular exponentiation computes \(A=a^N\bmod N^2\) using at most \(2n\) modular multiplications on at most \(2n\)-bit operands. Then compute

\[
x=A\bmod N,qquad h=(A-x)/N,
\qquad \lambda=h x^{-1}\bmod N.
\]

The inverse uses extended gcd. With standard fast arithmetic, the exponentiation costs \(O(nM(n))\) bit operations up to the usual modular-reduction factors, and inversion costs \(O(M(n)\log n)\). With schoolbook arithmetic, the coarse bound is \(O(n^3)\) per sample. No factors of \(N\) are required for these computations.

If \(p,q\) are already known, either Fermat quotient can be evaluated by one modular exponentiation modulo \(p^2\) or \(q^2\), followed by an exact division by the prime. This has the same \(O(nM(n))\) coarse bit bound. Knowing those moduli already means knowing the factorization.

Each gcd of two \(O(n)\)-bit integers costs \(O(M(n)\log n)\) with fast gcd, or \(O(n^2)\) classically. Thus \(R\) direct tests cost \(O(RM(n)\log n)\); testing all pairwise differences costs \(O(m^2M(n)\log n)\). Explicit menu membership takes at most one \(O(n)\)-bit comparison per menu entry; collision detection by sorting takes \(O(m\log m)\) such comparisons.

For the raw Fourier means at \(J\) frequencies and \(T\) samples, forming all exponents \(K_jZ_i\bmod N\) takes \(JT\) modular multiplications. The exact symbolic raw sums can be stored as sums of powers of \(\zeta_N\). Numerical magnitude evaluation has an additional precision-dependent cost; at \(b\)-bit precision it is \(JT\) evaluations of an \(N\)-th root of unity to that precision. No extra fair bits are needed after the samples and frequencies have been drawn. The probability statements do not assume that exact algebraic comparison is easy.

## 10. Exact scope and exclusions

The proved statements do **not** establish any of the following:

- uniformity, pseudorandomness, or cryptographic indistinguishability of \(h\) or \(\lambda\);
- absence of deterministic exceptional unit frequencies with large Fourier coefficients;
- failure of a frequency chosen adaptively from observations, rather than independently and uniformly;
- failure of adaptive recovery or of a menu/band that depends on the current full \(x\), \(a\), \(A\), or computed \(h\);
- bounds for nonlinear statistics, dense subsets, joint statistics, or statistics that combine many samples in a form not analyzed above;
- bounds for estimators other than the displayed raw empirical mean;
- impossibility of exact symbolic evaluation of a tiny coefficient, or of amplification using enough classical, quantum, or algebraic resources;
- a lower bound for factoring, or a claim that every use of \((x,h,\lambda)\) reduces to a sparse menu, collision, gcd, band, or random-frequency test.

The atom bounds are information about specified random sparse events. They are not secrecy claims: given \(a\) and \(N\), the values \(A,x,h,\lambda\) are all computable in polynomial time.

## Reconstruction status

**RECONSTRUCTION SUCCEEDS.** No mathematical mismatch was found. The bare statement does not define the name “P51-style”; the reconstruction gives the strongest unambiguous sparse integer-band theorem implied by the stated local point-mass law. Any broader, sample-dependent meaning of that label would require an additional definition and is expressly not claimed.
