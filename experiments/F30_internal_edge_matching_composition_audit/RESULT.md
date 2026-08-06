# Hostile audit of F30 — internal-edge matching composition

**Audit status:** fresh hostile proof-only audit.

**Candidate audited:**
`experiments/F30_internal_edge_matching_composition_kill/RESULT.md`.

**Materials checked:** `PROMPT.md`, `REGISTRY.md`, the relevant F21
entries in `FAILED.md`, promoted P38 in `PROVED.md`, C35 in
`notes/Progress.md`, and the proof and verification record under
`experiments/F28_positive_matching_factor_graph_*`.

No computation was run. The finite matching lists were checked directly
from the displayed adjacency matrices.

## Verdict

> **CLEAN PASS.**

I found no fatal error, required mathematical correction, unsupported
quantifier, or scope inflation in the candidate.

The exact result that survives is narrow but genuine:

1. closed internal-edge occupancy realizes AND and COPY with positive
   multiplicity one;
2. a clean four-port connector whose only boundary states are the two equal
   occupancy states cannot be a perfect-matching signature; and
3. this obstruction does not extend to contextual filtering, projected
   auxiliary states, block encodings, approximate/off-code constructions, or
   one global multiplication graph.

This is an auxiliary obstruction, not a factoring algorithm. It therefore
does not satisfy the top-level goal and must not be reported as completing
`PROMPT.md`. Subject to the required proof-blind reconstruction, it is fit
to be promoted as the next precisely scoped F21 boundary.

## 1. The closed AND enumeration is complete

The displayed graph is \(K_{3,3}\) with only \(L_1R_3\) removed. A perfect
matching corresponds to a permutation \(\pi\in S_3\), and the missing edge
excludes exactly the two permutations with \(\pi(1)=3\). The four survivors
are therefore exactly

\[
123,\qquad132,\qquad213,\qquad231.
\]

There is no fifth matching.

For the marked edges

\[
e_x=L_1R_2,\qquad e_y=L_2R_3,\qquad e_z=L_3R_1,
\]

the incidence table is

\[
\begin{array}{c|ccc}
\pi&x&y&z\\ \hline
123&0&0&0\\
132&0&1&0\\
213&1&0&0\\
231&1&1&1.
\end{array}
\]

These are all four and only the four rows satisfying \(z=xy\). Each row has
one matching preimage. The marked edges are mutually disjoint, but that
fact is not used to smuggle in a boundary deletion convention: they remain
ordinary internal edges of a closed graph.

Thus the candidate correctly demonstrates that P38's terminal-signature
obstruction is not an obstruction to arbitrary labels read from completed
internal matchings.

## 2. The closed COPY enumeration is complete

The second adjacency matrix allows

\[
L_1\in\{R_1,R_2\},\quad
L_2\in\{R_2,R_3\},\quad
L_3\in\{R_1,R_3\}.
\]

If \(L_1R_1\) is chosen, the remaining two rows are forced to
\(L_2R_2,L_3R_3\). If \(L_1R_2\) is chosen, they are forced to
\(L_2R_3,L_3R_1\). Hence the only perfect matchings are the displayed

\[
M_0=\{L_1R_1,L_2R_2,L_3R_3\},
\qquad
M_1=\{L_1R_2,L_2R_3,L_3R_1\}.
\]

Marking the three edges of \(M_1\) gives incidence words \(000\) and \(111\),
again each once. The graph is indeed a six-cycle. The claim that disjoint
union alone does not equate marked bits across components is immediate:
perfect matchings of a disjoint union are independent choices of component
matchings.

## 3. The two-endpoint state model is correct

For a marked occurrence edge \(e=uv\), choosing \(e\) covers both endpoints;
not choosing it forces both endpoints to be covered by other edges in a
perfect matching. Replacing \(e\) by

\[
u-a-b-v
\]

has exactly the two stated local states. At \(a\), either \(ua\) or \(ab\)
must be chosen. In the first case \(bv\) is then forced; in the second it is
forbidden. This gives a bijection between perfect matchings before and after
the odd subdivision, with the old occupied state represented by \(ua,bv\)
and the old unoccupied state represented by \(ab\).

The candidate correctly calls this transmission of one occurrence rather
than creation of a second occurrence pair.

## 4. Universality really forces the two-word deletion support

Let the two removed occurrence edges have four distinct endpoint ports

\[
B=B_1\sqcup B_2,\qquad |B_1|=|B_2|=2.
\]

When a connector \(K\) is glued to external contexts along \(B\), every
global perfect matching partitions the boundary according to whether a
boundary vertex is matched externally or inside \(K\). If \(S\subseteq B\)
is the externally matched set, the connector contributes exactly a perfect
matching of \(K-S\).

For both occurrence bits zero, the contexts cover all four ports, so the
connector state is \(S=B\). For both bits one, the connector covers all four
ports, so it is \(S=\varnothing\). Every other \(S\) is either a mismatched
pair state or covers only one endpoint of at least one occurrence. Thus the
definition of a clean equality connector is exactly

\[
\operatorname{supp}F_K=\{\varnothing,B\}.
\]

