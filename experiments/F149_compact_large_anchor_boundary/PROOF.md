# F149 proof — compact large-anchor canonicalization and singleton counting

## 1. Canonicalization

By definition, \(a\equiv\alpha\pmod N\).  Therefore

\[
[qa^2]_N=[q\alpha^2]_N=c,
\]

so the canonical inverse \(w\), every integer divisor of the canonical
endpoint \(c\), and every containment residual are unchanged.

The lifted value is

\[
L_a=qa^2w.
\]

The factor \(a^2\) is an exact rational square, so

\[
[L_a]=[qw]
\]

in the positive rational square-class group.  For the canonical-residue
clone \(L_\alpha=q\alpha^2w\),

\[
L_aL_\alpha
=q^2a^2\alpha^2w^2
=(qa\alpha w)^2.
\]

Modulo \(N\),

\[
qa\alpha w
\equiv
q\alpha^2c^{-1}
\equiv1.
\]

Thus the connecting square relation has normalized root \(+1\).  This proves
Section 2 of the statement.

## 2. The singleton criterion and root

The product of the canonical and lifted P128 values is

\[
CL_a
=(cw)(qa^2w)
=a^2w^2(qc).
\]

The positive rational factor \(a^2w^2\) is a square.  Hence \(CL_a\) is an
integer square if and only if \(qc\) is an integer square.  Write

\[
qc=s^2.
\]

Then the positive exact root is

\[
R=aws.
\]

Since \(a\equiv\alpha\) and \(c\equiv q\alpha^2\pmod N\),

\[
R
\equiv
\alpha s c^{-1}
\equiv
s(q\alpha)^{-1}
\pmod N.
\]

Multiplying \(R\pm1\) by the unit \(q\alpha\) gives

\[
q\alpha(R\pm1)\equiv s\pm q\alpha\pmod N.
\]

This proves the gcd identities and the ordinary congruence-of-squares
classification.

## 3. Positive self-containment

Put \(z=[\alpha^2]_N\).  Since \(1\le q,z<N\), there is a unique integer

\[
h=\left\lfloor{qz\over N}\right\rfloor
\quad\text{with}\quad
0\le h<q
\]

such that

\[
c=qz-hN.
\]

If \(q\mid c\), then \(q\mid hN\).  The unit condition
\(\gcd(q,N)=1\) gives \(q\mid h\).  Because \(0\le h<q\), this forces
\(h=0\).  Hence \(qz<N\) and \(c=qz\).  The converse is immediate.

In this case

\[
qc=q^2z.
\]

It is a square exactly when \(z=S^2\).  The singleton root formula becomes

\[
s(q\alpha)^{-1}
=qS(q\alpha)^{-1}
=S\alpha^{-1}
\pmod N.
\]

Finally, \(z=S^2=[\alpha^2]_N\) gives

\[
\alpha^2-S^2=h'N
\]

for an integer \(h'\ge0\).  A useful root excludes \(h'=0\), because then
\(0<\alpha,S<N\) would give \(\alpha=S\) and the global root \(+1\).
This proves Section 4.

## 4. Counting useful singleton anchor residues

Let \(N=p\ell\) for distinct odd primes, and write \(q=du^2\), with \(d\)
squarefree.  The condition \(qc=s^2\) is equivalent to \(c\) having the
same positive rational square class as \(q\).  Since \(1\le c<N\), every
such unit \(c\) has the unique form

\[
c=dv^2,
\qquad
dv^2<N,
\qquad
\gcd(v,N)=1.
\]

For one such \(v\), the canonical-endpoint condition is

\[
[q\alpha^2]_N=dv^2.
\]

Both sides are canonical positive representatives, so this is equivalent
to the modular equation

\[
du^2\alpha^2\equiv dv^2\pmod N,
\]

or

\[
(u\alpha)^2\equiv v^2\pmod N.
\tag{1}
\]

Because \(N\) is a product of two distinct odd primes and \(v\) is a unit,
(1) has exactly four solutions for \(u\alpha\): the two independent sign
choices modulo \(p\) and \(\ell\).  Two choices are the global values
\(u\alpha\equiv\pm v\pmod N\).  The other two have mixed signs.

The normalized root is

\[
{s\over q\alpha}
=
{duv\over du^2\alpha}
=
{v\over u\alpha}
\pmod N.
\]

It is global for the first two solutions and non-global for the mixed two.
Different positive \(v\)'s give different canonical integers \(c=dv^2\),
so their anchor-residue solutions are disjoint.  There are therefore exactly
\(2V_d\) useful residues.

The elementary estimates

\[
V_d<\sqrt{N/d}
\]

and

\[
\varphi(p\ell)=(p-1)(\ell-1)>N/2
\]

give

\[
{2V_d\over\varphi(N)}
<
{4\over\sqrt{dN}}.
\]

For self-containment, \(c=qS^2\), so the same four-sign argument gives two
useful anchors for each admissible unit \(S\).  Since

\[
W_q<\sqrt{N/q},
\]

its probability is less than \(4/\sqrt{qN}\).

For \(M=2^{\operatorname{polylog}n}\) trials whose individual marginals are
uniform units, the union bound gives

\[
\Pr[\text{a useful singleton}]
\le
{4M\over\sqrt N}
=2^{-n/2+o(n)}.
\]

No independence assumption is used.

## 5. Presentation collisions and cycle classification

If \(\alpha^2\equiv\beta^2\pmod N\), then

\[
\theta=\alpha\beta^{-1}
\]

satisfies \(\theta^2\equiv1\pmod N\).  For odd \(N\), a non-global such
root gives a proper divisor through \(\gcd(\theta\pm1,N)\).  Otherwise the
two anchors differ only by one global sign.  Thus a useful repeated squared
residue is precisely a P71 half-relation.

For a containment cycle collection, replacing every raw anchor \(a_e\) by
its residue \(\alpha_e\) leaves every endpoint and residual unchanged.  If
the residual product is \(S^2\), the usual endpoint cancellation gives

\[
\left(\prod_e\alpha_e\right)^2\equiv S^2\pmod N.
\]

The normalized root is

\[
\rho=\left(\prod_e\alpha_e\right)S^{-1}.
\]

If \(S\) has a declared word presentation, this equality says twice the
difference of the two public exponent vectors lies in the hidden relation
lattice, exactly P71.  Without such a presentation, it is an integer
square-class closure of the P128/P129 type.  Raw anchor size does not affect
either case.

## 6. Certificate checks

For \(N=77,q=2,a=25\),

\[
25^2=625=8\cdot77+9,
\]

so \(z=9\), \(qz=18<77\), and the residual is \(3^2\).  Also

\[
2\cdot25^2=1250=16\cdot77+18.
\]

Since \(18\cdot30=540=7\cdot77+1\), \(w=30\).  Euclid gives

\[
\gcd(12,77)=\gcd(48,77)=1.
\]

The exact product is

\[
(18\cdot30)(2\cdot25^2\cdot30)
=540\cdot37500
=20250000
=4500^2.
\]

Reduction gives \(4500=58\cdot77+34\), and

\[
33=3\cdot11,
\qquad
35=5\cdot7.
\]

Therefore the two root gcds are \(11\) and \(7\).  Since

\[
2\cdot3^2=18
\quad\text{and}\quad
2\cdot5^4=1250\equiv18\pmod{77},
\]

the same witness is also exactly the P128 same-residue parity-collision
lemma.  This completes all claims.
