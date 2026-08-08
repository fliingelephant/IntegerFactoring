# F102 — full-pool parity-core diagnosis of F98

## Question

Why does the F98 pool contain a useful relation circuit? Test whether its
factor-assisted prime-valuation matrix has a substantial dependency core, or
whether the public 166-value circuit is an isolated post-selected accident.

## Exact diagnostic

Read the frozen F98 public output. Regenerate and exact-value-deduplicate its
full 9,414-column relation pool. Factor each exact relation value for
diagnosis only.

Build the binary prime-valuation matrix. Repeatedly apply this lossless peel:

1. Find a parity-prime row of active degree one.
2. Delete its unique incident relation column.
3. Update all incident row degrees.

A degree-one row forces the coefficient of its column to zero in every
binary dependency. Thus the peel preserves the full kernel. Report the full
and peeled matrix sizes, ranks, nullities, row degrees, connected components,
provenance, and whether the public 166-column circuit lies in the peeled core.

Also run the same peel on the distinct-value pool whose first raw occurrence
is in the first 5,616 public records.

## Scope

This is a factor-assisted fixed-input diagnosis. It cannot prove that a core
or a useful root occurs on other inputs. It is designed to identify the
exact source-side property that an unbounded theorem would need to force.
