# F264-D03 V3 preregistration — noncommutative matrix-word lift search

## Status and purpose

This packet freezes a narrow operational repair of the finite C++17 discovery
experiment. V1, V2, and both hostile **FAIL** audits remain byte-for-byte
unchanged. V3 searches public
two-generator matrix representations for exact gcd tickets, certified common
order, and P205 residual support. It is not a proof of a factoring algorithm.
Hidden factors label outcomes only. They never select a generator, word,
expression, order trial, or retained candidate.

The source is materially different from F258--F263. It uses ordered words in
two noncommuting `SL_2` generators, their canonical lifts modulo `N^2`, and
exact multiplication and associativity carries. F264 is incompatible with
every F258--F263 production or validation run. Compilation, self-test,
benchmark, discovery, and held-out execution all use the same firewall.

## Prior-boundary audit

The full registries and ledgers were indexed before this design. The decisive
boundaries are P164, P170, P187, P191, P197, P205, P208, P209, P212, and P219.

- P164 warns that many public actions can remain one cyclic direction.
- P170 closes several explicit separating-representation shortcuts.
- P187 closes scalar abelian character products, but explicitly leaves
  nonabelian and ring-valued data open.
- P191/F217 shows that ordinary character traces can compress to the divisor
  sum target without supplying its evaluator.
- P197 permits lcm accumulation from unrelated certified primary blocks.
- P205 and P208 permit an unfactored integer word, but still require a public
  source that captures a hidden residual.
- P209/F244 kills numerical-QP products of signed powers of `N` on an infinite
  four-marker family. It explicitly leaves carries, differences,
  discriminant-dependent words, and retained-relation words open.
- P212/F245 closes fresh inverse-quotient words with no current-point feedback.
- P219 gives a separate signed Pell-resultant ticket and is not reused here.

Every trace-only `SL_2` expression is therefore a control. Fricke,
Cayley--Hamilton, trace cyclicity, inverse-trace, and determinant identities
are mined and canonicalized before any semiprime score. The ranked families
retain ordered matrix coordinates and exact lift carries. These are not
conjugacy-invariant character data and do not collapse to the three Fricke
coordinates. The source also feeds each retained word into its next generator
step, which lies outside F245's no-current-point-feedback grammar.

F244's marker theorem does not apply syntactically: F264 words are not
products of `N^k+1` and `N^k-1`. They are nonlinear functions of the entries
and exact lift carries of a public noncommuting word transcript. This is only
a reason to test the seam. It is not evidence that the words hit a marker.

## Frozen public source

For each public odd `N`, derive two profiles from the public hash of the
complete integer `N` and the constants in `V3_symbolic_search.cpp`. In each
profile, `a`, `b`, and `u` are the first units in three deterministic streams
of at most 128 public nonzero residues. Every rejected nonunit receives an
exact public gcd screen and preserves any proper factor certificate. Exhausting
128 attempts aborts. The value `c` is one public nonzero residue and is also
gcd-screened. This bounded rule makes both `a` and `b` units, so `U(a)` and
`L(b)` do not commute modulo odd `N`; the executable verifies this for both
profiles.

The main generators are

```text
A = U(a) = [[1,a],[0,1]],       A^-1 = U(-a),
B = L(b) = [[1,0],[b,1]],       B^-1 = L(-b).
```

They are interpreted as exact determinant-one integer matrices and reduced
canonically modulo `N^2` after every multiplication. Enumerate every reduced
word of length 1 through 7 over `{A,A^-1,B,B^-1}`. Adjacent inverse letters
are forbidden. There are exactly 4,372 words per profile and 8,744 main words
per input. Enumeration order is length, then base-four word code.

The cyclic-direction controls are public conjugates of

```text
diag(u,u^-1)  by U(c).
```

Their order is the scalar order of `u`; they are never interpreted as a new
noncommutative direction. They check that the order engine rediscovers known
split certificates without falsely calling them novel.

For a word matrix `R` modulo `N^2`, write entrywise

```text
R = r + N*C,       0 <= r_ij < N,       0 <= C_ij < N.
```

The four entries of `C` are the word-lift principal digits. For a generator
step, pair, or triple, construct every quotient only from an exact integer
identity in `V3_ALGEBRA.md`. The executable aborts on a failed divisibility
test.

To keep the full word layer resource-safe, scalar row families use the public
coordinate `q=SplitMix64(N,profile,word code,length,tag,source seed) mod 4`;
a two-coordinate
minor uses `(q,q+1 mod 4)`. Pair and triple families use the analogous public
hash of their complete scope. Commutator families retain all four coordinates.
Thus every listed family is exhaustive for its frozen coordinate projection.

## Frozen sparse scopes

All 8,744 words contribute row atoms. Word caps rank all 4,372 profile words
by a SplitMix64 key of `(N,profile,length,word code,scope tag,source seed)` and
retain the fixed number with smallest `(key,index)`. These caps are per
profile:

