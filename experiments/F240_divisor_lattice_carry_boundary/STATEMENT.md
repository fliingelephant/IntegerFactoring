# F240 candidate — the factored `N-1` divisor lattice has an exact centered-carry escape and a sharp divisor-only P205 boundary

## Status and scope

This is a proof-only boundary for a distinct odd semiprime

\[
N=pq,\qquad p<q.
\]

Put

\[
n=\lceil\log_2(N+1)\rceil,\qquad
M=N-1=2K,
\]

and grant the complete recursive factorization of `K`.  Thus the complete
factorization and divisor lattice of `M` are public.  No computation is used
in this packet.

Define the P205 data

\[
d=\gcd(p-1,q-1),\qquad
s_p={p-1\over d},\qquad s_q={q-1\over d}.
\]

The theorem has four purposes.

1. It extends the centered-carry identity from one special radix to every
   divisor `B | M`.
2. It identifies the guaranteed zero-carry lattice point `B=d`, including
   the round-half-up offset when `d=2`.
3. It proves that the entire divisor lattice adds no P205 prime support if
   it is used only multiplicatively.
4. It isolates the still-open escape: select a useful divisor and recover
   one centered residue or both center indices from an additive carry
   relation.

This is not an all-input factoring algorithm.  It proves no
quasipolynomial divisor selector, centered-carry law, residual smoothness
law, or lower bound against algorithms outside the narrow grammar defined
below.

## Theorem A — generalized divisor-centered carry

Let `B` be any positive divisor of `M` and put

\[
H_B={M\over B}.
\]

Fix an integer `u>=1`.  With round-half-up centers, define

\[
a=\left\lfloor {up\over B}+{1\over2}\right\rfloor,
\qquad
b=\left\lfloor {uq\over B}+{1\over2}\right\rfloor,
\]

and

\[
x=up-aB,\qquad y=uq-bB.
\]

Then

\[
-{B\over2}\le x,y<{B\over2}.
\]

The centered carry

\[
\boxed{c={xy-u^2\over B}}
\tag{1}
\]

is an integer.  Moreover

\[
\boxed{
T:=aq+bp={u^2H_B+abB-c\over u}
}
\tag{2}
\]

is an integer, `p` is a root of

\[
bX^2-TX+aN=0,
\tag{3}
\]

and

\[
T^2-4abN=(aq-bp)^2.
\tag{4}
\]

Thus a public guessed tuple `(B,u,a,b,c)` with `B | M` is verified by (2),
an integer-square test in (4), candidate recovery from (3), and exact
division into `N`.  When `b=0`, equation (3) is treated as a linear equation;
the usual quadratic formula is used only when `b!=0`.  False tuples are
harmless.

The exact short-offset implication is

\[
|x|\le X
\quad\Longrightarrow\quad
|c|\le {X\over2}+{u^2\over B}.
\tag{5}
\]

Conversely,

\[
|c|\le C
\quad\Longrightarrow\quad
\min(|x|,|y|)\le\sqrt{u^2+CB}.
\tag{6}
\]

Equation (6) is only a square-root-scale conclusion.  A short carry does
not by itself give a numerical-quasipolynomial centered residue when `B`
has exponentially large numerical value.

## Theorem B — the guaranteed zero-carry point is the P205 residual point

The hidden common divisor `d` is a divisor of `M`.  At `B=d` and `u=1`, the
centered carry is always zero.

- If `d>=4`, then

  \[
  a=s_p,\qquad b=s_q,qquad x=y=1,qquad c=0.
  \tag{7}
  \]

- If `d=2`, the declared round-half-up convention gives

  \[
  a=s_p+1,\qquad b=s_q+1,qquad x=y=-1,qquad c=0.
  \tag{8}
  \]

Thus the complete divisor lattice always contains a perfect carry-zero
radix.  But its two hidden center indices are exactly the two P205 residuals,
up to the forced additive one in the sole tie case `d=2`.  Carry zero alone
does not locate `d` or make either center small.

For any public bound `R>=1`,

\[
s_p\le R
\quad\Longleftrightarrow\quad
d\ge {p-1\over R},
\tag{9}
\]

and similarly for `q`.  Since `d | M` and `d<=p-1`, absence of every divisor
of `M` from

\[
\left[{p-1\over R},p-1\right]
\tag{10}
\]

forces `s_p>R`.  This equivalence proves numerical largeness only; it proves
no residual-smoothness conclusion.  Conversely, the presence of an arbitrary
divisor in (10) does not imply `s_p<=R`, because that divisor need not be
`d`.

