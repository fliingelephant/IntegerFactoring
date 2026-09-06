# F212 V2 blind reconstruction

## Verdict

**STRICT PASS within the declared scope.** I reconstructed every displayed
claim from the statement and found no false identity, endpoint failure,
threshold error, hidden enumeration claim, or Coppersmith exponent gap.
The distinction between a granted explicit list and an algorithm that
generates the list is mathematically and computationally necessary, and V2
states it correctly.

F212 V2 is not the all-input factoring result required by PROMPT.md. It is a
boundary theorem and a conditional terminal for balanced distinct odd
semiprimes. It neither constructs the promised list generator nor handles
general inputs, and it does not claim to.

## Blind source boundary and hash

Before reading V2_STATEMENT.md, I computed its SHA-256:

69e0ca4f9cefb0ed41cbeaff25aa48b184d4039dffce11257baf787d8866dd99.

It matches the supplied expected hash exactly. I then read only the
workspace PROMPT.md and
experiments/F212_f209_sqrt_phase_qplist_terminal/V2_STATEMENT.md. I did not
inspect any proof, audit, manifest, provenance file, durable ledger, or
prior reconstruction.

## 1. Exact factor intervals

The balance promise gives

\[
p^2<pq=N<2p^2.
\]

Since \(N\) is odd,

\[
\left\lfloor\frac N2\right\rfloor=\frac{N-1}{2}<p^2.
\]

Therefore

\[
p\geq
\left\lfloor\sqrt{\left\lfloor N/2\right\rfloor}\right\rfloor+1=L.
\]

Also \(p<\sqrt N\), so \(p\leq B\). Thus \(p\in P\).

Similarly, \(q>\sqrt N\) gives \(q\geq B+1\). Balance also gives

\[
q^2<2pq=2N.
\]

Because \(q^2\) is an integer, \(q^2\leq2N-1\), and hence \(q\leq U\).
Thus \(q\in Q\). Both primes are odd, as required by the definitions.

For a unit \(z\bmod m\), the odd integers congruent to \(z\bmod m\) form
one residue class modulo

\[
s=\operatorname{lcm}(2,m).
\tag{R1}
\]

Indeed, if \(m\) is even, every unit residue is odd and \(s=m\). If \(m\)
is odd, the two lifts modulo \(2m\) have opposite parity and exactly one is
odd, so \(s=2m\). In particular,

\[
m\leq s\leq2m.
\tag{R2}
\]

Because \(N\) and \(x\) are units modulo \(m\),
\(y_x=Nx^{-1}\) is also a unit. Multiplication by any public unit
\(R\bmod m\) is a bijection of \(U(m)\), which verifies the stated
coordinate change \(x=Ru\) independently of any frontier enumeration.

## 2. Uniform full-torsor threshold

Write

\[
R_0=\sqrt N.
\]

Under \(N\geq1024\), one has \(R_0\geq32\). Assume
\(s\leq R_0/8\).

First, every relevant progression meets both intervals. Since

\[
B>R_0-1,\qquad
L\leq\frac{R_0}{\sqrt2}+1,
\]

we have

\[
B-s>\frac{7R_0}{8}-1>L.
\tag{R3}
\]

For the last inequality, it is enough to use
\(1/\sqrt2<3/4\) and \(R_0\geq32\).

Also,

\[
U>\sqrt{2N-1}-1>\sqrt2\,R_0-2.
\]

Therefore

\[
U-s>\left(\sqrt2-\frac18\right)R_0-2>B+1.
\tag{R4}
\]

Here one may use \(\sqrt2>11/8\), \(B+1\leq R_0+1\), and
\(R_0\geq32\). For any residue class modulo \(s\), its last member at most
an upper endpoint lies strictly more than that endpoint minus \(s\).
Equations (R3) and (R4) therefore put such a member inside each interval.

For every \(x\in U(m)\), the first progression members satisfy

