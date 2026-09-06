# F236 run log

## Host check before scaling

The authorized remote was `ssh seetacloud`.  Before the first full run it
reported:

```text
Linux 5.4.0-153-generic x86_64
32 visible CPUs
load average approximately 60
503 GiB RAM total, 367 GiB available, no swap
30 GiB overlay disk, 22 GiB free
g++ 11.4.0
```

Because host load was high, every scan ran alone with `nice -n 19`.  The
largest arrays occupy about 35 MB.  No SageMath or Python was available in
the remote image, so the preregistered C++ path was used without a workflow
substitution.

## Build and run form

Every source used this form:

```text
g++ -std=c++20 -O3 SOURCE.cpp -o /tmp/BINARY
nice -n 19 /tmp/BINARY > /tmp/OUTPUT.out
```

Sources were copied with `scp` and raw outputs were copied back with `scp`.
No scan used parallel workers.  The first word scan finished in about 28
seconds.  The later scans finished in seconds to about one minute.

The four reproduction outputs were generated sequentially with `set -e`
from the same local sources copied again immediately before compilation.
The include-based follow-up sources emit a harmless compiler warning because
`scan.cpp` is included after macro-renaming its `main` to an uncalled
ordinary function.  That renamed function is never invoked.  Each actual
follow-up `main` returns normally.

## Final environment snapshot

At `2026-08-13T05:45:17Z` the host reported:

```text
Linux autodl-container-d9694eab60-f7a6b268 5.4.0-153-generic x86_64
g++ (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0
32 visible CPUs
load average 65.14 59.62 58.10
503 GiB RAM total, 367 GiB available
22 GiB free overlay disk
```

## Remote raw-output hashes

```text
38603fdc32a5a9f20cd396fbfa7ac41f2569d43a6760d7b34d996d30362ae1b7  word_scan.out
8d5b6f11a2f25a007b278178856167caee7b71e453da19e228bd9a9bf6530672  carry.out
d5722b8bc472179143cea98093e9aafa49b345927a4991acf2f8b8c361ea29d5  carry_order.out
8b076693c997208424c41a39091a8f5b97eea7df55a797de023d27fd66140f77  multiplier_carry.out
92a68135e0bd10b5dde320715228a7b798b2cc7fbcda6c03f8a2e9f2d87c67ef  tradeoff.out
63268e6260bf178b0a6426660a182e90eeb83e0b376a15ec7c65a537fad5fd1b  multiplier_scaling.out
389964b6367d3bd1ea5538175497a7e52d911cdff3a85109b4827a3a7a490ba3  fixed_center_scaling.out
6b72f5b762b797404b87a745f9aa46d881ff62fd737cd6d0ad46312deefb9348  first_hit.out
672b2119b1e41fae19b89432e846893474e8d6ed06f4f78e7fa1782bc95cdfe5  gcd_collision.out
f3a19a1557c4c1a6fea930bf57d77e66f8b79bbb50fd82741f2bcd87e84a977e  random_hit.out
```

The local copies have the same hashes.  `verify.py` checks them and every
headline finite claim used by `STATEMENT.md`.

