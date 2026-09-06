# F132 proof — cost, exact row law, and counterexamples

## 1. Units and block sizes

Every endpoint in the explicit conditional seed list is a unit modulo \(N\)
after its initial gcd screen. In the uniform composition, this is the
no-factor branch after F130. A
divisor of a unit endpoint is also a unit modulo \(N\). Thus every current
gcd-free block is a unit, and every declared canonical inverse exists.

Every block divides at least one endpoint smaller than \(N\), so every block
is itself smaller than \(N\).

## 2. Transcript-length recurrence

Let \(\mathcal A_t\) be the accumulated endpoint transcript after round \(t\),
and put

\[
\Lambda_t=
\sum_{a\in\mathcal A_t}\lceil\log _2(a+1)\rceil.
\]

Keeping duplicate endpoints only makes this upper bound larger. Let \(M_t\)
be the number of blocks in the complete pairwise-coprime basis of
\(\mathcal A_t\). One copy of every block divides the product of all endpoints.
Since every block is greater than one,

\[
2^{M_t}
\le \prod_{q\in\mathcal B_t}q
\le \prod_{a\in\mathcal A_t}a
<2^{\Lambda_t}.
\]

Hence

\[
M_t\le\Lambda_t.
\tag{1}
\]

Round \(t+1\) generates at most \(M_tE\) endpoint pairs. Every endpoint has
at most \(n\) bits. Therefore

\[
\Lambda_{t+1}
\le\Lambda_t+2nEM_t
\le(1+2nE)\Lambda_t.
\tag{2}
\]

The seed phase has at most \(E\) pairs, so

\[
\Lambda_0\le2nE.
\]

Iterating (2) for \(T=L^2\) rounds gives

\[
\Lambda_T
\le2nE(1+2nE)^T.
\]

Now \(\log _2n\le L\), \(\log _2E=L^2\), and \(T=L^2\). Thus

\[
\log _2\Lambda_T=O(L^4),
\qquad
\Lambda_T,M_t\le2^{O(L^4)}.
\tag{3}
\]

The total number of generated word positions is at most

\[
E\sum_{t<T}M_t
\le ET\Lambda_T
=2^{O(L^4)}.
\tag{4}
\]

## 3. Arithmetic and final-decoder cost

An exponent \(e\le E\) has \(O(L^2)\) bits. Repeated squaring computes each
\([q^e]_N\) with \(O(L^2)\) modular multiplications. Every inverse, direct
screen, endpoint, and exact value has \(O(n)\) bits; in particular,

\[
P_N(c)=c\iota_N(c)<N^2.
\]

Complete gcd-free refinement is polynomial in its explicit endpoint input
length. Equations (3) and (4) show that running it in all \(T\) rounds costs
\(2^{O(L^4)}\). The first-occurrence exact-value ledger has at most the number
of generated positions, so its P66 input length is also \(2^{O(L^4)}\).
P66 is polynomial in that explicit length, including its kernel-basis root
tests. This proves Theorem 1.

For the stronger F130 composition, replace the seed bound by

\[
\Lambda_0\le2^{C L^4}
\]

for some fixed constant \(C\), as supplied by the proved F130 transcript-cost
bound. The same recurrence (2) gives

\[
\log_2\Lambda_T
\le CL^4+T\log_2(1+2nE)
=O(L^4).
\]

All later bounds are unchanged. The old F130 relation ledger contributes only
\(2^{O(L^4)}\) additional bits to the final P66 input.

F130 admits to its named basis only descendants of its fixed initial endpoint
product. A terminal block that occurs only in a probe cofactor is explicitly
discarded from that generator state. Complete all-endpoint refinement retains
that same block, and the unary rule enumerates its powers in the next round.
Therefore the composed declared generator state is genuinely larger whenever
such a block exists. This statement is about the source grammar. It does not
assert that the new residue or exact value was inaccessible by every other
F130 word.

The argument uses the declared fixed round cap. It gives no comparable bound
for “repeat until no novel all-block factor occurs.”

## 4. Divisor-feedback identity

Let

\[
P_0=1+kN
\]

