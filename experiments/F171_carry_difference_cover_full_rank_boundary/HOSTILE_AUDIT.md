# Hostile audit of the F171 candidate

## Verdict

**PASS.** I found no mathematical defect in the frozen statement or proof.
The result has the stated selected-source scope only. It does not extend to a
complete static source, an adaptive source, balanced semiprimes, or every QP
cutoff.

Frozen inputs checked:

- `STATEMENT.md`:
  `22ee980dca180518170dde7d94df3a6a9225fffc880adf316738de6135e87b43`;
- `PROOF.md`:
  `ab9883b425c5957839a0d5a79bf235897360691854ab28b2a8d5ee030251c01c`;
- `SELF_AUDIT.md`:
  `bf8f5c6c6bfdc9b0e3c5e5e32d1bc6578909b3a04c8da576dc6a7c9b77cd7146`.

No computation was used.

## Kill attempts

### 1. Prime supply

For sufficiently large \(m\), the prime number theorem gives more than
\(m\) primes in

\[
(m,4m\log m).
\]

Thus the distinct odd primes \(g_1,\ldots,g_m\) exist. Their ordering does
not add a hidden constraint because every \(g_k>m\ge k\).

### 2. CRT compatibility and reducedness

The moduli \(g_k^2\) are pairwise coprime, and \(k\) is invertible modulo
each \(g_k^2\). The prescribed residue

\[
(g_k-1)k^{-1}\pmod {g_k^2}
\]

is \(-k^{-1}\ne0\pmod {g_k}\). Hence the CRT class \(Z\pmod Q\) is a unit
class. There is no compatibility or reducedness gap.

### 3. Semiprime construction and length

Bertrand supplies \(Q<p<2Q\), and \(p\) is a unit modulo \(Q\). The derived
class \(a=Zp^{-1}\pmod Q\) is also reduced. Since \(5\nmid Q\), at most one
of \(a+2Q,a+3Q,a+4Q\) is divisible by five. The selected
\(b\in(2Q,5Q)\) therefore satisfies \(\gcd(b,5Q)=1\).

Because \(b\) is the least positive representative of its class modulo
\(5Q\), every positive integer in that class is at least \(b\). Thus the
least prime \(\ell\equiv b\pmod {5Q}\) obeys

\[
2Q<b\le\ell.
\]

Linnik gives \(\ell\le C(5Q)^L\). Therefore \(p\ne\ell\),
\(N=p\ell\equiv Z\pmod Q\), and

\[
2Q^2<N<2C5^LQ^{L+1}.
\]

Together with

\[
2m\log m<\log Q=\Theta(m\log m),
\]

this proves \(n=\Theta(m\log m)\). No short-interval theorem and no balance
claim is used.

### 4. Canonical endpoints and sign screens

The CRT congruence gives \(g_k\mid1+kN\). Since \(k<g_k\),

\[
0<w_k=(1+kN)/g_k<N.
\]

Also \(g_k<N\), so \(w_k\) is exactly the least-positive inverse of \(g_k\)
modulo \(N\), and its carry is \(k\).

For either hidden prime \(s\in\{p,\ell\}\), a selected minus or plus screen
would imply \(g_k^2\equiv1\pmod s\) or
\(g_k^2\equiv-1\pmod s\). But, for large \(m\),

\[
0<g_k^2-1<g_k^2+1<Q<s.
\]

Thus every displayed selected sign gcd is one. This claim does not cover an
earlier presentation of the same exact value, and the statement does not say
that it does.

### 5. Exact valuation-one coverage, including \(r=2\)

For a prime \(r\le R\), let \(a=-N^{-1}\pmod r\) and
\(1+aN=rh\). The four carries \(k_j=a+jr\), \(0\le j\le3\), all lie in
\([1,m]\), and

\[
1+k_jN=r(h+jN).
\]

Exactly one residue class of \(j\pmod r\) makes the second factor divisible
by \(r\). For \(r=2\), the four indices contain each residue twice, so two
indices avoid the bad class. For \(r=3\), at least two avoid it. For
\(r\ge5\), at most one of the four indices is bad. Hence at least two
distinct selected columns have exact valuation \(v_r=1\). The proof does not
confuse divisibility with odd valuation.

### 6. Private endpoint-prime rows and rank

Modulo \(g_k^2\), the CRT prescription gives

\[
1+kN\equiv g_k,
\]

so \(v_{g_k}(P_k)=1\). For \(j\ne k\),

\[
1+jN\equiv(k-j)k^{-1}\not\equiv0\pmod {g_k},
\]

because \(0<|k-j|<m<g_k\). The \(g_k\)-rows are therefore an exact identity
submatrix. The selected parity matrix has column rank \(m\) and zero kernel.
Its restriction to rows at most \(R\) has at most \(\pi(R)\) rows, so its
nullity is at least \(m-\pi(R)\). There is no inference from restricted
nullity to full nullity.

### 7. Public endpoint bound and trial hardness

Since every \(g_i>m\),

\[
n>2\log_2Q>4m\log_2m>4m\log m>g_k
\]

for large \(m\), where the unlabelled logarithm is natural. Thus \(g_k<n\)
and the stated \(g_k\le n\) follows. Both hidden primes exceed
\(Q=2^{\Theta(n)}\), hence exceed \(n^2\) eventually. Their distinctness
also proves that \(N\) is not a perfect power.

### 8. Scope and QP claims

The frozen text repeatedly limits the identity-row conclusion to the
selected bank. It expressly allows omitted static or adaptive columns to
reuse the private rows or to factor \(N\). It makes no balanced-semiprime
claim. It notes only that this polynomial-size bank and cutoff fit inside the
QP budget; it does not claim an obstruction for every QP cutoff. I found no
scope leak.

## Corrections

No mathematical correction is required. One optional notation cleanup is to
replace the asymptotic inequality in Proof Section 7 by the explicit bounds

\[
\log N>2\log Q+\log2,
\qquad
\log N<(L+1)\log Q+\log(2C5^L),
\]

because an \(O(1)\) term inside a strict inequality is not literal. The
existing line is sufficient for its only use, the stated
\(\Theta(\log Q)\) conclusion.
