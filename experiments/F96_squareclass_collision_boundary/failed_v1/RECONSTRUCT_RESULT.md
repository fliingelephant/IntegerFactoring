# F96 proof-blind reconstruction result

## Verdict: **FAIL as written**

The general theorem is correct. The numerical claims in Parts II and III
are correct. The main claim in Part IV is also correct when "useful" means
that the induced root gives a proper gcd: the first useful hit is
\((99,1)\), with the stated ordinals and factors.

Three unqualified collision claims in Part IV are false under the exact-square
test that Part IV defines:

1. The \(0\leq a,b\leq12\) menu has four collisions, not zero. All four
   merely reproduce \(P_1\), so none is useful.
2. The 12 raw monomials other than 1 contain collisions with \(P_1\), under
   either natural reading of that sentence. None gives a new useful
   canonical relation.
3. The complete subgroup has six residues for which \(P_1P(c)\) is a
   square, not two. Four reproduce \(P_1\); exactly two are useful and
   give the new relation value \(P_2\).

Thus all substantive intended claims pass after inserting **useful/new**
in those three statements. The literal statement does not pass.

## I. General square-class theorem

For a prime \(p\), write \(v_p(P_i)=e_i\). Two positive integers have the
same class in
\(\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2\) exactly when
\(e_1-e_2\) is even for every \(p\). Since

\[
e_1-e_2\equiv e_1+e_2\pmod 2,
\]

this is equivalent to every exponent in \(P_1P_2\) being even. That is
equivalent to \(P_1P_2\) being an exact integer square. This proves
\((1)\Longleftrightarrow(2)\).

Let \(D=\gcd(P_1,P_2)\), and put \(X=P_1/D\), \(Y=P_2/D\). Then
\(\gcd(X,Y)=1\). If \(P_1P_2=D^2XY\) is a square, then \(XY\) is a square.
Coprimality makes every prime exponent in each of \(X\) and \(Y\) even,
so uniquely

\[
X=A^2,\qquad Y=B^2,\qquad \gcd(A,B)=1
\]

for positive integers \(A,B\). If \(D\) were a square, then both
\(P_i\) would be squares, contrary to the hypotheses. Conversely,
\(P_1=DA^2\) and \(P_2=DB^2\) give
\(P_1P_2=(DAB)^2\). This proves \((2)\Longleftrightarrow(3)\), including
the assertion that \(D\) is not a square.

Since \(P_i\equiv1\pmod N\), both \(P_i\) are units modulo \(N\).
Every divisor of a unit is coprime to \(N\), so \(D,A,B\) are units
modulo \(N\). From

\[
DA^2\equiv DB^2\equiv1\pmod N
\]

and the invertibility of \(D\), one gets \(A^2\equiv B^2\pmod N\). The
positive square root is

\[
R=\sqrt{P_1P_2}=DAB,
\qquad R^2\equiv1\pmod N.
\]

Multiplication by a unit does not change a gcd with \(N\). Moreover,

\[
B(R-1)=DAB^2-B\equiv A-B\pmod N,
\]

\[
B(R+1)=DAB^2+B\equiv A+B\pmod N.
\]

Therefore

\[
\gcd(R-1,N)=\gcd(A-B,N),\qquad
\gcd(R+1,N)=\gcd(A+B,N).
\]

For odd \(N>1\), no prime divisor of \(N\) divides both \(R-1\) and
\(R+1\), because their difference is 2. Since
\(N\mid(R-1)(R+1)\), every prime-power divisor of \(N\) lies wholly in
one of the two factors. Consequently

\[
\gcd(R-1,N)\gcd(R+1,N)=N.
\]

Both gcds are proper and nontrivial exactly when
\(R\not\equiv\pm1\pmod N\). The two gcd identities show that this is
equivalent to \(A\not\equiv B\pmod N\) and
\(A\not\equiv-B\pmod N\). This proves the factoring criterion (with
"factors" understood as producing a proper divisor of a composite
\(N\)).

For the stated counterexample,

\[
102\cdot136=13872=3\cdot68^2=1+97\cdot143,
\]

\[
125\cdot135=16875=3\cdot75^2=1+118\cdot143.
\]

All four endpoints lie in \([1,142]\), so the congruences also verify the
canonical inverses. Here \(D=3\), \(A=68\), \(B=75\), and

\[
R=3\cdot68\cdot75=15300=107\cdot143-1.
\]

Thus the root is global \(-1\), and the gcds are \(1\) and \(143\), not
proper factors.

## II. The state at \(N=2773\)

First,

\[
3\cdot43^2=5547=1+2\cdot2773.
\]

The following exact modular-power certificate proves the order claims:

\[
\begin{array}{c|c}
\text{power}&\text{residue modulo }2773\\ \hline
43^{667}&2772=-1\\
43^{1334}&1\\
43^{58}&237\\
43^{46}&847
\end{array}
\]

