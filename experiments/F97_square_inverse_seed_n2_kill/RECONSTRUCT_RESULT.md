# F97 proof-blind reconstruction result

## Verdict: PASS

Every arithmetic, group, enumeration, null, positive-control, and scope
claim in `RECONSTRUCT_STATEMENT.md` is correct.  The reconstruction below
uses no other F97 artifact.

## 1. Family arithmetic and the fixed input: PASS

For odd (x), (3x^2-1) is even, so

\[
N_x=\frac{3x^2-1}{2}\in\mathbb Z,
\qquad 3x^2=1+2N_x.
\]

Thus (3x^2\equiv1\pmod {N_x}).  In particular, (3) is a unit modulo
(N_x).  If (1\le x^2<N_x), then (x^2) is already the canonical
positive representative of (3^{-1}\pmod {N_x}).  An exact square-root
test on that representative returns (|x|), and the inputs considered
here have positive (x).

At (x=13),

\[
N=\frac{3\cdot169-1}{2}=253=11\cdot23,
\]

and

\[
3\cdot169=507=1+2\cdot253.
\]

Since (0<169<253), the canonical inverse is (169=13^2), and the old
relation value is (P_1=507).

For the stated certificate,

\[
g=\gcd(10,22)=2,
\quad A=10/2=5,
\quad B=22/2=11.
\]

Also (AB=55=5\cdot11), while
(N-1=252=2^2\cdot3^2\cdot7).  Hence

\[
\gcd(AB,N-1)=\gcd(55,252)=1.
\]

## 2. Menu size, group, and coverage: PASS

Because (2^7<254\le2^8),

\[
n=\lceil\log_2(254)\rceil=8,
\qquad n^2=64.
\]

There are independently (65) choices for each of (a,b\in[0,64]), so
the stated traversal has (65^2=4225) pairs.  Sorting these pairs does not
change that count.

The order of (13) modulo (253) follows from the two prime factors.  Modulo
(11), (13\equiv2), (2^5\equiv-1), and the order is (10).  Modulo
(23),

\[
13^2\equiv8,
\quad 13^4\equiv18,
\quad 13^8\equiv2,
\quad 13^{11}\equiv2\cdot8\cdot13\equiv1.
\]

Since (13\not\equiv1\pmod {23}) and (11) is prime, the order modulo
(23) is (11).  The Chinese remainder theorem therefore gives

\[
\operatorname{ord}_{253}(13)=\operatorname{lcm}(10,11)=110.
\]

The identity (3\cdot13^2=1+2N) also gives

\[
3\equiv13^{-2}\pmod N.
\]

Consequently

\[
H=\langle3,13\rangle=\langle13\rangle,
\qquad |H|=110,
\]

and every menu residue has the form

\[
3^a13^b\equiv13^{,b-2a}\pmod N.
\]

For fixed (a), the integer exponent (b-2a) runs through
([-2a,64-2a]).  As (a) runs from (0) to (64), these overlapping
intervals have union ([-128,64]).  This union contains the (110)
consecutive integers ([-45,64]), which form a complete residue system
modulo the order (110).  The menu therefore contains every element of
(H), and contains nothing outside (H).  It visits exactly (110)
distinct residues.

## 3. Exhaustive null certificate: PASS

Let (c\in H) be represented in ([1,252]), and let its canonical positive
inverse be (w\in[1,252]).  Then

\[
P=cw\equiv1\pmod {253},
\qquad 1\le P\le252^2=63504.
\]

Because (P_1=3\cdot13^2), the product (P_1P) is a square if and only if

\[
P=3t^2
\]

for a positive integer (t).  One direct proof is to write
(P_1P=y^2): then (13\mid y), so (y=13u), (u^2=3P), (3\mid u),
and (u=3t).  The converse is immediate.

The size bound gives (t\le145), since (145^2\le63504/3<146^2).  The
relation congruence gives

\[
3t^2\equiv1\pmod {253}
\quad\Longleftrightarrow\quad
t^2\equiv169\pmod {253}.
\]

Modulo (11), the roots are (t\equiv\pm2); modulo (23), they are
(t\equiv\pm13).  Combining the four sign choices by CRT gives exactly

\[
t\equiv13,79,174,240\pmod {253}.
\]

Only (13) and (79) lie in the required interval (1\le t\le145).
Thus the only possible canonical relation values in the square class of
(P_1) are

\[
3\cdot13^2=507,
\qquad
3\cdot79^2=18723.
\]

The factor pairs whose two entries are at most (252) are

\[
507:\ (3,169),(13,39),(39,13),(169,3),
\]

and

\[
18723:\ (79,237),(237,79).
\]

The first four all reproduce the ignored old value (P=P_1).  The two
residues for the distinct value do not lie in (H).  Indeed,
(79\equiv10\pmod {23}), and

\[
10^2\equiv8,
\quad10^4\equiv18,
\quad10^8\equiv2,
\quad10^{11}\equiv2\cdot8\cdot10\equiv-1\pmod {23}.
\]

Every element of the projection
(\langle13\rangle\subset(\mathbb Z/23\mathbb Z)^\times), which has order
(11), has eleventh power (1).  Hence (79\notin H).  Also

