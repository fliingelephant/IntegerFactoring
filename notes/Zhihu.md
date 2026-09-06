# Why We Should Be Confident That Efficient Classical Integer-Factoring Algorithms May Exist

**Author:** Kaiyi Zhang

**Source description:** Retired competitive programmer; published in *Computer Science Miscellany*
**Source edit time:** 2026-02-09 01:38, Beijing time

> **Translation note.** This is an English translation of the Chinese source
> preserved in Git history. It records the source author's motivation,
> arguments, factual assertions, and mathematical seeds. The repository has not
> audited or endorsed those assertions. A claim in this document is therefore a
> source claim, not research evidence. The translation preserves questionable
> claims rather than silently repairing them. For clarity, it uses \(N\) for the
> integer being factored and \(n\) for its bit length where the source used the
> same lowercase letter in both roles. Non-substantive page controls, reaction
> counts, tags, and sharing controls are omitted. The original Chinese text
> remains available in Git history.

Integer factorization is widely considered difficult. During several months of
early research, however, I found many reasons for doubt. My conclusion is that
large-integer factorization is an important scientific problem of extremely
high value that has not been studied sufficiently. This article aims to break
the widespread belief that integer factorization should not even be attempted.
It aims to give confidence to people in number theory and computer science who
want to study it.

The article focuses on integer factorization. It discusses the nature of the
problem, its connections to other problems, its history, and some of the people
involved. The expected background is elementary computational number theory,
computational complexity theory, and a popular-level understanding of quantum
computing.

## A preface: contradictory indicators

Which problem is harder, integer factorization or graph isomorphism? The
theoretical computer science community generally treats graph isomorphism as
easier and integer factorization as harder. The best known graph-isomorphism
algorithm has quasipolynomial complexity,

\[
\exp(\log^{O(1)} n),
\]

whereas the best known general number field sieve for integer factorization has
subexponential complexity, approximately

\[
\exp(1.9 n^{1/3}).
\]

Here \(n\) is the bit length of the input integer, and the displayed complexity
has been simplified.[1][2]

The comparison changes when quantum computing is included. Shor's algorithm
factors integers in polynomial time on a quantum computer. It is not known
whether graph isomorphism has a polynomial-time quantum algorithm.

From a complexity-theoretic viewpoint, integer factorization belongs to
\(NP\cap coNP\), while graph isomorphism belongs to \(NP\cap coAM\). Neither is
thought likely to be NP-complete.[3] They are therefore described here as
NP-intermediate problems. Because \(NP\subseteq AM\), and because a strong
derandomization assumption can turn this inclusion into equality, the article
argues that integer factorization sits at a slightly lower complexity level and
may be simpler.[4][5][6]

| Perspective | Problem indicated as harder |
| --- | --- |
| Best known classical algorithm | Integer factorization |
| Best known quantum algorithm | Graph isomorphism |
| Computational-complexity perspective | Graph isomorphism |

The article presents three main possibilities:[7]

1. Integer factorization has a better classical algorithm. To remove the
   apparent contradiction completely, it should have at least a
   quasipolynomial-time algorithm.
2. Graph isomorphism has a polynomial-time quantum algorithm.[8]
3. Algorithmic research on both problems has reached its limit, and quantum
   computers can change the relative difficulty of some problems while still
   being unable to help with graph isomorphism.

All three possibilities would be interesting. The first two would produce new
algorithms.[9] A proof of the third would show that quantum computation has
severe limits. This article focuses on the first possibility.

## A short history of integer factorization

Number theory and computation have a long history. Euclid's algorithm is often
described as the first algorithm known to humanity. Before the information age,
primality testing and integer factorization were interesting number-theory
problems. Famous examples include primality questions for Mersenne and Fermat
numbers, and Cole's factorization of \(2^{67}-1\) after spending “three years of
Sundays” on it.

Before computational complexity existed as a concept, the definition of a
prime already supplied a criterion for primality. Unique prime factorization
was treated as fact in Euclid's time and was stated and proved explicitly in
Gauss's *Disquisitiones Arithmeticae*. Gauss described distinguishing primes
from composites and resolving composites into prime factors as one of the most
important and useful problems in arithmetic.

Number theory was long regarded as useless mathematics. In the 1970s, personal
computers based on integrated circuits spread widely, and computer science
entered a golden age. RSA appeared in 1978 and based its security on the
difficulty of integer factorization. Miller–Rabin and Solovay–Strassen primality
tests, introduced two years earlier, supported practical use. The quadratic
sieve appeared in the 1980s and intensified the contest between cryptographic
design and cryptanalysis.

