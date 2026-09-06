# F152 V2 hostile re-audit — PASS

## Verdict

**PASS.** V2 fully repairs both defects found by the statement-only V1
reconstruction. The exact square-class coordinates are now independent, so
the binary kernel is the complete integer-square dependency kernel. The
exact-value rule now compares supplied roots before deletion and preserves
all occurrence and layer memberships.

I independently rechecked the decorated group, the P66 normalized-root
identity, the split-or-section equivalence in both directions, the online
decoder, abstract splitting, the two-layer disagreement map, the P134
cross-ratio formula, and the `N=2773` certificate. I found no remaining
mathematical or scope error.

This remains a structural decoder theorem. It supplies no relation source,
no disagreement-density theorem, and no factoring algorithm.

## Frozen inputs

I read the complete V2 statement, V2 proof, preserved V1 blind failure,
preserved V1 hostile audit, and current manifest. The requested hashes match
exactly:

- `V2_STATEMENT.md`:
  `3f5b232d6bdeb9ca6a70cecd2bdfc0e1307406de3f84a23c953c59323fcfc78e`;
- `V2_PROOF.md`:
  `46b45cc752f5524670431cd288b5b5baa6cb246d1f536f447e095e85a3824c67`.

I did not modify either frozen V2 input or a durable ledger. No research
computation was needed for this re-audit.

## Both V1 failures are fully repaired

### Exact rational square classes

V1 assumed only pairwise coprimality. Its blind reconstruction gave the
valid counterexample `q_1=4`: the formal parity kernel then misses an exact
integer square.

V2 also requires every positive `q_j` to be a nonsquare. Pairwise coprimality
makes the rational-prime supports disjoint. Every selected nonsquare block
has an odd prime valuation that no other block can cancel. Therefore

\[
v\longmapsto[Q(v)]
\]

is injective. Conversely, a square block puts its basis vector in the
kernel. The new condition is therefore necessary and sufficient under the
stated pairwise-coprime hypothesis.

For every selector `c`, the selected exact product has rational square class
`[Q(A(c))]`. A positive integer is a rational square only if it is an integer
square. Injectivity now gives the full equivalence

\[
A(c)=0
\quad\Longleftrightarrow\quad
\prod_iT_i^{c_i}\text{ is an integer square}.
\]

Thus the `N=15,q_1=4` V1 counterexample is excluded, and the completeness
claim is repaired.

### Supplied-root-aware exact-value deletion

Suppose

\[
T=s^2Q(v)=t^2Q(w)
\]

for two records with the same exact positive value. The exact equality and
the cocycle identity imply that `Q(v+w)` is a rational square. Independence
gives `v=w`, and positivity then gives `s=t`.

The quotient of supplied roots

\[
r=\alpha\beta^{-1}\pmod N
\]

satisfies `r^2=1 mod N`. If `r` is non-global, its two sign gcds factor `N`
before deletion. If `r` is global, the two decorated lifts are equal modulo
`Delta`. Their duplicate-pair dependency has only a global root. Deleting
one copy therefore preserves the useful normalized-root image.

V2 also keeps the union of all occurrence identities and named layer
memberships. If a retained record belongs to both layers, conceptual copies
can differ only by a global sign after this check. Cancelling or identifying
those copies cannot change the useful cross-layer image modulo global sign.
The named parity spans remain available through the retained membership
metadata. V2 also correctly forbids parity-only deletion.

## 1. Decorated group and exact sequence

For bit vectors `v,w`, exact multiplication gives

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2.
\]

This proves closure of the displayed product. Coordinatewise, the bit
identity

\[
ab+(a\mathbin{\mathsf{xor}}b)c
=bc+a(b\mathbin{\mathsf{xor}}c)
\]

is the cocycle law, so the product is associative. Symmetry gives
commutativity. Since `C(v,v)=Q(v)`, every element squares to `(0,1)`.

The projection image is exactly `V_Q(N)`, and its kernel is exactly
`(0,r)` with `r^2=1 mod N`. This proves the short exact sequence. For odd
`N`, every prime-power divisor of `N` assigns a sign to such an `r`. A root
that is not globally `+1` or `-1` has both signs among those components.
Hence both displayed gcds are proper nontrivial divisors.

## 2. Exact P66 normalized-root image

Each relation lift belongs to the group because

