# Proposed count-descent experiment

**Family:** route:F31

Status: next experiment design, not executed in F330. No probability bound or
factor-discovery improvement is asserted.

The retained seven-call path contains several x -> Q_a(x) stages. Test a new
partial procedure that deliberately keeps count descent and verifies factors,
without claiming to follow the old involution path.

For odd composite N and public unit a, start t=(N-1)/2. At each stage:

1. Check gcd(t,N), accepting a proper divisor.
2. Compute q=Q_a(t) with the existing exact floor sum.
3. Check proper gcds of both nonzero counts q and t-q with N.
4. If q is zero or t, return failure. Otherwise set t=min(q,t-q).
5. Stop with failure when t<=1.

Every continuing stage halves t, so one call makes O(log N) count queries
and has polynomial bit cost. This statement concerns work only. A useful
success probability is entirely unproved. The partial procedure returns only
verified factors, and is therefore a legal candidate for the F333 interface.

Compare fixed a against a control that resamples a fresh public unit at each
stage, accepting any generation gcd. Also compare t initially chosen as the
positive inverse representative min(a^(-1) mod N,N-a^(-1) mod N). The r=+/-1
identity supplies an exact control for that latter first count; its first
gcd may merely reproduce a gcd of a+1 or a-1 and must be labeled accordingly.

The first computation should enumerate small moduli and all Jacobi-positive
units, retaining actual success probabilities, count sequences and output
types. Then use independent public parameters on fixed larger inputs, with
every failure and all arithmetic/randomness charged. Compare per-input cost
per success and scope any zero only to the finite sample. Offline factors may
label where the descent first drops below the least factor, but must not
select a parameter, branch, or stopping rule.

Use the usual resource preflight and a small pilot before scaling. The precise
question is whether retaining one multiplier across count descents creates a
useful correlation, beyond the fresh-multiplier control. No arbitrary-cut
inverse counting oracle, hidden factor, or completed path is required.

## A dyadic-window control

Suppose every visited defect E_j=2Q_a(t_j)-t_j obeys |E_j|<=D, for example
using the separate continued-fraction certificate with a fixed public cutoff.
On each continuing stage,

    t_(j+1)=(t_j-|E_j|)/2.

Induction gives t_0/2^j-D(1-2^(-j))<=t_j<=t_0/2^j. Both screened child
counts at stage j therefore belong to the interval

    [t_0/2^(j+1)-D, t_0/2^(j+1)+D/2].

With fixed t_0=(N-1)/2 and fixed D, the union contains only O(D*log N)
integers and depends only on N and D. Directly gcd-screening this entire
menu is a necessary comparison: every successful bounded-defect descent
already has its factor-bearing count in that menu. This gives no general
obstruction when defects are large or starts vary; it prevents attributing
a new mechanism to a trajectory which merely selects from the same small
dyadic windows. Retain the actual maximum defect and whether the menu already
finds the observed factor. This control is a root-derived observation, not
part of the independently reconstructed P248 statement.