The word “arbitrary” in the candidate is doing real work. If an extra
\(S\) were supported, an adversarial external context could activate it:
attach a private leaf to each port in \(S\) and no external edge to each port
outside \(S\). The leaf edges cover exactly \(S\), while a matching of
\(K-S\) covers the complement. Hence extra support cannot be declared
harmless uniformly over all contexts. It can be harmless only after a
specific global construction proves that its own context never completes
that state, which the candidate explicitly leaves open.

Complementing any port convention twists both supported words by one fixed
set. Their symmetric difference remains the four occurrence ports. Common
fixed auxiliary boundary selections occur in both words and likewise cancel
from that symmetric difference. These observations are correct.

This argument is deliberately about four distinct ports and ordinary graph
gluing. Vertex identifications, projected assignment-dependent auxiliary
states, larger encodings, or a globally fused graph are not silently
included; the candidate lists them as survivors.

## 5. The symmetric-exchange proof is valid in every endpoint case

For supported deletion sets \(X,Y\), regard perfect matchings \(M_X\) of
\(H-X\) and \(M_Y\) of \(H-Y\) as edge sets of the common ambient graph
\(H\). In \(M_X\triangle M_Y\):

- a vertex outside \(X\triangle Y\) has degree zero or two; and
- a vertex in \(X\triangle Y\) has degree one.

Consequently every noncycle component is an alternating path with two
distinct endpoints in \(X\triangle Y\). Starting at a prescribed
\(e\in X\triangle Y\), let \(f\ne e\) be the other endpoint. Toggling the
path in \(M_X\) gives a perfect matching of

\[
H-\bigl(X\triangle\{e,f\}\bigr).
\]

This remains true for all four endpoint-type combinations:

- two endpoints in \(X\setminus Y\) are both restored;
- two endpoints in \(Y\setminus X\) are both deleted; and
- one endpoint of each type swaps which boundary vertex is deleted.

Taking \(X=\varnothing\), \(Y=B\), and any \(e\in B\), exchange therefore
forces a supported two-element set \(\{e,f\}\). It can be neither
\(\varnothing\) nor \(B\), contradicting the desired two-word support.

The proof is stronger than the bipartite application: it holds for every
finite graph. It neither assumes planarity nor bounds the size or number of
internal auxiliary vertices.

## 6. Positive weights and auxiliary structure do not evade support

With nonnegative edge weights, a weighted perfect-matching total is positive
exactly when there is a perfect matching using only positive-weight edges.
Deleting zero-weight edges therefore reduces the support question to the
unweighted graph. Strictly positive weights can alter multiplicities but
cannot remove the exchange-forced intermediate support.

Parallel edges similarly alter counts only. Arbitrary internal vertices,
disconnected pieces, nonplanarity, and an arbitrarily large connector were
already permitted in the alternating-path proof. Thus the candidate's
weight and auxiliary-vertex quantifiers are sound.

Signed or complex cancellations, and weights that merely make unwanted
states small rather than zero, are outside the stated positive exact-support
claim. The candidate does not claim otherwise.

## 7. Novelty and exact scope relative to the durable record

F30 is not a disguised resubmission of the route closed by P38. P38 itself
explicitly left closed internal-edge observables open. The two micrographs
occupy that survivor and supply exact positive relations that the direct
single-rail and one-hot terminal models cannot supply.

The connector obstruction is a new application of P38's already promoted
matching-support theorem, not a new proof that all internal-edge decoders
fail. This is described honestly. It closes only the proposed clean,
context-independent, four-port occurrence equality wire.

The candidate correctly keeps open:

1. one globally interleaved multiplication-specific graph;
2. off-code connector states suppressed by the complete surrounding graph;
3. assignment-dependent auxiliary states followed by projection;
4. block and heterogeneous occurrence codes;
5. fused multi-gate or cycle-state constructions;
6. global positive multiplicity balancing; and
7. weaker sampling laws with inverse-polynomial useful matching mass instead
   of one equal positive fiber for every ordered divisor.

The sentence in the Outcome calling contextual global suppression “the exact
remaining escape” must be read locally as the remaining escape from this
clean-connector contradiction; Sections 6 and 7 explicitly preserve the
other code-changing escapes. Read in that stated scope, it is not an
overclaim.

The F30 result is also distinct from X30/P36: X30 concerns exact holographic
contraction after basis changes, while F30 concerns positive individual
perfect matchings and boundary support. No tensor-contraction hardness or
terminal gcd is being imported.

## 8. Promotion boundary

The following statement is supported by this audit:

> A closed six-vertex bipartite matching decoder realizes AND, and a closed
> six-cycle realizes COPY, both with multiplicity one. However, no finite
> positive matching gadget on four distinct occurrence ports has deletion
> support consisting exactly of the two equal occupancy states. Matching
> symmetric exchange forces an intermediate two-port state.

Nothing stronger is supported. In particular, the audit proves neither the
nonexistence of a positive matching representation of multiplication nor a
polynomial-time factoring algorithm. The next verification step required
by `PROMPT.md` is a fresh proof-blind end-to-end reconstruction from the bare
statement and key ideas, without access to this proof.
