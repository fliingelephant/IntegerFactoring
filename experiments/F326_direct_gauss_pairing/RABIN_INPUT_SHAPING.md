# Adaptive square inputs retain the hidden-root reduction

**Family:** route:F31

Status: root-derived extension of P02 for choosing auxiliary inputs. No
speedup, independent reconstruction, or novelty claim is made here.

Uniformity over auxiliary squares is sufficient, but it is not necessary.
The useful invariant is uniformity of the private CRT signs after conditioning
on the entire public transcript.

Let odd N have s>=2 distinct prime divisors, with arbitrary exponents. Draw a
private uniform unit r, and publish a_0=r^2 modulo N. A public adaptive
procedure uses only N, a_0, and coins independent of r. It may select units
c_t, replace

    a_(t+1) = a_t*c_t^2 mod N,

and stop or fail based on this transcript. A proposed nonunit c_t is checked:
a proper gcd is an immediate factor, while zero modulo N may be rejected.
The outer procedure privately retains

    C_t = product_(j<t) c_j mod N,    r_t = C_t*r mod N.

It never uses r_t to select parameters or to decide when to call the root
routine. That routine may receive the full public transcript, not just a_t.
Its additional coins are independent of r. Verify every returned root y of
a_t and try gcd(y-r_t,N).

Conditional on a_0 and all public coins, r is uniform among the 2^s roots
of a_0. The entire adaptive transcript, including a stopping or failure
decision, is the same for all those roots. Multiplication by the public
unit C_t is a bijection between those roots and all roots of a_t: its inverse
is multiplication by C_t^(-1). Thus r_t is still uniform among all roots of
a_t after conditioning on the transcript and any valid returned y. Exactly
two CRT sign choices give an improper gcd. The proper-factor probability is
therefore still

    1 - 2^(1-s) >= 1/2,

conditional on a valid root output. This remains true when the distribution
of a_t is highly nonuniform or selected by a public acceptance filter.

For example, any public odd positive exponent E gives a_t -> a_t^E by
taking c_t=a_t^((E-1)/2). More general choices c_t=h(a_t,transcript) are
permitted whenever the unit condition is checked. These examples describe
legal input transformations; they do not establish useful concentration or
a cheap root routine. Even exponents do not inherit this particular argument.

If one complete shaped attempt has expected bit cost tau and valid factor
or root probability delta, actual factor probability is at least delta/2.
Independent restarts cost at most 2*tau/delta in expectation. Charge failed
filters, transformations, private root tracking, all calls, and verification
inside tau. No cheap uniform sampler for the final input distribution and
no fast routine for every auxiliary a are required. A uniform quasipolynomial
bound on this actual cost/success ratio, for every fixed N, is still missing.
