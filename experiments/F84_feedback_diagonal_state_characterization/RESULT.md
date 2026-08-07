# F84 — exhaustive direct-sign failure is exactly a diagonal graph state

**Status:** proof-only candidate. No research computation was run. This is a
state-characterization theorem and a residue-neutral refinement theorem. It
is not a selector, a relation source, or a factoring algorithm. No literature
novelty claim is made.

## 1. The quantifier that matters

Let

\[
N=pq
\]

for distinct odd primes, and let \(Q\) be an explicit set of public unit
blocks. Put

\[
H=\langle Q\rangle
\leq
(\mathbb Z/N\mathbb Z)^\times
\cong
\mathbb F_p^\times\times\mathbb F_q^\times.
\]

There are two different statements that must not be conflated.

1. **Exhaustive direct-sign failure:** every element of \(H\) fails the two
   direct sign gcds.
2. **Menu failure:** every element in one declared public finite menu fails.

Only the exhaustive statement characterizes the hidden subgroup. A finite
menu can miss a separator that already exists in \(H\).

For an explicit relation list on \(Q\), and for a public prime \(\ell\), let

\[
\rho_\ell:V_\ell\longrightarrow
\mu_\ell(\mathbb F_p)\times\mu_\ell(\mathbb F_q)
\]

be the exact prime-saturation root map of F83. Write
\(K_{p,\ell}\) and \(K_{q,\ell}\) for its two identity kernels.
The complete support-two decoder fails exactly when these kernels agree.

## 2. Diagonal-state theorem

### Theorem 1

The following conditions are equivalent.

1. For every \(x\in H\),

   \[
   \gcd(x-1,N)\in\{1,N\}.
   \tag{1}
   \]

2. Both projection maps

   \[
   H\longrightarrow H_p,
   \qquad
   H\longrightarrow H_q
   \]

   are isomorphisms.

3. There is an isomorphism

   \[
   \varphi:H_p\longrightarrow H_q
   \]

   such that

   \[
   H=\{(y,\varphi(y)):y\in H_p\}.
   \tag{2}
   \]

4. Every \(x\in H\) has equal local orders:

   \[
   \operatorname{ord}_p(x)
   =
   \operatorname{ord}_q(x).
   \tag{3}
   \]

When these conditions hold, negative signs also synchronize:

\[
\gcd(x+1,N)\in\{1,N\}
\qquad
\text{for every }x\in H.
\tag{4}
\]

Moreover, for every explicit relation list on the blocks \(Q\) and every
prime \(\ell\),

\[
\boxed{K_{p,\ell}=K_{q,\ell}.}
\tag{5}
\]

Thus every prime-saturation identity decoder fails. The restriction to
small or polynomial-size primes is needed for executable cost, but not for
the structural conclusion.

### Proof

The kernel of \(H\to H_p\) consists of elements \((1,y)\). Every nonidentity
element in this kernel is a positive separator, contrary to (1). Hence the
projection is injective. The same argument applies at \(q\). Each projection
is surjective onto its image by definition, proving condition 2.

Two bijective projections identify \(H\) with \(H_p\) and \(H_q\). Their
composition gives \(\varphi\) and the graph description (2). Conversely, a
graph of an isomorphism has trivial kernels in both projections, so it has
no positive separator. This proves the equivalence of conditions 1--3.

An isomorphism preserves element orders, so condition 3 implies (3). If
(3) holds and \(x\) lies in the kernel of the \(p\)-projection, then its
local \(p\)-order is one. Its \(q\)-order is also one, so \(x\) is the
global identity. Both projections are therefore injective, proving the
converse.

If \(x_p=-1\), then \(x_p\) has order two. Equal local orders force \(x_q\)
to have order two. The unique order-two element of
\(\mathbb F_q^\times\) is \(-1\). The converse is symmetric, proving (4).

