# Proof-blind reconstruction: fresh 54-bit all-pairs certificate

## Isolation

Read only this statement and `RECONSTRUCT_INPUT.json`. Do not read another
F116 file. Do not read F104, F110, F111, or F115. Do not use a factorization
or primality routine. Do not use a known factor of `N`.

Write only new files whose names start with `RECONSTRUCT_`, except the two
supplied files. Preserve all failed attempts. Use a named hard timeout. Pin
the input, source, output, log, failures, and report with SHA-256.

## Public source

The input gives an odd integer `N`, its bit length `n`, `B = n^2`, a retained
record stop, and one increasing list of zero-based retained-record indices.
The list is external certificate advice. It is not a discovery rule.

Maintain an ordered record list and a set of seen canonical residues. For an
attempted residue `c`:

1. Count the attempt.
2. If `c` was seen, count one duplicate and do nothing else.
3. Otherwise, mark `c` as seen.
4. If `gcd(c,N)` is proper, report it. Otherwise require that `c` is a unit.
5. Compute its canonical inverse `w`, with `1 <= w < N`.
6. Test `gcd(c-w,N)` and `gcd(c+w,N)`.
7. Retain the exact relation value `P = c*w`, its endpoints, and provenance.

First attempt every seed `c = 2,3,...,n` in order.

### Public gcd basis

Give endpoint `i` the signature `{i:1}`. Put every endpoint greater than one
into a work stack in endpoint order. Pop the last item first. Maintain one
ordered basis list.

For a popped pair `(x,s)`:

1. Discard it if `x = 1`.
2. If `x = a^e` for some `e > 1`, choose the largest such `e`, replace `x`
   by `a`, and multiply every signature multiplicity by `e`.
3. Scan the basis from its first item. For the first `(y,t)` with
   `d = gcd(x,y) > 1`, remove `(y,t)`.
4. If `x = y`, merge the signatures and push `(x,s+t)`.
5. Otherwise push, in this order,
   `(d,s)`, `(x/d,s)`, `(d,t)`, `(y/d,t)`.
6. If no basis item overlaps `x`, append `(x,s)`.

Continue until the stack is empty. Sort the basis by block value. Verify
pairwise coprimality, perfect-power freedom, and exact endpoint
reconstruction.

For each seed relation, collect the sorted block values whose signatures use
either endpoint. If there is one block `u`, select `(u,1)`. Otherwise select
the two smallest blocks `(u,v)`. Keep seed-relation order. These are the
frozen pairs.

### Frozen layer

For each frozen pair `(u,v)`, in order, and every `e = 0,1,...,B`, attempt
these residues in this order:

```
[u^e v]_N
[u v^e]_N
```

Use provenance `frozen_seed_basis_pair`, the pair index, `u`, `v`, `e`, and
the orientation.

### Complete small-pair menu

Then enumerate all unordered pairs

```
2 <= u < v <= n
```

in lexicographic order. Give them consecutive zero-based menu indices. For
each pair, attempt the same two orientations for every `e = 0,1,...,B` in
the order above. Use provenance `nonadaptive_seed_pair`.

Stop immediately when the retained-record count equals the declared stop.

## Certificate verification

Verify all of the following without factoring an endpoint or relation value:

1. `n`, `B`, and every trial gcd through `B`.
2. The seed basis, frozen pairs, frozen counts, appended pair count, source
   attempt count, duplicate count, exact stop, and every direct sign screen.
3. The supplied indices are distinct, increasing, in range, and end at the
   final retained record.
4. The selected provenance counts and the number of distinct appended pairs.
5. The exact selected product is a positive square.
6. Its positive root modulo `N` is a non-global square root of one.
7. Both terminal gcds and their product.

Use bounded byte encodings for large-integer hashes.

## Required boundary

The replay verifies one advised fixed support. It does not discover the
support and does not prove another input succeeds. However, if this support
is valid, exact-value dependency existence is monotone under appending more
records. Therefore a separate complete factor-free decoder can run the full
public pair menu without using the stop or support. This monotonic consequence
does not prove an all-input factoring theorem.
