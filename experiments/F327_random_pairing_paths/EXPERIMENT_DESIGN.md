# F327 bounded experiment design

Purpose: determine whether random-center reflections improve short-path absorption beyond the exact lazy-uniform-matching benchmark, using the same public inputs and verified gcd screens. This is a finite discovery experiment, not an asymptotic test.

## Public input and action boundary

Use the existing F326 GaussPairing implementation unchanged. For each fixed test N, an outer generator draws a uniform nonzero r, retains any proper gcd as an immediate factor, and otherwise computes a=r^2 mod N. Pass only N,a, independent method coins, and a public cap to the inner procedure. Do not pass r or use it to choose a center, screen, cap, or trajectory. Decode root outputs against r only after the inner procedure stops.

Compare three inner methods at the same N,a:

1. F326 reflection around rank L, retained as a deterministic baseline.
2. Uniform j in [0,d), start j, auxiliary reflection S_j(i)=2j-i mod d.
3. Uniform start and lazy uniform matching using the unused-pool algorithm in REPORT.md.

For each method retain two screens: the original F326 decoder/coordinate gcd only, and the static F-edge screen with gcd(x-1,N), gcd(x+1,N), gcd(x-F(x),N), gcd(x+F(x),N). An absorbed nonfixed edge must check both endpoints symmetrically so the absorbing set is F-invariant. Never count gcd 1 or N as a factor. If the current rank is fixed and the original decoder returns a root, retain that root even if the screen separately found a factor; record both so the exact-law control can use a specified consistent priority.

## Small exact-law controls

For a handful of odd N<=101 and every unit-square a, enumerate only these small rank domains. Compute d, q, the three fixed-point branch counts, and b for the static screen. Check q_unit=2^s-1 against offline factor labels. For d<=9, enumerate all auxiliary perfect matchings for every singleton start, confirming the exact capped survival, mean and uniform terminal-rank law by integer rational counts. Larger full-matching enumeration is unnecessary.

For the same small arithmetic instances, enumerate every reflection center j. Retain exact cumulative absorption counts for all caps through min(d,64), screened factors, roots, outer decoded factors, and first-hit types. Compare valid-output probability against 1-S_T; do not compare realized hidden-root success against the conditional-root expectation as if each fixed r had to attain it.

A cheap generic control is F(i)=-i mod d with prime odd d. For reflection S_j, H=1 at j=0 and H=(d+1)/2 at every nonzero j. This is an exact scoped example showing that reflection alone has no generic short-path amplification. It is not an arithmetic F326 counterexample and must be labeled separately.

## Bounded scaling pilot

Proposed initial N: 209, 1333, 10807, using 16 independent unit-square queries per N and caps 4,16,64,256. A single trajectory can supply its whole cap prefix. Use eight independent reflection centers and eight lazy matching starts per a if the pilot remains below budget. Compute q or b by enumeration only on the smallest instances; label unavailable larger diagnostics as unknown. Full output distribution estimates do not require these counts.

Retain every censor, valid root, failed outer split, immediate generation factor, visited F-call count, rank/select/floor-sum counters, gcd calls, random-bit or bounded-random-draw counts, maximum pool-map size, and elapsed time. Include per-N capped cost/success ratios with numerator charging failed attempts and setup. Do not pool input sizes into a single inferred asymptotic rate.

Before executing, inspect local load, memory pressure and processes. Use one process, a 28-second internal alarm, a 30-second external timeout and a 512 MiB ceiling. Start with a small exact control before scaling. Preserve named source, status, log, output and resource files. Ask the root to allocate the existing Sol support after this design is accepted; this file itself launches no process.
