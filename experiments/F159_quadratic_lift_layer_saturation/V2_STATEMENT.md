# F159 V2 candidate — root-layer saturation leaves integer refinement open

## Status and scope

This is a corrected proof-only source/decoder boundary. It proves that the
modular residues in one fixed quadratic-root layer add at most one coset on
a no-factor branch. It also proves that this bound does **not** control the
integer blocks that become named when canonical representatives refine old
blocks.

The distinction is essential for F154/F156:

\[
\text{root-generated residue subgroup}
\quad\ne\quad
\text{refinement-generated named subgroup}.
\]

The finite certificate below shows that an inert root residue can cause an
index-15 named-subgroup expansion and then expose a factor with a public
exponent. This is finite capability, not an all-input success law.

Let

\[
N=pq,
\qquad 3\le p<q,
\]

where \(p,q\) are distinct odd primes.

## 1. Exact saturation of an explicit root layer

Let \(H\le(\mathbf Z/N\mathbf Z)^\times\) be a public subgroup supplied as
a complete list. Let \(X\) be a public finite set of units with

\[
x^2\in H
\qquad(x\in X).
\tag{1}
\]

Process \(X\) in a fixed order. Before the first external element, compare
each \(x\) with every \(h\in H\) by

\[
\gcd(x-h,N).
\tag{2}
\]

The scan has the following priority:

1. return a proper gcd if any comparison gives one;
2. declare \(x\) internal if a comparison is \(N\);
3. declare \(x\) external only if every comparison is one.

If a first external element \(x_0\) occurs, form

\[
K=\langle H,x_0\rangle=H\sqcup x_0H
\tag{3}
\]

as a complete list. Compare every later \(x\) with all elements of \(K\),
with the same priority rule.

The exact result for the root residues is

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

In the last branch, both hidden images double:

\[
[\langle H_p,X_p\rangle:H_p]
=
[\langle H_q,X_q\rangle:H_q]
=2.
\tag{5}
\]

The scan uses at most \(2|H||X|\) gcds. Thus it is quasipolynomial when
the two explicit lists have quasipolynomial size.

Equation (4) concerns only \(\langle H,X\rangle\). It does not concern new
integer factors of old named representatives.

## 2. Compact cyclic alignment

Assume that \((g,M)\) is a certified common-order generator:

\[
\operatorname{ord}_p(g)=\operatorname{ord}_q(g)=M,
\tag{6}
\]

with the factorization of \(M\) supplied. Suppose the public roots satisfy

\[
x_i^2=g^{a_i},
\qquad
\gcd(a_i,M)=1
\qquad(1\le i\le s).
\tag{7}
\]

First solve

\[
2k\equiv a_i\pmod M
\tag{8}
\]

and test \(\gcd(x_i-g^k,N)\) for all zero, one, or two solutions. On the
no-factor branch this classifies \(x_i\) as internal in both hidden fields
or external in both.

If every root is internal, the root layer is inert. Otherwise choose a
first external root \(x_0\). For every later external \(x_i\), solve

\[
2k\equiv a_i-a_0\pmod M
\tag{9}
\]

and test

\[
\gcd(x_i-x_0g^k,N)
\tag{10}
\]

for every solution. Equation (9) is always soluble and has at most two
solutions.

If no proper gcd occurs, all external roots lie in the single cyclic group

\[
\langle g,x_0\rangle=\langle x_0\rangle,
\qquad
\operatorname{ord}_p(x_0)=
\operatorname{ord}_q(x_0)=2M.
\tag{11}
\]

This compact test uses \(O(s)\) gcds and modular exponentiations. It gives
the same root-residue saturation as (4), under all hypotheses in (6)--(7).

There is a stronger qualification when \(M\) is odd. The unique internal
root of \(g^{a_i}\) is a public power \(g^{k_i}\). On a no-factor branch,
every external root is its global negative \(-g^{k_i}\). Thus the only
possible extension is the already public group \(\langle g,-1\rangle\).
An odd-order root layer can still have useful **integer encodings**, but it
contains no new modular root information.

## 3. Integer refinement is a separate channel

Suppose an old named integer block \(b\) represents an element of \(H\),
and a canonical root representative \(x\) gives

\[
d=\gcd(b,x),
\qquad
1<d<b.
\tag{12}
\]

Factor-free refinement replaces \(b\) by integer blocks \(d\) and \(b/d\).
Although their product is the old element \(b\in H\), neither factor must
belong to \(\langle H,X\rangle\). Therefore (4) gives no upper bound on

\[
\langle H,d,b/d\rangle.
\tag{13}
\]

Its global index can exceed two. Its local indices can be unequal. A later
public exponent test on a new block can then factor \(N\).

There is an exact general post-refinement screen when the old state is the
certified common-order group \(H=\langle g\rangle\) from (6). For any
released unit block \(d\), compute

