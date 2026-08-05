# Failure dispositions

`run_001` requires exit status zero from both named, timed stages.  Any timeout
or nonzero exit creates `outputs/run_001_<stage>.failure.txt`, stops the run,
and preserves all prior output.  A failed scan does not certify omitted minors
as nonzero.  Source changes after the pre-run hash require a new run ID.

