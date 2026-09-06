# Mordell endpoint completion and uniform remainder moments

**Family:** route:F31

The root question is whether the whole floor-indexed boundary family can be
compressed, rather than evaluated one argument at a time. F292 provides only
a fast individual kernel; F294 retains the exact varying prefixes. F296 is
testing their full Mordell reciprocity. This packet isolates two potentially
useful pieces of that recurrence: cancellation of the original endpoint
chirp against the two Fresnel factors, and a uniform short polynomial for the
remaining Laplace integral. Neither piece alone evaluates the outer moments.

The formulas were derived from Kuznetsov, Theorem 1, equations (6)--(7), and
Proposition 1, equation (27), using the cached primary paper. No claim of
external novelty is made. The Rust reader found no earlier Mordell entry.

Resource estimate: one Python process, less than 128 MiB, at most 60 seconds.
The exact phase pilot uses small rational arithmetic. The numerical pilot
uses 35-digit quadrature on a finite interval and records its precision and
an analytic tail bound. It supplies observations, not a quadrature proof.
Preflight at 05:06 local time reported load 1.99/1.97/1.94, 72% available
memory, no swap I/O, and no other numerical process. Sources, output, timeout
status, and log are retained. No factor labels enter any formula.
