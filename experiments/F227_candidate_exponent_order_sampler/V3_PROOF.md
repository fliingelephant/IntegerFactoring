# Proof of the F227 V3 AP-exponent sampler boundary

## 1. Fixed conventions and factor-cell geometry

The input length and fixed envelope are (Q0)--(Q2). Thus

\[
\log_2Q(n)=O((\log n)^{k_*})=o(n),
\tag{1}
\]

with constants independent of every history and stage.

From `p<q<2p`,

\[
\sqrt{N/2}<p<\sqrt N<q<2p.
\tag{2}
\]

Hence `p` is in `I_N` and is the only member having a nontrivial gcd with
`N`. Since `L` is even and all candidates are congruent to the odd integer
`p`, every candidate `x` is odd and `A_x=x-1` is even. Also

\[
0<A_x<\sqrt N<q<2p.
\tag{3}
\]

The only positive multiple of `p` below `2p` is the odd integer `p`, so it
cannot equal `A_x`; no positive multiple of `q` occurs. Therefore

\[
\gcd(A_x,N)=1
\qquad(x\in\mathcal C).
\tag{4}
\]

Factoring `A_x` cannot itself expose a hidden factor of `N`. The only direct
factor candidate is `x=p`.

## 2. AP gcd mean

Use

\[
\gcd(A,m)=\sum_{d\mid\gcd(A,m)}\varphi(d).
\tag{5}
\]

For fixed `d|m`, put `g=gcd(d,L)`. The congruence

\[
c+jL\equiv0\pmod d
\tag{6}
\]

is insoluble unless `g|c`. When soluble, its solutions form one residue
class modulo `d/g`. In `H` consecutive indices their number is at most

\[
\frac{Hg}{d}+1\le\frac{HL}{d}+1.
\tag{7}
\]

A law of largest atom `eta` assigns at most `eta` times this count. Taking
the expectation in (5) gives

\[
\begin{aligned}
\mathbb E_\mu\frac{\gcd(A_j,m)}m
&\le\frac\eta m
\sum_{d\mid m}\varphi(d)
\left(\frac{HL}{d}+1\right)\\
&=\eta\left[
\frac{HL}{m}\sum_{d\mid m}\frac{\varphi(d)}d+1
\right]\\
&\le\eta\left(\frac{HL\tau(m)}m+1\right).
\end{aligned}
\tag{8}
\]

We used `sum_(d|m)phi(d)=m` and `phi(d)/d<=1`. The choice `eta=1/H`
gives (A4).

## 3. Local returns and the one-trial bound

Fix `x` and abbreviate `A=A_x`. A uniform unit modulo `N` has independent
uniform reductions in the two cyclic groups. Thus

\[
\alpha_p(x)=\Pr(a^A=1\bmod p)
=\frac{\gcd(A,p-1)}{p-1},
\tag{9}
\]

\[
\alpha_q(x)=\Pr(a^A=1\bmod q)
=\frac{\gcd(A,q-1)}{q-1}.
\tag{10}
\]

Apart from `x=p`, every useful exit of the declared channel needs at least
one local return. If neither side returns, the initial gcd is one and no
primary test is valid. If exactly one returns, the gcd is proper. If both
return, the gcd is `N` and factor-first stripping may split or certify
support. Hence

\[
\Pr(\text{useful}\mid x)
\le\mathbf1_{x=p}+\alpha_p(x)+\alpha_q(x).
\tag{11}
\]

The direct event has mass at most `eta`. Applying (8) with `m=p-1` and
`m=q-1` proves

\[
\Pr(\text{useful})
\le
\eta\left[
3+HL\left(
\frac{\tau(p-1)}{p-1}+
\frac{\tau(q-1)}{q-1}
\right)
\right].
\tag{12}
\]

This upper bound grants complete factorizations of all `A_x` and all sound
postprocessing after global return.

To implement a uniform unit exactly, draw uniform residues, retry zero,
accept gcd one, and return a proper gcd. Among the `N-1` nonzero residues,
exactly `(q-1)+(p-1)` are proper nonunits. Therefore the probability of a
proper factor before an accepted unit is

\[
\frac{p+q-2}{N-1}=O(1/p).
\tag{13}
\]

The accepted residue is an exact uniform unit.

## 4. Uniform preterminal asymptotics

Let `W=|I_N|`. Since `sqrt(N)>=p`,

\[
W\ge\left(1-\frac1{\sqrt2}\right)p-2.
\tag{14}
\]

A residue class in `W` consecutive integers occurs between `floor(W/L)`
and `ceil(W/L)` times. The nonterminal condition gives

\[
L<\frac{N^{1/4}}{S(n)}
\le N^{1/4}<2^{1/4}p^{1/2}.
\tag{15}
\]