Finally, every saturation root \(R_\ell(c)\) is a product of the blocks
\(Q\), so it lies in \(H\). Under the graph identification,

\[
R_\ell(c)_q
=
\varphi(R_\ell(c)_p).
\]

An isomorphism sends the identity to the identity. Therefore the root is
one modulo \(p\) exactly when it is one modulo \(q\), which is (5).
\(\square\)

### Exact consequence

Once condition (1) quantifies over the full subgroup, the added hypothesis
that all small-prime saturation decoders fail is logically redundant. A
diagonal graph state automatically defeats every identity-target prime
saturation decoder, not only the small ones.

## 3. What saturation failure says without exhaustive direct tests

### Theorem 2

For one fixed prime \(\ell\), the complete prime-saturation decoder fails if
and only if

\[
K_{p,\ell}=K_{q,\ell}.
\tag{6}
\]

After hidden identifications of nontrivial local root groups with
\(\mathbb F_\ell\), this has exactly two forms:

1. both local root functionals are zero; or
2. both are nonzero and one is a nonzero scalar multiple of the other.

Failure for a set \(\Lambda\) of public primes means only that this
projective synchronization holds separately on each root space
\(V_\ell\). It does not imply that the ambient block subgroup \(H\) is a
graph.

### Proof

F83's support-two theorem is complete for the identity-kernel gate, so
decoder failure is exactly (6). A nonzero linear functional to
\(\mathbb F_\ell\) is determined up to nonzero scalar by its hyperplane
kernel. Hence equal kernels have the two displayed forms.

These root maps can see only their images \(\rho_\ell(V_\ell)\). They need
not cover a projection kernel of the ambient subgroup. Therefore their
kernel agreement gives no injectivity theorem for \(H\). \(\square\)

### Finite-menu counterexample

Take

\[
N=35=5\cdot7,
\qquad
Q=\{2\},
\qquad
H=\langle2\rangle.
\]

The direct signs of the listed generator fail:

\[
\gcd(2-1,35)=\gcd(2+1,35)=1.
\]

With an empty relation list, every prime-saturation space is
\(\mathbb F_\ell^0\), so every saturation decoder is empty and fails.
Nevertheless,

\[
2^3=8,
\qquad
\gcd(8-1,35)=7.
\]

The subgroup already contains a positive separator and is not a graph.
Indeed, the local orders of \(2\) are \(4\) modulo \(5\) and \(3\) modulo
\(7\).

Thus failure of all declared small-prime decoders plus a finite direct menu
does not certify a synchronized diagonal state.

## 4. Residue-neutral canonical feedback

Assume now that the old subgroup \(H\) satisfies Theorem 1. Append public
canonical-inverse endpoints \(g,w\) with

\[
gw\equiv1\pmod N,
\qquad
g,w\in H.
\tag{7}
\]

At the residue level, these endpoints add nothing:

\[
\langle H,g,w\rangle=H.
\]

