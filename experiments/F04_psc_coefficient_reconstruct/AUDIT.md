# Self-audit record

## Verdict

`run_001` passed every mathematical stage.  The reconstruction is
**self-audited**, not cross-family or human audited.

The complete verifier found:

* 2,942 global vectors and 8,687,726 canonical global coefficients;
* zero nonunits and zero degree-2952 failures;
* zero Euclidean-chain failures over either prime field;
* 8,687,726 nonzero determinant statuses per field and 17,375,452 total, after
  applying the proved determinant criterion.

The exact global-vector SHA-256 digest is
`675a90c112edd2f5bbef94af674cc3101813d878aa568a064cdff3f144649e86`.

## Execution audit

The source/executable hashes in `manifests/run_001.inputs.sha256` were written
before `run_001`, checked at its start, and checked again after completion.
There are no `run_001_<stage>.failure.txt` files.

Stage results:

* complete trial division certified `p`, `q`, and `r` prime and checked
  `pq=N`;
* exhaustive small-field testing checked 231,494 literal determinants from
  80,302 polynomial pairs, including 17,700 positive-gcd cases and 13,352
  abnormal-gap cases;
* global generation took 17.9704 seconds;
* the complete two-field Euclidean verification took 10.9211 seconds;
* the independent Python artifact parser reread all 8,687,726 stored
  coefficients and all 2,942 per-shift result rows;
* a distinct direct-composite-modulus power path compared 11,812 coefficients
  at shifts `1,2,1471,2942`, and FLINT's general remainder routine independently
  checked the eight corresponding field chains.

The complete chain checker uses the exact two-coefficient quotient that must
occur when consecutive degrees differ by one.  It stops and records the first
actual smaller degree if the expected leading remainder coefficient vanishes.
Thus it cannot silently skip an abnormal drop.  The separate FLINT remainder
checks exercise a different implementation on the fixed audit sample.

## Dispositions and deviations

An initial build invocation failed with status 126 because the newly written
shell file did not have its executable bit set.  The failed log is retained as
`logs/build.log`; `bash scripts/build.sh` then compiled the unchanged sources
successfully before the pre-run manifest.  This was a build-launch failure, not
a mathematical execution.

Before the named sources existed, one incidental `python3 -c` command printed
the three residues `p mod r`, `q mod r`, and `N mod r`.  It did not generate a
polynomial or check any finite claim, is not an evidentiary dependency, and was
replaced by the named, timed `src/preflight.py` run.  It is disclosed here
because the requested workflow otherwise forbids unnamed computations.

The first `manifests/run_001.final.sha256` is quarantined as a packaging
failure: the runner included that manifest itself while shell redirection was
writing it, so its self-entry is necessarily stale.  This does not affect
`run_001.inputs.sha256`, `run_001.outputs.sha256`, or the artifact audit (which
uses the primary-output manifest).  `audit_fix_001` creates and verifies a
self-excluding `run_001.complete.sha256`; its plan, sources, and outcome are
separately preserved.

## Independence limits

This is one author's reconstruction.  The generator and complete verifier are
separate executables, and the audit uses alternative direct-power, generic
remainder, exhaustive-determinant, and Python parsing paths, but they ran in
the same software environment.  No fresh hostile agent, different model
family, or human has audited this directory.  The highest honest status of the
artifacts themselves is therefore `self-audited`.

