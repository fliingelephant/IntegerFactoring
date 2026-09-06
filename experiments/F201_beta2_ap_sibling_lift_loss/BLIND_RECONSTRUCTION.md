# Blind reconstruction of the F201 statement

## Verdict

**Pass, with the scope stated in the candidate.**  Every asserted arithmetic
claim follows from the stated hypotheses.  The last recurrences are
conditional observations, not a construction of the missing selector.  Thus
the result does not prove the factoring claim in `PROMPT.md`.

The statement used for this reconstruction had SHA-256

```text
4915cbeea9e258524ece5dcf21e115f1a6c8ef0775dd0d1b926b94cdcbda8d41
```

No proof, audit, ledger, candidate message, or other F201 file was used.

## 1. The public interval contains exactly one factor-bearing integer

Let

\[
N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor.
\]

Because (p<q),

\[
p<\sqrt{pq}<q.
\]

Since (p) is an integer, the first inequality gives (p\leq B), while the
second gives (B<q).  Also (p\geq3), and

\[
B<\sqrt{2}\,p<\frac{3p}{2}.
\]

Consequently

\[
\left\lceil\frac B2\right\rceil
\leq \frac B2+\frac12
<\frac{3p}{4}+\frac12<p.
\]

Thus (p\in I_B).  We already have (q>B), so (q\notin I_B), and
(B<3p/2<2p), so (2p\notin I_B).

If (J\in I_B) and \(\gcd(J,N)>1\), primality of (p,q) implies that (p)
or (q) divides (J).  The inequality (0<J\leq B<q) excludes (q\mid J).
The only positive multiple of (p) not exceeding (B<2p) is (p) itself.
Hence (p) is the unique element of (I_B) with a nontrivial gcd with
(N).

Because (p) is odd, it is a unit modulo (m=2^t).  If a residue
(u\equiv p^{-1}\pmod m) is known, then inverting (u) modulo (m) gives
the odd residue (a\equiv p\pmod m).  The associated full cell therefore
contains (p).  This justifies the stated passage from the reciprocal prefix
to the AP residue; it does not reveal which listed integer is (p).

## 2. Exact parity split and endpoint cleanup

Write

\[
S=\{x_j=c+mj:0\leq j<L\},\qquad m=2^t>0.
\]

The parity of (j) separates the residue (c\pmod m) into its two residues
modulo (2m).  If (L=2s), each parity has (s) elements.  If (L=2s+1),
the even indices have one extra element, namely

\[
x_*=x_{2s}=c+2ms.
\]

This endpoint belongs to (S\subseteq I_B).  The uniqueness result above
therefore gives

\[
\gcd(N,x_*)\in\{1,p\}.
\]

If this gcd is (p), it is already a proper factor of (N).  Suppose instead
that it is one.  Then (x_*\ne p), so removing (x_*) does not remove the
assumed member (p\in S).  After this removal, both parity classes have
length (s).  In the even-length case no element is removed and both classes
already have length (s).

In every unresolved case (s\geq1).  Indeed, an even positive (L) is at
least two.  If an odd (L) had (s=0), then (S=\{x_*\}); because (S)
contains (p), its endpoint gcd would be (p), which is the resolved case.

The two cleaned children are therefore

\[
e_i=c+2mi,\qquad o_i=c+(2i+1)m=e_i+m,
\qquad 0\leq i<s.
\]

Every displayed element remains in (S\subseteq I_B), and (m>0).  Hence

\[
\left\lceil\frac B2\right\rceil<e_i<o_i\leq B
\]

and, when (i<s-1),

\[
o_i=e_i+m<e_i+2m=e_{i+1}.
\]

The cleaned union still contains (p), and the two children are disjoint.
Thus exactly one child contains (p).  Since (p) is prime, exactly one of

\[
E=\prod_{i=0}^{s-1}e_i,\qquad
O=\prod_{i=0}^{s-1}o_i
\]

is divisible by (p).  No factor in either product equals or is divisible by
(q), because every factor lies strictly between zero and (q).  Euclid's
lemma then shows that (q\nmid E) and (q\nmid O).  It follows that

\[
\{\gcd(N,E),\gcd(N,O)\}=\{p,1\},
\]

with (p) attached to the child containing (p).  Computing either product
modulo (N), followed by a gcd with (N), therefore distinguishes the two
children exactly: a gcd of (p) selects that product, and a gcd of one
selects the other product.  This is only a correctness reduction to modular
product evaluation; it does not provide a fast evaluator.

## 3. Ordinary Euclidean division and loss of (p)-support

Every factor (o_i/e_i) exceeds one, so (O/E>1).  Re-indexing the factors
also gives

\[
\frac OE
=\frac{o_{s-1}}{e_0}
 \prod_{i=0}^{s-2}\frac{o_i}{e_{i+1}}.
\]

