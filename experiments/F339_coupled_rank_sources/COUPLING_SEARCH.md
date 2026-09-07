# Next search: nonuniform jumps on the existing gap sources

**Family:** route:F31

Status: root-designed experiment, not executed. RETURN_MAP_JUMPS.md is an
author derivation; its finite checks remain pending. Neither note supplies
a success law.

The uniform-jump law and the engineered adjacent-index source in that note
collapse to cheap controls. The next experiment must include other large
deleted intervals and nonuniform jumps instead of extrapolating either
collapse. Reuse every retained F337 source attempt, with no outcome-based
selection. Its existing source parameters are the seven laws on N=209,
1333,10807 at the three stated t values.

## Identity checks first

Execute the bounded check design at the end of RETURN_MAP_JUMPS.md. Retain
both source-generation exits for the engineered source. For the exhaustive
small general check, direct visit counts can be updated one full-rotation
step at a time; this avoids recomputing the same prefix from scratch.
Validate the proposed floor-sum expression independently against these
counts. Preserve a named source, resource preflight, timeout, log, JSON,
counts and first anomaly. A passing finite check is not proof promotion.

## Public jump rules on the F337 cells

For each existing unit cell use its m,u,v,alpha,beta and L=u+v. Evaluate
the following deterministic public q choices, keeping duplicate rules as
paired views and marking q=0 as a failed proposal:

    1,
    floor(L/2),
    alpha mod L,
    beta mod L,
    (beta-alpha) mod L,
    N mod L.

The fifth rule has the exact interpretation

    (beta-alpha) mod L = N*u^(-1) mod L,

because alpha*v+beta*u=N and v=L-u. It makes the orbit-index displacement
q*u equal N modulo L. This is a reason to test the rule, not an assumption
that it creates a factor. The q=1 rule is the adjacent-rank control on
accepted endpoints, with a possible wrap difference already covered by t.

For each nonzero q, sample k uniformly on A={0,...,m-1} in the proposed
algorithm and let k'=(k+q*u) mod L. A rejected endpoint is failure. In the
offline diagnostic enumerate all k, evaluate their already known exact
ranks, and count verified proper gcds. Report the exact unconditional
acceptance and factor probabilities with denominator m. Do not condition
away endpoint failures or resample for free. Check the exact K(q) formula.

Keep the uniform nonzero-q control analytically: its acceptance is
(m-1)/(L-1), and its unconditional factor probability is the F337 iid
uniform-rank delta multiplied by m/(L-1). Also retain the direct
uniform-rank gcd mass. These cheap controls need no rank-query algorithm.

For every rule record the separate direct gcd controls on

    t, m, L, u, v, alpha, beta, q, q-m, c, L-c,
    where c=q*u mod L.

Deduplicate control values when charging them. Keep cells with a control
factor in the output and identify that explanation; do not discard them to
invent a favorable conditional input law. Use no offline energy or factor
label to choose a jump rule or a parameter. For small d=L-m also compare
the explicit 2(d+1) menu with its full charged gcd cost. Do not require
that expensive menu to be enumerated for large d.

## Decision and resource limit

Look for a repeatable concentration of useful *coupled* displacements on
cells without a cheaper direct explanation. Record per-input, per-source
and per-rule values, duplicate rules, acceptance losses and setup/count
costs. A post hoc best cell is a pattern candidate, not an algorithmic
source. If no structure appears, retain that scoped finite result and
change the construction rather than repeating larger arbitrary batches.

The exact F337 arrays have at most 5,404 entries. Rebuilding them for this
diagnostic is feasible but is not runtime work of the proposed sampler.
Use one single-threaded job at a time, at most 256 MiB, a 28-second internal
and 30-second external timeout, current resource preflight and an N=209
pilot. Expected total calculation is under 20 seconds; split by N when
needed. A larger-input follow-up should identify the observed structure
and the specific cost or success question that it tests.
