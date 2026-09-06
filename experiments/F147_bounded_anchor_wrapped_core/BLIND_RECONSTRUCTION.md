# F147 statement-only blind reconstruction

## Protocol

- The only F147 source read for this audit was `STATEMENT.md`.
- Its SHA-256 was verified before reading:
  `2fc9e36eac6754ffe0405d017d9a58829f95965fbdde94b7ce0f060e4309c204`.
- No proof, manifest, ledger, earlier reconstruction, or other F147 artifact was consulted.

## Verdict

**FAIL as written.**  The wrapped-large-core theorem, bridge decoder,
normalized-root test, exact-value deletion argument, edge-surplus bound, and
quasipolynomial cost bound all reconstruct from first principles.  However,
the reachability assertion attached to (12) is false as stated.  The anchor
upper bound gives a necessary length condition, not a sufficient one, and the
strict threshold is also lost.  An explicit counterexample and the corrected
claim appear below.

The normalized-root reconstruction uses the intended P128 meaning of
`w = iota_N(c)`: `w` is a positive representative of `c^{-1} (mod N)`.  In
particular, `cw = 1 (mod N)`.  Likewise, the cost reconstruction uses the
usual convention that `n = Theta(log N)`.  Those meanings are imported rather
than defined in this statement.

## 1. Basic bounds

Because `q < N`, `a <= H`, and `c` is the nonzero residue of `qa^2` modulo
`N`,

\[
qa^2=c+tN,\qquad 0\leq t<a^2\leq H^2.
\]

The residue is nonzero because `q` and `a` are units modulo `N`.  If a
position wraps, then `qa^2>N`, hence

\[
q>\frac{N}{a^2}\geq\frac{N}{H^2}.
\tag{A}
\]

Also, `H^4 <= N` implies

\[
H^2\leq \frac{N}{H^2}.
\tag{B}
\]

These two inequalities drive the large-core theorem.

## 2. Large-core theorem

Consider an unwrapped edge `q -> r`.  Its defining equality is

\[
qa^2=rT.
\]

The named blocks `q` and `r` are distinct and pairwise coprime.  Therefore
`r` divides `a^2`, so

\[
r\leq a^2\leq H^2\leq N/H^2.
\tag{C}
\]

The target `r` is the source of the next edge on a directed cycle.  By (C),
for every legal next anchor `b <= H`, one has `rb^2 <= N`.  Thus that next
edge cannot wrap.  Hence one unwrapped edge forces every later edge on the
cycle to be unwrapped.  Going around the cycle proves the contrapositive:
if one edge wraps, every edge wraps.

For an all-wrapped cycle, (A) applies at every source.  Every target is the
next source.  Thus both endpoints of every cycle edge exceed `N/H^2`.  The
carry satisfies

\[
1\leq t<a^2\leq H^2,
\]

and, since `c=rT<N` and `r>N/H^2`,

\[
1\leq T=\frac c r<\frac N r<H^2.
\]

This proves all four bounds in (5).

For uniqueness, suppose two distinct named blocks `r` and `s`, both larger
than `N/H^2`, divide the same residue `c`.  Pairwise coprimality gives
`rs | c`, while

\[
rs>\frac{N^2}{H^4}\geq N>c,
\]

a contradiction.  Thus each position has at most one large target.  Every
edge of a wrapped cycle has a large source, a large target, and positive
carry, so the scan defining `G_H` retains it.  This proves containment of all
wrapped cycles and the no-branching claim per word position.  It does not
bound the number of different positions leaving one vertex.

## 3. Exact bridge square classes

For an edge `e:q -> r`,

\[
D_e=U_ec_e=(q a_e^2)(rT_e)=qra_e^2T_e,
\]

and `U_e = c_e (mod N)`, so `D_e = c_e^2 (mod N)`.  The anchor contributes
only the explicit square `a_e^2`.  Therefore the binary square class of
`D_e` is exactly the sum of the square classes of `q`, `r`, and `T_e`.

