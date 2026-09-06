# F215 blind reconstruction

## Verdict

**STRICT PASS within the declared scope.** Starting only from PROMPT.md and
STATEMENT.md, I reconstructed every theorem in the frozen statement. I
found no false congruence, Frobenius-orientation error, local-power gap,
fixed-witness error, coefficient-content collision, norm overclaim, or
Fourier-separation gap.

F215 is an information boundary for its explicitly defined scalar abelian
transcripts and a conditional extraction result from much stronger
ring-valued data. It is not the all-input factoring algorithm required by
PROMPT.md, and it does not claim to be.

## Blind source boundary and integrity

Before reading the F215 statement, I computed its SHA-256:

ef9c59a2cda7eb7a1341d7242aa432dd50a67ba5a85fe797b0343ade470c743e.

It matches the supplied expected value exactly. I then read only the
workspace PROMPT.md and
experiments/F215_higher_reciprocity_inversion_boundary/STATEMENT.md. I did
not inspect any other F215 file, proof, audit, manifest, provenance file,
ledger, or prior proof discussion.

## 1. Elementary inversion torsor

The setup gives

\[
N=2K+1.
\]

Therefore

\[
\gcd(N,K)=1.
\tag{R1}
\]

Every divisor \(d\mid K\) is consequently coprime to \(p\) and \(q\), so
both factors are units modulo \(d\). Reducing \(pq=N\) modulo \(d\) gives

\[
pq\equiv1\pmod d,
\]

and hence

\[
q\equiv p^{-1}\pmod d.
\tag{R2}
\]

Both factors are strictly below \(K\). The larger-factor inequality is
equivalent to

\[
q<\frac{pq-1}{2}
\iff q(p-2)>1.
\]

The odd prime \(p\) is at least three and \(q>p\), so the last inequality
holds. Thus

\[
0<p<q<K.
\tag{R3}
\]

At \(d=K\), the canonical representatives of the inversion orbit
\[
\{p\bmod K,p^{-1}\bmod K\}
\]
are therefore the actual integers \(p,q\). Reading those representatives
recovers the unordered factor pair, and their product verifies the result.

## 2. Cyclotomic Frobenius inversion

A rational prime ramifies in \(\mathbb Q(\zeta_d)\) only if it divides
\(d\). Equation (R1) shows that neither \(p\) nor \(q\) does, so both are
unramified.

For a rational prime \(r\nmid d\), cyclotomic Frobenius acts by

\[
\zeta_d\longmapsto\zeta_d^r.
\]

Equation (R2) therefore gives

\[
\operatorname{Frob}_q
=\operatorname{Frob}_p^{-1}.
\tag{R4}
\]

The cyclotomic Galois group is abelian, so no conjugacy-class ambiguity
remains. An element and its inverse generate the same subgroup:

\[
\langle\operatorname{Frob}_p\rangle
=\langle\operatorname{Frob}_q\rangle.
\tag{R5}
\]

The residue degree at an unramified rational prime is the order of its
Frobenius. Hence

\[
f_p=\operatorname{ord}_d(p)
=\operatorname{ord}_d(p^{-1})
=\operatorname{ord}_d(q)=f_q.
\tag{R6}
\]

This verifies equality of all unlabelled cyclotomic decomposition data
claimed in A2. It does not identify which integer in the inversion orbit is
the smaller factor.

## 3. One-dimensional ray, genus, and class characters

Let \(\chi\) be a one-dimensional character on the relevant abelian
quotient and set

\[
z=\chi(\operatorname{Frob}_p).
\]

Applying \(\chi\) to (R4) gives

\[
\left(
\chi(\operatorname{Frob}_p),
\chi(\operatorname{Frob}_q)
\right)
=(z,z^{-1}).
\tag{R7}
\]

Their product is

\[
zz^{-1}=1.
\tag{R8}
\]

Equivalently, in the rational residue model,
\(N\equiv1\pmod d\), so every character modulo \(d\) takes value one on
\(N\). Thus the character value of the composite does not select one of
the two factors.

If \(\chi\) is a genus character, its values have order at most two.
Therefore

