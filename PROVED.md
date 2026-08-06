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

## P25 — uniform Hurwitz one-sided gcds have an \(N^{1/4}\) birthday scale

**Status:** promoted.

**Verification record:** the normalized order, local splittings, shell count, orbit parametrizations, left/right handedness, exact gcd and product laws, balanced asymptotic obstruction, fixed-transform qualifications, and ramified/repeated-prime exclusions passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

Let

\[
\mathcal H=\mathbb Z\left[i,j,\frac{1+i+j+k}{2}\right]
\]

be the Hurwitz order with quaternion conjugation, reduced trace, and reduced norm \(\operatorname{nrd}(a+bi+cj+dk)=a^2+b^2+c^2+d^2\). Let \(p\ne q\) be odd primes, \(N=pq\), and

\[
S_N=\{\alpha\in\mathcal H:\operatorname{nrd}(\alpha)=N\}.
\]

**Exact orientations.** For each \(r\in\{p,q\}\), an algebra splitting

\[
\mathcal H/r\mathcal H\simeq M_2(\mathbb F_r)
\]

exists. Every \(\alpha\in S_N\) reduces to a nonzero rank-one matrix: its determinant is zero, while zero reduction would force \(r^2\mid N\). Write \(R_r(\alpha)\) and \(I_r(\alpha)\) for its row and image lines.

The norm is Euclidean on both sides, so every one-sided ideal of \(\mathcal H\) is principal, and

\[
[\mathcal H:\mathcal H d]=[\mathcal H:d\mathcal H]
=\operatorname{nrd}(d)^2.
\]

For a projective line \(L\subset\mathbb F_r^2\), the matrices whose rows lie in \(L\) form a two-dimensional minimal left ideal. The CRT preimage of any pair of such ideals at \(p,q\) has index \(N^2\), hence is \(\mathcal H\alpha\) for an \(\alpha\) of norm \(N\). This gives a bijection

\[
\mathcal H^\times\backslash S_N
\simeq
\mathbf P^1(\mathbb F_p)\times\mathbf P^1(\mathbb F_q)
\]

for the free left-unit action and the row-line pair. The analogous right-unit quotient is parametrized by image-line pairs. Since \(|\mathcal H^\times|=24\),

\[
|S_N|=24(p+1)(q+1).
\]

Thus a uniform shell element has independent uniform local row lines, and separately independent uniform local image lines. This does not assert independence between the row and image line of the same sample.

**Exact one-sided gcd law.** A greatest common right divisor \(d_R\) is defined by

\[
\mathcal H\alpha+\mathcal H\beta=\mathcal H d_R;
\]

right divisors are controlled by row lines. A greatest common left divisor is defined by the corresponding sum of right ideals and is controlled by image lines. For iid uniform \(\alpha,\beta\in S_N\),

\[
\begin{array}{c|cccc}
\operatorname{nrd}(d_R)&1&p&q&N\\ \hline
\Pr&
\dfrac{pq}{(p+1)(q+1)}&
\dfrac{q}{(p+1)(q+1)}&
\dfrac{p}{(p+1)(q+1)}&
\dfrac1{(p+1)(q+1)}.
\end{array}
\]

The same table holds for \(d_L\). Indeed,

\[
r\mid\operatorname{nrd}(d_R)
\quad\Longleftrightarrow\quad
R_r(\alpha)=R_r(\beta),
\]

and the two local equality events are independent with probabilities \(1/(p+1)\) and \(1/(q+1)\). Squarefreeness restricts the norm to \(1,p,q,N\). A proper event therefore outputs the prime directly as the quaternion-gcd norm; an additional terminal integer gcd is not logically required.

For independent samples, the product test has the same law: local rank-one matrices satisfy \(AB=0\) exactly when \(\operatorname{im}(B)=\ker(A)\), again an equality of independent uniform projective lines.

**Birthday obstruction.** With \(K\) iid uniform samples, testing every pair in one handedness satisfies

\[
\Pr(\text{some proper one-sided gcd})
\le
\binom K2\frac{p+q}{(p+1)(q+1)}.
\]

On \(p<q<2p\), this is \(O(K^2/\sqrt N)\). Bertrand's postulate supplies infinitely many such pairs, so every \(K=\operatorname{poly}(\log N)\) has exponentially small success along an infinite balanced family. The exact occupancy law places constant collision mass at \(K=\Theta(N^{1/4})\); the necessary lower scale is \(\Omega(N^{1/4})\). Fixed local sums, intersections, inclusions, equalities, and ranks of the reduced minimal ideals depend only on the same equality partitions and do not evade this bound.

Fixed left/right transforms with norms coprime to \(N\) act by local projective bijections on independent sources and preserve the orientation law. For non-unit transforms, only \(\gcd(\operatorname{nrd}(d),N)\) has the displayed table in general, because multiplier primes may enter the full gcd norm. For two right transforms of one source, the relative action is \(B_1B_2^{-1}\); a nonscalar action has at most two fixed lines, while scalarity in exactly one component is already detected by the three trace-free quaternion coordinates. Self-conjugation similarly reduces to local trace zero. None of these statements covers sample-dependent nonlinear transforms.

**Scope.** Exact-uniform sampling is an idealized premise here, not a supplied algorithm. Finding one four-square representation does not prove a uniform draw from \(S_N\), and multiplying it by units stays inside one constant-size orbit. The theorem is restricted to distinct odd primes: the Hurwitz order is ramified at 2, and repeated-prime norms admit rank-zero reductions and deeper ideal types. P25 is evidence against iid uniform one-sided-gcd collisions and their fixed-menu equality refinements; it does not rule out a factor-free nonuniform sampler with asymmetric local collision energy, adaptive/nonlinear constructions, mixed invariants, or non-collision quaternion methods.

The candidate proof, corrected hostile audit with its exact \(N=15\) and \(N=2,6,9\) checks, and proof-blind reconstruction are preserved under `experiments/F15_hurwitz_gcd_kill`, `experiments/F15_hurwitz_gcd_audit`, and `experiments/F15_hurwitz_gcd_reconstruct`.

## P26 — bounded scaled Fermat and literal CRT wheels do not manufacture a fine factor-trace hint

**Status:** promoted.

**Verification record:** the trace-hint reduction, quantifier order, all multiplier allocations and parity cases, prime construction, AM--GM gap, local wheel count, and explicit-state/uniform-sampling scope passed a focused hostile audit and a proof-blind end-to-end reconstruction. The reconstruction additionally supplied exact counterexamples to broader wheel interpretations. No cross-family audit has run.

Let \(N=pq\), where \(p<q<2p\) are distinct odd primes, and let \(n=\lceil\log_2(N+1)\rceil\).

**A fine metric hint is sufficient.** If an explicitly represented \(h\) satisfies

\[
|h-(p+q)|\le B(n)
\]

for a fixed polynomial \(B\), enumerate the polynomially many integers \(t\) in that interval and square-test \(t^2-4N\). At \(t=p+q\), the discriminant is \((q-p)^2\); parity, multiplication, and nontriviality checks make every return correct. All operands have \(O(n)\) bits, so this is a deterministic polynomial-bit reduction. It does not construct the hint.

**Every fixed polynomial numerical multiplier range can fail.** Fix eventual positive polynomial bounds \(K(n),T(n)\). There are infinitely many balanced pairs with \(q/p\) arbitrarily close, at a chosen inverse-polylogarithmic scale, to \(\sqrt2\). The classical prime-number-theorem error term supplies the required prime \(q\) in an interval of width \(p/(\log p)^A\), with \(A\) chosen after \(K,T\).

For every \(k\le K(n)\), eventually \(\gcd(k,N)=1\). Any factor-revealing factorization \(XY=kN\) allocates the two unknown primes oppositely, so after relabeling

\[
X=cp,\qquad Y=dq,\qquad cd=k,qquad c,d\le K(n),
\]

or the swapped orientation. Bad approximation to \(\sqrt2\) gives

\[
|X-Y|>\frac{p}{6K(n)}.
\]

The exact scaled-Fermat gap is

\[
\frac{X+Y}{2}-\sqrt{kN}
=\frac{(X-Y)^2}{2(\sqrt X+\sqrt Y)^2}
>\frac{p}{432K(n)^3}.
\]

This exceeds \(T(n)+1\) for all sufficiently large members of the family. The proof covers every divisor allocation; parity only removes impossible allocations. A found factor of \(kN\) reveals \(p\) or \(q\) through its gcd with \(N\), rather than necessarily being a factor of \(N\) itself. The family may depend on the fixed \(K,T\); the theorem does not cover polynomially many binary-encoded multipliers of exponential numerical magnitude.

**Literal square-residue wheels remain large.** For an odd auxiliary prime \(\ell\nmid N\), let

\[
W_\ell(N)=\{t\bmod\ell:t^2-4N\text{ is a square modulo }\ell\}.
\]

The map \(x\mapsto x+Nx^{-1}\) on \(\mathbb F_\ell^\times\) has fibers given by the involution \(x\mapsto N/x\), hence

\[
|W_\ell(N)|=\frac{\ell+(N/\ell)}2.
\]

For a squarefree product \(m\) of \(k\) distinct such primes, CRT gives

\[
|W_m(N)|=\prod_{\ell\mid m}\frac{\ell+(N/\ell)}2
\ge\frac{m}{3^k}=m^{1-o(1)}.
\]

Let \(L=\Theta(\sqrt N)\) be the number of integers in the public balanced trace interval. If \(m\ge L\), literal wheel materialization and unconditioned uniform sampling require \(L^{1-o(1)}\) states or expected trials. If \(m\le L\), explicitly visiting every accepted lift requires \(L^{1-o(1)}\) candidates. These are exponential in \(n\).

The regime qualifications are essential. A fixed small \(m\) has only constantly many materialized states, while an enormous factor-aware tailored product can reject every false interval trace and leave one lift. Thus P26 is only an explicit-state, explicit-lift, and unconditioned-uniform-sampling obstruction. It is not a lower bound against compressed character solvers, adaptive auxiliary primes, biased or interval-conditioned generation, or another way for bare \(N\) to manufacture metric information.

The candidate, hostile audit, and proof-blind reconstruction are preserved under `experiments/F18_metric_hint_kill`, `experiments/F18_metric_hint_audit`, and `experiments/F18_metric_hint_reconstruct`.

## P27 — exact-uniform imaginary-class ambiguity hunting has an exponential class-number barrier

**Status:** promoted.

**Verification record:** the form/class distinction, complete ambiguous-form lists, primitivity and extraction identities, direct and collision laws, inverse-orbit qualification, class-number asymptotic, public genus character, displayed powers, split-prime root count, and bit-complexity scope passed a focused hostile audit and a proof-blind reconstruction. No cross-family audit has run.

Let \(N=pq\) with distinct odd primes \(p<q\), and use the fundamental discriminant

\[
\Delta=\begin{cases}-N,&N\equiv3\pmod4,\\-4N,&N\equiv1\pmod4.\end{cases}
\]

Write \(G=\operatorname{Cl}(\Delta)\), \(h=|G|\), \(T=G[2]\), and \(t=|T|\). A canonical reduced primitive positive form \([a,b,c]\) represents a class fixed by inversion exactly when

\[
b=0,\qquad b=a,\qquad\text{or}\qquad a=c.
\]

**Complete ambiguity classification.** If \(\Delta=-N\), then \(t=2\). Besides the principal form

\[
[1,1,(N+1)/4],
\]

there is exactly one useful ambiguous form:

\[
\begin{cases}
[p,p,(p+q)/4],&q>3p,\\
[(p+q)/4,(q-p)/2,(p+q)/4],&q<3p.
\end{cases}
\]

If \(\Delta=-4N\), then \(t=4\). The complete list is

\[
[1,0,N],\quad [2,2,(N+1)/2],\quad [p,0,q],
\]

and

\[
\begin{cases}
[2p,2p,(p+q)/2],&q>3p,\\
[(p+q)/2,q-p,(p+q)/2],&q<3p.
\end{cases}
\]

The first two even-discriminant forms are useless; \([2,2,(N+1)/2]\) is a public nonprincipal decoy. The other two expose \(p,q\). Extraction uses

\[
N=ac,\qquad
N=(a/2)(2c-a/2),\qquad
N=(a-b/2)(a+b/2)
\]

in the three boundary cases. Equality \(q=3p\) is impossible for distinct primes. In either discriminant branch, the useless classes form an index-two subgroup \(T_0\le T\), and the useful classes are its other coset.

**Exact iid-uniform laws.** Grant independent exact-uniform classes of \(G\); this is an oracle premise, not a supplied sampler. One direct sample is useful with probability

\[
\frac{t}{2h},
\]

so its expected stopping count is \(2h/t\). An ordinary collision modulo inversion is redundant but not always empty: it can reveal \(X^2\), with exact useful probability

\[
\Pr(X^2\text{ useful})=\frac{t\,|(T\setminus T_0)\cap G^2|}{h}
\le\frac{t^2}{2h}.
\]

Thus \(4\)-torsion must not be discarded.

For square collisions \(X_i^2=X_j^2\), a specified pair has a useful quotient with probability \(t/(2h)\). Put \(H=h/t\). Each square fiber is a \(T\)-coset split into two \(T_0\)-halves, so after \(m\) samples the exact success probability is

\[
1-\frac1{(2H)^m}
\sum_{k=0}^{\min(m,H)}
\binom Hk2^k k!S(m,k).
\]

The expected and constant-success sample scale is \(\Theta(\sqrt H)\). Canonical form arithmetic only contributes polynomial factors in \(\log|\Delta|\); it does not repair the sample count.

