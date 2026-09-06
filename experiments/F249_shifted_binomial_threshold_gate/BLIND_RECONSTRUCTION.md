# F249 blind reconstruction

## Authentication and verdict

Before reading STATEMENT.md, I computed its SHA-256 digest:

> 2b6594484dcb394b58126398d9944ab3e6aa18f8bc2d62e462dcc6e3c18db825

It matches the required digest. I used only that authenticated statement, the
root PROMPT.md, and the root AGENTS.md. I did not use another F249 artifact or
a durable proof or progress ledger.

**Verdict: PASS.** Every algebraic, gcd, floor, endpoint, recurrence,
probability, and carry claim follows from the stated assumptions. The
evaluation claims are valid with their stated method-specific scope. They are
not lower bounds and do not turn this construction into a factoring
algorithm.

## Setup and two elementary facts

Assume

\[
N=pq,\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes. Define

\[
B=\lfloor\sqrt N\rfloor,\qquad
H=\left\lfloor\frac B2\right\rfloor,\qquad
s=B-p,
\]

and, for \(r\geq 1\) and \(1\leq c\leq H\),

\[
C_{r,c}=\binom{rN+c-1}{B}.
\]

The size assumptions give

\[
p<\sqrt N<\sqrt2\,p<\frac32p,\qquad
p\leq B<q,\qquad B<2p.
\]

The least possible pair is \(p=3,q=5\). Thus \(B\geq3\) and \(H\geq1\).
Also, \(s\geq0\) and \(H<p\). For the sharper bound on \(s\), note that
\(2B<3p\), hence \(2B-3p\leq-1\). If \(B\) is even, then

\[
3s=3B-3p=B+(2B-3p)<B=2H.
\]

If \(B\) is odd, then

\[
3s=B+(2B-3p)\leq B-1=2H.
\]

Therefore

\[
3s\leq2H,\qquad 0\leq s<H<p<q,\qquad B<q.
\tag{1}
\]

The prime-modulus coefficient fact used below also has a direct proof. For a
prime \(\ell\), integers \(a,d\geq0\), and \(0\leq b,e<\ell\),

\[
(1+x)^{\ell a+b}=(1+x^\ell)^a(1+x)^b
\quad\text{in }\mathbb F_\ell[x].
\]

Taking the coefficient of \(x^{\ell d+e}\) gives

\[
\binom{\ell a+b}{\ell d+e}
\equiv \binom ad\binom be\pmod\ell.
\tag{2}
\]

The bound \(b<\ell\) ensures that only exponent \(e\) from the second factor
can contribute. This proves the one-digit coefficient rule needed here.

## 1. Exact shifted threshold law

Because \(c-1<p\) and \(B=p+s<2p\), equation (2) modulo \(p\) gives

\[
\binom{rN+c-1}{B}
=\binom{p(rq)+(c-1)}{p+s}
\equiv rq\binom{c-1}{s}\pmod p.
\tag{3}
\]

Because \(c-1<B<q\), equation (2) modulo \(q\) gives

\[
\binom{rN+c-1}{B}
=\binom{q(rp)+(c-1)}B
\equiv\binom{c-1}{B}=0\pmod q.
\tag{4}
\]

The integer \(rq\binom{c-1}{s}\) is also zero modulo \(q\). Equations
(3) and (4), followed by the Chinese remainder theorem, give

\[
\boxed{C_{r,c}\equiv rq\binom{c-1}{s}\pmod N.}
\tag{5}
\]

If \(c\leq s\), the binomial coefficient on the right is zero by convention.
Thus \(C_{r,c}\equiv0\pmod N\). If \(c>s\), then
\(0\leq s\leq c-1<p\), so \(\binom{c-1}{s}\) is nonzero modulo \(p\).
On the screened branch \(\gcd(r,N)=1\), the right side of (5) is divisible
by \(q\) and nonzero modulo \(p\). Hence

\[
\boxed{
\gcd(N,C_{r,c})=
\begin{cases}
N,&1\leq c\leq s,\\
q,&s<c\leq H.
\end{cases}}
\tag{6}
\]

Equation (1) gives \(H>s\), so the public endpoint is deterministic:

\[
\boxed{\gcd(N,C_{1,H})=q.}
\tag{7}
\]

On this promised semiprime domain, the endpoint-gcd function factors \(N\):
it returns \(q\), and then \(p=N/q\). Conversely, a factorization identifies
\(q\) as the larger prime and computes the function. Both reductions have
polynomial overhead. An oracle for \(C_{1,H}\bmod N\) is sufficient because
a gcd gives (7). This does not show how to recover the full coefficient
residue from a factorization.

## 2. Exact Las Vegas accounting

For uniform \(c\in\{1,\ldots,H\}\), exactly \(H-s\) choices are above the
threshold. On the screened branch,

\[
\Pr(\gcd(N,C_{r,c})=q)=\frac{H-s}{H}.
\]

Since (1) gives \(s/H\leq2/3\),

\[
\boxed{\Pr(\gcd(N,C_{r,c})=q)\geq\frac13.}
\tag{8}
\]

Independent sampling with replacement has geometric expected call count

\[
\frac{H}{H-s}\leq3.
\]

The probability of no success after \(k\) calls is at most \((2/3)^k\), so
termination is almost sure. The algorithm returns only a gcd strictly
between \(1\) and \(N\); every returned factor is correct. Exact uniform
sampling by rejection uses \(O(\log H)\) random bits per expected constant
number of attempts. Gcd and verification work is polynomial in the input
length. If one exact coefficient-residue call costs at most a
quasipolynomial \(Q(n)\), total expected cost is at most

\[
3Q(n)+\operatorname{poly}(n),
\]

which is quasipolynomial. The endpoint \(c=H\) needs one deterministic
oracle call.

For general \(r\), first compute \(\gcd(r,N)\). A proper gcd already factors
\(N\). If the gcd is \(N\), use \(r=1\). Equations (6) and (8) apply when the
gcd is \(1\).

If \(s=0\), then \(B=p\), so \(\gcd(N,B)=p\). Also every permitted shift has
\(c>s\) and hence gcd \(q\). No input in the stated domain has \(B<3\).

## 3. Unique recurrence singularity

For \(a\geq B\),

\[
(a+1-B)\binom{a+1}{B}=(a+1)\binom aB.
\]

Taking \(a=rN+c-1\) gives

\[
\boxed{(rN+c-B)C_{r,c+1}=(rN+c)C_{r,c}.}
\tag{9}
\]

Assume \(s\geq1\) and \(1\leq c\leq H-1\). Since \(c<H<p<q\),

\[
\gcd(N,rN+c)=\gcd(N,c)=1.
\tag{10}
\]

For the denominator,

\[
\gcd(N,rN+c-B)=\gcd(N,B-c).
\]

Here

\[
B-H+1\leq B-c\leq B-1<q,
\]

and \(B-c<2p\). Thus \(q\) cannot divide it, and \(p\) can divide it only
when \(B-c=p\). This occurs exactly at \(c=B-p=s\). Since
\(1\leq s\leq H-1\), this edge occurs once:

\[
\boxed{
\gcd(N,rN+c-B)=
\begin{cases}
p,&c=s,\\
1,&c\ne s.
\end{cases}}
\tag{11}
\]

The transition in (6) occurs at the sole denominator that cannot be inverted
modulo \(N\). If \(s=0\), the corresponding denominator is at \(c=0\),
before the sampled range, and the elementary gcd \(\gcd(N,B)=p\) has already
factored the input.

## 4. Complementary central-binomial gate

Let

\[
K_B=\binom BH
=\frac{\prod_{j=B-H+1}^{B}j}{H!}.
\tag{12}
\]

Every factor of \(H!\) is below \(p\), so \(H!\) is a unit modulo \(N\).
Since \(s<H\),

\[
B-H+1\leq p=B-s\leq B.
\]

The numerator interval in (12) contains \(p\). It contains no other multiple
of \(p\), because \(B<2p\), and no multiple of \(q\), because \(B<q\).
Multiplication by the inverse of \(H!\) preserves divisibility by each
hidden prime. Therefore

\[
\boxed{\gcd(N,K_B)=p.}
\tag{13}
\]

Combining (7) and (13) gives

\[
\boxed{\gcd(N,C_{1,H})
=\frac{N}{\gcd(N,K_B)}=q.}
\tag{14}
\]

This is a relation between factor gates, not an equality of coefficient
residues. It directly proves, without using the earlier artifacts named in
the statement, that the endpoint contains no stronger gcd information than
the central-binomial numerator interval. It selects the complementary prime.

For even \(B=2H\), the numerator interval in (12) is
\(\{H+1,\ldots,B\}\). For odd \(B=2H+1\), its lower endpoint is \(H+2\).
Thus the upper-half interval \(\{H+1,\ldots,B\}\) has one extra factor
\(H+1\). In the odd case, \(s\leq H-1\) implies

\[
p=B-s\geq H+2.
\]

Hence \(H+1\) is a unit modulo \(N\). The two odd-\(B\) products have the
same gcd with \(N\), although their exact identities differ.

## 5. Recurrence fast-forward reaches the same gate

Assume \(s\geq1\), and multiply the denominators before the endpoint:

\[
D_r=\prod_{c=1}^{H-1}(rN+c-B).
\]

Modulo \(N\),

\[
D_r\equiv
\prod_{c=1}^{H-1}(c-B)
=(-1)^{H-1}\prod_{j=B-H+1}^{B-1}j
\pmod N.
\tag{15}
\]

The displayed interval contains \(p=B-s\), because
\(1\leq s\leq H-1\). It contains no second multiple of \(p\) and no multiple
of \(q\). Hence

\[
\boxed{\gcd(N,D_r)=p.}
\tag{16}
\]

When \(s\geq1\), \(B=p+s\) is itself a unit modulo \(N\). Adjoining the
missing endpoint \(B\) to the product in (15) gives the numerator interval
of (12) without changing the gcd. A denominator-product fast-forward
therefore reaches a factor-bearing upper-half product before it can invert
the recurrence.

The same obstruction appears in the defining quotient. Write

\[
B!=pU,\qquad
P_{r,c}=\prod_{j=1}^{B}(rN+c-j),\qquad
B!C_{r,c}=P_{r,c}.
\tag{17}
\]

There is exactly one multiple of \(p\) in \(1,\ldots,B\) and no multiple of
\(q\), so \(U\) is a unit modulo \(N\). The factor of \(P_{r,c}\) with
\(j=c\) is \(rN\). Remove it and denote the remaining product by
\(R_{r,c}\). Modulo either hidden prime, its factors reduce to \(c-j\).

There is no further zero modulo \(q\): for \(j\ne c\),
\(0<|j-c|<q\). Modulo \(p\), the only possible second index congruent to
\(c\) is \(j=c+p\). It belongs to \(1,\ldots,B=p+s\) exactly when
\(c\leq s\). Consequently,

\[
\gcd(N,R_{r,c})=
\begin{cases}
p,&c\leq s,\\
1,&c>s.
\end{cases}
\tag{18}
\]

The first case asserts a \(p\)-factor. It does not require the integer
\(p\)-adic valuation to equal one. Cancelling the common hidden factor \(p\)
in (17) gives the exact integer identity

\[
U C_{r,c}=rqR_{r,c}.
\tag{19}
\]

On the factor-free branch, (19) explains (6). Its right side has only the
\(q\)-factor when \(c>s\), and it has both hidden primes when \(c\leq s\).
But (17) modulo \(N\) does not permit this cancellation because \(B!\) is
not invertible. An exact residue of \(B!\), \(D_r\), or the corresponding
upper-half product immediately exposes \(p\) by a gcd. This is the existing
factorial gate, not a coefficient-evaluation method.

## 6. Top multipliers and the beta-two carry relation

Equation (5) gives, for every positive \(r\),

\[
\boxed{C_{r,c}\equiv rC_{1,c}\pmod N.}
\tag{20}
\]

On the factor-free branch, \(r\) is only a public unit multiplier. It does
not change the threshold \(s\) or the singular denominator in (11).

Now define

\[
A_r=(-1)^B\binom{rN-1}{B}.
\]

Modulo \(p\), equation (2) and
\(\binom{p-1}{s}\equiv(-1)^s\pmod p\) give

\[
A_r\equiv
(-1)^B(rq-1)(-1)^s
=1-rq\pmod p,
\tag{21}
\]

where the equality uses that \(p\) is odd and \(B=p+s\). Modulo \(q\),
since \(B<q\),

\[
A_r\equiv(-1)^B\binom{q-1}{B}
\equiv1\equiv1-rq\pmod q.
\tag{22}
\]

Thus \(A_r\equiv1-rq\pmod N\), and

\[
h_r=\frac{A_r-(1-rq)}N
\]

is an integer. Since \(N\) is odd, it has an inverse modulo \(2^t\). Define

\[
z_{r,t}=N^{-1}(A_r-1)\pmod {2^t}.
\]

The exact identity \(A_r-1=Nh_r-rq\) gives

\[
z_{r,t}\equiv h_r-rqN^{-1}
\equiv h_r-rp^{-1}\pmod {2^t},
\]

because \(qN^{-1}\equiv p^{-1}\pmod {2^t}\). Therefore

\[
\boxed{h_r-z_{r,t}\equiv rp^{-1}\pmod {2^t},}
\tag{23}
\]

and subtracting \(r\) times the \(r=1\) instance gives

\[
\boxed{h_r-rh_1\equiv z_{r,t}-rz_{1,t}\pmod {2^t}.}
\tag{24}
\]

The right side uses only public binomial and power-of-two residue data.
Equations (23) and (24) give the exact rank-one limitation. After removing
the public offsets \(z_{r,t}\), each multiplier gives only the same hidden
coordinate \(p^{-1}\), scaled by \(r\). Varying \(r\) gives no independent
hidden coordinate. Exploiting the integer carries \(h_r\) needs additional
information that distinguishes their actual integer lifts, such as a proved
carry evaluator or a sampler with a proved nonuniform bias. The congruences
alone do not provide that information.

## 7. Exact scope of the named evaluation routes

The input length satisfies \(n=\Theta(\log N)\), while

\[
B=\Theta(\sqrt N),\qquad H=\Theta(\sqrt N).
\tag{25}
\]

Thus \(N^\alpha=2^{\Theta(n)}\) for fixed \(\alpha>0\). Such work is not of
the form \(2^{O((\log n)^k)}\).

### Recurrence and product routes

Equations (11), (15), and (16) give the exact obstruction for the literal
recurrence route. Sequential inversion fails at \(c=s\), and batching all
denominators gives a residue whose gcd with \(N\) is already \(p\).
Equations (17) through (19) give the same obstruction for a literal
factorial quotient. These facts describe these representations. They do not
rule out a different coefficient algorithm.

### Vandermonde and Newton routes

At the endpoint,

\[
C_{r,H}
=\binom{(rN-1)+H}{B}
=\sum_{j=0}^{H}\binom Hj\binom{rN-1}{B-j}.
\tag{26}
\]

This is both the Vandermonde expansion and Newton's forward formula, because

\[
\left.
\Delta^j\binom{rN-1+c}{B}\right|_{c=0}
=\binom{rN-1}{B-j}.
\]

The literal formula (26) has \(H+1=2^{\Theta(\log N)}\) terms. Direct
materialization is exponential in \(n\), not numerical quasipolynomial time.
The term count is not a lower bound on every compressed evaluation.

### Standard baby-step/giant-step holonomic products

The recurrence (9) has order one and endpoint distance \(\Theta(H)\). In the
standard product method, take \(m\asymp\sqrt H\), form the degree-\(m\)
polynomial for one block of affine factors, and evaluate it at the
\(O(H/m)\) block offsets with a fast product/remainder tree. Since
\(H/m\asymp m\), fast polynomial arithmetic gives

\[
H^{1/2+o(1)}=N^{1/4+o(1)}
\tag{27}
\]

ring operations. By (25), this named method is exponential rather than
quasipolynomial in the input length. This is an accounting of the standard
method, not a lower bound for all algorithms.

### Power-of-two binomial routines

A binomial computation in \(\mathbb Z/2^t\mathbb Z\) occurs in an auxiliary
ring in which the odd integers \(N,p,q\) are units. It does not encounter or
cancel the nonunit \(p\) in \(\mathbb Z/N\mathbb Z\). A coefficient residue
modulo \(2^t\) is not a residue modulo \(N\). Equations (23) and (24) state
exactly what the auxiliary computation reveals about the carries. These
routines do not, by themselves, evaluate \(C_{r,c}\bmod N\) or perform the
hidden cancellation.

### Algebraic-series and finite-field remote coefficients

If \(B=2H\), the binomial-series identity gives

\[
\boxed{K_B=\binom{2H}{H}=[x^H](1-4x)^{-1/2}.}
\tag{28}
\]

If \(B=2H+1\), then

\[
K_B=\binom{2H+1}{H}
=\frac{2H+1}{H+1}\binom{2H}{H}.
\tag{29}
\]

Here \(H+1<p\), so the denominator is a unit modulo \(N\). The numerator is
\(B<q\). Since \(B<2p\), it can share a factor with \(N\) only when \(B=p\),
which the elementary screen \(\gcd(N,B)\) detects. After that screen, the
ratio in (29) is a public unit modulo \(N\). The odd case therefore has the
same gcd gate as (28), up to this unit.

Fast remote-coefficient algorithms over a finite prime field use the known
prime characteristic as their coefficient-index radix. In Cartier-operator
language, they repeatedly select index residue classes modulo that known
prime. Their preprocessing is polynomial or quasi-linear in the
characteristic. Here the useful prime characteristics are hidden and

\[
p,q=\Theta(\sqrt N)=2^{\Theta(n)}.
\]

Characteristic-sized preprocessing is not numerical quasipolynomial time.
The public ring \(\mathbb Z/N\mathbb Z\) is not a prime field. It has the
hidden zero divisors \(p\) and \(q\), and it does not supply the known prime
radix required by that method. Thus the named finite-field algorithm is not
directly applicable and does not give a numerical-quasipolynomial evaluator
here.

## Final scope

This reconstruction proves an exact factor oracle conditional on evaluating
one remote coefficient modulo \(N\). It proves that the public endpoint is
the complementary central-binomial or upper-half product gate. It also
identifies the sole nonunit recurrence denominator and the rank-one form of
the top-multiplier carry family.

It does not supply the missing remote-coefficient evaluator. The named routes
either expose the existing factorial gate, have exponential literal size or
standard running time, or operate in a ring that does not perform the hidden
cancellation. These are representation-specific boundaries, not an
impossibility theorem. The surviving target is a new
numerical-quasipolynomial algorithm for \(K_B\bmod N\), \(C_{r,c}\bmod N\),
or the relevant hidden divisibility that avoids first materializing a
factor-bearing factorial or interval product.
