# F214 V2 proof

## 1. Balanced interval geometry

The inequalities \(p<q<2p\) give

\[
p^2<N<2p^2,
\]

and hence

\[
\sqrt{N/2}<p<\sqrt N.
\tag{22}
\]

Similarly, \(q>p\) and \(q<2p\) give

\[
\sqrt N<q<\sqrt{2N}.
\tag{23}
\]

Both factors are odd, so \((p,q)\in P\times Q\). Also

\[
\gcd(N,K)=\gcd(N,(N-1)/2)=1,
\tag{24}
\]

which implies \(p,q\in U(K)\).

## 2. The full-\(K\) congruence is equality

Let integers \(X,Y\) lie in the continuous balanced box and satisfy
\(XY\equiv N\pmod K\). Put

\[
D=XY-N.
\]

The box gives the strict bounds

\[
\frac{N}{\sqrt2}<XY<\sqrt2N,
\]

so

\[
-\left(1-\frac1{\sqrt2}\right)N
<D<(\sqrt2-1)N.
\tag{25}
\]

A balanced product of distinct odd primes has \(N\geq15\). For \(N\geq7\),

\[
(\sqrt2-1)N<K,
\]

because

\[
K-(\sqrt2-1)N
=\left(\frac32-\sqrt2\right)N-\frac12>0.
\tag{26}
\]

For \(N\geq3\),

\[
\left(1-\frac1{\sqrt2}\right)N<K,
\]

because

\[
K-\left(1-\frac1{\sqrt2}\right)N
=\left(\frac1{\sqrt2}-\frac12\right)N-\frac12>0.
\tag{27}
\]

Thus \(-K<D<K\). Since \(K\mid D\), one has \(D=0\), or

\[
XY=N.
\tag{28}
\]

The positive divisors of the semiprime \(N=pq\) are \(1,p,q,N\). The
conditions \(X<\sqrt N<Y\) force \((X,Y)=(p,q)\). This proves (2).
Equation (24) also shows directly that every congruent \(X\) is a unit
modulo \(K\): a common divisor of \(X,K\) would divide \(XY\) and hence
\(N\), contradicting (24). Therefore (2) and the inverse formulation (3)
are equivalent.

Conversely, knowing \(p,q\) supplies the box point, while any box point is
\((p,q)\). This proves the claimed promise-problem equivalence. Notice that
condition (1) was not used.

## 3. The odd-representative singleton threshold

Suppose \(X_1,X_2\in P_m(a)\). Their difference is divisible by \(m\), and
it is even because both integers are odd. Therefore

\[
s_m=\operatorname{lcm}(2,m)\mid X_1-X_2.
\tag{29}
\]

If \(s_m>\max P-\min P\), equation (29) forces \(X_1=X_2\). The identical
argument applies to \(Q_m(a)\). Under (4), write the two nonempty singleton
sets as \(\{X\}\) and \(\{Y\}\). The endpoint predicate (1) becomes

\[
XY\leq N\leq XY,
\]

and hence \(XY=N\). The interval ordering then returns the nontrivial
factor pair. This proves the singleton generalization without asserting a
way to locate the branch.

## 4. Local child sizes, conditional accounting, and the residue terminal

Since \(N<2^n\),

\[
K=(N-1)/2<2^{n-1}.
\tag{30}
\]

Thus \(K\) is the single declared child at the current balanced node that
can have \(n-1\) bits. This is a size statement. It does not authorize a
recursive call to a balanced-semiprime promise algorithm, because \(K\) can
be an arbitrary composite. For example,

\[
N=247=13\cdot19,
\qquad K=123=3\cdot41,
\]

and the child is not balanced.

The floor definition of \(B\) gives

\[
0<E=N-B^2<(B+1)^2-B^2=2B+1<2\sqrt N+1,
\tag{31}
\]

so \(E\) has at most \(n/2+O(1)\) bits. The same bound applies to any declared
auxiliary child whose magnitude is bounded by a fixed multiple of \(\sqrt N\).

