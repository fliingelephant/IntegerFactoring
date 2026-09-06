# F133 blind reconstruction

## Audit status

**PASS.** I reconstructed all five theorems, the quantitative constant in
Corollary 4A, the quasipolynomial cost bound, and the stated scope limits.

I read only `STATEMENT.md` in this experiment directory. I did not read the
proof, manifest, prior audits, ledgers, or any other F133 artifact.

The frozen source was:

```text
STATEMENT.md
SHA-256 b4848b22ea324421282dcfbbef9afc28576d2ea8233f8256a03b0797e1ea1bb7
```

Theorem 5 is conditional on the stated F130 and F132 transcript-cost claims.
This reconstruction verifies the conditional implication. It does not verify
those antecedent claims, because they were outside the permitted source.

## 1. Exact anchored-carry law

Let \(w=\iota_N(q)\). For an eligible prime \(\ell\), \(N\) is invertible
modulo \(\ell\). Thus there is one and only one

\[
A_\ell\in\{0,\ldots,\ell-1\}
\]

such that \(w+NA_\ell\equiv0\pmod\ell\).

The inequalities are exact. Since \(\ell\le B\) and \(q<N/B\),

\[
0<\ell q<N.
\]

Also, \(1\le w<N\) and \(0\le A_\ell<\ell\), so

\[
0<w+NA_\ell<N+N(\ell-1)=N\ell.
\]

Therefore

\[
z_\ell=\frac{w+NA_\ell}{\ell}
\]

is an integer in \(\{1,\ldots,N-1\}\). Moreover,

\[
(\ell q)z_\ell=q(w+NA_\ell)\equiv qw\equiv1\pmod N.
\]

Hence \(z_\ell\) is the canonical inverse of \(\ell q\), and

\[
P_N(\ell q)=q(w+NA_\ell).
\]

The congruence defining the digit gives

\[
A_\ell=0\iff \ell\mid w.
\]

Finally, two different digits give different values because \(qN>0\):

\[
q(w+NA)-q(w+NA')=qN(A-A').
\]

This proves Theorem 1.

## 2. One anchor forces the large row

Fix the prime \(r>B\) with odd \(v_r(q)\). Since \(q\) is a unit modulo
\(N\), we have \(r\nmid N\).

Partition the eligible primes by their carry digit. The product of all
eligible primes with digit zero divides \(w\), so it is less than \(N\).
For a fixed nonzero digit \(A\), the product of all eligible primes with
that digit divides

\[
H_A=w+NA<NB.
\]

