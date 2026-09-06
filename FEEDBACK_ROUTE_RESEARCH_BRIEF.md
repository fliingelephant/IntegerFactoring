# Adaptive Canonical-Inverse Feedback for Classical Integer Factorization

## Self-contained research brief for mathematical and AI review

**Snapshot date:** 2026-08-08  
**Repository checkpoint:** `00c2a80`  
**Status:** exploratory framework with audited partial results; no all-input polynomial-time factoring algorithm is known.

---

## 0. One-paragraph summary

This project studies a classical adaptive relation-generation mechanism for
factoring an odd composite integer \(N\). For a unit \(c\bmod N\), let \(w\)
be its least positive inverse. The exact integer identity

\[
c\,w=1+\kappa N
\]

is called a **canonical-inverse relation**. Many such relations can be
refined, without factoring them into primes, into pairwise-coprime integer
blocks. Binary linear algebra then finds every product that is an exact
integer square. A non-global square root of \(1\bmod N\) factors \(N\).
The proposed feedback step does more than collect another scalar: it selects
blocks from several old relations, forms a modular word, replaces that word
by its canonical integer representative and inverse, refines all new and old
integer endpoints together, and uses the newly exposed blocks to change the
next relation source. The abstract modular subgroup may not grow. The
possible gain is a new **short named integer presentation**. Several exact
fixed examples prove that this representation-level effect is real. Larger
examples also prove that many individually useless relations can form a
useful cross-relation circuit. The missing theorem is a public
polynomial-size candidate rule that forces this useful effect on every hard
input, or with inverse-polynomial probability.

---

## 1. What is old, and what may be new

### 1.1 Classical foundation

The following parts are standard or close to standard:

1. Collect multiplicative relations.
2. Record exponent parity.
3. Use linear algebra over \(\mathbb F_2\).
4. Construct a congruence of squares.
5. Factor with one or two gcd computations.

This is the Dixon/quadratic-sieve pattern. Partial relations and graph cycles
are also classical. Factor refinement and gcd-free or coprime bases are known
algorithmic tools.

Useful references:

- J. D. Dixon, *Asymptotically Fast Factorization of Integers*:
  <https://pages.cs.wisc.edu/~cs812-1/dixon.pdf>
- A. K. Lenstra and M. S. Manasse, *Factoring with Two Large Primes*:
  <https://doi.org/10.1090/S0025-5718-1994-1250773-9>
- D. J. Bernstein, *Factoring into coprimes in essentially linear time*:
  <https://cr.yp.to/coprimes.html>

### 1.2 Working novelty claim

The candidate novelty is the following adaptive closed loop:

\[
\boxed{
\begin{array}{c}
\text{canonical-inverse relations}\\
\downarrow\\
\text{factor-free joint integer refinement}\\
\downarrow\\
\text{cross-relation block selection}\\
\downarrow\\
\text{canonical modular reduction and inversion}\\
\downarrow\\
\text{new canonical integer endpoints}\\
\downarrow\\
\text{new refinement and new named blocks}\\
\downarrow\\
\text{new relation grammar and retained cross-layer decode}.
\end{array}}
\]

The key distinction is:

\[
\boxed{
\text{new modular group element}
\ne
\text{new usable integer presentation}.}
\]

If the current blocks generate a modular subgroup \(H\), then the inverse of
an element of \(H\) is still in \(H\). Nevertheless, its least positive
integer representative can have new gcd overlaps with stored endpoints.
Those overlaps can expose blocks whose residue classes were not available as
named generators.

This seems to be more than a restatement of a static factor base. A suitable
paper-level claim would be:

> A new adaptive, factor-free relation-generation framework based on
> canonical integer presentations and recursive block refinement.

It would be premature to claim a new general factoring algorithm. A targeted
literature search did not find this exact complete loop, but no
publication-level prior-art audit has been completed.

### 1.3 Relation to Shor and Regev

The final algebraic target is related to the target in Shor-type and
Regev-type factoring:

\[
x^2\equiv1\pmod N,
\qquad
x\not\equiv\pm1\pmod N.
\]

Shor obtains periodic information by quantum Fourier sampling. Regev's
factoring algorithm obtains approximate lattice information from quantum
samples and uses classical lattice post-processing:
<https://arxiv.org/abs/2308.06572>.

This project does not simulate either quantum sampler. It asks whether a
fully classical adaptive integer-presentation process can generate enough
factor-correlated relations. The target is similar, but the information
source and the search dynamics are different.

---

## 2. Basic objects and standard terminology

Assume that \(N\ge3\) is odd. Even factors and perfect powers can be handled
before this framework starts.

In this brief, **factor-free** means that the procedure does not prime-factor
the relation values or their endpoints. It may use gcd, exact division,
perfect-power detection, exact square roots, and linear algebra.

The phrase **trial-division-hard** is local shorthand. For an \(n\)-bit test
input, it means that no prime factor is at most the declared polynomial trial
bound, usually \(n^2\). It is not a standard complexity class.

### 2.1 Canonical inverse and carry

For a unit \(1\le c<N\), let

\[
w_N(c)\in\{1,\ldots,N-1\}
\]

be the least positive inverse of \(c\bmod N\). Define

\[
A_N(c)=c\,w_N(c)=1+\kappa_N(c)N.
\]

Here:

- \(c,w_N(c)\) are the **integer endpoints**;
- \(A_N(c)\) is the **exact relation value**;
- \(\kappa_N(c)\) is the **carry** or inverse quotient.

Exact identities include

\[
0\le \kappa_N(c)<\min(c,w_N(c))
\]

and, for \(c\ge2\),

\[
\kappa_N(c)\equiv -N^{-1}\pmod c.
\]

The direct inverse-pair screens are

\[
\gcd(c-w_N(c),N)=\gcd(c^2-1,N),
\]

\[
\gcd(c+w_N(c),N)=\gcd(c^2+1,N).
\]

They test whether \(c\) agrees with \(c^{-1}\), or with \(-c^{-1}\), on
only some CRT components.

### 2.2 Exact-value projection

The two endpoints \(c\) and \(w_N(c)\) give the same exact value. Different
inverse orbits can also give the same exact integer product. Therefore the
square-class decoder keeps only the first occurrence of each exact value
\(A_N(c)>1\).

This **exact-value deduplication** is different from residue deduplication.
Extra endpoint presentations can still matter for future gcd refinement even
when they do not add a decoder column.

