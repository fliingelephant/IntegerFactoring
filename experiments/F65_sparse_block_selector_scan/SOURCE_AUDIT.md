# F65 hostile source-proof audit

**Verdict: PASS, with narrow evidence and scope.**

The D01 and D02 implementations enumerate the preregistered sources and menus
exactly. The gcd-free refinement is exact and does not prime-factor a block.
The exponent budgets are the full multiplicities in the retained endpoint
multiset. Candidate deduplication cannot suppress a gcd hit. The runners,
timeouts, logs, outputs, and declared hashes form a consistent completed-run
chain.

The pass does not turn a stored null into an independent certificate. F65-A01
did not re-enumerate a menu. This audit also did not rerun either scan. Thus the
nulls below are authenticated **source-run evidence**: the pinned program wrote
them after completing its enumeration. They are not proof-blind replay
evidence.

No new research computation was run for this audit. I read the source,
manifests, logs, outputs, F62 semantics, the F59 offset-source audit, and the
current artifact hashes.

## 1. Offset source and direct events — PASS

`collect_offset_relations` uses all starts `N-c` for `c=1,...,n`, where
`n=N.bit_length()`, and performs at most `n` inverse-quotient steps per start.
At each state it first computes `gcd(state,N)`. A proper gcd is recorded and
that path stops because the next inverse is undefined. If all `n` loop steps
finish, the code also checks the resulting capped endpoint. Therefore no
reachable direct nonunit event is omitted.

For every unit state greater than one, the canonical inverse gives

```text
state * inverse = 1 + quotient * N,   0 < quotient < state.
```

The strict lower bound follows because quotient zero would force
`state*inverse=1`. Hence every live path stays in `1,...,N-1`; the source never
reaches a hidden `gcd=N` case.

This is the corrected F59-D02 offset schedule. The independently audited
F59-A02 artifacts report the same D01 raw counts, quotient-unique counts, and
direct-event totals on all 12 inputs. They independently corroborate the D01
source schedule, not the F65 block menus. The two D01 direct events are exactly
the events on `N=1120697` and `N=1867141`. D02 reports no direct event on its
one input.

## 2. Gcd-free refinement and exponent budgets — PASS

The refinement starts from the public unit endpoints. When two current blocks
`a,b` have nontrivial gcd `d`, it replaces them by

```text
d, a/d, b/d
```

and removes one. This uses only integer gcd and exact division. It never uses
`p`, `q`, or prime factorization. Each old block remains an exact product of
the replacement blocks, so every original endpoint remains reconstructible.
The product of the distinct current blocks strictly decreases, so the loop
terminates. At termination the source checks every block pair for coprimality.

The source then divides every retained endpoint by every final block to full
multiplicity. It asserts that the final remainder is one. Summing these
multiplicities over the endpoint list gives the exact exponent budget of the
full retained relation multiset. Duplicate endpoint occurrences remain in that
list, so they contribute their full authorized multiplicity even though the
block list itself is a set.

The raw variant retains every nonzero source relation. The quotient-unique
variant retains the first relation for each quotient before refinement. This
can discard other public endpoint presentations, but that is the exact declared
variant. It does not make a candidate from the retained variant illegal. D02
tests only the quotient-unique variant.

The factors `p,q` construct and label the finite test inputs. They are not
passed to source collection, refinement, menu generation, or screening. Gcds
with `N` are the declared source and output screens; they are not hidden use of
the factor labels.

## 3. Exact menu semantics — PASS

All counts below are counts of distinct residues, not counts of generating
certificates.

| Menu | Exhaustive source enumeration | F62 meaning |
| --- | --- | --- |
| Current blocks | Every final block once. | A legal one-block state. |
| Legal pairs | Every two distinct blocks whose integer product is below `N`; also `q_i^2<N` exactly when its aggregate budget is at least two. | Legal divisor feedback. Taking all retained occurrences as the certifying indexed sublist supplies the recorded budgets. |
| Single-block powers | Every `q_i^e<N` for `1<=e<=budget_i`. The loop stops only after monotonic growth reaches `N`. | Legal whole-block power feedback. |
| Signed pairs | Both signs of every single block and all four sign choices on every pair of distinct blocks, reduced modulo `N`. | The support-at-most-two, exponent-`{-1,0,1}` public residue selector. It is not legal divisor feedback, and the F62 aggregate-quotient formula does not apply. |

The signed loop also tests harmless global residues if they occur. The F62
presentation can discard them. On these odd inputs they cannot pass a proper
`gcd(r-1,N)` or `gcd(r+1,N)` screen, so retaining them affects only the reported
candidate count, not any hit or miss.

Every generated residue is scanned with both gcds. Enumeration continues after
the first hit. `first_hit` is only the first stored witness; `screen_hit_count`
counts all distinct residues that pass either screen.

`self_inverse_count` excludes the global residues `1` and `N-1`, as required.
The Boolean stored on a first-hit witness tests only `r^2=1`. This is equivalent
for the declared odd inputs because neither global residue can pass a proper
`r-1` or `r+1` gcd screen.

The `seen` set is safe. If two certificates produce the same residue modulo
`N`, both gcd results and the self-inverse status are identical. Skipping the
second certificate cannot turn a hit into a miss. Every first retained
certificate is legal under the generator that emitted it.

## 4. F65-A01 scope — PASS, and no broader

F65-A01 pins the D01 source, runner, log, and output. It checks 12 records,
factor-label multiplication, sorted unique unit blocks, positive budget shape,
basic count identities, and the equivalence between a stored first hit and a
positive stored hit count. For each nonnull `first_hit`, it reconstructs the
residue from the declared block indices, signs, or exponent and recomputes both
gcd screens.