```text
generator commutators and Fricke carries: 1,024 words
pair/collision/minor scopes:               1,024 pairs
triple/associator scopes:                    256 triples
```

The smooth-order scope is one global scope:

```text
profile 0 main words:  8
profile 1 main words:  8
profile 0 controls:    1
profile 1 controls:    1
total matrices:       18
factored schedules:    2
total order trials:   36
```

Enumerating and hash-ranking all `C(4372,3)` triples per input would violate
the resource envelope. V3 does not claim to do that. Instead, pair and triple
tuples have their complete lexicographic ranks in `C(4372,2)` and
`C(4372,3)`. SplitMix64 applied to `(N,profile,scope tag,source seed)` selects
a start and a candidate step. The source searches at most 4,096 consecutive
candidate steps for the first one coprime to the universe size, then traverses
the resulting affine permutation for exactly the cap. It aborts if no step is
found. Combinatorial unranking is exact. Thus selection is bounded,
collision-free, and factor-blind. A tuple's rank uniquely encodes every word
length and code. No hidden label, prior score, rejection refill, or unbounded
retry enters a scope.

## Frozen 30-family static grammar

The exact family list and normalized schemas are compiled into the source:

```text
01 low_entry_control              entries of r
02 lift_entry                     entries of C
03 lift_trace                     tr(C)
04 lift_antitrace                 C00-C11 and C01-C10
05 determinant_N2_quotient        (det(R)-1)/N^2
06 cayley_hamilton_N2_quotient    (R^2-tr(R)R+I)/N^2 entries
07 step_carry_K                   K(r_parent,r_generator)
08 step_carry_digit               K mod N
09 step_second_carry_H            (K-(K mod N))/N
10 step_cross_minors              one projected minor for each of
                                  (K,C_parent),(K,C_word),(C_parent,C_word)
11 commutator_low                 entries of [W,G] mod N minus I
12 commutator_lift                lift entries of [W,G]
13 commutator_trace_lift          trace lift of [W,G]
14 fricke_N2_quotient             exact Fricke residual divided by N^2
15 fricke_pair_difference         differences of Fricke quotients
16 trace_collision                tr(W_i)-tr(W_j)
17 commutator_trace_collision     commutator-trace differences
18 lift_collision                 coordinate differences of lift vectors
19 low_entry_minors               2-minors of low word vectors
20 lift_minors                    2-minors of lift word vectors
21 mixed_low_lift_minors          mixed 2-minors
22 digit_associator_quotient      exact digit associator divided by N
23 associator_second_carry        second-carry side of the associator
24 word_finite_difference         first differences on public triples
25 word_second_difference        second differences on public triples
26 trace_hankel_minor             t0*t2-t1^2
27 lift_hankel_minor              coordinate lift Hankel minors
28 character_discriminant         tr(r)^2-4*det(r)
29 split_root_residual            one original-basis and one conjugate-basis
                                  proposal residual per word
30 conjugacy_coordinate_control   selected differences of low,lift,K,k,H
```

The exact global zeros are counted in ten separately named counters and never
inserted into an integer word: full matrix associativity, its second-carry
quotient identity, trace cyclicity, inverse trace, Fricke modulo `N^2`,
Cayley--Hamilton modulo `N^2`, determinant multiplicativity, determinant-one
word residues, conjugacy invariance of trace, and conjugacy invariance of
determinant. The row output retains every counter.

## Typed synthesized grammar

For each family form its public atom sum `S_f` and atom product `P_f`, reduced
modulo the scoring modulus. Zero is excluded from the product. Both `+1` and
`-1` remain in the sum and product after they are counted. The bounded
expression DAG contains:

```text
leaves:       S_f, P_f
unary:        S_f+P_f, S_f-P_f, S_f*P_f
pair:         S_f +/- S_g, P_f +/- P_g, S_f*S_g,
              S_f*P_g-P_f*S_g, S_f^2+S_g^2,
              S_f^2-4*P_f, and the quadratic resultant template
triple:       S_f-2*S_g+S_h and
              det([[1,S_f,P_f],[1,S_g,P_g],[1,S_h,P_h]])
```

Pair and triple operands are in increasing family order. Commutative operands
are syntax-sorted. Candidates are canonicalized by normalized syntax and two
evaluation fingerprints on public synthetic residues modulo `1000000007` and
`1000000009`. On a fingerprint collision the shortest normalized syntax is
retained and the alias count is recorded. No factor-labelled beam pruning is
used: the complete canonical survivor list is scored on both splits.

An accumulator evaluation is only a residue modulo the scoring modulus.
For direct tickets the identity

```text
gcd(candidate residue,N) = gcd(full public integer expression,N)
```

justifies the gcd. Residue accumulators are not called exact integer values.

