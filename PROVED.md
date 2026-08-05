# Promoted Results

Only verifier-backed results may be promoted here. Each result must include its exact status label and its proof or certificate.

## P01 — no rank reduction by universally sound linear square-class sketches

**Status:** promoted.

**Verification record:** initial proof, focused hostile audit, and proof-blind end-to-end reconstruction all completed. No cross-family audit has run.

**Statement.** Let \(a_1,\ldots,a_m\) be positive integers with classes \(v_i=[a_i]\) in the \(\mathbb F_2\)-vector space \(\mathbb Q^\times/(\mathbb Q^\times)^2\). Let a homogeneous linear sketch choose \(e_i\in\mathbb F_2^d\). Suppose it is universally sound in the exact sense that

\[
\sum_i c_i e_i=0
\quad\Longrightarrow\quad
\prod_i a_i^{c_i}\text{ is an integer square}
\]

for every \(c\in\mathbb F_2^m\). Then

\[
\operatorname{rank}(e_1,\ldots,e_m)
\ge
\operatorname{rank}(v_1,\ldots,v_m).
\]

In particular, if the \(a_i\) are distinct primes, then \(d\ge m\) and the sketch has no nonzero dependence.

**Proof.** Define \(E(c)=\sum_i c_i e_i\) and \(V(c)=\sum_i c_i v_i\). Positivity and unique factorization imply that \(V(c)=0\) exactly when \(\prod_i a_i^{c_i}\) is an integer square. Universal soundness is therefore \(\ker E\subseteq\ker V\). The map \(V\) factors through \(E\): define \(L(E(c))=V(c)\), which is well-defined by the kernel inclusion. Hence \(V=L\circ E\) and \(\operatorname{rank}V\le\operatorname{rank}E\). For distinct primes \(a_i=p_i\), taking the \(p_j\)-adic valuation modulo 2 in a relation shows each coefficient \(c_j=0\); thus \(\operatorname{rank}V=m\), forcing \(\operatorname{rank}E=m\), \(d\ge m\), and \(\ker E=0\). \(\square\)

**Scope.** This does not address lossy sketches followed by exact verification, randomized rejection, nonlinear or adaptive encodings, or special generators whose true square-class span is structurally small.

## P02 — factoring from a root of a hidden random unit square

**Status:** promoted.

**Verification record:** initial proof, focused hostile audit, and proof-blind end-to-end reconstruction all completed. No cross-family audit has run.

**Statement.** Let

\[
N=\prod_{j=1}^r p_j^{\alpha_j}
\]

be odd, with distinct primes \(p_j\). Choose hidden \(X\) uniformly in \((\mathbb Z/N\mathbb Z)^\times\), set \(A=X^2\), and give only \((N,A)\) to a routine whose private randomness is independent of \(X\). Conditional on the routine returning any valid root \(Y^2=A\),

\[
\Pr\bigl(1<\gcd(X-Y,N)<N\bigr)=1-2^{1-r}.
\]

Thus the probability is exactly \(1/2\) for a product of two distinct odd prime powers, at least \(1/2\) whenever \(r\ge2\), and zero for an odd prime power.

**Proof.** A unit square modulo an odd prime power has exactly two roots, since \(u^2=1\pmod {p^\alpha}\) implies \(p^\alpha\) divides one of the coprime-up-to-2 factors \(u-1,u+1\), hence \(u=\pm1\). CRT gives exactly \(2^r\) roots of \(A\), indexed by independent signs on the prime-power components. Conditional on \(A\) and on any returned \(Y\), the hidden \(X\) remains uniform among these roots because the routine sees no information about \(X\) beyond \(A\). If \(S\) is the set of components on which \(X=Y\), then

\[
\gcd(X-Y,N)=\prod_{j\in S}p_j^{\alpha_j};
\]

on every other component \(X-Y=-2Y\) is a unit. The gcd is proper and nontrivial for all sign subsets except the empty and full subsets. Exactly \(2^r-2\) of the \(2^r\) equiprobable choices succeed. \(\square\)

**Scope.** The unit, odd-modulus, root-validity, and hidden-root independence conditions are essential. This is a reduction, not a construction of an efficient square-root routine.

## P03 — synchronized collision products on one duplication-Lattès instance

**Status:** promoted.

**Verification record:** initial certificate, focused hostile audit, and proof-blind end-to-end reconstruction all completed. No cross-family audit has run.

**Statement.** Let \(R=\mathbb Z/15\mathbb Z\),

\[
E_{\mathrm{aff}}(R)=\{(x,y)\in R^2:y^2=x^3+2x+1\},
\]

and

\[
F(X)=\frac{X^4-4X^2-8X+4}{4(X^3+2X+1)}.
\]

For any \(P=(x_0,y_0)\in E_{\mathrm{aff}}(R)\), define \(x_{i+1}=F(x_i)\) by stepwise inversion. Every denominator is a unit, \(x_{i+3}=x_i\), and \(x_0,x_1,x_2\) have pairwise unit differences. Therefore

\[
D_m=\prod_{0\le i<j<m}(x_i-x_j)
\]

is a unit for \(1\le m\le3\) and is zero in \(R\) for \(m\ge4\). Every integer lift has gcd 1 or 15 with 15, respectively, and never produces a nontrivial factor.

**Proof.** The discriminant of the curve is \(-944\equiv1\pmod {15}\). Direct enumeration gives six affine points over each of \(\mathbb F_3\) and \(\mathbb F_5\), hence both elliptic-curve groups have prime order 7. The displayed rational function is the standard duplication formula

\[
x([2]P)=\left(\frac{3x^2+2}{2y}\right)^2-2x.
\]

Every affine local point consequently has order 7. Its doubling iterates remain nonidentity and cannot have \(y=0\), so every denominator \(4y^2\) is nonzero in both fields and hence a unit in \(R\). The multiplier classes \(1,2,4\) are distinct modulo sign in \(\mathbb Z/7\mathbb Z\), whereas \(2^3=1\pmod7\). Thus the first three local \(x\)-coordinates are pairwise distinct and the fourth repeats the first in both CRT components. Pairwise differences are units through \(m=3\), while \(x_0-x_3=0\) occurs in every \(D_m\) for \(m\ge4\). \(\square\)

**Scope.** This covers exactly the 36 affine CRT curve points for this fixed curve and modulus. It does not cover arbitrary residue seeds, randomized curves, or other dynamics. Indeed, for the same rational map the non-curve seed \(x=2\) gives \(2\to9\to7\pmod {15}\) and \(D_3=70\), whose gcd with 15 is 5.

## P04 — a Las Vegas splitter implies complete factorization

**Status:** promoted.

**Verification record:** initial proof, focused hostile audit with repairs, and proof-blind end-to-end reconstruction all completed. No cross-family audit has run.

**Statement.** Let \(\ell(x)=\lceil\log_2(x+1)\rceil\). Suppose one uniform classical randomized machine `Split` has the following guarantee on every composite \(M\): each invocation uses fresh random coins, halts almost surely, returns only \(d\) with \(1<d<M\) and \(d\mid M\), and has conditional expected bit cost at most a fixed nondecreasing polynomial \(Q(\ell(M))\). Let a uniform deterministic primality test have worst-case bit cost at most a fixed nondecreasing polynomial \(A(\ell(M))\). Then complete factorization is Las Vegas and, for \(n=\ell(N)\),

\[
\mathbb E[T(N)]
\le (n-2)Q(n)+(2n-3)A(n)+Kn^3
\]

for one fixed implementation constant \(K\).

**Algorithm.** Maintain a stack of unresolved occurrences, initially \([N]\), and a list of certified-prime occurrences. Primality-test each popped value. Move primes to the list; on a composite, call `Split`, verify the strict divisor and exact division, and replace it by the divisor and quotient. Sort and group the prime occurrences, verify their product, and output primes with multiplicities.

**Correctness and call bound.** At every state boundary, all stack/list occurrences are at least 2 and their product is \(N\). With \(k\) occurrences, \(2^k\le N<2^n\), hence \(k\le n-1\). A prime move preserves \(k\), while every split increases it by one. Starting from one occurrence gives at most \(n-2\) splits. Each split creates two tree nodes, so at most \(2n-3\) occurrences are primality-tested. This live invariant does not assume termination and counts repeated factors separately. When the stack empties, all leaves are certified prime and multiply to \(N\); grouping gives the unique complete factorization.

**Expected cost and termination.** Index the at most \(n-2\) possible split calls, assigning cost zero when a call is absent. Conditional on the full history before any reached call, its input is a fixed composite of at most \(n\) bits. Fresh coins and the conditional guarantee bound its expected cost by \(Q(n)\). The tower property and linearity give total expected split cost at most \((n-2)Q(n)\); mutual independence between different calls is unnecessary. The node bound gives deterministic primality cost \((2n-3)A(n)\). A finite union of the zero-probability nontermination events proves almost-sure termination. All stored values have at most \(n\) bits, and schoolbook validation, division, storage, sorting, grouping, product verification, and serialization cost at most \(Kn^3\). \(\square\)

**Scope.** Prime inputs use no split call; prime powers and repeated factors become repeated leaves; even and arbitrary composites are covered by the all-composite `Split` premise. Verification alone does not convert a fallible candidate generator: a separate inverse-polynomial success bound or direct polynomial expected-time guarantee is required.

## P05 — unequal local polynomial-gcd degrees expose a factor

**Status:** promoted.

**Verification record:** initial proof, focused hostile audit with convention/complexity repairs, and proof-blind end-to-end reconstruction all completed. No cross-family audit has run.

**Statement.** Let \(N=pq\) for distinct primes. Let densely represented \(A,B\in(\mathbb Z/N\mathbb Z)[X]\) have degrees at most \(D\) and unit leading coefficients. If their gcd degrees over \(\mathbb F_p\) and \(\mathbb F_q\) differ, a nontrivial factor of \(N\) is recoverable deterministically in \(\operatorname{poly}(D,\log N)\) bit operations.

**Proof.** Swap \(A,B\) so their degrees are \(m\ge n\). For \(0\le j<n\), let \(s_j\) be the determinant-form principal coefficient of the \(j\)-th subresultant. Over a field, if the gcd degree is \(d\), then \(s_j=0\) for \(j<d\) and \(s_d\ne0\). This follows from the Sylvester-map kernel: a common divisor of degree \(d\) gives a nonzero syzygy below index \(d\), while coprime cofactors and the strict degree bounds make the index-\(d\) map injective. If \(d_p\ne d_q\), take \(j=\min(d_p,d_q)<n\). Reduction of the determinant shows \(s_j\) is zero in exactly one CRT component, so \(\gcd(s_j,N)\) is a prime factor. Scanning all \(j\) finds it without knowing the local degrees. Each determinant has dimension at most \(2D\); a division-free Berkowitz circuit and modular reduction give, conservatively, \(O(D^5)\) ring operations and polynomial bit complexity. \(\square\)

**Scope.** This is conditional on efficiently constructing \(A,B\) with a local gcd-degree mismatch and on \(D=\operatorname{poly}(\log N)\).

## P06 — global-\(N\) powers can erase a genuine local cycle mismatch

**Status:** promoted.

**Verification record:** exact certificates passed focused hostile audit and proof-blind reconstruction. No cross-family audit has run.

**Certificate 1.** For \(N=15\), \(f=X^2+1\) is irreducible modulo 3, split squarefree modulo 5, and has unit resultant 4 with its derivative. Since \(X^2=-1\),

\[
X^{15^i}-X\equiv-2X\ (i\text{ odd}),
\qquad
X^{15^i}-X\equiv0\ (i\text{ even})
\pmod f
\]