Since \(1334=2\cdot23\cdot29\), testing the quotient by each prime
divisor proves \(\operatorname{ord}_{2773}(43)=1334\). Also
\(3\equiv43^{-2}\pmod{2773}\), so

\[
\operatorname{ord}_{2773}(3)
=\frac{1334}{\gcd(1334,2)}=667.
\]

(Direct checks are \(3^{667}=1\), \(3^{29}=2656\), and
\(3^{23}=753\).) Hence

\[
H=\langle3,43\rangle=\langle43\rangle,qquad |H|=1334.
\]

The inverse of 43 is 129 because \(43\cdot129=5547\equiv1\). Thus

\[
t=842\cdot129=108618\equiv471\pmod{2773},
\qquad471^2=221841=80\cdot2773+1.
\]

The residue 471 is neither 1 nor \(-1=2772\). If \(842\) belonged to
the cyclic group \(H\), then \(t=842\cdot43^{-1}\) would be a second
element of order two in \(H\), distinct from
\(43^{667}=-1\). A cyclic group has at most one element of order two, so
\(842\notin H\). Finally,

\[
842\cdot2526=2126892=1+767\cdot2773,
\]

so \(2526=842^{-1}\pmod{2773}\). Membership is closed under inversion;
hence \(2526\notin H\) as well.

## III. Alternative canonical presentation

Repeated squaring gives \(3^{99}\equiv2093\pmod{2773}\), and hence

\[
[3^{99}43]_{2773}=[2093\cdot43]_{2773}=1263.
\]

The claimed inverse and product check exactly:

\[
1263\cdot1684=2126892
=1+767\cdot2773
=3\cdot842^2
=842\cdot2526.
\]

Both 1263 and 1684 lie in \([1,2772]\), so 1684 is the canonical
inverse. The first is a word in \(H\), and the second is its inverse, so
both are in \(H\), although the two factors in the last presentation are
not.

Since \(P_1=3\cdot43^2\) and \(P_2=3\cdot842^2\),

\[
\sqrt{P_1P_2}=3\cdot43\cdot842=108618.
\]

Also \(2773=47\cdot59\), and exact division gives

\[
108617=47\cdot2311,\qquad 59\nmid108617,
\]

\[
108619=59\cdot1841,\qquad 47\nmid108619.
\]

Therefore the two gcds are exactly 47 and 59. This is a change of the
integer presentation of a relation inside the same residue subgroup; it
does not enlarge \(H\).

## IV. Exhaustive selector reconstruction

Because \(2^{11}<2773<2^{12}\), \(n=12\). The square menu has
\((144+1)^2=21025\) ordered pairs.

The complete exact-square output after skipping repeated residues is:

\[
\begin{array}{c|c|c|c|c|c|c|c}
\text{pair ordinal}&\text{unique ordinal}&(a,b)&c&w&P&\sqrt{P_1P}&
(\gcd(R-1,N),\gcd(R+1,N))\\ \hline
2&2&(0,1)&43&129&5547&5547&(2773,1)\\
3&3&(1,0)&3&1849&5547&5547&(2773,1)\\
4&4&(0,2)&1849&3&5547&5547&(2773,1)\\
5&5&(1,1)&129&43&5547&5547&(2773,1)\\
5150&299&(99,1)&1263&1684&2126892&108618&(47,59)
\end{array}
\]

There are no other exact-square hits among the 433 unique residues reached
by this menu. Thus \((99,1)\) is exactly the first **useful** hit, and it
has all the claimed values.

The pair ordinal also follows without enumeration. There are
\(1+2+\cdots+100=5050\) pairs with \(a+b<100\). At sum 100, increasing
\(a\) puts \((99,1)\) in position 100, hence ordinal 5150.

For the unique ordinal, use \(3=43^{-2}\) to write

\[
c_{a,b}=43^{b-2a}.
\]

Just before \((99,1)\), the exponents already seen are all integers from
\(-198\) through 100 except \(-197\). The target has exponent \(-197\).
Indeed, use \((a,b)=(0,e)\) for \(0\leq e\leq100\). For
\(e=-m\), use \(a=\lceil m/2\rceil\) and \(b=2a-m\in\{0,1\}\).
This pair precedes the target for \(1\leq m\leq196\) and for \(m=198\);
\(m=197\) gives the target itself. The ordering bounds show that no
earlier exponent lies outside that interval.
After it, there are therefore 299 exponents. Their span is less than the
order 1334, so none become equal modulo 1334. This proves unique-residue
ordinal 299.

### Independent finite check

The following standard-library code implements the definitions directly.
The scan itself uses only \(N\), 3, 43, integer modular arithmetic,
integer square root, and gcd. In particular, it does not use 842, 2526,
47, or 59 as inputs.

