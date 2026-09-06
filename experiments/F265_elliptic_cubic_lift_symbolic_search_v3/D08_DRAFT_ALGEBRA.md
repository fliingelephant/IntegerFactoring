# F265-D08 draft algebra amendment: peeled elliptic cubic-row kernel

## Status and exact composition

This is an unfrozen theory-only amendment. It has not received a hostile
audit. There is no D08 source, runner, manifest, compilation, preflight,
freeze, local execution, remote execution, or cohort result.

D08 imports exactly these immutable algebra drafts:

| imported artifact | SHA-256 |
|---|---|
| `D05_DRAFT_ALGEBRA.md` | `e3cbefeb597f263501d327f15f9dd4c7b78ee37d37178135ab1c0a5ff73e9fd3` |
| `D06_DRAFT_ALGEBRA.md` | `e79ea109a9cd8141dd27c4fc99cc7ec2957c454619b0e015802ab4eff5c45f74` |
| `D07_DRAFT_ALGEBRA.md` | `fbc4831cb4f11f849a779bf165cbedf2e6a3e8140228ba40b0d01ec103a2abbf` |

The immediate D07 draft received a conversation-only hostile `REVISE`.
There is no audit artifact and therefore no audit hash. Its mathematical
core passed; its four blockers were curve-acceptance composition, the deleted
`T_square64` definition, incomplete byte metadata, and the invalid sampled
`cpp_int` remainder dominance claim. D08 changes only those boundaries.

The normative D08 algebra starts with the exact D07 composite contract and
adds only the fixed-width P66 gcd theorem below. The mathematical claims in
D05 Algebra Sections 1 through 5, the D06 sticky-evidence amendment, and the
D07 closed factor boundary survive literally. There is no token rebinding or
unnamed import.

## 1. Fixed-width binary gcd theorem

Every value compared by the residual P66 refinement or terminal
pairwise-coprimality loops is a positive divisor of an admitted row value.
The row cap is 361 bits. Thus each production operand is positive and
strictly less than `2^361`. The primitive below is total on the slightly
larger boundary domain `0<=a,b<2^361`; zero is retained only to make the
fixed transition and its self-test unambiguous.

For positive `a,b<2^361`, write

\[
 a=2^\alpha u,\qquad b=2^\beta v,
\]

where `u,v` are odd. Then

\[
 \gcd(a,b)=2^{\min(\alpha,\beta)}\gcd(u,v).
\]

If `u>v`, put

\[
 u'={u-v\over 2^{v_2(u-v)}}.
\]

Then `u'` is positive and odd,

