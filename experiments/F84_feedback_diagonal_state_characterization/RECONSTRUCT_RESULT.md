# PASS

The SHA-256 of RECONSTRUCT_STATEMENT.md is
c903631dd78edc6487c3f3f890d3078a2f332a46012449456dc402cc523b7812,
as required. All claims are correct with the exhaustive-versus-access scope
made explicit below.

## 1. Equivalence of the four graph-state conditions

Write an element \(x\in H\) as \(x=(x_p,x_q)\), and let

\[
\pi_p:H\to H_p,\qquad \pi_q:H\to H_q
\]

be the two projections. Because \(N=pq\),

\[
1<\gcd(x-1,N)<N
\]

holds exactly when one, but not both, of \(x_p,x_q\) is \(1\).
Consequently, condition 1 is equivalent to

\[
\ker\pi_p=\ker\pi_q.
\]

The intersection of these two kernels contains only the global identity:

\[
\ker\pi_p\cap\ker\pi_q=\{(1,1)\}.
\]

If the kernels are equal, their common value equals their intersection and
is therefore trivial. Both projections are injective. They are surjective
onto \(H_p,H_q\) by the definition of projection image, so they are
isomorphisms. This proves \(1\Rightarrow2\). The converse is immediate:
if both kernels are trivial, a local identity in either coordinate forces
\(x=(1,1)\), so a positive separator cannot occur.

If both projections are isomorphisms, define

\[
\varphi=\pi_q\circ\pi_p^{-1}:H_p\longrightarrow H_q.
\]

It is an isomorphism, and

\[
H=\{(y,\varphi(y)):y\in H_p\}.
\]

Thus \(2\Rightarrow3\). Conversely, both coordinate projections of the graph
of an isomorphism are isomorphisms, so \(3\Rightarrow2\).

Assume condition 2. Isomorphisms preserve element order. For every
\(x\in H\),

\[
\operatorname{ord}_p(x)
=\operatorname{ord}_H(x)
=\operatorname{ord}_q(x).
\]

This proves \(2\Rightarrow4\). Finally, assume condition 4. If \(x_p=1\),
then its local order is one, so \(x_q\) also has order one and equals \(1\).
The converse is symmetric. Identity status is synchronized, so condition 1
holds. All four conditions are equivalent, including when \(H\) is trivial.

## 2. Negative signs and exact saturation kernels

In the multiplicative group of a field of odd characteristic, \(-1\) is the
unique element of order two. Under condition 4, if \(x_p=-1\), then

\[
\operatorname{ord}_p(x)=2
\]

and hence \(\operatorname{ord}_q(x)=2\), which forces \(x_q=-1\). The
converse is symmetric. Thus negative-identity status is synchronized for
every \(x\in H\). In particular,

\[
\gcd(x+1,N)\in\{1,N\}
\]

for every \(x\in H\).

Now fix any explicit relation list on \(Q\), any prime \(\ell\), and its
exact prime-saturation root map

\[
R_\ell:V_\ell\longrightarrow H.
\]

The image lies in \(H\) because every exact root produced by the map is a
product of integer powers of the public blocks \(Q\). Let

\[
L_p=\{v\in V_\ell:(R_\ell(v))_p=1\},
\qquad
L_q=\{v\in V_\ell:(R_\ell(v))_q=1\}.
\]

Every element of \(H\) has synchronized identity status, so for every
\(v\in V_\ell\),

\[
(R_\ell(v))_p=1\iff(R_\ell(v))_q=1.
\]

Therefore

\[
L_p=L_q.
\]

This argument includes a trivial root space, a trivial local
\(\ell\)-th-root group, \(\ell=2\), and primes \(\ell\) equal to \(p\) or
\(q\). It uses only that the exact root residue remains in \(H\).

Hence small-prime saturation failure is logically redundant once
subgroup-wide direct positive-sign failure has been established
exhaustively. It need not be computationally redundant: proving or checking
the exhaustive condition can require access to an exponentially large
subgroup, while an explicit saturation decoder tests a small public family.

## 3. Finite-menu failure is strictly weaker

The fixed example factors as

\[
35=5\cdot7.
\]

For the listed generator,

\[
\gcd(2-1,35)=1,\qquad
\gcd(2+1,35)=\gcd(3,35)=1.
\]

An empty relation list has no nonzero relation-coordinate vector and hence
no nontrivial saturation root. Nevertheless,

\[
2^3-1=7,
\qquad
\gcd(2^3-1,35)=7.
\]

Equivalently, \(2\) has local orders \(4\) modulo \(5\) and \(3\) modulo
\(7\), so condition 4 fails for \(H=\langle2\rangle\). The tested generator
does not reveal the later subgroup element \(2^3\). This proves that failure
of a finite direct-sign menu, even together with an empty saturation space,
does not imply the exhaustive graph-state condition.

## 4. Quotient projections after feedback

Assume \(H\le K\) and that \(H\) is a graph state. Since the ambient unit
group is abelian, \(H\) is normal in \(K\). Projection induces maps

\[
\bar\pi_p:K/H\longrightarrow K_p/H_p,
\qquad
\bar\pi_q:K/H\longrightarrow K_q/H_q.
\]

They are well-defined. They are also surjective: every local coset has a
representative obtained by projecting an element of \(K\). Their domain and
codomain sizes are

\[
|K/H|=c,\qquad
|K_p/H_p|=a,\qquad
|K_q/H_q|=b.
\]

The first isomorphism theorem, or Lagrange's theorem applied to the kernels,
therefore gives

\[
a\mid c,\qquad b\mid c.
\]

Because \(H\) is a graph,

\[
|H|=|H_p|=|H_q|=h.
\]

It follows that

