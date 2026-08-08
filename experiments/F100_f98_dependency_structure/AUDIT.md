# F100 hostile audit

## Verdict: **FAIL**

The structural core passes. The 166 selected exact values form one connected
binary matroid circuit. The root and factor extraction are correct. The
candidate fails as written because two reported labels do not match the
objects that the source computes:

1. The reported 230-row matrix includes the prime 2. It is a prime-valuation
   parity matrix, not an odd-prime-only matrix.
2. The five provenance groups are active-pair families. Under F98's own
   definition, the two orientations are separate trajectories. The
   certificate uses eight oriented trajectories, not five.

These are narrow defects. They do not invalidate the circuit. They do change
the literal row count, degree histograms, and trajectory count stated in
`RESULT.md`.

## 1. Pinned candidate

I pinned every requested F100 artifact before the audit:

```text
75c3c0935ed70b1180fb068d9761ece97c1345cf2612a579344acbe31236b773  DESIGN.md
60309c5ba6473eed0967efebb49d0bafbdcb7ef0a630859d722df67c152aa538  RESULT.md
5e403f38e788752225d0259d893d27c3ff95f3e639daceb1467802bac3076671  RUN_MANIFEST.md
cbe30dc982180d2315c38302da0fb738a32c20788054e260024c4e0a4d93b3b8  analyze_dependency.sage
73615f0baaafb8a7606cc460f505f66f0187aa442ff944f7478fdc7a2c34b20f  OUTPUT.json
ce05ab5d2431d3fe94ab356968dfa715be2c9f1e89bf40cdc01ad3248a39e3a3  RUN.log
fb8c2b5e98d9fea0ef9d9f8282dd0c0e9c2197c207b7255d797bac4b834a602d  FAILED_RUNS.md
88c429719d757cf812719b43630ab7924f333bf1c1c8824a427de3832a9ff817  run_with_timeout.py
```

I read all eight files in full, including all 6,959 lines of `OUTPUT.json`.
The named Sage source predates the authoritative output and log. The runner
used a hard 120-second timeout and exited zero.

I also pinned and read the public F98 certificate and its generating source:

```text
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  F98/PUBLIC_REPLAY_OUTPUT.json
5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b  F98/public_factorization_free_replay.py
f2d28d074d53bc93c675553b28e083b93b0d6dd35d1a65edb430c69a6cd26fb0  F98/RESULT.md
cfc8e9e7d2a87e730305ce11e2c612a0c4a449f7b05f714c8b41eb9fa09e94c3  F98/RUN_MANIFEST.md
```

## 2. Fresh certificate reconstruction: PASS

I wrote a new Sage verifier. It does not import the F100 analysis source.
Starting from the pinned public F98 JSON, it independently:

- regenerated all 12,549 first-occurrence public records;
- reconstructed the 9,414-value exact deduplication map;
- matched every selected column and raw index to its witness record;
- checked every canonical inverse, exact product, and provenance formula;
- factored all 166 relation values;
- compared every reported factorization with the candidate output;
- rebuilt both the all-prime parity matrix and the odd-prime-only matrix;
- checked all 166 one-column deletions for circuit minimality;
- rebuilt all degree histograms and support components;
- rebuilt all provenance counts; and
- recomputed the exact square root and both final gcds.

The final command was:

```text
/usr/bin/time -p /opt/homebrew/bin/timeout 120 /usr/local/bin/sage \
  audit_dependency_verifier.sage \
  --input ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json \
  --candidate-output OUTPUT.json \
  --output AUDIT_VERIFY_OUTPUT.json
```

It exited zero in 2.07 seconds. The source predates its output and log.

```text
c253ec23a611208ca351a1e89ca32136f8e6edd017ca892840d78b14434bb367  audit_dependency_verifier.sage
993d1d3e4280dd394a74e8154feb88eabefb86444c9dee31eac09dbdb2fb7e47  AUDIT_VERIFY_OUTPUT.json
bb31407a66efed3a825a9cf0123e8df152d1192cf1b364ca6ac97cd1e953a2c4  AUDIT_VERIFY_RUN.log
```

## 3. Certificate identity and distinctness: PASS

The public certificate contains 166 witness records. Their selected-column
indices, selected raw indices, and exact values are all distinct. Every
record satisfies

\[
1\le c,w<N,
\qquad
w=c^{-1}_{\mathrm{can}}\pmod N,
\qquad
P=cw\equiv1\pmod N.
\]

The records map exactly to the public stream. There is no duplicate-value
direction inside this selected set.

## 4. Rank, nullity, and circuit minimality: PASS

For each exact value \(P_j\), form one binary column from the primes whose
valuation in \(P_j\) is odd. This matrix includes every prime, including 2.
It has:

```text
rows       230
columns    166
rank       165
nullity      1
```

The sum of all 166 columns is zero. Rank 165 makes this the unique nonzero
dependency on the selected set. Its support is all 166 columns. Therefore
every proper subset is independent and the selected set is a binary matroid
circuit.

As a redundant direct check, I deleted each column in turn. Every resulting
230-by-165 matrix has rank 165.

This minimality is local to the selected 166 values. It does not prove that
the full 9,414-value F98 pool has no smaller dependency or no smaller useful
dependency.

## 5. The reported histograms: arithmetic PASS, label FAIL

The candidate's numerical histograms are exact for the prime-valuation
parity matrix **including 2**:

```text
row degrees
2:167, 4:31, 6:9, 8:7, 10:3,
12:1, 14:1, 16:1, 18:1, 20:1, 22:1, 28:1,
32:1, 34:1, 44:1, 52:1, 62:1, 80:1

column degrees
3:6, 4:13, 5:36, 6:41, 7:37, 8:22, 9:10, 11:1
```

