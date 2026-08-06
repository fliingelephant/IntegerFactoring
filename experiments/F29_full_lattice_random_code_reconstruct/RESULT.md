# RECONSTRUCTED

Let
\[
L_r:=\{z\in\mathbb Z^m:z\bmod r\in C_r\}\qquad(r=p,q)
\]
and use the Euclidean norm throughout. For \(x\in\mathbb Z^m\), define its
coordinate gcd relative to \(N\) by
\[
g_N(x):=\gcd(N,x_1,\ldots,x_m).
\]
Thus a proper coordinate gcd means \(1<g_N(x)<N\).

## Algebraic identities

Reduction modulo \(p\) and \(q\), followed by quotienting by the codes, gives
the surjective homomorphism
\[
\Phi:\mathbb Z^m\longrightarrow
(\mathbb F_p^m/C_p)\times(\mathbb F_q^m/C_q).
\]
Surjectivity follows coordinatewise from the Chinese remainder theorem, and
its kernel is \(L\). Consequently
\[
[\mathbb Z^m:L]=p^{m-u}q^{m-u}=N^{m-u},
\qquad
\boxed{\det L=N^{m-u}}.
\]

If \(x=py\), then its condition modulo \(p\) is automatic, while
\[
x\bmod q\in C_q
\iff p(y\bmod q)\in C_q
\iff y\bmod q\in C_q,
\]
because multiplication by the nonzero scalar \(p\bmod q\) preserves the
linear subspace \(C_q\). The symmetric argument gives the exact slices
\[
\boxed{L\cap p\mathbb Z^m=pL_q},
\qquad
\boxed{L\cap q\mathbb Z^m=qL_p}.
\]
Their intersection is \(N\mathbb Z^m\). Hence, for every \(x\in L\),
\[
\begin{array}{rcl}
g_N(x)=p&\iff&x\in pL_q\setminus N\mathbb Z^m,\\
g_N(x)=q&\iff&x\in qL_p\setminus N\mathbb Z^m,\\
g_N(x)=N&\iff&x\in N\mathbb Z^m,\\
g_N(x)=1&\iff&x\notin pL_q\cup qL_p.
\end{array}
\]
This is the exact proper coordinate-gcd classification. Equivalently, if
\(d(x)=\gcd(x_1,\ldots,x_m)\), the first two lines say that exactly one of
\(p,q\) divides \(d(x)\).

## A finite, tie-independent probability bound

Write
\[
\lambda_1(L)=\min_{0\ne x\in L}\|x\|_2,
\qquad
R_M=2v_m^{-1/m}N^{1-u/m},
\qquad
R_0=\min(R_M,N).
\]
Since
\[
v_mR_M^m=2^m\det L,
\]
Minkowski's theorem applied at every radius \((1+\varepsilon)R_M\), followed
by \(\varepsilon\downarrow0\), gives \(\lambda_1(L)\le R_M\). Also
\(Ne_i\in L\), so \(\lambda_1(L)\le N\). Therefore
\[
\lambda_1(L)\le R_0.
\]

For a prime \(r\), set
\[
A_{r,m}(T):=
\#\{z\in\mathbb Z^m:0<\|z\|_2\le T,\ z\bmod r\ne0\}.
\]
This is the eligible nonzero-residue count; retaining it is important below.
For a uniform \(u\)-dimensional subspace \(C\le\mathbb F_r^m\) and any fixed
\(0\ne a\in\mathbb F_r^m\), transitivity of
\(\operatorname{GL}_m(\mathbb F_r)\), or double-counting the nonzero elements
of \(C\), gives
\[
\Pr(a\in C)=\frac{r^u-1}{r^m-1}=:\theta_r.
\]

Let \(E\) be the event that **there exists** a nonzero exact shortest vector
of \(L\) having a proper coordinate gcd. This existential event dominates
the success event of every possible exact-SVP tie-breaking rule, including an
adversarial or randomized one. If such a shortest vector has gcd \(p\), it
is \(x=py\) with
\[
0<\|y\|_2\le R_0/p,\qquad y\bmod q\ne0,\qquad y\bmod q\in C_q.
\]
The gcd-\(q\) case is symmetric. A union bound over the eligible integer
vectors therefore gives the sharper finite estimate
\[
\boxed{
\Pr(E)\le
\theta_q A_{q,m}(R_0/p)+
\theta_p A_{p,m}(R_0/q).}
\tag{1}
\]
No independence among the individual membership events is asserted or
needed.

