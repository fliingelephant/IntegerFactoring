# Whole-family second products and the retained linear carry digit

**Family:** route:F31

**Status:** author-derived algebra and finite exact controls. No independent
proof reconstruction or novelty claim. This packet constructs a polynomial
whole-family norm gate, but does not construct P239's B evaluator.

## Candidate and outcome

The candidate was to multiply every correlated Möbius branch before taking
the second symmetric correction. This genuinely removes the need to compute
cross-branch quadratic terms individually. The result is one exact global
identity coupling B to a higher digit of the total *linear* carry. That
digit retains the mixed cut information. Reblocking preserves both the carry
and the norm's evaluation parameter, so the tested norm construction does
not give an independent equation or a decreasing-precision recurrence.

This is an exact test of the proposed whole-product contraction. It is not
a lower bound against another aggregate functional.

## 1. Full original input and shifted product

Let M=2^k, k>=2, H=M/2, and N odd. Use P239's shifted coordinates

    x=u+M*1_(u<c), y=v_N(u)+M*1_(v_N(u)<d),
    q=(xy-N)/M.

Write Q=sum q and B=sum binom(q,2). Define the two marginal products

    P_c=product_(u odd<M) [u+M*1_(u<c)],
    P_d=product_(v odd<M) [v+M*1_(v<d)].

Every actual point is retained, including negative carries and cuts at zero
or M. Since v is a permutation,

    R_cd = P_c P_d / N^H
         = product_(u odd<M) [1+(M/N)q].                    (1)

This is an exact rational identity with odd denominators.

For every integer list of carries,

    e2(q) = binom(Q,2)-B.                                  (2)

Consequently, modulo M cubed,

    R_cd = 1+(M/N)Q+(M squared/N squared)[binom(Q,2)-B].      (3)

All elementary terms of order at least three vanish at this precision.
There is no division-by-two precision loss in (2), since each binomial is
formed as an exact integer before reduction.

## 2. The computable norm residual and the missing digit

Compute R_cd modulo M cubed and set

    Qbar = N*((R_cd-1)/M) mod M, in [0,M),
    h=(Q-Qbar)/M,
    E_cd = N squared/M squared *
      [R_cd-1-(M/N)Qbar-(M squared/N squared)binom(Qbar,2)]
      mod M.                                               (4)

The displayed division by M squared is exact after reduction modulo
M cubed. Expanding Q=Qbar+Mh gives

    E_cd = (N-M/2)h-B mod M,
    B = (N-M/2)h-E_cd mod M.                               (5)

In particular, the M/2 correction cannot be dropped: although Qbar is
known modulo M, binom(Q,2) needs the extra parity of h. The factor
N-M/2 is odd. The second-order gate has therefore converted the quadratic
target to one higher linear-carry digit with an invertible coefficient.
It has not annihilated that digit.

## 3. A polynomial implementation of the entire norm gate

The shifted odd set consists of H consecutive odd integers starting at
a=2 floor(c/2)+1. Thus

    P_c = a^H product_(0<=t<H)(1+2t/a).

Modulo 2^P, only elementary-symmetric indices j<P contribute:

    P_c = a^H sum_(0<=j<P) (2/a)^j e_j(0,1,...,H-1) mod2^P. (6)

The pilot computes ordinary power sums of t by exact telescoping, and the
e_j by exact integer Newton identities. The index bank has P terms and
polynomial bit heights in k,P. Modular powering uses the binary exponent H.
Setting P=3k gives P_c and P_d, hence Qbar and E_cd, in polynomial bit
cost without enumerating the unit set or any Möbius branches.

This is an implemented global operation. Its arithmetic is a special case
of the universal product mechanisms already used in F303; the elementary
product algorithm carries no novelty claim.

## 4. What happens to cross-branch terms

Partition the original points into any blocks, with carry sums Q_j,
binomial sums B_j, and second elementary terms e2_j. Exactly,

    e2_all = sum_j e2_j + sum_(i<j) Q_i Q_j,
    B_all = sum_j B_j.