### 2.3 Factor-free block refinement

Given positive integers \(a_1,\ldots,a_m\), repeated gcd and exact division
can produce pairwise-coprime blocks \(q_1,\ldots,q_s\) and exponents
\(e_{ji}\) such that

\[
a_i=\prod_{j=1}^s q_j^{e_{ji}}.
\]

The \(q_j\) need not be prime. No integer factorization oracle is used.

The parity matrix is

\[
M=(e_{ji}\bmod2)\in\mathbb F_2^{s\times m},
\]

after rows for exact-square blocks are removed. Then

\[
Mx=0
\quad\Longleftrightarrow\quad
\prod_{i:x_i=1}a_i
\text{ is an exact integer square}.
\]

This decoder is complete for every explicit finite list.

### 2.4 Square closure versus factor correlation

For \(x\in\ker M\), write

\[
\prod_{i:x_i=1}A_i=R(x)^2,
\qquad R(x)>0.
\]

Because every \(A_i\equiv1\pmod N\),

\[
R(x)^2\equiv1\pmod N.
\]

The relation factors \(N\) only if

\[
R(x)\not\equiv\pm1\pmod N.
\]

The useful invariant is the normalized root map

\[
\bar\rho:
\ker M\longrightarrow
\mu_2(\mathbb Z/N\mathbb Z)/\{\pm1\}.
\]

Thus:

\[
\boxed{
\text{square correlation}
\ne
\text{factor correlation}.}
\]

A large kernel can map entirely to the global roots \(+1\) and \(-1\).

### 2.5 Two different relation spaces

Do not identify these objects:

1. The exact integer-square space

   \[
   \ker M,
   \]

   which records products that are squares in \(\mathbb Z\).

2. The modular exponent lattice

   \[
   \Lambda=
   \left\{
   v\in\mathbb Z^s:
   \prod_jq_j^{v_j}\equiv1\pmod N
   \right\}.
   \]

For modular 2-torsion, define

\[
\Lambda^{(2)}=\{v:2v\in\Lambda\},
\]

\[
\Lambda_{\pm}
=
\left\{
v:
\prod_jq_j^{v_j}\equiv\pm1\pmod N
\right\}.
\]

The useful modular target is

\[
v\in\Lambda^{(2)}\setminus\Lambda_{\pm},
\]

subject to the integer block capacities or word rules that the algorithm can
actually realize.

---

## 3. The complete factor-free decoder is already available

For any explicit polynomial-size list of congruences

\[
x_i^2\equiv a_i\pmod N,
\]

gcd-free refinement and binary linear algebra compute the exact square
kernel without factoring the \(a_i\). Exact square roots of selected products
can also be computed. The normalized root map is a homomorphism. Therefore:

> If any dependency in the explicit list has a non-global root, then every
> complete binary kernel basis contains at least one useful basis vector.

Only a basis must be screened. There is no need to enumerate every kernel
vector.

This closes the decoder problem for an explicit finite list. The main problem
is now the **source**:

> How can bare \(N\) generate a polynomial-size relation list whose normalized
> root image is nonzero?

The formal theorem is recorded as P66 in
[`PROVED.md`](./PROVED.md).

---

## 4. The starting source: completion-biased canonical inverses

For uniform \(U\in(\mathbb Z/N\mathbb Z)^\times\), define

\[
D_N(U)=\frac{U\,w_N(U)-1}{N}.
\]

For \(1\le k<N\), let

\[
f_N(k)
=
\#\{u:k<u<N,\ u\mid Nk+1\}.
\]

Then the output law is exactly

\[
\Pr(D_N(U)=k)=\frac{f_N(k)}{\varphi(N)}.
\]

Thus bare \(N\) manufactures a real nonuniform distribution. It is weighted
by the number of admissible factor-pair completions of \(Nk+1\).

This was a useful conceptual start because it is a metric or multiplicity
bias obtained without leaked bits. However, no theorem connects this bias to
the factors of \(N\).

On balanced semiprimes, polynomially many independent samples almost never
have equal or polynomially close quotient values. Independent relation
sampling is therefore too dispersed for the easiest collision decoders.

Deterministic offset sources did create exact square dependencies in some
tests, but the dependencies had only global roots. A later symbolic audit
showed that the observed dependencies were generic algebraic squares rather
than factor-correlated arithmetic events.

This gave the key lesson:

\[
\boxed{
\text{a source can manufacture relations}
\quad\text{without manufacturing factor information}.}
\]

It motivated dependent trajectories, retained cross-relation states, and
feedback.

---

## 5. Three logically different success channels

A feedback candidate can succeed in at least three different ways.

### 5.1 Direct inverse-pair separator

For a candidate \(g\) and its canonical inverse \(w\),

\[
1<\gcd(g-w,N)<N
\]

or

\[
1<\gcd(g+w,N)<N.
\]

This detects partial CRT agreement before any square-class dependency is
formed.

### 5.2 Direct non-global involution

If \(g=w\), then

\[
g^2\equiv1\pmod N.
\]

If \(g\not\equiv\pm1\pmod N\), the two sign gcds factor \(N\).

### 5.3 Factor-correlated exact-square closure

The new exact value can close in the old parity span. If the induced exact
root has nonzero image under \(\bar\rho\), the complete decoder factors \(N\).

These events must not be merged:

- a new relation value need not close;
- a closure need not have a useful root;
- a direct separator can succeed even when the new relation adds a private
  row and no dependency.

---

## 6. Exact incremental accounting

Suppose the old parity matrix is \(M\), and a new exact relation has column
\(b\).

### 6.1 Closure gate

The kernel dimension increases by one exactly when

\[
b\in\operatorname{colspan}(M).
\]

If \(b\) has a new private odd row, it cannot close on that step.

### 6.2 Root gate

If \(Mc=b\), the new kernel vector is \((c,1)\). The new induced root is

\[
s_c=
\sqrt{A_{\rm new}\prod_iA_i^{c_i}}
\pmod N.
\]

After the old complete kernel basis has been screened, the new closure is
useful exactly when

\[
s_c\not\equiv\pm1\pmod N.
\]

Thus feedback has two independent gates:

\[
\boxed{
\text{parity closure}
\quad+\quad
\text{non-global root label}.}
\]

### 6.3 Retention matters