**Unconditional asymptotic barrier.** The analytic class-number formula and Siegel's theorem give, for every fixed \(\varepsilon>0\),

\[
h(\Delta)\ge c_\varepsilon|\Delta|^{1/2-\varepsilon},
\]

with an ineffective positive constant. Taking \(\varepsilon=1/4\) proves that every fixed polynomial number of exact-iid direct samples or square-collision pairs has success \(2^{-\Omega(\log N)}\). Prime number theory in fixed residue classes supplies infinite balanced families in both discriminant branches. This says nothing about an unspecified “near-uniform” or deliberately biased distribution.

**Genus and powering qualifications.** For \(\Delta=-4N=(-4)N\), the public factorization of the discriminant gives a factor-free genus character

\[
\chi_{-4}=\chi_N.
\]

Thus it is false that every individual genus character needs \(p\) or \(q\). Nevertheless, there are exactly \(t\le4\) genera of size \(h/t\), so even free complete genus labels and exact uniform sampling from a chosen genus increase useful mass by at most the constant factor \(t\). The aggregate identity \((\Delta/r)=1\) for a primitively represented \(r\) is only the product relation among constituent characters.

If \(\lambda(G)=2^am\) with \(m\) odd, \(X^{\lambda(G)/2}\) is uniform on \(T\) when \(t=2\). When \(t=4\) and the Sylow subgroup is \(C_{2^a}\times C_{2^b}\), it is uniform on \(T\) if \(a=b\), and on an order-two subgroup—possibly the decoy direction—if \(a>b\). The different power \(X^{h/2}\) is uniform on \(T\) for \(t=2\) and identically the identity for \(t=4\). These statements analyze only the displayed powers; they assume unavailable class exponent or order data and do not prove such data necessary for every powering rule.

For a supplied split prime \(\ell\nmid\Delta\), the congruence \(b^2\equiv\Delta\pmod{4\ell}\) has four literal roots modulo \(4\ell\), two classes modulo \(2\ell\), and the two signs give inverse form classes. Constructing and reducing those forms is polynomial in \(\log|\Delta|+\log\ell\), but choosing signs or auxiliary primes does not yield exact-uniform class samples without a separate distribution theorem.

The candidate, corrected hostile audit and retained finite checks, and proof-blind reconstruction are preserved under `experiments/F17_classgroup_ambiguity_kill`, `experiments/F17_classgroup_ambiguity_audit`, and `experiments/F17_classgroup_ambiguity_reconstruct`.

## P28 — the Lipschitz Hurwitz slice is orientation-uniform, while a single unit orbit has an exact stabilizer criterion

**Status:** promoted.

**Verification record:** the two-handed unit-orbit count, projective-fibre theorem, exact rejection sampler including zero last coordinate, random-bit and bit-complexity bounds, memoryless and transcript-dependent finite-menu bounds, actual-unit quotient and handedness, characteristic-\(3\) faithfulness, Euclidean-gcd cost, and the \(N=15,39\) certificates passed a corrected hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

Let

\[
\mathcal H=\mathbb Z^4\sqcup(\mathbb Z+\tfrac12)^4
\]

be the Hurwitz order, let \(N=pq\) for distinct odd primes, and let

\[
L_N=\{a+bi+cj+dk\in\mathbb Z^4:a^2+b^2+c^2+d^2=N\}.
\]

**A strict coordinate slice does not bias either projective quotient.** Every left- and every right-unit orbit of odd norm contains exactly eight elements of \(L_N\). If an orbit contains an integral element, precisely the eight Lipschitz units preserve integrality. If it contains an all-half-integral element, a signed-sum parity argument shows that exactly eight half units send it into the integral coset. Consequently

\[
|L_N|=8(p+1)(q+1),
\]

and a uniform element of \(L_N\) has independent uniform row lines in
\(\mathbf P^1(\mathbb F_p)\times\mathbf P^1(\mathbb F_q)\); separately, its image lines have the same law. This does not assert independence between the row and image of one element. Thus iid samples have the same one-sided-gcd law as P25, and \(K\) all-pairs tests have proper-right-gcd probability at most

\[
{K\choose2}\frac{p+q}{(p+1)(q+1)}.
\]

**The direct exact sampler is exponentially slow in input length.** Put \(B=\lfloor\sqrt N\rfloor\) and \(M=2B+1\). Draw \(a,b,c\) uniformly from \([-B,B]\), square-test \(N-a^2-b^2-c^2\), and choose one of the two signs of the fourth coordinate; when that coordinate is zero, accept on only one value of the sign bit. Every element of \(L_N\) is emitted per outer trial with probability \(1/(2M^3)\). Hence the expected number of trials is

\[
\frac{M^3}{4(p+1)(q+1)}=\Theta(\sqrt N)
\]

on balanced semiprimes. Exact interval draws use \(\Theta(\sqrt N\log N)\) expected random bits in total, and the expected bit cost is
\(\sqrt N\operatorname{polylog}N\). The sampler terminates almost surely but is not polynomial in \(\log N\).

**Polynomial fixed transform menus do not repair the distribution.** Suppose a menu \(\mathcal T\) of \(C\) transforms sends, at each local prime, the input row or image line through a fixed projective bijection. This includes the unit/conjugation maps used in the candidate. A memoryless sample-dependent selector has every output-line atom at most \(C/(r+1)\), and two independently selected outputs collide with probability at most

\[
\min\!\left(1,\frac C{r+1}\right).
\]

Even if a joint or stateful selector inspects all \(K\) iid raw samples before choosing their transforms, one specified selected pair collides locally with probability at most

\[
\min\!\left(1,\frac{C^2}{r+1}\right).
\]

A union bound over pairs and \(r=p,q\) is exponentially small on balanced inputs for \(C,K=\operatorname{poly}(\log N)\). This theorem does not cover a transform that combines samples, an exponential menu, or an unrestricted nonlinear construction.

**One right-unit orbit has a constant-success criterion.** Fix a norm-\(N\) element \(\alpha\in\mathcal H\). Draw actual units \(U_1,U_2\) independently and uniformly from the 24 Hurwitz units, set \(Y_i=\alpha U_i\), and write

\[
G=\mathcal H^\times/\{\pm1\}\simeq A_4,
\qquad
H_r(\alpha)=\operatorname{Stab}_G(R_r(\alpha)).
\]

The relative projective unit is uniform on the 12 elements of \(G\), so row equality at \(r\) is membership in \(H_r(\alpha)\). Therefore

\[
\Pr\!\left(1<\operatorname{nrd}\operatorname{gcrd}_R(Y_1,Y_2)<N\right)
=\frac{|H_p(\alpha)\triangle H_q(\alpha)|}{12}.
\]

The projective \(A_4\)-action is faithful for every odd prime, including \(3\), and at most 22 projective lines have nontrivial stabilizer; this bounded-exception statement does not promise a trivial-stabilizer line in small characteristic. If \(H_p(\alpha)\ne H_q(\alpha)\), repetition gives a conditional Las Vegas splitter with at most 12 unit pairs in expectation. Hurwitz nearest-lattice Euclidean division contracts the norm by a constant factor, so the one-sided gcd and its reduced norm cost \(\operatorname{poly}(\log N)\) bits. On success that norm itself is \(p\) or \(q\); an integer gcd is optional verification, not the source of the separation.

The condition is not pointwise. For

\[
N=15,\qquad \alpha=1+i+2j+3k,
\]

the stabilizers have symmetric difference of size \(3\), giving success \(1/4\). For

\[
N=39,\qquad \alpha=1+i+j+6k,
\]

they are the same order-\(3\) subgroup, giving success \(0\). No factor-free expected-polynomial method is known for finding a mismatch-stratum \(\alpha\) with inverse-polynomial probability. Thus the exact conditional extractor is not a top-level factoring algorithm.

The candidate, corrected hostile audit and complete finite scan, and proof-blind reconstruction are preserved under `experiments/F15_hurwitz_bias_kill`, `experiments/F15_hurwitz_bias_audit`, and `experiments/F15_hurwitz_bias_reconstruct`.

## P29 — the fixed level-two Eisenstein metric coefficient is a semiprime divisor-sum oracle

**Status:** promoted.

**Verification record:** modularity and both cusps, the Fourier coefficients, arithmetic Hecke normalization, exact promise identity, all three oracle interfaces, decoding and bit lengths, converse computation, and the repeated/even counterexamples passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

Define

\[
F(z)=2E_2(2z)-E_2(z)
=1+24\sum_{m\ge1}b_mq^m.
\]

The quasimodular anomalies in the two \(E_2\) terms cancel on \(\Gamma_0(2)\). At the non-infinity cusp,

\[
(F|_2S)(z)=\frac12E_2(z/2)-E_2(z),
\]

which has no negative powers of the width-two parameter \(e^{\pi iz}\). Hence

\[
F\in M_2(\Gamma_0(2)).
\]

Direct coefficient subtraction gives

\[
b_m=\sigma_1(m)-2\mathbf1_{2\mid m}\sigma_1(m/2)
=\sigma_1(m_{\rm odd}).
\]

The space \(M_2(\Gamma_0(2))\) is one-dimensional. For odd \(m\), under the standard arithmetic weight-two Hecke normalization,

\[
T_m(F/24)=b_m(F/24).
\]

A unitary normalization instead rescales the eigenvalue by \(m^{-1/2}\).

**Exact factor-trace identity.** If

\[
N=pq
\]

for distinct odd primes, with no balance assumption, then

\[
b_N=\sigma_1(N)=(p+1)(q+1)=N+p+q+1.
\]

Thus \(s=b_N-N-1=p+q\), and

\[
D=s^2-4N=(q-p)^2.
\]

Exact integer square root, parity, nontriviality, ordering, and product checks recover and verify \(p,q\). This terminal extraction uses no gcd.

**Three precise high-information interfaces suffice.** Let

\[
n=\lceil\log_2(N+1)\rceil,\qquad M=2^n.
\]

Each of the following fixed uniform worst-case polynomial-time interfaces gives a deterministic one-call polynomial-bit factorization of every promised \(N\):

1. exact \(b_N\), the exact arithmetic Hecke eigenvalue, or the exact unnormalized coefficient \(24b_N\);
2. \(24b_N\bmod Q\) for arbitrary caller-supplied \(O(n)\)-bit \(Q\); choose

   \[
   Q=24M.
   \]

   Divide the canonical least residue by \(24\) to obtain \(b_N\bmod M\), then reduce \(b_N-(N+1)\) modulo \(M\). Since

   \[
   0<p+q<N+1\le M,
   \]

   its least residue is the ordinary integer \(p+q\);
3. an exactly encoded integer \(h\) satisfying \(|h-b_N|\le K(n)\) for an explicit known numerical polynomial \(K\). Enumerate the polynomial-width interval for \(p+q\), apply the discriminant decoder to every candidate, and return only a verified product.

All exact answers and intermediate values have \(O(n)\) bits; the modular choice has \(n+5\) bits; integer square root and the polynomial scan have deterministic polynomial bit complexity. An unspecified floating-point approximation, unknown polynomial, relative error, fixed small modulus, or nonuniform oracle is not covered.

**Converse and exact scope.** A supplied complete factorization of arbitrary \(m\) computes

\[
b_m
=\prod_{\ell^e\parallel m_{\rm odd}}
(1+\ell+\cdots+\ell^e)
\]

and therefore every displayed output in polynomial bit complexity. Mutual polynomial-time reducibility is proved only for the distinct-odd-semiprime promise. It is false under broader semiprime wording:

\[
b_9=13\ne9+3+3+1,
\qquad
b_6=\sigma_1(3)=4\ne6+2+3+1.
\]

This theorem is exactly the familiar divisor-sum trace identity packaged in a fixed Eisenstein series. It does not construct any coefficient evaluator, factor arbitrary integers, or prove a lower bound. It says nothing adverse about cusp forms, character twists, other levels or weights, fixed-small-modulus or coarse data, low-index Hecke data, Brandt or modular-symbol invariants, or any automorphic invariant with a genuinely different information path.

The candidate, corrected hostile audit, and proof-blind reconstruction are preserved under `experiments/F19_hecke_metric_kill`, `experiments/F19_hecke_metric_audit`, and `experiments/F19_hecke_metric_reconstruct`.

## P30 — a residual-only four-square finder is exactly diffuse in both matched handednesses

**Status:** promoted.

**Verification record:** the residual-fibre law, both exceptional-point bijections, the primitive one-sided-gcd lemma, handed normalization, collision and unit-orbit bounds, characteristic-\(3\) faithfulness and exact exceptional counts, the precise Pollack--Treviño interface, and expected bit and random-bit complexity passed a focused hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

Let \(n=pq\) for distinct odd primes, and let \(M\) be an odd squarefree multiple of \(n\). Draw \(x,y\) exactly uniformly modulo \(M\), put

\[
R=-x^2-y^2\pmod M,
\]

and suppose that acceptance and completion inspect \((x,y)\) only through \(R\) and fresh randomness. Assume every accepted \(R\) is a unit, completion gives \(z,w\) with

\[
z^2+w^2\equiv R\pmod M,
\]

and \(\beta=x+yi+zj+wk\) is primitive.

Fix \(r\in\{p,q\}\), write \(\chi_r=(-1/r)\), and define

\[
\mathcal S_r=
\{[u:v]\in\mathbf P^1(\mathbf F_r):u^2+v^2\ne0\},
\qquad |\mathcal S_r|=r-\chi_r.
\]

