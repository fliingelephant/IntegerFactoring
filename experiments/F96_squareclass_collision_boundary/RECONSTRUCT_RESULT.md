# Proof-blind reconstruction result: PASS

## Verdict

**PASS.** Every general claim and every fixed-instance claim in
`RECONSTRUCT_STATEMENT.md` is correct. No mathematical correction is
needed.

Two counting conventions are important:

- A menu hit is counted only when its residue occurs for the first time.
- The raw-monomial count of 12 excludes the monomial \(1=3^0 43^0\).

## I. General theorem

Let \(v_p\) denote the exponent of a prime \(p\) in a positive rational.
For positive integers \(P_1,P_2\), the following are equivalent:

\[
P_1/P_2\text{ is a rational square}
\iff v_p(P_1)-v_p(P_2)\text{ is even for every }p
\]

and

\[
P_1P_2\text{ is an integer square}
\iff v_p(P_1)+v_p(P_2)\text{ is even for every }p.
\]

The sum and difference have the same parity. Thus conditions 1 and 2 are
equivalent.

Put \(D=\gcd(P_1,P_2)\), \(X=P_1/D\), and \(Y=P_2/D\). Then
\(\gcd(X,Y)=1\). If \(P_1P_2\) is a square, then

\[
P_1P_2=D^2XY
\]

shows that \(XY\) is a square. Since \(X\) and \(Y\) are coprime, every
prime exponent in each one is even. Hence \(X=A^2\) and \(Y=B^2\) for
coprime positive integers \(A,B\). Therefore

\[
P_1=DA^2,\qquad P_2=DB^2.
\]

If \(D\) were a square, both \(P_i\) would be squares, contrary to the
hypothesis. Thus \(D\) is not a square. Conversely, this displayed
decomposition makes \(P_1P_2=(DAB)^2\), so condition 3 implies condition
2. This proves all three conditions equivalent.

Since \(P_i\equiv1\pmod N\), each \(P_i\) is a unit modulo \(N\). Since
\(D\mid P_i\), \(D\) is also a unit. The equations \(P_1=DA^2\) and
\(P_2=DB^2\) then show that \(A\) and \(B\) are units. Reducing the two
equations modulo \(N\) gives

\[
A^2\equiv D^{-1}\equiv B^2\pmod N.
\]

The positive square root is

\[
R=\sqrt{P_1P_2}=DAB,
\qquad R^2\equiv1\pmod N.
\]

Using \(DB^2\equiv1\pmod N\),

\[
R-1\equiv DB(A-B)\pmod N,
\qquad
R+1\equiv DB(A+B)\pmod N.
\]

Multiplication by the unit \(DB\) does not change a gcd with \(N\).
Therefore

\[
\gcd(R-1,N)=\gcd(A-B,N),
\qquad
\gcd(R+1,N)=\gcd(A+B,N).
\]

Now assume \(N>1\) is odd. If \(R\not\equiv\pm1\pmod N\), neither gcd is
\(N\). Neither gcd can be 1: for example, if \(R-1\) were a unit modulo
\(N\), then
\((R-1)(R+1)\equiv0\pmod N\) would imply \(R+1\equiv0\pmod N\). The same
argument applies with the signs reversed. Thus both gcds are proper
nontrivial factors. If \(R\equiv1\pmod N\), the two gcds are \(N\) and 1;
if \(R\equiv-1\pmod N\), they are 1 and \(N\). Oddness is used through
\(\gcd(2,N)=1\). Finally, the two unit-multiplier congruences show

\[
R\equiv 1\iff A\equiv B,
\qquad
R\equiv-1\iff A\equiv-B
\pmod N.
\]

Hence the collision factors \(N\) exactly in the claimed case.

### Counterexample

For \(N=143=11\cdot13\), direct multiplication gives

\[
102\cdot136=13872=3\cdot68^2=1+97N,
\]

\[
125\cdot135=16875=3\cdot75^2=1+118N.
\]

Here \(D=3\), \(A=68\), \(B=75\), and \(\gcd(A,B)=1\). The induced root is

\[
R=3\cdot68\cdot75=15300\equiv142\equiv-1\pmod {143},
\]

because \(68+75=143\). Consequently

\[
\gcd(R-1,143)=1,
\qquad
\gcd(R+1,143)=143.
\]

The collision gives no proper factor.