\[
 \gcd(u,v)=\gcd(u',v),
 \qquad u'<u/2,
\]

so `bitlen(u')<bitlen(u)`. The symmetric statement holds when `v>u`.
Consequently every unequal binary-gcd update lowers

\[
 \operatorname{bitlen}(u)+\operatorname{bitlen}(v)
\]

by at least one. Its initial value is at most 722 and its value is at least
two. Equality is therefore reached after at most 720 unequal updates. The
registered 722 rounds are deliberately loose and include the terminal
transition and an inactive suffix.

Here is the exact fixed-round state transition. Six limbs represent one
unsigned integer modulo `2^384`. `ctz6(0)=384`; otherwise `ctz6(x)` is the
ordinary trailing-zero count. `rshift6(x,s)` is defined for every
`0<=s<=384`, with `rshift6(x,384)=0`. Both functions scan all six input
limbs and mask-select every fixed limb-offset candidate.

At initialization compute zero masks `za=[a=0]`, `zb=[b=0]` and save
`zero_answer=a|b`. On the nonzero lane put

\[
 k=\min(\operatorname{ctz6}(a),\operatorname{ctz6}(b)),\quad
 u=a\mathbin{\mathrm{rshift6}}\operatorname{ctz6}(a),\quad
 v=b\mathbin{\mathrm{rshift6}}\operatorname{ctz6}(b).
\]

When either input is zero, mask-select the dummy state `u=v=1,k=0`. Thus
`u,v` are positive odd integers on every lane entering the round loop.

One round computes, unconditionally, both six-limb unsigned differences

\[
 d_{uv}=u-v\pmod {2^{384}},\qquad
 d_{vu}=v-u\pmod {2^{384}},
\]

the full-width comparison masks `gt=[u>v]`, `lt=[v>u]`, and the selected
nonnegative difference

\[
 d=\operatorname{select}(gt,d_{uv},d_{vu}).
\]

When `u=v`, both differences and `d` are zero. Compute in all cases

\[
 h=\operatorname{rshift6}(d,\operatorname{ctz6}(d)).
\]

Then mask-select

\[
 u'=\operatorname{select}(gt,h,u),\qquad
 v'=\operatorname{select}(lt,h,v).
\]

There is no separate active flag. At equality, `gt=lt=0`, so the state is
unchanged even though the zero difference follows the fully defined
`ctz6(0)` and `rshift6(0,384)` path. After an unequal update, `h` is exactly
the positive odd quotient in the proof above. Thus the invariant is:

- `u,v` stay positive and odd;
- `gcd(u,v)` is unchanged; and
- equality is absorbing.

Induction and the decreasing measure prove that after 722 applications the
two state values on a nonzero-input lane are equal to the odd gcd. A
zero-input dummy lane remains at `(1,1)`. The provisional answer is
`lshift6(u,k)`. If an original input was zero, a full-width mask instead
selects `zero_answer`; hence the exact endpoint laws are

\[
 \gcd(a,0)=a,\qquad \gcd(0,b)=b,\qquad \gcd(0,0)=0.
\]

For two nonzero inputs, `2^k u` is their mathematical gcd and is at most
`min(a,b)<2^361`. Therefore the restoring left shift cannot overflow the
six-limb representation and its upper 23 padding bits are zero. Both
subtractions use unsigned limb arithmetic: the selected difference never
underflows; the unselected modular wrap is computed but cannot enter the
state. Every selected unequal-state right shift decreases a represented
value. These facts close
the zero, equal, even-input, and six-limb overflow endpoints.

D08 uses this fact to require one production primitive,
`p66_gcd361_fixed`, with this exact abstract behavior:

1. represent each operand as six little-endian `uint64_t` limbs and assert
   outside the fixed body that the upper 23 padding bits are zero;
2. execute the initialization above, including both total zero-input lanes;
3. execute exactly 722 copies of the displayed transition;
4. in every round, scan all six limbs, compute both six-limb differences,
   compute a six-limb trailing-zero count and shift, and update through word
   masks;
5. after equality, keep the mathematical state unchanged but execute the
   same limb operations in every remaining round; and
6. execute the restoring shift, zero-lane selection, and six-limb return.

There is no early exit, `cpp_int` operation, allocation, integer division,
integer remainder, data-dependent loop bound, data-dependent memory address,
or data-dependent conditional branch inside the primitive. A fixed shift
evaluates every possible six-limb word offset and mask-selects one; a
128-bit two-limb window performs the remaining shift by 0 through 63 bits.
The only conditional branch in the emitted primitive is the fixed 722-round
loop backedge. Input data select values only through full-width masks.

`ctz6` computes a zero-word flag and a defined `0,...,64` count for every
limb; it never applies a language builtin outside its nonzero domain.
`lshift6(x,s)` is likewise total for `0<=s<=384`, with
`lshift6(x,384)=0` in the six-limb representation.
`rshift6` and `lshift6` evaluate each of the seven possible whole-word
offsets at fixed source addresses, use a 128-bit two-limb window for the
0-through-63 residual shift, and mask-select the result. No shift expression
uses a count equal to its language type width.

The proof above establishes the returned value for the complete boundary
domain. The fixed representation and fixed instruction schedule establish
the resource property that D07's
sampled `cpp_int` remainder rate lacked. No finite list of operand samples is
claimed to dominate arbitrary `cpp_int` division behavior.

The primitive is used only at the two closed P66 gcd call sites:

- a block-pair comparison in the refinement loop; and
- a final block-pair coprimality comparison.

All other public, peel, relation, and diagnostic gcds retain their surviving
D05/D06/D07 definitions. A future source audit must inspect the emitted
object code for the fixed control-flow property before any timed preflight.

## 2. Unchanged mathematical scope

The saturated private-primary theorem, simultaneous fixed-point peel,
kernel isomorphism, support-at-most-two criterion, normalized-root
homomorphism, and global-low-image quotient logic are unchanged.

D08 proves no elliptic source theorem. It does not prove that a bank has a
private pivot, that a residual core is small, that a useful relation occurs,
or that any finite frequency extends to unbounded inputs. The peel remains a
source-agnostic decoder optimization and a finite-source opening.

## 3. Authorization boundary

A fresh no-context hostile theory audit must reconstruct the three imported
algebra drafts and this amendment. A pass authorizes only preparation of a
standalone resolved theory contract. It does not authorize source, freezing,
compilation, preflight, or execution.
