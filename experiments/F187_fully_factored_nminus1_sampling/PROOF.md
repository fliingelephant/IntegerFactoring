# Proof of the F187 fully factored \(N-1\) sampling theorem

## 1. Local root groups

Let

\[
R_i=p_i^{e_i},
\qquad
H_i=(\mathbb Z/R_i\mathbb Z)^\times,
\qquad
|H_i|=h_i=p_i^{e_i-1}(p_i-1).
\tag{1}
\]

The group \(H_i\) is cyclic because \(p_i\) is odd. Since
\(p_i\mid N\),

\[
\gcd(N-1,p_i)=1.
\tag{2}
\]

It follows that

\[
d_i=\gcd(N-1,h_i)=\gcd(N-1,p_i-1).
\tag{3}
\]

The local root group

\[
K_i=\{x\in H_i:x^{N-1}=1\}
\tag{4}
\]

is therefore cyclic of order \(d_i\). Its order is coprime to \(p_i\).
Reduction from \(H_i\) to
\((\mathbb Z/p_i\mathbb Z)^\times\) has a \(p_i\)-group kernel, so it is
injective on \(K_i\). Consequently, for every \(x\in K_i\) and every
integer \(k\),

\[
x^k=1\pmod {p_i}
\quad\Longleftrightarrow\quad
x^k=1\pmod {p_i^{e_i}}.
\tag{5}
\]

This injectivity is what makes all stripping gcds select complete hidden
prime-power components even when \(N\) is not squarefree.

## 2. Proof of the deterministic trichotomy

If \(G_0=1\), then for every component

\[
a^{m}\ne1\pmod {p_i}.
\tag{6}
\]

For \(k\mid m\), the implication

\[
a^k=1\pmod {p_i}\Longrightarrow a^m=1\pmod {p_i}
\tag{7}
\]

proves \(\gcd(a^k-1,N)=1\). This proves the complete-nonreturn assertion.

Now assume \(G_0=N\). Put

\[
o_i=\operatorname{ord}_{R_i}(a).
\tag{8}
\]

Every \(o_i\mid m\), and each \(a\bmod R_i\) lies in \(K_i\). During
stripping, the maintained \(R\) is a common multiple of every \(o_i\).
For a prime \(q\mid R\), equation (5) shows

\[
\gcd(a^{R/q}-1,N)
=\prod_{o_i\mid R/q}R_i.
\tag{9}
\]

Thus a gcd equal to \(N\) means every local order divides \(R/q\), so the
copy of \(q\) can be deleted. A gcd equal to one means no local order divides
\(R/q\), so every local order needs the current \(q\)-adic valuation. A
proper gcd is already a factor.

If no proper gcd occurs, deleting all globally unnecessary prime copies and
retaining all globally necessary copies leaves

\[
o_1=\cdots=o_s=R.
\tag{10}
\]

The tests in (7) of the statement are exactly the terminal tests from this
stripping process, so they are also a directly verifiable certificate.

For every exact common order \(R\), equation (3) gives

\[
R\mid d_i\mid p_i-1
\quad(1\le i\le s).
\tag{11}
\]

The lcm \(C\) of several such orders also divides every \(p_i-1\). If \(N\)
were composite, some rational prime divisor would satisfy \(p_i\le\sqrt N\).
But \(C\mid p_i-1\) implies \(p_i>C\), contradicting \(C>\sqrt N\). This
proves the prime terminal.

## 3. Proof of the exact probability law

CRT makes the local components of a uniform unit independent and uniform in
the groups \(H_i\).

Modulo \(p_i\), exactly \(d_i\) of the \(p_i-1\) units are roots of
\(X^m-1\). Therefore the probability that the initial gcd contains no copy
of \(p_i\) is

\[
\beta_i=1-\frac{d_i}{p_i-1}.
\tag{12}
\]

Exactly \(d_i\) of the \(h_i\) elements of \(H_i\) are full roots modulo
\(R_i\), giving probability

\[
\gamma_i=\frac{d_i}{h_i}.
\tag{13}
\]

Independence proves (13)--(14) of the statement. Every event outside
\(G_0=1\) and \(G_0=N\) gives a nontrivial proper gcd, including a partial
prime-power lift.

Condition on \(G_0=N\). Each local component is now independent and uniform
in the cyclic root group \(K_i\). A cyclic group of order \(d_i\) has exactly
\(\varphi(r)\) elements of order \(r\) for each \(r\mid d_i\). Hence the
number of CRT tuples whose local orders all equal \(r\) is

\[
\varphi(r)^s,
\tag{14}
\]

