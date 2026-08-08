# F100 run manifest

## Authoritative run

The named runner invoked the named Sage source with a hard 120-second
timeout. It read the frozen public F98 output and wrote `OUTPUT.json`.

```text
command=/usr/local/bin/sage analyze_dependency.sage --input ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json --output OUTPUT.json
timeout_seconds=120
exit_code=0
elapsed_seconds=1.998962
```

The source predates the authoritative output and log. The computation is a
factor-assisted diagnosis only.

## Failed runs

`FAILED_RUNS.md` preserves two sandboxed Sage-cache failures and the first
post-analysis JSON serialization failure. No failed run supports a claim.

## SHA-256

```text
3cca68e44691bd7e16488ba1073de471bf7dc8bae6ee1d62f87cb41a75b41c48  DESIGN.md
b22c749489acb53338b6feed4cbec333b4cfdc92fba01e0a2544006526e768f5  RESULT.md
d997608bca403b9ce9a8a1e10298317fd483fb5d63cf7b546195d8117871ed2f  analyze_dependency.sage
88c429719d757cf812719b43630ab7924f333bf1c1c8824a427de3832a9ff817  run_with_timeout.py
9bcf6217f412f837fab8e3d0b832e01c80fbd5afa1d173156ec93df95bd94076  OUTPUT.json
753dfeaa57cd985a047f7d8a6d5dbccc9da3e838132b9251202f70deada10200  RUN.log
6eba6f30220e6a56ff1bd7f4129092c828303bf257259d239159d61ed7720b4a  FAILED_RUNS.md
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  ../F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
```
