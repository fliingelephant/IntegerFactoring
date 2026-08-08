# F119 hostile-audit preserved failed routes

No program was run. These are rejected proof extensions found during the
hostile audit.

## 1. Transfer named-residue sign screens through exact-value equality

The CRT and size argument controls `c^2` modulo the factors of `N_t` for the
named word `c=a^2b`. If a different residue `d` has the same exact value, the
identity `d w_d=c w_c` does not imply `d^2=c^2` modulo either factor. Thus the
named sign-screen proof cannot be transferred to the earlier representative.

## 2. Treat exact-value retention as raw-occurrence retention

Distinct protected carries prove that the final exact-value set contains every
protected value. They do not prove that the named exponent-two raw occurrence
is its global first exact-value occurrence. Value retention and provenance
retention are different statements.

## 3. Promote selected privacy to complete-source privacy

The CRT conditions exclude `q_c` from the other selected values only. They do
not constrain the carries of seed, frozen, or unselected all-pairs columns. An
unselected congruent carry can reuse the row.

## 4. Promote trial-hardness to operational survival

Factors larger than `n_t^2` defeat the initial trial screen. Null screens at
the named residues defeat those named positions. Neither fact controls an
unselected earlier endpoint sign screen.

## 5. Infer a dependency from row reuse

No degree-one rows would be necessary for some obstruction arguments, but it
does not force rank deficiency. A binary matrix can have no private row and
still have full column rank.

## 6. Infer a factor from a square dependency

An exact square dependency can have positive root `+1` or `-1 modulo N`. A
separate non-global-root statement is necessary.

## 7. Infer a complete-source impossibility from the CRT scale

This independent-modulus construction spends `Theta(M log M)` input bits to
protect `M` columns. That limits this route to `Theta(n/log n)`. It does not
exclude a more coupled construction with better scale.