be an old exact value divisible by a current block \(q\). If \(q>k\), then

\[
h=P_0/q
\]

is a positive integer and

\[
h<\frac{qN}{q}=N.
\]

Also \(qh=P_0\equiv1\pmod N\). Therefore \(h\) is the least positive inverse
of \(q\), and

\[
P_N(q)=P_0.
\tag{5}
\]

If \(P_N(q)\) is absent from the old ledger, (5) cannot hold for any old
incident value. Hence \(q\le k\) for every such value.

If (5) holds, the old complete basis already gives a monomial presentation
of \(P_0\). Since \(q\) is one current block, \(P_0/q\) is also a monomial in
the same blocks, with one copy of \(q\) removed. Inserting the endpoint pair
\((q,P_0/q)\) cannot refine the basis.

If one retained both equal columns, their difference vector would have exact
product \(P_0^2\), positive root \(P_0\), and normalized residue

\[
P_0\equiv1\pmod N.
\]

Thus exact-value deduplication removes only a global-root direction.

Deduplication must occur after the new endpoint screens. Put
\(h=\iota_N(q)\). Multiplication by the unit \(q\) gives

\[
\gcd(q-h,N)=\gcd(q^2-1,N),
\qquad
\gcd(q+h,N)=\gcd(q^2+1,N).
\tag{6}
\]

These screens depend on the endpoint presentation, not only on the exact
value. Therefore an exact duplicate can still return a factor. Only on the
branch where both gcds are nonproper can its endpoint refinement and decoder
direction be discarded.

For a new value \(P_N(q)=q\iota_N(q)\), its hidden prime-parity entry is
exactly

\[
v_r(P_N(q))
\equiv v_r(q)+v_r(\iota_N(q))\pmod2.
\tag{7}
\]

The second term in (7) can cancel the first. This proves Theorem 2. For
\(e\ge2\), modular reduction destroys even the integer divisibility premise:
\([q^e]_N\) is a residue representative, not the unreduced integer power.

## 5. Private-row splice law

First embed every old and new column in the common union of their prime rows,
adding zero entries where needed. Write the old parity matrix, after putting
its private row first and its private column last, as

\[
M=
\begin{pmatrix}
0&1\\
\widehat M&\widehat v
\end{pmatrix}.
\]

Append

\[
u=\binom{u_r}{\widehat u}.
\]

If a kernel vector has coefficients \((x,a,b)\), where \(a\) is the old
private-column coefficient and \(b\) is the new coefficient, its first row is

\[
a+u_rb=0.
\tag{8}
\]

If \(u_r=0\), equation (8) forces \(a=0\). The remaining equation is

\[
\widehat Mx+b\widehat u=0.
\]

The nullity grows exactly when
\(\widehat u\in\operatorname{colspan}(\widehat M)\).

If \(u_r=1\), equation (8) gives \(a=b\). Substitution leaves

\[
\widehat Mx+b(\widehat v+\widehat u)=0.
\]

The nullity grows exactly when

\[
\widehat v+\widehat u
\in\operatorname{colspan}(\widehat M).
\]

This proves Theorem 3. It also explains the peeling limitation. A fresh
private row of \(u\) forces \(b=0\); equation (8) then forces \(a=0\), so the
temporary reuse disappears in a two-column peeling cascade.

If \(u=v\), the contracted parity column is zero. If the two exact integer
values are also equal, Section 4 proves that the duplicate direction has
normalized root \(+1\). If two distinct exact values only have equal parity
columns, no root conclusion follows.

## 6. Complete-universe privacy

Choose one inverse endpoint orbit \(\{c,\iota_N(c)\}\) for every distinct exact
value. Distinct exact values have disjoint inverse orbits.

If a prime \(r>(N-1)/2\) divides an exact value, it divides at least one of
its two endpoints. The only positive multiple of \(r\) below \(N\) is \(r\)
itself. Therefore every exact value divisible by \(r\) comes from the single
inverse orbit

\[
\{r,\iota_N(r)}.
\]

There is at most one such exact value after global deduplication. If it has
odd \(r\)-valuation, its row degree is exactly one in the complete universe.

