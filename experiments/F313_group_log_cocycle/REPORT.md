# Canonical group-log cocycle: all cross bits and the unshifted transport bit

**Family:** route:F31

Route F31. Status: the two modulo-four constructors are independently
reconstructed in P242, with exact enumerative controls and nonenumerative
large-bit implementations. No external novelty claim or factoring algorithm
is established. STATEMENT_ONLY.md and RECONSTRUCTION.md preserve the checked
scope and the unchanged verification inputs.

Two concrete polynomial-bit constructors are supplied for M=2^k, k>=3:

* K(A,B) modulo 4 for every positive odd A,B, including raw arguments.
* T(N,0) modulo 4 for every canonical odd N, with the explicit P238
  correction for raw positive N stated below.

The second constructor uses two ordinary linear floor sums. Neither scans
the unit group. Neither supplies shifted K_d, shifted T_c, modulo-M carries,
or the four-corner count in P239.

## The canonical section, derived before computation

Put T=M/4. Every canonical odd A has unique coordinates

    A=(-1)^sigma 5^a mod M,  sigma in {0,1},  0<=a<T.

Let

    eta_j = floor((5^j mod 2M)/M),  0<=j<T.

The standard lift (-1)^sigma 5^j modulo 2M has high bit eta_j+sigma
modulo 2. Multiplying it by (1+M) to that power gives the canonical lift
below M. Also 5^T=1+M modulo 2M. Therefore the exact canonical product
carry has parity

    c_a(j)=floor(Aw/M) mod 2
      = floor((a+j)/T)+eta_a+eta_j+eta_((a+j) mod T) mod 2,     (1)

where w has exponent j, with either sign. Both signs cancel in (1). The
first term is the cyclic exponent-addition carry; the other terms are the
actual canonical-section coboundary. They are retained, not assumed zero.

The coordinates themselves have a polynomial-bit constructor. Determine
sigma from A modulo 4. Starting at 5^0, successively choose exponent bit j
to match the target modulo 2^(j+3). The element 5^(2^j) changes exactly
the next unmatched bit. This uses O(k) modular squarings/multiplications
on O(k)-bit integers. Each eta value uses ordinary binary modular
exponentiation on the same bit sizes.

## Complete inverse-paired cross product

Work in F2[z]/(z^T-1). Write

    E(z)=sum eta_j z^j,
    J(z)=sum_(0<=j<T) z^j,
    I_a(z)=sum_(T-a<=j<T) z^j,  with I_0=0.

The carry word C_a(z)=sum c_a(j)z^j satisfies

    (1+z)I_a=1+z^(-a),
    C_a=I_a[1+(1+z)E]+eta_a J.                              (2)

Since T is even, J^2=0 and J(1+z)=0. Squaring in characteristic two, the
coefficient needed for an inverse-paired product is consequently

    [z^0] C_a C_b
      = [z^0] I_a I_b
        +[z^0](1+z^(-a))(1+z^(-b))E^2
        +b eta_a+a eta_b.                                  (3)

Only four coefficients of E^2 remain. For r reduced modulo T, define

    gamma_r=0                                      if r is odd,
    gamma_r=eta_(r/2)+eta_(r/2+T/2) mod 2            if r is even.

Thus each gamma uses two modular exponentiations, rather than a section-word
sum. The interval overlap in (3) equals

    [z^0]I_a I_b=max(0,a+b-T+1) mod 2.

For sign coordinates sigma_A,sigma_B, pair w with M-w in the original K.
If f_A(w)=floor(Aw/M), then f_A(-w)=A-1-f_A(w). Hence K is even and

    K(A,B)/2
      = sum_j c_a(j)c_b(-j)+sigma_B*a+sigma_A*b mod 2.          (4)

Here sum c_a(j)=a modulo 2 follows directly from (1). Combining (3),(4),

    K(A,B)/2 = max(0,a+b-T+1)+b eta_a+a eta_b
       +gamma_0+gamma_a+gamma_b+gamma_(a+b)
       +sigma_B*a+sigma_A*b                                  (mod 2). (5)

Equation (5) computes every canonical cross bit. It contains the previous
diagonal modulo-4 result as a special case, but does not require A=B.

For raw positive odd A=A0+M alpha and B=B0+M beta, use their canonical
coordinates and add alpha*b+beta*a to (5). This follows from
f_A(w)=f_A0(w)+alpha*w and w odd. The division by 2 is made only after
the proof that K is even; the returned residue is twice the computed bit.

The section dependence has contracted to a fixed number of evaluations.
It has not disappeared for arbitrary coboundaries. For example, in the
formal case T=4,a=1,b=2, changing eta_1 changes the cross bit. The actual
eta is computed from the canonical powers of 5.

## Transport bit: reducing the remaining correlation to a linear window

Let u=w^-1 mod M, q(w)=(uw-1)/M, mu(w)=u q(w), and

    T(N,0)=sum mu(w) floor(Nw/M).

This is the unshifted fixed-measure transport of F305. It is even. Indeed,
mu(w)+mu(-w)=u^2+1 modulo M, and u^2+1=2 modulo 4. Pairing signs gives,
for N=(-1)^sigma 5^a modulo M,

    t(N):=T(N,0)/2
      = sigma+a+sum_j q_j c_a(j) mod 2,                       (6)

where

    q_j = 1(j!=0)+eta_j+eta_(-j) mod 2.

