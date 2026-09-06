# F156 V2 hostile re-audit — PASS

## Frozen inputs

I read the following files in full before writing this re-audit:

- `V2_STATEMENT.md`;
- `V2_PROOF.md`;
- the preserved V1 `HOSTILE_AUDIT.md`;
- the preserved V1 `BLIND_RECONSTRUCTION.md`;
- `MANIFEST.md`.

The two V2 hashes match the expected frozen values:

- `V2_STATEMENT.md`:
  `71b640469c0f57440d8e290b63af411eb33ee08b08c814413b5a04fff1c7d3dc`;
- `V2_PROOF.md`:
  `37e80fc0600eeb5a178f9e31c1f68f17b29ba3ed8837dcb5e391be0d6e5ef685`.

I did not edit a frozen input, the manifest, or a durable ledger. I ran no
research computation.

## Verdict

**PASS.** V2 repairs both defects reported by the V1 blind reconstruction.
The ordinary P118 batch now precedes construction of the same-stage base
section, and the statement now says exactly that nonempty subsets enumerate
the nonidentity part of that section. The omitted identity is inert in every
channel claimed by F156.

The remaining theorem is still only a deterministic source-and-cost theorem:

\[
2^{O((\log n)^6)}.
\]

It is not a progress theorem and not a factoring algorithm. I found no
algebraic, ordering, metadata, termination, or complexity counterexample to
the frozen V2 claims.

The F154 comparison has one important scope boundary. F156 exposes the full
list of nontrivial F154 inverse representatives when `r <= D`; it then uses
its own descendant-only rule for deciding which refined blocks become future
named generators. Therefore “captures the exact F154 refinement opportunity”
is correct as an endpoint-exposure claim. It does not mean that F156 adopts
every future grammar that F154 leaves open. The statement already specifies
the narrower F156 grammar.

## 1. The stage order is now unambiguous

The no-factor order at one named stage is now:

1. freeze the named basis;
2. complete the ordinary P118 word scan and append its base records;
3. factor-free-refine the accumulated distinct base values and select the
   actual lifted parity basis;
4. complete the sparse section scan;
5. jointly refine the endpoints from both scans against the frozen named
   basis;
6. continue only if an old named block split.

This order matters. If the section were formed before step 2, it could omit
the new base records made at the same stage. If a split were applied before
step 4, the section menu and the named menu would not belong to one frozen
stage. V2 rules out both failures.

The base ledger is cumulative, but the feedback ledger is excluded from all
later section bases. A feedback endpoint may still split a named block, and
that split may change a later ordinary P118 batch. This is controlled
indirect feedback. It is not recursive closure of the feedback relation
rank.

## 2. The base decorated lifts are actual and public

Every base value has an exact presentation

\[
A_i=t_i^2Q(v_i)\equiv1\pmod N.
\]

Because `A_i` is a unit, all of its factor-free blocks and `t_i` are units.
Thus

\[
(t_i^{-1})^2\equiv Q(v_i)\pmod N,
\]

so

\[
e_i=(v_i,t_i^{-1})
\]

is an actual public decorated lift. No factor of `N` and no hidden CRT sign
is used.

First-occurrence binary elimination chooses independent parity vectors and
keeps the corresponding actual lifts. For every subset `S`, their
star-product is therefore a public element

\[
e_S=(v_S,z_S),
\qquad
z_S^2\equiv Q(v_S)\pmod N.
\]

Changing a basis lift by a global sign can change its least-positive integer
endpoint, so retaining the actual lift is necessary. V2 does retain it. The
P138 consistency test has the right role: a non-global dependence factors
`N`; otherwise the observed records agree with one quotient section. The
sparse source itself still uses the selected actual lifts, not an abstract or
hidden section.

## 3. The direct screen is exact

Take the least-positive representatives of `z_S` and its inverse `w_S`.
Since `z_S` is a unit and `z_S w_S` is one modulo `N`, multiplication by
`z_S` preserves gcd with `N`. Hence

\[
\begin{aligned}
\gcd(z_S-w_S,N)
 &=\gcd(z_S^2-1,N)
  =\gcd(Q(v_S)-1,N),\\
\gcd(z_S+w_S,N)
 &=\gcd(z_S^2+1,N)
  =\gcd(Q(v_S)+1,N).
\end{aligned}
\]

These are gcd identities obtained from congruences modulo `N`. They do not
require expansion of the possibly dense integer `Q(v_S)`. Computing
`z_S^2 modulo N` is sufficient.

The direct screen is independent of a global sign change in `z_S`, although
the canonical integer endpoint presentation need not be. This is another
reason the frozen actual-lift convention is needed for refinement.

## 4. The identity is inert in every claimed channel

The empty basis subset gives the group identity, not a second lift over zero:

\[
v_0=0,
\qquad z_0=w_0=1,
\qquad F_0=1.
\]

On the surviving odd-input branch its direct screens are

\[
\gcd(1-1,N)=N,
\qquad
\gcd(1+1,N)=1.
\]

Thus it gives no proper factor. Endpoint `1` cannot split a nontrivial named
block. Exact value `1` has the zero parity vector and supplied root `1`, so it
adds no decoder direction and no non-global root. In F154 its manufactured
value is also

\[
P_0=1^2Q(0)=1.
\]

Therefore omission of the identity changes none of these outcomes:

- direct screening;
- named endpoint refinement;
- exact-value retention;
- the final normalized-root image;
- the F154 refinement-mediated endpoint opportunity.

