# F220 provenance

## Source question

The user asked whether several independently obtained, gcd-certified order
contributions can be accumulated until a supplied dyadic factor residue
reaches the Gao--Feng--Hu--Pan arithmetic-progression terminal. The requested
analysis also had to identify the weakest exact Las Vegas progress condition
and test it against bounded-gap and single-cyclic-direction witness sources.

The key refinement was to work one primary component at a time. A witness
does not need to have equal complete orders in every hidden local group. For
each \(\ell^{e_\ell}\parallel A\), the public conjunction

\[
a^A\equiv1\pmod N,
\qquad
\gcd(a^{A/\ell}-1,N)=1
\]

already certifies \(\ell^{e_\ell}\mid r-1\) for every rational prime
\(r\mid N\). Different witnesses can therefore contribute different
primary blocks, which are combined by lcm.

## Material result

F220 separates four logically different layers.

1. **Primary contribution.** The factored annihilator and one gcd-one test
   certify one full primary block universally across the hidden rational
   primes. Exact equality of whole local orders is unnecessary.
2. **Aggregate terminal.** If \(M\) is the lcm of certified blocks and
   \(p\bmod 2^t\) is supplied, generalized CRT gives
   \(p\bmod L\) for \(L=\operatorname{lcm}(2^t,M)\). A preliminary gcd
   handles \(L>p\); otherwise the imported GFHP terminal applies once
   \(L\ge N^{1/4}/\operatorname{QP}(n)\).
3. **Progress criterion.** The exact potential is the remaining binary
   logarithmic distance from the target modulus. Uniform positive
   conditional drift is sufficient for almost-sure termination and expected
   numerical-QP cost. Conditional inverse-QP mass of a factor or strict lcm
   growth is equivalent up to an \(O(n)\) factor.
4. **Source laws and ceilings.** For a CRT-uniform unit and a factored
   annihilator coprime to \(N\), F220 derives the exact no-progress law,
   including all four \(f_\ell(L)\) cases. Independently of the source,
   every aggregate is bounded by
   \(D_N=\gcd_{r\mid N}(r-1)\). Bounded-gap semiprimes and synchronized
   cyclic sources show why independence by itself cannot prove the needed
   drift.

The deterministic terminal is complete under its premises. The unresolved
claim is a witness-source theorem that gives inverse-QP conditional useful
mass on every nonterminal input and state.

## Closest local predecessors and exact differences

- F178, promoted as P160, supplies a factored exact-common-order state on one
  exit from coprime-order normalization. That state is an admissible F220
  block. Its surviving hard-branch theorem permits unequal local orders and
  does not supply a factored common annihilator or an acquisition law.
- F187, promoted as P165, gives exact order-stripping and uniform-root data
  for the fully factored \(N-1\) route. F220 weakens the certificate from
  equality of complete local orders to separate universal primary blocks,
  derives the resulting exact four-case probability kernel, and combines it
  with a dyadic modulus. P165's bounded-gap family still rules out an
  all-input inverse-QP progress bound for its uniform source.
- F198, promoted as P175, supplies the audited GFHP arithmetic-progression
  interface after low factor bits are known. F220 does not reproduce the
  carry evaluator. It accepts the residue \(p\bmod2^t\), merges it with
  order certificates by generalized CRT, and exposes the precise lcm
  threshold.
- `PROMPT.md` supplies the top-level factoring objective and numerical-QP
  cost convention. F220 remains a conditional terminal, not a solution of
  that objective.

The local source hashes used for this comparison are:

- `PROMPT.md`:
  `a4a85d0fc0cc540af7d2ab410dc8d7b6e6bf8a72dc2037509cb0999ddc9ee938`;
- `experiments/F178_coprime_order_normalization/STATEMENT.md`:
  `8a7cfbc7ea7d3fd2d0df3c31bbd540b9c3ae7a7b62dde2997b143135e5ae6ca4`;
- `experiments/F187_fully_factored_nminus1_sampling/STATEMENT.md`:
  `9434188bf8c35cbd54d0f6f553b7e0698f19470745515bb1fe503fbe8b67f14e`;
- `experiments/F198_beta2_carry_inverse_lowbits/STATEMENT.md`:
  `244e44b2d93fe6f62ef2ceb161b67132a12d3741a54a6ff80a2930e438dce0bb`.

## Mathematical dependencies

1. Lagrange's theorem in \(\mathbb F_r^\times\).
2. The generalized Chinese remainder theorem and extended Euclid.
3. The Gao--Feng--Hu--Pan arithmetic-progression factoring interface as
   frozen in P175.
4. Cyclicity of \((\mathbb Z/r^f\mathbb Z)^\times\) for odd \(r\), CRT,
   and the primary decomposition of finite cyclic groups.
5. Stopped telescoping for a bounded nonnegative additive-drift potential.
6. The standard bounded-prime-gap theorem, only for the existence of an
   infinite bounded-gap semiprime family. Every fixed-pair ceiling and
   probability estimate is elementary.

No heuristic independence of hidden CRT components, smoothness assumption,
prime-tuple conjecture, or unproved witness distribution is used.

## Computation and evidence

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. The packet
is proof-only. Hashing is used only to identify source files and freeze the
candidate.

## Ledger policy

No durable registry, proved ledger, failed ledger, progress ledger, statement
ledger, inspiration file, process-lessons file, or other durable ledger is
edited by this packet.
