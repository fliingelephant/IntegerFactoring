# F83 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F83 candidate,
hostile audit, progress notes, PROVED, or later F83 artifacts. Do not use
hidden factors as executable input. No research computation is requested.

Let \(N=pq\) for distinct odd primes. Let
\(q_1,\ldots,q_s\) be pairwise-coprime positive units modulo \(N\), and let

\[
A_i=\prod_{j=1}^s q_j^{e_{ji}}\equiv1\pmod N,
\qquad
1\le i\le m,
\]

be an explicit relation list with nonnegative integer exponents. Let \(E\)
be the \(s\times m\) exponent matrix. Fix a public prime \(\ell\), and put

\[
V=\ker(E\bmod\ell)\le\mathbb F_\ell^m.
\]

For \(c\in V\), use coordinate representatives
\(c_i\in\{0,\ldots,\ell-1\}\), and define

\[
\widetilde R(c)
=
\prod_{j=1}^s
q_j^{(\sum_i e_{ji}c_i)/\ell},
\qquad
R(c)=[\widetilde R(c)]_N.
\]

Prove or refute:

1. Every exponent is an integer, and

   \[
   R(c)^\ell\equiv1\pmod N.
   \]

2. The map

   \[
   \rho:V\to
   \mu_\ell(\mathbb F_p)\times\mu_\ell(\mathbb F_q),
   \qquad
   c\mapsto(R(c)\bmod p,R(c)\bmod q)
   \]

   is a group homomorphism despite the use of canonical coordinate
   representatives.
3. For \(r\in\{p,q\}\), define

   \[
   K_r=\{c\in V:R(c)\equiv1\pmod r\}.
   \]

   Each \(K_r\) is either all of \(V\) or a hyperplane, including the case
   \(\ell=r\).
4. The public gcd has the exact hidden-kernel gate

   \[
   1<\gcd(R(c)-1,N)<N
   \iff
   c\in K_p\mathbin\triangle K_q.
   \]

Let \(d_p,d_q\in\{0,1\}\) be the ranks of the two local maps and let
\(d\in\{0,1,2\}\) be their joint rank. For uniform \(c\in V\), prove or
refute the density formula

\[
\Pr(c\in K_p\mathbin\triangle K_q)
=
\ell^{-d_p}+\ell^{-d_q}-2\ell^{-d}.
\]

If \(K_p\ne K_q\), check that this density is either

\[
1-\frac1\ell
\quad\text{or}\quad
\frac{2(\ell-1)}{\ell^2}.
\]

Now let \(b_1,\ldots,b_D\) be any public basis of \(V\), and define

\[
\mathcal C
=
\{b_i:1\le i\le D\}
\cup
\{b_i+t b_j:1\le i<j\le D,\ t\in\mathbb F_\ell^\times\}.
\]

Prove or refute the deterministic completeness theorem

\[
K_p\ne K_q
\iff
\exists c\in\mathcal C:
1<\gcd(R(c)-1,N)<N.
\]

Check all zero-functional, proportional-functional, \(D=0\), and \(D=1\)
cases. Check that the menu elements are distinct and that

\[
|\mathcal C|=D+(\ell-1)\binom D2.
\]

For \(\ell=2\), prove or refute that basis vectors alone are complete.

Check the bit-complexity claim. If the explicit relation presentation has
total bit length \(L\), and the numerical value of \(\ell\) is polynomial
in \(L+\log N\), then Gaussian elimination, construction of all menu roots
modulo \(N\), and all gcd tests have deterministic polynomial total bit
complexity. The algorithm must use only \(N,\ell\), the public blocks, and
the exponent matrix.

Finally, verify the fixed operation-separation certificate

\[
N=215=5\cdot43,
\qquad
8\cdot27=216=1+N.
\]

Using blocks 2 and 3, the exponent column is \((3,3)^T\). Modulo 2 its
kernel is zero, so there is no nonzero binary saturation relation. Check
that the endpoint signs and raw difference give no factor. Modulo 3 the
column is zero, and \(c=1\) gives

\[
R=2\cdot3=6,
\qquad
R^3\equiv1\pmod{215},
\qquad
\gcd(R-1,215)=5.
\]

Record the scope defect of this fixed witness:

\[
\gcd(8+27,215)=5.
\]

Thus it separates odd-prime saturation from the binary relation space, but
not from every broader endpoint screen. State the general scope precisely:
the theorem is a factor-free polynomial decoder conditional on an explicit
relation state and on \(K_p\ne K_q\). It does not manufacture that kernel
asymmetry, select a useful prime on every input, prove literature novelty,
or give a factoring algorithm. Proportional nonzero local characters have
the same identity kernel and remain outside this decoder.
