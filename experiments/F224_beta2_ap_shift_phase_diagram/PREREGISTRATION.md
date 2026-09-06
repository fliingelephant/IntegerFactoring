# F224-D01 preregistration: beta-two AP scalar-root density

## Family and purpose

This finite discovery run serves F224, the carry-conditioned integer-shift
branch after P193.  It tests whether shifts drawn from the public factor
arithmetic progression show enough nontrivial modified-AKS scalar roots to
motivate a positive theorem.  It is guidance only.

The scalar is

\[
F_x=(1+x)^N-x^N-1\pmod N.
\]

For `N=pq`, `d=q-p`, its exact local forms are

\[
F_x\bmod p=(1+a)^{d+1}-a^{d+1}-1,
\qquad a=x\bmod p,
\]

and

\[
F_x\bmod q=(1+b)^p-b^p-1,
\qquad b=x\bmod q.
\]

Thus an exclusive local zero gives a proper gcd.  The point `x=p` is the
ordinary exact-candidate hit and is recorded separately.  The experiment
asks whether off-target exclusive roots are dense.

## Frozen cohort

For each `b` in `{12,14,16,18,20}` and `j` in `{0,1,2,3}`, let

```text
p = next_prime(2^b + j * floor(2^b/7)).
```

For each `alpha` in `{0.60,0.70,0.80,0.90}`, let

```text
q = next_prime(p + floor(p^alpha)).
```

Every row with `q<2p` is retained.  Put `N=pq`.  The public balanced
factor interval is

```text
ceil(sqrt(N/2)) <= x <= floor(sqrt(N)).
```

For `t` in

```text
{0, floor(b/10), floor(2b/10), ..., floor(5b/10)},
```

deduplicated in increasing order, scan exactly the integers in that interval
which satisfy

```text
x == p (mod 2^t).
```

The cohort and scan contain no random choices.

## Frozen outputs

For every `(b,j,alpha,t)` row record:

- `p,q,d,N`, the interval endpoints, `t`, and `L=2^t`;
- the AP population `H`;
- the exact-candidate count `x=p`;
- off-target counts `p_only`, `q_only`, `both`, and `neither` for the two
  displayed local zero tests.

The decisive discovery statistic is

\[
\frac{\#p\_only+\#q\_only}{H-1}.
\]

Positive guidance requires this off-target fraction to remain at least an
inverse polynomial in `b` near the capacity scale
`2^t approximately p/d` on a substantial part of the large-gap cohorts.
Obstruction guidance is recorded if off-target counts stay bounded or
polylogarithmic while `H` grows.  Neither outcome proves an asymptotic law.

## Resource envelope and exact command

The remote resource check on 2026-08-13 reported 503 GiB RAM, 367 GiB
available, 22 GiB free disk, and no visible CPU-heavy process inside the
container.  The host load averages were high, so this run uses one
nice-adjusted process.  Peak memory is below 2 GiB by construction.  The
wall cap is 600 seconds.

The frozen source is `scan.c`.  The frozen runner is `remote_run.sh`.
They are copied to `/tmp/f224_beta2_ap_shift_phase_diagram` and invoked as

```text
bash remote_run.sh scan.c OUTPUT.tsv RUN.log
```

No alternate runtime or reduced cohort will be substituted if this command
fails.  A changed workflow requires a new preregistration.
