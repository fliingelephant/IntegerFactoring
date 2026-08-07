# F62 — exact order and HSP boundary for cross-relation selection

**Status:** revised proof-only boundary result. No research computation was
run. The hostile audit preserves the failed first version and its hash.

The full F62 direct screen and the hidden-lattice 2-torsion target are not the
same problem.

- The full screen accepts any legal block product \(g\) for which
  \(\gcd(g-1,N)\) or \(\gcd(g+1,N)\) is proper.
- The 2-torsion subtarget asks for a legal \(g\) that is self-inverse modulo
  \(N\) and is not either global sign.

The second target has an exact hidden-relation-lattice formulation. On the
even-order promise, the least nonidentity involutory power of one generator
is exactly half its order. Recovering the complete hidden relation lattice
contains unrestricted order finding. The broader direct screen can succeed
without any self-inverse residue.

No all-input classical selector is proved.

## 1. Finite source and legal block products

Let \(N\ge3\) be odd. Let

\[
A_i=x_i y_i=1+k_iN,
\qquad 1\le i\le m,
\]

be a finite indexed list of seed-relation occurrences. Equal rows remain
separate occurrences. Deliberate amplification must add explicit copies to
this list, and its transcript length is part of the cost.

Let the complete gcd-free block list be

\[
q_1,\ldots,q_s>1,
\qquad \gcd(q_j,N)=1.
\]

The blocks are pairwise coprime as integers. For each occurrence, let
\(\lambda_i\in\mathbb Z_{\ge0}^s\) be its exact exponent row:

\[
A_i=q^{\lambda_i}=\prod_{j=1}^s q_j^{\lambda_{i,j}}.
\]

Select an indexed sublist with \(c_i\in\{0,1\}\), and put

\[
E=\sum_{i=1}^m c_i\lambda_i.
\]

An orientation is a vector \(v\in\mathbb Z^s\) with

\[
0\le v_j\le E_j.
\]

It gives complementary whole-block divisors

\[
g=q^v,
\qquad
h=q^{E-v},
\qquad
gh=q^E\equiv1\pmod N.
\]

An F62 state is legal only when

\[
1<g<N.
\]

This is an integer-magnitude condition. Replacing an oversized integer
product by its residue modulo \(N\) does not preserve its divisor provenance
and is a different source rule.

A row-type model with capacities \(\mu_i\) is equivalent only when it uses
\(0\le c_i\le\mu_i\) and charges the complete capacity and exponent
encoding. This note uses the explicit occurrence model.

## 2. Full direct screening versus self-inverse screening

Define the two direct screens

\[
D_-(v)=\gcd(q^v-1,N),
\qquad
D_+(v)=\gcd(q^v+1,N).
\]

### Theorem 1 — exact full-screen condition

A legal orientation gives an immediate factor exactly when

\[
1<D_-(v)<N
\quad\text{or}\quad
1<D_+(v)<N.
\]

For squarefree \(N\), this says that \(q^v\) equals one chosen sign on a
nonempty proper set of CRT prime components. Its other components do not
need to equal either sign. For nonsquarefree \(N\), even a partial positive
\(p\)-adic valuation of \(q^v\pm1\) can give a proper gcd.

This full condition is not a 2-torsion condition. For example,

\[
N=21,
\qquad
g=10,
\qquad
g^2\not\equiv1\pmod {21},
\qquad
\gcd(g-1,21)=3.
\]

The earlier F62 cross-relation witness selects exactly this \(g\). Thus a
useful source vector need not have its double in a hidden relation lattice.

Now define the public homomorphism

\[
\Phi_N:\mathbb Z^s\longrightarrow(\mathbb Z/N\mathbb Z)^\times,
\qquad
\Phi_N(v)=q^v\pmod N,
\]

and its full modular relation lattice

\[
\Lambda_N=\ker\Phi_N.
\]

### Theorem 2 — exact self-inverse subtarget

For every legal orientation,

\[
h\equiv g^{-1}\pmod N.
\]

The selected state is self-inverse exactly when

