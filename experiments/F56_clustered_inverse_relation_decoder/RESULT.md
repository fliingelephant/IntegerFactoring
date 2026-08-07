# F56 candidate: completion-biased inverse quotients admit an exact clustered square decoder

## Status and contribution

**Status:** verifier-backed proof-only result for F26. The first hostile audit
accepted the main theorem but found a duplicate-index error and scope wording
that required correction. The corrected theorem passed a fresh whole-artifact
re-audit and a strict proof-blind reconstruction. No cross-family audit has
run.

P62 gives an ordered descent and exact relations

\[
u_i v_i=N u_{i+1}+1.
\]

P64 separates empty endpoint-label parity from true arithmetic square parity.
This result supplies the next operation. It proves that all exact square
relations among values $Nk+1$ whose indices lie in a short public interval
have a polynomial-size kernel representation, and that any nontrivial modular
root in that kernel is detected in time polynomial in the interval width and
in $\log N$, without factoring the large values. It also identifies the
exact first-step law as an implicit completion-biased sampler.

This is a real batch decoder, not one scalar identity followed by one gcd. It
does not prove that a useful square relation exists with inverse-polynomial
probability. That is the remaining algorithmic question.

The closest prior results are P01, P62, and P64. P01
blocks universal compression of arbitrary square classes. Here the generators
are special: common prime factors of two values $Nk_i+1,Nk_j+1$ must divide
the public index difference $k_i-k_j$. P62 supplies these values and their
ordered tail. P64 closes only parity of repeated endpoint labels.

## 1. The exact completion-biased sampler

Let

\[
U_N=\{u\in\{1,\ldots,N-1\}:\gcd(u,N)=1\}.
\]

For $u\in U_N$, let $v$ be its least positive inverse modulo $N$, and
put

\[
D_N(u)=\frac{uv-1}{N}.
\]

For $1\le k<N$, define the completion count

\[
f_N(k)=\#\{u:k<u<N,\ u\mid Nk+1\}.
\tag{1.1}
\]

The exact reverse-fibre formula from P62 gives, for uniform $U\in U_N$,

\[
\boxed{
\Pr(D_N(U)=k)=\frac{f_N(k)}{\varphi(N)}.
}
\tag{1.2}
\]

Also, $D_N(U)=0$ only for $U=1$, with probability
$1/\varphi(N)$. Thus a public modular inversion, canonical integer
representatives, and one exact division sample an implicit distribution whose
weight is the number of admissible factor-pair completions of $Nk+1$. The
weights need not be evaluated to sample from them.

This is genuine source bias, but its atoms are small. Let

\[
\Delta_N=\max_{1\le m<N^2}\tau(m).
\]

Extend the notation by $f_N(0)=1$. Since
$f_N(k)\le\tau(Nk+1)\le\Delta_N$ for $k\ge1$, and the same upper
bound holds at zero, every set
$I\subseteq\{0,\ldots,N-1\}$ of $h$ indices has

\[
\Pr(D_N(U)\in I)\le\frac{h\Delta_N}{\varphi(N)}.
\tag{1.3}
\]

For balanced distinct semiprimes, $\varphi(N)=\Theta(N)$ and
$\Delta_N=N^{o(1)}$. Hence the maximum atom is
$N^{-1+o(1)}$. For $T$ independent samples and an integer width $H$,
a union bound gives

\[
\Pr\bigl(\exists i<j:\ |K_i-K_j|\le H\bigr)
\le
\binom T2\frac{(2H+1)\Delta_N}{\varphi(N)}.
\tag{1.4}
\]

Thus polynomially many independent first-step samples do not localize the
bias through exact collisions or polynomial-width clusters on balanced
semiprimes. This does not control other statistics or the dependent tail of
one descent trajectory.

## 2. Common factors are confined by public index differences

Let $k_1,\ldots,k_m$ be distinct integers with $1\le k_i<N$, and put

\[
A_i=Nk_i+1.
\]

For $i\ne j$,

\[
\boxed{
\gcd(A_i,A_j)=\gcd(A_i,|k_i-k_j|).
}
\tag{2.1}
\]

Indeed,

\[
A_i-A_j=N(k_i-k_j),
\]

and $\gcd(A_i,N)=1$, so the factor $N$ can be removed from the second
gcd argument.

For a positive integer $a$, let $\operatorname{sf}(a)$ be its squarefree
kernel: the product of the primes whose valuations in $a$ are odd.

Suppose $S\subseteq\{1,\ldots,m\}$ is nonempty and

\[
\prod_{i\in S}A_i
\]

is an integer square. Fix $i\in S$. Every prime in
$\operatorname{sf}(A_i)$ must occur to odd valuation in at least one other
$A_j$, $j\in S\setminus\{i\}$. Equation (2.1) then shows that it divides
$|k_i-k_j|$. Therefore

\[
\boxed{
\operatorname{sf}(A_i)
\mid
\prod_{\substack{j\in S\\j\ne i}}|k_i-k_j|.
}
\tag{2.2}
\]

The empty product is $1$, so for a singleton subset this states exactly
that $A_i$ itself is a square.

If all $k_i$ lie in an interval of diameter $H$, every prime in every
selected squarefree kernel is at most $H$. A square dependency is therefore
possible only when each selected $A_i$ is a square times an
$H$-smooth integer.

