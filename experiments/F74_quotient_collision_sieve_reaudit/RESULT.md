# Fresh hostile re-audit of corrected F74 — PASS

## Verdict

**PASS.** I pinned and audited the corrected candidate at SHA-256

```text
de21b1e693275cb14e05931d71a6ad6f8d30bb40dc85e3ab68ad30a7c83c78e6
```

The first hostile audit failed an earlier version. I did not carry its
accepted claims forward. I rederived the three gcd forms, the valuation law,
the exact divisor gate, the constructive (D_r>r) criterion, the CRT
duality, the polynomial bit bound, and the bounded-quotient domination
theorem. I also rechecked the equal-quotient counterexample, the two-sign
screen, multiplicity retention, every finite witness, the infinite power
family, and all stated scope limits.

The correction is substantive. In the bounded-quotient regime, a small-state
scan recovers not only the same relation value but also the same old
endpoint provenance and occurrence capacity. The quotient-collision sieve
therefore has no new source power in that regime. The candidate now says
this exactly.

No research computation, search, CAS, or numerical script was used in this
audit. All checks below are direct integer or symbolic derivations.

## 1. Setup is coherent

Each retained relation satisfies

\[
A_i=x_i y_i=1+k_iN,
\qquad 1\le x_i,y_i<N.
\]

Hence (A_i<N^2), (A_i\equiv1\pmod N), and
(gcd(A_i,N)=1). Therefore

\[
P=\prod_i A_i=1+KN
\]

for an integer (K), and (gcd(P,N)=1).

The source assumptions are sufficient for the later construction. The
retained pairwise-coprime block basis represents every endpoint with exact
exponents, and the indexed occurrence ledger retains total usable capacity.
If the known integer (D_r\mid P) is added to a gcd-free refinement, the
refinement can express (D_r) using those retained block occurrences. This
does not require prime factorization. Every resulting refined block divides
an old endpoint and is therefore strictly smaller than (N).

## 2. The three forms of (D_r) are exact

Let (A_r=1+rN). Since

\[
P-N(K-r)=A_r
\]

and (gcd(P,N)=1),

\[
\gcd(P,K-r)=\gcd(P,N(K-r))=\gcd(P,A_r).
\]

Also, modulo (A_r),

\[
A_i=1+k_iN\equiv(k_i-r)N.
\]

Thus

\[
P\equiv N^m\prod_i(k_i-r)\pmod {A_r}.
\]

Because (gcd(A_r,N)=1), the factor (N^m) is a unit modulo every
divisor of (A_r). Hence

\[
D_r
=\gcd(P,A_r)
=\gcd(P,K-r)
=\gcd\!\left(A_r,\prod_i(k_i-r)\right).
\]

If some (k_i=r), the last product is zero and both sides equal (A_r),
because (A_r=A_i\mid P). The candidate's convention is correct.

When no (k_i) equals (r), taking prime valuations gives

\[
v_p(D_r)=\min\!\left(v_p(1+rN),
                  \sum_i v_p(k_i-r)\right).
\]

Consequently every prime divisor of (D_r) divides at least one nonzero
quotient difference. The bound

\[
p\le\max_i|k_i-r|
\]

is exact. Repeated relation occurrences contribute repeated valuations, so
the multiplicity interpretation is also correct.

## 3. The canonical feedback divisor gate is exact

Let (g) be an occurrence-certified divisor of (P), with
(1<g<N). It is a unit modulo (N). Let its canonical inverse be
(w\in\{1,\ldots,N-1\}), and write

\[
gw=1+k(g)N.
\]

If (k(g)=r), then (g\mid A_r) and (g\mid P), so (g\mid D_r).
Moreover,

\[
1\le k(g)=\frac{gw-1}{N}<g,
\]

because (w<N). Therefore (r<g).

Conversely, suppose (g\mid D_r) and (r<g<N). Then

\[
w=\frac{1+rN}{g}
\]

is a positive integer, and

\[
w\le\frac{1+rN}{r+1}<N.
\]

It is therefore the canonical inverse of (g), and its quotient is exactly
(r). This proves the claimed equivalence without a missing unit or range
case.

## 4. The (D_r>r) construction is valid

Assume (N>r^2). After gcd-free refinement by the known integer (D_r),
write

\[
D_r=a_1\cdots a_t
\]

as retained refined block occurrences. Each (a_j) is in
({2,\ldots,N-1\}). Also

\[
t\le\log_2D_r\le\log_2P,
\]

so the list has polynomial length in the retained transcript.

If a legal quotient-(r) candidate exists, the divisor gate already gives
(D_r\ge g>r).

For the converse, suppose (D_r>r). If some occurrence (a_j>r), take
(g=a_j<N). Otherwise, multiply occurrences until the running product first
exceeds (r). The preceding product and the last multiplier are each at
most (r), so

\[
r<g\le r^2<N.
\]

In both cases (g\mid D_r), and the divisor gate constructs its canonical
quotient-(r) relation. No subset enumeration or integer factorization is
hidden in this argument.

