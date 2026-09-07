# The N-linked jump has a short direct menu

**Family:** route:F31

Status: author derivation, unpromoted. The identities below have not yet had
independent reconstruction or a finite check. No public-source success law
or expected-QP factoring claim is established.

## Scope and prior

Use the definitions and first-return representation in RETURN_MAP_JUMPS.md.
The root's COUPLING_SEARCH.md tests the specific public jump

    b=beta-alpha,   q=b mod L=N*u^(-1) mod L,
    L=u+v,   m=t+1,   d=L-m.

This note concerns that fifth rule on general gap data. It does not assume
adjacent u,v, uniform q, a small deleted interval, or a half-orbit window.
The source remains public. The nearest previous menu in RETURN_MAP_JUMPS.md
had 2(d+1) entries. Reversing an accepted pair gives the elementary
improvement based on q*=min(q,L-q). Here the arithmetic linkage to N gives
a further menu of at most 2(floor(N/L)+1) entries. Direct-menu successes
remain legitimate factors; dominance does not establish a poor source law.

The input identities used are

    alpha*v+beta*u=N,   gcd(u,v)=1,
    max(u,v)<m<=L,   alpha,beta>=1.

In particular L<=N. Treat q=0 as failure under the frozen rule.

## An exact physical-residue identity

Write

    Q=floor(N/L),   c=N mod L.

For an accepted starting index k put k'=(k+c) mod L and

    j=floor((k+N)/L)=Q+1_{k+c>=L}.

