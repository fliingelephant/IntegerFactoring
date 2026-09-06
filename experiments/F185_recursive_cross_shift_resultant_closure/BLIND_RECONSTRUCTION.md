# Blind reconstruction of F185

## Evidence boundary and verdict

I verified the SHA-256 digest of `STATEMENT.md` before reading it:

```text
f4fca86df79a72d473cc3e8dd943140978d1422efb6b2f2af324bd94076a555b
```

I used no other file in the F185 directory.

**Verdict: VERIFIED.** All mathematical claims in the statement follow under
its stated strong-induction premise. The quasipolynomial conclusion is
conditional on the fixed contraction and on the stated bounds for every
other recursive call. The surviving descendant is explicitly not closed by
F185.

## 1. The admissible range for \(K\)

The contraction condition is

\[
\lambda K^2+K-m\le 0.
\]

Here \(\lambda>0\). The positive root of the corresponding quadratic is

\[
\kappa=\frac{\sqrt{1+4\lambda m}-1}{2\lambda}.
\]

The quadratic is increasing for \(K\ge0\). Therefore its positive integral
solutions are exactly

\[
1\le K\le \lfloor\kappa\rfloor.
\]

This proves (7). The range contains \(K=1\) exactly when

\[
1+\lambda\le m,
\]

which proves the claimed nonemptiness criterion.

For \(L\ge1\),

\[
\lambda=\left\lceil 1+\log_2(L+1)\right\rceil
       =\Theta(\log_2(L+1)).
\]

The numerical-QP bound on \(L\) gives

\[
\lambda=O((\log(n+1))^{d_L})=o(n).
\]

Also, \(m=\rho n+O(1)\). Hence \(m\ge1+\lambda\) for all sufficiently
large \(n\), and the positive root satisfies

\[
\kappa=\Theta\!\left(\sqrt{m/\lambda}\right)
       =\Theta\!\left(
          \sqrt{\frac{n}{\log_2(L+1)}}
        \right).
\]

Thus (8) is correct for the largest admissible \(K\). An arbitrary smaller
admissible choice need not have this asymptotic size.

## 2. Exact action of a menu filter

Fix a hidden component \(R_j\), write \(g=g_j\), and let

\[
E_{\mathcal S}=P_{\mathcal S}^{,n}.
\]

For any group element of order \(g\),

\[
\operatorname{ord}(w^{E_{\mathcal S}})
=\frac{g}{\gcd(g,E_{\mathcal S})}.
\tag{A}
\]

If \(\ell^a\parallel g\), then \(\ell^a\le g<R_j\le N\). Since
\(n=\lceil\log_2(N+1)\rceil\), this implies \(a<n\), and in particular
\(a\le n\). Consequently:

- if \(\ell\mid P_{\mathcal S}\), then
  \(v_\ell(E_{\mathcal S})=n v_\ell(P_{\mathcal S})\ge a\), so the full
  factor \(\ell^a\) is deleted from (A);
- if \(\ell\nmid P_{\mathcal S}\), then the full factor \(\ell^a\)
  remains.

For one shift \(\delta\), the prime \(\ell\) divides \(C_\delta\) exactly
when either

\[
\ell\mid N+\delta,
\]

or \(\ell\nmid N+\delta\) and

\[
(N+\delta)^k\equiv1\pmod\ell
\quad\text{for some }1\le k\le K.
\]

In the second case, the last condition is equivalent to

\[
\operatorname{ord}_\ell(N+\delta)\le K.
\]

The linear factor \(N+\delta\) handles the nonunit case before an order is
mentioned. Combining this observation over all shifts with (A) proves the
exact formula (12), including its nonunit convention.

Now let \(p_j\) be the prime below \(R_j\). If
\(H_{\mathcal S}=1\), then \(p_j\nmid z_{\mathcal S}-1\) for every \(j\).
Thus no local order is trivial. Formula (12) shows that every prime in each
new local order remains coprime to \(N\), remains larger than \(T\), and
satisfies both conditions in (21) for every menu shift. If the gcd is
strictly between \(1\) and \(N\), it is already a proper factor. If it is
\(N\), then \(z_{\mathcal S}=1\) in every \(R_j\). This proves the filter
trichotomy and justifies the stated order of the two filters.

This reasoning does not assume that \(R_j\) is prime. A partial
\(p_j\)-adic gcd is also a proper factor, which is sufficient.

## 3. Cross-resultants are nonzero and small

Fix \(\delta\in\mathcal A\), \(\epsilon\in\mathcal B\), and put

\[
d=\epsilon-\delta.
\]

The separated menus give the exact bounds

\[
3\le d\le2L+1<2L+2\le2^\lambda.
\tag{B}
\]

Use the coordinate \(Y=X+\delta\). The roots of \(F_{\delta,k}\) in this
coordinate are \(0\) when \(k=0\), and the \(k\)-th roots of unity when
\(k\ge1\). The roots of \(F_{\epsilon,l}\) are \(-d\) when \(l=0\), and
\(\eta-d\), with \(|\eta|=1\), when \(l\ge1\).

