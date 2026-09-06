# F193 V3 candidate — narrow QP boundaries for separating representations

## Status and exact scope

This proof-only revision replaces the failed V2 candidate. No mathematical
computation is used. Its only substantive change repairs a TeX transcription
defect in the two copies of the CM characteristic polynomial.

It records four independent, narrow boundaries for Inspiration B5:

1. explicit sparse cusp-boundary constructions in modular symbols at
   squarefree level;
2. uniform small-modulus evaluation of P29's Eisenstein coefficient;
3. Dirichlet-twist banks of one fixed form at the one index \(N\);
4. prime torsion acted on by one endomorphism that descends over a connected
   arithmetic base.

This is not a general obstruction to modular symbols, cusp forms, modular
forms, finite etale algebras, elliptic torsion, or low-dimensional
representations.

In Sections 1--3, let \(N=pq\) for distinct odd primes and put

\[
n=\left\lceil\log _2(N+1)\right\rceil.
\]

## 1. Explicit sparse modular-symbol cusp boundary

For a reduced rational cusp \(a/c\), with \(c=0\) for infinity, define

\[
d(a/c)=\gcd(c,N).
\tag{1.1}
\]

At squarefree level, this divisor determines the \(\Gamma _0(N)\)-orbit.
Thus level \(pq\) has cusp types \(1,p,q,N\).

Let

\[
C=\sum_{i=1}^{L}u_i\{\alpha_i,\beta_i\}
\tag{1.2}
\]

be an explicitly encoded sparse modular-symbol chain whose total encoding
length is numerical-QP in \(n\). In particular, all coefficients and all
reduced rational endpoints are listed with numerical-QP total bit length.
Then one of the following happens in numerical-QP time:

1. an endpoint denominator has gcd \(p\) or \(q\) with \(N\), which factors
   \(N\);
2. all endpoints have type \(1\) or \(N\), and

   \[
   \partial C\in\mathbb Z([c_N]-[c_1]).
   \tag{1.3}
   \]

This is a statement about boundary support only. It does not restrict the
coefficient in (1.3), which could itself contain factor information. It does
not cover boundary-zero cuspidal classes or compressed dense presentations.

The standard public operators have the following exact support behavior:

- every good-prime Hecke branch \(T_m\), with \(\gcd(m,N)=1\), preserves
  cusp type;
- Fricke \(W_N\) sends type \(d\) to \(N/d\), and therefore preserves the
  partition \(\{1,N\}\cup\{p,q\}\);
- a standard Atkin--Lehner operator \(W_Q\) is labeled by an exact divisor
  \(Q\parallel N\) and toggles the primes dividing \(Q\). At level \(pq\),
  a proper label is \(p\) or \(q\), so the public label already factors
  \(N\). A standard unnormalized integral representative has determinant
  \(Q\); no determinant claim is made for normalized analytic matrices or
  opaque circuits.

Hence QP-many explicit endpoints, good-prime Hecke branches, and Fricke
applications cannot create factor-local boundary support from the global
cusps. An explicitly named selective Atkin--Lehner operator already includes
a factor.

## 2. Uniform small-modulus CRT amplification of P29

On the stated promise, P29's coefficient is

\[
b_N=\sigma _1(N)=N+p+q+1.
\tag{2.1}
\]

Suppose one uniform classical algorithm takes \((N,\ell)\), for every
auxiliary prime

\[
\ell\le Cn\log(n+2)
\tag{2.2}
\]

with one sufficiently large absolute constant \(C\), and returns
\(b_N\bmod\ell\) in numerical-QP time in \(n+\log\ell\). Then promised
semiprimes can be factored deterministically in numerical-QP time.

The same conclusion holds if the evaluator returns
\(24b_N\bmod\ell\) for every \(\ell\ge5\) in the range.

The proof makes \(O(n)\) calls at distinct \(O(\log n)\)-bit primes, uses CRT
to recover the exact \(b_N\), and then recovers \(p+q\). Thus P29's
fixed-small-modulus opening is pointwise:

- one fixed modulus or fixed finite bank is not covered;
- a single uniform evaluator over a growing small-modulus bank is already a
  factoring interface.

## 3. Dirichlet-twist banks have rank at most one

Let

\[
f=\sum_{m\ge1}a_f(m)q^m
\]

be one fixed normalized modular eigenform. Let
\(\chi_1,\ldots,\chi_L\) be explicitly represented Dirichlet characters,
possibly imprimitive and with different defining moduli and coefficient
fields. Then

\[
a_{f\otimes\chi_j}(N)=\chi_j(N)a_f(N)
\qquad(1\le j\le L).
\tag{3.1}
\]

Every scalar \(\chi_j(N)\), including a possible zero, is public. After
placing the exact coefficient values in their explicitly represented
compatible composita, the bank is the image of one unknown under a public
linear map. Its information rank is therefore at most one.

If at least one \(\chi_j(N)\ne0\), that row recovers \(a_f(N)\) by division
by a public root of unity. If all values vanish, the bank has rank zero and
does not recover the base coefficient. In particular, a primitive character
presented at a conductor coprime to \(N\), or any character whose defining
modulus is coprime to \(N\), has a nonzero value at \(N\).

This is an information identity, not an evaluator lower bound. A QP
evaluator for one nonzero twist would be a QP evaluator for \(a_f(N)\). The
claim does not cover genuinely different forms, Rankin convolutions,
nontwist operations, or unrelated indices.

## 4. One global endomorphism is synchronized on auxiliary-prime torsion

Let \(S\) be a connected arithmetic base with characteristic-zero generic
point. Let an elliptic curve \(E/S\) and an endomorphism

\[
\alpha\in\operatorname{End}_S(E)
\]

be globally defined. Let \(r\) be an auxiliary prime invertible on \(S\),
and let \(p,q\ne r\) be two good residue characteristics represented by
geometric points of \(S\).

After choosing geometric \(\mathbb F_r^2\)-bases, the actions

\[
\alpha_p:E_p[r]\to E_p[r],
\qquad
\alpha_q:E_q[r]\to E_q[r]
\tag{4.1}
\]

are conjugate in \(\operatorname{Mat}_2(\mathbb F_r)\). Hence they have the
same characteristic polynomial, the same canonical minimal polynomial, and,
when invertible, the same order.

For a globally defined CM endomorphism, its characteristic polynomial on the
prime-to-characteristic Tate module is

\[
X^2-\operatorname{Tr}(\alpha)X+\operatorname{Nm}(\alpha),
\tag{4.2}
\]

and reduction modulo \(r\) gives the common characteristic polynomial on
\(E_p[r]\) and \(E_q[r]\). A scalar map \([a]\) acts as \(aI_2\) in both
fibers.

Thus a fixed globally descended endomorphism cannot acquire a local order or
minimal-polynomial mismatch merely by good reduction. The theorem excludes
local Frobenius, endomorphisms created only after reduction, characteristic-
primary torsion, disconnected CRT bases, and CRT-glued local maps that do not
descend from one connected base. These excluded objects remain live.

## 5. Surviving B5 interface

F193 V3 removes four standard repackagings only. A live B5 route can still
use a boundary-zero cuspidal quotient, a compressed characteristic-scale
modular-symbol operation, genuinely different forms, a new uniform
small-modulus evaluator, local Frobenius, or a factor-free construction of a
reduction-only endomorphism or fine CRT orientation.
