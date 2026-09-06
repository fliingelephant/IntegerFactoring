# F154 V3 blind reconstruction

## Isolation and verdict

Before reading the statement, I verified

```text
SHA-256(V3_STATEMENT.md)
= 7021a1b9c509460606ea1168dc0f782e25cfa1461639ae256f41caf6147c1ef3.
```

I read no other F154 artifact or contextual file.

**Verdict: qualified pass.** Conditional on the stated F152 quotient-section
premise, the decorated-section construction, distinctness theorem, pure and
mixed decoder inertness, triple identity, and quasipolynomial cost bound are
correct. The restricted refinement claim is also correct as an interface
claim, not as an information-theoretic claim. All displayed numerical claims
for (N=77), including the orders, (26^{15}), and the two factor-producing
gcds, check exactly.

There is one useful scope qualification. The displayed endpoint screens
(gcd(26,77)) and (gcd(181,77)) are both inert, as claimed. If “direct
screens” is read more broadly to include a post-refinement (x\mathbin{\pm}1)
screen on every newly named block, then not all such screens are inert:

\[
\gcd(181+1,77)=7.
\]

Thus the (26^{15}) test is a valid later capability witness, but it is not
the first or simplest possible success after this refinement. This does not
contradict the literal statement, which only claims that the displayed
(gcd(x,N)) endpoint screens fail. It refutes any stronger reading that all
post-refinement direct screens must fail until the power test.

## 1. Decorated group and lifted section

Write addition in (mathbf F_2^m) as (oplus). Coordinate by coordinate,

\[
Q(v)Q(w)=Q(v\oplus w)C(v,w)^2. \tag{1}
\]

Therefore, if (z^2\equiv Q(v)) and (t^2\equiv Q(w)\pmod N), then

\[
\bigl(ztC(v,w)^{-1}\bigr)^2\equiv Q(v\oplus w)\pmod N.
\]

This proves closure of the stated product. The coordinatewise cocycle
identity for (C) proves associativity, and symmetry of (C) proves
commutativity. Also,

\[
(v,z)\star(v,z)
=\left(0,z^2Q(v)^{-1}\right)=(0,1).
\]

Thus every decorated element is self-inverse. The two global elements

\[
H=\{(0,1),(0,-1)\}
\]

form a subgroup. There can be more roots of (1) modulo a composite (N),
but the no-factor premise says that the retained subgroup meets the
zero-parity fibre only through these global roots, which is why quotienting
by (H) is the relevant operation.

Let (b_1,\ldots,b_d) be the chosen parity basis, and let (e_i) be its
retained decorated lifts. Define

\[
\widetilde h\!\left(\bigoplus_i\epsilon_i b_i\right)
=\mathop{\star}_{i:\epsilon_i=1}e_i.
\]

The basis representation is unique, and every (e_i) has order two, so this
is a homomorphism. Its quotient agrees with (h) on a basis and hence on all
of (W). In particular,

\[
\widetilde h(0)=(0,1).
\]

Every (z_v) is a unit: (z_v^2\equiv Q(v)) and (Q(v)) is a unit. Its
least positive inverse (s_v) therefore exists. Since

\[
s_v^2Q(v)\equiv z_v^{-2}z_v^2\equiv1\pmod N,
\]

the record (P_v=s_v^2Q(v)), supplied with root (1), is valid. For a
record (a^2Q(v)) with supplied modular root (alpha), its decorated
coordinate is (alpha a^{-1}). Hence the new record has decorated lift

\[
(v,1\cdot s_v^{-1})=(v,z_v)=\widetilde h(v),
\]

exactly as claimed.

## 2. Rational squareclass independence and distinctness

The pairwise-coprime nonsquare hypothesis gives the exact independence that
the proof needs. If (J) is nonempty, then

\[
\prod_{j\in J}q_j
\]

is not a rational square. To see this, choose (j\in J). Since (q_j) is
not an integer square, some prime has odd valuation in (q_j). Pairwise
coprimality keeps that prime out of every other (q_k), so its valuation in
the product remains odd. The same valuation argument works when each
(q_j) occurs with exponent (+1) or (-1).

If (P_v=P_w), then

\[
\frac{Q(v)}{Q(w)}=\left(\frac{s_w}{s_v}\right)^2. \tag{2}
\]

