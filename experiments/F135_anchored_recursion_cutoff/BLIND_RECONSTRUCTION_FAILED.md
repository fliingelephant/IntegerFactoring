# F135 blind reconstruction — narrow statement failure

## Protocol

I reconstructed F135 from `STATEMENT.md` only. I did not read the proof,
manifest, audits, ledgers, or any other F135 file.

Frozen input:

```text
STATEMENT.md
be8b976e72df20cfc1b19fe0e3618b9c23f508b45d00001db54558c42462a5fd
```

## Verdict

**FAIL as written, for one narrow but real scope defect.**

Theorems 1, 2, 4, and 5 reconstruct. The quantitative argument in Theorem
3 also reconstructs under its stated no-large-bucket assumption. However,
the boxed dichotomy (13) omits the case \(R_A=1\). In that case there is no
non-anchor residual block to release. The statement explicitly notes this
immediately before (13), so the phrase “exact dichotomy” is not literally
correct unless “small-block release” is defined to include residual
exhaustion.

The minimal repair is to replace (13) by

\[
\boxed{
\text{small-block release, anchor-smooth residual exhaustion, or}
\ \Omega(n^3/\log n)\text{ reused-row columns}.}
\]

Equivalently, the first branch can be named “presentation-level release or
exhaustion.” This repair does not turn the result into a dependency theorem.

There is also a minor notation typo in (6): `mid` must be `\mid`.

## Reconstruction of Theorem 1

For an eligible anchor, \(H_\ell=w+NA_\ell\) is divisible by \(\ell\), so

\[
z_\ell=H_\ell/\ell
\]

is an integer. Since \(0\le A_\ell<\ell\),

\[
0<H_\ell<N\ell,
\qquad 0<z_\ell<N.
\]

Also, \(c_\ell=\ell q<N\), and

\[
c_\ell z_\ell
=q(w+NA_\ell)
=1+(k+qA_\ell)N.
\]

Thus \(z_\ell=\iota_N(c_\ell)\), which proves (1).

If \(A_\ell=0\), then \(H_\ell=w\), so

\[
P_N(\ell q)=qH_\ell=qw=P_N(q).
\]

If \(A_\ell>0\), then

\[
z_\ell=\frac{w+NA_\ell}{\ell}
>\frac{N}{\ell}\ge\frac NB.
\]

Finally, \(z_\ell(\ell q)\equiv1\pmod N\), and
\(1\le\ell q<N\). Hence

\[
\iota_N(z_\ell)=\ell q,
\qquad
P_N(z_\ell)=P_N(\ell q).
\]

The cutoff and duplicate law are exact. They do not apply to a proper factor
of \(z_\ell\), a multi-block word, a power, or a wrapped large endpoint.

## Reconstruction of Theorem 2

For distinct digits,

\[
H_j-H_i=N(A_j-A_i).
\]

Since \(H_i\equiv w\pmod N\) and \(w\) is a unit modulo \(N\),
\(\gcd(H_i,N)=1\). Therefore

\[
\gcd(H_i,H_j)
=\gcd(H_i,N(A_j-A_i))
=\gcd(H_i,A_j-A_i)
\le |A_j-A_i|<B.
\]

Each \(z_t\) divides \(H_t\). Thus

\[
\gcd(z_i,z_j)\mid\gcd(H_i,H_j)<B.
\]

No assumption about \(\gcd(\ell_i,\ell_j)\) is needed. Division can reduce a
gcd, but it cannot create a new common divisor.

## Reconstruction and hostile check of Theorem 3

### Factor-free release

All anchor primes in one bucket divide the same known integer
\(H_A=w+NA\). Their full powers can be removed by exact repeated division;
this does not require factoring \(N\) or \(H_A\). With

\[
H_A=S_AR_A,
\qquad
S_A=\prod_{\ell\in\mathcal L_A}\ell^{v_\ell(H_A)},
\]

complete gcd-free refinement can only split the remaining cofactor further.
After named anchor-prime powers are removed, each residual block therefore
divides \(R_A\). Sharing with an old block does not invalidate this claim:
the shared refined block still divides \(R_A\).

For \(A=0\), \(H_0=w<N\), and \(S_0\ge L_0>B\). Hence

\[
R_0=H_0/S_0<N/B.
\]

