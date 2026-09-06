# F147 hostile audit — PASS

## Frozen inputs

I audited only the frozen proof candidate:

- `STATEMENT.md`:
  `2fc9e36eac6754ffe0405d017d9a58829f95965fbdde94b7ce0f060e4309c204`;
- `PROOF.md`:
  `6868737e521dcaa64473bc105d9fa85e1458947b5aa312bc98f3771e141577ad`.

Both hashes matched before the audit. I did not modify either frozen file.
I used no research computation.

I compared the claims with P124 and P128--P131. In particular, I checked
that F147 does not contradict P131's square-root-scale lower bound or revive
P130's formal-cycle decoy as a positive signal.

## Verdict

**PASS.** I found no false implication, missing arithmetic hypothesis, or
quasipolynomial complexity overclaim within the stated frozen-P128 scope.

The increment is narrow but real. Under `H^4 <= N`, a wrapped positive cycle
cannot mix wrapped and unwrapped edges. It must lie in an explicitly scanned
large-to-large core. The full standalone bridge kernel of that core can then
be decoded in quasipolynomial time. F147 does not prove that this kernel is
nonzero, survives exact-value deletion, or has a non-global root.

## 1. The fully wrapped implication is exact

Suppose an unwrapped edge `q -> r` with anchor `a` is followed by a wrapped
edge from `r` with anchor `b`. The first equality is

\[
qa^2=rT.
\]

The named blocks are distinct and pairwise coprime. Hence `r | a^2` and
`r <= a^2`. The next edge wraps, so `rb^2>N`. Therefore

\[
a^2b^2\ge rb^2>N.
\]

This contradicts `a,b <= H` and `H^4 <= N`. Any directed cycle containing
both edge types has an unwrapped-to-wrapped transition, so the proof covers
the entire mixed case. The strict inequality from wrapping also handles the
boundary `H^4=N`.

This does not contradict P131. It implies that a wrapped cycle has at least
enough bounded anchors to make their product exceed `sqrt(N)`; it does not
make such a cycle short or force one to exist.

## 2. The large-center, carry, and residual bounds survive

For every position,

\[
t=\left\lfloor{qa^2\over N}\right\rfloor<a^2\le H^2,
\]

because `q<N`. Thus a wrapped position has `1 <= t < H^2`.

For a wrapped cycle edge, `qa^2>N`, so

\[
q>{N\over a^2}\ge {N\over H^2}.
\]

The target is the source of the next cycle edge. Section 1 makes that edge
wrapped too, so the same bound holds for `r`. Since `c=rT<N`,

\[
1\le T<{N\over r}<H^2.
\]

All four inequalities are strict in the places needed by the graph
construction. No sign or zero case is omitted: residues are least positive,
and all source blocks and anchors are units.

## 3. A word position has at most one large target

If two distinct named blocks `r,s>N/H^2` divided the same `c<N`, their
pairwise coprimality would give `rs | c`. But

\[
rs>{N^2\over H^4}\ge N>c,
\]

which is impossible. Therefore the source position has at most one large
target. This is uniqueness per position, not uniqueness of an outgoing edge
per vertex; the statement keeps that distinction.

Sections 1--3 prove graph completeness exactly at the claimed level. Every
wrapped directed cycle on the frozen named basis uses only wrapped edges
between large vertices, and every one of its indexed positions is retained
by the scan.

## 4. The bridge decoder is exact

For one retained edge,

\[
D=Uc=(qa^2)(rT)=qra^2T,
\qquad
D\equiv c^2\pmod N.
\]

The anchor contributes an exact square. Joint multiplicity-aware gcd-free
refinement of the named blocks and residuals therefore supplies the exact
binary square class of every bridge without factoring a large named block.
Maximal perfect-power extraction is sufficient: a pairwise-coprime base
that is not a perfect power has an odd rational-prime valuation, so an odd
outer exponent cannot be hidden inside a square.

If `x` is in the resulting kernel and

\[
\prod_{e:x_e=1}D_e=Y_x^2,
\]

then

\[
\rho_x=Y_x\left(\prod_{e:x_e=1}c_e\right)^{-1}\pmod N
\]

is a square root of one. Every inverse exists because `c`, each named block,
and hence every residual are units modulo `N` on the no-earlier-factor
branch.

The actual matched P128 values obey

\[
C_eL_e=(c_ew_e)(U_ew_e)=D_ew_e^2.
\]

