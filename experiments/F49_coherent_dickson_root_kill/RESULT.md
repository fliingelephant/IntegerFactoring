# F49 — coherent Dickson-root selection collapses to one CRT idempotent

## Status and scope

**Status:** corrected candidate kill-first classification. The first hostile audit
passed the one-triangle algebra, endpoint theorem, and anchor probability, but
required mathematical amendments to the treatment of degenerate/repeated vertices,
shifted-root coherence, and disconnected components. Those amendments are included
below; the failed audit remains preserved. This file is proof-only. It uses no
computation, web search, or unproved distribution heuristic.

**Family:** F28, following P57.

**Closest prior route and material difference.** P57 proves that ordinary Dickson
trace identities have four exact exponent aliases and leaves polynomially many
coherent shifted-root choices open. This follow-up does not try to recover the
hidden exponent. It writes the entire nondegenerate coherent-root system as a
coordinate algebra and asks whether extra polynomial relations can select a mixed
CRT root.

**Classification claimed here.** After gcd screening, linear elimination of every
known constant root, and exact simplification of repeated-variable relations, each
connected component of the resulting orientation graph has one idempotent
orientation variable. Its coordinate algebra is

\[
  (\mathbb Z/N\mathbb Z)[f]/(f^2-f).
\]

The two public idempotents give the two synchronized roots. The two nontrivial
idempotents give the factor-bearing mixed roots. Any explicit polynomial equation
that holds at both public endpoints is tautological on this algebra. If it retains
a mixed point but excludes a public endpoint, evaluating it at the endpoints
already gives a proper gcd. Thus adding polynomially many algebraic coherence
relations cannot invisibly select the mixed root.

This is not a lower bound against arbitrary factoring algorithms. Metric order,
inequalities, canonical least representatives, stochastic or dissipative rules,
opaque root samplers, derivatives, lifts modulo \(N^2\), and lucky gcd
distributions remain outside the theorem.

## 1. Set-up

Let

\[
  N=pq,\qquad 3\le p<q
\]

for distinct odd primes, and put

\[
  R=\mathbb Z/N\mathbb Z,\qquad e=N-1,\qquad g=q-p.
\]

For a unit \(z\), write

\[
  T(z)=z+z^{-1},\qquad E(z)=z^e,\qquad G(z)=z^g.
\]

P57 gives

\[
  E(z)\equiv G(z)\pmod p,\qquad
  E(z)\equiv G(z)^{-1}\pmod q,
\]

and therefore \(T(E(z))=T(G(z))\) in \(R\).

Every introduced residue is screened by an ordinary gcd. A proper gcd is success;
a full gcd is a degeneracy or rejection. No hidden local generator, order, or
factor is used by the public procedure.

## 2. All trace-compatible homomorphisms

### Theorem 2.1

Let \(H:R^\times\to R^\times\) be a group homomorphism such that

\[
  T(H(a))=T(E(a))
  \quad\text{for every }a\in R^\times.
  \tag{2.1}
\]

Then, with possible coincidences in small or self-inverse image groups,

\[
  H\in\{E,E^{-1},G,G^{-1}\}.
  \tag{2.2}
\]

### Proof

Use CRT to write an input as \((a,b)\in\mathbb F_p^\times\times
\mathbb F_q^\times\). In the \(p\)-component, set \(a=1\). Equation
(2.1) becomes

\[
  H_p(1,b)+H_p(1,b)^{-1}=2.
\]

Over a field this is \((H_p(1,b)-1)^2=0\), so \(H_p(1,b)=1\). Hence
\(H_p\) kills the entire \(q\)-side subgroup and factors through
\(\mathbb F_p^\times\). The same argument shows that \(H_q\) factors
through \(\mathbb F_q^\times\).

Each local unit group is cyclic, so its local homomorphism is a power map.
The one-prime trace-alias theorem from P57 says

\[
  z^u+z^{-u}=z^v+z^{-v}\text{ for all }z\in\mathbb F_r^\times
  \quad\Longleftrightarrow\quad
  u\equiv\pm v\pmod{r-1}.
\]

