# Scope map from the F294 chart to the P235 support problem

This audit uses only F294 `RESULT.md`, F294 `FORMAL_DESCENT.md`, P235, and
F289 `AFFINE_PATCHES.md`. It records interfaces and index counts. It makes no
new cost or feasibility claim.

## Modulus and class layers

| Layer | Modulus or index | Number of classes | Object covered |
| --- | --- | ---: | --- |
| P235 target | \(M=2^k\), with the factoring reduction taking the largest \(M\leq N/8\) | one succinct union | All positive \((x,y)\) with \(xy\geq N\) and \(xy\equiv N\pmod M\) |
| P235 affine cover | \(s=2^h\), \(h=\max(1,\lfloor k/2\rfloor)\) | \(2^{h-1}\) odd bases \(u\bmod s\) | Exact affine inverse classes modulo \(M\) |
| F294 quadratic chart | \(m=2^r\), original inverse modulus \(m^3\) | \(m/2\) odd bases \(u_0\bmod m\) | One exact quadratic inverse chart for each base |
| F294 internal count | \(q=m^2\) | one count inside a fixed \(u_0\) chart | The two high-coordinate half-windows |
| F294 Fourier support | \(b_0\) odd modulo \(m\) | \(m/2\) frequencies inside a fixed chart | Fourier expansion of that one two-window count |

The symbol \(q=m^2\) in F294 is not the original inverse-graph modulus. The
faithful inverse identity starts with \(N\) and inverses modulo \(m^3\), then
factors out the fixed low base digit and leaves a residual calculation modulo
\(q=m^2\).

P235 also records higher polynomial covers through finite differences, but
its promoted factoring reduction accepts an arbitrary power-of-two modulus
\(M\) near \(N\). F294 states its faithful quadratic digit formula for the
aligned modulus \(M=m^3\).

## Exact windows in one F294 chart

Fix an odd base \(u_0\in[1,m)\), and put

\[
 v_0\equiv Nu_0^{-1}\pmod{m^3},\qquad
 \alpha\equiv-Nu_0^{-2}\pmod{m^2},\qquad
 \beta\equiv Nu_0^{-3}\pmod m,\qquad
 D=\lfloor v_0/m\rfloor.
\]

For \(x=u_0+mj\), F294 gives

\[
 y=(v_0\bmod m)+m\bigl((\alpha j+m\beta j^2+D)\bmod q\bigr).
\]

The faithful chart count uses the full coordinate half-windows

\[
 0\leq j<q/2,
 \qquad
 (\alpha j+m\beta j^2+D)\bmod q<q/2.
\]

Thus the low residues of both original coordinates are fixed by the chart,
while each high-coordinate variable ranges over half of its complete
\(q\)-cycle.

The universal-polynomial normalization \(j=u_0z\pmod q\), with
\(\gamma=Nu_0^{-1}\pmod q\), changes these to

\[
 u_0z\bmod q<q/2,
 \qquad
 D+\gamma(-z+mz^2)\bmod q<q/2,
 \qquad u_0\gamma\equiv N\pmod q.
\]

The formal-group coordinate gives the equivalent pair

\[
 u_0E(w)\bmod q<q/2,
 \qquad
 D+\gamma E(-w)\bmod q<q/2.
\]

These are two coupled wrapped half-windows. They are not two independent
translated intervals in the normalized variable. F294's abstract slope-block
formula permits a cyclic input interval and a translated output half while
the geometry is fixed. Its faithful origin shifts change the slope, constant,
and input interval together, so that fixed-geometry average is a different
parameter family.

## Which prototype covers which region

| Prototype or statement | Region actually covered |
| --- | --- |
| F294 `evaluator.py` and `FORMAL_DESCENT.py` | Complete cyclic half-windows in one quadratic chart, with both boundary indicators retained |
| P235's oracle statement and F289's exact-union pilot | The full unbounded positive feasible union \(S\), including \(xy\geq N\) and all congruence classes |
| The grouped cap-line prototype referenced by P235 as unpromoted | Only the short factor-isolating linear-objective cap, not full support and not a full chart half-window |

For the cap-line prototype, the public cap used in this route is

\[
 ax+by\leq U,
 \qquad U=\left\lfloor\sqrt{17abN/4}\right\rfloor,
 \qquad M>N/16.
\]

The P235 product-gap argument makes every target-congruent point under this
cap product-exact. P235 itself asks for a 1.01-relative support point over the
full set \(S\); it does not promote either the cap-line implementation or a
support oracle.

## Indices left after a complete fixed-chart frequency sum

Inside one fixed \(u_0\) chart, F294 parametrizes the surviving Fourier
frequencies by

\[
 b=b_0+mt,\quad b_0\text{ odd modulo }m,
 \qquad
 a=db+2mz,\quad z\bmod m/2.
\]

There are \(m/2\) choices of \(b_0\). The high-lift and \(z\)-contractions
remain internal to the same chart. Therefore, an evaluator that sums every
\(b_0\) returns one faithful two-half-window count for one fixed \(u_0\).

Two separate outer interfaces remain:

1. The original inverse graph modulo \(m^3\) has \(m/2\) odd classes
   \(u_0\bmod m\). Their chart results still have to be combined.
2. P235 needs support in the positive lifted set, or the short
   factor-isolating objective cap. Neither region is the pair of full cyclic
   half-windows evaluated by F294. The chart evaluator therefore still needs
   a window and lift interface for that geometry.

Accordingly, summing all \(b_0\) inside one F294 chart does not by itself
complete the P235 support problem. It leaves both the outer \(u_0\) classes
and the change from full chart half-windows to the support/cap region.
