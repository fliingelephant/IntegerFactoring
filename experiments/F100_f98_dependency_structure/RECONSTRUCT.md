# F100 proof-blind reconstruction

## Strict verdict

**OVERALL: PASS.**

Every claim in `RECONSTRUCTION_STATEMENT.md` passed an independent exact
reconstruction from the 166 allowed witness records. The verifier did not
use the replay's stored rank, histogram, connectivity, or root summaries.

## Input boundary

The only pre-existing mathematical inputs read for this reconstruction
were:

1. `RECONSTRUCTION_STATEMENT.md` in this directory.
2. The explicitly allowed
   `../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json`.

The replay SHA-256 is
`ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab`.
It is exactly the hash required by the statement. I did not read any other
F100 file, durable ledger, prior audit, or prior result.

The verifier reads only `N` and the 166 records at
`decoder.first_useful_certificate.witness_records` from the replay as
arithmetic data. All structural results below are recomputed.

## Presentations and exact factorizations

For every record, the verifier checked all of the following with

\[
N=202{,}537{,}109:
\]

- \(1\leq c,w<N\).
- \(P=cw\) as an exact integer equality.
- \(P\equiv1\pmod N\).
- \(\gcd(c,N)=1\).
- \(w=c^{-1}\bmod N\), with \(w\) equal to the representative in
  \([1,N-1]\).

Thus all 166 records are valid canonical-inverse presentations. The set of
their exact \(P\)-values has cardinality 166, so no selected value is a
duplicate.

The verifier factored every \(P\) with Sage exact integer factorization
under `proof.all(True)`. It then checked every returned prime with
`is_prime(proof=True)` and multiplied every prime power back to the
original \(P\). The exhaustive 166-entry factorization list is in
`RECONSTRUCT_OUTPUT.json`. Its canonical JSON digest is

```text
87e8c2caaa3d8a6afdf07d0c8a32248dae83a4220a4b920de39c1b7ec5637f9b
```

This is a factor-assisted diagnosis of a frozen public certificate. It is
not a step in the public algorithm.

## Parity matrix

For every prime \(p\) found in the factorizations and every selected value
\(P_j\), the verifier formed

\[
M_{p,j}=v_p(P_j)\bmod2.
\]

It retained every row that is nonzero and explicitly included the prime-2
row. This gives 230 rows and 166 columns.

The full matrix is recorded as sorted prime rows with exact zero-based
column supports in `RECONSTRUCT_OUTPUT.json`. The SHA-256 of that canonical
row encoding is

```text
e61f6a978368000494b43779e0fbe5197758a386173803fcc7c8b21a4759eb5b
```

Two exact rank implementations agree:

| Check | Result |
|:---|---:|
| Sage dense matrix over \(\mathbf F_2\) | 165 |
| Independent integer-bit-vector elimination | 165 |
| Nullity \(166-\operatorname{rank}M\) | 1 |

Every row has even support. Hence the sum of all 166 columns is zero. The
verifier also built all 166 matrices obtained by deleting one column. The
rank list is exactly 166 copies of 165.

The reconstructed row-degree histogram is:

```text
2:167, 4:31, 6:9, 8:7, 10:3, 12:1, 14:1, 16:1,
18:1, 20:1, 22:1, 28:1, 32:1, 34:1, 44:1, 52:1,
62:1, 80:1
```

The reconstructed column-degree histogram is:

```text
3:6, 4:13, 5:36, 6:41, 7:37, 8:22, 9:10, 11:1
```

Exactly 167 rows have degree two. The prime-2 row has degree 80, and it is
the unique degree-80 row.

### Circuit conclusion

Let \(\mathbf 1\) be the all-ones vector of length 166. The even row
degrees give \(M\mathbf1=0\). Since the kernel has dimension one,

\[
\ker M=\{0,\mathbf1\}.
\]

The unique nonzero dependency therefore uses all 166 columns. No proper
subset can be dependent. The 166 deletion-rank checks give the equivalent
direct statement that every 165-column deletion is independent. Hence the
selected set is a binary matroid circuit. It is not a duplicate direction
and it is not a two-column dependency.

## Connectivity

The verifier joined columns \(i,j\) exactly when at least one row contains
both. It built edges directly from the reconstructed row supports and ran
an exact component search.

| Graph | Distinct edges | Component sizes |
|:---|---:|:---|
| All 230 rows | 7,583 | `[166]` |
| Prime-2 row removed | 5,851 | `[166]` |

Both graphs are connected. Connectivity therefore does not depend on the
degree-80 prime-2 row.

## Provenance

There is exactly one record whose provenance kind is `initial_seed`. It
has seed 11 and \(c=11\). The other 165 records have kind
`feedback_trajectory` and round 1.

The verifier did not only count their labels. It regenerated every feedback
state. For exponent \(e\), it checked

