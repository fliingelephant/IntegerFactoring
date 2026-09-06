# F156 V2 blind reconstruction

## Provenance and verdict

The only source used for this reconstruction was `V2_STATEMENT.md`. Its
SHA-256 digest was verified before it was read:

```text
71b640469c0f57440d8e290b63af411eb33ee08b08c814413b5a04fff1c7d3dc
```

**Verdict: conditionally sound as a deterministic quasipolynomial source
construction.** The decorated-section algebra, the direct-screen identity,
the frozen schedule, the descendant termination argument, the
`2^{O((log n)^6)}` accounting, and the stated F154 inclusion all reconstruct
without a contradiction. The verdict is conditional because the statement
imports the P118 size bounds and descendant invariant, the P138 consistency
test, the F154 interpretation, and polynomial-time factor-free and decoder
primitives. Those imported results cannot be re-proved from this statement
alone.

This is not a conditional verdict about universal factoring success. The
last success gate is open by design. A surviving composite can reach the
final decoder without any promised non-global root.

## 1. Reconstructed decorated algebra

Let

\[
V=\mathbf F_2^m,
\qquad
Q(v)=\prod_{j=1}^m q_j^{v_j},
\]

and compute residue coordinates in \((\mathbf Z/N\mathbf Z)^\times\). For
two binary vectors define the carry monomial

\[
C(v,u)=\prod_{j:v_j=u_j=1}q_j.
\]

Then

\[
Q(v)Q(u)=Q(v\mathbin\oplus u)C(v,u)^2.
\tag{14}
\]

The decorated square-root extension required by the statement is

\[
E_Q(N)=\{(v,z):z^2\equiv Q(v)\pmod N\},
\]

with product

\[
(v,z)\star(u,y)
=
\left(v\mathbin\oplus u,
zyC(v,u)^{-1}\bmod N\right).
\tag{15}
\]

Equation (14) proves closure. The carry factors also give associativity
coordinate by coordinate. The product is commutative, its identity is
\((0,1)\), and

\[
(v,z)\star(v,z)
=
(0,z^2Q(v)^{-1})
=
(0,1).
\]

Thus this is an elementary binary extension, apart from any convention that
identifies the two global signs. Projection to the first coordinate is a
homomorphism onto the represented parity span.

For a base record,

\[
A_i=t_i^2Q(v_i)\equiv1\pmod N.
\]

Because \(A_i\) and every \(q_j\) are units, \(t_i\) is a unit. Therefore

\[
Q(v_i)\equiv t_i^{-2}\pmod N,
\]

so \(g_i=(v_i,t_i^{-1})\) really is an element of \(E_Q(N)\). This verifies
the direction of the inverse in (3). Using \(t_i\), instead of its inverse,
would not give the required lift.

Suppose \(b_1,\ldots,b_r\) is the selected parity basis and \(e_i\) is the
actual lift taken from the same record as \(b_i\). Define

\[
\sigma(\alpha_1,\ldots,\alpha_r)
=
\mathop{\star}_{i:\alpha_i=1}e_i.
\tag{16}
\]

This is a homomorphism. Its projection is
\(\sum_i\alpha_i b_i\). Independence of the \(b_i\) makes that projection,
and hence \(\sigma\), injective. Its image is therefore an actual lifted
section of the parity span. In particular, a nonempty subset of basis
indices gives a nonzero parity vector.

The P138 check concerns all base lifts, not the existence of the basis
section in (16). A parity dependency among arbitrary base records multiplies
to \((0,h)\), where \(h^2\equiv1\pmod N\). A root \(h\not\equiv\pm1\pmod N\)
gives a proper factor through \(\gcd(h-1,N)\) or \(\gcd(h+1,N)\). If no such
root exists, dependent lifts can still differ by the global sign. Thus any
claim that every original lift lies literally in one section must either
work modulo \(\{\pm1\}\) or fix signs. F156 only needs the actual basis lifts
and their products, so this global-sign point does not invalidate its scan.

## 2. Canonical inversion and the direct screens

For the numerical and cost claims, \(z_S\) and
\(w_S=\iota_N(z_S)\) must be the canonical integer representatives in
\(\{1,\ldots,N-1\}\), with

\[
z_Sw_S\equiv1\pmod N.
\tag{17}
\]

This is the meaning of canonical inversion forced by (8). It gives the
exact positive integer

\[
F_S=z_Sw_S=1+\kappa_SN,
\qquad 0<F_S<N^2.
\tag{18}
\]

Since \(z_S\) is a unit, multiplication by \(z_S\) does not change a gcd
with \(N\). Using (17) and \(z_S^2\equiv Q(v_S)\pmod N\),

\[
\begin{aligned}
\gcd(z_S-w_S,N)
&=\gcd(z_S^2-1,N)
=\gcd(Q(v_S)-1,N),\\
\gcd(z_S+w_S,N)
&=\gcd(z_S^2+1,N)
=\gcd(Q(v_S)+1,N).
\end{aligned}
\tag{19}
\]

These are exact gcd equalities because replacing an argument by a congruent
integer modulo \(N\) does not change its gcd with \(N\). Equation (9) is
therefore correct, with matching signs.