## Theorem C — exact divisor-only P205 saturation boundary

The **divisor-only multiplicative grammar** in this packet is deliberately
narrow.  It consists of words

\[
W=\prod_{j=1}^J B_j^{e_j},
\qquad B_j\mid M,quad e_j\ge0,
\tag{11}
\]

and the equivalent use of gcd or lcm on such words.  Exact division may
remove prime support but cannot add it.  This grammar excludes addition,
subtraction, divisor differences, `B+c`, the carry child `u^2+cB`, modular
residues, and every other externally supplied integer.

For `i` in `{p,q}`, define the part of `s_i` supported outside `M` by

\[
s_i^{\perp M}
=\prod_{\substack{\ell^e\parallel s_i\\ \ell\nmid M}}\ell^e.
\tag{12}
\]

Every divisor-only word satisfies

\[
\boxed{
s_i^{\perp M}
\mid {s_i\over\gcd(s_i,W)}.
}
\tag{13}
\]

This bound is attained simultaneously for `p` and `q` by the public word

\[
\boxed{W_*=M^n.}
\tag{14}
\]

Namely,

\[
{s_i\over\gcd(s_i,W_*)}=s_i^{\perp M}.
\tag{15}
\]

The word `W_*` has `O(n^2)` bits and needs no factorization of `K` or `M`.
Therefore complete recursive factorization of `K`, enumeration of any
quasipolynomial subfamily of divisors, and arbitrary multiplicative reuse of
those divisors cannot improve the P205 residual beyond (15).

More generally, if a public baseline `L` is also permitted but every word
prime remains in the support of `ML`, then `(ML)^n` attains the exact
support-saturated residual.  Taking `L=R!` absorbs all residual primary parts
on primes at most `R`; the remaining primary parts on primes `ell>R` with
`ell` not dividing `M` are untouched by the divisor lattice.

## Theorem D — the additive selector is the exact remaining escape

The carry identity supplies

\[
xy=u^2+cB.
\tag{16}
\]

If `a` and the signed divisor `x` are recovered, then

\[
\boxed{aB+x-u=u(p-1),}
\tag{17}
\]

so placing this positive integer in a public word absorbs all of `s_p`.
Similarly,

\[
bB+y-u=u(q-1)
\tag{18}
\]

absorbs all of `s_q`.  Hence a quasipolynomial bank that is guaranteed to
contain one correct pair `(a,x)` or `(b,y)` constructs a valid P205 word.
If both centers `a,b` and the carry `c` are in quasipolynomial banks, Theorem
A instead gives a direct verified factor bank.

When `u^2+cB` is nonzero, knowing the complete factorization of its absolute
value does not in general select the signed divisor `x`.  A factored `m`-bit
integer can have more than numerical-quasipolynomially many divisors.  Thus
complete recursive factorization is not, by itself, permission to enumerate
all centered-residue choices.  The publicly visible zero-product case is
degenerate and can be handled separately.  This is a selector boundary, not
a hardness theorem: a new semiprime-specific rule could still select the
correct divisor without enumeration.

In the literal near-factor case `u=a=1` and `|p-B|<=X`, scanning the signed
offset `x=p-B` already tests the candidate factor `B+x`.  Such a
quasipolynomial additive window gives a direct factor and does not need the
carry or P205.  The unresolved case is a public divisor/carry law that gives
useful support without already enumerating a hidden factor-sized offset.

## Boundary conclusion

Factoring `K=(N-1)/2` completely exposes all multiplicative divisor data but
does not label the common divisor `d`.  The guaranteed lattice point `d`
has carry zero and residual-sized centers.  Inside the divisor-only grammar,
the optimal P205 word is already the unfactored polynomial-bit word
`(N-1)^n`.  Absence of a divisor in the residual window forces the residual
to be larger; no smoothness conclusion has been proved.

Any genuine improvement must therefore use an additive output of the
divisor lattice and prove one of the following new source statements:

1. a quasipolynomial bank contains a correct center and centered residue;
2. a quasipolynomial bank contains both centers and a short carry;
3. a semiprime-specific selector recovers the required signed divisor of
   `u^2+cB` without exhaustive divisor enumeration; or
4. an additive divisor word reduces one exterior P205 residual to
   numerical quasipolynomial size with a proved all-input or inverse-QP law.

No such source statement is proved here.
