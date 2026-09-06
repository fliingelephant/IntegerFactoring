# F275 V2 blind reconstruction from two statements

## Seal and authentication

This reconstruction used exactly these two mathematical inputs:

1. `STATEMENT.md`, observed SHA-256
   `4fa048b441cbb9e6177e3577ebbdd910d5e6555b5ee904ff7a184a2eecbbaa34`.
2. `V2_STATEMENT.md`, observed SHA-256
   `a9bd86b4e4515f133c3c2d7711c530d334749675e0aa75eb8bc7547f3ad0f0da`.

The supplied V2 frozen-root commitment is
`fb8e508c100bc81cf1105ba7be09162df7d73eb7a5ef704b3a687b3567b1a372`.
I did not inspect a manifest to recompute that root, because the blind protocol
forbids reading manifest prose before sealing.

Before this seal, I did not read an F275 proof, audit, self-audit,
provenance file, manifest prose, prior blind attempt, or conversation-derived
mathematical claim. I did not read or modify the prior incomplete
`V2_BLIND_RECONSTRUCTION.md`. I used no ledger, remote machine, or substantive
computation.

## Verdict

**PASS.** The monomial pullback theorem, alternative-root screen, Eulerian
graph relation, even-cycle holonomy and gcd identities, canonical construction
bound, and reduced-complement boundary all follow from the stated hypotheses.
The V2 replacement fixes the only false unqualified row-bound inference: the
bound below `N^2` requires the construction input `d` itself to be canonical.
It does not require, and must not impose, that restriction on the carriers in
the general graph theorem.

The search disposition is also logically consistent with the theorems. It is
a scope judgment, not a success theorem for F270 or for reduced complements.
The statement's historical F268 search result is an input assertion; this
strict blind reconstruction does not independently authenticate that empirical
result.

## 1. Basic lemmas

Throughout, `N>=3` is odd.

### 1.1 Integer which is a rational square

If a positive integer `n` is the square of a rational number, then `n` is an
integer square. Indeed, every prime valuation of a rational square is even.
The valuations of `n` are therefore even, so its positive square root is an
integer.

### 1.2 Multiplication by a unit does not change a gcd with `N`

If `gcd(u,N)=1`, then

\[
 \gcd(uv,N)=\gcd(v,N).
\]

The same conclusion holds when `uv` is replaced by any integer congruent to
it modulo `N`.

### 1.3 Direct screen for two square roots

Suppose `x` and `x'` are units and

