# F154 V3 hostile re-audit — PASS

## Frozen inputs

I read the complete V3 statement and proof, the V2 hostile re-audit and blind
reconstruction, and the manifest. Before this audit, the V3 hashes matched
the expected values:

- `V3_STATEMENT.md`:
  `7021a1b9c509460606ea1168dc0f782e25cfa1461639ae256f41caf6147c1ef3`;
- `V3_PROOF.md`:
  `b9842a0d05893360af75a4571f46738a69ca9de624ab35b64adc75ae602b13ad`.

I did not modify a frozen input, the manifest, or a durable ledger.

## Verdict

**PASS.** V3 repairs the only material defect found by the V2 blind
reconstruction. It no longer says that the complete finite witness cannot
factor (77). It separates three facts correctly:

1. the current completion decoder and the immediate gcd screens give no
   factor;
2. a restricted named-block grammar can use the newly named block (26) in
   a later power test and factor this one input;
3. this is not new modular information, because (26=3^{-1}\pmod {77}) was
   already publicly computable from the supplied root (3).

The inherited decorated-group algebra, completion distinctness, pure and
mixed root claims, triple identity, and quasipolynomial cost bound remain
correct. The V3 additions make no all-input progress, order-finding,
exponent-selection, or factoring claim.

## 1. The inherited group and section algebra survives

Interpret the second coordinate of (E_Q(N)) as a residue class in
((\mathbb Z/N\mathbb Z)^\times), and use the least positive integer only
when a canonical representative is selected. Coordinatewise multiplication
gives

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2.
\]

The carry factor also obeys

\[
C(v,w)C(v+w,u)=C(w,u)C(v,w+u).
\]

These identities prove closure and associativity of the star law. The law is
commutative, and

\[
(v,z)\star(v,z)=(0,z^2Q(v)^{-1})=(0,1).
\]

Thus (E_Q(N)) is an elementary abelian (2)-group. Actual decorated lifts
of a binary basis of (W) therefore extend by star-products to a public
homomorphism

\[
\widetilde h:W\longrightarrow E_Q(N).
\]

On the stated no-factor branch, the quotient of every retained basis lift is
the corresponding value of the F152 quotient section. Hence the quotient of
(\widetilde h) is that section on all of (W). No factor of (N), CRT
orientation, or hidden character is used.

Writing (\widetilde h(v)=(v,z_v)), the public inverse (s_v=z_v^{-1}\pmod
N) satisfies

\[
P_v=s_v^2Q(v)\equiv1\pmod N.
\]

With supplied root (1), this record has decorated lift

\[
(v,s_v^{-1})=(v,z_v)=\widetilde h(v).
\]

## 2. Distinctness and all dependency-root claims survive

Pairwise coprimality and nonsquareness of the positive integers (q_j) make
their rational squareclasses independent. If (v\ne w), a prime with odd
valuation in a block from their symmetric difference occurs in no other
block. Therefore (Q(v)/Q(w)) is not a rational square.

If (P_v=P_w), then

\[
\frac{Q(v)}{Q(w)}=\left(\frac{s_w}{s_v}\right)^2,
\]

so (v=w). The (2^d) completion values are pairwise distinct. Also
(P_0=1), while (P_v>1) for (v\ne0).

For a subset (S\subseteq W), the rational squareclass of the product is

\[
\left[\prod_{v\in S}P_v\right]
=[Q(\sum_{v\in S}v)].
\]

It is an integer square exactly when the parity sum is zero. In that case,

\[
\mathop{\star}_{v\in S}\widetilde h(v)=\widetilde h(0)=(0,1),
\]

so the normalized root is exactly (+1). This proves the pure-completion
claim, including its sign.

Every old decorated lift with parity (v) differs from
(\widetilde h(v)) by a global sign on the no-factor branch. A zero-parity
mixed dependency therefore leaves only the product of those signs. It can
have root (+1) or (-1), but it cannot add a non-global normalized root.
The supplied-root comparison required before exact-value deletion is enough
to preserve this current root image. V3 correctly keeps occurrence,
presentation, and provenance outside that algebraic deletion claim.

## 3. The triple identity and its sign remain exact

The integer identity

\[
P_vP_wP_{v+w}
=\left(s_vs_ws_{v+w}Q(v+w)C(v,w)\right)^2
\]