An even `N` is removed by the elementary factor `2` before this source, as
the statement requires.

## 5. Deduplication preserves both algebra and endpoint data

Every feedback candidate gives

\[
F_S=z_Sw_S=1+\kappa_SN,
\qquad
1\le F_S<N^2.
\]

Different subsets can produce the same exact integer and can still carry
different endpoint presentations or provenance. V2 preserves the necessary
order:

1. run the two screens;
2. expose both endpoints;
3. retain the source occurrence and its ledger metadata;
4. delete only a duplicate algebraic exact value.

Two copies of the same exact value have the same parity row and supplied root
`1`. Their duplicate dependency has positive root equal to that exact value,
which is `1 modulo N`. Removing the duplicate algebraic column therefore does
not change the useful normalized-root image.

Ledger membership must follow occurrences, not only the first exact value.
In particular, a later P118 occurrence makes a value a base occurrence even
if the same integer first appeared in feedback. The two-ledger definition and
the requirement to retain every source occurrence support this convention.
Feedback-only occurrences remain excluded from later section bases.

## 6. Descendant-only refinement gives finite termination

Let `A_0` be the fixed initial P118 named endpoint product. F156 admits a
future named generator only when it is a terminal factor of an old named
block. Consequently every named block remains a divisor descendant of
`A_0`.

Complete multiplicity-aware factor-free refinement and perfect-power
normalization make a strict named stage refine at least one old block into
more terminal descendants. A refinement forest rooted at `A_0` has at most
its number of prime factors with multiplicity, and this is at most the bit
length

\[
\Lambda_0=2^{O(L^2)}.
\]

Thus the number of strict stages is at most `2^{O(L^2)}`. Probe-only
cofactors cannot enlarge this forest because they do not become named
generators.

If one stage produces no old-block split, the named basis is unchanged. Its
ordinary P118 menu, cumulative base ledger, selected section basis, and
one-layer feedback menu would all repeat. Stopping at that point is valid.
This proves termination only. It does not prove that the terminal state
contains a factor.

## 7. The quasipolynomial bound survives all explicit data

P118 supplies the bounds

\[
\Lambda_0=2^{O(L^2)},
\qquad
R_0=2^{O(L^4)}
\]

for the initial named product and the cumulative base records, including the
extra descendant stages allowed here. The base parity rank satisfies
`r <= R_0`. With `D=L^2`, one sparse section menu has at most

\[
\sum_{j=1}^{D}\binom rj
\le (D+1)\max\{1,r\}^{D}
=2^{O(L^6)}
\]

candidates. Multiplication by `2^{O(L^2)}` stages leaves the exponent
`O(L^6)`.

Each modular coordinate and endpoint has `O(n)` bits. Each feedback exact
value has fewer than `2n` bits. Base factor-free coordinates have total
quasipolynomial length. Actual-lift provenance, all endpoint presentations,
and occurrence-layer metadata add at most a polynomial factor to the
explicit transcript size.

Standard gcd-free refinement, perfect-power extraction, modular arithmetic,
binary elimination, and kernel-basis root evaluation are polynomial in that
explicit size. The complete decoder does not enumerate every kernel word; it
tests a kernel basis because the normalized-root map is a homomorphism. Thus
all source, storage, refinement, and decode work stays within

\[
2^{O(L^6)}=2^{O((\log n)^6)}.
\]

No hidden expansion of dense `Q(v_S)` and no recurrence of the form
`R -> R^D` across feedback layers occurs.

## 8. Dense provenance is a real grammar distinction

A P118 support count is measured in current named integer blocks. The F156
support count is measured in retained relation-basis vectors. One relation
vector can already be dense in the factor-free block coordinates. Therefore
the xor of at most `D` relation vectors can have far more than `D` old-block
coordinates.

This proves a syntactic enlargement of the declared source grammar. It does
not prove that the resulting modular residue is absent from the complete
P118 residue set, and it does not prove that the enlarged grammar has a
higher factoring success rate. V2 states both limits.

## 9. The repaired F154 inclusion is exact at the endpoint level

If `r <= D`, every nonzero vector in the base parity span has one nonempty
basis representation of size at most `D`. F156 therefore computes every
nonidentity actual lift `(v,z_v)` selected by that basis and exposes

\[
s_v=\iota_N(z_v).
\]

These are exactly the nontrivial inverse representatives used by the
corresponding F154 section completion, provided the same first-occurrence
actual section is used. The sole missing vector is zero, and Section 4 above
proves that its endpoint and value are inert.

The new retained value `z_v s_v` is not the F154 manufactured value
`s_v^2Q(v)`. This does not weaken the endpoint-refinement inclusion: the
integer `s_v` is exposed directly, and all endpoint presentations survive
deduplication. It may also give new final decoder data through `z_v s_v`.

The inclusion stops at this exact point. F156 keeps as future named
generators only descendants of old named blocks. F154 deliberately leaves a
broader class of later grammars open. V2 does not claim equality with those
broader grammars or a forced refinement.

## 10. The remaining gate is genuinely open

Nothing in the proof forces any of the following:

- a proper direct gcd;
- a split of an old named block;
- a productive later stage after a split;
- a new parity dependency;
- disagreement between the base and feedback sections;
- a non-global normalized root in the final union decoder.

The algorithm can terminate with every screen null, no old-block split, and
only global roots in the final decoder. V2 expressly permits that outcome.
Its exact contribution is a new, finite, deterministic quasipolynomial
source grammar whose success law remains to be proved or refuted.
