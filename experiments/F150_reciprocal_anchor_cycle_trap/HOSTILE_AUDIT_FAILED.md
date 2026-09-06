# F150 hostile audit — FAIL as frozen

## Verdict

**FAIL as written, with local repairs.** The residual-synchronization
identity, exact bridge square, intended odd-input root trap,
ceiling-reciprocal construction, quasipolynomial cost statement, and the
\(N=77\) certificate all survive re-derivation. The frozen statement has
two domain defects:

1. it permits even \(N\), for which the declared global root \(+1\) still
   gives the proper terminal gcd \(\gcd(1+1,N)=2\); and
2. it does not state that the new corollary parameter \(a\) is an integer,
   although divisibility, gcd, and least-positive residues are then applied
   to it.

The first defect makes the sentence “this cycle channel never factors
\(N\)” false on its stated domain. The second makes the corollary ill-typed
under its literal quantifiers. Neither defect damages the intended
structural result after odd-input preprocessing and an integer-domain
qualification.

Audited frozen hashes:

- `STATEMENT.md`:
  `485396a4df33ab8b708b35de12f018489f942e783f1d680c3c4c2bccb6c23435`;
- `PROOF.md`:
  `a9d94ec57fae30ae4a6e0084d9558dfc52721f1e5607af38a201dedc6ec5cd68`;
- pre-audit `MANIFEST.md`:
  `e272cfaf1e8482629c76779d83c46bed5880735789dff1c690aa38dc6741bb67`.

No passing `HOSTILE_AUDIT.md` was created.

## 1. Fatal scope defect: a global root can split an even input

The setup assumes only \(N\ge3\). Theorem 2 obtains

\[
\rho\equiv1\pmod N.
\]

For odd \(N\), this gives only

\[
\gcd(\rho-1,N)=N,\qquad
\gcd(\rho+1,N)=1.
\]

For every even \(N>2\), however,

\[
\boxed{\gcd(\rho+1,N)=\gcd(2,N)=2},
\]

which is a proper factor. Thus “global root” does not imply “no proper gcd”
on the frozen domain.

There are legal frozen instances, so this is not only an empty endpoint.
For example, take

\[
N=6,\qquad x=y=5.
\]

Then \(\gcd(xy,N)=1\),

\[
[xy^2]_6=[125]_6=5=y\cdot1,\qquad
[yx^2]_6=5=x\cdot1,
\]

and \(h=[xy]_6=1\). All hypotheses of Theorems 1 and 2 hold. The
normalized root is \(+1\), but its plus-sign terminal gcd is \(2\).

The statement notes that an endpoint screen can factor before decoding. On
an even input that is also true, because all units are odd. It does not
repair the stronger claim that the cycle's terminal root cannot factor.

Minimal repair: assume that \(N\) is odd in the setup, with the ordinary
factor-\(2\) preprocessing stated outside the theorem. Alternatively, keep
arbitrary \(N\) but weaken the conclusion to “the normalized root is the
global root \(+1\)” and explicitly exclude the known even-factor gcd from the
no-factor sentence.

## 2. Missing integer domain in the ceiling-reciprocal corollary

The corollary begins only with

\[
1<a<\sqrt N,\qquad q=\left\lceil N/a\right\rceil.
\]

It then uses \(a\mid N\), \(\gcd(a,N)\), and residues such as
\([qa^2]_N\). These operations require \(a\) to be an integer. The
inequality alone permits real or rational values. For example,
\(N=77\) and \(a=4/3\) satisfy the displayed inequality, but
\(h=qa-N\) and \(qa^2\) are not integers, so the subsequent modular
statements are undefined.

Integrality is also used in the proof of \(q>a\), \(q<N\), and
\(0<h<a\). The clean repair is

\[
\boxed{a\in\mathbb Z,\qquad 1<a<\sqrt N.}
\]

With this repair, \(q\) and \(h=qa-N\) are integers. If \(h=0\),
then \(\gcd(a,N)=a\) is proper. Otherwise \(0<h<a<q<N\), as
claimed.

## 3. Residual synchronization passes

Write

\[
xy=mN+h,\qquad 1\le h<N.
\]

Then \([xy^2]_N=[yh]_N=yT\). Ordinary division gives

\[
yh=tN+yT,\qquad 0\le t<y.
\]

