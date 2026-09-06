# F168 blind reconstruction — QP decoder rescaling and a length-linked stable core

## Scope and verdict

I verified before reading that `STATEMENT.md` has SHA-256

```text
a30c71c6bf8d6b715b84e4abb78cc5c47681e1c7f95971e85e610606176dade0
```

This reconstruction uses only that statement, the promoted statements P87 and
P92--P99 in `PROVED.md`, and standard Bertrand and Linnik theorems. I did not
read an F168 proof, audit, self-audit, or manifest. I did not run a research
computation.

**Verdict: PASS.** Parts I--III are valid QP rescalings. Part IV has a direct
CRT--Linnik construction with the required length link. The phrase “under
every fixed QP cap” in IV.3 has its usual asymptotic meaning: for each fixed QP
cap, the claimed failure holds after deletion of a finite prefix of the
family.

Throughout, put

\[
n=\lceil\log_2(N+1)\rceil.
\]

## 1. Elementary closure facts for QP bounds

Write \(u=\log_2(n+1)\). A finite collection of bounds of the form
\(2^{C_i u^{k_i}}\) has a common upper bound \(2^{C u^k}\), for fixed
\(C,k\). Sums, products, fixed powers, and multiplication by polynomial or
polylogarithmic factors preserve this form. In particular, a polynomial
number of bit operations on QP-bit integers, repeated a QP number of times,
still costs QP time. All uses below involve a fixed number of such closures,
so this observation does not hide an unbounded composition.

## 2. Part I: QP closure lemma

Let \(B\) be bounded by a fixed QP function.

### 2.1 The lcm and its bank

Construct the lcm iteratively by

\[
m_1=1,\qquad m_i=\operatorname{lcm}(m_{i-1},i).
\]

Every intermediate integer divides \(B!\), and hence has bit length at most

\[
\log_2(B!)\le B\log_2 B.
\]

This length is QP in \(n\). There are \(B\) gcd, division, and multiplication
steps, each on QP-bit operands. Even elementary deterministic integer
arithmetic therefore gives QP total bit complexity.

There is at most one bank entry for each prime power \(\ell^j\le B\), in
addition to \(M_B\). Thus the complete punctured bank has at most \(B+1\)
entries. Exact division of \(M_B\) by every such prime power has QP total bit
cost and QP total output length.

### 2.2 Prime scans

A deterministic sieve through \(B\) uses \(B\,\operatorname{polylog} B\)
elementary work. Even the much cruder method that deterministically tests
each candidate using trial divisors through its square root has only a fixed
power of \(B\) operations. Either bound is QP. The same applies to a scan
through any other public QP cap.

### 2.3 Modular powers and supplied generators

Every bank exponent has bit length at most \(B\log_2 B\). Binary modular
exponentiation modulo the \(n\)-bit integer \(N\) uses a number of modular
multiplications polynomial in that exponent length and in \(n\). The bank
size, the generator count, and the total generator encoding length are QP,
so powering every generator by every bank exponent remains QP. Reading the
input itself also remains within the assumed total encoding bound.

### 2.4 Capped subgroup enumeration

Let the numerical enumeration cap be \(U\), and let the supplied list have
\(d\) generators, with both \(U,d\) QP. Breadth-first search can stop upon
finding the \((U+1)\)-st distinct residue. Before that point it forms at most
\(Ud\) candidate products. A deliberately crude implementation can compare
each candidate with every stored residue, so it uses at most a fixed
polynomial in \(U,d,n\) equality and multiplication work. It can gcd-test
each candidate or each newly visited residue with \(N\) at the same cost
scale. Thus no hash-table or unit-cost arithmetic assumption is needed.

The numerical value of \(M_B\) is exponentially larger than its bit length,
but no step loops to that numerical value. This proves all deterministic
claims in Part I.

### 2.5 Verified repetition

Suppose a trial has worst-case work \(W(n)\), succeeds on each promised input
with probability at least \(1/R(n)\), and reports only a verified answer or
failure, where \(W,R\) are QP. Independent trials have expected stopping time
at most \(R\). The expected bit cost is therefore at most \(WR\), which is
QP. Verification prevents an incorrect output, and the probability of never
succeeding is zero. This is a Las Vegas algorithm.

The “work on every transcript” premise matters: it prevents a bad unpromised
transcript from hanging. Exact rejection sampling of an interval has
unbounded worst-case random-tape length, but it has constant expected work and
an exponentially decreasing tail. P97 and P99 use that separate expected-cost
fact; they do not require pretending that rejection sampling is transcript-
bounded.

## 3. Part II: the eight rescaled corollaries

