# Resource and reproduction record

Estimate before execution: one Python process, under 60 seconds and 128 MiB.
The source installs a 60-second alarm. The exact domains have M at most 128
and K at most 18. Moment tables have at most 648 entries; rational arithmetic
is performed without numerical approximation.

Preflight on 2026-09-07 at 06:53 local time: `memory_pressure -Q` reported
68% available; `uptime` reported load averages 1.98, 2.18, 2.23. No new
parallel mathematical process was launched by this worker.

Command:

    python3 experiments/F302_resolvent_lift/pilot.py > experiments/F302_resolvent_lift/run.log 2>&1

Measured: 0.0656845 seconds, peak RSS 17,858,560 bytes on macOS.
All checks passed. `output.json` stores exact rational poles, error bounds,
state counts, enumeration work counts, and diagnostic values.
