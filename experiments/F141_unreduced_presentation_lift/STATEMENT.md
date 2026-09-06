# F141 candidate statement — compact lifted-word relations

## Status and scope

This is a source and decoder candidate.  It proves a strict expansion of the
F130 retained relation source and one all-size row-reuse law.  It does not
prove a parity dependency, a non-global root on every input, or an integer
factoring algorithm.

The closest results are P118/F130, P120/X73, P123/X75, and P126.  F130
reduces a frozen word before it forms a retained exact value.  X73 shows that
a new endpoint presentation of the same canonical value can change a direct
screen, but does not change the decoder after that screen.  X75 shows that
row width alone need not make a dependency.  P126 forces large rational-prime
rows to reappear when a named block is below \(N/(12n)\).

F141 keeps information that F130 deletes: the exact monomial presentation
before reduction modulo \(N\).

## 1. Lifted source

At a frozen F130 word position, put

\[
U=\prod_{j\in S}q_j^{e_j},\qquad
c=[U]_N,\qquad w=\iota_N(c).
\]

The canonical and lifted values are

\[
A(U)=cw,
\qquad
B(U)=Uw.
\tag{1}
\]

Both are positive units congruent to one modulo \(N\).  F141 retains
\(B(U)\) in addition to \(A(U)\).  It does not delete a lifted position only
because an earlier word has the same residue.  It still runs the canonical
endpoint screens

\[
\gcd(c-w,N),\qquad\gcd(c+w,N).
\]

Using \(U\) instead gives the same gcds because \(U\equiv c\pmod N\).
The integer \(U\) is not a new named generator.  Its exponent presentation
on the frozen named basis is already known.

## 2. Compact factor-free decoder and exact cost

The lifted value need not be expanded.  Retain the exponent vector of \(U\)
and the endpoint \(w<N\).  Joint complete gcd-free refinement of all named
atoms and all retained \(w\)'s gives pairwise-coprime power-free blocks and
an exact exponent vector for every lifted relation.  Reducing these vectors
modulo two gives the exact square-class matrix.

For a binary dependency, every total block exponent is even.  Its square
root modulo \(N\) is

\[
R=\prod_h h^{E_h/2}\pmod N,
\tag{2}
\]

where \(E_h\) is the total exponent of the refined block \(h\).  Modular
binary powering computes (2) from the binary exponent encodings.  Since each
selected lifted value is one modulo \(N\), \(R^2\equiv1\pmod N\).  Testing
\(\gcd(R\pm1,N)\) is therefore the complete P66 root test.  Exact equality
and exact-value deletion can also be decided by comparing the refined
integer exponent vectors.

This compact representation preserves F130's deterministic bound

\[
\boxed{2^{O((\log n)^4)}}.
\tag{3}
\]

Indeed, the number of frozen word positions is unchanged.  Every position
has support at most \(D=L^2\), exponent at most \(E=2^{L^2}\), and named
atoms below \(N\).  Even explicit expansion gives

\[
\log_2 U\le DEn=2^{O(L^2)}.
\]

Multiplying this by the full \(2^{O(L^4)}\) transcript size is still
\(2^{O(L^4)}\).  The compact version only needs the smaller exponent-vector
encoding.  Thus the lift is a genuine source change, not a hidden increase
beyond quasipolynomial time.

## 3. Exact bridge equivalence

The lift is not decoder-equivalent to the canonical column alone.  It does,
however, have an exact standard square-congruence form.  Define

\[
D(U)=Uc,
\qquad c^2\equiv D(U)\pmod N.
\tag{4}
\]

In the exact square-class group,

\[
[B(U)]+[A(U)]=[D(U)],
\tag{5}
\]

because \(A(U)B(U)=D(U)w^2\).  Replacing the pair
\((A(U),B(U))\), with supplied modular square roots \((1,1)\), by
\((A(U),D(U))\), with supplied roots \((1,c)\), is an invertible binary
column operation.  It preserves the normalized-root map: whenever \(D(U)\)
is square, its normalized root is

\[
\sqrt{D(U)}c^{-1}\equiv w\sqrt{D(U)}\pmod N,
\]

which is the root obtained from \(A(U)B(U)\).

Therefore the union of canonical and lifted relations is exactly canonical
F130 plus the factored square congruences

\[
\boxed{Uc\equiv c^2\pmod N.}
\tag{6}
\]

This proves two boundaries at once:

- lifted retention can strictly enlarge the source;
- its algebraic information is a standard modular square-relation source,
  not a new decoder principle.

## 4. Same-residue parity-collision lemma

Let two unit monomials have the same residue and the same parity vector on a
common pairwise-coprime power-free basis:

\[
U=d a^2,\qquad V=d b^2,\qquad U\equiv V=c\pmod N.
\]

With \(w=\iota_N(c)\), the two lifted columns close exactly:

\[
(Uw)(Vw)=(dabw)^2.
\tag{7}
\]

Their normalized root is