Conditional on the accepted residual and the completion randomness, the row line and, separately, the image line of \(\beta\bmod r\) are exactly uniform on \(\mathcal S_r\).

**Exact local bijections.** Choose \(s,t\in\mathbf F_r\) with \(s^2+t^2=-1\), split the Hurwitz algebra by

\[
i\mapsto
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
j\mapsto
\begin{pmatrix}s&t\\t&-s\end{pmatrix},
\]

and put \(A=zs+wt\), \(B=zt-ws\). Then

\[
\beta_r=
\begin{pmatrix}
x+A&y+B\\
-y+B&x-A
\end{pmatrix},
\qquad A^2+B^2=-(z^2+w^2).
\]

The nonzero conic \(x^2+y^2=-(z^2+w^2)\) maps bijectively to \(\mathcal S_r\) through its row line and also through its image line. For rows, the usual first-row formula misses exactly \([-B:A]\), supplied by the point \((-A,-B)\) where that row vanishes. For images, the first-column formula misses the same line, supplied by \((-A,B)\). This proves exact uniformity, not merely a character-count estimate. It does not assert independence between the row and image of one matrix.

**Matched handedness.** A greatest common right divisor \(D_R\) of \(n\) and \(\beta\) has norm \(n\). Its generator is ambiguous by a left unit; normalize on the left, preserving its local row lines. A separately computed greatest common left divisor \(D_L\) also has norm \(n\); normalize on the right, preserving its image lines. Consequently, two independent right-gcd outputs have local right-gcd collision probability

\[
\Pr(\operatorname{row}_r(D_1)=\operatorname{row}_r(D_2))
=\frac1{r-\chi_r},
\]

and the same formula holds for the image lines of two independently computed left-gcd outputs tested by a left gcd. No independence between the \(p\)- and \(q\)-events is needed. With \(K\) calls, every-pair proper-divisor probability in either matched hand is at most

\[
\binom K2
\left(
\frac1{p-\chi_p}+\frac1{q-\chi_q}
\right).
\]

Testing both matched hands and every fixed projective Hurwitz-unit class changes this only by an absolute constant.

For a single right-gcd output, all right-unit pairs succeed exactly on a mismatch of the two row stabilizers in \(G=\mathcal H^\times/\{\pm1\}\cong A_4\). The projective action is faithful for every odd \(r\), including \(3\), and the number \(e_r\) of supported lines with nontrivial stabilizer is

\[
e_3=4,
\qquad
e_r=4\mathbf1_{(-1/r)=1}+8\mathbf1_{(-3/r)=1}
\quad(r\ge5).
\]

Thus

\[
\Pr(H_p\ne H_q)
\le
\frac{e_p}{p-\chi_p}+\frac{e_q}{q-\chi_q}
=O(1/p+1/q),
\]

with the dual statement for a separately computed left-gcd output and left units.

**The unconditional arithmetic source fits exactly.** After its preprocessing, the Pollack--Treviño four-square algorithm uses

\[
P=\prod_{\substack{\ell\le\log n\\\ell\equiv3\pmod4}}\ell,
\qquad
M=\frac{nP}{\gcd(n,P)}=\operatorname{lcm}(n,P),
\]

which is an odd squarefree multiple of the reduced distinct-prime semiprime. Its acceptance, modular square-root test, Gaussian gcd, and completion depend on \((x,y)\) only through \(R\) and fresh randomness; its output is primitive. Exact rejection sampling costs \(O(\log n)\) expected random bits per trial, and the source success bound gives \(O(\log n/\log\log n)\) trials. A crude fixed polynomial bounds the expected bit cost, with \(O(\log n)\)-bit intermediates.

Along an infinite balanced family \(p<q<2p\), every fixed polynomial number of independent calls, all pair tests in both matched hands, all fixed unit classes, and all within-output unit-orbit tests therefore have success

\[
2^{-\frac12\log_2 n+O(\log\log n)}.
\]

This does not control the image of a left-normalized right-gcd output, the row of a right-normalized left-gcd output, mixed-handed comparisons, sample-dependent nonlinear combinations, even or repeated-prime norms, completions that inspect the particular fibre point, or non-collision quaternion invariants.

The candidate, corrected hostile audit, and proof-blind reconstruction are preserved under `experiments/F20_four_square_fibre_kill`, `experiments/F20_four_square_fibre_audit`, and `experiments/F20_four_square_fibre_reconstruct`.

## P31 — mixed-handed four-square comparisons stay sparse independently, while the same-source graph survives

**Status:** promoted.

**Verification record:** conditional CRT product-uniformity, arbitrary transcript-dependent normalization, the exact constants \(12,27,378\), every independent comparison hand and both product orders, the total raw row--image graph, both split-free cross-hand criteria, the complete \(N=91\) certificate, and the two-or-four pooled-span theorem passed a corrected hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

Retain P30's notation. Thus \(N=pq\) for distinct odd primes, the four-square source is residual-only, and for

\[
s_r=r-\left(\frac{-1}{r}\right),
\qquad
\mathcal S_r=\{[u:v]:u^2+v^2\ne0\},
\]

the local row line and, separately, the local image line of a raw output \(\beta\) are uniform on \(\mathcal S_r\).

**The CRT law is a product law.** Conditional on any positive-probability accepted residual and all completion randomness,

\[
(\operatorname{row}_p\beta,\operatorname{row}_q\beta)
\quad\text{is uniform on }\mathcal S_p\times\mathcal S_q,
\]

and the image pair is separately uniform on the same product. This does not make the row and image of one \(\beta\) independent.

Let \(D_R\) be a greatest common right divisor of \(N\) and \(\beta\), normalized on the left by an arbitrary function of its entire call transcript. If \(r'\) is the other prime, then every local image atom obeys

\[
\Pr(\operatorname{im}_rD_R=L)
\le
\min\left(1,\frac{12(r'+1)}{s_rs_{r'}}\right)
\le
\min\left(1,\frac{27}{r+1}\right).
\]

Dually, if \(D_L\) is a separately computed greatest common left divisor with arbitrary transcript-dependent right normalization, every atom of \(\operatorname{row}_rD_L\) obeys the same bound. The incidence proof counts the full 12 projective unit classes; it assumes no canonical Euclidean-algorithm normalization.

**All independent direct comparisons remain rare.** For two independent finder calls, a one-sided gcd in either hand between any choices from \(\{D_R,D_L\}\), or either product-zero test \(AB=0\) and \(BA=0\), reduces locally to equality of two projective lines, at least one of which has atom at most \(27/(r+1)\). Hence one fixed comparison has proper-outcome probability at most

\[
27\left(\frac1{p+1}+\frac1{q+1}\right).
\]

A predetermined menu of \(T\) fixed projective transforms and all pairs among \(K\) independent outputs add only the explicit union factor \(K^2T\). On an infinite balanced family \(p<q<2p\), polynomial \(K,T\) therefore give

\[
2^{-\frac12\log_2N+O(\log\log N)}
\]

success. A joint rule that chooses normalizations or combinations after seeing several calls is not covered.

For one wrong-handed output, the projective Hurwitz-unit group \(G\simeq A_4\) has at most 14 exceptional projective lines with nontrivial stabilizer in every odd characteristic. Thus the complete twelve-unit wrong-hand stabilizer menu is bounded by

\[
378\left(\frac1{p+1}+\frac1{q+1}\right),
\]

with the dual statement for \(D_L\).

**The raw same-source dependence is exact.** Write \(C=zj+wk\). In a local split put

\[
J_{C,r}=
\begin{pmatrix}A&B\\B&-A\end{pmatrix},
\qquad
J_{C,r}^2=-(z^2+w^2)I.
\]

The accepted residual makes this scalar a unit, and at every supported point, including both exceptional descriptions,

\[
\operatorname{im}_r\beta
=J_{C,r}\operatorname{row}_r\beta.
\]

Consequently the two same-source cross hands admit the exact split-free tests

\[
\operatorname{row}_r(D_LU)=\operatorname{row}_r\beta
\iff
2[i](\bar C D_LU)\equiv0\pmod r,
\]

and

\[
\operatorname{im}_r(UD_R)=\operatorname{im}_r\beta
\iff
2[i](\bar CUD_R)\equiv0\pmod r.
\]

Changing the allowed normalization only permutes the full twelve-class menu.

These criteria have no pointwise guarantee. For

\[
N=91,\quad M=273,\quad \beta=172+82i+k,
\]

one may take

\[
D_R=\frac{-19+i+j+k}{2},
\qquad
D_L=\frac{-19+i-j+k}{2}.
\]

Both have norm 91 and satisfy the required right/left factorizations. In one fixed projective-unit order, the two complete coefficient menus are

\[
(-1,1,-19,-1,9,8,-10,-11,10,9,-9,-10)
\]

and

\[
(1,-1,-19,1,10,11,-9,-8,9,10,-10,-9).
\]

Every entry is coprime to 91. This finite certificate refutes only a universal twelve-unit guarantee; it has no asymptotic force.

**A narrow linear pool also collapses to equality.** Put

\[
Q_t=\bar C_tD_{L,t},
\qquad
L_{t,r}=\operatorname{row}_r\beta_t.
\]

Then \(\operatorname{im}_rQ_t=L_{t,r}\) and

\[
Q_tM_2(\mathbf F_r)
=\{X:\operatorname{im}X\subseteq L_{t,r}\}
\]

is a two-dimensional right ideal. The pooled span for a nonempty subset has dimension two exactly when all its \(L_{t,r}\) coincide, and dimension four otherwise; dimension three never occurs. Therefore every fixed polynomial family of dimension-only subset profiles is just a polynomial union of equality/birthday events.

This theorem does **not** cover adaptive or implicit subset selection, exact row spaces rather than their dimensions, coefficient/pivot/minor systems, resultants, noncommutative products, spectral or discrepancy statistics, nonlinear joint decoders, or a completion biased by the actual fibre point. Amortizing many coupled nonzero constraints is not refuted by the independent-ticket bounds.

The candidate, corrected hostile audit and finite certificate, and proof-blind reconstruction are preserved under `experiments/F21_mixed_handed_four_square_kill`, `experiments/F21_mixed_handed_four_square_audit`, and `experiments/F21_mixed_handed_four_square_reconstruct`.

## P32 — one complete real-infrastructure endpoint cycle can carry no single-endpoint factor hint

**Status:** promoted.

**Verification record:** the exact continued fraction, complete proper-form cycle, list/queue square classification with sign and counter-parity qualifications, repeated-factor audit, endpoint-only obstruction, infrastructure distance and reduction corrections, compact encodings, Terr bounds, regulator, exact published caps, and heuristic scope passed a corrected hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

For \(t\ge1\), set

\[
a=6t+1,
\qquad
N=a^2+2,
\qquad
\Delta=4N.
\]

Then \(N\) is odd and nonsquare, and

\[
N=3(12t^2+4t+1).
\]

Thus the family has the public nontrivial divisor 3 and is not a hard factoring family. It is also not uniformly squarefree: \(t=1\) gives \(51=3\cdot17\), \(t=3\) gives \(363=3\cdot11^2\), and \(t\equiv2\pmod3\) has \(9\mid N\).

The continued fraction and the complete reduced proper principal cycle in the Gower--Wagstaff \(\rho\) convention are

\[
\sqrt N=[a;\overline{a,2a}],
\qquad
(1,2a,-2)\xleftrightarrow{\rho}(-2,2a,1).
\]

Every endpoint coefficient is coprime to \(N\). The only oriented positive right square coefficient is \(1\). It is already present in the sufficient list/queue and is the improper period-completion square, so the unmultiplied cycle contains no proper SQUFOF square.

The sign and parity wording is essential. The negative coefficient \(-2\) cannot be replaced by its absolute value, and the two published pseudocode presentations have a local counter/index mismatch. In the invariant positive-right-end convention, \(C=1\) is tested and rejected as period completion; on the completely literal branch that skips that occurrence, no square is extracted. Neither reading produces a proper square.

Therefore the following deliberately restricted observation model never exposes a factor: traverse or jump within this fixed unmultiplied principal infrastructure, discard every composition/reduction transcript, retain only the reduced endpoint, and apply only a coefficient gcd or the standard single-endpoint proper-square localization. The result says nothing about the public factor, multipliers, another discriminant, intermediate coefficients, reduction failures, relative generators, power products, or joint decoders.

**The metric itself is small and exact.** The fundamental unit of \(\mathbf Z[\sqrt N]\) is

\[
\varepsilon=(N-1)+a\sqrt N,
\qquad
R=\log\varepsilon=\Theta(\log N).
\]

The two reduced principal endpoints lie at distances \(0\) and \(R/2\). Distance is injective on normalized reduced principal ideals, but composition adds distances only after retaining the reduction multiplier/correction. Neighbor gaps satisfy

\[
\frac1{\sqrt\Delta}<\delta_i<\frac12\log\Delta,
\qquad
\delta_i+\delta_{i+1}>\log2.
\]

Thus resolving an exact endpoint requires \(\frac12\log_2\Delta+O(1)\) fractional bits, and \(K\) approximate doublings require \(K+O(\log\Delta)\) guard bits. Compact power products can encode huge generators without expansion.

Buchmann--Vollmer's named Terr algorithms have bit-time and bit-space upper bound

\[
O\left((\log\Delta+\sqrt R)(\log\Delta)^2\right).
\]

The term is the square root of the numeric regulator, and this is an algorithmic upper bound, not a lower bound. On this explicit family it is \(O((\log N)^3)\).

The exact Gower--Wagstaff cap parameters are of order \(N^{1/4}\), but their body-pass counts depend on the published indexing convention. Their complexity theorems use explicit squarefree, distribution, random-walk, spacing, queue-density, and multiplier assumptions and are asymptotic averages, not per-input Las Vegas bounds. A cap is not a lower bound.

Accordingly, P32 closes only unmultiplied endpoint-only single-form localization. Full transcripts, multipliers, relative generators, failure-event decoders, adaptive distance computations, and every general infrastructure/factoring possibility remain open.

The candidate, corrected hostile audit, and proof-blind reconstruction are preserved under `experiments/F22_real_infrastructure_metric_kill`, `experiments/F22_real_infrastructure_metric_audit`, and `experiments/F22_real_infrastructure_metric_reconstruct`.

## P33 — an exposed selective two-isogeny kernel is semiprime factoring, but its coarse neighbor is not

**Status:** promoted.

**Verification record:** the modular-polynomial specializations and collision primes, Vélu quotients and invariants, the rank-two étale subgroup/section equivalence, both gcd directions, the exact semiprime promise reduction and bit complexity, the \(N=143\) certificate and all power identities, and the narrow irreducibility/discriminant/CM boundaries passed a corrected hostile audit and a proof-blind end-to-end reconstruction. No cross-family audit has run.

In the classical symmetric normalization,

\[
\Phi_2(0,Y)=(Y-54000)^3,
\]

\[
\Phi_2(1728,Y)=(Y-1728)(Y-287496)^2,
\]

and

\[
\Phi_3(0,Y)=Y(Y+12288000)^3.
\]

The level-two roots at 1728 collide exactly in characteristics \(2,3,7\); the level-three roots at 0 collide in \(2,3,5\); and the source/target pair \(0,54000\) collides in \(2,3,5\).

Let

\[
E_A:y^2=x^3+Ax
\]

over an odd base with \(A\) a unit. The public kernel generated by \((0,0)\) has quotient \(j=1728\). If \(s^2=-A\), either nonpublic kernel generated by \((\pm s,0)\) has quotient \(j=287496\). Nevertheless, if \(-A\) is a nonsquare over a finite field, Frobenius exchanges those two geometric points and neither nonpublic order-two subgroup descends from the fixed twist, even though the double coarse root \(287496\) is rational. A coarse modular-polynomial root is therefore weaker than a descended selective kernel.

Now let \(N=pq\) with distinct odd primes and assume

\[
A\in(\mathbf Z/N\mathbf Z)^\times,
\qquad
\left(\frac{-A}{N}\right)=-1.
\]

A finite étale rank-two subgroup \(C\subset E_A[2]\) whose reduction differs from the public subgroup in at least one CRT component, represented so that its unique nonidentity section is recoverable, is exactly a residue \(u\) satisfying

\[
u(u^2+A)\equiv0\pmod N,
\qquad
u\not\equiv0\pmod N.
\]

Exactly one CRT component admits \(u^2=-A\). Thus every valid output is mixed and

\[
\{\gcd(u,N),\gcd(u^2+A,N)\}=\{p,q\}.
\]

Conversely, known factors construct the mixed \(u\) by taking a verified square root on the residue component, zero on the other, and applying CRT. Hence the exposed fine-kernel task and factorization are polynomial-time equivalent on this promise.

Uniformly random \(A\bmod N\) reaches the unit Jacobi-minus-one promise with exact raw probability

\[
\frac{(p-1)(q-1)}{2pq}\ge\frac4{15}.
\]

Exact rejection sampling uses \(O(\log N)\) expected random bits. Promise tests, output verification, both gcds, and CRT have polynomial bit cost, so a uniform expected-polynomial fine-kernel solver gives a Las Vegas expected-polynomial factorization of every distinct odd semiprime. This is not a reduction for even, repeated-prime, prime-power, or multifactor inputs.

For the exact good-prime certificate

\[
N=143=11\cdot13,
\qquad A=1,
\qquad u=44,
\]

one has

\[
\gcd(44,143)=11,
\qquad
\gcd(44^2+1,143)=13.
\]

The mixed quotient has \(j=1\). The pure coarse residue \(66\) also exists, illustrating that a coarse root alone need not select the descended nonpublic component.

In \(\mathbf F_r[T]/(T^2+1)\), for every \(i\ge1\),

\[
T^{143^i}-T=
\begin{cases}
-2T,&i\text{ odd},\\
0,&i\text{ even},
\end{cases}
\]

at both \(r=11\) and \(r=13\). The true local Frobenius values are instead \(-2T\) and \(0\), respectively. Global \(N^i\)-powers synchronize and do not reproduce the selective local map.

For fixed \(\ell\), irreducibility of \(\Phi_\ell\) over \(\mathbf Q(X)\) rules out only a universal rational-function coarse selector. Outside finitely many primes, a uniform \(j\in\mathbf F_r\) has a modular-polynomial discriminant collision with probability at most \(d_\ell/r\), but this says nothing about fixed CM points such as 0 and 1728. A characteristic-zero CM ideal label also needs compatible local endomorphism embeddings; the abstract label alone does not orient the unknown CRT components.

P33 leaves open \(N\)-dependent selectors, higher-class-number CM with explicit embeddings, vertical and supersingular constructions, and every fine representation from which the selective section can actually be recovered. It proves no general selector lower bound.

The candidate, corrected hostile audit, and proof-blind reconstruction are preserved under `experiments/F23_canonical_isogeny_neighbor_kill`, `experiments/F23_canonical_isogeny_neighbor_audit`, and `experiments/F23_canonical_isogeny_neighbor_reconstruct`.

## P34 — Boolean pooling gives constant relation mass, but the exact evaluator remains exponential in the input length

**Status:** promoted.

**Verification record:** the probability theorem, floor constants, local-OR
scope, meet-in-the-middle identity and signs, composite-ring evaluator, exact
bit/space bounds, cube-tree identity, and representation-specific limitations
passed a corrected hostile audit and a proof-blind end-to-end reconstruction.
No cross-family audit has run.

Let

\[
N=pq,\qquad 53\le p<q<2p
\]

for distinct odd primes.  Put

\[
h=\lfloor\sqrt N\rfloor,\quad
K=\lfloor\log_2h\rfloor-3,\quad
T=2^K,
\]

draw independent uniform \(a_1,\ldots,a_K)\) modulo \(N\), and define

