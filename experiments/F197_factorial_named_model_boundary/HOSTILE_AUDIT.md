# F197 hostile audit

## Verdict

**PASS.** All four frozen inputs match their declared SHA-256 hashes. Every
mathematical claim follows under the stated balanced-semiprime promise, and
the two literature-dependent complexity claims agree with the cited primary
sources. I found no false theorem, missing hypothesis, illicit modular
division, reversed reduction, or scope leak.

## Frozen-input integrity

| File | Expected and observed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `774ce7c5496c28942d6cb11814b95cc2487ae10477127d40d8609332090e49c3` | match |
| `PROOF.md` | `6b30bd83a52b380c6f04e32c4839b924324b5e55688e48077265abd06e83bc84` | match |
| `SELF_AUDIT.md` | `8f307f3bc757603ce358b3dfa767697112b77d51149b312bfe6c844aacf8a971` | match |
| `PROVENANCE.md` | `7fec2a25aab0ca9035912aefe5ab663382a42d963e0bf00bf1e1383f3801d26b` | match |

I audited those bytes without altering them.

## Independent reconstruction

### 1. Balanced inequalities, factorial valuations, and the interval product

Because (p<q),

\[
p^2<pq=N<q^2.
\]

Thus (p<\sqrt N<q), so integrality gives (p\le B<q). The upper-balance
promise also gives (N=pq<2p^2), hence (B<\sqrt2p<2p). There is therefore
exactly one multiple of (p), namely (p), and no multiple of (q), in
(1,\ldots,B). This proves

\[
v_p(B!)=1,\qquad v_q(B!)=0,
\]

and both asserted gcds of (F=B!).

For (D=\prod_{j=1}^B(N-j)), no factor is divisible by (q), since
(N-j\equiv-j\not\equiv0\pmod q). Modulo (p), the only possible index is
(j=p). Its factor is (N-p=p(q-1)). If (p\mid q-1), then
(p<q<2p) forces (q=p+1), which is even and cannot be an odd prime.
Consequently (v_p(D)=1) and (v_q(D)=0), proving both gcd claims for
(D). Finally,

\[
\prod_{j=1}^B(N-j)=B!\binom{N-1}{B}
\]

is the standard exact binomial identity with the factors in reverse order.

Reduction modulo (N) or (N^2) preserves the relevant gcd with that
modulus. Hence every exact or canonical-residue representation explicitly
listed in Theorem 1 exposes (p) before an exact (D/F) division. This does
not reach a compressed representation that exposes none of those values;
the statement excludes that case.

### 2. The named dense block model

A materialized degree-(u) dense coefficient vector has (u+1) logical
positions. Covering (B) factors in consecutive width-(u) blocks exposes
(\lceil B/u\rceil) block values. After discarding one constant position,
the stated model therefore exposes at least

\[
u+\left\lceil\frac Bu\right\rceil
\ge u+\frac Bu\ge2\sqrt B.
\]

This is a count of materialized logical values, and hence a work/output
lower bound; it is not a claim that all values must remain live in distinct
memory cells simultaneously. Since (B=\Theta(\sqrt N)=2^{\Theta(n)}),
(\sqrt B) is exponential in (n).

The quantifiers are sound: the inequality holds for every integer
(1\le u\le B). It applies only to the dense coefficient-plus-block-value
scheme that the theorem defines. Streaming, compressed products, general
straight-line programs, and general modular-factorial algorithms are not
covered.

### 3. Published BGS and Costa--Harvey bounds

