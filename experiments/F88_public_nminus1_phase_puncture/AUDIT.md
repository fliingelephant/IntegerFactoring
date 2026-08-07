# F88 hostile proof audit

## Verdict: PASS

I audited RESULT.md at the pinned SHA-256

    c8a4d65af2ad0148ec3c05feb8147efc964e3f2fd2e9b97049ed7872d34b1c39

The hash matches. I ran no search, replay, or research computation. I found
no defect in the public annihilator, valuation puncture, powered-group
formulas, deterministic scan, capped enumeration, or fixed \(N=2047\)
specialization.

The result passes only as the conditional decoder that it claims to be. It
assumes a supplied strict pure-phase extension of a graph subgroup. It also
assumes that one prime in its phase quotient is within the public scan and
that the corresponding powered group fits the public cap. The algorithm
does not test these promises.

## 1. The public divisibility \(h\mid N-1\) is exact

The graph projections identify \(H\) with subgroups \(H_p\) and \(H_q\) of
the two cyclic local unit groups. Therefore

\[
h=|H_p|=|H_q|,
\qquad
h\mid p-1,
\qquad
h\mid q-1.
\]

It follows that

\[
p\equiv q\equiv1\pmod h
\]

and hence

\[
N-1=pq-1\equiv0\pmod h.
\]

Thus \(h\mid N-1\). The proof uses \(p,q\) only to establish the theorem.
The executable exponent is the public integer \(N-1\).

For completeness, a pure-phase extension also has

\[
c=[K:H]\mid h.
\]

Indeed, after identifying the graph, the map that removes the unique old
element with the same first coordinate identifies \(K/H\) with a subgroup
\(D\) of the cyclic group \(H_q\). Thus \(D\) is cyclic of order \(c\mid h\),
and

\[
K=H\cdot(\{1\}\times D)
\]

is an internal direct product. In particular, \(c\mid N-1\) as well.

The sentence that \(N-1\) kills the old graph and phase quotient is correct.
Also, every element of \(K\) has both local coordinates in groups of order
\(h\), so \(N-1\) kills \(K\) itself. No extension-exponent ambiguity occurs.

## 2. The valuation puncture is always in the public scan

Choose a prime \(\ell\mid c\), and write

\[
e=v_\ell(N-1),\qquad
H_\ell=v_\ell(h),\qquad
C_\ell=v_\ell(c).
\]

The divisibilities \(c\mid h\mid N-1\) give

\[
1\le C_\ell\le H_\ell\le e.
\]

Set

\[
j=e-C_\ell+1,
\qquad
E=(N-1)/\ell^j.
\]

Then \(1\le j\le e\), so this exponent occurs in the declared scan, and

\[
v_\ell(E)=e-j=C_\ell-1.
\]

For every \(r\ne\ell\), division by \(\ell^j\) changes no \(r\)-valuation:

\[
v_r(E)=v_r(N-1)\ge v_r(h)\ge v_r(c).
\]

Thus the exponent kills all non-\(\ell\) parts of both \(H\) and \(D\). It
does this even when those parts contain large primes that the algorithm
never factors or scans. They remain implicitly present in the public
integer \(E\).

The construction also handles excess public valuation. If \(e>H_\ell\),
the larger puncture \(j=e-C_\ell+1\) first removes the excess and then leaves
exactly \(C_\ell-1\) powers of \(\ell\) in \(E\). Nothing in the proof
requires \(e=H_\ell\).

## 3. The powered size formulas are exact

For a cyclic group of order \(n\), the image under the \(E\)-power map has
order

\[
n/\gcd(n,E).
\]

The graph \(H\) is cyclic of order \(h\), and the phase group \(D\) is
cyclic of order \(c\). Since the ambient group is abelian, powering the
internal direct product gives

\[
K^E=H^E\cdot(\{1\}\times D^E)
\]

with trivial intersection. Consequently

\[
|H^E|=\frac h{\gcd(h,E)},
\qquad
|D^E|=\frac c{\gcd(c,E)},
\qquad
|K^E|=|H^E|\,|D^E|.
\]

The valuations from the previous section therefore give

\[
h_E=\ell^{H_\ell-C_\ell+1},
\qquad
c_E=\ell,
\qquad
|K^E|=\ell^{H_\ell-C_\ell+2}.
\]

This remains correct when \(C_\ell<H_\ell\). The old graph then retains the
larger order \(\ell^{H_\ell-C_\ell+1}\); the theorem does not incorrectly
contract it to order \(\ell\). When \(C_\ell=H_\ell\), the formula reduces
to

\[
h_E=\ell,\qquad c_E=\ell,\qquad |K^E|=\ell^2.
\]

## 4. The separator count and density are exact

The two projections of \(K^E\) are the two local images of \(H^E\), each of
order \(h_E\). Therefore each projection kernel has order

\[
\frac{|K^E|}{h_E}=c_E=\ell.
\]

Every nonidentity element of the first kernel has first coordinate \(1\)
and nonidentity second coordinate. It is a positive separator. The same is
true with the coordinates reversed for the second kernel. The two kernels
meet only in the identity, so the exact count is

\[
(\ell-1)+(\ell-1)=2\ell-2.
\]