\[
Q_K=\prod_{\varnothing\ne S\subseteq[K]}
\left(\sum_{i\in S}a_i\right)\pmod N.
\]

For \(r\in\{p,q\}\), let \(E_r\) be the event that at least one nonempty
subset sum vanishes modulo \(r\), and put \(\mu_r=(T-1)/r\).

**Constant-mass pooled event.**  Distinct nonempty \(0/1\) incidence vectors
are linearly independent in pairs over every field.  The corresponding
zero indicators are therefore pairwise independent, so the second-moment
bound gives

\[
\Pr(E_r)\ge
\frac{\mu_r}{\mu_r+1-1/r}.
\]

The exact floors imply

\[
\frac1{32\sqrt2}<\mu_r<\frac{\sqrt2}{8}.
\]

The complete arrays modulo \(p\) and \(q\) are independent under CRT.  In
each field, and only in that componentwise sense, the product is a
cancellation-free OR:

\[
Q_K=0\pmod r
\quad\Longleftrightarrow\quad E_r.
\]

Consequently

\[
\Pr\bigl(1<\gcd(Q_K,N)<N\bigr)
=\Pr(E_p\mathbin\triangle E_q)
\ge
\frac{2}{32\sqrt2+1}
\left(1-\frac{\sqrt2}{8}\right).
\]

Thus a uniform exact evaluator for \(Q_K\bmod N\) with bit cost polynomial
in \(\log N+K\) would give a constant-expected-trial Las Vegas splitter on
this balanced squarefree-semiprime promise.  This does not cover unbalanced
semiprimes, repeated factors, prime powers, even inputs, or arbitrary
composites.

**Exact evaluator boundary.**  For a split
\([K]=A\mathbin{\dot\cup}B\), put

\[
x_U=\sum_{i\in U}a_i,\quad
y_V=\sum_{i\in V}a_i,\quad
F_A(X)=\prod_{U\subseteq A}(X+x_U),\quad
Q_A=\prod_{\varnothing\ne U\subseteq A}x_U.
\]

Then, over every commutative ring,

\[
Q_K=Q_A\prod_{\varnothing\ne V\subseteq B}F_A(y_V).
\]

Equivalently, with
\(P_B(X)=\prod_{V\ne\varnothing}(X-y_V)\),

\[
Q_K=Q_A\operatorname{Res}(P_B,F_A).
\]

The alternative ordering carries the usual
\((-1)^{\deg P_B\deg F_A}\) sign; no sign-free resultant convention is
assumed.

For \(|A|=\lceil K/2\rceil\) and
\(|B|=\lfloor K/2\rfloor\), enumerate the half sums by Gray code, build a
monic product tree for \(F_A\), and evaluate it at all \(y_V\) by a monic
subproduct/remainder tree.  Fast monic division over \(\mathbb Z/N\mathbb Z\)
uses reversal and Newton inversion only of a power series with constant
coefficient \(1\); it never inverts a data-dependent residue or a point
difference.  Carry-safe Kronecker packing reduces polynomial multiplication
to uniform integer multiplication.  Since the largest tree degree is

\[
D=2^{\lceil K/2\rceil}=\Theta(N^{1/4}),
\]

the exact evaluator uses

\[
N^{1/4+o(1)}
\]

bit time and space.  Direct Gray-code multiplication over all subsets uses
\(N^{1/2+o(1)}\) bit time and polynomial space.

**Structural identities and scope.**  The direction-weighted \(K\)-cube has
spanning-tree enumerator

\[
\tau_K=2^{2^K-K-1}Q_K.
\]

For \(a_i=u2^{i-1}\),

\[
Q_K=u^{2^K-1}(2^K-1)!.
\]

Over \(\mathbb Q(a_1,\ldots,a_K)\), the subset-sum diagonal operator has
minimal-polynomial degree \(2^K\), and a characteristic-zero polynomial
vanishing on every hyperplane
\(\sum_{i\in S}a_i=0\) is divisible by \(Q_K\).  These are exact
representation statements, not arithmetic-circuit, compressed-state, or
modular-evaluation lower bounds.  P34 therefore verifies that exponentially
many rare relations can be pooled into a constant-probability event, while
leaving the decisive polylogarithmic evaluator completely open.

The corrected candidate, hostile audit and fresh re-audit, and proof-blind
reconstruction are preserved under
`experiments/F24_amortized_mixed_relation_decoder`,
`experiments/F24_amortized_mixed_relation_decoder_audit`,
`experiments/F24_amortized_mixed_relation_decoder_reaudit`, and
`experiments/F24_amortized_mixed_relation_decoder_reconstruct`.

## P35 — public zero-syndrome lattices do not amortize hidden local kernels

**Status:** promoted.

**Verification record:** the Construction-A indices, determinantal-rank
separator, exact-kernel quotient, general rank/covolume formulas, CVP coset
invariance, Hurwitz handedness and minima, graph threshold, Gram quotient,
and public output/scaled-dual boundary passed a corrected hostile re-audit
and a proof-blind end-to-end reconstruction.  No cross-family audit has run.

Let \(A\in\mathbb Z^{t\times d}\), let \(N=pq\) for distinct primes, and set

\[
K_r(A)=\{x\in\mathbb Z^d:Ax\equiv0\pmod r\},\qquad
s_r=\operatorname{rank}_{\mathbb F_r}(A\bmod r).
\]

Then

\[
\det K_r(A)=r^{s_r},\qquad
K_N(A)=K_p(A)\cap K_q(A),\qquad
\det K_N(A)=p^{s_p}q^{s_q}.
\]

If \(s_p\ne s_q\), an integer determinantal divisor of \(A\) vanishes
modulo exactly one prime, so SNF followed by a gcd already factors \(N\) in
polynomial bit complexity.  In the remaining equal-rank case, the desired
set

\[
(K_p\setminus K_q)\cup(K_q\setminus K_p)
\]

is not a lattice.  More precisely, any subgroup contained in a union of two
subgroups lies wholly in one of them.  The public homogeneous
Construction-A object therefore represents the CRT intersection, not the
one-local-only disjunction.

Put

\[
\rho=\operatorname{rank}_{\mathbb Q}A,\qquad
K_0=\ker_{\mathbb Z}A.
\]

The lattice \(K_0\) is primitive of rank \(d-\rho\).  If \(\pi\) denotes
orthogonal projection off its real span and \(\Delta_0\) its covolume in
that span, then

\[
\det\pi(K_p)=\frac{p^{s_p}}{\Delta_0},\quad
\det\pi(K_q)=\frac{q^{s_q}}{\Delta_0},\quad
\det\pi(K_N)=\frac{p^{s_p}q^{s_q}}{\Delta_0}.
\]

When \(s_p=s_q=u\) and \(\rho>0\), the determinant-root scales in the
faithful rank-\(\rho\) quotient are

\[
p^{u/\rho}\Delta_0^{-1/\rho},\quad
q^{u/\rho}\Delta_0^{-1/\rho},\quad
N^{u/\rho}\Delta_0^{-1/\rho}.
\]

Only the full-local-rank case \(u=\rho\) simplifies to the exponent one.
For \(\rho=0\), \(A=0\) and there is no syndrome.  Thus concatenating many
samples into a fixed output does not create high-dimensional metric
amortization: it adds exact, prime-independent kernel directions.  For one
quaternion output the faithful quotient has rank at most four.

If a public target \(t\in\mathbb Z^d\) is reduced by any
\(v\in K_N(A)\), then \(e=t-v\) satisfies

