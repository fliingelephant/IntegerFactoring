# F147 V2 blind reconstruction

## Protocol

I read only `V2_STATEMENT.md` from F147.  Before reading it, I obtained

```text
a65034746ef11b0165ee4c0591c68107997e14d7234df1a4c1a45482b905d87b
```

as its SHA-256 hash.  This matches the required hash.

The reconstruction uses the following meanings that the statement inherits
but does not define locally:

- `[U]_N` is the least nonnegative residue.  Since `U` is a unit, in fact
  `1 <= c < N`.
- `w = iota_N(c)` is a positive representative of `c^{-1} mod N`.
- `n` in the cost section is the bit length of `N`.
- A global normalized root is a root congruent to `+1` or `-1` modulo `N`.

Under these meanings, every claimed theorem reconstructs.  The verdict is
**valid**.  In particular, the strict inequality in (12) is correct.

## 1. Carry bounds and fully wrapped cycles

For every position,

\[
t=\frac{qa^2-c}{N}.
\]

Because `q < N` and `c >= 1`,

\[
0\le t<\frac{qa^2}{N}<a^2\le H^2.
\tag{A}
\]

Now consider an unwrapped edge `q -> r`.  Its edge equation is

\[
qa^2=rT.
\]

The named blocks are pairwise coprime, so `gcd(q,r)=1`.  Hence

\[
r\mid a^2,\qquad r\le a^2\le H^2.
\tag{B}
\]

Let `r -> s` be the next edge of a directed cycle, with anchor `b`.  From
(B) and `b <= H`,

\[
rb^2\le H^4\le N.
\]

The product `rb^2` is a unit modulo `N`, so it cannot equal `N`.  Thus it is
strictly below `N`; the next edge is unwrapped.  Applying (B) again gives
`s <= H^2`.  Induction around the cycle shows that one unwrapped edge forces
all edges of that cycle to be unwrapped.  Therefore a cycle containing a
wrapped edge has no unwrapped edge.

For a wrapped edge, `qa^2=c+tN>N`.  Thus

\[
q>\frac{N}{a^2}\ge\frac{N}{H^2}.
\]

Every cycle vertex is the source of a wrapped edge, so both endpoints of
every cycle edge exceed `N/H^2`.  Equation (A) gives `1 <= t < H^2`.  Also,
for `c=rT` with `c<N` and `r>N/H^2`,

\[
1\le T=\frac cr<\frac Nr<H^2.
\]

This proves all four bounds in (5).

## 2. Unique large target and complete core scan

Suppose one residue `c` had two distinct named divisors `r` and `s`, both
larger than `N/H^2`.  Pairwise coprimality gives `rs | c`, while

\[
rs>\frac{N^2}{H^4}\ge N>c,
\]

a contradiction.  Thus a position has at most one large named target.

Every edge of a cycle containing a wrapped edge has, by Section 1, a large
source, a large target, and a wrapped position.  Testing every explicit
position against every named block therefore retains every such cycle in
`G_H`.  Conversely, every retained core edge has `t < H^2` by (A) and
`T < H^2` by the large-target calculation above.  Uniqueness is per
position; different anchors at one source can still give different edges.

No path choice is needed to perform this scan.  With at most `Q` positions
and `Q` named blocks, at most `Q^2` exact divisibility tests suffice.

## 3. Exact square-class decoder

For an edge `e:q -> r`,

\[
D_e=U_ec_e=(q a_e^2)(rT_e)=qr a_e^2T_e
\]

and `U_e congruent c_e mod N`, so

\[
D_e\equiv c_e^2\pmod N.
\tag{C}
\]

The anchor factor is already a square.  It remains to determine the parity
vector of `qrT_e`.

Complete gcd-free refinement makes the resulting atoms pairwise coprime
and records their multiplicities in every input.  Extract a maximal perfect
power from each atom.  The remaining base of an atom is not a perfect power.
For such a base, at least one rational-prime valuation is odd.  Since the
bases are pairwise coprime, a product of their powers is a square exactly
when every retained base has even total multiplicity.  Thus the formal
binary columns produced by this process give the exact rational
square-class relation without requiring full factorization of the large
center blocks.