## II. The first public state for \(N=2773\)

First,

\[
N=2773=47\cdot59,
\qquad
3\cdot43^2=5547=1+2N.
\]

The factorizations \(667=23\cdot29\) and
\(1334=2\cdot23\cdot29\), together with the following exact modular
values, certify the two orders:

| value | residue modulo 2773 |
|---|---:|
| \(3^{667}\) | 1 |
| \(3^{29}\) | 2656 |
| \(3^{23}\) | 753 |
| \(43^{1334}\) | 1 |
| \(43^{667}\) | 2772 |
| \(43^{58}\) | 237 |
| \(43^{46}\) | 847 |

For each prime divisor of the proposed order, the power obtained by
dividing the order by that prime is not 1. Hence

\[
\operatorname{ord}_N(3)=667,
\qquad
\operatorname{ord}_N(43)=1334.
\]

The first relation also gives \(3\equiv43^{-2}\pmod N\). Therefore

\[
H=\langle3,43\rangle=\langle43\rangle,
\qquad |H|=1334.
\]

Also \(43^{-1}=129\), because \(43\cdot129=5547\equiv1\pmod N\). Thus

\[
t=842\cdot43^{-1}\equiv842\cdot129\equiv471\pmod N,
\]

and

\[
471^2=221841=1+80N.
\]

The residue 471 is neither \(1\) nor \(2772=-1\). If \(842\) belonged to
\(H\), then \(t\) would belong to \(H\) and would be an order-two element
different from \(-1=43^{667}\). This is impossible because a cyclic group
has at most one element of order two. Therefore \(842\notin H\).

Finally,

\[
842\cdot2526=2126892=1+767N,
\]

so \(2526=842^{-1}\pmod N\). A subgroup contains an element exactly when
it contains its inverse. Hence \(2526\notin H\) as well.

## III. Alternative canonical presentation

Exact modular powering gives

\[
3^{99}\equiv2093\pmod N,
\qquad
2093\cdot43=89999\equiv1263\pmod N.
\]

Thus \(c=[3^{99}43]_N=1263\). Direct multiplication gives

\[
1263\cdot1684=2126892=1+767N,
\]

so the canonical inverse is \(w=1684\). Since \(c\in H\) and a subgroup
is closed under inversion, \(w\in H\). Moreover,

\[
cw=2126892=3\cdot842^2=842\cdot2526=P_2.
\]

Since \(P_1=3\cdot43^2\),

\[
\sqrt{P_1P_2}=3\cdot43\cdot842=108618.
\]

The exact gcds are

\[
\gcd(108617,2773)=47,
\qquad
\gcd(108619,2773)=59.
\]

Thus the alternative presentation stays inside \(H\), while its square
root gives the two proper factors.

## IV. Exact finite enumeration

Since \(2^{11}=2048<2773<4096=2^{12}\),
\(n=\lceil\log_2 2773\rceil=12\). The large menu therefore has
\((n^2+1)^2=145^2=21025\) pairs.

I used the following exact-integer selector. The selection loop uses only
\(N\), \(P_1\), the public bases 3 and 43, modular arithmetic, `isqrt`, and
`gcd`. It does not use either target endpoint or either factor.

```python
from math import gcd, isqrt

N = 2773
P1 = 3 * 43**2

def scan(L):
    seen = set()
    hits = []
    pair_ordinal = 0
    for s in range(2 * L + 1):
        for a in range(max(0, s - L), min(L, s) + 1):
            b = s - a
            pair_ordinal += 1
            c = pow(3, a, N) * pow(43, b, N) % N
            if c in seen:
                continue
            seen.add(c)
            w = pow(c, -1, N)       # representative in 1,...,N-1
            P = c * w
            R = isqrt(P1 * P)
            if R * R == P1 * P:
                hits.append((pair_ordinal, len(seen), a, b,
                             c, w, P, R,
                             gcd(R - 1, N), gcd(R + 1, N)))
    return pair_ordinal, len(seen), hits
```

For \(L=144\), this returns 21025 pairs, 433 first-occurrence residues,
and exactly these five hits:

| pair ord. | unique ord. | \((a,b)\) | \(c\) | \(w\) | \(P\) | \(R\) | gcds |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 2 | (0,1) | 43 | 129 | 5547 | 5547 | (2773,1) |
| 3 | 3 | (1,0) | 3 | 1849 | 5547 | 5547 | (2773,1) |
| 4 | 4 | (0,2) | 1849 | 3 | 5547 | 5547 | (2773,1) |
| 5 | 5 | (1,1) | 129 | 43 | 5547 | 5547 | (2773,1) |
| 5150 | 299 | (99,1) | 1263 | 1684 | 2126892 | 108618 | (47,59) |

The unique-residue counts also have a direct check. Since
\(3\equiv43^{-2}\), a pair has residue \(43^{\,b-2a}\). For
\(0\le a,b\le144\), the integer \(b-2a\) takes every value from \(-288\)
through 144. This interval has 433 values, and its width is less than
\(\operatorname{ord}_N(43)=1334\), so distinct exponents in the interval
give distinct residues. The same argument for \(0\le a,b\le12\) gives
all 37 exponents from \(-24\) through 12.

The table proves that four hits reproduce \(P_1\), and that the first
distinct useful hit is \((99,1)\). Its pair ordinal can also be checked
directly: the sums 0 through 99 contribute

\[
1+2+\cdots+100=5050
\]

pairs, and \((99,1)\) is the 100th pair at sum 100. Its ordinal is
\(5050+100=5150\). Exact first-occurrence tracking gives unique ordinal
299. Explicitly, sums at most 99 have exponent set
\(\{-198\}\cup[-196,99]\), which has 297 elements. At sum 100, the pair
\((0,100)\) adds exponent 100. Pairs \(a=1,\ldots,98\) add no new
exponent, and \((99,1)\) adds the previously missing exponent \(-197\).

For \(L=n=12\), the same code returns 169 pairs, 37 first-occurrence
residues, and only the first four rows of the table. Thus every hit has
\(P=P_1\), and there is no distinct or useful hit.

### Raw monomials

The inequalities

\[
3^7<N<3^8,
\qquad
43^2<N<43^3
\]

give exactly the following 12 monomials below \(N\), after excluding 1:

\[
3,9,27,81,243,729,2187,
43,129,387,1161,1849.
\]

Applying the same canonical-inverse and exact-square test gives hits only
for

\[
c\in\{3,43,129,1849\}.
\]

All four have \(cw=5547=P_1\). None of the other eight is a same-class
hit. More explicitly, the other canonical relation values and their
squarefree kernels (the products of the primes having odd exponent) are

| residues \(c\) | relation value \(cw\) | squarefree kernel |
|---|---:|---:|
| 9 | 22185 | 2465 |
| 27, 81, 243 | 47142 | 582 |
| 387, 729, 1161 | 720981 | 989 |
| 2187 | 2742498 | 418 |

The squarefree kernel of \(P_1=3\cdot43^2\) is 3, so none of these values
has its square class. Thus no raw monomial gives a distinct useful
collision.

### Complete subgroup check

Since \(H=\langle43\rangle\) has order 1334, enumerating
\(43^k\pmod N\) for \(0\le k<1334\) is a complete scan with no repeated
residue. The same exact test gives:

| \(k\) | \(c=43^k\bmod N\) | \(w\) | \(P=cw\) | gcds |
|---:|---:|---:|---:|---:|
| 1 | 43 | 129 | 5547 | (2773,1) |
| 2 | 1849 | 3 | 5547 | (2773,1) |
| 197 | 1684 | 1263 | 2126892 | (47,59) |
| 1137 | 1263 | 1684 | 2126892 | (47,59) |
| 1332 | 3 | 1849 | 5547 | (2773,1) |
| 1333 | 129 | 43 | 5547 | (2773,1) |

There are six same-class residues. Four reproduce \(P_1\). The two new
useful residues are one inverse pair and give one distinct relation value.
Therefore the exact densities are

\[
\frac{6}{1334}=\frac{3}{667},
\qquad
\frac{2}{1334}=\frac{1}{667}.
\]

## Scope

Part I is an elementary statement for positive relation values and an odd
modulus \(N>1\). Parts II--IV establish only exact facts about \(N=2773\).
The \(145^2\)-pair menu is public and polynomial in the 12-bit input length
for this instance, but its successful bound was post-selected after a
complete subgroup scan. The checks do not imply success on other inputs,
an inverse-polynomial density theorem, or an all-input polynomial-time
factoring algorithm. The factor extraction is exactly the standard
congruence-of-squares gcd step.
