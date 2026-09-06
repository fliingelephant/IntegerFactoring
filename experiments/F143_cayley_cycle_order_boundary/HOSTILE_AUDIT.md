# F143 hostile audit — PASS

## Frozen inputs

I audited the complete frozen candidate with hashes

- `STATEMENT.md`:
  `bc9a9e399c03bff991cc85920eb6c0218276b1d05d0788b82461b39030b1a35a`;
- `PROOF.md`:
  `7c2784202f2a42200b126b54262c5d202ad86a0c2d1cc35931ddf52322ad86c2`.

Both hashes matched the expected hashes before the audit.  I did not modify
either frozen file.  I used no research computation.

## Verdict

**PASS.**  I found no mathematical defect or scope overreach in the frozen
candidate.

The result is a boundary theorem.  It does not prove a useful cycle, a useful
arithmetic hypercycle, or a quasipolynomial factoring algorithm.  Its two
positive contributions survive audit:

1. every legal formal squared-action cycle has exactly the claimed public
   half-relation root; and
2. a bridge-only dependency in one fixed star must pass the stated public
   square-residual test after removal of primes at most $A^4$.

## 1. Legal source and quotient vertices

For

\[
v_z=[q\Phi(z)^2]_N,
\]

unit cancellation gives

\[
v_z=v_{z'}
\iff \Phi(2(z-z'))=1
\iff z-z'\in\Lambda_2.
\]

Thus the vertex quotient in (3)--(4) is exact.

The source claim is correctly conditional.  A canonical residue $v_z$ is
not declared to be a named block.  An edge exists only when the raw positive
word $v_za_j^2$ is a legal frozen F141 position.  Negative exponents occur
only in the abstract lattice and in reverse traversal of an already available
positive edge.  They are not smuggled into the F141 word grammar.  The
complete-Cayley-graph paragraph is explicitly counterfactual and makes no
source-existence claim.

Equal public vertices do not make edge lifting ambiguous.  If
$v_z=v_{z'}$, then $z-z'\in\Lambda_2$, and multiplication by the same
$a_j^2$ gives $v_{z+e_j}=v_{z'+e_j}$.  Therefore a public walk can be
lifted from any exponent representative, with total signed displacement
$\delta(C)$.

## 2. Exact cycle and normalized root

For one stored edge $u\to h$ with label $a$,

\[
D=u a^2 h,
\qquad D\equiv h^2\pmod N.
\]

On a closed edge-distinct trail, every public endpoint occurs twice.  Hence

\[
\prod_{e\in C}D_e
=\left(\prod_{t}x_t\prod_{e\in C}a_{j(e)}\right)^2
\]

as an exact integer identity.  Dividing this positive exact root by the
product of the supplied roots $h_e$ gives one factor $a_j$ for an edge
traversed forward and one factor $a_j^{-1}$ for an edge traversed backward.
Thus

\[
\rho(C)=\Phi(\delta(C)).
\]

Closure gives $v_z=v_{z+\delta(C)}$, so
$2\delta(C)\in\Lambda$ and $\rho(C)^2=1$.  For odd $N$, the two gcd
tests factor exactly when this root is not a global sign.  This also verifies
the direct-collision equivalence: once the signed edge labels are known, the
same residue $\Phi(\delta(C))$ can be evaluated without the bridge decoder.

Reversing the walk inverts the root.  Since the root is self-inverse, this
does not change it.  A zero displacement gives root $+1$, so the automatic
commutation diamond is a genuine global-root decoy.

The claim also survives loops, parallel edges, and repeated-edge walks.  A
repeated occurrence pair contributes $D_e^2$; its exact root is $D_e$,
its supplied root is $h_e^2$, and
$D_eh_e^{-2}\equiv1\pmod N$.  Removing occurrence pairs preserves the
normalized root and leaves the binary formal cycle support.  A non-global
walk therefore cannot collapse to the zero support.

## 3. Complete formal-cycle image

Let $H=\Phi(\mathbb Z^m)$.  The map

\[
\Lambda_2/\Lambda\longrightarrow H[2],
\qquad \delta+\Lambda\longmapsto\Phi(\delta)
\]

has kernel zero and is onto.  If every positive generator edge exists at
every public vertex, any signed word for $\delta\in\Lambda_2$ gives a
closed walk.  The cycle-root image is therefore exactly $H[2]$.

This does not give a short word.  In one generator, the first useful
displacement is the half-order target from P71 and can have exponential
numeric size in $n=\Theta(\log N)$.  The frozen statement correctly says
that a quasipolynomial decoder does not supply the missing displacement.

## 4. Deduplication and arithmetic hypercycles

The deduplication argument is applied at the correct level.  The actual
F141 values are $A_e=h_ew_e$ and $B_e=u_ea_j^2w_e$, and every one is
congruent to $1\pmod N$ with supplied root $1$.  Two selected equal
integer occurrences $T,T$ contribute the exact square $T^2$.  Removing
them changes the normalized root by $T\equiv1\pmod N$, so it changes
nothing.  One globally retained representative realizes every odd
exact-value class.

The proof does not incorrectly deduplicate conceptual bridge integers.
Those can have different supplied roots.  It first restores the actual
canonical and lifted occurrences, then performs exact-value cancellation.

The map $J\partial$ is also scoped correctly.  Formal endpoint incidence
implies true rational square-class cancellation, but the reverse can fail
when distinct composite endpoints share prime rows.  F143 therefore proves
only

\[
\ker\partial\subseteq\ker(J\partial)
\]

and leaves arithmetic hypercycles, including cancellation with old columns,
open.

## 5. Fixed-star carry bound

For distinct prime anchors $\ell,m$, direct expansion gives

\[
m^2c_\ell-\ell^2c_m
=N(\ell^2t_m-m^2t_\ell)=N\Delta_{\ell,m}.
\]

Every $c_\ell$ is a unit modulo $N$.  Hence
$g=\gcd(c_\ell,c_m)$ is coprime to $N$, and $g\mid\Delta_{\ell,m}$.
If the determinant is nonzero, both terms lie in
$[0,\ell^2m^2)$, which gives the strict bound
$0<|\Delta_{\ell,m}|<\ell^2m^2\le A^4$.

If $\Delta_{\ell,m}=0$, coprimality of the distinct prime squares forces
$\ell^2\mid t_\ell$ and $m^2\mid t_m$.  Their defining ranges force
both carries to be zero.  Then $c_\ell=q\ell^2$ as an integer and
$D_\ell=c_\ell^2$, with exact and supplied root $c_\ell$.  Its
normalized root is $+1$.  Thus the zero determinant is not an omitted
wrapped case.

For a wrapped endpoint,

\[
\gcd(q,c_\ell)=\gcd(q,t_\ell),
\]

because $q$ is a unit modulo $N$.  Its shared primes are below
$\ell^2\le A^2$.  After all prime powers at primes at most $A^4$ are
removed, the residuals are pairwise coprime and coprime to $q$.  Their
primes also cannot occur in any anchor square.  Therefore an exact square
product of fixed-star bridges can select $r_\ell$ only when every selected
$r_\ell$ is itself a square.  This is a necessary condition, as claimed;
the small-prime rows and the $q$-class can still obstruct closure.

The cost statement is valid.  If
$A=\exp((\log n)^{O(1)})$, enumerating primes or trial divisors through
$A^4$, performing repeated exact division on $O(n)$-bit endpoints, and
testing the residual square costs quasipolynomial time.  No factorization of
$N$ is used.  The theorem correctly excludes arbitrary old columns from
this fixed-star conclusion.

## 6. Relation to prior project results

- P71 gives the general hidden exponent-lattice and half-order boundary.
  F143 does not claim to escape it.  It identifies the exact displacement
  and root map for the F141 bridge graph.
- P122 gives a different one-star gcd confinement for canonical inverse
  cofactors.  F143's carry determinant applies to the squared-action residue
  endpoints and yields the new $A^4$ residual-square gate.
- P129 gives the bridge relative-rank gate and the root of an exact adaptive
  endpoint cycle.  F143 generalizes that cycle calculation to arbitrary
  signed Cayley walks, identifies its full formal image, and separates it
  from arithmetic hypercycles.

The novelty description is therefore appropriately narrow.  It is a useful
structural refinement and pruning theorem, not a new factoring principle.

## Residual risk

This audit is an internal proof check.  It is not a publication-level
literature review.  A proof-blind reconstruction is still required before
promotion under the project protocol.
