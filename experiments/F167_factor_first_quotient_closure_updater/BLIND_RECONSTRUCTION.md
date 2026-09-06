# F167 blind reconstruction

## Isolation record

I verified before reading the statement that

```text
SHA-256(STATEMENT.md) = e96e12303520b40c459b92ab192de48f7ffc4829daa20c60686007aba8884aad.
```

I then worked from that statement, the project protocol, and only the promoted
interfaces needed from P87, P148, P150, and P151. I did not read the F167 proof,
self-audit, manifest, hostile audit, or any other F167 work product. I did not
run a mathematical computation.

## Verdict

**PASS, with one harmless redundancy noted below.** All theorem-level claims
in the frozen statement reconstruct from the stated hypotheses. The
prime-power cases do not require an unstated assumption
that an order or quotient order is coprime to (N). More precisely:

- the certified initial state itself forces (gcd(M,N)=1);
- if a later relative order (e) has (gcd(e,N)>1), that gcd is already a
  proper factor;
- the same is true of the closed-table order (kappa);
- on the no-factor branches, the order-lift construction is therefore valid
  and gives the stated exact common order.

The optional hidden-log alignments have quasipolynomial cost only under the
statement's separate numerical bound on the relevant known prime factors. A
short factorization encoding by itself would not give that bound. The minimal
order-only updater does not need this optional alignment.

The result is a conditional decoder and state-transition theorem. It is not a
source theorem and does not prove a quasipolynomial factoring algorithm.

## 1. Certified common order over odd prime powers

Write

\[
N=\prod_jR_j,\qquad R_j=p_j^{\alpha_j},
\]

and put (G_j=(\mathbb Z/R_j\mathbb Z)^\times). Because (p_j) is odd,
(G_j) is cyclic. Let (m_j=\operatorname{ord}_{R_j}(g)). From (g^M=1)
we have (m_j\mid M).

If (m_j<M), some prime \(\ell\mid M\) has
(v_\ell(m_j)<v_\ell(M)). Then (m_j\mid M/\ell), so
(g^{M/\ell}=1\pmod {R_j}). This makes
(\gcd(g^{M/\ell}-1,N)>1), contrary to the certificate. Hence

\[
\operatorname{ord}_{R_j}(g)=M
\]

for every (j). Thus (H_j=\langle g\rangle) is the unique subgroup of
(G_j) of order (M).

There is a useful stronger consequence in the prime-power setting. Suppose
(p_j\mid M). Since (g) has order (M) modulo (R_j), the element
(g^{M/p_j}) has order (p_j) modulo (R_j). Its reduction modulo (p_j)
lies in the group of order (p_j-1), so that reduction must be (1). Hence

\[
p_j\mid g^{M/p_j}-1,
\]

contradicting the certificate for the prime divisor (p_j\mid M). Therefore

\[
\boxed{\gcd(M,N)=1.}
\]

This also explains why the certificate uses gcd equal to one, rather than
only nonidentity modulo each full prime power. It detects a partial
(p_j)-adic return.

Finally, (M\mid |G_j|=\varphi(R_j)<R_j\) for each (j), so (M<N). This
supports the later bound on the number of strict state updates.

The formal input list consists of units. At a system boundary, a candidate
with (1<\gcd(d,N)<N) gives a factor and does not enter the list. A candidate
congruent to zero modulo all of (N) must simply be rejected; the theorem
itself starts after unit certification and does not use such a value.

## 2. The absolute-order screen

Let (r_j=\operatorname{ord}_{R_j}(d)) and
(\Lambda_B=\operatorname{lcm}(1,\ldots,B)). For each (j),

\[
R_j\mid d^{\Lambda_B}-1
\quad\Longleftrightarrow\quad
r_j\mid\Lambda_B.
\]

The gcd can also contain a proper power of (p_j) without containing all of
(R_j). That causes no problem: any such value is already a nontrivial
proper divisor of (N).

Thus (A_d=\gcd(d^{\Lambda_B}-1,N)) has the stated trichotomy.

### 2.1 The (A_d=1) branch

If (A_d=1), no (r_j) divides (\Lambda_B). The exponent of a prime
(\ell\) in (\Lambda_B) is the largest (a) with (\ell^a\le B).
Consequently, an integer (r) divides (\Lambda_B) exactly when every full
prime-power divisor of (r) is at most (B). Therefore

\[
\boxed{\sigma(r_j)>B\quad\text{for every }j.}
\]

