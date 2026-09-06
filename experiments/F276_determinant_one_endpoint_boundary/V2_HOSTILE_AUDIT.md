# F276 V2 hostile proof audit

## Verdict

**PASS.** I found no counterexample to the claims in the authenticated V2
statement and proof. The conclusions stay within their declared hypotheses.
In particular, V2 does not claim that the constant-power lane is signal-free.

## Authentication

I authenticated the frozen packet before reading its mathematical claims.

- `V2_FROZEN.sha256`:
  `c7af4315d87f4e99a223cf6a30406a71288a55b7a3d3c835cd41aac0cff3f6e8`
- `V2_STATEMENT.md`:
  `bea005ed8c16878fdb334c12e01f55b4b6569294662e274121e8d1b396f65fea`
- `V2_PROOF.md`:
  `8164f562ec33a6ab4fe9cedf3345a2917c5cba7545d64dbb4e1e6f957b51bd62`

`shasum -a 256 -c V2_FROZEN.sha256` returned `OK` for every entry:

- `V2_STATEMENT.md`
- `V2_PROOF.md`
- `V2_SELF_AUDIT.md`
- `V2_PROVENANCE.md`
- `V2_MANIFEST.md`
- `FROZEN.sha256`

## Hostile checks

### Endpoint cocycle and gauge

The multiplication order is correct. Substitution
`(X,Y,Z)=(x_0,X,Y)` gives

\[
P(X,Y)P(x_0,X)=P(x_0,Y),
\]

so right multiplication by `P(x_0,X)^{-1}` gives
`P(X,Y)=G(Y)G(X)^{-1}`. An admissible `x_0` exists because only finitely
many nonzero coefficient polynomials and the specialized determinant must be
avoided, and a characteristic-zero field is infinite. The converse cancels
in the same order. Integer endpoint identities lift after denominators are
cleared because the admissible integer endpoint tuples are Zariski dense.

### Separable length law

The semigroup order `H_{r+s}=H_sH_r` matches adjacent interval composition.
Taking `s=1` gives `H_{m+1}=H_1H_m`, hence `H_m=C^m`. The one-step and interval
formulas follow with the stated factor order.

For determinant one,

\[
1=\det(C)\frac{\det G(X+1)}{\det G(X)}.
\]

The rational-function quotient has leading ratio one at infinity. Thus
`det(C)=1`. A characteristic-zero rational function with period one is
constant, so `det G(X)` is a nonzero field constant. This is exactly a
constant-matrix-power alias. It is not a claim that signals in `C^m` cannot
exist.

### Polynomial unimodularity and specialization

For `U in GL_d(R)`, with `R=K[X]` or `Z[X]`, `det U` is a constant unit.
Therefore the shifted conjugate

\[
M(X)=U(X+1)^{-1}A(X)U(X)
\]

has determinant one. Its first column is `(lambda,0,...,0)^T`; determinant
expansion makes `lambda` a unit. Over `Z[X]`, it is exactly `+1` or `-1`.

The coordinate-ideal proof is valid over every commutative ring because both
`M` and `M^{-1}` have ring entries. Specializing a polynomial `SL_d(Z[X])`
transition at an integer gives an integer unimodular matrix, so every product
preserves the coordinate ideal. A primitive state, row, or column cannot gain
a common hidden-prime divisor. The theorem does not exclude a divisor in one
selected coordinate, as V2 states.

### Affine `SL_2` classification and basis endpoints

Coefficient comparison in `det(C+XD)=1` gives `det C=1`, `tr(C^{-1}D)=0`, and
`det(C^{-1}D)=0`. Since `C^{-1}` is integral, `B_0=C^{-1}D` is integral, and
Cayley-Hamilton gives `B_0^2=0`.

A nonzero `B_0` is rationally conjugate to `E_12`. This is not generally an
integral unimodular conjugacy. More precisely, an integral unimodular basis
puts it in the form `nE_12` for some nonzero integer `n`; for example,
`2E_12` cannot be integrally conjugated to `E_12`. A rational rescaling then
normalizes `n` to one. V2 claims only rational conjugacy and does not claim
that this basis change preserves integral coordinates or modular units.
Therefore an endpoint implementation must audit its fixed denominators under
the stated `UNIT` rule.

The branch boundary is intrinsic. After normalization to `E_12`, any second
normalizing basis differs by a matrix commuting with `E_12`; such a change
preserves whether the lower-left entry `c` of the conjugated `C` is zero.
Equivalently, `c=0` says that `C` preserves the common image/kernel line of
`B_0`.

Direct elimination from

\[
x_{k+1}=a x_k+(ak+b)y_k,\qquad
y_{k+1}=c x_k+(ck+d)y_k
\]

gives

\[
y_{k+2}=(ck+a+c+d)y_{k+1}+(bc-ad)y_k
       =(ck+a+c+d)y_{k+1}-y_k.
\]

Thus `c=0` is the upper-triangular constant-power/geometric-sum branch, while
`c!=0` has a genuinely varying affine continuant coefficient. In the integral
normal form `nE_12`, the coefficient is
`cnk+a+cn+d`; this confirms that the same zero/nonzero boundary survives
without rational normalization.

### Search scope and the corrected signal statement

V2 distinguishes a reduction from a signal impossibility:

- It proves that the easy affine branch reduces to constant powers and
  geometric-weighted sums.
- It says only that this packet supplies no `SIGNAL` theorem for that branch.
- It explicitly leaves open a constant-power candidate with its own exact
  all-input signal law.
- It gives no lower bound or impossibility theorem for the generic affine
  continuant, higher degree or dimension, semilinear states, implicit large
  states, or special fast endpoint identities.

The no-search disposition is therefore conditional: the listed reductions
alone do not justify a resource-bearing interval-product scan. It does not
exclude a separately specified constant-power search with an exact signal law
and a numerical-quasipolynomial endpoint operation.

## Final result

No exact counterexample was found. The authenticated V2 correction closes the
V1 overclaim while preserving the proved algebraic boundaries.
