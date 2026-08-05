# Proof-blind reconstruction: the level-two Eisenstein coefficient and factor trace

## Verdict and exact scope

The corrected claim is true, with two interface conventions made explicit:

1. a modular answer is the canonical least nonnegative residue; and
2. the approximation bound is a fixed, explicit, uniformly computable numerical polynomial in the input length.

The result is a conditional oracle reduction. It does **not** construct any coefficient oracle. It gives a deterministic, one-call, worst-case polynomial-bit reduction only on the promise

\[
N=pq,\qquad p\ne q\text{ odd primes}.
\]

Calling this merely a reduction for “semiprimes” is false if that word permits repeated primes or the prime \(2\): the counterexamples \(N=9\) and \(N=6\) are checked below. Nothing here solves arbitrary integer factoring, proves a factoring lower bound, or constrains unrelated modular or automorphic invariants.

Throughout,

\[
q=e^{2\pi i z},\qquad
E_2(z)=1-24\sum_{r\geq 1}\sigma_1(r)q^r,
\]

where \(\sigma_1(r)=\sum_{d\mid r}d\), and

\[
F(z)=2E_2(2z)-E_2(z).
\]

## 1. Modularity, including the cusp \(0\)

The quasimodular transformation law is

\[
E_2\!\left(\frac{az+b}{cz+d}\right)
=(cz+d)^2E_2(z)+\frac{6c}{\pi i}(cz+d)
\tag{1}
\]

for \(\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\in
\mathrm{SL}_2(\mathbb Z)\).

Let

\[
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(2).
\]

Since \(2\mid c\), the matrix

\[
\gamma'=\begin{pmatrix}a&2b\\c/2&d\end{pmatrix}
\]

lies in \(\mathrm{SL}_2(\mathbb Z)\), and

\[
2\gamma z=\gamma'(2z).
\]

Applying (1) to \(\gamma'\) at \(2z\) gives

\[
E_2(2\gamma z)
=(cz+d)^2E_2(2z)+\frac{3c}{\pi i}(cz+d).
\]

After multiplication by \(2\), its anomalous term equals the anomalous term in (1) for \(E_2(\gamma z)\). Hence they cancel:

\[
F(\gamma z)=(cz+d)^2F(z).
\tag{2}
\]

Thus \(F\) has weight \(2\) on \(\Gamma_0(2)\), and it is holomorphic on the upper half-plane. It remains to check the cusps. The two cusp classes of \(\Gamma_0(2)\) are \(\infty\) and \(0\).

At \(\infty\), direct subtraction gives a convergent Fourier series with no negative powers:

\[
F(z)=1+24\sum_{r\geq1}
\left(\sigma_1(r)-2\mathbf 1_{2\mid r}\sigma_1(r/2)\right)q^r.
\tag{3}
\]

For the cusp \(0\), take

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad (F|_2S)(z)=z^{-2}F(-1/z).
\]

The cusp \(0=S\infty\) has width \(2\), so its local parameter is

\[
q_0=e^{2\pi i z/2}=e^{\pi i z}.
\]

Using (1) first with \(z/2\) and then with \(z\),

\[
\begin{aligned}
E_2(-2/z)&=\frac{z^2}{4}E_2(z/2)+\frac{3z}{\pi i},\\
E_2(-1/z)&=z^2E_2(z)+\frac{6z}{\pi i}.
\end{aligned}
\]

Consequently,

\[
(F|_2S)(z)=\frac12E_2(z/2)-E_2(z),
\]

and therefore

\[
(F|_2S)(z)
=-\frac12-12\sum_{r\geq1}\sigma_1(r)q_0^r
+24\sum_{r\geq1}\sigma_1(r)q_0^{2r}.
\tag{4}
\]

There are no negative powers of \(q_0\). This explicitly proves holomorphy at \(0\), including the correct width, rather than merely checking the transformation law on the upper half-plane. Equations (2)–(4) prove

\[
F\in M_2(\Gamma_0(2)).
\]

## 2. Coefficients and arithmetic Hecke normalization

Write

\[
F(z)=1+24\sum_{m\geq1}b_mq^m.
\]

Equation (3) says

