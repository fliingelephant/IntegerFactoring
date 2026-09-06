# F194 V3 focused hostile metadata re-audit

## Exact verdict

**PASS.**

The V3 metadata package is internally consistent. It reuses the exact V2
mathematical bytes that passed the prior hostile reconstruction, excludes the
defective V2 provenance from the V3 input set without altering or deleting
it, and replaces the sole four-versus-five defect with an accurate five-item
provenance list. No new inconsistency was found.

This is a focused metadata verdict. It does not replace the separate strict
statement-only reconstruction still required by `V3_MANIFEST.md`.

## 1. Manifest and frozen-input hashes

`V3_MANIFEST.md` was read first. Its own observed SHA-256 is

```text
f93d0b7db626755cc9195104df3dcc8de2fdcd6dca21047c90252469714ae404
```

Every hash it declares matches the current file bytes:

| V3 input | Manifest SHA-256 | Observed SHA-256 | Result |
|---|---|---|---|
| `V2_STATEMENT.md` | `95764227ebc288a528c7425c5593e9a75d7ad9030556c4a9c12b00c0c85f48ab` | `95764227ebc288a528c7425c5593e9a75d7ad9030556c4a9c12b00c0c85f48ab` | match |
| `V2_PROOF.md` | `ea19a8a5fe2410e24841876a5b04c4e6e23e4f9f466838e0a9ebaf83ffcbb029` | `ea19a8a5fe2410e24841876a5b04c4e6e23e4f9f466838e0a9ebaf83ffcbb029` | match |
| `V2_SELF_AUDIT.md` | `3b04854c356f7076841e47e088aff34b2007cc503400996e7efc011144bb8dbb` | `3b04854c356f7076841e47e088aff34b2007cc503400996e7efc011144bb8dbb` | match |
| `V3_PROVENANCE.md` | `3d45bd68212f8231048e3fb7eb93d5e41a58da55c9cb075747d6d1c687d50c32` | `3d45bd68212f8231048e3fb7eb93d5e41a58da55c9cb075747d6d1c687d50c32` | match |

The first three values are exactly the hashes frozen in V2. Hash equality
establishes that no statement, proof, or self-audit byte changed between the
V2 mathematical package and V3.

## 2. Prior mathematical verdict

The preserved `V2_HOSTILE_REAUDIT.md` has SHA-256

```text
1e48b4c793a5502c2ada9d1058d8252d239487703cc99dbf53381da65b397385
```

which matches the value stated in `V3_PROVENANCE.md`. Its exact disposition
was:

- **PASS** for the V2 mathematical statement-and-proof pair;
- **FAIL** for the exact V2 package solely because its provenance said four
  repairs while the self-audit listed five.

That re-audit found no other promotion-blocking mathematical defect. Since
V3 reuses byte-identical mathematical inputs, the prior mathematical pass
continues to apply. V3 introduces no new mathematical claim or proof text to
re-audit.

## 3. Exact repair of the package defect

The preserved V2 defect was the sentence that V2 made “only the four repairs
listed” in a file that visibly listed five. V3 does not overwrite that
historical file. Instead:

1. `V3_MANIFEST.md` explicitly excludes `V2_PROVENANCE.md` from the V3 input
   set and identifies `V3_PROVENANCE.md` as the sole replacement input.
2. `V3_PROVENANCE.md` accurately describes the V2 package failure as the
   four-versus-five mismatch.
3. It then states that there were five repairs and enumerates exactly five:
   the central-binomial inequality, Boolean cyclic incidence, numerical-QP
   gap bound, joint coefficient/carry residues, and removal of unsupported
   holonomic-algorithm language.
4. The five-item list agrees with `V2_SELF_AUDIT.md` and with the findings in
   the prior V2 hostile re-audit.

Thus the sole failed metadata assertion is removed from the active V3 input
set and replaced by a correct assertion. The repair does not conceal or
mutate the failed V2 package.

## 4. Cross-reference consistency

The two historical audit hashes recorded in `V3_PROVENANCE.md` both match
the preserved files:

| Historical audit | Provenance and observed SHA-256 | Result |
|---|---|---|
| V1 hostile audit | `a3f49a53f54ac7bb69488958e7b1141d2206c61a834ef28bdd6e6c46d1be5fb9` | match |
| V2 hostile re-audit | `1e48b4c793a5502c2ada9d1058d8252d239487703cc99dbf53381da65b397385` | match |

The old defective `V2_PROVENANCE.md` remains preserved with its previously
recorded SHA-256

```text
a7d5e7fdddfe9688797cf5bb0052ae12d4278d04eddb8df1fd3e995059077a61
```

but is not named as a V3 frozen input. This agrees with both the V3 manifest
and V3 provenance. There is no conflict between preservation of V2 as
history and exclusion of its defective provenance from the new package.

## 5. Scope of the pass

The following claims are verified by this focused re-audit:

- all V3 manifest input hashes match;
- all three reused V2 mathematical files are byte-identical to the files
  that received the prior mathematical pass;
- the prior hostile re-audit's verdict and digest are represented accurately;
- the four-versus-five provenance defect is exactly repaired;
- all repair counts, lists, exclusions, and historical audit hashes in the
  new metadata agree;
- no new mathematical byte or metadata inconsistency was introduced.

Accordingly, the V3 package passes the required focused hostile metadata
re-audit. The manifest's independent statement-only reconstruction remains a
separate verification gate and is not asserted complete here.
