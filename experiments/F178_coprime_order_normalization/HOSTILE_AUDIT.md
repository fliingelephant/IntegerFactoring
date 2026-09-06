# F178 hostile audit

## Frozen inputs

- `STATEMENT.md`:
  `8a7cfbc7ea7d3fd2d0df3c31bbd540b9c3ae7a7b62dde2997b143135e5ae6ca4`
- `PROOF.md`:
  `4500b8583e57d00c089c4870694e72c666aa7a72f0d0d0e388030783ec049f49`

Both hashes matched before review.

## Verdict

**PASS.** I found no false conclusion, missing branch, prime-power defect,
or super-QP operation. The postprocessor proves only its stated
trichotomy. The last branch can still have unequal local orders and is not
a factoring algorithm.

## Hostile checks

### P159/F176 V3 interface

In the P159 hard branch, the order of
\(2\langle-1\rangle\) in every hidden component exceeds \(C\). If
\(q=\operatorname{ord}_{R_j}(2)\), then both

\[
\operatorname{ord}_{R_j}(4)=\frac{q}{\gcd(q,2)}
\]

and the order of \(2\langle-1\rangle\) equal the same quantity. Thus the
imported hypothesis \(e_j=\operatorname{ord}_{R_j}(4)>C\) is exact. The
new cap \(T\ge\max\{n,2C\}\) remains QP for every fixed P159 cap choice.

### Removal exponent and arbitrary prime powers

For every rational prime \(r\mid N\),

\[
e_j<R_j\le N<2^n
\quad\Longrightarrow\quad
v_r(e_j)<n,
\]

whereas \(v_r(N^n)=n v_r(N)\ge n\). Hence \(N^n\) removes the full
\(r\)-primary part of every local order, including an \(r\)-part arising
in a different hidden component. Therefore

\[
f_j=\frac{e_j}{\gcd(e_j,N^n)},
\qquad \gcd(f_j,N)=1.
\]

This also closes the partial-prime-power trap in the identity and lcm
screens. The kernel of
\((\mathbb Z/p^a\mathbb Z)^\times\to(\mathbb Z/p\mathbb Z)^\times\)
is a \(p\)-group. A subgroup of order \(f_j\), with \(p\nmid f_j\),
meets that kernel trivially. Thus a tested power of \(y\) is one modulo
\(p\) exactly when it is one modulo \(p^a\). In particular, the proof's
terse statement that \(H\) is a product of full hidden components is
valid; it does not assume that \(N\) is squarefree.

### The identity-global branch

If \(H=N\), then \(f_p=1\) for the component above the least rational
prime \(p\mid N\). Put \(d=\operatorname{ord}_p(4)\). Then
\(d\mid e_p\mid N^n\), while every prime divisor of \(d\) is less than
\(p\) and every prime divisor of \(N^n\) is at least \(p\). Hence
\(d=1\), so \(p\mid3\) and \(p=3\). Since \(N\) is composite,
\(\gcd(3,N)=3\) is public and proper, including when \(N\) is a pure
power of three. On the surviving \(H=1\) branch, every \(f_j>1\).

### The lcm screen and factor-first stripping

The equivalence

\[
r\mid\Lambda_T
\quad\Longleftrightarrow\quad
\sigma(r)\le T
\]

is exact. Therefore \(J=1\) proves \(\sigma(f_j)>T\) in every hidden
component.

If \(J=N\), all local orders divide the known factored multiple
\(\Lambda_T\). During stripping, a global gcd permits deletion of one
prime factor from the current exponent. A proper gcd is already a factor.
A gcd of one says that no local order divides the reduced exponent. On a
no-factor run, the last test for every prime \(\ell\) forces every local
order to have the full surviving \(\ell\)-adic valuation. Hence all local
orders equal the final exponent \(m\). Its factorization is inherited from
\(\Lambda_T\). Also \(m=f_j\) gives \(\gcd(m,N)=1\), so \((y,m)\) is a
valid factored exact common-order state when \(m>n\).

### The \(m\le n\) factor exit

Let \(p\) again be the least prime divisor of \(N\), and set
\(d=\operatorname{ord}_p(4)\). Prime-power lifting gives

\[
e_p=d p^u,\qquad 0\le u<a.
\]

All prime divisors of \(d\) are below \(p\), so none divides \(N\).
The exponent \(N^n\) removes exactly the \(p^u\) part of \(e_p\), and
therefore \(f_p=d=m\). This proves \(p\mid4^m-1\), so
\(D=\gcd(4^m-1,N)>1\). If \(D=N\), every original order \(e_j\) divides
\(m\), contrary to

\[
e_j>C\ge n\ge m.
\]

Thus \(D\) is proper. This argument allows \(D\) to expose only a partial
power of \(p\), which is still a valid factor.

### Sign quotient

For a unit of order \(f\) modulo an odd prime power, its image modulo
\(\langle-1\rangle\) has order \(f/\gcd(f,2)\). An odd prime-power
divisor above \(T\) survives unchanged. If the large primary divisor is
\(2^a>T\), the quotient retains

\[
2^{a-1}>T/2\ge C.
\]

Therefore every final sign-quotient order is strictly above \(C\). The
factor two loss is fully covered by the condition \(T\ge2C\).

### QP cost and recursion

The public exponent \(N^n\) has \(O(n^2)\) bits. A sieve through the
fixed numerical QP bound \(T\) constructs

\[
\Lambda_T=\prod_{\ell\le T}
\ell^{\lfloor\log_\ell T\rfloor}
\]

and its complete factorization in QP time and space. The loose bound
\(\log_2\Lambda_T=O(T\log T)\) makes every modular exponent and stripping
call QP. There are at most \(O(\log\Lambda_T)\) successful deletions and
terminal prime tests. The remaining gcds and the \(m\le n\) power have no
larger cost.

Every factor is verified and can be passed back to the P159 recursion. A
complete factor tree has fewer than \(2n\) nodes, including repeated prime
factors, so this adds only a polynomial factor.

## Scope and computation

The audit used the promoted P159 text and the frozen F176 V3 statement and
proof. No mathematical computation was needed or run. No candidate byte or
durable ledger was changed.
