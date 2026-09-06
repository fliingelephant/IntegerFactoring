# F144 V3 hostile audit — passed

## Verdict

**PASS.** V3 repairs both failures in the preserved history.

- It does not restore V1's impossible short-cycle surplus regime.
- It changes V2's false strict bound to the exact non-strict bound
  \(\mathcal A\ge\sqrt{N+S^2}\), and it separates that fixed-\(S\)
  interval from the coarser anchor-only projection.

The frozen inputs match the requested hashes:

- `V3_STATEMENT.md`:
  `87dacd7af5121f66561cea4136d1445f10cfe0185bd9229277fd48b358bf5f6f`;
- `V3_PROOF.md`:
  `2635270473001fa32b6b9db15d9abb7460f31384ed9a8cec7de61f1c6717089e`.

I read both preserved hostile/blind reviews before this audit. No claim in
V3 reinstates the V1 contradiction, and the exact \(N=35\) equality that
refuted V2 now agrees with every displayed bound.

## 1. One-cycle law survives exact reconstruction

For a directed edge,

\[
U_e=q_ea_e^2=c_e+t_eN,
\qquad
c_e=r_eT_e.
\]

Around a directed cycle, the tail and head block multisets are equal. Thus,
with

\[
Q=\prod_eq_e=\prod_er_e,
\qquad
A=\prod_ea_e,
\qquad
T=\prod_eT_e,
\]

one has the exact products

\[
\prod_eU_e=QA^2,
\qquad
\prod_ec_e=QT.
\]

Every named block is a unit modulo \(N\), so cancellation of \(Q\) gives

\[
N\mid A^2-T.
\]

The termwise inequalities \(U_e\ge c_e>0\) give \(A^2\ge T\). Equality
holds exactly when all carries are zero. If one edge wraps, the difference
is a positive multiple of \(N\), and therefore

\[
A^2-T\ge N,
\qquad
A^2\ge N+T,
\qquad
A>\sqrt N.
\]

This is the exact obstruction that invalidated V1. V3 makes no residual-
square assumption here and makes no claim that a bounded wrapped cycle
exists.

## 2. Collection dependency and normalized root are exact

For an indexed collection of cycles, keep logical occurrences with
multiplicity. Tail-head balance again gives one common product \(Q\). If
the combined residual is \(S^2\), then

\[
\prod_e C_eL_e
=Q^2\mathcal A^2S^2W^2
=(Q\mathcal ASW)^2,
\]

where \(W=\prod_ew_e\). This is an exact integer square. Also

\[
W\equiv(QS^2)^{-1}\pmod N,
\]

so its normalized root is

\[
\rho\equiv\mathcal AS^{-1}\pmod N.
\]

The inverse exists. Since \(c_e=r_eT_e\), both \(c_e\) and \(r_e\) are
units, every \(T_e\) is a unit, and hence so is \(S\).

If at least one selected occurrence wraps, exact product comparison gives
\(\mathcal A>S\). Therefore

\[
\mathcal A^2-S^2=mN
\quad(m\ge1),
\]

and the sharp consequence is

\[
\boxed{\mathcal A\ge\sqrt{N+S^2}>\sqrt N.}
\]

The first sign is correctly non-strict. Equality occurs when \(m=1\).

## 3. The wrapped-cycle count boundary is correct

An unwrapped cycle has

\[
T_{\mathcal C}=A_{\mathcal C}^2.
\]

It contributes a square residual and normalized root \(+1\). Thus adjoining
unwrapped cycles cannot change the square status of the one wrapped
residual, and their anchor factors cancel from the normalized root.

If two indexed cycles wrap, each separately has anchor product greater than
\(\sqrt N\). Counting logical occurrences with multiplicity gives

\[
\mathcal A\ge
A_{\mathcal C_1}A_{\mathcal C_2}>N.
\]

Hence the metric hypothesis \(2\mathcal A<N\) can certify at most one
wrapped cycle. V3 correctly does **not** infer that every dependency using
two wrapped cycles has global root; it leaves those combinations to the
full decoder.

## 4. The metric gcd conclusion is valid for an odd composite

Assume a wrap, residual-square closure, and \(2\mathcal A<N\). Put

\[
x=\mathcal A-S,
\qquad
y=\mathcal A+S.
\]

Then

\[
0<x<y<N,
\qquad
N\mid xy.
\]

If \(x\) were a unit modulo \(N\), then \(N\mid y\), contrary to
\(0<y<N\). The same argument with \(x,y\) exchanged shows that neither is
a unit. Their strict size bounds show that neither gcd can equal \(N\).
Thus both

\[
1<\gcd(\mathcal A-S,N)<N,
\qquad
1<\gcd(\mathcal A+S,N)<N
\]

are proper. Since \(S\) is a unit, these are exactly the two sign tests for
the normalized root \(\mathcal AS^{-1}\).

For fixed \(S\), the necessary metric interval is now stated correctly as

\[
\sqrt{N+S^2}\le\mathcal A<N/2.
\]

After forgetting \(S\), its anchor-only projection is the strictly coarser
interval \(\sqrt N<\mathcal A<N/2\). V3 no longer identifies these two
statements.

