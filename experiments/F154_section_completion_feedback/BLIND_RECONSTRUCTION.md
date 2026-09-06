# Blind reconstruction of F154

## Source boundary

I used only `STATEMENT.md`. Its SHA-256 was verified before reading:

```text
0b516d4b195a1a90283b6d45bccdeb9df8f23e7f3fca49765d1ec16e250de807
```

Throughout, the second coordinate of (E_Q(N)) is a residue class modulo
(N). I take “nonsquare” to mean that each positive integer (q_j) is not
an integer square. This also follows if “nonsquare” means a quadratic
nonresidue modulo (N), since an integer square that is a unit is visibly a
quadratic residue.

## Verdict

The public lift, completion records, distinctness, all-completion inertness,
mixed inertness, triple identity, and stated output-size bound are correct.
The quasipolynomial conclusion is correct when the explicit transcript
length includes the (q_j) list and “decode” means the compact linear-algebra
decode, not enumeration of every dependency.

The claimed feedback possibility is real, but it is only a possibility. No
new block, later disagreement, relation, non-global root, or factor follows
from completion. The sentence saying that completion is “fully inert” when
there is no refinement or when the grammar excludes decoder blocks is too
broad unless the future grammar is explicitly restricted to observe
completion only through newly refined blocks. A grammar can otherwise read
the raw (s_v), the (P_v), their count, or their provenance.

## 1. Algebraic preliminaries

For bits (a,b), (a+b=(a\mathbin\oplus b)+2ab). Coordinatewise, this gives
the exact integer identity

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2. \tag{A}
\]

It follows that the operation in the statement is closed. The cocycle law is
also exact. In one coordinate, both sides have exponent

\[
vw+vu+wu-2vwu.
\]

Thus (E_Q(N)) is an abelian group with identity ((0,1)). Moreover,

\[
(v,z)\star(v,z)=(0,z^2Q(v)^{-1})=(0,1),
\]

so it is an elementary abelian (2)-group. The two elements
(H=\{(0,1),(0,-1)\}) form a subgroup because (N) is odd.

The squareclasses of the (q_j) are independent over (mathbf F_2). To see
this, choose a nonempty set of indices and one selected (j). Since (q_j)
is not a square, some prime has odd valuation in (q_j). Pairwise
coprimality says that this prime occurs in no other (q_k). The selected
product therefore has odd valuation at that prime and is not a square. The
same valuation argument applies to ratios and proves uniqueness of all
(2^m) rational squareclasses represented by the (Q(v)).

## 2. The public actual lift

Let (b_1,\ldots,b_d) be the chosen parity basis, and let (e_i\in E_Q(N))
be its retained actual lifts. Define

\[
\widetilde h\left(\sum_i\alpha_i b_i\right)
=\mathop{\star}_{i:\alpha_i=1}e_i.
\]

This is well-defined because basis coordinates are unique. It is a
homomorphism because (E_Q(N)) is abelian and every element has order two.
Its image in (E_Q(N)/H) agrees with (h) on a basis, hence agrees with
(h) on all of (W). This proves that it is an actual lift, not only a
choice of representatives of the quotient section.

All operations are public. Each required inverse exists because every
(q_j) is a unit. If (z_v^2\equiv Q(v)\pmod N), then (z_v) is also a
unit. It therefore has a unique representative in
(\{1,\ldots,N-1\}) and a public least-positive inverse (s_v).

This argument depends essentially on the exponent-two property. For a
general central extension, arbitrary basis lifts need not define a
homomorphic lift; here they do.

## 3. Completion records and distinctness

By definition, (s_vz_v\equiv1\pmod N), so

\[
P_v=s_v^2Q(v)\equiv z_v^{-2}Q(v)\equiv1\pmod N.
\]

With supplied modular root (1), removing the displayed square part (s_v)
leaves decorated coordinate (s_v^{-1}=z_v). Thus the new record has actual
lift (widetilde h(v)), as claimed.

A homomorphism sends (0) to ((0,1)). Hence (z_0=s_0=1) and (P_0=1).
For (v\ne0), squareclass independence implies (Q(v)>1), so (P_v>1).

Suppose (P_v=P_w). Then

\[
\frac{Q(v)}{Q(w)}=\left(\frac{s_w}{s_v}\right)^2.
\]

The left side is a rational square only when (v=w), by the valuation
argument above. Therefore the (P_v) are pairwise distinct.