## Public modular-nullspace controls

Before any semiprime score, use 96 public synthetic odd moduli and independent
public generator residues. Search all normalized coefficient vectors in
`{-1,0,1}` for the following feature matrices modulo `1000000007`:

```text
Fricke:       tr([A,B]), x^2, y^2, z^2, xyz, 2
associator:   six ordered scalar summands in
              K(z_uv,w)+K(u,v)w-K(u,z_vw)-uK(v,w)
trace cycle:  tr(AB), tr(BA)
Cayley:       three ordered scalar summands per matrix coordinate
det product:  det(AB), det(A)*det(B)
```

The associator columns are the exact six scalar columns displayed in
`V3_ALGEBRA.md`; the two coordinate products inside each matrix product are
not pre-aggregated. The engine enumerates all `3^d` coefficient vectors,
explicitly discards the all-zero vector, and normalizes a nonzero vector by
making its first nonzero coefficient positive. It must recover ranks
`5/6,5/6,1/2,2/3,1/2` for Fricke, associator, trace cycle, Cayley, and
determinant product respectively, with exactly one normalized ternary relation
in each matrix. It authenticates those five relations by exact or divisibility checks
on 64 disjoint public synthetic inputs. Unexpected extra ternary null vectors
abort validation.
This finite layer canonicalizes global decoys. It makes no statement about an
unbounded identity grammar.

A public unimodular conjugation control is also evaluated. Character-valued
features must remain unchanged. For every word step, all four entries of
`r,C,K,k,H` are hashed and counted in separate original-basis and
conjugate-basis transcripts. The 30th family contains five selected
coordinate differences. The raw streams remain controls and never enter a
family product.

## Operational score programs

### Direct factor tickets

Every exact atom is first made `N`-primitive by removing all exact powers of
`N`. This can change its gcd, as `N=15,a=45` demonstrates. V3 claims only
that a proper gcd of the resulting primitive integer is an exact factor.
Zero and units are counted. Units remain in the accumulators. Compute
`gcd(primitive_atom,N)` before multiplication into a family word. Every
synthesized candidate is also gcd-tested through its residue. Only a proper
gcd is a factor ticket. The output records zeros, units, removed `N` powers,
proper-gcd events, and the first public certificate.

### Certified common-order growth

For each frozen order word, test the two fully factored exponents
`lcm(1,...,64)` and `lcm(1,...,128)`. First compute the matrix power modulo
`N`. A proper gcd of all entries of `G^A-I` factors `N`. A global return is
stripped prime by prime. At each division, a proper gcd factors; gcd `N`
permits deletion; gcd `1` proves that no hidden prime component returned.
Thus, absent a factor, the final completely factored integer is the exact
common local matrix order.

It is added to the P197 lcm only if a public `s` satisfies

```text
s^2 = tr(G)^2-4 det(G) (mod N),     gcd(s,N)=1.
```

This certifies distinct split eigenvalues in every hidden prime component,
so the exact common matrix order divides every `r-1`. Candidate roots are all
14 original-basis and public-conjugate-basis proposals in `V3_ALGEBRA.md`; no
square-root oracle is assumed. Every order trial evaluates all 14 proposals
before any order-path return. It does not short-circuit after a unit root or a
proper gcd. Each input row records the total proposal count, total square,
unit, and proper-gcd matches, one check count for each of the 14 proposal
indices, and a deterministic transcript hash over every proposal residue and
outcome. The self-test requires 36 checks for every index and 504 total checks.
After the full 14-proposal loop, a retained proper gcd terminates that trial
with an exact factor. Otherwise a retained unit root is used only if the
smooth-order program reaches the split-certification gate.
Report the exact decimal accumulated certified
lcm, its bit length, and `max(0,bit_length(lcm)-1)` as new bits relative to the
initial lcm `1`.
The conjugated-diagonal results are reported separately as cyclic controls.

### Exact P205 residual improvement

For labels `N=pq`, put

```text
d=gcd(p-1,q-1),  s_p=(p-1)/d,  s_q=(q-1)/d.
```

The factors are first accessed only after all public atoms, family products,
and synthesized candidates are frozen for that input. Form the 467 public
word templates

```text
N-1;
(N-1)*P_f for each of 30 families;
(N-1)*P_f*P_g for every f<g;
(N-1)*product_f P_f.
```

Use `W=V^n`, where `n=bitlength(N)`. Products are evaluated modulo `s_p` and
`s_q`; this preserves the exact gcds. For every word record both residual
gcds, the exact integer baseline multipliers

```text
I_p=gcd(W,s_p)/gcd((N-1)^n,s_p),
I_q=gcd(W,s_q)/gcd((N-1)^n,s_q),
```

and the integer residual loss

```text
L=min(ceil(log2(s_p/gcd(W,s_p))),ceil(log2(s_q/gcd(W,s_q)))).
```

