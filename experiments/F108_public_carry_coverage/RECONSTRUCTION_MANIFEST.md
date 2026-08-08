# F108 proof-blind reconstruction manifest

## Scope boundary

The reconstruction read only these authorized pre-existing files:

```text
23c0b4dbd7c16605d12a00c00f91997cb5125c00be8906af79a4a16c8bd2bcae  RECONSTRUCT_STATEMENT.md
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
```

It did not read any other F108 file or any factor-assisted input. It did not
factor an endpoint or relation value.

## Authoritative run

```text
command=/opt/homebrew/bin/python3 reconstruction_independent_verifier.py --statement RECONSTRUCT_STATEMENT.md --public ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json --output RECONSTRUCTION_ATTEMPT_OUTPUT.json
working_directory=/Users/zhou/autoresearch/IntegerFactoring/experiments/F108_public_carry_coverage
timeout_seconds=60
elapsed_seconds=0.240549
timed_out=false
exit_code=0
verifier_status=PASS
fixed_reconstruction_verdict=PASS
general_theorem_verdict=PROVED
statement_verdict=FAIL
checks=219304
verifier_failures=0
```

The statement verdict fails only because the authorized statement omits the
F99 inverse formula that it requires the reconstruction to inspect. The
general theorem and all five fixed public claims pass.

`reconstruction_run_with_timeout.py` enforced the hard timeout. It promotes
only a successful verifier run to `RECONSTRUCTION_OUTPUT.json` and
`RECONSTRUCTION_RUN.log`. It preserves a timeout, invalid output, or verifier
failure as a timestamped `RECONSTRUCTION_FAILED_*` JSON and log pair.

The run used Python 3.14.5.

## Independent Sage rank check

SageMath 10.9 read only the factor-free masks in the reconstruction output.
It returned:

```text
full=165
represented_raw=165
all_raw=165
represented_local=54
all_local=54
```

## Reconstruction artifacts

```text
d2f3c31138834cbd521545715f13775c5f315329e5d73ba29ca5cd99aae225a3  RECONSTRUCT.md
58e9f72d21fb74eb83c6c6df5e28cb5d78031f5f0ee0149ed0373ff903996301  reconstruction_independent_verifier.py
ff0a9c46aa1ed4510c3cd0e533d756f7a5a3f99d95146efec9b98eba064f0d8e  reconstruction_run_with_timeout.py
57432c2fc59bbbb75c8ce68cb751f95de2595488928f8bb86b4b9586dedb07be  RECONSTRUCTION_OUTPUT.json
27d2ec09224cee9673fac65c3b425dda06ecbeb3b951a1a035c0de31138d90e9  RECONSTRUCTION_RUN.log
```

The canonical SHA-256 of the complete, represented-raw, all-raw,
represented-local, and all-local factor-free mask sets is:

```text
ff909525563be0b47ed74682999e700418cf9b89717afe1ffbc31892f655291b
```

## Preserved failed attempts

No verifier attempt failed. No `RECONSTRUCTION_FAILED_*` artifact was
created. No pre-existing file was edited.
