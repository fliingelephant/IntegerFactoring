# PASS — proof-blind reconstruction

The SHA-256 of the only input read, `STATEMENT.md`, is

```text
af82219350f7c27f79c25eb93a4d708f94a11ca8f32464f31fe62b743e2bc6e8
```

It matches the required digest. All claims follow.

Throughout, \(\iota_N(g)\) is the unique inverse of \(g\) in
\(\{1,\ldots,N-1\}\). If \(g\mid P\), then \(\gcd(g,N)=1\), because
\(P\equiv1\pmod N\). A legal quotient-\(r\) candidate is an
occurrence-certified \(g\) for which

\[
1<g<N,\qquad g\iota_N(g)=1+rN.
\]

The occurrence certificate records factors against indexed endpoints and
never merges equal occurrences.

## 1. The quotient-difference identities

Write \(A_r=1+rN\). The two exact relations

\[
P=A_r+(K-r)N,
\qquad
KA_r-rP=K-r
\]

show both inclusions between the common-divisor sets. Hence

\[
\gcd(P,A_r)=\gcd(P,K-r)=\gcd(A_r,K-r).
\]

Modulo \(A_r\),

\[
A_i=1+k_iN\equiv(k_i-r)N.
\]

Therefore

\[
P\equiv N^m\prod_i(k_i-r)\pmod {A_r}.
\]

Since \(\gcd(N,A_r)=1\), multiplication by \(N^m\) does not change a
gcd with \(A_r\). Thus

\[
D_r=\gcd\!\left(A_r,\prod_i(k_i-r)\right).
\]

This remains true when some \(k_i=r\): the product is zero, the corresponding
factor \(A_i=A_r\) divides \(P\), and both sides are \(A_r\).

If no difference is zero, taking the valuation of this last gcd gives, for
each prime \(p\),

\[
v_p(D_r)=\min\!\left(v_p(A_r),\sum_i v_p(k_i-r)\right),
\]

where valuations of negative differences mean valuations of their absolute
values. Consequently, a prime of \(D_r\) divides at least one nonzero
quotient difference. In the equal-quotient case it divides the declared zero
difference.

## 2. The exact supported fibre

Let \(h=\iota_N(g)\). Because \(g>1\), the congruence \(gh\equiv1\pmod N\)
has the form

\[
gh=1+k(g)N
\]

with \(k(g)\ge1\). Also \(h<N\), so

\[
1+k(g)N=gh\le g(N-1)<gN,
\]

and hence \(k(g)<g\).

If \(k(g)=r\), then \(g\mid A_r\) and \(g\mid P\), so \(g\mid D_r\);
the preceding inequality gives \(r<g<N\).

Conversely, suppose \(g\mid D_r\) and \(r<g<N\). Put

\[
h=\frac{A_r}{g}.
\]

It is a positive integer. Moreover,

\[
gN-A_r=(g-r)N-1>0,
\]

so \(h<N\). Since \(gh=A_r\equiv1\pmod N\), this \(h\) is the canonical
inverse \(\iota_N(g)\), and \(k(g)=r\). Therefore

\[
k(g)=r
\quad\Longleftrightarrow\quad
g\mid D_r\text{ and }r<g<N.
\]

In particular, refinement of \(D_r\) computes the complete supported fibre,
not merely a necessary superset.

## 3. Deterministic construction when \(N>r^2\)

First, an occurrence-allocation lemma makes the capacity issue explicit.
List the \(2m\) indexed endpoints in a fixed order as
\(e_1,\ldots,e_{2m}\), so \(P=\prod_j e_j\). For any \(d\mid P\), start
with \(T_0=d\) and set

\[
c_j=\gcd(T_{j-1},e_j),
\qquad
T_j=T_{j-1}/c_j.
\]

For every prime, the residual exponent after all endpoints is the positive
part of

\[
v_p(d)-\sum_jv_p(e_j),
\]

which is zero because \(d\mid P\). Hence \(T_{2m}=1\) and
\(d=\prod_jc_j\). Omit the \(c_j=1\). Each remaining chunk is attached to
one indexed endpoint, divides that endpoint, is less than \(N\), and respects
its capacity. The complete gcd-free block basis records the same splits with
exact block exponents.