For (s\geq2), every factor in the product on the right is strictly less
than one by interlacing.  For (s=1), that product is empty.  Therefore

\[
\frac OE\leq\frac{o_{s-1}}{e_0},
\]

strictly when (s\geq2) and with equality when (s=1).  Finally,
(o_{s-1}\leq B) and (e_0>B/2), so

\[
\frac{o_{s-1}}{e_0}<2.
\]

Combining the bounds yields (E<O<2E).  Hence ordinary Euclidean division
has quotient one and gives exactly

\[
O=E+D,\qquad D=O-E,\qquad 0<D<E.
\]

If (p\mid E), then (p\nmid O), and

\[
D\equiv O\not\equiv0\pmod p.
\]

If (p\mid O), then (p\nmid E), and

\[
D\equiv-E\not\equiv0\pmod p.
\]

Thus (p\nmid D) in both orientations.  Nothing in this argument controls
(D\pmod q), so (q\mid D) is not excluded and \(\gcd(D,N)=1\) does not
follow.  Reversing the division merely gives

\[
E=0\cdot O+E,
\]

whose remainder is the original smaller operand rather than a new auxiliary.

For the rising factorial ((z)_s=\prod_{i=0}^{s-1}(z+i)), direct factoring
of (2m) from every term gives the exact integer identities

\[
E=(2m)^s\left(\frac c{2m}\right)_s,
\qquad
O=(2m)^s\left(\frac{c+m}{2m}\right)_s.
\]

Both starting arguments are positive.  Applying
((z)_s=\Gamma(z+s)/\Gamma(z)) and cancelling ((2m)^s) gives

\[
\frac OE=
\frac{\Gamma((c+m)/(2m)+s)\,\Gamma(c/(2m))}
     {\Gamma((c+m)/(2m))\,\Gamma(c/(2m)+s)}.
\]

These are representations of the same ordered integers (E<O).  They do
not alter their ordinary Euclidean quotient or the first remainder (D).

## 4. Explicit size of the first remainder

Expanding the product difference over nonempty subsets (A\subseteq
\{0,\ldots,s-1\}) gives

\[
D=
\sum_{\varnothing\ne A\subseteq\{0,\ldots,s-1\}}
m^{|A|}\prod_{i\notin A}e_i.
\]

All summands are positive.  Retaining only the summand (A=\{0\}) yields

\[
D\geq m\prod_{i=1}^{s-1}e_i
\geq m\left(\frac B2\right)^{s-1}.
\]

When (s\geq2), every factor in the retained product satisfies (e_i>B/2),
so the final inequality is strict.  When (s=1), both products are empty,
and in fact (D=m), so it is equality.

For a positive integer (x),

\[
\operatorname{bitlen}(x)=\lfloor\log_2x\rfloor+1>\log_2x.
\]

Taking logarithms of the preceding lower bound therefore proves

\[
\operatorname{bitlen}(D)
>\log_2m+(s-1)(\log_2B-1).
\]

### Uniform AP lengths

The interval (I_B) contains

\[
B-\left\lceil\frac B2\right\rceil
=\left\lfloor\frac B2\right\rfloor=:K
\]

consecutive integers.  In any interval of (K) consecutive integers, the
number in a fixed residue class modulo (m) differs from (K/m) by less
than one.  Thus a full cell has

\[
L=\frac{\lfloor B/2\rfloor}{m}+O(1).
\]

This error remains uniform down the cleaned chain.  To see this, let a full
cell start with modulus (m_0) and length \(\Lambda_0\).  At every unresolved
split, either parity child after cleanup has length

\[
L_{r+1}=\left\lfloor\frac{L_r}{2}\right\rfloor,
\]

while its modulus is (m_{r+1}=2m_r).  Therefore

\[
L_r=\left\lfloor\frac{\Lambda_0}{2^r}\right\rfloor
=\frac K{2^rm_0}+O(1)
=\frac K{m_r}+O(1).
\]

For a parent whose current modulus is denoted by (m), the cleaned child
size (s=\lfloor L/2\rfloor) consequently satisfies

\[
s=\frac{K}{2m}+O(1)=\frac{B}{4m}+O(1).
\]

This proves both length estimates for the full cell and for every unresolved
consecutive descendant.

### P175 precision

Put \(\lambda=\log_2N\).  At the stated schedule,

\[
t=\left\lfloor\frac\lambda4\right\rfloor-L_0(n),
\qquad
m=2^{\lfloor\lambda/4\rfloor-L_0(n)}.
\]

Since

\[
\frac12N^{1/4}<2^{\lfloor\lambda/4\rfloor}\leq N^{1/4}
\quad\text{and}\quad
B=\Theta(N^{1/2}),
\]

the length formula, with its bounded additive error, gives

\[
s=\Theta\!\left(N^{1/4}2^{L_0(n)}\right).
\]

