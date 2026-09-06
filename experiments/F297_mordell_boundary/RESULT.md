# Centered theta endpoints and a uniformly short regular remainder

**Family:** route:F31

**Status:** root-derived identities, a uniform analytic remainder bound, and
finite checks. Independent statement-only reconstruction is not completed.
No outer moment evaluator or factoring complexity bound is claimed.

## A centered choice of the dual endpoint

Write e(x)=exp(2*pi*i*x) and

    F_n(alpha,t/2)=sum_(k=0)^n e(alpha*k+(t/2)*k^2),
    0<=alpha<1, 0<t<=1/2, X=n+1/2,
    r=floor(alpha+t*X), d=alpha+t*X-r, z=d-1/2.

Then 0<=d<1, -1/2<=z<1/2, and 0<=r<=floor(n/2)+1. This choice uses the
freedom to choose the dual endpoint in Kuznetsov's exact identity. It avoids
separately normalizing many different Mordell arguments. The constant-size
small-n cases can be summed directly.

There is a source-formula discrepancy to retain. Equation (7) in the cached
arXiv PDF visibly prints -1/2 for its second coefficient. F296 derives
-i/2 from the same paper's equations (16)--(17), retaining the other phases.
Its report preserves the PDF hash, printed image, failed printed-formula run,
an exact nonzero witness, and corrected checks. This packet uses that derived
version, not a claim that the cached equation already has the corrected i.
The source itself remains unchanged. P236 depends on Hiary's theorem and is
unaffected by this discrepancy.

For the derived identity, define

    E=(-1)^r e(alpha*X+(t/2)*X^2),
    Lambda=exp(pi*i/4)/sqrt(t),
    g_k=exp(-pi*i*(k-alpha)^2/t),
    eta=exp(-pi*i/4)*sqrt(pi/t),
    C0=-(i/2)*exp(-pi*i*(alpha-t/4))*h(alpha-t/2+1/2,-t).

Use the paper's Laplace integral

    J(w,t)=integral_0^infinity exp(-2*w*x+i*t*x^2/pi)/cosh(x) dx,
    R(z,t)=J(1+z,t)+J(1-z,t).

Combining its k=1 decomposition (27) with the derived theta identity gives

    F_n(alpha,t/2)
      = Lambda * [ sum_(k=0)^r g_k
                   - (1/2)*g_r*erfc(eta*d)
                   + (1/2)*g_(r+1)*erfc(eta*(1-d)) ]
        + C0 + i*E*R(z,-t)/(2*pi).                         (1)

This is an exact centered completed-prefix identity. The two erfc terms
remain explicit; the completion has not discarded the sharp endpoint.

The useful cancellation is elementary. Before inserting the erfc factors,

    E*exp(-pi*i*d^2/t)       = g_r,
    E*exp(-pi*i*(1-d)^2/t)   = -g_(r+1).                   (2)

For the first equality the remaining phase is exp(2*pi*i*r*(n+1))=1.
For the second it is exp(pi*i*(2*(r+1)*n+2*r+1))=-1. Thus the original
n^2 endpoint phase disappears into the dual phase at r or r+1. The identity
holds for any integer r; centering supplies the bounded argument interval.

## A uniform expansion for the whole regular remainder family

For any real t and |z|<=1/2, expand only the cosh factor:

    R(z,t)=sum_(j>=0) c_j(t)*(2*z)^(2j),
    c_j(t)=2/(2j)! * integral_0^infinity
                     x^(2j)*exp(-2*x+i*t*x^2/pi)/cosh(x) dx.

The bound 1/cosh(x)<=2*exp(-x) implies

    |c_j(t)| <= 4/3^(2j+1),
    |R(z,t)-sum_(j=0)^(K-1)c_j(t)*(2*z)^(2j)|
       <= (3/2)*9^(-K).                                  (3)

Indeed the coefficient integral is bounded by
4/(2j)! times integral x^(2j)*exp(-3x) dx. The resulting geometric
series proves (3), uniformly as t approaches zero. There is no inverse-t
loss in this regular part; the Fresnel endpoint terms carry that behavior.

Consequently, for any finite weights v_l and centered z_l,

    sum_l v_l*R(z_l,t)
       = sum_(j=0)^(K-1)c_j(t)*M_(2j) + error,
    M_(2j)=sum_l v_l*(2*z_l)^(2j),
    |error| <= (3/2)*9^(-K)*sum_l |v_l|.                 (4)

In (1), take v_l to include the original outer weight and E_l. Then only
O(p+log(2+sum|v_l|)) regular moments are needed for absolute error 2^(-p).
An exponential number of distinct arguments does not force an exponential
number of analytic basis functions.

For the relevant |t|<=1, the coefficients in (3) also have a constructive
polynomial-bit approximation procedure. On truncating at x=L, the omitted
part of every coefficient is at most 2*exp(-2L), because
x^(2j)/(2j)!<=exp(x). Take L=O(p+log(K+1)+1). On the remaining interval,
the integrand is analytic in a fixed-width complex strip: the nearest poles
of 1/cosh(x) have imaginary part pi/2. Its magnitude on radius-1/2 disks
centered on the real interval is bounded by exp(O(L+1)), uniformly in j
after the factorial normalization. Integrate its Taylor series on O(L)
subintervals of radius at most 1/4. Cauchy estimates give a geometric tail;
O(p+L+log(K+1)) Taylor terms suffice. Power-series arithmetic for the
polynomial, exponential, and reciprocal cosh uses polynomially many
operations and precision bits in K,p and the rational input length of t.
This supplies the coefficients; it does not supply the M_(2j).