If (v\ne w), a coordinate in their symmetric difference gives an odd
prime valuation on the left of (2), while every valuation on the right is
even. This is impossible. Therefore the (P_v) are pairwise distinct.

Because (widetilde h(0)=(0,1)), one has (z_0=s_0=1), and hence (P_0=1).
If (v\ne0), then (Q(v)>1): every selected (q_j) is a positive
nonsquare and therefore at least (2). Thus (P_v=s_v^2Q(v)>1).

This proves the distinctness and positivity claims without assuming that
the residues (z_v), or their representatives (s_v), are themselves
distinct.

## 3. Pure completion dependencies and their normalized roots

For (S\subseteq W), let

\[
k_j=\#\{v\in S:v_j=1\}.
\]

Then

\[
\prod_{v\in S}P_v
=\left(\prod_{v\in S}s_v\right)^2
 \prod_{j=1}^m q_j^{k_j}. \tag{3}
\]

If every (k_j) is even, (3) is a square. If some (k_j) is odd, choose a
prime having odd valuation in (q_j). Pairwise coprimality makes its total
valuation in (3) odd, so (3) is not a square. Since the (j)-th coordinate
of (igoplus_{v\in S}v) is (k_j\bmod2), this proves

\[
\prod_{v\in S}P_v\text{ is a square}
\quad\Longleftrightarrow\quad
\bigoplus_{v\in S}v=0. \tag{4}
\]

Assume now that (4) holds. The positive integer square root is

\[
R_S=left(\prod_{v\in S}s_v\right)
    \prod_{j=1}^m q_j^{k_j/2}. \tag{5}
\]

Multiplying the decorated section elements gives

\[
\mathop{\star}_{v\in S}(v,z_v)
=\left(0,
\left(\prod_{v\in S}z_v\right)
\prod_{j=1}^m q_j^{-k_j/2}
\right)
=\widetilde h(0)=(0,1). \tag{6}
\]

Consequently,

\[
\prod_{v\in S}z_v
\equiv\prod_jq_j^{k_j/2}\pmod N.
\]

Using (s_v\equiv z_v^{-1}), equation (5) now gives

\[
R_S\equiv1\pmod N. \tag{7}
\]

The product of all supplied roots is also (1). Whether normalization is
written as supplied root divided by the positive exact root or by the
inverse convention, (7) makes the normalized root exactly (+1). This is
stronger than merely saying it is global.

## 4. Mixed old/completion dependencies

Let (e_i) be old decorated records of parities (u_i), and let (c_v) be
completion records. The quotient-section premise says

\[
\overline{e_i}=h(u_i),
\qquad
\overline{c_v}=h(v).
\]

For any mixed parity dependency,

\[
\bigoplus_i u_i\oplus\bigoplus_v v=0,
\]

so, in the quotient,

\[
\prod_i\overline{e_i}\prod_v\overline{c_v}
=h(0)=\overline{(0,1)}.
\]

The unquotiented product therefore lies in (H), and its normalized root is
(+1) or (-1). No mixed dependency can create a non-global root. Pure
completion dependencies have the sharper (+1) result from Section 3.
Thus adjoining the completion cannot enlarge the decoder image modulo global
roots and cannot create a useful gcd split in the current decoder.

The exact-value deletion sentence needs its stated “root-aware” qualifier.
If two occurrences have the same exact integer value, their two-record
comparison is itself a dependency. Under the no-factor premise, the ratio of
their normalized supplied roots is global. One occurrence can therefore be
substituted for the other without changing the useful root image, provided
the comparison sign is retained when the literal ({+1,-1}) image matters.
A deletion that silently discards the root comparison, occurrence count, or
provenance does not preserve those metadata. The statement explicitly keeps
that metadata whenever the later grammar may observe it, so its qualified
claim is sound.

## 5. Triple identity

Equation (1) also gives the exact integer identity

\[
Q(v)Q(w)Q(v\oplus w)
=\left(Q(v\oplus w)C(v,w)\right)^2. \tag{8}
\]

Multiplying by the three (s)-squares proves

\[
P_vP_wP_{v\oplus w}
=\left(s_vs_ws_{v\oplus w}Q(v\oplus w)C(v,w)\right)^2. \tag{9}
\]

The section law says

