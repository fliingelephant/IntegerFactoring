# F228-D03 preregistration — source sparsity versus divisor-cap pressure

## Purpose

D02's fixed `omega<=20` cap rejected most trials at larger bit sizes.  D03
repeats the same 96-row cohort and the same quotient, shift, and exponent
menus, but computes the hidden compatible product before applying a cap.
This separates source sparsity from enumeration pressure.

For `k in {22,26,30}`, use the first 32 consecutive safe-prime pairs at or
above `2^k`.  For each row use all odd `1<=u<=255`, all `-4<=c<=4`, and all
`0<=i<256`.  Factor every positive `Q_u+c`.  For each multiplier compute the
exact predicate

```
exists i: product(ell | W_u and p == N^i mod ell) >= ceil(N^(1/4)).
```

Record its numerator out of 128 with no cap.  Also record the numerators
after the separate caps `omega(W_u)<=20`, `<=40`, and `<=64`, plus the
minimum, maximum, and mean numerator of `omega(W_u)`.

## Decisive interpretation

- A zero no-cap numerator is an exact obstruction to the fixed arithmetic
  source, even with hidden knowledge of the compatible subset.
- A no-cap success removed by a cap is enumeration pressure, not source
  sparsity.
- The `40` and `64` caps are finite probes only.  They are not declared to
  be the asymptotic QP cap.
- Any scale trend remains discovery evidence only.

## Resources and exact command

Use one thread on the inspected `seetacloud` host.  Estimated peak memory is
below 64 MiB and runtime below 300 seconds.  Use only `/usr/bin/timeout`.

Source: `/root/F228/run_F228_D03.cpp`, including the frozen D01 source with
SHA-256
`c3ebba44df3ba098e383fa84239c81503040fcf17e8dbed42927d5e601941256`.

Output: `/root/F228/D03_OUTPUT.tsv`.

Log: `/root/F228/D03_RUN.log`.

Commands:

```sh
/usr/bin/g++ -O3 -std=c++17 /root/F228/run_F228_D03.cpp -o /root/F228/run_F228_D03
/usr/bin/timeout 300s /root/F228/run_F228_D03 /root/F228/D03_OUTPUT.tsv > /root/F228/D03_RUN.log 2>&1
```

No alternate menu or factorization routine will be substituted.
