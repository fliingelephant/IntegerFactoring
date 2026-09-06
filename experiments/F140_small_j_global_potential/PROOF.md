# F140 proof — polynomial-depth public small-quotient paths

## 1. The block and carry recurrence

For fixed \(t\), let

\[
D_t=(t+3)\operatorname{rad}\!\left(
\prod_{i=0}^{t}(i+2)
\prod_{d=1}^{t}(2^d-1)
\right).
\]

It is harmless to multiply this integer by two if necessary.  Thus take it
even.  It satisfies \(D_t>t+2\), and

\[
\log D_t
\le O(\log t)
+\sum_{i=0}^{t}\log(i+2)
+\sum_{d=1}^{t}d\log2
=O(t^2).
\]

Put

\[
k_i=i+2,
\qquad
q_i=2^iD_t+1.
\]

Every prime divisor of \(k_i\) divides \(D_t\), so

\[
\gcd(k_i,q_i)=1.
\]

If \(i<j\), then

\[
2^{j-i}q_i-q_j=2^{j-i}-1.
\]

Any prime common to \(q_i,q_j\) would therefore divide \(2^{j-i}-1\), hence
would divide \(D_t\).  But every \(q_i\) is one modulo every prime divisor of
\(D_t\).  This is impossible.  Hence the \(q_i\) are pairwise coprime.

Define

\[
K_i=k_i+2q_i.
\]

Because \(q_{i+1}=2q_i-1\) and \(k_{i+1}=k_i+1\),

\[
K_i=q_{i+1}+k_{i+1}.
\tag{1}
\]

Also \(0<k_i<q_i\), and the \(K_i\) are strictly increasing.  Since
\(D_t>t+2\), every \(K_i\) is larger than every \(k_j\).  Therefore all
members of

\[
\mathcal C_t=\{k_0,\ldots,k_t,K_0,\ldots,K_{t-1}\}
\]

are distinct.

## 2. Polynomial-size private public labels

Let \(E_t\) be the product of all \(q_i\), all nonzero pairwise differences
of members of \(\mathcal C_t\), and 2.  Its number of distinct prime divisors
is at most \(\log_2 E_t\).

We have

\[
\sum_i\log q_i=O(t^3).
\]

There are \(O(t^2)\) carry differences, and each has \(O(t^2)\) bits.
Consequently

\[
\omega(E_t)=O(t^4).
\]

Exclude these prime divisors and all primes at most \(t+2\).  The standard
bound for the \(m\)-th prime then supplies \(2t+1\) distinct remaining primes
of size \(O(t^4\log t)\).  Assign \(t+1\) of them as
\(\sigma_0,\ldots,\sigma_t\), and assign the other \(t\) as
\(\lambda_0,\ldots,\lambda_{t-1}\).

Thus every label prime is coprime to every \(q_i\), exceeds the carry of its
base seed when applicable, and divides no nonzero difference between two
selected carries.

## 3. The CRT class and valuation-one rows

All moduli

\[
q_i,
\quad
\sigma_i^2,
\quad
\lambda_i^2
\]

are pairwise coprime.  For each \(q_i\), impose

\[
N\equiv-k_i^{-1}\pmod{q_i}.
\tag{2}
\]

For each \(\sigma_i\), let \(a_i\) solve

\[
k_ia_i\equiv-1\pmod{\sigma_i^2}
\]

and impose

\[
N\equiv a_i+\sigma_i\pmod{\sigma_i^2}.
\tag{3}
\]

Then

\[
1+k_iN\equiv k_i\sigma_i\not\equiv0
\pmod{\sigma_i^2},
\]

so \(v_{\sigma_i}(1+k_iN)=1\).

Similarly, for each \(\lambda_i\), choose \(b_i\) with

\[
K_ib_i\equiv-1\pmod{\lambda_i^2}
\]

and impose

\[
N\equiv b_i+\lambda_i\pmod{\lambda_i^2}.
\tag{4}
\]

Then \(v_{\lambda_i}(1+K_iN)=1\).  The Chinese remainder theorem gives a
unit class \(N_0\bmod R\), where

\[
R=
\left(\prod_iq_i\right)
\left(\prod_i\sigma_i^2\right)
\left(\prod_i\lambda_i^2\right).
\]

## 4. A quantitatively small semiprime in the class

We use only the standard Linnik theorem: the least prime in any reduced
residue class modulo \(m\) is at most \(O(m^L)\) for an absolute constant
\(L\).

First choose a prime

\[
P\equiv1\pmod R.
\]

Its least positive residue is 1, so \(P>R\), and Linnik gives
\(P\le R^{O(1)}\).

Take the representative \(1\le N_0<R\).  If \(N_0>1\), put

\[
b=N_0(1+R);
\]

and if \(N_0=1\), put \(b=(1+R)^2\).  In either case, \(b\) is composite,
\(b\equiv N_0\pmod R\), and \(\gcd(b,R)=1\).  By Bertrand's theorem choose a
prime

\[
h>\max(P,b)
\]

