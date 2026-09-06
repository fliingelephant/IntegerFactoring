# F295: auxiliary Gauss coordinates and the retained quadratic window

**Family:** route:F31

Status: exact identities and finite symbolic validation. This gives a
constructive transformed kernel and a counterexample to a specified joint
quadratic-phase closure ansatz, not a general impossibility result.

## Act on the full window expression

Use the F294 notation m=2^r,q=m^2,r>=3, omega=e_m(1), with u,gamma odd and
the faithful invariant u*gamma=N modulo q when using an inverse chart.
Set d=gamma/u modulo q and retain the **full** window polynomial

    B(Z,b)=sum_(i mod m) omega^(-Z*i-b*floor((d*i+m-1-D)/m)).

The actual count is

    C=q/4+(4/m^2)*sum_(b odd mod m) sum_(z mod m/2)
      G_m(b*gamma)*omega^(-u^2*z^2/(b*gamma))
      *B(2z,b)/((1-omega^(-d*b))*(1-omega^(-b))).

This is the expression already validated in F294. Using B before a
pole-bearing cone decomposition retains all window phases and all removable
values. Both displayed denominators are nonzero.

Undo the complete Gauss sum exactly:

    G_m(b*gamma)*omega^(-u^2*z^2/(b*gamma))
      =sum_(x mod m) omega^(b*gamma*x^2+2u*z*x).

Thus this step acts on the whole b,z expression, not on an isolated
denominator or a phase-free Gauss amplitude.

## Adjacent Euclidean rays become coordinate axes

Let two adjacent ray vectors be (p,q0),(r0,s), with
epsilon=p*s-q0*r0 in {+1,-1}. Write Z=2z and change coordinates by

    R1=p*Z+q0*b, R2=r0*Z+s*b modulo m.

The domain is exactly the parity coset

    R1=q0 mod 2, R2=s mod 2.

The inverse is `Z=epsilon*(sR1-q0R2)`,
`b=epsilon*(-r0R1+pR2)`. Substitute these expressions into the complete
window weight above. Its auxiliary phase is now

    R1*epsilon*(-gamma*r0*x^2+u*s*x)
      +R2*epsilon*(gamma*p*x^2-u*q0*x).

This identity preserves the full count. If the original weight is represented
by signed cone terms, the two selected denominator directions become R1
and R2. For full-expression validation the prototype instead substitutes
into B itself, so no pole correction can be lost by separate specialization.

## An exact axes summation, rather than another reindexing

Define the natural pole-excluded axis transform

    J_eta(P)=sum_(R mod m, R=eta mod 2, R!=0)
                 omega^(P*R)/(1-omega^(-R)).

It has the elementary exact values

    J_0(P)=(m/2-1)/2-(P mod m/2),
    J_1(P)=m/4 if P mod m<m/2, and -m/4 otherwise.

To derive them, the full nonzero transform is
`(m-1)/2-(P mod m)`. Subtract its even-R part to obtain the odd part.
Thus these sums are Bernoulli and half-window weights, not unevaluated
Gauss sums.

A third denominator from the original b direction can also be retained
exactly. Since b and d are odd,

    1/(1-omega^(-d*b))=(1/2)*sum_(0<=t<m/2) omega^(-d*b*t).

For a transformed cone with linear numerator shifts c1,c2, set

    L1(x,t)=epsilon*(-gamma*r0*x^2+u*s*x+d*r0*t)+c1,
    L2(x,t)=epsilon*( gamma*p*x^2-u*q0*x-d*p*t)+c2.

Its pole-excluded three-denominator auxiliary kernel becomes exactly

    (1/2)*sum_(x mod m) sum_(0<=t<m/2)
                       J_(q0 mod 2)(L1(x,t))*J_(s mod 2)(L2(x,t)).

This is a constructive contraction of the two coordinate sums. The result
is a two-variable quadratic window/Bernoulli moment at modulus m. It does
not require numerical Cauchy evaluation. Pole terms from a signed cone
decomposition must still be supplied by the original combined expression;
the separate full-window identity above includes them automatically.

The new arguments satisfy useful exact relations:

    p*L1+r0*L2=u*x+p*c1+r0*c2,
    q0*L1+s*L2=gamma*x^2-d*t+q0*c1+s*c2.

Hence (x,t) to (L1,L2) is a polynomial bijection modulo m: x is recovered
linearly and t then quadratically. The remaining restriction t<m/2 becomes
an extra quadratic half-window in the two new coordinates. It cannot be
dropped. If t instead ranges over all m values, bijectivity and the zero
means of both J weights make the moment exactly zero.