\[
z^{-1}=z\in\{1,-1\},
\]

and even separately granted local values agree.

For a more general public ray conductor coprime to \(N\), put

\[
\alpha=\chi(N)=\chi(p)\chi(q).
\]

If \(z=\chi(p)\), then

\[
\chi(q)=\alpha z^{-1}.
\tag{R9}
\]

The map

\[
T(z)=\alpha z^{-1}
\]

is an involution:

\[
T(T(z))
=\alpha(\alpha z^{-1})^{-1}
=z.
\tag{R10}
\]

It exchanges the two factor labels while preserving their public product
\(\alpha\). A conductor with a 2-part can make \(\alpha\ne1\), but it
does not remove this affine inversion ambiguity.

Exactly the same argument applies to an inverse class pair
\((C,C^{-1})\) in any abelian ray or ideal class group. A genus character
takes equal values on the pair, while a higher character takes inverse
values.

## 4. Hilbert-symbol product and the tame local-power claim

In a field containing \(\mu_m\), the \(m\)-th Hilbert symbol is
bimultiplicative. Thus, at every place where the symbols are defined,

\[
(p,a)_{m,v}(q,a)_{m,v}
=(pq,a)_{m,v}
=(N,a)_{m,v}.
\tag{R11}
\]

This is one product, not an ordered pair of the two hidden local values.
Global Hilbert reciprocity supplies further products of local symbols, so
it preserves the same distinction.

Let \(r\) be a rational prime dividing \(K\), with \(r\nmid m\). Because
\(K\) is odd, \(r\) is odd. Also

\[
N=2K+1\equiv1\pmod r.
\]

Apply Hensel's lemma to

\[
f(X)=X^m-N
\]

at \(X=1\). One has

\[
f(1)\equiv0\pmod r,
\qquad
f'(1)=m\not\equiv0\pmod r.
\]

There is therefore an \(x\in\mathbb Q_r\) with

\[
x^m=N.
\tag{R12}
\]

An \(m\)-th power represents the trivial class in either slot of the
Hilbert pairing. Hence all Hilbert symbols with \(N\) in one slot are
trivial at such tame primes \(r\).

When \(r\mid m\), the derivative argument is unavailable and a wild local
symbol can be nontrivial. Its product value \((N,a)_{m,v}\) still depends
only on public inputs and still constrains the hidden factors only through
(R11). The statement correctly does not claim tame triviality in this
case.

## 5. Closure of scalar reciprocity transcripts

The transcript definition permits only:

1. products over all hidden prime components;
2. fully symmetric residue or Jacobi symbols;
3. bilinear or global Hilbert products; and
4. public computations and adaptive choices based on prior entries of
   those types.

Each primitive entry is invariant under swapping \(p\) and \(q\). For a
character of conductor \(d\mid K\), every candidate pair

\[
(u,u^{-1}),\qquad u\in(\mathbb Z/d\mathbb Z)^\times,
\]

has the same product

\[
\chi(u)\chi(u^{-1})=1.
\tag{R13}
\]

Symmetric symbols are invariant by definition, and Hilbert data appear as
the public product (R11).

An induction on transcript length handles adaptivity. If all candidates
have produced the same entries through one stage, the public adaptive rule
chooses the same next conductor, character, or operation for all of them.
The next allowed primitive entry is again swap-invariant and, in the
\(d\mid K\) character case, is again (R13). Thus no allowed adaptive
sequence labels the two factors or eliminates a candidate inversion pair.

This conclusion relies on the exact transcript definition. It does not
apply to a sum of local values, a selected hidden prime ideal, a
non-diagonal CRT element, an exact divisor coefficient, or another
ring-valued carrier; all are expressly excluded.

## 6. The fixed witness \(N=527\)

The arithmetic data are exact:

\[
527=17\cdot31,\qquad
17<31<34,\qquad
527\equiv3\pmod4,
\]

and

\[
K=\frac{527-1}{2}=263.
\]

To verify primality of \(263\), it is enough to test primes at most
\(\sqrt{263}<17\):

\[
2,3,5,7,11,13
\]

all fail to divide it. Hence

