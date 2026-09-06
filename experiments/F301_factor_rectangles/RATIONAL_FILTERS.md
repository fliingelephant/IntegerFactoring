# Short rational windows and the global mixed resolvent they require

**Family:** route:F31

**Status:** root-derived construction and bit-cost arguments, with exact
integer and interval checks. Independent statement-only reconstruction of
this filter/resolvent extension is pending. The separate public rectangle
reduction has its own blind reconstruction. No mixed resolvent algorithm is
supplied here.

## Replace a discrete step by a bounded rational function

Let M=2^k, L=k+1, and choose an even positive s with 3^s>=32M. Define

    a_j=2^j, 0<=j<=L,
    P_+(X)=product_j(X+a_j), P_-(X)=product_j(X-a_j),
    W(X)=P_+(X)^s/(P_+(X)^s+P_-(X)^s), R(X)=2W(X)-1.

The denominator is positive for every real X: both powers are nonnegative
and the two products have disjoint root sets. Thus 0<=W<=1, and
W(-X)=1-W(X). If1<=X<=2M, choose a dyadic a_j in[X/2,X]. Then

    |(X-a_j)/(X+a_j)|<=1/3,

while every other factor has magnitude at most one. Hence

    1-W(X)<=3^(-s), W(-X)<=3^(-s).                     (1)

The numerator and denominator degrees are D=s(L+1)=O((log M)^2), and their
integer coefficient bit lengths are O((log M)^3). The products themselves
are also short exact descriptions.

This is a simple product-form rational sign approximation. That mechanism
is classical: compare Newman's Theorem(A) and product construction in
[Rational Approximation to |x|,1964](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/NEW64.pdf).
The present dyadic scales, even repetition, and bounds are derived above;
no novelty claim is made for rational approximation of a step.

For an integer interval I=[A,B] contained in[1,M-1], set

    Phi_I(u)=W(2u-2A+1)*W(2B+1-2u).                  (2)

At every integer0<=u<M the two arguments are nonzero odd integers of
magnitude less than2M. Equation(1) gives

    0<=Phi_I(u)<=1,
    |Phi_I(u)-1_(u in I)|<=2*3^(-s).                  (3)

For odd N, let v_N(u)=N*u^(-1) modM on odd units. For two such intervals,

    S_N(I,J)=sum_(1<=u<M,u odd) Phi_I(u)*Phi_J(v_N(u)),
    C_N(I,J)=#{1<=u<M,u odd:u in I,v_N(u) in J}.

The product error is at most4*3^(-s) at each point. Therefore

    |S_N(I,J)-C_N(I,J)|<=4M*3^(-s)<=1/8.              (4)

An additional absolute evaluation error below1/8 still allows exact integer
recovery by rounding. This applies to the original inverse graph, all public
factor rectangles, and every bisection subrectangle; it does not operate
only inside a selected u0 chart. It also does not evaluate the sum S_N.

## The poles have controlled location and positive residues

Write A_sum=sum_j a_j=2^(L+1)-1 and B(X)=P_-(X)/P_+(X). Away from the
cancelled intermediate denominators,

    R(X)=(1-B(X)^s)/(1+B(X)^s).

For Re(X)>0 every factor of B has modulus less than one; for Re(X)<0 every
factor has modulus greater than one. Thus every pole of R is purely
imaginary. There are no poles at0 or at the real roots of P_+ or P_-.

For y>0 define

    theta(y)=2s*sum_j arctan(a_j/y).

It decreases strictly from pi*D to0. Its crossings of the odd multiples
of pi give exactly D/2 positive pole heights y_h, with their negatives.
All poles are simple. The residue at either i*y_h or-i*y_h is

    rho_h=1/[s*sum_j a_j/(a_j^2+y_h^2)]>0.             (5)

Since R(X) tends to s*A_sum/X at infinity, partial fractions give

    R(X)=sum_(h=1)^(D/2) 2*rho_h*X/(X^2+y_h^2),
    sum_h 2*rho_h=s*A_sum.                            (6)

These statements also follow directly by differentiating1+B(X)^s at its
zeros. No polynomial term or unrecorded complex phase remains.

The arctangent bounds supply useful explicit conditioning:

    y_min>=pi/(4s), y_max<=2s*A_sum/pi,
    successive positive y values differ by at least pi/(2s).    (7)

For the first inequality, the phase drop from y=0 to the smallest root is
pi, and 2s*sum arctan(y/a_j)<=2s*y*sum(1/a_j)<=4s*y. For the largest root,
pi=2s*sum arctan(a_j/y)<=2s*A_sum/y. Finally,
|theta'(y)|<=2s*sum(1/a_j)<=4s; adjacent roots have phase gap2pi.

The pole heights can be approximated with polynomial bit cost in log M and
the requested precision. Bisect the monotone phase on[0,2s*A_sum]. On this
interval its derivative magnitude is at least

    2s*A_sum/[(2s*A_sum)^2+max(a_j)^2].                (8)