Now impose the separate theorem premise: a correct recursive factoring
dispatch is defined on every positive integer input. At every node of bit
length at most \(r\), its immediate recursive calls consist of at most one
call on at most \(r-1\) bits and at most \(Q(r)\) calls on at most
\(r/2+C\) bits. It performs at most \(Q(r)\) other bit operations. Define
\(T(r)\) as the maximum cost on inputs of at most \(r\) bits. Taking the
maximum gives (6) directly. P183 proves that this one-decrement-spine
recurrence is numerical QP. On a balanced node only, a numerical-QP
full-\(K\) selector, invoked after the all-input child call has supplied the
complete factorization of \(K\), fits inside the local \(Q(r)\) term.
Correctness and recursive closure come from the separate all-input premise,
not from the selector's balanced promise.

For the independent terminal, let \(m\) be a unit modulo \(N\), let \(s\)
be one listed residue, and suppose \(p\equiv s\pmod m\). Theorem 3.1 of
Gao--Feng--Hu--Pan, with its parameter \(r=1\), finds such a prime divisor
in

\[
O\!\left(
\left\lceil\frac{N^{1/4}}m\right\rceil
\log^{7+3\epsilon}N
\right)
\tag{32}
\]

deterministic bit operations for fixed \(\epsilon>0\). Under (7), the
ceiling factor is numerical QP in \(n\). A numerical-QP number of calls is
still numerical QP, and every returned candidate is verified by exact
division. This proves only the listed-residue consequence. Endpoint
liveness alone does not certify that a residue is \(p\bmod m\).

## 5. Literal scan sizes and the totient lower bound

The length of the first real interval is

\[
\left(1-\frac1{\sqrt2}\right)\sqrt N,
\]

and the length of the second is

\[
(\sqrt2-1)\sqrt N.
\]

The number of odd integers in any real interval of length \(H\) is
\(H/2+O(1)\). This gives (8).

For completeness, write a positive integer \(r\) as a product of prime
powers. For an odd prime power \(\ell^a\),

\[
\frac{\varphi(\ell^a)^2}{\ell^a}
=\ell^{a-2}(\ell-1)^2\geq1.
\tag{33}
\]

For \(2^a\), the same ratio is \(1/2\) when \(a=1\), and
\(2^{a-2}\geq1\) when \(a\geq2\). Multiplicativity therefore gives

\[
\varphi(r)^2\geq r/2
\tag{34}
\]

for every \(r\). Taking \(r=K=(N-1)/2\) proves (9). Equations (8) and (9)
are counts of the explicitly enumerated objects.

## 6. Explicit paired-CRT lists

CRT gives the exact product decomposition

\[
U(K)\cong\prod_{i=1}^r U(k_i).
\tag{35}
\]

If the local coordinates are partitioned into two blocks and every partial
unit assignment is materialized, the two list sizes are

\[
A=\prod_{i\in I}\varphi(k_i),
\qquad
B=\prod_{i\notin I}\varphi(k_i).
\]

Thus \(AB=\varphi(K)\), and

\[
\max(A,B)\geq\sqrt{AB}=\sqrt{\varphi(K)}.
\]

Equation (34) yields (10). This proof makes no assertion about a data
structure that does not materialize all partial assignments.

## 7. A rigorous fiber bound for \(u+u^{-1}\)

Fix \(s\bmod K\). A fiber element is a root of

\[
z^2-sz+1\equiv0\pmod K.
\tag{36}
\]

We bound the number of roots prime power by prime power.

### 7.1 Odd prime powers

Let \(\ell\) be odd. Since \(2\) is invertible modulo \(\ell^a\), the
change of variable \(t=2z-s\) is a bijection, and (36) becomes

\[
t^2\equiv s^2-4\pmod{\ell^a}.
\tag{37}
\]

More generally, consider \(t^2\equiv D\pmod{\ell^a}\). If
\(D\equiv0\pmod{\ell^a}\), then \(t\) is divisible by
\(\ell^{\lceil a/2\rceil}\), giving exactly
\(\ell^{\lfloor a/2\rfloor}\) possibilities. Otherwise, a solution forces

\[
v_\ell(D)=2h<a.
\]

Writing \(t=\ell^h w\), the unit congruence after division has at most two
roots modulo \(\ell^{a-2h}\), and each has \(\ell^h\) lifts relevant to
\(t\bmod\ell^a\). Hence there are at most

