# F141 blind reconstruction

Statement SHA-256: `64bf45085bfef91190be4e23021e5e4bebbc6a9f48e03db56e49b087cf2b4bcf`

Report-body SHA-256: `3b4fb31aef635e42e4913a3cc01ab20bdcbe55811869b37bfffa207bc1f2819a`

Hash convention: the report-body hash is the SHA-256 of this UTF-8 file after
deleting the complete line that starts with `Report-body SHA-256:`. This avoids
a self-referential hash.

## Audit boundary

I read only `STATEMENT.md` in the F141 directory. I did not read the proof,
audit, manifest, source, output, log, verifier, or another F141 file. I did not
run a mathematical search or certificate computation. I treated the registered
finite results as statement data, as requested.

## Verdict

**Pass, with explicit inherited-interface qualifications.** The new algebraic
claims and the large-block counting theorem reconstruct from first principles.
The theorem in fact gives a stronger intermediate lower bound than the stated
`n^2/5` bound.

Two facts are inherited from F130 rather than proved inside this statement:

1. the definitions relating `L`, `n`, the exponent cap, and the full F130
   transcript-size bound; and
2. the assertion that every word `q ell^2` in the stated range is a literal
   frozen F130 word position.

The conclusions about cost and source inclusion are valid conditional on those
declared F130 interface facts. The finite primality, rank, nullity, and scan
counts are also inputs to this audit, not independently recomputed facts.

No claim in the statement supplies the missing global parity-rank defect or a
non-global normalized root for every surviving input.

## 1. Lifted source

Let `c` be the unit residue of `U` modulo `N`, and let `w` be its inverse in the
chosen interval. Then

\[
cw\equiv Uw\equiv1\pmod N.
\]

All factors are positive units, so both `A(U)=cw` and `B(U)=Uw` are positive
units. Also, `N` divides `U-c`. Hence

\[
\gcd(U\pm w,N)=\gcd(c\pm w,N).
\]

The lift therefore changes the retained exact integer and not the endpoint
screen. It introduces no generator: `U` is already specified by its exponent
vector on the named basis.

## 2. Compact factor-free decoding and cost

A complete gcd-free refinement can be obtained using gcds and exact
perfect-power decomposition. It does not require prime factorization. After
refinement, distinct blocks are pairwise coprime, and each block is power-free
in the sense needed for square classes. Every

\[
B(U)=\left(\prod_j q_j^{e_j}\right)w
\]

then has an exact exponent vector. Pairwise coprimality and removal of proper
powers imply that a product is an integer square exactly when every total block
exponent is even. Thus reduction of the exponent vectors modulo two is the
exact square-class matrix, not a relaxation.

For a kernel vector, let `E_h` be the total integer exponent of block `h`.
Then

\[
R=\prod_h h^{E_h/2}\pmod N
\]

is the exact square root of the selected integer product, reduced modulo `N`.
All selected lifted values are `1` modulo `N`, so `R^2=1` modulo `N`. Modular
binary powering uses only the binary encodings of the exponents. For the usual
odd factoring scope, a non-global root assigns both signs among the prime-power
CRT components. Therefore one of `gcd(R-1,N)` and `gcd(R+1,N)` is a proper
factor. A global root `+1` or `-1` gives no factor. This is exactly the standard
root test.

The same canonical refined basis makes exact integer equality equivalent to
equality of exponent vectors. For comparisons with canonical F130 columns, one
must also use the already-present canonical factors (in particular the residue
factor `c`) or compare the bounded expanded integers. Either method is within
the stated bound.

The raw size estimate is direct:

\[
\log_2 U
 =\sum_{j\in S}e_j\log_2q_j
 < |S|En
 \le DEn.
\]

With `D=L^2` and `E=2^(L^2)`, this is `L^2 2^(L^2)n`. Under the inherited F130
relation `log n=O(L)`, it is `2^{O(L^2)}` bits. Multiplying by a full transcript
of size `2^{O(L^4)}` remains `2^{O(L^4)}`. Gcd-free refinement, perfect-power
tests, exact comparisons, and modular powering take polynomial time in this
total bit volume. Hence they preserve

\[
2^{O(L^4)}=2^{O((\log n)^4)}.
\]

The equality to the last expression and the transcript bound depend on the
frozen F130 definition of `L`; they do not follow from an independent
definition in this statement.

## 3. Exact bridge and normalized roots

Set `D=Uc`. Since `U=c` modulo `N`,

\[
D\equiv c^2\pmod N.
\]

Also

\[
A B=(cw)(Uw)=Uc\,w^2=Dw^2,
\]

so `[A]+[B]=[D]` in the exact square-class group.

The binary column replacement is explicit. If `(x,y)` selects the old columns
`(A,B)`, select `(x+y,y)` on the new columns `(A,D)`, with addition modulo two.
Because `D=A+B` in square class, this map and its inverse preserve every kernel
vector.

The supplied modular roots are essential. They are `(1,1)` for `(A,B)` and
`(1,c)` for `(A,D)`. The four selector cases show normalized-root preservation:

- For `(0,0)` and `(1,0)`, nothing changes.
- For `(0,1)`, the new exact product is `AD=Bc^2`. Its exact root gains a
  factor `c`, and its supplied modular root also gains `c`.
- For `(1,1)`, the old exact product is `AB=Dw^2`. If `t^2=D`, the old
  normalized root is `wt`, while the new normalized root is
  `tc^{-1}=tw` modulo `N`.

The argument multiplies over positions, so it also covers dependencies for
which only a product of several `D` columns is square. It is not limited to a
single square `D`.

Thus the union is isomorphic, as a square-congruence source with normalized
roots, to canonical F130 plus

\[
Uc\equiv c^2\pmod N.
\]

This is an algebraic source equivalence. It is not literal equality of the two
integer multisets. If transformed `D` columns are deduplicated, their supplied
roots must remain part of the relation data; equality of `D` alone is not a
license to discard a different supplied root without first testing the root
collision.

## 4. Same-residue parity collision

Equal parity vectors on a common pairwise-coprime power-free basis give

\[
U=da^2,\qquad V=db^2
\]

for integers `d,a,b`. Because `U` and `V` are units, all three are units modulo
`N`. If they have common residue `c` and inverse `w`, then

\[
(Uw)(Vw)=d^2a^2b^2w^2=(dabw)^2.
\]

Using `da^2w=1` modulo `N` gives

\[
dabw\equiv ba^{-1}\pmod N.
\]

Cancelling `d` from `da^2=db^2` modulo `N` gives `a^2=b^2` modulo `N`.
For odd `N`, the unit `ba^{-1}` is `+1` or `-1` on each prime-power CRT
component. The root is useful exactly when both signs occur. Equivalently,
`gcd(a-b,N)` and `gcd(a+b,N)` expose the two nonempty component sets. This
proves (7), (8), and the stated factoring criterion. The “mixed CRT signs”
wording presumes the standard odd-input preprocessing; powers of two have
additional square roots of one.

This is an order-at-most-two collision for the ratio `ba^{-1}`. It supplies a
mechanism, not a method that finds such a pair on every input.

## 5. Large-block squared-anchor theorem

Write `pi(x)` for the number of primes at most `x`, and use natural logarithms
in this section.

### Basic size and source facts

From `n=ceil(log2(N+1))`,

\[
2^{n-1}\le N<2^n.
\]

For `n>=64`, elementary monotonicity gives `n^6<N`. It also gives
`N/(12n)>n^3`. Hence `q>=N/(12n)` is larger than every anchor prime and is
distinct from it.

For a prime `ell<=n^3`, a nontrivial `gcd(ell,Nq)` equals `ell`. If `ell`
divides `N`, it is a proper factor because `ell<N`. If it does not divide `N`,
it divides `q` and strictly splits `q` because `ell<q`. Every remaining anchor
is coprime to both `N` and `q`.

The claim that the initial seed bank contains all these primes, and that the
support-two exponent pattern `(1,2)` is a literal frozen position, is an
inherited F130 source-definition fact stated in F141. Given that fact, (10) is
indeed in the source: it uses the current named block `q`, a seeded prime
`ell`, support two, and exponents within the declared caps.

### Distinct residues and inverses

Suppose `c_ell=c_m` for two eligible anchors. Cancelling the unit `q` modulo
`N` gives

\[
\ell^2\equiv m^2\pmod N.
\]

But both squares are below `n^6<N`. Therefore they are equal as integers, and
positive primality gives `ell=m`. The residues are pairwise distinct. Inversion
on the unit residues is a bijection, so the chosen inverses `w_ell` are also
pairwise distinct.

### Bad inverse count

The interval `1<=w<N` contains exactly `floor((N-1)/q)` multiples of `q`.
Using `q>=N/(12n)` gives

\[
\left\lfloor\frac{N-1}{q}\right\rfloor
 <\frac Nq\le12n.
\]

Since the inverses are distinct, fewer than `12n` anchors are bad.

On the branch with no strict split of `q`, a good anchor has
`gcd(q,w_ell)=1`: its gcd is neither a proper divisor of `q` nor all of `q`.

### Prime supply and exact-value collisions

It is enough to use anchor primes in `(n^2,n^3]`. The standard explicit bounds

\[
\pi(x)>\frac{x}{\log x}\quad(x\ge17),\qquad
\pi(x)<\frac{2x}{\log x}
\]

give more than

\[
\frac{n^3}{3\log n}-\frac{n^2}{\log n}
\]

primes in this interval. Fewer than `2n` distinct primes divide `Nq`, because
`q<N` and hence `Nq<N^2<2^{2n}`. Removing these and the fewer than `12n` bad
anchors leaves a number `G` of eligible good high anchors satisfying

\[
G>
\frac{n^3}{3\log n}-\frac{n^2}{\log n}-14n
>\frac{n^3}{4\log n}.
\tag{A}
\]

