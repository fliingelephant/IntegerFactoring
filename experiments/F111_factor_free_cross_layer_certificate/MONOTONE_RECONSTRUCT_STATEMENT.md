# Proof-blind reconstruction: monotone full-source consequence

## Isolation

Read only this statement, `MONOTONE_RECONSTRUCT_INPUT.json`, and the public
source specification below. Do not read another F111 file or an F98, F109,
F110, F115, or F116 file. Do not use a factorization or primality routine. Do
not use a known factor of `N`, a dependency support, or a retained-record stop.

Write only new files whose names start with `MONOTONE_RECONSTRUCT_`, except the
two supplied files. Preserve all failed attempts. Use a named hard timeout.
Pin every input, source, output, log, failure, and report with SHA-256.

## Claims to reconstruct

### 1. Exact-value extension theorem

Let an ordered source produce positive integers `P_i` with `P_i = 1 mod N`.
Keep only the first occurrence of each exact integer value and delete `P_i=1`.
Let `M` be the exact integer square-class parity matrix of the retained values.
For `x` in `ker(M)`, let `R(x)` be the positive square root of the selected
exact product. Define the normalized root class as `R(x) mod N`, modulo the
global roots `{+1,-1}`.

Prove that appending more ordered source records cannot destroy an existing
dependency with nonzero normalized root class. The old distinct exact values
remain the initial coordinate block. Also prove that every complete binary
kernel basis of the extended matrix contains a vector with nonzero normalized
root class whenever one exists. Do not claim that a particular kernel-basis
vector persists.

### 2. Public full source

The input gives an odd integer `N`, its bit length `n`, and `B=n^2`.

1. Test `gcd(t,N)` for every `2 <= t <= B` and return a proper divisor if one
   occurs.
2. Attempt seeds `c=2,3,...,n` in order. For every first canonical residue,
   compute its least positive inverse `w`, test both `gcd(c-w,N)` and
   `gcd(c+w,N)`, and retain the exact value `P=c*w`.
3. Build a deterministic factor-free gcd basis of all seed endpoints. Start
   with one signature per endpoint. Repeatedly extract maximal exact perfect
   powers, split the first overlapping basis item by gcd and exact division,
   merge equal values, and continue until the sorted blocks are pairwise
   coprime and perfect-power-free. Verify exact endpoint reconstruction.
4. For each seed relation, collect the sorted blocks that occur in either
   endpoint. Use its smallest block and `1` if there is only one block;
   otherwise use its two smallest blocks. These ordered pairs are the frozen
   pairs.
5. For every frozen pair `(u,v)`, every `e=0,1,...,B`, and the displayed
   order, attempt `[u^e v]_N` and `[u v^e]_N`.
6. After the frozen layer, run the fixed pairs `(2,3)` and `(2,4)`, in this
   order. For each pair, run both displayed orientations for every
   `e=0,1,...,B`.
7. Use one global first-occurrence residue set. Apply the invertibility and two
   direct sign screens to every newly retained residue.
8. After the complete source ends, remove `P=1` and repeated exact values by
   first occurrence. Compute a complete exact square-class kernel without
   factoring any endpoint or relation value. Test the exact positive root and
   both terminal gcds for every kernel-basis vector.

The factor-free gcd-basis implementation must be deterministic and fully
specified in the reconstruction source. It can use gcd, exact division,
integer perfect-power tests, exact integer square root, modular arithmetic,
and binary linear algebra.

### 3. Required fixed-input result

Independently run the full source and complete decoder from only `N`, `n`, and
`B`. Verify all source counts, all direct screens, rank, nullity, every basis
root, and any terminal factor. The computation must not read a certificate
stop or dependency indices.

### 4. Uniform complexity boundary

Prove symbolically that this is one uniform `N`-input polynomial-bit-time
algorithm. Count source positions, endpoint and relation-value bit lengths,
the total input length of gcd refinement, matrix dimensions, kernel-basis
size, exact dependency-product bit lengths, and all basis-root tests.

State the exact boundary. The fixed pairs are constant program text but were
historically chosen after experiments. Success is required only for the one
supplied `N`. Do not infer an all-input success theorem, probability law, or
factoring algorithm for arbitrary integers.