The proposed gcd-free route is sufficient without factoring the large named
blocks.  Complete multiplicity-aware refinement expresses all center blocks
and residuals as powers of pairwise coprime atoms.  Maximal perfect-power
extraction writes an atom as `b^k` with `b` not itself a perfect power.  For
such a `b`, `b^j` is a square exactly when `j` is even: if `j` is odd, at
least one rational-prime valuation of `b` is odd; if `j` is even, all
valuations in `b^j` are even.  Pairwise coprimality makes these conditions
independent between atoms.  The resulting parity matrix therefore has
kernel exactly equal to the set of edge subsets whose `D_e` product is an
integer square.

The direct residual route is also correct.  Since `T_e < H^2`, every
composite `T_e` has a prime divisor below `H`.  Trial division through `H`,
with multiplicities, leaves either `1` or one prime cofactor.  It takes time
polynomial in the numerical parameter `H`, as claimed; it is not claimed to
be polynomial in `log H`.

For `x in ker(M_H)`, let

\[
Y_x^2=\prod_{e:x_e=1}D_e,
\qquad C_x=\prod_{e:x_e=1}c_e.
\]

Every `c_e` is a unit modulo `N`, and

\[
\rho_x^2=Y_x^2C_x^{-2}
 =\prod_e D_e\prod_e c_e^{-2}=1\pmod N.
\]

Thus (7) is a square root of unity modulo `N`.

For the actual P128 pair,

\[
C_eL_e=(c_ew_e)(U_ew_e)=D_ew_e^2.
\]

Its positive product root is `Y_x product_e w_e`.  Since
`w_e = c_e^{-1} (mod N)`, this root is congruent to (7).  This proves the
same-normalized-root claim.

## 4. Exact-value deletion and basis-root test

Let `V` be the binary vector space with one coordinate for each global exact
integer equality class of actual P128 values.  Define the linear map

\[
A:\ker(M_H)\longrightarrow V
\]

by sending an edge to the two equality-class coordinates of `C_e` and
`L_e`.  Addition in `V` is parity, so two equal actual values cancel.  Since
the product before cancellation is a square and a cancelled pair contributes
an exact square, `A(x)` remains a square dependency.

The root map is multiplicative under binary addition.  Indeed, common edges
removed from `x+y` contribute the correction `D_e/c_e^2`, which is `1`
modulo `N`.  Hence

\[
\rho_{x+y}=\rho_x\rho_y\pmod N.
\tag{D}
\]

Moreover,

\[
C_e=c_ew_e=1\pmod N,
\qquad L_e=U_ew_e=1\pmod N.
\]

If `A(x)=0`, every selected exact value occurs an even number of times.  The
positive square root is then the product of one value from each equal pair,
so it is `1 (mod N)`.  Therefore