The Internet created strong demand for cryptography in the 1990s. Academic
discussion of integer factorization peaked around 2000. Representative results
included the general number field sieve and Shor's algorithm in 1994, and AKS
primality testing in 2002. Industry then deployed HTTPS broadly while academic
discussion became quieter. The article states that HTTPS traffic rose from
about 50 percent to about 90 percent between 2015 and 2019. It presents integer
factorization as having moved from an interesting pre-computer problem, to an
important pre-Internet academic problem, to a foundation of modern Internet
security.

## The prevalence of RSA

The other major branch of current public-key cryptography is based on the
elliptic-curve discrete-logarithm problem. ECDH and ECDSA are representative
examples. It is hard to measure what fraction of all Internet traffic RSA
protects.[10] The article suggests inspecting certificate signature algorithms
and subject public-key algorithms as one way to see modern dependence on RSA.
It also states that more than 90 percent of the root certificates in the
described Windows certificate store use RSA.

## Integer factorization and RSA

Efficient integer factorization breaks RSA, but breaking RSA does not
necessarily give an integer-factorization algorithm.[11][12] Misuse of RSA and
partial data leakage can also cause vulnerabilities. Attacks on RSA can
therefore be studied separately from integer factorization.

For RSA attacks, the article recommends Dan Boneh's 1999 survey *Twenty Years
of Attacks on the RSA Cryptosystem* and cryptography problems from
capture-the-flag competitions. This article remains focused on integer
factorization.

## The stated research situation

The article argues that research on integer factorization has almost stopped
despite the widespread use of RSA. It identifies the French group led by Paul
Zimmermann, which factored RSA-829 in 2020. It also reports an email response
from Pierrick Gaudry saying that very few other people still work on integer
factorization, and naming Nadia Heninger at UCSD, Peter Schwabe at the Max
Planck Institute, and Palash Sarkar in India.

## Related problems

### Discrete logarithms

Shor's algorithm solves both integer factorization and discrete logarithms on
a quantum computer. In *The Early Days of Quantum Computation*, Peter Shor
wrote:

> There's a strange relation between discrete log and factoring. There's no
> formula for taking an algorithm for one of these problems and applying it to
> the other. However, any time somebody has found an improved algorithm for one
> of them, people have reasonably quickly come up with a similar solution for
> the other one.

Changing the finite group creates many variants of the discrete-logarithm
problem, while integer factorization has only one formulation. In general, the
function field sieve is the best algorithm for discrete logarithms and shares
many ideas with the general number field sieve. Finite fields of small
characteristic have quasipolynomial-time algorithms.

### Shor's algorithm and the hidden subgroup problem

The hidden subgroup problem includes integer factorization, discrete
logarithms, graph isomorphism, and the shortest-vector problem on lattices.
This is another reason to discuss integer factorization and graph isomorphism
together. Shor's algorithm solves the Abelian hidden subgroup problem,
including integer factorization and discrete logarithms, but it does not solve
graph isomorphism or the shortest-vector problem on lattices.

## Why the article is confident about efficient classical factorization

The article argues that lack of confidence has suppressed research on integer
factorization. This section aims only to build confidence. Technical directions
appear later.

1. **Integer factorization is not considered NP-complete.** The article argues
   that this weakens the case for intrinsic difficulty. Many researchers study
   NP-complete problems, so integer factorization can also be studied. It says
   that intermediate results can be published in the same way as intermediate
   results about NP-complete problems.[13][14][15]

2. **The article criticizes Ron Rivest's record as a cryptographic designer.**
   Rivest helped create modern cryptography. He designed the MD hash family and
   the RC symmetric-cipher family, and he is the “R” in RSA. The article points
   to the breaks of MD5 and RC4, the replacement of WEP by WPA, and the lack of
   broad adoption of MD6 and RC6. It calls RSA the remaining Rivest algorithm
   still in use.

3. **The article emphasizes the informal origin of RSA and other early
   cryptosystems.** It quotes *The RSA Cryptosystem: History, Algorithm,
   Primes*:

   > In April 1977, they spent Passover at the house of a student and drank a
   > good deal of wine before returning to their homes at around midnight.
   > Rivest, unable to sleep, lay on the couch with a math textbook and started
   > thinking about their one-way function. He spent the rest of the night
   > formalizing his idea, and he had much of the paper ready by daybreak. The
   > algorithm is now known as RSA – the initials of their surnames in same
   > order as their paper.

   The article argues that many early cryptosystems followed a tradition of
   proposing an algorithm and treating the absence of a known break as success.
   It mentions the break of knapsack cryptography and the fact that replacing
   the Goppa code in McEliece with other codes often led to quick breaks.

