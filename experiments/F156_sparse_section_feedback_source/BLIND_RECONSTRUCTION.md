# F156 statement-only blind reconstruction

## Scope and verdict

I verified the supplied statement before reading it.

```text
d426df6c293fd835c85260b14fb6ddd57a99ff812a4c7b9a74b084318ed34527  STATEMENT.md
```

I read no other F156 file and used no prior F156 argument.

**Verdict: qualified pass.** The decorated-lift algebra, the dense-provenance
claim, the one-layer source semantics, stage termination, and the
\(2^{O((\log n)^6)}\) bound reconstruct. There is no asymptotic or algebraic
counterexample in the declared scope. Two qualifications are needed.

1. The operative stage order must be ordinary frozen P118 scan first, section
   construction and section scan second, and one joint refinement last. The
   statement says that both scans finish before refinement, but it does not say
   the first two steps in one unambiguous sentence. Reversing them defines a
   weaker source and invalidates the current-stage F154 inclusion claim.
2. Nonempty subsets enumerate the nonidentity part of the lifted section. They
   do not enumerate its identity. The omitted element has inverse endpoint
   \(1\) and manufactured value \(1\), so it has no refinement or decoder
   effect. Thus the F154 *opportunity* inclusion is correct, but “the entire
   actual lifted section” is literally false unless “section” is being used to
   mean its nonidentity menu.

The reconstruction also uses the inherited meanings of canonical modular
inverse, factor-free refinement, and complete normalized-root decoding. In
particular, “complete decoder” must mean a kernel-basis test. It cannot mean
enumeration of all kernel words.

## 1. The decorated extension and the actual lifts

Let \(V=\mathbf F_2^m\). For \(u,v\in V\), put

\[
c(u,v)=Q(u\mathbin{\&}v)
       =\prod_{j:u_j=v_j=1}q_j.
\]

Pairwise coprimality is not needed for the next identity, but it is needed for
the factor-free representation:

\[
Q(u)Q(v)=c(u,v)^2Q(u\oplus v).
\tag{14}
\]

Since every base value is congruent to \(1\pmod N\), every integer factor of a
base value is a unit modulo \(N\). Hence every \(q_j\) and every \(t_i\) is a
unit modulo \(N\). The standard decorated extension is therefore

\[
E_Q(N)=\{(v,z):z\in(\mathbf Z/N\mathbf Z)^\times,
                    \ z^2=Q(v)\pmod N\},
\]

with product

\[
(u,x)\star(v,y)
=
\bigl(u\oplus v,\;xyc(u,v)^{-1}\bigr).
\tag{15}
\]

Equation (14) proves closure. It also shows that this product uses only modular
values of the blocks. It does not require expansion of a dense exact product.

For a base record,

\[
A_i=t_i^2Q(v_i)\equiv1\pmod N.
\]

Thus

\[
(t_i^{-1})^2\equiv Q(v_i)\pmod N.
\]

So \(g_i=(v_i,t_i^{-1})\) is an actual lift. The inverse is well-defined
because \(t_i\) is a unit. This also explains why retaining only a parity
vector would be insufficient. A parity vector can have several square roots
modulo a composite \(N\). The source record fixes one of them.

Scan the base records in their deterministic occurrence order. Retain a record
when its parity vector increases the binary rank. This gives independent
vectors \(b_1,\ldots,b_r\) and their actual lifts \(e_1,\ldots,e_r\). Every
vector in their span has a unique basis expression. Therefore

\[
\sigma\left(\bigoplus_{i\in S}b_i\right)
=\mathop{\star}_{i\in S}e_i
\tag{16}
\]

is a well-defined lifted section. First occurrence fixes any sign or kernel
choice in each basis lift.

The consistency test has a separate role. A binary dependence among the base
parities multiplies the corresponding decorated records into the fiber above
zero. Its second coordinate is a square root of \(1\pmod N\). A non-global
root gives a proper factor through a gcd with \(x-1\) or \(x+1\). If the test
does not return a factor, all dependence discrepancies are global roots. The
chosen actual basis lifts can then represent the surviving records as one
consistent section, up to the declared global normalization.

