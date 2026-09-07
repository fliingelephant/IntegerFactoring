# The next cocycle precision and its guarded half-modulus transform

**Family:** route:F31

Route F31. Status: author-derived candidate and bounded exploratory result.
F313 is unchanged while its statement undergoes independent reconstruction.
This packet does **not** construct K modulo 8 or T modulo 8. It derives and
tests an exact half-modulus transform, including a specific lower-precision
mixed-section correction that remains unevaluated. No novelty or factoring
claim is made.

## Mechanism and inspected scope

The proposed mechanism was to lift the canonical section to modulo 4M,
preserve the integer cross terms that vanish only in characteristic two,
and then combine the two half-period projections with their actual guard
bit. F313 and P238 are the closest inspected records. The coefficient
identities below are finite derivations, not a literature-based assumption.
No new source was fetched.

Throughout M=2^k and T=M/4. The modulo-4 carry formulas below use k>=4.
The half-period recursion uses k>=5. Smaller cases are finite base cases;
they are not silently included in the stable half-period identity.

## Canonical section modulo 4M

For 0<=j<T define

    e_j=floor((5^j mod 4M)/M) in {0,1,2,3},
    eta_j=e_j mod 2,
    E(z)=sum e_j z^j,  J(z)=sum z^j,
    I_a(z)=sum_(T-a<=j<T) z^j.

Work in (Z/4Z)[z]/(z^T-1). For unsigned A=5^a mod M, A=1 modulo 4,
the canonical carry word modulo 4 is

    C_a(j)=floor(A*(5^j mod M)/M) mod 4
          =3 floor((a+j)/T)-e_a-e_j+e_(a+j mod T),             (1)
    C_a(z)=I_a(z)[3+(1-z)E(z)]-e_a J(z).                      (2)

Indeed 5^T=1+3M modulo 4M. Every unsigned canonical residue is 1 modulo
4, so multiplying by (1+M)^r changes its additive high digit by r. This
gives (1), including the sign of the section coboundary. Also
(1-z)I_a=z^(-a)-1, which gives (2).

Let S_M(r)=[z^r]E(z)^2 modulo 4, with r reduced modulo T. The complete
inverse-paired carry product satisfies

    [z^0]C_a C_b = max(0,a+b-T+1)+2 L_(a,b)
       +S_M(0)-S_M(a)-S_M(b)+S_M(a+b)
       -3[b e_a+a e_b]                              (mod 4), (3)
    L_(a,b)=sum_(j=T-a..T-1) [e_(b-j)-e_(-j)].

The linear term is needed only modulo 2. In deriving (3), J^2=TJ=0
modulo 4 and J[3+(1-z)E]=3J are used with their stated k>=4 guard.

The four-valued section does simplify in this square:

    E=eta+2xi implies E^2=eta^2 mod 4.                        (4)

Thus the second section digit survives in the point terms e_a,e_b, but
does not create a new array in S_M. This is not permission to replace
the square by its characteristic-two value: off-diagonal pairs still
contribute twice their products. For M=16,a=b=1, dropping the linear
term in (3) predicts 2 instead of the actual 0 modulo 4.

For unsigned A,B, sign pairing relates (3) to the original K/2 by
subtracting h_B sum C_a+h_A sum C_b, where h_A=(A-1)/2. Those linear
sums are ordinary floor marginals. General signs are handled by the
centered relation F_(-A)(w)=1-F_A(w) modulo 4 for w=1 modulo 4, with
F_A=f_A-h_A. This does not construct the remaining S terms.

## A genuine smaller-section projection

Put H=T/2 and L=M/2. For j<H define

    s_j=floor((5^j mod M)/L) in {0,1},
    B_j=1-s_j,
    P_j=eta_j,
    D_j=B_j+2*(j mod 2).

The word s is the binary canonical section at the **smaller graph modulus
L**. The word P is the first half of the current binary section; these are
different words and must not be identified.

For k>=5, 5^H=1-L modulo 4M and 5^j=1+4(j mod 2) modulo 8. Expanding the
product and retaining the canonical borrow gives

    e_(j+H)=e_j-D_j mod 4.                                   (5)

Write E=E0+z^H E1. Squaring and projecting onto z^H=1 or z^H=-1 gives

    S_M(r)+S_M(r+H)=[z^r]B(z)^2 mod (4,z^H-1),
    S_M(r)-S_M(r+H)=[z^r]B(z)^2 mod (4,z^H+1),  0<=r<H.       (6)

The second square is negacyclic: a coefficient that wraps by H has a
minus sign. Formula (6) is a real half-modulus transformation, not a
change of names at the old conductor.

