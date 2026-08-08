# Blind reconstruction report

## Verdict

`PASS_WITH_CORRECTIONS`

The mathematical degree bound, private-row consequence, carry inequalities,
seed construction, finite witness, kernel isomorphism, and root-class
preservation all hold. The finite primality claims have complete recursive
Lucas certificates rather than probable-prime evidence.

## Corrections and interpretation boundaries

1. The formula `-N^(-1) mod c` needs `c>=2`. At `c=1`, the carry is zero but
   an inverse modulo one is not standard notation. The original display is
   valid at `c=1` only after declaring the unique residue convention.

2. A source extension must stay inside the complete canonical universe for
   the same modulus. The permanence claim does not cover arbitrary external
   exact values or a changed modulus.

3. `REUSE`, `CLOSE`, and `ROOT` have no formal definitions in the supplied
   statement. The proof certifies the precise underlying facts: the private
   column occurs in no dependency; the remaining kernel is unconstrained by
   that fact; and parity closure does not decide whether a root class is
   nontrivial. A literal verdict on differently defined labels would require
   their definitions.

4. The statement should explicitly say that `N` is a positive odd modulus.
   The proof uses the standard positive-modulus interpretation.

## Claim-by-claim result

| Claim | Result | Basis |
|:--|:--|:--|
| Universal degree bound | Pass | Injection from distinct divisible values to divisible endpoints |
| Exact-value deduplication | Pass | The injection is on projected values; `N=11, P=12` shows why orbit uniqueness cannot be assumed |
| Large-row privacy and source permanence | Pass with stated scope | Degree is at most one in the complete fixed-modulus universe |
| Carry facts | Pass with `c=1` notation correction | Exact inequalities and modular reduction |
| General seed-2 family | Pass | `w(2)=q`, `P=2q`, carry one, and the degree bound |
| Sign screens | Pass | Euclidean reductions to gcds with `3` and `5` |
| Dirichlet scope | Pass | Only primes in the progression are supplied |
| Finite arithmetic | Pass | Exact multiplication, bit bounds, and threshold comparisons |
| Finite primality | Pass | Recursive Lucas certificates ending at `2` |
| Semiprime and non-power claims | Pass | Distinct certified prime factors with exponent one |
| Kernel consequence | Pass | Restriction/zero-extension is a kernel bijection |
| Positive exact root classes | Pass | The selected products are identical under the bijection |
| `REUSE`/`CLOSE`/`ROOT` separation | Pass conditionally on the stated interpretations | Linear counterexamples and exact canonical squares at `N=15` |

## Scope compliance

- No infinite trial-hard semiprime family is claimed.
- The exact missing shifted-semiprime statement is isolated.
- One private row is not promoted to full rank.
- No smoothness or random-matrix heuristic is used.
- No candidate proof, audit file, or durable ledger was read or edited during
  this reconstruction.
