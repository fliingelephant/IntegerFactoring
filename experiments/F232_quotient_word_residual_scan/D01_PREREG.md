# F232-D01 preregistration — shifted quotient word residual scan

## Frozen question

In the F230 zero-defect branch, does maximal prime-power saturation of a
small polynomial menu of shifted quotient children often make at least one
hidden residual odd order equal to one or at most `n^4`?  How much does it
increase the exact F231 factor-or-growth probability at the hostile
certificate state `M=D`?

This is discovery only.  No finite frequency, fitted trend, or successful
factorization proves an unbounded inverse-quasipolynomial bound.

## Closest prior routes and material difference

The closest routes are F228, F230, and F231.  This run differs because it
aggregates the complete prime support of every shifted, `N`-dependent
quotient child into one saturating F231 multiplier word.  It does not test
each quotient child as a separate annihilator.  It preserves every direct
gcd event before residual analysis.

## Frozen public source

For each row, use only the public values

```text
n = bits(N)
B = 2^floor(n/2)
H = (N-1)/B
Y = n^2
U = n
C = bits(n)
```

The corpus is restricted to rows with `B | N-1`.  The public source first
adds every prime at most `Y` and every prime divisor of `H`.  For every odd
`1<=u<=U` and every nonzero `-C<=c<=C`, it screens

```text
A = uH+c
gcd(A,N)
gcd(|c|B,N).
```

Every proper gcd event is recorded as an immediate public factor.  The
runner then continues the finite measurement, completely factors `A`, and
adds all of its prime divisors to the word support.  Continuing after an
already valid factor is only for a complete fixed-corpus label; the
algorithmic row is already solved at its first proper gcd.  The runner
checks that every odd defect prime is already in the smooth support.  The
unshifted child `uH` is included analytically; its support is contained in
the already included supports of `u` and `H`.

Every exposed prime is granted exponent `n`.  This is the maximal
saturating word for the exposed support.  It is stronger than taking the
plain lcm of the child integers and therefore gives the quotient source its
best possible residual shrink without introducing a new prime.

The function that builds this source accepts `N` only.  Hidden factors are
not arguments and do not affect the menu, child factorization, stopping
rule, support, or first-witness map.

## Frozen corpus

Use the fixed SplitMix64 state `0xF232D01C0FFEE123`.  For each target bit
length, sample odd candidates `p` from `[B/2+1,3B/2-1]`, retain primes, set
`v=p^(-1) mod B`, and test `q=v+kB` for `0<=k<=4`.  Retain the first 24
distinct rows satisfying

```text
p < q < 2p
p and q prime
bits(pq) = target_n
B | pq-1.
```

The split is fixed before the run:

- train target bits: `30,34,38,42`;
- holdout target bits: `49,53,57,61`.

There are 96 rows in each split and 192 rows total.  The intervals are
disjoint.  No menu or threshold changes after train rows are observed.
The output records every exact gap `q-p`; the generator does not select on
gap size beyond balance.

The hidden factors are used only for corpus construction and, after the
public word is complete, for residual and probability labels.

## Frozen measurements

For

```text
P = oddpart(p-1), Q = oddpart(q-1), D = gcd(P,Q)
sp = P/D, sq = Q/D,
```

record the baseline and quotient-word residual pairs.  Record:

- whether one residual is `1`;
- whether the smaller residual is at most `n^4`;
- the binary shrink in each residual;
- the exact F231 probability expression evaluated numerically at `M=1`;
- the same expression at the hostile state `M=D`;
- complete factorizations of `sp,sq`;
- the first public child witness for every newly captured residual prime;
- every direct gcd event.

Preserve 12 lowest-`M=D`-progress rows and 12 least-shrink rows from each
split in `D01_HOSTILE.tsv`.  The full output remains authoritative.

## Decisive interpretation

- A direct gcd is a valid finite success of the public source.
- A row with unchanged residuals is a finite obstruction to any claim that
  this exact menu always adds support.
- A row with both residuals above `n^4` is a finite obstruction to the same
  row-wise favorable-state claim.
- Train/holdout frequencies and bit trends guide the next symbolic test.
  They do not prove or refute an asymptotic probability theorem.
- The runner uses Pollard--Brent only to realize the conditionally supplied
  complete child factorizations in this finite test.  Its runtime is not a
  factoring-complexity claim.

## Frozen implementation hashes

```text
F232_D01.cpp
e8d8b14f0138d67b35245590669fe40c361858a8f56ea21dd7a70088c506ee41

run_F232_D01.sh
a73d311ba213f2b83148da683a3234ff6e76edd5d1fdc83cf0c0b09d554b57c3

STATEMENT.md
90265a37e03e5f86874b953fc8248aa7699f2113035d4a6ffeeaae64570749ac

PROOF.md
981a0353448f9d42ca4b9858163d27ab92c304818e8790fce44cc46ebf0d0f4a
```

The corrected V2 source passed local C++17 syntax checking.  The V1
pre-run FAIL is preserved in `PRERUN_AUDIT_V1_FAIL.md`.  No mathematical
run has occurred under this registration.

## Resource and workflow gate

The remote inspection observed 32 logical CPUs, load averages
`56.27,56.36,56.82`, 367 GiB available memory, and 22 GiB free disk.  The
host had no `python3` or Sage executable.  The frozen replacement is one
C++17 thread, estimated below 64 MiB peak memory, with a 600-second hard
timeout.  It must not run until the root approves this tool substitution.

## Exact remote commands after approval

```sh
ssh seetacloud 'mkdir -p /root/F232'
scp F232_D01.cpp run_F232_D01.sh seetacloud:/root/F232/
ssh seetacloud 'chmod +x /root/F232/run_F232_D01.sh && /root/F232/run_F232_D01.sh'
scp seetacloud:/root/F232/D01_OUTPUT.tsv .
scp seetacloud:/root/F232/D01_SUMMARY.txt .
scp seetacloud:/root/F232/D01_HOSTILE.tsv .
scp seetacloud:/root/F232/D01_RUN.stdout .
scp seetacloud:/root/F232/D01_RUN.stderr .
scp seetacloud:/root/F232/D01_SHA256SUMS .
```

No alternate corpus, menu, factorizer, threshold, timeout, or output rule
will be substituted.
