# F271 provenance

## 1. Origin

F271 arose during a resource audit of the proposed F265-D08 elliptic cubic
row experiment. D08's terminal P66 envelope allowed

\[
 1{,}000{,}000+\binom{4096}{2}=9{,}386{,}560
\]

fixed gcd comparisons per bank and 7,208,878,080 across 768 banks. The audit
question was whether this quadratic comparison schedule was mathematical or
only an implementation artifact.

The result is a decoder redesign. It is not derived from any finite elliptic
frequency and does not change the unresolved F265 source question.

## 2. Local mathematical predecessors

F271 uses the following project results as conceptual predecessors.

- **P66**, reconstructed in
  `experiments/F58_generic_gcdfree_square_decoder_reaudit/RESULT.md`, SHA-256
  `7f3107bec589462939d6ab02a135c86cf510cffea696f8439c9e2169c8a6f3e2`,
  gives the complete factor-free square-class decoder, exact roots, and
  normalized-root homomorphism.
- **P106**, the corrected candidate
  `experiments/F105_factor_free_prime_core_equivalence/RESULT.md`, SHA-256
  `ffcc2334acb34619ea2308ec9c544fbb1d0ecce4c696f9ce01c3caf9bbb53f45`,
  identifies terminal public parity rows with hidden prime-parity rows and
  proves parity-degree-one peeling. Its final re-audit has SHA-256
  `69868b43e9e10bf1fad7f981ad06406db0a635b6d919c986ffd44032a2193430`.
- **F265-D05 Algebra**, SHA-256
  `e3cbefeb597f263501d327f15f9dd4c7b78ee37d37178135ab1c0a5ff73e9fd3`,
  defines saturated positive-support private peeling and the low-support
  quotient question.
- **F265-D05 Preregistration**, SHA-256
  `a62dcb0f7d501778ef1f6092468d38a6ee15c794ec5b609bf145a3d7bf345a35`,
  supplies the proposed 64-row, 361-bit residual domain.
- **F265-D08 Algebra**, SHA-256
  `3af4a847ab65f9acde05ffd2ea98f4d5cee143c0162f915284b599e8fe007839`,
  supplies the fixed-width gcd proposal that F271 replaces.
- **F265-D08 Preregistration**, SHA-256
  `11e5a77f2c61c1f936bec775f86d0083e3fa05c2e0cf8c1420df9920a7f34b58`,
  supplies the 9,386,560-call per-bank and 7,208,878,080-call packet caps.

The local draft paths are:

```text
experiments/F265_elliptic_cubic_lift_symbolic_search_v3/D05_DRAFT_ALGEBRA.md
experiments/F265_elliptic_cubic_lift_symbolic_search_v3/D05_DRAFT_PREREGISTRATION.md
experiments/F265_elliptic_cubic_lift_symbolic_search_v3/D08_DRAFT_ALGEBRA.md
experiments/F265_elliptic_cubic_lift_symbolic_search_v3/D08_DRAFT_PREREGISTRATION.md
```

F271 does not import their full experiment contracts. It uses only the
mathematical and resource boundaries named above.

## 3. Prior art

Gcd-free bases, also called coprime bases, are established algorithmic
infrastructure. P66 already records the Bach--Shallit boundary. The main fast
reference is:

Daniel J. Bernstein, “Factoring into coprimes in essentially linear time,”
*Journal of Algorithms* 54 (2005), 1–30,
DOI [10.1016/j.jalgor.2004.04.009](https://doi.org/10.1016/j.jalgor.2004.04.009).

Bernstein computes the natural coprime base and the input factorizations over
that base in essentially linear time. His algorithm uses multiplication,
exact division, gcd, and equality testing. F271 neither reproves nor improves
that theorem.

F271 instead gives a deliberately simpler incremental proof vehicle, exact
F265 call caps, product-tree verification, and square-column grouping. These
are an experiment-engineering synthesis, not a publication-level novelty
claim.

## 4. Derivation history

The derivation proceeded in this order.

1. The P66 support-two criterion was rewritten in column form. Singleton
   relations are zero columns, and pair relations are equal columns.
2. This produced a star basis for the complete low-support span and removed
   all support-two arithmetic.
3. Terminal pairwise coprimality was replaced by the identity
   `(P mod q^2)/q = P/q mod q`.
4. A two-integer saturation recursion was derived from subtractive Euclid on
   hidden prime valuations.
5. The recursion was inserted into a dynamic product tree.
6. A first conversation-only count incorrectly assumed all general
   saturation probes created recursion edges.
7. The final construction added an explicit two-sided shared-support split.
   Equal support then became an invariant, and the corrected count became
   91,111 per bank.
8. D05 positive-support peeling was separated from P106 parity peeling after
   the valuation example `(1,2)` exposed their difference.

Only the corrected construction appears in `STATEMENT.md` and `PROOF.md`.
The correction is retained in `SELF_AUDIT.md`.

## 5. Finite checker

The included source is `sanity_check.cpp`. It is a small deterministic
checker for arithmetic edge cases and finite constants. It is not a search
for a useful factoring pattern.

The exact build and run commands are:

```text
c++ -std=c++17 -O2 -Wall -Wextra -Wpedantic sanity_check.cpp $(pkg-config --cflags --libs gmpxx) -o /tmp/f271_sanity_check
/tmp/f271_sanity_check
```

The expected single output line is:

```text
PASS pairs=250000 max_exhaustive_pair_nodes=11 max_fixed_edge_nodes=360 p58=271 primorial58_bits=368 p1875=16103 primorial1875_bits=23102 p1876=16111 primorial1876_bits=23116 f265_gcd_calls_per_bank=91111 f265_gcd_calls_packet=69973248
```

The checker covers all ordered pairs `1<=x,y<=500`, plus the fixed large
edge cases listed in `SELF_AUDIT.md`. It verifies reconstruction,
pairwise-coprime output, node charging, exact internal gcd-call accounting,
the 58-prime row certificate, the 1,875-block certificate, and final cap
arithmetic. It uses the locally installed GMP C++ interface for exact integer
arithmetic.

Checker-only, uninstrumented gcds supply the simulated carried leaf gcd,
check the shared-support split, and independently test the output list. The
last check deliberately uses a quadratic oracle because this is a finite
test assertion. These oracle gcds are not part of the decoder pseudocode or
its `Stats` call certificate; terminal production verification uses Section
5's `S`-gcd remainder method.

It does not test a dynamic global product tree, elliptic rows, P66 matrix
elimination, normalized roots, D05 peeling, output serialization, or a remote
resource envelope. Those are theorem or future-implementation obligations.

## 6. Execution and environment boundary

The checker was compiled and run locally only after the proof was complete.
The run is small: 250,000 pairs below 501, six fixed big-integer pairs, and a
sieve below 20,001. It uses one process, negligible memory, no network, no
randomness, and no remote host.

No F265 source was written or executed. No discovery or held-out corpus was
opened. No ledger, registry, proved-results file, failed-results file, or
frozen predecessor was edited.

## 7. Evidence status

The checker is implementation sanity evidence only. The general theorem rests
on the proofs in `PROOF.md`. The finite primorial bit lengths are exact
machine-verified constants whose transparent computation is included in the
frozen source.

F271 has received only its own self-audit. It has not received a fresh
no-context hostile audit, proof-blind reconstruction, human audit, or
publication-level literature review.
