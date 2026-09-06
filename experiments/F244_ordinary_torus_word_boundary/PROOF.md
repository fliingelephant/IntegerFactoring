# Proof of the F244 ordinary–torus square-word boundary

## 1. The lcm of the four shifted common divisors

Retain the notation of the statement.  First let `ell` be an odd prime.
Because

\[
\gcd(p-1,p+1)=2,
\]

`ell` divides at most one of `p-1,p+1`.  The same holds for `q`.  If it
divides neither side for one hidden prime, it does not occur in `G`.  If it
divides `p-a` and `q-b`, then

\[
v_\ell(d_{a,b})
=\min(v_\ell(A),v_\ell(B))=v_\ell(G),
\]

and none of the other three shifted gcds contains `ell`.  Therefore the
odd part of `lcm_{a,b} d_{a,b}` equals the odd part of `G`.

For the prime two, write

\[
x_a=v_2(p-a),\qquad y_b=v_2(q-b).
\]

Exactly one of `x_+,x_-` is one, and the other is `U-1`.  Likewise the two
`y` values are `1` and `V-1`.  Hence

\[
\max_{a,b}\min(x_a,y_b)
=\min(U-1,V-1)=v_2(G)-1.
\]

The lcm therefore loses exactly one factor two from `G`.  This proves (4).

## 2. Pairwise coprimality and the product identity

For every odd prime `ell`, put

\[
u=v_\ell(A),\qquad v=v_\ell(B).
\]

At most one `p`-side sign contains `ell`, and at most one `q`-side sign
contains it.  Formula (5) gives total `ell`-valuation

\[
\max(u-v,0)+\max(v-u,0)=\lvert u-v\rvert             \tag{21}
\]

across the four residuals.  The two positive terms in (21) cannot occur
simultaneously.  Thus `ell` occurs in at most one residual.

At two, the total valuation in the two `p` residuals is

\[
\max(U-1-V,0),
\]

and the total in the two `q` residuals is

\[
\max(V-1-U,0).
\]

Again at most one is positive.  Their sum is

\[
\lvert U-V\rvert-\mathbf 1_{U\ne V}.                 \tag{22}
\]

Equations (21) and (22) prove that the four residuals are pairwise coprime.
They also prove

\[
\prod t
=\frac{AB/G^2}{2^\delta}
=\frac{AB}{2^\delta G^2},
\]

which is (6).  At least one of four positive integers is at most their
geometric mean.  Since

\[
AB=(p^2-1)(q^2-1)<p^2q^2=N^2,
\]

equation (7) follows.

## 3. The common exponent and the averaged factor probability

In orientation `(a,b)`, `J=ab`.  Setting `W_J=N+J` gives (8).  Modulo
`p-a`, one has `p=a`, and hence

\[
N^2-1=p^2q^2-1=q^2-1=B\pmod {p-a}.
\]

Therefore

\[
{p-a\over\gcd(p-a,N^2-1)}=t_{p,a}.
\]

The `q` identity is symmetric.

Put `x_a=t_{p,a}` and `y_b=t_{q,b}`.  F242's exact clean powered law gives,
in orientation `(a,b)`,

\[
S_{a,b}\ge {1\over2\min(x_a,y_b)}
={1\over2}\max(1/x_a,1/y_b).                         \tag{23}
\]

A fresh uniform unit discriminant gives each orientation with probability
one quarter when the discriminant is retained while coefficient pairs are
resampled.  Averaging (23), and using
`max(r,s) >= (r+s)/2`, gives

\[
{1\over4}\sum_{a,b}S_{a,b}
\ge {1\over8}\sum_{a,b}\max(1/x_a,1/y_b)
\ge {1\over8}\left(\sum_a1/x_a+\sum_b1/y_b\right).
\]

Arithmetic–geometric mean applied to the four reciprocals proves (9).
Substitution from (6), followed by `AB<N^2`, proves (10).

## 4. The signed-power valuation law

Let `h=ord_ell(N)`.  If `h` does not divide `k`, then `ell` does not divide
`N^k-1`.  If `k=hu`, the odd-prime lifting-the-exponent identity gives

\[
v_\ell(N^{hu}-1)=v_\ell(N^h-1)+v_\ell(u).
\]

This proves (11).

The equation `N^k=-1 (mod ell)` is possible exactly when `h` is even and

\[
k\equiv h/2\pmod h.
\]

