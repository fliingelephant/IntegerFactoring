# Proof of F174 V2

## 1. Every HH accumulated state is common locally

We first strengthen the loop invariant stated in Harvey--Hittmeir Algorithm
3.1. The published invariant says that \(M\) is the exact global order of
the accumulated element \(g\), and that the complete factorization of
\(M\) is stored.

Suppose the algorithm computes the exact global order \(m\) of one loop
element \(\gamma\). For every prime \(\ell\mid m\), it tests

\[
\gcd(\gamma^{m/\ell}-1,N).
\tag{1}
\]

Because \(m\) is the exact global order, this gcd cannot be \(N\). On a
no-factor branch it is therefore one. Let \(p\mid N\) be rational prime. If
\(m_p=\operatorname{ord}_p(\gamma)\), then \(m_p\mid m\). The gcd-one
condition for every \(\ell\mid m\) says

\[
m_p\nmid m/\ell
\qquad(\ell\mid m).
\]

This forces

\[
v_\ell(m_p)=v_\ell(m)
\qquad(\ell\mid m),
\]

and hence \(m_p=m\). In particular, \(m\mid p-1\).

Now let \(R=p^a\parallel N\). The local order modulo \(R\) is a multiple of
the order modulo \(p\), and it divides the exact global order \(m\). Thus

\[
\operatorname{ord}_R(\gamma)=m.
\tag{2}
\]

The Harvey--Hittmeir lcm construction selects the largest primary-order
part from the old accumulated element or from \(\gamma\), and multiplies
parts of coprime order. Since both input orders are exact in every hidden
component, the constructed element has exact order

\[
\operatorname{lcm}(M,m)
\]

in every component too. Induction from \((g,M)=(1,1)\) proves (6) of the
statement.

Also, \(M\mid p-1\) for every rational prime \(p\mid N\). Hence no prime
dividing \(N\) divides \(M\), which proves \(\gcd(M,N)=1\). The published
line-19 test gives \(M\le D\) until it returns.

## 2. Every HH exit except line 13 is already resolved

Because \(D\ge n\),

\[
2^D\ge2^n>N.
\]

Thus the early line-4 return of the element two is unreachable. The finite
small-input branch is handled by preprocessing. The even branch is outside
the odd input promise.

If a loop integer \(\beta\) divides \(N\), it is a proper factor in the
published parameter range. A non-one prime-divisor gcd after an exact order
search is proper because it cannot equal \(N\). If line 19 returns, Section
1 shows that its \((g,M)\) is a factored exact common-order state with
\(M>D\).

If the main loop finishes, the Harvey--Hittmeir correctness proof shows that
every prime divisor \(p\mid N\) satisfies

\[
p\equiv1\pmod M
\]

and lies below its public bound \(Z\). The final scan of \(kM+1\) therefore
finds the least prime divisor of composite \(N\).

Only line 13 needs a new classification.

## 3. Structure immediately before line 13

Let \(\beta\) be the loop integer at which line 13 would return. On entry to
that iteration,

\[
\beta^M\ne1\pmod N,
\qquad
M\le D,
\tag{3}
\]

and the order search certifies

\[
\operatorname{ord}_N(\beta)>D.
\tag{4}
\]

For every positive integer \(a<\beta\), consider its earlier loop
iteration. Either \(a^{M_a}=1\pmod N\) for the state then current, or its
exact order was computed and merged into the state. Every later state order
is a multiple of every earlier state order. Therefore the current \(M\)
satisfies

\[
a^M=1\pmod N
\qquad(1\le a<\beta).
\tag{5}
\]

Every such \(a\) is a unit. Otherwise one of its prime divisors, which is
smaller than \(\beta\), would already have divided \(N\) and terminated the
algorithm.

If \(\beta=uv\) were composite with \(1<u,v<\beta\), then (5) would give

\[
\beta^M=(uv)^M=u^Mv^M=1\pmod N,
\]

contrary to (3). Thus \(\beta\) is prime.

Fix a hidden odd prime power \(R_j=p_j^{a_j}\). Its unit group is cyclic.
Since \(M\mid p_j-1\), the kernel of the \(M\)-th-power map has exactly
\(M\) elements and is the unique subgroup of order \(M\). The state element
\(g\) generates this subgroup. Equation (5) therefore gives

\[
a\bmod R_j\in H_j=\langle g\bmod R_j\rangle
\qquad(1\le a<\beta).
\tag{6}
\]

This proves the prime and local-prefix claims. Equation (3) says only that
\(\beta\) is outside at least one \(H_j\). On the later hard branch,
(15) holds in every component, so \(\beta\) is then outside every \(H_j\).

## 4. The truncated smooth-prefix factor scan

Put

\[
y=\beta-1.
\]

No rational prime divisor \(p\mid N\) is at most \(y\), because its loop
iteration would already have factored \(N\). Every positive \(y\)-smooth
integer \(a\le p\) is therefore a unit and is a product of integers at most
\(y\). Equation (5) gives

\[
a^M=1\pmod p.
\]

Distinct integers in \([1,p-1]\) give distinct residues. The polynomial
\(X^M-1\) has at most \(M\) roots over \(\mathbf F_p\). Hence

\[
\boxed{\Psi(p,y)\le M.}
\tag{7}
\]

Assume now that \(y\ge Y_D=H_D^2\). By the definitions in (8)--(9) of the
statement and \(X_D=2^{H_D}\),

\[
\log y\ge2\log H_D
>2\log\log X_D.
\tag{8}
\]

Also \(X_D\ge y\) for all sufficiently large \(D\), because
\(y\le\lceil D^{1/3}\rceil\) while

\[
\log_2X_D=H_D\ge8\log_2(2D).
\]