Apply the lemma to \(d=D_r\). If some occurrence chunk \(c_j>r\), choose
\(g=c_j\). Then \(r<g<N\). Otherwise, multiply the nonunit chunks in their
fixed order and stop at the first prefix whose product exceeds \(r\). Such a
prefix exists exactly when \(D_r>r\). If \(s\le r\) is the preceding prefix
and \(c_j\le r\) is the last chunk, the returned value satisfies

\[
r<g=sc_j\le r^2<N.
\]

In either case, \(g\mid D_r\), its indexed factor uses are certified, and
Section 2 proves that it is legal. This is a single scan of a fixed list; it
does not enumerate subsets.

Necessity is immediate: a legal candidate has \(r<g\le D_r\), so
\(D_r>r\). Thus, when \(N>r^2\), a legal quotient-\(r\) candidate exists if
and only if \(D_r>r\).

There are at most \(2m\) occurrence chunks. Each is smaller than \(N\). If
the ledger instead displays individual block powers, an endpoint contains at
most \(\lfloor\log_2N\rfloor\) nonunit factor copies, so that expanded list
also has polynomial length. The residuals are at most \(D_r\le1+rN\), and
all prefix products divide \(D_r\). Their bit lengths are therefore
\(O(\log N+\log r)\). The list and all intermediate integers have polynomial
bit length in the retained transcript, \(\log N\), and the encoding of
\(r\).

If \(r\le\operatorname{poly}(\log N)\) but \(N\le r^2\), then
\(\sqrt N\le r\). Trial division through \(\lfloor\sqrt N\rfloor\) uses only
polynomially many divisions of \(O(\log N)\)-bit integers. It finds a proper
factor or proves that \(N\) is prime, so this small-\(N\) branch is resolved
in polynomial bit complexity.

## 4. Residue duality

From

\[
g\iota_N(g)=1+k(g)N
\]

we get

\[
k(g)\equiv-N^{-1}\pmod g.
\]

Section 2 proved \(1\le k(g)<g\). It is therefore the specified representative:

\[
\rho_N(g)=k(g).
\]

If also \(g\mid P=1+KN\), then

\[
K\equiv-N^{-1}\equiv\rho_N(g)\pmod g.
\]

The residue is nonzero, so the ordinary remainder \(K\bmod g\) is exactly
\(\rho_N(g)\).

The duality is exact:

* Choosing an occurrence-certified \(g\mid P\), with \(1<g<N\), determines
  the unique target \(r=\rho_N(g)=K\bmod g\). The candidate then lies in the
  fibre supported by \(D_r\).
* Choosing \(r\) first computes the aggregate carrier
  \(D_r=\gcd(P,A_r)\). Its occurrence-certified divisors satisfying
  \(r<g<N\) are exactly the legal members of that fibre.

The aggregate \(D_r\) need not itself be a candidate. It can be at most
\(r\), or it can be at least \(N\). Even when it is legal, either sign gcd
can be trivial or global, so legality does not imply usefulness for factoring.
It can also aggregate several factor origins and therefore does not select a
particular useful presentation.

## 5. Bit complexity and the subproduct tree

Each \(A_i=x_iy_i<N^2\) has \(O(n)\) bits. Hence

\[
\operatorname{bitlen}(P)
 \le 1+\sum_i\operatorname{bitlen}(A_i)
 =O(mn),
\]

and \(K=(P-1)/N\) also has \(O(mn)\) bits. A balanced product tree, or even
successive multiplication, computes \(P\) using a polynomial number of
bit operations.

For \(r\le R\), \(A_r\) has \(O(n+\log R)=O(n)\) bits because
\(R=\operatorname{poly}(n)\). Each \(D_r\) is one gcd between
polynomial-bit-length integers. Refinement can use the residual allocation in
Section 3, or its stored block-basis version: process each indexed endpoint
or block record once, take a gcd with the current residual, divide exactly,
and record the exponent/capacity use. This uses no integer factorization. Its
record count is bounded by the retained transcript size. Thus one scan costs
polynomial time in that size and \(n\), and the \(R=\operatorname{poly}(n)\)
scans do also. All products, gcds, exact divisions, and exponent records have
polynomial bit length.

For a node \(v\) of a relation subproduct tree, let \(I_v\) be its indexed
leaf set and write

\[
P_v=\prod_{i\in I_v}A_i=1+K_vN.
\]

Repeating the two algebraic arguments from Section 1 gives