Thus there are absolute `c_1,c_2>0` such that, for all sufficiently large
inputs,

\[
c_1\frac pL\le H\le c_2\frac pL.
\tag{16}
\]

The uniform divisor estimate

\[
\tau(m)=
\exp\left(O\left(\frac{\log m}{\log\log m}\right)\right)
=m^{o(1)}
\tag{17}
\]

suffices. One proof splits the prime factors at `sqrt(log m)`. There are at
most that many small primes, each with exponent at most `log_2 m`. The
large-prime multiplicity is at most `log m/log sqrt(log m)`, and
`e+1<=2^e`. This gives (17) with absolute constants.

Balance and (Q0) give

\[
\log_2p=\frac n2+O(1).
\tag{18}
\]

The fixed `Q(n)` is `p^{o(1)}`, with one uniform `o(1)`. If
`eta H<=Q(n)`, equations (12), (15)--(18) give

\[
\Pr(\text{useful}\mid\text{history})
\le p^{-1/2+o(1)}.
\tag{19}
\]

Equation (13) is smaller and is absorbed. Uniformity supplies fixed
`c_0>0,n_0` such that (B5) holds for every admissible history. Applying the
conditional bound at each of at most `Q(n)` fresh trials proves (B6).

## 5. Fixed-base return progression

Fix a public unit and enumerate

\[
x_j=x_0+jL\qquad(0\le j<H).
\tag{20}
\]

The index of `p` is a solution of

\[
o_p\mid x_j-1.
\tag{21}
\]

Put

\[
g_p=\gcd(o_p,L),\qquad u_p=o_p/g_p.
\tag{22}
\]

After division by `g_p`, the step `L/g_p` is invertible modulo `u_p`.
Therefore the returning indices form exactly one class modulo `u_p`, with at
least `floor(H/u_p)` representatives in the cell.

## 6. Nonstale returns are useful

For a candidate returning modulo `p`:

- `x=p` gives the direct factor;
- no return modulo `q` makes `gcd(a^A-1,N)=p`; and
- return on both sides makes both local orders divide the completely
  factored exponent `A`.

In the last case repeatedly test, for every prime divisor `ell` of the
current exponent `E`,

\[
\gcd(a^{E/\ell}-1,N).
\tag{23}
\]

Replace `E` by `E/ell` when the gcd is `N`; return a proper gcd when it is
proper; and retain the primary exponent when it is one. If no factor occurs,
all local order valuations agree and the final value is

\[
E=o_p=o_q.
\tag{24}
\]

Its factorization comes from `A`, and the primary tests certify
`E|p-1,q-1`. It grows `L` unless `E|L`. Thus only

\[
o_p=o_q\mid L
\tag{25}
\]

is stale. Every returning index is useful otherwise, proving

\[
\Pr(\text{useful})
\ge\frac{\lfloor H/u_p\rfloor}{H}
\ge\frac1{u_p}-\frac1H.
\tag{26}
\]

If `u_p<=Q(n)` and `H>=2Q(n)`, this is at least `1/(2Q(n))`. If the cell is
smaller, direct enumeration uses fewer than `2Q(n)` gcds.

## 7. One progress state: trials, child preprocessing, and public work

Fix one nonterminal same-size state `(N,L)` and its supplied nonstale base.
In the large-cell branch, draw independent uniform candidates until useful.
Equation (26) makes the number of trials geometric with mean at most
`2Q(n)` and finite almost surely.

Let `F(m)` bound the expected complete conditional factorization cost of an
input of at most `m` bits. Let `P_tr(n)` bound the nonrecursive public work
in one candidate trial. It includes candidate generation, direct gcds,
modular powering, factor-first stripping, and a resulting aggregate update.
It excludes exactly one item: the recursive complete factorization of
`A_x`. Separately, let `P_st(n)` bound the one-time state initialization,
including production and verification of the supplied base. These work
classes are disjoint by definition.

Each `A_x<sqrt(N)` has at most `n/2+C_0` bits for one absolute `C_0`.
Conditional on reaching any trial, its expected cost is at most

\[
F(n/2+C_0)+P_{\rm tr}(n).
\tag{27}
\]

Success and trial cost may be correlated. Independence is unnecessary:
sum the conditional expected cost of trial `j` over the event that trial
`j` is reached. The reach probabilities have geometric tail at most
`(1-1/(2Q(n)))^{j-1}`. Thus

\[
\mathbb E[\text{one progress-state cost}]
\le
2Q(n)\left(F(n/2+C_0)+P_{\rm tr}(n)\right)
+P_{\rm st}(n).
\tag{28}
\]

