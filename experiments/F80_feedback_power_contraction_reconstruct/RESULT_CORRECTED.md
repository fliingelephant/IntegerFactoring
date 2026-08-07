# PASS

The SHA-256 of STATEMENT_CORRECTED.md is
3235f8bab26c75804ae1d9dbda3ed3563e88884a40cce9161b2e99beac017a5b,
as required.

## 1. A uniform source remains uniform on the powered image

The group \((\mathbb Z/N\mathbb Z)^\times\) is abelian. Therefore

\[
\phi_M:K\longrightarrow K,\qquad x\longmapsto x^M
\]

is a group homomorphism, and its image is exactly \(K^M\). For each
\(y\in K^M\), every nonempty fibre \(\phi_M^{-1}(y)\) is a coset of
\(\ker\phi_M\). All fibres consequently have the same size. If \(X\) is
uniform on \(K\), then

\[
\Pr(X^M=y)=\frac{|\ker\phi_M|}{|K|}
=\frac1{|K^M|}.
\]

Thus \(X^M\) is uniform on \(K^M\).

## 2. Projection and the exact density

Let \(\pi_p\) and \(\pi_q\) be the CRT projections. For either projection,

\[
\pi_p(K^M)
=\{\pi_p(x^M):x\in K\}
=\{\pi_p(x)^M:x\in K\}
=K_p^M,
\]

and similarly \(\pi_q(K^M)=K_q^M\).

Put \(J=K^M\). For uniform \(Y\in J\), let

\[
A_p=\{y\in J:\pi_p(y)=1\},\qquad
A_q=\{y\in J:\pi_q(y)=1\}.
\]

The restriction \(J\to J_p=K_p^M\) is surjective, so

\[
\Pr(A_p)=\frac1{|K_p^M|},\qquad
\Pr(A_q)=\frac1{|K_q^M|}.
\]

The intersection \(A_p\cap A_q\) consists only of the identity, by CRT.
Its probability is \(1/|K^M|\). A positive-sign gcd is nontrivial and proper
exactly when one, but not both, of the two local coordinates is \(1\).
Hence its success set is \(A_p\mathbin\triangle A_q\), and

\[
\delta_+(K^M)
=\frac1{|K_p^M|}+\frac1{|K_q^M|}-\frac2{|K^M|}.
\]

## 3. Exact local-order factor gate

For a unit \(u\), the defining property of element order gives

\[
u^M\equiv1\pmod p\iff r_p\mid M,
\qquad
u^M\equiv1\pmod q\iff r_q\mid M.
\]

Because \(N=pq\) with distinct primes, \(\gcd(u^M-1,N)\) is a nontrivial
proper divisor exactly when \(u^M-1\) is divisible by exactly one of \(p,q\).
Therefore

\[
1<\gcd(u^M-1,N)<N
\iff
(r_p\mid M)\mathbin{\mathrm{xor}}(r_q\mid M).
\]

This equivalence is exact. It is not a claim that the xor occurs often.

## 4. Complexity of the smooth exponent

Let \(n\) be the bit length of \(N\). Since \(M_B\mid B!\),

\[
\log_2 M_B\leq\log_2(B!)\leq B\log_2B.
\]

If \(B=\operatorname{poly}(n)\), the bit length of \(M_B\) is polynomial in
\(n\). Construct it deterministically by starting with \(m=1\) and applying

\[
m\leftarrow\operatorname{lcm}(m,k)
=\frac{mk}{\gcd(m,k)}
\qquad (k=1,\ldots,B).
\]

There are \(B=\operatorname{poly}(n)\) iterations. Every intermediate integer
has \(O(B\log B)\) bits. Integer gcd, multiplication, and exact division
therefore give polynomial construction time. Binary modular exponentiation
uses \(O(\log M_B)\) modular squarings and multiplications on \(n\)-bit
residues. It is also deterministic polynomial time. Neither step requires
the factorization of \(N\) or the local orders.

## 5. Verification of the fixed feedback history

First,

\[
37\cdot109=4033.
\]

The number \(37\) has no prime divisor at most \(\sqrt{37}<7\), and \(109\)
has no prime divisor among \(2,3,5,7\), the primes at most
\(\sqrt{109}<11\). Thus they are distinct odd primes.

### Order of \(2\) modulo \(37\)

Directly,

\[
2^9=512\equiv31\equiv-6\pmod{37},
\]

so

\[
2^{18}\equiv36\equiv-1\pmod{37},
\qquad
2^{36}\equiv1\pmod{37}.
\]

Also,

\[
2^6\equiv27\equiv-10\pmod{37},
\qquad
2^{12}\equiv100\equiv26\not\equiv1\pmod{37}.
\]

The order divides \(36\). Every proper divisor of \(36=2^2 3^2\) divides
either \(18\) or \(12\). The two displayed nonidentity checks exclude both
possibilities. Hence

\[
\operatorname{ord}_{37}(2)=36.
\]

### Order of \(2\) modulo \(109\)

Here

\[
2^{12}=4096\equiv63\pmod{109},
\]

and

