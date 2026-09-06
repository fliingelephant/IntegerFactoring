# F299 affine classes are the P235 cover on faithful inputs

**Outcome:** the root-derived coordinate change collapses each F299
three-variable halfbox class to one ordinary affine half-window. For faithful
inverse charts, the resulting classes are exactly P235's affine cover.
The two-stage construction did not discover a new asymptotic factoring
mechanism. Barvinok's theorem is unnecessary for this halfbox class.

**Status:** elementary root-derived identities, worker algebra check, and
small exact certificates. P235 was loaded through the Rust reader. No
external novelty claim is made.

## Abstract class: one affine half-window

Retain the F299 parameters

    m=2^k, r=2^floor(k/2), L=m/r,
    kappa=beta*r mod L, 2*kappa=0 mod L,
    E_i0=floor((m*beta*i0^2-d*i0+D)/r),
    A_i0=m*(2*beta*i0+kappa)-d,
    T=m*L=m^2/r.

The class in REPORT.md counts0<=x<L,0<=v<m/2 with

    (A_i0*x+E_i0-L*d*v) mod T<T/2.

Set t=x+L*v. This is a bijection onto the integers0<=t<T/2. Since

    A_i0+d=m*(2*beta*i0+kappa),

the difference between A_i0*t+E_i0 and the previous argument is
L*(A_i0+d)*v, a multiple of T. Hence the class is exactly

    W_(A_i0,T)(E_i0)
       =#{0<=t<T/2:(A_i0*t+E_i0) mod T<T/2}.            (1)

Two ordinary Euclidean floor sums evaluate this affine half-window in
polynomial bit complexity. Thus no fixed-dimensional polytope machinery
is needed for(1). This conclusion holds for the abstract odd d,beta and
arbitrary D used in F299; faithfulness is not needed for this part.
Explicitly, with n=T/2,

    W=n+sum_{t=0}^{n-1}floor((A_i0*t+E_i0)/T)
         -sum_{t=0}^{n-1}floor((A_i0*t+E_i0+T/2)/T).

This formula also allows negative representatives A_i0,E_i0.

For arbitrary restricted x,v ranges, t lies in the corresponding union of
intervals/arithmetic blocks. This note does not replace those restrictions
by a single full half-interval. The one-window statement above concerns the
full halfbox class that was counted in F299.

## Faithful inverse chart and its exact expansion

Now assume an original odd N and modulus M=m^3, with odd0<u0<m. Define

    v0=N/u0 mod M,
    d=N/u0^2 mod m^2,
    beta=N/u0^3 mod m,
    D=floor(v0/m).

For J modulo m^2, the original inverse graph is

    X=u0+m*J,
    Y=(v0 mod m)+m*(F(J) mod m^2),
    F(J)=-d*J+m*beta*J^2+D.                            (2)

This follows directly by truncating the inverse expansion at degree two
modulo m^3. In the F294 notation, gamma=N/u0 modulo m^2, so its d and beta
are exactly the quantities above.

Put

    S=m*r=2^floor(3k/2), T=m^2/r, S*T=M,
    U0=u0+m*i0,
    f0=F(i0), E_i0=floor(f0/r),
    V0=(v0 mod m)+m*(f0 mod r).

Write J=i0+r*t. Expanding F gives

    F(i0+r*t)=f0+r*(2m*beta*i0-d)*t+m*beta*r^2*t^2.

After division by r, the quadratic term is m*beta*r*t^2. Modulo
T=m*L it equals m*kappa*t, because beta*r=kappa modulo L and
kappa*(t^2-t)=0 modulo L. Consequently

    F(i0+r*t)=(f0 mod r)+r*(E_i0+A_i0*t) mod m^2.

Substitution into(2) proves the original-coordinate parametrization

    X=U0+S*t,
    Y=V0+S*((E_i0+A_i0*t) mod T), 0<=t<T.             (3)

The residues satisfy0<U0<S and0<V0<S. Therefore X<M/2 exactly when
t<T/2, and Y<M/2 exactly when(E_i0+A_i0*t) mod T<T/2. The half-window
in(1) is the original coordinate halfbox on this affine branch.

## Identification with P235, including the slope and class count

At t=0, the full y-coordinate is

    v=V0+S*(E_i0 mod T)=N/U0 mod M.

The difference between consecutive y-coordinates modulo M is

    delta=S*A_i0 mod M
         =N*((U0+S)^(-1)-U0^(-1)) mod M.                (4)

Thus the full lattice is precisely

    (U0,v)+Z*(S,delta)+Z*(0,M),

as in P235. The sign is the inverse finite-difference sign, not its
negative: (3) gives(4) directly.

As u0 ranges over the odd residues below m and i0 over0,...,r-1, U0=u0+m*i0
ranges bijectively over every odd residue below S. There are exactly S/2
classes. Since log2 M=3k, the stride

    S=2^floor((log2 M)/2)

is exactly P235's stride. The parity identity t^2=t mod2 is the same
reason that the floor rather than ceiling of the half-bit count suffices.

Accordingly, about sqrt(m) classes inside each of the m/2 faithful charts
are the same S/2 classes already present in P235. Reorganizing them in two
stages does not improve their asymptotic count. For abstract nonfaithful
(u,gamma,D), only the affine-window collapse in(1) is asserted; the original
N/M interpretation and P235 identification require the displayed faithful
relations.

## Small exact checks

`affine_equivalence.py` checked288 abstract coordinate-collapse points in
the retained q64/q256 controls. It also checked100 original inverse points
from20 faithful classes, using N=147053 and8464705853 at m=8,16. The tested
t values include0,1, both sides of the input-half boundary, and T-1.
Every predicted Y equals N/X modulo M exactly. The P235 base and finite
difference in(4), both coordinate-half tests, and the bijection of all U0
origins were also checked.

The integer-only pilot had a20-second alarm, estimated peak below64MiB,
and used16.3MiB with runtime0.0006seconds. Preflight reported
load2.54/2.33/2.18,71% available memory and no swap; several Apple background
processes occupied cores, so no heavier computation was started. Source,
JSON and log are retained. No shared metadata or commit was made.