\[
b_m=\sigma_1(m)-2\mathbf 1_{2\mid m}\sigma_1(m/2).
\tag{5}
\]

Write \(m=2^a u\), with \(u\) odd. If \(a=0\), (5) is \(\sigma_1(u)\). If \(a\geq1\), multiplicativity of \(\sigma_1\) gives

\[
\begin{aligned}
b_m
&=(2^{a+1}-1)\sigma_1(u)
-2(2^a-1)\sigma_1(u)\\
&=\sigma_1(u).
\end{aligned}
\]

Thus, for every \(m\geq1\),

\[
\boxed{b_m=\sigma_1(m_{\mathrm{odd}})},
\tag{6}
\]

where \(m_{\mathrm{odd}}=m/2^{v_2(m)}\).

Now put

\[
f=F/24=\frac1{24}+\sum_{m\geq1}b_mq^m.
\]

In particular, the coefficient of \(q\) in \(f\) is \(b_1=1\). The standard dimension formula gives

\[
\dim M_2(\Gamma_0(2))=1.
\]

Equivalently, \(X_0(2)\) has genus \(0\), so there are no weight-two cusp forms, while its two cusps contribute a one-dimensional weight-two Eisenstein space. Since \(F\ne0\), \(f\) spans this space.

For odd \(m\), the arithmetic Hecke operator \(T_m\) preserves
\(M_2(\Gamma_0(2))\). With the arithmetic normalization, if
\(g=\sum_{r\geq0}a_rq^r\), then

\[
[q^r](T_mg)=\sum_{d\mid(m,r)}d^{\,2-1}a_{mr/d^2}.
\tag{7}
\]

In particular, \([q](T_mf)=a_m=b_m\). One-dimensionality gives
\(T_mf=\lambda_m f\), and comparison with the \(q\)-coefficient of \(f\), which is \(1\), yields

\[
\boxed{T_m(F/24)=b_m(F/24)\qquad(m\text{ odd}).}
\tag{8}
\]

This is the arithmetic normalization. If one instead divides \(T_m\) by
\(m^{(2-1)/2}=\sqrt m\) to obtain a unitary normalization, the eigenvalue is
\(b_m/\sqrt m\), not \(b_m\). Also, (8) is asserted only away from the level, so it does not silently identify the level operator at \(2\) with this \(T_m\).

## 3. The factor trace on the exact promise

Suppose now that

\[
N=pq
\]

for distinct odd primes \(p<q\). Since \(N\) is odd, (6) gives

\[
\boxed{b_N=\sigma_1(N)=(1+p)(1+q)=N+p+q+1.}
\tag{9}
\]

Thus a value of \(b_N\) reveals the factor trace

\[
s=p+q=b_N-N-1.
\tag{10}
\]

The following exact decoder will be used in all three reductions. Given a candidate integer \(t\), compute

\[
D=t^2-4N.
\]

Reject it if \(D<0\), if its integer square root \(r=\lfloor\sqrt D\rfloor\) does not satisfy \(r^2=D\), or if \(t\not\equiv r\pmod2\). Otherwise set

\[
x=\frac{t-r}{2},\qquad y=\frac{t+r}{2},
\]

and return \((x,y)\) only after verifying

\[
1<x<y<N,\qquad xy=N.
\tag{11}
\]

For \(t=s\), \(D=(q-p)^2\), \(r=q-p\), the parity test passes because both \(s\) and \(r\) are even, and (11) returns \(p,q\). The square, parity, nontriviality, ordering, and product checks ensure that every returned output is correct. No gcd is used, terminal or otherwise.

## 4. Three one-call oracle reductions

All integer inputs and nonnegative exact outputs below use ordinary canonical binary without leading zeroes. A possibly negative approximation uses a sign and canonical binary magnitude. A factor output is the ordered binary pair \(p<q\). These conventions rule out an oracle hiding superpolynomial work in an unbounded or noncanonical output representation.

### 4.1 Exact normalized or unnormalized coefficient

For an oracle returning exact \(b_N\), make one query, form \(s=b_N-N-1\), and invoke the decoder above.

For an oracle returning the exact unnormalized Fourier coefficient

\[
[q^N]F=24b_N,
\]

