# F264-D02 validation gate

Status: **DO NOT LAUNCH pending fresh hostile audit**.

V2 is a new immutable packet. It does not modify or supersede V1 or
`HOSTILE_PRERUN_AUDIT.md`. Local compilation was unavailable because Boost is
absent. Target validation was prohibited because F258-D01 was active.

After a fresh hostile pre-run audit passes and F258--F263 are all absent, the
first operator must run the frozen `V2_remote_run.sh`. The runner must, in
order:

1. authenticate `V2_FROZEN.sha256`;
2. pass the process and resource gates before compile;
3. compile with target C++17, Boost Multiprecision, warnings, and the 4 GiB
   memory cap;
4. pass the full self-test, including five unique nonzero ternary controls,
   the exact six-summand associator, all three step-minor pairs, both conjugate
   basis transcripts, and the noncommutativity check;
5. pass one complete 60-bit-factor benchmark and the 1.75x four-hour
   projection gate;
6. pass the description and predicted-output gates;
7. run and validate discovery alone;
8. recheck resources and incompatibilities, then run and validate held-out
   alone;
9. validate all dimensions, split labels, 2,541-column row counts, decoy counts, and JSON
   counts before compression;
10. finish every stage inside one four-hour deadline while a two-second
    monitor enforces the process and 1 GiB owned-byte gates.

Any failed gate invalidates these V2 bytes. It does not authorize a new
threshold, grammar, source edit, replacement cohort, or alternate workflow.
No durable ledger may be edited from this packet without a completed run and
fresh hostile and blind interpretation audits.
