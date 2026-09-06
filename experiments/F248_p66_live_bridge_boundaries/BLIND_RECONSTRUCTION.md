# F248 blind reconstruction

## Blind boundary and verdict

Before opening the statement, I authenticated
`STATEMENT.md` as

```text
3f45f82829715678e2950dc07c80296e4c3f8230baf9d34bc84d5e2381bd3621
```

I then used only that file among the F248 theorem, proof, audit, provenance,
and history artifacts.  I used no numerical experiment and no external
source.

**Verdict: FAIL as a complete statement-only reconstruction.**  The
self-contained algebraic and counting parts of Theorems A--G reconstruct.
The P208/P209 specializations do not: the permitted statement never defines
P208, P209, their orientations or private markers, or the covered
signed-power grammar.  Thus their asserted values of (K), exponential
lower bounds for (H,H'), and coprimality/marker claims cannot be derived
from the supplied data.  Conditional on those missing family facts, their
negligibility consequences follow.

The proofs and exact residual scope are below.

## Elementary facts used throughout

1. By CRT,
   
   \[
   (\mathbb Z/N^2\mathbb Z)^\times\cong
   (\mathbb Z/p^2\mathbb Z)^\times\times
   (\mathbb Z/q^2\mathbb Z)^\times .
   \]
   
   Each local group is cyclic of order (r(r-1)).  Since
   (gcd(E,N)=1), the kernel of the (E)-power map has local size
   (gcd(E,r-1)=g_r), hence global size (K=g_pg_q).  Every nonempty
   fibre of that map is a coset of this kernel and has size (K).

2. A unit square modulo (N=pq) has exactly four roots modulo (N).
   Exactly two normalized roots of (1) are global, ((1,1)) and
   ((-1,-1)), and exactly two are mixed.  A mixed root (w) gives a
   factor through (gcd(w-1,N)), equivalently through one of the two
   signed gcds before normalization.  The same CRT argument gives exactly
   four roots of (1) modulo (N^2).

3. (arphi(N^2)=Narphi(N)).  Also, for distinct odd primes,
   (arphi(N)=2^{n+O(1)}).

4. Uniformly for positive integers (m) of (O(n)) bits,
   (	au(m)=2^{o(n)}).  One elementary proof is that, for every fixed
   (epsilon>0), all sufficiently large primes satisfy
   (a+1\le \ell^{\epsilon a}) for (a\ge1).  The finitely many smaller
   primes contribute an (epsilon)-dependent constant after maximizing
   ((a+1)/\ell^{\epsilon a}).  Thus
   (	au(m)\le C_\epsilon m^epsilon), and then let (epsilon) tend to
   zero.

## Theorem A: uniform full lifts

There are exactly (arphi(N)) possible integer squares in
({1,ldots,N^2-1}) that are units modulo (N^2): they are (s^2) with
(1\le s<N) and (gcd(s,N)=1).  Each such output has either zero or (K)
preimages under the (E)-power map.  Therefore

\[
 \Pr([A^E]_{N^2}\text{ is an integer square})
 \le {K\varphi(N)\over\varphi(N^2)}={K\over N}.
\]

Fix a square output (s^2) that is in the image, and fix one preimage
(A_0).  All preimages are (A_0k), with (k) uniform in the kernel.
Their supplied roots are consequently uniform, with equal fibre sizes, on

\[
 [A_0^{E/2}]_N\cdot
 \operatorname{im}\bigl(k\mapsto[k^{E/2}]_Nigr).
\]

On the (r)-side, the kernel is cyclic of order
(g_r=gcd(E,r-1)).  Every (k^{E/2}) in question squares to (1).  Write
(e=v_2(E)) and (t=v_2(r-1)).  The image size is

\[
 {g_r\over\gcd(g_r,E/2)}=
 \begin{cases}
 2,&e\le t,\\
 1,&e>t.
 \end{cases}
\]

Thus the local image is respectively ({1,-1}) or ({1}).  If at
least one local side has the two-element image, any coset of the resulting
subgroup of the four roots of (1) contains equally many global and mixed
roots.  Exactly half of the preimages of the fixed square output therefore
factor (N).

The claimed P209 values (K=4) for (E=N-1), (K=24) for
(E=N^2-1), and the claimed active/trivial local-image patterns require the
missing definition of P209.  If those values and patterns are assumed, all
three stated consequences follow.  In particular, (Q(n)K/N=2^{-\Omega(n)})
for a quasipolynomial number (Q(n)) of trials and fixed (K).

## Theorem B: a principal fibre

Binomial expansion modulo (N^2) gives

\[
 (a_0+tN)^E\equiv a_0^E+E a_0^{E-1}tN\pmod{N^2}.
\]

After separating the fixed residue (r=[a^E]_N), this is

\[
 h_t\equiv h_0+Ea^{E-1}t\pmod N.
\]

The slope is a unit because both (E) and (a) are units modulo (N).
Hence (t\mapsto h_t) is a bijection on the (N) lift digits.

Now (r=x^2\bmod N) is a unit square.  Its four roots modulo (N) have
four distinct representatives (s) in ({1,ldots,N-1}).  Their four
distinct integer squares (s^2<N^2) are exactly all integer-square outputs
congruent to (r) modulo (N).  The digit bijection therefore gives
exactly four square members of the fibre.  As (s) runs over the four
roots, (s/x) runs over all four roots of (1); exactly two are mixed.
This proves the probabilities (4/N) and (2/N).

The advertised equivalence is explicit.  A successful digit gives the
integer root (s), and (gcd(s-x,N)) or (gcd(s+x,N)) is nontrivial.
Conversely, given (p,q), CRT constructs the two roots of (r) that are
not (pm x).  For either least representative (s), compute

\[
 h={s^2-r\over N},\qquad
 t\equiv(h-h_0)(Ea^{E-1})^{-1}\pmod N.
\]

These are precisely the two successful digits.  Thus locating one of them
and finding a mixed second root are polynomial-time interreducible in this
setting.

### Fixed-past extension

Write the fixed integer (P) uniquely as (P=c^2d), where (d) is
squarefree.  If (PB_t) is a square, parity of prime valuations forces

\[
 B_t=dz^2
\]

for an integer (z).  Since (B_t<N^2), one has
(0\le z<N/\sqrt d\le N).  All of (c,d,z) are units modulo (N) whenever
such a row occurs.  Put

\[
 \delta=cdX^{-1}\pmod N.
\]

From (X^2\equiv c^2d) one obtains (delta^2\equiv d).  The positive
integer root of (PB_t) is (S=cdz), and its normalized root is

\[
 {S\over Xx}\equiv {\delta z\over x}\pmod N.
\]

For each of the four possible normalized roots (w), this congruence fixes
one residue (z\equiv wx\delta^{-1}\pmod N).  The interval (0\le z<N)
contains at most one representative of it.  Only two values of (w) are
mixed, so at most two digits (t) are useful.  Since the digit map is a
bijection, a fresh uniform (t), conditional on any fixed (P,X) and
past, has useful probability at most (2/N).

This is a one-fresh-row bound.  It does not apply after an algorithm sees
the fresh row and then chooses among exponentially many past subsets.
Nothing in this proof analyzes the fixed section (t=0).

## Theorem C: canonical duplicates

Restricting the (E)-power map on
((\mathbb Z/N^2\mathbb Z)^\times) to the (arphi(N)) canonical lifts
cannot increase a fibre beyond the full kernel size (K).  If the
canonical outputs have fibre sizes (c_u), then

\[
 \Pr(u(a)=u(b))={\sum_u c_u^2\over\varphi(N)^2}
 \le {K\sum_u c_u\over\varphi(N)^2}
 ={K\over\varphi(N)}.
\]

For a duplicate,
(x_a^2\equiv x_b^2\pmod N), so (x_ax_b^{-1}) is a root of (1).
A mixed ratio factors (N).

The numerical constants (4) and (24) again depend on the undefined
P209 facts.  Conditional on a fixed or (2^{o(n)}) value of (K), a union
bound over the pairs in a quasipolynomial bank is (2^{-\Omega(n)}).  This
bank conclusion presumes the uniform canonical-base sampling stated in the
theorem; it is not a bound for an adversarially chosen bank.

## Theorem D: reciprocal output

The least positive reciprocal (v) satisfies (uv\equiv1\pmod{N^2}).
If (uv=R^2) as integers, then (R^2\equiv1\pmod{N^2}).  Moreover
(u,v<N^2), so (R<N^2); hence (R) is the least representative of one
of the four roots of (1) modulo (N^2).

For a fixed (R), every possible (u) divides (R^2), so the number of
possible outputs is at most

\[
 S=\sum_{R^2=1\bmod N^2}\tau(R^2)=2^{o(n)},
\]

because (R^2<N^4).  Each output has at most (K) canonical-base
preimages, giving the precise general probability bound

\[
 \Pr_a(uv\text{ is a square})\le {KS\over\varphi(N)}
\]

for a uniform canonical unit (a).  It becomes (2^{-n+o(n)}) whenever
(K=2^{o(n)}).  The unconditional phrase “on P209” cannot be checked from
the statement alone because neither P209 nor the relevant exponent and
its (K) are specified here.

The supplied roots for (u) and (v) can be taken as (x) and (x^{-1}),
so their product root is (1).  Thus a mixed (R\bmod N) factors (N),
whereas a global (R) does not.  If instead one first takes the canonical
integer representative (b=[a^{-1}]_N), generally
(b\not\equiv a^{-1}\pmod{N^2}).  Therefore ([b^E]_{N^2}) need not equal
(u^{-1}\bmod N^2), and this proof says nothing about that pair.

## Torus preliminaries

Over (mathbb F_r), the group (x^2-Dy^2=1) has order

\[
 m_r=r-\left({D\over r}\right).
\]

Indeed, if (D) is a square, the change of variables
((x-dy,x+dy)) identifies it with (mathbb F_r^\times), of order (r-1).
If (D) is a nonsquare, it is the norm-one kernel in
(mathbb F_{r^2}^\times), of order ((r^2-1)/(r-1)=r+1).
Points with (x=0) solve (y^2=-D^{-1}), so their number is
(z_r=1+({-D}/r)).  CRT then gives

\[
 H=(m_p-z_p)(m_q-z_q)
\]

clean raw points.  For every admitted canonical (y), the nonzero square
(1+Dy^2) has two roots on each local side, hence exactly four global
(x)-values.

## Theorem E: raw torus rows

If (D_0=d^2) as an integer and (1+D_0y^2=s^2), then

\[
 (s-dy)(s+dy)=1.
\]

Both factors are nonnegative integers, so (y=0,s=1).  This proves the
square-(D_0) case.

Suppose now that (D_0) is not a square.  Positive-(y) square rows are
solutions of Pell's equation

\[
 s^2-D_0y^2=1.
\]

Let (epsilon=s_1+y_1\sqrt{D_0}>1) be its least positive unit.  The usual
minimality argument in the ordered norm-one units shows that every positive
solution is (epsilon^k), (k\ge1).  Also

\[
 \epsilon>2y_1\sqrt{D_0}\ge2\sqrt{D_0}.
\]

For (y<N),

\[
 epsilon^k=s+y\sqrt{D_0}<2N\sqrt{D_0}+1.
\]

Thus the number of positive-(y) solutions is no more than

\[
 \left\lfloor
 {\log(2N\sqrt{D_0}+1)\over\log(2\sqrt{D_0})}
 \right\rfloor.
\]

Adding (y=0) gives (B_D(N)).  Since (1<D_0<N) in the nonsquare case,
this is (O(n)).

At most (B_D(N)) admitted (y)-values can therefore be square rows.
Each has four points, proving (4B_D(N)/H).

Because (D_0>0) and canonical (y)'s are nonnegative,
(A_{y_1}=A_{y_2}) is equivalent to (y_1=y_2).  There are (H/4)
admitted (y)'s, each with fibre four.  Hence two independent uniform
clean points have duplicate probability

\[
 {H\over4}{4^2\over H^2}={4\over H}.
\]

For each fixed second point, exactly two of the four first roots have a
mixed ratio.  The useful-duplicate probability is therefore half of this,
namely (2/H).

The assertion (H=2^{\Omega(n)}) on P209 is not reconstructible without
the missing family definition.  Conditional on it, the one-row and
quasipolynomial-bank conclusions follow by a union bound.

## Theorem F: powered torus rows

Powering is a group homomorphism, so a uniform input maps uniformly onto
the product of its two local image subgroups.  Conditioning after removal
of (x=0) makes the distribution uniform on the clean image of size

\[
 H'=(r_p-z'_p)(r_q-z'_q).
\]

Represent a local point as (t=x+y\sqrt D).  Its inverse is
(t^{-1}=x-y\sqrt D).  The other possible point with the same (y) is

\[
 -t^{-1}=-x+y\sqrt D.
\]

For an image subgroup (G), both points lie in (G) exactly when
(-1\in G), which for a cyclic group is exactly when (|G|) is even.
After points with (x=0) are removed, the two are distinct.  Since the two
local image orders are coprime, at most one is even.  Every global
(y)-fibre consequently has size at most two.  Combining this with the
Pell count proves (2B_D(N)/H').

If both local orders are odd, every global (y)-fibre is a singleton, so
equal (y) means the same powered point and supplies no second root.  If
exactly one order is even, every admitted global (y)-fibre has exactly
two points.  Their (x)-coordinates differ by a sign on exactly one local
side, so their ratio is mixed.  There are (H'/2) such fibres and two
ordered distinct pairs in each.  Thus

\[
 \Pr(\text{useful duplicate})
 ={(H'/2)\,2\over H'^2}={1\over H'}.
\]

The claims about the P208/P209 square exponent, residual orders, private
markers, and the “numerical-QP signed-power grammar” cannot be reconstructed
because none of those objects or conditions is defined in the statement.
If their asserted coprimality and (H'=2^{\Omega(n)}) are supplied as
premises, the stated negligible-bank consequence follows.

## Theorem G: inverse torus points

For (1\le y<N), the canonical coefficient of the inverse point is
(N-y).  Direct expansion gives

\[
\begin{aligned}
 A_yA_{N-y}
 &=\bigl(1+D_0y^2\bigr)
   \bigl(1+D_0(N-y)^2\bigr)\\
 &=\bigl(1-D_0y(N-y)\bigr)^2+D_0N^2
 =C^2+D_0N^2.
\end{aligned}
\]

Also (C\equiv1+D_0y^2\equiv x^2\pmod N), so (C) is a unit on the clean
set.  If the product is (R^2), then (R>|C|) and

\[
 (R-C)(R+C)=D_0N^2.
\]

A positive divisor (R-C) of (D_0N^2) determines (R+C), hence
(C).  The quadratic equation
(C=1-D_0y(N-y)) has at most two integer solutions (y).  This proves the
stated upper bound (2\tau(D_0N^2)) for nonzero canonical (y)'s.

If the probability space also contains (y=0), its inverse pair is the
global decoy (A_0^2=1).  The displayed probability constants can still
be retained.  Indeed, for (1\le y<N), one has (C<0), so only divisors
(R-C>\sqrt{D_0N^2}) occur.  There are at most half of all divisors, and
the nonzero (y)-count sharpens to at most (	au(D_0N^2)).  Adding (y=0)
gives at most (	au(D_0N^2)+1\le2\tau(D_0N^2)) canonical (y)'s.

The raw fibre bound four and the powered fibre bound two now give

\[
 \Pr_{\rm raw}\le {8\tau(D_0N^2)\over H},\qquad
 \Pr_{\rm powered}\le {4\tau(D_0N^2)\over H'}.
\]

Since (D_0N^2<N^3), the divisor factor is (2^{o(n)}).  Finally,
(R^2\equiv C^2\pmod N), so (R/C) is a root of (1), and it factors
(N) exactly when mixed.

The raw and powered P208/P209 exponential estimates remain conditional on
the missing lower bounds for (H,H').

## Exact proved boundary

From the permitted statement alone, the reconstructed arguments exclude
only these mechanisms, under their stated uniform distributions and size
premises:

- a single exact-square scalar or torus row;
- equality of two scalar or torus rows;
- the scalar reciprocal **output** pair modulo (N^2);
- a torus point paired with its group inverse;
- a fresh principal-lift row multiplied by one product and root fixed
  before the fresh lift parameter is sampled.

They do not bound any of the following:

1. a relation between distinct, unrelated scalar rows, even with only two
   rows;
2. a relation between distinct, unrelated torus rows, even with only two
   rows;
3. a relation mixing scalar and torus rows;
4. adaptive selection among many past subsets after a fresh row is seen;
5. any bias of the fixed canonical principal section (t=0);
6. the pair formed by canonically lifting the inverse base modulo (N);
7. ordinary prime-factor parity dependencies among products of distinct
   row integers;
8. any all-input factoring or quasipolynomial-success theorem.

The statement's meta-claim that no bound for the canonical section is
known is not itself derivable mathematically from the statement-only
evidence.  It can only be retained as a declared research-status boundary.

## Missing data needed to change FAIL to PASS

A blind verifier needs a self-contained definition of P208 and P209,
including the prime congruences/order markers and the relation between
their size parameter and (n).  It also needs the exact allowed powering
exponents and a definition of the covered signed-power grammar.  From those
data one must independently derive:

- (K=4) for (E=N-1) and (K=24) for (E=N^2-1);
- the active local side for (E=N-1) and two trivial local images for
  (E=N^2-1);
- (H=2^{\Omega(n)});
- coprimality of the powered local image orders and
  (H'=2^{\Omega(n)}) in every claimed exponent/grammar case.

No conclusion about a general P66 dependency follows until those family
facts are supplied, and even those facts would establish only the named
one-row, duplicate, and inverse-pair boundaries.
