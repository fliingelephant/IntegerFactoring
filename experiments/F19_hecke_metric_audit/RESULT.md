# F19 hostile audit: level-2 Eisenstein metric coefficient

**Audited candidate:** `experiments/F19_hecke_metric_kill/RESULT.md`

**Audit outcome:** the mathematical core survives, subject to explicit Hecke-
normalization, oracle-interface, and promise-class qualifications below.  This
is only the hostile-audit step.  The result is not verifier-backed until the
separate proof-blind reconstruction also succeeds.

**Computation:** none.  This is a proof-only audit, so there is no run manifest.

## 1. Verdict and necessary qualifications

No counterexample exists under the candidate's actual promise

\[
N=pq,\qquad p\ne q\text{ odd primes},
\]

and under the precise uniform interfaces reconstructed in Sections 6--8.  In
that scope, exact, one suitably chosen large-modulus, or explicit polynomial-
additive-error access recovers \(p+q\), after which a verified discriminant
calculation factors \(N\) without a gcd.  Balance is not used.

Four qualifications should be made explicit before promotion.

1. The Hecke eigenvalue is \(b_m\) for the standard **arithmetic** weight-two
   operator \(T_m\).  A unitary normalization rescales it (for example by
   \(m^{-1/2}\)).  A bare phrase such as "the Hecke eigenvalue" is therefore
   convention-dependent.
2. "Semiprime" must retain both `distinct` and `odd` wherever identity (4) is
   invoked.  If repeated primes are allowed, the smallest odd counterexample is
   \(N=9\): \(b_9=\sigma_1(9)=13\), whereas
   \(N+3+3+1=16\).  If even semiprimes are allowed, already
   \(b_6=b_3=4\ne 6+2+3+1\).
3. The approximation reduction needs an explicit, effectively available
   integer error bound \(K(n)=\operatorname{poly}(n)\) and an exactly encoded
   integer (or exactly roundable rational) output.  Merely asserting that some
   unspecified polynomial bounds an analytic error does not give a uniform
   scan.
4. "Factoring-equivalent" is proved only as a promise-problem statement for
   distinct odd semiprimes.  Nothing here factors arbitrary composites or
   proves a lower bound for coefficient evaluation.

The result is, exactly, the familiar semiprime divisor-sum reduction embedded
in a fixed modular form: for every odd \(m\), \(b_m=\sigma_1(m)\).  The modular
language supplies no additional separating information.  That does not make
the reduction false; it sharply limits its novelty and scope.

## 2. Transformation law and both cusps

Use the exact quasimodular transformation law

\[
E_2(\gamma z)=(cz+d)^2E_2(z)+\kappa c(cz+d),
\qquad \kappa=\frac{6}{\pi i},
\tag{A1}
\]

for

\[
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z).
\]

Let

\[
\gamma\in\Gamma_0(2),\qquad c=2c',\qquad
\gamma'=\begin{pmatrix}a&2b\\c'&d\end{pmatrix}.
\]

Then

\[
\det\gamma'=ad-2bc'=ad-bc=1,
\qquad \gamma'(2z)=2\gamma z.
\]