Dividing by \(|K^E|\) gives

\[
\frac{2(\ell-1)}{\ell^{H_\ell-C_\ell+2}}.
\]

This argument includes \(\ell=2\). In that case there are exactly two
positive separators, and no odd-prime assumption is used.

## 5. The public scan needs no hidden group data

For each public prime \(\ell\le L\) that divides \(N-1\), the algorithm can
obtain \(e=v_\ell(N-1)\) by repeated exact division. It then tries every
\(1\le j\le e\). Therefore, for a successful scanned prime, it necessarily
tries the hidden proof witness

\[
j=e-C_\ell+1.
\]

The algorithm never needs to know which prime divides \(c\), or the values
of \(h,c,H_\ell,C_\ell\). It also never needs \(p\) or \(q\). Those values
only prove that one public trial succeeds.

Enumerating primes through \(L\), testing their divisibility into \(N-1\),
and obtaining their valuations is deterministic polynomial work when the
numerical value of \(L\) is polynomial in \(\log N\). The scan does not need
a complete factorization of \(N-1\).

A prime larger than \(L\) is not a hidden failure in the theorem. If every
prime divisor of \(c\) exceeds \(L\), Corollary 3 gives no success guarantee.
This is an explicit promise boundary.

## 6. Capped breadth-first enumeration is complete and polynomial

Let \(g_1,\ldots,g_m\) be the supplied public generators of \(K\). The
power map is a homomorphism, so

\[
K^E=\langle g_1^E,\ldots,g_m^E\rangle.
\]

Starting at the identity and repeatedly multiplying by these powered
generators reaches the full finite subgroup. Explicit inverse edges are not
required: each generator inverse is a nonnegative power of that generator
in a finite group.

For the theorem's exponent, condition

\[
\ell^{H_\ell-C_\ell+2}\le S
\]

means that the queue closes after at most \(S\) distinct residues. The rule
that stops only when the \((S+1)\)-st distinct residue appears cannot
interrupt it. Complete enumeration reaches all \(2\ell-2\) separators, so a
gcd test returns a proper factor.

For every wrong exponent, insertion of the \((S+1)\)-st residue stops that
trial. Redundant or identity generators only add duplicate edges. A
deterministic visited set makes the procedure deterministic.

There are at most \(L\) scanned primes and at most
\(\lfloor\log_2(N-1)\rfloor\) punctures per prime. Each exponent has
\(O(\log N)\) bits. Across the scan, the capped closure tests

\[
O(mLS\log N)
\]

generator edges, up to constant and bit-operation factors, and stores
\(O(S)\) residues at one time. Modular powering, multiplication, ordered-set
lookup, and gcd all have polynomial bit complexity. Thus the scan is
deterministic polynomial time and storage under the stated polynomial bounds
on \(L,S,m\), and the generator encodings.

The theorem needs the group-size quantity

\[
\ell^{H_\ell-C_\ell+2}
\]

to be polynomially bounded. Merely saying that the raw integer gap
\(H_\ell-C_\ell\) is polynomial in \(\log N\) would not be sufficient. The
formal condition (8) and the final scope paragraph use the correct
group-size requirement; the informal phrase “primary-gap parameter is
polynomially bounded” must be read in that exact sense.

## 7. The \(N=2047\) specialization is correct

The retained F82/F86 certificate supplies

\[
N=2047,\qquad h=22,\qquad c=11.
\]

The public integer is

\[
N-1=2046=2\cdot3\cdot11\cdot31.
\]

For \(\ell=11\),

\[
e=H_{11}=C_{11}=1,
\qquad
j=1,
\qquad
E=(N-1)/11=186.
\]

The exact power formulas give

\[
h_E=\frac{22}{\gcd(22,186)}=11,
\qquad
c_E=\frac{11}{\gcd(11,186)}=11,
\]

and hence

\[
|K^E|=121.
\]

The separator formula gives \(2\cdot11-2=20\). Thus \(E=186\) produces the
claimed small factor-bearing image. Since both \(186\) and the earlier
exponent \(2520\) kill the order-two component and act invertibly on the
order-eleven component, they produce the same unique \(11\)-primary image
of this finite abelian group.

## 8. Exact promise scope

The passing theorem gives a deterministic factor extractor only when all of
the following hold:

1. \(N=pq\) for distinct odd primes.
2. Public generators for \(K\le(\mathbb Z/N\mathbb Z)^\times\) are supplied.
3. There exists a graph subgroup \(H\) such that \(K\) is a strict pure-phase
   extension of \(H\): both local images remain unchanged.
4. Some prime \(\ell\mid[K:H]\) satisfies \(\ell\le L\).
5. Its residual image size satisfies
   \(\ell^{H_\ell-C_\ell+2}\le S\).
6. The numerical bounds \(L,S\), the generator count, and all input
   encodings are polynomial in \(\log N\).

The public procedure need not recognize items 3–5. They are correctness
promises, and the cap makes all non-successful trials safe.

The result does not create a pure-phase state, prove that feedback supplies
a scanned phase prime or small valuation gap, handle general order/phase
mixtures, reduce arbitrary composites to the promise, or give an all-input
factoring algorithm. Within these boundaries, all theorem and algorithm
claims pass.
