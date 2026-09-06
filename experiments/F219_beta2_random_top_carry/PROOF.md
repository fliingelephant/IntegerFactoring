# F219 proof

## 1. Primary annihilator certificates

Write the hidden prime-power decomposition as

\[
N=\prod_j R_j,\qquad R_j=r_j^{f_j}.
\]

Let \(o_j\) be the order of \(a\) modulo \(R_j\). The global identity
\(a^A=1\pmod N\) gives \(o_j\mid A\) for every \(j\). Fix
\(\ell^e\parallel A\).

If \(G_{a,A,\ell}=1\), then

\[
a^{A/\ell}\ne1\pmod {R_j}
\]

for every \(j\). If \(v_\ell(o_j)<e\), then \(o_j\mid A/\ell\), a
contradiction. Therefore

\[
v_\ell(o_j)=e
\tag{1}
\]

for every hidden component.

The kernel of

\[
(\mathbb Z/r_j^{f_j}\mathbb Z)^\times
\longrightarrow\mathbb F_{r_j}^\times
\]

is an \(r_j\)-group. Since \(\ell\ne r_j\), reduction preserves the
complete \(\ell\)-primary order. Equation (1) gives

\[
\ell^e\mid\operatorname{ord}_{r_j}(a)\mid r_j-1.
\tag{2}
\]

This proves the certificate. Taking a least common multiple preserves (2),
and the universal factor two can be inserted because every hidden rational
prime is odd. The witnesses need not share a base, annihilator, or whole
exact order.

## 2. Generalized CRT and uniform refinement

The known reciprocal prefix determines

\[
p\equiv u_s^{-1}\pmod {2^s}.
\]

Together with \(p\equiv1\pmod M\), generalized CRT gives one class modulo

\[
L_s=\operatorname{lcm}(M,2^s).
\]

Consistency is automatic for the true prefix. If \(t\ge s\), reduction of
classes modulo \(L_t\) to classes modulo \(L_s\) has constant fibre size

\[
[L_t:L_s]=L_t/L_s.
\]

Exactly one member of that fibre is the true class of \(p\). This proves
the exact probability \(L_s/L_t\).

If \(L_s<N^{1/4}\), increasing \(t\) multiplies \(L_t\) by either one or
two. At the first \(t\ge s\) with \(L_t\ge N^{1/4}\), it follows that
\(L_t<2N^{1/4}\). If \(L_s\ge N^{1/4}\), take \(t=s\). Each sampled class
is processed for the fixed bounded runtime of the known-residue algorithm.
A returned candidate is accepted
only after an integer gcd or exact division verifies a proper divisor.
Wrong classes therefore cannot cause an incorrect output. Independent
sampling eventually chooses the true class almost surely. If
\(\tau_{\rm true}\) is the first trial on which it is chosen, then

\[
\Pr(\tau_{\rm true}>k)=(1-L_s/L_t)^k,
\qquad
\mathbb E\tau_{\rm true}=L_t/L_s.
\tag{3}
\]

If \(\tau_{\rm factor}\) is the first trial returning any verified factor,
then \(\tau_{\rm factor}\le\tau_{\rm true}\). Equality need not hold:
a wrong class can fortuitously make the terminal expose a factor.

The expected-cost cancellation is algebraic:

\[
\frac{L_t}{L_s}\frac{N^{1/4}}{L_t}
=\frac{N^{1/4}}{L_s}.
\tag{4}
\]

Ceilings add at most \(L_t/L_s\), which is the same order when
\(L_t=\Theta(N^{1/4})\). Polynomial logarithmic factors are unchanged.
Thus uniform random refinement cannot improve the exponent supplied by the
already known modulus through the guaranteed true-class event alone. This
calculation is an upper bound on the actual accepted-factor runtime, not a
lower bound excluding useful off-class factor events.

## 3. The top-multiplier identity

Balance gives

\[
p\le B<q<2p.
\tag{5}
\]

