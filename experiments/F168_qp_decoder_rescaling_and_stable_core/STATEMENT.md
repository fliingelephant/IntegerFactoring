# F168 candidate — QP decoder rescaling and a length-linked stable core

## Status

This is a proof-only candidate. No hostile audit, statement-only
reconstruction, cross-family audit, human audit, or publication-level
literature audit has run.

Parts I–III below are exact quasipolynomial-complexity rescalings of promoted
results P87 and P92–P97/P99. They do not add a new arithmetic mechanism.
Part IV is the only new theorem: an infinite P98-stable semiprime family whose
two powered local orders each contain an exponentially large prime component.

Nothing here gives an all-input factor localizer or a complete factoring
algorithm.

Throughout,

\[
n=\lceil\log_2(N+1)\rceil.
\]

A QP bound means

\[
2^{C(\log_2(n+1))^k}
\]

for fixed constants \(C>0\) and \(k\ge1\), independent of \(N\) and its
unknown factors.

## I. QP closure lemma

Let \(B\), all public scan and enumeration caps, the number of supplied
residue generators, and the total explicit encoding length be QP in \(n\).
Then all of the following have uniform deterministic QP bit complexity:

1. constructing
   \(M_B=\operatorname{lcm}(1,\ldots,B)\) and its complete punctured bank;
2. sieving or deterministically testing every prime at most \(B\);
3. modular exponentiation by every bank exponent;
4. reading and powering every supplied generator; and
5. breadth-first enumeration of a generated subgroup through any QP
   numerical cap, including all equality, multiplication, and gcd tests.

The key bit-length bound is

\[
\log_2 M_B\le\log_2(B!)=O(B\log B)=2^{(\log n)^{O(1)}}.
\]

The numerical value of \(M_B\) is not the running-time measure. Its binary
length is QP.

Also, suppose one verified randomized trial has a QP work bound on every
input transcript and succeeds with probability at least the reciprocal of a
QP bound on every promised transcript. Independent verified repetition is
Las Vegas and has expected QP bit complexity.

## II. Exact rescaled decoder corollaries

The following promoted conditional algorithms remain uniform after replacing
their polynomial numerical caps by fixed QP caps. Any supplied generator list
and its total encoding must also have QP size.

1. **P87.** Given one public unit \(u\) modulo a distinct odd semiprime, the
   punctured-lcm bank is a deterministic QP factorer when the two local orders
   are unequal and

   \[
   \min\{\sigma(r_p),\sigma(r_q)\}\le Q(n).
   \]

2. **P92.** Given a strict pure-phase extension whose old graph order \(h\)
   satisfies \(\sigma(h)\le Q(n)\), whole-subgroup contraction and capped
   enumeration are deterministic QP. The useful image has at most \(Q(n)^2\)
   elements.

3. **P93.** Given a public subgroup \(K\) that contains a positive separator
   and satisfies

   \[
   \sigma(\exp K)\le Q(n),
   \]

   the complete punctured-bank scan and whole-subgroup enumeration are
   deterministic QP.

4. **P94.** Given a strict pure-phase state, scanning primes
   \(\ell\le L(n)\), all public puncture depths of \(N-1\), and powered images
   through cap \(S(n)\) is deterministic QP for QP bounds \(L,S\). It factors
   whenever some phase prime satisfies

   \[
   \ell\le L(n),
   \qquad
   \ell^{H_\ell-C_\ell+2}\le S(n).
   \]

5. **P95.** For a supplied subgroup \(K\), put \(S=K^{N-1}\), and let
   \(A,B\) be its coprime local image orders. Complete enumeration is a
   deterministic QP factorer when \(1<AB\le T(n)\) for a QP cap \(T\).
   Near-uniform sampling is a Las Vegas expected-QP factorer when \(S\ne1\)
   and \(\min(A,B)\le Q(n)\).

6. **P96.** If every supplied generator satisfies \(g_i^{N-1}=1\), the
   public-annihilator puncture scan is deterministic QP whenever a positive
   separator has some prime \(\ell\le L(n)\) with

   \[
   \ell^{2(H-C+1)}\le T(n)
   \]

   for QP bounds \(L,T\).

7. **P97.** The two-sample powered-rectangle source remains polynomial and
   has constant generation probability. A powered-rectangle localizer with
   QP work on every list and inverse-QP verified success on every promised
   list gives a Las Vegas expected-QP splitter for distinct odd semiprimes.

8. **P99.** The full-unit-group source remains polynomial and has constant
   generation probability. A localizer with QP work on every list and
   inverse-QP verified success on every list that generates the full unit
   group gives a Las Vegas expected-QP splitter for every composite. Verified
   recursion then gives complete factorization in expected QP time.

These are promise-preserving complexity corollaries. They supply none of the
missing separator, bounded-image, or localizer promises.

## III. Bare-N QP promise class

Let \(N=pq\) for distinct odd primes and put

\[
g=\gcd(p-1,q-1),
\qquad
A=\frac{p-1}{g},
\qquad
B=\frac{q-1}{g}.
\]

If

\[
\boxed{\min(A,B)\le Q(n),}
\]

then bare \(N\) has a classical Las Vegas splitter with expected QP bit
complexity. It samples \(a\) uniformly from \(1,\ldots,N-1\), checks
\(\gcd(a,N)\), and on the unit branch checks

\[
\gcd(a^{N-1}-1,N).
\]

This is an algorithm only for the displayed promise class. It is not an
all-input result.

## IV. New length-linked stable-family theorem

There is an absolute constant \(c>0\) and an infinite family of distinct odd
semiprimes \(N=pq\) with

\[
p<q,
\qquad
g=\gcd(p-1,q-1)=2,
\]

such that, for

\[
A=(p-1)/2,
\qquad
B=(q-1)/2,
\]

there are odd primes \(r\mid A\) and \(s\mid B\) satisfying

\[
\boxed{r,s\ge2^{cn}.}
\]

Moreover,

\[
\boxed{\gcd(AB,N-1)=1.}
\]

Consequently:

1. the P97 rectangle is immediately P98-stable;
2. every exponent supported only on primes dividing \(N-1\) acts as an
   automorphism on that rectangle;
3. \(\sigma(A),\sigma(B)\ge2^{cn}\), so the bounded-prime-component
   hypotheses fail for the two full powered local orders under every fixed
   QP cap; and
4. exact uniform direct sampling has density

   \[
   \frac1A+\frac1B-\frac2{AB}=2^{-\Omega(n)}.
   \]

Thus QP repetition of direct uniform sampling remains insufficient on this
family. This is not a lower bound against adaptive value-dependent words,
canonical integer feedback, relation decoding, or other classical
algorithms.
