# Proof-blind reconstruction: internal-edge matching composition

## 1. The three-variable multiplication gadget

Let the left vertices be \(L_1,L_2,L_3\), the right vertices be
\(R_1,R_2,R_3\), and let the adjacency matrix (left vertices indexing rows)
be

\[
A=\begin{pmatrix}
1&1&0\\
1&1&1\\
1&1&1
\end{pmatrix}.
\]

A perfect matching is the same as a permutation \(\sigma\in S_3\) for which
every edge \(L_iR_{\sigma(i)}\) is present.  The only absent edge is
\(L_1R_3\), so the permitted permutations are exactly

\[
(1,2,3),\qquad (1,3,2),\qquad (2,1,3),\qquad (2,3,1).
\]

Mark, in this order, the three edges

\[
a=L_1R_2,\qquad b=L_2R_3,\qquad c=L_3R_1.
\]

Their occupancy words in the four perfect matchings are

\[
\begin{array}{c|c}
\sigma & (\mathbf 1_{a\in M},\mathbf 1_{b\in M},\mathbf 1_{c\in M})\\ \hline
(1,2,3)&000\\
(1,3,2)&010\\
(2,1,3)&100\\
(2,3,1)&111
\end{array}
\]

Thus, on writing the three coordinates as \((x,y,z)\), the support is
exactly

\[
\{000,010,100,111\}=\{(x,y,z)\in\{0,1\}^3:z=xy\}.
\]

Each word is produced by one and only one perfect matching, so every allowed
assignment has multiplicity one.

## 2. The three-way copy gadget

Now take the bipartite graph with adjacency matrix

\[
C=\begin{pmatrix}
1&1&0\\
0&1&1\\
1&0&1
\end{pmatrix}.
\]

This is a six-cycle.  Its two perfect matchings are

\[
M_0=\{L_1R_1,L_2R_2,L_3R_3\}
\]

and

\[
M_1=\{L_1R_2,L_2R_3,L_3R_1\}.
\]

Indeed, choosing either incident edge at any one vertex forces alternating
choices around the whole cycle, giving precisely these two possibilities.
If the three edges of \(M_1\) are marked, then \(M_0\) has word \(000\) and
\(M_1\) has word \(111\).  Hence the marked-edge signature is exactly
COPY3, again with multiplicity one.

## 3. Why terminal-deletion parity is not an objection to these gadgets

For a graph \(G\) with a boundary set \(B\), define its boundary-deletion
family by

\[
\mathcal F(G,B)=\{X\subseteq B:G-X\text{ has a perfect matching}\}.
\]

Every \(X\in\mathcal F(G,B)\) satisfies

\[
|V(G)|-|X|\equiv 0\pmod 2.
\]

Consequently, all feasible terminal-deletion sets have the same cardinality
parity.  This is the usual terminal-deletion parity restriction.

The bits in Sections 1 and 2 are not deleted terminals.  They record whether
closed, internal edges belong to a perfect matching.  Selecting one such
edge covers two internal vertices; it does not delete one boundary vertex.
Therefore the Hamming parity of an internal-edge occupancy word is not the
cardinality parity in the display above.  In particular, the coexistence of
\(000\) with \(010,100,111\), or of \(000\) with \(111\), violates no
terminal-deletion parity law.

## 4. What a clean four-port connector would require

Consider two occurrence edges whose endpoint ports are all distinct.  Write

\[
P_1=\{p_1,q_1\},\qquad P_2=\{p_2,q_2\},\qquad
B=P_1\mathbin{\dot\cup}P_2,
\]

so \(|B|=4\).  Under the standard port-composition convention, a port
already consumed by the surrounding matching is deleted from the connector
before the connector is matched.  Selecting occurrence edge \(i\) consumes
both ports in \(P_i\).

Equality of the two occurrence-edge bits permits two states: neither
occurrence edge is selected, which presents deletion set \(\varnothing\) to
the connector, and both are selected, which presents deletion set \(B\).
A mismatched value presents \(P_1\) or \(P_2\).  Any state in which only one
endpoint of an occurrence edge is consumed presents one of the other proper
subsets of \(B\).

Thus a connector which is context-independent, supports both equal values,
and itself forbids every mismatched or partial-endpoint state must have

\[
\mathcal F(G,B)=\{\varnothing,B\}. \tag{1}
\]

The demand that this hold in arbitrary surrounding matching contexts is what
prevents relying on a particular surrounding graph to filter out additional
feasible deletion states.

## 5. Symmetric exchange for perfect-matching deletion families

**Theorem.** For every finite graph \(G\), every boundary set
\(B\subseteq V(G)\), and all \(X,Y\in\mathcal F(G,B)\), the following
symmetric-exchange property holds: for every \(e\in X\mathbin\triangle Y\),
there is a distinct \(f\in X\mathbin\triangle Y\) such that

