# F154 hostile audit — PASS

## Frozen inputs

I read the complete frozen statement and proof. Their SHA-256 hashes matched
the expected values before this audit:

- `STATEMENT.md`:
  `0b516d4b195a1a90283b6d45bccdeb9df8f23e7f3fca49765d1ec16e250de807`;
- `PROOF.md`:
  `9ed20153e83b3405a0681d822b96d21f186bebd0bae85a72f530741c99db9ca8`.

I also checked the relevant promoted boundaries P66, P128, P129, and P138.
I did not modify a frozen input or a durable ledger. I ran no research
computation.

## Verdict

**PASS.** The section completion is public, its group algebra is exact, all
of its pure dependencies have normalized root `+1`, and every mixed
old/completion dependency has only a global root. The output-size and
decoder bounds are quasipolynomial under the stated polylogarithmic-dimension
and quasipolynomial-transcript hypotheses.

The feedback claim is also valid in its narrow stated sense. Joint integer
refinement can split a previously named composite block, and a later grammar
can use the resulting subblocks separately. This is not new modular
information. It is not a forced refinement law, a subgroup-growth theorem
for unrestricted public residues, an iteration bound, or a factoring
algorithm.

Two scope points are important:

1. The exact completion records are not needed to compute the integers
   `s_v`. They can be enumerated directly from the lifted section. The
   completion records are a decoder-inert packaging of that public inverse
   list.
2. “New blocks” means new named integer blocks. It does not mean factors of
   `N`. Every input block and every `s_v` is a unit modulo `N`.

These points narrow the interpretation. They do not refute a frozen claim.

## 1. The public lift is well-defined

On the no-factor branch of P138, the observed lifts give a unique quotient
section

\[
h:W\longrightarrow E_Q(N)/\Delta.
\]

Choose parity basis vectors `b_1,...,b_d` from the retained relation vectors,
and choose their actual public decorated lifts `e_1,...,e_d`. Since
`E_Q(N)` is an abelian group of exponent two, the formula

\[
\widetilde h\left(\sum_i\lambda_i b_i\right)
=\mathop{\star}_i e_i^{\lambda_i}
\]

defines a homomorphism from the binary vector space `W` into `E_Q(N)`. Its
quotient agrees with `h` on a basis, so it agrees with `h` everywhere. No CRT
sign, prime factor of `N`, or hidden choice is required.

The construction is public. Binary elimination gives the basis and every
basis expansion. The star law uses only multiplication and inversion modulo
`N`. Canonical representatives in `{1,...,N-1}` and their least-positive
inverses are obtained by the Euclidean algorithm.

Writing

\[
\widetilde h(v)=(v,z_v),
\qquad
s_v=\iota_N(z_v),
\]

gives

\[
s_v^2Q(v)\equiv z_v^{-2}Q(v)\equiv1\pmod N.
\]

Therefore `P_v=s_v^2Q(v)` is a valid exact relation with supplied root `1`,
and its decorated lift is `(v,z_v)`. Equation (9) is exact.

## 2. Distinctness and the pure completion kernel are exact

If `P_v=P_w`, then

\[
s_v^2Q(v)=s_w^2Q(w).
\]

Thus `[Q(v)]=[Q(w)]` in the rational squareclass group. The pairwise-coprime
nonsquare hypothesis makes `v -> [Q(v)]` injective, so `v=w`. Hence all
`2^d` indexed completion values are distinct. Also `P_0=1`, while a nonzero
`v` has nontrivial rational squareclass and therefore `P_v>1`.

For a selected subset `S`, the exact product has squareclass

\[
\left[Q\left(\sum_{v\in S}v\right)\right].
\]

It is an integer square exactly when the parity sum is zero. On that branch,
the decorated product is

\[
\mathop{\star}_{v\in S}\widetilde h(v)
=\widetilde h(0)=(0,1).
\]

The second coordinate is the inverse of the usual positive-root ratio, but
it is a square root of one and is therefore self-inverse. The positive-root
normalized value is exactly `+1`, as claimed.

The triple identity is also correct. Exact multiplication gives

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2,
\]

so

\[
P_vP_wP_{v+w}
=\left(s_vs_ws_{v+w}Q(v+w)C(v,w)\right)^2.
\]

Using

\[
z_vz_wC(v,w)^{-1}=z_{v+w}
\]

shows that the displayed positive root is `1 modulo N`. No sign orientation
is missing.

## 3. Mixed old/completion dependencies stay global

Let `g_i` be an old decorated lift with parity vector `v_i`. Since both
`g_i` and `\widetilde h(v_i)` represent the same quotient section, there is
a sign `delta_i in Delta` such that

