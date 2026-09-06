# F150 V2 hostile re-audit — PASS

## Verdict

**PASS.** The V2 statement and proof repair all four issues identified by the
failed audit. I found no remaining domain error, canonical-residue error,
root-orientation error, deletion error, cost overclaim, or certificate error.

The result is still a narrow structural trap. It proves no cycle-hitting law,
no nonreciprocal or hypercycle obstruction, and no factoring algorithm.

## Audited inputs

I read the complete V2 statement and proof, the preserved original statement
and proof, the failed hostile audit, and the current manifest. Their SHA-256
hashes are:

- `V2_STATEMENT.md`:
  `04725f9125976998d482663774cfcd11a17f215c953bc81be701bad6e318d7ee`;
- `V2_PROOF.md`:
  `5afe0be2bf8526064b421384c27452fc393f88cc88cd47a07e52f7cb3a03ec66`;
- preserved `STATEMENT.md`:
  `485396a4df33ab8b708b35de12f018489f942e783f1d680c3c4c2bccb6c23435`;
- preserved `PROOF.md`:
  `a9d94ec57fae30ae4a6e0084d9558dfc52721f1e5607af38a201dedc6ec5cd68`;
- `HOSTILE_AUDIT_FAILED.md`:
  `3405daaec86ca8853c1b4441b5e3514e25e05caeb5c8f66b23cd7ef6404f55e0`;
- current `MANIFEST.md`:
  `af2c9e1f3b62c2fd722576dbab6035e4209cababea237073ed2b985d4f334808`.

The two requested V2 hashes match exactly. The preserved original statement,
proof, and failed-audit hashes also match the manifest.

## 1. The odd-input repair is complete

V2 first separates parity. For every even integer input \(N>2\), the public
factor \(2\) is already proper. The theorem then assumes that \(N\ge3\) is an
odd integer.

The normalized root proved below is \(\rho\equiv1\pmod N\). Therefore, on
the stated branch,

\[
\gcd(\rho-1,N)=N,
\qquad
\gcd(\rho+1,N)=\gcd(2,N)=1.
\]

Neither terminal gcd is proper. This removes the frozen even-input
counterexample \(N=6,x=y=5\). V2 also states
\(a\in\mathbb Z\) in the ceiling corollary, so every division, gcd, and
residue operation there is well-typed.

Oddness is not used in residual synchronization. It is used exactly where
V2 says it is used: to turn the global root \(+1\) into a null terminal
screen.

## 2. Canonical-residue synchronization is exact

Let

\[
xy=mN+h,
\qquad
1\le h<N.
\]

Because \(x\) and \(y\) are units, \(h=[xy]_N\) is also a unit. Multiplying
by \(y\) gives

\[
[xy^2]_N=[yh]_N=yT.
\]

Write the ordinary quotient as

\[
yh=tN+yT.
\]

The bound \(yh<yN\) gives \(0\le t<y\). Reduction modulo \(y\) gives
\(tN\equiv0\pmod y\). Since \(\gcd(y,N)=1\), one has \(y\mid t\), and the
quotient bound forces \(t=0\). Hence

\[
T=h,
\qquad
yh<N.
\]

Interchanging \(x\) and \(y\) gives

\[
S=h,
\qquad
xh<N.
\]

No zero-residue case is hidden here: all displayed residues are residues of
units. The proof uses both reciprocal divisibilities and does not infer one
from the other.

## 3. The bridge square and standard root orientation are correct

The synchronized canonical residues are

\[
c_x=[xy^2]_N=yh,
\qquad
c_y=[yx^2]_N=xh.
\]

Thus the two conceptual bridge values are

\[
D_x=(xy^2)c_x=xy^3h,
\qquad
D_y=(yx^2)c_y=yx^3h,
\]

and

\[
D_xD_y=x^4y^4h^2=(x^2y^2h)^2.
\]

Their positive exact root is \(x^2y^2h\). Their indexed supplied-root
product is

\[
c_xc_y=xyh^2.
\]

The promoted P128/P129 convention divides the positive exact root by the
supplied modular root. Therefore

\[
\rho
=x^2y^2h\,(xyh^2)^{-1}
=xyh^{-1}
\equiv1\pmod N,
\]

because \(h\equiv xy\pmod N\). Every denominator is a unit. This is also the
P131 cycle formula \(A/S\) with anchor product \(A=xy\) and residual root
\(S=h\). The inverse ratio used in the frozen version is also \(1\), but V2
now uses the standard orientation consistently.

## 4. Actual-column deletion does not change the root

For one P128 word position, write

\[
A=cw,
\qquad
B=Uw,
\qquad
D=Uc,
\qquad
w\equiv c^{-1}\pmod N.
\]

The actual canonical and lifted columns \(A,B\) are both \(1\pmod N\), and
each carries supplied root \(1\). The conceptual bridge \(D\) instead carries
the indexed supplied root \(c\). The standard invertible column replacement
between \((A,B)\) and \((A,D)\) preserves the normalized-root map.

