# F265-D10 draft algebra amendment — audited boundaries for the one-round mixed kernel

## Status and exact construction

This is an unfrozen theory-only additive draft. It creates no source, runner,
manifest, freeze, compilation, preflight, local execution, remote execution,
discovery result, heldout result, or ledger entry. A hostile theory PASS would
authorize only source drafting.

D10 has exactly these normative inputs:

| Artifact | SHA-256 |
|---|---|
| `D09_DRAFT_ALGEBRA.md` | `93ee6021b969a3624cf499df5e18ea9c262e2a095a6b0634644cc1d69ee8030d` |
| `D09_DRAFT_PREREGISTRATION.md` | `3b499578678a0f71c75f52608e53f2fba7f390fb5a09a95bc20c61d09fe1c0a4` |

Read the authenticated D09 algebra in full. Apply only the replacements and
additions below. Every D09 algebra clause not named here survives literally.
No earlier F265 draft is composed directly with D10. F271 V2 and P222 enter
only through D09's authenticated import table.

## 1. Preserved mathematical core

D10 does not change any of the following:

1. the `U` then `POWER` two-curve source law;
2. factor-first proposal and affine chronology;
3. the positive cubic row
   `a_i=u_i^3+A*u_i+B` with canonical unit supplied root `v_i`;
4. the exactly one-round saturated peel against the original complete bank;
5. the inverse that inserts zero coordinates at deleted rows;
6. the exact F271 V2 gcd-free decoder on a residual of at most 64 rows and
   at most 361 bits per row;
7. signature-class construction of the complete support-at-most-two span;
8. canonical complement construction and normalized-root classification;
9. omission of all-bank coordinate-pair controls; and
10. post-commit relation-local diagnostics.

For completeness, the one-round argument remains as follows. For an original
row set `S`, put

\[
 P_i=\prod_{j\in S\setminus\{i\}}a_j,
 \quad L_i=\operatorname{bitlen}(a_i),
 \quad g_i=\gcd(a_i,P_i^{L_i}\bmod a_i),
 \quad b_i=a_i/g_i.
\]

For every rational prime `ell`,

\[
 v_\ell(g_i)=\min\left(v_\ell(a_i),
 L_i\sum_{j\ne i}v_\ell(a_j)\right).
\]

Thus `b_i` is exactly the product of the complete primary parts of `a_i`
whose primes occur in no other original row. If `b_i` is nonsquare, some
private prime has odd valuation, so coordinate `i` is zero in every square
relation. Deleting every such row simultaneously therefore gives

\[
 \mathcal K(S)\simeq\mathcal K(S_1),
\]

with inverse given by zero insertion. Exact positive roots, supplied modular
roots, and normalized roots are unchanged. This proves preservation, not a
bound on `|S_1|` and not maximal reduction.

## 2. Empty residual and unit-row semantics

This section replaces any implicit D09 empty-core convention.

If the one-round survivor set is empty, define, before serialization,

```text
kernel_dimension       = 0
singleton_count        = 0
support_two_count      = 0
L                      = empty ordered basis
Q                      = empty ordered basis
quotient_defined       = true
all_Q_images_global    = true
decoder_reservation    = 0
decoder_call_count     = 0
```

The empty bank core is eligible after its zero-kernel certificate and all
required records commit. It contributes no factor event and satisfies every
universal statement over `L` and `Q` vacuously.

A surviving input row equal to one is different. It is a legal positive F271
input. The F271 block list can be empty even though the residual row list is
nonempty. In that case F271 V2 uses `P=1`, performs no terminal-tree operation,
and obtains a zero signature for each unit row. Such rows enter the low basis
and their supplied roots are classified normally. D10 must not confuse this
case with an empty one-round residual.

For a one-block terminal list, F271 V2 performs exactly one block squaring,
zero internal modulus-tree multiplications, zero remainder-tree edge
divisions, one final exact division, and one terminal gcd.

## 3. Fatal theorem boundaries

The following are mathematical invariant failures. They abort the split and
permit no finite label:

- a residual admitted to F271 has more than 64 rows;
- an admitted residual row is zero, exceeds 361 bits, has a noncanonical
  supplied residue, fails its square congruence, or has a nonunit supplied
  residue;
- a fixed 2,048-leaf tree overflows;
- one decoder exceeds `T=3,591`, `E=23,040`, `S=1,875`, depth 11, or the
  `91,111` refinement-plus-terminal gcd theorem bound;
