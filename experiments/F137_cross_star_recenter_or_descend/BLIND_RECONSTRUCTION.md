# F137 blind reconstruction — exact pass

## Source discipline

Project files read:

- `STATEMENT.md` only.

Its SHA-256 was

```text
2126e93be2be3abbca52ccb46615d3be8a2319c4dd064d8a5fa7705cd8084098
```

This equals the required hash. I did not read `PROOF`, `MANIFEST`, any audit,
any ledger, or any other project file. The reconstruction below is independent
of those materials.

## Verdict

**Exact pass.** Every stated arithmetic claim follows from the hypotheses. I
found no counterexample. The path bound is only a bound for an uninterrupted
run of large-quotient transitions; it does not bound the branching transcript
or the number of small-quotient interruptions. The statement preserves this
restriction.

## 1. Canonical parent position

Write the canonical inverse as (1\le w<N). From

\[
qw=1+kN
\]

and (q>1), one has

\[
1\le k<q.
\tag{A}
\]

The anchor condition includes \(\gcd(\ell,N)=1\), so exactly one
\(A\in\{0,\ldots,\ell-1\}\) makes \(w+NA\) divisible by \(\ell\). Moreover,

\[
0<H=w+NA<\ell N,
\]

and

\[
\ell q\le Cq<N.
\]

Consequently, both \(\ell q\) and \(H/\ell\) are integers in
\(\{1,\ldots,N-1\}\), and their product is

\[
(\ell q)(H/\ell)=qH.
\]

Also \(\gcd(H,N)=\gcd(w,N)=1\). Hence every divisor \(r\mid H\) is a unit
modulo \(N\), even without using the phrase “unit block” as an extra
hypothesis. Finally,

\[
qH=q(w+NA)=1+(k+Aq)N,
\]

so \(K=k+Aq\) is exact.

## 2. Divisor carry

Since \(H=Sr\), equation (3) gives

\[
(qS)r=1+KN.
\tag{B}
\]

In particular, \(qS\) is coprime to \(N\). Its Euclidean remainder modulo
\(N\) cannot be zero, so the division in (4) has \(1\le t<N\). Reducing (B)
modulo \(N\) gives

\[
tr\equiv1\pmod N.
\]

The representative \(t\in\{1,\ldots,N-1\}\) is therefore exactly
\(\iota_N(r)\).

Let \(rt=1+k_rN\). Multiplication of \(qS=jN+t\) by \(r\) yields

\[
1+KN=jrN+rt=1+(jr+k_r)N,
\]

hence

\[
K=jr+k_r.
\]

Because \(r>1\), the product \(rt\) is not (1). Because \(t<N\), it is
less than \(rN\). Thus

\[
1\le k_r<r.
\]

It follows at once that \(k_r\) is the ordinary remainder \(K\bmod r\).

## 3. Exact recentering and overlap

The division equation itself says

\[
qS=t+jN=H'_j.
\]

Thus the old value is represented in the new coordinates by

\[
V=r(qS)=rH'_j.
\]

For \(b\ne j\), subtract \(H'_j\) from \(H'_b\). Since
\(\gcd(qS,N)=1\),