\[
z_{v\oplus w}=z_vz_wC(v,w)^{-1},
\]

and inversion gives

\[
s_{v\oplus w}\equiv s_vs_wC(v,w)\pmod N. \tag{10}
\]

For the positive root displayed in (9), equations (10) and the definition of
(P_{v\oplus w}) yield

\[
\begin{aligned}
s_vs_ws_{v\oplus w}Q(v\oplus w)C(v,w)
&\equiv s_{v\oplus w}^2Q(v\oplus w)\\
&=P_{v\oplus w}\equiv1\pmod N.
\end{aligned}
\]

This also covers (v=w) or a zero vector; in those cases the “triple” has
repeated indexed factors, but the identity and root remain valid.

## 6. Size and quasipolynomial cost

There is one indexed record for each vector of a (d)-dimensional binary
space, hence exactly (2^d) records.

Put

\[
\ell_j=\left\lceil\log_2(q_j+1)\right\rceil,
\qquad \Lambda_Q=\sum_j\ell_j.
\]

The definitions imply (s_v<2^n) and (q_j<2^{\ell_j}). Therefore

\[
P_v=s_v^2Q(v)<2^{2n+\Lambda_Q},
\]

so its bit length is at most (2n+\Lambda_Q+O(1)).

After the basis lifts are known, enumerate the (2^d) masks. Each record
requires only modular products, an extended-gcd inverse of an (n)-bit unit,
products of selected explicit (q_j), and one final multiplication. Standard
integer arithmetic therefore gives

\[
\operatorname{poly}(2^d,n+\Lambda_Q)
\]

bit operations, in addition to reading and selecting the retained basis.
The output itself has

\[
O\!\left(2^d(2n+\Lambda_Q)\right)
\]

bits, so this polynomial dependence is also the right output-sensitive
scale.

If (d=(\log n)^{O(1)}), then

\[
2^d=\exp((\log n)^{O(1)}),
\]

which is quasipolynomial in (n). If the old explicit transcript and the
(q_j) data also have quasipolynomial length, polynomial work in all of
these explicit sizes remains quasipolynomial. A parity-kernel basis and the
root image of that basis can be computed by linear algebra and modular
arithmetic without enumerating every vector in the dependency space. Thus
the compact decode claim has the stated cost. It does not imply a compact
enumeration of every dependency.

## 7. What the restricted refinement channel does and does not say

The completion computes canonical integers (s_v). Joint gcd-free
refinement can split old endpoints and these integers into a finer coprime
block system. This can create new *names* that a block grammar accepts as
generators. It does not create new modular information: every (s_v) is a
deterministic inverse of the already public (z_v), and every completion
lift lies on the old section.

The logical channel is therefore

\[
\text{public section values}
\longrightarrow
\text{canonical integer representatives}
\longrightarrow
\text{joint integer refinement}
\longrightarrow
\text{new admissible block names}.
\]

Under the stated interface, the later grammar receives only the final new
block names. If refinement names no new block, or if the grammar rejects all
new blocks, the grammar receives no completion-dependent input and this
channel is inert. If it accepts a new block, its set of admissible generators
can expand even though its underlying public information does not.

No stronger behavioural inertness follows. A grammar allowed to inspect raw
(s_v), raw (P_v), the number of records, index order, or provenance can
change its behaviour without any refinement. Conversely, the algebra does
not prove that refinement must split anything or that a newly named block
must yield a useful later relation.

## 8. Independent (N=77) reconstruction

Take (N=77=7\cdot11), (q=4706), and supplied root (alpha=3). Exact
arithmetic gives

\[
4706=61\cdot77+9=26\cdot181=2\cdot13\cdot181.
\]

Hence (q\equiv9=3^2\pmod{77}), (gcd(q,77)=1), and (q) is not an
integer square. Equivalently, (68^2<4706<69^2). The single parity-one old
record has no nonempty parity dependency.

The inverse calculation is

\[
3\cdot26-77=1,
\]

so (s_1=26). The completion value is

\[
P_1=26^2\cdot4706=3{,}181{,}256\equiv1\pmod{77}.
\]

It is not a square, as also follows from its nonzero parity. The old record
and the new parity-one record do make a mixed dependency:

\[
qP_1=(26q)^2.
\]