\[
2^{18}=2^{12}2^6\equiv63\cdot64=4032\equiv-1\pmod{109}.
\]

Thus \(2^{36}\equiv1\pmod{109}\), while \(2^{18}\not\equiv1\) and
\(2^{12}\not\equiv1\). The same proper-divisor argument proves

\[
\operatorname{ord}_{109}(2)=36.
\]

By CRT, the order of \(2\) modulo \(4033\) is
\(\operatorname{lcm}(36,36)=36\).

### The stated refinement values

The power is literal:

\[
2^{11}=2048.
\]

Also \(3905=4033-128\), and

\[
2048\cdot3905
\equiv-2048\cdot128
=-262144
\equiv1\pmod{4033},
\]

because \(4033\cdot65=262145\). Since \(0<3905<4033\), this verifies the
stated canonical inverse.

The Euclidean algorithm gives

\[
\begin{aligned}
3905&=1985+1920,\\
1985&=1920+65,\\
1920&=29\cdot65+35,\\
65&=35+30,\\
35&=30+5,
\end{aligned}
\]

so \(\gcd(1985,3905)=5\). The descendant \(u=5\) is a unit because neither
\(37\) nor \(109\) divides it. Its immediate sign tests are

\[
\gcd(5-1,4033)=\gcd(4,4033)=1,
\qquad
\gcd(5+1,4033)=\gcd(6,4033)=1,
\]

the second equality following also from \(4033=6\cdot672+1\).

## 6. Verification of \(M_9\) and the final factor

The largest prime powers at most \(9\) are \(2^3,3^2,5,7\). Therefore

\[
M_9=2^3\cdot3^2\cdot5\cdot7=2520.
\]

Since \(2520=36\cdot70\), Fermat's theorem modulo \(37\) gives

\[
5^{2520}\equiv1\pmod{37}.
\]

Modulo \(109\),

\[
2520=23\cdot108+36,
\]

so Fermat's theorem reduces the exponent to \(36\). Repeated squaring gives

\[
\begin{aligned}
5^4&\equiv80\pmod{109},\\
5^8&\equiv80^2\equiv78\pmod{109},\\
5^{16}&\equiv78^2\equiv89\pmod{109},\\
5^{32}&\equiv89^2\equiv73\pmod{109},\\
5^{36}&\equiv73\cdot80\equiv63\pmod{109}.
\end{aligned}
\]

Hence

\[
5^{2520}\equiv63\pmod{109}.
\]

The integer \(3442\) satisfies

\[
3442=37\cdot93+1=109\cdot31+63
\]

and lies in \([0,4033)\). CRT therefore proves

\[
5^{2520}\equiv3442\pmod{4033}.
\]

Finally,

\[
3442-1=3441=37\cdot93,
\qquad
4033=37\cdot109,
\]

and \(\gcd(93,109)=1\). Thus

\[
\gcd(5^{2520}-1,4033)
=\gcd(3441,4033)
=37.
\]

The executable step needs only the public triple \((5,2520,4033)\): compute
\(5^{2520}\bmod4033\) by repeated squaring and then compute the gcd with one
less than the residue. The proof uses the hidden factors and orders only to
verify why this public computation succeeds.

## 7. Why the descendant is essential in the stated channel

Every \(h\in H_0=\langle2\rangle\) has the form \(h=2^j\). Since the order of
\(2\) modulo \(4033\) is \(36\) and \(2520=36\cdot70\),

\[
h^{2520}=2^{2520j}=(2^{36})^{70j}\equiv1\pmod{4033}.
\]

Thus the positive-sign gcd from any old-subgroup element is \(4033\), and
the negative-sign gcd is \(\gcd(2,4033)=1\). Neither is a proper factor.
The descendant \(5\), in contrast, yields \(37\). Therefore it is essential
relative to this declared old-subgroup and this fixed exponent channel.

## 8. Exact scope

Powering can contract a subgroup. In this example,

\[
H_0^{2520}=\{1\},
\]

which does not contain the nontrivial group \(H_0\). Uniform measure on
\(H_0\) is invariant under multiplication by \(H_0\), while its powered
image is the point mass at \(1\), which is not. Hence powering can leave an
old-\(H_0\)-invariant distribution class because its image subgroup need not
contain \(H_0\).

This map is explicit and polynomial-time executable. It therefore gives an
exact algorithmic way to escape that old-coset sampling ceiling. The factor
gate also shows why escape is not a success guarantee: if both local orders
divide \(M\), or neither does, the gcd is respectively \(N\) or \(1\), not a
proper factor.

The successful base \(5\) is an ordinary small public base. One could try it
with the same Pollard-style exponent without obtaining it from feedback.
Consequently, this witness does not prove that feedback is necessary to
factor the fixed integer \(4033\).

Finally, the argument gives one exact witness and one conditional gate. It
does not prove that suitable local orders have the required smoothness on all
inputs. It does not give an inverse-polynomial density of feedback blocks
that satisfy the xor gate. It therefore supplies no all-input smoothness law
and no general polynomial-time factoring algorithm.
