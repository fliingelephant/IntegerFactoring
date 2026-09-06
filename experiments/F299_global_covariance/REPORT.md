# F299: all-frequency covariance and a common-conductor lattice family

**Subsequent identification:** `AFFINE_EQUIVALENCE.md` proves that each
halfbox class below is one ordinary affine half-window. On faithful inputs,
the full two-stage family is exactly P235's affine cover. Barvinok is
unnecessary, and no new asymptotic factoring mechanism was obtained.

**Family:** route:F31. **Status:** author-derived identities and exact finite
checks; independent reconstruction pending. The outer frequencies are grouped
simultaneously within one F294 chart. The remaining chart union and the actual
factor-isolating window interface are not solved.

The transformation has a bounded parameter description and a common Fourier
conductor. A literal residue split then gives polynomial-bit linear lattice
counts per class, with about sqrt(m) classes. No faster aggregation of those
classes is established.

## Scope and prior navigation

F299 was checked unused through the Rust reader and filesystem. The C251 head,
F294 formal descent and recombination, F295 auxiliary coordinates, and cached
theta sources were inspected. The material difference from F296 is that the
present operation acts on **all original odd b at once**, before any
b-dependent theta normalization or completed-prefix child modulus.

The root filter is the same elementary mechanism used for F294's earlier
high-lift contraction, now applied to its remaining outer sum. No novelty
claim is made for that algebra.

All-frequency here means within one near-affine chart. In the intended
original modulus M=m^3 setting, the u0-mod-m chart family still remains.
The checked F294 outputs are shifted halfboxes. The generalized reduced
quadratic-window interface below retains arbitrary integer endpoints, but
it is not asserted to cover the original factor-isolating rectangles or
their complete chart union without the root's separate interface reduction.

## Preserve the exact complete frame

Use F294 notation q=m^2, m a power of two at least8. Let u,gamma be odd and
0<=D<q. Put

    d=gamma/u mod q, beta=gamma/u^2 mod m,
    Psi(i)=beta*i^2+floor((D-d*i)/m), 0<=i<m,
    Theta_b=sum_i e_m(b*Psi(i)),
    D_b=(1-e_m(-d*b))*(1-e_m(-b)).

The retained chart count is

    C=q/4+(4/m)*sum_{b odd mod m} Theta_b/D_b.             (1)

This is the full exact F294 expression after its justified z-Gauss
contraction. Both window denominators and all carry shifts remain. It is
not an absolute-square replacement for a Gauss/character moment.

The dependence on b is exactly A=b*beta, B=-b*floor(d/m), Z=e_m(-b), with
the corresponding constant phase from D. A completed-prefix representation
is equal to this whole frame, but its individual analytic terms need not
have the covariance below. The identity acts before that decomposition;
it therefore retains their combined phases without separately asserting
an aggregation algorithm for truncated analytic approximations.

## Exact global root filter

Let r=2^s divide m and L=m/r>=2. For every odd b0 modulo L,

    sum_{t=0}^{r-1} Theta_(b0+L*t)/D_(b0+L*t)
      =r/((1-e_L(-d*b0))*(1-e_L(-b0)))
          *sum_i sum_{j=0}^{r-1}
                    e_L(b0*floor((Psi(i)-d*j)/r)).       (2)

Proof: put x=e_m(-d*b0), y=e_m(-b0), xi=e_r(1). Expand each inverse
denominator as its length-r geometric polynomial divided by1-x^r or1-y^r.
The t sum imposes Psi(i)-d*j-k=0 mod r. The unique k in[0,r) is
(Psi(i)-d*j) mod r. Combining the remaining phase gives exactly(2).
All denominators are nonzero because b0,d are odd and L is even.

For r=2 the two children are simply floor(Psi/2) and floor((Psi-d)/2).
Successive applications compose without a list of separately named branches:

    floor((floor((Psi-d*j)/r)-d*k)/s)
         =floor((Psi-d*(j+r*k))/(r*s)).                  (3)

Thus one finite index j<r records the entire descent. Every b group has
the same conductor L; no b-dependent theta modulus has appeared.

The identity holds for arbitrary integer Psi values and arbitrary finite
index weights independent of b. A finite Fourier-polynomial prefactor in b
is retained by shifting Psi in each of its terms. This observation alone
does not prove that every original arbitrary window has a bounded such
representation on the odd-frequency stratum.

## Flatten the carry and account for the parameters

Using the unwrapped Psi,

    Phi_(r,j)(i)=floor((Psi(i)-d*j)/r)
      =floor((m*beta*i^2+D-d*i-m*d*j)/(m*r)).             (4)

Replacing Psi by its canonical value modulo m changes Phi by a multiple
of L, so the exponent is unchanged. The Fourier conductor is L while
the carry denominator is m*r. Their product remains m^2.

This constant product is descriptive, not an obstruction. A literal
evaluation has m*r index pairs and L/2 outer frequencies, hence m^2/2
elementary phase evaluations before further aggregation. The parameter
description stays O(log m) bits, but that alone does not evaluate its
growing finite index range.

There is a positive count version. Write

    W_(L,-d)(h)=#{0<=y<L/2:(h-d*y) mod L<L/2}.

