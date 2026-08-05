# Hostile audit of X10 / F09

## Verdict

The diagonal linear-algebra obstruction and the exact `N=91` certificate
survive, but only for a more explicit carrier class than the draft wording
could suggest.  The cyclotomic product argument also survives after adding
the missing coprimality hypothesis.  Claims that an orientation is
noncanonical, uncomputable from `N`, or factoring-equivalent do not follow
and must not be inferred.

## Corrected diagonal-carrier theorem

Let `ell` be prime, let `V=F_ell^2`, fix one common generator `zeta` of
`mu_ell`, and let `s(x,y)=(y,x)`.  An admissible scalar label is a group
homomorphism

`chi:(V,+) -> mu_ell`

whose **individual value** is fixed by factor swap: `chi o s=chi`.  Then
there is an `alpha in F_ell` such that

`chi(x,y)=zeta^(alpha*(x+y))`.

Consequently, a family of admissible labels has joint rank at most one.  If
the family contains a nontrivial label, its common kernel is exactly

`K={(t,-t):t in F_ell}`;

if every label is trivial, the rank is zero and the common kernel is all of
`V`.

Now restrict carrier queries to fixed public unit twists and integer powers,
`a -> t_j*a^k_j`, with later choices allowed to depend only on public
randomness and earlier admissible labels.  Allow multiplication/division of
such group expressions and postselection based only on the resulting
labels.  The complete transcript factors through

`Sigma(u(a))=u_p(a)+u_q(a)`.

For several independent base units it factors through the tuple of their
individual `Sigma` values.  It contains no dependence on their
anti-diagonal components.

### Proof

Writing `chi(x,y)=zeta^L(x,y)` identifies a group character with an additive
map `L:V->F_ell`.  Because `ell` is prime, every such map is `F_ell`-linear,
so `L(x,y)=alpha*x+beta*y`.  The identity `L(x,y)=L(y,x)` for all `x,y`
forces `alpha=beta`.  This proves the form and the rank/kernel statements.

For a unit twist,

`u(t*a^k)=u(t)+k*u(a)`.

An admissible label therefore has exponent

`alpha*Sigma(u(t)) + alpha*k*Sigma(u(a))`.

Addition/subtraction of group expressions preserves this form.  Inductively,
two hidden phase vectors with the same `Sigma` produce the same prior labels,
cause the same adaptive branch, and produce the same next label.  An event
defined by postselection on the transcript is therefore a union of `K`
cosets and cannot refine one.  Since the two nontrivial local order-`ell`
characters are surjective and CRT is surjective, every vector in `V`, hence
every point of each such coset, is realized by an actual unit modulo `pq`.

This proof does **not** cover a family whose individual labels are
factor-oriented but whose vector, multiset, or distribution is merely
swap-equivariant.  For example, the unordered pair of coordinate characters
is globally swap-invariant and has rank two, but it is vector/multiset-valued,
not an admissible scalar label.  Nor does the proof cover additive queries
such as `a -> a+1`, twists selected using information outside the carrier
transcript, nonlinear labels, or prime-dependent local coefficients.

## Exact cubic certificate

Use the convention `chi_7(3^e)=zeta^(e mod 3)` and
`chi_13(2^e)=zeta^(e mod 3)`.  Direct calculation gives

`u(15)=(0,1)`, `u(18)=(1,0)`, and `15/18=16 (mod 91)` with
`u(16)=(2,1)`.

Thus the two initial units have the same scalar sum, while their quotient has
zero scalar sum and neither local coordinate zero.  All nine phase pairs
occur exactly eight times among the 72 units; each of the three diagonal-sum
fibers therefore has 24 units.

The independent exhaustive run A02 reproduces these facts without importing
the discovery source.

## Corrected cyclotomic product proposition

Let `ell` be an odd prime, `K=Q(zeta_ell)`, let `p=1 (mod ell)` be rational
prime, and let the rational integer `a` satisfy `p` not dividing `a`.  Then

`product_{P|p} (a/P)_ell = 1`,

where the product ranges once over every prime ideal of `O_K` above `p`.

### Proof

The prime `p` splits completely, and `Gal(K/Q)` acts transitively on its
`ell-1` primes.  Power-residue symbols are Galois-covariant.  Since `a` is
rational, if `xi=(a/P_0)_ell`, the displayed factors are exactly
`sigma(xi)` as `sigma` ranges over `Gal(K/Q)`.  Their product is
`Norm_{K/Q}(xi)`.  Writing `xi=zeta_ell^e`, this norm is

`zeta_ell^(e*(1+2+...+(ell-1)))=1`,

because `ell` is odd.  Equivalently, it is the norm of an `ell`-th root of
unity, whose cyclotomic norm is one.

The restriction `p` not dividing `a` is necessary because the residue symbol
is otherwise not a `mu_ell`-valued unit symbol.  The proposition concerns the
equal product of all conjugate ideal symbols on rational numerators.  It does
not rule out symmetric nonmultiplicative data, vector/ring-valued output, or
other higher-residue constructions.

## What the orientation example proves

For `ell=3`, a root `rho` of `Phi_3` modulo squarefree `N` defines the
evaluation map

`Z[zeta_3] -> Z/NZ`, `zeta_3 -> rho`.

Its kernel is `I_rho=(N,zeta_3-rho)`, and the quotient has exactly `N`
elements, so `Norm(I_rho)=N`.  CRT decomposes this ideal into one selected
prime ideal above each rational prime dividing `N`.  This is the precise
sense in which `rho` supplies an orientation; the selection can be implicit
and does not require that the factors have already been computed.

For `N=91`, the four roots are

- `rho=9` with components `(2,9)`;
- `rho=16` with components `(2,3)`;
- `rho=74` with components `(4,9)`;
- `rho=81` with components `(4,3)`.

Global conjugation `rho -> -1-rho` pairs `9` with `81` and `16` with `74`;
the two differences are units modulo 91.  Two roots that agree in exactly
one CRT component instead have difference gcd 7 or 13 with 91.  Hence two
given roots from different global-conjugacy orbits split this example by a
gcd.

Existence of `I_rho` does not establish that a root is hard to compute from
`N`, that no canonical rule can select one, or that one root factors `N`.
The least root is already a mathematically canonical choice in this finite
example, irrespective of its computational cost.  No factoring equivalence
is proved.  The safe conclusion is only that a conventional nontrivial
one-valued ideal-symbol evaluation must supply or compute one such
orientation rather than multiply all Galois-conjugate primes.

## Computation provenance

`F09-PA-A01` passed all mathematical assertions but failed while serializing
Sage-integer dictionary keys; its traceback and partial invalid output are
retained.  `F09-PA-A02` passed with a 60-second timeout and records the phase
counts, collision, four roots, six gcds, and conjugate-symbol products in
`output/A02.json`.
