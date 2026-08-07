# F62 — polynomial sparse selectors for cross-relation blocks

**Status:** candidate. No research computation was run.

**Verdict:** there is a concrete polynomial-size selector that contains every
useful F62 witness known so far. It tests products and quotients supported on
at most two current blocks, with polynomially bounded exponents. This is a real
source operation, not a new final decoder. There is no all-input success law.

Small exact examples also show that one use of each block, prefix products, and
one or two rounds of pair closure are not enough. The unresolved statement is
now a precise **short CRT-separator law**, not the old one-block feedback law.

## 1. Closest prior route and material difference

The closest prior route is F61/P69. It feeds one whole current block. P69 proves
that this only repeats a known relation or a state already covered by a small
scan.

This retry permits a vector of block exponents. It can multiply blocks from
different relations, amplify a block by retaining duplicate relation
occurrences, and use a quotient through a negative exponent. These operations
change the selected residue. F62's exact aggregate-quotient law therefore does
not reduce them to P69.

## 2. A uniform sparse selector

Let

\[
q_1,\ldots,q_m
\]

be the current pairwise-coprime gcd-free endpoint blocks. Every block is a unit
modulo \(N\). For integers \(w,E\geq1\), define

\[
\mathcal S_{w,E}
=\left\{e\in\mathbb Z^m:
|\operatorname{supp}(e)|\leq w,
\quad |e_j|\leq E\right\}.
\]

For each nonzero \(e\), compute

\[
r_e=\prod_j q_j^{e_j}\pmod N,
\qquad 1\leq r_e<N,
\]

where a negative exponent uses a modular inverse. Test

\[
\gcd(r_e-1,N),\qquad \gcd(r_e+1,N).
\tag{1}
\]

Discard the global residues \(r_e=1\) and \(r_e=N-1\).

If neither gcd is proper, the algorithm can still add the canonical inverse
relation of \(r_e\), refine the block basis, and run the complete P66/P68
decoder on the enlarged batch.

For fixed \(w\),

\[
|\mathcal S_{w,E}|
\leq \sum_{s=1}^{w}\binom ms(2E)^s
=O((mE)^w).
\]

Thus \(\mathcal S_{2,E}\) has polynomial size when \(m\) and \(E\) are
polynomial in \(\log N\). Modular powers, inverses, products, and the screens
in (1) all have polynomial bit cost. All residues stay below \(N\).

There are two variants that must not be confused.

1. **Legal divisor feedback.** Use only nonnegative exponents available in an
   indexed aggregate of seed relations, and require the integer product to be
   less than \(N\). F62's formula \(k(g)=K_S\bmod g\) applies.
2. **Residue selector.** Permit negative exponents or reduce a product larger
   than \(N\). This is still a valid public state and a valid factoring screen,
   but it is a different feedback rule. F62's divisor formula does not apply.

Polynomial exponent amplification is legitimate. Repeat each indexed seed
presentation \(E\) times and retain its full integer exponent data. The
aggregate presentation length grows by only a factor \(E\). This supplies the
positive block powers used by the legal variant. The modular variant does not
need to construct the aggregate product.

## 3. Exact success condition

Call \(e\) a **CRT separator** if one of the gcds in (1) is proper. For a
squarefree input \(N=\prod_a p_a\), this means that \(r_e\) is \(+1\) or
\(-1\) modulo at least one, but not all, of the prime factors for the selected
sign. For prime powers, the equivalent statement uses the valuation of
\(r_e\mp1\).

A non-global square root of one is a CRT separator, but it is not necessary.
It is enough that one coordinate is \(+1\) or \(-1\). This distinction changes
the interpretation of an existing F62 witness.

For \(N=21\), the F62 distinct-relation choice is

\[
g=2\cdot5=10.
\]

It is not a square root of one modulo \(21\), but it factors immediately:

\[
\gcd(10-1,21)=3.
\]

Thus that witness does more than create a new relation and a new block. Its
two-block selector already succeeds before the batch decoder runs.

## 4. The sparse selector contains every current useful witness

### F62's \(N=55\) witness

The blocks \(3\) and \(7\) give

\[
3\cdot7=21,
\qquad 21^2\equiv1\pmod {55},
\]

and the two gcd screens return \(5\) and \(11\). This is in
\(\mathcal S_{2,1}\).

