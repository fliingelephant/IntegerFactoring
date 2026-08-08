# F98 hostile audit

## Verdict: **PASS**

The frozen F98 candidate passes strict audit for its stated finite claim.
On the fixed input $N=202{,}537{,}109$, the public executable receives only
$N$. It finds no direct canonical-inverse sign hit. Its factor-free relation
decoder then returns a correct factor from 166 distinct relation values.

The separate 5,616-relation diagnosis also passes. It has no useful circuit
of support one, two, or three. Its first useful online Gaussian circuit has
166 distinct values. This does not prove that 166 is minimum.

F98 does not give an all-input progress law or a polynomial-time factoring
algorithm. It also does not prove a new result about the abstract subgroup of
units. Its exact gain is at the level of retained integer presentations and
their joint square-class decoder.

## 1. Frozen candidate

I pinned the candidate before reading it. Every hash in `RUN_MANIFEST.md`
matched its current file:

```text
6f4ff30185cef38effd1cc0954f1d30504a5ba216144c422446cf4da8a014273  DESIGN.md
f2d28d074d53bc93c675553b28e083b93b0d6dd35d1a65edb430c69a6cd26fb0  RESULT.md
5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b  public_factorization_free_replay.py
7525f1eba47d154143e4df7706ed4c9150abd988927c999217dde01062a1438b  run_public_replay_with_timeout.py
6cf67bb5928248ad139daa374a805d463859a67d2a398303c6153d2b4defd7c7  PUBLIC_REPLAY_RUN.log
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  PUBLIC_REPLAY_OUTPUT.json
749e4c2c43d78d895aa53de685b719b051c6115135df6a9b51cb8d3ac7b3ffb6  analyze_minimum_circuit.py
90fde9c43fdb1797832ab2e97adddb442c7e692e852be0aaa324ecc41827cc76  run_minimum_circuit_with_timeout.py
433d12eef1de0407f85f74f7e102a05e41a8d358da135e44a253d8c8aa7ba6bb  SMALL_SUPPORT_RUN.log
3896034b332f55b0cd1b8302eecf117c26e9c3dcb934eb7b7912f332d49aa8c2  SMALL_SUPPORT_OUTPUT.json
d1cdf08cb99a26d671484d7b566442620d73a7d6c8c1958a79100b83d66788e7  search_direct_trajectory.py
3e611505a98e8fc8a54cfb6c707298fa150c277f6f6cd4bf84ca007fd20dec25  run_direct_10k_with_timeout.py
1d6be67149c368f9ec7810b3baec5e3900b60754891b0c101271455c5534a73c  DIRECT_10K_RUN.log
738a5738b6909ae3528d3eb9aea5194d510b56b0772bd476db742cd4ee902ea8  DIRECT_10K_OUTPUT.json
b68a07945899395649a5373f6d321009bb42cf072dfad9342392d2c8fd7c8c0a  ../F59_completion_bias_generic_decoder_scan/scripts/F59_D01_scan.py
```

The manifest hash itself is:

```text
cfc8e9e7d2a87e730305ce11e2c612a0c4a449f7b05f714c8b41eb9fa09e94c3  RUN_MANIFEST.md
```

I read `RESULT.md`, `DESIGN.md`, `RUN_MANIFEST.md`, both final sources,
both runners, both outputs, and both logs completely. I also checked the
discovery screen and its full 162-row trace.

One non-core manifest omission exists. `search_direct_trajectory.py` imports
`search_factor_assisted.py`, but the manifest does not pin that dependency.
I read and pinned its current version:

```text
cbf50afc19a387ee58dffa9b0cca9a4ac2e732265c1b841cb535907cce364479  search_factor_assisted.py
```

This omission does not affect the result. Discovery only selected the fixed
input. The final public replay does not import either discovery source, and
the exact certificate is independently checkable from $N$.

## 2. Clean public replay: PASS

I ran the frozen public source under a new 120-second timeout. The executable
received exactly these data:

```text
--modulus 202537109
--output AUDIT_PUBLIC_REPLAY_OUTPUT.json
```

It finished in 50.85 seconds with exit code zero. Its JSON object is exactly
the pinned public JSON after removal of the nondeterministic
`elapsed_seconds` field.

The audit-owned files are:

