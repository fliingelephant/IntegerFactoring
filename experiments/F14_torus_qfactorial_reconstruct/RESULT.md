# F14 torus q-factorial: independent reconstruction

**Approach-family ID:** `F14_torus_qfactorial_reconstruct`.

**Verdict:** every claim in the supplied corrected statement is valid with
the stated scope.  The product \(S_m\) has the same zero set as \(P_M\) in
each prime field, but it is not a gcd-preserving replacement over arbitrary
composite moduli.  Products made only from positive powers of
\(1-a^L\) need at least \(\lceil M/2\rceil\) distinct exponents.  The exact
q-Pochhammer addition law yields a two-child recursion with \(M\) leaves, but
this is a cost statement only about that literal evaluator.  The formal
support, cyclotomic-degree, and quotient-set bounds do not establish any
arithmetic-circuit lower bound.  In particular, the P20 evaluator remains
open.

This reconstruction used only the bare statement supplied for this task.  It
did not inspect either other F14 experiment, any canonical file, or any
candidate proof.

## 1. Prime zero sets agree, composite gcds need not

Let \(M=m-1\) and

\[
P_M(a)=\prod_{d=1}^{M}(1-a^d),\qquad
S_m(a)=\prod_{d=1}^{M}(1-a^d)^{m-d}.
\]

For every prime \(\ell\), a product in \(\mathbf F_\ell\) is zero exactly
when one of its factors is zero.  Every exponent \(m-d=M+1-d\) is positive,
so, for every residue \(a\),

\[
P_M(a)=0\pmod\ell
\iff \exists d\le M:\ a^d=1\pmod\ell
\iff S_m(a)=0\pmod\ell.                           \tag{1}
\]

No unit assumption is needed for (1).  If \(a\) is a unit, the middle
condition is equivalent to \(\operatorname{ord}_\ell(a)\le M\) with the
additional requirement that the order divide at least one integer through
\(M\), which is automatic because the order itself is in that range.

Over the integers,

\[
S_m(a)=P_M(a)
       \prod_{d=1}^{M}(1-a^d)^{M-d}.              \tag{2}
\]

Thus \(P_M(a)\mid S_m(a)\), and for every positive integer \(N\),

\[
\boxed{\gcd(P_M(a),N)\mid\gcd(S_m(a),N)}.         \tag{3}
\]

Equality can fail because (2) raises prime-adic valuations.  For

\[
N=875=5^3\cdot7,\qquad a=631,\qquad m=3,
\]

R01 obtained

\[
P_2(a)=250840800,qquad S_3(a)=-158029704000.
\]

Their relevant valuations are

\[
(v_5(P_2),v_7(P_2))=(2,2),\qquad
(v_5(S_3),v_7(S_3))=(3,3),
\]

and hence

\[
\gcd(P_2(a),875)=175,qquad
\gcd(S_3(a),875)=875.                             \tag{4}
\]

The weighted product therefore turns a proper divisor into the trivial gcd,
despite having exactly the same zero/nonzero behavior modulo both distinct
prime factors.

## 2. Every order has a finite-field witness

The needed witness fact does not require a prime in an arithmetic
progression.

**Lemma.** For every integer \(r\ge1\), some finite field contains a unit of
order exactly \(r\).

Choose a prime \(\ell\nmid r\).  Euler's theorem gives

\[
r\mid \ell^{\varphi(r)}-1.
\]

The multiplicative group of
\(\mathbf F_{\ell^{\varphi(r)}}\) is cyclic of that order, so it contains an
element of order \(r\).  The case \(r=1\) is immediate.  R01 additionally
constructed explicit prime-field witnesses for every \(r\le40\), but the
extension-field argument proves the statement for all \(r\).

## 3. Positive binomial products need all large exponents

Let

\[
F(a)=\prod_{h=1}^{H}(1-a^{L_h})^{w_h},
\qquad L_h,w_h\in\mathbf Z_{>0},                  \tag{5}
\]

and suppose that for every finite field and every unit \(a\),

\[
F(a)=0\iff\operatorname{ord}(a)\le M.            \tag{6}
\]

For a unit of order \(r\), positivity of the weights gives

\[
F(a)=0\iff \exists h:\ r\mid L_h.               \tag{7}
\]

Apply the witness lemma first with \(r=L_h\).  The corresponding factor in
(5) vanishes, so (6) forces

\[
L_h\le M\quad\text{for every }h.                 \tag{8}
\]

Now fix an integer \(t\) with \(M/2<t\le M\) and use a witness of order
\(t\).  Equations (6)--(7) give some \(L_h\) divisible by \(t\).  But (8)
and \(2t>M\) leave only one possible positive multiple:

\[
L_h=t.                                            \tag{9}
\]

Therefore every integer in \((M/2,M]\) must occur among the exponents, and

\[
\boxed{\#\{L_h:h\le H\}\ge
       M-\lfloor M/2\rfloor=\lceil M/2\rceil}.    \tag{10}
\]

This is a lower bound for the restricted representation (5), not for an
arbitrary arithmetic circuit.

### One-lcm compression has false positives

At \(M=4\), the proposed one-factor exponent is