Assume that no nonzero digit has even \(r\)-adic valuation. Then every
nonzero digit that occurs satisfies \(r\mid H_A\). If \(A\) and \(A'\)
both occur, then

\[
r\mid H_A-H_{A'}=N(A-A').
\]

Because \(r\nmid N\), this gives \(A\equiv A'\pmod r\). But
\(0<A,A'<B<r\), so \(A=A'\). Thus all nonzero anchors lie in one digit
bucket. It follows that

\[
G_B(N,q)<N\cdot NB=N^2B,

\]

which contradicts the hypothesis. Hence some eligible anchor has nonzero
digit and even \(v_r(H_A)\).

For this anchor, \(A\ne0\) gives

\[
P_N(\ell q)=q(w+NA)>qw=P_N(q).
\]

Also,

\[
v_r(P_N(\ell q))=v_r(q)+v_r(H_A)\equiv1\pmod2.
\]

This argument uses only valuation parity. It includes valuations
\(0,2,4,\ldots\). This proves Theorem 2.

## 3. Deduplication leaves at least two odd-row values

There are two cases.

### Case A: \(v_r(w)\) is even

Then the unary value \(qw\) has odd \(r\)-adic valuation. Theorem 2 gives
a second odd-row value with a nonzero digit. It differs from \(qw\).

### Case B: \(v_r(w)\) is odd

Now \(r\mid w\). For every nonzero digit \(0<A<B<r\),

\[
w+NA\not\equiv0\pmod r,
\]

because \(r\nmid N\). Thus every nonzero digit has valuation zero, which
is even.

There must be at least two distinct nonzero digits. Otherwise the zero
bucket has product less than \(N\), and the only possible nonzero bucket
has product less than \(NB\). This again gives

\[
G_B(N,q)<N^2B,
\]

which is impossible. The two nonzero digits give two different exact
values, and both values have odd \(r\)-adic valuation after multiplication
by \(q\).

In both cases, two distinct exact values exist. If either value occurred
in the old ledger, its first copy is already present and has the same
integer valuation. Global first-occurrence deduplication cannot remove a
distinct exact value from the set. This proves Theorem 3, including its
independence from the old ledger.

## 4. Uniform cutoff and the constant \(n^2/4\)

### 4.1 Elementary primorial bound

Write

\[
\Pi(m)=\prod_{p\le m}p,
\qquad
\Lambda(m)=\operatorname{lcm}(1,\ldots,m).
\]

The elementary binomial-coefficient identity

\[
\operatorname{lcm}_{0\le j\le m-1}\binom{m-1}{j}
=\frac{\Lambda(m)}m
\]

follows prime by prime from the valuations of the binomial coefficients.
Since the largest term is at least the average term,

\[
\Lambda(m)
\ge m\max_j\binom{m-1}{j}
\ge\sum_j\binom{m-1}{j}
=2^{m-1}.
\]

Only primes at most \(\sqrt m\) can occur above the first power in
\(\Lambda(m)\). There are at most \(\sqrt m\) such primes, and the extra
power for each one is at most \(m\). Hence

\[
\Lambda(m)\le \Pi(m)m^{\sqrt m},
\]

and therefore

\[
\boxed{\log_2\Pi(m)\ge m-1-\sqrt m\log_2m.}
\tag{8}
\]

Set \(m=n^3\). For \(n\ge64\), \(\log_2n\le\sqrt n\), so

\[
\log_2\Pi(n^3)
\ge n^3-1-3n^{3/2}\log_2n
\ge n^3-1-3n^2
>4n.
\]

The definition \(n=\lceil\log_2(N+1)\rceil\) gives \(N<2^n\). Thus

\[
\Pi(n^3)>N^4.
\tag{9}
\]

### 4.2 Remove the excluded primes

Let \(B=n^3\), and let

\[
D=\prod_{\substack{\ell\le B\text{ prime}\\ \ell\mid Nq}}\ell.
\]

The squarefree number \(D\) divides \(Nq\), so \(D\le Nq<N^2/B\).
Using (9),

\[
G_B(N,q)=\frac{\Pi(B)}D
>\frac{\Pi(B)B}{N^2}
>N^2B.
\]

This proves Theorem 4 without the prime number theorem.

### 4.3 Count the good carry digits

Fix \(r>B\) as in Corollary 4A. Let \(d\) be the number of distinct
nonzero digits \(A\) for which \(v_r(w+NA)\) is even.

As before, the zero-digit bucket has product less than \(N\). All
nonzero digits with odd valuation form at most one bucket, because
\(r>B\). Each of the \(d\) even-valuation digit buckets has product less
than \(NB\). Therefore

\[
G_B(N,q)<N(NB)^{d+1}.
\tag{10}
\]

Suppose \(d\le n^2/4\). From (10), \(B=n^3\), and \(N<2^n\),

\[
\log_2G_B
<\frac{n^3}{4}+2n
 +\frac{3n^2}{4}\log_2n+3\log_2n.
\tag{11}
\]

On the other hand, (8) and \(D<N^2/B\) give

\[
\log_2G_B
>n^3-1-3n^{3/2}\log_2n+3\log_2n-2n.
\tag{12}
\]

The lower bound minus the upper bound is

\[
\frac34n^3
-3n^{3/2}\log_2n
-\frac34n^2\log_2n
-4n-1.
\tag{13}
\]

For \(n\ge64\), \(\log_2n\le n/8\) and \(\sqrt n\ge8\). Hence (13) is
at least

\[
\frac{21}{32}n^3-\frac38n^{5/2}-4n-1
\ge\frac{39}{64}n^3-4n-1>0.
\]

This contradicts (11)--(12). Therefore

\[
d>\frac{n^2}{4}.
\]

Different digits give different exact values. If a direct sign screen has
not already returned a factor, the full scan retains all these distinct
values, subject only to keeping their earlier copy. This proves
Corollary 4A with the stated strict constant.

## 5. Conditional quasipolynomial composition

Let \(S_t\) be the number of accumulated endpoint presentations before
round \(t\). Every endpoint is less than \(N\). If \(K_t\) is the number
of nontrivial pairwise-coprime blocks after complete refinement, then the
product of the distinct blocks divides the product of the endpoints.
Consequently,

\[
K_t<nS_t.
\tag{14}
\]

One frozen round tests at most \(E K_t\) pairs and adds at most two
endpoint presentations per pair. Thus

\[
S_{t+1}\le(1+2nE)S_t.
\tag{15}
\]

The conditional starting transcript has the declared
\(2^{O((\log n)^4)}\) size bound. Since

\[
T=L^2,
\qquad
\log_2E=L^2,
\]

(15) gives

\[
\log_2S_T
\le O((\log n)^4)
+L^2\,O(\log n+L^2)
=O((\log n)^4).
\]

All canonical endpoints have \(O(n)\) bits, and every exact value is less
than \(N^2\). Modular inverses, gcd operations, batch gcd-free refinement,
and the final binary linear algebra take polynomial work in the accumulated
transcript size and its bit length. Thus the full conditional cost is

\[
2^{O((\log n)^4)}.
\]

Adding the old unary menu changes the candidate factor by at most another
factor of \(E\). Testing all \((a,e)\in[1,E]^2\) changes it to \(E^2\).
Both changes add only \(O(L^2)\) to the logarithm per round, so the same
bound holds.

For \(n\ge64\), \(L^2\ge3\log_2n\), so \(E\ge n^3\). Also
\(L^2<n-1\), so \(E<N-1\) on the allowed input range. The scan therefore
contains all prime anchors at most \(n^3\). If \(q<N/n^3\), their products
are unreduced, and Theorem 4 applies exactly.

If \(q<N/E\), the same excluded-prime argument gives

\[
G_E(N,q)>\frac{\Pi(E)E}{N^2}.
\]

Since \(E\ge n^3\), (9) implies \(\Pi(E)>N^4\), and hence
\(G_E(N,q)>N^2E\). Thus Theorems 2--3 also apply with \(B=E\) and
\(r>E\).

This proves the conditional claims in Theorem 5.

## 6. Hostile scope check

The result proves row reuse only. Its proof does not cover:

1. a selected block \(q\ge N/n^3\), because \(\ell q\) can reduce modulo
   \(N\);
2. odd rows at primes at most \(n^3\);
3. primes that occur to even order in the selected block; or
4. later degree-one peeling cascades.

The result also does not turn row degree two into a kernel. New columns can
share the row \(r\) and still have separate private rows. Even a binary
kernel can map only to the global roots \(\pm1\). Therefore the statement
does not claim, and the reconstruction does not derive, a factoring
algorithm.

## 7. Independent arithmetic checks

I exhaustively checked the exact carry formula for

```text
5 <= N < 300, 2 <= B < 16,
1 < q < N/B, gcd(q,N)=1,
all eligible prime anchors ell <= B.
```

Every canonical endpoint, inverse identity, exact-value identity, and
zero-digit equivalence passed. I also evaluated the two numerical margins
for every integer \(64\le n<100000\). Both were positive. At \(n=64\),
the margin in (13) was exactly

```text
168703
```

under the displayed real-valued bound.