Its supplied root product is (3), while its positive exact root satisfies

\[
26q\equiv26\cdot9=234\equiv3\pmod{77}.
\]

Thus its normalized root is (+1), and its standard two-square gcd screens
are (gcd(3-26q,77)=77) and (gcd(3+26q,77)=1). This directly confirms
current decoder inertness for the finite witness.

The elementary pre-refinement screens are also inert:

\[
\begin{array}{c|c}
\text{screen}&\text{value}\\ \hline
\gcd(q,77)&1\\
\gcd(3-1,77),\ \gcd(3+1,77)&1,1\\
\gcd(26,77)&1\\
\gcd(26-1,77),\ \gcd(26+1,77)&1,1\\
\gcd(P_1,77)&1\\
\gcd(P_1-1,77),\ \gcd(P_1+1,77)&77,1
\end{array}
\]

None gives a proper divisor of (77).

Joint refinement is nontrivial because

\[
\gcd(26,4706)=26,
\qquad 4706=26\cdot181,
\qquad \gcd(26,181)=1.
\]

The resulting endpoint screens displayed in the statement are exactly

\[
\gcd(26,77)=1,
\qquad
\gcd(181,77)=1.
\]

They do not factor (77). As noted in the verdict, an additional
post-refinement shifted screen does:

\[
181\equiv27\pmod{77},
\qquad
\gcd(181-1,77)=1,
\qquad
\gcd(181+1,77)=7.
\]

This success occurs only after (181) is admitted through the refined-block
interface, so it strengthens rather than invalidates the claimed later
capability.

### Orders and subgroup expansion

For the old block, (q\equiv9). Modulo (7), (9\equiv2) has order (3).
Modulo (11), (9) has order (5). Hence

\[
\operatorname{ord}_{77}(9)=\operatorname{lcm}(3,5)=15.
\]

For the new block, (26\equiv5\pmod7), and (5^3\equiv-1\pmod7), so its
order modulo (7) is (6). Also (26\equiv4\pmod{11}), whose order is
(5). Therefore

\[
\operatorname{ord}_{77}(26)=\operatorname{lcm}(6,5)=30.
\]

The refined generators still generate the old residue because
(26\cdot181\equiv9\pmod{77}), while the refined group contains the
order-(30) element (26). It therefore strictly contains the old
order-(15) cyclic subgroup. Direct enumeration gives refined subgroup size
(30), though only strict containment is needed.

### The fifteenth-power split

CRT evaluation is immediate:

\[
26^{15}\equiv5^{15}\equiv5^3\equiv-1\equiv6\pmod7,
\]

and

\[
26^{15}\equiv4^{15}\equiv1\pmod{11}.
\]

The unique residue modulo (77) satisfying these two congruences is (34).
Thus

\[
26^{15}\equiv34\pmod{77},
\qquad
\gcd(34-1,77)=\gcd(33,77)=11,
\qquad
\gcd(34+1,77)=\gcd(35,77)=7.
\]

This verifies the finite power test exactly.

## 9. Public-information and all-input scope

The number (26) was public before completion because

\[
26=3^{-1}\bmod77
\]

is obtained by the extended Euclidean algorithm from the supplied root and
the public modulus. Indeed, the same factor-producing residue was already
computable from the supplied root:

\[
3^{15}\equiv34\pmod{77}.
\]

This follows either by direct powering or from (3\cdot26\equiv1) and
(34^2\equiv1\pmod{77}). Therefore the finite example demonstrates a change
in what a *restricted named-block grammar* is allowed to use. It does not
demonstrate an increase in public modular information or an unconditional
need for completion.

The example also supplies no all-input algorithm. In particular, it does
not prove any rule that, for a general composite input,

1. forces joint refinement to name a new block;
2. makes that block admissible to the later grammar;
3. selects the exponent (15), or computes a suitable order within the
   claimed global cost;
4. makes the selected power a non-global square root of (1);
5. forces a later relation or a disagreement with the old section; or
6. bounds the number of feedback rounds.

For this fixed finite instance, a grammar can simply perform the stated
power test (or the simpler shifted (181) screen). Existence of that finite
successful action proves capability on this input only. It gives no
order-selection law and no all-input factoring law. The proposed
second-stage dichotomy in the statement remains a target theorem rather than
a consequence of section completion.