The exact integer \(Q(v_S)\) can be very large. It is not needed for (19).
Compute \(a=z_S^2\bmod N\), then compute \(\gcd(a-1,N)\) and
\(\gcd(a+1,N)\). This also explains why dense squareclass provenance does
not make a feedback exact value large.

If `iota_N` were instead a representative only up to sign, (17), (18), and
the displayed sign matching would need adjustment. The statement itself
rules out that reading by asserting \(F_S\equiv1\pmod N\).

## 3. Ledger and deletion semantics

The two-ledger rule has the following precise operational meaning.

1. The base ledger is cumulative and receives only exact canonical records
   from ordinary P118 named-word scans.
2. At a frozen stage, the section is built from the distinct exact values in
   that base ledger after factor-free refinement and perfect-power removal.
3. The feedback ledger receives at most the first record for each exact
   integer \(F_S\). “First” is deterministic because both the basis and the
   subset scan have deterministic orders.
4. Exact-value deletion has set semantics for decoder rows. A second copy of
   the same exact integer with the same supplied root adds no independent
   decoder information.
5. Endpoint presentations and source occurrences have multiset semantics.
   They are recorded before exact-value deletion. Two different pairs
   \((z_S,w_S)\) can have the same product but different refinement effects.
   Deleting the second product must not delete its endpoints or provenance.
6. The final decoder uses the union of the retained base and feedback exact
   records. No feedback exact record is allowed into the section basis at
   the same stage or at a later stage.

The statement does not say whether an exact value duplicated across the two
ledgers is physically stored twice. Either choice is algebraically harmless
if the ledger class remains attached to the surviving metadata and every
presentation is retained. A global deduplication can keep one decoder row;
the logical base/feedback tag must still prevent feedback provenance from
entering a future section.

This separation does not make feedback irrelevant to later stages. A
feedback endpoint can split an old named block. The descendants can then
change later ordinary P118 scans. The prohibited operation is direct use of
a feedback relation as a later section generator.

## 4. Frozen stage schedule

One stage reconstructs as follows.

1. Freeze the current named basis and its ordinary P118 menu.
2. Complete the full support-\(D\), exponent-\(E\) ordinary scan. Append its
   exact records only to the base ledger. Collect all ordinary endpoints.
3. Factor-free-refine the distinct cumulative base exact values. Remove
   maximal square powers to obtain the pairwise-coprime unit blocks and the
   parity vectors.
4. Run the complete P138 consistency test. Stop with a proper gcd if it
   finds a non-global root.
5. Choose the first-occurrence parity basis and freeze its actual lifts.
6. Enumerate every nonempty basis-index subset of size at most \(D\). For
   each subset, form its lifted product, run both direct screens, expose both
   endpoints, retain all presentations and occurrences, and retain the
   first feedback exact value.
7. Only after both menus finish, jointly refine the old named blocks by all
   collected ordinary and feedback endpoints.
8. If an old block strictly splits, freeze its allowed descendants as the
   next named state and start a new stage. If no old block splits, stop the
   source and run one complete decoder on the union ledger.

No discovery changes either menu during its scan. There is no feedback
fixed point inside a stage. A direct screen or the P138 check can terminate
early only because it has already produced a factor.

## 5. Descendant termination

Let \(X_0\) be the fixed initial named endpoint product. The stated bit bound
is

\[
\operatorname{bitlen}(X_0)=\Lambda_0=2^{O(L^2)}.
\]

The future named generators form a descendant factor forest of \(X_0\).
Probe-only cofactors do not become new roots of that forest. Every continuing
stage contains a strict split of an old node. Along a one-child retained
chain, the retained proper divisor loses at least one prime factor with
multiplicity. At a branching split, the total number of nonunit leaves is
at most the number of prime factors of \(X_0\), counted with multiplicity.
Consequently the total number of strict split events is

\[
O(\Omega(X_0))\le O(\log_2 X_0)=2^{O(L^2)}.
\tag{20}
\]

A stage with no strict old-block split does not repeat. It goes directly to
the final decoder. This proves source termination independently of whether
the final decoder factors \(N\). The descendant-only rule is essential: if
arbitrary probe cofactors became named generators, the fixed-product
potential in (20) would no longer apply.

## 6. Cost reconstruction

Treat the P118 claims

\[
T=2^{O(L^2)}
\quad\hbox{stages},
\qquad
R_0=2^{O(L^4)}
\quad\hbox{base records in total}
\tag{21}
\]

and quasipolynomial total base bit length as imported hypotheses. At every
stage, \(r\le R_0\). The feedback menu has

\[
C(r,D)=\sum_{j=1}^{\min(D,r)}\binom rj
\le (D+1)\max(1,r)^D.
\]

Since \(D=L^2\) and \(\log_2 R_0=O(L^4)\),

\[
\log_2 C
\le O(\log D)+D\log_2\max(1,R_0)
=O(L^6),
\]

so \(C=2^{O(L^6)}\). Multiplication by all
\(T=2^{O(L^2)}\) stages is absorbed into the same bound.

