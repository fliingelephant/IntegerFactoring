# F118 — registered 58-bit complete-source null search

## Question

Does the complete fixed F116 source have zero normalized-root quotient image
on a fresh odd, distinct-prime, non-perfect-power, trial-hard input larger
than the 54-bit F116 corpus?

## Corpus registration

Use `CORPUS_SPEC.json` without modification.

Start `p` at the first prime at least 320,000,000 and move upward through
consecutive primes. Start `q` at the last prime at most 639,999,999 and move
downward through consecutive primes. Pair primes with the same ordinal. Test
at most 16 pairs.

Require each candidate to satisfy all of these conditions:

1. `p` and `q` are distinct proven primes.
2. `N = p*q` has exactly 58 bits.
3. Both factors exceed `B = 58^2`.
4. The P98 stability certificate has
   `gcd(((p-1)/g)*((q-1)/g), N-1) = 1`, where
   `g = gcd(p-1,q-1)`.

Run the exact frozen F116 layer on eligible candidates. Select the first four
whose frozen layer has positive kernel nullity, no direct factor, and zero
normalized-root image modulo the global signs. Continue each selected case
through the complete fixed all-unordered-seed-pair menu. Stop the experiment
when a full-source null is found or four selected cases finish.

The corpus rule is frozen before candidate generation or source execution.
No smaller input is an allowed substitute.

## Fixed source

For `n = bitlength(N)` and `B = n^2`:

1. Attempt seeds `2..n`.
2. Construct the exact deterministic F116 gcd/perfect-power basis of the seed
   endpoints.
3. Freeze one ordered pair for every seed relation.
4. Attempt both ordered trajectories for every frozen pair and every
   exponent `0..B`.
5. Attempt every unordered pair `2 <= u < v <= n` in lexicographic order,
   again with both trajectories and every exponent `0..B`.
6. Apply canonical-residue deduplication before direct screens and retention.
7. Keep one exact parity decoder across all layers.

The source stops only on a proper residue gcd, a proper endpoint sign gcd, or
a non-global normalized dependency root. A case is a null only if the entire
menu finishes with none of these events.

For a 58-bit case, the complete source has exactly

```text
57 + 57*2*(3364+1) + binomial(57,2)*2*(3364+1)
= 11,124,747 attempt occurrences.
```

## Factor-assisted boundary

Known `p,q` values certify the corpus only. They do not choose a residue,
pair, exponent, or stopping position.

Sage/Pari factors each retained public endpoint `c,w` for discovery. The
decoder uses the distinct hidden-prime valuation-parity rows. P106 proves that
these rows have the same distinct nonzero row masks, rank, kernel, and peeled
core as the public P66 gcd-refined rows. The online half-root invariant gives
the exact positive dependency root modulo `N`.

This makes a completed null exact for the fixed finite source, but still
factor-assisted. A positive dependency has no recovered public support in
this run. It is not eligible for factor-free promotion without a separate
support replay.

Kernel nullity and normalized-root image are recorded separately. Every
dependent online column gives one fundamental kernel-basis vector. A null
requires positive nullity and zero image in
`mu_2(N)/{+1,-1}`.

## Resource registration

The runner uses the named hard timeout
`F118_58BIT_FULL_SOURCE_NULL_HARD_TIMEOUT`, set to 1,200 seconds. It preserves
the latest exact checkpoint on timeout or process failure.

Canonical deduplication uses a fixed open-addressed table. At 58 bits, its
registered capacity is `2^24` 64-bit slots, or 134,217,728 payload bytes.
The full source performs at most 22,249,494 endpoint factorizations before
cache hits. Checkpoints record completed pairs, exact prefix counts, decoder
rank and nullity, root counts, elapsed time, and peak resident-set data.

If the full registered work cannot finish, the result is only the exact
completed prefix plus the source-size, memory, factorization-count, and
measured-throughput scaling record. No smaller scan may replace it.

## Null follow-up boundary

If a null appears, freeze `p,q,N`, the corpus ordinal, the F118 source hash,
and the full-source output before defining the feedback run. Then register a
separate recursive canonical integer-block feedback source. This prevents a
feedback rule from being chosen after its behavior on the null is known.

No durable ledger is edited by F118.