There is also a direct treatment of the residuals.  Since `T_e < H^2`, any
composite residual has a prime divisor at most `sqrt(T_e) < H`.  Trial
division through `H`, with repeated division, therefore leaves either `1`
or one prime cofactor.  This fully factors every residual in time polynomial
in the numerical parameter `H`.  Refining the center blocks against these
known residual primes gives the same exact matrix `M_H`.

For `x in ker(M_H)`, let `S` be its selected edge set.  Exactness of the
matrix gives

\[
P_S:=\prod_{e\in S}D_e=Y_S^2
\]

for the positive integer `Y_S`.  From (C),

\[
\rho_S:=Y_S\left(\prod_{e\in S}c_e\right)^{-1},
\qquad
\rho_S^2\equiv1\pmod N.
\tag{D}
\]

Furthermore,

\[
C_eL_e=(c_ew_e)(U_ew_e)=D_ew_e^2.
\]

Thus selecting both actual values for every selected edge gives the exact
square with positive root `Y_S product(w_e)`.  Since
`w_e congruent c_e^{-1} mod N`, its residue is exactly (D).

If `rho_S` is neither `+1` nor `-1`, then
`d=gcd(rho_S-1,N)` is proper.  Indeed, `d=N` would give `rho_S=1`; and
`d=1`, together with `N | (rho_S-1)(rho_S+1)`, would give
`rho_S=-1`.  Hence `1<d<N` in the non-global case.

## 4. Global equality deletion and completeness

Let `K=ker(M_H)`.  Define a binary linear map

\[
A:K\longrightarrow \mathbb F_2^{\{\text{global exact-value classes}\}}
\]

by sending an edge to the equality classes of its two actual values
`C_e,L_e`.  This is the claimed map to the globally deduplicated ledger.

Two facts justify checking only basis preimages.

First, if `A(x)=0`, every selected exact value occurs an even number of
times.  The positive square root after pairing equal values is a product of
actual values.  Each actual value is `1 modulo N` because

\[
C_e=c_ew_e\equiv1,
\qquad
L_e=U_ew_e\equiv c_ew_e\equiv1\pmod N.
\]

Therefore `rho_x=1`.  In particular, a non-global dependency cannot vanish
under exact-value deletion, and the root map factors through `im(A)`.

Second, the root map is multiplicative under binary addition.  For selected
sets `S,T`, with intersection `I`, positivity of the square roots gives

\[
Y_SY_T=Y_{S\mathbin\triangle T}\prod_{e\in I}D_e.
\]

The duplicated denominator is `product_{e in I}(c_e^2)`, and
`D_e/c_e^2 congruent 1 mod N` by (C).  Hence

\[
\rho_{S\mathbin\triangle T}=\rho_S\rho_T\pmod N.
\]

Choose any binary basis of `im(A)` and lift its members to `K`.  If every
lift has root in `{+1,-1}`, every binary combination does too.  Elements in
`ker(A)` have root `+1`, so this covers all of `K`.  Conversely, if any
non-global bridge dependency exists, at least one member of every image
basis must have a non-global lifted root.  The scan is therefore complete
for bridge dependencies supported on `G_H`; it does not enumerate all
kernel vectors.

This completeness is limited exactly as the statement says.  It covers
selections that take the pair `C_e,L_e` for each chosen edge.  It does not
assert that `K` is nonzero, that a dependency survives the global map, or
that its root is non-global.

## 5. Kernel lower bound

Write `v(z)` for the rational-prime valuation parity vector of an integer.
Every edge column satisfies

\[
v(D_e)=v(q_e)+v(r_e)+v(T_e),
\]