in both CRT components, so the naive DDF profiles always agree. At \(i=1\), the true local differences \(X^3-X\) modulo 3 and \(X^5-X\) modulo 5 CRT-combine to \(10X\), whose coefficient exposes 5.

**Certificate 2.** For \(N=10\), \(f=X^2+9X+5\) is irreducible modulo 2, split squarefree modulo 5, and has unit resultant \(-61\). Modulo 2 the class of \(X\) has order 3 and \(10^i\equiv1\pmod3\); modulo 5, \(X^2=X\). Hence \(X^{10^i}-X=0\) in both components for every \(i\ge1\). The true local first differences combine to the constant 5.

**Scope.** These certificates refute only replacing component field-size powers by \(N^i\). Constructing the displayed true local CRT combinations directly uses the unknown components and is explanatory, not an algorithm or an impossibility theorem.

## P07 — the Jacobi-minus-one quadratic promise is restricted-semiprime factoring

**Status:** promoted.

**Verification record:** probability and both reduction directions passed focused hostile audit and proof-blind reconstruction. No cross-family audit has run.

**Statement.** Restrict inputs to \(N=pq\) for distinct odd primes and a monic quadratic with unit discriminant \(\Delta\) satisfying \((\Delta/N)=-1\). Producing a nontrivial factor on every such promise input is Las Vegas randomized-polynomial-time equivalent to factoring every distinct-odd-semiprime.

**Proof.** Factoring trivially solves the promise. Conversely, sample uniform monic quadratics. In each local field the discriminant is uniform; conditional on being nonzero, its square/nonsquare bit is fair. CRT makes the two bits independent. A valid negative-Jacobi unit therefore occurs per raw sample with probability \((p-1)(q-1)/(2pq)\), so its expected waiting time is \(2pq/((p-1)(q-1))\le15/4\). If a sampled discriminant has a proper gcd with \(N\), return it immediately; otherwise invoke the promise solver once the Jacobi symbol is \(-1\). All preprocessing is deterministic polynomial bit complexity, the loop terminates almost surely, and the promise solver's uniform expected-polynomial bound is preserved. \(\square\)

**Scope.** This covers neither prime squares nor unrestricted composites. It shows that recognizing/generating opposite local cycle signs does not perform the required separation; it does not rule out richer invariants of the polynomial.

## P08 — uniform linear gcd probes have exponentially small separation probability

**Status:** promoted.

**Verification record:** exact enumeration passed focused hostile audit and proof-blind reconstruction. No cross-family audit has run.

**Statement and proof.** Suppose a squarefree quadratic \(f\) splits modulo \(p\) and is irreducible modulo \(q\). For coefficientwise uniform \(B=aX+b\), the local gcd degree modulo \(p\) equals 2, 1, or 0 on respectively \(1\), \(2(p-1)\), or \((p-1)^2\) of the \(p^2\) coefficient pairs. Modulo \(q\), it equals 2 only for the zero polynomial and 0 otherwise. CRT independence gives

\[
\Pr(d_p\ne d_q)
=\frac{2p-1}{p^2}+\frac{p-2}{pq^2}
<\frac2p+\frac1{q^2}.
\]

Conditioning \(a\) to be a unit and normalizing \(B\) to \(X+t\) makes the exact probability \(2/p\). For balanced factors this is exponential in \(\log N\), so this probe strategy cannot have polynomial expected trials. \(\square\)

## P09 — blind substitution fails for a Hasse–Witt rank separator

**Status:** promoted.

**Verification record:** exact certificate passed focused hostile audit and proof-blind reconstruction. No cross-family audit has run.

**Statement.** Let \(N=15\) and \(E:y^2=f(x)=x^3+x+1\). The true genus-1 Hasse–Witt ranks of its reductions modulo 3 and 5 are 0 and 1, but the formal surrogate obtained by replacing the local characteristic with \(N\) in the coefficient formula is zero in both components.

**Proof.** The Weierstrass discriminant is

\[
-16(4+27)=-496,
\]

a unit modulo 15, so both reductions are good. Under the standard genus-1 coefficient convention,

\[
H_r=[x^{r-1}]f(x)^{(r-1)/2}.
\]

Thus \(H_3=[x^2]f=0\), while \(H_5=[x^4]f^2=2\); their one-dimensional ranks are 0 and 1. Transpose, Frobenius twist, sign, or basis conventions preserve zero versus nonzero in dimension one. The blind surrogate is

\[
B_{15}=[x^{14}]f^7.
\]

If \(a,b,c\) count selections of \(x^3,x,1\), then \(a+b+c=7\) and \(3a+b=14\), whose unique nonnegative solution is \((4,2,1)\). Hence

\[
B_{15}=\frac{7!}{4!2!1!}=105\equiv0\pmod {15}.
\]

The true CRT lift satisfies \(h=0\pmod3\), \(h=2\pmod5\), so \(h=12\pmod {15}\) and \(\gcd(h,15)=3\). \(\square\)

**Scope.** This refutes only the syntactic substitution of \(N\) into the prime-characteristic coefficient formula. Computing local entries after first factoring is circular, but a direct uniform computation of their CRT lift would be a legitimate factoring breakthrough; no other global geometric invariant is ruled out.

## P10 — scalar carry is not a sufficient binary-factor state

**Status:** promoted.

**Verification record:** the corrected obstruction passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

**Statement.** In low-to-high schoolbook binary multiplication, quotienting partial factor assignments only by the current scalar carry does not preserve future completability. In particular, for the canonical factor-length search \(2\le a\le b\), retaining the largest low \(x\)-prefix in each carry state can delete the only factor path. Moreover, when \(a<b\), the set of all raw histories compatible through the low \(a\) columns has exactly \(2^{a-2}\) members; a restart that samples uniformly from that whole set can therefore require exponentially many trials. These statements do not apply to richer states or arbitrary representative distributions.

**Carry recurrence and bound.** Write

\[
s_k=\sum_{i+j=k}x_i y_j,
\qquad
c_{k+1}=\frac{c_k+s_k-N_k}{2},
\qquad c_0=0.
\]

Accepted transitions require a nonnegative integer carry. If \(x\) has \(a\) bits, then \(s_k\le a\), and induction gives \(0\le c_k\le a-1\): from \(c_k\le a-1\),

\[
c_{k+1}\le\left\lfloor\frac{2a-1}{2}\right\rfloor=a-1,
\]

while an integral numerator at least \(-1\) cannot produce a negative integer.

**Collision certificate.** Let \(N=55=(110111)_2\) and search lengths \((a,b)=(3,4)\). After columns 0 and 1, the histories

\[
P:(x_0,x_1)=(1,0),\ (y_0,y_1)=(1,1),
\qquad
Q:(x_0,x_1)=(1,1),\ (y_0,y_1)=(1,0)
\]

both have \(c_1=c_2=0\). History \(P\) completes to \(x=5,y=11\). In \(Q\), the leading-bit condition forces \(x_2=1\); column 2 then forces \(y_2=0,c_3=0\), and the four-bit condition forces \(y_3=1\). Column 3 would give \(c_4=(1-0)/2\), so no completion exists. Equivalently, its forced integers are \(x=7,y=9\). The largest low \(x\)-prefix rule keeps \(Q\) and discards \(P\), deleting the sole \((3,4)\), \(a\le b\) factor path.

For this first-nontrivial-column destructive pattern, an accepting path has \(x\equiv1\pmod4\), \(y\equiv3\pmod4\). If equal-length swaps are allowed, equal lengths preserve the swapped completion, so the smallest destructive case has \(a<b\): the least factors are 5 and 11, giving 55. If a separate numerical rule \(x\le y\) rejects the swapped equal-length path, 35 is already a witness. No minimality over later collisions is asserted.

**Raw-history count.** Assume \(a<b\), let \(X\) be an odd \(a\)-bit candidate and let \(Y\) denote the low \(a\) bits of the other candidate. Summing the first \(t\) column equations yields

\[
\sum_{i+j<t}x_i y_j2^{i+j}-(N\bmod2^t)=2^t c_t.
\]

Thus compatibility through the low \(a\) columns is equivalent to \(XY\equiv N\pmod {2^a}\). Every odd \(a\)-bit \(X\) is invertible modulo \(2^a\) and determines the unique residue \(Y\equiv NX^{-1}\pmod {2^a}\). There are exactly \(2^{a-2}\) such \(X\), hence exactly that many raw histories. The congruence in every lower modulus reconstructs integral nonnegative carries, proving the converse. Some histories need not extend: at \(N=55,a=3\), the two histories are \((5,3)\) and \((7,1)\) modulo 8, and only the first extends.

**Global-uniform restart.** If \(N=pq\) is semiprime with a unique \(a\)-bit divisor \(p\) and the other factor has \(b>a\) bits, exactly one raw history fully completes. A uniform draw from the entire depth-\(a\) history set therefore succeeds with probability \(2^{-(a-2)}\). Bertrand's postulate supplies primes of lengths \(a\) and \(a+1\), for which the input length is \(2a\) or \(2a+1\); this particular restart rule consequently has success \(2^{-\Theta(n)}\). This is not the probability of selecting within the true carry class. For example, at \(N=187=11\cdot17\), global uniform sampling succeeds with probability \(1/4\), whereas the true final-carry class has two histories and a uniform choice within it succeeds with probability \(1/2\). \(\square\)

**Scope.** P10 refutes scalar carry as a sufficient state, the largest-prefix rule in the stated canonical search, and the specified global-uniform restart argument. It proves no lower bound for factoring, richer carry/convolution summaries, other representative rules, or other randomized merging distributions.

## P11 — the standard AKS coefficient scan need not localize compositeness

**Status:** promoted.

**Verification record:** an exact certificate passed a focused hostile audit with an independent full rescan, then a proof-blind end-to-end reconstruction with a second fresh exhaustive run. No cross-family audit has run.

**Statement.** The standard minimal-\(r\) AKS polynomial stage does not guarantee either a local pass/fail mismatch or an individual error coefficient whose gcd with the input is nontrivial. This already fails for a product of two distinct primes that survives the preliminary gcd stage.

**Certificate and parameters.** Let

\[
N=20{,}000{,}000{,}499{,}999{,}937
=100{,}000{,}007\cdot199{,}999{,}991=pq.
\]

Deterministic trial division through the respective square-root bounds proves that \(p,q\), and \(r=2953\) are prime. Both factors exceed \(r\). Rigorous interval arithmetic gives

\[
2932<(\log_2N)^2<2933,
\qquad
2942<\sqrt{2952}\log_2N<2943.
\]

Exact order enumeration for every \(2\le s\le2953\) shows that \(r=2953\) is the first candidate with \(\operatorname{ord}_r(N)>(\log_2N)^2\). At \(r\), \(\varphi(r)=2952=2^3 3^2 41\), \(N\bmod r=1146\), and

\[
1146^{2952}=1,quad
1146^{1476}=2952,quad
1146^{984}=800,quad
1146^{72}=1277\pmod {2953},
\]

so the order is exactly 2952. The standard shift bound is therefore

\[
A=\left\lfloor\sqrt{\varphi(r)}\log_2N\right\rfloor=2942.
\]

**Algebraic reduction.** Put

\[
H_a(X)=(X+a)^N-X^N-a,
\qquad
h_{m,a}(Y)=(Y+a)^m-Y^m-a.
\]

Frobenius gives

\[
H_a(X)=h_{q,a}(X^p)\pmod p,
\qquad
H_a(X)=h_{p,a}(X^q)\pmod q.
\]

