# Exact composition, summed doubling, and its retained precision

**Family:** route:F31

This continuation tests composition rather than reblocking. It derives the
exact carry cocycle, retains every weighted binomial term, and tests the
backwards-doubling proposal for h_c(x)=x/(1+cx). The result is a precise
third-digit requirement for a pairwise moment, not an assertion that all
composition identities fail.

## 1. Carry composition at canonical or shifted lifts

Write

    f(x)=(a x+b)/(c x+d), g(y)=(e y+f0)/(h y+i),

with c,h even and a,d,e,i odd. Both maps permute residues modulo L=2^s.
Let y,z be chosen integer lifts of f(x),g(y), and define

    q_f=[(cx+d)y-(ax+b)]/L,
    q_g=[(hy+i)z-(ey+f0)]/L.

With the ordinary matrix product defining g composed with f, direct
cross multiplication gives exactly

    q_(g f)=(cx+d)q_g+(e-hz)q_f.                            (1)

The identity holds equally for shifted fundamental representatives; no
canonicalization error is hidden. Set A=cx+d and B=e-hz. Then

    binom(q_(g f),2)
      = A squared binom(q_g,2)+B squared binom(q_f,2)
        +AB q_f q_g+binom(A,2)q_g+binom(B,2)q_f.             (2)

All five terms must be summed. Even c,h do not make AB even; it is a unit.
The first two terms are weighted binomial-carry sums, not automatically
the unweighted B_f and B_g. Equation (2) is the actual proposed cocycle
interface before any further cancellation.

## 2. Which higher-coordinate terms occur

Before multiplication by AB, the product L squared q_f q_g has only two
terms involving all three coordinates x,y,z:

    c h x y squared z +(c i-a h)xyz.                        (3)

All its other terms involve at most two coordinates. Thus (3)'s coefficient
valuations are v2(c)+v2(h) and v2(ci-ah), respectively. For a self-composition
of h_c the second coefficient vanishes identically, but the first is c squared.
There is real algebraic cancellation; merely pointing to a third variable
would miss it.

To recover q_f q_g modulo L by expanding its numerator requires that
numerator modulo L cubed. A moment supplied only modulo L squared is
enough for a term of (3) only if its coefficient is divisible by L.
For h_c self-composition this condition is 2v2(c)>=s. Pair terms with
unit coefficients still require their own additional precision or an
independent cancellation. The outer factor AB in (2) does not improve
the overall unit coefficient.

The exact controls below show that the *summed* weighted cross term also
need not vanish. This is stronger evidence than the pointwise unit test,
but still not a general impossibility statement.

## 3. Actual original-input factorization into maps

For the original modulus M=2L and n=(N-1)/2, the first quotient graph is

    F_N(x)=(n-x)/(1+2x)
          = translation_n composed with scaling_(-N)
            composed with h_2.                            (4)

The equality is an exact matrix identity because 2n-N=-1. Affine pieces
have ordinary-floor interpretations, but their composition with h_2 in
(2) still includes its cross-carry correlations. The pilot includes these
two actual composition steps with the same original N; N lies in [16L,32L),
so M=2L is the largest power of two at most N/8.

More generally, a map with odd d decomposes 2-adically into a translation
b/d, scaling (ad-bc)/d squared, and h_(c/d). This algebraic decomposition
does not by itself evaluate the binomial carry of the composition.

## 4. Summed doubling cancellation

For h_c let y=h_c(x), z=h_c(y)=h_(2c)(x), using canonical lifts. Equation
(1) specializes to

    q_(2c)=q_c(x)+q_c(y)+(c/L)[2xz-xy-yz].                  (5)

The numerator in brackets is divisible by L. This removes its apparent
three-coordinate term exactly. Since y permutes the residues, write

    S_c=sum_x x h_c(x), Q_c=sum_x q_c(x).

The marginal sums give an even simpler exact identity:

    Q_c=c S_c/L.                                          (6)

Summing (5) now yields

    Q_(2c)-2Q_c=(2c/L)(S_(2c)-S_c).                        (7)

Equation (7) follows identically from (6). Therefore, if its right side
is claimed computable from P240, the precision of S_c is decisive; the
equation is not independent of that moment.