The promoted results supply the arithmetic correctness. It remains to check
that replacing their polynomial numerical bounds by fixed QP bounds does not
introduce a bit-cost leak.

### 3.1 P87

Take \(B=\lceil Q(n)\rceil\). For completeness, the bank logic can be seen
directly. If, say, \(\sigma(r_p)\le B\), then \(r_p\mid M_B\). If
\(r_q\nmid M_B\), the unpunctured exponent separates the two orders. If both
orders divide \(M_B\) but are unequal, choose a prime at which their
valuations differ. If those valuations are \(a<b\) and
\(e=v_\ell(M_B)\), use the puncture \(M_B/\ell^{e-a}\). Its
\(\ell\)-valuation is \(a\), so that bank exponent is divisible by exactly
one local order. Conversely, if a divisor of \(M_B\) is divisible by one
local order, every full prime-power component of that order is at most
\(B\). P87's gcd criterion then proves the exact promise.

The bank construction and all modular powers and gcds are QP by Part I.

### 3.2 P92

With \(B=\lceil Q(n)\rceil\), P92 supplies a bank exponent whose image has

\[
|K^E|\le B^2.
\]

The square of a QP bound is QP. Powering a QP-encoded generator list and
enumerating the image through this cap are QP by Part I. The image contains
the separators asserted by P92, so deterministic enumeration finds one.

### 3.3 P93

Again take \(B=\lceil Q(n)\rceil\). P93 gives, for some bank exponent,

\[
|K^E|\le B^2
\]

and guarantees that this image contains a separator. Complete bank scanning
and capped enumeration therefore have deterministic QP bit complexity and
find a factor.

### 3.4 P94

There are at most \(L(n)\) prime candidates. For each prime divisor
\(\ell\mid N-1\), there are at most
\(v_\ell(N-1)\le n\) public puncture depths. Thus there are at most
\(L(n)n\) powered images to inspect. If the displayed P94 promise holds, the
useful image has exact size

\[
\ell^{H_\ell-C_\ell+2}\le S(n).
\]

Part I therefore gives deterministic QP scan, powering, enumeration, and gcd
cost.

### 3.5 P95: complete enumeration

The public power \(N-1\) has only \(O(n)\) bits. P95 gives
\(S=K_p^{N-1}\times K_q^{N-1}\) and \(|S|=AB\). When
\(1<AB\le T(n)\), the powered supplied list generates an image within the QP
cap. Complete enumeration visits a positive separator and is deterministic
QP.

### 3.6 P95: near-uniform sampling

The probability bound survives rescaling, but it is useful to make the
sampling cost explicit. Let \(m=\min(A,B)\). P95's separator density is

\[
\delta=\frac1A+\frac1B-\frac2{AB}.
\]

If \(m=1\), then \(AB>1\) gives \(\delta\ge1/2\). If \(m\ge2\), ordering
the two factors as \(m\le M\) gives

\[
\delta=\frac1m+\frac{m-2}{mM}\ge\frac1m.
\]

Hence \(m\le Q(n)\) always implies \(\delta\ge1/(2Q(n))\).

There is also a simple order-oblivious near-uniform sampler. Let
\(h_1,\ldots,h_d\) be the powered public generators and choose independent
uniform integers \(e_i\in\{0,\ldots,R-1\}\), where

\[
R\ge 8dNQ(n).
\]

For the unknown order \(o_i=\operatorname{ord}(h_i)<N\), reduction of
\(e_i\) modulo \(o_i\) is within total-variation distance at most
\(o_i/R<N/R\) of uniform. Replacing the coordinates one at a time shows that
the joint exponent vector is within \(dN/R\le1/(8Q)\) of the product of the
uniform cyclic-coordinate distributions. The multiplication map from those
cyclic coordinates onto \(S\) is a surjective homomorphism, so its uniform
input pushes forward to exact uniform measure on \(S\). Total variation
cannot increase under this map. The sampled group element consequently has
separator probability at least

\[
\frac1{2Q}-\frac1{8Q}=\frac3{8Q}.
\]

The bit length of \(R\) is
\(O(n+\log d+\log Q)\). Drawing the exponents, powering, multiplying, and
gcd-testing therefore costs QP. Exact interval rejection for the exponents
has constant expected overhead. Verified repetition is expected QP.

### 3.7 P96

The public annihilator tests use QP-many modular powers. The scan has at most
\(L(n)n\) prime/depth pairs. Under the displayed promise, P96 gives a useful
powered image of size at most

\[
\ell^{2(H-C+1)}\le T(n).
\]

Part I then gives deterministic QP enumeration and gcd cost.

### 3.8 P97

