# F201 candidate statement: dyadic AP siblings lose the active factor in their first Euclidean remainder

## Status and scope

Candidate, proof-only, and not yet independently checked.  This packet studies
one exact attempted lift for the P175 reciprocal prefix.  It applies to a
balanced squarefree semiprime and to the full arithmetic-progression cell in
the upper half of the public search interval.  It proves a same-node
output-size and factor-support boundary for the sibling quotient, its first
Euclidean remainder, and fixed public linear combinations.  It is not a
lower bound for implicit modular-product algorithms, adaptive integer
selectors, or factoring.

Assume

\[
N=pq,\qquad p<q<2p,
\qquad B=\lfloor\sqrt N\rfloor,
\]

where \(p,q\) are distinct odd primes.  Put

\[
I_B=\{J\in\mathbb Z:\lceil B/2\rceil<J\leq B\}.
\]

Then \(p\in I_B\), while \(q\notin I_B\) and \(2p\notin I_B\).
Thus \(p\) is the unique member of \(I_B\) having a nontrivial gcd with
\(N\).

Let \(t\geq1\), \(m=2^t\), and let \(a\) be an odd residue modulo \(m\).
The initial full cell is

\[
\widehat S(a,m)=\{J\in I_B:J\equiv a\pmod m\}.
\]

For the exact split below, let

\[
S=\{x_j=c+mj:0\leq j<L\}\subseteq I_B
\]

be any consecutive parent AP containing \(p\).  It may be the full cell
\(\widehat S(a,m)\), or a descendant obtained from it by the public endpoint
cleanup below.  This is the state obtained from a known prefix
\(p^{-1}\bmod 2^t\), after inversion of that odd residue.  Endpoint-cleaned
descendants remain consecutive APs of this form.

## Theorem 1: exact sibling split and public endpoint cleanup

Splitting by the parity of \(j\) gives the two residue-class children modulo
\(2m\).  If \(L=2s+1\), the even child has the extra public endpoint

\[
x_*=x_{2s}=c+2ms.
\]

Then

\[
\gcd(N,x_*)\in\{1,p\}.
\]

The value \(p\) factors \(N\) immediately.  On the branch where the gcd is
one, remove \(x_*\).  If \(L=2s\), no cleanup is needed.  In either
unresolved case, \(s\geq1\) and the remaining children have the interlaced
form

\[
e_i=c+2mi,
\qquad o_i=e_i+m,
\qquad 0\leq i<s,
\]

with

\[
\lceil B/2\rceil<e_i<o_i\leq B,
\qquad e_i<o_i<e_{i+1}\quad(i<s-1).
\]

Put

\[
E=\prod_{i=0}^{s-1}e_i,
\qquad O=\prod_{i=0}^{s-1}o_i.
\]

Exactly one of \(E,O\) is divisible by \(p\), and neither is divisible by
\(q\).  Therefore their gcds with \(N\) are \(p\) for the correct child and
one for the other child.  Evaluating either product modulo \(N\) is thus an
exact next-bit selector; this theorem does not supply that evaluation.

## Theorem 2: quotient one and exact loss of \(p\)-support

The interlacing forces

\[
1<\frac OE\leq\frac{o_{s-1}}{e_0}<2.
\]

The middle inequality is strict when \(s\geq2\) and is equality when
\(s=1\).

Consequently the exact Euclidean division is

\[
\boxed{O=E+D,\qquad D=O-E,\qquad 0<D<E.}
\]

Regardless of which child contains \(p\),

\[
\boxed{p\nmid D.}
\]

The prime \(q\) may divide \(D\) accidentally.  In particular, no claim
that \(\gcd(D,N)=1\) is made.  Reverse division has quotient zero and
remainder \(E\); it does not create a new smaller auxiliary.

The same conclusion applies to the exact rising-factorial or gamma quotient,
because

\[
E=(2m)^s\left(\frac c{2m}\right)_s,
\qquad
O=(2m)^s\left(\frac{c+m}{2m}\right)_s
\]

are identities for these same two integers.  Equivalently,