\[
P_x^-<L+s,\qquad Q_x^-<B+1+s.
\]

Using \(1/R_0\leq1/32\),

\[
\begin{aligned}
P_x^-Q_x^-
&<(L+s)(B+1+s)\\
&\leq R_0^2
\left(\frac1{\sqrt2}+\frac5{32}\right)\frac{37}{32}\\
&<R_0^2=N.
\end{aligned}
\tag{R5}
\]

The last constant inequality is exact. It is equivalent to

\[
\frac1{\sqrt2}<\frac{839}{1184},
\]

which follows by squaring because
\(2\cdot839^2>1184^2\).

The last progression members satisfy

\[
P_x^+>B-s,\qquad Q_x^+>U-s.
\]

Consequently,

\[
\begin{aligned}
P_x^+Q_x^+
&>(B-s)(U-s)\\
&>R_0^2\frac{27}{32}
\left(\sqrt2-\frac3{16}\right)\\
&>R_0^2=N.
\end{aligned}
\tag{R6}
\]

The last inequality is equivalent to

\[
\sqrt2>\frac{593}{432},
\]

which follows by squaring because
\(593^2<2\cdot432^2\).

Thus both progressions are nonempty and their endpoint products straddle
\(N\), uniformly for every \(x\in U(m)\). Hence

\[
\mathcal F_N(m)=U(m),\qquad
|\mathcal F_N(m)|=\varphi(m).
\tag{R7}
\]

If \(s(m_i)/\sqrt{N_i}\to0\), then eventually \(N_i\geq1024\) and
\(s(m_i)\leq\sqrt{N_i}/8\), proving the sequential statement. Equation
(R2) shows that \(m=o(\sqrt N)\) is sufficient.

The elementary lower bound on the torsor size is also correct. If
\(m=\prod_\ell\ell^{a_\ell}\), then

\[
\frac{\varphi(m)^2}{m}
=\prod_{\ell^{a_\ell}\parallel m}
\ell^{a_\ell-2}(\ell-1)^2.
\]

The factor for \(2^1\) is \(1/2\); every other prime-power factor is at
least one. Therefore

\[
\varphi(m)\geq\sqrt{m/2}.
\tag{R8}
\]

If \(m=N^{\alpha+o(1)}\), this is
\(N^{\alpha/2+o(1)}\). For fixed \(0<\alpha<1/2\), (R2) also puts the
modulus in the full-torsor regime. Thus an explicit state list is already
of fixed-power size there.

## 3. Singleton-progression boundary

An arithmetic progression of step \(s\) cannot have two members in a
closed interval of span less than \(s\). Therefore

\[
s>\max\{W_P,W_Q\}
\tag{R9}
\]

makes every nonempty progression in \(P\) or \(Q\) a singleton.

Let \(x\) be in the frontier, and call the unique members \(X\in P\) and
\(Y\in Q\). Both endpoint products are then the same number \(XY\), so the
frontier inequality becomes

\[
XY\leq N\leq XY.
\]

Hence \(XY=N\). Also \(x\equiv X\bmod m\), so

\[
x=X\bmod m,\qquad X\mid N,\qquad N/X=Y\in Q.
\]

Conversely, take \(X\in P\) with \(X\mid N\) and \(Y=N/X\in Q\). Since
\(\gcd(m,N)=1\), \(X\) is a unit modulo \(m\). Put \(x=X\bmod m\). Then

\[
y_x=Nx^{-1}\equiv Y\pmod m.
\]

The two progressions are the required singletons and their common endpoint
product is \(N\), so \(x\) belongs to the frontier. This proves

\[
\mathcal F_N(m)
=\{X\bmod m:X\in P,\ N/X\in Q,\ X\mid N\}.
\tag{R10}
\]

The only divisors of the promised semiprime are \(1,p,q,N\). Section 1
places \(p\) in \(P\) and \(q\) in \(Q\), while the interval ordering
excludes the other three possibilities for \(X\). Thus (R10) is exactly
the ordered branch \((p,q)\).

