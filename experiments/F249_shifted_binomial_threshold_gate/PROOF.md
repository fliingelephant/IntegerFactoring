# Proof of F249

## 1. Ranges and floor endpoints

Since \(p<q<2p\),

\[
p^2<N<2p^2.
\]

Therefore

\[
p\le B<\sqrt2\,p<2p.
\]

Also \(B<q\), because \(\sqrt N<q\).  It follows that

\[
0\le s=B-p<p,
\qquad
H<p.
\]

We next prove the strict endpoint \(s<H\).  From \(B<\sqrt2 p\),

\[
p>\frac B{\sqrt2}.
\]

For every integer \(B\ge3\),

\[
\frac B{\sqrt2}>\left\lceil\frac B2\right\rceil.
\]

For even \(B\) this is immediate.  For \(B=2k+1\ge3\), squaring reduces
it to \(2k^2>1\).  Hence

\[
p>\left\lceil\frac B2\right\rceil
\]

and

\[
s=B-p
<B-\left\lceil\frac B2\right\rceil
=\left\lfloor\frac B2\right\rfloor=H.
\]

The smallest distinct odd primes in the promise are \(3,5\), so
\(N\ge15\) and \(B\ge3\).  Thus there is no missing \(B<3\) case and
\(H\ge1\).

## 2. Lucas calculation

Fix \(r\ge1\) and \(1\le c\le H\).  Since \(c-1<B<q\), Lucas's theorem
modulo \(q\) gives

\[
\binom{rN+c-1}{B}
=\binom{q(rp)+c-1}{B}
\equiv\binom{c-1}{B}=0\pmod q.
\]

Modulo \(p\), use \(B=p+s\), with \(0\le s<p\), and \(c-1<p\).
Lucas's theorem gives

\[
\binom{rN+c-1}{B}
=\binom{p(rq)+c-1}{p+s}
\equiv
\binom{c-1}{s}\binom{rq}{1}
=rq\binom{c-1}{s}
\pmod p.
\]

The integer \(rq\binom{c-1}{s}\) is zero modulo \(q\) and has the same
residue modulo \(p\).  CRT proves

\[
C_{r,c}\equiv rq\binom{c-1}{s}\pmod N.
\]

If \(c\le s\), the binomial on the right is zero.  If \(c>s\), its upper
index satisfies

\[
s\le c-1<p.
\]

Its numerator and denominator factorials are units modulo \(p\), so it is
nonzero modulo \(p\).  After the initial gcd screen for \(r\), both \(r\)
and \(q\) are also units modulo \(p\).  Hence \(C_{r,c}\) is zero modulo
\(q\) and nonzero modulo \(p\).  This proves the gcd dichotomy and the
endpoint claim, because \(H>s\).

The function \(N\mapsto\gcd(N,C_{1,H})\) returns \(q\).  It factors the
promise input, and a factorization computes its output by selecting the
larger factor.  This proves the stated promise-function equivalence.  A
coefficient residue evaluator is a sufficient implementation because one
gcd recovers the same output.  The converse statement concerns the gcd
function only; it is not a claimed fast algorithm for the full residue.

## 3. Exact success probability

There are exactly \(H-s\) integers in \(\{1,\ldots,H\}\) that are larger
than \(s\).  This gives the exact probability.

For the constant lower bound, \(\sqrt2<3/2\) and \(B<\sqrt2p\) imply

\[
p>\frac{2B}{3},
\qquad
s=B-p<\frac B3.
\]

Thus \(3s<B\).  If \(B=2H\), then \(3s<2H\).  If \(B=2H+1\), integrality
gives \(3s\le2H\).  In both cases \(s\le2H/3\), and hence

\[
\frac{H-s}{H}\ge\frac13.
\]

Independent repetition has geometric mean at most three.  The fixed choice
\(c=H\) has success probability one if endpoint evaluation is available.

If \(s=0\), then \(B=p\).  Since \(B<q\),

\[
\gcd(N,B)=p.
\]

The threshold law also says every \(1\le c\le H\) has coefficient gcd
\(q\).  This treats the full exceptional case.

## 4. The recurrence and its singular edge

The ordinary adjacent-binomial identity gives

\[
\frac{C_{r,c+1}}{C_{r,c}}
=\frac{rN+c}{rN+c-B}.
\]

Cross multiplication proves the exact recurrence without any modular
division.