\[
L=\operatorname{lcm}(1,2,3,4)=12.
\]

In \(\mathbf F_{13}\), the element \(a=2\) has order 12.  Consequently,

\[
1-a^L=0,
\]

although its order is greater than 4.  Direct evaluation gives

\[
P_4(2)=3\pmod {13},\qquad S_5(2)=7\pmod {13},     \tag{11}
\]

so the true products are both nonzero.  This is an exact false positive for
one-lcm compression.

## 4. Exact shifted q-Pochhammer addition laws

Define the shifted pair

\[
Q_n(X;Y)=\prod_{j=0}^{n-1}(1-YX^j),
\qquad
T_n(X;Y)=\prod_{j=0}^{n-1}(1-YX^j)^{n-j},         \tag{12}
\]

with empty products equal to 1.  The original polynomials are

\[
Q_n(X)=Q_n(X;X)=\prod_{d=1}^{n}(1-X^d),
\qquad
T_n(X)=T_n(X;X)=\prod_{d=1}^{n}(1-X^d)^{n+1-d}.
\]

In particular, \(P_M(a)=Q_M(a)\) and \(S_m(a)=T_M(a)\).

Splitting \(u+v=n\) in (12) gives the exact laws

\[
\boxed{Q_{u+v}(X;Y)
=Q_u(X;Y)Q_v(X;YX^u)},                            \tag{13}
\]

\[
\boxed{T_{u+v}(X;Y)
=T_u(X;Y)Q_u(X;Y)^vT_v(X;YX^u)}.                 \tag{14}
\]

For (14), the first \(u\) factors have exponent

\[
u+v-j=(u-j)+v,
\]

which supplies \(T_uQ_u^v\); the remaining \(v\) factors have exactly the
weights in the shifted \(T_v\).  This proves both identities without any
specialization assumption.

Equivalently, with

\[
Q_{s,n}(X)=\prod_{j=1}^{n}(1-X^{s+j}),
\quad
T_{s,n}(X)=\prod_{j=1}^{n}(1-X^{s+j})^{n+1-j},
\]

the laws are

\[
Q_{s,u+v}=Q_{s,u}Q_{s+u,v},
\qquad
T_{s,u+v}=T_{s,u}Q_{s,u}^{v}T_{s+u,v}.           \tag{15}
\]

### Cost of the literal two-child evaluator

The evaluator directly induced by (13)--(14) recursively computes both
children

\[
(Y,u),\qquad(YX^u,v),
\]

then combines their returned \((Q,T)\) pairs.  Any recursion that continues
to length-one intervals is a full binary tree with exactly

\[
n\text{ leaves and }n-1\text{ internal nodes}.   \tag{16}
\]

For balanced splits, binary powering for \(X^u\) and \(Q_u^v\) costs
\(O(\log n)\) at a node of size \(n\).  Summed over the balanced tree, these
costs are \(O(n)\), while the \(n\) leaves give an \(\Omega(n)\) visit count.
Thus this modular-evaluation implementation has linear ring-operation cost.

This conclusion is deliberately narrow: (16) counts the calls made by this
specific two-child recursion.  It does not prove that every evaluator for
\(Q_n\) or \(T_n\) needs linear work, nor does it exclude sharing, a different
functional identity, or a succinct weighted circuit.

## 5. Formal and generic coefficient support

The formal exponent support of \(Q_n\) consists of subset sums of
\(1,2,\ldots,n\).  These fill every integer from 0 through

\[
D_Q=\sum_{d=1}^{n}d=\frac{n(n+1)}2.               \tag{17}
\]

Indeed, if \(1,\ldots,n-1\) fill \([0,D_{Q,n-1}]\), adjoining \(n\) adds the
overlapping interval \([n,D_{Q,n-1}+n]\).  Hence the formal support size is

\[
\boxed{D_Q+1=\frac{n(n+1)}2+1}.                  \tag{18}
\]

For \(T_n\), use the multiset in which \(d\) occurs \(n+1-d\) times.  Its
subset sums are also contiguous: after the copies of 1 are inserted, each
next weight \(d\le n\) is at most one plus the already reachable maximum, so
the reachable interval remains unbroken.  Its total is

\[
D_T=\sum_{d=1}^{n}d(n+1-d)
=\frac{n(n+1)(n+2)}6,                             \tag{19}
\]

and its formal support size is

\[
\boxed{D_T+1=\frac{n(n+1)(n+2)}6+1}.             \tag{20}
\]

These counts become genuine dense coefficient supports under a generic
deformation.  For example, set

\[
\widetilde Q_n=\prod_{d=1}^{n}(1-U_dX^d),
\qquad
\widetilde T_n=\prod_{d=1}^{n}(1-U_dX^d)^{n+1-d}.
\]

For each reachable exponent, distinct selection vectors give distinct
monomials in the independent \(U_d\).  Their binomial coefficients are
nonzero in characteristic zero, so the coefficient polynomial cannot
cancel.

The specialization \(U_d=1\) can cancel and need not be dense.  For example,

\[
Q_3(X)=1-X-X^2+X^4+X^5-X^6
\]

has zero \(X^3\) coefficient, and

