# F130 proof — termination and quasipolynomial cost

## 1. Public and deterministic construction

Every operation in the statement is public. The algorithm uses integer gcd,
exact division, exact perfect-power detection, modular multiplication,
modular inversion, exact integer square root, and binary linear algebra. It
uses no factor of \(N\), primality label for an endpoint, hidden prime row,
or advised word.

The seed order, block order, support order, exponent order, first-residue
rule, and first-exact-value rule are explicit. Use a fixed deterministic
complete gcd-free-basis algorithm with a fixed lexicographic split schedule.
Therefore the full transcript is a deterministic function of \(N\).

After the initial gcd screens, every seed endpoint is a unit modulo \(N\).
Each initial named block divides a product of seed endpoints, so it is also a
unit. Every later named block divides an earlier named block. Thus every word
residue is a unit and its canonical inverse exists.

## 2. The two bases have different invariants

Let \(\mathcal B_t\) be the named generator basis. By construction, each new
named block occurs in the exact exponent presentation of an old named block.
It therefore divides an old named block. Inductively, every named block is a
descendant of \(A_0\).

The final P66 decoder basis has no such restriction. A relation value
\(P(c)=cw\) can contain a prime that divides no initial endpoint. P66 must
retain this information to compute the exact parity kernel, but that decoder
block is not inserted into a later word menu. This separation is what makes
the named-stage bound valid.

## 3. Frozen scanning is necessary and sufficient

The basis does not change during a stage. Therefore the declared finite menu
is well-defined and its lexicographic scan is exhaustive.

It would not be lossless to restart when the first split appears. If an old
block has a nontrivial exponent presentation on its descendants, an old word
with exponent \(e\le E\) can require a descendant exponent larger than \(E\).
The remaining old positions therefore need not occur in the new capped
menu. The algorithm avoids this problem by collecting every old-stage
endpoint and relation before it applies the batch refinement.

Within one frozen stage, two word positions with the same canonical residue
\(c\) have the same canonical inverse \(w\), the same endpoints, the same
direct screens, and the same exact relation value \(cw\). Keeping only their
first word is therefore lossless for all declared operations.

The same statement is false for exact relation values. The integer \(P\)
does not determine its endpoint presentation. For example,

\[
N=35,
\qquad
P=36=1+N
\]

has the unit endpoint pairs

\[
(2,18),\ (3,12),\ (4,9),\ (6,6).
\]

They give the same exact relation value but can have different gcds with an
old named block. Hence every distinct residue endpoint pair is inserted into
the exposure batch before the relation ledger removes duplicate \(P\)'s.

After endpoint insertion, exact-value deduplication is lossless for P66.
Two equal values give equal parity columns. Their difference vector is a
kernel vector whose exact product is \(P^2\), whose positive root is \(P\),
and whose residue is

\[
P\equiv1\pmod N.
\]

Thus the duplicate direction has global normalized root \(+1\). Every other
kernel direction projects to the matrix with one copy retained. Removing all
but the first exact copy preserves the normalized-root image.

## 4. Full gcd-free refinement detects multiplicity splits

Apply complete gcd-free refinement to the old named blocks and all frozen
stage endpoints. It gives pairwise-coprime terminal bases \(h_j\) and exact
nonnegative exponent coordinates for every input. A terminal \(h_j\) is
named exactly when it occurs in an old named block's coordinate vector.
Such an \(h_j\) divides that old block; a terminal basis supported only on
probe cofactors is discarded from the named state.

This is stronger than one gcd per old block. In the example \(6,12\), a
complete gcd-free basis is \(2,3\), with

\[
6=2\cdot3,
\qquad
12=2^2\cdot3.
\]

It detects the multiplicity difference even though the first gcd is the
whole old block. Exact maximal-root extraction then makes every named block
perfect-power-free. Roots of pairwise-coprime integers remain pairwise
coprime.

Suppose the normalized new named basis differs from the old basis. Each old
block is a monomial in the new pairwise-coprime blocks. If an old block used
only one new block \(h\), it would have the form \(h^a\). The old block is
perfect-power-free, so \(a=1\), and maximal-root normalization gives the same
block. Therefore any genuine change expresses some old block using at least
two new named blocks. A strict stage increases the named block count by at
least one.

## 5. The number of stages is quasipolynomial

Put

\[
\Lambda_0=\lceil\log _2(A_0+1)\rceil.
\]

There are at most \(E\) seed pairs because

\[
H-1\le E.
\]

Every seed and inverse endpoint is smaller than \(N\). Hence

\[
\Lambda_0\le 2nE=2^{O(L^2)}.
\]

All named blocks are pairwise coprime integers greater than one and descend
from \(A_0\). Their product divides \(A_0\). Consequently

\[
2^{M_t}\le\prod_{q\in\mathcal B_t}q\le A_0.
\]

Therefore

\[
M_t\le\log_2 A_0<\Lambda_0=2^{O(L^2)},
\qquad
\log_2 M_t=O(L^2).
\]

Every nonterminal stage increases \(M_t\). Thus there are at most

\[
1+\lfloor\log _2 A_0\rfloor=2^{O(L^2)}
\]

frozen scans, including the final scan with no split.

## 6. Number of word positions

At a stage with \(M=M_t\) named blocks, the number of positions is

\[
W(M)=\sum_{s=0}^{\min(D,M)}\binom Ms E^s.
\]

Using \(\log_2M=O(L^2)\),

\[
W(M)
\le(D+1)(ME)^D.
\]

Since \(D=L^2\) and \(\log_2E=L^2\),