## 3. A complete clustered square-relation decoder

Assume now that the distinct indices have diameter at most $H\ge1$. The
following deterministic algorithm finds a factor from any nontrivial modular
root produced by an exact square-product subset, or certifies that no subset
of this batch produces such a root.

1. Enumerate the rational primes $\ell\le H$.
2. For each $A_i$, divide out every such prime completely and record the
   full exponent $e_{i,\ell}$. Let the remaining cofactor be $R_i$.
3. Discard $i$ if $R_i$ is not a perfect square. Otherwise write
   $R_i=s_i^2$ and retain the parity vector
   $(e_{i,\ell}\bmod2)_{\ell\le H}$.
4. Compute a basis of the kernel of these parity vectors over
   $\mathbb F_2$.
5. For each basis vector $c$, compute

\[
X(c)=
\prod_i s_i^{c_i}
\prod_{\ell\le H}
\ell^{\frac12\sum_i c_i e_{i,\ell}}
\pmod N,
\tag{3.1}
\]

   and test $\gcd(X(c)-1,N)$ and $\gcd(X(c)+1,N)$.

Equation (2.2) proves completeness of the discard step: an index with
nonsquare $R_i$ cannot occur in any square-product subset. Conversely, for
the retained indices, a parity-kernel vector makes every small-prime exponent
sum even, while every $R_i$ is already a square. Hence its selected product
is exactly $X(c)^2$ over the integers. Since every $A_i\equiv1\pmod N$,

\[
X(c)^2\equiv1\pmod N.
\tag{3.2}
\]

It is enough to test a kernel basis. For two kernel vectors $c,d$, direct
cancellation in (3.1) gives

\[
X(c)X(d)
\equiv
X(c+d)
\prod_{i:c_i=d_i=1}A_i
\equiv X(c+d)\pmod N.
\tag{3.3}
\]

Thus $c\mapsto X(c)$ is a homomorphism from the binary kernel to the roots
of $1\bmod N$. If every basis image is $1$ or $-1$, every kernel image
is $1$ or $-1$. If one basis image is nontrivial, then for odd $N$ its
two gcds expose a proper factor.

Sieve construction, trial division, exact square roots, binary linear
algebra, modular products, and gcds use time polynomial in
$m+H+\log N$. In particular, the decoder is polynomial in the input bit
length when $m,H=\operatorname{poly}(\log N)$.

If repeated indices occur, replace each nonempty equal-index class by one
representative before this decoder. For any selected subset, remove selected
copies in pairs. Each removed pair contributes $A_i^2$, whose positive square
root changes the decoded root by $A_i\equiv1\pmod N$. Thus every original
subset has the same modular-root image as a subset of the one-representative
batch. Conversely, every subset of the reduced batch is available in the
original batch by selecting one copy from each chosen class. This
deduplication preserves all modular-root images. Reducing the available class
size modulo two would be wrong. Alternative factorizations of the same $A_i$
are extra information outside this relation-value decoder.

## 4. A concrete polynomial-time tail algorithm

Let $n=\lceil\log_2(N+1)\rceil$. Fix once and for all an integer constant
$C\ge1$, and set $H(n)=n^C$. For every integer
$2\le u\le\min(H(n),N-1)$, first test $\gcd(u,N)$. On the factor-free
branch, compute the least positive inverse $v\bmod N$ and

\[
k=D_N(u)=\frac{uv-1}{N}<u\le H(n).
\]

Deduplicate the resulting $k$'s and feed the values $Nk+1$ to the decoder
in Section 3. This is one uniform deterministic polynomial-time algorithm. If
any exact square-product relation in the complete small-state pool has a
nontrivial modular root, the algorithm returns a proper factor through the
named square-root decoder. It need not return every factor obtainable from all
combinations.

The same decoder applies to the late part of one P62 trajectory. Once all
retained successor states $k_i=u_{i+1}$ lie in an interval of polynomial
width, the strict descent makes them distinct and the chronology supplies the
factorizations

\[
Nk_i+1=u_i v_i.
\]

The decoder does not require those factorizations, but other decoders may use
them.

For $N=15$ and $H=2$, the small state $u=2$ gives $v=8,k=1$ and

\[
Nk+1=16=4^2.
\]

The decoder returns $4$, and $\gcd(4-1,15)=3$. This is only an exact
example, not a success theorem.

## 5. Remaining theorem

To turn this clustered decoder into a factoring algorithm, one must close the
success gap. The evaluator gap for clustered exact square relations is closed.

A factoring result now needs to prove, on every hard input family, that a
polynomial-width pool produced from bare $N$ contains a parity dependency
whose modular square root is nontrivial with inverse-polynomial probability.
For this clustered-decoder route, support of the selected squarefree kernels
on the public difference set is one necessary structural condition. It is not
sufficient: the parity vectors can stay independent, or every dependency can
decode to $1$ or $-1$. The completion bias in (1.2) is a concrete source-side
effect, but (1.3)--(1.4) show that independent draws are too diffuse for simple
collision or clustering.

The open routes are a dependent descent tail, deliberately correlated starts,
partial-relation large-prime matching, a lattice or continued-fraction use of
the quotients, or a hidden-period/stabilizer construction that uses more than
the relation values. No all-input success probability, expected polynomial
factoring time, or lower bound for those routes is claimed.
