# F78 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the candidate proof,
its hostile audit, C81 in the progress notes, or any later artifact that
contains their proofs.

## Setup

Let \(N=pq\) for distinct odd primes, and identify

\[
G=(\mathbb Z/N\mathbb Z)^\times\cong G_p\times G_q.
\]

For \(J\le G\), let \(J_p,J_q\) be its projection images. A positive
separator is an element equal to \(1\) in exactly one CRT component.

Let \(H\le G\) contain no positive separator, and put \(h=|H|\).

## Claims to reconstruct

1. Both projections of \(H\) are isomorphisms onto their images. Hence

   \[
   |H|=|H_p|=|H_q|=h,
   \]

   and \(H\) is the graph of an isomorphism.

2. For any \(K\) with \(H\le K\le G\), define

   \[
   c=[K:H],\qquad
   a=[K_p:H_p],\qquad
   b=[K_q:H_q].
   \]

   Prove that \(a\mid c\), \(b\mid c\), and that the exact number of positive
   separators in \(K\) is

   \[
   \frac ca+\frac cb-2.
   \]

   Their uniform density is

   \[
   \frac{c/a+c/b-2}{ch}.
   \]

   Thus \(K\) contains a positive separator exactly when \(c>a\) or \(c>b\).

3. Suppose one old integer unit block \(B\), whose residue is in \(H\), is
   split as \(B=uv\). For

   \[
   K=\langle H,u,v\rangle,
   \]

   prove that \(K=\langle H,u\rangle\), so \(K/H\) is cyclic. Interpret
   \(c,a,b\) as the global and two local coset orders of \(u\). Prove that
   every element of \(K\) has a unique form \(u^tz\), with
   \(0\le t<c\) and \(z\in H\). Describe exactly the exponents and unique old
   elements that give the two local projection kernels.

4. Call a law on \(G\) \(H\)-invariant if it is a mixture of uniform laws on
   \(H\)-cosets. Prove that every \(H\)-coset contains at most four elements
   that can expose a proper factor through either
   \(\gcd(x-1,N)\) or \(\gcd(x+1,N)\). Therefore every \(H\)-invariant law
   has total direct-sign success probability at most \(4/h\).

   Deduce the sharper separate bounds

   \[
   \delta_+(K)\le 2/h,\qquad
   \delta_-(K)\le 2/h
   \]

   for uniform sampling from every supergroup \(K\ge H\).

5. In an adaptive sequence, suppose that for every realized prior history,
   trial \(t\)'s conditional law is within a deterministic
   total-variation bound \(\varepsilon_t\) of some \(H\)-invariant law.
   Prove

   \[
   \Pr(\text{some direct-sign success in \(T\) trials})
   \le \frac{4T}{h}+\sum_{t=1}^T\varepsilon_t.
   \]

6. If \(X\) is uniform on \(H\) and \(Y\) is any independent
   group-valued random variable, prove that every
   \(X^{\pm1}Y^{\pm1}\) law is \(H\)-invariant. State precisely which fixed,
   predictable, or independent-pool pair scans this controls and why it does
   not cover arbitrary value-dependent pair selection.

7. For \(L>2\), let

   \[
   H=\{(t,t):t\in C_L\}\le C_L\times C_L.
   \]

   Choose nonzero \(u,v\) such that \(v-u\) generates \(C_L\), and put
   \(z=(u,v)\). Prove that \(z\) is not a separator,
   \(\langle H,z\rangle=C_L\times C_L\), and the positive-separator density
   is

   \[
   \frac{2L-2}{L^2}.
   \]

## Required scope decision

Decide whether all claims are correct as stated. Keep the following
distinctions explicit:

* absence of every positive separator is stronger than failure of a finite
  test menu;
* the result concerns direct sign-gcd sampling, not exact square-class
  decoding or direct integer-overlap extraction;
* the abstract cyclic example is not an asserted canonical-inverse integer
  family;
* no public method for the hidden indices or cancellation word, no
  computational lower bound, and no factoring algorithm is claimed.
