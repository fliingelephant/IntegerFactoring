# F92 proof-blind reconstruction statement

Reconstruct or refute every claim below without reading the F92 candidate,
any F92 audit, later F92 artifacts, or later durable-state entries.

You may use the supplied P95 and P97 results:

- for \(N=pq\) with distinct odd primes and \(E=N-1\), the \(E\)-power
  image of a supplied subgroup is a full rectangle with coprime residual
  local orders;
- if

  \[
  g=\gcd(p-1,q-1),
  \qquad
  A=(p-1)/g,
  \qquad
  B=(q-1)/g,
  \]

  then the full unit-group image

  \[
  S=G^E,
  \qquad
  G=(\mathbb Z/N\mathbb Z)^\times,
  \]

  satisfies

  \[
  S\cong C_A\times C_B,
  \qquad
  \gcd(A,B)=1.
  \]

For a positive integer \(r\), let \(r_{\perp E}\) be its largest divisor
coprime to \(E\). Put

\[
A_*=A_{\perp E},
\qquad
B_*=B_{\perp E},
\]

and let \(T\le G\) be the CRT product of the unique local subgroups of orders
\(A_*,B_*\).

Prove or refute the following.

1. The exact identity

   \[
   E/g=gAB+A+B
   \]

   implies

   \[
   \gcd(A,E/g)=\gcd(B,E/g)=1.
   \]

2. The quotient above the full powered rectangle is

   \[
   G/S\cong C_g\times C_g.
   \]

   In particular \(g\mid E\). For every subgroup \(S\le K\le G\),

   \[
   (K/S)^E=1,
   \qquad
   S^E\le K^E\le S.
   \]

3. If

   \[
   n=\lceil\log_2(N+1)\rceil,
   \]

   then every such \(K\) has the same stable image

   \[
   K^{E^n}=T.
   \]

   Check the valuation bound, the subgroup sandwich, and the claimed public
   polynomial bit complexity of applying \(n\) successive \(E\)-powers to a
   polynomial-size generator list.

4. If \(\gcd(AB,g)=1\), then

   \[
   \gcd(AB,E)=1,
   \qquad
   T=S,
   \qquad
   K^E=S
   \]

   for every \(S\le K\le G\).

5. If every prime divisor of \(d>0\) divides \(E\), then powering by \(d\)
   is an automorphism of \(T\) and

   \[
   x_p^d=1\iff x_p=1,
   \qquad
   x_q^d=1\iff x_q=1.
   \]

   Decide whether this covers repeated \(N-1\) powers and all punctures
   obtained by removing prime powers from \(N-1\).

6. For every positive numerical bound \(H\), prove or refute the existence
   of distinct odd primes \(p,q\) such that

   \[
   g=2,
   \qquad
   A>H,
   \qquad
   B>H,
   \qquad
   \gcd(AB,E)=1.
   \]

   You may use Dirichlet's theorem and CRT. Check carefully that the chosen
   arithmetic progression is a reduced residue class and that it forces
   \(\gcd(A,B)=1\).

7. Verify the fixed cases:

   - \(4033=37\cdot109\) has \((A,B)=(1,3)\) with \(3\mid E\);
   - \(2047=23\cdot89\) has \((A,B)=(1,4)\) with \(2\mid E\);
   - \(2773=47\cdot59\) has \(g=2\), \((A,B)=(23,29)\), and
     \(\gcd(23\cdot29,2772)=1\).

State the exact algorithmic scope. On a P97 batch that really generates
\(S\), canonical feedback can still change the unpowered subgroup or expose
a transient component. The claims above would show only that repeated
\(N-1\)-smooth powering cannot change the stable core. Do not infer an axis
decoder, a factoring algorithm, or a computational lower bound.
