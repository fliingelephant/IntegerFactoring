# F271 fresh hostile audit — FAIL as written

## Frozen authentication

I authenticated the complete packet before inspecting any claim. The SHA-256
of `FROZEN.sha256` is

```text
bf3905d8ee94b8c4841eb60e4bcd2790090c30c0b5532c96d2f5f38fea68fb7b
```

Every entry in that freeze list matched both the file and the supplied audit
request:

| File | SHA-256 |
|---|---|
| `MANIFEST.md` | `a0cf849a135252fcd16ccf2774402ff7492be07656186d2b572598d719f1e4b1` |
| `STATEMENT.md` | `19b288038c4f9e339d3f56e51fb1c6d7277fd9e322e486f2339edd0c68bf64ba` |
| `PROOF.md` | `f65e65cd649d3e787fc452abf270142e9c790d424328c52b6e3d678fc7e77b24` |
| `SELF_AUDIT.md` | `210157a033acf41c0a0dd7efdd24efb326553e6a1c862587b0e2bb4d8e6331ea` |
| `PROVENANCE.md` | `d4495b9bcad39897ec12d02d5cb85c34989416776c36a462bf1cd479a3645877` |
| `sanity_check.cpp` | `70bb7398fe927c270f30f3961d72f8af408e845e784b06b3da113d94466a2c19` |

I did not modify a frozen file or a durable ledger.

## Verdict

**FAIL as written, on two local boundary defects.** The saturation theorem,
two-base recursion, global refinement invariant, valuation-mass bound, exact
gcd-call cap, primorial block cap, terminal coprimality identity, square-class
decoder, normalized-root homomorphism, and D05/P106 distinction all survived
hostile reconstruction. In particular, I found no counterexample to the
headline F265 bound of `91,111` gcd calls per bank and `69,973,248` across
768 banks.

The frozen text nevertheless makes an impossible terminal operation-count
claim on a legal all-one input, and its general bit bound does not fix the
encoding size of the supplied residues. Both repairs are local. Neither
changes the F265 arithmetic or the decoder construction.

## 1. Fatal edge-count defect: the legal case `S=0`

The statement explicitly permits an input integer equal to one. Hence, for
example, `m=1` and `a_1=1` is legal. The refinement then emits no block, so
`S=0`.

Proof Section 11 claims that the terminal modulus-product tree uses at most

```text
S-1 multiplications
2S-2 divisions with remainder
```

and inserts the terms `(2S-1)M(2R)` and `(2S-2)Q(2R)` into the displayed
upper bound. At `S=0`, these are respectively `-1`, `-2`, `-M(2R)`, and
`-2Q(2R)`. Zero operations cannot be bounded above by a negative operation
count. Thus the displayed detailed upper bound is not valid on an input that
the frozen statement expressly includes.

The algorithmic repair is immediate: when `S=0`, take `P=1` and accept
terminal coprimality vacuously without building a remainder tree. In the
uniform formulas, replace the affected counts by

```text
max(S-1,0), 2*max(S-1,0), and 2S+max(S-1,0)
```

for the modulus-tree multiplications, remainder divisions, and total
terminal multiplications respectively. Equivalently, state the displayed
tree-cost formula only for `S>=1` and give the empty case separately. The
`S` terminal gcd and exact-division counts are already correct at zero.
This repair preserves both polynomial bounds and the maximum F265 cap.

## 2. Required input-encoding boundary for the bit bound

The input section constrains `v_i` only by congruence and unitness. The
claimed full complexity depends on `R+bitlen(N)` and does not include the
encoded lengths of integer representatives of the `v_i`.

If `v_i` can be an arbitrary integer representative, the bound is false.
Fix `N=3`, `m=1`, and `a_1=1`, and supply

```text
v_1 = 1 + 3*2^L.
```

Then `gcd(v_1,N)=1` and `v_1^2 = 1 (mod N)` for every `L`, while `R=1` and
`bitlen(N)=2` stay fixed. Merely reading `v_1` takes `Theta(L)` bit time.

The intended F265 boundary appears to use canonical residues. The theorem
must say, for example, `0<=v_i<N`, or define each `v_i` as an already stored
residue-class element with an `O(bitlen(N))` representation. With that
condition, all `m` residues occupy `O(m bitlen(N))` bits; since `m<=R`,
their reading and reduction costs fit comfortably inside the stated fourth-
power bound. If arbitrary representatives are intended, their total bit
length must instead enter the complexity parameter.