\[
g_i=\delta_i\star\widetilde h(v_i).
\]

Take any mixed selector whose total parity is zero. Replacing every old lift
by the corresponding value of `\widetilde h` changes the decorated product
only by the product of the global signs `delta_i`. All remaining lifted
section terms multiply to `\widetilde h(0)`. Hence the mixed normalized root
lies in `Delta`.

This proves the exact claimed invariant: completion cannot enlarge the
normalized-root image after quotienting by the two global signs. A mixed
dependency can add the root `-1` when the old exact image previously
contained only `+1`, but it cannot add a useful CRT-sign pattern. The frozen
statement correctly claims only invariance of the useful image.

## 4. Exact-value deletion is safe with the stated metadata rule

Completion values are mutually distinct. Suppose a completion value equals
an old exact value:

\[
P_v=T_i.
\]

Squareclass independence forces the same parity vector. Positivity then
forces the same square multiplier. The quotient of the two supplied roots is
a square root of one modulo `N`.

If this quotient is non-global, the comparison already factors `N`. If it is
global, deleting one algebraic copy preserves the useful root image. The
occurrence, layer, and presentation data must remain attached to the retained
copy, as the proof says. In fact, equality in the fixed `Q(v)` presentation
also forces the same positive `s`, so deletion does not hide a genuinely
different square multiplier.

This rule does not authorize parity-only deletion. Two different exact
values in the same parity fibre can carry the section disagreement sought by
P138.

## 5. The bit bound and quasipolynomial specialization are valid

There are exactly `2^d` completion records. Every `s_v` is below `N`, and

\[
\log_2 Q(v)\le \Lambda_Q.
\]

Thus each `P_v` has at most `2n+Lambda_Q+O(1)` bits. Enumerating all binary
basis combinations, computing modular star-products and inverses, building
the exact presentations, and running gcd-free refinement plus P66 decoding
are polynomial in the total explicit output length.

If `d=(log n)^{O(1)}` and the old explicit transcript has
quasipolynomial total bit length, then both the number of records and their
total length are quasipolynomial. Polynomial work in that length is still
quasipolynomial. The theorem does not claim this when `d` itself is
quasipolynomial.

## 6. Integer refinement can genuinely change the named grammar

The feedback possibility is not only formal. The following proof-only
certificate shows an actual named-block split.

Take

\[
N=77,
\qquad
q_1=4706,
\qquad
T_1=q_1,
\qquad
s_1=1,
\qquad
\alpha_1=3.
\]

Here

\[
4706=61\cdot77+9,
\qquad
\alpha_1^2=9\equiv q_1\pmod{77}.
\]

The block `q_1` is a unit modulo `77` and is not an integer square because
its 2-adic valuation is one. A one-record transcript with nonzero parity has
zero parity kernel, so it is on the no-factor section branch.

Its lifted section value is `z_1=3`. The least positive inverse is

\[
s_{(1)}=26,
\qquad
3\cdot26=1+77.
\]

The completion record is

\[
P_{(1)}=26^2\cdot4706\equiv1\pmod{77}.
\]

Joint refinement is nontrivial because

\[
4706=26\cdot181,
\qquad
\gcd(26,4706)=26.
\]

Thus the old named block `4706` splits into the coprime named blocks `26`
and `181`. If the later source grammar admits decoder blocks as generators,
this can strictly enlarge its named-block-generated modular subgroup. The old
block has residue `9` of order `15` modulo `77`, while the new block `26` has
order `30`: modulo `7` their orders are respectively `3` and `6`, and modulo
`11` both orders are `5`.

This certificate also shows the exact limitation. The residue `26` is the
inverse of the already public residue `3`. An unrestricted modular grammar
therefore had this residue information already. The gain is caused by its
new integer representative and the factorization
`4706=26*181`, not by a larger group of all publicly computable residues.

## 7. What remains unproved

The construction gives no lower bound on how often an `s_v` meets an old
block, no guarantee that a newly named subblock is useful, and no reason that
the next source relation must disagree with the section. It also gives no
potential function that bounds repeated completion and refinement.

Moreover, once `\widetilde h` is enumerated, the algorithm can gcd-refine the
integers `s_v` directly. The exact records `P_v` are useful as a clean
relation-ledger representation, but they are not the cause of the refinement
opportunity.

Therefore the precise remaining theorem in the frozen statement is the
correct boundary. A positive route still needs an all-input quasipolynomial
law that turns a terminal common section into a forced refinement or a later
section disagreement.