Thus independently in the two fields, \(H_r\) is \(E_r\) or
\(E_r^{-1}\). The two synchronized sign choices give \(E,E^{-1}\).
The two opposite sign choices give \(G,G^{-1}\), by the displayed local
relations between \(E\) and \(G\). This includes \(r=3\) and self-inverse
classes. \(\square\)

### Consequence

The coherent ambiguity is exactly one local sign choice per hidden prime. It is
not a growing sequence of independent signs as more bases are added.

## 3. A public nondegenerate anchor appears in constant expectation

Let

\[
  d=\gcd(p-1,q-1),\qquad
  h_p=(p-1)/d,\qquad h_q=(q-1)/d.
\]

For a uniform unit \(a\), the two CRT coordinates of \(E(a)\) are
independent and uniform in cyclic image groups of sizes \(h_p,h_q\). Since
\(p<q\), one has \(h_p<h_q\).

Compute

\[
  \Delta=E(a)-E(a)^{-1}.
\]

If \(1<\gcd(\Delta,N)<N\), a factor is found. If the gcd is 1, \(a\)
is a nondegenerate anchor. If the gcd is \(N\), both local values are in
\(\{1,-1\}\). Then compute the gcds of \(E(a)-1\) and \(E(a)+1\).
Opposite local signs factor \(N\); equal signs give a synchronized constant
and the sample is discarded.

The exact probability of this last no-factor/no-anchor outcome is

\[
  \frac{1+\mathbf 1_{2\mid h_p,\,2\mid h_q}}{h_ph_q}\le\frac12.
  \tag{3.1}
\]

Indeed, \((1,1)\) is always one synchronized pair, while \((-1,-1)\)
exists exactly when both image orders are even. If both are even, their
strict inequality gives \(h_ph_q\ge8\); otherwise
\(h_ph_q\ge1\cdot2\). Equality in (3.1) occurs only at
\((h_p,h_q)=(1,2)\), equivalently \(q=2p-1\).

A raw uniform residue is a unit with probability

\[
  \frac{(p-1)(q-1)}{pq}\ge\frac8{15};
\]

a proper initial gcd is already success. Thus a factor or a unit-difference
anchor is obtained in constant expected trials and polynomial bit cost. This
does not choose a mixed orientation; it only makes later comparison exact.

## 4. One multiplicative triangle

Let \(A,B\in R^\times\), put \(C=AB\), and assume

\[
  A-A^{-1}\in R^\times,\qquad B-B^{-1}\in R^\times.
  \tag{4.1}
\]

Consider root variables \(X,Y,Z\) with

\[
\begin{aligned}
 &(X-A)(X-A^{-1})=0,\\
 &(Y-B)(Y-B^{-1})=0,\\
 &(Z-C)(Z-C^{-1})=0,\\
 &Z=XY.
\end{aligned}
\tag{4.2}
\]

Define

\[
  f=\frac{X-A^{-1}}{A-A^{-1}},\qquad
  h=\frac{Y-B^{-1}}{B-B^{-1}}.
\]

The first two equations are exactly \(f^2=f\) and \(h^2=h\). Before the
last root equation, the Boolean coordinate algebra is the product of its four
corners \((f,h)\in\{0,1\}^2\).

At \((1,1)\), \(XY=C\); at \((0,0)\), \(XY=C^{-1}\). At the mixed
corner \((1,0)\), the last root polynomial evaluates to

\[
  (AB^{-1}-AB)(AB^{-1}-A^{-1}B^{-1}),
\]

which is a unit by (4.1). The other mixed corner gives the analogous unit.
Therefore the last equation kills exactly the two mixed Boolean components.
The resulting coordinate algebra is

\[
  \boxed{R[f]/(f^2-f),}
  \tag{4.3}
\]

with \(h=f\),

\[
  X=A^{-1}+f(A-A^{-1}),\qquad
  Y=B^{-1}+f(B-B^{-1}),
\]

and \(Z=C^{-1}+f(C-C^{-1})\). No division by \(C-C^{-1}\) is needed.

Thus a nondegenerate multiplicative triangle synchronizes its three root
orientations. It does not decide which orientation is used.

## 5. Finite reduced relation systems

Take finitely many public values \(A_v=E(a_v)\) and root variables

