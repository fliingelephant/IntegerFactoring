# F261-D01 exact algebra — beta-two prefixes filter centered-carry banks

## Scope

This file contains proof-only statements.  The finite search in this packet
is separate evidence.  No statement here computes a beta-two carry prefix or
proves an all-input factoring algorithm.

Let

\[
N=pq,\qquad p<q<2p,
\]

where `p,q` are distinct odd primes.  Put

\[
n=\lceil\log _2(N+1)\rceil,\qquad
B=2^m,\quad m=\lfloor n/2\rfloor,
\]

and assume the zero-defect condition

\[
B\mid N-1,\qquad H=(N-1)/B.
\]

This is the F236 source family.  It is not every balanced semiprime.

## 1. The two exact nearest centers

For every integer `u>=1`, use round-half-up literally:

\[
K_p=\left\lfloor{up+B/2\over B}\right\rfloor,
\qquad
K_q=\left\lfloor{uq+B/2\over B}\right\rfloor.
\]

Define

\[
x=up-K_pB,\qquad y=uq-K_qB.
\]

Then

\[
-B/2\le x,y<B/2.
\]

Half ties can occur.  For `m>=2` and odd `p`, a tie in `up/B` occurs
exactly when `u` is congruent to `B/2` modulo `B`.  The floor formula sends
the tie to residue `-B/2`.  This packet never replaces `(K_p,K_q)` by one
forced common center.

This distinction repairs the failed F236/X85 statistic.  On its frozen
`B=2^22`, `u=1` audit, the exact nearest-center extremum was
`|c|=520969` at

```text
p=3105539, q=6201259, Kp=1, Kq=1, c=-520969.
```

The larger reported value `522514` was a forced-common-center value at

```text
p=3162347, q=6318019, forced K=1, forced c=-522514.
```

The two exact nearest centers there are `(Kp,Kq)=(1,2)` and give
`c=509443`.  These rows remain exact regression witnesses.  The smallest
half-tie regression row in this packet is `p=101,q=109,B=128,u=64`; the
literal rule above sends both residues to `-64`.

Expanding `u^2N=(K_pB+x)(K_qB+y)` modulo `B` gives

\[
c={xy-u^2\over B}\in\mathbb Z.                       \tag{1}
\]

Division of the same identity by `B` gives

\[
u^2H=K_pK_qB+K_py+K_qx+c.
\]

Consequently

\[
T:=K_pq+K_qp
 ={u^2H+K_pK_qB-c\over u}\in\mathbb Z.               \tag{2}
\]

The hidden factor `p` is a root of

\[
K_qX^2-TX+K_pN=0,                                    \tag{3}
\]

and

\[
T^2-4K_pK_qN=(K_pq-K_qp)^2.                          \tag{4}
\]

Thus every guessed tuple is verified by exact integer arithmetic.  Require
the numerator in (2) to be divisible by `u`, require a nonnegative square
discriminant, test both integral roots, and accept only a proper exact
divisor of `N`.

For completeness outside the canonical source bank, if `K_q=0` then (3)
is linear: test `X=K_pN/T` when `T` is nonzero and divides `K_pN`.
If `K_p=K_q=0`, reject the tuple because the equation contains no factor
information.  In the balanced source itself, `p>B/2` and `q>B/2`, so the
true centers are positive and these endpoints cannot occur.

## 2. Exact public center intervals

The balance promise gives

\[
\sqrt{N/2}<p<\sqrt N<q<\sqrt{2N}.
\]

Define the public integer bounds

\[
p_- =\left\lfloor\sqrt{\lfloor N/2\rfloor}\right\rfloor+1,
\quad p_+=\lfloor\sqrt N\rfloor,
\]

\[
q_-=p_++1,
\quad q_+=\left\lfloor\sqrt{2N-1}\right\rfloor.
\]

Monotonicity of round-half-up puts the true centers in the exact public
intervals

