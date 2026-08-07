# F68 proof-blind reconstruction — root-labelled feedback closure

**Input used:** STATEMENT.md only.

**Verified statement SHA-256:**
199d4b6eb19c780a08d2f4acf668236ecdfe2307fcb57ed0d7ecde8432da65da.

**Overall verdict: PASS.**

All four mathematical claims follow from the stated hypotheses. The phrase
that \(A_i\equiv1\pmod N\) is “essential” needs the standard interpretation:
it is essential as a uniform sufficient hypothesis for the literal
positive-root map, but it is not logically necessary in every individual
instance. A weaker instance-specific condition can suffice.

The lift statement has two distinct scopes:

- before the old decode, only \(s_cH\) is canonical;
- after an unsuccessful old basis decode proves
  \(H\subseteq G=\{1,-1\}\), the larger coset \(s_cG\) is canonical.

The second conclusion does not hold without the unsuccessful-old-decode
hypothesis.

## 1. Exact square-class model

Write vectors in \(\mathbb F_2^m\) additively. For
\(x=(x_1,\ldots,x_m)\), put

\[
Q(x)=\prod_i A_i^{x_i}.
\]

The exact gcd-free parity matrix must have the property

\[
x\in\ker M
\quad\Longleftrightarrow\quad
Q(x)\text{ is a square in }\mathbb Z_{>0}.
\tag{1}
\]

This equivalence is the only square-class property used below. Positivity
makes the exact integer square root \(R(x)>0\) unique.

When the appended value causes further gcd refinement, the notation
\([M\mid b]\) must mean that all old columns have been re-expressed in the
joint refined row system. Exact refinement may change the row presentation,
but it must preserve (1) for vectors whose last coordinate is zero. This is
the stated “intrinsic old kernel” hypothesis.

## 2. Claim 1 — positive-root homomorphism

**Verdict: PASS.**

Let \(x,y\in K\), with addition taken modulo \(2\). For each index \(i\),
the exponent of \(A_i\) in \(Q(x)Q(y)\) is

\[
x_i+y_i
=
(x_i+y_i\bmod2)+2\,\mathbf 1_{\{x_i=y_i=1\}}.
\]

Therefore

\[
Q(x)Q(y)
=
Q(x+y)
\left(\prod_{i:x_i=y_i=1}A_i\right)^2.
\]

All quantities are positive squares. Taking their unique positive square
roots gives the exact identity

\[
\boxed{
R(x)R(y)
=
R(x+y)\prod_{i:x_i=y_i=1}A_i.
}
\tag{2}
\]

Since every \(A_i\equiv1\pmod N\), reduction of (2) gives

\[
\psi(x)\psi(y)=\psi(x+y).
\tag{3}
\]

Also,

\[
\psi(x)^2
\equiv R(x)^2
=Q(x)
\equiv1\pmod N.
\]

Thus \(\psi(x)\) is a unit in \(\mu_2(N)\), and (3) proves that

\[
\psi:K\longrightarrow\mu_2(N)
\]

is a group homomorphism. Consequently \(H=\psi(K)\) is a subgroup.

### Exact role of \(A_i\equiv1\pmod N\)

The individual congruences are sufficient for both required properties:

1. every dependency root lies in \(\mu_2(N)\);
2. every overlap correction in (2) disappears modulo \(N\).

They cannot be dropped without replacement. For example, take

\[
N=5,\qquad A_1=A_2=2.
\]

The two columns have the same nonzero square class, so
\(K=\langle(1,1)\rangle\). But

\[
R(1,1)=\sqrt{2\cdot2}=2,
\qquad
2^2\not\equiv1\pmod5.
\]

The proposed map does not even land in \(\mu_2(5)\).

Individual congruence to \(1\) is not a logically minimal condition. For
example,

\[
N=5,\qquad A_1=2,\qquad A_2=8
\]

again gives \(K=\langle(1,1)\rangle\), while