For \(1\le c\le H-1\), one has \(c<p\), so

\[
\gcd(N,rN+c)=\gcd(N,c)=1.
\]

Also

\[
\gcd(N,rN+c-B)=\gcd(N,B-c).
\]

The integer \(B-c\) lies strictly between zero and \(B<q\), and it is
smaller than \(2p\).  It has a nontrivial gcd with \(N\) exactly when it
equals \(p\), which is exactly the condition \(c=B-p=s\).  If \(s\ge1\),
then \(s<H\) places this edge inside \(1,\ldots,H-1\).  At that edge,

\[
rN+s-B=rN-p=p(rq-1),
\]

which has gcd exactly \(p\) with \(N\).  This proves uniqueness.

If \(s=0\), this equality occurs at \(c=0\), and the preceding section's
gcd with \(B\) already exits.

## 5. The central-binomial collapse

The denominator \(H!\) is a unit modulo \(N\), because \(H<p<q\).  The
standard numerator interval for

\[
K_B=\binom BH
\]

is

\[
B-H+1,\ldots,B.
\]

It contains \(p=B-s\): the lower-end condition is \(s\le H-1\), which
follows from \(s<H\), and the upper-end condition is automatic.  Since the
whole interval lies below \(B+1<2p+1\), it contains no second multiple of
\(p\); more directly, its positive members are at most \(B<2p\).  It
contains no multiple of \(q\), because \(B<q\).  Hence

\[
\gcd(N,K_B)=p.
\]

Section 2 gives \(\gcd(N,C_{1,H})=q\).  Since \(N=pq\), the displayed
complementary-factor identity follows.

The commonly named upper-half interval is \(H+1,\ldots,B\).  When \(B\)
is even, this is the standard numerator interval above.  When \(B\) is odd,
it contains the one extra element \(H+1\).  The range proof gives
\(H+1<p\), so this extra element is a unit modulo \(N\).  The two interval
products therefore have the same gcd with \(N\), although they are not the
same integer.

This proves that the shifted endpoint does not create a stronger algebraic
factor source than the central-binomial/AP-product gate.  It only exposes
the other prime.

## 6. Product and exact-cancellation form

For \(s\ge1\), multiply the denominator terms in the recurrence.  Reduction
modulo \(N\), followed by the substitution \(j=B-c\), gives

\[
D_r
\equiv\prod_{c=1}^{H-1}(c-B)
=(-1)^{H-1}\prod_{j=B-H+1}^{B-1}j
\pmod N.
\]

The interval contains \(p=B-s\): its upper endpoint contains \(p\) because
\(s\ge1\), and its lower endpoint contains \(p\) because \(s\le H-1\).
It contains no other multiple of \(p\), since its upper endpoint is below
\(B<2p\), and it contains no multiple of \(q\), since it is below
\(B<q\).  Therefore \(\gcd(N,D_r)=p\).

For the defining quotient, the range facts show that \(B!\) contains
exactly one factor divisible by \(p\), namely \(p\), and none divisible by
\(q\).  Hence \(B!=pU\) with \(U\) a unit modulo \(N\).

In

\[
P_{r,c}=\prod_{j=1}^{B}(rN+c-j),
\]

the index \(j=c\) contributes \(rN\).  All other factors are nonzero
modulo \(q\), because another such index would differ from \(c\) by \(q>B\).
Modulo \(p\), the only possible second zero index is \(j=c+p\).  It lies
in \(1,\ldots,B\) exactly when

\[
c+p\le B,
\]

or \(c\le s\).  Consequently, after removing \(rN\), the product is a
unit modulo \(N\) exactly on the successful side \(c>s\), and it retains
an extra \(p\)-factor exactly on the zero side \(c\le s\).  Exact division
by \(B!=pU\) cancels the hidden factor from \(rN\), leaving the threshold
law.  Modular inversion cannot perform that cancellation because \(B!\)
is a zero divisor modulo \(N\).

The denominator interval can also be written as

\[
\prod_{j=B-H+1}^{B-1}j
=\frac{(B-1)!}{(B-H)!}.
\]

Its lower factorial is a unit modulo \(N\), because
\(B-H=\lceil B/2\rceil<p\).  Thus this is precisely an upper-half
factorial/AP product containing the hidden prime once.  The recurrence
representation has not removed the original product gate.

