# Proof of F198

## 1. Integrality of the signed carry

The inequalities \(p<q\) and \(N=pq\) give

\[
p<\sqrt N<q,
\qquad p\le B<q.
\tag{21}
\]

The promise \(q<2p\) also gives \(N<2p^2\), so \(B<2p\). Write

\[
B=p+r,
\quad 0\le r<p,
\qquad
q=p+d,
\quad 1\le d<p.
\tag{22}
\]

Modulo \(q\), every denominator \(1,\ldots,B\) is a unit. Therefore

\[
C
=\prod_{j=1}^{B}\frac{N-j}{j}
\equiv(-1)^B\pmod q,
\tag{23}
\]

and \(A=(-1)^BC\equiv1\equiv1-q\pmod q\).

In base \(p\),

\[
N-1=p^2+(d-1)p+(p-1),
\qquad
B=0\cdot p^2+1\cdot p+r.
\tag{24}
\]

Lucas' theorem yields

\[
C
\equiv\binom10\binom{d-1}{1}\binom{p-1}{r}
\equiv(d-1)(-1)^r\pmod p.
\tag{25}
\]

Since \(p\) is odd, \((-1)^B=-(-1)^r\). Hence

\[
A\equiv1-d\equiv1-q\pmod p.
\tag{26}
\]

The same congruence holds modulo the distinct prime \(q\). The Chinese
remainder theorem proves (4), so the integer \(h\) in (3) is well-defined.

## 2. Computing the public offset

The audited form of Andreica's 2013 algorithm has the following main-range
interface. At precision \(T\), uniform preprocessing costs

\[
O\!\left(T^3\mathsf M(T)+T^4\right)
\tag{27}
\]

bit operations. It then computes one coefficient
\(\binom P Q\bmod2^T\), for
\(0\le Q\le P\le2^T-1\), in

\[
O\!\left(T^2\log T\,\mathsf M(T)\right)
\tag{28}
\]

bit operations.

Use

\[
T=n,
\qquad P=N-1,
\qquad Q=B.
\tag{29}
\]

The definition of \(n\) gives

\[
N+1\le2^n,
\qquad N-1\le2^n-2<2^n.
\tag{30}
\]

Thus (29) is inside the source's main range. Including preprocessing, it
computes \(C_n=C\bmod2^n\) in time polynomial in \(n\).

For any \(t\le n\), compute

\[
a_t=(-1)^BC_n\bmod2^t.
\tag{31}
\]

This is \(A\bmod2^t\). Since \(N\) is odd, the extended Euclidean
algorithm computes \(N^{-1}\bmod2^t\) in polynomial time. Therefore

\[
z_t=N^{-1}(a_t-1)\bmod2^t
\tag{32}
\]

is polynomial-time computable. The construction deliberately runs the
published binomial algorithm once at precision \(n\) and then reduces. It
does not assume that \(N-1<2^t\).

The Andreica interface here is exactly the one audited and promoted in
P173. It uses four forced corrections to typographical defects in the
published formulas: two displayed additions are modular multiplications,
the valuation recurrence uses the preceding index, and Legendre's formula
uses floors. These corrections are forced by the definitions and preserve
(27)--(28). F198 adds no new interpretation of that source.

## 3. The hidden reciprocal identity

From the definition of \(h\),

\[
Nh=A-1+q.
\tag{33}
\]

Reduce (33) modulo \(2^t\) and multiply by \(N^{-1}\):

\[
h
\equiv N^{-1}(A-1)+N^{-1}q
\equiv z_t+N^{-1}q
\pmod {2^t}.
\tag{34}
\]

Because \(N=pq\) and \(p,q,N\) are units modulo \(2^t\),

\[
N^{-1}q=(pq)^{-1}q=p^{-1}\pmod {2^t}.
\tag{35}
\]

Equations (34)--(35) prove (7).

Let \(H\) be the canonical oracle output for \(h\bmod2^t\). Then

\[
u=(H-z_t)\bmod2^t=p^{-1}\bmod2^t.
\tag{36}
\]

The residue \(u\) is odd. Inverting it modulo \(2^t\) gives the canonical
residue \(p\bmod2^t\), proving (9). Conversely, a canonical residue
\(P_t=p\bmod2^t\) is odd, and (10) follows by one modular inversion and
addition. Both transformations make one oracle query and use a polynomial
number of bit operations. This proves Theorem 2.

## 4. Exact recovery at half precision

Since \(p<q\),

\[
p^2<N,
\qquad p<\sqrt N.
\tag{37}
\]

Also \(N+1\le2^n\), so \(N<2^n\). With
\(t_0=\lceil n/2\rceil\),

\[
p<\sqrt N<2^{n/2}\le2^{t_0}.
\tag{38}
\]

Equation (9) therefore returns not only a residue but the exact integer
\(p\). Check \(1<p<N\) and \(p\mid N\), and set \(q=N/p\). All operations
have polynomial bit cost. The reverse reduction is already (10). This
proves Theorem 3.

## 5. Matching the primary low-bit threshold

First relate the three length conventions. The definition of \(n\) gives

\[
2^{n-1}<N+1\le2^n.
\tag{39}
\]

Thus \(N\ge2^{n-1}\). Equality is impossible because \(N\) is odd and
composite. Hence

