# Frozen-layer reconstruction manifest

## Isolation and method

The reconstruction read only these supplied files:

1. `RECONSTRUCT_STATEMENT.md`
2. `RECONSTRUCT_LAYER_STATEMENT.md`
3. `RECONSTRUCT_INPUT.json`

It did not read another F111 file or any F98, F109, or F110 file. All new
files use the `RECONSTRUCT_LAYER_` prefix. The implementation uses no
factorization routine, primality routine, known factor, or endpoint prime
factorization.

Large integers are hashed as an 8-byte big-endian byte-length followed by the
minimal unsigned big-endian payload. A sequence ends with its 8-byte item
count. Matrix rows and kernel vectors use fixed-width little-endian bitsets,
followed by the matrix width and item count. Thus no digest depends on a
decimal conversion limit.

## Sources and evidence pins

| File | Bytes | SHA-256 | Role |
|---|---:|---|---|
| `RECONSTRUCT_STATEMENT.md` | 4,869 | `e1a573feaceb2465d599df21a41b46372c25c6c30cb15ad7d1b6c56230fe0dae` | permitted public specification |
| `RECONSTRUCT_LAYER_STATEMENT.md` | 3,099 | `4c8cfa6df11ec04e428a54335f51444fc79a012629fc0f4fa8fd869a62585722` | permitted layer specification |
| `RECONSTRUCT_INPUT.json` | 3,835 | `8622024473bd602d1d4928fad959099db1ae463e9bd736b7b6ec59fbb99c3f61` | permitted public input |
| `RECONSTRUCT_LAYER_decoder_v1.py` | 25,782 | `b8435179093f9121d7ab9ca6c5949e7816351c34cc85d4973cbc65bae6ae80f8` | independent attempt 1 source |
| `RECONSTRUCT_LAYER_run_with_timeout.py` | 2,588 | `1e24539abda9b10c72ea2172dcb3472004a80b4c76cce11678509839f24c69b1` | named timeout runner for attempt 1 |
| `RECONSTRUCT_LAYER_RUN.log` | 2,022,921 | `e38f4035557cce963bebda4e195b04abc580261c8fb2a8ee83ffe366c58117a1` | attempt 1 live log after failure |
| `RECONSTRUCT_LAYER_FAILED_20260808T034025Z_EXIT_1.log` | 2,022,921 | `e38f4035557cce963bebda4e195b04abc580261c8fb2a8ee83ffe366c58117a1` | preserved attempt 1 failure |
| `RECONSTRUCT_LAYER_decoder_v2.py` | 1,794 | `12a24643fa9df6b8ad03106d9a562b823b4029223cf2a26f1c5e75ab23f6f3e2` | versioned nullspace correction over preserved v1 |
| `RECONSTRUCT_LAYER_run_with_timeout_v2.py` | 2,539 | `b3f498dfe624ba83c036f1ad0b06b7b9c9cabbaf3e3feee8394df5ac2f1529b6` | named timeout runner for attempt 2 |
| `RECONSTRUCT_LAYER_RUN_V2.log` | 2,023,015 | `1e497c692b1c5dbde63576a9b2962da053d6a8e9951b0a8dd6a43e966e100b33` | successful complete run log |
| `RECONSTRUCT_LAYER_OUTPUT.json` | 10,982 | `57d6d2f5fc7b0f7de63de1d9c7c7b889b79b4e6daa263e1078ee37173fb2b22d` | machine-readable result |
| `RECONSTRUCT_LAYER_REPORT.md` | 4,580 | `7e5ffb9f02ba3957b443f82324dcecddbba450c6cf960ba0fd312e1677f2eec4` | human-readable result |

This manifest is not self-hashed. All computation sources, supplied inputs,
logs, failure evidence, and outputs that it indexes are pinned above.

## Commands and elapsed times

The primary attempt-1 command was:

```text
python3 experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_LAYER_run_with_timeout.py
```

Its named hard timeout was 3,600 seconds. It exited with code 1 after
232.139557 seconds. It had completed and validated the 13,284-block basis.
It then failed the decoder's kernel-orthogonality assertion. The runner copied
the full log to the timestamped `RECONSTRUCT_LAYER_FAILED_*` file.

The nullspace correction was checked on 1,200 deterministic random binary
matrices. Each check verified dimension, row orthogonality, and basis
independence. The command used Python `-B`, seed 0, column counts 1 through
12, and 100 matrices per count. Its output was:

```text
synthetic binary-kernel checks passed
```

The primary successful command was:

```text
python3 experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_LAYER_run_with_timeout_v2.py
```

Its named hard timeout was 3,600 seconds. The child command is recorded in
`RECONSTRUCT_LAYER_RUN_V2.log`. It exited with code 0 after 229.300478 seconds.
The decoder's measured elapsed time was 229.236753 seconds.

After the run, a read-only JSON consistency command verified all of these
identities:

```text
frozen attempts = retained frozen records + frozen duplicate residues
raw frozen values = normalized columns + removed units + removed repeats
total attempts = seed attempts + frozen attempts
total retained = seed retained + frozen retained
sign screens = 2 * total retained
kernel dimension = columns - rank = number of reported basis roots
```

It also checked every reported root residue and terminal gcd, the PASS
verdict, and the no-factor result. Its output was:

```text
output consistency checks passed
```

Read-only `wc`, `sed`, `tail`, and `shasum -a 256` commands measured,
inspected, and pinned only the three permitted inputs and the prefixed files
listed in this manifest. Interactive session polls produced no file content
and made no changes.

## Internal result pins

| Object | SHA-256 |
|---|---|
| seed basis block sequence | `ddd488cce7eafa3337e88db9bd164d6c42ea70291d8a014caaeeabf52655321d` |
| frozen record sequence | `90837c4b18ff70c2965260fbbe65fccf795fbefaece47340945b59d4e206d7a3` |
| normalized exact-value sequence | `e1fc0932563a1abeb71174fe107770b93f0da0b3dae6c4e677f28204dd119248` |
| exact-value basis block sequence | `8c572d9ad42b375cf4ef8e2a840662d19a36445a551e775daa818b47c72755c0` |
| public parity rows | `438b1f129185a20e773cb783e2cc8b16aad2dd77d3694862add96276ac2e0dd3` |
| full kernel basis | `56c211cc0fdec093e0bbd135692ebeca287f0b3ffc8c37f5528d4bf2759404c0` |