Reduction modulo \(y\) gives \(tN\equiv0\pmod y\). Since
\(\gcd(y,N)=1\), one has \(y\mid t\). The bound on \(t\) forces
\(t=0\), so \(T=h\) and \(yh<N\). Interchanging \(x\) and
\(y\) gives \(S=h\) and \(xh<N\). No canonical-residue
endpoint is missing from this argument.

## 4. Exact bridge square and root calculation pass

The two bridge values are exactly

\[
D_x=(xy^2)(yh)=xy^3h,\qquad
D_y=(yx^2)(xh)=yx^3h.
\]

Therefore

\[
D_xD_y=x^4y^4h^2=(x^2y^2h)^2.
\]

Their supplied modular root is

\[
(yh)(xh)=xyh^2.
\]

Under the P128/P131 convention, positive exact root divided by supplied
root gives

\[
\rho=\frac{x^2y^2h}{xyh^2}=\frac{xy}{h}\equiv1\pmod N.
\]

The frozen text writes the inverse ratio \(h/(xy)\). This is harmless
here: it is also \(1\), and a normalized square root of one equals its own
inverse. A corrected version should use the established P128/P131
orientation throughout to avoid a convention switch.

For odd \(N\), the result is exactly the advertised root-\(1\) trap.

## 5. Exact-value deletion passes under the established source rule

The deletion sentence is valid for the **actual** canonical and lifted P128
relation values. Each such value is \(1\pmod N\) and has supplied root
\(1\). Removing a selected equal pair divides its positive exact root by
that common value, which is \(1\pmod N\), so the normalized-root class is
unchanged. First-occurrence replacement by an equal actual value also
changes neither the integer product nor its supplied root. A dependency can
therefore disappear, but a surviving version cannot change from root
\(+1\) to a non-global root.

This sentence must not be read as permission to deduplicate transformed
bridge integers \(D\) by exact integer equality alone. P128/P129 require
their indexed supplied roots to be retained. The corrected statement should
name the actual-value deletion rule explicitly.

## 6. Ceiling-reciprocal identities and cost pass after repair

For integer \(a\) with \(1<a<\sqrt N\) and \(a\nmid N\), write

\[
qa=N+h,\qquad 0<h<a.
\]

Then \(a^2<N\) gives \(q>a\), and integer \(a\ge2\) gives
\(q<N\). Exact multiplication gives

\[
qa^2=aN+ah,\qquad 0<ah<a^2<N,
\]

so \([qa^2]_N=ah\). Also

\[
aq^2=qN+qh,\qquad
qh\le q(a-1)=N+h-q<N,
\]

so \([aq^2]_N=qh\). If the gcd screens on \(a\) and \(q\)
are null, both are units and this is exactly the reciprocal-anchor cycle
with synchronized residual \(h\).

Each value in this construction has \(O(\log N)\) bits, and division,
reduction, multiplication, inverse computation, and gcd have polynomial bit
cost. Applying the construction to an explicitly generated
quasipolynomial-size bank therefore has quasipolynomial total cost. This is
only a cost statement; it does not claim that the bank supplies useful
cycles.

## 7. The \(N=77\) certificate passes

For \(a=8\), one has \(q=10\) and \(h=3\). Directly,

\[
[10\cdot8^2]_{77}=24,\qquad
[8\cdot10^2]_{77}=30.
\]

The inverse identities are

\[
24\cdot61=19\cdot77+1,\qquad
30\cdot18=7\cdot77+1.
\]

The four endpoint sign quantities are \(-37,85,12,48\), each coprime
to \(77\). The exact bridge values satisfy

\[
15{,}360\cdot24{,}000=19{,}200^2.
\]

Both the supplied root \(24\cdot30=720\) and the positive exact root
\(19{,}200\) are \(27\pmod{77}\). Either normalized-root convention
therefore gives \(+1\). The certificate proves the intended odd-input
decoy and does not prove a factoring algorithm.

## Required V2 repairs

1. Restrict the setup to odd integer \(N\), or remove the no-factor claim
   for even inputs and state the trivial factor-\(2\) exception.
2. State \(a\in\mathbb Z\) in the ceiling-reciprocal corollary.
3. Use the standard P128/P131 normalized-root orientation, even though the
   inverse has the same value here.
4. Qualify exact-value deletion as deletion among actual P128 relation
   values, not transformed bridge values without supplied-root metadata.

After these local changes, the proof should receive a fresh hostile audit
and a new statement-only blind reconstruction.
