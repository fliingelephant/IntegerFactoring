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
1146^{2952}=1,\quad
1146^{1476}=2952,\quad
1146^{984}=800,\quad
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
N\equiv48,\qquad48^{134}=-1,\qquad48^4=239,
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

draw independent uniform \(a_1,\ldots,a_K\) modulo \(N\), and define

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

## P46 — the natural propagated multiplier cell is outside every independent-leg matchgate orbit

**Status:** promoted.

**Verification record:** a fresh hostile proof audit passed the complete
candidate as written.  A context-free proof-blind reconstruction independently
recovered the shifted-add recurrence, planar rotation system, rank computation,
degenerate-chart pure-spinor lemma, sign boundary, and exact scope.  No
computation and no cross-family audit were used.

Over a characteristic-zero field, define the eight-leg Boolean signature

\[
C(x_L,x_R,y_U,y_D,a,c,s,d)
=\mathbf 1[x_L=x_R]\mathbf 1[y_U=y_D]
 \mathbf 1[a+c+x_Ly_U=s+2d].
\]

Copies \(C_{j,i}\), \(0\le j,i<n\), form an exact planar shifted-add
multiplier.  Propagate \(x_i\) down column \(i\), propagate \(y_j\) across
row \(j\), connect \(d_{j,i}\) to \(c_{j,i+1}\), connect
\(s_{j,i}\) to \(a_{j+1,i-1}\) for \(i\ge1\), and connect each row's
final-column carry \(d_{j,n-1}\) to \(a_{j+1,n-1}\).  Pin
\(a_{0,i}=c_{j,0}=0\).  If

\[
A_j=\sum_{i=0}^{n-1}2^i a_{j,i},
\qquad X=\sum_{i=0}^{n-1}2^i x_i,
\]

then summing one row's cell equations gives

\[
A_j+Xy_j=s_{j,0}+2A_{j+1}.
\]

Telescoping over the rows shows that

\[
XY=
\sum_{j=0}^{n-2}2^j s_{j,0}
+\sum_{i=0}^{n-1}2^{n-1+i}s_{n-1,i}
+2^{2n-1}d_{n-1,n-1}.
\]

Thus the displayed boundary outputs have consecutive weights
\(0,\ldots,2n-1\).  Given \(x,y\), every carry and sum is forced by the
unique binary decomposition of \(a+c+xy\in\{0,1,2,3\}\), so the pinned
network has exactly one internal assignment per ordered factor witness.
Factor-prefix restrictions are boundary unaries and retain this
multiplicity-one semantics.

Placing cell \((j,i)\) at \((u,v)=(i+j,j)\) uses horizontal, vertical, and
one diagonal family of lattice edges; parallel propagation/carry edges fit in
disjoint thin lanes.  At every cell the incoming legs

\[
I=(x_L,y_U,a,c)
\]

occupy one local boundary arc and the outgoing legs

\[
O=(x_R,y_D,s,d)
\]

the complementary arc.  Constants, factor bits, prefix pins, target bits,
and neutral terminal unaries all attach in the outer face.

For any nonzero planar matchgate signature, the ordinary coefficient
flattening across two complementary contiguous cyclic arcs has rank \(2^r\)
for some \(r\).  This includes every degenerate chart and both parities.
Indeed, choose a nonzero coefficient and apply the needed particle-hole
operators

\[
\gamma_i=e_i\wedge+\iota_{e_i}.
\]

Each \(\gamma_i\) is a tensor-product Pauli string, preserves flattening
rank, and carries pure spinors to pure spinors; their product moves the chosen
coefficient to the even vacuum chart.  There the spinor is
\(\lambda\exp(\omega)\).  For a contiguous split write

\[
\omega=\omega_I+\omega_O+\omega_{IO}.
\]

The first two terms act by invertible row and column maps.  If the cross-form
has rank \(r\), separate changes of basis put it into
\(\sum_{k=1}^r u_k\wedge v_k\); expanding its exponential gives a diagonal
pairing indexed by all \(2^r\) subsets.  Cyclic rotations across a contiguous
cut contribute only rank-preserving row or column signs.  Contiguity is
essential: the pure spinor

\[
\exp(e_1\wedge e_2+e_3\wedge e_4+e_1\wedge e_4+e_2\wedge e_3)
\]

has ordinary \(\{1,3\}\mid\{2,4\}\) flattening

\[
\begin{pmatrix}
1&0&0&0\\
0&1&1&0\\
0&1&1&0\\
0&0&0&2
\end{pmatrix},
\]

of rank \(3\) over characteristic zero.

Finally, propagation makes the \(I\mid O\) flattening of \(C\) a direct sum
of four blocks indexed by \((x,y)\).  In each block the four \((a,c)\) rows
select exactly three distinct \((s,d)\) columns, so every block has rank
\(3\) and

\[
\operatorname{rank}\operatorname{Flat}_{I\mid O}(C)=12.
\]

Independent invertible \(2\times2\) transformations on the eight legs only
left- and right-multiply this flattening by invertible Kronecker products.
Because \(12\) is not a power of two, no such transformations make this cell
a matchgate.  Contraction-compatible shared-edge gauges are a specialization
and cannot repair the local failure.

P46 closes only the displayed natural scalar-Boolean cell in this planar port
order.  It does not close larger fused blocks, other rotations or encodings,
projected auxiliary states, global Pfaffian identities, modular
constructions, or non-matchgate exact contraction.  It is an auxiliary
obstruction, not a factoring algorithm.

The candidate, clean hostile audit, and context-free reconstruction are
preserved under experiments/F36_fused_matchgate_cell_kill,
experiments/F36_fused_matchgate_cell_audit, and
experiments/F36_fused_matchgate_cell_reconstruct.

## P47 — smooth multiplier clouds lose to their own Fermat scale

**Status:** promoted.

**Verification record:** the first hostile audit found no error in either
core obstruction but required the continuous surrogate, target-independence,
uniform cost quantifiers, and direct useful-square/gcd scope to be literal.
The amended whole artifact passed a fresh hostile re-audit.  A context-free
proof-blind reconstruction independently recovered the exact gap, coverage
bound, divisor estimate, LCM example, prime-ratio counterfamily, constants,
and exclusions.  No computation and no cross-family audit were used.

Let \(N=pq\) for distinct odd primes \(p<q\), and let a positive multiplier
\(k\) have a supplied complete factorization.  If \(\gcd(k,N)>1\), that gcd
or the supplied prime list already exposes a factor.  When \(\gcd(k,N)=1\),
every factor pair of \(kN\) is, up to exchange, either

\[
(cp,dq),\qquad(cq,dp),\qquad\text{or}\qquad(cN,d),
\qquad cd=k.
\]

The first two allocate \(p,q\) to opposite sides and have useful
intersections \(p,q\) with \(N\); the last has only the trivial/full
intersections \(1,N\).  Fermat represents a pair only when its two factors
have the same parity, equivalently \(c\equiv d\pmod2\).

For a useful allocation \(X=cp,Y=dq\), put

\[
r=\frac qp,qquad M=kN,qquad
\lambda=\log\frac{c/d}{r}.
\]

Its exact real gap above the Fermat square-root threshold is

\[
G=\sqrt{kN}\bigl(\cosh(\lambda/2)-1\bigr)
=\frac{(cp-dq)^2}{2(\sqrt{cp}+\sqrt{dq})^2}.
\]

If \(\theta_M=\lceil\sqrt M\rceil-\sqrt M\), its exact integer scan index is
\(j=G-\theta_M\).  Hence a parity-compatible pair occurs through index
\(T\) exactly when

\[
|\lambda|
\leq2\operatorname{arcosh}
\left(1+\frac{T+\theta_M}{\sqrt{kN}}\right),
\]

and necessarily

\[
|\lambda|
\leq2\sqrt2\,\frac{\sqrt{T+1}}{(kN)^{1/4}}.
\tag{47.1}
\]

This yields a precise continuous obstruction.  Fix \(S>0\), a log-ratio
interval \(I\) of length \(\ell\), target-independent multipliers \(k_i\),
and caps \(T_i\).  Define

\[
R_i=2\sqrt2\,\frac{\sqrt{T_i+1}}{(k_iS)^{1/4}}
\]

and

\[
\mathcal C=
\bigcup_i\ \bigcup_{c\mid k_i}
[2\log c-\log k_i-R_i,\ 2\log c-\log k_i+R_i].
\]

Every actual useful pair for an integer \(N\ge S\) found through its cap has
\(\log(q/p)\in\mathcal C\).  Summing the lengths of all necessary windows
gives

\[
\operatorname{meas}(I\cap\mathcal C)
\leq4\sqrt2\,S^{-1/4}
\sum_i\tau(k_i)k_i^{-1/4}\sqrt{T_i+1}.
\tag{47.2}
\]

For every fixed \(\varepsilon>0\),

\[
\tau(k)\le C_\varepsilon k^\varepsilon.
\]

Indeed, for primes \(s\ge2^{1/\varepsilon}\),
\(e+1\le2^e\le s^{\varepsilon e}\); each of the finitely many smaller
primes contributes the finite supremum
\(\sup_e(e+1)s^{-\varepsilon e}\).  Taking \(\varepsilon=1/8\) makes
\(\tau(k)k^{-1/4}\) uniformly bounded.  Thus one target-independent list of
uniformly polynomial cardinality and uniformly polynomial scan caps covers
only \(2^{-\Theta(n)}\operatorname{poly}(n)\) log measure when
\(S=2^{\Theta(n)}\), regardless of multiplier magnitude.  It cannot cover a
fixed positive-length balanced interval.  This is a continuous
necessary-window theorem, not a lower bound for a cloud chosen from the
particular input ratio.

The natural dense construction illustrates the same loss.  With

\[
L_m=\operatorname{lcm}(1,\ldots,m),\qquad k_m=L_m^2,
\]

the allocations

\[
c=L_m\frac ab,\qquad d=L_m\frac ba
\]

realize \(c/d=(a/b)^2\) for \(a,b\le m\).  Taking
\(b=\lfloor(m-2)/\sqrt2\rfloor\) and
\(a=\operatorname{round}(b\sqrt r)\) gives a uniform \(O(1/m)\) log mesh on
\(1\le r\le2\).  But \(\log L_m=\Theta(m)\), so
\(k_m^{-1/4}=\exp(-\Theta(m))\); even all \(\tau(k_m)\) allocations cannot
offset the required Fermat resolution in (47.2).

There is also an actual discrete obstruction which permits input-dependent
selection.  Fix functions

\[
B:\mathbb N\to\mathbb R_{\ge0},\qquad
T:\mathbb N\to\mathbb Z_{\ge0},
\]

with \(B(n)/\sqrt n\to0\) and \(T\) bounded by one fixed polynomial.  The
de la Vallée Poussin error term

\[
\pi(x)=\operatorname{Li}(x)+O(xe^{-a\sqrt{\log x}})
\]

puts a prime in every sufficiently large symmetric interval of relative
radius \(e^{-b\sqrt{\log x}}\) for a suitable \(b>0\).  Taking the interval
around \(\sqrt2p\), for arbitrarily large primes \(p\), produces primes
\(q\) with

\[
p<q<2p,qquad
\left|\frac qp-\sqrt2\right|\le e^{-\gamma\sqrt n},
\qquad n=\lceil\log_2(pq+1)\rceil.
\]

For all sufficiently large members of this infinite family, writing
\(K=2^{B(n)}\) gives

\[
\left|\frac qp-\sqrt2\right|\le\frac1{6K^2}.
\]

For every \(cd=k\le K\), quadratic irrationality gives

\[
|c-d\sqrt2|
=\frac{|c^2-2d^2|}{c+d\sqrt2}>\frac1{3k}.
\]

The prime-ratio error therefore yields, simultaneously for every such
\(k,c,d\),

\[
|c-d(q/p)|>\frac1{6k},
\]

and the same estimate after exchanging \(c,d\).  Both useful orientations
then satisfy

\[
G>\frac{p}{432k^3}>T(n)+1
\]

eventually, because \(\log p=\Theta(n)\) whereas
\(\log k=o(\sqrt n)\).  Every compatible useful pair has index greater than
\(T(n)\), and every incompatible one is absent from the Fermat scan.  This
holds before an algorithm selects \(k\), so it defeats every deterministic or
random input-dependent choice, and every list, within the stated size range.

P47 therefore closes target-independent continuous divisor clouds and the
direct useful-square/factor-pair/gcd method with adaptive coprime
\(o(\sqrt n)\)-bit multipliers on the constructed balanced family.  It does
not close \(\Omega(\sqrt n)\)-bit adaptive multipliers, concentration on the
actual discrete prime ratio, joint decoding of nonsquare values or complete
scan transcripts, other metric observables, non-gcd extraction, or general
factoring.  A represented polynomial-time scan must also charge multiplier
and supplied-factorization generation, total encoding length, every scan
step, arithmetic operands, and gcds.  Only an every-composite Las Vegas
splitter with one uniform expected polynomial bound would recurse to complete
factorization; P47 supplies no such splitter.

The candidate, historical amendment audit, clean whole-artifact re-audit,
and context-free reconstruction are preserved under
experiments/F37_smooth_multiplier_cloud_kill,
experiments/F37_smooth_multiplier_cloud_audit,
experiments/F37_smooth_multiplier_cloud_reaudit, and
experiments/F37_smooth_multiplier_cloud_reconstruct.

## P48 — every horizontal propagated-cell strip stays outside the matchgate orbit

**Status:** promoted.

**Verification record:** the first hostile audit preserved the tensor, topology,
and rank theorem but required the pure-spinor recap to distinguish the two local
two-forms from the cross-form.  The amended whole artifact passed a fresh hostile
re-audit.  A context-free proof-blind reconstruction independently recovered the
fused relation, multiplicity one, planar cyclic cut, exact rank, all-chart
pure-spinor obstruction, gauge invariance, and scope.  No computation and no
cross-family audit were used.

For (L\ge1), horizontally fuse (L) copies of the P46 Boolean cell

\[
C(x_i^-,x_i^+,y_i,y_{i+1},a_i,c_i,s_i,c_{i+1})
=\mathbf1[x_i^-=x_i^+]\mathbf1[y_i=y_{i+1}]
 \mathbf1[a_i+c_i+x_i^-y_i=s_i+2c_{i+1}].
\]

Contract only (y_1,\ldots,y_{L-1}) and
(c_1,\ldots,c_{L-1}).  All equalities inside the indicators are ordinary
integer Boolean equalities; only their truth values are embedded in a field.
Put

\[
X=\sum_{i=0}^{L-1}2^ix_i^-,\qquad
A=\sum_{i=0}^{L-1}2^ia_i,\qquad
S=\sum_{i=0}^{L-1}2^is_i.
\]

The resulting tensor is exactly

\[
\boxed{
\mathcal S_L=
\left(\prod_{i=0}^{L-1}\mathbf1[x_i^-=x_i^+]\right)
\mathbf1[y_0=y_L]
\mathbf1[A+y_0X+c_0=S+2^Lc_L].}
\tag{48.1}
\]

Indeed, a nonzero summand propagates every (x_i), makes all (y_i) equal,
and satisfies

\[
a_i+c_i+x_i^-y_0=s_i+2c_{i+1}.
\]

Multiplication by (2^i) and summation cancels every internal carry and
gives the last indicator in (48.1).  Conversely, start from the exposed
(c_0) and apply the ordinary full-adder recurrence.  Each input sum lies in
({0,1,2,3}), so it uniquely determines the next Boolean output bit and
carry.  The integer (A+y_0X+c_0) lies in
([0,2^{L+1}-1]), and ((s_0,\ldots,s_{L-1},c_L)) is its unique
((L+1))-bit representation.  Equation (48.1) therefore forces the
recursively generated outputs and final carry.  Every allowed external word
has exactly one internal (y)- and carry assignment, including the unique
empty assignment when (L=1).  Thus every tensor entry is literally (0) or
(1) over every field.

There is an explicit planar rotation with clockwise port order on cell (i)

\[
x_i^-,a_i,y_{i+1},c_{i+1},x_i^+,s_i,c_i,y_i.
\tag{48.2}
\]

Place the cells left to right, joining (y) in a lane above the parallel
carry lane.  The two ports are consecutive on both facing disk boundaries,
their endpoint orders agree, and the lens between the two wires contains no
external port.  The outer face encounters the top ports (x_i^-,a_i), the
right endpoint (y_L,c_L), the bottom ports (x_i^+,s_i), and the left
endpoint (y_0,c_0) cyclically.  Hence

\[
I_L=\{x_i^-\}_i\cup\{a_i\}_i\cup\{y_0,c_0\}
\]

is one cyclic boundary arc, using the wrap between the left and top groups,
and

\[
O_L=\{x_i^+\}_i\cup\{s_i\}_i\cup\{y_L,c_L\}
\]

is its complementary arc.  This also holds for (L=1), when there is no
internal lens.

Flatten (48.1) across (I_L\mid O_L).  Propagation makes it a direct sum of
(2^{L+1}) blocks indexed by
((x_0,\ldots,x_{L-1},y)).  Fix one block and put (Q=yX).  Its rows are
indexed by ((A,c_0)), its columns by the bijective integer label

\[
W=S+2^Lc_L\in\{0,\ldots,2^{L+1}-1\},
\]

and each row is the standard basis row supported at

\[
W=Q+A+c_0.
\]

As (A\in[0,2^L-1]) and (c_0\in\{0,1\}) vary, the used columns are
exactly

\[
Q,Q+1,\ldots,Q+2^L.
\]

They are all legal because (0\le Q\le2^L-1).  Distinct standard basis rows
are independent over every field, so each block has rank (2^L+1), and

\[
\boxed{
\operatorname{rank}\operatorname{Flat}_{I_L\mid O_L}(\mathcal S_L)
=2^{L+1}(2^L+1).}
\tag{48.3}
\]

For (L=1), this is (12), recovering P46.  For every (L\ge1), the
factor (2^L+1) is odd and greater than one, so (48.3) is not a power of
two.

P46 proves the needed all-chart theorem: over a characteristic-zero field,
every nonzero matchgate or parity-homogeneous pure-spinor signature has rank
(2^r) across complementary contiguous cyclic arcs.  Briefly, particle-hole
Clifford toggles move an arbitrary nonzero coefficient to the vacuum chart
without changing flattening rank.  There the spinor is
(\lambda\exp(\omega_I+\omega_O+\omega_{IO})).  Wedge multiplication by
(\exp(\omega_I)) and (\exp(\omega_O)) gives invertible row and column
maps, while a rank-(r) cross-form reduces to (r) paired terms whose subset
expansion has rank (2^r).  Cyclic recutting contributes only invertible
parity signs.  The all-zero assignment makes (\mathcal S_L\ne0), so
(48.3) contradicts this necessary matchgate rank form.

Finally, arbitrary independent (\mathrm{GL}_2) transformations on exposed
input and output legs left- and right-multiply the flattening by invertible
Kronecker products.  Its rank is unchanged.  Contraction-compatible dual
gauges on an internal shared edge cancel, leaving only the already covered
external gauges.  Therefore no such gauges put any finite horizontal strip
in the characteristic-zero matchgate orbit in the inherited port order.

P48 closes only horizontal fusion of the displayed scalar-Boolean cells,
with shared (y) and carry legs contracted and all (x), accumulator, and
sum legs exposed.  It does not close genuinely two-dimensional blocks,
alternate rotations or encodings, auxiliary or packed states, noninvertible
projections, asymmetric cells, global Pfaffian identities, independently
justified modular methods, or non-matchgate contraction algorithms.  It is
not a contraction lower bound and supplies no factoring algorithm.

The candidate, historical amendment audit, clean fresh re-audit, and
context-free reconstruction are preserved under
experiments/F38_horizontal_matchgate_strip_kill,
experiments/F38_horizontal_matchgate_strip_audit,
experiments/F38_horizontal_matchgate_strip_reaudit, and
experiments/F38_horizontal_matchgate_strip_reconstruct.

## P49 — modular-inverse clouds are Fourier-flat at every common-gcd-free mode

**Status:** verifier-backed narrow obstruction. The proof-only candidate
passed a hostile audit after mandatory scope amendments and a fresh
context-free reconstruction. No computation or cross-family audit was used.

Let \(N=pq\) with distinct odd primes and let

\[
 \widehat\mu_N(a,b)=\frac1{\varphi(N)}
 \sum_{u\in(\mathbb Z/N\mathbb Z)^\times}
 e_N(au+bu^{-1}).
\]

Choose \(\bar q_p,\bar p_q\) with

\[
 \bar q_pq\equiv1\pmod p,\qquad
 \bar p_qp\equiv1\pmod q.
\]

Coordinatewise inversion of units under CRT gives the exact factorization

\[
 \boxed{
 \widehat\mu_N(a,b)=
 \widehat\mu_p(\bar q_pa,\bar q_pb)
 \widehat\mu_q(\bar p_qa,\bar p_qb).}
 \tag{49.1}
\]

For a prime \(r\), the unnormalized local sum has the complete trichotomy

\[
 S_r(A,B)=
 \begin{cases}
 r-1,&A=B=0 \quad(Z),\\
 -1,&\text{exactly one of }A,B\text{ is zero}\quad(D),\\
 K_r(A,B),&AB\ne0\quad(K),
 \end{cases}
 \qquad |K_r(A,B)|\le2\sqrt r.
 \tag{49.2}
\]

Thus, for every nonzero frequency with
\(d=\gcd(a,b,N)=1\), neither component is of type \(Z\), and

\[
 \boxed{
 |\widehat\mu_N(a,b)|
 \le \delta_N:=\frac{4\sqrt N}{\varphi(N)}.}
 \tag{49.3}
\]

The zero character has coefficient \(1\) under both the cloud and the
uniform-grid baseline. The restriction in (49.3) is sharp in scope. Prime
orthogonality gives

\[
 \sum_{c\in\mathbb F_r}|K_r(1,c)|^2=r(r-1),
\]

so some \(c\ne0\) satisfies
\(|K_r(1,c)|^2\ge r-1/(r-1)\). A frequency \((p,pc)\) therefore has
\(p\)-type \(Z\), \(q\)-type \(K\), and normalized size
\(q^{-1/2+o(1)}=N^{-1/4+o(1)}\) on balanced semiprimes. But its displayed
common gcd is already \(p\). Separate screens
\(\gcd(a,N)\) and \(\gcd(b,N)\) can expose still more cross-degenerate modes;
accordingly, “publicly factor-free” means that none of these screens is a
nontrivial proper divisor, whereas (49.3) needs only the weaker common-gcd
condition.

After combining duplicate modes and removing the zero character, every
finite trigonometric observable

\[
 F(x,y)=\sum_j c_j e_N(a_jx+b_jy),
 \qquad A=\sum_j|c_j|,
\]

whose common-gcd screens all pass obeys

\[
 \boxed{
 |\mathbb E_{\mu_N}F-\mathbb E_{\lambda_N}F|
 \le A\delta_N.}
 \tag{49.4}
\]

This is an \(\ell^1\)-linear expectation theorem, not a theorem about
nonlinear processing of the vector of character values.

The larger hidden divisible modes also do not spoil coarse rectangular
equidistribution. Put

\[
 \alpha_r=\frac{2\sqrt r}{r-1},\qquad
 L(H)=2\sum_{k\le H}\frac1k,\qquad
 M_r(H)=\frac2r\sum_{k\le H/r}\frac1k.
\]

The two-dimensional Erdős--Turán--Koksma inequality and (49.2) give, for
\(1\le H<N\),

\[
\begin{aligned}
D_N^*\le C\Big[&\frac1{H+1}
+\alpha_p\alpha_q((1+L(H))^2-1)\\
&+\alpha_p((1+M_q(H))^2-1)
+\alpha_q((1+M_p(H))^2-1)\Big].
\end{aligned}
\tag{49.5}
\]

Indeed, the indicator that both coordinates are divisible by \(r\) has
reciprocal Fourier weight \((1+M_r(H))^2-1\); the simultaneous \(p\)- and
\(q\)-indicator occurs only at the excluded zero frequency. Taking
\(H=N-1\) yields, on every fixed balanced semiprime family,

\[
 \boxed{D_N^*=O(N^{-1/2}\log^2N).}
 \tag{49.6}
\]

Hence every half-open axis-parallel rectangle has mass error at most
\(4D_N^*\). A list of \(B\) such rectangles has summed absolute error at
most \(4BD_N^*\); only when the rectangles form a disjoint exhaustive
partition are the two bin vectors probability laws and
\(d_{\rm TV}\le2BD_N^*\).

Finally, for one fixed screened character
\(X=e_N(au+bu^{-1})\), mean \(\theta\ne0\), and \(m\) iid samples,

\[
 \boxed{
 \mathbb E|\overline X_m-\theta|^2
 =\frac{1-|\theta|^2}{m}.}
 \tag{49.7}
\]

Relative RMSE at most \(\eta\) therefore needs
\(m\ge(1-|\theta|^2)/(\eta^2|\theta|^2)=N^{1-o(1)}\) under (49.3).
A complex fourth-moment expansion and Paley--Zygmund give absolute constants
\(c_0,c_1>0\) such that

\[
 \Pr(|\overline X_m-\theta|\ge c_1m^{-1/2})\ge c_0.
\]

Consequently, success confidence greater than \(1-c_0\), not an arbitrary
unnamed fixed confidence, requires
\(m\ge c_1^2/(\eta^2|\theta|^2)\). One regular fixed rectangular-bin
frequency has the analogous Bernoulli MSE and sufficiently-high-absolute-
confidence conclusion, provided its area and complementary area are bounded
below as stated in the reconstructed theorem.

P49 is distributional and statistic-specific. It is not a factoring lower
bound, a computational-indistinguishability claim, or a proof that bare
\(N\) cannot manufacture a metric hint. It leaves open Fourier-dense or
nonlinear statistics, implicit hidden-frequency recovery, adaptive or
correlated sources, curved/diagonal bins, exact evaluation of tiny biases,
noisy ACD/HNP/Coppersmith decoding, and noninvertible or dissipative
dynamics. The candidate, hostile audit, and context-free reconstruction are
preserved under experiments/F39_inverse_metric_cloud_kill,
experiments/F39_inverse_metric_cloud_audit, and
experiments/F39_inverse_metric_cloud_reconstruct.

## P50 — bounded-degree fibre completions are diffuse unless a line map degenerates, and synchronized constant degenerations exist

**Status:** verifier-backed narrow classification and counterexample. The
proof-only candidate required a mathematical amendment in its first hostile
audit, passed a fresh whole-artifact re-audit after correction, and was then
reconstructed from the statement and key ideas by a context-free agent. No
computation or cross-family audit was used.

Let \(N=pq\) for distinct odd primes, put
\(A=\mathbb Z/N\mathbb Z\), and let

\[
 K=A[i],\qquad i^2=-1,qquad n(x+yi)=x^2+y^2.
\]

Fix \(R\in A^\times\). A source and completion satisfy

\[
 u=x+yi,\quad n(u)=-R,qquad
 c=z+wi,\quad n(c)=R.
\]

In the quaternion algebra with \(i^2=j^2=-1\) and \(ji=-ij\), the element
\(\beta=u+cj\) has norm zero. Over either CRT field
\(k=\mathbb F_r\), \(r\in\{p,q\}\), its nonzero split-matrix image has rank
one and therefore has intrinsic image and row lines in \(\mathbb P^1(k)\).
Write \(\chi_r=(-1/r)\). The affine source conic has exactly

\[
 |C_r^-|=#\{(x,y):x^2+y^2=-R\}=r-\chi_r.
\tag{50.1}
\]

Consider a rational completion branch represented on the projective source
conic

\[
 \bar C^-:X^2+Y^2=-RT^2
\]

by common-degree homogeneous forms \((Z,W,H)\) of degree \(d\le D\), with
\(Z^2+W^2=RH^2\) in the function field. Clearing denominators gives

\[
 \widetilde\beta=(X+iY)H+T(Z+iW)j.
\tag{50.2}
\]

Its four matrix coordinates are sections of
\(\mathcal O_{\bar C^-}(d+1)\). After cancelling their common base divisor,
the rational map extends across poles, base points, and points at infinity to
the rank-one Segre quadric

\[
 Q\simeq\mathbb P^1_{\rm image}\times\mathbb P^1_{\rm row}.
\]

Because \(\mathcal O_Q(1)=\mathcal O_Q(1,1)\) and
\(\deg\mathcal O_{\bar C^-}(1)=2\), the two factor maps obey

\[
 \deg L_{\rm image}^*\mathcal O(1)
 +\deg L_{\rm row}^*\mathcal O(1)
 \le 2(d+1).
\tag{50.3}
\]

Hence every nonconstant intrinsic row or image map has, with multiplicity,
at most

\[
 \boxed{2(D+1)}
\tag{50.4}
\]

preimages of any fixed local line. This remains true for inseparable maps.
If a current-point selector may choose among \(B\) displayed branches, each
locally nonconstant for the line under test, then for every fixed line
\(\ell\),

\[
 \boxed{
 \Pr[\text{no factor is output and the selected line is }\ell]
 \le {2B(D+1)\over r-\chi_r}.}
\tag{50.5}
\]

This is an unconditional output subprobability, not a probability conditioned
on the no-factor event. A denominator that is a nonunit is already a factor
ticket and is accounted for outside the displayed output.

The same argument is intrinsic for an algebraic graph component
\(\Gamma_i\subset\bar C^-\times\bar C^+\). On its normalization let

\[
 \delta_i=\deg\nu_i^*\mathcal O(1,1).
\]

Every nonconstant row or image map on that component has fibres of size at
most \(\delta_i\); selectable components contribute at most
\(\sum_i\delta_i\). The exact exception is a component dominant over the
source on which the tested line map is constant. There the relevant section
vanishes identically, so a point-count bound is impossible. Vertical
components instead lie over a finite exceptional source set.

The atom theorem supports fixed targets, past-measurable targets tested on a
fresh independent source call, fresh-call collisions, and finite menus after
the corresponding union bound. It gives no same-source comparison theorem:
two nonconstant maps can agree identically while both marginals are diffuse.

There is also a precise public detector for one explicit representation. If
a composed projective map is supplied as homogeneous binary forms

\[
 [P(S,T):Q(S,T)]
\tag{50.6}
\]

of declared degree \(d\), let \(G_r=\gcd(P_r,Q_r)\). Its reduced local
degree is \(d_r=d-\deg G_r\). If \(d_p\ne d_q\), the homogeneous
subresultant sequence has an index whose coefficients vanish in exactly one
CRT field; the gcd of such a coefficient with \(N\) is a proper factor.
Zero-pair and one-sided-zero-form cases are exposed directly by coefficient
gcds. Fraction-free subresultants give polynomial bit complexity. This
statement is only for explicitly supplied binary forms; it does not assert
that an implicit graph or selector admits a semantics-preserving polynomial
eliminant.

Uniform sampling from either conic fibre is nevertheless exact once one
public point \((a,b)\), \(a^2+b^2=\kappa\), is known. For uniform
\((s,t)\in A^2\), set

\[
\begin{aligned}
 X&=a(s^2-t^2)-2bst,\\
 Y&=b(s^2-t^2)+2ast,\\
 H&=s^2+t^2.
\end{aligned}
\tag{50.7}
\]

If \(\gcd(H,N)=1\), return \((X/H,Y/H)\); if the gcd is proper, return the
factor; if it is \(N\), reject and resample. Conditional on direct
acceptance the returned point is exactly uniform, and the exact direct-
acceptance probability is

\[
 \boxed{
 \prod_{r\in\{p,q\}}
 { (r-1)(r-\chi_r)\over r^2}.}
\tag{50.8}
\]

Indeed each affine point has \(r-1\) nonzero homogeneous parameter
representatives over \(\mathbb F_r\), and CRT multiplies both counts and
preimage multiplicities.

Most importantly, the diffuse-or-visible hope fails at the constant-component
boundary. From one public source/completion pair \((u_0,c_0)\), define

\[
 h=u_0^{-1}c_0,qquad n(h)=-1.
\tag{50.9}
\]

For every source \(u\), the completion \(c=uh\) gives

\[
 \beta=u(1+hj),
\tag{50.10}
\]

so left multiplication by the invertible local matrix of \(u\) leaves a
constant row line at both CRT primes. Dually, \(c=h\bar u\) gives

\[
 \beta=(1+hj)u,
\tag{50.11}
\]

and a constant image line at both primes. These are explicit
source-dominating constant graph components, not merely abstract exceptional
cases.

For a concrete certificate, take

\[
 N=21,\quad R=1,\quad u_0=2-4i,\quad c_0=-1,\quad h=2+4i.
\]

Then \(n(u_0)=-1\), \(n(c_0)=1\), and \(u_0h=c_0\) modulo \(21\). With
the split representation determined by \(s=2,t=4\), the fixed factor
\(\alpha=1+hj=1+2j+4ij\) satisfies

\[
 \rho(u\alpha)=
 \begin{pmatrix}0&2y\\0&2x\end{pmatrix}
\tag{50.12}
\]

for \(u=x+yi\), hence has constant row \([0:1]\) modulo both \(3\) and
\(7\), with no coefficient factor forced.

The synchronized constant bias is neutral only for the audited direct
equality/stabilizer and unequal-reduced-degree extractors: both hidden fields
see the same constant degree-zero behavior. P50 does not rule out a metric or
nonlinear statistic of the varying quaternion values, a factor-asymmetric
use of the constant family, same-source joint algebraic tests, implicit
graphs, unbounded or characteristic-scale degree, or piecewise, stochastic,
canonical-metric, and dissipative completions. It is neither a factoring
lower bound nor a bare-\(N\) factoring algorithm.

The candidate, failed historical audit, corrected clean re-audit, and
context-free reconstruction are preserved under
experiments/F40_fibre_completion_bias_kill,
experiments/F40_fibre_completion_bias_audit,
experiments/F40_fibre_completion_bias_reaudit, and
experiments/F40_fibre_completion_bias_reconstruct.

## P51 — ordinary LLL decodes granted one-sided approximate multiples at the \(2^{-\sqrt n}\) relative-error scale

**Status:** verifier-backed conditional decoder theorem and method boundary.
The proof-only candidate failed its first hostile audit, was mathematically
amended, passed a fresh whole-artifact re-audit, and was then reconstructed
from the statement by a context-free agent. No computation or cross-family
audit was used.

Let

\[
 N=pq,qquad z_i=pt_i+r_i\in[0,N),qquad |r_i|\le B,qquad
 \epsilon=B/p,
\tag{51.1}
\]

where \(p,q\) are distinct fixed-balance odd primes,
\(1\le B<p/8\), and the \(t_i\) are independent uniform residues modulo
\(q\). After seeing the entire quotient tuple, an adversary may choose the
whole error vector jointly, subject only to (51.1). All probabilities below
are uniform over those error rules.

The simultaneous Dirichlet lemma used here is explicit: for real
\(\alpha_1,\ldots,\alpha_m\) and \(A\ge2^m\), pigeonholing
\(\lfloor A^{1/m}\rfloor^m+1\) torus points gives an integer
\(1\le a\le A\) with

\[
 \max_i\|a\alpha_i\|_{\mathbb R/\mathbb Z}\le2A^{-1/m}.
\tag{51.2}
\]

Put \(d=m+1\) and \(\alpha_i=z_i/N\). If

\[
 \left({2\sqrt d\over\epsilon}\right)^m
 <{q\over2\sqrt d},
\tag{51.3}
\]

then (51.2), with nearest multiples of \(N\), produces

\[
 w=(aB,az_1-Nk_1,\ldots,az_m-Nk_m),qquad
 \|w\|_2<qB,qquad 1\le a<q.
\tag{51.4}
\]

The designated factor vector

\[
 v_q=(qB,qr_1,ldots,qr_m)
\tag{51.5}
\]

has norm at least \(qB\), so it is not shortest. The conclusion in (51.4)
is only \(q\nmid a\): \(a\) may still be divisible by \(p\). If, more
strongly, there is an \(A_0\) satisfying

\[
 \left({2\sqrt d\over\epsilon}\right)^m
 <A_0<\min\!\left(p,{q\over\sqrt d}\right),
\tag{51.6}
\]

the same proof gives the shorter vector with \(\gcd(a,N)=1\). Even this does
not rule out a still-shorter factor-bearing vector and therefore is not an
SVP-factoring lower bound.

Conversely, for every fixed \(1\le a<q\), the event

\[
 \max_i\|az_i/N\|\le\epsilon
\]

implies \(\|at_i/q\|<2\epsilon\) for every \(i\), regardless of the error
rule. Multiplication by \(a\) permutes \(\mathbb F_q\), so independence of
the quotients and a union bound give

\[
 \boxed{
 \Pr[\exists\,1\le a<q:\max_i\|az_i/N\|\le\epsilon]
 \le q\left(4\epsilon+{1\over q}\right)^m.}
\tag{51.7}
\]

Equations (51.3), (51.6), and (51.7) concern approximation-denominator
geometry, not statistical factor identifiability. At
\(\epsilon=n^{-c}\), they give only the coarse scale
\(m=\Theta(n/\log n)\); the \(\sqrt m\) in (51.3) changes constants.

For the decoder, use the row lattice

\[
 \begin{pmatrix}
 B&z_1&\cdots&z_m\\
 0&N&&0\\
 \vdots&&\ddots&\\
 0&0&&N
 \end{pmatrix}.
\tag{51.8}
\]

It has determinant \(BN^m\), and every vector has the unique form in
(51.4). Run \(\delta=3/4\) LLL and write its first vector as
\(b_1=(aB,w_1,\ldots,w_m)\). Define

\[
 \Gamma=2^{m/2},\quad
 R=\Gamma qB\sqrt d,\quad
 A=R/B=\Gamma q\sqrt d,
\quad
 \theta=\min\!\left(1,4\Gamma\epsilon\sqrt d+{1\over q}\right).
\tag{51.9}
\]

If \(R<N\) and \(A<N\), then

\[
 \boxed{
 \Pr[1<\gcd(|a|,N)<N]\ge1-2A\theta^m.}
\tag{51.10}
\]

Indeed, LLL gives \(\|b_1\|\le\Gamma\|v_q\|\le R\). A nonzero lattice
vector with \(a=0\) has norm at least \(N\), so the output has \(a\ne0\)
and \(|a|\le A<N\). On decoder failure, \(a\) is coprime to \(N\). For
each fixed signed such \(a\), a vector of norm at most \(R\) necessarily
satisfies

\[
 \operatorname{dist}(at_i,q\mathbb Z)
 \le {R+|a|B\over p}\le {2R\over p}.
\tag{51.11}
\]

At most \(4R/p+1\) quotient residues satisfy (51.11), giving probability
at most \(\theta^m\). There are at most \(2A\) signed coefficients. No
union over the \(k_i\) is needed: their existence is exactly the one torus-
distance event in (51.11). The argument also handles arbitrary nonzero
multiples of either factor; \(|a|<N\) makes their gcd proper.

Let \(n=\lceil\log_2N\rceil\). For every fixed \(\eta>0\), taking

\[
 \epsilon\le2^{-(1+\eta)\sqrt n},qquad
 m=\left\lfloor(1+\eta/2)\sqrt n\right\rfloor
\tag{51.12}
\]

makes the failure term in (51.10) equal to
\(2^{-\Omega_\eta(n)}\). The order-\(n\) exponent is

\[
 {1\over2}+{(1+\eta/2)^2\over2}
 -(1+\eta/2)(1+\eta)
 =-\eta-{3\eta^2\over8}.
\tag{51.13}
\]

The size conditions also hold, since
\(R/N=\Gamma\epsilon\sqrt d=2^{-\Omega_\eta(\sqrt n)}\) and
\(A/N=\Gamma\sqrt d/p=o(1)\). Optimizing the leading requirement

\[
 \log_2(1/\epsilon)
 \ge {\log_2q\over m}+{m\over2}+O(\log m)
\tag{51.14}
\]

at \(m\sim\sqrt n\) gives the asymptotic boundary
\(\epsilon\le2^{-(1+o(1))\sqrt n}\); a
\((1/4)\log n+\omega(1)\) additive exponent absorbs the displayed lower-
order terms.

At \(\epsilon=n^{-c}\), the same proved certificate is noninformative for
every \(m\). If \(\theta=1\), then \(2A\theta^m>1\). Otherwise
\(\theta\ge4\epsilon\), \(A\ge q\), and \(\theta<1\) forces
\(m<2c\log_2n\); hence

\[
 \log_2(2A\theta^m)
 \ge\log_2q-O((\log n)^2)>0.
\tag{51.15}
\]

This is failure only of the worst-case ordinary-LLL guarantee, not an LLL,
ACD, or arbitrary-decoder hardness theorem.

The lattice dimension is \(O(\sqrt n)\) in (51.12), its entries have
\(O(n)\) bits, and exact LLL plus all gcds and verification are polynomial
in \(n\). If a separate polynomial-time source supplies fresh independent
batches with (51.1), verified repetition is a conditional Las Vegas
factorization on that promise. P51 does not construct such a source from
bare \(N\), does not cover general composites, and is not the requested
all-input algorithm.

The candidate, preserved failed audit, clean amended re-audit, and
context-free reconstruction are under
experiments/F41_metric_acd_decoder_kill,
experiments/F41_metric_acd_decoder_audit,
experiments/F41_metric_acd_decoder_reaudit, and
experiments/F41_metric_acd_decoder_reconstruct.

## P52 — finite-field Newton iteration has singleton root basins on an infinite balanced semiprime family

**Status:** verifier-backed narrow method obstruction. The proof-only
candidate passed a clean hostile audit and a fresh context-free
reconstruction. No computation or cross-family audit was used.

Let \(r\) be an odd prime, \(s\in\mathbb F_r^\times\), and \(a=s^2\). The
affine Newton rule

\[
 T(x)={x^2+a\over2x}
\]

extends to the everywhere-defined degree-two morphism

\[
 F([X:Z])=[X^2+s^2Z^2:2XZ].
\tag{52.1}
\]

The two coordinates have no common projective zero. The Möbius map

\[
 M([X:Z])=[X-sZ:X+sZ]
\tag{52.2}
\]

has determinant \(2s\ne0\), and direct homogeneous calculation gives

\[
 \boxed{M\circ F([X:Z])=[(X-sZ)^2:(X+sZ)^2].}
\tag{52.3}
\]

Thus \(F\) is globally conjugate to squaring on \(\mathbb P^1\), including

\[
 s\leftrightarrow0,qquad -s\leftrightarrow\infty,qquad
 0\leftrightarrow-1,qquad\infty\leftrightarrow1.
\]

Only \(0\) maps to \(0\) under an iterate of squaring, and only \(\infty\)
maps to \(\infty\). Therefore

\[
 F^k(x_0)=s\iff x_0=s,qquad
 F^k(x_0)=-s\iff x_0=-s
\tag{52.4}
\]

for every \(k\ge0\). If \(r\equiv3\pmod4\), then \(-s^2\) is a
nonsquare, so \(x^2+a\ne0\) for every \(x\); a nonzero start remains finite
and nonzero forever.

Now let \(N=pq\) with distinct \(p,q\equiv3\pmod4\), take public
\(s\in(\mathbb Z/N\mathbb Z)^\times\), and start from a uniform unit
\(x_0\). Define

\[
 E_r^\pm=[x_0\equiv\pm s\pmod r],qquad E_r=E_r^+\vee E_r^-.
\]

For every iterate, the complete named-ticket law is

\[
\begin{aligned}
 \gcd(2x_k,N)&=1,\\
 \gcd(x_k^2+a,N)&=1,\\
 \gcd(x_k^2-a,N)&=p^{E_p}q^{E_q},\\
 \gcd(x_k-s,N)&=p^{E_p^+}q^{E_q^+},\\
 \gcd(x_k+s,N)&=p^{E_p^-}q^{E_q^-}.
\end{aligned}
\tag{52.5}
\]

Thus later Newton iterations create no new denominator, numerator, residual,
or root-difference event. Among the \((p-1)(q-1)\) unit starts, the five
disjoint counts are

\[
 (p-3)(q-3),\quad2(q-3),\quad2(p-3),\quad2,\quad2.
\tag{52.6}
\]

The last four root combinations split into two same-sign public roots, which
are unhelpful, and two opposite-sign roots, whose two difference gcds expose
\(p,q\). Hence the exact accepted-unit success probability is

\[
 \boxed{
 \theta_{\rm unit}(p,q)
 ={2p+2q-10\over(p-1)(q-1)}.}
\tag{52.7}
\]

This includes \(p=3\) or \(q=3\), where the corresponding nonroot count is
zero.

If a restart instead draws a uniform residue, returns any proper initial
gcd, redraws only zero, and otherwise uses the accepted unit, then the first
nonzero residue is uniform over \(N-1\) classes. The proper initial-gcd
counts are \(q-1\) and \(p-1\), so

\[
 \boxed{
 \theta_{\rm raw}(p,q)={3p+3q-12\over pq-1},
 \qquad
 1-\theta_{\rm raw}={(p-3)(q-3)+2\over pq-1}.}
\tag{52.8}
\]

The zero redraw costs exactly \(N/(N-1)<2\) raw draws on average. A
history-dependent factor-free choice of public unit \(s\) before each fresh
start does not alter these counts, so \(K\) restarts succeed with probability
at most \(K\theta_{\rm raw}\).

The prime number theorem in arithmetic progressions places at least two
distinct primes \(3\bmod4\) in \([X,2X]\) for every sufficiently large
\(X\). Taking disjoint intervals \([3^j,2\cdot3^j]\) yields an infinite
fixed-balance family. On it,

\[
 \theta_{\rm raw}\le {48\over\sqrt N},
\tag{52.9}
\]

and \(\theta_{\rm unit}=O(N^{-1/2})\). Polynomially many restarts have
negligible success, regardless of the number of iterations inside each
restart, while repeat-until-success requires \(\Omega(\sqrt N)\) expected
restarts.

P52 closes only the exact known-square Newton proposal with its named
denominator/numerator/residual/root-difference gcds. It does not cover longer
cross-iterate collision or order tests, arbitrary nonlinear transcript
processing, primes \(1\bmod4\), other rational maps, prime powers and
p-adic attraction, correlated starts, stochastic resets, piecewise or
canonical real rounding, metric dynamics, or factoring generally.

The candidate, hostile audit, and context-free reconstruction are preserved
under experiments/F42_newton_basin_kill,
experiments/F42_newton_basin_audit, and
experiments/F42_newton_basin_reconstruct.

## P53 — polynomial shifted-Jacobi scalar correlations have only Weil-scale drift or rare zero mass

**Status:** verifier-backed narrow observation-channel obstruction. The
proof-only candidate passed a clean hostile audit and a fresh context-free
proof-blind reconstruction. No computation or cross-family audit was used.

Let \(N=pq\) for distinct odd primes. Normalize a multiset of shifts by
reducing modulo \(N\), collecting equal residues with positive
multiplicities \(m_e\), and screening every distinct difference
\(\gcd(e-f,N)\). On the branch where no factor is found, the \(s\) distinct
shifts are also distinct modulo each \(r\in\{p,q\}\). Put

\[
 O=\{e:m_e\text{ is odd}\},\qquad A=E\setminus O,\qquad k=|O|,
\]

and, for uniform \(x\bmod N\), define

\[
 Y_H(x)=\prod_{e\in E}\left({x+e\over N}\right)^{m_e}.
\tag{53.1}
\]

With the Legendre symbol extended by zero, let

\[
 S_r=\sum_{u\in\mathbb F_r}\prod_{e\in E}\chi_r(u+e)^{m_e}.
\]

CRT gives the exact factorization

\[
 \boxed{\theta:=\mathbb EY_H={S_pS_q\over N}.}
\tag{53.2}
\]

If \(O=\varnothing\), then \(S_r=r-s\). If \(O\ne\varnothing\), write

\[
 P_{O,r}(X)=\prod_{o\in O}(X+o),\quad
 C_r(O)=\sum_u\chi_r(P_{O,r}(u)),\quad
 R_r(O,A)=\sum_{a\in A}\chi_r(P_{O,r}(-a)).
\]

Retaining the zeros contributed by even powers gives the exact identity

\[
 S_r=C_r(O)-R_r(O,A).
\tag{53.3}
\]

The centered hyperelliptic bounds, including their genus-zero endpoints,
are

\[
 |C_r(O)|\le(k-1)\sqrt r\quad(k\text{ odd}),\qquad
 |C_r(O)+1|\le(k-2)\sqrt r\quad(k\text{ even}).
\tag{53.4}
\]

Consequently, only on the nonempty odd-support branch,

\[
 \boxed{|S_r|\le(s-1)\sqrt r,\qquad
 |\theta|\le{(s-1)^2\over\sqrt N}.}
\tag{53.5}
\]

For both branches the exact second moment and complete scalar law are

\[
 \rho:=\mathbb EY_H^2=\left(1-{s\over p}\right)
                       \left(1-{s\over q}\right),\qquad
 \zeta:=1-\rho={s(p+q-s)\over N},
\tag{53.6}
\]

\[
 \Pr(Y_H=0)=\zeta,\qquad
 \Pr(Y_H=\pm1)={\rho\pm\theta\over2},\qquad
 \operatorname{Var}(Y_H)=\rho-\theta^2.
\tag{53.7}
\]

Thus \(m\) fresh samples have mean-squared error
\((\rho-\theta^2)/m\). On every fixed-balance family with polynomial
support, estimating a nonzero odd-pattern mean to relative RMSE at most
\(\eta\) eventually requires

\[
 m\ge {N\over2\eta^2(s-1)^4}.
\tag{53.8}
\]

When the odd-pattern mean is zero, only additive error is meaningful. In the
all-even branch, \(\theta=\rho=1-\delta\), where

\[
 \delta={s(p+q)-s^2\over N}.
\tag{53.9}
\]

For \(s>0\), exact knowledge of this mean recovers
\(p+q=[N(1-\theta)+s^2]/s\), but estimating the small deviation from raw
samples to relative RMSE \(\eta\) requires
\(\Omega(\sqrt N/(\eta^2s))\) samples on fixed-balance polynomial-support
families. The exact probability that an individual shift gcd directly
returns a proper factor is

\[
 \boxed{{s(p+q-s-1)\over N}.}
\tag{53.10}
\]

There are two uniform extensions. First, for an explicitly expanded
polynomial statistic \(F=\sum_j a_jY_{H_j}\), the public fair-sign baseline
\(B(F)\) has drift at most

\[
 {1\over\sqrt N}\sum_{O_j\ne\varnothing}|a_j|(s_j-1)^2
 +{1\over N}\sum_{O_j=\varnothing}|a_j|s_j(p+q-s_j).
\tag{53.11}
\]

Hence polynomial list size, support, and coefficient \(\ell_1\)-norm leave
only exponentially small drift on balanced semiprimes. The same statement
holds conditionally for a past-measurable menu followed by a fresh uniform
sample.

Second, suppose an adaptive protocol hides each fresh \(x_i\) and releases
only one scalar \(Y_{H_i}(x_i)\). Compare it with the public reference that
returns a fresh fair sign for nonempty odd support and the constant one for
all-even support. The exact one-call total-variation distances are

\[
 {\zeta_i+\max(\zeta_i,|\theta_i|)\over2}
 \quad\text{and}\quad \zeta_i,
\tag{53.12}
\]

respectively. If the pathwise total support is
\(\sum_i s_i\le T\) and \(p,q\le\Lambda\sqrt N\), sequential maximal
coupling gives

\[
 \boxed{d_{\rm TV}(\text{real transcript},\text{public reference})
 \le {2\Lambda T+T^2/2\over\sqrt N}.}
\tag{53.13}
\]

P53 deliberately does not cover a released or retained sample \(x_i\), the
per-shift character vector, gcd labels, several correlations on one source,
same-source adaptation, exact symbolic sums, dense or succinct exponentially
expanded statistics, or arbitrary nonlinear joint Jacobi processing. It
therefore closes polynomially many fresh compressed scalar correlations, not
the broader higher-residue family or factoring generally.

The candidate, hostile audit, and proof-blind reconstruction are preserved
under experiments/F44_jacobi_correlation_kill,
experiments/F44_jacobi_correlation_audit, and
experiments/F44_jacobi_correlation_reconstruct. Their SHA-256 hashes are,
respectively,
`0b5bdfb97afff96f8c8034c5bb633d4e98d82e7ab9705c3eeaae356efc475460`,
`67970e20c51905a074c7ebf7dbd59e3c8bd3e5a1b163749377ae1dadb930773c`,
and `d0914f3c8debf9b9675fa7367c1be41c29292fa73e6612669d51d5d665840e67`.

## P54 — the hidden-source Hadamard--Paley word has an exact low-Walsh-degree boundary

**Status:** promoted narrow observation-channel obstruction and conditional
reduction. The proof-only candidate passed a clean hostile audit and a fresh
context-free proof-blind reconstruction. No computation or cross-family audit
was used.

Let \(N=pq\), where \(p<q<2p\) are distinct odd primes. Reduce a public
shift list modulo \(N\), deduplicate it, and gcd-screen every nonzero
difference. On the branch where no factor is found, write the remaining
shifts as \(a_1,\ldots,a_m\); they are distinct modulo both hidden primes.
For the accepted-word statements below assume \(m<p\), which is equivalent
in this setting to positive acceptance probability.

Draw \(X\) uniformly modulo \(N\), put

\[
 Y_j=\left({X+a_j\over N}\right)\in\{-1,0,1\},
\]

and replace each zero coordinate by its own independent fair sign to obtain
\(W\in\{-1,1\}^m\). For \(S\subseteq[m]\), define

\[
 A_r(S)=\sum_{u\in\mathbb F_r}
 \chi_r\!\left(\prod_{j\in S}(u+a_j)\right),
 \qquad r\in\{p,q\},
\]

with the quadratic character extended by zero. Conditional centering of the
fill signs and CRT give the exact Walsh coefficient

\[
 \boxed{c_S:=\mathbb E\prod_{j\in S}W_j
 ={A_p(S)A_q(S)\over N}.}
 \tag{54.1}
\]

The screened polynomial is squarefree in both fields. Therefore

\[
 c_\varnothing=1,\qquad
 c_S=0\quad(|S|=1),\qquad
 c_S={1\over N}\quad(|S|=2),
 \tag{54.2}
\]

and, for \(t=|S|\ge2\), the squarefree character-sum bound gives

\[
 \boxed{|c_S|\le{(t-1)^2\over\sqrt N}.}
 \tag{54.3}
\]

The value at \(t=2\) uses the exact identity
\(\sum_u\chi_r((u+a)(u+b))=-1\) for distinct \(a,b\).

Let \(\mu\) be the law of \(W\) and \(U_m\) the uniform sign-word law.
For the likelihood ratio \(L=d\mu/dU_m\), one has
\(\widehat L(S)=c_S\). Walsh Parseval consequently gives the exact identity

\[
 \boxed{
 \chi^2(\mu\Vert U_m)
 =\sum_{\varnothing\ne S\subseteq[m]}c_S^2
 =\sum_{\varnothing\ne S\subseteq[m]}
 {A_p(S)^2A_q(S)^2\over N^2}.}
 \tag{54.4}
\]

In particular,

\[
 d_{\rm TV}(\mu,U_m)
 \le {1\over2}\left(
 {\binom m2\over N^2}
 +{1\over N}\sum_{t=3}^m\binom mt(t-1)^4
 \right)^{1/2}.
 \tag{54.5}
\]

This is not whole-word pseudorandomness. A source has at most one zero
coordinate in each local field, and direct CRT counting gives

\[
 |\operatorname{supp}\mu|
 \le N+m(p+q)+m^2-2m<4N.
 \tag{54.6}
\]

Conditional on a public source \(X\), the word is usually deterministic;
neither (54.4) nor (54.5) controls the pair \((X,W)\).

Let \(\mathcal A\) be the event that every shifted value is a unit, and let
\(\mu_{\rm acc}\) be the accepted no-zero word law. The exact acceptance and
conditioning quantities are

\[
 \alpha=\Pr(\mathcal A)
 =\left(1-{m\over p}\right)\left(1-{m\over q}\right),
 \qquad
 \beta=1-\alpha={m(p+q-m)\over N},
 \tag{54.7}
\]

\[
 d_{\rm TV}(\mu_{\rm acc},\mu)\le\beta.
 \tag{54.8}
\]

The raw sampler has the exact three-way partition

\[
 \boxed{
 \Pr(\text{accepted})=\alpha,\qquad
 \Pr(\gcd=N)={m\over N},\qquad
 \Pr(\text{proper gcd})={m(p+q-m-1)\over N}.}
 \tag{54.9}
\]

The proper-gcd branch is factoring success, while the full gcd is only a
rejection.

For \(D\le m\), put

\[
 R_D^2=\sum_{1\le|S|\le D}c_S^2.
\]

If \(f:\{-1,1\}^m\to[0,1]\) has Walsh degree at most \(D\), Parseval gives
\(\sum_{S\ne\varnothing}\widehat f(S)^2
=\operatorname{Var}_{U_m}(f)\le1/4\).
Cauchy--Schwarz and (54.8) therefore prove the norm-sharp channel bound

\[
 \boxed{
 |\mathbb E_{\mu_{\rm acc}}f-\mathbb E_{U_m}f|
 \le\beta+{R_D\over2}.}
 \tag{54.10}
\]

No Fourier-\(\ell_1\) or support-size restriction is present. If
\(n=\lceil\log_2(N+1)\rceil\), \(m\le Cn\),
\(n\ge\max(2,C+1)\), and

\[
 D\le {n\over20\log_2n},
\]

then (54.2)--(54.3), \(2^{n-1}\le N<2^n\), and balance imply

\[
 \boxed{
 |\mathbb E_{\mu_{\rm acc}}f-\mathbb E_{U_m}f|
 \le\epsilon_{n,C}:=
 (1+\sqrt2)Cn\,2^{(1-n)/2}
 +{1\over2}\sqrt{
 C^2n^2\,2^{1-2n}+n^4\,2^{1-9n/10}}
 =2^{-9n/20+O_C(\log n)}.}
 \tag{54.11}
\]

The finitely many small \(n\) may be absorbed into a constant-times-
\(n^{5/2}2^{-9n/20}\) bound; in the nontrivial range \(m<p\) follows
automatically.

The consequence remains exact for a sequential protocol only under its
stated compression rule. In round \(i\), after the previous released bits,
choose a screened menu and a bounded degree-\(D_i\) function, apply it to one
fresh independently accepted hidden-source row, release one Bernoulli bit,
and discard both the source and row. A kernel hybrid gives

\[
 d_{\rm TV}(\text{real bit transcript},
            \text{uniform-word bit transcript})
 \le\sum_i(\beta_i+R_{D_i}/2).
 \tag{54.12}
\]

This does not cover retention of \(X_i\) or the full word, multiple decisions
on one row, same-source adaptation, high or characteristic-order degree, or
exact symbolic/list-recovery transforms.

There is a separate exact conditional all-input reduction. Assume fixed
polynomials \(L,Q,T\) and one uniform randomized algorithm \(\mathsf{Dec}\)
with this property: for every odd composite non-perfect-power \(M\) of bit
length \(k\), all of whose prime divisors exceed \(4k^2\), take the \(k\)
consecutive shifts \(0,\ldots,k-1\) and give \(\mathsf{Dec}\) \(L(k)\)
independent accepted rows together with their retained sources. In at most
\(T(k)\) bit operations it returns, with probability at least \(1/Q(k)\), a
numerical prime \(r\mid M\) whose exponent in \(M\) is odd. This is the
**HP-LR hypothesis**; no such decoder is supplied.

For arbitrary odd \(M=\prod r^{e_r}\), the accepted Jacobi word is exactly
the coordinatewise product of the local Paley words for the primes with odd
exponent:

\[
 \left({z\over M}\right)
 =\prod_{e_r\ {\rm odd}}\chi_r(z)
 \qquad(z\in(\mathbb Z/M\mathbb Z)^\times).
 \tag{54.13}
\]

After trial division through \(4k^2\), all shifts are distinct modulo every
remaining prime, and the exact raw partition is

\[
 \alpha_M=\prod_{r\mid M}(1-k/r),\qquad
 \rho_M={k\over M},\qquad
 \sigma_M=1-\alpha_M-\rho_M.
 \tag{54.14}
\]

There are at most \(k\) distinct primes and every one exceeds \(4k^2\), so
\(\alpha_M>3/4\). Accepted batches therefore have constant expected sampling
overhead. Remove powers of two, certify primes, detect exact perfect powers,
trial-divide as above, collect a fresh batch, invoke \(\mathsf{Dec}\), verify
every proposed numerical prime by deterministic primality and exact division,
and retry on failure. A non-perfect-power has at least one odd prime exponent,
so the decoder hypothesis supplies a valid target. Fresh trials succeed with
probability at least \(1/Q(k)\), terminate almost surely, and have fixed
polynomial expected bit and fair-random-bit cost. Verified recursive splitting,
with perfect-power multiplicities restored, has only polynomially many calls
and covers primes, prime powers, repeated factors, evens, unbalanced inputs,
and arbitrary composites.

Thus HP-LR would imply the requested all-input classical Las Vegas theorem,
but it is the missing algorithmic core and already promises a labeled prime
factor with inverse-polynomial probability. P54 supplies no unconditional
decoder or factoring algorithm.

P54 is strictly an obstruction to fresh-hidden-source, immediate,
low-Walsh-degree one-bit decision channels. The public sampled source, full
word, same-row reuse, high-order processing, exact transforms, and actual
Hadamard--Paley/product-code list recovery remain open. The candidate, hostile
audit, and proof-blind reconstruction are preserved under
`experiments/F45_hadamard_paley_kill`,
`experiments/F45_hadamard_paley_audit`, and
`experiments/F45_hadamard_paley_reconstruct`. Their SHA-256 hashes are,
respectively,
`ecbfc505de24f391eedb62cbaaf293b518915ac91abb8abc27b2c7a49cd7bceb`,
`7a5e77055e4cb8244a4b155d2570542fbb05b9e99e16edc36f990f24140b577c`,
and `aa36ea413d6c2eadaba2778b52754d5f4457102f36aa84b2dfec4ab0ce7b4b82`.

## P55 — Lucas tori expose an exact signed factor gap, while opaque shared-exponent pooling stays generic-hard

**Status:** promoted narrow promise theorem, conditional reduction, and
generic-method boundary. The proof-only candidate passed a clean hostile
audit and a fresh context-free proof-blind reconstruction. No computation or
cross-family audit was used.

Let

\[
N=pq,\qquad 3\le p<q
\]

for distinct odd primes, put \(R=\mathbb Z/N\mathbb Z\), choose
\(D\in R^\times\), and define

\[
A_D=R[w]/(w^2-D),\qquad
\overline{a+bw}=a-bw,
\]

\[
\operatorname{Nm}(a+bw)=a^2-Db^2.
\]

An element of \(A_D\) is a unit exactly when its norm is a unit. For
\(t\in R\), put

\[
z_D(t)=1-Dt^2.
\]

On the branch \(\gcd(z_D(t),N)=1\), the Cayley element

\[
U_D(t)=\frac{1+tw}{1-tw}
=\frac{1+Dt^2}{1-Dt^2}
 +\frac{2t}{1-Dt^2}w
\tag{55.1}
\]

is a norm-one unit.

For an odd prime \(r\nmid D\), the local Cayley map is the exact bijection

\[
\{t\in\mathbb F_r:1-Dt^2\ne0\}
\longrightarrow T_D(\mathbb F_r)\setminus\{-1\},
\tag{55.2}
\]

whose inverse at \(a+bw\ne-1\) is \(t=b/(a+1)\). Moreover,

\[
|T_D(\mathbb F_r)|=r-\left(\frac Dr\right).
\tag{55.3}
\]

Indeed, a square \(D\) splits the algebra and identifies the torus with
\(\mathbb F_r^\times\), of order \(r-1\); a nonsquare \(D\) gives
\(\mathbb F_{r^2}\), where conjugation is Frobenius and the norm kernel has
order \(r+1\). The split chart has exactly two poles and the nonsplit chart
has none. No generator hypothesis occurs.

Now choose \(D\) uniformly among units with Jacobi symbol \(-1\). Its two
local orientations

\[
(+,-),\qquad(-,+)
\]

are exactly equiprobable. Conditional on \((+,-)\), a uniform \(t\bmod N\)
has

\[
\Pr(\gcd(z_D(t),N)=p)=\frac2p,
\qquad
\Pr(\gcd(z_D(t),N)=1)=1-\frac2p,
\tag{55.4}
\]

and no other gcd value; in orientation \((-,+)\), replace \(p\) by \(q\).
Thus every pole returns the unique split local prime. If \(D\) is kept and
only \(t\) is resampled, a clean parameter appears after at most three draws
in expectation, the orientation remains fair, and the two local Cayley
points are independent and uniform on their tori with \(-1\) removed.
Rejecting the whole pair \((D,t)\) would instead bias the accepted
orientation, so these two samplers must not be conflated.

Put \(g=q-p\). Reducing \(N-1\) modulo the exact local torus orders gives,
pointwise for every norm-one unit,

\[
\boxed{U^{N-1}=U^g\quad\text{in orientation }(+,-),}
\tag{55.5}
\]

\[
\boxed{U^{N-1}=U^{-g}\quad\text{in orientation }(-,+).}
\tag{55.6}
\]

For example, in orientation \((+,-)\), the local orders are \(p-1,q+1\)
and

\[
pq-1\equiv q-p\pmod{p-1},\qquad
pq-1\equiv q-p\pmod{q+1}.
\]

The other orientation is identical with exponent \(-g\). These identities
include lower-order elements and non-generators.

All relation generation is factor-free and polynomial-bit: exact uniform
residue sampling, gcd and Jacobi screening, one modular inverse, quadratic-
algebra arithmetic, and binary powering to \(N-1\) use polynomially many
operations on \(O(\log N)\)-bit values. A polynomial number of clean triples

\[
(D_i,U_i,V_i),\qquad V_i=U_i^{N-1},
\tag{55.7}
\]

therefore has polynomial expected bit and fair-random-bit cost.

There is an exact conditional reduction. Suppose one uniform decoder, on
every distinct odd semiprime, receives \(K(n)=\operatorname{poly}(n)\)
independent triples from the choose-\(D\)-first clean law and returns the
integer \(g=q-p\) with inverse-polynomial probability in polynomial bit
time. Verify a candidate \(h\) by checking

\[
h^2+4N=s^2,\qquad s\equiv h\pmod2,
\]

and then

\[
p'=(s-h)/2,qquad q'=(s+h)/2,qquad p'q'=N.
\tag{55.8}
\]

The true gap passes because \((q-p)^2+4pq=(p+q)^2\), and every accepted
output is an exact factor pair. Fresh verified retries are Las Vegas with
polynomial expectation. Early discriminant or denominator gcds cannot
invalidate the decoder guarantee: couple the real procedure to an ideal
sampler that ignores each proper gcd and continues on the same random tape.
On every tape where the ideal decoder succeeds, the real procedure either
has already factored or reaches the identical clean transcript and succeeds.
No false conditional-fairness assertion is needed.

This reduction is strictly promise-only. It supplies neither the decoder nor
an extension to prime squares, prime powers, products of three or more
distinct primes, even inputs, arbitrary composites, recursion, or complete
factorization.

There is also a precise generic boundary. Let \(G_1,\ldots,G_K\) be
independently random-encoded tagged cyclic groups of one prime order
\(\ell\). In group \(i\), give handles for exponents

\[
0,\qquad1,\qquad\sigma_i e,
\]

where every public \(\sigma_i\in\{\pm1\}\) and
\(e\) is uniform in \(\mathbb F_\ell\). Allow arbitrary adaptive generic
group operations, equality tests, and unlimited computation between at most
\(Q\) total oracle actions. Every group-operation input must be a previously
received handle; fabricated unseen labels are not valid handles. No cross-tag
group operation or inspection of the encodings is allowed. Then

\[
\boxed{
\Pr(\widehat e=e)\le
\min\left\{1,
\frac1\ell+
\frac{\binom{Q+3}{2}+3(K-1)}{\ell}
\right\}.}
\tag{55.9}
\]

To prove this, a symbolic generic execution assigns every handle in group
\(i\) an affine exponent \(a+bX\). If \(q_i\) new handles are produced in
that group, all surprise collisions lie in a set of at most

\[
C=\sum_i\binom{q_i+3}{2}
\le\binom{Q+3}{2}+3(K-1)
\tag{55.10}
\]

secret values. Outside this set, the adaptive real transcript couples to an
ideal lazy random encoding whose output is independent of \(e\), giving the
baseline \(1/\ell\); the collision event adds at most \(C/\ell\). The
minimum with one handles finite-label edge cases. If \(e\) is uniform on a
public \(H\)-element set, the bound is \((1+C)/H\); an output list of size
\(L\) gives \((L+C)/\ell\); and a prior of maximum mass \(\mu_*\) gives
\((C+1)\mu_*\), each truncated at one.

The generic theorem deliberately does not model (55.7). Actual Lucas
elements have explicit correlated coefficient pairs over one composite
ring; different discriminants admit cross-coordinate algebra; local orders
are unequal and composite; samples need not be generators; \(q-p\) is fixed
by a worst-case input rather than sampled from the generic prior; and zero
divisors or gcds have no generic-group analogue. Interval methods,
resultants, determinants, deliberately nonuniform sampling, and every other
coordinate-specific decoder remain open.

P55 therefore closes only the assertion that polynomially many opaque,
independently encoded common-prime-order relations force shared-exponent
recovery by their number alone. It promotes the exact Lucas relation and its
promise-only conditional reduction, but it is not an unconditional factoring
algorithm and does not satisfy the top-level statement.

The candidate, hostile audit, and context-free reconstruction are preserved
under `experiments/F46_lucas_torus_gap_kill`,
`experiments/F46_lucas_torus_gap_audit`, and
`experiments/F46_lucas_torus_gap_reconstruct`. Their SHA-256 hashes are,
respectively,
`2afc8df267dc270cee4a1780c232fe46a18addbba22c13fef462c92d6ad1cf9b`,
`942823b27dbf31d8eb80a067de50ff25ffd5e3903b479bd369943f1750d1c8cb`,
and `e6fcee2e4ce5bed2da4b956aba361b88fee8654b367ebb6ecbb6a2b5c07f29ef`.

## P56 — canonical Teichmüller high digits form one global multiplicative carry cocycle

**Status:** promoted narrow method classification. The proof-only candidate
passed a clean hostile audit and a fresh context-free proof-blind
reconstruction. No computation or cross-family audit was used.

Let

\[
G_N=(\mathbb Z/N\mathbb Z)^\times,
\qquad N\ge2.
\]

For a class \(a\in G_N\), choose any integer representative \(r\) and put

\[
A(a)=r^N\pmod {N^2}.
\tag{56.1}
\]

This is well defined. If \(r'=r+kN\), then

\[
(r+kN)^N-r^N
=Nr^{N-1}kN+
 \sum_{j=2}^N\binom Njr^{N-j}(kN)^j
\equiv0\pmod {N^2}.
\tag{56.2}
\]

Moreover, a representative of \(ab\) differs from the product of
representatives of \(a,b\) by a multiple of \(N\). Hence

\[
A(ab)=A(a)A(b)pmod {N^2},
\tag{56.3}
\]

so \(A:G_N\to(\mathbb Z/N^2\mathbb Z)^\times\) is a homomorphism for
every \(N\), including even and nonsquarefree inputs.

Use canonical integer representatives and write uniquely

\[
A(a)=x(a)+Nh(a),
\qquad 0\le x(a),h(a)<N.
\tag{56.4}
\]

Reduction makes \(x:G_N\to G_N\) a homomorphism. For \(a,b\in G_N\),
abbreviate

\[
x=x(a),\qquad y=x(b),\qquad
z=\langle xy\rangle_N=x(ab),\qquad
c(x,y)=\frac{xy-z}{N}.
\tag{56.5}
\]

Expanding (56.4) modulo \(N^2\) gives the exact canonical high-digit law

\[
\boxed{
h(ab)\equiv c(x,y)+xh(b)+yh(a)\pmod N.}
\tag{56.6}
\]

Since every \(x(a)\) is a unit, define

\[
\lambda(a)=h(a)x(a)^{-1},
\qquad
\kappa(x,y)=c(x,y)\langle xy\rangle_N^{-1}pmod N.
\tag{56.7}
\]

Multiplication of (56.6) by \(z^{-1}\) proves

\[
\boxed{
\lambda(ab)=\lambda(a)+\lambda(b)
 +\kappa(x(a),x(b))\pmod N.}
\tag{56.8}
\]

The plus sign is forced by \(xy=z+Nc\). The inverse specialization is

\[
\lambda(a^{-1})
=-\lambda(a)-\frac{x\langle x^{-1}\rangle_N-1}{N}pmod N,
\tag{56.9}
\]

because the product residue is \(1\). Associating a triple product in the
two possible ways gives the normalized section-cocycle identity

\[
\kappa(x,y)+\kappa(\langle xy\rangle_N,w)
=\kappa(y,w)+\kappa(x,\langle yw\rangle_N)pmod N.
\tag{56.10}
\]

Thus \(\kappa\) is the central \(2\)-cocycle of the canonical section
\(G_N\hookrightarrow(\mathbb Z/N^2\mathbb Z)^\times\), and its pullback
along \(x\) is the coboundary of the observed \(1\)-cochain \(\lambda\).

**Exact graph consequence.** Consider any finite occurrence-labelled
multiplicative graph. A vertex occurrence \(v\) carries a unit base
\(a_v\), and every edge occurrence \(e\) has roles \(s(e),m(e),t(e)\)
satisfying

\[
a_{t(e)}=a_{s(e)}a_{m(e)}\quad\text{in }G_N.
\tag{56.11}
\]

Repeated roles, loops, repeated products, and distinct occurrences with the
same public value are allowed. Let \(B\) have, in row \(e\), coefficient
\(+1\) at \(t(e)\) and coefficients \(-1\) at \(s(e),m(e)\), collecting
coefficients when roles coincide. Put

\[
\lambda_v=\lambda(a_v),
\qquad
\kappa_e=\kappa(x(a_{s(e)}),x(a_{m(e)})).
\]

Equation (56.8) holds edge by edge and proves the literal global identity

\[
\boxed{B\lambda=\kappa
\quad\text{over }\mathbb Z/N\mathbb Z.}
\tag{56.12}
\]

Consequently every genuine edge residual, every ring-linear combination of
edge residuals, and every left-syzygy, path, triangle, or cycle syndrome is
zero. Reduction of the same witness modulo every divisor remains a solution.
For each prime \(p\mid N\), in particular,

\[
\operatorname{rank}_{\mathbb F_p}[B_p\mid\kappa_p]
=\operatorname{rank}_{\mathbb F_p}B_p.
\tag{56.13}
\]

This compares a coefficient matrix with its own augmented column in one
field. It does **not** imply that \(\operatorname{rank}B_p\) and
\(\operatorname{rank}B_q\) agree, nor does it synchronize minors, Smith
data, unnormalized coefficient matrices, arbitrary eliminants, or nonlinear
statistics. An integer residual divisible by \(N\) may also have a
nontrivial quotient after division by \(N\); (56.12) does not control that
higher digit.

**When occurrences may be merged by their \(x\)-values.** The precise
descent criterion is

\[
\boxed{
A\text{ (equivalently }h\text{) is determined by }x
\text{ on all units}
\iff
N_{\rm odd}\text{ is squarefree and }8\nmid N.}
\tag{56.14}
\]

To prove it, fix \(p^e\parallel N\), write \(N=p^em\) with \(p\nmid m\),
and work modulo \(p^{2e}\).

For odd \(p\), decompose a local unit as

\[
a=\omega\eta,
\qquad \omega\in\mu_{p-1},quad \eta\in1+p\mathbb Z_p.
\]

Then

\[
A(a)\equiv\omega^m\eta^{p^em}\pmod {p^{2e}},
\qquad
x(a)\equiv\omega^m\pmod {p^e}.
\tag{56.15}
\]

When \(e=1\), the principal factor disappears and

\[
A(a)\equiv[x(a)\bmod p]_p\pmod {p^2},
\tag{56.16}
\]

where \([\cdot]_p\) is the Teichmüller lift. Thus every squarefree odd
component descends from \(x\), whether or not the power map itself is
injective.

For \(e\ge2\), the odd \(p\)-adic logarithm identifies exponentiation by
\(p^em\) with the isomorphism

\[
\frac{1+p\mathbb Z_p}{1+p^e\mathbb Z_p}
\xrightarrow{\ \sim\ }
\frac{1+p^{e+1}\mathbb Z_p}{1+p^{2e}\mathbb Z_p}.
\tag{56.17}
\]

Thus \(x\) erases the input principal coordinate, while \(A\) retains it
bijectively. The local units \(1\) and \(1+p\) have the same \(x\)-value
but different \(A\)-values; for \(N=p^2\), explicitly,

\[
(1+p)^{p^2}\equiv1+p^3\pmod {p^4}.
\tag{56.18}
\]

This includes \(p=3\).

For \(2^e\parallel N\), every local unit has

\[
A(a)\equiv1\pmod4\quad(e=1),
\qquad
A(a)\equiv1\pmod {16}\quad(e=2).
\tag{56.19}
\]

For \(e\ge3\), write uniquely

\[
a=(-1)^\epsilon\eta,
\qquad\eta\in1+4\mathbb Z_2.
\]

The exponent kills the sign and

\[
A(a)\equiv\eta^{2^em}\pmod {2^{2e}},
\qquad x(a)\equiv1\pmod {2^e}.
\tag{56.20}
\]

The \(2\)-adic logarithm gives the isomorphism

\[
\frac{1+4\mathbb Z_2}{1+2^e\mathbb Z_2}
\xrightarrow{\ \sim\ }
\frac{1+2^{e+2}\mathbb Z_2}{1+2^{2e}\mathbb Z_2},
\tag{56.21}
\]

so \(A\) retains the \(e-2\) signless principal bits erased by \(x\).
The boundary \(e=3\) is already nontrivial; \(1\) and \(5\) give a local
same-\(x\), different-\(A\) pair. CRT combines the local determining
formulas in the forward direction of (56.14), and lifts either kind of local
counterexample while fixing every other component in the reverse direction.

Occurrence labels are therefore always safe. Equal base classes may be
identified for every \(N\); distinct occurrences with merely equal
\(x\)-values may be identified exactly under (56.14), and not in general.

**Uniform cost and scope.** With
\(n=\lceil\log_2(N+1)\rceil\), binary modular exponentiation computes one
vertex value modulo \(N^2\) in \(O(n^3)\) schoolbook bit operations.
Extraction of \(h\), an extended-Euclidean inverse for \(x\), and every
edge carry use at most \(O(n^2)\) additional bit operations. A graph with
\(V\) vertices and \(E\) genuine edges is therefore evaluated in

\[
O(Vn^3+En^2)
\tag{56.22}
\]

bit operations and polynomial space. Nonunits are screened at the external
boundary by \(\gcd(a,N)\); a proper gcd is already a factor, while a full
gcd is rejected.

P56 is a method failure only for multiplicative **linear-cocycle
inconsistency** pooling. It proves no distributional rarity for the digits
and leaves open additive and other nonmultiplicative relations, coefficient-
rank and minor/Smith selectors not equivalent to augmented consistency,
nonlinear whole-graph processing, engineered bases, power-map inversion,
canonically useful quotients after division by \(N\), noncanonical or higher
lifts, inverse-polynomial separation, recursion, and all-input factoring.

The candidate, hostile audit, and context-free reconstruction are preserved
under `experiments/F47_teichmuller_cocycle_pooling_kill`,
`experiments/F47_teichmuller_cocycle_pooling_audit`, and
`experiments/F47_teichmuller_cocycle_pooling_reconstruct`. Their SHA-256
hashes are, respectively,
`2a667261e61979aca3b0ba11b7605b750bb18bff9cb8274c318782cadc9adce2`,
`0cfb9a9ab5588ab6bba28324bebb9d2469684c3fb4770bf538df71cf6e198d53`,
and `387ebc3980863938eacdb0653d3ecc0c828181b5fc8c6932dff9b27aa437061d`.

## P57 — ordinary Dickson traces have four exact index aliases, while coherent mixed roots remain open

**Status:** promoted narrow promise theorem and method classification. The
proof-only candidate passed a clean hostile audit and a fresh context-free
proof-blind reconstruction. No computation or cross-family audit was used.

Let

\[
 N=pq,\qquad 3\le p<q
\]

for distinct odd primes, put

\[
 R=\mathbb Z/N\mathbb Z,\qquad
 e=N-1,\qquad t=p+q-2,\qquad g=q-p,
\]

and let

\[
 L=\operatorname{lcm}(p-1,q-1).
\]

Define the Dickson polynomials by

\[
 D_0(X)=2,\qquad D_1(X)=X,\qquad
 D_{j+1}(X)=XD_j(X)-D_{j-1}(X),\qquad D_{-j}=D_j.
\]

For every commutative ring, every unit \(a\), and every integer \(j\),

\[
 \boxed{D_j(a+a^{-1})=a^j+a^{-j}.}
 \tag{57.1}
\]

Both sides have the same two initial values and recurrence, which proves the
identity without any field or characteristic assumption. Write

\[
 T(a)=a+a^{-1},\qquad F_j(a)=D_j(T(a)).
\]

The exact exponent relations are

\[
 e-t=(p-1)(q-1),
\]

\[
 e-g=(p-1)(q+1),\qquad
 e+g=(q-1)(p+1).
\]

Consequently, for every unit \(a\in R^\times\),

\[
 a^e=a^t,
\]

while

\[
 a^e\equiv a^g\pmod p,\qquad
 a^e\equiv a^{-g}\pmod q.
\]

Taking traces gives the universal promised-family identity

\[
 \boxed{F_e(a)=F_t(a)=F_g(a).}
 \tag{57.2}
\]

Thus the public pair

\[
 x=a+a^{-1},\qquad y=a^{N-1}+a^{1-N}
\]

satisfies both

\[
 y=D_{p+q-2}(x)=D_{q-p}(x)\pmod N.
\]

The unsymmetrized value \(a^e\) retains only the same-sign equality
\(a^e=a^t\).

**Complete trace-alias classification.** For an odd prime \(r\),

\[
 z^u+z^{-u}=z^v+z^{-v}
 \quad\text{for every }z\in\mathbb F_r^\times
\]

holds exactly when

\[
 u\equiv v\pmod{r-1}
 \quad\text{or}\quad
 u\equiv-v\pmod{r-1}.
\]

Indeed, the functions \(z\mapsto z^j\), indexed modulo \(r-1\), are
linearly independent over \(\mathbb F_r\): summing a relation after
multiplication by \(z^{-k}\) isolates its \(k\)-th coefficient. Equality
of the two traces therefore makes the two inversion orbits equal. This proof
also covers self-inverse exponent classes and \(r=3\); the possible
coefficient \(2\) is nonzero because \(r\) is odd.

CRT lets the two local unit coordinates vary independently. Hence, for any
integers \(u,v\),

\[
 F_u=F_v\text{ on }R^\times
\]

if and only if there are independent signs
\(\epsilon_p,\epsilon_q\in\{\pm1\}\) such that

\[
 u\equiv\epsilon_pv\pmod{p-1},\qquad
 u\equiv\epsilon_qv\pmod{q-1}.
\]

Applying this to \(v=e\) yields the full alias class

\[
 \boxed{
 F_m=F_e\text{ on }R^\times
 \iff
 m\equiv t,-t,g,\text{ or }-g\pmod L.}
 \tag{57.3}
\]

Coincidences among these four classes are allowed; there is no fifth class.
For comparison,

\[
 a^m=a^e\text{ for every }a\in R^\times
 \iff m\equiv e\equiv t\pmod L.
 \tag{57.4}
\]

The gap \(g\) is also in this unsymmetrized power class exactly when
\(q=2p-1\). An arbitrary alias class plus an unknown multiple of \(L\) is
not a short integer witness.

**Both exact short representatives factor.** Given a candidate exact gap
\(h=q-p\), square-test

\[
 h^2+4N=S^2
\]

and verify

\[
 p'=(S-h)/2,\qquad q'=(S+h)/2,\qquad p'q'=N.
\]

Given a candidate exact trace index \(u=p+q-2\), put \(S=u+2\),
square-test

\[
 S^2-4N=H^2,
\]

and verify

\[
 p'=(S-H)/2,\qquad q'=(S+H)/2,\qquad p'q'=N.
\]

Exact square root, parity, positivity, and product checks make both decoders
deterministic polynomial-bit verification procedures for polynomial-bit
candidates. False candidates are harmless; they are accepted only if they
nevertheless provide a genuine factorization.

**Why the displayed many-base identities do not localize an index.** The
universal Dickson identities

\[
 D_j(D_k(X))=D_{jk}(X),
\]

\[
 D_{u+v}(X)+D_{u-v}(X)=D_u(X)D_v(X)
 \tag{57.5}
\]

imply, for units \(a,b\),

\[
 T(a^k)=D_k(T(a)),\qquad
 F_e(a^k)=D_k(F_e(a)),
\]

\[
 T(a)T(b)=T(ab)+T(ab^{-1}),
\]

\[
 F_e(a)F_e(b)=F_e(ab)+F_e(ab^{-1}).
\]

The unsymmetrized map \(a\mapsto a^e\) is a homomorphism. Powers,
products, repeated bases, and chosen bases therefore instantiate the same
power map or trace function. More generally, an adaptive procedure that
chooses public units from its preceding public residues and then evaluates
ring expressions in \(T(a_i),F_e(a_i)\) receives exactly the same transcript
after replacing \(e\) by any alias in (57.3). This is exact
nonidentifiability inside the trace-function interface. It is not an
information-theoretic or computational lower bound for algorithms that
inspect the explicit ring coordinates in other ways.

**Shifted traces isolate the surviving coherent-root problem.** Fix one
unit and write

\[
 X=T(a),\qquad Y=D_e(X),\qquad K=D_k(X),
\]

\[
 A=D_{e+k}(X),\qquad B=D_{e-k}(X).
\]

Then

\[
 A+B=YK,
\]

\[
 AB=Y^2+K^2-4.
\]

Thus \(A,B\) are the two known roots of

\[
 P_k(Z)=Z^2-YKZ+(Y^2+K^2-4).
 \tag{57.6}
\]

The values

\[
 C=D_{g+k}(X),\qquad D=D_{g-k}(X)
\]

have the same sum and product. Their ordering agrees with \((A,B)\) modulo
\(p\) and is reversed modulo \(q\); they are precisely the two CRT-mixed
roots of (57.6). First screen \(\gcd(A-B,N)\). A proper gcd already
factors. If \(A-B\) is a unit, producing either mixed root gives, for
example,

\[
 \gcd(C-A,N)\in\{p,q\}.
 \tag{57.7}
\]

If \(A-B\) vanishes in both fields, that instance has no orientation.
Therefore a quadratic formula or symmetric resultant does not manufacture
the mixed root: it only returns the two synchronized global roots already
known. Polynomially many quadratics share a coherent hidden orientation, so
a genuinely joint mixed-root selector remains open; it is not excluded by
the trace-interface theorem.

The ordinary lucky gcds also remain live. For example,

\[
 A-B=(a^e-a^{-e})(a^k-a^{-k}),
\]

so \(Y^2-4\), \(K^2-4\), and \(A-B\) can split special inputs or
bases. No inverse-polynomial all-input lower bound for these events has been
proved.

**Derivatives and first lifts are genuinely additional data.** Over
\(\mathbb Z[X]\),

\[
 (X^2-4)D_m'(X)=m(D_{m+1}(X)-D_{m-1}(X)),
 \tag{57.8}
\]

\[
 (X^2-4)D_m'(X)^2=m^2(D_m(X)^2-4).
 \tag{57.9}
\]

The public derivative \(D_e'\) is computable and, through (57.8), encodes
one known shifted-root orientation. Equality of \(D_e\) and \(D_g\) as
functions on the finite trace set does not imply equality of their formal
derivatives. The missing object is a hidden-short-alias derivative or an
independent comparator that orients it against the public one. Neither
hidden prime divides \(g\); \(q\nmid t\), but \(p\mid t\) can occur, so
division by a candidate index is not uniformly valid.

Let \(\widetilde a\) be a fixed unit lift modulo \(N^2\), let

\[
 \varphi=(p-1)(q-1)=e-t,
\]

and put

\[
 Q_{\widetilde a}
 =\frac{\widetilde a^\varphi-1}{N}\pmod N.
\]

Then

\[
 \boxed{
 T(\widetilde a^e)-T(\widetilde a^t)
 \equiv
 NQ_{\widetilde a}
 (\widetilde a^t-\widetilde a^{-t})
 \pmod{N^2}.}
 \tag{57.10}
\]

This discrepancy is lift-dependent. Replacing
\(\widetilde a\) by \(\widetilde a(1+Nh)\) changes the quotient by

\[
 Q_{\widetilde a(1+Nh)}
 \equiv Q_{\widetilde a}+\varphi h\pmod N.
\]

The variations are coherent, but neither \(Q_{\widetilde a}\) nor the
factor-determining exponent \(\varphi\) is supplied. Pooling these first
lifts is a materially new route, not a consequence of the mod-\(N\) alias
and not ruled out here.

**Interval and representation accounting.** On balanced semiprimes the
useful indices can still occupy an interval of cardinality
\(2^{\Theta(\log N)}\); on unbalanced semiprimes they may be
\(\Theta(N)\). Ordinary BSGS over an \(H\)-element interval costs
\(\Theta(\sqrt H)\) group operations. Binary-index Dickson evaluation is
cheap, but expanding \(D_m\), emitting its coefficients, or forming a
generic dense resultant can cost \(\Omega(m)\). A polynomial-size metric
candidate list would already suffice via the verified discriminant decoders,
but no such list is manufactured.

**Opaque quotient-by-inversion boundary.** Let \(\ell\) be an odd prime
and \(E\) uniform in \(\mathbb F_\ell\). In each of \(K\) independently
random-encoded tags, expose inversion-orbit handles

\[
 [0],\qquad[1],\qquad[E],\qquad [z]=\{z,-z\}.
\]

Allow a scalar call \([u]\mapsto[cu]\), or an addition-pair call

\[
 [u],[v]\mapsto\{[u+v],[u-v]\},
\]

with at most \(Q\) calls in total and an output list of at most \(M\)
residues. If \(q_i\) calls occur in tag \(i\), then

\[
 \boxed{
 \Pr(\exists h\text{ output}:h=\pm E)
 \le
 \min\left(1,{2M+B\over\ell}\right),}
 \tag{57.11}
\]

where

\[
 B=2\sum_i\binom{2q_i+3}{2}
 \le2\binom{2Q+3}{2}+6(K-1).
 \tag{57.12}
\]

Every formal handle is an affine orbit \([\alpha+\beta Z]\). A tag sees
at most \(2q_i+3\) handles, and two distinct formal orbits collide only at
a root of \(f(Z)=\pm g(Z)\), contributing at most two secret values per
pair. Outside their union, lazy random encodings make the transcript
independent of \(E\); the output list covers at most \(2M\) field values.
The same proof gives public-subset and maximum-prior-mass variants.

In a stronger ordinary generic-group model, the corresponding bound is

\[
 \min\left(1,{2M+C\over\ell}\right),
 \qquad
 C\le\binom{Q+3}{2}+3(K-1).
 \tag{57.13}
\]

Composite orders require an explicit root-multiplicity term, and
non-generators may reveal only short congruences. Neither theorem transfers
to the explicit factoring ring: its local orders are unequal and composite,
bases share numerical coordinates and multiplicative correlations, gcds can
read CRT disagreement, and resultants, derivatives, and lifts inspect more
than generic equality. The generic theorem closes only the claim that many
opaque relations force recovery merely by their number.

**Scope.** Nonunits and every introduced denominator or difference must be
gcd-screened; proper gcds are success and full gcds are rejection or
degeneracy. The theorem excludes \(p=q\), prime powers, three-or-more-prime
products, even inputs, and primes. The displayed two-factor identities and
discriminant decoders do not extend automatically to those cases. Hidden
local generators, \(p-1\), \(q-1\), \(L\), group orders, or factoring
oracles cannot be treated as free preprocessing.

P57 is a method failure only for localizing an integer index by accumulating
the displayed symmetric trace identities, and for opaque prime-order generic
pooling. It does not close coherent mixed-root selection, explicit
derivative/resultant/minor comparators, useful lucky gcd distributions,
modulo-\(N^2\) pooling, factor-free metric shrinkage, non-generator
structure, an all-input extension, or integer factoring generally.

The candidate, hostile audit, and context-free reconstruction are preserved
under `experiments/F48_dickson_trace_index_kill`,
`experiments/F48_dickson_trace_index_audit`, and
`experiments/F48_dickson_trace_index_reconstruct`. Their SHA-256 hashes are,
respectively,
`801f86d6acb3c5278ba5f5e1d0ba4db6349b4e9be3878727d29602991c5d6d61`,
`86d840259d1ae0f035f95d4d1785d2c68c6f0a30bcce556f5133aab6bb2ebbef`,
and `278ab46afc83ee25af883f8ef82016084d9b2cdf7f55f0e9d78ac5121ea5dc9a`.

## P58 — a screened coherent Dickson-root component has one idempotent switch

**Status:** promoted narrow promise theorem and method classification.

**Verification record:** two hostile audits found real errors in earlier
versions: raw double-root nilpotents and overbroad component scope in the first,
then a false reduced equation when an eliminated constant was the product output
in the second. Both failed audits are preserved. The twice-corrected artifact
passed a fresh whole-proof hostile audit and a strict proof-blind reconstruction.
No cross-family or human audit has run.

Let

\[
N=pq,\qquad 3\le p<q
\]

for distinct odd primes, put \(R=\mathbb Z/N\mathbb Z\), and define

\[
E(z)=z^{N-1},\qquad G(z)=z^{q-p},\qquad T(z)=z+z^{-1}.
\]

Every group homomorphism \(H:R^\times\to R^\times\) satisfying

\[
T(H(a))=T(E(a))\qquad(a\in R^\times)
\]

is one of

\[
\boxed{E,E^{-1},G,G^{-1},}
\]

with coincidences allowed. CRT first shows that each output coordinate ignores
the opposite input coordinate. Over one field,
\(x+x^{-1}=y+y^{-1}\) forces the two multiplicative characters to agree or
be inverse globally. The two local signs give exactly the four displayed maps.

There is a factor-free constant-expected-trial screen for a nondegenerate public
root pair. For a uniform raw residue, first screen its gcd, then compute
\(Y=E(a)\) and screen \(Y-Y^{-1}\), followed in the full-gcd case by
\(Y-1\) and \(Y+1\). Put

\[
d=\gcd(p-1,q-1),\qquad h_p=(p-1)/d,\qquad h_q=(q-1)/d.
\]

Conditional on a unit input, the exact no-factor/no-anchor probability is

\[
\frac{1+\mathbf1_{2\mid h_p,\,2\mid h_q}}{h_ph_q}\le\frac12.
\]

The raw unit probability is at least \(8/15\), so one raw trial returns a
factor or a pair \(A,A^{-1}\) with unit difference with probability at least
\(4/15\). Every trial has polynomial bit and fair-random-bit cost.

Now take finitely many public inverse-root variables

\[
(X_v-A_v)(X_v-A_v^{-1})=0
\]

and genuine public multiplicative relations \(X_w=X_uX_v\). Gcd-screen every
root difference. A proper gcd is success. If the gcd is full, screen the two
signs, add the proved linear equation \(X_v=s\), \(s\in\{1,-1\}\), and
eliminate the variable. This linear reduction is necessary: the raw quotient
by \((X_v-s)^2\) has a nilpotent.

For every retained variable write

\[
X_v=A_v^{-1}+f_v(A_v-A_v^{-1}),\qquad f_v^2=f_v.
\]

A nondegenerate triangle kills exactly the unequal Boolean corners and
identifies its orientations. Repeated inputs, repeated outputs, and constants
must be simplified first. In particular, a constant input gives
\(X_w=sX_u\), while a constant product gives

\[
s=X_uX_v,\qquad X_v=sX_u^{-1}.
\]

In the latter case, with \(A=A_u\) and
\(\delta=A-A^{-1}\in R^\times\), write

\[
X_u=A^{-1}+f\delta,\qquad X_v=sA-hs\delta.
\]

The residual \(X_uX_v-s\) is zero at \((f,h)=(0,0),(1,1)\) and is the
unit \(sA\delta\) or \(-sA^{-1}\delta\) at the unequal corners. Thus it
also imposes \(h=f\).

Consequently every connected component of the screened, linearly reduced,
proved orientation graph has exact coordinate algebra

\[
\boxed{R[f]/(f^2-f).}
\]

Different components retain independent idempotents. Shifted quadratics are
covered only after their retained screened variables have been explicitly
proved to lie in one such component; the quadratics alone do not prove
coherence.

Every element of this component algebra has the unique endpoint form

\[
Q(f)=Q(0)(1-f)+Q(1)f.
\]

Hence a public, factor-free, polynomial-size polynomial relation that accepts
both synchronized endpoints is tautological on the component. If a nontrivial
CRT idempotent satisfies it while an endpoint fails, one of
\(\gcd(Q(0),N)\) and \(\gcd(Q(1),N)\) is a proper factor. If a solver
returns a mixed screened coordinate \(X\), then comparison with its two public
roots gives \(p\) and \(q\); conversely, known factors construct every mixed
coordinate by CRT. Producing that mixed coordinate is therefore
deterministic-polynomial-time equivalent to factoring on this promise.

P58 is an obstruction, not a sampler or factoring algorithm. It does not cover
independent-component couplings, auxiliary existential variables, ordered or
metric rules, inequalities, optimization, stochastic or positive-combinatorial
samplers, derivatives, lifts modulo \(N^2\), lucky distributions, prime powers,
even or multifactor inputs, recursion, or an all-input Las Vegas bound.

The corrected candidate, clean audit, and proof-blind reconstruction have
SHA-256 hashes
`b34c2965b4be06ca59c9c27ba54814a76c1cac286bcfb13beee65917f9093aba`,
`7a916baae18362ba03e92e59b9f06a20c220064ba5f0e094464aa556827aed8b`,
and `0deccee4937143f443455a3564a4b61812f1cfe8a815bb54c42915506daeeeae`.

## P59 — one derived defect does not remove the local Gibbs density bottleneck

**Status:** promoted narrow sampler obstruction.

**Verification record:** the first hostile audit found two literal scope errors:
an unordered balance hypothesis and a totient identity stated beyond distinct
semiprimes. The corrected proof passed a fresh whole-proof hostile re-audit and
a strict proof-blind reconstruction. No cross-family or human audit has run.

Let (R=\mathbb Z/N\mathbb Z), and use the constrained graph

\[
\widehat\Omega_N=\{(k,x,d)\in R^3:d=kx\}.
\]

Here (k,x) are the two free coordinates and (d) is recomputed after every
refresh; literal one-coordinate Gibbs on three independently held coordinates
would be reducible. Give a state weight (1) when (d=0) and a positive
scalar weight \(\lambda\) when (d\ne0). Conditioned on (d=0), the target is
exactly uniform on

\[
\Omega_N=\{(k,x):kx=0\pmod N\}.
\]

For the public choice \(\lambda=1/N\), the zero-defect sector has stationary
mass greater than (1/2). A random-scan refresh of one free coordinate has an
exact fair-bit implementation with (O(\log N)) expected random bits and
polynomial expected bit cost. The chain is reversible, irreducible, and
aperiodic. Unlike the cold in-locus heat bath, it can cross from one unit axis
to the other through a nonzero defect in two positive-probability updates.

Put

\[
H_N=\{a\in R:1<\gcd(a,N)<N\},\qquad h_N=|H_N|.
\]

Before a coordinate gcd finds a factor, every observed coordinate is zero or a
unit. Conditional on every such history, one refresh enters (H_N) with
probability at most

\[
\frac{h_N}{N}
\]

for \(\lambda=1/N\), and at most (h_N/(N-1)) for every positive scalar
activity. These are pathwise bounds; no independence between updates is used.
Thus, from any safe start, the expected coordinate-gcd hitting time is at least

\[
\frac{N}{h_N}
\quad\text{or respectively}\quad
\frac{N-1}{h_N}.
\]

For distinct primes (p<q),

\[
h_{pq}=p+q-2,
\qquad
|\Omega_{pq}|=(2p-1)(2q-1).
\]

On every fixed-balance family (q/p\le C), the expected hitting time is
\(\Omega_C(\sqrt N)\). The stationary factor-bearing mass is bounded below by
a constant, so the same history bound gives an explicit
\(\Omega_C(\sqrt N)\) fixed-threshold total-variation mixing obstruction.
For (N=p^2), (h_N=p-1) and

\[
|\Omega_{p^2}|=3p^2-2p,
\]

which gives \(\Omega(\sqrt N)\) hitting and mixing bounds, including the exact
small case (p=2). More generally, the proof records the corresponding
prime-power counts without claiming a growing lower bound when (p) is fixed.

P59 closes only one common good-state weight, one common positive defect-state
weight, and a local refresh of one free coordinate, with coordinate-gcd
extraction. It does not cover a nonconstant residual weight, a nonuniform
arithmetic proposal, a joint ((k,x)) move, multiple defects with cancellation,
a lifted or valuation-amplifying move, a transcript decoder, or a charged warm
start. Those changes alter the operation which creates or detects a CRT stratum.

The corrected candidate, clean re-audit, and proof-blind reconstruction have
SHA-256 hashes
`bec5fbfb0de76677d78aa36187485b06848be9891a033fd1a1f91cf4ddfd88b1`,
`1bdb02879801a922bbb5c3e464b65436a1f1b7408c3aafd9bff5585693e3dff4`,
and `908054491f1d5b6d47cd286a586d05fba04e4ce94e180891a4da801011bd3203`.

## P60 — canonical exponent-\(N\) high digits have exact local laws but sparse metric signals

**Status:** promoted narrow source-side obstruction.

**Verification record:** the first hostile audit verified every formula and all
five computations but rejected an overbroad Fourier inference. The corrected
proof passed a fresh whole-proof hostile re-audit and a strict proof-blind
reconstruction. All five retained computations reproduced byte-identically.
No cross-family or human audit has run.

Let

\[
N=pq,\qquad 3\le p<q<2p,
\]

for distinct primes. For a uniform unit (a\bmod N), define canonical values

\[
A=a^N\bmod N^2=x+Nh,
\qquad
\lambda=h x^{-1}\bmod N,
\qquad 0\le x,h,\lambda<N.
\]

The map (a\mapsto x=a^N\bmod N) is an automorphism of the unit group, so
(x) is exactly uniform. With the Fermat quotient

\[
Q_r(u)=\frac{u^{r-1}-1}{r}\pmod r,
\]

the high digits satisfy the exact local laws

\[
q\lambda\equiv Q_p(x)\pmod p,
\qquad
p\lambda\equiv Q_q(x)\pmod q,
\]

and

\[
qh\equiv xQ_p(x)\pmod p,
\qquad
ph\equiv xQ_q(x)\pmod q.
\]

Writing an integer representative of (x) in one local residue class makes
the missing CRT carry affine. Exact counting then gives, for
(Z\in\{h,\lambda\}),

\[
\Pr(Z\equiv c\pmod p)\le\frac2{q-1},
\qquad
\Pr(Z\equiv c\pmod q)\le\frac1{p-1},
\qquad
\max_z\Pr(Z=z)\le\frac1{p-1}.
\]

Consequently, polynomially many fixed or past-measurable exact-value menus,
exact collisions, direct gcds, and pairwise-difference gcds have total success
probability (2^{-\Omega(\log N)}). A hidden-prime residue band of absolute
half-width (B<p/2) has mass (O(B/p+1/p)). At the precision used by P51's
ordinary-LLL certificate, collecting the required batch from this raw source
needs (2^{\Omega(\sqrt n)}) samples, where (n) is the input bit length.
The theorem does not grant P51's independent hidden-quotient law even after a
band hit.

The integer high digit has the exact reflection

\[
h(N-x)=N-1-h(x),
\qquad
\mathbb E h=\frac{N-1}{2}.
\]

Its central-half bias is exponentially small, but this does not control other
intervals or imply uniformity. Parseval and the point-mass bound show that a
uniform unit frequency is exponentially unlikely to be an
inverse-polynomial-heavy Fourier mode. A local-isolating frequency is already a
nonzero multiple of (p) or (q), so its public gcd factors (N). The
sampling estimate for a fixed mode is only the exact mean-square error of the
raw empirical mean; it is not a lower bound for other estimators.

One exact source sample uses (O(n)) expected fair bits and (O(n^3)) bit
operations with schoolbook arithmetic. P60 does not prove pseudorandomness or a
factoring lower bound. It leaves deterministic exceptional frequencies,
adaptive recovery, exact symbolic evaluation or amplification of tiny biases,
dense or nonlinear joint statistics, correlated or nonuniform bases, other
estimators, and all-input constructions open.

The corrected candidate, clean re-audit, and proof-blind reconstruction have
SHA-256 hashes
`2a1e111ffdbc20e76582201cb6f7fab24669cb0609711e030cf6c88e95828f90`,
`9a7158a0dffe858eb3df619e547f8eab5429253b1e615b9328082075307ba2a5`,
and `a87a7016f48a2583165cd8b8db89b76e3a8dbba31154393ce065df3ccfc5570d`.
The computation manifest has hash
`b3fd206c0edba6903ad79444cf5a380207b970eff9b2a8eb80aed1da7cd5e8a1`.

## P61 — a residual-only local Gibbs wrapper cannot amplify factor mass

**Status:** promoted narrow sampler reduction and pathwise obstruction.

**Verification record:** the first hostile audit accepted the core probability
theorem but required five scope corrections. A fresh re-audit found two more
interface errors: nonuniform factor advice could be hidden in the weight
description, and the warm-start scope was too narrow. The twice-corrected
artifact passed a second fresh whole-proof audit and a strict proof-blind
reconstruction. No cross-family or human audit has run.

Let \(R=\mathbb Z/N\mathbb Z\), let \(w:R\to\mathbb R_{\ge0}\) satisfy
\(w(0)>0\), and give \((k,x)\) unnormalized weight \(w(kx)\). Put

\[
W=\sum_{d\in R}w(d),
\qquad
\nu_w(d)=\frac{w(d)}W.
\]

Conditioned on \(kx=0\), the target is exactly uniform on
\(\Omega_N=\{(k,x):kx=0\}\). If one coordinate is held at \(b\), the exact
one-coordinate Gibbs law is

\[
Q_{b,w}(a)=\frac{w(ab)}{\sum_{y\in R}w(yb)}.
\]

At a held unit, the new residual \(D=ab\) has law \(\nu_w\). At a held zero,
the refreshed coordinate is uniform on \(R\). Define

\[
H_N=\{d:1<\gcd(d,N)<N\},
\qquad
h_N=|H_N|,
\qquad
\theta_w=\nu_w(H_N).
\]

There is an immediate direct reduction. Suppose one uniform public algorithm
takes only bare \(N\), constructs a polynomial-size description of \(w_N\)
without advice, and exactly samples \(Q_{1,w_N}\), with all construction, bit,
and fair-bit costs under one fixed expected polynomial bound. If
\(\theta_{w_N}\) is uniformly inverse-polynomial, independent direct calls to
that conditional followed by gcd factor in expected polynomial time. The Gibbs
chain adds nothing to this source.

Conversely, monitor both coordinates and the residual during the local chain.
From every safe warm start, and under deterministic, random, lazy, or
past-measurable adaptive one-coordinate scan, the complete survival history
leaves the held coordinate either zero or a unit. The next conditional hazard
is therefore at most

\[
\rho_w=\max\left\{\theta_w,\frac{h_N}{N}\right\}.
\]

For the first monitored hit time \(\tau\),

\[
\Pr(\tau>t)\ge(1-\rho_w)^t,
\qquad
\Pr(\tau\le t)\le t\rho_w,
\qquad
\mathbb E\tau\ge\frac1{\rho_w}
\]

when \(\rho_w>0\); if \(\rho_w=0\), no hit occurs. For balanced distinct
semiprimes, \(h_N/N=O(N^{-1/2})\). For \(N=p^2\),
\(h_N/N<N^{-1/2}\). Thus negligible \(\theta_{w_N}\) gives negligible success
for every polynomial number of local refreshes and a superpolynomial expected
delay. The sharper condition

\[
\theta_{w_N}=O\!\left(N^{-1/2}\operatorname{poly}(\log N)\right)
\]

gives
\(\mathbb E\tau=\Omega(\sqrt N/\operatorname{poly}(\log N))\).

P61 is not a factoring lower bound and does not rule out constructing a useful
residual law. It proves only that the named residual-only one-coordinate
wrapper cannot amplify such a law. Joint block moves, genuinely joint
\((k,x)\)-weights, interacting residuals, valuation lifts, nonlocal proposals,
global transcript decoders, and different arithmetic screens remain open.

The twice-corrected candidate, passing re-audit, and proof-blind reconstruction
have SHA-256 hashes
`e2c9fcba130bb64b21c5f53dfac546cebf1b4a70603fb072f642518d1a8e1826`,
`721b707c9af57cc13af681e0ff27a180b54544354044ddb336b95a8225c67819`,
and `f56fc521ae8deab489999c59e56ec02944b6d8377c31ac89717676e23f1c4a6b`.
The two preserved failed audits have SHA-256 hashes
`4d830ab8cbcb4a5b5e6cd23b2ba2fdf9cd2c5a7a8df046a1968d700eaae24124`
and `bbbdea3abe7373c86d50b52de3a34aed2657d5dc00a2666281dd1897f5507ec6`.

## P62 — inverse-quotient descent has exact divisor fibres and a near-square-root depth bound

**Status:** promoted narrow structural theorem and exact depth-shortcut failure.

**Verification record:** the first hostile audit accepted the main mathematics
but found one incorrect reverse-fibre statement and several provenance and scope
errors. A fresh re-audit found one remaining stale manifest statement. After
that correction, a second fresh whole-artifact audit passed. A strict
proof-blind reconstruction also succeeded. No cross-family or human audit has
run.

For a unit $u\in\{1,\ldots,N-1\}$, let $v$ be its least positive
inverse modulo $N$, and define the integer quotient

\[
D_N(u)=\frac{uv-1}{N}.
\]

For $2\le u<N$, let $r_u$ be the least positive inverse of $N\bmod u$.
Then

\[
\boxed{D_N(u)=u-r_u},
\qquad
D_N(u)=u-r\iff u\mid Nr-1.
\]

Thus every defined nonterminal step strictly decreases its canonical integer
state. This operation uses order, modular inversion, and exact integer division.
It is not only a polynomial-algebra computation in \(\mathbb Z/N\mathbb Z\).

The reverse fibres are exact:

\[
D_N^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\]

If $v=(Nk+1)/u$, then automatically $k<v<N$, both $u,v$ are units
modulo $N$, and both map to $k$. Hence non-square fibres pair complementary
factors of the public integer $Nk+1$. This is a structural description, not
an efficient reverse sampler, because finding those divisors is not supplied.

For a trajectory with $L$ transitions, put

\[
\Delta_N=\max_{1\le m<N^2}\tau(m).
\]

For every $1\le B<N$, grouping steps by their decrement gives

\[
L\le \frac NB+B\Delta_N+1.
\]

The standard maximal-order bound for the divisor function gives

\[
L\le N^{1/2+o(1)}.
\]

This improves the trivial $L<N$ state bound, but it is still exponential in
the binary input length. It is not a polynomial-time runtime theorem.

Long trajectories are genuine. With

\[
M_L=\operatorname{lcm}(2,\ldots,L+1),
\qquad N_L=(M_L+1)^2,
\]

the exact trajectory is

\[
L+1\to L\to\cdots\to2\to1,
\]

and both its length and the bit length of $N_L$ are \(\Theta(L)\). These
inputs are easy perfect squares, so this family is only a warning against a
universal $o(\log N)$ depth claim.

The proposed uniform two-step contraction is false. Exact witnesses are
$7\to5\to4$ for $N=11$ and $19\to13\to10$ for the balanced
semiprime $N=35$. The second witness shows that the shortcut already fails
in the intended semiprime regime.

Finite scans found sparse named gcd tickets on the larger tested balanced
semiprimes, but they prove no asymptotic hit law. P62 proves no
inverse-polynomial success probability and gives no whole-transcript decoder.
The public relations

\[
u_i v_i=N u_{i+1}+1
\]

remain available for a genuinely joint parity, lattice, continued-fraction, or
other decoder. Therefore F26 remains open and P62 is not a factoring algorithm.

The corrected candidate, passing final re-audit, proof-blind reconstruction,
and computation manifest have SHA-256 hashes
`139d11d7858cfdcd40880ddde86ed40316038a94c5269fba6e9be19f547568e2`,
`fc172deb00838b4f77c4af813bc8747280bd5a3d74b139d0f9c06d86f0edc14d`,
`75e512ce136e60edfe3dffefc98df006c76059698e25b41227523b778be04f18`,
and `c36ee5112f7bb335ab39a938e4774c2bbe57733d85ea8ede68b0424796e2fcb9`.
The two preserved failed audits have SHA-256 hashes
`73fcda541a72c074af717e16a12bc73a07980bd735d5a3df4fba7f82d808e6aa`
and `1c321a097632d847b77fccdbe8274a24de1613a436a49ec69c6072d23aacd9a9`.

## P63 — branching degree does not force a polynomial root basin to grow

**Status:** promoted narrow polynomial-dynamics obstruction and general
necessary basin condition.

**Verification record:** the candidate passed a fresh hostile whole-artifact
audit as written. A strict proof-blind reconstruction then recovered the
theorem, both exact probabilities, affine-conjugacy boundary, infinite balanced
family, general basin bound, and edge cases. No cross-family or human audit has
run.

Let

\[
H(x)=x(x-1).
\]

For an odd prime $r\ne5$ with Legendre symbol

\[
\left(\frac5r\right)=-1,
\]

the target set $A=\{0,1\}$ has the exact inverse image

\[
\boxed{H^{-1}(A)=A}.
\]

The equation $H(x)=0$ gives $0,1$, while $H(x)=1$ has discriminant
$5$ and no root. Hence an orbit reaches $A$ at any time if and only if it
starts in $A$. The formal degree of $H^{\circ t}$ is $2^t$, but its
useful backward basin still has only two points.

Let $N=pq$, where $p\ne q$ are odd primes satisfying the same nonresidue
condition. From a uniform residue start, screen both public roots at every
iterate:

\[
\gcd(x_i,N),
\qquad
\gcd(x_i-1,N).
\]

For any number of iterations, the exact one-restart success probability is

\[
\boxed{\frac{2p+2q-6}{pq}}.
\]

For a uniform unit start it is

\[
\boxed{\frac{p+q-4}{(p-1)(q-1)}}.
\]

For every unit $c$, the map

\[
H_c(x)=\frac{x(x-c)}c
\]

is conjugate to $H$ by $x=cy$. Its targets $0,c$ have the same basin
and exact probabilities. General affine conjugacy preserves the basin and a
uniform raw-residue start; translation does not automatically preserve a raw
unit start. A nonunit parameter, mixed target, mixed root, or mixed public
difference is screened first and already factors on its proper-gcd branch.

Every prime $r\equiv2\pmod5$ has $(5/r)=-1$. The prime number theorem in
arithmetic progressions supplies infinitely many balanced pairs of distinct
such primes. On that family, both displayed probabilities are
$\Theta(N^{-1/2})$. Polynomially many restarts therefore have negligible
success, and repeat-until-success needs $\Omega(\sqrt N)$ expected restarts.

There is also a general necessary condition. For a public CRT-compatible map
$F_N$, local target set $A_r$, and time cap $t$, put

\[
B_{r,t}=\{u\in\mathbb F_r:F_{N,r}^{\,i}(u)\in A_r
\text{ for some }0\le i\le t\}.
\]

From a uniform CRT start, every target-ticket factor event satisfies

\[
\Pr(\text{factor by time }t)
\le\frac{|B_{p,t}|}{p}+\frac{|B_{q,t}|}{q}.
\]

The same inequality can be averaged over independent public map randomness on
the factor-free construction branch. It is necessary, not sufficient: the two
local hit signatures can still synchronize.

P63 does not cover unrelated or $N$-dependent maps, extra state, correlated
or nonuniform starts, valuation lifts, arbitrary nonroot targets, or full-orbit
decoders using periods and collisions. It is not a factoring algorithm. It
proves that noninvertibility and exponentially growing formal degree are not
enough; a useful dynamic sampler must prove actual inverse-polynomial basin
mass over every hidden-prime family.

The candidate, hostile audit, proof-blind reconstruction, and computation
manifest have SHA-256 hashes
`a0ca496ec0aba9cf0ad9c52683aefc0e05507558d3d0120eb6a50454dd96db19`,
`7cf5802d24c804a561641cb7164403a9a1291aac7c9ed16e1c72266b53cdbc8b`,
`e19d8b1c57daab4eb65a2dd5b02ab891a6234a24df8a6345ef738478c848d86c`,
and `bee0d78de357e606232f7166ec4e880811b394630f03efe18c18d0fff161f6dc`.

## P64 — formal parity of inverse-pair labels adds no factoring information

**Status:** promoted narrow whole-batch decoder obstruction.

**Verification record:** the first hostile audit found a false claim about
products of several self-loop roots and a false no-cycle sentence. The
corrected candidate passed a fresh whole-proof re-audit. A strict proof-blind
reconstruction then succeeded. No cross-family or human audit has run.

Let $N\ge3$ be odd, and let $\iota(x)$ be the canonical inverse of a
unit $x\bmod N$. Consider any finite, possibly adaptive, batch of inverse
pairs

\[
(a_j,b_j),
\qquad b_j=\iota(a_j),
\]

with repetitions allowed. Select a subset in which every public endpoint
label occurs an even number of times. Its visible integer product is a square

\[
\prod_j a_jb_j=X^2,
\qquad X^2\equiv1\pmod N.
\]

The inversion involution has only two types of orbit. On a two-element orbit
$\{x,\iota(x)\}$, endpoint parity selects an even number $2h$ of
parallel relations, whose root contribution is

\[
(x\iota(x))^h\equiv1\pmod N.
\]

On a singleton orbit, the submitted relation is a self-loop $(z,z)$ with
$z^2\equiv1\pmod N$. Hence every formal-parity output lies in the subgroup
generated by submitted self-loop labels. Several loops can multiply to a new
root value; the theorem does not deny that.

Each submitted loop is directly screened by

\[
\gcd(z-1,N),
\qquad
\gcd(z+1,N).
\]

For odd $N$, every prime-power divisor of $N$ divides exactly one of
$z-1,z+1$. The screen therefore returns a proper factor, or proves
$z\equiv\pm1\pmod N$. After all loop screens fail to factor, every pooled
output is also $\pm1$. Thus formal endpoint parity adds no factoring
information beyond direct loop screening.

This is strictly narrower than true arithmetic square parity. If $C$ is the
endpoint-label incidence matrix over $\mathbb F_2$, and $V$ maps labels
to their rational-prime valuation parities, then

\[
\ker C\subseteq\ker(VC),
\]

and the inclusion can be strict. For $N=15$, the single inverse pair
$(2,8)$ is not a formal label-parity relation, but

\[
2\cdot8=16=4^2,
\qquad \gcd(4-1,15)=3.
\]

This success uses the arithmetic square classes of the integer labels. It is
outside P64.

P64 does not cover smoothness, arithmetic factor-base pooling, chronological
quotient equations, lattices, continued fractions, hidden periods, HSP or
Shor simulation, stabilizer recursion, nonlinear graph constructions, or
factoring generally. It closes only the formal endpoint-incidence kernel of
inverse pairs.

The corrected candidate, passing re-audit, and proof-blind reconstruction have
SHA-256 hashes
`028d41a7db2f4600964aeb24a9547bd614f080a84ec438f09fbf14fd78d86c07`,
`45af2b5438e659e38734c721f6a5f7d73e34a66b83c27953df5a58e3c6575238`,
and `19199147c5c20b7d037ca77d90132df4dbbe90d874f8a395f0e81bd798971154`.
The preserved failed first audit has SHA-256
`958db4092d9bd9177df0ed7748be0f6f2b9aa0887bcb0d17f3d58d8f94223666`.

## P65 — inverse quotients give an exact completion-biased source and a clustered arithmetic decoder

**Status:** promoted narrow source theorem, independent-clustering obstruction,
and conditional batch decoder.

**Verification record:** the first hostile audit accepted the main theorem but
found a false duplicate-index reduction and an overstrong equivalence claim.
The corrected theorem passed a fresh whole-artifact re-audit. A strict
proof-blind reconstruction then recovered every substantive clause, including
duplicates, singleton relations, repeated prime powers, even inputs, and bit
complexity. No cross-family or human audit has run.

For a unit $u\in\{1,\ldots,N-1\}$, let $v$ be its least positive inverse
modulo $N$, and put

\[
D_N(u)=\frac{uv-1}{N}.
\]

For $1\le k<N$, define

\[
f_N(k)=\#\{u:k<u<N,\ u\mid Nk+1\},
\qquad f_N(0)=1.
\]

If $U$ is uniform over the units modulo $N$, then the exact output law is

\[
\boxed{
\Pr(D_N(U)=k)=\frac{f_N(k)}{\varphi(N)}.
}
\]

Thus modular inversion, canonical representatives, and one exact integer
division sample an implicit distribution weighted by the number of admissible
factor-pair completions of $Nk+1$. The weights do not have to be evaluated.
This is a real source bias manufactured from bare $N$. It is not yet a proved
bias toward a factor.

Let

\[
\Delta_N=\max_{1\le m<N^2}\tau(m).
\]

Every set of $h$ output indices has mass at most

\[
\frac{h\Delta_N}{\varphi(N)}.
\]

For $T$ independent outputs $K_1,\ldots,K_T$ and any integer $H\ge0$,

\[
\Pr\bigl(\exists i<j:\ |K_i-K_j|\le H\bigr)
\le
\binom T2\frac{(2H+1)\Delta_N}{\varphi(N)}.
\]

On balanced distinct semiprimes, polynomially many independent samples have
negligible probability of an exact collision or a cluster of polynomial
numerical width. This conclusion does not apply to dependent descent tails or
other statistics of an unclustered batch.

There is also an exact arithmetic confinement law. For distinct indices, put

\[
A_i=Nk_i+1.
\]

Then

\[
\boxed{
\gcd(A_i,A_j)=\gcd(A_i,|k_i-k_j|).
}
\]

If a nonempty selected product of the $A_i$ is an integer square, then for
every selected $i$,

\[
\operatorname{sf}(A_i)
\mid
\prod_{\substack{j\ne i\\j\text{ selected}}}|k_i-k_j|.
\]

Hence a square relation whose indices have diameter at most $H$ can use only
squarefree kernels supported on primes at most $H$. Trial division by those
primes, exact square tests on the residual cofactors, and binary linear algebra
therefore give a deterministic decoder polynomial in $m+H+\log N$. It
represents every exact square subset in the batch. The map from its parity
kernel to the resulting roots of $1\bmod N$ is a homomorphism, so testing a
kernel basis detects a non-global root whenever any dependency has one.

Repeated equal indices are replaced by one representative per nonempty class.
For a selected subset, removing copies in pairs changes its positive root by
a factor $A_i\equiv1\pmod N$. This preserves every modular-root image.
Reducing the available class size modulo two would be false.

Fix $n=\lceil\log_2(N+1)\rceil$, a constant $C\ge1$, and
$H(n)=n^C$. Enumerating the factor-free states
$2\le u\le\min(H(n),N-1)$, computing their quotient indices, deduplicating,
and applying the decoder is one uniform deterministic polynomial-time
conditional algorithm. The same decoder applies to a trajectory interval of
polynomial numerical width. Neither construction proves that a useful
dependency exists, that such an interval is reached in polynomial time, or
that the completion bias correlates with a hidden factor. P65 is not a
factoring algorithm.

The final candidate, failed first audit, passing re-audit, and proof-blind
reconstruction have SHA-256 hashes
`4771cb22933a56e3811185be4f7a5becac5fd6e52c015770f49ef4a9be2e2984`,
`ef1ed485edf880c750b9285bc14cbdaf22eeefa33dfc1cc23590444e38b41a80`,
`0b9b4d5a4327122503d560d5906972bc17c89f04a47805165824036f75f6d6fb`,
and `47724940db357442e06c30c1fdd50727ceab5b7ce1f5ac303dbb2784577f7d1c`.
The passing re-audit pinned mathematical-content hash
`5fc697fe596b37b973813004a2463f5a234dc56c6be5f44a88d094a4a1b124d5`;
the later candidate changes were status and scope-label edits only.

## P66 — any explicit polynomial-size congruence list has a complete factor-free square decoder

**Status:** promoted deterministic conditional decoder. This is not a source
theorem and not a factoring algorithm.

**Prior-art boundary:** gcd-free or coprime bases are known infrastructure;
see Bach--Shallit and Bernstein. Detecting multiplicative relations with such
bases is also standard. The promoted project result is the exact synthesis and
scope below. No publication-level novelty is claimed without a dedicated
literature review.

Let $a_1,\ldots,a_m$ be positive integers, let $N\ge3$ be odd, and suppose
each $a_i$ comes with a known unit $x_i\bmod N$ such that

\[
x_i^2\equiv a_i\pmod N.
\]

Put

\[
L=m+\sum_i\left\lceil\log_2(a_i+1)\right\rceil,
\qquad
n=\left\lceil\log_2(N+1)\right\rceil.
\]

There is a deterministic algorithm polynomial in $L+n$ that uses gcd, exact
division, exact integer square tests, and binary linear algebra, but no prime
factorization, to compute pairwise-coprime blocks $g_j$ and exponent
coordinates

\[
a_i=\prod_j g_j^{e_{ji}}.
\]

One parity row $e_{ji}\bmod2$ for each nonsquare block gives a matrix $M$
with the exact equivalence

\[
Mc=0
\quad\Longleftrightarrow\quad
\prod_i a_i^{c_i}\text{ is an integer square}.
\]

For every supplied $c\in\ker M$, its exact positive root $R(c)$ is computable
in polynomial time. The theorem supplies an evaluator; it does not list all
$2^{\dim\ker M}$ vectors. Define

\[
X(c)=\prod_i x_i^{c_i}\pmod N,
\qquad
\rho(c)=R(c)X(c)^{-1}\pmod N.
\]

The positive-root overlap identity makes $\rho$ a homomorphism from
$\ker M$ to the square roots of $1\bmod N$. Therefore, if any square subset
has $R(c)\not\equiv\pm X(c)\pmod N$, every binary basis of $\ker M$ contains
a vector with the same non-global property. Testing only the basis vectors via

\[
\gcd(R(c)-X(c),N),
\qquad
\gcd(R(c)+X(c),N)
\]

then returns proper divisors. This covers arbitrary odd, possibly
nonsquarefree, $N$. Inputs $1$, duplicate integers, square integers, composite
nonsquare blocks, and repeated prime powers are all retained correctly.
Nonunit $x_i$ are outside the homomorphism premise; a proper
$\gcd(x_i,N)$ is already a factor.

P66 meets P01 with equality. It computes the true finite-list square-class
rank and does not compress it. It also does not make a dependency exist or
make a normalized root non-global. For inverse quotients, use
$a_i=Nk_i+1$ and $x_i=1$. The complete remaining step is source-side: produce
such a useful list from bare $N$ with an all-input inverse-polynomial law.

The final candidate, failed first audit, passing fresh re-audit, and strict
proof-blind reconstruction have SHA-256 hashes
`f30c5c1b25abe0d0a5df11f84afd2cf5e70ce4b3dcea9d368b25e2eb5b4022bf`,
`c826f43ae4d86b13d8910195ef1c41fda8895cdc7731f78af7fa35663f6d4314`,
`7f3107bec589462939d6ab02a135c86cf510cffea696f8439c9e2169c8a6f3e2`,
and `d3b61761b7bd980fc5fa3019f5106413c0d0d9740a60ab21a85ff0d64887112c`.
The passing re-audit pinned mathematical-content hash
`a103f1d42350e67ccda23792fc72b2d84beee2436c920678e3cfb83e5c03520c`;
the later candidate change was status-only. No research computation,
cross-family audit, or human audit ran.

## P67 — inverse-quotient trajectories have a sharper global bound and exact adjacent laws

**Status:** promoted narrow structural theorem and sublogarithmic contraction
obstruction. It proves neither polynomial trajectory depth nor factoring.

For a trajectory $u_0,\ldots,u_L$, let $v_i$ be the canonical inverse at
each unit source state and put

\[
r_i=u_i-u_{i+1},
\qquad
t_i=N-v_i.
\]

Every transition satisfies

\[
Nr_i=u_i t_i+1.
\]

The $t_i$ are positive and distinct. Combining this fact with logarithmic
telescoping gives the all-input bound

\[
\boxed{
\frac{L(L+1)}2<N\log N,
\qquad
L<\sqrt{2N\log N}.
}
\]

This includes a last transition to a proper nonunit. It is strictly sharper
than P62's $N^{1/2+o(1)}$ bound, but it is still exponential in the input bit
length.

When two consecutive unit transitions exist, define

\[
\delta_i=r_i t_{i+1}-r_{i+1}t_i.
\]

Then $\delta_i$ is a positive integer and

\[
\delta_i u_i=r_i^2t_{i+1}+r_{i+1}-r_i,
\qquad
N\delta_i=r_i t_i t_{i+1}+t_{i+1}-t_i.
\]

In particular, if $r_i,t_i,t_{i+1}\le B$, then
$B^3+B\ge N+1$. Also, $t_i/r_i$ and $v_i/u_{i+1}$ are the two Farey parents
of $N/u_i$, with

\[
v_i r_i-t_i u_{i+1}=1.
\]

The next transition uses $N/u_{i+1}$, not $v_i/u_{i+1}$. This numerator reset
is why the local Farey identity does not itself give Euclidean descent.

There is an explicit logarithmic-depth family. For positive integer $L$, put

\[
M=\operatorname{lcm}(2,\ldots,L+1),
\quad
A=M^2+M+1,
\quad
B=(M+1)^2,
\quad
N=AB.
\]

Then $N$ is a nonsquare composite, $1<B/A<2$, and

\[
L+1\longrightarrow L\longrightarrow\cdots\longrightarrow1
\]

is an all-unit trajectory with $\log N=\Theta(L)$. The family is not hard:
the first Fermat square test factors $N$ into $A$ and $B$. Its exact force is
narrower. For every nonnegative integer-valued $h(N)=o(\log N)$ and every
fixed $c<1$, these inputs eventually satisfy

\[
D_N^{h(N)}(L+1)>c(L+1).
\]

Thus no all-input proof can promise a fixed multiplicative contraction within
sublogarithmically many steps. A different invariant may still prove a
polynomial depth bound.

The final candidate, failed first audit, passing fresh re-audit, and strict
proof-blind reconstruction have SHA-256 hashes
`8d81f35c7dc3e20495acff9bffd71cd40becc224137e2cb95a7b68bfbb57229e`,
`d92188adcfbfee156b117495a0e651415f27368118e26c768cb3c7a0bebc5586`,
`b1189aafb5777e30e2fdff5b6153cb61c1690beb6e55465e6690f0a38f9f1607`,
and `1779aaaa7297ec31a0ecf0b5b6be907df36b44ec3ad14010d91d0de41007e5fb`.
The passing re-audit pinned mathematical-content hash
`e65df85135f4793096d49147ba066682c9afd134b7e166e5386bc1898698b05f`;
the later candidate change was status-only. No research computation,
cross-family audit, or human audit ran.

## P68 — unit-denominator generic dependencies are certified global-root decoys

**Status:** promoted source-filter theorem. This is not a source-success
theorem and not a factoring algorithm.

Let $N\ge3$ be odd. Let nonzero polynomials
$A_1(T),\ldots,A_m(T)\in\mathbb Q[T]$ satisfy

\[
A_i(0)=1,
\qquad
a_i=A_i(N)\in\mathbb Z_{>0},
\qquad
a_i\equiv1\pmod N.
\]

Let $K_N$ be the binary kernel of integer-square products of the $a_i$, and
let $K_{\rm gen}$ be the binary kernel of products that are squares in
$\mathbb Q(T)$. Then

\[
K_{\rm gen}\subseteq K_N.
\]

For $c\in K_{\rm gen}$, write the symbolic product as $S_c(T)^2$ and let
$d_c$ be the least positive coefficient denominator of $S_c$. If
$\gcd(d_c,N)=1$, then the positive numeric root satisfies

\[
R_N(c)\equiv\pm1\pmod N.
\]

Such a relation is therefore a global-root decoy. The denominator condition
is essential: at $N=15$, the generic square with

\[
S(T)=1-\frac45T+\frac1{15}T^2
\]

has $S(15)=4$ and factors $15$, even though its denominator gcd is the whole
modulus and $K_N=K_{\rm gen}$.

The harmless subspace is computable without factoring $N$. If $D_i$ is the
least coefficient denominator of $A_i$, exact Gauss valuations give

\[
d_c^2=\prod_iD_i^{c_i}.
\]

Hence

\[
U_N
=K_{\rm gen}\cap
\{c:c_i=0\text{ whenever }\gcd(D_i,N)>1\}.
\]

Let $\bar\rho_N$ map a square relation to its numeric root modulo the global
signs. Then

\[
U_N\subseteq Z_N:=\ker\bar\rho_N.
\]

The computable quotient $K_N/U_N$ is a certified residual search space. It is
not the exact signal quotient; the latter is $K_N/Z_N$. Thus a nonzero
$K_N/U_N$ is necessary for this decoder to succeed, but it is not sufficient.

The theorem causes a real algorithmic change. Compute $K_N$ with P66, compute
$K_{\rm gen}$ by rational-polynomial factor parity, remove $U_N$, and screen
only a basis of the remaining quotient. The constant-term condition makes the
residual rational unit a square whenever all nonconstant parities cancel, so
this step does not hide integer factorization. All work is polynomial in the
explicit lift/list size and $\log N$.

For the 12 audited F59 deterministic-offset batches, all 19 complete numeric
basis dependencies lie in $U_N$. Therefore every dependency in those batches
is a global decoy. This finite certificate does not imply an unbounded source
law.

The final candidate, failed first audit, passing fresh re-audit, proof-blind
reconstruction, and reconstruction computation manifest have SHA-256 hashes
`07d5fcd049a4047adff6651cc297df4646a1b43b5fab69b2d9b2c351da1983fb`,
`d514a92f48b64063e27b302551c4bc8b24e63f861174b5a060be5c3bd9588299`,
`20f557b82eb6afc25124471f2980e7b644e6f9d1bf63c536bfc0df1dd5ae9b68`,
`f7cd9b4ad1dd12ba338617845af4b93ca856a14ef8697851d5555e58f5f63af0`,
and `e0469b2e6b1d05b02a2d847e8ad13445aea7c376cb7671be00782f6465559eed`.
The passing re-audit pinned mathematical-content hash
`804d0776a1ba446b3e604cb19a7b6abdae4ed052589ae62723bf23b6e48b6c93`;
the final edits only clarified status, rational units, and the distinction
between the certified and exact signal quotients. No cross-family or human
audit has run. No publication-level novelty is claimed without a dedicated
literature review.

## P69 — one-block gcd-free feedback is saturated by a quotient-bounded scan

**Status:** promoted narrow adaptive-source redundancy theorem. This is not a
decoder obstruction and not a factoring algorithm.

Let $2\le x<N$ be a unit, let $y$ be its canonical inverse, and write

\[
xy=1+kN.
\]

Then $1\le k<x$. If $g>1$ divides $1+kN$, exactly the following useful
dichotomy applies:

\[
g\le k,
\quad\text{or}\quad
g>k\text{ and }
\iota_N(g)=\frac{1+kN}{g},\ k(g)=k.
\]

Now refine every known endpoint completely into pairwise-coprime gcd-free
blocks, while retaining exact block exponents and every endpoint presentation.
Feed one whole current block $g$ back as a canonical inverse state.

If the source consists exactly of all valid states $2\le x\le B<N$, the
feedback creates neither a new relation value nor a proper split of a current
block. If $g\le k$, state $g$ was already scanned because $k<B$. If $g>k$,
the feedback relation is the old value $1+kN$. Its complementary endpoint is
an exact product of whole current blocks, including multiplicities, so it
cannot refine a block.

More generally, let an explicit seed list have all quotients at most $K$.
Add every valid state

\[
2\le x\le\min(K,N-1)
\]

before the first complete refinement. This seed list plus saturation dominates
every finite sequence of one-block feedback steps. The added list has $O(K)$
states. The total size is the original seed-presentation size plus $O(K)$, so
it is polynomial when both that seed size and $K$ are polynomial in
$\log N$.

The order of bookkeeping matters. Different endpoint presentations of one
relation value must enter refinement before duplicate decoder columns are
removed. The theorem covers composite blocks, repeated block powers, one
block shared by several values, loose bounds $K\ge N$, and repeated feedback.

The result closes only “feed one whole current block.” It does not cover a
product, power, quotient, or unknown proper divisor of blocks; noncanonical
representatives; cross-relation constructions; or large selected states not
dominated by a polynomial quotient bound.

The final candidate, hostile audit, proof-blind reconstruction statement, and
reconstruction have SHA-256 hashes
`bb9ac13264f8213f8f1892525e328ef2461e0324824e234437e304c847fa3ac4`,
`da85af61e760e2e0a5016e3479e85aa5286adc220f54b28101a12b9b416754f9`,
`0b85bdd2e4c21d12580837d7280b9963f1aec3ba98932d9aba5ff2ae46986f9b`,
and `1ed6a8a99e37b25b41747be1af99bf228c4bd4d78bbdab39ff3b45d45df941a3`.
The audit pinned pre-clarification candidate hash
`c3ad4d4f5a210d64feeb803e9e8047e6d0b95310c08bed3aaf088d68fb253658`.
The final changes state the audit and reconstruction scope conditions; they do
not change the divisor or saturation proofs. No computation, cross-family
audit, or human audit ran. No publication-level novelty is claimed without a
dedicated literature review.

## P70 — cross-relation block feedback can escape one-block saturation

**Status:** promoted exact feedback theorem and special-family construction.
This is not an all-input selector and not a factoring algorithm.

Let

\[
A_i=x_i y_i=1+k_iN
\]

be canonical inverse relations. Completely refine their endpoints into
pairwise-coprime gcd-free blocks $q_j$, and retain every exact endpoint
exponent before decoder-column deduplication. For an indexed subset $S$,
write

\[
P_S=\prod_{i\in S}A_i=1+K_SN.
\]

Let $E_j(S)$ be the total exponent of $q_j$ in $P_S$. Select any

\[
g=\prod_jq_j^{c_j},
\qquad 0\le c_j\le E_j(S),
\qquad 1<g<N.
\]

If $w$ is the canonical inverse of $g\bmod N$ and

\[
gw=1+k(g)N,
\]

then the new quotient is exactly

\[
\boxed{k(g)=K_S\bmod g}
\]

in the least nonzero residue range $1,\ldots,g-1$. The proof is the exact
division $P_S/g=w+tN$, which gives $K_S=k(g)+gt$. Different subset
certificates for the same $g$ cannot assign different quotients.

This operation is strictly stronger than P69's one-block loop. At $N=21$,

\[
22=2\cdot11,\qquad 85=5\cdot17,\qquad g=2\cdot5=10
\]

give the new relation

\[
10\cdot19=190=1+9\cdot21.
\]

The complementary endpoint contributes the new block $19$, so feedback is
not closed in the old block set. The new three-column square kernel is still
zero, but the selected state itself factors because

\[
\gcd(10-1,21)=3.
\]

Thus the full direct target is broader than non-global square roots of one: a
selected residue can equal $+1$ or $-1$ in only one hidden CRT component
without being self-inverse globally.

There are also genuinely cross-relation self-inverse witnesses. At $N=55$,

\[
56=2\cdot28,\qquad 111=3\cdot37,\qquad g=3\cdot7=21.
\]

The two seed square classes are independent, while

\[
21^2=441=1+8\cdot55
\]

gives factors $5$ and $11$. This is not a power of one repeated relation.

Deliberate relation reuse changes the source exponent budget even though it
adds no independent decoder observation. With three authorized uses of
$22=2\cdot11$ at $N=21$, the old decoder has only global roots, but the
available power $2^3=8$ is self-inverse and splits $21$.

The power mechanism has an infinite exact family. For every odd $t\ge3$,
put

\[
g=2^t,
\qquad
N=\frac{g^2-1}{3}=(g-1)\frac{g+1}{3}.
\]

Use $t$ authorized copies of the quotient-one relation
$N+1=2(N+1)/2$. Every old decoded root is global, while

\[
g^2=1+3N,
\qquad
\gcd(g-1,N)=g-1,
\qquad
\gcd(g+1,N)=\frac{g+1}{3}.
\]

Here $t=\Theta(\log N)$, so the explicit source and selected integer have
polynomial bit size, while $g=\Theta(\sqrt N)$ is exponentially larger than
the seed quotient $1$. This disproves domination by a scan only through the
largest seed quotient.

The theorem does not choose $g$. The number of legal subsets and exponent
vectors can be exponential. Products above $N$ reduced modulo $N$, or
negative block exponents, define valid public residue selectors but are a
different operation and do not obey the displayed quotient formula. A full
algorithm must first handle even inputs and perfect powers, then prove that a
polynomial-size selector finds a direct CRT separator on every remaining odd
composite with inverse-polynomial probability.

The final candidate, hostile audit, proof-blind reconstruction statement, and
proof-blind reconstruction have SHA-256 hashes
`401bfb5b29724584455bb3d4edae93ebbe58f1224969f8c0fce19187b82b7072`,
`4cf5da70bd0d176db33f07e15d7ff6222cc55da2573bc95e2035a2f6139dfac6`,
`d2dbbbfc7ebac3b913172e136f2535ff55cb29cfdeee7ad39599622e2bb0d6cb`,
and `5245330fab0a5a52f833f98fbd7e7f30c07820a7916f5e3d18a747ac4083527b`.
The audit pinned the pre-correction candidate hash
`b18f37b176eb697e039946c713c8e20c38e7f2f5f97e2b463436b78719cce67e`;
the final version applies its required exponent-budget, direct-screen,
duplicate-semantics, and prime-power corrections. No research computation,
cross-family audit, human audit, or publication-level literature review
supports the theorem.

## P71 — cross-relation self-inverse selection is a bounded hidden-lattice problem

**Status:** promoted exact structural boundary after a failed first hostile
audit, a corrected fresh hostile re-audit, and a proof-blind reconstruction.
This is not an all-input selector and not a factoring algorithm.

Let $q_1,\ldots,q_s$ be public unit blocks and define

\[
\Phi_N:\mathbb Z^s\longrightarrow(\mathbb Z/N\mathbb Z)^\times,
\qquad
\Phi_N(v)=\prod_jq_j^{v_j},
\qquad
\Lambda_N=\ker\Phi_N.
\]

For a finite indexed set of relation occurrences, let
$L_0\subseteq\Lambda_N$ be the integer lattice generated by their exponent
rows. If a selected occurrence set has total exponent $E$ and a legal
whole-block divisor has exponent $0\le v\le E$ with $1<q^v<N$, then its two
endpoints are modular inverses. They are equal exactly when

\[
2v\in\Lambda_N.
\]

For odd $N$, a self-inverse residue other than the two global signs exposes
proper factors through both $\gcd(q^v-1,N)$ and $\gcd(q^v+1,N)$. This is only
a sufficient subtarget. The full direct screen can succeed when
$2v\notin\Lambda_N$; $N=21$ and $q^v=10$ give
$\gcd(10-1,21)=3$ although $10^2\not\equiv1\pmod {21}$.

The exact modular residue image of the old square-relation decoder is

\[
R_{\rm old}
=\{\Phi_N(v):v\in\mathbb Z^s,\ 2v\in L_0\}.
\]

This is not an equality of legal positive divisors. A representative can have
negative coordinates, lie outside every finite occurrence box, or have
integer magnitude at least $N$. In the quotient
$Q_0=\mathbb Z^s/L_0$ with $K=\Lambda_N/L_0$, the conditions
$x\notin K$ and $2x\in K$ characterize a nonidentity involution in the
generated residue group. Usefulness still needs a non-global residue outside
the old image and a legal bounded representative.

For one generator $a$ of exact order $r$, the least positive $e$ satisfying

\[
a^{2e}=1,
\qquad
a^e\ne1
\]

exists exactly when $r$ is even and then equals $r/2$. A total least-answer
oracle that returns `NONE` for odd order is Turing-equivalent to exact modular
order finding: after `NONE` on $a$, the element $-a$ has order $2r$ and its
least answer is $r$. Full recovery of $\Lambda_N$ contains unrestricted order
finding because one generator has kernel $r\mathbb Z$.

If a basis of $\Lambda_N$ is supplied, Smith normal form computes the finite
generated group and a basis of its 2-torsion in time polynomial in all supplied
and produced encodings. Screening at most $s$ basis residues finds a
non-global involution whenever the generated subgroup contains one. Pulled-back
exponents can be negative and therefore do not establish legal divisor
provenance. Output equality under $\Phi_N$ is exactly coset equality modulo
$\Lambda_N$; this is the algebraic hidden-subgroup identity, not a complete
efficient quantum implementation on the infinite domain.

Two finite witnesses separate the scopes. At $N=65$, the independent relation
rows for $66=2\cdot3\cdot11$ and $651=3\cdot7\cdot31$ admit the legal cross
choice $2\cdot7=14$, a non-global involution that factors $65$. At $N=187$,
the one-copy relation $188=2^2\cdot47$ has exactly the legal proper products
$2,4,47,94$, and none passes either direct screen. Nevertheless
$\operatorname{ord}_{187}(2)=40$, and $2^{20}$ is a non-global involution.
Thus useful unbounded subgroup data can be absent from the finite source box.

There is also an exact occurrence-multiplicity hierarchy. For odd $t\ge3$,
put

\[
G=2^t,
\qquad
N=\frac{G^2-1}{3},
\qquad
B=\frac{N+1}{2}.
\]

With fewer than $t$ indexed copies of $2B=N+1$, no legal divisor below $N$
is self-inverse. With $t$ copies, $G<N$, $G^2=1+3N$, and $G$ is a
non-global involution. The old parity decoder still yields only the global
identity, $\operatorname{ord}_N(2)=2t$, and $t=\Theta(\log N)$. This is a
lower bound on total occurrence multiplicity for the self-inverse subtarget,
not on support and not on the broader direct screen.

The result therefore blocks a false shortcut. A classical selector cannot be
obtained merely by naming the complete hidden lattice or its 2-torsion; that
contains order finding and ignores the finite-box constraint. The remaining
route is narrower: use the observed integer block presentation to find a legal
direct separator without recovering the full lattice. No such all-input
polynomial selector is known here.

The corrected candidate, failed first audit, passing hostile re-audit,
proof-blind statement, and proof-blind reconstruction have SHA-256 hashes
`b0d19ae14669dbe1330fafd22447919368149b497accf870387abbda1e891bae`,
`862c5dc768cee9a91933f9acfe5bdfdd9d4554eda81b3e2ded48a2bcb6d60289`,
`df9e18d00918bfcf96aa25f469f7d8bf93ad2a554b0d09123af86fb399e468a6`,
`9f140a320d5ec8267bb981b316ce9b72fdb7642872908d92abf5cf7241446bcc`,
and `6bbc0fce0620c983d86b970223dad56cb6cb2ab1af1fcccfafb0d72c821b3855`.
No computation, cross-family audit, human audit, or publication-level
literature review supports this theorem.

## P72 — fixed cross-relation orientations and fresh pivots remain diffuse

**Status:** promoted probability boundary after the first hostile audit found
an overbroad scope claim, the corrected theorem passed a fresh hostile
re-audit, and a proof-blind reconstruction succeeded. This is not a selector
or a factoring algorithm.

Let $X_1,\ldots,X_m$ be independent uniform units modulo $N$, and fix a
nonzero signed exponent vector
$\epsilon\in\{-1,0,1\}^m$. Then

\[
Z=\prod_iX_i^{\epsilon_i}\pmod N
\]

is exactly uniform in $(\mathbb Z/N\mathbb Z)^\times$. Conditioning on all
but one nonzero coordinate leaves a bijective identity-or-inversion map of
the remaining uniform unit.

For $N=pq$ with distinct odd primes, a nontrivial proper direct screen means
$1<\gcd(Z-1,N)<N$ or $1<\gcd(Z+1,N)<N$. Its exact probability is

\[
\boxed{\frac{2p+2q-10}{(p-1)(q-1)}}.
\]

The probability that $Z$ is a useful non-global square root of one is

\[
\boxed{\frac{2}{(p-1)(q-1)}}.
\]

The direct event is strictly broader: only one hidden component needs to
equal one selected sign.

For any fixed menu of $T$ signed patterns, entries can share inputs, coincide,
or be inverses. Joint independence is unnecessary. Marginal uniformity and a
union bound give

\[
\Pr(\text{some direct screen succeeds})
\le T\frac{2p+2q-10}{(p-1)(q-1)},
\]

and

\[
\Pr(\text{some useful involution appears})
\le\frac{2T}{(p-1)(q-1)}.
\]

These are upper bounds, not asymptotic equalities. On balanced semiprimes,
every polynomial-size menu has exponentially small success in the input bit
length.

The adaptive extension has an exact filtration condition. Before trial $t$,
let the full history determine a unit multiplier $C_t$ and a sign
$s_t\in\{+1,-1\}$. If $U_t$ is uniform conditional on that full history and
is not observed before the choice, then

\[
Z_t=C_tU_t^{s_t}
\]

is uniform conditional on every realized history. Prior failures do not
change the bound. A pivot that is only marginally uniform or physically
unseen is insufficient when it is correlated with the past.

The scope boundary is essential. A fixed menu can reuse base units, but a rule
that observes a unit before choosing its exponent can destroy uniformity even
without inspecting an integer factorization or endpoint presentation.
Correlated or nonuniform states are also outside the theorem. In particular,
P72 does not prove that integer block data is the only escape. P70's gcd-free
block, magnitude, multiplicity, and feedback operations are outside the model
and remain legitimate targets. The theorem only rules out the idea that
ordinary fixed multiplication of independent uniform relations creates factor
correlation by itself.

The corrected candidate, failed first audit, passing fresh re-audit,
proof-blind statement, and proof-blind reconstruction have SHA-256 hashes
`b7a56e611d4f679237a9923204daa188b820f01bf869712a6636d91cc9065bc2`,
`64fdc4370f5dbc2763ecbeeb1a74afa64e20ebbaa54aa6e5e62fc871b97b2b25`,
`f9c89f3f12aa597dd492a6e96b992647feeeb53dc839ff3b88246c2a08bcdeb4`,
`0ed9962e67d4ee5f1980b1d034b674b13c3a954edb62288d7f34795fd6e4fd4a`,
and `e76e918c555587381d81bc1618104bda7e445ddd56c8c0981d9cd69d68405240`.
No computation, cross-family audit, human audit, or publication-level
literature review supports this theorem.

## P73 — feedback creates a new dependency exactly at square-class closure

**Status:** promoted exact accounting theorem after a first proof-blind
reconstruction found two scope errors, the corrected result passed a fresh
hostile re-audit, and a corrected proof-blind reconstruction succeeded. This
is not a selector, a root-usefulness theorem, or a factoring algorithm.

Assume that $N$ is odd, or remove the factor $2$ first. Let indexed positive
relation values $B_1,\ldots,B_m$, all coprime to $N$, be represented after
complete gcd-free refinement by the parity matrix

\[
M\in\mathbb F_2^{r\times m}
\]

on pairwise-coprime nonsquare blocks. These block square classes are
independent even when the blocks are composite or prime powers. Hence
$\ker M$ is exactly the indexed rational-square relation space. Perfect-square
blocks can be omitted from the parity rows, but their exact exponent data must
remain available for root construction.

Append one indexed feedback value $B_{m+1}=gw$, jointly refine all old and new
values, and let $b$ be the new parity column in the refined coordinates.
Refinement can split old blocks, but it preserves the old column kernel. The
new nullity increases by one exactly when

\[
b\in\operatorname{colspan}_{\mathbb F_2}(M).
\]

Otherwise rank and column count both increase, so nullity is unchanged. In
particular, if any refined nonsquare row is zero on all old columns and one on
$b$, then $b$ cannot close in the old span. Arithmetically, a fully refined
block with odd **total** multiplicity in $gw$ and zero old parity row is such a
witness. Its occurrence in $w$ alone is insufficient because an odd
occurrence in $g$ can cancel it modulo squares.

For a feedback sequence, write

\[
d_t=(\text{number of indexed columns})-(\text{square-class rank}).
\]

Exact refinement preserves $d_t$. Every appended class either raises rank and
leaves $d_t$ fixed, or closes in the current span and raises $d_t$ by one. If
each appended column has a new-only nonsquare row at its insertion time, then
$d_t=d_0$ for every finite prefix. This preserves the initial nullity; it
implies absolute independence only when $d_0=0$. A block that is new-only now
can recur later and participate in a closure.

The strongest immediate closure is a canonical self-inverse state. If $w$ is
the canonical inverse endpoint of $g$ and $g^{-1}\equiv g\pmod N$, then $w=g$
as integers. Appending $g^2$ gives a zero parity column and one singleton
dependency. For odd $N$, both direct screens $\gcd(g-1,N)$ and
$\gcd(g+1,N)$ are proper exactly when $g$ is a non-global square root of one.

This theorem separates two jobs that must not be merged. Square-class closure
creates a dependency; P66's complete decoder computes its modular root. The
root can still be global, so closure alone does not reveal a factor. P73 gives
no closure frequency, no factor-correlated root law, and no polynomial-time
selector. It only proves the exact event that a feedback sampler must cause
before a *new* decoder dependency can exist.

At $N=21$, the feedback value $190=10\cdot19$ adds a private $19$ row, so the
three relation columns remain independent even though the direct screen of
$10-1$ already factors $N$. At $N=55$, the self-inverse state $21$ gives
$21^2=441$, a zero column, and direct factors $5$ and $11$. These witnesses
show that a new quotient and a new dependency are different events.

The corrected candidate, original hostile audit, failed first proof-blind
statement and reconstruction, passing fresh hostile re-audit, corrected
proof-blind statement, and corrected reconstruction have SHA-256 hashes
`210198cdbc8d15a67fe84577d80a41e8d501f6df23f80ed612989ebf322405ea`,
`9c0c7fd436d6b92baf52df5e21a70d1b78f01a4699effadcf199e556c773e557`,
`71ba7a01069657c4f66b1b88be4f22cecb5d928ec208cc8422486190f71cb9f6`,
`b69f425918a278d3311e3f9ffbc92d0a263837f2fd098e4f233bba171b4b2675`,
`4ff069a12fa753e3228a9928ecbef8944319644d77ea1928dfeb1006d0e0bc48`,
`86c041ea3d56fe2af0ef7682b4ed6b8d5c91c4c93979ca598da18c96e4f45395`,
and `1a0d7f05721045fa0a8fb5295f674efb75f51aae47bd1ec2f63e0b6a2b4ba7f0`.
No computation, cross-family audit, human audit, or publication-level
literature review supports this theorem.

## P74 — one square-class closure adds one canonical root coset

**Status:** promoted exact incremental decoder theorem after hostile audit and
strict proof-blind reconstruction. This is not a closure-frequency theorem, a
selector, or a factoring algorithm.

Let $N>1$ be odd, and let indexed positive relation values
$A_1,\ldots,A_m$ satisfy $A_i\equiv1\pmod N$. After complete exact gcd-free
refinement, let

\[
M\in\mathbb F_2^{r\times m},
\qquad K=\ker M
\]

represent their rational square classes. For $x\in K$, put

\[
\prod_iA_i^{x_i}=R(x)^2,
\qquad
\psi(x)=R(x)\pmod N,
\]

where $R(x)>0$ is the exact integer root. The overlap identity

\[
R(x)R(y)
=R(x+y)\prod_{i:x_i=y_i=1}A_i
\]

shows that $\psi:K\to\mu_2(N)$ is a homomorphism. Let
$H=\psi(K)$ be the complete old root image.

Append one indexed value $A_{m+1}\equiv1\pmod N$, jointly refine, and write
the new parity matrix as $[M\mid b]$. If $b$ is outside the old column span,
the kernel is exactly $K\times\{0\}$ and there is no new decoder output. If
$b$ closes, choose any $c$ with $Mc=b$ and put $z_c=(c,1)$. Then

\[
K'=(K\times\{0\})\oplus\langle z_c\rangle.
\]

The induced root and full new root image are

\[
s_c=\sqrt{A_{m+1}\prod_iA_i^{c_i}}\pmod N,
\qquad
H'=\langle H,s_c\rangle.
\]

Different solutions need not give the same literal root. If $c'$ is another
solution, then

\[
s_{c'}=s_c\psi(c'+c).
\]

Therefore the exact canonical object added by the closure is the coset

\[
s_cH\in\mu_2(N)/H,
\]

not a preferred residue representative.

Now suppose that a basis of the old kernel has already been screened with
both sign gcds and no proper factor was found. For arbitrary odd, possibly
nonsquarefree $N$, every non-global root of one splits the full odd
prime-power CRT components between the two signs. Hence failed old basis
screens prove

\[
H\subseteq G=\{1,-1\}.
\]

At the next closure, the enlarged complete decoder has a factor-bearing root
if and only if $s_c\notin G$. The class $s_cG$ is then independent of the
chosen lift. Thus one induced root test, together with the already screened
old basis, is complete. Before the old decode, only the $H$-coset is
canonical; replacing $H$ by the global signs can be false.

This gives an exact two-gate target for feedback:

1. the new parity column must close in the current square-class span;
2. its induced root coset must be non-global.

At $N=21$, two indexed copies of $22$ pass the first gate but have global
root $22\equiv1$. At $N=55$, the zero-column relation $21^2$ passes both
gates and its root exposes $5$ and $11$. The theorem proves exact incremental
accounting only. It gives no distribution or all-input method that makes
either gate occur.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
`87738f81027c00ded3e4861550b0de8faffa8fbc5787751780a406773d631328`,
`64200e4aef7643e078f05011c465d5124ca211a0cbc9abc88dc0ab1191005d9d`,
`199d4b6eb19c780a08d2f4acf668236ecdfe2307fcb57ed0d7ecde8432da65da`,
and `d23f801dd93b3b9d3b195ace94b8c1790fb5ef225a1cf516d4146474abaa837b`.
No computation, cross-family audit, human audit, or publication-level
literature review supports this theorem.

## P75 — the inverse-diagonal target has useful mass but resists three simple samplers

**Status:** promoted metric-target and access-obstruction theorem after
hostile audit, audit-directed precision corrections, and fresh proof-blind
reconstruction. It is not a general sampling lower bound or a factoring
algorithm.

Let $N=pq$ for distinct odd primes. For a canonical unit
$u\in\{1,\ldots,N-1\}$, let $v(u)$ be its canonical inverse and put

\[
d(u)=u-v(u),
\qquad
\delta(u)=|d(u)|.
\]

For a signed difference $d$, the exact fibre is

\[
F_d=left\{u:
\max(1,1+d)\le u\le\min(N-1,N-1+d),\quad
u^2-du-1\equiv0\pmod N
\right\}.
\]

With $\Delta_d=d^2+4$, the congruence has, before the canonical interval
cut, exactly

\[
\left(1+\left(\frac{\Delta_d}{p}\right)\right)
\left(1+\left(\frac{\Delta_d}{q}\right)\right)
\]

roots. Hence every signed fibre has at most four elements. Inversion gives
$|F_d|=|F_{-d}|$. The public discriminant ticket
$\gcd(d(u)^2+4,N)$ detects a local root of $u^2=-1$; uniform proposals hit a
proper ticket with probability at most $2/(p-1)+2/(q-1)$.

Now weight the inverse graph by

\[
w(u)=\frac1{1+\delta(u)},
\qquad
\pi(u)=\frac{w(u)}{Z_N}.
\]

The four roots of one have distance zero. Two are global and two expose the
factors. The four-point fibre bound gives

\[
4\le Z_N\le8H_{N-1}-4,
\]

so the two useful roots have mass

\[
\pi(M_N)=\frac2{Z_N}
\ge\frac1{4H_{N-1}-2}
=\Omega\!\left(\frac1{\log N}\right).
\]

Therefore a sampler within total-variation distance
$1/(8H_{N-1}-4)$ of $\pi$ would still factor with inverse-polynomial
probability. The target signal is large enough; efficient access is the open
part.

Three natural access rules fail.

1. Uniform rejection accepts with probability $Z_N/\varphi(N)$ and needs
   $\Omega(N/\log N)$ proposals in expectation.
2. Independent uniform-proposal Metropolis--Hastings has
   $\Omega(N/\log N)$ worst-start mixing time. From a uniform start, its
   probability of entering the useful two-point set by time $t$ is at most
   $2(t+1)/\varphi(N)$, so polynomially many steps also miss the required
   target accuracy on balanced inputs.
3. Nearest-neighbor descent has sealed factor-free minima. If
   $u^2+u-1\equiv0\pmod N$ and $\gcd(N,5)=1$, then $u,u+1$ are inverse
   states of distance one, while both outer neighbors have larger distance.
   The discriminant ticket is $5$ and is trivial. The smallest clean example
   with two distinct odd prime factors is

   \[
   N=209=11\cdot19,
   \]

   where the four consecutive distances at $79,80,81,82$ are
   $48,1,1,48$.

The first two costs are exponential in the input bit length. These results
rule out only the named rejection, proposal kernel, and line descent. Larger
or block-guided moves, nonuniform correlated sources, and other metric
samplers remain open. P75 therefore manufactures a mathematically adequate
metric target, but not a way to sample it from bare $N$.

The corrected candidate, amended hostile audit, proof-blind statement, and
fresh proof-blind reconstruction have SHA-256 hashes
`0037947187b324ff655a539bbff8dd82d68c8fe52e8c0a0edcd34fab20b8568e`,
`329b0986ee40cb177d7cf57b3bc341d3855da76109f9a7613e3f8b81a47d1787`,
`c25264a5fcc7490b734daeca8cff985d4071423c2e97f818c8f480e8653ea79c`,
and `694851544bef297dfc529597eecdae0b5d17e86d51f72bce6e4116bbc03bc5d8`.
No computation, cross-family audit, human audit, or publication-level
literature review supports this theorem.

## P76 — endpoint refinement can enlarge the block-generated subgroup

**Status:** promoted exact adaptive witness and metric boundary after a failed
first hostile audit, a corrected passing re-audit, and a strict proof-blind
reconstruction. This is not an all-input selector or a factoring algorithm.

For a unit \(r\), let \(w\) be its canonical inverse modulo \(N\), and put
\(d=r-w\). The public distance and discriminant screens contain no new
torsion mechanism:

\[
\gcd(d,N)=\gcd(r^2-1,N).
\]

If \(N\) is squarefree, then also

\[
\gcd(d^2+4,N)=\gcd(r^2+1,N).
\]

Thus ranking by \(|d|\) only reorders exact \(r^2=1\) and \(r^2=-1\)
tickets. It does not make them more frequent. Small distance is not monotone
toward a factor. At \(N=143\), two pairs have the same distance \(7\), but
only one pair product is an integer square. At \(N=77\), retaining a global
identity can give a conditional fixed point. These examples rule out a
universal inverse-distance ranking argument for the exact screened
distinct-block support-two menu.

Canonical endpoint feedback nevertheless has a real representation-level
effect. At

\[
N=209=11\cdot19,
\]

start from

\[
31\cdot27=1+4N,
\qquad
3\cdot70=1+N.
\]

The old gcd-free blocks are \(\{3,31,70\}\). The exact distinct-block
support-two menu has the two non-global inverse orbits

\[
\{80,81\},
\qquad
\{9,93\}.
\]

The first orbit has the unique smallest positive distance. It passes none of
the immediate direct, discriminant, or integer-square screens. Append

\[
80\cdot81=1+31N.
\]

Joint gcd refinement uses

\[
80=2^4\cdot5,\qquad
81=3^4,\qquad
70=2\cdot5\cdot7,\qquad
27=3^3
\]

and produces the blocks \(\{2,3,5,7,31\}\). The next exact support-two menu
contains \(2\cdot5=10\), and

\[
\gcd(10+1,209)=11.
\]

Before feedback,

\[
70\equiv3^{-1},
\qquad
31\equiv3^{-3}\pmod {209},
\]

so the subgroup generated by the old block residues is
\(H_0=\langle3\rangle\). The feedback endpoints \(80=3^{-4}\) and
\(81=3^4\) remain in \(H_0\). Yet \(10\notin H_0\), because the reduction of
\(\langle3\rangle\) modulo \(11\) has order \(5\) and does not contain
\(-1\). Therefore integer gcd refinement, not the endpoint residue, strictly
enlarges the block-generated subgroup.

This is an algorithm-level change, but its scope is narrow. The exact menu
does not include repeated indices, higher powers, a free global minus sign,
or support-one candidates. Also, \(H_0\) already contains another direct
separator, \(3^5=34\bmod209\). The witness proves strict subgroup expansion
and a new success inside the declared bounded menu. It does not prove that
feedback is necessary against every algorithm using arbitrary old-block
monomials.

The remaining claim is source-side. One must select polynomially many
feedback endpoints and prove that their integer overlaps cause either a
direct separator or P74's two-gate non-global closure with
inverse-polynomial probability on every input. Distance alone gives no such
law.

The corrected candidate, failed first hostile audit, passing fresh re-audit,
proof-blind statement, and corrected proof-blind reconstruction have
SHA-256 hashes
`e6413ba7703a5daa371a104a15a10c326fb881c2538f6dbd7b1cf3fec304de79`,
`6a07f63e7f61e8b644947d4a385839b68cc1582dbbae41ad1ad46b03f2ef40e5`,
`b454f483c961af2330c72103f1fcf926683e3a5b76355a56c43a33aaa44042fa`,
`46144733d8239f5914209b06be43809d742eb151177a07dae3638f69cb811494`,
and `08114b9f4bc476449bdd48135c371f1ce2a53c3adca24465107ec343eaede7c5`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P118 — adaptive named refinement has a deterministic quasipolynomial closure

**Status:** promoted from F130 after a hostile audit and an independent
proof-blind reconstruction. This is a terminating adaptive source and cost
theorem. It is not an all-input success theorem or a factoring algorithm.

Let

\[
n=\lceil\log_2(N+1)\rceil,quad
L=\lceil\log_2(n+1)\rceil,quad
D=L^2,quad E=2^{L^2}.
\]

After standard preprocessing, take every unit seed

\[
2\le s\le\min(E+1,N-1)
\]

and its canonical inverse. Complete gcd-free refinement and maximal
perfect-power extraction give the first **named generator basis**. This basis
and the later P66 **decoder basis** are different objects. A decoder-only
factor never becomes a named generator.

At each stage, freeze the named basis and exhaust every word

\[
u=\prod_{j\in S}q_j^{e_j},qquad |S|\le D,quad1\le e_j\le E.
\]

For the canonical residue (c=[u]_N), compute its canonical inverse (w),
run both direct signs, insert both integer endpoints into the exposure batch,
and permanently retain the exact value (P(c)=cw). Residues can be deleted
on first occurrence inside a frozen stage. Exact values can be globally
deleted only after every endpoint pair has been inserted.

After the complete scan, jointly refine the old named blocks with every new
endpoint. Keep as future generators only terminal blocks that occur in an
old named block. Discard probe-only cofactors from the named grammar, but not
from the final relation decoder. Normalize perfect powers, freeze the new
basis, and repeat. Stop only when the named basis is unchanged. Then run one
complete P66 decode on every distinct retained exact value.

This construction is adaptive in an algorithmic sense. A new endpoint can
split an old block and thereby change the future word grammar. It is not
equivalent to one fixed static word list. The complete old stage must be
scanned before a split is applied, because an old bounded word can exceed the
new coordinate caps after expansion on its descendants.

The process nevertheless has deterministic bit complexity

\[
\boxed{2^{O((\log n)^4)}}.
\]

To prove this, let (A_0) be the fixed initial endpoint product. Every named
block is a descendant of (A_0), and the product of the named blocks divides
(A_0). The initial product has at most

\[
2nE=2^{O(L^2)}
\]

bits. Complete multiplicity-aware refinement and perfect-power normalization
make every strict stage split at least one old block into two or more
descendants. Thus both the named block count and the number of stages are
(2^{O(L^2)}). At one stage,

\[
\sum_{s\le D}\binom MsE^s
\le(D+1)(ME)^D
=2^{O(L^4)}.
\]

Every endpoint and relation value has (O(n)) bits. All refinements,
storage, parity linear algebra, exact products, roots, and gcds are
polynomial in this explicit quasipolynomial transcript.

Residue deletion is lossless because a residue fixes both canonical
endpoints. Equal exact values add only duplicate kernel directions whose
positive root is (P\equiv1\pmod N); deleting them preserves the normalized
root image. Every earlier dependency extends by zero on later columns, so
one final complete kernel-basis decode is sufficient.

The enlarged seed bank eventually contains every fixed polynomial seed
range. It does not necessarily contain every word presentation formed by a
smaller seed bank on its different, less-refined basis.

The exact missing theorem remains:

> For every surviving composite input, some declared direct screen succeeds,
> or the final retained parity kernel has a non-global normalized-root image.

P118 proves that this is one finite uniform quasipolynomial algorithmic gate.
It proves neither rank closure nor root asymmetry.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`56c47a3737d1fb1be697757a2b5268b7bdb107fc36ad2a49f55442e4a5293824`,
`8740ffeed6d94f0530c2f499dabe6c39c0c3a62c7cf29a0dde1ef832f5e9eaf6`,
`c97d6454ea277211e25f24da5babd8ca7a6346377678365d8a654b072f28f0f1`,
and
`59ffa2d211fbb254180073df576b43f3db7ce328791219ed9ecf90d1507ce055`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P117 — support layers have an exact cross-quotient and relative-root accounting

**Status:** promoted from F129 after a corrected candidate passed a fresh
hostile audit and an independent proof-blind reconstruction. The first
formal re-audit failure remains preserved. This is an exact decoder theorem
for a fixed finite source. It is not a source-success law or a factoring
algorithm.

For every distinct retained canonical-inverse exact value (P), define its
intrinsic source support (sigma(P)) as the minimum generator support over
every declared presentation of either endpoint before exact-value deletion.
This makes the layer independent of enumeration order. Let (A_s) be the
prime-parity matrix of the values with (sigma(P)=s), all in one aligned row
space, and put

\[
U_s=[A_1\;\cdots\;A_s],qquad
K_s=\ker A_s,qquad
\widehat K_s=\ker U_s.
\]

For (s\ge2), define the genuinely cross-layer quotient

\[
C_s=
\widehat K_s/(\widehat K_{s-1}\oplus K_s).
\]

Then

\[
\boxed{
C_s\simeq
\operatorname{im}U_{s-1}\cap\operatorname{im}A_s
}
\]

and, for every (d\ge1),

\[
\boxed{
\dim\widehat K_d
=\sum_{s=1}^{d}\dim K_s
+\sum_{s=2}^{d}\dim C_s.
}
\]

Let (T_N) be the square roots of one modulo (N), modulo the two global
roots. Write (H_{\le s}) and (H_s) for the normalized-root images of the
cumulative and pure-layer kernels. The root assignment does not naturally
descend from (C_s) directly to (T_N) in general. Its exact canonical form
is the relative map

\[
\boxed{
\bar\rho_s:C_s\longrightarrow
T_N/(H_{\le s-1}+H_s),qquad
\operatorname{im}\bar\rho_s
=H_{\le s}/(H_{\le s-1}+H_s).
}
\]

On the decoder-failure path (H_{\le s-1}=H_s=0), this is an ordinary map
to (T_N). Thus the complete decoder first becomes useful in exactly one of
two ways: a pure layer has a non-global root, or a cross quotient has a
nonzero relative root image.

The cross quotient also has the necessary bound

\[
\dim C_s\le |S_s|,
\]

where (S_s) is the set of parity rows shared by the old and new layers. If
each new column has its own private odd-valuation row, then (C_s=0). A
shared rational-prime row between

\[
1+\kappa N,qquad1+\kappa'N
\]

requires

\[
\kappa\equiv\kappa'\equiv-N^{-1}\pmod r.
\]

This carry collision is necessary, not sufficient.

Finally, there are exact-congruence lists with arbitrarily large (C_2) but
zero complete normalized-root image: take independent primes
(a_i,b_i\equiv1\pmod N), put (a_i,b_i) in layer one and (a_ib_i) in
layer two. The cross triples have roots (a_ib_i\equiv1\pmod N). These
values exceed the canonical-inverse size range, so this is not an F26-Q
counterexample. It proves that retention, cross rank, and root usefulness
are separate invariants.

The exact consequence is a two-gate theorem target. A positive source law
must first defeat private rows and create a pure or cross dependency. It
must then make the corresponding normalized-root image non-global. Relation
count or cross nullity alone proves neither gate.

The statement, proof, failed first audit, passing hostile audit, and blind
reconstruction have SHA-256 hashes
`51db643888e6902c491a89f1258db4e4a582cea46a33be19284cee305047ac94`,
`f82d10b3480de4197592ae10725d73b9969dce4f80670dca2967d28223eb06b9`,
`6377454e7a9c07d6b172460ecec91f6e368a2a1b29221632a1783c22d5efc0f1`,
`60a27293d521b6fc1b86edf3b1e752de75b058606f3f84a935864410df4b58bb`,
and
`2a9209a70e188ca6f6e91e5aa28d94f2273295e6f066ce956ed918014a3e6e42`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P115 — numerically small unreduced rectangles have an exact carry obstruction

**Status:** promoted from F127 after the corrected theorem passed a fresh
hostile audit and a fresh proof-blind reconstruction. The first version's
endpoint overclaim and the first V2 statement's under-specification remain
preserved. This is a source boundary for P114. It is not a factoring
algorithm or a null for the complete F26-Q source.

Let \(N\) be composite, with least prime divisor \(h\). Let
\(u,a,b\) be positive units with \(uab<N\). For every divisor \(m\) of
\(uab\), put

\[
K_m=(-N^{-1})\bmod m,
\qquad 0\le K_m<m.
\]

This is the canonical carry because

\[
w_m={1+K_mN\over m}
\]

is the least positive inverse of \(m\) modulo \(N\). Divisibility gives
\(K_s\equiv K_r\pmod r\) whenever \(r\mid s\). Therefore there are unique
digits

\[
K_{ua}=K_u+uA,
\quad
K_{ub}=K_u+uB,
\quad
K_{uab}=K_u+uT,
\]

with \(0\le A<a\), \(0\le B<b\), \(0\le T<ab\), and

\[
T\equiv A\pmod a,
\qquad
T\equiv B\pmod b.
\]

This does not require \(a\) and \(b\) to be coprime. Substitution into the
P114 rectangle residual gives the exact formula

\[
\boxed{
\Omega_{\square}
=u[(b-a)T+(ab-1)(A-B)].
}
\]

With \(M=\max(a,b)\),

\[
\boxed{
|\Omega_{\square}|<2uabM.
}
\]

If \(a,b>1\), \(a\ne b\), and \(h>2uabM\), the residual and each P114
eligibility-factor screen give only gcd \(1\) or \(N\). This bound does not
cover ordinary endpoint signs. If instead \(u,a,b\le R\), \(R\ge2\), and

\[
h>R^6+1,
\]

then every corner \(c\le R^3\) satisfies \(c^2+1<h\). The identities

\[
\gcd(c-w_c,N)\mid c^2-1,
\qquad
\gcd(c+w_c,N)\mid c^2+1
\]

then kill all eight endpoint signs as well. Thus the full local rectangle
channel is null or global.

For a menu of \(Q\ge1\) canonical unit residues, let \(T_R\) count entries
whose numerical representative exceeds \(R\). If \(2R^4<h\), every proper
residual or prefactor hit must use at least one large entry. Hence its raw
ordered-triple fraction is at most

\[
{Q^3-(Q-T_R)^3\over Q^3}
\le {3T_R\over Q}.
\]

Under \(R^6+1<h\), the same statement includes endpoint signs. On balanced
\(n\)-bit semiprimes, every numerical
\(R=2^{O((\log n)^k)}\) is eventually below both thresholds. This is a
numerical-magnitude statement, not a description-length statement.

Two infinite fixed traps show both global outcomes. If

\[
(u,a,b)=(1,2,3),
\qquad N\equiv5\pmod6,
\]

then

\[
(K_1,K_2,K_3,K_6)=(0,1,1,1),
\qquad \Omega_{\square}=1.
\]

If

\[
(u,a,b)=(1,3,7),
\qquad N\equiv23\pmod {42},
\]

then

\[
(K_1,K_3,K_7,K_{21})=(0,1,3,10),
\qquad \Omega_{\square}=0.
\]

Fixed-modulus prime number theorems in arithmetic progressions give
infinitely many balanced distinct-prime semiprimes in both classes. Once the
hidden factors exceed the fixed corner squares, all endpoint screens are
also nonproper. More generally, every fixed finite bank of literal,
\(N\)-independent unreduced integer triples fails on all sufficiently large
balanced semiprimes.

The result does not cover wrapped rectangles, a numerically large or
adaptive selector, or the retained P66 decoder. Its exact force is to remove
small unreduced P114 rectangles and fixed banks from the surviving source
theorem. The first hostile version incorrectly used \(2R^4<h\) for endpoint
screens; the preserved certificate

\[
N=577\cdot587,
\quad (u,a,b)=(4,2,3),
\quad 24^2+1=577
\]

refutes that overclaim and is excluded by the final \(R^6+1\) threshold.

The final statement, proof, hostile audit, failed first proof-blind report,
and passing second proof-blind report have SHA-256 hashes
`56ecc3f749381b36743117df3405182ae25e035d7a1bcfc47446390665a7acb9`,
`1c6fbe2f1ff0ecd7123d975f6728604635143f71ac3113c1ac54b19701dbaa0d`,
`81a3325a19c8cdd395880f9aeb3226e7b10ef438ea598a51d3c51a8a9d75060d`,
`7731df34afbf69aa2b22d2c601cb5d150d10aa4f18bab4ae7f75863381b1b54c`,
and
`3fca5432c837080ea0eafffb478ed02204b1795de86be0e5b608d24c359be2e6`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P113 — any fixed finite seed-carry pattern can be programmed on balanced trial-hard semiprimes

**Status:** promoted after a hostile audit and an independent proof-blind
reconstruction. This is a fixed-dimensional source obstruction. It is not a
complete-source obstruction or a factoring lower bound.

Fix \(m\ge1\), independent of \(N\). Fix distinct rational primes
\(g_1,\ldots,g_m\) and integers \(1\le k_i<g_i\). There are infinitely many
balanced odd distinct-prime semiprimes \(N=pq\) such that, for
\(n=\operatorname{bitlength}(N)\),

\[
p,q>n^2,
\qquad
g_i\le n,
\]

and the least positive inverse of \(g_i\bmod N\) is

\[
w_i={1+k_iN\over g_i}.
\]

Both direct screens are null:

\[
\gcd(g_i-w_i,N)=\gcd(g_i+w_i,N)=1.
\]

Every exact pairwise-coprime positive-integer block basis with nonnegative
exponent presentations of all seed endpoints contains the block \(g_i\).

If the \(k_i\) are pairwise distinct, fixed distinct auxiliary primes \(r_i\)
can additionally satisfy

\[
v_{r_i}(1+k_iN)=1,
\qquad
r_i\nmid1+k_jN\quad(j\ne i).
\]

Thus each \(r_i\) is a valuation-one row private among the selected exact
values \(1+k_iN\).

### Proof

Prescribe

\[
N\equiv-k_i^{-1}\pmod {g_i}
\]

for every \(i\), and prescribe \(N\equiv1\pmod2\) if needed. CRT gives a
reduced class \(A\pmod M\), with fixed \(M\). Choose primes

\[
p\equiv1\pmod M,
\qquad
q\equiv A\pmod M
\]

in the disjoint intervals \([X,1.1X]\) and \([1.2X,1.3X]\). The prime number
theorem in fixed arithmetic progressions supplies them for all sufficiently
large \(X\). Disjoint increasing choices of \(X\) give infinitely many
pairs. Since \(p,q=\Theta(X)\), the input length is
\(2\log_2X+O(1)\); trial hardness and \(g_i\le n\) follow for large \(X\).

The CRT condition makes \(w_i\) an integer. Also

\[
0<1+k_iN\le1+(g_i-1)N<g_iN,
\]

so \(0<w_i<N\), and \(g_iw_i\equiv1\pmod N\). Hence \(w_i\) is the
canonical inverse with carry \(k_i\). Multiplication by the unit \(g_i\)
gives

\[
\gcd(g_i\mp w_i,N)=\gcd(g_i^2\mp1,N).
\]

Both factors of \(N\) eventually exceed every fixed \(g_i^2+1\), proving the
direct-null claim. The prime endpoint \(g_i\) can have only the one-block
monomial presentation \(g_i^1\), proving the block claim.

For the strengthening, choose distinct odd primes \(r_i\) larger than all
\(g_j\) and all \(|k_u-k_v|\). Add the coprime CRT conditions

\[
N\equiv(r_i-1)k_i^{-1}\pmod {r_i^2}.
\]

Then

\[
1+k_iN\equiv r_i\pmod {r_i^2},
\]

while for \(j\ne i\),

\[
1+k_jN\equiv(k_i-k_j)k_i^{-1}\not\equiv0\pmod {r_i}.
\]

This gives the private valuation-one rows.

The prescription is fixed while \(N\) grows. It does not program
\(m=m(n)\), the full initial block basis, polylog-support words, or their
canonical reductions. Other source columns may reuse every \(r_i\). P111 is
stronger for a growing cross-pair submatrix; P113 adds arbitrary fixed seed
carries and balanced factors.

The statement, proof, hostile audit, and proof-blind reconstruction have
SHA-256 hashes
`196cd165a89dfe69cd9e3896ad660d0402cb17d14b7e5f2db864fd2e4a589ad6`,
`ad81580820b1699a1ee6eceaf4bf26b856752c46fd0e00ebe69947e7c2044138`,
`de1a21b66f3face73c7147d1b8b8a6bb05cb25f15ab5f9d01655a84f50ef016d`,
and
`e7a8463a2e533ea8c051dc341a3c79b8a8bba4c1f863b487acce571e321d0634`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P77 — raw balanced relation partitions do not give a universal selector

**Status:** promoted exact magnitude and counterexample theorem after hostile
audit and strict proof-blind reconstruction. This is not a hardness theorem
for partition algorithms and not a factoring algorithm.

Let one retained exact relation be

\[
A=\prod_jq_j^{E_j}=1+kN,
\]

where the \(q_j\) are pairwise-coprime gcd-free blocks. A
balanced-canonical split chooses complementary exponent vectors and requires

\[
A=gh,
\qquad
1<g,h<N.
\]

Such a split can exist only when

\[
A\le(N-1)^2,
\qquad
k\le N-2.
\]

Equality forces the global pair \(g=h=N-1\). An aggregate of at least two
nontrivial relation occurrences satisfies

\[
A\ge(N+1)^2.
\]

For every \(1<g<N\), its raw complement \(A/g\) is then greater than \(N\).
The canonical inverse endpoint is the raw complement reduced modulo \(N\),
so ordinary integer or logarithmic partitioning optimizes the wrong number.

For one relation, an exact complementary split only re-presents the old
value. It introduces no new integer block, has the same square-class column,
and an appended duplicate has modular root \(1\). It changes the later search
only if the algorithm explicitly charges another occurrence and enlarges the
allowed exponent capacity.

Multiplicative balance also has the wrong precision scale. If \(g\le h\) and

\[
\beta=\frac12\log(h/g),
\]

then exactly

\[
h-g=2\sqrt A\,\sinh\beta.
\]

When \(A=\Theta(N^2)\), guaranteeing an additive
\(\operatorname{poly}(\log N)\) gap from a log-balance certificate requires
\(\beta=2^{-\Omega(\log N)}\). This is a precision boundary, not a
complexity lower bound for every exact algorithm.

Even a free exact closest-partition oracle does not give a factoring law. At
\(N=209\), the relation

\[
80\cdot81=6480
\]

is the unique closest divisor pair and passes none of the named direct or
discriminant screens. The same block box contains the farther split

\[
45\cdot144=6480,
\qquad
\gcd(45-1,209)=11.
\]

There is also an infinite exact support obstruction. Put

\[
F(z)=z^2+z-1.
\]

For every positive multiple \(t\ge5\) of \(5\), let

\[
a=F(t),
\qquad
b=F(t+1),
\qquad
N=ab.
\]

The factors \(a,b>1\) are odd, coprime, and asymptotically equal. CRT gives
a unique canonical \(u\) with \(u\equiv t\pmod a\) and
\(u\equiv t+1\pmod b\). Then

\[
u(u+1)=1+kN
\]

for some \(k\ge1\). In the exact two-block box
\(\{u,u+1\}\), this consecutive pair is the sole admissible unordered split.
All four endpoint sign screens, the discriminant-\(5\) screen, and the
integer-square screen fail. Every distribution supported on this declared
split set therefore has zero useful mass for those tickets.

The scope is essential. This family is not a general factoring lower bound:
if \(t\) is supplied, then \(\gcd(u-t,N)=a\). Modular reduction of oversized
cross-relation complements, internal block refinement, other block
statistics, and explicitly charged occurrence amplification are outside the
theorem. The result closes raw balance as a universal justification, not the
broader endpoint-refinement route from P76.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
`0501b6f40e150c53b22ffd9119e42f9136bec0f77945ed451fc852f03841fe36`,
`3bfe6b0150e982e0ee191b4124e11e5ce81d7c1cec0d1fd332395c19e889f810`,
`218244fb1c1532df0e9f3bbbc836e1e6e0d607f49517ca9d82901ef8211df5f3`,
and `be625fdc995dae3cec63a36984014e0fa791c62ecd792899cb9dbf5614c74195`.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.


## P78 — endpoint refinement can create a factor-bearing subgroup beyond a separator-free old subgroup

**Status:** promoted exact representation-level feedback theorem and selector
boundary. This is not a uniform selector or a factoring algorithm.

**Verification record:** the first hostile audit accepted the core arithmetic
but rejected five scope claims. The corrected version passed a fresh audit.
A first proof-blind statement then failed because it left the screens and
domains undefined and called a whole-block containment the sole overlap. The
candidate was corrected again. Its exact final version passed a new hostile
audit and a fresh proof-blind reconstruction. No research computation,
cross-family audit, human audit, or publication-level literature review ran.

Let a positive endpoint transcript have pairwise-coprime nontrivial gcd-free
blocks. After appending one canonical inverse relation, let \(\sigma\) count
the extra descendants created by splitting old block types, and let \(\nu\)
count private new block types. If \(r,r'\) are the old and new block counts,
then

\[
r'=r+\sigma+\nu.
\]

For any fixed finite transcript of positive endpoints, if \(R\) is its final
block count and

\[
L=\sum_x\left\lceil\log_2(x+1)\right\rceil,
\]

then

\[
R\le L,
\qquad
\sum_t(\sigma_t+\nu_t)=R-r_0\le L-r_0.
\]

This is only accounting. In an adaptive run, every new endpoint also enlarges
\(L\), so the identity gives no polynomial stopping bound.

At

\[
N=4033=37\cdot109=\Phi_{36}(2),
\]

the element \(2\) has order \(36\) modulo both prime factors. Hence

\[
H_0=\langle2\rangle
\]

has no direct sign separator: the exponents giving \(+1\) or \(-1\) are the
same in both CRT components.

There is an infinite immediate-square family that shows old-block splitting
is not necessary. For odd \(s>1\), \(s\equiv1\pmod3\), put

\[
N_s=\frac{4s^2-1}{3}
=(2s-1)\frac{2s+1}{3}.
\]

Two charged copies of \(N_s+1\) authorize \(g=4\). Its canonical inverse is
\(w=s^2\), and

\[
gw=4s^2=1+3N_s=(2s)^2.
\]

The old duplicate dependency has only the global root
\(N_s+1\equiv1\pmod{N_s}\), while the new root \(2s\) gives both displayed
factors. On the subfamily \(s\equiv55\pmod{1530}\), all declared sign,
difference, and discriminant gcd screens fail before the exact-square screen.
At \(s=55\), this gives \(N=4033\), \(w=3025\), and \(\sigma=0\).
The private square endpoint gives positive total block gain, so the exact
conclusion is only that positive old-block splitting is unnecessary.

A separate \(N=4033\) history proves strict subgroup expansion. Start from

\[
2\cdot2017=1+N,
\qquad
64\cdot3970=1+63N,
\qquad
8\cdot3529=1+7N.
\]

Complete refinement gives

\[
Q_0=\{2,2017,1985,3529\},
\qquad
H(Q_0)=H_0.
\]

The legal occurrence product

\[
g=2^{11}=2048
\]

has canonical inverse \(w=3905\), with

\[
gw=1+1983N.
\]

All immediate screens fail. The containment
\(\gcd(2,2048)=2\) reuses one whole old block and does not split it. The only
proper refinement-causing overlap is

\[
\gcd(1985,3905)=5.
\]

It gives

\[
1985=5\cdot397,
\qquad
3905=5\cdot781,
\]

\[
Q_1=\{2,2017,5,397,3529,781\},
\qquad
\sigma=1,\quad\nu=1.
\]

The private odd block \(781\) prevents immediate square-class closure.
Nevertheless,

\[
H(Q_1)=\langle H_0,5\rangle\supsetneq H_0.
\]

Strictness follows from

\[
5=2^{23}\pmod {37},
\qquad
2^{23}=77\ne5\pmod {109}.
\]

The enlarged subgroup contains

\[
x=5\cdot2^{-23}=5\cdot2^{13}=630\pmod {4033},
\]

and

\[
\gcd(x-1,4033)=37.
\]

This is a genuine representation-level gain: both feedback endpoint residues
were already in the separator-free old subgroup, but integer refinement
exposed a generator outside it and enlarged the subgroup to one containing a
factor-bearing element.

The current positive whole-block occurrence box still cannot contain the
canonical integer \(630=2\cdot3^2\cdot5\cdot7\). The modular representation
\(5\cdot2^{13}=40960\) exceeds \(N\). Thus subgroup expansion does not by
itself supply a legal representative.

The two histories also show that \(\sigma>0\) is neither necessary nor
sufficient for immediate success across those histories. They do not give a
same-menu ranking theorem and do not rule out using \(\sigma\) as one feature.
The missing theorem remains a public polynomial-size selector or trajectory
with an all-input inverse-polynomial law.

The final candidate, hostile re-audit, corrected proof-blind statement, and
proof-blind reconstruction have SHA-256 hashes

baa75d5935ca576dcea16bd5ebc675bbb76fad2ded26bbe3baff7c3e1a3decfe,
e342d83efe424d086d78ed6af10ba38b210028a75f6086b0716fcea64843c47b,
c55f7b1bbd691ebffac02d1863ed5df4e33b8ad85f8d90cdecc8030e6702c281,
and
e1fe9c6dc87b56aef1da9823944abad7e0c24b800a67ef945d357ddd22a30e9b.

## P79 — order-three endpoint feedback can be trapped, while quotient promotion has an exact square-class escape gate

**Status:** promoted source-specific obstruction, operation-set separation,
and exact two-gate theorem. This is not a general quotient sampler or a
factoring algorithm.

**Verification record:** the endpoint trap first passed a kill-first review
with two corrections: canonical reduction can produce the trivial state, and
retained raw powers give \(c^{3t}\), not always \(c^3\). The corrected exact
theorem then passed a fresh hostile audit and proof-blind reconstruction. The
infinite quotient-escape family and the exact prime-block square-class gate
each passed their own fresh hostile audit and proof-blind reconstruction. No
research computation, cross-family audit, human audit, or publication-level
literature review ran.

### Endpoint-only trap

Let \(c\) be an odd prime and assume

\[
N=c^2+c+1
\]

is composite with \(3\nmid N\). The seed relation is

\[
c\cdot c^2=c^3=1+(c-1)N.
\]

For every prime power dividing \(N\), the residue of \(c\) has exact order
three. Therefore

\[
H_0=\langle c\rangle=\{1,c,c^2\}\pmod N
\]

has no sign separator.

Allow arbitrary occurrence amplification of the endpoint block, optional
canonical reduction, canonical inversion, retained oversized raw powers,
integer gcd refinement, exact perfect-power extraction, all declared direct
screens, integer relation coefficients, and complete \(2\)-saturation. Every
raw relation value is \(c^{3t}\). Every rational-square relation root has
exponent divisible by three and is therefore \(1\pmod N\). No second block
appears, and the full positive decoder image is exactly \(\{1\}\).

This is not a small-factor artifact. For every \(B\ge3\), CRT, simple-root
lifting, and Dirichlet's theorem give infinitely many prime values of \(c\)
for which \(N\) has at least two distinct prime factors, every prime factor is
larger than \(B\), and two prescribed factors have valuation one. Thus \(N\)
is not a perfect power and its least prime factor can tend to infinity.

### Quotient promotion changes the source

The public seed quotient is

\[
g=c-1.
\]

It is not an endpoint block or a power of one. Promoting it to a state is an
operation change, although it adds no hidden information. Put

\[
b=\frac{c+1}{3}.
\]

Its canonical inverse and relation value are

\[
w=\frac{c^2-1}{3}=gb,
\qquad
A_1=gw=g^2b
=1+\frac{c-2}{3}N.
\]

The promoted state always passes the subgroup gate. Since

\[
1<g=c-1<c
\]

and the canonical representatives of \(H_0\) are \(1,c,c^2\), one has
\(g\notin H_0\). Complete refinement preserves products for both \(c\) and
\(g\), so the refined block-generated subgroup strictly contains \(H_0\).

The square-class gate is independent. The old and new relation classes are

\[
[A_0]=[c],
\qquad
[A_1]=[b].
\]

Because \(c\) is prime and \(\gcd(c,b)=1\), the two nonzero classes cannot
be equal. Hence

\[
\boxed{
\text{the quotient-fed column closes immediately}
\iff
\frac{c+1}{3}\text{ is an integer square}.
}
\]

Complete \(2\)-saturation adds no missed relation in the nonsquare branch. In
the square branch it adds exactly the displayed root generator and no further
\(2\)-division.

If \(b=s^2\), then \(c=3s^2-1\), \(s\) is even, and the new relation has
positive root

\[
R=s(c-1).
\]

With

\[
A=3s^2-3s+1,
\qquad
B=3s^2+3s+1,
\]

one has

\[
N=AB,
\qquad
R-1=(s-1)B,
\qquad
R+1=(s+1)A,
\]

and therefore

\[
\gcd(R-1,N)=B,
\qquad
\gcd(R+1,N)=A.
\]

The example \(c=11\) gives \(N=133=7\cdot19\) and \(R=20\).

There is also an infinite robust operation-set separation without requiring
prime \(c\). For even \(s\ge2\), put \(c=3s^2-1\). Then

\[
N=(3s^2-3s+1)(3s^2+3s+1).
\]

For every fixed \(B\ge13\), a CRT construction gives infinitely many such
\(s\) for which every prime factor of both \(c\) and \(N\) exceeds \(B\), and
one large prime has valuation one in \(c\). Thus \(c\) is a non-perfect-power
composite gcd-free block that survives the bounded prepass. Endpoint-only
feedback remains trapped, while promotion of \(c-1\) creates the exact square

\[
(c-1)\frac{c^2-1}{3}
=\bigl(s(c-1)\bigr)^2
\]

and factors \(N\). All sign, difference, and discriminant screens can be
forced to fail before this square.

The result identifies a real algorithmic distinction:

1. subgroup expansion;
2. square-class closure;
3. a non-global root.

The quotient always gives the first event on the prime-block source. It gives
the second and third only on the exact square branch. Thus manufacturing new
relations or blocks is not enough; a general sampler must manufacture
square-class cancellation and a useful root with an all-input
inverse-polynomial law.

The families are deliberately manufactured and recognizable from public
squares. The algebraic factorization is explicit. No infinitude theorem for
prime \(c=3s^2-1\), general quotient bias, all-input sampler, or unrestricted
factoring algorithm follows.

For the endpoint trap, the final candidate, hostile audit, proof-blind
statement, and reconstruction hashes are

3d769c9760f1b947d3023979cfef83d0d3a9d71ee9444eeef9169344910579a1,
623fcaa760fb89a0d691ad98ed131fcba08a9b78ebf83cad161c27a51825869f,
9422a610006d0804f7be6182cc944a93e0aef62e55f7bea1ab989eb301422ee9,
and
b8bd7e3fefcfd9448466d5b5a37eaa9e0b80e194c705bbb64383e9c98f09a0af.

For the infinite quotient escape, the corresponding hashes are

c6a02473aa6efd340bfec009d0fb9581cd164b4ce80d4b32b9969d00d53b6c10,
173d217fa5bf20cabd1c5b9c086c880e42878b13aafdc1db3e4e0975c87157d7,
ee9b0d5bb9c9d9c27acb89f7c7abedb797dbe519aa68feedeb8d3d955f7a99e1,
and
b4faf236890075b153ceb1773e8bf4b7a9bc2075f86c865bf23e4a800f2ba045.

For the exact square-class gate, the corresponding hashes are

480fa3fbe324dfcc9947ce32724904618e05933d05eb5282c9d4ce344bb8d1f5,
45fb0bdf53c54b1f67ccc05aeaa5826529d61bd4797dafbb2ca36cde10b0f688,
8a8f96f1b9ccd454ec02da906bcc7984affa32de7ca22ac2bd8d559b7060766a,
and
52c2cb450ab2692794c603fa97e4a748b2d74e23175f6bc9f1f03cfc69786466.

## P80 — quotient-collision feedback has an exact target-first fibre and a bounded-quotient boundary

**Status:** verifier-backed exact feedback theorem and method boundary. This
is not an all-input selector or a factoring algorithm.

Let

\[
A_i=x_i y_i=1+k_iN,
\qquad
P=\prod_iA_i=1+KN,
\]

be a polynomial-size indexed list of retained canonical inverse relations,
with complete gcd-free endpoint blocks, exact exponents, and occurrence
capacities. For a target quotient \(r\ge1\), put

\[
A_r=1+rN,
\qquad
D_r=\gcd(P,A_r).
\]

Then the complete supported target fibre collapses to quotient differences:

\[
\boxed{
D_r
=\gcd(P,K-r)
=\gcd\!\left(A_r,\prod_i(k_i-r)\right).
}
\]

If \(r\ne k_i\) for every \(i\), then

\[
v_p(D_r)
=\min\!\left(v_p(A_r),\sum_i v_p(k_i-r)\right).
\]

Thus every prime in \(D_r\) is supported by an old quotient difference, and
repeated relation occurrences can increase its valuation even when they add
no decoder rank.

For any occurrence-certified divisor \(1<g<N\) of \(P\), let

\[
g\iota_N(g)=1+k(g)N.
\]

The exact fibre condition is

\[
\boxed{
k(g)=r
\iff
g\mid D_r\text{ and }r<g<N.
}
\]

If \(N>r^2\), a legal target-\(r\) candidate exists after gcd-free
refinement by \(D_r\) exactly when \(D_r>r\). Refine \(D_r\) into retained
block occurrences. If one occurrence exceeds \(r\), use it. Otherwise
multiply occurrences until the product first exceeds \(r\); the result is at
most \(r^2<N\). For polynomially bounded \(r\), the branch \(N\le r^2\) is
resolved by polynomial trial division.

This is the exact dual of the proposed CRT state. For

\[
\rho_N(g)=(-N^{-1})\bmod g,
\]

one has \(\rho_N(g)=k(g)\). A CRT product search chooses \(g\) and computes
its label \(r\); the quotient-collision scan chooses \(r\) and computes the
largest supported divisor \(D_r\). One gcd per declared \(r\) therefore
replaces subset enumeration inside that fibre. The aggregate \(D_r\) can
exceed \(N\) and need not itself be legal or factor-bearing.

There is an exact domination boundary. If

\[
1\le r,k_i\le B=operatorname{poly}(\log N),
\qquad r\ne k_i,
\]

then every prime of \(D_r\) is at most \(B\). When \(D_r>r\), trial
factorization of the small differences constructs

\[
r<g\le rB\le B^2.
\]

Either trial division resolves \(N\), or a prior state scan through \(B^2\)
already emits \(A_r\). With the unchanged product and endpoint ledger it then
recovers the same \(D_r\), refinement, and occurrence provenance. Hence the
sieve has genuinely different source power only in a regime with large old
quotient differences.

Two implementation corrections are essential. First,

\[
\gcd(g-\iota_N(g),N)=\gcd(g^2-1,N)
\]

does not replace the two sign screens: it equals \(N\) on a non-global
involution. Second, an HNF/SNF decoder basis cannot replace the source
occurrence ledger. At \(N=4033,r=3\), one quotient-one occurrence gives
\(D_3=2\), while two identical occurrences give \(D_3=4\) and authorize
\(g=4\).

The gate contains all central P70/P78 witnesses. For example, at \(N=4033\)
with old quotients \(1,63,7\), target \(r=1983\) gives

\[
D_r=10240=2^{11}\cdot5.
\]

It certifies \(g=2048\), complement \(3905\), and the block split
\(\gcd(10240,1985)=5\). In the repeated power family

\[
N=(2^{2t}-1)/3,
\]

\(t\) quotient-one occurrences and target \(r=3\) give \(D_3=2^t\).

The theorem supplies no law that puts a successful \(r\) in a polynomial
range, makes the generic fibre member useful, or creates large correlated
quotients from bare \(N\).

The corrected candidate, passing proof-only re-audit, proof-blind statement,
and proof-blind reconstruction have SHA-256 hashes
`de21b1e693275cb14e05931d71a6ad6f8d30bb40dc85e3ab68ad30a7c83c78e6`,
`99e25f64ade770f0fd9f6367e2a4f9e546ce3d78b642c21a05bed2547d0db51e`,
`af82219350f7c27f79c25eb93a4d708f94a11ca8f32464f31fe62b743e2bc6e8`,
and
`8d30ce452d0712f41f2527f8245ea66b515b94f0535d9d6c2016bba435a91bbf`.
The failed first candidate and hostile audit remain preserved at hashes
`6cdb5cea5121d07972c2f84211d6cfd26d0a30088769355806b86eec0c26a217`
and
`61e5e85c08c523849ecce6feb36a516186147290802db863bf873dc753e14ba1`.
No authoritative research computation, cross-family audit, human audit, or
publication-level literature review supports this theorem.

## P81 — canonical-residue closure is a real source change and completes the fixed P78 chain

**Status:** verifier-backed operation-change theorem and fixed witness. This
is not an all-input word selector or a factoring algorithm.

For a unit \(1<g<N\), the CRT state

\[
\rho_g=(-N^{-1})\bmod g,
\qquad
w_g=\frac{1+N\rho_g}{g}
\]

is exactly the canonical inverse relation. If a coprime block \(b\) is added,

\[
t=(\rho_b-\rho_g)g^{-1}\bmod b,
\]

then

\[
\rho_{gb}=\rho_g+gt,
\qquad
w_{gb}=\frac{w_g+Nt}{b}=[w_gw_b]_N.
\]

This is exact bookkeeping for a coprime extension. It does not cover another
copy of an existing block, an overlapping macroblock, or missing occurrence
provenance.

The proposed beam scores do not have scalar extension monotonicity. Exact
\(N=55\) examples reverse the ordering of canonical-inverse size, quotient
size, and inverse distance after one common coprime extension. Old-block gcd
gain can also appear or disappear after extension. These examples prove only
that the current scalar values are not exact dominance certificates. They do
not prove that any polynomial-width beam fails, or even exhibit a failed run
after all mandatory screens.

The genuine operation change is canonical-residue closure. For current
blocks generating

\[
H=\langle q_1,\ldots,q_m\rangle,
\]

take a public exponent vector and compute

\[
c=\left[\prod_jq_j^{e_j}\right]_N,
\qquad
w=[c^{-1}]_N.
\]

Both residues remain in \(H\), so this does not enlarge the residue subgroup.
But it removes the positive-product and finite-occurrence-box restriction.
Gcd-free refinement of the new canonical integers can expose individual
integer factors whose residue classes lie outside \(H\). This is the
representation-level gain from P78 in an executable source operation.

On P78's refined state

\[
N=4033=37\cdot109,
\qquad H_1=\langle2,5\rangle,
\]

the known oversized word becomes

\[
5\cdot2^{13}\bmod N=630,
\qquad
630\cdot3220=1+503N,
\]

and

\[
\gcd(630-1,N)=\gcd(630-3220,N)=37.
\]

More strongly, the literal small exponent menu already contains the
support-two certificate

\[
5^2 2^8\bmod N=2367,
\qquad
2367\cdot443=1+260N,
\]

with

\[
\gcd(2367+1,N)=\gcd(2367-443,N)=37.
\]

Thus a polynomial exhaustive support-two scan closes P78's finite-box caveat
on this fixed post-refinement state. The earlier feedback step is now part of
a complete explicit multi-step chain: a separator-free old subgroup is
refined to expose \(5\), then a canonical residue of the new subgroup factors
\(N\).

No theorem explains how every input reaches such a state, why every useful
subgroup has a separator in a polynomial exponent menu, or why a capped beam
or random word finds one with inverse-polynomial probability.

The corrected candidate, proof-only re-audit, proof-blind statement, and
proof-blind reconstruction have SHA-256 hashes
`9e3333f490c62c68c1aab66f920394e13e4ce51974bbde543be312a5cc30309a`,
`a8319eae8acb4d7c0c3f8181afbc35950be622706094c74cbecfb068f0783c28`,
`331d9571034b8894d92ca9e1cb5834e65243dc7b8ca2ffefc3e75cfc681ed3e4`,
and
`2204a2fd2853938307ed01c71cdfb1cef850042e19f7d19364cbd96bc3a889ee`.
The first audit of the earlier scope wording is preserved at hash
`d26b343a84125ea3d056012ec6e88d2a21e3e2c74a599e4769dfb4059883dd01`;
its transient unregistered arithmetic is non-authoritative. No research
computation supports the promoted proof, and no cross-family, human, or
publication-level literature audit has run.

## P82 — uniform inverse seeds almost never add a hard large prime to a polynomial quotient scan

**Status:** verifier-backed independent-source obstruction. This does not
cover adaptive correlated feedback and is not a factoring lower bound.

Let \(n=\lceil\log_2(N+1)\rceil\). Stop on primes, and trial-divide the
remaining composite \(N\) through \(B\ge\max(3,n)\). If this does not factor
\(N\), every prime divisor of \(N\) exceeds \(B\).

Let \(U_i\) be uniform unit representatives, let

\[
V_i=\iota_N(U_i),
\qquad
A_i=U_iV_i,
\qquad
P=\prod_{i=1}^mA_i,
\]

and for \(1\le r\le R\) put

\[
C_r=1+rN,
\qquad
D_r=\gcd(P,C_r).
\]

Independence is unnecessary; uniform marginals suffice. With

\[
L=n+\lceil\log_2(R+1)\rceil+1,
\]

one has

\[
\Pr\!\left(
\exists r\le R,\ \exists\text{ prime }\ell>B:\ell\mid D_r
\right)
\le
\frac{2mRNL}{B\varphi(N)}.
\]

Indeed, for fixed \(i,r\) and \(\ell\mid C_r\), primality implies that
\(\ell\mid A_i\) only if it divides \(U_i\) or \(V_i\). Each event has
probability at most \(N/(\ell\varphi(N))\), because inversion permutes the
units. Union over the at most \(L\) prime divisors of \(C_r\), then over all
\(mR\) pairs.

The small-factor prepass also gives

\[
\frac N{\varphi(N)}
\le
\exp\!\left(
\frac{n}{B\log_2(B+1)}
\right)
\le e.
\]

Therefore the probability is at most \(2e mRL/B\). For fixed
\(m\le n^a\), \(R\le n^b\), and any \(c\ge1\), take

\[
B=n^{a+b+c+3}.
\]

Trial division remains polynomial and the large-common-prime probability is
\(O(n^{-c-1})\). This bound already unions over every numerical
\(r\le R\), so it also covers an adaptive final choice of \(r\) inside that
range.

On the complementary event, every \(D_r\) is \(B\)-smooth. Polynomial trial
division completely factors it, exposes the full \(B\)-smooth part of every
\(C_r\), and can strip the same public small primes from every retained
endpoint block. The remaining difficulty can still be a hard selection among
many known small factors; the theorem does not claim \(D_r\le r\) or that a
smooth fibre is useless.

Thus fresh uniform inverse samples do not supply the hard large overlap needed
to make P80 new. The live route must use adaptive canonical-residue or block
feedback whose marginals are factor-correlated or otherwise nonuniform.

The corrected candidate, passing proof-only re-audit, proof-blind statement,
and proof-blind reconstruction have SHA-256 hashes
`87a5706f674dfd507acaf1777ff69217c0a6040483c6651b41351c8a1bc84aac`,
`a08ac57657391577da054b288ddcb45aaf2a7c412cd9d6e81cbd3a7ff9d0d92a`,
`cc94c7ce5b923dec32d0e7526f8301b9b898ca914d6a02f59694677d7991826f`,
and
`9f0170089584861602ee959a4778945c71f483779f3bc84c911032651ee64724`.
The failed first candidate and audit remain preserved at hashes
`c7d24e5e57effd5242006d06c4b9b45c746398ecd6b6514dcaf6dcd7936669bd`
and
`68b710bdc9988d39f1d0ef63beeed38f50c397bdd7cab09f30c0841e08512e08`.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P83 — a public generated subgroup has an easy near-uniform sampler; separator density is the exact gate

**Status:** promoted from F77 after a proof-only hostile audit and a
proof-blind reconstruction. This is a conditional theorem, not a factoring
algorithm.

Let

\[
H=\langle q_1,\ldots,q_s\rangle
\le (\mathbb Z/N\mathbb Z)^\times,
\qquad n=\lceil\log_2N\rceil.
\]

The factorization of \(N\), the generator orders, and \(|H|\) need not be
known. Put

\[
L=3n+\lceil\log_2(s+1)\rceil,
\qquad M=2^L.
\]

Choose independent uniform exponents
\(E_j\in\{0,\ldots,M-1\}\) and output

\[
X=\left[\prod_{j=1}^s q_j^{E_j}\right]_N.
\]

Then the law of \(X\) has total-variation distance less than \(2^{-2n}\)
from uniform on \(H\). The sampler uses \(O(s(n+\log s))\) random bits and
polynomial bit complexity. The proof reduces each exponent modulo the
unknown order of its generator: a long uniform interval is already close to
uniform modulo every order below \(N\), and a surjective homomorphism sends
uniform exponent tuples to uniform subgroup elements.

For \(N=pq\), with distinct odd primes, let \(H_p,H_q\) be the two local
projection images. For uniform \(X\in H\), the exact positive-sign success
density is

\[
\delta_+
=\Pr(1<\gcd(X-1,N)<N)
=\frac1{|H_p|}+\frac1{|H_q|}-\frac2{|H|}.
\]

If \(\epsilon_p,\epsilon_q,\epsilon\) record whether \(-1\) lies in
\(H_p,H_q,H\), respectively, then

\[
\delta_-
=\Pr(1<\gcd(X+1,N)<N)
=\frac{\epsilon_p}{|H_p|}
 +\frac{\epsilon_q}{|H_q|}
 -\frac{2\epsilon}{|H|}.
\]

If either density is inverse polynomial in \(n\), repeated public subgroup
sampling and the two sign gcd tests give a classical Las Vegas polynomial-time
factorer for that state. The negligible sampler error is smaller than every
nonzero event mass for the finitely many small inputs, so the statement has
no hidden asymptotic exception.

Subgroup expansion alone does not give this density. In the abstract group
\(C_L\times C_L\), the subgroup
\(\langle(a,a),(1,-1)\rangle\) contains a separator, but its positive-sign
density is only \(1/L\). This is a density example, not an asserted integer
family.

Thus a heuristic dense-exponent beam is unnecessary. The missing all-input
theorem must instead prove inverse-polynomial factor-bearing density after
feedback, find a separator with a polynomial sparse-word menu, or prove that
further integer refinement reaches a subgroup with one of those properties.

The candidate, passing proof-only audit, proof-blind statement, and
proof-blind reconstruction have SHA-256 hashes
`7fd5bbec5485da405ecd71869f8caee2a7daa950e7eca1815f9f7de6b943449d`,
`2de45c5b2af5f427d1884a5479a8601e04857c441535d86279b4854fabec3896`,
`d07645a53bc3348d46a2addea066dae150f15ab285aa37dd8c12d40bf857882b`,
and
`c49d9e787f81e0129802ade3b9bab2de04cc3e13fb84fa2a4c5e32c53dde4f33`.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P84 — feedback expansion has an exact projection-kernel gate and a permanent old-subgroup density ceiling

**Status:** verifier-backed exact feedback boundary after a hostile proof-only
audit and a proof-blind reconstruction. This is not a factoring algorithm, a
hardness theorem, or a theorem about the square-class decoder.

Let \(N=pq\) for distinct odd primes. Let an old block-generated subgroup
\(H\le(\mathbb Z/N\mathbb Z)^\times\) contain no positive separator, and put
\(h=|H|\). Both hidden projections of \(H\) are injective, since a
nonidentity projection-kernel element would itself be a positive separator.
Hence

\[
|H|=|H_p|=|H_q|=h,
\]

and \(H\) is the graph of an isomorphism between its local images.

For any later subgroup \(K\ge H\), define

\[
c=[K:H],
\qquad
a=[K_p:H_p],
\qquad
b=[K_q:H_q].
\]

The induced quotient projections are surjective, so \(a\mid c\) and
\(b\mid c\). Their unquotiented kernels have sizes \(c/a\) and \(c/b\) and
intersect only in the identity. Therefore the exact positive-separator count
and uniform density in \(K\) are

\[
\boxed{\frac ca+\frac cb-2},
\qquad
\boxed{\delta_+(K)=\frac{c/a+c/b-2}{ch}}.
\]

A factor-bearing positive word exists exactly when

\[
\boxed{c>a\quad\text{or}\quad c>b.}
\]

Raw subgroup growth \(c>1\) is not sufficient.

One exact old unit-block split \(B=uv\), with \(B\bmod N\in H\), is the
cyclic case:

\[
\langle H,u,v\rangle=\langle H,u\rangle.
\]

Here \(c,a,b\) are the global and two local orders of the coset of \(u\).
Every enlarged-subgroup element has a unique form \(u^tz\), with
\(0\le t<c\) and \(z\in H\). The \(p\)-kernel exponents are exactly the
multiples of \(a\), and the \(q\)-kernel exponents are exactly the multiples
of \(b\). Each such exponent has one unique old-subgroup cancellation
element. This characterizes the missing word but does not compute it.

The stronger boundary is coset-level. Every \(H\)-coset contains at most
four elements that can pass either direct sign gcd. Thus every mixture of
uniform \(H\)-coset laws has total direct-sign success probability at most

\[
\boxed{\frac4h}.
\]

Uniform sampling from every \(K\ge H\) is such a law, with separate bounds

\[
\delta_+(K)\le\frac2h,
\qquad
\delta_-(K)\le\frac2h.
\]

The ceiling does not depend on \([K:H]\). If \(h\) is exponential in the
input bit length, even maximal subgroup expansion leaves dense
random-exponent direct-sign sampling exponentially sparse.

The exact adaptive form also holds. If trial \(t\), conditional on every
prior history, is within deterministic total-variation error
\(\varepsilon_t\) of an \(H\)-invariant law, then

\[
\Pr(\text{some direct-sign success in \(T\) trials})
\le
\frac{4T}{h}+\sum_{t=1}^T\varepsilon_t.
\]

If \(X\) is uniform on \(H\) and independent of arbitrary group-valued
\(Y\), each fixed law \(X^{\pm1}Y^{\pm1}\) is \(H\)-invariant. This covers
fixed or predictable pair lists and all distinct pairs in a polynomial
independent pool. It does not cover value-dependent pair selection.

The ceiling is sharp at group scale. For \(L>2\), the diagonal subgroup of
\(C_L\times C_L\) has size \(L\) and no positive separator. Adjoining
\(z=(u,v)\), where \(u,v\ne0\) and \(v-u\) generates \(C_L\), gives the full
product although \(z\) is not a separator, and

\[
\delta_+=\frac{2L-2}{L^2}.
\]

This is an abstract example, not a canonical-inverse integer family.

The result removes “expand the subgroup, then sample it densely” as the
missing theorem in the large synchronized regime. It leaves precisely the
non-\(H\)-invariant branches: a public targeted cancellation word, direct
integer overlap, quotient-fibre targeting, or square-class closure followed
by a non-global root. It does not bound any of these operations.

The final candidate, hostile audit, proof-blind statement, and corrected
proof-blind reconstruction have SHA-256 hashes
b9f77023c1b63ee392d72167f2902b771bd33237e7e23ed01f31b739649a7f24,
9656ce11a6857e52644d1242cd1a12c69284e9e36f245ca49add94f78de9152f,
ea87352c021194438aa42793c975bf75a5043b8964c00c98a96636ea1707239d,
and
ce8d175c46d2c5a5bf09258ddab026bf404c32139af6d012ccfe317696a38b67.
The audit pinned pre-clarification mathematical hash
73bbd8d875a3c91acb3332bcab765acee3784491c322784c0c6a526ea131427b;
the final edits only state its scope corrections explicitly and remove one
trailing space. No research
computation, cross-family audit, human audit, or publication-level literature
review has run.

## P85 — every fixed sublinear word menu can miss a maximal one-generator correlation break

**Status:** promoted from F79 after a proof-only hostile audit and a
proof-blind reconstruction. This is an abstract group-level boundary, not an
integer hard family, a computational lower bound, or a factoring algorithm.

Let \(L>2\) be prime, write \(C_L\) additively as \(\mathbb F_L\), and fix any
menu

\[
S\subseteq\mathbb F_L^2,
\qquad |S|\le L-3,
\]

before choosing a new generator. A pair \((A,B)\in S\) denotes the word
\(Az+Bg\). There are distinct nonzero \(r,s\in\mathbb F_L\) such that, with

\[
g=(1,1),\qquad H=\langle g\rangle,
\qquad z=(r,s),
\]

the old subgroup \(H\) has no positive separator, \(z\) is not itself a
separator, and

\[
\langle H,z\rangle=\mathbb F_L^2,
\]

yet no word in the declared menu is a separator.

For each pair with \(A\ne0\), the word

\[
Az+Bg=(Ar+B,As+B)
\]

can have a zero coordinate only when \(r\) or \(s\) equals the one forbidden
ratio \(-B/A\). There are at most \(L-3\) such values. Their complement
contains two distinct nonzero choices for \(r,s\). The determinant \(s-r\)
is nonzero, so \(g,z\) generate the full product even though the complete
menu misses every positive separator. The cardinality guarantee is sharp:
there is a menu of size \(L-2\) that hits every admissible pair of distinct
nonzero \(r,s\).

Consequently, every predeclared menu of \(T(n)\) exponent pairs is avoidable
in this model when \(L>T(n)+2\). The complete integer box

\[
|A|,|B|\le E(n)
\]

is avoidable when

\[
L>(2E(n)+1)^2+2,
\]

after reducing its pairs modulo \(L\). The same statement applies to a fixed
union of schedules only when its total number of distinct residue pairs fits
the bound.

The quantifier order is essential:

\[
\text{menu first}\quad\longrightarrow\quad\text{generator second}.
\]

After seeing \(z=(r,s)\), the adaptive word \(z-rg=(0,s-r)\) succeeds.
Therefore P85 does not cover a value-dependent or adaptive selector,
quotient-fibre processing, integer refinement, square-class decoding, or a
canonical-inverse integer realization. In an odd-order local realization,
local \(-1\) lies outside the modeled subgroup, so the negative sign adds no
target inside this model.

Thus maximal subgroup expansion does not justify a fixed polynomial word
catalogue. A live feedback algorithm must use numerical or refinement data
observed after the new integer block appears.

The candidate, hostile audit, proof-blind statement, and corrected
proof-blind reconstruction have SHA-256 hashes
`1182b0088dcf105324c929d622dc0c63952dbbf00951659ca27e725a3784566e`,
`9835898bde0a460abaf2bec0f296339383ff87bce11e90ed6e615ca3cabb401b`,
`ccb4db80e17d96ecf1f19681170f0981eb559461ef5dc1a86bbc3fc7b2738212`,
and
`d8d0a27467a1ae6045fd15f7cf39530d3fe86e04bc50b0e1ea972dabe39ba599`.
The reconstruction's only post-proof edit restored TeX formatting; it did
not change any mathematical claim. No research computation, cross-family
audit, human audit, or publication-level literature review has run.

## P86 — power contraction escapes the old-coset ceiling and completes a second fixed feedback chain

**Status:** promoted from F80 after a proof-only hostile audit and a corrected
proof-blind reconstruction. This is an exact conditional mechanism and fixed
witness, not an all-input smoothness theorem or a factoring algorithm.

Let \(K\) be a finite subgroup of
\((\mathbb Z/N\mathbb Z)^\times\), let \(M\ge1\), and put

\[
K^M=\{x^M:x\in K\}.
\]

The power map is a surjective homomorphism from \(K\) to \(K^M\). All fibres
have equal size, so uniform \(X\in K\) gives uniform \(X^M\in K^M\). For
\(N=pq\), projection commutes with powering, and the exact positive-sign
density is

\[
\delta_+(K^M)
=
\frac1{|K_p^M|}
+\frac1{|K_q^M|}
-\frac2{|K^M|}.
\]

This operation can leave P84's hypothesis: \(K^M\) need not contain the old
subgroup \(H\), so the powered law need not be \(H\)-invariant.

For one public unit \(u\), let

\[
r_p=\operatorname{ord}_p(u),
\qquad
r_q=\operatorname{ord}_q(u).
\]

Then

\[
\boxed{
1<\gcd(u^M-1,N)<N
\iff
(r_p\mid M)\mathbin{\mathrm{xor}}(r_q\mid M).
}
\]

For

\[
M_B=\operatorname{lcm}(1,\ldots,B),
\]

the bound \(M_B\le B!\) gives
\(\log_2M_B=O(B\log B)\). If \(B\) is polynomial in the bit length of
\(N\), constructing \(M_B\), computing the modular power, and taking the
gcd all have deterministic polynomial bit complexity.

The P78 history gives a complete fixed witness at

\[
N=4033=37\cdot109.
\]

Before feedback, \(H_0=\langle2\rangle\), and \(2\) has exact order \(36\)
in both hidden fields. The canonical feedback relation with

\[
g=2^{11}=2048,
\qquad
g^{-1}_{\mathrm{can}}=3905
\]

splits the old integer block \(1985\) through

\[
\gcd(1985,3905)=5.
\]

Thus refinement exposes the public descendant block \(u=5\). With

\[
M=M_9=2520,
\]

one has

\[
5^M\equiv1\pmod{37},
\qquad
5^M\equiv63\pmod{109},
\qquad
5^M\equiv3442\pmod{4033}.
\]

The public final operation therefore returns

\[
\boxed{\gcd(5^{2520}-1,4033)=37.}
\]

Every old \(h\in H_0\) instead has \(h^{2520}=1\) globally. The new block is
therefore essential relative to this declared old-subgroup, fixed-exponent
channel. It is not necessary against all public algorithms: \(5\) is also a
small ordinary Pollard-style base that could be tried without feedback.

The theorem proves that power contraction is a real post-feedback operation,
distinct from uniform supergroup sampling and from P81's mixed cancellation
word. It gives no law that feedback produces a block with a one-sided
polynomial-smooth local order on every input.

The candidate, hostile audit, corrected proof-blind statement, and corrected
proof-blind reconstruction have SHA-256 hashes
e5b205098b837a37616df563b82cd3f65dc953129bdb213797d97e122af771bf,
af40985d221049090ea7fa14ffb23841aa3536b52e64927b813d69799fb47067,
3235f8bab26c75804ae1d9dbda3ed3563e88884a40cce9161b2e99beac017a5b,
and
b67b34e8cae0883ad8063f7adfeda1b35123b7cfbbe0c974138d56ee284177e7.
The first proof-blind statement accidentally omitted the plus sign between
the two reciprocal projection terms. It correctly failed reconstruction;
those two hashes are
93df9398feeb558bdfdccfef0ec501a626bd1a624fceaf0deccda7388d2b0080
and
51ce2322c3ec0d00cd771d1a61fe47155a2198b53bf876f1eb7becb1a29ab353.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P87 — feedback subgroup gain has an exact order branch and a phase branch

**Status:** promoted from F81 after a corrected proof-only hostile audit and
a proof-blind reconstruction. This is an exact one-block classification and
a conditional polynomial decoder, not an all-input feedback law or a
factoring algorithm.

Let \(N=pq\) for distinct odd primes, let
\(u\in(\mathbb Z/N\mathbb Z)^\times\), and put

\[
r_p=\operatorname{ord}_p(u),
\qquad
r_q=\operatorname{ord}_q(u),
\qquad
r=\operatorname{lcm}(r_p,r_q).
\]

Then \(\langle u\rangle\) contains a positive direct-sign separator if and
only if

\[
\boxed{r_p\ne r_q}.
\]

Its exact positive-separator count and uniform density are

\[
\boxed{\frac r{r_p}+\frac r{r_q}-2},
\qquad
\boxed{\frac1{r_p}+\frac1{r_q}-\frac2r}.
\]

For every public exponent \(E\ge1\),

\[
\boxed{
1<\gcd(u^E-1,N)<N
\iff
(r_p\mid E)\mathbin{\mathrm{xor}}(r_q\mid E).
}
\]

If \(r_p=r_q\), the two local negative-sign conditions also synchronize.
Thus no pure power can factor through either direct sign.

For a positive integer \(a\), define its largest full prime-power divisor by

\[
\sigma(a)=\max_{\ell^e\mid a}\ell^e,
\qquad
\sigma(1)=1.
\]

Let

\[
M_B=\operatorname{lcm}(1,\ldots,B)
\]

and define the punctured-lcm bank

\[
\mathcal E_B
=
\{M_B\}
\cup
\left\{
\frac{M_B}{\ell^j}:
\ell\le B\text{ prime},\
1\le j\le\lfloor\log_\ell B\rfloor
\right\}.
\]

This bank is complete for the bounded part of the order branch:

\[
\boxed{
\exists E\in\mathcal E_B:\ 1<\gcd(u^E-1,N)<N
\iff
r_p\ne r_q
\text{ and }
\min\{\sigma(r_p),\sigma(r_q)\}\le B.
}
\]

The bank has at most \(B+1\) exponents. For
\(B=\operatorname{poly}(\log N)\), its construction and all modular-power
and gcd tests have deterministic polynomial bit complexity. The condition
\(\sigma(r)\le B\) is stronger than ordinary \(B\)-smoothness: it bounds
each complete prime-power component, not only the prime divisors.

At \(N=4033=37\cdot109\), the feedback descendant \(u=5\) has

\[
\operatorname{ord}_{37}(5)=36,
\qquad
\operatorname{ord}_{109}(5)=27,
\]

with \(\sigma(36)=9\) and \(\sigma(27)=27\). The member
\(M_9=2520\) therefore separates the two local orders, as in P86.

There is also a genuinely different phase branch. For prime \(L>2\), work
additively in \(\mathbb F_L^2\) and put

\[
g=(1,1),
\qquad
H=\langle g\rangle,
\qquad
z=(a,b),
\]

where \(a,b\) are distinct and nonzero. Both coordinates of \(z\) have
order \(L\), so no scalar multiple of \(z\) is a separator. Nevertheless,

\[
\langle H,z\rangle=\mathbb F_L^2,
\qquad
z-ag=(0,b-a)
\]

is a separator. Hence maximal subgroup gain need not create an order
mismatch. A post-feedback algorithm must retain both operations: a
punctured power bank for the order branch, and an adaptive mixed-cancellation
or further-refinement rule for the phase branch.

No public branch detector, all-input source law, canonical-integer hard
family, computational lower bound, or factoring algorithm is proved.

The corrected candidate, corrected hostile audit, proof-blind statement,
and proof-blind reconstruction have SHA-256 hashes
1aea866b07229545b14c7dbb34955e6d092adce65ccf8d47b93c2ecbf93dc94e,
1972cb59af7640eab0a9c1817279db464659cf02071673978975f40a3185aec2,
67359dc153a68ec0536aa7cfce9a91a8ee151ad55141293d05c9ea414c690ec5,
and
2469fbeade02d8440f0e8fed4273b3d578602e2adbaec1d3e11781febbba1e54.
The first candidate and first hostile audit have hashes
4fa0278a3299fe49fc2e60062c562c2ed7c327a0e03cdeb7b44208cfbf64701e
and
059697ec65cb4203f85b5c89473a7d88e4f1e790ea25c997bbf4a307ef893b50.
The first audit correctly rejected the use of standard smoothness
terminology. No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P88 — canonical integer feedback has a literal phase-only expansion

**Status:** promoted from F82 after a hostile whole-proof and provenance
audit and a proof-blind reconstruction. This is a fixed mechanism witness,
not an all-input selector or a factoring algorithm.

Let

\[
N=2047=23\cdot89.
\]

The public canonical relations

\[
11\cdot1861=1+10N,
\qquad
312\cdot269=1+41N
\]

have four pairwise-coprime endpoints, none of which is a nontrivial integer
perfect power. Their residues generate exactly

\[
H_0=\langle11\rangle.
\]

The element 11 has exact order 22 in both hidden fields. Its \(+1\) and
\(-1\) states are therefore synchronized, so no direct sign gcd from
\(H_0\) is proper.

Now take the canonical-residue feedback word

\[
g=[11^7]_N=1778,
\qquad
w=1735,
\]

for which

\[
1778\cdot1735=1+1507N.
\]

Both residues already lie in \(H_0\). The relation adds no new modular
subgroup element, and all immediate endpoint sign and difference tests are
trivial. Neither feedback endpoint is an integer perfect power. However,

\[
\boxed{\gcd(312,1778)=2.}
\]

Joint integer refinement therefore exposes the public block 2. This block
does not lie in \(H_0\), so the available block-generated subgroup strictly
expands even though the selected residue was redundant.

The new block is phase-only:

\[
2^{11}=2048=1+N
\]

and 2 has exact order 11 in both hidden fields. Hence, for every \(e\ge0\),

\[
\gcd(2^e-1,N)\in\{1,N\},
\qquad
\gcd(2^e+1,N)=1.
\]

No pure power of the newly exposed block can factor \(N\). The mixed public
word does:

\[
2\cdot11=22,
\qquad
\boxed{\gcd(22+1,2047)=23.}
\]

Thus a post-split policy that discards the old generators and tests only
pure powers of the new block is incomplete. This does not rule out powering
arbitrary mixed elements of the expanded subgroup or any unrelated
factoring method. The block 2 is visible by trial division of the old
endpoint 312 and is an ordinary small public base, so feedback is not
necessary for this fixed integer under stronger preprocessing. No frequency,
hard-family, branch-detector, all-input selector, or factoring theorem
follows.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
85f9b310a0e1a10af3cdae8c081b1f374e3be3bddf2437c2d40c39b16ec45990,
fdb0f290efba7ff188a50fe1dc93d93b4df99cc51e0783675ac49c5f293720df,
dee4543c9f3eed076446c789c64dd2055fb0e9612302d44473c948a5cac0426c,
and
9e8027e15a2702f925af91513bb74e56feed61ed26ffe587b4071de59b3588f1.
The finite search is authenticated discovery evidence, not an independent
replay or asymptotic result. No cross-family audit, human audit, or
publication-level literature review has run.

## P89 — prime saturation has a complete deterministic support-two decoder

**Status:** promoted from F83 after a hostile proof-only audit and a
proof-blind reconstruction. This is a conditional factor-free decoder for
an explicit relation list, not a relation source or a factoring algorithm.

Let \(N=pq\) for distinct odd primes. Let \(q_1,\ldots,q_s\) be
pairwise-coprime positive unit blocks, and let

\[
A_i=\prod_{j=1}^s q_j^{e_{ji}}\equiv1\pmod N,
\qquad
1\le i\le m,
\]

be explicit relations with exponent matrix \(E\). For a public prime
\(\ell\), put

\[
V=\ker(E\bmod\ell).
\]

For canonical coordinate representatives of \(c\in V\), define

\[
\widetilde R(c)
=
\prod_jq_j^{(\sum_i e_{ji}c_i)/\ell},
\qquad
R(c)=[\widetilde R(c)]_N.
\]

The exponents are integers, \(R(c)^\ell=1\pmod N\), and

\[
\rho:c\longmapsto(R(c)\bmod p,R(c)\bmod q)
\]

is a homomorphism. Let

\[
K_r=\{c\in V:R(c)=1\pmod r\},
\qquad r\in\{p,q\}.
\]

Each local kernel is either all of \(V\) or a hyperplane, including when
\(\ell\) equals one hidden characteristic. The exact decoder gate is

\[
\boxed{
1<\gcd(R(c)-1,N)<N
\iff
c\in K_p\mathbin\triangle K_q.
}
\]

If the two local map ranks are \(d_p,d_q\in\{0,1\}\) and their joint rank
is \(d\), uniform \(c\in V\) succeeds with exact probability

\[
\boxed{
\ell^{-d_p}+\ell^{-d_q}-2\ell^{-d}.
}
\]

When \(K_p\ne K_q\), this is either
\(1-1/\ell\) or \(2(\ell-1)/\ell^2\).

For any public basis \(b_1,\ldots,b_D\) of \(V\), define

\[
\mathcal C
=
\{b_i\}
\cup
\{b_i+t b_j:i<j,\ t\in\mathbb F_\ell^\times\}.
\]

This support-two menu is complete:

\[
\boxed{
K_p\ne K_q
\iff
\exists c\in\mathcal C:
1<\gcd(R(c)-1,N)<N.
}
\]

Its exact size is

\[
D+(\ell-1)\binom D2.
\]

The proof covers zero and proportional local functionals and dimensions
zero and one. For \(\ell=2\), basis vectors alone are complete. If the
explicit relation presentation has bit length \(L\) and the numerical value
of \(\ell\) is polynomial in \(L+\log N\), all linear algebra, modular-root
construction, and gcd tests have deterministic polynomial total bit
complexity. The executable decoder uses no hidden factor, order, or local
character.

A fixed operation-separation certificate is

\[
N=215=5\cdot43,
\qquad
8\cdot27=216=1+N.
\]

On blocks 2 and 3 the exponent column is \((3,3)^T\). Its binary kernel is
zero, but modulo 3 the column is zero and the exact cube root is 6. Thus

\[
\boxed{\gcd(6-1,215)=5.}
\]

This witness does not separate odd-prime saturation from every endpoint
screen, because

\[
\gcd(8+27,215)=5.
\]

The theorem changes the decoder: 2-saturation is only one prime case, and
odd-prime kernels require support-two combinations. It gives no public law
that manufactures \(K_p\ne K_q\), selects a useful prime on every input, or
produces an all-input factoring algorithm. Proportional nonzero local
characters have equal identity kernels and remain outside this decoder.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
9fef7c952aa61895552374f6f64e360f09c25d4ec12b2fa8937727f8f0fd4163,
6558ed289102a3b3e7927d4b9579572902321f9343c0c5e7efea2e2a9b03c9d4,
7868d3f7c31a558bed9d0e2afd129a593658285de07aefff1208e40e0ddc64b4,
and
55f204f4cce33814238c670c446273040f91dadbb06da8f19275dec7135a5103.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P90 — exhaustive direct-sign failure is exactly a diagonal graph state

**Status:** promoted from F84 after a hostile proof-only audit and a
proof-blind reconstruction. This is a state characterization and an exact
feedback-transition theorem, not a public state recognizer, selector, or
factoring algorithm.

Let \(N=pq\) for distinct odd primes and let

\[
H\le(\mathbb Z/N\mathbb Z)^\times
\cong\mathbb F_p^\times\times\mathbb F_q^\times.
\]

The following conditions are equivalent:

1. every \(x\in H\) has
   \(\gcd(x-1,N)\in\{1,N\}\);
2. both hidden projections of \(H\) are isomorphisms onto their images;
3. \(H\) is the graph of an isomorphism
   \(H_p\to H_q\); and
4. every \(x\in H\) has equal local orders modulo \(p\) and \(q\).

In this state, negative signs synchronize as well. Every identity-target
prime-saturation root map has equal local kernels, for every prime, so all
such decoders fail automatically. The quantifier over the full subgroup is
essential: failure of a finite direct menu and all currently available
saturation tests does not certify a graph state. For example,
\(N=35\), \(H=\langle2\rangle\) passes the two direct tests on the listed
generator and has no relation roots, but \(2^3\) separates the factors.

Now suppose canonical feedback appends integer endpoints whose residues
already lie in an old graph subgroup \(H\). Exact gcd-free refinement can
still expose smaller integer blocks and produce a larger public subgroup
\(K\ge H\). Put

\[
c=[K:H],
\qquad
a=[K_p:H_p],
\qquad
b=[K_q:H_q].
\]

The quotient projections are surjective, \(a\mid c\), \(b\mid c\), and the
exact number of positive separators in \(K\) is

\[
\boxed{\frac ca+\frac cb-2.}
\]

Thus the old graph breaks exactly when

\[
\boxed{c>a\quad\text{or}\quad c>b.}
\]

This identifies the precise framework-level effect. Residue-neutral
feedback can change the algorithm's available subgroup because integer
factor blocks need not lie in the subgroup containing their product.
Lockstep growth with \(c=a=b\) does not help.

For the P88 canonical phase witness at \(N=2047\), refinement exposes the
block 2 and gives

\[
\boxed{c=11,\qquad a=b=1.}
\]

Neither local projection image grows, yet the old graph breaks and the new
subgroup contains exactly 20 positive separators. This is a pure phase
expansion. The theorem does not make the hidden indices public, enumerate
the subgroup, choose a separator, or prove that feedback creates this event
on general inputs.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
7a53ba1df08ad90c54e034fe23712587563f764fcaf1efb3e4a8445103a4319d,
98debf97ea45cd4f444e993d8c07f93d4b93c534ce7871da8af5ac26f5d2cd0b,
c903631dd78edc6487c3f3f890d3078a2f332a46012449456dc402cc523b7812,
and
c949c944d9c674551f92bfa0abc8decfbd178d0577a04643051101ae5103b6bd.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P91 — one prime-saturation closure adds one canonical root coset

**Status:** promoted from F85 after a hostile proof-only audit with explicit
scope corrections and a proof-blind reconstruction. This is an incremental
factor-free decoder theorem, not a relation source or a factoring algorithm.

Let \(E\) be the exponent matrix of an explicit relation list on
pairwise-coprime unit blocks, let \(\ell\) be a public prime, and put

\[
V=\ker(E\bmod\ell).
\]

After complete joint gcd-free refinement, append one relation column \(b\).
If

\[
b\notin\operatorname{colspan}_{\mathbb F_\ell}(E),
\]

then no new saturation vector appears:

\[
\ker[E\mid b]=V\times\{0\}.
\]

If \(Ec+b=0\) and \(z=(c,1)\), then

\[
\boxed{
\ker[E\mid b]
=(V\times\{0\})\oplus\langle z\rangle.
}
\]

Let \(H\) be the old image of the exact \(\ell\)-th-root map, and let
\(s_c\) be the exact public root induced by \(z\). The full new root image is

\[
\boxed{H'=\langle H,s_c\rangle.}
\]

Changing the solution \(c\) multiplies \(s_c\) by an old root. Therefore
the canonical new object, relative to the full lifted block and exponent
presentation, is the coset \(s_cH\), not one preferred root.

Assume the complete old prime-saturation decoder has failed. If all old
basis roots are one, then \(H=1\), and the single test
\(\gcd(s_c-1,N)\) is complete for the new image. Otherwise, any public
nonidentity old basis root \(h\) generates the old graph line, and the menu

\[
\boxed{\{s_ch^t:0\le t<\ell\}}
\]

is complete. It contains exactly two positive separators if the new coset
leaves the old graph and none if it does not. Thus one appended relation
needs at most \(\ell\) new gcd tests, rather than a fresh scan of all
support-two kernel combinations. The procedure is polynomial when the
numerical value of \(\ell\) is polynomial in the explicit presentation
size. A public implementation first tests \(\gcd(\ell,N)\).

The result gives no law that makes the new column close, makes the induced
coset leave the graph, or selects a useful prime. The final candidate adds
only the audit's explicit nonnegative-exponent, presentation, and
\(\gcd(\ell,N)\) scope qualifications to the audited theorem.

The final candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
51f858a40d1756dd27efbabfac0aeedb16cb86eef5ef48679b81b861b0cb069f,
eb6bb95999fcb80ce521029474a91e75a605e392a95c0912f0215f58ebb31dc8,
cd439393760f0e4d5ad88fbe8321cb8a752dab270cfc8353223d8c3eb040706d,
and
27d68ef66df52d13f1ccd6ad31740f68629833f9dcc1a0bb8bf2bed41159fa9f.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P92 — whole-subgroup power contraction makes a bounded phase expansion enumerable

**Status:** promoted from F86 after a hostile proof-only audit and a
proof-blind reconstruction. This is a conditional deterministic
post-feedback algorithm, not an all-input source law or factoring algorithm.

Let \(H\) be a diagonal graph subgroup of order \(h\), and let \(K\ge H\)
be a strict pure phase extension:

\[
K_p=H_p,
\qquad
K_q=H_q.
\]

Then \(K/H\) is cyclic of order \(c\mid h\), and after identifying the old
graph,

\[
K=H\cdot(\{1\}\times D)
\]

for a cyclic group \(D\) of order \(c\), with trivial intersection. For a
public exponent \(M\), put

\[
h_M=\frac h{\gcd(h,M)},
\qquad
c_M=\frac c{\gcd(c,M)}.
\]

Then

\[
\boxed{|K^M|=h_Mc_M.}
\]

If \(c_M>1\), the powered subgroup contains exactly \(2c_M-2\) positive
separators.

Let \(M_B=\operatorname{lcm}(1,\ldots,B)\) and let the punctured bank contain
\(M_B\) and every \(M_B/\ell^j\) with \(\ell^j\le B\). If the largest full
prime-power component \(\sigma(h)\) is at most \(B\), then some bank exponent
\(E\) gives

\[
\boxed{c_E=\ell,\qquad h_E\le B,\qquad |K^E|\le B^2}
\]

for a prime \(\ell\mid c\). The image contains exactly
\(2\ell-2\) separators and has density at least \(1/B\).

A public algorithm powers every generator of \(K\) by every bank exponent,
enumerates the resulting subgroup with a \(B^2\) cap, and gcd-tests every
visited element. This is deterministic polynomial time for
\(B=\operatorname{poly}(\log N)\). It uses no hidden branch detector,
order, projection, or cancellation word.

For the P88 state

\[
N=2047,
\qquad
H=\langle11\rangle,
\qquad
K=\langle11,2\rangle,
\]

one has \(h=22\), \(c=11\), and the bank exponent \(E=2520\) gives a
subgroup of order 121 with 20 positive separators. This completes that
fixed phase witness even though every pure power of the exposed block 2
fails. The theorem changes the operation from selecting one mixed word to
contracting and completely enumerating a whole public subgroup.

The missing theorem is still source-side. Nothing here proves that feedback
creates a strict pure phase extension or that \(\sigma(h)\) is polynomially
bounded on all inputs. The final candidate differs from the audited version
only by wording and TeX corrections; the proof-blind reconstruction verifies
the final mathematical statement.

The final candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
1b53676cae4856a1a745c44aae8c0c49d9750d57cae26d2157dd34f0a9e644c2,
c5ce39d4d4b1a63fe31a691509d259a88a427869d91018ca41122340d7efd16a,
e864530fbf489c1af09aef0371fcb86857d9c502c8bca887c1767138d1c9af3c,
and
9186362a09e28c77c4ff6bdc4be5a8d25de56c970b325bc5a7d417396de9b488.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P93 — bounded subgroup exponent makes every positive separator enumerable

**Status:** promoted from F87 after a hostile proof-only audit and a
proof-blind reconstruction. This is a conditional deterministic decoder for
a supplied subgroup of a squarefree semiprime, not a subgroup source or an
all-input factoring algorithm.

Let \(N=pq\) for distinct odd primes. Let \(K\) be given by a public
polynomial-size generator list and let

\[
\lambda=\exp(K).
\]

Assume that \(K\) contains a positive separator and that every full
prime-power component of \(\lambda\) is at most \(B\):

\[
\boxed{\sigma(\lambda)\le B.}
\]

For \(M_B=\operatorname{lcm}(1,\ldots,B)\), use the same punctured bank as
P92. Choose any separator \(x\), a prime
\(\ell\mid\operatorname{ord}(x)\), and put

\[
C=v_\ell(\operatorname{ord}(x)),
\qquad
H=v_\ell(\lambda),
\qquad
e=v_\ell(M_B).
\]

The bank exponent

\[
E=M_B/\ell^{e-C+1}
\]

keeps \(x^E\) as a positive separator of exact order \(\ell\), kills every
other primary component, and makes \(K^E\) an \(\ell\)-group of exponent at
most \(\ell^{H-C+1}\le B\). Because a subgroup of the product of two cyclic
local groups has rank at most two,

\[
\boxed{|K^E|\le B^2.}
\]

The same capped public enumeration as in P92 therefore finds a factor in
deterministic polynomial time. It does not know the separator, the useful
prime, an element order, the subgroup exponent, either hidden factor, or an
order/phase branch. It covers unequal-order and equal-order phase separators
uniformly.

For \(N=2047\), \(K=\langle11,2\rangle\) has exponent 22. With \(B=11\),
the exponent 2520 again gives a group of order 121 containing 20 positive
separators.

The theorem removes the branch detector and mixed-word selector only under
the supplied separator and bounded-exponent promises. It gives no law that
canonical feedback creates such a subgroup, and its rank-two size bound is
specific to the two-field CRT setting. The final candidate differs from the
audited version only by TeX corrections; the proof-blind reconstruction
verifies the final mathematical statement.

The final candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
e12d85db167da5b6611e30dd808194b33d1944a2090819d1e08b27625335d984,
a42cf3d89d8e3f1b7f79c834ab03bd6d0d195e4e15f6c36c0d749c693126ebe8,
f4647ddba86b2ff7ce85936f8fd977158f78ece9d2ef55692fac01213eb5494f,
and
a051db102398e38564632656332d667a6cdd7bfe6f00595d7cb8b586eeb8de34.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P94 — the public exponent N−1 isolates a bounded pure-phase component

**Status:** promoted from F88 after a hostile proof-only audit and a
proof-blind reconstruction. This is a conditional deterministic decoder for
a supplied pure-phase feedback state, not an all-input source law or
factoring algorithm.

Let \(N=pq\) for distinct odd primes. Let \(H\) be a diagonal graph subgroup
of order \(h\), and let \(K\ge H\) be a strict pure phase extension with

\[
K_p=H_p,
\qquad
K_q=H_q,
\qquad
c=[K:H]>1.
\]

The phase quotient is cyclic and

\[
c\mid h.
\]

More importantly, the synchronized old order has a public annihilator:

\[
\boxed{h\mid N-1.}
\]

Indeed, \(h\mid p-1\) and \(h\mid q-1\), so
\(pq\equiv1\pmod h\). This replaces P92's global bounded-order hypothesis
by a public integer already available from bare \(N\).

Choose a prime \(\ell\mid c\), and write

\[
e=v_\ell(N-1),
\qquad
H_\ell=v_\ell(h),
\qquad
C_\ell=v_\ell(c).
\]

For

\[
E=\frac{N-1}{\ell^{e-C_\ell+1}},
\]

the exact powered-state parameters are

\[
\boxed{
c_E=\ell,
\qquad
h_E=\ell^{H_\ell-C_\ell+1},
\qquad
|K^E|=\ell^{H_\ell-C_\ell+2}.
}
\]

The image contains exactly \(2\ell-2\) positive separators. All
non-\(\ell\) components of the old graph and phase quotient disappear,
including large primes that the algorithm never factors or scans. In the
strongest case \(C_\ell=H_\ell\), the image has order \(\ell^2\), with no
condition on the other prime-power components of \(h\).

A public algorithm scans primes \(\ell\le L\) dividing \(N-1\), every
puncture \((N-1)/\ell^j\), and enumerates each powered subgroup with cap
\(S\). It deterministically factors \(N\) whenever some
\(\ell\mid c\) satisfies

\[
\boxed{
\ell\le L,
\qquad
\ell^{H_\ell-C_\ell+2}\le S.
}
\]

For polynomial numerical bounds \(L,S\), the scan has polynomial bit
complexity. It uses no hidden factor, subgroup order, phase index,
valuation, branch detector, or cancellation word.

For the P88 state at \(N=2047\), one has \(h=22\), \(c=11\), and

\[
\boxed{E=(N-1)/11=186.}
\]

The powered subgroup has order 121 and contains 20 positive separators.
This is the strongest current algorithmic completion of the literal phase
witness: it powers and enumerates a whole subgroup instead of selecting one
scalar for one gcd.

The remaining promise is exact. Feedback must first create a strict pure
phase extension, and its quotient must contain a scanned prime whose full
residual image fits the polynomial cap. A small raw valuation gap alone is
not sufficient. General order/phase mixtures, arbitrary composites, and an
all-input source law remain open.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
c8a4d65af2ad0148ec3c05feb8147efc964e3f2fd2e9b97049ed7872d34b1c39,
b319de808fc88d9f811fc61d59619ede7b12bbebd4b22b4c01660705339ac687,
f6b264e4c7e45fbac65fe8071dc59b68332715f559102f09df3da076f384d054,
and
537468a5dcd233bae1970a7f10f09005e70bdb5d2dd5b0dfb24c338932d62ba3.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P95 — powering by N−1 removes all shared local-order components

**Status:** promoted from F89 after a hostile proof-only audit and a
proof-blind reconstruction. This is a public subgroup normalization and two
conditional decoders, not an all-input factoring algorithm.

Let \(N=pq\) for distinct odd primes, let

\[
K\le(\mathbb Z/N\mathbb Z)^\times,
\]

and put \(E=N-1\), \(S=K^E\). If the two local projection orders of \(K\)
are \(m_p,m_q\), define

\[
A=\frac{m_p}{\gcd(m_p,E)},
\qquad
B=\frac{m_q}{\gcd(m_q,E)}.
\]

Then

\[
\boxed{\gcd(A,B)=1}
\]

and the powered subgroup is the full product of its local images:

\[
\boxed{
S=K_p^E\times K_q^E,
\qquad
|S|=AB.
}
\]

Indeed, a prime dividing both residual image orders would force both
\(p\) and \(q\) to be one modulo a prime power larger than the corresponding
valuation of \(N-1\), a contradiction. Surjective projections of coprime
orders force the full product. Thus the public power removes every shared
order component and every residual graph correlation.

The powered subgroup contains exactly

\[
\boxed{A+B-2}
\]

positive separators, with uniform density

\[
\boxed{
\frac1A+\frac1B-\frac2{AB}.
}
\]

Near-uniform public sampling is therefore a Las Vegas polynomial-time
decoder when \(S\ne1\) and one of \(A,B\) is numerically polynomial in
\(\log N\). Deterministic capped subgroup enumeration succeeds when
\(1<AB\) fits a public polynomial cap. Neither algorithm knows the hidden
orders.

If \(K\) contains a diagonal graph subgroup \(H\), then
\(|H|\mid N-1\), so the power map kills \(H\), factors abstractly through
\(K/H\), and

\[
|S|\le[K:H].
\]

At \(N=4033\), the feedback-exposed block 5 has local orders 36 and 27.
The public exponent \(4032=N-1\) leaves local orders one and three, so

\[
\boxed{\gcd(5^{4032}-1,4033)=37.}
\]

At \(N=2047\), the special phase subgroup \(\langle11,2\rangle\) has
exponent 22 dividing \(N-1\), so the unpunctured image is trivial. P94's
puncture 186 is therefore necessary for that supplied subgroup.

The theorem does not decode the case in which both coprime local image
orders are large. It does not prove that feedback creates a polynomial
image or give an arbitrary-composite reduction. The final candidate fixes
two fraction-command characters and replaces one misleading “public
quotient” phrase in the audited version. The proof-blind reconstruction
verified the forced intended formula, and a separate certificate confirms
that the corrected statement makes no mathematical change.

The final candidate, hostile audit, original proof-blind statement,
corrected statement, proof-blind reconstruction, and correction certificate
have SHA-256 hashes
92b912f3741ff9d04e7772a03fb82bf2e80fe01d09c24de699921c374aad6101,
c7e51fadaf9259aa2fae128d2d1efb2480bb6ebd3a13c38add3902bf338b521b,
aafa64e607c6cd108b08b43d3084a91ca388930792c569db083c4b9d9e58fabe,
e504a24c285e0c98d64a37302e53e56b6656ec50361a507e003f37a1848d5779,
8d0948ae5348e5a67772f13f4b7a9249a25a85be6752ef229fd41bc51a4816f5,
and
11d7ccc125a27d6bea5a95e9b97f380366f812202aab07c1278ea260ee71e9e2.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P96 — a public annihilator makes every bounded primary separator enumerable

**Status:** promoted from F90 after a hostile proof-only audit and a
proof-blind reconstruction. This is a conditional deterministic decoder for
a supplied subgroup killed by \(N-1\), not a separator source or an
all-input factoring algorithm.

Let \(K\) be given by public generators and let
\(\lambda=\exp(K)\). The public test

\[
g_i^{N-1}=1\pmod N
\qquad\text{for every generator }g_i
\]

is equivalent to

\[
\boxed{\lambda\mid N-1.}
\]

Assume that this test passes and that \(K\) contains a positive separator
\(x\). Choose a prime \(\ell\mid\operatorname{ord}(x)\), and put

\[
e=v_\ell(N-1),
\qquad
H=v_\ell(\lambda),
\qquad
C=v_\ell(\operatorname{ord}(x)).
\]

The puncture

\[
E=(N-1)/\ell^{e-C+1}
\]

keeps \(x^E\) as a positive separator of exact order \(\ell\). It kills
every other primary component, and

\[
\boxed{
\exp(K^E)=\ell^{H-C+1},
\qquad
|K^E|\le\ell^{2(H-C+1)}.
}
\]

The size bound follows because a subgroup of two cyclic local
\(\ell\)-groups has rank at most two.

A public algorithm scans small primes \(\ell\le L\) dividing \(N-1\), every
puncture depth, and cap-enumerates every powered subgroup. It
deterministically factors \(N\) whenever some separator and prime satisfy

\[
\boxed{
\ell\le L,
\qquad
\ell^{2(H-C+1)}\le T
}
\]

for a public polynomial cap \(T\). The algorithm does not know the
separator, subgroup exponent, useful prime, hidden valuations, or factors.

At \(N=2047\), the subgroup \(\langle11,2\rangle\) passes the annihilator
test. The prime 11 and exponent 186 give the general upper bound 121; the
exact phase calculation attains 121 and contains 20 positive separators.
The public algorithm does not need to recognize the phase branch.

Together, P95 and P96 give a public structural split. If
\(K^{N-1}\ne1\), the powered subgroup is a nontrivial coprime-order
rectangle containing separators. If \(K^{N-1}=1\), \(N-1\) is a public
annihilator and the puncture decoder applies under its primary-image
promise. Neither branch proves that its factor-bearing image is polynomially
accessible on every input.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
96275cc1cb5b454722cc4ae18dead7ec8260d8c05e842f71709696afc19cc8f3,
7a82a8d3a8a8bb57d499b6e8a7c89c2869484e4df0e6694fd04ba62b53fa607c,
d65001d43a35c32ff826e6fa7cda54dbcaccf47cf9078c07111eb47b5aa005cf,
and
a1283b5e6d6de1f72404a75bbc0f43e706775d4a7ff55b95f49eed3e530747eb.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P97 — bare N supplies constant-probability generators of a factor-bearing rectangle

**Status:** promoted from F91 after a hostile proof-only audit and a
proof-blind reconstruction. This is a source theorem and an exact reduction
to axis localization for distinct odd semiprimes. It is not an axis decoder
or a factoring algorithm.

Let

\[
N=pq,
\qquad
g=\gcd(p-1,q-1),
\qquad
A=(p-1)/g,
\qquad
B=(q-1)/g
\]

for distinct odd primes \(p,q\), and put

\[
G=(\mathbb Z/N\mathbb Z)^\times,
\qquad
S_N=G^{N-1}.
\]

Then

\[
\boxed{
S_N\cong C_A\times C_B\cong C_{AB},
\qquad
\gcd(A,B)=1,
\qquad
AB>1.
}
\]

The two nonidentity coordinate axes contain exactly \(A+B-2\) positive
separators. Their exact uniform density is

\[
\delta_N=\frac1A+\frac1B-\frac2{AB}.
\]

Sample \(a\) uniformly from \(1,\ldots,N-1\). A nonunit sample immediately
gives a proper factor. Conditioned on being a unit, \(a\) is exactly uniform
in \(G\), and \(a^{N-1}\) is exactly uniform in \(S_N\). Unit acceptance has
probability greater than one half.

For two independent accepted units, put

\[
y_i=a_i^{N-1}\pmod N.
\]

The public pair generates the complete powered rectangle with exact
probability

\[
\boxed{
\Pr(\langle y_1,y_2\rangle=S_N)
=\prod_{\ell\mid AB}(1-\ell^{-2})
\ge\frac6{\pi^2}>0.6.
}
\]

Thus bare \(N\) supplies a constant-size public generating set for a
guaranteed factor-bearing subgroup with constant probability and polynomial
work. No new subgroup sampler is required on this input class.

This gives an exact promise reduction. Suppose a polynomial-time procedure,
on every public list generating \(S_N\), returns an element \(z\) of that
generated subgroup with

\[
1<\gcd(z-1,N)<N
\]

with inverse-polynomial probability. Suppose it has polynomial bounded work
on every list and returns only verified factors or failure. Fresh two-sample
batches and verified repetition then give a classical Las Vegas
expected-polynomial factorer for distinct odd semiprimes. The reduction does
not need to recognize which pairs generate \(S_N\).

The source does not solve the promise task. When both \(A\) and \(B\) are
large, direct uniform sampling can have exponentially small separator
density in the input length. Inside the cyclic group \(C_{AB}\), the two
axes are the unique subgroups of hidden orders \(A\) and \(B\). The missing
operation is therefore axis localization, or a feedback/refinement step that
changes this coprime-order rectangle. This is an access statement, not a
computational lower bound.

At \(N=4033=37\cdot109\), one has \(g=36,A=1,B=3\), and

\[
\gcd(5^{4032}-1,4033)=37.
\]

At \(N=2047=23\cdot89\), one has \(g=22,A=1,B=4\), so a fresh powered unit
gives a proper gcd with probability \(3/4\). This does not contradict the
smaller feedback subgroup \(\langle11,2\rangle\) being killed by \(N-1\).

The final candidate implements the audit's exact-versus-near-uniform wording
correction and adds explicit generated-subgroup membership to the promise
task. These are precision and scope corrections; they do not change the
proved theorem. The final candidate, hostile audit, proof-blind statement,
and proof-blind reconstruction have SHA-256 hashes
22d818157876d303c038fa4caa68bef2c94f9b6a709e2691be2d8554e642d46d,
e1a20aef5e85424fed8ac42606dc12be44c9c5cd47ef69b98ed1827ad6ee2cee,
547f538367abef228c387761fb1f67a4c778d127c0c69b8ce013e96ae211b07c,
and
7e1d572adb0ce54008e521bd23e8fa777c9f39755c6f4b4d5b3c7bbe6412116b.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P98 — feedback cannot change the stable N−1-powered core

**Status:** promoted from F92 after a hostile proof-only audit and a
proof-blind reconstruction. This is a structural boundary for retained
multiplicative feedback after the P97 source succeeds. It is not an axis
decoder or a factoring algorithm.

Let \(N=pq\) for distinct odd primes. Put

\[
E=N-1,
\qquad
g=\gcd(p-1,q-1),
\qquad
A=(p-1)/g,
\qquad
B=(q-1)/g,
\]

and let

\[
G=(\mathbb Z/N\mathbb Z)^\times,
\qquad
S=G^E.
\]

P97 gives \(S\cong C_A\times C_B\) with \(\gcd(A,B)=1\). The quotient
above this full powered rectangle is exactly

\[
\boxed{G/S\cong C_g\times C_g},
\qquad
g\mid E.
\]

Consequently, every retained multiplicative no-factor feedback state
\(S\le K\le G\) satisfies

\[
(K/S)^E=1,
\qquad
S^E\le K^E\le S.
\]

Let \(A_*\) and \(B_*\) be the largest divisors of \(A\) and \(B\)
coprime to \(E\), and let

\[
T\cong C_{A_*}\times C_{B_*}
\]

be the corresponding CRT product. For
\(n=\lceil\log_2(N+1)\rceil\), every such feedback supergroup has the same
stable image:

\[
\boxed{K^{E^n}=T.}
\]

Every exponent supported only on primes dividing \(E\) acts as an
automorphism of \(T\). It preserves the two hidden coordinate identity
tests and therefore cannot turn a nonseparator in \(T\) into a separator.
This includes every repeated \(N-1\) power and every existing puncture made
by deleting prime powers from \(N-1\).

The exact identity

\[
E/g=gAB+A+B
\]

implies

\[
\gcd(A,E/g)=\gcd(B,E/g)=1.
\]

Thus the transient primes in the P97 local orders are precisely primes
already present in \(g\). If \(\gcd(AB,g)=1\), then \(T=S\), and one
\(N-1\) power sends every feedback supergroup back to the original P97
rectangle.

Stable hard cases are not exceptional. For every numerical \(H\), there
are distinct odd primes \(p,q\) with

\[
g=2,
\qquad
A>H,
\qquad
B>H,
\qquad
\gcd(AB,E)=1.
\]

The proof uses CRT and Dirichlet's theorem. It is an existence family, not
an executable factoring step or an input-density theorem.

The fixed witnesses \(4033\) and \(2047\) are transient: their P97 order
pairs are \((1,3)\) and \((1,4)\), supported on primes dividing \(N-1\).
They prove a real feedback operation but do not test the stable two-large-
order case. A small stable example is

\[
2773=47\cdot59,
\qquad
(A,B)=(23,29),
\qquad
\gcd(23\cdot29,2772)=1.
\]

The theorem assumes that the P97 generators of \(S\) were retained and
that feedback only changes the multiplicative unit subgroup between \(S\)
and \(G\). It does not constrain useful transient steps before
normalization, canonical integer side information, non-multiplicative data,
or states that discard the P97 generators. It treats distinct odd
semiprimes only and gives no axis localizer, progress law, lower bound, or
factoring algorithm.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
6c9d9166ca335d115fab18bef6c7c7d90a4bafd7aee3789a071618f6a3f918c0,
b64ae5e9d2365002d55571b17578a93e75a88a836ee7bd9f983b75e837ac739b,
fa3b1b9f81e14b8c054a0b8b9b0f589781f46615277cf12adc25da98ee5a6cc7,
and
1e5ddb53a9b14e3bd020d55ad5771e672cc10a0f0b03f624bc055edaed21df17.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P99 — bare N supplies constant-probability generators of the full unit group

**Status:** promoted from F93 after a hostile proof-only audit and a
proof-blind reconstruction. This is an all-input source theorem and a
correction to the abstract-subgroup interpretation of feedback. It is not a
factor localizer or a factoring algorithm.

For a finite abelian group \(H\), let

\[
r_\ell=\dim_{\mathbb F_\ell}(H/\ell H).
\]

The exact probability that \(d\) independent uniform elements generate
\(H\) is

\[
\boxed{
\prod_{\ell\mid |H|}
\prod_{i=0}^{r_\ell-1}(1-\ell^{i-d}).
}
\]

In particular, if \(|H|<2^n\), then \(n\) uniform elements generate
\(H\) with probability at least the absolute constant

\[
c_0=
\prod_{\ell\ \mathrm{prime}}
\prod_{k=2}^{\infty}(1-\ell^{-k})
>e^{-4/3}>0.
\]

For any \(N\ge2\), put

\[
G_N=(\mathbb Z/N\mathbb Z)^\times,
\qquad
n=\lceil\log_2(N+1)\rceil.
\]

Sample \(n\) exact uniform integers from \(1,\ldots,N-1\) and compute
their gcds with \(N\). One batch has probability at least \(c_0\) of
either returning a proper factor or supplying a public list that generates
the complete unit group \(G_N\). Exact rejection sampling has expected
polynomial fair-random-bit cost with an exponentially decaying tail, and
the total expected bit cost is polynomial.

For a distinct odd semiprime, three independent uniform units generate the
full unit group with probability at least

\[
\boxed{1/(\zeta(2)\zeta(3))>0.}
\]

The complete unit group contains a factor-revealing element for every
composite \(N\). For a prime power \(p^e\), the unit \(1+p\) exposes
\(p\). For an integer with at least two primary factors, CRT gives a unit
that is one on a proper nonempty set of components and nonidentity on the
others. This is existential and does not publicly construct the element
without the factorization.

Condition on a batch that generates \(G_N\). Every later unit exposed by
canonical multiplicative feedback is already in the generated abstract
subgroup. Thus feedback cannot enlarge that subgroup on this event. This
does not make feedback redundant. The theorem supplies no public method to
recover an exponent word for the element. Feedback can instead expose one
named canonical integer, one gcd-free block, one relation with known
provenance, or one direct decoder input. Therefore

\[
\boxed{
\text{abstract subgroup availability}
\ne
\text{public word and integer-presentation accessibility}.
}
\]

This distinction is the correct scope of the \(4033\) and \(2047\)
feedback witnesses. They prove representation-level gain relative to their
restricted transcripts. They do not prove that feedback expands the
abstract subgroup after a full-group generator batch is retained.

If one polynomial-bounded procedure factors \(N\) with
inverse-polynomial probability on every list generating \(G_N\), then
fresh batches, verified outputs, and repetition give a classical Las Vegas
expected-polynomial factorer for every composite \(N\). The source theorem
does not supply this promised localizer, recognize the generation event,
give useful separator density, compute orders, recover words, solve an HSP,
or prove a factoring algorithm.

The hostile audit pinned the original candidate with SHA-256 hash
a198049a27b409516926c716b3ea281c95b430cd6c3382abc3de0a3a4ee764c5.
The final candidate applies its two wording corrections: exact interval
sampling has expected polynomial random-bit cost, and no classical hardness
claim is made for word recovery. The final candidate, hostile audit,
proof-blind statement, and proof-blind reconstruction have SHA-256 hashes
90a4a39313544a554201a463066f539c16f2f2dc09aef4e2dbfb135c5e42bb34,
7d98b6232cbd5dc89271e53b87f526623d39c40dfd54af546e14f99aac014c4f,
a9ddb299aee512ec028cd8ed52c631f86675e2d134b2aa1e3c8b2c80c1f387bb,
and
6857799dc1aa91aeb87336a8586ae9eeb074ee6d64c162348aee7ac1c1e80030.
No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P100 — feedback saturation has two exact presentation gates

**Status:** promoted from F94 after two earlier versions failed hostile
audit, the corrected candidate passed a fresh hostile audit, and a
proof-blind reconstruction passed. This is an exact accounting theorem for
known multiplicative relations. It is not a feedback source law or a
factoring algorithm.

Let \(E\) be the integer exponent matrix of the relations that an algorithm
currently knows on pairwise-coprime unit blocks. Suppose exact gcd-free
refinement replaces the old blocks by new blocks, with public exponent map
\(\Delta_\alpha\). For every prime \(\ell\), reduction modulo \(\ell\) gives

\[
\boxed{
\dim\ker(\Delta_\alpha E)-\dim\ker E
=\dim(\operatorname{im}E\cap\ker\Delta_\alpha).
}
\]

Thus refinement creates a new known \(\ell\)-saturation dependency exactly
through an exponent-multiplicity event. With disjoint old-block supports,
\(\ker\Delta_\alpha\) is generated by the old blocks for which every
descendant exponent is divisible by \(\ell\). Multiplicity-free refinement
cannot open this gate.

After refinement, append one known relation column \(u\). It creates a new
kernel direction exactly when

\[
\boxed{u\in\operatorname{colspan}(\Delta_\alpha E\bmod\ell).}
\]

When this column-closure gate opens, the nullity grows by exactly one and
the decoder obtains one normalized candidate root coset. The coset can be
the old root image, so closure alone does not prove a new root or a factor.
Under the P91 distinct-odd-semiprime hypotheses, at most \(\ell\) cross-coset
gcd tests complete this update. A polynomial-in-\(\log N\) algorithm must
therefore cap the numerical size of \(\ell\), or cap the total materialized
decoder menu explicitly.

A new relation that contains a fresh block with exponent nonzero modulo
\(\ell\) cannot close on that step. In particular, a fresh cofactor with
exponent one blocks closure for every prime. More generally, any fixed
collection of relation columns with distinct stable private rows adds no
new kernel direction, regardless of its size. Later progress requires
reuse of such a row by another relation, or loss of its witness through the
multiplicity gate. Therefore relation count alone does not amortize into a
saturation dependency.

On P99's constant-probability full-unit-group source event, the current
blocks already generate the full abstract unit group. Exact no-factor
refinement preserves that equality. Feedback can still change the public
presentation by naming integer blocks and recording relations, but
abstract subgroup growth is not progress on this event.

The accounting also shows that a proposed ephemeral-probe rule is not
lossless if it deletes every nonclosing relation. Over \(\mathbb F_2\), the
first column \([1]\) is nonclosing, while a second \([1]\) closes against it
and creates the dependency \((1,1)\). Deleting the first column destroys
this future closure.

All matrix and root operations are polynomial in the total explicit state
and menu size. This does not prove that a feedback process keeps that state
polynomial in \(\log N\). The theorem supplies no all-input gate-opening
law, non-global root law, polynomial state cap, or factoring algorithm.

The corrected candidate, final hostile audit, proof-blind statement, and
proof-blind reconstruction have SHA-256 hashes
1992f91ad7a4d3dce8dd51836098f0f7dce2411dc043a055fa7f1363463af2d1,
77559859ca5a1f642a3101d531b770955beb68871aeb7df3a2cb1a8931265664,
69229c3b4e2590812dc8bf45aa536f8837b337107957f3ac2914956879067def,
and
2f4a28fa711707c7767ce1d13bf5a197eeb830d64c64a6ef44cbe02f6ae6894b.
The two failed candidates and their audits remain in the F94 artifact
directory. No research computation, cross-family audit, human audit, or
publication-level literature review has run.

## P101 — two retained canonical-inverse relations can close on a stable input

**Status:** promoted from F95 after a hostile audit and a proof-blind
reconstruction. This is an exact finite mechanism witness. It is not a
polynomial-time relation selector or a factoring algorithm.

At the P98-stable semiprime

\[
N=2773=47\cdot59,
\qquad
\gcd(23\cdot29,N-1)=1,
\]

two canonical-inverse relation values are

\[
P_1=3\cdot1849=1+2N=3\cdot43^2
\]

and

\[
P_2=842\cdot2526=1+767N=3\cdot842^2.
\]

Public factorization-free normalization uses

\[
\gcd(P_1,P_2)=3,
\qquad
P_1/3=43^2,
\qquad
P_2/3=842^2.
\]

On the pairwise-coprime basis \((3,43,842)\), the two exponent columns are

\[
(1,2,0)^T,
\qquad
(1,0,2)^T.
\]

Each column is nonzero modulo two. The two columns are equal modulo two, so
the first retained relation makes the second one close. The induced exact
root is

\[
R=\sqrt{P_1P_2}=108{,}618,
\]

and

\[
\gcd(R-1,N)=47,
\qquad
\gcd(R+1,N)=59.
\]

Deleting the first nonclosing relation loses this cycle. Thus relation
retention can create a useful state that is not represented by the latest
scalar gcd alone. Algebraically, the event is an exact congruence-of-squares
collision: \(43\) and \(842\) are two roots of the same unit and differ by a
non-global CRT sign.

The declared search exhausted all nontrivial residues modulo this fixed
\(N\). It inspected 634 distinct relation values and 934 eligible relation
pairs. This costs \(\Theta(N)\), and the result supplies no polynomial-time
rule for selecting the second relation. Its value is the stable, exact
existence of the retained-relation cycle.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
`b18011a72a0fa7c53e9520963498b5a14af73f9877abd91a96b0262fb3d48ead`,
`11902f16cab1619a7dd54b513e24197df0edbbb7002707e51055a3f73525b9d2`,
`f9c7e4a0a35fe58ae4cf46320dd858bbfd99e7fd18dfd799eb5f3bc10bdbc690`,
and
`4c2ccd6ffb429c6193000e5bec70380f91b5b5380bfce181bc289b2db9cfe58c`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P102 — canonical reduction can create a useful relation presentation inside the old subgroup

**Status:** promoted from F96 after two failed wording or counting rounds, a
fresh hostile re-audit, and a proof-blind reconstruction. This is an exact
square-class theorem and a target-free polynomial-size selector on one fixed
input. It is not an all-input factoring algorithm.

Let \(N\) be odd, and let two positive nonsquare canonical-inverse relation
values satisfy

\[
P_i=g_iw_i\equiv1\pmod N.
\]

They have the same nonzero class in
\(\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2\) exactly when
\(P_1P_2\) is an integer square. Equivalently, for
\(D=\gcd(P_1,P_2)\), there are coprime positive integers \(A,B\) with

\[
P_1=DA^2,
\qquad
P_2=DB^2,
\]

where \(D\) is nonsquare. For

\[
R=\sqrt{P_1P_2}=DAB,
\]

one has the exact public identities

\[
\gcd(R-1,N)=\gcd(A-B,N),
\qquad
\gcd(R+1,N)=\gcd(A+B,N).
\]

The collision factors \(N\) exactly when its root is not globally
\(\pm1\). Equal square class alone is insufficient: an exact example at
\(N=143\) produces only the global root \(-1\).

For the P101 state at \(N=2773\), let

\[
H=\langle3,43\rangle=\langle43\rangle.
\]

The useful endpoint \(842\) is outside \(H\). Nevertheless, the same useful
relation value has the target-free presentation

\[
c=[3^{99}43]_N=1263,
\qquad
w=c^{-1}_{\rm can}=1684,
\]

with both endpoint residues in \(H\), and

\[
cw=2{,}126{,}892=3\cdot842^2=P_2.
\]

Thus canonical reduction creates no new abstract modular element. It creates
a new exact integer presentation. Public square normalization of that
presentation exposes the closing root and factors \(N\). This is a genuine
source-operation change: the twelve raw products \(3^a43^b<N\) find no
distinct useful relation, while canonical reduction of a longer word does.

A separate target-free executable receives only \(N\), blocks \(3,43\), and
the bound \(n^2=144\). It tests \(145^2=21{,}025\) exponent pairs. The first
distinct useful hit is \((a,b)=(99,1)\); four earlier same-class hits only
repeat \(P_1\) and give a global root. This is a polynomial-size selector for
the fixed input. The bound was found after a complete \(O(N)\) subgroup scan,
so no all-input word-length or success-density law follows.

The final candidate, hostile re-audit, proof-blind statement, and
proof-blind reconstruction have SHA-256 hashes
`4ffa68dc66bd48f62c15fc1ef16dc8e54c4157e64f5c1f49ee544e24e06783d9`,
`d41637b590974e88d9bf73206d0681c297ec9c42e77fec8878eead0e2309a788`,
`b2a06e0ee52c2734595e22bebaaaa8dcabd5378d1d175f2e88473704d0c6c783`,
and
`b7e3fd7e00149dfbcd9dbecebfca3597455720c94b8a2f07a73220eaa9d31ca2`.
Both failed candidate rounds remain in the F96 artifact directory. No
cross-family audit, human audit, or publication-level literature review has
run.

## P103 — one public feedback batch can factor only through an amortized relation circuit

**Status:** promoted from F98 after a hostile audit and a proof-blind
reconstruction. This is an exact fixed-input mechanism witness. It is not an
all-input success law or a factoring algorithm for arbitrary integers.

Let

\[
N=202{,}537{,}109=10{,}267\cdot19{,}727.
\]

Both factors are prime and exceed the declared trial bound
\(n^2=784\), where \(n=28\). The stable-core certificate is

\[
g=2,\qquad (A,B)=(5133,9863),\qquad \gcd(AB,N-1)=1.
\]

The public one-round rule receives only \(N\). It starts from the canonical
inverse presentations for seeds 2 through 28, refines their integer
endpoints into a pairwise-coprime exact basis, and deterministically selects
27 block pairs. For each pair \((u,v)\), it processes both trajectories

\[
[u^e v]_N,\qquad [uv^e]_N,\qquad 0\le e\le784.
\]

It retains 27 seed relations and 12,522 new first-occurrence relations.
Every one of the 12,549 individual tests

\[
\gcd(c-w,N),\qquad\gcd(c+w,N),
\quad w=c^{-1}_{\rm can},
\]

is nonproper. Thus no selected presentation factors \(N\) by itself.

The factor-free joint decoder removes one value \(P=1\) and 3,134 repeated
exact values. On the remaining 9,414 distinct relation values, exact gcd
refinement gives 11,015 nonsquare rows, rank 8,926, and kernel dimension
488. A public kernel-basis vector uses 166 distinct exact values. Its exact
positive root satisfies

\[
R\equiv132{,}013{,}085\pmod N,
\]

\[
\gcd(R-1,N)=19{,}727,
\qquad
\gcd(R+1,N)=10{,}267.
\]

An independent online elimination on the first 5,616 retained occurrences
first finds a useful dependency at occurrence 5,616. After repeated exact
values are normalized away, the dependency contains 166 distinct values and
gives the opposite mixed root. Exhaustive factor-free checks find no useful
dependency of support one, two, or three in that prefix. They do not prove
that 166 is globally minimal.

This is a real algorithmic change from evaluating one new scalar and taking
one gcd. No local scalar succeeds. The public state retains many individually
useless integer presentations, finds one exact square-class circuit, and
only then applies the final two gcds. The mechanism is close in form to
classical relation collection. No novelty relative to that literature is
claimed.

The bounded rule has polynomial bit complexity: it generates
\(O(n^3)\) candidate positions in this round, keeps polynomially many
\(O(n)\)-bit endpoints, performs exact gcd refinement, and runs binary
linear algebra on the explicit polynomial-size matrix. The theorem gives no
reason that a useful circuit must occur on another input.

The candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
`f2d28d074d53bc93c675553b28e083b93b0d6dd35d1a65edb430c69a6cd26fb0`,
`0c924e0b4805470c0e0a4547950b9b2a3d1b9a57cacfc5204f680d42354b9856`,
`92fd51676c579d26d573818782754d8db0687c7c554270b377f8421b33742e48`,
and
`7c3544af839a121b60fb05c07933966c85b4494b468bb0abeb0879b66075cb5a`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P104 — power feedback can create only duplicate roots or no relation at all

**Status:** promoted from corrected F99 after a failed scope audit, a fresh
hostile re-audit, and a proof-blind reconstruction. This is an exact
trajectory obstruction. It does not refute P103 or the full multi-seed rule.

Suppose

\[
N=\frac{a^m-1}{k},
\qquad 1\le k<a,
\]

and both \(a^r\) and \(a^{m-r}\) are canonical representatives for
\(1\le r<m\). Then

\[
c_r=a^r,\qquad w_r=a^{m-r},\qquad c_rw_r=a^m=1+kN.
\]

Every relation on this orbit is the same exact integer. If \(m\) is odd and
\(a\) is one prime basis block, all nonzero parity columns are identical.
Every duplicate-column dependency has normalized root \(+1\), and endpoint
refinement exposes no new block. Raw kernel nullity can therefore grow while
the normalized-root image does not grow.

The stable trial-hard instance

\[
N=64{,}570{,}081=1{,}871\cdot34{,}511
=\frac{3^{17}-1}{2}
\]

realizes this obstruction. Both factors exceed \(n^2=676\), and

\[
g=170,\qquad(A,B)=(11,203),\qquad\gcd(AB,N-1)=1.
\]

The complete range \(0\le e\le676\) visits 17 residues. Every nontrivial
presentation has exact value \(3^{17}=1+2N\), every direct sign gcd is one,
and every duplicate dependency has root \(+1\). Other seeds can still make
progress on this modulus.

There is also an opposite infinite obstruction. For every sufficiently
large \(T\), CRT, Dirichlet, and Linnik constructions give an odd semiprime
\(N_T\) with \(T\) consecutive states \(c_e=2^e\). Each relation

\[
P_e=1+(2^e-1)N_T
\]

has a private prime with odd valuation that divides no other \(P_j\). Their
square classes are linearly independent. The input length is
\(\Theta(T^2)\), so this gives \(T=\Theta(\sqrt{\log N_T})\) consecutive
relations with no dependency.

The two examples prove only that record count, raw nullity, and
consecutiveness are not progress laws. A successful multi-seed theorem must
prove reuse of parity rows and a non-global normalized root. The private-row
family does not establish stability, null direct screens, no block split, or
an \(n^2\)-long obstruction.

The corrected candidate, fresh hostile re-audit, proof-blind statement, and
proof-blind reconstruction have SHA-256 hashes
`d3a1af9e01f0209d8f06d53c2641bbad2056077bdca4d7966f9e6bdc98e592aa`,
`5f219d88f2c4fcc40d5ce3ea4040da91b86d97535b7efeac92fb7f07df5c6ca8`,
`53feb27185d06de2c0e8565bb1c324b02c13f64d1dfbab641ca9efa0923b1058`,
and
`52cc3f9bef3cf2e3abfeb49738f3dd69bd164328df6682e940fad6a54fde680c`.
The failed candidate and failed audit remain in the F99 directory. No
cross-family audit, human audit, or publication-level literature review has
run.

## P105 — the selected F98 factor certificate is one connected cross-trajectory circuit

**Status:** promoted from F100 after two failed wording audits, a final
hostile re-audit, and a proof-blind reconstruction. This is an exact
fixed-input structural result. It is not an all-input circuit-existence law.

Take the 166 distinct exact relation values used by the public F98
certificate for

\[
N=202{,}537{,}109=10{,}267\cdot19{,}727.
\]

Factor these values for diagnosis only and form their prime-valuation parity
matrix, including the row for prime 2. The matrix has 230 rows, 166 columns,
rank 165, and nullity one. The sum of all 166 columns is zero, while deleting
any one column leaves rank 165. Therefore the displayed dependency is the
unique nonzero dependency on this selected set, and every proper subset is
independent.

The shared-prime incidence graph is connected. It remains connected after
the prime-2 row is removed. The certificate contains one seed relation and
165 feedback relations. These feedback relations come from five active-pair
families and eight oriented trajectories. Thus the successful F98 event is
not a duplicate relation, one trajectory, or a local pair or triple. It is
one cross-trajectory parity circuit.

The exact root is again

\[
R\equiv132{,}013{,}085\pmod N,
\qquad
(\gcd(R-1,N),\gcd(R+1,N))=(19{,}727,10{,}267).
\]

This strengthens the finite interpretation of P103: the successful decoder
amortizes many individually useless presentations. It does not show that a
similar circuit occurs for another input. In particular, the computation
does not separate a general feedback effect from a fixed-input
smoothness/shared-prime effect.

The final candidate, final hostile re-audit, proof-blind statement, and
proof-blind reconstruction have SHA-256 hashes
`b22c749489acb53338b6feed4cbec333b4cfdc92fba01e0a2544006526e768f5`,
`8ebf65e6657d9e813ea1c22228c81916714bde753c1f9a979909b1ad62d992f1`,
`1235cbf1c34eb47502286e4607337d9f43392853847bddb8711c0ad05072c82f`,
and
`3a3ef8d468fafe113a3b801b7ca933d68b303b098a064f51a2da091cdf10cfa4`.
Both failed audits remain in the F100 directory. No cross-family audit,
human audit, or publication-level literature review has run.

## P106 — factor-free gcd refinement exposes the exact hidden-prime parity core

**Status:** promoted from corrected F105 after a hostile audit, an exact
wording correction, a fresh narrow re-audit, and the independent F103
proof-blind reconstruction. This is a decoder theorem for a frozen explicit
batch. It is not a source theorem or an all-input factoring algorithm.

Let the explicit endpoint batch consist of integer-mask pairs

\[
(a_i,m_i),\qquad a_i>1,\quad m_i\in\mathbb F_2^s.
\]

For every prime \(p\), define the unavailable prime-parity row

\[
r_p=\sum_i(v_p(a_i)\bmod2)m_i.
\]

The public P66 refinement selects two entries \((x,u),(y,v)\) with
\(d=\gcd(x,y)>1\), and replaces them by the nontrivial, nonzero-mask entries

\[
(d,u+v),\qquad(x/d,u),\qquad(y/d,v).
\]

For \(\alpha=v_p(x)\), \(\beta=v_p(y)\), and
\(\gamma=\min(\alpha,\beta)\), the new contribution is

\[
\gamma(u+v)+(\alpha-\gamma)u+(\beta-\gamma)v
=\alpha u+\beta v
\quad\text{over }\mathbb F_2.
\]

Thus every hidden prime row is invariant. Each eligible split strictly
decreases the sum of the prime-factor counts with multiplicity, so every
schedule terminates. At termination the integer blocks are pairwise
coprime. A hidden nonzero row is then exactly the mask of its unique block
with odd prime valuation. Conversely, every nonsquare terminal block has an
odd-valuation prime. Therefore the public nonsquare-block rows and the hidden
prime rows have the same set of distinct nonzero masks. They can differ only
by duplicate nonzero rows and, if retained, hidden zero rows.

Consequently the public and hidden matrices have exactly the same rank,
kernel, degree-one relation core, and column-incidence components. No
factorization of the endpoint values is needed.

Degree-one peeling is lossless on the frozen matrix. If a row has one active
column, that coordinate is zero in every kernel vector. Deleting the column
preserves the full kernel by zero extension. Every exhaustive peeling order
leaves the same unique greatest column set in which no incident row has
degree one.

This is not a safe permanent online deletion rule. A later relation can reuse
a row that is private in the current prefix and create a new dependency.

The fixed public F103 replay illustrates the theorem. Its 9,414 distinct
relation values have rank 8,926 and nullity 488. Public peeling removes 7,633
columns and leaves a connected core with 1,781 columns, 1,298 public rows,
rank 1,293, and the same nullity 488. The factor-assisted prime matrix has
1,299 core rows but exactly the same core columns. The public 166-value
factor certificate lies inside this core. A frozen 4,293-column prefix has
rank 4,291; peeling leaves 373 columns and rank 371. Thus column surplus is
not necessary for a finite rank defect.

The theorem makes the decoder side complete. It does not make a core
nonempty or rank deficient, and it does not make a square root non-global.
The remaining problem is entirely source-side: force a polynomial-size core
with a dependency whose normalized root is not globally \(\pm1\).

The corrected theorem candidate, final hostile re-audit, proof-blind
statement, and proof-blind reconstruction report have SHA-256 hashes
`ffcc2334acb34619ea2308ec9c544fbb1d0ecce4c696f9ce01c3caf9bbb53f45`,
`69868b43e9e10bf1fad7f981ad06406db0a635b6d919c986ffd44032a2193430`,
`85a3cc9997df45cec233741e41099e2eddf94ba0c5ef18a82aeb81cf8073cc74`,
and
`2aa63a861a050da79adba855bf29000db77e99654fc066ee193186ae0e9ecb49`.
The first audit's implementation failure and wording caveats remain
preserved. No cross-family audit, human audit, or publication-level
literature review has run.

## P107 — carry-exposed parity rows are exactly computable without factoring

**Status:** promoted from corrected F108 after a hostile audit, a fresh narrow
re-audit, a proof-blind reconstruction, and an amended-boundary proof-blind
re-audit. This is a public diagnostic theorem for a frozen explicit batch. It
is not a source theorem or an all-input factoring algorithm.

Let factor-free gcd refinement turn a frozen endpoint batch into pairwise
coprime integer-mask blocks \((q_j,m_j)\). Let \(E\) be the product of any
explicit public exposure list. Define \(S_E(q_j)\) as the largest divisor of
\(q_j\) supported on primes dividing \(E\). Repeated gcd and exact division
compute it without identifying a prime. If \(r_p\) is the hidden parity row
for prime \(p\), then

\[
\{m_j:S_E(q_j)\text{ is nonsquare}\}
=
\{r_p:p\mid E,\ r_p\ne0\}
\]

as sets of distinct masks. The proof combines the P106 row invariant with
gcd saturation: a terminal block contains the complete \(p\)-power in its
supported part exactly when \(p\mid E\). The computation is polynomial in the
total explicit endpoint and exposure-list bit length. It is polynomial in
\(\log N\) when those lists have polynomial size and polynomial-bit entries.

For the public 166-column F98 circuit at \(N=202{,}537{,}109\), all 54 raw
round-one trajectories give 15,935 exposure insertions after 6,008 two-zero
duplicates are excluded. The theorem recovers 200 distinct public masks of
rank 165, equal to the full circuit rank. The eight represented trajectories
already give 191 masks of rank 165. These are raw full-batch exposures. If
both adjacent values must lie inside the selected 166 columns, only 34 or 82
exposure events remain, and their rank is 54. Raw exposure is therefore a
reservoir property, not an internal-circuit carry explanation.

The F99 private-row family gives an exact boundary. Every transition has one
zero carry and exposes only powers of two, while distinct private primes form
an identity submatrix of rank \(T\). Carry frequency alone forces neither a
dependency nor the mixed CRT signs needed for a non-global root.

This theorem makes carry coverage public and testable. It does not prove that
the source covers the full row space on another input, that a dependency
exists, or that a dependency root is non-global.

The corrected result, final hostile re-audit, amended proof-blind statement,
original proof-blind report, and amended-boundary proof-blind re-audit have
SHA-256 hashes
`739e23ee12a251bb2f4a4cdbe0df3cebfa8cdf6fe6b2e12fcaca5bb513677eae`,
`6e17edd24681e003a894943a6e6f37975d2cc1fb8b8d66f87cc54d4804c48a0f`,
`9100aa6c2e0e3b9ce42c00b2888d87b41c6f0a43cac2026cd31c1aa2409fd722`,
`d2f3c31138834cbd521545715f13775c5f315329e5d73ba29ca5cd99aae225a3`,
and
`6d667a98dc565bba20d356ece41dc81bcc0f1ff1adb40bd6506b49faa50d3a03`.
The original under-specified statement failure and both hostile-audit
environment failures remain preserved. No cross-family audit, human audit,
or publication-level literature review has run.

## P108 — two individually useless relation layers can create a useful root only through their cross quotient

**Status:** promoted from F111 after a hostile factor-free layer-interaction
audit and an independent proof-blind reconstruction. This is an exact linear
algebra theorem and one fixed-input mechanism witness. It is not an all-input
source law or a factoring algorithm for arbitrary integers.

Apply one global first-occurrence exact-value deduplication to two ordered
relation layers. Let $M_F$ contain the first layer's columns, and let $M_A$
contain only second-layer values that are new relative to the first layer.
Put

\[
M_U=[M_F\;M_A].
\]

Write $K_F,K_A,K_U$ for their kernels. The map

\[
(x,y)\longmapsto M_Fx=M_Ay
\]

induces an exact isomorphism

\[
\boxed{
K_U/(K_F\oplus K_A)
\simeq
\operatorname{im}M_F\cap\operatorname{im}M_A.
}
\]

Consequently,

\[
\dim K_U-\dim K_F-\dim K_A
=
\operatorname{rank}M_F+
\operatorname{rank}M_A-
\operatorname{rank}M_U.
\]

This quotient measures dependencies that require both layers. It is separate
from raw nullity. For any exact square dependency, take its positive integer
root modulo $N$, then quotient the root image by the two global roots
\(\{+1,-1\}\). If the normalized root map is zero on both pure kernels but
nonzero on the displayed quotient, every useful dependency crosses the layer
boundary.

The factor-free F111 replay realizes this event at

\[
N=3{,}241{,}632{,}473.
\]

After first-occurrence exact-value deduplication, the frozen layer has

\[
11{,}885\text{ columns},\quad
\operatorname{rank}=11{,}878,\quad
\dim K_F=7.
\]

All seven basis roots are global $+1$. When decoded in isolation, the
appended source has 837 distinct exact values, rank 837, and no dependency.
Of these values, 153 already occur in the frozen layer. The global
first-occurrence rule therefore gives $M_A$ 684 new columns, which are also
independent by themselves. The complete union has

\[
12{,}569\text{ columns},\quad
\operatorname{rank}=12{,}551,\quad
\dim K_U=18.
\]

Hence the cross quotient has dimension

\[
18-7-0
=11{,}878+684-12{,}551
=11.
\]

Its normalized root-map image has rank one. Thus neither layer supplies a
useful root, while their union does. Every useful union dependency necessarily
uses both layers.

The hostile verifier found a 363-value cross-layer dependency. A separate
proof-blind decoder, which did not read that support or any layer-audit
artifact, independently found a different 367-value dependency. Both give

\[
R\equiv1{,}058{,}780{,}986\pmod N,
\qquad R^2\equiv1\pmod N,
\]

and

\[
\gcd(R-1,N)=79{,}043,
\qquad
\gcd(R+1,N)=41{,}011.
\]

All direct endpoint screens before the joint decode are nonproper. Both
decoders use gcd refinement, exact division, perfect-power extraction, exact
integer square roots, and binary linear algebra. They do not factor an
endpoint, call a primality routine, read a known factor, or read the published
dependency indices.

This is a real stateful algorithmic distinction from computing one new scalar
and taking one gcd. The new layer changes the accessible normalized-root
image only through its interaction with retained old relations. It does not
show growth of the abstract unit group. It also gives no reason that the
cross intersection or its non-global root image must be nonzero on another
input.

The hostile layer audit, its machine output, the proof-blind statement, and
the proof-blind reconstruction report have SHA-256 hashes
`6133c966d6e14e966314dd43360998289102507d1cb144f5f9a29d158310d95e`,
`6b9c66ca97c47d1307212db9ba5fa299df3c66c3312af6ee8f110c9d3e8e52a8`,
`a4c50da4ba3d76d2137115bdd423b5738b35f14d13dc6b1fed1d76c9f54627e6`,
and
`820ef26300e9de99fdce93dd551665621f460d81b79e49f17b6b39a482ce7f35`.
One hostile-verifier self-check failure and the proof-blind command-format
errors remain preserved. No cross-family audit, human audit, or
publication-level literature review has run.

## P109 — exact-value extension preserves useful roots, so a complete fixed source needs no certificate stop

**Status:** promoted from F111 after a hostile monotone-extension audit and an
isolated proof-blind full-source reconstruction. This is one general extension
theorem and one fixed-input polynomial-time computation. It is not an
all-input source law.

Let an ordered source produce positive exact relation values
$P_i\equiv1\pmod N$. Remove $P_i=1$, and keep only the first occurrence of
each exact integer value. Appending source records leaves every old coordinate in place.
Thus an old kernel vector extends by zeros on the new coordinates. Its exact
selected product, positive square root, and normalized root class do not
change.

The normalized root map from the binary square-class kernel to the square
roots of one modulo $N$, modulo global sign, is a homomorphism. Therefore, if
its image is nonzero, every complete kernel basis contains at least one vector
with nonzero normalized class. The theorem preserves the useful image, not a
particular basis vector.

For

\[
N=3{,}241{,}632{,}473,
\]

an isolated decoder executed the full fixed source from only $N$, $n=32$,
and $B=n^2=1024$. It used seeds $2,\ldots,n$, every frozen seed-basis
trajectory, then the constant pairs $(2,3)$ and $(2,4)$. It used
no retained-record stop, dependency support, known divisor, endpoint
factorization, or primality routine.

The source attempted 67,681 positions and retained 15,884 first residues. The
$(2,3)$ append added no new residue. The $(2,4)$ append added 1,533. Global
exact-value deduplication left 12,962 columns. Factor-free refinement and a
complete binary decode gave

\[
\operatorname{rank}=12{,}923,
\qquad
\operatorname{nullity}=39.
\]

All 39 basis products were tested by exact integer square root and terminal
gcd. Twenty-three roots were global $+1$, five were global $-1$, and eleven
had nonzero normalized class. The useful roots exposed the proper divisors
$41{,}011$ and $79{,}043$. No earlier direct sign screen gave a proper
divisor.

The full program has $O(n^3)$ source positions. Its relation values,
factor-free refinement state, binary matrix, dependency products, complete
kernel basis, and every root test have polynomial bit size. It is therefore a
uniform polynomial-bit-time computation. The pair choices are now constant
program text, but they were historically selected after experiments. Nothing
here proves that this fixed source has a useful root on another input.

The hostile audit report and output, proof-blind statement, reconstruction
report and output, and final reconstruction manifest have SHA-256 hashes
`55bdaf32d841a47a5ad8ce4cb422eb80c4bb0d0bc6991699fd8eff50f3ab7b95`,
`f629bc58e14d3a21877f8642145ac6bab3ef1cf8d85a4589ba321eb219763095`,
`1cdea0d4292e3f80a54551a3cc5f4c1160cfdf4af2e4ed6a110f35fbeef8936b`,
`138a41f1506ae5a4261e0b390d731f7413efc9232fe366bfedad577f04f9735c`,
`94f3550d27f2a5d6101b648c4e8432a7fb2e6ed9cdb1e12ad5695b70938dd4fd`,
and
`b6b0114948dc125a07d228d956b4434662550f522622f459bfc103c9b210b83b`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P110 — the complete all-seed-pair source is a no-advice polynomial algorithm on one fresh 54-bit input

**Status:** promoted from F116 after a hostile exact-value audit and an
isolated proof-blind reconstruction. This is a fixed-input success theorem. It
does not give an all-input source law.

For

\[
N=12{,}800{,}004{,}879{,}996{,}637,
\]

set $n=54$ and $B=n^2=2916$. The fixed source tries seeds $2,\ldots,n$,
all frozen seed-basis trajectories, and then both orientations of every
unordered seed pair $2\leq u<v\leq n$ through exponent $B$. It keeps the
first occurrence of each residue and the first occurrence of each nonunit
exact relation value. It then uses the complete factor-free square-class
decoder and tests every vector in a complete kernel basis.

This complete algorithm receives only $N$. It receives no retained-record
stop, dependency support, known divisor, endpoint factorization, or primality
advice. Its source has exactly

\[
(n-1)+(B+1)n(n-1)=8{,}348{,}507
\]

positions, and its complete decoder has polynomial bit cost.

The isolated reconstruction regenerated an initial prefix of 1,336,218 source
positions. It retained 771,082 first residues. Global exact-value projection
left 622,151 distinct nonunit columns. An advised set of 6,486 regenerated
records consists entirely of distinct nonunit exact values at their global
first occurrences. Their 672,808-bit exact product is a square. Its positive
root satisfies

\[
R\equiv5{,}266{,}287{,}723{,}884{,}331\pmod N,
\qquad R^2\equiv1\pmod N,
\]

and

\[
\gcd(R-1,N)=159{,}999{,}943,
\qquad
\gcd(R+1,N)=80{,}000{,}059.
\]

No direct sign screen in the prefix gives a proper divisor. Exact-value
projection preserves this nonzero normalized root class. P109 append
monotonicity then extends it through the unexecuted remainder of the fixed
source. The factor-free decoder theorem and root-map homomorphism imply that
every complete kernel basis for the final source contains at least one useful
vector. Therefore the specified no-advice algorithm factors this supplied
$N$.

The complete 8,348,507-position source and its complete decoder were not run.
The advised prefix and support are proof data, not algorithm inputs. Nothing
here proves success on another input, a success density, an inverse-polynomial
probability, or a classical polynomial-time factoring algorithm for arbitrary
integers.

The hostile audit report and output, proof-blind statement, reconstruction
report and output, and final manifest have SHA-256 hashes
`020b8cc8c9c8c15fb9a42186496ffb20e7302519ffa5ec2319c24ae62b9c1cd6`,
`e25bbbeb6453230753ea569bba8d9b2d2dc97b59088c37988056c4472768cab4`,
`dacb0f606313045ce3f0e7b6ff75433bad437ac2b372056f71a021cfce5dce1b`,
`8e64015edf3dbd2df9002edbed7c81324d88ea8decc91cf114f9d06527e8e34f`,
`0c1fdcbf734592fee9b9f7722816f5cbfbee6f00d53bc8a6fa1fc8d8b8fb0ca1`,
and
`996639d418ca78603f4af384c8328596dd59d72c5701020d855757243c06a745`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P111 — carry congruences admit an infinite trial-hard cross-pair private-row submatrix

**Status:** promoted from F119 after a hostile audit found one endpoint-scope
error, the theorem was corrected, the corrected bytes passed a fresh
re-audit, and a proof-blind agent reconstructed the theorem by a different
CRT construction. This is an infinite selected-submatrix theorem. It is not
a complete-source obstruction or a factoring algorithm.

For a unit $1\leq c<N$, let $w$ be its least positive inverse and write

\[
P_N(c)=cw=1+\kappa_N(c)N.
\]

For distinct nonzero carries $k,\ell$,

\[
\gcd(1+kN,1+\ell N)
=\gcd(1+kN,|k-\ell|)
=\gcd(1+\ell N,|k-\ell|).
\]

Indeed, every $1+kN$ is coprime to $N$, so subtraction removes the factor
$N$. Consequently, for every prime $r\nmid N$,

\[
r\mid1+kN
\quad\Longleftrightarrow\quad
k\equiv-N^{-1}\pmod r.
\]

Thus a prime row can occur only in one carry residue class. If a finite carry
set has diameter $D$, row $r$ has degree at most
$1+\lfloor D/r\rfloor$. If column $k$ has no private odd-valuation row, then

\[
\operatorname{sf}(1+kN)
\mid
\prod_{\ell\ne k}|k-\ell|,
\]

where $\operatorname{sf}$ is the product of primes with odd valuation.

The following construction shows that genuine cross-pair provenance does not
itself force row reuse. For sufficiently large $t$, choose $t$ primes
$a\in(t^2,2t^2)$ and set

\[
C_t=\{a^2b:a\ne b\},
\qquad |C_t|=t(t-1),
\qquad L_t=\prod_a a^2.
\]

The values in $C_t$ are distinct and divide $L_t$. For each $c\in C_t$,
choose a distinct prime $q_c\in(t^{10},2t^{10})$ and put $d_c=c-1$. Let

\[
Q_t=L_t\prod_{c\in C_t}q_c^2.
\]

CRT gives a reduced class $R_t\pmod {Q_t}$ with

\[
R_t\equiv1\pmod {L_t},
\qquad
R_t\equiv(q_c-1)d_c^{-1}\pmod {q_c^2}
\quad(c\in C_t).
\]

Choose a prime $p_t$ with $Q_t<p_t<2Q_t$. Choose a reduced representative
between $2Q_t$ and $5Q_t$ for the required class modulo $Q_t$. Dirichlet's
theorem and Linnik's theorem then give a distinct prime $\ell_t>2Q_t$ of size
$Q_t^{O(1)}$ such that

\[
p_t\ell_t\equiv R_t\pmod {Q_t}.
\]

Set $N_t=p_t\ell_t$. Then $N_t\equiv1\pmod c$ for every $c\in C_t$, so

\[
w_c=N_t-\frac{N_t-1}{c}
\]

is the canonical inverse of $c$, and

\[
P_{N_t}(c)=cw_c=1+(c-1)N_t.
\]

The protecting congruence gives

\[
P_{N_t}(c)\equiv q_c\pmod {q_c^2},
\]

so $q_c$ has valuation one in this value. For $d\in C_t$, $d\ne c$,

\[
P_{N_t}(d)
\equiv(c-d)(c-1)^{-1}\not\equiv0\pmod {q_c},
\]

because $q_c$ exceeds every selected word difference. The $q_c$ rows
therefore form an identity submatrix. All $t(t-1)$ selected square-class
columns are independent.

Moreover,

\[
\log Q_t=\Theta(t^2\log t),
\qquad
n_t=\operatorname{bitlength}(N_t)=\Theta(t^2\log t).
\]

Hence

\[
t(t-1)=\Theta(n_t/\log n_t).
\]

For large $t$, every base is at most $n_t$, exponent two is inside the
declared $n_t^2$ range, and every $c<N_t$. Thus these are genuine words in
the fixed unordered-seed-pair menu. Both factors exceed $n_t^2$, so the
inputs are trial-hard distinct semiprimes and not perfect powers.

For each named residue $c$, both endpoint sign gcds are one. A proper sign
gcd modulo a factor $s$ would force $c^2\equiv1$ or $-1\pmod s$, while
$0<c^2-1<c^2+1<Q_t<s$. This also covers an earlier occurrence of the same
canonical residue. It does not cover a different earlier residue that has
the same exact integer value. Exact-value deduplication preserves the value
and its private row, but sign screens depend on the endpoint representation.

The construction controls privacy only inside the selected submatrix. A
seed, frozen, or other all-pairs carry can be congruent to $c-1\pmod {q_c}$
and reuse the row. It also does not exclude an earlier direct factor. A
complete-source obstruction still needs stable privacy for the final
self-generated carry set. A positive factoring theorem instead needs both a
rank defect and a non-global normalized root. These are three separate
conditions.

The corrected result, final hostile re-audit, proof-blind statement,
reconstruction proof and report, reconstruction manifest, and final re-audit
manifest have SHA-256 hashes
`552a54c8382341709305e53bd535efd9ef0ec0bc7957fa32be8ddc5c061f4575`,
`a629dc043d915caaf9ac1240b018f5c72014849f89bf31969a57c992121cf6ae`,
`4a4aaf43119609e7745b5f88623a3ea9fb3c72aac7d15b16062d1aef0e692986`,
`e8aa7a5f4c10bb24d99b766b1fe774912d939e9db16f565de035d92d4442db46`,
`5f9c9dae4ff42ad4c8685dcd3c0a39a95931c792f0fe8973b9b79749450ba5ef`,
`f60e3e3bc9923df29145c4d9e831a6ea8888af237f73ff76bee27a4f91426d82`,
and
`3379c8903638149795cd0bc8baeebe7de6ae4732d23891821fa7e09826aa5b30`.
The original overbroad result hash retains `PASS_WITH_CORRECTIONS`. No
cross-family audit, human audit, or publication-level literature review has
run.

## P112 — canonical prime rows obey a complete-universe degree bound

**Status:** promoted from F120 after a fresh hostile audit passed and a
proof-blind reconstruction passed with two wording corrections. The modular
inverse formula below is stated only for $c\ge2$, and the three algorithmic
gates are stated as exact matrix properties. This is a row-reuse theorem and
one finite counterexample. It is not a factoring obstruction.

Let $N\ge3$ be odd. For each unit $1\le c<N$, let $w(c)$ be its least
positive inverse and set

\[
P_N(c)=c\,w(c)=1+\kappa_N(c)N.
\]

Let the columns be the distinct integer values $P_N(c)>1$, after global
exact-value deduplication. For a prime $r$, put a one in a column when its
$r$-adic valuation is odd. Then

\[
\deg(r)\le
\left\lfloor\frac{N-1}{r}\right\rfloor.
\]

For each distinct column containing $r$, choose one endpoint divisible by
$r$. Two different exact values cannot choose the same endpoint, because
that endpoint has a unique inverse modulo $N$. The chosen endpoints are
distinct positive multiples of $r$ below $N$, which proves the bound.
Different inverse orbits can share one exact product; global exact-value
deduplication is therefore essential.

Consequently, every present row with $r>(N-1)/2$ has degree one in the
complete canonical universe. It remains private under every fixed-modulus
source extension inside that universe. The exact carry also satisfies

\[
0\le\kappa_N(c)<\min(c,w(c)),
\qquad
\kappa_N(c)\equiv-N^{-1}\pmod c
\quad(c\ge2).
\]

At $c=1$, the carry is zero; no inverse modulo one is used.

There is a proof-certified trial-hard distinct semiprime witness:

\[
N=2{,}000{,}887{,}089{,}301
=1{,}000{,}289\cdot2{,}000{,}309.
\]

Here

\[
r=(N+1)/2=1{,}000{,}443{,}544{,}651
\]

is prime. Seed $2$ has least inverse $r$, exact value $N+1=2r$, and
odd $r$-valuation. Since $r>(N-1)/2$, this row is private against every
canonical exact-value column. Both endpoint sign gcds are one. The two
factors of $N$ exceed $41^2$, and $N$ is not a perfect power.

If a row is private, its unique column has coefficient zero in every binary
dependency. Deleting that row and column gives a coordinate-preserving kernel
bijection. It preserves every positive exact root and its residue modulo
$N$ on the surviving columns. Thus the finite witness refutes the universal
claim that every present row must be reused. It does not decide whether the
remaining columns contain a dependency or whether any dependency has a
non-global square root. It also does not rule out feedback that exposes a new
named integer representation of an existing exact value.

The candidate result, fresh hostile report, blind reconstruction proof, and
blind reconstruction report have SHA-256 hashes
`a8a63cc9a2bfab6acea2ded42e851fe3d6a185e15f9962bbe802a0ecb1866445`,
`862f30200ccef7491e16bd366b69dea67f1e438caeb5b7b8698edd47d91f338a`,
`ab367ec8a2853b365e881b88bd4dc1dc2adf1e0ba6d226755934651b5433a56f`,
and
`4f6008ca54c4bf4efa4b8a2fa849b85c78eeaf467047898eaee701820a41b952`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P114 — multiplicative rectangles give an exact canonical-carry rank-mismatch screen

**Status:** promoted after a hostile audit and an independent proof-blind
reconstruction. This is a deterministic quasipolynomial decoder extension.
It is not an all-input source theorem.

Let \(u,\alpha,\beta\) be units modulo \(N\). For
\(i,j\in\{0,1\}\), define

\[
x_{ij}=[u\alpha^i\beta^j]_N,
\qquad
y_{ij}=[x_{ij}^{-1}]_N,
\qquad
\kappa_{ij}={x_{ij}y_{ij}-1\over N}.
\]

Order the rows \((1,x_{ij},y_{ij},\kappa_{ij})\) as \(00,10,01,11\), and
call the matrix \(L\). Put

\[
\Omega_{\square}
=(\beta-\alpha)(\kappa_{11}-\kappa_{00})
+(\alpha\beta-1)(\kappa_{10}-\kappa_{01}).
\]

If

\[
\gcd(\alpha\beta(\alpha-1)(\beta-1)(\beta-\alpha),N)=1,
\]

then

\[
\boxed{
\det L\equiv
{(\alpha-1)(\beta-1)\over\alpha\beta}
\Omega_{\square}\pmod N,
}
\]

and

\[
\boxed{
\gcd(\det L,N)=\gcd(\Omega_{\square},N).
}
\]

### Proof

Write \(d=\beta-\alpha\) and \(e=\alpha\beta-1\). Form

\[
S=-dR_{00}+eR_{10}-eR_{01}+dR_{11}.
\]

Modulo \(N\), its first column is zero. Its second column is

\[
u[-d+e\alpha-e\beta+d\alpha\beta]=0.
\]

After multiplication by the unit \(u\alpha\beta\), its third column is

\[
-d\alpha\beta+e\beta-e\alpha+d=0.
\]

Its fourth column is \(\Omega_{\square}\). Replacing the last row by \(S\)
multiplies the determinant by \(d\). Expansion along that row gives

\[
d\det L\equiv\Omega_{\square}D\pmod N,
\]

where

\[
D=
\det
\begin{pmatrix}
1&u&u^{-1}\\
1&u\alpha&(u\alpha)^{-1}\\
1&u\beta&(u\beta)^{-1}
\end{pmatrix}
={(\alpha-1)(\beta-1)(\beta-\alpha)\over\alpha\beta}.
\]

The last equality is the three-point Vandermonde determinant after the two
column scales cancel. Cancel the unit \(d\). The remaining multiplier is a
unit, which proves both claims.

For \(u=\alpha=t\) and \(\beta=[t^2]_N\), the four vertices are the
canonical residues of \(t,t^2,t^3,t^4\), and

\[
\Omega_{\square}\equiv
t(t-1)
\left[
\kappa_4-\kappa_1+(1+t+t^{-1})(\kappa_2-\kappa_3)
\right]
\pmod N.
\]

The bracket is the F123 residual. Thus F123 is the consecutive-power slice
of P114.

If the F26-Q menu has \(Q=2^{O((\log n)^2)}\) canonical residues, scanning
every ordered triple \((u,\alpha,\beta)\), constructing its four corners,
and testing \(\Omega_{\square}\) costs at most \(Q^3\operatorname{poly}(n)\),
which is quasipolynomial. Prefactor components must be screened separately;
a proper gcd is already a factor. The rectangle scan runs before P66
exact-value deduplication and retains \(P=1\) vertices.

P114 gives a real cross-word decoder. It has no theorem that any rectangle
has rank three in one hidden CRT component and rank four in another. Since
\(Q^3=N^{o(1)}\), menu counting alone cannot supply that law. A
feedback-specific result still needs a successful rectangle that essentially
uses a feedback-created block.

The statement, proof, hostile audit, and proof-blind reconstruction have
SHA-256 hashes
`e9e366887297e260c196e040c9d5a7cdf01a4c8ca63f7d2e246405eeba9e6e9c`,
`edff10c753a903808ad8fe0c3954f1135dd3a4aa8b739b3f8c47458a57fb486b`,
`c8e52e3eef9d49610f1fc083ddf10b5836f28d76d0ece6730cf538f0593ebecb`,
and
`f6db5ad782683fc019632632b0699d34bdfc46cbb979adcc0101ea0ca10a0027`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P116 — wrapped rectangle information is exactly floor curvature

**Status:** promoted from F128 after a hostile audit and a fresh
proof-blind reconstruction of the corrected self-contained statement. This
is an exact P114 structure theorem and source obstruction. It is not an
all-input rank-mismatch law or a factoring algorithm.

Let \(N\) be odd, and let \(u,a,b\) be canonical unit representatives. Put

\[
d=b-a,
\qquad e=ab-1,
\]

and define the four P114 corners

\[
x_{ij}=[ua^ib^j]_N,
\qquad
y_{ij}=[x_{ij}^{-1}]_N,
\qquad
\kappa_{ij}={x_{ij}y_{ij}-1\over N}.
\]

Let

\[
M=uab,
\qquad z=[M^{-1}]_N,
\qquad K={Mz-1\over N},
\]

and define the six public floor quotients

\[
A=\left\lfloor{ua\over N}\right\rfloor,
\quad
B=\left\lfloor{ub\over N}\right\rfloor,
\quad
C=\left\lfloor{uab\over N}\right\rfloor,
\]

\[
R_0=\left\lfloor{zab\over N}\right\rfloor,
\quad
R_a=\left\lfloor{zb\over N}\right\rfloor,
\quad
R_b=\left\lfloor{za\over N}\right\rfloor.
\]

Before reduction, every corner product is the same integer \(Mz=1+NK\).
Expanding the four reductions gives

\[
\boxed{
\Omega_{\square}
=Ne(AR_a-BR_b)+u\Phi_y+z\Phi_x,
}
\]

where

\[
\Phi_x=e(aB-bA)-dC,
\qquad
\Phi_y=dR_0+e(bR_b-aR_a).
\]

Therefore

\[
\boxed{
\gcd(\Omega_{\square},N)
=\gcd(u\Phi_y+z\Phi_x,N).
}
\]

Under the P114 unit conditions, the first three columns of the local matrix
\((1,x,y,\kappa)\) have rank three modulo every prime divisor \(\ell\) of
\(N\). Reduction raises the rank to four exactly when

\[
u\Phi_y+z\Phi_x\not\equiv0\pmod\ell.
\]

Thus the unreduced common-product rank defect contains no factoring
information by itself. Only the two floor-curvature terms can create a local
rank mismatch.

There is also an exact density boundary. Let \(N=pq\), with \(p<q\) odd
primes, fix \(a,b\), and draw \(u\) uniformly from the unit group. The six
floor quotients have at most \(a^4b^4\) joint patterns. On a fixed pattern,
multiplication by \(uab\) gives the quadratic congruence

\[
ab\Phi_yu^2+\Phi_x\equiv0\pmod p.
\]

If

\[
p>(ab)^2(ab+\max(a,b)),
\]

each non-global pattern has at most two roots modulo either hidden prime.
Consequently,

\[
\boxed{
\Pr_u(1<\gcd(\Omega_{\square},N)<N)
\le
{2a^4b^4(p+q)\over(p-1)(q-1)}
=O\!\left({a^4b^4\over p}\right).
}
\]

This is only a uniform-source theorem. It does not constrain an adaptive
selector that observes earlier carries or relations.

Canonical magnitude can also be misleading. Suppose the three inputs have
signed-small representatives

\[
u\equiv\epsilon_0s,
\quad a\equiv\epsilon_aa_0,
\quad b\equiv\epsilon_bb_0\pmod N,
\]

and put \(L=sa_0b_0<N\). Multiplication by \(L\) converts the curvature to
an explicit integer \(B_{\rm sign}\) satisfying

\[
\gcd(\Omega_{\square},N)=\gcd(B_{\rm sign},N),
\]

\[
\boxed{
|B_{\rm sign}|
<6L^2(a_0+b_0+a_0b_0+1).
}
\]

When both hidden primes exceed the displayed bound, the curvature,
eligibility factors, and all eight endpoint signs are null or global. A
canonical representative near \(N\) therefore does not escape the metric
obstruction when it has a small signed representative.

Finally, visible wrapping itself gives no success law. Fix \(s,a,b>1\),
\(a\ne b\), put \(L=sab\), and take

\[
u=N-s,
\qquad N\equiv-1\pmod L.
\]

All three nontrivial products wrap, but the weights cancel the constant,
linear, and reciprocal terms exactly:

\[
\boxed{\Omega_{\square}=0.}
\]

Comparable primes in the classes \(1\) and \(-1\pmod L\) give infinitely
many balanced semiprimes with this behavior and with all named side screens
nonproper. At the boundary \(s=1\), the exact residual is instead

\[
\boxed{
\Omega_{\square}=(b-a)(1-N),
}

whose gcd is one under eligibility.

P116 moves the surviving P114 target into rectangles with genuinely large
least-signed multipliers and nontrivial floor curvature. It does not prove
that this tail has inverse-quasipolynomial mass or that an adaptive rule can
find its rare local mismatches. It also does not address retained P66
relations.

The statement, proof, hostile audit, and final proof-blind reconstruction
have SHA-256 hashes
`bf7b1a10feb6bc22061ac6e4f1744ce86819b3c4d0fcdaf99db9daf731c0c06b`,
`e3dd1a72ac5cb2079d7d880a2d3ae19d4798788dc2164e472004ca7cc264987d`,
`834c0a23d67c9f161c2c36e23dd90e36dff140b4682871ebfd0e0ab458301713`,
and
`106902091f4a081a472efed08b1e544519692dfc763e82c0996caeee280ebf4c`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P119 — two-column closure has one exact small-kernel global-root trap

**Status:** promoted from corrected F131 after a fresh hostile re-audit and
an independent proof-blind reconstruction. The first under-specified version
and its counterexample remain preserved. This is an exact root-label theorem
and an auxiliary counterexample. It is not a complete-source null or a
factoring algorithm.

Let two distinct canonical exact values satisfy

\[
P_1P_2=R^2,qquad P_i\equiv1\pmod N.
\]

Their prime-valuation parities agree. Hence there is one squarefree (s)
and unique positive (a,b) such that

\[
P_1=sa^2,qquad P_2=sb^2,qquad R=sab.
\]

Canonical endpoints give (0<a,b<N/\sqrt s\). Since (sa^2\equiv1),

\[
R\equiv ba^{-1}\pmod N.
\]

Therefore

\[
R\equiv1\pmod N\iff a=b,
\qquad
R\equiv-1\pmod N\iff a+b=N.
\]

Distinct exact values exclude the first case. Thus a two-column dependency
has a global root exactly when (a+b=N), and that root is (-1). The metric
bounds then give

\[
N=a+b<{2N\over\sqrt s},
\]

so (s<4). Consequently,

\[
\boxed{
s\ge5\quad\Longrightarrow\quad R\not\equiv\pm1\pmod N.
}
\]

Only the common squarefree kernels (1,2,3) can hide a distinct two-column
dependency behind a global root. Endpoint sign screens do not remove this
trap.

The strict counterexample is

\[
N=9407=23\cdot409,
\]

with canonical endpoint pairs

\[
(9025,4802),qquad(6534,6912).
\]

Their exact values are

\[
2\cdot4655^2,qquad2\cdot4752^2.
\]

All four endpoint sign gcds are one, but their joint root is

\[
2\cdot4655\cdot4752=4703N-1.
\]

Thus both individual values are nonsquares and the joint root is global.

This is not a sporadic endpoint degeneracy. For

\[
t=373+mM,qquad N=t^2-2,
\]

with the explicit modulus

\[
M=6\cdot529\cdot119\cdot17\cdot4559\cdot5233,
\]

the proof constructs two such relations for every (m\ge0). Every input is
an odd nonsquarefree composite with (23^2\mid N), every endpoint screen has
gcd one, and the root is (-1\). The first member is

\[
139127=23^2\cdot263.
\]

The exact consequence for retained relations is positive and negative. A
weight-two parity closure usually resolves the root gate automatically: any
common squarefree kernel at least five is useful. But closure alone does not
remove the kernels (1,2,3). A complete algorithm must detect or escape
those antipodal metric pairs.

The statement, proof, failed first audit, passing hostile audit, and blind
reconstruction have SHA-256 hashes
`5d523c297f4304830fed3fec2b72b8ad476e27ab97e31bdac8e3d4ede303438c`,
`5f12d13d27a2586b1512beeb0332a5c54fabac78a92502ff8ac4e037ddb7a327`,
`193b559628788714a73c32bacedd60e658f8bb50349d04e4fe089dedb89206ff`,
`9e7c8f33cc97a516e9df7ee25c9247208a6b74b95445a7a5b3063192cd91015e`,
and
`5241c43d5e85b667c9bb4a39fd7ac8e67fb88600553594413f3dc8449b2c0925`.
F131-D01 independently checks the displayed finite arithmetic. No
cross-family audit, human audit, or publication-level literature review has
run.

## P120 — bounded all-block unary feedback remains quasipolynomial but does not force closure

**Status:** promoted from corrected F132 after a preserved failed hostile
audit, a fresh hostile re-audit, and an independent proof-blind
reconstruction. This is an exact cost and feedback-accounting theorem. It is
not a progress law or a factoring algorithm.

Put

\[
n=\lceil\log_2(N+1)\rceil,\quad
L=\lceil\log_2(n+1)\rceil,\quad
E=2^{L^2},\quad T=L^2.
\]

Start on the no-factor branch after the complete P118/F130 transcript. Refine
all accumulated endpoints into one pairwise-coprime all-block basis. In each
of \(T\) frozen rounds, and for every current block \(q\) and
\(1\le e\le E\), form

\[
c=[q^e]_N,\qquad w=\iota_N(c),\qquad P_N(c)=cw.
\]

Run both endpoint sign screens before exact-value deletion. Retain each first
exact value and every endpoint presentation. Batch-refine all endpoints only
after the round. Run the complete P66 decoder after the last round.

If \(\Lambda_t\) is the accumulated endpoint bit length and \(M_t\) the number of
blocks, then

\[
M_t\le\Lambda_t,
\qquad
\Lambda_{t+1}\le(1+2nE)\Lambda_t.
\]

The full P118 transcript has \(2^{O(L^4)}\) bits. Therefore the new source,
all refinements, and the final P66 decode have deterministic bit complexity

\[
\boxed{2^{O((\log n)^4)}}.
\]

This changes the source grammar. A cofactor that P118 keeps only in its
decoder basis can now become a named generator in a later round. The result
uses the fixed cap \(T=L^2\); it does not bound iteration to a fixed point.

The exponent-one branch has an exact law. If a current block \(q\) divides an
old value \(P_0=1+kN\) and \(q>k\), then

\[
\iota_N(q)=P_0/q,
\qquad
P_N(q)=P_0.
\]

Thus a new exact value requires \(q\le k\) for every old incident value. An
exact duplicate changes neither the refined basis nor the normalized-root
image, but its new endpoint presentation can still factor before deletion.
At

\[
N=63,
\]

the old value \(64\) has presentation \((8,8)\); feeding the exposed block
\(2\) gives the duplicate presentation \((2,32)\) and

\[
\gcd(2-32,63)=3.
\]

A new value need not reuse the fed prime rows. At

\[
N=253,
\]

the old value \(26\cdot146=2^2\cdot13\cdot73\) exposes \(q=13\), but

\[
13\cdot39=3\cdot13^2
\]

has zero parity in row \(13\). Conversely, real row reuse does not force a
2-core. At \(N=77\), the old and new parity supports are

\[
\{2,29\},\qquad\{2,3,13\}.
\]

Row \(2\) is reused, but the fresh private rows peel both columns.

More generally, let an old row \(r\) occur only in column \(v\), and append a
new column \(u\). After deleting row \(r\), write the residual columns as
\(\widehat v,\widehat u\) and all other old columns as \(\widehat M\). If
\(u_r=0\), a new dependency appears exactly when

\[
\widehat u\in\operatorname{colspan}(\widehat M).
\]

If \(u_r=1\), it appears exactly when

\[
\boxed{\widehat u+\widehat v\in
\operatorname{colspan}(\widehat M).}
\]

Row reuse contracts two columns; it does not close their other rows.

There is also an exact stable obstruction. Any odd prime

\[
r>{N-1\over2}
\]

can occur in at most one globally deduplicated canonical exact value. If its
valuation there is odd, its row remains degree one in the complete canonical
universe. No unary power schedule can reuse it.

P120 proves that bounded all-block feedback is a valid quasipolynomial
extension and that it can enlarge the later generator grammar. It also
separates three gates: creation of a new relation, reuse of an old row, and
closure after degree-one peeling. A successful route must still force a
closed dependency and a non-global normalized root.

The statement, proof, failed first audit, passing re-audit, blind
reconstruction, and final manifest have SHA-256 hashes
`41331f37531a2303dc7c372cbabe49110450b4b2e080800c842c62fb84d79a64`,
`da1d333a4dd87745013f56bd17fc04a06b08f29cd09258be65071ec77afae56b`,
`fdbf9cb7078a19b8287e6357e245a4ab2d98b559a47802aeba2ee150f8398e24`,
`a0e690209182053993e3b1b4634856dd7b5ef433c4db8de8f5cd97d7ded21938`,
`25f237a201152aad8e211a89b31887301ea02b8bf354d5700f1dc371f3ac7c80`,
and
`ad191d8285f5c13a5b7151dc468bfa9973c928f8da9d9e253b3c2afe25b206ff`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P121 — small-prime anchors force polynomial reuse of every covered large row

**Status:** promoted from F133 after an independent hostile audit and an
independent proof-blind reconstruction. This is an exact source-side progress
theorem. It is not a parity-closure theorem or a factoring algorithm.

For a unit \(c\in\{1,\ldots,N-1\}\), put

\[
\iota_N(c)=c^{-1}_{\mathrm{can}}\pmod N,
\qquad
P_N(c)=c\iota_N(c).
\]

Let \(B\ge2\), let \(1<q<N/B\) be a unit block, and put
\(w=\iota_N(q)\). For every eligible prime

\[
\ell\le B,\qquad \ell\nmid Nq,
\]

there is one carry digit \(A_\ell\in\{0,\ldots,\ell-1\}\) such that

\[
w+NA_\ell\equiv0\pmod\ell.
\]

Both endpoints are canonical integers:

\[
\ell q<N,\qquad
z_\ell={w+NA_\ell\over\ell}<N,
\]

and the exact anchored relation is

\[
\boxed{
\iota_N(\ell q)=z_\ell,\qquad
P_N(\ell q)=q(w+NA_\ell).
}
\]

Different carry digits give different exact values, and
\(A_\ell=0\) exactly when \(\ell\mid w\).

Now let \(r>B\) be prime with \(v_r(q)\) odd. Define

\[
G_B(N,q)=
\prod_{\substack{\ell\le B\ {\rm prime}\\ \ell\nmid Nq}}\ell.
\]

If

\[
\boxed{G_B(N,q)>N^2B,}
\]

then an eligible anchor has a nonzero digit with

\[
v_r(w+NA_\ell)\equiv0\pmod2.
\]

Thus its exact value is distinct from \(P_N(q)\) and has odd \(r\)-adic
valuation.

The proof is a carry-bucket argument. The zero-digit prime product divides
\(w<N\). For any fixed nonzero digit \(A\), its prime product divides
\(w+NA<NB\). Since \(r>B\), at most one observed digit can have positive
odd \(r\)-valuation. If no good nonzero digit existed, all eligible primes
would fit in the zero bucket and one bad bucket, contradicting
\(G_B(N,q)>N^2B\).

Processing the unary value and the full anchor bank gives a stronger
deduplication-safe conclusion:

\[
\boxed{\deg(r)\ge2}
\]

in the globally deduplicated parity matrix. If the unary value is already odd
in row \(r\), one distinct good anchor supplies the second column. If it is
even because \(r\) divides \(w\) oddly, the product bound forces two distinct
nonzero good digits. An earlier ledger cannot erase this result: a duplicate
value is already present, and different digits give different exact integers.

There is an unconditional uniform cutoff. Put

\[
n=\lceil\log_2(N+1)\rceil,\qquad B_0=n^3.
\]

For every \(n\ge64\) and every unit block \(q<N/n^3\),

\[
\boxed{G_{n^3}(N,q)>N^2n^3.}
\]

An elementary central-binomial and least-common-multiple argument gives

\[
\prod_{\ell\le n^3\ {\rm prime}}\ell>N^4.
\]

The product of excluded primes divides \(\operatorname{rad}(Nq)\) and is
less than \(N^2/n^3\), which gives the displayed bound. No prime number
theorem is used.

Keeping the excess primorial mass gives the quantitative form. For each prime
\(r>n^3\) that occurs oddly in \(q<N/n^3\), either a declared gcd screen
already returns a factor, or the completed anchor scan leaves more than

\[
\boxed{{n^2\over4}}
\]

distinct exact values with odd \(r\)-valuation after global deduplication.
The audited bucket estimate is

\[
g>{48n^2-599\over179}>{n^2\over4}.
\]

This source operation fits the existing quasipolynomial algorithm. With

\[
L=\lceil\log_2(n+1)\rceil,\quad
E=2^{L^2},\quad T=L^2,
\]

scan every integer anchor \(1\le a\le\min(E,N-1)\) against every current
all-block generator in each frozen round. Keep all endpoint presentations
before exact-value deletion, then batch-refine. Since \(E\ge n^3\) for
\(n\ge64\), the source contains the full uniform prime subbank. The endpoint
recurrence from P120 remains

\[
\Lambda_{t+1}\le(1+2nE)\Lambda_t,
\]

so the full composition and final P66 decode cost

\[
\boxed{2^{O((\log n)^4)}}.
\]

P121 is the first general positive source theorem in this feedback route. It
proves that bare-\(N\) canonical carries can force polynomial multiplicity of
a hidden prime-parity row. It does not force those columns to survive
degree-one peeling: each can still carry a different fresh private row. It
does not cover \(q\ge N/n^3\), odd rows at primes at most \(n^3\), or large
primes occurring evenly in \(q\). It also does not force a non-global root.

The statement, proof, hostile audit, blind reconstruction, and final manifest
have SHA-256 hashes
b4848b22ea324421282dcfbbef9afc28576d2ea8233f8256a03b0797e1ea1bb7,
44e85f1914ba600a86288fb9961ff5b295dd1e0839d14493c8a6f38f83077cec,
bbe078d771026f46042e2a00aae5ab8efc42aea9a104cc6702c6529e5308b722,
ba0d72259f7d50fce72b191d077dc71b760e80f7c0ae0dedd6206510c2e8c081,
and
19661481698bc52666519f0b3f2b1d089b1c4ffe87ea12d92ae7d94d17274632.
No cross-family audit, human audit, or publication-level literature review
has run.

## P122 — one anchored star cannot amortize unrelated fresh large rows

**Status:** promoted from F134 after an independent hostile audit and an
independent proof-blind reconstruction. This is an exact local pruning
theorem. It is not a source-success theorem, a route killer, or a factoring
algorithm.

Let \(N\) be odd, let \(q\) be a unit, put \(w=\iota_N(q)\), and choose
distinct carry digits \(A_i\in[0,B]\). Define

\[
H_i=w+NA_i,
\qquad
P_i=qH_i.
\]

Retain only those \(P_i\) that have a displayed canonical endpoint
presentation below \(N\). For two distinct digits,

\[
\boxed{
\gcd(H_i,H_j)
=\gcd(H_i,A_i-A_j)
\le |A_i-A_j|
\le B.
}
\]

Thus no prime larger than \(B\) divides two different fresh cofactors
\(H_i\). This statement does not apply to the full values \(P_i\), which all
contain the common anchor \(q\).

Let \(\nu(x)\) be the rational-prime valuation-parity vector, and put

\[
a=\nu(q),\qquad h_i=\nu(H_i).
\]

For a selected-column vector \(x\), with \(t(x)=\sum_i x_i\),

\[
\boxed{
x\in\ker M
\iff
\sum_i x_i h_i=t(x)a.
}
\]

Therefore every star-only dependency with selected set \(S\) satisfies

\[
\boxed{
\prod_{i\in S}\operatorname{sf}_{>B}(H_i)
=
\operatorname{sf}_{>B}(q)^{\,|S|\bmod2}.
}
\]

The large squarefree parts on the left are pairwise coprime. Hence:

1. an even dependency can select only arms whose fresh squarefree kernel is
   \(B\)-smooth;
2. an odd dependency must partition the large squarefree kernel of \(q\);
3. the full star kernel has at most one odd coset beyond its even kernel.

Equivalently, a fresh large odd row is private inside the even star kernel.
Complete P66 gcd-free refinement computes this exact kernel without factoring
the large cofactor.

The theorem is local. If \(M_0\) is the retained old matrix, an old/new
dependency instead satisfies

\[
M_0y+a\,t(x)+\sum_i x_i h_i=0.
\]

An old combination can cancel a row that is private among the new arms.
Different stars also escape the gcd bound because their inverses differ.

Three exact certificates mark the boundary.

- At \(N=25\), a generalized odd star arm gives the singleton square
  \(576=24^2\), with global root \(-1\). The anchor and arm share the same
  large parity.
- At \(N=143\), the nonzero-carry value
  \(84\cdot63=3\cdot42^2\) closes against the old retained value
  \(102\cdot136=3\cdot68^2\). The joint root \(8568\) gives factors
  \(11\) and \(13\), although the fresh cofactor is not parity-smooth.
- At \(N=49\), the canonical presentation \(38\cdot40\) exposes the private
  row \(19\). Feeding \(19\) creates the distinct value \(19\cdot31\), so
  the row is no longer private in the next round.

The first and third certificates use the broader exact-value/all-block model;
they do not prove that the literal small-prime F133 source must generate their
first presentation. The second becomes a literal anchored arm with multiplier
\(3\), and its success is explicitly cross-layer.

P122 closes one tempting proof after P121: polynomial multiplicity of the old
row cannot be converted into closure by claiming that the fresh large arm
factors overlap within one star. They do not. The live mechanisms are
parity-smooth arms, the one odd anchor coset, retained cross-layer matches,
and later promotion of a private cofactor.

The statement, proof, hostile audit, blind reconstruction, and final manifest
have SHA-256 hashes
40354e169ef8632c206bd653819b3d0d117c670f134e18ff2f4558bc191c9483,
ca9fb0dc855fb032258908854e20f85da9851ba0777a5461382438f2839e5f3a,
1f434232f2bb2f2658a693d59552c3ae6d0f5b33f3bb35071a65d6db94a79ef9,
b0419abf326a4d590edbd05c13ce500e3f76c88751cba6b2790d5a16cf59ad34,
and
6a4f8745ff0802c6103ec4d450f40033e8400d45e77af01a7300d8edff1b0ec1.
No cross-family audit, human audit, or publication-level literature review
has run.

## P123 — anchored feedback has an exact recursion cutoff and forest boundary

**Status:** promoted from corrected F135 after three preserved failed review
rounds, a passing hostile re-audit, and a fresh statement-only blind
reconstruction. This is a narrow feedback-boundary theorem. It is not a
closure theorem, a complete-source obstruction, or a factoring algorithm.

Let \(N\ge3\) be odd, let \(B\ge2\) be an integer, and let \(q<N/B\) be a
unit. Write

\[
w=\iota_N(q),\qquad qw=1+kN.
\]

For each eligible prime anchor \(\ell\le B\), let
\(A_\ell\in\{0,\ldots,\ell-1\}\) satisfy
\(w+NA_\ell\equiv0\pmod\ell\), and put

\[
H_\ell=w+NA_\ell,
\qquad
c_\ell=\ell q,
\qquad
z_\ell=H_\ell/\ell.
\]

Then \(z_\ell=\iota_N(c_\ell)\). If \(A_\ell=0\), the arm repeats the old
exact value. If \(A_\ell>0\), then

\[
\boxed{z_\ell>N/B.}
\]

In both cases,

\[
\boxed{
\iota_N(z_\ell)=\ell q,
\qquad
P_N(z_\ell)=P_N(\ell q).
}
\]

Thus direct unary feedback on the complete new reciprocal endpoint is an
exact duplicate. It cannot recursively invoke the same small-block theorem.
This does not cover a proper block released from that endpoint, a power or
multi-block word, or wrapped feedback.

For two distinct carry digits in one star,

\[
\gcd(H_i,H_j)=\gcd(H_i,A_i-A_j)<B,
\qquad
\gcd(z_i,z_j)<B.
\]

Hence different-digit reciprocal endpoints cannot share a prime larger than
the anchor range.

The retained endpoint presentations give a sharper same-digit alternative.
For the anchors in one digit bucket, remove their complete prime powers from
\(H_A=w+NA\) and call the reciprocal-side residual \(R_A\). If
\(L_0>B\), or if \(A>0\) and \(L_A>B^2\), then

\[
R_A<N/B.
\]

Therefore that bucket either releases a proper small reciprocal-side block
or exhausts its residual. With \(B=n^3\), if no bucket reaches either
threshold, the number \(d\) of occupied nonzero digits satisfies

\[
\boxed{
d>
\frac{n^3}{25\log n}
-
\frac{n\log2}{3\log n}.
}
\]

For each covered prime row \(r>B\) that occurs oddly in \(q\), at least
\(d-1\) distinct retained exact values remain odd in row \(r\), unless a
declared gcd already factors \(N\).

This width still does not force a dependency. A full quasipolynomial-size
rooted-tree parity matrix can meet the same local row-multiplicity pattern,
have full column rank, and peel completely. F135 also gives an infinite CRT
family with five selected canonical relations whose displayed parity
submatrix is unitriangular through two feedback generations. That family
controls only the selected columns, not the complete source.

The exact live gate is now cross-layer or cross-star closure, a proper
released block, a wrapped or multi-block operation, and then a non-global
normalized root. More arms, endpoint reversal, or row multiplicity alone do
not prove progress.

The statement, proof, passing hostile re-audit, passing blind reconstruction,
and final manifest have SHA-256 hashes
`b03002c70c97e38506f6e0c4fc4585e4e5268ec59c2b3557f8f3600dd837ef02`,
`646e667edea22eb586cf069c6efdfdd8198132e00372d47e7ae882208d91a7a2`,
`d0c7c8a0a3192be884d92e644f824bacdc7f769ec26f3c66844254bebe000870`,
`a24cc841627f0abfa9192f5d6a58b6b4bcdfcf0d090b54a0a16704cc78c1b5bc`,
and
`85e62c43a8bde4779c61c237252a6755d24b968a9c49bc6a2136629b1d653326`.
The three preserved failed review reports have SHA-256 hashes
`d8decca251815841ffd984faed01c31309bc671715f2f32cbc0097dc6543de76`,
`14784e866cd6100878081e1934f7c60446bea109262f69d80674956b9cd0a2e1`,
and
`908bf72ca8cec4d1eba10331b6868347ccac92b3b2289c6549b69e9cd7d6eb04`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P124 — released feedback obeys an exact cross-star recenter-or-descend law

**Status:** promoted from corrected F137 after one preserved failed hostile
audit, a passing hostile re-audit, and a fresh statement-only blind
reconstruction. This is a conditional path theorem. It is not a closure
theorem, a transcript bound, or a factoring algorithm.

Let \(C\ge2\), let \(1<q<N/C\), and write

\[
q\iota_N(q)=1+kN.
\]

Suppose an eligible anchored parent relation has cofactor
\(H=\iota_N(q)+NA=Sr\), where complete endpoint refinement releases a unit
block \(1<r<N/C\). Put

\[
qSr=1+KN,
\qquad
qS=jN+t,
\qquad
1\le t<N.
\]

Then

\[
\boxed{
t=\iota_N(r),
\qquad
K=jr+k_r,
\qquad
k_r=K\bmod r.
}
\]

In the next star at \(r\), define \(H'_b=t+bN\). The old complement is
exactly

\[
\boxed{qS=H'_j.}
\]

For every \(b\ne j\),

\[
\boxed{
\gcd(qS,H'_b)=\gcd(qS,b-j)\le |b-j|.
}
\]

Therefore:

1. if \(j<C\), the parent is one virtual digit of the child star, and every
   genuinely different observed child digit has gcd below \(C\) with the
   parent complement;
2. if \(j\ge C\), then the released block strictly decreases: \(r<q\).

For two consecutive transitions with quotients at least \(C\),

\[
\boxed{
q_2<\frac{C}{C+1}q_0.
}
\]

Hence an uninterrupted large-quotient path has length \(O(C\log N)\), which
is \(O(n^4)\) for \(C=n^3\). The theorem does not bound branching or the
number of small-quotient interruptions.

The exact \(N=143\) certificate realizes both branches. Releasing \(r=7\)
from one parent arm gives \(j=5=C\) and \(7<28\). Releasing \(r=19\) from a
second arm gives \(j=4<C\); child digit \(4\) reproduces the old exact value
with canonical endpoints \((95,140)\), whose sign screens are null.

This result extends the one-star separation law by one adaptive generation.
It shows that simple parent-to-child overlap cannot appear freely: it either
recenters into the duplicate position or pays block descent. It does not
control another retained column, another star, small primes, parity of the
remaining cofactors, or the normalized-root image.

The statement, proof, passing hostile re-audit, passing blind reconstruction,
and final manifest have SHA-256 hashes
`2126e93be2be3abbca52ccb46615d3be8a2319c4dd064d8a5fa7705cd8084098`,
`2f973e801b849693d9f5f0951556bb6978eb6f4e0236387b17fc38a686deeecc`,
`c44e91c038e1d2e762abd616cfb4d0baa032a72e61f64f4196c4545e0eeb8aeb`,
`5e389f0b8084e964bea1359f8477c3ad78ff756e1aab8fa1f5d5ee821894aad5`,
and
`84d1b43a2beb0420bf7a6c3a97306db6def269aa1c7d924b2255410c2e82ace0`.
The preserved failed hostile audit has SHA-256
`66dfdf3b39cecb385e3b27fdc5d94f587029bd6c368052fecec31b94b9a605ef`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P125 — final row reuse requires carry-class hitting and still need not close

**Status:** promoted from F138 after a full artifact hostile audit and an
independent result-only blind reconstruction. Three registered proof-enabled
Sage verifiers passed and their pinned JSON outputs were reproduced. This is
an exact auxiliary obstruction. It is not a complete-source null or a
factoring algorithm.

For a canonical inverse pair, write

\[
P_N(c)=c\iota_N(c)=1+\kappa_N(c)N.
\]

After exact-value deduplication, retained columns are indexed by distinct
carries. A prime row \(r\) can occur in two retained columns only if their
carries satisfy

\[
\boxed{\kappa\equiv\lambda\pmod r,}
\]

with odd \(r\)-adic valuation in both values. For anchored stars,

\[
\kappa(b,A)=k_b+bA,
\]

so cross-star reuse has the exact gate

\[
\boxed{
k_b+bA\equiv k_d+dB\pmod r.
}
\]

Adaptive generation and relation count do not remove this congruence gate.

F138 gives two proof-certified 400-bit balanced-semiprime examples with a
canonical exact value whose valuation-one prime row satisfies
\(r>(N-1)/2\). Such a row is private in the complete canonical-inverse
universe: the only positive endpoint below \(N\) divisible by \(r\) is
\(r\) itself, and its inverse fixes one exact value. No old column, later
block, or different star can create a second deduplicated column on that
row.

The stronger maximum-anchor certificate uses

\[
n=400,\qquad L=9,\qquad E=2^{81},\qquad c=2E,
\]

and

\[
P_N(c)=cr=1+(c-1)N.
\]

The complete initial seed bank is null by an exact size bound. However,
\(c=2^{82}\) is already an allowed F130 support-one word. Thus this
certificate refutes universal owner-pivot cancellation, not a narrower claim
about values globally new in the later F133 layer. It also does not prove
that no earlier adaptive word factors the input.

Row reuse is a separate gate from rank closure. At

\[
N=161=7\cdot23,
\]

four canonical exact values have parity matrix

\[
\begin{pmatrix}
1&1&1&0\\
0&0&1&1\\
0&1&1&0\\
1&0&0&1\\
0&1&0&1
\end{pmatrix}.
\]

Its row degrees are \((3,2,2,2,2)\), so it has no degree-one row, but its
column rank is four and its kernel is zero. All displayed endpoint sign
screens are null.

Therefore a valid source theorem needs three distinct results:

1. enough carry-class hits to remove the rows it uses;
2. a strict final rank defect after all fresh pivots are included; and
3. a non-global normalized-root image on that kernel.

Minimum row degree two, a nonempty parity core, or cancellation of every
named owner row does not imply the second result.

The result, hostile audit, blind reconstruction, preserved local replay
failure record, and final manifest have SHA-256 hashes
`f6ac31e00bbf81b67f4cc64137f108fbe2224b3c5ba629e32bbabab58f0832be`,
`16c70c0b6602bcfb94bf241dd1d475613436ae8e61e7f6b7ffbcbc648015b514`,
`0238ffed30d9d370f4f3902f1072b8d5386042382114334aa79f9cbb5ff38545`,
`28b057bdb19e3af06ff6ed37c7ac2e9b24b9355e9f61454a7ff539d5adcba406`,
and
`44ebf0009a38dcb7d77c39bb24c30206ca0bf755d86e79bd4557ca76435778c3`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P126 — a linear public-anchor bank forces every covered large row to reappear

**Status:** promoted from the corrected F136 statement after a final hostile
re-audit and a fresh statement-only blind reconstruction. Earlier audit and
scope failures remain preserved in the artifact. This is an exact
source-side theorem. It is not a rank-closure theorem or a factoring
algorithm.

Put

\[
n=\lceil\log_2(N+1)\rceil,
\qquad
B=\lceil12n\rceil.
\]

Let \(q\) be a current unit block with \(1<q<N/B\), and let
\(w=\iota_N(q)\). For every eligible prime anchor

\[
\ell\le B,
\qquad
\ell\nmid Nq,
\]

there is a unique digit \(A_\ell\in\{0,\ldots,\ell-1\}\) for which
\(\ell\mid w+NA_\ell\). The exact canonical relation is

\[
P_N(\ell q)=q(w+NA_\ell).
\]

An elementary central-binomial and least-common-multiple estimate proves

\[
\vartheta(x)>\frac6{25}x
\qquad(x\ge2^{18}).
\]

Consequently, for \(n\ge21846\), the product of eligible anchors satisfies

\[
G_B(N,q)>N^2B.
\]

Let \(r>B\) be a prime with \(v_r(q)\) odd. After the unary value and the
complete anchor bank are processed, either a declared gcd screen has already
returned a proper divisor, or the globally deduplicated parity matrix has

\[
\boxed{\deg(r)\ge2.}
\]

Thus the polynomial anchor range \(n^3\) in P121 is not needed merely to
remove privacy. A linear bank already covers every odd large-prime row in
every block below \(N/(12n)\). This expands the proved source-side region,
although it gives fewer copies of each row than P121.

The same endpoint presentations give an exact release boundary. For an
occupied carry digit \(A\), let \(L_A\) be the product of anchor primes in
that digit bucket, with the empty product equal to one. Complete
multiplicity-aware refinement removes the full anchor-prime powers from the
cofactor \(H_A=w+NA\). If

\[
A=0,\ L_0>B,
\qquad\text{or}\qquad
A>0,\ L_A>B^2,
\]

then every remaining reciprocal-side residual block is below \(N/B\), or
the residual is exhausted. If no bucket meets these thresholds, the number
\(d\) of occupied nonzero digits obeys

\[
\boxed{
d>\frac{37n}{50\log(13n)}
}
\qquad(n\ge21846).
\]

For any fixed covered row \(r>B\), all but at most one of these values remain
odd in row \(r\). The exact trichotomy is therefore: a new small residual
block, residual exhaustion, or \(\Omega(n/\log n)\) retained columns reusing
the row.

The existing F130/F132/F133 source already scans every integer anchor through
\(E=2^{L^2}\), where \(L=\lceil\log_2(n+1)\rceil\). Under its explicit
imported cost guarantee, \(B<E\) in the declared range, so marking the F136
subbank changes no source position and preserves deterministic cost

\[
2^{O((\log n)^4)}.
\]

The theorem still does not force a binary dependency. Fresh cofactor rows
can make all new columns peel, exactly as in P122--P125. A complete proof
must force a strict final rank defect and then a non-global normalized root.

The final statement, proof, hostile re-audit, blind reconstruction, and
manifest have SHA-256 hashes
`e17c70e87c87d0893814ffb503f636087e60a373e31e06659ef524d1f8561c49`,
`ecb2a92c7c382473ec0466f8dc544d7118e6ac160f927df9e7d0e31f11eb0655`,
`2890e4c66634f110778e6828860704182f9286c3bda08d17641a4cdfe6db4b6d`,
`c8d55ef91e7f5de000541e94414ea9fd774dadaca213f80750fe9bfc73bd434f`,
and
`bb9b1e70172f0d3f31e43d1ac1e558cef47ed77c8a4c31b804a6b1bc15eb0409`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P127 — value-dependent packing can preserve several old rows at once but need not close

**Status:** promoted from corrected F139 after a passing final hostile
re-audit, a fresh statement-only blind reconstruction, and a registered Sage
certificate. The first invalid finite witness and two local statement audits
remain preserved. This is an exact source-operation and rank-boundary theorem.
It is not a complete-source theorem or a factoring algorithm.

Let \(N\) be odd, let \(B\ge2\), and let a public unit word satisfy
\(1<q<N/B\). Write \(w=\iota_N(q)\) for its least positive inverse. For
every eligible integer anchor \(1\le\ell\le B\), its canonical relation has
the form

\[
P_N(\ell q)=q(w+NA_\ell),
\qquad 0\le A_\ell<\ell.
\]

Let \(D\) be the occupied nonzero carry digits and let

\[
\mathcal R_B(q)=
\{r>B:r\text{ prime and }v_r(q)\text{ is odd}\}.
\]

A digit is common-good when its fresh cofactor has even valuation at every
row in \(\mathcal R_B(q)\). Then

\[
\boxed{
\#\{A\in D:A\text{ is common-good}\}
\ge |D|-|\mathcal R_B(q)|,
\qquad
|\mathcal R_B(q)|<\frac{\log q}{\log B}.
}
\]

The same new relations therefore preserve all large odd rows of the packed
word simultaneously. If two such rows are globally degree one in different
old owner columns, every common-good value is also new under global exact-
value deduplication. Public gcd-free refinement and sorting make the packing
operation quasipolynomial on an explicit quasipolynomial ledger, conditional
on at least two qualifying owner blocks having product below \(N/B\). No
theorem forces that size condition.

The exact rank gate is explicit. Suppose old independent columns
\(v_1,\ldots,v_t\) own private pivot rows, \(W\) contains the other old
columns, and each appended column \(u_j\) contains every pivot. Delete the
pivot rows and use hats for residual columns. A new dependency with nonzero
new coefficient vector \(\beta\) exists exactly when

\[
\boxed{
\sum_j\beta_j
\left(\widehat u_j+\sum_i\widehat v_i\right)
\in\operatorname{colspan}(\widehat W).
}
\]

Thus multi-pivot packing contracts all owner equations to one shifted
residual-class test, but it does not force that test to pass. An arbitrary-
size peelable incidence system can preserve all old pivots and remain fully
independent through one fresh private row per new column.

The registered exact certificate uses

\[
N=989=23\cdot43,
\qquad B=5,
\qquad q=187,
\qquad \iota_N(q)=238.
\]

The complete integer-anchor scan through five has digits
\((0,0,1,2,3)\). All packed and anchor endpoint sign screens are one. Every
nonzero arm preserves the two selected old rows \(11,17\), but the complete
six-column selected matrix has rank six, zero kernel, and a full peeling
order. The privacy claim is only for that frozen selected old ledger, not the
complete F26-Q source.

The original \(N=667\) witness was rejected because
\(\gcd(133+331,667)=29\). It is preserved and is not evidence.

The final statement, proof, hostile re-audit, blind reconstruction, verifier
output, and manifest have SHA-256 hashes
`a01cd50a749a61d70aefac9b50fca91e4a87332ef882c343fccc07009b75f27b`,
`8a41448676a1df5850fe90cc144bbca23a0513a36b9ac7e974a6b5de80de1a60`,
`c8495d43e50ed83400ea6956116ccc2f242478ae7b52caf0ca2fa63f68f31a9c`,
`d4c85ce6a31bbfefb4815a757a8c2daf312f9109e4b4ae7be439a687b48192ff`,
`4cda0f1af6adf29f73fc7e5f0d0d74f85ca4b331c02e8cbabe61b97a7c0778ba`,
and
`62e1e0fc9d00f8311ba800d66e412449279e5f25a33da133ff4f9d47a9790ff5`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P128 — unreduced word presentations give a strict quasipolynomial square-relation source

**Status:** promoted from F141 after a passing hostile audit, a fresh
statement-only blind reconstruction, and a registered replay. This is a
source and decoder theorem. It is not an all-input rank theorem or a
factoring algorithm.

At every frozen F130 word position, retain the exact monomial presentation

\[
U=\prod_{j\in S}q_j^{e_j}
\]

as well as its canonical residue `c=[U]_N` and least positive inverse
`w=iota_N(c)`. The old and new exact values are

\[
A(U)=cw,
\qquad
B(U)=Uw.
\]

They have the same endpoint sign screens because `U=c mod N`, but they need
not have the same integer square class. Store `U` by its exponent vector and
jointly gcd-free-refine the named atoms and all inverse endpoints. The exact
square-class matrix, its full binary kernel, and every normalized root can be
computed without rational prime factorization. Retaining every frozen word
position preserves the deterministic bound

\[
\boxed{2^{O((\log n)^4)}}.
\]

The source change has an exact standard form. Put `D(U)=Uc`. Then

\[
A(U)B(U)=D(U)w^2,
\qquad
D(U)\equiv c^2\pmod N.
\]

Thus canonical plus lifted columns are related by an invertible binary
column operation to the canonical ledger plus the factored square
congruences

\[
\boxed{Uc\equiv c^2\pmod N.}
\]

The transformation preserves the normalized-root map when the supplied root
`c` is retained. The lift is therefore a genuine source expansion, but it is
not a new decoding principle.

There are two exact positive mechanisms. First, if two monomials have the
same residue and parity presentations

\[
U=da^2,
\qquad
V=db^2,
\]

then their lifted product is a square with normalized root
`b*a^{-1} mod N`. It factors exactly when this root has mixed CRT signs. This
is a bounded multiplicative-order or rational-square collision, not an
all-input collision theorem.

Second, let `n>=64`, `A=n^3`, and let `q` be any current named unit block
with

\[
q\ge\frac{N}{12n}.
\]

For every eligible prime `ell<=A`, the literal support-two word

\[
U_\ell=q\ell^2
\]

is already in the frozen F130 source. On the branch where the declared gcds
neither factor `N` nor split `q`, the residues and inverse endpoints are
pairwise distinct, fewer than `12n` inverses are divisible by `q`, and global
exact-value deletion leaves more than

\[
\boxed{n^2/5}
\]

distinct good lifted values. Every rational prime `r|q` with odd
`v_r(q)` occurs oddly in all of them. The blind reconstruction obtained the
stronger intermediate count `>n^2/2`; the frozen promoted claim remains the
stated `>n^2/5` bound.

This complements P126: small named blocks and large named blocks now both
have explicit quasipolynomial relation families that reuse their old odd
rows. It does not follow that the full parity matrix loses rank. The new
inverse or residue endpoints can still contribute fresh private rows.

The registered 123-bit certificate uses the two allowed words `2` and
`2^513`, which have the same residue but different unreduced presentations.
The matched canonical one-column kernel is zero, while the lifted pair has
normalized root `2^256` and splits the two certified prime factors. The
903-input finite slice also contains five matched cases where the lifted
root image is useful and the canonical one is global. These are finite
capability certificates only.

The final statement, proof, hostile audit, blind reconstruction, registered
output, source, and manifest have SHA-256 hashes
`64bf45085bfef91190be4e23021e5e4bebbc6a9f48e03db56e49b087cf2b4bcf`,
`e0cea48fc14328f63c23d5ce56385cd6a216042da1f8e6c00bd2efe81914ae5a`,
`d1a8f3b6f1b106452612f155d5e28ec311521b10a7459415f7b3e341587f6581`,
`96199f72b55c82b79231df1202e20b13493abbc53c287b3a7dba1b1d667a9363`,
`c127a1a9c0a206aa7cc2d2d4285abb4791d37cf2ac8757b7b142a0ff42022ae3`,
`036e985399fd9e312a5f0f07de5dfe81400587ae56ce13833ad13fc77b306869`,
and
`cde9bde270cdbf3fa8bab8acad0353cc8c14fc1a0ba7cc90344b7a006083c6c0`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P129 — lifted squared anchors reduce exactly to a bridge-cycle and root gate

**Status:** promoted from F142 after a passing hostile audit and a fresh
statement-only blind reconstruction. This is a proof-only rank and root
boundary. It assumes the P128 source and proves no cycle-existence law.

For one squared-anchor position, write rational square classes additively:

\[
a=[q],\qquad \gamma_\ell=[c_\ell],\qquad h_\ell=[w_\ell].
\]

The canonical and lifted columns are

\[
[A_\ell]=\gamma_\ell+h_\ell,
\qquad
[B_\ell]=a+h_\ell.
\]

Hence the standalone lifted matrix is `B=H+a1^T`, so its rank differs from
the inverse-endpoint matrix by at most one. Relative to a retained matched
canonical column, adding `B_ell` is exactly adding the bridge

\[
D_\ell=q\ell^2c_\ell,
\qquad
[D_\ell]=[q]+[c_\ell],
\qquad
D_\ell\equiv c_\ell^2\pmod N.
\]

Let `C` be the old parity-column span and let `Gamma` contain the residue
classes `gamma_ell`. A nonzero new selection `x` closes with old columns
exactly when

\[
\boxed{
\Gamma x+(\mathbf1^{\mathsf T}x)a\in C.
}
\]

This is the exact relative-rank gate. Repetition of the old `q` rows does
not imply closure. In the atomic endpoint model, bridge columns are graph
edges. A forest, including a fixed-center star with one fresh residue row per
arm, has full column rank. Before bridge contraction, the corresponding
canonical and lifted columns form a subdivided star and are also independent.

If an adaptive transcript does create an exact endpoint cycle

\[
c_i=[q_i\ell_i^2]_N=q_{i+1},
\qquad q_{k+1}=q_1,
\]

then the bridge product is the exact square

\[
\prod_iD_i=
\left(\prod_iq_i\ell_i\right)^2.
\]

Its supplied root is `prod_i q_i`, so its normalized root is

\[
\boxed{
\rho=\prod_i\ell_i\pmod N.
}
\]

It factors an odd preprocessed input exactly when this public anchor product
is a non-global square root of one. If endpoints match only by rational
square class, with

\[
c_i=d_ir_i^2,
\qquad q_{i+1}=d_is_i^2,
\]

the exact normalized root becomes

\[
\rho=prod_i\ell_i s_i r_i^{-1}\pmod N.
\]

For composite endpoint vectors, the graph becomes a binary hypergraph and
the displayed quotient-span condition remains the complete rank test.
Deduplication must preserve indexed supplied roots; equal bridge integers
with different supplied roots cannot be discarded by integer equality alone.

The result changes the target. P128 solves a source-side row-reuse problem.
The remaining theorem must force a cycle or hypercycle modulo the old span
within quasipolynomial work, and must prove that its normalized root is not
global. Neither P128 nor P129 proves either fact.

The final statement, proof, hostile audit, blind reconstruction, and manifest
have SHA-256 hashes
`0049f74a635b7da7f288460ddbaf8e6669eb329073e8164b0834e74d3e4c1a1e`,
`4f257c6425f81926459b6acba3d401af2024c5d9394889150bcb9fa148f7dc4e`,
`d79807b7c91e0f1e4148665160e3e4bd422ca10b6af31ad1c8d892a7114fc3a9`,
`2e48402b73781d9779c271566f0548eddbade68052c033f5eed8b9d27d58d498`,
and
`72fd5d9519b3022e39887041f6d8316a7d9b21dd0a1862f60f3649060a69e483`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P130 — formal squared-action cycles are public half-relations, not a new signal

**Status:** promoted from F143 after a passing hostile audit and a fresh
statement-only blind reconstruction. This is a proof-only boundary for the
P128 bridge source. It proves no short useful cycle and no factoring
algorithm.

Let public unit generators define

\[
\Phi(z)=\prod_j a_j^{z_j},\qquad
\Lambda=\ker\Phi,
\]

and, for one unit center `q`, let

\[
v_z=[q\Phi(z)^2]_N.
\]

Then

\[
v_z=v_{z'}
\quad\Longleftrightarrow\quad
2(z-z')\in\Lambda.
\]

For every legal F141 squared-action edge, the matched canonical/lifted pair
is the bridge between its two public endpoint integers. If a formal closed
trail has signed generator displacement `delta`, its exact normalized root is

\[
\boxed{\rho=\Phi(\delta)},
\qquad
2\delta\in\Lambda.
\]

The same root is directly computable from the public collision
`v_z=v_{z+delta}`. Thus a useful formal bridge cycle is exactly a bounded
non-global half-relation. It is not a new mechanism beyond P71. Automatic
commutation diamonds have displacement zero and root `+1`; after exact-value
deletion they either remain root-`+1` dependencies or collapse to zero. If
every Cayley edge were legal, the formal-cycle root image would be exactly

\[
\Phi(\mathbb Z^m)[2]
\cong
\Lambda_2/\Lambda,
\qquad
\Lambda_2=\{z:2z\in\Lambda\}.
\]

This image equality gives no short representative. In one generator, the
first useful displacement is the ordinary half-order and can be exponential
in the input bit length.

The true arithmetic bridge kernel can be larger than the formal graph cycle
space because different endpoint integers can share rational-prime factors.
P130 gives one exact restriction on that remaining channel. For a fixed
center `q` and distinct prime anchors `ell,m<=A`, write

\[
c_\ell=q\ell^2-t_\ell N.
\]

Then

\[
\gcd(c_\ell,c_m)
\mid \ell^2t_m-m^2t_\ell,
\qquad
0<|\ell^2t_m-m^2t_\ell|<A^4
\]

unless both carries are zero. The zero-carry bridges are individual exact
squares with normalized root `+1`. After public removal of all prime powers
at primes at most `A^4`, the wrapped endpoint residuals are pairwise
coprime and coprime to `q`. Hence any bridge-only dependency inside this
fixed star can select an endpoint only when its residual is an integer
square. This necessary test is quasipolynomial when
`A=exp((log n)^{O(1)})`.

The result leaves open arithmetic hypercycles that cancel through older
columns or across different stars. That is the only bridge continuation not
reduced here to ordinary half-order search or a fixed-star private residual.

The final statement, proof, hostile audit, blind reconstruction, and manifest
have SHA-256 hashes
`bc9a9e399c03bff991cc85920eb6c0218276b1d05d0788b82461b39030b1a35a`,
`7c2784202f2a42200b126b54262c5d202ad86a0c2d1cc35931ddf52322ad86c2`,
`834facda506ed2995c46a17e1212c1896fbc69d7c969f043fb7003a05c4a2c74`,
`52f1f2506b9c74eff93389655ccddb3a4323fe732ead56aecc987690392d331c`,
and
`686fab587ada74b0e7ae338d5bd3a3263918b192d6156684db3b0f3e64bf765e`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P131 — wrapped positive containment cycles require square-root-scale anchor mass

**Status:** promoted from F144 V3 after a fresh hostile audit and an
independent statement-only blind reconstruction. The failed V1 surplus
theorem and the V2 strictness error remain preserved. This is a proof-only
boundary for P128/P129, not a factoring algorithm.

For one directed containment edge, write

\[
U_e=q_ea_e^2,
\qquad
c_e=[U_e]_N=r_eT_e.
\]

For every directed cycle \(\mathcal C\), with

\[
A_{\mathcal C}=\prod_{e\in\mathcal C}a_e,
\qquad
T_{\mathcal C}=\prod_{e\in\mathcal C}T_e,
\]

the endpoint cancellation gives

\[
N\mid A_{\mathcal C}^2-T_{\mathcal C}.
\]

If any edge of the cycle wraps modulo \(N\), then

\[
A_{\mathcal C}^2\ge N+T_{\mathcal C},
\qquad
A_{\mathcal C}>\sqrt N.
\]

This lower bound needs no residual-square assumption. Consequently, a
wrapped positive cycle whose total raw anchor product is
\(2^{\operatorname{polylog} n}=2^{o(n)}\) is impossible for all sufficiently
large inputs. A polynomial-length selected path, or a compact public anchor
whose numerical value already exceeds \(\sqrt N\), is not excluded.

For an indexed collection of cycles whose combined residual product is
\(S^2\), the corresponding actual P128 columns form an exact square relation.
Its normalized root is

\[
\rho=A/S\pmod N,
\qquad
A=\prod_{\mathcal C}A_{\mathcal C}.
\]

If the collection contains a wrapped cycle, then

\[
A^2-S^2=mN,
\qquad m\ge1,
\qquad
A\ge\sqrt{N+S^2}>\sqrt N.
\]

If also \(2A<N\), both \(\gcd(A-S,N)\) and \(\gcd(A+S,N)\) are proper.
For fixed \(S\), the useful metric window is therefore

\[
\sqrt{N+S^2}\le A<N/2.
\]

An unwrapped cycle has a square residual and normalized root \(+1\). Adding
unwrapped cycles does not help one wrapped cycle close its residual. Two
wrapped cycles already have combined anchor product above \(N\), so the same
metric window cannot hold.

The conditional certificate \(N=35\) uses centers \(13,17\), anchors \(2,3\),
and residuals \(1,1\). It has \(A=6=\sqrt{35+1}\), \(S=1\), and gives
\(\gcd(6-1,35)=5\), \(\gcd(6+1,35)=7\). It proves the algebra can succeed
when the required cycle is supplied; it does not construct such a cycle on
general input.

The result also verifies that a zero two-endpoint carry determinant has
normalized root \(+1\), while a four-endpoint cross-star grid is exactly the
P114 multiplicative rectangle. Thus neither object supplies a separate
closure law.

The exact remaining problem is to select, in quasipolynomial work, a path
that reaches the square-root scale and closes with a square residual, or to
force a different arithmetic hypercycle through actual integer prime-factor
overlap. The theorem supplies no cycle-existence, residual-square, or
non-global-root law.

The final V3 statement, proof, hostile audit, blind reconstruction, and
manifest have SHA-256 hashes
`87dacd7af5121f66561cea4136d1445f10cfe0185bd9229277fd48b358bf5f6f`,
`2635270473001fa32b6b9db15d9abb7460f31384ed9a8cec7de61f1c6717089e`,
`52cefa0f458d5c78c987d2353865e8220a8efcf63c93466b6a15ee6bc4216a95`,
`b706ca6fed8c0e45969814238854ae90142ee348fbb23e4a69d34a35294c71b7`,
and
`62fe96085b1c8fbcff31a748e5d44a9478c5bbd3fdce5ae6fec1f3c6c89239e7`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P132 — quasipolynomial finite-algebra sampling remains locally sparse

**Status:** promoted from F145 V2 after a fresh hostile audit and an
independent statement-only blind reconstruction. The V1 statement and its
failed reconstruction remain preserved. This is a proof-only source
boundary, not a factoring algorithm or a general lower bound.

Let \(N=pq\) for distinct primes. If \(A\) is a \(d\)-dimensional finite
commutative algebra over \(\mathbb F_r\), then a uniform element is a
nonunit with probability

\[
1-\prod_i(1-r^{-e_i})\le d/r,
\]

where \(A/\operatorname{Jac}(A)\simeq\prod_i\mathbb F_{r^{e_i}}\).
The nilpotent radical does not change this probability for a fixed
semisimple quotient. Therefore a uniform element of a rank-\(d\) finite
free algebra over \(\mathbb Z/N\mathbb Z\) gives a proper multiplication-
determinant gcd with probability at most \(d(1/p+1/q)\).

The same bound holds conditionally when the next probe is fresh and uniform.
Thus quasipolynomially many probes in an explicit quasipolynomial-rank
algebra remain exponentially sparse on balanced semiprimes.

For a finite etale \(\mathbb F_r\)-algebra of dimension \(d<r\), the algebra
is monogenic. A uniform element's Krylov matrix fails full rank with
probability at most

\[
\min(1,d(d-1)/r).
\]

Therefore \(M\) fresh probes in two etale reductions have local rank-
mismatch probability at most \(Md(d-1)(1/p+1/q)\). This is exponentially
small when \(Md^2=2^{o(n)}\). It does not control biased sources, adaptive
polynomials of the same sample, typical nonzero values, characteristic-
scale rank, or intermediate matrix entries.

For a squarefree polynomial with local factor-degree partition \(\lambda_r\),
the characteristic polynomial of absolute Frobenius is

\[
H_{\lambda_r}(T)=\prod_{e\in\lambda_r}(T^e-1).
\]

The map \(\lambda\mapsto H_\lambda\) is injective. If the local partitions
differ, \(p,q>2^{d+1}\), and the genuine CRT-glued Frobenius matrix is
supplied, coefficient gcds extract a factor in quasipolynomial time for
polylogarithmic \(d\). Known factors construct that map. Thus the missing
Frobenius object is itself factor-bearing on this promise; \(x\mapsto x^N\)
is not a substitute in general.

For a monomial power on \(\mathbb F_{r^e}\), the fixed-point count is
\(1+\gcd(E-1,r^e-1)\), and additivity is equivalent to
\(E\equiv r^j\pmod{r^e-1}\). Public exponents \(E=N^k\) therefore reduce to
hidden local order congruences. This gives no order-hitting impossibility.

Finally, if \(p<q\), then

\[
N\mid {N\choose k}\quad(1\le k<p),
\qquad
\gcd\left({N\choose p},N\right)=q.
\]

Every initial Hasse-jet interval of quasipolynomial numerical length is
therefore synchronized on sufficiently large balanced semiprimes. Sparse
large indices and a compressed large-range evaluator remain open.

The final V2 statement, proof, hostile audit, blind reconstruction, and
manifest have SHA-256 hashes
`9b7b5b21b65222be8a522163e4686dca7a232c94b87645d062dc017088eee18e`,
`435877c8bb5fbf6791f280bd7e9e4bd8d5764e66e16971138cda4491287effc8`,
`1e46a571056199825151534ae9fc358f10e4d592473c4a0a5e6d4c17df726c22`,
`2fc4b10040a351b371164d4db90d201dd27e8c7d92f821579cd7e9dd593b3ac0`,
and
`1b5365d222bd5808e592e43706c1f65bb2d1d8742071dd7630a29828f8049faa`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P133 — polylogarithmic AKS exchange scans are quasipolynomial but not generically complete

**Status:** promoted from F146 V2 after a fresh hostile re-audit and an
independent statement-only blind reconstruction. The false V1 equivalence
remains preserved. This is a general-matrix boundary for F04, not an AKS
counterexample or a factoring algorithm.

Let \(M_N=[B\mid T]\) have \(A\) rows over \(\mathbb Z/N\mathbb Z\), with
\(\det B\) a unit, \(t\) tail columns, and \(C=B^{-1}T\). Replacing \(k\)
base columns by \(k\) tail columns gives

\[
\det E_{I,J}=\pm\det(B)\det C[I,J].
\]

Thus an exchange gcd succeeds exactly when the corresponding square minor
of \(C\) has a proper gcd with \(N\). On arbitrary composites, prime-power
valuations can split before the first residue-field matroid disagreement.
On squarefree \(N\), the two success radii are equal.

The number of exchanges through support \(s\) is

\[
Q_s(A,t)=\sum_{k=0}^{\min(s,A,t)}{A\choose k}{t\choose k}
\le(s+1)\max\{1,At\}^{s}.
\]

For polynomial \(A,t\) and polylogarithmic \(s\), this scan is
quasipolynomial. If the full tail is polylogarithmic, it scans every maximal
minor. A prime AKS modulus with polylogarithmic positive excess above
\((\log_2N)^2\) has such a tail under the standard shift count. This is only
a conditional cost result.

Generic matrix structure cannot force a polylogarithmic mismatch radius.
For every \(s\), an explicit CRT/Vandermonde construction gives balanced
primes and one matrix whose exchanges through support \(s\) agree over both
fields, while the first disagreement occurs at \(s+1\). Its input length is

\[
n=\Theta(s^2\log(s+1)).
\]

It can be padded to \(A=n^2\), \(r=A+s+1\) without moving the first
disagreement. Hence no theorem about generic representable matroids forces
polylogarithmic locality. The construction is not an AKS error matrix. A
positive F04 result must use its coefficient arithmetic, prove the required
near-threshold modulus law, or use a different selector.

The finite P11 two-column-exchange hit is at the ordinary random-singularity
scale under the stated comparison model. This is calibration, not a
randomness claim or a forcing theorem.

The final V2 statement, proof, hostile re-audit, blind reconstruction, and
manifest have SHA-256 hashes
`886ca7aafa5d5cd42514fa4fbd6223a9e7ca12a368820a8c53b9731b3553ac57`,
`d4836162de32274bf253461b3f712c8e6d5662127ac2a907dc723d7c028a093c`,
`2b42343c0ba2edcc88b9d3c32cf4769a4b395c4b5590286781f3359788b07dc0`,
`3faaf0f299da164a31d30ed7a2a853476418c64b149c033e983bb0b18d70ac22`,
and
`ab52c2b3d60f9a6ba6329f54b7425cae90f6cf5f2d0eb9ea6a5acff6beeb1e35`.
The blind reconstruction verified the exact formulas and counts. Four
quoted P11 decimal evaluations depend on prime values omitted from its
isolated statement. No cross-family audit, human audit, or publication-level
literature review has run.

## P134 — residual square classes let two feedback cycles close by a cross ratio

**Status:** promoted from F148 after an independent hostile audit and a
statement-only blind reconstruction. This is an exact conditional decoder
and source target for F26-Q. It does not prove that the required cycles exist
and is not a factoring algorithm.

For a directed P128 containment cycle (mathcal C_i), let

\[
\alpha_i=\prod_{e\in\mathcal C_i}a_e,
\qquad
T_i=\prod_{e\in\mathcal C_i}T_e.
\]

Then (alpha_i^2\equiv T_i\pmod N). Take two cycle vectors with disjoint
retained-column supports after global exact-value deduplication. If their
residual products have the same rational square class,

\[
T_i=d s_i^2,
\qquad
T_j=d s_j^2,
\]

their union is an exact square relation. Its normalized root has the public
cross-ratio form

\[
\rho_{ij}
\equiv
\frac{\alpha_i\alpha_j}{d s_i s_j}
\equiv
\frac{\alpha_i s_j}{\alpha_j s_i}
\pmod N.
\]

Consequently,

\[
\gcd(\rho_{ij}\mp1,N)
=
\gcd(\alpha_i s_j\mp\alpha_j s_i,N).
\]

If the two exact slopes differ and

\[
\alpha_i s_j+\alpha_j s_i<N,
\]

both signs give proper factors. This is materially stronger than P131's
combined-product window: each cycle can have a nonsquare residual, and the
two wrapped anchor products can have product above (N).

A conditional quasipolynomial consequence is exact. If an explicit source
provides more than (R) column-disjoint cycles with (T_i\le R),
(alpha_i\le H), distinct exact slopes inside each residual square-class
bucket, and (2H\sqrt R<N), pigeonhole plus the cross-ratio test factors
(N). The decoding cost is quasipolynomial when the explicit transcript and
(R) are quasipolynomially bounded. No theorem currently forces this cycle
supply, small residual products, or slope diversity.

The finite (N=745) certificate verifies the formulas and has null declared
inverse-pair endpoint screens. It is not an isolation certificate: the two
centres already satisfy a simpler useful congruence of squares. This does not
affect the theorem.

The statement, proof, hostile audit, blind reconstruction, and final manifest
have SHA-256 hashes
`8d790d05d8161444684d109ad16c3cc1f2be453dcc04638a8d8a10406b78cc35`,
`92542fe2f91fbdb26311112bef799f0f0f7d02d22ca161b34d1ca2fcf082e405`,
`08403d4008e36336980ba43ae9d0e5ed90a632409cd63b645492c33f2f94dba7`,
`ed74340c81c32390c9121f5cb33c28ab92b0cbf5463a83a239cd04beb1585a03`,
and
`15ff945ef399a8efa3e21502bb29be795e8acf2b8534b3645e9d4bb77bb999a4`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P135 — compact large squared anchors canonicalize to an ordinary congruence of squares

**Status:** promoted from F149 V2 after a fresh hostile re-audit and an
independent statement-only reconstruction. This is a proof-only source
boundary. It is not an all-input source theorem and not a factoring
algorithm.

Let \(q\) be a unit centre, let \(a\) be an arbitrarily large integer with
compact presentation, and put

\[
\alpha=[a]_N,\qquad
c=[q\alpha^2]_N,\qquad
w=\iota_N(c).
\]

The P128 canonical and lifted values are \(C=cw\) and \(L_a=qa^2w\).
Their lifted square class is

\[
[L_a]=[qw],
\]

so the exact size and exponent mass of \(a\) disappear. Replacing \(a\) by
its canonical residue changes the integer presentation only through a square
relation with normalized root \(+1\). Every canonical endpoint,
containment edge, and residual also stays unchanged.

The two actual columns close exactly when

\[
qc=s^2.
\]

Then their normalized root is

\[
\rho\equiv s(q\alpha)^{-1}\pmod N,
\]

and the terminal tests are exactly

\[
\gcd(s-q\alpha,N),\qquad
\gcd(s+q\alpha,N).
\]

Thus one compact large-anchor hit is an ordinary congruence of squares. For
\(N=p\ell\) with distinct odd primes and fixed unit \(q=du^2\), the exact
number of useful uniform anchor residues is \(2V_d=O(\sqrt{N/d})\).
Consequently, quasipolynomially many fixed-centre uniform trials still have
success probability \(2^{-n/2+o(n)}\). This does not apply to a
factor-correlated compact-word source.

The \(N=77\) certificate verifies a useful canonical-plus-lifted singleton
after both endpoint sign screens fail. It is a local semantic witness, not a
surviving complete-algorithm input, and it reduces to the existing
congruence-of-squares/half-relation mechanism.

The V2 statement, reused proof, hostile re-audit, blind reconstruction, and
final manifest have SHA-256 hashes
8e116d027dd5ecfe14f789fd301e9a6f4cf3b62e402fa2575cfc34406aa4d4dd,
08cd204330f47429f20e747a1c8bad9a7084ec5de9249a8e5e755f55e305da0e,
8d4ecd2eaccdfc9fe89677e6678e77eb4100ee91a6409ac228b36c79366933ab,
844505799fb6a3ca04a4690547feb8aa9ae63f036f08133d185a4f123463dbda,
and
fac3d8405bf4910a7079010018b485d4b6d2e6992b689e6203e92418b84354a1.
The failed V1 statement and audit remain preserved. No cross-family audit,
human audit, or publication-level literature review has run.

## P136 — bounded-anchor wrapped cycles lie in one quasipolynomially decodable core

**Status:** promoted from F147 V2 after a fresh hostile re-audit and an
independent statement-only reconstruction. This is a frozen-source reduction
and complete conditional decoder. It does not prove that a cycle or useful
root exists and is not a factoring algorithm.

Fix one P128 named basis and an explicit list of squared-anchor positions
\((q,a)\) with \(1<a\le H\) and

\[
H^4\le N.
\]

If a directed containment cycle has one wrapped edge, every edge in that
cycle is wrapped. Every source and target block on it satisfies

\[
q,r>\frac{N}{H^2},
\]

while its carry and residual satisfy

\[
1\le t,T<H^2.
\]

Each frozen word position has at most one named target above \(N/H^2\).
Therefore every wrapped cycle lies in one public large-block core obtained
by scanning the entire frozen source. No exponential path branching is
needed inside that source.

Complete gcd-free refinement of the core bridge values gives its exact
parity kernel and normalized-root map. If \(E_H\) is its edge count and
\(R_H\) the number of residual primes, then

\[
\dim\ker M_H\ge E_H-m-R_H
\ge E_H-m-\pi(H^2).
\]

This only forces a conceptual dependency. Exact-value survival and a
non-global root remain separate gates. The complete core scan and decode
are quasipolynomial when the explicit source size and \(H\) are
quasipolynomial.

Every wrapped cycle with length \(L\) also obeys the strict necessary bound

\[
L>\frac{\log N}{2\log H}.
\]

This gives no cycle-existence or upper-length law.

The V2 statement, reused proof, hostile re-audit, blind reconstruction, and
final manifest have SHA-256 hashes
a65034746ef11b0165ee4c0591c68107997e14d7234df1a4c1a45482b905d87b,
6868737e521dcaa64473bc105d9fa85e1458947b5aa312bc98f3771e141577ad,
e5deb09c9b3e8874658a999fbb4f7e86204c59dc4eeb3e22c6f01e19495bdf69,
e61406b24486ff77e4b5a3f5ec7394c5a6ec9c1c1b2eb5869bc7b55ab8a6e296,
and
8451bc265510735abfd9e1e35fed558fdc997b125c7c93746afcbc6e971e3a41.
The false V1 reachability sentence and failed blind reconstruction remain
preserved. No cross-family audit, human audit, or publication-level
literature review has run.

## P137 — reciprocal-anchor positive two-cycles are exact global-root traps

**Status:** promoted from F150 V2 after a fresh hostile re-audit and an
independent statement-only reconstruction. This is a proof-only boundary for
one natural feedback subfamily. It is not a factoring algorithm.

Let \(N\) be odd and preprocessed. Suppose units \(x,y\) give the positive
containment edges

\[
[xy^2]_N=yT,
\qquad
[yx^2]_N=xS.
\]

With \(h=[xy]_N\), exact quotient arithmetic forces

\[
S=T=h,
\qquad
xh<N,
\qquad
yh<N.
\]

The two bridge values have product

\[
D_xD_y=(x^2y^2h)^2.
\]

Their supplied modular root is \(xyh^2\), so the normalized root is

\[
\rho=xyh^{-1}\equiv1\pmod N.
\]

Thus the reciprocal-anchor cycle can survive all endpoint screens and still
produce only the global root. Actual P128 exact-value deletion is safe
because its duplicate directions have root \(+1\); this does not authorize
deduplication of transformed bridge values without supplied-root labels.

The public choice

\[
q=\left\lceil\frac Na\right\rceil,
\qquad
1<a<\sqrt N,
\]

either finds a divisor through the ordinary screens or creates such a
reciprocal decoy. The \(N=77\) certificate verifies the strict null-screen
case.

The V2 statement, proof, hostile re-audit, blind reconstruction, and final
manifest have SHA-256 hashes
04725f9125976998d482663774cfcd11a17f215c953bc81be701bad6e318d7ee,
5afe0be2bf8526064b421384c27452fc393f88cc88cd47a07e52f7cb3a03ec66,
7563e1680eb7facebbd2b1be75dcc8205f40a300435d6bc89c3ab4d154a0451b,
c6ab916b5381eee61f36d52b520f65e88b6650fa584659410e3baf30e397e996,
and
9ced646e64341070ca6be395f745400f8b18f56bb8d2ec030db16f48f5ff7514.
The failed V1 files remain preserved. No cross-family audit, human audit, or
publication-level literature review has run.

## P138 — retained square relations obey an exact split-or-section law

**Status:** promoted from F152 V2 after a fresh hostile re-audit and an
independent statement-only reconstruction. This is a structural decoder
theorem. It is not a relation-source theorem or a factoring algorithm.

Let (q_1,\ldots,q_m) be pairwise-coprime nonsquare unit blocks, so their
rational square classes are independent. For

\[
Q(v)=\prod_j q_j^{v_j},
\qquad
C(v,w)=\prod_jq_j^{v_jw_j},
\]

put

\[
E_Q(N)=\{(v,z):z^2\equiv Q(v)\pmod N\}
\]

with product

\[
(v,z)\star(w,t)=(v+w,ztC(v,w)^{-1}).
\]

This is an abelian group of exponent two. Its kernel over the parity space is
the group of square roots of one modulo (N). For an exact retained relation

\[
T_i=s_i^2Q(v_i),
\qquad
\alpha_i^2\equiv T_i\pmod N,
\]

the decorated lift is (g_i=(v_i,\alpha_i s_i^{-1})). The binary parity
kernel is exactly the complete integer-square dependency kernel, and its
product in (E_Q(N)) is exactly the P66 normalized-root map.

Consequently, every explicit transcript has an exact dichotomy:

1. one parity dependency has a non-global root and immediately factors
   (N); or
2. all observed decorated lifts define one unique homomorphic section over
   their generated parity span, modulo the two global signs.

The test is online Gaussian elimination plus modular group operations, so it
is polynomial in the explicit transcript size and remains
quasipolynomial for a quasipolynomial source. Equal exact values can be
deleted only after their supplied roots are compared; a non-global mismatch
already factors (N), while a global match is inert. Occurrence and layer
metadata must remain attached.

For two individually null relation layers, the useful cross-layer image is
exactly their section disagreement on the intersection of their parity
spans. P108 is one finite instance of this law, and the P134 cross ratio is
its two-record same-squareclass specialization. A single family can also
violate the section through an internal circuit; two named families are not
logically necessary.

The extension always has abstract sections. Thus parity rank, many circuits,
small doubling, and row reuse alone cannot prove factoring. The missing
quasipolynomial theorem must force the supplied lifts not to factor through
one common section, or derive another public contradiction from persistent
agreement.

The V2 statement, proof, hostile re-audit, blind reconstruction, and final
manifest have SHA-256 hashes
3f5b232d6bdeb9ca6a70cecd2bdfc0e1307406de3f84a23c953c59323fcfc78e,
46b45cc752f5524670431cd288b5b5baa6cb246d1f536f447e095e85a3824c67,
bd6f32a0c5c9d431ab1864df6050ef5a69874c26fe3b3962f31df4c889dc170d,
0ae27e94baf3f67baded253fbd642b23ba318cc671e67b7098fa1acccdb36c0b,
and
332049287e3a69a7f012959059649b247160c291253fca99ba8fa0bf3957638a.
The V1 failure history remains preserved. No cross-family audit, human audit,
or publication-level literature review has run.

## P139 — certified high order removes short local collisions but does not supply factor correlation

**Status:** promoted from F151 V3 after a fresh hostile audit and an
independent statement-only reconstruction. The Harvey--Hittmeir and Pilatte
results used below are explicit external premises. This is a source boundary,
not a factoring algorithm.

Let

\[
n=\lceil\log_2(N+1)\rceil,
\qquad
4\le B<N-1,
\qquad
B=2^{(\log n)^{O(1)}}.
\]

The Harvey--Hittmeir large-order procedure, followed by the public scan

\[
\gcd(\alpha^e-1,N),
\qquad 1\le e\le B,
\]

returns a proper factor or certifies

\[
\operatorname{ord}_r(\alpha)>B
\quad\text{for every rational prime }r\mid N.
\]

This complete local-order certificate is deterministic and
quasipolynomial. On its no-factor branch, put

\[
c_e=[\alpha^e]_N,
\qquad
w_e=\iota_N(c_e),
\qquad
1\le e\le\lfloor B/4\rfloor.
\]

For distinct eligible positions, every listed difference, signed
difference, product-to-\(\pm1\), and inverse-pair sign screen is one modulo
every hidden prime. Thus the short power bank has no local collision of
these forms.

This clean modular source does **not** make its canonical exact integers

\[
P_e=c_ew_e=1+\kappa_eN
\]

independent. Exact values can repeat, share ordinary integer factors, or
close under the factor-free square decoder. Two strict finite certificates
show both residual effects:

- for \(N=143\), \(B=8\), \(\alpha=2\), the first two positions have the
  same exact value \(144\), although the two local orders are \(10\) and
  \(12\);
- for \(N=391=17\cdot23\), \(B=12\), \(\alpha=37\), the local orders are
  \(16\) and \(22\), but

  \[
  2738\cdot392=1036^2,
  \]

  and the two signs of the positive root expose \(17\) and \(23\).

Hence large local order removes easy modular coincidences but leaves the
canonical integer carry channel alive. It neither proves nor rules out a
factor-correlated exact-value source.

Pilatte's cited relation-lattice theorem supplies dimension
\(d=\Theta(\sqrt n)\) and basis norm \(\exp(O(d))\), but it supplies no
classical sampler and no sparse-support bound. The full integer ball at that
radius contains \(\exp(\Theta(n))\) candidates, so direct enumeration is not
quasipolynomial.

Finally, the direct splice from \(\alpha\) to one fixed Jacobi-minus-one
Kummer coordinate

\[
x=(\alpha+\alpha^{-1})/2
\]

loses the split/nonsplit orientation: its Chebyshev orbit depends on
\(\alpha\) but not on the Jacobi parameter. This only blocks that fixed
coordinate splice. Other torus points, larger exponents, carry decoders, and
multi-relation combinations remain open.

The V3 statement, proof, hostile audit, independent reconstruction, and
final manifest have SHA-256 hashes
73c8e7a8c58fd3fd40f56f3128ded748313a98cd9b76ec663bee9ec55ba50b98,
a4ffebd5cd981ea949850bc2cb71ff34a07ec41969904cf7c46cd05941ca3f57,
c56708f30685bad8e9623e3184824e917ebf1709ba0c2c6236f3859de43b2f02,
d2723413004c14e035526e5b176d7228d86a596431aa605ea23836d32b8e0698,
and
4874aeaa48906aeda7c460906b46eb2d845fe897a6baa0eeb4bd5e516498c5f0.
The failed V1 and conditional V2 histories remain preserved. No
cross-family audit, human audit, or publication-level literature review has
run.

## P140 — Jacobi orientation is factor-correlated but standard torus operations preserve one section

**Status:** promoted from F153 V3 after a fresh hostile audit and an
independent statement-only reconstruction. This is an operation-specific
boundary for distinct odd semiprimes. It is not a factoring algorithm and
does not classify all torus coordinates.

Let \(N=pq\) with distinct odd primes. For every unit discriminant \(D\)
with Jacobi symbol \(-1\), define the hidden orientation

\[
\epsilon(D)=\left(\frac Dp\right).
\]

Then \((D/q)=-\epsilon(D)\). Thus bare \(N\) can create a guaranteed local
asymmetry. For every multiplicative discriminant word

\[
F=\prod_iD_i^{e_i},
\]

its two local quadratic characters are determined by the single character
\((\cdot/p)\), the parity of \(\sum_i e_i\), and
\(\prod_i\epsilon(D_i)^{e_i}\). This controls the base square class. It does
not determine the supplied coordinate root or the P138 decorated section.
Two sections with the same orientation character can still differ by a
non-global square root and then factor \(N\).

Six natural extraction operations have exact boundaries:

1. the P55 signed-gap exponent has one universal synchronized division by
   two, but the same direct argument cannot produce a uniform halving ladder;
2. Cayley halving is exactly a square-root choice for \(1-Dt^2\); the two
   global branches differ only by global \(-1\), while a mixed branch already
   factors \(N\);
3. a conjugation-preserving map between two quadratic discriminant algebras
   needs a square root of their discriminant ratio; synchronized choices
   differ only by global conjugation;
4. the three direct relative norms in the biquadratic algebra return only
   \(U^2\), \(V^2\), or \(1\);
5. a homomorphism from an ordinary local unit group of order \(r-1\) to a
   nonsplit norm-one torus of order \(r+1\) has image order at most two; and
6. the fixed Kummer coordinate

   \[
   x=(\alpha+\alpha^{-1})/2
   \]

   has a Chebyshev orbit independent of the Jacobi discriminant, so the
   direct high-order splice loses the orientation label.

There is also one exact product-discriminant identity. If \(D,E\) both have
Jacobi symbol \(-1\), put \(F=DE\) and
\(\eta=\epsilon(D)\epsilon(E)\). Every \(W\) in the norm-one torus for
\(F\) satisfies

\[
\boxed{
W^{N-1}=W^{\eta(p+q-2\eta)}.
}
\]

Equal orientations give exponent \(p+q-2\); opposite orientations give
\(-(p+q+2)\). This specializes the P55 local-order identity and does not
publicly reveal \(\eta\), the exponent, or a mixed root.

Therefore the Jacobi bit is real factor-correlated information, but the
listed word, halving, norm, isomorphism, and homomorphic-transfer operations
remain compatible with one common section. A live retry needs extra
coordinate data, a non-norm invariant, a nonhomomorphic map with its own
order theorem, or a torus-native source that forces section disagreement.

The V3 statement, proof, hostile audit, independent reconstruction, and
final manifest have SHA-256 hashes
91886c70c39496dc0519ab4928f7234a263539eb235a863c7ac8bbe21c50d8a0,
f86807ae0bff8b4557f24da18c17b6729e4cb78895b22f6987f8a77efc17447d,
176a12902893b11fdbda5c86ff113cea50978bac070cdfb2e55dfd4b4dbcb645,
67b772502c1dd8341d4b0c4ae26ff7eb1248a29b82b61342e5b0f673cc29b595,
and
c136a17dc21ece551d4e5ec43e4b398c40a30a28ce59a578f2db05a39ab0cabc.
The failed V1 and repaired V2 histories remain preserved. No cross-family
audit, human audit, or publication-level literature review has run.

## P141 — section feedback can expand a frozen named subgroup on an infinite family, but the released block can be public already

**Status:** promoted from F155 after hostile audit and independent
statement-only reconstruction. This is an unconditional representation-level
feedback theorem. It is not an information-gain theorem or a factoring
algorithm.

Let

\[
M=23{,}400,
\qquad
N\equiv77\pmod M,
\]

and define

\[
z=\frac{N-3}{2},
\qquad
s=\frac{N-2}{3},
\qquad
a=\frac{3N+9}{4}.
\]

These public integers lie in \((0,N)\), are units, and satisfy

\[
z^2\equiv a\pmod N,
\qquad
zs\equiv1\pmod N.
\]

Both endpoint screens are null:

\[
\gcd(z-s,N)=\gcd(z+s,N)=1.
\]

Nevertheless, exact integer refinement gives

\[
\gcd(a,s)=5,
\qquad
a=5(a/5),
\qquad
\gcd(5,a/5)=1.
\]

There are infinitely many balanced distinct-prime semiprimes \(N=PR\) in
this class with

\[
P\equiv7\pmod M,
\qquad
R\equiv11\pmod M,
\qquad
P,R>n^2.
\]

For every such input, both \(z\) and \(s=z^{-1}\) already lie in the old
cyclic subgroup

\[
H=\langle a\rangle.
\]

Thus canonical inversion adds no new modular residue class. But if the old
named state is frozen as the single integer block \(\{a\}\), refinement by
\(s\) names \(5\) and \(a/5\). Quadratic character at \(P\) proves

\[
5\notin H,
\qquad
H<\langle5,a/5\rangle.
\]

This is an infinite-family version of the feedback distinction: one can
change the algorithm's named multiplicative subgroup through a new integer
presentation even when the selected residue has no new modular information.

The limitation is decisive. The released block is literally the fixed
public integer \(5\), and \(a/5\) is directly computable from \(N\). A
routine can name them before feedback, and the full F130 seed bank already
contains \(5\). Therefore the theorem proves strict growth only relative to
the declared frozen one-block ledger. It does not prove new factor
information, operational growth over the full source, a useful exponent, or
an all-input progress law.

The statement, proof, hostile audit, independent reconstruction, and final
manifest have SHA-256 hashes
b42079fcb9b0d09a16483fffd8ee41d24f3fc6c3ac6bddc4495af6fa09298998,
5fd7d453b96c67b6112b4a50d52d5ce877e317ac7029dc792da21dfd1e52c233,
e2f4c51a74cdc9366b4a5735050f70249ef2df291a1b6e39b702a1894494d3c5,
febdb18ab441da7e3f1dde1f9711aa70d4d565056bb9503997d5904c398e328f,
and
cd4a30c24cd14d9af8514bd3fa0f13f937771a042e55cd9c2de1610a63c0cca9.
No cross-family audit, human audit, or publication-level literature review
has run.

## P142 — completing a failed section is decoder-inert but can change a refinement-mediated grammar

**Status:** promoted from F154 V3 after a fresh hostile re-audit and an
independent statement-only reconstruction. This is a proof-only closure and
interface theorem. It is not an all-input source or factoring theorem.

Assume the no-factor branch of P138. Let the observed parity span be \(W\),
and choose actual retained lifts to obtain a public homomorphic lift

\[
\widetilde h(v)=(v,z_v),
\qquad v\in W.
\]

For the least positive inverse \(s_v=\iota_N(z_v)\), form

\[
P_v=s_v^2Q(v).
\]

Every \(P_v\equiv1\pmod N\), its decorated lift is exactly
\(\widetilde h(v)\), the values \(P_v\) are pairwise distinct, and
\(P_0=1\). For every indexed subset \(S\subseteq W\),

\[
\prod_{v\in S}P_v\text{ is a square}
\quad\Longleftrightarrow\quad
\sum_{v\in S}v=0.
\]

Every such pure completion dependency has normalized root \(+1\). Every
mixed old/completion dependency has only a global root. Thus adding the
whole completion does not enlarge the current useful normalized-root image.
For every pair \(v,w\), the explicit triple \(P_vP_wP_{v+w}\) is a square
whose displayed positive root is \(1\pmod N\).

The completion has \(2^{\dim W}\) records and costs

\[
\operatorname{poly}(2^{\dim W},n+\Lambda_Q).
\]

It is quasipolynomial when the observed dimension is polylogarithmic and the
explicit block transcript has quasipolynomial total length.

The completion can still change a later algorithm through integer
presentation. Joint gcd-free refinement by the canonical endpoints \(s_v\)
can name blocks that were absent from the old named ledger. Under the exact
interface studied here, later source rules see completion data only through
those newly named blocks. No inertness claim is made for a grammar that can
read raw completion values or provenance.

The finite witness is

\[
N=77,
\qquad
q_1=4706,
\qquad
z=3,
\qquad
s=26.
\]

Completion refines

\[
4706=26\cdot181.
\]

The old residue subgroup has order \(15\), while the new named block \(26\)
has order \(30\). A later permitted operation factors the input, for example

\[
26^{15}\equiv34\pmod{77},
\qquad
\gcd(34-1,77)=11,
\]

or more simply

\[
\gcd(181+1,77)=7.
\]

This is only a restricted-grammar capability witness. Both \(26=3^{-1}\)
and \(181=4706/26\) were already public computations, so completion adds no
new modular information. The theorem does not force refinement, select a
later exponent or screen, bound feedback rounds, or prove all-input success.

The V3 statement, proof, hostile re-audit, blind reconstruction, and final
manifest have SHA-256 hashes
7021a1b9c509460606ea1168dc0f782e25cfa1461639ae256f41caf6147c1ef3,
b9842a0d05893360af75a4571f46738a69ca9de624ab35b64adc75ae602b13ad,
d3a2ed6abe1f27bc2fe395307b30101c975e9ecd28f8cb137cc560a5ca9741f1,
fa070e5d5dd4fa76e5b300f1d65ee3389c72492252f060290780dfc5f7f8f666,
and
2e40897f73444d00d5e5715568c1300ef381f63cfe7305f78b18d1ccf71b3b47.
The V1/V2 repair history remains preserved. No cross-family audit, human
audit, or publication-level literature review has run.

## P143 — sparse products of relation lifts form a deterministic quasipolynomial feedback source

**Status:** promoted from F156 V2 after a fresh hostile re-audit and an
independent statement-only reconstruction. This is a uniform source-and-cost
theorem. It does not prove that the source factors every input.

At each frozen named-block state, first complete the ordinary P118 scan and
run the P138 consistency test. From the retained base relations, choose a
deterministic parity basis \(b_1,\ldots,b_r\) together with their actual
decorated lifts. Put

\[
D=\lceil\log_2(n+1)\rceil^2.
\]

For every nonempty subset of at most \(D\) basis lifts, compute its decorated
product \((v_S,z_S)\), its canonical inverse \(w_S=\iota_N(z_S)\), and the
exact feedback value \(F_S=z_Sw_S\). The direct screens satisfy the exact
identities

\[
\gcd(z_S-w_S,N)=\gcd(Q(v_S)-1,N),
\]

\[
\gcd(z_S+w_S,N)=\gcd(Q(v_S)+1,N).
\]

Expose both endpoints before exact-value deletion. Keep occurrence,
presentation, layer, and provenance metadata. Retain only the first decoder
copy of an equal exact value. Base relations and feedback relations remain
in separate logical ledgers: feedback endpoints may split named blocks, but
feedback relations never enter a later section basis.

After the ordinary and section menus both finish, apply one joint
multiplicity-aware gcd-free refinement. Continue only after a strict split
of a descendant of the fixed initial named product. This gives finitely many
frozen stages. Under the imported P118 transcript bounds, the full source,
all refinement, and one final complete decoder cost

\[
\boxed{2^{O((\log n)^6)}}.
\]

The source is strictly different at the grammar level: support is measured
in retained relation-basis vectors, and one such vector can be dense in the
named integer blocks. This is a syntactic enlargement, not a proof that the
set of produced residues is strictly larger. If \(r\le D\), the scan contains
every nonidentity section vector and therefore every F154 refinement
opportunity; the omitted identity has \(z=w=1\) and is inert.

The construction can terminate with a direct factor, a strict named
refinement, a useful final normalized root, or a null terminal decoder. No
theorem excludes the last outcome. Thus P143 supplies a complete
deterministic QP search grammar and precise decoder, but no all-input
success, density, rank-defect, or non-global-root law.

The V2 statement, proof, hostile re-audit, blind reconstruction, and final
manifest have SHA-256 hashes
71b640469c0f57440d8e290b63af411eb33ee08b08c814413b5a04fff1c7d3dc,
37e80fc0600eeb5a178f9e31c1f68f17b29ba3ed8837dcb5e391be0d6e5ef685,
5c5edb2f48f851c71cdb4656cc8aed71004c6ec011286bc1b4d809ce96034c96,
19691cfefa8e718b96befe20220f57fd8fdcde1d2a2340368d5739be423a58d3,
and
1a566b4390b9513b45f5de3170dece1c87804f012fae9a25288c1199879e2789.
The V1 repair history remains preserved. No cross-family audit, human audit,
or publication-level literature review has run.

## P144 — a certified quadratic lift gives a factor, no change, or exact common-order doubling

**Status:** promoted from F158 after hostile audit and independent
statement-only reconstruction. This is a conditional decoder and monotone
progress theorem. It does not construct the required quadratic lifts and is
not an unconditional factoring algorithm.

Let \(N=pq\) with distinct odd primes. If a public subgroup
\(H\le(\mathbf Z/N\mathbf Z)^\times\) is supplied as a complete list and a
public unit \(x\) satisfies \(x^2\in H\), scan

\[
\gcd(x-h,N),
\qquad h\in H,
\]

with factor-first priority. The exact outcomes are:

1. a proper gcd factors \(N\);
2. an \(N\)-gcd proves \(x\in H\); or
3. all gcds are one, and adjoining \(x\) doubles \(H\) globally and doubles
   its image in each hidden prime field.

This scan is quasipolynomial when \(H\) has a quasipolynomial explicit list.

There is also a compact version. A pair \((g,M)\), with the rational-prime
factorization of \(M\), is a certified common-order generator when

\[
g^M\equiv1\pmod N
\]

and

\[
\gcd(g^{M/\ell}-1,N)=1
\qquad(\ell\mid M\text{ prime}).
\]

These public conditions prove

\[
\operatorname{ord}_p(g)=\operatorname{ord}_q(g)=M.
\]

If a supplied unit and exponent satisfy

\[
x^2\equiv g^a\pmod N,
\qquad
\gcd(a,M)=1,
\]

solve \(2k=a\pmod M\) and compare \(x\) with its at most two internal root
candidates \(g^k\). The result is a factor, an inert internal root, or

\[
\operatorname{ord}_p(x)=\operatorname{ord}_q(x)=2M.
\]

Thus the last branch produces the next compact certified state \((x,2M)\).
After \(t\) genuine expansions,

\[
M_t=2^tM_0
\quad\text{and}\quad
M_t\mid p-1,\ q-1.
\]

Since \(p<\sqrt N\), no no-factor branch can reach
\(M_t\ge\sqrt N\). Therefore a uniform source that returns a factor or a
non-inert coprime quadratic lift at every surviving state would give a
deterministic polynomial- or quasipolynomial-time factorization algorithm,
according to the source cost. The decoder overhead and number of levels are
polynomial.

Every odd input has the public certified state \((-1,2)\). This is not a
universal viable tower start. The next lift is a square root of \(-1\), which
does not exist if either hidden prime is \(3\pmod4\). Even when it exists,
the common two-adic capacity can end far below \(\sqrt N\). The missing
factor-or-lift source must return a factor whenever the next lift is absent.
It contains the unsolved factor-correlated step.

Every F154 inverse section representative is a legal explicit lift because

\[
s_v^2\equiv Q(v)^{-1}\in H.
\]

For \(N=77\), \(H=\langle9\rangle\), and \(x=26\), the membership scan
already gives

\[
\gcd(26-9^2,77)=11.
\]

This is finite capability only. The theorem does not prove that F154/F156
supplies an external lift, a certified cyclic presentation, or a coprime
exponent at every level.

The statement, proof, hostile audit, blind reconstruction, and final
manifest have SHA-256 hashes
82c67580584de96200be0644b809ddd10f67fa24e5c088bd484342f3b4fee864,
6c4f6254709c25e0c5d673dc24e2ac4af843cb8e2d39adb3a7d18b86b4d756e7,
fd96fa54727beab048c380bc2673600c907ceeafb52613c748b9966c2e392170,
8b8e1213e2a054c2a4ca1481d76365e9e70ad77e20d475d11ae41093d844e837,
and
72cfa89242e113f50d64c0638e9127e4806117caf72e18d699d4d9af67fe9fa6.
No cross-family audit, human audit, or publication-level literature review
has run.

## P145 — sign normalization removes the inert branch, but not the quadratic-root source problem

**Status:** promoted from F160 after hostile audit and independent
statement-only reconstruction. This is a conditional decoder and a sharper
source boundary. It is not a factoring algorithm.

Let \(N=pq\) for distinct odd primes, and let \((g,M)\) be a certified
common-order state. If public data satisfy

\[
x^2\equiv g^a\pmod N,
\qquad
\gcd(a,M)=1,
\]

then deterministic polynomial work returns a proper factor or a certified
common-order state of exact order \(2M\). If \(M\) is even, the supplied
root \(x\) already has order \(2M\) in both hidden fields. If \(M\) is odd,
the unique internal root is \(g^k\), where \(2k\equiv a\pmod M\).
Comparing \(x\) with \(g^k\) factors on a mixed CRT sign. On either global
sign, keeping or negating \(x\) gives the common order \(2M\).

Consequently, every odd common-order state has one source-free public
doubling: negate its public internal root. After that step the order is even.
The unresolved source problem therefore occurs only at even common order.

The decorated section of P138 gives an exact bridge. If it supplies public
\(v,u,a\) with

\[
u^2Q(v)\equiv g^a\pmod N,
\qquad
\gcd(a,M)=1,
\]

then \(x=uz_v\) is the required root, and the factor-or-double decoder
applies. This removes the old requirement that the lift be externally
certified. It does not create the lift: for fixed \(v,a\), finding \(u\) is
the original scalar-root problem after a public change of coordinates.

At even \(M\), the exact local character law is

\[
\left(\frac{g^a}{r}\right)
=(-1)^{(r-1)/M}
\qquad(r=p,q).
\]

Thus Jacobi symbol \(-1\) means that exactly one hidden field admits the
next root, so no scalar root modulo \(N\) exists. Jacobi symbol \(+1\)
means either both fields admit roots or neither does; the Jacobi bit cannot
distinguish them. Pairing two Jacobi-minus-one discriminants \(D\) and
\(E=Dg^a\) does not solve this: multiplication by \(D\) is a public
bijection between roots of \(g^a\) and roots of \(DE\).

The exact remaining theorem is to produce, at every surviving even state,
a factor or one section square-class hit of the displayed form in
deterministic or Las Vegas expected quasipolynomial time. P145 proves no
uniform hit law or hit density.

The statement, proof, hostile audit, blind reconstruction, and final
manifest have SHA-256 hashes
fd232fabd54a66ed03090a3ce4a03905dc1d3e3667b6ba712acee80751751ecc,
cc18b16e96f8363c0eb71bdb85e840bef9d5d9c7c954d5ec1f0b15875d9b17c7,
75b1f930eef9db366bbf8db97c765860673a2b5a6aecd8fe04984c63035d058f,
6d709720c97c89c7c3a7176ca0007c407682400bb2ed368418af597f98f85bc5,
and
ba5bb82f354fcdb04203632b19e5cb7766653afa2b496d1635b02a2ed0ffe8cd.
No cross-family audit, human audit, or publication-level literature review
has run.

## P146 — root-layer saturation does not bound subgroup growth from integer refinement

**Status:** promoted from F159 V2 after fresh hostile re-audit and
independent statement-only reconstruction. This is a structural boundary
with one exact finite capability certificate. It is not a source theorem or
a factoring algorithm.

Let \(N=pq\) for distinct odd primes. For a public subgroup \(H\) given as a
complete list and public roots \(x\) with \(x^2\in H\), a factor-first scan
against \(H\) and then against the first external coset has only three
outcomes:

1. a proper gcd factors \(N\);
2. every root lies in \(H\); or
3. all roots lie in one common index-two extension of \(H\), and both hidden
   local images also have index two.

For a certified common-order generator \((g,M)\) and roots
\(x_i^2=g^{a_i}\) with \(\gcd(a_i,M)=1\), the same alignment needs only a
constant number of exponent candidates and gcds per root. When \(M\) is
odd, every surviving root is a public power of \(g\) or its global negative.
Thus an odd-order root layer has no new modular information.

This saturation law applies only to root residues. A canonical integer
representative can share a proper integer divisor with an old named block.
Factor-free refinement can then name residues far outside the
root-generated subgroup. For any released unit block \(d\), the public
screen

\[
\gcd(d^M-1,N)
\]

has an exact meaning:

- a proper value factors \(N\);
- \(N\) means membership in both old local order-\(M\) subgroups, without
  proving that the two hidden exponents align globally; and
- \(1\) means that adjoining \(d\) strictly enlarges both local subgroups.

At

\[
N=341=11\cdot31,
\qquad
g=70,
\qquad
M=5,
\]

a legal one-record section uses the old square part \(467\), whose canonical
residue is \(126\). The root residues \(126\) and \(295\) are public powers
inside \(\langle70\rangle\), and all direct and membership screens are
null. Integer refinement nevertheless gives

\[
70=14\cdot5,
\qquad
126=14\cdot9.
\]

The complete refined named subgroup is
\(\langle14,5,9,467\rangle=\langle14,5\rangle\). Its global size is \(75\);
its local sizes modulo \(11\) and \(31\) are \(5\) and \(15\). Finally,

\[
\gcd(14^5-1,341)=11.
\]

Thus canonical feedback can create operational subgroup growth even when
its chosen root contains no new modular information. The result does not
prove that such a refinement occurs on every input, that it recurs, or that
the new subgroup admits a compact common-order presentation.

The V2 statement, proof, hostile re-audit, blind reconstruction, and final
manifest have SHA-256 hashes
53584b0152b3eeca7dd37ded6707596ee763e48d7d6c55bb4b335a1ef4c8415f,
527343a68b58a1331f02566c90c1368b7d747e17716c64e1ec7064fe1dab1918,
2f21fd6f4453d5c05f3e2602c6f6e7dee0f5ba52e73be5821afd268d64fdcf80,
35c4ad3c5bf6f4030fb0dff19d885f417e2d1378171f7d9d2d6d5ce4317c3541,
and
a27a65ead4f34f17aa981649bcacef5e67e1ef1214d28a3943caa06ebc6373b7.
The failed V1 history remains preserved. No cross-family audit, human audit,
or publication-level literature review has run.

## P147 — sparse section feedback gives a public quasipolynomial factor path on one frozen-null input

**Status:** promoted from F157 V2 after the registered finite computation, a
failed V1 claim audit, a corrected fresh hostile re-audit, and an independent
blind reconstruction. This is a fixed-input capability result. It is not an
all-input factoring theorem.

F156 publicly enumerates every nonempty subset of its retained relation basis
with support at most

\[
D=\lceil\log_2(n+1)\rceil^2.
\]

On the frozen F111 input

\[
N=3{,}241{,}632{,}473=41{,}011\cdot79{,}043,
\]

the old layer has rank \(11{,}874\). Its direct endpoint screens are null and
its normalized-root image is global. All \(11{,}874\) support-one section
records also miss. The support-two layer contains 65 proper pairs. The first
reported pair has public common-block product \(C=534\) and gives

```text
z = 3183314832
w = 205056
z*w = 1 mod N
gcd(z-w,N) = 41011
gcd(z+w,N) = 1
```

The public F156 algorithm can locate this pair without the factors. Here
\(n=32\), \(D=36\), so every support-two pair is already in its declared
menu. More generally, the public basis size is quasipolynomial and squaring a
quasipolynomial size remains quasipolynomial. Exhaustive lexicographic pair
enumeration followed by the two public gcd screens is therefore a public
quasipolynomial locator on this fixed positive input.

The registered 167.39-second experiment used the disclosed factors only to
index and classify all \(15{,}366{,}751{,}493\) pairs on five fixed inputs.
That index is an implementation acceleration, not the public locator. The
same run found no support-at-most-two hit on four frozen 58-bit inputs. Those
four nulls do not cover support three or higher, later feedback stages, or
new inputs.

Thus sparse products of retained relation lifts have real algorithmic
capability beyond the old frozen decoder. The result gives no success
frequency, useful-pair density, all-input progress law, polynomial-time
algorithm, or public selector asymptotically smaller than exhaustive F156
enumeration.

The frozen V2 result, fresh hostile re-audit, and blind reconstruction have
SHA-256 hashes
`a6278bc71959396e7dbb745c2dbce18f2a4c1df0fffc5c8b5cd09c9daf87b3d4`,
`7e0d5716dc5afcc764f31f0b60c80caa302856137d7b3bc6ed17450de7a8f67a`,
and
`dead670fb8fec3c8cc5493024ab4886d55a1374276697c707199381cafbe12dd`.
The V1 result and failed claim audit remain preserved. The registered
arithmetic evidence was not rerun by the blind reconstruction; its public
certificate and complexity boundary were independently reconstructed.

## P148 — released blocks admit a factor-first quasipolynomial relative-order updater

**Status:** promoted from F161 after hostile audit and independent
statement-only reconstruction. This is a conditional decoder and monotone
progress theorem. It is not a source theorem or a factoring algorithm.

Let \(N\) be odd, with unknown odd prime-power CRT components \(R_j\). Suppose
\((g,M)\) is a public certified common-order state: \(M\) has a supplied
\(B\)-smooth factorization,

\[
g^M=1\pmod N,
\qquad
\gcd(g^{M/\ell}-1,N)=1
\quad(\ell\mid M,\ \ell\text{ prime}),
\]

and \(d\) is one public released unit block. For \(e=1,\ldots,B\), compute

\[
D_e=\gcd(d^{eM}-1,N).
\]

This scan has an exact factor-first meaning.

1. A proper \(D_e\) factors \(N\).
2. If the first non-one value is \(D_e=N\), then the order of \(dH_j\) in
   \((\mathbb Z/R_j\mathbb Z)^\times/H_j\) is exactly the same \(e\) for every
   component, where \(H_j=\langle g\rangle\).
3. If every \(D_e=1\), all local relative orders exceed \(B\).

Equal relative orders are not sufficient. The hidden logarithms of
\(x=d^e\) inside the local order-\(M\) subgroups can differ. A digit-wise
factor-first Pohlig--Hellman calculation either exposes that mismatch as a
proper gcd or returns one aligned exponent

\[
d^e=g^a\pmod N.
\]

The alignment costs at most

\[
\sum_{\ell^c\parallel M}c\ell\le B\log_2M
\]

digit tests. It never scans \(\ell^c\) possibilities.

When \(e=1\), \(d\) is already in the old diagonal subgroup. When \(e\ge2\),
the shared presentation

\[
\mathbb Z^2/\langle(M,0),(-a,e)\rangle
\]

is cyclic of exact order \(Me\). This follows because its image in every odd
prime-power unit group has order \(Me\), and each such unit group is cyclic.
Choose \(s\equiv a\pmod M\), with \(s\equiv1\) at every prime dividing \(e\)
but not \(M\), and choose \(u,v\) with \(ue+vs=1\). Then

\[
h=g^u d^v
\]

has exact common order \(Me\). The usual prime-divisor order screens certify
the new state publicly. The factorization stays \(B\)-smooth.

The naive relative-index rule fails without the logarithm step. At

\[
N=91,
\quad g=-1,
\quad M=2,
\quad d=30,
\]

both local relative orders are three, but \(d^3\) is \(+1\) modulo \(7\) and
\(-1\) modulo \(13\). The alignment gcds return the two factors.

Each genuine enlargement multiplies \(M\) by \(e\ge2\), while the common
order always divides every \(\varphi(R_j)\). Therefore fewer than \(n\)
successful enlargements can occur. One updater call and any full sequence of
successful calls have deterministic quasipolynomial bit cost.

The unresolved branch is exact: the source can keep producing inert blocks
or blocks whose relative orders exceed \(B\) in every component. P148 gives
no bound on either event and no method to construct a useful \(d\). Thus it
turns feedback refinement into a certified state transition, but it does not
close the feedback route.

The statement, proof, hostile audit, blind reconstruction, and final manifest
have SHA-256 hashes
c999958e6b1cce04b7aa4fbf03e7b233a57c4461da66a4ba68c46cf2aaba4a32,
409bdd11bdff1dc0b571b6169f669186e16b3aac04ad7566a009f14ddeb41a27,
7a560d27491db84b27d9308bf9daf126f1b60e61e7061e71a0581ae57f8090b0,
e3a9e51bd7ed1d4d4379158c5f6945bd1bda69dbbbedc7bf91ebef447079b16e,
and
de6812c57587fcfa96ade93c1f734e8959ae117cf40d1ddef2a7d5cf71de0479.
No cross-family audit, human audit, or publication-level literature review
has run.

## P149 — pure decorated-PFR structure is exactly the public parity section

**Status:** promoted from F163 after hostile audit and independent
statement-only reconstruction. This is an exact obstruction to one
Babai/PFR splice. It is not a factoring algorithm and does not cover PFR on
integer presentations, carries, block incidences, sizes, or provenance.

Use the P138 decorated square-class group after quotienting by the two global
signs. Let \(A\) be a root-aware-deduplicated set of retained decorated lifts,
let \(H=\langle A\rangle\), let \(W\) be its public parity projection, and let
\(K\) be the non-global root kernel. There is an exact dichotomy:

1. \(H\cap K\ne0\), in which case binary elimination reconstructs a
   non-global square root of one and factors \(N\); or
2. the parity projection

   \[
   \pi|_H:H\longrightarrow W
   \]

   is a public isomorphism whose inverse is the already computed P138
   section \(h\).

On the second branch, every additive word equality is preserved exactly.
For every \(k\ge1\),

\[
kA\longleftrightarrow k\pi(A),
\qquad
|kA|=|k\pi(A)|.
\]

Thus every intrinsic Freiman relation, additive energy, affine-subspace
containment, and coset/subspace cover inside \(H\) is only the public lift of
the corresponding parity structure. Applying an algorithmic PFR theorem to
the decorated group cannot create new root information after the consistency
test has selected this branch.

Both natural PFR outcomes can remain root-global. If
\(W=\mathbb F_2^d\) and \(e_1,\ldots,e_d\) is a basis, then

\[
B_1=\{h(0),h(e_1),\ldots,h(e_d)\}
\]

already generates \(h(W)\), while

\[
|B_1+B_1|=1+d+\binom d2.
\]

Repeated Hamming-ball doubling gives real cardinality growth but stays in
the same known graph. At the other extreme, every subspace \(U\le W\) and
every identity-free affine coset satisfy doubling one, yet also remain in
that graph.

F163 realizes both extremes with exact P142 canonical-inverse
section-completion records. CRT and Dirichlet supply independent prime
blocks and simultaneous roots. Every dependency has global normalized root,
and every displayed endpoint sign screen is one. This is a factor-assisted
realizability family, not a bare-\(N\) source. The records need not be the raw
two-endpoint values \(z\iota_N(z)\); this distinction is explicit.

The useful remaining target must use data not preserved by the decorated
group isomorphism. It can force two supplied sections to disagree on an
overlapping parity vector, or prove that a section-consistent PFR cell forces
a bounded chain of integer refinements, relative-order updates, or another
public capacity decrease. Pure additive structure alone cannot supply that
step.

The statement, proof, candidate manifest, hostile audit, and blind
reconstruction have SHA-256 hashes
`82ff2a0fef918e3c4e992ca70b334656fcd661146e4b61dac7c871c0216dbd95`,
`534f1e4903b76c63f79d6e13e4f5dd64952fa6a94aaf811604cd027220c41007`,
`d695d645220d80afe0df62292b4054f58890933178608258184351b31279c581`,
`7936183bd7e0a33333de797c66f82c2890155559127aa31d5884de2e6718b262`,
and
`f56315c47dcafe51cad8fe3b9654d0bd05e40cf96b2940364307519d0c4528d6`.
No prior-art novelty review or human audit has run.

## P150 — F161 common-order growth does not require hidden-log alignment

**Status:** promoted from F166 after a fresh proof-only hostile audit and an
independent statement-only reconstruction. This refines the minimum-work
interpretation of P148. P148 remains a valid stronger factor-or-relation
procedure.

Start after an F161 common return. Thus \((g,M)\) has exact order \(M\) in
every unknown odd prime-power CRT component, and the released unit \(d\) has
the same local relative order \(e\) modulo \(\langle g\rangle\) in every
component. In particular,

\[
d^{eM}=1\pmod N.
\]

Use the known factorization of \(eM\) to compute the exact global order
\(m=\operatorname{ord}_N(d)\) by divisor stripping. For every prime
\(\ell\mid m\), test

\[
E_\ell=\gcd(d^{m/\ell}-1,N).
\]

A proper value factors \(N\). If all values are one, then \(d\) has exact
order \(m\) in every hidden component. Local unit groups are cyclic, so

\[
\boxed{\operatorname{lcm}(M,m)=Me}.
\]

This identity includes shared prime factors. It uses only orders, not the
hidden exponents in \(d^e=g^{a_j}\).

Put \(L=Me\). For each prime \(\ell\mid L\), select the
\(\ell\)-primary component of whichever public element \(g\) or \(d\) has
the larger \(\ell\)-adic order. Multiply these selected components. The
resulting public word \(h\) has exact order \(L\) in every hidden component.
The usual prime-divisor screens certify \((h,L)\). Thus hidden-log alignment
is not needed only to construct the next common-order state.

The distinction from full alignment is real. At

\[
N=341,
\quad g=202,
\quad M=5,
\quad d=277,
\quad e=2,
\]

\(d\) has common local order ten. The lcm construction gives \(h=139\) of
common order ten. But

\[
|\langle g,d\rangle|=50,
\qquad
|\langle h\rangle|=10,
\qquad
\gcd(d^2-g,N)=11.
\]

Thus the lcm state preserves the generated subgroup in each hidden
component, but it need not preserve the full global named subgroup. A safe
algorithm can use \((h,L)\) as its next order state while retaining \(g\),
\(d\), and their provenance. Alignment is still needed for its extra factor
test, an exact global relation, global subgroup compression, and F164-style
rank-volume accounting. When \(e=1\), the shortcut gives no growth and does
not prove global membership.

The update is deterministic quasipolynomial time. It does not construct a
released block, force a bounded common return, or control the \(e=1\) and
above-cap branches. The source problem is unchanged.

The statement, proof, clean proof-only hostile audit, blind reconstruction,
and final manifest have SHA-256 hashes
`5b245ddc902f300b89dab11c61d06dfffb2deef09d01182f4f8e6f7cce608615`,
`bba045350ed11b8756d11c233d909f4f14a0225b19b5d7bab74296ced04ec4a6`,
`f97e6bc0bd80c7ee19b0d83a951e8de716e7055db5261c0e45b4d2190659c1fe`,
`756275ebc55c14df7b091edfbd5e4c32afa26c585c978684f7f70111fd2304ce`,
and
`b13a23104aa50631158ce4f7f5a011024fe669d603c6255b41112c839eb79584`.
The first audit's unregistered finite check is preserved as a workflow
failure and is not used as evidence. No prior-art novelty review or human
audit has run.

## P151 — quotient fingerprints give a rank–capacity updater

**Status:** promoted from F164 V2 after a fresh hostile re-audit and an
independent statement-only reconstruction. This is an exact finite-bank
state theorem. It is not an all-input source law or a factoring algorithm.

Let \((g,M)\) be a certified common-order state for an odd composite \(N\),
and let \(d_1,\ldots,d_t\) be public unit blocks. For an exponent word \(v\),
define its quotient fingerprint

\[
F(v)=\left(\prod_i d_i^{v_i}\right)^M\pmod N.
\]

In every unknown odd prime-power CRT component, the kernel of the
\(M\)-th-power map is exactly \(\langle g\rangle\). Hence two fingerprints
are equal locally exactly when their words occupy the same quotient coset.
A gcd of their public difference therefore has a factor-first trichotomy:
it returns a proper factor, proves equality in every component, or proves
inequality in every component.

After exact public deduplication, a bank of \(\kappa\) fingerprints certifies
the local capacity bound

\[
|\langle g,d_1,\ldots,d_t\rangle_{R_j}|\ge M\kappa
\]

in every hidden component. When one new block \(d\) is introduced, compare
the layers \(d^eT\), \(0\le e\le B\), against all earlier layers.

- A proper difference gcd or hidden-log mismatch factors \(N\).
- A first common collision gives one aligned integer relation whose new-block
  coefficient is nonzero. It is independent of all old relation rows.
- If no collision occurs, all \(B+1\) layers are disjoint in every component,
  so the certified capacity multiplies by \(B+1\).

Introduce blocks one at a time. Let \(t\) be their count, let \(r\) be the
rank of the retained first-collision rows, and put \(\delta=t-r\). Then

\[
\boxed{\kappa\ge(B+1)^\delta}.
\]

Let \(L\) be the complete aligned integer relation lattice, including the
base relation of order \(M\). If \(L\) has full rank and index \(D\), every
hidden generated subgroup is a quotient of the public presentation of order
\(D\). If

\[
\boxed{D=M\kappa},
\]

the lower and upper bounds meet. Smith normal form then gives one public
element of exact common order \(D\). The equality is essential. Rank or many
relations alone do not certify closure.

The obstruction is exact. At \(N=341\), the canonical-inverse source releases
the pairwise-coprime blocks \(337\) and \(277\). Each has local relative
order five against \(\langle-1\rangle\), above the cap \(B=2\), but

\[
277\cdot337^2\equiv-1\pmod{341}.
\]

The second block adds an aligned relation rather than a second independent
quotient direction. Arbitrarily many blocks can behave this way inside one
synchronized cyclic quotient. Thus block count and individual above-cap
orders do not force capacity growth or a factor.

The updater has deterministic quasipolynomial cost whenever the complete
encoded transcript has quasipolynomial bit length. A cap only on
\(\kappa\) is not sufficient because collision rows, coefficients, word
occurrences, and provenance can still grow.

The remaining alternatives are exact: force enough disjoint layers, force
enough aligned relations for \(D=M\kappa\), or certify relative order
against the full previously generated subgroup. F164 proves none of these
source laws.

The V2 statement, proof, hostile re-audit, blind reconstruction, and final
manifest have SHA-256 hashes
`8e47a9e249ff7f6fd7996664daddbbd53ace7dafd1e85b159ad20502a6d6fa19`,
`53488652f65c7138412389a584e6a4dd7fa5a9367191c8d5bbc1558f7a4bf2bb`,
`bb84972f5d5c82d28c9d15e63228f4a91d82ae98489582100b8d496c6d97e047`,
`1d08428330c288933ee71e10c13cc8fa7d07b165cf27866da2ffe8fab49d0647`,
and
`b3a3af26d02b2acf1b6a0759f6f7065fbeb99b0b7cfff03764aa272517f189a8`.
The V1 failure history remains preserved. No prior-art novelty review,
cross-family audit, or human audit has run.

## P152 — signed inverse collisions admit a near-linear public batch locator

**Status:** promoted from F162 V2 after a fresh hostile re-audit and an
independent statement-only reconstruction. This is a locator for existing
pair collisions, not a collision-existence theorem or factoring algorithm.

Let \(a_1,\ldots,a_r\) be an explicit public list of units modulo an arbitrary
composite \(N\). Deduplicate their canonical residues to a set \(A\) and form

\[
P(X)=\prod_{b\in A}(X-b)\in(\mathbb Z/N\mathbb Z)[X].
\]

For each \(a\in A\) and sign \(\varepsilon\in\{\pm1\}\), put
\(x=\varepsilon a^{-1}\pmod N\). If \(x\notin A\), evaluate \(P(x)\).
If \(x\in A\), evaluate

\[
P'(x)=\prod_{\substack{b\in A\\b\ne x}}(x-b).
\]

The derivative removes exactly the one improper global partner
\(ab\equiv\varepsilon\pmod N\) and keeps every other candidate. Equal-value
source positions are covered by the unconditional self screens
\(\gcd(a^2-\varepsilon,N)\).

For every candidate pair,

\[
\gcd(ab-\varepsilon,N)=\gcd(b-x,N).
\]

Therefore any proper signed pair-product collision divides the corresponding
ordinary or derivative evaluation. If the aggregate gcd is already proper,
return it. If it equals \(N\), descend a scalar subproduct tree of the
differences \(x-b\). At a distinct canonical leaf, the nontrivial gcd is
strictly smaller than \(N\). This localization works for arbitrary
composites and prime powers.

All polynomial divisors in the product and remainder trees are monic.
No coefficient inverse is required over \(\mathbb Z/N\mathbb Z\). Including
the mandatory cost of reading, canonicalizing, and deduplicating the
explicit \(r\)-position input, the method is soft-linear in the encoded
list size up to polynomial coefficient arithmetic. A quasipolynomial-size
explicit list therefore remains quasipolynomial.

For the F156 shared-block source, normalize every owner at a declared
intersection \(T\) by \(a_{i,T}=q_iC_T^{-1}\). When \(T\) is the pair's
exact block intersection, the product of the two normalized values is
exactly its corrected star value. Enumerating all intersections of
polylogarithmic size keeps the complete batch quasipolynomial.

On the fixed F157 input \(N=3{,}241{,}632{,}473\), 28 certified hits have
empty block intersection. The single raw batch therefore contains a public
pair whose product gives

\[
\gcd(2{,}922{,}074{,}762-1,N)=41{,}011.
\]

This removes the quadratic pair locator from that channel. It does not
explain why a collision exists. The four frozen controls rule out only the
adjusted support-at-most-two source, not the larger raw batch.

The V2 statement, proof, hostile re-audit, blind reconstruction, and final
manifest have SHA-256 hashes
`89eb6821c394e70b779a014212a1d5ac50f3658ccfe6ffd21248a27f244b4899`,
`582c100d7e39f85bd1cd4c154e77d6dea9de98d91581db4a6a1771f7ec3cfaa1`,
`9e3e9ce76f562b547ca4a4aaf9216e2f019efe4a431ab1b107099a56aa4745a4`,
`e4faaabb53a64a3c57638677a5a629b39135836ca9732aabccbb653bc5b9d1fe`,
and
`7dbe46bfeb0eed675492b2f69c6c76aafd75c90fc9eb5836d04d994028a7605e`.
The V1 failure history remains preserved. No prior-art novelty review,
cross-family audit, or human audit has run.

## P153 — the smooth-order decoders rescale to QP, but an infinite stable core remains

**Status:** promoted from F168 after hostile audit and independent
statement-only reconstruction. Parts I--III are exact complexity rescalings
of P87 and P92--P99. Part IV is a new infinite-family theorem. This is not an
all-input factoring algorithm.

Let \(n=\lceil\log_2(N+1)\rceil\), and let every numerical cap, explicit
generator list, and encoded transcript have size

\[
2^{(\log n)^{O(1)}}.
\]

Then the complete punctured bank for

\[
M_B=\operatorname{lcm}(1,\ldots,B)
\]

has QP construction and evaluation cost. Indeed,

\[
\operatorname{bitlen}(M_B)=O(B\log B),
\]

and the bank contains at most \(B+1\) exponents. Prime scans, modular powers,
and breadth-first subgroup enumeration through a QP cap also have QP bit
cost. Therefore every exact bounded-component or bounded-image algorithm in
P87 and P92--P97/P99 remains valid after replacing its polynomial cap by any
fixed QP cap, provided its full input and state also remain QP. The missing
separator and localizer promises do not follow from this rescaling.

There is one unconditional bare-\(N\) promise class. For

\[
N=pq,\qquad
g=\gcd(p-1,q-1),\qquad
A=\frac{p-1}{g},\quad B=\frac{q-1}{g},
\]

if \(\min(A,B)\) is QP, uniform sampling of
\(a\in\{1,\ldots,N-1\}\), followed by

\[
\gcd(a,N),\qquad \gcd(a^{N-1}-1,N),
\]

is a Las Vegas expected-QP splitter. On the unit branch, the exact success
density is

\[
\delta_N=\frac1A+\frac1B-\frac2{AB},
\]

which is at least the reciprocal of a QP bound under the promise.

The promise cannot be made universal by QP rescaling alone. There is an
absolute constant \(c>0\) and an infinite family of distinct odd semiprimes
\(N=pq\) with

\[
p<q,\qquad \gcd(p-1,q-1)=2,
\]

such that, for \(A=(p-1)/2\) and \(B=(q-1)/2\), there are primes
\(r\mid A\) and \(s\mid B\) satisfying

\[
r,s\ge 2^{cn},
\qquad
\gcd(AB,N-1)=1.
\]

The construction uses reduced arithmetic progressions, Bertrand's theorem,
CRT, and Linnik's theorem. The length link is essential: both powered local
orders contain a prime component exponential in the actual input length.
Every exponent supported on primes dividing \(N-1\) acts as an automorphism
on the P97 rectangle. The direct uniform density satisfies

\[
\delta_N=2^{-\Omega(n)}.
\]

Thus every fixed QP number of direct samples still has exponentially small
total success on this family. This conclusion is asymptotic after removing a
finite prefix for each fixed QP cap. It does not cover adaptive words,
canonical integer feedback, retained relations, or other factoring methods.

The statement, proof, self-audit, hostile audit, blind reconstruction, and
final manifest have SHA-256 hashes
a30c71c6bf8d6b715b84e4abb78cc5c47681e1c7f95971e85e610606176dade0,
2b580ac93b52cbea6cf1a42d57cb0c74de52072c04326a62cf641de304f6d38f,
da8a8b44c5896f55d2fd32e9347ec90ad8bbce1f508ea95a25b7093ee034825c,
6cd284ad24515064202cc264d261367c394b4086005d0da2b6350ac8b0945660,
6aa02c054c03a93e1f313820012599bce3975afe02333f18b6e63da2d5af4bf8,
and
99079cdc64f7cd115ff31095e2b6dfff67c1dceca26cebdca15fbd0ee2e09ff9.
No research computation, cross-family audit, human audit, or publication-level
literature review has run.

## P154 — complete quotient closure gives factor, exact state growth, or certified capacity

**Status:** promoted from F167 after hostile audit and independent
statement-only reconstruction. This is a conditional factor-first decoder and
state updater. It is not a source theorem or a factoring algorithm.

Let \(N\) be odd. Let \((g,M)\) have exact order \(M\) in every unknown
prime-power CRT component. Let \(d_1,\ldots,d_t\) be a frozen public list of
unit blocks. The state screens also force \(\gcd(M,N)=1\), including for
nonsquarefree \(N\).

For one block \(d\), put

\[
\Lambda_B=\operatorname{lcm}(1,\ldots,B),
\qquad
A_d=\gcd(d^{\Lambda_B}-1,N).
\]

There are three exact outcomes.

1. A proper \(A_d\) factors \(N\).
2. If \(A_d=N\), divisor stripping either factors \(N\) or certifies one
   exact local order \(m\) for \(d\) in every component. P150 then constructs
   a common-order state of order \(\operatorname{lcm}(M,m)\).
3. If \(A_d=1\), every local absolute order contains a full prime-power
   component larger than \(B\). A subsequent relative-order scan either
   factors, returns a bounded common relative order and state growth, or
   certifies that both the absolute primary component and the relative order
   exceed \(B\) in every component.

The complete block list has a stronger joint decoder. Form the fingerprint
group

\[
F=\langle d_1^M,\ldots,d_t^M\rangle\pmod N
\]

by breadth-first search. Compare each new value with the stored table through
gcds of differences. A proper gcd factors \(N\). On the no-factor branch,
all stored distinct fingerprints remain distinct in every hidden component.

If the table closes with

\[
|F|=\kappa\le C,
\]

then projection identifies \(F\) with every local quotient

\[
\langle g,d_1,\ldots,d_t\rangle/\langle g\rangle.
\]

All these quotients are cyclic of exact order \(\kappa\). A table generator
retains a public word \(a\) with fingerprint \(a^M\). P150 therefore returns
a factor or a new exact common-order state of order

\[
\boxed{M\kappa}.
\]

This is strict growth when \(\kappa>1\). When \(\kappa=1\), it proves only
local membership in \(\langle g\rangle\), not one globally aligned
membership relation.

If the search instead stores \(C+1\) distinct fingerprints, every hidden
generated subgroup has size at least

\[
\boxed{M(C+1)}.
\]

This is a certified capacity lower bound. It is not a factor and does not
prove that different blocks give independent quotient directions.

Hidden-log alignment is optional for the state update. It remains necessary
when the algorithm wants its extra factor channel, explicit global relations,
or compression of the complete named subgroup. After strict state growth,
all fingerprint tables must be rebuilt because the quotient kernel changed.
Exact relations and endpoint occurrences must remain in two separate
ledgers: a root-aware deduplicated relation ledger and a
presentation-complete endpoint ledger.

With QP numerical caps and a QP bound on the full encoded transcript, one
updater call and every fixed-depth source composition have deterministic QP
cost. Fewer than \(n\) strict common-order enlargements can occur. The exact
surviving obstruction is a synchronized cyclic quotient larger than the cap,
with no forced collision, independent capacity increase, aligned lattice
closure, or non-global root.

The statement, proof, self-audit, hostile audit, blind reconstruction, and
final manifest have SHA-256 hashes
e96e12303520b40c459b92ab192de48f7ffc4829daa20c60686007aba8884aad,
8e639c631355951a1c9656fbf99df46320a4c75bf4ef745949f01705b4df6060,
a7a65c9306a3efdcd64f82b26353f78285e0d8aba82140261cb9d5f926af965f,
6c60b057761dc6e521731a37ef7a9038a2b9de8b1552dcecbdaf6154bd89ca93,
0a74b6b6a59810b128282012a2f606065df8d80d10d5563ca0f0d9d7d2678e7d,
and
423f28ab0db7822d59d9f40adff94d86336d4f9d17683eff394a9be33c64d3a7.
No research computation, cross-family audit, human audit, or publication-level
literature review has run.

## P155 — every fixed number of sparse exact-value feedback layers remains quasipolynomial

**Status:** promoted from F165 after a registered exact finite reconstruction,
a hostile proof audit, and a fresh statement-only reconstruction. This is a
cost theorem plus finite capability evidence. It is not a growing-depth bound,
a presentation-complete source theorem, or a factoring algorithm.

Let

\[
n=\lceil\log_2(N+1)\rceil,
\qquad
L=\lceil\log_2(n+1)\rceil.
\]

Assume that the explicit base relation transcript has
$2^{L^{O(1)}}$ total bits and at most $2^{CL^a}$ records. At each layer,
freeze a deterministic selected column basis, enumerate every nonempty subset
of support at most

\[
D\le L^b,
\]

retain at most one canonical exact-value record per attempt, rebuild the full
multiplicity-aware gcd/perfect-power block basis, compute a complete binary
kernel basis, and test the normalized root of every basis dependency.

If $R_h$ is the retained record count, one layer makes at most

\[
T_h\le(D+1)(R_h+1)^D
\]

attempts and satisfies $R_{h+1}\le R_h+T_h$. Every generated residue is
reduced modulo $N$, every exact value is below $N^2$, and compact parent
references keep the complete transcript at quasipolynomial bit length.

Complete factor-free refinement is polynomial in that explicit transcript.
A multiplicity-aware gcd split strictly decreases

\[
\Phi=\sum_{\text{distinct live }q}\log_2q,
\]

and exact maximal-perfect-power extraction needs only deterministic integer
root tests. The final parity matrix, a complete kernel basis, every exact
basis root, both signed gcd screens, zero columns such as $A=1$, and the next
selected basis are also polynomial in the transcript.

Therefore, for every fixed integer $H$ independent of the input,

\[
\boxed{\text{time and space through layer }H
=2^{L^{O_H(1)}}.}
\]

Here “complete kernel” means computing a basis and decoding each basis
member. Enumerating all $2^{\dim\ker}$ kernel vectors is neither required nor
covered. The proof does not give one fixed QP exponent when $H$ grows with
$n$.

The registered depth-two reconstruction exactly matched the original F165
transcript on 64 semiprimes and 192 snapshots: 15,644 attempted candidates,
3,220 exact values, 4,323 factor-free blocks, and 3,089 selected columns. Of
the 64 inputs, one already factored at the base through $N+1=10008^2$.
All 63 base-null inputs remained direct/root-null through both feedback
levels. Nevertheless, level one added 315 exact values, gained total parity
rank 251, and strictly split 67 old blocks; level two added 310 exact values,
gained total rank 310, and strictly split 69 old blocks. Thus exact-value
feedback creates real new integer structure, but rank and refinement growth
alone do not force a useful root.

The exact scope excludes endpoint-presentation completeness, a success
density, a minimum useful depth, a growing-depth QP bound, and an all-input
factor theorem.

The statement, audited proof draft, hostile audit, fresh blind
reconstruction, and final exact comparison report have SHA-256 hashes
`1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd`,
`39a36e862162d405d15943f59995010c1471e6af8baef6e2b7b9d7f984a9b380`,
`982c667b7d7fde8b3832ea4db131341835fee26ba734d07d23633622be9c83e4`,
`8428aadcbf8d8d494c6cbda9fd5767d49eaeae6707e524056a775cd8024ed8fa`,
and
`fa48cba13d3317f4d7d4417505e27e5b8a512ced3c52e06f79e90dc675ca2330`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P156 — ordinary and Jacobi-torus common orders form an almost multiplicative CRT modulus

**Status:** promoted from F170 after hostile audit and fresh statement-only
reconstruction. This is a conditional decoder and terminal theorem for
distinct odd semiprimes. It is not a source theorem or a factoring algorithm.

Let $N=pq$ with distinct odd primes. Suppose a public ordinary unit has
exact order $A$ modulo both hidden primes, and a public norm-one point for
one Jacobi-minus-one discriminant has exact order $B$ in both hidden local
tori. If $\epsilon=(D/p)=-(D/q)$, then

\[
A\mid p-1,\quad A\mid q-1,
\qquad
B\mid p-\epsilon,\quad B\mid q+\epsilon.
\]

Therefore

\[
\boxed{A\mid N-1,\qquad B\mid N+1,\qquad \gcd(A,B)\mid2.}
\]

Starting both channels at the public element $-1$ makes both orders two.
Every later exact strict update preserves

\[
\gcd(A,B)=2,
\qquad
L=\operatorname{lcm}(A,B)=AB/2,
\]

and multiplies $L$ by exactly the update factor. The smaller prime lies in
one of the two computable generalized-CRT classes

\[
x\equiv1\pmod A,
\qquad
x\equiv\pm1\pmod B.
\]

Thus $L\ge\sqrt N/Q(n)$ gives a deterministic QP factor search. Under
$p<q<2p$, the single orientation-free class for $p+q$ gives the sharper
sufficient threshold $L\ge\sqrt N/(8Q(n))$.

P154's quotient-fingerprint updater transfers to the torus by using both
coordinates in every equality gcd. A closed table of size $\kappa$ gives
an exact torus common-order update $B\mapsto B\kappa$; a table exceeding
its cap certifies capacity only. The explicit $N=143$ example has local
orders five and seven and shows why capacity is not an order modulus.

The theorem supplies no source of strict updates. Prime powers, more than
two hidden components, and complete factorization remain outside its scope.

The statement, proof, hostile audit, blind reconstruction, and manifest have
SHA-256 hashes
`268d55df4968a25eae7d50207c4cde54112706cd8a8e2860b699cc3c5d18ec99`,
`9f81fc1539b7fe84774a7fd4d5e57ad51dcce936d4b3a5958488001ff5ee9d9b`,
`0c6d103a61366fab1db5bd67098ed03aa56dfbeb438a8adf38bfb51466857c44`,
`97f4df96c64e2031eba53a586c9a2b701b8275d1a54b96f38a7feeb69b228f16`,
and
`847a12d28ae9961d0d7dcf906d74333f0a6683bdb53e827de63ca0f4c64da7bb`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P157 — complete small carry-row coverage does not force parity closure

**Status:** promoted from F171 after hostile audit and independent
statement-only reconstruction. This is a selected-source obstruction. It is
not a complete-source null or a factoring lower bound.

For every prime $r\nmid N$, a canonical carry value

\[
P_k=1+kN
\]

contains row $r$ exactly when

\[
k\equiv -N^{-1}\pmod r.
\]

A numerical difference cover only repeats some residue class. It does not
force this occupied class, odd valuation, a final rank defect, or a
non-global normalized root.

There is an infinite trial-hard family with a selected bank of

\[
m=4R=\Theta(n/\log n)
\]

canonical relations carrying exactly $1,\ldots,m$. Their public prime
endpoints $g_k\le n$ satisfy

\[
g_k\iota_N(g_k)=1+kN.
\]

Every selected endpoint sign screen is null. Every rational-prime row
$r\le R$ has at least two exact valuation-one selected columns. Yet each
column has its own private endpoint-prime row $g_k>m$ at valuation one.
Those rows form an identity submatrix, so the full selected parity matrix has
rank $m$ and zero kernel even though its restriction to rows at most $R$
has nullity at least $m-\pi(R)$.

Thus carry coverage is a locator, not a source-closure theorem. The result
does not prevent a richer complete adaptive grammar from later reusing the
private rows.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`22ee980dca180518170dde7d94df3a6a9225fffc880adf316738de6135e87b43`,
`ab9883b425c5957839a0d5a79bf235897360691854ab28b2a8d5ee030251c01c`,
`90d4a63148d5dee7c4ebfd231d1d8076de90216f229a2b7c8ee7ee0745f52447`,
and
`8402bf3db3c2bb4fc783a50dda47f14d2a516c3be67621f32a41838ac31a80a1`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P158 — dual ordinary/torus common-order capacity can remain constant on trial-hard semiprimes

**Status:** promoted from F172 after hostile audit and fresh statement-only
reconstruction. This is an infinite-family obstruction to one terminal
mechanism. It is not a factoring lower bound or an all-input impossibility
result.

For every prime $p\equiv1\pmod3$, write

\[
p^2-1=2^u3^vM,\qquad \gcd(M,6)=1,
\]

and set $H_p=8p3^vM$. The reduced CRT class

\[
q\equiv3\pmod8,\quad q\equiv1\pmod p,\quad
q\equiv4\pmod{3^v},\quad q\equiv2\pmod M
\]

contains a prime $q\le H_p^{O(1)}$ by Linnik's theorem. Every such prime
satisfies $q>2p$. For $N=pq$, the four shifted gcds obey

\[
\gcd(p-1,q-1)=6,\qquad
\gcd(p+1,q-1)=2,
\]

\[
\gcd(p-1,q+1),\ \gcd(p+1,q+1)\in\{2,4\}.
\]

Hence every ordinary element having the same exact local order $A$ in both
hidden fields has $A\mid6$. Every quadratic norm-one torus point having the
same exact local order in both components has order dividing $6$, $4$, $2$,
or $4$, according to its two Legendre orientations. Even after retaining all
Jacobi-minus-one orientations and all available common orders, their combined
least common multiple is at most

\[
\boxed{12}.
\]

Moreover $H_p<8p^3$, so Linnik gives $q=p^{O(1)}$. Thus the input length
satisfies $n=\Theta(\log p)$, and both hidden factors are
$2^{\Theta(n)}$. For every fixed QP bound $Q(n)$, eventually

\[
12<\sqrt N/Q(n).
\]

Therefore the P156/F170 terminal strategy cannot be universal if it relies
only on accumulating exact common orders. The result leaves open, and may
even favor, factor extraction from unequal local orders, quotient
fingerprints, alignment failures, or any non-order decoder.

The statement, proof, self-audit, hostile audit, blind reconstruction, and
manifest have SHA-256 hashes
`d2ff244f1fb28e00ba262fdb89cd5a23b7b75954586bfb998ffd188db4a8ed9f`,
`b23989a19a23653dab9946dca55888384a2c4493184878a3dfac68ec9c067a21`,
`2ac2410cdedfeafc98d997bac7a3c7cae11e8613f34a34dd2e920d8d0410bf9d`,
`f5c7d24a300ecd6f55f17f441d6f745bc27ae59a19f8d6fffe12d820cdc0d528`,
`86595e81177051fead3e6e4c805157fb893f72ad93d0f8012186fd12fb7f92a0`,
and
`86b1d8e6bb6715d86381230e5669e2ca3f50078a557f735479f41780aae8cc81`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P159 — every surviving QP-hard ordinary source normalizes to base two

**Status:** promoted from F176 V3 after fresh hostile re-audit and independent
statement-only reconstruction. This is a uniform deterministic QP reduction
for arbitrary odd composites. It is not an all-input factoring algorithm.

Let

\[
n=\lceil\log_2(N+1)\rceil,
\qquad n\le B<N-1,
\qquad C\ge n,
\]

where \(B\) and \(C\) are any fixed numerical quasipolynomial bounds. Put

\[
\Lambda_B=\operatorname{lcm}(1,\ldots,B),
\qquad
A=\gcd(2^{\Lambda_B}-1,N).
\]

If \(A\) is proper, it factors \(N\). If \(A=N\), factor-first divisor
stripping with the known factorization of \(\Lambda_B\) either factors
\(N\) or certifies one exact local order

\[
m=\operatorname{ord}_{p^a}(2)
\]

in every hidden prime-power component. When \(m>n\), this is already a
factored exact common-order state. When \(m\le n\), size forces

\[
m=n,
\qquad
N=2^n-1.
\]

Composite \(n\) gives the explicit proper divisor \(2^{n/\ell}-1\) for a
prime \(\ell\mid n\). Prime \(n\) is odd, and \(-2\) then has exact common
order \(2n>n\).

It remains to consider \(A=1\). For every hidden prime-power component
\(R_j\), this certifies

\[
\sigma(\operatorname{ord}_{R_j}(2))>B,
\]

where \(\sigma(t)\) is the largest prime-power divisor of \(t\). Scan

\[
G_e=\gcd(2^{2e}-1,N),
\qquad 1\le e\le C.
\]

A proper value factors. If the first global return is \(G_e=N\), all local
orders of the coset \(2\langle-1\rangle\) equal \(e\); stripping the known
annihilator \(2e\) either factors or constructs an exact common-order state
of order \(2e>B\). If every \(G_e=1\), then every local sign-quotient order
exceeds \(C\).

Thus the procedure returns exactly one of

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{factored exact common-order state of order }>n
\quad\lor\quad
\text{normalized hard block }2
}
\]

and the hard branch satisfies both

\[
\sigma(\operatorname{ord}_{R_j}(2))>B,
\qquad
\operatorname{ord}_{R_j^\times/\langle-1\rangle}
  (2\langle-1\rangle)>C
\]

for every hidden component. Constructing \(\Lambda_B\), divisor stripping,
the relative scan, verification, and complete-factor recursion all have
uniform deterministic QP bit cost. The exact remaining case is the one
normalized base-two branch; P159 does not factor it.

The statement, proof, self-audit, hostile re-audit, blind reconstruction,
and manifest have SHA-256 hashes
`c7c4c9963c078dc1ba4d68a86a81fa4cd9e46626ab6fa9d8645779b92d6b4b1f`,
`6100a81be386458c9e875ed5dc042ee9906ed3691c57fcd2950f27485be4316a`,
`8c40f7d97410db1b06733e71bba30dd131332f8577a49e415018551f45ae7534`,
`cbeaa46e1a73639b5ec62bde181c5545fd05bf06aacdeba09d30e332576d4051`,
`a22fb4801c386f07005e88c83bac741e932217c2b1c42bfc2b1595bb796fdadf`,
and
`198805cf6df897c08d081c4d7646b8880849996e0c428a15d5f34bd221ad543d`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P160 — the surviving local orders can be made coprime to the input

**Status:** promoted from F178 after hostile audit and independent
statement-only reconstruction. This is a uniform deterministic QP
postprocessor for the P159 hard branch. It is not an all-input factoring
algorithm.

Let \(N=\prod_jR_j\) be the hidden odd prime-power decomposition and

\[
n=\lceil\log_2(N+1)\rceil.
\]

On P159's hard branch,

\[
e_j=\operatorname{ord}_{R_j}(4)>C\ge n.
\]

Choose any fixed QP cap \(T\ge\max\{n,2C\}\), and put

\[
E=N^n,
\qquad
y=4^E\bmod N,
\qquad
f_j=\operatorname{ord}_{R_j}(y)
    =\frac{e_j}{\gcd(e_j,E)}.
\]

Every prime dividing \(N\) occurs in \(E\) to exponent at least \(n\),
while \(e_j<N<2^n\). Thus \(E\) removes the full primary part supported on
every hidden rational prime, and

\[
\gcd(f_j,N)=1
\qquad(1\le j\le s).
\]

The identity screen \(H=\gcd(y-1,N)\) factors if it is proper. If \(H=N\),
let \(p\) be the least prime divisor of \(N\). Then
\(\operatorname{ord}_p(4)\) divides both \(p-1\) and \(N^n\). Its prime
divisors would have to be both smaller than \(p\) and prime divisors of
\(N\), so its order is one. Hence \(p=3\), and \(\gcd(3,N)\) is proper.
The surviving branch therefore has \(f_j>1\) for every component.

Next construct

\[
\Lambda_T=\operatorname{lcm}(1,\ldots,T)
\]

with its complete factorization and test

\[
J=\gcd(y^{\Lambda_T}-1,N).
\]

A proper \(J\) factors. If \(J=N\), factor-first divisor stripping either
factors or returns one exact common local order \(m\). If \(m>n\), this is
the required factored state. If \(m\le n\), the least hidden prime satisfies
\(\operatorname{ord}_p(4)=m\), so it divides
\(D=\gcd(4^m-1,N)\). The old inequality \(e_j>C\ge n\ge m\) prevents
\(D=N\); hence \(D\) is proper.

The only surviving case is \(J=1\). It certifies

\[
\boxed{
f_j>1,
\qquad
\gcd(f_j,N)=1,
\qquad
\sigma(f_j)>T
}
\]

for every hidden component. Modding out by \(\langle-1\rangle\) loses at
most one factor two. Since \(T\ge2C\), every resulting sign-quotient order
still exceeds \(C\).

The exponent \(N^n\) has \(O(n^2)\) bits. The sieve through \(T\), modular
powers, gcds, divisor stripping, verification, and P159 factor-tree
composition all have uniform deterministic QP bit cost. The theorem removes
the nonsquarefree and hidden-prime-supported order obstructions. It does not
localize unequal coprime local orders.

The statement, proof, self-audit, hostile audit, and blind reconstruction
have SHA-256 hashes
`8a7cfbc7ea7d3fd2d0df3c31bbd540b9c3ae7a7b62dde2997b143135e5ae6ca4`,
`4500b8583e57d00c089c4870694e72c666aa7a72f0d0d0e388030783ec049f49`,
`7c221adb25ebff0b11eca17d8179d40d5bb1e6ba4395af0e7bb4f6dc8462e03b`,
`5932c2969db9531bdaba31cf8a52c9b67c5722cc797133f5b4437b99c6cd07eb`,
and
`d41b16068b3fda6617de06e92f68c1276880eefdf8ee3cdf077d4c6d478e139c`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P161 — the surviving local orders can be made rough

**Status:** promoted from F181 after a hostile audit and an independent
statement-only reconstruction. This is a uniform deterministic QP
postprocessor for the P160 hard branch. It is not an all-input factoring
algorithm.

Let \(N=\prod_jR_j\) be the hidden odd prime-power decomposition and

\[
n=\lceil\log_2(N+1)\rceil.
\]

Suppose P160 returns a public unit \(y\) with local orders \(f_j\) such that

\[
f_j>1,
\qquad
\gcd(f_j,N)=1,
\qquad
\sigma(f_j)>T,
\]

where \(T\) is any fixed integer-valued numerical quasipolynomial bound.
Construct the completely factored exponent

\[
\Lambda_T=\operatorname{lcm}(1,\ldots,T),
\qquad
Q=\Lambda_T^n,
\qquad
w=y^Q\bmod N.
\]

For every component,

\[
\operatorname{ord}_{R_j}(w)
=\prod_{\substack{\ell^a\parallel f_j\\\ell>T}}\ell^a.
\]

Indeed, every exponent \(a<n\). The power \(Q\) therefore removes the
complete primary part for every \(\ell\le T\), and it preserves every
primary part with \(\ell>T\).

The gcd \(H=\gcd(w-1,N)\) gives an exact trichotomy. A proper \(H\) is a
factor. If \(H=N\), every \(f_j\) divides the fully factored \(Q\), and
factor-first divisor stripping returns a factor or proves that all local
orders equal one exact value \(m>T\). If \(H=1\), every local order of
\(w\) is nontrivial, coprime to \(N\), and has least prime divisor above
\(T\):

\[
\boxed{
\operatorname{ord}_{R_j}(w)>T,
\qquad
\gcd(\operatorname{ord}_{R_j}(w),N)=1,
\qquad
P^-(\operatorname{ord}_{R_j}(w))>T.
}
\]

The prime-power statement is exact. Because the retained order is coprime
to the hidden rational prime, reduction from a hidden prime power to its
prime field is injective on the generated cyclic subgroup. Thus identity in
the prime field is equivalent to identity in the full hidden component.

A sieve constructs \(\Lambda_T\) and its factorization. Its bit length is
\(O(T\log T)\), while \(Q\) has \(O(nT\log T)\) bits. All modular powers,
gcds, and stripping attempts therefore have uniform deterministic QP bit
cost.

The same primary-filter argument removes the nonunit alternative from the
two-shift F180 interface by including the explicit factor \(N+3\). If both
the zero-shift and shift-three filters extinguish globally, every order
prime divides either \(3^k-(-1)^k\) or a nonzero resultant of
\(X^k-1\) and \((X+3)^l-1\). For polylogarithmic \(k,l\), these integers
can be fully factored in QP time and give a factor or exact common order.

P161 removes all small rational-prime support from the local orders. It does
not localize unequal large rough local orders.

The frozen statement, proof, hostile audit, and blind reconstruction have
SHA-256 hashes
`992f84a580a362d7908d9287e186dbae46963044956dae65b7b52540fa15df32`,
`8666ed09370836682fa13af3dc3396860104fb021ee478e324aed9dcb5449b06`,
`1175d756bd0b4ceb5968ba2d990d565e62d6676938ba6054144f908b96711561`,
and
`7016f15e0dc72db6a4e761412daca932ef57d88275b737b8c1c31d61081892ea`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P162 — fixed-contraction cross-resultants close synchronized action extinction

**Status:** promoted from F185 after hostile audit and independent
statement-only reconstruction. This is a conditional recursive transition
for the P161 rough-order branch. It is not an all-input factoring algorithm.

Let \(w\) be a public P161 unit. In every hidden prime-power component its
local order \(g_j\) is nontrivial, coprime to \(N\), and \(T\)-rough. Choose
two separated shift menus

\[
\mathcal A=\{0,\ldots,L-1\},\qquad
\mathcal B=\{L+2,\ldots,2L+1\}
\]

and an action cap \(K\) satisfying

\[
K\left(1+K\left\lceil\log_2(2L+2)\right\rceil\right)
\le \lfloor\rho n\rfloor
\]

for one fixed \(0<\rho<1\). Each menu filter deletes every local-order
primary part for which some shifted base is nonunit or has order at most
\(K\).

A proper identity gcd factors \(N\). A gcd of one returns a rough descendant
on which every surviving order prime sees every shift in that menu as a unit
of order above \(K\). Suppose instead that both menus extinguish globally.
For

\[
F_{\delta,0}(X)=X+\delta,\qquad
F_{\delta,k}(X)=(X+\delta)^k-1,
\]

every cross-menu resultant

\[
R_{\delta,\epsilon;k,l}
=\left|\operatorname{Res}
 (F_{\delta,k},F_{\epsilon,l})\right|
\]

is positive and has at most \(\lfloor\rho n\rfloor\) bits. The separated
centres make the resultants nonzero, including when \(k=0\) or \(l=0\).
Every rational prime in every \(g_j\) divides at least one such resultant.
Therefore, after recursively factoring them, the completely factored product
\(U^n\) is a common multiple of all local orders. Factor-first stripping
returns a proper factor or proves one fully factored exact common local order
above \(T\).

There are at most

\[
L^2(K+1)^2
\]

recursive children at one node. If the enclosing complete procedure gives
all recursive calls the same fixed contraction and QP branching bound, then

\[
\mathcal T(n)
\le A(n)+B(n)\mathcal T(\lfloor\rho n\rfloor)
\]

has QP total cost. This is a sufficient bound for this many-child recursion.
It is not a general necessity: a unique recursive child may lose only one
bit, since

\[
\mathcal T(n)\le\mathcal T(n-1)+\operatorname{QP}(n)
\]

is still QP. F185 itself did not supply such a one-child lift; P163 below
now supplies it for this double-extinction branch. The unresolved
wide-shift-hard descendant still prevents a complete factoring recursion.

For a canonical inverse relation \(xy=1+cN\), one has either
\(c=0,x=y=1\), or

\[
0<c<\min(x,y),\qquad \gcd(c,xy)=1.
\]

This carry can expose a factor through \(\gcd(c,N)\), but its own prime
factors do not divide the two endpoints. It is only a direct-endpoint
boundary.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`f4fca86df79a72d473cc3e8dd943140978d1422efb6b2f2af324bd94076a555b`,
`98c4ad7dc7fafb7466bf1a6e2384c20ec86f4d6f29c4c8394749bcc9c5583491`,
`7284ed4a944a7e94e49b4a1a0779a3afb25761ba01ff8da0263981bf225537f0`,
and
`f4adb0570b16111c3b7f3c2ee1ea715f004996c5a88140c7b83212dcc75d3bec`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P220 — the F263 shifted-block leads are public boundary decoys

**Status:** promoted from F267 after a fresh hostile audit and a strict
statement-only reconstruction. This is a boundary theorem for six frozen
symbolic candidates. It is not a converse zero classification, an evaluator
lower bound, or a factoring algorithm.

Let

\[
N=pq,\qquad p<q<2p,\qquad
B=\lfloor\sqrt N\rfloor,\qquad s=B-p,
\]

and put

\[
R_L(X)=\prod_{j=0}^{L-1}(X+j)
\]

for an even public query length \(L\). The six F263 shifted candidates are
integer combinations of

\[
R_L(a),\quad R_L'(a),\quad {R_L''(a)\over2},
\quad R_L(a-B),\quad R_L'(a-B),\quad {R_L''(a-B)\over2}
\]

and two division-free upper-triangular transfer identities. Rising-factorial
reflection proves four exact query-edge mechanisms. They occur only at the
public offsets

\[
s\in\{L-1,L,L+1,L+2\}.
\]

Thus each mechanism already supplies the directly testable candidate
\(p=B-s\). Under the sufficient small-offset condition \(s^2<p\), the two
inequalities defining \(B=\lfloor\sqrt N\rfloor\) force

\[
q-p=2(s+1),\qquad B+1={p+q\over2}.
\]

Since \(B+1=\lceil\sqrt N\rceil\), the first Fermat trial gives

\[
(B+1)^2-N=(s+1)^2
\]

and returns both factors. The condition \(s^2<p\) is sufficient, not sharp.

These four mechanisms account for all six nondirect candidate families in
the authenticated F263 held-out output: 136 candidate-row incidences on 67
rows. Every such row is a consecutive-prime control already factored by the
first Fermat trial. The theorem does not claim that the six polynomials have
no other zeros or that another remote-coefficient grammar cannot work.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`feff0a8b5dfd254cba265c9378106520c4fed718bbff3d507112c59a367045ee`,
`f6e95ae5d8a27828cfd4802cdc587f2bba2b2e94d50f523d42b559ef14e4fac3`,
`cd4ce8010307db57e267c222c2dabd9c42e846b578033feb36ad0d3f97b6fcf4`,
and
`81c3876f69b456ed40f5202190f2a93f1d08e917b234750e25e6616f9206e728`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P219 — signed Pell resultants give exact one-sided gcd tickets under a short-carry condition

**Status:** promoted from F257 after a fresh hostile audit and a strict
statement-only reconstruction. This is a conditional Las Vegas interface,
not an all-input hit-probability theorem or a factoring algorithm.

For two distinct canonical Pell rows with the same positive discriminant,
write

\[
T_h=y_h+k_hN,\qquad A_h=1+Dy_h^2,
\qquad \Delta=y_i k_j-y_j k_i.
\]

Put

\[
d=\gcd(A_i,A_j),\qquad
d_-=\gcd(A_i,y_i-y_j),\qquad
d_+=\gcd(A_i,y_i+y_j).
\]

Every odd prime power in \(d\) occurs to its full exponent in exactly one
of \(d_-\) or \(d_+\). The full integer identity has a necessary public
two-adic correction:

\[
d_{\rm odd}=(d_-)_{\rm odd}(d_+)_{\rm odd},\qquad
d=\operatorname{lcm}(d_-,d_+)2^\eta,\quad \eta\in\{0,1\}.
\]

The same-discriminant resultant factors as

\[
\operatorname{Res}(f_i,f_j)=D^2Q_-Q_+,
\qquad
Q_\pm=D\Delta^2+(k_i\pm k_j)^2,
\]

and the signed shared parts satisfy

\[
d_-\mid Q_-,\qquad d_+\mid Q_+.
\]

Now let \(N=pq\), with \(p<q<2p\), and suppose
\(\left(\frac{-D}{N}\right)=-1\). Thus \(-D\) is a square at exactly one
hidden prime. For either sign, if

\[
0<|k_i\pm k_j|<\sqrt{N/2},
\]

then

\[
\gcd(Q_\pm,N)\in\{1,r_{\rm sp}\},
\]

where \(r_{\rm sp}\) is the unique split hidden prime. Hence every nontrivial
ticket is automatically a certified factor. A source that produces such a
ticket with inverse-QP probability immediately gives an expected-QP Las
Vegas stage.

The coordinate sign does not determine the P66 normalized-root sign.
Exact same-channel examples can be either global decoys or non-global roots.
Thus signed refinement helps direct gcd extraction but does not replace the
square-class decoder.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`de5c6833d7a5af14b144188b24cfa0c6e4734d5699824689baeed0bb45b2aa8a`,
`f5d1efbc4a61d67fe2cb4c68de7b96ceec281d144b1a899dd5eb8d737f99ab73`,
`bc292605831bc1e71fd1eac5a59970838aee520100c31cb0b2d13bd2a396b67f`,
and
`bb1d26e51dd6739bed4dae10aa0b99426a110abc5116f88b8df62e9b95800697`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P218 — fixed-past Pell sparsity gives only a logarithmic rank floor, and clean odd multiples are decoys

**Status:** promoted from F253 V2 after a fresh hostile re-audit and strict
statement-only reconstruction. F253 V1 is preserved with its strict blind
failure. This is a retrospective-rank boundary and a clean-dependency
classification, not a factoring algorithm.

For a finite menu of rows (A_{D,y}=1+Dy^2), remove exact-square
singletons and repeated (y)'s within each (D). Put

\[
B_D=1+\left\lfloor
{\log(1+2Y_D\sqrt D)\over\log(2+\sqrt2)}
\right\rfloor,qquad B_\Sigma=\sum_D B_D.
\]

P214 implies that each nonzero rational square class occurs at most
(B_\Sigma) times. If the (m) columns have rank (r) and nullity
(d=m-r), then

\[
\boxed{m\le B_\Sigma(2^r-1)},
\qquad
r\ge\left\lceil\log_2\left(1+{m\over B_\Sigma}\right)\right\rceil.
\]

For (Z_k), the number of (k)-row square subsets,

\[
kZ_k\le B_\Sigma {m\choose k-1}.
\]

A uniformly random full subset is square with exact probability (2^{-r}),
at most (B_\Sigma/(m+B_\Sigma)). These bounds are sharp using only a
class-fibre cap: take (B) labelled copies of every nonzero vector in
(mathbf F_2^r). Thus fixed-past sparsity alone cannot control a
retrospective P66 choice among the full past span.

There is also a complete clean odd-multiple classification. For odd
(k>1), integer polynomials (F_{k,D},G_{k,D}) satisfy

\[
1+D F_{k,D}(Y)^2=(1+DY^2)G_{k,D}(Y)^2.
\]

If both distinct Pell rows (j,kj) are present and retained, their canonical
coordinates are distinct, and (F_{k,D}(y_j)<N), then

\[
A_{kj}=A_jG_{k,D}(y_j)^2.
\]

This gives a genuine two-column dependency, but its positive integer root
equals the supplied modular root. Its normalized root is (+1). The span
of all actual nonzero clean-pair vectors therefore has trivial normalized
root image.

With (F_{k,D}(y_j)=y_{kj}+cN), the exact carried defect is

\[
A_jG_{k,D}(y_j)^2-A_{kj}
=DcN(2y_{kj}+cN).
\]

The (c=0) branch is the global decoy. Carried relations and other
arithmetic specializations remain open. The exact finite certificate
(N=4331=61\cdot71), (D=2), indices (17,51), has
(A_{17}=73), (A_{51}=73\cdot289^2), and normalized root (+1).

The V2 statement, V2 proof, fresh V2 hostile re-audit, and strict V2 blind
reconstruction have SHA-256 hashes
`53c7f59bc3f2a2e1b2f38d77661abfe94465945f5ce8691516e5c5c76ec277ba`,
`b76aed1d24455ec1a32d9c586d1b9f55f9b0c713273a9a3a7f1ba54b5ba1afec`,
`53416862803b7d7303318f2eca5ca26dc1db6f4d24ea65ecd3b5670c33888a93`,
and
`ee2a078f6420c528b6fa520d44b709cc1fb1bdbc0f915eb5f0ce2594e20f9529`.
V1 strict blind failure hash is
`05386c64670c09c99b236d668959a5c6ff8428e01aa3095a1c52e06c38b9c906`.
The finite certificate came from a frozen local search with the workflow
qualifications recorded in F253. No cross-family audit, human audit, or
publication-level literature review ran.

## P217 — cleaned Pell polynomials have zero generic kernel and an explicit resultant core

**Status:** promoted from F252 after a fresh hostile audit and a strict
statement-only reconstruction. This is a deterministic structural filter for
an explicit Pell bank. It is not a source theorem and not a factoring
algorithm.

For Pell data

\[
S_i^2-D_iT_i^2=1,qquad
f_i(X)=1+D_i(T_i-k_iX)^2,qquad a_i=f_i(N),
\]

the rows with (k_i=0) are constant squares. If (k_i>0), the exact
content and primitive discriminant are

\[
\operatorname{cont}(f_i)=\gcd(S_i^2,k_i^2,2k_i),
\qquad
-{4D_i k_i^2\over\operatorname{cont}(f_i)^2}<0.
\]

Thus every post-wrap primitive part is irreducible over (mathbf Q). For

\[
f=1+D(T-kX)^2,qquad g=1+E(U-\ell X)^2,qquad
\Delta=T\ell-Uk,
\]

the exact resultant is

\[
\boxed{
\operatorname{Res}_X(f,g)
= [DE\Delta^2+E\ell^2+Dk^2]^2-4DEk^2\ell^2.}
\]

It vanishes exactly when (Delta=0) and (Dk^2=E\ell^2), which is
equivalent to (f=g) as integer polynomials. Hence, after constant-square
rows and exact polynomial duplicates are removed, the generic square-class
kernel over (mathbf Q(X)) is zero. Before cleanup, every generic
dependency has an integral polynomial root and specializes to a global
normalized root. There is no coefficient-denominator exception.

The specialization-only kernel has a factor-free explicit localization.
For each cleaned row put

\[
\mathcal R_i=\prod_{j\ne i}|\operatorname{Res}(f_i,f_j)|,
\quad e_i=\lceil\log_2(a_i+1)\rceil,
\quad g_i=\gcd(a_i,\mathcal R_i^{e_i}),
\quad b_i=a_i/g_i.
\]

Then (gcd(b_i,a_j)=1) for every (j\ne i). If (b_i) is nonsquare,
it supplies a private odd-valuation pivot and row (i) occurs in no
numerical square dependency. If (b_i) is square, it can be removed from
the parity column. The complete residual parity problem is therefore
supported on explicit pairwise resultants. All operations have polynomial
bit complexity in the materialized input size.

This strengthens P68 for the Pell family: it kills the entire cleaned
generic kernel and identifies the specialization-supported numerical core.
It does not bound that core, prove a private pivot for every row, or control
its normalized-root image.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`cf49a2ea6ef9158f7ed60e79385b5aad5f28bd7583e9404216eadadf30457cf7`,
`acf073dc3c5c402eca8b5c9769ce14cc357d5c13ff74caa02c633ce5ac47c130`,
`0915c14a1da2a0b75dfa45c7b4ac151805aadc969d9073915908b932ef6f3717`,
and
`d923ea2051157ed3b6a72af7e56f874f1d6c3037807d32a19db40bbfffea8757`.
No research computation, cross-family audit, human audit, or
publication-level literature review ran.

## P216 — the complete tailored negative-Pell component bank need not contain a square dependency

**Status:** promoted from F254 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact counterexample to one
integer-specific Pell source. It is not a probability bound and not a
factoring obstruction.

Let (N) be odd and let

\[
b^2-2y^2=-1,qquad 1<y<N.
\]

Put (T=N+y), (D=T^2-2), (S=T^2-1), and

\[
A=1+Dy^2.
\]

Then (S^2-DT^2=1), (S\bmod N) is a supplied square root of
(A\bmod N), and, with (u=(b-1)/2), (v=(b+1)/2),

\[
\boxed{
A=(yN+2u^2)(yN+2v^2).}
\]

Each public component is twice a square modulo (N). Therefore every even
component subset has a known modular square root and can be sent to P66.
For two component forms

\[
F_i(X)=y_iX+2w_i^2,qquad F_j(X)=y_jX+2w_j^2,
\]

every prime shared after specialization at (X=N) divides the explicit
resultant

\[
\operatorname{Res}(F_i,F_j)
=2(y_iw_j^2-y_jw_i^2).
\]

This enlarged source is not universal. For (N=143=11\cdot13), the
complete negative-Pell window (1<y<N) contains exactly (y=5,29). Its
four components are

\[
733,qquad 3^2\cdot83,qquad
3\cdot17\cdot97,qquad47\cdot107.
\]

The primes (733,83,17,47) are private parity pivots. Hence the full
four-column component matrix has rank four and zero kernel; the original
two-row bank also has rank two. Every component, supplied root, defining
parameter, and pairwise resultant is coprime to (143). Thus the complete
admissible tailored recurrence produces neither a direct factor nor an
exact-square dependency on this input.

The certificate refutes only the universal form of this construction.
Randomized discriminants, other Pell windows, mixed sources, and the general
retrospective multirow P66 channel remain open.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`25d20381188d0ffe5e7d9b87331c3921b0f78dd9344d73628ca33e1f1201e190`,
`ac78cae56d0063191e0eafa8cf37ad61358fb9246bf5cd94033413434e96625e`,
`c21e974c50ecfe0f28c141ec21f9d775f66929bc2dcc43048c0c0de928b0feab`,
and
`c2e4bbbf8748f18bf11232eb7cd3ccca78ad149625037243ff7de6478fe1214a`.
No research computation, cross-family audit, human audit, or
publication-level literature review ran.

## P215 — one shifted binomial coefficient is a deterministic balanced factor oracle

**Status:** promoted from F249 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact evaluator target and a
named-method boundary. It does not evaluate the coefficient in numerical
quasipolynomial time and is not a factoring algorithm.

Let (N=pq), where (p<q<2p) are distinct odd primes, and put

\[
B=\lfloor\sqrt N\rfloor,\qquad
H=\left\lfloor {B\over2}\right\rfloor,\qquad
s=B-p.
\]

Then (B\ge3) and (0\le s<H<p<q). For every positive integer (r),
after screening (gcd(r,N)), and every (1\le c\le H), Lucas's theorem
gives the exact CRT identity

\[
\boxed{
\binom{rN+c-1}{B}
\equiv rq\binom{c-1}{s}\pmod N.}
\]

Consequently

\[
\gcd\!\left(N,\binom{rN+c-1}{B}\right)
=
\begin{cases}
N,&c\le s,\\
q,&c>s.
\end{cases}
\]

The public endpoint (c=H) therefore always returns (q), provided the
coefficient residue can be evaluated. Uniform (c) succeeds with exact
probability ((H-s)/H\ge1/3), but this randomization is unnecessary at the
endpoint. If (s=0), then (B=p) and the elementary gcd with (B) already
factors.

The adjacent recurrence

\[
(rN+c-B)C_{r,c+1}=(rN+c)C_{r,c}
\]

has one hidden nonunit denominator, at (c=s). The accumulated denominators
are an upper-half interval product with gcd (p). More sharply,

\[
\gcd\!\left(N,\binom BH\right)=p,
\qquad
\gcd\!\left(N,\binom{N+H-1}{B}\right)=q.
\]

Thus the shifted endpoint is algebraically no stronger than the existing
central-binomial or upper-half factorial gate. It only returns the
complementary factor. Random top multipliers scale the residue by the public
unit (r) and do not move the threshold.

For even (B=2H), the central coefficient is

\[
\binom BH=[x^H](1-4x)^{-1/2}.
\]

For odd (B), it differs from this algebraic-series coefficient by a public
unit after the elementary screen. The standard product recurrence,
Vandermonde/Newton expansion, dense block methods, and published holonomic
baby-step/giant-step algorithms all remain exponential in the input bit
length or encounter the factor-bearing product. Known logarithmic-index
algebraic-series algorithms require a known prime characteristic and
characteristic-size preprocessing; they do not directly transfer to
(\mathbb Z/N\mathbb Z). These are named-method boundaries, not a general
circuit lower bound.

**Exact remaining gap.** Construct a genuinely new numerical-QP evaluator
for the central or shifted coefficient modulo the unfactored composite
modulus, or for its hidden divisibility, without materializing a
factor-bearing factorial or interval product.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`2b6594484dcb394b58126398d9944ab3e6aa18f8bc2d62e462dcc6e3c18db825`,
`8938898cf8118ddcee1b4831468c7f6a62a4928c35688abe61ace52ca8bd9865`,
`e591b68f7ad92bc3174fc7bb8826abd1ea7a0b1f92fdd82e676a68449fb52e89`,
and
`c92226e23ef321e917d68c2db090b512ad1ac906af6cbb39ffeda94eebadf338`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P214 — a fixed past product has only logarithmically many Pell square closures

**Status:** promoted from F251 after a fresh hostile audit and a strict
statement-only reconstruction. This is a fixed-past source boundary for
torus rows. It is not a theorem about retrospective multirow P66 selection
and is not a factoring algorithm.

Let (D,Y>0), put

\[
A_y=1+Dy^2\qquad(0\le y<Y),
\]

and fix a positive integer (P) before (y) is selected. Then

\[
\#\{0\le y<Y:P A_y\text{ is an exact integer square}\}
\le
1+\left\lfloor
{\log(1+2Y\sqrt D)\over\log(2+\sqrt2)}
\right\rfloor.
\]

The bound is independent of the size and squarefree kernel of (P).
Writing (P=au^2), exact square closure is equivalent to

\[
av^2-Dy^2=1.
\]

For two solutions (y_2>y_1), the quotient of
(av_i+y_i\sqrt{aD}) is an integral norm-one unit
(s+t\sqrt{aD}). If (aD) is a square, no two distinct solutions exist.
Otherwise every gap quotient is at least (2+\sqrt2). This gives the
uniform logarithmic count and avoids the usual multiple-seed issue for a
generalized Pell equation.

If rows carry supplied roots modulo (N), useful mixed-root closures are a
subset of these coordinates. Therefore a fresh coordinate law of maximum
atom (mu), conditional on the full past, has useful closure probability at
most

\[
\mu\left(1+\left\lfloor
{\log(1+2Y\sqrt D)\over\log(2+\sqrt2)}
\right\rfloor\right).
\]

For two independent uniform admitted rows, conditioning on the first row
gives the same pair bound. On a clean raw torus with (H) points and at
most four points over each canonical (y), it is at most (4B(D,N)/H).
For a clean powered image with fibres of size at most two, it is at most
(2B(D,N)/H). A numerical-QP bank is exponentially unlikely to contain a
useful pair whenever the source size is (2^{\Omega(n)}).

**Exact remaining gap.** P214 controls one fresh row against one product
fixed before that row, all pairs in an independent bank, and prescribed
fixed-past closures. It does not control a decoder that sees the fresh row
and then chooses among exponentially many earlier subset products, nor a
general retrospectively selected product of three or more rows.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`2fce8c0126d1454c68a39068ab28b8fda95cc3f270a1d83d7cd758a66c50c5e6`,
`3948902e35ae73e3a1cdcf68e1674f7be83e468911027c77bd9cb98c294ac707`,
`37455b527e93ba38e5f616bfbdcec2832acf5aa183a6a63b299257fada48f74b`,
and
`c74d04bf7ed4565498d80636bce727e76ab37b57d970d74da80e63daf08d911a`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P213 — rigid exact-square lift and torus events are exponentially sparse

**Status:** promoted from F248 V2 after a fresh hostile audit and a strict
statement-only reconstruction. This is a source-boundary theorem for several
explicit P66 events. It is not a bound for a general multirow square
dependency and is not a factoring algorithm.

Let (N=pq) for distinct odd primes and let (E>0) be even with
(gcd(E,N)=1). Put

\[
g_p=\gcd(E,p-1),\qquad g_q=\gcd(E,q-1),\qquad K=g_pg_q.
\]

For a uniform full unit lift (A\bmod N^2), the canonical output
(L=[A^E]_{N^2}) is an exact integer square with probability at most
(K/N). Conditional on a fixed square output, the supplied roots are
uniform on a coset of the half-power image of the (E)-power kernel. On a
local side (r\in\{p,q\}), that image is ({\pm1}) exactly when
(v_2(E)\le v_2(r-1)), and is ({1}) otherwise. If at least one side is
active, exactly half of the output fibre gives a mixed root and factors.

For one fixed residue (a\bmod N), the principal lifts
(A_t=a_0+tN\bmod N^2) obey

\[
h_t=h_0+Ea^{E-1}t\pmod N.
\]

The (N) output digits contain exactly four integer squares, two with mixed
normalized roots. Thus a uniform principal lift factors through this event
with exact probability (2/N). Locating either useful digit is equivalent
to finding a mixed second square root modulo (N).

This remains history-wise sparse against one fixed past product. If a unit
integer (P) and one root (X^2\equiv P\pmod N) are fixed before the fresh
coordinate (t), at most two values of (t\bmod N) make
(P[A_t^E]_{N^2}) an exact square with mixed normalized root. Writing
(P=du^2) shows why: a square closure forces the fresh row to equal (dv^2),
and the resulting congruence has only four CRT classes, at most two mixed.

The same packet gives exact or subexponential-over-exponential bounds for
canonical scalar duplicates, a scalar output paired with its reciprocal
modulo (N^2), raw and powered norm-one torus singleton squares, torus
duplicates, and torus inverse-point pairs. Therefore every numerical-QP bank
of the applicable rigid events has exponentially small success under the
explicit parameter hypotheses

\[
K=2^{o(n)},\qquad H=2^{\Omega(n)}
\quad\text{or}\quad H'=2^{\Omega(n)},
\]

where (H,H') are the relevant clean source sizes. P213 does not construct
an input family satisfying those hypotheses.

**Exact remaining gap.** The theorem does not control a nonduplicate
multirow integer-prime parity dependency, a mixed scalar--torus relation, a
subset selected retrospectively from many rows, the canonical scalar section
(t=0), or the canonical-inverse-base pair. Those source channels remain
live.

The V2 statement, proof, hostile re-audit, and strict blind reconstruction
have SHA-256 hashes
`57ea62c39ce0e04b4a271135e613eabdcf79a32dd5df85dc692effb6dc8d8504`,
`0d292831f42bb515d298c26846c7c912cddbf07682b7b63564e9ff2fce3c46f8`,
`2d99e789263f3ef6341fa311ac0ef0eca53df54096bb2e7a812f864f118cee2b`,
and
`a79ec436926390d7431fe8dc84ccd3e79980c2c3581a17e0d9e0a816185f7b66`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P212 — fresh inverse-quotient words and feedback-free torus trials remain exponentially sparse

**Status:** promoted from F245 V3 after a fresh hostile audit and a strict
statement-only reconstruction. This is a lower bound for the formal
restricted Las Vegas grammar below. It is not a general factoring lower
bound and it does not cover canonical carries, biased sources, retained-point
feedback, or an unrestricted relation decoder.

Let (N=pq) be a product of distinct odd primes and put

\[
\Delta_N=\max_{1\le m<N^2}\tau(m).
\]

For an exactly uniform canonical unit (u), let (v) be its least positive
inverse modulo (N) and define

\[
K(u)={uv-1\over N}.
\]

The exact fibre identity

\[
K^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}
\]

gives at most (Delta_N) preimages per value. After replacing the zero
value by one, every residue class modulo a prime (ell<N) has mass less
than

\[
{8\Delta_N\over\ell}.
\]

The same bound holds for a difference of one fresh quotient and any earlier
one. Thus an adaptive bank with at most (B) accepted seeds hits a fixed
prime through a singleton or pair-difference atom with probability at most

\[
8\left(B+{B\choose2}\right){\Delta_N\over\ell}.
\]

There is an unconditional infinite semiprime family with four distinct
marker primes

\[
\lambda_+,\lambda_-,\rho_+,\rho_->2^{c_0n},
\]

one in each of (p\pm1,q\pm1), such that the opposite hidden factor is
primitive modulo its marker and

\[
\bigl(\gcd(p-1,q-1),\gcd(p-1,q+1),
\gcd(p+1,q-1),\gcd(p+1,q+1)\bigr)
=(2,12,2,2).
\]

Every explicitly materialized numerical-QP-bit product of signed powers
(N^k\pm1) misses all four markers. Even if exact common-order tokens from
all four orientations are granted, their accumulated lcm divides (12).

The restricted grammar may combine those signed powers and order tokens
with arbitrary products and positive powers of the fresh inverse quotients
and their pair differences. It may also sample exact uniform discriminants
and factor-free Hilbert--90 points. Before each fresh point it must fix an
exponent

\[
E=(N-J)(N^2-1)^nW_{\rm sp}W_{\rm iq}M.
\]

Its only factor exits are the explicitly listed raw gcd screens, direct word
gcds, the two signed torus identity screens, and their two-primary Miller
chain. Current-point coordinates and carries cannot feed back into the word.

For this complete grammar, every stopped run of at most (B) bit
operations has factor probability at most

\[
\boxed{
48\left(B+{B\choose2}\right){\Delta_N\over L}
+4B\left({1\over p}+{1\over q}\right)
+{2B\over L},
}
\]

where (L) is the smallest marker. Since
(Delta_N=2^{o(n)}), this is (2^{-\Omega(n)}) for every numerical-QP
cutoff. Markov truncation therefore rules out expected numerical-QP time for
every Las Vegas machine confined to this grammar on the infinite family.

The exact Hilbert--90 lift identities outside the grammar show why the scope
matters. Canonical norm carries are nonlinear combinations of inverse and
coordinate quotient digits, and no atom bound above applies to them.

**Exact remaining gap.** Analyze a genuinely integer-specific source outside
the grammar: a canonical high digit, nonlinear carry or determinant, biased
seed, current-point feedback word, inverse-quotient descent, or a decoder
using the full retained relation transcript.

The V3 statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`2120f53ec1762cd6b90236eb165d59368f9e0aad4750dcb3a5afadf3508d2c8b`,
`52e7b9391d8d4f36d4653b016f58805776655f732d3a398f9e753c9f14205e7d`,
`e4335fa3e3345d76d53973f628e9675630dfdec4869eefffad28ce2fd38b98d3`,
and
`35a751ad54971be6005dec16317375f640efa327bfc26a8664d1542beb57041d`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P211 — fresh principal-lift carries form an affine torsor, while the canonical section remains live

**Status:** promoted from F247 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact boundary for randomized
ordinary and quadratic-torus lift fibres. It is not an all-input factoring
algorithm and it gives no distribution law for a fixed canonical lift.

Let (N) be odd, let (a) be a unit modulo (N), and let
(gcd(E,N)=1). For the lifts

\[
a_t=a+Nt\pmod {N^2},
\qquad
a_t^E\equiv x+NK_t\pmod {N^2},
\qquad
x=\langle a^E\rangle_N,
\]

one has the exact affine law

\[
\boxed{K_t=K_0+Ea^{E-1}t\pmod N.}
\]

Its slope is a unit. Thus a fresh uniform lift parameter makes the carry
exactly uniform modulo (N), even after conditioning on the complete
transcript visible modulo (N). The same formula holds for a signed return.
For a negative return, the signed carry is the canonical-residue carry plus
one.

If (N=pq) for distinct odd primes, a uniform carry (K) has exact
proper-factor probability

\[
\boxed{
\Pr(1<\gcd(K,N)<N)={p+q-2\over N}.
}
\]

Translation by any value fixed by the past preserves this law. For an
exterior prime (ell), replacing zero by one gives

\[
\Pr(\ell\mid\widehat K)<{1\over\ell},
\]

and a fresh conditionally uniform carry collides with a fixed earlier carry
modulo (ell), without being equal to it, with probability at most
(1/\ell). Hence random motion inside a lift fibre has generic scalar
incidence; a failed modulo-(N) order transcript does not create a biased
high digit.

The signed carry nevertheless has exact arithmetic meaning. If
(r\in\{p,q\}), (r\nmid E), and

\[
a^E\equiv\sigma+NC\pmod {N^2},
\qquad \sigma\in\{+1,-1\},
\]

then

\[
\boxed{
r\mid C
\iff a^E\equiv\sigma\pmod {r^2}
\iff \operatorname{ord}_{r^2}(a)=\operatorname{ord}_r(a).
}
\]

Thus a proper carry gcd really factors (N), but a random lift reaches it
only at the generic exponential scale on balanced inputs. A canonical null
witness is (a=N-1): for even (E), its carry is (-E\pmod N); for
(E=(N-1)W), it is (W\pmod N). In particular, (W=1) gives a global
return with the useless carry one.

The quadratic-torus analogue is also exact. In

\[
\mathcal A_{N^2}=(\mathbb Z/N^2\mathbb Z)[w]/(w^2-D),
\]

every exact norm-one lift of a fixed norm-one residue has the unique form

\[
U_t=U(1+Ntw),\qquad t\in\mathbb Z/N\mathbb Z.
\]

For a normalized carry (C_t),

\[
\boxed{C_t=C_0+Etw.}
\]

The trace coordinate is fixed by the chosen section, while the tangent
coordinate is uniform for uniform (t). Without the norm-one restriction,
both carry coordinates are affine and uniform.

Carries along one power chain are not fresh samples. In the ordinary case,

\[
K_{mE}=Q_m+mx^{m-1}K_E\pmod N,
\]

and in the torus case,

\[
C_{mE}=Q_m+mC_E.
\]

For (T) fresh lift parameters that remain conditionally uniform after the
complete past, any positive product of their nonzero carries, pair
differences, and positive powers satisfies

\[
\boxed{
\Pr(\ell\mid W_{\rm lift})
\le {T+\binom T2\over\ell}.
}
\]

This history-wise bound permits adaptive later bases and exponents. On the
P209 four-marker family, a numerical-QP bank of these random gauge carries
and differences hits any exponential marker with probability
(2^{-\Omega(n)}). This last consequence is conditional on P209's marker
interface and product-support progress criterion.

**Exact remaining gap.** Analyze the canonical integer section. The theorem
does not cover canonical intercepts, nonlinear same-gauge functions,
cross-base identities, determinants, Euclidean quotients, retained exact
relations, or a decoder that uses more than product prime support. A
canonical high digit can still have inverse-QP factor or exterior-residual
bias.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`7009dcdd153e327f32f0a09d94298d0ff4b79c7196a2228e345f442d2c356d1b`,
`583c206ac262804ef3ba67d5f8e78950fd2c0dd8fa9517d80b6a2a797b4ab81e`,
`35b650ccc33affe25981183fdd4d0ec2aeb025486f67bb33e38cc45ecaf0c849`,
and
`b6280e1739d5308eb09ff2c098f75008213002b3573207fafc4a035569e096e7`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P210 — the square baseline strips all cross-sign support, but the natural collision sources stay generic

**Status:** promoted from F243 after a fresh hostile audit and a strict
statement-only reconstruction. This is a conditional collision bridge and a
set of scoped source boundaries for distinct odd semiprimes. It is not an
all-input factoring algorithm.

Let (N=pq), let

\[
A=N^2-1,qquad n=\lceil\log_2(N+1)\rceil,
\]

and fix one P208 orientation
(\epsilon=(\epsilon_p,\epsilon_q)\). Put

\[
m_i=i-\epsilon_i,qquad
d_\epsilon=\gcd(m_p,m_q),qquad
s_{i,\epsilon}=m_i/d_\epsilon.
\]

Let (s_{i,\epsilon}^{\rm ext}) be the largest divisor of
(s_{i,\epsilon}) supported on primes outside (A). The single public word

\[
\boxed{W_0=A^n}
\]

has (O(n^2)) bits and leaves exactly

\[
\boxed{r_{i,\epsilon}=s_{i,\epsilon}^{\rm ext}}
\]

for every side and every orientation at once. Indeed, every primary
exponent in (s_i<N<2^n) is below (n). For odd
(\ell\mid p-\epsilon_p),

\[
\boxed{
\ell\mid N^2-1
\iff
\ell\mid q-\delta\text{ for some }\delta\in\{\pm1\}.
}
\]

Thus every surviving exterior prime on one side is absent from both shifted
orders on the other side. The baseline removes all cross-sign support but
does not bound the exterior residuals.

For iid samples from any exact public integer law, replace an equal pair by
one and otherwise put (\Delta=|Z-Z'|). Define

\[
\kappa_\ell=\Pr(Z\ne Z',\ Z\equiv Z'\pmod\ell).
\]

If every prime in one fixed exterior residual satisfies
(\kappa_\ell\ge1/Q(n)), then

\[
R=\lceil Q(n)\log(2n)\rceil
\]

independent differences, raised to the (n)-th power and multiplied by
(A^n), absorb that residual with probability at least one half. A fresh
uniform discriminant selects the corresponding hidden orientation with
probability one quarter, and P208 then factors with conditional probability
at least one half. The complete conditional success probability is therefore

\[
\boxed{1/16}.
\]

One concrete sufficient source grants a complete factorization

\[
A=\prod_j b_j^{a_j},\qquad T=\tau(A),
\]

and samples a uniform divisor. If (h_\ell) is the subgroup size generated
by the reductions of the (b_j) modulo an exterior prime, then

\[
\boxed{\kappa_\ell\ge {1\over h_\ell}-{1\over T}}.
\]

This is a genuine positive bridge, but the factorization of (A) and the
all-prime collision lower bound are not supplied.

The natural factor-free and canonical sources obey exact generic-scale
boundaries.

- Split and nonsplit quadratic norm fibres give distinct collision rates of
  order (1/\ell); a nonsplit norm difference has no distinct local zero.
- A uniform Hilbert--90 point has trace-collision probability
  ((2m-2)/m^2), and distinct-point probability ((m-2)/m^2), on a torus
  of order (m).
- For two fixed nonzero coefficient tuples and independent uniform
  discriminants, the normalized trace resultant vanishes with probability
  exactly (1/(\ell-1)).
- Either canonical coefficient of a clean product-torus point has useful
  distinct-integer collision probability below (15/\ell). The union of
  both coordinates is below (30/\ell). A uniform discriminant in one
  Jacobi class has the same generic scale.

The exactly sampleable factor-free law

\[
X\text{ uniform modulo }A,qquad Z=\gcd(X,A)
\]

has

\[
\Pr(Z=d)={\varphi(A/d)\over A}\le {1\over d}
\]

and, for every exterior prime,

\[
\boxed{\kappa_\ell\le {2(1+\log A)^2\over\ell}}.
\]

It may have zero useful collision energy, so it does not simulate uniform
divisor sampling for this purpose.

Finally, in

\[
\mathbb Z[w]/(w^2-A),\qquad\eta=N+w,
\]

write (\eta^k=X_k+Y_kw). If
(h_\ell=\operatorname{ord}_\ell(\eta)), a (T)-term trace window has no
distinct collision whenever (h_\ell\ge2T-2). If (h_\ell) is QP-small,
the deterministic product of the positive-index words (X_k-1) already
captures (\ell). Pell randomization therefore reduces exactly to another
small-meta-order gate.

**Exact remaining gap.** Produce inverse-QP distinct-integer aliasing on one
exterior residual without factoring (N^2-1), or use a genuinely nonlinear
cross-coordinate/carry word. The bounds above do not cover determinants,
adaptive nonlinear lifts, or arbitrary integer transforms.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`569b32183ae53bb687dc2cd5453e6d4e769bcf2ae7bd16e957e2d5da52db6488`,
`8bf76e78037bd3631016be24db7d45d6abc5603d8b86b20185bec6b0ac3d7a97`,
`51fb8ba2603bd3174f2e9486f342323ad6baf31b259023566b845cfad839be05`,
and
`ad8a98a618f94e39a84c512f3a198a3f5dc2c1bf8349a48dbe7a7b31399f4f42`.
F243-R2 is finite guidance only. Its authenticated artifacts do not by
themselves certify remote chronology, and its raw report omitted the
preregistered Wilson intervals. No numerical claim is needed for P210. No
cross-family audit, human audit, or publication-level literature review has
run.

## P209 — the square exponent conserves four shifted residuals, while signed-power words can miss them all

**Status:** promoted from F244 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact ordinary--torus bridge and
an infinite-family boundary for signed-power words. It is not an all-input
factoring algorithm or a lower bound against other integer words.

Let (N=pq) for distinct odd primes. For (a,b\in\{\pm1\}), put

\[
d_{a,b}=\gcd(p-a,q-b),\qquad
A=p^2-1,\quad B=q^2-1,\quad G=\gcd(A,B),
\]

and let

\[
\delta=\mathbf 1_{v_2(A)\ne v_2(B)}.
\]

The exact combined shifted common capacity is

\[
\boxed{\operatorname{lcm}_{a,b\in\{\pm1\}}d_{a,b}={G\over2}}.
\]

Define

\[
t_{p,a}={p-a\over\gcd(p-a,B)},\qquad
t_{q,b}={q-b\over\gcd(q-b,A)}.
\]

These four integers are pairwise coprime, including at the prime two, and

\[
\boxed{
\prod_{a\in\{\pm1\}}t_{p,a}
\prod_{b\in\{\pm1\}}t_{q,b}
={AB\over2^\delta G^2}.
}
\]

Consequently

\[
\min(t_{p,+},t_{p,-},t_{q,+},t_{q,-})
< {\sqrt N\over2^{\delta/4}\sqrt G}.
\]

This is only a square-root bound. It does not force a numerical-QP
residual.

For the P208 torus orientation ((a,b)), the public Jacobi sign is
(J=ab). Choosing the unfactored word (W_J=N+J) makes every orientation
use the same exponent

\[
(N-J)W_J=N^2-1.
\]

Its two local residuals are exactly (t_{p,a}) and (t_{q,b}). Averaging
the clean P208 trial over the four equally likely orientations gives

\[
\Pr(\mathrm{factor})
\ge {1\over8}\sum_{z\in
\{t_{p,+},t_{p,-},t_{q,+},t_{q,-}\}}{1\over z}
>{2^{\delta/4-1}\sqrt G\over\sqrt N}.
\]

Thus (N^2-1) is one exact (O(\log N))-bit bridge for all four shifted
orders, but its unconditional success guarantee is still exponential in
the input length.

For an odd prime (\ell\nmid N), signed-power support is exact. If
(h=\operatorname{ord}_\ell(N)), then LTE gives

\[
v_\ell(N^k-1)=0\quad(h\nmid k),
\]

and otherwise

\[
v_\ell(N^k-1)=v_\ell(N^h-1)+v_\ell(k/h).
\]

Likewise (v_\ell(N^k+1)) is nonzero exactly when (h) is even and
(k=(h/2)u) with (u) odd, in which case it equals
(v_\ell(N^{h/2}+1)+v_\ell(u)).

There is an absolute (c>0) and an infinite family of distinct odd
semiprimes with four distinct marker primes

\[
\lambda_+,\lambda_-,\rho_+,\rho_->2^{cn},
\]

such that (\lambda_a\mid p-a), (\rho_b\mid q-b), the opposite factor
is primitive modulo each marker, and

\[
(d_{+,+},d_{+,-},d_{-,+},d_{-,-})=(2,12,2,2).
\]

In particular (G=24). The family follows from reduced CRT conditions
and two sequential applications of Linnik's theorem; the size estimates
link the marker primes exponentially to the final input length.

On every sufficiently large member of this family, every positive
numerical-QP-bit word of the form

\[
W=\prod_{j=1}^{s}|N^{k_j}-\sigma_j|^{e_j},
\qquad k_j,e_j\ge1,\quad\sigma_j\in\{\pm1\},
\]

is coprime to all four marker primes. This remains true for adaptive
selection, pathwise, because the final word has the same grammar and bit
bound. Each P208 orientation retains one marker on each hidden side, so a
clean powered trial succeeds with probability at most (2^{1-cn}).
Numerical-QP many trials still have exponentially small success.

All exact ordinary and torus common orders on the same family have lcm at
most (12). Combining them with a known dyadic residue modulo (2^t)
therefore gives modulus at most

\[
\operatorname{lcm}(2^t,12)=3\cdot2^t\qquad(t\ge2).
\]

**Exact remaining gap.** Produce an integer word outside the signed-power
grammar with an all-input inverse-QP progress law. Difference, carry,
quotient, discriminant-dependent, and retained-relation words are not
covered by this boundary.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`ace1c3ec745c64b4ac9383b8620720791a3c87b065307a2702baa63f1607a70a`,
`9a5030717a6611ad56dc8f013f6dc59e81bd93cf63e9a825e60a01e4688979be`,
`a91882591ebc07d4b8ebf7269877cfedaa1925ef80cb2e850793d2e0c30b9110`,
and
`cdc6b275cc0cabe4c4d1bfcb6d93ca5766bd59ce02f6e98444c7cc4330da6937`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P208 — quadratic tori give four exact unfactored-word Miller interfaces

**Status:** promoted from F242 V2 after a fresh hostile re-audit and a
strict statement-only reconstruction. This is a conditional Las Vegas
reduction for distinct odd semiprimes. It is not an all-input factoring
algorithm and does not construct the required word.

Let \(N=pq\) for distinct odd primes. For a public unit \(D\), put

\[
\epsilon_p=\left({D\over p}\right),\qquad
\epsilon_q=\left({D\over q}\right),\qquad
J=\left({D\over N}\right)=\epsilon_p\epsilon_q.
\]

The two local norm-one quadratic tori are cyclic of orders

\[
m_p=p-\epsilon_p,\qquad m_q=q-\epsilon_q.
\]

Writing

\[
d=\gcd(m_p,m_q),\qquad s_i={m_i\over d},
\]

one has \(\gcd(s_p,s_q)=1\) and the exact shifted common-capacity identity

\[
\gcd(N-J,m_i)=d.
\]

For any public integer word \(W\ge1\), whose factorization is neither
known nor needed, set

\[
E=(N-J)W,
\qquad
r_i={s_i\over\gcd(s_i,W)},
\qquad
\alpha_i={1\over r_i}.
\]

Then

\[
{\gcd(m_i,E)\over m_i}={1\over r_i}.
\]

There is a factor-free exact sampler for uniform local torus points. Work
in

\[
A_D=(\mathbb Z/N\mathbb Z)[w]/(w^2-D).
\]

For uniform \(z=A+Bw\), gcd-screen its norm and, on the unit branch, form

\[
U={z\over\bar z}.
\]

Over either hidden prime, Hilbert 90 has exactly \(r-1\) preimages for
every local torus point, in both the split and nonsplit quadratic algebras.
Consequently the accepted reductions \(U_p,U_q\) are independent and
uniform on the *full* local tori, including \(\pm1\). A coefficient pair is
clean with probability at least \(16/81\); every nonclean proper gcd is
already a verified factor.

The local return events under \(U^E\) are independent with exact
probabilities \(\alpha_p,\alpha_q\). On a simultaneous return, write
\(h_i=\min(v_2(m_i),v_2(E))\),
\(a=\min(h_p,h_q)\), and \(b=\max(h_p,h_q)\). Joint coefficient gcd
screens along the Miller square chain split the two components with exact
conditional probability

\[
\mu_{a,b}=1-{4^a+2\over3\,2^{a+b}}\ge {1\over2}.
\]

Thus one clean powered trial factors with exact probability

\[
S=\alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q
\]

and in particular

\[
\boxed{S\ge {1\over2\min(r_p,r_q)}}.
\]

No local sign is needed by the algorithm. Sampling a uniform unit \(D\)
makes the four hidden orientations

\[
(p-1,q-1),\quad(p-1,q+1),\quad
(p+1,q-1),\quad(p+1,q+1)
\]

equiprobable. The chosen \(D\) must be retained while coefficient pairs
are resampled, because clean-point density depends on the orientation. If
\(R_\epsilon\) is the smaller residual in orientation \(\epsilon\), the
complete factor-first trial obeys

\[
\Pr(\text{factor})
\ge {1\over8\min_\epsilon R_\epsilon}.
\]

If \(\log W\) and the relevant residual bound are numerical QP, binary
powering, algebra arithmetic, sampling, all gcd screens, and expected
repetition have numerical-QP bit cost. The word remains unfactored
throughout.

**Exact remaining gap.** Construct, for every distinct odd semiprime, a
public QP-bit word \(W\) that makes at least one of the four shifted
residuals numerical QP, or give a randomized integer source with an
all-input expected-QP progress law. The torus sampler supplies four exact
Las Vegas interfaces, but it does not prove that any interface is small.
A word depending materially on the full value of \(D\) is a new source
mechanism and needs a separate probability proof.

The V2 statement, proof, hostile re-audit, and strict blind reconstruction
have SHA-256 hashes
`4ec456a0aa8794e36497a663b14747eba15dcaebd7984a923b53169969c1bfbd`,
`8012cc4899226fec123a9f86d150e3dbe8fa199df88c4ee95651c3e0557f2090`,
`29e27f439e44f949223c533dca6d44d4ef3d17fecd603ad29d9466e5d20e8b95`,
and
`2f6ffc3151e5c1e30856e053528ab67f65576b28d16ebbedd80fb19c2c4a08b0`.
The preserved V1 strict blind failure concerned only an imported,
undefined counterfamily. No V2 computation, cross-family audit, human
audit, or publication-level literature review has run.

## P207 — the factored divisor lattice of \(N-1\) adds no multiplicative word support

**Status:** promoted from F240 V2 after a fresh hostile re-audit and a
strict statement-only reconstruction. This is a boundary theorem for a
narrow divisor-only grammar, not a factoring algorithm or a lower bound
against additive selectors.

Let \(N=pq\) for distinct odd primes \(p<q\), put

\[
M=N-1,\qquad d=\gcd(p-1,q-1),\qquad
s_p={p-1\over d},\quad s_q={q-1\over d},
\]

and grant the complete factorization and divisor lattice of \(M\). For any
divisor \(B\mid M\), integer \(u\ge1\), and round-half-up centers

\[
a=\left\lfloor {up\over B}+{1\over2}\right\rfloor,
\quad
b=\left\lfloor {uq\over B}+{1\over2}\right\rfloor,
\]

write \(x=up-aB\), \(y=uq-bB\), and \(H_B=M/B\). Then

\[
c={xy-u^2\over B}\in\mathbb Z,
\qquad
T=aq+bp={u^2H_B+abB-c\over u},
\]

and \(p\) is a root of

\[
bX^2-TX+aN=0,
\qquad
T^2-4abN=(aq-bp)^2.
\]

A public guessed tuple is safely verified by requiring \(a,b\ge0\),
rejecting \((a,b)=(0,0)\), and testing only integral proper divisors of
\(N\) obtained from the quadratic (or the harmless linear branch when
\(b=0\)). The exclusion is necessary: at \(B=M,u=1\), the true tuple has
\(a=b=0,c=1,T=0\), so the displayed polynomial is identically zero.

The hidden common divisor itself is the guaranteed zero-carry lattice
point. At \(B=d,u=1\),

\[
(a,b,x,y,c)=
\begin{cases}
(s_p,s_q,1,1,0),&d\ge4,\\
(s_p+1,s_q+1,-1,-1,0),&d=2.
\end{cases}
\]

Thus carry zero does not label \(d\): its hidden centers are exactly the
two P205 residuals, apart from the forced half-tie offset when \(d=2\).

The exact multiplicative boundary is sharper. For

\[
s_i^{\perp M}=
\prod_{\substack{\ell^e\parallel s_i\\ \ell\nmid M}}\ell^e,
\]

every word made only from divisors of \(M\) by multiplication, positive
powers, gcd, lcm, and exact division obeys

\[
s_i^{\perp M}\mid {s_i\over\gcd(s_i,W)}.
\]

The public unfactored word \(W=M^n\), where
\(n=\lceil\log_2(N+1)\rceil\), attains equality simultaneously for
\(i=p,q\) and has \(O(n^2)\) bits. Hence complete factorization of
\((N-1)/2\), complete divisor enumeration, and arbitrary multiplicative
reuse of those divisors cannot improve the P205 support beyond what
\((N-1)^n\) already supplies.

The exact surviving escape is additive. If a true signed residue is
selected, then

\[
aB+x-u=u(p-1),
\qquad
bB+y-u=u(q-1),
\]

so either integer saturates the corresponding P205 residual. Likewise a
QP bank containing the true nondegenerate \((a,b,c)\) tuple factors
directly. Factoring \(|u^2+cB|=|xy|\) does not by itself select the signed
divisor \(x\), and the number of divisors can be super-QP. This is an
enumeration warning, not a selector lower bound.

**Exact remaining gap.** Use additive divisor/carry data to select a true
centered residue, or construct a QP-bit word with new prime support outside
\(N-1\), with an all-input or inverse-QP guarantee. Factoring the divisor
lattice alone supplies neither result.

The V2 statement, proof, hostile re-audit, and strict blind reconstruction
have SHA-256 hashes
`d74ea1c31f24a59b643dc38d69326be553bc3944ef80cee4f72a7a2e607e9914`,
`1a4bb957465f2bceb0ce3166df5f1c56d7ece68af36a4a5f9cafa426aa3dd758`,
`1bccf6cb6e9c184202e513cb5bdaa8f99cd271f2c6e21749dca299d5fff97d14`,
and
`5f029c719731d3c1130e3ecc30b0a3cb7f3c809dd5d68099595a24bd51db3f06`.
The preserved V1 hostile failure found the repaired zero-polynomial
endpoint. No theorem computation, cross-family audit, human audit, or
publication-level literature review has run.

## P206 — modular collision energy is the exact difference-word source

**Status:** promoted from F241 after a fresh hostile audit and a strict
statement-only reconstruction. This is a conditional Las Vegas source
theorem for P205, not an all-input factoring algorithm.

Let \(N=pq\) for distinct odd primes, put

\[
n=\lceil\log_2(N+1)\rceil,
\quad d=\gcd(p-1,q-1),
\quad s_p={p-1\over d},\quad s_q={q-1\over d},
\]

and let \(s_i^\perp\) be the largest divisor of \(s_i\) supported on
primes not dividing \(N-1\). The deterministic public word

\[
W_0=(N-1)^n
\]

has \(O(n^2)\) bits and leaves exactly the P205 residuals

\[
r_p=s_p^\perp,
\qquad r_q=s_q^\perp.
\]

Thus every residual primary whose rational prime is already visible in
\(N-1\) is free; only support outside \(N-1\) remains.

Now let \(Z,Z'\) be fresh independent samples from any public exact
integer law, and define \(\Delta=|Z-Z'|\) when \(Z\ne Z'\), but
\(\Delta=1\) when \(Z=Z'\). For squarefree \(m\), put

\[
\kappa_m=Pr(Z\ne Z'\ \hbox{and}\ Z\equiv Z'\pmod m).
\]

For \(s=\prod_{\ell\in\mathcal P}\ell^{e_\ell}<N\), one has the exact
collision-energy identity

\[
\boxed{
\mathbb E{\gcd(s,\Delta^n)\over s}
={1\over s}\left[
1+\sum_{\varnothing\ne S\subseteq\mathcal P}
\left(\prod_{\ell\in S}(\ell^{e_\ell}-1)\right)
\kappa_{\prod_{\ell\in S}\ell}
\right].
}
\]

The exponent \(n\) saturates the full hidden primary power after one
collision modulo its rational prime. Equal integer samples are excluded
because they would create the false zero word. Applying P205 after the
word is sampled gives, history by history,

\[
\Pr(\mathrm{factor})\ge {1\over2}
\max\left(\mathbb E{1\over r_p},\mathbb E{1\over r_q}\right),
\]

provided the two integer samples and the later unit are conditionally
fresh. This identifies distinct-integer modular aliasing, not raw sample
entropy, as the exact useful statistic.

There is a concrete conditional source. Grant a complete factorization

\[
N-1=\prod_{j=1}^k b_j^{a_j},
\qquad T=\tau(N-1),
\]

and sample a uniform divisor \(Z=\prod_jb_j^{J_j}\). For squarefree
\(m\) coprime to \(N-1\), Parseval gives

\[
\kappa_m={1\over\varphi(m)}
\sum_{\chi}
\prod_j\left|{1\over a_j+1}
\sum_{e=0}^{a_j}\chi(b_j)^e\right|^2-{1\over T}.
\]

If \(h_m\) is the subgroup size generated by the reductions of the
\(b_j\), then

\[
\kappa_m\ge {1\over h_m}-{1\over T}.
\]

Consequently, if all prime divisors of one exterior residual have
\(h_\ell\le Q(n)\) for a public numerical-QP \(Q\), and
\(T\ge2Q(n)\), then
\(\lceil2Q(n)\log(2n)\rceil\) fresh divisor pairs produce a QP-bit word
that absorbs that residual with probability at least \(1/2\). A fresh
P205 trial then factors with total probability at least \(1/4\).

The subgroup hypothesis is essential. For \(N-1=b^a\), with
\(h=\operatorname{ord}_m(b)\), \(T=a+1=qh+r\), the exact distinct-sample
collision law is

\[
\kappa_m={h q(q-1)+2rq\over T^2}.
\]

It vanishes when \(h\ge T\): the integer samples are distinct and remain
distinct modulo \(m\). Random divisor radices are only pushforwards of the
same complementary-divisor law and add no independent carry entropy.

**Exact remaining gap.** Prove inverse-QP distinct-integer modular
aliasing, with enough primary weight, in one exterior residual on every
input. Exact samplability and large support alone do not imply this law.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`11cbe1a262a546ad05c3462f8189f3704a98e73b1725d334a487ad36f0d5c48b`,
`5150d7416741d8bfa45f832f6d41e621e12068cced8d1267e241616b399c9edb`,
`0e139800c942104310c715a8d8e6f97950b7d2a03fbbaf8814f98cd75d0dc298`,
and
`6eb17dc45bd04221d64b6b67dc416064eac2b32aeebdb357494e87a12eee9b29`.
The hostile audit records two harmless strict-inequality wording slips in
the proof. No theorem computation, cross-family audit, human audit, or
publication-level literature review has run.

## P205 — an unfactored word gives a Miller splitter for every odd semiprime

**Status:** promoted from F238 V2 after a fresh hostile audit and a strict
statement-only reconstruction. This is a conditional Las Vegas reduction,
not an all-input factoring algorithm: it does not construct the required
word on every input.

Let (N=pq) for distinct odd primes, without balance or zero-defect
assumptions, and put

\[
d=\gcd(p-1,q-1),\qquad
s_p={p-1\over d},\qquad s_q={q-1\over d}.
\]

For any public positive integer (W), whose factorization is not required,
define

\[
E=(N-1)W,\qquad
r_p={s_p\over\gcd(s_p,W)},\qquad
r_q={s_q\over\gcd(s_q,W)},
\]

and (alpha_p=1/r_p,alpha_q=1/r_q). The integer identity

\[
\gcd(N-1,p-1)=\gcd(N-1,q-1)=d
\]

gives exact independent local-return probabilities (alpha_p,alpha_q)
for a uniform unit modulo (N).

Write (e_i=v_2(i-1)), (v=v_2(E)),
(h_i=\min(e_i,v)), and

\[
a=\min(h_p,h_q),\qquad b=\max(h_p,h_q).
\]

Conditional on a verified global return, the local two-primary coordinates
remain independent and uniform in (C_{2^{h_p}}) and (C_{2^{h_q}}). A
Miller square chain splits exactly when their exact two-power orders differ,
with exact probability

\[
\mu_{a,b}=1-{4^a+2\over3\,2^{a+b}}\ge{1\over2}.
\]

Thus one complete trial has exact factor probability

\[
\boxed{
\alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q
}
\]

and the useful lower bound

\[
\boxed{
\Pr(\mathrm{factor})
\ge\mu_{a,b}\max(\alpha_p,\alpha_q)
\ge{1\over2\min(r_p,r_q)}.
}
\]

Therefore a public numerical-QP-bit word with
(min(r_p,r_q)=\operatorname{QP}(\log N)) gives a Las Vegas
numerical-QP splitter. Neither (W), (E), nor (N-1) is factored. Every
output is a verified proper gcd. The public exponent (N-1) automatically
exploits the entire hidden common divisor (d); accumulated common
certificates from P197 are divisors of the same capacity but are unnecessary
for this direct-factor reduction.

The optional multi-prime-support extension also holds. V1 used an invalid
last inference in its proof; the frozen V2 corrigendum repairs it with the
identity

\[
S-\mu a=(1-a)(1-B)+(1-\mu)a(1-C)\ge0.
\]

The semiprime theorem was unaffected.

**Exact remaining gap.** Construct from (N) a public QP-bit word (W)
that leaves one of the coprime residuals ((p-1)/d,(q-1)/d) numerical QP
on every input. Randomness supplies the Miller amplification after this
integer progress; it does not itself supply a hidden divisor of (W).

The V1 statement, proof, V2 corrigendum, hostile audit, and strict blind
reconstruction have SHA-256 hashes
`4be9c61c28826701960cdebdf326638d04ae00ec5ffa5db279ca3a7b5b19d2d9`,
`3dae9a2543dccd5ca52403dc3e6a732f75e34cb5dd16c6db3fe4507828946913`,
`459038e7d3ddfde462c5badbd41bd2ca7b076fb5c9952a97261103f33724414a`,
`7d8728ea0ffcc4a9802c84126c88eb6f5ce6a2758b5577db08001e8735e887d0`,
and
`94212f013ad6ab9b94a4aff79b903141b4f828a610d4b5e07037cb8f1b4e4b7c`.
The local manifest omitted its hash table; the audit authenticated the
externally frozen hashes before reading. A disclosed post-freeze random
diagnostic was excluded from evidence. No cross-family or human audit has
run.

## P204 — an unfactored QP-bit word gives a Miller-amplified zero-defect splitter

**Status:** promoted from F235 after a fresh hostile audit and a strict
statement-only reconstruction. This is a conditional Las Vegas splitter on
the balanced zero-defect branch. It is not an all-input factoring algorithm:
it does not construct a word leaving a numerical-QP residual on every input.

Let

\[
N=pq,\qquad p<q<2p,
\qquad n=\lceil\log_2(N+1)\rceil,
\qquad B=2^{\lfloor n/2\rfloor},
\]

where \(p,q\) are distinct odd primes, and assume

\[
B\mid N-1,\qquad H=(N-1)/B.
\]

Write

\[
p-1=2^eP,\qquad q-1=2^fQ,
\qquad D=\gcd(P,Q),
\qquad s_p=P/D,\quad s_q=Q/D.
\]

Zero defect and balance force

\[
\boxed{e=f\ge1},
\qquad
\gcd(H,P)=\gcd(H,Q)=D,
\qquad
\gcd(s_p,s_q)=1.
\]

Now let \(W\ge1\) be any public integer of numerical-QP bit length. Its
factorization is neither known nor needed. Put

\[
E=(N-1)W,
\qquad
r_p={s_p\over\gcd(s_p,W)},
\qquad
r_q={s_q\over\gcd(s_q,W)},
\qquad
\alpha_p={1\over r_p},\quad\alpha_q={1\over r_q}.
\]

For a uniform unit \(x\bmod N\), the two local return events are independent
and have exact probabilities

\[
\Pr(x^E=1\bmod p)=\alpha_p,
\qquad
\Pr(x^E=1\bmod q)=\alpha_q.
\]

If exactly one return occurs, \(\gcd(x^E-1,N)\) is a proper factor. If both
occur, run the ordinary Miller square chain using the verified return, not an
assumed universal annihilator. Conditional on this global return, the two
local \(2\)-Sylow coordinates remain independent and uniform in
\(C_{2^e}\). The chain splits exactly when their exact two-power orders
differ, with probability

\[
\mu_e={2\over3}(1-4^{-e})\ge{1\over2}.
\]

Consequently one complete trial factors with exact probability

\[
\boxed{
\alpha_p+\alpha_q-(2-\mu_e)\alpha_p\alpha_q.
}
\]

In particular, if \(s_p\mid W\) or \(s_q\mid W\), every fresh trial succeeds
with probability at least \(1/2\). This includes simultaneous saturation:
a global return is then useful through the Miller chain rather than a stale
common-order event. The expected number of trials is at most two, and no
factor-first stripping or recursive factorization of \(H\) is used.

More generally, the same exact formula gives

\[
\Pr(\text{factor})
\ge \mu_e\max(\alpha_p,\alpha_q)
\ge {1\over2\min(r_p,r_q)}.
\]

Thus it is enough for the word to leave either residual numerical QP; full
saturation is not necessary. This is a direct-factor probability, not an
lcm-growth statement.

Two public word families make the remaining source requirement precise.
First, for

\[
W_K=\prod_{k=1}^K(N^k-1),
\qquad
t_p=\operatorname{ord}_{s_p}(N),
\quad t_q=\operatorname{ord}_{s_q}(N),
\]

with the order modulo one defined as one,

\[
t_p\le K\Longrightarrow s_p\mid W_K,
\qquad
t_q\le K\Longrightarrow s_q\mid W_K,
\]

and

\[
\log_2W_K<{nK(K+1)\over2}.
\]

Thus a numerical-QP bound on \(\min(t_p,t_q)\) would close this branch.
No such all-input bound is proved.

Second, for any public positive children \(A_1,\ldots,A_J\), the unfactored
word

\[
W=\prod_{j=1}^J A_j^n
\]

contains the complete primary part of either residual supported on the union
of the child prime supports. Numerical-QP aggregate child encoding length
gives numerical-QP word length, without factoring a child. In particular,
shifted quotient children can be used directly as exponent factors.

The exact all-input gap is therefore an integer source theorem:

\[
\boxed{
\text{construct a public QP-bit }W
\text{ such that }\min(r_p,r_q)=\operatorname{QP}(n).
}
\]

The congruences

\[
N\equiv1+(q-p)\pmod{s_p},
\qquad
N\equiv1-(q-p)\pmod{s_q}
\]

show the factor-gap coupling but do not bound either meta-order. P204 removes
the factored-word and half-size-dispatch assumptions from P202's direct
factor branch; it does not solve this final residual-reduction problem.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`175f79d14b3c952fe3411ce6b716cc91815853896e2e78210a82f3f4d9f13698`,
`22402d37b0a638326e5fb29c3d3f6bc1a6809ba8c72ea38c80462dbaa4b525c8`,
`472063f98a5e72dbe0712f62fcfa1fd6b772573502dfd60bc78368755ac333c4`,
and
`12872053dbbc547aa9811cfc561b80efcc529f94f9d6a8fca6371346a89d4c45`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P203 — rectangular shifted quotient banks are projective gap-ratio covers

**Status:** promoted from F233 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact integer-incidence theorem
and a named source boundary. It is not an actual-input counterfamily or an
all-input factoring algorithm.

Retain the balanced zero-defect notation

\[
N=pq,\qquad p<q<2p,\qquad
B=2^{\lfloor n/2\rfloor},\qquad
B\mid N-1,\qquad H=(N-1)/B,
\]

and put \(g=q-p\). Write the odd local orders as

\[
P=(p-1)_{\rm odd},\qquad Q=(q-1)_{\rm odd},
\qquad D=\gcd(P,Q),\qquad s_p=P/D,\quad s_q=Q/D.
\]

Fix public numerical-QP values \(U,C,Y\), with

\[
Y\ge\max(U,C,3),\qquad 1\le U<B,\qquad1\le C<H,
\]

and use the shifted quotient children

\[
A_{u,c}=uH+c,
\qquad1\le u\le U,
\qquad-C\le c\le C.
\]

These are genuine integer quotient shifts because

\[
uN=(uH)B+u.
\]

Let \(\ell>Y\) be an exclusive residual prime with \(\ell\nmid H\), and
define its nonzero gap ratio

\[
\rho_\ell=gB^{-1}\pmod\ell,
\qquad
\mathcal R_\ell(U,C)=
\{cu^{-1}:1\le u\le U,\ 1\le|c|\le C\}\pmod\ell.
\]

Then the two hidden orientations obey the exact laws

\[
\ell\mid s_p:quad
\ell\mid A_{u,c}
\Longleftrightarrow ug+cB\equiv0\pmod\ell,
\]

\[
\ell\mid s_q:quad
\ell\mid A_{u,c}
\Longleftrightarrow-ug+cB\equiv0\pmod\ell.
\]

Because the shift interval is symmetric, either orientation is captured
exactly when

\[
\boxed{\rho_\ell\in\mathcal R_\ell(U,C).}
\]

Moreover, residual primes captured from \(s_p\) by \(A_{u,c}\) and from
\(s_q\) by \(A_{u,-c}\) have squarefree product dividing the one actual
integer

\[
|ug+cB|.
\]

Thus the source is genuinely integer-specific: it depends on the hidden
Archimedean gap, not only on generic unit-group operations.

The projective cover has exact elementary bounds. For every prime
\(\ell>\max(U,C)\),

\[
\ell\le C(U+1)
\Longrightarrow
\mathcal R_\ell(U,C)=\mathbb F_\ell^*,
\]

while

\[
|\mathcal R_\ell(U,C)|\le\min(\ell-1,2CU),
\]

so

\[
\ell-1>2CU
\Longrightarrow
\mathcal R_\ell(U,C)\ne\mathbb F_\ell^*.
\]

The first implication is sufficient rather than an optimal threshold; this
is the wording qualification recorded by the blind reconstruction.

Large-prime reuse also disappears after projective deduplication. If

\[
\ell>2UC,\qquad
\ell\mid uH+c,\qquad
\ell\mid vH+d,
\]

then elimination and \(\ell\nmid H\) give

\[
ud-vc=0
\]

as an integer. Hence the two pairs represent the same rational slope.

It follows that every prime for which the complete rectangle has a
residue-independent coverage guarantee is already below the numerical-QP
smooth cutoff

\[
Y_* = \max(Y,2UC+1).
\]

Replacing the bank by the ordinary smooth word through \(Y_*\) absorbs all
such guaranteed support. Any large-rough advantage must therefore prove an
actual number-theoretic statement forcing enough hidden ratios
\(\rho_\ell\) into the finite covers. Generic finite-field coverage and lcm
aggregation do not provide that statement.

If every exposed child prime is raised to exponent \(n\), all supported
hidden primary powers are saturated. Substitution into P202 gives the exact
post-bank residuals and its exact factor-or-growth law, conditional on the
declared all-input child-factorization dispatcher. P204 subsequently shows
that a direct-factor attempt can instead multiply the child values into one
unfactored word and avoid that dispatcher. Neither version supplies the
missing all-input gap-ratio incidence theorem.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`779fc3dafec72264ed0ae6bb0fee8835d2500cb70cfb2bcfea936d059841b510`,
`58f35d1037d37143da61d1296b2df3bac4279546bf1c2792cd4479402a003bbc`,
`ffd33c76b44f877d410fdadc2034cf58fc40b5d93e57155ddf916b51751a740b`,
and
`244b10d4a218fb4725e752e1a4e3117e266ae9128160c2209886324c2a4cd9e1`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P202 — a QP-bit smooth word closes one saturated zero-defect residual

**Status:** promoted from F231 after a fresh hostile re-audit and a strict
statement-only reconstruction. This is a conditional favorable-state theorem
and an exact return-law boundary. It is not an all-input factoring algorithm.

Let

\[
N=pq,
\qquad p<q<2p,
\qquad B=2^{\lfloor n/2\rfloor},
\]

with distinct odd primes, and assume the zero-defect branch

\[
B\mid N-1,
\qquad H={N-1\over B}.
\]

Grant a correct all-input recursive dispatcher that completely factors the
public half-size integer \(H\). Put

\[
P=(p-1)_{\rm odd},
\qquad Q=(q-1)_{\rm odd},
\qquad D=\gcd(P,Q),
\]

\[
s_p=P/D,
\qquad s_q=Q/D.
\]

Then \(\gcd(s_p,s_q)=1\) and

\[
\gcd(H,P)=\gcd(H,Q)=D.
\]

Maintain any certified odd common modulus \(M\mid D\), accumulated by lcm
from unrelated witnesses as in P197. For any public completely factored word
\(W\), define

\[
r_p={s_p\over\gcd(s_p,W)},
\qquad
r_q={s_q\over\gcd(s_q,W)}.
\]

Choose a uniform unit \(x\bmod N\), project it to odd order by
\(a=x^{2^n}\bmod N\), and use exponent \(A=WH\). The local return
probabilities are exactly

\[
\Pr(a^A=1\bmod p)=1/r_p,
\qquad
\Pr(a^A=1\bmod q)=1/r_q.
\]

After the initial gcd, completely strip the known prime powers of \(A\).
Unequal local orders expose a factor; equal local orders give their exact
common order. The exact factor-or-strict-growth probability is

\[
\boxed{
{1\over r_p}+{1\over r_q}-{1\over r_pr_q}
-{1\over PQ}\sum_{d\mid M}\varphi(d)^2.
}
\]

The final term is exactly the stale global-return probability. It includes
arbitrary prime powers in \(P,Q,D,M,W\), and it obeys

\[
{1\over PQ}\sum_{d\mid M}\varphi(d)^2
\le
\left({M\over D}\right)^2{1\over s_ps_q}.
\]

This formula identifies the useful Las Vegas role of a long integer word:
it changes the local return kernels, while independently certified common
primary blocks still accumulate in \(M\).

For a public \(Y\ge3\), let

\[
\Lambda_Y=\operatorname{lcm}(1,\ldots,Y),
\qquad U_Y=\Lambda_Y^n.
\]

Every \(Y\)-smooth integer below \(N\), including all of its prime powers,
divides \(U_Y\). If at least one of \(s_p,s_q\) is \(Y\)-smooth, then one
residual is one. The edge case \(s_p=s_q=1\) is impossible here: writing
\(p=2^eD+1\), \(q=2^fD+1\), balance forces \(f=e+1\), hence
\(v_2(N-1)=e\), while \(B\mid N-1\) requires at least \(e+1\) powers of
two. Therefore \(s_ps_q\ge3\), and every history has

\[
\boxed{
\Pr(\text{factor or strict }M\text{-growth})
\ge 1-{1\over s_ps_q}\ge {2\over3}.
}
\]

This needs no terminal-capacity premise. Once \(M=D\), every useful event is
a factor. There are fewer than \(n\) strict lcm-growth events, so fresh
stages factor almost surely in at most \(3n/2\) expected stages. If beta-two
carry bits are also available, each updated
\(\operatorname{lcm}(2^t,M)\) may invoke the P197 known-residue terminal
earlier.

The factorization of \(H\) supplies a stronger integer-specific word at
only \(O(n^2)\) extra bit length:

\[
\widehat U_Y
=U_Y\prod_{\substack{\ell\mid H\\\ell>Y}}\ell^n.
\]

It absorbs every residual primary whose rational prime is either at most
\(Y\) or occurs in the public child \(H\). The only surviving residual
prime powers have \(\ell>Y\) and \(\ell\nmid H\).

If the numerical value of \(Y\) is numerical QP, then

\[
\log_2 U_Y\le nY\log_2Y,
\]

so sieving, the factor list, modular powers, gcds, and all punctures have
numerical-QP bit cost. Lcm aggregation of several factored words is a safe
monotone aggregator whose height and factor-list size are bounded by the
input totals. Products may also add repeated prime valuations; the lcm is
the minimal simultaneous aggregator, not the only possible factored word.

For \(W=U_Y\), the residuals consist exactly of the prime powers of
\(s_p,s_q\) above \(Y\). If both remain nontrivial, every declared factor or
certificate requires a local return and hence has probability at most

\[
{1\over r_p}+{1\over r_q}.
\]

Thus the remaining all-input problem is precise: construct, from the
integer data, a QP-height factored word that saturates one residual (or makes
a residual numerical QP) at every reached state. Marginal one-coordinate
identity mass is insufficient unless simultaneous stale returns are also
controlled. F231 still assumes the missing correct all-input dispatcher for
the arbitrary half-size child \(H\).

The statement, proof, frozen hostile re-audit, and strict blind
reconstruction have SHA-256 hashes
`f7503be5f8db21697157bc6f267b5719e656d55b395f8d8d524c5a0661d1dd56`,
`02a8c7a863bbec8b4bbd2475b617456a1d4e059c44e693c96526f7ae60c663c5`,
`d3f5fd41c13d42aa72440659a2e8de26212bb6ff7b04e7a2507fc8125749c896`,
and
`210eec7c88a32e5d363d6c357b24a82748d6c5b225e992fb250e9a807271ed68`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P201 — diffuse candidate exponents cannot replace an integer-biased fixed base

**Status:** promoted from F227 V5 after a fresh hostile re-audit and a
strict statement-only reconstruction. This is a source boundary and an
oracle-relative favorable-state theorem. It is not an all-input factoring
algorithm.

Let

\[
N=pq,
\qquad p<q<2p,
\]

with distinct odd primes. Suppose the beta-two/common-modulus state gives
an even integer \(L\ge2\) and a residue \(s\pmod L\) such that

\[
p\equiv s\pmod L,
\qquad \gcd(L,N)=1.
\]

In the balanced factor interval put

\[
\mathcal C=
\{x\in[\lceil\sqrt{N/2}\rceil,\lfloor\sqrt N\rfloor]:
x\equiv s\pmod L\},
\qquad H=|\mathcal C|,
\]

and attach the completely factored candidate exponent \(A_x=x-1\).

For an arithmetic progression \(A_j=c+jL\), a law of largest atom
\(\eta\), and every positive integer \(m\), F227 proves

\[
\boxed{
\mathbb E{\gcd(A_j,m)\over m}
\le
\eta\left({HL\tau(m)\over m}+1\right).
}
\]

After the candidate and all its public preprocessing are fixed, let the
base be a fresh independent uniform unit modulo \(N\). For the declared
candidate gcd, return gcd, and complete factor-first stripping screens,

\[
\Pr(\text{factor or new common primary block})
\le
\eta\left[
3+HL\left({\tau(p-1)\over p-1}
+{\tau(q-1)\over q-1}\right)
\right].
\]

Exact rejection sampling of a unit adds only the proper-nonunit mass

\[
{p+q-2\over N-1}=O(1/p).
\]

Fix one numerical-QP envelope \(Q(n)\). At every preterminal state

\[
L<{N^{1/4}\over S(n)},
\qquad 1\le S(n)\le Q(n),
\]

the factor cell has \(H=\Theta(p/L)\). Hence any adaptive bank of at most
\(Q(n)\) trials whose conditional candidate laws satisfy
\(\eta H\le Q(n)\), and whose fresh bases satisfy the stated conditional
independence, has total useful probability

\[
\boxed{2^{-\Omega(n)}}.
\]

The conclusion is history-wise and needs no independence between trials.
It grants the complete factorization of every candidate exponent. It does
not cover heavy candidate atoms, candidate/base coupling, integer-biased
bases, or joint processing of nonreturns.

The fixed-base law is the complementary positive statement. For a public
unit \(a\), write

\[
o_p=\operatorname{ord}_p(a),
\qquad
o_q=\operatorname{ord}_q(a),
\qquad
u_p={o_p\over\gcd(o_p,L)}.
\]

The base is stale in the declared order channel exactly when

\[
o_p=o_q\mid L.
\]

If it is not stale, a uniform candidate gives a factor or strict common
modulus growth with probability at least

\[
\boxed{
{\lfloor H/u_p\rfloor\over H}
\ge {1\over u_p}-{1\over H}.
}
\]

Thus \(u_p\le Q(n)\) gives inverse-QP progress whenever \(H\ge2Q(n)\),
while a smaller cell can be enumerated directly. Complete factor-first
stripping is essential: a simultaneous return either exposes unequal local
orders or certifies their exact common order, unless that order already
divides \(L\).

Factoring \(A_x\) is deliberately charged to an external correct all-input
Las Vegas oracle. F227 proves only the current-node accounting. There are at
most

\[
\left\lceil\log_2{J_N\over L_0}\right\rceil=O(n),
\qquad
J_N=\left\lceil{N^{1/4}\over S(n)}\right\rceil,
\]

same-size growth states. At each state, the expected number of half-size
oracle calls is at most \(2Q(n)\). This is not a recursive all-input theorem,
because \(x-1\) is an arbitrary even integer.

On the named P161 rough-order branch, if every prime divisor of \(o_p\)
exceeds a cap \(T(n)>Q(n)\), then

\[
u_p=1\quad\text{or}\quad u_p>T(n).
\]

Thus the favorable QP-residual regime collapses to \(o_p\mid L\). The
remaining source problem is exact: manufacture a nonstale public base with
this property with inverse-QP conditional probability, or use a genuinely
integer-biased coupled law. Fresh uniform randomness does not do it. A
separate all-input dispatcher for the arbitrary exponent children is also
still missing.

The blind reconstruction's PASS uses the narrow declared-screen
interpretation above; it is not an upper bound against arbitrary extra gcd
queries hidden in preprocessing. The V5 statement, proof, hostile re-audit,
and strict blind reconstruction have SHA-256 hashes
`b4f1ad6826f867105cd4cafaaeaa02ea6914a92ff1986be1698f10a136a457c1`,
`92c1869539e78b247823d89ff29d2194c63368296b13bd10ca18b6b26810ee6f`,
`8aa93193126b6cae5a78c29fe803481d46f036112441ecf67868c49d3b8d7328`,
and
`5c6356706a307405bdadd090e5decf08b546fa2349bfafe7f45909178e3369ff`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P200 — the zero-defect quotient branch has an exact odd-order Las Vegas dichotomy

**Status:** promoted from F230 after a fresh hostile audit and a strict
statement-only reconstruction. This is a favorable-state theorem and a
matching bounded-source boundary. It is not an all-input factoring
algorithm.

Let

\[
N=pq,
\qquad p<q<2p,
\qquad B=2^{\lfloor n/2\rfloor},
\]

where \(p,q\) are distinct odd primes. For odd \(1\le u<B\), write

\[
uN=Q_uB+R_u,
\qquad 0<R_u<B,
\]

and define

\[
A_{u,c}=Q_u+c,
\qquad E_{u,c}=u-R_u+cB.
\]

The exact zero-defect branch is

\[
\boxed{
E_{u,c}=0
\iff
B\mid N-1\text{ and }c=0.
}
\]

Putting

\[
H={N-1\over B}
\]

then gives

\[
R_u=u,
\qquad Q_u=uH,
\qquad A_{u,0}=uH.
\]

Thus multiplier randomization does not create independent quotient children
in this branch. It exposes one public half-size integer \(H\), and every
child is a known small multiple of it. A complete factorization of \(H\),
together with a sieve of a numerical-QP multiplier range, factors every
exponent \(uH\).

Write the odd local group orders as

\[
P=(p-1)_{\rm odd},
\qquad Q=(q-1)_{\rm odd},
\qquad D=\gcd(P,Q),
\]

and

\[
s_p=P/D,
\qquad s_q=Q/D.
\]

Then

\[
\gcd(s_p,s_q)=1,
\qquad
\gcd(H,P)=\gcd(H,Q)=D.
\]

For a uniform unit \(x\bmod N\), put

\[
a=x^{2^n}\pmod N.
\]

Its two CRT coordinates are independent and uniform in the odd-order
subgroups of sizes \(P,Q\). Therefore, for every fixed odd multiplier \(u\),

\[
\alpha_p(u)=\Pr(a^{uH}=1\bmod p)
={\gcd(u,s_p)\over s_p},
\]

\[
\alpha_q(u)=\Pr(a^{uH}=1\bmod q)
={\gcd(u,s_q)\over s_q}.
\]

The exact proper-factor probability is

\[
\alpha_p+alpha_q-2\alpha_p\alpha_q,
\]

and the global-return probability is \(\alpha_p\alpha_q\).

This yields a history-wise Las Vegas progress theorem. Let \(U(n)<B\) be
public and numerical QP. Maintain an odd certified common modulus \(M\mid D\)
and suppose

\[
\min(s_p,s_q)\le U(n).
\]

If the current beta-two residue has precision \(2^t\), assume also that the
available odd capacity reaches the known-residue threshold:

\[
\operatorname{lcm}(2^t,D)
\ge
J:=\left\lceil {N^{1/4}\over S_0(n)}\right\rceil,
\]

where \(S_0(n)\ge1\) is fixed numerical QP. Scan every odd \(u\le U\), use
fresh projected units, and perform complete factor-first stripping of every
global return.

If \((s_p,s_q)\ne(1,1)\), one bank entry annihilates one complete odd local
subgroup and returns a proper factor with probability at least \(2/3\). If
\(s_p=s_q=1\), preterminality forces a missing primary \(\ell^k\mid D\).
At \(u=1\), the two independent local orders contain that primary with
probability at least

\[
(1-1/\ell)^2\ge4/9.
\]

Unequal valuations factor; equal valuations certify strict common-primary
growth. Hence every preterminal history has factor-or-growth probability at
least

\[
\boxed{4/9}.
\]

The P197 potential has at most \(n\) levels, so the expected number of bank
stages is at most \(9n/4\). Once
\(\operatorname{lcm}(2^t,M)\ge J\), the verified known-residue terminal
factors \(N\). This cost statement is conditional on a correct all-input
recursive dispatcher supplying the complete factorization of the half-size
integer \(H\).

One uniform odd multiplier succeeds with probability at least

\[
{4\over9\lceil U/2\rceil}.
\]

Conversely, after the direct gcd screen, any use of one fresh uniform odd
projection with an adaptively preselected \(u\le U\) has useful probability
at most

\[
U\left({1\over s_p}+{1\over s_q}\right).
\]

Thus the same source is exponentially sparse when both residual odd orders
are exponential. For a raw uniform integer sampler, add the exponentially
small nonunit-gcd atom. Carry-correlated multipliers, nonuniform projected
witnesses, APR-compatible residues, and other uses of the factorization of
\(H\) remain open.

The hostile F228 witness becomes a positive exact example:

\[
2881=43\cdot67,
\quad B=64,
\quad H=45,
\quad (s_p,s_q)=(7,11).
\]

At \(u=7\), the direct-factor probability is \(10/11\).

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`96edf9b0eb183364ce9178385e289e8e7c5dc967d32f74912aaff7548ba5999f`,
`2a07b604ac59d3090ed6cc7e46c8c4aed197665ce79db84068b802031a82d407`,
`1de0974cbdade6ef5ae1ba08f9ca1b4cf9d0cc47f8ada1c6a2fdf0a4cf14436e`,
and
`a49385bd933f1c1b5550a8a1857ea19f92e98febf88ffad0716dea645f32d17d`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P199 — small integers and fully mixed small-prime words cannot drive the aggregate-order sampler

**Status:** promoted from F229 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact obstruction for three
declared integer-sampling laws on one infinite balanced semiprime family. It
is not a factoring lower bound and does not cover intermediate nonuniform
integer words.

The bounded-prime-gap theorem supplies one fixed even integer \(d\ge2\) and
infinitely many odd prime pairs

\[
q=p+d,
\qquad N=pq,
\qquad p<q<2p.
\]

Grant the complete factorization of \(A=N-1\). For every unit integer \(X\),
the opposite exponent reductions modulo the two hidden primes give the exact
identity

\[
\boxed{
\gcd(X^{N-1}-1,N)=\gcd(X^d-1,N).
}
\]

Indeed, \(N-1\equiv d\pmod {p-1}\) and
\(N-1\equiv-d\pmod {q-1}\); inversion at \(q\) preserves the zero event.
Consequently every global return has both local orders dividing \(d\).
Every common primary block certified by the P197 factor-first tests divides
\(d\), and the lcm of arbitrarily many such blocks remains at most \(d\).
The identity case \(X=1\) has order one and gives no nontrivial block.

This collapse has three exact sampling consequences.

1. For every fixed numerical-QP value bound \(H(n)\), eventually
   \(H(n)^d<p\). Hence every ordinary integer \(2\le X\le H(n)\) has
   \(\gcd(X,N)=1\) and no local return. More generally, a positive product
   word \(X=\prod_j b_j\), \(b_j\ge2\), cannot return before

   \[
   \sum_j\log_2b_j\ge {\log_2p\over d}
   ={n\over2d}+O(1).
   \]

   This height condition is necessary, not sufficient.

2. Let the history choose any integer \(H\ge2\), then draw \(X\) uniformly
   from \(\{2,\ldots,H\}\). If \(H^d<p\), useful probability is zero.
   Otherwise root counting for \(T^d-1\) gives

   \[
   \Pr(\text{factor or certified new block})
   \le {4+4d\over p}+{4d\over H}
   \le(4+8d)p^{-1/d}
   =2^{-\Omega(n)}.
   \]

   This is an upper bound, not a matching asymptotic. It holds conditionally
   at every history and for arbitrary interval height.

3. Let \(B\) be numerical QP with
   \(\log n=o(\log B)\) and \(\log B=o(n)\), and even grant an exact uniform
   sample from the subgroup of \((\mathbb Z/N\mathbb Z)^\times\) generated
   by every rational prime at most \(B\). Projection to each hidden field is
   uniform on its image. The local \(d\)-torsion therefore has probability
   at most \(d/|G_p(B)|\) and \(d/|G_q(B)|\). Every positive \(B\)-smooth
   integer below the corresponding prime injects into that image, so the
   smooth-number lower bound yields

   \[
   |G_p(B)|\ge\Psi(p,B)=p^{1-o(1)},
   \qquad
   |G_q(B)|\ge\Psi(q,B)=q^{1-o(1)}.
   \]

   Thus

   \[
   \Pr(\text{proper or global return})
   \le {d\over\Psi(p,B)}+{d\over\Psi(q,B)}
   =2^{-n/2+o(n)}.
   \]

No independence between the two projections is used. An exact subgroup
sampler is granted rather than constructed.

The surviving integer-specific source is therefore sharply intermediate.
It must build a long, deliberately nonuniform word whose exact integer
value creates a genuine factor-scale wrap in

\[
X^d-1
\]

and places inverse-QP mass on a one-sided return or a genuinely new common
primary block. Bounded values have not wrapped; full mixing makes the fixed
\(d\)-torsion exponentially sparse. P199 does not rule out such a biased
word law, carry/quotient labels, joint processing of failed samples, or any
other factoring mechanism.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`715d27021f59e53f2d1198ae7440985d8cf7749123aa2f94463d9d870ce49dfb`,
`3554973f56f9c48b4ef727473fc016e1d2fe6939067a12b1a5999934e20e475d`,
`b1ebb7c9704bd78f7b639fe77f5ae312b03de41c2d43d9840868abb7c3c5f89c`,
and
`8bbfad2bcba668e17a1bd57138a22853acc32bc437a1b2e3b3275ab0b15f7aea`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P198 — exact-uniform half-size binary children give a conditional Las Vegas compatible-support source

**Status:** promoted from F226 after a fresh hostile audit and a strict
statement-only reconstruction. This is a conditional source theorem and a
named source boundary. It is not an all-input factoring algorithm.

Let \(N\ge3\) be odd,

\[
n=\lceil\log_2(N+1)\rceil,
\qquad m=\lfloor n/2\rfloor,
\qquad B=2^m.
\]

Choose \(u\) uniformly among the odd residues modulo \(B\), and define the
canonical binary-prefix children

\[
R_j(u)=uN\bmod 2^j,
\qquad 2\le j\le m.
\]

Multiplication by odd \(N\) permutes the odd residues modulo \(B\). Hence
\(R_m(u)\) is exactly uniform among the odd integers in \([1,B)\), while

\[
R_{j+1}(u)\in\{R_j(u),R_j(u)+2^j\}.
\]

Changed consecutive prefixes are coprime; arbitrary nonconsecutive prefixes
need not be. One bank has \(O(n)\) distinct half-size children and total
encoded length \(O(n^2)\). A numerical-QP number of independent banks,
including the complete factorizations of the children and of every exposed
\(\ell-1\), has a numerical-QP recursion tree **provided** a correct
all-input factoring dispatcher is already available for every arbitrary
half-size child. The theorem proves the recursive cost, not that missing
dispatcher.

The complete multiplier ensemble is exact and integer-specific:

\[
\{R_m(u):u\bmod B\text{ odd}\}
=\{1,3,\ldots,B-1\}.
\]

Consequently its full prime multiset is independent of \(N\), and a fixed
odd prime \(\ell<B\) occurs in one full child with exact probability

\[
\pi_\ell=
\frac{\left\lceil\frac12\left\lfloor(B-1)/\ell\right\rfloor\right\rceil}
     {B/2}
\le \frac1\ell+\frac2B.
\]

One prefix bank exposes \(\ell\) with probability at most
\(\min(1,(m+4)/\ell)\).

Now assume \(N=pq\) with distinct odd primes. For an exposed auxiliary prime
\(\ell\), put \(h_\ell=\operatorname{ord}_\ell(N)\). Then

\[
p\in\langle N\rangle\pmod\ell
\Longleftrightarrow
q\in\langle N\rangle\pmod\ell.
\]

When this holds, \(p\equiv N^{i_\ell}\pmod\ell\) for a unique class modulo
\(h_\ell\). Several rows admit one exponent precisely when the classes pass
the generalized-CRT compatibility conditions. For fixed \(i\ge0\), every
compatible auxiliary prime divides the hidden integer

\[
N^i-p.
\]

Thus the squarefree compatible support for \(0\le i<T\) has total binary
logarithm below \(nT\), but there is no unconditional lower bound on its
harmonic mass.

F226 removes the hidden-subset oracle from this conditional source. Sample
\(s=(\log n)^{O(1)}\) independent full children, recursively factor them,
and let \(W\) be the squarefree product of all exposed odd primes. If
\(2^{\omega(W)}\le D\), enumerate every squarefree divisor \(d\mid W\) and
every \(0\le i<T\), combine

\[
p\equiv N^i\pmod d
\]

with the current beta-two/common-order modulus \(L_0\), and invoke the
verified known-residue terminal whenever the combined modulus reaches
\(N^{1/4}/\operatorname{QP}(n)\). Every returned factor is gcd-verified.
Moreover,

\[
\mathbb E\,2^{\omega(R_m)}\le 2+\log B,
\qquad
\Pr(2^{\omega(W)}>D)
\le\frac{(2+\log B)^s}{D}.
\]

If \(C_i\) is the compatible subproduct captured by the block and
\(X_i=\log_2C_i\), then

\[
\mathbb E X_i
=\sum_{\ell\in\mathcal G_i}
  \log_2\ell\,[1-(1-\pi_\ell)^s].
\]

An inverse-QP surplus of this expectation above the remaining terminal
threshold gives an explicit inverse-QP verified transition after choosing
the divisor-cap tail smaller than that surplus. In particular, fix a public
numerical-QP bound \(Q(n)\). If some hidden odd squarefree
\(d\le Q(n)\) divides \(p-1\) or \(q-1\), if

\[
\operatorname{lcm}(L_0,d)
\ge N^{1/4}/\operatorname{QP}(n),
\qquad 4d\le B,
\]

then the public cap

\[
D=4Q(n)(2+\log B)
\]

makes one block succeed with probability at least \(1/(4Q(n))\). The
algorithm need not know \(d\): complete divisor enumeration tries it.

The exact boundary is equally important. The child-value ensemble is
\(N\)-independent; scalar character products leave the affine inversion
torsor unoriented; compatible support above a chosen QP cutoff contributes
only a QP-over-cutoff expected logarithmic weight; and one terminal-size
small-order auxiliary prime is exponentially unlikely. Quotient/carry
labels \(\lfloor uN/B\rfloor\), non-scalar identities, and a uniform
all-input harmonic-support theorem remain outside this boundary.

The preregistered finite scans are guidance only. Among 7,212 deterministic
half-bank rows, 797 missed the ideal-oracle threshold and 54 exposed no
accepted prime. The smallest zero-acceptance witness was

\[
333859=563\cdot593,
\]

with distinct children \(3\) and \(35=5\cdot7\). Exact enumeration of random
multipliers on those finite rows was favorable, but supplies no asymptotic
probability theorem.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`204b34f248610717000bc7d90dc80836125b78844fb23e6142412e0652ea6d40`,
`534f0a8fe8c0464678bb7e854ffd341a490e8a293b1559574eb2db374406c65f`,
`f20de258591d32ce7e2395cfe3859d6c5687dbcd11ce899d3f112e56541cc5e6`,
and
`57544809b27eee2b49a171c33cb2dfabe1d30ab60fbdba662a4c8a1dfa6ddc92`.
No cross-family or human audit has run.

## P197 — aggregate primary certificates give the exact beta-two Las Vegas drift target

**Status:** promoted from F220 V2 after a fresh hostile re-audit and a
strict statement-only reconstruction. This is the framework theorem for
the accumulated-order Las Vegas route. It is conditional on a witness
source with inverse-QP progress; it is not an all-input factoring algorithm.

Let \(N>1\) be odd. Suppose a completely factored integer

\[
A=\prod_\ell\ell^{e_\ell}
\]

and a public unit \(a\) satisfy \(a^A=1\pmod N\). For every
\(\ell^{e_\ell}\parallel A\), compute

\[
g_\ell=\gcd(a^{A/\ell}-1,N).
\]

A proper value factors \(N\). If \(g_\ell=1\), then for every rational
prime \(r\mid N\), reduction modulo \(r\) shows

\[
v_\ell(\operatorname{ord}_r(a))=e_\ell,
\qquad
\ell^{e_\ell}\mid r-1.
\]

Thus

\[
c(A,a)=
\prod_{\substack{\ell^{e_\ell}\parallel A\\g_\ell=1}}
\ell^{e_\ell}
\]

is a certified common primary block. Blocks from unrelated witnesses may be
accumulated:

\[
M=\operatorname{lcm}_i c(A_i,a_i)
\quad\Longrightarrow\quad
M\mid r-1\quad(r\mid N).
\]

No witness needs the same complete local order in every component, and no
single public element needs exact order \(M\).

On a balanced semiprime \(N=pq\), suppose the beta-two carry gives
\(b=p\bmod2^t\). Put

\[
L=\operatorname{lcm}(2^t,M).
\]

Generalized CRT gives one public residue \(s\pmod L\) with

\[
p\equiv s\pmod L,
\qquad
\gcd(L,N)=1.
\]

A gcd screen handles \(L>p\); otherwise the GFHP known-residue terminal
factors in numerical-QP time once

\[
L\ge J_{\rm G}:=
\left\lceil {N^{1/4}\over S(n)}\right\rceil
\]

for any fixed positive numerical-QP function \(S\).

The exact Las Vegas potential is

\[
\Phi(L)=
\max\left\{0,
\left\lceil\log_2{J_{\rm G}\over L}\right\rceil
\right\}.
\]

If each stage has a uniform numerical-QP bit-cost bound and, at every
nonterminal history,

\[
\mathbb E[\Phi_k-\Phi_{k+1}\mid\mathcal F_k]
\ge {1\over Q(n)},
\]

then optional-stopping by direct telescoping gives

\[
\mathbb E\tau\le O(nQ(n)).
\]

The procedure terminates almost surely and has expected numerical-QP bit
complexity. A sufficient condition is conditional inverse-QP probability
of either a factor or a block \(c\nmid L\). Conversely, the drift condition
implies such useful-event mass after only an \(O(n)\) loss. No independence
between stages is required. This uniform history-by-history condition is
not claimed necessary for every possible expected-QP source.

For a completely factored \(A\) with \(\gcd(A,N)=1\) and a uniform unit
\(a\), F220 also proves the exact no-progress law for arbitrary odd prime
powers. Write

\[
N=\prod_{j=1}^{\nu}r_j^{f_j},\qquad
h_j=\varphi(r_j^{f_j}),\qquad
d_j=\gcd(A,h_j)=\gcd(A,r_j-1),
\]

\[
B=\prod_j\left(1-{d_j\over r_j-1}\right),
\qquad
\Gamma=\prod_j{d_j\over h_j}.
\]

For \(\ell^{e_\ell}\parallel A\), let
\(c_\ell=\#\{j:v_\ell(d_j)=e_\ell\}\), and define

\[
f_\ell(L)=
\begin{cases}
1,&c_\ell=0,\\
\ell^{-c_\ell},&0<c_\ell<\nu,\\
\ell^{-\nu},&c_\ell=\nu,\ e_\ell>v_\ell(L),\\
\ell^{-\nu}+(1-\ell^{-1})^\nu,
 &c_\ell=\nu,\ e_\ell\le v_\ell(L).
\end{cases}
\]

Then one sample returns neither a factor nor strict lcm growth with exact
probability

\[
P_{\rm np}(L)=B+\Gamma\prod_{\ell\mid A}f_\ell(L).
\]

This formula allows different witnesses to contribute different primary
powers.

The attainable deterministic ceiling is

\[
D_N=\gcd_{r\mid N}(r-1),
\qquad
M\mid D_N,
\qquad
L\mid\operatorname{lcm}(2^t,D_N).
\]

Hence a ceiling below \(J_{\rm G}\) blocks aggregate growth, although a
proper gcd may still factor. On bounded-gap semiprimes,
\(D_N=\gcd(p-1,q-1)\mid q-p\), and uniform \((N-1)\)-annihilator
sampling has useful probability at most

\[
{D_N\over p-1}+{D_N\over q-1},
\]

which is exponentially small on the infinite bounded-gap family.

Finally, a source confined to one synchronized cyclic direction of order
\(c\), with \(\gcd(c,N)=1\), never splits \(N\): every factor-first gcd
is \(1\) or \(N\), and every certified block divides \(c\). Uniform
exponents fill each \(\ell\)-primary part after \(k\) samples with failure
probability \(\ell^{-k}\), but they cannot leave that direction. Thus
randomness can efficiently fill available common capacity; it does not
prove that the capacity reaches the terminal.

The exact missing theorem is now a source law: at every preterminal state,
produce a verified factor or genuinely new common primary support with
inverse-QP conditional probability. The dyadic carry itself, arbitrary
composites, and complete recursion remain outside P197.

The V2 statement, proof, hostile re-audit, and strict blind reconstruction
have SHA-256 hashes
`935ef9a28dff6bfade891ca069eb5d544236977c4c8c20c6d4208ff582b5fe45`,
`99ae21becd47b17a288af31670ba5a6df96529164a93c2b39e5704ef520af99d`,
`97eaa8e2ba4d9c380a932bd4857bacd50b49289f554daf459f4b15dee769467b`,
and
`92799679d950c231b89e2c9157365de77435e75c88b9e65ebfc12ba5b8f8cd02`.
The hostile audit records one editorial `)mid` typo in the frozen proof;
it does not affect the theorem. No cross-family or human audit has run.

## P196 — compatible APR/CL orbit residues can enlarge the beta-two terminal, while fixed and generic sources need not supply progress

**Status:** promoted from F223 V2 after a fresh hostile re-audit and a
strict statement-only reconstruction. This is a conditional residue
accumulator plus exact source boundaries. It is not an all-input factoring
algorithm and does not supply the compatible APR/CL certificate.

Let \(q\nmid N\) be prime, let \(r\in(\mathbb Z/q\mathbb Z)^\times\), and
put \(h_q=\operatorname{ord}_q(N)\). The following are equivalent:

\[
r\in\langle N\rangle\pmod q,
\]

and there is one integer \(i\) such that

\[
\chi(r)=\chi(N)^i
\]

for every multiplicative character modulo \(q\). When this holds, the
complete exponent set is one residue class

\[
i\equiv i_q(r)\pmod {h_q}.
\]

For several auxiliary primes, one global exponent exists exactly when

\[
i_q(r)\equiv i_{q'}(r)
 \pmod{\gcd(h_q,h_{q'})}
\]

for every pair. Independent local orbit membership is therefore
insufficient.

Under the full hypotheses of Cohen--Lenstra Theorems 6.3 and 7.8, their
condition (6.4) supplies one primary \(p\)-adic exponent
\(\ell_p(r)\), independent of the auxiliary prime and character. Passing
the corresponding Gauss/Jacobi-sum relations gives

\[
\chi(r)=\chi(N)^{\ell_p(r)}.
\]

The primary exponents combine by CRT, and the theorem concludes

\[
r\equiv N^i\pmod S
\]

for one exponent in a public finite set. A failed APR/CL identity proves
compositeness but is not, by itself, a numerical factor.

This compatible residue has an exact beta-two terminal. Assume

\[
N=pq,\qquad p<q<2p,
\]

and suppose public certified data give

\[
0\le b<2^\tau,\qquad p\equiv b\pmod {2^\tau},
\]

an integer \(M\) satisfying

\[
M\mid r-1\qquad\text{for every rational prime }r\mid N,
\]

and a unit modulus \(S\) with a QP-enumerable set \(I\) such that every
prime divisor \(r\mid N\) obeys

\[
r\equiv N^i\pmod S
\]

for some \(i\in I\). If \(\tau\ge n\), canonicality forces \(b=p\), so
a gcd factors \(N\) without constructing \(2^\tau\). Otherwise put

\[
L_0=\operatorname{lcm}(2^\tau,M),\qquad
L=\operatorname{lcm}(L_0,S).
\]

Generalized CRT first produces the true residue of \(p\) modulo \(L_0\),
then combines it with each \(N^i\pmod S\). At least one retained residue
is \(p\pmod L\), and \(\gcd(L,N)=1\). Hence the Gao--Feng--Hu--Pan
known-residue algorithm factors \(N\) in numerical-QP bit complexity once

\[
L\ge {N^{1/4}\over\operatorname{QP}(n)}.
\]

No single public element of exact order \(M\) is required. The certificate
\(M\mid r-1\) may be accumulated as an lcm of independently certified
common primary blocks.

Three exact boundaries prevent treating the compatible residue as an
automatic Las Vegas source.

1. For every fixed finite auxiliary-prime bank, infinitely many balanced
   semiprimes have both hidden primes congruent to \(-1\) modulo every odd
   bank prime while \(N\equiv1\). Every odd row then rejects both factors;
   the row at 2 is vacuous.
2. In a model where the hidden residues at different auxiliary primes are
   independent uniform units, the accepted-product tail has the exact
   Bernoulli moment products stated in F223. This is only a probability
   model, not an all-input number-theoretic law.
3. For the primary-prime-2 exponent \(E=(N-1)/2\), the exact local return
   probability of a uniform unit is
   \(\gcd(E,r-1)/(r-1)\), with the corresponding exact \(\{\pm1\}\)
   correction. On bounded-gap semiprimes these events remain exponentially
   sparse.

The exact witness

\[
1088340091=32987\cdot32993
\]

has the standard least squarefree auxiliary bank
\(\{2,3,7,23,67\}\), whose product exceeds \(\sqrt N\), but only the
vacuous row \(2\) accepts in the local orbit test. The remote discovery was
not preregistered; a post-hoc exact verifier reproduces this witness, so it
is a certificate only, not distributional evidence.

P196 leaves open an \(N\)-dependent adaptive bank with a proved drift law,
a compatible integer-derived source, joint processing of rejected rows,
and any mechanism that grows \(S\) or \(M\) with inverse-QP certified
progress.

The V2 statement, proof, hostile re-audit, and strict blind reconstruction
have SHA-256 hashes
`a5d38c57213a9c237723e2ea916ee2865f81cc8b086287728d493a07ebf2334c`,
`290af2762069471b625442a851fd56b9e65d2db8964ee50ae3ab4a3832ea0e5a`,
`563d7a5bf4be121244cfaa217f7833d17a7a602be8f21386afff7d5c9fb6378d`,
and
`2a56bd37bcc8ec5af83b3b295f72d2a4209b8ab75e8002162d600a7b5c1670be`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P195 — fixed-shift random AKS evaluations can remain exponentially sparse at the upper balance edge

**Status:** promoted from F225 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact obstruction for one scalar
Las Vegas source. It is not a lower bound against biased points, variable
shifts, coefficient vectors, or joint processing of nonzero values.

Let

\[
N=pq,\qquad p<q<2p,
\]

where (p,q) are distinct odd primes, and define

\[
d=q-p,\qquad c=2p-q=p-d.
\]

The integer (c) is odd. Assume (c\ge3), put

\[
k=c-2,\qquad s=(c+1)/2,
\]

and consider the fixed-shift scalar

\[
H_N(x)=(x+1)^N-x^N-1\pmod N.
\]

Modulo (p), the two exceptional points (0,-1) are roots, and every
other root is exactly a root of

\[
P_k(X)=X^k-(X+1)^k-[X(X+1)]^k.
\]

This polynomial has degree (2k), so the number (A_p) of local roots
satisfies

\[
A_p\le2c-2.
\]

Modulo (q), partition (x\notin\{0,-1\}) by the two quadratic-character
signs

\[
(\epsilon,\delta)=(\chi_q(x+1),\chi_q(x)).
\]

On a sign cell the root equation is exactly

\[
Q_{\epsilon,\delta}(X)
=\epsilon(X+1)^s-\delta X^s-1=0.
\]

The opposite-sign polynomials have degree (s), the equal-sign
polynomials have degree (s-1), and the cells are disjoint. Thus the number
(A_q) of local roots obeys

\[
A_q\le2c+2.
\]

CRT now gives exact XOR laws. For uniform (x\bmod N),

\[
\Pr(1<\gcd(H_N(x),N)<N)
={A_p\over p}\left(1-{A_q\over q}\right)
 +{A_q\over q}\left(1-{A_p\over p}\right).
\]

For a uniform unit (x\bmod N), the exact law is

\[
{A_p-1\over p-1}\left(1-{A_q-1\over q-1}\right)
+{A_q-1\over q-1}\left(1-{A_p-1\over p-1}\right),
\]

and hence is at most

\[
{4c-2\over p-1}.
\]

When obtaining the unit by screening a uniform residue, condition on
(gcd(x,N)=1), or reject (x=0) as well: the branch
(gcd(x,N)=N) is not a unit branch and yields no proper factor. This is the
minor qualification recorded by the hostile audit.

The Baker--Harman--Pintz short-interval theorem gives an unconditional
hostile family. For each sufficiently large odd prime (p), take a prime

\[
q\in[X_p-X_p^{0.525},X_p],
\qquad X_p=2p-\lfloor p^{3/5}\rfloor.
\]

Then

\[
c=\Theta(p^{3/5}),\qquad d=p-\Theta(p^{3/5})=\Theta(p),
\]

yet one fresh uniform unit evaluation succeeds with probability only

\[
O(c/p)=O(p^{-2/5})=2^{-\Omega(n)}.
\]

The same conditional bound holds for every reached transcript if the next
point is freshly uniform. A numerical-QP adaptive bank therefore has total
success probability (2^{-\Omega(n)}). Thus the large-gap regime left by
P194 does not become easy merely by fixing the shift and randomizing the
evaluation point.

P195 leaves open carry-biased or otherwise nonuniform points, variable
shifts, a point selected after seeing its own value, joint processing of
typical nonzero scalars, coefficient/rank data, and samplers that certify a
new contribution to the common modulus (M).

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`57a0764b549a79a5a725612b95a6f57b41791760bc6a1a2d188354041d6b1a20`,
`b6f9feb7d2dfe9cb9a0829e750defdd1a2a1025c7c42523671b4a6a6ea35c03a`,
`0d9f2d588cd5a1baea60217462051f89904b7e7a888ecf699070f23064f14831`,
and
`876de92d43d9da28dd856378b47e48c4f36a9bac5923eadf3c312ddb5d5a34e9`.
No mathematical computation, cross-family audit, human audit, or
publication-level literature review has run.

## P194 — the factor residue gives an AP--Fermat terminal, while uniform AP shifts add no earlier progress below the two-thirds gap

**Status:** promoted from F224 after a fresh hostile audit and a strict
statement-only reconstruction. This is a positive deterministic terminal
and a matching boundary for one Las Vegas sampling family. It does not
compute a new carry bit or enlarge the certified common modulus.

Let

\[
N=pq,\qquad p<q<2p,\qquad d=q-p,
\]

where (p,q) are distinct odd primes. Suppose a public certificate gives

\[
p\equiv s\pmod L,\qquad \gcd(L,N)=1.
\]

This includes the combined beta-two state
(L=\operatorname{lcm}(2^t,M)), where the carry supplies
(p\bmod 2^t) and every prime divisor of (N) is (1\bmod M).
Compute

\[
u\equiv Ns^{-1}\pmod L.
\]

Then (q\equiv u\pmod L), so the Fermat midpoint
(A_*=(p+q)/2) lies in one public residue class modulo
(L/\gcd(2,L)). Scanning only that class from (sqrt N) reaches (A_*)
in fewer than

\[
1+{d^2\over4pL}
\]

square tests. Hence

\[
{d^2\over pL}=\operatorname{QP}(n)
\]

is a deterministic numerical-QP terminal. It can apply before the
gap-independent GFHP threshold (N^{1/4}/L=\operatorname{QP}(n)).

There is also an exact matching sampling boundary for the P193 modified-AKS
channels. Put

\[
I_N=[\lceil\sqrt{N/2}\rceil,\lfloor\sqrt N\rfloor]\cap\mathbb Z,
\qquad
\mathcal C_{L,s}=\{x\in I_N:x\equiv s\pmod L\},
\]

and (H=|\mathcal C_{L,s}|). The only nonunit in (I_N) is the true
factor (p), and reduction of (I_N) is injective modulo each hidden
prime. For a fixed (r) with

\[
2\le r<d<p-1,\qquad \gcd(r,N)=1,
\]

scan every coefficient gcd and the complete resultant/local-nullity channel
of

\[
E_x(X)=(X+x)^N-X^N-x^N\pmod{X^r-1,N}.
\]

Among all off-target integers in the cell, at most

\[
rd(r+5)
\]

activate either channel. A distribution on the cell with largest atom
(eta) therefore succeeds with probability at most

\[
(1+rd(r+5))\eta;
\]

the initial (1) is the exact draw (x=p). Uniform sampling gives the
bound ((1+rd(r+5))/H), and the same statement holds conditionally when
each (r) and sampling law are fixed before its fresh draw.

Consequently, fix (epsilon>0) and assume

\[
d\le p^{2/3-\epsilon}.
\]

For any numerical-QP AP--Fermat cap and numerical-QP adaptive bank of
fresh uniform cell shifts and numerical-QP moduli fixed before those draws,
one of two things happens on every sufficiently large input: the
AP--Fermat scan factors (N), or the entire direct-candidate,
raw-coefficient, and resultant/local-nullity bank succeeds with probability
only (2^{-\Omega(n)}). Indeed, failure of the Fermat cap forces

\[
L=O\!\left({d^2\over p\operatorname{QP}(n)}\right),
\qquad H=\Theta(p/L),
\]

and the total sampling probability is bounded by a numerical-QP multiple of

\[
{dL\over p}\le {d^3\over p^2\operatorname{QP}(n)}
\le p^{-3\epsilon}\operatorname{QP}(n).
\]

Thus the integer AP is genuinely useful through Fermat geometry, but
uniformly sampling it does not create a missing Las Vegas source before
that terminal. The result leaves open nonuniform laws with a proved useful
heavy atom, joint processing of typical nonzero coefficient vectors,
choosing (r) after seeing the same shift, gaps
(d\ge p^{2/3-o(1)}), and samplers that enlarge (M) or reveal the next
dyadic factor bit.

The exact certificate (N=187=11\cdot17), (L=2), (s=1), (r=2)
shows that the factor cell ({11,13}) can contain no useful off-target
modified-AKS shift. The approved preregistered D02 remote run completed 480
finite rows and is guidance only; D01's pre-Python wrapper failure is
preserved and contributes no evidence.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`cd9ac0c208c7d62a1c486fd94f63cdd6851dd924a85bf4fa42527f0c36b9f745`,
`b3297337dc856e5e2cf1af0697ab3047bdffc6943542b599c13d3abe4e7e39a2`,
`cad68a6138aac3826f45cf6bce07b1d8ed229653e111f9154d47495476fd6f9a`,
and
`646baa8f662d2112b4c20bbb0d5bc91c28fc1c4cad3ba3858317b20935f54f7c`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P193 — uniform modified-AKS shifts are exponentially sparse on an intermediate-gap family

**Status:** promoted from F222 V2 after a fresh hostile audit and a strict
statement-only reconstruction. This is a theorem about one randomized,
integer-specific AKS source. It is not a factoring algorithm and is not a
lower bound against biased or carry-correlated shifts.

Let

\[
N=pq,\qquad p<q<2p,\qquad d=q-p,
\]

where (p,q) are distinct odd primes. For an integer (r\ge2), coprime to
(N), and a unit shift (a\bmod N), put

\[
E_a(X)=(X+a)^N-X^N-a^N
       \pmod{X^r-1,N}.
\]

Assume (r<d<p-1). For every cyclic coefficient position, the reduction
modulo (p) is a nonzero polynomial in (a) of degree at most (d). On
the (q)-side, clearing the Frobenius-induced negative exponent produces a
nonzero polynomial of degree at most (d(r+1)-1), outside at most (r)
common exceptional shifts. Consequently, for a fresh uniform unit shift,

\[
\Pr\bigl(\exists k:1<\gcd([X^k]E_a,N)<N\bigr)
\le {rd\over p-1}+{rd(r+1)\over q-1}.
\]

This bounds the complete raw coefficient scan, not one selected
coefficient. If

\[
\nu_\ell(a,r)=\deg\gcd(E_a\bmod\ell,X^r-1),
\]

then the exact Frobenius formulas also give

\[
\Pr(\nu_p>0\text{ or }\nu_q>0)
\le {rd\over p-1}+{2rd\over q-1}.
\]

A proper resultant gcd is contained in this event. Therefore the union of
the raw-coefficient and resultant/nullity channels has probability at most

\[
{2rd\over p-1}+{rd(r+3)\over q-1}.
\]

The Baker--Harman--Pintz short-interval theorem supplies an infinite
balanced family with

\[
d=\Theta(p^{3/5}).
\]

On this family, allow an adaptive numerical-QP bank. Before trial (i), it
may choose a numerical-QP (r_i), coprime to (N), from the entire previous
public transcript; it must then use a fresh conditionally uniform unit shift
(a_i). The conditional union bound is

\[
d\sum_i\left({2r_i\over p-1}
       +{r_i(r_i+3)\over q-1}\right)=2^{-\Omega(n)},
\]

where (n) is the bit length of (N). Thus Las Vegas resampling of uniform
modified-AKS shifts does not provide inverse-QP progress on all inputs, even
when every coefficient and the full resultant/nullity event are inspected.

P193 leaves open nonuniform or carry-correlated shifts, a modulus chosen
after seeing the same shift, fixed shifts with random evaluation points,
joint processing of typical nonzero coefficients, multi-shift elimination,
and implicit moduli larger than numerical QP. The preregistered F222-D01
remote run completed 913 exact small rows and is finite guidance only; its
positive small-gap observations do not enter the theorem.

The V2 statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`586d2edd549a8c580aa9d66c9dd2cee7866ee4f0d74ed0956bc3f07772ad6cd9`,
`e098bb138dd033537436cdc64ed8a46e67b80ba4ae1e0c489c48a8d0c71ff4c1`,
`83f0dd1a7d20610cbe8bd6f790a80a312397d1d6d2db22be8c71fa8e4416e72b`,
and
`598934a635f67f25e5d47a8acdccf1aaa30e8dbc4a5d81f48d9ff9ba0f29a13f`.
No cross-family audit, human audit, or publication-level literature review
has run.

## P192 — moving-weight and eta fast-forward reduce to the same affine divisor coefficient

**Status:** promoted from F218 after a fresh hostile audit and a strict
statement-only reconstruction. This is a collection of exact congruences and
named-model boundaries. It does not evaluate the remaining coefficient and
is not a factoring algorithm.

Retain the balanced beta-two setup

\[
N=pq,\qquad p<q<2p,\qquad N\equiv3\pmod4,
\qquad K=(N-1)/2,
\]

with \(K\) completely factored. If \(\Lambda\) is any positive multiple of
\(\lambda(K)\), \(k=\Lambda+2\), and \(\ell^e\parallel K\), then for every
positive \(m\),

\[
\boxed{
\sigma_{k-1}(m)
\equiv\sigma_1\!\left(m/\ell^{v_\ell(m)}\right)
\pmod{\ell^e}.}
\]

These are exactly the positive coefficients of the fixed-weight depleted
Eisenstein form

\[
\frac{\ell E_2(\ell\tau)-E_2(\tau)}{24}.
\]

At \(m=N\), no depletion occurs, so CRT gives

\[
\sigma_{k-1}(N)\equiv\sigma_1(N)\pmod K.
\]

Thus binary moving weight changes the packaging but not the P191 target.
For prime \(K=r\), the eta quotient \(F_r=P(q)^r/P(q^r)\) obeys the
stronger all-index formula

\[
-\frac{[q^m]F_r}{r}
\equiv u^{-1}\sigma_1(u)\pmod r,
\qquad m=r^v u,\quad(r,u)=1.
\]

At \(m=N=2r+1\), this again equals \(\sigma_1(N)\bmod r\).

Three proposed fast-forward mechanisms have exact boundaries.

1. In a big-Witt ghost circuit using only ring operations and
   \(F_d,V_d\) supported on primes dividing \(K\), every dependency path
   preserves the \(K\)-rough part of its index. Since \((N,K)=1\), no seed
   coordinate below \(N\) can reach the affine target \(N=2K+1\).
2. Frobenius compresses the full theta coefficient

   \[
   \vartheta^{2r+2}\equiv\vartheta(q^r)^2\vartheta(q)^2\pmod r,
   \]

   but not its factor-sensitive Eisenstein projection. At
   \(r=17,N=35\), the compressed full coefficient is \(15\bmod17\), the
   Eisenstein target is \(10\bmod17\), and the cusp contribution is the
   nonzero residue \(5\).
3. For every prime \(r\) and every positive integer \(s\), the affine
   section

   \[
   j\longmapsto\sigma_s(rj+1)\pmod r
   \]

   is not eventually periodic. Hence it has no finite-order
   constant-coefficient homogeneous or affine linear recurrence and its
   generating series is not rational over \(\mathbb F_r\). The proof uses
   prime powers \(\ell^a\) with \(\ell\equiv1\pmod{rT}\) to contradict any
   proposed period \(T\).

P192 leaves open nonlinear or QP-growing Cartier state, additive index
mixing, a computable cusp projector, a randomized exact coefficient
observable, and any new integer-specific statistic. The preserved remote
run failed before Python started because its frozen command required an
absent `/usr/bin/time`; it was not rerun and supplies no empirical claim.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`458924ffa7bf4554fd697e36bd45acf29930e414a0dd09bab10a7e388a95a481`,
`cfd2319a72f087c2b1c63f64c5dfbba68e16bbe6da0950019af3f1874d712ea3`,
`988721f326a08d5a5f8bb2c12a64127dfb9281f34650172bd8bb2b03c57e362a`,
and
`a2f5291d650a99a2ef0df6d5dc6b3b2824b6adadc82fc82eed666f1210f4d1e6`.
No successful computation, cross-family audit, human audit, or
publication-level literature review has run.

## P191 — moving-level traces compress the beta-two target to one divisor-sum residue

**Status:** promoted from F217 after a fresh hostile audit and a strict
statement-only reconstruction. This identifies equivalent compressed targets
and conditional decoders. It does not construct the missing coefficient
evaluator and is not a factoring algorithm.

Assume

\[
N=pq,\qquad p<q<2p,\qquad N\equiv3\pmod4,
\qquad K=\frac{N-1}{2},
\]

with the complete factorization of \(K\) granted. In the group algebra of
\(G=(\mathbb Z/K\mathbb Z)^\times\), the divisor element is

\[
\mathcal A_N=2[1]+[p]+[p^{-1}].
\]

The tautological ring map \([a]\mapsto a\pmod K\) gives

\[
\Theta_K(\mathcal A_N)
=\sigma_1(N)
\equiv2+p+q\pmod K.
\]

Except for the trial-divisible input \(N=15\), one has \(p+q<K\).
Therefore this single \(O(n)\)-bit residue recovers the exact sum \(p+q\),
and the roots of \(X^2-(p+q)X+N\) factor \(N\).

There are three exact realizations of the same target.

1. Given a separately certified cyclic decomposition of \(G\), QP forward
   and inverse coordinate maps, succinct coordinate characters, and a QP
   evaluator for

   \[
   D_N(\chi)=\sum_{d\mid N}\chi(d)
   \]

   to absolute error \(2^{-4n-20}\), at most \(2r-1\le2n-1\) scalar
   traces recover \(p\) up to inversion. Coordinate cosines recover the
   individual signs, and anchor cross-characters align them. Factoring
   \(K\) alone does not supply any of these extra premises.
2. With \(k=\varphi(K)+2\), Euler's theorem gives

   \[
   \sigma_{k-1}(N)\equiv\sigma_1(N)\pmod K.
   \]

   Thus one binary-weight, level-one Eisenstein coefficient modulo \(K\)
   factors \(N\). Standard dense state is exponential in the numeric weight
   and the exact coefficient has exponentially many bits; a modular-residue
   random-access evaluator remains open.
3. If \(K=r\) is prime, the holomorphic eta quotient

   \[
   F_r(q)=\frac{P(q)^r}{P(q^r)}
   \]

   satisfies, for \(r\nmid m\),

   \[
   -\frac{[q^m]F_r}{r}\equiv m^{-1}\sigma_1(m)\pmod r.
   \]

   At \(m=N=2r+1\), this is the same factor-revealing residue. Its exact
   logarithmic derivative is the original Lambert divisor series, so the
   eta quotient packages rather than evaluates the hard coefficient.

A twisted Ramanujan expansion supplies a matching integer-specific
boundary: after subtracting the public \(n=1\) baseline, every explicit
multiplier \(m<p\) is identically insensitive to the factorization and
\(m=p\) is the first nonzero term. Standard termwise evaluation therefore
touches the hidden factor before it sees useful information.

Direct Hecke representatives, moving-level Manin symbols, moving-weight
symmetric powers, and termwise Ramanujan sums are exponential only in their
named explicit models. P191 leaves open a randomized or deterministic
compressed coefficient evaluator, trace formula, nonholomorphic method,
nonabelian extension, nonlinear integer selector, and any implicit
Archimedean decoder. The one-child recursion correction remains in force:
factoring \(K\) is not rejected merely because it loses only one bit.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`f6bada7e65dc7c6617760cb1ce1e7b87618953cea6f46d11dc0d1fd8416e384d`,
`16946a7a8d2c6adc869524b9e27d15b2317bfb4336688a5bc5e960dafce82e5a`,
`603844aaa0be4d3c91baad4397654a90f589f47b8464a46904fc74b9cf3d36c0`,
and
`fdba3d32ae877840ce86f0b0ba49b0a91fe83c354eaafe2b417dae98670d150d`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P190 — dyadic trace lifting retains constant-density ambiguity

**Status:** promoted from F216 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact named-model boundary for
the orientation-free dyadic trace projection. It is not a factoring
algorithm or a lower bound against an implicit decoder that retains the
inverse parameter. The finite remote check is not used as proof evidence;
its preregistration timing has only mutable-filesystem provenance.

For every odd integer \(N\) and \(t\ge5\), put

\[
W_t(N)=\{u+Nu^{-1}\pmod{2^t}:u\in U(2^t)\}.
\]

If \(N=pq\), then the factor trace \(p+q\bmod2^t\) lies in \(W_t(N)\)
by taking \(u=p\). Let \(d\in\{1,3,5,7\}\) be \(N\bmod8\). A public odd
\(a\) satisfies

\[
N\equiv da^2\pmod{2^t},
\]

and multiplication by \(a\) gives

\[
\boxed{W_t(N)=aW_t(d).}
\]

The three nontrivial normalized images are exactly

\[
W_t(3)=\{s:s\equiv4\pmod8\},
\]

\[
W_t(7)=\{s:s\equiv0\pmod8\},
\]

and

\[
W_t(5)=\{s:s\equiv6\text{ or }26\pmod{32}\}.
\]

Thus their sizes are \(2^{t-3},2^{t-3},2^{t-4}\), respectively. For
\(d=1\), the image splits into the positive and negative valuation strata
of

\[
u+u^{-1}-2=(u-1)^2/u.
\]

Its exact size is

\[
|W_t(1)|=
\begin{cases}
(2^{t-4}+8)/3,&t\text{ even},\\
(2^{t-4}+10)/3,&t\text{ odd}.
\end{cases}
\]

Consequently, uniformly for all odd \(N\),

\[
\boxed{|W_t(N)|\ge 2^t/48.}
\]

At the P175 partial-factor threshold

\[
t=n/4-\operatorname{polylog}(n),
\]

a literal trace-residue list therefore still has \(2^{\Omega(n)}\)
entries. Increasing dyadic precision does not provide one independent trace
bit per lift: after public scaling, the classes \(3,7\) retain one fixed
modulo-eight condition, class \(5\) retains two modulo-32 conditions, and
class \(1\) retains \(O(t)\) valuation strata of asymptotic density \(1/48\).

This theorem closes only the proposed bridge that discards \(u\), keeps the
single trace \(u+Nu^{-1}\), and explicitly materializes its dyadic image.
It leaves open an implicit short-interval finder, a method retaining \(u\)
or reciprocal-prefix orientation, nonlinear integer statistics, mixed odd
moduli, and direct Archimedean selection.

The statement, proof, hostile audit, and strict blind reconstruction have
SHA-256 hashes
`fdc4a78e1189b4e733edf5a8d07549c459c3dbabf096ecf445a94acdc0f1df59`,
`aeefbbd1a6425383ffb9f924628e0c1bed15dbcf571596bb1052b91ad8de7592`,
`b936aa92b4ffdffad040e043fb4835a2b47b0e3386cd8ce60f3ef9c971866c9b`,
and
`85a3fc1c95e66e646dcf64d53f071396a0591640e5dc60610de4b01a9c07ae3d`.

## P189 — the full inverse box is exactly the factor pair, while explicit representations remain exponential

**Status:** promoted from F214 V2 after a fresh hostile re-audit and a
strict statement-only reconstruction. This is an exact balanced-semiprime
equivalence and a collection of named explicit-method boundaries. It is not
an inverse-box algorithm, a general lower bound, or an all-input factoring
algorithm.

Let

\[
N=pq,\qquad p<q<2p,\qquad K=(N-1)/2,
\]

with distinct odd primes. If integers satisfy

\[
\sqrt{N/2}<X<\sqrt N<Y<\sqrt{2N},
\qquad XY\equiv N\pmod K,
\]

then the strict product window gives \(|XY-N|<K\). Hence \(XY=N\), and
the interval ordering forces

\[
\boxed{(X,Y)=(p,q).}
\]

Thus the full-modulus inverse-box point is the factor pair itself. More
generally, for \(m\mid K\), if \(\operatorname{lcm}(2,m)\) exceeds both
odd-interval diameters, every nonempty residue progression is a singleton
and the endpoint-live predicate again forces \(XY=N\). This does not locate
the live residue before that threshold.

The literal balanced scans have \(\Theta(\sqrt N)\) points. The full unit
torsor has exactly \(\varphi(K)\) points, with

\[
\varphi(K)\ge \sqrt{K/2}=\tfrac12\sqrt{N-1}.
\]

An explicit paired-CRT meet in the middle has a list of size at least
\(\sqrt{\varphi(K)}\). For

\[
\psi_K(u)=u+u^{-1},
\]

every fiber satisfies

\[
|\psi_K^{-1}(s)|
\le 4\,2^{\omega(K_{\rm odd})}\sqrt K.
\]

Consequently the image has size \(K^{1/2-o(1)}\), and an explicit
CRT-MCSS half-list has size \(K^{1/4-o(1)}\). These are materialization
bounds only; implicit and adaptive representations remain open.

The determinant identity \(XY-2K=1\) is exactly divisor selection and
supplies no separate public continued-fraction approximation. In coordinates
\(a=B-X,c=Y-B\), with \(B=\lfloor\sqrt N\rfloor\), the root equation

\[
Bc-Ba-ac-(N-B^2)=0
\]

has box product \(AC=\Theta(N)\) and scaled height \(W=\Theta(N)\), outside
the published direct bivariate Coppersmith sufficient range
\(AC<W^{2/3}\). This is theorem-range nonapplicability, not a lattice lower
bound. When \(K\) is odd, an odd interval of length \(L<K\) has exact
Fourier support

\[
K-\gcd(K,L)+1,
\]

so termwise Fourier or Kloosterman materialization is also exponential.
Compressed exact summation remains open.

The recursion scope is essential. At a balanced node, \(K\) has at most
\(n-1\) bits and \(E=N-\lfloor\sqrt N\rfloor^2\) has at most
\(n/2+O(1)\) bits, but \(K\) need not satisfy the balanced-semiprime
promise. Only inside an independently correct all-input dispatch may one
invoke P183's recurrence

\[
T(n)\le T(n-1)+Q(n)T(n/2+O(1))+Q(n).
\]

The balanced inverse-box selector alone does not prove recursive closure.

The V2 statement, proof, hostile re-audit, and strict blind reconstruction
have SHA-256 hashes
`3aa3260154c8f0f7848b5fd5f8f427de41be07c986c044ad3141e32bc1928e97`,
`a7209b215d5d5b5d3c72e73a577a50a541b413dc3ed3e31a4772235dbe5d97b3`,
`4355367e5865532114322aec1a99ecf897a67197a8ad1d01dff8eebc79aee93b`,
and
`53467aa3fc1395caf0299510bece0c31c0fcd6324ceb707d792bd21f86e9c2b7`.

## P188 — polynomial near-square norm banks can have only global parity roots

**Status:** promoted from F213 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact obstruction to the ordinary
rational-prime parity decoder for the displayed norm bank. It is not a
factoring algorithm or a lower bound against nonlinear postprocessing.

For every (M\ge2), there is an even (s>M) such that

\[
N=s^2+1
\]

is odd and composite, and there are distinct primes
(\ell_1,\ldots,\ell_M), with the following exact behavior. For
(1\le a\le M), put

\[
r_a=\lfloor a\sqrt N\rfloor,
\qquad E_a=a^2N-r_a^2,
\qquad F_a=(r_a+1)^2-a^2N.
\]

Then the no-carry identity is

\[
\boxed{r_a=as,\qquad E_a=a^2,
\qquad F_a=2as+1-a^2,}
\]

with (0<E_a,F_a<N). Every displayed base and norm is coprime to (N).
The construction forces

\[
v_{\ell_a}(F_a)=1,
\qquad
\ell_a\nmid E_bF_b\quad(b\ne a),
\qquad
\ell_a\nmid E_a.
\]

Thus each adjacent-norm column has a private valuation-one pivot row.

In the signed rational-prime parity matrix with columns

\[
(-E_1),F_1,\ldots,(-E_M),F_M,
\]

the exact kernel is

\[
\boxed{
\{(x_1,0,\ldots,x_M,0):
x_1+\cdots+x_M=0\text{ in }\mathbb F_2\}.}
\]

Every dependency therefore excludes every (F_a) and uses an even subset
(S) of the square columns. With

\[
X=\prod_{a\in S}r_a,
\qquad Y=\prod_{a\in S}a,
\qquad k=|S|,
\]

one has

\[
XY^{-1}\equiv s^k=(-1)^{k/2}\in\{1,-1\}\pmod N.
\]

Hence both standard gcds are trivial/full. A sign-free odd subset produces
only the already public root (\pm s) of (-1), whose two gcds are also
trivial.

The construction uses only CRT and Bertrand's postulate and can be chosen
with input length (n=\lceil\log_2(N+1)\rceil) satisfying

\[
\Omega(M^2)\le n\le O(M^2\log(M+1)),
\qquad M=n^{1/2+o(1)}.
\]

The (E_a) have (O(\log M)) bits and the (F_a) have
((1/2+o(1))n) bits. A public prefix
(a\le\lfloor n^{1/3}\rfloor) inherits the same private rows and global
root image. Therefore recursively factoring every child is compatible with
P183's QP fixed-ratio side-call accounting; contraction is not the failure.
Even after all factorizations are granted, ordinary parity closure need not
produce a non-global root.

The theorem does not cover all (N), semiprimes, larger banks, or adaptive,
nonlinear, and Archimedean use of the factored norms. The statement, proof,
hostile audit, and strict blind reconstruction have SHA-256 hashes
`9e74427637283e893c5a91bc5d0d24d7a4040526dbe5cf2e1599971474081fff`,
`ac83b7fa190b16226b69d7f2604fe6a0aa684e8594251dbe702aa5f780a43b35`,
`269d4d0aa2718cb139da02e09deb4b502da0517381bacf42243a39ea868f6c5d`,
and
`22fc9d7ffd7597d1d91c2659d94012850afbbce12997e9f8a9438fcc292b0019`.

## P187 — scalar abelian reciprocity preserves the beta-two inversion torsor

**Status:** promoted from F215 after a fresh hostile audit and a strict
statement-only reconstruction. This is an exact information boundary for
the declared scalar abelian frameworks and an exact extraction theorem for
a coherent non-diagonal lift. It is not a factoring algorithm.

Let

\[
N=pq,\qquad p<q<2p,\qquad N\equiv3\pmod4,
\qquad K=(N-1)/2,
\]

and grant the complete factorization of (K). For every (d\mid K), the
factors are units modulo (d) and

\[
\boxed{q\equiv p^{-1}\pmod d}.
\]

Consequently, in (\mathbb Q(\zeta_d)),

\[
\operatorname{Frob}_q=\operatorname{Frob}_p^{-1}.
\]

Their decomposition subgroups and residue degrees are equal. Every
one-dimensional Artin or ray character therefore sees the pair
((z,z^{-1})), while the computable composite-ideal value is only the
public product one. Genus characters take equal values on the two factors.
With an additional public conductor part, the exact involution is the
affine inversion (z\mapsto\chi(N)z^{-1}), which still supplies no label.
Likewise, bimultiplicativity gives

\[
(p,a)_{m,v}(q,a)_{m,v}=(N,a)_{m,v}.
\]

For a prime (r\mid K) with (r\nmid m), Hensel lifting makes (N) an
(m)-th power in (\mathbb Q_r), so every such Hilbert symbol with (N)
in one slot is trivial. Adaptive scalar transcripts built only from these
products remain invariant and, on a (K)-supported conductor, eliminate no
candidate ((u,u^{-1})).

The fixed input

\[
N=527=17\cdot31,\qquad K=263
\]

certifies the small-order boundary. Since
((\mathbb Z/263\mathbb Z)^\times\cong C_{262}) and both 17 and 31 are
squares modulo 263, all rational cubic characters are trivial and all
quartic, octic, and genus characters take value one on both factors. The
rational cubic, quartic, and octic residue symbols at every prime above 263
are also trivial. Moreover, every unit returning under exponent (N-1)
has local orders at most (gcd(16,30)=2); mixed signs factor, while equal
signs yield only common order one or two.

There is an exact positive boundary. Let
(A_m=\mathbb Z[\zeta_m]), with (gcd(m,N)=1), and suppose an explicit
(Y\in A_m/NA_m) satisfies, in the complete rational components,

\[
Y\equiv\zeta_m^a\pmod{pA_m},\qquad
Y\equiv\zeta_m^b\pmod{qA_m},\qquad a\ne b\pmod m.
\]

For each (e<m), take the gcd of (N) with every power-basis coefficient
of (Y-\zeta_m^e). At (e=a) this gcd is (p), and at (e=b) it is
(q): distinct (m)-th roots differ by a unit in every finite-field
factor because (m) is coprime to (N). Thus a numerical-QP-degree
coherent non-diagonal lift is already a deterministic factor transition.
A value at only one selected prime ideal needs a separate all-conjugates
no-collision theorem.

Finally, the additive character traces

\[
t_\chi(u)=\chi(u)+\chi(u)^{-1}
\]

separate inversion orbits by Fourier inversion, but the required value at
the hidden factor is exactly

\[
\sum_{c\mid N}\chi(c)=2+\chi(p)+\chi(p)^{-1}.
\]

Ordinary reciprocity evaluates the product, not this divisor coefficient.
The remaining route is therefore a QP evaluator/decoder for an additive
trace bank, a coherent non-diagonal ring-valued carrier, or a genuinely
nonabelian or Archimedean selector. The statement, proof, hostile audit,
and strict blind reconstruction have SHA-256 hashes
`ef9c59a2cda7eb7a1341d7242aa432dd50a67ba5a85fe797b0343ade470c743e`,
`e6c7d1cf668baac847bf98f14dc3eb1d9a9091bc93316f9892a9ace788e33b62`,
`424cf867cb2a12f14aefb2221275240facd37bcc3228d69d1c8b9e51f1bdecb8`,
and
`10cea4bc56f6b03b11acdd70e248df3e4e3436bcd75a1e8e38051ee152d7297d`.

## P186 — the interval frontier changes at square-root scale, and a large-modulus QP residue list is terminal

**Status:** promoted from F212 V2 after a fresh hostile audit and a strict
statement-only reconstruction. This is a phase theorem and a conditional
postprocessor on balanced distinct odd semiprimes. It does not construct the
required residue list or factor all inputs.

Let

\[
N=pq,\qquad p<q<2p,
\]

and use the exact balanced odd intervals

\[
P=[L,B],\qquad Q=[B+1,U],
\]

where \(B=\lfloor\sqrt N\rfloor\),
\(L=\lfloor\sqrt{\lfloor N/2\rfloor}\rfloor+1\), and
\(U=\lfloor\sqrt{2N-1}\rfloor\). For \(m\ge2\), coprime to \(N\), put
\(s=\operatorname{lcm}(2,m)\). The F209 relaxed frontier consists of unit
residues \(x\bmod m\) for which the two associated odd progressions in
\(P,Q\) are nonempty and their endpoint products straddle \(N\).

If \(N\ge1024\) and

\[
s\le\frac{\sqrt N}{8},
\]

then the frontier is exactly the full unit group:

\[
\boxed{\mathcal F_N(m)=U(m)}.
\]

Thus every modulus \(m=o(\sqrt N)\) eventually provides no geometric
pruning. Conversely, if \(s\) exceeds both interval widths, every
progression is a singleton and the frontier is the exact divisor event.
The unresolved phase is \(m=\Theta(\sqrt N)\).

At the recursively factored modulus

\[
K=(N-1)/2,
\]

the collapse is exact. For \(X\in P,Y\in Q\),

\[
XY\equiv N\pmod K\iff XY=N.
\]

Hence

\[
|\mathcal F_N(K)|=
\sum_{X=L}^{B}
\left(
\left\lfloor\frac NX\right\rfloor-
\left\lfloor\frac{N-1}{X}\right\rfloor
\right)=1,
\]

and the unique witness is \(p\). Literal equal-quotient grouping has
\(\Theta(\sqrt N)\) blocks on this shell; this is only a named-method
boundary.

There is a precise positive terminal. Fix \(\varepsilon>0\). Given an
explicit numerical-QP-size list of pairs \((m_j,r_j)\), each with

\[
N^{1/4+\varepsilon}\le m_j\le N^C,
\qquad \gcd(m_j,N)=1,
\]

if one residue is \(p\) or \(q\) modulo its listed modulus, a deterministic
numerical-QP postprocessor factors \(N\) by the standard univariate
unknown-divisor Coppersmith theorem. It need not know which entry is correct.
This becomes an end-to-end QP algorithm only when a public numerical-QP
generator constructs the list; a mere bound on list size does not bound its
construction time.

The exact remaining gate is a QP list generator above the quarter-power
threshold, an implicit finder or isolating counter in the square-root phase,
or another integer-specific statistic bypassing the frontier. The statement,
proof, hostile audit, and strict blind reconstruction have SHA-256 hashes
`69e0ca4f9cefb0ed41cbeaff25aa48b184d4039dffce11257baf787d8866dd99`,
`7cb6eb791cb05e2bb9139730bd188ca9566f890c7ce28d1f21f28e8c041708dc`,
`8b29b445c2738594d94e3e5e303a61322126e8b87a0cfcd19a15729730195d7e`,
and
`3cc3b2dd947dee4cb8c4fffc192e955a637392be205eec8326a99da9c1dce4f0`.

## P185 — dyadic quotient siblings are half-translated and differ only at the balanced integer point

**Status:** promoted from F210 V2 after a fresh hostile re-audit and a strict
statement-only reconstruction. This is a conditional boundary theorem for
balanced distinct odd semiprimes. It is not a child selector or a factoring
algorithm.

Let

\[
N=pq,\qquad p<q<2p,
\]

and grant a correct reciprocal prefix modulo \(m=2^t\), with \(t\ge1\) and
\(2m<p\). Write

\[
r\equiv p\pmod m,\qquad c\equiv q\pmod m,
\qquad K=(N-rc)/m,\qquad \delta=K\bmod2.
\]

The two legal next-bit lifts are

\[
r_a=r+am,\qquad c_a=c+(a\mathbin{\mathsf{xor}}\delta)m,
\qquad K_a={N-r_ac_a\over2m},\qquad a\in\{0,1\}.
\]

They are positive units modulo \(N\), and their exact difference is

\[
K_0-K_1=
\begin{cases}
(r+c+m)/2,&\delta=0,\\
(c-r)/2,&\delta=1.
\end{cases}
\]

Hence they coalesce exactly when \(\delta=1\) and \(r=c\). Outside
coalescence, all common prime-power support lies in this public difference:

\[
\gcd(K_0,K_1)=\gcd(K_0,|K_0-K_1|).
\]

Put \(h=2m\), \(\sigma=(-1)^\delta\), and

\[
F_a(P,Q)=hPQ+c_aP+r_aQ-K_a.
\]

Then the sibling curves satisfy the exact identity

\[
\boxed{F_1(P-1/2,Q-\sigma/2)=F_0(P,Q)}
\]

over \(\mathbb Z[1/2]\). In physical coordinates

\[
X=hP+r_a,\qquad Y=hQ+c_a,
\]

both charts are simply \(XY=N\). Thus every odd-local invariant preserved by
affine coordinate change agrees. Finite \(2\)-adic lift counts agree as well:
for every \(s\ge t+1\), each chart has exactly \(2^{s-t-1}\) solutions modulo
\(2^s\). The surviving distinction is integer and Archimedean: the true
chart has the nontrivial balanced point

\[
1<X<\sqrt N<Y<N,
\]

namely \((p,q)\). Trivial points such as \((1,N)\) do not orient the chart.

Complete factorizations of both children do have one conditional positive
use. Define \(H_a=hK_a\), \(G=\gcd(H_0,H_1)\), and test a public unit \(w\).
If both \(w^{H_a}=1\pmod N\), factor-first stripping of the known
factorization of \(G\) either factors \(N\) or returns a fully known exact
common local order \(e\mid G\). P172 then terminates whenever
\(N^{1/4}/e\) is numerical QP. None of the simultaneous return, large-order,
or asymmetric-gcd events is guaranteed.

The recursion accounting respects the one-child correction. At stages
\(t\ge\eta n-O(1)\), both children have at most
\((1-\eta)n+O(1)\) bits, so a numerical-QP bank of sibling calls can sit
beside one \((n-1)\)-bit spine under P183. At early stages \(t=o(n)\), two
independent near-size children are not covered; a single decrement chain
would still be QP if a selector constructed it.

The remaining gate is therefore a raw asymmetric factor-support/action
statistic, an adaptive order witness, or an implicit test for the balanced
integer point. The statement, proof, hostile re-audit, and strict blind
reconstruction have SHA-256 hashes
`d71fadf26f194f067647d7cee3ac8bcdfbc2d84c1d518d356f0df0c1e1268fa0`,
`b53f7fd20fc71f3495dc04893d3ab7101db710256b751ac9948c40299faca0f9`,
`cee5aa603125a96b49399eb0a06a0a06d4cb385eb3196e652252702fe5f44fb1`,
and
`bdd79a25a06bce3d3a4376216e7314a6a6c244627c4e4b5dbaa6778cbd015367`.

## P184 — named integer transforms relocate the beta-two selector but do not evaluate it

**Status:** promoted from F208 after a fresh hostile audit and a strict
statement-only reconstruction. This is a named-model boundary on balanced
distinct odd semiprimes. It is not a coefficient evaluator or a factoring
algorithm.

Let

\[
N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor,
\]

put \(\chi=\chi_4\), \(\eta=\chi(N)\), and define

\[
J_d(N)=\left\lfloor\frac Nd\right\rfloor-
       \left\lfloor\frac{N-1}{d}\right\rfloor
       =\mathbf 1_{d\mid N}.
\]

For

\[
A(N)=\sum_{d\mid N}d\chi(d),
\]

reciprocal divisor pairing gives

\[
A(N)=\sum_{d\le B}\chi(d)
\left(d+\eta\left\lfloor\frac Nd\right\rfloor\right)J_d(N).
\]

Only \(d=1,p\) survive, so

\[
T=A(N)-(1+\eta N)=\chi(p)(p+\eta q),
\qquad \operatorname{sgn}T=\chi(q).
\]

In particular, the exact orientation bit is the signed divisor-event OR

\[
\chi(p)=\sum_{2\le d\le B}\chi(d)J_d(N).
\]

Totalized floor reciprocity makes the hidden correction explicit. For odd
\(d\),

\[
\Delta_N(d)=
\sum_{i=1}^{(N-1)/2}\left\lfloor\frac{id}{N}\right\rfloor+
\sum_{j=1}^{(d-1)/2}\left\lfloor\frac{jN}{d}\right\rfloor-
\frac{(d-1)(N-1)}4
=\frac{\gcd(d,N)-1}{2}.
\]

Balance implies \(B/2<p\le B<2p\), hence \(p\) is the unique gcd spike
in that interval and

\[
2\sum_{\substack{B/2<d\le B\\d\text{ odd}}}
\chi(d)\Delta_N(d)=\chi(p)(p-1).
\]

The standard integer transforms do not compress this spike. Dedekind
reciprocity satisfies \(s(h,k)=s(h/g,k/g)\), where
\(g=\gcd(h,k)\), and the cotangent form acquires exactly \(g-1\) poles;
it exposes the gcd before contracting. The triangular HNF determinant shell
is the same divisor jump. The nonprincipal diagonal reduced form
\([p,0,q]\) already contains the factor. Pair-symmetric twisted weights
cancel on the hard \(\eta=-1\) branch, while exact magnitude extraction is
the ordinary difference-of-squares witness.

The surviving target is a nonlinear or adaptive compressed evaluation of
the signed divisor OR. The theorem does not rule out such an evaluator,
an asymmetric representation statistic, implicit class-group navigation,
or a support-preserving smaller child. The statement, proof, hostile audit,
and blind reconstruction have SHA-256 hashes
`e036b99dd345aacad134e716929e410a3ed083d601d7a5d50cf013957522f330`,
`a19f04c5c705f22bcf37d8b2a1eeac9bae3da5880121e7a986e133ec9f2c2bc9`,
`6385b8d8439e783f1607294ec51ff775d540a9f1223d5d867615f31220687d11`,
and
`718c5861f61eab13b81f1caf9015850952cb0a630bf378184b91aa234a0ea68b`.

## P183 — one near-size recursion spine is QP, while the two factored children leave an inversion torsor

**Status:** promoted from F207 after a fresh hostile audit and a strict
statement-only reconstruction. This is a recursion theorem and a boundary
for the declared joint congruence information. It is not an all-input
factoring algorithm.

Let \(Q\) be numerical QP and fix \(0<\rho<1\). If

\[
T(n)\le T(n-1)+Q(n)T(r(n))+Q(n),
\qquad r(n)\le\rho n+O(1),
\]

then

\[
\boxed{T(n)\le 2^{O((\log n)^{k+1})}}
\]

whenever \(Q(n)\le2^{O((\log n)^k)}\). The proof telescopes the unique
decrement spine, then iterates only \(O(\log n)\) fixed-ratio scales. A
fixed or QP-weighted number of fixed-ratio side calls is absorbed in
\(Q\). Thus weak one-bit contraction is not the obstruction. The theorem
does not cover two independent \(n-O(1)\)-bit children on an unbalanced
branch.

For the balanced semiprime geometry, define

\[
K=(N-1)/2,\qquad B=\lfloor\sqrt N\rfloor,
\qquad E=N-B^2,qquad M=\operatorname{lcm}(K,E).
\]

After the direct \(\gcd(E,N)\) exit, complete factorizations of \(K\) and
\(E\) construct in polynomial time a public \(R\bmod M\) satisfying

\[
R^2\equiv N\pmod M.
\]

Every product-consistent ordered unit pair has the unique form

\[
\boxed{(x,y)=(Ru,Ru^{-1}),\qquad u\in(\mathbb Z/M\mathbb Z)^\times.}
\]

There are exactly \(\varphi(M)\) such pairs, with

\[
\varphi(M)\ge\sqrt{M/2}\ge\frac{\sqrt{N-1}}2.
\]

Moreover,

\[
(x+y)^2-4N\equiv R^2(u-u^{-1})^2\pmod M.
\]

Factor swap is exactly \(u\leftrightarrow u^{-1}\). Product,
square-discriminant, symmetric-ring, quadratic-character, support-prime
Jacobi, and genus-vector tests all preserve this inversion. For
\(N\equiv3\pmod4\), every odd prime \(\ell\mid KE\) has the predetermined
Jacobi sign

\[
\left(\frac{\ell}{N}\right)=\chi_4(\ell).
\]

The remaining postprocessor must use nonsymmetric Archimedean size or exact
division, nonquadratic class-group data, an adaptive factor-free transition,
or the integer-specific reciprocal-prefix selector. The statement, proof,
hostile audit, and blind reconstruction have SHA-256 hashes
`d3ca187a62f3706749cbe3f0083c25dccf7b82b21edf3c514377b2cc839c0774`,
`692c011c170e81251faa4ae590c2b927ed2ecd0b21c4c5d2d4f715aeee101484`,
`e9c1373f0e00e3771bd40a3ae2071dad58c767537b4774b331cb1a472acaff00`,
and
`d44b7a9f3c3c15820c983c5ad8f58dd69bf6d642a384f11a0ae8d209ebdeae7a`.

## P182 — the natural vector completion preserves the hard coefficient at the same index

**Status:** promoted from F206 after a fresh hostile audit and a strict
statement-only reconstruction. This is a named-model boundary. It is not a
factoring algorithm or a lower bound against arbitrary nonholomorphic or
integer-specific constructions.

Let

\[
A(n)=\sum_{d\mid n}d\chi_4(d),\qquad
L(q)=\sum_{n\ge1}A(n)q^n,
\]

and

\[
P(q)=\frac{(q;q^4)_\infty}{(q^3;q^4)_\infty},\qquad
R(q)=\frac{P(q)}{P(-q)}.
\]

The exact radial asymptotics at the two rational cusps are

\[
P(e^{-t})\sim
2\frac{\Gamma(3/4)}{\Gamma(1/4)}\sqrt t,
\qquad P(-e^{-t})\longrightarrow\sqrt2,
\]

\[
L(e^{-t})=\frac1{2t}-\frac t{24}+O(t^3),
\qquad L(-e^{-t})=-\frac t8+O(t^3).
\]

Consequently \(P,R,L\) have different nonexponential polynomial powers at
the cusps \(0\) and \(1/2\). For an ordinary finite-dimensional
meromorphic vector-valued modular form of one fixed weight, with semisimple
parabolic monodromy and finite-principal-part Puiseux expansions, every
nonzero nonexponential fixed projection has the same power \(-k\) at every
rational cusp. Hence no fixed projection in this model equals \(P\), \(R\),
or \(L\).

Define the transposed coefficient

\[
A^\vee(n)=\sum_{d\mid n}d\chi_4(n/d).
\]

For every odd \(n\),

\[
\boxed{A^\vee(n)=\chi_4(n)A(n).}
\]

The two Mellin transforms are

\[
\mathcal M_A(s)=\Gamma(s)(2\pi)^{-s}\zeta(s)L(s-1,\chi_4),
\]

\[
\mathcal M_\vee(s)=\Gamma(s)(2\pi)^{-s}\zeta(s-1)L(s,\chi_4),
\]

and satisfy

\[
\mathcal M_A(s)=2^{3-2s}\tan(\pi s/2)\mathcal M_\vee(2-s).
\]

After conductor normalization, the reflection matrix has off-diagonal
entries \(2\tan(\pi s/2)\) and
\(-\tfrac12\cot(\pi s/2)\). No fixed basis gives a constant Fricke matrix;
the hostile audit supplied a direct pole-order proof in addition to the
matrix calculation. A fixed finite collection of Euler derivatives,
antiderivatives, and period-polynomial corrections changes Mellin kernels
only by rational functions and finitely many polar terms, so it cannot
remove the infinite alternating pole-zero pattern.

A Whittaker or Mellin-convolution correction can absorb the archimedean
factor, but it leaves the arithmetic coefficients \(A(n)\) and
\(A^\vee(n)\) unchanged. At an odd target \(N\), the dual amplitude is only
the public sign \(\chi_4(N)\) times the original factoring-equivalent
amplitude at the same index. The functional equation transforms a global
kernel sum; it does not send \(N\) to a smaller public arithmetic state.

The theorem leaves open nonsemisimple logarithmic cusp data, a genuinely new
mock or nonholomorphic arithmetic shadow, nonpolynomial quantum cocycles,
QP-growing state, nonlinear identities, and adaptive integer-specific
decoders. The statement, proof, hostile audit, and blind reconstruction have
SHA-256 hashes
`a35bfc475cb068bab78cb3f12bae605492ab22f4b208b6c809f7692f1cd4805c`,
`e617d242fe213e9ea5ec691493e7694c2550ab6a559a7eaf4eeee1f8aa2464cc`,
`dc830b3f2fbb9bcc78f04782e3b06f0a884938f82e6e636864244c79395ed126`,
and
`b1b0c5fddcaef1a5170dcdd4b12831171f75294cd3413a0531f1f5a64f6dca1e`.
No cross-family or human audit has run.

## P181 — the binary q-product norm deletes the twisted odd coefficient

**Status:** promoted from F204 after a fresh hostile audit and a strict
statement-only reconstruction passed. This is a boundary for four named
fast-forward mechanisms applied to P179's first twisted coefficient. It is
not a coefficient evaluator, factoring algorithm, or general lower bound.

Let \(\chi=\chi_4\), and define

\[
A(n)=\sum_{d\mid n}d\chi(d),\qquad
L(q)=\sum_{n\ge1}A(n)q^n,
\]

and

\[
P(q)=\frac{(q;q^4)_\infty}{(q^3;q^4)_\infty}
=\prod_{a\ge1}(1-q^a)^{\chi(a)}.
\]

Then, as formal power series,

\[
L(q)=-q\frac d{dq}\log P(q),
\qquad
P(q)P(-q)=P(q^2),
\]

so

\[
L(q)+L(-q)=2L(q^2)
\iff A(2n)=A(n).
\]

This loss is exact. For any \(G(q)\in1+qR[[q]]\) over a rational algebra,
writing \(\log G=\sum g_nq^n\), the same norm equation is equivalent to

\[
2g_{2n}=g_n.
\]

Every odd \(g_r\) is free, and all iterated binary norms still impose no
equation at an odd target \(N\).

There is a narrow scalar modular boundary. For

\[
F_{a,b,\alpha}(\tau)
=e^{2\pi i\alpha\tau}P(q)^aP(-q)^b,
\]

assume a nonzero scalar meromorphic modular form of one fixed real weight,
with multiplier, on a finite-index subgroup, and ordinary meromorphic
Fourier expansions at rational cusps. The radial asymptotics

\[
P(e^{-t})\sim
2\frac{\Gamma(3/4)}{\Gamma(1/4)}\sqrt t,
\qquad
P(-e^{-t})\longrightarrow\sqrt2
\]

force \(a=b\) by comparing the cusp powers at zero and one-half. But the
odd-\(N\) coefficient of
\(-q\,d\log(P(q)^aP(-q)^b)/dq\) is

\[
(a-b)A(N).
\]

Thus every monomial in this binary orbit that retains the selector fails
the stated scalar cusp condition, while every monomial surviving the test
deletes it. No converse modularity claim is made.

The Lambert series also satisfies no fixed finite linear base-two Mahler
equation over \(\mathbb Q(q)\), homogeneous or inhomogeneous. Modulo two,

\[
A(n)\equiv1
\iff \operatorname{oddpart}(n)\text{ is a square}.
\]

For \(s_e(k)=A(2^ek+1)\bmod2\), the witnesses
\(k_e=2^e+2\) give \(s_e(k_e)=1\), while
\(s_f(k_e)=0\) for \(f\ge e+2\). Hence the two-kernel is infinite and the
sequence is not two-automatic. Primitive integral reduction of a proposed
linear Mahler relation would, by Frobenius, make the generating series
algebraic over \(\mathbb F_2(q)\); Christol's theorem gives the
contradiction.

Finally, for an odd prime \(\ell\), primitive \(\ell\)-th root \(\zeta\),
and \(\epsilon=\chi(\ell)\),

\[
\prod_{j=0}^{\ell-1}P(\zeta^jq)
=\frac{P(q^\ell)^{1+\ell\epsilon}}
       {P(q^{\ell^2})^\epsilon},
\]

which yields only

\[
A(\ell k)
=(1+\ell\epsilon)A(k)
-\epsilon\ell\,\mathbf1_{\ell\mid k}A(k/\ell).
\]

A fixed public \(\ell\) contracts the target only when \(\ell\mid N\),
where its gcd already factors; otherwise it moves to \(A(\ell N)\).

P181 closes the binary norm, scalar binary-orbit modular monomial, fixed
linear binary-Mahler, and fixed root-norm routes. It leaves open
vector-valued or nonholomorphic completions, nonlinear functional equations,
QP-growing state, and adaptive one-child integer selectors. The obstruction
is same-node information loss, not recursion depth.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`020717143764c86138c4ac0d211924884330385c2d7a578c1e1c4a540c2f5929`,
`705dff58fcda88f8d7906e9019289f7d8ba73e0d85e56ab7a3e5dcefa3e87c91`,
`ad99343487f2b211c131211252236c08149cb0a1a8ed71f437d11a818a2ec017`,
and
`024d24dadf8a42ff646ace29e874776e66306eebe2d343785088e78150ded7a5`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P180 — the factored square gap leaves a principal-genus orientation gate

**Status:** promoted from F202 after a fresh hostile audit and a strict
statement-only reconstruction passed. This is a named-mechanism boundary for
balanced squarefree semiprimes. It is not a lower bound against arbitrary
uses of the factored child and is not a factoring algorithm.

Let

\[
N=pq,\qquad p<q<2p,\qquad
B=\lfloor\sqrt N\rfloor,\qquad E=N-B^2.
\]

Writing

\[
a=B-p,\qquad c=q-B,\qquad d=c-a=p+q-2B
\]

gives the exact integer identities

\[
E=Bd-ac,qquad a^2+E=pd,qquad c^2+E=qd,
\]

and

\[
d^2+4Bd-4E=(q-p)^2.
\]

Here \(d\) is positive and even, \(d\le q-p<p\), and
\(1\le E\le2B\). Thus the correct \(d\) factors by one square test.
Furthermore,

\[
\gcd(E,N)=\gcd(B^2,N).
\]

A nonunit value already factors. On the coprime branch,
\(B^2\equiv-E\pmod N\). A mixed CRT root of this congruence factors through
the two gcds with \(r\pm B\), and the factors conversely construct such a
root. Likewise, a norm representation \(N=x^2+Ey^2\) yields a root
\(xy^{-1}\), but a second mixed principal representation is not guaranteed.

The child \(E\) has roughly half the input bits and in particular fewer than
\(n\) bits. Recursively factoring it is complexity-safe. This is only
conditional accounting: the recursive routine must already factor arbitrary
smaller integers, since \(E\) need not satisfy the parent semiprime promise.

The complete factorization of \(E\) does not orient the factors through the
literal supported congruence sieve. For every \(m\mid E\), every unit
candidate \(x\bmod m\), and \(y=Nx^{-1}\), the candidate offset
\(d_x=x+y-2B\) automatically satisfies

\[
d_x^2+4Bd_x-4E
=\left(\frac{x^2-B^2}{x}\right)^2\pmod m.
\]

Thus product consistency and the discriminant-square test accept every unit
candidate factor residue.

There is an exact class-group explanation. In
\(\mathcal O=\mathbb Z[\sqrt{-E}]\), let
\(\alpha=B+\sqrt{-E}\), and write \(C=[\mathfrak p]\) for the proper
invertible ideal class over \(p\) selected by \(\alpha\). The two mixed-root
classes are \(C^2\) and \(C^{-2}\). Every genus character is therefore
\(+1\) on them. A mixed principal norm exists exactly when \(C^2=1\), while
the canonical invertible ambiguous classes supplied by discriminant factors
generate only two-torsion and need not reach a nontrivial square.

The exact certificate

\[
N=2627=37\cdot71,\qquad B=51,\qquad E=26=2\cdot13
\]

has mixed root \(162\), which factors via
\(\gcd(162-51,N)=37\) and \(\gcd(162+51,N)=71\). Yet
\(x^2+26y^2=2627\) has only the public solutions
\((\pm51,\pm1)\). The mixed form reduces to \([3,-2,9]\), whereas the
ramified classes generate only
\(\{[1,0,26],[2,0,13]\}\). Thus neither a second principal norm nor the
factor-supported ambiguous subgroup is forced.

P180 leaves open full-class-group navigation, nonlocal auxiliary moduli,
Archimedean statistics, joint use with another recursively factored child,
and direct P175 reciprocal-prefix selection.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`266e527434b5c6b9f3a680b0ea31498cd8f55411d1ec75a459f4d8bd21587719`,
`7a7227718561de054330a1ae29c128e20e1bff477125370856376fcb7759e8cf`,
`eda0cad418001cda557c9c2ade61ad185d1b4df6bb5165009b13c8733cb9c540`,
and
`782e6acfc4d1d98c16996d5523155c1bc19064ca86f6b783647925636132ac20`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P179 — a twisted divisor coefficient is the exact beta-two lift selector

**Status:** promoted from F203 after a fresh hostile audit and a strict
statement-only reconstruction passed. This is an exact evaluator target and
quotient-state boundary for balanced squarefree semiprimes. It does not
evaluate the coefficient or factor unrestricted integers.

Let

\[
N=pq,\qquad p<q<2p,
\]

let \(m=2^t<p\), and suppose the correct P175 prefix
\(u\equiv p^{-1}\pmod m\) is known. Put

\[
r\equiv u^{-1}\equiv p\pmod m,
\qquad
c\equiv Nu\equiv q\pmod m,
\]

using the odd representatives in \([1,m-1]\). Define the signed two-lift
weight

\[
w_{m,r}(d)=
\begin{cases}
+1,&d\equiv r\pmod{2m},\\
-1,&d\equiv r+m\pmod{2m},\\
0,&d\not\equiv r\pmod m.
\end{cases}
\]

Let \(v=r^{-1}\bmod 2m\), \(c_0=Nv\bmod2m\), and, when \(c=r\),
let \(\lambda=w_{m,r}(c_0)\). The exact twisted divisor coefficient

\[
S_{m,r}(N)=\sum_{d\mid N}d\,w_{m,r}(d)
\]

has the Lambert-series representation

\[
S_{m,r}(N)
=[X^N]\sum_{a\ge1}\frac{a w_{m,r}(a)X^a}{1-X^a}.
\]

After subtracting the public \(d=1,N\) terms, write the result as \(T\).
If \(\epsilon=w_{m,r}(p)\), then

\[
T=
\begin{cases}
\epsilon p,&c\ne r,\\
\epsilon(p+q),&c=r,\ \lambda=+1,\\
\epsilon(p-q),&c=r,\ \lambda=-1.
\end{cases}
\]

Every case reveals the next reciprocal bit and factors \(N\) in polynomial
time. Conversely, the factorization evaluates the coefficient. At the first
stage \(m=2,r=1\), the weight is \(\chi_4\); thus the fixed integer-specific
coefficient

\[
\sum_{d\mid N}d\chi_4(d)
\]

already factors every distinct odd semiprime. The divisor weight \(d\) is
what retains the Archimedean orientation; the unweighted character sum need
not do so.

The canonical quotient state

\[
K=\frac{N-rc}{m}
\]

satisfies \(0<K<N/2\) and \(\gcd(K,N)=1\). Put
\(\delta=K\bmod2\). If the candidate bit for \(p\) is \(a\), the candidate
bit for \(q\) is \(b=a\mathbin{\mathsf{xor}}\delta\), and the two next
quotient states are

\[
K'_a=\frac{K-ac-br-abm}{2}.
\]

They are positive, smaller than \(N/(2m)\), and coprime to \(N\). However,

\[
K'_0=K'_1
\iff \delta=1\text{ and }r=c.
\]

In particular, for \(m=2\) and \(N\equiv3\pmod4\), both orientations give

\[
K'_0=K'_1=\frac{N-3}{4}.
\]

Thus quotient contraction can erase precisely the sign needed to select the
smaller factor. Factoring the coalesced child is not proved useless, but the
child value alone carries no orientation.

The size accounting remains valid only conditionally: an eventual algorithm
whose *whole* recursion is one nested chain may use

\[
\mathcal T(n)\le\mathcal T(n-1)+\operatorname{QP}(n).
\]

Having at most one call per selector stage does not itself prove that global
recursion shape. The live beta-two problem is now exact: evaluate the
twisted divisor coefficient, or obtain an equivalent nonlinear integer
syndrome that selects one reciprocal-prefix child without materializing an
exponential AP product.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`10481fa918cffefe71eee3dee08ad23b7b837d685c899a23e5c03a2a74aa9b4f`,
`415b2079baed3b0d01ffa1b82d2d537dbf5288c2dce0640a0175f4bb1515c174`,
`bcd961ec52dfd0d6adc6004bd8e5adb36d7d8d5b8422245ffb0c5ca659feb7a1`,
and
`017045ff4286f6c9de54d20313398ef15fa21178c552c2c08efdbc3273ee2b98`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P178 — dyadic AP sibling division loses the active prime before it contracts

**Status:** promoted from F201 after a fresh hostile audit and a strict
statement-only reconstruction passed. This is a named-mechanism boundary for
balanced squarefree semiprimes. It is not a lower bound for implicit AP
products, adaptive nonlinear selectors, or factoring.

Let

\[
N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor,
\]

and consider one consecutive arithmetic-progression cell in

\[
I_B=(\lceil B/2\rceil,B]\cap\mathbb Z
\]

with step \(m=2^t\), known to contain \(p\). Split it by index parity.
If its cardinality is odd, gcd-screen and remove the single public extra
endpoint; that screen either factors \(N\) or leaves two equal-size children

\[
e_i=c+2mi,\qquad o_i=e_i+m,\qquad 0\le i<s.
\]

Their products

\[
E=\prod_{i<s}e_i,\qquad O=\prod_{i<s}o_i
\]

have exactly one active axis: one is divisible by \(p\), the other is not,
and neither is divisible by \(q\). Thus either modular product would select
the next bit, but P178 does not evaluate it.

Interlacing gives the exact Archimedean bound

\[
1<\frac OE\le\frac{o_{s-1}}{e_0}<2.
\]

Therefore ordinary Euclidean division is

\[
\boxed{O=E+D,\qquad D=O-E,\qquad 0<D<E.}
\]

In both possible orientations,

\[
\boxed{p\nmid D.}
\]

The other hidden prime may divide \(D\) accidentally; no unit-gcd claim is
made. Reverse division has quotient zero and simply returns \(E\). Writing
the products as rising factorials or gamma quotients changes no integer and
therefore leaves the same quotient and remainder.

Moreover,

\[
D\ge m\prod_{i=1}^{s-1}e_i
 \ge m(B/2)^{s-1}.
\]

At the P175 precision

\[
t=\left\lfloor\frac14\log_2N\right\rfloor-(\log n)^{O(1)},
\]

the full cell has

\[
s=\Theta\!\left(N^{1/4}2^{(\log n)^{O(1)}}\right)=2^{\Theta(n)},
\]

so the exact ordinary remainder itself has \(2^{\Theta(n)}\) bits. This is
an output-size statement for explicit materialization, not a circuit lower
bound.

Finally, for \(F_{\alpha,\beta}=\alpha E+\beta O\), reduction modulo \(p\)
gives

\[
p\mid E\Longrightarrow
 p\mid F_{\alpha,\beta}\iff p\mid\beta,
\qquad
p\mid O\Longrightarrow
 p\mid F_{\alpha,\beta}\iff p\mid\alpha.
\]

Hence a fixed public linear form with unit coefficients loses the guaranteed
active-prime support on both axes. Coefficients that restore both axes either
already expose a gcd or give the trivial zero form.

This obstruction is not about recursion depth. A correct next-bit selector
would need only \(O(n)\) stages, and a unique integer child may satisfy

\[
T(n)\le T(n-1)+\operatorname{QP}(n).
\]

The live beta-two problem remains a QP implicit AP-cell selector, a nonlocal
integer carry or floor, or another support-preserving one-child auxiliary.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`4915cbeea9e258524ece5dcf21e115f1a6c8ef0775dd0d1b926b94cdcbda8d41`,
`56dce149bdd39b545b35e695108aa8a1dd3fa0bb8cc891aaf437a95d03e82e17`,
`d9177c17ce57a6466c42484c4870ea3131673af4a3b54b38d36d736cc2756726`,
and
`525199ece25960c647a3e04ab67046057bfd6d73d6fbdf219daf80a632379798`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P177 — the beta-two defect is one Archimedean denominator delta

**Status:** promoted from F200 V2 after a fresh hostile re-audit and a
strict statement-only reconstruction passed. V1 and its failed audit remain
preserved. This is a named-model boundary, not a factoring algorithm or a
general arithmetic-circuit lower bound.

On the balanced semiprime promise, put

\[
A_k=(-1)^k\binom{N-1}{k},\qquad
x_j=\frac{A_{j-1}}j,\qquad 1\le j\le B=\lfloor\sqrt N\rfloor.
\]

The exact recurrence gives

\[
x_j=\frac{A_{j-1}-A_j}{N}.
\]

Every (x_j) is an integer except at the unique hidden index (j=p), and

\[
\boxed{x_j+\mathbb Z=\frac1p\mathbf1_{j=p}}
\qquad\text{in }\mathbb Q/\mathbb Z.
\]

For any subset (I\subseteq\{1,\ldots,B\}), let

\[
S_I=\sum_{j\in I}x_j,
\qquad
D_I=NS_I.
\]

Then (p\notin I) gives (S_I\in\mathbb Z), (D_I\equiv0\pmod N),
and \(\gcd(D_I,N)=N\). If (p\in I), then

\[
S_I\in\mathbb Z+\frac1p,
\qquad
D_I\equiv q\pmod N,
\qquad
\gcd(D_I,N)=q.
\]

The complementary index-product test returns (1) or (p). For an interval,

\[
S_{[a,b]}=\frac{A_{a-1}-A_b}{N}.
\]

Thus exact harmonic support, rational integrality, endpoint-difference gcd,
and arithmetic-progression product support are the same factor-bearing event.
At the root,

\[
\sum_{j=1}^Bx_j=\frac1p-h,
\qquad
\boxed{h=-\left\lfloor\sum_{j=1}^B\frac{A_{j-1}}j\right\rfloor}.
\]

This identifies the P175 carry as an Archimedean floor defect.

The quotient-valued signal has full Walsh and Fourier support. Its
unnormalized Haar transform has exactly one nonzero wavelet at every scale,
forming the path to (p). This sparsity does not locate the path. On any
finite dyadic partition, for every proposed leaf \(\ell\) and residue (u),
subtracting (u) on all ancestors of \(\ell\) preserves every parent-equals-
children equation. Ordinary integers represent every finite (2)-adic
residue. Hence finite additive consistency gives the same feasible correction
for every proposed path; only the actual Archimedean floors orient it.

For the reciprocal-prefix cell

\[
C_{t,a}=\{j\le B:j\text{ odd and }j^{-1}\equiv a\pmod{2^t}\},
\]

inversion turns membership into one arithmetic progression. Its literal
endpoint representation has

\[
\frac B{2^t}+O(1)
=N^{1/4}2^{(\log n)^{O(1)}}
\]

runs at P175 precision. Uniform sampling has the reciprocal exponential hit
rate. These are exact costs for those named evaluators, not lower bounds for
implicit circuits.

Finite factor-free auxiliary residue rings and value-local continuous
(2)-adic or Mahler tests cannot recognize integer versus integer-plus-
(1/p), because ordinary integers already fill every finite residue class
and are dense in \(\mathbb Z_2\). Bounded-frequency complex phases have only
exponentially small separation. An exact high-order phase test is equivalent
to the support gcd and therefore already factors.

The optional local cyclotomic statement is strictly conditional. Pre-register
a QP extension-degree cap (D(n)), run P160--P161 with (T\ge D(n)), keep
its factor/common-order exits separate, and consider only the surviving
(H=1) branch. There (w) is a power of two and

\[
\operatorname{ord}_p(2)\ge\operatorname{ord}_p(w)>T\ge D(n).
\]

A finite extension of \(\mathbb Q_2\) containing a primitive (p)-th root
of unity has degree at least \(\operatorname{ord}_p(2)\), so no degree-
(D(n)) explicit cyclotomic realization contains the active phase on that
branch. This says nothing about complex approximation or implicit encodings.

The exact opening remains a QP nonlinear statistic of the specific integer
parts, a QP implicit exact phase evaluator, or another non-additive
integer operation selecting the correct prefix cell.

V2 statement, proof, hostile re-audit, and blind reconstruction hashes are
`1edaedf1e0121e4603b8502cfb2473de250366cdc4b35acb216c3be314c8b7e5`,
`b573b44d35d577e4c567448092997923c0a83cdeda8a1a1cb89ec9e1cf03e30b`,
`7ff9aca10cd611c75bc492e54622916d3295b54cab765d1a239b988bcdc86d53`,
and
`3035bc728b7df3bebd140109b6e2e5adf14feab5091740987c7e6a29265f5901`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P176 — direct multiplicity and low-degree holdout do not select the beta-two reciprocal

**Status:** promoted from F199 after a fresh hostile audit and a strict
statement-only reconstruction passed. This is an exact boundary for direct
congruence-jet and feature-space encodings. It is not a factoring algorithm
and not a lower bound against nonlocal integer features or adaptive prefix
syndromes.

Retain the balanced squarefree semiprime promise and the P175 precision

\[
N=pq,\qquad p<q<2p,\qquad
t=\left\lfloor\frac{\log_2N}{4}\right\rfloor-L(n),
\qquad L(n)=(\log n)^{O(1)}.
\]

Let

\[
A=(-1)^B\binom{N-1}{B},\qquad
z=N^{-1}(A-1)\pmod{2^t}.
\]

For every odd candidate (u\bmod2^t), put

\[
P=u^{-1},\qquad Q=Nu,\qquad H=z+u.
\]

Then

\[
PU=1,\qquad Q=NU,\qquad H=z+U
\]

parametrizes all (2^{t-1}) candidates. More precisely,

\[
(\mathbb Z/2^t)[U,P,Q,H]/(PU-1,Q-NU,H-z-U)
\cong(\mathbb Z/2^t)[U,U^{-1}],
\]

and the Jacobian minor in (P,Q,H) has unit determinant (U). The true
candidate (u=p^{-1}\bmod2^t) is therefore not a singular or
higher-multiplicity point of this public system.

The same saturation appears in the public coefficient transcript. For

\[
A_i=(-1)^i\binom{N-1}{i},\qquad
z_i=N^{-1}(A_i-1)\pmod{2^t},
\]

every supplied (z_i) is polynomial-time computable and

\[
(i+1)(z_{i+1}-z_i)+1+Nz_i=0.
\]

The two state derivatives of this recurrence sum to the odd unit (N).
Hence the recurrence remains smooth at the hidden edge (i=p-1). The
one-spike word appears only after inserting the unavailable integer quotient
labels

\[
H_i-z_i\equiv p^{-1}\mathbf 1_{i\ge p}\pmod{2^t}.
\]

Direct Boolean holdout also has an exact degree boundary. On the
(m=t-1) free bits of an odd reciprocal, every nonzero multilinear
degree-(d) polynomial has support at least

\[
2^{m-d}.
\]

Thus a singleton needs degree (m=\Theta(n)), and deleting only a QP
number of candidate columns does not reduce the span of a polylog-degree
Reed--Muller feature matrix. Higher Hasse vanishing is no shortcut: order at
least two at every point except one forces vanishing at the missing point,
because it lies in a constrained neighbor's radius-one ball.

Every one-bit lift remains paired. If (u_1=u_0+2^j\pmod{2^{j+1}}), then

\[
u_1^{-1}=u_0^{-1}+2^j,
\qquad
Nu_1=Nu_0+2^j
\pmod{2^{j+1}}.
\]

Both children satisfy the full public congruence system. Up to the P175
quarter precision, each child also has plausible integer representatives
obeying the balanced size inequalities. Primality and the exact product
equation are precisely the missing integer selector.

The result deliberately leaves the valid sequential route open. A prefix
cell of codimension \(\ell\) has an exact degree-\(\ell\) indicator. For
polylogarithmic \(\ell\), its feature space is QP. A QP syndrome that
selected the correct cell at each of (O(n/\ell)) stages would therefore
give a valid one-child QP chain; no fixed-ratio contraction is needed.
F199 supplies no such syndrome and proves no lower bound against one,
nonlocal Euclidean carries, canonical integer representatives, aggregate
interval statistics, nonlinear target-correlated embeddings, or sparse
high-degree circuits.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`04c309ece29db251826247c6cfee7481b9e0b1a4e17c2ef5839ee06ac73be38c`,
`5324fe02ed675f4aedb5925559fa4a7cbc8d42295bbe41d33a775810d479c8f9`,
`65dd4b28ac858014d98f0bda0e378dd7b8aa71bdd54acdcf2e4ae27712646a3e`,
and
`b2fe548fdc21d6337fbc99e340333b4b6b0b6d02859489112e5f9aa072de66ec`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P175 — a quarter-minus-polylog beta-two carry prefix is terminal

**Status:** promoted from F198 after a primary-source hostile audit and a
strict statement-only reconstruction passed. This is a literature-dependent
promise reduction for balanced squarefree semiprimes. It does not evaluate
the carry and is not an all-input factoring algorithm.

Let

\[
N=pq,
\qquad p<q<2p,
\qquad n=\lceil\log_2(N+1)\rceil,
\qquad B=\lfloor\sqrt N\rfloor,
\]

where \(p,q\) are distinct odd primes. Put

\[
C=\binom{N-1}{B},
\qquad A=(-1)^BC,
\qquad h=\frac{A-(1-q)}N.
\]

P171 proves that \(h\) is an integer, and P173 proves that the corrected
Andreica power-of-two algorithm computes \(A\bmod2^n\) in deterministic
polynomial bit time. For every \(1\le t\le n\), define the public residue

\[
z_t=N^{-1}(A-1)\pmod{2^t}.
\]

This is modular multiplication by the inverse of the odd integer \(N\); it
does not assert that \((A-1)/N\) is integral. The exact equality

\[
Nh=A-1+q
\]

gives

\[
\boxed{h-z_t\equiv p^{-1}\pmod{2^t}.}
\]

Consequently, for any public polynomial-time precision schedule, the two
promise functions

\[
h\bmod2^t
\quad\text{and}\quad
p\bmod2^t
\]

are interreducible by deterministic polynomial-time one-query reductions:
subtract \(z_t\) and invert modulo \(2^t\), or invert the odd residue of
\(p\) and add \(z_t\). At

\[
t_0=\left\lceil\frac n2\right\rceil,
\]

the canonical residue is the exact integer \(p\), because

\[
0<p<\sqrt N<2^{n/2}\le2^{t_0}.
\]

Only approximately half that precision is needed for a QP terminal. Since
\(N\) is odd,

\[
\lfloor\log_2N\rfloor=n-1.
\]

Set

\[
k=\left\lfloor\frac{\log_2N}{4}\right\rfloor
 =\left\lfloor\frac{n-1}{4}\right\rfloor,
\qquad
t=k-L(n),
\]

where \(L(n)=(\log n)^{O(1)}\) is a fixed public integer-valued function
and \(t\ge1\). From one value \(h\bmod2^t\), obtain
\(s=p\bmod2^t\) and put \(m=2^t\). The hypotheses of
Gao--Feng--Hu--Pan Theorem 3.1 with \(r=1\) hold:

\[
\gcd(m,N)=1,
\qquad 1\le s<m<N,
\qquad p\equiv s\pmod m.
\]

Its deterministic cost is

\[
O\!\left(
\left\lceil\frac{N^{1/4}}{2^t}\right\rceil
\log^{7+3\epsilon}N
\right)
<2^{L+1}\operatorname{poly}(n),
\]

for fixed \(\epsilon>0\), hence numerical QP. This direct terminal does
not enumerate the missing bits.

Independently, enumerate the \(2^L\) residues modulo \(2^k\) that extend
\(p\bmod2^t\). One is \(p\bmod2^k\). Coppersmith's 1997 Theorem 5
factors from the low

\[
\left\lfloor\frac14\log_2N\right\rfloor
\]

bits of one factor in deterministic polynomial time. Running it on every
extension and verifying every candidate by exact division costs
\(2^L\operatorname{poly}(n)\), again numerical QP.

Thus the live beta-two problem is narrower than P173 stated: it is enough
to compute about the first quarter of the hidden reciprocal \(p^{-1}\) in
\(\mathbb Z_2\), allowing a polylogarithmic precision deficit. A sequential
one-bit lift has only \(O(n)\) stages and would be QP if each correct lift
were selected in QP time. F198 supplies no such selector and proves no lower
bound below this precision.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`244e44b2d93fe6f62ef2ceb161b67132a12d3741a54a6ff80a2930e438dce0bb`,
`7bde29f9c62ab8fa357f7103615a8c5a45db5a38ddb4e94a9bc576bde5bba12a`,
`0310958a949fdb582f5f581a03d95288d133757553a9aad1f092e8c63d55c8f1`,
and
`a25c0674733fabefe12a3b08dd0747f58d69691dcef3b6446e2e0bc5ae837c3d`.
No computation, cross-family audit, or human audit has run.

## P174 — the factorial quotient-bit gate survives every named classical representation

**Status:** promoted from F197 after a primary-source hostile audit and a
strict statement-only reconstruction passed. This is an exact collection of
named-model boundaries and published upper scales. It is not a lower bound
for general arithmetic circuits, modular factorial algorithms, or factoring.

Let

\[
N=pq,
\qquad
p<q<2p,
\qquad
n=\lceil\log_2(N+1)\rceil,
\qquad
B=\lfloor\sqrt N\rfloor,
\qquad
F=B!,
\]

where \(p,q\) are distinct odd primes. Then

\[
p\le B<q,
\qquad
B<2p,
\qquad
v_p(F)=1,
\qquad
v_q(F)=0,
\]

and therefore

\[
\gcd(F,N)=\gcd(F,N^2)=p.
\]

The same is true for the exact numerator

\[
D=\prod_{j=1}^{B}(N-j)
=F\binom{N-1}{B}.
\]

Thus a method that materializes either product or its canonical residue
modulo \(N\) or \(N^2\) reaches the factor-bearing gcd before it performs
the nonunit division. This does not cover a compressed method that never
materializes those values.

For the explicit dense block representation

\[
P_u(X)=\prod_{j=1}^{u}(X+j),
\]

materializing its coefficients and all consecutive width-\(u\) block values
exposes at least

\[
u+\left\lceil\frac Bu\right\rceil\ge2\sqrt B
\]

positions. This is only a lower bound for that declared representation. The
published Bostan--Gaudry--Schost factorial/holonomic algorithm has the
matching square-root-in-\(B\) upper scale, and the Costa--Harvey
multitape-Turing refinement improves the complete deterministic factoring
bound by a factor of \(\sqrt{\log\log N}\) without changing the
\(N^{1/4}\) power. No universal lower bound is inferred.

The exact lift laws show why ordinary modular division does not repair the
gate. Write \(F=pU\) with \(\gcd(U,N)=1\). Then

\[
Fx\equiv Fy\pmod N
\iff
x\equiv y\pmod q,
\]

while

\[
Fx\equiv Fy\pmod{N^2}
\iff
pq^2\mid x-y.
\]

Multiplication by \(F\) loses a full local component modulo \(N\) and still
has a kernel of size \(p\) modulo \(N^2\). Its restriction to canonical
\(0\le x<N\) is injective, but inverse-based modular division remains
unavailable. A full residue modulo \(N^2\) contains a quotient digit, yet
its low base-\(N\) digit is already \(F\bmod N\), whose gcd factors.

The clean sufficient primitive is a quotient-bit block. Write

\[
F=NQ+R,
\qquad
Q=\left\lfloor\frac FN\right\rfloor,
\qquad
0<R<N.
\]

Then \(\gcd(R,N)=p\). The residue \(f_2=F\bmod2^n\) is deterministic
polynomial-time computable: if \(v_2(F)\ge n\), it is zero; otherwise
\(\lfloor B/2\rfloor<n\), so \(B<2n+2\) and direct modular multiplication
is polynomial. Hence

\[
Q_2=Q\bmod2^n
\]

is a sufficient factoring primitive, because

\[
R=\left(f_2-NQ_2\right)\bmod2^n
\]

as an exact integer in \(0<R<N<2^n\). Equivalently,
\(F\bmod(N2^n)\) contains \(R\) and \(Q_2\). The theorem proves
sufficiency only; it does not prove that factoring computes \(Q_2\) in QP
time.

Exact integers \(F,D,Q\) have \(2^{\Theta(n)}\) bits outside a finite
initial set, so sequential materialization is exponential. This does not
apply to a hypothetical succinct residue or quotient-bit evaluator.

Finally, the recursion correction is explicit. If there is only one
surviving child and

\[
T(m)\le T(m-1)+\operatorname{QP}(m),
\]

then \(T(m)\) is QP. Fixed-ratio contraction is not necessary. The named
factorial methods fail to become QP because their \(N^{1/4+o(1)}\) work is
paid at the current node before any smaller child exists, not because a
one-bit chain is too deep.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`774ce7c5496c28942d6cb11814b95cc2487ae10477127d40d8609332090e49c3`,
`6b30bd83a52b380c6f04e32c4839b924324b5e55688e48077265abd06e83bc84`,
`9cb4afd73e5c0ed925e55ceae9ba0bf6284ffc06f075d33e7089d9e4fadcea98`,
and
`feab5fecc6a83fc855a7a1aa66b8f15f060d68bace6a9fa1d6ac1d2686eee26d`.
No computation, cross-family audit, or human audit has run.

## P173 — the beta-two quotient carry alone is factoring-equivalent

**Status:** promoted from F196 after a source-level hostile audit and a strict
statement-only reconstruction passed. This is a literature-dependent
promise-function equivalence. It does not compute the carry or factor the
input.

Let

\[
N=pq,
\qquad
p<q<2p,
\qquad
n=\lceil\log_2(N+1)\rceil,
\qquad
B=\lfloor\sqrt N\rfloor,
\]

where \(p,q\) are distinct odd primes. Put

\[
C=\binom{N-1}{B},
\qquad
A=(-1)^BC,
\qquad
h=\frac{A-(1-q)}N.
\]

P171 makes \(h\) integral. The corrected form of Andreica's 2013
power-of-two binomial algorithm computes

\[
C_n=C\bmod2^n
\]

deterministically in polynomial bit time. The direct substitution is
\(T=n,P=N-1,Q=B\), which lies in the source's main parameter range. The
hostile audit independently reconstructed the algorithm after correcting
four typographical defects in the published formulas: two additions must be
multiplications, one recurrence uses the preceding index, and Legendre's
valuation uses floors. Those forced corrections preserve the published
polynomial bounds.

Define the promised function problems

\[
\mathcal F(N)=q,
\qquad
\mathcal H(N)=h\bmod2^n.
\]

They are interreducible by deterministic polynomial-time one-query
reductions. Given \(H=h\bmod2^n\), compute \(C_n\) and form

\[
q_0=
\left(
1+HN-(-1)^BC_n
\right)\bmod2^n.
\]

The exact identity \(q=1+hN-A\) gives
\(q_0\equiv q\pmod{2^n}\). Since \(0<q<N<2^n\), the canonical residue is
the exact factor \(q\).

Conversely, given \(q\), the odd integer \(N\) is invertible modulo \(2^n\),
and

\[
h\equiv
N^{-1}\left(q-1+(-1)^BC_n\right)
\pmod{2^n}.
\]

Thus a numerical-QP carry evaluator exists on this promise if and only if a
numerical-QP factorer does. The joint pair

\[
\left(C\bmod2^n,\ h\bmod2^n\right)
\]

has exactly the same complexity because its first coordinate is already in
deterministic polynomial time.

The equivalence is also exact base conversion. Euclidean division of the
possibly negative integer \(A\) gives

\[
A=(h-1)N+(N+1-q),
\qquad
0<N+1-q<N.
\]

For \(t\ge1\), let \(a_t=A\bmod(N2^t)\) be canonical. Then

\[
h\equiv1+\left\lfloor\frac{a_t}{N}\right\rfloor\pmod{2^t},
\qquad
q=N+1-(a_t\bmod N).
\]

Consequently, computing \(A\bmod(N2^n)\) is also polynomial-time equivalent
to factoring on the promise.

This theorem removes a false separation in the live beta-two primitive.
The \(2\)-adic coefficient is easy; the signed base-\(N\) quotient digit is
the entire hard coordinate. Rewriting it with odd factorials, \(2\)-adic
gamma functions, Kummer carries, or mixed-radix conversion is progress only
if the rewrite computes this digit. The result is a reduction, not a lower
bound against such an algorithm. Exact materialization of \(C\) has
exponential output length, but that does not rule out a succinct modular
method.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`07d2bccb9f508248a44f39faba3bd13a87cc0b2a1bc3dafa1464c348ae871c5c`,
`9f6e71c1c69661ad62780f0864b8fa460bd43df9f262b2774b7d231d20bba19b`,
`e9eeddfb8dc5cc9a36119bf6df74da24655e800395afae0848ea297a05c5e263`,
and
`f39f54088dbec5ed84cda7938521f2c378119e3b7069daf633f447f8061d2b00`.
No computation, cross-family audit, human audit, or publication-level
literature review beyond the focused source audit has run.

## P172 — the latest common-order terminal does not consume the beta-two hard branch

**Status:** promoted from F195 V2 after a primary-source hostile re-audit and
a strict statement-only reconstruction passed. This is a
literature-dependent terminal and interface theorem. It is not an all-input
QP factoring algorithm.

Suppose a public unit \(g\bmod N\) has one fully known exact order \(M\) in
every hidden prime-power component and

\[
\gcd(M,N)=1.
\]

Reduction modulo each underlying rational prime is injective on
\(\langle g\rangle\), because its kernel is a \(p\)-group. Hence

\[
\operatorname{ord}_p(g)=M,
\qquad
p\equiv1\pmod M
\]

for every rational prime \(p\mid N\). Gao--Feng--Hu--Pan Corollary 3.2,
with \(s=1,m=M\), therefore factors \(N\) in

\[
O\!\left(
\left\lceil\frac{N^{1/4}}M\right\rceil
\log^{7+3\epsilon}N
\right)
\]

bit operations for fixed \(\epsilon>0\), under the published hypotheses.
Thus a common order is already terminal when

\[
N^{1/4}/M=\operatorname{QP}(n).
\]

This has a smaller same-node search count and broader input scope than the
balanced \(\sqrt N/M^2\) enumeration terminal, but the two have the same QP
threshold class because

\[
\sqrt N/M^2=(N^{1/4}/M)^2.
\]

This terminal does not consume the existing beta-two hard state. Assume an
odd input beyond the finite lookup range has

\[
\operatorname{ord}_N(2)>C(n)
\]

for a numerical-QP cap \(C\). Harvey--Hittmeir Algorithm 3.1, run with
\(1\le D\le C\), returns \(2\) either at its initial size test or at the
first bounded-order test. It exits before the later smooth-number stage. Its
same-node cost is

\[
O\!\left(
\frac{D^{1/2}\log D}{\sqrt{\log\log D}}\log N
\right),
\]

with the source's convention for small \(D\). Substituting a fixed positive
power of \(N\) makes this cost exponential in \(n\). The valid one-child
recurrence

\[
T(n)\le T(n-1)+\operatorname{QP}(n)
\]

does not remove that current-node cost, because the bounded-order search
produces no smaller child before doing it.

The direct 2025 rank-three interface likewise retains an exponential list.
Its legal balanced parameters satisfy

\[
72<m<N^{1/4}/2,
\qquad
k=\Theta(N^{1/2}/m^{3/2})=\Omega(N^{1/8}).
\]

The direct order-bound certificate needs \(m^2k\le C\). The P161 roughness
certificate needs the largest prime \(P(k)\le k\) to lie below its roughness
cap \(T\); Bertrand's postulate gives \(T\ge P(k)>k/2\). Neither condition
is numerical QP throughout the published parameter range.

There is nevertheless an integer-specific fork. Scan ordinary rational
primes \(\beta\le B\), where

\[
\log n\ll\log B=o(n),
\]

and synchronize every bounded exact local order. If every scanned prime is
low, their public lcm \(M\) satisfies

\[
M\mid p-1,
\qquad
M\mid q-1,
\qquad
\Psi(p,B)\le M.
\]

The Harvey--Hittmeir smooth-number bound then gives
\(M\ge p^{1-o(1)}\), and the Gao--Feng--Hu--Pan congruence terminal factors
in QP time. Otherwise the branch exposes small ordinary integers of high
order; beta two is the first such witness in P159. The missing theorem is
still in this mixed high-order branch: several high witnesses need not reveal
their exact orders, generate independent directions, or factor.

The V2 statement, proof, primary-source hostile re-audit, and blind
reconstruction have SHA-256 hashes
`49df39f6311c00c9fa1fc2f54b7da715783f17da10eec302373fe0fe479e2c3a`,
`bdbcbcff93de0fb1cee7ecc2783d9edf1fb066f87f9c943bec4ce1d990205bb5`,
`d0aa16f2872303213af6141fbbdbb2ff8eac60c5f22915045d1ec942ef0e573f`,
and
`5e08a972df2395228b715ec0439aa7f2f5cf36adc7e62e93a10f75eb40496a64`.
No computation, cross-family audit, human audit, or publication-level
literature review beyond the focused primary-source re-audit has run.

## P171 — the balanced beta-two core is one hidden binomial cancellation

**Status:** promoted from F194 V3 after the repaired mathematical packet,
a focused metadata re-audit, and a strict statement-only reconstruction all
passed. This is a proof-only theorem for balanced squarefree semiprimes. It
does not supply a QP coefficient evaluator or a factoring algorithm.

Let

\[
N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor,
\qquad A_k=(-1)^k\binom{N-1}{k}.
\]

Then, for every \(0\le k\le B\),

\[
A_k\equiv
\begin{cases}
1\pmod N,&k<p,\\
1-q\pmod N,&p\le k\le B.
\end{cases}
\]

Equivalently, in the same prefix,

\[
\binom Nk\equiv
\begin{cases}
q\pmod N,&k=p,\\
0\pmod N,&k\ne p.
\end{cases}
\]

Therefore the single remote coefficient is a sufficient statistic:

\[
\boxed{\gcd\!\left(N,(-1)^B\binom{N-1}{B}-1\right)=q.}
\]

The mechanism is exact integer division, not an invertible ring operation.
The recurrence

\[
(k+1)(A_{k+1}-A_k)=-NA_k
\]

is constant modulo \(N\) except at the hidden nonunit index \(k+1=p\),
where cancellation releases \(N/p=q\). For comparison, if
\(m=\lceil B/2\rceil\), then

\[
m<p\le2m<q,
\qquad
\gcd\!\left(N,\binom{2m}{m}\right)=p,
\qquad
\gcd\!\left(N,\binom{2B}{B}\right)=q.
\]

The first comparison is the familiar interval-product zero predicate. The
remote coefficient above is a unit; only its signed shift exposes the
cofactor.

Two exact boundaries narrow the missing evaluator. First, every polynomial
index weight collapses:

\[
\sum_{k=1}^{N-1}W(k)\binom Nk
\equiv W(0)(2^N-2)\pmod N
\]

for all \(W\in\mathbb Z[T]\). Thus derivative moments and polynomial
quadrature do not isolate the hidden prefix coefficient.

Second, the logarithmic-size power circuit

\[
E_N(X)=(1+X)^N-1-X^N
\]

has derivative zero over \((\mathbb Z/N\mathbb Z)[X]\), but its exact local
\(X\)-adic orders are \(p\) modulo \(p\) and \(q\) modulo \(q\). With
\(d=q-p\), its nonzero local supports are

\[
E_N\equiv
\sum_{j=1}^{d}\binom djX^{pj}
+\sum_{j=0}^{d-1}\binom djX^{p^2+pj}\pmod p,
\]

\[
E_N\equiv
\sum_{j=1}^{p-1}\binom pjX^{qj}\pmod q.
\]

For a numerical-QP cap \(R<p\), the branch \(d<R\) is directly enumerable
from \(d^2+4N\). On the branch \(d\ge R\), every exponent class modulo every
\(r\le R\) has Boolean source support in both local expansions. This is only
an incidence obstruction: coefficient cancellation or a richer succinct
invariant could still separate the factors.

There is also an exact carry formulation. Put
\(C=\binom{N-1}{B}\) and

\[
h=\frac{(-1)^BC-(1-q)}N.
\]

For \(2^t>q\), the pair \((C\bmod2^t,h\bmod2^t)\) recovers \(q\). Either
residue alone is not claimed sufficient. Consequently the live beta-two
primitive is now precise: compute the remote signed coefficient, compute the
joint coefficient/carry pair, or recover one local \(X\)-adic order of the
succinct circuit in QP time. Direct truncation still has
\(B+1=2^{\Theta(n)}\) coordinates.

The V3 statement, proof, focused hostile re-audit, and blind reconstruction
have SHA-256 hashes
`95764227ebc288a528c7425c5593e9a75d7ad9030556c4a9c12b00c0c85f48ab`,
`ea19a8a5fe2410e24841876a5b04c4e6e23e4f9f466838e0a9ebaf83ffcbb029`,
`81c1a868db74021b068a7627ccecef6e0a27e2709109a706ed2ff85ab9180b1f`,
and
`fa4cd599d6391c4e50b715cd866d4e27b9aa4aeafb3949b18c467afe1970d4b9`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P170 — explicit QP separating representations saturate before they orient the hidden factors

**Status:** promoted from F193 V3 after a fresh hostile audit and a strict
statement-only reconstruction. This is a collection of four narrow interface
boundaries. It is not a general obstruction to modular forms, elliptic
curves, succinct representations, or factoring.

For a reduced modular-symbol endpoint (a/c) at squarefree level (N=pq),
the Γ₀((N))-cusp type is determined by (gcd(c,N)). An explicitly
listed endpoint of type (p) or (q) therefore factors (N) immediately.
If every endpoint has type (1) or (N), the explicit boundary sees only
the two global cusps. Good-prime Hecke correspondences preserve the cusp
type, Fricke swaps (d) with (N/d), and a selective Atkin–Lehner operator
must already reveal the exact divisor (p) or (q). This does not address
the boundary-zero cuspidal quotient or an implicit dense chain.

For (N=pq), the coefficient

\[
b_N=\sigma_1(N)=N+p+q+1
\]

satisfies (b_N<2^{n+1}). A uniform evaluator of (b_N) modulo enough
distinct auxiliary primes of (O(\log n)) bits reconstructs (b_N) by CRT
in QP time, then recovers (p+q) and factors (N). Thus a fixed small
modulus may be low-information, but a uniform growing bank is already a
factoring bridge.

At a fixed index (N), Dirichlet twists of one normalized eigenform satisfy

\[
a_{f\otimes\chi}(N)=\chi(N)a_f(N),
\]

so every such twist bank has rank at most one over the public character
values. It yields no new separating representation unless a nonzero base
coefficient is itself supplied by a stronger evaluator.

Finally, one endomorphism globally defined over the factor-free base acts on
good auxiliary-prime torsion with conjugate characteristic data in the two
hidden reductions. Characteristic-dependent Frobenius or a reduction-only
endomorphism remains outside the theorem and is exactly the missing fine
orientation.

The V3 statement, proof, hostile audit, and blind reconstruction have
SHA-256 hashes
`286ff3962751262c7256e5d78cfb0b510fb9563523765c9c9776e949eaeadc05`,
`71b21f064ddbc3e03bdaef8989125d7e3d68d88939a71845e16a6d184fbc188b`,
`062e73068040ecbec7189266cf8410690c687242795ff40ebfe8482f8ea2be8e`,
and
`14259e9fd45ea987f2d27097313ea1017eaa5e488d5ac6c72a76c4a61be4192e`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P169 — P164 supplies hidden ACD clusters, but the standard row lattice has coprime shortest vectors

**Status:** promoted from F192 after a fresh hostile audit and an independent
statement-only reconstruction. This is a narrow decoder obstruction, not a
general lattice, ACD, or factoring lower bound.

Let (N=PQ), where (P\ge Q) are distinct odd primes. Suppose a public
unit (w), a public base (a), and a cap (K\ge1) satisfy

\[
\ell\nmid a,
\qquad
\operatorname{ord}_\ell(a)>K
\]

for every prime \(\ell\) in either local order of \(w\). With \(R=K+1\),
the public word

\[
x_j=[w^{a^j}]_N,
\qquad 0\le j<R,
\]

is pairwise distinct modulo both hidden primes. Hence, for every
\(1\le m<R\), each hidden prime \(S\in\{P,Q\}\) has an existential cluster
of public differences

\[
z_i=St_i+r_i,
\qquad
0<r_i\le\left\lceil\frac{mS}{R}\right\rceil,
\qquad 1\le i\le m.
\]

Every \(z_i\) is a unit modulo \(N\). The cluster indices depend on the
hidden cyclic order and are not made public by this theorem.

Grant the correct cluster modulo the larger prime \(P\), and an integer
bound \(\widehat B\) with

\[
\left\lceil\frac{mP}{R}\right\rceil
\le\widehat B<Q.
\]

For the standard row lattice

\[
L=\left\langle
(\widehat B,z_1,\ldots,z_m),
(0,N,0,\ldots,0),\ldots,(0,\ldots,0,N)
\right\rangle_{\mathbb Z},
\]

one has \(\det L=\widehat B N^m\), and the hidden factor gives the literal
vector

\[
(Q\widehat B,Qr_1,\ldots,Qr_m)\in L.
\]

Put \(D=m+1\) and \(\epsilon=\widehat B/P\). If an integer \(A\ge2^m\)
satisfies

\[
\left(\frac{2\sqrt D}{\epsilon}\right)^m
<A<\frac Q{\sqrt D},
\]

simultaneous Dirichlet approximation constructs a lattice vector of norm
strictly below \(Q\widehat B\). Consequently every exact shortest vector
has coefficient \(c\) with \(0<|c|<Q\). Since \(c\), \(\widehat B\), and
all \(z_i\) are units modulo \(N\), every coordinate of every exact shortest
vector is a unit modulo \(N\). Exact Euclidean SVP followed by coefficient
or coordinate gcd tests therefore returns no factor.

For fixed-balance semiprimes, numerical-QP \(R\), polylogarithmic \(m\),
and the natural error scale \(\widehat B/P=O(m/R)\), the displayed interval
for \(A\) exists for all sufficiently large inputs. Thus the failure is not
a recursion-depth objection. A one-bit recursive chain remains QP; the
named lattice instead fails at the factor-extraction step.

An order-oblivious predeclared bank guaranteed to contain an \(s\)-label
consecutive block in every hidden oriented cyclic order needs at least

\[
\frac1R\binom Rs
\]

subsets. This is only a necessary count for unknown cyclic orders; it does
not apply to a selector that exploits the public recurrence
\(x_{j+1}=x_j^a\bmod N\).

The exact surviving interface is a source-aware local-cluster selector or a
different decoder that also proves local-order support for any smaller
integer it returns. Other lattices, robust ACD, affine targets, recurrence-
aware methods, and non-coordinate postprocessing remain open.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`23834b7193ce2f3e8e32a3277832fab633c2b7a701bd74591087b3d30ab57cb8`,
`73c520f978b47c7a937a5169456e8303818f69f6123a59ba5758ba4f9684e1f4`,
`80ad7501f1ebdd3e33f987ba8f8302a9d52981a4ca708d1f5208d37dc8543baf`,
and
`fb0950e52dcbadb189e9f1e77588748ee176a42388d74c12fbaaf93add249239`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P168 — Euclidean normalization conserves hidden support but does not localize it

**Status:** promoted from F191 V2 after a fresh hostile re-audit and a strict
statement-only reconstruction. V1's failed direct interface is preserved.
This is a named-model obstruction for the P164-to-P163 bridge. It is not a
factoring lower bound and does not describe the actual P164 transcript.

Let \(\ell\) be a prime, let \(\ell\mid X\), and write

\[
X=QD+R.
\]

If \(\ell\nmid D\), then

\[
\ell\mid R\quad\Longleftrightarrow\quad\ell\mid Q.
\]

Thus ordinary or centered reduction modulo an \(\ell\)-free divisor cannot
create \(\ell\)-support in the remainder. It retains that support exactly
when the discarded quotient already has it. If \(\ell\mid D\), the divisor
is only a usable P163 auxiliary after the separate conditions

\[
0<|D|<N/2
\]

are proved. Zero and oversized carriers do not satisfy the one-child
interface.

This loss is exact, not only possible in a loose complexity model. For every
composite \(N\) and every odd prime \(3\le\ell<N/2\) coprime to \(N\), take
the balanced nonzero representative \(c\equiv-N\pmod\ell\) and set
\(X=N+c\). Then \(\ell\mid X\), while the centered quotient and remainder
are \(1\) and \(c\). Both are nonzero and below \(N/2\), and both miss
\(\ell\).

A finite permutation-bank theorem strengthens this example. Grant \(B\)
public permutations \(\pi_i\) and the exact multiples
\(X_i(u)=\ell\pi_i(u)\). For centered division by \(N\), one selector retains
\(\ell\) in its quotient or remainder on at most \(N/\ell+2\) parameters.
If \(\ell\ge4B\) and \(N\ge8B\), a union bound gives a parameter for which
all \(2B\) quotient/remainder children are valid nonzero integers below
\(N/2\), but every one misses \(\ell\). Choosing the roughness cap after an
independent numerical-QP bank bound makes these inequalities noncircular.

The exact positive interface is unchanged: construct, at total numerical-QP
cost, a public numerical-QP list \(A_j\) satisfying

\[
0<|A_j|<N/2
\]

and covering every surviving local-order prime. Then the absolute values are
P163-admissible one-bit-smaller children. Merely constructing a huge
supported integer and centering it does not prove this interface. A positive
route needs an \((N,w)\)-correlated quotient/carry theorem, a separate
support-preserving size-localization theorem, a non-Euclidean selector, or a
direct factor/common-order transition.

The V2 statement, proof, hostile re-audit, and blind reconstruction have
SHA-256 hashes
4666ed13b2318932a357c5a35ef4021c83355bf78cfeab3ffa1eb7bd6c8ac9ce,
807d7c7e30ec7950e083bd9624050a1859fe724ce74843bcb16b64f3b184ca39,
32abdb240acaa89152ce8f032931fe580fa6b6a963c270c693a2efec87cd7e0c,
and
53176bf7629e24ef748986fd41188981cbaf7617e374a3bad84d244d19fdfedb.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P166 — segment Jacobi zero is a sufficient but still unevaluated QP primitive

**Status:** promoted from F189 after hostile audit and an independent
statement-only reconstruction. This is a conditional splitter plus exact
boundaries for named representations. It does not construct the required
segment-zero evaluator.

For every odd \(N\),

\[
z_N(x)=1-\left(\frac{x}{N}\right)^2
=\mathbf 1_{\gcd(x,N)>1}.
\]

The exact totalized floor reciprocity identity is

\[
\sum_{i=1}^{(N-1)/2}\left\lfloor\frac{ix}{N}\right\rfloor
+
\sum_{j=1}^{(x-1)/2}\left\lfloor\frac{jN}{x}\right\rfloor
=\frac{(x-1)(N-1)}4+\frac{\gcd(x,N)-1}{2}.
\]

Thus ordinary reciprocity compresses the sign, but its only nonunit
correction is the hidden gcd term itself. A QP oracle that decides whether a
length-\(L<N\) interval contains a Jacobi zero would isolate one proper factor
with one retained child per binary-search level. On a balanced semiprime,
the affine pool \(U+tV\), at a public length \(T=\Theta(\sqrt N)\), contains
a useful local zero with probability greater than \(1/40\). Therefore that
oracle would give a classical Las Vegas QP splitter on the balanced promise.

The exact zero mask has least period and full Fourier support
\(\operatorname{rad}(N)\), hence the same order for a materialized linear
recurrence and deterministic residue automaton. For \(N=pq\), its puncture
correction already has recurrence order \(p+q-1\). The rising-factorial
identity turns interval zero into a carry in the unknown bases \(p\) or
\(q\), not into a public evaluation algorithm. These facts close dense
Fourier/recurrence, explicit-state, ordinary Jacobi-reciprocity, and literal
hidden-base Kummer implementations only. They do not lower-bound succinct
arithmetic circuits, implicit determinants, nonlinear integer-register
algorithms, or new gcd-based evaluation.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`2e7c4df447013db2e5ebc5d51045eec0abff3a36f1bf59760d74ae31f4adbfc1`,
`ced9a963f902541836a1214a2d7afea4616ae53d7360b26c4d47e3434247c03e`,
`a8e85f3fd7a2d98e4579a8c926db6488defcfa14ffa1f86b7accf1e4cb38e878`,
and
`a6959cad63a8cee6e452f79bddc6347aef92322ba56a21e31f8f5781317236ea`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P167 — QP retained-source Paley words leave one high-order decomposition gate

**Status:** promoted from F190 after hostile audit and an independent
statement-only reconstruction. This is a collection of exact named-model
boundaries. It is not a factoring algorithm and not a lower bound against
arbitrary processing of a retained full word.

For a squarefree balanced semiprime \(N=pq\), the complete Jacobi sequence
has exactly

\[
\varphi(N)=(p-1)(q-1)=2^{\Theta(n)}
\]

nonzero Fourier modes, minimal constant-coefficient recurrence order, and
periodic Hankel rank. Its complete autocorrelation is factor-sensitive only
when the public shift difference already exposes the same factor by a gcd.
Consequently dense Fourier, Prony, Padé, Hankel, and raw complete-correlation
routes remain exponential after polynomial resources are enlarged to QP.

For \(m=(\log n)^{O(1)}\) punctures, every row-only exact Hadamard-product
word has \(2^{n-o(n)}\) local decompositions. Directly shrinking this entropy
to QP requires \(m=n-(\log n)^{O(1)}\), where enumerating all sign splits is
exponential. This does not apply after the numerical source is retained.
Indeed, \(O(n)\) well-chosen columns can give the local Paley code constant
relative distance. Information theory therefore does not close the
long-word regime.

QP many independent coordinate collisions and QP many bounded-degree
fresh-source equality tests occur with probability only
\(2^{-n/2+o(n)}\). Explicit low-order shifted-character expansions retain
the same negligible drift. The exact surviving interface is a source-aware,
high-order, modulus-blind decomposition of a retained Hadamard--Paley product
word that produces a verifiable zero divisor without materializing the
exponential local objects. A decoder whose specification already requires a
numerical hidden prime with inverse-QP probability is QP-equivalent to the
original factoring task.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`78e8cfd74e5ed824e6bb74c3aacbef0e9af6c67746373aa6e478a77ed9930b38`,
`03a3a80387d43fd9a89e5c5453ac36af7c1dd09133f7029b419cdeacc4dd41bb`,
`635c80c3126a24c2f10aeb9bb108dacee1a8a66088bf63d939aa88a400e52660`,
and
`a79bd4123d2c1be569d94ab196390c7ade597c69d730c4b5be1d470c00e58c6a`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.


## P163 — sequential support peeling reduces synchronized extinction to one recursive child

**Status:** promoted from F186 after hostile audit and independent
statement-only reconstruction. This strengthens the recursive interface of
P162. It is not an all-input factoring algorithm.

Let \(w\) be a public unit whose order in every hidden prime-power component
is nontrivial, coprime to \(N\), and \(T\)-rough. Suppose a public QP list

\[
A_1,\ldots,A_B
\]

covers the rational-prime support of every local order, and every nonunit
entry has at most \(n-1\) bits.

Set \(v_0=w\). Process the entries in public order by

\[
v_i=v_{i-1}^{A_i^n}\bmod N,
\qquad
H_i=\gcd(v_i-1,N),
\]

after first screening \(\gcd(A_i,N)\). A proper gcd factors \(N\). If
\(H_i=1\), retain \(v_i\) and continue. Prime-support coverage and the
bound on primary exponents below \(N<2^n\) force a global return by the end
of the list.

At the first index with \(H_i=N\), every local order of the current element
\(v_{i-1}\) is nontrivial and divides the single power \(A_i^n\). Therefore
only \(A_i\) must be recursively factored. Factor-first stripping from the
fully factored annihilator \(A_i^n\) returns a proper factor or one fully
factored exact common local order above \(T\).

This gives at most one recursive child of at most \(n-1\) bits. For a
nondecreasing numerical-QP local bound \(Q\),

\[
\mathcal T(n)
\le \mathcal T(n-1)+Q(n)
\le nQ(n)
=2^{(\log n)^{O(1)}}.
\]

Thus the relevant invariant is QP recursion-tree volume. A fixed-ratio
contraction is not required for a single strictly descending chain.

Applied to the P162 double-extinction branch, take the cross-resultants as
the ordered support-covering list. Their exact bound need only satisfy

\[
K\left(1+K\left\lceil\log_2(2L+2)\right\rceil\right)
\le n-1,
\]

rather than a fixed \(\rho n\) contraction. Sequential peeling resolves
double extinction with one recursive child. The output remains a factor, a
fully factored exact common order above \(T\), or one wide-shift-hard rough
descendant. The last branch remains unresolved.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`a23b980441b75afc10dd21e82582be5a53afa1c3da0555cf71a91feb2110bacc`,
`4926909c50b13f3d64865dab6e90ff2bfc619612c5f46502feccfb9c44dedf6e`,
`e5c2390395daa0b8c738adedbe3ab3b334b5c80a59b61037f10d7c2fb8ac0473`,
and
`f618b8d76728c25e4b737907d5640008a307367865c82da04d757dea0dbe5798`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P164 — root counting forces QP-wide long actions on every surviving order prime

**Status:** promoted from F184 V2 after a fresh hostile re-audit and a strict
statement-only reconstruction. This is a deterministic postprocessor for the
P161 rough-order branch. It is not an all-input factoring algorithm.

Let \(w_0\) be a public unit whose order in every hidden prime-power
component is nontrivial, coprime to \(N\), and \(T\)-rough. Choose arbitrary
fixed integer-valued numerical-QP bounds \(K(n),M(n)\ge1\), put

\[
D=1+\frac{K(K+1)}2,
\]

and choose the P161 roughness cap so that

\[
T>1+M(D+1).
\]

At stage \(t\), test the \(D+1\) consecutive bases

\[
\mathcal I_t=
\{2+t(D+1),\ldots,1+(t+1)(D+1)\}.
\]

For \(a\in\mathcal I_t\), define

\[
C_a=a\prod_{k=1}^K(a^k-1),
\qquad
z_{t,a}=w_t^{C_a^n}\bmod N,
\qquad
H_{t,a}=\gcd(z_{t,a}-1,N).
\]

A proper \(H_{t,a}\) factors \(N\). Otherwise, at least one candidate has
\(H_{t,a}=1\). Indeed,

\[
F_K(X)=X\prod_{k=1}^K(X^k-1)
\]

is monic of degree \(D\). If all \(D+1\) candidates extinguished one
nontrivial current order prime \(\ell>T\), then they would be \(D+1\)
distinct roots of \(F_K\) modulo \(\ell\), which is impossible. Retain the
first gcd-one candidate and repeat for \(M\) stages.

On the no-factor branch, the final local orders remain nontrivial, coprime
to \(N\), and \(T\)-rough. Every prime \(\ell\) in every final local order
satisfies, for all selected public bases \(a_0,\ldots,a_{M-1}\),

\[
\ell\nmid a_t,
\qquad
\operatorname{ord}_\ell(a_t)>K.
\]

The bases are distinct. Complete primary deletion by \(C_a^n\), and the
identity gcd, are exact for arbitrary hidden prime powers because the local
orders are coprime to the hidden rational primes. All candidate counts,
integer bit lengths, modular powers, and gcds are numerical QP.

P164 supplies simultaneous long action under a QP-wide adaptive public
base bank. It does not prove that the actions generate independent
directions. They may lie in one large cyclic subgroup, so no factor or exact
common order follows in the surviving branch.

The V2 statement, reused proof, fresh hostile re-audit, and fresh blind
reconstruction have SHA-256 hashes
`cf14b7ad25ecb9092419deaddca08327bcfe43d4bc9e35f89923a4f7e45f1632`,
`52c4c1ba6410241db7e03d739ee973af3b918d0a422999f1b6b67d6aec0c8c72`,
`fa9b9cf22098d59a18334f0c8b8ca8bdc267323cafc57567b7042ed1a4fa6278`,
and
`aec36c26d664261abd71f2bb92c2a44b55392d796f11d000ed2d49c8556e8f83`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P165 — fully factoring \(N-1\) does not make uniform-base return likely

**Status:** promoted from F187 after hostile audit and an independent
statement-only reconstruction. This is a theorem about one restricted
Pocklington/Lucas sampling route. It is not a factoring algorithm or a
lower bound against adaptive base selection.

Let

\[
N=\prod_{i=1}^{s}p_i^{e_i},\qquad m=N-1,
\qquad h_i=p_i^{e_i-1}(p_i-1),
\qquad d_i=\gcd(m,p_i-1).
\]

Assume the complete factorization of \(m\) is known. For a unit \(a\), the
initial gcd \(\gcd(a^m-1,N)\) gives exactly one of a proper factor, complete
nonreturn, or global return. In the global-return case, factor-first stripping
over the known prime factors of \(m\) either factors \(N\) or certifies one
fully factored exact order common to every hidden prime-power component.
Reduction modulo \(p_i\) is injective on this \(m\)-torsion, so the claim is
valid for repeated prime powers and not only squarefree inputs.

For a uniform unit, put

\[
\beta_i=1-\frac{d_i}{p_i-1},\qquad
\gamma_i=\frac{d_i}{h_i},\qquad
D=\gcd_i d_i.
\]

Then

\[
\Pr(G_0=1)=\prod_i\beta_i,
\qquad
\Pr(G_0=N)=\prod_i\gamma_i,
\]

and, conditional on global return, stripping does not factor with exact
probability

\[
\frac{\sum_{r\mid D}\varphi(r)^s}{\prod_i d_i}.
\]

For a squarefree semiprime \(N=pq\), let
\(d=\gcd(p-1,q-1)\). Starting from common-order state one, the exact
probability of a proper factor or strict common-order growth is

\[
\frac d{p-1}+\frac d{q-1}
-\frac{d^2+1}{(p-1)(q-1)}.
\]

On any bounded-gap prime pair, \(d\mid q-p\), so every synchronized order
and their accumulated lcm stay bounded. The success probability per uniform
base is \(O(1/p)=2^{-n/2+O(1)}\). The proved bounded-prime-gap theorem gives
infinitely many such balanced pairs. A numerical-QP bank therefore still
succeeds with probability only \(2^{-\Omega(n)}\). Fully factoring
\((N-1)/2\) removes hidden order ambiguity after a return, but it does not
make return likely.

The recursive factorization of \((N-1)/2\) is one child with at least one
bit of contraction. If it is the only recursive child, its cost satisfies

\[
T(n)\le T(n-1)+\operatorname{QP}(n)=\operatorname{QP}(n).
\]

This does not account for also recursively completing both children after a
later factor split. P165 closes only independent uniform-base sampling after
the one-child preprocessing. Deterministic bases, adaptive bases, other
exponent families, and complete factorization remain open.

The statement, proof, hostile audit, and blind reconstruction have SHA-256
hashes
`9434188bf8c35cbd54d0f6f553b7e0698f19470745515bb1fe503fbe8b67f14e`,
`0f3790117a8e6ed34fbdaa934b576cbdec2ef248865ef9c5268aeb262f77f7cb`,
`ab4a15edfa10342460f3dc7ab1b258af8cf8705f1a8139947414a7cd013f070a`,
and
`def51ce9e6e31451ecbe546f50a90e8a48a79c4d9d6278de609e193efe8241e5`.
No computation, cross-family audit, human audit, or publication-level
literature review has run.

## P221 — explicit divisor covers have linear prime mass, independent of additive rank

**Status:** promoted from corrected F272 V2 after a fresh hostile audit and
an independent statement-only reconstruction. This is an obstruction to
explicit covers and explicit prefactor output. It is not an integer-factoring
algorithm or a lower bound for succinct modular evaluators.

Fix \(X\ge2\). For finite \(S,T\subset\mathbb Z\), discard zero differences
and let

\[
D=\{|s-t|:s\in S,t\in T,s\ne t\},\qquad M=|D|,
\]

with maximum binary length \(L\). Suppose every \(m\le X\) divides at
least one \(d\in D\). Then every prime \(p\le X\) divides at least one
difference, and the product of the distinct such primes supported by one
difference divides that difference. Consequently

\[
\vartheta_2(X)
\le \sum_{d\in D}\log_2 d
<ML
\le |S||T|L.
\]

Since \(\vartheta_2(X)=\Theta(X)\), the cardinalities of \(S,T\) and the
expanded bit lengths of all differences cannot all be quasipolynomial in
\(\log X\). This proof does not use arithmetic-progression or generalized-
progression rank. It also covers multisets after passing to their supports;
signs and duplicate differences do not change coverage.

There is a second, representation-independent obstruction when every
difference is explicitly prefactored. Let \(K\) be the number of nonzero
ordered pairs. If each complete factorization writes at most
\(F_{\rm out}\) bits, then

\[
KF_{\rm out}\ge\vartheta_2(X).
\]

On any fixed bit machine the corresponding time statement is
\(KF_{\rm time}=\Omega(X)\). Shared dictionaries must be charged for the
binary prime names they materialize. Thus succinct descriptions of huge
differences do not rescue *explicit* prefactor output.

For a fixed prime band \([a\sqrt X,b\sqrt X]\), if \(v\) primes lie in the
band and one difference contains at most \(h\) of them, pair coverage gives

\[
\binom{v}{2}\le M\binom{h}{2}.
\]

Under the Umans--Wang scaling

\[
|S|,|T|\le X^{\beta+o(1)},\qquad
\log\max(S\cup T)\le X^{\alpha+o(1)},
\]

the necessary inequalities are

\[
\alpha+2\beta\ge1,\qquad \alpha+\beta\ge\tfrac12.
\]

If explicit factor output costs \(X^{\gamma+o(1)}\) per difference, also
\(\gamma+2\beta\ge1\). At \((\alpha,\beta)=(1/3,1/3)\), only the first
inequality is saturated; the pair-incidence inequality has slack. These
conditions neither construct nor refute a higher-rank cover at that scale,
and even such a cover would give an exponential \(N^{1/6+o(1)}\) factoring
algorithm rather than a quasipolynomial one.

A static prime-separating family has the analogous mass boundary. Distinct
prime divisibility codewords require \(m\ge\lceil\log_2\pi(X)\rceil\), and
explicit factorizations of its \(m\) values satisfy

\[
mF_{\rm out}\ge\vartheta_2(X)-\log_2X.
\]

P221 leaves compressed and adaptive mechanisms open. In particular, a
uniform evaluator

\[
(a,b,d)\longmapsto\prod_{j=a}^{b}j\pmod d
\]

in quasipolynomial time in \(\log b+\log d\) is a sufficient, factoring-hard
interface: compute the product of \([1,\lfloor\sqrt N\rfloor]\) modulo \(N\),
then follow one binary interval path using gcds until a proper divisor
appears. The path cannot end at a singleton because no integer below \(N\)
is divisible by \(N\). P221 neither constructs this evaluator nor proves it
is the unique possible escape or factoring-equivalent.

The corrected statement, proof, hostile audit, and strict statement-only
reconstruction have SHA-256 hashes
`1b6c52624e5f957b2814f5e3e98572612e7cf9312b167ed117e01dddf0d4abb5`,
`671c6810a753791fa7c08e3c8eec89b68a0b9fa64fc129d7263130a2b19b67d8`,
`8daf9b037a2e310100251b6dda4765ead8d1a4b9560d708f17d2fe3fab72a772`,
and
`84cd09d97e21f4722bc4749233b08507d6470f50abffabd86b0db133080951f0`.
The V1 blind failure remains preserved. No research computation,
cross-family audit, or human audit ran.

## P222 — batch gcd-free P66 decoding has no quadratic pair-arithmetic step

**Status:** promoted from corrected F271 V2 after a fresh hostile audit and
an independent reconstruction from the authenticated base and additive V2
statements. This is a deterministic decoder theorem. It does not construct a
square relation or factor an integer.

Let \(N\ge3\) be odd. The input consists of positive integers
\(a_1,\ldots,a_m\) and canonical unit residues \(0\le v_i<N\) with

\[
v_i^2\equiv a_i\pmod N.
\]

For \(u,v>1\), define the factor-free saturation

\[
\operatorname{Sat}(u;v)
=\gcd\!\left(u,v^{\operatorname{bitlen}(u)}\bmod u\right).
\]

Prime by prime, this contains the complete primary part of \(u\) supported
on \(v\). Subtractive equal-support refinement, followed by incremental
insertion through a balanced product tree, therefore constructs pairwise
coprime opaque blocks \(q_1,\ldots,q_S\) and exact exponents \(e_{ji}\) such
that

\[
a_i=\prod_{j=1}^{S}q_j^{e_{ji}}
\]

without rational-prime factorization. If \(T\) old blocks are touched,
\(E\) equal-support recursion nodes occur, and the fixed tree has depth
\(D\), the complete refinement plus independent terminal-coprimality check
uses at most

\[
\boxed{(D+1)T+m+2E+S}
\]

scalar gcd calls. The valuation telescope gives \(T\le I\), \(E\le V\),
and \(S\le I\), for the proof measures

\[
I=\sum_i\omega(a_i),
\qquad
V=\sum_p\sum_i v_p(a_i).
\]

Pairwise coprimality is verified with one product/remainder tree and exactly
\(S\) terminal gcds. The empty-block case performs no tree operation; with
\(\delta_S=\max(S-1,0)\), its exact tree terms are

\[
[S+\delta_S]M(2R)+2\delta_S Q(2R)+S Q(2r)+S G(r).
\]

There is also no arithmetic scan over support-two row pairs. Form the binary
parity matrix from the nonsquare blocks and let \(\sigma_i\) be column \(i\).
Singleton relations are exactly the zero columns. Support-two relations are
exactly pairs of equal columns. Zero-column unit vectors and one star inside
each nonzero equal-signature class form a basis of their complete span.
Reducing a canonical kernel basis against this low basis gives a direct
structural complement.

For every kernel vector, the coprime-block exponents give its exact positive
integer root. Dividing by the product of the supplied modular roots defines
a homomorphism into the roots of one modulo \(N\). It is therefore complete
to classify a basis of the low span and its complement: at most \(m\) root
checks, \(m\) inversions, and \(2m\) signed gcds. These signed gcds are
separate from the displayed refinement call count.

With schoolbook arithmetic, the refinement, reconstruction, and terminal
verification use \(O(R^3\log R)\) bit operations, and the complete decoder
has the conservative bound

\[
O\!\left((R+\operatorname{bitlen}N)^4\right).
\]

The canonical-residue input clause is essential to this encoding bound.

For the intended F265 residual domain \(m\le64\) and row bit length at most
361, the exact primorial certificates give

\[
T\le3591,
\qquad E\le23040,
\qquad S\le1875,
\qquad D=11.
\]

Hence the refinement and terminal check use at most

\[
\boxed{91{,}111}
\]

scalar gcd calls per bank and \(69{,}973{,}248\) across 768 maximum banks.
This is about 103.02 times smaller than the abandoned F265-D08 fixed-call
envelope. It is a call-count comparison, not a runtime projection.

P222 keeps two peeling semantics distinct. D05 positive-support privacy can
be read from the exact exponent matrix after refinement. P106
parity-degree-one peeling is stronger and remains kernel-safe, but it is not
the same rule. A future experiment must choose one and keep its counters
separate.

The theorem proves no elliptic source law, residual-core bound, nonzero
kernel, non-global normalized root, or factoring result. It only makes a
previously infeasible exact decoder a credible preflight target.

The base statement, V2 statement, base proof, V2 proof, frozen V2 root,
hostile audit, and strict two-statement reconstruction have SHA-256 hashes
`19b288038c4f9e339d3f56e51fb1c6d7277fd9e322e486f2339edd0c68bf64ba`,
`29fd1a79e569c2e4da72d3489e7385de4123e6b299241bfe46defb421c84b82c`,
`f65e65cd649d3e787fc452abf270142e9c790d424328c52b6e3d678fc7e77b24`,
`5371d049eecb2451f073edb96d5bf36f99ab7be662fb48c5d8de2b2d93f10b51`,
`5e396f4e20f54ee37ed70b19ed85a82e483247b10423a7ce58e7081e961c7a15`,
`5827e5a5a80a052b486259a7994b69f00c18b0a3e07a91fc0038dd1e08f9acec`,
and
`21c8784eb36fb477cad4944df7216c6897151ab1fa4608a6c9dbb3f2f90c78f1`.
No research computation, remote run, cross-family audit, or human audit ran.
## P223 — named interval-product grammars retain a product gate or literal exponential closure

**Status:** promoted from corrected F273 V2 after a fresh hostile audit and
an independent statement-only reconstruction. This is a boundary for four
explicit symbolic grammars. It is not a lower bound for general arithmetic
circuits or for a uniform succinct interval-product evaluator.

First, let \(A\) be an integral domain and

\[
R=A[e_0,o_0,z_1,\ldots,z_r],
\]

where the displayed coordinates are algebraically independent. If
\(F\in R\) vanishes identically when \(e_0=0\), then \(e_0\mid F\). If it
vanishes on both child-product axes, then

\[
\boxed{e_0o_0\mid F}.
\]

For a rational observable \(G/H\), the same numerator conclusion holds only
when the denominator remains defined and nonzero on both generic axes. Thus
a division-free orientation selector retains the selected child product,
and an orientation-blind zero observable retains the parent product. This
does not apply after imposing affine, characteristic-specific, or
row-specific relations among the other coordinates.

The corresponding formal leaf bound is exact. If \(M\) algebraically
independent leaves enter an expression only through \(K\) summaries, each
depending on at most \(q_0\) leaves, and the expression equals their complete
product, then

\[
Kq_0\ge M.
\]

Second, let an integer \(m\)-square matrix have rank \(m-1\) modulo \(p\)
and full rank modulo \(q\), where \(N=pq\). If \(\Delta_k\) is the gcd of
its \(k\)-minors and \(d_k=\Delta_k/\Delta_{k-1}\), then

\[
\gcd(\Delta_k,N)=1\quad(k<m),
\qquad
\gcd(\Delta_m,N)=\gcd(d_m,N)=p.
\]

For \(A_B=\operatorname{diag}(1,\ldots,B)\), with
\(B=\lfloor\sqrt N\rfloor\) on the balanced semiprime promise,

\[
\Delta_B=B!,
\qquad
\Delta_{B-1}=\frac{B!}{\operatorname{lcm}(1,\ldots,B)},
\qquad
d_B=\operatorname{lcm}(1,\ldots,B).
\]

Both terminal values have gcd \(p\) with \(N\). The determinant is the
factorial gate; the last Smith invariant is a distinct lcm gate. P223 gives
no reduction or quasipolynomial evaluator between them.

Third, for the rising factorial

\[
P_m(X)=\prod_{j=1}^{m}(X+j),
\]

its unsigned derivative resultant is

\[
\boxed{
D_m=|\operatorname{Res}(P_m,P_m')|
=\prod_{d=1}^{m-1}d^{2(m-d)}
=\left(\prod_{k=1}^{m-1}k!\right)^2.}
\]

Moreover, \(D_{m+1}/D_m=(m!)^2\), its bit length is
\(\Theta(m^2\log(m+1))\), and after the preliminary
\(\gcd(B,N)\) screen the unresolved balanced branch satisfies

\[
\gcd(D_B,N)=p.
\]

The full discriminant is therefore a valid factor-bearing weighted product,
not a fast evaluator.

Fourth, define

\[
R_c(m)=\operatorname{Res}(P_{0,m},P_{cm,m}).
\]

Literal dyadic splitting gives

\[
R_c(2m)=R_{2c-1}(m)R_{2c}(m)^2R_{2c+1}(m).
\]

Starting from \(R_1(2^tq_0)\), the base frontier contains exactly
\(2^{t+1}-1\) offsets, while the complete memoized DAG keyed by length and
offset has exactly

\[
\boxed{2^{t+2}-t-3}
\]

cross-resultant states. With \(S(k)=\prod_{r=1}^{k-1}r!\), the alternative
closed form is

\[
R_c(m)=\frac{S((c+1)m)S((c-1)m)}{S(cm)^2},
\qquad
D_m=S(m)^2.
\]

This is an integer identity and does not authorize modular inversion at a
zero divisor. Treating remote \(S\)-values as primitive merely names the
factor-bearing weighted product, since \(\gcd(S(B),N)=p\) on the unresolved
balanced branch. For remote length \(M=2^{\Theta(n)}\) and
\(q_0=\operatorname{QP}(n)\), the literal state count is
\(\Theta(M/q_0)=2^{\Theta(n)}\).

P223 closes only these named grammars. It says nothing about a special
affine transition, characteristic-dependent identity, nonlinear
Archimedean operation, adaptive algorithm, succinct matrix algorithm, or
general arithmetic circuit. In particular, the factoring-hard uniform
interval-product evaluator left open by P221 remains open.

The corrected statement, proof, frozen V2 root, hostile audit, and strict
statement-only reconstruction have SHA-256 hashes
`95cf55e02dd02322de2c78f95dfa6ddecae7c783fd152f7c00a64de511bf96b4`,
`a91f2cdf97c26ac95010594383a299c3450527b98c8219638bef02d98ce28d99`,
`68cfb6e2d7c15563f9cb953b3233421746c62bfe9ee8ed6b04ee996530f62a94`,
`9159c285282f1cec1a297089906d0f4b32682e0f4c4925686ef0a047727fcb6a`,
and
`e266f1fe6d42cede0854f644cab30171c1e32e7acfbe8f2e15edfa12f3755574`.
The V1 hostile PASS and strict-blind failure remain preserved. No research
computation, remote run, cross-family audit, or human audit ran.

## P224 — the characteristic-shift threshold needs the full regular state, while polynomial differences and rational gauges retain named product gates

**Status:** promoted from F274 after a fresh hostile audit and a strict
statement-only reconstruction. This is a boundary for the displayed
regular-shift, integer-polynomial-difference, and rational-gauge mechanisms.
It is not a lower bound for every low-dimensional invariant, nonlinear or
semilinear state, implicit representation, determinant-one cocycle, adaptive
algorithm, or interval-product evaluator.

For a prime \(r\), let \(V_r\) be the \(r\)-dimensional space of functions
\(\mathbb F_r\to\mathbb F_r\), let \(T_rf(x)=f(x+1)\), and put
\(\Delta_r=T_r-I\). The regular shift is one \(r\)-cycle, so

\[
 \mu_{T_r}(Z)=Z^r-1=(Z-1)^r,
 \qquad
 \mu_{\Delta_r}(Z)=Z^r.
\]

Hence \(\Delta_r^k=0\) exactly when \(k\ge r\). On a balanced semiprime
\(N=pq\), with \(B=\lfloor\sqrt N\rfloor\), this gives the exact full-state
separator

\[
 \Delta_p^B=0,
 \qquad
 \Delta_q^B\ne0.
\]

But every \(d_r\)-dimensional \(T_r\)-stable subspace, quotient, or
subquotient has induced difference nilpotent of index at most \(d_r\). Thus
if both local dimensions are at most \(d\le B\), then the \(B\)-th difference
is zero in both CRT components. In particular, an explicitly stored
numerical-QP-dimensional regular-shift subquotient loses this specific
nilpotency asymmetry for all sufficiently large balanced inputs. This says
nothing about another invariant of the same state or a succinct state that
does not enumerate a basis.

For the ordinary forward difference \(\delta F(X)=F(X+1)-F(X)\), every
\(F\in\mathbb Z[X]\), integer \(a\), and \(k\ge0\) satisfy

\[
 \delta^kF(a)\in k!\mathbb Z,
 \qquad
 \delta^kX^k\big|_{X=0}=k!.
\]

The exact quotient is an integer combination of Stirling numbers. Therefore
an entrywise integer-polynomial probe at \(k=B\) retains \(B!\) as a common
factor. Dividing by \(B!\) either removes the universal signal through exact
integer evaluation or asks for an invalid inverse of a zero divisor modulo
\(N\). This is a divisibility identity, not an evaluator lower bound, and it
does not cover integer-valued rational polynomials such as
\(\binom{X}{B}\).

Finally, a rational scalar cocycle \(R\in\mathbb Q(X)^*\) has a shift gauge

\[
 R(X)=\frac{h(X+1)}{h(X)}
\]

exactly when \(R(X)\to1\) at infinity and the total valuation of \(R\) is
zero on every integer-translation orbit of irreducible polynomials. In that
case its interval product telescopes to \(h(X+m)/h(X)\); otherwise no rational
gauge exists. A rational matrix gauge must satisfy the same condition on its
determinant. An uncancelled rising affine determinant is therefore obstructed,
while determinant-one systems remain completely open to other invariants.
Every modular telescope also requires an explicit denominator-unit audit.

The practical search conclusion is scoped methodology: do not run a larger
search confined to these exact mechanisms. A materially new candidate must
exhibit a nonlinear or semilinear state, an implicit regular representation,
a determinant-one non-determinant invariant with a QP endpoint evaluator, or
another characteristic-dependent construction outside the hypotheses. The
reviews explicitly reject reading this recommendation as an exhaustive
no-search theorem.

The statement, proof, frozen root, hostile audit, and strict statement-only
reconstruction have SHA-256 hashes
`22674281efe2fc593ef8b657bc4782f1892e118a2a193c6f5028d514a245ce47`,
`0077b4d4bea0ceed8d4771b78d02a48f67b446af7358a86273145f3215866d0b`,
`b7a307fcc0aa0f818e250775499d355fd07396da22bebb4f74e1f5e5b5ebab86`,
`9bc97d0d1cb36b0801e335f3f4506dba74785e23b9419ac49b4ef802ec5b7f52`,
and
`e890d571c53e85088881e088eaf616c1f2933a8a3105c95d53bec922a17e84d3`.
No research computation, remote run, cross-family audit, or human audit ran.

## P225 — inherited monomial rows pull back to the old square-class kernel, and inverse-square even cycles expose only a direct label gcd

**Status:** promoted from corrected F275 V2 after a fresh hostile audit and a
strict reconstruction from the authenticated V1 and V2 statements. This is a
source-boundary theorem, not a factoring algorithm or a rank theorem for
canonically reduced rows.

Let positive unit rows \(a_i\) have public unit roots \(x_i\bmod N\). For
nonnegative integers \(M_{ji}\), positive integers \(s_j\), and signs
\(\varepsilon_j\), form exact inherited monomial rows

\[
 A_j=s_j^2\prod_i a_i^{M_{ji}},
 \qquad
 X_j\equiv \varepsilon_js_j\prod_i x_i^{M_{ji}}\pmod N.
\]

If a parity vector \(c\) makes \(\prod_jA_j^{c_j}\) an exact integer square,
put \(d=M^Tc\bmod2\). Then \(d\) is an exact square-class relation among the
old rows, and the normalized roots satisfy

\[
 \boxed{\rho_A(c)=\left(\prod_j\varepsilon_j^{c_j}\right)\rho_a(d)\pmod N.}
\]

Thus an inherited monomial transformation cannot create a normalized-root
class outside the image of the old square-class kernel. In particular,
relations in the structural incidence kernel \(M^Tc=0\) have global root
\(\pm1\). This does not say that every transformed relation is global: a
useful old arithmetic relation can be retained. If an independently supplied
root differs from the inherited one, their signed comparison either factors
\(N\) immediately or proves that they differ only by a global sign.

For graph rows \(A_e=d_ud_v\) with public roots \(y_e\), every Eulerian edge
set is an exact square. On a simple even cycle, define

\[
 P_0=\prod_{i\ {m even}}y_{e_i},
 \qquad
 P_1=\prod_{i\ {m odd}}y_{e_i}.
\]

If \(R=\prod_i d_{v_i}\) is the positive exact root and
\(X=P_0P_1\) is the supplied cycle root, then

\[
 RX^{-1}\equiv P_0P_1^{-1}\equiv P_1P_0^{-1}\pmod N,
\]

and, exactly,

\[
 \gcd(R-X,N)=\gcd(P_0-P_1,N),
 \qquad
 \gcd(R+X,N)=\gcd(P_0+P_1,N).
\]

Therefore a useful explicit inverse-square even cycle is already exposed by
the alternating public-label gcds; otherwise its guaranteed graph relation is
global. The corrected factor-blind construction

\[
 T_y(d)=[y^2d^{-1}]_N,
 \qquad A=dT_y(d)
\]

uses a canonical carrier \(1\le d<N\), so
\(1\le A\le(N-1)^2<N^2\). General graph carriers need not be canonical; the
cycle theorem does not use that size bound.

Canonical reduction is an explicit exclusion. The unreduced complement
product \(U_E(a)U_E(N-a)\) is inherited and covered, but

\[
 C_E(a)=[(a(N-a))^E]_{N^2}
\]

differs from it by an additive multiple of \(N^2\). Reduction can destroy all
rational-prime support inherited from the operands, so P225 proves neither a
private-pivot law nor a failure law for that reduced section. The F270
cross-family union likewise recomputes arithmetic sharing and is not an
inherited-incidence decoy.

The corrected V2 statement, proof, frozen root, hostile audit, and strict
two-statement reconstruction have SHA-256 hashes
`a9bd86b4e4515f133c3c2d7711c530d334749675e0aa75eb8bc7547f3ad0f0da`,
`9c0ec169e6402114a0546fca5506985ff6cec6250f7f5cc73081aa946063623f`,
`fb8e508c100bc81cf1105ba7be09162df7d73eb7a5ef704b3a687b3567b1a372`,
`547a6bc2c1d073a6aaa6d6d93e105395558f70dfdb433987c139d6efcb73ffdb`,
and
`ebbc02fe85324441a6a176fd9ee703f7041999b87c28a3535d619bb23ae8e526`.
The V1 hostile size-bound failure and the first incomplete blind attempt are
preserved and are not verification evidence. No computation or remote run
occurred.

## P226 — rational endpoint matrix laws are gauges, while affine determinant-one transfers reduce to a constant-power lane or an unresolved continuant

**Status:** promoted from corrected F276 V2 after fresh hostile and strict
statement-only audits. This is a boundary for named matrix-transfer
mechanisms. It is not a lower bound for determinant-one systems and does not
factor an input.

If a rational matrix interval law satisfies

\[
 P(Y,Z)P(X,Y)=P(X,Z),
 \qquad P(X,X)=I,
\]

then for some rational matrix \(G\),

\[
 \boxed{P(X,Y)=G(Y)G(X)^{-1}.}
\]

Thus every rational two-endpoint composition law is a gauge telescope. More
generally, a separable length state

\[
 P(x,y)=G(y)H_{y-x}G(x)^{-1},
 \qquad H_{r+s}=H_sH_r
\]

has \(H_m=C^m\). In determinant one, \(\det C=1\) and \(\det G\) is
constant. This is a constant-matrix-power problem after a rational gauge, and
every modular denominator still needs a unit audit.

Two exact structural obstructions accompany the gauge law. A polynomial
unimodular moving-frame line in \(\operatorname{SL}_d(R)\), for
\(R=K[X]\) or \(\mathbb Z[X]\), can carry only a unit scalar multiplier;
over \(\mathbb Z[X]\) that multiplier is \(\pm1\). Also every unimodular
matrix preserves the ideal generated by a state's coordinates. Hence a
whole-state or whole-column gcd signal is global, although one selected
coordinate can still contain a factor while another retains a unit.

Every affine transition

\[
 A(X)=C+XD\in\operatorname{SL}_2(\mathbb Z[X])
\]

has

\[
 A(X)=C(I+XB_0),
 \qquad B_0=C^{-1}D,
 \qquad \operatorname{tr}B_0=\det B_0=0,
 \qquad B_0^2=0.
\]

For \(D\ne0\), a constant rational basis puts \(B_0=E_{12}\). If the
conjugated constant matrix is
\(\widetilde C=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\), then the
second coordinate of
\(z_{k+1}=\widetilde C(I+kE_{12})z_k\) obeys

\[
 \boxed{y_{k+2}=(ck+a+c+d)y_{k+1}-y_k.}
\]

When \(c=0\), the step reduces to constant powers and
geometric-weighted polynomial sums. P226 supplies no universal signal
failure for that lane; a constant matrix with its own exact asymmetric law
remains a separate candidate. When \(c\ne0\), the exact normal form is a
variable-coefficient continuant. A holonomic recurrence certificate alone
does not evaluate its remote term in numerical quasipolynomial time, but no
lower bound or failure law is proved.

The rational factorial lift gives a real factor signal only by pairing
\(B!\) with a reciprocal that becomes undefined at the hidden prime. A
constant Jordan block contains the genuine entry \(\binom{B}{\lfloor
B/2\rfloor}\), whose gcd is the smaller hidden prime, but its explicit state
has exponential dimension and an implicit entry request is the same remote
binomial evaluator gate. These are controls, not algorithms.

The V2 statement, proof, frozen root, hostile audit, and strict blind
reconstruction have SHA-256 hashes
`bea005ed8c16878fdb334c12e01f55b4b6569294662e274121e8d1b396f65fea`,
`8164f562ec33a6ab4fe9cedf3345a2917c5cba7545d64dbb4e1e6f957b51bd62`,
`c7af4315d87f4e99a223cf6a30406a71288a55b7a3d3c835cd41aac0cff3f6e8`,
`62e617933f06b051c4d4852420e82a27d952fe0a2c0039b898a00a35011f9a09`,
and
`7c9fdf2ccc01d25a418146f5fad81bab1ff2e178572da9bce6adc4b4fa11aed3`.
No numerical search, remote run, or human audit occurred.

## P227 — integer-valued finite differences move the hidden threshold but leave a remote Stirling evaluator

**Status:** promoted from F277 after a fresh hostile audit and a strict
statement-only reconstruction. This is a boundary for three named
integer-valued finite-difference families. It is not an evaluator lower bound
or a factoring algorithm.

Let

\[
 N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor=p+s,
\]

with distinct odd primes. The branch \(s=0\) is already factored by
\(\gcd(B,N)=p\). On \(s>0\),

\[
 q-p\ge 2s+2,\qquad q-B\ge s+2,\qquad 2s+1<p.
\]

Every integer-valued polynomial has the Newton expansion

\[
 f(X)=\sum_{j=0}^{D}\Delta^jf(0)\binom Xj,
 \qquad
 \Delta^kf(a)=\sum_{j=k}^{D}\Delta^jf(0)\binom a{j-k}.
\]

Thus a high difference shifts Newton coefficients; it does not evaluate a
remote one. For a monomial, the exact normalized difference is

\[
 \frac{\Delta^BX^m(0)}{B!}
 =\left\{\begin{matrix}m\\B\end{matrix}\right\}.
\]

The hostile audit stresses that this Stirling number is the normalized
difference. The literal Newton coefficient of \(X^m\) is
\(B!\left\{\begin{smallmatrix}m\\B\end{smallmatrix}\right\}\).

For the shifted-binomial family

\[
 F(c)=\binom{N+c-1}{B},
\]

one has the exact phase law, for \(1\le c<p\),

\[
 \Delta_c^kF(c)\equiv
 \begin{cases}
 q\binom{c-1}{s-k},&0\le k\le s,\\[3pt]
 \binom{c-1}{B-k},&s<k\le B
 \end{cases}
 \pmod N.
\]

At \(c=1\), the only nonzero residues are the hidden spike \(q\) at
\(k=s\) and the terminal value one at \(k=B\). Finite differences therefore
translate the unknown threshold; the first order after that threshold has
already lost the CRT asymmetry.

If \(w=\min(V,U-V)<p\), then

\[
 \binom UV=\frac{\prod_{i=1}^{w}(U-w+i)}{w!}
\]

has a unit denominator modulo \(N\). Every hidden-prime valuation, hence
every short-side Kummer carry, is already present in a displayed numerator
factor. This is a direct factor-first screen and modular evaluator, but its
gcd can be saturated; it is not a guaranteed proper-factor oracle. The
central control

\[
 \Delta^B\binom X{2B}\bigg|_{X=2B}=\binom{2B}{B}
\]

has gcd exactly \(q\), reproducing the known remote central-binomial gate.

The new exact local laws are

\[
 T_0=\left\{\begin{matrix}2B\\B\end{matrix}\right\},
 \qquad
 T_1=\left\{\begin{matrix}2B+1\\B\end{matrix}\right\},
\]

with

\[
 T_0\equiv T_1\equiv0\pmod q,
\]

and

\[
 T_0\equiv2\left\{\begin{matrix}2s+1\\s\end{matrix}\right\}\pmod p,
 \qquad
 T_1\equiv2\left\{\begin{matrix}2s+2\\s\end{matrix}\right\}\pmod p.
\]

Each scalar has an explicit saturated balanced example. The pair is
simultaneously saturated exactly when \(p\) divides both

\[
 \left\{\begin{matrix}2s+1\\s\end{matrix}\right\},
 \qquad
 \left\{\begin{matrix}2s+1\\s-1\end{matrix}\right\}.
\]

No joint nonvanishing theorem is proved. Literal inclusion-exclusion has
\(B+1\) terms and a nonunit \(B!\); the ordinary recurrence has a
characteristic-size index range; exact materialization has
\(\Theta(B\log(B+1))\) bits. These are representation costs, not a circuit
lower bound. A succinct modular central-Stirling evaluator, together with a
proved dispatcher for simultaneous saturation, remains a genuinely open
route.

The statement, proof, frozen root, hostile audit, and strict reconstruction
have SHA-256 hashes
`1f4c3226ddabfc231f37f4da4b6f9ac410e225f646e82a54cbc29b845bed381a`,
`03eb08846cf696c064cf6c878cf12387800d821d68d9fccd884f446fa407c01a`,
`5c7d3bb9fb87971342c0023cfb270ce88d81deb2151d220123a7f587a6178cc0`,
`c922f515995b92a24bf855ef3205e34ad1e1069a7c47090d93d492cb0c391531`,
and
`d9e0960d9a3f99ccf0c96b1953777c51a1f6e81f929612d6c73752b897d49431`.
No production computation, remote run, or human audit occurred.

## P228 — explicit constant-matrix powering closes Jordan windows and spectral collisions, but not additive coordinates

**Status:** promoted from F278 after a fresh hostile audit and a strict
statement-only reconstruction. This is a boundary for explicit ordinary
matrix powers. It is not a recurrence lower bound or a factoring algorithm.

Let

\[
 N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor=p+s,
\]

with distinct odd primes. The branch (s=0) is already factored by
\(\gcd(B,N)=p\). If an explicit public matrix (C_N\) has numerical-QP
dimension and numerical-QP constructible entries, binary powering computes
the complete (C_N^B\bmod N) in numerical quasipolynomial time and space.
Thus the endpoint is automatic; the missing object is an asymmetric
observable.

For a unit scalar \(\alpha\) and a nilpotent Jordan shift (J_h), with
\(h\le d<p\),

\[
 (\alpha I+J_h)^B
 =\sum_{j=0}^{h-1}\binom Bj\alpha^{B-j}J_h^j.
\]

For every (1\le j<h\),

\[
 \gcd\!\left(\binom Bj\alpha^{B-j},N\right)=p
 \iff j>s
 \iff
 \gcd\!\left(\prod_{t=0}^{j-1}(B-t),N\right)=p.
\]

Hence a QP-width Jordan block is exactly the direct scan of
(B,B-1,\ldots,B-h+2\). After the boundary screen, a nonzero local Jordan
block keeps its nilpotent type under (X\mapsto X^B\); a zero block of size
at most (B) dies in both CRT components. Recovering the displayed
coefficients after conjugacy requires a public unit change of basis.

If (C\bmod r) is clean, invertible, and semisimple, two distinct
eigenvalues collide in (C^B\) exactly when

\[
 (\alpha_i/\alpha_j)^B=1.
\]

Thus a powered characteristic-polynomial discriminant or a separately
proved collision-sensitive rank loss is an extension-field order event.
The invertible matrix (C^B\) itself never loses rank.

For the clean quadratic companion

\[
 C=\begin{pmatrix}t&-\delta\\1&0\end{pmatrix},\qquad
 U_{k+1}=tU_k-\delta U_{k-1},
\]

one has ((C^B)_{2,1}=U_B\), and

\[
 U_B=0\pmod r\iff z_r^B=1,
\]

where (z_r\) is the ratio of the two roots. This is an ordinary split-group
event when the polynomial splits and a norm-one-torus event when it is
irreducible. At the smaller prime the residual exponents are respectively
(s+1\) and (s-1\).

Cayley--Hamilton identifies every explicit matrix coordinate with a public
constant-in-index recurrence of order at most (d\), and every such
initialized recurrence with a public state-space matrix endpoint. This is
an evaluator equivalence, not a lower bound.

The boundary is deliberately incomplete. A general two-mode coordinate can
vanish through

\[
 a\alpha^B+b\beta^B=0
 \iff (\alpha/\beta)^B=-b/a,
\]

which is a power-coset condition rather than the collision target one.
Such cancellation already occurs in dimension two and is not classified by
P228. Three-or-more-mode additive cancellation, semilinear constructions,
arbitrary (N\)-dependent coefficients, and accidental agreement of an
ordinary power with a local Frobenius action also remain open. The packet's
decision not to search its three closed mechanisms is methodological, not
an impossibility theorem for these open lanes.

The statement, proof, frozen root, hostile audit, and strict reconstruction
have SHA-256 hashes
`4232a1007700802b25acafed944f7b5adc227a913af26aec8ab6b17a7bdba0fa`,
`194461e35d35a82ccea95df3c99ffb76cc414af5852c5fff7c917409a9403073`,
`cfeb683b75c36129da0623a0a4172fb7c1b23dd50f6c3af5e8176af1591045a8`,
`5d148b2e01d89874134a49f5a69716a47aef57371600d83025bafe28fd30c53a`,
and
`ccc7270675f88069b4db196e7e206c1f7d8ba2a9d6d5ec8b83515b8bbec23b7c`.
No numerical search, remote run, or human audit occurred.

## P229 — bounded global-order sources admit an all-local postprocessor, but no useful transfer follows

**Status:** promoted from F280 V2 after an independent primary-source hostile
audit and a strict statement-only reconstruction. F280 V1 remains failed and
immutable. This is a source theorem and a transfer boundary. It is not a
factoring algorithm.

Let \(N\ge3\), let \(1\le D<N-1\), and suppose a deterministic source returns
either a nontrivial factor of \(N\) or a unit \(a\bmod N\) with

\[
 \operatorname{ord}_N(a)>D.
\]

For \(1\le e\le D\), compute successive powers and

\[
 g_e=\gcd(a^e-1,N).
\]

The saturated case \(g_e=N\) is impossible, because it would imply
\(\operatorname{ord}_N(a)\mid e\le D\). A proper \(g_e\) factors \(N\). If
all \(g_e=1\), then

\[
 \operatorname{ord}_p(a)>D
 \qquad\text{for every rational prime }p\mid N.
\]

The postprocessor uses exactly \(D\) power-gcd rounds on a completed scan and
costs

\[
 O\!\left(D\,\mathsf M(n)\log n\right),
 \qquad n=\lceil\log_2(N+1)\rceil.
\]

Composed with the authenticated Harvey--Hittmeir interface, this gives a
deterministic factor-or-all-local-unit procedure with total time

\[
 O\!\left(
 D^{1/2}\frac{\log D}{\sqrt{\log\log D}}\log N
 +D\,\mathsf M(n)\log n
 \right),
\]

with the finite case \(D=1\) absorbed separately. Composed with Nir
Proposition 1.2, it gives a factor, a prime report, or an ordinary integer

\[
 2\le a\le D^2+D
\]

whose order exceeds \(D\) at every prime divisor of \(N\), in

\[
 O\!\left(D^{5/2+o(1)}\operatorname{polylog}N\right)
\]

time. Therefore numerical-quasipolynomial \(D\) gives a
numerical-quasipolynomial, bounded-height, all-local-order source. Nir's main
theorem has a larger parameter threshold and is not the interface used for
this numerical-QP conclusion.

Two exact boundaries prevent promotion into a factoring transfer.

1. Large global order alone need not be large locally. For
   \(N=77,D=10,a=2\), the local orders are \(3\) and \(10\), while the global
   order is \(30\).
2. If screened exact orders \(m_i\) synchronize at every prime divisor and
   \(M=\operatorname{lcm}(m_i)\), then for a semiprime \(N=pq\),
   \[
    M\mid\gcd(p-1,q-1)\mid N-1.
   \]
   Its relevant prime-power capacity is already contained in the registered
   \((N-1)^n\) baseline. This is a capacity statement, not a theorem that a
   known common order is useless in every algorithm.

The construction supplies no rough-order law, asymmetric residual word,
carry, quotient, determinant, or P205 transfer. A future use must add and
prove such a transfer; merely increasing the source order is not enough.

The V2 statement, proof, frozen root, hostile audit, and strict blind
reconstruction have SHA-256 hashes
`36d2323aa63822f23b55b5daa5aa98032592a4c3112040ab6d4bb33427143083`,
`9d4e1a7d57c8fe2023f38e83cb42044f0b08d5852145c370b4edd18d2b9c94ab`,
`9a451b1c294c770d8c7f936bd9ad8d5f34abe2b002eabf81274a2349bfc95f76`,
`164e34cde001e168c7e897df740a746e0469f1fa12e64d68ce5cf3e231559656`,
and
`b08966b99920287dc24544fc180a6eedeb3dfc8d13d84595092604ae33996f0d`.
No numerical search or remote run occurred.

## P230 — random shifts remove central-Stirling saturation, conditional on one normalized-difference evaluator

**Status:** promoted from F282 after a fresh hostile proof audit and an
independent statement-only reconstruction. This is a constant-success
splitter theorem conditional on a missing evaluator. It is not an executable
factoring algorithm or an all-input reduction.

Let

\[
 N=pq,
 \qquad p<q<2p,
 \qquad B=\lfloor\sqrt N\rfloor,
\]

where \(p,q\) are distinct odd primes. First test \(\gcd(B,N)\). On the
unresolved branch there are integers \(s,h\) with

\[
 B=p+s,
 \qquad q=B+h,
 \qquad s\ge1,
 \qquad h\ge s+2,
 \qquad p\ge2s+3.
\]

For every integer shift \(a\), define the exact integer

\[
 F_B(a)=\frac{\Delta^B X^{2B}|_{X=a}}{B!}.
\]

The division is exact in \(\mathbb Z\), not modular division. The consecutive
divided-difference identity gives

\[
 \boxed{F_B(a)=h_B(a,a+1,\ldots,a+B).}
\]

The complete-homogeneous generating series then gives the two exact local
laws

\[
 \boxed{F_B(a)\equiv0\pmod q}
\]

for every shift, and

\[
 \boxed{
 F_B(a)\equiv
 2h_{s+1}(a,a+1,\ldots,a+s)\pmod p.}
\]

The second expression is a nonzero polynomial in \(a\) of exact degree
\(s+1\). Its leading coefficient is

\[
 2\binom{2s+1}{s}\not\equiv0\pmod p.
\]

It therefore has at most \(s+1\) roots modulo \(p\). A uniform residue
\(a\bmod N\) is uniform modulo \(p\), so

\[
 \Pr\!\left[\gcd(F_B(a),N)=q\right]
 \ge1-\frac{s+1}{p}
 \ge\frac{p+1}{2p}
 >\frac12.
\]

Every other trial returns the saturated gcd \(N\). Independent repetition
has expected trial count below two, and only a verified proper divisor is
returned. Consequently, any one uniform classical numerical-QP algorithm
which computes \(F_B(a)\bmod N\) from public \((N,a)\) yields a uniform
classical Las Vegas numerical-QP factorer on this balanced
distinct-odd-semiprime promise.

The evaluator is not supplied. On the unresolved branch

\[
 p<B<q<2p,
 \qquad \gcd(B!,N)=p.
\]

Since \(q\mid F_B(a)\) for every shift, the raw difference

\[
 B!F_B(a)=\Delta^B X^{2B}|_{X=a}
\]

is zero modulo all of \(N\). Thus evaluating the raw numerator does not
retain the splitter. The useful residue appears only after exact division by
the factor-bearing \(B!\). The literal alternating sum has \(B+1\) terms,
the direct complete-homogeneous recurrence has characteristic-size state,
and exact materialization has \(\Theta(B\log B)\) bits already at \(a=0\).
These are costs of named representations, not lower bounds against another
succinct modular evaluator.

P230 removes the separate F281 simultaneous-saturation conjecture from this
conditional route: random shifts already give constant success. It does not
recognize the promise, handle unbalanced or nonsquarefree composites, or
provide an all-input reduction. The sole operational gap on the stated
promise is now the normalized evaluator itself.

The statement, proof, frozen root, hostile audit, and strict statement-only
reconstruction have SHA-256 hashes
`831ac1a429968a20fdeffa2e0c0e7d1972fe43deec3a22e43ee4b71a2d01f0bf`,
`0a5e20cb27f671d5e797196b1a987e776547b2f67be5a2e95af21b663ce69d2c`,
`5e173dbf13cea22681133082df0b5771c7e2397d8612b5becf2ef63c9f468fec`,
`c48fe03bf875fec09f9c6d0c2e8341e1a2fe85c5e308c4aeba1e1622bdb75cc8`,
and
`a615ca4fd6645d928082ce9c1a3d953e420ad3d078e0eec9164876eea2d40628`.
The proof packet used no computation or remote run. A separate post-freeze
82-case local sanity check was non-authoritative and is not promotion
evidence.

## P231 — named normalized-difference evaluators retain characteristic state or meet a factor gate

**Status:** promoted from F283 after a fresh hostile proof audit and an
independent statement-only reconstruction. This is a scoped boundary for the
evaluator left open by P230. It is not an evaluator, a factoring algorithm,
or a general circuit lower bound.

Keep the unresolved balanced-semiprime notation of P230 and put

\[
 F_B(a)=\frac{\Delta^B X^{2B}|_{X=a}}{B!}
       =h_B(a,a+1,\ldots,a+B).
\]

This target is exactly the generalized-Stirling endpoint

\[
 F_B(a)=G_a(2B,B),
 \qquad
 \sum_{d\ge0}G_a(B+d,B)t^d
 =\prod_{j=0}^{B}(1-(a+j)t)^{-1}.
\]

Over \(\mathbb Q(a)\), the denominator has \(B+1\) distinct uncancelled
poles. Therefore the full canonical coefficient sequence has minimal
constant-coefficient recurrence order and constant-matrix realization
dimension \(B+1\). Every fixed-radix decimation keeps all \(B+1\) modes.
Translation, consecutive-block composition, and the even--odd split likewise
retain a full \(B+1\)-coefficient convolution or a literal linear-size
two-child recursion. These are exact facts about the named canonical linear
states, not bounds on a tailored nonlinear single-output evaluator.

For the divided-power operators \(\mathcal D_k=\Delta^k/k!\),

\[
 \mathcal D_m\mathcal D_n
 =\binom{m+n}{m}\mathcal D_{m+n}.
\]

In every monotone positive-index addition chain from \(1\) to \(B\), the
first index \(k=m+n\ge p\) satisfies

\[
 \gcd\!\left(\binom{k}{m},N\right)=p.
\]

Thus literal normalized composition meets a factor-bearing structure
constant. Deferring normalization gives only
\(B!F_B(a)\equiv0\pmod N\).

The guaranteed larger-prime zero is universal interval content. The exact
coefficient law is

\[
 [a^k]F_B(a)=\binom{2B}{k}
 \left\{\begin{matrix}2B-k\\B\end{matrix}\right\}.
\]

If

\[
 P_B=\prod_{\substack{r\ \mathrm{prime}\\B+1<r<2B}}r,
\]

then \(P_B\mid\operatorname{content}(F_B)\), and on the P230 branch

\[
 \gcd(P_B,N)
 =\gcd(\operatorname{content}(F_B),N)
 =q.
\]

The leading coefficient is \(\binom{2B}{B}\), so explicit interval-content
or leading-coefficient evaluation is already the known factor gate. Removing
that content also removes the guaranteed \(q\)-zero.

The immediate lift does not repair normalization. Writing \(B!=pU\) and
\(F_B=qV_B\), exact division of the raw difference modulo \(N^2\) yields

\[
 \frac{B!F_B(a)}N\equiv U V_B(a)\pmod N,
\]

which has no promised prime divisor of \(N\). The faithful modulus \(NB!\)
has characteristic bit length and materializes the already factor-bearing
factorial gate.

Consequently, no finite search is justified inside the named
generalized-Stirling sum, full coefficient state, literal block convolution,
monotone normalized addition chain, raw-difference, explicit content,
canonical constant-matrix, immediate \(N^2\)-quotient, or known
\(B^{1/2+o(1)}\) endpoint grammars. A future search must first supply a
different, explicit numerical-QP transition which accepts an arbitrary
public shift, uses unit-safe public operations, and preserves the P230
factor asymmetry. Nonlinear, adaptive, branching, tailored, higher-lift, and
general arithmetic-circuit routes remain open.

The statement, proof, frozen root, hostile audit, and strict statement-only
reconstruction have SHA-256 hashes
`97711c57667f13d4a86daa5b0533ecdb3165818f92544016fb38ee8673b3e006`,
`b14153c052c20e5059dbd1a0881cd71dc846a439c712f1a871ec80cabc6520e1`,
`4e71c1866f2fc8badfa063f3e08aee43531de12a7fde49452254d04fec681e5e`,
`c983e378d1717604369e8c89b30ebfacb3fc20e54fbbc6beaa04aa6ab54fcbd5`,
and
`1ba622e780e53f7c7446143d470efe7846df7b19d15db06e695a3a5e831e2c42`.
No computation or remote run occurred.

## P232 -- Public matrix-power derivative ranks and mutual-order exceptions

**Status:** promoted after a fresh statement-only Sol reconstruction and root
verification of the exact claims. No literature-level novelty claim is made.

**Scope:** individual derivative ranks on the squarefree-characteristic-polynomial
branch over a distinct-prime semiprime. Not a general factoring lower bound.

**Statement.**

Let N=rs with distinct primes and let A be a d-by-d matrix modulo N. Over F_r
assume its characteristic polynomial is squarefree and define

    L_A(H) = sum_(i=0)^(N-1) A^i H A^(N-1-i).

Then ker(L_A)=Cent(A^N), and rank(L_A)=rank(ad_(A^N)). If m_z counts the
distinct eigenvalues of A with N-th power z, the rank is d^2-sum_z m_z^2.
In particular it is d^2-d whenever ord_s(r)>d, or whenever ord_s(r) divides
none of the irreducible factor degrees of the characteristic polynomial.

For a fixed odd prime p and D>=1, fewer than D(D+1) prime q in (p,2p) have
ord_q(p)<=D or ord_p(q)<=D. Outside this set, both ranks equal d^2-d for
every d<=D and every public matrix with unit characteristic discriminant,
including adaptively selected matrices. By the prime number theorem the
exceptional proportion is O(D^2 log(p)/p), and tends to zero when D is any
fixed quasipolynomial in log p. Prime distribution is used only for this
asymptotic interpretation, not the finite count.

**Proof.** Over a splitting field, the matrix units diagonalize L_A. Diagonal
units have eigenvalue zero; an off-diagonal unit has eigenvalue
(lambda_i^N-lambda_j^N)/(lambda_i-lambda_j). This gives the kernel and rank
formulas. A nonzero eigenvalue belongs to an extension of degree e<=d and has
multiplicative order dividing r^e-1. If ord_s(r) divides no such e, the group
generated by any two eigenvalues has order coprime to s. N-th powering is
injective on that group; a zero eigenvalue cannot collide with a nonzero one.

For exceptional q with ord_q(p)<=D, their distinct product divides
product_(k=1)^D(p^k-1)<p^(D(D+1)/2), while each q>p. Their count is strictly
less than D(D+1)/2; the empty set satisfies this directly. The second
exceptional set injects through q-p into elements of F_p^* with order<=D,
of which there are at most sum_(k=1)^D k. This proves the union count.
The PNT gives pi(2p)-pi(p)~p/log p and eventual positivity; D=p^o(1) gives
the stated limit. This avoids any extra dependency for small finite intervals.

The conclusion excludes combined operators, selected minors or entries,
intermediate nonunit pivots, and nonsquarefree characteristic polynomials.
It does not close those sources of factor information.

Proof and scope: `experiments/F285_finite_algebra_operator_search/DIMENSION_EXTENSION.md`.
Independent proof: `experiments/F285_finite_algebra_operator_search/RECONSTRUCTION.md`.
Its statement-only input SHA-256 is
`259375eb1a4494cd010055c61f5f5bb7f0927388216da05092a02bf8a5717377`.
The separate two-by-two probability calculation is not promoted by this record.

## P233 -- Global congruence-tangent cuts leave every early modular branch

**Status:** promoted after independent statement-only reconstruction and root
verification. The finite computations support examples, not the proof.

**Scope:** the exact continuous relaxation and bounded global-tangent menu below.

**Statement.**

Let N be odd, B,A positive integers, 2B^2<=N<=9B^2/4, and M=2^k with k>=1
and M<=B/(4096A^3). For each odd u modulo M put v=N/u modulo M. Let I_u,I_v
be the intervals between the least and greatest integers in [B,2B] in those
residue classes. For every 1<=a,b<=A, let T_ab be the least integer at least
2 sqrt(abN) congruent to au+bv modulo M.

Every one of the M/2 states admits real x,y satisfying

    x in I_u, y in I_v, xy=N, ax+by>=T_ab for every a,b.

The same point also satisfies the corresponding ancestor constraints modulo
2^j, 1<=j<=k. These real points are not asserted to satisfy discrete congruences.

**Proof.** Every rounded coordinate interval contains [B+M,2B-M]. The
hyperbola arc x in [5B/4,7B/4] has y in [8B/7,9B/5], inside that common
core. On this arc, the set where ax+bN/x<2 sqrt(abN)+M is contained in an
interval of length sqrt(7MB/a), since the exact excess is
a(x-sqrt(bN/a))^2/x. The sum of these lengths over all a,b is at most
2 sqrt(7) A^(3/2) sqrt(MB)<=sqrt(7)B/32<B/2, the arc's length. A point
outside the union satisfies every cut because T_ab<2 sqrt(abN)+M.
Fine residue intervals lie inside ancestor intervals, and fine thresholds
are at least the corresponding ancestor thresholds, proving consistency.

Literal retention therefore has a numerical-scale population before these
cuts can prune all branches. The result does not cover recomputed local
minima, additional constraints, compressed access, or arbitrary algorithms.

Author proof and finite certificates:
`experiments/F286_diophantine_constraint_search/RESULT.md` and `output.json`.
Independent proof: `experiments/F286_diophantine_constraint_search/RECONSTRUCTION.md`.
Statement-only input SHA-256:
`3a3356cb1b779a2a40d46fe4f9fde4caad262ab928bc3ae44fba397a901b9e9f`.
The separate iterated and fast-forward analyses remain unpromoted candidates.

## P234 -- Fast normalized Gaussian-binomial jets and sparse uniform-index probes

**Status:** promoted after fresh statement-only reconstruction, exact Sage checks,
and root verification. The underlying cumulant method is established mathematics;
this record does not claim a new literature result or a factoring algorithm.

**Scope:** short normalized exponential jets and their individual coefficient
gcds under uniform indices. Selected indices and other decoders are outside the bound.

**Statement.**

For b>=0 let G_b(t)=[2b choose b]_t and define c_j(b) by

    G_b(exp(z))/binom(2b,b) = sum_(j>=0) c_j(b) z^j.

For each j>=1, c_j is a rational polynomial in b of exact degree 2j and
leading coefficient 1/(2^j j!). Its coefficient denominator primes are at
most j+1. The first J+1 coefficients have an exact algorithm polynomial in
J+log(b+1), without materializing either G_b or the central binomial.
The bound is polynomial in the output count J, not log J.

If N=pq with distinct primes p,q>J+1 and b is uniform modulo N, then

    Pr[exists 1<=j<=J with 1<gcd(c_j(b) mod N,N)<N]
       <= J(J+1)(1/p+1/q).

**Proof.** Put phi(z)=(exp(z)-1)/z. The normalized product equals
product_(r=1)^b phi((b+r)z)/phi(rz). Its logarithm has coefficient
l_n=[z^n]log(phi(z)) * (S_n(2b)-2S_n(b)), where S_n is a Faulhaber
polynomial. Thus deg l_n<=n+1 and l_1=b^2/2. In the exponential, degree
2j comes uniquely from l_1^j/j!. Truncated logarithm, power-sum, and
exponential recurrences use only rational denominators with primes<=J+1
and O(J^2) arithmetic operations of polynomial bit size. A detailed
denominator/bit-size proof is in the independent reconstruction. Reductions
modulo p and q remain nonzero degree-2j polynomials. The root bound and
union bound give the displayed probability, without independence assumptions.

This successful compression removes the unknown central-binomial scalar.
It does not evaluate the unnormalized factor-bearing product. It supplies
no all-input useful-source guarantee, and the uniform-index bound does not
apply to b=floor(sqrt(N)) or to moment determinants.

Author derivation, sources, and Sage evidence:
`experiments/F284_cyclotomic_binomial_search/RESULT.md` and `RUN_MANIFEST.md`.
Independent proof: `experiments/F284_cyclotomic_binomial_search/RECONSTRUCTION.md`.
Statement-only input SHA-256:
`3744a4d9d3e7561fed0bf51917fb02ab70bed64d24d2ed93ae7e90d6103e7d21`.

## P235 -- Dyadic inverse graphs admit affine and higher-difference covers, and constant-accuracy support would split odd composites

**Status:** promoted after independent statement-only reconstruction and root
verification. This is a conditional reduction, not a support optimizer or a
factoring algorithm.

**Scope:** inverse graphs modulo powers of two, their exact finite-difference
representations, and the succinct-instance support reduction below.

**Statement.**

Let \(N\) be odd, \(M=2^k\), \(k\geq1\),
\(h=\max(1,\lfloor k/2\rfloor)\), and \(s=2^h\). Define

\[
 S=\{(x,y)\in\mathbb Z_{>0}^2:xy\geq N,\ xy\equiv N\pmod M\}.
\]

For each odd \(u\in[1,s)\), put

\[
 v\equiv Nu^{-1}\pmod M,\qquad
 \delta\equiv N((u+s)^{-1}-u^{-1})\pmod M.
\]

Then \(S\) is the disjoint union of

\[
 \bigl((u,v)+\mathbb Z(s,\delta)+\mathbb Z(0,M)\bigr)
 \cap\{x>0,y>0,xy\geq N\}.
\]

There are exactly \(2^{h-1}\) translates, each with difference-lattice
determinant \(sM\).

More generally, for \(r,d\geq1\), \(s=2^r\), and odd \(u\),

\[
 \Delta_s^d\!\left(\frac Nu\right)
 \equiv
 \frac{(-1)^d d!Ns^d}{\prod_{i=0}^d(u+is)}
 \pmod M.
\]

If \(rd+v_2(d!)\geq k\), the sequence
\(j\mapsto N(u+sj)^{-1}\pmod M\), for all \(j\in\mathbb Z\), is represented
by a degree-at-most-\(d-1\) polynomial in the binomial basis.

For the conditional reduction, let \(N\geq9\) be any odd composite,
\(n=\lceil\log_2(N+1)\rceil\), and let \(M\) be the largest power of two at
most \(N/8\). For \(-n\leq j\leq n\), use

\[
 a_j=2^{\max(j,0)},\qquad b_j=2^{\max(-j,0)}.
\]

Suppose an optimizer receives the succinct \(O(n)\)-bit instance
\((N,M,a_j,b_j)\), or an equivalent succinct description of \(S\), and
returns a feasible \(Q_j=(x_j,y_j)\) satisfying

\[
 a_jx_j+b_jy_j
 \leq\frac{101}{100}
 \min_{(x,y)\in S}(a_jx+b_jy)
\]

in bit cost \(T(n)\). At least one of the \(2n+1\) returned points has
\(x_jy_j=N\) and \(x_j,y_j>1\). The returned coordinates have \(O(n)\)
bits, and the literal splitter cost is

\[
 O\bigl(nT(n)+\operatorname{poly}(n)\bigr).
\]

Explicitly listing the \(2^{h-1}\) affine translates is not a succinct input
and is outside this cost statement.

**Proof.** The affine inverse error is

\[
 u^{-1}+a((u+s)^{-1}-u^{-1})-(u+as)^{-1}
 =\frac{-a(a-1)s^2}{u(u+s)(u+as)}.
\]

Its numerator is divisible by \(2^{2h+1}\), which proves the cover,
disjointness, and count. The displayed higher-difference formula follows by
induction; its valuation makes the \(d\)-th difference vanish, and Newton's
binomial expansion extends in both integer directions without dividing by
\(d!\).

For the reduction, write \(N=pq\), \(3\leq p\leq q\), and choose the dyadic
normal nearest to \(q/p\). Then \(t=a_jp/(b_jq)\) lies between
\(2^{-1/2}\) and \(2^{1/2}\). Weighted AM--GM and the relative guarantee give

\[
 x_jy_j
 \leq \left(\frac{101}{100}\right)^2
 N\frac{(1+t)^2}{4t}
 <\frac{17N}{16}<N+M.
\]

The product congruence forces \(x_jy_j=N\), and its objective is below \(N\),
excluding \((1,N)\) and \((N,1)\). The small \(M=1\) cases obey the same
integer-product conclusion.

Full proof:
experiments/F289_modular_support_union/PATCH_RECONSTRUCTION.md.
Statement-only input:
experiments/F289_modular_support_union/PATCH_STATEMENT_ONLY.md.
Input SHA-256:
`89487b6b7d852efa9c43b7f6dfd3ae6915e37a24683d0e5583edc9875cd395e3`.

The implemented one-patch support oracle, affine-tree pruning, grouped
cap-line bound, F287 dynamics, and F290 transforms are not promoted here.

## P236 -- One rational-root quadratic-Gauss/Cauchy kernel has an output-sensitive polynomial-time Taylor/Laurent algorithm

**Status:** promoted after fresh statement-only Sol reconstruction and root
scope verification. The only external algorithmic dependency is Hiary 2011,
Theorem 1.1.

**Scope:** one finite quadratic-Gauss/Cauchy kernel at one rational root of
unity, including its requested Taylor or Laurent coefficients and exact pole
removability. No outer-index contraction or factoring bound.

**Statement.**

For \(m,D\geq1\), integers \(a,b,c,s\), and

\[
 e_q(x)=\exp(2\pi i x/q),\qquad
 t_0=e_D(s),\qquad
 \ell=\frac{m}{\gcd(b,m)},
\]

define the rational function

\[
 F(t)=\sum_{z=0}^{m-1}
 \frac{e_m(az^2+cz)}{1-t\,e_m(bz)}.
\]

Let \(J,p\geq0\) and \(\rho=t/t_0\). If \(t_0^\ell\neq1\), every coefficient through degree
\(J\) in

\[
 F(t_0\rho)=\sum_{j=0}^J B_j(\rho-1)^j
             +O((\rho-1)^{J+1})
\]

can be approximated to absolute error at most \(2^{-p}\). If
\(t_0^\ell=1\), the same holds for \(A,B_0,\ldots,B_J\) in

\[
 F(t_0\rho)=\frac{A}{1-\rho}
 +\sum_{j=0}^J B_j(\rho-1)^j+O((\rho-1)^{J+1}).
\]

There is a deterministic algorithm with bit complexity polynomial in the
ordinary binary lengths of \(m,D,a,b,c,s\) and in the numerical output
parameters \(J,p\). It does not enumerate \(m\) or \(\ell\), factor \(m\) or
\(D\), or materialize a degree-\(D\) cyclotomic field. In the pole case it
decides exactly whether \(A=0\), equivalently whether the potential pole is
removable.

The output-sensitive reading of \(J,p\) is essential: the requested output
itself can have order \(Jp\) bits.

**Proof.** Put

\[
 G(a,C;m)=\sum_{z=0}^{m-1}e_m(az^2+Cz),\qquad
 P(t)=\sum_{n=0}^{\ell-1}t^nG(a,c+bn;m).
\]

The finite geometric identity gives

\[
 F(t)=\frac{P(t)}{1-t^\ell}.
\]

Imprimitive complete-Gauss reduction and the exhaustive odd/even primitive
Gauss formulas restrict every nonzero \(G(a,c+bn;m)\) to one arithmetic
progression in \(n\). On that progression its phase is a rational quadratic
polynomial. Expanding the needed binomial weights reduces all derivatives of
\(P(t_0\rho)\) through degree \(J+1\) to polynomially many weighted
quadratic sums.

Hiary, Annals of Mathematics 174 (2011), 859--889, Theorem 1.1 evaluates
each normalized polynomially weighted quadratic sum with operation count and
working precision polynomial in \(\log(\mathrm{length}+1)\), the weight
degree, and \(\log(1/\mathrm{accuracy})\). Undoing normalization adds only
the corresponding precision bits.
Complete Gauss amplitudes use the same \(j=0\) case or explicit gcd,
Jacobi, and parity formulas.

The pole test is the exact divisibility condition \(D\mid s\ell\). At a
potential pole, let \(g=\gcd(b,m)\), \(b_0=b/g\), and
\(r_0=s\ell/D\). If \(z_0\) solves
\(b_0z_0\equiv-r_0\pmod\ell\), then

\[
 A=e_m(az_0^2+cz_0)
   G(a\ell,2az_0+c;g).
\]

The complete-Gauss gcd and parity cases decide its vanishing exactly, without
integer factorization. Finally, triangular division by
\(1-t_0^\ell\rho^\ell\), or by its simple zero in the Laurent case, gives
the requested coefficients. Root-of-unity separation and coefficient bounds
show that

\[
 p+O((J+2)(\log(m+1)+\log(D+1)+\log(J+2)+1))
\]

working bits suffice. Tightening Hiary's error parameter absorbs its stated
polynomial prefactor.

Independent proof:
experiments/F292_localized_character/KERNEL_RECONSTRUCTION.md.
Statement-only input:
experiments/F292_localized_character/KERNEL_STATEMENT_ONLY.md.
Author derivation and exact finite checks:
experiments/F292_localized_character/KERNEL_PRIMITIVE.md.
Input SHA-256:
314695ff8f987a46eb8d90f1f9be4a6deb646bde324379b94a902971e957116b.

This record does not cover a sum over many outer kernel indices, products of
several Cauchy denominators, arbitrary interior \(t\), or any factoring
runtime. Adjacent F292 and F294 author claims remain unpromoted.

## P237 -- Succinct modular rectangle emptiness would factor every integer with O(n^2) queries

**Status:** promoted after fresh statement-only Sol reconstruction and root
scope verification, including the adaptive Las Vegas randomness argument.

**Scope:** a conditional all-input reduction from complete integer
factorization to the stated succinct modular rectangle-emptiness oracle. No
efficient implementation of that oracle, support optimizer, or rational-filter
evaluation theorem.

**Statement.** Let \(N\geq2\) have bit length \(n\). Suppose

\[
 \operatorname{Empty}(K,M,[A,B],[C,D])
\]

correctly decides whether some integers \(x\in[A,B]\), \(y\in[C,D]\) satisfy
\(xy\equiv K\pmod M\), where \(M\) is a power of two, every endpoint lies in
\([1,M-1]\), and all inputs have \(O(n)\) bits with a uniform fixed constant.
Assume each call has uniform deterministic bit cost at most \(T(n)\), or is
always correct with Las Vegas expected bit cost at most \(T(n)\).

Then one uniform algorithm completely factors every \(N\) with
\(O(n^2)\) oracle calls and polynomial additional bit work. Its total cost is

\[
 O\bigl(n^2T(n)+\operatorname{poly}(n)\bigr).
\]

In the Las Vegas case it returns only correct outputs, terminates almost
surely, and satisfies the displayed expected bound. Thus a quasipolynomial
\(T(n)\) would give an all-input classical quasipolynomial factoring
algorithm.

**Construction and proof.** At each recursive input \(K\), first test the
fixed primes \(2,3,5,7,11,13\), treating equality as a prime leaf and a
proper division as a recursive split. For the remaining \(K\geq17\), let
\(M\) be the largest power of two at most \(K/8\), put
\(R=17/16\), \(L_j=16R^j\), and, while \(L_j\leq\sqrt K\), form

\[
\begin{aligned}
 I_j&=[\max(17,\lceil L_j\rceil),
        \min(\lfloor\sqrt K\rfloor,\lfloor RL_j\rfloor)],\\
 J_j&=[\max(1,\lceil K/(RL_j)\rceil),
        \min(M-1,\lfloor K/L_j\rfloor)].
\end{aligned}
\]

Omit empty pairs and query the others. If all are empty, return \(K\) as a
prime leaf. Otherwise, keep \(J_j\) fixed and bisect the \(x\)-interval of
one nonempty box with further emptiness queries. At a singleton \(x\), split
\(K\) into \(x\) and \(K/x\) and recurse.

Maximality of \(M\) gives \(K/16<M\leq K/8\). Every retained box has
endpoints in \([1,M-1]\), and its products obey

\[
 \frac{16K}{17}\leq xy\leq\frac{17K}{16}.
\]

Hence \(xy-K\in(-M,M)\), so within every queried box

\[
 xy\equiv K\pmod M\quad\Longleftrightarrow\quad xy=K.
\]

If a surviving \(K\) is composite, its least prime divisor \(x\) satisfies
\(17\leq x\leq\sqrt K\). The largest index with \(L_j\leq x\) puts \(x\)
in \(I_j\), while \(y=K/x<K/16<M\) lies in \(J_j\). Thus a composite
cannot reach either prime-return branch. Conversely, a nonempty box for a
prime would give a proper exact factorization. Bisection preserves a
nonempty rectangle and therefore ends at a proper exact divisor. Recursion
handles prime powers, repeated factors, and arbitrarily unbalanced
composites without an external primality test.

There are \(O(\log K)\) grid indices. The exact representation
\(L_j=16\cdot17^j/16^j\), all roundings, and every oracle endpoint have
\(O(n)\) bits. Box search and bisection use \(O(n)\) calls per recursive
node. A proper factor tree has fewer than \(n\) prime leaves counted with
multiplicity and therefore \(O(n)\) nodes, giving \(O(n^2)\) calls and
polynomial non-oracle work.

For an always-correct Las Vegas oracle, use fresh independent random bits on
each call. The adaptive query sequence has a deterministic \(O(n^2)\) call
cap. Conditioned on the full history, the next input is fixed and its fresh
randomness has expected cost at most \(T(n)\). Assign zero cost to unused
call positions; conditional expectation and linearity give the displayed
total expected cost. Finitely many almost-surely terminating calls preserve
almost-sure termination.

Independent proof:
experiments/F301_factor_rectangles/RECTANGLE_RECONSTRUCTION.md.
Statement-only input:
experiments/F301_factor_rectangles/RECTANGLE_STATEMENT_ONLY.md.
Statement SHA-256:
e6a68b51f1dc7f0820741b290c916f4318a126d4932ae3a12da3cab28777623d.
Reconstruction SHA-256:
76aea453f4c0e5cbdb759982afe78939d0c6dfcc7c7fcc7cec0999e700975fa7.

The numerical reference oracle and finite F301 tests are evidence for the
implementation only. No efficient `Empty` oracle, rational-filter identity,
or adjacent F298--F300 candidate is promoted here.

## P238 -- Global dyadic inverse moments modulo M squared have a polynomial-bit residue constructor

**Status:** promoted after fresh statement-only Sol reconstruction and root
verification of the precision schedule, formal division, and full-input
\(N\) handling.

**Scope:** the global canonical inverse graph modulo \(M=2^k\), the carry
moments \(Q_j\bmod M\), and all mixed power moments \(S_{ab}\bmod M^2\)
through a requested degree bank. No modulo-\(M^3\) correction bank,
Archimedean approximation, ordinary Cauchy-resolvent evaluator, rectangle
count, or factoring algorithm.

**Statement.** Let \(k\geq3\), \(M=2^k\), \(D\geq0\), and let \(N\) be
any positive odd integer. Put

\[
 U_M=\{1,3,\ldots,M-1\},\qquad
 v_N(u)=Nu^{-1}\bmod M\ \text{in }[1,M-1],
\]

and define, using the full integer \(N\),

\[
 q_u=\frac{u\,v_N(u)-N}{M},\qquad
 Q_j=\sum_{u\in U_M}u^jq_u,\qquad
 S_{ab}=\sum_{u\in U_M}u^av_N(u)^b.
\]

There is a deterministic algorithm that computes

\[
 Q_j\bmod M\quad(0\leq j\leq D),\qquad
 S_{ab}\bmod M^2\quad(0\leq a,b\leq D)
\]

in bit complexity polynomial in \(k\), the numerical degree bound \(D\),
and the ordinary binary length of \(N\). It does not enumerate \(U_M\) or
the inverse graph, receive factors of \(N\), or receive a numerical-length
unit list.

The construction also includes the following uniform primitive: for every
precision \(P\geq1\),

\[
 \Pi_M=\prod_{u\in U_M}u\pmod {2^P}
\]

is computable in bit complexity polynomial in \(k\) and \(P\), without
enumerating \(U_M\).

**Proof.** Write \(h=M/2\). For \(s\geq3\) and \(r\geq1\), put

\[
 H_r^{(s)}=\sum_{u\in U_{2^s}}u^{-r}\in\mathbb Z_2.
\]

The decomposition
\(U_{2^{s+1}}=U_{2^s}\mathbin{\dot\cup}(U_{2^s}+2^s)\) gives

\[
 H_r^{(s+1)}
 =2H_r^{(s)}
 +\sum_{t\geq1}(-1)^t
   {r+t-1\choose t}2^{st}H_{r+t}^{(s)}. \tag{1}
\]

Modulo \(2^W\), only
\(t\leq\lfloor(W-1)/s\rfloor\) contributes. To request indices through
\(R\) at level \(s\), set \(R_s=R\) and, backwards,

\[
 R_\ell=R_{\ell+1}+\lfloor(W-1)/\ell\rfloor
 \quad(\ell=s-1,\ldots,3).
\]

Compute the four base inverses in \(U_8\) modulo \(2^W\), their powers
through \(R_3\), and apply (1) forwards. The largest required index is
polynomial in \(s,R,W\), so this computes all requested inverse power sums
without listing a growing unit set.

For power sums \(p_j=\sum_i x_i^j\) and elementary symmetric functions
\(e_t\), Newton's identity is

\[
 t e_t=\sum_{j=1}^t(-1)^{j-1}e_{t-j}p_j. \tag{2}
\]

To obtain \(e_1,\ldots,e_T\bmod2^L\), compute the \(p_j\) modulo
\(2^{L+\nu_2(T!)}\), and compute \(e_t\) at precision

\[
 \lambda_t=L+\nu_2(T!/t!).
\]

At step \(t\), the right side of (2) is known modulo
\(2^{\lambda_t+\nu_2(t)}=2^{\lambda_{t-1}}\). Divide its canonical
representative exactly by the 2-part of \(t\), then invert only the odd
part modulo \(2^{\lambda_t}\). Thus no even integer is inverted in a
power-of-two residue ring.

Let \(G_s=\prod_{u\in U_{2^s}}u\). The same two-lift decomposition gives

\[
 G_{s+1}=G_s^2C_s,\qquad
 C_s=\prod_{u\in U_{2^s}}(1+2^s/u). \tag{3}
\]

If \(e_t^{(s)}\) is the \(t\)-th elementary symmetric function of the
inverse units, then modulo \(2^P\),

\[
 C_s=\sum_{t=0}^{T_s}2^{st}e_t^{(s)},\qquad
 T_s=\min\!\left(2^{s-1},\left\lfloor\frac{P-1}{s}\right\rfloor\right).
 \tag{4}
\]

Equations (1), (2), and (4), at precision
\(P+\nu_2(T_s!)\), compute each correction. Starting from
\(G_3=105\), equation (3) gives \(\Pi_M\bmod2^P\). Here
\(T_s\leq P\), the precision is at most \(2P\), and only polynomially
many modular operations and coefficient bits occur. This proves the unit
product primitive.

For \(n\geq1\), let \(B_j(n)=\sum_{x=0}^{n-1}x^j\). Telescoping gives
the exact integer recurrence

\[
 B_j(n)=
 \frac{n^{j+1}-\sum_{r=0}^{j-1}{j+1\choose r}B_r(n)}{j+1}. \tag{5}
\]

Consequently the ordinary unit power sums are

\[
 A_j=\sum_{u\in U_M}u^j=B_j(M)-2^jB_j(h). \tag{6}
\]

Apply exact integer Newton identities to \(A_j\) to obtain
\(\alpha_t=e_t((u)_{u\in U_M})\) through
\(E=\min(D,h)\). Apply (1) and guarded Newton identities at precision
\(2k+\nu_2(E!)\) to obtain

\[
 \beta_t=e_t((u^{-1})_{u\in U_M})\pmod {M^2}
 \quad(0\leq t\leq E).
\]

Set \(\alpha_0=\beta_0=1\) and both coefficient families to zero beyond
the number \(h\) of units.

Let \(\eta=N^{-1}\pmod {M^2}\), compute
\(\pi=\Pi_M\bmod M^2\), and put

\[
\begin{aligned}
 c&=\pi^2\eta^h\pmod {M^2},\\
 X(T)&=\sum_{t=0}^{E}\beta_tT^t,\\
 Y(T)&=\sum_{t=0}^{E}\alpha_t\eta^tT^t.
\end{aligned}
\]

Since \(Y(0)=1\), formal division is valid in
\(\mathbb Z_2[[T]]\). For

\[
 R(T)=
 \Pi_M\frac{\prod_{u\in U_M}(T+u)}
              {\prod_{u\in U_M}(N+Tu)}
 \equiv\frac{cX(T)}{Y(T)}\pmod {M^2},
\]

its coefficients \(r_n=[T^n]R(T)\) through \(D\) satisfy

\[
 r_0=c,\qquad
 r_n=c\beta_n-
 \sum_{t=1}^{\min(n,E)}\alpha_t\eta^t r_{n-t}
 \pmod {M^2}. \tag{7}
\]

This remains a polynomial-size truncated computation when \(D>h\).

The map \(u\mapsto v_N(u)\) permutes \(U_M\) and is an involution. The
definition of \(q_u\) gives

\[
 1+\frac{Mq_u}{N+Tu}
 =\frac{u(T+v_N(u))}{N+Tu}.
\]

Multiplying over \(U_M\) proves the displayed product formula for \(R\).
Modulo \(M^2\), products of two correction terms vanish, hence

\[
 R(T)-1\equiv
 M\sum_{u\in U_M}\frac{q_u}{N+Tu}\pmod {M^2}. \tag{8}
\]

Let \(d_0=(r_0-1)\bmod M^2\), and let \(d_j=r_j\) for \(j\geq1\),
using representatives in \([0,M^2-1]\). Coefficient extraction in (8)
shows that each \(d_j\) is divisible by \(M\) and gives

\[
 Q_j=(-1)^jN^{j+1}(d_j/M)\pmod M. \tag{9}
\]

This is exact integer division, not inversion of \(M\).

For \(a\geq b\geq1\), put \(j=a-b\). The identity
\(uv_N(u)=N+Mq_u\) gives

\[
 S_{ab}=N^bA_j+bMN^{b-1}Q_j\pmod {M^2}. \tag{10}
\]

The involution gives \(S_{ab}=S_{ba}\), while an exponent zero gives
\(S_{a0}=A_a\) and \(S_{0b}=A_b\). This includes \(D=0\).

The full \(N\) in \(q_u\) is essential: replacing \(N\) by \(N-cM\)
leaves \(v_N(u)\) and every \(S_{ab}\) unchanged, but changes \(q_u\)
by \(c\) and \(Q_j\) by \(cA_j\). The construction retains \(N\bmod
M^2\), which is sufficient for \(Q_j\bmod M\); it does not silently
replace the carry definition by one using only \(N\bmod M\).

The exact ordinary coefficients have \(O(Dk)\)-bit size. The reciprocal
precision is at most \(2k+E\), the inverse-sum index bank is polynomial in
\(k,D\), and (7) and (10) use \(O(D^2)\) modular operations. The exponent
\(h=2^{k-1}\) has \(k\) bits. Reducing the binary input \(N\) modulo the
needed powers of two, inversion, and modular powering all have polynomial
bit cost. This proves the stated uniform bound.

Independent proof:
experiments/F303_global_moment_precision/MOMENT_RECONSTRUCTION.md.
Statement-only input:
experiments/F303_global_moment_precision/MOMENT_STATEMENT_ONLY.md.
Input SHA-256:
568441f2eebe3f519c356a4d0fe3cf43ac7243ede4a0e229f18683862f1f5b95.
Reconstruction SHA-256:
604a19e1cda14356b13e6e7bdc704e7a85fc3fc448fcb842c2ed6ed08a555450.

Author derivation and finite evidence:
experiments/F303_global_moment_precision/REPORT.md, UNIT_PRODUCTS.md,
moment_precision.py, moment_precision.json, and moment_precision.log.

Andreica, *The Scientific World Journal* (2013), Article 751358,
already gives a non-enumerative power-sum/Newton algorithm for the odd
unit product in its stated precision range. Neither the unit-product
primitive nor this mixed-moment construction carries a novelty claim.
The closed-form modulo-\(M^2\) refinement, higher-precision carry
corrections, exponent-derivative identities, and finite Mahler evidence
are not promoted by this record.

## P239 -- Shifted binomial carry sums recover exact inverse-graph rectangle counts

**Status:** promoted after fresh statement-only Sol reconstruction and root
verification of the algebra, endpoints, retained precision, and conditional
cost.

**Scope:** an exact reduction from arbitrary canonical inverse-graph rectangle
counts to four shifted binomial-carry sums modulo \(M\). No uniform efficient
evaluator for those sums, independent rectangle oracle, or factoring algorithm
is supplied.

**Statement.** Let \(k\geq2\), \(M=2^k\), and let \(N\) be any positive odd
integer. For each odd \(u\in[0,M)\), let

\[
 v(u)=Nu^{-1}\bmod M
\]

be the canonical representative in \([0,M)\). For cut coordinates
\(c,d\in[0,M]\), define

\[
\begin{aligned}
 x_c(u)&=u+M\mathbf 1_{u<c},\\
 y_d(u)&=v(u)+M\mathbf 1_{v(u)<d},\\
 q_{cd}(u)&=\frac{x_c(u)y_d(u)-N}{M},\\
 B(c,d)&=\sum_{\substack{0\leq u<M\\u\ {\rm odd}}}
          \binom{q_{cd}(u)}2\pmod M.
\end{aligned}
\]

The full integer \(N\) defines the carry, which may be negative. Each
\(\binom q2=q(q-1)/2\) is an exact integer, including for negative \(q\).

For arbitrary integer cuts

\[
 0\leq a\leq b\leq M,\qquad 0\leq c\leq d\leq M,
\]

let

\[
 C=\#\{u\ {\rm odd}:a\leq u<b,\ c\leq v(u)<d\}.
\]

Then \(C\) is the canonical residue modulo \(M\) of

\[
 \left(N-\frac M2\right)^{-1}
 \bigl(B(b,d)-B(a,d)-B(b,c)+B(a,c)\bigr). \tag{1}
\]

This includes empty intervals and endpoints \(0\) and \(M\).

**Proof.** Put

\[
 r(u)=\frac{uv(u)-N}{M},\quad
 A_s=\mathbf 1_{u<s},\quad D_t=\mathbf 1_{v(u)<t}.
\]

Integer expansion of the shifted product gives

\[
 q_{st}(u)=r(u)+uD_t+v(u)A_s+MA_sD_t. \tag{2}
\]

Take the pointwise mixed difference of \(f(q)=\binom q2\) at
\((b,d),(a,d),(b,c),(a,c)\). If \(u\notin[a,b)\) or
\(v(u)\notin[c,d)\), the corresponding indicator does not change and the
mixed difference is zero. If the point lies in both intervals, the four
carries are

\[
 r,\quad r+v,\quad r+u,\quad r+u+v+M.
\]

The integer identities

\[
 f(z+M)-f(z)=Mz+\frac{M(M-1)}2
\]

and

\[
 f(r+u+v)-f(r+u)-f(r+v)+f(r)=uv
\]

show that the mixed difference at this point is

\[
 uv+M(r+u+v)+\frac{M(M-1)}2
 \equiv N-\frac M2\pmod M. \tag{3}
\]

Summing (3) proves the congruence in (1). Since \(k\geq2\), \(M/2\) is
even, so \(N-M/2\) is odd and invertible modulo \(M\). There are \(M/2\)
odd residues, hence \(0\leq C\leq M/2<M\); the recovered canonical residue
is therefore the exact count.

At cut zero the relevant indicator is always zero, and at cut \(M\) it is
always one. Thus (2) also proves the endpoint and empty-interval cases
without a correction.

**Retained precision.** In general \(f(q)\bmod M\) is determined by
\(q\bmod2M\), but not by \(q\bmod M\), because

\[
 f(q+M)-f(q)\equiv M/2\pmod M,\qquad
 f(q+2M)-f(q)\equiv0\pmod M.
\]

Consequently a modular implementation must retain
\(x_cy_d-N\bmod2M^2\) before the exact division by \(M\). Equivalently,
\(N\bmod2M^2\) suffices to evaluate a summand modulo \(M\), but
\(N\bmod M\) does not. The mathematical carry definition continues to use
the full \(N\). The four completed \(B\)-values themselves need only be
returned modulo \(M\).

**Conditional consequence.** Suppose a uniform deterministic or classical
Las Vegas algorithm evaluates every required \(B(c,d)\bmod M\) in expected
bit cost \(T(n)\) on \(O(n)\)-bit inputs, where \(T\) is nondecreasing.
Equation (1) implements one exact rectangle count and its emptiness test
with four calls and polynomial additional bit work. Fresh random bits give
the same expected bound for adaptive Las Vegas calls.

Using P237's public dyadic rectangle interface, complete all-input factoring
then has expected bit cost

\[
 O\!\left(n^2T(n)+\operatorname{poly}(n)\right),
 \qquad n=\lceil\log_2(N+1)\rceil.
\]

A quasipolynomial \(T\) would therefore suffice. This conclusion is
conditional: neither this record nor its finite reference program constructs
such an evaluator.

Independent proof:
experiments/F306_shifted_carry_counts/RECONSTRUCTION.md.
Statement-only input:
experiments/F306_shifted_carry_counts/STATEMENT_ONLY.md.
Input SHA-256:
463bec85607b7bbaac1dcdb04c79b4210041285288c2b79603d2dbaade827e2a.
Reconstruction SHA-256:
36851132bf7d7ce095fac6979f36482c47b3ddc41645c909c1eb9b2e8444f187.

Author derivation and finite evidence:
experiments/F306_shifted_carry_counts/REPORT.md, pilot.py, output.json,
run.log, status.json, and RESOURCE.md. The retained checks cover 1,200
general rectangles, 175 public factor rectangles, and 21 complete reference
inputs using 620 \(B\)-calls. The reference evaluator enumerates graph
points; these checks support the identity but do not supply the missing
asymptotic evaluator. No novelty claim is made.

## P240 -- Canonical Möbius mixed and carry moments have a polynomial-bit constructor

**Status:** promoted after fresh statement-only reconstruction and root
review of the scope, precision guards, and full-input convention.

**Scope:** one canonical Möbius permutation modulo a power of two. No fast
sum over a family of maps, shifted-window statistic, rectangle count, or
factoring algorithm is supplied.

**Statement.** Let \(s\geq1\), \(L=2^s\), let \(A,B\) be odd integers,
let \(C\) be a positive even integer, and let \(n\) be any integer. For
\(0\leq x<L\), put

\[
 D(x)=B+Cx,\quad T(x)=\frac{n-Ax}{D(x)}\in\mathbb Z_2,
 \quad y(x)=T(x)\bmod L\text{ in }[0,L),
\]

and, using the full integer \(n\),

\[
 q_x=\frac{D(x)y(x)-(n-Ax)}L.
\]

For every numerical \(d\geq0\), a uniform deterministic algorithm computes

\[
 S_{ij}=\sum_{0\leq x<L}x^iy(x)^j\pmod {L^2}
 \quad(0\leq i,j\leq d)
\]

and

\[
 Q_j=\sum_{0\leq x<L}\frac{q_xT(x)^j}{D(x)}\pmod L
 \quad(0\leq j\leq d)
\]

in bit complexity polynomial in \(s\), numerical \(d\), and the binary
lengths of \(A,B,C,n\). It does not enumerate the \(L\) arguments or their
images and receives no factors, permutation list, or precision advice.

**Construction.** Cross multiplication shows that equality of two
\(T(x)\bmod L\) values forces
\((AB+Cn)(x_2-x_1)=0\bmod L\). The coefficient is odd, so \(y\) permutes
\(Y=\{0,\ldots,L-1\}\). With \(u_x=q_x/D(x)\), exactly

\[
 y(x)=T(x)+Lu_x. \tag{1}
\]

All needed ordinary sums are computed from

\[
 \sum_{x=0}^{L-1}x^m=
 \sum_{r=0}^m
 \left\{\begin{matrix}m\\r\end{matrix}\right\}r!\binom L{r+1}. \tag{2}
\]

At precision \(P\), expand \((B+Cx)^{-j}\) as a negative-binomial
series. If \(v\) is the 2-adic valuation of \(C\), every term after
\(\lfloor(P-1)/v\rfloor\) vanishes. Expanding \((n-Ax)^j\) and applying
(2) computes every required sum \(\sum x^iT(x)^j\) without enumerating
\(x\).

For the carry bank, use

\[
 J=\max\left(d,2d-1+\left\lfloor\frac{s-1}{v}\right\rfloor\right),
 \qquad E=\min(J+1,L).
\]

Compute the elementary symmetric coefficients of \((T(x))_x\) from its
power sums at precision \(2s+\nu_2(E!)\). At Newton step \(k\), retain the
numerator through precision
\(2s+\nu_2(E!)-\nu_2((k-1)!)\), divide exactly by the 2-part of \(k\), and
invert only its odd part. Every coefficient remains known modulo \(L^2\).

Let \(e_m^Y\) and \(e_m^T\) denote the two symmetric banks and set

\[
 H_m=(e_{m+1}^Y-e_{m+1}^T)/L\pmod L
\]

for \(m<L\), with \(H_m=0\) afterward. This division is guarded by the
known \(L^2\) residue and exact divisibility. Expanding
\(e_m(Y\setminus\{y\})\) gives a unit-triangular recurrence for
\(U_m=\sum_xu_xy(x)^m\bmod L\). Since \(T(x)=y(x)\bmod L\), these are
the required \(Q_m\). The recurrence continues through \(J\), including
when \(J\geq L\), without listing roots.

Finally solve \(x=(n-BT)/(A+CT)\). The denominator is odd, and its
binomial expansion modulo \(L\) has degree at most
\(i+j-1+\lfloor(s-1)/v\rfloor\). Thus the carry bank computes
\(W_{i,j-1}=\sum_xx^iu_xT(x)^{j-1}\bmod L\). Equation (1) gives

\[
 S_{i0}=\sum_xx^i,\qquad
 S_{ij}=\sum_xx^iT(x)^j+jLW_{i,j-1}\pmod {L^2}.
\]

All even divisions are exact integer divisions with the displayed guards.
The case \(d=0\) returns \(Q_0\) and \(S_{00}=L\); it also preserves the
convention \(0^0=1\). Every index and precision is \(O(s+d)\), which gives
the stated polynomial bit bound. The bound is in numerical \(d\), not its
binary length.

Complete independent proof:
experiments/F304_guarded_digit_circuits/MOBIUS_RECONSTRUCTION.md.
Statement-only input:
experiments/F304_guarded_digit_circuits/MOBIUS_STATEMENT_ONLY.md.
Input SHA-256:
19599f6d20c1fac30bfeda265dd395dcdda6d81d1786c1dacb8dd8b1f4b3165c.
Reconstruction SHA-256:
bc9ef597891d4b61df699975fdd1abbc3769b4a203c928397e8ada490dd762d0.

Author derivation and finite evidence:
experiments/F304_guarded_digit_circuits/ERROR_BANK.md,
experiments/F304_guarded_digit_circuits/MOBIUS_BANK.py,
experiments/F304_guarded_digit_circuits/MOBIUS_BANK_output.json,
experiments/F304_guarded_digit_circuits/MOBIUS_BANK_run.log, and the
separate edge and large-pilot artifacts. The repaired \(d=0\) interface
passed 32 exact requested-output checks. The preserved \(s=33,65\) pilot
is a valid generic one-map run, but not an original patch with
\(M=2^s\);
experiments/F304_guarded_digit_circuits/MOBIUS_LARGE_PILOT_SCOPE.md
records that correction. The
correctly coupled original case used \(M=2^{65}\), \(L=2^{64}\),
\(s=64\), and \(N=9M+1\). It ran in 0.529 seconds at 18,087,936 bytes
peak RSS and matched the universal row and column marginals. Its large
mixed outputs were not independently verified. No novelty claim is made
for the elementary power-sum or Newton machinery.

## P241 -- Sign-inversion quadratic corrections need only two fewer value bits

**Status:** promoted after fresh statement-only reconstruction and root
review of every exceptional orbit, the \(p=3\) boundary, negative values,
and arbitrary odd \(\epsilon\).

**Statement.** Let \(M=2^k\) with \(k\geq3\), let \(\epsilon\) be any odd
integer, and let \(U\) be the odd canonical residues modulo \(M\). Define
\[
 s(w)=M-w,\qquad i(w)=\epsilon w^{-1}\bmod M,
\]
and, for integer-valued \(f\) on \(U\),
\[
 Q_\epsilon(f)=\sum_{w\in U}
 \bigl(f(w)f(i(w))-f(w)^2\bigr).
\]
For every integer \(p\geq3\), if
\(r(s(w))=-r(w)\), \(g(s(w))=-g(w)\), and
\(r(w)\equiv g(w)\pmod {2^{p-2}}\) pointwise, then
\[
 Q_\epsilon(r)\equiv Q_\epsilon(g)\pmod {2^p}. \tag{1}
\]
This includes roots of both \(\epsilon\) and \(-\epsilon\) modulo \(M\).

For canonical odd \(0<A<M\), put
\(f(w)=\lfloor Aw/M\rfloor\), \(h=(A-1)/2\), and
\(r=f-h\). On \(w<M/2\), let \(g(w)\) be the canonical residue of
\(r(w)\) modulo \(2^{p-2}\), and extend by \(g(M-w)=-g(w)\). Then
\[
 H_\epsilon(f)\equiv U_2(f)+H_\epsilon(g)-U_2(g)
 \pmod {2^p}, \tag{2}
\]
where \(H_\epsilon(x)=\sum_wx(w)x(i(w))\) and
\(U_2(x)=\sum_wx(w)^2\). At \(p=3\), \(g\) takes values in
\(\{-1,0,1\}\).

**Proof.** The commuting involutions \(s\) and \(i\) split \(U\) into
inversion-fixed sign pairs, sign-inversion pairs, and four-point orbits.
For a sign-antisymmetric function with representative values \(a,b\),
their respective contributions to \(Q_\epsilon\) are
\[
 0,\qquad -4a^2,\qquad -2(a-b)^2. \tag{3}
\]
Put \(q=2^{p-2}\). On a sign-inversion pair, replacing \(a\) by a
congruent value modulo \(q\) changes (3) by a multiple of \(4q\). On a
four-point orbit, the two differences are congruent modulo the even number
\(q\), so their sum is even; their squared difference is therefore a
multiple of \(2q\), and the last expression in (3) changes by a multiple
of \(4q=2^p\). This proves (1), including \(p=3\).

The identity \(f(M-w)=A-1-f(w)\) makes \(r=f-h\)
sign-antisymmetric, and the stated lower-half construction makes \(g\)
pointwise congruent to \(r\). Finally, translating a function by a constant
does not change \(Q_\epsilon\), because \(i\) is a permutation. Equation
(2) follows by applying (1) and expanding \(Q_\epsilon\).

This result compresses only the value alphabet. It does not reduce the
inverse-graph modulus, the number of summands, or the requested output
precision, and it does not evaluate \(H_\epsilon(g)\) or give a runtime or
factoring bound.

Complete independent proof:
experiments/F312_orbit_precision/RECONSTRUCTION.md.
Statement-only input:
experiments/F312_orbit_precision/STATEMENT_ONLY.md.
Input SHA-256:
5214d1c68cd48eeeff1e746974d2c9600535c43ea512bf9da5b35d14f5303878.
Reconstruction SHA-256:
44b3c0853041be1c75cb82a8c35de08f7872d61f15b7bc7a06a2d8c1e08d83b6.

## P242 -- Canonical unshifted cross and transport sums modulo four have polynomial-bit constructors

**Status:** promoted after fresh statement-only reconstruction and root
comparison with the author derivation. The formulas, parity guards, raw
corrections, and stated cost matched without a gap.

**Scope:** canonical \(K(A,B)\bmod4\), canonical \(T(N)\bmod4\), and the
stated raw-input corrections. No shifted sum, sharp cut, higher-precision
carry, rectangle count, or factoring algorithm is supplied.

Let \(M=2^k\), \(k\geq3\), and \(L=M/4\). For odd canonical \(w\), let
\(u(w)=w^{-1}\bmod M\),
\(q(w)=(u(w)w-1)/M\), and \(\mu(w)=u(w)q(w)\). Define
\[
 K(A,B)=\sum_w\left\lfloor\frac{Aw}{M}\right\rfloor
                 \left\lfloor\frac{Bu(w)}M\right\rfloor,
 \qquad
 T(N)=\sum_w\mu(w)\left\lfloor\frac{Nw}{M}\right\rfloor.
\]

Write every canonical odd \(A\) uniquely as
\(A=(-1)^{\sigma_A}5^a\bmod M\), with \(0\leq a<L\). Put
\[
 \eta_j=\left\lfloor\frac{5^j\bmod2M}{M}\right\rfloor,
 \qquad
 \gamma_r=\begin{cases}
 0,&r\text{ odd},\\
 \eta_{r/2}+\eta_{r/2+L/2},&r\text{ even},
 \end{cases}
 \pmod2,
\]
where indices are reduced modulo \(L\). For canonical \(A,B\), with
exponents \(a,b\), \(K(A,B)\) is even and
\[
\begin{aligned}
 \frac{K(A,B)}2={}&\max(0,a+b-L+1)+b\eta_a+a\eta_b\\
 &+\gamma_0+\gamma_a+\gamma_b+\gamma_{a+b}
   +\sigma_Ba+\sigma_Ab \pmod2. \tag{1}
\end{aligned}
\]
For positive raw \(A=A_0+M\alpha\) and \(B=B_0+M\beta\), add
\(\alpha b+\beta a\pmod2\) to (1). There is no
\(\alpha\beta\) term.

For canonical odd \(N=(-1)^\sigma5^a\bmod M\), let
\(C=5^a\bmod2M\) in \([1,2M)\), and define the ordinary integer
\[
 D=\sum_{j=0}^{L-1}\left\lfloor\frac{C(1+4j)}M\right\rfloor
 -2\sum_{j=0}^{L-1}\left\lfloor\frac{C(1+4j)}{2M}\right\rfloor.
\]
Then \(T(N)\) and \(D-a\) are even, and
\[
 \frac{T(N)}{2}=\sigma+\gamma_0+\gamma_a+\eta_a+\frac{D-a}{2}\pmod2. \tag{2}
\]

For the optional positive raw correction \(N=N_0+M\ell\), P238 supplies
\(Q_0=\sum_wq(w)\bmod4\), and
\[
 T(N)=T(N_0)+\ell Q_0\pmod4. \tag{3}
\]
Sign pairing proves that \(Q_0\) is even, so division of the correction by
two uses its residue modulo four and is an exact integer operation.

The proof extracts the canonical multiplication carry from the high bit of
\(5^j\bmod2M\). Sign pairing reduces \(K/2\) to one cyclic binary
correlation; the involution \(j\mapsto r-j\) leaves exactly the displayed
\(\gamma_r\) terms. For \(T/2\), the same pairing gives an explicit
\(q_j\) word. Its section correlation and prefix term combine into the
ordinary carry count \(D\), with the parity identity \(D\equiv a\pmod2\).

Coordinates are recovered one bit at a time with \(O(k)\) modular
multiplications. A constant number of \(\eta\) and \(\gamma\) values use
binary modular exponentiation, and the two sums defining \(D\) use the
Euclidean floor-sum recurrence. No unit group is enumerated. With
schoolbook arithmetic, the conservative bit cost is \(O(k^3)\), enlarged
by the raw input bit lengths when present, with polynomial space.

Complete independent proof:
experiments/F313_group_log_cocycle/RECONSTRUCTION.md.
Statement-only input:
experiments/F313_group_log_cocycle/STATEMENT_ONLY.md.
Input SHA-256:
48af5e43fad1e06e651bc627d3e20ddfe10ca633c92c0b49d233bea4c63eaa1b.
Reconstruction SHA-256:
71fe7dda465f38215d6ebe1756fd46df7d374948d26c2e72d774540906f42e15.

Author derivation and finite evidence:
experiments/F313_group_log_cocycle/REPORT.md,
experiments/F313_group_log_cocycle/pilot.py,
experiments/F313_group_log_cocycle/pilot.json,
experiments/F313_group_log_cocycle/pilot.log,
experiments/F313_group_log_cocycle/transport_bit.py,
experiments/F313_group_log_cocycle/transport_bit.json, and
experiments/F313_group_log_cocycle/transport_bit.log.
The focused nondependency comparison is retained in
experiments/F313_group_log_cocycle/SOURCE_LEADS.md.

## P243 -- The fixed inverse half-box count modulo eight has a polynomial-bit constructor

**Status:** promoted after fresh statement-only reconstruction and root
review of the full-input correction, negative carries, parity constants,
division guards, finite controls, and uniform cost.

**Scope:** one fixed half/half box on the inverse graph modulo \(2R\), returned
modulo eight for every positive odd full input. No arbitrary endpoint,
exact count, emptiness oracle, or factoring algorithm is supplied.

Let \(R=2^k\), \(k\geq3\), and \(\phi=R/2\). For positive odd \(N\), define
\[
 C(N,2R)=\#\{\,u\text{ odd}:1\leq u<R,\quad
       N/u\bmod2R\in[1,R)\,\}.
\]
Write \(N=\nu+R\ell\), where \(1\leq\nu<R\) is odd. For odd \(u<R\), put
\[
 v_u=\nu/u\bmod R,\qquad q_N(u)=\frac{uv_u-N}{R},
\]
and define the exact integer sums
\[
 H_N=\sum_uq_N(u),\quad
 B_N=\sum_u\binom{q_N(u)}2,\quad
 A_N=\sum_u\binom{q_N(u)}3.
\]
The binomial polynomials use their all-integer values, including at negative
\(q_N(u)\).

The lift of \(v_u\) to the inverse graph modulo \(2R\) lies below \(R\)
exactly when \(q_N(u)\) is even. The all-integer congruence
\[
 \mathbf1_{q\ {\rm even}}
 =1-q+2\binom q2-4\binom q3\pmod8
\]
therefore gives
\[
 C(N,2R)=\phi-H_N+2B_N-4A_N\pmod8. \tag{1}
\]
Sign/inversion orbits give the universal constants
\[
 H_1=2\pmod4,\qquad B_1=2\pmod4,
\]
and fixed points of \(u\mapsto\nu/u\) give
\[
 A_N=\mathbf1_{N\equiv1\ ({\rm mod}\ 8)}\pmod2. \tag{2}
\]
The fixed-point proof includes the \(k=3\) boundary and negative carries.

Let \(f(w)=\lfloor\nu w/R\rfloor\) and
\[
 J_\nu=\sum_{w\ {\rm odd}<R}\bigl(f(w)^2+w f(w)\bigr)\pmod8.
\]
Every summand is even. Divide the even canonical residue by two in the
integers, call P242 for \(T_R(\nu)\bmod4\), and set
\[
 b_\nu=2+\nu(\nu-1)+J_\nu/2-\nu T_R(\nu)\pmod4. \tag{3}
\]
Then \(b_\nu=B_\nu\bmod4\), and exact binomial translation gives
\[
 B_N=b_\nu-\ell H_N\pmod4. \tag{4}
\]
The moments in \(J_\nu\) are ordinary degree-two floor sums. An explicit
Euclidean recurrence computes \(\sum f\), \(\sum xf\), and \(\sum f^2\)
as exact integers in \(O(k)\) reciprocal steps, including its exact
division by two.

Let \(P_R\) be the product of the positive odd integers below \(R\). P238
computes it modulo \(8R\). Since \(u\mapsto v_u\) permutes the odd residues,
\[
 P_R^2=N^\phi+R N^{\phi-1}H_N\pmod {8R}.
\]
Consequently
\[
 H_N=
 \left(\frac{P_R^2-N^\phi\bmod8R}{R}\right)N^{1-\phi}
 \pmod8. \tag{5}
\]
The numerator is its canonical residue modulo \(8R\) and is divisible by
\(R\) before division. The negative exponent means inversion of the odd
unit \(N^{\phi-1}\bmod8\).

Equations (1)--(5) form the constructor:
\[
 C(N,2R)=\phi-H_N+2(b_\nu-\ell H_N)
          -4\mathbf1_{N\equiv1\ ({\rm mod}\ 8)}\pmod8. \tag{6}
\]
It calls P238 at exactly \(k+3\) bits of precision and P242 once on the
canonical input \(\nu\). Modular exponentiation, input reduction, and the
Euclidean moments have polynomial bit cost in \(k\) and \(\log N\). No
graph point is enumerated.

The exact polarization identity in
experiments/F318_half_box_precision/ENDPOINTS.md reduces an arbitrary
rectangle to four variable diagonal-interval counts with one guard bit.
P243 computes only the single interval \([0,R)\) inside modulus \(2R\);
it does not construct those variable endpoint values. A zero residue
modulo eight also does not certify emptiness.

Complete independent proof:
experiments/F318_half_box_precision/RECONSTRUCTION.md.
Statement-only input:
experiments/F318_half_box_precision/STATEMENT_ONLY.md.
Input SHA-256:
c9c611f8148a365866a08212270731465d2d4244985b8610ffbcfee3be4f2fbe.
Reconstruction SHA-256:
24b44c98684c5915b7bbc353c26b453bc9c64de06c56eb1ee8559720ecb12791.

Author derivation and finite evidence:
experiments/F318_half_box_precision/REPORT.md,
experiments/F318_half_box_precision/ENDPOINTS.md,
experiments/F318_half_box_precision/pilot.py,
experiments/F318_half_box_precision/pilot.json,
experiments/F318_half_box_precision/pilot.log,
experiments/F318_half_box_precision/pilot.status.json, and
experiments/F318_half_box_precision/RESOURCE.md.
The pilot passed 1,173 direct count comparisons through \(R=4096\).
Nonenumerative cases completed through \(R=2^{256}\); that largest case
took 0.585 seconds. Large cases use the proof-based constructor and were
not independently graph-enumerated.

An independent finite verifier retained in
experiments/F318_half_box_precision/blind_check.py and blind_check.log
passed 5,080 full-input cases for \(k=3,\ldots,9\), including large positive
quotients and negative \(q_N\) values. Its source SHA-256 is
b762b56831dbfa7233ccdc67a0e243d24d4451bf47e466818d1d2bb64a167768;
the log SHA-256 is
c545e97b9911d5a97311e009ae62ffa84b140537e95e3b722a90d3166a3d0cd7.
