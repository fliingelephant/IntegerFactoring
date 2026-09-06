# F160 candidate — sign normalization turns a section square-class hit into an exact order doubling

## Status and scope

This is a proof-only source/decoder theorem. It does not prove that the
required square-class hit occurs on every input.

The closest results are P140, P144, and F159. P144 tests a supplied
quadratic lift and retains an inert-root branch. F159 proves that one fixed
quadratic layer gives at most one no-factor doubling. P140 proves that a
Jacobi-minus-one discriminant carries a real hidden orientation, but that
the tested torus operations preserve one section.

The material differences here are exact.

1. For a primitive power of a certified common-order generator, the
   inert-root branch can always be removed by a public sign choice.
2. A P138 decorated section gives the next common-order state whenever its
   span contains the current generator's square class with public
   provenance.
3. The natural pair of Jacobi-minus-one discriminants is exactly equivalent
   to the missing scalar square root. It does not make that root easier by
   itself.

Let

\[
N=pq,
\qquad 3\le p<q,
\]

where \(p,q\) are distinct odd primes. Let \((g,M)\) be a P144 certified
common-order generator. Thus the factorization of \(M\) is public and

\[
\operatorname{ord}_p(g)=\operatorname{ord}_q(g)=M.
\tag{1}
\]

## 1. Sign-normalized primitive-root theorem

Suppose public \(x,a\) satisfy

\[
x^2\equiv g^a\pmod N,
\qquad
\gcd(a,M)=1.
\tag{2}
\]

There is a deterministic polynomial-time procedure with the exact outcome

\[
\boxed{
\text{proper factor of }N
\quad\lor\quad
\text{a certified common-order generator }(y,2M).
}
\tag{3}
\]

More precisely:

- If \(M\) is even, put \(y=x\). Then

  \[
  \operatorname{ord}_p(y)=\operatorname{ord}_q(y)=2M.
  \tag{4}
  \]

- If \(M\) is odd, solve the unique congruence

  \[
  2k\equiv a\pmod M
  \tag{5}
  \]

  and compute

  \[
  d=\gcd(x-g^k,N).
  \tag{6}
  \]

  If \(d\) is proper, return it. If \(d=N\), put \(y=-x\). If \(d=1\),
  put \(y=x\). In both no-factor cases, (4) holds.

Thus a source does **not** have to prove that its primitive quadratic lift
is external. It only has to produce any scalar root in (2). Sign
normalization removes the inert case.

There is also one source-free consequence. If \(M\) is odd, then

\[
x_0=g^{a(2^{-1}\bmod M)}
\]

is a public internal root of \(g^a\), and \(-x_0\) has common order \(2M\).
Hence every odd common-order state has one unconditional public doubling.
After this step the order is even. All later missing-source calls occur at
even order.

## 2. Decorated-section hit criterion

Assume the no-factor branch of P138. Let \(W\) be its observed parity span,
let

\[
Q(v)=\prod_jq_j^{v_j},
\]

and let the public decorated section supply

\[
z_v^2\equiv Q(v)\pmod N
\qquad(v\in W).
\tag{7}
\]

Suppose a public unit \(u\), vector \(v\), and integer \(a\) satisfy

\[
v\in W,
\qquad
u^2Q(v)\equiv g^a\pmod N,
\qquad
\gcd(a,M)=1.
\tag{8}
\]

Then

\[
x=uz_v
\tag{9}
\]

satisfies (2). The sign-normalized procedure therefore returns a proper
factor or the next certified state \((y,2M)\).

All conditions in (8) are public and exactly verifiable. If a source emits
a quasipolynomial list of candidate triples \((v,u,a)\), the complete
verification and decoding remain quasipolynomial. No explicit enumeration
of \(\langle g\rangle\) is required.

The F154 inverse representatives are the special case

\[
s_v^2\equiv Q(v)^{-1}\pmod N.
\]

Thus a public provenance equality

\[
Q(v)^{-1}\equiv g^a\pmod N,
\qquad
\gcd(a,M)=1,
\tag{10}
\]

is already a complete factor-or-double certificate. P138, P143, and F159
do not prove that such a hit exists uniformly.

## 3. Exact Jacobi boundary at an even state

Assume \(M\) is even and write

\[
c_r=\frac{r-1}{M}
\qquad(r=p,q).
\tag{11}
\]

For every \(a\) coprime to \(M\),

\[
\boxed{
\left(\frac{g^a}{r}\right)=(-1)^{c_r}.
}
\tag{12}
\]

Consequently:

1. If \(\left(\frac gN\right)=-1\), exactly one hidden prime admits a
   square root of \(g^a\). No scalar \(x\) satisfying (2) exists modulo
   \(N\). A total factor-or-root source must return a factor on this branch.
2. If \(\left(\frac gN\right)=+1\), the two local capacities agree. Either
   both \(c_p,c_q\) are even and roots exist in both fields, or both are odd
   and roots exist in neither field. The Jacobi bit alone does not
   distinguish these cases.

The universal state \((-1,2)\) already shows both possibilities with the
same Jacobi value. For

\[
N=13\cdot17=221,
\]

\(\left(\frac{-1}{N}\right)=+1\) and
\(174^2\equiv-1\pmod{221}\). For

\[
N=7\cdot11=77,
\]

\(\left(\frac{-1}{N}\right)=+1\), but \(-1\) has no square root in either
hidden field.

Finally, let \(D\) be any unit with
\(\left(\frac DN\right)=-1\). When
\(\left(\frac gN\right)=+1\), put

\[
E\equiv Dg^a\pmod N.
\tag{13}
\]

Then \(\left(\frac EN\right)=-1\), so \(D,E\) form the natural P140 pair.
But

\[
DE\equiv D^2g^a\pmod N.
\tag{14}
\]

The maps

\[
x\longmapsto z=Dx,
\qquad
z\longmapsto x=D^{-1}z
\tag{15}
\]

are mutually inverse public reductions between

\[
x^2\equiv g^a\pmod N
\quad\text{and}\quad
z^2\equiv DE\pmod N.
\tag{16}
\]

Therefore pairing two Jacobi-minus-one discriminants only re-encodes the
same missing root. A P138 section root for \(DE\) would solve the lift gate
through (15), but the Jacobi orientations alone do not supply that section
root.

## 4. Remaining theorem

The live source problem is now narrower than the P144 formulation:

> At every surviving **even** certified common-order state, produce a
> factor or one public P138/F156 square-class hit of the form (8), in
> deterministic or Las Vegas expected quasipolynomial time.

No externality condition is needed. The result above proves no all-input
hit law, no inverse-quasipolynomial hit density, and no factoring algorithm.