Now suppose two actual columns have the same positive integer value
\(P_i=P_j=P\). Selecting both gives exact product \(P^2\), positive root
\(P\), and supplied-root product \(1\). Its normalized root is
\(P\equiv1\pmod N\). Thus a duplicate direction is root-null. Replacing a
selected later occurrence by the globally retained first occurrence changes
neither the integer value nor its supplied root. An even multiplicity cancels
through a root-\(1\) direction; an odd multiplicity uses the retained
representative.

Consequently, exact-value deletion can remove the displayed dependency, but
it cannot turn a surviving dependency from root \(+1\) into a useful root.
This conclusion applies only to the actual canonical and lifted values. It
does not permit deduplication of equal transformed bridge integers without
their indexed supplied roots. V2 states this distinction correctly.

The algebraic theorem is slightly broader than the legal P128 source subset:
it needs only the displayed unit and divisibility hypotheses. Whenever the
two word positions occur in the P128 source, the actual-column interpretation
above applies. V2 does not claim that the frozen source must hit such a pair.

## 5. The ceiling-reciprocal corollary is correct

Let \(a\in\mathbb Z\), \(1<a<\sqrt N\),
\(q=\lceil N/a\rceil\), and \(h=qa-N\).

If \(h=0\), then \(a\mid N\). Since \(1<a<\sqrt N\), the gcd \(a\) is a
proper factor. Otherwise

\[
qa=N+h,
\qquad
0<h<a.
\]

The inequality \(N/a>a\) gives \(q>a\). Since \(a\ge2\) and \(N\) is odd,

\[
q\le\left\lceil\frac N2\right\rceil<N.
\]

If neither the \(a\)-screen nor the \(q\)-screen succeeds, both are units.
Exact multiplication then gives

\[
qa^2=aN+ah,
\qquad
0<ah<a^2<N,
\]

so

\[
[qa^2]_N=ah.
\]

Similarly,

\[
aq^2=qN+qh.
\]

Since \(h\le a-1\) and \(h<q\),

\[
qh\le q(a-1)=qa-q=N+h-q<N.
\]

Therefore

\[
[aq^2]_N=qh.
\]

These are exactly the two reciprocal-anchor identities with
\((x,y)=(q,a)\), so their normalized root is \(+1\).

Let \(n\) be the input bit length. The values \(a,q,h\), both unreduced
words, all residues, and all gcd or inverse operands have \(O(n)\) bits.
Integer division, multiplication, reduction, inversion, and gcd therefore
have polynomial bit cost per \(a\). Applying them to an explicitly generated
bank of quasipolynomial size has quasipolynomial total cost. This cost claim
does not imply a useful-root probability or a source-hitting theorem.

## 6. The \(N=77\) certificate is exact

For \(N=77,a=8,q=10,h=3\), direct recomputation gives

\[
[10\cdot8^2]_{77}=24,
\qquad
[8\cdot10^2]_{77}=30.
\]

The inverse checks are

\[
24\cdot61=19\cdot77+1,
\qquad
30\cdot18=7\cdot77+1.
\]

The endpoint differences and sums are

\[
-37, 85, 12, 48,
\]

and each has gcd \(1\) with \(77\). The bridge values are

\[
D_q=640\cdot24=15{,}360,
\qquad
D_a=800\cdot30=24{,}000,
\]

with

\[
D_qD_a=368{,}640{,}000=19{,}200^2.
\]

The supplied root is \(24\cdot30=720\). Both \(19{,}200\) and \(720\) are
\(27\pmod{77}\), so the standard normalized ratio is \(+1\). The certificate
survives all named endpoint sign screens and exhibits only the claimed
global-root decoy.

## 7. Independent finite stress check

As supporting evidence, I exhaustively checked the theorem with exact integer
arithmetic for every odd \(3\le N\le501\), every unit pair \(x,y\), and every
pair satisfying both reciprocal divisibilities. All 87,861 qualifying cycles
satisfied synchronization, both strict residue bounds, the exact bridge
square, and normalized root \(+1\).

I also checked every integer anchor \(a\) with \(1<a<\sqrt N\) for every odd
\(3\le N\le1001\). All 9,815 cases satisfied the divisor branch or the two
claimed canonical-residue identities and bounds. The complete displayed
\(N=77\) tuple was checked separately. No counterexample occurred.

The finite check is corroborating evidence. The general claims follow from
the exact arguments above.

## Scope conclusion

All requested V2 claims pass. In particular:

1. parity preprocessing makes the no-factor conclusion valid on the stated
   odd branch;
2. both canonical residues synchronize to the same exact residual \(h\);
3. the standard positive-root-over-supplied-root orientation gives \(+1\);
4. first-occurrence deletion is safe for actual P128 columns and is not
   extended to unindexed bridge values;
5. the ceiling selector and its quasipolynomial cost statement are valid;
   and
6. every integer in the \(N=77\) certificate recomputes exactly.

This re-audit does not supply the still-required independent statement-only
blind reconstruction.