To check (6) directly, the sign-pair contribution is
(q_j+1)c_a(j)+sigma*q_j modulo 2. The total sum of q_j is 1: pairs j,-j
cancel, while j=T/2 contributes 1 and j=0 contributes 0.

Let Ebar(z)=E(z^-1). The q word is J+1+E+Ebar. Expanding (6) using (2)
and collecting the terms gives

    t(N)=sigma+gamma_0+gamma_a+H+R_a+L_a mod 2,                (7)
    H=sum_j eta_j,
    R_a=sum_j eta_j eta_(j+a),
    L_a=sum_(r=1..a) (eta_r+eta_(T-r)).

Indices in H,R are cyclic modulo T. The section correlation and the
apparent prefix term in (7) must both be retained until the following
cancellation; discarding either gives the wrong formula.

Define the ordinary integer cyclic mismatch count and its wrap part by

    m_a=#{j<T: eta_j != eta_(j+a mod T)},
    w_a=#{T-a<=j<T: eta_j != eta_(j+a-T)}.

Then H+R_a=m_a/2 modulo 2, and L_a=w_a+eta_a modulo 2.

Extend eta to length 2T by its actual lifted high bit. Since 5^T=1+M,

    eta_(j+T)=eta_j+1 mod 2.

The mismatch count of this antiperiodic word under shift a is exactly

    2[m_a+a-2w_a].

On the other hand, the 2T powers of 5 are precisely the residues x=1
modulo 4 in [0,2M). Shifting the exponent by a multiplies x by
C=5^a mod 2M. Pairing x with x+M shows that this full mismatch count is
twice the following ordinary linear-window count:

    D_a=#{x<M: x=1 mod 4, Cx mod 2M>=M}.

It follows that D_a=m_a+a-2w_a. In particular D_a-a is even, with an
integer divisibility proof independent of numerical testing. Substitute in
(7) to obtain the constructor

    t(N)=sigma+gamma_0+gamma_a+eta_a+(D_a-a)/2 mod 2.           (8)

The count D_a is two ordinary floor sums:

    D_a=sum_(j=0..T-1) floor(C(1+4j)/M)
              -2 sum_(j=0..T-1) floor(C(1+4j)/(2M)).         (9)

Each term in the bracket is exactly the high-bit indicator, not a p-adic
approximation. The implementation computes (9) as exact integers using
the degree-one Euclidean floor recurrence, divides D_a-a by 2 in the
integers, and then reduces modulo 2. Thus (8) gives T(N,0) modulo 4 for
every canonical odd N, including all four square classes.

For raw N=N0+M ell, the exact correction is

    T(N,0)=T(N0,0)+ell*Q0 mod M,
    Q0=sum q(w).

P238 computes Q0 modulo 4; it is even by sign pairing. Hence add
ell*(Q0/2 modulo 2) to (8). This is a guarded division of an even residue
modulo 4. The raw correction is stated as a composition with P238; the
new transport pilot directly checks canonical N.

## Actual bit cost

The two group logarithms for (5), or one for (8), use O(k) modular
multiplications. A constant number of eta/gamma values require O(k)
modular multiplications each. The Euclidean floor sums in (9) use O(k)
steps. Their exact sums have O(k) bits because the slope and range have
O(k)-bit inputs and the floor sums are bounded by O(M^2).

Both constructors therefore use polynomial bit complexity, for example
O(k^3) with schoolbook integer arithmetic and conservative division costs,
and polynomial space. They contain no loop over T or over odd units.
For raw inputs add their bit lengths to the preliminary quotient cost.

The polynomials E,J,I_a are proof devices only. The implementation does
not construct their coefficient arrays. The bulk section correlation in
(7) is also never constructed: the exact canonical lifted word turns it,
together with the prefix correction, into the linear count (9).

## Cut and precision boundaries

All successful contractions above use complete, unshifted sign classes.
For K_d or T_c, an arbitrary sharp cut inserts a nonconstant mask into the
group coefficient sum. Equations (2),(3) then do not authorize dropping
that mask, and the antiperiodic mismatch identity does not automatically
give an unweighted linear window. The shifted sums may also be odd, so
the displayed sign-pair divisions are not their formulas.

This packet constructs one additional unshifted precision layer. It does
not construct K modulo 8, T modulo M, shifted binomial carries, or exact
rectangle counts. No Archimedean approximation is inferred from modulo-4
information. The square-class and raw-input coverage of this specific
layer does not remove P239's cut requirements.

## Retained evidence

`pilot.py/json/log` check 508 group logs, 720 canonical cocycles, 720 full
cross residues modulo 4, and 720 raw cross residues for M=8 through 512.
The smaller moduli use all input pairs; larger ones use seed 313. The
nonenumerative k=256 cross computation took 0.00058 seconds.

`transport_bit.py/json/log` check 708 canonical inputs for M=8 through
2048, including every odd input through M=512 and seed 3133 thereafter.
Every divisibility guard D_a=a modulo 2 and every predicted transport bit
passed. The nonenumerative k=512 constructor took 0.0015 seconds. The
two complete pilots each took less than 0.02 seconds and used less than
19 MB peak RSS. No failed case was dropped.

Preflight around 11:20 on 2026-09-07 reported a 16 GiB host, load averages
1.85,2.08,2.23, and no large research process in the busy-process snapshot.
The planned budget was 30 seconds and 256 MiB, with a below-one-second,
32 MiB estimate. Both pilots retained a 30-second alarm. No shared records,
prior source files, or commits were changed.