\[
|(\mathbb Z/263\mathbb Z)^\times|=262=2\cdot131,
\]

and this unit group is cyclic.

The displayed square identities are also exact:

\[
65^2=4225=16\cdot263+17,
\]

\[
174^2=30276=115\cdot263+31.
\tag{R14}
\]

Thus both hidden factor residues are squares modulo \(263\).

For a homomorphism from a cyclic group of order \(262\) to \(\mu_m\), the
image order divides \(\gcd(262,m)\). For \(m=3\), this gcd is one, so every
cubic character is trivial. For \(m=4\) or \(8\), it is two. The image then
has exponent at most two, and every square lies in the character kernel:

\[
\chi(x^2)=\chi(x)^2=1.
\]

Equation (R14) therefore makes every cubic, quartic, octic, and genus
character value one on both \(17\) and \(31\), even if the two values are
provided separately.

## 7. Fixed-order cyclotomic residue symbols over \(263\)

For a rational prime \(\ell\nmid m\), the residue degree of a prime above
\(\ell\) in \(\mathbb Q(\zeta_m)\) is

\[
\operatorname{ord}_m(\ell).
\]

Here

\[
263\equiv-1\pmod3,\qquad
263\equiv-1\pmod4,\qquad
263\equiv-1\pmod8.
\]

Thus

\[
\operatorname{ord}_m(263)=2
\qquad(m=3,4,8).
\tag{R15}
\]

Every prime \(\mathfrak R\mid263\) in the corresponding cyclotomic field
has residue field of size \(263^2\).

Let \(a\) be a rational integer not divisible by \(263\). Its reduction
lies in the rational subfield

\[
\mathbb F_{263}^{\times}
\subset\mathbb F_{263^2}^{\times},
\]

so

\[
a^{262}=1.
\tag{R16}
\]

The \(m\)-th power residue symbol is represented by

\[
a^{(263^2-1)/m}.
\]

Since

\[
\frac{263^2-1}{m}
=262\frac{264}{m}
\]

and \(m=3,4,8\) all divide \(264\), equation (R16) makes this value one:

\[
\left(\frac a{\mathfrak R}\right)_m=1.
\tag{R17}
\]

This proves the assertion for every prime above \(263\), not just one
choice. A symbol whose numerator is a nonrational primary factor above
\(17\) or \(31\) uses factor-selected data absent from the rational scalar
input and is outside this conclusion.

## 8. Common-order obstruction for rational bases

Let \(a\) be a unit modulo \(527\) satisfying

\[
a^{526}=1\pmod{527}.
\]

Its local order modulo \(17\) divides both \(16\) and \(526\), hence
divides

\[
\gcd(16,526)=2.
\]

Its local order modulo \(31\) divides both \(30\) and \(526\), hence
divides

\[
\gcd(30,526)=2.
\tag{R18}
\]

Thus the two local residues are independently in \(\{1,-1\}\).

Because \(K=263\) is odd, raising to the \(K\)-th power preserves these
signs. If they differ, one hidden prime divides \(a^K-1\) and the other
divides \(a^K+1\). Therefore the two gcds

\[
\gcd(a^K-1,N),\qquad
\gcd(a^K+1,N)
\]

are the two proper factors, in some order.

If the signs agree, they are either both \(1\), giving exact common order
one, or both \(-1\), giving exact common order two. Factor-first stripping
of the known exponent \(526=2\cdot263\) can return only that public common
order unless it first returns a proper factor. Equation (R18) proves that
no base satisfying the return condition can yield a larger local or common
order.

## 9. Complete-component coefficient-content extraction

Let

\[
A_m=\mathbb Z[Z]/(\Phi_m(Z)).
\]

Because \(\Phi_m\) is monic of degree \(\varphi(m)\), the ring is a free
\(\mathbb Z\)-module with basis

\[
1,\zeta_m,\ldots,\zeta_m^{\varphi(m)-1}.
\tag{R19}
\]

Reduction modulo any rational prime preserves this coefficient basis:
an element is zero in \(A_m/pA_m\) exactly when all its standard
coefficients are divisible by \(p\).

