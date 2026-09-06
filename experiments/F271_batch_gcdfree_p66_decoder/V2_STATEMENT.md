# F271 V2 statement — additive boundary repair

## Status and construction

F271 V2 is a narrow additive repair of the frozen V1 statement. Its
normative base is the exact file

```text
STATEMENT.md
SHA-256 19b288038c4f9e339d3f56e51fb1c6d7277fd9e322e486f2339edd0c68bf64ba
```

Read that file in full, then apply only the two replacements below. Every
other definition, algorithm, theorem, constant, scope restriction, and
novelty boundary is unchanged. In particular, V2 does not change the
saturation primitive, `SAME_SUPPORT`, `TWO_BASE`, incremental insertion,
the square-class matrix, either peel rule, or any F265 call cap.

## 1. Canonical supplied residues

Replace the V1 input clause for `v_i` by the following clause.

For every row, the supplied modular root is its canonical integer
representative `v_i` satisfying

\[
 0\le v_i<N,
 \qquad v_i^2\equiv a_i\pmod N,
 \qquad \gcd(v_i,N)=1,
\]

where `N>=3` is odd. Thus each supplied root has at most
`bitlen(N)` bits. Arbitrarily long unreduced integer spellings of the same
residue are outside this theorem's input contract.

All remaining V1 input definitions are unchanged, including

\[
 R=\sum_i\operatorname{bitlen}(a_i),
 \qquad
 r=\max_i\operatorname{bitlen}(a_i).
\]

Because every positive row contributes at least one bit, `m<=R`. The total
supplied-root encoding length is therefore at most
`m*bitlen(N)<=R*bitlen(N)` and is covered by the V1 full-decoder bound

\[
 O((R+\operatorname{bitlen}N)^4).
\]

This is a representation boundary only. It does not strengthen the modular
root premise.

## 2. Empty terminal block list

Replace the final paragraph of V1 Section 5 by the following exact case
statement.

If `S=0`, set `P=1`. Row reconstruction is checked as usual, and terminal
block coprimality is vacuous. Build no terminal modulus-product tree or
remainder tree, and perform zero terminal divisions and zero terminal gcds.

If `S>=1`, build one product tree for the moduli `q_j^2`, propagate `P`
through one remainder tree, and perform exactly `S` terminal gcd calls. The
identity

\[
 \gcd\left(q_j,{P\bmod q_j^2\over q_j}\right)
 =\gcd\left(q_j,\prod_{k\ne j}q_k\right)
\]

is unchanged. It verifies all pairwise-coprimality claims without an
unordered-pair scan.

The exact multiplication and remainder-division counts for `S=0`, `S=1`,
and `S>=2` are supplied in `V2_PROOF.md`. The refinement and terminal gcd
bound remains exactly

\[
 (D+1)T+m+2E+S.
\]

## 3. Unchanged scope

F271 V2 is still a deterministic, factor-free decoder theorem. It proves no
elliptic source theorem, residual-core bound, nonzero kernel, non-global
normalized root, or integer-factoring result. The maximum F265 values remain
`91,111` gcd calls per bank and `69,973,248` calls across 768 banks.
