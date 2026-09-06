# F143 candidate statement — Cayley bridge cycles are a bounded half-relation problem

## Status and scope

This is a proof-only boundary for one possible continuation of F141 and
F142.  It does not change the F141 source.  It does not prove that the
required source positions exist, that a useful cycle occurs, or that \(N\)
can be factored in quasipolynomial time.

The main theorem studies only **formal endpoint cycles** among
squared-anchor bridges.  The full arithmetic square-class kernel can be
larger.  Section 7 gives one exact restriction on that larger channel for a
single fixed star, but does not close it.

The closest general result is P71.  P71 identifies self-inverse selections
with half-relations in a hidden exponent lattice.  F143 gives the exact
specialization to the F141 bridge graph: it computes every cycle root,
shows that the automatic commutation cycles are global decoys, and proves
that a useful formal cycle is already a directly visible square collision.
It is not an independent escape from P71.

## 1. Public squared-action vertices

Let \(N\ge3\) be odd.  Let \(1\le q<N\), and let
\(q,a_1,\ldots,a_m\) be positive units modulo \(N\).  Define

\[
\Phi:\mathbb Z^m\longrightarrow (\mathbb Z/N\mathbb Z)^\times,
\qquad
\Phi(z)=\prod_{j=1}^m a_j^{z_j},
\]

and let

\[
\Lambda=\ker\Phi,
\qquad
\Lambda_2=\{\delta\in\mathbb Z^m:2\delta\in\Lambda\}.
\tag{1}
\]

Negative exponents in this definition mean modular inverses.  They do not
assert that the F141 word grammar accepts negative integer exponents.

For each exponent label \(z\), define the public canonical vertex

\[
v_z=[q\Phi(z)^2]_N\in\{1,\ldots,N-1\}.
\tag{2}
\]

Then