The widths satisfy

\[
W_P<\sqrt N,\qquad W_Q<\sqrt{2N}.
\]

Since \(s\geq m\), the condition \(m/\sqrt N\to\infty\) implies (R9) for
all sufficiently large inputs. Together with the full-torsor result for
\(m=o(\sqrt N)\), this leaves only \(m=\Theta(\sqrt N)\) unresolved for
this exact endpoint geometry. It says nothing about hardness at that
scale.

## 4. The modulus \(K=(N-1)/2\) and the divisor spike

Let

\[
K=\frac{N-1}{2}.
\]

Then

\[
\gcd(K,N)=\gcd(K,N-2K)=1.
\tag{R11}
\]

For \(X\in P\), the definition of \(L\) gives \(X^2>K\). For \(Y\in Q\),
\(Y^2>N\). Hence

\[
XY>\sqrt{KN}.
\]

For every promised input \(N\geq15\),

\[
\sqrt{KN}>\frac{N+1}{2}=N-K,
\tag{R12}
\]

because, after squaring, the difference is
\((N^2-4N-1)/4>0\).

At the other endpoint,

\[
X<\sqrt N,\qquad Y\leq\sqrt{2N-1},
\]

so

\[
XY<\sqrt{N(2N-1)}
<\frac{3N-1}{2}=N+K.
\tag{R13}
\]

The squared difference in the last comparison is
\((N-1)^2/4>0\). Thus

\[
N-K<XY<N+K.
\]

If \(XY\equiv N\pmod K\), the difference \(XY-N\) is a multiple of \(K\)
with absolute value less than \(K\), and must be zero. The converse is
immediate. Therefore

\[
XY\equiv N\pmod K\iff XY=N.
\tag{R14}
\]

The progressions modulo \(K\) are singletons on both intervals. Indeed,
\(s(K)\geq K\), and for \(N\geq15\),

\[
K>\sqrt N>W_P,\qquad
K>\sqrt{2N}>W_Q.
\tag{R15}
\]

Both inequalities follow by squaring; their relevant polynomials are
\(N^2-6N+1\) and \(N^2-10N+1\), respectively, and are positive at and
above \(N=15\).

It follows either from (R10) or directly from (R14) and singleton
progressions that the frontier counts divisors \(X\) in \([L,B]\). For any
positive integer \(X\),

\[
\left\lfloor\frac NX\right\rfloor
-\left\lfloor\frac{N-1}{X}\right\rfloor
=\mathbf1_{X\mid N}.
\tag{R16}
\]

Although the displayed sum includes even \(X\), every even summand is zero
because \(N\) is odd. Also, if \(X\in[L,B]\) divides \(N\), then
\(Y=N/X\) automatically lies in \(Q\): \(X^2>N/2\) gives
\(Y^2<2N\), while \(X^2<N\) gives \(Y^2>N\). Therefore

\[
|\mathcal F_N(K)|
=\sum_{X=L}^{B}
\left(
\left\lfloor\frac NX\right\rfloor
-\left\lfloor\frac{N-1}{X}\right\rfloor
\right).
\tag{R17}
\]

Only \(p\) divides \(N\) in this interval, so the value is one.

The strict quotient claim also holds. For \(L\leq X<B\),

\[
X(X+1)\leq(B-1)B<N.
\]

Consequently,

\[
\frac NX-\frac N{X+1}
=\frac{N}{X(X+1)}>1,
\]

which implies

\[
\left\lfloor\frac NX\right\rfloor
>
\left\lfloor\frac N{X+1}\right\rfloor.
\tag{R18}
\]

The shell contains

\[
B-L+1=
\left(1-\frac1{\sqrt2}\right)\sqrt N+O(1)
=\Theta(\sqrt N)
\]

