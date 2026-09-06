# F217 proof

## 1. Elementary identities and the exact exceptional input

The relation \(N=2K+1\) gives

\[
pq\equiv1\pmod K.
\tag{1}
\]

Neither hidden prime divides \(K\). Indeed,

\[
2K=pq-1\equiv-1\pmod p
\]

and similarly modulo \(q\). Thus \(p,q\in G\), and (1) gives

\[
q\equiv p^{-1}\pmod K.
\tag{2}
\]

Both factors are strictly smaller than \(K\):

\[
2(K-q)=q(p-2)-1>0
\]

because \(p\ge3\) and \(q\ge5\), and then \(p<q<K\).

The relation between \(p+q\) and \(K\) has one exact exception. If
\(p=3\), the only odd prime satisfying \(3<q<6\) is \(q=5\). This gives

\[
N=15,\qquad K=7,\qquad p+q=8>K.
\tag{3}
\]

If \(p\ge5\), then \(q\ge7\), and

\[
\begin{aligned}
2(K-p-q)
&=pq-1-2p-2q\\
&=(p-2)(q-2)-5\\
&\ge3\cdot5-5=10.
\end{aligned}
\tag{4}
\]

Hence \(0<p+q<K\) for every allowed input other than \(N=15\).
This proves both the claimed range and the completeness of the exception.

Finally, \(N\equiv3\pmod4\) implies

\[
K=\frac{N-1}{2}\equiv1\pmod2.
\tag{5}
\]

Since the smallest allowed semiprime is \(15\), one also has \(K>1\).

## 2. Every character divisor coefficient is an inversion trace

The four positive divisors of \(N\) are \(1,p,q,N\). For every character
\(\chi\) of \(G\), equations (1) and (2) give

\[
\chi(N)=1,\qquad \chi(q)=\chi(p)^{-1}.
\]

Therefore

\[
\boxed{
D_N(\chi)
=2+\chi(p)+\chi(p)^{-1}.}
\tag{6}
\]

The nonconstant part is real and is the character trace of the inversion
orbit \(\{p,p^{-1}\}\). Ordinary character multiplicativity evaluates
only

\[
\chi(p)\chi(q)=1;
\]

it does not evaluate the sum in (6).

## 3. Proof of the \(2r-1\) trace decoder

Write the hidden coordinate tuple as

\[
\iota^{-1}(p)=(a_1,\ldots,a_r),
\qquad a_i\in\mathbb Z/m_i\mathbb Z.
\]

For the coordinate character \(\chi_i\), subtracting the public constant
two from (6) gives

\[
t_i
=D_N(\chi_i)-2
=2\cos(2\pi a_i/m_i).
\tag{7}
\]

### 3.1 Recovering one coordinate up to inversion

For two integers \(a,b\), the cosine identity gives

\[
\begin{aligned}
&\left|
2\cos(2\pi a/m)-2\cos(2\pi b/m)
\right|\\
&\qquad
=4\left|
\sin\!\left(\frac{\pi(a+b)}m\right)
\sin\!\left(\frac{\pi(a-b)}m\right)
\right|.
\end{aligned}
\tag{8}
\]

If \(a\not\equiv\pm b\pmod m\), neither sine factor vanishes. For every
integer \(c\not\equiv0\pmod m\),

\[
\left|\sin(\pi c/m)\right|
\ge\sin(\pi/m)\ge\frac2m.
\tag{9}
\]

The last inequality follows from concavity of sine on
\([0,\pi/2]\). Hence distinct inversion orbits in one coordinate have
trace separation at least

\[
\boxed{\frac{16}{m^2}.}
\tag{10}
\]

The function \(a\mapsto2\cos(2\pi a/m)\) is strictly decreasing for
\(0\le a\le\lfloor m/2\rfloor\). Certified comparisons and binary search
on this interval recover the unique representative of
\(\{a,-a\}\) in \(O(\log m)\) comparisons. This avoids enumeration of
the \(m\) possible exponents.

A coordinate is self-inverse exactly when

\[
2a_i\equiv0\pmod{m_i},
\]

equivalently when its trace is \(2\) or \(-2\). The same separation
bound certifies this test.

### 3.2 Aligning the coordinate signs

If every coordinate is self-inverse, the coordinate tuple is already
unique under global inversion, and no cross trace is required.

Otherwise, choose an active coordinate \(i_0\) and fix either of its two
orientations. For another active coordinate \(i\), the two possible
relative orientations predict