Sampling an exact uniform integer from \(1,\ldots,N-1\) by rejection has
expected polynomial bit cost: use
\(\lceil\log_2(N-1)\rceil\) random bits, whose acceptance probability is
greater than one half. A nonunit gives a verified factor. Otherwise, two
accepted units give the P97 powered pair. Conditional on the unit branch,
that pair generates the full rectangle with probability at least
\(6/\pi^2\).

Let a localizer have worst-case QP work on every list and success probability
at least \(1/R(n)\) on every list that generates the rectangle, for a fixed
QP bound \(R\). One fresh batch therefore has verified success probability at
least

\[
\frac6{\pi^2R(n)},
\]

apart from the additional possibility of an immediate gcd factor. The source
has expected polynomial cost, the localizer costs QP even on nongenerating
lists, and independent batches therefore have expected QP total cost. This
proves the claimed Las Vegas splitter without recognizing the generation
event.

### 3.9 P99 and complete factorization

P99's batch source remains polynomial. Let \(X\) be the event that the batch
already exposes a proper gcd, and let \(Y\) be the event that it exposes no
factor and its list generates the full unit group. P99 gives

\[
\Pr(X)+\Pr(Y)\ge c_0>0.
\]

If a localizer succeeds with probability at least \(1/R(n)\) on every
full-group generating list and has QP worst-case work on every list, a batch
succeeds with probability

\[
\Pr(X)+\frac{\Pr(Y)}{R(n)}
\ge \frac{c_0}{R(n)}.
\]

The exact interval samplers have polynomial expected cost; all other batch
work is QP. Fresh verified batches thus give an expected-QP splitter for
every composite.

To obtain complete factorization, first use a deterministic polynomial-time
primality test. On a composite \(m\), call the splitter, verify
\(1<d<m\) and \(d\mid m\), and recurse on \(d\) and \(m/d\). A binary split
tree for \(N\) has at most \(\log_2N<n\) leaves, counted with multiplicity,
because every leaf is at least two and their product is \(N\). It therefore
has fewer than \(n\) internal splitter calls. Every subproblem has bit length
at most \(n\), so each conditional expected cost is bounded by the same
monotone QP function of \(n\). Linearity of conditional expectation bounds
the total expected splitting work by \(n\) times that QP bound, still QP.
The primality tests and output verification add only polynomial work. This
also covers repeated prime factors; it does not assume a squarefree recursive
input.

## 4. Part III: the bare-\(N\) promise class

For a unit \(a\), P97 says that \(a^{N-1}\) is exactly uniform in
\(C_A\times C_B\), and the gcd with \(a^{N-1}-1\) succeeds precisely on the
two nonidentity coordinate axes. Its conditional success density is the
same \(\delta\) analyzed above. Thus

\[
\min(A,B)\le Q(n)\quad\Longrightarrow\quad
\delta\ge\frac1{2Q(n)}.
\]

For distinct odd primes,

\[
\frac{\varphi(N)}{N-1}=\frac{(p-1)(q-1)}{pq-1}>\frac12,
\]

because the equivalent inequality is
\((p-2)(q-2)>1\). Hence one exact uniform sample has factor probability
greater than \(1/(4Q(n))\) on the displayed promise class, counting only the
unit-powered branch; a nonunit can only improve it. Modular exponentiation
and the two gcds are polynomial per accepted sample, exact interval sampling
has constant expected overhead, and verified repetition has expected QP bit
complexity. No step tests whether the hidden promise holds.

## 5. Part IV: a length-linked stable family

Use the following standard form of Linnik's theorem: there are absolute
constants \(C_0\ge1\) and \(L\ge1\) such that the least prime in any reduced
residue class modulo \(m\) is at most \(C_0m^L\).

### 5.1 Construction

Choose an arbitrarily large odd prime \(r\). The class

\[
p\equiv 2r+1\pmod{4r}
\]

is reduced, because \(2r+1\) is odd and is one modulo \(r\). Linnik gives a
prime \(p\) in this class with

\[
p\le C_0(4r)^L.
\]

Put \(A=(p-1)/2\). The congruence gives

\[
A=r(2u+1)
\]

for some \(u\ge0\). Thus \(A\) is odd, \(r\mid A\), and \(A\ge r\).

By Bertrand's theorem, choose a prime \(s\) with

\[
A<s<2A.
\]

Then \(s\) is odd and \(\gcd(A,s)=1\). Apply the generalized CRT to

\[
q\equiv-1\pmod{2A},\qquad
q\equiv 1\pmod{2s},\qquad
q\equiv 3\pmod4.
\]

The residues agree modulo every pairwise common divisor, which is two. They
therefore define one class modulo

\[
m=\operatorname{lcm}(2A,2s,4)=4As.
\]

