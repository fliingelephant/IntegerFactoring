# Proof of F176 V2

## 1. Factor-first order stripping lemma

Let \(d\) be a unit modulo an odd composite \(N\), and suppose a positive
integer \(E\), with known complete factorization, satisfies

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

On a no-factor branch, let \(m\) be the final exponent. Every local order
\(m_j=\operatorname{ord}_{R_j}(d)\) divides \(m\). For every
\(\ell\mid m\), the final gcd-one result says

\[
m_j\nmid m/\ell
\qquad(1\le j\le s).
\]

Therefore \(v_\ell(m_j)=v_\ell(m)\) for every \(\ell\mid m\), and

\[
m_j=m
\qquad(1\le j\le s).
\tag{3}
\]

If \(\gcd(m,N)>1\), it is a proper factor because
\(m\le\varphi(R_j)<N\). Otherwise \((d,m)\) is a certified exact
common-order state. This argument includes repeated odd prime powers.

## 2. Absolute classification

For a positive integer \(r\),

\[
r\mid\Lambda_n
\quad\Longleftrightarrow\quad
\sigma(r)\le n.
\tag{4}
\]

Let \(r_j=\operatorname{ord}_{R_j}(2)\). If the gcd \(A\) in (7) of the
statement is proper, it factors \(N\).

If \(A=N\), every \(r_j\) divides the factored exponent \(\Lambda_n\).
The lemma returns a factor or their common exact value \(m\).

If \(A=1\), no \(r_j\) divides \(\Lambda_n\). Equation (4) gives

\[
\sigma(r_j)>n
\qquad(1\le j\le s).
\tag{5}
\]

This proves the absolute trichotomy.

## 3. A small common order forces an exact Mersenne input

Suppose the no-factor branch of the lemma gives

\[
r_j=m\le n
\qquad(1\le j\le s).
\]

Then \(N\mid2^m-1\). Since

\[
n=\lceil\log_2(N+1)\rceil
\]

and \(N\) is odd,

\[
N>2^{n-1}.
\tag{6}
\]

If \(m<n\), then \(2^m-1<N\), a contradiction. Hence \(m=n\). Also

\[
N\mid2^n-1,
\qquad
2^n-1<2N.
\]

The positive quotient is therefore one:

\[
N=2^n-1.
\tag{7}
\]

If \(n\) is composite and \(\ell\mid n\) is prime, then

\[
1<2^{n/\ell}-1<2^n-1=N
\]

and \(2^{n/\ell}-1\mid N\). This is a proper factor.

Suppose \(n\) is prime. Since \(N\) is composite, \(n\ne2\), so \(n\) is
odd. In every hidden component, \(2\) has order \(n\). Therefore
\[
\operatorname{ord}_{R_j}(-2)=2n.
\tag{8}
\]

Indeed, \(\langle2\rangle\) has odd order, while \(-1\) has order two, so
their intersection is trivial. The order factorization \(2\cdot n\) is
known. Also \(N\) is odd and Fermat's theorem gives

\[
N=2^n-1\equiv1\pmod n,
\]

so \(\gcd(2n,N)=1\). Thus \((-2,2n)\) is the required exact common state.

This proves that every common base-two return gives a factor or a state
above \(n\).

## 4. Relative classification against the sign subgroup

Assume \(A=1\). In every odd prime-power unit group, the kernel of the
squaring map is exactly

\[
H_j=\langle-1\rangle=\{1,-1\}.
\]

For \(e_j\) defined in (14) of the statement,

\[
2^{2e}=1\pmod{R_j}
\quad\Longleftrightarrow\quad
e_j\mid e.
\tag{9}
\]

Scan \(e=1,\ldots,C\). A proper gcd factors \(N\). If the first non-one gcd
is \(N\), (9) and minimality give

\[
e_j=e
\qquad(1\le j\le s).
\tag{10}
\]

The integer \(2e\) is a known annihilating multiple for the absolute order
of \(2\). Factor it by trial division and apply the lemma. On a no-factor
branch, \(2\) has one exact common local order \(m\).

Local cyclicity gives

\[
\operatorname{lcm}(2,m)=2e.
\tag{11}
\]

More explicitly, if \(m\) is even then \(e=m/2\) and \(2\) itself has
order \(2e\). If \(m\) is odd then \(e=m\) and \(-2\) has order \(2e\).
The absolute hard certificate (5) gives \(m>n\), so the state order is
above \(n\).

If every scanned gcd is one, (9) gives \(e_j>C\) for every component.
Together with (5), this is exactly Outcome C.

## 5. QP cost and recursion

The sieve through \(n\), construction and factorization of \(\Lambda_n\),
and its divisor stripping have polynomial bit cost. The relative scan has
\(C\) iterations. Factoring an integer \(e\le C\) by trial division takes
at most \(\sqrt C\) iterations. Modular exponents and all produced integers
have QP bit length. Hence every branch has deterministic QP cost.

A full binary factor tree for \(N\) has fewer than \(2n\) nodes because its
prime leaves, counted with multiplicity, number at most
\(\lfloor\log_2N\rfloor\). Thus complete-factor recursion adds only a
polynomial factor to the per-node QP bound.
