# F30 follow-up: closed internal-edge AND survives, but a clean occupancy connector does not

**Status:** promoted as P42 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Family:** F21.

**Closest prior route and material difference.**  F28's candidate boundary
concerns terminal-deletion signatures: direct single rail has fixed parity,
and exact one-hot dual rail can express only a subcube.  The present report
tests the most immediate escape, in which logical bits are decoded from
**internal edge occupancy in a closed graph**.  That escape really does
realize COPY and AND.  The report then kills only a context-independent
connector that would identify two such internal-edge occurrences without
off-code states.

**Classification.**  This is a positive survivor followed by evidence
against one exact auxiliary composition mechanism.  It is not a failure of
closed global decoders, globally filtered off-code states, block codes,
assignment-dependent auxiliary states, or a globally interleaved
multiplication-specific graph.

No computation was used.  All finite matching lists are displayed in full.

## Outcome

There is a six-vertex bipartite graph with exactly four perfect matchings
whose occupancies on three marked edges are

\[
000,\quad010,\quad100,\quad111.
\]

These are exactly the truth rows of \(z=xy\).  A six-cycle has two
perfect matchings whose three alternating marked edges give \(000,111\),
exactly COPY\(_3\).  Thus the direct terminal-signature obstruction does
not apply to a decoder that reads internal edges of a closed graph.

The obvious modular composition still fails.  One occurrence bit occupies
an edge and therefore consumes two endpoints.  A universal positive matching
connector that identifies two such occurrences, for arbitrary surrounding
contexts and with no off-code boundary states, would need a four-terminal
deletion support consisting of only

\[
\{\varnothing,B\},\qquad |B|=4.
\]

That family violates matching delta-matroid exchange.  No amount of internal
auxiliary structure or positive weighting can realize the clean connector.

This does not rule out a single globally designed graph in which the
surrounding multiplication construction itself suppresses every partial
connector state.  That is the exact remaining escape.

## 1. A closed positive AND decoder

Let the left vertices be \(L_1,L_2,L_3\), the right vertices be
\(R_1,R_2,R_3\), and take adjacency matrix

\[
A_{\rm AND}=
\begin{pmatrix}
1&1&0\\
1&1&1\\
1&1&1
\end{pmatrix}.
\tag{1.1}
\]

Because \(L_1R_3\) is the only forbidden position in an otherwise complete
\(3\times3\) bipartite graph, the perfect matchings are precisely the four
permutations whose first image is \(1\) or \(2\):

\[
\begin{array}{c|c}
\text{permutation}&\text{matching edges}\\ \hline
123&L_1R_1,\ L_2R_2,\ L_3R_3\\
132&L_1R_1,\ L_2R_3,\ L_3R_2\\
213&L_1R_2,\ L_2R_1,\ L_3R_3\\
231&L_1R_2,\ L_2R_3,\ L_3R_1.
\end{array}
\tag{1.2}
\]

Mark the three mutually disjoint edges

\[
e_x=L_1R_2,
\qquad
e_y=L_2R_3,
\qquad
e_z=L_3R_1.
\tag{1.3}
\]

Decode a matching to \((x,y,z)\in\{0,1\}^3\) by the three edge-incidence
indicators.  Reading (1.2) gives

\[
\begin{array}{c|c}
123&000\\
132&010\\
213&100\\
231&111.
\end{array}
\tag{1.4}
\]

The decoded relation is exactly

\[
z=xy,
\tag{1.5}
\]

and every truth row has multiplicity one.  There is no cancellation, signed
weight, interpolation, or hidden extra matching.

This does not contradict the single-rail parity obstruction.  The marked
edges are internal observables of a **closed** graph.  They are not boundary
vertices whose selected set is deleted before an internal perfect matching
is counted.

## 2. A closed positive COPY decoder

Take the six-cycle with bipartite adjacency matrix

\[
A_{\rm COPY}=
\begin{pmatrix}
1&1&0\\
0&1&1\\
1&0&1
\end{pmatrix}.
\tag{2.1}
\]

Its only perfect matchings are

\[
M_0=\{L_1R_1,L_2R_2,L_3R_3\},
\qquad
M_1=\{L_1R_2,L_2R_3,L_3R_1\}.
\tag{2.2}
\]

Mark the three edges of \(M_1\).  Their incidence vectors on
\(M_0,M_1\) are \(000\) and \(111\).  Hence a closed internal-edge
decoder realizes COPY\(_3\), again with multiplicity one.

Disjoint unions of these graphs do not form a Boolean circuit: their marked
edge values are independent across components.  A composition operation is
still required.

## 3. Why an edge occurrence is a two-endpoint state

Let \(e=uv\) be a marked edge in a matching graph.  When \(e\) is chosen,
both \(u\) and \(v\) are covered by the occurrence.  When it is not chosen,
both vertices must be covered through other incident edges.  The logical
state therefore changes the availability of a **pair** of vertices, not one
terminal.

Subdividing \(e\) illustrates transmission but not copying.  Replace it by
the three-edge path

\[
u-a-b-v.
\]

At the two new degree-two vertices, perfect matching forces the two endpoint
edges \(ua,bv\) to be chosen together or omitted together:

- if they are chosen, the middle edge \(ab\) is omitted and both old
  endpoints are covered, reproducing the occupied state of \(e\);
- if they are omitted, \(ab\) is chosen and both old endpoints remain for
  their surrounding graph, reproducing the unoccupied state.

