# F196 hostile audit

Verdict: **PASS**.

The verdict reads Andreica's algorithm with four necessary source errata.
The displayed formulas are false if their plus signs and self-referential
valuation index are read literally. The corrected formulas are uniquely
forced by the definitions. An independent reconstruction confirms that the
corrections preserve the published bit bounds.

## 1. Frozen-input integrity

All four hashes declared in *MANIFEST.md* match the files on disk.

| frozen input | declared and observed SHA-256 |
|---|---|
| *STATEMENT.md* | 07d2bccb9f508248a44f39faba3bd13a87cc0b2a1bc3dafa1464c348ae871c5c |
| *PROOF.md* | 9f6e71c1c69661ad62780f0864b8fa460bd43df9f262b2774b7d231d20bba19b |
| *SELF_AUDIT.md* | 4120ee13f7fbeef46620e2c07b269fe162d6a17d5cdc5d0e6d710997027242d6 |
| *PROVENANCE.md* | c4f6d7a89f1f6e2e146a789063afe23265a235c44439385e79434e9a5064d889 |

The observed hash of the manifest itself is
df70590eae86b041948211d5adc545cd17d1be03e598fa1f3cd1e0924701d130.
The manifest does not declare itself as a frozen input.

## 2. Primary-source audit

I read the complete primary article, including Sections 1--11 and every
displayed formula:

Mugurel Ionut Andreica, “A Fast Algorithm for Computing Binomial
Coefficients Modulo Powers of Two,” *The Scientific World Journal* 2013,
Article 751358, DOI
[10.1155/2013/751358](https://doi.org/10.1155/2013/751358), PMCID
[PMC3856163](https://pmc.ncbi.nlm.nih.gov/articles/PMC3856163/).

The complete archival XML came from the Europe PMC full-text service. Its
observed SHA-256 was
de018435a2556ebc9d93d225d425ca643d03f050de95bb1cda948e31a78430b0.

The abstract and Sections 1, 7, and 8 support exactly the premise used by
F196. For precision \(T\), uniform preprocessing costs

\[
O\!\left(T^3\mathsf M(T)+T^4\right).
\]

One query with \(0\le Q\le P\le 2^T-1\) then costs

\[
O\!\left(T^2\log T\,\mathsf M(T)\right).
\]

The source uses \(N\) where F196 uses \(T\). Its Section 9 large-index
extension is not needed by F196.

### Source errata

1. **Equation (25) uses the wrong operation.** The source displays

   \[
   \operatorname{FODD}(P)
   =\operatorname{FFODD}(P,1)+\cdots+\operatorname{FFODD}(P,K).
   \]

   It must say

   \[
   \operatorname{FODD}(P)
   =\prod_{i=1}^{K}\operatorname{FFODD}(P,i)\pmod {2^T}.
   \tag{S25}
   \]

   The binary blocks in the preceding paragraph partition the odd integers
   in \([1,P]\). Each FFODD is the product within one block. Therefore their
   product, not their sum, is FODD.

2. **Equation (29) uses the wrong operation and suppresses an integer
   floor.** The source displays

   \[
   F_2(P)=\operatorname{FODD}(P)+F_2(P/2).
   \]

   From

   \[
   P!=
   \left(\prod_{\substack{1\le j\le P\\j\ {\rm odd}}}j\right)
   2^{\lfloor P/2\rfloor}\lfloor P/2\rfloor!,
   \]

   the required recurrence is

   \[
   F_2(P)=\operatorname{FODD}(P)
          F_2(\lfloor P/2\rfloor)\pmod {2^T}.
   \tag{S29}
   \]

3. **The Section 3 valuation recurrence repeats the current index.** Let

   \[
   U=v_2(2^P-X-Q+1),\qquad V=v_2(Q).
   \]

   The printed right side contains \(\operatorname{Exp}_2(P,X,Q)\). The
   correct recurrence is

   \[
   \operatorname{Exp}_2(P,X,Q)
   =\operatorname{Exp}_2(P,X,Q-1)+U-V.
   \tag{SV}
   \]

   This follows by taking \(v_2\) in

   \[
   \binom{2^P-X}{Q}
   =\binom{2^P-X}{Q-1}\frac{2^P-X-Q+1}{Q}.
   \]

   The printed recurrence is self-referential and cannot be an algorithm.

4. **Equation (17) omits floors in Legendre's formula.** The intended
   valuation is

   \[
   v_2(Q!)=
   \sum_{k=1}^{\lfloor\log_2 Q\rfloor}
   \left\lfloor\frac{Q}{2^k}\right\rfloor.
   \tag{SL}
   \]

   The displayed unfloored sum is not generally an integer. The later
   precision argument uses the standard floored valuation and
   \(v_2(Q!)\le Q-1\).

These are local transcription errors. Equations (S25), (S29), (SV), and
(SL) are forced by definitions on the same pages. Replacing addition by
modular multiplication adds no new asymptotic cost. Replacing \(Q\) by
\(Q-1\), adding floors, and taking integer halves also leaves every bound
unchanged.

### Independent reconstruction of the source premise

The main-range algorithm remains valid after these corrections.

- Sections 2--3 compute small and large binomial tables. The corrected
  valuation recurrence separates powers of two from odd, invertible parts.
- Section 4 computes power sums by splitting \([1,2^P]\) into two halves and
  applying the binomial theorem.
- Section 5 uses Newton's identity

  \[
  Qe_Q=\sum_{k=1}^{Q}(-1)^{k-1}e_{Q-k}p_k.
  \]

  Division by \(Q\) loses exactly \(v_2(Q)\) bits. Thus the stored precision
  is \(T-v_2(Q!)>T-Q\).
- Section 6 always multiplies that truncated \(e_Q\) by \(2^Q\). The lost
  precision cannot affect a residue modulo \(2^T\).
- Section 7 evaluates products of odd integers in binary blocks. It then
  applies (S29) through at most \(T\) halvings.
- Section 8 combines the three odd factorial parts with

  \[
  2^{v_2(P!)-v_2(Q!)-v_2((P-Q)!)}.
  \]

All stored modular values have \(T\) bits. Preprocessing performs
\(O(T^3)\) such multiplications and \(O(T^3)\) such additions. This gives
\(O(T^3\mathsf M(T)+T^4)\) bit operations. A query performs
\(O(T^2\log T)\) modular multiplications. The tables depend only on \(T\).
Thus the preprocessing is uniform. Storing \(O(T^3)\) residues also uses
only polynomial space. F196 does not treat preprocessing as free advice.

## 3. Direct parameter substitution and bit complexity

Put \(T=n\), \(P=N-1\), and \(Q=B\). From

\[
n=\lceil\log_2(N+1)\rceil
\]

we get

\[
N+1\le2^n,\qquad N-1\le2^n-2<2^n.
\]

Also \(0\le B\le N-1\). Therefore

\[
0\le B\le N-1\le2^n-1.
\]

This is exactly Andreica's main range. Computing \(n\), \(N-1\), and
\(B=\lfloor\sqrt N\rfloor\) has polynomial bit cost. Including uniform
preprocessing, the total bound is

\[
O\!\left(n^3\mathsf M(n)+n^4+
n^2\log n\,\mathsf M(n)\right).
\]

It is polynomial in the input bit length. No Section 9 extension is hidden
in the substitution.

## 4. Independent Lucas proof

Since \(p<\sqrt N<q\),

\[
p\le B<q.
\]

The promise \(q<2p\) gives \(B<2p\). Write

\[
B=p+r,\quad 0\le r<p,\qquad
q=p+d,\quad 1\le d<p.
\]

Modulo \(q\), all denominators \(1,\ldots,B\) are units. Hence

\[
C=\prod_{j=1}^{B}\frac{N-j}{j}\equiv(-1)^B\pmod q,
\]

and \(A\equiv1\pmod q\).

In base \(p\),

\[
N-1=1\cdot p^2+(d-1)p+(p-1),\qquad
B=0\cdot p^2+1\cdot p+r.
\]

Lucas' theorem gives

\[
C\equiv(d-1)\binom{p-1}{r}
\equiv(d-1)(-1)^r\pmod p.
\]

Because \(p\) is odd, \((-1)^B=-(-1)^r\). Therefore

\[
A\equiv1-d\equiv1-q\pmod p.
\]

The same congruence holds modulo \(q\), since
\(1-q\equiv1\pmod q\). The primes are distinct, so CRT gives

\[
A\equiv1-q\pmod N.
\]

Thus \(h=(A-(1-q))/N\) is an integer and \(q=1+hN-A\) is exact.

## 5. Both one-query reductions

Suppose a carry oracle returns \(H=h\bmod2^n\). Andreica gives
\(C_n=C\bmod2^n\) in polynomial time. Then

\[
Q_0=\left(1+HN-(-1)^BC_n\right)\bmod2^n
\equiv q\pmod{2^n}.
\]

The canonical residue is the exact factor because

\[
0<q<N<N+1\le2^n.
\]

This is a deterministic polynomial-time, one-query reduction from factoring
to the carry problem.

Conversely, suppose a factoring oracle returns \(q\). The odd integer \(N\)
is a unit modulo \(2^n\). From \(hN=q-1+A\),

\[
h\equiv
N^{-1}\left(q-1+(-1)^BC_n\right)\pmod{2^n}.
\]

This is the reverse deterministic polynomial-time, one-query reduction.
Adding or deleting the already polynomial-time coordinate \(C_n\) gives the
same equivalence for the joint residue problem. Polynomial overhead
preserves numerical-QP time in both directions.

## 6. Signed Euclidean quotient: both parities

If \(B\) is even, then \(A=C>0\) and

\[
C\equiv N+1-q\pmod N.
\]

Write \(C=JN+(N+1-q)\). Then \(h=J+1\), so

\[
\left\lfloor\frac AN\right\rfloor=J=h-1.
\]

If \(B\) is odd, then \(A=-C<0\) and \(C\equiv q-1\pmod N\). Write

\[
C=JN+(q-1).
\]

Then \(h=-J\), while

\[
\left\lfloor\frac AN\right\rfloor
=\left\lfloor-J-\frac{q-1}{N}\right\rfloor
=-J-1=h-1.
\]

In both cases,

\[
A\bmod N=N+1-q,\qquad 0<N+1-q<N.
\]

Thus F196 correctly uses floor division. Truncation toward zero would be
wrong when \(B\) is odd.

## 7. Mixed-modulus equivalence

Let \(a_t=A\bmod(N2^t)\) be canonical. For some integer \(k\),

\[
A=a_t+kN2^t.
\]

Divide by positive \(N\) and take floors:

\[
h-1=\left\lfloor\frac{a_t}{N}\right\rfloor+k2^t.
\]

Therefore

\[
h\equiv1+\left\lfloor\frac{a_t}{N}\right\rfloor\pmod{2^t}.
\]

Reduction modulo \(N\) also gives

\[
a_t\bmod N=N+1-q,\qquad
q=N+1-(a_t\bmod N).
\]

Thus the mixed residue directly factors \(N\). In the reverse direction,
a known \(q\) supplies

\[
A\equiv1-q\pmod N,\qquad
A\equiv(-1)^BC_n\pmod{2^n}.
\]

Since \(\gcd(N,2^n)=1\), CRT reconstructs the unique
\(A\bmod(N2^n)\) in polynomial time. The mixed-residue problem and factoring
are polynomial-time interreducible on the promise.

## 8. Boundary and nonclaim

For \(1\le j\le B\),

\[
\frac{N-j}{j}\ge\frac{N-B}{B}\ge B-1.
\]

Thus \(C\ge(B-1)^B\). Together with \(C\le2^{N-1}\), this gives exact
output length \(2^{\Theta(n)}\). This blocks materialization only. It does
not block a succinct modular algorithm.

F196 proves an equivalence on the balanced-semiprime promise. It does not
prove a lower bound for factoring, the carry, or mixed-modulus binomial
evaluation. The frozen statement preserves this distinction.