For \(A>0\), \(A\le B-1\), so \(H_A=w+NA<NB\). If
\(S_A\ge L_A>B^2\), then

\[
R_A=H_A/S_A<N/B.
\]

Thus the factor-free statement and the numerical bounds (9) and (10) are
sound. If \(R_A>1\), a non-anchor residual exists and every refined part of
it meets the small-size condition. If \(R_A=1\), no such block exists.

The release is factor-free. It is not factor-correlated. It does not by
itself give a parity dependency or a non-global root.

### Independent proof of the width bound

Let

\[
E=\prod_{\substack{\ell\le B\text{ prime}\\\ell\nmid Nq}}\ell.
\]

For \(x\ge2^{18}\), an elementary central-binomial estimate gives the
explicit bound

\[
\vartheta(x)>\frac{6x}{25}.
\tag{A}
\]

Here is a self-contained verification of the constant. Put
\(m=\lfloor x/2\rfloor\). Then

\[
\psi(x)\ge\log {2m\choose m}
\ge (x-1)\log2-\log(x+1).
\]

Moreover,

\[
\psi(x)-\vartheta(x)
=\sum_{j\ge2}\vartheta(x^{1/j})
\le\frac{\sqrt{x}(\log x)^2}{\log2}.
\]

The error ratio decreases for \(x\ge2^{18}\). At \(x=2^{18}\), these two
bounds give

\[
\frac{\vartheta(x)}x>0.2544647>0.24.
\]

This proves (A). Since the product of excluded distinct primes divides
\(Nq<N^2/B\), and \(N<2^n\),

\[
\log E
>\frac{6B}{25}-2n\log2+\log B.
\tag{B}
\]

Under (11), the bucket product satisfies

\[
E=L_0\prod_{A>0}L_A
\le B(B^2)^d.
\tag{C}
\]

For \(B=n^3\), comparison of (B) and (C) gives

\[
(2d+1)3\log n
>\frac{6n^3}{25}-2n\log2+3\log n,
\]

and hence

\[
d>
\frac{n^3}{25\log n}
-\frac{n\log2}{3\log n}.
\]

This reconstructs (12) with the stated strict inequality.

### Reused-row count and deduplication

If \(r>B\) has odd valuation in \(q\), then Theorem 2 implies that \(r\)
can divide \(H_A\) for at most one digit \(A\). Therefore

\[
v_r(qH_A)=v_r(q)+v_r(H_A)
\]

is odd for at least \(d-1\) occupied nonzero digits. The values \(qH_A\)
are distinct for distinct \(A\). Global exact-value deduplication keeps one
occurrence of every distinct value, even if its first occurrence came from
an older layer. Thus the \(d-1\) count survives deduplication. A proper
endpoint screen can only terminate earlier with a factor.

This is a row-width theorem. It is not a kernel, 2-core, or normalized-root
theorem.

### The omitted \(R_A=1\) branch is real

The omission is not only formal. The following exact setup has a large odd
row in \(q\), a large same-digit bucket, null endpoint screens, and
\(R_A=1\):

\[
N=383237=157\cdot2441,
\quad B=23,
\quad q=47,
\quad w=8154,
\]

\[
qw=383238=1+N,
\qquad
H_1=w+N=391391=7\cdot11\cdot13\cdot17\cdot23.
\]

For every

\[
\ell\in\{7,11,13,17,23\},
\]

the carry digit is \(A_\ell=1\). Thus

\[
L_1=S_1=391391>B^2,
\qquad R_1=1.
\]

All five anchored presentations have the same exact value

\[
(\ell q)(H_1/\ell)=qH_1=18395377=1+48N.
\]

The base screen and all anchored endpoint screens are null:

\[
\gcd(q\pm w,N)=1,
\qquad
\gcd(\ell q\pm H_1/\ell,N)=1.
\]

This finite example is not a counterexample to the specialized
\(B=n^3,n\ge64\) width inequality. It shows that \(R_A=1\) is a genuine
arithmetic outcome and is not a hidden small-block release. A trichotomy, or
an explicit convention that “release” includes exhaustion, is necessary.

## Reconstruction of Theorem 4

Order vertices with every parent before its children. Column \(C_v\) has a
one on its diagonal row \(r_v\), and its only possible second one is in an
earlier parent row. The matrix is triangular with diagonal one. Therefore
its column kernel is zero.

