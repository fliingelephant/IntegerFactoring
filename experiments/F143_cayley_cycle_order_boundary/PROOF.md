# F143 proof — exact displacement and root of a Cayley bridge cycle

## 1. Vertex equality and legal edges

Let

\[
\Phi(z)=\prod_j a_j^{z_j},
\qquad
v_z=[q\Phi(z)^2]_N.
\]

Here \(1\le q<N\), as in the statement.  All displayed elements are units.
Therefore

\[
v_z=v_{z'}
\quad\Longleftrightarrow\quad
q\Phi(z)^2\equiv q\Phi(z')^2\pmod N
\]

is equivalent to

\[
\Phi(2(z-z'))=1.
\]

This is exactly \(2(z-z')\in\Lambda\), which proves (3).

For a positive step \(z\to z+e_j\),

\[
v_za_j^2
\equiv q\Phi(z)^2a_j^2
=q\Phi(z+e_j)^2
\equiv v_{z+e_j}\pmod N.
\]

Thus the canonical reduction of the raw word \(U_e=v_za_j^2\) is the
declared head \(h_e=v_{z+e_j}\).  If this raw word is a legal F141 position,
F141 gives

\[
A_e=h_ew_e,
\qquad
B_e=v_za_j^2w_e.
\]

Their product is

\[
A_eB_e
=v_za_j^2h_ew_e^2
=D_ew_e^2.
\]

Hence the bridge square class is \([v_z]+[h_e]\), and
\(D_e\equiv h_e^2\pmod N\) supplies the root \(h_e\).

## 2. Exact square on a closed trail

Traverse an edge-distinct closed trail as

\[
x_0\xrightarrow{e_1}x_1
\xrightarrow{e_2}\cdots
\xrightarrow{e_k}x_k=x_0.
\]

Every traversed edge \(e_t\) has unordered endpoint product
\(x_{t-1}x_t\), irrespective of its stored orientation.  Therefore

\[
\prod_{t=1}^kD_{e_t}
=
\left(\prod_{t=1}^kx_t\right)^2
\left(\prod_{t=1}^ka_{j(e_t)}\right)^2.
\tag{1}
\]

The exact positive root is

\[
R_C=
\left(\prod_{t=1}^kx_t\right)
\left(\prod_{t=1}^ka_{j(e_t)}\right).
\tag{2}
\]

The supplied root product is

\[
X_C=\prod_{t=1}^k h_{e_t},
\tag{3}
\]

where \(h_{e_t}\) is the head in the stored positive orientation.

For one traversed edge, compare its arrival vertex \(x_t\) with its stored
head.

- If traversal agrees with the stored orientation, then
  \(x_t=h_{e_t}\).  Its contribution to \(R_CX_C^{-1}\) is
  \(a_{j(e_t)}\).
- If traversal opposes the stored orientation, then \(x_t=u_{e_t}\), while
  \(h_{e_t}\equiv u_{e_t}a_{j(e_t)}^2\pmod N\).  Its contribution is
  \(a_{j(e_t)}u_{e_t}h_{e_t}^{-1}\equiv a_{j(e_t)}^{-1}\).

Multiplying these contributions proves

\[
R_CX_C^{-1}
\equiv
\prod_{e\in C}a_{j(e)}^{\epsilon_e}
=\Phi(\delta(C))\pmod N.
\tag{4}
\]

This is (13).

## 3. Closure is a half-relation

Lift the traversal to exponent labels.  An agreeing edge adds \(e_j\), and
an opposing edge subtracts \(e_j\).  The lifted endpoint is therefore
\(z+\delta(C)\).  The projected public walk is closed, so

\[
v_z=v_{z+\delta(C)}.
\]

Section 1 gives \(2\delta(C)\in\Lambda\).  Hence

\[
\rho(C)^2
=\Phi(2\delta(C))
=1.
\]

For odd \(N\), a square root of one yields a proper gcd exactly when it is
not one of the two global roots \(+1,-1\).  This proves (12), (14), and the
direct-collision equivalence.

If \(\delta(C)=0\), equation (4) gives \(\rho(C)=1\).  The four signed steps
in a commutation diamond are

\[
e_i+e_j-e_i-e_j=0,
\]

so every such diamond is root-trivial.  More generally,
\(\delta(C)\in\Lambda\) also gives root \(+1\), even when the integer
displacement is nonzero.  If vertex or exact-value coincidences make a
diamond degenerate, Section 5 removes duplicate logical occurrences in
pairs.  It can reduce the diamond to the zero dependency, but cannot change
its root to a useful one.

## 4. Exact image of the complete graph

Put \(H=\Phi(\mathbb Z^m)\).  The map

\[
\Lambda_2/\Lambda\longrightarrow H[2],
\qquad
\delta+\Lambda\longmapsto\Phi(\delta)
\tag{5}
\]

is well-defined.  Its kernel is \(\Lambda\).  It is surjective because every
\(r\in H[2]\) has a preimage \(\delta\in\mathbb Z^m\), and
\(r^2=1\) implies \(2\delta\in\Lambda\).  Thus (5) is an isomorphism.

Assume every positive edge is allowed.  Any \(\delta\in\Lambda_2\) has a
signed generator word.  Starting from any exponent label and following this
word gives a closed walk in the public vertex graph.  Section 2 assigns it
the root \(\Phi(\delta)\).  Conversely, Section 3 assigns every closed walk
a displacement in \(\Lambda_2\).  Therefore the formal-cycle root image is
exactly \(H[2]\).

A closed walk can repeat edges.  Delete repeated occurrences in pairs.
The square of one bridge has exact root \(D_e\) and supplied root \(h_e^2\),
so its normalized contribution is

\[
D_eh_e^{-2}\equiv1\pmod N.
\]

Thus reducing a walk to its binary edge support does not change its
normalized root.  The same argument permits decomposition into edge-disjoint
cycles.

## 5. Global exact-value deletion

The actual source contains canonical and lifted relation values, each
congruent to one modulo \(N\) and each with supplied root one.  A bridge
selection is shorthand for selecting its matched pair \(A_e,B_e\).

Restore all logical occurrences used by a formal cycle.  If two selected
occurrences have the same exact integer value \(T\), their product is
\(T^2\).  Removing the pair removes exact root \(T\) and supplied root one.
Since \(T\equiv1\pmod N\), this changes the normalized root by \(+1\).
Repeated deletion leaves at most one occurrence of each exact integer and
preserves (4).  The globally retained representative of each odd class is
therefore sufficient.

This argument occurs before the bridge column change.  It does not license
deduplication of two conceptual bridge values that have different supplied
roots.

## 6. Formal graph kernel versus arithmetic kernel

Let \(\mathbb F_2^V\) have one formal coordinate for each distinct public
integer vertex.  The endpoint incidence map sends an edge to

\[
\partial e=e_{u_e}+e_{h_e}.
\]

Let \(J\) send each formal coordinate to the exact rational square class of
that positive integer.  By (9), the true bridge parity column is
\(J\partial e\).  Therefore every formal cycle is an arithmetic dependency:

\[
\ker\partial\subseteq\ker(J\partial).
\]

The reverse inclusion need not hold.  Two different vertex integers can
share rational-prime factors, and several composite endpoint vectors can
cancel without even formal endpoint incidence.  Such a dependency is an
arithmetic hypercycle, not a Cayley graph cycle.  None of the displacement
arguments above characterizes that extra kernel.

## 7. Fixed-star carry isolation

For one fixed \(q\), write

\[
c_\ell=q\ell^2-t_\ell N,
\qquad
c_m=qm^2-t_mN.
\]

Cross-multiplication cancels the common raw product:

\[
m^2c_\ell-\ell^2c_m
=N(\ell^2t_m-m^2t_\ell)
=N\Delta_{\ell,m}.
\tag{6}
\]

Let \(g=\gcd(c_\ell,c_m)\).  Both endpoints are units modulo \(N\), so
\(\gcd(g,N)=1\).  Since \(g\) divides the left-hand side of (6), it divides
\(N\Delta_{\ell,m}\), and coprimality with \(N\) gives

\[
g\mid\Delta_{\ell,m}.
\tag{7}
\]

Because \(0\le t_\ell<\ell^2\) and \(0\le t_m<m^2\), both
\(\ell^2t_m\) and \(m^2t_\ell\) lie in
\([0,\ell^2m^2)\).  If their difference is nonzero, then

\[
0<|\Delta_{\ell,m}|<\ell^2m^2\le A^4.
\tag{8}
\]

If \(\Delta_{\ell,m}=0\), then
\(\ell^2t_m=m^2t_\ell\).  The anchors are distinct primes, so their squares
are coprime.  Reducing this equality modulo \(\ell^2\) gives
\(\ell^2\mid t_\ell\).  The bound \(0\le t_\ell<\ell^2\) forces
\(t_\ell=0\).  Symmetrically, \(t_m=0\).  Then
\(c_\ell=q\ell^2\), and its bridge satisfies

\[
D_\ell=q\ell^2c_\ell=c_\ell^2.
\]

Its exact and supplied roots are both \(c_\ell\), so its normalized root is
\(+1\).

For one wrapped endpoint,

\[
\gcd(q,c_\ell)
=\gcd(q,q\ell^2-t_\ell N)
=\gcd(q,t_\ell N)
=\gcd(q,t_\ell),
\tag{9}
\]

because \(q\) is a unit modulo \(N\).  Every prime in this gcd is below
\(\ell^2\le A^2\).

Let \(r_\ell\) be the result of removing from \(c_\ell\) all prime powers
whose primes are at most \(A^4\).  Any prime common to two distinct
\(r_\ell,r_m\) would exceed \(A^4\), contradicting (7)--(8).  The zero
difference case cannot occur for wrapped anchors.  Equation (9) likewise
shows that no prime of \(r_\ell\) divides \(q\).  This proves (27).

Now select a fixed-star bridge \(D_\ell=q\ell^2c_\ell\).  Every prime in
\(r_\ell\) occurs in no other selected endpoint, does not occur in \(q\),
and occurs to even exponent in the anchor square \(\ell^2\).  If the total
bridge product is an exact square, each valuation in \(r_\ell\) must
therefore be even.  Hence every selected \(r_\ell\) is an integer square.

If \(A=\exp((\log n)^{O(1)})\), trial division by all integers through
\(A^4\), repeated exact division, and an integer square test cost
\(\exp((\log n)^{O(1)})\operatorname{poly}(n)\).  No factorization of
\(N\) is used.

This argument concerns dependencies made only from the fixed-star bridges.
An old relation can contain a large prime from \(r_\ell\) and cancel its
private row.  The theorem does not control that full relative kernel.

## 8. Relation to P71 and quasipolynomial work

For \(m=1\), a nontrivial closed displacement is an integer \(d\) with
\(a^{2d}=1\pmod N\).  Its root is \(a^d\).  The least useful such \(d\) is
the half-order target in P71.  The multi-generator equations are the same
statement for the relation lattice \(\Lambda\).

If an allowed graph has quasipolynomial size, standard graph linear algebra
and the direct root tests are also quasipolynomial.  The proof supplies no
bound on the size or density of a displacement in
\(\Lambda_2\setminus\Lambda\), and no source theorem that makes the needed
edges legal.  The quasipolynomial runtime allowance therefore does not by
itself cross the existence boundary.