\[
g\equiv h\pmod N
\quad\Longleftrightarrow\quad
g^2\equiv1\pmod N
\quad\Longleftrightarrow\quad
2v\in\Lambda_N.
\]

Under these equivalent conditions, both direct gcds are proper exactly when

\[
\Phi_N(v)\notin\{1,-1\}.
\]

**Proof.** The complement relation gives \(gh\equiv1\pmod N\). The three
self-inverse conditions then follow directly from the definition of
\(\Lambda_N\). For odd \(N\), a square root of one is one of the two signs
on each prime-power component. A root that is not a global sign has both
signs on nonempty component sets, so both gcds are nontrivial and proper.
\(\square\)

The final gcd is still only the extractor. The main source problem is to
choose a legal vector. For the full screen, that vector can be a general CRT
separator. For the narrower lattice route, its double must lie in
\(\Lambda_N\).

A non-self-inverse state can also create a new inverse endpoint and new blocks
for later rounds. That iterative route is not a 2-torsion search at each
intermediate step.

## 3. Exact residue image of the old decoder

Put

\[
L_0=\langle\lambda_1,\ldots,\lambda_m\rangle_{\mathbb Z}
\subseteq\Lambda_N.
\]

Before quotienting by a global sign, the old decoder's modular root-residue
image is

\[
R_{\rm old}
=
\left\{
\Phi_N\!\left(\frac{\sum_i c_i\lambda_i}{2}\right):
c_i\in\{0,1\},\ 
\sum_i c_i\lambda_i\in2\mathbb Z^s
\right\}.
\]

### Theorem 3 — known-lattice 2-saturation gives the same residue image

One has the exact modular-image equality

\[
\boxed{
R_{\rm old}
=
\{\Phi_N(v):v\in\mathbb Z^s,\ 2v\in L_0\}.}
\]

**Proof.** The forward containment is immediate. Conversely, write

\[
2v=\sum_i z_i\lambda_i
\]

with \(z_i\in\mathbb Z\). Choose \(c_i\in\{0,1\}\) with
\(c_i\equiv z_i\pmod2\), including for negative \(z_i\). Then
\(z=c+2w\) for an integer vector \(w\), and

\[
v=\frac{\sum_i c_i\lambda_i}{2}+\sum_iw_i\lambda_i.
\]

The first term is integral. The second term lies in \(L_0\), so it maps to
1 under \(\Phi_N\). It can have negative coordinates, but every block is a
unit modulo \(N\), so those coordinates are valid for this residue-image
identity. \(\square\)

This is not an equality of positive integer roots or legal bounded divisors.
A right-hand vector can contain negative coordinates, lie outside every
current source box, or have \(q^v\ge N\).

For the abstract quotient interpretation, put

\[
Q_0=\mathbb Z^s/L_0,
\qquad
K=\Lambda_N/L_0.
\]

Then \(Q_0/K\) is the generated modular subgroup. The old decoder maps the
visible subgroup \(Q_0[2]\). An abstract nonidentity involution is represented
by a class \(x\in Q_0\) with

\[
x\notin K,
\qquad
2x\in K.
\]

To be a genuinely new *legal F62 self-inverse root*, the class must also:

1. map to a residue outside \(\{1,-1\}\) and outside the old image;
2. have a representative \(v\) in a box \(0\le v\le E\) made from a finite
   selected occurrence list; and
3. satisfy \(1<q^v<N\).

The abstract quotient conditions alone do not supply these source and
magnitude properties.

## 4. Exact cyclic order boundary

For one fixed unit residue \(a\), let \(r=\operatorname{ord}_N(a)\). Seek an
exponent \(e>0\) with

\[
a^{2e}=1,
\qquad
a^e\ne1.
\]

### Theorem 4 — the even-order promise

Such an exponent exists exactly when \(r\) is even. In that case all
solutions are

\[
e=\frac r2(2j+1),
\qquad j\in\mathbb Z_{\ge0},
\]

and the least solution is \(r/2\). Every solution gives the same involution
\(a^{r/2}\). A factoring-useful exponent exists exactly when that involution
is non-global.

