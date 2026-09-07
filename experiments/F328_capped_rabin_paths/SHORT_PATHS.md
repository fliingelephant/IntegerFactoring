# Short sampled paths and an exact inverse-endpoint identity

**Family:** route:F31

Status: root interpretation and elementary derivation. Not independently
reconstructed, not a novelty claim, and not a short-path probability theorem.

Three of the 32 retained 28-bit trials already factor at cap 32:

| Modulus ID | Trial | Matching | Terminal F call |
| --- | --- | --- | --- |
| b28_i0 | 4 | rank reflection | 7 |
| b28_i0 | 10 | delete-adjacent | 31 |
| b28_i1 | 12 | rank reflection | 25 |

All three endpoints are nonunits. These isolated successes suggest examining
their arithmetic branches. They do not establish a probability gain, and
choosing filters after seeing their offline factors would not be a public
algorithm.

Here is a useful exact simplification for that examination. Keep the F326
notation h=(N-1)/2 and

    Q(t) = #{1<=y<=t : rep(a*y)>0}.

For a unit a and 1<=t<=h:

    a*t =  1 mod N  implies  Q(t)=ceil(t/2),
    a*t = -1 mod N  implies  Q(t)=floor(t/2).

For the first identity, pair y and t-y in 1,...,t-1. Their residues under
multiplication by a sum to 1 modulo N. One is positive and one negative
except when both residues are (N+1)/2. This exception occurs exactly at
y=t/2 when t is even, and contributes a negative residue. The endpoint
y=t contributes the positive residue 1. Counting the pairs gives ceil(t/2).

For the second identity, the paired residues sum to -1. The sole possible
same-sign exception is the positive residue h at y=t/2 when t is even.
The endpoint contributes -1, which is negative. The resulting count is
floor(t/2). In either argument, when t is odd the candidate exceptional
index is (t+N)/2>t and therefore absent. Only invertibility of a and oddness
of N were used, so repeated factors cause no change.

For example, suppose 1<a<=h and t=rep(a^(-1))>0. Under F326's
rank-reflection auxiliary with start coordinate zero, the first two moving
F/A stages have current coordinates

    0 -> -1 -> ceil(t/2).

Indeed, F(0)=1 and the nearest accepted negative coordinate is -1. Next,
F(-1)=-t; reflecting its rank returns the positive coordinate Q(t), to which
the first identity applies. This is a constant-length algebraic shortcut,
not a solution of the remaining path. After substituting t=2v or 2v-1,
later branch equations can be examined for longer families of short paths.
Their public occurrence probability and total attempt cost must still be
proved; completing every path is unnecessary.
