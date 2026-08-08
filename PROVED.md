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
