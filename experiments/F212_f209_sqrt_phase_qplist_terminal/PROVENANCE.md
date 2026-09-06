# F212 provenance

## Namespace

Before creation, a repository-wide search found no F212 entry or experiment
directory. F211 is intentionally left unused here and reserved for the
dyadic quotient experiment requested by the root agent.

## Source question

F209-D01 showed finite geometric collapse of the exact F207 inverse torsor,
but its constructor usually scanned the full balanced factor interval. The
live implicit problem was to find, count, or isolate a residue \(x\) whose
modular inverse partner lies in the opposite balanced interval and whose two
progressions pass the endpoint product test.

F212 was derived from a first-principles audit of that exact predicate. The
central observation is that its odd representative step
\(\operatorname{lcm}(2,m)\) creates two elementary regimes:

1. below the square-root scale, every class has enough lifts that all three
   F209 tests pass uniformly; and
2. above the square-root scale, both progressions are singletons and the
   product test is exact divisibility.

The \(N^{1/4+\varepsilon}\) terminal was added after checking the standard
univariate unknown-divisor Coppersmith threshold for a supplied factor
residue class.

## Closest prior work and material difference

- P183/F207 proves that factoring \(K=(N-1)/2\) and the square-gap child is
  recursion-safe on the balanced branch and constructs the inverse torsor.
- F209-D01 gives finite evidence that Archimedean pruning often orients this
  torsor, but its exact constructor scans \(\Theta(\sqrt N)\) candidates.
- P184/F208 identifies the reciprocal-floor divisor spike but does not tie
  it exactly to the full \(K\)-modular F209 predicate.

F212 adds an unbounded theorem about the exact F209 geometry and a positive
QP-list postprocessor. It does not promote the finite F209-D01 behavior to a
QP algorithm.

## Mathematical dependency

The only external algorithmic theorem used is the standard univariate
unknown-divisor form of Coppersmith's small-root theorem. The packet states
the exact version it needs: fixed degree one, a hidden divisor at least
\(N^\beta\), and root size \(N^{\beta^2-\eta}\). A fresh audit must verify
that dependency before promotion.

No general bivariate Coppersmith heuristic is used.

## Computation and evidence

No mathematical computation, search, random sampling, or remote run was
performed for F212. Existing F209-D01 output was read only as motivation.
The proof is independent of those finite rows. SHA-256 hashing is used only
to freeze the candidate text.

## Ledger policy

No durable registry, proved ledger, failed ledger, progress ledger, or
inspiration ledger is edited by this packet.