\[
R(1,1)=4\equiv-1\pmod5.
\]

Here the literal root map works although neither input is \(1\pmod5\).
Instance-wise, it is enough to require that every dependency product be
\(1\pmod N\) and that every overlap factor in (2) be \(1\pmod N\). The
statement uses the cleaner uniform hypothesis.

## 3. Claim 2 — one closure adds one root coset

**Verdict: PASS.**

A vector in the new kernel has the form \((x,t)\), with
\(x\in\mathbb F_2^m\), \(t\in\mathbb F_2\), and satisfies

\[
Mx+tb=0.
\tag{4}
\]

### Nonclosure case

If \(b\notin\operatorname{colspan}(M)\), equation (4) has no solution with
\(t=1\). With \(t=0\), it is exactly \(Mx=0\). Hence

\[
\boxed{
\ker[M\mid b]=K\times\{0\}.
}
\tag{5}
\]

There is no new dependency direction and no new exact-root output.

### Closure case

Suppose \(b\in\operatorname{colspan}(M)\), and choose \(c\) with \(Mc=b\).
Then

\[
z_c=(c,1)\in\ker[M\mid b].
\]

Every solution of (4) with \(t=1\) has \(M(x+c)=0\), so it is
\(z_c+(k,0)\) for a unique \(k\in K\). The last coordinate of \(z_c\) is
\(1\), so its span meets \(K\times\{0\}\) trivially. Therefore

\[
\boxed{
K'
=(K\times\{0\})\oplus\langle z_c\rangle.
}
\tag{6}
\]

Because \(Mc+b=0\), the integer

\[
A_{m+1}\prod_iA_i^{c_i}
\]

is an exact square. Let its positive square root, reduced modulo \(N\), be
\(s_c\). Applying Claim 1 to the new kernel and (6) gives