\[
T_2(X)=1-2X+2X^3-X^4
\]

has zero \(X^2\) coefficient.  Therefore (18) and (20) are formal/generic
support statements, not lower bounds for arbitrary specializations,
representations, or evaluation circuits.

## 6. Cyclotomic weights and floor quotients

Up to their global signs, the cyclotomic factorizations are

\[
Q_M(X)=\prod_{t=1}^{M}\Phi_t(X)^{\lfloor M/t\rfloor},               \tag{21}
\]

and

\[
T_M(X)=\prod_{t=1}^{M}\Phi_t(X)^{W_t},
\quad
W_t=r_t(M+1)-\frac{t r_t(r_t+1)}2,
\quad r_t=\left\lfloor\frac Mt\right\rfloor.     \tag{22}
\]

The weights in (21) take many distinct values.  Let

\[
\mathcal V_M=\left\{\left\lfloor\frac Md\right\rfloor:1\le d\le M\right\},
\qquad s=\lfloor\sqrt M\rfloor.
\]

First, every \(k\in\{1,\ldots,s\}\) belongs to \(\mathcal V_M\).  Set
\(d=\lfloor M/k\rfloor\) and write \(M=kd+r\), where \(0\le r<k\).  Since
\(d\ge k\),

\[
\left\lfloor\frac Md\right\rfloor
=\left\lfloor k+\frac rd\right\rfloor=k.
\]

Second, the \(s\) values

\[
\left\lfloor M/1\right\rfloor,ldots,
\left\lfloor M/s\right\rfloor
\]

are distinct: for \(j<s\),

\[
\frac Mj-\frac M{j+1}=\frac{M}{j(j+1)}>1.
\]

They are all at least \(s\), so the two displayed sets intersect in at most
the value \(s\).  Consequently,

\[
\boxed{|\mathcal V_M|\ge2\lfloor\sqrt M\rfloor-1}.                \tag{23}
\]

The nonconstant weights in (21)--(22), even together with (23), do not
refute a succinct weighted circuit.  Exponent weights can be generated by
repeated squaring, and these formulas give no lower bound against sharing or
other algebraic structure.

## 7. Root-of-unity degree bound

Let \(f\) be a nonzero univariate polynomial over a characteristic-zero
field, evaluated in an algebraic closure, and suppose it vanishes at every
root of unity whose exact order is at most \(M\).  There are exactly
\(\varphi(t)\) roots of exact order \(t\), and exact-order classes are
disjoint.  A nonzero polynomial has at most its degree many distinct roots,
so

\[
\deg f\ge\sum_{t=1}^{M}\varphi(t).                \tag{24}
\]

An elementary estimate is enough for the requested explicit bound.  If
\(p_1<\cdots<p_k\) are the distinct prime factors of \(n\), then

\[
\frac n{\varphi(n)}
=\prod_{i=1}^{k}\frac{p_i}{p_i-1}
\le\prod_{i=1}^{k}\frac{i+1}{i}
=k+1
\le1+\log_2 n.                                   \tag{25}
\]

Here \(p_i\ge i+1\), and \(n\ge2^k\).  The case \(n=1\) is immediate.
Therefore

\[
\sum_{t=1}^{M}\varphi(t)
\ge\frac{1}{1+\log_2 M}\sum_{t=1}^{M}t
=\frac{M(M+1)}{2(1+\log_2 M)}.
\]

This is stronger than the requested inequality, and in particular

\[
\boxed{\deg f\ge\sum_{t=1}^{M}\varphi(t)
\ge\frac{M^2}{4(1+\log_2 M)}}.                   \tag{26}
\]

Nonzero is essential.  Just as importantly, degree is not arithmetic-circuit
size: repeated squaring computes \(X^{2^k}-1\) with a circuit of size
\(O(k)\).  Thus (26) is not an arbitrary arithmetic-circuit lower bound.

## 8. Exact finite verification

The immutable R01 source independently checked:

- 3,280 prime-field zero-set comparisons for all residues, primes through
  47, and lengths through 10;
- 55,614 sampled composite gcd divisibility instances;
- the exact counterexample (4) and false positive (11);
- explicit prime-field witnesses for every order through 40;
- 200 exact integer-polynomial checks of (13)--(15);
- both formal support intervals through \(n=20\), including the two
  specialization cancellations above;
- (23) for every \(M\le2000\) and the totient bound through \(M=5000\);
- the exact \(n\)-leaf, \(n-1\)-internal-node counts through a 1,024-leaf
  balanced evaluator tree.

All checks passed.  These computations corroborate the proofs; none is used
as a substitute for an all-\(M\) argument.

## 9. What remains open

The reconstruction establishes lower bounds only for:

- the number of distinct exponents in the restricted positive product (5);
- the leaves visited by the literal two-child evaluator from (13)--(14);
- formal/generic dense coefficient materialization; and
- the degree of a nonzero characteristic-zero root-of-unity annihilator.

It establishes no lower bound for arbitrary arithmetic circuits or arbitrary
specialized evaluators.  Nonconstant cyclotomic weights alone do not refute
succinct weighted circuits.  The P20 evaluator therefore remains open.