make one query, verify divisibility by \(24\), divide by \(24\), and do the same. A correct oracle always passes the divisibility test.

### 4.2 The unnormalized coefficient modulo a caller-chosen modulus

Let

\[
n=\lceil\log_2(N+1)\rceil,\qquad
M=2^n,\qquad
\boxed{Q=24M=24\cdot2^n}.
\tag{12}
\]

The modulus has exactly \(n+5\) binary digits, hence \(O(\log N)\) bits. Query once for the canonical least residue

\[
R=[24b_N]_Q,\qquad 0\leq R<Q.
\]

Because \(Q=24M\), this residue is divisible by \(24\), and

\[
\beta=R/24=[b_N]_M,\qquad 0\leq\beta<M.
\tag{13}
\]

Compute

\[
t=[\beta-(N+1)]_M,\qquad 0\leq t<M.
\tag{14}
\]

By (9), \(t\equiv p+q\pmod M\). There is no balance assumption in the following bound:

\[
N+1-(p+q)=(p-1)(q-1)>0.
\tag{15}
\]

Hence

\[
0<p+q<N+1\leq2^n=M.
\tag{16}
\]

The least residue in (14) is therefore exactly \(t=p+q\), not merely a congruence class. The decoder recovers \(p,q\).

The choice \(Q=24M\) is essential to this simple reconstruction: \(24\) is not invertible modulo \(2^n\). Enlarging the modulus by the exact factor \(24\), then dividing the least residue by \(24\), preserves \(b_N\bmod M\).

### 4.3 An exactly encoded integer with known polynomial additive error

Fix as part of the interface a nonnegative explicit function \(K(n)\) satisfying

\[
K(n)\leq Cn^d
\]

for fixed constants \(C,d\), and assume \(K(n)\) is uniformly computable in polynomial time. The oracle returns one exactly encoded signed integer \(A\) satisfying

\[
|A-b_N|\leq K(n).
\tag{17}
\]

Let \(B=\lceil K(n)\rceil\). Make the single oracle call and enumerate every integer

\[
t\in[A-N-1-B,\ A-N-1+B].
\tag{18}
\]

For each \(t\), run the exact decoder in Section 3 and return the first verified pair. Equation (17) ensures that the true trace \(p+q=b_N-N-1\) occurs in (18). There are at most \(2B+1=\operatorname{poly}(n)\) candidates. False candidates cannot cause an incorrect return because of (11).

The fact that \(A\) is an *exactly encoded integer* matters. An unspecified floating-point value, an unknown error bound, or a bound having merely polynomial bit length but exponential numerical size would not justify the polynomial-width enumeration.

## 5. Uniform bit complexity and all bit lengths

The reductions are uniform: the same algorithms and the same fixed \(K\) are used for every input, with no advice depending on \(N,p,q\). The modular oracle must accept every caller-supplied modulus of the allowed \(O(n)\)-bit size; an oracle for only one unrelated fixed modulus would not suffice.

For every promise input,

\[
N+1\leq 2^n,\qquad
p+q<N+1,\qquad
b_N=N+p+q+1<2(N+1)\leq2^{n+1}.
\tag{19}
\]

Thus exact coefficient answers have \(O(n)\) bits; multiplication by \(24\) changes this by only a constant. In the modular interface, \(M,Q,R\) all have \(O(n)\) bits. In the approximation interface, (17) and \(K(n)=\operatorname{poly}(n)\) imply that \(A\), the interval endpoints, and every candidate \(t\) have \(O(n)\) bits (more precisely \(O(n+\log K(n))=O(n)\)). Each discriminant has \(O(n)\) or \(O(2n)\) bits, and exact integer square root, squaring, parity tests, multiplication, division by \(2\) or \(24\), and comparisons all have deterministic polynomial bit complexity. Section 4.3 performs only polynomially many such operations.

There is no asymptotic small-input exception hidden here. Distinct odd-prime promise inputs begin at \(N=3\cdot5=15\). At that boundary,

\[
n=4,\quad M=N+1=16,\quad Q=384,\quad b_{15}=24.
\]

The modular response is

\[
[24b_{15}]_{384}=192,
\]

