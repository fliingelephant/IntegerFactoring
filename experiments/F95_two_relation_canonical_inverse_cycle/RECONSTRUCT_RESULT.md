# F95 independent proof-blind reconstruction

## Strict verdict

**PASS.**

Claims 1–5 are arithmetically and algebraically correct. The optional finite
counts also reproduce exactly. One indexing convention must be stated:
“relation indices 1 and 306” are zero-based identifiers in the full sorted
list of 634 unique relation values, before the three square values are
removed. In the filtered list their zero-based positions are 1 and 305
(one-based positions 2 and 306).

The P98 name is certificate context. This reconstruction verifies the
displayed arithmetic criterion, but does not infer any unstated P98 theorem.

## 1. Modulus certificate

\[
47\cdot59=47(60-1)=2820-47=2773=N.
\]

Also,

\[
d=\gcd(46,58)=2,\qquad A=46/2=23,\qquad B=58/2=29.
\]

Thus \(AB=667\) and \(N-1=2772\). The Euclidean algorithm gives

\[
\begin{aligned}
2772&=4\cdot667+104,\\
667&=6\cdot104+43,\\
104&=2\cdot43+18,\\
43&=2\cdot18+7,\\
18&=2\cdot7+4,\\
7&=4+3,\\
4&=3+1.
\end{aligned}
\]

Hence \(\gcd(AB,N-1)=1\). This verifies the stated stable-class certificate
criterion. The given relations and all checks below can be specified and
verified from \(N\) and their endpoints without using \(47\) and \(59\) to
choose an endpoint. A static certificate cannot establish historical search
provenance; the factorization is used here only to certify the class and to
identify the final proper factors.

## 2. Canonical-inverse relations

All endpoints satisfy \(1<g_i,w_i<N\). Direct calculation gives

\[
3\cdot1849=5547=1+2\cdot2773,
\]

and \(1849=43^2\), so

\[
P_1=3\cdot43^2.
\]

For the second relation,

\[
2526=3\cdot842,\qquad 842^2=708964,
\]

so

\[
842\cdot2526=3\cdot842^2=2126892.
\]

Also,

\[
767\cdot2773
=700\cdot2773+60\cdot2773+7\cdot2773
=2126891,
\]

and therefore \(P_2=1+767N\).

Each product is congruent to one modulo \(N\), so each \(w_i\) is an inverse
of \(g_i\). Since \(1\le w_i<N\), uniqueness of the representative in that
interval makes it the least positive inverse.

## 3. Public normalization and the modular kernel

The factorizations above give

\[
\gcd(P_1,P_2)=3\gcd(43^2,842^2).
\]

The Euclidean algorithm starts with \(842=19\cdot43+25\) and continues
through remainders \(18,7,4,3,1\), so \(\gcd(43,842)=1\). Also,
\(\gcd(3,43)=\gcd(3,842)=1\). Hence

\[
\gcd(P_1,P_2)=3,\qquad P_1/3=43^2,\qquad P_2/3=842^2,
\]

and \(3,43,842\) are pairwise coprime. These operations require only the
public integers, gcd, exact division, and exact integer square root.

On the ordered basis \((3,43,842)\), the exact columns are

\[
u_1=(1,2,0)^T,\qquad u_2=(1,0,2)^T.
\]

Modulo two they both equal \(v=(1,0,0)^T\ne0\). The one-column map
\(a\mapsto av\) is injective over \(\mathbb F_2\), so either column by
itself has rank one and zero kernel. For the two-column map,

\[
[v\mid v](a,b)^T=(a+b)v.
\]

Its rank is one and its kernel is
\[
\{(a,b):a+b=0\}=\langle(1,1)^T\rangle.
\]

Deleting either copy leaves the injective one-column map again. This is the
claimed retain-then-close cycle.

## 4. Root extraction and factors

For the kernel vector \((1,1)\), the summed exact exponent vector is

\[
u_1+u_2=(2,2,2)^T.
\]

Dividing by two gives the induced root

\[
R=3\cdot43\cdot842=108618.
\]

Equivalently,

\[
P_1P_2=(3\cdot43\cdot842)^2=R^2.
\]

Since each \(P_i\equiv1\pmod N\), \(R^2\equiv1\pmod N\). Division gives

\[
108618=39\cdot2773+471,
\]

