# F212 V2 fresh hostile audit

## Verdict

**PASS.**

I found no fatal or nonfatal mathematical defect in the frozen V2 packet.
The uniform full-torsor constants and parity are valid. The singleton
criterion is exact. The (K=(N-1)/2) divisor-spike identity and strict
quotient decrease are valid. The granted-list theorem charges exactly
postprocessing, and the end-to-end corollary separately charges the list
generator. The degree-one unknown-divisor Coppersmith invocation has enough
fixed exponent slack for both balanced factors.

This verdict is only for the theorems that V2 states. V2 does not construct
the generator (G), does not settle the critical
(m=\Theta(\sqrt N)) band, and does not give an unconditional factoring
algorithm.

## 1. Pre-read authentication

I enumerated and SHA-256 hashed the F212 directory before opening any V1 or
V2 content. After opening `V2_MANIFEST.md`, I compared those pre-read values
with every frozen hash in the manifest. All matched exactly.

### V2

- `V2_STATEMENT.md`:
  `69e0ca4f9cefb0ed41cbeaff25aa48b184d4039dffce11257baf787d8866dd99`
- `V2_PROOF.md`:
  `7cb6eb791cb05e2bb9139730bd188ca9566f890c7ce28d1f21f28e8c041708dc`
- `V2_PROVENANCE.md`:
  `8d98d62a81d5ec2290d98c8d38cb8a297dcb7734fe3bc020b2175d4fbe910096`

The independently recorded hash of `V2_MANIFEST.md` was

`1f8a21596d1b9b6ec9b4508583156fdec3d04e62b0fb9b6f02c0ec330e06df76`.

### Preserved V1

- `STATEMENT.md`:
  `f02027e683c21e7ca83082ac62d57b3d8df87e99f9e1ac0344ca98c6cd0a4400`
- `PROOF.md`:
  `bd91b0b05203aa4814e32970e3619def8066afd5081d9727e6c88ae1b392b878`
- `SELF_AUDIT.md`:
  `69973aa7217e5a798d8944c49a2ad86f9a62ba34b665d4aa43588804e397065c`
- `PROVENANCE.md`:
  `70a6165e013b95824428d8dbb2d860ef9df881e98ad6a4b324b9e23de6cb96bd`
- `MANIFEST.md`:
  `29efbe5eda6fda4bb7c6cc96079d02e51e055ff8091a2caaf4b35574fc083f08`
- `HOSTILE_AUDIT.md`:
  `e5ffa28f2d4f6f5b7f6621af5214b2a08ded069cd764304cd2a3d3d87595165c`

The V1 failed audit was used only as historical evidence. Its verdict was
not transferred to V2.

## 2. Uniform full-torsor theorem

Put (t=\sqrt N\) and (s=\operatorname{lcm}(2,m)). Under the finite
hypotheses, (t\geq32) and (s\leq t/8\).

### 2.1 Parity and exact progression step

If (m) is even, every unit class modulo (m) is odd. All of its lifts
are odd, and consecutive lifts differ by (m). If (m) is odd, adding
(m) reverses parity, so consecutive odd lifts differ by (2m). Thus in
both cases the exact odd-lift step is

\[
s=\operatorname{lcm}(2,m).
\]

There is no compatibility hole: every residue class modulo an odd (m)
has one odd lift class modulo (2m), while every unit class modulo an even
(m) is already odd. Since \(\gcd(m,N)=1\), both (x) and
(Nx^{-1}\bmod m) are units.

An inclusive integer interval of span at least (s-1) contains (s)
consecutive integers and hence meets each relevant step-(s) class. The
proof uses span, not cardinality, with the correct one-unit offset.

### 2.2 Both interval progressions are nonempty

The frozen bounds give

\[
B-L>\left(1-\frac1{\sqrt2}\right)t-2,
\qquad
U-(B+1)>(\sqrt2-1)t-3.
\]