\[
\frac OE=
\frac{\Gamma((c+m)/(2m)+s)\,\Gamma(c/(2m))}
     {\Gamma((c+m)/(2m))\,\Gamma(c/(2m)+s)}.
\]

These changes of representation do not change the ordered integer pair.
Its ordinary Euclidean quotient is still one, and its first remainder is
still \(D\).

## Theorem 3: the first remainder is explicitly exponential at P175 precision

Expanding the positive product difference gives

\[
D=\prod_{i=0}^{s-1}(e_i+m)-\prod_{i=0}^{s-1}e_i
\geq m\prod_{i=1}^{s-1}e_i
\geq m\left(\frac B2\right)^{s-1}.
\]

The final inequality is strict when \(s\geq2\) and is equality when
\(s=1\).

Hence its binary length satisfies

\[
\operatorname{bitlen}(D)
>\log_2m+(s-1)(\log_2B-1).
\]

For the full cell \(\widehat S(a,m)\), and for every consecutive descendant
produced by repeated parity splitting and this endpoint cleanup,

\[
L=\frac{\lfloor B/2\rfloor}{m}+O(1),
\qquad
s=\frac{B}{4m}+O(1).
\]

At the P175 schedule

\[
t=\left\lfloor\frac{\log_2N}{4}\right\rfloor-L_0(n),
\qquad
L_0(n)=(\log n)^{O(1)},
\qquad n=\lceil\log_2(N+1)\rceil,
\]

where \(L_0\) is a fixed nonnegative integer-valued polylogarithm, and with
\(t\geq1\), one has

\[
s=\Theta\!\left(N^{1/4}2^{L_0(n)}\right)=2^{\Theta(n)}
\]

and therefore \(\operatorname{bitlen}(D)=2^{\Theta(n)}\).  Exact binary
materialization of \(D\) already costs exponential time at the current
node.  This is an output-size statement for explicit materialization.  It
does not exclude an implicit evaluator.

## Theorem 4: linear axes lemma

For public integers \(\alpha,\beta\), put

\[
F_{\alpha,\beta}=\alpha E+\beta O.
\]

The two possible active axes modulo \(p\) obey

\[
\begin{array}{c|c}
p\mid E,\ p\nmid O & p\mid F_{\alpha,\beta}\iff p\mid\beta,\\
p\mid O,\ p\nmid E & p\mid F_{\alpha,\beta}\iff p\mid\alpha.
\end{array}
\]

Thus, if both public coefficients are units modulo \(N\), every such linear
combination loses the guaranteed \(p\)-support in both orientations.  A
linear form guaranteed to retain \(p\)-support on both axes must have both
coefficients divisible by \(p\).  A proper gcd of either coefficient with
\(N\) already factors \(N\).  A coefficient divisible by \(N\) contributes
zero modulo \(N\); if both are divisible by \(N\), the whole form is only
the trivial zero.  As with \(D\), a linear combination may still be
divisible by \(q\) accidentally.

## Exact boundary and surviving opening

Let \(S'\) be \(S\) itself when \(L\) is even, and let it be the parent AP
after removal of the gcd-screened endpoint when \(L\) is odd.  The
product-tree identity

\[
\prod_{J\in S'}J
=E\,O
\]

after endpoint cleanup gives a genuine unique-child chain if a QP procedure
can select the factor-bearing child.  There are only \(O(n)\) bit lifts.
At the lift level, such a selector has a recurrence of the form

\[
U(t)\leq U(t+1)+\operatorname{QP}(n)
\]

through only \(O(n)\) stages.  Likewise, a unique recursive integer child
may obey

\[
T(n)\leq T(n-1)+\operatorname{QP}(n),
\]

and fixed-ratio contraction is not needed.

This packet closes only the proposed handoff through the ordinary sibling
quotient, its first Euclidean remainder, reverse division, explicit
materialization of that remainder, and fixed linear combinations.  A QP
modular AP-product evaluator, a nonlocal carry or floor, a different
one-child integer auxiliary, and an adaptive nonlinear selector remain open.
