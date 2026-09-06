# F140-D01 final broad-search timeout

The source with SHA-256
`6188ef3ce918b4769d948267d7dfe34b422aebc27f8c3c34a87cb229ca3b9a04`
ran under the registered 300-second timeout.  `gtimeout` stopped Sage before
the script wrote a new result.  `RUN.log` is empty because the script prints
only after the complete corpus finishes.  The existing `OUTPUT.json` is the
invalid output from the preserved Sage-preparser failure and must not be used
as evidence.

No finite-search conclusion is claimed.  The proof-only construction in the
F140 statement and proof does not depend on this timed-out search.