Thus an odd subdivision can transport one occurrence between the same two
old constraints.  It does not create a second pair of endpoints carrying the
same bit.

## 4. Formal universal-connector requirement

Consider two otherwise arbitrary matching contexts.  Remove one occurrence
edge from each, leaving endpoint pairs

\[
B_1=\{a_1,b_1\},
\qquad
B_2=\{a_2,b_2\},
\qquad
B=B_1\sqcup B_2.
\]

A **clean context-independent occupancy connector** is a finite graph
\(K\), with boundary vertices \(B\) and arbitrary internal vertices, that
has the following property under every pair of surrounding contexts:

- it permits the state in which both contexts cover their own endpoint pair
  elsewhere, corresponding to both occurrence bits being zero;
- it permits the state in which the connector covers all four endpoints,
  corresponding to both occurrence bits being one; and
- it permits no mismatched bit state and no state in which only one endpoint
  of an occurrence pair is covered by the connector.

Use the standard deletion signature

\[
F_K(S)=\#\operatorname{PM}(K-S),
\qquad S\subseteq B,
\tag{4.1}
\]

where \(S\) is the set of boundary vertices already covered by the external
contexts.  In the zero-zero state, all four endpoints are externally covered,
so \(S=B\).  In the one-one state, none is externally covered, so
\(S=\varnothing\) and \(K\) covers them.  Exactness for arbitrary contexts
requires

\[
\operatorname{supp}F_K=\{\varnothing,B\}.
\tag{4.2}
\]

If the opposite convention is used, the support is twisted by a fixed set.
Its two words still have symmetric difference of size four.  Common fixed
auxiliary boundary bits likewise appear in both words and cancel from the
symmetric difference.

The word **arbitrary** is essential.  If (4.1) has additional partial
support, a specially designed surrounding graph might make those states
globally impossible.  Such contextual filtering is one of the open routes;
it is excluded only from the universal connector defined here.

## 5. Matching delta-matroid exchange kills the connector

For completeness, the needed support theorem has a short direct proof.
Let \(H\) be any finite graph with boundary \(B\), and let

\[
\mathcal F_H=\{S\subseteq B:H-S\text{ has a perfect matching}\}.
\]

Take \(X,Y\in\mathcal F_H\) and perfect matchings \(M_X,M_Y\) of
\(H-X,H-Y\).  In the symmetric difference
\(M_X\triangle M_Y\), every non-cycle component is an alternating path
whose endpoints lie in \(X\triangle Y\).  Starting at any
\(e\in X\triangle Y\), follow its path to the other endpoint
\(f\in X\triangle Y\).  Toggling \(M_X\) along that path produces a
perfect matching after toggling the two boundary deletions.  Therefore

\[
\forall X,Y\in\mathcal F_H,\ \forall e\in X\triangle Y,
\ \exists f\in X\triangle Y:
X\triangle\{e,f\}\in\mathcal F_H.
\tag{5.1}
\]

Now suppose (4.2) held.  Take \(X=\varnothing\), \(Y=B\), and any
\(e\in B\).  The other path endpoint \(f\) is distinct from \(e\).
Equation (5.1) would require the two-element set \(\{e,f\}\) to belong to
\(\mathcal F_K\), contradicting (4.2).

Hence no clean context-independent occupancy connector exists.

The proof permits nonplanarity, arbitrary internal auxiliary vertices,
parallel positive contributions, and arbitrary nonnegative edge weights:
after zero-weight edges are removed, positivity changes multiplicities but
not support.  It also permits an arbitrarily large connector.  The
obstruction is not a small-gadget search.

## 6. What is and is not closed

The following statements are exact.

1. Closed internal-edge decoding escapes the direct terminal parity and
   one-hot subcube obstructions: (1.1) realizes AND and (2.1) realizes
   COPY.
2. These closed primitives do not compose by disjoint union.
3. No universal positive connector with arbitrary internal structure can
   identify two occurrence-edge states while exposing only the two clean
   equal states to arbitrary contexts.

The following remain open.

1. A single globally interleaved graph whose internal matching is decoded
   directly as the entire multiplication witness, with no modular gate
   composition.
2. Connectors with partial/off-code support that the specific surrounding
   graph provably suppresses.
3. Assignment-dependent auxiliary boundary states whose projection enforces
   equality even though the full supported family contains exchange states.
4. Block codes in which a logical value is a family of matching patterns,
   rather than the occupancy of one edge.
5. Heterogeneous occurrence encodings, cycle states, fused multi-gate blocks,
   and a globally balanced multiplicity construction.
6. A graph whose decoder gives nontrivial factors inverse-polynomial total
   matching mass without a constant multiplicity for every witness.

In particular, the delta-matroid contradiction must not be applied directly
to the labels of internal matchings of a closed graph.  For a closed graph
the boundary family has only the empty set, and (5.1) is vacuous.  The AND
survivor is an explicit warning against that overclaim.

## 7. Reopen condition

The next F21 attempt is materially new only if it does one of the following:

- gives a concrete globally interleaved bipartite graph construction for
  multiplication and proves its decoder and matching-mass law;
- gives a contextual connector, lists all of its off-code states, and proves
  that the complete surrounding graph eliminates them without cancellation;
  or
- changes the occurrence code so that logical equality no longer requires
  the forbidden clean four-terminal support.

Reusing the closed micrographs while assuming a clean universal occupancy
wire is covered by this obstruction.  The top-level positive-matching route
and the factoring goal remain open.
