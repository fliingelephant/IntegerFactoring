# A Farey-spacing control for fixed orbit windows

**Family:** route:F31

Status: root-derived lemma, not independently reconstructed or promoted.
It concerns a fixed menu of coefficients, not all public functions of N.

Fix H>=21. Let P_H be the primes in [H,2H] and R=|P_H|. Fix a list of K
real coefficients alpha_i, independent of the particular pair of primes,
and a common error radius D>=1. For N=p*q with distinct p,q in P_H, test
only positive integers w<= (N-1)/2 in the windows

    |w-alpha_i*N|<=D.

At most

    2*R*K*(floor(8D)+1)

ordered distinct prime pairs can yield a proper gcd from this menu.

## Proof

Fix p and one alpha. If w=p*k is in the window, then 1<=k<q and

    |alpha-k/q|<=D/(p*q)<=D/H^2.

Because q is prime and 0<k<q, k/q is reduced. Two distinct reduced fractions
with denominators at most 2H are separated by at least1/(4H^2): their
cross-product numerator is a nonzero integer. An interval of length2D/H^2
therefore contains at most floor(8D)+1 such fractions. Each eligible q gives
one of these fractions, so there are at most that many prime cofactors q.
Sum over the K coefficients and R choices of p. Interchanging p and q gives
the same count for a q-divisible w. A proper nonunit for the semiprime must
fall into one of these two classes. The union bound proves the claim.

## Meaning of the restriction

Rosser--Schoenfeld's prime-interval bound, stated as a dependency in F335,
gives R>3H/(5 log H). If K*D is quasipolynomial in log H, the fraction of
eligible pairs tends to zero. This conclusion is uniform over the fixed
coefficient list, regardless of its denominators or how it was computed.
It is false to extend this count to an arbitrary alpha that changes with
the individual input N. When lists depend only on input bit length, the
three possible lengths across H^2<=N<=4H^2 can be combined in one list.

F335's separately author-derived triangular-wave model suggests a concrete
application. A fixed rational r/b may have a known reference orbit for
t/N, with error O(b+r) and a contractive or nonexpansive update. Its screened
counts then lie near N times fixed orbit coefficients. Before interpreting
success from short r,b as a new mechanism, enumerate that explicit window
menu and charge it. A whole small-height parameter family can sometimes
be included in the same menu. This application remains conditional on the
exact orbit/error bounds; it is not promoted by the abstract spacing proof.

The F336 experiment deliberately includes numerically large r,b, sampled
with only O(log N) bits. The error widths or the number of distinct orbit
coefficients can then be a numerical power of N, making direct enumeration
expensive. A fast sampled count could still be useful there. No success
probability or quasipolynomial factoring bound is asserted for that source.
