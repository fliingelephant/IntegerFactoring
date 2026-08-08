# F119 Preregistered Question — Private Rows in the Complete All-Pairs Source

## Object

For an odd input `N`, let `n = N.bit_length()` and `B = n^2`. Use the fixed
F116 source order:

1. seeds `2..n`;
2. the deterministic frozen seed-basis pairs;
3. every unordered seed pair `2 <= u < v <= n` in lexicographic order;
4. for each pair and `0 <= e <= B`, residues `[u^e v]_N` followed by
   `[u v^e]_N`;
5. canonical-residue first occurrence, then global exact-value first
   occurrence.

For a retained unit `c`, write `w` for its least positive inverse and

```text
P(c) = c*w = 1 + kappa_N(c)*N.
```

The square-class matrix has one column for each distinct nonunit exact value
`P(c)` and one hidden row for each prime with odd valuation.

## Primary question

Decide whether either statement can be proved unconditionally.

### Obstruction target

Construct an infinite family of odd distinct-semiprime, non-perfect-power
inputs for which every column in the complete polynomial-size source has a
prime row that remains private after the entire source is appended.

### Progress target

Prove that the complete cross-pair source forces enough prime-row reuse to
create a nonzero square-class dependency. A useful factoring theorem would
also have to prove that the normalized root map is nonzero.

Neither relation count nor one repeated prime is sufficient.

## Permitted proof tools

- Exact canonical-inverse and carry identities.
- Integer gcd and valuation arguments.
- CRT, the prime number theorem, Bertrand, Dirichlet, and Linnik as named
  established theorems.
- Exact finite computation only if a named source, hard timeout, output, log,
  and preserved failures are created before the result is used.

Smoothness heuristics, random-integer models, and empirical factor-size
distributions are not proof.

## Planned proof sequence

1. Express exact-value equality and prime-row incidence only through the carry
   set.
2. Prove the strongest unconditional row-degree and private-row criteria that
   follow from carry differences.
3. Try to extend the P104/X69 CRT construction to a genuine cross-pair
   submatrix.
4. Audit whether that construction is stable against the frozen layer and all
   other pair columns.
5. If the complete target remains open, state one exact self-generated-carry
   lemma sufficient for each direction.

## Falsifiers and scope controls

- A private prime only inside a selected submatrix does not prove a full-source
  obstruction.
- A private row at insertion time is not stable if a later column reuses it.
- Row reuse does not imply a dependency.
- A dependency does not imply a non-global root.
- A family with a polynomially small factor is not a live-route obstruction
  after trial division.
- A source whose bases or exponent exceed the declared F116 bounds is invalid.
- A construction whose output bit length makes the controlled submatrix
  subpolynomial must be reported with its actual asymptotic size.

## Deliverable boundary

The result will separate:

1. exact general laws;
2. a proved full-source theorem, if any;
3. proved submatrix constructions;
4. the precise unresolved number-theory lemma.

No durable project ledger will be edited.