\[
\begin{aligned}
u_+
&=2\cos\!\left(
\frac{2\pi a_{i_0}}{m_{i_0}}
+\frac{2\pi a_i}{m_i}\right),\\
u_-
&=2\cos\!\left(
\frac{2\pi a_{i_0}}{m_{i_0}}
-\frac{2\pi a_i}{m_i}\right).
\end{aligned}
\tag{11}
\]

These are exactly the two candidate values of
\(D_N(\chi_{i_0}\chi_i)-2\). Their difference is

\[
|u_+-u_-|
=4\left|
\sin(2\pi a_{i_0}/m_{i_0})
\sin(2\pi a_i/m_i)
\right|.
\tag{12}
\]

Activity says that neither doubled exponent is zero modulo its
coordinate order. Applying (9) to the doubled residues yields

\[
\boxed{
|u_+-u_-|
\ge\frac{16}{m_{i_0}m_i}.}
\tag{13}
\]

Thus one product trace aligns coordinate \(i\) with the anchor.
Self-inverse coordinates need no alignment. Reversing the anchor reverses
every active coordinate, so the two surviving tuples are exactly global
inverses.

### 3.3 Precision, query count, and reconstruction

Every coordinate order satisfies

\[
m_i\le |G|=\varphi(K)<K<N<2^n.
\tag{14}
\]

The lower bounds (10) and (13) are therefore larger than
\(2^{4-2n}\). Certified intervals of absolute radius
\(2^{-4n-20}\), together with the same or better precision for the
candidate cosine values, are disjoint by a wide margin. All comparisons
above are consequently exact. Standard high-precision evaluation of
elementary functions to \(O(n)\) bits and \(O(n)\) binary-search steps
per coordinate are polynomial-time subroutines; they do not materialize
an algebraic number field of degree \(\varphi(K)\).

The decoder makes \(r\) coordinate queries and at most one cross query
for every active coordinate other than the anchor. The total is at most

\[
r+(r-1)=2r-1.
\tag{15}
\]

Since every \(m_i\ge2\),

\[
2^r\le\prod_i m_i=|G|<2^n,
\]

so \(r<n\), and in particular \(2r-1\le2n-1\).

Apply the supplied forward map \(\iota\) to either aligned tuple. This
produces residues \(u,u^{-1}\in G\). For the true data they are
\(p,q\), and Section 1 proves that both residues already lie in
\((0,K)\) as integers. Exact multiplication by \(N\) certifies the
answer. This completes Theorem A.

The proof used the supplied inverse coordinate map to define and encode
the coordinate characters, and the supplied forward map to reconstruct
the residue. It did not derive either map, or the divisor-coefficient
evaluator, from \(\operatorname{factor}(K)\).

## 4. The tautological group-algebra specialization

In \(\mathbb Z[G]\), the four-divisor expansion and equations (1)--(2)
give

\[
\mathcal A_N
=[1]+[p]+[q]+[N]
=2[1]+[p]+[p^{-1}].
\tag{16}
\]

The assignment \([a]\mapsto a\bmod K\) is induced by the group
homomorphism

\[
G\longrightarrow(\mathbb Z/K\mathbb Z)^\times,\qquad a\longmapsto a.
\]

It therefore extends linearly and multiplicatively to the asserted ring
map \(\Theta_K\). Applying it to (16) yields

\[
\Theta_K(\mathcal A_N)
\equiv2+p+q\pmod K.
\tag{17}
\]

This is also the elementary identity

\[
\Theta_K(\mathcal A_N)
\equiv\sum_{d\mid N}d
=\sigma_1(N)\pmod K.
\]

For \(N\ne15\), equation (4) shows that the least residue after
subtracting two is the integer \(s=p+q\). Then

\[
s^2-4N=(q-p)^2
\]

is a perfect square, and

\[
p=\frac{s-\sqrt{s^2-4N}}2,\qquad
q=\frac{s+\sqrt{s^2-4N}}2.
\tag{18}
\]

Exact squareness, parity, and multiplication checks certify the result.
For \(N=15\), trial division by three gives the factors. This proves
Theorem B.

## 5. The moving-weight Eisenstein coefficient

The prime factorization of \(K\) computes

\[
\varphi(K)
=K\prod_{\ell\mid K}\left(1-\frac1\ell\right)
\tag{19}
\]

with polynomial-bit arithmetic. By (5), \(K>1\) is odd, so
\(\varphi(K)\) is even. Thus

\[
k=\varphi(K)+2
\]

is an even integer at least four, and the holomorphic level-one
Eisenstein series in Theorem C exists.

