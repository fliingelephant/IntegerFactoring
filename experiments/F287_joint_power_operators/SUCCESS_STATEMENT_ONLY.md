# F287 success-law follow-up: statement-only input

Definitions: N=pq for distinct odd primes, t is a field unit, u=t^(N-1),
F_h=t u^2+h(t-1)u-1. In F_ell, r is the other prime and t^N=t^r.
An admissible local value has t!=1 and t^r!=1. A locally non-Fermat
value additionally has t^r!=t.

Independently verify or refute these claims without reading SUCCESS_LAW.md
or counts.py first.

1. For h=3 every admissible root has a distinct reciprocal root.
The equation is equivalently t=v(3-v)/(3v-1), v=t^r, and no admissible
root is lost by this denominator at odd characteristic. There are no
admissible roots when r equals either 1 or -1 modulo the order of t.
Dividing F_3 by (t-1)t^(r-1) gives
3+sum_{j=-(r-1)}^(r-1)t^j.

2. If p>3 and q=p+2 are both prime, the q-field has no admissible roots.
The p-field admissible root count is
R_p=sum_{x in F_p:x^2+x+2=0}(1+chi_p(x^2-4)).
Each counted root is locally non-Fermat. Under uniform CRT sampling
conditioned on all local admissibility screens and global Fermat gcd 1,
the exact F_3 split probability is R_p/(p-3).
If chi_p(-7)=-1 then R_p=0; if chi_p(-7)=1 and chi_p(2)=-1 then R_p=2.

3. Let A_h=[[0,1,1],[1,0,1],[1,h-1,0]], B=diag(0,1,t).
The characteristic polynomial of A_h is (x+1)(x^2-x-h), with
discriminant (1+4h)(2-h)^2. Whenever this is nonzero,
Cent(A_h) intersects the off-diagonal subspace in span(A_h).
Subject to the squarefree and collision-free hypotheses of F287's triple
compression lemma, the derivative triple has rank4 iff F_h=0, otherwise5.

4. At h=0, A_h has eigenvalues -1,0,1. For odd N its derivative is
the projection onto im ad_(A_h) along its centralizer in every odd field.
F_0=t^(2N-1)-1, and its admissible local root count is
gcd(2r-1,ell-1)-1. Every such root is locally non-Fermat.
At h=1, F_h=(u+1)(tu-1); at h=-1, F_h=(u-1)(tu+1).

5. For N=187, original h=3, t=3, both individual ranks are6, both adjacent
ranks5, and the derivative triple ranks at 11 and17 are4 and5.
The mutual orders are10 and16. Here u=25,F_3=154 modulo187,
gcd(F_3,187)=11 and gcd(u-1,187)=1.

No asymptotic success law, infinitude of prime patterns, or novelty claim
is part of these statements.
