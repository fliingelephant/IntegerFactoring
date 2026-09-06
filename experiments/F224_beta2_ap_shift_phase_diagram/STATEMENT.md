# F224 candidate: an AP-Fermat bridge and an AP-shift obstruction

## Status and scope

This is a self-audited proof-only candidate for the balanced beta-two branch.  It uses a
public certified residue

\[
p\equiv s\pmod L,
\qquad \gcd(L,N)=1,
\]

where in the active application `L=lcm(2^t,M)`.  It proves a positive
gap-dependent deterministic terminal.  It then shows that uniform shifts
from the same public factor cell do not turn the P193 modified-AKS test into
a Las Vegas progress source on P193's intermediate-gap family before that
terminal applies.

It does not compute a new carry bit or enlarge `M`.

## Setup

Let

\[
N=pq,\qquad p<q<2p,\qquad d=q-p,
\]

where `p,q` are distinct odd primes.  Let `L>=1` and `s` be public, with

\[
\gcd(L,N)=1,\qquad p\equiv s\pmod L.
\]

## Theorem A: the residue gives a gap-sensitive Fermat terminal

Compute

\[
u\equiv Ns^{-1}\pmod L.
\]

Then `q congruent u (mod L)`.  Put `g=gcd(2,L)` and `m=L/g`.  The equation

\[
2A\equiv s+u\pmod L
\]

has one computable solution class modulo `m`, and

\[
A_*={p+q\over2}
\]

lies in it.  Starting at the first integer in this class not below
`sqrt(N)`, square-test `A^2-N` along the class.  The scan reaches `A_*`
after fewer than

\[
\boxed{1+{d^2\over4pL}}
\]

tests.  Every returned factor is verified by exact multiplication.

Consequently, this is a deterministic numerical-QP terminal whenever

\[
\boxed{{d^2\over pL}=\operatorname{QP}(n).}
\]

This can apply strictly before the gap-independent GFHP threshold
`N^(1/4)/L=QP(n)`.

## Theorem B: exact AP min-entropy bound for the P193 channels

Let

\[
I_N=\left[\left\lceil\sqrt{N/2}\right\rceil,
          \left\lfloor\sqrt N\right\rfloor\right]\cap\mathbb Z,
\]

and

\[
\mathcal C_{L,s}=\{x\in I_N:x\equiv s\pmod L\},
\qquad H=|\mathcal C_{L,s}|.
\]

The true `p` lies in this cell.  Fix `r>=2` with `gcd(r,N)=1` and

\[
r<d<p-1.
\]

For `x` sampled from the cell, first test `gcd(x,N)`.  On the remaining
unit shifts, form

\[
E_x(X)=(X+x)^N-X^N-x^N\pmod{X^r-1,N}
\]

and scan every raw coefficient gcd and the resultant/local-nullity channel
of P193.

Among all off-target integers in the cell, at most

\[
\boxed{rd(r+5)}
\]

can activate either modified-AKS channel.  Therefore a law `mu` on the
cell with largest atom `eta` has one-trial success probability at most

\[
\boxed{(1+rd(r+5))\eta.}
\]

The initial `1` is the exact-candidate event `x=p`.  In particular, a
uniform cell shift has success probability at most

\[
\boxed{{1+rd(r+5)\over H}.}
\]

The same bound holds conditionally at an adaptive stage when `r` and the
sampling law are fixed before its fresh shift.  Conditional union bounds
therefore apply to a bank of stages.

## Theorem C: below the two-thirds gap, the hybrid adds no preterminal progress

Fix `epsilon>0` and consider any balanced input family with

\[
d\le p^{2/3-\epsilon}.
\]

Fix any numerical-QP Fermat scan cap, numerical-QP trial count, and
numerical-QP moduli `r_i`, each chosen before its fresh uniform draw from
the full cell `C_(L,s)`.  On every sufficiently large member of this
family, one of the following holds:

1. the AP-Fermat scan factors `N` within its numerical-QP cap; or
2. the total probability that any exact-candidate, raw-coefficient, or
   resultant/local-nullity trial factors `N` is `2^(-Omega(n))`.

Indeed, failure of the capped Fermat scan forces, up to a fixed constant,

\[
L<{d^2\over p\,\operatorname{QP}(n)}.
\]

The balanced cell has `H=Theta(p/L)`, so Theorem B makes the complete bank
at most

\[
\operatorname{QP}(n){dL\over p}
\le
\operatorname{QP}(n){d^3\over p^2}
\le\operatorname{QP}(n)p^{-3\epsilon}
=2^{-\Omega(n)}.
\]

Thus the public AP does give genuine integer progress through Fermat, but
uniform sampling from that AP does not repair the modified-AKS source on
the remaining branch.

In particular, P193 supplies an infinite family with
`d=Theta(p^(3/5))`.  This is the case `epsilon=1/15`, and the last bound
contains the explicit factor `p^(-1/5)` before numerical-QP terms.

## Exact small certificate: AP conditioning need not add an off-target root

Take

\[
N=187=11\cdot17,\qquad L=2,\qquad s=1,\qquad r=2.
\]

Then `I_N={10,11,12,13}` and `C_(L,s)={11,13}`.  The point `11` is the
exact factor.  At the only off-target point `x=13`, the two cyclic
coefficients of the local modified-AKS error are

\[
(9,3)\pmod {11},\qquad (4,1)\pmod {17}.
\]

Its evaluations at the two roots of `X^2-1` are

\[
(1,6)\pmod {11},\qquad (5,3)\pmod {17}.
\]

Thus every coefficient gcd is `1`, both local nullities are zero, and the
resultant gcd is `1`.  This exact certificate refutes any claim that the
factor AP must contain an additional useful modified-AKS shift.

## Exact remaining scope

The result leaves open:

- public nonuniform laws with a proved heavy atom on a useful off-target
  shift;
- joint processing of typical nonzero coefficient vectors;
- choosing `r` after seeing the same shift;
- gaps `d>=p^(2/3-o(1))`, where the two phase scales cross;
- a sampler that certifies a new primary contribution to `M`; and
- a sampler that certifies the next dyadic factor bit.

The preregistered F224-D01 scalar-root run failed before mathematical work
because the remote image lacked `/usr/bin/time`.  The approved D02 changed
only that wrapper to shell `time -p` and completed 480 rows.  At the
preregistered capacity scale it found 15 off-target exclusive roots among
933,751 cell integers.  Across bit scales 12, 14, 16, 18, and 20, the
aggregate off-target fractions decreased from `9.93e-4` to `3.99e-6`.
This is finite obstruction guidance only.  No numerical claim is used in
the proof.