**Proof.** The equations say \(r\mid2e\) and \(r\nmid e\). They force
\(r\) to be even and \(e/(r/2)\) to be odd. The converse is immediate.
\(\square\)

Thus, on the even-order promise, doubling the least nonidentity involutory
exponent gives the exact order. This statement does not apply to odd order,
where no answer exists.

There is also an exact abstract Turing equivalence. Define a total oracle that
returns the least such exponent or `NONE`. An order oracle implements it
immediately. Conversely:

- if the oracle returns \(e\) on \(a\), then \(r=2e\);
- if it returns `NONE`, then \(r\) is odd, \(-a\) has order \(2r\), and the
  least answer on \(-a\) is \(r\).

This reduction uses arbitrary modular residues. It need not preserve an F62
block list, source box, or integer-divisor certificate. A least
*factoring-useful* power oracle is weaker: it also has no answer when the
half-order involution is the global element \(-1\).

An arbitrary valid exponent does not determine the order. Modulo 21, the
same exponent \(e=3\) sends the order-6 base 2 and the order-2 base 8 to the
same non-global involution 8. Leastness is essential to the order identity.

For a legal one-block multiplicity scan, also take \(a\) to be its canonical
positive integer block representative with \(1<a<N\). If its available
exponent capacity is \(M\), the conditions

\[
r/2\le M,
\qquad
a^{r/2}<N
\]

are both necessary for the least involutory integer power to be an F62 state;
factoring also requires that its residue be non-global. Modular exponentiation
followed by reduction does not require the magnitude condition, but that is a
different source operation.

Finally, in the one-generator lattice model,

\[
\Lambda_N=r\mathbb Z.
\]

Therefore full relation-lattice recovery contains exact modular order finding
without an even-order promise.

## 5. A strict multi-block construction

Take

\[
N=65=5\cdot13.
\]

Use the two canonical inverse relations

\[
2\cdot33=66=1+65,
\qquad
21\cdot31=651=1+10\cdot65.
\]

Their complete gcd-free blocks are

\[
2,3,7,11,31.
\]

In this order, the two exact exponent rows are

\[
\lambda_1=(1,1,0,1,0),
\qquad
\lambda_2=(0,1,1,0,1).
\]

They are independent over \(\mathbb F_2\). Hence the old two-row square
decoder has zero kernel.

Choose the block 2 from the first relation and the block 7 from the second:

\[
g=2\cdot7=14<65.
\]

It divides \(66\cdot651\), but it divides neither relation value alone. The
aggregate quotient is

\[
\frac{66\cdot651-1}{65}=661,
\qquad
661\bmod14=3.
\]

Indeed,

\[
14^2=196=1+3\cdot65,
\]

so

\[
\gcd(14-1,65)=13,
\qquad
\gcd(14+1,65)=5.
\]

The two selected constituent blocks fail when tested separately by the usual
order-halving postprocessing:

\[
\operatorname{ord}_{65}(2)
=\operatorname{ord}_{65}(7)=12,
\qquad
2^6\equiv7^6\equiv-1\pmod {65}.
\]

Their individual direct \(g\pm1\) screens are also trivial. Their cross
product is a non-global element of order 2.

This comparison is only with the selected blocks 2 and 7. It is not a claim
that every blockwise order test on the complete public list fails. In fact,
block 3 has order 12 and

\[
3^6\equiv14\pmod {65},
\]

and blocks 11 and 31 also have useful half-order residues. Once 14 has been
selected, its own order is trivially 2. The new operation is the public
construction of 14 from two original block directions, not new
postprocessing after 14 is known.

This gives a valid polynomial partial selector. Given an explicit seed
transcript of polynomial total bit length, first compute the complete
gcd-free refinement. Then enumerate all occurrence-certified block pairs,
retain integer products below \(N\), and run both direct gcd screens. The
refinement, \(O(s^2)\) candidate products, modular tests, and gcds have
polynomial bit cost in the complete transcript and \(\log N\). This selector
factors the displayed input. It has no all-input success theorem.

## 6. An exact self-inverse total-multiplicity hierarchy

Let \(t\ge3\) be odd, and put

