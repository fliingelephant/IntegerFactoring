# F260 target-check resource gate

At `2026-08-13T14:18:33Z`, the target exposed 32 CPUs, load averages
`57.80,58.21,57.99`, 503 GiB RAM with 367 GiB available, no swap, and
22 GiB free disk.  F258-D01 was active under `nice 15`, using about
31 MiB RSS and one CPU.  A fresh check at `2026-08-13T14:43:41Z` observed
load averages `57.40,57.50,57.54` and the same memory and disk margins.

The root authorized only one low-priority compile, algebra self-test, and
public synthetic benchmark, each under a 120-second timeout.  No corpus was
generated.  No hidden factor label was scored.

The first compile failed on two Boost expression-template ternaries.  Its
exact log is preserved as `compile_v1.stderr`.  Replacing integer zero by
`cpp_int(0)` fixed both mechanical errors.  The final checked source at
that stage had SHA-256
`905001a2bc2a06a653bfad68bb22d09f9dee36a78472a288ba305632c5f7f01b`.

The system lacks `/usr/bin/time`, so the first benchmark wrapper did not
start.  With explicit approval, the source then used
`getrusage(RUSAGE_SELF)` and `steady_clock`.  The algebra self-test and
public-only benchmark both passed.  Their exact stdout, stderr, and hash
files are preserved here.

One post-check mechanical selection-fill repair is disclosed in
`PREREGISTRATION.md`.  The final source must be recompiled and self-tested
by the production runner.  A transfer of that last source revision timed
out; it produced no mathematical result.