## 2. Sparse candidates and the exact gcd identity

For nonempty \(S\) with \(|S|\le D\), write

\[
e_S=(v_S,z_S),\qquad
v_S=\bigoplus_{i\in S}b_i.
\]

Independence of the \(b_i\) implies \(v_S\ne0\). Take \(z_S\) to be its
canonical integer representative and let

\[
w_S=\iota_N(z_S)
\]

be the canonical integer representative of its modular inverse. Then
\(z_Sw_S\equiv1\pmod N\), while decorated membership gives
\(z_S^2\equiv Q(v_S)\pmod N\).

Multiplication by the unit \(z_S\) does not change a gcd with \(N\). Also, a
congruence modulo \(N\) does not change that gcd. Hence, for either sign,

\[
\begin{aligned}
\gcd(z_S\pm w_S,N)
&=\gcd(z_S(z_S\pm w_S),N)\\
&=\gcd(z_S^2\pm z_Sw_S,N)\\
&=\gcd(Q(v_S)\pm1,N).
\end{aligned}
\tag{17}
\]

This proves the boxed identity exactly, not only up to divisibility. The last
gcd can be evaluated using \(z_S^2\bmod N\). The exact integer \(Q(v_S)\)
does not have to be formed.

With least positive representatives,

\[
1\le z_S,w_S<N,
\qquad
F_S=z_Sw_S=1+\kappa_SN<N^2.
\tag{18}
\]

Thus every feedback value is another exact relation with supplied root \(1\).
The direct screen is performed for every occurrence before any exact-value
deletion. A gcd equal to \(1\) or \(N\) is nonproductive; a value strictly
between them is a proper factor.

## 3. Exact-value deletion does not delete endpoint semantics

Two distinct subsets can give the same integer \(F_S\). They can still give
different ordered or unordered endpoint presentations. The source must perform
these actions in this order for each occurrence:

1. run both direct screens;
2. expose that occurrence's \(z_S\) and \(w_S\);
3. record its source provenance;
4. deduplicate only the exact integer \(F_S\) in the feedback relation ledger.

This is what the statement's “before exact-value deletion” clause requires.
It is essential. The product alone does not recover the endpoint gcd data.
For example, two endpoints can meet complementary factors of an old block
while their product meets the whole block. Refining only the product can then
miss both endpoint splits.

Deduplication of the relation value itself is safe here. Every occurrence of
the same \(F_S\) has the same supplied root \(1\), and its exact factor-free
parity row is the same. Repeating that row adds no kernel information. Endpoint
presentations and occurrence provenance are retained separately, so their
named-refinement effects are not lost.

## 4. The required frozen-stage semantics

The coherent stage schedule is:

1. Freeze the current named basis.
2. Run the complete ordinary P118 menu against that basis. Append its exact
   relations to the base ledger. Do not apply an endpoint split yet.
3. Factor-free-refine the now current distinct base ledger. Run the complete
   consistency test. Select the parity basis and actual lifts.
4. Run the complete sparse section menu from that fixed basis. Append only its
   exact values to the feedback ledger. Preserve every endpoint occurrence.
5. Jointly refine all ordinary and feedback endpoints against the named basis
   frozen in step 1.
6. Start another stage only if an old named block split. Otherwise stop and run
   the final decoder on both ledgers.

The ordinary scan must precede section construction. Otherwise the feedback
menu omits base records produced in the same frozen stage. In particular, if
that stage does not split a named block, there is no later stage in which those
records can feed a section. The claimed F154 inclusion for the frozen base span
would then not hold for the span after the ordinary scan.

No split can be applied between the two menus. Such a split would change the
named grammar and make the rest of the menu non-frozen. Early return on a
proper factor is harmless; the complete-menu condition is needed only on paths
that continue to refinement.

Only terminal factors that divide an old named block become future named
generators. A factor found only in a probe endpoint remains decoder data. This
gives the invariant:

\[
\text{every named block at every stage is a descendant of the initial named
product.}
\tag{19}
\]