Every divisor \(d\mid N\) is coprime to \(K\). Euler's theorem gives

\[
d^{\varphi(K)}\equiv1\pmod K,
\]

and hence

\[
d^{k-1}=d^{\varphi(K)+1}\equiv d\pmod K.
\tag{20}
\]

The stated normalization

\[
\mathcal G_k=-\frac{B_k}{2k}E_k
\]

has nonconstant coefficient

\[
[q^m]\mathcal G_k=\sigma_{k-1}(m)
\]

exactly. Summing (20) over \(d\mid N\) proves

\[
[q^N]\mathcal G_k
=\sigma_{k-1}(N)
\equiv\sigma_1(N)\pmod K.
\tag{21}
\]

The rational Bernoulli constant is irrelevant to this coefficient
congruence; no reduction of that constant modulo \(K\) is asserted.
Combining (21) with Section 4 proves the conditional factor transition.

### 5.1 Output size versus standard numeric state

For an odd prime power \(\ell^e\),

\[
\frac{\ell^e}{\varphi(\ell^e)^2}
=\frac{\ell^{2-e}}{(\ell-1)^2}\le1.
\tag{22}
\]

For \(e=1\), the largest odd-prime value is
\(3/4\); for \(e\ge2\), the value is at most \(1/4\).
Multiplying (22) over the prime powers dividing \(K\) gives

\[
\frac K{\varphi(K)^2}\le1,
\qquad
\boxed{\varphi(K)\ge\sqrt K.}
\tag{23}
\]

Since \(K=(N-1)/2\), this is \(2^{\Omega(n)}\). Standard dense
level-one weight-\(k\) methods use a space of dimension
\(\dim M_k=\Theta(k)\), and the usual symmetric-power coefficient module
has dimension \(k-1\). These are numeric-exponential state sizes.

For the present semiprime,

\[
\sigma_{k-1}(N)
=1+p^{k-1}+q^{k-1}+N^{k-1}.
\tag{24}
\]

Its binary length is bounded below by
\((k-1)\log_2N\) and above by that quantity plus a constant. It is
therefore \(\Theta(kn)\), also exponential in \(n\).

By contrast, \(k\) in binary, a residue modulo \(K\), and the requested
output all have \(O(n)\) bits. Equations (23)--(24) rule out only
algorithms that materialize the standard numeric weight state or the
unrestricted exact coefficient. They do not rule out computation
directly modulo \(K\) from a succinct binary weight.

## 6. Eta-quotient modularity in the prime-\(K\) subfamily

Assume \(K=r\) is prime. Since \(N\ge15\),

\[
r=\frac{N-1}{2}\ge7.
\]

The powers of \(q\) in the eta quotient cancel:

\[
\frac{\eta(\tau)^r}{\eta(r\tau)}
=\frac{q^{r/24}P(q)^r}{q^{r/24}P(q^r)}
=F_r(q).
\tag{25}
\]

For the eta quotient with level \(r\), the exponents are

\[
r_1=r,\qquad r_r=-1.
\]

Its weight is \(w=(r-1)/2\). The two eta-quotient congruences are

\[
\sum_{\delta\mid r}\delta r_\delta=r-r=0\pmod{24},
\tag{26}
\]

and

\[
\sum_{\delta\mid r}\frac r\delta r_\delta
=r^2-1=0\pmod{24}.
\tag{27}
\]

For an odd prime \(r>3\), one has \(r^2\equiv1\pmod8\) and
\(r^2\equiv1\pmod3\), proving (27). The eta-quotient transformation
criterion therefore makes \(F_r\) a weight-\(w\) modular form on
\(\Gamma_0(r)\). The eta-quotient character formula uses the square class

\[
\prod_{\delta\mid r}\delta^{r_\delta}=r^{-1}.
\]

Since \(r^{-1}\) and \(r\) differ by the rational square \(r^{-2}\), the
character on integers coprime to \(r\) is

\[
\chi_r(d)=
\left(\frac{(-1)^w r}{d}\right),
\tag{28}
\]

in Kronecker-symbol notation.

There are only two cusps. Equation (25) gives

\[
F_r(q)=1+O(q)
\]

at infinity. At the other cusp, apply the Fricke matrix. The eta
transformation

\[
\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)
\]

shows, up to a nonzero constant depending only on the slash convention,

\[
F_r\big|_w W_r
\ \doteq\
\frac{\eta(r\tau)^r}{\eta(\tau)}.
\tag{29}
\]

The right side has leading exponent