Deleting every relation that does not close immediately is unsafe. The first
column \([1]\) is nonclosing. A later second column \([1]\) creates the
dependency \((1,1)\). The same phenomenon occurs in audited integer
certificates below.

An unsuccessful relation can be the first half of a later circuit.

---

## 7. Exact small certificates for cross-relation feedback

### 7.1 Cross-relation selection at \(N=21\)

Start with

\[
22=2\cdot11=1+N,
\]

\[
85=5\cdot17=1+4N.
\]

Select one block from each relation:

\[
g=2\cdot5=10.
\]

Its canonical inverse is \(w=19\), and

\[
10\cdot19=190=1+9N.
\]

The new endpoint \(19\) is not in the old block set. The new exact relation
does not create a square dependency, but the direct screen already gives

\[
\gcd(10-19,21)=3.
\]

This proves that direct factor extraction and square closure are different
channels.

### 7.2 Cross-relation self-inverse state at \(N=55\)

Use

\[
56=2\cdot28=1+N,
\]

\[
111=3\cdot37=1+2N.
\]

A legal cross-relation product is

\[
g=3\cdot7=21.
\]

Then

\[
21^2=441=1+8N,
\]

\[
\gcd(21-1,55)=5,
\qquad
\gcd(21+1,55)=11.
\]

The two old square classes are independent. The useful self-inverse state is
not a power of one repeated relation.

### 7.3 Infinite repeated-block family

For odd \(t\ge3\), let

\[
g=2^t,
\qquad
N=\frac{g^2-1}{3}
=(g-1)\frac{g+1}{3}.
\]

Authorize \(t\) copies of the quotient-one relation \(N+1\). The old decoded
roots are global, while

\[
g^2=1+3N
\]

and

\[
\gcd(g-1,N)=g-1,
\qquad
\gcd(g+1,N)=\frac{g+1}{3}.
\]

Here \(t=\Theta(\log N)\). A polynomial number of tiny seed relations can
authorize a useful product near \(\sqrt N\). This is an exact warning that
small seed quotients do not bound the size of useful cross-relation words.

The missing step is to select such a word without enumerating exponentially
many block subsets.

---

## 8. Representation-level feedback certificates

### 8.1 First strict subgroup expansion: \(N=209\)

Let

\[
N=209=11\cdot19.
\]

Start from

\[
31\cdot27=1+4N,
\qquad
3\cdot70=1+N.
\]

The old blocks generate

\[
H_0=\langle3\rangle.
\]

The selected canonical pair is

\[
80\cdot81=1+31N.
\]

Both residues are already in \(H_0\). Joint integer refinement gives the
blocks

\[
\{2,3,5,7,31\}.
\]

The next bounded support-two menu contains

\[
2\cdot5=10,
\]

and

\[
\gcd(10+1,209)=11.
\]

The block \(10\) is outside the old block-generated subgroup, even though
the feedback residue itself was not. This is the first exact
representation-level effect.

This witness is not strong enough to prove feedback necessity. The old
subgroup contains another separator through a larger power.

### 8.2 Stronger restricted-state chain: \(N=4033\)

Let

\[
N=4033=37\cdot109=\Phi_{36}(2).
\]

The element \(2\) has order \(36\) modulo both factors. Thus

\[
H_0=\langle2\rangle
\]

has synchronized \(+1\) and \(-1\) states and no direct sign separator.

Use the endpoint history

\[
2\cdot2017=1+N,
\]

\[
64\cdot3970=1+63N,
\]

\[
8\cdot3529=1+7N.
\]

Complete refinement gives

\[
Q_0=\{2,2017,1985,3529\},
\qquad
H(Q_0)=H_0.
\]

The legal repeated-block product

\[
g=2^{11}=2048
\]

has canonical inverse

\[
w=3905,
\qquad
2048\cdot3905=1+1983N.
\]

All immediate screens fail. The important overlap is

\[
\gcd(1985,3905)=5.
\]

Hence

\[
1985=5\cdot397,
\qquad
3905=5\cdot781.
\]

The refined blocks are

\[
Q_1=\{2,2017,5,397,3529,781\}.
\]

The new block \(5\) is not in \(H_0\). Therefore

\[
H(Q_1)=\langle2,5\rangle\supsetneq H_0.
\]

The enlarged subgroup contains a separator:

\[
5\cdot2^{-23}\equiv630\pmod{4033},
\]

\[
\gcd(630-1,4033)=37.
\]

Canonical-residue closure makes the oversized modular word executable:

\[
630\cdot3220=1+503N,
\]

\[
\gcd(630-3220,N)=37.
\]

A smaller literal support-two certificate is

\[
5^2\,2^8\equiv2367\pmod N,
\]

\[
2367\cdot443=1+260N,
\]

\[
\gcd(2367-443,N)=37.
\]

A separate power-bank completion uses

\[
M=\operatorname{lcm}(1,\ldots,9)=2520,
\]

\[
\gcd(5^{2520}-1,4033)=37.
\]

This fixed chain is important:

1. The old subgroup is separator-free.
2. The feedback residue is already in the old subgroup.
3. Integer refinement exposes a named block outside the old subgroup.
4. A later canonical word or power of that block factors \(N\).

However, stronger static preprocessing also factors \(4033\). Section 12
explains the correction.

### 8.3 Phase-only expansion: \(N=2047\)

Let

\[
N=2047=23\cdot89.
\]

Use

\[
11\cdot1861=1+10N,
\qquad
312\cdot269=1+41N.
\]

The old endpoint residues generate \(H_0=\langle11\rangle\). The element
\(11\) has order \(22\) in both hidden fields, so pure old powers do not
separate the factors.

Canonical-residue feedback gives

\[
g=[11^7]_N=1778,
\qquad
w=1735,
\]

\[
1778\cdot1735=1+1507N.
\]

The feedback residue adds no new modular information. Yet

\[
\gcd(312,1778)=2.
\]

The block \(2\) is outside \(H_0\), so the block-generated subgroup expands.
But \(2\) has order \(11\) in both hidden fields. Every pure power of \(2\)
still fails.

The mixed word succeeds:

\[
2\cdot11=22,
\qquad
\gcd(22+1,2047)=23.
\]

This proves a distinct **phase branch**. A new block can be useful only in a
mixed word, even when its local orders are equal.

