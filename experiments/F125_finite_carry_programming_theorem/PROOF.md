# F125 proof

Put \(G=\prod_i g_i\). For each \(i\), prescribe

\[
N\equiv-k_i^{-1}\pmod {g_i}.
\]

Each residue is reduced. Add \(N\equiv1\pmod2\) if parity is not already one
of these conditions. The Chinese remainder theorem gives one reduced class
\(A\pmod M\), for a fixed modulus \(M\).

Choose primes in the fixed progressions

\[
p\equiv1\pmod M,
\qquad
q\equiv A\pmod M.
\]

The prime number theorem in fixed arithmetic progressions supplies such
primes in the disjoint intervals

\[
p\in[X,1.1X],
\qquad
q\in[1.2X,1.3X]
\]

for all sufficiently large \(X\). Taking a disjoint unbounded sequence of
these intervals gives infinitely many distinct pairs. The factors are odd,
distinct, and comparable. Also \(N=pq\equiv A\pmod M\).

Since \(p,q=\Theta(X)\),

\[
n=2\log_2X+O(1).
\]

For sufficiently large \(X\), both factors exceed \(n^2\), every fixed
\(g_i\) is at most \(n\), and both factors exceed every \(g_i^2+1\).

The congruence modulo \(g_i\) gives \(g_i\mid1+k_iN\). Therefore

\[
w_i={1+k_iN\over g_i}
\]

is an integer and \(g_iw_i\equiv1\pmod N\). It is positive. Since
\(k_i\le g_i-1\),

\[
1+k_iN\le1+(g_i-1)N<g_iN,
\]

so \(w_i<N\). It is the least positive inverse and its carry is exactly
\(k_i\).

Because \(g_i\) is a unit modulo \(N\), multiplication by \(g_i\) gives

\[
\gcd(g_i-w_i,N)=\gcd(g_i^2-1,N),
\qquad
\gcd(g_i+w_i,N)=\gcd(g_i^2+1,N).
\]

Both prime factors exceed the fixed positive integers on the right, so both
gcds are one.

For the block claim, the seed endpoint \(g_i\) is prime. An exact monomial
presentation of this positive integer by pairwise-coprime blocks greater than
one and nonnegative exponents must use exactly one block, once. That block is
\(g_i\).

For the strengthening, assume the \(k_i\) are pairwise distinct. Choose
distinct odd primes \(r_i\) larger than every \(g_j\) and every
\(|k_u-k_v|\). Enlarge the fixed CRT system by

\[
N\equiv(r_i-1)k_i^{-1}\pmod {r_i^2}.
\]

The moduli are pairwise coprime and every displayed residue is reduced. Use
the same prime-in-progressions construction with the enlarged \(M,A\). For
\(P_i=1+k_iN\),

\[
P_i\equiv r_i\pmod {r_i^2},
\]

so \(v_{r_i}(P_i)=1\). For \(j\ne i\),

\[
P_j\equiv(k_i-k_j)k_i^{-1}\not\equiv0\pmod {r_i}.
\]

Thus \(r_i\) is private among the selected columns. This proves the theorem.

## Scope

The fixed modulus depends on the fixed finite prescription. The proof does
not apply with \(m=m(n)\). Other word or feedback columns can reuse the
auxiliary rows. This is not a complete-source obstruction and not a factoring
lower bound.
