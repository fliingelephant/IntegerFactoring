# F285 extension — Dimension-scaled rank synchronization

Status: author-derived candidate theorem. Independent reconstruction pending.
This extension preserves the original two-by-two `RESULT.md` unchanged.

## Exact statement

Let N=rs for distinct primes, and let A be a d-by-d matrix over Z/N whose
characteristic polynomial is squarefree modulo r. Let

\[
L_A=D(A^N),\qquad L_A(H)=\sum_{i=0}^{N-1}A^iHA^{N-1-i}.
\]

If the multiplicative order f=ord_s(r) is greater than d, then

\[
\boxed{\operatorname{rank}_{\mathbb F_r}(L_A)=d^2-d.}
\tag{D1}
\]

No assumption r>d is needed for (D1). For N=pq, the two local ranks are
therefore both d^2-d if the characteristic polynomial is squarefree in both
components and ord_q(p)>d, ord_p(q)>d.

More specifically, write e_1,...,e_k for the irreducible factor degrees over
F_r. The weaker sufficient hypothesis is that f divides none of the e_i.
The order>d condition implies this weaker hypothesis and is independent of A.

## Proof

Extend F_r to a splitting field of the squarefree characteristic polynomial.
There A is diagonalizable with d distinct eigenvalues lambda_1,...,lambda_d.
The matrix units are eigenvectors of L_A. Its eigenvalues are zero on the
d diagonal units because N=0 in F_r. On the i,j unit for i!=j they are

\[
\frac{\lambda_i^N-\lambda_j^N}{\lambda_i-\lambda_j}.
\tag{D2}
\]

Each eigenvalue lambda_i lies in F_(r^e) for some irreducible factor degree
e<=d. If lambda_i is nonzero, its multiplicative order divides r^e-1. The
condition f>d implies s does not divide any such r^e-1. For two nonzero
eigenvalues, their generated multiplicative subgroup has order dividing the
lcm of their individual multiplicative orders. This order is coprime to s.
Thus raising to s is injective on that subgroup. Raising to r is injective
on every field. Since N=rs and lambda_i!=lambda_j, their N-th powers differ.
If one eigenvalue is zero, the other is nonzero and their N-th powers also
differ. Both cannot be zero because the eigenvalues are distinct.

All d(d-1) off-diagonal values in (D2) are nonzero. Rank does not change
under field extension, proving (D1). The same proof works when f divides no
irreducible factor degree. It does not require that the whole splitting field
have degree at most d. Such a splitting-field assertion would be false in
general and is deliberately not used.

There is also an exact rank description without the order hypothesis. If m_z
is the number of eigenvalues lambda_i with lambda_i^N=z, then

\[
\ker L_A=\operatorname{Cent}(A^N),\qquad
\operatorname{rank}L_A=d^2-\sum_zm_z^2
=\operatorname{rank}(\operatorname{ad}_{A^N}).
\tag{D2a}
\]

Here Cent(B) is the space of matrices commuting with B and ad_B(H)=BH-HB.
In the eigenbasis, both kernels consist of exactly those matrix units for
which lambda_i^N=lambda_j^N, including the diagonal. This equality descends
to the base field. Thus the derivative's rank equals that of the ordinary
commutator of the publicly computable power A^N. It contributes no additional
rank invariant beyond the multiplicities of these power collisions.

## Sharpness of the local dimension threshold

Suppose f=ord_s(r)>=2, f<=d, and r>d. A primitive s-th root alpha has a
Frobenius orbit of length f, hence a degree-f irreducible minimal polynomial
over F_r. All f roots have s-th power 1, hence N-th power 1. Include this
factor in the characteristic polynomial and fill the remaining d-f degrees
with distinct linear factors whose roots lie in F_r other than 1.

This is possible since r>d. Because f>=2, s does not divide r-1, and s-th
powering is injective on F_r. The added roots have pairwise different N-th
powers, none equal to 1. The resulting squarefree polynomial's companion
matrix therefore has

\[
\operatorname{rank}_{\mathbb F_r}L_A=d^2-d-f(f-1).
\tag{D3}
\]

Thus a low order can produce an actual rank drop once its degree fits, not
just a gap in the proof. If f=1 and d>=2, two distinct s-th roots in F_r
already give a rank drop; r>d permits additional distinct roots if needed.
For d=1 the operator is always zero, so no rank drop below d^2-d is possible.

This construction proves local existence only. It uses the named local
characteristic and is not a public factor-free construction over Z/N.

## Few exceptional partners in a balanced interval

