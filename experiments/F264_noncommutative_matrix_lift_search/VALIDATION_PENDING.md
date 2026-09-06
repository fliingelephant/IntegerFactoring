# F264-D01 validation gate

Status: source frozen; target compile pending or complete as recorded in
`PRELAUNCH_MANIFEST.md`; every execution mode remains unopened.

F258 was active during preparation. F264 declares F258--F263 incompatible.
Therefore no `--self-test`, `--benchmark`, discovery cohort, or held-out cohort
may run until all six incompatible process families are absent.

The first allowed validation must use the frozen `remote_run.sh` gates. It
must verify hashes, inspect target resources, run the exact self-test and full
60-bit benchmark, reject a 1.75x projection above four hours, reject predicted
output above 1 GiB, and check overlap again immediately before production.

Any failed identity, exact-division, candidate-count, atom-count, cohort-count,
resource, or output gate invalidates the packet. It does not authorize a
source, grammar, threshold, or interpretation change. No mathematical cohort
has been opened at freeze time.
