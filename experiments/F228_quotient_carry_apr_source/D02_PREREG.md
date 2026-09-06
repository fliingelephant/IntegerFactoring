# F228-D02 preregistration — fixed-menu bit-scale ladder

## Purpose

D01 found no zero row at 37--38 bits.  D02 tests the identical mathematical
menu at larger input sizes.  It is a finite discovery run.  It cannot prove
an asymptotic rate.

For each `k` in `{22,26,30}`, form the increasing list of safe primes
`r=2s+1` starting at `2^k`.  Use the first 33 such primes and hence the first
32 consecutive pairs `(p,q)`.  Stop with an error if a pair has `q>=2p`.
This gives 96 frozen semiprime rows.

For every row use exactly the D01 menu:

- `B=2^floor(bit_length(N)/2)`;
- all 128 odd multipliers `1<=u<=255`;
- all shifts `-4<=c<=4`;
- all exponents `0<=i<256`;
- divisor cap `omega(W_u)<=20`;
- exact terminal threshold `J=ceil(N^(1/4))`;
- exact threshold saturation and exact selected prime-list certificate.

The only implementation change is a primality precheck before and during
trial division.  It returns an exact prime factorization and does not change
the menu or predicate.

## Decisive interpretation

- A zero row is an exact obstruction to this fixed menu, even with hidden
  compatible-subset knowledge.
- A positive row gives only a finite success numerator out of 128.
- Change with `k` is discovery guidance only.  No fit or finite trend proves
  an inverse-QP lower bound or its failure.
- The safe-prime cohort still has `gcd(p-1,q-1)=2`, so odd common-order
  accumulation cannot account for success.

## Resources and exact command

Use the already inspected `seetacloud` host.  The run is single-threaded.
Estimated peak memory is below 64 MiB.  Estimated runtime is below 300
seconds.  The only accepted timeout wrapper is `/usr/bin/timeout`.

Sources:

- `/root/F228/run_F228_D01.cpp`, frozen SHA-256
  `c3ebba44df3ba098e383fa84239c81503040fcf17e8dbed42927d5e601941256`;
- `/root/F228/run_F228_D02.cpp`.

Output: `/root/F228/D02_OUTPUT.tsv`.

Log: `/root/F228/D02_RUN.log`.

Commands:

```sh
/usr/bin/g++ -O3 -std=c++17 /root/F228/run_F228_D02.cpp -o /root/F228/run_F228_D02
/usr/bin/timeout 300s /root/F228/run_F228_D02 /root/F228/D02_OUTPUT.tsv > /root/F228/D02_RUN.log 2>&1
```

A compile failure or timeout ends D02.  No alternate menu, runtime, or
factorization routine will be substituted.