\[
X\mathbin\triangle\{e,f\}\in\mathcal F(G,B). \tag{2}
\]

**Proof.** Choose perfect matchings \(M_X\) of \(G-X\) and \(M_Y\) of
\(G-Y\), and regard both as edge sets in \(G\).  Consider the graph formed
by their symmetric difference \(M_X\mathbin\triangle M_Y\).

At a vertex of \(X\mathbin\triangle Y\), exactly one of the two matchings
has an incident edge, so that vertex has degree one in the symmetric
difference.  A vertex deleted in both matchings has degree zero.  Every
vertex present in both matchings has degree zero if the matchings use the
same incident edge there, and degree two otherwise.  Hence every nontrivial
component is an alternating cycle or an alternating path, and the endpoints
of the paths are exactly the vertices of \(X\mathbin\triangle Y\).

Fix \(e\in X\mathbin\triangle Y\).  Its component is an alternating path
\(P\), whose other endpoint is some distinct
\(f\in X\mathbin\triangle Y\).  Toggle the edges of this path in \(M_X\):

\[
M'=M_X\mathbin\triangle E(P).
\]

At every internal vertex of \(P\), one \(M_X\)-edge is removed and one
\(M_Y\)-edge is added, so the vertex remains matched exactly once.  At an
endpoint \(v\in X\setminus Y\), there was no \(M_X\)-edge and the toggle
adds its \(M_Y\)-edge; correspondingly, \(v\) is removed from the deletion
set.  At an endpoint \(v\in Y\setminus X\), the toggle removes its
\(M_X\)-edge and adds no edge; correspondingly, \(v\) is added to the
deletion set.  All vertices outside \(P\) are unchanged.  Therefore \(M'\)
is a perfect matching of

\[
G-\bigl(X\mathbin\triangle\{e,f\}\bigr),
\]

which proves (2). \(\square\)

## 6. Impossibility of the clean connector

Suppose (1) held.  Apply the theorem with \(X=\varnothing\) and \(Y=B\).
For any \(e\in B\), symmetric exchange supplies a distinct \(f\in B\) for
which

\[
\{e,f\}=\varnothing\mathbin\triangle\{e,f\}
\]

is feasible.  Since \(|B|=4\), this two-element set is neither
\(\varnothing\) nor \(B\), contradicting (1).  Therefore no such clean,
context-independent four-distinct-port connector exists.

This proof already permits an arbitrary number and arrangement of auxiliary
vertices: they are simply the vertices of \(G\setminus B\), and the
symmetric-difference argument places no restriction on them.

Weights do not evade the obstruction when they are nonnegative.  For
nonnegative edge weights, let

\[
Z_G(X)=\sum_{M\text{ perfect in }G-X}\prod_{a\in M}w(a).
\]

Because there is no cancellation, \(Z_G(X)>0\) exactly when \(G-X\) has a
perfect matching using only positive-weight edges.  Equivalently, the
positive support of \(Z_G\) is the boundary-deletion family of the subgraph
obtained by discarding zero-weight edges.  It therefore obeys the same
symmetric-exchange theorem.  In particular, neither strictly positive nor
merely nonnegative weights can produce positive support exactly
\(\{\varnothing,B\}\).

## 7. Exact scope of the obstruction

The theorem rules out only the raw, context-independent four-distinct-port
connector described above.  It does not settle any of the following:

- **Contextual filtering and off-code states.** A connector may admit the
  exchange-forced intermediate states while a particular surrounding graph
  prevents those states from extending to global perfect matchings.
- **Projected auxiliary states.** A construction may retain extra boundary
  or internal state and impose the desired relation only after a projection
  or decoding.  Its raw feasible family need not be (1).
- **Block codes.** A logical bit may be encoded by several physical ports or
  several physical matching states.  Symmetric exchange can then pass
  through states outside the chosen code space without producing a forbidden
  decoded assignment.
- **Vertex identifications.** If occurrence edges share or identify endpoint
  vertices, the physical boundary is not a four-element set of independent
  ports, so the deduction from (1) does not apply in this form.
- **One global multiplication graph.** A monolithic graph may correlate
  internal-edge observables without factoring the construction through a
  universal equality connector.  The local internal-edge gadgets and the
  boundary-deletion no-go theorem do not decide whether such a global graph
  exists.

These are exclusions from the theorem's scope, not claims that the listed
alternatives are possible.

## Verdict

Both local gadgets have the claimed signatures and multiplicity one.  Their
bits are closed internal-edge observables, so terminal-deletion parity is not
a direct objection.  However, exposing two occurrence edges as four distinct
ports and demanding a clean equality connector in every context would require
deletion support \(\{\varnothing,B\}\), and symmetric exchange proves that
support impossible, even with arbitrary auxiliary vertices and nonnegative
edge weights.  No correction to the stated claims is needed; the result is a
no-go theorem for that specific modular composition scheme, not for the open
alternatives listed above.
