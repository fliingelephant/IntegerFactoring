# F157-D01 failed runs

No authoritative run has failed.

Before the source was frozen, two environment probes failed. The first used
plain Python to import the pinned F118 Sage source. It failed because
`sage.all` was not on that interpreter's path. The second used the variable
name `SAGE_DOT_SAGE`, which Sage ignored, and failed because its default cache
directory was not writable. No experiment result was produced. The runner
uses no Sage import, so neither failure changes the registered workflow.

Several development checks then found source defects before freezing. One
F111 check omitted exact values equal to one from the local seed-basis
reconstruction. One comparison used raw columns where the pinned F111
convention uses normalized columns. A later support-two refactor left one
undefined local name. Each check stopped before it produced an experiment
result. The defects were corrected in the source.

Long development commands were initially launched without a persistent tool
session. The tool cancelled them after its short return boundary. These were
tool-session cancellations, not experiment timeouts or memory failures. The
same commands ran normally in a persistent session.

The first support-two index stored every pair that matched a sign modulo
either disclosed factor. It therefore also stored a very large number of
globally same-sign pairs, which can give only an improper gcd. On the first
F118 input, development counters reached 49,504,223 candidates after 10,000
left records, 91,590,338 after 20,000, and 132,057,498 after 30,000. The run
was stopped before any result. The final index uses the joint two-factor
value and discards globally same-sign pairs before storage. This changes only
the disclosed discovery index. Public construction and gcd verification are
unchanged.