The last inequality holds at `n=64` and its positive margin increases for
`n>=64`; equivalently,
`n(n/12-1)>14 log n`.

Now fix one exact integer value `X` shared by `t` good high anchors. For every
anchor in this collision class,

\[
X/q=\ell^2w_\ell<n^6N.
\]

The distinct eligible primes are coprime to `q`. Each `ell^2` divides `X/q`,
so their product does too. Since every `ell>n^2`,

\[
n^{4t}<\prod_{i=1}^t\ell_i^2\le X/q<n^6N<n^6 2^n.
\]

Consequently

\[
t<\frac32+\frac{n\log2}{4\log n}
  <\frac{n}{2\log n}\qquad(n\ge64).
\tag{B}
\]

Combining (A) and (B), the number of distinct good exact values is greater
than

\[
\frac{n^3/(4\log n)}{n/(2\log n)}=\frac{n^2}{2},
\]

which is stronger than the claimed `n^2/5`.

Global keep-one exact-value deduplication cannot reduce the count of distinct
integer values. A good anchor value also cannot equal a bad anchor value. If
it did, `q|w_m` on the bad side would imply `q|ell^2w_ell` on the good side,
contradicting `gcd(q,ell w_ell)=1`. A duplicate with a non-anchor column still
leaves one representative of the same integer, whose rational-prime parities
are intrinsic. Thus the bound survives global exact-value deduplication.

### Odd row reuse

Let a rational prime `r` divide `q` to odd valuation. Eligibility gives
`r` not dividing `ell`, and goodness on the no-split branch gives `r` not
dividing `w_ell`. Therefore

\[
v_r(B_\ell)=v_r(q)+2v_r(\ell)+v_r(w_\ell)=v_r(q),
\]

which is odd. Every odd row of `q` occurs in every counted exact value. This
property belongs to the exact integer, so choosing another presentation during
deduplication does not change it.

Finally,

\[
U_\ell=q\ell^2<Nn^6,
\]

so its bit length is at most `n+6 log2(n)=O(n)`. Compact storage is not needed
for this layer.

The theorem proves polynomial width and common-row reuse. It gives no rank
defect because the `w_ell` factors can introduce distinct odd rows. A peelable
matrix is still possible.

## 6. Logical role of the finite certificates

### Large order collision

Take the stated primality and divisibility facts as certificate data. From

\[
p\mid2^{256}+1,\qquad q\mid2^{256}-1
\]

we get `2^512=1` modulo both distinct primes, hence modulo `N=pq`. Therefore
`2^513=2` modulo `N`. Since `N` is odd, the inverse of `2` is `(N+1)/2`.

The endpoint claims also follow without a large computation. Multiplying the
two endpoint arguments by the unit `2` reduces their gcds with `N` to the gcds
of `3` and `5` with `N`. Neither large prime is `3` or `5`. Thus both screens
are one.

Canonical residue deletion retains `2w=N+1`. The displayed primes are both
`1` modulo `4`, so `N+1` is `2` modulo `4` and is not an integer square. The
matched one-column canonical kernel is therefore zero.

For the lifted pair,

\[
(2w)(2^{513}w)=2^{514}w^2=(2^{257}w)^2,
\]

and `2w=1` modulo `N` makes its normalized root `2^256`. The two stated
divisibilities, together with the fact that an odd prime cannot divide both
`2^256-1` and `2^256+1`, give exactly

\[
\gcd(2^{256}-1,N)=q,\qquad
\gcd(2^{256}+1,N)=p.
\]

The cap and source-position facts are finite statement data. Numerically,
`513<2^49` and the displayed factors exceed `2^49+1`, so those assertions are
internally consistent.

This certificate proves that the lift can strictly improve the matched source.
It does not prove that the complete canonical F130 source fails, and the
statement correctly says so.

### Small exhaustive slice

There are 43 primes from `7` through `199`, and `43 choose 2=903`, so the
corpus size is consistent. The scan totals, ranks, and nullities are accepted
as registered statement data.

For the first displayed input, `67*107=7169`. Also

\[
6724=82^2,\qquad335872=2^{12}\cdot82,
\]

so

\[
2^{24}\cdot6724=335872^2.
\]

The two gcd identities put the root at `+1` modulo `67` and `-1` modulo `107`.
Thus it is a useful mixed-sign root, and the one-column lifted square has the
claimed logical effect. The reported absence of small distinct-residue
circuits is only a null result for that finite corpus. It cannot support a
universal absence claim.

## 7. Exact scope

The reconstruction establishes:

- a compact, factor-free decoder with the inherited quasipolynomial bound;
- an exact square-congruence bridge that preserves normalized roots;
- the same-residue collision criterion;
- more than `n^2/5` globally distinct good anchor values for every named unit
  block above `N/(12n)`, with all odd rows of that block reused; and
- finite examples in which lifted retention adds useful information.

It does not establish a parity dependency, a non-global normalized root on
every input, or an integer factoring algorithm. Fresh cofactor rows remain the
precise obstruction. This matches the statement's declared remaining gate.
