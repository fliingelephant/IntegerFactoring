# SUCCESS — independent end-to-end reconstruction

## Verdict and conventions

All substantive claims in the supplied theorem are correct. The decoder is
complete for the stated conditional target: useful exact-square relations in
a batch of distinct numerical indices of diameter at most $H$. It does not
prove that such a relation exists on every input.

I use these standard conventions.

1. In the definition of $\Delta_N$, the maximum is over positive integers
   $1\le m<N^2$, since $\tau$ is defined on positive integers.
2. A relation space contains its zero vector (the empty subset), whose root
   image is $1$. With this convention, duplicate compression preserves
   exactly all root images. If one excludes the empty subset but permits
   nonempty duplicate pairs, exact equality can differ only by the identity
   image $1$; all useful non-global images are still preserved.

An interval of width $H$ means numerical index diameter at most $H$. Merely
taking a polynomial number of consecutive trajectory times does not itself
give the diameter condition.

## 1. Reverse fibres and the law of \(D_N\)

Let $u$ be a unit modulo $N$, and let
$v\in\{1,\ldots,N-1\}$ be its least positive inverse. There is a unique
integer $k\ge0$ such that

\[
uv=Nk+1.
\]

Since $v<N$, we have $Nk=uv-1<uN$, so $k<u<N$. If $k=0$, then
$uv=1$, and hence $u=v=1$. Thus the fibre at zero has size one.

Now fix $1\le k<N$. Every unit $u$ in the fibre at $k$ is a divisor of
$Nk+1$ and satisfies $k<u<N$. Conversely, suppose

\[
u\mid Nk+1,\qquad k<u<N.
\]

Put $v=(Nk+1)/u$. It is positive, and $k\le u-1$ gives

\[
Nk+1\le N(u-1)+1<Nu,
\]

so $v<N$. Also, every common divisor of $u$ and $N$ divides both $Nk+1$
and $Nk$, and therefore divides $1$. Thus $u$ is a unit, $v$ is its least
positive inverse, and $D_N(u)=k$. This proves

\[
\#D_N^{-1}(k)=f_N(k)\quad(1\le k<N),
\qquad
\#D_N^{-1}(0)=1=f_N(0).
\]

Uniformity over the $\varphi(N)$ units now gives

\[
\Pr(D_N(U)=k)=\frac{f_N(k)}{\varphi(N)}.
\]

For $k\ge1$, $Nk+1<N^2$, and each counted $u$ is a divisor of $Nk+1$.
Hence $f_N(k)\le\Delta_N$. The same is true at zero because
$f_N(0)=1\le\Delta_N$. Therefore every set $S$ of $h$ indices satisfies

\[
\Pr(D_N(U)\in S)\le\frac{h\Delta_N}{\varphi(N)}.
\]

Let $K_1,\ldots,K_T$ be independent copies. For fixed $K_i$, the interval
at distance at most $H$ contains at most $2H+1$ integer indices. Thus

\[
\Pr(|K_i-K_j|\le H)
\le \frac{(2H+1)\Delta_N}{\varphi(N)}.
\]

A union bound over unordered pairs proves

\[
\Pr\!\left(\exists i<j:\ |K_i-K_j|\le H\right)
\le {T\choose2}\frac{(2H+1)\Delta_N}{\varphi(N)}.
\]

### Negligibility for distinct semiprimes

For every fixed $\epsilon>0$, choose a constant $P$ such that
$p^{\epsilon/2}\ge2$ for every prime $p>P$. If
$m=\prod p^{a_p}$, then the contribution of primes above $P$ to $\tau(m)$
is at most

\[
\prod_{p>P}(a_p+1)
\le\prod_{p>P}2^{a_p}
\le\prod_{p>P}p^{\epsilon a_p/2}
\le m^{\epsilon/2}.
\]

There are only constantly many primes at most $P$, and each corresponding
exponent is at most $\log_2m$. Their contribution is at most

\[
(1+\log_2m)^{\pi(P)}\le m^{\epsilon/2}
\]

for all sufficiently large $m$. Hence $\tau(m)\le m^\epsilon$ eventually.
Uniformly over $m<N^2$, this gives $\Delta_N\le N^{2\epsilon}$ for all
sufficiently large $N$, after enlarging the threshold to cover the finitely
many smaller values of $m$.

If $N=pq$ with distinct primes, then

\[
\varphi(N)=N(1-1/p)(1-1/q)\ge N/3,
\]

because the two primes are at least $2$ and $3$. Taking $\epsilon=1/8$, the
collision bound is a polynomial in $n$ times at most $N^{-3/4}$ whenever
$T$ and $H$ are polynomial in $n$. Since $N\ge2^{n-1}$, this is negligible
in $n$. Balance is not needed for this particular estimate, so the claimed
balanced distinct-semiprime case follows.

## 2. Common divisors and clustered dependencies

