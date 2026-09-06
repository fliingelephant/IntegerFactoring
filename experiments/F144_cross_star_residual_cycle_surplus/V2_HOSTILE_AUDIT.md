# F144 V2 hostile audit — passed

## Verdict

**PASS.**  The corrected V2 statement removes the impossible V1 surplus
regime and promotes the exact obstruction that killed it.  Every principal
identity, inequality, root formula, deletion rule, and conditional scope
claim survives hostile reconstruction.

The frozen inputs match the requested hashes:

- `V2_STATEMENT.md`:
  `a07a992ac3d43dac6f25c2cc337e470f81c9a8265eb54e091922ecd63cef138b`;
- `V2_PROOF.md`:
  `f4c8f8fef6ca21b18f2bce70c400cf2ab6c748a55d32b8a1836ab2dd92de6df9`.

The preserved V1 failure was also read before this audit.  V2 does not
repeat its vacuous short-cycle claim.

## 1. The one-cycle obstruction is exact and needs no square residual

For a directed containment edge,

\[
U_e=q_ea_e^2=c_e+t_eN,
\qquad
c_e=r_eT_e.
\]

Around a directed cycle, the tail and head block multisets agree.  With

\[
Q=\prod q_e=\prod r_e,
\qquad
A=\prod a_e,
\qquad
T=\prod T_e,
\]

the exact products are

\[
\prod U_e=QA^2,
\qquad
\prod c_e=QT.
\]

The named blocks are units modulo (N), so cancellation of (Q) gives

\[
N\mid A^2-T.
\]

Also (U_e\ge c_e) term by term.  Hence (A^2\ge T), with equality
exactly when every edge is unwrapped.  If one edge wraps, the difference is
a positive multiple of (N), and therefore

\[
A^2-T\ge N,
\qquad
A^2\ge N+T,
\qquad
A>\sqrt N.
\]

No residual-square hypothesis enters this argument.  This is the precise
obstruction that was missing from V1.

## 2. The general residual-square dependency and root are correct

For an indexed collection of cycles, logical occurrences are counted with
multiplicity.  Tail-head balance gives one common block product (Q).  If
the combined residual is (S^2), then

\[
\prod_e C_eL_e
=Q^2\mathcal A^2S^2W^2
=(Q\mathcal ASW)^2.
\]

Since

\[
W\equiv(QS^2)^{-1}\pmod N,
\]

the normalized root is

\[
\rho\equiv\mathcal AS^{-1}\pmod N,
\qquad
\mathcal A^2\equiv S^2\pmod N.
\]

Every residual (T_e), and hence (S), is a unit modulo (N): (c_e)
and (r_e) are units and (c_e=r_eT_e).  Thus the displayed inverse is
legal.

If at least one selected occurrence wraps, exact product comparison gives

\[
\mathcal A>S,
\qquad
\mathcal A^2-S^2=mN
\]

for an integer (m\ge1).  If also (2\mathcal A<N), then

\[
0<\mathcal A-S<\mathcal A+S<N.
\]

Their product is divisible by (N).  Neither factor can be a unit modulo
(N), because that would make the other factor divisible by (N), which
its strict size bound forbids.  Neither gcd can equal (N) for the same
reason.  Both gcds in V2 are therefore proper.  This proof works for an
arbitrary odd composite, not only a semiprime.

## 3. The per-cycle collection boundary is correct

An unwrapped cycle has (T_{\mathcal C}=A_{\mathcal C}^2) exactly.  Its
positive residual root is (A_{\mathcal C}), so its normalized root is
(+1).

Two indexed wrapped cycles separately satisfy

\[
A_{\mathcal C_1}>\sqrt N,
\qquad
A_{\mathcal C_2}>\sqrt N.
\]

Because logical occurrences are retained with multiplicity, the collection
anchor product contains both factors and is greater than (N).  It cannot
satisfy (2\mathcal A<N).

If exactly one indexed cycle wraps, every other cycle contributes an exact
square residual.  Multiplication by those squares cannot change whether the
wrapped residual is a square.  Their anchor factors also cancel from the
normalized root.  Thus they provide neither residual closure nor a new
root.  V2 correctly leaves collections of two or more wrapped cycles open
to the general P66 decoder; it only denies them the stated metric
certificate.

## 4. Exact-value deletion is sound

V2 restores the actual canonical and lifted values before deletion.  Each
actual value is congruent to (1\pmod N).  Removing two copies of the same
integer (P) divides the selected square by (P^2) and divides its positive
root by (P\equiv1\pmod N).  The normalized root is unchanged.

This remains valid for shared logical edges and for equality between a
canonical value and a lifted value.  It does not confuse conceptual bridge
columns with different supplied roots.  Under the metric hypotheses, the
selection cannot delete to the empty dependency, because an empty
dependency has normalized root (+1), while the preserved root is
non-global.

