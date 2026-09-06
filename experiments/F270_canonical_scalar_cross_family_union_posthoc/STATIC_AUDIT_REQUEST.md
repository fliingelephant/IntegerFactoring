# F270-D01 static hostile audit request

Review the frozen packet before any compile, self-test, preflight, or target
execution. Give a literal verdict: `PASS`, `REVISE`, or `INVALID`.

At minimum, check these points:

1. The implementation joins F268's global evidence `case_index` to the corpus
   position and does not confuse it with the cell-local public `index`.
2. It reads only `ROW` records for arithmetic. It never reads or concatenates
   the prior per-family `BLOCK` records.
3. It compares every supplied-root pair in an equal exact-value class before
   it deduplicates that class.
4. It recomputes one pairwise-coprime opaque block system from the global
   deduplicated values and verifies reconstruction.
5. Original union rank expands deduplicated columns through all provenance.
   Each family rank is independently restricted and must replay as full.
6. Peeling marks all current degree-one rows in one round, deletes them
   simultaneously, and continues to a fixed point.
7. Singleton and support-two scans use only the fixed core. The residual
   quotient is complete when no useful low relation exists.
8. Every emitted relation verifies an exact positive square root, supplied
   modular root, normalized root, both signed gcds, and root class.
9. Clean/control labels use only the public bank-table `earlier_factor` field.
   Controls cannot create a held-out trigger.
10. Empty core in all target cases produces the literal seam-kill status.
11. Work caps fail closed. The runner cannot exceed eight `nice -n 15`
    workers, 4 GiB projected live memory, 512 MiB output, or four hours.
12. No direct gcd screen was added outside input/relation authentication.

Also compile mentally for type, aggregate-initializer, empty-core, exact-
duplicate, all-global-low-span, and output-order errors. Dynamic testing cannot
start until all blocking static findings are repaired in a new frozen packet.