This lower bound has O(log M+log s) bits of conditioning. Certified
arctangent evaluation and(8) handle a midpoint whose phase interval contains
the target, so the method need not wait for an undecidable exact comparison.
The residues then follow from(5). All roots, coefficients, and intermediate
precision requirements have polynomial-size descriptions.

## A window becomes a short sum of ordinary Cauchy poles

The first factor in(2) has real pole coordinate A-1/2; the second has real
pole coordinate B+1/2. Their imaginary heights are +/-y_h/2. The two real
coordinates differ by B-A+1>=1, so the two pole sets cannot collide.
Each step has constant part1/2 and total absolute residue s*A_sum/4 in
the variable u. Put C=s*A_sum/4. Partial fractions of their product give

    Phi_I(u)=1/4+sum_z alpha_(I,z)/(u-z),              (9)
    number of poles<=2D,
    sum_z |alpha_(I,z)|<=C+2C^2.                     (10)

Indeed a residue of one step is multiplied by the other step's value at
that pole. Its modulus is at most1/2+C because the cross-set distance is
at least one. Summing the two sets proves(10).

Every real part in(9) is an exact half-integer. Its distance to every integer
u is at least1/2, including during approximation of the imaginary parts.
There is therefore no hidden exponentially small distance to a graph point.
Residue and parameter approximation only needs O(log M) additional bits
for the polynomial-in-M coefficient bounds; it does not need M bits.

## The actual remaining global kernel

Define the ordinary coordinate resolvents

    H_M(z)=sum_(1<=u<M,u odd) 1/(u-z),
    Z_(N,M)(z,w)=sum_(1<=u<M,u odd) 1/[(u-z)*(v_N(u)-w)].    (11)

Substitution of(9) into the finite sum is exact:

    S_N(I,J)=phi(M)/16
       +(1/4)*sum_z alpha_(I,z)*H_M(z)
       +(1/4)*sum_w alpha_(J,w)*H_M(w)
       +sum_(z,w) alpha_(I,z)*alpha_(J,w)*Z_(N,M)(z,w). (12)

The v marginal is H_M because v_N permutes the odd units. The number of
mixed calls is O(D^2)=O((log M)^4). If B=C+2C^2, the total absolute mixed
coefficient norm is at most B^2. Thus absolute precision2^(-O(log M)) in
the individual calls suffices for the constant error budget in(4), with
slightly tighter precision for the pole/residue approximations. The
half-integer real parts keep the same bounds along those perturbations.

The marginal H_M has a direct polynomial-bit approximation. Partition the
odd integers to either side of Re(z) into dyadic distance shells starting
at distance1/2. There are O(log M) intervals. At each shell center the
deviation-to-denominator ratio is at most1/3; expand its reciprocal as a
geometric series. Degree O(p+log M) gives error2^(-p), and the polynomial
moments on each arithmetic progression are computed by exact finite-sum
recurrences. All numbers need polynomially many bits. This calculation
does not use v_N or factor information.

The mixed Z is uncomputed. A uniform quasipolynomial-bit evaluator for(11)
at these O(log M)-bit pole approximations and precision would, through(12),
(4), and the separately verified rectangle reduction, imply the requested
all-input factoring algorithm. The construction would use O(n^6) mixed
queries for complete factorization, up to fixed polynomial factors, plus
polynomial work. This is a conditional interface, not such an evaluator.

This Z is a sum over the entire original inverse graph, with *ordinary*
Cauchy denominators in canonical integer coordinates. P236 instead treats
a complete quadratic phase with a denominator1-t*e_m(bx). Neither it nor
the complete Salié identities supplies(11) without another proved step.
The short rational description of a window does not remove the joint
position correlation.

## Exact and interval computation

`rational_filters.py` checked131,064 exact integer inequalities from(1),
at every positive odd argument for moduli8 through65536. It then evaluated
67 public rectangles for seven original factoring inputs using200-bit real
interval arithmetic. Every interval, enlarged by the proved1/8 filter
error, contained exactly one integer: the direct modular count. It scanned
4,768 graph units, took0.781seconds after Sage startup, and used256,344,064
bytes peak RSS. This computation is certified but still enumerative.

`rational_poles.py` isolates the roots by monotone interval bisection and
checks positive residues, location/separation bounds, total residue mass,
and partial-fraction value enclosures. Its source and final JSON retain the
root intervals and precisions. The first run stopped on a Sage comparison
between different numeric parent types, after its first pole set had been
isolated. The comparison was changed to use the scalar lower endpoint;
the formula, error target, and failed log were preserved.
The successful run isolated93 positive poles to width at most2^(-70) and
passed24 partial-fraction value checks at200-bit interval precision. It
took1.342seconds after startup and256,425,984bytes peak RSS.
Its successful guard is rational_poles_fixed.status.json; the first failed
guard remains in rational_poles.status.json.

Neither experiment accelerates the mixed graph kernel. Its purpose is to
make the analytic interface precise, with a controlled representation and
precision budget, so a subsequent global recursion can be tested against
the original factoring windows rather than only chart halfboxes.