so \(\beta=8\), and subtracting \(N+1\equiv0\pmod{16}\) gives the exact trace \(8=3+5\). Thus the possible equality \(M=N+1\) causes no endpoint error. Equations (15)–(19), rather than an eventual asymptotic estimate, cover every promise input and every input length at which the promise is nonempty.

Each reduction makes exactly one oracle call. Its non-oracle work is deterministic worst-case polynomial time. If the stipulated oracle itself runs in uniform worst-case polynomial time with these encodings, the composition does too. This is a conditional statement about access to the oracle; no algorithm for producing the oracle response from bare \(N\) has been supplied.

## 6. Converse computation from a supplied complete factorization

Let a complete factorization

\[
m=2^{e_0}\prod_{j=1}^k\ell_j^{e_j}
\]

be supplied, where the \(\ell_j\) are distinct odd primes and the factor \(2^{e_0}\) is omitted when absent. Equation (6) gives the explicit product

\[
\boxed{
b_m=\prod_{j=1}^k
\left(1+\ell_j+\cdots+\ell_j^{e_j}\right)
=\prod_{j=1}^k\frac{\ell_j^{e_j+1}-1}{\ell_j-1}.}
\tag{20}
\]

Repeated squaring and exact integer arithmetic compute (20) in polynomial bit complexity. There are at most \(O(\log m)\) prime factors counted with multiplicity, every exponent is at most \(\log_2m\), and the crude bound

\[
b_m\leq\sigma_1(m)\leq m\,\tau(m)\leq m^2
\]

shows that all exact intermediate/output values may be kept to \(O(\log m)\) bits up to a constant factor. From \(b_m\), one computes \(24b_m\), its canonical residue modulo any \(O(\log m)\)-bit caller modulus, and a valid answer to any admissible approximation relation. For the last interface, simply outputting the exact integer \(A=b_m\) has error zero.

Therefore, on the distinct-odd-semiprime promise:

* factoring reduces deterministically in polynomial time to each interface with one oracle call; and
* a supplied factorization computes each interface in deterministic polynomial time.

For the exact and canonical modular interfaces this is a polynomial-time oracle equivalence of functions on that promise. The approximation interface is a relation rather than a single-valued function; the precise mutual statement is that every valid approximation answer factors the promised input via the decoder, while a factorization produces a valid answer (for example \(A=b_N\)). No implication in the first direction has been proved for arbitrary integers.

## 7. Required hostile boundary checks

### Repeated odd prime: \(N=9\)

Here \(N=3^2\), and

\[
b_9=\sigma_1(9)=1+3+9=13.
\]

The distinct-factor formula would incorrectly give

\[
N+3+3+1=16.
\]

Indeed, the attempted trace \(b_9-N-1=3\) has discriminant

\[
3^2-4\cdot9=-27,
\]

so the decoder rightly returns nothing. The identity
\((1+p)(1+q)\) double-counts the middle divisor when \(p=q\). Distinctness is essential.

### Even semiprime: \(N=6\)

Here \(N=2\cdot3\), but (6) discards the entire \(2\)-part:

\[
b_6=\sigma_1(3)=4.
\]

In contrast,

\[
N+2+3+1=12.
\]

The attempted trace is \(b_6-N-1=-3\), not \(2+3=5\). Oddness is therefore essential. This also illustrates why the Hecke statement was restricted to indices coprime to the level \(2\).

These two examples refute every wording that silently uses “semiprime” to include either \(p^2\) or \(2p\).

## 8. What the reduction does and does not say

The entire computational content is the elementary divisor-sum identity

\[
\sigma_1(pq)=(1+p)(1+q)=pq+p+q+1
\]

for two distinct primes, embedded as a Fourier coefficient of one fixed level-two Eisenstein series. The modular-form calculation identifies the packaging and the exact Hecke normalization; it does not manufacture the coefficient from \(N\). Asking an oracle for \(b_N\) (or enough exact information to recover it) is asking for the factor trace in this promise case.

Accordingly, this proves neither a polynomial-time algorithm for general factoring nor a lower bound against one. It gives no obstruction, algorithm, or equivalence for coefficients of other forms, cusp-form data, periods, \(L\)-values, spectral invariants, geometric invariants, or other automorphic constructions. Those invariants remain untouched unless a separate reduction analyzes them.
