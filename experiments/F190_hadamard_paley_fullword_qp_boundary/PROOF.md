# Proof of the F190 retained-source full-word boundary

## 1. QP accounting and public transcript generation

For fixed \(C,k\),

\[
\log_2\mathcal Q(n)=C(\log_2(n+1))^k=o(n).
\tag{1.1}
\]

Thus \(\mathcal Q(n)=2^{o(n)}\). Multiplying a fixed number of QP
functions adds a fixed number of polynomial-in-\(\log n\) exponents, so the
result is still QP. Multiplication by a polynomial or by \(n\) also preserves
the class.

Given \(M,X,a_j\), Euclid computes \(\gcd(X+a_j,M)\), and the binary Jacobi
algorithm computes \(((X+a_j)/M)\), in polynomial bit complexity. Therefore
QP many rows and columns are still publicly computable in QP bit complexity.
The retained transcript contains no hidden observation: it is a deterministic
function of its public source and \(M\).

Let \(k=\lceil\log_2(M+1)\rceil\), let the decoder use \(m=m(k)\)
consecutive shifts, and trial-divide through

\[
B=4mk.
\tag{1.2}
\]

This costs QP bit operations. If trial division does not split \(M\), every
prime \(r\mid M\) exceeds \(B>m\). The shifts \(0,\ldots,m-1\) are then
distinct modulo every such prime. For uniform \(X\bmod M\), CRT over the
distinct prime-power components gives the exact acceptance probability

\[
\alpha_M=\prod_{r\mid M}(1-m/r).
\tag{1.3}
\]

Since the number \(\omega(M)\) of distinct primes is at most \(k\), the union
bound gives

\[
1-\alpha_M\le m\sum_{r\mid M}{1\over r}
<{mk\over B}={1\over4}.
\tag{1.4}
\]

For each raw source, compute all coordinate gcds. A proper gcd is already a
split. If every gcd is one, the row is accepted. A gcd equal to \(M\) is a
public rejection. Hence an exact independent accepted batch is generated
with constant expected overhead unless the sampling itself factors \(M\)
first.

Assume the retained-source decoder succeeds with probability at least
\(1/Q(k)\), uses at most \(Q(k)\) bit operations, and requests at most
\(Q(k)\) entries, for a fixed QP \(Q\). Fresh-batch repetition has at most
\(Q(k)\) expected attempts and terminates almost surely. Verify every returned
integer by deterministic primality testing and exact division, so no decoder
error can corrupt the answer.

To cover arbitrary inputs, remove powers of two, certify prime nodes, and use
standard exact perfect-power detection. If \(M=A^e\), recursively factor
\(A\) and multiply its exponents by \(e\). Otherwise the gcd of the hidden
prime exponents is one, so not all exponents are even; at least one hidden
prime has odd exponent and is a valid decoder target. Trial division handles
small factors, and the decoder handles the remaining node. Every verified
split strictly reduces the integer, and the complete factor tree has \(O(k)\)
nodes. A polynomial number of QP node costs is QP. This proves the forward
reduction to all-input Las Vegas QP factoring.

Conversely, an all-input Las Vegas QP factorer can ignore the supplied rows,
factor \(M\), select a prime of odd exponent, and, if requested, compute its
local Paley word from the retained sources. This proves the reverse reduction
and the QP equivalence in Section 1 of the statement.

## 2. Fourier support

Use the CRT representation \(t\leftrightarrow(t_p,t_q)\). The additive
character \(\zeta_N^{-at}\) factors into nontrivial local additive characters
whose local frequencies are zero exactly when the corresponding prime divides
\(a\). Therefore the Fourier sum factors as two local quadratic Gauss sums:

\[
\widehat s(a)=G_p(c_pa)G_q(c_qa),
\tag{2.1}
\]

where \(c_p\) and \(c_q\) are units in their respective fields and

\[
G_r(b)=\sum_{u\in\mathbb F_r}\chi_r(u)e_r(-bu).
\tag{2.2}
\]

If \(b=0\), then \(G_r(b)=\sum_u\chi_r(u)=0\). If \(b\ne0\), substitution
by \(b^{-1}\), followed by the standard quadratic Gauss-sum identity, gives

\[
|G_r(b)|=\sqrt r.
\tag{2.3}
\]