Apply this to every generated residue \(c=[r^e]_N\). If its exact value is
divisible by \(r\), its inverse orbit is the orbit above, so its exact value
is the old duplicate. Otherwise its \(r\)-valuation is zero. This proves
Theorem 4 for arbitrarily many rounds and arbitrarily large exponent menus.

Degree-one peeling forces the coordinate of the unique incident column to
zero in every dependency. It preserves every dependency and root supported
on the remaining columns, so the theorem says nothing about success
elsewhere.

## 7. Verification of Certificate A

For \(N=253=11\cdot23\),

\[
26\cdot146=3796=1+15\cdot253=2^2\cdot13\cdot73.
\]

Since

\[
26=2\cdot13,
\qquad
146=2\cdot73,
\]

complete gcd-free refinement exposes \(q=13\). Its inverse is \(39\), and

\[
13\cdot39=507=1+2\cdot253=3\cdot13^2.
\]

The values \(3796\) and \(507\) are distinct. Their parity supports are
\(\{13,73\}\) and \(\{3\}\). In particular, the new \(13\)-entry is zero.
Direct Euclidean calculation gives

\[
\gcd(120,253)=\gcd(172,253)=
\gcd(26,253)=\gcd(52,253)=1.
\]

Thus no declared endpoint sign screen explains the failure. Both columns
have a private row, so the binary matrix has rank two and empty 2-core.

## 8. Verification of Certificate B

For \(N=77=7\cdot11\),

\[
4\cdot58=232=1+3\cdot77=2^3\cdot29,
\]

and the endpoints expose \(\{2,29\}\). The inverse of \(2\) is \(39\), with

\[
2\cdot39=78=1+77=2\cdot3\cdot13.
\]

The two values are distinct. Their parity supports are
\(\{2,29\}\) and \(\{2,3,13\}\), so row \(2\) has degree two. However, row
\(29\) forces the first column to zero and either row \(3\) or \(13\) forces
the second column to zero. The greatest degree-one-peeled column set is empty.

The four sign-screen magnitudes are \(54,62,37,41\), each coprime to \(77\).

## 9. Verification of Certificate C

For \(N=91=7\cdot13\),

\[
2\cdot46=92=1+91=2^2\cdot23.
\]

The endpoint gcd is \(2\), and division exposes the basis \(\{2,23\}\).
The inverse of \(23\) is \(4\), so unary feedback gives the same exact value
\(23\cdot4=92\). The alternative endpoints use only the old basis.

The four sign-screen magnitudes are \(44,48,19,27\), each coprime to \(91\).
The raw duplicate root is \(92\equiv1\pmod {91}\). Thus this branch changes
neither the basis nor the normalized-root image.

## 10. Verification of Certificate D

For \(N=63=3^2\cdot7\), both \(8\) and \(62\) are self-inverse:

\[
8^2=64=1+63,
\qquad
62^2=3844=1+61\cdot63.
\]

Their sign-screen magnitudes are \(0,16,0,124\). The zero screens are global,
and the other two are coprime to \(63\), so neither old presentation gives a
proper factor. Complete endpoint refinement of \(8=2^3\) and
\(62=2\cdot31\) exposes the block \(q=2\). Its canonical inverse is \(32\),
and

\[
2\cdot32=64.
\]

This is an exact-value duplicate, but

\[
\gcd(2-32,63)=\gcd(30,63)=3.
\]

The plus screen is null: \(\gcd(34,63)=1\), so only the minus screen returns a
factor. This verifies that the new presentation must be screened before it is
discarded.

## 11. Boundary

The all-block rule is materially stronger than descendant-only named
refinement because a novel cofactor can generate words in the next round.
The transcript recurrence proves that this stronger state is affordable for
\(T=L^2\) rounds.

The proofs above also separate four events:

1. a new exact value appears;
2. it has odd incidence in a selected old row;
3. its columns survive degree-one peeling and close a parity circuit; and
4. the circuit has non-global normalized root.

None of the first three implies the next. An all-input success theorem must
control the fourth event or produce a direct factor independently. P119/F131
gives an exact example where distinct values close but their root is global.
