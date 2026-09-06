# F271 V2 fresh hostile audit — PASS

## Verdict

**PASS.** The V2 additive packet repairs both defects in the frozen V1
hostile audit. I found no new counterexample, missing case, false call cap,
or unsupported asymptotic claim in the imported theorem.

The verdict has the theorem's narrow scope. F271 is a deterministic
factor-free decoder. It does not supply an F265 row source, prove the
64-row residual boundary, force a nonzero square relation, force a
non-global normalized root, or prove integer factoring.

The `91,111` and `69,973,248` caps count scalar gcd calls in refinement plus
terminal block-coprimality verification. The theorem separately states at
most `m` modular inversions and `2m` signed gcds for relation-root
classification. I did not conflate those scopes.

## Frozen authentication

The SHA-256 of the V2 freeze root is

```text
5e396f4e20f54ee37ed70b19ed85a82e483247b10423a7ce58e7081e961c7a15  V2_FROZEN.sha256
```

Every V2 entry matches the supplied audit request and the freeze list:

| File | SHA-256 |
|---|---|
| `V2_MANIFEST.md` | `4057129cdb495656a63c7aa792253edf8c9fd93c476e7309b9787685813c0584` |
| `V2_STATEMENT.md` | `29fd1a79e569c2e4da72d3489e7385de4123e6b299241bfe46defb421c84b82c` |
| `V2_PROOF.md` | `5371d049eecb2451f073edb96d5bf36f99ab7be662fb48c5d8de2b2d93f10b51` |
| `V2_SELF_AUDIT.md` | `3eea92643a38ad3a4893ac9f181a31feba258da82782c53ee61aecdc939e1539` |
| `V2_PROVENANCE.md` | `c795f9959d75e42dcd3928ce49f5294717c5cd6ec695448a3a18e4c2b48ad404` |

The imported V1 root and pinned reports also match the V2 freeze:

| File | SHA-256 |
|---|---|
| `FROZEN.sha256` | `bf3905d8ee94b8c4841eb60e4bcd2790090c30c0b5532c96d2f5f38fea68fb7b` |
| `HOSTILE_AUDIT.md` | `9e8279e7814fe184b2effb950af8be48959d1c415bb7d7e58536fc8f168331be` |
| `BLIND_RECONSTRUCTION.md` | `059b07104df60baa6f4590488a67ccdd20212827907733015c86e0e65ed21313` |

The V1 root in turn authenticates the imported statement, proof,
self-audit, provenance, manifest, and checker at the hashes recorded in
`V2_PROVENANCE.md`. I did not modify a frozen file or a durable ledger.

## 1. Both V1 defects are fixed

### Empty and singleton terminal lists

Put

\[
\delta_S=\max(S-1,0).
\]

For `S=0`, the algorithm takes the empty product `P=1`. Exact row
reconstruction forces every row to equal one. Block coprimality is an empty
conjunction. The terminal tree, divisions, and gcds all have count zero.

For `S=1`, the algorithm squares `q_1` once. It has no internal tree node
and no remainder edge. Since `P=q_1`, it divides
`P mod q_1^2=q_1` by `q_1` once and computes `gcd(q_1,1)` once.

For `S>=2`, a full binary product tree with `S` leaves has `S-1` internal
nodes and `2S-2` edges. The V2 table is therefore exact in all three cases:

\[
\begin{array}{c|c}
\text{operation}&\text{count}\\ \hline
q_j^2\text{ squarings}&S\\
\text{internal modulus multiplications}&\delta_S\\
\text{remainder calls}&2\delta_S\\
\text{final exact divisions}&S\\
\text{terminal gcds}&S.
\end{array}
\]

Thus

\[
[S+\delta_S]M(2R)+2\delta_SQ(2R)+SQ(2r)+SG(r)
\]

is zero at `S=0` and equals the V1 expression at every `S>=1`. No negative
operation count remains.

The later decoder also handles `S=0`. Its parity matrix has no block rows,
all row signatures are zero, every unit vector is a square relation, and
the exact integer root is one. Supplied roots can still expose a non-global
root of one modulo `N`.

### Canonical supplied roots

V2 requires `0<=v_i<N`. Hence each root has at most
`n_N=bitlen(N)` bits. Since every positive row contributes at least one bit,

\[
m\le R,
\qquad
\sum_i\operatorname{bitlen}(v_i)\le mn_N\le Rn_N.
\]

Reading these roots costs `O(R n_N)`, which is inside
`O((R+n_N)^4)`. Every later modular operand is reduced modulo `N` and has
`O(n_N)` bits. The V1 counterexample with an arbitrarily long unreduced
representative is outside the V2 input contract.

## 2. Saturation and two-base coordinates survive attack

For each rational prime `p`, modular reduction before the gcd preserves the
valuation and gives