\[
\begin{aligned}
\log_2W(M)
&\le \log_2(D+1)+D(\log_2M+\log_2E)\\
&=O(L^2(L^2+L^2))\\
&=O(L^4).
\end{aligned}
\]

Therefore

\[
W(M)=2^{O((\log n)^4)}.
\]

Multiplying by \(2^{O(L^2)}\) stages does not change this class. If \(Q\) is
the total number of processed first residues and \(R\) the number of
retained distinct exact values, including the seed values, then

\[
Q,R\le2^{O((\log n)^4)}.
\]

## 7. Seed cost, per-record arithmetic, and provenance

The seed phase has at most \(E=2^{O(L^2)}\) positions. Its gcds, inverses,
direct screens, endpoint storage, initial gcd-free refinement, and exact
perfect-power normalization are polynomial in its explicit
\(O(nE)=2^{O(L^2)}\)-bit transcript.

A word exponent has

\[
\log_2(E+1)=O(L^2)
\]

bits. A record has at most \(D=L^2\) block indices, each using
\(O(\log M)=O(L^2)\) bits, and at most \(D\) exponents. Its word provenance,
including its stage number, uses

\[
O(D(\log M+\log E))+O(\log\Lambda_0)=O(L^4)
\]

bits.

Repeated squaring computes one canonical word residue with
\(O(D\log E)=O(L^4)\) modular multiplications. Modular inversion and the two
direct gcds have polynomial cost in \(n\). The canonical endpoints satisfy

\[
1\le c,w<N,
\]

and every exact relation satisfies

\[
1\le P(c)=cw<N^2.
\]

Thus endpoint and relation values have \(O(n)\) bits. The full retained
source transcript, including provenance, has

\[
Q\,O(n+L^4)=2^{O(L^4)}
\]

bits.

At each stage, complete gcd-free refinement and exact perfect-power
normalization are polynomial in the total explicit endpoint bit length.
That length is at most \(2^{O(L^4)}\). Raising it to any fixed polynomial
power remains \(2^{O(L^4)}\). Multiplication by the
\(2^{O(L^2)}\) stage count is absorbed by the same bound.

## 8. Final P66 cost

The final P66 input consists of \(R\) integers below \(N^2\), each with the
known modular square residue \(1\). Its explicit input length is

\[
O(Rn)=2^{O(L^4)}.
\]

P66 computes its gcd-free decoder basis, parity matrix, and a complete binary
kernel basis in time polynomial in this explicit length. The decoder basis
can have quasipolynomially many blocks; this does not affect the named-stage
bound because it is never used as a generator basis.

There are at most \(R\) kernel-basis vectors. For each one, the selected exact
product has at most \(O(Rn)\) bits. Exact multiplication, square root, and the
two terminal gcds for all basis vectors have cost polynomial in \(Rn\), hence

\[
2^{O(L^4)}.
\]

Testing a basis is complete. The normalized-root map is a homomorphism from
the parity kernel to the square roots of one modulo \(N\), modulo global
sign. If its image is nonzero, some vector in every kernel basis has nonzero
image. There is no need to enumerate all kernel subsets.

The final ledger contains every earlier retained relation. Any earlier
dependency extends by zero on later columns, with the same exact product and
root. Therefore one final P66 run is sufficient. Re-running P66 after every
append or split would remain quasipolynomial, but it cannot improve the final
completeness claim.

Combining the seed phase, source, refinement, storage, and final decoder
bounds proves the uniform deterministic bit complexity

\[
\boxed{2^{O((\log n)^4)}}.
\]

## 9. Source inclusions and their boundary

The enlarged seed bank contains the original seeds \(2,\ldots,n\). For any
fixed constant \(C\), take \(n\) sufficiently large that \(L\ge C\). Then

\[
\log_2(n^C)=C\log_2n\le CL\le L^2=\log_2E.
\]

Also \(n^C<N-1\) for all sufficiently large \(n\). Therefore

\[
\{2,\ldots,n^C\}\subseteq\{2,\ldots,H\}.
\]

Thus the F130 seed phase contains every fixed polynomially bounded seed bank
eventually. Its first frozen stage exhausts every support-\(D\),
exponent-\(E\) word on the actual enriched basis \(\mathcal B_0\). This does
not assert containment of the word menu that a smaller sub-bank would have
produced on its own basis.

There is no unconditional literal inclusion of every old C116/F26-Q word
record built on the narrower \(2,\ldots,n\) endpoint basis. Extra seed
endpoints can refine one narrow block into many enriched named blocks. An old
word with small narrow-basis support can then require more than \(D\) blocks
after expansion. The old exact record is included only when its enriched
presentation meets the new caps.

This limitation does not make later stages redundant. If refinement replaces
an enriched block by proper named descendants, a bounded word in one
descendant need not have a word representation inside the previous capped
menu. P106 says that refinement cannot improve the decoder on already frozen
relation values. It does not say that the new named grammar cannot generate
new relation values.

## 10. Missing success theorem

The proof establishes only a well-defined terminating deterministic source
and its quasipolynomial cost. It does not prove that any stage has a strict
split. A split alone is also not a factor. It does not prove that the final
relation matrix has a dependency, or that any dependency has a non-global
root.

To obtain a factoring algorithm, one must prove that every surviving odd
composite non-perfect-power input satisfies at least one of these two events:

1. a declared direct screen returns a proper divisor; or
2. the final P66 normalized-root image is nonzero modulo
   \(\{+1,-1\}\).

That all-input source-and-root statement is the exact remaining gate.
