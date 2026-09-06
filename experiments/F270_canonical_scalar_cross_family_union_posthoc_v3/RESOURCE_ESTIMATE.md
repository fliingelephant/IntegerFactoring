# F270-D03 static resource estimate

## Immutable workload

- Cases: 188 discovery moduli.
- Rows: 284 original rows per modulus, 53,392 total.
- Maximum singleton tests: 53,392.
- Maximum support-two tests after no peeling:

  ```text
  188 * C(284,2) = 7,554,968.
  ```

- Preferred clean cohort: 125 cases, with maximum

  ```text
  125 * C(284,2) = 5,023,250
  ```

  support-two tests.

Discovery factors have at most 32 bits. Thus every `N` has at most 64 bits,
every canonical row `U<N^2` has at most 128 bits, and one complete 284-row
case has at most 36,352 input bits. The 100,000-bit cap is checked across the
original serialized rows before exact-value deduplication.

## Time

The dominant operations are pairwise gcd refinement of at most 284 short
integers, degree-one peeling, at most 40,186 support-two tests per case, and
binary elimination on at most 284 columns. The support-two count is about
5.83 times the 1,294,704 pair tests in F268-D04; no claim of a smaller exact
workload is made.

No old benchmark is mathematical or admission evidence. The target host runs a
deterministic eight-case preflight. It multiplies observed wall extrapolation
by four. It likewise projects the complete raw tree, including runner metadata
and hash manifests, by a factor of four. The target may start only if that
projection fits the time remaining before the 600-second closure reserve in the one
14,400-second packet deadline.

## Live memory

At the 65,536-block cap, one dense exponent array has 284 unsigned 32-bit
entries. The raw exponent payload is about 71 MiB per active decoder before
container and multiprecision overhead. Eight simultaneous cap-saturating cases
have about 568 MiB of raw exponent payload. A case can transiently retain its
union result while it constructs the core decoder.

The analyzer retains at most one deterministic batch of eight `CaseResult`
objects. It never retains all 188 cases and never materializes a complete TSV
in memory. Relation strings have 96 MiB of globally reserved serialized
payload, one relation line is at most 1 MiB, and the count is at most
1,000,000. These source caps make the intended live set bounded. The target
host still treats the preflight as the admission evidence.

The whole workload runs in cgroup v2 with
`memory.max=3,758,096,384`, `memory.swap.max=0`, and an independent 4-GiB
`RLIMIT_AS`. Factor-four projected RSS must fit the cgroup. Any source-cap,
projection, cgroup, or address-space failure aborts without a mathematical
result.

## Output and disk

The source reserves exact bytes before retaining each relation and before
writing every other TSV line. Preflight raw output is capped at 16 MiB. Target
raw output is capped at 192 MiB. Those totals include a 64-KiB allowance for
runner metadata and the per-file SHA manifest. Exact relation TSV payload is
capped at 96 MiB. Every generated line and each buffered summary file is
capped at 1 MiB.

The complete run directory has a 512-MiB regular/apparent-size cap. It also has
a 16-MiB log cap, 1-MiB cap per captured phase stream, 32-MiB root-sidecar cap,
16-MiB binary cap, and 384-MiB per-file `RLIMIT_FSIZE`. Before deterministic
compression, the runner admits the transient only if

```text
current packet bytes
+ largest live raw file
+ raw_tree_bytes / 100
+ 4 MiB
<= 512 MiB.
```

GNU tar deletes each raw file after it enters the archive. GNU gzip runs with
fixed metadata. The runner verifies the archive structures and hashes every
raw output before removal, both archives, and every final packet file. The
host must have at least 4 GiB free before launch.

The D03 process firewall adds two byte-identical complete `/proc` identity
snapshots of at most 1 MiB each and one bounded acknowledgement file. These
are root sidecars inside the unchanged 32-MiB sidecar and 512-MiB packet caps.
Each process identity is capped at 256 KiB, the PID list at 16,384 entries,
and the exact ancestor chain at 64 entries and 16 KiB. Reaching a cap aborts;
it never truncates evidence and continues.