follows directly from
(Q(v)Q(w)=Q(v+w)C(v,w)^2). Its displayed positive root reduces modulo
(N) to

\[
\frac{z_{v+w}C(v,w)}{z_vz_w}=1
\]

by the star-homomorphism law. There is no omitted local sign.

## 4. The cost claim remains quasipolynomial at the stated boundary

There are exactly (2^d) indexed completion records. Since (s_v<N<2^n)
and the selected block product (Q(v)) uses at most (\Lambda_Q) bits,

\[
\operatorname{bits}(P_v)\le 2n+\Lambda_Q+O(1).
\]

Enumeration, modular star-products, inversion, exact multiplication,
gcd-free refinement, binary kernel computation, and evaluation of the root
map on a kernel basis are polynomial in the explicit transcript and output
length. They do not require enumeration of all kernel vectors. Thus the
construction remains quasipolynomial when (d=(\log n)^{O(1)}) and the
whole explicit input transcript has quasipolynomial length. No hidden
(N^\alpha) enumeration appears in V3.

## 5. Exact audit of the (N=77) witness

The starting data are valid:

\[
4706=61\cdot77+9=26\cdot181,
\qquad
3^2\equiv4706\pmod {77},
\]

and (4706) is a nonsquare unit modulo (77). The one nonzero parity
column has no parity dependency. The canonical inverse is

\[
s=26,
\qquad
3\cdot26=1+77,
\]

and

\[
P=26^2\cdot4706=3{,}181{,}256\equiv1\pmod {77}.
\]

Joint refinement is a real proper split of the old integer endpoint:

\[
\gcd(26,4706)=26,
\qquad
4706=26\cdot181,
\qquad
\gcd(26,181)=1.
\]

It is not a split of (N):

\[
\gcd(26,77)=\gcd(181,77)=1.
\]

The usual direct canonical-inverse screens also fail:

\[
\gcd(3-26,77)=1,
\qquad
\gcd(3+26,77)=1.
\]

The old residue (4706\equiv9\pmod {77}) has local orders (3) modulo (7)
and (5) modulo (11), so its order is (15). The new block (26) has
local orders (6) and (5), so its order is (30). Since
(9\equiv26^{-2}\pmod {77}),

\[
\langle9\rangle
\subsetneq
\langle9,26\rangle
=\langle26\rangle.
\]

This proves strict growth of the frozen named-block-generated subgroup.

The repaired later test is also exact:

\[
26^{15}\equiv34\pmod {77},
\qquad
34^2\equiv1\pmod {77},
\]

and

\[
\gcd(34-1,77)=11,
\qquad
\gcd(34+1,77)=7.
\]

Thus the later exponent-(15) operation produces a non-global square root
and factors this finite input.

## 6. The interface distinction is now exact

The witness supports only the following narrow operational statement. If a
later grammar takes newly refined integer blocks as its legal generators,
then refinement changes that typed generator ledger from one whose generated
subgroup has order (15) to one whose generated subgroup has order (30).
The grammar can then apply the displayed power test to the newly legal name
(26).

This does not show an information gain for unrestricted public modular
computation. The supplied root (3) was already public, inversion is
polynomial time, and

\[
26=3^{-1}\pmod {77},
\qquad
3^{15}\equiv34\pmod {77}.
\]

Therefore the same modular test was expressible before refinement in an
unrestricted grammar. V3 states this limitation. Its word “capability” must
be read as capability relative to the restricted named-block interface, not
as new factor information or an unconditional algorithmic advantage.

The three stages are consequently distinct:

1. current section completion: all new dependency roots are global;
2. integer refinement: a new legal block name appears, but no factor of
   (N) appears;
3. later restricted-grammar power test: the specially supplied exponent
   (15) yields a factor on this one instance.

## 7. No success law slipped into V3

V3 does not claim that an arbitrary input yields a new block. It does not
give a rule to select exponent (15), compute a useful order, obtain a
non-global half-power, force a later section disagreement, or bound an
iteration. The proposed second-stage dichotomy remains explicitly labeled
as the next theorem to seek, not as a proved result.

The proved result is therefore exactly a general decoder-inert completion
theorem plus one finite and interface-relative refinement/later-power
certificate. It is not a quasipolynomial factoring algorithm.
