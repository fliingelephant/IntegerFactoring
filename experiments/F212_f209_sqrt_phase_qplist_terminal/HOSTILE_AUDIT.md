# F212 self-hostile audit

## Verdict

**FAIL.**

The elementary square-root phase theorems, parity handling, exact
\(K\)-divisor identity, and Coppersmith exponent calculation survive. The
frozen terminal theorem nevertheless has a fatal complexity-quantifier gap:
it bounds the number and bit lengths of the listed residues but never assumes
that the procedure producing that list runs in QP time, nor does it formally
take the list as granted auxiliary input. Its proof accounts only for
postprocessing. Therefore the stated conclusion that \(N\) can be factored
in numerical QP time does not follow from the frozen premises.

This is a self-hostile audit by the author of F212, not an independent audit.
A separate statement-only reconstruction is still required after repair.

## 1. Authentication

Before reading the packet, the four MANIFEST content hashes were recomputed.
All matched:

- STATEMENT.md:
  f02027e683c21e7ca83082ac62d57b3d8df87e99f9e1ac0344ca98c6cd0a4400
- PROOF.md:
  bd91b0b05203aa4814e32970e3619def8066afd5081d9727e6c88ae1b392b878
- SELF_AUDIT.md:
  69973aa7217e5a798d8944c49a2ad86f9a62ba34b665d4aa43588804e397065c
- PROVENANCE.md:
  70a6165e013b95824428d8dbb2d860ef9df881e98ad6a4b324b9e23de6cb96bd

The MANIFEST hash was

29efbe5eda6fda4bb7c6cc96079d02e51e055ff8091a2caaf4b35574fc083f08.

## 2. Fatal finding F212-H1: list size is not list-generation time

Theorem 4 assumes only that

> a public procedure outputs at most \(Q(n)\) pairs

with the listed modulus, residue, and correctness properties. No running-time
bound is imposed on that procedure. The list is also not explicitly declared
to be a granted auxiliary input to the factoring postprocessor.

The proof establishes the following valid statement:

> Given an explicit list of at most \(Q(n)\) such pairs, the list can be
> postprocessed deterministically in numerical QP time.

It does not establish a uniform QP algorithm from bare \(N\), because an
unspecified list-producing procedure may take arbitrary time. A short output
does not imply a short computation producing that output.

Either of these repairs is sufficient:

1. **Granted-list formulation.** Replace the conclusion by a QP
   postprocessing theorem whose input is \(N\) together with the explicit
   list.
2. **Uniform factoring formulation.** Require that a deterministic numerical
   QP-time public procedure, on input \(N\), produces the list. Then compose
   it with the proved QP postprocessor.

The proof's final complexity paragraph counts only the \(Q(n)\) Coppersmith
and gcd calls, so it does not silently supply the missing generation bound.
This defect affects the headline positive terminal and forces FAIL for the
frozen statement.

## 3. Uniform full-torsor theorem: passes

Let \(t=\sqrt N\) and \(s=\operatorname{lcm}(2,m)\). The frozen proof uses

\[
B-L>\left(1-\frac1{\sqrt2}\right)t-2,
\qquad
U-(B+1)>(\sqrt2-1)t-3.
\]

For \(t\geq32\) and \(s\leq t/8\), both spans are at least \(s-1\).
Therefore every compatible step-\(s\) class meets both intervals.

For the lower endpoint product,

\[
P_x^-Q_x^-
<
\left(\left(\frac1{\sqrt2}+\frac18\right)t+1\right)
\left(\frac98t+1\right).
\]

At \(t=32\), \(t^2\) minus the right side is

\[
839-592\sqrt2>0,
\]

because \(839^2-2\cdot592^2=2993\). The difference has positive derivative
for \(t\geq32\): its quadratic coefficient exceeds \(1/16\), and the
magnitude of its linear coefficient is less than \(2\).

For the upper endpoint product,

\[
P_x^+Q_x^+
>
\left(\frac78t-1\right)
\left(\left(\sqrt2-\frac18\right)t-2\right).
\]

The quadratic coefficient exceeds \(1+1/8\), while the magnitude of the
linear coefficient is less than \(25/8\). Hence its excess over \(t^2\) is
greater than

\[
\frac{t^2-25t}{8}+2>0
\]

for \(t\geq32\). Thus all unit classes pass the product bracket as claimed.

The asymptotic implication is also correct:
\(s/\sqrt N\to0\) eventually enters the explicit \(1/8\) range, and
\(m=o(\sqrt N)\) implies this because \(s\leq2m\).

The elementary bound

\[
\varphi(m)\geq\sqrt{m/2}
\]

is valid. Every odd prime-power factor contributes at least one to
\(\varphi(m)^2/m\); only a single factor \(2\) can be lost at the
\(2^1\)-component.

## 4. Odd parity and progression compatibility: passes

For even \(m\), every unit residue is odd, and its odd lifts have step \(m\).
For odd \(m\), consecutive lifts alternate parity, so the odd lifts form one
class modulo \(2m\). Thus the common step is exactly

\[
s=\operatorname{lcm}(2,m).
\]

An inclusive integer interval of span at least \(s-1\) contains one member of
each compatible class. Since \(\gcd(m,N)=1\), both \(x\) and
\(Nx^{-1}\bmod m\) are units.

The F207 coordinate change is sound. From \(R^2\equiv N\pmod m\) and
\(\gcd(R,m)=1\),

