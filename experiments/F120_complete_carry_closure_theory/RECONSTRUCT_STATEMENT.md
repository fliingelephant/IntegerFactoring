# F120 proof-blind reconstruction statement

This file states the claims only. Do not read any other file in this
directory before completing the reconstruction.

## Definitions

Let `N` be odd. For each unit `1 <= c < N`, let `w(c)` be its least positive
inverse modulo `N` and define

```text
P_N(c) = c*w(c) = 1 + kappa_N(c)*N.
```

Project the family to distinct positive exact values `P_N(c)`, with `P=1`
removed. For a prime `r`, its row degree is the number of projected columns
whose exact value has odd `r`-adic valuation.

## Claims to reconstruct

1. For every prime `r`, every set of distinct canonical exact values for one
   modulus satisfies

   ```text
   degree(r) <= floor((N-1)/r).
   ```

   The proof must allow different inverse-endpoint orbits to have the same
   exact product and must explain why exact-value projection does not break
   the bound.

2. Consequently, every present odd row with `r>(N-1)/2` is private against
   the complete universe of canonical exact values. It remains private under
   every source extension.

3. Establish the exact carry facts

   ```text
   0 <= kappa_N(c) < min(c,w(c)),
   kappa_N(c) = -N^(-1) mod c in the interval 0..c-1.
   ```

4. For every prime `q>2`, set `N=2q-1`. Prove that the seed `c=2` has
   inverse `q`, exact value `N+1=2q`, carry one, and a valuation-one row `q`
   that is private in the complete canonical universe. For primes
   `q congruent to 1 mod 30`, also prove that both endpoint sign gcd screens
   are one. State exactly what Dirichlet's theorem does and does not supply.

5. Independently verify this finite instance:

   ```text
   p = 1,000,289,
   ell = 2,000,309,
   N = p*ell = 2,000,887,089,301,
   n = bit_length(N) = 41,
   n^2 = 1,681,
   r = (N+1)/2 = 1,000,443,544,651.
   ```

   Prove that `p`, `ell`, and `r` are prime; that `N` is an odd distinct
   semiprime and not a perfect power; that both input factors exceed `n^2`;
   and that the seed-2 exact value has a private valuation-one `r` row with
   null sign screens. A fully deterministic primality argument is required.

6. Prove the exact kernel consequence of one private row: its column has
   coefficient zero in every binary dependency. Deleting that row and column
   preserves the kernel on the remaining coordinates and preserves every
   surviving positive exact root class modulo `N`.

7. Keep these conclusions separate:

   - `REUSE` is false on the finite trial-hard semiprime.
   - No conclusion about `CLOSE` follows from one private row.
   - No conclusion about `ROOT` follows from one private row or from `CLOSE`.

## Required boundary

Do not claim an infinite trial-hard semiprime family. Isolate the exact
missing statement needed to make `N=2q-1` such a family. Do not claim that
one private column makes the complete matrix full rank. Do not use
smoothness or random-matrix heuristics.

Write a self-contained proof, rejected extensions, a verdict, and hashes in
new files prefixed `RECONSTRUCT_`. Do not read or edit the candidate proof,
audit files, or durable project ledgers.