Because \(p,q\) are coprime to \(r\), substitution by \(X^p\) or \(X^q\) permutes the \(r\) coefficient positions modulo \(X^r-1\). Thus zero/nonzero status is preserved and can be checked by the two reduced-exponent families.

**Exhaustive certificate.** For every \(1\le a\le2942\), exact quotient-ring arithmetic scanned all 2953 coefficients of \(h_{q,a}\) over \(\mathbb F_p[Y]/(Y^{2953}-1)\) and all 2953 coefficients of \(h_{p,a}\) over \(\mathbb F_q[Y]/(Y^{2953}-1)\). Each side contains

\[
2942\cdot2953=8{,}687{,}726
\]

coefficient positions; both zero counts are zero. Hence every one of the \(17{,}375{,}452\) local residues is nonzero. Direct exponent-\(N\) evaluations at shifts \(a=1,2,1471,2942\) in both characteristics agree with the permuted reduced-exponent calculation. Complete row hashes, order tables, source hashes, timeouts, logs, outputs, and failed-run dispositions are preserved under `experiments/F04`, `experiments/F04_audit`, and `experiments/F04_reconstruct`.

It follows that every \(H_a\) is nonzero in both prime components, while every one of its global coefficients is nonzero modulo both \(p\) and \(q\), hence a unit modulo \(N\). Therefore every standard local identity fails and every coefficient gcd is 1. \(\square\)

**Scope.** P11 is a finite counterexample to exactly the standard minimal-\(r\), standard-shift pass/fail and individual coefficient-gcd localization claim. It does not rule out polynomially many nonstandard moduli, annihilator ranks or minors, relationships among multiple coefficients, or other group-algebra constructions. Finite computation refutes this universal auxiliary claim but does not address the top-level factoring theorem.

## P12 — natural multiplication-spectrum probes can require exponential dense support

**Status:** promoted.

**Verification record:** the corrected theorem passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

**General formulas.** Let \(N\ge2\), \(a\in(\mathbb Z/N\mathbb Z)^\times\), and let \(U_a|x\rangle=|ax\bmod N\rangle\). For each \(d\mid N\), put \(r_d=\operatorname{ord}_d(a)\), with \(r_1=1\). Then

\[
\chi_{U_a}(X)=\prod_{d\mid N}(X^{r_d}-1)^{\varphi(d)/r_d},
\qquad
\operatorname{tr}(U_a^k)=\gcd(a^k-1,N).
\]

Indeed, the residues of additive order \(d\) are in bijection with \((\mathbb Z/d\mathbb Z)^\times\), so they form \(\varphi(d)/r_d\) cycles of length \(r_d\). Every \(r_d\) divides \(r_N\), while the \(d=N\) stratum supplies every \(r_N\)-th root; hence the distinct complex spectrum is exactly all \(r_N\)-th roots. The trace counts solutions of \((a^k-1)x=0\pmod N\), of which there are exactly the displayed gcd. Binary modular exponentiation and Euclid compute it in \(\operatorname{poly}(n+\log(k+1))\) bit operations without forming \(a^k\).

For a basis point \(x\), let \(g=\gcd(x,N)\) and \(D=N/g\). Its orbit length is \(r_D\),

\[
\langle x|U_a^k|x\rangle=\mathbf1_{r_D\mid k},
\qquad
\mu_x=\frac1{r_D}\sum_{\zeta^{r_D}=1}\delta_\zeta
\]

over \(\mathbb C\). The point \(x=0\) has constant moments and gcd \(N\); a nonzero nonunit already exposes a proper gcd; a unit retains all \(r_N\) frequencies. A normalized whole-orbit indicator is fixed by \(U_a\) and has constant moments 1, whereas the squared norm of its unnormalized indicator is the orbit length. This proves no lower bound on succinct orbit-state representations.

**Synchronized family.** Fix effective Linnik constants: every reduced residue class modulo \(M\) contains a prime at most \(AM^L\). For each sufficiently large \(m\), choose an \(m\)-bit prime \(\ell\). Use Linnik first to choose \(p\equiv1\pmod\ell\), then \(q\equiv1\pmod {p\ell}\). Thus \(q>p>\ell\) and, for an absolute \(C\),

\[
p,q\le\ell^C.
\]

Choose elements of exact order \(\ell\) in \(\mathbb F_p^\times\) and \(\mathbb F_q^\times\), and CRT-combine them to \(a\pmod {N=pq}\). Since

\[
\ell^2<N\le\ell^{2C},
\]

the input length satisfies \(n=\Theta(\log\ell)=\Theta(m)\), so \(\ell=2^{\Theta(n)}\). Every nonzero residue has period exactly \(\ell\), while zero is fixed. Therefore

\[
\chi_{U_a}(X)=(X-1)(X^\ell-1)^{(N-1)/\ell},
\qquad
\operatorname{tr}(U_a^k)=
\begin{cases}
N,&\ell\mid k,\\
1,&\ell\nmid k.
\end{cases}
\]

For every nonzero point, the moment generating function is

\[
M_x(z)=\frac1{1-z^\ell}.
\]

The numerator 1 makes this fraction reduced over every coefficient field, even when the denominator is inseparable. For the exact integer trace sequence, over \(\mathbb Q\) or \(\mathbb C\),

\[
T(z)=\frac1{1-z}+\frac{N-1}{1-z^\ell}
=\frac{N+z+\cdots+z^{\ell-1}}{1-z^\ell}.
\]

At a nonidentity \(\ell\)-th root the numerator is \(N-1\), and at 1 it is \(N+\ell-1\), so there is no cancellation and the minimal denominator degree is \(\ell\). This trace conclusion is coefficient-field dependent: since \(N\) is odd, reduction modulo 2 makes every trace value 1 and reduces the denominator to \(1-z\).

Choosing least primes and exhaustively finding local witnesses makes the family uniformly enumerable in \(\ell^{O(1)}=2^{O(m)}\) time, not polynomial time in \(m\). Given \(p,q\), local order-\(\ell\) witnesses and the CRT combination are Las Vegas polynomial time, but this uses the witness factors.

**Consequence and scope.** Consecutive-moment dense Padé/Prony reconstruction and explicit enumeration of all frequencies require \(\Omega(\ell)=2^{\Theta(n)}\) representation or query/output size on these fixed pairs. P12 gives no lower bound for adaptive binary-encoded indices, sparse descriptions, finite-field trace methods, arbitrary probes, non-Prony arithmetic algorithms, or algorithms that choose or resample \(a\). The construction is not a density theorem for random bases and proves nothing about the hardness of factoring.

## P13 — natural fixed-degree automorphism counts hide the factoring oracle

**Status:** promoted.

**Verification record:** the corrected theorem passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

**Dual numbers.** Let \(A=\mathbb Z/N\mathbb Z\) and \(R=A[\varepsilon]/(\varepsilon^2)\). Every \(A\)-algebra automorphism is uniquely

\[
\varepsilon\longmapsto a+b\varepsilon,
\qquad b\in A^\times,\quad 2a=0,\quad a^2=0.
\]

The relation follows by squaring the image; invertibility is equivalent to the unit condition on \(b\). If \(N\) is even, the solutions to \(2a=0\) are \(0,N/2\), and the latter squares to zero exactly when \(4\mid N\); for odd \(N\), only zero occurs. Hence, for arbitrary \(N\),

\[
|\operatorname{Aut}_A R|=\delta(N)\varphi(N),
\qquad
\delta(N)=\begin{cases}2,&4\mid N,\\1,&4\nmid N.\end{cases}
\]

Augmentation-preserving automorphisms force \(a=0\) and have count exactly \(\varphi(N)\). Since \(\delta(N)\) is known, the unrestricted count also gives \(\varphi(N)\). For \(N=pq\),

\[
p+q=N+1-\varphi(N),
\]

so an exact integer square root of the quadratic discriminant recovers the factors in polynomial bit complexity. Conversely, factors compute the count.

**A richer rank-3 square-zero algebra.** Assume \(N=pq\) for distinct primes and put \(S=A\oplus M\), where \(M=A^2\) and \(M^2=0\). Since \(A\) is reduced, \(M\) is exactly the nilradical. Therefore

\[
\operatorname{Aut}_A(S)=GL_2(A)
\simeq GL_2(\mathbb F_p)\times GL_2(\mathbb F_q).
\]

Writing \(u=\varphi(N)=(p-1)(q-1)\), the exact count is

\[
C=N u^2\bigl(2(N+1)-u\bigr).
\]

For fixed \(N\), the full cubic in \(u\) has derivative

\[
Nu\bigl(4(N+1)-3u\bigr)>0
\qquad(0<u<N+1).
\]

Binary search over \(1\le u\le N\) therefore recovers the unique \(u\) from \(C\) using polynomially many operations on \(O(\log N)\)-bit integers; the factors then follow as above. This informative count is again factoring-equivalent despite not literally equaling \(\varphi(N)\).

**Quadratic monogenic algebras.** Let \(p,q\) be distinct odd primes and

\[
B=A[X]/(X^2-uX+v),\qquad\Delta=u^2-4v.
\]

After translating locally by \(u/2\), the algebra over \(\mathbb F_\ell\) is \(\mathbb F_\ell[Y]/(Y^2-\Delta/4)\). Its automorphism count is 2 if \(\ell\nmid\Delta\), whether split or irreducible, and \(\ell-1\) if \(\ell\mid\Delta\). CRT gives

\[
4,\quad2(p-1),\quad2(q-1),\quad\varphi(N)
\]

according as \(\gcd(\Delta,N)\) is \(1,p,q,N\). These values can collide, so the count alone need not identify the case. In mixed cases the known gcd already factors \(N\); the fully degenerate count is a \(\varphi(N)\) oracle; the fully étale count is constant.

**Fixed-rank étale algebras.** Every rank-\(d\) finite étale \(\mathbb F_p\)-algebra has a decomposition

\[
E\simeq\prod_e\mathbb F_{p^e}^{m_e},
\qquad\sum_e e m_e=d,
\]

and

\[
|\operatorname{Aut}_{\mathbb F_p}E|
=\prod_e e^{m_e}m_e!\le d!.
\]

The formula is the product of wreath-product orders: each block permits \(m_e!\) permutations and \(e\) Frobenius choices per factor. It is bounded independently of \(p\); over a squarefree semiprime base the global count is at most \((d!)^2\). A parameterized sequence of decomposition patterns could still carry information—only growing field-size magnitude is absent.

**Construction versus counting.** At \(N=15\), \(\varepsilon\mapsto-\varepsilon\) is an easy nonidentity automorphism but gives only gcds 1 and 15, whereas \(\varepsilon\mapsto4\varepsilon\) is identity modulo 3 and negation modulo 5 and exposes both factors through \(\gcd(4\mp1,15)\). Finding an arbitrary automorphism is too weak; a component-selective one already contains a factor certificate. All displayed counts have \(O(\log N)\) bits for fixed rank, so output size is not the obstruction.

**Scope.** P13 proves that in these canonical families the decomposition “easy exact counting, then interpolate” hides the target difficulty in the exact count. It does not prove that such a count lacks a factor-free polynomial-time algorithm, that every B12 family fails, or that bounded étale decomposition-pattern sequences cannot separate CRT components.

## P14 — standard AKS error nullities can agree at full rank

**Status:** promoted.

**Verification record:** an analytic counterexample passed a focused hostile audit with an independent exact run and a proof-blind end-to-end reconstruction. No cross-family audit has run.