Let z(k)=a*k mod N be the original orbit residue. Since
au=alpha mod N and av=-beta mod N, one has aL=-b mod N. Therefore

    k'-k=N-j*L,
    z(k')-z(k)=j*b mod N.                                 (1)

These are coupled identities; no independence of ranks is used. If e_j is
the centered representative of j*b modulo odd N, the circular rank distance
in its signed direction is bounded above by

    floor(|e_j|/min(alpha,beta)).

Indeed every traversed orbit gap is at least min(alpha,beta). A zero e_j
cannot occur for an accepted distinct pair. This is one diagnostic
consequence, but the following full-rotation argument gives a simpler
uniform bound without the physical factor j.

## Deleted visits consume both kinds of rotation steps

For any accepted full-rotation arc of length s with 1<=s<L, let H be its
number of visits to B={m,...,L-1}. The endpoints lie in A. A visit x in B
has predecessor x-u in A and successor x-v in A. To verify this, use
m>u,v and m<=u+v. Its incoming step is a nonwrapped +u step, and its
outgoing step is a wrapped -v step. Different deleted visits use different
steps of each kind. Thus, if W is the total number of wrapped steps,

    H<=min(W,s-W).                                        (2)

For an arc starting at k, the wrapped-step count is exactly

    W=floor((k+s*u)/L).

As 0<=k<L, W is either floor(s*u/L) or that integer plus one.
The nonwrapped count s-W has the corresponding bound with v. Hence

    H<=floor(s*min(u,v)/L)+1.                             (3)

This statement is general rotation geometry. The next bound is specific
to the N-linked choice.

## Arithmetic linkage bounds H by floor(N/L)

Reverse an accepted pair when q>L/2, and put s=q*=min(q,L-q). The reversed
pair follows +u for L-q steps, so the same first-return reasoning applies.
The signed gcd of the ordinary rank difference is unchanged by reversal.

The positive gap equation gives

    |b|*min(u,v)<=N-L.                                    (4)

For example, if b>=0 then N=alpha*L+b*u>=L+b*u, and
min(u,v)<=u. The b<=0 case uses N=beta*L+(-b)*v.
Also s<=|b|, including when b lies outside [-L,L]. Combining (3) and (4),

    H<=floor(s*min(u,v)/L)+1
      <=floor((N-L)/L)+1
       =floor(N/L)=Q.                                    (5)

There is also H<=d. Since the accepted endpoints are distinct, their forward
retained rank displacement D satisfies

    D=s-H,    1<=D<m,
    0<=H<=min(d,Q).                                      (6)

Consequently every verified factor obtainable from this N-linked coupling
for the fixed parameter a,t is covered by the direct public menu

    {s-h, m-s+h : 0<=h<=min(d,Q)}.                        (7)

The ordinary rank difference is D or D-m, and gcd ignores its sign.
Entries inconsistent with 1<=D<m can be omitted. Duplicates can be removed.
Zero, unit gcds, and gcd N are failures. Formula (7) is a dominance statement:
some menu entries may be unattained by the coupling, so its success set can
be strictly larger. It gives no lower bound on that set's source mass.

The root's general small-arc menu may be combined with (7), including the
lower bound D>=s-d and H<=s-1. The new count of candidate entries is at most
2(min(d,Q)+1), independently of whether d is numerically large or of
intermediate size.

## Consequences for the current three window scales

For the half-orbit window t=(N-1)/2, m=(N+1)/2 and Q=1 whenever q is
nonzero. Four direct integers suffice:

    s, s-1, m-s, m-s+1.

Since N is odd and 2m=N+1, their gcds can equivalently be tested using

    s, s-1, 2s-1, 2s-3.                                  (8)

This is a testable prediction for every fifth-rule F337 half-orbit cell,
including nonadjacent return indices and intermediate d.

For t=floor((N-1)/8), m=ceil(N/8)>N/8 because N is odd. Thus Q<=7,
and at most sixteen direct entries suffice. This bound does not assert
that the entries have a high factor probability.

For t=floor(sqrt(N)), Q can have square-root numerical size. Neither
this bound nor the earlier small-d bound makes all such menus cheap in
bit complexity. Sparse selection from the menu, another source law, or a
different observable remains a substantive question at that scale.

## The resulting public source is still worth measuring

For a macroscopic window m>=N/K with a public small integer K, setup is
the existing polynomial-bit extremum search. Compute b,q,s,Q. Scan (7)
with at most 2(K+1) gcds, charging setup, source-generation failures and
all tested entries. The procedure has no orbit-index draw, no rejected
endpoint, and no per-pair rank query. Any already found generation or setup
factor is a real output. Do not discard such cells from source accounting.

This is a concrete simplification of the selected N-linked coupling, not
a factoring impossibility conclusion. The unresolved question is the
unconditional source mass of proper gcds among the short list, particularly
the shifted entries absent from the frozen experiment's direct controls.
No factor label may choose a source parameter, jump, or menu entry.

## Half-orbit data reduce further to a reciprocal quotient

There is an exact, cheaper description of (8), including for nonadjacent
return indices. Let t=(N-1)/2 and

    r=min(a^(-1) mod N, N-(a^(-1) mod N)).

Then 1<=r<=t. Suppose first a*r=1 mod N, so alpha=1 and u=r.
Put s0=floor(t/r). The least positive integer beta for which the orbit
contains residue -beta is beta=s0+1. Indeed the orbit index for -beta is
N-beta*r: for beta<=s0 it is greater than t; for beta=s0+1 it lies between
1 and t. Thus

    beta=s0+1,   v=N-(s0+1)*r,   L=N-s0*r.

The a*r=-1 case interchanges alpha,beta and u,v. In both cases

    |beta-alpha|=s0,   L=N-s0*r.

For r>=2, s0<=t/2<L/2, so the centered jump length is exactly s=s0.
For r=1, a is 1 or -1, the centered jump length is 1 and the four-entry
menu has no proper gcd. Therefore every nontrivial half-orbit source can
be evaluated by one inverse, one quotient, and four gcds; the extremum
search is unnecessary for this particular menu.

Write

    N=2*r*s+R,   1<=R<2*r,   R odd.

Because r and 2r are units modulo N, the four gcds in (8) are exactly
the gcds with the following positive integers, in the same order:

    R, R+2*r, R+r, R+3*r.                                (9)

For example N-2*r*(s-1)=R+2*r and
N-r*(2*s-3)=R+3*r. All four residuals are less than 5r. Hence if the
least prime divisor of N is at least 5r, this source has no proper factor.
This is an offline diagnostic exclusion for the specified half-orbit
N-linked menu; the algorithm does not know the least prime divisor.

The closest earlier inverse-source calculation is F337
INVERSE_GAP_TRANSFER.md: its half-orbit cluster-boundary differences have
nonzero residuals bounded by 2b^2. Equation (9) concerns a different,
specific four-entry source and has a linear residual bound in r. Neither
bound covers arbitrary coupled rank procedures.

For numerically large r, (9) is still just four efficiently computed
remainders. Their source-level factor mass remains the question. This
quotient-and-remainder description is the concrete candidate to retain
if the rank experiment reports any fifth-rule gains.

## A scoped count for the uniform-unit half-orbit source

The same formula gives a specific source-mass upper bound. Let N=p*q with
distinct odd primes, and let ell be either prime. If one of the four
entries gives a proper gcd divisible by ell, then

    r>ell/5,   s>=ell/2.

The first inequality follows from (9). For the second, each nonzero
argument in (8) has absolute value at most 2s; the zero at s=1 is a full
gcd and is not an accepted output. Moreover s lies in at most four
residue classes modulo ell, from

    s=0,   s=1,   2s=1,   2s=3 mod ell.

Since s=floor(t/r)<5N/(2ell), the number of possible s is at most
4(floor(5N/(2ell^2))+1). For fixed s>=ell/2, its integer preimages r
lie in (t/(s+1),t/s], whose length is less than 2N/ell^2. There are
at most floor(2N/ell^2)+1 such integers. Thus the number of centered
inverse indices that can give a proper factor divisible by ell is at most

    B_ell=4*(floor(5N/(2ell^2))+1)
             *(floor(2N/ell^2)+1).                       (10)

This is an upper bound; it includes nonunits and unattained/unsuccessful
menu entries. Uniform a on the units makes r uniform on the phi(N)/2
unit indices in 1,...,t. Hence the menu-success probability is at most

    min(1, 2*(B_p+B_q)/phi(N)).

If q/p is bounded by a fixed constant, B_p+B_q is bounded independently
of N. The success probability is therefore O(1/N) for this specified
uniform-unit half-orbit menu. This does not include successes from drawing
and screening nonunits before obtaining a unit a. It does not bound a
biased source that concentrates on the small admissible set of r values,
or another window, source, transcript decoder, or factoring method.

The exact distinction is that the N-linked source can have a short,
efficiently evaluated menu but still needs appropriate source mass. This
calculation settles that mass only for the stated uniform-unit law.

## A precise zero regime for bounded rational sources

For the same half-orbit menu, let N be any odd composite integer with
least prime divisor P, and suppose

    a=x*y^(-1) mod N,   1<=x,y<=H<=P/5,

where x,y are units. Then the menu has no proper factor. Generation gcd
outputs, if a source is implemented with screening, remain separate real
outputs; this statement concerns its unit branch.

If a menu factor existed, choose any prime ell dividing that proper gcd.
Then ell>=P, the positive residual bound gives r>ell/5>=P/5, and the
nonzero original arguments give s>=(ell+1)/2. Thus
r<=t/s<N/ell<=N/P. These steps require neither squarefreeness nor
semiprimality. But x*r is congruent to either y or -y modulo N,
according to which centered representative defines r. The positive bound

    x*r+y<=H*(N/P+1)<=(N+P)/5<N

forces x*r=y; the negative congruence cannot hold. Thus r<=y<=H<=P/5,
a contradiction. The r=1 trivial branch gives no factor either.

This applies to direct sources (y=1), inverse sources (x=1), and bounded
positive ratio sources under the displayed bound. In particular a fixed
power cutoff H=N^gamma with gamma<1/2 eventually lies in this zero regime
on balanced semiprimes. It does not apply to larger cutoffs, other windows,
different jump rules, or other uses of the rational parameter. No factor
label chooses an actual parameter or test; P/5 is only the analysis guard.

## Positive pilot example at the boundary of the height guard

The frozen search pilot reports N=209, a=70=3^(-1) mod N, and t=104
with acceptance 103/105 and factor probability 22/35 under the fifth rule.
This is a legitimate finite factoring success. Here

    r=3, s=34, R=5, L=107, d=2,
    gcd(s-1,N)=gcd(33,209)=11,
    R+2r=11.

The direct quotient menu succeeds on this source with no endpoint loss.
It is outside the height-zero guard: P=11<5r=15.

The reported count also has a short exact explanation. For 0<=j<=34,
the ranks of indices 3j, 3j+1, 3j+2 are j, 35+j, 70+j, respectively.
The coupled endpoint is k'=(k-5) mod 107. Starts 3 and 4 are rejected.
For k=3j or 3j+1 with 2<=j<=34, the ordinary rank difference is 33;
these are 66 factor-producing starts. The remaining 37 accepted starts
have differences 34 or -71, both units modulo 209. Thus the exact
unconditional factor probability is 66/105=22/35.

Evidence for the frozen finite pilot is search_pilot_output.json and its
status/log in this packet. The general claims above remain unpromoted;
this one example neither establishes nor refutes an asymptotic source law.

The completed frozen search retains 147, 144, and 168 unit cells for
N=209,1333,10807. The fifth rule has respectively 35, 5, and 6 positive
cells, with cell-mean unconditional factor probabilities
10691/138915, 247037/98913432, and 387/151312. These means retain endpoint
failures within each unit cell, but are conditional on the original source
having supplied a unit parameter; generation records are separate.

The search worker's scale split gives 15/49, 1/48, and 4/56 positive
half-window cells. Every positive half-window cell at N=1333 or N=10807
already has a factor in the frozen basic direct controls. At N=209,
11 of the 15 positive half-window cells lack that basic explanation;
the inverse-three example above shows how the extra shifted quotient
entry can explain a real gain. These finite data do not test the new
unbounded proofs. The independent post-check below remains necessary
before using those proofs as a verified dependency.

Source artifacts are search_N209_output.json, search_N1333_output.json,
search_N10807_output.json, and search_aggregate_output.json. Strong gains
under other jump rules in those files are outside this note's algebraic
scope and must not be explained away by the fifth-rule result.

## Discriminating check after the frozen run

Do not change the frozen six-rule experiment. After it completes, an
independent small checker can use its retained arrays or regenerate the
same arrays to test (1), (2), (5), and (6) for every accepted fifth-rule
pair. In particular every half-orbit fifth-rule factor must be covered by
(8). Retain q=0 failures and the j branch. Report any first anomaly before
interpreting performance.

A separate exact source-level summary can count parameters for which (7)
has a proper gcd at the half and eighth scales. Compare with both the
coupling's unconditional factor probability and its existing direct
controls, retaining duplicate source parameters and all generation events.
The short-menu success indicator is not the coupling's per-index success
probability; report these separately and charge their different work.
This observation would measure a legitimate public candidate source,
without calling the extra coverage a collision gain.
