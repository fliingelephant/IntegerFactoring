# Proof of F173

Use the integer cap and Harvey--Hittmeir target

\[
T(n)=\lfloor Q(n)\rfloor,
\qquad D=T(n),
\]

as in the statement.

## 1. Four exponential shifted divisors

Choose an arbitrarily large odd prime \(r>3\). By Bertrand's theorem,
choose a prime

\[
r<u<2r.
\tag{1}
\]

Use CRT to prescribe a reduced residue class modulo \(3ru\) by

\[
p\equiv1\pmod3,
\qquad
p\equiv1\pmod r,
\qquad
p\equiv-1\pmod u.
\tag{2}
\]

Every prescribed residue is nonzero modulo its prime modulus. Linnik's
theorem supplies a prime in this class with

\[
p\le C_0(3ru)^{L_0}.
\tag{3}
\]

This prime is larger than \(r\). It is also larger than \(u\): the least
positive integer congruent to \(-1\pmod u\) is \(u-1\), which is an even
integer larger than two and is not prime. Thus

\[
r\mid p-1,
\qquad
u\mid p+1.
\tag{4}
\]

Write

\[
p^2-1=2^a3^bM,
\qquad
\gcd(M,6)=1,
\]

and put

\[
H=8p3^bM.
\tag{5}
\]

Choose primes

\[
H<s<2H,
\qquad
2H<t<4H
\tag{6}
\]

by two applications of Bertrand's theorem. They are distinct and coprime to
\(H\).

Let \(a_p\pmod H\) be the F172 reduced class

\[
\begin{aligned}
a_p&\equiv3\pmod8,\\
a_p&\equiv1\pmod p,\\
a_p&\equiv4\pmod{3^b},\\
a_p&\equiv2\pmod M.
\end{aligned}
\tag{7}
\]

When \(M=1\), omit the final congruence. Extend it by

\[
q\equiv1\pmod s,
\qquad
q\equiv-1\pmod t.
\tag{8}
\]

The moduli \(H,s,t\) are pairwise coprime and every prescribed residue is a
unit. CRT gives a reduced class modulo \(Hst\), and Linnik gives a prime

\[
q\le C_1(Hst)^{L_0}.
\tag{9}
\]

The congruence \(q\equiv1\pmod p\) gives \(q=1+vp\). The cases \(v=0,1\)
are not prime, so \(q>2p\). Equations (8) also give

\[
s\mid q-1,
\qquad
t\mid q+1.
\tag{10}
\]

The proof of F172 uses only (7) to establish

\[
\gcd(p-1,q-1)=6,
\tag{11}
\]

\[
\gcd(p-1,q+1)\in\{2,4\},
\qquad
\gcd(p+1,q-1)=2,
\tag{12}
\]

and

\[
\gcd(p+1,q+1)\in\{2,4\}.
\tag{13}
\]

The extra congruences (8) do not change the residue modulo \(H\), so the
same proof applies verbatim.

## 2. Link to the input length

Equation (3) and \(u<2r\) give \(p=r^{O(1)}\). Also

\[
H<8p^3,
\qquad
s,t=p^{O(1)},
\qquad
q=p^{O(1)}
\tag{14}
\]

by (5), (6), and (9). The reverse inequalities

\[
r<p<q
\]

show that, for \(N=pq\),

\[
n=\lceil\log_2(N+1)\rceil=\Theta(\log r).
\tag{15}
\]

After reducing one absolute constant \(c>0\) and deleting a finite prefix,

\[
r,u,s,t\ge2^{cn}.
\tag{16}

\]

Every fixed QP function has logarithm \(o(n)\). Therefore all four primes
are greater than \(4Q(n)\) for all sufficiently large members. The same
size estimate makes both hidden factors trial-hard.

The construction is infinite because \(r\) is unbounded and every resulting
\(p\) is larger than \(r\).

## 3. Ordinary common order and primitive witness

Both \(p-1\) and \(q-1\) are divisible by six. Their cyclic unit groups
therefore contain elements of exact order six. CRT combines local choices
to one global element \(g\) of exact order six in both fields.

Choose local primitive roots and combine them to one unit \(a\). Then

\[
\operatorname{ord}_p(a)=p-1,
\qquad
\operatorname{ord}_q(a)=q-1.
\tag{17}
\]

Any ordinary element having one exact order \(A\) in both fields satisfies

\[
A\mid\gcd(p-1,q-1)=6.
\tag{18}
\]

Thus \((g,6)\) is a maximal common-order state.

The local order \(p-1\) contains \(r>Q(n)\), and \(q-1\) contains
\(s>Q(n)\). Neither order divides \(\Lambda_T\), so

\[
\gcd(a^{\Lambda_T}-1,N)=1.
\tag{19}
\]

Because the order-six subgroup is the unique such subgroup in each cyclic
field group, the local order of the coset \(a\langle g\rangle\) is

\[
A_p=(p-1)/6,
\qquad
A_q=(q-1)/6.
\tag{20}
\]

The first number contains \(r\), and the second contains \(s\). Both exceed
\(T(n)\). Therefore \(a^{6e}\ne1\) in both fields for
\(1\le e\le T(n)\), which proves the relative screens. It also proves that
the first \(T(n)+1\) powers of the fingerprint \(a^6\) are pairwise
distinct in both fields. Every fingerprint difference gcd is one, and P154
reaches only its capacity branch.

For exponents \(|i|,|j|\le T(n)\), every equality or inverse equality among
\(a^i,a^j\) reduces to an exponent difference of absolute value at most
\(2T(n)\). A signed equality would require such a difference to be congruent
to half a local primitive order. Both local half-orders exceed \(2T(n)\).
The same bound applies to signed pair products. Thus all nonliteral short
power comparisons are null in both fields.