The local frequency in (2.1) is nonzero at both primes exactly when
\(\gcd(a,N)=1\). This proves

\[
\widehat s(a)=0\quad((a,N)>1),
\qquad
|\widehat s(a)|=\sqrt{pq}=\sqrt N\quad((a,N)=1).
\tag{2.4}
\]

Fourier inversion now writes

\[
s(t)={1\over N}\sum_{a\in(\mathbb Z/N\mathbb Z)^\times}
\widehat s(a)\zeta_N^{at},
\tag{2.5}
\]

as a sum of exactly \(\varphi(N)\) distinct exponentials with nonzero
coefficients.

Let \(E\) be the shift operator \((Ef)(t)=f(t+1)\). If a nonzero polynomial
\(P\) satisfies \(P(E)s=0\), linear independence of the distinct exponential
sequences in (2.5) forces

\[
P(\zeta_N^a)=0
\quad\text{for every }a\in(\mathbb Z/N\mathbb Z)^\times.
\tag{2.6}
\]

These are the primitive \(N\)-th roots. Thus \(\Phi_N\mid P\), and
\(\deg P\ge\varphi(N)\). Conversely, \(\Phi_N(E)s=0\) follows directly from
(2.5). The minimal recurrence order is exactly \(\varphi(N)\).

The periodic Hankel matrix has the factorization

\[
H=V\,\operatorname{diag}(\widehat s(a)/N)_{(a,N)=1}V^{\mathsf T},
\qquad
V_{i,a}=\zeta_N^{ai}.
\tag{2.7}
\]

The selected columns of the \(N\)-point Fourier matrix are independent, and
the diagonal entries are nonzero. Hence \(\operatorname{rank}_{\mathbb C}H
=\varphi(N)\).

Finally,

\[
N-\varphi(N)=p+q-1<(1+\sqrt2)\sqrt N,
\tag{2.8}
\]

by balance. This proves (9) and the named dense-reconstruction obstruction.
The argument makes no claim against a representation whose description is
much shorter than its recurrence degree.

## 3. Autocorrelation and raw empirical costs

For an odd prime \(r\), define

\[
C_r(d)=\sum_{u\in\mathbb F_r}\chi_r(u)\chi_r(u+d).
\tag{3.1}
\]

If \(d=0\), exactly \(r-1\) summands equal one, so \(C_r(0)=r-1\). If
\(d\ne0\), scaling by \(d\) reduces to
\(\sum_v\chi_r(v(v+1))=-1\), the standard exact quadratic-character sum.
Thus

\[
C_r(d)=\begin{cases}r-1,&r\mid d,\\-1,&r\nmid d.\end{cases}
\tag{3.2}
\]

CRT gives \(C_N(d)=C_p(d)C_q(d)\), which is exactly the four-case formula
in (12). If a nonzero \(d\bmod N\) enters either middle case, then
\(\gcd(d,N)\) is the corresponding hidden prime. Otherwise its complete
correlation is the fixed public value one.

For uniform \(T\bmod N\) and a unit frequency \(a\), let

\[
Z=s(T)\zeta_N^{-aT}.
\tag{3.3}
\]

Then \(|\mathbb EZ|=N^{-1/2}\), while

\[
\mathbb E|Z|^2={\varphi(N)\over N},
\qquad
\operatorname{Var}(Z)={\varphi(N)-1\over N}.
\tag{3.4}
\]

The average of \(R\) independent copies therefore has relative mean-squared
error \((\varphi(N)-1)/R\). This proves the Fourier sampling requirement.

For a unit difference \(d\), let \(W=s(T)s(T+d)\). Its mean is \(1/N\).
Modulo each local prime, exactly two distinct source residues make either
factor zero, so

\[
\mathbb EW^2=(1-2/p)(1-2/q)=\rho_d,
\qquad
\operatorname{Var}(W)=\rho_d-N^{-2}.
\tag{3.5}
\]

The relative mean-squared error of the average of \(R\) copies is therefore
\((N^2\rho_d-1)/R\). The sample lower bounds in the statement concern these
raw empirical averages, not arbitrary estimators with other arithmetic input.

## 4. QP extension of the explicit shifted-correlation channel

Consider one screened shifted-Jacobi monomial. Collect equal shifts and let
\(u\) be the number of distinct shifts. If at least one collected
multiplicity is odd, the squarefree local character-sum bounds used in P53
give

