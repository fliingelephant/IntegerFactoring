# F118 result — no null in the registered 58-bit corpus

## Exact verdict

The preregistered run completed. It found no full-source null.

Fifteen prime pairs were reached before the fourth selected case completed.
Eleven failed the preregistered P98-stability gate. Four passed every corpus
gate and had a complete frozen layer with positive kernel nullity and zero
normalized-root quotient image.

The complete fixed source produced a non-global normalized root on all four
selected inputs. No selected input used a direct factor channel.

| Ordinal | `N = p*q` | Frozen columns | Frozen rank | Frozen nullity | First useful pair | Attempts | Columns at stop | Rank at stop | Nullity at stop |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | `204800061759986701 = 320000143*639999907` | 127,840 | 106,937 | 20,903 | `(6,50)` | 2,140,916 | 1,387,495 | 1,077,074 | 310,421 |
| 7 | `204800066879973329 = 320000179*639999851` | 100,935 | 80,446 | 20,489 | `(6,44)` | 2,100,674 | 1,359,062 | 1,053,289 | 305,773 |
| 14 | `204800093759919353 = 320000287*639999719` | 74,036 | 65,005 | 9,031 | `(6,47)` | 2,126,202 | 1,384,574 | 1,080,202 | 304,372 |
| 15 | `204800123199900673 = 320000339*639999707` | 112,147 | 91,979 | 20,168 | `(6,49)` | 2,139,704 | 1,407,595 | 1,090,999 | 316,596 |

Every frozen fundamental dependency root was `+1`. At the stop, the earlier
fundamental roots were global, followed by one non-global root. Ordinals 7,
14, and 15 also had one or two `-1` fundamental roots before the useful root.
Thus the kernel was large long before the quotient-root image became nonzero.

The four exact terminal roots and gcds are in `OUTPUT.json`. Each root squares
to one modulo its displayed `N`. Its two sign gcds are the displayed input
primes and multiply to `N`.

## Why the online check is complete

Each retained relation column is reduced against earlier pivot columns. A
column that reduces to zero gives a dependency whose latest column is unique.
These dependencies are independent. Their count is `columns - rank`, so they
form a kernel basis.

The online half-root invariant is exact. When two parity expressions are
added, it multiplies their half-roots and one copy of each prime in the
intersection of their odd supports. This is exactly the carry from

```text
floor((a+b)/2) = floor(a/2) + floor(b/2) + (a mod 2)(b mod 2).
```

P66 makes the normalized-root map a homomorphism. Therefore all-global roots
on this fundamental basis prove zero quotient image for the completed prefix.
The first non-global basis root proves image dimension one for a distinct
semiprime.

This is stronger than counting dependencies. For example, ordinal 5 had
310,420 global fundamental roots before its first non-global root.

## Exact source positions

For `n=58`, each unordered pair has `2*(n^2+1) = 6,730` attempt positions.
The complete source has 11,124,747 attempts. The four useful roots occurred
at pair indices 255, 258, 260, and 261, zero based. Their exact exponents were
428, 3097, 3118, and 359. The source attempt counts in the table follow from

```text
383,667 + pair_index*6,730 + 2*exponent + orientation_offset.
```

All four witnesses used the first orientation, so the offset is one.

## Registered scaling record

The four selected runs processed 8,507,496 attempt occurrences and retained
5,538,726 distinct relations. Their case times sum to 292.353993 seconds.
The measured rates over these exact prefixes were 29,099.982 attempts per
second and 18,945.272 retained relations per second.

The endpoint-factor cache recorded 11,019,260 misses. The fixed deduplication
table used 134,217,728 payload bytes. Peak process resident memory was
1,450,786,816 bytes on macOS. These are measured prefix costs. They are not a
runtime extrapolation for a hypothetical null, because sparse elimination
fill and endpoint factorization cost are data dependent.

## Factor-assisted boundary

The source residues, pair order, exponents, deduplication, direct screens, and
stopping positions depend only on `N`. Known `p,q` values certify the corpus.

Sage/Pari endpoint factorization supplies hidden prime-parity rows. P106 makes
their nonzero row-mask set, rank, and kernel exact equivalents of the public
P66 refinement. The online root invariant is exact. Thus `CAP_COMPLETE_NO_NULL`
is an exact result for this registered finite corpus.

The run did not recover public dependency supports. The four positive cases
remain factor-assisted. They are not factor-free certificates. The result is
not an input-independent source theorem.

## Feedback boundary

No `NULL_INPUT.json` exists. The registered feedback condition was therefore
false. Running recursive canonical integer-block feedback on one of the four
positive inputs would answer a different question and was not authorized.

## Artifacts

- Registration: `REGISTRATION.json`.
- Corpus and source design: `CORPUS_SPEC.json`, `DESIGN.md`.
- Source: `scan_full_source.py`.
- Timeout runner: `run_with_timeout.py`.
- Output: `OUTPUT.json`.
- Log: `RUN.log`.
- Named timeout: `F118_58BIT_FULL_SOURCE_NULL_HARD_TIMEOUT`, 1,200 seconds.
- Wrapper result: `PASS`, 295.204076 seconds.

SHA-256:

- Registration: `4918e7d9b48e9310145ad466ab330e51e9ce36891b5bdc7904e769df399cd055`.
- Corpus: `96555c4a63378fd965caf93c761b93110168caea5a2a03e1939c68c778a93cd7`.
- Design: `3e474dd0bcacda89b6fca863fda59c019066da3664b6ef17312c00ef55da9c2a`.
- Source: `07be2d7b124fc4470de568b559a7918d0111802c69d2cfbe144fdccbcb7ec75c`.
- Runner: `2a5324ffb2ce66026327f6f1e82b75ff33729c29f09bf1f12cf0602b26ca310f`.
- Output: `6c8571ef2e851d5cec1c31314887f35932a22ef1de10dcff7e7b40a0cfa572bf`.
- Log: `00249d4de1531ca44b37fd6af2392310586c746d502ff95423bfd0d068d06e66`.

No durable ledger was edited.
