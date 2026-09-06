# F165 fixed-depth blind reconstruction V2

## Blind boundary and verdict

The SHA-256 of the only F165 source read for this reconstruction was

1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd

for V2_BLIND_STATEMENT.md, as required. I did not read another F165 file and
did not run a mathematical computation.

**Verdict: PASS for the fixed-depth cost theorem.** Here, as the ordered
decoder specification requires, “each square dependency” means each member of
the computed complete kernel basis. It does not mean all binary combinations
of that basis. This distinction is necessary and is audited below.

## Quantifiers and notation

Let \(N\) be the modulus. As in the public workflow, let

\[
n=\left\lceil\log_2(N+1)\right\rceil,
\qquad
L=\left\lceil\log_2(n+1)\right\rceil.
\]

Thus \(N<2^n\) and \(n<2^L\). The constants \(a,b,C\) do not depend on \(n\).
Write \(B_0\) for the total bit length of the explicit base transcript.
“Quasipolynomial” gives constants \(c_0,K_0\), independent of \(n\), such
that

\[
B_0\le 2^{K_0L^{c_0}}.
\]

For each fixed \(H\), the proof below gives constants \(c_H,K_H\) such that
the total time and peak space through layer \(H\) are at most
\(2^{K_HL^{c_H}}\). The constants can depend on \(H\), but not on \(n\) or
\(N\).

## 1. Attempt and record counts

If the selected column basis at layer \(h\) has \(r_h\) columns, the exact
number of attempted nonempty subsets is

\[
T_h=\sum_{k=1}^{\min(D,r_h)}{r_h\choose k}.
\]

For \(D\ge 1\),

\[
T_h\le (D+1)(R_h+1)^D.
\]

The case \(D=0\) has no attempts and is immediate. Since at most one record is
retained per attempt,

\[
R_{h+1}\le R_h+T_h.
\]

Set \(x_h=\log_2(R_h+1)\). The two inequalities give

\[
x_{h+1}\le D x_h+\log_2(D+2).
\]

Using \(D\le L^b\) and \(x_0\le CL^a+1\), induction gives, for every fixed
\(h\),

\[
x_h=L^{O_h(1)},\qquad
R_h,T_h=2^{L^{O_h(1)}}.
\]

More explicitly, a loose bound is
\(x_h=O_h(L^{a+bh}+L^{bh+1})\). Therefore the total number of attempts through
any fixed \(H\), \(P_H=\sum_{h<H}T_h\), is quasipolynomial.

This count includes duplicates and failed direct screens. Deduplication can
only decrease \(R_h\); it is not needed for the upper bound.

## 2. Numeric, record, and provenance bit lengths

Candidate generation does not hide a large integer. The decorated products
are reduced modulo \(N\). Their canonical unit representative \(z\) and its
least positive inverse \(w\) satisfy

\[
1\le z,w<N,\qquad A=zw<N^2<2^{2n}.
\]

Thus a generated exact value has at most \(2n+O(1)=2^{O(L)}\) bits. A product
of at most \(D\) residues can be reduced after every multiplication, so its
working residues have \(O(n)\) bits. Even an unreduced temporary product has
only \(O(Dn)\) bits. Correcting repeated parity blocks requires at most a scan
of the current block rows and modular arithmetic on \(O(n)\)-bit operands.

Let \(S_h\) be the sum of the bit lengths of all distinct positive exact
values in the union through layer \(h\). The base values are charged to
\(B_0\), so

\[
S_h\le B_0+O(nP_h)=2^{L^{O_h(1)}}.
\]

The same conclusion holds if a simple implementation temporarily keeps every
candidate before exact-value deduplication.

Canonical retention can use an exact integer comparison tree, or a
deterministic sort at the end of a layer. A hash may summarize a sequence, but
it is not used as equality evidence. The first occurrence fixes the record
label and the retained decorated root. Every later equal value increments an
occurrence count and first compares the exact decorated roots. The count needs
only \(O(\log(P_H+1))\) bits. Per-layer counts and layer metadata have the same
bound for fixed \(H\).

An attempt provenance descriptor needs at most \(D\) parent indices, each of
\(O(\log(R_h+1))\) bits. If it also records every parity correction rather
than recomputing it, it uses at most one entry per current block row. The row
count is at most \(S_h\). Hence retaining every attempt descriptor still uses
quasipolynomial space. References give a provenance DAG. Even fully expanding
the parent trees adds at most
\(1+D+\cdots+D^H=L^{O_H(1)}\) nodes per record, which does not change the
fixed-depth class.

