# F159 candidate — one quadratic-lift layer gives a factor or at most one doubling

## Status and scope

This is a proof-only source/decoder boundary. It strengthens the fixed-layer
part of F158. It is not a factoring algorithm because it does not produce a
new quadratic layer after the first doubling.

Let

\[
N=pq,
\qquad 3\le p<q,
\]

with distinct odd primes. Let \(H\le(\mathbf Z/N\mathbf Z)^\times\) be a
public subgroup, and let \(X\) be a public finite set of units such that

\[
x^2\in H
\qquad(x\in X).
\tag{1}
\]

## 1. Explicit one-layer saturation

Assume that \(H\) is supplied as a complete list. Process every \(x\in X\)
with the F158 priority scan

\[
\gcd(x-h,N),
\qquad h\in H.
\tag{2}
\]

Return a proper gcd first. Discard \(x\) if one comparison is \(N\). If a
first element \(x_0\) survives with all comparisons equal to one, form the
explicit subgroup

\[
K=\langle H,x_0\rangle=H\sqcup x_0H
\tag{3}
\]

and compare every remaining \(x\in X\) with every element of \(K\).

The exhaustive result is

\[
\boxed{
\text{proper factor}
\quad\lor\quad
\langle H,X\rangle=H
\quad\lor\quad
[\langle H,X\rangle:H]=2.
}
\tag{4}
\]

In the last branch, both hidden images also double:

\[
[\langle H_p,X_p\rangle:H_p]
=
[\langle H_q,X_q\rangle:H_q]
=2.
\tag{5}
\]

Thus one fixed quadratic-root layer can give at most one no-factor subgroup
doubling. Any second apparent external coset either agrees with the first
one globally or exposes a hidden-component mismatch by a proper gcd.

The scan uses at most \(2|H||X|\) gcds and remains quasipolynomial when the
two explicit lists have quasipolynomial size.

## 2. Compact cyclic alignment test

Assume instead that \((g,M)\) is an F158 certified common-order generator:

\[
\operatorname{ord}_p(g)=\operatorname{ord}_q(g)=M,
\tag{6}
\]

with the factorization of \(M\) supplied. Suppose

\[
x_i^2=g^{a_i},
\qquad
\gcd(a_i,M)=1
\tag{7}
\]

for a public list \(x_1,\ldots,x_s\).

First use the F158 internal-root comparisons

\[
2k\equiv a_i\pmod M,
\qquad
\gcd(x_i-g^k,N).
\tag{8}
\]

If no factor occurs and every \(x_i\) is internal, the layer is inert.
Otherwise choose a first external \(x_0\). For every other external \(x_i\),
solve

\[
2k\equiv a_i-a_0\pmod M
\tag{9}
\]

and test, for its at most two solutions,

\[
\gcd(x_i-x_0g^k,N).
\tag{10}
\]

Equation (9) is always soluble: if \(M\) is even, both \(a_i\) and \(a_0\)
are odd; if \(M\) is odd, two is invertible.

If no proper gcd occurs, every external \(x_i\) lies in the same public
cyclic group

\[
\langle g,x_0\rangle=\langle x_0\rangle,
\qquad
\operatorname{ord}_p(x_0)=\operatorname{ord}_q(x_0)=2M.
\tag{11}
\]

Therefore the complete fixed layer again gives at most one common-order
doubling. The compact alignment test uses \(O(s)\) gcds and modular
exponentiations.

## 3. Relation to section feedback

In F154/F156, every inverse section representative \(s_v\) satisfies

\[
s_v^2\in H.
\tag{12}
\]

When \(H\) is explicit, or has the certified cyclic presentation required
above, the whole frozen section layer has only three possible effects:

\[
\boxed{
\text{factor by alignment mismatch}
\quad\lor\quad
\text{no subgroup change}
\quad\lor\quad
\text{one common doubling}.
}
\tag{13}
\]

Consequently, quasipolynomially many roots in one frozen layer cannot be
multiplied into quasipolynomially many independent capacity gains. A route
to the F158 capacity cutoff must recursively create roots over the newly
doubled subgroup. Alternatively, it must force two same-layer lifts to have
incompatible hidden alignments, which (10) detects directly.

F159 proves no law that either event must occur. It narrows the missing
source theorem from “many roots” to “adaptive new layers or forced alignment
disagreement.”
