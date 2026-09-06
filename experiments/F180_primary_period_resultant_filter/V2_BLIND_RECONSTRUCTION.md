# F180 V2 blind reconstruction

## Input and verdict

This reconstruction uses only `V2_STATEMENT.md`. Its SHA-256 is

```text
8bf8e7ca10a0d58f8548bd88605d015b87fa62f41208e542075cf83951aa6a3c
```

**Verdict: proved.** All mathematical and complexity claims follow from the
stated hypotheses. Two readings are important:

1. A “proper” gcd means a nontrivial proper divisor, (1<H_\delta<N).
2. To factor (M) in QP time, factor the small resultants separately and
   aggregate their factorizations. Do not trial-divide the expanded integer
   (M).

## 1. The input length supplies the missing multiplicity

Write (R_j=p_j^{e_j}). The (R_j) are pairwise coprime. For every unit of
order (f_j) modulo (R_j),

\[
f_j\mid \varphi(R_j)<R_j\leq N.
\]

The definition

\[
n=\lceil\log_2(N+1)\rceil
\]

is exactly the binary length of (N). In particular, (N<2^n). Therefore,
for every primary divisor \(\ell^a\parallel f_j\),

\[
2^a\leq \ell^a\leq f_j<N<2^n,
\qquad\text{so}\qquad a<n.
\tag{15}
\]

This strict inequality is what makes the exponent (A_\delta^n) delete a
whole primary power after only one divisibility witness in (A_\delta).

## 2. Exact primary-power deletion

Fix (j) and (delta\in\{0,3\}). Put (b=N+\delta), (A=A_\delta), and
(E=A^n). The standard order formula gives

\[
\operatorname{ord}_{R_j}(y^E)
=\frac{f_j}{\gcd(f_j,E)}.
\tag{16}
\]

For a prime (ell),

\[
\begin{aligned}
\ell\mid A
&\iff \ell\mid b^k-1\text{ for some }1\leq k\leq K\\
&\iff \ell\nmid b\text{ and }\operatorname{ord}_\ell(b)\leq K.
\end{aligned}
\tag{17}
\]

Indeed, a congruence (b^k\equiv1\pmod\ell) first makes (b) a unit, and
then its order is at most (k\leq K). Conversely, use (k) equal to its
order.

If (ell\nmid A), then (v_\ell(E)=0), so the full factor (ell^a) stays
in (16). If (ell\mid A), then

\[
v_\ell(E)=n v_\ell(A)\geq n>a,
\]

by (15), so the full factor (ell^a) is removed. No partial primary power
can remain. Thus

\[
\operatorname{ord}_{R_j}(z_\delta)
=
\prod_{\substack{\ell^a\parallel f_j\\
\ell\mid N+\delta\ \text{or}\
\operatorname{ord}_\ell(N+\delta)>K}}
\ell^a,
\]

which proves (6) and (7).

### All gcd shapes

The gcd need not select whole hidden prime powers. If
(R_j=p_j^{e_j}), then its local contribution can be any

\[
\gcd(z_\delta-1,R_j)=p_j^{r_j},
\qquad 0\leq r_j\leq e_j.
\]

This causes no gap:

- If (1<H_\delta<N), then (H_\delta) and (N/H_\delta) give a
  nontrivial factorization, even when some (0<r_j<e_j).
- If (H_\delta=1), then (z_\delta\not\equiv1\pmod {R_j}) for every
  (j). Hence every local order in (7) is greater than one and retains at
  least one primary part.
- If (H_\delta=N), then (z_\delta\equiv1\pmod {R_j}) for every (j).
  Hence every local order in (7) is one.

For (delta=0), every (ell\mid f_j) satisfies (ell\nmid N) because
(gcd(f_j,N)=1). The nonunit clause in (7) is therefore impossible. Every
prime in a surviving local order has

\[
\operatorname{ord}_\ell(N)>K.
\]

Together with the nontriviality forced by (H_0=1), this proves (8).

## 3. Double extinction and resultant multiplicity

Assume (H_0=H_3=N). Fix (ell^a\parallel f_j). The exact deletion result
shows that there are (k,l\in\{1,\ldots,K\}) such that

\[
N^k\equiv1\pmod\ell,
\qquad
(N+3)^l\equiv1\pmod\ell.
\tag{18}
\]

Both bases must be units modulo (ell). In particular, the second
extinction rules out the alternative (ell\mid N+3), because that
alternative would retain (ell^a).

Modulo (ell), the residue (X=N) is a common root of
(X^k-1) and ((X+3)^l-1). Hence

\[
\ell\mid R_{k,l}.
\tag{19}
\]

The integer resultant is nonzero. If a complex number (zeta) were a
common root, then (|\zeta|=1) and (|\zeta+3|=1). But

\[
|\zeta+3|\geq 3-|\zeta|=2,
\]

a contradiction.

Since (X^k-1) is monic, the root formula for the resultant gives

\[
R_{k,l}
=\prod_{\zeta^k=1}\left|(\zeta+3)^l-1\right|.
\]

For every such (zeta),

\[
\left|(\zeta+3)^l-1\right|
\leq |\zeta+3|^l+1
\leq4^l+1
<2^{2l+1}.
\]

Therefore

\[
\log_2 R_{k,l}<k(2l+1),
\]

which proves (11).

One factor of the product in (12) is divisible by (ell), by (19). Thus

