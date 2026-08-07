# Proof-blind reconstruction: inverse-quotient descent

## Status

The reconstruction succeeds. There is no gap in the stated claims, provided that
`D_N^{-1}(k)` means the inverse image inside the units in
`{1,\ldots,N-1}`, and that a trajectory starts at such a unit. The proof below
uses only the stated definitions, the standard maximal-order bound for the
divisor function, and an elementary Chebyshev estimate for an lcm.

Let

\[
U_N=\{u:1\leq u<N,\ \gcd(u,N)=1\}.
\]

For `u` in `U_N`, let `v` be the representative of `u^{-1} mod N` in
`{1,\ldots,N-1}`. Then

\[
uv=1+N D_N(u).
\]

## 1. The descent identity

Fix `u` with `2\leq u<N` and `gcd(u,N)=1`, and put

\[
k=D_N(u)=\frac{uv-1}{N}.
\]

The inverse `v` cannot be `1`, since that would give `u=1`. Hence `uv>1`
and `k\geq 1`. Also `v<N`, so

\[
uv-1<uN,
\]

and therefore `k<u`. Thus

\[
1\leq k<u. \tag{1.1}
\]

Reducing `uv=1+Nk` modulo `u` gives

\[
Nk\equiv -1\pmod u. \tag{1.2}
\]

Let `r_u` be the unique integer in `{1,\ldots,u-1}` such that

\[
Nr_u\equiv 1\pmod u.
\]

Then `u-r_u` also lies in `{1,\ldots,u-1}`, and

\[
N(u-r_u)\equiv -1\pmod u.
\]

Multiplication by `N` is a permutation modulo `u`. Equations (1.1) and
(1.2) therefore force

\[
\boxed{D_N(u)=u-r_u}.
\]

In particular,

\[
1\leq D_N(u)<u,
\]

so every defined nonterminal step is a strict descent.

For any `r` with `1\leq r<u`, the same uniqueness gives the equivalent
form

\[
\boxed{D_N(u)=u-r\quad\Longleftrightarrow\quad u\mid Nr-1}.
\]

Indeed, the divisibility condition says exactly that `r` is the least
positive representative of `N^{-1} mod u`.

## 2. Exact inverse fibers

Fix `k` with `1\leq k<N`. If `D_N(u)=k`, then Part 1 gives `k<u<N`, and

\[
uv=Nk+1.
\]

Thus `u\mid Nk+1`.

Conversely, suppose

\[
k<u<N,\qquad u\mid Nk+1,
\]

and set

\[
v=\frac{Nk+1}{u}.
\]

This is a positive integer. Since `k<u`,

\[
Nk+1<Nu,
\]

so `v<N`. Since `u<N`,

\[
Nk+1-ku=k(N-u)+1>0,
\]

so `v>k`. Therefore

\[
k<v<N. \tag{2.1}
\]

Any common divisor of `u` and `N` divides both `Nk+1` and `Nk`, hence
divides `1`. Thus `gcd(u,N)=1`. The same argument applies to `v`, because
`v\mid Nk+1`. Hence both `u` and `v` are in `U_N`. Their product satisfies

\[
uv=Nk+1\equiv 1\pmod N.
\]

By (2.1), `u` and `v` are the least positive inverse representatives of
each other modulo `N`. It follows that

\[
D_N(u)=D_N(v)=\frac{uv-1}{N}=k.
\]

Consequently,

\[
\boxed{
D_N^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
}
\]

The map

\[
u\longmapsto \frac{Nk+1}{u}
\]

is an involution of this fiber. It pairs complementary divisors of
`Nk+1`. If `Nk+1` is not a square, it has no fixed point, so the whole
fiber splits into disjoint two-element complementary pairs. If `Nk+1`
is a square, then

\[
k^2<Nk+1<N^2,
\]

so its square root lies strictly between `k` and `N` and is the single
possible fixed point.

## 3. A divisor-count depth bound

Let

\[
u_0,u_1,\ldots,u_L
\]

be a trajectory with `L` transitions. Thus `u_i` is a unit and `u_i>1`
for every `i<L`,

\[
u_{i+1}=D_N(u_i),
\]

and `u_L` is either `1` or the first proper nonunit. Define

\[
r_i=u_i-u_{i+1}\qquad(0\leq i<L).
\]

Part 1 gives

\[
r_i\geq 1,
\qquad
u_i\mid Nr_i-1. \tag{3.1}
\]

The descent is strict, so the sources `u_0,\ldots,u_{L-1}` are distinct.
The decrements telescope:

\[
\sum_{i=0}^{L-1}r_i=u_0-u_L<N. \tag{3.2}
\]

Fix a real number `B` with `1\leq B<N`. Split the transitions into those
with `r_i>B` and those with `r_i\leq B`. Equation (3.2) shows that the
first class has fewer than `N/B` members.

Now fix one positive integer `r\leq B`. By (3.1), every source with
`r_i=r` is a distinct positive divisor of `Nr-1`. Moreover,

\[
1\leq Nr-1\leq NB-1<N^2.
\]

With

\[
\Delta_N=\max_{1\leq m<N^2}\tau(m),
\]

there are at most `\Delta_N` such sources for each `r`. There are
`\lfloor B\rfloor\leq B` possible values of `r`. The second class therefore
has at most `B\Delta_N` members. Hence the proof actually gives the
slightly stronger estimate

\[
L<\frac NB+B\Delta_N.
\]

In particular, the requested bound follows:

\[
\boxed{L\leq \frac NB+B\Delta_N+1}. \tag{3.3}
\]

The standard maximal-order theorem for the divisor function states

\[
\max_{m\leq x}\tau(m)
=\exp\!\left((\log 2+o(1))\frac{\log x}{\log\log x}\right).
\]

