# F222-D01 run manifest

## Status

The frozen run completed on 2026-08-13 in 16.707 seconds.  It used one remote
Python process under the declared 900-second timeout and 2-GiB address-space
cap.  No retry or source change occurred.

## Frozen inputs

- preregistration:
  `5af81584198083adbf59cec31b072e438e9671bc93ff8cfe8e2314147c28a569`
- source:
  `d2cc2ce1a39228eecc3d407d40368b536ff8067389eb6974998b9b56e616a31d`
- runner:
  `9a13859e837994157a46cb801c5f8a79d820e8b2273326099584d021b54a6c51`

The remote source and runner hashes matched before launch.

## Runtime and command

- host alias: `seetacloud`
- remote directory: `/root/IntegerFactoring_F222/F222-D01`
- runtime: `/root/miniconda3/bin/python`, Python 3.12.3
- dependencies: Python standard library only
- concurrency: one process

The runner invoked exactly:

```text
timeout 900 /root/miniconda3/bin/python \
  /root/IntegerFactoring_F222/F222-D01/scripts/F222_D01_coefficient_search.py \
  --output /root/IntegerFactoring_F222/F222-D01/output/F222-D01.json \
  --p-limit 500
```

The shell applied `ulimit -v 2097152` before this command.

## Outputs

- JSON: 485,408 bytes,
  `cebb7a614c1af895bb820e5e4bfadfae6afd16aa8502ab1829220ff0a275ec32`
- log: 152 bytes,
  `526081803458be4f8fd518ad1b0338d7e287120ca8848c138803b1380faf99c6`

Remote and local hashes agree.  The JSON status is `complete`; its internal
direct-formula validation passed.