```text
42e2d78e22bf8d1ffb7549c92fda3cd74e594dbc6c8152dd50b051d28a3f7596  AUDIT_PUBLIC_REPLAY_OUTPUT.json
2b30405fd46a1c6cb9bd5963f2bce596dff462d13c84eaedf4b094a4f71d4c79  AUDIT_VERIFY_OUTPUT.json
bd36a74f79c4832e01ae7acd02831fd2d946e4c54bfa0c93ea1117b9719d4271  AUDIT_RUN.log
301e59e822ed474914cbc4dda31ace75cc35af1efb11fb0e8b811d38a429cb01  hostile_audit_verify.py
6d04696d38d21feedf1b55847f7f4915f83ad272252a098727efbfd1ec3af311  run_hostile_audit_with_timeout.py
```

The verifier is independent of the candidate arithmetic. It does not import
candidate functions. It uses Sage factorization only as an audit method to
reconstruct prime square classes.

## 3. Input and trial screen: PASS

Independent factorization gives

\[
202{,}537{,}109=10{,}267\cdot19{,}727.
\]

Both factors are prime. Also

\[
g=\gcd(10{,}266,19{,}726)=2,
\quad A=5133,
\quad B=9863,
\]

and

\[
\gcd(AB,N-1)=1.
\]

Thus the stated P98 stability certificate is correct. The bit length is 28,
so the public trial bound is $28^2=784$. The least factor is 10,267. No
trial gcd from 2 through 784 is proper.

## 4. No hidden factor or target: PASS

The public source has no import except the Python standard library. It has no
copy of either factor, either final root, the prefix length 5,616, a target
word, a target exponent, or a target square class.

Its data flow is public:

1. It derives $n$ and $n^2$ from $N$.
2. It makes seeds 2 through $n$.
3. It computes canonical inverses with modular inversion.
4. It derives the initial gcd/perfect-power basis from integer endpoints.
5. It derives all active block pairs from that basis.
6. It enumerates both declared trajectories in fixed order.
7. It refines all retained endpoints by gcd and decodes binary dependencies.

It does not call factorization, primality testing, order finding, discrete
logarithms, or an equivalent oracle. The only extraction calls are the
declared gcd tests.

## 5. Complete direct screen: PASS

The public run retains 27 seed residues and 12,522 new trajectory residues.
This gives 12,549 unique residues. I regenerated the full stream and tested
both

\[
\gcd(c-w,N),\qquad \gcd(c+w,N)
\]

for every first occurrence, where $w=c^{-1}_{\rm can}$. There are no
proper gcds. Skipping a repeated residue is safe because its canonical
inverse and both gcd values are unchanged.

Therefore the factor is not a hidden direct hit. The algorithm must use its
retained relation state.

## 6. Factor-free decoder: PASS

The decoder first removes one value $P=1$ and 3,134 repeated relation
values from the binary matrix. This is safe. Two copies of the same positive
relation value make the square $P^2$, whose positive root is
$P\equiv1\pmod N$. Removing pairs of copies cannot change a useful root.
The source retains the original presentations and provenance.

For every endpoint, the gcd refinement tracks its binary incidence mask.
When two blocks overlap by $d$, the mask of $d$ becomes the xor of their
masks. This preserves every prime-exponent parity. At termination, surviving
blocks are pairwise coprime. An exact-square block creates no parity row. A
nonsquare block creates one row. Thus the resulting row kernel is exactly the
set of relation subsets whose integer product is a square.

The binary routine returns a full kernel basis. Testing only that basis is
sufficient. The map from a relation dependency to its square-root residue is
a homomorphism into the roots of one modulo $N$. If every basis root were a
global sign, every kernel root would be a global sign.

The replay reproduces:

```text
raw relation values       12,549
zero values                    1
repeated values            3,134
distinct nonzero values    9,414
nonsquare parity rows      11,015
rank                        8,926
kernel dimension              488
```

The first useful public basis certificate has 166 columns. All 166 relation
values are distinct. Each record satisfies

\[
1\le c,w<N,
\quad w=c^{-1}_{\rm can},
\quad P=cw,
\quad P\equiv1\pmod N.
\]

I multiplied all 166 values and took the exact integer square root. It gives

\[
R\equiv132{,}013{,}085\pmod N,
\]

\[
\gcd(R-1,N)=19{,}727,
\qquad
\gcd(R+1,N)=10{,}267.
\]