The (s_v) themselves need not be distinct or absent from the old state.
For example, take (N=15), (q_1=7), (q_2=13), and let (W) be spanned
by (v=(1,1)). Both (q_j) are coprime nonsquare units, while
(Q(v)=91\equiv1\pmod {15}). The valid lift (z_v=1) gives
(s_v=1=s_0). Thus “new” can only mean newly computed, not a guaranteed
new integer value.

## 4. All-completion dependencies and their signs

For a finite set (S\subseteq W), put

\[
u=\sum_{v\in S}v,\qquad
k_j=\sum_{v\in S}v_j,\qquad
D_S=\prod_jq_j^{(k_j-u_j)/2}.
\]

The exponent in (D_S) is an integer because (u_j\equiv k_j\pmod2).
There are two useful exact identities:

\[
\prod_{v\in S}Q(v)=Q(u)D_S^2, \tag{B}
\]

and, by induction using the cocycle (C),

\[
\mathop{\star}_{v\in S}(v,z_v)
=\left(u,\frac{\prod_{v\in S}z_v}{D_S}\right). \tag{C}
\]

Since (widetilde h) is a homomorphism, the left side of (C) equals
((u,z_u)). In particular, when (u=0),

\[
\prod_{v\in S}z_v\equiv D_S\pmod N. \tag{D}
\]

Now

\[
\prod_{v\in S}P_v
=\left(\prod_{v\in S}s_v\right)^2\prod_jq_j^{k_j}.
\]

Squareclass independence shows that this is an integer square exactly when
every (k_j) is even, which is exactly (u=0). In that case its positive
integer square root is

\[
R_S=\left(\prod_{v\in S}s_v\right)D_S.
\]

Equation (D) and (s_v\equiv z_v^{-1}) give

\[
R_S\equiv\left(\prod z_v^{-1}\right)D_S\equiv1\pmod N.
\]

Every completion record supplies root (1), so their product supplies root
(1). Whether normalization is written as supplied-root divided by the
positive root or conversely, the normalized root is therefore exactly
(+1). This proves (10) and (11), including their sign.

## 5. Mixed old/completion dependencies

Let an old record of parity (a) have actual lift (e). The F152 hypothesis
used in the statement says precisely

\[
eH=h(a).
\]

A completion record of parity (v) has lift (widetilde h(v)), whose coset
is also (h(v)). For any mixed selection with total parity zero, the coset
of the product of all actual lifts is

\[
h\left(\sum a+\sum v\right)=h(0)=H.
\]

The product itself consequently has the form ((0,1)) or ((0,-1)). These
are exactly the two global normalized roots. Thus mixed dependencies cannot
enlarge the useful normalized-root image.

This also gives the exact scope of safe deletion of duplicate exact values.
If two copies of the same unit-valued integer have supplied roots (x) and
(y), then (r=xy^{-1}) satisfies (r^2=1\pmod N). If
(r\not\equiv\pm1\pmod N), comparing the roots already gives a proper
factor through (gcd(r-1,N)) or (gcd(r+1,N)). If
(r\equiv\pm1\pmod N), replacing one record by the other changes any
normalized root only by a global sign. Deletion is therefore safe for the
current useful-root decoder after this comparison.

It is not automatically safe for an arbitrary later feedback grammar that
observes record multiplicity, provenance, or alternative presentations.
For that broader purpose, deletion must retain or merge that metadata. The
minimal accurate wording is “root-aware exact-value deletion preserves the
current normalized-root image after supplied roots are compared.”

## 6. The triple relation

Apply (A) and multiply by (Q(v+w)):

\[
Q(v)Q(w)Q(v+w)
=\bigl(Q(v+w)C(v,w)\bigr)^2.
\]

Multiplication by the three square parts gives exactly

\[
P_vP_wP_{v+w}
=\left(s_vs_ws_{v+w}Q(v+w)C(v,w)\right)^2.
\]

The sign can also be checked directly. Homomorphicity gives

\[
z_vz_wC(v,w)^{-1}\equiv z_{v+w}\pmod N.
\]

For the displayed positive root (R), therefore,

\[
R\equiv
\frac{Q(v+w)C(v,w)}{z_vz_wz_{v+w}}
\equiv
\frac{Q(v+w)C(v,w)}{z_{v+w}^2C(v,w)}
\equiv1\pmod N.
\]

So the formula and the claimed (+1) sign are both correct.

## 7. Size and bit complexity

There are (2^d) vectors in (W), hence exactly (2^d) indexed records.
Distinctness above shows that these are also (2^d) different integer
values.

Since (1\le s_v<N),

