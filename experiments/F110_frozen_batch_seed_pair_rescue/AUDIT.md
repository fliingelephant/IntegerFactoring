# F110 hostile audit

## Verdict: PASS for the stated seven-input claim

The narrow claim is correct.

- The frozen first layer has only global square roots on all seven inputs.
- The fixed prefix `(2,3), (2,4), ..., (2,n)` factors all seven inputs.
- Six factors come from exact-square parity dependencies.
- Each of those six dependencies contains frozen-layer and appended-menu
  relations.
- The seventh factor is the declared direct endpoint gcd at `(2,13)`.

This is a finite result.  It is not an all-input theorem.  It gives no
success-density bound.

## Independent evidence

I did not import or run the candidate source.

The Sage verifier independently rebuilt the initial public basis, all retained
relations, the hidden-prime parity columns, and the online elimination.  It
matched every deterministic case field.  This includes the frozen pairs,
relation counts, dependency counts, duplicate-residue counts, factors, roots,
and all six dependency index lists.

The second verifier used standard Python only.  It ignored the published `p`
and `q` fields.  It used `N`, exact arithmetic, modular powers, inverses, gcds,
perfect-power tests, and integer square roots.  It rebuilt all seven traces and
verified the six fixed exact-square certificates and the seventh direct gcd.
This is an N-only certificate replay.  It is not an N-only discovery algorithm.

Both authoritative runs passed:

```text
N-only replay:       0.725360 seconds, exit 0
Sage reconstruction: 5.309204 seconds, exit 0
```

## Seven reproduced traces

| N | first-layer dependencies | first appended pair | result | exact dependency split |
|---:|---:|---:|---|---|
| 3,241,632,473 | 2,473 global | `(2,4)` | parity factor 79,043 | 327 frozen + 36 appended |
| 12,809,029,193 | 4,506 global | `(2,9)` | parity factor 159,899 | 372 frozen + 2 seed + 148 appended |
| 12,828,426,053 | 5,087 global | `(2,7)` | parity factor 159,631 | 455 frozen + 69 appended |
| 12,854,972,153 | 4,257 global | `(2,4)` | parity factor 159,319 | 450 frozen + 1 seed + 43 appended |
| 12,859,936,021 | 6,883 global | `(2,4)` | parity factor 80,779 | 611 frozen + 28 appended |
| 12,862,140,737 | 3,485 global | `(2,5)` | parity factor 159,179 | 384 frozen + 31 appended |
| 204,816,942,773 | 5,327 global | `(2,13)` | direct factor 639,839 | not applicable |

The seventh stop is exact:

```text
pair=(2,13)
exponent=44
orientation=u_times_v_power
c=68137094950
w=54674882390
gcd(c-w,N)=639839
```

The trial screen is null for every integer from 2 through `n^2` in every case.

## The first layer is genuinely frozen

The source calls `public_basis` once, at line 150.  It does so after retaining
the initial seeds and before running a frozen trajectory.  It builds the full
`frozen_pairs` list before it generates any first-layer relation.  It never
recomputes that basis.

The independent N-only gcd/perfect-power basis produced the same frozen pair
list in every case.  Thus endpoint factorization is not needed to define this
part of the source.

The online dependent-column vectors form a basis of the parity kernel.  Every
first-layer basis root is `+1` or `-1` modulo `N`.  The normalized-root map is
multiplicative on the kernel because every exact relation value is `1` modulo
`N`.  Therefore every first-layer dependency has a global root, not only the
vectors printed by one elimination order.

I also removed unit values, removed repeated exact relation values, and used a
different pivot order based on prime labels.  The resulting first-layer kernel
bases had 6 to 24 dependencies.  Every root was still global.

## The `(2,v)` prefix is nonadaptive after the seed batch

The stored executable declares all pairs in lexicographic order.  The loop
values depend only on `n` and the loop counters.  They do not read generated
relations.  A factor only stops the loop.

