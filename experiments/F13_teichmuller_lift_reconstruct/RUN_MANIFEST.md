# F13 reconstruction run manifest

## Scope and blindness

- Working directory: `/Users/zhou/autoresearch/IntegerFactoring`
- Fresh experiment directory: `experiments/F13_teichmuller_lift_reconstruct`
- Inputs used: the bare task statement and the supplied repository instructions
- Forbidden candidate directories opened: none
- Canonical project files opened or edited: none
- Prior or derived F13 artifacts opened: none
- Web sources used: none
- Subagents used: none
- Commit created: no

The reconstruction and checker were produced independently from the bare statement.

## Environment

- Python: `Python 3.14.5`
- Timeout utility: GNU coreutils `timeout 9.11`

## Named sources and retained artifacts

- `RESULT.md`: complete independent proof and scope audit
- `verify_reconstruction.py`: final exhaustive finite checker
- `verification_output.json`: structured final certificate
- `verification_run.log`: retained final stdout/stderr
- `explore_high_digits.py`: first enumeration of additive and iterate behavior
- `explore_high_digits.log`: retained exploratory stdout/stderr
- `inspect_high_digit_events.py`: directional high-digit-difference exploration
- `inspect_high_digit_events.log`: retained exploratory stdout/stderr
- `SHA256SUMS`: SHA-256 hashes of all proof, source, output, and log artifacts above

## Timed commands

All executable experiments used an external wall-clock timeout and a named source file. No inline Python or stdin-fed program was used.

### Initial enumeration

```text
set -o pipefail; /opt/homebrew/bin/timeout 30s python3 experiments/F13_teichmuller_lift_reconstruct/explore_high_digits.py 2>&1 | tee experiments/F13_teichmuller_lift_reconstruct/explore_high_digits.log
```

- Exit status: `0`
- Result: completed within `0.1 s`

### Directional-event exploration

```text
set -o pipefail; /opt/homebrew/bin/timeout 30s python3 experiments/F13_teichmuller_lift_reconstruct/inspect_high_digit_events.py 2>&1 | tee experiments/F13_teichmuller_lift_reconstruct/inspect_high_digit_events.log
```

- Exit status: `0`
- Result: completed within `0.1 s`

### Final certificate

```text
set -o pipefail; /opt/homebrew/bin/timeout 60s python3 experiments/F13_teichmuller_lift_reconstruct/verify_reconstruction.py --output experiments/F13_teichmuller_lift_reconstruct/verification_output.json 2>&1 | tee experiments/F13_teichmuller_lift_reconstruct/verification_run.log
```

- Exit status: `0`
- Result: `PASS: all assertions passed`; completed within `0.1 s`

The final checker exhausts all unit residue classes for its listed pairs. It includes the exceptional twin `(3,5)`, ordinary twins through `(29,31)`, non-twin balanced pairs through `(23,43)`, and the noninvertible quotient example `(3,7)`.

### Hash generation

```text
set -o pipefail; /opt/homebrew/bin/timeout 10s shasum -a 256 experiments/F13_teichmuller_lift_reconstruct/RESULT.md experiments/F13_teichmuller_lift_reconstruct/verify_reconstruction.py experiments/F13_teichmuller_lift_reconstruct/verification_output.json experiments/F13_teichmuller_lift_reconstruct/verification_run.log experiments/F13_teichmuller_lift_reconstruct/explore_high_digits.py experiments/F13_teichmuller_lift_reconstruct/explore_high_digits.log experiments/F13_teichmuller_lift_reconstruct/inspect_high_digit_events.py experiments/F13_teichmuller_lift_reconstruct/inspect_high_digit_events.log 2>&1 | tee experiments/F13_teichmuller_lift_reconstruct/SHA256SUMS
```

- Exit status: `0`
- Result: completed within `0.1 s`

The hashes were then verified with:

```text
/opt/homebrew/bin/timeout 10s shasum -a 256 -c experiments/F13_teichmuller_lift_reconstruct/SHA256SUMS
```

- Exit status: `0`
- Result: all eight listed artifacts reported `OK`

## Preserved failed route

The directional-event exploration tested a possible proof of a bound for *differences* of consecutive high digits by bounding events per fixed CRT component. The retained output refutes that route: for `(17,19)` it finds three `p`-only events in one fixed-`p` fiber, and for `(19,23)` it finds three `q`-only events in one fixed-`q` fiber. No such per-fiber claim appears in `RESULT.md`.

The successful high-digit proof instead concerns the direct gcd of each canonical `H_r`, exactly as scoped in `RESULT.md`, and counts canonical representatives of Teichmüller residue classes. The consecutive-*iterate* difference theorem is separately proved for `A_{r+1}-A_r`.

No timed run failed or timed out.