\[
\left|\mathbb E Y_H\right|\le{(u-1)^2\over\sqrt N}.
\tag{4.1}
\]

If every multiplicity is even, the monomial is one precisely when all shifted
arguments are units, and hence

\[
\mathbb E Y_H=(1-u/p)(1-u/q),
\qquad
|\mathbb E Y_H-1|={u(p+q-u)\over N}.
\tag{4.2}
\]

On the balanced family, both (4.1) and (4.2) are
\(O(u^2/\sqrt N)\). If a list has coefficient \(\ell_1\)-norm at most
\(\mathcal Q(n)\) and every \(u\le\mathcal Q(n)\), its drift from the
corresponding public baseline is at most

\[
{\mathcal Q(n)^3\over\sqrt N}
=2^{-n/2+o(n)}.
\tag{4.3}
\]

The scalar sequential simulator in P53 has, on a \(\sqrt2\)-balanced
semiprime and pathwise total support \(T\), total-variation error at most

\[
{2\sqrt2T+T^2/2\over\sqrt N}.
\tag{4.4}
\]

Putting \(T\le\mathcal Q(n)\) again gives \(2^{-n/2+o(n)}\). This proves the
claimed polynomial-to-QP extension inside exactly P53's observation model.
It does not convert P53 into a theorem about a retained source or full word.

## 5. Short-puncture list formulas

Fix distinct \(a_1,\ldots,a_m\bmod r\). For nonempty
\(S\subseteq[m]\), put \(t=|S|\). The complete sum

\[
A_r(S)=\sum_{x\in\mathbb F_r}
\chi_r\!\left(\prod_{j\in S}(x+a_j)\right)
\tag{5.1}
\]

has a squarefree degree-\(t\) polynomial. For \(t=1\), it is zero. For
\(t\ge2\), the standard squarefree quadratic-character bound gives

\[
|A_r(S)|\le(t-1)\sqrt r.
\tag{5.2}
\]

Passing from the complete sum to \(B_r(S)\) removes the \(m-t\) excluded
roots not indexed by \(S\). Each removed summand has magnitude one. Therefore

\[
|B_r(S)|\le(t-1)\sqrt r+(m-t)
\le(m-1)\sqrt r.
\tag{5.3}
\]

On the accepted domain, every character value is a sign, so the exact
indicator for local word \(\epsilon\) is

\[
2^{-m}\prod_{j=1}^m(1+\epsilon_j\chi_r(x+a_j)).
\tag{5.4}
\]

Summing and expanding proves (17). The empty term is \((r-m)/2^m\); bounding
all \(2^m-1\) nonempty terms by (5.3) proves its error bound.

For a pair \((x,z)\) over \(p,q\), the indicator that the product word equals
\(y\) is

\[
2^{-m}\prod_{j=1}^m
\left(1+y_j\chi_p(x+a_j)\chi_q(z+a_j)\right).
\tag{5.5}
\]

Summing over both accepted local domains and expanding proves

\[
F_y=2^{-m}\sum_SY_S B_p(S)B_q(S).
\tag{5.6}
\]

The empty term is \((p-m)(q-m)/2^m\). For every nonempty term,

\[
|B_p(S)B_q(S)|\le(m-1)^2\sqrt{pq}=(m-1)^2\sqrt N.
\tag{5.7}
\]

After multiplication by \(2^{-m}\), the sum of the \(2^m-1\) errors is at
most \((m-1)^2\sqrt N\). This proves (19).

Now fix \(\delta>0\) and assume (20). Balance and \(m=O(n)\) give

\[
(p-m)(q-m)=N(1-o(1)).
\tag{5.8}
\]

The ratio of the error in (19) to \(N/2^m\) is at most

\[
{m^2 2^m\over\sqrt N}
\le m^2N^{-\delta}=o(1).
\tag{5.9}
\]

This proves (21) uniformly in \(y\). If \(m=(\log n)^{O(1)}\), then
\(2^m=2^{(\log n)^{O(1)}}\) is QP and

\[
{N\over2^m}=2^{n-o(n)}.
\tag{5.10}
\]

Conversely, the inequality \(N/2^m\le\mathcal Q(n)\) forces
\(m\ge\log_2N-(\log n)^{O(1)}\). Then \(2^m=2^{\Theta(n)}\). This last
entropy calculation does not assert that (19) is sharp near \(m=n\); it only
shows why brute sign-splitting is not a QP bridge between the two regimes.

