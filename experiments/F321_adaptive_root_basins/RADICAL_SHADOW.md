# Prime powers can be handled by a radical shadow

**Family:** route:F29

Status: exact comparison and conditional all-input reduction independently
reconstructed in P245. No quasipolynomial growth or success bound for the
squarefree process is assumed proved. SHADOW_STATEMENT_ONLY.md and
SHADOW_RECONSTRUCTION.md preserve the verification scope.

## Compare classifications, not valuation distributions

Let N have at least two distinct prime divisors and put R=rad(N). The
algorithm does not know R. Couple each fresh uniform seed X modulo N to
its reduction modulo R. This is an independent uniform seed modulo R,
because every residue has N/R lifts.

Until the N process has already returned a factor, its current polynomial
and stored unit roots reduce to those of the R process. This is initially
true for H(X)=X. All updates H -> H(H-A) commute with reduction. For any
evaluated integer Y, the classifications obey the following exact table.

| Outcome modulo R | Outcome modulo N |
| --- | --- |
| gcd(Y,R)=1 | gcd(Y,N)=1 |
| 1<gcd(Y,R)<R | 1<gcd(Y,N)<N |
| gcd(Y,R)=R | either a proper gcd, or gcd(Y,N)=N |

The first row holds because N and R have exactly the same prime divisors.
For the second, Y is divisible by at least one such prime and misses at
least one, so its N-gcd is proper. In the last row, any incomplete prime
valuation only supplies an additional proper divisor of N.

Thus every unit update agrees after projection. A full-zero rejection
also agrees unless the N process factors earlier. Every shadow success
is consequently an actual success by the same probe. For each fixed cap B,

    Pr_N(success within B probes) >= Pr_R(success within B probes). (1)

This is a pathwise coupling, not an independence assumption about histories
conditioned on survival. No valuation histogram or computed radical is
required. The arithmetic is performed at the full input bit length.

The optional fixed fiber guard has the same property. Apply the table to
each H(X)-A instead of H(X). Guard acceptance consists entirely of unit
outcomes and hence agrees; a rejected full-zero proposal agrees or is
replaced by an earlier proper factor. With equal total evaluation caps,
mid-guard failure is treated identically until such an extra success.

## A sufficient squarefree contract gives an all-input algorithm

Suppose that for every odd squarefree composite of length m, the unguarded
attempt with public cap B(m) succeeds with probability at least 1/Q(m),
where B and Q have fixed quasipolynomial bounds. Choose explicit
nondecreasing quasipolynomial envelopes b(n),q(n) for these bounds. Such
envelopes can be integer functions of ceil(log2(n+1)), with their fixed
constants part of the supplied quantitative hypothesis. The algorithm
does not need to evaluate a nonconstructive smaller B or Q.

For a full N of length n with at least two distinct primes, its analytic
radical has length m<=n. The cap b(n) is at least B(m). Increasing only
the cap does not change an earlier unguarded trajectory, so (1) gives

    Pr_N(success in one capped attempt) >= 1/Q(m) >= 1/q(n). (2)

The public algorithm uses b(n); it never computes m or rad(N).

One attempt has at most b(n) evaluations and b(n)(b(n)-1)/2 modular
multiplications, plus gcds and bookkeeping. Exact uniform sampling uses
expected O(n) fair bits per seed by rejection from the next power of two.
Its expected bit cost is therefore O(b(n)^2*poly(n)). Independent attempts
and exact divisor verification give total expected cost

    O(b(n)^2*q(n)*poly(n)),                               (3)

which is quasipolynomial. No independence between an attempt's own runtime
and success event is used; only fresh randomness for later attempts is
needed for the usual stopped-cost identity.

Even inputs can first be stripped of powers of two. Use polynomial-bit
primality testing for prime leaves. Exact integer-root tests identify
nontrivial perfect powers N=A^e; factor A recursively and multiply its
prime exponents by e. If a remaining composite is not a perfect power,
it must have at least two distinct prime divisors, so (2) applies. A proper
factor tree has polynomially many nodes in n, and multiplying (3) by that
factor preserves quasipolynomial expected cost. Every output is verified,
each capped attempt terminates almost surely, and positive success with
independent restarts proves almost-sure termination of every splitter.

The primality and exact integer-root algorithms are explicit standard
dependencies of this conditional reduction. The unproved part remains
the uniform squarefree success contract B,Q. This packet does not claim
that contract, or completion of the factoring goal.

## Scope of the improvement

ANALYSIS.md correctly notes that the field collision-energy identity does
not hold unchanged in a prime-power ring. The comparison here makes that
identity unnecessary at prime-power precision for this public protocol:
field-shadow success is already enough, and additional valuations can only
make a gcd success occur earlier. This conclusion depends on the exact
unit-update/full-zero-rejection rules. It is not a theorem about arbitrary
N-dependent dynamical maps or algorithms that make different choices after
nonunit observations.