Again, the block \(2\) is visible by ordinary trial division of \(312\).
This is a mechanism witness, not a necessity witness.

---

## 9. Retained relations and amortized cross-layer closure

This is the strongest departure from “compute one scalar and take one gcd.”

### 9.1 Two retained relations at \(N=2773\)

Let

\[
N=2773=47\cdot59.
\]

Two canonical-inverse values are

\[
P_1=3\cdot1849=1+2N=3\cdot43^2,
\]

\[
P_2=842\cdot2526=1+767N=3\cdot842^2.
\]

Each relation is nonclosing alone. Together they have the same nonzero
square class. Their product has exact root

\[
R=\sqrt{P_1P_2}=108618,
\]

\[
\gcd(R-1,N)=47,
\qquad
\gcd(R+1,N)=59.
\]

Deleting the first relation because it did not close immediately loses the
factor certificate.

There is also a canonical presentation inside the old modular subgroup:

\[
c=[3^{99}43]_N=1263,
\qquad
w=1684,
\]

\[
1263\cdot1684=3\cdot842^2=P_2.
\]

Canonical reduction adds no abstract group element. It creates the useful
exact integer presentation.

### 9.2 A 166-relation circuit at \(N=202{,}537{,}109\)

Let

\[
N=202{,}537{,}109
=10{,}267\cdot19{,}727.
\]

A public one-round rule uses seeds \(2,\ldots,28\), refines their endpoints,
selects 27 block pairs, and follows two bounded trajectories per pair.

It performs 12,549 individual inverse-pair sign screens. Every local screen
fails.

After exact-value deduplication:

\[
\begin{array}{rcl}
\text{distinct exact columns}&=&9{,}414,\\
\text{square-class rank}&=&8{,}926,\\
\text{kernel dimension}&=&488.
\end{array}
\]

A public kernel-basis vector uses 166 distinct exact values. Its root is

\[
R\equiv132{,}013{,}085\pmod N,
\]

\[
\gcd(R-1,N)=19{,}727,
\qquad
\gcd(R+1,N)=10{,}267.
\]

Factor-assisted diagnosis showed that these 166 columns have rank 165 and
nullity one. Every proper subset is independent. Their shared-prime graph is
connected and crosses eight trajectories. This is one genuine
cross-relation circuit, not one lucky local identity.

### 9.3 Two useless layers become useful at \(N=3{,}241{,}632{,}473\)

Let

\[
N=3{,}241{,}632{,}473
=41{,}011\cdot79{,}043.
\]

After global exact-value deduplication:

- The frozen layer has 11,885 columns, rank 11,878, and kernel dimension 7.
  All seven basis roots are global \(+1\).
- The appended layer contributes 684 genuinely new columns. Those columns
  are independent when decoded alone.
- The union has 12,569 columns, rank 12,551, and kernel dimension 18.

The cross-layer quotient therefore has dimension

\[
18-7-0=11.
\]

Its normalized root image has rank one.

A hostile verifier found a 363-value cross-layer dependency. A separate
proof-blind decoder found a different 367-value dependency. Both give

\[
R\equiv1{,}058{,}780{,}986\pmod N,
\]

\[
\gcd(R-1,N)=79{,}043,
\qquad
\gcd(R+1,N)=41{,}011.
\]

Neither layer contains a useful root alone. Every useful dependency must
cross the layer boundary. This is a real stateful effect.

A later no-stop replay used a fixed source with 67,681 positions. It obtained
12,962 exact columns, nullity 39, and 11 useful kernel-basis roots. Thus the
success did not depend on a supplied support or a hidden stopping position.
The fixed source was historically selected after earlier experiments, so it
is still only a fixed-input theorem.

### 9.4 Fresh 54-bit fixed-source success

For

\[
N=12{,}800{,}004{,}879{,}996{,}637
=80{,}000{,}059\cdot159{,}999{,}943,
\]

a complete fixed all-seed-pair source has 8,348,507 positions. An audited
prefix contained a 6,486-value exact dependency with root

\[
R\equiv5{,}266{,}287{,}723{,}884{,}331\pmod N,
\]

\[
\gcd(R-1,N)=159{,}999{,}943,
\qquad
\gcd(R+1,N)=80{,}000{,}059.
\]

Append monotonicity proves that this useful root survives to the end of the
fixed source. This is a no-advice polynomial algorithm for that one input,
not an all-input theorem.

---

## 10. Important structural barriers

### 10.1 Abstract subgroup growth is not the missing operation

For every finite abelian group \(H\), sufficiently many independent uniform
elements generate \(H\) with constant probability. Applied to

\[
G_N=(\mathbb Z/N\mathbb Z)^\times,
\]

\(O(\log N)\) uniform units generate the complete unit group with constant
probability. For a distinct odd semiprime, three uniform units suffice with
probability at least \(1/(\zeta(2)\zeta(3))\).

Therefore a feedback theorem cannot rely only on enlarging an abstract
subgroup. On a constant-probability event, the full unit group is already
available abstractly.

The real issue is accessibility:

\[
\boxed{
\text{abstract element availability}
\ne
\text{known short word}
\ne
\text{known integer block}
\ne
\text{known exact relation}.}
\]

There is a sharper semiprime version. For \(N=pq\), set

\[
g=\gcd(p-1,q-1),
\qquad
A=\frac{p-1}{g},
\qquad
B=\frac{q-1}{g}.
\]

Then

\[
G_N^{\,N-1}\cong C_A\times C_B,
\qquad
\gcd(A,B)=1.
\]

Two independent uniform accepted units, raised to \(N-1\), generate this
factor-bearing rectangle with probability at least

\[
\frac{6}{\pi^2}.
\]

The two coordinate axes contain factor-revealing elements. Direct uniform
sampling can still miss the axes because their density can be exponentially
small in the input length. The missing operation is **axis localization**,
not group generation. This is one precise point of contact with hidden
subgroup and relation-lattice thinking.

### 10.2 One-block feedback is saturated

If the source already scans every valid state through the largest known
quotient bound, feeding back one whole current block produces no new relation
value and no proper block split. This closes the simplest feedback version.

Cross-relation products, repeated powers, signed words, canonical reduction,
and proper descendants are genuinely different operations.

### 10.3 Many records are not progress

At

\[
N=64{,}570{,}081
=\frac{3^{17}-1}{2},
\]

