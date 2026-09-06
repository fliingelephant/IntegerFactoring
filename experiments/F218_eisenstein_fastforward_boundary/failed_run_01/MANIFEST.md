# F218-D01 failed run 01

The frozen source and preregistration were copied to
`/tmp/f218_eisenstein_fastforward_boundary_20260812` on `seetacloud` and
verified before execution.

Command:

```text
timeout 600s nice -n 10 /usr/bin/time -v python3 search.py --r-max 2000000 --bm-r-max 200000 --output RESULT.json
```

The command exited with status `127` before Python started because the
remote image has no `/usr/bin/time`.  No `RESULT.json` was produced.

SHA-256:

- frozen preregistration: `ce5bf8997c7efc46f466a3da3aec7e87d5e1207b03448b55ced9532dd1d67674`
- frozen source: `aaa64578c03289289f879c647b6ee4e1668b719d50c7908d8b0e9cd1558a8676`
- `EXIT_STATUS`: `743c7850cccfba5e53a9002663ec1ddd1079315a98bdbfdde10e6044f56abefe`
- `RUN.stderr`: `4939cc77c948270938337ed67a692628a6bede06223806df52b0853a3553fd0b`
- `RUN.stdout`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

This failed run is preserved.  A rerun without GNU `time` requires an
explicit workflow amendment under the repository instructions.
