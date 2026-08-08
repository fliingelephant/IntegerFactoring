# F116 — independent 54-bit all-pairs stress

## Question

Does the fixed all-seed-pair batch from F110 still factor a fresh set of
larger inputs whose frozen first layer has dependencies but only global
roots?

## Registered corpus

Generate at most 24 prime pairs in this exact order:

- `p` starts at the first prime at least 80,000,000 and increases through
  consecutive primes;
- `q` starts at the last prime at most 159,999,999 and decreases through
  consecutive primes;
- pair the values with the same ordinal.

Keep the first six pairs that meet all of these conditions:

1. `N = p*q` is trial-hard and P98-stable.
2. The pinned F104 first-round replay completes.
3. Its public kernel basis is nonempty.
4. Every basis root is `+1 mod N`.

This selection uses the known factors only to certify the corpus. The batch
replay receives `p,q` because its current endpoint decoder is factor-assisted;
the generated residues and menu depend only on `N`.

## Fixed source

For each selected input, run the pinned F110 source without modification:

1. retain seeds `2..n`;
2. freeze the complete initial-basis trajectory layer through `n^2`;
3. append every unordered seed pair `2 <= u < v <= n` in lexicographic order;
4. keep one joint parity decoder across all layers.

Stop at the first direct factor or non-global parity dependency. If the full
menu ends without a factor, preserve that input as a null.

## Falsifiers and scope

The run fails if a source hash changes, fewer than six qualifying cases occur
within the registered 24 pairs, a selected frozen layer is not globally
trapped under F110, or any worker does not finish before the hard timeout.

A null refutes sufficiency of this exact bounded source on that input. A
success is finite evidence only. Endpoint factoring makes all positive cases
factor-assisted until an N-only replay or theorem replaces it.
