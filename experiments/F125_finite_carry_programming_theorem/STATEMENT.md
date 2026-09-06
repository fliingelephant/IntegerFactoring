# F125 statement — finite canonical-carry programming

Fix an integer \(m\ge1\), independent of \(N\). Fix distinct rational primes
\(g_1,\ldots,g_m\) and integers \(1\le k_i<g_i\).

There are infinitely many balanced odd distinct-prime semiprimes \(N=pq\)
such that, for \(n=\operatorname{bitlength}(N)\):

1. \(p,q>n^2\) and every \(g_i\le n\);
2. the least positive inverse of \(g_i\bmod N\) is
   \[
   w_i={1+k_iN\over g_i};
   \]
3. both \(\gcd(g_i-w_i,N)\) and \(\gcd(g_i+w_i,N)\) are one; and
4. every exact pairwise-coprime positive-integer block basis with
   nonnegative exponent presentations of all seed endpoints contains the
   block \(g_i\).

If the \(k_i\) are pairwise distinct, the family can additionally satisfy:
for fixed distinct auxiliary primes \(r_i\),

\[
v_{r_i}(1+k_iN)=1,
\qquad
r_i\nmid1+k_jN\quad(j\ne i).
\]

Thus each \(r_i\) is a valuation-one row private among the selected exact
values \(1+k_iN\).

The finite prescription is fixed while \(N\) grows. The statement does not
control a growing F26-Q source or privacy against its other columns.
