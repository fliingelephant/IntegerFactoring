# F333 partial FacRoot mixture

**Family:** route:F31

Status: root-derived conditional reduction verified by fresh independent
reconstruction and root comparison. No partial FacRoot procedure satisfying
the required cost/success contract is supplied.

## Result

Fix an odd \(N\) with \(s\geq2\) distinct prime divisors. Let \(U\) be its
unit group, \(J\) the Jacobi-positive units, and \(S\) the unit squares.
A single public randomized procedure \(A\) receives only \(N,a\) and the
same independent coin law in every mode. It may return a verified divisor,
a verified root of \(a\), or failure.

For a bounded call on uniform \(a\in J\), let \(f_J,r_J\) be its disjoint
factor and root probabilities and put \(\delta_J=f_J+r_J\). Since
\[
 \rho=\frac{|S|}{|J|}\leq2^{1-s}
\]
and a root output is possible only on \(S\), mode invisibility gives
\(r_J=\rho r_S\). A fair mixture of a \(J\)-mode attempt accepting only
factors and a secret-square attempt using P02 therefore factors with
probability at least \(\delta_J/2\). Root privacy and independent coins,
not mode secrecy alone, supply P02's conditional CRT-sign law.

Exact uniform nonzero-residue sampling, gcd screening, and Jacobi rejection
implement both modes without factoring \(N\). Every generation factor is an
immediate success. The expected generation bit and fair-bit costs are
polynomial.

Suppose for every such fixed \(N\), with input length \(n\),
\[
 \tau_J(N)\geq1,\qquad \delta_J(N)>0,\qquad
 \frac{\tau_J(N)}{\delta_J(N)}\leq Q(n),
\]
where \(\tau_J\) is the verified mean cost on uniform \(J\) and \(Q\) is a
uniform quasipolynomial envelope. Two uncapped retry engines suffice. One
uses \(J\) mode; the other uses secret-square mode. Store their machine
states and alternate one bit operation of each. If \(g(n)\) bounds expected
generation and outer verification, then
\[
 \mathbb E T_{\rm dovetail}
 \leq\frac{6(g(n)+\tau_J(N))}{\delta_J(N)}
\]
up to constant machine-simulation overhead. This requires no evaluation of
\(Q\), no separate mean-cost bound on \(S\), and no cost/success
independence inside one attempt. Either engine may have zero success
probability.

There is also a capped construction. With a cap
\(B=\lceil2Q(n)\rceil\), Markov's inequality retains \(J\)-valid-output
probability at least \(\delta_J/2\), so the mixed attempt factors with
probability at least \(\delta_J/4\). Its retry work after \(B\) is available
is \(O(Q^2+\operatorname{poly}(n)Q)\). Computing a literal \(Q(n)\) adds
its evaluation cost \(E_Q(n)\). Alternatively, an efficiently evaluable
quasipolynomial majorant \(R\geq Q\) gives
\(O(R^2+\operatorname{poly}(n)R)\). Mere computability of \(Q\) does not
by itself bound this setup cost.

Primality testing, removal of two-powers, exact perfect-power reduction,
verified splitting, and recursive factoring give the all-input result under
the stated uniform contract. The contract must hold pointwise for every
recursive composite input; it is not an average over input integers.

## Scope

The theorem changes the sufficient source contract from a promise on secret
squares to an average cost/success contract on all Jacobi-positive units.
It does not construct \(A\), establish the contract for F326 or any feedback
policy, or make an external novelty claim.

Evidence:
STATEMENT_ONLY.md,
PROOF.md, and
RECONSTRUCTION.md.

Statement SHA-256:
0cc27150004a4d59380cdf50f5a413751ca997c473595268df0d0e43ec706239.
Proof SHA-256:
a9d6a0363a03ee2a9254aa99548987c5e27a862c3a48aba7fef6fb8b0a8f8961.
Reconstruction SHA-256:
63d19572f130b697a6df47e52103c569bd06c736a057b6636c715b2f12a85cd2.