\[
G=2^t,
\qquad
N=\frac{G^2-1}{3},
\qquad
B=\frac{N+1}{2}.
\]

The canonical state 2 has the relation

\[
2B=N+1.
\]

Supply explicit indexed copies of this relation. Across all copies the block
types are \(2,B\). If a selection uses \(c<t\) occurrences, every legal
whole-block divisor below \(N\) is either \(B\) or \(2^a\) with
\(1\le a\le c\). A divisor containing both blocks is at least
\(2B=N+1\), and \(B^2>N\).

Neither possible type is self-inverse. From \(2B\equiv1\pmod N\), the
congruence \(B^2\equiv1\pmod N\) would imply \(4\equiv1\pmod N\), which is
impossible because \(N>3\). Also, for \(a<t\),

\[
0<2^{2a}-1<N,
\]

so \(2^{2a}\not\equiv1\pmod N\).

With exactly \(t\) explicit occurrences, the legal choice

\[
g=2^t=G<N
\]

satisfies

\[
g^2=1+3N.
\]

It is non-global because

\[
N=(G-1)\frac{G+1}{3},
\qquad
G\equiv1\pmod {G-1},
\qquad
G\equiv-1\pmod{(G+1)/3},
\]

and the two displayed factors are coprime and proper. The old decoder still
has only global roots: every even number of identical rows gives a power of
\(N+1\equiv1\pmod N\).

The order is exact. It divides \(2t\) because \(2^{2t}\equiv1\pmod N\).
Reduction modulo the factor \(2^t-1\) gives exact order \(t\), so the order
modulo \(N\) is a multiple of \(t\). Since \(2^t\not\equiv1\pmod N\),

\[
\operatorname{ord}_N(2)=2t.
\]

Thus the first legal self-inverse power in this explicit occurrence model
uses total multiplicity \(t\), exactly half the order.

This is not a support-size lower bound. The successful exponent vector has
support one. A constant-support rule with exponent capacity at least \(t\)
can select it. It is also not a lower bound against the full direct
\(g\pm1\) screen. For example, at \(t=9\), three occurrences permit
\(g=2^3=8\), and

\[
7=g-1\mid2^9-1\mid N,
\]

so the ordinary direct gcd already splits \(N\). The theorem concerns only
self-inverse total multiplicity.

Since \(t=\Theta(\log N)\), the successful amplified transcript still has
polynomial total length. The result does not rule out a polynomial-time
structured selector.

## 7. Exact HSP and Smith-normal-form boundary

The map

\[
\Phi_N:\mathbb Z^s\to(\mathbb Z/N\mathbb Z)^\times
\]

is a homomorphism, and two outputs are equal exactly when their exponent
difference lies in \(\Lambda_N\). In this algebraic sense, full relation
lattice recovery is an abelian hidden-subgroup problem. The case \(s=1\) is
the cyclic period map.

This identity alone is not a complete efficient quantum algorithm over the
infinite domain \(\mathbb Z^s\). Such a claim would also need a finite
sampling domain, truncation bounds, precision bounds, and a complete circuit
and success analysis. None is claimed here.

Suppose instead that a full-rank basis of \(\Lambda_N\) is supplied. Smith
normal form gives

\[
H=\mathbb Z^s/\Lambda_N
\cong\langle q_1,\ldots,q_s\rangle
\]

as a product of cyclic invariant factors. For each even invariant factor
\(d_i\), multiply its invariant-factor generator by \(d_i/2\). The resulting
elements form an \(\mathbb F_2\)-basis of \(H[2]\).

There are at most \(s\) such elements. If \(H\) contains a non-global
involution, at least one basis element is non-global: distinct nonzero basis
elements cannot all equal the single global residue \(-1\). Screening these
elements therefore solves the unbounded subgroup 2-torsion target.

The transformed exponent representatives can have negative coordinates.
They are valid modular products through inverses, but they need not be legal
positive F62 divisors.

