# Blind reconstruction of F143

## Integrity and verdict

The SHA-256 of the only input consulted, STATEMENT.md, is

bc9a9e399c03bff991cc85920eb6c0218276b1d05d0788b82461b39030b1a35a

**Verdict: verified.** All algebraic claims follow from the stated
definitions. The legal-edge hypothesis is essential. The complete-graph and
complexity conclusions are conditional in exactly the way stated. Four
wording qualifications are worth making explicit:

1. Equation (4) identifies the label quotient with the vertex parameter set.
   The displayed residues form the coset \(q\Phi(\mathbb Z^m)^2\), not
   necessarily a subgroup under ordinary residue multiplication.
2. “Outside the two global roots” means outside
   \(\{+1,-1\}\cap\Phi(\mathbb Z^m)[2]\). The element \(-1\) need not belong
   to the generated subgroup.
3. In Section 5, a signed word can repeat a logical edge. To obtain an
   element of the binary cycle space, reduce repeated occurrences modulo
   two. This preserves the normalized root, as proved below.
4. In Section 7, the residual \(r_\ell\) and its square requirement concern
   wrapped anchors. An unwrapped anchor already gives an individually exact
   square bridge and can be removed from a dependency.

These are interpretation details, not counterexamples to the statement.

## 1. Public vertices

Put

\[
H=\Phi(\mathbb Z^m)\le (\mathbb Z/N\mathbb Z)^\times.
\]

Since \(q\) is a unit,