In fact, (A_d=1) also rules out a return even modulo each (p_j), which is
stronger than merely ruling it out modulo (R_j).

### 2.2 The (A_d=N) branch and stripping

Now every (r_j\mid\Lambda_B). Start with (q=\Lambda_B). For every prime
factor \(\ell\) of (q), repeatedly evaluate

\[
\gcd(d^{q/\ell}-1,N).
\]

- If the gcd is (N), replace (q) by (q/\ell).
- If it is proper, return that factor.
- If it is (1), retain the \(\ell\)-factor in (q).

After all prime powers have been processed, (q) is the exact global order
of (d). Call it (m). If a local order had a smaller valuation at some
prime \(\ell\) than another local order, the last attempted removal at that
valuation would return on some components and not on others. The gcd would
be proper. Hence, on the no-factor branch,

\[
\boxed{\operatorname{ord}_{R_j}(d)=m\quad\text{for every }j.}
\]

Prime powers add one more possible factor event. If (p_j\mid m), then
(d^{m/p_j}) has order (p_j) modulo (R_j), but reduces to (1) modulo
(p_j). The corresponding gcd is nontrivial. It cannot be (N), because
(d^{m/p_j}\ne1\pmod {R_j}) for every component of exact order (m).
Thus no-factor stripping also proves

\[
\boxed{\gcd(m,N)=1.}
\]

This is the prime-power detail that prevents a partial return from being
mistaken for a certified order.

### 2.3 Relative order and the order-only lift

In a cyclic group, subgroups of orders (m) and (M) intersect in a subgroup
of order (\gcd(m,M)). Therefore

\[
\operatorname{ord}_{G_j/H_j}(dH_j)
=\frac{m}{\gcd(m,M)}
=\frac{\operatorname{lcm}(M,m)}{M}.
\]

With (L=\operatorname{lcm}(M,m)) and (e=L/M), this gives exact common
relative order (e) in every component. It does not require
(\gcd(M,m)=1).

Also (e\mid |G_j/H_j|\) for every (j). For a hidden prime
(p_j^{\alpha_j}\parallel N),

\[
v_{p_j}(e)\le v_{p_j}(|G_j/H_j|)\le \alpha_j-1.
\]

Hence (N\nmid e). If (\gcd(e,N)>1), it is automatically a proper factor.
On the remaining branch (e) is coprime to (N), although the group formula
above did not need that coprimality.

The public primary-component lift can now be reconstructed. The exact orders
of (g) and (d) are the common integers (M) and (m). For each prime
(\ell\mid L), extract the \(\ell\)-primary component of whichever one of
(g,d) has the larger \(\ell\)-adic order. Multiply the selected components.
The selected factors have pairwise coprime orders, so their product has order

\[
\prod_{\ell\mid L}\ell^{\max(v_\ell(M),v_\ell(m))}=L
\]

in every (G_j). Prime-divisor screens either expose a partial return as a
proper gcd or certify the resulting public word as an exact common-order
element. This proves the factor-or-state claim with order (L=Me), without
hidden logarithms.

### 2.4 Optional alignment and the punctured bank

Since (dH_j) has order (e), the element (d^e) lies in (H_j) for every
(j). Write its local logarithms as (d^e=g^{a_j}). A digit-wise,
factor-first Pohlig--Hellman comparison works prime power by prime power in
the known factorization of (M). If local digits disagree, the comparison
matches only a proper subset of the hidden components, or only a proper
(p_j)-adic part, and its gcd factors (N). If no such gcd appears, every
digit agrees and one obtains

\[
d^e=g^a\pmod N.

\]

For (e=1), this is exact global membership. For (e>1), it supplies the
extra relation needed for global presentation compression. It is not needed
for the order-only state lift.

The punctured P87 bank adds no terminal outcome here. If (A_d=1), then for
every divisor (E\mid\Lambda_B), a return modulo any (p_j) at exponent
(E) would force a return at exponent (\Lambda_B), contrary to
(A_d=1). If (A_d) is proper, the factor is already known. If (A_d=N),
stripping either factors or produces a common order (m) coprime to (N).
In the latter case reduction modulo (p_j) preserves the order (m), since
the reduction kernel is a (p_j)-group. Hence for every divisor
(E\mid\Lambda_B), the gcd is (N) when (m\mid E) and is (1) otherwise.
No remaining punctured exponent can add a factor. This simplifies the new
decoder and does not contradict P87 in its original setting.

