# Proof-blind reconstruction of claims A–C

## Verdict

Claims A, B, and C are correct with the boundaries stated in the supplied
statement. Claim B gives an infinite independent submatrix. It does not give
a null for the complete source, a square dependency, or a factorization
obstruction.

No computation is used. The only external results used are the prime number
theorem, the Chinese remainder theorem, and Linnik's theorem. Dirichlet's
theorem is implicit in the prime-in-progression conclusion and is not needed
separately.

## A. Exact carry laws

Let

\[
A_k=1+kN,\qquad A_\ell=1+\ell N,
\]

where \(k\ne\ell\). Since \(\gcd(A_k,N)=1\), a common divisor of \(A_k\)
and \(A_\ell\) divides

\[
A_k-A_\ell=(k-\ell)N
\]

and is coprime to \(N\). It therefore divides \(|k-\ell|\). Conversely, a
divisor of \(A_k\) and \(|k-\ell|\) divides

\[
A_\ell=A_k+(\ell-k)N.
\]

Thus

\[
\gcd(A_k,A_\ell)=\gcd(A_k,|k-\ell|).
\]

Interchanging \(k\) and \(\ell\) gives

\[
\gcd(1+kN,1+\ell N)
=\gcd(1+kN,|k-\ell|)
=\gcd(1+\ell N,|k-\ell|).
\]

Now let \(r\) be prime and \(r\nmid N\). Then

\[
r\mid1+kN
\quad\Longleftrightarrow\quad
k\equiv-N^{-1}\pmod r.
\]

This is one residue class modulo \(r\).

Let \(K\) have diameter \(D\). An interval of length \(D\) contains at most

\[
1+\left\lfloor\frac Dr\right\rfloor
\]

integers in one residue class modulo \(r\). The odd-valuation row for \(r\)
is supported on a subset of the columns divisible by \(r\). Its degree has
the same upper bound.

Finally fix \(k\in K\) and suppose its column has no private odd-valuation
row. For each prime \(r\) with odd valuation in \(1+kN\), the row for \(r\)
contains another column \(\ell\ne k\). Hence \(r\) divides both exact values,
so the gcd identity gives

\[
r\mid |k-\ell|.
\]

Every prime in \(\operatorname{sf}(1+kN)\) therefore divides

\[
\prod_{\ell\in K,\,\ell\ne k}|k-\ell|.
\]

The left side is squarefree, so the individual divisibilities combine to

\[
\operatorname{sf}(1+kN)
\mid
\prod_{\ell\in K,\,\ell\ne k}|k-\ell|.
\]

## B. Infinite cross-pair submatrix

### B.1 Bases and distinct carries

Let

\[
b_1<b_2<\cdots<b_t
\]

be the first \(t\) odd primes, and put \(A=b_t\). The prime number theorem
gives

\[
A=\Theta(t\log t),
\qquad
\sum_{i=1}^t\log b_i=\Theta(t\log t).
\]

For every ordered pair \(\alpha=(i,j)\) with \(i\ne j\), define

\[
c_\alpha=b_i^2b_j,
\qquad
k_\alpha=c_\alpha-1.
\]

There are

\[
M=t(t-1)
\]

such pairs. Unique factorization shows that the \(c_\alpha\), and therefore
the \(k_\alpha\), are distinct: the prime with exponent two identifies
\(i\), and the prime with exponent one identifies \(j\). Also

\[
1\le k_\alpha<A^3.
\]

Thus the carry diameter is less than \(A^3\).

Put

\[
L=\prod_{i=1}^t b_i^2.
\]

Every \(c_\alpha\) divides \(L\).

### B.2 One protected prime for every selected value

The prime number theorem gives more than \(t(t-1)\) primes in

\[
(2A^3,4A^3]
\]

for all sufficiently large \(t\), because the number of primes in this
interval is \(\Theta(A^3/\log A)\), which is larger than \(t^2\).

Choose distinct primes \(r_\alpha\) in that interval, one for each ordered
pair. They are different from all base primes, and

\[
r_\alpha>2A^3>|k_\alpha-k_\beta|
\]

for all \(\alpha,\beta\).

Define the even modulus

\[
Q=2L\prod_\alpha r_\alpha^2.
\]