**Statement.** Under the standard AKS convention—choose the smallest \(r\) with \(\operatorname{ord}_r(N)>(\log_2N)^2\), then test shifts through \(\lfloor\sqrt{\varphi(r)}\log_2N\rfloor\)—the local multiplication nullities of every standard error polynomial can be equal and zero in both prime components.

**Parameters.** Let

\[
N=79{,}403=271\cdot293.
\]

Trial division proves both factors prime, so \(N\) is not a perfect power. Exact rational bounds give

\[
264<(\log_2N)^2<265.
\]

For \(s\le265\), \(\operatorname{ord}_s(N)\le s-1\le264\), while \(\varphi(266),\varphi(267),\varphi(268)=108,176,132\). Modulo the prime 269,

\[
N\equiv48,qquad48^{134}=-1,qquad48^4=239,
\]

so \(\operatorname{ord}_{269}(N)=268\). Hence the first AKS modulus is \(r=269\). Both factors exceed it, so the preliminary gcd scan survives. Moreover

\[
266<\sqrt{268}\log_2N<267,
\]

and the standard shift bound is \(A=266\).

**Nullity reduction.** Put

\[
h_{m,a}(Y)=(Y+a)^m-Y^m-a.
\]

Frobenius and the substitutions \(X\mapsto X^{271}\) and \(X\mapsto X^{293}\), which are automorphisms modulo \(X^{269}-1\), reduce the two local nullities to

\[
\nu_{271}(a)=\deg\gcd(h_{293,a},Y^{269}-1),
\qquad
\nu_{293}(a)=\deg\gcd(h_{271,a},Y^{269}-1).
\]

In general, multiplication by \(h\) on \(F[Y]/(f)\) has kernel dimension \(\deg\gcd(h,f)\): writing \(h=dh_0,f=df_0\) with coprime cofactors, the kernel consists exactly of the multiples of \(f_0\) modulo \(f\).

**Cyclotomic obstruction.** Exact modular powers give

\[
\operatorname{ord}_{269}(271)=268,
\qquad
\operatorname{ord}_{269}(293)=67.
\]

Thus every nontrivial irreducible factor of \(Y^{269}-1\) has degree 268 over \(\mathbb F_{271}\) and degree 67 over \(\mathbb F_{293}\). For a nontrivial 269th root \(\zeta\), either relevant local vanishing equation implies

\[
G_a(\zeta)=0,
\qquad
G_a(Y)=(Y^2+a)(Y+a)^{22}-Y^{24}-a.
\]

In characteristic 293, division by \((\zeta+a)^{22}\) is legitimate: if \(\zeta+a=0\), the original error equals \(\zeta(1-\zeta)\ne0\). For \(a\ne0\), the \(Y^{24}\) terms in \(G_a\) cancel and its \(Y^{23}\) coefficient is \(22a\), so \(G_a\) has exact degree 23. It cannot vanish at an element of degree 67 or 268.

Only \(Y=1\) remains. Writing \(b=1+a\), the equations reduce locally to \(b^{293}=b\) and \(b^{271}=b\). Since

\[
\gcd(22,270)=\gcd(270,292)=2,
\]

the only exceptional shifts are \(a=-1,0,-2\), with nullities \(1,269,1\). Every integer \(1\le a\le267\), hence every standard shift, avoids these residues in both fields. Therefore

\[
\nu_{271}(a)=\nu_{293}(a)=0
\qquad(1\le a\le266).
\]

**Scope.** P14 refutes only universal unequal local nullity/gcd-degree separation for the standard minimal \(r\) and standard \(H_a\). Equal full ranks do not rule out zero divisors in individual intermediate minors, principal subresultant coefficients, or elimination transcripts. Nonstandard moduli, other group-algebra elements, joint invariants, shift distributions, and factoring remain open.

## P15 — individually symmetric scalar higher-residue labels have only diagonal rank

**Status:** promoted.

**Verification record:** the corrected theorem and finite certificate passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

**Character theorem.** Let \(\ell\) be prime, \(V=\mathbb F_\ell^2\), \(s(x,y)=(y,x)\), and fix a primitive \(\ell\)-th root \(\zeta\). Every group character \(\chi:V\to\mu_\ell\) has the form

\[
\chi(x,y)=\zeta^{\alpha x+\beta y}.
\]

If the **individual scalar value** is factor-swap invariant, \(\chi\circ s=\chi\), then \(\alpha=\beta\), so

\[
\chi(x,y)=\zeta^{c(x+y)}.
\]

Consequently, any family of such labels has joint rank at most one. If every label is trivial, its rank is zero and common kernel is \(V\); otherwise its rank is one and common kernel is exactly

\[
A=\{(t,-t):t\in\mathbb F_\ell\}.
\]

This follows immediately by identifying characters with \(\mathbb F_\ell\)-linear exponent maps and imposing \(L(x,y)=L(y,x)\).

**Transcript closure.** Suppose local order-\(\ell\) characters give a hidden phase vector \(u(a)=(u_p(a),u_q(a))\). Allow fixed public unit twists \(a\mapsto t_j a^{k_j}\), integer powers, multiplication and division of carrier expressions, choices depending only on public randomness and previous admissible scalar labels, adaptive stopping, and postselection solely on the resulting transcript. Every label exponent is an affine function of

\[
\Sigma(u)=u_p+u_q.
\]

Inductively, two phase vectors in the same \(A\)-coset produce the same prior transcript, force the same next choice, and produce the same next label. Thus the entire variable-length transcript and every label-only postselection event are constant on \(A\)-cosets. They cannot refine the anti-diagonal component.

The individual-character hypothesis is essential. The ordered vector \((\zeta^x,\zeta^y)\) is swap-equivariant and rank two; the multiset \(\{\zeta^x,\zeta^y\}\) is swap invariant but distinguishes \(x-y\) up to sign; and the scalar function \(\zeta^{(x-y)^2}\) is swap invariant for odd \(\ell\) but is not a character. Factor-oriented labels, additive or nonlinear probes, vector/ring-valued carriers, and adaptivity using external side information are outside the theorem.

**Cyclotomic product proposition.** Let \(\ell\) be odd, \(K=\mathbb Q(\zeta_\ell)\), \(p\equiv1\pmod\ell\) be rational prime, and \(a\in\mathbb Q^\times\) have numerator and denominator coprime to \(p\). Then

\[
\prod_{\mathfrak P\mid p}\left(\frac a{\mathfrak P}\right)_\ell=1.
\]

Indeed \(p\) splits completely. If \(\alpha=(a/\mathfrak P_0)_\ell\), rationality of \(a\) makes the displayed factors the full Galois orbit of \(\alpha\). Their product is \(N_{K/\mathbb Q}(\alpha)\). Writing \(\alpha=\zeta_\ell^m\) gives exponent \(m(1+\cdots+\ell-1)\), divisible by \(\ell\). This does not apply to a proper subset of the primes, a nonrational numerator, \(\ell=2\), or a numerator divisible by \(p\).

**Exact cubic certificate and orientation scope.** For \(\ell=3\), \(N=91=7\cdot13\), with local exponent conventions induced by the global root \(\rho=16\) of \(\Phi_3\),

\[
u(15)=(0,1),\qquad u(18)=(1,0),\qquad
15/18=16\pmod {91},\qquad u(16)=(2,1).
\]

Hence the two inputs have the same diagonal phase, while their quotient has zero diagonal phase and neither local coordinate zero. CRT and surjectivity give eight units for every ordered phase pair and 24 for every diagonal-sum fiber. The four roots of \(\Phi_3\) modulo 91 are \(9,16,74,81\), with CRT pairs

\[
(2,9),(2,3),(4,9),(4,3).
\]

Two roots that agree in exactly one component expose 7 or 13 through their difference; globally conjugate roots differ by a unit.

A root \(\rho\) defines the ideal \(I_\rho=(N,\zeta-\rho)\subset\mathbb Z[\zeta]\), and evaluation gives \(\mathbb Z[\zeta]/I_\rho\cong\mathbb Z/N\mathbb Z\), so its norm is \(N\). It thereby supplies, possibly implicitly, one prime choice above each rational factor. For composite \(N\), the ideal is not prime. Its existence proves neither that such an orientation is hard or noncanonical to compute, nor that one root factors \(N\); the usual immediate gcds for \(\rho=16\) are trivial. Only additional roots with different CRT choices are shown to split this example.

**Scope.** P15 is a method failure for individually factor-swap-invariant multiplicative scalar carriers and their transcript-internal combinations. It is not a no-go theorem for higher-power residue methods in general. The proofs and independent finite checks, including the failed-run dispositions, are preserved under experiments/F09_phasekill, experiments/F09_phase_audit, and experiments/F09_phase_reconstruct.

## P16 — P14's full-rank witness has an intermediate determinant separator

**Status:** promoted.

**Verification record:** the finite construction and uniform-computability statement passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

**Fixed determinant.** Let

\[
N=79403,\qquad r=269,\qquad
P=X^{269}-1,
\]

and form

\[
H=(X+1)^N-X^N-1
\quad\text{in}\quad
(\mathbb Z/N\mathbb Z)[X]/(P),
\]

using the representative of degree below 269. Its global degree is \(n=268\). For \(0\le j\le n\), let \(D_j\) be the determinant of

\[
(U,V)\longmapsto UP+VH,
\qquad \deg U<n-j,\quad \deg V<269-j,
\]

after projecting to coefficient degrees \(j,\ldots,269+n-j-1\), with rows increasing and the increasing \(P\)-shift columns followed by the increasing \(H\)-shift columns. The matrix dimension is \(269+n-2j\).

**Exact certificate.** A factor-free increasing-index computation gives

\[
\gcd(D_j,N)=1\quad(0\le j\le46),
\]

followed by

\[
D_{47}\equiv30352\pmod {79403},
\qquad \gcd(30352,79403)=271.
\]

The witness matrix has dimension \(443\). Reduction of the same global coefficient vector gives local degrees 46 and 268 and

\[
D_{47}\equiv0\pmod{271},
\qquad
D_{47}\equiv173\pmod{293}.
\]

Reduction commutes with determinant formation because both are polynomial operations in the matrix entries. The local degree drop must be treated by retaining the global formal degree \(n=268\); with that padding, at \(j=47>46\) the unshifted \(H\)-column is zero modulo 271.

Under the fixed ordering of standard positive shifts and then increasing \(j\), \((a,j)=(1,47)\) is the first determinant separator for this input and convention. No broader minimality is claimed.

**Uniform computability.** Cyclic binary powering forms every \(H_a\) in \(O(r^2\log N)\) ring operations under schoolbook multiplication. Each \(D_j\) is computable division-free over \(\mathbb Z/N\mathbb Z\), for example by Berkowitz, in polynomially many operations on matrices of dimension at most \(2r\). Scanning \(O(r)\) indices over a shift range polynomial in \(\log N\) therefore has polynomial bit complexity when \(r=\operatorname{poly}(\log N)\). This proves computability of the family, not universal separation.

**Scope.** The certificate is not PSC-specific. The constant coefficient already satisfies

\[
[X^0]H=36585,\qquad \gcd(36585,N)=271,
\]

and the leading coefficient also separates. Thus P16 only proves that P14's equality of full multiplication nullities does not control intermediate determinants; it gives no advantage over coefficient scanning and no factoring theorem. The proof-blind reconstruction's early preselected-index probe had incomplete, deleted provenance; it was restored and replayed but is explicitly disqualified. Authoritative reconstruction evidence is R01–R03 under experiments/F04_psc_reconstruct.

## P17 — constructing the natural cubic order-3 automorphism is factoring-equivalent

