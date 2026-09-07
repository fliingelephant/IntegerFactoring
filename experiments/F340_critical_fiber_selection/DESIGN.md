# Select adaptive fibers with a public quadratic character

**Family:** route:F29

Status: root-derived mechanism and bounded next experiment. Not independently
reconstructed or executed. No growth, success-probability, or QP claim.

## Question and closest prior

P245/F321 supplies a conditional all-input reduction for the adaptive
unit-output protocol H <- H(H-A), but no sufficient squarefree root-basin
growth law. Its ANALYSIS.md derives the additive-overlap drift and tests
the meaning of fiber guards; it also describes a two-sample-sum alternative.
The present source instead uses a public quadratic character tied to a
critical value of the composed polynomial. It aims to change the joint
local fiber law, not just add more uniform gcd probes.

Scoped Rust searches found no indexed "critical value" statement. The
Jacobi-filter route F10 instead constructs fixed-degree local automorphisms
from order filters; its existence-versus-construction gap is relevant context,
not a result about this adaptive selector. Recognizing different local fiber
sizes here does not construct the unknown roots or an automorphism. This
comparison establishes no novelty. Check relevant arithmetic-dynamics
literature after examining the construction; feasibility opinions are not
hypotheses.

The question is whether the character can select useful local fiber
asymmetry at higher depths with enough growth per total charged work.
A lower accepted-update count alone is not the objective.

## A precise degree-four seed

For odd N put H_1(X)=X(X-1). Choose a public U and let c_2=H_1(U),
accepting this initialization only when c_2 and 2U-1 are units; a proper
gcd during either check is a legitimate factor. Put

    H_2(X)=H_1(X)*(H_1(X)-c_2).

For a fresh public X define y=H_1(X), Y=H_2(X), and

    D=1+4*(c_2-y),
    J=(2X-1)*(2y-c_2).

Suppose Y,D,J are units. Over any odd prime factor p, the equation
H_2(Z)=Y splits into

    H_1(Z)=y  or  H_1(Z)=c_2-y.

The first has the two distinct known roots X,1-X. The second has
discriminant D. The J guard makes the two branches distinct; the D guard
excludes a repeated root in the second branch. Therefore the exact local
fiber size is

    3+Legendre(D,p),

namely four or two. For distinct-prime N=pq, Jacobi(D,N)=-1 forces these
sizes to be four in one field and two in the other. Appending c_3=Y gives
H_3=H_2(H_2-Y), whose new zero roots are disjoint from the old ones because
Y is a unit. This is an exact finite-degree mechanism, not an exponential
growth conclusion. The initializer gives four simple H_2-zero roots in
each field whenever its unit guards hold.

## The public observable at arbitrary depth

For coefficients c_1=1,c_2,...,c_t, let

    H_0(X)=X,
    H_j(X)=H_(j-1)(X)*(H_(j-1)(X)-c_j),
    z=1/2 mod N.

Define the derivative product and divided critical-value difference by

    J_t(X)=product_{j=1}^t (2H_(j-1)(X)-c_j),
    W_t(X)=-product_{j=2}^t
        (H_(j-1)(X)+H_(j-1)(z)-c_j).

Polynomial factorization of a difference gives the exact identity

    H_t(z)-H_t(X)=(X-z)^2*W_t(X).

No division by X-z is needed to evaluate W_t. At depth two, 4W_2=D,
so its Jacobi symbol gives precisely the preceding selector. Cache the
single critical orbit H_j(z) as coefficients are appended. Once J_t is a
unit, X-z is a unit too. Thus W_t has the same gcd and Jacobi symbol as

    Delta_t=H_t(z)-H_t(X).

The runtime should use this single subtraction, not multiply the W factors.
The W formula remains an identity to check and a way to analyze the selector.
A fresh probe evaluates H_t and J_t in O(t) modular operations; the formal
degree 2^t is never expanded.

At larger depths the character of W_t is only a proposed selector. It
does not by itself prove a four-versus-two fiber law, useful logarithmic
drift, or control of the rest of the preimage tree. Those are research
questions, not assumptions.