If (N\le r^2) and the scan has (r\le\operatorname{poly}(\log N)), then
trial division through (sqrt N\le r) takes polynomially many arithmetic
steps. The candidate therefore handles, rather than silently omits, the
small-(N) branch.

## 5. CRT quotient duality is exact

For a unit (1<g<N), let

\[
\rho_N(g)=(-N^{-1})\bmod g
\]

in the range (1,\ldots,g-1). The residue cannot be zero because (N) is a
unit modulo (g).

For the canonical inverse (w=iota_N(g)), the integer

\[
q=\frac{gw-1}{N}
\]

satisfies (1\le q<g) and (qN\equiv-1\pmod g). Hence
(q=\rho_N(g)), proving

\[
g\iota_N(g)=1+\rho_N(g)N.
\]

If (g\mid P=1+KN), then (KN\equiv-1\pmod g), so

\[
K\equiv\rho_N(g)\pmod g.
\]

Thus choosing (g) and computing its quotient label is exactly dual to
choosing (r) and computing the aggregate common divisor (D_r). The
candidate correctly keeps two limits explicit: (D_r) can exceed (N),
and it can encode many divisors without selecting a useful one.

## 6. Polynomial bit complexity and product-tree scope pass

With (m\le n^a), where (n=\lceil\log_2N\rceil), the explicit product
(P) has (O(mn)) bits because every (A_i<N^2). With
(R\le n^b), the scan performs only polynomially many gcds

\[
\gcd(P,1+rN),\qquad 1\le r\le R,
\]

on polynomial-bit integers. The products, exact divisions, and gcd-free
refinements used after an open gate also have polynomial bit complexity in
the transcript size. This proves runtime of the bounded scan, not its
factoring success; the candidate maintains that distinction.

For every product-tree node (T), the same congruence proof gives

\[
\gcd\!\left(\prod_{i\in T}A_i,A_r\right)
=\gcd\!\left(A_r,\prod_{i\in T}(k_i-r)\right).
\]

Descent can therefore identify which indexed old relation occurrences
support the gcd blocks. Shared prime powers can occur in more than one child,
so exact capacity still needs gcd-free refinement and the indexed ledger.
The candidate does not claim that the tree alone selects an arbitrary useful
subset.

## 7. The bounded-quotient domination theorem passes

Assume

\[
1\le r,k_i\le B,
\qquad r\ne k_i,
\qquad B=\operatorname{poly}(\log N),
\]

and (D_r>r). Every prime factor of (D_r) divides some nonzero
(k_i-r), so it is at most (B). Trial division factors all quotient
differences, and therefore (D_r), in polynomial time.

Multiply prime occurrences of (D_r) until the product first exceeds (r).
The last prime is at most (B), so the resulting divisor satisfies

\[
r<g\le rB\le B^2.
\]

If (N\le B^2), trial division through (B) resolves (N). If
(N>B^2), then (g<N), and the exact divisor gate gives

\[
g\iota_N(g)=1+rN=A_r.
\]

Thus an exhaustive prior scan of all states (2\le g\le B^2) emits the
same relation value. The scan is polynomial because (B^2) is polynomial
in (log N).

### The same-provenance claim also passes

There is no provenance loophole in this domination result. After the small
scan emits (A_r), it uses the unchanged retained product and computes

\[
\gcd(P,A_r)=D_r.
\]

It can then run the same gcd-free refinement against the same indexed
endpoint ledger and the same product tree. Therefore it recovers the same
old block divisibility, indexed relation support, valuations, and usable
occurrence capacities as the target-first gate. A different presentation of
(A_r) does not erase the old ledger.

The repeated-power family is the strongest test of this point. With (t)
retained copies of the quotient-one relation and target (r=3), the direct
small scan includes (g_0=4\le3^2) and emits

\[
A_3=1+3N=2^{2t}.
\]

It then computes

\[
D_3=\gcd(P,A_3)=2^t.
\]

The indexed old ledger still contains all (t) authorized occurrences of
the block (2). It therefore certifies the same large state (2^t) that the
quotient-collision route certifies. The small scan recovers the full
endpoint/provenance power, not only the scalar value (A_3).

The theorem is only a domination theorem for bounded (r) and bounded old
quotients. Large quotient differences are a necessary condition for a new
source role, not a sufficient success theorem. The candidate states both
limits.

## 8. The equal-quotient boundary is corrected

At (N=55), retain

\[
56=2\cdot28=1+55.
\]

The old endpoints pass both sign screens:

\[
\gcd(1,55)=\gcd(3,55)=1,
\]

\[
\gcd(27,55)=\gcd(29,55)=1.
\]

The same relation value also has the occurrence-certified presentation

\[
56=14\cdot4,
\]

because the retained endpoint product is (2^3\cdot7). This presentation
is useful:

\[
\gcd(14+1,55)=5.
\]

For (r=k_1=1), however,

\[
D_1=\gcd(56,56)=56.
\]

The root gcd is the entire relation value and does not select (14) from
its divisors. The candidate now excludes equal quotients for this exact
localization reason. It does not claim that every new presentation of an old
value is redundant.