all 16 nontrivial states of one power orbit give the same exact value
\(3^{17}=1+2N\). Duplicate dependencies have only root \(+1\), and no new
block appears.

There are also constructed families with many consecutive independent
relations, each protected by a private odd prime row. Thus:

- record count is not progress;
- raw kernel nullity is not progress;
- trajectory length is not progress;
- relation provenance is not progress.

The progress measure must include the normalized root image.

### 10.4 Cross-pair provenance does not force closure

There are infinite trial-division-hard semiprime families with
\(\Theta(n/\log n)\) genuine cross-pair exact values, each with a different
private odd row. The selected columns are independent.

This does not control the complete source, but it blocks an easy proof that
“polynomially many cross-pair relations must close.”

### 10.5 Complete-universe private-row theorem

Let the columns be all distinct canonical exact values \(A_N(c)>1\).
For every prime \(r\),

\[
\boxed{
\deg(r)\le
\left\lfloor\frac{N-1}{r}\right\rfloor.}
\]

Proof: assign every \(r\)-divisible exact value to a distinct endpoint below
\(N\) that is divisible by \(r\). An endpoint has a unique inverse, so two
different exact values cannot receive the same endpoint.

Therefore every present row with

\[
r>\frac{N-1}{2}
\]

is permanently private against the complete canonical universe.

There is a proof-certified trial-division-hard distinct semiprime witness:

\[
N=2{,}000{,}887{,}089{,}301
=1{,}000{,}289\cdot2{,}000{,}309,
\]

\[
r=\frac{N+1}{2}
=1{,}000{,}443{,}544{,}651
\quad\text{prime}.
\]

Seed \(2\) has inverse \(r\) and exact value

\[
N+1=2r.
\]

The \(r\)-row has degree one against every possible canonical exact-value
column.

This falsifies universal row reuse. It does not block factoring. A private
row and its column peel away exactly. Every dependency and every root among
the remaining columns is unchanged.

---

## 11. Trial history: how the framework evolved

| Version | Main idea | What survived | What failed or remained open |
|---|---|---|---|
| V0 | Independent uniform canonical inverses | Exact completion-biased carry distribution | Polynomial samples are too dispersed; no factor correlation |
| V1 | Deterministic offsets and short trajectories | Some exact square dependencies | Observed roots were global algebraic decoys |
| V2 | Feed back one whole gcd-free block | Exact quotient and saturation laws | Dominated by a bounded static scan |
| V3 | Select blocks across several relations | Exact new relations and direct separators at \(N=21,55\) | Candidate selection can be exponential |
| V4 | Use endpoint refinement to expand the block vocabulary | Exact representation-level expansion at \(N=209,4033,2047\) | Small witnesses have stronger static shortcuts |
| V5 | Canonical-residue closure and bounded power banks | Complete fixed post-refinement chains | No all-input reachability or density law |
| V6 | Retain every relation and decode cross-layer circuits | Exact useful circuits at \(N=2773\), \(202{,}537{,}109\), and \(3{,}241{,}632{,}473\) | No theorem that another input gets a useful circuit |
| V7 | Complete fixed all-pairs sources | Many finite positive controls, including a fresh 54-bit case | No preregistered complete-source null; feedback gate did not open |
| V8 | Prove row-reuse barriers | Infinite selected-submatrix barrier and complete-universe degree bound | A private row does not imply source failure |
| V9 | Compare feedback with the complete static source | Exact attribution correction at \(4033\) and the large private-row witness | No static-failure/feedback-success certificate yet |

---

## 12. Latest attribution corrections

### 12.1 Why \(N=4033\) is not yet a full feedback advantage

The restricted P78 history proves a real representation-level transition.
However, the stronger complete static source already contains the relevant
information.

There is also a general algebraic correction. If

\[
N=2q-1
\]

with \(q\) prime, then

\[
q\equiv2^{-1}\pmod N.
\]

Naming \(q\) does not add an independent modular generator. Every word using
\(q\) is a Laurent word using \(2\), with a signed exponent. It can enlarge a
bounded language that previously allowed only nonnegative exponents. It
cannot enlarge the abstract subgroup. It also cannot reuse the private
\(q\)-row, because \(q\) divides a canonical exact value only for the inverse
pair \(\{2,q\}\).

For \(N=4033\), the no-stop static replay had

\[
\begin{array}{rcl}
\text{source positions}&=&19{,}151,\\
\text{first residues}&=&2{,}737,\\
\text{distinct exact values}&=&869,\\
\text{rank}&=&522,\\
\text{nullity}&=&347.
\end{array}
\]

Hypothetically authorizing all new pairings with the named block
\(q=(N+1)/2=2017\) added:

\[
50\text{ new residue presentations},
\qquad
0\text{ new exact-value columns}.
\]

The static seed \(c=4\) already has inverse \(3025\) and

\[
4\cdot3025=12100=110^2,
\]

\[
\gcd(110-1,4033)=109,
\qquad
\gcd(110+1,4033)=37.
\]

Thus the static source already has both square closure and a useful root.
The feedback chain remains an exact restricted-state mechanism, but it does
not prove capability beyond the complete static source.

### 12.2 Why the complete-universe private-row witness is not a feedback test

For

\[
N=2{,}000{,}887{,}089{,}301,
\]

the private seed row remains private, as proved. Yet the fixed static
all-pairs source reaches a public direct certificate at attempt 166,901:

\[
c=[2\cdot12^{1012}]_N
=1{,}407{,}720{,}713{,}745,
\]

\[
w=c^{-1}_{\rm can}
=1{,}483{,}206{,}522{,}841,
\]

\[
\gcd(c-w,N)=1{,}000{,}289.
\]

A stopped prefix also contained 42,071 non-global fundamental roots. The
first recorded root was

\[
x=721{,}509{,}455{,}990,
\]

\[
\gcd(x-1,N)=1{,}000{,}289,
\qquad
\gcd(x+1,N)=2{,}000{,}309.
\]

The run was stopped near 993 MB of resident memory because success was
already certified. The result is conceptually important:

\[
\boxed{
\text{failure of universal row reuse}
\not\Rightarrow
\text{failure of closure or factoring}.}
\]

The feedback gate is closed on this input because the fixed static source
already succeeds.

---

## 13. Proposed adaptive framework

Maintain a state

\[
\mathcal S=(B,\mathcal R,M,\bar\rho,\mathcal P),
\]