Let $A_i=Nk_i+1$ for distinct $k_i,k_j\in[1,N-1]$, and put
$d=|k_i-k_j|>0$. Since $\gcd(A_i,N)=1$,

\[
\begin{aligned}
\gcd(A_i,A_j)
 &=\gcd(A_i,A_j-A_i)\\
 &=\gcd(A_i,N(k_j-k_i))\\
 &=\gcd(A_i,d).
\end{aligned}
\]

Suppose a nonempty product $\prod_{i\in S}A_i$ is an integer square. Fix
$i\in S$, and let $p$ occur to odd valuation in $A_i$. The total
$p$-valuation is even, so some $A_j$ with $j\in S\setminus\{i\}$ is
divisible by $p$. The gcd identity gives

\[
p\mid |k_i-k_j|.
\]

Every prime in $\operatorname{sf}(A_i)$ therefore divides at least one factor
of the following product:

\[
\operatorname{sf}(A_i)
\mid\prod_{j\in S\setminus\{i\}}|k_i-k_j|.
\]

For a singleton square relation, $\operatorname{sf}(A_i)=1$, so the formula
holds with the empty product equal to $1$. If the selected indices have
diameter at most $H$, every prime on the right is at most $H$. Thus each
selected squarefree kernel is $H$-smooth.

## 3. Complete deterministic clustered decoder

Assume the input indices are distinct and

\[
\max_i k_i-\min_i k_i\le H.
\]

The decoder is as follows.

1. Use a deterministic sieve to list all primes $p\le H$.
2. For each $A_i=Nk_i+1$, remove the full power of every such prime. Record
   $e_{p,i}=v_p(A_i)$ and call the residual cofactor $q_i$. Compute
   $\lfloor\sqrt{q_i}\rfloor$. Discard column $i$ unless $q_i$ is a square.
3. On retained columns form
   $M_{p,i}=e_{p,i}\bmod2$ over $\mathbb F_2$. Compute a basis
   $b_1,\ldots,b_r$ for $\ker M$.
4. For every basis vector $b_t$, form the exact positive integer
   \[
   x_t=\sqrt{\prod_{i:(b_t)_i=1}A_i}.
   \]
   Reduce $x_t$ modulo $N$. Test $\gcd(x_t-1,N)$ and
   $\gcd(x_t+1,N)$. Return any gcd strictly between $1$ and $N$.
5. If none yields a factor, report that the batch contains no exact square
   subset with a non-global root modulo $N$.

The square root in step 4 is exact: each residual $q_i$ is a square, and a
kernel vector makes every total small-prime valuation even. It can also be
constructed directly from the stored roots $\sqrt{q_i}$ and half of the
summed small-prime valuations.

### Discarding loses no true relation

Let $S$ be any exact square subset of the original batch. Section 2 shows
that every prime occurring oddly in any selected $A_i$ is at most $H$.
After all such small primes are removed, its residual $q_i$ is a square.
Thus no member of $S$ is discarded. Among retained columns, a subset has
square product exactly when its indicator is in $\ker M$. The kernel
therefore contains every exact square subset that could be useful.

### A kernel basis is sufficient

Let $\mathcal K=\ker M$, with addition given by symmetric difference. For
$S\in\mathcal K$, define

\[
\rho(S)=\sqrt{\prod_{i\in S}A_i}\pmod N.
\]

For $S,T\in\mathcal K$, positivity gives the exact identity

\[
\sqrt{\prod_{i\in S}A_i}\,
\sqrt{\prod_{i\in T}A_i}
=\left(\prod_{i\in S\cap T}A_i\right)
\sqrt{\prod_{i\in S\triangle T}A_i}.
\]

Every $A_i\equiv1\pmod N$, so

\[
\rho(S\triangle T)=\rho(S)\rho(T)\pmod N.
\]

Thus $\rho$ is a homomorphism from the relation vector space to the group of
square roots of $1$ modulo $N$. If every basis image lies in
$\{1,-1\}$, every image does. Contrapositively, if any exact square subset
has a non-global image, at least one basis vector has a non-global image.
This proves basis-only completeness and the final negative certificate.

### Factor extraction and edge cases

Let $x^2\equiv1\pmod N$, with $x\not\equiv1,-1\pmod N$. If
$\gcd(x-1,N)=1$, then $x-1$ is invertible modulo $N$, so
$N\mid(x-1)(x+1)$ would imply $x\equiv-1\pmod N$, a contradiction. The gcd
also cannot equal $N$, since that would imply $x\equiv1\pmod N$. Hence

\[
1<\gcd(x-1,N)<N.
\]

