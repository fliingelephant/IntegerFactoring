# FAIL

The SHA-256 digest of the reconstruction statement is

~~~text
93df9398feeb558bdfdccfef0ec501a626bd1a624fceaf0deccda7388d2b0080
~~~

It matches the required digest.

Claim 2 is false as written. Projection does commute with powering, but the
displayed density multiplies the two reciprocal projection sizes. The exact
formula adds them. This is the first exact failure. Claims 1, 3, and 4, all
fixed-instance arithmetic, and the requested scope statements are correct.

## 1. Uniformity after powering

The map

\[
\psi_M:K\longrightarrow K,\qquad x\longmapsto x^M
\]

is a homomorphism because \(K\) is abelian. Its image is \(K^M\). For each
\(y\in K^M\), the fiber \(\psi_M^{-1}(y)\) is a coset of
\(\ker\psi_M\), so every nonempty fiber has the same size. Therefore the
pushforward of the uniform law on \(K\) assigns probability

\[
\frac{|\ker\psi_M|}{|K|}
=\frac1{|K^M|}
\]

to each \(y\in K^M\). Claim 1 is true.

## 2. Projection and the failed density formula

Projection does commute with powering:

\[
\pi_p(K^M)
=\{\pi_p(x^M):x\in K\}
=\{\pi_p(x)^M:x\in K\}
=K_p^M,
\]

and similarly for \(q\).

For any subgroup \(J\le G_p\times G_q\), the elements of \(J\) whose
\(p\)-component is \(1\) form \(\ker(\pi_p|_J)\), of size
\(|J|/|J_p|\). After the identity is removed, these give
\(|J|/|J_p|-1\) positive separators. The other projection contributes
\(|J|/|J_q|-1\), and the two nonidentity sets are disjoint. Hence

\[
\delta_+(J)
=\frac1{|J_p|}+\frac1{|J_q|}-\frac2{|J|}.
\]

Taking \(J=K^M\) and using projection commutation gives the correct identity

\[
\boxed{\displaystyle
\delta_+(K^M)
=\frac1{|K_p^M|}+\frac1{|K_q^M|}-\frac2{|K^M|}.}
\]

The statement instead places the first two fractions next to one another,
which denotes multiplication:

\[
\frac1{|K_p^M|}\frac1{|K_q^M|}-\frac2{|K^M|}.
\]

For the valid subgroup \(K=\{1\}\), its powered image and both projections
all have size \(1\). The true density is \(0\), while the displayed
right-hand side is \(1-2=-1\). Thus Claim 2 is false literally; inserting
the missing plus sign makes it true.

## 3. The exact local-order gate

For a unit \(u\), the definition of multiplicative order gives

\[
u^M\equiv1\pmod p\iff r_p\mid M,
\qquad
u^M\equiv1\pmod q\iff r_q\mid M.
\]

Because \(N=pq\) is squarefree, \(\gcd(u^M-1,N)\) is a proper nontrivial
factor exactly when \(u^M-1\) is divisible by exactly one of \(p,q\).
Therefore

\[
1<\gcd(u^M-1,N)<N
\iff
(r_p\mid M)\mathbin{\mathrm{xor}}(r_q\mid M).
\]

Claim 3 is true.

## 4. Size and construction of the smooth exponent

The elementary bound

\[
M_B=\operatorname{lcm}(1,\ldots,B)\le B!
\]

gives

\[
\log_2 M_B\le \log_2(B!)\le B\log_2 B.
\]

If \(B\) is polynomial in \(n=\lceil\log_2 N\rceil\), this bit length is
polynomial in \(n\). Construct \(M_B\) iteratively by

\[
L_1=1,\qquad
L_k=\frac{L_{k-1}k}{\gcd(L_{k-1},k)}
\quad(2\le k\le B).
\]

There are polynomially many iterations, and every intermediate integer has
polynomial bit length. Euclid's algorithm and integer multiplication are
deterministic polynomial-time operations at these lengths. Repeated
squaring computes \(u^{M_B}\bmod N\) in a number of modular operations
polynomial in \(\log M_B\) and \(\log N\). Claim 4 is true.

## 5. Verification of the fixed feedback chain

First,

\[
37\cdot109=4033.
\]

The number \(37\) has no prime divisor at most \(\sqrt{37}<7\), and \(109\)
has no prime divisor among \(2,3,5,7\), the primes at most
\(\sqrt{109}<11\). Thus both are distinct odd primes.

### The order of \(2\)

Modulo \(37\),

\[
2^9=512\equiv31,
\qquad
2^{18}\equiv31^2=961\equiv-1.
\]

