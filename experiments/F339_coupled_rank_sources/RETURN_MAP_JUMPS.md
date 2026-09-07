# Coupled rank jumps and the deleted-interval count

**Family:** route:F31

Status: author-derived identity and scoped failure of a coupling. Unpromoted;
no independent reconstruction or numerical execution. No QP factoring claim.

## Question and closest prior

F336 `RANDOMIZED_WINDOWS.md` and F337 sample individual ranks using orbit gaps.
Their exact useful energies concern independent draws, and shared-endpoint
effects prevent an automatic birthday conclusion. Here two endpoints are
coupled by a fixed jump in a larger rotation. The question is whether choosing
that jump creates useful congruences unavailable in the individual marginals.
This is different from the adjacent-successor control: the jump can be any
public integer q between 1 and L-1.

Rust navigation inspected `route:F31` and searched `three-gap` and
`window menu`; neither query found a closer indexed statement. This note uses
the explicit successor table proved in F336, not a new three-gap theorem or
an external distribution result. F337 `INVERSE_GAP_TRANSFER.md` is a related
but different reduction: it transfers inverse-source boundary ranks to a
smaller modulus b. The present reduction concerns all retained orbit indices
and transfers a coupled displacement to a deleted-interval visit count.

## Full-rotation representation

Fix N>1, a unit a modulo N, and 1<=t<N. Set m=t+1. Let u and v be the
indices attaining the least positive orbit residue alpha and the largest
orbit residue N-beta among indices 1,...,t. Put

    L=u+v,   d=L-m,   A={0,...,m-1},   B={m,...,L-1}.

The F336 successor table gives max(u,v)<m<=L. Each successor changes the
index by u, -v, or u-v. If g=gcd(u,v), every change preserves the index
modulo g. The successor is one cycle containing both 0 and 1, so g=1.
Summing the gaps around that cycle also gives

    alpha*v + beta*u = N.

Consider the full rotation T(k)=k+u modulo L. Its first return to A is
exactly the F336 successor. Indeed, a direct step that lands in A is +u or
-v. A step that lands in B is followed by a second step with total change
u-v. There cannot be a second deleted landing: d<min(u,v). Thus removing
the B entries from the full L-cycle gives the sorted orbit-index order.

Let w=u^(-1) modulo L and put

    s(k)=w*k mod L,
    H(s)=#{0<=j<s: u*j mod L is in B}.

For k in A its sorted orbit rank is exactly

    r(k)=s(k)-H(s(k)).                                      (1)

The ranks start at r(0)=0. This representation does not require an inverse
modulo N, and remains valid even when gcd(u,N) is proper. Such a gcd is a
separate charged factor output if the public implementation screens it.

## An explicit public coupled source

Choose a public parameter q with 1<=q<L. Draw k uniformly from A and set

    k'=(k+q*u) mod L.

