# Resource plan for the rational-nullspace follow-up

Preflight on 2026-09-07 reported 69 percent free memory and load averages
2.18, 2.17, 2.11. One Apple system process occupied one core. No numerical
process was active.

The four matrices have orders 8, 16, 32, and 64. Exact rational elimination
and three normalized null vectors per expected case are small compared with
the completed 256 by 256 finite-field run. The command retains the same hard
30-second outer timeout, 28-second internal alarm, 1 GiB RSS watchdog, and
single-process execution.