All seven successful positions satisfy

```text
successful_pair = (2, seed_pair_menu_attempted + 2).
```

The positions are 2, 7, 5, 2, 2, 3, and 11.  No run reaches a pair with first
member greater than 2.  The N-only replay executed only this `u=2` prefix and
reproduced the same stopping relation or direct gcd in every case.

Thus the smaller source in `RESULT.md` is valid for these seven traces.  It is
an inferred source restriction.  The stored candidate executable still
contains the larger all-pairs menu.

## Exact-value and order audit

The candidate removes repeated residues, but it does not remove repeated exact
relation values `P=c*w`.  This creates many raw dependency directions.

| N | frozen pair entries / distinct pairs | first-layer raw relations / unique nonunit `P` |
|---:|---:|---:|
| 3,241,632,473 | 31 / 7 | 14,351 / 11,885 |
| 12,809,029,193 | 33 / 9 | 20,820 / 16,320 |
| 12,828,426,053 | 33 / 10 | 23,130 / 18,049 |
| 12,854,972,153 | 33 / 9 | 20,819 / 16,575 |
| 12,859,936,021 | 33 / 11 | 23,703 / 16,842 |
| 12,862,140,737 | 33 / 8 | 18,506 / 15,045 |
| 204,816,942,773 | 37 / 8 | 23,122 / 17,799 |

Therefore the large raw first-layer dependency counts are order- and
duplicate-sensitive.  They must not be read as counts after the public
decoder's exact-value deduplication.  The qualitative all-global claim is
unchanged.

This artifact does not weaken the six successful certificates.  Each selected
support already uses distinct exact relation values.  Canonical first-occurrence
deduplication changes no selected index, support size, root, gcd, or provenance
split.  All six witnesses still cross the layer boundary.

Repeated frozen pair entries are also real.  A later copy is normally a no-op
because the residue set is global.  Similarly, early appended pairs can repeat
frozen trajectories.  The reported menu position counts scheduled pairs, not
only pairs that retain a new relation.  This is consistent with the source.

## Complexity

Let `B=n^2`.  The restricted source has at most

```text
(n-1) + 2(n-1)(B+1) + 2(n-2)(B+1)
```

residue attempts.  This is `O(n^3)`.  The stored all-pairs menu has

```text
2 * binomial(n-1,2) * (B+1)
```

menu attempts.  This is `O(n^4)`.  The exact wording in `RESULT.md` correctly
distinguishes the stored source from the restricted seven-trace source.

These are source-size counts.  They are not total runtime bounds.  Each modular
power also costs arithmetic operations.  More importantly, the stored decoder
factors endpoint integers.  F110 does not prove that operation polynomial in
`n`.

## Factor-assisted and public-equivalence caveats

The candidate gets `p` and `q` from F109 to define its fixed test cases.  Inside
each trace, it uses them only to form `N` and report metadata.  The N-only replay
confirms that the certificates do not depend on access to those fields.

The discovery decoder still factors every retained endpoint.  The separate
N-only replay verifies fixed certificates.  It does not discover their supports.

F110 cites P106 for a factor-free polynomial decoder on an explicit frozen
batch.  F110 does not pin or execute that decoder.  This audit therefore treats
the P106 statement as an external theorem.  The relevant preconditions are
clean here: exact-value deduplication preserves every successful witness, and
an independent prime-label elimination finds a useful dependency by the same
final raw relation in all six parity cases.  If the cited public-row equivalence
is accepted, a factor-free kernel decoder has the same success existence.

No statement here promotes the seven examples to all inputs.

## Preserved failed audit attempts

Two audit-harness failures remain under timestamped names.  The first omitted
unit fragments during public basis splitting and had a log-newline error.  The
second N-only replay passed, but a brittle source-text count stopped the Sage
stage.  `AUDIT_FAILED_RUNS.md` records both corrections.  Neither failure found
a candidate defect.
