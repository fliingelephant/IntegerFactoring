# F141 proof — compact lifts, bridge equivalence, and large-block reuse

## 1. Compact factor-free decoding

Collect every named integer atom that occurs in a retained monomial and every
canonical inverse endpoint \(w_i\).  Complete multiplicity-aware gcd-free
refinement and maximal perfect-power extraction produce pairwise-coprime
integers \(h_1,\ldots,h_s>1\) and exact nonnegative presentations

\[
U_iw_i=\prod_{j=1}^s h_j^{a_{ji}}.
\tag{1}
\]

After maximal extraction, the gcd of the rational-prime valuations inside
each \(h_j\) is one.  Since different \(h_j\)'s are coprime, the product
selected by \(z\in\mathbf F_2^R\) is an integer square if and only if

\[
\sum_i z_i a_{ji}\equiv0\pmod2
\qquad(1\le j\le s).
\tag{2}
\]

Necessity follows by taking a prime of odd valuation in each power-free
block.  Sufficiency is immediate.

For a vector satisfying (2), put

\[
E_j=\sum_i z_i a_{ji}.
\]

The exact positive root is \(\prod_jh_j^{E_j/2}\).  The terminal gcd only
needs its residue modulo \(N\), which repeated squaring computes directly
from the encoded exponents.  Every atom is a unit unless an earlier gcd has
already factored \(N\).  Since every selected lifted value is one modulo
\(N\), the computed residue squares to one.  This proves correctness of the
compact P66 decode.

Complete gcd-free refinement is polynomial in the total atom bit length.
The parity matrix and its full binary kernel basis are polynomial in the
explicit relation-vector transcript.  Each modular power is polynomial in
\(n+\log(E_j+1)\).  Thus the compact decoder is polynomial in its encoded
input.

For the literal F130 bounds, a word has at most \(D=L^2\) atoms, each below
\(N\), and each exponent is at most \(E=2^{L^2}\).  Hence

\[
\log_2U\le DEn=2^{O(L^2)}.
\tag{3}
\]

F130 enumerates \(2^{O(L^4)}\) word positions over all frozen stages.
Retaining one exponent vector and one \(n\)-bit inverse per position, or even
expanding (3), therefore uses \(2^{O(L^4)}\) bits.  Every later operation is
polynomial in that transcript.  This proves the declared cost.

## 2. Bridge equivalence

Fix one position and abbreviate

\[
A=cw,\qquad B=Uw,\qquad D=Uc.
\]

Then

\[
AB=Uc\,w^2=Dw^2.
\tag{4}
\]

Thus the exact square-class column of \(D\) is the sum of those of \(A\) and
\(B\).  Also \(D\equiv c^2\pmod N\), so \(c\) is its supplied modular square
root.

In a ledger containing \(A\), replacing \(B\) by \(D\) is the invertible
binary change of variables \(D=A+B\).  If a selected product containing
\(D\) is square, equation (4) says that the corresponding selected product
containing \(A,B\) has an exact root larger by the factor \(w\).  Its supplied
modular root changes from \(c\) to one.  Since \(w=c^{-1}\pmod N\), the
normalized roots are equal.  Applying this independently at every word
position proves the bridge theorem.

The finite certificates below show that \(B\) is not determined by the
canonical column \(A\) alone.  Therefore this is a strict source expansion,
although (4) identifies it with an ordinary square-congruence source.

## 3. Same-residue collision

Equal parity presentations give integers \(d,a,b\) with

\[
U=da^2,\qquad V=db^2.
\]

Every named atom is a unit, so \(d,a,b\) are units modulo \(N\).  If
\(U\equiv V=c\), then

\[
a^2\equiv b^2\pmod N.
\tag{5}
\]

With \(w=c^{-1}\pmod N\), direct multiplication gives

\[
(Uw)(Vw)=d^2a^2b^2w^2=(dabw)^2.
\tag{6}
\]

Since \(c=da^2\), reduction of the positive root gives

\[
dabw\equiv dab(da^2)^{-1}\equiv ba^{-1}\pmod N.
\tag{7}
\]

Equation (5) proves that (7) is a square root of one.  It is non-global
exactly when \(a-b\) and \(a+b\) split different CRT components.  This proves
the lemma.

## 4. Squared-anchor theorem

Put \(A=n^3\), assume \(n\ge64\), and let
\(q\ge N/(12n)\) be a named unit block.

### 4.1 The positions are in the source

Write \(L=\lceil\log_2(n+1)\rceil\) and \(E=2^{L^2}\).  In the declared
range,

\[
3\log_2n<L^2,
\]