and such a tuple exists exactly when \(r\mid D=\gcd_i d_i\). Dividing by
\(\prod_i d_i\) proves the conditional formula (15).

Without conditioning, the number of unit CRT tuples with common order \(r\)
is still \(\varphi(r)^s\), while the whole unit group has size
\(\prod_i h_i\). This proves (16). A common order is no progress exactly
when it divides the current lcm state \(C\). Adding complete nonreturn gives
(17).

## 4. Semiprime specialization

Let \(N=pq\). Since \(p\equiv1\pmod {p-1}\),

\[
pq-1\equiv q-1\pmod {p-1},
\tag{15}
\]

and symmetrically modulo \(q-1\). Therefore both root-group orders equal

\[
d=\gcd(p-1,q-1).
\tag{16}
\]

At state \(C=1\), no progress consists of either nonreturn at both primes,
with probability

\[
\left(1-\frac d{p-1}\right)
\left(1-\frac d{q-1}\right),
\tag{17}
\]

or the unique pair of local identity elements, with probability

\[
\frac1{(p-1)(q-1)}.
\tag{18}
\]

Subtracting (17)--(18) from one and expanding proves (20). Formulae
(21)--(22) follow by splitting the common-order count into \(r=1\),
\(r>1\), and unequal local orders.

## 5. Bounded-gap obstruction

Every common divisor of \(p-1\) and \(q-1\) divides their difference, so

\[
d\mid q-p.
\tag{19}
\]

If \(q-p\le H\), every common order divides \(d\le H\), and common-order
accumulation can never exceed \(H\). A unit base cannot factor or enlarge the
state unless at least one local residue is an \(m\)-th root. A union bound
therefore gives

\[
\Pr(\text{success})
\le\frac d{p-1}+\frac d{q-1}
=O_H(p^{-1}).
\tag{20}
\]

For a uniform residue rather than a conditioned unit, a nonunit proper gcd
has probability at most \(p^{-1}+q^{-1}\). Adding this to (20) preserves the
same \(O_H(p^{-1})\) bound.

When \(q=p+O_H(1)\), one has \(N=p^2(1+O_H(p^{-1}))\), hence

\[
p=2^{n/2+O_H(1)}.
\tag{21}
\]

A union bound over \(K(n)=2^{(\log n)^{O(1)}}\) samples gives

\[
K(n)O_H(p^{-1})=2^{-\Omega(n)}.
\tag{22}
\]

This proves the obstruction for every infinite bounded-gap prime-pair
family. The assertion that such a family exists uses the standard
bounded-prime-gap theorem. No distributional claim about primes and no
unproved prime-tuple conjecture is used.

## 6. Contrasting input classes

If \(N\) is prime, its unit group is cyclic of order \(m\). Let
\(q^E\parallel m\). A uniform element fails to have \(q^E\) in its order
exactly when its exponent coordinate is divisible by \(q\), an event of
probability \(1/q\). Across \(k\) independent bases this has probability
\(q^{-k}\). A union bound over the distinct primes of \(m\) proves (27).

If \(N\) is squarefree Carmichael, Korselt's criterion gives
\(p_i-1\mid m\), so \(K_i=H_i\) for all \(i\). Every unit fully returns.
For the first base, no factor and no growth means that every local order is
one, which occurs only for the unique CRT identity tuple. Dividing by
\(|(\mathbb Z/N\mathbb Z)^\times|=\varphi(N)\) proves (28).

Finally, if \(N=p^e\), then \(p-1\mid p^e-1\), so \(d_1=p-1\). Equations
(12)--(13) give \(\beta_1=0\) and \(\gamma_1=p^{1-e}\). With only one hidden
prime-power component, every remaining case is a proper partial-power gcd.
This proves (29).

## 7. Recursive accounting

The integer \(A=(N-1)/2\) has at most \(n-1\) bits. Once its complete
factorization is available, adjoining one factor 2 gives the complete
factorization of \(m\). The number of prime-copy stripping tests is at most
\(\log_2m<n\) per base. Modular exponentiation and gcd computation have
polynomial bit complexity, so a numerical-QP sample bank has numerical-QP
nonrecursive cost.

With one recursive child and no additional recursive calls, summing

\[
\mathcal T(n)\le\mathcal T(n-1)+Q(n)
\tag{23}
\]

gives \(\mathcal T(n)\le nQ(n)\), which is numerical QP. If returned factors
are also completed recursively, the two factor children in (32) of the
statement are additional calls and this summation no longer applies. This is
an interface limitation, not a fixed-contraction objection.