\[
v_p(\operatorname{Sat}(u;v))
=\min(v_p(u),\operatorname{bitlen}(u)v_p(v)).
\]

If `p` divides `v`, then
`v_p(u)<bitlen(u)`, so the saturation contains the complete `p`-primary
part of `u`. If `p` does not divide `v`, it contains none. This covers
powers of two, prime powers, and mixed composite inputs.

At an equal-support node, let the local prime exponents be `(r,s)`. Division
by `d=gcd(x,y)` sends that prime to exactly one place:

- `(x_0,A)` with exponents `(r-s,s)` if `r>s`;
- `(y_0,B)` with exponents `(s-r,r)` if `s>r`; or
- `C` if `r=s`.

The supports of these three destinations are disjoint. The coordinate maps

\[
(u,v)\mapsto(u+v,v),
\qquad
(u,v)\mapsto(v,u+v)
\]

then reconstruct `x` and `y` exactly. The two outer saturations in
`TWO_BASE` isolate all and only the shared prime supports. Their gcd is the
carried leaf gcd. The two exclusive quotients are coprime to the shared
output and to each other.

No step uses a rational-prime factorization. Equal inputs, divisibility,
prime powers, and blocks with several prime factors use the same proof.

## 3. Global insertion, tree capacity, and telescoping survive attack

Every replacement with positive old-block coordinate has support inside the
touched block. It stays coprime to every untouched block. The new residual
contains exactly the new-only output and is coprime to all blocks produced
by that touch. A prime removed from the residual cannot cause another touch
in the same row.

The exponent update

\[
uw+ve_i
\]

reconstructs every old row and the absorbed part of the current row. During
tree descent, if the left-child gcd is one, pairwise coprimality of the child
products makes the carried parent gcd exactly the right-child gcd. Thus no
right-child gcd is omitted.

The fixed tree cannot overflow. At each completed replacement, the live
blocks are pairwise coprime and nonunit. Their product divides the product
of processed rows and the absorbed part of the current row. It is therefore
less than the complete input-row product. Distinct blocks select distinct
rational primes. The universal `R`-leaf cap and the sharper F265 2,048-leaf
cap apply to intermediate states, not only to the final state.

For one prime, equal-support recursion is subtractive Euclid. With
`g=gcd(r,s)`, the measure `r+s-2g` decreases at every unequal node and ends
at the equality node. Hence

\[
F(r,s)\le r+s-2g+1.
\]

If `e_1,...,e_k` are that prime's positive row valuations and
`g_t=gcd(e_1,...,e_t)`, its exponent inside its unique opaque block before
row `t` is `g_{t-1}`. Therefore

\[
\begin{aligned}
\sum_{t=2}^kF(g_{t-1},e_t)
&\le e_1-g_k+\sum_{t=2}^ke_t\\
&<\sum_{t=1}^ke_t.
\end{aligned}
\]

Every recursion node lies on at least one prime path. Different children
have disjoint support. Charging nodes to prime-path incidences gives
`E<=V`, including nodes where different primes later split into different
branches. A touch consumes at least one previously unconsumed distinct
prime of its row, so `T<=sum_{i=2}^m omega(a_i)`. Pairwise-coprime nonunit
blocks similarly give `S<=omega(product_i a_i)<=I`.

## 4. Gcd and product-tree call counts survive attack

For a touch whose equal-support tree has `e` nodes:

- the two outer saturations use two gcds;
- its `e-1` recursion edges use `e-1` saturation gcds; and
- its `e-1` nonroot nodes use `e-1` ordinary gcds.

The local total is exactly `2e`. Across all rows, root-loop calls are at
most `T+m`, descent uses at most `DT`, and terminal verification uses
exactly `S`. Thus the scoped call bound is

\[
(D+1)T+m+2E+S.
\]

The terminal identity also works before coprimality is known. Write
`P=q_jQ_j`. Then

\[
\frac{P\bmod q_j^2}{q_j}=Q_j\bmod q_j,
\]

so its gcd with `q_j` equals `gcd(q_j,Q_j)`. All `S` gcds equal one exactly
when the blocks are pairwise coprime. A remainder tree does not require its
leaf moduli to be coprime, so this is a genuine independent check and not a
hidden pair scan.

## 5. F265 constants survive attack

For one positive integer with bit length at most 361,

\[
\sum_pv_p(a)\le\lfloor\log_2a\rfloor\le360.
\]

Thus `V<=64*360=23,040`. The exact frozen certificate gives 368 bits for
the 58-prime primorial, so one row has at most 57 distinct prime factors.
The first row touches no old block. Hence

\[
T\le63\cdot57=3,591.
\]

The product of 64 rows is below `2^23104`. The frozen exact primorial
certificate gives

\[
\operatorname{bitlen}(p_1\cdots p_{1875})=23102,
\qquad
\operatorname{bitlen}(p_1\cdots p_{1876})=23116.
\]

