# Public square-input feedback

**Family:** route:F31

Status: root-designed discovery experiment. No favorable distribution or
quasipolynomial bound is assumed.

## Question and prior scope

Can a public coordinate from a short F326 path produce a better next square
input than an independent square rescaling, after all failed attempts and
proposal work are charged?

F328 always restarts the same arithmetic path at rank L for a fresh random
square. P02 and F326/RABIN_INPUT_SHAPING.md permit adaptive public changes
a -> a*c^2 while a public product tracks the multipliers. P52's exact
Newton obstruction concerns a fixed rational iteration. The present proposal
uses sign-selected, ranked path coordinates and changes the auxiliary input;
it is not that iteration and is not a certified jump on its old path.

## Exact public/private boundary

Draw the initial hidden r uniformly from 1,...,N-1; accept any proper gcd.
Otherwise a_0=r^2 is a unit square. A controller receives only N,a_0 and
independent coins. It keeps public a and C, initially a=a_0 and C=1, with
a=a_0*C^2 mod N. A public unit multiplier c updates these to b=a*c^2 and
C_new=C*c modulo N. If y is a verified root of the current a, return
y*C^(-1) modulo N as a verified root of a_0. Only the outer driver compares
this root with the private r. No private root enters intermediate decisions.

At every round, check whether the current a is an ordinary integer square.
A public integer square root is then a valid modular root. Next run at most
B=8 calls of the F326 rank-L reflection path. Stop on a verified factor or
root. Retain distinct absolute values of visited unit coordinates other than
+1 and -1 as a public multiplier pool. Thus opposite coordinates do not
duplicate the same square proposal. Coordinate zero is never a multiplier.

If no output is obtained, form at most four proposed unit multipliers according
to the policy below. For each b=a*c^2, find the nearest ordinary integer square
k^2 (choose the smaller k on a tie). The score is |b-k^2|. Check gcd(b-k^2,N);
a proper value is a verified factor. If b=k^2, return k*(C*c)^(-1) as a
verified root of a_0 for outer decoding. A valid root whose comparison is
trivial ends that attempt with failure.

If every proposal fails, update to the proposed b with the smallest score and
its associated c. Charge every proposal, including unselected ones. Use at
most R=16 rounds; retain the cap failure. Equal scores are resolved by proposal
order. Repeated a values need not be stored or forbidden: they remain charged
observations of the actual feedback policy.

## Policies and controls

1. `path`: sample without replacement up to four distinct multipliers from the
   visited unit-coordinate pool. If it is empty, end the attempt as a retained
   failure. Continue at the smallest-score proposal.
2. `uniform`: propose four independent uniform nonzero residues. A proper
   generation gcd is a factor; otherwise use the resulting unit as c. Continue
   at the smallest-score proposal. Include rejection bits and all gcds.
3. `last`: use only the absolute value of the last nontrivial visited unit
   coordinate as c. This
   removes proposal selection while preserving the path-derived feedback.

The uniform-multiplier control has a useful exact property: for each fixed
current unit square a, a*c^2 is uniform among unit squares when c is a uniform
unit. Thus any advantage from the path policy requires an arithmetic
correlation absent from independent square proposals. The intervening path
probe on a selected state still matters, so no whole-policy equivalence or
lower bound is asserted for the uniform control.

## Finite plan and accounting

Use the retained F328 moduli at 20, 28, 36, and 44 bits, with two moduli per
scale and 32 independent outer trials per modulus and policy. All policies
share each trial's initial r for a paired comparison but receive independent
policy coins. The solver/controller never receives the initial or current r.
Offline factors are used only for exact validation and labels.

Preserve the full short state/proposal history, ordinary-square hits, direct
path factors, proposal-screen factors, multiplier-generation factors, failed
root decodes, empty pools, round censors, and every attempt's cost. Count F,
floor-sum, rank/select, gcd, inversion, multiplication, square-root, proposal,
and random-bit operations; also record charged wall time and peak memory.
Report per-N cost/success ratios only when observed successes exist. No fit
or finite zero is an asymptotic conclusion.

First check the public/private root invariant exactly on a few tiny moduli
and run a two-trial pilot. Compare unchanged path prefixes against F328's
arithmetic walk. One process/thread, 512 MiB ceiling, a 28-second internal
alarm and 30-second external timeout per fresh batch. Inspect load, memory,
and processes before running, and coordinate with other numerical work.
If the pilot exceeds the estimate, reduce batch size rather than discarding
unfinished trials. Retain named source, resource record, status, log, output,
and manifest files. This is a one-off mathematical experiment.