with \(h\le2\max(P,b)\).  The residue \(b\) is reduced modulo \(Rh\), is
composite, and lies below \(Rh\).  Linnik now gives a prime

\[
Q\equiv b\pmod{Rh}.
\]

Thus \(Q>Rh>P\), while \(Q\le R^{O(1)}\).  Put \(N=PQ\).  Then \(N\) is an
odd distinct semiprime,

\[
N\equiv N_0\pmod R,
\qquad
\log N=O(\log R)=O(t^3).
\tag{5}

\]

For all sufficiently large \(t\), the product structure of \(R\) gives

\[
R>(C_tq_t)^4,
\qquad
C_t=\max_i(\sigma_i,\lambda_i).
\tag{6}

Indeed,

\[
\sum_{i=0}^{t}\log q_i
\ge
(t+1)\log D_t+\frac{t(t+1)}2\log2,
\]

whereas

\[
4\log(C_tq_t)
\le
4\log D_t+4t\log2+O(\log t).
\]

Their difference tends to infinity.  Small \(t\) can be absorbed into the
absolute threshold.

## 5. Canonical sources and public release

Define

\[
B_i=1+k_iN,
\qquad
V_i=1+K_iN.
\]

Equation (2) gives \(q_i\mid B_i\).  Since \(k_i<q_i\),

\[
w_i=B_i/q_i
\]

is the least positive inverse of \(q_i\).

Equation (3) says that the public seed \(\sigma_i\) gives the canonical pair

\[
\left(\sigma_i,B_i/\sigma_i\right),
\]

because \(k_i<\sigma_i\).

At state \(q_i\), use anchor \(\lambda_i\) and digit 2.  Since

\[
w_i+2N=V_i/q_i
\]

and (4) makes \(\lambda_i\mid V_i\), coprimality gives
\(\lambda_i\mid w_i+2N\).  The digit is valid because \(2<\lambda_i\).  The
canonical endpoints are

\[
\left(\lambda_iq_i,V_i/(\lambda_iq_i)\right).
\]

They lie below \(N\) once \(N>C_tq_t\).  The right endpoint contains
\(q_{i+1}\), because (1)--(2) give \(q_{i+1}\mid V_i\), and
\(q_{i+1}\) is coprime to \(q_i\lambda_i\).

Both exact integers \(V_i\) and \(B_{i+1}\) are public products of retained
endpoints.  Using (1),

\[
\begin{aligned}
\gcd(V_i,B_{i+1})
&=\gcd(1+K_iN,1+k_{i+1}N)\\
&=\gcd(B_{i+1},(K_i-k_{i+1})N)\\
&=\gcd(B_{i+1},q_{i+1})\\
&=q_{i+1}.
\end{aligned}
\tag{7}

Thus exact gcd-free refinement publicly names the next unit block.  In the
P124 division,

\[
K_i=1\cdot q_{i+1}+k_{i+1},
\]

so every quotient is exactly one.  The next selected digit is two, genuinely
different from the virtual parent digit one.

## 6. Deduplication, endpoint screens, and rank

The carries in \(\mathcal C_t\) are distinct, so all \(B_i,V_i\) are
distinct exact values.  Duplicate presentations \((q_i,w_i)\) of \(B_i\)
are still screened before exact-value deduplication.

Consider any canonical pair \((c,z)\) on the selected path or any duplicate
anchor presentation on its active blocks with anchor at most \(C_t\).  Then

\[
c\le C_tq_t.
\]

If a prime factor \(p\in\{P,Q\}\) divided \(c-z\) or \(c+z\), the relation
\(cz\equiv1\pmod p\) would imply \(c^2\equiv1\pmod p\) or
\(c^2\equiv-1\pmod p\).  Hence \(p\mid c^4-1\).  But (6) and \(P,Q>R\)
give \(p>c^4-1\).  This is impossible.  Every such endpoint screen is null.

Finally, \(\sigma_i\) occurs to odd valuation in \(B_i\).  If it divided any
other selected exact value with carry \(x\), subtraction would give

\[
\sigma_i\mid x-k_i,
\]

contrary to its selection.  Thus row \(\sigma_i\) is private to column
\(B_i\).  The identical argument makes row \(\lambda_i\) private to column
\(V_i\).  These rows form an identity submatrix, so the selected columns
have full binary rank.  There is no dependency and therefore no normalized
root to test.

## 7. Size and scope

We have \(\log R=O(t^3)\), so (5) gives \(n=O(t^3)\), or

\[
t=\Omega(n^{1/3}).
\]

Also \(n=\Omega(t^2)\), while \(C_t=O(t^4\log t)\).  Therefore
\(C_t<n^3\) for large \(t\).  The much faster growth of \(N\) than \(q_t\)
also gives \(q_i<N/n^3\).  Hence the displayed sources are available under
the operational cap \(n^3\), and the selected transcript has polynomial
work.

This proves only a selected-path obstruction from an already named \(q_0\).
It does not describe the complete source, rule out progress elsewhere, or
exclude a polynomial global potential.
