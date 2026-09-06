# F141 hostile audit — PASS

## Verdict

**PASS.** I found no counterexample to the compact decoder, bridge
equivalence, same-residue lemma, squared-anchor theorem, registered fixed
certificate, or finite-search claims.

The result remains a source and decoder theorem. It does not prove a parity
dependency, a non-global root for every input, or an integer-factoring
algorithm.

## Frozen inputs

I audited these bytes without changing them.

| Artifact | SHA-256 |
|---|---|
| `QUESTION.md` | `0d1460de3c7f50fc221e6119cc4421996b9e3eba89f4ec8e1b5d3d6ae5a82583` |
| `PREREGISTRATION.md` | `63d4daa7917fad62c5b207a52c3e820016d03a59bf797315cf1917374c4cf02d` |
| `STATEMENT.md` | `64bf45085bfef91190be4e23021e5e4bebbc6a9f48e03db56e49b087cf2b4bcf` |
| `PROOF.md` | `e0cea48fc14328f63c23d5ce56385cd6a216042da1f8e6c00bd2efe81914ae5a` |
| `search.py` | `036e985399fd9e312a5f0f07de5dfe81400587ae56ce13833ad13fc77b306869` |
| `OUTPUT.json` | `c127a1a9c0a206aa7cc2d2d4285abb4791d37cf2ac8757b7b142a0ff42022ae3` |
| `RUN.log` | `c127a1a9c0a206aa7cc2d2d4285abb4791d37cf2ac8757b7b142a0ff42022ae3` |
| `OUTPUT_V1.json` | `63e762c245c62a1491a7f7c60c863a97f6e6a5e9a0d9a55a2363069753c820ad` |
| `RUN_V1.log` | `63e762c245c62a1491a7f7c60c863a97f6e6a5e9a0d9a55a2363069753c820ad` |
| `RUN_FAILED_SANDBOX.log` | `770e06cc5187c8faab3d138bfe3d32a5c2918ea1489ff297013893db0efcf2e2` |
| `RUN_FAILURE.md` | `a1afeee1921acffe646120410c0b9b483ab0acf79d905c5c0741c1c876bfd454` |
| `MANIFEST.md` | `9213229a2c28939fc188961aea98a87009e150319d9965d982289fd5565bbe13` |

The requested statement and proof hashes match exactly. The manifest's
listed hashes also match their files. `RUN.log` and `OUTPUT.json` are
byte-identical, as are the two V1 files.

## 1. Compact factor-free decoder

The square criterion is exact. Joint multiplicity-aware gcd-free refinement
gives pairwise-coprime blocks. Maximal perfect-power extraction makes the gcd
of the rational-prime valuations within each block equal to one. Therefore
each block has at least one prime of odd valuation.

For a selected product, an odd total exponent on a block makes that prime's
total valuation odd. Conversely, even total exponents make every rational
prime valuation even. Thus

\[
\prod_i (U_iw_i)^{z_i}\text{ is a square}
\quad\Longleftrightarrow\quad
\sum_i z_i a_{ji}=0\pmod 2\text{ for every block }j.
\]

No rational factorization is assumed. Gcd-free refinement, exact
perfect-power extraction, binary linear algebra, and modular powering are
polynomial in the explicit encoded transcript.

Retaining every word position does not break the F130 cost. A position has
at most \(D=L^2\) named atoms, each below \(N\), and exponents at most
\(E=2^{L^2}\). Hence

\[
\log_2 U<DEn=2^{O(L^2)}.
\]

F130 already bounds all frozen word positions, not only first residues, by
\(2^{O(L^4)}\) over all stages. Multiplying the position count by the
expanded-word bound, or retaining the smaller exponent vectors, stays in
\(2^{O(L^4)}\). The final joint refinement and P66 decode are polynomial in
that transcript. The claimed total cost survives.

## 2. Bridge and normalized roots

For one position,

\[
A=cw,\qquad B=Uw,\qquad D=Uc,
\]

and

\[
AB=Dw^2,\qquad D\equiv c^2\pmod N.
\]

Thus replacing \(B\) by \(D=A+B\) in exact square-class coordinates is an
invertible binary column operation. The supplied modular root changes from
one to \(c\).

The normalized-root check also works in both nontrivial coefficient cases:

- old \(B\) corresponds to new \(A,D\), and \(AD=Bc^2\);
- old \(A,B\) corresponds to new \(D\), and \(AB=Dw^2\), with
  \(w\equiv c^{-1}\pmod N\).

These identities preserve \(R/X\pmod N\), so they also preserve every
multi-position normalized-root image.

This equivalence is presentation-aware on the bridge side. If two equal
integers \(D\) have different supplied roots \(c\), they must not be deleted
solely because their exact integers agree. F141 does not require that
deletion. Its actual canonical and lifted columns all have supplied root one,
so their exact-value duplicate directions have normalized root \(+1\) and
can be deleted safely.

## 3. Same-residue collision

Equal parity presentations give

\[
U=da^2,\qquad V=db^2.
\]

The common residue implies \(a^2\equiv b^2\pmod N\). Direct multiplication
gives the positive root \(dabw\), and

\[
dabw\equiv ba^{-1}\pmod N.
\]

This is non-global exactly when the signs of \(a\) and \(b\) differ across
CRT components. The two gcds of \(a-b\) and \(a+b\) then give the proper
split. The proof uses only that \(d,a,b\) are units. It does not assume that
\(d\), \(q\), or a named block is prime.

## 4. Literal squared-anchor positions

Let \(A=n^3\) and \(n\ge64\). Every prime \(\ell\le A\) is in the complete
initial F130 seed bank because

\[
3\log_2 n<L^2,\qquad A<E=2^{L^2},\qquad A<N-1.
\]

On the surviving seed branch, exact representation of the prime input
\(\ell\) forces \(\ell\) itself to be a named singleton block. Later named
refinement can split blocks but cannot merge it, so \(\ell\) remains present
in every later frozen basis.

Also,

\[
A^2=n^6<N,
\qquad
\frac{N}{12n}>A.
\]

Both inequalities hold at \(n=64\) from \(N\ge2^{n-1}\), and their margins
increase. Therefore a current block \(q\ge N/(12n)\) is different from every
anchor. The frozen named basis is pairwise coprime, and

\[
q\ell^2
\]

is a literal support-two F130 position with exponents \(1,2\le E\). F141's
source change processes this position even when an earlier word has the same
residue. Seed refinement does not remove the position.

This argument applies to a composite named block \(q\) as well as a prime
one. A prime anchor dividing \(N\) factors \(N\). A prime anchor properly
dividing \(q\) splits \(q\). Neither case is silently treated as an eligible
anchor.

## 5. Distinctness, bad inverses, and exact-value deletion

For different anchors \(\ell,m\le A\), equal residues would imply

\[
N\mid \ell^2-m^2,
\]

after cancellation of the unit \(q\). This is impossible because
\(0<|\ell^2-m^2|<A^2<N\). Inversion is a bijection on units, so the
\(w_\ell\) are also distinct.

There are exactly \(\lfloor(N-1)/q\rfloor\) positive multiples of \(q\)
below \(N\). Hence

\[
\#\{\ell:q\mid w_\ell\}
\le\left\lfloor\frac{N-1}{q}\right\rfloor
<\frac Nq\le12n.
\]

On the no-proper-split branch, a good inverse therefore has
\(\gcd(q,w_\ell)=1\), even when \(q\) is composite.

The imported P126 elementary estimate applies at \(A=n^3\ge2^{18}\):

\[
\vartheta(A)>\frac6{25}n^3.
\]

The excluded-prime logarithmic mass is below \(2\log N\), since the
squarefree product is at most \(\operatorname{rad}(Nq)\le Nq<N^2\). Removing
fewer than \(12n\) bad anchors costs less than
\(12n\log A=36n\log n\). Thus the good-anchor mass \(M\) satisfies

\[
M>\frac6{25}n^3-2\log N-36n\log n>\frac15n^3.
\]

The last step follows from

\[
\frac{n^2}{25}>2\log2+36\log n.
\]

At \(n=64\), its margin is greater than \(12.73\), and its derivative is
positive thereafter.

For an equality class of good lifted values, the common integer

\[
T=\ell^2w_\ell
\]

is divisible by the square of every distinct anchor in the class. Therefore
the class's logarithmic anchor mass is less than

