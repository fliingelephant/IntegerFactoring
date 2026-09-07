# Fair branches without a worst-case shrinking path

**Family:** route:F31

Status: root derivation and experiment proposal, not independently
reconstructed or promoted. No new factor-success bound or novelty claim.

F334 always continues at the smaller child. F336 changes the multiplier
source but keeps that choice. The policy below changes the branch law. It
is separate from the frozen F336 sampling experiment and its results.

## Public policy and expected work

For odd N, put h=(N-1)/2 and start at a public t_0 in [1,h]. At a reached
state t>=2, choose a public unit a and compute

    q = #{1<=y<=t : 1<=a*y mod N<=h}.

Screen t by gcd with N, returning a proper divisor immediately. Otherwise
compute q and screen both positive children q,t-q, even if the first child
already yields a factor. Then return their verified proper divisors, as in
frozen F334/F336. If no factor is found, fail if a child is zero. Otherwise
select q or t-q with one independent fair bit. Stop with failure when the
selected child is at most one. For the first proposed experiment, a is
retained for the whole attempt.

Let H be the number of reached queries. Set X_j to the size before query j,
and to zero after the attempt terminates. Each live X_j is at least two.
Conditionally on the history before the branch bit,

    E[X_(j+1) | history] <= X_j/2.

The inequality includes success, empty children, and size-one termination.
It does not require a small count defect or a small multiplier. Iterating
and applying Markov's inequality gives

    Pr(H>j) <= min(1, t_0/2^(j+1)),
    E[H] <= ceil(log_2(t_0))+1.

This also permits adaptively selected multipliers chosen before each fresh
branch bit. If each reached query has conditional expected charged cost
at most B(n), including that selection, the attempt has expected cost at
most g(n)+B(n)*(ceil(log_2(t_0))+1), where g covers initial generation.
For a fixed n-bit unit, ordinary Euclidean floor sums supply polynomial
bit cost per query. No claim here requires every realized path to halve.

Independent fresh attempts with success probability delta(N)>0 and finite
mean total cost tau(N) give expected factor time tau(N)/delta(N). Cost may
correlate with success within an attempt. The missing result is a useful
delta(N) for some explicit public source, uniformly for each input N.

## Exact small-input success and cost recurrences

Fix N and a. A state is successful when its declared gcd screens find a
proper divisor. It is a failure when t<=1 or an empty side is reached
without a successful screen. Let s(t) be its eventual success probability,
and c(t) its mean total cost in a specified additive operation measure.
Let w(t) be the cost of the reached query under this screen convention. Then

    s(t) = 1                                      at success;
    s(t) = 0                                      at failure;
    s(t) = (s(q)+s(t-q))/2                         otherwise;

    c(t) = w(t)                                   at terminal states;
    c(t) = w(t)+(c(q)+c(t-q))/2                    otherwise.

For t<=1, w(t) is just the declared stopping check. Both continuing
children are smaller than t, so memoized rational arithmetic evaluates
these recurrences exactly on small inputs. This exhaustive analysis is
validation work, not a proposed fast factoring routine.

Complementing a exchanges the two children, preserving the branch law.
Charging both child gcds also preserves the gcd-call count. This need not
preserve every low-level arithmetic counter.

## What changes, and what does not

With |2q-t|<=D, either child differs from t/2 by at most D/2. Thus a
bounded-defect branch remains within D*(1-2^(-j)) of t_0/2^j after j
steps. Random branch choice alone does not escape the fixed-center menu
control. It does allow cheaply generated, highly unbalanced count splits
without discarding a route for a poor worst-case path length.

The next discriminating calculation is the exact small-input recurrence,
paired with the minimum-child rule for the same source parameters. If
that exposes a useful difference, compare the branch laws on the already
specified biased rational sources, charging generation, both child
screens, all failed attempts, and the branch bits. Do not infer a
success-probability theorem from the work bound or finite improvements.