**Status:** promoted.

**Verification record:** the algebraic theorem, probability calculation, reverse construction, and finite certificates passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

**Local classification.** Let \(k=\mathbb F_\ell\) for an odd prime \(\ell\), let \(f\in k[X]\) be monic, squarefree, and cubic, and put \(A=k[X]/(f)\). For factorization types \((111),(12),(3)\), respectively,

\[
\operatorname{Aut}_k(A)\cong S_3,C_2,C_3.
\]

Among squarefree monic cubics the exact type probabilities are

\[
\frac{\ell-2}{6\ell},\qquad \frac12,\qquad
\frac{\ell+1}{3\ell}.
\]

The discriminant character is \(+1\) for types \((111),(3)\) and \(-1\) for type \((12)\). This follows by writing the discriminant as the square of the Vandermonde product: Frobenius multiplies that product by the sign of its permutation of the three roots.

**Recognizable promise and extraction.** Let \(N=pq\) for distinct odd primes and let \(f\in(\mathbb Z/N\mathbb Z)[X]\) be monic cubic with

\[
\gcd(\operatorname{disc}(f),N)=1,
\qquad
\left(\frac{\operatorname{disc}(f)}N\right)=-1.
\]

Exactly one local algebra then has type \((12)\), while the other has type \((111)\) or \((3)\). Suppose an algorithm returns a globally nonidentity automorphism of \(A_N=(\mathbb Z/N\mathbb Z)[X]/(f)\) satisfying \(\sigma^3=1\). Write

\[
\sigma(x)=a+bx+cx^2,
\qquad x=X\bmod f.
\]

The type-\((12)\) automorphism group \(C_2\) contains no nonidentity element whose cube is the identity. Therefore \(\sigma\) is the identity in that component and nonidentity in the other. Consequently

\[
\gcd(N,a,b-1,c)
\]

is exactly the prime supporting the type-\((12)\) component; equivalently at least one of the three individual coefficient gcds is that proper factor. The endomorphism, invertibility, order, and nonidentity conditions are all checkable by reducing fixed-degree polynomial identities modulo \(f\), so a purported output is efficiently verifiable.

**Reduction from factoring.** Sample the three nonleading coefficients of a monic cubic uniformly modulo \(N\), compute its discriminant, and first take its gcd with \(N\). If that gcd is nontrivial, return it. If the discriminant is a unit with Jacobi symbol \(-1\), call the promised automorphism solver and apply the coefficient gcd above; otherwise resample. A trial reaches the promise with exact probability

\[
\frac{(p-1)(q-1)}{2pq}\ge\frac4{15}.
\]

Thus at most \(15/4\) trials are expected. Exact rejection sampling consumes fewer than \(6\lceil\log_2N\rceil\) expected random bits for the three coefficients. Discriminants have constant degree, and gcd, Jacobi, verification, and extraction all have polynomial bit complexity. Hence a Las Vegas expected-polynomial solver for this promised construction problem yields a Las Vegas expected-polynomial algorithm for factoring every distinct odd semiprime.

**Reverse reduction.** Given \(p,q\), put the identity on the type-\((12)\) side. On a type-\((3)\) side use Frobenius; on a type-\((111)\) side factor the fixed-degree polynomial and interpolate a 3-cycle of its roots. CRT-lift the three coefficients. Fixed-degree finite-field factorization and modular exponentiation give expected polynomial bit complexity (for example \(\widetilde O((\log N)^2)\) with standard arithmetic). Thus factoring also solves every promised instance, establishing the stated Las Vegas equivalence.

**Order-2 boundary.** If exactly one local type is \((3)\), every globally nonidentity involution is likewise component-selective, so the promised-input extraction theorem is valid. There is no analogous Jacobi recognizer. In fact

\[
N=15,\qquad f=X^3+10X^2+6X+10
\]

has squarefree types \((12)\) modulo 3 and \((111)\) modulo 5 and unit discriminant \(11\pmod {15}\) of Jacobi symbol \(-1\). Nevertheless

\[
\sigma(x)=2+3x+8x^2
\]

is an involution nonidentity in both components, while

\[
\gcd(15,2)=\gcd(15,3-1)=\gcd(15,8)=1.
\]

Calling an order-2 promise solver on every Jacobi-minus-one sample is therefore incorrect; a promise-only solver also need not terminate off-promise.

**Geometric scope and certificates.** Over a separable closure, the order-dividing-3 and order-dividing-2 automorphism subschemes have constant ranks 3 and 4. Their varying rational-point counts are a descent phenomenon, including in characteristic 3. Hence full geometric nonemptiness or rank cannot detect the local mismatch, but this says nothing universal about coordinate projections or eliminants. On the promised example \(N=35,f=X^3+2\), the maps \(x\mapsto11x\) and \(x\mapsto16x\) expose 5. The proof-blind verifier also checked a characteristic-3 promised example over \(N=15\) and the order-2 counterexample above. Exact sources, timeouts, logs, outputs, and failed-run dispositions are preserved under `experiments/F10_autkill`, `experiments/F10_aut_audit`, and `experiments/F10_aut_reconstruct`.

P17 is a method failure for obtaining a factoring advantage by directly searching for this natural component-selective cubic automorphism. It does not rule out other fixed-degree algebras, other certificates, or a factor-free descent mechanism that is not already the hidden CRT choice.

## P18 — the coefficient-hard AKS witness is also hard for every fixed canonical PSC

**Status:** promoted.

**Verification record:** the field theorem and complete finite obstruction passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

**Fixed determinant theorem.** Let \(K\) be a field and let nonzero \(F,G\in K[X]\) have degrees \(m>n\). For \(0\le j\le n\), define \(D_j(F,G)\) as the determinant of

\[
(U,V)\longmapsto UF+VG,
\qquad \deg U<n-j,\quad \deg V<m-j,
\]

projected to coefficient degrees \(j,\ldots,m+n-j-1\), using increasing output rows, increasing shifts of \(F\) first, and then increasing shifts of \(G\). Run ordinary Euclidean division

\[
R_0=F,\quad R_1=G,\quad
R_{i-1}=Q_iR_i+R_{i+1}
\]

through the last nonzero remainder \(R_s\), and write

\[
m=d_0>d_1=n>d_2>\cdots>d_s=g.
\]

Then

\[
D_j(F,G)\ne0
\quad\Longleftrightarrow\quad
j\in\{d_1,\ldots,d_s\}.
\]

This includes a positive-degree gcd, arbitrary abnormal degree gaps, a constant second polynomial, and the top formula

\[
D_n(F,G)=\operatorname{lc}(G)^{m-n}.
\]

**Proof.** Write \(R_i=S_iF+T_iG\). Extended Euclid gives coprime \(S_i,T_i\) and, for \(i\ge2\),

\[
\deg S_i=n-d_{i-1},\qquad
\deg T_i=m-d_{i-1}.
\]

The defining matrix is singular exactly when a nonzero bounded pair makes \(UF+VG\) have degree below \(j\). If \(d_{i+1}<j<d_i\), the pair \((S_{i+1},T_{i+1})\) is within both bounds and maps to \(R_{i+1}\), whose degree is below \(j\). If \(j<g\), the exact syzygy \((G/R_s,-F/R_s)\) is within both bounds. Hence all indices outside the displayed remainder-degree set give zero determinants.

Now take \(j=d_i\) and suppose a bounded pair gives \(L=UF+VG\) with \(\deg L<d_i\). The identity

\[
V R_i-T_iL=(VS_i-T_iU)F
\]

has both terms on its left of degree below \(m\); therefore its right side must be zero. Coprimality forces \((U,V)=C(S_i,T_i)\), whence \(L=CR_i\), which cannot have degree below \(d_i\) unless \(C=0\). Thus the square map is injective and \(D_{d_i}\ne0\). At \(i=1\), the \(U\)-space is zero and multiplication by \(G\) gives the same conclusion; its increasing-order matrix is triangular with the displayed top determinant. This proves the theorem without any PRS normalization or dense-list convention.

**Finite AKS obstruction.** Set

\[
N=20000000499999937
=100000007\cdot199999991,\qquad r=2953,\qquad
P=X^{2953}-1.
\]

For every standard shift \(1\le a\le2942\), first form the degree-below-2953 global vector

\[
H_a=(X+a)^N-X^N-a
\quad\text{in}\quad
(\mathbb Z/N\mathbb Z)[X]/(P).
\]

Every \(H_a\) has degree 2952, and every one of the

\[
2942\cdot2953=8{,}687{,}726
\]

global coefficients is a unit modulo \(N\). Reducing those same global vectors to either factor field gives the complete ordinary Euclidean chain

\[
2953,2952,2951,\ldots,1,0
\]

for every shift. The theorem therefore makes all 8,687,726 fixed canonical determinants nonzero in each field, for 17,375,452 nonzero local statuses in total. Every corresponding global determinant is a unit, so no gcd from this entire fixed PSC scan splits \(N\).

The hostile audit independently reconstructed every global vector before local reduction, checked all coefficient gcds and chains, materialized complete determinant residue vectors at shifts 1 and 2942, and passed a full artifact/hash audit. Its direct theorem stress test covered 4,932 field pairs and 17,556 defining determinants. The proof-blind reconstruction independently proved the theorem, checked 231,494 literal determinants over small fields, materialized all global vectors in a separate artifact, verified every field chain and status, and used both direct-composite exponentiation and a separate general-remainder implementation for spot checks.

**Scope.** P18 is an exact finite counterexample to universal factor localization by individual coefficients, individual multiplication nullities, or the fixed canonical \(D_j\) family within this one standard minimal-\(r\), standard-shift AKS scan. It is not an asymptotic lower bound. It does not address nonstandard \(r\), other group-algebra errors, arbitrary Sylvester minors or pivot-dependent elimination transcripts, joint-shift column matroids, or a uniform separation theorem. The supplied factorization is used only to certify the two local reductions; no factoring algorithm follows.

Every named source, timeout, log, output, and failed-run disposition is preserved under `experiments/F04_psc_coefficient_hard`, `experiments/F04_psc_coefficient_audit`, and `experiments/F04_psc_coefficient_reconstruct`. Non-authoritative failed launches, overwritten early source revisions, sparse Sage-list assumptions, incidental pre-source diagnostics, and manifest-packaging failures are all explicitly excluded from the proof.

## P19 — complete factoring reduces exactly to search CVP on one-hot multiplication lattices, but the natural tractability claims fail

**Status:** promoted.

**Verification record:** the corrected theorem passed a focused hostile audit and a proof-blind reconstruction from a bare statement. No cross-family audit has run. All parts are symbolic; no computation is evidence for this result.

**Exact affine multiplication system.** Let \(N\) be an odd composite of bit length \(n\). Enumerate

\[
2\le a\le b,\qquad a+b\in\{n,n+1\}.
\]

For a fixed pair put \(L=a+b\) and \(H=\lceil\log_2 a\rceil\). Use integer coordinates

\[
x_i\ (0\le i<a),\qquad y_j\ (0\le j<b),
\]

four tuple coordinates \(t_{ij}^{uv}\) for every \(0\le i<a\), \(0\le j<b\), and \((u,v)\in\{0,1\}^2\), and binary-digit coordinates for carries

\[
C_k=\sum_{h=0}^{H-1}2^h c_{k,h}\qquad(1\le k<L),
\]

with \(C_0=C_L=0\). Impose the affine integer equations

\[
\sum_{u,v}t_{ij}^{uv}=1,
\]

\[
x_i=t_{ij}^{10}+t_{ij}^{11},\qquad
y_j=t_{ij}^{01}+t_{ij}^{11},
\]

