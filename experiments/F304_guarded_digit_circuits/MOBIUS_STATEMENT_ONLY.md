# Statement for independent reconstruction

Let s>=1, L=2^s, let A,B be odd integers, let C be a positive even
integer, and let n be any integer. Put K=AB+Cn, which is odd. For every
integer x in [0,L), define

    D(x)=B+Cx,
    T(x)=(n-Ax)/D(x) in Z_2,
    y(x)=T(x) mod L in [0,L),
    q_x=[D(x)y(x)-(n-Ax)]/L.

All denominators D(x) are odd and every q_x is an integer. Exponents below
are nonnegative integers, and zero to exponent zero means1.

Claim: for every numerical degree bound d>=0, there is a uniform
deterministic algorithm computing

    S_ij=sum_(0<=x<L) x^i y(x)^j mod L^2, 0<=i,j<=d,
    Q_j=sum_(0<=x<L) q_x T(x)^j/D(x) mod L, 0<=j<=d,

in bit complexity polynomial in s, the numerical bound d, and the binary
lengths of A,B,C,n. The algorithm does not enumerate the L canonical
arguments or their image values. It receives no factors of K, no
precomputed list of the permutation, and no numerical-length advice.
All modular divisions by even numbers must be justified by integer
divisibility and guard precision. Modular inverses may be used only for
odd elements.

Canonical graph coordinates in this statement matter. It is not enough
to compute S_ij modulo L, moments of the 2-adic rational T(x) in place of
y(x), or normalized moments by dividing residues whose guards are absent.
Retain the full n in q_x. No cost polynomial in the binary length of d is
claimed; d is a numerical bank bound.

Elementary identities for power sums, elementary symmetric functions,
formal power series with unit constant coefficients, and finite binomial
expansions over powers of two may be derived and used. No external
algorithm is a declared dependency.

Please reconstruct a complete algorithm and its precision and bit-cost
bounds from this statement alone. The claim supplies one-map modular
moments. It claims no fast union over a family of maps, no integer interval
count, no Archimedean approximation and no factoring algorithm. Do not
read author proofs, other packet files or shared ledgers.