\[
 x^2\equiv (x')^2\pmod N.
\]

Set `h=x'x^{-1} mod N`. Then `h^2=1 mod N`. Hence

\[
 N\mid(h-1)(h+1).
\]

Because `N` is odd, no prime divisor of `N` can divide both `h-1` and
`h+1`. Each prime-power divisor of `N` is therefore assigned to one of the
two signed factors. It follows that exactly one of these alternatives occurs:

- `gcd(h-1,N)` or `gcd(h+1,N)` is a proper divisor of `N`;
- `h=1 mod N` or `h=-1 mod N`.

Thus a nonglobal square root of one exposes a factor through the two signed
gcds. For example, modulo `15`, both `1` and `4` square to `1`, but their
ratio `4` is not a global sign and `gcd(4-1,15)=3`. This shows why silently
identifying independently supplied roots up to sign would be invalid.

## 2. Exact inherited monomials

Let the old positive rows and supplied units satisfy

\[
 x_i^2\equiv a_i\pmod N,\qquad \gcd(a_i,N)=1.
\]

For each new row, let

\[
 A_j=s_j^2\prod_i a_i^{M_{ji}},
 \qquad
 X_j\equiv\varepsilon_j s_j\prod_i x_i^{M_{ji}}\pmod N,
\]

where `s_j>0`, `M_{ji}>=0`, and `epsilon_j` is a sign. Since `A_j` is a
unit modulo `N`, so is `s_j`; all inverses below exist.

Take `c in F_2^t` and use its representatives `c_j in {0,1}`. Define

\[
 z_i=\sum_jc_jM_{ji},\qquad d_i=z_i\bmod2,
 \qquad h_i=(z_i-d_i)/2.
\]

All `h_i` are nonnegative integers. Put `S=prod_j s_j^{c_j}` and
`H=prod_i a_i^{h_i}`. If the selected new rows form an exact square,

\[
 R_c^2=\prod_jA_j^{c_j},
\]

then expansion gives

\[
 R_c^2=S^2H^2\prod_i a_i^{d_i}.
\]

Consequently,

\[
 \prod_i a_i^{d_i}=\left(\frac{R_c}{SH}\right)^2.
\]

The left side is a positive integer. Lemma 1.1 makes it an exact integer
square. If its positive root is `r_d`, positivity in the preceding equality
also gives

\[
 R_c=SHr_d.
\]

This proves that `d=M^Tc mod 2` is an old square-class relation.

Modulo `N`, use `x_i^2=a_i` to obtain

\[
 \prod_jX_j^{c_j}
 \equiv
 \left(\prod_j\varepsilon_j^{c_j}\right)
 SH\prod_i x_i^{d_i}.
\]

Since a sign is its own inverse,

\[
 \boxed{
 R_c\left(\prod_jX_j^{c_j}\right)^{-1}
 \equiv
 \left(\prod_j\varepsilon_j^{c_j}\right)
 r_d\left(\prod_ix_i^{d_i}\right)^{-1}
 \pmod N.}
\]

The expression on the right is the old normalized root, changed by at most a
global sign. Thus the transformation cannot create a new useful root class.
It only maps a new relation back to a relation already present in the old
square-class kernel.

If `M^Tc=0`, then every `d_i=0`, the old exact product is `1`, and `r_d=1`.
The normalized root is therefore `+1` or `-1`. This proves the
structural-incidence corollary for pair-product cycles, even-incidence
hypergraph relations, and exact unreduced product circuits with inherited
roots.

### Arbitrarily supplied roots

The inherited expression for row `j` is itself a public square root of
`A_j mod N`. Compare any other supplied root to it before using the pullback.
Lemma 1.3 either returns a proper factor immediately or proves that the new
root differs by one global sign `epsilon_j`. If every row passes this screen
without a factor, the preceding theorem applies with those signs. This is a
complete dichotomy; compatibility is not an extra assumption.

## 3. Graph rows

Let a finite graph have positive carrier `d_v` at each vertex, with
`gcd(d_v,N)=1`. For an edge `e={u,v}`, set

\[
 A_e=d_ud_v,
 \qquad y_e^2\equiv d_ud_v\pmod N,
\]

where `y_e` is a unit.

### 3.1 Every Eulerian edge set is an exact square

For an edge set `F`, direct collection of vertex exponents gives

\[
 \prod_{e\in F}A_e=\prod_v d_v^{\deg_F(v)}.
\]

If every degree is even, then

\[
 \prod_{e\in F}A_e
 =\left(\prod_vd_v^{\deg_F(v)/2}\right)^2.
\]

This proves the general Eulerian relation. It imposes no size bound on any
carrier. It also does not produce a general label-only formula: an Eulerian
set can contain odd cycles or have more complicated cycle structure.

### 3.2 Canonical factor-blind edge construction

For the explicit construction only, require `1<=d<N` and define

\[
 T_y(d)=[y^2d^{-1}]_N.
\]

Because `y` and `d` are units, the canonical representative satisfies
`1<=T_y(d)<N`. The positive row

\[
 A=dT_y(d)
\]

therefore satisfies

\[
 1\le A\le(N-1)^2<N^2.
\]

Also `A=y^2 mod N`, so `y` is its supplied root.

The canonical input hypothesis is necessary for this bound. For example, take
`N=5`, `d=26`, and `y=1`. Then `d` is a unit, `T_y(d)=1`, and the construction
gives `A=26>25`. This invalidates the bound if arbitrary positive carriers are
allowed, while leaving every general graph identity intact. It is exactly the
distinction made by the V2 repair.

## 4. Even-cycle holonomy

Consider a simple cycle of even length `2k`, with edges
`e_i={v_i,v_{i+1}}` and indices modulo `2k`. Define the positive integer
products

\[
 P_0=\prod_{i\text{ even}}y_{e_i},\qquad
 P_1=\prod_{i\text{ odd}}y_{e_i},\qquad X=P_0P_1.
\]

Each vertex has degree two in the cycle, so the exact row product is

\[
 \prod_iA_{e_i}=\prod_i d_{v_i}^2=R^2,
 \qquad R=\prod_i d_{v_i}>0.
\]

The even-position edges form a perfect matching of the cycle vertices. The
odd-position edges form the complementary perfect matching. Squaring the
label products therefore gives

\[
 P_0^2\equiv R\equiv P_1^2\pmod N.
\]

All label products are units. Hence the normalized root is

\[
 \boxed{
 \rho=RX^{-1}
 \equiv P_0^2(P_0P_1)^{-1}
 \equiv P_0P_1^{-1}
 \equiv P_1P_0^{-1}\pmod N.}
\]

For the minus gcd,

\[
 R-X\equiv P_0^2-P_0P_1=P_0(P_0-P_1)\pmod N.
\]

Lemma 1.2 gives

\[
 \boxed{\gcd(R-X,N)=\gcd(P_0-P_1,N).}
\]

Similarly,

\[
 R+X\equiv P_0(P_0+P_1)\pmod N,
\]

so

\[
 \boxed{\gcd(R+X,N)=\gcd(P_0+P_1,N).}
\]

Since `P_0^2=P_1^2 mod N`, Lemma 1.3 applies to `P_0P_1^{-1}`. A
nonglobal cycle root makes one of the two public alternating-label gcds a
proper factor. If neither gcd is proper, the cycle root is global. Thus the
guaranteed even-cycle relation is either directly exposed by its public
labels or is a global decoy.

The parity argument is special to even cycles. On a triangle, for example,
the putative split `P_0=y_0y_2`, `P_1=y_1` gives

\[
 P_0^2\equiv d_0^2d_1d_2,
 \qquad P_1^2\equiv d_1d_2,
\]

so the perfect-matching equality fails in general. The triangle row product
is still a square because its edge set is Eulerian, but this proof supplies no
alternating-label formula. Extra arithmetic square-class relations among the
carriers are likewise outside the graph-incidence proof.

## 5. Unreduced and reduced complement products

Let `1<=a<N` be a unit and let `E` be positive and even. Define

\[
 U_E(a)=[a^E]_{N^2},\qquad Y_E(a)=[a^{E/2}]_N.
\]

Because reduction modulo `N^2` also preserves congruence modulo `N`,

\[
 Y_E(a)^2\equiv U_E(a)\pmod N.
\]

Thus `U_E(a)` is an old row with supplied root `Y_E(a)`.

### 5.1 Unreduced product

The positive integer

\[
 P_E(a)=U_E(a)U_E(N-a)
\]

is an exact monomial in two old rows. Its inherited root is
`Y_E(a)Y_E(N-a)`, so the pullback theorem applies to every exact relation
built from such rows. In particular,

\[
 Y_E(a)Y_E(N-a)
 \equiv (-1)^{E/2}a^E\pmod N.
\]

This differs from `a^E` by only a global sign.

### 5.2 Reduced product and exact principal-lift calculation

The reduced complement is

\[
 C_E(a)=[(a(N-a))^E]_{N^2}.
\]

Since each `U_E` row is congruent to its defining power modulo `N^2`,

\[
 \boxed{C_E(a)=[P_E(a)]_{N^2}.}
\]

Modulo `N`, `N-a=-a`, and `E` is even. Therefore

\[
 C_E(a)\equiv a^{2E}\pmod N,
\]

so `a^E mod N` is a public square root, up to a chosen global sign.

Write Euclidean division as

\[
 a^2=qN+r,qquad 1\le r<N.
\]

The lower bound on `r` follows from `gcd(a,N)=1`. Set

\[
 c=N-r,qquad t=a-q-1.
\]

Since `a<N`, one has `a^2<aN`, hence `q<=a-1` and `t>=0`. Direct
calculation gives

\[
 \boxed{a(N-a)=aN-a^2=c+tN,}
 \qquad \boxed{c=[-a^2]_N.}
\]

This already proves that the row is a deterministic, `a`-correlated lift
above the canonical base `c`. The lift can be written completely explicitly
modulo `N^2`. Let

\[
 b=[c^E]_N,qquad c^E=b+\ell N,
\]

and let `h` be the least residue in `{0,...,N-1}` of
`ell+Etc^{E-1}`. The binomial theorem gives

\[
 (c+tN)^E\equiv c^E+Etc^{E-1}N\pmod{N^2},
\]

and therefore the exact canonical representative is

\[
 \boxed{C_E(a)=b+hN.}
\]

All terms of binomial degree at least two in `tN` vanish modulo `N^2`.
This formula displays the additive lift coefficient that an exact monomial
argument cannot control.

Indeed, for a unique integer `k>=0`,

\[
 P_E(a)=C_E(a)+kN^2.
\]

If `k=0`, reduction is vacuous and `C_E(a)=P_E(a)` is the old exact
monomial; its displayed public root differs from the inherited root by only a
global sign, so the pullback theorem applies. If `k>0`, the additive term
breaks the exact monomial identity. Congruence modulo `N^2` cannot recover
rational-prime incidence of the two operands.

A small exact counterexample shows the loss. Take `N=5`, `a=2`, and `E=2`.
Then

\[
 U_2(2)=4,\qquad U_2(3)=9,\qquad P_2(2)=36,
\]

but

\[
 C_2(2)=[36]_{25}=11.
\]

The reduced row retains neither the rational prime `2` from the first
operand nor the rational prime `3` from the second. This refutes any general
claim that canonical reduction preserves an operand factor. It does not
prove that reduced rows never share factors: coincidences can occur, but the
inherited-monomial theorem predicts neither their rank behavior nor their
root image.

## 6. Search scope

The following conclusions use only the grammar and search facts stated in the
two authenticated inputs.

- Separate scalar banks having private parity pivots does not settle their
  union. A column private inside one bank can occur in another bank. In the
  simplest parity model, each of two one-row banks can contain the same
  nonzero row. Each bank separately has full row rank and a private pivot,
  while their union has a dependency. Thus cross-family sharing can remove a
  separate-bank pivot.
- The proposed F270 operation unites authenticated same-modulus scalar
  families. It is not an exact inherited-monomial transformation of the kind
  proved in Section 2. Theorem A therefore does not close that union search.
- The unreduced complement proposal is closed as an inherited monomial. The
  reduced complement is outside Theorem A, but canonical reduction removes
  the deliberate operand-factor sharing. Without another mechanism that
  predicts repeated pivot loss or a useful normalized root, the proof gives
  no reason to prefer a resource-bearing reduced-section production packet.
- Under the compared proposals in the input, F270 consequently remains the
  justified next search. This is not a proof that F270 will succeed.
- The canonical `t=0` scalar-row grammars stipulated for F268 and the proposed
  F270 can include both operands of `P_E(a)`. They do not thereby include the
  additively reduced row `C_E(a)` as an operation. The reduced section is
  genuinely outside those grammars, not an inherited factor-sharing
  construction hidden inside them.

## 7. Exact boundary of the result

The reconstruction proves no statement beyond these boundaries:

- The canonical condition `1<=d<N` applies only to the explicit construction
  `dT_y(d)`. General graph carriers can be any positive units.
- The graph theorem supplies exact-square relations for Eulerian edge sets,
  but the public alternating-label law is proved only for simple even cycles.
- No carrier-size bound is used in the cycle proof.
- No graph-carrier square-class kernel is classified.
- No canonical-section lower bound is proved.
- No event law, runtime law, factoring algorithm, or F270 result is proved.
- No numerical rational-prime coincidence between independently reduced rows
  is ruled in or ruled out.

These exclusions are necessary. Removing any of them would require a new
argument rather than a reformulation of the inherited-monomial or even-cycle
identities.
