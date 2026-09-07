# What the uniform proposal control measures

**Family:** route:F31

Status: root-derived counting observations. Not independently reconstructed
or promoted. These bounds concern uniform unit multipliers, not the adaptive
path-derived multiplier distribution.

## Ordinary-square proposals

Fix odd N and a unit square a. A uniform unit c makes b=a*c^2 uniform over
the unit squares. If N has s distinct prime divisors, that image has size
phi(N)/2^s. Put M=floor(sqrt(N-1)) and

    A_M = #{1<=k<=M : gcd(k,N)=1}.

The ordinary integer squares k^2 in [1,N-1] are distinct residues. Exactly
A_M of them are unit squares. Therefore one conditional-unit proposal has
ordinary-square output probability

    2^s*A_M/phi(N).

With the independent hidden-root protocol, its proper-factor probability
through this particular output is (2^s-2)*A_M/phi(N). This is P02 applied
after public root pullback. Generation gcds and path outputs are different
events and are not included in this formula.

The law holds conditional on every public past before a fresh uniform unit
multiplier. Selecting a previous small-score proposal does not itself bias
the next uniform proposal. It can affect the intervening path probe, so this
observation is not a bound for the whole feedback controller.

## A nearest-square gcd on a semiprime

Let N=p*q for distinct odd primes p<q. For b in [1,N-1], let k^2 be the
nearest ordinary integer square and put delta=b-k^2. There is no integer tie
between consecutive squares. The cell for k is

    k^2-k+1 <= b <= k^2+k,

intersected with [1,N-1]. Thus -k+1<=delta<=k. Write
K=ceil(sqrt(N-1)). Because q>=p+2,

    (q-1)^2 - N = q*(q-p-2)+1 > 0,

so K<q. Consequently every nonzero delta has |delta|<q. A proper gcd
gcd(delta,N) can therefore only be p: this screen cannot directly return q.
In particular, no nonzero score smaller than p can yield a factor.

For a given k, the number of nonzero multiples of p in its full difference
cell is floor(k/p)+floor((k-1)/p). Therefore the number of b values producing
a proper gcd is at most

    sum_(k=1)^K [floor(k/p)+floor((k-1)/p)] <= K^2/p.

Restricting b to unit squares can only reduce this count. A uniform unit-
square proposal consequently has proper-gcd probability at most

    min(1, 4*K^2/(p*phi(N))).

This is an O(1/p) bound for semiprimes. If K<2p, the only possible nonzero
factor scores are delta=+p or delta=-p. This describes the particular
nearest-square screen; it is not an obstruction to other decoders or to a
nonuniform, correlated source of proposals.

The feedback score thus has two distinct objectives. Reaching zero gives a
verifiable modular root, but merely reducing a nonzero score below the least
factor removes the direct-gcd event. Whether the resulting public state makes
the next arithmetic path more useful still needs evidence and a probability
bound. No global search lower bound follows from this local observation.
