# F155 candidate — an infinite trial-hard family with strict section-feedback subgroup expansion

## Status and scope

This is a proof-only candidate. It gives an unconditional infinite family of
balanced distinct-prime semiprimes on which one public square relation,
section completion, and factor-free integer refinement strictly enlarge the
named-block-generated subgroup.

It is not an all-input refinement theorem. The enlarged subgroup is not
proved to contain a quasipolynomially accessible factor separator.

## Closest prior results and the material difference

P76 gives the finite \(N=209\) witness: canonical feedback endpoints already
lie in the old block subgroup, but their integer overlap exposes new blocks
and enlarges the next search space. P128 and P129 give quasipolynomial
unreduced square-relation sources and their bridge gate. P138 gives the
split-or-section law. F154 proves that completing a failed section is
decoder-inert but can still refine named integer blocks.

F155 upgrades the representation-level phenomenon from a finite witness to
an explicit infinite balanced trial-hard semiprime family. The source is a
one-row public square relation, and every formula is uniform in the bare
input \(N\).

## 1. The public construction

Let

\[
M=23{,}400.
\tag{1}
\]

Suppose

\[
N>13,
\qquad
N\equiv77\pmod M.
\tag{2}
\]

Define

\[
z=\frac{N-3}{2},
\qquad
s=\frac{N-2}{3},
\qquad
a=\frac{3N+9}{4}.
\tag{3}
\]

Then \(z,s,a\) are positive integers below \(N\), all are units modulo
\(N\), and

\[
z^2\equiv a\pmod N,
\qquad
zs\equiv1\pmod N.
\tag{4}
\]

Thus \(a\) is a public exact nonsquare atom with supplied modular square root
\(z\), and \(s=\iota_N(z)\) is the least positive inverse used by the F154
section completion.

The two ordinary endpoint screens are strictly null:

\[
\boxed{
\gcd(z-s,N)=\gcd(z+s,N)=1.
}
\tag{5}
\]

Equivalently,

\[
\gcd(a-1,N)=\gcd(a+1,N)=1.
\tag{6}
\]

## 2. Forced integer refinement

Writing \(N=77+Mt\) gives

\[
s=25+7800t,
\qquad
a=60+17550t.
\tag{7}
\]

The exact identity

\[
4a-9s=15
\tag{8}
\]

and the displayed residue classes imply

\[
\boxed{\gcd(a,s)=5.}
\tag{9}
\]

Also \(v_5(a)=1\). Hence \(a\) is not a perfect power, and complete
factor-free refinement of the old atom \(a\) against the new inverse
representative \(s\) strictly replaces it by the coprime named blocks

\[
\boxed{5,\quad a/5.}
\tag{10}
\]

The new representative can be used ephemerally: after splitting \(a\), the
algorithm can discard \(s\). The progress is a refinement of the fixed old
atom, not unbounded accumulation of probe cofactors.

## 3. Infinite balanced trial-hard semiprimes

There are infinitely many choices

\[
N=PR
\tag{11}
\]

with distinct primes \(P,R\) such that

\[
P\equiv7\pmod M,
\qquad
R\equiv11\pmod M,
\qquad
\frac12<\frac PR<2.
\tag{12}
\]

For all sufficiently large members, if
\(n=\lceil\log_2(N+1)\rceil\), then

\[
P,R>n^2.
\tag{13}
\]

Thus the family is balanced and trial-hard under the project convention.
Equation (12) gives \(N\equiv77\pmod M\), so the public construction and
forced refinement apply to every member.

## 4. The endpoint residues add no subgroup element

For every hidden prime \(L\in\{P,R\}\),

\[
z\equiv-\frac32\pmod L.
\tag{14}
\]

The classes \(P\equiv7\pmod{24}\) and \(R\equiv11\pmod{24}\) give

\[
\left(\frac{-6}{P}\right)
=
\left(\frac{-6}{R}\right)
=1.
\tag{15}
\]

Therefore \(z\) is a quadratic residue modulo both hidden primes. Both
primes are \(3\pmod4\), so their square subgroups have odd order. It follows
that \(z\) has odd local order and

\[
\langle z^2\rangle=\langle z\rangle
\tag{16}
\]

in each component. Since \(a\equiv z^2\), the old named subgroup

\[
H=\langle a\rangle
\le(\mathbf Z/N\mathbf Z)^\times
\tag{17}
\]

already contains both \(z\) and \(s=z^{-1}\).

Thus section completion adds no residue outside \(H\).

## 5. Refinement strictly enlarges the named subgroup

Quadratic reciprocity gives

\[
\left(\frac5P\right)
=
\left(\frac P5\right)
=
\left(\frac25\right)
=-1.
\tag{18}
\]

Every element of \(H=\langle z^2\rangle\) is a quadratic residue modulo
\(P\), while \(5\) is not. Therefore

\[
5\notin H.
\tag{19}
\]

After (10), the new named-block subgroup contains both \(a\) and \(5\).
Consequently,

\[
\boxed{
H
\;<\;
\langle5,a/5\rangle.
}
\tag{20}
\]

The strict growth comes only from the new integer factorization of a product
whose selected endpoint residues were already in \(H\).

## 6. Exact conclusion

The family proves all of the following at once:

1. the source is uniform and public from bare \(N\);
2. the immediate factor screens are null;
3. the feedback endpoint residues lie in the old named subgroup;
4. integer refinement is forced;
5. the refined named subgroup is strictly larger;
6. the factors of \(N\) remain unknown and trial division is ineffective.

This is an infinite-family validation of the feedback mechanism. It does not
prove that the expanded subgroup contains a separator of bounded order,
that a quasipolynomial selector finds one, or that every input admits such a
refinement.