\[
c\equiv u^e v\pmod N
\]

for `u_power_times_v`, and

\[
c\equiv u v^e\pmod N
\]

for `u_times_v_power`. All 165 regenerated residues equal the recorded
canonical \(c\)-values.

The reconstructed five-family counts are:

| Active index | Pair \((u,v)\) | Count |
|---:|:---|---:|
| 9 | \((11,36824929)\) | 15 |
| 11 | \((13,124638221)\) | 10 |
| 12 | \((2,5)\) | 54 |
| 15 | \((2,17)\) | 53 |
| 25 | \((3,17)\) | 33 |

The reconstructed eight nonempty oriented trajectories are:

| Active index | Pair \((u,v)\) | Orientation | Count |
|---:|:---|:---|---:|
| 9 | \((11,36824929)\) | `u_power_times_v` | 15 |
| 11 | \((13,124638221)\) | `u_power_times_v` | 10 |
| 12 | \((2,5)\) | `u_power_times_v` | 32 |
| 12 | \((2,5)\) | `u_times_v_power` | 22 |
| 15 | \((2,17)\) | `u_power_times_v` | 38 |
| 15 | \((2,17)\) | `u_times_v_power` | 15 |
| 25 | \((3,17)\) | `u_power_times_v` | 15 |
| 25 | \((3,17)\) | `u_times_v_power` | 18 |

Because the unique circuit contains every selected column, it contains the
initial seed, all five feedback families, and all eight nonempty oriented
trajectories. This proves the stated cross-family and cross-orientation
support claim.

## Exact square and root

The verifier summed the full prime exponents across all 166 independent
factorizations. Every aggregate exponent is even. It constructed the
positive integer

\[
R=\prod_p p^{\frac12\sum_j v_p(P_j)}
\]

and independently checked with integer square root that

\[
R^2=\prod_{j=1}^{166}P_j
\]

as an exact integer equality. The exact 1,292-digit positive root is stored
in `RECONSTRUCT_OUTPUT.json`. Its decimal SHA-256 is

```text
43f3b0c6c08821a6fc221521783538bebbebcc4b3d623c7f2b6fd0888065bbfa
```

Reduction and exact gcd computation give

\[
R\equiv132{,}013{,}085\pmod N,
\]

\[
\gcd(R-1,N)=19{,}727,
\qquad
\gcd(R+1,N)=10{,}267.
\]

The verifier also proved both gcd outputs prime and checked

\[
19{,}727\cdot10{,}267=202{,}537{,}109=N.
\]

Thus the unique selected dependency produces a non-global square root and
factors this modulus.

## Exact scope

This reconstruction proves only that the selected 166-value F98
certificate is one connected, cross-family, cross-orientation circuit. It
also proves that this circuit is not a duplicate-value direction, a pair,
or a dependency on a proper subset of the 166 selected values.

It does **not** prove any of the following:

- Minimum support in the full 9,414-value pool.
- Inverse-polynomial circuit density.
- An all-input progress law.
- Publication novelty.
- A new complexity bound.
- A factoring algorithm.

The factorization work here is allowed only as diagnosis of the frozen
public certificate.

## Reproducibility record

The named source is `RECONSTRUCT_verify.py`. It ran with Sage exact
arithmetic under this hard 300-second timeout and exited with status zero:

```text
DOT_SAGE=/private/tmp/RECONSTRUCT_F100_SAGE /opt/homebrew/bin/timeout --verbose 300s /usr/local/bin/sage -python RECONSTRUCT_verify.py > RECONSTRUCT_OUTPUT.json 2> RECONSTRUCT_LOG.txt
```

The successful run took approximately four wall-clock seconds. Its log
ends with `VERDICT PASS`.

| File | SHA-256 |
|:---|:---|
| `RECONSTRUCTION_STATEMENT.md` | `1235cbf1c34eb47502286e4607337d9f43392853847bddb8711c0ad05072c82f` |
| Allowed `PUBLIC_REPLAY_OUTPUT.json` | `ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab` |
| `RECONSTRUCT_verify.py` | `ca99e176a87beceebb12fbac1a5bd8dfc1d2e276e589a58734a424a08fd45795` |
| `RECONSTRUCT_OUTPUT.json` | `f9008ff13b16bb064ad645bd7c74b85e8117f520adfcfb8bf5fb716cca8a8449` |
| `RECONSTRUCT_LOG.txt` | `36d773640614f4a9e184885d65cfe04a255b0e363c88328044fbfb6352cd847f` |

Files created by this reconstruction are `RECONSTRUCT.md`,
`RECONSTRUCT_verify.py`, `RECONSTRUCT_OUTPUT.json`, and
`RECONSTRUCT_LOG.txt`. No statement, candidate, audit, replay, or prior
result file was edited.
