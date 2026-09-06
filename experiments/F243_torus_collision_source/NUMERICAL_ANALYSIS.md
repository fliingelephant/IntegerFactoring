# F243-R2 numerical analysis

## Run integrity

F243-R1 is not evidence.  A local five-input implementation smoke violated
its remote-only clause.  `R1_STATUS.md` preserves that failure.

F243-R2 used disjoint SHA-256 ranks and a disjoint small-prime interval.  It
ran as one C++20 process on `seetacloud`.

- Inputs: 25,000.
- Exterior target rows per exact source: 137,233.
- Total TSV data rows: 3,019,750.
- Wall time: 21.260 seconds.
- Peak RSS: 122,644 KiB.
- Monte Carlo pairs per row: 200,000.
- Input transcript SHA-256:
  `d9ec5e879846ffe4733f51c7df1096d38f05492c8fc97dfb32ff4a58746f97ce`.
- Verifier SHA-256:
  `139351e7432afc885e8b1a114fdba97d7cc992cc16d80528e1a45db41760cb63`.
- Uncompressed TSV SHA-256:
  `5ec0d488a50952af7e2a59f59ef08aacc29bf4c952f5f779ca04a37d8b20a4e4`.
- Compressed TSV SHA-256:
  `cfccda1386e7f98277c0860f9616b51c265b4c72f11b397588427129b7139b1e`.
- Raw report SHA-256:
  `59ef5d79b7cc743f32e944d1674a65d5b90c729bb7eb7c6b0ba38f7d6b6e73ae`.

The raw report and compressed row data are `R2_REPORT.md` and `R2.tsv.gz`.
All finite measurements below are guidance, not proof.

## Main pattern

The tested factor-free and canonical sources stayed at the generic
`Theta(1/ell)` scale.

| source | zero rows | rows with `kappa>4/ell` | rows with `kappa>=1/sqrt(ell)` | median `ell*kappa` | maximum `ell*kappa` |
|---|---:|---:|---:|---:|---:|
| gcd-divisor of `N^2-1` | 7,781 | 0 | 0 | 0.149 | 1.036 |
| primitive box determinant, `B=64` | 4,171 | 0 | 0 | 0.938 | 1.013 |
| primitive box trace resultant, `B=64` | 893 | 0 | 0 | 1.842 | 2.002 |
| raw Jacobi `D`, both signs | 0 of 48 | 0 | 0 | about 1.000 | 1.221 |
| canonical Hilbert coordinate, all fixed `D` | 0 of 288 | 0 | 0 | about 1.000 | 1.350 |
| canonical Hilbert coordinate union | 0 of 144 | 0 | 0 | about 1.94 | 2.414 |
| canonical Hilbert determinant | 0 of 144 | 0 | 0 | about 1.04 | 1.285 |

The Monte Carlo extrema at the largest targets are consistent with counting
noise.  For example, the raw negative-Jacobi row at
`N=33,276,433`, `ell=1,187` had `152/200,000` hits.  Its 95% Wilson
interval is approximately `[0.000648,0.000891]`; after multiplication by
`ell`, this is `[0.769,1.057]`.  The exact counts, not this interval, are
the data.  The proof-level atom bounds in `STATEMENT.md` supersede these
finite coordinate and discriminant diagnostics.

No tested canonical representative showed the hoped-for carry bias.
Changing `D` among `-1,2,3,5,N-1,N+1` did not change the scale.

## Pell spikes are small orders

Pell pair and trace sources behaved differently.  They had many exact-zero
rows and a thin set of large spikes.

- At window 128, pair collisions were zero on 37,090 of 137,233 rows.
- At window 128, trace collisions were zero on 26,445 rows.
- The median exact Pell order divided by `ell` was 0.538.
- The largest trace value was `ell*kappa=4,117.54`.

The largest row was

`N=170,603,813`, `ell=7,541`, `ord_ell(N+sqrt(N^2-1))=3`.

Every large spike similarly had a small exact Pell order.  This matches the
proved law: a `T`-term trace window is injective when the order is at least
`2T-2`.  The spikes are not a new random effect.  They are the already
visible small-meta-order branch.

## Factored uniform divisors contain rare real aliases

Uniform divisors of a granted factorization were not uniformly generic.

- Divisors of `N^2-1` had 631 rows above `4/ell`.
- Three rows reached `1/sqrt(ell)`.
- The maximum was `ell*kappa=97.925`.

A post-hoc explanation of the maximum row is exact.  It had

\[
N=245360887=15661\cdot15667,
\qquad \ell=3917,
\]

and

\[
N+1=8\cdot30670111,
\qquad30670111=1\pmod {3917}.
\]

Toggling this known prime factor produces many distinct divisor pairs with
the same residue.  The uniform-divisor law had

\[
\kappa_\ell=160/6400.
\]

The factor-free gcd-divisor law on the same row had only

\[
\ell\kappa_\ell\approx8.18\cdot10^{-5}.
\]

Thus the alias is useful but comes from the granted factorization.  Once the
factor `b=30670111` is known, the simpler deterministic child `b-1` already
contains the target.  The factor-free gcd law gives the toggle probability
about `1/b` and loses the effect.

## Interpretation

The computation supports three proof-level conclusions.

1. The `N^2-1` uniform-divisor bridge is real on some inputs and is more
   general than the small-generated-subgroup sufficient condition.
2. Exact factor-free gcd sampling does not approximate uniform divisor
   sampling in the statistic that matters.
3. Pell traces and canonical torus coordinates do not show a new all-input
   source.  They reduce respectively to a small order or to generic modular
   collision.

The live numerical target is now narrower: search cross-coordinate or
nonlinear canonical carry words after the universal `N^2-1` baseline.  The
present scan does not prove a bound for those words.
