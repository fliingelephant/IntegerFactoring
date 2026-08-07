# PASS

The SHA-256 digest of `STATEMENT.md` is

```text
cc94c7ce5b923dec32d0e7526f8301b9b898ca914d6a02f59694677d7991826f
```

It matches the required digest. The proof below uses only that statement.

## 1. The large-prime collision bound

Write

\[
\mathcal U_N=\{u\in\{1,\ldots,N-1\}:\gcd(u,N)=1\}.
\]

This set has size \(\varphi(N)\). Fix a prime \(\ell\). The number of
members of \(\mathcal U_N\) divisible by \(\ell\) is at most the number of
multiples of \(\ell\) in \(1,\ldots,N-1\), namely

\[
\#\{u\in\mathcal U_N:\ell\mid u\}
 \le \left\lfloor\frac{N-1}{\ell}\right\rfloor
 \le \frac N\ell.
\]

Consequently, for every \(i\), marginal uniformity gives

\[
\Pr(\ell\mid U_i)\le \frac{N}{\ell\varphi(N)}.
\]

Canonical inversion is a bijection of \(\mathcal U_N\). Thus \(V_i\) has
the same uniform marginal law, even if the samples are mutually dependent,
and

\[
\Pr(\ell\mid V_i)\le \frac{N}{\ell\varphi(N)}.
\]

Since \(\ell\) is prime and \(A_i=U_iV_i\),

\[
\Pr(\ell\mid A_i)
 \le \Pr(\ell\mid U_i)+\Pr(\ell\mid V_i)
 \le \frac{2N}{\ell\varphi(N)}.
\]

A prime divides \(P=\prod_i A_i\) only if it divides some \(A_i\). A
second union bound therefore gives

\[
\Pr(\ell\mid P)\le \frac{2mN}{\ell\varphi(N)}. \tag{1}
\]

No step multiplied probabilities. Hence no independence assumption was
used.

Let \(q=\lceil\log_2(R+1)\rceil\), and let \(S_r\) be the deterministic set
of distinct primes \(\ell>B\) dividing \(C_r\). The definitions of \(n\)
and \(q\) imply

\[
N\le 2^n-1,
\qquad
R\le 2^q-1,
\qquad
C_r\le 1+RN<2^{n+q}.
\]

The product of the distinct primes in \(S_r\) divides \(C_r\), and each
such prime is at least \(2\). Hence

\[
2^{|S_r|}\le C_r,
\qquad
|S_r|\le \log_2 C_r<L.
\]

In particular, \(|S_r|\le L\). Also, \(\gcd(N,C_r)=1\), so every prime in
\(S_r\) is external to \(N\).

Now \(\ell\mid D_r\) is equivalent to \(\ell\mid P\) and
\(\ell\mid C_r\). The sets \(S_r\) are fixed before sampling. Applying the
union bound over \(r\), then over \(S_r\), and using (1), gives

\[
\begin{aligned}
\Pr\!\left(\exists r\le R,\ \exists\ell>B:\ell\mid D_r\right)
&\le \sum_{r=1}^R\sum_{\ell\in S_r}\Pr(\ell\mid P)\\
&\le \sum_{r=1}^R\sum_{\ell\in S_r}
       \frac{2mN}{\ell\varphi(N)}\\
&\le \frac{2mRN L}{B\varphi(N)}.
\end{aligned}
\]

This proves Claim 1.

## 2. The totient ratio on the continuation branch

Let \(p\) be the least prime divisor of the composite continuation input.
Then \(p>B\ge3\), so \(p\ge5\). The following elementary lemma avoids any
need to assume that the numerical trial bound \(B\) is integral.

**Lemma.** If \(M\) is composite and its least prime divisor is
\(p\ge5\), then

\[
\log\frac{M}{\varphi(M)}
 \le \frac{\log M}{p\log(p+1)}. \tag{2}
\]

Here and in the lemma proof, `log` is the natural logarithm.

**Proof.** Put \(g(x)=\log(x/(x-1))\). For every distinct prime
\(s>p\),

\[
g(s)\le\frac1{s-1}
 \le \frac{\log s}{p\log(p+1)}. \tag{3}
\]

It remains to pay for the contribution of the least prime \(p\). If
\(p^2\mid M\), then \(p+1\le p^{3/2}\) and \(p\ge5\) give

\[
g(p)\le\frac1{p-1}
 \le\frac{2\log p}{p\log(p+1)}. \tag{4}
\]

Thus two of the copies of \(\log p\) in \(\log M\) pay for \(g(p)\).

Suppose instead that \(p\) has exponent one. Since \(M\) is composite,
there is a distinct prime divisor \(s>p\), and therefore \(s\ge p+2\).
The function \(g(s)\) decreases while \(\log s\) increases, so it is
enough to establish

\[
g(p)+g(p+2)
 \le \frac{\log p+\log(p+2)}{p\log(p+1)}. \tag{5}
\]

For \(x>1\), the logarithmic series gives

\[
g(x)\le \frac1x+\frac1{2x(x-1)}.
\]

For \(p\ge5\), direct rearrangement gives

\[
\frac1{2p(p-1)}+\frac1{2(p+2)(p+1)}
 \le \frac3{2p(p+2)}.
\]

Therefore the left side of (5) is at most

\[
\frac2p-\frac1{2p(p+2)}. \tag{6}
\]

Also, \(\log(1-x)\ge-x/(1-x)\) for \(0<x<1\). Applying this with
\(x=(p+1)^{-2}\) yields