Their positive root is `Y_x prod_e w_e`, which reduces to the same `rho_x`.
Thus the conceptual bridge computation and the legal actual-ledger
selection agree. The decoder is complete for standalone bridge dependencies
supported on `G_H`; it does not claim completeness for arbitrary mixtures
with outside old columns.

## 5. Global exact-value deletion cannot erase a useful root

Every actual P128 relation value is a positive integer congruent to one
modulo `N`. If an equal actual value `V` occurs twice in a selected square
product, deleting the pair divides the positive root by `V`. Prime
valuations show that this quotient is an integer, and `V=1 mod N` leaves the
normalized root unchanged.

If the whole selected vector maps to zero after equality-class reduction,
its positive root is a product of deleted relation values. Its root is
therefore `+1 mod N`. Consequently a vector with a non-global root cannot
vanish under deletion.

This uses equality of **actual** values, not equality of conceptual bridges.
It therefore respects P129's warning that conceptual bridge integers with
different supplied roots cannot be discarded by integer equality alone.

The kernel-to-ledger map and the normalized-root map are binary group
homomorphisms. The root map descends to the image because its value is `+1`
on the deletion kernel. Hence testing roots for preimages of an image basis
is complete: if all basis roots are in `{+1,-1}`, every combination is
global.

## 6. The edge-surplus rank bound is valid

Before residual refinement, the `m` pairwise-coprime, maximally extracted
named blocks need at most `m` independent gcd-free bases. Let `R_H` be the
set of rational primes in all residuals.

For a prime in `R_H` that is new to the named blocks, refinement adds at
most one base. For a prime that divides one named block, pairwise
coprimality prevents it from splitting any other named block, and isolating
it increases the total base count by at most one. Repeating this argument
over the distinct residual primes gives at most

\[
m+|R_H|
\]

rows. Multiplicities do not create additional rows. They only change the
integer exponents recorded on an existing base.

Rank-nullity now gives

\[
\dim\ker M_H\ge E_H-m-|R_H|.
\]

Every residual is below `H^2`, so every one of its prime divisors is below
`H^2`, and `|R_H| <= pi(H^2)`. The statement correctly keeps exact-value
survival and root asymmetry outside this rank conclusion.

## 7. Source legality and cost are correctly scoped

F147 does not promote residues, cofactors, or gcd aggregates to new named
generators. It scans an explicit list of already legal frozen P128
positions and retains their original word provenance. Later refinement only
changes the gcd-free presentation of those integers. It does not change the
frozen word or invent a new source position.

With at most `Q` positions and `Q` named blocks, all target tests cost at
most `Q^2` exact divisions. Core residues are below `H^2`, so trial division
through `H` completely factors them: after all factors at most `H` are
removed, a composite cofactor would have a factor below its square root and
therefore below `H`, a contradiction.

Every core actual value has `O(n+log H)` bits. The remaining operations are
polynomial in the explicit frozen-P128 transcript, `H`, and the displayed
matrix dimensions. The inherited P128 representation bounds cover compact
outside-ledger entries used for global equality classes. Thus

\[
Q,H=2^{(\log n)^{O(1)}}
\]

make `Q^2`, `QH`, `H^2`, refinement, elimination, and root tests all
quasipolynomial. Also `4 log H=o(n)`, so `H^4<=N` holds for all sufficiently
large inputs. The finite exceptional prefix can be handled separately.

If one detached the theorem from the frozen P128 encoding and let `Q` mean
only a cardinality bound on arbitrary huge ledger entries, `Q` alone would
not bound bit cost. That is outside the declared source scope and does not
invalidate the stated quasipolynomial consequence.

## 8. The parameter regime is not internally contradictory

P131 rules out wrapped cycles whose **total** anchor product stays
quasipolynomial in magnitude. F147 instead permits a polynomial-length list
of individually bounded anchors. Their product can exceed `sqrt(N)` while
the explicit edge list and decoder remain quasipolynomial. Therefore
`H^4<=N` does not reintroduce F144 V1's impossible short-cycle regime.

The theorem is still conditional. It does not force a large target, a
cycle, a kernel vector, exact-value survival, or a non-global normalized
root. Its stated remaining gate is accurate:

\[
\text{force a surviving large-core bridge dependency with non-global root.}
\]

No all-input factoring theorem follows from F147 alone.

## Final scope

The hostile attacks requested in the frozen statement all survive. F147 is
eligible for a fresh statement-only blind reconstruction. Promotion, if any,
must retain its exact scope: a bounded-anchor large-core reduction and
complete standalone bridge decoder, not a cycle-existence law or a factoring
algorithm.
