# F123 — Canonical-Carry Recurrence Determinant Screen

## Verdict

**Status: self-audited candidate.**

There is an exact constant-size carry determinant. It gives a proper factor
on one trial-division-hard semiprime where the declared direct
canonical-inverse screens and the complete exact-square decoder are both
null on the same finite public source.

This is a real finite capability separation between the named screens. It is
not an all-input factoring theorem. It is not an adaptive feedback result.
It supplies no proved success density.

The supplied name “GCT carry obstruction” is retained as provenance only.
The precise mathematical name used here is **canonical-carry recurrence
determinant** or **CRT rank-mismatch screen**.

## 1. Exact determinant identity

Let \(N\ge3\) be odd and let \(a\) be a unit with \(1<a<N\). For
\(1\le j\le4\), define

\[
c_j=[a^j]_N,\qquad
w_j=[c_j^{-1}]_N,\qquad
\kappa_j=\frac{c_jw_j-1}{N}.
\]

Put

\[
L_N(a)=
\begin{pmatrix}
1&c_1&w_1&\kappa_1\\
1&c_2&w_2&\kappa_2\\
1&c_3&w_3&\kappa_3\\
1&c_4&w_4&\kappa_4
\end{pmatrix}
\]

and

\[
\Omega_N(a)=
\kappa_4-\kappa_1+
(1+a+w_1)(\kappa_2-\kappa_3).
\]

Then

\[
\boxed{
\det L_N(a)\equiv
(a-1)^3(a+1)w_1^2\,\Omega_N(a)
\pmod N.}
\]

Consequently, if

\[
\gcd(a(a^2-1),N)=1,
\]

then the prefactor is a unit and

\[
\boxed{
\gcd(\det L_N(a),N)=\gcd(\Omega_N(a),N).}
\]

This version does not require \(N\) to be squarefree. The source note stated
the gcd equality for squarefree \(N\); the proof works directly modulo \(N\)
under the displayed unit condition.

### Proof

Modulo \(N\),

\[
c_j\equiv a^j,\qquad w_j\equiv a^{-j}.
\]

Set

\[
s=1+a+a^{-1}.
\]

The three sequences \(1,a^j,a^{-j}\) satisfy

\[
u_{j+3}-s u_{j+2}+s u_{j+1}-u_j=0.
\]

Apply, modulo \(N\), the row operation

\[
R_4\leftarrow R_4-sR_3+sR_2-R_1.
\]

The first three entries of the new fourth row are zero. Its last entry is
\(\Omega_N(a)\), because \(w_1\equiv a^{-1}\pmod N\). The remaining minor is

\[
\det
\begin{pmatrix}
1&a&a^{-1}\\
1&a^2&a^{-2}\\
1&a^3&a^{-3}
\end{pmatrix}
=\frac{(a-1)^3(a+1)}{a^2}.
\]

Replacing \(a^{-2}\) by \(w_1^2\) gives the stated integral congruence.
Multiplication by a unit does not change a gcd with \(N\).

## 2. Exact finite certificate

Take

\[
\boxed{
N=4{,}840{,}987=1{,}847\cdot2{,}621.}
\]

Both factors pass deterministic 64-bit primality testing. The input has
\(n=23\) bits, and

\[
1{,}847>n^2=529.
\]

Thus it is trial-division-hard under this project’s declared local
convention.

For \(a=68\), the four canonical relations are

\[
\begin{array}{c|r|r|r}
j&c_j&w_j&\kappa_j\\ \hline
1&68&71{,}191&1\\
2&4{,}624&4{,}486{,}079&4{,}285\\
3&314{,}432&3{,}696{,}712&240{,}109\\
4&2{,}017{,}428&2{,}047{,}711&853{,}361
\end{array}
\]

and

\[
\Omega_N(68)=-16{,}803{,}964{,}880.
\]

The public factor certificate is

\[
\boxed{
\gcd(\Omega_N(68),N)=2{,}621.}
\]

The exact determinant is

\[
\det L_N(68)=937{,}401{,}734{,}708{,}188{,}800,
\]

with local ranks

\[
\operatorname{rank}_{\mathbf F_{1847}}L_N(68)=4,
\qquad
\operatorname{rank}_{\mathbf F_{2621}}L_N(68)=3.
\]

The vector

\[
(1590,1257,283,1)^T
\]

is a right-null vector modulo \(2621\), but not modulo \(1847\).

## 3. Finite source separation

The public source is

\[
2\le a\le4n=92,\qquad 1\le j\le4.
\]

