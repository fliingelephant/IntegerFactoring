# F100 proof-blind reconstruction statement

Reconstruct and verify the following finite structural claim without reading
any other file in this F100 directory.

## Allowed certificate

The only external arithmetic artifact you may read is

```text
../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
```

Its required SHA-256 is

```text
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab
```

Use the 166 `witness_records` in
`decoder.first_useful_certificate`. You may use exact integer factorization
because this is a factor-assisted diagnosis of an already public factoring
certificate. Do not treat the diagnostic as part of the public algorithm.

## Claim to reconstruct

The 166 exact values \(P=cw\) are distinct. Each record is a valid canonical
inverse presentation modulo

\[
N=202{,}537{,}109.
\]

Make one binary column for each value. Make one row for every prime whose
valuation is odd in at least one selected value. Include the prime 2. This
prime-valuation parity matrix has

```text
rows     230
columns  166
rank     165
nullity    1
```

The sum of all columns is zero. Deleting any one column leaves rank 165.
Therefore the full 166-value set is a binary matroid circuit: it has one
nonzero dependency, and every proper subset is independent.

The row-degree histogram is

```text
2:167, 4:31, 6:9, 8:7, 10:3, 12:1, 14:1, 16:1,
18:1, 20:1, 22:1, 28:1, 32:1, 34:1, 44:1, 52:1,
62:1, 80:1.
```

The column-degree histogram is

```text
3:6, 4:13, 5:36, 6:41, 7:37, 8:22, 9:10, 11:1.
```

Thus 167 of the 230 rows have degree two. The degree-80 row is the row for
prime 2.

Join two selected relation values when they share a prime of odd valuation.
This graph is connected on all 166 values. It remains connected when the
prime-2 row is removed.

The certificate has one initial seed relation and 165 feedback relations.
The feedback relations occur in five active-pair families:

```text
active index 9,  (11, 36824929):   15
active index 11, (13, 124638221):  10
active index 12, (2, 5):           54
active index 15, (2, 17):          53
active index 25, (3, 17):          33
```

They span eight nonempty oriented trajectories:

```text
index 9,  (11, 36824929),  u_power_times_v: 15
index 11, (13, 124638221), u_power_times_v: 10
index 12, (2, 5),          u_power_times_v: 32
index 12, (2, 5),          u_times_v_power: 22
index 15, (2, 17),         u_power_times_v: 38
index 15, (2, 17),         u_times_v_power: 15
index 25, (3, 17),         u_power_times_v: 15
index 25, (3, 17),         u_times_v_power: 18
```

The product of all 166 values is an exact integer square. Its positive root
satisfies

\[
R\equiv132{,}013{,}085\pmod N,
\]

\[
\gcd(R-1,N)=19{,}727,
\qquad
\gcd(R+1,N)=10{,}267.
\]

## Required scope

This proves that the selected F98 certificate is one connected,
cross-family, cross-orientation circuit. It is not a duplicate-value
direction, a pair, or a dependency on a proper subset of these 166 selected
values.

It does not prove minimum support in the full 9,414-value pool,
inverse-polynomial circuit density, an all-input progress law, publication
novelty, a new complexity bound, or a factoring algorithm. The computation
may use factorization only because it diagnoses a frozen public certificate.