- the exact F271 call identity, row reconstruction, terminal coprimality,
  exponent equation, parity equation, kernel equation, exact-root equation,
  or normalized-root equation fails; or
- a supposedly canonical basis, complement, mask embedding, or replay value
  differs from its independently reconstructed value.

A residual larger than 64 rows is still the deliberate D09 resource boundary
and is `RESOURCE_REJECT_RESIDUAL_CORE`; it never enters F271. Exhaustion of a
smaller packet reservation before a decoder begins is also a recoverable
resource rejection. Once a decoder begins under the theorem hypotheses, a
breach of a theorem envelope is not a recoverable resource event.

## 4. Exact nontrivial decoder certificates

Every future D10 source packet must send the following inputs through the
same production decoder, basis, root, factor-journal, and serialization
bodies used by corpus evaluation.

### 4.1 Three-row structural certificate

Use

\[
 N=15,
 \quad(a_0,a_1,a_2)=(31\cdot61,31\cdot151,61\cdot151)
                  =(1891,4681,9211),
\]

and canonical supplied roots

\[
 (v_0,v_1,v_2)=(1,1,4).
\]

All three row residues and all three supplied-root squares are one modulo 15.
The pairwise-coprime nonsquare blocks are `31,61,151`, with parity rows

```text
31: 110
61: 101
151: 011
```

The three signatures are distinct and nonzero. Hence `L` is empty and the
complete kernel and canonical complement are generated by mask `111`. Its
exact positive root is

\[
 R=31\cdot61\cdot151=285541,
\]

its supplied root is `X=4`, and

\[
 \rho=R X^{-1}\bmod15=4.
\]

The minus and plus signed gcds, in that order, are exactly 3 and 5. Both are
recorded as `STRUCTURAL_Q` events. This fixture proves that a unit-mask,
all-square fixture cannot stand in for structural-complement work.

### 4.2 Full-support, near-maximum-width certificate

Let `q_0<...<q_63` be the first 64 rational primes congruent to one modulo 15.
Let `r_0<...<r_63` be the next 64 such primes. Indices on `q` are cyclic.
For each `i`, let `e_i` be the largest positive integer such that

\[
 a_i=q_iq_{i+1}r_i^{2e_i}
\]

has bit length at most 361. Put `v_0=4` and `v_i=1` for `i>0`.

The future source packet must materialize the 128 primes, every `e_i`, every
row, and their SHA-256 digest as immutable fixture bytes. The preflight
independently verifies primality, ordering, congruence, distinctness, maximal
`e_i`, row widths, and root congruences before timing.

The nonsquare parity subsystem on the `q_i` is the binary incidence matrix of
one 64-cycle. The private square powers `r_i^{2e_i}` add no parity equation.
All signatures are distinct and nonzero, so `L` is empty. The kernel and `Q`
are one-dimensional and generated by the all-64-rows mask. Its exact root is

\[
 R=\left(\prod_{i=0}^{63}q_i\right)
   \left(\prod_{i=0}^{63}r_i^{e_i}\right),
\]

which is one modulo 15. The supplied product is 4, so the normalized root is
again 4 and the signed gcds are exactly 3 and 5. This fixture executes a
support-64 structural root whose selected product is near the registered
23,104-bit row-total boundary.

### 4.3 Empty and singleton block cases

The one-round input rows `(31,61)` with `N=15` and supplied roots `(1,1)`
are both deleted in the same round. They certify the exact empty-core values
in Section 2.

The F271 input `m=1,a_0=1,N=15,v_0=1` reaches a nonempty residual with
`S=0`, `L={1}`, and `Q` empty. The input `m=1,a_0=31,N=15,v_0=1` reaches
`S=1` and a zero kernel. These cases exercise both repaired F271 terminal
boundaries.

## 5. Pair-control and finite-scope boundary

D10 retains D09's zero count for all-bank unordered coordinate, signed-
coordinate, chord, support-two gcd, quotient, and square-test loops. Signature
classes still give the complete support-at-most-two square-relation span.

Consequently, `decoder_strict_structural_hit` means strict only relative to
generation-stage factors and the complete low-support image. It does not mean
that the same bank would survive an omitted coordinate-pair control menu. A
result may not drop the word `decoder` or claim novelty beyond that definition.

D10 remains a finite experiment over the authenticated reused F268 corpus.
It proves no source law, residual-size law, success probability, all-input
factorization theorem, or asymptotic running time.