The following choices make the whole transcript deterministic without a
probabilistic assumption:

1. Label exact values by first occurrence in the specified subset order.
2. Compare and merge values by their exact canonical unsigned encoding.
3. Choose gcd-refinement pairs and replacement order lexicographically.
4. Order final block rows by a fixed exact order.
5. Scan columns by first occurrence and use the largest active row as pivot.
6. Stream sequence hashes only after the exact sequence is fixed.

All comparisons, metadata updates, and hashing process at most a
quasipolynomial number of bits.

## 3. Complete factor-free refinement

This phase is polynomial in \(S_h\); it does not invoke integer factorization.
Ignore the numerical value \(1\) during block refinement, but retain its
record as a zero parity column for decoding.

For every distinct \(A_i>1\), initialize one block \(A_i\) and an exponent
vector that records its multiplicity in every labelled value. Maintain the
exact invariant

\[
A_i=\prod_j b_j^{e_{ij}}.
\]

Keep only one copy of each numerical block. If two current blocks \(x,y\)
have \(g=\gcd(x,y)>1\), replace them by the nonunit members of

\[
g,\quad x/g,\quad y/g.
\]

If the exponent columns of \(x,y\) were respectively \(\alpha,\beta\), the
new columns are \(\alpha+\beta,\alpha,\beta\), with columns of equal numerical
blocks added. This addition is the multiplicity-aware step. Merely replacing
sets of divisors would lose valuations, for example when a quotient still
shares a factor with the gcd.

Termination is elementary. Let

\[
\mu=\sum_j\log_2 b_j
\]

over the distinct current blocks. A nontrivial gcd replacement decreases
\(\mu\) by at least \(\log_2 g\ge1\); merging coincident replacement blocks can
only decrease it further. Initially \(\mu\le S_h\). Thus there are at most
\(S_h\) refinement steps. At termination the blocks are pairwise coprime.
Their count and every exponent are also \(O(S_h)\). A deterministic scan for
the first overlapping pair, gcd, exact division, and vector updates therefore
take \(S_h^{O(1)}\) bit operations and space.

For each resulting block \(b>1\), test exponents
\(2,3,\ldots,\lfloor\log_2 b\rfloor\) by exact integer-root computation and
write

\[
b=q^d
\]

with maximal \(d\). A binary-search integer root plus exact powering is already
a deterministic polynomial-bit algorithm; no fast root algorithm is needed
for this bound. Maximality makes \(q\) not a perfect power, hence in particular
not a square. Roots of pairwise coprime blocks remain pairwise coprime.

Multiply the corresponding exponent column by \(d\). Then set

\[
v_{ji}=e_{ij}\bmod2,\qquad
s_i=\prod_jq_j^{\lfloor e_{ij}/2\rfloor}.
\]

This gives exactly

\[
A_i=s_i^2\prod_{j:v_{ji}=1}q_j.
\]

It removes whole-square and odd-perfect-power redundancy, preserves all
multiplicities, and yields pairwise coprime nonsquare blocks. The positive
\(s_i\) and the parity vector are unique relative to this deterministic block
basis. Exact-root tests, exponent updates, and construction of all \(s_i\)
remain polynomial in \(S_h\). The recorded transformation columns also give,
at the same cost, the preservation or strict splitting map from every old
block to the rebuilt union blocks.

## 4. Full parity-kernel and root decoding

Let \(m=R_h\) and let \(K\) be the number of positive blocks. We have
\(K\le S_h\). Form the \(K\times m\) binary parity matrix \(V\). A product of
columns is an exact square if and only if its parity sum is zero. Indeed,
pairwise coprimality prevents cancellation between different \(q_j\), and an
odd power of a nonsquare is a nonsquare.

Deterministic column elimination costs a polynomial in \(K+m\). Scan columns
in first-occurrence order. Reduce with existing pivots, and choose the largest
active row for every new pivot. Store transformation bits during reduction.
Each rejected column then gives one dependency; the \(m-r_h\) such vectors are
independent and span \(\ker V\). This is a complete binary kernel basis.

For a basis dependency \(d\), compute the exact positive root

\[
X_d=
\prod_{i:d_i=1}s_i
\prod_jq_j^{\frac12\sum_{i:d_i=1}v_{ji}}.
\]

Its bit length is at most the total bit length of the participating exact
values, hence at most \(S_h\). If \(\rho_i\) is the supplied modular root on
record \(i\), compute