### F62's infinite multiplicity witness

There

\[
g=2^t,
\qquad
N=\frac{g^2-1}{3},
\qquad t=\Theta(\log N).
\]

This is in \(\mathcal S_{1,E}\) for a linear exponent cap
\(E=O(\log N)\). Duplicate seed presentations supply the required copies of
the block \(2\).

Therefore a two-support selector with a sufficiently large fixed polynomial
exponent cap contains all useful examples currently used to justify F62. This
is evidence for testing it. It is not evidence for an all-input theorem.

## 5. Exact limits of smaller selectors

### 5.1 Exhausting one relation's legal divisors can fail

Take

\[
N=187=11\cdot17.
\]

The public state \(2\) gives

\[
2\cdot94=188=1+N=2^2\cdot47.
\]

The complete block list is \(2,47\). Every legal divisor state below \(N\)
from this one presentation is

\[
2,\ 4,\ 47,\ 94.
\]

For each of these four states, both gcds in (1) equal one. Feeding any one of
them only reproduces the value \(188\), as P69 predicts. Thus even exhaustive
one-round legal divisor selection need not factor the input.

Duplicate amplification changes the result. For example,

\[
2^4=16<187,
\qquad
\gcd(16+1,187)=17.
\]

Two indexed copies of the presentation supply the four copies of block \(2\),
so this is legal divisor feedback. This is why multiplicity is an algorithmic
resource and must not be removed as a duplicate decoder column. The modular
variant succeeds even sooner because

\[
47^2\equiv152\pmod {187},
\qquad \gcd(152+1,187)=17.
\]

### 5.2 One signed direct pass can fail, while feedback can repair it

On the same \(N=187\) transcript, the residues produced by support at most two
and exponents in \(\{-1,0,1\}\) reduce to

\[
2,\ 4,\ 8,\ 47,\ 94,\ 117
\]

and their already listed inverses. None has a proper gcd with \(N\) after
adding or subtracting one. Thus the first direct \(\mathcal S_{2,1}\) pass
fails on this exact seed transcript, while \(\mathcal S_{1,2}\) succeeds.
A selector theorem must state its exponent cap, not only its support width.

The failed direct pass still creates useful source state. The residue \(8\)
has inverse \(117\) and gives

\[
8\cdot117=936=1+5N=2^3\cdot117.
\]

The endpoint \(117\) is coprime to the old blocks, so gcd-free refinement adds
it as one whole block; it does not factor \(117\). A second sparse pass tests

\[
117\cdot47\equiv76\pmod {187},
\qquad
\gcd(76+1,187)=11.
\]

So this example is also exact evidence that a nonfactoring first pass can
improve the next selector. It does not give a uniform bound on the number of
rounds.

### 5.3 Pair-residue feedback can reach a nonfactoring fixed point

Take

\[
N=91=7\cdot13,
\qquad
2\cdot46=92=2^2\cdot23.
\]

Start with blocks \(2,23\). In each round, form every product of at most two
current block types modulo \(N\), allowing a repeated type, screen it, feed its
canonical inverse relation, and refine again. Do not allow higher powers.

The first round gives the nontrivial states

\[
4,\ 46,\ 74.
\]

States \(4\) and \(46\) reproduce \(92\). State \(74\) has inverse \(16\) and
gives

\[
74\cdot16=1184=1+13N=2^5\cdot37.
\]

The refined blocks are \(2,23,37\). Their pair products add only state

\[
23\cdot37\equiv32\pmod {91},
\]

whose inverse is \(37\) and whose relation value is again \(1184\). The full
fixed-point state set is

\[
2,\ 4,\ 23,\ 32,\ 37,\ 46,\ 74.
\]

Every \(\gcd(r\pm1,91)\) for this set is trivial. A further pair round adds no
state and no block. Thus one or two pair-feedback rounds have no general
closure-to-factor theorem; this example in fact reaches a fixed point.

The boundary is exact. The higher power \(2^3=8\) is outside this pair rule
and gives

\[
\gcd(8-1,91)=7.
\]

### 5.4 Prefix and balanced products add no guarantee

