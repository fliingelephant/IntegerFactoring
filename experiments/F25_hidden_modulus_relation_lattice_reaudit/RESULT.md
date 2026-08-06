# Fresh hostile re-audit of revised F25

**Artifact audited:** `experiments/F25_hidden_modulus_relation_lattice/RESULT.md`.

**Prior audit consulted:** `experiments/F25_hidden_modulus_relation_lattice_audit/RESULT.md`.

**Audit type:** fresh symbolic re-audit of the substantively revised theorem.

**Computation:** none.

## Verdict in brief

The revised theorem passes. Its central conclusion is now narrow enough for
the proofs: adding samples does not create a high-dimensional advantage in
the displayed public zero-syndrome Construction-A kernel, fixed-output
coefficient/Gram presentation, Hurwitz block sum, or below-threshold graph
slice. The report no longer transfers that conclusion to the public output
lattice, the scaled dual lattice, a faithful fixed-rank quotient decoder,
biased targets, or nonlinear sample-combining maps.

The two substantive defects found by the prior audit have been repaired:

1. the projected covolume calculation now uses general rational rank ρ and
   common local rank u, rather than silently assuming u = ρ; and
2. the public output, scaled-dual, and fixed-rank metric lattices are derived
   correctly and explicitly left open.

I found no new mathematical error. Two wording clarifications are useful but
do not change the theorem: display the Hurwitz basis literally as
`{1, i, j, (1+i+j+k)/2}`, and repeat the hypothesis `x ∈ J_r(α)` in the
graph threshold conclusion.

## 1. Construction-A indices, CRT, and rank separation

For an integer matrix `A ∈ ℤ^(t×d)`, put

    K_r(A) = {x ∈ ℤ^d : Ax ≡ 0 mod r},
    s_r = rank over F_r of A mod r.

Reduction onto `im(A mod r)` has kernel `K_r(A)`, so

    [ℤ^d : K_r(A)] = r^(s_r).

For distinct primes p and q, CRT gives, without an independence assumption,

    K_pq(A) = K_p(A) ∩ K_q(A),
    [ℤ^d : K_pq(A)] = p^(s_p) q^(s_q).

The determinantal-divisor separator is exact. If `s_p < s_q`, take
`k = s_q`. Some k-minor is nonzero modulo q, so the integer determinantal
divisor `δ_k(A)` is nonzero and not divisible by q, while all k-minors
vanish modulo p. Therefore

    gcd(N, δ_k(A)) = p.

The other ordering is symmetric. One need not know k in advance: SNF
computes all relevant determinantal divisors, and polynomially many gcd
tests suffice. Unequal local ranks are therefore a direct SNF-minor
factorization event, not a metric gain.

The useful set

    (K_p ∖ K_q) ∪ (K_q ∖ K_p)

is not additive. The subgroup lemma used in F25 is valid: a subgroup
contained in `U ∪ V` lies in one branch, since otherwise the sum of one
element from each branch lies in neither. This proves only the claimed
homogeneous linear-encoding obstruction. It does not constrain a larger
public lattice followed by nonlinear postprocessing, and the revision does
not claim that it does.

## 2. Exact-kernel projection and the general (ρ,u) formula

Put

    ρ = rank over ℚ of A,
    K_0 = kernel of A in ℤ^d.

The quotient `ℤ^d / K_0 ≅ Aℤ^d` is torsion-free, so `K_0` is primitive
and has rank `d − ρ`. Let π be orthogonal projection onto the orthogonal
complement of the real span of `K_0`, and let `Δ_0` be the covolume of
`K_0` in its span.

Primitivity supplies a basis of `ℤ^d` extending a basis of `K_0`.
Orthogonal volume decomposition then gives

    det π(ℤ^d) = 1 / Δ_0.

There is no missing projection index. Since

    (real span of K_0) ∩ ℤ^d = K_0

and `K_0 ⊆ K_r(A)`, projection identifies

    ℤ^d / K_0  ≅ π(ℤ^d),
    K_r(A) / K_0 ≅ π(K_r(A)).

Consequently,

    [π(ℤ^d) : π(K_r(A))] = [ℤ^d : K_r(A)] = r^(s_r).

The corrected covolumes are therefore

    det π(K_p) = p^(s_p) / Δ_0,
    det π(K_q) = q^(s_q) / Δ_0,
    det π(K_N) = p^(s_p) q^(s_q) / Δ_0.

In the unseparated equal-rank case `s_p = s_q = u ≤ ρ`, all three
projected lattices have real rank ρ, and their determinant-root scales are

    p^(u/ρ) Δ_0^(−1/ρ),
    q^(u/ρ) Δ_0^(−1/ρ),
    N^(u/ρ) Δ_0^(−1/ρ).

