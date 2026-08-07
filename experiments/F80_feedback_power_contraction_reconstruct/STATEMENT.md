# F80 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F80 candidate,
its hostile audit, C83 in the progress notes, or any later F80 proof
artifact. You may use the stated earlier P78 feedback history as an input
fact, but independently verify every group, order, complexity, and numerical
claim below.

Let \(N=pq\) for distinct odd primes. For a finite subgroup
\(K\le(\mathbb Z/N\mathbb Z)^\times\), define

\[
K^M=\{x^M:x\in K\}.
\]

Prove or refute:

1. If \(X\) is uniform on \(K\), then \(X^M\) is uniform on \(K^M\).
2. Projection commutes with powering. Therefore the exact positive-sign
   success density on the powered image is

   \[
   \delta_+(K^M)
   =
   \frac1{|K_p^M|}
   \frac1{|K_q^M|}
   -\frac2{|K^M|}.
   \]

3. For a public unit \(u\), with hidden local orders

   \[
   r_p=\operatorname{ord}_p(u),
   \qquad
   r_q=\operatorname{ord}_q(u),
   \]

   one has the exact factor gate

   \[
   1<\gcd(u^M-1,N)<N
   \iff
   (r_p\mid M)\mathbin{\mathrm{xor}}(r_q\mid M).
   \]

4. For

   \[
   M_B=\operatorname{lcm}(1,\ldots,B),
   \]

   choosing \(B=\operatorname{poly}(\log N)\) gives a polynomial-bit
   exponent that can be constructed and used in modular exponentiation in
   deterministic polynomial time.

Then verify or refute this fixed feedback chain:

\[
N=4033=37\cdot109.
\]

Before feedback, the declared block subgroup is

\[
H_0=\langle2\rangle.
\]

The element \(2\) has exact order \(36\) modulo both \(37\) and \(109\).
The earlier P78 feedback history uses

\[
g=2^{11}=2048,
\qquad
g^{-1}_{\mathrm{can}}\bmod4033=3905,
\]

and the integer refinement

\[
\gcd(1985,3905)=5
\]

exposes the public descendant block \(u=5\). Its immediate sign gcds are
trivial.

For

\[
M=M_9=\operatorname{lcm}(1,\ldots,9)=2520,
\]

prove or refute:

\[
5^M\equiv1\pmod{37},
\qquad
5^M\equiv63\pmod{109},
\qquad
5^M\equiv3442\pmod{4033},
\]

and hence

\[
\gcd(5^{2520}-1,4033)=37.
\]

Check that the executable final step uses only the public values
\((5,2520,4033)\). Check also that every \(h\in H_0\) instead satisfies
\(h^{2520}=1\pmod{4033}\), so the descendant block is essential relative to
this declared old-subgroup, fixed-exponent channel.

Finally, determine the exact scope:

- powering can leave the old-\(H_0\)-invariant distribution class because
  the image subgroup need not contain \(H_0\);
- this gives an exact algorithmic escape from the old-coset sampling
  ceiling, but not a success guarantee;
- \(5\) is also an ordinary small public Pollard-style base, so the witness
  does not show that feedback is necessary to factor the fixed integer
  \(4033\);
- the theorem supplies no all-input smoothness law, no inverse-polynomial
  density of suitable feedback blocks, and no general polynomial-time
  factoring algorithm.