\[
e\in K_r(A)\quad\Longleftrightarrow\quad t\in K_r(A).
\]

CVP inside the public intersection cannot manufacture a new local-zero
syndrome.  For a target uniform modulo \(N\), the exact probability of
landing in exactly one local kernel is

\[
p^{-s_p}+q^{-s_q}-2p^{-s_p}q^{-s_q},
\]

which is exponentially small on balanced inputs when the common rank is
positive.

**Exact Hurwitz block.**  For a norm-\(N\) Hurwitz integer \(\alpha\), the
matrix of left multiplication has

\[
\operatorname{SNF}(M_\alpha)=\operatorname{diag}(1,1,N,N).
\]

The intrinsic local right ideals

\[
J_r(\alpha)=\{x:\alpha x\in r\mathcal H\}
\]

have determinant \(r^2\) and exact shortest Hurwitz length \(\sqrt r\).
Their public intersection is

\[
J_N(\alpha)=\bar\alpha\mathcal H,
\qquad \det J_N=N^2,
\qquad \lambda_1(J_N)=\sqrt N.
\]

Its Gram matrix is exactly \(N\) times the fixed Hurwitz Gram matrix.
Direct sums preserve the three determinant-root scales
\(\sqrt p,\sqrt q,\sqrt N\), so block multiplication also gains no
amortization.  A basis of a local ideal would reveal its prime from the
determinant before LLL is invoked.

For the public graph lattice

\[
\Gamma_{a,b}(A,N)=
\{(ax,b(Ax-Nz)):x\in\mathbb Z^d,z\in\mathbb Z^t\},
\]

the determinant is \(a^d(bN)^t\).  In one Hurwitz block,

\[
\|\alpha x-Nz\|_Q^2
=N\|x-\bar\alpha z\|_Q^2.
\]

If \(x\in J_r(\alpha)\) and the unshifted residual has length strictly below
\(r\), the residual must be zero and \(x\in J_N(\alpha)\).  This closes
only that below-threshold graph slice.

**The remaining metric boundary is explicit.**  Two other full-rank public
lattices are

\[
\Lambda_{\rm out}=A\mathbb Z^d+N\mathbb Z^t,
\qquad
\det\Lambda_{\rm out}=p^{t-s_p}q^{t-s_q},
\]

and

\[
\Lambda_{\rm dual}
=NK_N(A)^*
=N\mathbb Z^d+A^{\mathsf T}\mathbb Z^t,
\qquad
\det\Lambda_{\rm dual}=p^{d-s_p}q^{d-s_q}.
\]

P35 proves no shortest-vector, closest-vector, target-distribution, or
factor-extraction theorem for either lattice, nor for a faithful fixed-rank
quotient, biased targets, or nonlinear combinations.  It is a narrow
obstruction to public zero-syndrome and high-dimensional Gram amortization,
not a lattice lower bound or a factoring algorithm.

The corrected candidate, hostile audit and fresh re-audit, and proof-blind
reconstruction are preserved under
`experiments/F25_hidden_modulus_relation_lattice`,
`experiments/F25_hidden_modulus_relation_lattice_audit`,
`experiments/F25_hidden_modulus_relation_lattice_reaudit`, and
`experiments/F25_hidden_modulus_relation_lattice_reconstruct`.

## P36 — exact pinned factor-witness counts self-reduce, but the natural
COPY--AND matchgate basis is impossible

**Status:** promoted.

**Verification record:** the count-to-factor self-reduction, every-input
recursion and bit bound, contraction-preserving transpose-dual convention,
complete ternary-COPY basis classification, AND parity contradiction, and
explicit bipartite fanout realization passed a corrected hostile re-audit
and an independent proof-blind reconstruction.  The reconstruction used a
different slice-pencil proof of the AND obstruction.  No cross-family audit
has run.

Let \(N>1\), and let \(Z(P)\) denote the exact number of Boolean
multiplication witnesses

\[
xy=N,
\]

whose fixed-length \(x\)-encoding extends a prefix \(P\).  A polynomial-size
deterministic multiplier network has exactly one internal assignment for
each ordered divisor pair.  Define

\[
Z_*(P)=Z(P)
-\mathbf1_{\{1\text{ extends }P\}}
-\mathbf1_{\{N\text{ extends }P\}}.
\]

If \(N\) is composite, then \(Z_*(\varnothing)=\tau(N)-2>0\), and

\[
Z_*(P)=Z_*(P0)+Z_*(P1).
\]

Choosing a positive child at every bit therefore returns an integer
\(1<x<N\) with \(x\mid N\).  Exact division verifies the split.
Deterministic primality testing and recursion give the complete
factorization, including even inputs, prime powers, repeated factors, and
unbalanced composites.  There are \(O(\log N)\) recursion nodes and
\(O(\log N)\) pinned contractions per node, and every count has polynomial
bit length.  Consequently a uniform exact polynomial-bit contraction
algorithm for every original and prefix-pinned witness network would imply
deterministic polynomial-time factoring.  The divisor is recovered directly,
with no terminal factor-extracting gcd.

The natural Valiant-style landing fails locally.  Put

\[
E=e_0^{\otimes3}+e_1^{\otimes3}
\]

for ternary COPY and let \(A\) be the ternary AND relation.  Ordinary edge
contraction requires a primal action \(T\) on one endpoint and the
transpose-dual action

\[
S=(T^{-1})^{\mathsf T}
\]

on the other.  Every invertible \(T\) making \(T^{\otimes3}E\) parity-pure
has one of the two forms

\[
T=\operatorname{diag}(a,c)
\begin{pmatrix}1&-\rho\\1&\rho\end{pmatrix}
\quad\text{or}\quad
T=\operatorname{diag}(a,c)
\begin{pmatrix}1&\rho\\1&-\rho\end{pmatrix},
\qquad \rho^3=-1.
\]

For either form there are nonzero \(\lambda_0,\lambda_1,r\) such that

\[
Se_0=\begin{pmatrix}\lambda_0\\\lambda_1\end{pmatrix},
\qquad
Se_1=r\begin{pmatrix}\lambda_0\\-\lambda_1\end{pmatrix}.
\]

Permit independent common bases for the two copied input roles and an
arbitrary invertible action on the AND-output leg.  After nonzero input
scalings are removed, the transformed AND output slice is

\[
W_{s,t}=u(1+xs+yt)+vxy\,st,
\qquad s,t\in\{\pm1\},\qquad xy\ne0,
\]

where \(u,v\) are independent.  If the tensor were even, its four forbidden
entries force both \(x=y\) and \(x=-y\); the odd case forces the same two
equalities in the opposite order.  If either relevant coordinate of \(u\)
is zero, the equations instead force \(xy=0\).  Thus transformed AND is
neither even nor odd and hence is not a ternary matchgate.

The local hypotheses occur literally in a polynomial-size bipartite
realization: complete padded trees of ternary COPY tensors put all leaf COPY
vertices on one side and connect their used leaf legs directly to AND
inputs on the other; neutral unaries and binary equality subdivisions
preserve every witness with multiplicity one.  Therefore the displayed
separated COPY\(_3\)--AND\(_3\) network cannot acquire an FKT/Pfaffian
contraction through a common role basis and its required dual action.

This is not a tensor-contraction lower bound.  High-arity equality, fused
multiplier cells, edge- or vertex-dependent gauges, other gate sets,
different Pfaffian identities, public-pin cancellations, bounded-genus
constructions, and non-matchgate exact contraction remain open.

The corrected candidate, first audit, fresh re-audit, and proof-blind
reconstruction are preserved under
`experiments/F26_holographic_factor_network`,
`experiments/F26_holographic_factor_network_audit`,
`experiments/F26_holographic_factor_network_reaudit`, and
`experiments/F26_holographic_factor_network_reconstruct`.

## P37 — public output/dual quotients have only public scale, and the fixed-completion tail is cyclic

**Status:** promoted.

**Verification record:** the CRT, Smith-block, output/transpose faithful
quotient, fixed-batch, cyclic normal-form, duality, scalar-gcd, SVP/CVP,
uniform-line, edge-case, and bit-complexity claims passed a corrected hostile
re-audit and a strict proof-blind reconstruction.  A first blind
reconstruction prompt incorrectly strengthened the Smith branch by requiring
every nonzero invariant to be coprime to \(N\); it was rejected on
\(A=(N)\), is preserved, and supplies no evidence.  A fresh reconstruction
of the exact \(1\)-/\(N\)-block theorem succeeded.  No cross-family audit
has run.

Let \(N=pq\) for distinct primes and
\(A\in\mathbb Z^{t\times d}\).  Define

\[
\Lambda_{\rm out}(A,r)=A\mathbb Z^d+r\mathbb Z^t,
\qquad
\Lambda_{\rm dual}(A,r)=r\mathbb Z^d+A^{\mathsf T}\mathbb Z^t.
\]

Both are exact CRT intersections of their \(p\)- and \(q\)-local
versions.  Subtracting any vector of the public \(N\)-lattice preserves both
local cosets, so CVP cannot change whether a target belongs to exactly one
local output module.  If
\(s_r=\operatorname{rank}_{\mathbb F_r}(A\bmod r)\), a target uniform
modulo \(N\) has exact one-local output probability

\[
p^{-(t-s_p)}+q^{-(t-s_q)}
-2p^{-(t-s_p)}q^{-(t-s_q)},
\]

with the analogous formula in dimension \(d\) for the transpose side.
The scaled Euclidean dualities are

\[
N\Lambda_{\rm out}(A,N)^*=K_N(A^{\mathsf T}),
\qquad
NK_N(A)^*=\Lambda_{\rm dual}(A,N).
\]

Take integer Smith form
\(UAV=\operatorname{diag}(\sigma_1,\ldots,\sigma_\rho,0,\ldots)\)
and put \(\delta_i=\gcd(\sigma_i,N)\).  A value
\(1<\delta_i<N\) is already a proper factor.  Otherwise the divisibility
chain gives a block of \(1\)'s followed by a block of \(N\)'s.  Let
\(u\) be the number of \(1\)'s; the later nonzero Smith entries are
divisible by \(N\), not asserted coprime to it.  Define the public primitive
exact directions

\[
E_{\rm out}=U^{-1}(\mathbb Z^u\oplus0),
\qquad
E_{\rm dual}=V^{-\mathsf T}(\mathbb Z^u\oplus0).
\]

Then, simultaneously for \(r=p,q,N\),

\[
\Lambda_{\rm out}(A,r)=E_{\rm out}+r\mathbb Z^t,
\qquad
\Lambda_{\rm dual}(A,r)=E_{\rm dual}+r\mathbb Z^d.
\]

Orthogonal projection off either exact-direction span therefore gives
literally \(r\) times one fixed public projected ambient lattice.  The
quotient dimensions are \(t-u\) and \(d-u\), and their covolumes are

\[
\frac{r^{t-u}}{\operatorname{covol}(E_{\rm out})},
\qquad
\frac{r^{d-u}}{\operatorname{covol}(E_{\rm dual})}.
\]

These are exact quotient identities, not an orthogonal splitting of the
original integer lattice; full-lattice metric coupling remains open.

For a batch with columns
\(\beta_i=(x_i,y_i,z,w)^{\mathsf T}\) sharing one completion, let
\(T\) have columns \((x_i,y_i,1)^{\mathsf T}\).  Surjectivity of
\(T\) over \(\mathbb Z/N\) is equivalent to

\[
\gcd(N,\Delta_3(T))=1,
\]

where \(\Delta_3\) is the gcd of all maximal minors.  Under this condition
the output lattice splits as

\[
\mathbb Z^2\oplus O_C,
\qquad
O_C=(z,w)\mathbb Z+N\mathbb Z^2.
\]

For \(C=(z,w)\ne0\), write
\(g=\gcd(z,w)>0\), \(h=\gcd(g,N)\), \(C_0=C/g\), and choose
\(D\) with \(\det(C_0,D)=1\).  The determinant-congruence lattice

\[
L_C=\{v:wv_1-zv_2\equiv0\pmod N\}
\]

has the exact normal forms

\[
L_C=\mathbb ZC_0+\frac Nh\mathbb ZD,
\qquad
O_C=h\mathbb ZC_0+N\mathbb ZD,
\]

with determinants \(N/h\) and \(Nh\).  They are equal exactly when
\(h=1\), while \(1<h<N\) already exposes a factor and \(h=N\) makes
\(L_C=\mathbb Z^2\).  Quarter rotation \(R\) gives

\[
NO_C^*=R(L_C),
\qquad
NL_C^*=R(O_C).
\]

On the unfactored \(h=1\) branch every public vector is uniquely

\[
v=aC_0+NbD,
\qquad
\gcd(N,v_1,v_2)=\gcd(N,a),
\]

where local output-line membership of an ambient
\(\alpha C_0+\beta D\) is instead \(r\mid\beta\).  Thus the
coordinate-gcd event is one explicit public scalar ticket, not a hidden
determinant scale.  If \(\lVert C_0\rVert^2<N\), the complete shortest
set is \(\{\pm C_0\}\).  Projecting off \(C_0\) leaves the rank-one
lattices

\[
\frac r{\lVert C_0\rVert}\mathbb Z
\quad(r=p,q,N),
\]

and the two-dimensional scaled dual is only the rotation
\(NL_C^*=R(L_C)\).

A target uniform in the cyclic quotient has exact one-local CVP probability

\[
\frac1p+\frac1q-\frac2N,
\]

independent of the chosen closest-vector tie.  If
\(p<q\le\kappa p\) are distinct odd primes and the completion line is
marginally uniform on