## Absorb the bulk cut correction into four completed endpoints

F296 gives a simpler linear-floor endpoint R_j with r_j=R_j-delta_j,
delta_j in{0,1}. Instead of retaining that indicator as a separate recursive
state, choose R=R_j directly in the exact theta identity. Now

    d=alpha+t*(n+1/2)-R in[-1,1), z=d-1/2 in[-3/2,1/2).

The k=2 version of the H_k decomposition is valid here by analytic
continuation: J(2+z,t) and J(2-z,t) are analytic for |Re(z)|<5/2. Define
R_2(z,t)=J(2+z,t)+J(2-z,t), and use E=(-1)^R e(alpha*X+(t/2)*X^2).
The exact expression is

    F_n(alpha,t/2)
      = Lambda * [ sum_(h=0)^R g_h
          - (1/2)*sum_(l=0)^1 g_(R-l)*erfc(eta*(d+l))
          + (1/2)*sum_(l=0)^1 g_(R+l+1)*erfc(eta*(1-d+l)) ]
        + C0 - i*E*R_2(z,-t)/(2*pi).                      (5)

There are four Fresnel endpoint families. Their signs follow from

    E*exp(-pi*i*(d+l)^2/t)       =(-1)^l*g_(R-l),
    E*exp(-pi*i*(1-d+l)^2/t)     =(-1)^(l+1)*g_(R+l+1),

and the factor (-1)^l in H_k. The sign of the regular part changes because
the k=2 H_k decomposition has a positive J remainder inside h.

This really absorbs the delta correction. If R=r+1, then E_R=-E_r and
z_R=z_r-1. The exact h shift relation makes the change in the boundary
equal -Lambda*g_(r+1), canceling precisely the added dual-prefix term.
No delta position is discarded or approximated.

The new regular part still has a uniform short expansion:

    R_2(z,t)=sum_(j>=0)c_j^(2)(t)*(2z)^(2j),
    |c_j^(2)(t)|<=4/5^(2j+1),
    tail after K terms <=(5/4)*(9/25)^K for |z|<=3/2.     (6)

The same proof uses exp(-4x)/cosh(x)<=2exp(-5x). Rescaling the moment
variable to 2z/3 keeps its magnitude at most one. Coefficient approximation
has the same polynomial bit cost as above.

Thus the bulk in F296 can be interchanged and shortened using its single
linear-floor R_j. A separate indicator family is unnecessary if the four
completed endpoints in (5) are retained. The remaining moments still depend
on the fractional parts of two linear expressions through d_j. This is a
cleaner exact candidate family, not its recursive evaluator.

## What remains after this compression

F296 expresses the bulk as one shorter quadratic-floor moment. Equation (5)
absorbs its modular cut correction into four endpoint families; equation (6)
compresses the regular analytic remainder to a short moment list. The
uncomputed work is still the aggregate Fresnel endpoint family and the
polynomial moments with their actual floor and residue data.

In particular, z_l contains the fractional part of a linear function of a
floor-indexed prefix, and E_l retains its quadratic phase and parity. Calling
these moments polynomial weights does not make them ordinary unconstrained
Hiary sums. Nor does a shorter bulk sum prove that the number of boundary
states remains bounded over successive recursions. No recurrence for total
bit cost is established here.

The next useful question is closure of the *completed* prefix family (5)
under the bulk/cut interchange. Discarding its four erfc endpoints or
replacing the phase by its norm would change the count.

This entire prefix family is still within one fixed F294 frequency b0.
Across the original odd-b0 sum, the quadratic coefficient, normalization,
root weight Z, and child modulus p can change. A fast evaluator for each
completed frame would not itself aggregate those original frequencies.
The factoring route needs a bound for that combined family too, without
enumerating all b0 or their different child moduli.

## Evidence

`boundary_moments.py` checked 6,072 endpoint phase identities in exact
rational arithmetic. Twenty 35-digit quadrature comparisons, including
t=0 and t=1/4096, satisfy the uniform nine-term bound. At the limiting
t=0,z=1/2, the observed error 3.87154e-9 nearly reaches the proved upper
bound 3.87176e-9. The run took 2.69 seconds and 32,407,552 bytes peak RSS.

`completed_prefix.py` independently evaluates h through H1 plus the Laplace
integral, while F296 uses the rotated h contour. All 45 centered identities
agree with direct theta sums to at most 8.91e-37 at 42 decimal digits. The
printed-coefficient version differs by up to 1.58 on this sample. The run
took 4.09 seconds and 32,882,688 bytes peak RSS. These quadratures are finite
numerical comparisons, not interval certificates or replacements for proof.

The first runtime invocation found no mpmath in Homebrew Python and ended
before any mathematical calculation. Its failed log is retained. The same
unchanged program then ran with Sage's bundled Python and mpmath. Both
successful runs completed within their timeout guards. Sources, JSON output,
logs, and timeout statuses are in this packet. No shared record or source
paper was altered by the mathematical experiments.

`uncentered_prefix.py` checks all 16 prefixes in the faithful q=64 and q=256
frames, using their actual simple R_j. The q=256 delta positions j=2,6 are
absorbed by (5). It checks every prefix and the complete weighted moments
against direct sums at 42 decimal digits; its output retains the errors,
resource use, and positions. The centered author independently checked the
algebraic signs, analytic continuation domain, and exact delta cancellation.
That is a collaborative check, not a fresh statement-only reconstruction.