\[
\log_2P_v
<2\log_2N+\sum_jv_j\log_2q_j
\le2n+\Lambda_Q.
\]

After the usual one-bit allowance for integer bit length, this is the stated
(2n+\Lambda_Q+O(1)) bound.

Enumerate the (d)-bit basis coordinates. For each vector, compute its
star-product modulo (N), use the extended Euclidean algorithm for (s_v),
and multiply the explicit integers for (Q(v)) and (P_v). These operations
are polynomial in their operand bit lengths. Also (d\le m\le\Lambda_Q),
because every nonsquare positive (q_j) is at least (2). The total cost is
therefore

\[
\operatorname{poly}(2^d,n+\Lambda_Q),
\]

including the output cost.

If (d=(\log n)^{O(1)}), then (2^d=\exp((\log n)^{O(1)})). If the explicit
transcript length includes the binary encodings of all (q_j), its assumed
quasipolynomial bound also bounds (Lambda_Q). Polynomial-time row
reduction and modular arithmetic on the resulting explicit transcript then
remain quasipolynomial. This proves the decode-cost claim in the normal
compact sense of finding a kernel basis and its root image.

Two qualifications are necessary for the literal wording:

1. If the (q_j) list is not counted in “explicit block transcript,” one
   must separately assume
   (Lambda_Q=\exp((\log n)^{O(1)})).
2. Enumerating every dependency is not polynomial in (2^d), because the
   kernel can itself contain exponentially many elements. “Full decode” must
   mean a compact linear-algebra decode, not listing all dependencies.

These are wording requirements, not defects in the construction bound (14).

## 8. What integer refinement can and cannot do

The refinement mechanism is arithmetically possible. Here is a concrete
witness compatible with the displayed setup.

Take (N=15), (q_1=7), (q_2=37), and let (W) be spanned by
(v=(1,1)). Both (q_j) are pairwise-coprime nonsquare units and

\[
Q(v)=259\equiv4\pmod {15}.
\]

Choose the actual basis lift (z_v=2). An old relation with square part
(a=22), exact value (A=22^2\cdot259), and supplied modular root (14)
has this lift because

\[
14^2\equiv A\equiv1\pmod {15},\qquad
14\cdot22^{-1}\equiv2\pmod {15}.
\]

A one-record transcript of nonzero parity has no nonempty parity dependency.
Completion computes (s_v=2^{-1}\equiv8\pmod {15}). If (22) is an old
named endpoint, joint gcd-free refinement sees

\[
\gcd(22,8)=2
\]

and can name the proper integer blocks (2) and (11), which are not among
the old (q)-blocks (7) and (37). This does not factor (15); it only
shows that the integer naming state can become finer.

Nothing forces this event. The earlier example with (s_v=1) already shows
that completion need not supply any useful refinement. Even when a new block
appears, no statement proved above forces a future grammar to accept it, a
later lift to leave the old section, a later relation to close, or a
normalized root to become non-global.

## 9. Exact grammar scope and minimal repair

From the formal assumptions alone, the following literal implication is
false:

> no new refinement, or no admission of decoder blocks, implies that the
> completion is fully inert for every future grammar.

For a counterexample, let a future grammar read a newly materialized (s_v)
directly, use (P_v) as a seed, branch on the number of completion records,
or inspect record provenance. Such a grammar can change even if the named
gcd-free state was already fine enough and even if it never accepts a
decoder block as a generator. This does not contradict root inertness; it
uses a different information channel.

The exact minimal repair is:

> Assume that the future grammar can observe completion data only through
> blocks newly named by the joint gcd-free refinement. Under this interface
> restriction, if refinement names no new block, or if the grammar excludes
> all such blocks as generators, this refinement-mediated feedback channel
> is inert.

Equivalently, replace “the completion is fully inert” with “this
refinement-mediated feedback channel is inert.” No restriction on an
arbitrary future grammar follows from the algebraic theorem.

Under that repair, the feedback claim has the precise form supported by the
proof:

- completion adds no useful root to the current decoder;
- completion can, but need not, refine the named integer state;
- only a later grammar that is permitted to consume the new state can react;
- even such a reaction does not guarantee section disagreement or a factor.

The quoted “precise remaining theorem” is therefore a research target, not
a consequence of F154. As written, terms such as “terminal,” “usable,”
“later,” and “separate public restriction” are not formally defined here,
so the disjunction cannot be proved or refuted from this statement alone.
The established result is one bounded completion round and the two
inertness statements above; there is no iteration or progress theorem.
