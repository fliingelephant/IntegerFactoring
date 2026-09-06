# Proof of F176 V3

## 1. Factor-first stripping for arbitrary odd composites

Let \(d\) be a unit modulo an odd composite \(N\). Suppose \(E\), with
known complete factorization, satisfies

\[
d^E=1\pmod N.
\tag{1}
\]

For each prime \(\ell\mid E\), repeatedly compute

\[
\gcd(d^{E/\ell}-1,N).
\tag{2}
\]

If (2) is \(N\), replace \(E\) by \(E/\ell\). If it is proper, return the
factor. If it is one, retain the \(\ell\)-primary part.

On a no-factor branch, let \(m\) be the final exponent and let
\(m_j=\operatorname{ord}_{R_j}(d)\). Every \(m_j\mid m\). For every
\(\ell\mid m\), the final gcd-one result proves

\[
m_j\nmid m/\ell
\qquad(1\le j\le s).
\]

Thus \(v_\ell(m_j)=v_\ell(m)\) for every prime dividing \(m\), and

\[
m_j=m
\qquad(1\le j\le s).
\tag{3}
\]

If \(\gcd(m,N)>1\), it is proper because \(m\le\varphi(R_j)<N\).
Otherwise \((d,m)\) is a factored exact common-order state. The argument
also detects partial congruences inside repeated prime-power components.

## 2. Absolute classification at a QP cap

For every positive integer \(r\),

\[
r\mid\Lambda_B
\quad\Longleftrightarrow\quad
\sigma(r)\le B.
\tag{4}
\]

Let \(r_j=\operatorname{ord}_{R_j}(2)\). A proper value of \(A\) factors
\(N\). If \(A=N\), every \(r_j\mid\Lambda_B\), so Section 1 returns a
factor or their common exact value \(m\). If \(A=1\), no \(r_j\) divides
\(\Lambda_B\), and (4) gives

\[
\sigma(r_j)>B
\qquad(1\le j\le s).
\tag{5}
\]

## 3. Classification of every common return

Suppose Section 1 returns one common exact order \(m\).

If \(m>n\), this is Outcome B. No comparison with \(B\) is needed. In
particular, \(n<m\le B\) is progress, not a hard branch.

Suppose \(m\le n\). Then \(N\mid2^m-1\). Because

\[
n=\lceil\log_2(N+1)\rceil
\]

and \(N\) is odd,

\[
N>2^{n-1}.
\tag{6}
\]

The inequality rules out \(m<n\), so \(m=n\). Now

\[
N\mid2^n-1,
\qquad
2^n-1<2N,
\]

and therefore

\[
N=2^n-1.
\tag{7}
\]

If \(n\) is composite and \(\ell\mid n\) is prime, the integer
\(2^{n/\ell}-1\) is a proper divisor of \(N\).

If \(n\) is prime, composite \(N\) excludes \(n=2\), so \(n\) is odd. In
every hidden component, \(2\) has order \(n\), while \(-1\) has order two.
Their commuting product \(-2\) has exact order \(2n\). The factorization
of \(2n\) is known. Fermat's theorem gives

\[
N=2^n-1\equiv1\pmod n,
\]

so \(\gcd(2n,N)=1\). This proves Outcome B.

## 4. Relative classification

Assume \(A=1\). In every odd prime-power unit group, the kernel of the
squaring map is

\[
H_j=\langle-1\rangle=\{1,-1\}.
\]

For \(e_j\) in (14) of the statement,

\[
2^{2e}=1\pmod{R_j}
\quad\Longleftrightarrow\quad
e_j\mid e.
\tag{8}
\]

A proper \(G_e\) factors \(N\). At a first global return, (8) and
minimality give \(e_j=e\) for every \(j\).

The completely factored integer \(2e\) is a common annihilating multiple
for \(2\). Section 1 returns a factor or one common exact local order \(m\).
Local cyclicity gives

\[
e=\frac{m}{\gcd(m,2)},
\qquad
\operatorname{lcm}(2,m)=2e.
\tag{9}
\]

If \(m\) is even, \(2\) has order \(2e\). If \(m\) is odd, \(-2\) has
order \(2e\). Equation (5) gives \(m>B\), hence \(2e>n\).

If every scanned gcd is one, (8) gives \(e_j>C\) for every component.
Together with (5), this is Outcome C.

## 5. QP cost and recursion

A sieve through the numerical bound \(B\) constructs

\[
\Lambda_B=\prod_{\ell\le B}
\ell^{\lfloor\log_\ell B\rfloor}.
\]

The loose estimate

\[
\log_2\Lambda_B\le\log_2(B!)=O(B\log B)
\]

shows that its encoding and every absolute stripping exponent have QP bit
length. The sieve, modular powers, and gcds have QP cost.

The relative scan has \(C\) iterations. Factoring a returned \(e\le C\)
by trial division costs at most \(\sqrt C\) iterations, still QP. The
Mersenne branch and state construction are polynomial in \(n\).

A full binary factor tree has fewer than \(2n\) nodes because its prime
leaves, counted with multiplicity, number at most
\(\lfloor\log_2N\rfloor\). Thus complete-factor recursion adds only a
polynomial factor to the uniform per-node QP cost.