Once the full basis is supplied, exact Smith postprocessing and modular
screening have polynomial bit cost in the total encoding of \(N\), all public
generators, the supplied lattice basis, the computed change-of-basis
transformation data, and the resulting exponent vectors. This charges any
large transformed representative. It does not prove an efficient way to
obtain the full lattice basis. Recovering that basis already contains exact
order finding when \(s=1\).

## 8. Unbounded subgroup data does not satisfy a finite source box

Take

\[
N=187=11\cdot17
\]

and the one-occurrence relation

\[
2\cdot94=188=2^2\cdot47.
\]

The complete block list is \(2,47\), and the one-copy box has
\(E=(2,1)\). Its proper legal divisors below \(N\) are exactly

\[
2,4,47,94.
\]

Every full direct screen is trivial:

\[
\begin{array}{c|cc}
g&\gcd(g-1,187)&\gcd(g+1,187)\\ \hline
2&1&1\\
4&1&1\\
47&1&1\\
94&1&1
\end{array}
\]

However,

\[
\operatorname{ord}_{187}(2)
=\operatorname{lcm}(10,8)=40,
\]

and its half-order power has opposite CRT signs:

\[
2^{20}\equiv1\pmod {11},
\qquad
2^{20}\equiv-1\pmod {17}.
\]

Thus the unbounded generated subgroup contains a non-global involution,
while the finite one-copy box contains neither a direct CRT separator nor a
non-global involution. Full order or HSP data does not remove the legal-box
and integer-magnitude constraints.

Conversely, a general F62 direct success need not give any involution. The
\(N=21,g=10\) witness in Section 2 already proves this.

The exact relationship is therefore:

- full lattice recovery contains exact modular order finding;
- on the even-order promise, the least nonidentity involutory exponent is
  exactly half the order;
- a supplied full lattice solves the unbounded subgroup 2-torsion task by
  Smith normal form;
- a legal F62 self-inverse state also needs a finite source-box
  representative and an integer product below \(N\); and
- the full F62 direct screen is broader than the 2-torsion target.

No classical simulation of Shor and no efficient quantum HSP implementation
follows from these identities.

## 9. Algorithmic consequence and remaining target

The framework-level observation causes a real algorithm change. The source
and decoder must retain:

- the complete gcd-free block list;
- exact exponent rows and finite occurrence capacities;
- legal cross-block candidate vectors and their integer magnitudes; and
- both full direct gcd screens before any self-inverse filter.

The seed list cannot be reduced only to its old square-class kernel. The
\(N=65\) witness proves that pair construction can create a useful root when
the old two-row decoder has no dependency. The final gcd remains simple, but
the source operation is now a search over structured multi-block states.

For an all-input factoring theorem, first use polynomial-time primality,
even-input, and perfect-power handling. Prime inputs are reported as prime.
Even inputs split by 2. Perfect powers reduce recursively to their integer
base. The remaining target is an odd composite that is not a perfect power.

There are then two different research goals.

1. **Full F62 target.** Produce a legal direct gcd separator \(v\) for which
   one of \(D_-(v),D_+(v)\) is proper.
2. **Self-inverse lattice subtarget.** Produce a legal bounded \(v\) with
   \(2v\in\Lambda_N\) and \(\Phi_N(v)\notin\{1,-1\}\).

The second target is sufficient but not necessary for the first. Odd prime
powers have no non-global square root of one, which is why perfect-power
preprocessing is required before claiming an all-input square-root route.

A polynomial candidate count is not enough. The source theorem must bound by
\(\operatorname{poly}(\log N)\):

- the number of seed occurrences \(m\) and block types \(s\);
- the total encoding of all relations, blocks, exponent rows, and occurrence
  capacities;
- the number and encoded size of every candidate exponent vector;
- the total number of adaptive rounds; and
- the number of random bits, when the source is randomized; and
- all refinement, multiplication, modular, and gcd work.

It must then prove deterministic success or inverse-polynomial success with a
Las Vegas verification rule on every remaining input. A route that first
recovers the full lattice has not avoided order finding. Constant-arity claims
do not follow from the odd-\(t\) family. A genuinely new selector must exploit
the finite relation boxes and integer magnitudes without confusing the full
direct screen with the narrower 2-torsion problem.
