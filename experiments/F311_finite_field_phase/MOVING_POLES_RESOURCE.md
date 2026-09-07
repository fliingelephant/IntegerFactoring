# Resource plan for moving simple poles

Preflight on 2026-09-07 reported 67 percent free memory and load averages
2.73, 2.36, 2.27. The existing F311 runs used less than 24 MiB. The new
search uses one Python process and one RSS watchdog thread.

For `q=256`, there are `2*q*(q-1)=130560` single-pole parameter triples.
The affine-quotient hash retains at most two witnesses with different pole
locations per key. Packed truth tables use 256-bit Python integers. The
largest target set has only 32 tables. Translation of the pole-zero tables
uses precomputed XOR index permutations, and hash complementation replaces
the naive four-parameter pole-pair loop.

The estimated peak RSS is below 256 MiB. The enforced budget is 512 MiB.
The command has a hard 30-second outer timeout and a 28-second internal
alarm. Scaling runs in order `q=32,64`, then `q=128`, then the seeded
16-residue subset at `q=256`; it stops before the next scale if elapsed time
or RSS no longer leaves the stated headroom.

The pilot left sufficient headroom and completed every scale. It took
1.987550 seconds and used 86,982,656 bytes peak RSS. The timeout and memory
guards did not fire.