The small-cell branch performs at most `2Q(n)` public gcds and no recursive
candidate factorization, so it is also bounded by (28). Equation (28) counts
the one-time state cost once, not once per candidate.

This counts each recursive candidate factorization and each public trial
exactly once. In particular, it does not replace `Q(n)` trials of public
cost `P_tr(n)` by only one copy of `P_tr(n)`.

## 8. All same-size lcm-growth states

Define

\[
J_N=\left\lceil\frac{N^{1/4}}{S(n)}\right\rceil,
\qquad
\Phi_N(L)=
\max\left\{0,
\left\lceil\log_2\frac{J_N}{L}\right\rceil
\right\}.
\tag{30}
\]

If a useful transition does not factor, it replaces `L` by

\[
L'=\operatorname{lcm}(L,c)>L.
\tag{31}
\]

Since `L|L'`, the integer ratio `L'/L` is at least two. If the new state is
still nonterminal, the ceiling identity gives

\[
\Phi_N(L')\le\Phi_N(L)-1.
\tag{32}
\]

Crossing the terminal threshold or returning a factor also sets the
potential to zero. Therefore, from entry modulus `L_0`, the number of
same-size progress states is deterministically at most

\[
R_N(L_0)=\Phi_N(L_0)\le\lceil\log_2J_N\rceil.
\tag{33}
\]

Since `N<2^n` and `S(n)>=1`,

\[
J_N\le2^{n/4}+1,
\qquad R_N(L_0)=O(n).
\tag{34}
\]

At every later same-size state the conditional premise supplies a new
nonstale base with residual order at most the same fixed `Q(n)`. Apply (28)
conditionally at each state and use the deterministic bound (33). Adding a
terminal and verification cost `G(n)` gives

\[
F(n)
\le
R_N(L_0)\left[
2Q(n)F(n/2+C_0)
+2Q(n)P_{\rm tr}(n)
+P_{\rm st}(n)
\right]+G(n).
\tag{35}
\]

This is the complete current-node recurrence. V2 stopped after one copy of
(28); equation (35) includes all later strict lcm-growth states.

The fixed envelope gives

\[
P_{\rm tr}(n),P_{\rm st}(n),G(n)\le Q(n).
\tag{36}
\]

Equations (34)--(36) imply, after increasing one absolute constant,

\[
F(n)
\le
C_2nQ(n)F(n/2+C_0)
+C_2nQ(n)^2.
\tag{37}
\]

The first term counts at most `O(n)Q(n)` complete half-size candidate
factorizations. The second counts at most `O(n)Q(n)` public trials, each of
cost at most `Q(n)`. No public factor is missing and neither work class is
counted twice.

## 9. Solving the corrected recurrence

Put

\[
B(m)=C_2mQ(m),
\qquad D(m)=C_2mQ(m)^2.
\tag{38}
\]

Starting with `m_0=n`, set `m_(i+1)=m_i/2+C_0` until a fixed base size is
reached. This takes `d=O(log n)` levels. Let

\[
K=\max\{1,k_*\}.
\]

Then

\[
\log_2B(m_i),\ log_2D(m_i)
=O((\log_2(m_i+1))^K).
\tag{39}
\]

The size sequence is geometrically decreasing up to an absolute additive
constant, so

\[
\sum_{i=0}^{d-1}
(\log_2(m_i+1))^K
=O((\log_2(n+1))^{K+1}).
\tag{40}
\]

Unrolling (37) gives one base term multiplied by
`prod_i B(m_i)` and at most `d` additive terms, each `D(m_j)` multiplied by
`prod_(i<j)B(m_i)`. Equations (39)--(40), plus
`log_2d=O(log log n)`, show that every term and their sum are at most

\[
2^{O((\log_2(n+1))^{K+1})}.
\tag{41}
\]

Thus the corrected recurrence is numerical QP.

Each progress state terminates almost surely by its geometric success law.
There are finitely many same-size states by (33), and the recursive size
depth is finite. Induction on the size therefore gives almost-sure
termination of the conditional routine as well as the expected bound (41).

## 10. Rough-order corollary

Every prime divisor of

\[
u_p=\frac{o_p}{\gcd(o_p,L)}
\tag{42}
\]

is a prime divisor of `o_p`. If `o_p` is `T(n)`-rough, then either `u_p=1`
or `u_p>T(n)`. Hence `u_p<=Q(n)<T(n)` forces `u_p=1`, equivalently
`o_p|L`.

When `o_p|L`, the relations `o_p|p-1` and `x\equiv p\pmod L` imply
`o_p|x-1` for every candidate. Section 6 gives a factor or new support unless
`o_p=o_q|L`. This proves Corollary D.