4. **RSA permits key lengths to grow over time.** Modern cryptographic
   competitions reject algorithms for relatively small flaws. In contrast,
   elliptic-curve systems retain 256-bit keys while RSA needs much larger keys
   for comparable security because it has subexponential attacks.[16] Its keys
   must continue to grow. The article says that RSA remains in use through
   inertia even though it is slower and less secure than the elliptic-curve
   alternative.

5. **Others have expressed a similar attitude.** Henry Cohn published
   *Factoring May Be Easier Than You Think*. His main criticism was of the
   belief that a problem is impossible because “one hundred smart people have
   tried it and failed.”

6. **The article says that few people have studied the problem.** The author
   reports crawling a website that listed more than 2,600 number theorists and
   finding fewer than 30 whose pages indicated work on factorization. The
   author's subjective estimate is that no more than 100 recorded experts have
   studied it. The article compares roughly 30,000 citations for RSA, 14,000 for
   Shor's algorithm, and slightly more than 1,000 for the general number field
   sieve. It says that papers about breaking the assumption form less than one
   tenth of the related literature.

7. **The article says that many cryptographers do not want to break it.** Most
   cryptographers design systems and need confidence in the underlying hard
   problems. Only a minority specialize in cryptanalysis. The article argues
   that researchers who build systems on number-theoretic assumptions have
   little incentive to invalidate their own work.

8. **Quantum computing redirected attention.** The general number field sieve
   and Shor's algorithm both appeared in 1994. The article argues that Shor's
   compact and elegant algorithm drew attention away from complicated classical
   methods. It describes Feynman's proposal of quantum computation at Caltech,
   originally motivated by quantum simulation, and notes that Shor studied
   there. It calls Shor's algorithm the main driver of quantum computing and
   more persuasive than Gaussian boson sampling.

   The article describes the boom around Google's 2019 announcement of quantum
   supremacy. The author was drawn to Shor's algorithm at that time, studied
   quantum computing, and entered quantum information and post-quantum
   cryptography. It then describes slow progress, the lack of a business model,
   the closing of Alibaba's and Baidu's quantum laboratories in late 2022,
   discussion of a “quantum winter,” and artificial intelligence replacing
   quantum computing as the favorite of Silicon Valley and Wall Street.

9. **High value does not imply high difficulty.** A successful factoring
   algorithm could endanger Internet security. That shows the problem's value,
   not its intrinsic difficulty. The problem itself did not change as its
   applications became more important. The article gives the breaks of Rainbow
   and SIDH as examples that mattered within the field but had limited wider
   impact because the systems had not been broadly deployed.

10. **“We must know; we will know.”** The article invokes Ladner's theorem and
    says that breakthroughs on integer factorization and graph isomorphism are
    necessary on the path to an answer of \(P=NP\). It also gives the author's
    view that a proof of \(P\ne NP\) would be uninteresting because it would not
    change the world.

## Early results and possible research directions

### The quadratic sieve and the general number field sieve

Carl Pomerance published *A Tale of Two Sieves* in 1996. It recounts the
invention of the quadratic sieve and the general number field sieve. The
general number field sieve can be viewed as a generalization of the quadratic
sieve. Both have two similar steps.

First, sample many relations from some distribution:

\[
x_i^2=a_i\pmod N.
\]

Second, use linear algebra to find a subset of the \(a_i\) whose product is a
perfect square. This gives

\[
X^2=Y^2\pmod N.
\]

Computing \(\gcd(X-Y,N)\) then gives a nontrivial factor with high probability.

The literature generally requires each generated \(a_i\) to factor into small
primes. Such integers are smooth. The article says that Legendre symbols can be
used to find a square-product subset in polynomial time without factoring the
\(a_i\). It also says that the existence of such a subset still depends on the
distribution of smooth numbers. Smoothness probability therefore remains the
bottleneck.

The author draws three conclusions. First, the quadratic sieve and general
number field sieve are not especially difficult to learn. A well-educated
undergraduate, or an excellent high-school student, can understand them.
Second, algorithm-contest participants can improve on how the second step is
presented in historical literature. This gave the author early confidence that
the problem is approachable. Third, the low probability of smooth numbers
limits further progress along this route. The article reports that email
discussion with French researchers supported the view that the sieving route
has reached its end and that a completely new idea is needed.