\[
H=3\log n+\frac12\log N
<3\log n+\frac12n\log2<n.
\]

The last inequality has margin greater than \(29.34\) at \(n=64\) and an
increasing margin thereafter. The number of distinct exact values is
therefore strictly greater than

\[
\frac{M}{H}>\frac{n^2}{5}.
\]

Global exact-value deletion cannot merge two distinct integers. If one was
retained earlier, the retained column is the same integer and has the same
rational-prime valuations. Finally, for every good anchor,

\[
\gcd(q,\ell w_\ell)=1,
\qquad
v_r(q\ell^2w_\ell)=v_r(q)
\]

for every prime \(r\mid q\). All odd rows of \(q\) occur in every counted
value. This proves the stated simultaneous row preservation without a
primality assumption on \(q\).

## 6. Registered computation and fixed arithmetic

I ran the frozen source from a temporary directory under the registered
300-second wrapper and cache override. It completed in less than five
seconds. The replayed output and stdout were byte-identical to
`OUTPUT.json` and `RUN.log`.

I also recomputed the small corpus with an independent implementation. It
reproduced all authoritative counts:

| Quantity | Count |
|---|---:|
| Semiprimes | 903 |
| Slice-direct-null inputs | 178 |
| Canonical-global and lifted-non-global | 5 |
| Useful same-residue pairs | 3 |
| Useful one-column squares | 24 |
| Useful all-distinct weight-two or weight-three circuits | 0 |

The independent scan also reproduced the first category witness
\(7169=67\cdot107\), canonical rank/nullity \(18/0\), and lifted
rank/nullity \(14/2\). Direct calculation gives

\[
2^{24}\cdot6724=112810000384=335872^2,
\]

with terminal gcds \(67\) and \(107\).

For the fixed 123-bit certificate, Sage proof arithmetic and an independent
OpenSSL primality check both label

\[
p=1238926361552897,
\qquad
q=5704689200685129054721
\]

as prime. Direct integer arithmetic verifies all registered divisibilities,
caps, residues, inverse, screens, square identity, root reduction, and gcd
labels. In particular,

\[
E=2^{49},\quad p,q>E+1,\quad 513<E,
\]

\[
p\mid2^{256}+1,\qquad q\mid2^{256}-1,
\]

and the two terminal gcds are exactly \(q\) and \(p\), in that order.

The exact lifted value from \(U_2=2^{513}\) exceeds \(N^2\), while every
canonical F130 value is below \(N^2\). It is therefore a genuinely new exact
source value. The certificate does not assert that the complete canonical
F130 decoder is null.

The current circuit predicate is exact for weights two and three. Requiring
nonempty, pairwise-distinct parity supports excludes singleton dependencies
and equal-column pairs; together with zero total parity, this is equivalent
to minimal binary dependence in those weights.

## 7. Preserved history and prior compatibility

The first sandbox log fails during `import sage.all`, before any fixed
certificate or corpus item runs. `RUN_FAILURE.md` describes the same cache
write denial, and the corrected command changes only `DOT_SAGE`.

The V1 output's first alleged all-distinct pair at \(N=4033\) consists of
\(12100=110^2\) and \(16257024=4032^2\). It is a union of two singleton
squares, not a circuit. The current source rejects it and reports zero
all-distinct circuits, as required.

The obsolete V1 source file is not preserved, so the historical claim that
only the circuit test and labels changed cannot be replayed line by line.
This is a provenance limitation for the superseded run, not evidence used by
the current result. Its output, log, source hash, defect, and corrected
current run are all preserved.

The construction is consistent with the closest promoted results:

- P118/F130 bounds every frozen position and preserves prime seed singleton
  blocks, which validates literal inclusion and the cost composition.
- P120 requires presentation-dependent direct screens before deletion. F141
  does this and does not promote the unreduced \(U\) into the named grammar.
- P126 supplies the stated elementary \(6/25\) Chebyshev bound and covers its
  declared odd-row part of the complementary small-block region. F141 does
  not import a rank or root conclusion from it.

## Accepted boundary

The common \(q\)-rows can coexist with independent inverse-cofactor rows.
The resulting matrix can still be a full-rank forest. Nothing audited here
forces a parity kernel or a non-global normalized root on every input. The
exact remaining gate in the frozen statement is therefore unchanged.