\[
\boxed{
H'=\psi'(K')=\langle H,s_c\rangle.
}
\tag{7}
\]

Thus one appended column adds no root coset in the nonclosure case. In the
closure case it adds at most the single coset \(s_cH\).

### Lift dependence

If \(c'\) is another solution of \(Mc'=b\), then

\[
k=c'+c\in K.
\]

In the new kernel,

\[
z_{c'}=z_c+(k,0).
\]

The new positive-root map is a homomorphism, so

\[
\boxed{
s_{c'}=s_c\psi(k)=s_c\psi(c'+c)\pmod N.
}
\tag{8}
\]

The literal label can change. Equation (8) proves exactly that

\[
\boxed{s_{c'}H=s_cH.}
\tag{9}
\]

No stronger quotient is canonical at this stage without another hypothesis.

### Why modulo \(G=\{\pm1\}\) is not yet valid

Take

\[
N=15,\qquad A_1=A_2=16.
\]

The old column is zero because \(16=4^2\), so

\[
K=\mathbb F_2,\qquad H=\{1,4\}.
\]

For the appended duplicate, \(b=0\). Both \(c=0\) and \(c'=1\) are lifts.
Their induced roots are

\[
s_0=4,\qquad s_1=\sqrt{16\cdot16}=16\equiv1\pmod{15}.
\]

They differ by the old root \(4\in H\), as (8) requires. But

\[
4G\ne G
\quad\text{for}\quad
G=\{1,14\}.
\]

Thus \(s_cG\) is not lift-independent before one knows \(H\subseteq G\).
This old state is factor-bearing:
\(\gcd(4-1,15)=3\), so it is correctly excluded by Claim 3's
unsuccessful-decode hypothesis.

## 4. Odd-modulus sign lemma

The nonsquarefree case rests on the following exact lemma.

### Lemma

Let

\[
N=\prod_{j=1}^t p_j^{e_j}
\]

be odd, and let \(z^2\equiv1\pmod N\). For every \(j\), exactly one of

\[
z\equiv1\pmod{p_j^{e_j}},
\qquad
z\equiv-1\pmod{p_j^{e_j}}
\tag{10}
\]

holds. Moreover,

\[
\gcd(z-1,N)
=
\prod_{j:z\equiv1\;(\mathrm{mod}\;p_j^{e_j})}p_j^{e_j},
\tag{11}
\]

\[
\gcd(z+1,N)
=
\prod_{j:z\equiv-1\;(\mathrm{mod}\;p_j^{e_j})}p_j^{e_j}.
\tag{12}
\]

The two gcds are coprime and their product is \(N\). Hence

\[
\boxed{
z\notin\{1,-1\}\pmod N
\quad\Longleftrightarrow\quad
1<\gcd(z-1,N)<N
}
\tag{13}
\]

and equivalently the \(z+1\) gcd is proper.

#### Proof

For an odd prime \(p_j\),

\[
p_j^{e_j}\mid(z-1)(z+1).
\]

The gcd of \(z-1\) and \(z+1\) divides \(2\), so \(p_j\) divides at most one
of them. The full power \(p_j^{e_j}\) must therefore divide exactly one
factor. This proves (10), and (11)–(12) follow by collecting prime-power
components.

If all signs in (10) are \(+\), then \(z=1\pmod N\); if all are \(-\), then
\(z=-1\pmod N\). Otherwise both sign sets are nonempty, and (11)–(12) are
proper nontrivial divisors. This proves (13). \(\square\)

This proof uses oddness. It does not assume that \(N\) is squarefree. A prime
power contributes one whole CRT sign component. In particular, if \(N\) is
an odd prime power, then \(\mu_2(N)=G\), so this decoder cannot obtain a
non-global square root of one.

## 5. Claim 3 — one new test is complete

**Verdict: PASS for every odd \(N>1\), including nonsquarefree \(N\).**

Let \(u_1,\ldots,u_d\) be the tested basis of \(K\). Each
\(\psi(u_j)\) lies in \(\mu_2(N)\). By the odd-modulus sign lemma, absence of
a proper sign gcd implies

\[
\psi(u_j)\in G=\{1,-1\}
\]

for every basis vector. Claim 1 gives, for
\(x=\sum_j\alpha_ju_j\),

\[
\psi(x)=\prod_j\psi(u_j)^{\alpha_j}\in G.
\]

Therefore

\[
\boxed{H=\psi(K)\subseteq G.}
\tag{14}
\]

This also proves that screening a basis is complete for the entire old
decoder. It is not necessary to enumerate all of \(K\).

### Nonclosure

If \(b\notin\operatorname{colspan}(M)\), (5) says that the new kernel and
root image are the old ones. Since \(H\subseteq G\), no dependency can give a
proper sign gcd.

### Closure

If \(b\) closes, (7) and (14) give

\[
H'=\langle H,s_c\rangle.
\]

If \(s_c\in G\), then \(H'\subseteq G\), so the sign lemma rules out every
factor-bearing dependency.

If \(s_c\notin G\), then the dependency \(z_c\) itself has a non-global root
of one. The sign lemma gives proper factors through both

\[
\gcd(s_c-1,N)
\quad\text{and}\quad
\gcd(s_c+1,N).
\]

Consequently,

\[
\boxed{
H'\text{ contains a factor-bearing root}
\quad\Longleftrightarrow\quad
s_c\notin G.
}
\tag{15}
\]

This is the claimed if-and-only-if test.

Finally, for another lift \(c'\), equations (8) and (14) give

\[
s_{c'}=s_c h
\quad\text{for some }h\in H\subseteq G.
\]

Hence

\[
\boxed{s_{c'}G=s_cG.}
\tag{16}
\]

Membership in \(G\) is lift-independent. If \(h=-1\), changing the lift only
swaps the two sign gcds. Thus one induced-root test is complete after the old
basis has been screened.

### Needed hypotheses for the iff

The following hypotheses are used:

1. \(N>1\) is odd.
2. Every old and new indexed value is positive and congruent to \(1\pmod N\).
3. The parity matrix is exact, so its kernel is precisely the set of exact
   integer-square products.
4. Joint refinement preserves the intrinsic old kernel.
5. Every vector in a generating basis of \(K\) was tested with both sign
   gcds, and no proper factor occurred.
6. “Factor-bearing” refers to these exact-root sign gcds. It does not refer
   to an unrelated factorization method.

Without item 5, \(H\) can contain a non-global root, the enlarged decoder can
already be factor-bearing independently of \(s_c\), and only the \(H\)-coset
in (9), not the \(G\)-coset in (16), is canonical.

## 6. Claim 4 — indexed semantics and examples

**Verdict: PASS.**

### Indexed duplicates

A matrix column represents an indexed occurrence. If two equal values are
retained as two indices, they give two equal columns and their coordinate
sum is a dependency. If the values are deduplicated before matrix
construction, only one coordinate exists and this dependency does not exist.
Equal arithmetic values do not create an unrecorded second column.

### The \(N=21\) duplicate is a global decoy

Take one old indexed value

\[
A_1=22=2\cdot11\equiv1\pmod{21}.
\]

Its column is nonzero, so the old one-column kernel is trivial. Append a
separately indexed duplicate \(A_2=22\). The two parity columns are equal,
and the new dependency is \((1,1)\). Its exact product and positive root are

\[
A_1A_2=22^2,
\qquad
R(1,1)=22\equiv1\pmod{21}.
\]

Thus the closure is real, but its root is global:

\[
\gcd(22-1,21)=21,
\qquad
\gcd(22+1,21)=1.
\]

It gives no proper factor.

### The \(N=55\) zero column is useful

The appended value

\[
A_{m+1}=21^2=441\equiv1\pmod{55}
\]

is already an exact square, so its rational square class is zero under every
exact joint refinement. Thus \(b=0\), \(c=0\) is a valid lift, and the new
coordinate alone is a dependency. Its induced positive root is \(21\).
Indeed,

\[
\gcd(21-1,55)=\gcd(20,55)=5,
\]

\[
\gcd(21+1,55)=\gcd(22,55)=11.
\]

Thus column closure is only the linear-algebra gate. The induced root still
needs the sign test.

## 7. Scope and complexity

**Verdict: PASS.**

The proof supplies an exact update rule:

\[
b\notin\operatorname{colspan}(M)
\Rightarrow \text{no new dependency},
\]

\[
b\in\operatorname{colspan}(M)
\Rightarrow \text{one induced-root coset }s_cH.
\]

It supplies no law that closure occurs often and no law that a closing root
lies outside \(G\). It therefore gives no selector and no factoring
algorithm.

Linear algebra over \(\mathbb F_2\), multiplication of the selected explicit
integers, and exact integer square-root extraction are polynomial in the
total explicit input length and matrix dimensions. This statement does not
bound the number or total bit length of values generated by repeated
feedback in terms of \(\log N\). Such a bound would require a separate
argument.

## Final classification

| Claim | Verdict | Exact qualification |
|---|---|---|
| Positive-root homomorphism | PASS | \(A_i\equiv1\) is sufficient and cannot be dropped wholesale; it is not instance-wise minimal. |
| One closure adds one root coset | PASS | The canonical object is \(s_cH\). |
| One new test is complete | PASS | The old basis screen proves the needed condition \(H\subseteq G\); without that condition only the \(H\)-coset is canonical. |
| Arbitrary odd nonsquarefree \(N\) | PASS | CRT components are odd prime powers, and every root of one has one sign on each whole component. |
| Indexed semantics and examples | PASS | A duplicate counts only when retained as a second index. |
| Algorithmic scope | PASS | Exact incremental decoding only; no polynomial-in-\(\log N\) feedback theorem follows. |
