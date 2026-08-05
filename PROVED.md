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