## 3. Saturation and `TWO_BASE` — pass

For every prime `p`, the saturation valuation is

```text
min(v_p(u), bitlen(u)*v_p(v)).
```

If `p` divides `v`, then `v_p(u)<bitlen(u)`, so saturation takes the complete
`p`-primary part of `u`; otherwise it takes none. Modular reduction before
the gcd does not alter this valuation.

In an equal-support node, division by `d=gcd(x,y)` sends a prime with local
exponents `(r,s)` into exactly one of three disjoint destinations:

- `(x_0,A)` with exponents `(r-s,s)` when `r>s`;
- `(y_0,B)` with exponents `(s-r,r)` when `s>r`; or
- `C` when `r=s`.

The maps `(u,v)->(u+v,v)` and `(u,v)->(v,u+v)` are therefore exact. The two
outer saturations in `TWO_BASE` retain all and only shared primary parts, so
their radicals agree and their gcd is the carried leaf gcd. The two exclusive
quotients are coprime to the shared output and to each other. Equality,
divisibility, prime powers, and mixed composite blocks need no extra branch.

## 4. Global insertion and finite tree capacity — pass

Every replacement with positive old-block coordinate has support inside the
touched block. It remains coprime to every untouched block. The sole
new-only support is returned to the residual with its exact exponent. Thus
the residual loses every primary part supported on that leaf and cannot
touch any replacement from that leaf again during the same row.

For an old exponent vector `w`, the update `u*w+v*e_i` reconstructs every
old row and the absorbed part of the current row. If a left-child gcd is
one during descent, pairwise coprimality of the child products makes the
carried parent gcd exactly the right-child gcd. No omitted right-child gcd is
needed.

The fixed tree cannot overflow. At every intermediate time, not only at the
end, its pairwise-coprime nonunit blocks select distinct rational primes and
their product divides the processed row product. Hence the universal `R`-
leaf cap and the sharper 2,048-leaf F265 cap apply to transient states as
well as final states.

## 5. Valuation charging and exact call counts — pass

For one prime, the equal-support recursion is subtractive Euclid on its two
positive exponents. With `g=gcd(r,s)`, the measure `r+s-2g` decreases by at
least one at every unequal node and ends at the equality node. Thus

```text
F(r,s) <= r+s-2g+1.
```

Across successive rows containing that prime, its exponent in its unique
opaque block is the running gcd `g_t` of the row valuations. Therefore

```text
sum_{t>=2} F(g_{t-1},e_t)
  <= e_1-g_k + sum_{t>=2} e_t
  <  sum_t e_t.
```

Every recursion node contains at least one prime, and a prime occurs only
along its unique path inside each touched recursion tree. Charging nodes to
these paths proves `E<=V`, even when different primes split into different
branches. Each touch consumes at least one previously unconsumed distinct
prime of the current residual, so `T<=sum_{i=2}^m omega(a_i)`. Pairwise
coprimality similarly gives `S<=omega(product_i a_i)`.

For one touch, the two outer saturation gcds plus one saturation and one
ordinary gcd on every nonroot recursion node give exactly `2e` local gcds.
There are at most `T+m` root-loop gcds, at most `DT` descent gcds, and
exactly `S` terminal gcds. The claimed bound

```text
(D+1)T + m + 2E + S
```

is correct. The parallel exact counts `E+T` modular powers, `2T+3E` exact
divisions, and at most `E+T+m` leaf assignments also survive inspection.

## 6. F265 constants — pass

For a positive integer of at most 361 bits,
`sum_p v_p(a)<=360`. Thus `V<=64*360=23,040`. The 58-prime primorial has
368 bits, so one row has at most 57 distinct primes and
`T<=63*57=3,591`.

Any `S` current or final pairwise-coprime nonunit blocks select `S` distinct
primes whose product divides the product of the rows. The latter is below
`2^23104`. The first 1,876 primes have product bit length 23,116, so
`S<=1,875`. Therefore `D=11`, and

```text
12*3591 + 64 + 2*23040 + 1875 = 91111,
91111*768 = 69973248.
```

The comparison with the D08 cap is arithmetically consistent. It is only a
call-count comparison, as the candidate states.

## 7. Terminal identity, parity basis, and roots — pass

