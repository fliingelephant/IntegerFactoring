# Retained first-run wrapper issue

The first complete source run used `/usr/bin/time -l`. The Python process
finished all checks and wrote `status: complete`, but the wrapper returned
exit code 1 after its attempt to read `kern.clockrate` was blocked by the
local sandbox. The complete verbose log is `run_time_wrapper_failed.log`.
Its output and source status are preserved as `output_time_wrapper.json` and
`status_time_wrapper_source_complete.json`.

The formal run uses the source's own monotonic timer and `ru_maxrss` field.
