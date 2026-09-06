# F259-D02 validation gate

Status: source repair complete; fresh hostile pre-run audit and target
validation are pending.

`remote_run.sh` must not be invoked until a fresh auditor returns PASS on the
frozen V2 bytes. F258 is currently active, so no target executable mode is
permitted. Compilation, describe, self-test, benchmark, and production all
remain unopened for V2.

The first permitted target invocation must use the frozen runner without
manual substitutions. It must, in order:

1. require the fresh hostile audit file and its PASS verdict, then authenticate
   every entry in `FROZEN.sha256`;
2. start with empty output and log directories, and find no F258, F260, F261,
   F263, or F264 process by command line, working directory, or executable
   path;
3. pass the CPU, memory, disk, and load gates;
4. compile with the frozen C++17 command;
5. pass the monitored self-test, including the 12-column rank-10 cocycle
   control and zero-carry checks;
6. pass three monitored full-pipeline 120-bit benchmarks;
7. accept only a conservative 1.75x eight-thread projection at most 14,400
   seconds and predicted output at most 1 GiB;
8. pass describe-mode dimensions;
9. repeat the overlap and resource gates immediately before production;
10. keep overlap and output monitors active throughout production;
11. validate exactly 7,040 rows, 634 columns, every split/cohort count,
    parseable JSON, 255 rankings, 462 family summaries, and 5,355 word
    summaries;
12. finish validation and compression within the shared production deadline;
13. keep aggregate output and logs at or below 1 GiB, including the reserved
    final manifest space.

Any failed gate invalidates the run. It does not authorize an edit to the
source, grammar, cohorts, runner, thresholds, or interpretation. No durable
ledger may be edited by this experiment.
