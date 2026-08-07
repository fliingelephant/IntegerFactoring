# F80 hostile audit — feedback power contraction

## Verdict: PASS

I audited
`experiments/F80_feedback_power_contraction/RESULT.md` at SHA-256

```text
e5b205098b837a37616df563b82cd3f65dc953129bdb213797d97e122af771bf
```

The hash matches the requested artifact. This was a proof-only audit. I ran
no research computation.

The power-pushforward theorem, the exact local-order gate, the polynomial
cost bound, and every displayed arithmetic identity in the \(N=4033\)
witness are correct. The final modular exponentiation and gcd use only public
data. The factorization of \(4033\) and the local orders are used to prove
success, not to execute the step.

The novelty claim has one essential limit. The integer \(5\) can be tried as
an ordinary public Pollard-style base even without feedback. The witness
proves that \(5\) is new and necessary relative to the declared old
block-generated subgroup and the fixed \(M=2520\) channel. It does not prove
that feedback is necessary to factor this fixed integer. The candidate's
phrases “this exact power-contraction channel” and “familiar ... Pollard
\(p-1\)” preserve that limit.

## 1. Uniform power pushforward

The ambient unit group is abelian. Hence for every subgroup \(K\) and
integer \(M\geq1\), the map

\[
\pi_M:K\longrightarrow K,\qquad x\longmapsto x^M
\]

is a homomorphism. Its image is exactly \(K^M\), and every nonempty fibre is
a coset of \(\ker\pi_M\). All fibres have equal size. Therefore uniform
\(X\in K\) pushes forward to exact uniform law on \(K^M\).

For \(N=pq\), projection commutes with powering:

\[
(K^M)_p=K_p^M,\qquad (K^M)_q=K_q^M.
\]

Applying the positive-separator formula to the subgroup \(K^M\) gives

\[
\delta_+(K^M)
=\frac1{|K_p^M|}
+\frac1{|K_q^M|}
-\frac2{|K^M|}.
\]

No independence of the two CRT projections is assumed. The formula counts
the two projection kernels and subtracts the global identity twice.

A uniform law on \(K\geq H\) is uniform within old \(H\)-cosets. Its powered
image is uniform on \(K^M\), which need not contain \(H\). Thus the powered
law need not be \(H\)-invariant. This genuinely leaves the hypothesis of the
old-coset ceiling; it does not guarantee that the new image contains a
separator.

## 2. Exact local-order XOR gate

For a unit \(u\), field-group order gives

\[
u^M\equiv1\pmod p
\iff \operatorname{ord}_p(u)\mid M,
\]

and the same statement at \(q\). Since \(N=pq\) is squarefree,
\(\gcd(u^M-1,N)\) is:

- \(1\) when neither local order divides \(M\);
- \(N\) when both local orders divide \(M\); and
- one of \(p,q\) when exactly one divides \(M\).

This proves the displayed XOR equivalence exactly. The orders are analysis
variables. The executable gcd does not compute them.

## 3. Cost of the smooth exponent

For

\[
M_B=\operatorname{lcm}(1,\ldots,B),
\]

the elementary bound \(M_B\leq B!\) gives

\[
\log_2M_B\leq\log_2(B!)=O(B\log B).
\]

If \(B\) is polynomial in \(n=\lceil\log_2N\rceil\), both \(B\) and the bit
length of \(M_B\) are polynomial in \(n\). Repeated updates

\[
m\leftarrow \frac{m\,j}{\gcd(m,j)}
\]

for \(1\leq j\leq B\) use a polynomial number of gcd and integer operations
on polynomial-bit integers. Binary modular exponentiation uses
\(O(\log M_B)\) modular squarings and multiplications. The claimed
deterministic polynomial bit complexity is correct.

The condition is still a smooth-order condition. An order divides \(M_B\)
only when all of its prime-power divisors fit inside the lcm. F80 proves no
reason that feedback must produce a one-sided instance of this condition.

## 4. Re-audit of the old synchronized subgroup

The factorization is

\[
4033=37\cdot109.
\]

Modulo \(37\),

\[
2^{12}\equiv26,\qquad
2^{18}\equiv-1.
\]

Modulo \(109\),

\[
2^{12}=4096\equiv63,\qquad
2^{18}\equiv-1.
\]

In each field, \(2^{36}=1\). Every proper divisor of \(36\) divides either
\(12\) or \(18\), so the two displayed nonidentity checks prove exact order
\(36\) in both components.