The moduli \(2L\) and \(r_\alpha^2\) are pairwise coprime. Since
\(0<k_\alpha<r_\alpha\), the Chinese remainder theorem gives one reduced
residue \(z\pmod Q\) satisfying

\[
z\equiv1\pmod {2L},
\]

and, for every \(\alpha\),

\[
z\equiv(r_\alpha-1)k_\alpha^{-1}pmod {r_\alpha^2}.
\]

The residue \(z\) is a unit modulo \(Q\). It is not one modulo \(Q\). Indeed,
if it were one modulo some \(r_\alpha^2\), then

\[
k_\alpha\equiv r_\alpha-1\pmod {r_\alpha^2},
\]

which is impossible because \(0<k_\alpha<A^3<r_\alpha-1\).

### B.3 The semiprime

Apply Linnik's theorem to the two reduced residue classes

\[
1\pmod Q,
\qquad
z\pmod Q.
\]

Choose primes \(p_t,q_t\) in these classes with

\[
p_t,q_t\le C Q^\lambda

\]

for absolute constants \(C,\lambda\). Put

\[
N_t=p_tq_t.
\]

Both primes are odd because both residue classes are one modulo two. They are
distinct because \(z\not\equiv1\pmod Q\). Hence \(N_t\) is an odd product of
two distinct primes and is not a perfect power.

The defining congruences give

\[
N_t\equiv z\pmod Q,
\qquad
N_t\equiv1\pmod L.
\]

### B.4 Size and menu bounds

The selected private primes satisfy \(\log r_\alpha=\Theta(\log t)\). Hence

\[
\log Q
=\log 2+2\sum_i\log b_i+2\sum_\alpha\log r_\alpha
=\Theta(t^2\log t).
\]

Any prime congruent to one modulo \(Q\) is larger than \(Q\), so
\(p_t>Q\). Linnik's upper bound therefore gives

\[
\log N_t=\Theta(\log Q)=\Theta(t^2\log t).
\]

If \(n_t\) is the bit length of \(N_t\), then

\[
n_t=\Theta(t^2\log t),
\qquad
\log n_t=\Theta(\log t),
\]

and consequently

\[
M=t(t-1)=\Theta\!\left(\frac{n_t}{\log n_t}\right).
\]

The largest base satisfies

\[
A=\Theta(t\log t)=o(n_t),
\]

so every \(b_i\) is in the source range \(2\le b_i\le n_t\) for large
\(t\). The exponent is two, and therefore is at most \(n_t^2\).

Also \(c_\alpha\le A^3<N_t\) for large \(t\). Thus the canonical residue at
the named attempt is the ordinary integer \(c_\alpha\). For an unordered pair
\(b_i<b_j\), the two menu orientations give \(b_i^2b_j\) and \(b_ib_j^2\).
Over all unordered pairs, these are exactly the \(t(t-1)\) ordered values
\(c_\alpha\).

It remains to check trial hardness. The congruence \(q_t\equiv1\pmod L\)
implies \(q_t\ge L+1\). Since

\[
\log L=\Theta(t\log t)
\]

while \(\log(n_t^2)=O(\log t)\), both \(q_t\) and \(p_t>Q\) exceed
\(n_t^2\) for sufficiently large \(t\).

### B.5 Exact carries, protected valuations, and independence

Fix \(\alpha\) and abbreviate \(c=c_\alpha\), \(k=k_\alpha=c-1\). Because
\(c\mid L\) and \(N_t\equiv1\pmod L\),

\[
c\mid 1+(c-1)N_t.
\]

Define

\[
w=\frac{1+(c-1)N_t}{c}.
\]

This is positive, satisfies \(cw\equiv1\pmod {N_t}\), and is less than
\(N_t\), since

\[
1+(c-1)N_t<cN_t.
\]

It is therefore the least positive inverse of \(c\), and

\[
\kappa_{N_t}(c)=c-1=k,
\qquad
P_{N_t}(c)=1+kN_t.
\]

The selected exact values are distinct because their carries are distinct.

Modulo \(r_\alpha^2\), the CRT condition gives

\[
1+k_\alpha N_t
\equiv
1+k_\alpha z
\equiv
1+(r_\alpha-1)
\equiv r_\alpha
\pmod {r_\alpha^2}.
\]

Thus

\[
v_{r_\alpha}(1+k_\alpha N_t)=1.
\]