Joint exact gcd-free refinement of the old blocks and the new integer
endpoints can nevertheless expose smaller integer blocks. Let \(Q'\) be the
refined block list and put

\[
K=\langle Q'\rangle.
\]

Every old block is a product of refined descendants, so

\[
H\leq K.
\tag{8}
\]

The inclusion can be strict because membership of an integer product in
\(H\) does not force the residues of its integer factors to lie in \(H\).
This is the exact place where canonical integer representation changes the
state.

## 5. Exact quotient-kernel transition

Put

\[
h=|H|,
\qquad
c=[K:H],
\qquad
a=[K_p:H_p],
\qquad
b=[K_q:H_q].
\tag{9}
\]

### Theorem 3

The quotient projections

\[
K/H\longrightarrow K_p/H_p,
\qquad
K/H\longrightarrow K_q/H_q
\]

are surjective. Hence \(a\mid c\) and \(b\mid c\).

The number of positive separators in \(K\) is exactly

\[
\boxed{\frac ca+\frac cb-2.}
\tag{10}
\]

The following are equivalent.

1. \(K\) is still a diagonal graph state.
2. Every direct positive-sign test on \(K\) fails.
3. \(c=a=b\).
4. Both quotient projections have trivial kernels.

Therefore a residue-neutral refinement breaks the old diagonal structure
exactly when

\[
\boxed{c>a\quad\text{or}\quad c>b.}
\tag{11}
\]

### Proof

The ambient group is abelian, so the quotient maps are well-defined. They
are surjective by the definitions of \(K_p,K_q\). Their target sizes are
\(a,b\), while their source has size \(c\), proving the divisibilities.

The group sizes are

\[
|K|=ch,\qquad
|K_p|=ah,\qquad
|K_q|=bh,
\]

because \(|H|=|H_p|=|H_q|=h\). The kernels of
\(K\to K_p\) and \(K\to K_q\) therefore have sizes \(c/a\) and \(c/b\).
After the shared identity is removed, these two kernels are disjoint and
are exactly the two types of positive separator. This gives (10).

The count is zero exactly when \(c/a=c/b=1\), which is \(c=a=b\). By
Theorem 1, absence of positive separators is equivalent to the graph
condition. This also proves the quotient-kernel formulation. \(\square\)

### Interpretation

The endpoints in (7) are residue-redundant. The split breaks synchronization
only if the newly exposed factor blocks create a kernel in at least one
hidden quotient projection. Projection growth by itself is not the event:
a lockstep enlargement with \(c=a=b>1\) remains a graph.

## 6. One-overlap split

Suppose the only new refinement is one public overlap

\[
B=uv,
\qquad
g=uz,
\tag{12}
\]

where \(B\) is an old block, \(g\in H\) is a feedback endpoint, and the
gcd-free refinement exposes \(u\). All quantities are units because \(B\)
and \(g\) are units. Assume no other overlap introduces an independent
block coset.

Then

\[
v=Bu^{-1}\pmod N,
\qquad
z=gu^{-1}\pmod N,
\]

so the refined subgroup is

\[
K=\langle H,u\rangle.
\tag{13}
\]

### Corollary 4

In this cyclic extension,

\[
\begin{aligned}
c&=\operatorname{ord}(uH\text{ in }K/H),\\
a&=\operatorname{ord}(u_pH_p\text{ in }K_p/H_p),\\
b&=\operatorname{ord}(u_qH_q\text{ in }K_q/H_q).
\end{aligned}
\tag{14}
\]

Every element of \(K\) has a unique form

\[
u^t y,
\qquad
0\leq t<c,
\qquad
y\in H.
\tag{15}
\]

For every \(t\) divisible by \(a\), there is a unique \(y\in H\) that
cancels \(u_p^t\). If \(0<t<c\), the resulting element is a positive
separator. The analogous statement holds at \(q\).

Thus the graph breaks exactly when a power of the exposed block can be
cancelled by one old element in one hidden component before the block coset
returns globally.

### Proof

Equation (13) makes \(K/H\) cyclic and proves (14). Equality of two
representations in (15) would put \(u^{t-t'}\) in \(H\), so \(c\mid t-t'\);
the chosen range gives uniqueness.

The condition \(a\mid t\) is exactly
\(u_p^t\in H_p\). Since \(H\to H_p\) is an isomorphism, there is one and
only one \(y\in H\) with

\[
y_p=u_p^{-t}.
\]

Then \((u^ty)_p=1\). If its \(q\)-component were also one, the element would
be the global identity, forcing \(c\mid t\). This is impossible for
\(0<t<c\). Hence it is a positive separator. \(\square\)

## 7. Order and phase are different quotient patterns

The raw local orders of the exposed block control pure powers:

\[
\gcd(u^E-1,N)\text{ is proper}
\iff
\operatorname{ord}_p(u)\mid E
\mathbin{\mathrm{xor}}
\operatorname{ord}_q(u)\mid E.
\tag{16}
\]

But equal raw local orders do not imply that \(K\) remains a graph. The
block can have synchronized pure powers while its phase relative to the old
graph differs.

The strongest phase-only quotient pattern is

\[
\boxed{c>1,\qquad a=b=1.}
\tag{17}
\]

Here neither local projection subgroup grows:

\[
K_p=H_p,\qquad K_q=H_q.
\]

All growth occurs inside the old rectangle \(H_p\times H_q\), by adding new
pairings between the same local elements. The old graph is replaced by
several graph cosets. Formula (10) gives \(2c-2\) positive separators even
though both local image groups are unchanged.

## 8. The F82 phase witness has \(c=11,\ a=b=1\)

For

\[
N=2047=23\cdot89,
\qquad
H_0=\langle11\rangle,
\]

the old local orders are \(22,22\), so \(H_0\) is a graph of size \(22\).
The canonical feedback endpoints

\[
g=1778=11^7\bmod N,
\qquad
w=1735=11^{-7}\bmod N
\]

already lie in \(H_0\). Their integer overlap with the old endpoint \(312\)
exposes

\[
u=2.
\]

The block \(2\) has local orders \(11,11\), so every pure direct-sign power
is synchronized. It is not in \(H_0\), because

\[
2\cdot11=22
\]

is \(-1\) modulo \(23\) but not modulo \(89\).

Since \(2^{11}=1\pmod N\), the coset \(2H_0\) has order dividing \(11\).
It is nontrivial, and \(11\) is prime, so

\[
c=11.
\]

Modulo \(23\), \(H_{0,p}\) has order \(22=|\mathbb F_{23}^\times|\), so it
already contains \(2\). Thus \(a=1\).

Modulo \(89\), \(H_{0,q}\) is cyclic of order \(22\). It contains the unique
subgroup of order \(11\) in \(\mathbb F_{89}^\times\). Since \(2\) has
order \(11\), it lies in that subgroup, so \(b=1\).

Therefore

\[
\boxed{c=11,\qquad a=b=1.}
\]

The feedback changes no local projection image, yet it breaks the graph and
creates

\[
11+11-2=20
\]

positive separators in the refined subgroup. The displayed public word
\(2\cdot11=22\) is a negative separator. This is a literal
canonical-integer realization of a pure phase break.

## 9. Saturation after a graph break

If refinement leaves \(K\) as a graph, then Theorem 1 applies to every
relation root map on the refined blocks, and all prime-saturation identity
decoders fail.

If refinement breaks the graph, \(K\) contains a direct separator
mathematically. It does not follow that any chosen small-prime saturation
space reaches that separator. For each \(\ell\), the decoder still sees only
\(\rho_\ell(V_\ell)\), and it can have equal local kernels even inside a
non-graph ambient subgroup.

Therefore:

- exhaustive direct-sign failure after refinement is equivalent to the
  graph surviving;
- failure of all currently available small-prime saturation decoders is not;
  and
- continued failure of a finite direct menu after (11) is an access or
  selector gap, not absence of a separator from the subgroup.

## 10. Exact conclusion and scope

A state in which every **subgroup element** fails direct signs is exactly a
synchronized diagonal graph. In that state, every identity-target
prime-saturation decoder fails automatically.

Canonical feedback can break the graph without adding an endpoint residue:
the new endpoints stay in \(H\), but gcd-free integer refinement exposes
factor blocks outside \(H\). The exact break is a nontrivial kernel in one
of the quotient projections \(K/H\to K_p/H_p,K_q/H_q\). A phase-only split
can even have no local projection growth at all.

This theorem does not make the hidden indices \(a,b,c\) public, enumerate
the enlarged subgroup, select a cancellation word, or prove that a useful
split occurs on general inputs. It supplies no all-input probability law or
factoring algorithm. Its role is only to distinguish algebraic absence from
failure of the current public selectors.