\[
U_d=\prod_{i:d_i=1}\rho_i\pmod N,\qquad
Z_d=X_dU_d^{-1}\pmod N.
\]

All retained relation values are units, so these inverses exist. Then
\(Z_d^2\equiv1\pmod N\). Test both signs with

\[
\gcd(Z_d-1,N),\qquad\gcd(Z_d+1,N),
\]

equivalently with the two gcds of \(X_d\pm U_d\) and \(N\). There are only
\(m-r_h\le m\) basis dependencies. Exact multiplication/root construction,
modular products, inverses, and both gcd tests for all of them take
\(S_h^{O(1)}+(K+m+n)^{O(1)}\) bit operations and space.

The selected column basis used by the next generation is a different object
from a reduced column. On accepting an independent column, the decoder stores
that column's original decorated lift

\[
(v_i,s_i^{-1}\bmod N).
\]

It must not store the elimination residue in its place. At most \(r_h\)
decorated lifts are stored. For a selected subset, let \(t_j\) count how many
selected parity columns contain row \(j\). Generation multiplies the actual
lifts and divides the modular product by
\(q_j^{\lfloor t_j/2\rfloor}\) for every row. This needs at most \(D\) lift
products plus a scan of the \(K\) rows. It is polynomial in \(D,K,n,S_h\) per
attempt, or in \(D,K,n\) after the residues \(q_j\bmod N\) are precomputed once
during decoding.

### The \(A=1\) column

The value \(A=1\) contributes no positive block, but it is not deleted from
the parity matrix. It is a zero column. Therefore it gives a unit kernel
dependency and receives the same supplied-root normalization and both-sign
gcd tests as every other dependency. It is never selected into an independent
column basis, so it cannot create a false feedback basis vector. Exact-value
canonicalization retains at most its first record, while every duplicate root
is still compared before the occurrence is merged. These rules cover both
correctness and cost. The same treatment applies to any other zero-parity
exact-square column.

## 5. Combining the costs

At a fixed layer, subset enumeration and candidate generation cost

\[
T_h\,\operatorname{poly}(D,n,S_h,R_h),
\]

and retention, refinement, matrices, the complete kernel basis, exact roots,
gcd screens, metadata, and provenance cost a polynomial in the total state
and attempted-output lengths. Every argument of these polynomials is
\(2^{L^{O_h(1)}}\). A fixed sum and product of such quantities is again
\(2^{L^{O_h(1)}}\). Summing over the fixed set of layers
\(0,\ldots,H\) proves

\[
\boxed{\text{time and space through fixed }H
=2^{L^{O_H(1)}}.}
\]

The proof is only a cost proof. It does not imply that any tested root is
non-global or that a factor is found.

## 6. Why \(H\) must be fixed

The recurrence contains a factor \(D\) in the exponent at every layer. Its
direct iteration has the form

\[
\log_2(R_H+1)\lesssim L^{a+bH}
\]

up to lower-order terms and constants depending on \(H\). When \(b>0\), for
example, substituting \(H=\lceil\log L\rceil\) into this proof yields an
exponent \(L^{a+b\lceil\log L\rceil}\), not a fixed polynomial in \(L\). If
\(b=0\), some growing-depth schedules can still be quasipolynomial, but the
theorem supplies no bound on \(H\), and an arbitrary \(H\) contributes at
least the cost of visiting that many layers. Thus the fixed-\(H\) proof gives
no uniform quasipolynomial claim for growing \(H\). This does not prove that
every growing-depth run is expensive.

## 7. Kernel-enumeration boundary

The theorem would be false if “full decoding” meant enumerating all vectors
of \(\ker V\), rather than computing a complete basis and decoding every basis
member. This is not the ordered decoder in the statement, but the boundary is
exact.

For a family of \(n\)-bit odd moduli \(N\), where
\(L=\lceil\log_2(n+1)\rceil\), take \(m=2^{\Theta(L)}\) distinct base records

\[
A_k=(1+kN)^2,\qquad \rho_k=1.
\]

Their explicit total length is \(2^{O(L)}\), they are units congruent to \(1\)
modulo \(N\), and every parity column is zero. Thus the nullity is \(m\), and
the full kernel has \(2^m\) vectors. Enumerating all of them takes
\(2^{2^{\Theta(L)}}\) output steps. Computing and decoding the complete basis
has only \(m\) vectors and satisfies the theorem proved above.