\[
v_z=v_{z'}
\iff \Phi(z)^2=\Phi(z')^2
\iff \Phi(2(z-z'))=1
\iff z-z'\in\Lambda_2.
\]

Thus the map \(z\mapsto v_z\) has kernel \(\Lambda_2\). Multiplication by
\(q\) is a bijection on residues, so its image is the coset \(qH^2\). The
first isomorphism theorem applied to \(z\mapsto\Phi(z)^2\) gives

\[
\mathbb Z^m/\Lambda_2\cong H^2.
\]

This proves (3) and the precise set-theoretic/group interpretation of (4).
Negative coordinates cause no problem because every \(a_j\) is a unit. This
group fact says nothing about which negative or positive exponent words
occur in the frozen source grammar.

## 2. Edge and bridge identities

For a positive step \(z\to z+e_j\), homomorphicity of \(\Phi\) gives

\[
h_e=v_{z+e_j}=[v_z a_j^2]_N=[u_ea_j^2]_N.
\]

Writing \(w_e\) for the canonical inverse of \(h_e\), both relation values
satisfy

\[
A_e=h_ew_e\equiv1\pmod N,
\qquad
B_e=u_ea_j^2w_e\equiv h_ew_e\equiv1\pmod N.
\]

Their product is

\[
A_eB_e=(u_ea_j^2h_e)w_e^2=D_ew_e^2.
\]

Consequently the relative rational square class is represented by \(D_e\),
and

\[
[D_e]=[u_e]+[h_e]
\]

because \(a_j^2\) is an exact integer square. Also

\[
D_e=u_ea_j^2h_e\equiv h_e^2\pmod N,
\]

so the supplied bridge root is exactly \(x_e=h_e\). This proves (7)--(9).
It uses the edge only after it has been declared allowed. None of these
identities proves that \(u_ea_j^2\) is present in the source or obeys its
caps.

## 3. Exact cycle square and normalized root

Let a traversal of \(C\) visit the canonical integer vertices

\[
p_0,p_1,\ldots,p_k=p_0,
\]

and let \(a_i=a_{j(e_i)}\). The unordered endpoints of \(e_i\) are
\(p_{i-1}\) and \(p_i\), regardless of traversal orientation. Hence, as an
identity of positive integers,

\[
\prod_{i=1}^kD_{e_i}
=\prod_{i=1}^k a_i^2p_{i-1}p_i
=\left(\prod_{i=1}^k a_i\prod_{i=1}^kp_{i-1}\right)^2.
\tag{A}
\]

The last equality uses equality of the two vertex multisets
\(\{p_{i-1}\}_i\) and \(\{p_i\}_i\). Thus a positive exact square root is

\[
S(C)=\prod_i a_i\prod_i p_{i-1}.
\]

The product of the supplied bridge roots is

\[
X(C)=\prod_i h_{e_i}.
\]

Normalize by supplied root divided by exact root. For a forward traversal,
\(h_{e_i}=p_i\equiv p_{i-1}a_i^2\pmod N\). For a reverse traversal,
\(h_{e_i}=p_{i-1}\). Therefore

\[
\frac{X(C)}{S(C)}
\equiv
\prod_{\epsilon_i=+1}\frac{p_i}{a_ip_{i-1}}
\prod_{\epsilon_i=-1}\frac{p_{i-1}}{a_ip_{i-1}}
\equiv
\prod_i a_i^{\epsilon_i}
=\Phi(\delta(C))\pmod N.
\tag{B}
\]

This proves the exact sign in (13). If normalized root is written with the
opposite quotient convention, (B) is inverted. After closure it is the same
residue because it is self-inverse.

Closure also gives, edge by edge,

\[
p_i\equiv p_{i-1}a_i^{2\epsilon_i}\pmod N.
\]

Multiplying and cancelling the unit
\(\prod_i p_i=\prod_i p_{i-1}\) yields

\[
1\equiv\prod_i a_i^{2\epsilon_i}
=\Phi(2\delta(C))\pmod N.
\]

Thus \(2\delta(C)\in\Lambda\), proving (12), and (B) satisfies
\(\rho(C)^2=1\).

For completeness, the same normalization follows from the original
relations rather than the bridge shorthand. The product of all selected
\(A_eB_e\) has exact root \(S(C)\prod_e w_e\) and supplied root \(1\).
Since \(\prod_e w_e\equiv X(C)^{-1}\pmod N\), its normalized root is again
\(X(C)/S(C)\).

If \(N=\prod p_i^{k_i}\) is odd and \(r^2\equiv1\pmod N\), then modulo each
odd prime power \(p_i^{k_i}\), \(r\) is \(+1\) or \(-1\). This follows since
\(p_i^{k_i}\mid(r-1)(r+1)\) and the two factors have gcd dividing \(2\).
If all local signs agree, \(r\equiv+1\) or \(r\equiv-1\pmod N\). Otherwise
\(\gcd(r-1,N)\) and \(\gcd(r+1,N)\) split the prime-power factors into two
nonempty proper groups. Hence the usual gcd decoder returns a nontrivial
factor exactly when \(r\not\equiv\pm1\pmod N\), proving (14). Reversing the
walk replaces \(\delta\) by \(-\delta\) and \(r\) by \(r^{-1}=r\).

## 4. Collision and half-relation equivalence

Because \(\delta(C)\in\Lambda_2\), for every \(z\), not only for one chosen
lift of the initial public vertex,

\[
v_{z+\delta(C)}
=[q\Phi(z)^2\Phi(\delta(C))^2]_N
=v_z.
\]

The labels and traversal signs publicly determine \(\delta(C)\), so direct
modular exponentiation computes \(r=\Phi(\delta(C))\). Equation (B) proves
that this is exactly the bridge-decoder root.

On \(\Lambda_2\), define

\[
\theta:\Lambda_2/\Lambda\longrightarrow H[2],
\qquad
\delta+\Lambda\longmapsto\Phi(\delta).
\]

It is well-defined. Its kernel is \(\Lambda\). It is surjective because if
\(h=\Phi(z)\in H\) and \(h^2=1\), then \(2z\in\Lambda\), so
\(z\in\Lambda_2\). Thus

\[
\Lambda_2/\Lambda\cong H[2].
\]

For \(\delta\in\Lambda_2\), the root is \(+1\) exactly when
\(\delta\in\Lambda\), and it is the global root \(-1\) exactly when
\(\Phi(\delta)=-1\). Therefore usefulness is equivalent to

\[
\delta\notin\Lambda,
\qquad 2\delta\in\Lambda,
\qquad \Phi(\delta)\ne-1,
\]

which is (16). In particular, \(\delta\ne0\) is insufficient because every
nonzero lattice vector in \(\Lambda\) has root \(+1\).

A commutation diamond has signed displacement

\[
e_i+e_j-e_i-e_j=0.
\]

Its bridge product is an exact square by (A), and its normalized root is
exactly \(+1\) by (B). Exact-value deletion can erase all of its relation
occurrences, or leave a nonzero dependency, but Section 6 below shows that
either result retains root \(+1\). The root map is multiplicative under
symmetric difference of cycles, so any span of such diamonds also has root
\(+1\). Large nullity created by commutativity is therefore not evidence of
a factor signal.

## 5. Root image of the complete Cayley graph

Assume every positive edge from every public vertex is allowed. A formal
cycle has displacement in \(\Lambda_2\), so Sections 3--4 show that every
cycle root lies in \(H[2]\).

Conversely, take \(r\in H[2]\). Choose \(\delta\in\mathbb Z^m\) with
\(\Phi(\delta)=r\). Then \(\Phi(2\delta)=1\), hence
\(\delta\in\Lambda_2\). Express \(\delta\) as a signed generator word.
Starting at any public vertex, a positive letter traverses the corresponding
stored edge forward. A negative letter traverses backward the positive edge
whose head is the current vertex. Completeness supplies every such edge. The
endpoint is the start because \(\delta\in\Lambda_2\).

This closed walk can repeat logical edges. Formulae (A)--(B), with edge
occurrences counted with multiplicity, give it normalized root
\(\Phi(\delta)=r\). Reduce the number of occurrences of each *same logical
edge* modulo two. Removing two copies of \(e\) removes \(D_e^2\), whose
positive exact root is \(D_e\), and supplied root
\(x_e^2\equiv D_e\pmod N\). The removed pair has normalized root \(+1\).
The remaining edge set still has even incidence at every vertex, so it is
an element of \(\ker\partial\), possibly a disjoint union of edge-distinct
closed trails, and it has the same root \(r\). This proves

\[
\operatorname{im}(\text{formal cycle root map})=H[2].
\]

The same pair-removal argument proves that the root map from the binary
cycle space to \(H[2]\) is a homomorphism. It also closes the small gap that
would result from treating an arbitrary repeated closed walk as though it
were already a binary cycle.

For one generator \(a\) of order \(d\),

\[
\Lambda=d\mathbb Z,
\qquad
\Lambda_2=\{t:d\mid2t\}.
\]

When \(d\) is even, the least positive representative of the nonzero class
is \(d/2\), and its root is \(a^{d/2}\). This is useful precisely when that
involution is not global. Its size can be exponential in the bit length.
For an explicit family, let \(N=3^k5^k\) and choose \(a\) by CRT so that
\(a\equiv2\pmod{3^k}\) and \(a\equiv1\pmod{5^k}\). The order of \(2\) modulo
\(3^k\) is \(2\cdot3^{k-1}\), so \(d=2\cdot3^{k-1}\). At exponent \(d/2\),
the component modulo \(3^k\) is \(-1\) and the component modulo \(5^k\) is
\(+1\). The root is useful, while

\[
d/2=3^{k-1}=\exp(\Theta(\log N)).
\]

Thus equality of root images is purely structural and gives no
quasipolynomial bound on a representing walk.

## 6. Exact-value deduplication and the arithmetic kernel

For a logical cycle, restore its actual \(A_e\) and \(B_e\) occurrences.
Every such exact relation value \(R\) is congruent to \(1\pmod N\) and has
supplied root \(1\). Two equal occurrences contribute \(R^2\), whose
positive exact root is \(R\). Their normalized root is therefore \(+1\).
Deleting equal actual relation values in pairs and retaining one
representative for an odd multiplicity preserves the cycle root exactly.

The qualification “actual relation values” is necessary. If two proof
coordinates have the same bridge integer \(D_e=D_f=R\) but supplied roots
\(x_e\ne x_f\), their pair has normalized root

\[
x_ex_fR^{-1}\pmod N,
\]

which is not forced to be \(+1\). Equality of bridge integers is therefore
not a valid deduplication key. Deduplication by the original \(A,B\) values
is valid because their supplied roots and residues are both fixed at \(1\).

For the kernel comparison, the unoriented endpoint incidence column of an
edge is

\[
\partial e=[u_e]_{\mathrm{formal}}+[h_e]_{\mathrm{formal}}.
\]

Applying \(J\) gives

\[
J\partial e=[u_e]+[h_e]=[D_e]
\]

in positive rational square classes. Thus the true bridge parity map is
exactly \(J\partial\), and

\[
\ker\partial\subseteq\ker(J\partial).
\]

The inclusion can be strict, even in a way that survives exact-value
deduplication and gives a useful root. For example, take

\[
N=15,\qquad q=2,\qquad a=7,
\]

and consider the edge from \(u=2\) to
\(h=[2\cdot7^2]_{15}=8\), if that edge is declared allowed. Its formal
boundary is the nonzero vector
\([2]_{\rm formal}+[8]_{\rm formal}\), while

\[
D=2\cdot7^2\cdot8=784=28^2.
\]

Hence it lies in \(\ker(J\partial)\setminus\ker\partial\). With
\(w=8^{-1}\bmod15=2\), the actual relation values are

\[
A=16,\qquad B=196,
\]

so they are not exact duplicates. The supplied bridge root is \(8\), and
the normalized root is

\[
8/28\equiv11\pmod{15},
\]

a non-global square root of \(1\). This example proves only the algebraic
possibility. It does not assert that the frozen source contains this edge.
It also demonstrates why formal endpoint cycles do not exhaust the
arithmetic kernel.

## 7. Fixed-star carry isolation

Because \(q<N\) and \(c_\ell\) is the least positive residue of
\(q\ell^2\), Euclidean division gives

\[
c_\ell=q\ell^2-t_\ell N,
\qquad 0\le t_\ell<\ell^2.
\]

For distinct prime anchors \(\ell,m\), direct elimination of \(q\) gives

\[
m^2c_\ell-\ell^2c_m
=N(\ell^2t_m-m^2t_\ell)
=N\Delta_{\ell,m}.
\tag{C}
\]

Any common divisor of \(c_\ell,c_m\) is coprime to \(N\), since each
\(c_\ell\) represents the unit \(q\ell^2\pmod N\). Equation (C) therefore
implies

\[
\gcd(c_\ell,c_m)\mid\Delta_{\ell,m}.
\]

Moreover both nonnegative terms in \(\Delta\) are strictly below
\(\ell^2m^2\), so

\[
|\Delta_{\ell,m}|<\ell^2m^2\le A^4.
\]

If \(\Delta=0\), then \(\ell^2t_m=m^2t_\ell\). Since the distinct primes
have coprime squares, \(\ell^2\mid t_\ell\) and \(m^2\mid t_m\). The strict
quotient bounds force \(t_\ell=t_m=0\). Then \(c_\ell=q\ell^2\) and

\[
D_\ell=q\ell^2c_\ell=c_\ell^2,
\]

with supplied root \(c_\ell\), so the normalized root is \(+1\). The same
conclusion holds for every individual unwrapped anchor, whether or not it
is paired with another one.

For a wrapped anchor,

\[
\gcd(q,c_\ell)
=\gcd(q,q\ell^2-t_\ell N)
=\gcd(q,t_\ell N)
=\gcd(q,t_\ell),
\]

where the last equality uses \(\gcd(q,N)=1\). Thus a prime shared by \(q\)
and \(c_\ell\) is strictly below \(A^2\).

Define

\[
r_\ell=\frac{c_\ell}
{\prod_{p\le A^4}p^{v_p(c_\ell)}}
\]

for each wrapped anchor. Every prime divisor of \(r_\ell\) exceeds \(A^4\).
Such a prime cannot divide \(q\) by the preceding gcd identity. If it also
divided \(r_m\), then \(\Delta_{\ell,m}\ne0\) because both anchors are
wrapped, and it would divide a nonzero integer of absolute value below
\(A^4\), an impossibility. Hence

\[
\gcd(r_\ell,q)=1,
\qquad
\gcd(r_\ell,r_m)=1\quad(\ell\ne m).
\]

Now take an exact square dependency of fixed-star bridges. Discard every
selected unwrapped bridge because it is already an exact square. For the
remaining selected wrapped set \(S\),

\[
\prod_{\ell\in S}D_\ell
=q^{|S|}\left(\prod_{\ell\in S}\ell\right)^2
 \prod_{\ell\in S}c_\ell.
\tag{D}
\]

If \(p\mid r_\ell\), then \(p>A^4\), \(p\nmid q\), and \(p\nmid c_m\) for
every other selected wrapped anchor \(m\). Its contribution from the anchor
squares in (D) is even. Therefore the parity of its valuation in (D) is
exactly the parity of \(v_p(r_\ell)\). Since (D) is an exact square, every
such valuation is even. Thus each selected \(r_\ell\) is itself an integer
square.

This is only necessary. It says nothing about parity at primes at most
\(A^4\), about the common \(q\)-class, or about arbitrary older relation
columns. Those can still decide whether a dependency exists.

Let \(n=\Theta(\log N)\) and
\(A=\exp((\log n)^{O(1)})\). There are at most \(A\) anchors. Naive trial
division of every \(n\)-bit \(c_\ell\) by all integers through \(A^4\) costs
at most

\[
A\cdot A^4\cdot\operatorname{poly}(n)
=\exp((\log n)^{O(1)}),
\]

and exact integer-square testing is polynomial in the bit length. The
fixed-star necessary condition is therefore publicly decidable in
quasipolynomial time. Pairwise coprimality proves that no prime above the
factor-base bound can be a shared hidden cofactor among wrapped endpoints.

## 8. Scope and quasipolynomial consequence

Given an explicit allowed graph with
\(\exp((\log n)^{O(1)})\) vertices and edges, standard binary linear algebra
computes a cycle basis in quasipolynomial time. For each basis cycle, signed
label multiplication computes (13), followed by the two gcd tests. Because
the normalized-root map is a homomorphism, if every basis root is global
then every cycle root is global. If a useful cycle exists, some basis root
is useful. Thus the decoder is affordable once the legal graph has been
supplied.

Nothing in the statement proves that the frozen source supplies any desired
edge, that a complete Cayley graph is available, that a non-global class in
\(\Lambda_2/\Lambda\) has a short representative, or that such a
representative can be found. A formal useful cycle is exactly a visible
collision of \(z\mapsto v_z\) with a non-global half-relation root. The
one-generator family above shows why this representative can be
exponentially long.

The only remaining channel identified here is
\(\ker(J\partial)\setminus\ker\partial\). Section 7 restricts its
bridge-only part inside one fixed prime-anchor star, but does not cover old
columns and gives no sufficiency theorem. Therefore the final disjunction
is exact: progress requires either a short findable non-global half-relation
inside the legal source, or a genuinely arithmetic dependency outside the
formal endpoint cycle space. The statement proves neither existence claim
and does not imply quasipolynomial-time factorization.

The statement-only constraint does not permit an independent audit of the
contents or priority of the named earlier results P71, F141, and F142. The
derivation above does independently establish the mathematical substance of
the comparison: the formal-cycle target is exactly a half-relation in
\(\Lambda_2/\Lambda\), while the larger arithmetic kernel is not closed.
Likewise, the claim that this is a proof-only boundary is correct as a scope
claim; it is not evidence that any required frozen-source position exists.