Each pair \((x,z)\) corresponds to one global source by CRT. Therefore this
is exactly a row-only product-code list count. Once the numerical global
source is retained, it labels that CRT pair relative to the hidden moduli;
the list theorem alone gives no indistinguishability result for \((X,Y(X))\).

## 6. Long-word distance caveat

Fix distinct \(x,z\in\mathbb F_r\). For shifts \(a\ne-x,-z\), agreement
minus disagreement equals

\[
\sum_{a\in\mathbb F_r}\chi_r((a+x)(a+z))=-1.
\tag{6.1}
\]

There are \(r-2\) common-unit shifts. If \(A\) and \(D\) are their agreement
and disagreement counts, then

\[
A+D=r-2,
\qquad A-D=-1,
\tag{6.2}
\]

so

\[
D={r-1\over2}.
\tag{6.3}
\]

Choose \(m\) distinct shifts uniformly without replacement. For this fixed
source pair, the selected disagreement count is hypergeometric with mean

\[
\mu=m{r-1\over2r}\ge {m\over3}.
\tag{6.4}
\]

The multiplicative lower-tail bound for hypergeometric sampling gives

\[
\Pr[D_{x,z}<m/6]
\le\Pr[D_{x,z}<\mu/2]
\le e^{-\mu/8}
\le e^{-m/24}.
\tag{6.5}
\]

There are fewer than \(r^2/2\) unordered source pairs. For
\(m\ge96\ln r\), the union bound is less than
\(r^2e^{-4\ln r}=r^{-2}\). Hence, with probability at least \(1-r^{-2}\),
all local source words have relative distance at least \(1/6\). This proves
that distance cannot be used as a universal obstruction at \(m=\Theta(n)\).
It supplies no efficient decoder and presumes the local code indexed by the
known modulus \(r\).

## 7. Independent and polynomially correlated collision bounds

Let

\[
U_r=\mathbb F_r\setminus\{-a_1,\ldots,-a_m\}.
\tag{7.1}
\]

An accepted global source has independent local coordinates uniform on
\(U_p\) and \(U_q\). Sources in different rows are independent. For fixed
arguments \(X_i+a_j\) and \(X_h+a_\ell\) in two different rows, and for
each fixed value of the first local source, at most one value of the second
local source creates equality modulo \(r\). Thus

\[
\Pr[X_i+a_j=X_h+a_\ell\pmod r]\le{1\over r-m}.
\tag{7.2}
\]

Within one row, equality is impossible on the screened branch. A union bound
over fewer than \(\binom K2\) cross-row pairs proves (24). Since
\(K,m=2^{o(n)}\) and \(p,q=2^{n/2+O(1)}\), its right side is
\(2^{-n/2+o(n)}\). Solving \(K^2/p=\Theta(1)\) gives the birthday scale
\(K=\Theta(\sqrt p)=2^{n/4+O(1)}\).

For the correlated-source claim, lift each coefficient of \(P_\nu\) to an
integer and compute its gcd with \(N\). On a no-factor branch, each
coefficient is either zero modulo both primes or a unit modulo both primes.
If not all coefficients vanish modulo \(N\), at least one coefficient is a
unit. Hence the reduced polynomial is nonzero over each of
\(\mathbb F_p\) and \(\mathbb F_q\). For sufficiently large \(n\),
\(D<p,q\), and the elementary root bound gives

\[
\Pr[P_\nu(Z)=0\pmod p]\le D/p,
\qquad
\Pr[P_\nu(Z)=0\pmod q]\le D/q.
\tag{7.3}
\]

The union bound over \(H\) polynomials proves (25). Conditioning on an event
of probability \(\alpha\ge\alpha_0>0\) multiplies any probability by at most
\(1/\alpha_0\). For a past-adaptive protocol with a fresh uniform source,
fix the past first and apply the same bound to its now-fixed polynomial menu.
Taking all differences \(g_i-g_j\) gives \(H\le\binom K2\) and proves the
stated equality-test special case.

No step treats a succinct exponential-degree polynomial as degree QP. No step
controls a nonlinear rule that repeatedly reuses one retained source. Those
are part of the surviving interface, not consequences of the collision
bound.
