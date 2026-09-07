# F335 resource control

**Family:** route:F31

The bounded checker first uses odd N through 51 and then, only after a
successful pilot, odd N through 301. It stores aggregate counts and a first
failure witness only. Estimated peak RSS is below 100 MiB and runtime below
30 seconds.

An earlier single-process coordination hold was superseded by the root's
09:33 UTC preflight on 2026-09-07: load averages 1.69, 1.79, 1.83,
59 percent system-wide free memory, zero swap, and no numerical worker in
the top processes. The authorized ceiling is two independent single-threaded
jobs, each below 512 MiB and the usual 28-second internal / 30-second
external limits. F335 nevertheless runs its checker and reference renderer
sequentially. The checker enforces its narrower 100 MiB peak-RSS ceiling.

The `N <= 51` pilot passed in 0.183 seconds at 25,739,264 bytes peak RSS.
The planned `N <= 301` run passed in 1.462 seconds at 26,017,792 bytes peak
RSS. The PDF renderer then processed the 370 KiB arXiv PDF in about 4.03
seconds and generated 211 image assets using `pymupdf4llm 1.27.2.3`. Its
`/usr/bin/time -l` wrapper returned status 1 after a denied
`sysctl kern.clockrate` metrics query, but the renderer completed both new
Markdown entries; identity checks and `kb_doctor` subsequently passed.
