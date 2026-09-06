# F180 V2 hostile re-audit

## Frozen inputs

- `V2_STATEMENT.md`:
  `8bf8e7ca10a0d58f8548bd88605d015b87fa62f41208e542075cf83951aa6a3c`
- reused `PROOF.md`:
  `ef703570255ba10a68e034ba1d0434648f1411b2ef61f8a2bd3f0287a4117dd4`

Both hashes matched before review. The preserved V1 blind reconstruction was
also read. No frozen file or durable ledger was altered.

## Verdict

**PASS.** Defining

\[
n=\lceil\log_2(N+1)\rceil
\]

repairs the only defect found by the V1 blind reconstruction. It supplies
both missing size facts: every primary exponent in a local order satisfies
\(a<n\), and \(N+3\) has \(O(n)\) bits. I found no remaining error involving
arbitrary hidden prime powers, partial gcds, resultant multiplicities,
exact-order stripping, or QP cost.

F180 V2 proves only the stated factor/common-order/primary-period-hard
trichotomy. It does not eliminate the final hard branch and does not prove
QP integer factoring.

## Repair of the V1 failure

The new definition gives

\[
N+1\le 2^n,
\qquad
N<2^n.
\]

For a hidden prime-power component \(R_j\), its local order satisfies

\[
f_j\le\varphi(R_j)<R_j\le N.
\]

Therefore, for every \(\ell^a\parallel f_j\),

\[
2^a\le \ell^a\le f_j<N<2^n,
\]

so \(a<n\). This is the strict inequality used by the reused proof. It
rules out the partial-deletion counterexample in the V1 blind report.

Also, \(N+3<2^{n+1}\) for the present odd-composite inputs. Hence
\(\log_2(N+3)=O(n)\). The shifted powers in \(A_3\) consequently have the
bit sizes claimed in the complexity analysis.

## Exact primary filtering

Fix \(\ell^a\parallel f_j\). For any exponent \(E\),

\[
v_\ell\!\left(\operatorname{ord}_{R_j}(y^E)\right)
=\max\{a-v_\ell(E),0\}.
\]

With \(E=A_\delta^n\), either \(\ell\nmid A_\delta\), in which case the
full \(\ell^a\) part survives, or \(\ell\mid A_\delta\), in which case

\[
v_\ell(E)=n v_\ell(A_\delta)\ge n>a
\]

and the full part vanishes. No partial primary power can remain.

If \(\ell\mid N+\delta\), every factor
\(((N+\delta)^k-1)\) is \(-1\pmod\ell\), so \(\ell\nmid A_\delta\). If
\(\ell\nmid N+\delta\), then \(\ell\mid A_\delta\) exactly when
\(\operatorname{ord}_\ell(N+\delta)\le K\). This proves equations (6) and
(7), including the nonunit alternative. For \(\delta=0\),
\(\gcd(f_j,N)=1\) excludes that alternative and proves equation (8).

## Arbitrary hidden prime powers and gcd endpoints

Let \(R_j=p^b\). Every filtered local order divides \(f_j\), so it is
coprime to \(p\). If a filtered power is one modulo \(p\), its order modulo
\(p^b\) lies in the \(p\)-group kernel of reduction

\[
(\mathbb Z/p^b\mathbb Z)^\times
\longrightarrow
(\mathbb Z/p\mathbb Z)^\times.
\]

That order is both a power of \(p\) and coprime to \(p\), so it is one.
Thus each gcd \(H_\delta\) contains either all of \(R_j\) or none of it.
The endpoint interpretations \(H_\delta=1\) and \(H_\delta=N\) are exact
for repeated prime factors. Any intermediate gcd would in any event be a
proper factor, so a hypothetical partial prime-power gcd would not create a
missing algorithmic branch.

## Double extinction and resultant multiplicities

Assume \(H_0=H_3=N\). Then for every component,

\[
f_j\mid A_0^n,
\qquad
f_j\mid A_3^n.
\]

For each \(\ell^a\parallel f_j\), some \(k,l\le K\) satisfy

\[
N^k-1\equiv0\pmod\ell,
\qquad
(N+3)^l-1\equiv0\pmod\ell.
\]

Evaluation of the integral resultant Bezout identity at \(X=N\) gives
\(\ell\mid R_{k,l}\). Different primes and hidden components may select
different pairs, but the full product over all \((k,l)\) contains each
required prime at least once. Raising that product to the \(n\)-th power
supplies multiplicity at least \(n>a\). Hence \(f_j\mid M\) for every
hidden component.

The resultants cannot vanish. A common complex root \(u\) would have
\(|u|=|u+3|=1\), while \(|u+3|\ge3-|u|=2\). The root-product formula gives

\[
\log_2 R_{k,l}<k(2l+1),
\]

so the integers used as trial-division inputs have the asserted size.

## Exact-order stripping

The completely factored \(M\) is a common annihilator. Maintain an integer
\(m\) divisible by every \(f_j\). For each prime \(q\mid m\), test

\[
g=\gcd(y^{m/q}-1,N).
\]

- If \(g=N\), every \(f_j\mid m/q\), so deleting that copy of \(q\)
  preserves the invariant.
- If \(1<g<N\), the algorithm returns a proper factor.
- If \(g=1\), no local order divides \(m/q\). Since every local order
  divides \(m\), all of them require the current full \(q\)-adic exponent.

Consequently, on a no-factor run, the terminal valuation at every prime is
the valuation of every \(f_j\). Thus

\[
m=f_1=\cdots=f_s.
\]

The factorization of \(m\) is inherited from that of \(M\), and
\(\sigma(f_j)>T\) gives \(m>T\ge n\). This also covers arbitrary hidden
prime powers: a proper gcd already factors, while the endpoint tests have
the componentwise meanings above.

## QP cost

For \(\delta\in\{0,3\}\), the factors in \(A_\delta\) have
\(O(nk)\) bits. Therefore

\[
\log A_\delta=O(nK^2),
\qquad
\log(A_\delta^n)=O(n^2K^2).
\]

There are \(K^2\) resultants, each with \(O(K^2)\) bits. Their total
product has \(O(K^4)\) bits, and \(M\) has \(O(nK^4)\) bits. Exact
resultant computation is polynomial in \(K\). Trial division of all the
resultants costs \(2^{O(K^2)}\). Modular exponentiation, gcds, aggregation
of the known factorizations, and at most \(O(nK^4)\) stripping tests add
only polynomial cost in \(n\) and \(K\).

Because

\[
K=\left\lceil(\log_2(n+1))^c\right\rceil
\]

for fixed \(c\ge1\), the total bit cost is

\[
2^{O(K^2)}=2^{(\log n)^{O(1)}}.
\]

No unfactored exponentially large evaluated value is treated as if its
factorization were public.