\[
dabw\equiv ba^{-1}\pmod N.
\tag{8}
\]

Thus this pair factors \(N\) exactly when the congruence
\(a^2\equiv b^2\pmod N\) has mixed CRT signs.  Equivalently, a proper factor
is one of \(\gcd(a-b,N)\) and \(\gcd(a+b,N)\).

This mechanism is a bounded multiplicative order or rational-square
collision.  It explains the clean collision certificates, but it does not
show how to find such a collision on every input in quasipolynomial time.

## 5. A distinct-residue squared-anchor theorem for large blocks

Let

\[
n=\lceil\log_2(N+1)\rceil,\qquad A=n^3,
\]

and assume \(n\ge64\).  Let \(q\) be a current named unit block with

\[
q\ge\frac{N}{12n}.
\tag{9}
\]

Screen every prime \(\ell\le A\) against \(Nq\).  A nontrivial gcd factors
\(N\) or strictly splits \(q\).  For every remaining eligible prime, form
the already-allowed support-two word

\[
U_\ell=q\ell^2,\qquad
c_\ell=[U_\ell]_N,\qquad
w_\ell=\iota_N(c_\ell),\qquad
B_\ell=q\ell^2w_\ell.
\tag{10}
\]

The complete initial F130 seed bank contains every such prime, and (10) is a
literal frozen F130 word position.  On the branch where no declared gcd has
factored \(N\) and no \(\gcd(q,w_\ell)\) strictly splits \(q\), call an
anchor good when \(q\nmid w_\ell\).  Then:

1. the residues \(c_\ell\), and hence the inverses \(w_\ell\), are pairwise
   distinct;
2. fewer than \(12n\) anchors are not good;
3. after global exact-value deletion, more than \(n^2/5\) distinct retained
   exact values from (10) remain good; and
4. every rational prime row \(r\mid q\) with \(v_r(q)\) odd occurs oddly in
   all of those values.

In particular, the unreduced lift forces polynomially many columns to reuse
all odd rows of every named block above the P126 size cutoff.  These are
distinct-residue relations, not same-residue order collisions.

Together with P126, this removes the specific objection that a large named
block cannot be touched by a polynomial public anchor bank.  It does not
prove that the resulting columns have a rank defect.  Their \(w_\ell\)
cofactors can still contribute fresh rows and form a peelable forest.

For this large-block theorem, compact storage is optional.  Each displayed
word satisfies \(U_\ell<Nn^6\), so it has \(O(n)\) bits even when expanded.

## 6. Registered finite certificates

The registered F141-D01 computation passed.

### A large literal F130 order collision

Let

\[
p=1238926361552897,\qquad
q=5704689200685129054721,\qquad N=pq.
\]

Both numbers are prime,

\[
p\mid2^{256}+1,\qquad q\mid2^{256}-1.
\]

For this 123-bit input, the F130 cap is \(E=2^{49}\), both factors exceed
\(E+1\), and the support-one exponents \(1,513\) are allowed.  The two words

\[
U_1=2,\qquad U_2=2^{513}
\]

have residue \(2\) and inverse \(w=(N+1)/2\).  Both endpoint screens are
one.  Canonical residue deletion keeps the single nonsquare value \(N+1\),
so the matched canonical one-column kernel is zero.  The lifted product is

\[
(2w)(2^{513}w)=(2^{257}w)^2.
\]

Its normalized root is \(2^{256}\), and

\[
\gcd(2^{256}-1,N)=q,\qquad
\gcd(2^{256}+1,N)=p.
\]

If an earlier F130 seed screen factors this input, the algorithm has already
succeeded.  Otherwise these are valid positions in its first frozen stage.
This does not say that the complete canonical F130 source is null.

### Exhaustive small slice

The script scanned all 903 semiprimes \(pq\) with
\(7\le p<q\le199\), using \(U_e=2^e\) for \(1\le e\le24\).  Of these, 178
were direct-null for the complete declared slice.

On five inputs the matched canonical normalized-root image was global while
the lifted image was non-global.  The first was

\[
N=7169=67\cdot107.
\]

The canonical ledger had rank 18 and nullity zero.  The lifted ledger had
rank 14 and nullity two.  Its exponent-24 value was already a useful square:

\[
2^{24}\cdot6724=112810000384=335872^2,
\]

and

\[
\gcd(335872-1,N)=67,\qquad
\gcd(335872+1,N)=107.
\]

The scan found three inputs with a useful same-residue pair and 24 with a
useful one-column square.  It found no useful weight-two or weight-three
binary circuit whose residues were all distinct.  This last result is only a
finite null for the fixed small corpus.

## Exact remaining gate

The lifted source now has a clean algebraic meaning and it forces
distinct-residue reuse for large blocks.  The hard missing statement is:

> After the fresh cofactor rows are included, prove that some
> quasipolynomial lifted-word layer has a strict parity-rank defect and that
> its normalized-root image is non-global on every surviving input.

Neither the same-residue order certificate nor the squared-anchor width
theorem proves this statement.