The [Bostan--Gaudry--Schost primary paper](https://specfun.inria.fr/bostan/publications/BoGaSc07.pdf)
states on page 1780 that, in any ring, (1\cdots L) can be computed in
(O(\mathsf M_R(\sqrt L)\log L)) ring operations. Its Theorem 14 gives the
sharper square-root recurrence bound subject to explicit unit and supplied-
inverse conditions. Its Theorem 11 gives complete deterministic
factorization in

\[
O\!\left(\mathsf M_{\rm int}(N^{1/4}\log N)\right)
\]

bit operations. The frozen statement keeps the arbitrary-ring factorial
claim separate from the stronger conditional recurrence result, so it does
not erase the latter's invertibility hypotheses.

For (L=B) over (\mathbb Z/N\mathbb Z), standard fast residue and
polynomial arithmetic turns this published route into
(B^{1/2+o(1)}\operatorname{poly}(n)) bit operations. With
(B=\Theta(\sqrt N)), the displayed upper-bound scale is
(N^{1/4+o(1)}=2^{\Theta(n)}).

The [Costa--Harvey primary preprint](https://arxiv.org/pdf/1201.2116)
explicitly specifies multitape-Turing bit complexity in its introduction.
Its Theorem 1 proves

\[
O\!\left(\mathsf M_{\rm int}\!\left(
\frac{N^{1/4}\log N}{\sqrt{\log\log N}}
\right)\right),
\]

and its introduction gives the (K!\), block-polynomial, and gcd extraction
used in the provenance. Thus the claimed (\sqrt{\log\log N}) improvement
and unchanged (N^{1/4}) power are source-accurate.

These are upper bounds whose displayed numerical scales are not QP. Neither
the statement nor proof turns them into a lower bound on another algorithm.

### 4. Nonunit cancellation and exact lift digits

The valuation result permits (F=pU) with (U) a unit modulo both (N)
and (N^2). Therefore

\[
N\mid F(x-y)\iff q\mid x-y,
\]

and

\[
N^2\mid F(x-y)\iff pq^2\mid x-y.
\]

No division by (p), (F), or another nonunit occurs in these
equivalences; they are integer divisibility cancellations using
(\gcd(U,N)=1). In (\mathbb Z/N^2\mathbb Z), the kernel consists of the
(p) residue classes represented by multiples of (pq^2). On the
restricted canonical interval (0\le x<N), a difference has absolute value
less than (N), so divisibility by (pq^2>N) forces equality. The global
noninjectivity and restricted injectivity are therefore both exact.

Writing (F=NQ+R), reduction gives
(\gcd(R,N)=\gcd(F,N)=p). If (a_2) is the canonical residue modulo
(N^2), then for some integer (k\),

\[
F=a_2+kN^2,
\qquad
Q=\left\lfloor\frac{a_2}{N}\right\rfloor+kN.
\]

It follows that (a_2=R+N(Q\bmod N)), with both digits canonical. The low
digit is (R), so the lift factors (N) before its quotient digit can
supply an inverse-based division.

### 5. Exact sizes, the (v_2(B!)) split, and quotient-bit recovery

The bounds

\[
(B/2)^{\lfloor B/2\rfloor}\le B!\le B^B
\]

give (\log_2F=\Theta(B\log B)=2^{\Theta(n)}). Also

\[
(N-B)^B\le D<N^B,
\]

so (D) has (2^{\Theta(n)}) bits. Once (F>2N), which fails only on a
finite initial set, (F/(2N)<\lfloor F/N\rfloor<F/N). Hence (Q) has the
same coarse (2^{\Theta(n)}) bit length. These are sequential output-size
bounds only; they do not obstruct short residues or compressed states.

For the power-of-two residue, Legendre's formula gives

\[
v_2(B!)=\sum_{i\ge1}\left\lfloor B/2^i\right\rfloor.
\]

The sum has (O(\log B)=O(n)) terms and is polynomial-time computable. If
(v_2(B!)\ge n), then (F\bmod2^n=0). Otherwise
(\lfloor B/2\rfloor<n), so (B<2n+2), and direct multiplication of the
(B=O(n)) factors modulo (2^n) is polynomial time. The split covers every
input, including the small nonzero-residue cases.

Let (f_2=F\bmod2^n) and suppose the (n)-bit value
(Q_2=Q\bmod2^n) is supplied. Euclidean division gives

\[
R\equiv f_2-NQ_2\pmod{2^n}.
\]

Here (R\ne0), because (\gcd(F,N)=p<N), and
(R<N<2^n) because (n=\lceil\log_2(N+1)\rceil). The canonical residue is
therefore the exact integer (R), after which one gcd returns (p). This
uses no illegal division modulo (N).

For (a=F\bmod(N2^n)), write (F=a+kN2^n). Since this modulus is a
multiple of (N), (a\bmod N=R), and division by (N) gives

\[
Q=\left\lfloor a/N\right\rfloor+k2^n.
\]

The bound (0\le a<N2^n) makes (\lfloor a/N\rfloor) the canonical
(Q_2). Thus (a=R+NQ_2) exactly.

The direction of the reduction is only

\[
\text{compute }Q\bmod2^n\quad\Longrightarrow\quad\text{factor }N.
\]

No converse is proved or used. In particular, the packet does not claim
that knowing (p) makes (Q_2) QP-computable.

### 6. Exact one-child recurrence and final scope

Choose a nondecreasing quasipolynomial (q(m)) that dominates the per-node
term. Unrolling the exact one-child decrement gives

\[
T(m)\le T(0)+\sum_{j=1}^m q(j)
\le T(0)+m q(m),
\]

which is quasipolynomial. A fixed-ratio decrease is unnecessary for one
chain. This closure claim does not depend on the factorial constructions.

The dense named model already incurs its value-exposure lower bound at the
root, while the cited published algorithms supply only exponential-scale
root upper bounds. The packet correctly stops there: it does not claim that
all possible root primitives are expensive, and it does not claim a general
factoring lower bound.

## Hostile-scope conclusion

The dangerous strengthenings all fail, but none is made by the frozen
packet: the block count is not a circuit lower bound; the BGS and
Costa--Harvey estimates are not lower bounds; the (N^2) map is not
globally injective; exact-output size says nothing about residues; quotient
bits are sufficient but not shown necessary or factor-computable; and a
one-child decrement chain with QP node cost is accepted as QP. The frozen
self-audit and provenance accurately preserve each of these boundaries.