\[
\mathcal S_r=
\{[x:y]\in\mathbb P^1(\mathbb F_r):x^2+y^2\ne0\},
\qquad
|\mathcal S_r|=r-\left(\frac{-1}{r}\right),
\]

then the probability that **any** shortest vector has a proper coordinate
gcd is \(O(1/p+1/q)\).  The proof divides a bad shortest vector by its
factor, uses the planar Hermite bound to leave only finitely many primitive
integer directions, proves the opposite-prime reduction is nonzero, and
handles isotropic reductions, collisions, ties, and small primes.  Only the
two marginals are used.  This hypothesis is not supplied by P30's
conditional row/image-line theorem.

All Smith, gcd, minor, projection, and fixed-dimensional lattice operations
have deterministic polynomial bit complexity.  P37 proves no factoring
algorithm and no general lattice lower bound.  Biased completions or targets,
batches without the fixed-completion/surjective-\(T\) hypotheses, nonlinear
combinations, and coordinate-gcd optimization in the original
nonorthogonally coupled full lattice remain open.

The candidate, first audit, fresh re-audit, rejected over-strengthened blind
attempt, and successful corrected reconstruction are preserved under
`experiments/F27_public_output_dual_metric_kill`,
`experiments/F27_public_output_dual_metric_audit`,
`experiments/F27_public_output_dual_metric_reaudit`,
`experiments/F27_public_output_dual_metric_reconstruct`, and
`experiments/F27_public_output_dual_metric_reconstruct_corrected`.

## P38 — positive perfect-matching sampling would factor, but direct deletion gadgets are subcubes

**Status:** promoted.

**Verification record:** the equal-fiber sampling reduction, all-input
recursion, exact total-variation constants, rational cooling schedule,
empirical-failure accounting, fair-bit implementation, expected-cost
argument, deletion-support exchange theorem, one-hot subcube classification,
four local-signature obstructions, and Valiant-scope distinction passed four
hostile audit rounds—three requiring corrections and one clean—and a strict
proof-blind reconstruction.  The
reconstruction independently made bounded terminal conditioning and bounded
bad-estimate paths explicit.  No cross-family audit has run.

Let

\[
\mathcal W_N=\{(x,y)\in\mathbb Z_{>0}^2:xy=N\}.
\]

Suppose uniform polynomial-time algorithms build an unweighted bipartite
graph \(G_N\), with at most \(n^a\) vertices per side for
\(n=\lceil\log_2(N+1)\rceil\), and decode every perfect matching to a member
of \(\mathcal W_N\).  Suppose further that one positive integer \(c_N\)
is the number of matching preimages of every ordered witness.  Then a uniform
perfect matching pushes forward to the uniform law on the
\(\tau(N)\) ordered positive divisors.

The Jerrum--Sinclair--Vigoda almost-uniform sampler can be implemented on fair
bits so that it always returns an actual perfect matching, has
total-variation error \(1/12\), terminates almost surely, and has expected
bit and fair-random-bit cost polynomial in the graph size.  One explicit
Turing implementation uses rational \(3/4\) cooling one nonedge at a time,
terminal activity \(1/m!\), at most

\[
O(m^3\log m)
\]

phases and \(O(m^5\log m)\) empirical sector estimates.  The full event that
any estimate misses its multiplicative window is assigned probability at
most \(1/24\); a zero count is only a detectable subevent and triggers a
known perfect-matching fallback.  Positive but inaccurate paths retain
positive polynomial-bit rational weights and run for predetermined polynomial
length, so they are total and are charged to the same bad event.  On good
paths, bounded terminal conditioning/rejection returns a genuine original-edge
matching and contributes at most the remaining \(1/24\) in total variation.
Unreduced rational numerators and denominators grow by only polynomially many
bits.  Exact rational coins treat probabilities \(0,1\) deterministically and
otherwise use power-of-two rejection with fewer than two rounds in
expectation.

Exactly two witnesses, \((1,N)\) and \((N,1)\), are trivial.  Every
composite has \(\tau(N)\ge3\), so a sample at distance \(1/12\) from
uniform returns a verified proper divisor with probability at least

\[
\frac{\tau(N)-2}{\tau(N)}-\frac1{12}
\ge\frac14.
\]

Fresh complete sampler invocations therefore give at most four expected
trials per composite node.  Deterministic primality testing, exact product
verification, and recursive splitting handle primes, prime powers, repeated
factors, even inputs, and unbalanced composites.  If the complete
factorization has \(r\) prime leaves with multiplicity, then
\(2^r\le N\), so the recursion tree has at most \(2n-1\) nodes.  Summing
fresh-call expectations gives one fixed polynomial expected bit and fair-bit
bound without assuming independence between a call's own cost and success.
This is a complete conditional factoring theorem, but no graph satisfying
the hypothesis is constructed.

There is also an unconditional support boundary.  For a finite graph \(H\)
with boundary \(B\), put

\[
F_H(S)=\#\operatorname{PM}(H-S),
\qquad
\mathcal F_H=\{S\subseteq B:F_H(S)>0\}.
\]

Every feasible deletion set has fixed parity.  In a bipartite graph it also
has fixed left-minus-right charge.  If
\(X,Y\in\mathcal F_H\), symmetric differences of perfect matchings give

\[
\forall e\in X\triangle Y\ \exists f\in X\triangle Y:
X\triangle\{e,f\}\in\mathcal F_H.
\]

Thus a nonempty support is an even matching delta-matroid.  If logical words
are encoded exactly by choosing one deleted terminal from each dual-rail
pair, all feasible sets have equal size and hence are matroid bases.  Basis
exchange cannot move a rail between different logical coordinates without
creating an off-code word, so every coordinate that varies can be flipped
individually.  The logical relation must therefore be a subcube.  Empty
support is a separate realizable case.

Direct single-rail COPY\(_3\), AND\(_3\), full addition, and
\(a+c+xy=s+2d\) each contain valid words of opposite parity.  Their exact
nonempty one-hot dual-rail relations fail single-coordinate closure and are
not subcubes.  Positive weights and arbitrary internal auxiliary vertices do
not change this support theorem.

Valiant's permanent-hardness gadgets do not supply the missing positive
distribution: negative contributions cancel only after summation, modular
equalities control residues rather than positive fibers, and interpolation
combines totals from several instances.  None gives an individual-matching
decoder with equal positive witness multiplicities.

P38 does not cover closed internal-edge observables, off-code states filtered
globally, larger block codes, assignment-dependent auxiliary states, global
multiplicity balancing, or one multiplication-specific graph.  These are
the exact F21 survivors.

The candidate, three correction audits, and strict reconstruction are
preserved under
experiments/F28_positive_matching_factor_graph_kill,
experiments/F28_positive_matching_factor_graph_audit,
experiments/F28_positive_matching_factor_graph_reaudit,
experiments/F28_positive_matching_factor_graph_reaudit2,
experiments/F28_positive_matching_factor_graph_reaudit3, and
experiments/F28_positive_matching_factor_graph_reconstruct.

## P39 — uniform full-lattice random codes do not amortize factor-divisible shortest vectors

**Status:** promoted.

**Verification record:** the CRT determinant and slice identities,
coordinate-gcd classification, uniform-subspace incidence, Minkowski/public
cutoff, eligible-point and cube bounds, all shortest-vector ties, both radius
branches, and every dimension regime passed a corrected hostile audit, a
clean re-audit, and a strict proof-blind reconstruction.  The first audit
correctly separated the actual small-dimension event from a loose
cube-volume expression.  No cross-family audit has run.

Let \(N=pq\) for distinct primes.  Independently choose uniform
\(u\)-dimensional subspaces

\[
C_p\le\mathbb F_p^m,
\qquad
C_q\le\mathbb F_q^m,
\qquad
1\le u<m,
\]

and form the complete CRT Construction-A lattice

\[
L=\{x\in\mathbb Z^m:x\bmod p\in C_p,\ x\bmod q\in C_q\}.
\]

If

\[
L_r=\{x\in\mathbb Z^m:x\bmod r\in C_r\},
\]

then

\[
\det L=N^{m-u},
\qquad
L\cap p\mathbb Z^m=pL_q,
\qquad
L\cap q\mathbb Z^m=qL_p.
\]

For nonzero \(x\in L\), a proper coordinate gcd with \(N\) is therefore
exactly membership in one of these two slices but not
\(N\mathbb Z^m\).

Put

\[
v_m=\frac{\pi^{m/2}}{\Gamma(m/2+1)},\qquad
R_M=2v_m^{-1/m}N^{1-u/m},\qquad
R_0=\min(R_M,N),
\]

and

\[
\theta_r=\frac{r^u-1}{r^m-1}.
\]

Minkowski gives \(\lambda_1(L)\le R_M\), while
\(Ne_i\in L\) gives \(\lambda_1(L)\le N\).  Hence every exact
shortest vector lies inside radius \(R_0\).  For the \(p\)-slice, division
by \(p\) leaves a nonzero residue that must land in the random code \(C_q\),
which has exact incidence probability \(\theta_q\).  The sharp finite union
bound is

\[
\theta_q
\#\{y\in\mathbb Z^m:\|y\|_2\le R_0/p,\ y\bmod q\ne0\},
\]

with the symmetric \(q\)-slice term.  The unit-cube relaxation gives the
tie-independent bound

\[
\Pr(\exists\text{ proper-gcd shortest vector})
\le
\theta_qv_m\left(\frac{R_0}{p}+\frac{\sqrt m}{2}\right)^m
+
\theta_pv_m\left(\frac{R_0}{q}+\frac{\sqrt m}{2}\right)^m.
\]

Fix \(u\), a balance constant \(\kappa\), and \(K\).  Uniformly over

\[
p\le q\le\kappa p,
\qquad
u<m\le(\log N)^K,
\]

the **actual** event satisfies

\[
\Pr(\exists\text{ proper-gcd shortest vector})
\le N^{-u/2+o(1)}.
\]

When \(u<m<2u\), the divided radii tend below one and the eligible
nonzero-vector count is eventually zero; the literal cube relaxation is not
claimed to have the sharper exponent.  At \(m=2u\), only constantly many
divided vectors remain and each costs \(N^{-u/2+o(1)}\).  For
\(m\ge2u+1\) and \(R_M\le N\), substitution leaves leading terms below
\(2^m/p^u\) and \(2^m/q^u\); the branch inequality forces
\(m\log m=O(\log N)\), so \(2^m=N^{o(1)}\).  On the
\(R_M>N\) branch, the public radius \(N\), the inequality
\(v_mN^u<2^m\), and the shrinking unit-ball volume give the same bound.
The event quantifies over every shortest vector simultaneously, so it is
independent of tie-breaking.

P39 grants even an exact-SVP oracle and proves only that its complete
shortest set is almost surely useless in this clean model.  It is not an SVP
hardness theorem and does not cover biased or dependent arithmetic codes,
growing local dimension \(u\), affine targets, CVP, LLL, nonshortest
statistics, nonlinear decoding, or arbitrary public lattices manufactured
from \(N\).

The candidate, audit, clean re-audit, and strict reconstruction are preserved
under
experiments/F29_full_lattice_random_code_kill,
experiments/F29_full_lattice_random_code_audit,
experiments/F29_full_lattice_random_code_reaudit, and
experiments/F29_full_lattice_random_code_reconstruct.

## P40 — low-actual-degree products only OR rare affine CRT zeros

**Status:** promoted.

**Verification record:** the fixed-polynomial theorem, actual reduced-degree
caps, exact CRT XOR, sharp rectangular envelope, random-coefficient
conditioning, fresh-batch adaptation, four formal-zero cases, coefficient
content, zero-function ideal, representation boundaries, and balanced
threshold passed an initial hostile audit with six required repairs, two
intermediate re-audits, a strict reconstruction that found a substantive
interpretive correction, a clean hostile audit of the amended theorem, and a
fresh context-free proof-blind reconstruction of that final statement.  No
cross-family audit has run.

Let \(N=pq\) for distinct primes and let

\[
X\sim\operatorname{Unif}((\mathbb Z/N\mathbb Z)^k).
\]

For \(F_1,\ldots,F_s\in\mathbb Z[X_1,\ldots,X_k]\), suppose every
formal reduction \(f_{j,r}=F_j\bmod r\) is nonzero for
\(r\in\{p,q\}\).  Put

\[
\delta_{j,r}=\deg f_{j,r},\qquad
\Delta_r=\sum_j\delta_{j,r},\qquad
u_r=\min\left(1,\frac{\Delta_r}{r}\right),
\]

and

\[
\alpha_r=
\Pr\left[\prod_jf_{j,r}(X_r)=0\right].
\]

CRT makes \(X_p,X_q\) independent and uniform.  Since a polynomial ring
over a field is an integral domain, the reduced product is nonzero of degree
\(\Delta_r\), and Schwartz--Zippel gives \(0\le\alpha_r\le u_r\).
The proper-gcd probability is exactly

\[
\Pr\left(1<\gcd\left(N,\prod_jF_j(X)\right)<N\right)
=\alpha_p+\alpha_q-2\alpha_p\alpha_q.
\]

If

\[
\Psi(u,v)=\max\{u,v,u+v-2uv\},
\]

then the sharp envelope implied by the separate local caps is

\[
\Pr(\text{proper gcd})\le\Psi(u_p,u_q).
\]

In particular, for \(D=\sum_j\deg F_j\),

