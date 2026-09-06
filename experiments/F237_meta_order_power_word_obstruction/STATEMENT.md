# F237 candidate — an exact finite obstruction to the zero-defect meta-order power word

## Status and scope

This is a finite proof certificate.  It gives one balanced zero-defect
semiprime on which both residual meta-orders are large and the P204 power
word

\[
W_K=\prod_{k=1}^K(N^k-1)
\]

leaves both exclusive residuals large for every `K <= 2^57`.

This statement is not an asymptotic counterfamily.  It does not disprove an
unspecified numerical-quasipolynomial upper bound.  It does not rule out a
different public integer word.

## Exact instance

Let

\[
\begin{aligned}
p&=15187245471009208343,\\
q&=26569391171797958567,\\
N&=pq
  =403515865741360589240927487586184724481.
\end{aligned}
\]

Then `p` and `q` are distinct primes and

\[
p<q<2p.
\]

For

\[
n=\lceil\log_2(N+1)\rceil=129,
\qquad
B=2^{\lfloor n/2\rfloor}=2^{64},
\]

one has

\[
N-1=BH,
\qquad
H=21874638913457614155.
\]

Moreover,

\[
v_2(p-1)=v_2(q-1)=1,
\]

and the P204 residual data are

\[
D=1,
\qquad
s_p=7593622735504604171,
\]

\[
s_q=13284695585898979283
   =37\cdot359045826645918359.
\]

All three displayed residual factors are prime.  Their exact local orders
are

\[
\operatorname{ord}_{s_p}(N)
 =3796811367752302085,
\]

\[
\operatorname{ord}_{37}(N)=36,
\qquad
\operatorname{ord}_{359045826645918359}(N)
 =179522913322959179.
\]

Consequently,

\[
\operatorname{ord}_{s_q}(N)
 =6462824879626530444,
\]

and both whole-residual meta-orders exceed `2^61`.

## Power-word obstruction

For every integer

\[
1\le K\le2^{57},
\]

put

\[
r_p={s_p\over\gcd(s_p,W_K)},
\qquad
r_q={s_q\over\gcd(s_q,W_K)}.
\]

Then

\[
r_p=s_p,
\qquad
r_q\ge359045826645918359,
\]

and hence

\[
\boxed{
\min(r_p,r_q)>2^{58}.
}
\]

The packet supplies a recursive Lucas primality certificate for every
prime used above and exact modular-order witnesses.  The verifier uses only
Python integer arithmetic.

