# Statement for independent reconstruction

Let M=2^k with k>=3, and let epsilon be an odd integer. Let U be the
canonical odd residues in [0,M). Define the two permutations

    s(w)=M-w,
    i(w)=epsilon*w^(-1) mod M in [0,M).

For an integer-valued function f on U, put

    H_epsilon(f)=sum_(w in U) f(w)*f(i(w)),
    U2(f)=sum_(w in U) f(w)^2,
    Q_epsilon(f)=H_epsilon(f)-U2(f).

Claim: for every integer p>=3 and any two integer-valued functions r,g
on U satisfying

    r(s(w))=-r(w),
    g(s(w))=-g(w),
    r(w)=g(w) mod 2^(p-2) for every w in U,

one has

    Q_epsilon(r)=Q_epsilon(g) mod 2^p.

There is no promise about the roots of epsilon or -epsilon modulo M;
fixed points of i and points satisfying i(w)=s(w) are included. Negative
function values and arbitrary odd epsilon are allowed.

The following corollary is also claimed. For canonical odd 0<A<M, let
f(w)=floor(Aw/M) and h=(A-1)/2. Choose g on w<M/2 as the canonical
residue of f(w)-h modulo 2^(p-2), and define g(M-w)=-g(w). Then

    H_epsilon(f)=U2(f)+H_epsilon(g)-U2(g) mod 2^p.

For p=3 the function g takes values in {-1,0,1}. The corollary does not
compute H_epsilon(g). It compresses the value alphabet, not the graph
modulus, number of summands, or requested output precision. No runtime
or factoring claim is made. No external theorem is a declared dependency.

Please reconstruct the claim, including all exceptional orbits and
division/integrality details, from this statement alone. Do not read
the author proof, other packet files, or shared ledger bodies.
