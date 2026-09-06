# F258-D01 result

Status: **TIMEOUT BEFORE MATHEMATICAL OUTPUT**.

The unchanged frozen runner started at `2026-08-13T13:27:10Z` and ended at
`2026-08-13T17:27:10Z` with exit status `124`, exactly at its four-hour
limit.  The Python process used one low-priority core at approximately 100%
CPU and about 31 MiB RSS throughout.  It remained in deterministic serial
cohort construction and never reached the eight-worker scan.  It created no
summary or row file.  Both captured streams are empty.

This is a workflow and implementation result only.  It supplies no finite
mathematical evidence for or against the F257 ticket law.  F258-D01 is not to
be rerun or translated to C++ under the D01 label.

Authenticated remote artifacts:

```text
REMOTE_D01/F258-D01.manifest
  7c374a323cd924e0cfb5530d21049d3b08e2d200fa5029e994e3cd4eb0c65c31
REMOTE_D01/F258-D01.stdout
  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
REMOTE_D01/F258-D01.stderr
  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The manifest reauthenticates the frozen input hashes:

```text
PREREGISTRATION.md  1b6c7d04141a2c4b2b8b5aeb218f7754eb5e86177df72097a0e8802e1a4db9ec
scan.py              778ac8ad5a8728a52737a6c20da6771523c1ffd53b1a5649c5002da56409e005
remote_run.sh        6ac03c66d00d9cd914e95274d02d9a350581b397ea35c34dc59074ee97343aa7
```