\[
(\alpha_i s_i^{-1})^2\equiv Q(v_i)\pmod N.
\]

For `c in ker A`, let

\[
d_j=\sum_i c_i(v_i)_j.
\]

Every `d_j` is even, and the exact positive square root is

\[
R(c)=\left(\prod_i s_i^{c_i}\right)
     \left(\prod_jq_j^{d_j/2}\right).
\]

The accumulated cocycle corrections divide the supplied-root product by
the second factor. The kernel coordinate is therefore

\[
\frac{\prod_i\alpha_i^{c_i}}{R(c)}.
\]

P66 uses the reciprocal convention. The two residues are equal because the
residue squares to one. With the repaired square-class equivalence, no exact
integer-square dependency lies outside `ker A`. Therefore `G(ker A)` is the
complete P66 image, not a restricted formal image.

## 3. Split or section, including the online decoder

If every kernel lift is global, define

\[
h(Ac)=\overline{G(c)}.
\]

Two representations of the same parity vector differ by a kernel word, so
their quotient is in `Delta`. Thus `h` is well-defined. It is a homomorphism,
it projects to the identity, and its generator values determine it uniquely.

Conversely, a section with the prescribed generator values sends every
kernel word to the identity modulo `Delta`. Hence every normalized kernel
root is global. The factor event and the section event are therefore
exclusive and exhaustive.

The online form implements the same proof. Binary elimination either adds a
new parity basis vector or reconstructs the old lift of a dependent vector.
The quotient of the old and new lifts has parity zero. A non-global quotient
factors `N`; a global quotient is agreement in the section. All steps are
polynomial in the explicit transcript length, so an explicit
quasipolynomial transcript has quasipolynomial decoding cost.

## 4. Abstract section boundary

The exact sequence consists of finite-dimensional vector spaces over
`F_2`. Choosing a basis of `V_Q(N)` and one lift of each basis vector gives a
full abstract section. Therefore parity-space structure alone cannot force a
contradiction. The theorem correctly leaves open the source-side task of
forcing incompatible *supplied* lifts.

## 5. P108 two-layer equivalence

Under the two pure no-factor assumptions, each layer gives a section on its
parity span. For `u in W_F intersect W_A`, choose one representation in each
layer. Their combined word is a parity dependency, and its useful root class
is

\[
h_F(u)h_A(u)\in R_N/\{+1,-1\}.
\]

Changing either representation multiplies by a pure-layer global root, so
the class is well-defined. Every cross dependency gives an intersection
vector, and every intersection vector gives a cross dependency. The image is
therefore exactly P108's induced cross-layer normalized-root image. It is
nonzero exactly when the two sections disagree on their intersection.

The supplied-root-aware membership rule also covers a record shared by both
named layers. Selecting both conceptual copies cancels algebraically, up to
the already-checked global sign, and cannot create or remove a useful class.

## 6. P134 specialization

For two records with the same parity vector, `C(v,v)=Q(v)=d`. Their decorated
product has kernel root

\[
r=\frac{\alpha_i\alpha_j}{d s_i s_j}.
\]

Using either congruence `alpha_k^2=d*s_k^2 mod N` gives

\[
r=\frac{\alpha_i s_j}{\alpha_j s_i}\pmod N.
\]

This is the P134 cross-ratio formula. No disjoint-support or source-existence
claim is added here.

## 7. `N=2773` illustration

The exact identities are

\[
5547=3\cdot43^2=1+2\cdot2773,
\]

\[
2126892=3\cdot842^2=1+767\cdot2773.
\]

Both supplied roots are `1`. Their positive joint root is

\[
R=3\cdot43\cdot842=108618\equiv471\pmod {2773}.
\]

Also

\[
471^2-1=80\cdot2773,
\]

and

\[
\gcd(470,2773)=47,
\qquad
\gcd(472,2773)=59.
\]

The decorated group initially gives the reciprocal of the positive root,
but a square root of one equals its reciprocal. The displayed certificate is
therefore exact.

## Scope conclusion

F152 V2 gives a precise public invariant: a new decorated relation extends
the current section, agrees with it, or exposes a factor. It also explains
why parity compression alone is insufficient. It does not prove that any
quasipolynomial source creates a section disagreement. A fresh independent
statement-only reconstruction is still required before promotion.
