# Inspiring Points

## A

### A1. Smoothness-free square-relation generation

Use mechanisms such as Reed–Solomon power sums, list decoding, and low-dimensional square-class encoding to recover, directly from \(\mathrm{poly}(\log N)\) samples,

\[
X^2\equiv Y^2\pmod N,\qquad X\not\equiv\pm Y.
\]

The core goal is to bypass smooth-number probability completely.

### A2. A CRT separator from modular forms／Hecke operators

Find a modular form, Hecke trace, Brandt matrix, or automorphic invariant that can be computed in \(\mathrm{poly}(\log N)\) time without factoring \(N\), but whose local behavior differs in the two components of

\[
\mathbb Z/N\mathbb Z\simeq \mathbb F_p\times\mathbb F_q.
\]

Use a determinant, kernel, or eigenvalue collision to produce a zero divisor, and then take a gcd.

### A3. p-adic Frobenius rank-drop

Automatically search for families of elliptic curves, Abelian varieties, motives, or algebraic varieties such that a Frobenius/Hasse–Witt/crystalline operator has different ranks over \(p\) and \(q\) with constant probability. If the corresponding minor can be computed modulo \(N\) in polynomial time, it leaks a factor.

### A4. Inconsistent isogeny neighbors

Construct CM curves or special Shimura data over \(\mathbb Z/N\mathbb Z\), and look for a “canonical isogeny neighbor” that can be computed in polynomial time. If the two CRT sides select different branches, a modular-polynomial evaluation or a coordinate difference becomes a zero divisor.

### A5. Classicalizing Shor’s special order-finding problem

Do not try to simulate general quantum computation. Study only the highly structured periodic states produced by modular multiplication. Search for:

- an automorphic trace formula;
- sparse Fourier reconstruction;
- tensor-network compressibility;
- algebraic reconstruction of exponential sums.

The goal is to recover \(\operatorname{ord}_N(a)\) in classical polynomial time.

### A6. Low-complexity idempotent extraction

Directly search for a polynomial-time algorithm that constructs

\[
e^2=e\pmod N,\qquad e\notin\{0,1\}.
\]

A nontrivial idempotent is equivalent to a factorization. AI can search for new structures in modular symbols, class groups, étale algebras, resultants, or matrix algebras that can produce such an \(e\).

### A7. Structured CVP → factoring, rather than general CVP

Encode a factor as the closest vector in a special class of lattices, while forcing that lattice to belong to a class for which a polynomial-time algorithm already exists or may exist, such as circulant lattices, bounded-treewidth lattices, or lattices of low displacement rank. The point is not to reduce factoring to general CVP, but to discover a new lattice class that “expresses factoring while remaining solvable.”

### A8. An algebraic-reconstruction factoring gadget

Following the research style of the recent CVP work, search for a completely new chain:

\[
\text{factor} \rightarrow \text{finite-field power sums}
\rightarrow \text{codeword / polynomial reconstruction}
\rightarrow \text{zero divisor}.
\]

The AI’s task is to enumerate intermediate gadgets and automatically test which gadgets simultaneously satisfy “generatable, decodable, and provably successful with inverse-polynomial probability.”

## B

The common insight offered by GI and Shor is: do not continue optimizing sieve methods; instead, look for a “hidden-symmetry object” that can be operated on at size \(\mathrm{poly}(\log N)\). Babai’s key tools are local certificates, canonical partitioning, and stabilizer recursion; Shor turns factorization into a hidden period in a cyclic group; Kuperberg shows how to progressively amplify a hidden frequency by combining representations; Kayal–Saxena give a direct bridge between integer factorization and the search for automorphisms of finite rings. OpenAI’s CVP work also suggests replacing item-by-item search with a small number of power sums plus algebraic reconstruction.

### B1. A Babai-style treatment of fixed-degree ring automorphisms

For Kayal–Saxena-type rings

\[
R_N=\mathbb Z_N[x]/(f(x)),\qquad \deg f=3,4,
\]

search for special families of \(f\) such that the action of \(\operatorname{Aut}(R_N)\) has a very small base or avoids the Johnson-type obstruction in GI. Use local certificates to find a nontrivial automorphism, and then extract a zero divisor.

