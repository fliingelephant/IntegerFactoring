# F217 provenance

## Namespace

Before creation, a repository-wide search found no F217 entry in the
durable ledgers, notes, or experiment tree.

## Source question

On the balanced beta-two branch,

\[
N=pq=2K+1,\qquad
p<q<2p,\qquad
N\equiv3\pmod4,
\]

the factorization of \(K\) is granted and the hidden factors form an
inverse pair in

\[
G=(\mathbb Z/K\mathbb Z)^\times.
\]

P187 showed that the full complex character-trace family separates the
inversion orbit, but exposed each trace as the unevaluated divisor
coefficient

\[
\sum_{d\mid N}\chi(d)
=2+\chi(p)+\chi(p)^{-1}.
\]

The new question was whether the special moving relation
\(N=2K+1\) makes the trace output compressible or converts the same
additive target into an exact Eisenstein, modular-symbol, Hecke,
Lambert-product, or representation-theoretic evaluator.

Two cautions shaped the result.

1. Generic ring operations can preserve information that scalar complex
   characters lose. A negative argument restricted to scalar characters
   is not a boundary for ring-valued evaluation.
2. A fixed-ratio recursive contraction is not necessary for one
   near-size chain. A recurrence

   \[
   T(n)\le T(n-1)+\operatorname{QP}(n)
   \]

   remains QP. Branching, rather than one-bit shrinkage alone, is the
   relevant cost risk.

## Material result

F217 separates decoding from evaluation.

1. Under a fully explicit and certified cyclic coordinate system, at most
   \(2r-1\le2n-1\) scalar traces align every coordinate sign and recover
   the inverse orbit. This removes the full character table and
   high-degree algebraic output as necessary decoder costs.
2. The cyclic coordinate system, its inverse map, and the trace evaluator
   remain explicit premises. F217 does not infer them from
   \(\operatorname{factor}(K)\).
3. The tautological ring character maps the universal group-algebra
   divisor coefficient to the exact residue

   \[
   \sigma_1(N)\equiv2+p+q\pmod K.
   \]

   This is the direct ring-valued answer to the generic-ring concern.
4. With the exact moving weight

   \[
   k=\varphi(K)+2,
   \]

   the arithmetic-normalized level-one Eisenstein coefficient obeys

   \[
   [q^N]\mathcal G_k
   =\sigma_{k-1}(N)
   \equiv\sigma_1(N)\pmod K.
   \]

5. When \(K=r\) is prime, the eta quotient

   \[
   \eta(\tau)^r/\eta(r\tau)
   \]

   is modular in the stated prime-level scope and its coefficient modulo
   \(r^2\) yields the same residue.
6. A twisted Ramanujan expansion proves that the first explicit
   factor-sensitive multiplier is exactly \(p\). This is a boundary for
   termwise summation, not for compressed tails.
7. Standard dense Hecke, Manin-symbol, moving-weight, and \(q\)-truncation
   models have numeric-exponential state or iteration counts. These are
   named-model boundaries only.

The core unresolved task is one random-access exact divisor-coefficient
evaluator with QP same-node work.

## Closest prior routes and material difference

- F215, promoted as P187, proves the inverse-Frobenius boundary for scalar
  abelian reciprocity, a full-family Fourier separation theorem, and the
  divisor-coefficient formulation. F217 does not repeat the scalar
  reciprocity boundary. It proves that a linear-size adaptive trace bank
  is sufficient under an explicit coordinate premise, then develops
  moving-level ring and modular coefficient targets.
- F203, promoted as P179, gives the fixed \(\chi_4\)-twisted divisor
  selector for the beta-two next-bit gate. F217 uses characters modulo
  the moving level \(K\) and targets the whole inverse orbit or
  \(\sigma_1(N)\bmod K\); it does not repeat the fixed-level selector.
- F204, promoted as P181, proves boundaries for the binary q-product norm,
  scalar modular monomials, fixed-base Mahler equations, and fixed
  root-of-unity norms. F217's prime-\(K\) eta quotient has moving prime
  exponent and level and is audited separately.
- F206, promoted as P182, treats finite-dimensional vector completion and
  the natural Whittaker pair for the fixed \(\chi_4\) route. F217 does not
  reopen that fixed-level completion. Its representation statement is
  limited to representations factoring through the moving abelian group
  \(G\).
- F193, promoted as P170, records narrow state and evaluator boundaries for
  standard modular-symbol and representation models. F217 adds exact
  moving-weight and moving-level coefficients tied to
  \(N=2K+1\), and carefully distinguishes the small output residue from
  the large standard numeric state.
- The earlier \(\sigma_1(N)\) Eisenstein target identifies the general
  additive factor sum. F217's new contribution is the moving congruence
  \(\sigma_{\varphi(K)+1}(N)\equiv\sigma_1(N)\pmod K\), together with
  the exact small exception and output-state audit.

## Choices fixed before freeze

1. The Eisenstein weight is

   \[
   k=\varphi(K)+2.
   \]

   This gives the exponent \(k-1=\varphi(K)+1\), so Euler's theorem
   reduces every divisor power to the divisor itself modulo \(K\).
2. The Eisenstein normalization is stated explicitly. Only its integral
   positive-index coefficient is reduced modulo \(K\); the Bernoulli
   constant is not.
3. The trace theorem treats a certified cyclic decomposition and both
   coordinate maps as premises. No consequence from
   \(\operatorname{factor}(K)\) is implied.
4. The eta claim is restricted to prime \(K=r>3\), and actual semiprime
   inputs have \(r\ge7\). Both cusp conditions and the coefficient
   congruence modulo \(r^2\) are proved.
5. The Ramanujan identity is first stated only for \(\Re(s)>0\). The
   unweighted nonprincipal boundary is an Abel limit, not an
   ordinary-convergence assertion.
6. The exceptional residue case \(N=15\) is isolated and handled by
   trial division.
7. Standard numeric state, unrestricted exact coefficient output, binary
   parameter encoding, and requested modular-residue output are four
   distinct cost notions throughout the packet.

## Mathematical dependencies

1. Character duality for a finite abelian group.
2. Elementary trigonometric identities, sine separation, and certified
   binary search.
3. Euler's theorem and the prime-factor formula for \(\varphi(K)\).
4. The standard Fourier expansion of the holomorphic level-one Eisenstein
   series.
5. The Dedekind eta transformation and the eta-quotient transformation
   congruences.
6. Formal binomial expansion modulo a prime square.
7. The Euler product for a Dirichlet \(L\)-function in its absolute
   convergence half-plane.
8. The divisor formula for Ramanujan sums.
9. Standard upper-triangular Hecke representatives and the standard
   Manin-symbol index.

No smoothness assumption, distribution theorem, random-character
independence, unproved analytic continuation claim, or hidden coefficient
oracle is used as proof.

## Computation and evidence

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, or numerical fit was performed. The result is
proof-only. Targeted retrieval was limited to the local predecessor packets
listed above. Hashing is used only to freeze this packet.

## Ledger policy

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, or process-lessons file is edited by
this packet.
