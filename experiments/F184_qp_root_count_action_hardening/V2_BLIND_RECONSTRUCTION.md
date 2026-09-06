# F184 V2 — statement-only blind reconstruction

## Isolation record and verdict

This reconstruction uses only `V2_STATEMENT.md`. Its verified SHA-256 is

```text
cf14b7ad25ecb9092419deaddca08327bcfe43d4bc9e35f89923a4f7e45f1632
```

No other F184 artifact or durable ledger was read. No prior proof or audit was
used. No mathematical computation was run.

**Verdict: VERIFIED.** The root count, prime-power gcd behavior, persistence of
rough local orders, exact block cardinality, simultaneous action conclusion,
and deterministic quasipolynomial cost all follow from the frozen statement.

## 1. Preliminary order facts

Write each hidden component as

\[
R_j=p_j^{e_j}.
\]

The following two facts account for the use of the exponent \(n\) and for the
claim that every gcd screen treats a whole hidden prime-power component at
once.

### 1.1 The exponent \(n\) removes a complete order-primary component

Let \(u\) be a unit modulo \(R_j\), and let its order be \(g\). Since

\[
R_j\le N<2^n,
\]

we have

\[
g\le \varphi(R_j)<R_j\le N<2^n.
\]

Consequently, for every rational prime \(\ell\mid g\),

\[
v_\ell(g)<n.
\tag{12}
\]

For an integer \(C\), the standard order-of-a-power formula gives

\[
\operatorname{ord}_{R_j}(u^{C^n})
=\frac{g}{\gcd(g,C^n)}.
\tag{13}
\]

If \(\ell\mid C\), then

\[
v_\ell(C^n)\ge n>v_\ell(g).
\]

Thus raising to \(C^n\) removes the entire \(\ell\)-primary part of \(g\).
If \(\ell\nmid C\), it removes none of that primary part. In particular,

\[
u^{C^n}=1\pmod {R_j}
\quad\Longleftrightarrow\quad
\operatorname{rad}(g)\mid C.
\tag{14}
\]

### 1.2 Coprime order makes the gcd all-or-none on a prime power

Suppose \(\gcd(g,p_j)=1\). Reduction

\[
(\mathbb Z/R_j\mathbb Z)^\times
\longrightarrow
(\mathbb Z/p_j\mathbb Z)^\times
\]

has a \(p_j\)-group kernel. Its intersection with the cyclic subgroup
\(\langle u\rangle\), whose order is coprime to \(p_j\), is therefore
trivial. Reduction is injective on \(\langle u\rangle\). Hence

\[
u=1\pmod {p_j}
\quad\Longleftrightarrow\quad
u=1\pmod {R_j}.
\tag{15}
\]

It follows that

\[
\gcd(u-1,R_j)\in\{1,R_j\}.
\tag{16}
\]

The same conclusion applies after every powering operation because the new
order divides the old order and remains coprime to \(N\). Therefore each
screen

\[
H=\gcd(u-1,N)
\]

is exactly the product of those full hidden components on which \(u\) is the
identity. This proves the asserted gcd trichotomy even when \(N\) contains
repeated prime factors. If \(H\notin\{1,N\}\), it is a proper factor of
\(N\).

## 2. Exact block size and separation

Put \(B=D+1\). At stage \(t\), the lower and upper endpoints of
\(\mathcal I_t\) are

\[
L_t=2+tB,
\qquad
U_t=1+(t+1)B.
\]

The inclusive cardinality is exactly

\[
U_t-L_t+1
=1+(t+1)B-(2+tB)+1
=B
=D+1.
\tag{17}
\]

Moreover,

\[
L_{t+1}=U_t+1.
\]

Thus the \(M\) blocks are pairwise disjoint consecutive blocks, and their
union is

\[
\{2,3,\ldots,1+M(D+1)\}.
\tag{18}
\]

In particular, the full bank contains exactly \(M(D+1)\) bases. Every base
obeys

\[
2\le a\le1+M(D+1)<T.
\tag{19}
\]

Any one base chosen from each block is therefore distinct from every base
chosen at another stage.

## 3. A surviving base exists at every stage

Assume inductively that the local orders of \(w_t\) are nontrivial, coprime
to \(N\), and \(T\)-rough. For a candidate \(a\in\mathcal I_t\), let

\[
C_a=a\prod_{k=1}^K(a^k-1),
\qquad
z_{t,a}=w_t^{C_a^n}.
\]

By Section 1.2, the gcd \(H_{t,a}\) is either \(1\), \(N\), or a proper
factor. Suppose that no candidate gives a proper factor and, toward a
contradiction, that every one of the \(D+1\) candidates gives

\[
H_{t,a}=N.
\]

Fix one hidden component \(R_j\), and select any rational prime
\(\ell\mid g_{t,j}\); such a prime exists because \(g_{t,j}>1\). Roughness
gives

\[
\ell>T>1+M(D+1)\ge a
\tag{20}
\]

for every base in the block. Since \(z_{t,a}=1\pmod {R_j}\), (14) gives

\[
\ell\mid C_a.
\]

Consider the polynomial over \(\mathbb F_\ell\)

\[
F(X)=X\prod_{k=1}^K(X^k-1).
\tag{21}
\]

It is monic and nonzero, and its degree is exactly

\[
1+\sum_{k=1}^K k=D.
\tag{22}
\]

The \(D+1\) integers in \(\mathcal I_t\) are distinct modulo \(\ell\) by
(20), and \(\ell\mid C_a=F(a)\) makes all of them roots of \(F\). A nonzero
degree-\(D\) polynomial over a field has at most \(D\) roots. This is a
contradiction.

Therefore, unless a proper factor has already appeared, at least one base in
the stage has

