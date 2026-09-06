# F268-D03 independent hostile pre-run audit request

Audit this packet from no prior context before any target command. First
authenticate every entry in `FROZEN.sha256` and bind the verdict to the
coordinator-supplied SHA-256 of those exact manifest bytes. Do not compile
C++, execute a binary, invoke `remote_run.sh`, generate a corpus, or inspect
future output. Write only `HOSTILE_PRERUN_AUDIT.md`; it is a post-freeze audit
artifact and is not an entry in `FROZEN.sha256`.

Authenticate `PROVENANCE.md`. Independently authenticate the immutable D02
manifest root
`31e05f0f310ff6f0b37421ccf68634bf57bce65cb708074408dec96b7801561b`
and its post-freeze hostile `FAIL` record hash
`1b2c37510ec4680d0c8996d3654108e8727e9a44e92acf8523c550b79735a7b0`.
Confirm that D02 has no dynamic output. Reproduce its exact marker attempt-law
and overlap-gate failures. Compare D03 against D02 and reject any change beyond
the marker-cap alignment, conservative all-F265-token overlap rule,
packet/output version change, corrected D03 template-version sentence, and
frozen provenance/status/audit metadata.

A passing file must contain these exact standalone lines:

```text
# Verdict: PASS
frozen_manifest_sha256: <coordinator-supplied digest>
```

Reconstruct the packet from first principles and try to give one strict
`FAIL`. Give `PASS` only if every item below survives.

1. Prove the canonical scalar-section root law for
   `U_E(a)=[a^E]_(N^2)` and `Y_E(a)=[a^(E/2)]_N` for all five frozen even
   exponents. Check positivity, canonical ranges, and coprimality with `N`.
2. Re-derive every exact multiplication, inverse, power, and complement
   quotient identity. Check exact divisibility, signs, unit multipliers, and
   every claimed gcd equality. Confirm that these controls never enter P66.
3. Prove the complete rational support-two test: for `g=gcd(u,v)`, `uv` is a
   square exactly when `u/g` and `v/g` are squares, with root `g*s*t`.
   Check that every singleton and unordered pair is classified and certified.
4. Check the freeze-critical chronology in prose and source: build and
   use stage-1 source gcds to authenticate the full public bank first; finish
   direct stages 2 through 4 without modifying it; classify every exact
   singleton and pair next;
   retain and count every useful low-support factor
   certificate; insert only verified global-sign decoys into the quotient;
   authenticate the complete P66 kernel; and emit residual support-at-least-
   three relations only on the no-useful-low-support branch. No useful pair
   may be discarded, quotiented, or relabelled as residual. If a later P66 or
   evidence cap rejects the bank, check that every completed low-support
   record and every useful certificate survive in replayable evidence while
   the bank remains neither eligible nor null.
5. Reconstruct the gcd-free P66 block refinement, exact exponent-vector
   reconstruction, square-block treatment, parity matrix, binary kernel,
   global-decoy span, quotient-basis dimension identity, product square,
   exact root, supplied root, normalized root, and both signed gcds. Check
   replay validation independently recomputes all of them and all frozen
   template predicates.
6. Compare the seam against P211/F247, P212/F245, P213/F248, P66/P138,
   F262, F264, F265, F266, and the F26 canonical-inverse endpoint route.
   Reject duplication or any claim broader than a finite canonical scalar
   section and retrospective nonduplicate multirow search.
7. Check every family and template in `FAMILY_SYNTAX.tsv` against the C++
   implementation. Verify the staged tier exactly: all 12 discovery families
   have 20/24 rows and only four authenticated heldout families have 45/48
   rows. The last column must advertise the real 45/48 grammar maxima, not an
   obsolete 64/72/90/96-row maximum. Complete low-support testing must remain
   inside every eligible bank.
8. Audit the information firewall. Source generation must receive only `N`,
   family syntax, a frozen row target, and public gcd outcomes. Discovery
   aggregation and ranking must receive only arithmetic `BankResult` values,
   not `Case`, shape, factor bits, `p,q`, markers, or hidden labels. The search
   `Case` has no secret fields. Labels are mode 600 and enter only through the
   separate post-heldout auditor. Check selection and family-syntax digest
   authentication before heldout and the exact rank-prefix replay.
9. Check the random, nonconsecutive-neighbor, safe-safe, and bounded
   P209/F244 four-marker constructors. Verify deterministic 64-bit primality,
   exact factor bits, balance, global modulus uniqueness, shifted gcd table,
   four distinct marker primes, cross primitive-root tests, bounded attempts,
   explicit marker shortfalls, and post-run label verification. In both prose
   and source, require exactly two requested marker rows per registered cell,
   4,096 seeded pair attempts per requested row, and 128 candidates per
   congruence-class prime request. Check the resulting upper bound of
   1,048,576 constrained-prime candidate tests per requested marker row. Do
   not substitute the 200,000-candidate ordinary-prime cap.
10. Audit all caps and resource dispositions. In particular check source
    exhaustion, rows, row bits, gcd-free steps, blocks, low relations,
    quotient relations, relation bits, evidence bytes, workers, aggregate
    output, memory, disk, load, process overlap, and the packet deadline.
    A cap crossing must be `RESOURCE_REJECT`, never a null bank. Verify that
    `refuse_overlap` rejects every process command containing `F265` or
    `f265`, including packet paths, corpus, search, label-audit, validator,
    compiler, preflight, and runner commands. Verify that its bracketed grep
    expressions do not match the grep process itself and that the gate runs
    before target creation and before every target phase.
11. Recompute the maximum staged scale with all marker rows present:
    3,440 banks and 1,942,040 row-pair bundles. Check the compiled F265-D02
    observation `2,369,895 / 3,316.220420 = 714.637358152448` pair bundles per
    wall second. The C++ gate must take the maximum of the two measured F268
    projections and the twice-safety F265 empirical floor, include complete
    real corpus generation, use the largest real 45/48-row banks, gate RSS
    against the measured peak and `512 MiB + 4*projected output`, gate
    projected output, require zero preflight rejects, and require one completed
    48-row bank.
    Its timed path must actually construct the source grammar, exponentiate
    every row, execute all eight stage-3 gcds per unordered pair, execute
    every singleton and support-two rational squareclass test, run P66 and the
    quotient, and serialize and replay evidence. Check the exact recorded
    row-power, singleton, pair-gcd, and support-two count identities.
12. Inspect the C++ self-tests for SHA-256, both frozen row tiers, unique
    `(base,exponent)` rows, a useful support-two certificate excluded from the
    decoy quotient and preserved across a later resource rejection, a global
    singleton admitted to it, a clean support-three quotient relation, carry
    algebra, P66 decoding, and selection re-ranking.
    Inspect the runner and validators for C++17/POSIX-only operation and no
    Python dependency.

A `PASS` authorizes only the frozen validation sequence after every F265
process has ended. It does not authorize discovery after a failed compile,
self-test, corpus, preflight, replay, digest, resource, or output gate. Any
future result is finite evidence only.