where:

- \(B\) is a pairwise-coprime integer block basis;
- \(\mathcal R\) is the list of distinct exact relation values;
- \(M\) is the complete factor-free parity matrix;
- \(\bar\rho\) is the normalized root map on the kernel;
- \(\mathcal P\) stores endpoint and word provenance.

### 13.1 Initialization

1. Remove factor \(2\), perfect powers, and small factors according to a
   public polynomial bound.
2. Generate a fixed seed source from \(N\).
3. Compute canonical inverses.
4. Run every direct gcd screen.
5. Refine all endpoint integers jointly.
6. Deduplicate exact values, but retain endpoint presentations.
7. Run the complete factor-free decoder.

### 13.2 One feedback round

For every candidate word allowed by a public polynomial menu:

1. Form a modular residue

   \[
   c=\left[\prod_jq_j^{e_j}\right]_N.
   \]

2. Screen \(\gcd(c,N)\).
3. Compute the canonical inverse \(w=[c^{-1}]_N\).
4. Screen

   \[
   \gcd(c-w,N),\qquad\gcd(c+w,N).
   \]

5. Record

   \[
   A=cw=1+\kappa N.
   \]

6. Refine \(c,w\), and all retained endpoints jointly.
7. Retain every genuinely new exact relation. Do not delete a relation only
   because it fails to close now.
8. Update the complete parity kernel and normalized root image.
9. If a useful root occurs, return the verified gcd factor.

### 13.3 What counts as real progress

At least one of these events must occur:

1. a verified proper factor;
2. a block split that changes the future allowed word source;
3. a new exact relation column;
4. a new kernel direction;
5. a nonzero change in the normalized root image.

Relation count or raw nullity alone does not count as progress.

---

## 14. Promising candidate generators inspired by the GPT Pro comments

These are proposals, not proved algorithms.

### 14.1 Fixed-support local closure

Enumerate

\[
g=\prod_{j=1}^{s}b_{i_j}^{e_j},
\qquad
s\le d,
\]

for fixed \(d=3\) or \(4\), with public polynomial exponent bounds.

This is polynomial work for fixed \(d\). It includes repeated-block
trajectories and several known fixed certificates.

**Open issue:** no theorem says that a useful candidate always has bounded
support.

### 14.2 CRT beam search for high-support words

For a positive product \(g\), define

\[
\rho(g)=(-N^{-1})\bmod g,
\qquad
w(g)=\frac{1+\rho(g)N}{g}.
\]

If \(\gcd(g,b)=1\), let

\[
\rho_b=(-N^{-1})\bmod b,
\]

\[
t=(\rho_b-\rho(g))g^{-1}\bmod b.
\]

Then

\[
\rho(gb)=\rho(g)+gt,
\]

\[
w(gb)=\frac{w(g)+Nt}{b}.
\]

This gives exact incremental CRT bookkeeping. A beam can retain candidates
with small \(w\), small \(\rho/g\), small inverse distance, large refinement
gain, or diverse parity signatures.

**Open issue:** the tested scalar scores are not monotone under extension.
No lossless dominance rule is known. A polynomial-width beam is currently a
heuristic selector.

### 14.3 Remainder and product-tree sieve

If a retained relation product is

\[
P=1+KN,
\]

then for every integer \(r\),

\[
\boxed{
\gcd(P,K-r)=\gcd(P,1+rN).}
\]

The identity is exact because \(\gcd(P,N)=1\).

This suggests scanning small \(r\) and using a product tree to locate
high-support contributors without enumerating every relation subset.

**Open issue:** the identity alone does not prove that the extracted divisor
corresponds to a legal useful block word, or that a useful small \(r\) exists
with inverse-polynomial density.

### 14.4 Canonical-residue closure

Allow any public modular word with provenance:

\[
c=\left[\prod_jq_j^{e_j}\right]_N.
\]

Then replace it by the canonical integer pair

\[
(c,[c^{-1}]_N).
\]

This removes the restriction that the unreduced positive product must be
below \(N\). It is the operation that completes the restricted \(4033\)
chain.

Promising exponent schedules include:

- \(1,\ldots,\operatorname{poly}(n)\);
- powers of two;
- \(\operatorname{lcm}(1,\ldots,t)\);
- sparse mixed exponent vectors;
- a small reservoir of dense random vectors.

**Open issue:** no all-input schedule or success density is known.

### 14.5 Power-bank decoder

For an exposed block \(u\), test public exponents such as

\[
M_B=\operatorname{lcm}(1,\ldots,B)
\]

and punctured variants \(M_B/\ell^j\).

This is complete when the two hidden local orders differ and one complete
prime-power component is bounded by \(B\).

**Open issue:** equal local orders and phase-only gains require mixed words.
No public branch detector is known.

### 14.6 Temporary probes and state control

It is reasonable to discard a probe that produces no new endpoint, no new
exact value, no block split, and no factor. It is not safe to discard a new
exact relation merely because it is nonclosing at insertion time.

A lossless polynomial state compression remains open. Explicit polynomial
caps prove polynomial runtime only for the capped procedure. They do not
prove that the cap preserves a useful future circuit.

### 14.7 Repeated 2-saturation

Repeated 2-saturation or complete parity decoding is useful operationally,
but it is not the missing mathematical component. The factor-free decoder is
already complete for every explicit relation list.

The missing part is candidate generation and a non-global root law.

---

## 15. The precise research problem

### 15.1 Main technical problem: prove source-side progress

The decoder is not the main open problem. For any explicit polynomial-size
relation list, the factor-free decoder can find every exact square dependency
and test a basis of its roots.

The main open problem is a **source-side progress theorem**.

Assume that the current public state contains:

- a polynomial-size set of pairwise-coprime integer blocks \(B\);
- a polynomial-size set of retained exact relations \(R\);
- their complete factor-free square decoder;
- no proper factor from any direct gcd screen; and
- only global roots \(+1\) and \(-1\) from every decoded dependency.

We need a public polynomial-time rule that selects an integer presentation

\[
c=\left[\prod_{b\in B}b^{e_b}\right]_N
\]

and its least positive inverse

\[
w=c^{-1}\bmod N.
\]

The rule must have a proved guarantee. Within polynomially many rounds, and
with at least inverse-polynomial probability, it must do one of these things:

1. produce a proper factor through
   \(\gcd(c-w,N)\) or \(\gcd(c+w,N)\);