```python
from math import gcd, isqrt

N = 2773
P1 = 3 * 43**2

def scan(m):
    pairs = []
    for s in range(2*m + 1):
        for a in range(m + 1):
            b = s - a
            if 0 <= b <= m:
                pairs.append((a, b))

    seen = set()
    hits = []
    for pair_ordinal, (a, b) in enumerate(pairs, 1):
        c = pow(3, a, N) * pow(43, b, N) % N
        if c in seen:
            continue
        seen.add(c)
        w = pow(c, -1, N)
        P = c * w
        R = isqrt(P1 * P)
        if R * R == P1 * P:
            hits.append((pair_ordinal, len(seen), a, b, c, w, P,
                         R, gcd(R-1, N), gcd(R+1, N)))
    return pairs, seen, hits

pairs, seen, hits = scan(144)
assert len(pairs) == 21025 and len(seen) == 433
assert hits == [
    (2, 2, 0, 1, 43, 129, 5547, 5547, 2773, 1),
    (3, 3, 1, 0, 3, 1849, 5547, 5547, 2773, 1),
    (4, 4, 0, 2, 1849, 3, 5547, 5547, 2773, 1),
    (5, 5, 1, 1, 129, 43, 5547, 5547, 2773, 1),
    (5150, 299, 99, 1, 1263, 1684, 2126892, 108618, 47, 59),
]

_, _, small_hits = scan(12)
assert small_hits == hits[:4]

raw = []
a = 0
while 3**a < N:
    b = 0
    while 3**a * 43**b < N:
        raw.append(3**a * 43**b)
        b += 1
    a += 1
assert sorted(raw) == [1, 3, 9, 27, 43, 81, 129, 243, 387,
                       729, 1161, 1849, 2187]

canonical_raw_closers = set()
direct_raw_closers = set()
for c in raw[1:]:
    w = pow(c, -1, N)
    R = isqrt(P1 * c * w)
    if R * R == P1 * c * w:
        canonical_raw_closers.add(c)
    R = isqrt(P1 * c)
    if R * R == P1 * c:
        direct_raw_closers.add(c)
assert canonical_raw_closers == {3, 43, 129, 1849}
assert direct_raw_closers == {3, 27, 243, 2187}

subgroup_closers = set()
c = 1
for k in range(1334):
    w = pow(c, -1, N)
    R = isqrt(P1 * c * w)
    if R * R == P1 * c * w:
        subgroup_closers.add((c, w, c*w, gcd(R-1, N), gcd(R+1, N)))
    c = c * 43 % N
assert c == 1
assert subgroup_closers == {
    (3, 1849, 5547, 2773, 1),
    (43, 129, 5547, 2773, 1),
    (129, 43, 5547, 2773, 1),
    (1849, 3, 5547, 2773, 1),
    (1263, 1684, 2126892, 47, 59),
    (1684, 1263, 2126892, 47, 59),
}
```

### Literal failures and exact corrections

For \(0\leq a,b\leq12\), the scan returns the first four rows of the
table above. Therefore the smaller menu has four non-useful collisions,
not no collision. The correct claim is:

> The smaller menu has no **useful** collision and no new relation value.

There are 13 raw monomials below \(N\), including 1. The other 12 are

\[
3,9,27,43,81,129,243,387,729,1161,1849,2187.
\]

If each is used as the canonical residue \(c\), then
\(c\in\{3,43,129,1849\}\) gives \(P(c)=P_1\), hence four non-useful
exact-square collisions. If instead "collision with \(P_1\)" means that
the raw monomial \(M\) itself has the same square class, then

\[
M\in\{3,27,243,2187\}
\]

gives an exact square \(P_1M\). Thus the unqualified raw-monomial claim is
false under either reading. The supported correction is:

> The 12 raw monomials other than 1 give no **new useful canonical-relation**
> collision with \(P_1\).

Finally, an exhaustive traversal \(c=43^k\), \(0\leq k<1334\), gives all
exact-square-closing residues:

\[
\begin{array}{c|c|c|c}
c&w&P(c)&\text{gcd pair}\\ \hline
3&1849&5547&(2773,1)\\
43&129&5547&(2773,1)\\
129&43&5547&(2773,1)\\
1849&3&5547&(2773,1)\\
1263&1684&2126892&(47,59)\\
1684&1263&2126892&(47,59)
\end{array}
\]

Thus there are six exact-square closers, with density
\(6/1334=3/667\). There are exactly two **useful/new** closers, 1263 and
1684. They form one inverse pair, give one relation value, and have the
claimed useful density \(2/1334=1/667\).

## Exact scope after correction

The selector \(0\leq a,b\leq n^2\) is public and polynomial-size: it has
\((n^2+1)^2=O(n^4)\) candidates, and every operation used by the scan is
polynomial-time in \(n=\lceil\log_2N\rceil\). For this post-selected
instance it finds a useful alternative canonical presentation inside the
unchanged group \(H\).

The reconstruction gives no all-input success guarantee, no lower bound
on useful-closing density for other inputs, and no new factoring mechanism
beyond decoding a nontrivial square root of 1 by gcd.
