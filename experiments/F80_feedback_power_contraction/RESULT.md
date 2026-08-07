# F80 — power contraction is a real escape from the old-coset ceiling and gives a second complete \(N=4033\) feedback chain

**Status:** proof-only candidate. No research computation was run. This is an
exact order-divisibility theorem and a fixed feedback witness. It is not an
all-input smoothness theorem or a factoring algorithm for arbitrary inputs.

## 1. Closest prior result and material difference

P84 proves that every distribution uniform inside cosets of a large
separator-free old subgroup \(H\) has sparse direct-sign success, even after
subgroup expansion. P81 escapes by a targeted support-two canonical word on
the fixed post-P78 state.

Powering is a different operation. It maps a subgroup \(K\) to the generally
smaller image \(K^M\). This image need not contain the old \(H\), so its law
need not be uniform inside old \(H\)-cosets. The operation is the familiar
order-contraction mechanism behind Pollard \(p-1\), now applied to a block
that did not exist before feedback refinement.

## 2. Exact power-pushforward law

Let \(K\) be any finite subgroup of
\((\mathbb Z/N\mathbb Z)^\times\), and let \(M\ge1\). Define

\[
K^M=\{x^M:x\in K\}.
\]

### Theorem 1

If \(X\) is uniform on \(K\), then \(X^M\) is uniform on \(K^M\).

### Proof

The power map

\[
\pi_M:K\longrightarrow K^M,
\qquad
x\longmapsto x^M
\]

is a surjective homomorphism. Every fibre is a coset of
\(\ker\pi_M\) and therefore has the same size. Uniform input pushes forward
to uniform output. \(\square\)

For \(N=pq\), P83's exact density formula can therefore be applied to
\(K^M\), not to \(K\). In particular,

\[
\delta_+(K^M)
=
\frac1{|K_p^M|}
+\frac1{|K_q^M|}
-\frac2{|K^M|}.
\tag{1}
\]

This explains the escape from P84: powering can contract the old synchronized
subgroup to \(H^M\), rather than preserve uniformity inside the original
\(H\)-cosets.

## 3. Exact one-base order gate

Let \(u\) be a unit modulo \(N=pq\), and let

\[
r_p=\operatorname{ord}_p(u),
\qquad
r_q=\operatorname{ord}_q(u).
\]

Then

\[
\boxed{
1<\gcd(u^M-1,N)<N
\iff
\bigl(r_p\mid M\bigr)\mathbin{\mathrm{xor}}\bigl(r_q\mid M\bigr).
}
\tag{2}
\]

This follows because \(u^M=1\) in a field component exactly when the local
order divides \(M\).

Let

\[
M_B=\operatorname{lcm}(1,2,\ldots,B).
\]

For \(B=\operatorname{poly}(\log N)\), the integer \(M_B\) has polynomial
bit length: the elementary product bound gives

\[
M_B\le B!,
\qquad
\log_2M_B=O(B\log B).
\]

It is computable by repeated gcd/lcm operations, and modular exponentiation
by \(M_B\) has polynomial bit complexity. Thus (2) gives a deterministic
polynomial-time factor from a declared block \(u\) whenever exactly one of
its two local orders divides \(M_B\).

This is a conditional state theorem. It gives no all-input reason for such a
block or bound \(B\) to occur.

## 4. A complete feedback-to-power witness at \(N=4033\)

Use the verifier-backed P78 history

\[
N=4033=37\cdot109.
\]

Before feedback, the block subgroup is

\[
H_0=\langle2\rangle,
\]

and \(2\) has exact order \(36\) modulo both hidden primes. Hence every old
subgroup power has synchronized \(+1\) and \(-1\) status. In particular,
raising any old element to a multiple of \(36\) gives the global identity.

The P78 cross-relation feedback step uses \(g=2^{11}=2048\), appends its
canonical inverse \(3905\), and splits the old block \(1985\) through

\[
\gcd(1985,3905)=5.
\]

Thus the public refined block list contains the new block \(u=5\). The
immediate sign screens of \(5\) are trivial.

Now take the standard smooth exponent

\[
M=M_9=\operatorname{lcm}(1,\ldots,9)=2520=36\cdot70.
\]

Modulo \(37\), P78 gives \(5=2^{23}\), and the order of \(2\) is \(36\).
Therefore

\[
5^M\equiv1\pmod{37}.
\tag{3}
\]

Modulo \(109\), exact repeated squaring gives

\[
5^4\equiv80,\qquad
5^8\equiv78,\qquad
5^{16}\equiv89,\qquad
5^{32}\equiv73,
\]

and hence

\[
5^{36}\equiv73\cdot80\equiv63\pmod{109}.
\tag{4}
\]

Moreover,

\[
63^2\equiv45,
\qquad
63^3\equiv1\pmod{109}.
\]

Since \(70\equiv1\pmod3\), equations (4) and \(M=36\cdot70\) give

\[
5^M\equiv63\ne1\pmod{109}.
\tag{5}
\]

The unique CRT residue satisfying (3) and (5) is \(3442\), because

\[
3442=1+37\cdot93
\qquad\text{and}\qquad
3442=63+109\cdot31.
\]

Therefore the completely factor-free final operation returns

\[
\boxed{
\gcd(5^{2520}-1,4033)
=\gcd(3441,4033)
=37.
}
\tag{6}
\]

Before the feedback split, every \(h\in H_0\) satisfies \(h^{2520}=1\)
globally because \(36\mid2520\). Thus the newly exposed integer block is
essential for this exact power-contraction channel.

This gives a second complete fixed chain:

\[
\text{cross-relation feedback}
\to
\text{integer block split exposing }5
\to
\text{smooth power contraction}
\to
\text{proper gcd}.
\]

It is algorithmically different from P81's support-two cancellation word.

## 5. Exact remaining gap

The fixed witness shows that P84's old-coset ceiling does not close feedback.
A newly exposed block can have different local order divisibility even when
all old blocks were synchronized.

The all-input theorem would have to prove that polynomial feedback work
produces, with inverse-polynomial probability, a public block \(u\) and a
polynomial-bit exponent \(M\) such that exactly one local order divides
\(M\). A smooth ladder is only one possible exponent source.

No such law is known. Ordinary Pollard \(p-1\) has the same smooth-order
limitation, and feedback has not yet been proved to manufacture the required
local smoothness mismatch. Fixed predeclared exponent catalogues also face
the abstract F79 candidate boundary; adaptive numerical exponents remain
outside it.

Thus power contraction is a genuine live feedback operation and an exact
fixed success, but it does not yet give a classical polynomial-time
factoring algorithm.
