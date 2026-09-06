# Preserved pre-freeze benchmark-wrapper failure

The first public benchmark command placed the `cd` and setup chain in the
background because of shell `&` precedence.  The benchmark binary completed,
but the monitoring shell stayed in the wrong directory, lost the start-time
variable, failed to hash its artifacts, and reported an invalid elapsed time.

No cohort was generated or opened.  The C++ source and compiled binary did
not change.  This wrapper attempt is non-authoritative.  The unchanged binary
was rerun with `cd` completed in the foreground and with the benchmark PID,
elapsed time, peak RSS, stdout, stderr, and hashes captured together.
