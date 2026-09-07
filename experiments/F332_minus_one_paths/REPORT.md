# F332 public `a=-1` paths

**Family:** route:F31

Status: bounded implementation and finite comparison passed. This fixed public
input has no hidden-root or Rabin interpretation, and no path-length theorem is
claimed.

## Outcome

F332 implements the F330 reflection formula and the positive adjacent P/Q
block kernel for `N=1 mod 4`, with `a=N-1`. Reflection is capped in fine F
calls. The compressed kernel is capped in block iterations; a P block covers
one fine call and a Q block covers two. Equal numeric caps therefore represent
different path coverage.

At the initial cap 8,192, both methods completed on the 20- and 28-bit inputs.
Both remained censored on the other five inputs. Fresh 262,144-cap jobs then
completed both methods at 36 bits and completed reflection on one 44-bit input.
The remaining extended paths stayed censored.

| Input | Offline root label | Reflection final result | Fine calls | Adjacent-block final result | Blocks | Equivalent fine calls |
|---|---|---|---:|---|---:|---:|
| `b20_i1` | impossible, Blum | factor 907 | 632 | factor 919 | 700 | 1,042 |
| `b28_i1` | possible | factor 13,789 | 4,185 | factor 12,373 | 6,695 | 9,999 |
| `b36_i0` | impossible, Blum | factor 218,987 | 49,481 | factor 215,051 | 148,248 | 222,070 |
| `b44_i0` | possible | censor | 262,144 | censor | 262,144 | 393,319 |
| `b44_i1` | impossible, Blum | factor 3,827,143 | 154,242 | censor | 262,144 | 392,874 |
| `b60_i1` | possible | censor | 262,144 | censor | 262,144 | 392,733 |
| `b92_i0` | impossible, Blum | censor | 262,144 | censor | 262,144 | 393,098 |

All four reflection factors and all three adjacent factors were verified by
exact divisibility. No public run returned a square root of `-1`. Offline Blum
labels were used only to confirm that roots are impossible on four inputs.

## Exact controls and the lift counterexample

For every `N=1 mod 4` through 101, including primes and composites, the direct
reflection formula and direct fine adjacent formula agree with frozen F326 at
every visited coordinate, branch, stopping call, and output. The compressed
kernel agrees with the fine adjacent path in equivalent fine calls, terminal
coordinate, and output class. This gives 75 complete path comparisons over 25
moduli. Root values are compared by their square and conjugated coordinate,
because the kernel and F326 can choose opposite integer representatives.

For `N=61`, the kernel verifies the requested itinerary

    P, P, Q, Q, P, Q

with positive lifts

    (2,1), (3,2), (5,3), (3,8), (8,11), (19,8), (8,27)

and even modular coordinates

    2, 32, 22, 8, 34, 10, 50.

The first norm exceeding `2N` is `8^2+11^2=185>122` after the fourth update.
The terminal norm is `8^2+27^2=793=13N`, and 50 is a square root of `-1`
modulo 61. A smaller-modulus witness also occurs at `N=53`: after four updates,
`(7,11)` has norm 170, exceeding `2N=106`. The exhaustive range found no
witness before update four. Further first witnesses occur at `N=89,97,101`.
These observations refute only the proposed `2N` lift-size bound.

The exact fine-adjacent controls also enforce the forbidden triple identical
negative-inverse branch. All Q intermediate fixed and special guards are
checked at their correct fine positions. No special-return guard was reached.

## Charged arithmetic and matrix words

The public solvers reuse current inverses and verified gcds. Their final gcd and
modular-inversion counts are:

| Input | Reflection gcd / inverse | Adjacent gcd / inverse | Reflection seconds | Adjacent seconds |
|---|---:|---:|---:|---:|
| `b20_i1` | 631 / 630 | 700 / 699 | 0.001 | 0.001 |
| `b28_i1` | 4,184 / 4,183 | 6,695 / 6,694 | 0.011 | 0.019 |
| `b36_i0` | 49,480 / 49,479 | 148,248 / 148,247 | 0.082 | 0.360 |
| `b44_i0` | 262,143 / 262,143 | 262,144 / 262,144 | 0.459 | 0.707 |
| `b44_i1` | 154,241 / 154,240 | 262,144 / 262,144 | 0.284 | 0.721 |
| `b60_i1` | 262,143 / 262,143 | 262,144 / 262,144 | 0.601 | 0.843 |
| `b92_i0` | 262,143 / 262,143 | 262,144 / 262,144 | 0.944 | 1.247 |

The terminal or capped matrix-word statistics are:

| Input | Reflection `+/-` | Max same `+/-` | Max alternating | Block `P/Q` | Max same `P/Q` | Max alternating |
|---|---:|---:|---:|---:|---:|---:|
| `b20_i1` | 316 / 314 | 10 / 8 | 11 | 359 / 340 | 9 / 8 | 14 |
| `b28_i1` | 2,057 / 2,126 | 16 / 18 | 10 | 3,392 / 3,302 | 17 / 12 | 12 |
| `b36_i0` | 24,765 / 24,714 | 14 / 15 | 17 | 74,427 / 73,820 | 15 / 16 | 15 |
| `b44_i0` | 131,197 / 130,946 | 19 / 18 | 21 | 130,970 / 131,174 | 19 / 17 | 18 |
| `b44_i1` | 76,870 / 77,370 | 15 / 18 | 20 | 131,415 / 130,729 | 18 / 15 | 18 |
| `b60_i1` | 130,898 / 131,245 | 15 / 19 | 18 | 131,556 / 130,588 | 17 / 15 | 18 |
| `b92_i0` | 130,819 / 131,324 | 17 / 16 | 19 | 131,191 / 130,953 | 19 / 15 | 18 |

These finite run lengths do not imply a distributional or worst-case bound.
In particular, near-balanced letter counts do not certify rapid absorption.

## Lift guard and root-pair postprocessing

Exact lift recording stops before a coordinate exceeds 4,096 bits. Reflection
first saturated between updates 3,897 and 3,952 on the retained long inputs;
the block lift saturated between updates 7,110 and 7,204. Modular traversal,
gcd tests, and word counters continued after saturation. No large diagnostic
integer was constructed.

When both methods return verified roots for one N, the outer postprocessor
computes one charged `gcd(c_adj-c_reflection,N)`. The pure method results remain
unchanged. The small-prime controls exercise seven global-opposite and five
same-root failures. Public runs produced no pair of roots, so this additional
factor attempt was not applicable and produced no factor. No independence or
uniformity of the two roots is assumed.

## Resources and scope

The exhaustive control took 0.003 seconds. Seven initial and five extended
jobs used 6.699 process seconds in total. The longest job took 2.193 seconds;
the largest numerical-job peak RSS was 28,393,472 bytes. Every job was
single-threaded and stayed below the 28-second internal, 30-second external,
and 512 MiB limits.

The result is a finite comparison at one fixed public radicand per modulus.
It supplies no random-square success claim, no lift-size theorem, and no
polynomial or quasipolynomial factoring bound.