\[
2\ell^h\leq2\ell^{\lfloor a/2\rfloor}
\leq2\sqrt{\ell^a}
\tag{38}
\]

roots. An odd valuation of \(D\) gives no root. Therefore every local fiber
over an odd prime power has size at most \(2\sqrt{\ell^a}\).

### 7.2 The power of two

Every unit modulo \(2^a\) is odd. Thus any nonempty image residue \(s\) is
even. Choose its even representative and write \(s=2h\). Translation turns
(36) into

\[
(z-h)^2\equiv h^2-1\pmod{2^a}.
\tag{39}
\]

For a general square congruence \(t^2\equiv D\pmod{2^a}\), the zero case
has \(2^{\lfloor a/2\rfloor}\) roots. In the nonzero case, existence forces
\(v_2(D)=2h_0<a\). After writing \(t=2^{h_0}w\), the remaining odd unit
square congruence modulo \(2^{a-2h_0}\) has at most four roots. Each has
\(2^{h_0}\) relevant lifts. The assertion “at most four” follows directly
from the kernel of squaring on \(U(2^b)\): it has one element for \(b=1\),
two for \(b=2\), and four for \(b\geq3\). Hence the number of roots in (39)
is at most

\[
4\,2^{h_0}\leq4\sqrt{2^a}.
\tag{40}
\]

### 7.3 CRT multiplication and the image size

Let

\[
K=2^{a_0}\prod_{i=1}^r\ell_i^{a_i}
\]

with the \(\ell_i\) distinct and odd; omit the first factor when \(K\) is
odd. CRT makes a global fiber the Cartesian product of its local fibers.
Equations (38) and (40) give

\[
|\psi_K^{-1}(s)|
\leq4\,2^r\sqrt K
=4\,2^{\omega(K_{\rm odd})}\sqrt K,
\tag{41}
\]

where the constant \(4\) is harmlessly retained even when \(K\) is odd.
This proves (11). Since all \(\varphi(K)\) units are partitioned into
fibers, division by the largest possible fiber proves the explicit finite
bound (12).

We record why the asymptotic shorthand in (13) is uniform. The
Rosser--Schoenfeld totient estimate implies, for all sufficiently large
integers \(r\),

\[
\varphi(r)\gg\frac{r}{\log\log r},
\tag{42}
\]

and therefore \(\varphi(r)=r^{1-o(1)}\). If \(j=\omega(r)\), the product of
the \(j\) smallest possible distinct primes is at least

\[
2\cdot3\cdots(j+1)=(j+1)!.
\]

Thus \(r\geq(j+1)!\), and the elementary lower bound for
\(\log((j+1)!)\) gives

\[
j=O\!\left(\frac{\log r}{\log\log r}\right).
\tag{43}
\]

Consequently

\[
2^{\omega(r)}
=\exp\!\left(O\!\left(\frac{\log r}{\log\log r}\right)\right)
=r^{o(1)}.
\tag{44}
\]

Substitution of (42) and (44) into (12) proves (14). No claim about the
typical factorization of \(K\) was used.

Finally, CRT also gives

\[
\psi_K(U(K))
\cong
\prod_{\ell^a\parallel K}\psi_{\ell^a}(U(\ell^a)).
\tag{45}
\]

If these local sum choices are split into two blocks and every half choice
is materialized, the product of the two list sizes is exactly the left side
of (14). One list therefore has at least its square root,
\(K^{1/4-o(1)}\). This proves (15) for the explicit CRT-MCSS half-list
model.

## 8. The determinant-one and continued-fraction scope

Section 2 proves \(XY=N\), and \(N=2K+1\). Therefore

\[
XY-2K=1,
\]

which is the determinant identity in (16). Conversely, that identity gives
\(XY=2K+1=N\), so every positive solution is obtained by choosing a
positive divisor \(X\mid N\) and setting \(Y=N/X\). The box selects
\(X=p\), but making that selection is the original balanced factor task.

The usual continued-fraction criterion starts from a public rational number
and proves that a sufficiently close hidden fraction must be one of its
convergents. Identity (16) instead has two hidden diagonal entries and the
fixed public off-diagonal product \(2K\). It yields no additional public
approximation datum. This establishes only the exact equivalence of this
direct determinant-completion formulation. It cannot exclude a future
algorithm that uses continued fractions together with new information.