## 5. Exact-value deletion is sound

V3 deletes duplicate **actual P128 integer values**, not conceptual bridge
columns. Every such value is congruent to \(1\pmod N\). If a selected
square product has positive root \(R\) and an exact value \(P\) occurs
twice, removing that pair leaves

\[
R^2/P^2=(R/P)^2.
\]

Prime valuations show \(P\mid R\). The new root is \(R/P\), and
\(P\equiv1\pmod N\), so the normalized root does not change. Repetition of
this operation handles shared edges, repeated cycles, canonical/lifted
cross-equalities, and all other even exact-value multiplicities.

The globally deduplicated ledger retains one representative of every odd
exact-value class, so the remaining parity selection is legal. Under the
metric hypotheses it cannot become empty: the empty product has root
\(+1\), while Section 4 proves that the preserved root has two proper sign
gcds.

## 6. Quasipolynomial scope is stated at the correct level

If a wrapped cycle has length \(k\) and every anchor is at most \(H>1\),
then

\[
H^k\ge A_{\mathcal C}>\sqrt N,
\qquad
k>{\log N\over2\log H}.
\]

For \(n=\lceil\log_2(N+1)\rceil\), every fixed-polylogarithmic exponent
satisfies \((\log n)^d=o(n)\). Consequently a family whose **total raw
anchor magnitude** is bounded by
\(2^{(\log n)^{O(1)}}\) cannot contain a wrapped positive cycle for all
sufficiently large \(n\). This is an arithmetic magnitude boundary, not a
runtime lower bound.

The displayed shorthand
\(2^{(\log n)^{O(1)}}=2^{o(n)}\) must be read as the implication used in
the proof: every fixed quasipolynomial magnitude is \(2^{o(n)}\). The two
growth classes are not equal in the reverse direction. This notation does
not affect any theorem.

The two open scopes are also accurate.

1. With anchors at most \(n^3\), the lower bound is only
   \(\Omega(n/\log n)\) edges. One specified trajectory of that length has
   polynomially many records. V3 claims neither a selector nor affordable
   exhaustive branching.
2. P118/F130 permits at most \(D=L^2\) named atoms and exponents through
   \(E=2^{L^2}\). An expanded square anchor can therefore have
   quasipolynomial bit length and magnitude above \(\sqrt N\), while its
   representation and arithmetic remain within the existing
   quasipolynomial cap. V3 makes no cycle-existence claim for such a word.

Thus V3 does not overextend the obstruction to the complete P128 source.

## 7. The \(N=35\) equality certificate passes

The reductions and inverses are

\[
13\cdot2^2=17+35,
\qquad
17\cdot3^2=13+4\cdot35,
\]

\[
17^{-1}=33\pmod{35},
\qquad
13^{-1}=27\pmod{35}.
\]

Hence the actual values are

\[
561,\quad1716,\quad351,\quad4131.
\]

Their positive exact root is

\[
(13)(17)(2)(3)(33)(27)=1{,}181{,}466,
\]

which is \(6\pmod{35}\). The anchor and residual-root products are
\(\mathcal A=6\) and \(S=1\), so

\[
\mathcal A^2-S^2=35,
\qquad
6=\sqrt{35+1},
\]

and

\[
\gcd(5,35)=5,
\qquad
\gcd(7,35)=7.
\]

This now validates, rather than contradicts, the non-strict lower endpoint.
The four exact values are distinct. The centers are pairwise-coprime units,
and the anchor words meet the stated support and exponent bounds. V3
correctly labels the basis occurrence as conditional; it does not claim
that the actual P118 transcript for \(N=35\) reaches this basis.

## 8. Carry determinant and rectangle checks pass

For two endpoints,

\[
\Delta=sc-td=qa^2s-rb^2t.
\]

If \(h=\gcd(c,d)\), then \(h\mid\Delta\). The strict carry bounds give

\[
|\Delta|<{qr a^2b^2\over N}.
\]

Therefore \(hN\ge qr a^2b^2\) forces \(|\Delta|<h\), hence
\(\Delta=0\). In the zero case, the coprime reduction of the two carries
gives

\[
c=\tau z,
\quad d=\sigma z,
\quad qa^2=\tau(z+gN),
\quad rb^2=\sigma(z+gN).
\]

The two bridges then form an exact square whose normalized root is
\((z+gN)/z\equiv1\pmod N\). The separate zero-carry case is also a product
of root-\(+1\) squares.

Finally, direct modular substitution sends the four cross-star endpoints to

\[
u,\quad u\alpha,\quad u\beta,\quad u\alpha\beta.
\]

Thus the claimed P114 rectangle embedding is exact. V3 makes no density or
all-input hitting claim for its determinant.

## 9. Exact surviving claim and remaining gate

V3 is a correct conditional factoring certificate plus a sharp negative
boundary:

\[
\boxed{
\text{a positive directed cycle with a wrapped edge has }
\prod_ea_e>\sqrt N.
}
\]

It does not prove a public path selector, a cycle-existence theorem, a
residual-square law, a non-global root for multiple wrapped cycles, or an
all-input factoring algorithm. Those omissions are stated explicitly and
are not hidden assumptions in the proof.