At (t=32), each right side is greater than (3). This remains true for
larger (t). Since (s\leq4) when (t=32), and generally (s\leq t/8),
the stronger displayed linear bounds imply both spans are at least
(s-1). Therefore every unit state has a nonempty progression in both
intervals.

### 2.3 Lower endpoint product

Uniformly in (x),

\[
P_x^-Q_x^-
<
\left(\left(\frac1{\sqrt2}+\frac18\right)t+1\right)
\left(\frac98t+1\right).
\]

Let (D_-(t)) be (t^2) minus the right side. Its quadratic coefficient
is

\[
1-\frac9{8\sqrt2}-\frac9{64}>\frac1{16};
\]

the last inequality is equivalent to (51>36\sqrt2), whose square is
(2601>2592). The magnitude of its linear coefficient is

\[
\frac1{\sqrt2}+\frac54<2.
\]

Consequently (D_-'(t)>0) for (t\geq32). At the endpoint,

\[
D_-(32)=839-592\sqrt2>0,
\]

because (839^2-2\cdot592^2=2993>0). Hence
(P_x^-Q_x^-<N) uniformly.

### 2.4 Upper endpoint product

Uniformly in (x),

\[
P_x^+Q_x^+
>
\left(\frac78t-1\right)
\left(\left(\sqrt2-\frac18\right)t-2\right).
\]

The product's quadratic coefficient exceeds (1+1/8), since
(56\sqrt2>79). The magnitude of its linear coefficient is
(13/8+\sqrt2<25/8). Therefore the product minus (t^2) is greater than

\[
\frac{t^2-25t}{8}+2,
\]

which is positive for (t\geq32). Thus (P_x^+Q_x^+>N) uniformly.

All three frontier conditions hold for every (x\in U(m)), proving

\[
\mathcal F_N(m)=U(m).
\]

The asymptotic consequences have the correct quantifiers. A sequence with
(s/\sqrt N\to0) eventually enters the fixed (1/8) range, and
(m=o(\sqrt N)) suffices because (s\leq2m).

Finally, the lower bound

\[
\varphi(m)\geq\sqrt{m/2}
\]

is valid. In the product for (\varphi(m)^2/m), every odd prime-power
component contributes at least (1), and only the component (2^1) can
contribute (1/2). No assumption that (m) is odd was smuggled into this
bound.

## 3. Singleton criterion

Two distinct odd lifts in one residue class differ by at least the exact
step (s). The strict condition

\[
s>\max\{B-L,U-(B+1)\}
\]

therefore makes each nonempty progression a singleton. It must be strict:
equality of step and span can leave both endpoints in one progression. V2
uses the correct strict inequality.

Writing the singleton representatives as (X\in P) and (Y\in Q), the
endpoint bracket becomes

\[
XY\leq N\leq XY,
\]

so (XY=N). Conversely, if (X\in P), (X\mid N), and
(Y=N/X\in Q), then \(\gcd(X,m)=1\) follows from
\(\gcd(m,N)=1\), and (Y\equiv NX^{-1}\pmod m). These representatives
form the required live branch. Singletonness also makes the map from (X)
to (X\bmod m) injective on (P), so the displayed set identity does not
lose multiplicities.

For the promised semiprime,

\[
p^2>N/2,quad p^2<N,quad q^2>N,quad q^2<2N.
\]

The exact definitions of (L,B,U) then place (p\in P) and (q\in Q).
The other divisors (1,N) do not lie in the ordered intervals. The frontier
is exactly the ((p,q)) branch.

If (m/\sqrt N\to\infty), then (s\geq m), while both interval spans are
(O(\sqrt N)). The singleton condition follows eventually. V2 correctly
treats the intervening (\Theta(\sqrt N)) scale as an unresolved band, not
as a hardness theorem.

## 4. The (K=(N-1)/2) divisor spike

The basic identities are exact:

\[
\gcd(K,N)=1,
\qquad
N\equiv1\pmod K.
\]

The smallest promised input is at least (15). For (N\geq15),

\[
K>\sqrt{2N-1}\geq U
\]

follows from (N^2-10N+5>0). Thus the relevant interval
representatives are unique modulo (K).

For (X\in P) and (Y\in Q), the lower interval endpoints give

\[
XY>\sqrt{\frac{N(N-1)}2}>\frac{N+1}{2}=N-K.
\]

The second strict inequality is equivalent after squaring to
(N^2-4N-1>0), valid here. The upper endpoints give

\[
XY\leq BU<\sqrt{N(2N-1)}<\frac{3N-1}{2}=N+K,
\]

where the final squared difference is ((N-1)^2/4>0). Hence

\[
|XY-N|<K.
\]

The congruence (XY\equiv N\pmod K) now forces equality; the converse is
immediate.

For every positive (X),

\[
\left\lfloor\frac NX\right\rfloor-
\left\lfloor\frac{N-1}{X}\right\rfloor
=\mathbf1_{X\mid N}.
\]

If (L\leq X\leq B) divides the odd (N), then (X) is automatically
odd. Since (N) is nonsquare, (Y=N/X>B). Also
(X^2\geq(N+1)/2), so

\[
Y^2\leq\frac{2N^2}{N+1}\leq2N-1,
\]

and (Y\leq U). Thus every nonzero summand corresponds to exactly one
frontier state, and every frontier state gives one such summand. Even
indices contribute zero. The divisor-spike identity and its unique witness
(p) are exact.

For strict quotient decrease, if (L\leq X<B), then

\[
X(X+1)\leq B(B-1)<B^2\leq N.
\]

Therefore

\[
\frac NX-\frac N{X+1}
=\frac{N}{X(X+1)}>1,
\]

which implies

\[
\left\lfloor\frac NX\right\rfloor>
\left\lfloor\frac N{X+1}\right\rfloor.
\]

Since (B-L+1=\Theta(\sqrt N)), literal equal-quotient grouping has that
many blocks on the shell. V2 properly limits this to the named literal
method and states no lower bound against a different exact floor evaluator.

## 5. Granted-list Coppersmith postprocessing

### 5.1 Imported theorem and fixed parameters

The imported result is the standard monic univariate small-root theorem
modulo an unknown divisor. In fixed degree (\delta=1), fixed
(0<\beta\leq1), and fixed margin (\eta>0), its range is

\[
|t_0|\leq N^{\beta^2-\eta}
\]

for a root modulo a divisor (D\mid N) with (D\geq N^\beta), in
deterministic polynomial bit complexity. V2 does not invoke a heuristic
multivariate theorem.

It is enough to audit (0<\varepsilon\leq1/8). A list satisfying the
stronger lower bound for a larger (\varepsilon) also satisfies it for
(\varepsilon=1/8).

For a correct (p)-residue,

\[
p=r+mt,
\qquad
0\leq t<\frac{\sqrt N}{m}\leq N^{1/4-\varepsilon}.
\]

For a correct (q)-residue,

\[
0\leq t<\frac{\sqrt{2N}}m
\leq\sqrt2N^{1/4-\varepsilon}
\leq N^{1/4-\varepsilon/2}
\]

for all sufficiently large (N).

Take

\[
\beta=\frac12-\frac\varepsilon4.
\]

Balance gives (p>\sqrt{N/2}\geq N^\beta) for sufficiently large (N),
and (q>\sqrt N\geq N^\beta). Moreover,

\[
\beta^2-\left(\frac14-\frac\varepsilon2\right)
=\frac\varepsilon4+\frac{\varepsilon^2}{16}>0.
\]

Choosing one fixed theorem margin (\eta) below this difference puts both
roots inside the imported bound. The balance constant and the factor
(\sqrt2) are absorbed by explicit exponent slack, not discarded.

### 5.2 Monic normalization and verification

The promise \(\gcd(m,N)=1\) gives (m^{-1}\bmod N). With

\[
c\equiv r m^{-1}\pmod N,
\qquad
f(T)=T+c,
\]

the polynomial is monic and has an (O(n))-bit coefficient. If
(r+mt=p) or (q), then modulo that hidden divisor,

\[
mf(t)\equiv mt+r\equiv0.
\]

Because (m) is also a unit modulo the divisor, (f(t)\equiv0). The
Coppersmith routine therefore returns the correct integer (t). Exact
computation of

\[
\gcd(r+mt,N)
\]

recovers the promised factor. Roots produced for incorrect list entries
cannot cause an incorrect output because every gcd is checked for
properness. The fixed-parameter theorem returns only a polynomial-size root
list per call.

The asymptotic inequalities exclude only finitely many inputs for fixed
(\varepsilon). Trial division below a fixed effective cutoff has constant
cost relative to the varying input length and closes those cases.

### 5.3 Input length and exact checks

Theorem 4A takes the explicit list as an auxiliary input. It does not claim
to construct it. For each promised entry,

\[
m\leq N^C,
\qquad
0\leq r<m,
\]

so the canonical binary encodings of both values have (O_C(n)) bits.
Self-delimiting lengths add only lower-order overhead. The asserted
bit-length validation rejects noncanonical padding or an overlong field; it
does not require scanning a field after its declared length has already
exceeded the bound.

Writing (1/4+\varepsilon=A/D) in lowest terms gives the exact equivalence

\[
m\geq N^{1/4+\varepsilon}
\quad\Longleftrightarrow\quad
m^D\geq N^A.
\]

The integers (A,D,C) are fixed. Both this comparison and
(m\leq N^C) therefore involve only (O_{C,\varepsilon}(n))-bit
operands. Syntax, count, range, and gcd checks are polynomial per entry.

There are at most (Q(n)) entries. Each modular inverse, linear-polynomial
construction, fixed-parameter Coppersmith call, candidate reconstruction,
and exact gcd costs \(\operatorname{poly}(n)\). Even for an incorrect
entry, a returned root has fixed-power size and (r+mt) has (O_C(n))
bits. Thus the full postprocessing cost is

\[
Q(n)\operatorname{poly}(n),
\]

which is a numerical quasipolynomial. The list itself has
(Q(n)O_C(n)) bits, so its serialization and parsing fit the same bound.
No generation cost is hidden inside Theorem 4A.

## 6. End-to-end generator accounting

Corollary 4B repairs the exact V1 quantifier failure. It separately assumes
a deterministic public generator (G) that

1. runs in numerical QP bit complexity;
2. emits the explicit, bounded encoding promised by Theorem 4A;
3. emits at least one correct factor residue; and
4. uses no hidden-factor oracle.

The first premise charges all internal list construction. Explicit output
serialization is also charged because a standard bit machine emits at most
one constant-size output unit per step. Independently, the list promises
bound the output by (Q(n)O_C(n)) bits. The postprocessor then charges
parsing, exact bound checks, gcd-promise checks, inverses, polynomial
construction, every Coppersmith call, candidate multiplication, gcd
verification, and exact division.

The sum or composition of two fixed numerical quasipolynomial bounds is
again a numerical quasipolynomial. Thus the conditional end-to-end
conclusion follows. The condition that (G) emits a correct residue is the
unresolved constructive content, not an omitted runtime cost. V2 explicitly
states that it does not construct (G).

## 7. Named method boundaries

The Fourier expansion has the correct normalization and signs under the
displayed transform convention. It applies only to the two separable
residue indicators. V2 explicitly excludes the nonseparable endpoint-product
predicate from that identity and does not turn approximate Kloosterman
bounds into an exact decision procedure.

Likewise, the CRT-order discussion concerns only literal explicit torsor
expansion and a literal full interval scan. It expressly leaves compressed
states, adaptive exact counters, meet-in-the-middle methods, and nonlinear
decoders open. Neither section states an algorithmic lower bound.

## 8. Strict disposition

The frozen V2 statement and proof survive this hostile audit. The V1
terminal defect is repaired without changing the claim into an
unconditional generator theorem. The packet may proceed to a separate
statement-only blind reconstruction.

**Final verdict: PASS.**