indices, and every adjacent quotient differs. Thus ordinary
equal-quotient grouping has \(\Theta(\sqrt N)\) blocks here. This is a
cost statement for that literal grouping, not an exact-floor lower bound.

## 5. Granted-list Coppersmith postprocessor

Fix the rational \(\varepsilon>0\). Suppose one list entry
\((m,r)\) satisfies

\[
d\equiv r\pmod m
\]

for \(d=p\) or \(d=q\). Since \(0\leq r<m\), write

\[
d=r+mk,\qquad k\geq0.
\tag{R19}
\]

Balance gives \(d<\sqrt{2N}\), while
\(m\geq N^{1/4+\varepsilon}\). Hence

\[
k<\sqrt2\,N^{1/4-\varepsilon}.
\tag{R20}
\]

Because \(\gcd(m,N)=1\), compute \(\mu=m^{-1}\bmod N\) and form the monic
linear polynomial

\[
f(Z)=Z+r\mu\pmod N.
\tag{R21}
\]

Equation (R19) makes \(f(k)\equiv0\pmod d\).

The standard unknown-divisor form of univariate Coppersmith says the
following. For fixed \(\beta>0\), fixed slack \(\gamma>0\), and a monic
degree-one polynomial modulo \(N\), all integer roots \(z\) with

\[
f(z)\equiv0\pmod d,\qquad
d\geq N^\beta,\qquad
|z|\leq N^{\beta^2-\gamma}
\tag{R22}
\]

can be found in deterministic polynomial bit complexity in \(\log N\).

There is enough fixed slack to apply (R22). Put

\[
\varepsilon_0=\min\{\varepsilon,1/8\},\qquad
\beta=\frac12-\frac{\varepsilon_0}{4},\qquad
\gamma=\frac{\varepsilon_0}{4}.
\]

Both hidden primes exceed \(\sqrt{N/2}\), so for all sufficiently large
\(N\) they exceed \(N^\beta\). Moreover,

\[
\beta^2-\gamma
=\frac14-\frac{\varepsilon_0}{2}
+\frac{\varepsilon_0^2}{16}
>\frac14-\varepsilon_0.
\tag{R23}
\]

Equations (R20) and (R23) show that the constant \(\sqrt2\) is absorbed
for all sufficiently large \(N\), so \(k\) is inside the Coppersmith
radius. The finitely many smaller \(N\), with the cutoff depending only on
the fixed \(\varepsilon\), can be handled by deterministic trial division.
This changes only a fixed complexity constant.

Run this procedure for every list entry. For every root returned, compute

\[
\gcd(r+mk,N)
\]

and accept only a proper divisor. Thus every returned factor is verified,
and the one promised live entry guarantees success. The algorithm does not
need to identify that entry in advance.

It remains to count the actual input and runtime. The bit-length convention
gives \(N<2^n\). Since \(m_j\leq N^C\), both \(m_j\) and
\(0\leq r_j<m_j\) use \(O_C(n)\) bits. Self-delimiting field lengths add
only \(O(\log n)\) bits per field. Therefore a list of at most \(Q(n)\)
pairs has

\[
Q(n)\,O_C(n)
\tag{R24}
\]

bits. Multiplying a numerical quasipolynomial by a polynomial preserves
the numerical-QP class.

One can read the whole input and validate:

1. its self-delimiting syntax and entry count;
2. all bit-length and residue bounds;
3. the fixed rational power bounds on \(m_j\), by constant-degree integer
   exponent comparisons; and
4. every condition \(\gcd(m_j,N)=1\).

These checks cost polynomial time per entry. Modular inversion,
Coppersmith with fixed parameters, candidate multiplication, and gcd
verification also cost polynomial time per entry. With at most \(Q(n)\)
entries, the total deterministic bit complexity is numerical QP.

This proves only a postprocessor for an explicit auxiliary input whose
entire encoding is already bounded by (R24). A mathematical assertion that
some QP-size list exists does not include the time needed to discover,
construct, or serialize it.

