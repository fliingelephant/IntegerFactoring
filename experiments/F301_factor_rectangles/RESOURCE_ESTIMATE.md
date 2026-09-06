# Resource estimate

Checked 2026-09-07 before the pilot.

- Host load average: 2.11, 2.07, 2.02.
- System-wide memory free: 74% of 16 GiB.
- Swap I/O: zero swap-ins and zero swap-outs.
- Process inspection through `ps` and `top` was blocked by the local sandbox.
- One Python process is used. No external package or service is used.
- The exhaustive range has 4,095 inputs. The 120-input reference corpus is
  at most 24 bits. Its oracle scans odd `x` values directly.
- The 40 large coverage cases generate boxes only; they never call the
  numerical reference oracle.
- Estimated runtime: below 15 seconds. Source alarm: 60 seconds.
- Estimated peak memory: below 128 MiB. Hard planning cap: 256 MiB.

The reference enumeration cost is intentionally retained as a counter. It is
not an estimate for a succinct oracle.