The hypothesis \(\gcd(m,N)=1\) ensures that both \(p\) and \(q\) are
unramified in the cyclotomic ring. More concretely, \(X^m-1\) is separable
modulo either prime. The roots of \(\Phi_m\) in an algebraic closure then
have exact order \(m\). Consequently, in the complete rational component
\(A_m/qA_m\),

\[
\zeta_m^a=\zeta_m^b
\iff a\equiv b\pmod m.
\tag{R20}
\]

The same holds modulo \(p\).

Choose representatives \(0\leq a,b<m\). At \(e=a\), condition (C1) gives

\[
Y-\zeta_m^a=0\quad\text{in }A_m/pA_m.
\]

By (R19), every coefficient \(c_{a,j}\) is divisible by \(p\). In the
other rational component,

\[
Y-\zeta_m^a
=\zeta_m^b-\zeta_m^a
\ne0\quad\text{in }A_m/qA_m
\]

by (R20). Therefore at least one coefficient \(c_{a,j}\) is not divisible
by \(q\). Since \(N=pq\) is squarefree,

\[
g_a
=\gcd(N,c_{a,0},\ldots,c_{a,\varphi(m)-1})
=p.
\tag{R21}
\]

Interchanging \(a,b\) and \(p,q\) gives

\[
g_b=q.
\tag{R22}
\]

The extraction algorithm does not know \(a\) or \(b\). It enumerates all
\(0\leq e<m\), computes the coefficient content, and accepts any gcd
strictly between one and \(N\). Equations (R21) and (R22) guarantee two
successful indices.

This is exactly where the complete-rational-component condition matters.
Vanishing at one selected prime ideal over \(p\) would not make every
power-basis coefficient divisible by \(p\); vanishing in \(A_m/pA_m\)
does.

## 10. Bit complexity of the coefficient-content transition

The explicit element \(Y\) uses
\(\varphi(m)\) coefficients modulo \(N\), hence

\[
O(\varphi(m)n)
\]
input bits. The hypotheses make this numerical QP.

The presentation polynomial can also be handled within that bound. Its
degree is \(\varphi(m)\), its integer coefficients have
\[
O(\varphi(m))
\]
bits by the elementary-root bound on coefficients, and it can be
constructed using polynomial arithmetic in a number of operations
polynomial in the numerical value of \(m\). Since \(m\) is numerical QP,
this is numerical QP in \(n\).

Starting from the standard vector for \(1\), repeated multiplication by
\(\zeta_m\) and reduction by \(\Phi_m\) generates all vectors
\(\zeta_m^e\) for \(0\leq e<m\). There are \(m\varphi(m)\) output
coefficients modulo \(N\). Each modular ring operation and each gcd has
bit complexity polynomial in \(n\), \(\varphi(m)\), and the coefficient
sizes.

A product of numerical-QP quantities, and a polynomial in them, is still
numerical QP. Thus enumeration of all \(e\), coefficient subtraction, and
gcd extraction are deterministic numerical QP. No hidden factor or
selected prime ideal is used by the algorithm.

## 11. Selected-prime norm boundary

Choose any integral lift of \(Y-\zeta_m^e\). Its algebraic norm can be
computed as a resultant or as the determinant of multiplication in the
power basis. Divisibility by \(p\) or \(q\) is independent of the chosen
lift modulo \(N\).

Because \(p,q\nmid m\), the reductions are finite products of residue
fields:

\[
A_m/pA_m\simeq\prod_{\mathfrak p\mid p}k(\mathfrak p),
\qquad
A_m/qA_m\simeq\prod_{\mathfrak q\mid q}k(\mathfrak q).
\tag{R23}
\]

Modulo a rational prime, the algebraic norm is the product of the
corresponding field norms of all components. It vanishes modulo \(p\) if
the element vanishes at at least one selected
\(\mathfrak p\mid p\). It is nonzero modulo \(q\) only if the element is
nonzero at every \(\mathfrak q\mid q\).

Hence a label match at one selected prime above \(p\) proves

\[
p\mid\operatorname N(Y-\zeta_m^e),
\]