\[
|K|=ch,\qquad |K_p|=ah,\qquad |K_q|=bh.
\]

The number of elements of \(K\) whose \(p\)-coordinate is \(1\) is the size
of the projection kernel:

\[
|\ker(\pi_p|_K)|=\frac{|K|}{|K_p|}=\frac ca.
\]

Similarly,

\[
|\ker(\pi_q|_K)|=\frac cb.
\]

The intersection of these kernels is the global identity alone. Positive
separators form their symmetric difference. Their exact number is therefore

\[
\boxed{\frac ca+\frac cb-2}.
\]

The projection \(K\to K_p\) is injective exactly when \(c/a=1\), or
\(c=a\). The \(q\)-projection is injective exactly when \(c=b\). By the
equivalence in Section 1, \(K\) remains a graph exactly when both are
injective:

\[
K\text{ is a graph}\iff c=a=b.
\]

Since \(a,b\mid c\), graph failure is exactly

\[
c>a\quad\text{or}\quad c>b.
\]

These conclusions include \(H=1\), \(K=H\), and one-sided local growth.

## 5. A single-overlap extension and cancellation words

Let \(K=\langle H,u\rangle\). The quotient \(K/H\) is cyclic and generated
by \(uH\). Therefore the order of the global coset \(uH\) is

\[
\operatorname{ord}_{K/H}(uH)=[K:H]=c.
\]

Likewise, \(K_p/H_p\) is generated by \(u_pH_p\), and \(K_q/H_q\) is
generated by \(u_qH_q\). Hence

\[
\operatorname{ord}_{K_p/H_p}(u_pH_p)=a,\qquad
\operatorname{ord}_{K_q/H_q}(u_qH_q)=b.
\]

Take an exponent \(t\) with

\[
0<t<c,\qquad a\mid t.
\]

The quotient-order condition gives \(u_p^t\in H_p\). Since
\(\pi_p:H\to H_p\) is an isomorphism, there is a unique \(h_t\in H\) such
that

\[
(h_t)_p=u_p^{-t}.
\]

Thus \(h_tu^t\) has \(p\)-coordinate \(1\). Its \(q\)-coordinate cannot also
be \(1\): if it were, CRT would give \(h_tu^t=1\), so
\(u^t=h_t^{-1}\in H\), contradicting the fact that \(uH\) has order \(c\)
and \(0<t<c\). Therefore \(h_tu^t\) is a positive separator.

The symmetric statement is exact: for every \(0<t<c\) divisible by \(b\),
there is a unique \(h'_t\in H\) whose \(q\)-coordinate cancels \(u_q^t\),
and \(h'_tu^t\) is a positive separator with only its \(q\)-coordinate equal
to \(1\).

There are \(c/a-1\) positive multiples of \(a\) below \(c\), matching the
nonidentity part of the \(p\)-projection kernel. There are \(c/b-1\)
corresponding \(q\)-cancellations. The two families are disjoint, and their
sum is the separator count from Section 4.

## 6. Exact classification of the fixed phase witness

Use

\[
N=2047=23\cdot89,
\qquad
H_0=\langle11\rangle,
\qquad
K=\langle11,2\rangle.
\]

The given local orders of \(11\) are both \(22\). Therefore the global order
of \(11\) modulo \(N\) is

\[
\operatorname{lcm}(22,22)=22,
\]

and \(|H_0|=22\). The equal local orders also show that \(H_0\) is a graph
state.

The local order of \(2\) is \(11\) at both primes, so its global order is
\(11\). The coset \(2H_0\) in \(K/H_0\) consequently has order dividing
\(11\). It is not the identity coset because \(2\notin H_0\). Since \(11\)
is prime,

\[
c=\operatorname{ord}_{K/H_0}(2H_0)=11.
\]

Modulo \(23\), the subgroup \(H_{0,p}\) has order \(22\), which is the full
order of \(\mathbb F_{23}^\times\). Thus \(2\) already lies in \(H_{0,p}\)
and

\[
a=[K_p:H_{0,p}]=1.
\]

Modulo \(89\), the multiplicative group is cyclic. Its subgroup
\(H_{0,q}\) has order \(22\), so it contains the unique subgroup of order
\(11\). Every element of order \(11\), including \(2\), lies in that unique
subgroup. Hence \(2\in H_{0,q}\) and

\[
b=[K_q:H_{0,q}]=1.
\]

Therefore

\[
\boxed{c=11,\qquad a=b=1}.
\]

Neither local projection grows, but \(c>a,b\), so the graph breaks. The
exact positive-separator count is

\[
\frac{11}{1}+\frac{11}{1}-2=20.
\]

Finally,

\[
2\cdot11=22\equiv-1\pmod{23},
\]

while \(22\not\equiv-1\pmod{89}\), where \(-1\equiv88\). Thus \(22\) is a
negative separator, and indeed

\[
\gcd(22+1,2047)=\gcd(23,23\cdot89)=23.
\]

## 7. Scope

The characterization is structural. It does not reveal the hidden factors
\(p,q\), and it does not publicly compute \(a,b,c\). The cancellation proof
uses the hidden isomorphism \(H\to H_p\) to establish existence and
uniqueness; it does not give a public method to find the cancelling element.

Exhaustively checking every element of \(H\) can require exponential work.
The theorem does not enumerate \(H\), select a short cancellation word, or
show that a residue-neutral feedback refinement enlarges the subgroup on
every input. It therefore gives no all-input factoring algorithm.

After a graph break, the ambient subgroup contains positive separators by
the exact count. A current finite word menu or a currently exposed
small-prime root space can still miss them. Such a failure is an access gap,
not evidence that the ambient subgroup is separator-free. The \(N=35\)
example already shows the same logical distinction before feedback.
