# F119 Preserved Failed Routes

These are logical failures, not failed program runs. F119 ran no computation.

## 1. Selected privacy is not complete-source privacy

The CRT family in `RESULT.md` gives each selected exponent-two cross-pair
value a valuation-one prime that divides no other selected value. It does not
control the carries of the seed layer, the frozen layer, or the remaining
all-pairs words.

By the exact carry law, an unselected carry congruent to the protected carry
modulo its assigned prime reuses that row. Therefore an identity submatrix on
selected columns does not prove a private row after the complete source is
appended.

## 2. Privacy at insertion time is not stable privacy

A prime can be private when its column first appears and be reused by a later
column. Any complete obstruction must quantify over the final deduplicated
carry set `K_N`, as condition `(FSP)` does. Source order alone does not prevent
later reuse.

## 3. Row reuse is not a parity dependency

Eliminating degree-one rows is necessary for a dependency that uses every
affected column, but it does not imply that the columns are linearly
dependent. A binary matrix can have no degree-one row and still have full
column rank. Thus `(REUSE)` is strictly weaker than `(CLOSE)`.

## 4. A dependency is not yet a factor

Even if a subset product is an exact square, its positive root can be `+1` or
`-1 modulo N`. That gives only a global gcd. A factoring theorem needs the
separate `(ROOT)` conclusion.

## 5. Direct independent CRT protection has the wrong scale

The present construction assigns one modulus `q_c^2` to each protected
column. Since each `q_c` must exceed the selected carry diameter, protecting
`M` columns costs `Theta(M log M)` input bits in this design. It therefore
protects only `Theta(n/log n)` columns at bit length `n`.

This is a limitation of this route. It is not a proof that a more coupled
construction cannot protect a polynomial-size complete source.

## 6. Smoothness and random-row models do not close the gap

Heuristics about large prime factors, smoothness, or random binary matrices
do not prove either stable privacy or forced closure for the self-generated
carry set. No such heuristic is used in `RESULT.md`.

## 7. Earlier direct factors remain uncontrolled

The named exponent-two residues have null sign screens, and both factors of
the constructed semiprime exceed the trial bound. The proof does not control
the sign screens of a different earlier residue with the same exact value. It
also does not exclude a direct factor at another unselected source position
before the named positions are reached. The theorem is therefore about the
complete no-stop source and its selected submatrix, not operational survival
through every earlier position.
