# F154 V2 hostile re-audit — PASS

## Frozen inputs

I read the complete V2 statement and proof, the frozen V1 hostile audit and
blind reconstruction, and the manifest. Before this audit, the two V2 hashes
matched the expected values:

- `V2_STATEMENT.md`:
  `8c75dd708a4c7bbd99e593e92474b266fb38c2b9ff8c07b3f17d0645583566c6`;
- `V2_PROOF.md`:
  `08ef5ebd3428d93a8c6b0203667b3387e0d3367ceb8e2c182968c0a84e4b39b1`.

I did not modify a frozen input, the manifest, or a durable ledger.

## Verdict

**PASS.** The V1 future-grammar overclaim is repaired. V2 proves inertness
only for the current squareclass decoder and for one explicitly restricted
refinement-mediated generator channel. It makes no claim that arbitrary
future use of raw completion values, counts, presentations, or provenance is
inert.

The group algebra, exact-value distinctness, pure and mixed dependency-root
claims, supplied-root-aware deletion, triple identity, output-size bound,
and the `N=77` refinement and subgroup certificate are all correct. V2 adds
one valid finite certificate and sharper scope language. It adds no forced
progress claim, all-input source law, iteration bound, or factoring
algorithm.

## 1. The public lift exists and uses no hidden factor data

The identity

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2
\]

makes the stated star law closed. Its cocycle is associative and symmetric,
and

\[
(v,z)\star(v,z)=(0,z^2Q(v)^{-1})=(0,1).
\]

Thus `E_Q(N)` is an abelian group of exponent two. This exponent-two fact is
essential: actual lifts of a binary basis extend by star-products to a
homomorphism.

On the no-factor branch of F152 V2, every retained basis lift has quotient
equal to the unique section value on that basis vector. Therefore

\[
\widetilde h\!\left(\sum_i\lambda_i b_i\right)
=\mathop{\star}_i e_i^{\lambda_i}
\]

is a public actual lift of the quotient section on all of `W`. Binary basis
coordinates, modular multiplication, and modular inversion are enough. No
CRT orientation or factor of `N` is used.

Writing `\widetilde h(v)=(v,z_v)` gives a unit `z_v` with
`z_v^2=Q(v) mod N`. Its least-positive inverse `s_v` is public and satisfies

\[
P_v=s_v^2Q(v)\equiv z_v^{-2}Q(v)\equiv1\pmod N.
\]

With supplied root `1`, the decorated lift of this record is
`(v,s_v^{-1})=(v,z_v)`, exactly as claimed.

## 2. Distinctness uses the stated integer-square hypothesis correctly

Pairwise coprimality and the requirement that every positive integer `q_j`
is not an integer square make their rational squareclasses independent.
For each selected `q_j`, one of its prime valuations is odd, and that prime
does not occur in another block.

If `P_v=P_w`, then

\[
\frac{Q(v)}{Q(w)}=\left(\frac{s_w}{s_v}\right)^2.
\]

Squareclass independence forces `v=w`. Hence all `2^d` completion values are
pairwise distinct. The identity vector has `z_0=s_0=P_0=1`. For `v` nonzero,
`Q(v)` has nontrivial rational squareclass, so `P_v` cannot be `1` and is
positive. The claims `P_0=1` and `P_v>1` are exact.

V2 also correctly avoids saying that the integers `s_v` themselves are
distinct or absent from the old state.

## 3. Every pure completion dependency has root exactly `+1`

For a selector `S`, let `u=sum_{v in S} v`. The selected product has rational
squareclass `[Q(u)]`. Independence gives

\[
\prod_{v\in S}P_v\text{ is an integer square}
\quad\Longleftrightarrow\quad u=0.
\]

On this branch, homomorphicity gives

\[
\mathop{\star}_{v\in S}\widetilde h(v)
=\widetilde h(0)=(0,1).
\]

The second coordinate is the normalized root. If the convention uses its
inverse, the value is unchanged because every square root of one is
self-inverse. Thus the normalized root is exactly `+1`, not only a global
sign. This proves both directions of (10) and the sign in (11).

## 4. Mixed dependencies cannot add a useful root

For an old lift `g_i` of parity `v_i`, the section theorem gives

\[
g_i=\delta_i\star\widetilde h(v_i),
\qquad \delta_i\in\{(0,1),(0,-1)\}.
\]

In a mixed dependency of total parity zero, the section terms multiply to
`\widetilde h(0)`. Only the product of the global signs remains. Therefore
every mixed normalized root is `+1` or `-1`. Adding the completion cannot
enlarge the useful root image modulo global sign. It can add a global `-1`
where only `+1` was previously represented, but V2 does not claim otherwise.

## 5. Root-aware exact-value deletion is safe at the claimed interface

