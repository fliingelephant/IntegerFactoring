# Proof of the F227 V5 oracle-relative AP-exponent boundary

## 1. Factor-cell geometry

From `p<q<2p`,

\[
\sqrt{N/2}<p<\sqrt N<q<2p.
\tag{1}
\]

Thus `p` is the sole member of `I_N` with a nontrivial gcd with `N`. Since
`L` is even and every candidate is congruent to the odd integer `p`, each
candidate `x` is odd and `A_x=x-1` is even. Also

\[
0<A_x<\sqrt N<q<2p.
\tag{2}
\]

The only positive multiple of `p` below `2p` is `p`, which is odd, and no
positive multiple of `q` occurs. Hence

\[
\gcd(A_x,N)=1.
\tag{3}
\]

Factoring `A_x` alone cannot expose `p` or `q`. The direct factor candidate
in the cell is `x=p`.

## 2. Proof of Theorem A

Use the identity

\[
\gcd(A,m)=\sum_{d\mid\gcd(A,m)}\varphi(d).
\tag{4}
\]

For a fixed divisor `d|m`, set `g=gcd(d,L)`. The congruence

\[
c+jL\equiv0\pmod d
\tag{5}
\]

is insoluble unless `g|c`. When it is soluble, its solutions form one class
modulo `d/g`. Among `H` consecutive indices there are at most

\[
\frac{Hg}{d}+1\le\frac{HL}{d}+1
\tag{6}
\]

solutions. A law of largest atom `eta` gives that solution set mass at most
`eta` times (6). Therefore

\[
\begin{aligned}
\mathbb E_\mu\frac{\gcd(A_j,m)}m
&\le\frac\eta m\sum_{d\mid m}\varphi(d)
\left(\frac{HL}{d}+1\right)\\
&=\eta\left[
\frac{HL}{m}\sum_{d\mid m}\frac{\varphi(d)}d+1
\right]\\
&\le\eta\left(\frac{HL\tau(m)}m+1\right).
\end{aligned}
\tag{7}
\]

Here `sum_(d|m) phi(d)=m` and `phi(d)/d<=1`. Setting `eta=1/H` proves
(A4).

## 3. Local returns and Theorem B

Fix a candidate and write `A=A_x`. A uniform unit modulo `N` reduces to
independent uniform elements in the two cyclic field groups. Hence

\[
\alpha_p(x)=\Pr(a^A=1\bmod p)
=\frac{\gcd(A,p-1)}{p-1},
\tag{8}
\]

and similarly

\[
\alpha_q(x)=\frac{\gcd(A,q-1)}{q-1}.
\tag{9}
\]

Except for the direct event `x=p`, every useful exit in the declared
channel requires a return in at least one field. Thus

\[
\Pr(\text{useful}\mid x)
\le\mathbf1_{x=p}+\alpha_p(x)+\alpha_q(x).
\tag{10}
\]

The direct event has mass at most `eta`. Apply (A3) to `p-1` and `q-1` to
obtain

\[
\Pr(\text{useful})
\le
\eta\left[
3+HL\left(
\frac{\tau(p-1)}{p-1}+
\frac{\tau(q-1)}{q-1}
\right)
\right].
\tag{11}
\]

This proves (B1), and `eta=1/H` proves (B2). Among the `N-1` nonzero
residues modulo `N`, exactly `(q-1)+(p-1)` are proper nonunits. Exact unit
rejection therefore adds the mass in (B3).

Let `W=|I_N|`. Since `sqrt(N)>=p`,

\[
W\ge\left(1-\frac1{\sqrt2}\right)p-2.
\tag{12}
\]

A residue class in `W` consecutive integers occurs within one of `W/L`
times. The nonterminal inequality gives

\[
L<\frac{N^{1/4}}{S(n)}\le N^{1/4}<2^{1/4}p^{1/2}.
\tag{13}
\]

Consequently, for absolute constants `c_1,c_2>0` and every sufficiently
large input,

\[
c_1\frac pL\le H\le c_2\frac pL.
\tag{14}
\]

The standard uniform divisor bound is

\[
\tau(m)=m^{o(1)}.
\tag{15}
\]

Also `log_2 p=n/2+O(1)`, while the fixed envelope satisfies
`Q(n)=p^{o(1)}` uniformly. If `eta H<=Q(n)`, equations (11), (13)--(15)
give

\[
\Pr(\text{useful}\mid\text{history})
\le p^{-1/2+o(1)}=2^{-\Omega(n)}.
\tag{16}
\]

The rejection mass is smaller. The uniform fixed envelope lets us choose
fixed `c_0,n_0` valid for every input, stage, and reachable history. A
conditional union bound over at most `Q(n)` trials proves (B6). No
cross-trial independence is needed for this negative bound.

## 4. Fixed-base return progression

Enumerate the cell as

\[
x_j=x_0+jL\qquad(0\le j<H).
\tag{17}
\]

The index of `p` is a solution of `o_p|x_j-1`. Let

\[
g_p=\gcd(o_p,L),\qquad u_p=o_p/g_p.
\tag{18}
\]

