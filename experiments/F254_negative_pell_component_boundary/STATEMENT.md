# F254: the tailored negative-Pell component source is not universal

## Status

This is a proof-only, self-audited candidate counterexample. It closes only
the claim that the complete negative-Pell recurrence below must create an
exact-square dependency. It is not a probability bound for randomized
discriminants and not a factoring obstruction.

## Tailored Pell row and its public components

Let (N) be odd and let

\[
b^2-2y^2=-1,
\qquad 1<y<N.
\]

Put

\[
T=N+y,
\qquad D=T^2-2,
\qquad S=T^2-1,
\]

and define the canonical Pell row

\[
A=1+Dy^2.
\]

Then (D) is positive and nonsquare,

\[
S^2-DT^2=1,
\qquad S\equiv y^2-1\pmod N,
\]

and (S\bmod N) is a supplied square root of (A\bmod N).

Both (b) and (y) are odd. With

\[
u={b-1\over2},
\qquad v={b+1\over2},
\]

there is an exact public factorization

\[
\boxed{
A=F_-(N)F_+(N),
\quad
F_-(X)=yX+2u^2,
\quad
F_+(X)=yX+2v^2.}
\]

Modulo (N), each component is twice a square. Hence every even component
subset is a congruence of squares with a known modular root. This gives a
component-level extension of the original-row P66 bank.

For any two components (F_i(X)=y_iX+2w_i^2) and
(F_j(X)=y_jX+2w_j^2),

\[
\boxed{
\operatorname{Res}(F_i,F_j)
=2(y_iw_j^2-y_jw_i^2).}
\]

Thus every rational prime shared by the two specialized integers divides
this public determinant. Distinct nonassociate component forms have no
generic polynomial square dependency. Any cross-component square-class
reuse is an arithmetic-specialization event supported by these determinants.

## Complete counterexample

Take

\[
N=143=11\cdot13.
\]

The positive solutions to (b^2-2y^2=-1), in increasing (y), begin

\[
(b,y)=(1,1),(7,5),(41,29),(239,169).
\]

These are consecutive solutions. Therefore the complete admissible window
(1<y<N) contains exactly (y=5) and (y=29).

For (y=5),

\[
(b,u,v,T,D,S)=(7,3,4,148,21902,21903),
\]

and

\[
A=733\cdot747
=733\cdot3^2\cdot83,
\qquad S\equiv24\pmod{143}.
\]

For (y=29),

\[
(b,u,v,T,D,S)=(41,20,21,172,29582,29583),
\]

and

\[
A=4947\cdot5029
=(3\cdot17\cdot97)(47\cdot107),
\qquad S\equiv125\pmod{143}.
\]

The four component square-class columns are therefore

\[
733,
\quad 3^2\cdot83,
\quad3\cdot17\cdot97,
\quad47\cdot107.
\]

They have respective private odd-prime parity rows

\[
733,
\quad83,
\quad17,
\quad47.
\]

Consequently the full four-column parity matrix has rank four. It has no
nonzero exact-square subset, even before imposing the even-cardinality
condition required for a known component root. The original two-row bank
also has rank two.

All direct screens are inert: every displayed component, supplied root,
(b,y,u,v,T,D), and every pairwise component resultant is coprime to
(143). The two root congruences are

\[
24^2\equiv547551\equiv4\pmod{143},
\]

\[
125^2\equiv24878463\equiv38\pmod{143}.
\]

Hence the complete admissible negative-Pell recurrence supplies neither a
direct factor nor any P66 dependency on this input.

## Exact scope

The certificate refutes only a universal assertion for this specific
tailored construction and its complete (1<y<N) negative-Pell bank. It
does not bound the probability that another public randomized choice of
(D), index, window, or mixed source creates a useful dependency. It also
does not refute the general retrospective multirow P66 channel left open by
P213 and P214.