\[
\boxed{v_z=v_{z'}\quad\Longleftrightarrow\quad z-z'\in\Lambda_2.}
\tag{3}
\]

Thus the distinct public vertices form the quotient

\[
\mathbb Z^m/\Lambda_2\cong \Phi(\mathbb Z^m)^2.
\tag{4}
\]

## 2. Legal F141 edges and bridges

For a positive generator step \(z\to z+e_j\), put

\[
u_e=v_z,
\qquad
h_e=v_{z+e_j}=[u_ea_j^2]_N,
\qquad
w_e=\iota_N(h_e).
\tag{5}
\]

Call this edge **allowed** only if the current frozen source legally contains
the F141 word

\[
U_e=u_ea_j^2.
\tag{6}
\]

In particular, (2) alone does not make \(u_e\) a named block and does not
prove that (6) is inside the source support and exponent caps.

For an allowed edge, the canonical and lifted relations are

\[
A_e=h_ew_e,
\qquad
B_e=u_ea_j^2w_e.
\tag{7}
\]

Relative to the retained canonical relation, the F141 bridge is

\[
D_e=u_ea_j^2h_e,
\qquad
D_e\equiv h_e^2\pmod N.
\tag{8}
\]

Its exact square class and supplied modular root are

\[
[D_e]=[u_e]+[h_e],
\qquad
x_e=h_e.
\tag{9}
\]

The stored orientation of \(e\) is from \(u_e\) to \(h_e\), and its public
label is \(a_j\).

## 3. Exact cycle-root theorem

Let \(C\) be an edge-distinct closed trail of allowed edges.  Choose a
traversal orientation.  For each traversed edge \(e\), let

\[
\epsilon_e=
\begin{cases}
+1,&\text{if traversal agrees with the stored orientation},\\
-1,&\text{if traversal opposes the stored orientation}.
\end{cases}
\tag{10}
\]

If \(e\) has generator label \(a_{j(e)}\), define its exponent displacement

\[
\delta(C)=\sum_{e\in C}\epsilon_e e_{j(e)}\in\mathbb Z^m.
\tag{11}
\]

Closure of the public vertex walk gives

\[
\boxed{2\delta(C)\in\Lambda.}
\tag{12}
\]

The bridge product is an exact integer square.  Its P66 normalized root is

\[
\boxed{
\rho(C)
=\prod_{e\in C}a_{j(e)}^{\epsilon_e}
=\Phi(\delta(C))
\pmod N.
}
\tag{13}
\]

Consequently, \(\rho(C)^2\equiv1\pmod N\).  The cycle factors \(N\) exactly
when

\[
\Phi(\delta(C))\not\equiv\pm1\pmod N.
\tag{14}
\]

The sign convention in (10) is immaterial after closure: the reverse
traversal gives the inverse root, and every root in (13) is self-inverse.

## 4. Formal cycles give no mechanism beyond a square collision

The cycle itself supplies the public collision

\[
v_z=v_{z+\delta(C)}.
\tag{15}
\]

Given the cycle labels, one can compute

\[
r=\Phi(\delta(C))\pmod N
\]

directly and test \(\gcd(r-1,N)\) and \(\gcd(r+1,N)\).  Equations (12)--(13)
show that this direct collision screen returns exactly the same root as the
bridge decoder.

Therefore a formal Cayley-cycle organization does not manufacture a new
factor signal.  It repackages a bounded half-relation:

\[
\boxed{
\delta\notin\Lambda,
\qquad
2\delta\in\Lambda,
\qquad
\Phi(\delta)\not\equiv-1\pmod N.
}
\tag{16}
\]

Equivalently, the useful target is a class of

\[
\Lambda_2/\Lambda
\cong
\Phi(\mathbb Z^m)[2]
\tag{17}
\]

outside the two global roots.  The condition \(\delta\ne0\) alone is much
too weak: every nonzero \(\delta\in\Lambda\) still gives root \(+1\).

Any formal exponent-lattice cycle with \(\delta(C)=0\) has normalized root
exactly \(+1\).  In particular, every available commutation diamond

\[
z\to z+e_i\to z+e_i+e_j
\to z+e_j\to z
\tag{18}
\]

has a logical bridge product that is an exact square with root \(+1\).
After exact-value deletion, a degenerate diamond can collapse to the zero
dependency.  If its four edge columns survive as a nonzero cycle, it is an
exact root-\(+1\) dependency.  Nondegenerate collections of these automatic
diamonds can create large nullity without creating a factor.

## 5. Complete Cayley graph image

Suppose, only for this paragraph, that every positive generator edge at
every public vertex is allowed.  Then the normalized-root image of the
formal graph cycle space is exactly

\[
\boxed{\Phi(\mathbb Z^m)[2].}
\tag{19}
\]

Indeed, every closed walk has displacement in \(\Lambda_2\), so its root is
in the right-hand side.  Conversely, if \(r=\Phi(\delta)\) and \(r^2=1\),
then \(\delta\in\Lambda_2\).  Any signed generator word for \(\delta\)
projects to a closed walk whose normalized root is \(r\).

This is an equality of root images, not an efficient construction of a
useful walk.  In the one-generator case, the least useful displacement is
the usual half-order problem from P71.  It can be exponentially large in
\(n=\Theta(\log N)\).

## 6. Deduplication and the true arithmetic kernel

The bridge \(D_e\) is a proof coordinate.  Exact-value deletion must be
applied to the actual canonical and lifted relation values \(A_e,B_e\),
not to equal bridge integers with possibly different supplied roots.

Global exact-value deletion does not change (13).  Restore the logical
occurrences \(A_e,B_e\) used by the cycle, group equal exact relation values,
and remove them in pairs.  Each removed pair has exact root equal to that
relation value, which is \(1\pmod N\), and has supplied root \(1\).  It has
normalized root \(+1\).  One retained representative of every odd class
therefore realizes the same cycle root.

Let \(\partial:\mathbb F_2^E\to\mathbb F_2^V\) be the formal endpoint
incidence map, and let

\[
J:\mathbb F_2^V
\longrightarrow
\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2
\]

send a formal vertex label to its true rational square class.  The actual
bridge parity matrix is \(J\partial\).  Hence

\[
\boxed{\ker\partial\subseteq\ker(J\partial),}
\tag{20}
\]

and the inclusion can be strict.  F143 describes \(\ker\partial\), the
formal graph cycles.  It does not describe arithmetic hypercycles in
\(\ker(J\partial)\setminus\ker\partial\), where different endpoint integers
can cancel through shared rational-prime rows.  Those hypercycles remain a
genuine possible continuation of F141.

## 7. Fixed-star carry isolation

There is a separate exact restriction on bridge-only hypercycles inside one
fixed-\(q\) squared-anchor star.  Let \(\mathcal L\) be distinct rational
prime anchors \(\ell\le A\), all coprime to \(Nq\), and write

\[
c_\ell=[q\ell^2]_N=q\ell^2-t_\ell N,
\qquad
0\le t_\ell<\ell^2.
\tag{21}
\]

For distinct \(\ell,m\in\mathcal L\), put

\[
\Delta_{\ell,m}
=\ell^2t_m-m^2t_\ell.
\tag{22}
\]

Then

\[
\boxed{
\gcd(c_\ell,c_m)\mid\Delta_{\ell,m},
\qquad
|\Delta_{\ell,m}|<\ell^2m^2\le A^4,
}
\tag{23}
\]

unless \(\Delta_{\ell,m}=0\).  In the zero case,

\[
t_\ell=t_m=0,
\qquad
c_\ell=q\ell^2,
\qquad
c_m=qm^2.
\tag{24}
\]

Each corresponding bridge is already the exact square

\[
D_\ell=q\ell^2c_\ell=c_\ell^2
\tag{25}
\]

with supplied root \(c_\ell\), so its normalized root is \(+1\).

For a wrapped anchor \(t_\ell>0\),

\[
\boxed{\gcd(q,c_\ell)=\gcd(q,t_\ell),}
\tag{26}
\]

so every prime shared by \(q\) and \(c_\ell\) is below \(A^2\).

Remove all prime powers at primes at most \(A^4\) from every wrapped
\(c_\ell\), and call the remaining integer \(r_\ell\).  Equations
(23) and (26) give

\[
\gcd(r_\ell,q)=1,
\qquad
\gcd(r_\ell,r_m)=1
\quad(\ell\ne m).
\tag{27}
\]

Therefore, in any exact square dependency made only from the fixed-star
bridges \(D_\ell=q\ell^2c_\ell\), every selected residual
\(r_\ell\) must itself be an integer square.  Otherwise an odd valuation at
a prime above \(A^4\) is private to that bridge column.

This condition is necessary, not sufficient.  The remaining \(q\)-class and
the rows at primes at most \(A^4\) still have to cancel.  It also does not
cover cancellation against arbitrary old columns in the full F142 relative
kernel.

If the numerical anchor cap satisfies

\[
A=\exp((\log n)^{O(1)}),
\]

trial division through \(A^4\) and exact square testing evaluate this
necessary condition in quasipolynomial time.  Thus a fixed star cannot hide
its bridge-only arithmetic closure in an uncontrolled large shared cofactor:
after a public quasipolynomial factor-base removal, every selected endpoint
must have a square residual.

## Exact consequence for the quasipolynomial target

An explicit quasipolynomial-size allowed graph can be built and its cycle
basis can be tested in quasipolynomial time.  This only makes the decoder
affordable.  It does not force a useful root.

The automatic cycles caused by commutativity have root \(+1\).  Every useful
formal cycle is already a useful collision of the public squared-action map
\(z\mapsto v_z\), which is the bounded hidden-lattice target of P71.  Thus a
new continuation must do at least one of the following:

1. prove that a non-global half-relation has a quasipolynomial-size public
   representative and can be found in the allowed source; or
2. exploit a true arithmetic hypercycle outside the formal endpoint cycle
   space.  In a fixed squared-anchor star, Section 7 shows that this requires
   square residuals after a quasipolynomial factor-base removal, or
   cancellation through older columns.

F143 gives no such theorem.