Only `u = ρ` permits the simplification to p, q, and N times the common
factor. The revision states this and records the relevant multiplication-map
case `(ρ,u) = (4,2)`.

If `ρ = 0`, then `A = 0`, all three kernels are `ℤ^d`, and there is no
syndrome. This correctly handles the otherwise undefined root exponent.

For a scalar coefficient map or the displayed fixed-output quaternion map,
the informative quotient rank is at most four. More samples can change
`Δ_0`, but that factor occurs in every local and public covolume. This
removes the claimed dimension-amortized determinant gain. It does not control
the shape or optimizer of the resulting fixed-rank metric, which the revision
correctly leaves open.

## 3. CVP coset invariance and rank-zero cases

If `v ∈ K_N(A)` and `e = t − v`, then for each `r ∈ {p,q}`,

    e ∈ K_r(A)  if and only if  t ∈ K_r(A).

This is independent of whether v is exact closest, approximate closest,
shortest, or selected by another rule inside `K_N`. Subtracting an
intersection vector cannot manufacture a vanishing local syndrome.

For a target uniform modulo N, CRT makes its p- and q-residues independent.
The exact symmetric-difference probability is

    p^(−s_p) + q^(−s_q) − 2 p^(−s_p) q^(−s_q).

On balanced semiprimes this is exponentially small in `log N` when both
local ranks are positive. The revision handles every zero-rank case:

- if `s_p = 0 < s_q`, the success probability is `1 − q^(−s_q)`, but
  the rank mismatch has already exposed p;
- `s_q = 0 < s_p` is symmetric; and
- if `s_p = s_q = 0`, then `A ≡ 0 mod N`, all three kernels are
  `ℤ^d`, and the symmetric difference is empty.

The report does not extend this calculation to a deliberately biased target
distribution.

## 4. Public output and scaled-dual lattices

The revision correctly separates two public lattices from the kernel
intersection theorem. For

    Λ_out = Aℤ^d + Nℤ^t,

reduction modulo N gives

    ℤ^t / Λ_out ≅ (ℤ/Nℤ)^t / im(A mod N),

and hence

    det Λ_out = p^(t−s_p) q^(t−s_q).

The composite-modulus dual identity also survives direct checking. Let

    L = ℤ^d + (1/N) Aᵀℤ^t.

For `x ∈ K_N(A)`, every element of L pairs integrally with x, so
`L ⊆ K_N(A)*`. Modulo `ℤ^d`, the first lattice has

    |L / ℤ^d| = |im(Aᵀ mod N)| = p^(s_p) q^(s_q).

The last equality is valid over the squarefree composite `N = pq`: CRT
reduces it to two fields, and transpose preserves rank over each field.
Thus

    det L = 1 / (p^(s_p) q^(s_q)) = det K_N(A)*,

so the inclusion is equality. Scaling by N gives

    Λ_dual = N K_N(A)* = Nℤ^d + Aᵀℤ^t,
    det Λ_dual = p^(d−s_p) q^(d−s_q).

Neither lattice is a sublattice of the coefficient kernel in the sense
needed by the coset argument. The check `A = (1)`, where
`K_N = Nℤ` but `N K_N* = ℤ`, correctly prevents that transfer. The
revision makes no shortest-vector, closest-vector, or extraction assertion
for either public lattice.

The same restraint appears in the Gram quotient. With fixed
positive-definite T,

    G = CᵀTC,
    kernel over ℚ of G = kernel over ℚ of C,
    rank over ℚ of G ≤ 4.

Quotienting its exact zero directions identifies the metric with reduced
norm on the public image lattice `Cℤ^m`, of rank at most four. Exact
SVP/CVP for a specified rational lattice and target in fixed dimension is
polynomial in the input bit length. F25 correctly treats this as a tractable
but open decoder, not as an obstruction or a factoring algorithm.

## 5. Hurwitz multiplication, ideals, and minima

Assume `N = pq` for distinct odd primes and `nrd(α) = N`. In a Hurwitz
basis, left multiplication satisfies

    det M_α = N²,
    Q(M_α x) = N Q(x).

Modulo either `r ∈ {p,q}`, α is nonzero; otherwise `α ∈ rℋ` would force
`r² | N`. The odd local Hurwitz algebra is `M₂(F_r)`, where the nonzero
determinant-zero image of α has matrix rank one. Left multiplication by a
rank-one 2 by 2 matrix has rank two on the four-dimensional matrix algebra.

It follows that precisely two Smith invariants are divisible by p and
precisely two by q. Their total valuations are two at each prime, and the
invariant-factor divisibility chain puts both primes in the last two
positions. Thus

    SNF(M_α) = diag(1,1,N,N).

For

    J_r(α) = {x ∈ ℋ : αx ∈ rℋ},