2. create an essential new integer block or exact relation that gives a
   strictly useful state transition; or
3. create a square dependency whose root is non-global, so its signs differ
   across the unknown prime factors of \(N\).

The second exit needs more than the word *new*. It needs a polynomially
bounded progress measure. Each accepted transition must increase that
measure, and polynomially many increases must force the first or third exit.
The algorithm must also keep only polynomially many bits of state without
discarding a relation that is essential later.

In short, the missing object is:

> A public polynomial-time sampler of integer presentations that is provably
> correlated with a hidden CRT sign mismatch.

This is hard for five concrete reasons:

1. The candidate space contains exponentially many block words.
2. Generating the full multiplicative group modulo \(N\) is not sufficient.
   The algorithm needs useful short integer presentations of group elements.
3. Feedback can give a new integer encoding of an old residue. This can split
   blocks, but many such splits do not help with the hidden factors.
4. More relations, more blocks, or a larger nullspace do not force a
   non-global root. They can give only duplicates, private rows, or global
   roots.
5. A feedback success can disappear after a complete static-source audit.
   The static source can already contain the exact values needed for the same
   factor certificate.

This is the hard boundary between the present framework and a factoring
algorithm. The framework gives a new way to generate candidates. It does not
yet prove that a useful candidate occurs often enough, or at all, for every
input.

### 15.2 Decisive finite milestone

Find a preregistered odd composite \(N\) with no factor below a public
polynomial trial bound such that:

1. A fixed complete static source \(S_0(N)\) is exhausted.
2. Every direct static gcd screen is nonproper.
3. The complete static normalized root image is zero.
4. A public factor-free feedback step exposes a block that did not exist in
   the static block basis.
5. The later source uses that block in an essential way.
6. A new exact relation or cross-layer dependency has a non-global root.
7. Removing the feedback-created block from the certificate destroys the
   success.

This would prove a real algorithmic capability difference, even before an
all-input theorem is available.

No such certificate is currently known.

### 15.3 Positive all-input theorem target

Let \(n=\lceil\log_2N\rceil\). Seek constants \(d,c\) and a public adaptive
candidate generator with \(n^{O(1)}\) work and state such that, for every odd
non-perfect-power composite \(N\), every live state with zero normalized root
image has one of the following:

1. a \(d\)-local feedback candidate that gives a proper factor;
2. a \(d\)-local candidate that creates an essential future-source block
   split;
3. an inverse-polynomial density of useful candidates in a precisely defined
   CRT-beam or remainder-sieve distribution;
4. a new closure whose normalized root class is nonzero.

A deterministic existence statement for one bounded-local candidate would
give a deterministic polynomial algorithm. An inverse-polynomial density
statement would give a randomized Las Vegas polynomial algorithm after
verified repetition.

### 15.4 A cleaner two-lemma decomposition

The desired proof may separate into:

**Presentation-progress lemma.**  
Before a factor is found, a polynomial candidate rule produces a strict,
usable integer-presentation gain with inverse-polynomial probability.

**Root-progress lemma.**  
Polynomially many such gains force a nonzero normalized root image, rather
than only more square relations or global-root decoys.

Neither lemma is currently proved.

### 15.5 Negative theorem target

A negative result would also be valuable. Possible targets:

1. Extend one-block saturation to every fixed-support feedback language.
2. Construct a trial-division-hard family whose complete adaptive
   presentation closure has stable private rows and zero kernel.
3. Prove that a specified beam score can prune every useful path.
4. Prove that a specified polynomial state cap necessarily deletes a future
   useful circuit.

Such results would identify the exact strength required from any successful
classical sampler.

---

## 16. Questions for another agent

An agent can contribute by addressing one narrow question.

### Prior art

1. Is the full adaptive loop already present under another name in factoring,
   index calculus, dynamic factor bases, large-prime recombination, rational
   reconstruction, or gcd-free basis literature?
2. Is the complete-universe degree bound

   \[
   \deg(r)\le\lfloor(N-1)/r\rfloor
   \]

   known for canonical inverse products?
3. Is there prior work where integer representatives of already-known group
   elements recursively change a factor base or relation source?

### Positive theory

4. Can one prove a lossless dominance rule for CRT beam search?
5. Can carry congruence or endpoint geometry give inverse-polynomial row
   reuse?
6. Can the remainder identity locate a legal high-support feedback word in
   polynomial work?
7. Can one prove a bounded-support or bounded-treewidth theorem for a useful
   relation circuit?
8. Can the canonical-inverse completion bias be connected to factor
   correlation rather than only smoothness or multiplicity?

### Counterexamples and barriers

9. Can one construct an infinite family where the complete static source is
   null but feedback is positive?
10. Can one instead construct a family where every bounded-round feedback
    closure is null?
11. Can one generalize the universe-private-row theorem from one column to a
    full-rank complete source?

### Quantum connection

12. Is there a precise classical distribution produced by this feedback loop
    that approximates any useful marginal of Shor or Regev sampling?
13. Can a Bayesian or graphical model describe the adaptive presentation
    process without assuming the hidden CRT factors?
14. Is there a provable interface between canonical-inverse relation
    generation and approximate modular relation-lattice sampling?

No result presently suggests that the Shor circuit itself is classically
simulatable.

---

## 17. Executable certificate checker

The following Python program uses only exact integer arithmetic, modular
inversion, gcd, integer square root, and deterministic Miller--Rabin for the
displayed 64-bit primality claims.

