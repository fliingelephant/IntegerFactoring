# F150 V2 blind reconstruction

## Protocol and verdict

I used only `V2_STATEMENT.md` as an F150 source. Before reading it, I
verified its SHA-256 digest:

```text
04725f9125976998d482663774cfcd11a17f215c953bc81be701bad6e318d7ee
```

I did not inspect `PROOF.md`, either V1 file, an audit, a manifest, a
ledger, or another F150 artifact.

**Verdict: PASS for every self-contained algebraic and numerical claim.**
The reciprocal-anchor theorem, its odd-input factoring conclusion, the
ceiling construction, and the \(N=77\) certificate all reconstruct from
first principles.

There is one statement-only evidence limit. The paragraph about the
"actual canonical and lifted P128 retained columns" uses data-model terms
that this statement does not define. Its deletion rule is sound under the
invariant stated in that paragraph, but the statement alone cannot prove
that an external P128 implementation has that invariant. The
quasipolynomial-cost sentence is also a conditional closure claim, not a
construction of a useful bank.

## 1. Units and exact residual synchronization

Let

\[
h=[xy]_N.
\]

Since \(x\) and \(y\) are units, \(h\) is a unit. In particular, all
modular divisions used later exist.

The first containment equality gives

\[
yT=[xy^2]_N\equiv xy^2\equiv yh\pmod N.
\]

Cancellation of the unit \(y\) gives \(T\equiv h\pmod N\). The
least-positive-residue condition gives

\[
1\le yT<N,
\]

so \(1\le T<N\). Also \(1\le h<N\). Hence the congruence forces
\(T=h\), not only equality modulo \(N\). The second containment equality
similarly gives

\[
xS\equiv xh\pmod N,
\qquad 1\le S,h<N,
\]

and therefore \(S=h\). Thus

\[
S=T=h.
\]

Substitution into the original exact residue equalities gives

\[
[xy^2]_N=yh<N,
\qquad
[yx^2]_N=xh<N.
\]

This proves the claimed no-second-wrap interpretation. It also proves
that the residual product is the exact square \(ST=h^2\).

This synchronization argument does not need \(N\) to be odd. It works for
any modulus for which \(x\) and \(y\) are units and the two positive exact
containments hold.

## 2. Exact bridge square and root orientation

Using \(S=T=h\), the two bridge integers are exactly

\[
\begin{aligned}
D_x&=(xy^2)[xy^2]_N=(xy^2)(yh)=xy^3h,\\
D_y&=(yx^2)[yx^2]_N=(yx^2)(xh)=yx^3h.
\end{aligned}
\]

Their product is

\[
D_xD_y=x^4y^4h^2=(x^2y^2h)^2.
\]

Let the positive exact square root be

\[
R=x^2y^2h.
\]

Each bridge has its displayed canonical residue as a supplied modular
square root because

\[
D_x\equiv [xy^2]_N^2,
\qquad
D_y\equiv [yx^2]_N^2
\pmod N.
\]

The product of those supplied roots is therefore

\[
M=(yh)(xh)=xyh^2.
\]

The slash in the normalized root must mean multiplication by a modular
inverse. It is not required to be exact integer division. Since \(M\) is
a unit,

\[
\rho=RM^{-1}
 =x^2y^2h\,(xyh^2)^{-1}
 =xyh^{-1}
 \equiv1\pmod N,
\]

where the last step uses \(h\equiv xy\pmod N\). Reversing the quotient
gives

\[
MR^{-1}=h(xy)^{-1}\equiv1\pmod N.
\]

Thus the anchor product is \(A=xy\), the residual square root is \(h\),
and the two reciprocal orientations are \(A/h\) and \(h/A\). Both are
\(+1\). Choosing the negative exact square root would give \(-1\), which
is also a global root. There is no orientation that gives a non-global
square root from this two-edge relation.

For the positive orientation and odd \(N\),

\[
\gcd(\rho-1,N)=\gcd(0,N)=N,
\qquad
\gcd(\rho+1,N)=\gcd(2,N)=1.
\]

Oddness is needed only for the second terminal gcd. If \(N>2\) is even,
parity already gives the proper factor \(2\). Therefore the advertised
odd-\(N\) scope is correct and conservative.

An endpoint gcd or endpoint sign gcd can still produce a factor before
this relation is decoded. That result would come from the screen, not
from the normalized cycle root, so it does not contradict the theorem.

## 3. Duplicate and supplied-root semantics

The root calculation depends on both an exact bridge value and its
indexed supplied root. Exact equality of transformed bridge integers is
not enough to identify two bridge occurrences. If

\[
D\equiv r_1^2\equiv r_2^2\pmod N,
\]

a composite modulus can have \(r_1\not\equiv\pm r_2\pmod N\). Replacing
one supplied root by the other can change the normalized root. There is
an exact transformed-value example modulo \(15\):

\[
16[16]_{15}=16\cdot1=16,
\qquad
4[4]_{15}=4\cdot4=16.
\]

The exact transformed value is the same, but its indexed supplied root is
\(1\) in the first occurrence and \(4\) in the second. Their product is
the exact square \(16^2\), while the supplied-root product is \(4\). Its
normalized root is \(16\cdot4^{-1}\equiv4\pmod {15}\), which is
non-global and exposes \(3\) and \(5\). This confirms the statement's
warning: transformed \(D\) values must not be deleted by raw integer
equality without their supplied-root metadata.