\[
2^{n-1}<N<2^n,
\qquad
\lfloor\log_2N\rfloor=n-1.
\tag{40}
\]

Since \(\log_2N\in(n-1,n)\), taking one quarter and floors gives

\[
\left\lfloor\frac{\log_2N}{4}\right\rfloor
=\left\lfloor\frac{n-1}{4}\right\rfloor
=k.
\tag{41}
\]

Coppersmith's 1997 Theorem 5 states that the factorization of
\(N=PQ\) can be found in deterministic polynomial time when the low-order

\[
k=\left\lfloor\frac14\log_2N\right\rfloor
\tag{42}
\]

bits of \(P\) are known. The proof writes

\[
P=2^kx+P_0,
\qquad
Q=2^ky+Q_0,
\tag{43}
\]

and applies the bivariate integer small-root method to the primitive
polynomial

\[
\frac{(2^kx+P_0)(2^ky+Q_0)-N}{2^k}.
\tag{44}
\]

The source also iterates over the possible bit length of \(P\). Our promised
smaller factor \(p\) is a valid choice for \(P\), so the theorem applies
without supplying an extra hidden size parameter.

## 6. Direct arithmetic-progression terminal

Suppose \(t=k-L\ge1\), where \(L=(\log n)^{O(1)}\), and suppose an oracle
returns \(h\bmod2^t\). Section 3 computes

\[
p_t=p\bmod2^t,
\qquad 0\le p_t<2^t.
\tag{45}
\]

Put

\[
m=2^t,
\qquad s=p_t.
\tag{46}
\]

The hypotheses of Gao--Feng--Hu--Pan 2025, Theorem 3.1, with \(r=1\),
hold directly:

\[
\gcd(m,N)=1,
\qquad 1\le s<m<N,
\qquad p\equiv s\pmod m,
\qquad p\mid N.
\tag{47}
\]

Here \(s\ge1\) because it is odd, and \(m<N\) because
\(t\le k<(\log_2N)/4<\log_2N\). The cited deterministic algorithm finds
the prime divisor \(p\) in

\[
O\!\left(
\left\lceil\frac{N^{1/4}}m\right\rceil
\log^{7+3\epsilon}N
\right)
\tag{48}
\]

bit operations for any fixed \(\epsilon>0\). It is Theorem 3.1, rather than
Corollary 3.2, that applies: only the selected prime \(p\), not every prime
divisor of \(N\), is asserted to lie in the class \(s\bmod m\).

Let \(\alpha=(\log_2N)/4\). Since \(k=\lfloor\alpha\rfloor\) and
\(t=k-L\),

\[
\frac{N^{1/4}}m
=2^{\alpha-t}
=2^{\alpha-k+L}
<2^{L+1}.
\tag{49}
\]

Thus (48) is numerical QP. Verify the returned divisor by checking
\(1<p<N\) and \(p\mid N\). This proves the carry-to-factoring direction of
Theorem 4 without enumerating the missing bits. The reverse direction is
the polynomial-time formula (10).

## 7. Independent Coppersmith terminal

The exact older low-bit theorem gives an independent derivation of the same
QP boundary. Starting again from (45), every residue modulo \(2^k\) whose
reduction modulo \(2^t\) is \(p_t\) has one unique representation

\[
p_{0,j}=p_t+j2^t,
\qquad 0\le j<2^{k-t}=2^L.
\tag{50}
\]

All these residues are odd because \(t\ge1\) and \(p_t\) is odd. For each
\(j\), compute the canonical value

\[
q_{0,j}=Np_{0,j}^{-1}\bmod2^k.
\tag{51}
\]

For the unique \(j=j_*\) satisfying

\[
p_{0,j_*}=p\bmod2^k,
\tag{52}
\]

equation (51) equals \(q\bmod2^k\). Therefore the data for this iteration
are exactly the low bits used in (43)--(44), and Coppersmith's Theorem 5
returns the factorization.

For an incorrect extension, the small-root routine has no promised output.
This causes no soundness issue. Accept an output \(d\) only after checking

\[
1<d<N,
\qquad d\mid N.
\tag{53}
\]

If a valid divisor is returned, orient the factors by taking
\(p=\min(d,N/d)\). If no valid divisor is returned, continue to the next
extension. The correct extension guarantees termination.

There are \(2^L\) iterations. The primary theorem has polynomial bit cost
per iteration, as do modular inversion and exact verification. Hence this
independent post-oracle cost is

\[
2^L\operatorname{poly}(n)
=2^{(\log n)^{O(1)}}.
\tag{54}
\]

One numerical-QP call to a truncated-carry evaluator, followed by either
the direct bound (48) or the independent bound (54), is still numerical QP.

## 8. What the reduction does not prove

The construction computes \(z_t\), not \(h\). The difference between them
is precisely the unknown residue \(p^{-1}\bmod2^t\). Therefore F198 gives no
factoring algorithm unless another method supplies that residue or selects
its correct lifts.

The independent enumeration in Section 7 is QP only because the missing
precision is \(L=(\log n)^{O(1)}\), rather than a positive fraction of
\(n\). This is an
algorithmic sufficiency threshold, not a lower bound below that threshold.
In particular, the proof does not exclude a different succinct evaluator,
a gradual one-child lift, or a direct factoring algorithm.