Each feedback occurrence stores two residues below \(N\), a product below
\(N^2\), a subset of at most \(D\) basis indices, and bounded provenance.
Dense parity vectors can be processed as vectors over the factor-free base
blocks. Their length is bounded by the imported total base representation
size. Modular carry products in (15) need only be evaluated modulo \(N\).
They do not require expansion of dense \(Q(v_S)\).

Standard gcd arithmetic, perfect-power extraction, factor-free refinement,
binary elimination, modular multiplication and inversion, and the final
kernel/root decode take polynomial time in their input representation.
Applying any fixed polynomial to
\(2^{O(L^6)}\) objects of quasipolynomial total bit length still gives

\[
2^{O(L^6)}=2^{O((\log n)^6)}.
\tag{22}
\]

Retaining every endpoint presentation does not change the exponent: there
are only two endpoint presentations per feedback candidate. The claimed
bound would not follow from the statement alone if the cited factor-free or
decoder primitives were superpolynomial; their usual polynomial bounds are
therefore part of the imported framework.

## 7. Dense provenance and strict source relation

The two support measures count different objects.

- A named word selects at most \(D\) current named integer blocks.
- A section word selects at most \(D\) basis relations.

One retained basis relation can have many nonzero coordinates after its
exact value is refined into the common \(q_j\) blocks. A record created when
a named block was coarse can also become dense in its later descendants.
The xor of at most \(D\) such basis vectors therefore has no support-\(D\)
bound in the old-block or refined-\(q_j\) coordinates. A one-term section
word can already be dense in those coordinates.

This proves a strict enlargement of the source syntax: bounded support is
measured in a new alphabet. It does not prove a strict enlargement of the
set of residues ever produced by P118. A dense section residue could
coincide with a residue obtained from a different named word or at a
different stage. The statement correctly makes only the syntactic claim.

## 8. Full-section and F154 inclusion

The map from subsets of \(\{1,\ldots,r\}\) to the parity span is bijective
because the \(b_i\) form a basis. If \(r\le D\), every subset is within the
support cap. The F156 scan therefore contains exactly one selected lift

\[
e_v=(v,z_v)
\]

for every nonzero vector \(v\) in the span.

Let \(s_v=\iota_N(z_v)\), which is the F154 canonical inverse endpoint
described in the statement. Then

\[
P_v=s_v^2Q(v)\equiv z_v^{-2}z_v^2\equiv1\pmod N.
\tag{23}
\]

With supplied root \(1\), normalization of this manufactured relation gives

\[
(v,s_v^{-1})=(v,z_v)=e_v
\]

in the decorated group. Thus \(P_v\) contributes a lift already generated
by the base section. It cannot add a new decoder dependency or a new
non-global root. This is the precise sense in which the manufactured F154
relation is decoder-inert. Its possible new action is endpoint refinement by
\(s_v\). F156 exposes that same endpoint as \(w_S\), and also exposes
\(z_S\), without retaining \(P_v\).

For the zero vector, the empty product is

\[
e_0=(0,1),\qquad s_0=1,\qquad P_0=1.
\]

Its two screens are \(\gcd(0,N)=N\) and \(\gcd(2,N)=1\) after the even-input
branch has been removed. Endpoint \(1\) cannot split a named integer, and
exact value \(1\) is the zero relation. Omitting the empty subset loses no
direct-screen, refinement, or decoder action. Hence, when \(r\le D\), the
nonempty scan captures every F154 refinement opportunity, including the
fact that the identity opportunity is inert.

When \(r>D\), F156 scans only vectors whose coordinates in this particular
deterministically chosen basis have Hamming weight at most \(D\). It does not
claim full-section coverage in that case.

## 9. Exact logical boundary

The construction proves a finite, deterministic, uniformly specified
candidate source. It can finish in one of four states:

1. a direct screen gives a proper factor;
2. endpoint feedback strictly refines the named state, after which another
   bounded stage runs;
3. the final union decoder gives a non-global normalized root and hence a
   proper factor;
4. the named state stops refining and the final decoder has only global
   roots.

The first three states can support factoring. Nothing in the statement
excludes the fourth. In particular, the cost and termination proofs do not
imply a density theorem, a rank defect, a section disagreement, or a
termination-to-factor theorem. The final success gate is therefore an exact
description of what remains to be proved, not a hidden consequence of the
source construction.

## Audit summary

| Claim | Blind result |
|---|---|
| Decorated lifts and section products | Pass under the reconstructed standard carry law |
| Actual section from retained basis lifts | Pass; literal coverage of all original lifts may require quotienting global sign |
| Direct-screen identity | Pass exactly |
| Exact-value deletion and occurrence retention | Pass; cross-ledger physical deduplication is underspecified but immaterial if tags survive |
| Ordinary scan, section scan, joint refinement | Pass |
| Descendant termination | Pass under the imported fixed-product invariant |
| `2^{O((log n)^6)}` deterministic cost | Pass under the stated P118 bounds and polynomial primitive costs |
| Dense-provenance enlargement | Pass as a syntactic claim only |
| Full F154 refinement inclusion for `r <= D` | Pass; identity is inert |
| Universal factoring success | Not proved and not claimed |