Under the deletion rule stated in V2, duplicate identity is evaluated on
the actual retained column together with that metadata. If all eligible
cycle-column occurrences have modular value \(1\) and supplied root \(1\),
choosing the first such occurrence cannot change the modular calculation.
Deletion can remove an occurrence needed by the displayed dependency; in
that case there is no surviving cycle output. If the reciprocal cycle
survives, Sections 1 and 2 still force its root to be global.

This is the exact limit of a statement-only reconstruction. V2 does not
define a P128 canonical column, a lifted column, or the retention
procedure. I therefore cannot independently derive the external invariant
that every eligible P128 column is \((1,1)\). I can verify that the
metadata-aware rule is logically sufficient and that the explicit refusal
to deduplicate transformed \(D\) values is necessary.

## 4. Ceiling-reciprocal construction

Let

\[
1<a<\sqrt N,
\qquad
q=\left\lceil\frac Na\right\rceil,
\qquad
h=qa-N.
\]

If \(h=0\), then \(N=qa\), so \(a\) is a proper divisor because
\(1<a<\sqrt N<N\).

Assume \(h>0\). The defining ceiling inequalities give

\[
(q-1)a<N<qa,
\]

and hence \(0<h<a\). Also \(a<\sqrt N\) implies
\(N/a>\sqrt N>a\), so \(q>a\). Since \(a\ge2\) and \(N\ge3\),
\(q<N\). Therefore

\[
0<h<a<q<N.
\]

If neither \(a\) nor \(q\) has a proper gcd with \(N\), both are units;
their being strictly between \(1\) and \(N\) rules out gcd \(N\). Also
\(h\equiv qa\pmod N\), so \(h\) is a unit.

Now

\[
qa^2=a(N+h)=aN+ah.
\]

The bound \(ah<a^2<N\) shows that the canonical residue is exactly

\[
[qa^2]_N=ah.
\]

Similarly,

\[
aq^2=q(N+h)=qN+qh.
\]

To check the less immediate residue bound, use \(h\le a-1\) and
\(h<q\):

\[
qh\le q(a-1)=qa-q=N+h-q<N.
\]

Thus

\[
[aq^2]_N=qh.
\]

Taking \(x=q\) and \(y=a\) puts these equations exactly in the theorem's
setup, with \(S=T=h\). Its normalized root is

\[
qah^{-1}\equiv1\pmod N.
\]

The cost sentence is valid with its stated qualifier. Let
\(n=\lceil\log_2 N\rceil\). Computing \(q,h\), two gcds, and the displayed
products for one pair costs polynomially many bit operations in \(n\).
If a bank has quasipolynomial size in \(n\) and its explicit generator
also runs in quasipolynomial time, multiplying that cost by a polynomial
per-pair cost remains quasipolynomial. This does not prove that a useful
bank exists. In particular, enumerating every \(a<\sqrt N\) has
\(\Theta(\sqrt N)\) entries and is exponential in the input bit length;
V2 does not claim otherwise.

Every isolated pair generated this way has root \(+1\). A dependency that
mixes pairs or closes through older columns would be a different
hypercycle and is outside the theorem.

## 5. The \(N=77\) certificate

For \(N=77\) and \(a=8\),

\[
q=\left\lceil\frac{77}{8}\right\rceil=10,
\qquad
h=10\cdot8-77=3.
\]

Both public values pass the ordinary unit screen:

\[
\gcd(8,77)=\gcd(10,77)=1.
\]

The residues are

\[
10\cdot8^2=640=8\cdot77+24,
\qquad
8\cdot10^2=800=10\cdot77+30,
\]

so they equal \(8h=24\) and \(10h=30\), respectively. The claimed
inverses are exact:

\[
24\cdot61=1464=19\cdot77+1,
\qquad
30\cdot18=540=7\cdot77+1.
\]

Using each endpoint and its canonical inverse, the four sign screens are

\[
\begin{aligned}
\gcd(24-61,77)&=1,&
\gcd(24+61,77)&=1,\\
\gcd(30-18,77)&=1,&
\gcd(30+18,77)&=1.
\end{aligned}
\]

If "endpoint sign" instead denotes direct \(r\pm1\) screens, those also
all return \(1\): the tested values are \(23,25,29,31\).

With \(x=q=10\) and \(y=a=8\), the bridges are

\[
D_q=640\cdot24=15{,}360,
\qquad
D_a=800\cdot30=24{,}000.
\]

Their positive exact root is

\[
x^2y^2h=10^2\cdot8^2\cdot3=19{,}200,
\]

and direct multiplication confirms

\[
15{,}360\cdot24{,}000=368{,}640{,}000=19{,}200^2.
\]

The supplied root is \(24\cdot30=720\). Reduction gives

\[
19{,}200\equiv27\pmod {77},
\qquad
720\equiv27\pmod {77}.
\]

Since \(27^{-1}\equiv20\pmod {77}\), the normalized modular quotient is

\[
19{,}200\cdot720^{-1}\equiv27\cdot20\equiv1\pmod {77}.
\]

The ordinary rational quotient \(19{,}200/720=80/3\) is not an integer;
this again confirms that the slash denotes modular division. The terminal
gcds are \(77\) and \(1\), so the certificate is an exact null-screen
example.

## 6. Scope audit

The proof uses both reciprocal-anchor equations and positivity of the
canonical residue presentations. It does not establish a claim about
nonreciprocal anchors, longer directed cycles, cross-column hypercycles,
or signed presentations. It also does not rule out a factor obtained by
parity, an endpoint screen, or a separate adaptive mechanism. The six
listed exclusions therefore match the actual logical reach of the proof.

The comparisons with P128--P131 and the description of their conventions
are external provenance claims. They are not needed for the algebra above,
and I did not inspect those sources under the blind protocol.