For the \(N=91\) seed transcript, the sorted block order is \(2,23\). Its
prefix products and its balanced binary-tree products are a subfamily of the
failed pair closure above. Reordering or using a richer interval family can
change a finite example, but no canonical order supplies a proved CRT
separator. Prefix and balanced rules are compression heuristics, not a source
law.

## 6. What the aggregate quotient does and does not give

For an indexed subset of relations, write

\[
P_S=1+K_SN.
\]

Once a legal divisor \(g<N\) of \(P_S\) has been selected, F62 gives the useful
exact formula

\[
k(g)=K_S\bmod g.
\]

But this formula does not select \(g\). For every admissible divisor,

\[
K_S\equiv-N^{-1}\pmod g,
\]

which is only another form of \(g\mid1+K_SN\). Computing the residue is cheap
after the divisor choice. Finding a useful divisor among exponentially many
block exponent vectors remains the hard step.

For two aggregate relations,

\[
K_{S\cup T}=K_S+K_T+NK_SK_T.
\]

This lets the algorithm update quotients without expanding the full product,
but it does not linearize the divisor selection problem.

## 7. Random choice and amortized gcds

### Relation to order finding

For one block \(q\), let \(o_p\) be its multiplicative order modulo an odd
prime-power component \(p^a\mid N\). Then

\[
q^e\equiv1\pmod {p^a}
\quad\Longleftrightarrow\quad o_p\mid e,
\]

and \(q^e\equiv-1\pmod {p^a}\) exactly when \(o_p\) is even and
\(e\equiv o_p/2\pmod {o_p}\). Therefore \(\mathcal S_{1,E}\) is the
bounded-exponent part of order-based factoring. It succeeds when two CRT
components have a useful order mismatch visible below \(E\).

This states the Shor connection precisely. Shor learns a possibly very large
period and then halves it. The sparse classical selector only tries a
polynomial interval of exponents. No theorem here makes a large order
classically available. With two blocks, the target becomes a short
two-variable multiplicative relation instead of a one-variable period, but
the same missing size bound remains.

### Random selection

Suppose a random selector output \(R\) is uniform on a subgroup \(H_p\) of
\((\mathbb Z/p\mathbb Z)^*\) for a prime \(p\mid N\). Then

\[
\Pr[R\equiv\pm1\pmod p]\leq\frac{2}{|H_p|}.
\]

Thus uniformity alone is not favorable. If the projected subgroup has
exponential size in \(\log N\), polynomially many independent samples still
have negligible chance to hit a screenable coordinate. A successful random
selector needs a proved bias, a small projected subgroup, or a period-finding
operation. Ordinary random subset products do not come with such a theorem.

Many screens can be amortized. For a polynomial explicit family \(F\), compute

\[
D=\prod_{e\in F}(r_e^2-1)\pmod N
\]

and take one gcd with \(N\). A product tree can localize a proper factor if the
first gcd equals \(N\) because different nonglobal candidates covered
different factors. Global residues were discarded before the product. This
reduces gcd overhead. It does not increase the success set: one of the
enumerated residues still has to be a CRT separator. It also does not by itself
compress an exponential subset family into a polynomial computation.

## 8. Disposition

The most concrete next sampler is:

1. obtain a polynomial-size seed transcript;
2. retain duplicate presentations and exact block exponents;
3. enumerate \(\mathcal S_{2,E}\) for a fixed polynomial
   \(E=\operatorname{poly}(\log N)\);
4. screen every residue directly;
5. add the surviving inverse relations; and
6. run complete gcd-free refinement and the P66/P68 decoder once.

This is polynomial in the input length for every fixed exponent polynomial.
It differs algorithmically from “compute one scalar and take one gcd.” It
constructs a polynomial family of new states and can change the block basis.

The missing theorem is exact:

> For every composite input not handled by elementary preprocessing, does a
> polynomial seed transcript contain, or create after polynomially many
> rounds, a CRT separator of support at most two and polynomial exponent?

Nothing proved here implies that statement. The \(N=187\) first pass and the
\(N=91\) unsigned pair fixed point kill the smallest local versions, but they
do not kill signed feedback or polynomial exponent amplification. Increasing
the support to an unbounded value gives exponentially many choices. Even
support \(O(\log\log N)\) is generally quasipolynomial, not polynomial.

The route therefore remains open only at the source-selection law. There is no
classical polynomial-time factoring algorithm yet.
