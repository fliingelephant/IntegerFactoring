# F94 hostile proof audit

## Verdict: FAIL

I audited RESULT.md in full at SHA-256

    2785f19170236cf22734ffc1f9a2a8833dde9d1dc40260a88fac8d039bd16eca

The central one-column rank calculation is correct. The private-fresh-row
obstruction is also correct relative to a fixed known matrix. However, three
claims need correction:

1. A general exact gcd-free refinement does not merely duplicate old rows.
   It can introduce exponent multiplicities, and these can change a kernel
   modulo a prime.
2. Corollary 4 does not require its private rows to vanish on the old
   matrix. Its proof establishes independence among the appended columns,
   but not independence modulo the old column span.
3. The P91 root-coset decoder consequence is invoked under the setup
   \(N\ge2\), although that decoder needs the distinct-odd-semiprime scope
   and its other stated hypotheses.

The smallest exact corrections are given in Sections 2, 6, and 7 below.

## 1. The general gcd-free refinement map has multiplicities

For a complete exact gcd-free basis, the general old-block representation is

\[
q_j=\prod_r b_r^{\alpha_{rj}},
\qquad
\alpha_{rj}\in\mathbb Z_{\ge0}.
\]

Because the old \(q_j\) are pairwise coprime, the supports for distinct
columns \(j\) are disjoint. But the positive exponents
\(\alpha_{rj}\) need not equal one.

The true coordinate map is therefore

\[
(\Delta_\alpha x)_r=\alpha_{rj}x_j
\]

on a row supported by \(q_j\), rather than simple row duplication. It is
injective over \(\mathbb Z\), but its reduction modulo \(\ell\) need not be
injective. If all multiplicities belonging to one old block are divisible
by \(\ell\), that old coordinate is killed modulo \(\ell\).

### Exact counterexample

Take

\[
N=3,\qquad Q=(4).
\]

The block \(4\) is a unit modulo \(3\), and the one-column relation

\[
4\equiv1\pmod3
\]

has old exponent matrix

\[
E=[1].
\]

Joint exact gcd-free refinement with the new endpoint \(2\) has the single
block \(B=(2)\) and exact representation

\[
4=2^2.
\]

Thus the refined old relation matrix is

\[
E'=[2].
\]

Modulo \(2\),