### B2. Galois cycle-type CRT separator

Randomly choose low-degree polynomials \(f_t\) with \(S_k\) or \(A_k\) monodromy. Their Frobenius cycle types modulo \(p\) and modulo \(q\) will usually differ; the goal is to detect that difference over \(\mathbb Z_N\) through a resolvent, subresultant, or rank certificate, and then take the gcd of the relevant minor with \(N\). The ideal parameter is \(k=O(\log\log N)\).

### B3. Compressed Pollard-rho discriminant

For an algebraic dynamical system \(F\), consider

\[
D_m=\prod_{0\le i<j<m}\bigl(F^i(x)-F^j(x)\bigr).
\]

Ordinary Pollard rho explicitly takes \(m\approx\sqrt p\) steps. The new goal is to find an \(F\) with an addition law such that \(D_m\) can be computed by a recursive circuit of size \(\mathrm{poly}(\log m,\log N)\). Candidates include Chebyshev maps, Lattès maps, isogeny endomorphisms, and special linear recurrences.

### B4. Power-sum reconstruction of Shor’s spectrum

Let \(U_a\) be the multiplication operator \(x\mapsto ax\bmod N\). Find easily described probes \(v_j\) such that the spectral measure has only \(\mathrm{poly}(\log N)\) effective frequencies and

\[
\langle v_j,U_a^k v_j\rangle
\]

can be computed quickly classically. Then use Prony, Padé, or Reed–Solomon power sums to reconstruct the common denominator \(r\) of the eigenphases. This is the most direct “transfer of the CVP methodology.”

### B5. Low-dimensional separating representations

Search for a family of representations computable without factoring \(N\),

\[
\rho_j:(\mathbb Z/N\mathbb Z)^\times
\longrightarrow GL_{d_j}(K_j),
\qquad d_j=\mathrm{poly}(\log N),
\]

such that the orders of the images, their minimal polynomials, or their eigenvalues jointly determine enough of \(r_p\) and \(r_q\). Candidate sources include small étale algebras, quotients of modular symbols, torsion of algebraic groups, and modules of finite-ring automorphisms.

### B6. A classical Kuperberg phase sieve

Construct classically computable “phase carriers,” each of which gives a noisy linear congruence about \(r_p\) or \(r_q\), together with a combining operation

\[
C_u,C_v\longmapsto C_{u\pm v}.
\]

As in the Kuperberg sieve, eliminate low bits round by round until exact local order information is obtained. Candidate carriers are higher-power residue symbols, Gauss/Jacobi sums, and extension-ring traces.

### B7. A nonabelian lift of Shor’s HSP

Embed the hidden period \(r\mathbb Z\) into the stabilizer of an affine group or semidirect product so that it acts on only \(\mathrm{poly}(\log N)\) algebraic test objects. If the action has a small base, it may be possible to recover the hidden subgroup classically using a Schreier–Sims/Luks-type stabilizer chain.

### B8. Symbolic Weisfeiler–Leman over the CRT

Do not run WL on all \(N\) residue classes. Instead, build a coherent configuration on a small number of symbolic objects—roots, ideals, orbit fragments, and low-degree polynomials. Define colors using traces, ranks, resultants, and multiplication identities. Search for a constant \(k\) such that \(k\)-WL stabilizes to different configurations modulo \(p\) and modulo \(q\); the determinant of a color certificate then yields a factor.

### B9. Higher-power residue symbols as individualization

GI breaks symmetry by fixing a small number of vertices; here, use \(\ell\)-th power residue symbols, Hilbert symbols, or cyclotomic twists to break the symmetry between the two local components \(p\) and \(q\). The goal is to use \(\mathrm{poly}(\log N)\) adaptive labels so that the two local character vectors can be decoded by coding theory, and then recover the Sylow-order profile.

### B10. Succinct functional-graph product decomposition

