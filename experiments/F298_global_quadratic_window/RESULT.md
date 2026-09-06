# F298: a closed global parity recurrence, with its branching retained

**Family:** route:F31

Status: exact author-derived recurrence and finite verification. The nonlinear
family closes with one additional even linear parameter, but no
quasipolynomial bound on total states has been established.

## The global object and its scope

Let m=2^r, r>=3, and let the ray matrix have entries p,q,r0,s with
epsilon=p*s-q*r0 in {+1,-1}. Put eta1=q mod 2, eta2=s mod 2. Let u,d be
odd. Retain an even parameter v and arbitrary wrapped constants c1,c2:

    L1(x,t)=epsilon*(-r0*gamma*x^2+(u*s-r0*v)*x+d*r0*t)+c1,
    L2(x,t)=epsilon*( p*gamma*x^2+(p*v-u*q)*x-d*p*t)+c2.

The F295 family is v=0. Allowing even v is necessary for the descent.
Use the weights

    J0^m(z)=(m/2-1)/2-(z mod m/2),
    J1^m(z)=m/4 if z mod m<m/2, and -m/4 otherwise.

The global moment is

    M_m=(1/2)*sum_(x mod m) sum_(0<=t<m/2) J_eta1^m(L1)*J_eta2^m(L2).

Both variables are summed; this is not a fixed-frequency primitive. It
remains one global moment associated with one F294 chart/cone expression.
It does not aggregate the original u0 chart classes or replace a
factor-isolating short rectangle. Arbitrary c1,c2 translations are kept;
the half-window lengths are not generalized silently.

## The two parity symmetries are exact

Write H=m/2. The quadratic change under x to x+H is zero modulo m. The
remaining shifts of the two arguments are H*(s,-q), up to odd factors.
J0 is H-periodic and J1 is H-antiperiodic, so the product changes by
`(-1)^(q*s+s*q)=1`.

The shift t to t+H instead changes the arguments by H*(r0,-p), up to odd
factors. The product changes by `(-1)^(q*r0+s*p)=-1`, because the ray
determinant is odd. Hence

    M_m=sum_(0<=x,t<H) J_eta1^m(L1)*J_eta2^m(L2).

These properties continue to hold when gamma is even and v is even. The
smallest child modulus is handled directly when needed.

## Four children remain in the same nonlinear family

Set n=m/2 and split x=2X+e,t=2T+f, with e,f in {0,1}. Let

    C_i=L_i(e,f), kappa_i=C_i mod 2.

Then `L_i(2X+e,2T+f)=2*L_i'(X,T)+kappa_i`, where the child has exactly the
same ray matrix, odd u,d, and parameters

    gamma'=2gamma mod n,
    v'=v+2gamma*e mod n,
    c_i'=floor(C_i/2) mod n.

The weighted scaling identities are

    J1^m(2z+kappa)=2*J1^n(z),
    J0^m(2z+kappa)=2*J0^n(z)+(1/2-kappa).

At least one eta is one, because the ray matrix is unimodular. Therefore
there is no product of two constant correction terms. The exact recurrence
is

    M_m=4*sum_(e,f) M_n(child_(e,f))+single-window corrections.

If eta2=0, its correction for (e,f) is

    (1-2*kappa2)*sum_(X,T<n/2) J1^n(L1'(X,T)).

There is the symmetric formula if eta1=0. If both eta values are one,
there is no correction. The constants and even v are part of each child;
discarding them would not be the same recurrence.

## The boundary corrections are polynomial-cost

Every single-window child has the form

    S_n(A,B,C,D)=sum_(X,T<n/2) J1^n(A*X^2+B*X+C*T+D),

with A,B even and C odd. Thus the X summand is invariant under X to X+n/2,
and one may use half of the complete X histogram.

The complete dyadic quadratic histogram is a union of residue progressions.
Every progression with period at most n/2 pairs its values y,y+n/2 and
cancels against J1, for each retained T. Only the top atom strata remain.
After removing the common power of two from A,B:

* an even quadratic coefficient and odd linear coefficient give a uniform
  progression, whose contribution vanishes;
* odd quadratic and odd linear coefficients likewise give a uniform parity
  progression, except for the two-element degenerate quotient;
* odd quadratic and even linear coefficients allow square completion. An
  even quotient bit length leaves two atoms; an odd quotient bit length
  leaves one after the opposite top pair cancels;
* the constant polynomial leaves one atom.

If these surviving atoms have values y_j and multiplicities mu_j, then

    S_n=(n/8)*sum_j mu_j*(2*W_(C,n)(y_j+D)-n/2),

where W is the ordinary affine half-window count. There are at most two
atoms, and each W is computed by Euclidean floor-sum reciprocity. This
retains the T half-window and costs polynomially many bit operations in
log n. The source implements these cases explicitly; no complete-histogram
substitution is made for the main two-window moment.

## Exact signed merging and its observed cost

The recurrence is signed. Canonicalize each constant into [0,n/2) using

    J_eta^n(z+n/2)=(-1)^eta J_eta^n(z).

The induced sign is stored in the state's integer weight. Identical full
states are then merged, and exactly zero weights are discarded. This is
valid cancellation of identical global objects, not a heuristic ranking.

For an initially odd gamma, gamma becomes zero modulo the child modulus
after ceil(r/2) steps. Before merging there are up to 4^ceil(r/2) paths.
This gives only a numerical-scale upper bound for the nonlinear stage.
The following complete signed-state expansions stop when the remaining
states are linear; large linear base values were not assumed to be free or
silently computed by a new oracle.

| Initial modulus bits r | Random terminal states | Fixed-control terminal states |
|---:|---:|---:|
| 6 | 40 | 16 |
| 8 | 100 | 90 |
| 10 | 706 | 453 |
| 12 | 2304 | 1514 |
| 14 | 6368 | 6818 |
| 16 | 28692 | 17828 |

For the r=16 random case, the live counts by level were
`4,16,64,256,1024,4096,14438,28692`. Cancellation is real near the end, but
this pilot provides no polynomial bound on the total family. The fixed
control uses the same public coefficient tuple across sizes; it is not
claimed to be a faithful inverse chart for a fixed N at every size.

The state descriptions do close: the matrix,u,d remain fixed, gamma and v
have O(r)-bit representatives, and c1,c2 remain wrapped constants. Main
weights had at most 20 bits in this pilot. Generally their magnitude is at
most 16^k after k levels, so their bit length is O(r) at the stopping depth.
The obstacle found here is state count, not an exponential operand-precision
requirement. A constant branching factor with a one-bit modulus decrease
is not the desired polynomial branching with a bit-length halving.

## Verification and remaining scope

`parity_descent.py`, seed 202609070535, passed 192 exact checks of the two
pointwise parity symmetries, 24 complete one-step global recurrences, and
96 independent single-window correction checks. Four small cases also
validated the entire signed recursion through its linear base against
direct double sums. Their direct/recursive values were 2176,5376,-97280,
and47104.

The state-growth run retained every initial parameter, per-level count,
exact correction and weight-size statistic in `output.json`. It took
0.51 seconds in one process under a 50-second alarm, estimated memory below
256 MB. The final preflight showed 71% available memory and load 2.23.
Source, output and log are preserved. No shared record or earlier packet
was changed.

The constructive result is a genuinely closed parity recurrence on the
global rank-one quadratic moment, with cheap exact boundary terms and
arbitrary translated constants. It does not yet yield polynomially many
total states, arbitrary short-window closure, or aggregation of inverse
chart classes. Further work would need an identity on the **whole child
bank**, beyond canonical constant/sign merging, before this descent can
supply the required quasipolynomial factoring interface.