For example, a component test using the actual q=64 ray matrix `(1,5;1,6)`,
u=1,gamma=45 and test shifts `(c1,c2)=(1,13 mod 8)`, gives the retained
moment -4. These test shifts are not asserted to identify a particular
term of the full cone expansion; the whole window is checked separately.
Removing
the t half-window gives zero. This is an exact counterexample to the
“complete the last coordinate sum” shortcut. The moment is signed; it is
not a positive witness count on its own.

## The joint quadratic-phase ansatz fails precisely

The auxiliary phase is quadratic in x for each fixed pair R1,R2, but it is
not jointly quadratic. Let R1=eta1+2t1 and R2=eta2+2t2, so the parity domain
is retained. Its mixed third difference is

    Delta_t1 Delta_x^2 phase = -4*epsilon*gamma*r0,
    Delta_t2 Delta_x^2 phase =  4*epsilon*gamma*p  modulo m.

At least one of p,r0 is odd because the ray matrix is unimodular. Since
gamma is odd and m>=8, at least one difference is nonzero. A genuine
jointly quadratic phase has every third additive difference zero. An
invertible affine change of the retained lattice coordinates cannot remove
this nonzero difference; it only changes its direction labels.

Thus the specific ansatz “undo Gauss, align the adjacent rays, then invoke
a fixed-dimensional complete quadratic-Gauss evaluator” is already false
at q=64. This does not exclude an efficient evaluator for the new quadratic
window moment or other non-Gaussian manipulations.

## A complete residue-stratified repair, with its actual state count

Consider the literal repair of partitioning only x into residues modulo
2^a, keeping both ray coordinates on their full parity coset. Write
x=x0+2^a*y. The sole jointly cubic term is

    2^(2a+1)*gamma*(-epsilon*r0*t1+epsilon*p*t2)*y^2.

It becomes a quadratic function modulo 2^r precisely at

    2a+2>=r.

If 2a+1>=r it vanishes. If 2a+1=r-1, replace y^2 by y in that term,
because their difference is even. If 2a+2<r, the same mixed third-difference
test remains nonzero on at least one ray coordinate.

Therefore this particular exact repair needs

    2^ceil((r-2)/2)

auxiliary residue classes. This is a proved count for the specified
stratification, not a lower bound for every possible evaluator. The windows
are still present even after this repair.

| Reduced modulus bits r | Minimum residue bits a | Classes |
|---:|---:|---:|
| 3 | 1 | 2 |
| 4 | 1 | 2 |
| 8 | 3 | 8 |
| 16 | 7 | 128 |
| 24 | 11 | 2048 |
| 32 | 15 | 32768 |

The original modulus had 2r bits. Consequently this literal route has an
exponential branch factor at the proposed bit-halving step, rather than
the required polynomial number of smaller instances. The exact axis-moment
route avoids that stratification but requires the extra retained quadratic
half-window described above; its recursive closure has not been proved.

## State and precision accounting

The transformation has polynomial-size coefficient descriptions. Phase
coefficients can be reduced modulo m, while the full d,D data in B retain
O(r)-bit descriptions. No numerical-scale operand length is introduced.
For a fixed nonresonant three-denominator term, denominators at m-th roots
have magnitude at least 4/m. The direct sum bounds therefore require only
O(r+log(1/error)) precision bits up to fixed constants. The present issue
is the number and type of retained states, not an exponential precision
requirement. Resonant terms use the previously recorded full-polynomial or
common-deformation finite-part rule.

## Exact evidence and conclusion

`auxiliary_coordinates.py` retains all data and phases. It checks seven
complete window expressions, including faithful N=147053 charts at q=64
and q=256 with D=13 and D=230, plus D=0 and additional controls. Their counts
are respectively 18,19,67,63,17,64,18. All transformed expressions match
direct counts.

The run also checked 256 auxiliary-Gauss identities, 256 coordinate-domain
points, seven exact axis-moment identities, and 3584 residue-repaired phase
equalities. The seven unrestricted-t controls are exactly zero. Larger
stratification counts in the table come from the explicit valuation formula,
not a runtime fit.

Preflight showed 73% available memory and load 1.97. The one-process exact
Python pilot took about 0.10 seconds under a 30-second alarm, estimated
memory below 128 MB. Source, JSON output and log are retained here. Its
small cyclotomic arrays are validation tools, not a claimed polynomial-bit
implementation of the enlarged kernel.

The new constructive target is explicit: a two-variable quadratic
half-window/Bernoulli moment under a unit-Jacobian polynomial map. The
single joint-quadratic-phase shortcut is refuted, and its literal
residue-stratified repair has quantified branching. No conclusion against
other exact contractions or the full factoring goal is drawn.
