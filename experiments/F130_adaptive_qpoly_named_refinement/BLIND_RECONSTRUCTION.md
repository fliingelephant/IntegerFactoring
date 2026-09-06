# F130 proof-blind reconstruction — PASS

The verifier read only the final statement and independently reconstructed
the construction and its cost. It found no counterexample.

## Reconstructed invariants

Every named block is a unit divisor of the fixed initial endpoint product.
Later probe-only factors never enter the named grammar. A complete
multiplicity-aware refinement represents each old named block on
pairwise-coprime descendants. Perfect-power normalization implies that any
genuine basis change replaces at least one old block by two or more
descendants. Hence the named block count strictly grows at each nonterminal
stage, while the product of all named blocks continues to divide (A_0).

Within a frozen stage, equal residues have identical endpoints, direct
screens, and exact relation values, so residue deduplication is lossless.
All endpoint pairs are inserted before exact-value deletion. Equal exact
values differ only by a square factor whose positive root is the value
itself, congruent to (1\bmod N). Their removal therefore preserves the
normalized-root image.

## Reconstructed cost

The initial endpoint product has at most (2nE=2^{O(L^2)}) bits. Thus both
the named block count and the stage count are (2^{O(L^2)}). At any frozen
stage,

\[
\sum_{s\le D}\binom MsE^s
\le(D+1)(ME)^D
=2^{O(L^4)}.
\]

All endpoints and exact values have (O(n)) bits. The transcript,
factor-free refinements, parity matrix, kernel basis, exact products, roots,
and gcds remain polynomial in an explicit input of size
(2^{O(L^4)}). The complete deterministic bit cost is therefore

\[
2^{O((\log n)^4)}.
\]

The permanent ledger preserves every earlier dependency by zero extension.
The normalized-root assignment is a homomorphism, so testing one final
complete kernel basis is sufficient.

The seed bank eventually contains every fixed polynomial range. This does
not imply containment of the word menu that a smaller seed bank would have
formed on a different basis.

Verdict: **PASS** as a terminating deterministic quasipolynomial source and
decoder. The reconstruction found no theorem that makes its direct screens
or final normalized-root image succeed on every composite input.

