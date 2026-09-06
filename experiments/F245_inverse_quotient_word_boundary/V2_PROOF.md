# Proof of F245 V2

## Inverse quotients

For \(0\le k<N\),

\[
K^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\]

Every member divides \(Nk+1<N^2\), so the fibre has size at most
\(\Delta_N\).  Uniformity gives the first atom bound.  Replacing zero by
one merges at most two atoms.  One residue class modulo \(\ell\) contains
at most \(\lceil N/\ell\rceil\) supported integers.  Since

\[
{N\over\varphi(N)}={p\over p-1}{q\over q-1}\le {15\over8}
\]

and \(\lceil N/\ell\rceil<2N/\ell\), equation (1) follows.

If \(\rho_r\) is the mass of residue class \(r\), then independent copies
satisfy

\[
\Pr(K_i\equiv K_j\pmod\ell)=\sum_r\rho_r^2
\le\max_r\rho_r.
\]

Deleting exact equality by replacing a zero difference with one cannot add
an odd-prime divisibility event.  Conditional uniformity gives the same
calculation after every prior transcript.  A prime dividing an adaptively
selected positive product must divide one of the complete bank's at most
\(Q+\binom Q2\) entries.  The union bound proves (3), including adaptive
stopping under the fixed envelope.

## Marker consequence and Las Vegas truncation

The primitive-order implication in the statement proves (9): if a marker
\(\ell\) divides \(|N^k-\sigma|\), then \(N^{2k}=1\pmod\ell\).  Modulo a
marker, \(N\) is \(\pm p\) or \(\pm q\), and (6) therefore forces
\(\ell-1\mid2k\).  Such a factor has binary length at least
\(\Omega(n\ell)\), which exceeds every fixed numerical-QP bound when
\(\ell>2^{cn}\).

The standard divisor bound

\[
\max_{m\le x}\log\tau(m)=O(\log x/\log\log x)
\]

at \(x=N^2\) gives \(\Delta_N=2^{o(n)}\).  A numerical-QP count is also
\(2^{o(n)}\).  Apply (3) to four markers larger than \(2^{cn}\) and take a
union bound to prove (12).

The square baseline is itself one allowed signed-power factor and therefore
misses the markers.  In orientation \((a,b)\), the identity

\[
\gcd(N-ab,p-a)=\gcd(p-a,q-b)
\]

and its \(q\)-side counterpart show that the large markers do not divide the
base exponent, because the four gcds are given by (7).  On the event (12),
the full word misses them too.  Hence the two residuals contain
\(\lambda_a\) and \(\rho_b\).  A uniform element of a cyclic group of order
\(m\) returns under exponent \(E\) with probability \(\gcd(E,m)/m\).
Every identity or Miller-chain split needs at least one local return, proving
(14).  A local quadratic norm vanishes with probability below \(2/p\) or
\(2/q\), so nonclean factor screens are also exponential because (5) makes
\(p,q>2^{cn}-1\).  Equation (7) bounds all accumulated common orders by
their lcm 12.

If a confined Las Vegas algorithm had expected time \(Q(n)\), Markov's
inequality would give probability at least \(1/2\) of stopping within
\(2Q(n)\).  That truncated run falls under the complete-bank and trial union
bounds and has exponentially small success.  This contradiction proves the
expected-time formulation for the stated grammar.

For the unconditional family, the first CRT class fixes \(p\), the four
marker incidences, and the two primitive \(p\)-residues.  The second class is
formed only after the complete support of \(p^2-1\) is known.  Its residues
avoid both signs at every prime \(s\ge5\) in that support, while the mod-8
and mod-\(3^{\max(e,2)}\) rows leave exactly the dyadic and ternary overlap
in (7).  Hence \(\gcd(p^2-1,q^2-1)=24\).  If the markers lie between
\(X\) and \(16X\), the first Linnik modulus is \(O(X^4)\).  Its prime
obeys \(p<X^{O(1)}\).  The second modulus is
\(O(p^2X^2)\), so \(q<X^{O(1)}\).  Marker congruences also give
\(p,q>X\).  Therefore \(n=\Theta(\log X)\), yielding one absolute
constant \(c\) in (4).

## Carry algebra

The definitions give

\[
X=Av-Nq_A,
\qquad
Y=Bv-Nq_B,
\qquad
gv-1=N\widetilde d.
\]

Direct substitution yields (15).  Also

\[
A^2-DB^2=(a^2-Db^2)^2=g^2.
\]

Using \(gX=A+Nk\) and \(gY=B+Nl\), expand

\[
g^2(X^2-DY^2)
=g^2+2N(Ak-DBl)+N^2(k^2-Dl^2).
\]

Subtract \(g^2\) and divide by \(Ng^2\) to obtain (16).  For a
noncanonical signed \(g=r+tN\), the quotient is
\(\widetilde d=K(r)+tv\); it need not have the uniform canonical law.
Thus no probability conclusion transfers to these nonlinear carries.