\[
  (X_v-A_v)(X_v-A_v^{-1})=0.
\]

For every genuine multiplicative relation \(a_w=a_ua_v\), impose
\(X_w=X_uX_v\). First gcd-screen every \(A_v-A_v^{-1}\). A proper gcd
is success. A full gcd is further screened by \(A_v\pm1\); an unfactored
survivor has \(A_v=s\in\{1,-1\}\) in \(R\).

At this point impose the **linear** equation \(X_v=s\) and eliminate that
variable. This step is necessary at the coordinate-algebra level. The raw
double-root algebra \(R[X_v]/((X_v-s)^2)\) has a nilpotent, even though
every \(R\)-valued point has \(X_v=s\).

Now simplify each relation and form the **reduced orientation graph**. Its
vertices are the remaining distinct nondegenerate root variables. Add an
orientation edge exactly in the following proved cases:

1. If \(u,v,w\) are three distinct nondegenerate variables, Section 4
   identifies all three orientations.
2. If \(u=v\), \(w\ne u\), and both remaining variables are
   nondegenerate, then \(X_w=X_u^2\). The two unequal Boolean corners are
   excluded because
   \(A_w-A_w^{-1}=A_u^2-A_u^{-2}\) is a unit. Thus the two
   orientations agree.
3. After substituting one known constant \(s=\pm1\), two distinct remaining
   nondegenerate variables satisfy \(X_w=sX_u\). Their unequal corners
   violate this equation by \(A_u-A_u^{-1}\), up to a unit factor, so
   their orientations agree.
4. A simplified relation containing at most one distinct nondegenerate
   variable supplies no orientation edge.

The first case is Section 4. In the second and third cases, normalize both
root pairs by their unit root differences. Direct evaluation at the four
Boolean corners leaves the two equal corners and gives units at the unequal
corners. The same product-ring argument therefore kills exactly the unequal
components. Notice that two triangles sharing only a constant vertex need not
connect their other orientations.

On every connected component of this reduced orientation graph, the displayed
edge equalities identify all orientation variables. The component coordinate
algebra is exactly

\[
  R[f_j]/(f_j^2-f_j).
  \tag{5.1}
\]

Different reduced components have one such idempotent each. Adding more proved
orientation edges inside a component repeats the same idempotent; it does not
create new local orientation bits.

For P57's shifted roots, one screened quadratic with public known roots
\(A_i,B_i\) gives only

\[
  Z_i=B_i+f_i(A_i-B_i),\qquad f_i^2=f_i,
  \tag{5.2}
\]

with an independent \(f_i\). The quadratics alone do **not** identify these
variables. Define a shifted family to be **coherent** only after explicit
relations have been proved to identify all its \(f_i\) in the reduced
orientation graph. Equivalently, the four sections induced by one
trace-compatible homomorphism \(H\in\{E,E^{-1},G,G^{-1}\}\) are coherent:
their normalized idempotents are respectively \(1,0\), and the two fixed
nontrivial CRT idempotents, for every shift. On such an established common
component,

\[
  Z_i=B_i+f(A_i-B_i),\qquad f^2=f.
  \tag{5.3}
\]

The choices \(f=0,1\) are the two public synchronized root families. The
two nontrivial CRT idempotents are the coherent mixed families associated to
\(G\) and \(G^{-1}\). No unspecified Dickson identity is asserted to force
this coherence.

## 6. The exact selector boundary

Let

\[
  \mathcal A=R[f]/(f^2-f).
\]

Every polynomial expression has the unique endpoint form

\[
  Q(f)=Q(0)(1-f)+Q(1)f.
  \tag{6.1}
\]

### Theorem 6.1 — endpoint dichotomy

1. If \(Q(0)=Q(1)=0\) in \(R\), then \(Q=0\) in \(\mathcal A\). The
   equation \(Q(f)=0\) is tautological.
2. Suppose a nontrivial idempotent \(e\in R\) satisfies \(Q(e)=0\). If
   at least one synchronized endpoint is not a solution, then
   \(\gcd(Q(0),N)\) or \(\gcd(Q(1),N)\) is a proper factor.

### Proof