If an F207/F209 branch is represented by \(u_j\bmod m_j\) and its public
coordinate map is \(x=R_ju_j\), computing

\[
r_j=R_ju_j\bmod m_j
\]

is polynomial in the entry length. Thus a granted QP-size live-branch list
above the modulus threshold is enough; the progression need not already be
a singleton.

## 6. Generator versus output-size accounting

Assume the public algorithm \(G\) has every property stated in Corollary
4B. Its output is an explicit list with the encoding bound (R24), contains
a live factor residue, and is produced in numerical-QP time without a
hidden-factor oracle. The postprocessor in Section 5 then has its full
promised input and also runs in numerical-QP time. The sum of two
numerical-QP bounds is numerical QP, so their composition factors \(N\).

In the bit model, the runtime of \(G\) already bounds how many output bits
it can write. The separate explicit list promise also supplies the precise
format and per-entry bounds required by the postprocessor. Consequently
construction, serialization, reading, validation, modular arithmetic,
Coppersmith, and final gcd checks are all charged.

Without \(G\), only the conditional auxiliary-input theorem remains.
Bounding the cardinality of an unknown output list does not bound the time
to generate it. V2 correctly makes no unconditional terminal claim.

## 7. Exact Fourier expansion and method boundaries

Choose the Fourier convention

\[
\widehat f(a)=\sum_{z\bmod m}
f(z)e^{-2\pi iaz/m},
\qquad
f(z)=\frac1m\sum_{a\bmod m}
\widehat f(a)e^{2\pi iaz/m},
\]

and the same convention for \(g\). Insert both inversion formulas into

\[
\sum_{x\in U(m)}f(x)g(Nx^{-1}).
\]

Interchanging the finite sums gives

\[
\frac1{m^2}\sum_{a,b\bmod m}
\widehat f(a)\widehat g(b)
\sum_{x\in U(m)}
e^{2\pi i(ax+bNx^{-1})/m}.
\]

The inner sum is exactly \(K_m(a,bN)\), proving the displayed
incomplete-Kloosterman expansion.

The formula has \(m^2\) displayed frequency pairs and is only an identity.
It supplies no compressed exact evaluation algorithm. An additive
square-root-scale estimate generally has uncertainty much larger than the
unit gap between counts zero and one, and the frontier also has the
nonseparable endpoint-product test. Therefore the standard expansion and
its approximate estimates do not by themselves certify the exact frontier
state.

Likewise, reordering CRT components does not alter either proved endpoint:

- in the small-step regime, every unit state survives; and
- in the singleton regime, survival is exact divisibility.

Changing enumeration order alone does not reduce the number of terms in a
literal frontier expansion or interval scan. This observation does not
exclude compressed states, adaptive exact counters, meet-in-the-middle
methods, or nonlinear decoders, and the statement does not extend it into
a lower bound.

## 8. Strict scope conclusion

The statement establishes:

1. a uniform full-unit-torsor theorem when
   \(s(m)\leq\sqrt N/8\) and \(N\geq1024\);
2. exact divisor isolation when the progression step exceeds both interval
   widths;
3. an unresolved transition restricted to \(m=\Theta(\sqrt N)\) for this
   declared geometry;
4. the exact \(K=(N-1)/2\) divisor-spike identity and the
   \(\Theta(\sqrt N)\) failure of literal equal-quotient compression on
   that shell;
5. deterministic numerical-QP factor recovery from a granted explicit
   QP-size list containing one residue modulo
   \(m\geq N^{1/4+\varepsilon}\); and
6. an end-to-end terminal only after a numerical-QP public generator for
   such a list is supplied.

It does not construct that generator, give a compressed critical-band
counter, prove a lower bound, or factor arbitrary inputs. The exact
remaining gap in V2_STATEMENT.md is therefore consistent with every
reconstructed theorem.
