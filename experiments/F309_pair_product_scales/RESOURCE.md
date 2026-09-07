# Resource budget

The integer-only pilot is expected to use less than 5 seconds and 128 MiB.
It has a 30-second alarm and an outer 35-second timeout. Direct pairs are
limited to L<=128. The large case uses degree-truncated progression
products only, with no graph or pair list.

Preflight: load2.34/2.03/2.06,71 percent available memory, no swapins or
swapouts. Two macOS indexing processes together used about187 percent CPU;
no competing mathematical process was present in the busiest-process list.
The bounded pilot remains small relative to the16 GiB machine.

Retain pilot.py, output.json, run.log and status.json. The source records
runtime, peak RSS, direct comparison counts and non-enumeration scope.
