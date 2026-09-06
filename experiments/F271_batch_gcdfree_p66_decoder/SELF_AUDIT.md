# F271 self-audit

## Verdict

PASS as an internally consistent proof candidate. This is a self-audit, not
a hostile audit or an independent reconstruction. No F265 source, freeze,
preflight, or production run is authorized by this verdict.

## 1. Disclosed correction during drafting

An earlier conversation report gave `89,293` gcd calls per maximum residual
bank. That count treated every saturation call inside a general two-integer
recursion as a successful recursion edge. This was not valid: without an
equal-support precondition, a saturation probe can return one.

F271 repairs the issue explicitly.

1. `TWO_BASE` first performs two saturations to isolate the complete common
   prime support.
2. `SAME_SUPPORT` then preserves equal support at every recursive call.
3. Its saturation calls correspond exactly to recursion edges.
4. The corrected full bound is `91,111` calls per bank and `69,973,248`
   across 768 banks.

No frozen artifact contained the discarded count. The corrected count is the
only normative F271 value.

## 2. Saturation checks

1. The exponent is `bitlen(u)`, where `u` is the integer whose full primary
   parts are requested. It is not the bit length of the support witness.
2. Modular reduction does not change a gcd with `u`.
3. If `p|v`, then `bitlen(u)*v_p(v)>v_p(u)`, including powers of two and the
   maximum 361-bit boundary.
4. The primitive is never called with `u=1` or `v=1`. Those branches are
   handled before the call.

## 3. Two-integer recursion checks

5. The first two saturations make the shared operands have exactly equal
   radicals. Their gcd remains the supplied leaf gcd.
6. After division by `d`, `x_0` and `y_0` are coprime.
7. Equal support guarantees that nonunit `x_0` gives nonunit `A`, and the
   two have equal support. The same holds on the `y` branch.
8. `A`, `B`, and `C` have disjoint support. Outputs of the two recursive
   branches therefore cannot overlap.
9. The coordinate maps reconstruct `d*x_0` and `d*y_0`. They do not assume
   squarefree inputs or unit exponents.
10. Equality and divisibility are not special algorithm branches. The same
    recursion handles them.

## 4. Global insertion checks

11. Every replacement block with positive old-block coordinate has support
    inside that old block. It stays coprime to untouched old blocks.
12. Every new-only output is multiplied to its exact local exponent into the
    residual. Multiplying each opaque block only once would be wrong when
    its local exponent exceeds one.
13. The residual loses the complete primary part supported on the touched
    leaf. One row cannot touch that leaf again.
14. A left-first tree descent carries an exact gcd. If the left child gcd is
    one, pairwise coprimality of child products implies that the parent gcd
    is the right-child gcd.
15. Exact-value duplicate rows are not deduplicated. Their distinct modular
    roots can make their support-two relation useful.

## 5. Termination and resource checks

16. Every rational prime follows subtractive Euclid on positive integer
    exponents. The measure uses the invariant exponent gcd and reaches
    equality.
17. Across row insertions, the current opaque-block exponent is the running
    gcd of prior positive row valuations for that prime. The telescoping
    charge is therefore valid.
18. One recursion node can contain many rational primes, but nodes at one
    depth have disjoint prime supports. Charging a node to any participating
    prime does not undercount the sum of prime paths.
19. `T<=sum omega(a_i)` and `S<=omega(product a_i)` are proof bounds. The
    executable need not factor an input to enforce the fixed caps.
20. The F265 valuation-mass bound is `64*360`, not `64*361`.
21. The sharper `S<=1875` bound uses the total product limit `2^23104`, not
    the valuation-mass limit `2^23040`.
22. A 2,048-leaf tree has exactly 11 descent levels.
23. The registered formula includes the final `S` independent coprimality
    gcds. They are not hidden in the refinement count.

## 6. Terminal verification checks

24. `P mod q_j^2` is divisible by `q_j` because `P` is divisible by
    `q_j`.
25. Dividing that remainder by `q_j` gives `P/q_j mod q_j`, so one gcd per
    block verifies coprimality with the complete complementary product.
26. A result equal to one for every block is equivalent to pairwise
    coprimality. No unordered-pair scan remains.
27. Exact reconstruction is checked separately. Coprimality alone does not
    verify exponent provenance.

## 7. Parity and root checks

28. A nonsquare composite block supplies one public parity row. All its
    nonzero hidden prime-parity rows equal that row; even internal prime
    valuations give zero rows.
29. Singleton relations are exactly zero columns. Support-two relations are
    exactly equal columns.
30. The star basis spans every pair in one nonzero signature class. Unit
    vectors span every zero-class pair.
31. Low-basis dimension plus complement dimension is the full kernel
    dimension. Root verification is therefore at most `m`, not `2m`.
32. Exact positive roots use square-block roots and half-exponents on
    nonsquare blocks. No prime factorization is needed.
33. The normalized-root homomorphism still requires unit supplied roots. A
    zero or nonunit residue is outside F271 and must be handled first.

## 8. Peel-semantics checks

34. D05 private support uses `e_ji>0`, not parity support.
35. Its private product is nonsquare exactly when one private nonsquare block
    has odd exponent. Pairwise coprimality prevents cancellation between
    private blocks.
36. The `(1,2)` valuation example proves that P106 parity-degree-one peeling
    can delete a row that D05 does not delete.
37. F271 states both legal rules but does not silently substitute one for the
    other. A future packet must freeze its choice.

## 9. Complexity checks

38. Every opaque block has at most `r` bits. The product-tree root has at
    most `R` bits.
39. At most `O(E)` leaves are created across the recursion forest. Updating
    a dynamic tree therefore costs `O(E log S)` product-node changes, not a
    rebuild after every comparison.
40. The stated `O(R^3 log R)` schoolbook bound deliberately charges every
    product-tree multiplication at the full `R`-bit width.
41. The full `O((R+bitlen(N))^4)` decoder bound is conservative. It includes
    matrix work, exact roots, modular products, inversions, and signed gcds.
42. Bernstein's faster coprime-base theorem is prior art. F271 does not claim
    its own simple refinement is essentially linear in bit operations.

## 10. Sanity checker boundary

`sanity_check.cpp` is a deterministic finite checker, not proof of the
general theorem. It checks:

- all 250,000 ordered pairs `1<=x,y<=500`;
- exact reconstruction and pairwise coprimality for every overlapping pair;
- the recursion-node valuation-mass bound;
- exactly two internal gcd calls per recursion node when the leaf gcd is
  supplied;
- equal values, divisibility, 360/359-bit powers of two, opposed mixed
  prime-power slopes, and two composite small fixtures;
- the 58th, 1,875th, and 1,876th primes and their exact primorial bit
  lengths; and
- the final F265 per-bank and packet arithmetic.

The source uses the locally installed GMP C++ interface, exact GMP gcd and
modular powering, and a deterministic sieve through 20,000. It uses no
random input, factorization library, network, remote host, or hidden dataset.

## 11. Remaining attack surface

The following still require a fresh hostile audit before this result can be
promoted or used in an experiment.

- Reconstruct the recursion and exponent-coordinate maps without using this
  proof.
- Check the node charging when several primes split into different branches.
- Independently reproduce the primorial constants.
- Inspect a future dynamic product-tree implementation for stale products or
  duplicate-support transients.
- Check that a future F265 byte contract does not demand every quadratic
  support-two event while claiming subquadratic output.
- Check that direct coordinate and chord pair controls remain explicitly
  outside the decoder speedup.

F271 remains a decoder theorem. It supplies no evidence that an elliptic bank
contains a useful relation.
