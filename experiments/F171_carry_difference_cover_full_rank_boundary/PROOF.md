# Proof of the F171 candidate

## 1. The occupied carry class

For \(P_k=1+kN\) and a prime \(r\nmid N\),

\[
r\mid P_k
\quad\Longleftrightarrow\quad
1+kN\equiv0\pmod r
\quad\Longleftrightarrow\quad
k\equiv-N^{-1}\pmod r.
\]

This proves the exact carry gate. It also shows why

\[
r\mid(k-\ell)
\]

is only a necessary same-class condition. It does not show that the common
class is the occupied class, and it says nothing about valuation parity.

## 2. Public endpoints that are also private-row primes

Let \(m=4R\), with \(m\) sufficiently large. The prime number theorem
permits the choice of distinct odd primes

\[
m<g_1<\cdots<g_m<4m\log m.
\]

All these primes exceed five. In particular,

\[
k<g_k,
\qquad
g_k>m>|k-j|\quad(k\ne j).
\]

Put

\[
Q=\prod_{k=1}^m g_k^2.
\]

The moduli are pairwise coprime. By the Chinese remainder theorem there is
one residue class \(Z\pmod Q\) satisfying, for every \(k\),

\[
Z\equiv(g_k-1)k^{-1}\pmod {g_k^2}.
\]

Every inverse exists because \(g_k>m\ge k\). The class \(Z\) is reduced
modulo \(Q\): its residue modulo each \(g_k\) is \(-k^{-1}\), which is
nonzero.

## 3. A trial-hard semiprime in the CRT class

Bertrand's postulate gives a prime

\[
Q<p<2Q.
\]

Let \(a\in\{1,\ldots,Q-1\}\) be the reduced representative of

\[
a\equiv Zp^{-1}\pmod Q.
\]

Because \(5\nmid Q\), one of \(j\in\{2,3,4\}\) makes

\[
b=a+jQ
\]

coprime to five. Then

\[
2Q<b<5Q,
\qquad
\gcd(b,5Q)=1.
\]

Choose the least prime \(\ell\) in the progression \(b\pmod {5Q}\).
Dirichlet's theorem gives existence, and Linnik's theorem gives absolute
constants \(C,L\) such that

\[
2Q<b\le\ell\le C(5Q)^L.
\]

Set

\[
N=p\ell.
\]

The primes are distinct because \(p<2Q<\ell\). They are odd, and

\[
N\equiv p b\equiv p a\equiv Z\pmod Q.
\]

This construction makes no bounded-ratio claim for \(p\) and \(\ell\).

## 4. Canonical carries and endpoint bounds

For each \(1\le k\le m\), the congruence modulo \(g_k\) gives

\[
g_k\mid1+kN.
\]

Define

\[
w_k=\frac{1+kN}{g_k}.
\]

It is a positive integer. Since \(k<g_k\),

\[
1+kN\le1+(g_k-1)N<g_kN,
\]

so \(w_k<N\). Also \(g_k<N\), and

\[
g_kw_k=1+kN\equiv1\pmod N.
\]

Thus \(w_k=\iota_N(g_k)\), and the canonical carry is exactly \(k\).
Distinct carries give distinct exact values, so global exact-value
deduplication keeps one column for each of these \(m\) values. An earlier
source position can own the retained occurrence of the same value, but it
cannot delete the value or its \(g_k\)-incidence. Its endpoint presentation
must remain in the separate presentation ledger.

For a hidden factor \(s\in\{p,\ell\}\), if

\[
s\mid g_k-w_k,
\]

then \(g_k^2\equiv1\pmod s\). If

\[
s\mid g_k+w_k,
\]

then \(g_k^2\equiv-1\pmod s\). For large \(m\),

\[
0<g_k^2-1<g_k^2+1<Q<s.
\]

Neither congruence is possible. Every selected sign screen is therefore
one.

## 5. Every small target row occurs twice with valuation one