## 3. The relative scan and the double-hard certificate

For a released unit (d), put

\[
q_j=\operatorname{ord}_{G_j/H_j}(dH_j).
\]

Because the kernel of the (M)-th power map on (G_j) is (H_j),

\[
R_j\mid d^{eM}-1
\quad\Longleftrightarrow\quad
q_j\mid e.
\]

Now scan (e=1,\ldots,B) in order.

- A proper (D_e=\gcd(d^{eM}-1,N)) is a factor.
- Suppose the first non-one value is (N). Then every (q_j\mid e). If
  some (q_j<e), the earlier test at (q_j) would have returned on at least
  that component, producing either a proper gcd or an earlier global return.
  Thus every (q_j=e).
- If all (D_e=1), no (q_j\le B), so every (q_j>B).

The common-return branch feeds the same order-only lift. Again, if
(\gcd(e,N)>1), that gcd is a proper factor; otherwise the lift can certify
order (Me). Optional alignment can instead produce a factor or the stronger
global relation.

This relative scan is needed only after (A_d=1). Combining its all-one
branch with the absolute conclusion gives exactly

\[
\boxed{
\sigma(\operatorname{ord}_{R_j}(d))>B
\quad\text{and}\quad
\operatorname{ord}_{G_j/H_j}(dH_j)>B
}

for every (j). This is a valid public certificate about the hidden
components. It is not a factor, and it says nothing about independence among
different retained blocks.

## 4. Complete quotient-fingerprint closure

Let

\[
K_j=\langle H_j,d_1,\ldots,d_t\rangle,
\qquad Q_j=K_j/H_j,
\]

and let

\[
F=\langle d_1^M,\ldots,d_t^M\rangle
\le(\mathbb Z/N\mathbb Z)^\times.
\]

### 4.1 Why difference gcds give simultaneous injectivity

Whenever two globally distinct stored fingerprints (y,z) are compared,
(\gcd(y-z,N)) cannot be (N). If it is not proper, it must be (1).
Therefore (y-z) is nonzero modulo every (p_j), and hence (y\ne z)
modulo every (R_j). Thus, on the no-factor branch, every projection is
injective on the stored set.

The instruction to compare a candidate with every stored value is safe even
when it is an exact global duplicate of one of them. It is also redundant once
the pairwise invariant has already been maintained: if (y=zpmod N), then
(\gcd(y-w,N)=\gcd(z-w,N)) for every other stored (w), and the latter gcd
was tested when the later of (z,w) was stored. Thus an exact duplicate cannot
newly expose a partial equality against another stored value on a live
no-factor run. Continuing the comparisons is harmless and stays within the
claimed cost, but the statement's sentence offered for why they must continue
is stronger than necessary. After all comparisons, an exact duplicate is
deleted and is not enqueued.

The breadth-first search needs only the listed generators, not separately
listed inverses. In a finite group, the monoid generated by a set equals the
subgroup it generates: a positive power of each generator is its inverse.
Each stored node has each outgoing generator edge processed once. Thus queue
closure means that the stored table is all of (F).

### 4.2 The closed branch

Suppose the queue closes with (|F|=\kappa\le C) and no factor. Projection
(F\to F_j) is surjective by the definition

\[
F_j=\langle d_1^M,\ldots,d_t^M\rangle\pmod {R_j},

\]

and the pairwise gcd argument makes it injective. Hence it is an isomorphism.

It remains to identify (F_j) with (Q_j). In the cyclic group (G_j), the
kernel of (x\mapsto x^M) has size
(\gcd(M,|G_j|)=M). It is the unique subgroup of order (M), namely
(H_j). Restricting the map to (K_j) therefore induces an injective map

\[
Q_j\longrightarrow F_j,qquad xH_j\longmapsto x^M,

\]

and it is surjective by the definition of (F_j). Thus

\[
\boxed{|Q_j|=|F_j|=\kappa\quad\text{for every }j.}

\]

Each (F_j) is a subgroup of the cyclic group (G_j), so it is cyclic.
The isomorphisms show that every (Q_j) and the global group (F) are also
cyclic. This proves the claimed closure and cyclicity, not merely a lower
bound.

## 5. Public generator provenance and the F166 lift

Factor (\kappa\) by deterministic trial division. Since (\kappa\le C),
the number of divisions is quasipolynomial when the numerical cap (C) is
quasipolynomial. The complete closed table permits direct enumeration of
powers. Testing the prime divisors of (\kappa) therefore finds a table
element (y) of exact order (\kappa).

Provenance follows inductively from the BFS. Store (a_1=1) at the root. If
an edge multiplies (y=a_y^M) by (d_i^M), store the word
(a_yd_i) for the new fingerprint. Thus the chosen generator has a public
word (a) with

\[
y=a^M.

\]

Under the local isomorphism (Q_j\to F_j), the image of (aH_j) is (y).
Since projection preserves the order of the global generator (y),

\[
\operatorname{ord}_{Q_j}(aH_j)=\kappa

\]

for every (j).

The gcd issue for (\kappa) is exact. Since
(\kappa=|Q_j|\mid |G_j/H_j|), for every
(p_j^{\alpha_j}\parallel N),

\[
v_{p_j}(\kappa)\le\alpha_j-1.
\]

Therefore (N\nmid\kappa). If (gcd(\kappa,N)>1), it is a proper factor.
No algorithm is entitled to cancel (\kappa) modulo (N) before making this
check. No such cancellation is needed here.

On the no-factor branch, apply the order-only lift as follows. The bound
(M\kappa) kills (a) in every local group. Use its known factorization to
strip the exact order of (a). Any disagreement or partial (p_j)-adic
return factors (N); otherwise (a) has one exact common order (m).
Local cyclicity and the quotient order give

\[
\operatorname{lcm}(M,m)=M\kappa.

\]

The primary-component construction from Section 2.3 then gives a public word
of exact common order (M\kappa), or a certification gcd factors (N).

If (\kappa>1), this is strict state growth. If (\kappa=1), then (F) is
trivial, so every (d_i^M=1\pmod N). The local kernel result proves
(d_i\in H_j) for every (i,j). It does not prove that the local logarithms
of a fixed (d_i) agree across (j). Thus (\kappa=1) is exactly the stated
synchronized inert branch, not global aligned membership.

## 6. Optional complete relation recovery

Since (aH_j) has order (\kappa), align (a^\kappa) against (g).
A failed alignment gives a proper gcd. A successful one gives a single
global relation

\[
a^\kappa=g^b\pmod N.

\]

Because (y=a^M) generates the closed cyclic table, for each (i) one can
find (c_i\pmod\kappa) such that

\[
d_i^M=(a^M)^{c_i}.

\]

Then (w_i=d_i a^{-c_i}) satisfies (w_i^M=1), so (w_i\in H_j) locally.
Aligning each (w_i) against (g) either factors (N) or gives

\[
d_i=g^{b_i}a^{c_i}\pmod N.

\]

If all alignments succeed, every named generator lies in
(\langle g,a\rangle). Conversely (g,a) are named generators, so this is
the complete named subgroup. The relations (g^M=1) and
(a^\kappa=g^b) give a public presentation of order at most (M\kappa),
while projection to any (R_j) has order exactly (M\kappa). Hence the
global subgroup has exactly that order. Its local image is cyclic of that
same order, so the presentation and the global subgroup are cyclic. Global
compression is therefore justified only after the alignment.

These alignments are optional for state growth. Their usual digit scan costs
(\sum_{\ell^c\parallel M}c\ell). The statement correctly conditions their
quasipolynomial cost on the relevant prime factors (\ell) being
quasipolynomial in numerical size. Merely writing a very large prime factor
of (M) in (O(n)) bits would not make a linear-in-(\ell) digit scan
quasipolynomial.

## 7. The capacity branch

Suppose (C+1) globally distinct fingerprints are stored without a proper
difference gcd. Every pair then differs modulo every (R_j), by the same
argument as in Section 4.1. Their projections give (C+1) distinct elements
of (F_j). The quotient-power map is always an isomorphism
(Q_j\simeq F_j), independent of whether the BFS has closed. Therefore

\[
|Q_j|\ge C+1

\]

and, because (H_j\le K_j) has order (M),

\[
\boxed{|K_j|=M|Q_j|\ge M(C+1)}

\]

for every (j). This proves a common local-capacity lower bound. It does not
prove that the quotient is noncyclic—it is always cyclic locally—or that
different blocks give independent directions.

## 8. State resets and the two ledgers

The fingerprint map uses the current exponent (M), and its local kernel is
the current subgroup (H_j). A strict update replaces these by a larger
order and a larger unique local subgroup. An old fingerprint equality or
capacity lower bound can therefore collapse in the new quotient. Old
fingerprint tables, queues, and capacities must be discarded and recomputed.

An exact integer or modular relation remains true after the state changes.
The occurrence history that produced a generator also remains true. Those
relations and provenance must be retained. Freezing the block list during a
single BFS makes its graph and cap well-defined; newly exposed blocks can be
added after that search ends.

Exact relation-value deduplication and endpoint-presentation retention serve
different purposes. The same exact product can arise from two different
endpoint factorizations. Removing the second occurrence preserves the parity
column but can remove an endpoint whose gcd with another endpoint exposes a
new common block. Thus one ledger can deduplicate root-aware parity data,
while a second ledger must retain every endpoint occurrence and its full
provenance.

A persistent gcd-free basis is compatible with this rule. When a new
endpoint splits an existing block, record the decomposition and retain the
old generator as historical provenance. The terminal unit blocks become the
current updater inputs. This does not assert that the source must expose a
useful block; it only prevents the bookkeeping from deleting one that was
actually exposed.

A bound on (C) controls the number of stored fingerprints but does not
control the source transcript. Generator occurrences, predecessor words,
integer relations, decomposition histories, and coefficient bit lengths can
grow independently. The full encoded transcript bound is therefore
necessary for the cost theorem.

## 9. Quasipolynomial bit complexity

The following counts reconstruct the stated bound.

1. (\Lambda_B) has (O(B\log B)) bits by an elementary upper bound. Its
   factorization and modular powers are computable in quasipolynomial time
   when the numerical value (B) is quasipolynomial in (n).
2. Divisor stripping uses at most the total number of prime factors in the
   supplied factorizations, with multiplicity. It uses modular exponentiation
   and gcds on explicitly bounded integers. It does not enumerate all
   residues modulo a prime factor.
3. The relative scan uses (B) modular powers and gcds.
4. With at most (C+1) stored nodes, the BFS processes (O(tC)) generator
   edges. Each candidate is compared with at most (C+1) stored values, for
   (O(tC^2)) gcd comparisons.
5. A predecessor path has length at most the number of stored nodes, hence at
   most (C). The provenance encoding stays quasipolynomial under the full
   transcript hypothesis.
6. Factoring (\kappa\le C) by trial division and enumerating its cyclic
   table are quasipolynomial under a quasipolynomial numerical cap.
7. Optional alignments have the separate numerical prime-factor condition
   described in Section 6 above.

Every strict update replaces (M) by (Me) with (e\ge2). The new common
order still divides every (\varphi(R_j)), so it remains below (N). After
(u) strict updates it has grown by at least (2^u), and hence there are
fewer than (n) such updates. Multiplying a quasipolynomial rescan cost by
(n) remains quasipolynomial.

For a fixed-depth canonical section source, the corollary assumes that the
complete explicit transcript at those levels is quasipolynomial. Persistent
gcd-free refinement, freezing, screening, reset-and-rescan, and capped BFS
then perform only quasipolynomially many operations on quasipolynomial-size
integers. The base must be saturated before a later block is called
feedback-only, and an (N)-only replay must verify the provenance chain.
These are classification and cost conditions. They are not an existence law
for a useful feedback event.

## 10. Exact nonclaims and remaining obstruction

The reconstruction supports the statement's limitations exactly.

- No rule here constructs a released unit block with a useful order.
- A double-hard block is not a factor and need not add a new quotient
  direction.
- A closed table with (\kappa=1) proves only synchronized local membership,
  unless the optional alignments also succeed.
- A capacity certificate is not a factor and does not prove independence of
  the released blocks.
- The minimal F166 lift preserves the next common-order state. Without full
  alignment, it need not preserve or compress the complete globally named
  subgroup.
- The two-ledger rule preserves information; it does not force useful
  information to appear.
- Fixed-depth closure proves conditional running time, not that a useful
  branch occurs.
- The punctured-bank simplification does not refute P87.
- Large powered local components can motivate the capacity obstruction, but
  no example family outside the hypotheses can establish an all-input law
  inside this common-order quotient model.
- No argument rules out a synchronized cyclic quotient whose order exceeds
  (C) while all tested equalities remain global.

Therefore the exact missing result is still a source law: on every surviving
input, a public quasipolynomial canonical source would have to force a factor,
a bounded absolute or relative closure, closure of the full fingerprint
subgroup below the cap, or a contradiction from repeated capacity
certificates. F167 proves the decoder under those events and proves none of
those events must occur. It is not an all-input factoring algorithm.