Feedback exact values never enter step 3 at a later stage. Their endpoints can
split a named block, and that split can change later ordinary base records.
This is indirect adaptive feedback, not recursive section closure. Each stage
still has exactly one section layer over the base ledger.

## 5. Stage termination

Let \(P_0\) be the fixed initial named endpoint product and let its bit length
be \(\Lambda_0\). A strict named split replaces at least one integer block by
two or more proper factors greater than one. In the refinement forest, all
leaves divide the occurrences in \(P_0\). Since a product of \(k\) integers
greater than one is at least \(2^k\), the forest has fewer than
\(\log_2P_0+1\le\Lambda_0+1\) leaves, with multiplicity included. Every strict
stage increases the leaf count. Therefore

\[
T\le O(\Lambda_0)=2^{O(L^2)}.
\tag{20}
\]

Probe-only cofactors cannot invalidate this potential argument because they do
not enter the named forest. If no old block splits, the algorithm stops instead
of repeating an identical frozen stage. This proves finite stage termination.
It does not prove that termination yields a factor.

## 6. Base-source count

Let \(M\) be the maximum number of named blocks in a stage. The descendant
invariant gives \(M=O(\Lambda_0)=2^{O(L^2)}\). A support-\(D\), exponent-\(E\)
word menu has, up to a constant choice for signs and zero exponents,

\[
W\le (D+1)\bigl(M\,O(E)\bigr)^D.
\]

Using \(D=L^2\), \(\log_2E=L^2\), and \(\log_2M=O(L^2)\),

\[
\log_2W
\le O\bigl(D(\log M+\log E)\bigr)
=O(L^4).
\tag{21}
\]

Multiplication by the stage count and the inherited seed-bank size does not
change this exponent. Thus

\[
R_0=2^{O(L^4)}.
\tag{22}
\]

An ordinary word has at most \(D\) selected blocks and exponent magnitude at
most \(E\). Its bit length is at most a polynomial factor times
\(DE\Lambda_0+n=2^{O(L^2)}\). Consequently the total base-ledger bit length is
\(2^{O(L^4)}\), as stated. This step is inherited from the P118 word grammar;
the important F156 point is that feedback records never increase the input to
a later ordinary or section basis ledger.

## 7. Section-source count

The basis is selected from base records, so \(r\le R_0\). For \(r\ge1\),

\[
\sum_{j=1}^{D}\binom rj
\le (D+1)\max\{1,r\}^D.
\tag{23}
\]

For \(r=0\), the left side is zero and the same displayed bound remains true.
Therefore

\[
\log_2\left((D+1)\max\{1,r\}^D\right)
\le O(\log D+D\log R_0)
=O(L^6).
\tag{24}
\]

One stage has \(2^{O(L^6)}\) section candidates. Multiplication by
\(T=2^{O(L^2)}\) gives the same bound across all stages.

The parity-vector width also fits this budget. If the base factor-free
refinement has \(m\) nontrivial coprime blocks, then their product divides a
product of the base exact values. Hence \(m\) is at most the total base input
bit length, namely \(2^{O(L^4)}\). Even a direct implementation that processes
an \(m\)-bit vector and at most \(D\) decorated products per candidate adds
only a \(2^{O(L^4)}\operatorname{poly}(n)\) factor. This is absorbed by
\(2^{O(L^6)}\).

## 8. Total bit complexity

There are \(2^{O(L^6)}\) feedback occurrences over the full run. Each endpoint
has \(O(n)\) bits, and each feedback exact value has fewer than \(2n\) bits.
An occurrence label needs at most
\(O(D\log r)=O(L^6)\) bits. Since \(n=2^{O(L)}\), total feedback storage is

\[
2^{O(L^6)}.
\tag{25}
\]

The base values, bases, and factor-free blocks total only
\(2^{O(L^4)}\) bits. Standard deterministic integer multiplication, modular
arithmetic, gcd, perfect-power extraction, pairwise factor-free refinement,
and binary Gaussian elimination take a fixed polynomial in their total input
size. A fixed polynomial of \(2^{O(L^6)}\) is still
\(2^{O(L^6)}\). Reprocessing a cumulative base ledger at each of
\(2^{O(L^2)}\) stages is also absorbed.

