# F269-D02 provenance

## Theory source

The immutable sixth theory drafts remain byte-for-byte:

- `DRAFT_ALGEBRA.md`: SHA-256
  `9bf47b7c8facea2e6d23f8d07ca6b76a433c8ee9b3f314cfc40454e51c29e0ab`.
- `DRAFT_PREREGISTRATION.md`: SHA-256
  `9179b7fe4b24f9be80a9c75afbbaed60ac432d98a31c2268726aacf22debde8b`.

The sixth fresh hostile theory review returned `PASS` in the parent
conversation before D01 implementation. It created no artifact and therefore
has no artifact SHA-256. D02 does not invent one. D02 preserves the D01
algebra, expression grammar, cohort construction, selection orders, and
finite verdict definitions.

## Failed D01 implementation state

The exact failed D01 frozen-manifest SHA-256 is
`a1d6d3493ffac3a68bee992fd524a94a8e68db7294a52c650f679ae504d4486b`.
Its fresh hostile pre-run audit is preserved here as
`D01_HOSTILE_PRERUN_AUDIT.md`, SHA-256
`35d269675310a4dc10b85f562d5d8480c9f5b209f3d97bf95201dec79e869b5b`.
The original D01 directory remains unchanged.

That audit returned `FAIL` for exactly eight operational defects: semantic
outputs were charged as 8 MiB sidecars; F265 exclusion was narrow; the
process-shared checked ledger and reserved failure writer were absent; the
final log hash was stale; writable `cgroup.kill` was not mandatory; external
commands were not completely gated; maximum-work used substitute aggregate
arrays; and grammar repetitions omitted the complete mask evidence.

## D02 repair boundary

D02 changes only the implementation/resource boundary needed to close those
eight findings. It splits mixed physical outputs for independent semantic
caps. It uses a process-shared flock-backed ledger for source writes, shell
text, command stdout/stderr, compression temporaries, replacement, and final
hash closure. Its exact failure writer alone owns the last 1 MiB. It requires
writable `cgroup.kill`, performs a generic in-process F265 argument scan, and
gates every external command and used GNU option. Its maximum-work fixture
allocates and updates the literal production aggregate types. Every grammar
repetition emits and authenticates the full root-attempt mask and all retained
control-case masks.

The user approved implementation without `/simplify` and without a commit.
No D02 source was compiled or executed locally or remotely. No self-test,
stress preflight, discovery cohort, heldout cohort, or compression ran. A
fresh hostile static audit must authenticate the D02 frozen manifest before
the runner can compile.