```python
from math import gcd, isqrt


def canonical_inverse(N, c):
    assert 1 <= c < N and gcd(c, N) == 1
    return pow(c, -1, N)


def check_pair(N, c, w, carry):
    assert canonical_inverse(N, c) == w
    assert c * w == 1 + carry * N


def is_prime_64(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # Deterministic for every n < 2^64.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


# N = 21: cross-relation direct separator.
N = 21
assert 22 == 2 * 11 == 1 + N
assert 85 == 5 * 17 == 1 + 4 * N
check_pair(N, 10, 19, 9)
assert gcd(10 - 19, N) == 3

# N = 55: cross-relation non-global involution.
N = 55
assert 56 == 2 * 28 == 1 + N
assert 111 == 3 * 37 == 1 + 2 * N
assert 21 * 21 == 1 + 8 * N
assert gcd(21 - 1, N) == 5
assert gcd(21 + 1, N) == 11

# N = 209: integer refinement changes the bounded block menu.
N = 209
assert 31 * 27 == 1 + 4 * N
assert 3 * 70 == 1 + N
check_pair(N, 80, 81, 31)
assert gcd(80, 70) == 10
assert gcd(81, 27) == 27
assert gcd(10 + 1, N) == 11

# N = 4033: restricted feedback chain.
N = 4033
assert N == 37 * 109
assert 2 * 2017 == 1 + N
assert 64 * 3970 == 1 + 63 * N
assert 8 * 3529 == 1 + 7 * N
check_pair(N, 2048, 3905, 1983)
assert gcd(1985, 3905) == 5
check_pair(N, 630, 3220, 503)
assert gcd(630 - 3220, N) == 37
check_pair(N, 2367, 443, 260)
assert gcd(2367 - 443, N) == 37
assert gcd(pow(5, 2520, N) - 1, N) == 37

# N = 4033: stronger static shortcut.
assert canonical_inverse(N, 4) == 3025
assert 4 * 3025 == 110 * 110
assert pow(110, 2, N) == 1
assert gcd(110 - 1, N) == 109
assert gcd(110 + 1, N) == 37

# N = 2047: phase-only feedback expansion.
N = 2047
assert N == 23 * 89
assert 11 * 1861 == 1 + 10 * N
assert 312 * 269 == 1 + 41 * N
check_pair(N, 1778, 1735, 1507)
assert gcd(312, 1778) == 2
assert gcd(2 * 11 + 1, N) == 23

# N = 2773: two retained relations close.
N = 2773
assert N == 47 * 59
P1 = 3 * 1849
P2 = 842 * 2526
assert P1 == 1 + 2 * N == 3 * 43**2
assert P2 == 1 + 767 * N == 3 * 842**2
R = isqrt(P1 * P2)
assert R * R == P1 * P2 == 108618**2
assert gcd(R - 1, N) == 47
assert gcd(R + 1, N) == 59
check_pair(N, 1263, 1684, 767)
assert 1263 * 1684 == P2

# 166-relation audited root.
N = 202_537_109
R = 132_013_085
assert N == 10_267 * 19_727
assert pow(R, 2, N) == 1
assert gcd(R - 1, N) == 19_727
assert gcd(R + 1, N) == 10_267

# Cross-layer audited root.
N = 3_241_632_473
R = 1_058_780_986
assert N == 41_011 * 79_043
assert pow(R, 2, N) == 1
assert gcd(R - 1, N) == 79_043
assert gcd(R + 1, N) == 41_011

# Fresh 54-bit fixed-source root.
N = 12_800_004_879_996_637
R = 5_266_287_723_884_331
assert N == 80_000_059 * 159_999_943
assert pow(R, 2, N) == 1
assert gcd(R - 1, N) == 159_999_943
assert gcd(R + 1, N) == 80_000_059

# Complete-universe private-row witness and static direct certificate.
p = 1_000_289
q = 2_000_309
N = 2_000_887_089_301
r = 1_000_443_544_651
assert N == p * q
assert 2 * r == N + 1
assert all(is_prime_64(x) for x in (p, q, r))
assert r > (N - 1) // 2
assert gcd(r - 2, N) == gcd(r + 2, N) == 1

c = 1_407_720_713_745
w = 1_483_206_522_841
assert c == 2 * pow(12, 1012, N) % N
assert canonical_inverse(N, c) == w
assert gcd(c - w, N) == p

x = 721_509_455_990
assert pow(x, 2, N) == 1
assert gcd(x - 1, N) == p
assert gcd(x + 1, N) == q

print("all displayed certificates passed")
```

---

## 18. How to interpret the evidence

### Strongest positive conclusions

1. Canonical integer normalization is a real source operation.
2. Joint refinement can expose new named blocks even when the modular residue
   is redundant.
3. Retained relation state can produce useful roots only through
   cross-relation or cross-layer interaction.
4. The complete factor-free decoder is available.
5. Several fixed polynomial-size sources factor nontrivial inputs without a
   supplied dependency support.

### Strongest negative conclusions

1. Independent canonical-inverse samples are too diffuse for easy local
   collisions.
2. Exact square relations can be global-root decoys.
3. One-block feedback is statically saturated.
4. Abstract subgroup growth is not enough.
5. Relation count, nullity, and cross-pair provenance do not force useful
   closure.
6. Universal row reuse is false, even in the complete canonical universe.
7. The best small feedback witnesses are absorbed by stronger static
   sources.

### Current overall assessment

The route is reasonably described as **partly new, leaning new**:

- the algebraic end point is classical;
- the decoder infrastructure is classical or a precise synthesis of known
  tools;
- the adaptive integer-presentation loop appears to be a new algorithmic
  architecture;
- the fixed mechanism and cross-layer certificates are nontrivial;
- the all-input sampler or progress law is still missing.

The framework has moved beyond isolated identities. It now has:

1. a well-defined state;
2. exact progress gates;
3. positive mechanism witnesses;
4. hostile counterexamples to easy proofs;
5. a precise decisive experiment;
6. a precise theorem target.

The next major result should not be another small identity. It should prove
that feedback creates a capability unavailable to the complete static source,
or prove that an important bounded feedback language can always be compiled
back into a static source.

---

## 19. Repository evidence map

The brief is self-contained. These files contain the full proofs, audit
records, and machine outputs:

- Complete decoder and promoted results:
  [`PROVED.md`](./PROVED.md)
- Current synthesis:
  [`notes/Progress.md`](./notes/Progress.md)
- Failed mechanisms and exact retry boundaries:
  [`FAILED.md`](./FAILED.md)
- Complete-universe private-row theorem:
  [`experiments/F120_complete_carry_closure_theory/RESULT.md`](./experiments/F120_complete_carry_closure_theory/RESULT.md)
- \(4033\) static-versus-feedback comparison:
  [`experiments/F121_private_row_feedback_grammar/RESULT.md`](./experiments/F121_private_row_feedback_grammar/RESULT.md)
- Static prefix on the private-row witness:
  [`experiments/F122_stable_private_full_source/RESULT.md`](./experiments/F122_stable_private_full_source/RESULT.md)

The important promoted result labels are P65, P66, P70, P73, P74, P76,
P78, P81, P86, P88, and P97--P112.