If 1,876 pairwise-coprime nonunit blocks existed, choosing one distinct
prime from each would make their product at least the 1,876-prime
primorial, which is at least `2^23115`. This exceeds the row-product bound.
Therefore `S<=1,875`, a 2,048-leaf tree suffices, and `D=11`.

The final arithmetic is

\[
12(3,591)+64+2(23,040)+1,875=91,111,
\]

\[
91,111\cdot768=69,973,248.
\]

These are valid upper bounds for the scoped scalar gcd calls. They are not a
runtime ratio and do not include the separately declared relation-root
inversions and signed gcds.

## 6. Bit complexity survives attack

Every local two-base operand has at most `r` bits. Every dynamic
product-tree value has at most `R` bits. A saturation uses `O(log r)`
multiplications and remainder divisions on `O(r)`-bit values. The forest has
`O(R)` nodes and the dynamic tree has `O(log R)` depth.

There are at most `E+T+m=O(R)` leaf assignments. Exponent-vector work has
`O(m(E+T))` entries of `O(log r)` bits. The incidence count

\[
H=|\{(j,i):e_{ji}>0\}|\le\sum_i\lfloor\log_2a_i\rfloor\le R
\]

bounds exact row reconstruction. The terminal modulus tree has total width
at most `2R`. Sorting uses `O(R log R)` comparisons of `O(r)`-bit values.
With schoolbook arithmetic, all these terms fit
`O(R^3 log R)`.

The parity matrix has at most `R` rows and `R` columns. Its elimination is
polynomial. There are at most `m<=R` basis vectors. Forming each selected
row product keeps exact intermediates at at most `R` bits. Across all basis
vectors there are at most `m^2` row-factor multiplications. Integer square
roots, canonical-root modular products, inversions, and signed gcds all fit
the conservative

\[
O((R+\operatorname{bitlen}N)^4)
\]

bound. This count includes the V2 root-input reading cost. No operand-length
or arithmetic-operation-to-bit-operation gap remains.

## 7. Signatures, roots, and factor classification survive attack

For a selected row set, let `E_j=sum_i c_i e_ji`. Pairwise block
coprimality makes the product square exactly when every nonsquare block has
even `E_j`. A nonsquare block has at least one internal prime with odd
valuation, while no other block contains that prime. One parity row per
nonsquare block is therefore sufficient even when the block is composite.

A singleton is a relation exactly when its signature is zero. A pair is a
relation exactly when its two signatures agree. Unit vectors in the zero
class and a star in each nonzero equal-signature class are independent and
span every support-at-most-two relation. The displayed binomial hit counts
are exact.

Reducing a full kernel basis by the low RREF preserves kernel membership and
clears the low pivot coordinates. The retained normal forms intersect the
low span only at zero and span the quotient. The low basis plus this
complement is therefore a basis of the full kernel with at most `m` vectors.

For a kernel vector, the displayed block formula is the exact positive
integer square root `R(c)`. The supplied product `X(c)` is a unit modulo
`N`. If `c` and `d` overlap on row set `J`, then

\[
R(c\mathbin\oplus d)
=\frac{R(c)R(d)}{\prod_{i\in J}a_i},
\qquad
X(c\mathbin\oplus d)
\equiv\frac{X(c)X(d)}{\prod_{i\in J}v_i^2}\pmod N.
\]

Since `v_i^2` is congruent to `a_i`, the overlap factors cancel in
`rho(c)=R(c)X(c)^{-1}`. Thus `rho` is a homomorphism. Testing one full
kernel basis classifies its complete image.

For odd `N`, a root of one is `+1` or `-1` on each complete prime-power
component. A non-global root has both signs. Consequently both
`gcd(rho-1,N)` and `gcd(rho+1,N)` are nontrivial proper divisors. This also
covers nonsquarefree `N`. Prime and prime-power inputs simply have no
non-global root.

## 8. Peel semantics survive attack

All rational primes inside one block have the same positive row support.
The D05 private primary part of active row `i` is exactly the product of
blocks with positive exponent only on that active row, raised to their
stored row exponents. Pairwise block coprimality makes this product
nonsquare exactly when at least one private nonsquare block has odd row
exponent. Updating active positive supports after simultaneous deletions
reproduces D05 without new integer gcds.

P106 instead uses parity support. A nonsquare block whose parity row has
degree one forces that active coordinate to zero in every kernel vector.
Every D05 deletion meets this condition, but the converse can fail. The
valuation vector `(1,2)` has parity support only on the first row and
positive support on both rows. Thus P106 can be strictly stronger, and V2
correctly keeps the two counters and meanings separate.

## Scope conclusion

F271 V2 is suitable for the next proof-blind reconstruction step. This PASS
does not promote it by itself. It also does not authorize an F265 run or
alter the unresolved source and usefulness obligations outside the decoder.