After division by `g_p`, the step `L/g_p` is invertible modulo `u_p`.
Therefore the returning indices form exactly one residue class modulo
`u_p`. They have at least `floor(H/u_p)` representatives in the cell.

## 5. A nonstale return is useful

Consider a candidate that returns modulo `p`.

- If `x=p`, the direct gcd finds `p`.
- If there is no return modulo `q`, then `gcd(a^{A_x}-1,N)=p`.
- If both sides return, both local orders divide the completely factored
  exponent `A_x`.

In the last case, start with `E=A_x`. For each prime divisor `ell` of the
current `E`, test

\[
\gcd(a^{E/\ell}-1,N).
\tag{19}
\]

If the gcd is `N`, replace `E` by `E/ell`. If it is proper, return the
factor. If it is one, retain the primary exponent. Repeat until no division
by a tested prime is possible. If no proper factor appears, each retained
prime-power valuation is necessary in both local orders, so

\[
E=o_p=o_q.
\tag{20}
\]

The factorization of `E` is known and the tests certify a common order. It
strictly enlarges `L` unless `E|L`. Thus a returning candidate can fail to
progress only when

\[
o_p=o_q\mid L,
\tag{21}
\]

which is exactly the stale case. The return progression from Section 4 now
proves (C3). If `u_p<=Q(n)` and `H>=2Q(n)`,

\[
\frac{\lfloor H/u_p\rfloor}{H}
\ge\frac1{Q(n)}-\frac1H
\ge\frac1{2Q(n)}.
\tag{22}
\]

When `H<2Q(n)`, direct gcd enumeration checks the whole cell.

## 6. One oracle-relative progress state

Fix one nonterminal same-size state and its supplied nonstale base. Draw
fresh uniform candidates until a useful one occurs. Equation (22) makes the
number of trials stochastically dominated by a geometric variable of mean
`2Q(n)`. The state terminates almost surely.

Each candidate exponent satisfies `A_x<sqrt(N)`, so it has at most
`n/2+C_0` bits for one absolute constant `C_0`. Conditional on any reached
trial and on its public history, the all-input oracle premise bounds the
expected child cost by `F_all(n/2+C_0)`. The remaining trial work is at most
`P_tr(n)`.

Success and cost on the same trial can be correlated. Let `R_j` be the
event that trial `j` is reached. It depends only on earlier trials, and

\[
\Pr(R_j)\le\left(1-\frac1{2Q(n)}\right)^{j-1}.
\tag{23}
\]

Using the uniform conditional cost bound after conditioning on `R_j`,

\[
\begin{aligned}
\mathbb E[\text{trial work in one state}]
&\le\sum_{j\ge1}\Pr(R_j)
\left(F_{\rm all}(n/2+C_0)+P_{\rm tr}(n)\right)\\
&\le2Q(n)\left(F_{\rm all}(n/2+C_0)+P_{\rm tr}(n)\right).
\end{aligned}
\tag{24}
\]

Adding one copy of `P_st(n)` proves (C8). The small-cell enumeration branch
uses no child factorization and is bounded by the same expression.

## 7. Exact same-size potential and current-node cost

The state is nonterminal exactly when `L<J_N`. Hence `Phi_N(L)>=1` whenever
a candidate loop runs. A useful nonfactor transition gives

\[
L'=\operatorname{lcm}(L,c)>L.
\tag{25}
\]

Because `L|L'`, the ratio `L'/L` is an integer at least two. If the new
state remains nonterminal, then

\[
\Phi_N(L')\le\Phi_N(L)-1.
\tag{26}
\]

A factor or terminal-threshold crossing ends the current node. This also
counts the final state when the potential is one. Thus the number of
same-size progress states is at most

\[
R_N(L_0)=\Phi_N(L_0)
\le\lceil\log_2J_N\rceil=O(n).
\tag{27}
\]

Apply (C8) conditionally at each reached state, multiply by the deterministic
bound (27), and add `G(n)`. This gives (C9).

The symbol `F_all` in (C9) cannot be replaced by the left-hand side. Every
`A_x` is even and otherwise unrestricted. Its odd part can be a prime, a
prime power, an unbalanced semiprime, or a product of many primes. F227
proves no transition for those input classes. Therefore (C9) is an
oracle-relative current-node estimate, not a closed recurrence.

## 8. Proof of Corollary D

Every prime divisor of

\[
u_p=\frac{o_p}{\gcd(o_p,L)}
\tag{28}
\]

is a prime divisor of `o_p`. On the named rough branch, each such prime is
greater than `T(n)`. Hence `u_p` is one or exceeds `T(n)`. Since
`Q(n)<T(n)`, the condition `u_p<=Q(n)` forces `u_p=1`, equivalently
`o_p|L`.

Now `x\equiv p\pmod L` and `o_p|p-1,L` imply `o_p|x-1` for every candidate.
Every candidate returns modulo `p`. Section 5 gives a factor or a strict
common-order update unless the base is stale. This proves the corollary
without producing the required base or the all-input oracle.
