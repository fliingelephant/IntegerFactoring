# F189 candidate — segment-Jacobi zero compression

## Status and scope

This is a frozen proof-only candidate awaiting hostile audit. It supplies no
quasipolynomial segment evaluator and no unconditional factoring algorithm.
Its positive statement is conditional: a uniform quasipolynomial oracle for
the segment-Jacobi zero predicate would give a one-child quasipolynomial
splitter for the affine balanced-semiprime source.

The totalized floor identity, the zero reduction, and the conditional binary
isolation theorem apply to every odd modulus. The exact affine-source
probability and the sharpened \(p+q-1\) Fourier recurrence apply only to a
squarefree semiprime \(N=pq\). Every recurrence and automaton conclusion is a
lower bound only in its explicitly named representation model.

The affine source below uses the numerical \(T\)-scale of P34 but is not
P34's original independent Boolean subset-sum source. No evaluator for the
original \(Q_K\) is claimed.

## Segment zero and the totalized Gauss correction

Let \(N>1\) be odd, let

\[
 n=\lceil\log _2(N+1)\rceil,
 \qquad
 \chi_N(x)=\left(\frac{x}{N}\right),
\]

and, for positive integers \(a,L\), define

\[
 J_N(a,L)=\prod_{t=0}^{L-1}\chi_N(a+t).
 \tag{1}
\]

For every integer \(x\),

\[
 z_N(x):=1-\chi_N(x)^2
       =\mathbf 1_{\gcd(x,N)>1}.
 \tag{2}
\]

Therefore

\[
 J_N(a,L)=0
 \quad\Longleftrightarrow\quad
 \sum_{t=0}^{L-1}z_N(a+t)>0.
 \tag{3}
\]

For positive odd \(x\), put

\[
 F(x,N)=\sum_{i=1}^{(N-1)/2}
          \left\lfloor\frac{ix}{N}\right\rfloor.
 \tag{4}
\]

Then, without a coprimality assumption,

\[
 \boxed{
 F(x,N)+F(N,x)
 =\frac{(x-1)(N-1)}4+
  \frac{\gcd(x,N)-1}{2}.}
 \tag{5}
\]

Both terms on the right are integers because \(x,N\), and
\(\gcd(x,N)\) are odd. When \(\gcd(x,N)=1\), Eisenstein's lemma gives

\[
 \chi_N(x)=(-1)^{F(x,N)}.
 \tag{6}
\]

When \(\gcd(x,N)>1\), the right side of (6) remains a sign and cannot equal
the zero Jacobi value. Equation (5) identifies the missing information
exactly: it is \((\gcd(x,N)-1)/2\).

For any finite multiset \(\mathcal A\) of positive odd integers, define

\[
 G_N(\mathcal A)=
 \sum_{x\in\mathcal A}(\gcd(x,N)-1).
 \tag{7}
\]

Summing (5) gives the exact reduction

\[
 \boxed{
 G_N(\mathcal A)
 =2\sum_{x\in\mathcal A}\bigl(F(x,N)+F(N,x)\bigr)
 -\frac{N-1}{2}\sum_{x\in\mathcal A}(x-1).}
 \tag{8}
\]

Thus \(G_N(\mathcal A)=0\) exactly when every member is a unit modulo \(N\).
For a general segment, powers of two can be removed because \(N\) is odd:

\[
 \gcd(2^ju,N)=\gcd(u,N).
 \tag{9}
\]

When \(1\le a<N\) and \(1\le L<N\), grouping the segment by
\(j=v_2(a+t)\) gives \(O(n)\) odd arithmetic subsegments. Hence (8) is an
exact reduction of the full segment-zero predicate to a short-interval
hidden-divisor hit count. It is not an algorithm for evaluating that count.

## Conditional one-child isolation theorem

Assume a uniform oracle \(\mathcal Z\) that, on every odd \(N>1\),
\(1\le a<2N\), and \(1\le L<N\), decides whether \(J_N(a,L)=0\) in

\[
 Q(n)=2^{(\log n)^{O(1)}}
 \tag{10}
\]

bit operations.

Given a segment known to have zero product and containing no multiple of
\(N\), query only its left half. Descend to the left half if that answer is
zero and to the right half otherwise. The retained half is again known to
have zero product. After

\[
 \lceil\log_2 L\rceil
 \tag{11}
\]

oracle calls, the interval is one integer \(x\). Then

\[
 1<\gcd(x,N)<N,
 \tag{12}
\]

so the gcd is a proper factor. This uses one oracle child per level, not both
children. The total bit cost is \(nQ(n)\), hence quasipolynomial.

A multiple of \(N\) is a public but unhelpful zero. It must be excluded from
the known-zero premise or rejected and resampled. An interval of length less
than \(N\) contains at most one such integer.

## Exact affine-source probability on the P34 scale

Now assume

\[
 N=pq,
 \qquad 53\le p<q<2p,
 \tag{13}
\]

with distinct odd primes. Put

\[
 K=\left\lfloor\log_2\lfloor\sqrt N\rfloor\right\rfloor-3,
 \qquad T=2^K.
 \tag{14}
\]

