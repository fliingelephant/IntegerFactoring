# Cached Mordell identity: a phase discrepancy in equation(7)

The cached arXiv:1306.4081 PDF is dated October30,2018 and has SHA-256
`32eb8fb8697a1289707186bdcf93c1b3644bcc5b6689c7d0f82324a2c9af75b5`.
Its extracted equation image
`.knowledge/.figures/arxiv__1306.4081/1306.4081.pdf-0003-11.png` visibly has
coefficient **-1/2** on the second remainder term. The raw PDF and image
remain unchanged. This note concerns that cached version; no claim about
every published version or an author's intended formula is made.

The identity used in F296 has **-i/2** there. This is an author-derived
correction, not an unmarked transcription of the displayed equation.
The discrepancy was found by a failed numerical check and then resolved
algebraically from the source's equations(16),(17). The failed comparison
is retained in `outer_mordell_setup.log`.

## Derivation from the earlier equations

Use the source's F_n(z,tau)=sum_{k=0}^n e(z*k+tau*k^2). Set w=alpha+1/2,
t=2tau, X=n+1/2. Equation(16), divided by its F_n prefactor, gives

    F_n(alpha,tau)
      = C0+(i/2)*e(X*(alpha+tau*X))*h(alpha+t*n+tau+1/2,-t),

    C0=-(i/2)*exp(-pi*i*(alpha-tau/2))
                 *h(alpha-tau+1/2,-t).

The i in the second coefficient follows from
(-1)^n*exp(pi*i*(n+1/2))=i. Applying equation(17) to shift the last h argument
down by r+1 multiplies its remaining h term by(-1)^(r+1). Therefore that
term has coefficient

    -(i/2)*(-1)^r*e(X*(alpha+tau*X)).

The accompanying finite Gaussian term, after reversing its summation index
as in source equation(18), is

    lambda*F_r(alpha/(2tau),-1/(4tau)),
    lambda=exp(pi*i/4-pi*i*alpha^2/(2tau))/sqrt(2tau).

This proves the corrected identity used in `REPORT.md`, conditional only
on the earlier stated h transformation identities. No absolute-square
substitution or discarded phase is involved.

## An exact nonzero difference between the two versions

Take n=r=0, alpha=3/4, tau=1/4. The endpoint h argument is1/2. Pairing x
and-x in its defining integral cancels cosh and gives

    h(1/2,-1/2)=1-i.

The exponential endpoint weight is e(7/16). Changing the printed coefficient
-1/2 to the derived coefficient-i/2 changes the right side by

    ((1-i)/2)*e(7/16)*(1-i)=-i*e(7/16)=e(3/16),

which has absolute value1. Thus the two formulas are not interchangeable
even at this simple input. This is an exact difference witness. The six
full numerical comparisons in the retained pilot support the derived
version, with maximum discrepancy below2e-42 at45-digit working precision.
Those quadrature checks are not interval-certified proofs.

The root subsequently reported45 independent comparisons using the H1+J
Laplace representation rather than this packet's rotated h integral. The
derived coefficient agreed within8.91e-37, while the printed coefficient
differed by up to1.58. That separate evidence is retained in
`../F297_mordell_boundary/completed_prefix.json`; consult the root's F297
packet for its completed-prefix formulas.

The source is [Kuznetsov, arXiv:1306.4081](https://arxiv.org/abs/1306.4081),
equations(6),(7),(16)--(18). Full-text provenance is retained in
`../F292_localized_character/reference_theta_algorithms/SOURCE_MANIFEST.json`.
