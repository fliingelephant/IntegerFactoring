# Hostile audit of F49 coherent Dickson-root selection

## Verdict

**PASS WITH REQUIRED AMENDMENTS.** The one-triangle algebra, the
one-idempotent endpoint theorem, and the anchor probability are correct. The
current Section 5 is not yet an exact proof for systems containing degenerate or
repeated vertices, and its shifted-root sentence needs a definition of
coherence. The scope must also remain one common-idempotent component; the
stated endpoint argument does not automatically cover arbitrary couplings of
several disconnected components.

These are mathematical amendments, not prose-only edits. Under the status rules
in `PROMPT.md`, this exact version has not passed a clean hostile audit and must
not advance. A corrected version requires a fresh hostile audit before the
proof-blind reconstruction step.

## 1. Triangle algebra: passes, including \(C=C^{-1}\)

After the unit changes of variables, eliminate \(Z\) and write

\[
 B=R[f,h]/(f^2-f,h^2-h)\cong R^4.
\]

The remaining root polynomial for \(Z=XY\) has corner values

\[
 0,\quad
 A(B^{-1}-B)B^{-1}(A-A^{-1}),\quad
 B(A^{-1}-A)A^{-1}(B-B^{-1}),\quad
 0.
\]

The middle two values are units under (4.1). Hence quotienting kills exactly
the two unequal-orientation factors of \(R^4\), leaving

\[
 R\times R\cong R[f]/(f^2-f),\qquad h=f.
\]

This is an algebra statement, not merely a statement about \(R\)-points. It
also covers \(C=C^{-1}\), globally or in only one CRT component: although the
isolated polynomial \((Z-C)^2\) would have a nilpotent thickening, the equation
\(Z=XY\) and the two nondegenerate input root pairs remove it. No division by
\(C-C^{-1}\) is used.

## 2. Required correction: degenerate and repeated vertices

If screening leaves \(A_v=s\in\{1,-1\}\), then the raw coordinate algebra

\[
 R[X_v]/((X_v-s)^2)
\]

contains the nonzero nilpotent class \(X_v-s\). Thus “the vertex is a known
constant” is true for \(R\)-valued solutions, because \(R\) is reduced, but is
false for the raw coordinate algebra. Section 5 must explicitly **eliminate
\(X_v\) by the linear equation \(X_v=s\)** before making its exact coordinate-
algebra claim. Equivalently, state the theorem only for the linearly reduced,
screened system.

Connectivity must then be defined after simplifying every triangle, not as
ordinary incidence connectivity through discarded constant vertices. The
needed case analysis is:

- three distinct nondegenerate vertices give the equality of all three
  orientation idempotents by Section 4;
- if \(u=v\) and \(w\ne u\) is nondegenerate, \(X_w=X_u^2\) kills the two
  unequal Boolean corners because \(A_w-A_w^{-1}=A_u^2-A_u^{-2}\) is a unit;
- after substituting one known constant \(s=\pm1\), two distinct remaining
  nondegenerate vertices have equal orientations; the unequal corners differ
  from the required product by a unit;
- a simplified relation containing at most one distinct nondegenerate vertex
  supplies no orientation edge.

In particular, two triangles sharing only a constant vertex need not join
their other orientation pairs. Define the **reduced orientation graph** using
exactly the equalities above. Its connected components, not the naïve original
hypergraph components, have coordinate algebra

\[
 R[f_j]/(f_j^2-f_j).
\]

This supplies the missing proof for repeated and degenerate occurrences.

## 3. Required correction: shifted-root transfer

For a screened shifted pair \(A_i,B_i\), its quadratic alone gives

\[
 Z_i=B_i+f_i(A_i-B_i),\qquad f_i^2=f_i,
\]

with an independent \(f_i\) for each pair. A common \(f\) does not follow from
the individual quadratics.

The valid common-idempotent statement is narrower and should be written
explicitly: for the four shifted sections induced by one trace-compatible
homomorphism \(H\in\{E,E^{-1},G,G^{-1}\}\), the normalized idempotents are the
same for every \(i\). The \(E\) and \(E^{-1}\) sections have respectively
\(f_i=1\) and \(f_i=0\); the \(G\) and \(G^{-1}\) sections have respectively
the two fixed nontrivial CRT idempotents. More generally, a finite shifted-root
system has one \(f\) only after explicit coherence equations have been shown to
identify all \(f_i\) in its reduced orientation graph.

Therefore replace “every coherent section” by this definition and proof. Do
not claim that unspecified shifted-root relations, or the quadratics alone,
force coherence.

## 4. Endpoint theorem: passes with one-component scope

For one common idempotent,

\[
 \mathcal A=R[f]/(f^2-f),\qquad
 Q=Q(0)(1-f)+Q(1)f,
\]

so Theorem 6.1 is correct. For a finite system \(Q_r(f)=0\), if a mixed
idempotent solves every equation and an endpoint fails the system, choose an
equation failing there; its endpoint value has exactly one zero CRT component,
and its gcd with \(N\) is proper. This argument is equation-by-equation and is
valid for polynomial expressions in the established coordinate algebra.

It must not be stated without qualification for several disconnected
idempotents or for systems with additional existential variables. For example,
\(Q(f_1,f_2)=f_1-f_2\) retains common mixed assignments and excludes the public
corners \((0,1)\) and \((1,0)\), but those excluded endpoint values are units,
not factor-bearing. Once this equation is recognized as joining the two
orientations, the correct one-variable endpoints are only \((0,0)\) and
\((1,1)\). Thus every selector claim must first prove reduction to one common
\(f\). Arbitrary polynomial coupling of genuinely disconnected components is
outside the proved endpoint dichotomy.

## 5. Anchor probability: passes exactly

For a uniform unit, the two coordinates of \(E(a)\) are independent and
uniform in image groups of orders \(h_p,h_q\). The no-factor/no-anchor event is
exactly the synchronized pair \((1,1)\), together with \((-1,-1)\) iff both
orders are even. Hence its conditional probability is exactly

\[
 \frac{1+\mathbf 1_{2\mid h_p,\,2\mid h_q}}{h_ph_q}.
\]

Since \(h_p<h_q\), this is at most \(1/2\); equality occurs exactly at
\((h_p,h_q)=(1,2)\), equivalently \(q=2p-1\). A raw residue is a unit with
probability at least \(8/15\), so even ignoring proper gcds from nonunits, a
factor or unit-difference anchor occurs with probability at least \(4/15\) per
trial. The claimed constant expected trial count and polynomial bit cost
follow.

## Corrected scope

After the amendments, F49 proves an exact obstruction for a finite, explicitly
given polynomial system whose screened and linearly reduced root relations have
already been proved to form one common-idempotent component. It does not cover
raw degenerate quadratic schemes, unspecified shifted-root coherence,
arbitrary multicomponent polynomial couplings, auxiliary existential variables,
or any of the nonalgebraic and modulo-\(N^2\) reopen conditions already listed
by the candidate.