\[
\Pr(\text{proper gcd})
\le
\min\left\{1,\frac{\Delta_p}{p}+\frac{\Delta_q}{q}\right\}
\le
\min\left\{1,D\left(\frac1p+\frac1q\right)\right\}.
\]

When \(D\le\min(p,q)/2\), monotonicity on the half-square gives the sharper

\[
\Pr(\text{proper gcd})
\le\frac Dp+\frac Dq-\frac{2D^2}{pq},
\]

with the corresponding local-degree version.

Random coefficients must be conditioned on before applying CRT independence:

\[
\Pr(\text{proper gcd})
=\mathbb E_\Theta[
\alpha_p(\Theta)+\alpha_q(\Theta)
-2\alpha_p(\Theta)\alpha_q(\Theta)].
\]

Shared coefficient randomness can correlate the two conditional rates, so an
XOR formula formed from unconditional marginals is false in general.  The
same conditional argument works for adaptive polynomials only on a genuinely
fresh full-affine batch.  Selecting \(F_X(T)=T-X\) after observing the point
shows why same-sample adaptation is outside the theorem.

If \(Z_r\) is the set of factors formally zero modulo \(r\), the exact
product-gcd alternatives are

| \(Z_p\) | \(Z_q\) | proper-gcd probability |
|---|---|---|
| empty | empty | \(\alpha_p+\alpha_q-2\alpha_p\alpha_q\) |
| nonempty | empty | \(1-\alpha_q\) |
| empty | nonempty | \(1-\alpha_p\) |
| nonempty | nonempty | \(0\) |

For an explicit collected coefficient list, formal zero modulo \(r\) is
equivalent to divisibility of the coefficient content by \(r\); a one-sided
formal identity therefore exposes a factor.  Individual contents must be
checked before multiplication: \(F_1=p,F_2=q\) each separates, whereas their
product has gcd \(N\).  No efficient content extractor is asserted for a
succinct arithmetic circuit.

Formal nonzero is not functional nonzero.  The vanishing ideal of the full
affine field space is exactly

\[
(X_1^r-X_1,\ldots,X_k^r-X_k).
\]

Thus characteristic-scale degree can make Schwartz--Zippel vacuous.  Sparse
binary exponents and repeated-squaring circuits can reach exponential actual
degree with polynomial description and evaluation size.

On fixed-balance semiprimes, polynomial total actual degree gives

\[
\Pr(\text{proper gcd})
=O\left(\frac{D}{\sqrt N}\right)
=2^{-n/2+O(\log n)}
\]

for \(D=\operatorname{poly}(n)\).  Inverse-polynomial success inside this
model requires total actual degree
\(\Omega(\sqrt N/\operatorname{poly}(n))\).  This is not a circuit-size,
evaluation-time, or factoring lower bound.

Most importantly, P40 is **not** a genuine joint-decoder theorem.  Locally,

\[
\prod_jf_{j,r}(X_r)=0
\quad\Longleftrightarrow\quad
\bigvee_j[f_{j,r}(X_r)=0].
\]

The product merely ORs rare zero tickets; CRT turns the two local OR events
into an XOR.  High-actual-degree succinct pooling, nonuniform or correlated
sources, rational/branching/metric computations, and decoders that combine
typical nonzero values remain open.

The candidate, audits, correction reconstruction, final clean audit, and
context-free final reconstruction are preserved under
`experiments/F31_low_degree_joint_amortization_kill`,
`experiments/F31_low_degree_joint_amortization_audit`,
`experiments/F31_low_degree_joint_amortization_reaudit`,
`experiments/F31_low_degree_joint_amortization_reaudit2`,
`experiments/F31_low_degree_joint_amortization_reconstruct`,
`experiments/F31_low_degree_joint_amortization_reaudit3`, and
`experiments/F31_low_degree_joint_amortization_reconstruct2`.

## P41 — quadratic Fourier energy has constant factor mass; its classical sampler remains missing

**Status:** promoted.

**Verification record:** the Gauss-energy identity, normalizer, sharp useful
mass, all-input sampler reduction, recursive expected-cost proof, rejection
and direct-gcd costs, hidden-normalizer audit, and natural Metropolis
obstruction passed an initial clean hostile audit and strict blind
reconstruction.  The reconstruction found a stronger exact zero-atom
eigenmode; the amended \(\Omega(N)\) semiprime mixing theorem passed a fresh
hostile re-audit and a new context-free proof-blind reconstruction.  No
cross-family audit has run.

For odd \(N\), define

\[
G_N(k)=\sum_{x\bmod N}\exp(2\pi i kx^2/N).
\]

The bijection \((x,y)\mapsto(x-y,x+y)\) gives, including \(k=0\),

\[
|G_N(k)|^2
=\sum_{u,v\bmod N}e^{2\pi i kuv/N}
=N\gcd(k,N).
\]

Hence the normalized Fourier-energy law is

\[
\pi_N(k)=\frac{\gcd(k,N)}{S(N)},
\qquad
S(N)=\sum_{d\mid N}d\varphi(N/d).
\]

The normalizer is multiplicative and

\[
S(p^a)=p^{a-1}((a+1)p-a)
=p^a+a\varphi(p^a).
\]

For every odd composite,

\[
\pi_N\{k:1<\gcd(k,N)<N\}
=1-\frac{N+\varphi(N)}{S(N)}
\ge\frac27,
\]

with equality only at \(N=9\).  For distinct odd primes,

\[
S(pq)=(2p-1)(2q-1),
\qquad
\pi_{pq}(\text{proper gcd})
=\frac12-\frac1{2(2p-1)(2q-1)}.
\]

Suppose one uniform classical algorithm, on every odd modulus, returns an
explicit residue from a law within total variation \(1/28\) of \(\pi_N\),
terminates almost surely, and has expected bit and independent fair-bit cost
polynomial in \(\log N\).  On every odd composite a call then returns a
verified proper gcd with probability at least

\[
\frac27-\frac1{28}=\frac14.
\]

Fresh invocations give at most four expected calls per split.  Correlation
between one call's runtime and its own success is harmless because the event
that call \(i\) is reached depends only on earlier calls; the stopped cost is
the corresponding geometric sum of unconditional one-call expectations.
Deterministic primality testing, removal of powers of two, exact verification,
and recursive splitting handle primes, prime powers, repeated factors,
unbalanced inputs, and arbitrary composites.  A factor tree has
\(O(\log N)\) nodes.  This is a complete conditional all-input classical
Las Vegas factoring theorem.

The most immediate implementations remain exponential in input length.  On
balanced distinct semiprimes:

- uniform rejection with acceptance \(\gcd(k,N)/N\) is exact but has
  expected \(N^2/S(N)=\Theta(N)\) proposals;
- direct uniform-residue gcd discovery takes
  \(N/(p+q-2)=\Theta(\sqrt N)\) trials.

For the lazy uniform-proposal independence-Metropolis chain with weight
\(w(x)=\gcd(x,N)\), let

\[
f=\mathbf1_{\{0\}}-\frac N{S(N)}.
\]

Then the exact transition probabilities to and from zero give

\[
Pf=\left(1-\frac{S(N)}{2N^2}\right)f.
\]

Therefore

\[
\operatorname{gap}(P)\le\frac{S(N)}{2N^2},
\]

and the eigenmode's general time scale is \(N^2/S(N)\).  On distinct
semiprimes \(S(N)=\Theta(N)\), so worst-start mixing is \(\Omega(N)\);
more precisely on balanced families

\[
t_{\rm mix}(1/4)\ge(N/2+o(N))\log3.
\]

An initializer that exactly repairs the zero mass can kill this mode, but if
its initial mass on proper-gcd residues is \(o(1)\), entering that class under
uniform proposals still takes \(\Omega(\sqrt N)\) steps for any fixed target
error below \(1/2\).  An explicit initializer with constant proper-gcd mass
is already a constant-success factoring routine.

Exact normalization is not a free shortcut.  On a semiprime,

\[
p+q=\frac{4N+1-S(N)}2,
\]

so exact \(S(N)\) factors by an integer discriminant.  Sampling separately
from prime-power CRT laws likewise assumes the desired factorization.

P41 is a positive amortization theorem at the distribution level, not an
unconditional factoring algorithm.  The exact missing lemma is a factor-free
explicit sampler for \(\pi_N\) with fixed error below \(2/7\) and expected
polynomial bit/fair-bit cost on every odd modulus.  Uniform rejection,
uniform-gcd discovery, and the stated Metropolis chain fail, but nonuniform,
nonlocal, nonreversible, auxiliary-state, positive-combinatorial, and other
direct samplers remain open.

The candidate, initial audit and reconstruction, strengthened re-audit, and
context-free final reconstruction are preserved under
`experiments/F32_quadratic_fourier_energy_kill`,
`experiments/F32_quadratic_fourier_energy_audit`,
`experiments/F32_quadratic_fourier_energy_reconstruct`,
`experiments/F32_quadratic_fourier_energy_reaudit`, and
`experiments/F32_quadratic_fourier_energy_reconstruct2`.

## P42 — closed matching AND/COPY survive, but a universal clean occupancy wire does not

**Status:** promoted.

**Verification record:** both finite matching enumerations, multiplicity-one
decoding, the internal-edge/terminal distinction, the arbitrary-context
four-port support requirement, matching symmetric exchange, every endpoint
case, and the positive-weight/auxiliary-vertex scope passed a clean hostile
audit and a fresh context-free proof-blind reconstruction.  No computation
and no cross-family audit were used.

The bipartite graph with adjacency matrix

\[
\begin{pmatrix}
1&1&0\\
1&1&1\\
1&1&1
\end{pmatrix}
\]

has exactly four perfect matchings.  Marking

\[
L_1R_2,\qquad L_2R_3,\qquad L_3R_1
\]

gives occupancy words

\[
000,\quad010,\quad100,\quad111,
\]

exactly the Boolean relation \(z=xy\), once each.  The six-cycle with
adjacency matrix

\[
\begin{pmatrix}
1&1&0\\
0&1&1\\
1&0&1
\end{pmatrix}
\]

has exactly its two alternating perfect matchings; marking one alternating
triple gives \(000,111\), exactly COPY\(_3\), again once each.  These are
closed internal-edge observables, so P38's direct boundary-deletion parity
and one-hot subcube obstruction do not apply to them.

The immediate modular composition mechanism nevertheless fails.  Removing
two occurrence edges exposes four distinct endpoint ports

\[
B=B_1\mathbin{\dot\cup}B_2,
\qquad |B_1|=|B_2|=2.
\]

A connector that equates the two occupancy bits in **every** surrounding
matching context, while allowing neither mismatches nor partial endpoint
states, must have boundary-deletion support

\[
\{\varnothing,B\}.
\]

For any graph \(H\) with boundary \(B\), however, the feasible deletion
family

\[
\mathcal F_H=\{S\subseteq B:H-S\text{ has a perfect matching}\}
\]

satisfies symmetric exchange:

\[
\forall X,Y\in\mathcal F_H\ \forall e\in X\triangle Y
\exists f\in X\triangle Y,\ f\ne e:
X\triangle\{e,f\}\in\mathcal F_H.
\]

This follows by taking perfect matchings of \(H-X\) and \(H-Y\), following
the alternating path from \(e\) to its other endpoint \(f\), and toggling
that path.  With \(X=\varnothing\) and \(Y=B\), exchange forces a feasible
two-element deletion set, contradicting the proposed two-word support.

Arbitrary internal auxiliary vertices, nonplanarity, graph size, parallel
positive contributions, and nonnegative edge weights do not help: deleting
zero-weight edges reduces positive support to the same unweighted matching
family.  Signed cancellation and merely approximate suppression are outside
the theorem.

P42 closes only a clean, context-independent equality wire on four distinct
occurrence ports.  Contextual filtering of exchange states, projected
auxiliary states, block or heterogeneous encodings, vertex identifications,
fused cells, global multiplicity balancing, and a single interleaved
multiplication-specific graph remain open.  The explicit AND survivor is a
warning not to transfer P38's terminal theorem to arbitrary internal labels.

The candidate, hostile audit, and context-free reconstruction are preserved
under
`experiments/F30_internal_edge_matching_composition_kill`,
`experiments/F30_internal_edge_matching_composition_audit`, and
`experiments/F30_internal_edge_matching_composition_reconstruct`.

## P43 — quadratic Fourier energy is a positive zero-product marginal, but coordinate heat bath is slow

**Status:** promoted.

**Verification record:** the first hostile audit preserved the core theorem
but rejected the prime-power geometry, matching-decoder quantifiers, and
overbroad kernel/start scope.  A full re-audit of that amendment rejected the
origin-ambiguous “chosen axis” equivalence.  After replacing it by exact
\(H/V/O\) local types and making fair-bit rejection explicitly
almost-sure/expected-cost, a fresh whole-artifact hostile re-audit passed.
A new context-free proof-blind reconstruction recovered every theorem and
the complete all-input cost proof without reading any F33 artifact.  Both
historical failed versions are retained.  No computation and no cross-family
audit were used.

For every positive integer \(N\), put

\[
\Omega_N=\{(k,x)\in(\mathbb Z/N\mathbb Z)^2:kx=0\}.
\]

For each \(k\bmod N\),

\[
\#\{x:kx=0\}=\gcd(k,N),
\qquad
|\Omega_N|=S(N):=\sum_{k\bmod N}\gcd(k,N).
\]

Thus the first marginal of the uniform law on \(\Omega_N\) is
\(\gcd(k,N)/S(N)\).  For odd \(N\), the invertible change
\((y-z,y+z)\) gives

\[
\left|\sum_{y\bmod N}e^{2\pi i ky^2/N}\right|^2=N\gcd(k,N),
\]