\[
\begin{aligned}
D_{v,r}:=\gcd(P_v,A_r)
 &=\gcd(P_v,K_v-r)\\
 &=\gcd\!\left(A_r,\prod_{i\in I_v}(k_i-r)\right).
\end{aligned}
\]

The zero-difference convention and the valuation formula apply unchanged.
A tree has only \(2m-1\) fixed, laminar node sets. Descending it, with residual
valuation/capacity accounting, locates which fixed child branches can supply
a divisor and ultimately identifies indexed leaves. This is provenance. It
does not choose an arbitrary subset: the \(2^m\) leaf subsets are not the
\(2m-1\) tree nodes, and selecting a union of leaves remains a separate
combinatorial choice.

## 6. Bounded-quotient domination

Assume \(1\le r,k_i\le B\), no \(k_i=r\), and \(D_r>r\). Put

\[
\delta_i=|k_i-r|.
\]

Then \(1\le\delta_i\le B\), and Section 1 gives

\[
D_r\mid\prod_i\delta_i.
\]

Allocate \(D_r\) deterministically against these indexed differences. Start
with \(T_0=D_r\) and set

\[
q_i=\gcd(T_{i-1},\delta_i),
\qquad T_i=T_{i-1}/q_i.
\]

The valuation argument used in Section 3 shows that \(T_m=1\), so the
nonunit \(q_i\) multiply to \(D_r\), and every \(q_i\le B\). Take the first
prefix product exceeding \(r\). If its preceding product is \(s\le r\),
then

\[
r<g=sq_i\le rB\le B^2.
\]

Also \(g\mid D_r\). The endpoint block ledger independently certifies its
occurrences because \(g\mid P\).

If \(N\le B^2\), trial division only through \(\sqrt N\le B\) resolves
\(N\) in polynomial time. Otherwise \(N>B^2\), and the constructed value
satisfies

\[
r<gle B^2<N.
\]

It is therefore legal by Section 2. A canonical-state scan through \(B^2\)
checks each state \(a\) in that range: a nontrivial \(\gcd(a,N)\) resolves
\(N\), while for a unit it computes \(\iota_N(a)\) and emits
\(a\iota_N(a)\). When the scan reaches \(g\), its inverse is \(A_r/g\), so
it emits exactly \(A_r\). Since \(B=\operatorname{poly}(\log N)\), this scan
is polynomial.

Reusing the unchanged source product gives the same mathematical value
\(\gcd(P,A_r)=D_r\). Reusing the unchanged indexed endpoint ledger gives the
same exact capacity and provenance refinement. Thus bounded-quotient
feedback supplies no source state beyond this prior polynomial small-state
scan.

## 7. Equal quotients at \(N=55\)

Both presentations are valid and have quotient one:

\[
2\cdot28=14\cdot4=56=1+55.
\]

For the first presentation, all individual sign screens are trivial:

\[
\begin{array}{c|cc}
g&\gcd(g-1,55)&\gcd(g+1,55)\\ \hline
2&1&1\\
28&1&1.
\end{array}
\]

The alternative presentation is useful because

\[
\gcd(14+1,55)=\gcd(15,55)=5.
\]

Once a quotient-one occurrence is in the source, \(56\mid P\), and hence

\[
D_1=\gcd(P,56)=56.
\]

The gcd saturates the entire target value. It is identical for every indexed
occurrence or endpoint split having that quotient, and it does not say
whether to select \(2\), \(28\), \(14\), \(4\), or another divisor of
\(56\). Thus it gives no localization of the useful alternative
presentation; that information can only come from the indexed endpoint
ledger or a separate selection rule.

## 8. The inverse-difference gcd and both signs

Let \(h=\iota_N(g)\). Since \(\gcd(g,N)=1\), multiplying by \(g\) preserves
a gcd with \(N\). Also \(gh\equiv1\pmod N\). Therefore

\[
\begin{aligned}
\gcd(g-h,N)
 &=\gcd(g(g-h),N)\\
 &=\gcd(g^2-gh,N)\\
 &=\gcd(g^2-1,N).
\end{aligned}
\]

On a non-global involution, \(g^2\equiv1\pmod N\) and the canonical inverse
is \(h=g\), although \(g\not\equiv\pm1\pmod N\) globally. The displayed gcd
is then \(\gcd(0,N)=N\), not a proper factor. The two separate sign screens
\(\gcd(g-1,N)\) and \(\gcd(g+1,N)\) cannot be replaced by this collapsed
quadratic screen.