\[
x_0=y_0=x_{a-1}=y_{b-1}=1,
\]

and, for every \(0\le k<L\),

\[
C_k+\sum_{i+j=k}t_{ij}^{11}=N_k+2C_{k+1},
\]

where \(N_k=0\) above the leading bit of \(N\). The last column equation is essential. The total number of integer coordinates is

\[
M=a+b+4ab+(L-1)H=O(n^2),
\]

and the system has \(O(n^2)\) equations with \(O(\log n)\)-bit coefficients.

**Binary-solution theorem.** The binary solutions of this system are exactly the factorizations \(xy=N\) with bit lengths \((a,b)\). Indeed, one-hotness and the marginal equations force \(t_{ij}^{11}=x_i y_j\). Multiplying the column equations by \(2^k\) and summing telescopes the carries and gives \(xy=N\). Conversely, ordinary schoolbook multiplication supplies all tuple and carry coordinates for any such factorization. Its carries obey

\[
0\le C_k\le a-1,
\]

because each column contains at most \(a\) products and

\[
C_{k+1}=\frac{C_k+\sum_{i+j=k}x_i y_j-N_k}{2};
\]

therefore \(H\) digits suffice.

Every nontrivial factorization has an ordering \(x\le y\) whose bit lengths occur in the enumeration, since

\[
2^{a+b-2}\le N<2^{a+b}
\quad\Longrightarrow\quad
a+b\in\{n,n+1\}.
\]

This includes unbalanced composites, repeated factors, and prime powers.

**Exact CVP reduction.** Write the system as \(Az=d\). Polynomial-bit HNF or SNF decides integral feasibility and, when feasible, computes an integral particular solution \(z_0\) and a basis \(B\) of \(\ker_{\mathbb Z}A\). Thus its integral solutions are the affine lattice

\[
z_0+B\mathbb Z^r.
\]

At the target \(h=\tfrac12\mathbf 1\), every integral coordinate contributes at least \(1/4\) to squared distance, with equality exactly at 0 or 1. Hence

\[
\min_{Az=d,\ z\in\mathbb Z^M}\|z-h\|^2=M/4
\]

exactly when a binary multiplication witness exists; otherwise the minimum is at least \(M/4+2\). Every minimizer at the baseline is therefore a valid factor witness. Equivalently, query the embedded integer lattice generated by \(2B\) at the integer target

\[
\mathbf 1-2z_0.
\]

This multiplies squared distances by four, so the baseline and separation become \(M\) and at least \(M+8\). A polynomial-size padding also converts the instance to a convention requiring full ambient rank. The oracle must return a closest vector: this is a reduction to search exact Euclidean CVP, not merely an invocation of an unspecified decision oracle.

Even inputs are split directly and deterministic polynomial-time primality testing terminates prime leaves. At each odd composite node, try the \(O(n)\) length pairs, skip integrally infeasible systems, decode and directly verify a baseline answer, and recurse on the two factors. The factorization tree has \(O(n)\) nodes, so this is a deterministic polynomial-bit Turing reduction from complete integer factoring to exact search CVP on this explicit lattice family, with \(O(n^2)\) oracle calls of polynomial size.

**The natural structural shortcuts do not follow.** In the displayed variable-equation incidence graph, every pair \((i,j)\) supplies the internally disjoint path

\[
x_i-E^x_{ij}-t_{ij}^{11}-E^y_{ij}-y_j.
\]

Deleting other incidences and contracting these paths produces \(K_{a,b}\), so this presentation has treewidth at least \(\min(a,b)\). Its \(ab\) one-hot rows are linearly independent, since each contains a private \(t_{ij}^{00}\) coordinate, so the affine lattice has codimension at least \(ab\). These are claims about this presentation, not universal lower bounds for every exact encoding or every basis of the same lattice.

Dropping the tuple consistency and keeping only a lifted binary matrix \(W=(w_{ij})\), its anti-diagonal sums, and the carries gives a lower-codimension convolution relaxation but loses Boolean rank one. For \(N=25\), \(a=b=3\), the genuine lift and a spurious lift are

\[
W_{\rm true}=
\begin{pmatrix}
1&0&1\\
0&0&0\\
1&0&1
\end{pmatrix},
\qquad
W_{\rm spurious}=
\begin{pmatrix}
1&0&1\\
0&1&0\\
0&0&1
\end{pmatrix}.
\]

Both have anti-diagonal sums \((1,0,2,0,1,0)\) and carries \((0,0,0,1,0,0,0)\), but \(\det W_{\rm spurious}=1\). Both are binary and attain the absolute half-target baseline, while the second is not an outer product. This proves only that a closest relaxed matrix need not itself decode as a factor matrix. It does not rule out all postprocessing—the common convolution polynomial in this example factors as \((1+T^2)^2\)—and it proves no width lower bound for every possible restoration of rank one.

**Scope.** P19 is a rigorous oracle reduction and a precise failure of the displayed bounded-width, low-codimension, and direct relaxed-decoding arguments. It supplies no polynomial-time algorithm for exact CVP on these lattices. Proving such an algorithm would already prove polynomial-time classical factoring through the reduction, while no theorem here excludes a different exact lattice encoding or favorable presentation.

The complete derivation and its two independent checks are preserved under `experiments/F11_structured_cvp_kill`, `experiments/F11_structured_cvp_audit`, and `experiments/F11_structured_cvp_reconstruct`.

## P20 — balanced Hasse bounds synchronize cleared elliptic collisions, while a torus evaluator would factor

**Status:** promoted.

**Verification record:** the corrected identities, universal obstruction, finite certificate, conditional factoring reduction, and bit complexity passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

**Elliptic identity.** Let

\[
E:y^2=x^3+Ax+B
\]

be nonsingular over a field of characteristic different from 2 and 3. Use the standard division polynomials \(\psi_k\) and

\[
\phi_k=x\psi_k^2-\psi_{k+1}\psi_{k-1},
\qquad
x([k]P)=\frac{\phi_k(P)}{\psi_k(P)^2}.
\]

The division-polynomial addition recurrence gives, as a polynomial identity,

\[
\phi_i\psi_j^2-\phi_j\psi_i^2
=\psi_{i+j}\psi_{j-i}
\qquad(1\le i<j).
\]

Therefore the division-free numerator of the pairwise \(x\)-collision product is

\[
C_m(P)
=\prod_{1\le i<j\le m}
  (\phi_i\psi_j^2-\phi_j\psi_i^2)(P)
=\prod_{1\le i<j\le m}\psi_{i+j}(P)\psi_{j-i}(P).
\]

If the affine point \(P\) has order \(t\), then \(\psi_k(P)=0\) exactly when \(t\mid k\). For \(m\ge3\), the nonconstant indices occurring in the last product are exactly \(2,3,\ldots,2m-1\), each with positive multiplicity. Hence

\[
C_m(P)=0\quad\Longleftrightarrow\quad t\le2m-1.
\]

Moreover \(\psi_1(P),\ldots,\psi_m(P)\) are all nonzero exactly when \(t>m\). Thus the interval \(m<t\le2m-1\) consists of denominator-clean collisions caused by \(x(Q)=x(-Q)\). The restriction \(m\ge3\) is necessary: at \(m=2\), a point of order 2 need not zero \(C_2=\psi_3\).

**Universal balanced obstruction.** Take

\[
N=10403=101\cdot103,
\qquad m=\lfloor\sqrt N\rfloor=101,
\qquad 2m-1=201.
\]

For any short Weierstrass curve with good reduction at a prime \(\ell\), Hasse's theorem gives

\[
\#E(\mathbb F_\ell)
\le\left\lfloor\ell+1+2\sqrt\ell\right\rfloor.
\]

The bounds at 101 and 103 are 122 and 124. Every affine local point therefore has order at most 201. For every short Weierstrass curve good at both primes and every global affine point,

\[
C_{101}(P)\equiv0\pmod {101},
\qquad
C_{101}(P)\equiv0\pmod {103}.
\]

Thus \(C_{101}(P)\equiv0\pmod N\) and \(\gcd(C_{101}(P),N)=N\). This is independent of the curve and point distribution. If the curve discriminant \(\Delta\) is not a unit, \(1<\gcd(\Delta,N)<N\) already splits the input, but \(\gcd(\Delta,N)=N\) is only a retry case; the universal statement above is specifically for good reduction at both primes.

The checked denominator-clean witness is

\[
E:y^2=x^3+x+5,
\qquad P=(5461,5889)\pmod {10403}.
\]