\[
\frac{r^2}{24}-\frac1{24}
=\frac{r^2-1}{24}>0.
\tag{30}
\]

Thus \(F_r\) is holomorphic at the cusp zero as well. Eta has no zeros
in the upper half-plane, so the negative exponent in the quotient creates
no interior pole. This proves the exact modularity scope asserted in
Theorem D. No claim is made for \(r=2\) or \(r=3\), which do not occur
in the semiprime subfamily.

## 7. Eta coefficient congruence modulo \(r^2\)

For \(1\le j\le r-1\),

\[
\frac{(-1)^j}{r}\binom rj
=\frac{(-1)^j}{j}\binom{r-1}{j-1}
\equiv-\frac1j\pmod r.
\tag{31}
\]

Consequently, as a formal power series,

\[
\frac{(1-x)^r}{1-x^r}
\equiv
1-r\sum_{j=1}^{r-1}
\frac{x^j}{j(1-x^r)}
\pmod{r^2}.
\tag{32}
\]

Substitute \(x=q^a\) and multiply over \(a\ge1\). For each fixed
coefficient only finitely many factors contribute, and every product of
two nonconstant correction terms is divisible by \(r^2\). Hence

\[
F_r(q)
\equiv1-r
\sum_{a\ge1}\sum_{j=1}^{r-1}\sum_{h\ge0}
j^{-1}q^{a(j+hr)}
\pmod{r^2}.
\tag{33}
\]

Fix \(m\) with \(r\nmid m\). For every divisor \(a\mid m\), set
\(b=m/a\). There is a unique pair

\[
1\le j\le r-1,\qquad h\ge0,
\qquad b=j+hr.
\]

Its contribution in (33) is

\[
j^{-1}\equiv b^{-1}
\equiv a\,m^{-1}\pmod r.
\]

Summing over \(a\mid m\) proves

\[
-\frac{[q^m]F_r}{r}
\equiv m^{-1}\sum_{a\mid m}a
=m^{-1}\sigma_1(m)\pmod r.
\tag{34}
\]

Equation (33) first shows that \([q^m]F_r\) is divisible by \(r\).
If its residue modulo \(r^2\) is supplied, choose the unique multiple of
\(r\) representing that residue and divide by \(r\); the quotient is
well-defined modulo \(r\).

For \(m=N=2r+1\), one has \(N\equiv1\pmod r\), so (34) becomes

\[
-\frac{[q^N]F_r}{r}
\equiv\sigma_1(N)
\equiv2+p+q\pmod r.
\tag{35}
\]

Section 4 gives factor recovery, including the explicit \(N=15\)
exception. This proves the coefficient part of Theorem D.

## 8. The exact eta logarithmic derivative

The Euler product satisfies

\[
q\frac d{dq}\log P(q)
=-\sum_{a\ge1}\frac{aq^a}{1-q^a}
=-\sum_{m\ge1}\sigma_1(m)q^m
=-L(q).
\tag{36}
\]

Using \(F_r=P(q)^r/P(q^r)\) and the chain rule,

\[
q\frac d{dq}\log F_r
=-rL(q)+rL(q^r).
\]

Multiplication by \(-1/r\) proves

\[
-\frac1r q\frac d{dq}\log F_r
=L(q)-L(q^r).
\tag{37}
\]

This is an exact identity over characteristic zero, not only a congruence.
It also shows why iterated \(r\)-adic extraction from the eta quotient
returns to the same Lambert-series coefficient problem.

## 9. Twisted Ramanujan identity

For fixed \(n\), the Ramanujan sum has the divisor formula

\[
c_m(n)=\sum_{e\mid(m,n)}e\,\mu(m/e).
\tag{38}
\]

For \(\Re(s)>0\), the bound

\[
|c_m(n)|\le\sum_{e\mid n}e=\sigma_1(n)
\]

makes

\[
\sum_{m\ge1}\frac{\chi(m)c_m(n)}{m^{s+1}}
\]

absolutely convergent. Substitute (38), interchange the absolutely
convergent sums, and write \(m=ek\):

\[
\begin{aligned}
\sum_{m\ge1}\frac{\chi(m)c_m(n)}{m^{s+1}}
&=\sum_{e\mid n}\sum_{k\ge1}
\frac{\chi(ek)e\mu(k)}{(ek)^{s+1}}\\
&=\left(\sum_{e\mid n}\chi(e)e^{-s}\right)
\left(\sum_{k\ge1}
\frac{\chi(k)\mu(k)}{k^{s+1}}\right)\\
&=\frac{A_{\chi,s}(n)}{L(s+1,\chi)}.
\end{aligned}
\tag{39}
\]

