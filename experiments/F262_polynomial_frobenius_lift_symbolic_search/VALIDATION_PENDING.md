# Mandatory post-conflict validation gate

F262-D01 is compile-validated but not execution-validated. F258-D01 was active
during the freeze. The incompatibility rule forbids even the synthetic
self-test and throughput benchmark from overlapping it.

After F258-D01, F259-D01, F260-D01, and F261-D01 are all absent, the frozen
runner must, in this order:

1. verify `FROZEN.sha256`;
2. compile the frozen source with target C++17 and Boost.Multiprecision;
3. run `--self-test` under `nice 15` and a 15-minute timeout;
4. run the full-largest-static-scope `--benchmark` under `nice 15` and a
   30-minute timeout;
5. refuse the cohort run unless the conservative eight-thread projection is
   at most 14,400 seconds and the printed memory/output projections stay below
   4 GiB and 1 GiB;
6. recheck all four incompatible process patterns immediately before opening
   any cohort.

Any self-test, identity-miner, quotient-divisibility, translation-conjugacy,
candidate-count, or benchmark failure invalidates the packet. Do not reduce
scope or substitute a different arithmetic engine after this freeze.