\[
D_d=\gcd(d^M-1,N).
\tag{14}
\]

Then

\[
\begin{array}{c|c}
D_d&\text{exact local meaning}\\ \hline
N&d_p\in H_p\text{ and }d_q\in H_q,\\
1<D_d<N&d_r\in H_r\text{ for exactly one }r\in\{p,q\},\\
1&d_p\notin H_p\text{ and }d_q\notin H_q.
\end{array}
\tag{15}
\]

Thus a proper value factors \(N\). A value of one proves that both local
generated subgroups strictly grow. A value of \(N\) proves only local
membership in both images; it does not prove that the two hidden exponents
align to make \(d\in H\) globally. The screen uses one modular
exponentiation and one gcd.

## 4. Exact \(N=341\) F154 certificate

Take

\[
N=341=11\cdot31,
\qquad
g=q_1=70.
\tag{16}
\]

The complete old subgroup is

\[
H=\langle70\rangle
=\{1,70,126,295,190\}.
\tag{17}
\]

The element \(70\) has order five modulo \(11\), modulo \(31\), and modulo
\(341\). Thus \((70,5)\) is a certified common-order state.

For the one-dimensional section, take

\[
Q(1)=70,
\qquad
t=467=126+341,
\qquad
z=295,
\qquad
s=\iota_{341}(z)=126.
\tag{18}
\]

A legal one-record base transcript is

\[
A=t^2Q(1)
=15{,}266{,}230
=1+44{,}769\cdot341.
\tag{19}
\]

It has one nonzero parity column and therefore no dependency. Also

\[
\gcd(t,Q(1))=\gcd(467,70)=1,
\qquad
t^{-1}\equiv z\pmod{341}.
\tag{20}
\]

Thus the old square part does not refine the old block. Its actual decorated
lift is \((1,z)\). Canonical section completion replaces the representative
\(t\) by its least positive residue \(s=126\).

Then

\[
z^2\equiv70,
\qquad
zs\equiv1,
\qquad
s^2\equiv70^4
\pmod{341},
\tag{21}
\]

and the exact completion value is

\[
s^2Q(1)
=1{,}111{,}320
=1+3{,}259\cdot341.
\tag{22}
\]

All current direct screens are null:

\[
\gcd(z-s,N)=
\gcd(z+s,N)=
\gcd(70-1,N)=
\gcd(70+1,N)=1.
\tag{23}
\]

The complete membership scans give, in the order in (17),

\[
\bigl(\gcd(s-h,N)\bigr)_{h\in H}
=(1,1,341,1,1).
\tag{24}
\]

For the other section endpoint,

\[
\bigl(\gcd(z-h,N)\bigr)_{h\in H}
=(1,1,1,341,1).
\tag{25}
\]

The two compact equations give \(s=70^2\) and \(z=70^3\). Thus

\[
\langle H,z,s\rangle=H.
\tag{26}
\]

The root layer is fully inert and contains no new modular information.
Nevertheless,

\[
\gcd(70,126)=14,
\qquad
70=14\cdot5.
\tag{27}
\]

The refined named subgroup

\[
H'=\langle14,5\rangle
\tag{28}
\]

has exact sizes and indices

\[
\begin{array}{c|ccc}
&\text{global}&\bmod 11&\bmod31\\ \hline
H&5&5&5\\
H'&75&5&15\\
[H':H]&15&1&3.
\end{array}
\tag{29}
\]

The new blocks have null scalar screens:

\[
\gcd(14\pm1,N)=
\gcd(5\pm1,N)=1.
\tag{30}
\]

But the old public order gives an immediate later test:

\[
14^5\equiv67\pmod{341},
\qquad
\boxed{\gcd(14^5-1,341)=11},
\qquad
\gcd(14^5+1,341)=1.
\tag{31}
\]

This is a real finite refinement capability. It comes from the canonical
integer encoding, not from new modular information: both \(z\) and \(s\)
were already public powers of \(g\). The certificate does not show that a
section source is necessary to find them.

## 5. Exact consequence for F154/F156

Every inverse section representative satisfies

\[
s_v^2\in H.
\tag{32}
\]

If \(H\) is explicitly enumerable, (4) bounds the subgroup generated by
all root residues in that frozen layer. If the compact presentation is used,
every tested root must separately satisfy all conditions in (7), including
the coprime exponent presentation.

Neither theorem bounds the subgroup generated after joint gcd-free
refinement. Therefore one fixed section layer has two distinct outcomes:

1. its root residues give a factor, no coset, or one common index-two coset;
2. its integer representatives can independently refine old named blocks
   and release generators outside that root-generated subgroup.

F159 V2 proves no density of useful refinements, no bound on repeated named
growth, no all-input source, and no quasipolynomial factoring algorithm.
The missing theorem can use adaptive new root layers, forced alignment
disagreement, **or refinement-created generators**.