## 4. Ordinary signed public-exponent screens

Let \(1\le j\le T(n)\). Modulo \(p-1\),

\[
j(N-1)\equiv j(q-1),
\qquad
j(N+1)\equiv j(q+1).
\tag{21}
\]

The prime \(r\) divides \(p-1\). Equations (11)--(12) show that it divides
neither \(q-1\) nor \(q+1\). Since \(j<r\), the prime \(r\) divides neither
exponent in (21), nor twice either exponent. Hence neither exponent is zero
or \((p-1)/2\) modulo \(p-1\).

Modulo \(q-1\), the same argument uses \(s\mid q-1\), the shifted gcds
(11)--(12), and \(j<s\). Therefore

\[
a^{j(N-1)}\ne\pm1,
\qquad
a^{j(N+1)}\ne\pm1
\]

in both fields. This proves every gcd in (12) of the statement is one.

The local orders after the \((N-1)\)-power are exact because

\[
\gcd(p-1,N-1)=\gcd(p-1,q-1)=6
\]

and likewise at \(q\). Hence they are the two numbers in (20). Equation
(11) also gives

\[
\gcd(A_p,A_q)=1.
\tag{22}

\]

Uniform powers of an element with coprime local orders are uniform on the
product of its two local cyclic groups. Exactly one coordinate is the
identity with density

\[
\frac1{A_p}+\frac1{A_q}-\frac2{A_pA_q}
\le\frac1r+\frac1s
=2^{-\Omega(n)}.
\tag{23}

\]

## 5. Torus witnesses

For each sign \(\epsilon\), choose nonzero residues of quadratic character
\(\epsilon\) modulo \(p\) and \(-\epsilon\) modulo \(q\), and combine them
by CRT. This gives a unit discriminant \(D_\epsilon\) of Jacobi symbol
minus one.

The corresponding local norm-one groups are cyclic of orders

\[
R_{p,\epsilon}=p-\epsilon,
\qquad
R_{q,\epsilon}=q+\epsilon.
\tag{24}

\]

Choose primitive points in both local groups and combine their coordinate
pairs by CRT. This gives \(U_\epsilon\) with the exact local orders (24).

Their common divisors are

\[
b_+=\gcd(p-1,q+1)\in\{2,4\},
\qquad
b_-=\gcd(p+1,q-1)=2.
\tag{25}

\]

Local cyclicity supplies a global point of exact common order
\(b_\epsilon\), so granting this state is valid and maximal.

For \(\epsilon=+1\), the two primitive orders contain \(r\) and \(t\).
For \(\epsilon=-1\), they contain \(u\) and \(s\). These large primes are
greater than \(T(n)\). The absolute screen, relative scan, fingerprint
table, short signed-power bank, and capacity conclusions now follow exactly
as in Section 3, with \(6\) replaced by \(b_\epsilon\).

For completeness, all signed public-exponent screens also remain null.
The four local reductions of \(N\pm1\) use precisely the four shifted pairs:

\[
\begin{array}{c|cc}
&N-1&N+1\\ \hline
\epsilon=+1,\ p\text{-side}&q-1&q+1\\
\epsilon=+1,\ q\text{-side}&-(p+1)&-(p-1)\\
\epsilon=-1,\ p\text{-side}&-(q+1)&-(q-1)\\
\epsilon=-1,\ q\text{-side}&p-1&p+1.
\end{array}
\tag{26}

\]

On each row, the designated large prime from \(r,u,s,t\) divides the local
torus order and, by (11)--(13), does not divide the displayed cross-shift.
It also does not divide \(2j\) for \(j\le T(n)\). Thus no exponent in (26),
after multiplication by \(j\), is zero or half the local order. Both signs
are null in both components.

Here and throughout this torus section, equality of points is tested with
the F170 joint-coordinate gcd. If \(X=x_0+x_1w\) and
\(Y=y_0+y_1w\), the test is

\[
\gcd(N,x_0-y_0,x_1-y_1).
\]

The identity and signed-identity tests use the analogous joint gcd against
\(\pm1\). Distinct local points make this joint gcd one. The proof does not
claim that either one-coordinate gcd is one separately.

Raising \(U_+\) to \(N+1\) gives coprime local orders

\[
\frac{p-1}{b_+},
\qquad
\frac{q+1}{b_+},
\tag{27}
\]

and raising \(U_-\) to \(N+1\) gives

\[
\frac{p+1}{2},
\qquad
\frac{q-1}{2}.
\tag{28}
\]

The first pair retains \(r,t\); the second retains \(u,s\). The same
calculation as (23) gives exponential small direct identity-axis density.

## 6. Exact order versus lower bounds

Equations (18) and (25) prove

\[
\operatorname{lcm}(A_{\rm ordinary},B_+,B_-)\mid
\operatorname{lcm}(6,4,2)=12.
\tag{29}

\]

Since \(\sqrt N/Q(n)=2^{\Theta(n)}\), this cannot reach the F170 CRT
threshold.

In contrast, the exact global order of \(a\) is

\[
m=\frac{(p-1)(q-1)}6.
\tag{30}

\]

The prime \(r\) divides \(p-1\) and does not divide \(q-1\). Therefore
\(q-1\mid m/r\), while \(p-1\nmid m/r\). It follows that

\[
\gcd(a^{m/r}-1,N)=q.
\tag{31}

\]

If the complete factorization of \(m\) is supplied, this is one of the
standard prime-divisor order screens. The same proof uses \(r\) or \(u\) on
the \(p\)-side of either torus orientation. Hence a factored exact global
order exposes the mismatch; a lower bound and a capacity certificate do not.

This proves the stated interface separation.