but a separate no-collision condition at every prime above \(q\) is needed
to prove

\[
q\nmid\operatorname N(Y-\zeta_m^e).
\]

When exactly one rational factor divides the norm, its gcd with \(N\)
extracts that factor. Two different labels at two selected prime ideals do
not control unselected prime ideals and therefore do not imply the required
norm separation. This verifies both the positive variant and its stated
limitation.

With numerical-QP degree and input representation, determinant or
resultant computation and the final gcd also have numerical-QP bit
complexity.

## 12. Fourier proof that traces separate inversion orbits

For \(u\in G=(\mathbb Z/K\mathbb Z)^\times\), define the function

\[
\mu_u=\delta_u+\delta_{u^{-1}}
\]

on the finite abelian group \(G\), with multiplicity two when
\(u=u^{-1}\). Its Fourier coefficient at
\(\chi\in\widehat G\) is

\[
\widehat{\mu_u}(\chi)
=\chi(u)+\chi(u^{-1})
=\chi(u)+\chi(u)^{-1}
=t_\chi(u).
\tag{R24}
\]

If \(t_\chi(u)=t_\chi(v)\) for every character, then all Fourier
coefficients of \(\mu_u\) and \(\mu_v\) agree. Fourier inversion on the
finite group gives

\[
\mu_u=\mu_v.
\]

Thus the unordered multisets

\[
\{u,u^{-1}\}
\quad\text{and}\quad
\{v,v^{-1}\}
\]

are equal, and

\[
v=u\quad\text{or}\quad v=u^{-1}.
\tag{R25}
\]

This proves separation by the full trace family, including the
self-inverse case.

## 13. The divisor coefficient and conditional positive transition

The divisors of \(N=pq\) are \(1,p,q,N\). For any
\(\chi\in\widehat G\),

\[
\begin{aligned}
\sum_{d\mid N}\chi(d)
&=\chi(1)+\chi(p)+\chi(q)+\chi(N)\\
&=1+\chi(p)+\chi(p)^{-1}+1\\
&=2+t_\chi(p).
\end{aligned}
\tag{R26}
\]

Here (R2) with \(d=K\) gives
\(\chi(q)=\chi(p)^{-1}\), and \(N\equiv1\pmod K\) gives
\(\chi(N)=1\).

Therefore an exact evaluator for the divisor coefficient supplies the
trace after subtracting two. If a uniformly constructible numerical-QP
subfamily of characters separates all live inversion orbits, and if:

1. every required coefficient is evaluated exactly in numerical-QP time;
2. all character values have numerical-QP exact representations; and
3. a numerical-QP decoder maps the trace vector to its inversion orbit,

then the orbit of \(p\bmod K\) is recovered. Section 1 converts that orbit
to the actual unordered factors.

The full dual group can have too many characters, and equation (R26) is a
sum rather than the reciprocity product
\[
\chi(p)\chi(q)=1.
\]
Neither Fourier separation nor ordinary reciprocity supplies an exact
coefficient evaluator. The statement therefore keeps bank construction,
representation, coefficient evaluation, and decoding as explicit
conditional costs.

## 14. Strict scope conclusion

The reconstructed negative boundary applies only to the scalar abelian
transcripts defined at the start:

- one-dimensional Artin, ray, genus, and residue-symbol products;
- unlabelled cyclotomic splitting information;
- symmetric Jacobi or residue data; and
- Hilbert-symbol information available only through bilinear or global
  products.

The following stronger inputs remain outside that boundary:

1. a factor-free construction of the complete-component non-diagonal
   element in (C1);
2. an exact compressed evaluator for the divisor coefficient;
3. selected-prime data with a proved all-primes norm separator;
4. nonabelian or nonlinear ring-valued data;
5. Archimedean, exact-division, or reciprocal-prefix selectors; and
6. an independently supplied multiple of a hidden group order.

The fixed input \(527\) is a witness against the listed fixed-order scalar
labels, not an all-input theorem. Theorems C and D are positive transitions
conditioned on data or evaluators that F215 does not construct. Nothing in
the statement constitutes a general higher-reciprocity lower bound or a
factoring algorithm.
