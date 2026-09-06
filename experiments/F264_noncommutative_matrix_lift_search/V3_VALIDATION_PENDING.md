# F264-D03 V3 validation gate

Status: **DO NOT LAUNCH pending a fresh independent hostile audit**.

F258-D01 was active while V3 was prepared. F264 declares every F258--F263
production or validation process incompatible. Therefore V3 has no C++
compile, self-test, benchmark, description, cohort, or score result.

After the fresh V3 audit passes and all incompatible processes are absent, the
first operator must run the frozen `V3_remote_run.sh` without editing a byte.
That one runner must:

1. authenticate `V3_FROZEN.sha256` inside the shared monitored envelope;
2. compile the frozen C++17 source on the target;
3. pass the nullspace, algebra, scope, noncommutativity, unit, P205, and
   exhaustive 36-by-14 root self-tests;
4. pass one full 60-bit-factor benchmark and its 1.75x four-hour projection;
5. validate the exact description and 2,560-column contract;
6. generate and exactly validate discovery in one process;
7. recheck the firewall and resources, then generate and exactly validate
   held-out data in a separate process;
8. compress the four row/anomaly files inside the same envelope;
9. create the complete manifest inside that envelope;
10. pass the final monitored aggregate-size and deadline gate after the
    manifest exists.

Every material child uses at most eight threads, `nice 15`, 4 GiB virtual
memory, the one shared four-hour deadline, and the 1 GiB owned output/log cap.
Any failed gate invalidates these bytes. It does not authorize a relaxed
threshold, replacement cohort, source edit, or alternate workflow.

No durable ledger may be edited from this packet without a completed run and
fresh hostile and blind interpretation audits.