## 7. Multiplier and representation boundaries

The Lucas formula gives

\[
C_{r,c}\equiv rq\binom{c-1}{s}
\equiv rC_{1,c}\pmod N.
\]

For gcd-screened \(r\), this is multiplication by a unit.  The denominator
gcd calculation is independent of \(r\).  Hence top-multiplier
randomization does not move or smooth the threshold.

For the beta-two carries, the exact decomposition already gives

\[
h_r-z_{r,t}\equiv rp^{-1}\pmod {2^t}.
\]

Subtracting \(r\) times the \(r=1\) equation proves

\[
h_r-rh_1\equiv z_{r,t}-rz_{1,t}\pmod {2^t}.
\]

Thus all these hidden coordinates lie on one public affine line.

Vandermonde gives the exact endpoint expansion

\[
C_{r,H}
=\sum_{j=0}^{H}\binom Hj\binom{rN-1}{B-j}.
\]

Equivalently, the Newton differences of the degree-\(B\)
integer-valued polynomial \(c\mapsto C_{r,c}\) are remote binomial
coefficients.  Literal use of either formula has \(H+1\) terms.  Since
\(H=\Theta(\sqrt N)\), this is exponential in the bit length of \(N\).

The scalar recurrence is an order-one holonomic product of length \(H\).
The standard baby-step/giant-step scale is
\(H^{1/2+o(1)}=N^{1/4+o(1)}\), also exponential in the bit length.  In
composite characteristic, its denominator product is exactly the
factor-bearing product proved above.

Power-of-two binomial algorithms can evaluate the same integer modulo a
large power of two.  That modulus is coprime to \(N\), so this computation
does not test the coefficient's hidden \(p\)-divisibility and does not give
its residue modulo \(N\).  The local \(p\)-adic formula in Section 2
describes the desired jump, but accessing that hidden component already
requires the unknown prime or another factor-bearing operation.

None of these observations is a circuit lower bound.  They identify the
same unresolved succinct coefficient/product evaluator in each named
representation.

## 8. Algebraic-series presentation

Let

\[
a_k=\binom{2k}{k}=[x^k](1-4x)^{-1/2}.
\]

If \(B=2H\), then \(K_B=a_H\).  If \(B=2H+1\), then

\[
K_B=\frac{2H+1}{H+1}a_H.
\]

The denominator \(H+1\) is a unit modulo \(N\).  If the numerator
\(2H+1=B\) is a nonunit, then \(B=p\) and the elementary
\(\gcd(N,B)\) screen factors.  On the unresolved branch, the displayed
multiplier is a unit, so evaluation of \(K_B\) and of the algebraic-series
coefficient \(a_H\) have the same factor-bearing gcd.

The coefficient recurrence is

\[
(k+1)a_{k+1}=2(2k+1)a_k.
\]

Every denominator through \(k=H-1\) is a unit because \(H<p\).  On the
unresolved branch \(p\le B-1\), so the unique index

\[
k=\frac{p-1}{2}
\]

lies in \(0,\ldots,H-1\).  Its numerator is divisible by \(p\).  No
numerator is divisible by \(q\), because \(2k+1<B<q\).  Thus this
algebraic recurrence is the same hidden-product gate with the nonunit in a
numerator rather than a denominator.

Bostan, Christol, and Dumas give logarithmic-in-index remote-coefficient
algorithms for algebraic series over a *known finite prime field*.  Their
method uses the prime-field Frobenius, base-characteristic section
operators, and preprocessing whose cost grows polynomially or
quasi-linearly with the characteristic.  Applying it separately in
characteristic \(p\) or \(q\) requires the hidden factor and an exponential
size characteristic.  Applying the same proof over
\(\mathbb Z/N\mathbb Z\) is invalid: this ring is not a prime field, and
the required single prime-characteristic Frobenius/Cartier decomposition is
not available from the public modulus.

Using many small auxiliary prime fields computes residues of the exact
integer coefficient.  Reconstructing the integer this way needs total
auxiliary modulus larger than a coefficient with \(\Theta(H)\) bits, hence
exponentially many bits in the input length.  Those residues do not by
themselves determine the residue modulo the coprime modulus \(N\).

Therefore the algebraic-series encoding is a genuinely different
representation but supplies no known numerical-QP evaluator for this gate.
This is a named-method boundary, not a proof that no such evaluator exists.