Thus 167 of 230 rows have degree two, and the reported fraction
\(167/230=0.7260869565\ldots\) is correct for that matrix.

However, the unique degree-80 row is the row for the prime 2. The source
puts 2 in `odd_primes`, and `OUTPUT.json` contains 2 in many `odd_support`
lists. Therefore these phrases in `RESULT.md` are false under their ordinary
mathematical meaning:

- "230 odd-prime rows";
- "between 3 and 11 odd-prime rows"; and
- "shared-odd-prime support graph" when it refers to the reported matrix.

If "odd-prime" is meant literally, remove the prime-2 row. The exact data
then become:

```text
rows       229
rank       165
nullity      1
degree-two rows  167

row degrees
2:167, 4:31, 6:9, 8:7, 10:3,
12:1, 14:1, 16:1, 18:1, 20:1, 22:1, 28:1,
32:1, 34:1, 44:1, 52:1, 62:1

column degrees
3:8, 4:21, 5:44, 6:50, 7:23, 8:18, 9:1, 10:1
```

The odd-prime-only matrix still has rank 165, nullity one, and the
all-column dependency. Thus it also proves the same circuit. The cleanest
repair is to keep the current 230-row computation and rename it the
"prime-valuation parity matrix" or the "odd-valuation prime matrix."

## 6. Connected support: PASS under all three meanings

The 2-section relation graph is connected on all 166 columns when adjacency
means a shared prime with odd valuation. It remains connected after the
prime-2 row is removed. It is also connected when adjacency means any shared
prime factor, without reducing valuations modulo two.

Therefore the connected-support claim is not an artifact of the prime-2
row. The candidate must only name the chosen support relation correctly.

For reference, the pair counts are:

```text
shared parity prime, including 2       7,583
shared odd parity prime only           5,851
nontrivial integer gcd                11,358
```

## 7. Provenance: counts PASS, trajectory label FAIL

The certificate has one initial seed relation and 165 feedback relations.
The five reported table rows are exact active-pair family counts:

```text
active index 9,  (11, 36824929):   15
active index 11, (13, 124638221):  10
active index 12, (2, 5):           54
active index 15, (2, 17):          53
active index 25, (3, 17):          33
```

The global orientation counts also reproduce:

```text
u_power_times_v     110
u_times_v_power      55
```

F98 defines the two oriented words as two trajectories. With that
definition, the certificate uses eight oriented trajectories:

```text
index 9,  (11, 36824929),  u_power_times_v:  15
index 11, (13, 124638221), u_power_times_v:  10
index 12, (2, 5),          u_power_times_v:  32
index 12, (2, 5),          u_times_v_power:  22
index 15, (2, 17),         u_power_times_v:  38
index 15, (2, 17),         u_times_v_power:  15
index 25, (3, 17),         u_power_times_v:  15
index 25, (3, 17),         u_times_v_power:  18
```

`RESULT.md` must say "five active-pair families spanning eight oriented
trajectories," not "five distinct trajectories."

## 8. Root and factor extraction: PASS

The product of all 166 exact values is an exact integer square. Its positive
root satisfies

\[
R\equiv132{,}013{,}085\pmod {202{,}537{,}109}.
\]

The final gcds are

\[
\gcd(R-1,N)=19{,}727,
\qquad
\gcd(R+1,N)=10{,}267.
\]

Their product is \(N\). The factor extraction is exact.

## 9. Interpretation and asymptotic scope: PASS

After the two naming corrections, the finite interpretation is supported:

- the selected dependency is not a duplicate-value cancellation;
- it is a circuit, not only an arbitrary dependency;
- it uses several active-pair families and both orientations;
- its parity-support graph is connected; and
- it cannot be reduced to a dependency on a proper subset of these 166
  values.

This establishes one fixed, factor-assisted structural diagnosis. It does
not establish:

- minimum dependency or minimum useful support in the full F98 pool;
- an inverse-polynomial density of useful circuits;
- an all-input progress law;
- a new factoring complexity bound;
- novelty relative to published relation-collection methods; or
- a polynomial-time factoring algorithm.

`RESULT.md` explicitly disclaims an unbounded theorem and an all-input law.
Its comment about smoothness and shared factors is a hypothesis compatible
with this finite instance, not a proved asymptotic explanation. The result
is not publication-level evidence by itself.

## 10. Manifest defect

`RUN_MANIFEST.md` pins the design, source, runner, output, log, failed-run
note, and F98 input. It does not pin `RESULT.md`. The current result hash is:

```text
60309c5ba6473eed0967efebb49d0bafbdcb7ef0a630859d722df67c152aa538  RESULT.md
```

Add this pin when correcting the result. This omission does not affect the
independent arithmetic, but it leaves the stated conclusion outside the
manifest's frozen evidence chain.

## Exact correction required

To pass re-audit while retaining the current computation:

1. Rename the 230-row object everywhere to "prime-valuation parity matrix,"
   "odd-valuation support," or another term that clearly includes 2.
2. Rename the output keys `odd_prime_row_count` and
   `pairwise_odd_support_intersections` consistently, or explicitly define
   "odd" as modifying valuation rather than prime.
3. Replace "five distinct trajectories" with "five active-pair families
   spanning eight oriented trajectories."
4. Add the `RESULT.md` hash to `RUN_MANIFEST.md`.

No change to rank, nullity, circuit minimality, connectivity, or the root is
required.

## Final decision

**FAIL.** The circuit theorem for the fixed 166-value certificate is correct.
The failure is limited to two object labels and one manifest omission. The
candidate can pass after those exact corrections and a frozen re-audit.