An internal row occurs in its own column and in its \(b\) child columns, so
its degree is \(b+1\). A leaf row occurs only in its own column. Peeling first
removes all leaf columns. Their parents then become leaves, and the same
step repeats to the root. Sibling residual rows are distinct by
construction.

The vertex count is

\[
V=1+b+\cdots+b^T=\frac{b^{T+1}-1}{b-1}.
\]

If \(\log b=O(\log n)\) and \(T=O((\log n)^2)\), then

\[
\log V=O((\log n)^3),
\qquad
V=2^{O((\log n)^3)}.
\]

This proves only an abstract incidence obstruction. It says nothing about
which trees canonical arithmetic can realize.

## Reconstruction of Theorem 5

### CRT consistency and infinitude

All moduli in (18) and (19) are pairwise coprime. The combined CRT class is

```text
a = 4364121389770277
M = 12522249183293850
gcd(a,M) = 1
```

Choose one prime in the class \(1\pmod M\) and one prime in the class
\(a\pmod M\). The prime number theorem in fixed arithmetic progressions
lets both primes be selected in disjoint intervals of comparable size.
Their product is congruent to \(a\pmod M\), is balanced, and has distinct
prime factors. As the intervals tend to infinity, the factors exceed every
fixed polylogarithmic trial bound. This gives infinitely many trial-hard
members.

### Canonical identities

For the five base blocks, the square-modulus congruences give

\[
1+k_vN\equiv q_v\pmod {q_v^2}.
\]

Thus \(q_v\mid C_v\), \(v_{q_v}(C_v)=1\), and

\[
0<C_v/q_v<N
\]

because \(k_v<q_v\). Therefore \(P_N(q_v)=C_v\).

The edge carries satisfy

\[
k_1=k_0+q_0,
\quad
k_2=k_0+3q_0,
\quad
k_3=k_1+q_1,
\quad
k_4=k_2+q_2.
\]

The anchor congruences in (19) make the corresponding \(H\) divisible by
\(3,7,13,29\). Equivalently, they make \(C_1,C_2,C_3,C_4\) divisible by
\(15,35,143,551\), respectively. In every case \(k_v<c\), so \(C_v/c<N\).
This proves all identities in (20).

Reduction modulo the five displayed block primes gives exactly

\[
\begin{pmatrix}
1&1&1&0&0\\
0&1&0&1&0\\
0&0&1&0&1\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix}
\]

for valuation parity. The square-modulus residues show that every displayed
one has valuation exactly one, not merely positive valuation. The matrix is
triangular after the forest ordering, so it has full column rank.

Rows \(23\) and \(37\) first remove \(C_3\) and \(C_4\). Rows \(11\) and
\(19\) then remove \(C_1\) and \(C_2\). Row \(5\) finally removes \(C_0\).
Extra prime rows inside these five values do not change the degrees of the
five named rows. Unselected source columns can change them, which is why the
selected-source scope is essential.

For a presentation \(cz=1+kN\), reduction modulo a prime factor \(s\mid N\)
gives \(z\equiv c^{-1}\pmod s\). A sign screen can hit \(s\) only if
\(s\mid c^2-1\) or \(s\mid c^2+1\). All displayed \(c\)'s are fixed. Hence
every displayed screen is null once both semiprime factors exceed the
finitely many integers \(c^2\pm1\).

### Independent exact member

Sage, with proved primality tests, produced

```text
P = 12584860429210319251 = 1 + 1005 M
Q = 15131241134808741077 = a + 1208 M
N = 190424557802293971365417506484567573327
Q/P = 1.20233682526094...
ceil(log2(N+1)) = 128
```

Both \(P\) and \(Q\) are prime. For this \(N\):

- every congruence in (18) and (19) holds;
- every identity in (20) has integral canonical endpoints;
- the five parity rows are exactly (21); and
- every base and edge endpoint sign gcd is \(1\).

This independently verifies the CRT arithmetic and the sign-screen scope.

## Final scope

The reconstructed result proves a real recursion cutoff and a real
incidence obstruction. It does not control proper blocks released from a
reciprocal endpoint. It does not control wrapped, powered, or multi-block
feedback. The selected CRT family does not control the complete source.
Nothing here proves a dependency, a non-global normalized root, or a
factoring algorithm.

After the narrow \(R_A=1\) wording repair, I find no further defect in the
statement.
