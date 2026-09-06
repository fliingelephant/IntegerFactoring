# F194 V3 — statement-only blind reconstruction

## Blind boundary

Before reading the statement, I computed

```text
SHA-256(V2_STATEMENT.md)
= 95764227ebc288a528c7425c5593e9a75d7ad9030556c4a9c12b00c0c85f48ab.
```

This equals the expected hash. I then read only `V2_STATEMENT.md`. The
statement was self-contained for the requested reconstruction, so I did not
read `PROMPT.md`. I did not read any other F194 file, audit, manifest,
provenance record, ledger entry, or agent report.

## Strict verdict

**PASS, with notation-only qualifications.** Every mathematical claim in the
fixed statement reconstructs from the stated hypotheses. I found no missing
case, sign error, coefficient error, false balance inequality, or unjustified
factor gcd. The qualifications at the end concern implicit definitions of
the input bit length, integer-valued bounds, circuit cost, and Boolean source
support. They do not change the theorem.

## 1. Balance and the unique hidden cancellation

Because (p<q),

\[
p<\sqrt{pq}<q.
\]

The middle quantity is not an integer, since (p\ne q) are primes. Hence

\[
p\le B=\lfloor\sqrt N\rfloor<q.
\tag{R1}
\]

The upper balance assumption gives

\[
B<\sqrt{2p^2}=\sqrt2,p<2p.
\tag{R2}
\]

Thus the only positive multiple of either hidden prime in
\(\{1,\ldots,B\}\) is (p).

Starting from

\[
A_k=(-1)^k\binom{N-1}{k},
\]

the binomial recurrence gives the exact integer identity

\[
(k+1)A_{k+1}=-(N-1-k)A_k=(k+1-N)A_k,
\]

and therefore

\[
(k+1)(A_{k+1}-A_k)=-NA_k.
\tag{R3}
\]

For (1\le k+1<p), the multiplier (k+1) is a unit modulo (N), so
\(A_{k+1}\equiv A_k\pmod N\). Since (A_0=1),

\[
A_k\equiv1\pmod N\qquad(0\le k<p).
\tag{R4}
\]

At (k+1=p), division occurs in the integers, not in
\(\mathbb Z/N\mathbb Z\):

\[
p(A_p-A_{p-1})=-pqA_{p-1}
\quad\Longrightarrow\quad
A_p-A_{p-1}=-qA_{p-1}.
\tag{R5}
\]

Using (R4), this yields

\[
A_p\equiv1-q\pmod N.
\tag{R6}
\]

For (p<k+1\le B), (R1)--(R2) show that (k+1) is divisible by neither
\(p\) nor (q). The recurrence is again invertible modulo (N), so the
word remains constant at (1-q). This proves the exact one-jump formula.
It also identifies the hidden cancellation: the factor (p) on the left of
(R5) cancels the hidden (p) in (N=pq), exposing the cofactor (q).

### AKS coefficient and sign

Pascal's identity gives the exact sign relation

\[
A_k-A_{k-1}
=(-1)^k\binom Nk
\qquad(1\le k\le N-1).
\tag{R7}
\]

Thus the coefficient of (X^k) in the Frobenius/AKS defect

\[
(1+X)^N-1-X^N
\]

is the unsigned coefficient \(\binom Nk\). Away from (k=p), the
difference in (R7) is zero modulo (N). At (k=p), (R5) gives
\(A_p-A_{p-1}\equiv-q\pmod N\), and (p) is odd, so

\[
\binom Np
\equiv(-1)^p(-q)=q\pmod N.
\tag{R8}
\]

The exceptional AKS coefficient therefore has sign (+q). The jump in the
signed (A_k)-word has sign (-q). These are consistent, not competing
sign conventions. For all other (1\le k\le B), (R7) gives
\(\binom Nk\equiv0\pmod N\).

Since (p\le B), the endpoint lies after the jump:

\[
(-1)^B\binom{N-1}{B}-1\equiv-q\pmod N.
\]

Consequently its gcd with (N=pq) is exactly (q). If
\(C=\binom{N-1}{B}\), then

\[
C\equiv q-1\pmod N\quad(B\text{ odd}),
\]

and

\[
C\equiv1-q\equiv N-q+1\pmod N\quad(B\text{ even}).
\]

Both displayed representatives lie in \([0,N)\), proving the canonical
residue formula.

## 2. Both central-binomial gcds

Let (m=\lceil B/2\rceil\). From (B<q\le2p-1),

\[
B\le q-1\le2p-2,
\]

so (m\le p-1<p\). Also (p\le B\le2m\). Finally,
\(2m\in\{B,B+1\}\). We already know (B<q). Equality (2m=q) could
only occur when (B) is odd and (2m=B+1), but then (2m) is even while
the prime (q) is odd. Therefore

\[
m<p\le2m<q.
\tag{R9}
\]

Now

\[
\binom{2m}{m}=\frac{(m+1)(m+2)\cdots(2m)}{m!}.
\]