The smooth-number bound used by Harvey--Hittmeir gives

\[
\Psi(X_D,y)
\ge
\frac{X_D}{(\log X_D)^{\log X_D/\log y}}.
\tag{9}
\]

Taking logarithms and using (8),

\[
\begin{aligned}
\log \Psi(X_D,y)
&\ge
\log X_D\left(
1-\frac{\log\log X_D}{\log y}
\right)\\
&\ge\frac12H_D\log2\\
&=4L_DJ_D\log2\\
&\ge4\log(2D)\\
&>\log D\\
&\ge\log M
\end{aligned}
\tag{10}
\]

after one absolute finite threshold. Thus

\[
\Psi(X_D,y)>M.
\tag{11}
\]

If \(p>X_D\), monotonicity would give

\[
\Psi(p,y)\ge\Psi(X_D,y)>M,
\]

contrary to (7). Therefore every rational prime divisor of \(N\) satisfies

\[
p\le X_D.
\tag{12}
\]

Section 1 gives \(p\equiv1\pmod M\). Scanning every
\(kM+1\le X_D\) and testing divisibility therefore finds a proper prime
factor of composite \(N\).

Finally,

\[
\log_2X_D=H_D=O(\log D\log\log D).
\]

If \(D=2^{(\log n)^{O(1)}}\), then \(X_D\) is also QP in \(n\). The scan
has at most \(X_D\) candidates, each with QP bit length. This proves the
factor claim under (12) of the statement. On the no-factor branch,

\[
\beta\le Y_D=O((\log D\log\log D)^2)
=(\log n)^{O(1)}.
\tag{13}
\]

## 5. Absolute factor-first classification

The complete factorization of

\[
\Lambda_D=\operatorname{lcm}(1,ldots,D)
\]

is obtained by a sieve through \(D\). For a positive integer \(r\),

\[
r\mid\Lambda_D
\quad\Longleftrightarrow\quad
\sigma(r)\le D.
\tag{14}
\]

Let

\[
r_j=\operatorname{ord}_{R_j}(\beta).
\]

If the gcd \(A_\beta\) in (18) of the statement is proper, it factors
\(N\). If it is one, no \(r_j\) divides \(\Lambda_D\). Equation (14) gives

\[
\sigma(r_j)>D
\qquad(1\le j\le s).
\tag{15}
\]

Suppose instead that \(A_\beta=N\). Then the exact global order \(m\) of
\(\beta\) divides the known factored multiple \(\Lambda_D\). Repeatedly
strip a prime \(\ell\) whenever

\[
\beta^{m/\ell}=1\pmod N.
\]

This computes \(m=\operatorname{ord}_N(\beta)\) and its complete
factorization. The line-13 certificate (4) gives \(m>D\).

For every prime \(\ell\mid m\), compute

\[
\gcd(\beta^{m/\ell}-1,N).
\tag{16}
\]

A non-one value is proper. If all values are one, the argument of Section 1
gives

\[
\operatorname{ord}_{R_j}(\beta)=m
\qquad(1\le j\le s).
\]

It also gives \(\gcd(m,N)=1\). Therefore \((\beta,m)\) is a factored exact
common-order state above \(D\).

## 6. Relative factor-first classification

Only the absolute-gcd-one branch remains. Put

\[
e_j=\operatorname{ord}_{(\mathbb Z/R_j\mathbb Z)^\times/H_j}
(\beta H_j).
\]

For a positive integer \(e\),

\[
\beta^{eM}=1\pmod{R_j}
\quad\Longleftrightarrow\quad
e_j\mid e.
\tag{17}
\]

Scan \(e=1,\ldots,C\) in order. If the first non-one gcd \(G_e\) is
proper, it factors \(N\). If it is \(N\), then (17) and minimality give

\[
e_j=e
\qquad(1\le j\le s).
\tag{18}
\]

The complete factorization of \(eM\) is obtained by trial division of
\(e\) and merging it with the known factorization of \(M\). P150 divisor
stripping and its prime-divisor screens now either factor \(N\), or compute
the exact global order \(m\) of \(\beta\) and certify it in every hidden
component. Local cyclicity then gives

\[
\operatorname{lcm}(M,m)=Me.
\tag{19}
\]

The P150 prime-primary lcm word has exact order \(L=Me\) in every hidden
component. Since (4) says \(m>D\),

\[
L=\operatorname{lcm}(M,m)\ge m>D.
\tag{20}
\]

Also \(e\ne1\), because \(e=1\) would give \(\beta^M=1\pmod N\), contrary
to (3).

If every scanned gcd is one, (17) gives \(e_j>C\) for every \(j\). The
fingerprint \(\beta^M\) has order \(e_j\) in component \(j\), so its first
\(C+1\) powers are distinct in every component. The P154 capacity bound is

\[
|\langle g,\beta\rangle_{R_j}|
=M e_j
\ge M(C+1).
\tag{21}
\]

This proves every outcome in the trichotomy.

## 7. QP complexity and the F172 corollary

The HH call has its stated cost. The bit length of \(\Lambda_D\) is at most

\[
\log_2(D!)=O(D\log D),
\]

so its construction, factorization, modular powers, and divisor stripping
are QP. The relative scan contributes \(C\) modular powers and gcds. Section
4 proves that the smooth-prefix trial scan has QP length. The prime-primary
state words use at most the number of prime divisors in their supplied
factored orders and have QP provenance length. Thus the full deterministic
procedure is QP.

On the F172 family, an exact common ordinary order divides six. If \(D>6\),
the exact-state outcome \(L>D\) cannot occur without a prior factor. The
remaining no-factor outcome is therefore the algorithm-selected hard prime
block. This proves the stated corollary and no stronger factor claim.