Fix a rational prime \(r\le R\). Both hidden factors exceed \(Q>r\), so
\(r\nmid N\). Let

\[
a=-N^{-1}\pmod r,
\qquad 1\le a<r,
\]

and write

\[
1+aN=rh.
\]

For \(j=0,1,2,3\), put

\[
k_j=a+jr.
\]

Then

\[
1+k_jN=r(h+jN),
\qquad
1\le k_j\le4r-1\le4R-1<m.
\]

Because \(N\) is a unit modulo \(r\), exactly one residue class of \(j\)
modulo \(r\) makes \(h+jN\equiv0\pmod r\). Among
\(j=0,1,2,3\), at least two avoid that class: for \(r=2\), each residue
occurs twice; for \(r=3\), one residue occurs twice and the other two occur
once; for \(r\ge5\), the four residues are distinct. For at least two
distinct indices \(k_j\), therefore,

\[
v_r(1+k_jN)=1.
\]

This is a four-point local selection. It does not claim that at most one
carry in the full interval \(1\le k\le4R\) is divisible by \(r^2\).

This proves exact odd-parity row reuse for every prime \(r\le R\).

## 6. Every column retains a private valuation-one row

The CRT condition modulo \(g_k^2\) gives

\[
1+kN\equiv g_k\pmod {g_k^2}.
\]

Hence

\[
v_{g_k}(P_k)=1.
\]

For \(j\ne k\), reduction modulo \(g_k\) gives

\[
1+jN
\equiv
1-jk^{-1}
\equiv
(k-j)k^{-1}
\not\equiv0\pmod {g_k},
\]

because \(0<|k-j|<m<g_k\). Thus \(g_k\) divides no other selected exact
value. The rows \(g_1,\ldots,g_m\) form an identity submatrix, so the full
selected parity matrix has rank \(m\) and kernel zero.

This is also the exact P111 diameter gate: every private row \(g_k>m\)
exceeds the diameter of the carry interval, so it cannot divide any nonzero
selected carry difference.

By contrast, its restriction to rational-prime rows at most \(R\) has at
most \(\pi(R)\) rows and \(m\) columns. Hence

\[
\dim\ker M_{\le R}\ge m-\pi(R),
\]

but every nonzero vector in this restricted kernel is killed by at least one
private \(g_k\)-row in the full matrix.

## 7. Input length, source size, and trial hardness

Every selected prime lies between \(m\) and \(4m\log m\). Therefore

\[
2m\log m<\log Q=\Theta(m\log m).
\]

The bounds on \(p\) and \(\ell\) give

\[
2\log Q+O(1)
<\log N
<(L+1)\log Q+O(1).
\]

Consequently,

\[
n=\Theta(m\log m),
\qquad
m=\Theta\!\left(\frac{n}{\log n}\right),
\qquad
R=\Theta\!\left(\frac{n}{\log n}\right).
\]

Taking the unlabelled logarithm to be natural, the lower bound gives

\[
n>2\log_2Q>4m\log_2m
=\frac4{\log 2}m\log m
>4m\log m>g_k
\]

Thus every selected first endpoint lies in the ordinary public seed interval
through \(n\). The selected bank has polynomial size, and each endpoint and
exact value has \(O(n)\) bits.

Both hidden factors exceed \(Q=2^{\Theta(n)}\), so both exceed \(n^2\) for
large \(m\). They are distinct, so \(N\) is not a perfect power.

## 8. Exact scope

The construction proves full rank only for the displayed selected bank.
Another canonical relation can reuse a private \(g_k\)-row. A complete
static or adaptive source can also find a direct factor before or after this
bank, including through an earlier endpoint presentation of the same exact
value. No claim excludes either event.

The result therefore refutes only the implication

\[
\text{small carry-difference coverage}
\Longrightarrow
\text{full parity closure}.
\]

It does not refute a complete-source theorem that proves final rank defect
after every fresh row is included. Even such a theorem must separately prove
that the P138 normalized-root image is non-global.