No root can occur in both sets. In the only potentially close case,
\(k,l\ge1\), a common root would give

\[
d=\eta-\zeta,
\]

whose right side has absolute value at most \(2\), contrary to \(d\ge3\).
The cases with a zero index are even more immediate. Both polynomials are
monic and have positive degree. Their resultant is therefore a nonzero
integer, so its absolute value is positive. This proves that a zero
resultant never occurs.

Set

\[
E=K(1+K\lambda).
\]

If \(k,l\ge1\), the root formula for a monic resultant gives

\[
R_{\delta,\epsilon;k,l}
\le\prod_{\zeta^k=1}
   \left|(\zeta+d)^l-1\right|.
\]

For each factor,

\[
\left|(\zeta+d)^l-1\right|
\le(d+1)^l+1
<2(d+1)^l
\le2^{1+l\lambda}.
\]

Hence

\[
R_{\delta,\epsilon;k,l}
<2^{k(1+l\lambda)}\le2^E.
\]

Since the resultant is a positive integer, this strict inequality implies
\(R+1\le2^E\), and hence \(\operatorname{bitlen}(R)\le E\).

The zero-index cases satisfy the same bound:

\[
\begin{array}{c|c}
(k,l)&R_{\delta,\epsilon;k,l}\\ \hline
(0,0)&d\\
(0,l),\ l\ge1&d^l-1\\
(k,0),\ k\ge1&\left|(-d)^k-1\right|.
\end{array}
\]

By (B), the first two have bit length at most \(\lambda\) and \(l\lambda\),
respectively. In the last case,

\[
R<2d^k<2^{1+k\lambda},
\]

so its bit length is at most \(1+k\lambda\). Each bound is at most \(E\)
for \(1\le k,l\le K\). This proves the first inequality in (16). Condition
(6) proves the second.

Finally, bit length is strictly increasing with a positive integer. Since

\[
\operatorname{bitlen}(R)\le\lfloor\rho n\rfloor<n
=\operatorname{bitlen}(N),
\]

we have \(R<N\). Therefore every resultant greater than one is a valid
recursive input with the promised fixed bit contraction.

## 4. Double extinction forces \(g_j\mid U^n\)

Assume

\[
H_{\mathcal A}=H_{\mathcal B}=N.
\]

Fix \(j\) and a prime power \(\ell^a\parallel g_j\). Formula (12), or
equivalently \(g_j\mid P_{\mathcal S}^n\), implies that \(\ell\) divides
at least one menu factor in each menu. Thus there are

\[
\delta\in\mathcal A,\quad 0\le k\le K,
\qquad
\epsilon\in\mathcal B,\quad 0\le l\le K
\]

such that

\[
F_{\delta,k}(N)\equiv0\pmod\ell,
\qquad
F_{\epsilon,l}(N)\equiv0\pmod\ell.
\]

The reductions of these two polynomials modulo \(\ell\) have the common
root \(N\bmod\ell\). Their resultant is therefore zero modulo \(\ell\).
It is nonzero over the integers by the separation argument above, so

\[
\ell\mid R_{\delta,\epsilon;k,l}\mid U.
\]

As proved in Section 2, \(a\le n\). It follows that

\[
\ell^a\mid U^n=M.
\]

This holds for every prime power in every \(g_j\), proving (18). It also
shows that \(U>1\) in the double-extinction branch.

Recursive factorization of every nonunit resultant gives a complete prime
factorization of \(U\), because the skipped resultants equal one. Raising
the recorded multiplicities by \(n\) gives the complete factorization of
\(M\).

## 5. Factor-first exact common-order extraction

Write the known factorization as

\[
M=\prod_r r^{e_r}.
\]

First compute \(\gcd(r,N)\) for every recorded prime \(r\). If one is
nontrivial, it is a proper factor of the composite \(N\). Assume this does
not happen.

Initialize \(Q=M\). For each prime \(r\mid Q\), repeatedly compute

\[
D=\gcd(w^{Q/r}-1,N).
\]

- If \(1<D<N\), return \(D\).
- If \(D=N\), replace \(Q\) by \(Q/r\) and repeat.
- If \(D=1\), keep the current power of \(r\) and continue with the next
  prime.

Only the \(D=N\) case removes a factor. Therefore every \(g_j\) continues
to divide \(Q\). Suppose the procedure returns no factor. For each prime
\(r\mid Q\), its final failed removal has \(D=1\). Hence
\(w^{Q/r}\ne1\pmod{R_j}\) for every \(j\), and thus

\[
g_j\nmid Q/r
\qquad\text{for every }j.
\]

Since \(g_j\mid Q\), this forces

\[
v_r(g_j)=v_r(Q)
\qquad\text{for every }j
\]

for every prime \(r\mid Q\). Consequently

\[
g_1=g_2=\cdots=g_s=Q=:q.
\]