For `S>=1`, writing `P=q_j Q_j` gives

```text
(P mod q_j^2)/q_j = Q_j mod q_j.
```

One gcd with `q_j` therefore checks coprimality with the complete
complementary product. All `S` checks equal one exactly when the blocks are
pairwise coprime. A modulus product tree and remainder tree compute the
remainders without a pair scan. At `S=0`, the claim is vacuous as described
in Finding 1.

Because the blocks are pairwise coprime, a selected row product is square
exactly when the aggregate exponent of every nonsquare block is even. Thus
singleton relations are exactly zero signature columns and support-two
relations are exactly equal signature columns. Unit vectors on the zero
class and a star in each nonzero class give an independent basis of the
complete low-support span and give the stated binomial hit counts.

Reducing a full kernel basis modulo the low RREF gives vectors that remain in
the kernel, vanish on the low pivot coordinates, intersect the low span only
at zero, and span the quotient. The retained independent normal forms are
therefore a genuine direct complement. The combined basis has at most `m`
vectors.

For every kernel vector, the displayed block formula is the exact positive
integer square root. The overlap factors in exact roots and supplied modular
roots are the same units, so they cancel and make the normalized-root map a
homomorphism. Testing the low basis and complement therefore classifies the
full image. A non-global involution yields a proper signed gcd for odd `N`,
including nonsquarefree `N`.

## 8. D05 versus P106 — pass

All primes inside one opaque block have the same positive row support. The
D05 saturated private part of an active row is therefore exactly the product
of the blocks supported only on that row, to their stored row exponents. It
is nonsquare exactly when one private nonsquare block has odd row exponent.
Updating positive support after simultaneous deletions reproduces the D05
rounds without new integer gcds.

P106 instead uses active support after reducing exponents modulo two. Every
D05 deletion is a parity-degree-one deletion, but the converse can fail. A
prime with active row valuations `(1,2)` has parity support only on the first
row while its positive support contains both rows. Thus the frozen text
correctly keeps the two peel rules distinct and correctly says P106 can be
strictly stronger.

## 9. Bit complexity after the residue repair — pass

All refinement operands have at most `r` bits and all product-tree operands
have at most `R` bits. The counts above, modular powering by an exponent at
most `r`, dynamic path updates, sparse exponent propagation, exact row
reconstruction, sorting, and the terminal remainder tree fit the stated
`O(R^3 log R)` schoolbook envelope after the `S=0` correction.

There are at most `m` basis roots. Forming each selected row product keeps
exact intermediates at at most `R` bits. Matrix elimination, exact square
roots, modular products, inversions, and signed gcds fit the conservative
`O((R+bitlen(N))^4)` envelope when each supplied residue has the intended
`O(bitlen(N))` representation. The computation is deterministic and uses no
factoring oracle.

## 10. Checker audit and fresh run

I audited the checker before compiling it. Its `Stats` object counts only the
decoder gcds claimed by the local recursion certificate. The carried leaf
gcd, supplied-gcd consistency check, and quadratic output-coprimality oracle
are visibly checker-only and are not included in `Stats`. The sieve bounds,
integer types, fixed recursion depth, and edge inputs are safe.

The run was resource-small: one process, 250,000 pairs below 501, six fixed
edge pairs, and a sieve through 20,000. The host load averages before the run
were `1.71, 2.05, 1.95`; the process finished in about 2.1 seconds with
negligible memory demand. The sandbox denied a process-list query, but this
did not affect the safety estimate for this bounded run.

Using the exact frozen command produced three deprecation warnings in the
installed GMP header and no candidate-source warning. The output was exactly

```text
PASS pairs=250000 max_exhaustive_pair_nodes=11 max_fixed_edge_nodes=360 p58=271 primorial58_bits=368 p1875=16103 primorial1875_bits=23102 p1876=16111 primorial1876_bits=23116 f265_gcd_calls_per_bank=91111 f265_gcd_calls_packet=69973248
```

This confirms the finite arithmetic only. It does not repair either frozen
boundary defect and is not evidence for the unbounded proof.

## Scope conclusion

F271 remains only a factor-free decoder redesign. It proves no elliptic row
source, residual-size theorem, nonzero kernel, non-global image, or factoring
algorithm. After the two local repairs and a new freeze, the mathematical
core is suitable for a fresh hostile re-audit. The current exact version must
not advance to verifier-backed status.