Its discriminant is \(-10864\equiv9942\pmod N\), a unit. Modulo 101, \(P=(7,31)\), \(\#E=112\), and \(P\) has order 112; the first lexicographic collision through \(m=101\) is \((11,101)\). Modulo 103, \(P=(2,18)\), \(\#E=106\), and \(P\) has order 106; the first collision is \((5,101)\). Both point orders exceed 101, so every denominator through \(m\) is nonzero, while the two colliding index sums equal the respective orders.

**Torus identity and order test.** For any commutative ring,

\[
\begin{aligned}
D_m(a)
&=\prod_{0\le i<j<m}(a^i-a^j)\\
&=a^{\binom m3}S_m(a),\\
S_m(a)
&=\prod_{d=1}^{m-1}(1-a^d)^{m-d}.
\end{aligned}
\]

Indeed, the extracted powers have total exponent \(\binom m3\), and the difference \(d=j-i\) occurs \(m-d\) times. If \(a\) is a unit modulo a prime \(\ell\), then

\[
S_m(a)=0\text{ in }\mathbb F_\ell
\quad\Longleftrightarrow\quad
\operatorname{ord}_\ell(a)\le m-1.
\]

For a distinct semiprime \(N=pq\), \(p<q\), and \(m=\lfloor\sqrt N\rfloor\), every unit makes \(S_m(a)=0\pmod p\), while it is nonzero modulo \(q\) exactly when \(\operatorname{ord}_q(a)\ge m\). The exact conditional separation probability for a uniform unit modulo \(q\) is

\[
\frac{1}{q-1}
\sum_{\substack{d\mid q-1\\d\ge m}}\varphi(d),
\]

and in particular is at least \(\varphi(q-1)/(q-1)\) by primitive residues.

**Conditional complete-factoring theorem.** Assume a uniform exact algorithm

\[
\operatorname{Eval}(N,a,m)=S_m(a)\bmod N
\]

with worst-case bit cost \(T(\log N+\log m)\), where \(T\) is polynomial. Then there is a classical Las Vegas algorithm that completely factors every positive integer in expected polynomial bit complexity.

Handle powers of two, deterministic primality testing, and exact perfect-power detection first. For an odd composite \(N\) that is not a perfect power, write

\[
N=\prod_i p_i^{e_i},
\qquad s=\sum_i e_i,
\]

and let \(p_{\min}<p_{\max}\) be its smallest and largest distinct prime factors. The weighted geometric mean gives

\[
p_{\min}\le
m_s=\left\lfloor N^{1/s}\right\rfloor
<p_{\max}.
\]

The unknown \(s\) lies between 2 and the bit length \(n\), so compute exact integer-root floors \(m_k=\lfloor N^{1/k}\rfloor\) for every \(2\le k\le n\). In one trial choose \(a\) uniformly from \(\{0,\ldots,N-1\}\). A proper \(\gcd(a,N)\) already splits the input; otherwise evaluate \(S_{m_k}(a)\) and take its gcd with \(N\) for each \(k\).

At \(k=s\), every unit has order at most \(p_{\min}-1\le m_s-1\) modulo \(p_{\min}\), so that prime divides \(S_{m_s}(a)\). If \(a\bmod p_{\max}\) is primitive, then its order is \(p_{\max}-1\ge m_s\), so \(p_{\max}\) does not divide the product and the gcd is proper. This remains valid with repeated prime powers.

For \(t=p_{\max}-1\), if \(r\) is the number of distinct prime divisors of \(t\), then

\[
\frac{t}{\varphi(t)}
=\prod_{q\mid t}\frac q{q-1}
\le r+1
\le1+\log_2t.
\]

Because sampling is uniform modulo \(p_{\max}\), the success probability of the primitive-residue event is

\[
\frac{\varphi(p_{\max}-1)}{p_{\max}}
\ge\frac{1}{2(1+n)}.
\]

Independent retries therefore terminate almost surely after \(O(n)\) expected trials. Each trial makes \(O(n)\) evaluator calls on \(O(n)\)-bit inputs, so one proper split costs

\[
O\bigl(n^2T(O(n))+\operatorname{poly}(n)\bigr)
\]

in expectation. Recursing only on verified proper factors creates at most \(O(n)\) split nodes; exact perfect-power handling preserves multiplicities. A coarse complete-factorization bound is

\[
O\bigl(n^3T(O(n))+\operatorname{poly}(n)\bigr).
\]

Every proposed divisor is checked by gcd and exact division, and prime leaves are certified by deterministic primality testing, so the algorithm is Las Vegas and covers evens, primes, prime powers, repeated factors, and arbitrary composites.

**Missing lemma and scope.** No polylogarithmic evaluator is supplied. The recurrences

\[
P_d=P_{d-1}(1-a^d),
\qquad
S_{d+1}=S_dP_d
\]

take \(O(m)\) explicit iterations. The cyclotomic factorization of \(S_m\) still displays \(m-1\) factors. Neither observation is a lower bound, but neither proves the evaluator hypothesis. Thus P20 contains an unconditional elliptic obstruction and torus order theorem plus an exact conditional reduction; it is not an unconditional factoring algorithm.

The discovery, hostile audit, proof-blind reconstruction, named sources, timeouts, logs, outputs, and failed-run dispositions are preserved under `experiments/F12_elliptic_collision_kill`, `experiments/F12_elliptic_collision_audit`, and `experiments/F12_elliptic_collision_reconstruct`.

## P21 — fixed-binomial shortcuts do not supply the torus threshold evaluator

**Status:** promoted.

**Verification record:** the corrected threshold theorem, valuation statement, explicit counterexamples, recurrence accounting, and scope passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

Put \(M=m-1\) and

\[
P_M(a)=\prod_{d=1}^{M}(1-a^d),
\qquad
S_m(a)=\prod_{d=1}^{M}(1-a^d)^{m-d}.
\]

For every prime \(\ell\), the two products have the same zero set modulo \(\ell\). Over an arbitrary integer modulus they need not give the same gcd: integer valuations instead give

\[
v_\ell(P_M(a))\le v_\ell(S_m(a)),
\qquad
\gcd(P_M(a),N)\mid\gcd(S_m(a),N).
\]

The distinction is operationally real. For

\[
N=875=5^3\cdot7,
\qquad a=631,
\qquad m=3,
\]

one has

\[
\gcd(P_2(a),875)=175,
\qquad
\gcd(S_3(a),875)=875.
\]

Thus the unweighted product is at least as useful for obtaining a proper split, but it is neither the requested weighted residue nor a gcd-preserving replacement on nonsquarefree inputs.

**Threshold-binomial obstruction.** Fix \(M\ge2\), and suppose

\[
F(a)=\prod_{h=1}^{r}(1-a^{L_h})^{w_h},
\qquad L_h,w_h\in\mathbb Z_{>0},
\]

has, over every finite field and every unit \(a\), the exact zero predicate

\[
F(a)=0
\quad\Longleftrightarrow\quad
\operatorname{ord}(a)\le M.
\]

Every positive integer \(t\) occurs as the order of a unit in some finite field: choose a prime \(q\nmid t\), use \(t\mid q^{\varphi(t)}-1\), and use cyclicity of the resulting finite-field unit group. Applying this first with \(t=L_h\) forces every \(L_h\le M\). Applying it with \(M/2<t\le M\) forces \(t\mid L_h\) for some \(h\), and \(t\le L_h\le M<2t\) then forces \(L_h=t\). Hence the exponent list contains every integer

\[
\lfloor M/2\rfloor+1,\ldots,M
\]

and therefore at least \(\lceil M/2\rceil\) distinct exponents. This rules out replacing the exact universal threshold predicate by a polylogarithmic number of positive binomial factors. It says nothing about sums, rational functions, characteristic-dependent formulas, or arbitrary arithmetic circuits.

The simplest lcm compression already has a concrete false positive. With \(M=4\), the proposed exponent is \(\operatorname{lcm}(1,2,3,4)=12\). The element 2 has order 12 in \(\mathbb F_{13}^{\times}\), so \(1-2^{12}=0\), even though

\[
P_4(2)=3\pmod {13},
\qquad
S_5(2)=7\pmod {13}.
\]

**Other exact but narrow boundaries.** For shifted blocks

\[
Q(s,n)=\prod_{d=1}^{n}(1-a^{s+d}),
\qquad
T(s,n)=\prod_{d=1}^{n}(1-a^{s+d})^{n+1-d},
\]

direct splitting gives

\[
Q(s,n+k)=Q(s,n)Q(s+n,k),
\]

\[
T(s,n+k)=T(s,n)Q(s,n)^kT(s+n,k).
\]

The literal syntax-directed evaluator recursively computes two shifted children, so its tree has \(n\) singleton leaves and linear ring-operation cost. This is an accounting theorem for that evaluator, not a lower bound for a shared or differently represented circuit.

The quotient set \(\{\lfloor M/d\rfloor:1\le d\le M\}\) has at least \(2\lfloor\sqrt M\rfloor-1\) elements, so a literal constant-work-per-equal-floor cyclotomic grouping is not polylogarithmic. Nonconstant weights show that an unweighted group aggregate loses information, but do not exclude a succinct weighted aggregate. Finally, every nonzero characteristic-zero polynomial vanishing at all roots of unity of order at most \(M\) has degree at least

\[
\sum_{t=1}^{M}\varphi(t)
\ge
\frac{M^2}{4(1+\log_2 M)}.
\]

Degree and dense materialization are not arithmetic-circuit lower bounds.

**Scope.** P21 closes the fixed positive-binomial/lcm compression, the literal two-child recursion, and the displayed grouping/materialization shortcuts. It does not prove an evaluation-time or circuit-size lower bound for \(P_M\) or \(S_m\), and it does not provide the evaluator assumed in P20. The general polylogarithmic torus evaluator remains open.

The candidate analysis, hostile audit, and proof-blind reconstruction are preserved under `experiments/F14_torus_qfactorial_evaluator`, `experiments/F14_torus_qfactorial_audit`, and `experiments/F14_torus_qfactorial_reconstruct`.

## P22 — exponent-\(N\) lifts erase principal input digits, and fixed canonical output digits rarely split balanced inputs

**Status:** promoted.

**Verification record:** the structural formulas, corrected twin exception, carrier probabilities, balanced-family upper bound, and scope passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

Let \(N=pq\) for distinct odd primes and define

\[
\tau_N(a)=a^N\pmod {N^2}.
\]

**Principal kernel and local image.** Reduction of units modulo \(N^2\) to units modulo \(N\) has the full kernel

\[
K=\{1+kN\pmod {N^2}:k\bmod N\}.
\]

Its two local principal coordinates are \(qk\bmod p\) and \(pk\bmod q\), so uniform \(k\bmod N\) ranges over the whole local principal kernel. Nevertheless,

\[
(1+kN)^N\equiv1\pmod {N^2},
\qquad
(a+Nt)^N\equiv a^N\pmod {N^2}.
\]

Thus \(\tau_N\) kills all principal input digits and factors through reduction modulo \(N\). If \([x]_\ell\) denotes the Teichmüller lift of \(x\in\mathbb F_\ell\), with \([0]_\ell=0\), CRT gives the exact formula

\[
\tau_N(a)=
\bigl([a\bmod p]_p^q,[a\bmod q]_q^p\bigr)
\pmod {p^2q^2}.
\]

This also covers nonunits locally: a component divisible by its prime maps to zero modulo that prime squared.

On the quotient

\[
(\mathbb Z/N^2\mathbb Z)^\times/K
\cong C_{p-1}\times C_{q-1},
\]

the map is exponentiation by \(N\). With \(\lambda=\operatorname{lcm}(p-1,q-1)\), it is invertible exactly when \(\gcd(N,\lambda)=1\). Known factors then give the inverse exponent \(d=N^{-1}\bmod\lambda\) and the factor-aware untwist

\[
\tau_N(a)^d=([a]_p,[a]_q).
\]

No factoring equivalence for computing an untwist without the factors is proved.

Every \(A\in\operatorname{im}\tau_N\), including a locally zero component, satisfies

\[
A^{N+1}=A^{p+q}\pmod {N^2},
\]

because \((N+1)-(p+q)=(p-1)(q-1)\). For a unit this reveals only a congruence modulo \(\operatorname{ord}(A)\); it is an order identity, not an extraction of the integer \(p+q\).

**Consecutive iterates and additive defects.** Assume \(p<q\), take a uniform unit \(a\), and put \(A_r=\tau_N^r(a)\) for \(r\ge1\). Then

\[
A_r\equiv[a]_p^{q^r}\pmod {p^2},
\qquad
A_r\equiv[a]_q^{p^r}\pmod {q^2}.
\]

The exact local equality probabilities for \(A_{r+1}=A_r\) are

\[
P_p=\frac{\gcd(q-1,p-1)}{p-1},
\qquad
P_q(r)=\frac{\gcd(p^r(p-1),q-1)}{q-1}.
\]

The two CRT events are independent, so the exact proper-gcd probability is

\[
P_p(1-P_q(r))+(1-P_p)P_q(r).
\]

Two Teichmüller lifts that agree modulo a local prime already agree modulo its square. Consecutive differences therefore have no local valuation-one category, and division by \(N\) after a full first gcd cannot create a second-stage split. This claim starts at \(r=1\) and does not cover arbitrary linear combinations or comparisons with the original lift.

For independent uniform units \(a,b\), define the additive defect

\[
\Delta(a,b)=\tau_N(a+b)-\tau_N(a)-\tau_N(b).
\]

Let \(\pi_{\ell,c}\) be the exact probability that its local value has valuation category \(c\in\{0,1,2\}\), where category 2 means zero modulo \(\ell^2\). A first gcd followed, only after a full gcd, by the quotient gcd has exact success probability

\[
1-\sum_{c=0}^{2}\pi_{p,c}\pi_{q,c},
\]

and the second stage adds exactly

\[
\pi_{p,1}\pi_{q,2}+\pi_{p,2}\pi_{q,1}.
\]

For twin primes \(q=p+2\) with \(p>3\), the local counts are

\[
(p-2,0,1),
\qquad
(q-4,0,3),
\]

so the two-stage success probability is

\[
\frac{4(p-2)}{(p-1)(p+1)},
\]

with no second-stage gain. The excluded twin \((3,5)\) is a real exception: its counts are \((0,1,1)\) and \((3,0,1)\), and its success probability is \(7/8\). No infinitude of twin primes is assumed.

**Canonical high-digit obstruction.** Choose canonical representatives \(A_r\in[0,N^2)\), put \(b_r=A_r\bmod N\) in \([0,N)\), and define

\[
H_r=\frac{A_r-b_r}{N}\pmod N.
\]

For every balanced pair of odd primes \(p<q<2p\), every fixed set \(R\) of \(K\) positive iterate indices chosen independently of the uniform unit \(a\) satisfies

\[
\Pr\left(\exists r\in R:
1<\gcd(H_r,N)<N\right)
\le
K\left(\frac2{q-1}+\frac1{p-1}\right)
\le\frac{3K}{p-1}.
\]

Indeed, the local exponent maps permute the unit groups. The interval \([0,N)\), whose length is below \(2p^2\), contains at most two representatives of each Teichmüller class modulo \(p^2\), while its length is below \(q^2\) and contains at most one representative of each class modulo \(q^2\). These are exactly the necessary conditions for \(p\mid H_r\) and \(q\mid H_r\), respectively; a union bound needs no independence across iterates.

Bertrand's postulate supplies infinitely many prime pairs \(p<q<2p\). Along this family \(p=2^{\Theta(\log N)}\), so every \(K=\operatorname{poly}(\log N)\) makes the displayed success bound exponentially small in the input bit length.

**Scope.** P22 kills the premise that exponentiation by \(N\) preserves a freely sampled principal input digit, and it rules out inverse-polynomial success for direct gcds of any fixed polynomial-size collection of canonical high digits from a uniform base on an infinite balanced family. It exactly characterizes the displayed consecutive and additive carriers. It does not cover deliberately engineered or adaptive nonuniform bases, cross-base combinations, other uses of the output digits, or all constructions over \(\mathbb Z/N^2\mathbb Z\); it is neither a hardness theorem nor a factoring algorithm.

The candidate analysis, hostile audit, and proof-blind reconstruction are preserved under `experiments/F13_teichmuller_lift_kill`, `experiments/F13_teichmuller_lift_audit`, and `experiments/F13_teichmuller_lift_reconstruct`.

## P23 — small affine bases still require exponential faithful permutation degree

**Status:** promoted.

**Verification record:** the corrected prime-cycle, normal-subgroup, minimum-degree, base-size, and vector-stabilizer claims passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

For a nontrivial finite group \(G\), let \(\mu(G)\) be its minimum faithful permutation degree.

**Prime-order and cyclic obstructions.** If \(G\) contains an element of prime order \(p\), every faithful permutation action has degree at least \(p\): the image of that element must contain a \(p\)-cycle. If a diagonal family of actions is faithful, at least one component sees that element and therefore has degree at least \(p\).

More generally, if

\[
r=\prod_i\ell_i^{e_i}\ge2,
\]

then

\[
\mu(C_r)=\sum_i\ell_i^{e_i}.
\]

Disjoint cycles of the displayed prime-power lengths give the upper bound. For the lower bound, the cycle lengths in a faithful action must have least common multiple \(r\). Assign each maximal prime power \(\ell_i^{e_i}\) to a cycle whose length it divides. The prime powers assigned to one cycle are pairwise coprime, their product divides that cycle length, and their product is at least their sum. Summing over cycles proves the formula.

**Local affine group.** Let

\[
G_p=\operatorname{AGL}_1(\mathbb F_p)
=T_p\rtimes\mathbb F_p^\times,
\qquad T_p\cong C_p.
\]

The translation subgroup and the prime-cycle bound give \(\mu(G_p)\ge p\), while the natural action on \(\mathbb F_p\) is faithful, so

\[
\mu(G_p)=p.
\]

That natural action has base size 2 for \(p>2\): fixing 0 and 1 fixes an affine map. At \(p=2\), its base size is 1 because \(G_2\cong C_2\) acts regularly. Thus constant base size and permutation degree are different invariants.

Every nontrivial normal subgroup of \(G_p\) contains \(T_p\). Indeed, a nonidentity translation generates \(T_p\); if a normal subgroup instead contains \(g=(a,b)\) with \(a\ne1\), then its commutator with translation by \(c\ne0\) is translation by \((a-1)c\), again generating \(T_p\). Consequently every nonfaithful local action kills every translation. A faithful diagonal family of \(G_p\)-actions must therefore contain an individually faithful component of degree at least \(p\). This last conclusion is special to \(G_p\), not to arbitrary groups or CRT products.

**Exact degree over composite rings.** For every \(N\ge2\) with prime-power decomposition

\[
N=\prod_i\ell_i^{e_i},
\]

one has the abstract group identity

\[
\boxed{
\mu\!\left(\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)\right)
=\sum_i\ell_i^{e_i}.}
\]

