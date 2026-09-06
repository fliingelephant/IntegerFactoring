# Proof of the F172 constant-capacity family

## 1. The CRT class is reduced

The moduli $8$, $p$, $3^v$, and $M$ in (1) are pairwise coprime. Each
prescribed residue is a unit modulo its modulus. Therefore the Chinese
remainder theorem gives one reduced class $a_p\pmod{H_p}$.

Linnik's theorem gives absolute constants $c,L_0$ such that the least prime
in this class satisfies

\[
q\le cH_p^{L_0}.
\tag{10}

Because $q\equiv1\pmod p$, write $q=1+tp$ with $t\ge0$. The cases $t=0$
and $t=1$ give respectively $q=1$ and the even integer $q=p+1>2$.
Neither is prime. Thus $t\ge2$ and

\[
q>2p.
\tag{11}

In particular, $p$ and $q$ are distinct odd primes.

## 2. The ordinary shifted gcd

First consider an odd prime $\ell\ge5$ dividing $p-1$. Then $\ell\mid M$,
so (1) gives $q\equiv2\pmod\ell$. Hence $q-1\equiv1\pmod\ell$, and no such
$\ell$ divides $\gcd(p-1,q-1)$.

Since $p\equiv1\pmod3$, all of the factor $3^v$ in $p^2-1$ lies in $p-1$.
If $v=1$, (1) gives $3\mid q-1$, while $9\nmid p-1$. If $v\ge2$, then

\[
q-1\equiv3\pmod{3^v},
\]

so $v_3(q-1)=1$. In either case the common $3$-part is exactly $3$.

Finally, $q\equiv3\pmod8$ gives $v_2(q-1)=1$. Since $p$ is odd,
$2\mid p-1$, so the common $2$-part is exactly $2$. This proves

\[
\gcd(p-1,q-1)=6.
\]

## 3. The two torus shifted gcds

Let $\ell\ge5$ divide $p-1$. Again $q\equiv2\pmod\ell$, so
$q+1\equiv3\pmod\ell$. Because $\ell\ne3$, it does not divide $q+1$.
Also $q\equiv1\pmod3$, so $3\nmid q+1$. Thus
$\gcd(p-1,q+1)$ is a power of two.

The congruence $q\equiv3\pmod8$ gives $v_2(q+1)=2$. Therefore

\[
\gcd(p-1,q+1)=2^{\min(v_2(p-1),2)}\in\{2,4\}.
\]

Now let an odd prime $\ell\ge5$ divide $p+1$. It also divides $M$, so
$q\equiv2\pmod\ell$ and $q-1\equiv1\pmod\ell$. The prime $3$ does not
divide $p+1$, because $p\equiv1\pmod3$. Thus
$\gcd(p+1,q-1)$ is a power of two. Since $v_2(q-1)=1$, it equals exactly
$2$. This proves (4) and (5).

The same odd-prime argument gives $q+1\equiv3\pmod\ell$ for every
$\ell\ge5$ dividing $p+1$. Again $3\nmid p+1$. Hence
$\gcd(p+1,q+1)$ is a power of two. Since $v_2(q+1)=2$, it lies in
$\{2,4\}$. This proves (5a).

## 4. Common-order bounds

The multiplicative groups of the two fields have orders $p-1$ and $q-1$.
An ordinary element of exact order $A$ in both fields therefore satisfies

\[
A\mid\gcd(p-1,q-1)=6.
\]

For any unit discriminant, put $\epsilon_p=(D/p)$ and
$\epsilon_q=(D/q)$. The two local norm-one torus groups are cyclic of orders
$p-\epsilon_p$ and $q-\epsilon_q$. A torus point of exact order $B$ in both
groups therefore satisfies

\[
B\mid\gcd(p-\epsilon_p,q-\epsilon_q).
\]

The four orientation pairs are exactly (3), (4), (5), and (5a). A
Jacobi-minus-one discriminant uses one of the two mixed pairs. Taking the
least common multiple of all maximal divisibility bounds gives

\[
\operatorname{lcm}(6,4,2)=12.
\]

This bound is independent of the public source and of how effectively it
finds elements inside the available local groups.

## 5. Quantitative size

The odd part $3^vM$ of $p^2-1$ is smaller than $p^2$. Hence

\[
H_p=8p3^vM<8p^3.
\]

By (10),

\[
q\le c(8p^3)^{L_0}=p^{O(1)}.
\]

Together with $q>2p$, this gives

\[
2\log_2p+O(1)le\log_2N\le(3L_0+1)\log_2p+O(1).
\]

Thus $\log p=\Theta(n)$ and $p=2^{\Theta(n)}$. Since $q>p$, both hidden
primes exceed every fixed polynomial in $n$ after a finite prefix.

For a fixed quasipolynomial

\[
Q(n)=2^{C(\log_2(n+1))^k},
\]

we have $\log_2 Q(n)=o(n)$, whereas
$\log_2\sqrt N=\Theta(n)$. Therefore

\[
12<\frac{\sqrt N}{Q(n)}
\]

for all sufficiently large members. The dual common-order state cannot
reach the F170 CRT threshold on this family.

## 6. Infinitude and scope

Dirichlet's theorem supplies infinitely many primes $p\equiv1\pmod3$.
For each such $p$, the construction gives a prime $q>2p$. The resulting
semiprimes are distinct and unbounded.

The proof makes no claim that an attempted state update is inert. If hidden
orders or equality patterns differ, the updater may factor $N$. The theorem
only proves that a no-factor branch cannot accumulate a large exact common
order, because no such common order exists in the ambient local groups.