For completeness, center a unit cube at every point of
\(\mathbb Z^m\cap B_2(0,T)\). These cubes have disjoint interiors and their
union lies in \(B_2(0,T+\sqrt m/2)\). Hence
\[
A_{r,m}(T)\le\#(\mathbb Z^m\cap B_2(0,T))
\le v_m(T+\sqrt m/2)^m.
\]
Substitution in (1) proves exactly
\[
\boxed{
\Pr(E)\le
\theta_qv_m\left(\frac{R_0}{p}+\frac{\sqrt m}{2}\right)^m
+\theta_pv_m\left(\frac{R_0}{q}+\frac{\sqrt m}{2}\right)^m.}
\tag{2}
\]
Because (1) bounds the existence of a successful shortest vector, all ties
are covered. In particular, (2) also bounds the event that all shortest
vectors are successful, or that any specified exact solver returns one.

## Uniform asymptotic bound for the actual event

Fix \(u\ge1\), \(\kappa\ge1\), and \(K>0\). Let \(N=pq\to\infty\) through
distinct primes satisfying
\[
p\le q\le\kappa p,
\qquad
u<m\le(\log N)^K.
\]
Then
\[
\sqrt{N/\kappa}\le p\le\sqrt N\le q\le\sqrt{\kappa N}.
\tag{3}
\]
We prove uniformly over all these choices that
\[
\Pr(E)\le N^{-u/2+o(1)}.
\tag{4}
\]

We will use
\[
v_m=\frac{\pi^{m/2}}{\Gamma(m/2+1)}
=\frac{(2\pi e/m)^{m/2}}{\sqrt{\pi m}}(1+O(1/m)).
\tag{5}
\]
Thus, with \(a_m:=2v_m^{-1/m}\) and \(s_m:=\sqrt m/2\),
\[
\log v_m=-\tfrac12m\log m+O(m),
\quad
\log a_m=\tfrac12\log m+O(1),
\quad
\frac{s_m}{a_m}=O(1).
\tag{6}
\]
All constants implicit below may depend on the fixed \(u,\kappa,K\), but not
on \(p,q,m,N\). Also, since \(m\ge2\),
\[
\theta_r\le 2r^{u-m}.
\tag{7}
\]

### 1. The range \(u<m<2u\)

Here \(m\) ranges over a fixed finite set. By (3),
\[
\frac{R_0}{p}\le\frac{R_M}{p}
\le a_m\sqrt\kappa\,N^{1/2-u/m}=o(1),
\qquad
\frac{R_0}{q}\le\frac{R_0}{p}.
\]
Both radii are therefore strictly less than \(1\) for all sufficiently large
\(N\), uniformly over this range. A nonzero integer vector has Euclidean norm
at least \(1\), so both eligible counts in (1) are zero. Thus
\[
\boxed{\Pr(E)=0\quad\text{eventually when }u<m<2u.}
\tag{8}
\]
This conclusion comes from the exact count (1). The padded cube-volume
right-hand side in (2) need not have exponent \(-u/2+o(1)\) in this range,
and no such claim about that literal right-hand side is being made.

### 2. The boundary \(m=2u\)

Now \(m\) is fixed, and
\[
R_0/p\le a_m\sqrt{q/p}\le a_m\sqrt\kappa,
\qquad
R_0/q\le a_m\sqrt{p/q}\le a_m.
\]
The two eligible counts in (1) are consequently \(O_{u,\kappa}(1)\). From
(7), (3), and \(m=2u\),
\[
\theta_q=O(q^{-u})=O(N^{-u/2}),
\qquad
\theta_p=O(p^{-u})=O(N^{-u/2}).
\]
Equation (1) gives \(\Pr(E)=O(N^{-u/2})\).

