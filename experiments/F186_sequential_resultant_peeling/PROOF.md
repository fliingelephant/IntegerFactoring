# Proof of the F186 one-child sequential peeling theorem

## 1. Local orders under one peeling step

Fix a hidden component \(R_j=p_j^{e_j}\). Let

\[
h_{j,i}=\operatorname{ord}_{R_j}(v_i).
\tag{1}
\]

Repeated use of the order-of-a-power formula gives

\[
h_{j,i}
=\frac{g_j}{\gcd\!\left(g_j,\prod_{r=1}^i A_r^n\right)}.
\tag{2}
\]

In particular, every \(h_{j,i}\) divides \(g_j\). It is therefore coprime
to \(N\). If it is nontrivial, all its rational-prime divisors exceed
\(T\).

The kernel of reduction

\[
(\mathbb Z/p_j^{e_j}\mathbb Z)^\times
\longrightarrow
(\mathbb Z/p_j\mathbb Z)^\times
\tag{3}
\]

is a \(p_j\)-group. Since \(h_{j,i}\) is coprime to \(p_j\), reduction is
injective on \(\langle v_i\rangle\). Hence

\[
v_i=1\pmod {p_j}
\quad\Longleftrightarrow\quad
v_i=1\pmod {R_j}
\quad\Longleftrightarrow\quad
h_{j,i}=1.
\tag{4}
\]

Thus every \(H_i=\gcd(v_i-1,N)\) is a product of complete hidden
prime-power components. Its only types are one, a proper factor, or \(N\).
This remains exact for repeated prime factors and arbitrary hidden
prime-power exponents.

## 2. Complete support coverage forces a first global return

Every local order satisfies

\[
g_j<N<2^n.
\tag{5}
\]

Therefore, for every prime power \(\ell^a\parallel g_j\), one has

\[
a<n.
\tag{6}
\]

By the support-cover hypothesis, choose one index \(i\) with
\(\ell\mid A_i\). Then

\[
v_\ell(A_i^n)\ge n>a.
\tag{7}
\]

Consequently the cumulative exponent

\[
E_B=\prod_{i=1}^B A_i^n
\tag{8}
\]

is divisible by every \(g_j\). Equation (2) gives \(h_{j,B}=1\) for all
\(j\), so

\[
H_B=N.
\tag{9}
\]

If no proper gcd appeared earlier, there is therefore a first index \(i\)
with \(H_i=N\). Minimality gives

\[
H_{i-1}=1,
\tag{10}
\]

where \(v_0=w\) handles \(i=1\). Thus every current order
\(h_{j,i-1}\) is nontrivial and \(T\)-rough.

By construction,

\[
v_i=v_{i-1}^{A_i^n}=1\pmod {R_j}
\tag{11}
\]

for every \(j\). Therefore

\[
h_{j,i-1}\mid A_i^n
\qquad(1\le j\le s).
\tag{12}
\]

This is the key one-child point. The current orders divide the power of the
single final entry \(A_i\). They need not divide any earlier individual
entry, and no earlier entry needs recursive factorization.

## 3. Recursive factorization and exact common-order stripping

Before using an entry, the procedure screens \(\gcd(A_i,N)\). A proper gcd
factors \(N\). On the no-factor branch, condition (4) in the statement gives

\[
1<A_i<2^{n-1}\le N,
\tag{13}
\]

so \(\gcd(A_i,N)=N\) is impossible. Hence the surviving entry is coprime to
\(N\), and so is \(A_i^n\).

Strong induction on input bit length completely factors the one integer
\(A_i\). Its bit length is at most \(n-1\). This gives the complete
factorization of

\[
M=A_i^n.
\tag{14}
\]

Equation (12) says that every current local order divides \(M\). For each
prime \(r\mid M\), repeatedly compute

\[
D_r=\gcd(v_{i-1}^{M/r}-1,N).
\tag{15}
\]

If \(D_r=N\), delete that copy of \(r\) from \(M\). If
\(1<D_r<N\), return the factor. If \(D_r=1\), retain the copy.

Assume no proper factor appears. At termination, every retained prime copy
is required by every local order: otherwise the corresponding local order
would divide \(M/r\), contradicting \(D_r=1\). Every deleted copy was
unnecessary for all local orders. Thus all current local orders equal the
same final value

\[
h_{j,i-1}=m
\qquad(1\le j\le s),
\tag{16}
\]

whose complete factorization is known. Equation (10) makes \(m>1\), and
the inherited roughness gives

\[
m>T.
\tag{17}
\]

This proves the output trichotomy of the general theorem.

## 4. One-child QP recursion

Every modular exponent \(A_i^n\) has bit length

\[
O(n\,\operatorname{bitlen}(A_i))=O(n^2).
\tag{18}
\]

The list length, list construction, modular powers, gcd screens, and final
stripping work are numerical QP by hypothesis. Entries before the first
global return are not recursively factored. Exactly one recursive call is
made, and its input has at most \(n-1\) bits.

Let \(Q(n)\) be a nondecreasing numerical-QP envelope for all nonrecursive
work. If the enclosing complete procedure makes no other recursive calls,

\[
\mathcal T(n)\le\mathcal T(n-1)+Q(n).
\tag{19}
\]

Summing the recurrence gives

\[
\mathcal T(n)
\le \mathcal T(n_0)+\sum_{r=n_0+1}^n Q(r)
\le \mathcal T(n_0)+nQ(n),
\tag{20}
\]

which is numerical QP. No fixed ratio is needed for this unique chain.
This argument does not apply if a parent can retain several recursive
children without another QP recursion-tree bound.

## 5. Verification of the cross-resultant corollary

Assume both separated F185 menu filters are globally extinct on the same
original unit \(w\). Fix \(\ell^a\parallel g_j\). Extinction in the first
menu gives \(\delta\in\mathcal A\) and \(0\le k\le K\) such that

\[
F_{\delta,k}(N)=0\pmod\ell.
\tag{21}
\]

Extinction in the second gives \(\epsilon\in\mathcal B\) and
\(0\le l\le K\) such that

\[
F_{\epsilon,l}(N)=0\pmod\ell.
\tag{22}
\]

The two monic polynomials therefore have a common root modulo \(\ell\), so

\[
\ell\mid
\operatorname{Res}_X(F_{\delta,k},F_{\epsilon,l}).
\tag{23}
\]

Thus the cross-resultant list covers every prime in every local order.

The menu separation gives \(3\le\epsilon-\delta\le2L+1\). The same
unit-circle argument as P162 shows that every cross-resultant is nonzero and

\[
0<R_{\delta,\epsilon;k,l}
<2^{K(1+K\lambda)}.
\tag{24}
\]

Under condition (12) of the statement, its bit length is at most \(n-1\).
There are \(L^2(K+1)^2\) entries, a numerical-QP list. The general theorem
therefore applies.

If the first menu instead returns a gcd of one, or the first is extinct and
the second returns a gcd of one, the corresponding P162 rough descendant is
unchanged. Hence F186 changes only the recursive implementation of double
extinction. The wide-shift-hard branch remains open.