Equivalently, `k=(h/2)u` for an odd integer `u`.  Then
`N^{h/2}=-1 (mod ell)`, and the plus form of the same lifting identity gives

\[
v_\ell(N^k+1)=v_\ell(N^{h/2}+1)+v_\ell(u).
\]

This proves (12).

## 5. Construction of the infinite family

Fix absolute constants `A_L,L_L` for Linnik's theorem: every reduced
residue class modulo `M` contains a prime at most `A_L M^{L_L}`.

Let `X` tend to infinity.  Four applications of Bertrand's theorem in
successive disjoint dyadic intervals give distinct primes

\[
X<\lambda_+<2X,
\quad 2X<\lambda_-<4X,
\quad 4X<\rho_+<8X,
\quad 8X<\rho_-<16X.                                 \tag{24}
\]

Take `X` large enough that all four exceed five.  Choose primitive roots
modulo each selected prime.

### 5.1 Choosing `p`

By CRT, choose the residue class

\[
\begin{aligned}
p&=13\pmod {24},\\
p&=+1\pmod {\lambda_+},\\
p&=-1\pmod {\lambda_-},\\
p&=g_+\pmod {\rho_+},\\
p&=g_-\pmod {\rho_-},
\end{aligned}                                        \tag{25}
\]

where `g_+,g_-` are primitive roots modulo the two `rho` primes.  Every
displayed residue is a unit modulo its modulus, so (25) is a reduced class
modulo

\[
M_p=24\lambda_+\lambda_-\rho_+\rho_-.
\]

Linnik supplies a prime `p` in this class.  In particular,

\[
\lambda_+\mid p-1,\qquad \lambda_-\mid p+1,
\]

and `p` is primitive modulo both `rho` primes.

### 5.2 Choosing `q` after the full support of `p^2-1` is fixed

The congruence `p=13 (mod 24)` gives

\[
v_2(p-1)=2,\qquad v_2(p+1)=1,
\]

so `v_2(p^2-1)=3`; it also gives `p=1 (mod 3)`.  Write

\[
p^2-1=2^3 3^e\prod_{s\ge5}s^{e_s},\qquad e\ge1.      \tag{26}
\]

For each prime `s>=5` in (26), choose a unit residue `c_s modulo s^{e_s}`
whose reduction modulo `s` is not `+1` or `-1`.  If
`s=lambda_+` or `s=lambda_-`, choose that reduction to be a primitive root
modulo `s`.  This is possible because every primitive root modulo a prime
larger than five differs from `+1` and `-1`.  For every other `s`, the
residue `2 modulo s` suffices, and it can be lifted arbitrarily to
`s^{e_s}`.

The primes `rho_+,rho_-` do not divide `p^2-1`: by (25), `p` has order
`rho_+-1` or `rho_--1` modulo them, and these orders exceed two.  Thus all
the following congruences have pairwise coprime moduli:

\[
\begin{aligned}
q&=3\pmod 8,\\
q&=2\pmod {3^{\max(e,2)}},\\
q&=c_s\pmod {s^{e_s}} &&(s\ge5,\ s^{e_s}\parallel p^2-1),\\
q&=+1\pmod {\rho_+},\\
q&=-1\pmod {\rho_-}.
\end{aligned}                                        \tag{27}
\]

Every residue in (27) is a unit.  Hence (27) is one reduced CRT class.
Linnik supplies a prime `q` in it.  It is distinct from `p`, because (25)
makes `p` neither `+1` nor `-1` modulo either `rho` prime, while (27) gives
those two residues to `q`.

Equations (25) and (27) prove all four divisibilities in (14) and both
primitive-root assertions in (15).  The construction is sequential, so it
uses neither a simultaneous-prime conjecture nor Artin's conjecture.

### 5.3 Exact shifted gcds

The congruences for `p` and `q` give

\[
\begin{array}{c|cc}
 & -1 & +1\\ \hline
p &v_2(p-1)=2&v_2(p+1)=1\\
q &v_2(q-1)=1&v_2(q+1)=2.
\end{array}
\]

Also, `3` divides `p-1`, while `q=2 (mod 9)` makes

\[
v_3(q+1)=1,\qquad 3\nmid q-1.
\]

For every prime `s>=5` dividing `p^2-1`, (27) makes `q` different from
both signs modulo `s`.  Therefore `s` does not divide `q^2-1`.  These facts
exhaust all prime divisors of `p^2-1` and prove