The two divisions defining `I_p,I_q` are checked exactly. Output reports the
lower median `L`, improvement count, and saturation count for every
`(factor_bits,cohort,word)` cell. No factorization of `W` is used.

## Frozen cohorts

Factor sizes and data split are

```text
discovery: 16,24,32 bits
held-out:  40,48,56,60 bits.
```

At each size generate disjoint deterministic balanced cohorts:

```text
random prime pairs:       384
consecutive prime pairs:  192
safe-safe prime pairs:    192, except 96 at 16 bits.
```

Both factors have the declared bit length and `p<q<2p`. Safe-safe means
`p=2r+1`, `q=2s+1` with all four integers prime. Duplicate moduli across all
cohorts in one executable split are rejected; different factor sizes cannot
duplicate. Total planned inputs: 5,280. Cohort seeds are frozen in
`V3_symbolic_search.cpp`. Safe-safe is the hostile cohort.

Every prime search examines at most `2^20` public starting points, with at
most 16,384 odd increments from each. Every safe-prime search makes at most
`2^20` bounded prime calls. The consecutive-prime scan checks at most `2^20`
odd successors. Each `(factor_bits,cohort)` fill accepts its prescribed count
within at most `2^22` outer attempts or aborts. Output records the attempt and
accepted counts. Pair and triple construction has no refill loop.

The executable opens only one named split per process. The runner completes
and validates discovery output, rechecks the firewall and resources, then
starts a new held-out process. It writes separate JSON, row TSV, anomaly TSV,
and logs for each split. Since the candidate universe is exhaustive and
frozen, discovery output changes no held-out candidate set or threshold.

## Frozen interpretation

- One proper gcd is an exact certificate for that input, but only an anomaly.
- A direct family is a finite lead only with at least 16 held-out hits across
  at least three held-out sizes and at least one safe-safe input. A synthesized
  candidate uses the same exact gate.
- A common-order lead uses the same `16 / three sizes / safe-safe` gate on rows
  with a noncyclic certified block and exact lcm greater than one. Cyclic
  controls do not count. The exact lcm across such rows is also reported.
- A P205 word is a finite lead only if its lower median `L` is at least two
  bits below the baseline lower median at every held-out size for both the
  safe-safe and random cohorts, and if its median growth from 40 to 60 factor
  bits is at most 16 bits in each of those two cohorts. These constants are
  frozen before discovery output. Consecutive cohorts remain diagnostic.
- Linear hostile-tail loss is a finite null for this grammar.
- Finite rates neither prove nor refute inverse-QP progress.

## Resource envelope and launch gate

The target is `seetacloud`. The runner uses at most 8 threads, `nice 15`, a
4 GiB virtual-memory limit, a 1 GiB uncompressed-output limit, and one shared
4-hour deadline covering compile, validation, both split runs, report checks,
and compression. The memory cap applies to compile, self-test, benchmark,
describe, both split runs, validation, and compression. The output cap counts
both output and logs and is monitored during every stage. Sparse anomaly rows
are capped; no candidate-by-atom dense matrix is emitted. The planned hot loop
has 8,744 word steps and both-basis carry controls, 2,048 pair scopes, 512
triple scopes, 36 smooth-order trials, and the complete canonical synthesized
candidate list per input.

The authoritative light benchmark is one complete largest 60-bit-factor
public pipeline, including word enumeration, pair/triple scopes, candidate
gcds, order trials, and P205 scoring. The runner refuses production unless a
conservative 1.75x eight-thread projection is at most 14,400 seconds and the
predicted output is below 1 GiB.

The runner checks processes before checksum authentication, compile,
self-test, every report parser, benchmark, describe, discovery, held-out,
report validation, compression, manifest construction, and the final output
gate. A two-second monitor
stops a running child if an incompatible process appears or owned bytes exceed
1 GiB. It refuses any active `F258` through `F263` job in every executable
mode. It checks at least 8 allowed CPUs, 8 GiB available RAM, 5 GiB free disk,
and one-minute load no greater than three times the allowed CPU count before
each material stage. The runner validates the exact ordered 2,560-field TSV
schema, exact JSON key schemas and dimensions, the ten exact ordered decoy
names and positive counts, exact family names, exact cohort cells, root-check
counts, candidate identifiers, and split labels before compression. Checksum
authentication, report parsing, compression, and manifest creation use the
same remaining deadline, 4 GiB limit, `nice 15`, firewall, resource gates, and
owned-byte monitor as the computational stages. The manifest is complete
before a final monitored aggregate-size and deadline check. No file is added
to the owned output after that check.

At freeze time this packet is **DO NOT LAUNCH pending fresh hostile audit**.
Any validation failure invalidates these bytes. It does not authorize a source
edit or relaxed gate. No durable ledger may be edited by this experiment.