## 9. The direct bivariate Coppersmith scale

For integers in the balanced box, define

\[
a=B-X,
\qquad c=Y-B.
\]

Then

\[
(B-a)(B+c)=N=B^2+E
\]

is equivalent to

\[
f(a,c)=Bc-Ba-ac-E=0.
\tag{46}
\]

The affine change \(U=B-a,V=B+c\) turns this into \(UV-N\), which is
irreducible over \(\mathbb Q\). Thus \(f\) meets the irreducibility premise
of the cited bivariate integer-root theorem.

The full ranges have upper bounds

\[
A=B-\sqrt{N/2}+O(1)=\Theta(\sqrt N),
\]

\[
C=\sqrt{2N}-B+O(1)=\Theta(\sqrt N).
\tag{47}
\]

After scaling, the four coefficient magnitudes are

\[
BC,\quad BA,\quad AC,\quad E.
\]

The first three are \(\Theta(N)\), while (31) gives
\(E=O(\sqrt N)\). Hence

\[
W=\|f(Ax,Cy)\|_\infty=\Theta(N),
\qquad AC=\Theta(N)=\Theta(W).
\tag{48}
\]

Coppersmith's proved bivariate integer theorem, in the corrected form of
Coron--Kirichenko--Tibouchi, has a sufficient range at separate degree
\(\delta=1\) of \(AC<W^{2/3}\), with its explicit constant or epsilon
slack. Equation (48) lies outside that range by the ratio
\(\Theta(N^{1/3})\). Failure of a sufficient inequality proves only that
this theorem cannot be invoked directly. It is not an impossibility result
for lattices.

## 10. Dense support of the odd-interval Fourier transform

Assume \(K\) odd and put \(e_K(t)=\exp(2\pi it/K)\). For

\[
\mathcal A=\{a+2j:0\leq j<L\}\subset\mathbb Z/K\mathbb Z,
\]

the unnormalized Fourier coefficient at \(r\bmod K\) is

\[
\widehat{1_{\mathcal A}}(r)
=e_K(ra)\sum_{j=0}^{L-1}e_K(2rj).
\tag{49}
\]

At \(r=0\), this equals \(L\). For \(r\neq0\), oddness of \(K\) makes
\(e_K(2r)\neq1\), so the geometric sum vanishes exactly when

\[
e_K(2rL)=1
\iff K\mid rL.
\tag{50}
\]

There are \(\gcd(K,L)\) solutions to \(rL\equiv0\pmod K\), one of which
is \(r=0\). Thus exactly \(\gcd(K,L)-1\) Fourier coefficients vanish, and
the support size is

\[
K-\gcd(K,L)+1\geq K-L+1.
\tag{51}
\]

For \(N\geq15\), both balanced intervals lie inside a complete residue
system modulo \(K\); their odd points form progressions of this type with
\(L=\Theta(\sqrt N)<K\). An exact inverse-hyperbola count can be written as
a sum of additive Fourier coefficients against Kloosterman sums. Any
implementation that explicitly materializes and handles each nonzero mode
therefore sees at least \(K-o(K)\) modes. Equation (51) says nothing about
an evaluator that sums those modes implicitly.

## 11. What the modular-hyperbola literature does and does not supply

The cited Cilleruelo--Garaev result proves concentration bounds for points
of modular hyperbolas in short boxes over prime moduli. Such a distribution
bound is not an algorithm for locating the promised unique point for the
composite, fully factored modulus \(K\). Hittmeir gives an explicit
hyperbolic-sieve reduction to MCSS and rigorous power-time improvements in
the divisor-difference setting, while the faster two-list time-space route
is stated with heuristic asymptotics. Neither source supplies an exact
numerical-QP subbox locator at the F209 scale.

Conversely, an exact numerical-QP oracle that counted points in arbitrary
subrectangles of \(P\times Q\) would locate the unique full-\(K\) point by
binary subdivision in \(O(n)\) oracle calls. The total full-box count alone
is already known to be one from Section 2 and does not reveal its location.
This isolates the remaining compressed counting or localization primitive
without assuming it exists.