This class is reduced modulo \(m\): it is odd, is \(-1\) modulo every prime
dividing \(A\), and is \(1\) modulo \(s\). Linnik supplies a prime \(q\) in
the class with

\[
q\le C_0(4As)^L.
\]

Put \(B=(q-1)/2\). The three congruences give

\[
B\equiv-1\pmod A,\qquad s\mid B,\qquad B\text{ odd}.
\]

Consequently \(\gcd(A,B)=1\). Also \(q\equiv1\pmod{2s}\) and \(q>1\), so
\(q\ge2s+1>2A+1=p\). Thus \(N=pq\) is a distinct odd semiprime with
\(p<q\), and

\[
\gcd(p-1,q-1)=2\gcd(A,B)=2.
\]

Since \(A,B\) are odd and coprime,

\[
N-1=(2A+1)(2B+1)-1=2(2AB+A+B).
\]

Reduction modulo \(A\) and \(B\) gives

\[
\gcd(A,N-1)=\gcd(A,2B)=1,
\qquad
\gcd(B,N-1)=\gcd(B,2A)=1.
\]

It follows that

\[
\boxed{\gcd(AB,N-1)=1}.
\]

### 5.2 Linking \(r,s\) to input length

Set \(C_1=C_0 4^L\). The first Linnik bound gives

\[
p\le C_1r^L.
\]

Because \(A<p/2\) and \(s<2A<p\), the second one gives

\[
q\le C_0(4As)^L<C_0(2p^2)^L
\le C_2r^{2L^2}

\]

for an absolute constant \(C_2\). Hence, with

\[
D=L+2L^2,
\]

there is an absolute \(C_3\) such that

\[
N=pq\le C_3r^D.
\]

Since \(n=\lceil\log_2(N+1)\rceil\), one has
\(\log_2N>n-2\). Therefore

\[
\log_2r\ge\frac{n-2-\log_2C_3}{D}.
\]

After discarding finitely many choices, this is at least \(n/(2D)\). With

\[
c=\frac1{2D}>0,
\]

we obtain

\[
r\ge2^{cn},\qquad s>r\ge2^{cn}.
\]

There are infinitely many resulting semiprimes. Indeed, a fixed \(p\) can
arise from only finitely many choices of \(r\), since each such \(r\) divides
\((p-1)/2\). Thus infinitely many input primes \(r\) yield infinitely many
distinct \(p\) after passage to a subsequence, and unique factorization plus
\(p<q\) gives infinitely many distinct \(N\).

### 5.3 Stable-core consequences

Let \(E=N-1\), and let \(S\cong C_A\times C_B\) be the P97 rectangle.

1. Since \(\gcd(AB,E)=1\), the \(E\)-power map is an automorphism of
   \(S\), so \(S^E=S\). P98 gives \(S^E\le K^E\le S\) for every retained
   feedback supergroup \(S\le K\le G\). Hence \(K^E=S\): the core is stable
   after the first normalization, which is the claimed immediate P98
   stability.

2. If every prime divisor of an exponent \(t\) divides \(E\), then
   \(\gcd(t,AB)=1\). The \(t\)-power map is therefore an automorphism on both
   cyclic coordinates and on their product. In particular, a coordinate is
   the identity before powering if and only if it is the identity after
   powering.

3. Since \(r\mid A\) and \(s\mid B\), the complete \(r\)- and \(s\)-primary
   components show

   \[
   \sigma(A)\ge r\ge2^{cn},\qquad
   \sigma(B)\ge s\ge2^{cn}.
   \]

   For every fixed QP cap
   \(Q(n)=2^{C(\log_2(n+1))^k}\), one has
   \(Q(n)<2^{cn}\) for all sufficiently large \(n\). Thus both full powered
   local orders eventually violate every such bounded-component promise.

4. P97 gives the exact direct-uniform separator density

   \[
   \delta_N=\frac1A+\frac1B-\frac2{AB}.
   \]

   The construction gives \(A\ge r\ge2^{cn}\) and
   \(B\ge s\ge2^{cn}\), so

   \[
   0<\delta_N\le\frac1A+\frac1B\le2^{1-cn}=2^{-\Omega(n)}.
   \]

   If \(T(n)\) is any fixed QP repetition bound, the union bound gives

   \[
   \Pr(\text{success in at most }T(n)\text{ direct samples})
   \le T(n)\delta_N=2^{-\Omega(n)}.
   \]

   Thus QP repetition of direct uniform rectangle sampling does not give a
   constant- or inverse-QP-success decoder on this family. This argument says
   nothing about adaptive value-dependent operations, integer presentations,
   relations, or unrelated factoring algorithms.

All four parts of the candidate follow.