## Public finite protocols and controls

Use the same fixed initial H_1=X(X-1) in every policy. Each raw probe draws
X uniformly modulo N and first gcd-screens Y=H_t(X). A proper gcd returns
a verified factor; a full gcd rejects the probe without an update.

Compare five policies on independent, reproducible streams:

1. Baseline appends each unit Y, as the unguarded adaptive protocol does.
2. Screened control additionally gcd-screens J_t and, for t>=2, Delta_t.
   A proper gcd succeeds; a full gcd rejects. A surviving Y is appended.
3. Negative-character selection uses the same screens, and for t>=2
   appends Y only when Jacobi(Delta_t,N)=-1.
4. Positive-character control uses the same screens and Jacobi(Delta_t,N)=1.
5. Coin-thinning control uses the same screens but, for t>=2, appends Y
   with an independent fair coin instead of evaluating a Jacobi symbol.
   Record actual acceptance rates; one half is only this control's rule.

At t=1 the last four policies use the J_1 guard but no W/Jacobi/coin selector;
W_1=-1 would be constant. This supplies the stated guarded c_2 initialization.
All failed probes and rejected parameters are charged. If a product gcd is
N, the initial protocol rejects it; it does not silently count an unrun
factor-isolation search. Different treatment can be a later measured policy.

Separate factors found through Y, derivative J, and critical difference Delta.
Compare
the character policies with the same-screen control so extra gcd successes
are not mistaken for a selection advantage. The coin control distinguishes
character information from merely holding H fixed for more probes. Keep
modular multiplications, gcd work, Jacobi work, raw probes, accepted updates,
and time visible.

The screened policies preserve a known unit at the critical point:
V_t=H_t(z) starts at -1/4, and an accepted update gives
V_(t+1)=V_t*Delta_t. At t=1 the J_1 guard already makes Delta_1 a unit;
later Delta is explicitly screened. Thus no screened polynomial vanishes
on the entire field at a prime divisor. This does not bound overshoot away
from 1-1/p or prevent a rejected-parameter stall. The negative-character
policy also flips Jacobi(V_t,N) at each selected update after depth one;
this sign identity is not a root-growth theorem.

## Bounded discovery sequence

First verify the displayed polynomial identities and the degree-four fiber
law on small fields and odd distinct-prime products, including all guard
failures. This is a finite algebra check, not a proof promotion.

Then use F321's wider-gap balanced and unbalanced public inputs, not only
the first-Fermat-step inputs used by F337. Start with 32 independent trials
per policy on its 17--33-bit pilot cases and a public cap of 512 raw probes.
Record the first Fermat square-test control from N separately. These are
finite resource caps; they are not requirements for a final Las Vegas proof.
Keep compact per-trial seeds, outcomes and operation summaries. Full traces
are needed for the identity controls, selected witnesses and anomalies;
other runs must reproduce from the frozen source and seed.

For a small subset with affordable field populations, separately retain
offline local zero masses, selected-fiber sizes, nonzero collision energies,
and W-character labels before each public update. Prime factors may label
and audit those populations, but must never choose a public seed, reject a
parameter, or direct the algorithm. Distinguish actual surviving histories
from any forced-chain diagnostic, as F321's analysis requires.

Look for a repeatable change in local growth or survival after all selector
costs are included. If no such change appears, record the scoped null and
change the mechanism. Do not infer a QP law from a fitted exponent or a
constant speedup.

Use suitable exact modular tools, current CPU/memory/process preflight,
a small pilot, named sources, logs, outputs, and hashes. Start with one
single-threaded job, at most 512 MiB and 28s internal/30s external timeout;
split cases when needed. Estimate the field-array memory before allocating
it. Larger searches can use seetacloud after the required remote preflight.

P245's existing radical-shadow theorem does not automatically apply to these
Jacobi-based rejections: changing prime exponents changes the Jacobi
character. A positive new squarefree result would still need a correct
all-input reduction or separate repeated-factor analysis.