It follows that

\[
H_0=\langle2\rangle
\]

is synchronized by the common exponent modulo \(36\). For every \(h=2^t\)
and every power \(e\), \(h^e=1\) either in both local components or in
neither, and \(h^e=-1\) either in both or in neither. In particular,
\(36\mid2520\) implies

\[
h^{2520}=1\pmod{4033}
\qquad\text{for every }h\in H_0.
\]

Therefore no base from the declared old subgroup can give a proper direct
sign gcd through this exponent.

## 5. Re-audit of the feedback split

The canonical inverse claim is exact:

\[
2048\cdot3905
=7{,}997{,}440
=1+1983\cdot4033.
\]

The split gcd is

\[
\gcd(1985,3905)=5,
\]

because \(1985=5\cdot397\), \(3905=5\cdot781\), and
\(\gcd(397,781)=1\). Thus \(5\) is a public descendant block obtained by
ordinary integer gcd, without either hidden prime.

Its immediate signs do not factor:

\[
\gcd(5-1,4033)=1,\qquad
\gcd(5+1,4033)=1.
\]

The exponent arithmetic is also exact:

\[
M_9=\operatorname{lcm}(1,\ldots,9)
=2^3\,3^2\,5\,7
=2520
=36\cdot70.
\]

## 6. Re-audit modulo \(37\)

Modulo \(37\), \(2^5=32=-5\) and \(2^{18}=-1\), so

\[
2^{23}=(-1)(-5)=5.
\]

Since \(36\mid2520\),

\[
5^{2520}=2^{23\cdot2520}\equiv1\pmod{37}.
\]

Equivalently, \(5\) has order \(36/\gcd(36,23)=36\) modulo \(37\), which
divides \(2520\).

## 7. Re-audit modulo \(109\)

Direct reductions give

\[
\begin{aligned}
5^4&=625\equiv80,\\
5^8&\equiv80^2=6400\equiv78,\\
5^{16}&\equiv78^2=6084\equiv89,\\
5^{32}&\equiv89^2=7921\equiv73
\end{aligned}
\qquad(\bmod 109).
\]

Therefore

\[
5^{36}\equiv73\cdot80=5840\equiv63\pmod{109}.
\]

The remaining claims are

\[
63^2=3969\equiv45,\qquad
63^3\equiv45\cdot63=2835\equiv1\pmod{109}.
\]

Since \(63\neq1\), it has exact order three. As \(70\equiv1\pmod3\),

\[
5^{2520}=(5^{36})^{70}
\equiv63^{70}
\equiv63
\not\equiv1\pmod{109}.
\]

Thus exactly one local order divides \(2520\), as required by the XOR gate.

## 8. CRT residue and final gcd

The proposed canonical residue satisfies both congruences:

\[
3442-1=3441=37\cdot93,
\]

and

\[
3442-63=3379=109\cdot31.
\]

CRT uniqueness modulo \(4033\) therefore gives

\[
5^{2520}\equiv3442\pmod{4033}.
\]

Finally,

\[
\gcd(3441,4033)
=\gcd(37\cdot93,37\cdot109)
=37.
\]

An implementation performs only

\[
x=\operatorname{powmod}(5,2520,4033),
\qquad \gcd(x-1,4033).
\]

It does not use \(37\), \(109\), either local order, or CRT. Those quantities
are only the proof certificate.

## 9. Essentiality and exact scope

The witness proves the following state-relative statement:

- every declared old block lies in \(H_0\);
- every old-subgroup base raised to \(2520\) becomes the global identity;
- feedback exposes the descendant block \(5\); and
- that block raised to \(2520\) has a one-sided identity component.

Thus a newly exposed block is essential for success within this declared
old-block, fixed-exponent channel.

It does not prove that the integer \(5\) was unavailable to every public
algorithm before feedback. In fact, an ordinary algorithm can try the small
base \(5\) directly and obtain the same gcd. Nor does it prove that no other
public base or factoring method works on \(4033\). The fixed chain is a
mechanism witness, not an advantage or necessity theorem for feedback.

The general theorem is the classical Pollard-style order-divisibility gate
applied to a feedback-generated state. F80 does not claim a new smoothness
law, an inverse-polynomial density of suitable blocks, a universal exponent
selector, or an all-input factoring algorithm. It explicitly leaves those
as the missing theorem. The historical references to P78, P81, P83, P84,
and F79 are not needed for the algebra audited here and were not independently
re-audited.
