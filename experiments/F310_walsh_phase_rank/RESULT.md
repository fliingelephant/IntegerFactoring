# Fixed-order rank of the canonical inverse top-bit phase

**Family:** route:F31

**Status:** exact finite exploratory evidence. The tested linear signed-state
matrices have high rank in the fixed order below. This is not an algorithmic
lower bound and does not exclude a different split, ordering, nonlinear state,
or arithmetic aggregation.

## Object and period reduction

Let the original modulus be `M=2^k`, put `L=M/2=2^s`, and let `N` be odd.
For `0<=x<L`, define

    F_N(x)=((N-1)/2-x)/(1+2x) mod L,
    phase(x)=(-1)^[bit_(s-1)(x)+bit_(s-1)(F_N(x))].

All denominators are odd. If `h=L/2`, then

    1+2(x+h) = 1+2x mod L,
    F_N(x+h) = F_N(x)-h mod L.

Multiplication of `h` by any odd inverse leaves `h` modulo `L`. Hence the
top bits of both `x` and `F_N(x)` toggle, and

    phase(x+h)=phase(x).

The implementation checked this equality at every `0<=x<h` in every case.
It then used only the `s-1` effective bits.

## Fixed linear representation

Set

    r=floor((s-1)/2),
    A[a,b]=phase(a+2^r*b),

for `0<=a<2^r` and `0<=b<2^(s-1-r)`. The script constructs `A` over
`GF(65521)` and computes its exact rank. For each case it retains pivot
columns, independent rows, and the nonzero determinant modulo 65521 of the
resulting rank-by-rank minor. These data are a directly replayable certificate
of the reported rank.

No factor of `N` is computed or supplied. No denominator can be zero modulo
`L` because every denominator is odd.

A nonzero minor modulo 65521 is also a nonzero integer minor. Thus it is
a lower bound for the rank over the rationals or complex numbers. Any
fixed-cut linear representation `A[a,b]=sum_(j=1..t) p_j(a) q_j(b)` over
characteristic zero needs at least that many components for this particular
finite matrix. No uniform asymptotic lower bound is inferred from the cases.

This does not bound the cost of summing the phase. For example, the matrix
`(-1)^(a dot b)` on two r-bit vectors has full rank `2^r`, but its total
sum is just `2^r` by character cancellation. A nonlinear or algebraic
aggregate can therefore remain useful even when a sequential linear-state
representation is large. The experiment tests that representation, not the
possibility of an efficient total sum or a factoring algorithm.

## Exact results

The seed was `31020260907`.

| s | Matrix | Input label | N | Rank | Deficiency |
|---:|---:|---|---:|---:|---:|
| 7 | 8 x 8 | 9M+1 | 2305 | 5 | 3 |
| 7 | 8 x 8 | seeded | 4019 | 8 | 0 |
| 9 | 16 x 16 | 9M+1 | 9217 | 13 | 3 |
| 9 | 16 x 16 | seeded | 9227 | 14 | 2 |
| 11 | 32 x 32 | 9M+1 | 36865 | 29 | 3 |
| 11 | 32 x 32 | seeded | 42207 | 24 | 8 |
| 13 | 64 x 64 | 9M+1 | 147457 | 61 | 3 |
| 13 | 64 x 64 | 9M+3 | 147459 | 62 | 2 |
| 13 | 64 x 64 | 9M+5 | 147461 | 62 | 2 |
| 13 | 64 x 64 | seeded | 163481 | 62 | 2 |
| 15 | 128 x 128 | 9M+1 | 589825 | 125 | 3 |
| 15 | 128 x 128 | 9M+3 | 589827 | 126 | 2 |
| 15 | 128 x 128 | 9M+5 | 589829 | 126 | 2 |
| 15 | 128 x 128 | seeded | 969131 | 122 | 6 |
| 17 | 256 x 256 | 9M+1 | 2359297 | 253 | 3 |
| 17 | 256 x 256 | 9M+3 | 2359299 | 254 | 2 |
| 17 | 256 x 256 | 9M+5 | 2359301 | 254 | 2 |
| 17 | 256 x 256 | seeded | 3229937 | 254 | 2 |

For the structured inputs, the observed deficiencies stabilize at three for
`9M+1` and two for `9M+3` and `9M+5` over the displayed range. The seeded
cases show that the deficiency need not follow either value. These are finite
patterns only. No recurrence or all-size rank formula is asserted.

The data answer the preregistered question for this representation: exact
Möbius-map distinctness does not force literal full rank, but the selected
low-bit/high-bit matrix also does not exhibit a small rank in the tested
range. A compressed representation could still use another variable order,
split, field, nonlinear state, or arithmetic identity.

## Resources and retained evidence

The six pilot cases completed well inside the scaling rule, so all twelve
larger cases ran. The 18 cases took 0.366 seconds after Sage startup and used
258,392,064 bytes peak RSS. The command had a hard 30-second outer timeout,
a 28-second internal alarm, and a 1 GiB RSS watchdog. The run used one Sage
process and no numerical concurrency.

An initial direct `.sage` launch stopped before matrix construction because
the Sage preparser changed standard-library seed and timeout literals into
Sage numeric types. The successful command used `sage -python` on the same
pure Python source, while importing Sage's exact `GF` and matrix operations.
The setup failure occurred before any numerical matrix comparison.

Evidence:
`walsh_phase_rank.sage`, `walsh_phase_rank.json`, `walsh_phase_rank.log`,
`RESOURCE.md`, and `SOURCE_LEADS.md`.
