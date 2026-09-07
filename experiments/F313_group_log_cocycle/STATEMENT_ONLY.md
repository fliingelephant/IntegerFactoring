# Statements for independent reconstruction

Do not consult the candidate proof or implementation. Reconstruct the claims
below from the definitions and ordinary integer arithmetic. A failed
reconstruction is inconclusive. Record any additional hypothesis or weaker
conclusion explicitly.

Let k >= 3, M = 2^k, and L = M/4. All sums below run over canonical odd
residues w in [1,M). Let u(w) be the canonical inverse of w modulo M, and put
q(w) = (u(w)w - 1)/M and mu(w) = u(w)q(w). Define the exact integers

    K(A,B) = sum_w floor(Aw/M) floor(Bu(w)/M),
    T(N) = sum_w mu(w) floor(Nw/M).

For every canonical odd A in [1,M), write uniquely
A = (-1)^sigma_A 5^a modulo M, where sigma_A is 0 or 1 and 0 <= a < L.
Define eta_j = floor((5^j modulo 2M)/M) for 0 <= j < L. For an index r
reduced modulo L, define gamma_r = 0 if r is odd, and otherwise
gamma_r = eta_(r/2) + eta_(r/2+L/2) modulo 2.

Claim 1. K(A,B) is even for positive odd A and B. For canonical A and B
with exponents a and b,

    K(A,B)/2 = max(0,a+b-L+1) + b eta_a + a eta_b
               + gamma_0 + gamma_a + gamma_b + gamma_(a+b)
               + sigma_B a + sigma_A b                    modulo 2.

For positive raw A = A0 + M alpha and B = B0 + M beta, with canonical
A0,B0 and their coordinates as above, add alpha*b + beta*a modulo 2 to
the right side. There is no raw alpha*beta contribution modulo 2.

Claim 2. T(N) is even for every canonical odd N. Let its coordinates be
(sigma,a), let C = 5^a modulo 2M in [1,2M), and define the ordinary integer

    D = sum_(j=0..L-1) floor(C(1+4j)/M)
             - 2 sum_(j=0..L-1) floor(C(1+4j)/(2M)).

Then D-a is even and

    T(N)/2 = sigma + gamma_0 + gamma_a + eta_a + (D-a)/2 modulo 2.

Claim 3. These are uniform deterministic polynomial-bit algorithms for
K(A,B) modulo 4 and canonical T(N) modulo 4. Give explicit procedures and
bit bounds for coordinates, eta/gamma, and the two ordinary floor sums;
do not enumerate the group of size M/2. The claimed bound may be stated as
a conservative fixed polynomial in k and the raw input bit lengths.

For the optional raw-T corollary only, the declared dependency P238 supplies
Q0 = sum_w q(w) modulo 4 in deterministic polynomial bit complexity.
The claimed correction for raw positive N = N0 + M ell is
T(N) = T(N0) + ell*Q0 modulo 4. Verify that the division of this correction
by two is guarded by an even residue modulo four.

Scope: no shifted arguments, sharp interval masks, K modulo 8, T modulo M,
or factoring/counting algorithm is claimed.