\[
\begin{aligned}
\gcd(qS,H'_b)
 &=\gcd(qS,(b-j)N)\\
 &=\gcd(qS,b-j)\\
 &\le |b-j|.
\end{aligned}
\tag{C}
\]

This proves the claimed equality, not only its upper bound. It also covers a
negative \(b-j\), since gcd uses absolute divisibility.

## 4. Canonical child positions and the observed-digit branch

For an eligible child anchor \(a\), \(\gcd(a,N)=1\). Therefore exactly one
\(b_a\in\{0,\ldots,a-1\}\) solves

\[
t+b_aN\equiv0\pmod a.
\]

The first child endpoint satisfies

\[
1<ar\le Cr<N.
\]

For the second endpoint,

\[
0<t+b_aN<N+(a-1)N=aN.
\]

It is a positive multiple of \(a\), so

\[
1\le \frac{t+b_aN}{a}<N.
\]

Their product is

\[
(ar)\frac{t+b_aN}{a}=r(t+b_aN)
 =1+(k_r+b_ar)N,
\]

so this is a canonical source position. Also \(b_a<a\le C\), hence every
observed digit is less than \(C\).

Suppose now that \(j<C\). If \(b_a=j\), the child product is

\[
rH'_j=rqS=V.
\]

Thus representation-specific endpoint screens must be applied before a
deduplication operation that retains only one representation of the exact
value. If \(b_a\ne j\), then both digits lie in
\(\{0,\ldots,C-1\}\), so (C) gives

\[
\gcd(qS,H'_{b_a})\le |b_a-j|\le C-1<C.
\]

Any prime common to the old complement and a genuinely different observed
child cofactor is therefore less than \(C\). In particular, a prime larger
than \(C\) cannot reappear there.

The formal digit \(j\) need not be observed: being less than \(C\) does not
imply that some eligible \(a\) has both \(j<a\) and \(a\mid H'_j\).

## 5. One-step descent

Suppose \(j\ge C\). The parent bound from Section 1 gives

\[
H<CN.
\]

If \(r\ge q\), then

\[
qS=\frac{qH}{r}\le H<CN.
\]

But the Euclidean division gives

\[
qS=jN+t\ge CN+1,
\]

a contradiction. Hence \(r<q\). The equality case \(j=C\) is safely in the
descent branch because \(t\ge1\).

## 6. Two-step contraction

For transition \(i\), let \(A_i\) be its parent digit. The divisor-carry
identity gives the exact carry recurrence

\[
k_i+A_iq_i=j_iq_{i+1}+k_{i+1}.
\tag{D}
\]

Canonical carries and anchor digits satisfy

\[
1\le k_i<q_i,
\qquad
0\le A_i\le C-1.
\tag{E}
\]

Use \(j_0\ge C\) in (D). Equations (D) and (E) imply

\[
Cq_1+k_1
 \le j_0q_1+k_1
 =k_0+A_0q_0
 <Cq_0,
\]

and therefore

\[
k_1<C(q_0-q_1).
\tag{F}
\]

At the next transition, \(j_1\ge C\) gives

\[
Cq_2+k_2
 \le k_1+A_1q_1
 \le k_1+(C-1)q_1.
\]

Since \(k_2\ge1\), substitution of (F) yields

\[
Cq_2<Cq_0-q_1,
\qquad
q_2<q_0-\frac{q_1}{C}.
\tag{G}
\]

Each large-quotient transition is also a strict descent, so \(q_2<q_1\).
Put \(\rho=C/(C+1)\). If \(q_1\le\rho q_0\), then
\(q_2<q_1\le\rho q_0\). If \(q_1>\rho q_0\), then (G) gives

\[
q_2<q_0-\frac{q_1}{C}
 <q_0-\frac{q_0}{C+1}
 =\rho q_0.
\]

Thus in all cases

\[
q_2<\frac{C}{C+1}q_0.
\]

## 7. Path length

Let a path contain \(L\) consecutive large-quotient transitions, and put
\(\rho=C/(C+1)\). Repeated application of the two-step result gives

\[
q_{2m}<\rho^m q_0
\qquad (2m\le L).
\]

Every released block is an integer larger than (1), while \(q_0<N\).
Consequently,

\[
\left\lfloor\frac L2\right\rfloor
 <\frac{\log N}{\log(1+1/C)}.
\]

Since \(\log(1+1/C)\ge1/(C+1)\), one explicit coarse bound is

\[
L<2(C+1)\log N+2=O(C\log N).
\]

With \(C=n^3\) and \(n=\lceil\log_2(N+1)\rceil\), this is \(O(n^4)\).
This calculation cannot charge a small-quotient transition, so it gives no
bound when such transitions interrupt every pair.

## 8. Exact certificate

For \(N=143\), \(q=28\), and \(w=46\),

\[
28\cdot46=1288=1+9\cdot143.
\]

Also \(28<143/5\), and all stated anchor coprimality conditions hold.

For \(\ell=3\), the digit equation gives \(A=1\). Then

\[
H=189=27\cdot7,
\quad K=9+28=37,
\quad 28\cdot27=756=5\cdot143+41.
\]

Moreover,

\[
7\cdot41=287=1+2\cdot143,
\quad 37=5\cdot7+2,
\]

so \(j=5=C\), \(t=\iota_{143}(7)=41\), \(k_r=2=37\bmod7\), and
\(7<28\).

For \(\ell=5\), the digit equation gives \(A=3\). Then

\[
H=475=25\cdot19,
\quad K=9+3\cdot28=93,
\quad 28\cdot25=700=4\cdot143+128.
\]

Here

\[
19\cdot128=2432=1+17\cdot143,
\quad 93=4\cdot19+17.
\]

Thus \(j=4<C\), \(t=\iota_{143}(19)=128\), and \(H'_4=700\). Child
anchor \(a=5\) observes \(b_5=4\), and its endpoints are

\[
(5\cdot19,700/5)=(95,140).
\]

Their product is

\[
95\cdot140=13300=1+93\cdot143.
\]

The parent endpoints are \((5\cdot28,475/5)=(140,95)\), so this certificate
recenters the same exact position with the endpoints exchanged. Both endpoint
gcd screens against \(N\) are null:

\[
\gcd(95,143)=\gcd(140,143)=1.
\]

## 9. Refutation attempts

I tested the following possible failure points directly.

- A zero Euclidean remainder is impossible because \((qS)r\equiv1\pmod N\).
- A non-unit cancellation in (C) is impossible because
  \(\gcd(qS,N)=1\).
- The extreme child bounds \(a=C\) and \(r\) arbitrarily close to \(N/C\)
  remain strict because the hypothesis is \(r<N/C\).
- The boundary \(j=C\) cannot leak into the recenter branch and gives the
  strict contradiction \(qS\ge CN+1\) in the descent proof.
- The apparent weak point in two-step contraction is an intermediate
  \(q_1\) near \(Cq_0/(C+1)\). The two complementary bounds
  \(q_2<q_1\) and \(q_2<q_0-q_1/C\) meet exactly there and remain strict.
- A bounded exhaustive search over all valid data with \(3\le N\le200\)
  checked 331,809 one-step releases and 23,203 composable pairs with both
  quotients at least \(C\). It checked the endpoint bounds, inverse and carry
  identities, gcd equality, observed-digit overlap, one-step descent, and
  strict two-step contraction. It found zero counterexamples. This search is
  corroboration only; the proofs above do not depend on it.

## 10. Scope

The result is conditional on a qualifying released divisor at each
transition. It proves only these local alternatives:

1. a small quotient identifies the parent as a virtual child digit and
   excludes overlap by primes larger than \(C\) with every different observed
   child cofactor; or
2. a large quotient strictly decreases the released block, with contraction
   after two consecutive large-quotient transitions.

It does not control primes at most \(C\), the recentered digit itself,
non-parent columns, other stars, the frequency of small-quotient interruptions,
or the total number of branches. It also supplies no even-valuation-parity
argument and no proof that a resulting square root is non-global. Therefore
it is not a closure theorem or an integer-factoring algorithm, exactly as the
statement says.