\[
\gcd(p^2-1,q^2-1)=2^3\cdot3=24.                      \tag{28}
\]

The two-adic and three-adic sign locations just displayed refine (28) to

\[
\gcd(p-1,q-1)=2,
\quad \gcd(p-1,q+1)=12,
\quad \gcd(p+1,q-1)=2,
\quad \gcd(p+1,q+1)=2.
\]

No avoidance of an unspecified future divisor is used: (27) explicitly
handles every prime divisor of the already fixed integer `p^2-1`.

### 5.4 The input-length link

By (24), `M_p=O(X^4)`.  Linnik gives an absolute `C_1` such that

\[
X<p<X^{C_1}                                           \tag{29}
\]

for all sufficiently large `X`.  The modulus in (27) is at most

\[
3(p^2-1)\rho_+\rho_-=O(p^2X^2).
\]

Another application of Linnik gives an absolute `C_2` such that

\[
X<q<X^{C_2}.                                          \tag{30}
\]

The lower bounds follow from the congruences modulo `lambda_+` and
`rho_+`.  Equations (29) and (30) show

\[
n=\Theta(\log X).
\]

In particular, one absolute `c>0` satisfies (13).  Taking an unbounded
sequence of `X` gives infinitely many distinct semiprimes.

## 6. Why every short signed-power word misses all four selected primes

If `lambda_a | p-a`, then

\[
N=aq\pmod {\lambda_a}.
\]

The element `q` is primitive modulo `lambda_a`.  Multiplication by the sign
`a` leaves its order equal to `lambda_a-1` or
`(lambda_a-1)/2`.  In either case,

\[
\operatorname{ord}_{\lambda_a}(N)
\ge {\lambda_a-1\over2}.                              \tag{31}
\]

The symmetric argument gives

\[
\operatorname{ord}_{\rho_b}(N)
\ge {\rho_b-1\over2}.                                 \tag{32}
\]

Let `K=max_j k_j`.  If a selected prime divides `N^k-1`, its order is at
most `k`.  If it divides `N^k+1`, its order is at most `2k`.  Therefore no
selected prime divides any factor in (17) when

\[
4K<\min(\lambda_+,\lambda_-,\rho_+,\rho_-)-1.         \tag{33}
\]

Each factor in (17) has binary length at least `k_j` for this family.
Thus `K` is no larger than the binary length of `W`.  For every fixed
numerical-quasipolynomial `Q`,

\[
Q(n)=2^{o(n)}<2^{cn}/8
\]

for all sufficiently large `n`.  Equations (13) and (33) then prove (18).

The prime `lambda_a` divides `p-a` but not the base `N-ab`, because its
primitive residue `q` is not `b`.  It also misses `W` by (18), so it remains
in the `p`-side F242 residual for orientation `(a,b)`.  The `rho_b` argument
is symmetric.  The exact clean powered law is at most the union bound

\[
1/r_{p,a}+1/r_{q,b}
\le1/\lambda_a+1/\rho_b,
\]

which proves (19).

For completeness, the sampler gcd exits do not change this asymptotic
conclusion.  A uniform discriminant modulo `N` is a zero divisor in exactly
one hidden component with probability at most

\[
{1\over p}+{1\over q}.
\]

For a fixed unit discriminant and one uniform coefficient pair, the
coefficient gcd is proper with probability at most `1/p^2+1/q^2`.  In a
local split quadratic algebra, at most `2r-1` of the `r^2` coefficient
pairs have zero norm; in a nonsplit algebra only the zero pair does.
Therefore a proper norm gcd has probability at most `2/p+2/q` per pair.
F242's clean-acceptance probability is at least `16/81`, so the expected
number of coefficient pairs before a clean acceptance or a factor exit is
at most `81/16`.  The total probability of an incidental factor exit in
one outer trial is consequently `O(1/p+1/q)=O(1/X)=2^{-Omega(n)}`.  A
union bound over a numerical-quasipolynomial number of trials remains
exponentially small.

Finally, any exact common order in orientation `(a,b)` divides
`d_{a,b}`.  Their total lcm therefore divides `12` by (16), even if all
four hidden sign labels are granted.  Equation (20) follows directly.

The construction proves only the boundary stated in the packet.  It does
not restrict public integer sources outside (17).