\[
\begin{aligned}
\frac{\log p+\log(p+2)}{p\log(p+1)}
&\ge \frac2p-
 \frac1{p^2(p+2)\log(p+1)}\\
&\ge \frac2p-\frac1{2p(p+2)}.
\end{aligned}
\]

This proves (5). Group \(p\) with one such \(s\), use (3) for every other
distinct prime, and use any remaining prime-power copies only on the right.
The identity

\[
\log\frac{M}{\varphi(M)}
=\sum_{t\mid M,\ t\ {m prime}}g(t)
\]

then proves (2). \(\square\)

Apply the lemma to \(M=N\). Since \(N<2^n\), since \(p>B\), and since
\(x\mapsto x\log(x+1)\) increases for positive \(x\),

\[
\log\frac N{\varphi(N)}
 \le \frac{\log N}{p\log(p+1)}
 \le \frac{n\log 2}{B\log(B+1)}
 =\frac{n}{B\log_2(B+1)}.
\]

Exponentiation proves the first displayed inequality in Claim 2. Moreover,
\(B\ge n\) and \(\log_2(B+1)\ge1\), so

\[
\frac{n}{B\log_2(B+1)}\le1.
\]

Thus the exponential is at most \(e\).

This argument uses distinct prime divisors in the totient formula and their
multiplicities only through \(\log N\). It therefore covers nonsquarefree
composites. For a prime power, the \(p^2\mid N\) case above applies. Inputs
with a prime divisor at most \(B\), including such prime powers, stop in the
prepass and do not reach the claimed branch.

Substitution in Claim 1 gives

\[
\Pr\!\left(\exists r\le R,\ \exists\ell>B:\ell\mid D_r\right)
 \le \frac{2mRL}{B}\frac N{\varphi(N)}
 \le \frac{2e\,mRL}{B}.
\]

## 3. Adaptive selection of the target

Let \(T\) be any target selected after the samples and any prior transcript,
subject only to \(T\in\{1,\ldots,R\}\). Pointwise, for every outcome,

\[
\{\exists\ell>B:\ell\mid D_T\}
\subseteq
\{\exists r\le R,\ \exists\ell>B:\ell\mid D_r\}.
\]

The right side is the predeclared union already bounded above. This
containment is valid even when \(T\) is a randomized function of the complete
sample vector. Thus adaptation of the final target adds no probability cost.
It does not require conditional uniformity after revealing the transcript.

## 4. Polynomial parameters

Let \(d=a+b+c+3\), so \(B=n^d\). The exponent \(d\) is fixed. Deterministic
primality testing is polynomial in \(n\). Enumerating all integers, or all
primes, through \(B\) and trial-dividing the \(n\)-bit integer \(N\) takes
polynomial time in \(n\), because \(B\) itself is a fixed power of \(n\).
The chosen \(B\) also exceeds \(\max(3,n)\) for the present range \(n\ge2\).

Since \(R\le n^b\),

\[
L=n+\lceil\log_2(R+1)\rceil+1=O(n).
\]

Consequently,

\[
\frac{2e\,mRL}{B}
 =O\!\left(
 \frac{n^a n^b n}{n^{a+b+c+3}}
 \right)
 =O(n^{-c-2})
 =O(n^{-c-1}).
\]

This is the probability that any \(D_r\), over the complete declared range,
has a prime divisor larger than \(B\).

## 5. The complementary event and the smooth prepass

On the complementary event, no prime larger than \(B\) divides any \(D_r\).
Therefore every \(D_r\) is \(B\)-smooth. Also,

\[
D_r\mid C_r=1+rN,
\]

so \(D_r\) has \(O(n+\log R)=O(n)\) bits in the polynomial regime. One can
compute it without expanding \(P\): multiply the \(A_i\) modulo \(C_r\),
then take the gcd with \(C_r\). There are polynomially many samples, and
each \(A_i<N^2\), so this is polynomial work.

Trial-divide \(D_r\) by every prime at most \(B\), repeatedly for each prime.
On the complementary event the residual is \(1\), so this gives the complete
prime factorization. There are at most \(B=n^d\) trial divisors and at most
\(O(n)\) successful divisions per \(r\). With \(R\le n^b\), the total work
is polynomial in \(n\).

The same trial list gives, before any selection step, the exact decomposition

\[
C_r=S_rQ_r,
\qquad
S_r=\prod_{p\le B}p^{v_p(C_r)},
\]

where \(Q_r\) has no prime divisor at most \(B\). Thus \(S_r\) is the full
\(B\)-smooth part of \(C_r\), not only its squarefree support. On the
complementary event, \(D_r\mid S_r\).

For any retained integer endpoint block, use the same prime list to divide
out every occurrence of each prime appearing in the relevant \(S_r\), while
recording the removed powers. If a block is retained for several targets,
use the union of their prime supports. This operation is polynomial per
polynomial-size represented block and loses no information because the
removed powers are recorded. No unspecified structure of an endpoint block
is needed for this stripping operation.

## Scope

The proof uses \(D_r\mid C_r\); it never asserts \(D_r\le r\). It also does
not say that a smooth \(D_r\) is useless or that no factor-bearing product
exists. It only bounds hard common prime divisors larger than the enlarged
polynomial trial threshold. The remaining smooth factors can still form a
large pool whose useful subset is difficult to select.

The counting proof requires every \(U_i\) to have the stated uniform
marginal law. It does not apply to adaptive canonical-residue states or
block-feedback seed states when those marginals become nonuniform. Finally,
none of the arguments supplies a selection method or a factoring algorithm
for \(N\).