The translation by 1 has order \(N\), so restriction to its cyclic subgroup and the cyclic theorem give the lower bound. CRT identifies the affine group with the product of its prime-power local affine groups; their faithful natural actions on disjoint sets of sizes \(\ell_i^{e_i}\) give the upper bound. This upper construction uses the prime-power factorization and is not a factor-free algorithm. Its existence also does not show that every minimum-degree presentation exposes the factors.

For a distinct semiprime \(N=pq\), the minimum degree is \(p+q\). On balanced inputs it is \(2^{\Theta(\log N)}\). The natural degree-\(N\) action has base \((0,1)\); the factor-aware disjoint local action has base size 4 for odd \(p,q\), and 3 for \(N=2q\). Ordinary explicit-permutation Schreier–Sims or Luks-style orbit work is polynomial in this degree, and even reading a generator costs linear time in it. A constant-size base therefore does not make that explicit workflow polynomial in the input bit length.

**Succinct action boundary.** Affine maps still have the factor-free two-dimensional representation

\[
(a,b)\longmapsto
\begin{pmatrix}a&b\\0&1\end{pmatrix}.
\]

The affine point \(x\) is the homogeneous vector \((x,1)^T\); the zero vector is fixed by the whole matrix group. Separately, for a unit \(a\pmod N\), put

\[
M_a=\operatorname{diag}(a,1),
\qquad e_1=(1,0)^T.
\]

Literal vector equality gives

\[
M_a^ke_1=e_1
\quad\Longleftrightarrow\quad
a^k=1\pmod N,
\]

so

\[
\operatorname{Stab}_{\mathbb Z}(e_1)
=\operatorname{ord}_N(a)\mathbb Z.
\]

Computing the least positive stabilizing exponent in this formulation is exactly modular order finding. This is a vector statement; projectivizing \(e_1\) changes the stabilizer.

**Scope.** P23 closes only the inference that a small affine base yields a polynomial-size ordinary explicit-permutation stabilizer chain. It does not rule out a factor-sufficient quotient that discards translations, succinct/circuit actions, new matrix or module stabilizer algorithms, resampling arguments, or nonabelian lifts with a different mechanism. The displayed matrix formulation remains succinct but has not removed the order-finding dependency.

The candidate proof, hostile audit, and proof-blind reconstruction are preserved under `experiments/F16_affine_stabilizer_kill`, `experiments/F16_affine_stabilizer_audit`, and `experiments/F16_affine_stabilizer_reconstruct`.

## P24 — joint AKS prefix summaries agree while a full-column minor separates

**Status:** promoted.

**Verification record:** the global-before-local construction, P14 and P11 ranks, P11 row/prefix obstruction, exchange identity, exhaustive one-/two-tail scan, direct determinant certificate, factor-free evaluation bound, and artifact provenance passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

For standard shifts \(1\le a\le A\), form

\[
H_a=(X+a)^N-X^N-a
\quad\text{in}\quad
(\mathbb Z/N\mathbb Z)[X]/(X^r-1),
\]

and let \(M_N\) be the \(A\)-by-\(r\) matrix of their coefficients. The matrix is formed over \(\mathbb Z/N\mathbb Z\) before reduction modulo any prime factor.

**A genuine joint separator.** For

\[
N=79403=271\cdot293,\qquad (A,r)=(266,269),
\]

the local ranks are \(23\) and \(266\). The rank-23 side follows from

\[
H_a=(y^2+a)(y+a)^{22}-y^{24}-a,
\qquad y=X^2,
\]

whose coefficient functions span exactly \(a,a^2,\ldots,a^{23}\); the other side contains a scaled 266-by-266 Vandermonde submatrix. The first-266-column determinant has residues \(0\) and \(30\), hence global residue \(71815\) and gcd \(271\). Thus stacking shifts can separate an input.

**The P11 row/prefix obstruction.** For

\[
N=20000000499999937
=100000007\cdot199999991,
\qquad (A,r)=(2942,2953),
\]

write \(B=M_N[:,0:A]\). Exact reduction of the same global matrix gives

\[
\det B\equiv56136614\pmod {100000007},
\qquad
\det B\equiv132391112\pmod {199999991}.
\]

Both residues are nonzero. Consequently both complete row matroids are the free matroid \(U_{A,A}\), every row-prefix rank is \(s\), every full-row column-prefix rank is \(\min(t,A)\), and the lexicographically first column basis is \(0,\ldots,A-1\). The determinant's CRT lift is \(16315256998204520\), with gcd 1, and all \(8{,}687{,}726\) raw global entries are units. Equality of these invariants does not imply equality of the full column matroids.

**A full-column separator on the same matrix.** Put \(T=M_N[:,A:r]\) and, over either local field, \(W=B^{-1}T\). Remove base columns

\[
I=(423,2336)
\]

and add global tail columns \(2944,2948\), corresponding to tail offsets \(J=(2,6)\). For the selected columns in increasing global order, the exchange identity is

\[
\det M[:,S]
=(-1)^{3122}\det(B)\det W[I,J]
=\det(B)\det W[I,J].
\]

The normalized 2-by-2 determinants are \(67899852\) and \(0\), and direct dense evaluation of the exchanged local matrices independently gives

\[
\det M[:,S]\equiv15564403\pmod {100000007},
\qquad
\det M[:,S]\equiv0\pmod {199999991}.
\]

Therefore \(S\) is a basis in exactly one local column matroid. The determinant's global residue and gcd are

\[
2473353088699106\pmod N,
\qquad
\gcd(2473353088699106,N)=199999991.
\]

All \(2942\cdot11=32{,}362\) one-tail exchanges are bases in both fields. Among all

\[
\binom{2942}{2}\binom{11}{2}=237{,}941{,}605
\]

two-tail exchanges, the first field has no dependent set, the second has exactly two, and those are the only support mismatches. The second mismatch removes \(1618,1874\) and uses tail offsets \(3,10\). No claim is made about exchanges using three through eleven tail columns.

**Factor-free evaluation and scope.** Any specified minor here is globally evaluable without the factors. Binary exponentiation forms all rows using \(O(Ar^2\log N)\) naive ring operations, and Samuelson--Berkowitz evaluates an \(A\)-square determinant division-free in \(O(A^4)\) ring operations. Reducing after every operation keeps bit complexity polynomial in \(\log N\) whenever \(A,r=\operatorname{poly}(\log N)\). The local solves and CRT were discovery/certification devices; they are not needed to define the displayed global minor.

P24 refutes universal separation only for the joint row matroid and the named one-axis prefix, greedy-basis, raw-entry, and canonical-base-minor summaries. It simultaneously proves that the complete column-matroid refinement survives on this fixed coefficient-hard witness. It supplies neither a factor-free rule that selects successful parameters and minors on arbitrary composites nor a uniform theorem forcing a mismatch, so it is not a general factoring algorithm.

The candidate analyses, hostile audit, and proof-blind reconstruction are preserved under `experiments/F04_joint_matroid_kill`, `experiments/F04_full_column_matroid_kill`, `experiments/F04_joint_matroid_audit`, and `experiments/F04_joint_matroid_reconstruct`.
