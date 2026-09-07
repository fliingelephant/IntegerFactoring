# F324 resource control

**Family:** route:F31

The pilot uses three moduli, eight public parameter pairs per modulus, and
eight second matchings. Each path has at most
\(\min(3N,8192)\) calls to the imported F322 involution. The path code
computes \(r\) and \(s\) on demand and retains only a bounded trace prefix.
It does not precompute a \(3N\)-vertex graph.

Small controls through \(N=31\) exhaust all states for the F322 involution
and all reflection constants for the second matching. The estimate is below
10 seconds and 128 MiB.

A local preflight at approximately 13:41 on 2026-09-07 found a 16 GiB host,
67 percent free memory, zero swap, and load averages 1.65, 1.73, 1.78.
The source has an internal 28-second alarm. Each run also uses an external
30-second timeout and a 512 MiB ceiling.

The pilot completed in 2.292173 seconds at 32,325,632 bytes peak RSS.
Before scaling, a second preflight found 68 percent free memory, zero swap,
and load averages 1.37, 1.50, 1.65. The scale then completed in 0.300202
seconds at 35,520,512 bytes peak RSS. Both stayed below every limit.