The denominator is a unit modulo (N), since (m<p<q). The numerator
contains (p), contains no second multiple of (p) because
\(2m<q<2p\), and contains no multiple of (q). Hence

\[
v_p\!\left(\binom{2m}{m}\right)=1,
\qquad
v_q\!\left(\binom{2m}{m}\right)=0,
\]

which proves

\[
\gcd\!\left(N,\binom{2m}{m}\right)=p.
\tag{R10}
\]

For the second central coefficient, (R2) sharpens to

\[
B<\sqrt2,p<\frac32p,
\qquad 2B<3p.
\tag{R11}
\]

Because (p\le B<2p), (B!) contains exactly one multiple of (p).
Because (2p\le2B<3p), ((2B)!) contains exactly two. There are no
higher-(p)-power contributions: (2B<3p\le p^2) for odd (p\), with
strict inequality also when (p=3). Thus

\[
v_p\!\left(\binom{2B}{B}\right)=2-2\cdot1=0.
\tag{R12}
\]

On the other hand, (q<2p\le2B), while (B<q) and (2B<2q). Hence
\((2B)!) contains exactly one multiple of (q), and each copy of (B!)
contains none. Therefore

\[
v_q\!\left(\binom{2B}{B}\right)=1,
\]

and

\[
\gcd\!\left(N,\binom{2B}{B}\right)=q.
\tag{R13}
\]

This also confirms the stated distinction: (R10) is an interval-product
zero test with invertible denominator (m!), whereas the remote endpoint
coefficient (C) is itself a unit and only its signed shift exposes (q).

## 3. Polynomial index moments

Work first in \(\mathbb F_p[X]\). Frobenius gives

\[
(1+X)^{pq}=\bigl((1+X)^q\bigr)^p
\equiv(1+X^p)^q\pmod p.
\]

Therefore

\[
\binom{pq}{k}\equiv0\pmod p
\]

unless (k=pj), and for (0\le j\le q),

\[
\binom{pq}{pj}\equiv\binom qj\pmod p.
\]

For any integer polynomial (W), (W(pj)\equiv W(0)\pmod p\), with no
degree restriction. Hence

\[
\begin{aligned}
\sum_{k=1}^{N-1}W(k)\binom Nk
&\equiv W(0)\sum_{j=1}^{q-1}\binom qj\\
&=W(0)(2^q-2)\\
&\equiv W(0)(2^{pq}-2)\pmod p,
\end{aligned}
\tag{R14}
\]

where the last step is Frobenius applied to the integer (2^q).
Interchanging (p) and (q) gives the same claimed right-hand side
modulo (q). The Chinese remainder theorem then proves

\[
\sum_{k=1}^{N-1}W(k)\binom Nk
\equiv W(0)(2^N-2)\pmod N.
\tag{R15}
\]

The proof uses only evaluation of an integer polynomial at multiples of a
prime. Its degree never enters, so the absence of a degree bound is exact.

## 4. Frobenius circuit, expansions, and local orders

Binary powering constructs both \((1+X)^N\) and (X^N) with
\(O(\log N)\) arithmetic gates, so (E_N) has the claimed succinct
circuit. Its formal derivative is

\[
E_N'(X)=N\bigl((1+X)^{N-1}-X^{N-1}\bigr),
\]

which is the zero polynomial over \(\mathbb Z/N\mathbb Z\).

In characteristic (p), the freshman's-dream identity gives

\[
\begin{aligned}
\bigl((1+X)^q-1-X^q\bigr)^p
&=(1+X)^{pq}-1-X^{pq}\\
&=E_N(X).
\end{aligned}
\tag{R16}
\]

The characteristic-(q) identity follows symmetrically. The inner
polynomial in (R16) has linear coefficient (q\not\equiv0\pmod p\), so
its (X)-adic order is one; raising it to the (p)-th power makes the
order exactly (p). Symmetrically, the local order modulo (q) is exactly
(q).

For the explicit expansion modulo (p), write (q=p+d). Since
\(1\le d<p\),

\[
\begin{aligned}
E_N
&\equiv(1+X^p)^{p+d}-1-X^{p(p+d)}\\
&=(1+X^{p^2})(1+X^p)^d-1-X^{p^2+pd}\\
&=\sum_{j=1}^{d}\binom djX^{pj}
  +\sum_{j=0}^{d-1}\binom djX^{p^2+pj}
  \pmod p.
\end{aligned}
\tag{R17}
\]

The omitted (j=d) term in the second block cancels the subtracted
\(X^{p^2+pd}\). Every \(\binom dj\) is nonzero modulo (p), because
\(d<p\). The two exponent blocks are disjoint: the first lies strictly
below (p^2), and the second begins at (p^2). Thus no unstated
cross-block cancellation occurs, and the least exponent is (p).

Modulo (q),

\[
E_N\equiv(1+X^q)^p-1-X^{pq}
=\sum_{j=1}^{p-1}\binom pjX^{qj}\pmod q.
\tag{R18}
\]

For (1\le j<p\), every prime divisor of \(\binom pj\) is at most (p),
so the larger prime (q) cannot divide it. All displayed coefficients are
therefore nonzero in \(\mathbb F_q\), and the least exponent is (q).

