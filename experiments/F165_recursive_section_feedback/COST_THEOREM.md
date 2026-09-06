# F165 fixed-depth recursive-section cost theorem

**Status:** proof-only candidate. This statement has not received a hostile
audit or an independent reconstruction.

## Statement

Let `n` be the input bit length and put

\[
L=\lceil\log_2(n+1)\rceil.
\]

Suppose an explicit base relation source has at most

\[
R_0\le 2^{C L^a}
\]

records, with quasipolynomial total bit length. At recursive layer `h`, run a
complete factor-free decoder on the retained union. Choose a parity basis of
rank `r_h<=R_h`. Enumerate every nonempty basis subset of support at most

\[
D\le L^b.
\]

Retain at most one canonical exact record for each attempted subset. Let
`R_(h+1)` be the new union size.

For every fixed integer `H>=0`, all records through layer `H` can be
generated, retained, factor-free refined, and completely decoded in

\[
2^{L^{O_H(1)}}
\]

bit operations and space. In particular, every fixed number of recursive
decorated-section layers remains quasipolynomial.

The same hypotheses do not give a uniform quasipolynomial bound when `H`
grows with `n`. This is a limit of the counting proof. It is not a lower
bound for the canonical-inverse source.

## Proof

One layer attempts at most

\[
S_h=\sum_{j=1}^{D}\binom{r_h}{j}
\le (D+1)\max(1,R_h)^D
\]

subsets. Exact-value deletion can only reduce the retained count. Thus

\[
R_{h+1}\le R_h+S_h
\le 2(D+1)\max(2,R_h)^D.
\]

Put

\[
x_h=\log_2\max(2,R_h).
\]

Then

\[
x_{h+1}\le D x_h+O(\log(D+1)).
\]

Because `D<=L^b`, induction gives

\[
x_H=O_H(L^{a+bH}+L^{bH}).
\]

For fixed `H`, this is `L^(O_H(1))`. Hence

\[
R_H\le 2^{L^{O_H(1)}}.
\]

Each canonical inverse endpoint has `O(n)` bits. Each exact product has
`O(n)` bits. A support word at depth `H` uses at most `D^H`, and therefore
`L^(bH)`, base-basis occurrences. For fixed `H`, its provenance is also
polylogarithmic.

Gcd-free refinement, perfect-power extraction, binary elimination, decorated
lift arithmetic, kernel decoding, canonical inversion, and gcd tests are
polynomial in the explicit transcript bit length. A polynomial in
`2^(L^(O_H(1)))` has the same form. Summing over the fixed `H` layers does
not change the bound.

## Why growing depth is not covered

Even for support cap `D=2`, the recurrence permits

\[
x_H=O(2^H x_0).
\]

If `H` grows as `ceil(log2 n)`, this upper bound becomes
`2^(O(n*polylog(n)))`, which is not quasipolynomial in `n`.

More strongly, the size assumptions alone permit an abstract rank sequence
with `r_h=R_h` and

\[
R_{h+1}=R_h+\binom{R_h}{2}.
\]

It has `log R_H=Theta(2^H)`. This shows that no uniform QP conclusion follows
from only `r_h<=R_h` and support-two enumeration.

This abstract sequence is not claimed to be realizable by canonical-inverse
feedback. A separate rank, duplicate, or stabilization theorem could keep a
growing-depth canonical source quasipolynomial. F165-D01 does not prove such
a theorem.