\[
N(Ru)^{-1}\equiv Ru^{-1}\pmod m.
\]

Therefore multiplication by \(R\) bijects the \(u\)-frontier and the frozen
\(x\)-frontier.

There is one nonfatal definitional edge: the setup permits \(m=1\), for
which notation for the unit group of the zero ring and modular inversion
depends on convention. F209's nontrivial component stages have \(m>1\).
A repair should state \(m\geq2\), or declare the trivial \(m=1\) convention.

## 5. Singleton criterion: passes

Two odd lifts of the same residue differ by at least \(s\). Hence

\[
s>\max\{B-L,U-(B+1)\}
\]

makes each nonempty progression a singleton. The endpoint bracket then reads

\[
XY\leq N\leq XY,
\]

which is exactly \(XY=N\).

Conversely, if \(X\mid N\) and \(X\in P,\ N/X\in Q\), then
\(\gcd(X,m)=1\), because \(\gcd(m,N)=1\), and the two singleton residues
satisfy the modular inverse relation. The set identity is exact.

Balance places \(p\) in \(P\) and \(q\) in \(Q\):

\[
p^2>N/2,\qquad p^2<N,\qquad q^2>N,\qquad q^2<2N.
\]

No other divisor of the promised semiprime lies in the ordered intervals.
The super-square-root corollary follows from \(s\geq m\) and
\(W_P,W_Q=O(\sqrt N)\).

## 6. Exact \(K\)-divisor spike: passes

For \(K=(N-1)/2\),

\[
\gcd(K,N)=1,\qquad N\equiv1\pmod K.
\]

For every promised input \(N\geq15\),

\[
K>\sqrt{2N-1}\geq U,
\]

because the squared difference is \(N^2-10N+5>0\). Thus the interval
representatives modulo \(K\) are singleton.

For \(X\in P,\ Y\in Q\), the proof correctly establishes

\[
N-K<XY<N+K.
\]

The lower inequality reduces to
\(N^2-4N-1>0\), and the upper inequality to
\((N-1)^2>0\). Therefore congruence modulo \(K\) forces \(XY=N\).

The floor jump

\[
\left\lfloor\frac NX\right\rfloor
-\left\lfloor\frac{N-1}{X}\right\rfloor
=\mathbf1_{X\mid N}
\]

is exact. If \(L\leq X\leq B\) divides \(N\), then
\(X^2\geq(N+1)/2\), so its complementary divisor satisfies

\[
(N/X)^2\leq\frac{2N^2}{N+1}\leq2N-1
\]

and lies in \(Q\). This proves the exact frontier-count identity.

The named ordinary quotient-grouping boundary is also correct:
for \(L\leq X<B\),

\[
X(X+1)\leq B(B-1)<B^2\leq N,
\]

so \(\lfloor N/X\rfloor\) strictly decreases at every step. The packet
properly disclaims a lower bound against other floor algorithms.

## 7. Coppersmith exponent and residue normalization: arithmetic passes

The packet explicitly imports the standard monic univariate theorem modulo
an unknown divisor \(D\geq N^\beta\), with degree-one root range
\(N^{\beta^2-\eta}\). This is the same scoped imported theorem previously
audited in F41; F212 does not rely on a general bivariate heuristic.

For a correct residue \(r=p\bmod m\),

\[
p=r+mt,\qquad
0\leq t<N^{1/4-\varepsilon}.
\]

With

\[
\beta=\frac12-\frac\varepsilon4,
\]

balance gives \(p>\sqrt{N/2}\geq N^\beta\) for sufficiently large \(N\), and

\[
\beta^2-\left(\frac14-\frac\varepsilon2\right)
=\frac\varepsilon4+\frac{\varepsilon^2}{16}>0.
\]

One fixed theorem margin therefore contains the root. For \(q\), the bound

\[
q<\sqrt{2N}
\]

adds only a constant, which is absorbed by the same
\(\varepsilon/2\) exponent slack.

The monic normalization is correct. With

\[
c\equiv r m^{-1}\pmod N,\qquad f(T)=T+c,
\]

one has

\[
mf(t)\equiv mt+r\equiv0\pmod p
\]

or modulo \(q\). Since \(m\) is a unit modulo the hidden divisor,
\(f(t)\) vanishes there. A gcd of \(r+mt\) with \(N\) verifies and returns
the factor.

Thus the mathematically valid terminal is:

\[
\boxed{\text{given a correct QP-size list, QP postprocessing factors }N.}
\]

Only the missing list-generation/input quantifier invalidates the frozen
headline theorem.

## 8. Named-boundary scope: passes

The Fourier expansion is an exact identity for the separable interval
indicators. The packet explicitly notes that the endpoint product predicate
is additional and nonseparable. It claims neither an exact Kloosterman
lower bound nor an arithmetic-circuit lower bound.

The CRT-order discussion is confined to F209's literal explicit expansion
and full interval scan. It explicitly leaves compressed states, adaptive
implicit algorithms, exact counters, and nonlinear decoders open. No
unconditional lower bound is stated.

## 9. Required disposition

Do not promote the frozen F212 packet.

Prepare a repaired version that changes Theorem 4 and its proof in one of the
two ways listed in Finding F212-H1. Rehash the repaired packet, then obtain a
fresh hostile audit and a separate statement-only blind reconstruction.