\[
H_{t,a}=1.
\tag{23}
\]

The deterministic rule that chooses the first such base is consequently
well-defined.

## 4. Induction through all stages

For the selected base \(a_t\), the next local order is

\[
g_{t+1,j}
=\frac{g_{t,j}}{\gcd(g_{t,j},C_{a_t}^n)}.
\tag{24}
\]

The condition \(H_{t,a_t}=1\), together with the all-or-none property
(15)--(16), says that \(w_{t+1}\) is nonidentity in every hidden component.
Thus

\[
g_{t+1,j}>1.
\]

Equation (24) also shows that \(g_{t+1,j}\mid g_{t,j}\). Its prime divisors
are therefore inherited from \(g_{0,j}\). They remain coprime to \(N\), and
their least prime divisor remains greater than \(T\). This proves the
inductive hypothesis at stage \(t+1\).

Starting from (2), Section 3 can therefore be applied successively at all
\(M\) stages. If no proper gcd occurs, the final orders satisfy

\[
g_{M,j}>1,
\qquad
\gcd(g_{M,j},N)=1,
\qquad
P^-(g_{M,j})>T
\tag{25}
\]

for every hidden prime-power component.

## 5. Every selected base acts with order greater than \(K\)

Fix a component \(R_j\), a rational prime

\[
\ell\mid g_{M,j},
\]

and a selected stage \(t\). The order chain in (24) is descending, so
\(\ell\mid g_{t,j}\) and \(\ell\mid g_{t+1,j}\). If
\(\ell\mid C_{a_t}\), Section 1.1 shows that \(C_{a_t}^n\) removes the
entire \(\ell\)-primary component of \(g_{t,j}\). That would contradict
\(\ell\mid g_{t+1,j}\). Hence

\[
\ell\nmid C_{a_t}.
\tag{26}
\]

Using the complete product defining \(C_{a_t}\), (26) gives simultaneously

\[
\ell\nmid a_t
\quad\text{and}\quad
a_t^k\not\equiv1\pmod\ell
\quad(1\le k\le K).
\tag{27}
\]

The first condition makes \(a_t\) a unit modulo \(\ell\). If its
multiplicative order were at most \(K\), taking \(k\) equal to that order
would contradict the second condition. Therefore

\[
\operatorname{ord}_\ell(a_t)>K.
\tag{28}
\]

This proves (10) simultaneously for every final order prime, every hidden
component, and every selected stage.

There is also a literal automorphism interpretation. If
\(\ell^r\parallel g_{M,j}\), exponentiation by \(a_t\) is an automorphism
of the cyclic \(\ell\)-primary subgroup because \(\ell\nmid a_t\). Its
order is \(\operatorname{ord}_{\ell^r}(a_t)\), which is a multiple of
\(\operatorname{ord}_\ell(a_t)\), and hence is greater than \(K\).
Furthermore, all selected bases lie below \(\ell\) by (19)--(20), so their
distinct integer values are distinct modulo \(\ell\). They induce \(M\)
distinct automorphisms on every such surviving primary subgroup.

This proves the factor-or-hardened-descendant transition (11). It does not
prove independence: several distinct long-order elements of
\((\mathbb Z/\ell\mathbb Z)^\times\) may lie in the same cyclic subgroup.
Nothing above yields equal hidden local orders, a common-order state, or a
factor after the surviving branch.

## 6. Deterministic quasipolynomial cost

Numerical quasipolynomial bounds are closed under fixed sums and products.
Since \(K\) and \(M\) are numerical QP,

\[
D=1+\frac{K(K+1)}2,
\qquad
M(D+1),
\qquad
a_{\max}=1+M(D+1)
\tag{29}
\]

are numerical QP. Thus the algorithm examines a QP number of candidates,
and every base has QP numerical size and polylogarithmic-in-\(n\) bit
length.

For \(a\ge2\),

\[
C_a
=a\prod_{k=1}^K(a^k-1)
<a^{,1+\sum_{k=1}^K k}
=a^D.
\]

Therefore

\[
\operatorname{bitlen}(C_a)
\le 1+D\log_2 a,
\tag{30}
\]

which is numerical QP. The exponent \(C_a^n\) has bit length

\[
O(n\operatorname{bitlen}(C_a)),
\tag{31}
\]

also numerical QP. The powers \(a^k\), their exact product \(C_a\), and
\(C_a^n\) can be constructed with a QP number of integer operations on
QP-bit integers. Modular exponentiation of \(w_t\) by \(C_a^n\) is
polynomial in \(n\) and the exponent bit length. Each gcd is polynomial in
\(n\).

Multiplying these bounds by the exact candidate count \(M(D+1)\) remains
QP. Choosing an integer roughness cap larger than \(1+M(D+1)\) also remains
within the class of fixed numerical QP bounds. Conditional on the stated
F181 interface that supplies \(w_0\) at that cap, the entire transition is
uniform deterministic quasipolynomial in \(n\).

At no point does the procedure require the factorization of \(C_a\). It
uses only its explicit product representation to construct an exponent,
then performs modular powering and gcd. No resultant or auxiliary
annihilator is introduced or factored.

## 7. Scope check

The proof establishes exactly these outcomes:

1. a proper gcd factors the arbitrary odd composite \(N\), including all
   prime-power multiplicities; or
2. the final rough descendant retains a nontrivial local order in every
   hidden component and supports \(M\) distinct public exponentiation
   automorphisms, each of order greater than \(K\), on every rational prime
   in its surviving order support.

The root count controls the order of each selected action separately. It
does not show that the actions generate independent directions. The stated
boundary therefore follows: the surviving branch need not contain an exact
common order or expose a factor.
