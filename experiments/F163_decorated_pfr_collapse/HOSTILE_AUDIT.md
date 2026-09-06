# Hostile audit of F163

## Verdict

**PASS, with the scope in the frozen statement.**

F163 proves an exact obstruction for additive-combinatorial processing of the
P138 decorated binary group on its no-factor branch. It does not prove an
obstruction for algorithms that use the integer presentations, canonical
carries, block incidences, sizes, provenance, or an external source of
decorated lifts.

## Frozen inputs

The files audited in full have these SHA-256 hashes:

- `STATEMENT.md`:
  `82ff2a0fef918e3c4e992ca70b334656fcd661146e4b61dac7c871c0216dbd95`
- `PROOF.md`:
  `534f1e4903b76c63f79d6e13e4f5dd64952fa6a94aaf811604cd027220c41007`
- `MANIFEST.md`:
  `d695d645220d80afe0df62292b4054f58890933178608258184351b31279c581`

These hashes agree with the superseding freeze supplied for the audit.

## Attacks and results

### 1. The split-or-isomorphism step is exact

For `H=<A>` and `W=pi(H)`,

\[
\ker(\pi|_H)=H\cap K.
\]

If this intersection contains a nonzero class, a parity dependency gives a
square root of one that is not globally `+1` or `-1`. For odd `N`, the
standard gcds give a proper factor. If the intersection is zero, `pi|_H` is
injective and is surjective onto `W` by definition. It is therefore an
isomorphism.

The inverse is public. Binary elimination can retain one decorated lift for
each parity-basis vector. A public coordinate expression in that basis gives
the unique lift. Root-aware deduplication is necessary here and is stated
explicitly. Parity-only deduplication could destroy the kernel witness, but
F163 does not permit it.

### 2. All intrinsic additive structure collapses to parity

Every iterated sumset of `A` is contained in `H`. Since `pi|_H` is a group
isomorphism, its restriction gives

\[
kA \simeq k\pi(A)
\]

for every `k`. The same argument preserves every additive-word equality,
additive energy, affine subspace, subgroup coset, and intrinsic cover. An
ambient coset or subspace can be intersected with `H`; a nonempty
intersection is a coset of the corresponding intersection subgroup.

Thus a PFR routine that sees only this decorated additive group cannot obtain
a hidden-root direction after the P138 consistency test has returned the
section branch. This conclusion does not cover a routine with an oracle for
ambient kernel directions or with access to richer integer data. The frozen
statement preserves this boundary.

### 3. The large-doubling examples are valid

For

\[
B_1=\{h(0),h(e_1),\ldots,h(e_d)\},
\]

the pair sums are exactly zero, the `d` basis vectors, and the
`binom(d,2)` distinct weight-two vectors. Hence

\[
|B_1+B_1|=1+d+\binom d2.
\]

The basis elements already generate all of `h(W)`, so this cardinality
growth does not enlarge the generated subgroup.

For Hamming balls, a vector of weight at most `min(s+t,d)` can split its
support into parts of sizes at most `s` and `t`, and the reverse inclusion is
the triangle inequality for Hamming weight. Therefore

\[
B_s+B_t=B_{\min(s+t,d)}.
\]

All these points remain in the same public section.

### 4. The doubling-one examples are valid

Linearity in characteristic two gives

\[
h(U)+h(U)=h(U)
\]

for every subspace `U`. If `u` is not in `U`, the affine coset omits the
identity and satisfies

\[
h(u+U)+h(u+U)=h(U).
\]

The cardinalities agree. No kernel direction appears.

### 5. The canonical-inverse realization is exact

The CRT classes in (8) are units modulo `N`. Dirichlet's theorem supplies
infinitely many primes in each class, so finitely many distinct primes
`ell_j` can be selected. Distinct prime blocks are pairwise coprime and have
independent rational square classes.

Equation (9) gives `z_j^2 = ell_j mod N`. Since the projected generators are
the independent basis vectors `e_j`, their generated decorated subgroup has
zero projection kernel and is a section.

For a section root `z_v`, the least positive inverse `s_v` satisfies
`s_v z_v = 1 mod N`. Hence

\[
T_v=s_v^2Q(v)=1\pmod N,
\]

and the supplied root `alpha_v=1` is legal. Its decorated root is

\[
\alpha_v s_v^{-1}=z_v\pmod N.
\]

Thus these records realize the claimed section exactly.

This is a P142 section-completion realization. The values are **not claimed
to be the raw two-endpoint products** `z_v iota_N(z_v)`. This distinction is
mathematically material and is stated correctly in both the statement and
the proof.

### 6. The endpoint screens are genuinely null

For nonzero `v`, write `k=sum_j v_j 2^j`. Modulo either hidden prime,

\[
Q(v)=a^{2k},
\qquad
0<2k<(r-1)/2.
\]

The primitive-root exponent is therefore neither the exponent of `+1` nor
that of `-1`. Neither hidden prime divides `Q(v)-1` or `Q(v)+1`.
Consequently both gcds are one. Since

\[
z_v\mp s_v=s_v(z_v^2\mp1)\pmod N
\]

and `s_v` is a unit, the two endpoint gcd identities in (11) follow.

The construction uses the hidden factors and primitive roots. It proves
realizability of a null structural model. It is not a public source from
bare `N`. F163 states this limitation.

## Defects found

No mathematical defect was found in the frozen theorem or proof.

No claim was verified beyond the stated boundary. In particular, this audit
does not establish a lower bound for PFR on exact integer values, carries,
block refinements, magnitude data, or provenance. It also does not establish
a factoring algorithm, an all-input source theorem, or a prior-art novelty
claim.
