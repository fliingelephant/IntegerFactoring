# Proof of F206

## 1. The recursion theorem

Replace `Q` by its nondecreasing envelope and enlarge it so that `Q(n)>=1`.
This does not change its numerical-QP class. Define

\[
S(n)=1+\max_{1\le m\le n}T(m).
\]

Choose a fixed base cutoff `n_0` large enough that `r(m)<m` above it. Unroll
the decrement term in the recurrence. For every `m<=n`,

\[
\begin{aligned}
T(m)
&\le T(n_0)+\sum_{j=n_0+1}^{m}
Q(j)(T(r(j))+1)\\
&\le T(n_0)+nQ(n)S(\lceil\rho n\rceil+c).
\end{aligned}
\]

After increasing a fixed constant `A`, this gives

\[
S(n)\le A nQ(n)S(\lceil\rho n\rceil+c).
\tag{1}
\]

Fix `sigma` with `rho<sigma<1`. For all sufficiently large `n`,

\[
\lceil\rho n\rceil+c\le\sigma n.
\tag{2}
\]

Iterate (1) along the geometrically decreasing sequence from `n` to the base
range. It has `L=O(log(n+1))` terms. Every logarithmic factor satisfies

\[
\log_2(An_jQ(n_j))
\le O(\log_2(n+1))+C(\log_2(n+1))^k
=O((\log_2(n+1))^k),
\]

because `k>=1`. Summing over `L` scales gives

\[
\log_2 S(n)=O((\log_2(n+1))^{k+1}).
\]

This proves the displayed bound on `T`.

The proof is unchanged if there are a fixed number of fixed-ratio side
children, or even at most `Q(n)` of them, because their total contribution is
absorbed into the coefficient `Q(n)` after increasing its constants.

Now consider the balanced application. The integer `K=(N-1)/2` has one less
bit than `N`. From the square-gap bound,

\[
E\le2\lfloor\sqrt N\rfloor<2\sqrt N.
\]

Also `p<sqrt(N)<q` and `q<2p` imply

\[
q^2<2pq=2N,
\]

so both `p` and `q` are below `sqrt(2N)`. Hence `E,p,q` have at most
`n/2+O(1)` bits. Above a fixed base range they all have at most `rho*n` bits
for one fixed `rho<1`, for example `rho=3/4`. The auxiliary `K` calls form
the decrement spine, while `E,p,q` are fixed-ratio side children.

On an unbalanced split, one output cofactor can have `n-O(1)` bits. It then
coexists with the `K` child of `n-1` bits. The proof of (1) no longer applies
because the second recursive term is not fixed-ratio. The theorem makes no
claim for that recurrence.

## 2. Construction of the joint square root

The identities

\[
N=2K+1,
\qquad N=B^2+E
\]

give

\[
N\equiv1\pmod K,
\qquad N\equiv B^2\pmod E.
\tag{3}
\]

Let `ell^a || M`. If `v_ell(K)>=v_ell(E)`, then `ell^a|K`, so the first
congruence in (3) gives

\[
R_\ell^2=1\equiv N\pmod{\ell^a}.
\]

If `v_ell(E)>v_ell(K)`, then `ell^a|E`, so the second congruence gives

\[
R_\ell^2=B^2\equiv N\pmod{\ell^a}.
\]

The prime powers are pairwise coprime. CRT therefore constructs `R mod M`
with `R^2=N mod M`.

Moreover,

\[
M\le KE<N^{3/2}.
\]

Thus every CRT modulus and intermediate reduced residue has `O(n)` bits.
The supplied factorizations contain at most `O(n)` prime-power entries, so
ordinary product-tree or sequential CRT arithmetic constructs `M,R` in
deterministic polynomial bit complexity.

The assumptions imply

\[
\gcd(N,K)=1,
\qquad \gcd(N,E)=1,
\qquad \gcd(N,M)=1.
\]

Thus `N` and `R` are units modulo `M`.

## 3. The inverse torsor and its size

For each unit `u mod M`, define

\[
x=Ru,
\qquad y=Ru^{-1}.
\]

Then

\[
xy=R^2\equiv N\pmod M.
\]

Conversely, let `(x,y)` be a unit pair with `xy=N mod M`. Put

\[
u=xR^{-1}.
\]

Then `x=Ru`, and

\[
y=Nx^{-1}=R^2(Ru)^{-1}=Ru^{-1}\pmod M.
\]

This proves existence and uniqueness of the parameterization.

For completeness, if `m=prod p^a`, then

\[
{\varphi(m)^2\over m}
=\prod_{p^a\parallel m}p^{a-2}(p-1)^2.
\]

Every odd-prime factor on the right is larger than one. The factor for 2 is
at least `1/2`, with equality only at exponent one. Therefore

\[
\varphi(m)^2\ge m/2.
\tag{4}
\]

Since `M>=K=(N-1)/2`, equation (4) gives

\[
\varphi(M)\ge\sqrt{M/2}\ge {\sqrt{N-1}\over2}.
\]

The torsor is therefore exponentially large in the bit length of `N`.
This is a local candidate count. It is not a lower bound after an
Archimedean size filter.

## 4. Discriminants and inversion

For a torsor pair,

\[
\begin{aligned}
(x+y)^2-4N
&\equiv R^2(u+u^{-1})^2-4R^2\\
&=R^2(u-u^{-1})^2\pmod M.
\end{aligned}
\]

Thus every pair has square discriminant modulo `M`.

Swapping `x` and `y` replaces `u` by `u^{-1}`. If `chi` is a quadratic
character, then

\[
\chi(u^{-1})=\chi(u)^{-1}=\chi(u),
\]

because its values have order at most two. Symmetric ring expressions are
invariant by definition. Neither interface supplies an orientation bit.

For `N==3 mod 4`, the hidden primes in a balanced semiprime have opposite
residues modulo 4. Since every odd residue modulo 4 is its own inverse, the
first P179 reciprocal bit is changed by swapping the two hidden primes. The
quadratic and symmetric interfaces above are therefore exactly blind to that
bit.

## 5. Predetermined Jacobi signs

Let `ell` be an odd prime dividing `K`. Equation (3) gives

\[
\left({N\over\ell}\right)=1.
\]

If instead `ell|E`, equation (3) gives `N=B^2 mod ell`. The coprimality
assumption implies `ell` does not divide `B`, so again

\[
\left({N\over\ell}\right)=1.
\]

Quadratic reciprocity for the Jacobi symbol gives

\[
\left({\ell\over N}\right)
\left({N\over\ell}\right)
=(-1)^{((\ell-1)/2)((N-1)/2)}.
\]

The second exponent factor is odd because `N==3 mod 4`. The second symbol on
the left is one. Hence

\[
\left({\ell\over N}\right)=(-1)^{(\ell-1)/2}=\chi_4(\ell).
\]

This depends only on the public residue of `ell mod 4`.

Finally, F202 identifies the two mixed ideal classes as `C^2` and `C^{-2}`.
For every genus character `gamma`,

\[
\gamma(C^2)=\gamma(C)^2=1
=\gamma(C^{-2}).
\]

For a fixed auxiliary class `D`, multiplicativity also gives

\[
\gamma(DC^2)=\gamma(D)=\gamma(DC^{-2}).
\]

Thus auxiliary classes obtained from the factored `K` child cannot repair
the orientation through genus characters alone.