It is also not an invertible pair of congruences modulo 4. Adding the
two projected residues and dividing by 2 requires their values modulo 8.
On actual canonical data M=32,r=0, both projections are 1 modulo 4 but
S_M(0)=3 modulo 4. Choosing the displayed residues and dividing gives
the incorrect answer 1. The lost bit is present in the faithful family.

## Retaining the guard bit gives one explicit mixed correction

The missing bit can be written exactly. Squaring a coefficient lift
changed by 4 does not change its square polynomial modulo 8. Hence (5)
is enough to compute the two projections modulo 8 symbolically:

    (E0+E1)^2=D^2+4(E0^2-E0 D) mod (8,z^H-1),
    (E0-E1)^2=D^2              mod (8,z^H+1).

Now combine these identities and divide in the integers. For 0<=r<H,

    S_M(r)= sum_(j=0..r) B_j B_(r-j)
          +2( [z^r]P^2-[z^r]PB )                 (mod 4),    (7)

where the two bracketed products are cyclic modulo z^H-1 and are needed
only modulo 2. The first term is an **ordinary truncated convolution**,
not a cyclic coefficient; the wrap terms cancel in the guarded sum.

The P^2 coefficient is computable from at most two point values by
characteristic-two squaring. The surviving term is specifically

    [z^r]PB mod 2
      =sum_(j=0..H-1) highbit_M(5^j mod 2M)
                  *[1-highbit_L(5^(r-j mod H) mod M)] mod 2. (8)

Thus the transform has one lower-section truncated square modulo 4,
one point-value term, and one mixed high/low-section correlation modulo
2. At M=32,r=0 the prefix term is 1, the point term is 0, and the mixed
bit is 1; together they correctly return 3. Dropping (8) returns 1.

This identifies an actual lower-precision correction with its exact
canonical arguments. It is not an evaluator for that correction. In
particular, F313's complete square cancellation does not apply to a
product of these two distinct section words. The truncation in the
first term also remains a real boundary.

One application of (7) has a constant number of scalar subproblems and
polynomial additional bit work. Repetition has not been shown to keep a
closed polynomial-size bank: the mixed word in (8) retains a digit from
the larger lift, and the truncated square introduces an endpoint. No
total quasipolynomial state bound is asserted. The two projections in
(6) alone do not fix this gap.

## Exact transport identity at this precision

For an unsigned A=5^a mod M, let

    L_a=sum_(r=1..a)(e_r+e_(T-r)),
    R_a=sum_j e_j e_(j+a),  R_0=sum_j e_j^2.

The directly checked next-precision identity is

    T(A,0)/2=2a+L_a+S_M(0)-S_M(a)+R_0-R_a-(A-1)/2 mod 4.   (9)

Proof: on the unsigned sign representatives, u=1 modulo 4, so mu=u q
equals q modulo 4. The inverse carry word is
Q=3(J-1)-E-E(z^-1). Sign pairing gives
T/2=[z^0](Q-J)C_a-h_A sum q. Expand with (2). The complete binary
section has even sum, so the terms 2e_a sum e_j vanish modulo 4;
sum q is odd and h_A is even. The remaining terms give (9).

At this precision the ordinary section autocorrelation and the prefix
correction must remain together. This packet has not reduced their
combination, together with the new S term, to the linear window used in
F313. Equation (9) is an exact diagnostic, not a new T constructor.

For opposite signs the known sign-pair marginal gives
T(M-A,0)/2=sum_(w=1 mod 4)q(w)-T(A,0)/2 modulo 4. This is a consistency
relation, not a new solution for its unknown unsigned term.

## Full-cut scope

These identities use complete exponent cycles and unshifted sign pairs.
An input or output cut inserts a nonconstant mask. It must be retained
in the products and changes the endpoint family in (7). There is no
claim that arbitrary coboundaries or cut masks disappear. The mixed
correlation and truncated endpoint are the explicit current gaps; the
remaining task is their aggregation, not a larger convolution table.

## Evidence and resources

`pilot.py`, `pilot.json`, and `pilot.log` retain the exact source, seed
316, outputs and separating failures. For M=16 through 512, the pilot
checked 6,048 canonical modulo-4 carries, 144 inverse-paired products,
144 transport identities, 252 section-square replacements, and 124
half-modulus projections and guarded recursions. Both omitted-linear
and unguarded-division failures remain in the output.

The final pilot took 0.010 seconds and 17,612,800 bytes peak RSS. Its
estimate was below one second and 32 MiB, with a 30-second alarm. The
shared preflight supplied by the root reported about 70% free memory,
zero swap, load 1.98/2.12/2.20, and no large research process. No balanced
k128 marginal benchmark was rerun, no large table was built, and no
shared record or F313 file was changed.
