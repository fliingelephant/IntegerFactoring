# F123 Question — Canonical-Carry Recurrence Determinant

## Status and origin

This is a retrospective registration of a result supplied by the user after
a GPT Pro brainstorm. It was not preregistered before discovery.

The current status is **self-audited candidate**. The supplied exact verifier
passes, and the root agent ran independent small-case identity checks. No
fresh hostile audit, proof-blind reconstruction, cross-family audit, human
audit, or publication-level literature audit has run.

## Closest prior routes

The closest prior routes are:

- F03 and F04, which use a publicly computable determinant or rank mismatch
  to expose one CRT component;
- Inspiration A2, which explicitly proposes a determinant, kernel, or
  eigenvalue collision followed by a gcd; and
- F26/F26-P, which generate canonical-inverse relations and study their
  carries, integer presentations, and square-class decoder.

The material difference is narrow but real. F123 gives a constant-size
determinant and a closed carry-recurrence residual for four consecutive
canonical-inverse power relations. It also gives one finite source on which
the named direct screens and complete exact-square decoder are null while
the new residual gives a factor.

## Exact question

For a public unit \(a\bmod N\), define

\[
c_j=[a^j]_N,\qquad
w_j=c_j^{-1}\bmod N,\qquad
\kappa_j=\frac{c_jw_j-1}{N},
\qquad 1\le j\le4.
\]

Does the determinant of

\[
L_N(a)=
\begin{pmatrix}
1&c_1&w_1&\kappa_1\\
1&c_2&w_2&\kappa_2\\
1&c_3&w_3&\kappa_3\\
1&c_4&w_4&\kappa_4
\end{pmatrix}
\]

reduce to a public carry-recurrence residual whose gcd with \(N\) can split
the hidden CRT components?

## Required boundaries

The record must distinguish:

1. an exact determinant identity;
2. one finite capability-separation certificate;
3. a fixed-degree polynomial-time screen;
4. an unproved all-input success or density law;
5. a static decoder-side test; and
6. adaptive feedback that changes the future source grammar.

The words “GCT” and “orbit closure” must not be used to imply an algebraic
complexity lower bound, a general factoring theorem, or publication-level
novelty.