\[
A(x)=0\quad\Longrightarrow\quad\rho_x=1.
\tag{E}

Equations (D) and (E) show that the root homomorphism factors through
`im(A)`.  Choose a binary basis of `im(A)` and tracked preimages in
`ker(M_H)`.  If every basis preimage has root `+1` or `-1`, every linear
combination does too.  Conversely, a non-global root must occur on at least
one such basis preimage.  This validates the claimed polynomial-size basis
test; it is a compact representation and does not enumerate exponentially
many kernel vectors.

If `rho_x` is neither `+1` nor `-1`, put `d=gcd(rho_x-1,N)`.  One has
`d<N` because `rho_x != 1`.  If `d=1`, then from
`N | (rho_x-1)(rho_x+1)` and oddness of `N` it follows that
`N | rho_x+1`, contradicting `rho_x != -1`.  Hence `1<d<N` and `d` is a
proper factor.  Finally, (E) proves the exact deletion statement: a
non-global dependency cannot map to zero.

## 5. Edge-surplus bound

Let `v(q)` denote the rational-prime parity vector of a named block and let
`v(T_e)` denote that of a residual.  Each column of `M_H` is

\[
v(q)+v(r)+v(T_e).
\]

All center contributions lie in the span of at most `m` vectors `v(q_i)`.
All residual contributions lie in the span of the `R_H` rational-prime unit
vectors that occur in residuals.  Thus

\[
\operatorname{rank}(M_H)\leq m+R_H,
\]

and rank-nullity gives

\[
\dim\ker(M_H)\geq E_H-m-R_H.
\]

Every residual prime is below `H^2`, so `R_H <= pi(H^2)`.  This proves (9).
The bound forces only a conceptual bridge dependency.  It does not imply a
nonzero exact-value image or a non-global root.

## 6. Cost reconstruction

There are at most `Q` explicit positions and at most `Q` named blocks.
Testing every position against every possible named target uses at most
`Q^2` exact divisions.  The operands have `O(n+log H)` bits.

The remaining operations are polynomial in the stated parameters:

- gcd and endpoint screens use polynomial-time integer arithmetic;
- each actual value has `O(n+log H)` bits up to a constant factor, and at
  most `Q` ledger values are sorted;
- gcd-free refinement and perfect-power detection are polynomial in the
  number and bit length of their inputs;
- residual trial division costs polynomial time in `Q`, `H`, and the bit
  length;
- the matrices have polynomial dimensions in `Q`, so kernel, image, and
  tracked-preimage calculations are polynomial;
- a basis preimage selects at most `Q` bridges, so its exact product has
  `O(Q(n+log H))` bits; exact square root, modular inverse, and gcd tests are
  polynomial in that size.

Consequently a polynomial in `Q`, `H`, and `n+log H` is quasipolynomial in
`n` after substituting (11).  Also `log H=(log n)^{O(1)}=o(n)`, while
`log N=Theta(n)`, so `H^4 <= N` eventually holds.  The complexity claim is
valid in the compact-basis sense above.  Literal enumeration of every
kernel vector or every normalized root would, in general, require
exponential output and is not what the stated basis algorithm does.

## 7. Exact defect in (12)

For anchors `a_1,...,a_L <= H`, the only implication supplied by the upper
bound is

\[
\prod_{i=1}^L a_i\leq H^L.
\]

Therefore

\[
\prod_{i=1}^L a_i>\sqrt N
\quad\Longrightarrow\quad
L>\frac{\log N}{2\log H}.
\tag{F}
\]

This is a **necessary** magnitude condition.  The converse does not follow:
the legal anchors can all be strictly smaller than `H`.  Even the envelope
`H^L` only equals, rather than exceeds, `sqrt(N)` when equality holds in
(12).

An admissible concrete counterexample is `N=81` and `H=3`.  Then `N` is odd
and `H^4=N`.  The only integer anchor with `1<a<=H` that is a unit modulo
`N` is `a=2`; `a=3` is not legal.  Formula (12) permits `L=2`, because

\[
\frac{\log 81}{2\log 3}=2,
\]

but the product of two legal anchors is at most `2^2=4<9=sqrt(81)`.
Thus length (12) does not make the P131 threshold reachable in the stated
grammar.

A correct replacement is (F).  If one additionally assumes that anchors
equal to `H` are legal and selectable at every step, then the sufficient
integer condition is

\[
L>\frac{\log N}{2\log H},
\qquad\text{equivalently}\qquad
L\geq\left\lfloor\frac{\log N}{2\log H}\right\rfloor+1.
\]

The numerical threshold is polynomial in `n` when `H=n^{O(1)}` (and also
when `H` is any fixed integer at least two), but that asymptotic fact does
not supply suitable legal anchors.

## 8. Scope check

The proved content is conditional and source-local:

- it contains every already-existing wrapped cycle in the enumerable core;
- it does not prove that any wrapped cycle exists;
- it exactly represents and tests bridge dependencies supported on that
  core;
- it does not force a nonzero kernel, survival after equality-class parity,
  or a non-global normalized root;
- it preserves frozen named generators and uses refinement only to decode
  their integer square classes;
- it says nothing about a grammar that creates and follows new aggregate
  generators;
- without the final positive theorem (or a suitable density theorem), it is
  not an all-input factoring algorithm.

Those scope limitations are internally consistent.  The only false
mathematical assertion found is the sufficiency/reachability wording of
(12), including its non-strict boundary.