Thus \(2^{36}\equiv1\), but the order does not divide \(18\). Also,

\[
2^{12}\equiv(2^6)^2\equiv27^2\equiv26\not\equiv1\pmod{37}.
\]

The divisors of \(36\) that do not divide \(18\) are \(4,12,36\).
The last calculation excludes orders \(4\) and \(12\), so

\[
\operatorname{ord}_{37}(2)=36.
\]

Modulo \(109\),

\[
2^9=512\equiv76,
\qquad
2^{18}\equiv76^2=5776\equiv-1,
\]

and hence \(2^{36}\equiv1\). Moreover,

\[
2^{12}=4096\equiv63\not\equiv1\pmod{109}.
\]

The same divisor argument gives

\[
\operatorname{ord}_{109}(2)=36.
\]

Consequently \(\operatorname{ord}_{4033}(2)=\operatorname{lcm}(36,36)=36\).

### The feedback arithmetic

The equality \(g=2^{11}=2048\) is immediate. Also,

\[
3905\equiv-128\pmod{4033}
\]

and

\[
2048(-128)=-262144=1-65\cdot4033.
\]

Therefore \(3905\) is the canonical inverse of \(2048\) modulo \(4033\).
Euclid's algorithm gives

\[
\begin{aligned}
3905&=1\cdot1985+1920,\\
1985&=1\cdot1920+65,\\
1920&=29\cdot65+35,\\
65&=1\cdot35+30,\\
35&=1\cdot30+5,
\end{aligned}
\]

so

\[
\gcd(1985,3905)=5.
\]

The immediate sign gcds of the resulting public block are trivial:

\[
\gcd(5-1,4033)=\gcd(4,4033)=1,
\qquad
\gcd(5+1,4033)=\gcd(6,4033)=1.
\]

### The powered block

The largest prime powers at most \(9\) are \(8,9,5,7\), so

\[
M_9=8\cdot9\cdot5\cdot7=2520.
\]

Since \(36\mid2520\), Fermat's theorem modulo \(37\) gives

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
5^4&\equiv80,\\
5^8&\equiv80^2\equiv78,\\
5^{16}&\equiv78^2\equiv89,\\
5^{32}&\equiv89^2\equiv73,\\
5^{36}&\equiv73\cdot80\equiv63
\pmod{109}.
\end{aligned}
\]

Thus

\[
5^{2520}\equiv63\pmod{109}.
\]

The claimed CRT representative is verified directly:

\[
3442=37\cdot93+1,
\qquad
3442=109\cdot31+63.
\]

It lies in the canonical range modulo \(4033\), so

\[
5^{2520}\equiv3442\pmod{4033}.
\]

It follows that \(5^{2520}-1\) is divisible by \(37\) and not by \(109\).
Hence

\[
\gcd(5^{2520}-1,4033)=37.
\]

The executable step needs no hidden factor or hidden order. It computes

\[
x=5^{2520}\bmod4033
\]

and then \(\gcd(x-1,4033)\), using only the public triple
\((5,2520,4033)\). The factorization of \(4033\) and the local orders are
used only to prove why this public computation succeeds.

Finally, every \(h\in H_0=\langle2\rangle\) has order dividing \(36\).
Since \(36\mid2520\),

\[
h^{2520}=1\pmod{4033}.
\]

Thus no element of the declared old subgroup yields a proper sign gcd after
this fixed exponent, whereas the descendant \(5\) does. The descendant is
essential relative to this old subgroup and this fixed-exponent channel.

## 6. Exact scope

An \(H_0\)-invariant law is a mixture of uniform laws on \(H_0\)-cosets.
Powering a uniform supergroup law produces a uniform law on its image, but
that image need not contain \(H_0\). For example, here

\[
H_0^{2520}=\{1\}.
\]

Since \(|H_0|=36\), the point mass on \(1\) is not an
\(H_0\)-invariant law. Powering can therefore leave the old invariant-law
class, so an old-coset direct-sampling ceiling no longer applies to the
powered image.

This is an exact algorithmic escape from that distribution class, not a
success guarantee. The local-order xor in Claim 3 can fail because both
local orders divide \(M\), or because neither does.

The fixed witness also does not prove that feedback is necessary to factor
\(4033\). Once \(5\) is considered as an ordinary public base, the same
calculation is a standard smooth-exponent, Pollard-style factor attempt
without any feedback history.

Nothing proved here supplies an all-input smoothness law for the two local
orders, an inverse-polynomial density of feedback blocks satisfying the xor
gate, a computational lower bound, or a general polynomial-time factoring
algorithm.