## 5. Bounded gap and Boolean incidence

If (d=q-p<R), then

\[
d^2+4N=(q-p)^2+4pq=(p+q)^2.
\tag{R19}
\]

Thus enumeration of (1\le\delta<R) reaches (delta=d). An exact square
root (s) gives

\[
p=\frac{s-\delta}{2},
\qquad
q=\frac{s+\delta}{2}.
\]

There is no harmful earlier square in the stated range. Any square
\(s^2=\delta^2+4N\) yields positive integer factors
\((s-\delta)/2\) and \((s+\delta)/2\) of (N). The only other positive
factor pair is (1,N), whose gap is (N-1>R) because (R<p<N-1).
Each square test and verification has polynomial bit cost, and there are
numerical-QP many candidates.

Now assume (d\ge R), and let (1\le r\le R<p). In (R17), the first
block already contains the exponents

\[
p,2p,\ldots,rp.
\]

Since (p) is prime and (r<p), \(\gcd(p,r)=1\); multiplication by (p)
permutes \(\mathbb Z/r\mathbb Z\). These (r) labeled source monomials
therefore meet every residue class. In (R18), the monomials with
\(j=1,\ldots,r\) exist because (r\le R<p), and
\(\gcd(q,r)=1\). Their exponents (q,2q,\ldots,rq) likewise meet every
class.

This proves exactly the stated Boolean incidence claim. It does **not**
prove that the polynomial obtained after substituting
\(X^r=1\) has nonzero aggregate coefficient in every class: multiple
source monomials can enter one class and cancel. The proof tracks presence
of labeled sources before coefficient aggregation, as the statement
requires.

## 6. Exact joint carry interface

Let (C=\binom{N-1}{B}\). The endpoint congruence proves that

\[
(-1)^BC-(1-q)
\]

is divisible by (N), so (h) in the statement is an integer. Rearranging
its definition gives the exact equality

\[
q=1+hN-(-1)^BC.
\tag{R20}
\]

Reducing (R20) modulo (2^t) shows that the two residues
\(C\bmod2^t\) and (h\bmod2^t\) determine (q\bmod2^t\). If
\(2^t>q>0\), the canonical representative is the integer (q) itself,
so the pair recovers the factor exactly.

For fixed (C\bmod2^t) and a proposed (q\bmod2^t), compatibility is
equivalent to

\[
hN\equiv q-1+(-1)^BC\pmod{2^t}.
\tag{R21}
\]

Because (N=pq) is odd, (N) is invertible modulo (2^t). Equation
(R21) has exactly one solution (h\bmod2^t). Thus neither marginal is
claimed to determine (q); the sufficient statistic is genuinely the
joint pair.

Computing the signed endpoint residue gives (q) by a gcd. Computing the
joint pair gives (q) by (R20). Recovering either local (X)-adic order
returns the integer (p) or (q). Therefore each listed primitive is
sufficient. None is constructed by the statement. Under the balance
promise, (B=\Theta(\sqrt N)=2^{\Theta(n)}), so literal coefficient
truncation is exponential in the input bit length.

## Implicit assumptions and exact limits

1. The symbol (n), used in “numerical-QP”, (R(n)), and (t=O(n)), is
   not defined inside V2. The claims require the standard interpretation
   (n=\Theta(\log N)), normally the binary input length.
2. (R(n)) is implicitly a positive integer-valued bound. The variables
   (r,t,\delta) are integers, with (t\ge0). If (R) were real-valued,
   the enumeration and inequalities should be read with the appropriate
   floor or ceiling.
3. “(O(\log N))-gate powering circuit” uses the usual fan-in-two
   arithmetic-circuit model and repeated squaring. It is a circuit-size
   statement, not a claim that expanded coefficients or dense
   polynomials can be materialized in that cost.
4. A local (X)-adic order means the least exponent having nonzero
   coefficient in \(\mathbb F_p[X]\) or \(\mathbb F_q[X]\). It is not an
   order after reducing exponents modulo (r).
5. “Boolean source support” must mean incidence of the labeled monomials
   displayed in (12)--(13), before sources with the same residue class are
   added. This is also the only meaning supported by the proof, and it is
   consistent with the statement's express cancellation disclaimer.
6. The square test in the bounded-gap branch is an exact integer-square
   test, followed by parity and multiplication verification. These steps
   have polynomial bit complexity.
7. The quotient (h) is defined using the hidden (q). Its definition is
   a sufficient-statistic identity, not a public evaluation algorithm.
   Primitive 2 must compute its residue from the public input by some new
   method; the theorem does not provide one.
8. “Recover a local order” must mean output its numerical value. Merely
   proving that the two hidden local orders exist would not by itself
   reveal a factor.
9. All gcds use positive gcd convention. The binomial coefficients and
   recurrence are exact integer objects; no modular division by a nonunit
   is hidden in either central-binomial argument or the one-jump proof.

Subject to these explicit readings, the fixed V2 statement is internally
complete and correct.