### 3. The range \(m\ge2u+1\) with \(R_M\le N\)

Here \(R_0=R_M=a_mN^{1-u/m}\). Factoring the principal radius out of the
first term of (2) and using (7) gives
\[
\begin{aligned}
\theta_qv_m(R_M/p+s_m)^m
&\le 2q^{u-m}v_m(R_M/p)^m
 \left(1+\frac{s_mp}{R_M}\right)^m\\
&=2^{m+1}p^{-u}
 \left(1+\frac{s_m}{a_m}pN^{-1+u/m}\right)^m.
\end{aligned}
\tag{9}
\]
The cancellation in the last line uses \(a_m^mv_m=2^m\) and \(N=pq\).
Similarly,
\[
\theta_pv_m(R_M/q+s_m)^m
\le2^{m+1}q^{-u}
 \left(1+\frac{s_m}{a_m}qN^{-1+u/m}\right)^m.
\tag{10}
\]
By (3), (6), and \(u/m<1/2\), the quantities added to \(1\) in (9) and
(10) are bounded uniformly (the latter by a constant also depending on
\(\kappa\)).

It remains to control the apparent exponential in \(m\). The branch
condition is
\[
a_m\le N^{u/m},
\qquad\text{so}\qquad m\log a_m\le u\log N.
\tag{11}
\]
By (6), for all sufficiently large \(m\),
\(\log a_m\ge\frac14\log m\). Thus (11) implies
\(m\log m=O_u(\log N)\), and hence, uniformly on this branch,
\[
m=O_u(\log N/\log\log N)=o(\log N).
\tag{12}
\]
(Bounded \(m\) trivially satisfies the same \(o(\log N)\) conclusion.)
Equations (3), (9), (10), and (12) now yield
\[
\Pr(E)\le(p^{-u}+q^{-u})\exp(O(m))
\le N^{-u/2+o(1)}.
\tag{13}
\]

### 4. The range \(m\ge2u+1\) with \(R_M>N\)

Here \(R_0=N\), so \(R_0/p=q\) and \(R_0/q=p\). Equations (2) and (7) give
\[
\Pr(E)\le
2v_mq^u(1+s_m/q)^m+2v_mp^u(1+s_m/p)^m.
\tag{14}
\]
The dimension cap and (3) imply
\[
m\log(1+s_m/p)\le\frac{m^{3/2}}{2p}
\le O\!\left(\frac{(\log N)^{3K/2}}{\sqrt N}\right)=o(1),
\tag{15}
\]
and the \(q\) factor is no larger. It remains to use the branch condition,
not merely discard the small unit-ball volume. Since
\[
a_m>N^{u/m}
\quad\text{and}\quad
a_m^m=\frac{2^m}{v_m},
\]
we have
\[
v_m<2^mN^{-u}.
\tag{16}
\]
This already gives \(v_m\le N^{-u+o(1)}\) when
\(m\le \log N/\sqrt{\log\log N}\). Above that threshold, (6) gives, for
large \(N\),
\[
\log v_m\le-\tfrac14m\log m\le-2u\log N,
\tag{17}
\]
because
\[
\frac{\log N}{\sqrt{\log\log N}}\,
\frac{\log(\log N/\sqrt{\log\log N})}{\log N}\longrightarrow\infty.
\]
Together, (16)--(17) prove uniformly throughout this branch that
\[
v_m\le N^{-u+o(1)}.
\tag{18}
\]
Finally (3), (14), (15), and (18) give
\[
\Pr(E)\le O(v_mN^{u/2})=N^{-u/2+o(1)}.
\tag{19}
\]

The four cases prove (4), with every \(o(1)\) uniform over balanced
\(p,q\) and all \(u<m\le(\log N)^K\).

## Scope

The result concerns independent uniform linear-code lattices and exact
shortest vectors. It does not settle arithmetically generated biased or
dependent code ensembles, CVP outputs, LLL outputs, nonshortest-vector
observables, or nonlinear observables; those remain open here. The finite
union bound happens to use only the stated uniform marginal inclusion
probabilities, but no broader arithmetic-code model is claimed.