## 5. The size and quasipolynomial scope claims pass

For anchors at most (H>1) on a cycle of length (k),

\[
A_{\mathcal C}\le H^k
\]

and the wrapped-cycle obstruction forces

\[
k>{\log N\over2\log H}.
\]

A fixed quasipolynomial magnitude bound
(2^{(\log n)^{O(1)}}) is (2^{o(n)}), while
(\sqrt N=2^{\Theta(n)}).  Therefore it cannot contain a wrapped positive
cycle for all sufficiently large (n).  This is an arithmetic size
obstruction, not a runtime lower bound.

The two stated escape scopes are also legitimate and are not existence
claims.

1. With anchors at most (n^3), reaching the necessary scale can take
   (\Theta(n/\log n)) selected edges.  This is polynomially many records.
   V2 explicitly does not claim a public way to find or close such a path,
   and it does not claim that exhaustive path search is quasipolynomial.
2. Under the quoted F130 caps, an allowed even exponent can make the
   expanded integer anchor have quasipolynomial bit length and magnitude
   above (\sqrt N).  Arithmetic on that explicit expansion remains within
   quasipolynomial work.  V2 only says that this possibility is not ruled
   out; it does not claim that such a word produces a containment cycle.

Thus there is no hidden claim that the current F130 source already hits the
required characteristic scale in a useful way.

## 6. The (N=35) certificate checks exactly

The raw reductions are

\[
13\cdot2^2=52=17+35,
\qquad
17\cdot3^2=153=13+4\cdot35.
\]

The inverses are (17^{-1}=33\pmod{35}) and
(13^{-1}=27\pmod{35}).  Hence the four actual values are

\[
561,\quad1716,\quad351,\quad4131.
\]

Their positive square root can be reconstructed without trusting the
displayed decimal square:

\[
\sqrt{(561)(1716)(351)(4131)}
=(13\cdot17\cdot2\cdot3)(33\cdot27)
=1181466.
\]

It is (6\pmod{35}).  Also

\[
6^2-1=35,
\qquad
\gcd(5,35)=5,
\qquad
\gcd(7,35)=7.
\]

The blocks (13,17) are pairwise coprime units, and the anchors (2,3)
are eligible primes.  V2 correctly labels this as a conditional frozen-basis
certificate, not as a claim about the actual P118 transcript for (N=35).

## 7. The determinant and rectangle boundaries pass

Substitution gives

\[
\Delta=sc-td=qa^2s-rb^2t.
\]

If (h=\gcd(c,d)), then (h\mid\Delta).  Both nonnegative terms in the
last difference are strictly below (qra^2b^2/N), so their absolute
difference is also strictly below that quantity.  Therefore

\[
hN\ge qra^2b^2
\quad\Longrightarrow\quad
|\Delta|<h
\quad\Longrightarrow\quad
\Delta=0.
\]

When (\Delta=0), the coprime reduction of (t,s) gives

\[
c=\tau z,
\quad d=\sigma z,
\quad qa^2=\tau(z+gN),
\quad rb^2=\sigma(z+gN).
\]

The exact bridge root divided by the supplied root is
((z+gN)/z\equiv1\pmod N).  The (t=s=0) case also consists of individual
root-(+1) squares.  The zero determinant is therefore a global decoy.

Finally, direct modular substitution maps the four cross-star endpoints to

\[
u,quad u\alpha,quad u\beta,quad u\alpha\beta.
\]

The P114 rectangle identification is exact, and V2 makes no new density
claim for it.

## 8. Wording qualification

Two summary sentences omit the word **wrapped** when they say that bounded
positive cycles are asymptotically impossible.  Read literally, that would
also exclude unwrapped root-(+1) cycles, which the proof does not exclude.
Every formal theorem and the detailed consequence in Section 5 correctly
says **wrapped positive directed cycle**.  This is a non-material summary
shorthand, but the manifest should use the precise phrase when it is next
updated.

The logarithmic length formula also implicitly assumes (H>1), as is true
for the prime-anchor cases under discussion.

## 9. Surviving content and remaining gate

Relative to P129, V2 permits nonsquare residuals on individual edges and
closes them only at the cycle-collection level.  Relative to F143, it is an
arithmetic containment statement, not a formal commutation cycle.  Its most
important unconditional result is negative but exact:

\[
\boxed{
\text{a stored positive-direction cycle with a wrapped edge requires }
\prod_ea_e>\sqrt N.
}
\]

The positive part is a correct conditional factoring certificate.  V2 does
not prove a cycle selector, a residual-square law at this scale, an
all-input theorem, or a factoring algorithm.  The remaining live scope is
exactly the scope it states: a selected long or large-anchor cycle, an
arithmetic hypercycle outside positive containment cycles, or a non-formal
signed cycle with a non-global root.