### A simple and elegant formula

Let the RSA modulus be \(N=pq\), with \(p<q<2p\). Euler's theorem gives

\[
a^{N+1}=a^{p+q}\pmod N.
\]

The identity was already known. The article notes that baby-step giant-step can
be applied directly to obtain an \(O(N^{1/4})\) algorithm.

### Thoughts inspired by AKS primality testing

AKS primality testing uses the fact that

\[
(x+a)^N=x^N+a^N\pmod N
\]

when \(N\) is prime. One way to analyze this identity is through binomial
coefficients. For a prime \(N\) and \(0<k<N\),

\[
\binom Nk=0\pmod N,
\]

while the coefficients at \(k=0,N\) equal one. This suggests studying the
binomial coefficients of an RSA composite \(N=pq\), where \(p<q<2p\).

Lucas's theorem gives

\[
\binom{N}{kq}\bmod q
=\binom00\binom pk\binom00\bmod q
=\binom pk\bmod q.
\]

For \(0\le k<p\),

\[
\binom{N}{kp}\bmod p
=\binom00\binom{q-p}{k}\binom10\bmod p
=\binom{q-p}{k}\bmod p.
\]

For \(p\le k<q\),

\[
\binom{N}{kp}\bmod p
=\binom00\binom{q-p}{k-p}\binom11\bmod p
=\binom{q-p}{k-p}\bmod p.
\]

The article therefore describes the binomial expansion as consisting of three
groups of nonzero terms. It calls this property interesting but says that its
use is unknown.

### Inspiration from primality testing and ECM

Primality testing is solved, but its information and methods do not appear to
transfer directly to factorization even though the problems are closely
related. The converse of Fermat's little theorem fails for some composites.
Composite numbers that pass the Fermat test are Carmichael numbers. The article
says that Miller–Rabin can factor Carmichael numbers.[17]

This example strengthens the author's intuition that primality testing and
integer factorization are closely related. It suggests studying factorization
through primality testing, including efficient algorithms for special classes
of composites.[18]

ECM uses elliptic curves for integer factorization. The ring \(\mathbb Z_N\)
supports addition and multiplication, but its nonzero elements need not be
invertible, so it is not a finite field. If a nonzero nonunit \(x\) is found,
then

\[
\gcd(x,N)
\]

gives a nontrivial factor. The article informally calls this ring a
“pseudo-field.” It proposes acting as though addition, multiplication, and
division were available, because a failed division finishes the factorization
task.[20]

### Polynomial root-finding

Polynomial root-finding and factorization over finite fields are easy.[19]
Given a finite field \(\mathbb F_p\) and a polynomial \(f(x)\), choose a random
integer \(z\) and compute

\[
\gcd\left(f(x-z),x^{(p-1)/2}-1\right).
\]

This randomly returns some linear factors of \(f(x)\). Repetition yields linear
factors. The reason is

\[
x^{(p-1)/2}-1
=\prod_{i\in\mathrm{QR}(\mathbb F_p)}(x-i).
\]

This simple polynomial contains a “random” set of \((p-1)/2\) linear factors,
which a gcd can extract.

If a nontrivial solution of

\[
x^2=1\pmod N
\]

can be found, then \(N\) can be factored. This is root-finding for
\(f(x)=x^2-1\). The proposed direction is therefore to construct a “simple”
polynomial \(g(x)\) with many linear factors and then compute a gcd.

## Closing remarks

Integer factorization is unquestionably valuable. The article argues that two
beliefs have constrained the field: cryptographic designers promote the
difficulty of factorization, and Shor's algorithm drew researchers away from
classical algorithms. It treats these beliefs, rather than technical difficulty
itself, as important reasons why the problem receives little attention.

The article repeats its main claim: integer factorization is an important
scientific problem of extremely high value that has not been studied
sufficiently. It calls the problem an obvious rich area in cryptography and
computational number theory that deserves serious effort.

## About the author

The author graduated from the ACM class at Shanghai Jiao Tong University in
2020 and won several gold medals in international collegiate programming
contests. The author completed a doctorate in cryptography at Shanghai Jiao
Tong University's School of Computer Science in 2025.[21] At the time of the
article, the author was a postdoctoral researcher at Tsinghua University's
Institute for Advanced Study, working with Xiaoyun Wang.

