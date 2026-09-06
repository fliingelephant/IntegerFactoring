# F292: binary carry frontiers and geometry-first contraction

The constructive continuation is in `TWISTED_RECURRENCE.md`: an exact
fixed-conductor character lift with linear additive phases, followed by a
sparse moment recurrence and seeded cap tests. The present file records the
initial representation attempt only.

The next attempt is in `RECIPROCITY.md`: identification of the primitive
Cochrane difference, an exact Gauss-square dual, and an inverse-reciprocal
map with explicit divisor boundary terms. The modulus decreases, but the
number of distinct smaller-modulus calls has not been contracted.

`KERNEL_PRIMITIVE.md` supplies a positive supporting primitive: an individual
finite quadratic-Gauss/Cauchy kernel and its exact-root finite parts reduce
to Hiary's polynomial-bit weighted theta algorithm. The remaining outer
sum is explicitly outside that result.

**Family:** route:F31. **Status:** author-derived scoped rank bound and exact
finite certificates. Independent reconstruction is pending. No support
algorithm or novelty claim is established.

## Mechanism proposed before literature

The attempted representation processes the bits of both coordinates together.
It retains the exact modular multiplication condition and compresses the
remaining carry functions by linear dependence. Coordinate interval tests can
then be contracted against this representation. This is materially different
from F290's complete objective histogram: it preserves both coordinate strings
and does not merge their unwrapped placements at the outset.

The relevant P235/C251 heads were loaded through the Rust reader after reading
README.md, research/STATE.md, and PROMPT.md. F290/REPORT.md and NORMALS.md are the
closest prior work used here. No related paper informed the initial mechanism.

## Exact frontier at the balanced cut

Let L=2^t with t>=3, M=L^2, and N odd. Write

    x=u+LX, y=v+LY, 0<=u,v,X,Y<L.

For every odd u there is exactly one odd v in [0,L) with uv=N mod L. Put

    c=(N-uv)/L mod L,
    s=v/u mod L, d=c/u mod L.

The residual modular condition is exactly

    f_u(X,Y) = 1_{Y+sX=d mod L}.

Thus the paired low-bit/high-bit coefficient matrix has L/2 rows and L^2
columns. Its row functions are affine-line indicators over Z/LZ. This is also
a block lift of the one-bit carry identity: the high coordinates must solve
uY+vX=c mod L. No approximation or unknown factor is used.

## A precise obstruction to the reusable representation

**Candidate proposition.** Over C, the matrix with rows f_u has rank at least
L/8=sqrt(M)/8, for every odd N.

Proof. Fourier transform each row in X,Y, using frequencies (h,k). Substituting
Y=d-sX gives

    fhat_u(h,k)=L exp(-2 pi i k d/L) 1_{h=ks mod L}.

Restrict to odd k. Rows with different slopes s have disjoint Fourier support,
and each has nonzero support. The slopes are N/u^2 mod L. The square map on
the odd units modulo 2^t has kernel of size four, hence exactly L/8 images.
Choose one row for each slope. Their restricted Fourier transforms have
disjoint nonempty supports, so these rows are linearly independent. This
proves the claimed lower bound.

In particular any exact sum

    f_u(X,Y)=sum_{j=1}^R A_j(u) B_j(X,Y)

valid for all remaining high-coordinate pairs needs R>=sqrt(M)/8. The same
bound applies to the bond dimension of an exact linear tensor representation
whose cut separates the paired low bits from the paired high bits. It does
not constrain other bit orders, nonlinear representations, query-dependent
contractions, or the permitted short-cap family alone. It is not a lower bound
on factoring or on the required support oracle.

`frontier_rank.py` checks 30 public cases for t=3,...,8. The Gram entry for
lines (s,d),(s',d') is g=gcd(s-s',L) when g divides d-d', and zero otherwise.
The program computes the Gram rank modulo 1000003. These ranks certify
characteristic-zero lower bounds. In all sampled cases they equal the number
of distinct line rows, often the full L/2. At L=256 the five measured ranks
are 128,128,128,126,128; the proved lower bound is32. These finite observations
do not prove a stronger universal formula.

## Geometry first avoids that bound, but does not supply the contraction

For a balanced short cap, x and y are each O(sqrt(M)). At the same cut, only
O(1) high-coordinate blocks can occur. Its geometry-masked matrix therefore
has O(1) columns and O(1) rank. The preceding lower bound **does not apply**
to it. Low rank of the final masked answer is not the missing operation:
one must construct or contract the relevant low-coordinate rows without
enumerating all L/2 choices of u.

The exact remaining expression for a block (X,Y) is

    sum_{u odd<L} W(u+LX,v(u)+LY)
        1_{uY+v(u)X=c(u) mod L},

where v(u)=N/u mod L and c(u)=(N-u*v(u))/L mod L. Retaining this indicator
preserves the representative geometry. Completing it would again lose the
needed restriction. The small number of high blocks gives no procedure for
this sum on its own. Claiming that it does would hide precisely the original
localized-carry problem.

`cap_frontier.py` checks the retained F290 separator N=12827 versus12851 at
M=1024, L=32. For the (1,1) cap with T=228, the first input has exactly two
nonzero low rows, u=5,31, both in high block(X,Y)=(3,3); the second has none.
Their masked ranks are therefore1 and0. The first input gives(101,127) and
(127,101). The public odd menu normal(a,b)=(67,65), with the public threshold
floor(1.01*sqrt(4abN)), gives the same occupied rows for12827 and none for12851.
Both thresholds satisfy T^2<4ab(N+M), so every retained product is exactly N.
No equality of the odd-normal histograms is asserted. This test enumerated
all16 low rows; it does not provide a faster construction of them.

## Result and next discriminating direction

The universal paired-bit linear compression attempt fails in its stated
representation. Geometry-first compression remains possible and even has
constant formal rank in a balanced cap, but its basis/support discovery has
not been made constructive. A next transform must act on the displayed
block contraction directly, or use a different bit order; increasing generic
frontier precision cannot remove the rank bound.

Resource evidence: load2.04/2.13/2.08, memory_pressure reported72% free and no
swap. The initial sandbox process inspection was denied; the same read-only
ps call succeeded with approved escalation. One Apple process used one core;
other leading processes used below5% each. Pilots had explicit30-second
timeouts and estimated peak memory below64MiB. Recorded runtimes were0.039s
and0.0005s. Source, exact JSON output, and logs are retained beside this report.
Shared records, catalogs, skills, and Git were not modified.