Equation (2) cancels every cross-block term after the product is assembled.
Thus the whole-family norm really does aggregate the quadratic cross terms;
the failure is not an overlooked extra denominator or failure to multiply
the blocks first.

For clarity, normalize *every block* with the same original step M/N and
the same output modulus M. Let Qbar_j=Q_j modM and h_j=(Q_j-Qbar_j)/M.
Then the exact residual recurrence is

    h_parent = h_0+h_1+floor((Qbar_0+Qbar_1)/M),
    E_parent = E_0+E_1
               +(N-M/2)floor((Qbar_0+Qbar_1)/M) modM.       (7)

The known carry correction in (7) is cheap when the two low sums are
available. The unknown h values still add with coefficient one. The
recurrence does not halve their requested precision.

## 5. Faithful Möbius reblocking has a rigid norm parameter

On an actual r-bit low-residue patch set R=2^r, L=M/R and

    u=u0+R X, v=v0+R Y,
    C=R, A=v0, B=u0, n=(N-u0 v0)/R.

For shifted representatives the same formulas hold with X,Y in shifted
integer intervals. They give

    CXY+AX+BY-n=Lq, K=AB+Cn=N,
    LC/K=M/N.                                              (8)

F304's parity transformation replaces C by 2C and L by L/2, preserves K,
and preserves q pointwise. Therefore the diagonal specialization of its
formal product always has the same parameter LC/K=M/N. Combining
different dyadic blocks does not provide a second specialization of
product(1+tq). Varying t independently would require an additional
evaluator; it is not supplied by faithful coordinate changes.

This proves parameter rigidity for this actual branch-product ansatz.
It does not rule out another kernel whose parameter changes under descent.

The needed precision is also fixed. Recovering B modulo M by (5) needs
Q modulo M squared, regardless of the current branch length L. In the
Möbius coordinates this means retaining F=Lq modulo L M squared before
division by L. Applying only a branch-local moment theorem modulo L squared
would silently discard information when L<M.

## 6. The joint cut remains in h

The marginal norm is multiplicatively separable in c,d. Its additive
second-order residual nevertheless has the joint term in (5), coupled to h.
An explicit exact relation identifies it. For a rectangle [a,b) by [c,d),

    Q(b,d)-Q(a,d)-Q(b,c)+Q(a,c) = M*rectangle_count.          (9)

Thus, writing Delta for this four-corner contrast,

    Delta h = rectangle_count - Delta Qbar/M.               (10)

The numerator Delta Qbar is divisible by M. It is known from the norm
gate. Formula (10) shows exactly where the retained cut correlation sits;
it is not a smooth marginal term. No assertion is made that the full input
cannot determine h by a different operation.

## 7. Exact controls and closest prior overlap

The initial mechanism preceded source checks. Rust reads used P239 and the
F306 packet; targeted prior reads used F303/CLOSED_FORM.md and
EXPONENT_DERIVATIVE.md. F303 already records the unshifted second-order
carry correction and dependent exponent-derivative equation. This packet's
scope is the fully shifted, whole-family product, its exact norm residual,
and rigidity under faithful Möbius block changes. No broad novelty claim is
made, and no new external summation theorem is assumed.

`pilot.py` checked 373 original-N cut pairs, including endpoints, random
cuts, and cuts from F301 public factor rectangles. It checked 1,095 block
regroupings and 62 exact mixed first-moment rectangle identities. The norm
gate itself does not enumerate; independent controls enumerate Q and B.
All checks passed. Setting the missing h to zero gave a wrong B in 367
of the 373 cases, so that shortcut is concretely rejected.

For the actual public input N=323, M=32 and cuts c=17,d=18,

    B=19, Qbar=27, h modM=12, E=17.

Equation (5) returns 19; dropping h returns 15. The same original N and
windows are used in both computations.

The run took 0.131 seconds and 21,397,504 peak RSS bytes. Source, output,
log, resource record, and the preliminary exploratory source/output are
retained. The achieved contraction is in algebraic degree, from a quadratic
sum to a higher linear-carry digit. Its required precision does not decrease,
so no quasipolynomial recurrence or rectangle oracle is established.
