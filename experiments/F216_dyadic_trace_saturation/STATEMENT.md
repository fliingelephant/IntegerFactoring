# F216 candidate — dyadic trace saturation erases almost all reciprocal-prefix bits

## Status and scope

This is a frozen, self-audited theorem candidate with a preregistered finite
verification. It is a named-model boundary for the orientation-free dyadic
trace projection. It is not a factoring algorithm and not a lower bound
against a decoder that retains the inverse parameter.

For an odd integer `N` and `t >= 5`, put

\[
W_t(N)=\{u+Nu^{-1}\pmod {2^t}:u\in U(2^t)\}.
\]

For a semiprime `N=pq`, the factor trace `p+q mod 2^t` is in `W_t(N)` by
taking `u=p`.

## Theorem 1: reduction to four square classes

Let `d` be the element of `{1,3,5,7}` congruent to `N modulo 8`. There is a
publicly computable odd `a modulo 2^t` such that

\[
N\equiv da^2\pmod {2^t}.
\]

Multiplication by `a` gives the exact image identity

\[
\boxed{W_t(N)=aW_t(d).}
\]

Thus the cardinality depends only on `N modulo 8`.

## Theorem 2: exact images and cardinalities

For every `t >= 5`,

\[
\boxed{W_t(3)=\{s\pmod {2^t}:s\equiv4\pmod8\}},
\]

\[
\boxed{W_t(7)=\{s\pmod {2^t}:s\equiv0\pmod8\}},
\]

and

\[
\boxed{W_t(5)=\{s\pmod {2^t}:s\equiv6\text{ or }26\pmod {32}\}}.
\]

Consequently,

\[
|W_t(3)|=|W_t(7)|=2^{t-3},
\qquad
|W_t(5)|=2^{t-4}.
\]

For the square class `d=1`, define

\[
c_b=\begin{cases}5,&b=2,\\1,&b\ge3.\end{cases}
\]

Then `W_t(1)` is the disjoint union of the negative of the following set
and the set itself:

\[
W_t^+(1)=\{2\}\cup
\bigcup_{b=2}^{\lfloor(t-1)/2\rfloor}
\left\{
2+2^{2b}w\pmod {2^t}:
w\in U(2^{t-2b}),\quad
w\equiv c_b\pmod {2^{\min(3,t-2b)}}
\right\}.
\]

Its exact size is

\[
\boxed{
|W_t(1)|=
\begin{cases}
(2^{t-4}+8)/3,&t\text{ even},\\
(2^{t-4}+10)/3,&t\text{ odd}.
\end{cases}}
\]

In particular,

\[
|W_t(1)|=2^t/48+O(1).
\]

## Corollary: the trace list never becomes QP-small

Uniformly for every odd `N` and `t >= 5`,

\[
\boxed{|W_t(N)|\ge 2^t/48.}
\]

At the partial-factor threshold `t = n/4 - polylog(n)`, a literal trace
residue list therefore still has `2^{Omega(n)}` entries. A high power of two
does not contribute one independent trace bit per lift:

- in square classes `3` and `7`, all higher conditions reduce to one fixed
  congruence modulo `8`;
- in square class `5`, they reduce after public scaling to two fixed
  congruences modulo `32`;
- in square class `1`, they form only `O(t)` valuation strata but retain
  asymptotic density `1/48`.

This closes only a specific proposed bridge: replacing many odd-prime trace
conditions by one large dyadic trace condition and then materializing its
residue list. It does not close an implicit interval finder, a method that
retains `u`, a nonlinear integer statistic, mixed odd moduli, or a direct
reciprocal-prefix selector.