If k' is outside A, return failure for this attempt. Otherwise calculate
the two ranks and test gcd(r(k')-r(k),N). Endpoint rejection is retained as
failure; no hidden acceptance normalizer or repeated rejection is assumed.
The two retained endpoints are distinct because u is a unit modulo L.

Let h(k,q) count the deleted indices along the q-step arc of the full
rotation, including the starting position and excluding the endpoint:

    h(k,q)=#{0<=j<q: (k+j*u mod L) is in B}.

Since k and k' lie in A, the forward displacement in the retained cycle is

    D=q-h(k,q),    1<=D<m.                                 (2)

Consequently the ordinary integer rank difference satisfies

    r(k')-r(k)=q-h(k,q)-epsilon*m,                          (3)

where epsilon is 1 exactly when r(k')<r(k), and otherwise 0. This is an
identity for the joint source, not an iid assumption or an energy estimate.

All required counts are public floor sums. Write

    FS(q,L,u,b)=sum_{j=0}^{q-1} floor((u*j+b)/L).

Then, for the integer representative 0<=k<L,

    h(k,q)=FS(q,L,u,k+L-m)-FS(q,L,u,k).                     (4)

The floor difference is precisely the indicator that the residue is at
least m. Formula (1) uses the same expression with k=0 and q=s. Euclidean
floor sums give polynomial bit cost. Setup uses the charged F336 extremum
search, followed by one inverse modulo L. Uniform k uses fair-bit rejection.
This construction has no sorting step at runtime.

## Precise failure when only a short interval is deleted

For each fixed public q, all gcd arguments produced by every retained pair
belong to the public menu

    M(q)={q-h, q-h-m : 0<=h<=d}.                           (5)

This follows because each full-rotation position is visited at most once
on an arc shorter than L, so 0<=h(k,q)<=d. The menu contains at most
2(d+1) integers. Zero and arguments with gcd equal to N are simply failures.
Scanning it therefore finds a factor whenever *any* pair under this fixed-q
coupling finds a factor. It may also find a factor from a menu entry that
no pair attains. This dominance is pathwise and needs no probabilistic
claim about the source or hidden factors.

In particular:

* For d=0, every output is covered by the two direct tests gcd(q,N) and
  gcd(q-m,N). Arbitrarily long rotation jumps do not escape this control.
* For d bounded by a polynomial in the bitlength, the complete menu has
  polynomial bit cost and can be tested without rank queries or sampling k.
* For an adaptive list of q values, all successes of the coupling are still
  covered by the union of the corresponding menus. Failed endpoint samples
  create no additional gcd argument outside that union.

This does **not** prove that the menu has a good success probability. It
does show that this particular coupling with a short deleted interval
cannot owe a new cheap success mechanism to its rank geometry. Any claimed
advantage must be compared with the explicit nearby-integer menu, including
its different cost. The statement does not cover other uses of a transcript,
such as nonlinear combinations of several rank differences.

When d is numerically large, exhaustive menu evaluation can be expensive.
Equations (2)--(4) then give a concrete remaining question: can the visit
count h select useful entries of a long menu with sufficient public-source
mass? There is currently no success law or reason to prioritize a large run.
This note does not close that regime or arbitrary coupled sources.

## Exact endpoint law for arbitrary deletion size

For fixed q put c=q*u mod L. The number of accepted starting indices is

    K(q)=max(0,m-c)+max(0,m-(L-c)).

These are the nonwrapped and wrapped intersections of A and A-c. Thus
acceptance is K(q)/m; conditional on acceptance, k is uniform on that
intersection and k' is its deterministic translate. For any public law
pi(q), the unconditional factor probability is exactly

    (1/m) sum_q pi(q) sum_{k in A, (k+q*u mod L) in A}
        1_{1<gcd(r(k')-r(k),N)<N}.                         (6)

This formula retains dependence of the endpoints and failed attempts.

A concrete all-d choice is uniform q in {1,...,L-1}, independent of k.
For each fixed k, k' is uniform on the other L-1 full-cycle indices.
Acceptance is (m-1)/(L-1), and conditional on acceptance the ordered pair
(k,k') is uniform on all distinct elements of A. Since r is a bijection,
the retained ranks are exactly uniform distinct ranks. No rank computation
is needed to reproduce this law: draw I uniformly from 0,...,m-1, draw J
uniformly from the other m-1 ranks, and apply the same gcd. An optional
independent acceptance coin reproduces the original failed-attempt law too.
This exact collapse applies even when d is exponential in bitlength.

Each attempted rotation coupling charges sampling k and q, one modular
product, the endpoint test, and (only when accepted) two rank evaluations
and one gcd. Setup is charged even when all endpoints fail. For a randomized
parameter source, expectation of (6) and of this full cost is taken over
that source before forming the cost/success ratio. Conditioning away an
expensive or unsuccessful parameter is not valid accounting.

## A deliberately manufactured large-deletion source also collapses

There is a stronger concrete collapse for an engineered source with large d;
it holds for every q law, including nonuniform and adaptive jump choices.
For odd N>=9 set M=floor(sqrt(N)) and screen gcd(M,N). If it is proper,
return it. For the remaining branch put

    alpha=N mod M,   beta=floor(N/M)-alpha,
    u=M,   v=M+1,   m=M+2,   a=N-alpha-beta.

Here 1<=alpha<M, beta>=1, and alpha*v+beta*u=N. Screen gcd(a,N), returning
a proper factor if present. On the unit branch, these data are an actual
orbit instance with t=M+1. To see this without assuming the desired extrema,
take the first-return cycle of +M modulo 2M+1 on A. Assign its three step
types the positive gaps alpha, beta, and alpha+beta. Their sum is N and
their residues agree with a times their index increments, since
a*M=alpha mod N and a*(M+1)=-beta mod N. The accumulated gaps therefore
give the distinct sorted residues of the orbit, with the specified extrema.

In this source L=2M+1 and d=M-1, so deleting a short interval is not a
valid explanation. Nevertheless the sorted order is explicitly

    0, M, M-1, ..., 2, 1, M+1.

Its rank map is

    r(0)=0,   r(M+1)=M+1,   r(k)=M+1-k for 1<=k<=M.         (7)

For any fixed q let c=q*M mod L. If neither endpoint is 0 or M+1,
the rank difference is exactly k-k', hence either -c or L-c. Each of
the two exceptional indices can occur as a start or as an endpoint for
at most one starting index under this fixed translation. There are at most
four exceptional pairs. They can be constructed directly as

    k=e or k=(e-c mod L),   e in {0,M+1},

retaining only k,k' in A. Formula (7) evaluates their differences with
constant work. Thus **at most six direct public gcds cover every success
of every retained pair for each chosen q**, despite d being of square-root
numerical size. This is not just the q near L/2 case. No floor sum, orbit
sample, or sorted array is required for this control.

The construction was chosen to force coprime large return indices and
positive gap data. It succeeds at that geometric task but fails to create
a complicated local rank observable: adjacent u,v make the retained rank
map affine except at two points. The failure is restricted to this stated
source and output rule. General large-deletion data need not have (7).

## Bounded check design, not executed

A finite identity check is sufficient before using this reduction as a
dependency. It is not a performance experiment. After resource preflight,
use one thread, a 10-second timeout, and a 64 MiB budget. Enumerate odd
N<=31, every unit a, and every 1<=t<N. Build the full sorted array only as
an offline oracle. Check the first-return cycle, gcd(u,v)=1, the positive
gap equation, and (1) for every k in A. Check (2)--(5) for every
1<=q<L and every k whose endpoint stays in A, using direct deleted counts.
Preserve a named source, output totals, first anomaly, log, and hashes.

No hidden factors are needed for these identity checks. If later measuring
factoring performance, retain failed endpoints and all setup work, compare
against the menu whenever feasible, and keep d=0 as a mandatory exact
control. A success proportion on small N would remain finite evidence.

Add a separate source-specific check for odd 9<=N<=511. Preserve both
generation-gcd exits. For every unit source branch check the manufactured
extrema, sorted order (7), and every accepted k,q against the six-entry
control. This directly distinguishes a real large-d collapse from an
unsupported extrapolation of the small-d menu. The root can assign this
finite implementation to Sol; the present author has not executed it.