Applied with `x=N^2`, it gives

\[
\Delta_N
\leq
\exp\!\left((2\log 2+o(1))\frac{\log N}{\log\log N}\right)
=N^{o(1)}. \tag{3.4}
\]

For `N\geq 3`, choose `B=\lceil\sqrt N\rceil`, which is less than `N`.
Equations (3.3) and (3.4) then give

\[
\boxed{L\leq N^{1/2+o(1)}}.
\]

If `n=\lceil\log_2 N\rceil` is the input bit length, this bound has size

\[
N^{1/2+o(1)}=2^{(1/2+o(1))n}.
\]

Thus this estimate is still exponential in the input length. It is not a
polynomial-time depth bound.

## 4. An exact logarithmic-depth family

Let `L\geq 1` and define

\[
M_L=\operatorname{lcm}(2,3,\ldots,L+1),
\qquad
N_L=(M_L+1)^2.
\]

For every `j` with `2\leq j\leq L+1`, one has `j\mid M_L`. Hence

\[
j\leq L+1\leq M_L<N_L
\]

and

\[
N_L=(M_L+1)^2\equiv 1\pmod j.
\]

It follows both that `gcd(j,N_L)=1` and that the least positive inverse
of `N_L` modulo `j` is `1`. Part 1 now gives

\[
D_{N_L}(j)=j-1.
\]

Therefore the trajectory is exactly

\[
\boxed{L+1\longrightarrow L\longrightarrow\cdots\longrightarrow2
\longrightarrow1},
\]

with exactly `L` transitions.

For completeness, write

\[
\psi(x)=\sum_{p^a\leq x}\log p
=\log\operatorname{lcm}(1,2,\ldots,\lfloor x\rfloor).
\]

The elementary Chebyshev estimate is `\psi(x)=\Theta(x)`. One short proof
is as follows.

For the lower bound, Legendre's formula shows

\[
\binom{2n}{n}\mid \operatorname{lcm}(1,2,\ldots,2n).
\]

Indeed, each summand in the `p`-adic valuation of the binomial coefficient
is `0` or `1`, so its total valuation is no larger than the largest `a`
with `p^a\leq2n`. Also, the central term is the largest term in the
binomial expansion of `4^n`, so

\[
\binom{2n}{n}\geq\frac{4^n}{2n+1}.
\]

This gives `\psi(2n)\geq 2n\log2-\log(2n+1)`.

For the upper bound, every prime power `p^a` in `(n,2n]` contributes a
factor `p` to `\binom{2n}{n}`. There is at most one such power for each
prime. Therefore

\[
\psi(2n)-\psi(n)\leq\log\binom{2n}{n}\leq2n\log2.
\]

Summing this inequality over powers of two gives `\psi(x)=O(x)`. Taking
`n=\lfloor x/2\rfloor` in the lower estimate gives `\psi(x)=\Omega(x)`.

Since

\[
M_L=\operatorname{lcm}(1,2,\ldots,L+1),
\]

we have

\[
\log M_L=\psi(L+1)=\Theta(L).
\]

Thus

\[
\log N_L=2\log(M_L+1)=\Theta(L),
\]

and the bit length of `N_L` is `\Theta(L)`.

This family only disproves a universal `o(\log N)` depth claim. It does
not give hard factoring instances: every `N_L` is the explicit perfect
square of `M_L+1`, so an integer square root factors it immediately.

## 5. Failure of two-step contraction

For `N=11` and `u=7`, the least positive inverse of `11` modulo `7` is
`2`, because `11\cdot2\equiv1\pmod7`. Hence

\[
D_{11}(7)=7-2=5.
\]

The least positive inverse of `11` modulo `5` is `1`, so

\[
D_{11}(5)=5-1=4.
\]

Thus

\[
7\longrightarrow5\longrightarrow4,
\qquad
2D_{11}(D_{11}(7))=8>7.
\]

For the balanced semiprime `N=35=5\cdot7` and `u=19`, one has

\[
35\cdot6\equiv1\pmod{19},
\]

so

\[
D_{35}(19)=19-6=13.
\]

Next,

\[
35\cdot3\equiv1\pmod{13},
\]

so

\[
D_{35}(13)=13-3=10.
\]

Therefore

\[
19\longrightarrow13\longrightarrow10,
\qquad
2D_{35}(D_{35}(19))=20>19.
\]

Both examples directly refute the proposed universal two-step contraction.

## 6. Limits of the theorem

The theorem proves none of the following stronger claims.

1. **A polylogarithmic worst-case depth bound.** The proved upper bound is
   `N^{1/2+o(1)}`, which is exponential in `\log N`. The square family
   supplies a logarithmic lower bound, not a polylogarithmic upper bound.

2. **An inverse-polynomial factor-hit law.** No probability distribution
   on starting units is specified, and no count or measure of trajectories
   that reach a proper nonunit is bounded below. A trajectory can instead
   reach `1`. The divisor-fiber identity alone gives no success probability.

3. **A whole-transcript decoder.** Part 2 inverts one step only after one
   finds suitable divisors of `Nk+1`. It neither factors that integer nor
   selects a unique predecessor. Repeated inversion can branch. Thus the
   local identity is not an efficient or unique decoder for an entire
   trajectory.

4. **A factoring algorithm.** If a trajectory reaches a proper nonunit,
   a gcd reveals a factor. The theorem does not guarantee that event, give
   it sufficient probability, or bound the required number of steps by a
   polynomial in the input length. The constructed long-depth inputs are
   already easy perfect squares.

Finally, the two exact counterexamples in Part 5 establish only the failure
of one universal inequality. No asymptotic depth law, success probability,
or factoring complexity can be inferred from any finite scan. All
asymptotic conclusions above come from the general proofs and the stated
standard divisor bound.