The functional graph of \(F\bmod N\) is the direct product of the graphs modulo \(p\) and modulo \(q\). The explicit graph is too large, but one can search for a special \(F\) whose cycle index, dynamical zeta function, or canonical product decomposition can be computed from a small arithmetic circuit. A canonical component of the decomposed graph then corresponds to a CRT idempotent.

### B11. Canonical decomposition of a small arithmetic tensor

Construct a multiplication/trace tensor \(T_N\) of dimension \(\mathrm{poly}(\log N)\) from a number of modular-exponentiation probes. Require that, after reduction modulo \(p\) and \(q\), it decomposes into two non-isomorphic tensor factors, and that it belongs to a class with bounded slice rank, bounded degree, or some other property that permits polynomial-time canonization. Recovering a tensor factor is equivalent to recovering a nontrivial central idempotent.

### B12. Automorphism-count moment interpolation

Construct a family of fixed-degree rings \(R_t(N)\) such that

\[
|\operatorname{Aut}R_t(N)|
=A_t(p)A_t(q),
\]

where the \(A_t(z)\) form a low-complexity exponential-polynomial family. If the automorphism counts of these special rings can be computed quickly, a small number of values of \(t\) may reconstruct \(p+q\) through power sums, and thereby factor \(N\). This directly combines ring isomorphism with OpenAI-style moment reconstruction.

## Z

### Z1. Thesis of the article

The integer factorization problem is widely considered difficult. However, the author found many points of doubt during several months of early research. The author’s conclusion is that large-integer factorization is an important scientific problem of extremely high value that has not been studied sufficiently. The main purpose of the article is to break the widespread blind belief that “the integer factorization problem should not be attempted,” and to give confidence to number-theory and computer-science enthusiasts who want to study it.

### Z2. Contradictory indicators: integer factorization and graph isomorphism

The article begins by asking which problem is harder: integer factorization or graph isomorphism. The theoretical-computer-science community generally considers graph isomorphism easier and integer factorization harder. The best known graph-isomorphism algorithm has quasipolynomial time complexity,

\[
\exp(\log^{O(1)}n),
\]

while the best known general number field sieve for integer factorization has subexponential time complexity, approximately

\[
\exp(1.9\cdot n^{1/3}).
\]

Here \(n\) denotes the bit length of the input integer, not the input integer \(N\).

When quantum computing is included, integer factorization has Shor’s polynomial-time quantum algorithm, while it remains unknown whether graph isomorphism has a polynomial-time algorithm in the quantum-computing model.

From the viewpoint of computational complexity, integer factorization belongs to \(NP\cap coNP\), while graph isomorphism belongs to \(NP\cap coAM\). The article says that neither is likely to be NP-complete and calls them NP-intermediate problems. Because \(NP\subseteq AM\), and because this inclusion can become equality under a strong derandomization assumption, the article says that integer factorization lies at a slightly lower complexity level, suggesting that it may be simpler.

| Perspective | Problem indicated as harder |
| --- | --- |
| Best known classical algorithm | Integer factorization |
| Best known quantum algorithm | Graph isomorphism |
| Computational-complexity perspective | Graph isomorphism |

The article lists three possibilities:

1. Integer factorization has a better classical algorithm. To remove the contradiction completely, integer factorization should have at least a quasipolynomial-time algorithm.
2. Graph isomorphism has a polynomial-time quantum algorithm.
3. Research on algorithms for integer factorization and graph isomorphism has reached its limit, and quantum computers can change the relative difficulty ordering of some problems while remaining unable to help with graph isomorphism.

The article’s footnotes also list the possibility that Babai’s quasipolynomial-time graph-isomorphism algorithm is wrong. They note that a classical polynomial-time graph-isomorphism algorithm would also satisfy the second possibility because quantum computation includes classical computation, and that if graph isomorphism had both classical and quantum polynomial-time algorithms, this would not demonstrate an advantage for quantum computation. The first two possibilities can both hold without contradiction.

The article says that all three possibilities would be interesting: the first two would at least produce new algorithms, while proving the third would mean that the power of quantum computation is quite limited. Because the article focuses on integer factorization, it mainly discusses the first possibility.

### Z3. Historical context