## 9. Both sign screens are necessary

For a canonical inverse pair (gw\equiv1\pmod N), multiplication by the
unit (g) gives

\[
\gcd(g-w,N)=\gcd(g^2-1,N).
\]

If (g) is a non-global square root of one, then its canonical inverse is
(w=g). The difference gcd is therefore (N), not a factor. At (N=55),
(g=w=21) gives

\[
\gcd(g-w,55)=55,
\qquad
\gcd(g-1,55)=5,
\qquad
\gcd(g+1,55)=11.
\]

The candidate correctly rejects replacement of the two sign gcds by the
single difference gcd.

## 10. Multiplicity is source state

At (N=4033) and (r=3), one indexed quotient-one occurrence gives

\[
D_3=\gcd(1+3N,1-3)=2\le3.
\]

Two indexed copies give

\[
D_3=\gcd(1+3N,(1-3)^2)=4>3.
\]

The second relation row is redundant in a decoder span, but it adds one
usable endpoint occurrence. It opens the exact gate and authorizes (g=4).
Therefore decoder-basis compression is not source compression. Retaining a
multiplicity counter or equivalent provenance capacity is necessary and
sufficient for this example. The candidate says this correctly.

## 11. Every displayed witness checks

The finite gcd values follow directly from the quotient-difference form.

### (N=21), quotients ({1,4}), target (r=9)

Here (A_9=190) and the difference product is
((-8)(-5)=40). Hence (D_9=\gcd(190,40)=10). Taking (g=10)
gives (w=19), and

\[
\gcd(g-1,21)=\gcd(9,21)=3.
\]

### (N=55), quotients ({1,2}), target (r=8)

Here (A_8=441=21^2) and the difference product is
((-7)(-6)=42). Hence (D_8=21). The candidate (g=w=21) is the
stated non-global root.

### (N=21), quotients ({1,1,1}), target (r=3)

Here (A_3=64) and the difference product is ((-2)^3=-8), so
(D_3=8). Taking (g=w=8) gives the two proper sign gcds (7) and
(3).

### (N=4033), quotients ({1,1}), target (r=3)

Here

\[
A_3=12100=110^2,
\qquad D_3=\gcd(12100,4)=4.
\]

The candidate (g=4) has complement (w=3025=55^2), so the new relation
is

\[
4\cdot3025=110^2.
\]

The root (110) gives

\[
\gcd(110-1,4033)=109,
\qquad
\gcd(110+1,4033)=37.
\]

### (N=4033), quotients ({1,63,7}), target (r=1983)

The target value is

\[
A_{1983}=7{,}997{,}440=2048\cdot3905
=2^{11}\cdot5\cdot781.
\]

The quotient differences factor as

\[
1983-1=2\cdot991,
\]

\[
1983-63=2^7\cdot3\cdot5,
\]

\[
1983-7=2^3\cdot13\cdot19.
\]

The valuation law therefore gives

\[
D_{1983}=2^{11}\cdot5=10240.
\]

The retained endpoints

\[
2\cdot2017,
\qquad64\cdot3970,
\qquad8\cdot3529
\]

contain (1+6+1+3=11) indexed occurrences of the block (2), so
(g=2^{11}=2048) is source-certified. Its complement is (3905<N).
Also (1985=5\cdot397), and therefore

\[
\gcd(D_{1983},1985)=5.
\]

Thus the gate exposes the stated old-block split. The target (1983) is a
fixed witness value only; the candidate does not promote it to an all-input
polylogarithmic bound.

### Infinite power family

Under the P70 family conditions (in particular (t\ge3)), put

\[
N=\frac{2^{2t}-1}{3}
\]

and retain (t) quotient-one occurrences. Then

\[
A_3=1+3N=2^{2t},
\qquad
\prod_i(k_i-3)=(-2)^t,
\]

so

\[
D_3=2^t>3.
\]

Moreover (2^t<N), so (g=D_3=2^t) is a legal candidate and
(g^2=1+3N). This is exactly the claimed useful power state. The generic
first-over-(r) construction need not choose this useful divisor; the
candidate expressly does not claim that it does.

## 12. Scope limitations are now exact

The corrected candidate proves a target-first, fixed-(r) fibre gate. It
compresses all source-supported quotient-(r) divisors into (D_r) and can
construct at least one legal candidate exactly when (D_r>r), subject to
the handled small-(N) branch.

It does **not** prove any of the following:

- that a useful (r\le\operatorname{poly}(\log N)) exists for every input;
- that the generic constructed divisor is factor-bearing;
- that a large quotient difference makes the gate open;
- that (D_r) itself is smaller than (N);
- that a product tree chooses a useful subset;
- that subgroup expansion, block splitting, or non-global square closure
  follows whenever (D_r>r);
- or that the method is a factoring algorithm.

It also proves that bounded old quotients and bounded target quotients give
no new source state beyond a polynomial small-state scan. These limitations
remove the two blocking overclaims from the failed first version.

The corrected F74 result is therefore internally valid at its declared
scope and is ready for proof-blind reconstruction.
