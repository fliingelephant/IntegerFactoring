# Independent reconstruction

Let

\[
f(z)=\frac{z(z-1)}2,
\qquad
r(u)=\frac{u v(u)-N}{M}.
\]

The inverse \(v(u)\) exists uniquely in \([0,M)\) because \(u\) is odd and
therefore invertible modulo \(M=2^k\). It is odd because \(N\) is odd. The
integer \(r(u)\) is well-defined by \(u v(u)\equiv N\pmod M\); it can be
negative.

For cut coordinates \(s,t\in[0,M]\), put

\[
A_s=\mathbf 1_{u<s},\qquad D_t=\mathbf 1_{v(u)<t}.
\]

Expanding the lifted product over the integers gives

\[
q_{st}(u)=r(u)+uD_t+v(u)A_s+M A_sD_t. \tag{1}
\]

This also proves directly that every \(q_{st}(u)\) is an integer. For every
integer \(q\), including a negative one, \(q(q-1)\) is even. Thus every
\(f(q_{st}(u))\) is an integer, and no division by two in
\(\mathbb Z/M\mathbb Z\) is being used.

## The pointwise mixed difference

Fix \(0\leq a\leq b\leq M\) and \(0\leq c\leq d\leq M\). For one odd \(u\),
define

\[
\delta_u=f(q_{bd}(u))-f(q_{ad}(u))-f(q_{bc}(u))+f(q_{ac}(u)).
\]

The cut-indicator differences are

\[
A_b-A_a=\mathbf 1_{a\leq u<b},\qquad
D_d-D_c=\mathbf 1_{c\leq v(u)<d}.
\]

If either indicator difference is zero, the corresponding two states in
the alternating difference coincide, so \(\delta_u=0\) exactly. If both
differences are one, then

\[
A_a=D_c=0,\qquad A_b=D_d=1.
\]

Writing \(r=r(u)\) and \(v=v(u)\), equation (1) then gives

\[
q_{ac}=r,\quad q_{bc}=r+v,\quad q_{ad}=r+u,\quad
q_{bd}=r+u+v+M.
\]

The two elementary integer identities

\[
f(z+M)-f(z)=Mz+\frac{M(M-1)}2
\]

and

\[
f(r+u+v)-f(r+u)-f(r+v)+f(r)=uv
\]

therefore imply

\[
\begin{aligned}
\delta_u
 &=uv+M(r+u+v)+\frac{M(M-1)}2\\
 &\equiv uv-\frac M2\\
 &\equiv N-\frac M2 \pmod M. \tag{2}
\end{aligned}
\]

Here \(M(M-1)/2=M^2/2-M/2\), and \(M^2/2\) is a multiple of \(M\).
Thus (2) is exactly the contribution of a graph point inside the
rectangle, while a graph point outside the rectangle contributes zero.
The value of the possibly negative carry \(r\) cancels modulo \(M\); no
sign assumption was made.

Summing the pointwise mixed differences and using the definition of \(B\)
gives

\[
B(b,d)-B(a,d)-B(b,c)+B(a,c)
\equiv \left(N-\frac M2\right)C\pmod M. \tag{3}
\]

Because \(k\geq2\), \(M/2\) is even. Hence \(N-M/2\) is odd and is a unit
modulo the power of two \(M\). Multiplication of (3) by its inverse recovers
\(C\pmod M\). There are only \(M/2\) odd residues \(u\in[0,M)\), so

\[
0\leq C\leq M/2<M.
\]

Consequently \(C\) itself is the canonical representative of the recovered
residue, including when \(C=M/2\).

## Endpoints and empty intervals

The indicator formulas above remain valid at both endpoints. At cut zero
the indicator is always zero. At cut \(M\) it is always one because both
\(u\) and \(v(u)\) lie in \([0,M)\). Thus intervals ending at \(M\) need no
special correction. If \(a=b\) or \(c=d\), one indicator difference is zero
for every \(u\); both the count and the mixed difference in (3) are zero.
The argument does not require the cut coordinates to be odd.

## Precision that must be retained

The exact division by two means that reducing \(q\) modulo \(M\) before
forming \(f(q)\) loses information. In fact,

\[
f(q+M)-f(q)\equiv -M/2\equiv M/2\pmod M,
\]

whereas

\[
f(q+2M)-f(q)=2Mq+M(2M-1)\equiv0\pmod M.
\]

Therefore \(f(q)\bmod M\) is determined by \(q\bmod 2M\), but in general
it is not determined by \(q\bmod M\). Since

\[
q_{st}=\frac{x_s y_t-N}{M}
\]

is an exact integer quotient, retaining \(x_s y_t-N\pmod{2M^2}\) before
the division determines \(q_{st}\pmod{2M}\). Equivalently, \(N\) may be
reduced modulo \(2M^2\) for the sole purpose of computing a summand modulo
\(M\), but replacing the full \(N\) merely by \(N\bmod M\) is insufficient.
The mathematical definition still uses the exact integer \(N\) and its
possibly negative carries.

The four supplied \(B\)-values need only be residues modulo \(M\). Taking
their alternating sum and multiplying by the modular inverse preserves
(3); no higher precision for the already computed \(B\)-values is needed.

## Conditional cost

Assume the stated uniform deterministic or classical Las Vegas subroutine
for \(B(s,t)\bmod M\). A rectangle count uses the four calls at
\((b,d),(a,d),(b,c),(a,c)\). It then performs modular additions, computes
the inverse of the odd integer \(N-M/2\) modulo \(M\), multiplies, and takes
the canonical representative. These operations have polynomial bit cost.
The resulting exact count also decides emptiness by comparison with zero.
For inputs of \(O(n)\) bits, the expected cost is

\[
4T(n)+\operatorname{poly}(n).
\]

For Las Vegas calls, fresh random bits give an almost-surely terminating,
always-correct result at every requested coordinate. Linearity of
conditional expectation bounds the cost even when later rectangles are
chosen from earlier answers.

Using the declared P237 interface, complete factoring makes \(O(n^2)\)
such rectangle-emptiness queries. Its chosen modulus is the largest power
of two at most one eighth of the current odd cofactor, so every modulus,
cut coordinate, and current cofactor has \(O(n)\) bits relative to the
original input length \(n=\lceil\log_2(N+1)\rceil\). Since \(T\) is a
nondecreasing uniform bound, all calls are bounded by \(T(n)\). The four
\(B\)-calls per rectangle are absorbed into the constant, and the expected
all-input cost is

\[
O\!\left(n^2T(n)+\operatorname{poly}(n)\right).
\]

Small constant inputs are handled directly as allowed by P237. Multiplying
a quasipolynomial \(T(n)\) by \(n^2\) and adding polynomial work remains
quasipolynomial. This conclusion is conditional on both the stated \(B\)
subroutine and P237. The argument constructs neither a fast evaluator for
\(B\) nor an independent factoring algorithm.
