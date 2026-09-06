# F249 — shifted binomial threshold and the same factorial gate

## Status and scope

This is a proof-only candidate.  It gives an exact shifted-binomial
factor oracle on the balanced beta-two branch and identifies the unique
singular denominator in its first-order recurrence.  It does not evaluate
the remote coefficient in numerical quasipolynomial time, and it is not a
factoring algorithm.

Let

\[
N=pq,\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes.  Put

\[
B=\lfloor\sqrt N\rfloor,\qquad
H=\left\lfloor\frac B2\right\rfloor,\qquad
s=B-p.
\]

For a positive integer \(r\) and \(1\le c\le H\), define

\[
C_{r,c}=\binom{rN+c-1}{B}.
\]

When a gcd conclusion uses \(r\), first screen \(\gcd(r,N)\).  The
factor-free branch has \(\gcd(r,N)=1\).

## Theorem 1 — exact shifted threshold law

The public ranges satisfy

\[
B\ge3,\qquad 0\le s<H<p<q,\qquad B<q.
\]

For every positive \(r\) and every \(1\le c\le H\), with the convention
\(\binom uv=0\) for \(0\le u<v\),

\[
\boxed{
C_{r,c}\equiv rq\binom{c-1}{s}\pmod N.}
\]

Consequently, on the factor-free branch for \(r\),

\[
\boxed{
\gcd(N,C_{r,c})=
\begin{cases}
N,&1\le c\le s,\\
q,&s<c\le H.
\end{cases}}
\]

In particular, the single public endpoint always gives

\[
\boxed{\gcd(N,C_{1,H})=q.}
\]

The promise function that outputs this gcd is therefore polynomial-time
equivalent to factoring the promised input.  Computing
\(C_{1,H}\bmod N\) is a sufficient oracle for that function.  The theorem
does not provide such a coefficient evaluator.  It also does not claim that
factoring alone fast-forwards the full remote coefficient residue.

## Theorem 2 — exact Las Vegas accounting

If \(c\) is uniform in \(\{1,\ldots,H\}\), then

\[
\Pr\bigl(\gcd(N,C_{r,c})=q\bigr)
=\frac{H-s}{H}\ge\frac13.
\]

Thus an oracle that evaluates the coefficient modulo \(N\) at sampled
shifts gives a Las Vegas factorer with expected at most three calls.  This
randomization is unnecessary if the same oracle accepts the endpoint
\(c=H\), which succeeds deterministically.

The exceptional floor case is explicit.  If \(s=0\), then \(B=p\), so
\(\gcd(N,B)=p\) already factors \(N\).  In this case every permitted
shift has gcd \(q\).  No input in the stated domain has \(B<3\).

## Theorem 3 — the unique recurrence singularity

The exact recurrence is

\[
\boxed{
(rN+c-B)C_{r,c+1}=(rN+c)C_{r,c}.}
\]

If \(s\ge1\), then for \(1\le c\le H-1\),

\[
\gcd(N,rN+c)=1,
\]

and

\[
\boxed{
\gcd(N,rN+c-B)=
\begin{cases}
p,&c=s,\\
1,&c\ne s.
\end{cases}}
\]

Thus the threshold jump occurs at the unique hidden nonunit denominator.
If \(s=0\), the singular edge is the preceding edge \(c=0\), outside the
sampled interval, and the elementary gcd \(\gcd(N,B)\) has already
factored the input.

## Theorem 4 — the endpoint is the complementary central-binomial gate

Put

\[
K_B=\binom BH.
\]

Then

\[
\boxed{\gcd(N,K_B)=p,}
\qquad
\boxed{
\gcd(N,C_{1,H})=\frac{N}{\gcd(N,K_B)}=q.}
\]

Indeed, \(H!\) is a unit modulo \(N\), while the numerator interval of
\(K_B\) contains \(p\) exactly once and contains no multiple of \(q\).
The shifted endpoint is therefore algebraically no stronger than the
central-binomial or upper-half interval-product gate already isolated by
F197 and F201.  It returns the complementary factor.

For odd \(B\), the interval \(\{H+1,\ldots,B\}\) has one more public unit
than the standard numerator interval of \(\binom BH\); both have the same
gcd with \(N\).  This distinction matters for exact identities but not for
the factor gate.

## Theorem 5 — recurrence fast-forward is the upper-half product gate

Assume \(s\ge1\).  The product of all recurrence denominators before the
endpoint is

\[
D_r=\prod_{c=1}^{H-1}(rN+c-B).
\]

It obeys

\[
D_r\equiv(-1)^{H-1}
\prod_{j=B-H+1}^{B-1}j\pmod N
\]

and

\[
\boxed{\gcd(N,D_r)=p.}
\]

The displayed public interval contains \(p\) exactly once and contains no
multiple of \(q\).  Hence an explicit denominator-product computation has
reached the ordinary interval/factorial product factor gate before it can
invert the recurrence.

There is the same cancellation in the defining binomial quotient.  Write

\[
B!=pU,
\qquad
P_{r,c}=\prod_{j=1}^{B}(rN+c-j).
\]

Here \(U\) is a unit modulo \(N\), and the factor with \(j=c\) is \(rN\).
After removing that factor, the remaining product is a unit modulo \(N\)
exactly when \(c>s\); it has an additional \(p\)-factor exactly when
\(c\le s\).  The passage from

\[
B!\,C_{r,c}=P_{r,c}
\]

to \(C_{r,c}\bmod N\) therefore requires cancellation of the hidden
\(p\)-factor.  Materializing \(B!\bmod N\), \(D_r\bmod N\), or the
corresponding upper-half interval product exposes \(p\) by a gcd.

## Theorem 6 — random top multipliers add no new threshold coordinate

For every positive \(r\),

\[
C_{r,c}\equiv rC_{1,c}\pmod N.
\]

On the factor-free branch, changing \(r\) only multiplies the local
factor-bearing residue by a public unit.  It neither moves the threshold
\(s\) nor changes the unique singular recurrence edge.

The analogous beta-two carry family has the same rank-one boundary.  Put

\[
A_r=(-1)^B\binom{rN-1}{B},\qquad
h_r=\frac{A_r-(1-rq)}N,
\]

and

\[
z_{r,t}=N^{-1}(A_r-1)\pmod {2^t}.
\]

Then

\[
h_r-z_{r,t}\equiv rp^{-1}\pmod {2^t},
\]

so

\[
\boxed{h_r-rh_1\equiv z_{r,t}-rz_{1,t}\pmod {2^t}.}
\]

The right side is public.  Multiple top multipliers therefore give affine
copies of the same hidden reciprocal coordinate.  They can help only if an
integer carry evaluator or sampler supplies a proved nonuniform bias toward
the actual carries.

## Exact evaluation boundary

The following literal routes do not give numerical-QP evaluation:

- the recurrence crosses the factor-bearing denominator product above;
- the Vandermonde/Newton formula has \(H+1=2^{\Theta(\log N)}\) literal
  terms at the endpoint;
- standard baby-step/giant-step algorithms for this order-one holonomic
  product use \(H^{1/2+o(1)}=N^{1/4+o(1)}\) ring work;
- power-of-two binomial routines compute the coefficient in a factor-free
  auxiliary ring, not modulo \(N\), and do not perform the hidden
  cancellation.

The algebraic-series presentation does not currently change this boundary.
For \(B=2H\),

\[
K_B=[x^H](1-4x)^{-1/2}.
\]

For \(B=2H+1\), it differs from this coefficient by
\((2H+1)/(H+1)\); after the elementary \(\gcd(N,B)\) screen, this is a
public unit modulo \(N\).  Fast remote-coefficient algorithms for algebraic
series over a finite prime field use its known prime characteristic and
have preprocessing polynomial or quasi-linear in that characteristic.
Here the two useful characteristics are the hidden primes of size
\(2^{\Theta(\log N)}\), while \(\mathbb Z/N\mathbb Z\) is not a prime
field and has no public prime-field Cartier radix.  Thus the known
finite-field method is neither directly applicable nor numerical QP here.

These are boundaries for named representations, not a lower bound against a
different succinct evaluator.  The surviving target is a genuinely new
numerical-QP evaluator for the central coefficient, shifted coefficient, or
their hidden divisibility that does not first materialize a factor-bearing
factorial or interval product.