The exact verifier reports:

~~~text
source positions                 364
distinct exact relation values   240
gcd-free exact-value blocks      267
parity rank                      240
kernel dimension                   0
proper direct inverse screens      0
~~~

Thus the complete exact-square decoder has no nonzero dependency on this
finite source. The carry determinant nevertheless factors \(N\) at seed 68.

The verifier also confirms:

- \(68\) has order \(1846\) modulo \(1847\);
- \(68\) has order \(2620\) modulo \(2621\);
- \(\gcd(68^t\pm1,N)=1\) for \(1\le t\le8\); and
- the declared two-point sign and inverse-collision screens on the four
  trajectory residues are all null.

This excludes the named short-order and two-point explanations. It does not
prove algebraic independence from every possible scalar screen.

## 4. Exact algorithmic meaning

For a fixed determinant degree and a polynomial seed range, this screen has
polynomial bit complexity. Every success is verified by a gcd.

The missing theorem is a source law. Nothing here proves that

\[
\Pr_a\bigl(1<\gcd(\Omega_N(a),N)<N\bigr)
\]

is inverse-polynomial on every composite input, or on any unbounded
trial-hard family.

On the displayed modulus, exactly one of the 91 seeds \(2,\ldots,92\)
produces a proper \(\Omega\)-gcd. As a diagnostic only, if these residues
behaved like independent uniform scalars modulo the two factors, the expected
number of accidental proper hits would be about \(0.084\), and the chance of
at least one hit would be about eight percent. No uniformity or independence
claim is made. This baseline shows why one post-discovery witness is not
evidence of an asymptotic bias.

## 5. Relation to feedback

F123 consumes the same canonical data as F26:

\[
(c,w,\kappa),\qquad cw=1+\kappa N.
\]

It does not perform the operation that defines the feedback route:

- no feedback-created block is used;
- no old block is split;
- no new named generator changes the next word menu;
- no retained relation changes a later cross-layer kernel; and
- no recursive state transition is required.

F123 is therefore a new static decoder-side screen, not evidence that
feedback changes the future source grammar.

A feedback-specific certificate would need a preregistered static source on
which every declared carry determinant is null, followed by a
feedback-created block or trajectory that is essential to the first proper
determinant gcd.

## 6. Relation to geometric complexity theory

The determinant is a relative invariant for the left-right action on
\(4\times4\) matrices. Its zero set is the rank-at-most-three determinantal
variety. The two CRT reductions of the public matrix lie in different rank
strata.

This makes “GCT-inspired” a defensible analogy. It does not make the result a
geometric complexity lower bound or an implementation of the GCT program.
The actual proof uses a four-row recurrence, a determinant, and a gcd. The
closest project precedent is the determinant/rank-mismatch template already
present in F03, F04, and Inspiration A2.

No publication-priority claim is made.

## 7. General fixed-weight hierarchy

For a fixed weight set \(W=\{m_1,\ldots,m_d\}\), form \(d+1\) rows whose
first \(d\) entries are

\[
[a^{m_1j}]_N,\ldots,[a^{m_dj}]_N
\]

and whose last entry is a chosen carry feature such as \(\kappa_j\).
Modulo each prime divisor, the first \(d\) columns are exponential sequences
with characteristic roots \(a^{m_t}\). Their determinant is a generalized
Vandermonde factor times the recurrence residual of the carry column.

For fixed \(d\), every specified determinant is polynomial-time computable.
This is an exact hierarchy of possible screens. It does not supply a useful
weight selector or a nonnegligible mismatch probability.

## 8. Next decisive tests

1. Freeze the seed bound and weight sets before generating a balanced
   semiprime corpus.
2. Measure proper-gcd frequency and compare it with a matched random-scalar
   baseline.
3. Prove an inverse-polynomial asymmetric-vanishing law, or construct an
   infinite family with a public successful seed rule.
4. For a feedback claim, require the first successful determinant to depend
   essentially on a feedback-created block or trajectory.
5. Run the required hostile audit and statement-only blind reconstruction
   before any promotion.

## 9. Evidence boundary

The preserved verifier checks the displayed finite arithmetic, source
counts, exact-value gcd-free refinement, parity rank, local ranks, null
vector, local orders, short screens, and the cyclotomic synchronized control.

The named independent sweep checks the determinant congruence and gcd
equality on 3,571 small \((N,a)\) cases satisfying the unit condition. This
is self-audit evidence only.

The theorem proof and finite certificate remain **self-audited candidate**
until the project verification cadence is complete.