so \(A<E\).  Every prime \(\ell\le A\) occurs as an initial F130 seed and,
on the no-factor branch, as its own prime named block.  Also
\(N/(12n)>A\) in this range, so \(q\ne\ell\).  Before forming the word, test
\(\gcd(\ell,N)\) and \(\gcd(\ell,q)\).  A nontrivial first gcd factors
\(N\); a nontrivial second gcd strictly splits \(q\).  On the remaining
branch \(\ell\) is an eligible named prime block coprime to \(q\), and
\(q\ell^2\) is an allowed support-two, exponent-two frozen word.

Inputs below the fixed threshold can be completely handled by fixed finite
trial division.  No asymptotic claim depends on their source transcript.

### 4.2 Distinct residues and few bad inverses

For distinct primes \(\ell,m\le A\), equality of the residues would give

\[
N\mid q(\ell^2-m^2).
\]

Because \(q\) is a unit, this implies \(N\mid\ell^2-m^2\).  But

\[
0<|\ell^2-m^2|<A^2<N,

\]

a contradiction.  Thus all \(c_\ell\), and hence all \(w_\ell\), are
distinct.

There are exactly \(\lfloor(N-1)/q\rfloor\) positive multiples of \(q\)
below \(N\).  Consequently

\[
\#\{\ell:q\mid w_\ell\}
\le\left\lfloor{N-1\over q}\right\rfloor
<{N\over q}\le12n.
\tag{8}
\]

If \(1<\gcd(q,w_\ell)<q\), complete refinement has already strictly split
\(q\).  On the declared no-split branch, every inverse not counted in (8) is
coprime to \(q\).

### 4.3 Deduplication capacity

Let \(\mathcal G\) be the good anchor primes.  The elementary bound already
proved in P126 gives

\[
\vartheta(x)>\frac6{25}x\qquad(x\ge2^{18}).
\]

The product of the distinct primes excluded because they divide \(Nq\) is
less than \(Nq<N^2\), so their total logarithmic mass is below
\(2\log N\).  Removing those primes and the fewer than \(12n\) bad inverses
from (8) gives

\[
M:=\sum_{\ell\in\mathcal G}\log\ell
>\frac6{25}n^3-2\log N-36n\log n
>\frac15n^3.
\tag{9}
\]

Using \(\log N<n\log2\), the last inequality follows from

\[
\frac{n^2}{25}>2\log2+36\log n.
\]

This holds at \(n=64\), and its margin increases thereafter.

Partition \(\mathcal G\) by equality of the lifted exact values

\[
B_\ell=q\ell^2w_\ell.
\]

For one equality class \(C\), the integer

\[
T=B_\ell/q=\ell^2w_\ell
\]

is independent of \(\ell\in C\).  The anchor primes are distinct, so

\[
\prod_{\ell\in C}\ell^2\mid T.
\]

Since \(w_\ell<N\) and \(\ell\le A\),

\[
2\sum_{\ell\in C}\log\ell
\le\log T
<2\log A+\log N.

\]

Hence every class has logarithmic anchor mass less than

\[
H=\log A+\frac12\log N
<3\log n+\frac12n\log2<n.
\tag{10}
\]

Equations (9) and (10) show that the number of distinct exact values is more
than

\[
{M\over H}>{n^2\over5}.
\tag{11}
\]

Global deletion cannot reduce this number.  If one of these exact integers
was retained earlier, that earlier column is the same integer and has the
same parity rows.

### 4.4 Simultaneous row preservation

For a good anchor, \(\gcd(q,w_\ell)=1\) and
\(\gcd(q,\ell)=1\).  Therefore every prime \(r\mid q\) satisfies

\[
v_r(B_\ell)=v_r(q).
\]

Every row with odd \(v_r(q)\) occurs oddly in every one of the more than
\(n^2/5\) distinct values from (11).  This proves the squared-anchor theorem.
Also \(U_\ell=q\ell^2<Nn^6\).  These particular lifted words have \(O(n)\)
bits explicitly, so their theorem does not depend on compact storage.

## 5. Certificate arithmetic

For the large certificate, proof arithmetic verifies the primality of

\[
p=1238926361552897,\qquad q=5704689200685129054721

\]

and the divisibilities \(p\mid2^{256}+1\) and
\(q\mid2^{256}-1\).  Hence \(2^{513}\equiv2\pmod{pq}\).  Both words have
inverse \(w=(N+1)/2\).  Their exponent parity is odd, so Section 3 applies
with \(d=2,a=1,b=2^{256}\).  The displayed root and gcds follow.

The small-corpus ranks, exact squares, root residues, direct screens, and
aggregate counts are reproduced by the registered `search.py`.  Its hidden
prime factors are used only to certify the finite normalized-root labels.

## 6. What is not proved

The bridge identity shows that F141 is a standard relation-lattice source.
The same-residue theorem reduces to bounded order finding.  The squared
anchor theorem forces many common rows, but gives no upper bound on the rank
contributed by the distinct cofactors \(w_\ell\).  A unitriangular or
hyperforest support pattern remains compatible with every theorem above.
No all-input rank or root conclusion follows.