because `a_e^2` has zero parity.  All center contributions lie in the span
of the `m` vectors `v(q_1),...,v(q_m)`.  All residual contributions lie in
the span of the `R_H` prime unit vectors for primes that occur in residuals.
Consequently,

\[
\operatorname{rank}(M_H)\le m+R_H
\]

and rank-nullity gives

\[
\dim\ker(M_H)\ge E_H-m-R_H.
\]

Every residual prime is below `H^2`, so `R_H <= pi(H^2)`.  This proves both
inequalities in (9), and `E_H>m+R_H` forces a nonzero conceptual bridge
kernel.  It does not prove either later gate.

## 6. Cost reconstruction

All integers used for core construction have `O(n+log H)` bits.  There are
at most `Q` vertices, positions, core edges, and retained actual values up
to harmless constant factors.  The following operations have polynomial
cost in the parameters stated in (10):

- `Q^2` divisibility tests and the endpoint gcd screens;
- construction and exact sorting of the actual values;
- gcd-free refinement and perfect-power tests on `O(Q)` integers;
- at most `O(QH)` residual trial divisions, up to bit-operation factors;
- binary row reduction for `M_H` and the global equality map;
- exact products and integer square roots whose bit lengths are
  `O(Q(n+log H))`; and
- modular inverses, modular products, and final gcd tests.

Thus the algorithm is polynomial in `Q`, numerical `H`, and `n+log H`.
If `Q` and `H` are each `2^((log n)^O(1))`, any fixed polynomial in these
quantities has the same quasipolynomial form.  Also
`4 log H = (log n)^O(1) = o(n)`, while an `n`-bit `N` has
`log N = Theta(n)`.  Hence `H^4 <= N` holds for all sufficiently large
`n`.  The statement explicitly delegates the finite remainder.

The trial-division claim is polynomial in the value `H`, not merely in its
binary encoding.  This is consistent with (10) and is sufficient for (11).

## 7. Strict cycle-length implication

This claim can be reconstructed directly and does not need an external
cycle lemma.  Index a directed cycle cyclically and write its equations as

\[
q_i a_i^2=q_{i+1}T_i+t_iN.
\]

Put

\[
A=\prod_{i=1}^L a_i,
\qquad
R=\prod_{i=1}^L T_i.
\]

Reducing every edge equation modulo `N`, multiplying, and cancelling the
unit `product(q_i)` gives

\[
A^2\equiv R\pmod N.
\tag{E}
\]

Before reduction, every edge gives
`q_i a_i^2 >= q_{i+1}T_i`, and a wrapped edge makes one inequality strict.
Multiplication and cancellation of the positive integer `product(q_i)`
therefore give

\[
A^2>R.
\tag{F}
\]

Equations (E) and (F) show that `A^2-R` is a positive multiple of `N`.
Since `R>=1`,

\[
A^2\ge R+N>N,
\qquad
A>\sqrt N.
\tag{G}
\]

The strict sign in (G) is essential and justified.  It is stronger than
the non-strict statement `A^2 >= N`; the positive residual product supplies
the extra strictness.

A cycle has anchors larger than one, so its existence implies `H>1` and
`log H>0`.  From `A <= H^L` and (G),

\[
H^L>\sqrt N,
\qquad
L>\frac{\log N}{2\log H}.
\]

For integral `L`, this is exactly

\[
L\ge\left\lfloor\frac{\log N}{2\log H}\right\rfloor+1.
\]

There is no ceiling or equality exception, even when the displayed ratio
is an integer.  The result is only a necessary lower bound.  It supplies no
cycle, no suitable anchor sequence, no square residual product, and no
non-global root.

## Final verdict

**VALID, conditional only on the inherited notation listed in the
protocol.**  The fully wrapped-cycle argument, all center/carry/residual
bounds, per-position target uniqueness, exhaustive frozen-core scan, exact
bridge decoder, global-deletion argument, kernel lower bound, and
quasipolynomial cost claim all follow.  The strict bound

\[
L>\frac{\log N}{2\log H}
\]

also follows exactly as written.