F65-A01 does **not**:

- re-enumerate any menu;
- validate every residue counted as a hit;
- independently validate an aggregate hit count or any stored null;
- check pairwise coprimality of the stored block list; or
- reconstruct source endpoints and exponent budgets from the offset
  transcript.

The pinned D01 source performs the last two checks during the run. A01 does not
independently repeat them. Its retained claim is exactly: every stored
**first-hit certificate** is valid relative to the stored blocks and budgets,
and the pinned artifacts satisfy its stated internal identities.

## 5. Runtime and artifact provenance — PASS

Both runners use `set -euo pipefail`, refuse to overwrite an existing log or
output, and invoke `/opt/homebrew/bin/timeout 300s`. Both Python programs write
their JSON with exclusive creation only after all requested menus finish. The
logs end with the final output-write message.

- D01 completed with exit status 0 and source elapsed time
  `216.68114329200034` seconds.
- D02 completed with exit status 0 and source elapsed time
  `211.9324433340007` seconds.

Both are below the declared 300-second timeout. The source, dependency, and
runner hashes match the preregistrations. The completed manifests pin the log
and output hashes:

| Artifact | SHA-256 |
| --- | --- |
| D01 source | `c7810ba32ce5d359530bf865252ee4446d4b95c29047e6e43ecbe03581c385ba` |
| D01 runner | `82d204d8d2c69b43011aa020a843feefdec081d02cfd3e2ab141c0dcbf58bd15` |
| D01 log | `5cf9dcb382afa5ca186ccd45103467d47d1585aedb72c9b4a6ba890c5b5c058c` |
| D01 output | `0d41c802e316689ea0617820535616dec55d5f331155ffbb55dcdb5599f71309` |
| A01 source | `9c5261efa88c394eda98644d504d2dacda0efe6efb8cf91140d8f32d55e5f602` |
| A01 runner | `348f56323a8fd8f4414c6e2bd7900e178b38dea2a0fb1b7f744b33caf2cd156e` |
| A01 log | `71f92dfdf74de19e07b1bc99319abae2ad0ed7a886beee8dbaa7c1718890bcbf` |
| A01 output | `b0af62734d9dc447b9fe05ff52797023a386344a3e8a6cdaa38b160f064e1ff5` |
| D02 source | `c8153e3a8ab10349c97f1e0fd724fbc17bb36a6013e4416b7cc5150b97cca2bd` |
| D02 shared D01 dependency | `c7810ba32ce5d359530bf865252ee4446d4b95c29047e6e43ecbe03581c385ba` |
| D02 runner | `b39ac2b1c7403f06eaebc4a8c5677d54d974a610bd87a05e18684d562b663ebe` |
| D02 log | `2e51413bc2b5c3365d88e22193793cd20abe5e2974b3e55d2108d97f3f398844` |
| D02 output | `9fb849478a76928dc317ef87000d709f937c84c2b79ba1fc662e188a282a8a91` |

This chain is sufficient for source-run evidence. It does not substitute for
an independently implemented replay.

## 6. Exact retained conclusions

### F65-D01

For the exact 12 declared inputs and both the raw and quotient-unique retained
transcripts:

- current blocks and all available single-block powers have zero stored source-run hits;
- legal positive pairs hit 10 inputs, including eight of the ten inputs with no direct source event;
- signed support-at-most-two residues hit all 12 inputs, including all ten inputs with no direct source event; and
- the raw and quotient-unique variants have the same input-level hit pattern.

The source-run aggregate counts are:

| Variant and menu | Distinct residues | Screen hits | Inputs with a hit |
| --- | ---: | ---: | ---: |
| Raw blocks | 13,170 | 0 | 0 |
| Raw powers | 18,960 | 0 | 0 |
| Raw legal pairs | 3,111,775 | 158 | 10 |
| Raw signed pairs | 40,456,689 | 1,989 | 12 |
| Unique blocks | 13,166 | 0 | 0 |
| Unique powers | 18,538 | 0 | 0 |
| Unique legal pairs | 3,105,251 | 158 | 10 |
| Unique signed pairs | 40,429,885 | 1,989 | 12 |

A01 independently checks only each stored first-hit witness, not these complete
enumerations or nulls.

### F65-D02 and the 61-bit null

The exact declared input is

```text
N = 1537228689631084579 = 1073741827 * 1431655777.
```

Its offset source has 2,662 raw relations, no direct event, and 2,247 retained
quotient-unique relations. Refinement produces 4,485 blocks. The pinned run
reports:

| Exact menu | Distinct residues | Screen hits |
| --- | ---: | ---: |
| Current blocks | 4,485 | 0 |
| Available single-block powers | 6,237 | 0 |
| Legal positive pairs | 2,942,006 | 0 |
| Signed support-at-most-two residues, including singles | 39,956,681 | 0 |

**The 61-bit zero-hit conclusion is trustworthy without rerunning the
39,956,681-residue signed scan, at the source-run evidence level.** The pinned
source exhausts the exact menus, does not stop early, writes output only after
completion, and the authenticated log and output record a completed run below
the timeout. No independent audit re-enumerated those residues, so the stronger
phrase “independently certified null” is not retained.

This input is a finite counterexample to a universal claim that the exact
quotient-unique offset transcript and these four exact menus must find a
factor. It says nothing about the raw transcript on this input, support above
two, mixed higher exponents, signed exponents beyond one, another source,
additional feedback rounds, a success probability, or an asymptotic
obstruction. D01's positive rates likewise do not establish factor bias or an
all-input law.