For \(\beta\ne\alpha\), if \(r_\alpha\) divided
\(1+k_\beta N_t\), the unique carry class modulo \(r_\alpha\) would give

\[
k_\beta\equiv k_\alpha\pmod {r_\alpha}.
\]

Both carries lie strictly between zero and \(A^3<r_\alpha\), so this would
force equality, a contradiction. Therefore \(r_\alpha\) has valuation one in
its selected value and valuation zero in every other selected value.

Each selected column has its own private row. In any binary linear relation,
inspection of that row forces the corresponding coefficient to be zero.
Doing this for every column proves that all \(M\) selected square-class
columns are linearly independent.

### B.6 Named endpoint sign screens

For large \(t\),

\[
L>A^6+1.
\]

Both prime factors of \(N_t\) exceed \(L\): \(p_t>Q>L\), and
\(q_t\ge L+1\). Hence both factors exceed \(c_\alpha^2+1\) for every
selected \(c_\alpha\).

Since \(c\) is a unit and \(w\) is its inverse,

\[
\gcd(c-w,N_t)=\gcd(c^2-1,N_t),
\qquad
\gcd(c+w,N_t)=\gcd(c^2+1,N_t).
\]

Neither prime factor can divide the positive integers \(c^2-1\) or
\(c^2+1\), which are both smaller than the factors. Thus both named endpoint
sign gcds are one.

If the same canonical residue \(c\) occurred earlier in the source, its least
positive inverse and its sign screens are unchanged. This proves the screen
claim for that earlier occurrence too.

A different earlier residue \(d\) can have the same positive exact value
\(P_{N_t}(d)=P_{N_t}(c)\). Exact-value deduplication then retains one column
for that same integer. Its valuation row is unchanged, so the private-row and
independence claims survive. But the endpoint screen for \(d\) depends on
\(d^2\pm1\), not on the integer value alone. The proof above gives no screen
claim for \(d\), and gives no claim that execution reaches the named attempt.

## C. Exact boundary and missing gates

### C.1 Stable private rows after the complete source

For a protected row \(r_\alpha\) to stay private, the complete distinct-value
matrix must contain the selected value and must satisfy

\[
v_{r_\alpha}(P_\alpha)\equiv1\pmod2,
\qquad
v_{r_\alpha}(P)\equiv0\pmod2
\]

for every other retained exact value \(P\). A stronger sufficient arithmetic
condition is that no other full-source carry is congruent to
\(k_\alpha\pmod {r_\alpha}\). Claim B proves this only among the selected
\(M\) carries. Seed, frozen, and other all-pairs values can reuse the row.

For an operational claim about the stopping source, one must also prove that
no earlier residue or endpoint sign screen terminates execution before the
value is retained. Claim B does not do this.

### C.2 A nonzero exact square dependency

Let \(M_{\rm full}\) be the full exact valuation-parity matrix. The exact
missing condition is

\[
\ker M_{\rm full}\ne\{0\}.
\]

Equivalently, one must give a nonempty set of distinct retained exact values
whose product is an integer square. Column count, row reuse, or the existence
of many selected values does not by itself prove this.

Indeed, the private rows in Claim B prove the opposite statement for its
selected submatrix. If those rows remain private in the full source, every
full dependency has coefficient zero on every protected column. Stable
private rows cannot themselves create a dependency.

### C.3 A non-global root that factors the semiprime

Suppose a nonzero dependency has exact positive square root \(R\). Every
inverse relation is one modulo \(N_t\), so

\[
R^2\equiv1\pmod {N_t}.
\]

The further missing condition is

\[
R\not\equiv\pm1\pmod {N_t}.
\]

For \(N_t=p_tq_t\) with distinct odd primes, this means that the signs of
\(R\) are different in the two prime components. Consequently

\[
\gcd(R-1,N_t),\qquad \gcd(R+1,N_t)
\]

are the two proper prime factors. Dependency existence alone does not imply
this condition; every dependency root can still be global.

## Final scope

The construction proves a cross-pair private-row submatrix of size
\(\Theta(n/\log n)\). It does not prove stable private rows after the complete
source, a full-source null, a nonzero dependency, a non-global root, or the
absence of an earlier direct factor. It proves no arbitrary-input factoring
algorithm and makes no publication-novelty claim.