The first part is immediate from (6.1). For the second, write under CRT,
without loss of generality, \(e=(1,0)\). Then \(Q(e)=0\) says

\[
  Q(1)=0\pmod p,\qquad Q(0)=0\pmod q.
\]

If \(Q(1)\ne0\) in \(R\), its gcd with \(N\) is \(p\). If
\(Q(0)\ne0\), its gcd is \(q\). If both vanish in \(R\), both public
endpoints remain solutions. The case \(e=(0,1)\) swaps \(p,q\).
\(\square\)

The theorem applies equation by equation to every finite explicit polynomial
system **after** all its relevant variables have been proved to lie in one
common-\(f\) component. For a system \(Q_j(f)=0\), if a mixed idempotent
solves all equations and a synchronized endpoint fails the system, choose one
equation that fails there and apply Theorem 6.1. Therefore, on one established
component:

- if every added equation accepts both public endpoints, the system is
  identically true on the whole idempotent algebra;
- if the system retains a mixed point but removes a public endpoint, an
  endpoint evaluation factors before any root solver is called;
- if a solver returns a mixed point, comparison with any unit-difference
  anchor factors immediately;
- a solver may always return one of the two public endpoints, so mere
  solvability gives no factor.

This is the exact sense in which polynomial relation amortization fails in
this one-component coherent-root model. It does not automatically cover several
independent idempotents, arbitrary polynomial couplings between components, or
extra existential variables. For example, \(f_1-f_2=0\) must first be
recognized as an orientation edge and reduced to one variable; applying the
one-variable endpoint statement to the unreduced two-variable presentation would
be invalid.

## 7. Factor extraction and equivalence of the mixed section

For a unit-difference pair \(A,A^{-1}\), let

\[
  X=A^{-1}+e(A-A^{-1})
\]

with a nontrivial idempotent \(e\). Then one of

\[
  \gcd(X-A,N),\qquad \gcd(X-A^{-1},N)
\]

is \(p\) and the other is \(q\). Conversely, known factors construct both
nontrivial idempotents by CRT and hence every coherent mixed section. Thus,
on the screened promise, constructing one mixed coherent root is
deterministic polynomial-time equivalent to factoring the semiprime.

This equivalence is an extraction theorem, not a construction of the root.

## 8. Strongest amortization conclusion

Polynomially many relations inside one proved connected component do not provide
polynomially many independent chances. They provide one common idempotent. More
relations on that component can do only one of the following inside the explicit
polynomial model:

1. repeat identities that also hold for the two public synchronized sections;
2. expose a selective endpoint coefficient, which already factors by gcd; or
3. request a nontrivial idempotent, which is the factorization itself.

Separate reduced components give more idempotent variables, and the all-public
endpoint assignments survive, but arbitrary cross-component equations are outside
the one-variable theorem until their effect on the orientation graph is proved.
A claim that a random root solver returns a mixed point needs a separately
specified sampling law and a proved inverse-polynomial probability; no such law
follows from the equations.

## 9. Exact reopen conditions

This result closes only finite explicit polynomial coherence over a screened,
linearly reduced, proved common-idempotent component of the root-pair interface.
A retry is materially new if it supplies one of:

1. an ordered or metric rule, inequality, optimization objective, rounding, or
   canonical representative that can be evaluated without already exposing an
   idempotent;
2. a stochastic, dissipative, or positive-combinatorial sampler with a proved
   mixed-section probability and uniform polynomial bit cost;
3. a derivative, resultant/minor using data not already an endpoint polynomial,
   or a controlled lift modulo \(N^2\);
4. a lucky-gcd or non-generator distribution theorem with inverse-polynomial
   all-input success;
5. an explicit-coordinate algorithm outside the finite polynomial relation
   model;
6. a promise decoder plus a complete treatment of prime powers, repeated
   factors, evens, multifactor inputs, recursion, and one uniform Las Vegas
   expected-bit bound.

Raw degenerate quadratic schemes, unspecified shifted-root coherence, arbitrary
multicomponent polynomial couplings, and auxiliary existential variables are also
outside the proved classification unless they are first reduced to the exact
one-component form above.

No generic computational lower bound, information-theoretic lower bound, or
all-input factoring theorem is claimed.
