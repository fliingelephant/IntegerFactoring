# Inverse-source gap ranks transfer to a smaller modulus

**Family:** route:F31

Status: root derivation for direct finite checking. Not independently
reconstructed or promoted. This is a diagnostic addition to the frozen
random-window pilot, not a change of its sampler.

## Exact cluster law

Let N>1 be odd, 2<=b<N, gcd(b,N)=1, and a=b^(-1) mod N in [1,N-1].
For 1<=t<N put m=t+1 and assume b<=m. Write

    m=b*L+r,  0<=r<b,
    sigma_j=(-N*j mod b),  0<=j<b.

The sorted set {0,a,...,t*a} modulo N consists, in order, of the b
clusters

    {(N*j+sigma_j)/b + k : 0<=k<L+1_{sigma_j<r}},
    j=0,...,b-1.

All quantities are integers. Indeed, put c=(b*a-1)/N. Then c is a unit
modulo b and c^(-1)=-N mod b. Orbit indices in residue class sigma_j
modulo b have the form sigma_j+b*k; their residues modulo N start at
(N*j+sigma_j)/b and increase by one. There are exactly L+1_{sigma_j<r}
such indices in [0,t]. If d_j=(t-sigma_j mod b), the gap from the end of
cluster j to the start of the next cluster is

    (N-t+sigma_(j+1)+d_j)/b > 0,

with the last cluster followed by N and sigma_b=0. This proves the
ordering, absence of wrap within a cluster, and full coverage.

Define A(j)=#{0<=k<=j: sigma_k<r}. The sorted rank of the final point
of cluster j is exactly

    R_j=L*(j+1)+A(j)-1.

Thus the b boundary ranks can be evaluated by modular floor sums at the
smaller public modulus b. The original modulus N enters this count only
through N mod b and the explicit quotient L. Building the entire sorted
orbit is unnecessary for the identity or for evaluating a selected R_j.

## A half-orbit residual identity

Now take t=(N-1)/2, so 2bL=N+1-2r. For 0<=k<l<b let d=l-k and
z=A(l)-A(k). Then

    2b*(R_l-R_k) = N*d + E,
    E=(1-2r)*d+2b*z,
    gcd(R_l-R_k,N)=gcd(E,N).

For r=0, z=0 and E=d. For r>=1, 0<=z<=d and the two endpoint
coefficients lie between 1-2r and 2b+1-2r. Consequently

    0<|E|<2b^2.

The strict lower bound follows without a distribution assumption:
0<R_l-R_k<N and gcd(2b,N)=1 rule out E=0. Therefore, if the least prime
divisor of N exceeds 2b^2, no difference of two cluster-boundary ranks
has a proper gcd with N.

This concerns precisely the boundary ranks, which follow the possibly
large gaps. It does not forbid factors from other ranks or other starts,
and does not apply when b is numerically large. It illustrates why a
large total gap mass need not be useful off-diagonal collision mass.

## Finite diagnostic

For existing inverse-source pilot cells with b<=t+1, compare all cluster
starts, lengths and boundary ranks to the explicitly sorted orbit. For
t=(N-1)/2 also check the residual identity, nonzero bound and gcd equality
for boundary pairs. This uses offline arrays only to check an exact public
formula. Neither hidden factors nor these energies may choose the pilot's
actual parameters or sampling law.
