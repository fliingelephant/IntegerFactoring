# Resource plan

**Family:** route:F29

The root supplied a preflight with 70 percent free memory, zero swap,
load averages 1.69, 1.67, 1.90, and no large research job. A local recheck
at approximately 12:34 on 2026-09-07 found 69 percent free memory, zero
swap, and load averages 2.69, 1.94, 1.97.

The public composite pilot has eight cases, three methods, and 16 independent
trials per method and case. Its per-trial gcd budget is
min(512, bitlength(N)^2). The worst adaptive trial uses fewer than 131,000
modular multiplications. The estimate is below 15 seconds and 128 MiB.

The finite-field diagnostic has five fields, four seeds per field, and at
most 256 vectorized updates. Its largest live arrays have 65,521 signed
64-bit entries. The estimate is below 15 seconds and 128 MiB.

The two stages run separately. Each has an internal 28-second alarm, an
external 30-second timeout, and a 512 MiB peak-RSS check. A failure or
timeout in one stage does not overwrite the other stage's files.

The public composite stage completed in 0.017654 seconds at 25,886,720 bytes
peak RSS. The finite-field stage completed in 0.436121 seconds at 39,141,376
bytes peak RSS. Both stayed below every limit.
