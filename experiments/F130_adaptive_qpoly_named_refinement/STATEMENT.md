# F130 statement — adaptive quasipolynomial named refinement

## Status and scope

This is a proof-only algorithm and cost candidate. It is not an all-input
factoring theorem. No success law, computation, hostile audit, or blind
reconstruction is part of this artifact.

The core construction applies to an odd input \(N\) that is not prime and is
not a perfect power. Standard deterministic preprocessing handles even
inputs and tests primality. If \(N=a^k\) is an exact perfect power with
\(1<a<N\), preprocessing returns \(a\) as a proper divisor; recursive use of
the splitter then handles its factorization. The unresolved claim below
concerns the remaining odd non-perfect-power input.

Put

\[
n=\lceil\log _2(N+1)\rceil,
\qquad
L=\lceil\log _2(n+1)\rceil,
\qquad
D=L^2,
\qquad
E=2^{L^2}.
\]

The construction keeps two different factor-free bases. They must never be
identified.

1. The **named generator basis** contains only descendants of a fixed
   initial endpoint product. Only this basis generates later word menus.
2. The **decoder basis** is the final P66 gcd-free basis of all retained
   exact relation values. It can contain novel private factors. Its blocks
   never become named generators merely because P66 found them.

## Initial seed state

Put

\[
H=\min(E+1,N-1).
\]

For every seed \(s=2,\ldots,H\), compute \(d=\gcd(s,N)\). Return \(d\) if it
is proper. Otherwise compute the least positive inverse

\[
w_s=s^{-1}_{\mathrm{can}}\pmod N.
\]

Test

\[
\gcd(s-w_s,N),
\qquad
\gcd(s+w_s,N),
\]

and return any proper divisor. On the branch where all these screens are
null, define the fixed initial endpoint product

\[
A_0=\prod_{s=2}^{H}s\,w_s.
\]

Use deterministic complete gcd-free refinement and exact maximal
perfect-power extraction to obtain a sorted pairwise-coprime basis

\[
\mathcal B_0=(q_{0,1},\ldots,q_{0,M_0})
\]

of integers greater than one. Every \(s\) and \(w_s\) has a known
nonnegative exponent presentation on this basis. Every \(q_{0,j}\) is not an
exact perfect power.

The exact seed relations

\[
P_s=s w_s\equiv1\pmod N
\]

start the relation ledger. Remove \(P_s=1\), and retain only the first
occurrence of each exact positive integer value in increasing seed order.

## One frozen adaptive stage

At stage \(t\), sort the current named basis

\[
\mathcal B_t=(q_{t,1},\ldots,q_{t,M_t}).
\]

Freeze it for the whole stage. Enumerate the following word positions in a
fixed order:

1. increasing support size;
2. lexicographic support indices; and
3. lexicographic positive exponent tuples.

The positions are

\[
u=\prod_{j\in S}q_{t,j}^{e_j},
\qquad
|S|\le D,
\qquad
1\le e_j\le E.
\]

The empty support is allowed and gives \(u=1\). Compute only the canonical
residue

\[
c=[u]_N\in\{1,\ldots,N-1\}.
\]

Within the frozen stage, process only the lexicographically first word for
each distinct \(c\). This loses no endpoint, relation value, or named
refinement because \(c\) determines its canonical inverse. Compute

\[
w=c^{-1}_{\mathrm{can}}\pmod N,
\qquad
P(c)=cw\equiv1\pmod N.
\]

Run both direct screens

\[
\gcd(c-w,N),
\qquad
\gcd(c+w,N),
\]

and return any proper divisor.

Every distinct residue contributes both integer endpoints \(c,w\) to the
stage exposure batch. This endpoint insertion occurs before exact-value
deduplication. Thus two different residues with the same integer value
\(P(c)\) can cause different named refinements.

After inserting the endpoints, remove \(P(c)=1\). If the exact positive
integer \(P(c)\) has not occurred in an earlier seed or stage record, append
it to the permanent relation ledger together with its first word
provenance. Never delete a retained relation because it does not yet close.

Do not change the named basis during this scan. Exhaust the complete frozen
menu first.

## Multiplicity-aware named refinement

After the full stage scan, run deterministic complete gcd-free refinement on
the union of

1. the old named blocks \(\mathcal B_t\), and
2. all stage endpoints \(c,w\).

The refinement returns pairwise-coprime bases and exact exponent
presentations of every input. Retain as new named candidates only those
terminal bases that occur with positive exponent in the presentation of an
old named block. Discard bases that occur only in novel probe cofactors.
Apply exact maximal perfect-power extraction to the retained candidates,
update the exponent presentations, and sort the result. Call it
\(\mathcal B_{t+1}\).

This must be full multiplicity-aware gcd-free refinement. A single pass of
the tests \(1<\gcd(q,c)<q\) is not sufficient. For example, \(q=6\) and
\(c=12\) have \(\gcd(q,c)=q\), but complete refinement separates the named
block into \(2\) and \(3\).

If \(\mathcal B_{t+1}=\mathcal B_t\), stop. Otherwise restart the complete
word menu from its first position on the new frozen basis. Relations from
all earlier stages remain in the ledger.

## One final complete decode

Only after named refinement reaches a fixed point, run P66 once on all
distinct retained exact values

\[
P_1,\ldots,P_R,
\qquad
P_i\equiv1\pmod N.
\]

Use the known modular square residue \(x_i=1\) for every column. P66 builds
its own decoder basis, computes a complete binary square-class kernel basis,
and tests every kernel-basis vector. For a basis vector \(z\), compute the
exact positive square root

\[
R_z=\sqrt{\prod_{i:z_i=1}P_i}
\]

and test

\[
\gcd(R_z-1,N),
\qquad
\gcd(R_z+1,N).
\]

Return any proper divisor. If every direct screen and every final basis-root
screen is null, return “no certificate from F130.”

## Claimed cost and exact open gate

The complete construction is a uniform deterministic

\[
\boxed{2^{O((\log n)^4)}}
\]

bit-operation algorithm. The proof is in PROOF.md.

The initial seed phase contains the old seeds \(2,\ldots,n\), and the ledger
contains their exact relations. More strongly, for every fixed constant
\(C\), the seed phase contains the complete bank
\(2,\ldots,n^C\) for all sufficiently large \(n\). The first frozen stage
contains the full \(D,E\) word menu on its actual enriched basis
\(\mathcal B_0\).

This does not by itself give literal containment of every old C116/F26-Q
word position built on the narrower \(2,\ldots,n\) endpoint basis. The extra
seed endpoints can split a narrow old block into more than \(D\) named
descendants. An old bounded-support word can then exceed the new support cap
when expanded. The guaranteed inclusion is the seed bank, not every earlier
presentation.

No theorem proves that a proper named refinement occurs, that a refinement
creates a useful later relation, that the final parity kernel is nonzero, or
that its normalized-root image is non-global. The exact missing theorem is:

> For every surviving odd composite non-perfect-power \(N\), either one of
> the declared direct screens returns a proper divisor, or the normalized
> root map of the final retained P66 kernel has nonzero image modulo the two
> global roots \(\{+1,-1\}\).

Without this all-input progress theorem, F130 is a finite deterministic
quasipolynomial candidate, not a factoring algorithm.
