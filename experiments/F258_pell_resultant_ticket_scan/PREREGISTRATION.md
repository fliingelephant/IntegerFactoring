# F258-D01 preregistration — F257 direct Pell-resultant ticket scan

## Purpose

This is a finite discovery search for the conditional Las Vegas event in
F257.  It does not prove an inverse-quasipolynomial probability law.

For a balanced labelled semiprime `N=pq`, the source uses only public `N`.
The labels `p,q` are used after a gcd solely to verify the output and to
stratify the frozen cohort.

## Frozen public source

Use

```text
D = 2,3,5,6,7,10,11,13
1 <= j <= 12*bitlength(N)
```

For the least positive norm-one Pell unit, generate exact powers

```text
S_j^2-D*T_j^2=1
T_j=y_j+k_j*N, 0<=y_j<N.
```

Use only discriminants with `Jacobi(-D,N)=-1`.  Apply the following public
cleanup in increasing index, separately for every `D`:

1. test `gcd(D,N)`;
2. test `gcd(S_j mod N,N)`;
3. verify the supplied modular square root of `A_j=1+D*y_j^2`;
4. remove exact-square rows after testing both root-difference gcds;
5. remove repeated `y_j` after testing both supplied-root gcds;
6. retain only distinct nonsquare post-wrap rows with `k_j>0`.

For every retained same-`D` pair `i<j`, put

```text
Delta = y_i*k_j-y_j*k_i
a_minus = k_j-k_i
a_plus  = k_j+k_i
Q_sigma = a_sigma^2+D*Delta^2.
```

Test a sign only when `a_sigma>0` and `2*a_sigma^2<N`.  Compute
`gcd(Q_sigma mod N,N)`.  F257 proves that the result is either `1` or the
unique hidden prime at which `-D` is a square.  Every proper result is
therefore an exact certified factor ticket.

The implementation enumerates the minus pairs with a monotone sliding
window in `k`, and the plus pairs with a monotone prefix.  These procedures
enumerate exactly all pairs satisfying the frozen inequality.

## Frozen cohorts

Factor bit sizes:

```text
12,16,20,24,28,32,40,48,56,60
```

At every size use disjoint deterministic cohorts:

```text
random balanced prime pairs:      4096
consecutive balanced prime pairs: 1024
safe-safe balanced prime pairs:   128 at 12 bits, 1024 otherwise
```

All factors have the declared bit length.  Accept only distinct
`p<q<2p`.  Duplicate moduli within a cohort are rejected.  Generation uses
fixed SHA-256 streams encoded in the source.  Total planned inputs: 60,544.

Factor sizes through 32 bits are the discovery block.  Sizes 40,48,56,60
are held out.  No source or interpretation parameter may change after any
mathematical output is inspected.

## Frozen output

For each input preserve:

- cleanup-factor status;
- selected discriminant count;
- eligible and hit counts by `D` and sign;
- whether any hit is strict, meaning no earlier cleanup factor;
- the first exact ticket certificate, if present.

Aggregate these fields by factor size, cohort, `D`, and sign.  Preserve the
complete per-input JSONL stream and a summary JSON.

Interpretation:

- any strict held-out hit is an exact anomaly worth explaining;
- at least 16 strict hit inputs over at least three held-out factor sizes is
  a strong finite signal for this fixed source;
- zero strict held-out hits is a finite null for this source only;
- finite rates never establish an asymptotic inverse-QP bound.

## Frozen resource envelope

Run on `seetacloud` with `/root/miniconda3/bin/python`, eight forked workers,
`nice -n 15`, at most 4 GiB virtual memory, and a four-hour timeout.  The
remote container was idle at preregistration time, but the shared host load
was about 57 on 32 visible CPUs.  Do not run F255 concurrently.  Hash the
source, runner, outputs, and logs.