Write \(B=p+s\), where \(0\le s<p\). Modulo \(q\), (5) and the ordinary
negative-binomial congruence give

\[
(-1)^B\binom{rN-1}{B}
\equiv(-1)^B\binom{-1}{B}=1\pmod q.
\tag{6}
\]

Modulo \(p\), Lucas's theorem uses the two low base-\(p\) digits:

\[
\binom{rpq-1}{p+s}
\equiv
\binom{p-1}{s}\binom{rq-1}{1}
\equiv(-1)^s(rq-1)\pmod p.
\]

Since \((-1)^{p+s}=-(-1)^s\),

\[
A_r\equiv1-rq\pmod p.
\tag{7}
\]

The right side is also one modulo \(q\). Equations (6)--(7) and CRT give

\[
A_r\equiv1-rq\pmod N.
\tag{8}
\]

Hence \(h_r\) is integral. Its defining equality is

\[
A_r-1=N h_r-rq.
\]

Reducing after multiplication by \(N^{-1}\pmod {2^t}\) gives

\[
z_{r,t}\equiv h_r-rqN^{-1}
=h_r-rp^{-1}\pmod {2^t},
\]

which proves the boxed identity.

For odd \(r\), multiplication by \(r^{-1}\) and translation by
\(-z_{r,t}\) are permutations modulo \(2^t\). The same is true after
restricting to the affine coset of prefixes compatible with the certified
CRT class. Thus conditional uniform carry guessing has the same exact hit
probability at every \(r\); averaging over any law \(\rho\) leaves it
unchanged. For a nonuniform law, the correct event is exactly
\(c=h_r\pmod {2^t}\), which gives the displayed atom formula.

To compute \(z_{r,t}\), choose

\[
T\ge\max\{t,\lceil\log_2(rN)\rceil\}.
\]

Then \(0\le B\le rN-1\le2^T-1\), so the same corrected binomial-modulo-
\(2^T\) algorithm used in P173 applies in its stated main range. Reduction
modulo \(2^t\) and multiplication by \(N^{-1}\) are polynomial in \(T\).

## 4. Exact uniform-source probability

For squarefree \(N=pq\), the unit group is the direct product of two cyclic
groups of orders \(p-1\) and \(q-1\). Its \(A\)-torsion subgroup has exact
size \(d_pd_q\). A uniform unit lands in it with probability

\[
\frac{d_pd_q}{(p-1)(q-1)}.
\tag{9}
\]

Conditioned on this event, the two local components are independent and
uniform in cyclic groups of sizes \(d_p,d_q\). If
\(v_\ell(d_p)=v_\ell(d_q)=e\), each local \(\ell\)-primary coordinate is
uniform in a cyclic group of order \(\ell^e\). The fraction whose order has
full \(\ell\)-adic valuation \(e\) is

\[
1-\frac1\ell.
\]

Both local coordinates have full valuation with conditional probability
\((1-1/\ell)^2\). This is exactly the event
\(G_{a,A,\ell}=1\). If either local torsion group has smaller
\(\ell\)-valuation, the event is impossible. Multiplying by (9) proves the
probability law.

For \(A=N-1\), reduction modulo \(p-1\) gives

\[
N-1=pq-1\equiv q-1\pmod {p-1},
\]

and hence

\[
d_p=\gcd(p-1,q-1)=d_q=d.
\tag{10}
\]

Every primary certificate, from this or any unrelated annihilator, divides
both \(p-1\) and \(q-1\). Therefore their lcm divides \(d\). On the
infinite P165 bounded-gap family, \(d\mid q-p=O(1)\), so \(M=O(1)\).

Finally,

\[
L_s=\operatorname{lcm}(M,2^s)\le M2^s=O(2^s).
\]

The QP terminal condition \(N^{1/4}/L_s=\operatorname{QP}(n)\) forces

\[
s\ge\frac14\log_2N-(\log n)^{O(1)}.
\]

Thus accumulated ordinary primary certificates do not remove the P175
quarter-prefix gate on this family.
