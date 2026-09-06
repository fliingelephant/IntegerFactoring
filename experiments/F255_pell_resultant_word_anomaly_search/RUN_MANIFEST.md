# F255 run manifest

## Frozen inputs

- `PREREGISTRATION.md`:
  `6f5c61b09d01b5a17b3a2d54558ac828732d660f4024e826fee70177c14bc67c`
- `PRELAUNCH_MANIFEST.md`:
  `f1d30bbaa71c09a4e03c659ccce3ff23c055068cab909a15ce61198dfb45e439`
- `search.cpp`:
  `b207e826311792aff8e1a74c87e23011a9bbde4e011a0eda43be94ef10548cd2`
- `remote_run.sh`:
  `6477c8899881629955d781de39b94ec9780314eb5c0ee3931f1ca81aa0e3cd70`

The prelaunch manifest states that the remote image initially lacked Boost
headers, that the user explicitly authorized the dependency installation,
and that `libboost-dev` 1.74 was installed before compilation. It freezes an
eight-worker run under `nice -n 15`.

Remote timestamps place `search.cpp`, `remote_run.sh`, `PREREGISTRATION.md`,
and `PRELAUNCH_MANIFEST.md` at approximately `2026-08-13 21:09:17–18 +0800`.
The compiled binary is timestamped `21:17:08 +0800`, and the output artifacts
are timestamped `21:19:29–30 +0800`.

## Copied remote artifacts

- `output/F255-D01.json`:
  `955c0b4776ae8bbd2fca82a24b2dd86262c93f5ccabc40ecbe296e587e69af9e`
- `output/F255-D01.tsv`:
  `35054d382c31dd2777da5e3cd2e8e67172642150d55d5a06aaa9f243ea1a5873`
- `logs/F255-D01.stdout`:
  `dd698f2052f5fc986934ce704324146a7b3941a5fc9cd12062b8edd317cca3c2`
- `logs/F255-D01.stderr`:
  `230109af6d114c0504ad1b113bf45a2e089e26469c6db605e07810ab1d6ea3ed`
- `logs/F255-D01.manifest`:
  `7fff875ad068b53b40cb9eb36981ebeb43c9b89f8d038a8ea6a9c1c0163d6b26`

The live remote files and copied local files have identical hashes. The
remote run manifest records:

- compiled `search` binary:
  `77fecee76df2dbfa1b93e1430299045770541a12c46824be65178068100f2bfb`;
- start: `2026-08-13T13:17:08Z`;
- end: `2026-08-13T13:19:30Z`;
- exit status: zero.

The stdout contains the PASS record with 50,304 inputs and 139.224 elapsed
seconds. The stderr contains progress records through `50304/50304` and no
failure record.

The available artifacts do not identify who launched the runner. Launch
ownership is unknown. This provenance limitation does not change the byte
authentication above.

## Review state

`RESULT.md` contains an independent source and artifact verification. It is
not the fresh hostile audit. A separate reviewer must audit the frozen packet
before any durable promotion.

The run is finite discovery evidence only. It supports no asymptotic claim.
