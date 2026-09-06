# F264-D01 prelaunch manifest

Status: frozen and target-compile validated. Execution validation is pending.

Reserved experiment ID: `F264-D01`.

The complete C++17 source and runner are present. Target compilation passed
with `/usr/bin/g++ -std=c++17 -O2 -pthread` on `seetacloud` and emitted no
diagnostic. F258-D01 remained active, so the declared incompatibility gate
prohibited every execution mode.

Frozen source facts:

```text
C++ source lines: 1,429
static families: 30
reduced main words per input: 8,744
P205 words per input: 467
planned inputs: 5,280
threads: at most 8
virtual-memory limit: 4 GiB
uncompressed-output limit: 1 GiB
hard cohort deadline: 14,400 seconds
```

The static operation forecast per input is about 8,744 word multiplications,
2,048 pair scopes, 512 triple scopes, 2,048 commutator scopes, 36 smooth-order
trials, approximately 11,000 synthesized gcd residues, and 467 P205 words.
The output forecast is below 256 MiB before compression, dominated by the
5,280-by-467 residual table and candidate aggregate JSON. The authoritative
60-bit full-pipeline benchmark remains mandatory after incompatible jobs end.

Target resources observed at `2026-08-13T15:37:55Z`:

```text
32 allowed CPUs (96-127)
load average 57.26,57.32,57.70
503 GiB RAM; 367 GiB available; no swap
22 GiB free disk
F258-D01 active at nice 15
```

The hashes are recorded in `FROZEN.sha256`. The runner must satisfy every gate
in `VALIDATION_PENDING.md` after all F258--F263 jobs end. A failed gate
invalidates this packet; it does not authorize a grammar or threshold change.

No mathematical run occurred. No durable ledger was edited.
