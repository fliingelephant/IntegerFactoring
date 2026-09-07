# Original-graph resolvent lift and a certified moment interface

**Family:** route:F31

**Scope:** the original modular inverse graph, ordinary rational Cauchy poles,
and the dyadic carry and joint moments.

## Question and closest records

Can pole-distance Taylor compression turn the exact dyadic lift of the
original-graph resolvent into polynomially many computable states, without
discarding its signed carry?

The candidate was stated before checking records. Rust navigation resolved
`experiment:F292_localized_character`, `experiment:F293_carry_convolution`,
and `experiment:F301_factor_rectangles`. F292/TWISTED_RECURRENCE.md already
retains a growing carry-character family. F293/RESULT.md already identifies
the phase-sensitive half-count and its inverse-Bernoulli mixed moment.
F301/RATIONAL_FILTERS.md supplies the ordinary-pole interface and its absolute
precision requirement. This packet does not claim that carries or the mixed
moment are new. It supplies the ordinary-resolvent lift, an explicit certified
Taylor interface, and the exact lowest-order retained operation that this
particular compression still needs.

## Exact lift

Let M=2L, L even, N odd, and let a run through odd residues in [1,L).
Set b=N/a mod L and c=(N-ab)/L mod 2. The two graph lifts are

    (a+Lh, b+L(h xor c)), h in {0,1}.

Indeed, the product congruence modulo 2L reduces to h+k=c because a,b
are odd and L squared is divisible by 2L. Write sigma=(-1)^c and

    S_z(a)=1/(a-z)+1/(a+L-z),
    D_z(a)=1/(a-z)-1/(a+L-z).

Then exactly, at every nonpole rational or complex z,w,

    Z_(N,2L)(z,w)
      = (1/2) sum_a [S_z(a) S_w(b) + sigma D_z(a) D_w(b)].       (1)

Expansion gives four ordinary lower-modulus resolvents and four signed
lower-modulus resolvents, with pole coordinates chosen from z,z-L and
w,w-L. Their coefficients are ±1/2. A recurrence solely in ordinary Z
does not result. The new signed object keeps N modulo 2L, even though its
point coordinates use modulus L. Iterating the character is the same
issue treated explicitly by F292; the pole representation does not remove it.

## Certified far-pole interface

Center each lower coordinate at c0=L/2, radius R=L/2. For either pole z
or z-L, suppose its imaginary height has absolute value at least y_z>R.
Let rho_z=R/y_z. The K-term expansion of 1/(a-z) has uniform error

    E_z = rho_z^K / [y_z (1-rho_z)]

and polynomial magnitude at most 1/[y_z(1-rho_z)]. The same estimates
hold for the shifted pole. Hence replacing every individual reciprocal in
the two-point lift by this expansion gives total error at most

    B_K = L [E_z/y_w + E_w/(y_z(1-rho_z))].                   (2)

This follows from the product difference and exactly L lifted points;
no cancellation or random input assumption is used. Complex modulus is
meant throughout. The coefficient arrays are

    S_z,i = -[(z-c0)^(-i-1) + (z-L-c0)^(-i-1)],
    D_z,i = -[(z-c0)^(-i-1) - (z-L-c0)^(-i-1)].

Equation (1) is therefore approximated by

    (1/2) sum_(i,j<K) [S_z,i S_w,j mu_ij + D_z,i D_w,j tau_ij], (3)

where mu_ij sums (a-c0)^i(b-c0)^j and tau_ij sums the same monomial
times sigma. For y_z,y_w at least M, rho<=1/4, K=O(log M) gives any
fixed M^(-c) target. Only 2K squared scalar moment states are needed.
Their integer bit heights are O(K log M); rational coefficient and
arithmetic precision likewise remain polynomial in log M for rational
poles of polynomial bit height. This is an evaluation bound GIVEN the
moments, not a construction bound for them.

The public F301 poles also include small heights of order 1/log M.
The global expansion (2) then does not certify contraction. One can
partition each coordinate into O(log M) intervals whose lengths are a
fixed fraction of their distance from a pole, including the half-integer
near-pole gap. This gives O(log squared M) joint boxes with local Taylor
convergence. However, each local zeroth joint moment is already an original
inverse-graph rectangle count. Local signed moments retain the carry too.
Thus geometric partitioning alone supplies no way to populate its moment
bank; counting its boxes as computed states would be incorrect.

## The first signed moment is already a retained cut

Let C_M(N) count original graph points with both coordinates in [1,L).
Exactly the c=0 lower pairs supply these points. Consequently

    tau_00 = 2 C_M(N) - L/2.                                 (4)

Changing N to N+L leaves the entire lower graph unchanged and negates
sigma. Any method using only unsigned lower moments therefore gives the
same approximation for these two inputs, while (1) retains their difference.
For M=32 the original composite inputs N=481 and N=497 have C=6 and C=2,
and tau_00=4 and -4. M is the largest power of two at most N/8 for both.

For another exact view, define uncentered mu11(M)=sum_u u*v_N(u). The
two lifted products sum to 2ab+L(a+b)+L squared for c=0, and to
2ab+L(a+b) for c=1. The lower marginal sum of a+b is L squared/2.
Therefore

    mu11(M) = 2 mu11(L) + L^3/2 + L^2 C_M(N).                (5)

Even the unsigned mixed moment of degree two contains the same selected
half-count once its lower-modulus moment is removed. This agrees with
F293's inverse-Bernoulli relation. It is a precise necessary suboperation
for the proposed moment-bank recursion, not a lower bound against other
resolvent algorithms.

For general uncentered moments the exact recurrence is

    mu_ij(2L) = (1/2) sum_a [P_i(a)P_j(b)+sigma Q_i(a)Q_j(b)],
    P_i(a)=a^i+(a+L)^i, Q_i(a)=a^i-(a+L)^i.

The carry term lowers each positive degree by one, which is useful
triangular structure. It does not eliminate its base tau_00. A constructive
next question is whether these lower-degree signed banks can be computed
together with ordinary banks without growing the carry-character family.
The localized-character worker studies that separate possibility.

## Exact pilot and costs

`pilot.py` uses pairs of rational numbers for complex arithmetic. It
checks (1), (5), and the squared rational error bound in (2). There is no
floating-point acceptance test. The displayed floats are diagnostics only.
All four fixed composite inputs satisfy the original M-selection rule:
(M,N)=(32,481),(32,497),(64,1001),(128,1995).

Twelve pole cases passed the exact lift. Eight far-pole Taylor cases
passed the error target M^-6. At height M the K values were 13,13,16,18,
and the scalar moment-state counts were 338,338,512,648. Exact moment
construction in this pilot explicitly visits L/2 graph points and performs
2(L/2)K squared scalar updates. It is exponential in input bit length.

The height M squared controls are deliberately smoother diagnostics, outside
the required O(M log M) maximum-height family for large M. They require K=3
here and sometimes allow the carry to be discarded at this particular
precision. No inference is made for the mandatory near poles from those cases.

Four further cases use rational midpoints of the certified first and last
positive-pole intervals in F301/rational_poles.json, divided by two for
ordinary-coordinate window poles. These are exact rational midpoint probes,
not assertions that the true algebraic roots equal those midpoints. Their
real parts are half-integers from public boundaries near floor(sqrt N).
For both N=481 and N=497, dropping the carry exceeds M^-6 at the near
probe; the far probe is also retained in the output. The near probe fails
the global rho<1 condition, as expected.

The pilot ran in 0.066 seconds with 17,858,560 peak RSS bytes. Source,
full output, run log, and resource estimate are retained. No factoring
oracle, state-count contraction, or quasipolynomial algorithm is established.
