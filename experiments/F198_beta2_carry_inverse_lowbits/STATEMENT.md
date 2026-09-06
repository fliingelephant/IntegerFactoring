# F198: the beta-two carry is a hidden inverse, and a quarter-minus-polylog prefix is terminal

Status: frozen literature-dependent proof-only candidate.

## Scope and notation

Let

\[
N=pq,
\qquad p<q<2p,
\tag{1}
\]

where \(p\) and \(q\) are distinct odd primes. Define

\[
n=\left\lceil\log _2(N+1)\right\rceil,
\qquad B=\lfloor\sqrt N\rfloor,
\qquad C=\binom{N-1}{B},
\qquad A=(-1)^BC,
\tag{2}
\]

and

\[
h=\frac{A-(1-q)}N.
\tag{3}
\]

The balanced-prime congruence

\[
A\equiv1-q\pmod N
\tag{4}
\]

makes \(h\) an integer. For each \(1\le t\le n\), all residues modulo
\(2^t\) below are their canonical representatives in \([0,2^t)\). Put

\[
z_t=N^{-1}(A-1)\pmod {2^t}.
\tag{5}
\]

This notation means multiplication by the modular inverse of the odd integer
\(N\). It does not assert that \((A-1)/N\) is an integer.

All complexity claims use the deterministic classical bit model. A
numerical-QP bound has the form
\(2^{(\log n)^{O(1)}}\).

## Theorem 1: the public offset is polynomial-time computable

There is a deterministic algorithm that, from \((N,t)\) with
\(1\le t\le n\), computes \(z_t\) in time polynomial in \(n\).

The algorithm first uses the corrected Andreica 2013 power-of-two binomial
algorithm at precision \(n\) to compute

\[
C\bmod2^n.
\tag{6}
\]

It applies the public sign \((-1)^B\), reduces the result modulo \(2^t\),
and evaluates (5). In particular, the algorithm does not apply Andreica's
main-range theorem directly at precision \(t\), where the upper index
\(N-1\) could exceed \(2^t-1\).

## Theorem 2: exact hidden-inverse decomposition

For every \(1\le t\le n\),

\[
\boxed{
h-z_t\equiv p^{-1}\pmod {2^t}.}
\tag{7}
\]

Define the promise functions

\[
\mathcal H_t(N)=h\bmod2^t,
\qquad
\mathcal P_t(N)=p\bmod2^t.
\tag{8}
\]

For every public polynomial-time computable choice of \(t=t(N)\) in
\([1,n]\), these two functions are interreducible by deterministic
polynomial-time one-query reductions. Explicitly,

\[
\mathcal P_t(N)
=\left(\mathcal H_t(N)-z_t\right)^{-1}\pmod {2^t},
\tag{9}
\]

and

\[
\mathcal H_t(N)
=z_t+\mathcal P_t(N)^{-1}\pmod {2^t}.
\tag{10}
\]

The inverses exist because \(p\) is odd. Thus the only nonpublic coordinate
of the truncated carry is exactly the low \(t\)-bit block of the hidden
factor, written reciprocally in \(\mathbb Z_2\).

## Theorem 3: half precision gives exact polynomial-time recovery

Let

\[
t_0=\left\lceil\frac n2\right\rceil.
\tag{11}
\]

One value \(h\bmod2^{t_0}\) determines the exact smaller factor \(p\) in
deterministic polynomial time. Indeed, (9) gives \(p\bmod2^{t_0}\), and

\[
0<p<\sqrt N<2^{n/2}\le2^{t_0}.
\tag{12}
\]

Hence its canonical residue is the integer \(p\) itself. Division by the
candidate verifies the factor and gives \(q=N/p\).

Conversely, the exact factorization computes \(h\bmod2^{t_0}\) in
polynomial time through (10). Therefore this half-precision carry problem
and factoring are polynomial-time equivalent on the promise.

## Theorem 4: a quarter-minus-polylog prefix is a deterministic QP terminal

Because \(N\) is odd,

\[
\lambda=\lfloor\log_2N\rfloor=n-1.
\tag{13}
\]

Define

\[
k=\left\lfloor\frac{\log_2N}{4}\right\rfloor
 =\left\lfloor\frac{n-1}{4}\right\rfloor.
\tag{14}
\]

Let \(L=L(n)\ge0\) be any fixed integer-valued function satisfying

\[
L(n)=(\log n)^{O(1)},
\tag{15}
\]

and assume

\[
t=k-L(n)\ge1.
\tag{16}
\]

Then one value \(h\bmod2^t\) factors \(N\) deterministically in numerical-QP
time.

To see this, first use (9) to obtain the canonical residue

\[
p_t=p\bmod2^t.
\tag{17}
\]

Set

\[
m=2^t,
\qquad s=p_t.
\tag{18}
\]

The integer \(m\) is a unit modulo the odd input \(N\), and
\(1\le s<m<N\). Moreover, \(p\equiv s\pmod m\). Gao--Feng--Hu--Pan 2025,
Theorem 3.1, with \(r=1\), therefore finds this prime divisor in

\[
O\!\left(
\left\lceil\frac{N^{1/4}}{2^t}\right\rceil
\log^{7+3\epsilon}N
\right)
\tag{19}
\]

bit operations, for every fixed \(\epsilon>0\). Since

\[
\frac{N^{1/4}}{2^t}
=2^{(\log_2N)/4-k+L}
<2^{L+1},
\tag{20}
\]

this is numerical QP. This direct arithmetic-progression terminal needs no
enumeration of the missing \(L\) bits.

There is also an independent older terminal. Enumerate the \(2^L\)
extensions

\[
p_{0,j}=p_t+j2^t,
\qquad 0\le j<2^L.
\tag{21}
\]

They are exactly the residues in \([0,2^k)\) that reduce to \(p_t\) modulo
\(2^t\). One of them is \(p\bmod2^k\). For each extension, compute

\[
q_{0,j}=Np_{0,j}^{-1}\pmod {2^k},
\tag{22}
\]

and run the deterministic algorithm of Coppersmith's 1997 Theorem 5 for
factoring \(N=PQ\) from the known low-order \(k\) bits of \(P\). Verify every
returned candidate by exact division. The correct extension satisfies the
theorem's hypothesis and therefore returns the factorization. This
independent route costs

\[
2^L\operatorname{poly}(n)
=2^{(\log n)^{O(1)}}.
\tag{23}
\]

Consequently, a numerical-QP evaluator for this truncated carry yields a
numerical-QP factorer. In the reverse direction, factoring computes the
truncated carry in polynomial time by (10). The two promise functions are
therefore interreducible with numerical-QP overhead at the precision
(16). Finite inputs for which \(k-L<1\) can be handled directly and do not
affect the uniform asymptotic bound.

## Exact boundary

F198 does not evaluate any bit of \(h\). It proves that the low
quarter of the hidden inverse, allowing a polylogarithmic deficit, is
already a complete numerical-QP factoring statistic. A one-bit-at-a-time
method is not excluded: a QP selector for the correct lift at each precision
would form one sequential chain of only \(O(n)\) stages, which
is still QP.

The result is integer-specific. The easy term \(z_t\) is a power-of-two
compression of a remote integer coefficient. The remaining term is the
canonical low-bit residue of the rational prime factor. Generic ring
operations, a \(2\)-adic-gamma rewrite, or a product representation make
progress only if they select the correct lift of this hidden inverse.
