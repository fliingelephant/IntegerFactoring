# F81 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F81 candidate,
either hostile audit, C84 or later progress notes, or any later F81 proof
artifact.

Let \(N=pq\) for distinct odd primes and let
\(u\in(\mathbb Z/N\mathbb Z)^\times\). Put

\[
r_p=\operatorname{ord}_p(u),
\qquad
r_q=\operatorname{ord}_q(u),
\qquad
r=\operatorname{lcm}(r_p,r_q).
\]

Prove or refute:

1. The cyclic group \(\langle u\rangle\) contains a positive direct-sign
   separator if and only if \(r_p\ne r_q\).
2. Its exact positive-separator count and uniform density are

   \[
   \frac r{r_p}+\frac r{r_q}-2,
   \qquad
   \frac1{r_p}+\frac1{r_q}-\frac2r.
   \]

3. For every \(E\ge1\),

   \[
   1<\gcd(u^E-1,N)<N
   \iff
   (r_p\mid E)\mathbin{\mathrm{xor}}(r_q\mid E).
   \]

4. If \(r_p=r_q\), every pure power also has synchronized negative-sign
   status, so neither direct sign can factor through a pure power.

For a positive integer \(a\), let \(\sigma(a)\) be its largest full
prime-power divisor, with \(\sigma(1)=1\). Put

\[
M_B=\operatorname{lcm}(1,\ldots,B)
\]

and define

\[
\mathcal E_B
=
\{M_B\}
\cup
\left\{
\frac{M_B}{\ell^j}:
\ell\le B\text{ prime},\
1\le j\le\lfloor\log_\ell B\rfloor
\right\}.
\]

Prove or refute the exact completeness claim:

\[
\exists E\in\mathcal E_B:
1<\gcd(u^E-1,N)<N
\]

if and only if

\[
r_p\ne r_q
\quad\text{and}\quad
\min\{\sigma(r_p),\sigma(r_q)\}\le B.
\]

Check that \(|\mathcal E_B|\le B+1\), and that the complete bank has
deterministic polynomial bit complexity for
\(B=\operatorname{poly}(\log N)\). Explicitly distinguish
\(\sigma(r)\le B\) from standard \(B\)-smoothness.

Verify the fixed order data used at \(N=4033=37\cdot109\):

\[
\operatorname{ord}_{37}(5)=36,
\qquad
\operatorname{ord}_{109}(5)=27,
\]

so

\[
\sigma(36)=9,
\qquad
\sigma(27)=27,
\]

and \(M_9=2520\) separates the two orders.

Finally, prove or refute the phase-only example. For prime \(L>2\), work
additively in \(\mathbb F_L^2\), and put

\[
g=(1,1),
\qquad
H=\langle g\rangle,
\qquad
z=(a,b)
\]

for distinct nonzero \(a,b\). Both coordinates of \(z\) have order \(L\),
so no scalar multiple of \(z\) is a separator. Nevertheless,

\[
\langle H,z\rangle=\mathbb F_L^2,
\qquad
z-ag=(0,b-a)
\]

is a separator. Check the exact scope: this is an abstract
order-versus-phase classification, not a canonical-integer hard family,
feedback source law, computational lower bound, or factoring algorithm.