After the gcd screens certify that two sampled residues \(U,V\) are units,
set

\[
 a=UV^{-1}\pmod N.
 \tag{15}
\]

The affine pool \(U+tV\), \(0\le t<T\), has the same zero positions as
\(a+t\), and conditional on the unit branch, \(a\) is uniform in
\((\mathbb Z/N\mathbb Z)^\times\).

Since \(T<p<q\), put

\[
 \alpha_p=\frac{T-1}{p-1},
 \qquad
 \alpha_q=\frac{T-1}{q-1}.
 \tag{16}
\]

The two local root positions are independent and uniform in
\(\{1,\ldots,p-1\}\) and \(\{1,\ldots,q-1\}\). Therefore the exact probability
that the segment product is zero is

\[
 \boxed{
 \rho_0=\alpha_p+\alpha_q-\alpha_p\alpha_q.}
 \tag{17}
\]

The sole unhelpful case has the two roots at the same position, equivalently
\(a+t\equiv0\pmod N\), and has exact probability

\[
 \boxed{
 \beta=\frac{T-1}{(p-1)(q-1)}.}
 \tag{18}
\]

Hence the exact useful one-trial probability, conditional on the unit
branch, is

\[
 \boxed{
 \rho_{\rm use}
 =\alpha_p+\alpha_q-\alpha_p\alpha_q
  -\frac{T-1}{(p-1)(q-1)}.}
 \tag{19}
\]

Moreover \(\rho_{\rm use}>1/40\). Thus the oracle, the one-child isolation,
and restart after the public global zero give an expected-constant-trial QP
splitter on this promise.

## Exact named-model obstructions

Let

\[
 m=\operatorname{rad}(N).
 \tag{20}
\]

The sequence \(z_N(x)\) in (2) has least period \(m\). Its discrete Fourier
transform over \(\mathbb Z/m\mathbb Z\) is nonzero at every one of the \(m\)
frequencies. Consequently its minimal complex constant-coefficient linear
recurrence has exact order \(m\), with characteristic polynomial

\[
 X^m-1.
 \tag{21}
\]

For a squarefree semiprime \(N=pq\), define the globally corrected count

\[
 c_N(x)=z_N(x)+\mathbf 1_{N\mid x}
       =\mathbf 1_{p\mid x}+\mathbf 1_{q\mid x}.
 \tag{22}
\]

Its Fourier support has exact size \(p+q-1\), and its minimal complex
constant-coefficient recurrence has exact order \(p+q-1\), with

\[
 \boxed{
 \operatorname{lcm}(X^p-1,X^q-1)
 =\frac{(X^p-1)(X^q-1)}{X-1}.}
 \tag{23}
\]

The binary language

\[
 \{w\in\{0,1\}^*: \gcd(\operatorname{val}_2(w),N)>1\}
 \tag{24}
\]

with leading zeros allowed has a minimal deterministic finite automaton with
exactly \(m\) states. Thus explicit periodic tables, constant-coefficient
linear recurrences, exact Fourier-mode lists, and explicit finite-state
automatic representations require \(2^{\Theta(n)}\) size on balanced
squarefree semiprimes.

## Hidden-base carry interpretation

For \(a,L\ge1\), let

\[
 R_{a,L}=\prod_{t=0}^{L-1}(a+t)
 =L!\binom{a+L-1}{L}.
 \tag{25}
\]

If \(r\mid N\) is prime and \(L<r\), then \(L!\) is an \(r\)-adic unit and

\[
 r\mid R_{a,L}
 \quad\Longleftrightarrow\quad
 r\mid\binom{a+L-1}{L}.
 \tag{26}
\]

By Kummer's theorem, this is equivalent to a carry when adding \(L\) and
\(a-1\) in base \(r\). Since \(L<r\), it is equivalent to the low-digit
condition

\[
 ((a-1)\bmod r)+L\ge r.
 \tag{27}
\]

Thus factorial and binomial identities recast the zero as a carry in an
unknown prime base. They do not compute it without the hidden factor or the
shifted-factorial residue.

## Exact boundary

F189 proves no general time lower bound. In particular, the recurrence and
DFA sizes do not constrain nonlinear arithmetic algorithms, algorithms with
integer registers, implicit global determinants, sparse nonlinear state,
random-input detectors, or a new gcd-only observable. Equation (8) is an
exact target reduction, not evidence that its right side is hard.

The unresolved positive problem is a uniform QP evaluation, or a sufficiently
accurate certified approximation, of the short-interval quantity

\[
 \sum_{t=0}^{L-1}(\gcd(a+t,N)-1)
 \tag{28}
\]

without scanning the interval or evaluating \(R_{a,L}\bmod N\). Such a
construction would be materially different from full shifted-factorial
evaluation and would activate the conditional theorem above.

On the promise \(p<q<2p\), every positive summand in (28) is at least
\(p-1>\sqrt{N/2}-1\). Therefore a certified additive approximation with
error less than

\[
 \frac{\sqrt{N/2}-1}{2}
 \tag{29}
\]

would already distinguish zero from nonzero by a public threshold. No such
QP approximation is supplied here.
