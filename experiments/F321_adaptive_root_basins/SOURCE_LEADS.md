# Focused primary-source check, 2026-09-07

The adaptive output-selected-root process and its drift questions were
specified before this search. No external novelty claim is made.

For the primality dependency in the conditional radical-shadow reduction,
the [published AKS abstract](https://annals.math.princeton.edu/2004/160-2/p12)
states unconditional deterministic polynomial-time primality testing. The
full AKS proof was not rechecked here. Exact perfect-power testing can be
implemented directly by testing integer e-th roots for 2<=e<=bitlength(N).

[Brent's original publication page](https://maths-people.anu.edu.au/~brent/pub/pub051.html)
identifies the established cycle-finding improvement to Pollard rho. Only
its abstract and author comments were inspected. F321's control uses Floyd
iteration and measures its own finite costs; it does not claim to outperform
an optimized Brent implementation. No heuristic average rho bound is used
as an all-input theorem in this packet.

A separate lead is [Jerábek, Integer factoring and modular square roots](https://arxiv.org/abs/1207.5220),
v3 (2015), published in JCSS (2016). The inspected abstract gives randomized
polynomial reductions of general factoring to particular PPA and WEAKPIGEON
search problems. Their structured witnesses could be investigated directly;
the abstract gives no quasipolynomial solver. Full constructions have not
been read or compared with the repository yet, and this paper is not a
dependency of any result in F321.

The limited search did not establish a literature classification of the
adaptive process. Missing a matching source is not evidence of novelty.