\[
v_\ell(M)
=n\sum_{u=1}^K\sum_{v=1}^K v_\ell(R_{u,v})
\geq n>a.
\]

Consequently (ell^a\mid M). Applying this to every primary divisor of
every (f_j) proves

\[
f_j\mid M\qquad(1\leq j\leq s).
\]

The outer (n)-th power in (12) is therefore sufficient even when a
resultant contains only one copy of (ell). No unproved resultant
multiplicity is needed.

## 4. Factor-first recovery

Factor every (R_{k,l}), combine the lists of prime factors, and multiply
all multiplicities by (n). This gives a complete factorization of (M).
Start with (m=M), represented both as an integer and by this
factorization. Maintain the invariant

\[
f_j\mid m\quad\text{for every }j.
\tag{20}
\]

For a prime (q\mid m), compute

\[
D=\gcd(y^{m/q}-1,N).
\]

Use the following three branches.

1. If (1<D<N), return the factor (D). This also covers a gcd that cuts
   through one hidden prime power.
2. If (D=N), replace (m) by (m/q). All local orders divide (m/q),
   so (20) remains true.
3. If (D=1), retain this copy of (q).

After every deletion, restart a scan over the prime divisors. Stop after a
full scan makes no deletion. This terminates because each deletion strictly
decreases (m).

Suppose the algorithm stops without a factor. For every (q\mid m), the
terminal gcd is then one. If some (f_j) were a proper divisor of (m),
there would be a prime (q\mid m) with
(v_q(f_j)<v_q(m)). Then (f_j\mid m/q), so

\[
y^{m/q}\equiv1\pmod {R_j}.
\]

In particular, (p_j\mid\gcd(y^{m/q}-1,N)), contradicting the terminal
gcd value one. Hence

\[
m=f_1=f_2=\cdots=f_s.
\tag{21}
\]

The factorization of (m) is still known. Also

\[
m=f_j\geq\sigma(f_j)>T\geq n.
\]

Thus the no-factor outcome is exactly the claimed factored common-order
state ((y,m)) above (n).

## 5. The trichotomy

The possible gcd values give the stated exhaustive procedure.

- If (1<H_0<N), return a factor.
- If (H_0=1), return the first hard descendant. Section 2 proves (8), and
  every hidden component has a nontrivial surviving primary part.
- If (H_0=N), compute (H_3).
  - If (1<H_3<N), return a factor.
  - If (H_3=1), return the second hard descendant. Extinction at
    (delta=0) says every prime in every original (f_j) has
    (N)-action order at most (K). Every prime surviving the
    (delta=3) filter either divides (N+3) or has
    ((N+3))-action order greater than (K). Every hidden component has at
    least one such survivor.
  - If (H_3=N), Sections 3 and 4 return either a factor or the exact
    common-order state.

These terminal cases are disjoint and exhaustive. This proves (14).

The hard cases are genuine under the stated assumptions. For example, set
(c=1) and (T=n).

- For (N=2773=47\cdot59), (n=12), (K=4), and (y=2187), the local
  orders are (23) and (29). Also
  (operatorname{ord}_{23}(N)=11) and
  (operatorname{ord}_{29}(N)=28). Hence (H_0=1).
- For (N=43739=191\cdot229), (n=16), (K=5), and (y=42072), both
  local orders are (19). Here (N\equiv1\pmod {19}), while
  (N+3\equiv4\pmod {19}) and
  (operatorname{ord}_{19}(4)=9). Hence (H_0=N) and (H_3=1).

Both examples satisfy (gcd(f_j,N)=1) and
(sigma(f_j)>T\geq n). They show directly why the theorem cannot replace
the hard branch by a guaranteed factor.

## 6. Exact bit-cost bound

The integers (N) and (N+3) have (O(n)) bits. Therefore

\[
\begin{aligned}
\log_2 A_\delta
&=\sum_{k=1}^K O(kn)=O(nK^2),\\
\log_2(A_\delta^n)
&=O(n^2K^2).
\end{aligned}
\tag{22}
\]

There are (K^2) resultants. Section 3 gives (O(K^2)) bits per
resultant. If (B=\prod_{k,l}R_{k,l}), then

\[
\log_2 B=O(K^4),
\qquad
\log_2 M=O(nK^4).
\tag{23}
\]

Exact resultant computation is within the claimed bound. Trial division of
one (O(K^2))-bit resultant uses at most (2^{O(K^2)}) bit operations.
The extra factor (K^2) for all resultants is absorbed in the exponent.
Their factorizations give the factorization of (M=B^n) by multiplying
the recorded exponents by (n).

The two filter exponentiations use exponents with
(O(n^2K^2)) bits. During stripping, every exponent has
(O(nK^4)) bits. The number of deletion attempts and full scans is
polynomial in that bit length. Modular exponentiation, integer arithmetic,
and gcd computation therefore have total cost polynomial in (n) and
(K).

Because (c\geq1) is fixed and

\[
K=\left\lceil(\log_2(n+1))^c\right\rceil,
\]

every such polynomial cost is at most (2^{O(K^2)}), and trial division
also costs (2^{O(K^2)}). Hence the total bit cost is

\[
2^{O(K^2)}
=2^{(\log n)^{O(1)}}.
\]

The proof closes only the synchronized-extinction case. The two explicit
hard-branch examples show that it does not force a filtered order to vanish
and does not imply QP integer factoring.