The main term tends to infinity, so the additive (O(1)) does not affect
this asymptotic.  Moreover (n=\Theta(\log_2N)), and a fixed nonnegative
polylogarithm satisfies (L_0(n)=o(n)).  Hence

\[
\log_2\!\left(N^{1/4}2^{L_0(n)}\right)
=\frac14\log_2N+L_0(n)=\Theta(n),
\]

which proves

\[
s=2^{\Theta(n)}.
\]

The lower bit-length bound now gives

\[
\operatorname{bitlen}(D)=2^{\Omega(n)},
\]

because (s-1=\Theta(s)) and \(\log_2B-1=\Theta(n)\).  For the matching
upper bound, (0<D<O\leq B^s), so

\[
\operatorname{bitlen}(D)\leq s\log_2B+1=2^{O(n)}.
\]

Therefore

\[
\operatorname{bitlen}(D)=2^{\Theta(n)}.
\]

Any explicit binary materialization must write or store this many bits and
therefore already takes exponential bit time at this node.  This argument
does not apply to an implicit representation or an implicit modular
evaluator.

## 5. Linear axes lemma

For public integers \(\alpha,\beta\), let

\[
F_{\alpha,\beta}=\alpha E+\beta O.
\]

On the first possible active axis, (p\mid E) and (p\nmid O), so

\[
F_{\alpha,\beta}\equiv\beta O\pmod p.
\]

Since (O) is nonzero modulo the prime (p), multiplication by (O) is
invertible modulo (p).  Thus

\[
p\mid F_{\alpha,\beta}\iff p\mid\beta.
\]

On the other axis, (p\mid O) and (p\nmid E), and the same argument gives

\[
F_{\alpha,\beta}\equiv\alpha E\pmod p,
\qquad
p\mid F_{\alpha,\beta}\iff p\mid\alpha.
\]

If both coefficients are units modulo (N), neither is divisible by (p),
so the linear form is not divisible by (p) in either orientation.  To be
divisible by (p) on both possible axes, it is necessary and sufficient
that (p\mid\alpha) and (p\mid\beta).

Under that condition each gcd \(\gcd(\alpha,N)\) and
\(\gcd(\beta,N)\) is either (p) or (N).  If either is the proper gcd
(p), it already factors (N).  Otherwise (N) divides both coefficients,
each term is zero modulo (N), and the whole form is the trivial zero modulo
(N).  More generally, any coefficient divisible by (N) contributes zero
modulo (N).  As before, the axis argument is only about (p); accidental
divisibility by (q) remains possible.

## 6. Conditional child chain and recurrence depth

Let (S'=S) for even (L), and for odd (L) let (S') be (S) after the
screened endpoint is removed on the unresolved branch.  The two lists
(\{e_i\}) and \(\{o_i\}) are a disjoint partition of (S').  Therefore

\[
\prod_{J\in S'}J=EO.
\]

Exactly one child contains (p).  If an external procedure selects that
child, it becomes another consecutive AP containing (p), now with doubled
modulus, and the argument repeats.  This is a genuine unique-child chain.

There are only (O(n)) possible bit lifts.  Each lift doubles the modulus.
Once the modulus exceeds the width of (I_B), a residue class has at most
one representative in that interval.  Since that width is less than
(B<N<2^n), at most (n+O(1)) doublings suffice from any (t\geq1).

Consequently, if a selector at every level costs
(\operatorname{QP}(n)), its conditional recurrence can be written

\[
U(t)\leq U(t+1)+\operatorname{QP}(n)
\]

through only (O(n)) levels.  Unrolling adds at most
(O(n)\operatorname{QP}(n)), which is still quasipolynomial under the
definition in `PROMPT.md`.  Likewise,

\[
T(n)\leq T(n-1)+\operatorname{QP}(n)
\]

unrolls through at most (n) stages and has the same closure property.
Thus a fixed-ratio contraction is not necessary for such a one-child
recurrence.  These observations are conditional: no quasipolynomial
selector or modular AP-product evaluator has been constructed here.

## 7. Exact boundary

The proof applies only to the stated balanced squarefree semiprime setting,
to a full upper-half AP cell containing (p), and to unresolved consecutive
descendants produced by the stated parity split and endpoint cleanup.  It
establishes the exact sibling ordering, quotient one, loss of guaranteed
(p)-support in the first remainder, the explicit size of that remainder,
and the two-axis obstruction for fixed public linear forms.

It does not establish a lower bound against implicit modular AP-product
evaluation.  It does not rule out a nonlocal carry or floor, a different
one-child integer auxiliary, an adaptive integer or nonlinear selector, or
any other factoring mechanism.  In particular, it neither supplies the
conditional selector used in the recurrences nor extends the result to
prime powers, unbalanced semiprimes, repeated factors, or arbitrary
composites.  Therefore it is a valid scoped obstruction to this exact
sibling-quotient handoff, not a quasipolynomial factoring algorithm or a
factoring lower bound.