The exact Fourier formula for W and(2) give

    C=sum_{i=0}^{m-1} sum_{j=0}^{r-1} W_(L,-d)(Phi_(r,j)(i)). (5)

The baseline cancels exactly: there are m*r arguments and each has baseline
L/4. At L=2 this is the original quadratic-window sum written as a signed
floor-parity count. It has not become a phase-free constant.

## Simultaneous residue splitting makes each class linear

Write m=2^k and choose

    r=2^floor(k/2), L=m/r, kappa=beta*r mod L.

Then L divides2r, so kappa is0 or L/2 and kappa*x^2=kappa*x mod L. This
slightly improves the sufficient condition L|r, where the quadratic term
vanishes outright. Put i=i0+r*x, 0<=i0<r,0<=x<L, and define

    E_i0=floor((m*beta*i0^2-d*i0+D)/r),
    A_i0=m*(2*beta*i0+kappa)-d.

Expanding(4) gives, modulo L,

    Phi_(r,j)(i0+r*x)
      =(2*beta*i0+kappa)*x
           +floor((E_i0-d*x-L*d*j)/m).                 (6)

In(5), combine j+r*y=v. This is a bijection from j<r,y<L/2 to v<m/2.
The contribution of i0 is exactly the number of integer triples(x,v,h)
satisfying

    0<=x<L, 0<=v<m/2,
    0<=A_i0*x+E_i0-L*d*v-m*L*h<m*L/2.                  (7)

These are linear inequalities in three integer variables. The polytope is
bounded: the boxes bound x,v and the strip bounds h. Strict integer endpoints
are replaced by upper endpoint minus1. All coefficient descriptions have
O(log m) bits for the stated chart input ranges.

The initial analysis invoked the fixed-dimensional rational-polytope counting
theorem for(7). The stronger coordinate collapse in `AFFINE_EQUIVALENCE.md`
makes that invocation unnecessary: t=x+L*v reduces(7) to one ordinary affine
half-window of modulus m*L. This retains the scoped r*poly(log m) count bound
per chart, but the faithful chart union is precisely P235's existing affine
cover. No Barvinok solver was implemented or benchmarked.

## Arbitrary endpoints for the reduced interface

The same linearization handles

    #{i in I,v in V:(Psi(i)-d*v) mod m in[Y0,Y1)},

where I,V are integer intervals in[0,m) and0<=Y0<=Y1<=m. For each i0,
restrict x by i0+r*x in I and v by V, and replace the strip in(7) by

    L*Y0<=A_i0*x+E_i0-L*d*v-m*L*h<L*Y1.                (8)

To verify the endpoints, the original numerator equals r times the displayed
affine expression plus a fixed residue in[0,r). Since m/r=L is integral,
that residue cannot alter either integer-aligned endpoint in(8). The pilot
checks22 non-half window instances. No arbitrary endpoint has been rounded
or replaced by a halfbox in this reduced interface.

## What remains when the residue classes are aggregated

An exact root filter can express the i0 classes, but its zero Fourier mode
is precisely their desired sum. The nonzero modes do not uniformly vanish:
the faithful q64 count18 has two equal class counts9,9, whereas the faithful
q256 count67 has class counts16,19,16,16 and all four class Fourier modes
are nonzero. This separates only the constant-class/automatic-mode-cancellation
shortcut. It is not a lower bound against a different aggregation.

Short generating functions apply to each fixed linear polytope(7). Making
i0 another variable changes A_i0*x into a bilinear term and E_i0 into a
quadratic/floor term. Consequently the displayed common family is not
itself a fixed rational polytope to which the same linear theorem can simply
be reapplied. No joint short generating function for that family is supplied.
Other coordinate changes or root filters remain open.

## Exact pilot

`global_covariance.py` checked11 algebraic chart inputs: the faithful q64
and q256 examples, their q256 D=0 control, and eight seeded random cases
with m=8,16,32,64(seed2992608). All equalities are exact in cyclotomic fields
or integers. Totals are129 complete frequency-coset checks,10896 floor
flattenings,5728 affine-class point checks, and22 arbitrary-window checks.

The faithful counts remain18 and67, with63 for the D=0 q256 control. All
successive conductor descents preserve those totals. The full original
b-normalization has m/8 distinct p values in these dyadic cases; that
descriptive fact is not used as an obstruction. Equation(2) avoids choosing
any of them.

The pilot had a60-second alarm and estimated peak below512MiB. The final
run took0.061seconds after Sage initialization and used248.3MiB. Preflight
reported load1.98/2.03/2.00,73% available memory and no swap. Approved process
inspection showed one Apple process using a core. Source, JSON and log are
retained. No shared metadata or commit was made.

The bounded result is an exact all-frequency common-conductor identity,
closed as a succinct indexed floor family, plus an affine-window evaluator
for each of about sqrt(m) residue classes. On faithful inputs these classes
collectively reproduce P235; they are not a new asymptotic cover.
Simultaneous class aggregation,
the original u0 chart sum, and the all-input factor-isolating interface
remain separate obligations. No further round is started by this report.