During the doctorate, the author studied post-quantum cryptography and quantum
information and published in venues including CRYPTO and PNAS. Those fields
assume the future existence of large-scale quantum computers. Slow recent
progress caused the author and others to become more skeptical of quantum
computing.[22] The article accepts the theoretical correctness of Shor's
algorithm. Its questions concern when large-scale quantum computers will be
built and whether quantum computers truly have more computational power than
classical computers. The latter question motivated this article.

## Before making a public claim

The article warns against repeating prominent claims that later failed, citing
Shor's 2016 claim about LWE, Schnorr's 2021 claim about RSA, and Yilei Chen's
2024 claim about LWE. It asks researchers to implement an algorithm and try to
factor public RSA moduli before announcing a result. It presents this as direct
and strong evidence.[23]

- RSA Factoring Challenge: https://en.wikipedia.org/wiki/RSA_Factoring_Challenge
- Tool introduction: https://www.youtube.com/watch?v=OJJK3-R465c

## Source notes and references

1. In the complexity expressions, \(n\) is the bit length of the input, not the
   integer \(N\).
2. The displayed complexity has been simplified.
3. The source says this makes NP-hardness still less likely, and calls it a
   common error to say that integer factorization or graph isomorphism is
   NP-hard.
4. Complexity Zoo, NPI: https://complexityzoo.net/Complexity_Zoo:N#npi
5. Complexity Zoo, AM: https://complexityzoo.net/Complexity_Zoo:A#am
6. Discussion of factorization and graph isomorphism:
   https://www.quora.com/Do-we-know-whether-factorization-is-harder-than-graph-isomorphism
7. The source lists a fourth possibility: László Babai's quasipolynomial
   graph-isomorphism algorithm is wrong.
8. Because quantum computation includes classical computation, this could also
   be a classical polynomial-time algorithm. The source asks why, if graph
   isomorphism is classically easier, its quantum algorithm was found much later
   than the factoring algorithm. It also notes that a problem with both
   classical and quantum polynomial-time algorithms would not demonstrate a
   quantum advantage.
9. The first two possibilities can hold simultaneously.
10. The source later corrects the RSA figure to about 71 percent and cites:
    https://radar.cloudflare.com/certificate-transparency
11. The source calls complete equivalence between breaking RSA and factoring a
    common misconception.
12. Further reading: Neal Koblitz, *Another Look at “Provable Security”*.
13. Dominik Scheder, *PPSZ Is Better Than You Think*, FOCS 2021:
    https://ieeexplore.ieee.org/document/9719845
14. Venkatesan Guruswami, Bingkai Lin, Xuandi Ren, Yican Sun, and Kewen Wu,
    *Almost Optimal Time Lower Bound for Approximating Parameterized Clique,
    CSP, and More, under ETH*, STOC 2025:
    https://dl.acm.org/doi/10.1145/3717823.3718130
15. Anna R. Karlin, Nathan Klein, and Shayan Oveis Gharan, *A (Slightly)
    Improved Approximation Algorithm for Metric TSP*:
    https://dl.acm.org/doi/10.1145/3406325.3451009
16. RSA security strength and modulus size:
    https://crypto.stackexchange.com/questions/8687/security-strength-of-rsa-in-relation-with-the-modulus-size
17. Discussion of factoring Carmichael numbers:
    https://crypto.stackexchange.com/questions/5279/carmichael-number-factoring
18. The source adds that results for special classes can support publications
    and researchers' livelihoods.
19. Berlekamp–Rabin algorithm:
    https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Rabin_algorithm
20. The source notes that \(\mathbb Z_N\) is not a Euclidean domain. It retains
    the pseudo-field intuition that a failed remainder or division operation
    completes the task.
21. The source cites CSRankings and says that Shanghai Jiao Tong University's
    cryptography program ranks first in Asia and ninth worldwide:
    https://csrankings.org/#/index?crypt&asia
22. The source recommends Yuxi Fu's *Computational Complexity Theory*.
23. The source supplies RSA-2048 as a test input:

    ```text
    2519590847565789349402718324004839857142928212620403202777713783604366202070
    7595556264018525880784406918290641249515082189298559149176184502808489120072
    8449926873928072877767359714183472702618963750149718246911650776133798590957
    0009733045974880842840179742910064245869181719511874612151517265463228221686
    9987549182422433637259085141865462043576798423387184774447920739934236584823
    8242811981638150106748104516603773060562016196762561338441436038339044149526
    3443219011465754445417842402092461651572335077870774981712577246796292638635
    6373289912154831438167899885040445364023527381951378636564391212010397122822
    120720357
    ```