The last equality is the absolutely convergent Euler product for the
reciprocal Dirichlet \(L\)-function. Rearranging proves the first identity
in Theorem E.

Since \(A_{\chi,s}(1)=1\) and \(c_m(1)=\mu(m)\), subtraction gives

\[
A_{\chi,s}(N)-1
=L(s+1,\chi)
\sum_{m\ge1}
\frac{\chi(m)(c_m(N)-\mu(m))}{m^{s+1}}.
\tag{40}
\]

If \(m<p\), then \((m,N)=1\), so (38) gives

\[
c_m(N)=\mu(m).
\]

At \(m=p\),

\[
c_p(N)=\mu(p)+p\mu(1)=p-1,
\]

and therefore

\[
c_p(N)-\mu(p)=p.
\tag{41}
\]

Also \((p,K)=1\), so \(\chi(p)\ne0\). The first nonzero
factor-sensitive summand is precisely

\[
\chi(p)p^{-s}.
\]

On balanced inputs \(p>\sqrt{N/2}=2^{\Omega(n)}\), proving the direct
termwise boundary.

The finite divisor sum \(A_{\chi,s}(N)\) has a limit at \(s=0\).
For nonprincipal \(\chi\), equation (40) may therefore be carried to the
boundary by taking \(s\downarrow0\), or by analytic continuation. The
proof above establishes ordinary absolute convergence only for
\(\Re(s)>0\). For the principal character, \(L(1,\chi)\) has a pole, so
no separate \(s=0\) right-side assertion is made.

## 10. Hecke, modular-symbol, and representation boundaries

Because \((N,K)=1\), the standard good-index upper-triangular
representatives for \(T_N\) have

\[
ad=N,\qquad 0\le b<d.
\]

Their number is

\[
\sum_{d\mid N}d=\sigma_1(N).
\tag{42}
\]

For \(N=pq\), the divisor labels explicitly include the hidden \(p,q\),
and the number of representatives is at least \(N\). Thus direct
materialization is exponential in the bit length. Equation (42) does not
exclude an implicit or random-access Hecke algorithm.

The diamond operator uses only the residue of its index modulo the level.
Equation (1) therefore gives

\[
\langle N\rangle=\langle1\rangle.
\tag{43}
\]

This is a scalar level action and is not the correspondence (42).

The standard Manin-symbol presentation at level \(K\) is indexed by a
set comparable to

\[
\mathbb P^1(\mathbb Z/K\mathbb Z),
\]

whose size is

\[
K\prod_{\ell\mid K}\left(1+\frac1\ell\right)\ge K.
\tag{44}
\]

Thus materializing that presentation has exponential numeric state.
Likewise, the standard weight-\(k\) coefficient module has dimension
\(k-1\). These are named-model state counts, not information-theoretic
lower bounds.

For a representation \(\rho:G\to\operatorname{GL}(V)\), the four
divisors and (2) give

\[
\sum_{d\mid N}\rho(d)
=2I+\rho(p)+\rho(p)^{-1}.
\tag{45}
\]

Because \(G\) is finite abelian, every characteristic-zero semisimple
representation over a splitting field is a direct sum of
one-dimensional characters. Thus a matrix representation factoring
through \(G\) packages character traces of the form (6); it does not by
itself evaluate them. A genuinely nonabelian representation that does not
factor through \(G\) is not covered by (44)'s decomposition argument.

Finally, \((K,N)=1\) implies for every integer \(m\)

\[
(Km,N)=(m,N).
\tag{46}
\]

Therefore a formula whose only factor-sensitive dependence on a
multiplier is through this gcd retains the threshold found in
Section 9. The qualification is essential: Kloosterman phases, spectral
weights, or other terms can depend on more than the gcd.

## 11. Recursive cost and conclusion

Replacing \(N\) by \(K=(N-1)/2\) reduces the bit length by one. If a
recursive construction follows only one child, then

\[
T(n)\le T(n-1)+\operatorname{QP}(n)
\]

unrolls to at most \(n\) QP summands and remains QP. A fixed-ratio
bit-length contraction is therefore not necessary for a single chain.
It becomes relevant only if multiple recursive children survive and their
aggregate work is not otherwise controlled.

F217 grants \(\operatorname{factor}(K)\), and none of Theorems A--E
turns that grant alone into the missing evaluator. The exact positive
boundary is now narrow: one must evaluate a compressed divisor
coefficient, not decode an exponentially large orbit once a small
separating bank is available.
