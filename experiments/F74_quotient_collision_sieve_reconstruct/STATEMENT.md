# Proof-blind reconstruction statement: quotient-collision batch feedback

Reconstruct every claim below from this statement only. Do not read any other
F74 artifact, audit, proof, or durable ledger. Do not run computation. Give a
self-contained proof or return FAIL with the first exact obstruction.

## Setup

Let \(N\ge3\). For \(1\le i\le m\), let

\[
A_i=x_i y_i=1+k_iN,
\qquad
1\le x_i,y_i<N,
\]

be indexed canonical inverse relation occurrences. Equal values remain
separate. Put

\[
P=\prod_iA_i=1+KN.
\]

Assume all endpoint presentations have a complete gcd-free block basis with
exact exponents and indexed occurrence capacities. For \(r\ge1\), define

\[
A_r=1+rN,
\qquad
D_r=\gcd(P,A_r).
\]

## Claims to reconstruct

1. For every \(r\ge1\),

   \[
   D_r
   =\gcd(P,K-r)
   =\gcd\!\left(A_r,\prod_i(k_i-r)\right),
   \]

   with the last product interpreted as zero when \(r=k_i\). If no
   \(k_i=r\), then

   \[
   v_p(D_r)=\min\!\left(v_p(A_r),\sum_i v_p(k_i-r)\right).
   \]

   In particular, every prime of \(D_r\) divides a quotient difference.

2. Let \(g\) be an occurrence-certified divisor of \(P\), with
   \(1<g<N\), and let

   \[
   g\iota_N(g)=1+k(g)N.
   \]

   Then

   \[
   k(g)=r
   \quad\Longleftrightarrow\quad
   g\mid D_r\text{ and }r<g<N.
   \]

3. If \(N>r^2\), then a legal quotient-\(r\) candidate exists after
   gcd-free refinement by \(D_r\) if and only if \(D_r>r\). Give a
   deterministic construction without subset enumeration. Explain why the
   factor-occurrence list and all intermediate integers have polynomial bit
   length. If \(r\le\operatorname{poly}(\log N)\) but \(N\le r^2\), explain
   the polynomial trial-division branch.

4. Define

   \[
   \rho_N(g)=(-N^{-1})\bmod g
   \]

   in \(1,\ldots,g-1\). Prove that \(\rho_N(g)=k(g)\). If \(g\mid P\),
   prove it is also \(K\bmod g\). Explain the exact duality between choosing
   \(g\) and computing \(r\), versus choosing \(r\) and computing \(D_r\).
   State why \(D_r\) need not itself be a legal or useful candidate.

5. Assume \(m\) and the scan bound \(R\) are polynomial in
   \(n=\lceil\log_2N\rceil\). Prove that computing \(P\), scanning all
   \(r\le R\), and doing the required gcd-free refinements has polynomial bit
   complexity in the retained transcript size and \(n\). Prove the same
   quotient-difference identity for every node of a relation subproduct tree,
   and explain why the tree gives provenance but not arbitrary subset
   selection.

6. Prove the bounded-quotient domination theorem. If

   \[
   1\le r,k_i\le B,
   \qquad r\ne k_i,
   \qquad B=\operatorname{poly}(\log N),
   \]

   and \(D_r>r\), then either trial division resolves \(N\), or a prior
   canonical-state scan through \(B^2\) emits \(A_r\). With the unchanged
   source product and endpoint ledger, it then recovers the same \(D_r\) and
   divisor provenance. The key construction should give
   \(r<g\le rB\le B^2\).

7. Verify the equal-quotient warning at \(N=55\):

   \[
   56=2\cdot28=14\cdot4=1+55,
   \]

   where the first displayed endpoints pass both sign screens but
   \(\gcd(14+1,55)=5\). Explain why \(D_1=56\) gives no localization of the
   useful alternative presentation.

8. Prove

   \[
   \gcd(g-\iota_N(g),N)=\gcd(g^2-1,N),
   \]

   and explain why this gcd is \(N\), not a proper factor, on a non-global
   involution. Verify \(N=55,g=21\), and conclude that both sign screens must
   remain.

9. Explain why decoder-lattice compression is not source compression. Verify
   at \(N=4033,r=3\) that one quotient-one occurrence gives \(D_3=2\), while
   two occurrences give \(D_3=4\), although the duplicate does not enlarge
   the decoder row span.

10. Verify the five exact gate rows:

   \[
   \begin{array}{c|c|c|c}
   N&\{k_i\}&r&D_r\\ \hline
   21&\{1,4\}&9&10\\
   55&\{1,2\}&8&21\\
   21&\{1,1,1\}&3&8\\
   4033&\{1,1\}&3&4\\
   4033&\{1,63,7\}&1983&10240=2^{11}\cdot5.
   \end{array}
   \]

   In the last row, verify that \(g=2048\) has complement \(3905\) and that
   \(\gcd(10240,1985)=5\). Also verify the family with \(t\) quotient-one
   copies,

   \[
   N=(2^{2t}-1)/3,
   \qquad r=3,
   \qquad D_3=2^t.
   \]

## Required scope

The result computes the complete supported fibre for each declared target
\(r\). It does not prove that a polynomial target range contains a successful
\(r\), that the generic greedy divisor is factor-bearing, or that any
all-input success probability exists. In the bounded-quotient regime it gives
no new source state beyond a polynomial small-state scan. No factoring
algorithm is claimed.