Number theory and computation have a long history. Euclid’s algorithm is a number-theoretic algorithm. Before the information age, primality testing and integer factorization were interesting number-theory problems. Examples include primality questions for special forms such as Mersenne and Fermat numbers, and Cole’s factorization of \(2^{67}-1\) after spending “three years of Sundays” on it.

The claim that every integer has a unique prime factorization was treated as fact in Euclid’s time and was explicitly stated and proved in Gauss’s *Disquisitiones Arithmeticae*. Gauss described distinguishing primes from composites and resolving composites into prime factors as one of the most important and useful problems in arithmetic.

In the 1970s, personal computers based on integrated circuits became widespread and computer science entered a golden age. RSA appeared in 1978, based on the difficulty of integer factorization. Miller–Rabin and Solovay–Strassen primality tests, introduced two years earlier, supported its practical use. The quadratic sieve appeared in the 1980s. Major developments around 1994 included the general number field sieve and Shor’s algorithm, followed by AKS primality testing in 2002.

The article says that academic discussion of integer factorization gradually became quiet after 2000, while HTTPS and public-key cryptography became broadly deployed. It states that the share of Internet traffic using HTTPS rose from 50 percent to 90 percent between 2015 and 2019. It presents integer factorization as having changed from an interesting pre-computer problem, to an important pre-Internet academic problem, to a foundation of modern Internet security.

### Z4. RSA, integer factorization, and research status

The article notes that the other half of current public-key cryptography is based on the elliptic-curve discrete-logarithm problem, including ECDH and ECDSA. It describes inspecting certificate signature algorithms and subject public-key algorithms as one way to see dependence on RSA, and says that more than 90 percent of root certificates in the described Windows certificate store use RSA. Its later correction states that RSA accounts for approximately 71 percent in the cited certificate-transparency data.

An efficient integer-factorization algorithm can break RSA, but the reverse does not necessarily hold. Misuse of RSA and partial data leakage can also create vulnerabilities, so attacks on RSA can be studied separately from integer factorization. The article points to Dan Boneh’s 1999 *Twenty Years of Attacks on the RSA Cryptosystem* and to cryptography problems from capture-the-flag competitions as places to learn about attacks on RSA.

The article says that research on integer factorization has almost stopped despite the deployment of RSA. It identifies the French group led by Paul Zimmermann, which factored RSA-829 in 2020, and reports Pierrick Gaudry’s statement that very few other researchers work on integer factorization, mentioning Nadia Heninger, Peter Schwabe, and Palash Sarkar.

### Z5. Discrete logarithms

Shor’s algorithm solves both integer factorization and discrete logarithms on a quantum computer. The article quotes Peter Shor:

> There’s a strange relation between discrete log and factoring. There’s no formula for taking an algorithm for one of these problems and applying it to the other. However, any time somebody has found an improved algorithm for one of them, people have reasonably quickly come up with a similar solution for the other one.

By changing the finite group, the discrete-logarithm problem has many variants, while integer factorization has only one formulation. In general, the function field sieve is the best algorithm for discrete logarithms and has many similarities with the general number field sieve. For finite fields of small characteristic, quasipolynomial-time algorithms exist.

### Z6. Shor’s algorithm and the hidden subgroup problem

The hidden subgroup problem includes integer factorization, discrete logarithms, graph isomorphism, and the shortest-vector problem on lattices. This is another reason to discuss integer factorization and graph isomorphism together. Shor’s algorithm solves the Abelian hidden subgroup problem, including integer factorization and discrete logarithms, but does not solve graph isomorphism or the shortest-vector problem on lattices.

### Z7. Reasons given in the article for confidence in efficient classical factorization

The article says that lack of confidence has severely suppressed research on integer factorization. It presents the following points.

1. Integer factorization is not considered NP-complete or NP-hard, while many researchers study NP-complete problems. The article says that integer factorization can be studied and that intermediate results can be published in the same way as intermediate results about NP-complete problems.

2. The article argues that Ron Rivest is not a good designer of cryptographic algorithms. It mentions the breaks of MD5 and RC4, the replacement of WEP by WPA, and the lack of broad adoption of MD6 and RC6, and says that RSA is the remaining Rivest algorithm still in use.