Fix an odd prime p and an integer D>=1. Define E_1 to be primes q in (p,2p)
with ord_q(p)<=D. Every q in E_1 divides

\[
P=\prod_{k=1}^{D}(p^k-1)<p^{D(D+1)/2}.
\]

The product of the distinct q in E_1 divides P and is greater than p^|E_1|.
Therefore

\[
|E_1|<D(D+1)/2.
\tag{D4}
\]

Define E_2 using ord_p(q)<=D. Each q in (p,2p) gives a distinct nonzero
residue q-p modulo p. The union of roots of X^k-1 for 1<=k<=D has size at
most sum_{k=1}^D k. More exactly, its size is

\[
S_p(D)=\sum_{\substack{m\le D\\m\mid p-1}}\varphi(m).
\]

Thus |E_2|<=S_p(D)<=D(D+1)/2. In particular

\[
\boxed{|E_1\cup E_2|<D(D+1).}
\tag{D5}
\]

These are elementary finite counts with no prime distribution assumption.
The exact fraction among prime partners is bounded by

\[
\frac{D(D+1)}{\pi(2p)-\pi(p)}.
\tag{D6}
\]

Using the standard prime number theorem as a declared external dependency,
pi(2p)-pi(p)~p/log p, so the fraction is O(D^2 log p/p). In particular it
tends to zero for every fixed quasipolynomial bound
D(p)=2^{C(log_2(log_2 p+1))^k}: such D is p^{o(1)}.

The prime number theorem is used only for this last density interpretation,
not for (D1)-(D6). Primary bibliographic source: P. Erdős, *On a New Method
in Elementary Number Theory Which Leads to an Elementary Proof of the Prime
Number Theorem*, Proceedings of the National Academy of Sciences 35 (1949),
374-384, [original scan](https://combinatorica.hu/~p_erdos/1949-02.pdf).
Focused search located the original scan and bibliographic record; opening
the scan timed out. No fresh audit of the prime number theorem is claimed.

## Uniformity and exact limits

For each q outside E_1 union E_2, (D1) applies simultaneously to every matrix
A of every dimension d<=D with unit characteristic discriminant modulo N.
The matrix may be selected adaptively, nonuniformly, or with unbounded search;
its two local ranks are still both d^2-d. No union bound over samples is
needed. For a dimension bound stated in terms of the input bit length,
choose D(p) to bound it over the interval p<q<2p; a fixed quasipolynomial
bound in the input bit length remains quasipolynomial in log p.

The conclusion concerns only the local rank profile of each individual
D(A^N). It does not cover ranks of sums, products, block combinations,
concatenations, or projections of several operators. Nor does it cover
individual entries, selected minors, coordinate-sensitive decoders, or other
matrix functions. A rank calculation may encounter a factor in an intermediate
entry even when its two final local ranks agree. No claim is made about that
event. Non-squarefree matrices in dimensions above two also remain outside
this extension. The two-by-two repeated-root calculation is in `RESULT.md`.

This rules out an all-input guarantee based solely on a mismatch of these
individual ranks on the unit-discriminant branch at quasipolynomial dimensions.
It is neither a general
factoring lower bound nor a lower bound against arbitrary finite-algebra
algorithms.

## Verification artifacts

`general_dimension_pilot.py` constructs companion matrices from public random
coefficients modulo N. It computes the full derivative by binary powering
with tangents, then uses known prime factors only as offline labels for
squarefreeness and local ranks. It tests dimensions 2, 3, 4 on six semiprimes
and records both the synchronized and exceptional rank histograms. The source
has a ten-second alarm. Resource estimate is less than five seconds and 30 MB.
The root supplied the shared process snapshot at 23:49 because this worker's
local ps call was sandbox-blocked: load 2.46/2.30/2.17, memory available 74%,
no swap; two OS processes occupied roughly one core each, Codex was at 13.5%,
and no numerical research process was running. The root authorized the pilot.

Execution passed on 112 matrices with squarefree characteristic polynomial
at both labeled primes. Every full derivative rank also equaled the rank of
the commutator of A^N. Nonexceptional orders gave the predicted ranks; some
exceptional cases gave actual mismatches, including ranks (6,4) for N=7*13
in dimension three. These finite examples are not an asymptotic success law.
Runtime was 0.155 seconds and peak RSS 17,383,424 bytes on this Mac. Exact
histograms are in `general_dimension_results.json`; stdout is retained in
`general_dimension_run.log`.

Fresh statement-only reconstruction of (D1)-(D6) remains the next verification
step. No catalog, shared ledger, or commit is modified by this worker.