For \(N=55\) and \(g=21\),

\[
21^2-1=440=8\cdot55,
\]

so \(\iota_{55}(21)=21\) and both inverse-difference gcds equal \(55\).
But

\[
\gcd(21-1,55)=5,
\qquad
\gcd(21+1,55)=11.
\]

Both sign screens must therefore remain.

## 9. Decoder rows do not compress source multiplicity

At \(N=4033\),

\[
A_3=1+3\cdot4033=12100=4\cdot3025.
\]

For one quotient-one occurrence, Section 1 gives

\[
D_3=\gcd(A_3,1-3)=\gcd(12100,2)=2.
\]

For two indexed copies it gives

\[
D_3=\gcd(A_3,(1-3)^2)=\gcd(12100,4)=4.
\]

A repeated decoder row does not enlarge a linear row span. It does,
however, multiply another copy of \(A_1\) into the source product and adds
another unit of the relevant source valuation and occurrence capacity.
Discarding it therefore preserves decoder-lattice span but changes \(P\),
\(D_r\), and the ledger. Decoder-lattice compression is not source
compression.

## 10. Exact gate certificates

For the first four rows, the certificate is the target value and the product
of quotient differences:

\[
\begin{array}{c|c|c|c|c}
N&\{k_i\}&r&A_r&\left|\prod_i(k_i-r)\right|\\ \hline
21&\{1,4\}&9&190&40\\
55&\{1,2\}&8&441&42\\
21&\{1,1,1\}&3&64&8\\
4033&\{1,1\}&3&12100&4.
\end{array}
\]

Thus

\[
\gcd(190,40)=10,
\quad
\gcd(441,42)=21,
\quad
\gcd(64,8)=8,
\quad
\gcd(12100,4)=4.
\]

For the last row,

\[
\begin{aligned}
A_{1983}
 &=1+1983\cdot4033\\
 &=7{,}997{,}440\\
 &=10{,}240\cdot781\\
 &=2^{11}\cdot5\cdot11\cdot71.
\end{aligned}
\]

The absolute quotient differences factor as

\[
\begin{aligned}
1982&=2\cdot991,\\
1920&=2^7\cdot3\cdot5,\\
1976&=2^3\cdot13\cdot19.
\end{aligned}
\]

Their product is

\[
2^{11}\cdot3\cdot5\cdot13\cdot19\cdot991.
\]

The odd cofactor \(11\cdot71\) of \(A_{1983}/(2^{11}\cdot5)\) is coprime
to \(3\cdot13\cdot19\cdot991\): in particular
\(991\equiv1\pmod {11}\) and \(991\equiv68\pmod {71}\), and the remaining
small factors divide neither \(11\) nor \(71\). Hence

\[
D_{1983}=2^{11}\cdot5=10240.
\]

The declared divisor has the exact complement

\[
2048\cdot3905=7{,}997{,}440=A_{1983}.
\]

Both endpoints are below \(4033\), and \(1983<2048\), as required. Also

\[
1985=5\cdot397,
\qquad
10240=2^{11}\cdot5,
\]

so

\[
\gcd(10240,1985)=5.
\]

Finally, let \(t\ge2\) and

\[
N=\frac{2^{2t}-1}{3}.
\]

This is an integer and is at least \(3\). A quotient-one occurrence exists,
for example through

\[
1+N
=2\cdot\frac{2^{2t-1}+1}{3},
\]

whose two endpoints lie strictly between \(1\) and \(N\). Repeat it as \(t\)
indexed occurrences. Since

\[
A_3=1+3N=2^{2t}
\]

and the difference product is \((1-3)^t=(-2)^t\), Section 1 gives

\[
D_3=\gcd(2^{2t},2^t)=2^t.
\]

## Scope of the result

For a declared \(r\), \(D_r\) plus the indexed refinement computes exactly
the supported fibre described in Section 2. None of the arguments proves
that a polynomial target range contains a successful target, that the greedy
member of a nonempty fibre yields a proper factor, or that an all-input
success probability exists. In the bounded-quotient regime, Section 6 shows
that the target relation was already emitted by a polynomial small-state
scan. No factoring algorithm follows from these claims.
