# Proof of the F152 decorated-squareclass theorem

## 1. The group law

For bit vectors \(v,w\), exact integer multiplication gives

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2.
\tag{9}
\]

All \(q_j\) are units modulo \(N\), so (1) is defined. If
\(z^2=Q(v)\) and \(t^2=Q(w)\), then (9) shows that the second coordinate
of their product squares to \(Q(v+w)\). Thus the set is closed.

For bits \(a,b,c\in\{0,1\}\), with addition in \(\mathbf F_2\),

\[
ab+(a+b)c=bc+a(b+c)
\]

as integer exponents after writing XOR as \(x+y-2xy\). Coordinatewise, this
gives the cocycle identity

\[
C(u,v)C(u+v,w)=C(v,w)C(u,v+w).
\]

Hence (1) is associative. Symmetry of \(C\) gives commutativity. The identity
is \((0,1)\). Since \(C(v,v)=Q(v)\),

\[
(v,z)\star(v,z)=(0,z^2Q(v)^{-1})=(0,1).
\]

Every element is its own inverse. Closure also shows that \(V_Q(N)\) is a
subspace. The kernel of the projection consists exactly of the pairs
\((0,r)\) with \(r^2=1\), which proves (2).

If \(r^2=1\pmod N\) but \(r\ne\pm1\pmod N\), neither sign can have gcd \(N\),
and the product \((r-1)(r+1)\) is divisible by \(N\). At least one sign has a
nontrivial gcd, and any nontrivial sign gcd is proper. This proves (3).

## 2. Relation lifts and the normalized root

Equation (4) gives

\[
(\alpha_i s_i^{-1})^2\equiv Q(v_i)\pmod N,
\]

so (5) lies in \(E_Q(N)\).

Fix \(c\in\ker A\). Write

\[
d_j=\sum_i c_i(v_i)_j.
\]

Every \(d_j\) is even. The exact positive root of the selected integer
product is

\[
R(c)=\left(\prod_i s_i^{c_i}\right)
      \left(\prod_jq_j^{d_j/2}\right).
\tag{10}
\]

The repeated use of (1) divides the product of second coordinates by exactly
\(\prod_jq_j^{d_j/2}\). Therefore the second coordinate of \(G(c)\) is

\[
\frac{\prod_i\alpha_i^{c_i}}{R(c)}.
\tag{11}
\]

Its square is one. A square root of one is its own inverse, so (11) is also
\(R(c)/(\prod_i\alpha_i^{c_i})\), the P66 normalized root. This proves the
exact decoder identification.

## 3. Split or section

Assume first that every element of \(G(\ker A)\) lies in \(\Delta\). Define

\[
h(Ac)=\overline{G(c)}.
\]

If \(Ac=Ac'\), then \(c+c'\in\ker A\), so
\(G(c)G(c')\in\Delta\). Hence the two quotient classes agree and \(h\) is
well-defined. It is a homomorphism because \(G\) is one. Its projection is
\(Ac\), and it sends every \(v_i\) to \(\overline g_i\). Since the \(v_i\)
span \(W\), these values make \(h\) unique.

Conversely, if such an \(h\) exists, then for every \(c\in\ker A\),
\(\overline{G(c)}=h(0)\) is the identity. Thus \(G(c)\in\Delta\). Therefore
failure of (6) is exactly the existence of a non-global normalized root, and
(3) factors \(N\).

The online algorithm is Gaussian elimination on the \(v_i\). When a new
vector is dependent, the stored basis expression gives a comparison lift.
Their group quotient has parity coordinate zero. Equality up to global sign
is a direct modular comparison. Otherwise (3) applies. All group operations,
comparisons, gcds, and elimination steps are polynomial in the explicit
input length.

Finally, (2) is a short exact sequence of finite-dimensional vector spaces
over a field. Choose a basis of \(V_Q(N)\), choose any lift of each basis
vector, and extend linearly. This proves that an abstract full section always
exists. It need not be computable from bare \(N\) without supplied lifts, but
its existence blocks any contradiction based only on parity-space structure.

## 4. Two layers

For a pure layer whose normalized-root image is global, Section 3 gives a
section on its parity span. Let \(u\in W_F\cap W_A\), and choose coefficient
vectors \(c_F,c_A\) that represent \(u\) in the two layers. Their union is a
parity dependency. Its decorated product modulo \(\Delta\) is

\[
h_F(u)h_A(u).
\]

Changing either representation multiplies the corresponding lift by a pure
kernel element, which is global and disappears in the quotient. Thus (7) is
well-defined. It is a homomorphism. Every cross dependency gives one such
intersection vector, and every intersection vector gives a cross dependency.
Therefore its image is exactly the induced cross normalized-root image from
P108.

When two objects have the same parity vector, their product has parity zero.
For \(T_i=d s_i^2\) and \(T_j=d s_j^2\), formula (1) divides their two lift
coordinates by \(d\), giving

\[
\frac{\alpha_i\alpha_j}{d s_i s_j}.
\]

Using \(\alpha_i^2\equiv ds_i^2\) and
\(\alpha_j^2\equiv ds_j^2\) converts this to either cross-ratio form in (8).
This is exactly P134.

## 5. Finite illustration

The displayed integer factorizations are direct. Their product is

\[
T_1T_2=(3\cdot43\cdot842)^2.
\]

Also \(108618\equiv471\pmod{2773}\), and

\[
471^2-1=47\cdot59\cdot80.
\]

Thus the two gcds are \(47\) and \(59\), as stated.

## 6. Scope

This proof constructs no relation source. It does not show that a canonical
inverse, feedback, torus, or high-order family violates a common section. It
does not turn algorithmic PFR into a factoring algorithm. It isolates the
additional datum that any such source theorem must control: the decorated
lift, not only its parity projection.