Suppose an old value equals a completion value. F152 squareclass
independence forces the same parity vector and the same positive square
multiplier. The quotient of the supplied roots is therefore a square root
of one modulo `N`.

- A non-global quotient immediately exposes a factor.
- A global quotient changes any dependency root only by a global sign.

After this comparison, deleting one algebraic copy preserves the current
useful normalized-root image. V2 also requires retention of occurrence,
presentation, and provenance metadata when a later grammar can observe it.
It does not authorize parity-only deletion or deletion of feedback metadata.

## 6. The triple square and its sign are exact

Exact multiplication gives

\[
P_vP_wP_{v+w}
=\left(s_vs_ws_{v+w}Q(v+w)C(v,w)\right)^2.
\]

The star-homomorphism law is

\[
z_vz_wC(v,w)^{-1}=z_{v+w}.
\]

After substituting `s_x=z_x^{-1}` and `Q(v+w)=z_{v+w}^2 mod N`, the displayed
positive root reduces to

\[
\frac{z_{v+w}C(v,w)}{z_vz_w}=1\pmod N.
\]

There is no missing CRT sign. Degenerate choices such as `v=w` still give a
valid integer-square identity; distinct nonzero pairs give the usual
three-record binary dependency.

## 7. The quasipolynomial cost claim is correctly qualified

There are exactly `2^d` indexed records. Since `s_v<N` and
`log_2 Q(v)<=Lambda_Q`, each `P_v` has at most
`2n+Lambda_Q+O(1)` bits. Also `d<=m<=Lambda_Q`, so basis coordinates and the
block list fit within the stated input-size parameter.

Enumeration, modular star-products, inverses, exact products, gcd-free
refinement, binary elimination, and evaluation of the normalized-root image
on a kernel basis are polynomial in the explicit input and output length.
They therefore cost

\[
\operatorname{poly}(2^d,n+\Lambda_Q).
\]

If `d=(log n)^{O(1)}` and the full explicit transcript, including the `q_j`
encodings, has quasipolynomial length, this remains quasipolynomial. V2 now
says “compact full decode”: it computes a kernel basis and its image and does
not enumerate every kernel element. This closes both complexity ambiguities
identified in the V1 blind reconstruction.

## 8. The `N=77` certificate is exact

For

\[
N=77,\qquad q_1=4706,\qquad \alpha_1=3,
\]

the checks are

\[
4706=61\cdot77+9,\qquad 3^2\equiv9\pmod{77},
\]

and `gcd(4706,77)=1`. The integer `4706` is nonsquare because its 2-adic
valuation is one. A one-column nonzero parity matrix has zero kernel, so the
old transcript is on the no-factor section branch.

The least-positive inverse is

\[
s_{(1)}=26,\qquad 3\cdot26=1+77.
\]

Also

\[
4706=26\cdot181,\qquad \gcd(26,181)=1,
\]

so joint refinement really replaces one old named block with two proper
coprime named blocks.

The old residue is `9`. It has local orders `3` modulo `7` and `5` modulo
`11`, hence order `15` modulo `77`. The new residue `26` has local orders `6`
and `5`, hence order `30`. Moreover, the congruences

\[
k\equiv4\pmod6,\qquad k\equiv3\pmod5
\]

give `k=28 mod 30`, so `26^28=9 mod 77`. Therefore the refined subgroup is
in fact `\langle26\rangle`, of order `30`, and strictly contains the old
subgroup of order `15`.

This is only growth relative to the named-block generator ledger. The
residue `26` was already the public inverse of `3`. The split is a
factorization of the old integer block, not a factorization of `77`. V2 and
the manifest state these limitations correctly.

## 9. The interface repair is complete at its stated narrow scope

V1 said that the completion was fully inert if no refinement occurred or if
decoder blocks were not admitted. That could fail for a grammar that reads
raw `s_v`, raw `P_v`, record count, or provenance.

V2 explicitly excludes those observations from its theorem. It considers
only the channel in which joint gcd-free refinement names blocks and a later
source grammar admits those blocks as integer generators. Under this exact
interface:

- no newly named block means no input to the channel;
- exclusion of all newly named blocks as generators disables the channel;
- admission of a new block can change the named generator state.

This does not say that a grammar permitted to inspect a new block as general
metadata must be unchanged. Such behavior is outside the claimed
generator-admission channel, just as direct inspection of raw completion
data is outside it. With this narrow reading, there is no residual V1
overclaim.

## 10. What still does not follow

The completion values can be made directly from the public inverse list.
They are a decoder-inert ledger for that list, not the cause of the gcd
opportunity. Nothing here proves that refinement occurs on another input,
that a refined block is useful, that a later relation violates the section,
or that repeated completion terminates. The “precise remaining theorem” is
a research target, not a result of F154.