so this marginal is exactly P41's normalized quadratic Fourier-energy law.
The positive identity itself also holds for even and nonsquarefree \(N\).

The pairs on which neither coordinate exposes a proper gcd are exactly

\[
A_N=
((\mathbb Z/N\mathbb Z)^\times\times\{0\})
\mathbin{\dot\cup}
(\{0\}\times(\mathbb Z/N\mathbb Z)^\times)
\mathbin{\dot\cup}\{(0,0)\},
\]

of size \(2\varphi(N)+1\).  Using

\[
S(p^a)=p^{a-1}((a+1)p-a)
\]

and multiplicativity, the uniform useful-pair mass is at least \(1/3\) on
every odd composite, asymptotically sharply along prime squares.  For
distinct semiprimes it is strictly greater than \(1/2\).

For \(N=pq\), local field points have the three intrinsic types

\[
H=(\mathbb F_r^\times,0),\qquad
V=(0,\mathbb F_r^\times),\qquad O=(0,0).
\]

A proper coordinate gcd occurs exactly when the \(p\)- and \(q\)-types
differ.  This includes all cases involving a local origin.  Prime powers
instead have intermediate valuation strata and are not described by this
three-type CRT rule.

Suppose one uniform algorithm, on every odd modulus, returns an actual pair
in \(\Omega_N\) within TV \(1/12\) of uniform, terminates almost surely, and
has one fixed expected polynomial bit/fair-bit bound.  Each fresh call then
returns a verified proper divisor with probability at least \(1/4\).
Deterministic primality testing, direct even splitting, exact division,
fresh retries, and a factor tree of \(O(\log N)\) nodes give complete
all-input classical Las Vegas factoring.  The stopped-cost argument uses
only independence of a fresh call from the event that it is reached; one
call's runtime may be correlated with its own success.

A sufficient positive-matching hypothesis must be fully uniform: a
polynomial-time builder outputs a polynomial-size bipartite graph, a
uniform deterministic decoder maps every explicit perfect matching to two
\(O(\log N)\)-bit residues in \(\Omega_N\) in polynomial time, and every
pair has one equal positive preimage multiplicity.  P38's almost-uniform
matching sampler would then instantiate the preceding conditional theorem.
No such graph is constructed here.

The exact random-scan coordinate heat bath is implementable without hidden
factors: update one coordinate uniformly from the annihilator of the other.
If \(g=\gcd(y,N)\), sample

\[
jN/g,\qquad 0\le j<g,
\]

by fair-bit rejection.  The update terminates almost surely and has expected
polynomial bit and \(O(\log N)\) fair-bit cost.  The chain is reversible,
irreducible, and aperiodic with uniform stationary law.

Nevertheless, for \(N=pq\), distinct odd primes, from \((1,0)\), with
\(h=p+q-2\), the factor-bearing hitting time has expectation

\[
\Omega(N/h),
\]

and

\[
t_{\rm mix}(1/4)\ge
\left\lfloor\frac{N}{8h}\right\rfloor.
\]

Both are \(\Omega(\sqrt N)\) on fixed-balance semiprime families.  This is
only a worst-start result for the exact random-scan one-coordinate kernel.
Efficient warm starts, block or nonlocal moves, auxiliary/lifted chains,
positive matching encodings, and direct spectral samplers remain open.

The candidate, two historical failed audits, clean final audit, and
context-free reconstruction are preserved under
experiments/F33_quadratic_energy_positive_lift_kill,
experiments/F33_quadratic_energy_positive_lift_audit,
experiments/F33_quadratic_energy_positive_lift_reaudit,
experiments/F33_quadratic_energy_positive_lift_reaudit2, and
experiments/F33_quadratic_energy_positive_lift_reconstruct.

## P44 — zero-product scheme automorphisms cannot desynchronize CRT axes invisibly

**Status:** promoted.

**Verification record:** the hostile audit found no mathematical
counterexample and required only an intrinsic first-jet proof, an exact
division-free circuit model, and narrower all-input wording.  It explicitly
verified every amendment.  A fresh context-free proof-blind reconstruction
independently recovered the field classification, CRT dichotomy, circuit
extraction, invariant, count, characteristic-two case, and nonsquarefree
boundary.  No computation and no cross-family audit were used.

Let \(N=pq\) for distinct primes, \(R=\mathbb Z/N\mathbb Z\), and

\[
A_R=R[K,X]/(KX).
\]

Over any field \(F\), the two minimal primes of
\(F[K,X]/(KX)\) are \((K)\) and \((X)\).  Every \(F\)-algebra automorphism
therefore has exactly one of the forms

\[
(K,X)\mapsto(uK,vX),
\qquad
(K,X)\mapsto(uX,vK),
\qquad u,v\in F^\times.
\]

Over \(R\), every automorphism fixes \((K,X)\), so its intrinsic first jet in
\(A_R/(K,X)^2\) is well-defined.  If its reductions modulo \(p\) and \(q\)
have different preserve/swap orientations, a first-jet entry vanishes in
exactly one field component; taking its ordinary integer gcd with \(N\)
returns \(p\) or \(q\).  If none of the four entry gcds is proper, the
orientations synchronize and the global automorphism is exactly

\[
(K,X)\mapsto(uK,vX)
\quad\text{or}\quad
(K,X)\mapsto(uX,vK)
\]

for units \(u,v\in R^\times\).

The jet is efficiently accessible from an explicit division-free
\(+,-,\times\) straight-line circuit.  Evaluate every gate in
\(A_R/(K,X)^2\), storing \(c+\alpha K+\beta X\); multiplication is

\[
(c,\alpha,\beta)(c',\alpha',\beta')
=(cc',c\alpha'+c'\alpha,c\beta'+c'\beta).
\]

This costs a constant number of ring operations per gate and bit time
polynomial in \(\log N\) plus the encoded circuit length.  A polynomial-time
factoring proposal must uniformly materialize circuits of
\(\operatorname{poly}(\log N)\) encoded size.

On the no-factor branch, every such automorphism preserves

\[
\mathcal A_N=(R^\times,0)\mathbin{\dot\cup}(0,R^\times)
\mathbin{\dot\cup}\{(0,0)\}.
\]

This is pathwise and survives arbitrary random or adaptive selection among
materialized global automorphisms.  Uniform \(\Omega_N\) assigns the
complement mass

\[
\frac{2N-2}{(2p-1)(2q-1)}>\frac12,
\]

so a run started in \(\mathcal A_N\) either exposes a factor in a selected
map's jet or stays more than \(1/2\) from the uniform target.

P44 covers coordinate-algebra automorphisms over distinct semiprimes.  It
does not cover endomorphisms, finite-set-only permutations, auxiliary or
lifted kernels, division/rational circuits, stitched branch-dependent or
opaque maps, independently useful warm starts, or prime powers and other
nonsquarefree bases.  The semiprime theorem refutes an all-input proposal
only when that proposal remains factor-free and automorphism-only in this
exact explicit model on the semiprime subfamily.

The candidate, amendment-verified hostile audit, and context-free
reconstruction are preserved under
experiments/F34_zero_product_automorphism_orientation_kill,
experiments/F34_zero_product_automorphism_orientation_audit, and
experiments/F34_zero_product_automorphism_orientation_reconstruct.

## P45 — low-degree finite-set bijections obey a factor-or-invariant dichotomy

**Status:** promoted.

**Verification record:** the first hostile audit passed the local structural
theorem but rejected the submitted claim that it refuted an accurate sampler:
a sampler may expose a factor, which is success rather than contradiction.
The candidate was materially amended to the unconditional quantitative
factor-or-TV theorem below, with uniform degree, circuit, adaptive-branch,
and expected-cost quantifiers made explicit.  A fresh whole-artifact hostile
re-audit passed that amendment.  A new context-free proof-blind
reconstruction independently recovered the theorem, circuit monitor,
stopped-cost calculation, characteristic-two handling, and exact exclusions.
No computation and no cross-family audit were used.  The historical failed
audit is retained.

Let

\[
N=pq,\qquad R=\mathbb Z/N\mathbb Z,\qquad
\Omega_N=\{(k,x)\in R^2:kx=0\},
\]

where \(p\ne q\) are primes.  Suppose

\[
T=(F,G):\Omega_N\longrightarrow\Omega_N
\]

is induced by polynomials \(F,G\in R[K,X]\) of total degree at most
\(D\), is a bijection of the finite point set, and satisfies

\[
2D<\min(p,q).
\]

CRT makes \(T\) the product of bijections
\(T_r:\Omega_r\to\Omega_r\), where

\[
\Omega_r=\{(a,b)\in\mathbb F_r^2:ab=0\}.
\]

On either source axis, the two coordinate restrictions \(f,g\) obey
\(f(t)g(t)=0\) at every field point.  Their formal product has degree below
\(r\), so root counting makes it the zero polynomial; the domain property of
\(\mathbb F_r[Z]\) then gives \(f=0\) or \(g=0\).  Bijectivity forces the
two source axes to enter distinct target axes and fixes their common origin.
Thus, independently modulo \(p\) and \(q\), the map either preserves the two
axes or swaps them.  This proof does not divide by two and includes
characteristic two whenever the hypotheses are nonvacuous.

If the two local orientations differ, one coefficient of one of

\[
F(K,0),\quad G(K,0),\quad F(0,X),\quad G(0,X)
\]

vanishes modulo exactly one prime.  Its integer gcd with \(N\) is therefore
\(p\) or \(q\).  If none of these coefficient gcds is proper, the
orientations synchronize and \(T\) preserves

\[
\mathcal A_N=
(R^\times\times\{0\})\mathbin{\dot\cup}
(\{0\}\times R^\times)\mathbin{\dot\cup}\{(0,0)\}.
\]

Mixed maps genuinely exist.  For complementary CRT idempotents \(e_p,e_q\),

\[
(K,X)\longmapsto
(e_pK+e_qX,\ e_pX+e_qK)
\]

is a degree-one involution which preserves axes modulo one prime and swaps
them modulo the other.  Its coefficients expose the factors.  Hence the
theorem is a factor-or-invariant reduction, not a nonexistence theorem for
accurate samplers.

The reduction is algorithmic for explicit division-free straight-line
circuits.  Given a public numeric cap \(D\), evaluate the circuit after the
two axis substitutions in

\[
R[Z]/(Z^{D+1}).
\]

The quotient map is a ring homomorphism, so arbitrarily high intermediate
degrees and cancellations do not corrupt the final low-degree coefficients.
For a circuit with \(g\) gates the two evaluations cost \(O(gD^2)\) ring
operations under ordinary truncated convolution.  A proposed uniform run
must use one fixed public bound \(D_N\le P(n)\), where \(P\) is independent
of the input, history, randomness, move, and stopping time; every materialized
branch circuit must have exact formal outputs below that cap and must itself
be a global bijection of all \(\Omega_N\).  These are semantic promises, not
properties certified by the monitor.  If the expected total encoded circuit
length is at most another fixed polynomial \(Q(n)\), the expected total
monitoring overhead is polynomial.  A one-time gcd scan through
\(2,\ldots,2D_N\) either finds a small factor or certifies the strict degree
condition without knowing \(p,q\).

For an almost-surely finite adaptive run, inspect both initializer-coordinate
gcds and all restriction coefficients of each realized branch circuit.  Let
\(H\) be the event that any check finds a proper factor, let \(Y\) be the
unmodified run's output, and let \(\mu\) be its **unconditional** terminal
law.  On \(H^c\), the initializer lies in \(\mathcal A_N\), every realized
move synchronizes, and pathwise induction keeps \(Y\) in \(\mathcal A_N\).
With \(B_N=\Omega_N\setminus\mathcal A_N\), therefore

\[
\{Y\in B_N\}\subseteq H.
\]

The exact counts are

\[
|\Omega_N|=(2p-1)(2q-1),\qquad
|B_N|=2N-2,
\]

so, for uniform \(\pi_N\) on \(\Omega_N\),

\[
\rho_N:=\pi_N(B_N)
=\frac{2N-2}{(2p-1)(2q-1)}>\frac12.
\]

Consequently

\[
\boxed{
\Pr(H)\ge\mu(B_N)
\ge\rho_N-d_{\rm TV}(\mu,\pi_N).}
\]

A genuinely factor-free run is therefore more than \(1/2\) from uniform.
Conversely, fresh repeatable runs whose TV error is at most
\(1/2-1/Q_0(n)\) for one fixed polynomial \(Q_0\), and whose full expected
cost is uniformly polynomial, yield a Las Vegas splitter for every distinct
semiprime by stopping at the first monitored factor.  The expected cost is
the one-run expectation divided by the inverse-polynomial success lower
bound; a merely pointwise inequality \(\delta_N<1/2\) is insufficient.
This is not by itself a complete all-input factoring theorem.

P45 does not cover characteristic-scale or succinctly high-degree point
permutations, noninvertible or stochastic moves, auxiliary/lifted kernels,
rational, division, opaque, or nonmaterialized piecewise maps, useful warm
starts whose construction is not charged, prime powers, or general
nonsquarefree bases.  State-dependent selection is covered only when every
materialized branch is itself a promised global low-degree bijection.  These
are the exact reopen conditions.

The candidate, historical failed audit, amended hostile re-audit, and
context-free reconstruction are preserved under
experiments/F35_low_degree_zero_product_bijection_kill,
experiments/F35_low_degree_zero_product_bijection_audit,
experiments/F35_low_degree_zero_product_bijection_reaudit, and
experiments/F35_low_degree_zero_product_bijection_reconstruct.
