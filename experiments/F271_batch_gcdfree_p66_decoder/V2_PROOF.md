# F271 V2 proof — additive boundary repair

## Status and imported proof

The mathematical base is the complete frozen V1 proof

```text
PROOF.md
SHA-256 f65e65cd649d3e787fc452abf270142e9c790d424328c52b6e3d678fc7e77b24
```

V2 changes only the terminal-tree operation count at an empty block list and
the encoding premise for supplied modular roots. Every other V1 proof is
incorporated unchanged by its hash.

## 1. Exact terminal-tree cases

Let

\[
 \delta_S=\max(S-1,0).
\]

### Case `S=0`

There is no modulus `q_j^2` and no terminal leaf. Take the empty block
product to be `P=1`. The terminal coprimality predicate is an empty
conjunction and is true. The terminal phase uses exactly

\[
 0\text{ squarings},\quad
 0\text{ product-tree multiplications},\quad
 0\text{ remainder divisions},\quad
 0\text{ final exact divisions},\quad
 0\text{ gcds}.
\]

This is the case reached, for example, when every legal input row equals
one.

### Case `S=1`

Square the sole block once to obtain the leaf modulus `q_1^2`. There is no
internal product-tree node and no remainder-tree edge. Since `P=q_1`, the
final numerator is `P mod q_1^2=q_1`; one exact division gives one, and one
gcd verifies the vacuous pairwise condition. The exact counts are

\[
 1\text{ squaring},\quad
 0\text{ product-tree multiplications},\quad
 0\text{ remainder divisions},\quad
 1\text{ final exact division},\quad
 1\text{ gcd}.
\]

### Case `S>=2`

The V1 construction applies literally. Squaring the `S` blocks produces the
leaf moduli. A binary product tree with `S` leaves has `S-1` internal nodes,
and its remainder tree has `2S-2` parent-to-child edges. The final step has
`S` exact divisions and `S` gcds.

### Uniform exact upper-bound expression

All three cases are represented without a negative coefficient by

\[
 \begin{array}{c|c}
 \text{operation}&\text{count}\ \\ \hline
 q_j^2\text{ squarings}&S\\
 \text{modulus-tree multiplications}&\delta_S\\
 \text{remainder divisions}&2\delta_S\\
 \text{final exact divisions}&S\\
 \text{terminal gcds}&S.
 \end{array}
\]

Therefore replace the terminal part of the V1 Section 11 bit-operation
display

```text
(2S-1)M(2R) + (2S-2)Q(2R) + S Q(2r) + S G(r)
```

by

\[
 \boxed{
 [S+\delta_S]M(2R)
 +2\delta_S Q(2R)
 +S Q(2r)
 +S G(r).}
\]

For `S>=1`, this is exactly the V1 expression. For `S=0`, every coefficient
is zero. Hence the detailed bound now covers every legal input. Since
`delta_S<=S`, the repaired terms remain `O(S(M(2R)+Q(2R)+Q(2r)+G(r)))`
and do not change the `O(R^3 log R)` schoolbook bound.

The scalar gcd proof is unchanged: terminal verification contributes
exactly `S` gcds in all three cases. Thus

\[
 (D+1)T+m+2E+S
\]

and the F265 maximum `91,111` remain exact upper bounds.

## 2. Supplied-root encoding

Put `n_N=bitlen(N)`. V2 requires `0<=v_i<N`, so each supplied modular root
uses at most `n_N` bits. Since every `a_i` is positive,

\[
 m\le \sum_i\operatorname{bitlen}(a_i)=R.
\]

The complete supplied-root input therefore has at most `m n_N<=R n_N`
bits. Reading it costs `O(R n_N)` bit operations, which is at most
`O((R+n_N)^2)`. Every modular product starts with operands below `N`, and
all later products are reduced modulo `N`. The V1 counts of at most `m`
inversions, `2m` signed gcds, and at most `m^2` selected-row modular
multiplications consequently use `O(n_N)`-bit modular operands.

These costs lie within

\[
 O((R+n_N)^4).
\]

No arbitrary external representative must first be read or reduced. If a
different file format permits unreduced representatives, that format must
charge their total byte length separately; it is not the V2 input contract.

## 3. Preservation of the V1 theorem

Neither repair changes an arithmetic value used by saturation, refinement,
row reconstruction, parity elimination, exact-root construction, normalized-
root classification, D05 peeling, or P106 peeling. The primorial
certificates and all F265 substitutions are unchanged. The V1 proof of every
core theorem therefore applies byte-for-byte through its pinned hash.