\[
\ker(E\bmod2)=0,
\qquad
\ker(E'\bmod2)=\mathbb F_2.
\]

Refinement alone has created a new mod-\(2\) dependency. This example
satisfies the initial unit, relation, and pairwise-coprime requirements. The
only failed assertion is the candidate's implicit claim that a standard
gcd-free refinement always has the multiplicity-free form (1).

This is not a cosmetic issue. It directly refutes the unqualified title of
Theorem 1, the material claim that block refinement alone never changes a
prime-saturation kernel, and the Section 8 instruction to “duplicate” old
rows after every gcd-free refinement.

## 2. Smallest correction to Theorem 1

The proof of Theorem 1 is correct under the displayed map \(\Delta\). The
problem is the assertion that every joint gcd-free refinement has that map.

The smallest correction is to add the explicit restriction:

> Assume the refinement is multiplicity-free on every old block: each old
> \(q_j\) is the product of distinct refined blocks, each to exponent one,
> exactly as in (1).

Then each nonempty old support contains rows with coefficient one, so
\(\Delta\bmod\ell\) is injective for every prime and

\[
\ker(\Delta E\bmod\ell)=\ker(E\bmod\ell).
\]

Every statement that says “gcd-free refinement” without qualification,
including the bookkeeping instruction in Section 8, must be narrowed to
this multiplicity-free case. Without that restriction, Theorem 1 is false.

This correction restricts the candidate. It does not add a new general
refinement theorem.

## 3. The one-column rank accounting is correct

Fix a prime \(\ell\) and work over \(\mathbb F_\ell\). Let

\[
V_\ell=\ker E'.
\]

A vector \((x,a)\) lies in the kernel of \([E'\mid u]\) exactly when

\[
E'x+au=0.
\]

If \(u\) is not in the old column span, this forces \(a=0\), so

\[
\ker[E'\mid u]=V_\ell\times\{0\}.
\]

The new column increases rank and column count by one, leaving nullity
unchanged.

If \(u\) is in the old span and \(E'c+u=0\), then subtracting
\(a(c,1)\) from \((x,a)\) leaves an element of
\(V_\ell\times\{0\}\). The last coordinate proves that the sum is direct:

\[
\ker[E'\mid u]
=
(V_\ell\times\{0\})\oplus\langle(c,1)\rangle.
\]

Rank is unchanged while column count increases by one. The nullity
therefore increases by exactly one. Theorem 2 passes for the explicit known
matrix.

This is presentation accounting. It does not say that \(E'\) contains the
complete modular relation lattice of the residues.

## 4. The fixed private-fresh-row obstruction is correct

Under the candidate's defined refined matrix, every row in \(F\) is zero in
every old column. Hence every vector in the old column span is zero on that
row.

If the new column satisfies

\[
u_r\not\equiv0\pmod\ell
\]

for such a row, it cannot lie in the old span. Theorem 2 then shows that
appending this column creates no new kernel direction. If \(u_r=1\), this
holds for every prime.

Thus Theorem 3 is correct relative to the refined known matrix. It remains
correct even when the known relation list is incomplete: incompleteness can
hide other true relations, but it does not put the displayed vector into
the span of the columns that are actually present.

Theorem 3 does not repair Theorem 1. In a general multiplicity-bearing
refinement, the refinement itself can enlarge the old kernel before the new
private column is appended. The private column can be nonclosing while the
overall feedback step still gains a dependency from refinement.

## 5. Canonical-inverse interpretation

If \(g\) is a unit modulo \(N\) and \(w\) is its least positive inverse,
then the exact integer identity

\[
gw=1+kN
\]

holds for an integer \(k\ge0\). If joint refinement produces a block that

1. divides no old \(q_j\), and
2. occurs in the new relation column to exponent one,

then its row is zero in \(E'\) and one in \(u\). Theorem 3 applies for every
prime. This interpretation is correct.

The phrase “has not appeared before” must mean the precise row condition
above, or at least zero incidence in every old known column. Merely assigning
a new integer label to a factor that lies in old-supported rows is not
sufficient.

The conclusion concerns closure of the known exponent column. It does not
exclude a direct gcd, a power decoder, a mixed word, an internal
perfect-power structure of the fresh block, or a relation absent from the
known list. The candidate mostly preserves these distinctions.

## 6. Corollary 4 is insufficient relative to the old matrix

Condition (9) says that each \(u_i\) has a row on which it is nonzero and all
earlier appended columns are zero. Choosing the largest index with a
nonzero coefficient proves that

\[
u_1,\ldots,u_M
\]

are mutually linearly independent, provided “nonzero” means nonzero modulo
\(\ell\). That part of the proof is correct.

It does not show that their images are independent modulo
\(\operatorname{colspan}(E')\). A column can be independent of the other
new columns and still close against the old columns.

### Exact counterexample

Over \(\mathbb F_2\), take

\[
E'=[1],
\qquad
u_1=[1].
\]

For the sole row \(r_1\), the displayed condition (9) holds: \(u_1\) is
nonzero and there is no earlier appended column. The one-element list
\(\{u_1\}\) is linearly independent.

Nevertheless,

\[
[E'\mid u_1]=[1\mid1]
\]

has the new kernel direction \((1,1)\). The appended relation closes
against the old column and creates a dependency.

There is a second literal ambiguity. The \(u_i\) were defined as integer
columns. If \((u_i)_{r_i}\ne0\) means nonzero as an integer, it can still be
zero modulo \(\ell\). For example, a one-entry column \([\ell]\) is nonzero
over \(\mathbb Z\) but zero over \(\mathbb F_\ell\).

### Smallest correction to Corollary 4

For every \(i\), require all three conditions

\[
(u_i)_{r_i}\not\equiv0\pmod\ell,
\]

\[
(E')_{r_i,*}=0\pmod\ell,
\]

and

\[
(u_j)_{r_i}\equiv0\pmod\ell
\qquad(j<i).
\]

Then the last-index argument works modulo the old column span, and the
appended columns create no new dependency beyond the old kernel.

The special case in which every feedback relation introduces a genuinely
fresh block to exponent one does satisfy these corrected conditions. The
general Corollary 4, as currently written, does not.

## 7. The P91 decoder paragraph has the wrong ambient scope

F94 begins with

\[
N\ge2.
\]

The linear-algebra Theorems 1–3 need no semiprime assumption. The cited P91
decoder consequence does. Its short complete coset scan uses the
two-coordinate CRT structure for

\[
N=pq
\]

with distinct odd primes, together with the failed complete old decoder and
the other P91 hypotheses.

For a modulus with more local prime components, the old \(\ell\)-root image
can have dimension greater than one. One selected old root need not generate
it, and an \(\ell\)-element menu need not cover the relevant coset. The
candidate cannot invoke that decoder under the unrestricted \(N\ge2\)
setup.

The smallest correction is to prefix the P91 consequence in Section 4 and
its use in Section 8 with:

> Under P91's distinct-odd-semiprime hypotheses and after its complete old
> decoder has failed, ...

Here “complete old decoder” must mean complete for the root image generated
by the explicit known relation kernel. It does not mean that the algorithm
knows the complete relation lattice of the full unit group.

Without this scope restriction, the decoder claim is false as quantified.

## 8. The P99 full-group consequence is correct

Assume the retained units \(a_1,\ldots,a_d\) generate the complete unit
group and each is represented by products of current unit blocks \(B\).
Then, as residue subgroups,

\[
G_N
=
\langle a_1,\ldots,a_d\rangle
\le
\langle B\rangle
\le
G_N.
\]

Thus

\[
\langle B\rangle=G_N.
\]

If later no-factor refinement retains exact representations of all the
\(a_i\), the same sandwich remains true. Abstract multiplicative subgroup
growth is impossible on this conditional source event.

This does not make the public relation matrix complete. Since the \(a_i\)
generate \(G_N\), a modular word expressing a new unit block in those
generators exists. The algorithm is not thereby given that word or its
relation column. The candidate states this distinction correctly.

The algebraic consequence is conditional on the full-group source event and
the retained exact block representations. Any probability or input-class
scope belongs to P99 and is not proved by F94.

## 9. Known relations versus complete relations

All kernel and rank statements in Sections 3–6 concern the columns in the
known list \(E\). They do not characterize every true multiplicative
relation among the block residues.

Accordingly:

- a nonclosing private column means nonclosing relative to the known span;
- a closing column gives an indexed dependency in the known presentation;
- full abstract generation of \(G_N\) does not supply missing relation
  words; and
- discarding a known column can lose useful future presentation
  information even though the abstract subgroup remains unchanged.

The candidate explicitly states most of this. Any reading in which
\(\ker(E\bmod\ell)\) is the complete hidden relation lattice would be
incorrect.

## 10. Discarding ephemeral relations is not lossless

The candidate makes only a possibility claim, and it is valid. In a
one-row presentation, a first column

\[
u_1=[1]
\]

is nonclosing against an empty old span. A later identical column

\[
u_2=[1]
\]

closes against the retained first column and creates the dependency
\((1,-1)\) over every prime.

If the first relation column and its row provenance are discarded, the
second column is again nonclosing in the remaining presentation. Abstract
subgroup equality does not reconstruct the missing public dependency.

Thus retaining only a block split is not proved lossless. A bounded-memory
ephemeral rule can still be chosen as a heuristic, but the P99 full-group
consequence does not justify the deletion.

## 11. Complexity and bookkeeping

For an explicit matrix and an explicitly bounded list of scanned primes,
column-span tests and incremental ranks are deterministic polynomial-time
linear algebra. The at-most-\(\ell\) P91 scan is polynomial only when
\(\ell\) is numerically polynomial in \(\log N\), as the candidate states,
and only under the corrected P91 scope.

The instruction to duplicate old rows is polynomial but is not correct for
a general exact gcd-free refinement. Exact exponent multiplicities must be
represented. Under the smallest correction adopted in Section 2, row
duplication is valid because the theorem is restricted to
multiplicity-free refinement.

The overall bookkeeping cost is polynomial in the explicit presentation,
the retained relation count, the generator encodings, and the scanned-prime
list. F94 supplies no bound on how many feedback rounds or relations an
external algorithm retains, so it does not by itself prove an all-input
polynomial-time closure algorithm.

## 12. Exact corrected scope

The valid core is:

1. for a fixed known exponent matrix, Theorem 2 gives exact one-column rank
   accounting;
2. a row that is zero in every old known column and nonzero in the new
   column prevents that column from closing;
3. a retained full-group generator batch prevents further abstract subgroup
   growth but does not reveal unknown relations; and
4. deleting relation columns can lose future public dependencies.

F94 fails as written because its general refinement claim, Corollary 4
saturation conclusion, and unrestricted P91 decoder consequence exceed that
valid core.

The smallest corrections are restrictions, not extensions:

- restrict Theorem 1 and all row-duplication claims to multiplicity-free
  refinements satisfying (1);
- add old-matrix zeros and explicit mod-\(\ell\) nonzero conditions to
  Corollary 4; and
- restrict every P91 decoder claim to P91's distinct-odd-semiprime scope and
  other hypotheses.
