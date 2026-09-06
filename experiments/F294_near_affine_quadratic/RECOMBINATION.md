# Recombine reciprocal window boundaries before closing the kernel family

Status: exact small-modulus symbolic recombination and coefficient-level
pairing test. No asymptotic closure or general impossibility claim.

## What was corrected by recombination

The added denominator in a termwise Euclidean decomposition is not
automatically an independent obligation. For the faithful N=147053 chart
at q=64, it cancels when the full child window polynomial is recombined.
This confirms the root's reason for requesting the test.

Here m=8, u=1, gamma=45, D=13, d=45. Put

    omega=e_8(1), Y=omega^(-b0), X=omega^(-2z),
    Z=X*Y^5, R=X*Y^6=Y*Z.

The first Euclidean child is exactly

    H=Z^2+Y*Z^3+Y^2*Z^5+Y^3*Z^6
     =Z^2*(1+R)*(1+Z*R^2).

In its two-boundary form it is

    Z^2*(P_4(R)+(Z-1)*R^2*(1+R)),

where P_4 is a finite geometric polynomial. The potential denominator
1-R cancels before a Gauss/Cauchy kernel is introduced. Both sides are
polynomials, so this cancellation is valid at resonance as well.

After this complete child recombination the remaining boundary bracket is

    H/(1-Z)+Z^(m-1)*P_4(Y)/(1-Z^(-1)).

The common outer factor and all Y phases are retained in the source. The
first full-period geometric term vanishes off resonance; its resonant value
is retained separately. For q=256 the child has twelve terms, with exponents
`1,2,3,5,6,7,8,10,11,12,13,15`; it too is recombined as its full polynomial.

## Pair the actual kernels, including affine recentering

Use the half-period convention

    F_(A,c)(t)=sum_(0<=z<m/2, t*omega^(-2z)!=1)
                 omega^(A*z^2+c*z)/(1-t*omega^(-2z)),

with c even. This is half the full-period F292 kernel. Write G_(A,c) for
the complete half-period Gauss sum and P_(A,c)(t) for the excluded pole
residue. Natural pole-excluded sums obey

    F_(A,c)(t)+F_(A,-c)(1/t)=G_(A,c)-P_(A,c)(t).

This convention was confirmed with `/root/localized_character`; see
`experiments/F292_localized_character/KERNEL_PRIMITIVE.md`.

Testing coefficients before recentering would be insufficient. If
t=omega^e, choose h=-e modulo m/2 so that shifting z by h sends the
inverse argument to t. The full reciprocal involution on phases is

    J(c)=-c+2A*h mod m,
    R_c=omega^(A*h^2-c*h),
    F_c(t)+R_c*F_(J(c))(t)=G_c-P_c(t).

For a two-element orbit, coefficients K_c,K_(J(c)) collapse to a Gauss
term exactly when `K_(J(c))=K_c*R_c`. Otherwise the exact remainder is

    (K_(J(c))-K_c*R_c)*F_(J(c))(t).

Self-reciprocal orbits with R_c=1 collapse to `(G_c-P_c)/2`. These are
actually present at q=256 and were included. They must not be mistaken
for unmatched terms merely because two earlier coefficients differ.

The source combines every child monomial, moves every inverse-argument
kernel into this common convention, and exhausts these reciprocal phase
orbits. No internal cone term is omitted.

## A concrete unmatched faithful boundary

For the q=64 faithful chart and b0=1, the quadratic coefficient is A=3,
t=omega^3, h=1. After including the reciprocal boundary, the only nonzero
same-argument coefficients are

    K_2=1,
    K_4=-1-omega-2omega^2,
    K_6=-omega.

The reciprocal orbits are `{0,6}` and `{2,4}`. Here R_2=omega. The exact
remainders after the available pairing are therefore

    -omega*F_(3,6)(omega^3),
    (-1-2omega-2omega^2)*F_(3,4)(omega^3).

Both coefficients are nonzero in Q(omega), since their displayed degrees
are below the cyclotomic degree four. This frame has no poles at all:
e=3 is odd whereas the orbit exponent is even. No finite-part convention
can remove this particular mismatch.