The factorization of \(q\) is known because the algorithm only deletes
recorded prime factors from \(M\). Also \(q>1\), and every prime factor of
\(q=g_j\) exceeds \(T\). Therefore \(q>T\). This proves (19), including
the word “exact.”

The gcd step also covers nonsquarefree \(N\). If an exponentiation is one
modulo \(p_j\) but not modulo the full \(p_j^{e_j}\), the gcd exposes a
proper power of \(p_j\); it does not invalidate the procedure.

## 6. Exhaustive output classification

The first filter has three possible gcd outcomes. A proper gcd returns a
factor. A gcd of one returns \(z_{\mathcal A}\), with all properties in
(21). Only a gcd of \(N\) reaches the second filter. The second filter has
the same three outcomes. Its gcd-one case returns \(z_{\mathcal B}\).
Only double extinction reaches the resultant closure, where Section 5
returns either a factor or the fully factored common order.

Thus the execution returns exactly one of the three categories in (20).
“Exactly one” is an operational statement about these disjoint control-flow
outcomes. It does not assert that the abstract existence of one certificate
excludes every other certificate.

For either returned descendant, Section 2 proves all of the following:

\[
\operatorname{ord}_{R_j}(z_{\mathcal S})>1,
\qquad
\gcd(\operatorname{ord}_{R_j}(z_{\mathcal S}),N)=1,
\]

every prime in that order is larger than \(T\), and (21) holds for every
shift in the selected menu. Nothing in the construction contradicts the
possibility of this long-action branch. Therefore the explicit statement
that F185 does not close it is correct.

## 7. Complete recursive quasipolynomial accounting

There are exactly

\[
|\mathcal A||\mathcal B|(K+1)^2=L^2(K+1)^2=B(n)
\]

indexed resultants, and no more than this many recursive calls. Since
\(K\le n\) and \(L\) is numerical QP, \(B\) is numerical QP.

The nonrecursive work is also numerical QP. There are \(O(LK)\) filter
factors. Their total encoded exponent length is numerical QP. Modular
exponentiation is polynomial in \(n\) and that exponent length. Each
resultant has degree at most \(K\) in each input and has bit length at most
\(\rho n\); standard exact determinant or resultant algorithms therefore
take numerical-QP time over the complete menu. Moreover,

\[
\operatorname{bitlen}(U)
\le B(n)\lfloor\rho n\rfloor,
\]

so merging the returned factorizations, representing \(M=U^n\), and all
factor-stripping exponentiations also take numerical-QP time. This justifies
a fixed numerical-QP bound \(A(n)\).

Let

\[
n_i=\lfloor\rho^i n\rfloor.
\]

The recursion reaches a fixed base after \(h=O(\log(n+1))\) levels. Choose
fixed constants \(C,D\) large enough that, throughout the recursion,

\[
A(t),B(t)\le2^{C(\log_2(t+1))^D}
\le2^{C(\log_2(n+1))^D}.
\]

Unrolling (23) across at most \(h\) levels gives

\[
\log_2\mathcal T(n)
=O\!\left(h(\log_2(n+1))^D\right)
=(\log_2(n+1))^{O(1)}.
\]

This proves (24). For Las Vegas children, linearity of expectation gives
the same recurrence. Fixed contraction gives a finite-depth, finite-branching
recursion tree. If each call terminates almost surely, the whole finite tree
does too.

A mere numerical decrease of recursive inputs would not prove this bound.
For example, a recurrence with two calls on an input whose bit length drops
by only one can grow as \(2^{\Theta(n)}\), and a decrease by one in the
integer value can leave the bit length unchanged for exponentially many
steps. The fixed \(\rho\)-contraction is therefore essential.

## 8. Prime powers and the inverse-carry boundary

All previous arguments use the CRT decomposition into pairwise coprime
prime powers, but none replaces a component by its residue field. The group
identity for orders holds in \((\mathbb Z/R_j\mathbb Z)^\times\), and a
partial prime-power gcd is a valid factor. The proof therefore applies to
arbitrary odd composites, including pure prime powers and nonsquarefree
inputs, under hypotheses (2).

Finally, suppose \(1\le x,y<N\) and

\[
xy=1+cN.
\]

Then \(c\ge0\). If \(c=0\), positivity gives \(xy=1\), hence
\(x=y=1\). If \(c>0\), the strict inequalities \(y<N\) and \(x<N\) give

\[
cN=xy-1<xN,
\qquad
cN=xy-1<yN.
\]

Therefore

\[
0<c<\min(x,y)<N.
\]

If a positive integer divides both \(c\) and \(x\), it divides
\(xy-cN=1\); hence \(\gcd(c,x)=1\). The same argument gives
\(\gcd(c,y)=1\), and therefore

\[
\gcd(c,xy)=1.
\]

Strong induction can factor \(c\) because \(c<N\), including the trivial
factorization when \(c=1\). No prime obtained from \(c\) divides either
endpoint of that same inverse relation. This proves exactly the stated
direct-endpoint boundary and supplies no broader impossibility result for
nonlinear combinations of carry data.