\[
79\cdot237=18723=74\cdot253+1,
\]

so (237=79^{-1}\pmod {253}); subgroup closure under inversion shows
(237\notin H) as well.

Therefore no residue of (H) produces a distinct canonical relation value
whose product with (P_1) is a square.  Since the menu covers all of (H),
increasing its exponent bound cannot add such a residue.  There is no
distinct square closure to classify as either a global-sign root or a useful
root.

## 4. Increasing-order claim: PASS

Direct substitution gives

| (x) | (N_x=(3x^2-1)/2) | status |
|---:|---:|:---|
| 3 | 13 | prime |
| 5 | 37 | prime |
| 7 | 73 | prime |
| 9 | 121 | (11^2) |
| 11 | 181 | prime |
| 13 | 253 | (11\cdot23) |

Trial division by primes up to the square root proves the four primality
claims: use (2,3) for (13); (2,3,5) for (37); (2,3,5,7) for
(73); and (2,3,5,7,11,13) for (181).  None divides its respective
number.  The preceding positive odd value (x=1) gives (N_1=1), not a
semiprime.  Hence (x=13) is the first increasing positive odd (x) for
which (N_x) is a product of two distinct primes.  The certificate in
Section 1 verifies the stated stable condition.

## 5. Positive control and firstness: PASS

At (x=43),

\[
N=\frac{3\cdot43^2-1}{2}=2773=47\cdot59,
\qquad P_1=3\cdot43^2=5547=1+2N.
\]

Since (2^{11}<2774\le2^{12}), (n=12) and the bound is (n^2=144).
Repeated squaring modulo (2773) gives

| exponent (e) | 1 | 2 | 4 | 8 | 16 | 32 | 64 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| (3^e\bmod2773) | 3 | 9 | 81 | 1015 | 1442 | 2387 | 2027 |

Multiplying the entries for (99=64+32+2+1) gives
(3^{99}\equiv2093\pmod {2773}).  Therefore

\[
c=[3^{99}43]_N=1263.
\]

The proposed inverse is canonical because (0<1684<N) and

\[
1263\cdot1684=2126892=767\cdot2773+1.
\]

Thus (w=1684) and (P=2126892=3\cdot842^2).  The exact induced root is

\[
s=\sqrt{P_1P}=3\cdot43\cdot842=108618.
\]

Since (s\equiv471\pmod {2773}),

\[
\gcd(s-1,N)=\gcd(470,47\cdot59)=47,
\]

and

\[
\gcd(s+1,N)=\gcd(472,47\cdot59)=59,
\]

using (470=10\cdot47) and (472=8\cdot59).

The following complete, deterministic enumeration independently certifies
both null search and positive-control firstness.  It reads no file.  Pair
ordinal (0) is ((0,0)).  Residues and then relation values are deduplicated
exactly as stated.

```python
from math import gcd, isqrt

def ordered_pairs(bound):
    for total in range(2 * bound + 1):
        lo = max(0, total - bound)
        hi = min(bound, total)
        for a in range(lo, hi + 1):
            yield a, total - a

def scan(x, bound):
    N = (3 * x * x - 1) // 2
    P1 = 3 * x * x
    residues = set()
    values = set()
    square_hits = []

    for ordinal, (a, b) in enumerate(ordered_pairs(bound)):
        c = (pow(3, a, N) * pow(x, b, N)) % N
        if c in residues:
            continue
        residues.add(c)

        w = pow(c, -1, N)
        P = c * w
        if P == P1 or P in values:
            continue
        values.add(P)

        s = isqrt(P1 * P)
        if s * s == P1 * P:
            square_hits.append(
                (ordinal, a, b, c, w, P, s,
                 gcd(s - 1, N), gcd(s + 1, N))
            )

    return len(residues), len(values), square_hits

print(scan(13, 64))
print(scan(43, 144))
```

Its exact output is

```text
(110, 33, [])
(433, 225, [(5149, 99, 1, 1263, 1684, 2126892, 108618, 47, 59)])
```

Thus the F97 menu has no distinct square-compatible value at all.  In the
positive control, the only distinct square-compatible value in the complete
menu occurs at ((99,1)), and its two gcds are nontrivial.  In particular,
it is the first useful distinct hit in the required traversal order.  Its
zero-based raw-pair ordinal is (5149), so every earlier pair was tested.

## 6. Scope: PASS

The menu calculation above uses only (N), the blocks (3,x), and the
fixed exponent bound and traversal rule.  Neither the factorization of
(253) nor that of (2773) selects a menu residue.  Those factorizations
are used only in this independent certificate to establish group facts,
primality status, and the returned gcds.

The (x=13) input satisfies the square-inverse construction and the stable
arithmetic certificate, while its complete source group (H) has no useful
distinct one-step closure.  One counterexample is sufficient to refute the
universal isolated closure claim.

Nothing in the proof analyzes a refined block presentation, more than one
seed, retention of more than one square class, a source outside (H), or a
different decoder.  Also

\[
11<n^2=64.
\]

Therefore this finite counterexample does not refute a hybrid algorithm
that first removes polynomially bounded small factors.  A single certified
input also supplies neither an asymptotic failure frequency nor a general
lower bound.  These limitations match the stated scope.