3. The article recounts the history in which Rivest formulated RSA after returning home from a Passover gathering where a good deal of wine had been consumed. It says that many early cryptographic algorithms followed a tradition of proposing an algorithm and treating the absence of a known break as success. It mentions the break of knapsack-based cryptography and the fact that replacing the Goppa code in McEliece with other codes often led to quick breaks.

4. RSA is one of the few exceptions in which key sizes are allowed to grow over time. Because RSA has subexponential attacks, it needs much longer keys than elliptic-curve cryptography for the same security level, and its key length must continue to grow. The article says that RSA remains in use through inertia despite being slower and less secure than elliptic-curve alternatives.

5. Henry Cohn expressed a similar view in *Factoring May Be Easier Than You Think*. His main criticism was of the belief that a problem is impossible because “one hundred smart people have tried it and failed.”

6. The article says that very few people have studied integer factorization. It reports searching a website listing more than 2,600 number theorists and finding fewer than 30 whose pages indicated work on factorization. The author’s subjective estimate is that no more than 100 recorded experts have studied the problem. It compares citation counts of roughly 30,000 for RSA, 14,000 for Shor’s algorithm, and slightly more than 1,000 for the general number field sieve, and says that papers studying how to break the assumption are fewer than one tenth of the related papers.

7. The article says that many cryptographers do not want to break integer factorization because most design cryptographic algorithms and need to believe that the underlying problem is difficult, while only a minority specialize in cryptanalysis.

8. The general number field sieve and Shor’s algorithm were both published in 1994. The article says that Shor’s small and elegant quantum algorithm redirected attention away from complicated classical algorithms. It says that Feynman proposed quantum computation at Caltech with the original motivation of simulating quantum systems, and that Shor was studying there at the time. It describes Shor’s algorithm as the main driving force behind quantum computing and as more persuasive than Gaussian boson sampling. It then describes the quantum-computing boom around Google’s 2019 claim of quantum supremacy, the author’s own move into quantum information and post-quantum cryptography at that time, the absence of a commercialization model, the closing of Alibaba’s and Baidu’s quantum laboratories in late 2022, discussion of a “quantum winter,” and the replacement of quantum computing by artificial intelligence as the favorite of Silicon Valley and Wall Street.

9. High value does not imply high difficulty. Research on integer factorization could threaten Internet security, which shows that the problem has high value but does not show that it is intrinsically difficult. The problem itself did not change as its applications became more important. The article mentions the breaks of Rainbow and SIDH as important within the field but limited in wider impact because they were not broadly deployed.

10. The article invokes Ladner’s theorem and says that breakthroughs on integer factorization and graph isomorphism are necessary on the path to answering \(P=NP\). It also states the author’s view that a proof of \(P\ne NP\) would be uninteresting because it would not change the world.

### Z8. Quadratic sieve and general number field sieve

Carl Pomerance published *A Tale of Two Sieves* in 1996, describing the invention of the quadratic sieve and the general number field sieve. The general number field sieve can be viewed as a generalization of the quadratic sieve. Both consist of two similar steps.

First, sample many relations from some distribution:

\[
x_i^2=a_i\pmod N.
\]

Second, use linear algebra to find a subset of the \(a_i\) whose product is a perfect square. This gives

\[
X^2=Y^2\pmod N.
\]

Then compute \(\gcd(X-Y,N)\), which gives a nontrivial factor with high probability.

The literature generally requires the generated \(a_i\) to factor into small primes, meaning that they are smooth numbers. The article says that one can use Legendre symbols to find a subset whose product is a perfect square in polynomial time, without factoring the \(a_i\). However, the existence of such a square-product subset still depends on the probability distribution of smooth numbers, so the bottleneck remains the distribution of smooth numbers.

The author draws three conclusions from studying the best current factorization algorithms: the quadratic sieve and general number field sieve are not especially difficult to learn; algorithm-contest participants can give algorithms for the second step that improve on the presentation in historical literature; and the low probability of smooth numbers limits further progress along this route. The article says that this route has reached its end and that a completely new idea is needed.