Applying (A1) to \(\gamma'\) at \(2z\) gives

\[
E_2(2\gamma z)
=(cz+d)^2E_2(2z)+\kappa c'(cz+d).
\]

After multiplication by \(2\), its anomalous term is
\(2\kappa c'(cz+d)=\kappa c(cz+d)\), exactly the anomaly in
\(E_2(\gamma z)\).  Hence

\[
F(\gamma z)=(cz+d)^2F(z),
\qquad F(z)=2E_2(2z)-E_2(z).
\]

The infinity cusp is holomorphic from the ordinary \(q\)-series.  The only
other cusp class of \(\Gamma_0(2)\) is \(0\), of width \(2\).  From (A1) with
\(S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\),

\[
E_2(-1/z)=z^2E_2(z)+\kappa z
\]

and, on replacing \(z\) by \(z/2\),

\[
E_2(-2/z)=\frac{z^2}{4}E_2(z/2)+\frac{\kappa z}{2}.
\]

Therefore the anomalies again cancel and

\[
(F|_2S)(z)=z^{-2}F(-1/z)
=\frac12E_2(z/2)-E_2(z).
\tag{A2}
\]

This is a power series in the correct local parameter
\(q^{1/2}=e^{\pi iz}\), with constant term \(-1/2\) and no negative powers.
Thus \(F\in M_2(\Gamma_0(2))\).  All signs and factors of \(2\) in the
candidate's transformation and cusp calculation are correct.

## 3. Fourier coefficients and powers of two

Direct subtraction, without any modular-form input, gives

\[
\begin{aligned}
F(z)
&=2\left(1-24\sum_{j\ge1}\sigma_1(j)q^{2j}\right)
 -\left(1-24\sum_{j\ge1}\sigma_1(j)q^j\right)\\
&=1+24\sum_{m\ge1}
 \left(\sigma_1(m)-2\mathbf 1_{2\mid m}\sigma_1(m/2)\right)q^m.
\end{aligned}
\]

Thus the sign is positive and the scale is \(24\).  Put

\[
b_m=\sigma_1(m)-2\mathbf 1_{2\mid m}\sigma_1(m/2).
\]

If \(m=2^a u\) with \(u\) odd, then for \(a\ge1\)

\[
\begin{aligned}
b_m
&=\left(2^{a+1}-1\right)\sigma_1(u)
 -2\left(2^a-1\right)\sigma_1(u)\\
&=\sigma_1(u).
\end{aligned}
\]

For \(a=0\), the same conclusion is immediate.  Hence, including \(m=1\),

\[
\boxed{b_m=\sigma_1(m_{\mathrm{odd}})},
\tag{A3}
\]

where \(m_{\mathrm{odd}}=m/2^{v_2(m)}\).  There is no missing power of two.
In particular \(b_1=b_2=b_4=1\), while \(b_3=4\), consistently with the
displayed expansion.

## 4. The Eisenstein line and Hecke normalization

The one-dimensional-line assertion is valid.  Indeed,

\[
[\mathrm{SL}_2(\mathbb Z):\Gamma_0(2)]=3,
\]

\(X_0(2)\) has two cusps, one elliptic orbit of order \(2\), and none of order
\(3\).  The genus formula gives

\[
g(X_0(2))=1+\frac3{12}-\frac14-\frac22=0.
\]

Weight-two cusp forms are holomorphic differentials, so \(S_2(\Gamma_0(2))=0\).
Weight-two modular forms correspond to differentials allowed simple poles at
the two cusps with residues summing to zero, and consequently

\[
\dim M_2(\Gamma_0(2))=g+2-1=1.
\]

Since \(F\ne0\), it spans this Eisenstein line.

For normalization, set

\[
f=F/24=\frac1{24}+\sum_{r\ge1}b_rq^r,
\]

so that the first positive Fourier coefficient is \(1\).  Define the standard
arithmetic weight-two Hecke operator, for odd \(m\), by

\[
[q^r](T_m f)=\sum_{d\mid(m,r)}d\, [q^{mr/d^2}]f,
\tag{A4}
\]

with the same formula at \(r=0\), where every \(d\mid m\) occurs.  Hecke
operators preserve the one-dimensional space, and comparison of the \(q^1\)
coefficient gives

\[
T_m f=b_m f.
\tag{A5}
\]

Equivalently, (A5) follows coefficientwise from multiplicativity and

\[
b_{\ell^{j+1}}=b_\ell b_{\ell^j}-\ell b_{\ell^{j-1}}
\]

for odd primes \(\ell\).  Thus the candidate has the correct eigenvalue under
(A4).  If instead one denotes \(m^{-1/2}T_m\) by the normalized Hecke operator,
its eigenvalue is \(b_m/\sqrt m\); the candidate's theorem must not be quoted
without its arithmetic normalization.

## 5. Semiprime identity and exact extraction

Now impose the full promise \(N=pq\) for distinct odd primes.  Since \(N\) is
odd, (A3) and multiplicativity give

\[
b_N=\sigma_1(pq)=(p+1)(q+1)=N+p+q+1.
\tag{A6}
\]

Set \(s=b_N-N-1\).  Then \(s=p+q\), and

\[
D=s^2-4N=(q-p)^2.
\tag{A7}
\]

Compute \(d=\lfloor\sqrt D\rfloor\), verify \(d^2=D\), verify that \(s\pm d\)
are even, and put

\[
x=(s-d)/2,\qquad y=(s+d)/2.
\]

The true pair is \(\{p,q\}\); checking \(1<x,y<N\) and \(xy=N\) makes every
returned answer correct.  This procedure uses subtraction, multiplication,
integer square root, parity tests, and exact division by \(2\).  It uses no gcd.

The distinct-prime promise is essential to (A6), not just cosmetic.  For
\(N=p^2\),

\[
b_N=1+p+p^2\ne(p+1)^2.
\]

At the smallest odd example \(N=9\), the candidate's proposed trace expression
would be \(13-9-1=3\), not \(6\), and its discriminant would be negative.  Thus
any wording that extends (A6) to repeated-prime semiprimes is false.

No balance bound occurs in (A6)--(A7).  The proof works equally when one prime
is much smaller than the other.

## 6. Exact bit lengths and the exact oracle interface

Let

\[
n=\lceil\log_2(N+1)\rceil,
\qquad M=2^n.
\]

Then \(N+1\le M\), so \(N<M\).  Also

\[
N+1-(p+q)=(p-1)(q-1)>0.
\]

Consequently

\[
0<s<M,
\qquad
0<b_N=N+s+1<2N+2\le2^{n+1}.
\tag{A8}
\]

Thus \(b_N\) has at most \(n+1\) bits.  The actual coefficient

\[
c_N=[q^N]F=24b_N
\]

has at most \(n+6\) bits.  During extraction, \(s^2<2^{2n}\), \(D<2^{2n}\),
and all other values have \(O(n)\) bits.  Standard exact integer square root and
the displayed arithmetic therefore have deterministic polynomial bit
complexity.

A precise exact interface is a single fixed uniform routine

\[
\mathcal E(m)\longmapsto b_m
\]

for odd binary \(m\), running in time polynomial in the bit length of \(m\).
Equivalently it may return \(c_m\), since exact division by \(24\) is available,
or it may return the arithmetic eigenvalue in (A5).  On a promised input \(N\),
one call to \(\mathcal E\) followed by (A7) factors \(N\).  The reduction itself
makes no factoring, divisor-enumeration, order-finding, or gcd call.

This says nothing about a routine taking time polynomial in the numerical
index \(m\), a nonuniform family with unbounded advice, or an oracle using an
unspecified Hecke normalization.

## 7. Supplied-modulus reconstruction

The modular claim also survives exactly.  Give a fixed uniform routine the two
binary inputs \(m,Q\), require it to return some integer representing

\[
c_m=24b_m\pmod Q,
\]

for every caller-supplied positive modulus \(Q\), and require running time
polynomial in

\[
\operatorname{bitlen}(m)+\operatorname{bitlen}(Q).
\]

For the promised \(N\), choose

\[
M=2^n,\qquad Q=24M=3\cdot2^{n+3}.
\tag{A9}
\]

The modulus \(Q\) has exactly \(n+5\) bits.  Reduce the oracle output to its
least residue \(r\in[0,Q)\).  Since both \(c_N\) and \(Q\) are divisible by
\(24\), every integer in this residue class, and in particular \(r\), is
divisible by \(24\).  Therefore

\[
u=r/24\in[0,M),\qquad u\equiv b_N\pmod M.
\tag{A10}
\]

Using (A6),

\[
u-(N+1)\equiv p+q\pmod M.
\]

By (A8), \(0<p+q<M\).  Hence the least nonnegative residue

\[
s=(u-(N+1))\bmod M
\tag{A11}
\]

is the ordinary integer \(p+q\).  Notice that the proof does **not** require
\(b_N<M\); only the smaller trace must lie below \(M\).  Equation (A7) then
finishes the split.

The factor \(24\), the least-residue convention, and the power \(2^n\) all
check.  The claim does require arbitrary caller-supplied moduli.  It does not
cover access only modulo one fixed small modulus, only for a restricted family
of moduli excluding (A9), or modulo values whose total reconstructible size is
substantially below \(n\) bits.

Again, balance is irrelevant.  Repeated-prime and even inputs are excluded by
the identity feeding (A11), not by the residue argument itself.

## 8. Additive approximation and rounding

Let \(K:\mathbb N\to\mathbb N\) be an explicit polynomially bounded function
known to the caller.  Suppose a fixed uniform routine, running in time
polynomial in \(n\), returns an integer \(h\) such that, on every promised \(N\),

\[
|h-b_N|\le K(n).
\tag{A12}
\]

Then \(\hat s=h-N-1\) obeys \(|\hat s-(p+q)|\le K(n)\).  Enumerate the at most
\(2K(n)+1\) integers \(t\in[\hat s-K(n),\hat s+K(n)]\).  For each one, reject
\(t^2-4N<0\), square-test the remainder, apply the parity test and formulas of
Section 5, and verify the product.  The true trace is examined, and the total
bit complexity is polynomial in \(n\).

For an integer approximation \(H\) to the unnormalized coefficient satisfying

\[
|H-24b_N|\le24K(n),
\]

take \(h\) to be a nearest integer to \(H/24\).  Because the endpoints
\(b_N\pm K(n)\) are integers, \(h\) still satisfies (A12).  If the stated error
bound is not integer-valued, replace it by its ceiling.  A floating-point value
without a proved exact rounding enclosure is not covered.

Nor does this argument cover a relative approximation, average-case accuracy,
an unknown polynomial error bound, or a success probability that has not been
converted to the required uniform deterministic/Las Vegas interface.

## 9. Converse computation and what "equivalent" means

Given a complete factorization of any \(m\), remove its power of two and write

\[
m_{\mathrm{odd}}=\prod_i\ell_i^{e_i}.
\]

Then

\[
b_m=\prod_i(1+\ell_i+\cdots+\ell_i^{e_i})
=\prod_i\frac{\ell_i^{e_i+1}-1}{\ell_i-1}.
\tag{A13}
\]

There are at most \(\lfloor\log_2m\rfloor\) prime factors counted with
multiplicity.  Repeated squaring computes each power in polynomial bit
complexity, and the final value has polynomial bit length; crudely,

\[
b_m=\sigma_1(m_{\mathrm{odd}})\le m^2.
\]

Thus a supplied complete factorization uniformly computes the exact
coefficient, its residues, and admissible approximations in polynomial time.
There is no hidden assumption in this converse beyond actually being given the
factorization.

Combining this with Sections 5--8 proves mutual polynomial-time reducibility
only on the distinct-odd-semiprime promise.  It does not prove that computing
\(b_m\) on arbitrary integers is equivalent to complete factoring on arbitrary
integers.  It also does not turn the candidate into a top-level factoring
algorithm, because the coefficient/eigenvalue routine is precisely the missing
primitive.

The terminal extraction genuinely avoids a gcd.  That statement concerns the
reduction after the oracle answer arrives.  It cannot certify that a proposed
implementation of the oracle avoids gcds or factoring internally.

## 10. Strongest corrected theorem and boundary

> **Corrected F19 theorem.**  Let
> \(F=2E_2(2z)-E_2(z)\in M_2(\Gamma_0(2))\), write
> \(F=1+24\sum_{m\ge1}b_mq^m\), and use the arithmetic Hecke normalization
> (A4).  Then \(b_m=\sigma_1(m_{\mathrm{odd}})\), and for odd \(m\), \(b_m\)
> is the \(T_m\)-eigenvalue of \(F/24\).  On every promised input
> \(N=pq\) with distinct odd primes, \(b_N=N+p+q+1\).  Therefore each of the
> following uniform worst-case polynomial-time interfaces yields a
> deterministic polynomial-time factorization of that promise class with one
> oracle call and no terminal gcd: exact \(b_N\) (or exact arithmetic Hecke
> eigenvalue); \(24b_N\bmod Q\) for arbitrary supplied \(O(n)\)-bit \(Q\); or
> an exactly encoded integer within a known additive \(K(n)=\operatorname{poly}(n)\)
> of \(b_N\).  Conversely, the factors compute all three outputs in polynomial
> bit complexity.

This is a clean reformulation of the \(\sigma_1(pq)\) trace identity.  It rules
out treating these exact high-information interfaces for this one Eisenstein
series as independent cheap primitives.  It gives no unconditional hardness
lower bound and says nothing adverse about cuspidal forms, character twists,
other levels or weights, fixed-small-modulus data, low-index Hecke data,
relative or coarse approximations, Brandt or modular-symbol invariants that do
not encode \(\sigma_1(N)\), or any other automorphic invariant whose binary-index
evaluation has a genuinely different information path.