\[
\left\lfloor{up_-+B/2\over B}\right\rfloor
 \le K_p\le
\left\lfloor{up_++B/2\over B}\right\rfloor,
\]

\[
\left\lfloor{uq_-+B/2\over B}\right\rfloor
 \le K_q\le
\left\lfloor{uq_++B/2\over B}\right\rfloor.          \tag{5}
\]

Each interval has `O(u)` entries.  The coarser range `1<=K_p,K_q<=3u`
also follows, but the decoder and the scan use (5).

## 3. A known dyadic factor prefix filters the carry bank

Let

\[
R=2^t\mid B,
\qquad a=p\bmod R,
\qquad b=q\bmod R=N a^{-1}\bmod R.                   \tag{6}
\]

The values `a,b` are operational data once one beta-two prefix is supplied.
They do not use the hidden labels after `a` is known.

Reducing (2) before division gives

\[
T\equiv K_pb+K_qa\pmod R.                            \tag{7}
\]

Equivalently,

\[
c\equiv
u^2H+K_pK_qB-u(K_pb+K_qa)
\pmod {uR}.                                           \tag{8}
\]

The `K_pK_qB` term in (8) is essential.  It cannot in general be deleted
modulo `uR`.

For a carry cap `|c|<=C`, put

\[
A=u^2H+K_pK_qB.
\]

Instead of enumerating signed carries, enumerate the integers

\[
\left\lceil{A-C\over u}\right\rceil
\le T\le
\left\lfloor{A+C\over u}\right\rfloor,
\qquad
T\equiv K_pb+K_qa\pmod R,                            \tag{9}
\]

and reconstruct `c=A-uT`.  This makes the division in (2) automatic and
handles negative carries without a language-dependent remainder convention.
Every true tuple survives (9).

One residue class modulo `R` has at most

\[
1+\left\lfloor{2C\over uR}\right\rfloor             \tag{10}
\]

members in the interval.  Combining (5), (9), and (10), the complete
verified bank through `u<=U` contains at most

\[
O\!\left(U^3+{CU^2\over R}\right)                   \tag{11}
\]

candidates, times polynomial-bit exact arithmetic.  With no prefix,
`R=1`, integrality alone already sharpens the old crude `O(CU^3)` count to
`O(U^3+CU^2)`.  If `uR>2C`, each fixed center pair has at most one candidate
`T`.

This theorem improves candidate enumeration.  It does not make the true
carry small and does not supply `a`.  If the known-residue terminal already
applies to `R`, any factorization must be credited to that terminal rather
than to this bank.

## 4. One-dimensional inverse-quotient representation

Assume `R>=2` and `u` is odd.  Then the true `x` is odd and hence a unit
modulo `B`.  From (1),

\[
y\equiv u^2x^{-1}\pmod B.                            \tag{12}
\]

Also `x` is congruent to `ua` modulo `R`.  Therefore write

\[
x=ua+Rz,
\qquad -B/2\le x<B/2,                                \tag{13}
\]

take `y(x)` to be the unique round-half-up centered representative of
`u^2x^{-1} mod B`, and define

\[
c(z)={x\,y(x)-u^2\over B}.                           \tag{14}
\]

Equations (12)--(14) reduce the hidden pair of centered residues to a
one-dimensional dyadic inverse-quotient map with exactly `B/R` candidate
values of `z`.  The true point is present.  Exhausting this map costs
`B/R`, which is still exponential at a quarter-size prefix.  Sampling its
fibres is therefore diagnostic unless a separate theorem makes the true
point accessible or proves useful density.

## 5. Verification boundary

All identities above are elementary integer identities.  They prove no
inverse-QP law for `|c_u|`, no useful distribution of (14), and no public
surrogate for the two true centers.  F261-D01 searches for such patterns on
frozen finite cohorts.  Its hidden-label features are marked `oracle` and
cannot be used as algorithmic inputs.