The selected public columns also map exactly to their stated raw stream
indices and witness records.

## 7. Support one, two, and three: PASS

I regenerated the first 5,616 relations in public order. I independently
factored their endpoints and built prime-exponent parity vectors. This gives
5,658 prime rows. It is independent of the candidate's factor-free 5,607
coarser rows, but both descriptions have the same square-class kernel.

The independent exhaustion gives:

```text
support-one circuits                         1
useful support-one circuits                  0
support-two circuits                     1,847
useful support-two circuits                  0
support-three first-right cases          1,530
useful support-three cases                   0
```

The one support-one circuit is the trivial value $P=1$.

Every support-two circuit uses two equal relation values. Its product is
$P^2$, so its connecting root is $P\equiv+1\pmod N$. It is global.

The first-right compression for support three is exact. Fix ordered left and
middle columns. Every valid right column is in one required parity class.
Any two such right columns have equal relation values, as established by the
complete support-two check. Replacing one right column by another therefore
does not change the triple product or its positive square root. Testing the
first right column in each case tests all possible right columns.

An independent online elimination finds its first useful circuit at relation
ordinal 5,616. Its support is 166. The pinned diagnostic certificate has 166
distinct values and gives

\[
R\equiv70{,}524{,}024\pmod N,
\]

\[
\gcd(R-1,N)=10{,}267,
\qquad
\gcd(R+1,N)=19{,}727.
\]

This proves only a lower boundary of four for useful support in that prefix.
It does not exclude useful supports from 4 through 165.

## 8. The two 166-column certificates are separate

The full public certificate and the prefix diagnostic certificate must not
be conflated.

| Property | Full public round | Pinned prefix diagnosis |
|---|---:|---:|
| relation pool | 12,549 raw | first 5,616 raw |
| root modulo $N$ | 132,013,085 | 70,524,024 |
| support | 166 | 166 |
| largest raw index | 12,540 | 5,615 |

Their index sets and relation-value sets are different. Each certificate is
valid independently.

## 9. Polynomial bit complexity: PASS for the declared bounded rule

Let $n$ be the bit length. The trial screen has $n^2$ gcd calls. A full
C2T rule with $n$ rounds, at most $n$ expanded presentations per round,
two trajectories, and $n^2+1$ exponents retains $O(n^4)$ presentations.

Each residue and endpoint has $O(n)$ bits. Each relation value has $O(n)$
bits. Gcd refinement never creates a larger integer block. Its binary masks
have polynomial length. The total number of effective block refinements is
bounded by the total endpoint bit length. Naive pair scans can be large, as
the replay shows, but remain polynomial.

The binary matrix has polynomial dimensions. A selected exact product has at
most polynomially many $O(n)$-bit factors, so its integer square root also
has polynomial bit length. Modular arithmetic, exact roots, gcd operations,
and binary elimination all have polynomial bit cost.

This establishes that the declared finite-round procedure is a uniform
polynomial-time procedure. It does not establish that it succeeds on all
inputs.

## 10. Wording and exact scope

The candidate's narrow mechanism wording is supported:

- one direct canonical-inverse residue does not expose the factor;
- many nonclosing presentations are retained;
- factor-free refinement and binary decoding combine them;
- one actual decoder certificate uses 166 distinct relation values; and
- in the pinned prefix, no pair or triple can replace the larger circuit.

This is a real algorithm-level change from selecting one scalar and applying
one gcd. The final extraction still uses gcd, as every congruence-of-squares
decoder does.

The evidence does **not** establish any of these stronger claims:

- success for every composite or every stable semiprime;
- inverse-polynomial success density;
- a useful polynomial-size circuit on every input;
- progress in every later feedback round;
- minimum useful support 166;
- expansion of the abstract multiplicative subgroup;
- novelty relative to all published factoring methods; or
- a classical polynomial-time factoring algorithm.

`RESULT.md` states these main limitations. I found no hidden promotion of the
fixed witness into an unbounded theorem.

## Final decision

**PASS.** F98 is an exact and reproducible finite witness of an amortized
canonical-presentation decoder. Its strongest valid lesson is that retained
integer presentations can provide useful joint square-class information even
when every individual direct sign test is null. The missing step remains an
all-input progress or density theorem.