Completeness of the normalized-root decoder does not require enumeration of
every vector in a binary kernel. The normalized-root assignment is a group
homomorphism from that kernel to the square roots of unity modulo global
\(\{\pm1\}\). If every vector of a kernel basis maps to the global subgroup,
then every kernel word does. Conversely, a non-global image forces at least one
basis image to be non-global. Gaussian elimination plus a basis scan is
therefore complete and polynomial in the ledger size.

It follows that enumeration, endpoint batches, factor-free refinement,
storage, all consistency tests, and the final union decoder have deterministic
bit complexity

\[
2^{O(L^6)}=2^{O((\log n)^6)}.
\tag{26}
\]

For literal deterministic output, all “first” choices also need inherited
canonical orderings: record order, factor-free block order, subset order, and
least positive modular representatives. Lexicographic subset order suffices.
These choices do not change the bound or the generated complete menu.

## 9. Why the source is genuinely new but only syntactically new

Named-word support counts current named integer generators. Section-word
support counts retained relation-basis vectors. These are different
coordinates.

A retained parity vector can have many nonzero old-block coordinates. Even if
individual retained vectors happen to be moderately sparse, the xor of up to
\(D\) of them can cross the named support cap. For the extreme shape

\[
b_1=(1,1,\ldots,1),
\]

the section word \(S=\{1\}\) has section support one but dense old-block
provenance. Its \(Q(v_S)\) is a product over every indicated block. Its root
\(z_S\) is nevertheless computed in the decorated group with modular block
values.

Thus the production rule is outside the bounded-support named-word grammar.
This does not imply that its final residue is outside the full set of residues
that P118 can produce. Different syntactic derivations can coincide modulo
\(N\), or even as exact completion values. The statement correctly claims a
grammar enlargement and expressly declines the stronger semantic-separation
claim.

## 10. The \(r\le D\) comparison with F154

If \(r\le D\), every subset of \(\{1,\ldots,r\}\) is within the support cap.
Unique basis coordinates give a bijection

\[
S\longmapsto \bigoplus_{i\in S}b_i
\]

from all subsets to the base span. The scan uses only nonempty subsets, so it
enumerates exactly every nonzero span vector and its chosen actual lift. For
each such lift \((v,z_v)\), it exposes

\[
\iota_N(z_v),
\]

which is the inverse representative used by the corresponding F154 completion
\(P_v=s_v^2Q(v)\), provided F154 uses the same actual first-occurrence section.
F156 does not need to retain \(P_v\) to obtain that endpoint refinement.

The empty subset is absent. It would give

\[
(v,z)=(0,1),\qquad \iota_N(z)=1,
\qquad P_0=1.
\]

Endpoint \(1\) cannot split a nontrivial named block, and value \(1\) adds no
parity or decoder information. Therefore omission of the identity does not
remove any F154 refinement opportunity. It does refute the unqualified literal
phrase “entire actual lifted section.” The exact valid claim is “the entire
nonidentity section menu, with the identity omitted as inert.”

The F154 comparison also depends on matching the chosen actual section. A
parity basis by itself is not enough because changing a lift by a global sign
can change its least positive inverse endpoint. The statement's retention of
the corresponding actual lifts supplies the needed choice. If F154 uses a
different lift convention, equality of the endpoint menus would require a
separate argument.

## 11. What is and is not proved

The construction proves a finite deterministic source and its cost. It can
terminate in any of these states:

- a direct screen returns a proper factor;
- endpoint exposure strictly refines a named block and causes another stage;
- no named block splits, so the final union decoder runs;
- the final decoder has only global normalized roots and returns no factor.

The last state is allowed by the statement. The stage potential proves only
that strict refinement cannot continue forever. It gives no density, rank, or
root-disagreement theorem. Therefore a complete factoring theorem needs an
additional result that excludes the last state on every surviving composite
input, or proves that an earlier refinement chain must lead to a productive
screen or relation. This is exactly the remaining success gate in Section 7.

The source-and-cost result is consequently sound under the ordinary-first
schedule and the inherited P118/P138/F154 primitives. It is not an all-input
factoring result.