### Z9. A simple and elegant formula

For an RSA modulus \(N=pq\), with \(p<q<2p\), Euler’s theorem gives

\[
a^{N+1}=a^{p+q}\pmod N.
\]

The property was already known in the literature. The article notes that baby-step giant-step can be applied directly to it to obtain an \(O(N^{1/4})\) algorithm.

### Z10. Thoughts inspired by AKS primality testing

AKS primality testing uses the fact that

\[
(x+a)^N=x^N+a^N\pmod N
\]

when \(N\) is prime. One way to analyze it is through the binomial coefficients: when \(N\) is prime and \(0<k<N\),

\[
\binom Nk=0\pmod N,
\]

while the coefficients for \(k=0,N\) equal one. This suggests studying the binomial coefficients of an RSA composite \(N=pq\), with \(p<q<2p\).

Lucas’s theorem gives

\[
\binom{N}{kq}\bmod q
=
\binom00\binom pk\binom00\bmod q
=
\binom pk\bmod q.
\]

For \(0\le k<p\),

\[
\binom{N}{kp}\bmod p
=
\binom00\binom{q-p}{k}\binom10\bmod p
=
\binom{q-p}{k}\bmod p.
\]

For \(p\le k<q\),

\[
\binom{N}{kp}\bmod p
=
\binom00\binom{q-p}{k-p}\binom11\bmod p
=
\binom{q-p}{k-p}\bmod p.
\]

The binomial expansion therefore consists of three groups of nonzero parts.

The article describes this property as looking interesting while its use remains unknown.

### Z11. Inspiration from primality testing and ECM

Primality testing is a solved problem, but the information and methods it provides do not appear to transfer directly to factorization even though the two problems are closely related. The converse of Fermat’s little theorem fails in some cases. Composite numbers that pass the Fermat test are called Carmichael numbers, and the Miller–Rabin algorithm can factor Carmichael numbers.

The article says that this strengthens the intuition that primality testing and integer factorization are closely connected and suggests studying factorization from the viewpoint of primality testing, including efficient factorization algorithms for particular classes of composite numbers.

ECM uses elliptic curves for integer factorization. The ring \(\mathbb Z_N\) supports addition and multiplication, but its nonzero elements are not necessarily invertible, so it is not a finite field. If a nonzero element \(x\) without an inverse is found, then

\[
\gcd(x,N)
\]

gives a nontrivial factor. The article informally calls this ring a “pseudo-field” and treats it as if addition, multiplication, and division were available, with a failed division exposing a factor.

### Z12. Polynomial root-finding

Polynomial root-finding and factorization over finite fields are easy. Given a finite field \(\mathbb F_p\) and a polynomial \(f(x)\), choose a random integer \(z\) and compute

\[
\gcd\bigl(f(x-z),x^{(p-1)/2}-1\bigr).
\]

This randomly returns some linear factors of \(f(x)\). Repeating the procedure yields linear factors. The reason is

\[
x^{(p-1)/2}-1
=
\prod_{i\in\mathrm{QR}(\mathbb F_p)}(x-i).
\]

This simple polynomial contains a “random” set of \((p-1)/2\) linear factors, which can be extracted by taking a gcd.

If a nontrivial solution of

\[
x^2=1\pmod N
\]

can be found, then \(N\) can be factored. This is root-finding for \(f(x)=x^2-1\). The corresponding direction is to construct a “simple” \(g(x)\) with many linear factors and then compute a gcd.

### Z13. Closing position and implementation evidence

The article’s closing position is that integer factorization is an extremely valuable problem. It says that cryptographic designers’ promotion of its difficulty and Shor’s algorithm drawing researchers away from classical algorithms—not the technical difficulty itself—are important reasons why the problem receives little attention. It restates the view that integer factorization is an important scientific problem of extremely high value that has not been studied sufficiently, and is a rich area for work in cryptography and computational number theory.

Before making a public claim, the article asks researchers to implement their algorithm and try to factor public RSA moduli. It presents this as direct and powerful evidence and links the RSA Factoring Challenge and a tool introduction.