the local rank calculation gives index r², and `J_r` is a right ideal. The
revised principality proof has the correct handedness. Choose nonzero d of
minimum norm in a right ideal I. The one-sided norm-Euclidean theorem gives
`h ∈ ℋ` with

    nrd(d⁻¹x − h) < 1.

Then `x − dh ∈ I` because `dh ∈ I`, and

    nrd(x − dh) = nrd(d) nrd(d⁻¹x − h) < nrd(d).

Minimality forces `x = dh`. Hence `I = dℋ`, in particular
`J_r = d_rℋ`. Since

    [ℋ : d_rℋ] = nrd(d_r)² = r²,

one has `nrd(d_r) = r`. Units attain norm one, so

    λ₁(J_r) = √r.

For the public modulus, cancellation in the rational quaternion division
algebra gives

    J_N(α) = conjugate(α)ℋ = J_p(α) ∩ J_q(α),

with index N², Gram matrix N times the fixed Hurwitz Gram, and

    λ₁(J_N) = √N.

The direct-sum formulas follow: local determinant roots remain √p and √q,
while the public root remains √N regardless of the number of blocks.

A supplied basis of `J_r` already reveals `r = √[ℋ : J_r]`. Conversely,
if a nonzero `x = conjugate(α)y ∈ J_N ∩ rℋ`, then
`r² | Q(x) = NQ(y)`, so `r | Q(y)` and `Q(x) ≥ Nr`. This validates the
coordinate-divisibility lower bound and the constant-dimensional LLL
comparison after trial division by the fixed small primes.

## 6. Graph lattice and its threshold quantifier

For integer-cleared positive weights a and b, the graph lattice has block
basis

    [ aI_d     0   ]
    [  bA   −bNI_t ],

so

    det Γ_(a,b) = a^d (bN)^t.

For one 4 by 4 multiplication block, its eighth determinant root is
`√(abN)`, unchanged by direct sums. On the unwrapped slice `z = 0`,

    a²Q(x) + b²Q(M_α x) = (a² + b²N) Q(x),

so a nonzero local-kernel input is at least √r times the unit baseline.

The wrapped threshold statement is correct with its local-kernel hypothesis
made explicit:

> If `x ∈ J_r(α)` and `s = M_αx − Nz`, then `s ∈ rℋ`. Therefore a
> nonzero s has `√Q(s) ≥ r`; if instead `√Q(s) < r`, then `s = 0` and
> `x ∈ J_N(α)`.

Residual length below r does not force `s = 0` for an arbitrary x outside
`J_r`. The candidate introduces s as the residual “of a local-kernel
vector,” so its mathematical claim has the correct conditional scope.
Repeating `x ∈ J_r` in the concluding sentence would remove any literal
misreading.

Above the threshold, the report asserts only that local divisibility gives no
automatic saving. It explicitly leaves other weights, targets, affine shifts,
and postprocessors open.

## 7. Bit complexity and relation to P19/P30

For polynomially many samples with `O(log N)`-bit coordinates, all displayed
generator matrices have polynomial dimensions and polynomial-bit entries.
Their determinant values can be exponential, but their bit lengths are
polynomial:

- `log det K_N(C) ≤ 4 log N`;
- the block determinant has `O(m log N)` bits;
- the graph determinant has polynomial bit length for polynomial-bit
  weights; and
- the output and dual generators and determinants have
  `O((d+t) log N)` bit size.

Integer HNF/SNF, rational kernel/projection arithmetic, LLL, gcd, norm, and
division checks are polynomial-bit operations on these inputs.
Growing-dimensional exact SVP/CVP is not silently included.
Fixed-dimensional exact SVP/CVP is correctly limited to the
rank-at-most-four quotient.

The comparisons with the promoted boundaries are accurate. P19 uses exact
CVP only after encoding the nonlinear Boolean multiplication witness and
does not supply a polynomial exact-CVP algorithm. P30 rules out specified
pairwise projective collision tests for the residual-only source, but does
not bound abundant many-sample linear relations or nonlinear combinations.
F25 imports no conclusion beyond those scopes and claims no top-level
factoring algorithm.

## Nonblocking editorial points

1. “Fix a ℤ-basis” should preferably display
   `{1, i, j, (1+i+j+k)/2}`. The current ring-generation notation is
   recognizable but is not a literal four-element basis.
2. The graph threshold should repeat `x ∈ J_r(α)` in the final implication.
3. Hurwitz-ideal determinants are indices/covolumes relative to the fixed
   Hurwitz coordinate lattice. Absolute Euclidean covolumes differ by a fixed
   normalization factor; every ratio and N-dependent scale is unaffected.

None changes a formula, a quantifier in the proved theorem, or a scope
boundary.

## Final disposition

**PASS.**

The revised F25 is suitable for strict proof-blind reconstruction. That is
the next required verification step; this hostile audit alone does not make
the result verifier-backed.