At q=256 the faithful parameters are **D=230**, not D=6:
`(u,gamma,d)=(1,109,109)`. For b0=1, A=11,t=omega^10,h=6, and z=5 is a
resonance. The self-reciprocal phases do collapse. Three other phase orbits
retain coefficients

    -1-omega^6,  -1-omega^2-omega^7,  2omega^3-omega^5,

at phases 4,14,12 respectively. They are nonzero in Q(zeta_16). Dropping
the high quotient in D would instead count a different window.

The established scalar identity holds its quadratic parameter fixed. In
the normalized frames that parameter is `-u^2/(b0*gamma) mod m`; distinct
odd b0 give distinct parameters. It supplies no additional cross-frame
pairing in this normalization. Stronger identities between those frames
are not ruled out by this test.

## Pole deformation is handled before substitution

An equality such as `Z^(m-1)=Z^(-1)` holds on the sampled roots but not
under a common deformation. Reducing that power before taking finite parts
can lose a coefficient-derivative correction.

The coordinated convention is: if

    F(t0*rho)=A/(1-rho)+B+O(rho-1),

then using t=t0*rho^s and a coefficient Q(rho) gives finite part

    Q(1)*(B+A*(s-1)/(2s))-Q'(1)*A/s.

Instead of mixing termwise conventions, the implementation evaluates the
**original complete finite polynomial** at each resonant z. This includes
the full-period geometric term and all varying monomial coefficients.
Away from those z it uses the paired pole-excluded kernels. Every frame is
checked against the unreduced polynomial expression before frames are summed.

## Full recombined results

The following are exact cyclotomic equalities, not numerical totals. The
columns give a fixed canonical decomposition after exhausting the stated
reciprocal pairs. “Pole” is the full-polynomial resonance contribution.

| q | u | gamma | D | Baseline | Paired Gauss | Unmatched kernel | Pole | Count |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 64 | 1 | 45 | 13 | 16 | 1 | 1 | 0 | 18 |
| 64 | 1 | 45 | 0 | 16 | 0 | 3 | 0 | 19 |
| 256 | 1 | 109 | 230 | 64 | 5/4 | 7/4 | 0 | 67 |
| 256 | 1 | 109 | 0 | 64 | 1/2 | -5/2 | 1 | 63 |
| 64 | 3 | 5 | 7 | 16 | -1/4 | 3/4 | 1/2 | 17 |
| 256 | 3 | 11 | 17 | 64 | 1 | -1 | 0 | 64 |

All totals match direct counts of the two original wrapped windows. The
last row shows why a total equal to the baseline is not proof that boundary
terms disappeared: its Gauss and unmatched contributions cancel each other.
The D=0, q=256 row also shows a nonzero resonance contribution.

The unmatched coefficients are the substantive evidence. A nonzero number
in the table alone would not prove that a further identity is unavailable.
Conversely, recombination really removed the intermediate denominator, so
its previous appearance is not being used as evidence against closure.

## Outcome and evidence

The attempted mechanism partially succeeds: opposite child boundaries cancel
an added denominator, affine recentering exposes genuine scalar reciprocal
pairs, and self-reciprocal kernels collapse with the correct residue term.
It does **not** automatically collapse the full actual window family under
that scalar identity. The explicit cut-phase coefficient mismatches above
remain after all frames and resonant values are retained.

This is a scoped result for the tested pairing mechanism, not a general
lower bound for Mordell reciprocity. The individual unmatched F kernels are
already covered by F292's fast-primitive analysis. The remaining issue is
aggregating their window-dependent coefficient family without enumerating
the outer phases.

`RECOMBINATION.py` uses exact rational coefficient arithmetic in
Q[X]/(X^(m/2)+1). It retains every frame coefficient and unmatched orbit in
`RECOMBINATION_output.json`. All six full-expression checks and every local
pairing/frame identity passed. The run took 0.067 seconds, one process,
with a 20-second alarm and estimated memory below 128 MB. Preflight showed
72% available memory and load 1.68. The log is empty on success.
No earlier source or shared research record was changed.
