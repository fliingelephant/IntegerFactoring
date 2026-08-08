# F111 Hostile Audit

## Verdict

**PASS, within the stated certificate boundary.**

The independent replay regenerated the ordered public source and verified the
363-index certificate. It used only (N), `CERTIFICATE.json`, and the pinned
public basis specification. It did not import or execute the candidate replay.
It did not read F109, F110, a private factor file, or an endpoint prime
factorization. Candidate files were not changed.

## Frozen candidate

The audit read all nine candidate artifacts and the pinned F98 public-basis
source. The seven candidate files and the F98 source listed in
`RUN_MANIFEST.md` match every declared SHA-256 pin. The audit manifest also
pins `RESULT.md` and `RUN_MANIFEST.md` themselves.

The candidate `RUN.log` JSON is identical to `OUTPUT.json`. The candidate has
no declared or stored failed run.

## Independent public-source replay

For (N=3{,}241{,}632{,}473), the independent replay obtained (n=32) and
(B=n^2=1024). All 1,023 trial gcd screens, for (2\le t\le1024), equal one.

Seeds (2,\ldots,32) give 31 retained relations and 62 endpoints. Independent
LIFO gcd splitting and exact perfect-power extraction give 23 pairwise-coprime,
perfect-power-free basis blocks:

```text
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 3595103, 12214847,
20010077, 24880951, 58995227, 69463553, 116496167, 287564171,
305094821, 514544837, 736734653, 2992276129
```

Their signatures reconstruct every endpoint exactly. The basis SHA-256 is
`b4eb7c477c8a89405da6a93fc06e685091cb61d99125bb1bd3523061469e2c42`.
Its operation counts are 6,234 gcd calls, 72 overlap splits, 19 perfect-power
splits, and 114 identical merges.

The exact ordered frozen pairs are:

```text
(2,3), (2,3), (2,5), (2,5), (2,3), (2,5), (2,3), (2,3),
(2,5), (2,11), (2,3), (13,2992276129), (2,5), (2,3),
(2,3), (5,17), (2,3), (2,3), (2,5), (3,7), (2,11),
(2,3), (2,3), (2,3), (2,3), (2,3), (2,5), (2,3),
(2,3), (2,31), (2,5)
```

The complete frozen layer ends at 14,351 retained relations. The appended
((2,3)) layer makes 2,050 attempts and adds no relation. The appended
((2,4)) layer makes 1,382 attempts and adds 1,032 relations. It reaches the
declared stop at exactly 15,383 retained relations.

The full source makes 67,013 ordered attempts. First-occurrence deduplication
removes 51,630 repeats. The replay records these order commitments:

- attempt stream: `849c2752e4c9c7cf4fec08af6124f01d6d54cf9717c550c169b1270dbcf87043`;
- retained record stream: `66c23e21efe348bc5f1d8ebda3e783f0ce0cc407cab180096f50bfacfc1477be`.

## Direct screens

The replay checked both (c-w) and (c+w) for every retained record. This
gives exactly 30,766 direct gcd screens. Of these, 30,765 equal one. One equals
(N): record 6,166 has (c=w=1), so the minus difference is zero. It comes
from frozen pair index 11, ((13,2992276129)), at exponent one. No screen gives
a proper divisor. The complete direct-screen stream SHA-256 is
`92dd696491442adfb8bacb1ed3a7586106fe00d28a6212c1aab0d49c676d7822`.

## Certificate replay

The certificate contains 363 distinct, strictly increasing indices. They run
from 92 through 15,382, so the last index anchors the declared stop. Their
stream SHA-256 is
`3225efb124f40d833e84e4e09e5beb60fbbcde9ea21d116856558f7d484e9555`.

The selected records split exactly as declared:

- 327 frozen seed-basis relations;
- 36 appended relations, all from pair ((2,4)).

Their exact product is a 21,620-bit square. Its unsigned big-endian SHA-256 is
`89473e8304aa37aa3a9e06152c3dd0ffe2b59b637f8395c8c1e88ea0ebb8a3f1`.
The positive exact root is 10,810 bits. Its unsigned big-endian SHA-256 is
`71329b88fd9d2e6abac0b32a6886480450853c884097ef5e5d8edabd637fa0c7`.

The independently computed root satisfies

\[
R\equiv1{,}058{,}780{,}986\pmod N,
\qquad R^2\equiv1\pmod N,
\]

and is not congruent to (\pm1\pmod N). Terminal extraction gives

\[
\gcd(R-1,N)=79{,}043,
\qquad
\gcd(R+1,N)=41{,}011,
\]

with (79{,}043\cdot41{,}011=N).

## Static source audit

The candidate replay and pinned source parse as Python ASTs. Neither imports or
calls a general integer-factorization package, a primality test, a network
client, or a subprocess. Neither contains a hidden F109 or F110 path or hidden
`p` or `q` variable. The candidate has only two file-read sites:
`CERTIFICATE.read_text()` and the generic `sha256_file(path)` helper. Every
call to that helper receives only `CERTIFICATE` or `PUBLIC_BASIS_SOURCE`.

The candidate dynamically imports only the SHA-256-pinned F98 file. It calls
only `gcd_free_basis` and `relation_columns` from that module. The pinned file
also defines decoder and binary-kernel routines, but the F111 replay does not
call them. The pinned module has no file-read site. Its CLI body does not run
when imported.

“Factor-free” needs a precise meaning here. The replay does not call a general
integer-factorization or primality routine. It does decompose endpoints by gcd
splitting and exact perfect-power extraction. It also extracts the terminal
factors of (N) by gcd, as intended. `CERTIFICATE.json` publicly contains the
expected terminal gcd values. Those values are checked only after the audit
has independently regenerated the source, multiplied the selected relations,
computed the exact root, and computed both gcds. They do not guide source
generation or selection.

## Exact advice boundary

The index list verifies an existence claim: for this (N), the fixed public
batch contains the stated useful cross-layer dependency. The list is external
selection advice. The replay reads it directly and does not derive it.

Therefore this pass does **not** verify:

- a public algorithm that selects the 363 indices;
- a selector for another modulus or another generated batch;
- a success probability, expected running time, or all-input factoring claim.

The certificate verifies existence. It is not a selector.

## Preserved audit failures

Two audit-tool failures are preserved. Neither is a candidate failure.

1. `AUDIT_FAILED_20260808T031046339104Z_EXIT_1.*` records an order-sensitive
   comparison of two authorized AST read sites. The comparison was corrected
   to be order-independent.
2. `AUDIT_FAILED_20260808T031120635333Z_EXIT_1.*` records Python's decimal
   integer-string limit while hashing the exact product. The audit now hashes
   canonical unsigned big-endian bytes instead.