P240 computes S_c modulo L squared. Put r=v2(c)>=1. Using only that
precision gives the correction in (7) modulo 2^(s+r+1). After dividing
by two to solve backwards, Q_c is known only modulo 2^(s+r), even if
Q_(2c) were supplied exactly. (Using the uncombined form of (5) would
lose the extra factor of two visible in (7).) This is a legitimate
precision gain over Q_c modulo L when r>0, but it remains far below the
precision required by the binomial norm relation below. It is also exactly
the precision already obtained directly from (6) and S_c modulo L squared;
doubling has supplied no additional independent digit.

At c=L the canonical map is the identity and q_c=x squared, so the
backwards-doubling proposal has a polynomially computable endpoint. The
issue is not lack of a base case.

## 5. A non-enumerative norm reduction identifies the exact missing digit

Now take c=2^r, 1<=r<=s, which includes the entire doubling path from
h_2 to h_L. Let m=Lc. Pointwise,

    (1+cx)(1-cy)=1-Lc q_c.

Since y is a permutation,

    R_c=product_x(1-Lc q_c)=product_(0<=x<L)(1-c squared x squared). (8)

Let Sbar_c be S_c modulo L squared in [0,L squared), and write

    t_c=(S_c-Sbar_c)/L squared,
    qbar_c=c Sbar_c/L.

The latter is an integer, by (6). Expand (8) modulo m squared L.
Terms of order at least three vanish. Since m/2 is divisible by L,
binom(qbar_c+m t_c,2)=binom(qbar_c,2) modulo L. Consequently

    E_c=[R_c-1+m qbar_c-m squared binom(qbar_c,2)]/m squared modL
       =-t_c-B_c modL,
    B_c=-t_c-E_c modL.                                    (9)

The division in (9) is exact, with work precision 3s+2r bits.
The norm is non-enumerative: expand (8) using elementary symmetric
coefficients of x squared. Only j<(3s+2r)/(2r) can contribute; these
coefficients come from ordinary power sums and exact Newton identities.
Together with P240 this computes E_c in polynomial bit time.

Formula (9) is stronger than a raw cross-term observation: it assembles
all weighted and cross terms into one pairwise moment digit. However,
that is precisely the third L-adic digit of S_c. Its required precision
is L cubed, independent of r. Increasing the evenness of c reduces the
norm's coefficient count, but does not reduce this missing digit.

Trying to use B_(2c) and (7) to solve for B_c must therefore compute the
pair correction at the precision containing S_c modulo L cubed. Calling
P240 at its established L-squared precision is insufficient. The summed
identity itself does not supply the extra digit, since (7) is already (6).
No extension of P240 to L cubed is assumed.

## 6. Relation to the inverse-coordinate gradient

On odd x, conjugating h_c by inversion turns it into translation by c.
With z x=1+L a and (z+c)y=1+L b, direct subtraction gives

    q_c=x b-y a,
    q_c/(xy)=b/y-a/x.

This is the exact gradient identity supplied by the root. Squaring it
retains the adjacent product of the two inverse-carry values. Equations
(5)-(9) show one precise integrated consequence and its precision, but
do not prove that this translated carry correlation lacks another closure.
That weighted arithmetic-progression route remains open.

## 7. Exact evidence

`COMPOSITION.py` checked 35 map pairs and 10,160 exact point identities.
It includes h_2 self-composition, h_2 with h_4, high-valuation self maps,
and the two actual original-input steps in (4). All identities passed.
For L=64,c=2, the five terms of (2), after summation modulo L, are

    12,12,46,17,17,

and B_(h4)=40. Omitting the summed cross term 46 gives the wrong result.
The cross term has valuation one, so even c has not suppressed it to the
required modulus. In the actual N=259,L=16 scaling step the summed cross
term is 3 modulo16, which is odd.

`H_C_NORM.py` uses the non-enumerative P240 bank and norm expansion to
compute E_c, then audits the unknown third digit by enumeration. All 52
cases, s=3 through10 and r=1 through s, matched (6)-(9). At L=64,c=2,

    Sbar=2464, t=14, E=54, B=60.

Discarding t would give 10. It failed in all52 controls, including the
identity endpoint, where t is easy to compute but is still nonzero.

The composition pilot took 0.011 seconds at 17,350,656 peak RSS bytes;
the norm pilot took 0.017 seconds at 17,235,968 bytes. All arithmetic
checks are exact. Sources, outputs, and logs are retained separately.
The established result is the exact composition law and this tested
precision boundary for backwards doubling, not an evaluator for shifted
B or a general no-composition theorem.
