# F99 proof-blind reconstruction statement

Reconstruct the following statements without reading any other file in this
experiment directory.

## A. Orbit collapse

Let \(a\ge2\), \(m\ge3\), and

\[
N=(a^m-1)/k
\]

be an odd integer, with \(1\le k<a\). For \(1\le r<m\), assume
\(a^r<N\) and \(a^{m-r}<N\). Define

\[
c_r=a^r,
\qquad
w_r=a^{m-r}.
\]

Prove that \(w_r\) is the least positive inverse of \(c_r\) modulo \(N\)
and that every exact canonical-inverse relation on this trajectory is the
same integer:

\[
c_rw_r=a^m=1+kN.
\]

If \(m\) is odd and \(a\) is one square-normalized basis block, prove that
all nonzero binary columns from this trajectory are identical. Every new
dependency made only from exact copies has normalized root \(+1\) modulo
\(N\), even if one copy was retained before the trajectory. Therefore raw
nullity can grow without enlarging the normalized-root image. If \(a\) is
already a prime basis block, prove also that endpoint gcd refinement creates
no new block.

## B. Fixed stable witness

Verify the exact instance

\[
N=(3^{17}-1)/2=64{,}570{,}081=1{,}871\cdot34{,}511.
\]

Prove both displayed factors prime from explicit Lucas certificates. Verify
that \(n=26\), \(n^2=676\), both factors exceed the trial bound, and

\[
g=\gcd(1870,34510)=170,
\quad
(A,B)=(11,203),
\quad
\gcd(AB,N-1)=1.
\]

Verify that 3 has order 17 modulo each factor and modulo \(N\). The complete
range \(0\le e\le676\) visits only 17 residues. Apart from the residue 1,
all first-occurrence presentations have the exact relation value
\(3^{17}=1+2N\). For every nontrivial residue \(c\) with canonical inverse
\(w\), both \(\gcd(c-w,N)\) and \(\gcd(c+w,N)\) are one. All endpoints are
powers of the known block 3. Hence this complete one-seed trajectory adds
duplicate kernel directions with global root \(+1\), but no direct factor or
block split.

This is not a failure claim for the other seeds of the full F98 rule.

## C. Private-row family

For every sufficiently large integer \(T\), construct a distinct odd
semiprime \(N_T\) and the consecutive states \(c_e=2^e\),
\(1\le e\le T\), whose exact canonical-inverse relation values

\[
P_e=1+(2^e-1)N_T
\]

are linearly independent in the positive rational square-class group.

The construction must give a distinct prime \(q_e\) for every column such
that

\[
v_{q_e}(P_e)=1,
\qquad
q_e\nmid P_j\quad(j\ne e).
\]

It must also prove

\[
\log N_T=\Theta(T^2),
\qquad
T=\Theta(\sqrt{\operatorname{bitlength}(N_T)}).
\]

You may use Bertrand's postulate, the Chinese remainder theorem,
Dirichlet's theorem on primes in progressions, and Linnik's theorem.

## Required scope

Conclude only that exact duplicate relation count and raw binary nullity are
not progress measures, and that consecutiveness alone does not force a
binary closure. This obstruction does not apply to the current F98
certificate, which removes repeated exact values, uses 166 distinct selected
values, and produces a non-global root that factors its modulus. Do not claim
that the full multi-seed rule fails, that an \(n^2\)-long private-row family
was proved, or that a factoring lower bound follows.