The same argument applies to $x+1$. It uses no squarefreeness assumption and
no restriction on prime-power exponents. In fact it works for every
$N\ge2$, not only odd $N$. For a pure odd prime power there is no
non-global root: $\gcd(x-1,x+1)\mid2$, so an odd prime power dividing their
product must divide one factor in full. Thus the implication is vacuous
there. Repeated prime powers inside a general odd composite cause no problem.
On an even composite, a
globally signed root can additionally expose the factor $2$; this cannot
damage correctness. A singleton relation is already covered: its zero
parity column is a kernel relation, and its exact root is tested.

### Bit complexity

Each $A_i<N^2$, so it has $O(\log N)$ bits. A sieve through $H$ uses space
and bit time polynomial in $H$. Exhaustive valuation extraction makes a
polynomial number of divisions in $m+H+\log N$, each on
$O(\log N)$-bit integers. Exact square testing is polynomial in $\log N$.
The parity matrix has at most $H$ rows and $m$ columns, so Gaussian
elimination is polynomial in $m+H$.

There are at most $m$ basis relations. A relation product has
$O(m\log N)$ bits. Multiplication, exact square root, modular reduction, and
gcd computation all have deterministic polynomial bit complexity at this
length. Therefore the complete decoder has a fixed bit-time bound polynomial
in

\[
m+H+\log N.
\]

This count includes prime generation, valuation extraction, matrix storage
and elimination, all large intermediate products, square roots, and gcds.
The decoder invokes no factoring or order-finding oracle.

## 4. Repeated equal indices

Group equal indices into classes $c$. Let their common value be $A_c$, and
let the available multiplicity be $r_c\ge1$. A subset of occurrences is
described by counts $0\le t_c\le r_c$. Put
$\epsilon_c=t_c\bmod2$. Then

\[
\prod_c A_c^{t_c}
=\left(\prod_c A_c^{\lfloor t_c/2\rfloor}\right)^2
 \prod_{c:\epsilon_c=1}A_c.
\]

Thus the occurrence product is a square exactly when the product of one
representative from every odd-count class is a square. In that event,

\[
\sqrt{\prod_c A_c^{t_c}}
=\left(\prod_c A_c^{\lfloor t_c/2\rfloor}\right)
 \sqrt{\prod_{c:\epsilon_c=1}A_c}.
\]

The prefactor is $1$ modulo $N$, because every $A_c=Nk_c+1$. The two root
images are equal. Conversely, every parity pattern is realizable by choosing
zero or one occurrence from each nonempty class. One representative per
nonempty class therefore preserves exactly the root-image set. The parity of
the available multiplicity $r_c$ is irrelevant: even when $r_c$ is even, a
subset can choose one occurrence.

The all-even pattern maps to the compressed empty relation and image $1$.
This is why the zero relation must be included when exactly all images is
read literally. If only useful non-global images matter, this convention
does not affect the decoder.

## 5. Uniform small-state enumeration

Let $n=\lceil\log_2(N+1)\rceil$. Fix an explicit constant exponent $C\ge1$,
take an integer rounding of $H=n^C$, and set

\[
B=\min(H,N-1).
\]

For each $u=2,\ldots,B$, first compute $d=\gcd(u,N)$. If $d>1$, then
$d<N$ because $u<N$, so this is already a proper factor. Otherwise compute
the least positive inverse $v$ by the extended Euclidean algorithm and set

\[
k=\frac{uv-1}{N}.
\]

No oracle is hidden in the phrase factor-free: a nonunit is detected by this
gcd and immediately factors $N$. For every surviving $u\ge2$, the equality
$uv=1$ is impossible, while $v<N$. Hence

\[
1\le k<u\le B\le H.
\]

After retaining one representative of each repeated $k$, the pool has
distinct indices, size at most $H$, and numerical diameter at most $H$.
Section 4 shows that deduplication loses no useful root image. The clustered
decoder therefore returns a proper factor whenever this pool contains a
useful exact square relation, and otherwise gives its negative certificate.

For fixed $C$, enumeration uses $O(n^C)$ gcd and inverse computations on
$O(n)$-bit integers. The decoder parameters $m,H$ are polynomial in $n$.
This is a uniform deterministic polynomial-time conditional factoring
algorithm. The same reasoning applies to any other set of distinct
successor-state indices contained in a numerical interval of polynomial
width. Their origin in a descent trajectory, and the word late, add no
further mathematical requirement.

## 6. Exact scope

The reconstruction proves:

- the exact reverse-fibre law and its collision bound;
- confinement of odd prime valuations in clustered exact-square relations;
- a deterministic polynomial-bit-complexity decoder complete for all useful
  relations in such a cluster;
- correctness for zero fibres, singleton relations, duplicate classes,
  repeated prime powers, and even inputs; and
- the conditional small-state and polynomial-width-interval algorithms.

It does not prove that every integer supplies a useful relation, that a
descent reaches such an interval in polynomial depth, or that a random batch
has a useful relation with inverse-polynomial probability. Accordingly, it
does not by itself give an all-input polynomial-time factoring algorithm.