so \(R\bmod N=471\). More sharply,

\[
R-1=108617=47\cdot2311,\qquad
R+1=108619=59\cdot1841.
\]

The first number is two less than the displayed multiple of \(59\), and the
second is two more than the displayed multiple of \(47\). Since
\(N=47\cdot59\),

\[
\gcd(R-1,N)=47,\qquad \gcd(R+1,N)=59.
\]

The congruence-of-squares form follows independently from

\[
3\cdot43^2\equiv3\cdot842^2\equiv1\pmod N
\]

and \(\gcd(3,N)=1\). Thus \(43^2\equiv842^2\pmod N\). Its two differences
are

\[
842-43=799=47\cdot17,\qquad
842+43=885=59\cdot15,
\]

which give the same two gcds.

## 5. Interpretation and stable-core scope

The presentation contains two literal canonical-inverse relations. Each is
individually nonclosing modulo two, while the retained pair closes and
produces the proper square root \(R\). If the first column is deleted, this
specific later closure is lost. Therefore retention can be necessary for a
later dependency in the maintained presentation.

This is also exactly classical congruence-of-squares factoring. It does not
establish a different factoring mechanism or a novelty claim.

The first normalization gives

\[
43^2=1849\equiv3^{-1}\pmod N,
\]

and the second gives

\[
842^2\equiv3^{-1}\pmod N.
\]

Thus the selected \(842\) is a second square root of \(3^{-1}\), distinct
from the known \(43\) up to sign. Conversely, selecting this exact endpoint
supplies that second root; its inverse is \(3\cdot842=2526<N\). Hence, for
this certificate, selecting the useful second relation contains exactly the
missing second-root task. The certificate gives no efficient method to do
so.

The factorization and the conditions on \(d,A,B\) certify the fixed test
modulus. They do not make the endpoint selection factor-blind or efficient.
The result does not prove that stable-core hypotheses cause such a cycle on
other inputs. It proves no frequency law, all-input progress law, polynomial
state bound, polynomial-time factoring algorithm, or lower bound against a
different selection or decoding method.

## Optional finite enumeration

An independent exhaustive run used the following deterministic procedure:

1. Enumerate \(g=2,\ldots,2772\).
2. Count and skip \(g\) when \(\gcd(g,N)>1\).
3. For each unit, compute its least positive inverse \(w\) and store
   \((gw,\min(g,w),\max(g,w))\).
4. Sort these triples, retain the first triple for each new exact value
   \(P=gw\), and assign zero-based indices at this point.
5. Remove entries whose \(P\) is an integer square.
6. Traverse the remaining pairs in the order
   \(i=0,\ldots\), \(j=i+1,\ldots\). Test whether \(P_iP_j\) is a square.
   If it is, test the two gcds of its positive square root with \(N\).

The run returned

\[
\begin{array}{c|r}
\text{quantity}&\text{count}\\ \hline
\text{raw candidates}&2771\\
\text{units}&2667\\
\text{nonunits}&104\\
\text{unique relation values}&634\\
\text{nonsquare relation values}&631
\end{array}
\]

The three removed square entries had full-list zero-based indices and
triples

\[
\begin{aligned}
51&:(221841,157,1413),\\
567&:(5299204,2302,2302),\\
633&:(7683984,2772,2772).
\end{aligned}
\]

The witness values \(P_1=5547\) and \(P_2=2126892\) have full-list
zero-based indices \(1\) and \(306\). After square filtering, their
zero-based positions are \(1\) and \(305\). There are \(630\) comparisons
with \(i=0\), followed by \(304\) comparisons
\((i,j)=(1,2),\ldots,(1,305)\). Therefore the witness is comparison
\(630+304=934\). No earlier tested product was an exact square. The witness
product has positive square root \(108618\), whose gcds are \(47\) and
\(59\).

This exhaustive check costs work proportional to the numerical size of
\(N\). It is supplementary finite verification, not a
polynomial-in-\(\log N\) relation-selection algorithm.

## Final scope

The result is an exact fixed-instance certificate for a two-relation
presentation and its modulo-two kernel. It shows that ephemeral deletion can
lose a later closing dependency. It does not explain how to find the second
relation efficiently or turn the example into an asymptotic algorithm.

Within this scope, the strict verdict is **PASS**.
