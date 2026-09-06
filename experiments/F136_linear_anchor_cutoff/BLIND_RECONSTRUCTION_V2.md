# F136 strict blind reconstruction, version 2

## Provenance and verdict

I reconstructed this note from STATEMENT.md only. Its SHA-256 was

    7f751c757ce61b341e1845abf04c7f1076b6417af827480520a9f77ebd6c9a3e

I did not inspect a proof, manifest, audit, failure report, ledger, or other
project file.

**Verdict: pass in the stated outside-the-fixed-threshold regime.** The four
theorems follow from the definitions. Theorem 4 is only a composition with
an imported hypothesis. It does not prove the imported hypothesis, parity
closure, or factoring.

Two conventions must be explicit.

1. Set an unoccupied bucket product to the empty product, \(L_A=1\). This is
   needed when the statement writes \(L_0\le B\) but digit zero is unoccupied.
2. The numerical width bound (6) uses Theorem 1 and therefore inherits
   \(n\ge21846\). The residual-size implications do not need that restriction.
   The surrounding statement sends smaller inputs to fixed finite trial
   division. A literal all-small-\(n\) reading of (6) needs a separate finite
   verification, although an independent stress check found no counterexample.

I use \(\log\) or \(\ln\) for the natural logarithm and reserve \(\log_2\)
for the base-two logarithm.

## 1. Reconstructed objects

For a unit \(c\in\{1,\ldots,N-1\}\), let

\[
\iota_N(c)\in\{1,\ldots,N-1\},\qquad
c\iota_N(c)\equiv1\pmod N,
\]

and define the exact integer

\[
P_N(c)=c\iota_N(c).
\]

The source first applies the two declared gcd screens to every generated
unit. If either screen gives a nontrivial factor, that is already one branch
of every later conclusion. Otherwise it stores the two integer endpoints,
retains one column for each distinct exact value \(P_N(c)\), and performs
complete gcd-free refinement. The refinement gives pairwise-coprime named
blocks and exact nonnegative exponents. Thus the parity row of a rational
prime \(r\) at a retained value \(V\) is \(v_r(V)\bmod2\), and its degree is
the number of retained exact values on which that bit is one.

Put

\[
n=\lceil\log_2(N+1)\rceil,\qquad B=\lceil12n\rceil=12n.
\]

Choose a unit block

\[
1<q<N/B,
\]

and put \(w=\iota_N(q)\). An eligible anchor is a prime

\[
\ell\le B,\qquad \ell\nmid Nq.
\]

Since \(N\) is invertible modulo such an \(\ell\), there is one digit

\[
A_\ell\equiv-wN^{-1}\pmod\ell,\qquad 0\le A_\ell<\ell.
\]

For each digit, occupied or not, define

\[
H_A=w+NA,\qquad
\mathcal L_A=\{\ell:A_\ell=A\},\qquad
L_A=\prod_{\ell\in\mathcal L_A}\ell,
\]

using \(L_A=1\) for an empty bucket. Every occupied digit lies in
\(\{0,\ldots,B-1\}\). Finally,

\[
G_B(N,q)=
\prod_{\substack{\ell\le B\ {\rm prime}\\\ell\nmid Nq}}\ell
=\prod_A L_A.
\]

### Anchor identity

For an eligible \(\ell\), the integer

\[
x_\ell=\frac{H_{A_\ell}}\ell
\]

is positive. Also,

\[
H_{A_\ell}\le (N-1)+N(\ell-1)=N\ell-1,
\]

so \(x_\ell<N\). Moreover,

\[
(\ell q)x_\ell=q(w+NA_\ell)\equiv qw\equiv1\pmod N.
\]

The cutoff \(q<N/B\) and \(\ell\le B\) give \(\ell q<N\). Hence

\[
\iota_N(\ell q)=x_\ell,\qquad
\boxed{P_N(\ell q)=qH_{A_\ell}}.
\]

Thus the unary column is \(qH_0=qw\), and every occupied nonzero digit \(A\)
gives the exact column \(qH_A\). Distinct digits give distinct exact values.
If digit zero is occupied, its anchored value equals the unary value, so
exact-value deletion correctly keeps one copy.

## 2. Theorem 1: elementary primorial estimate

Define

\[
\psi(x)=\log\operatorname{lcm}(1,2,\ldots,\lfloor x\rfloor).
\]

Let \(m=\lfloor x/2\rfloor\). For every prime \(p\),

\[
v_p\binom{2m}{m}
=\sum_{j\ge1}
\left(
\left\lfloor\frac{2m}{p^j}\right\rfloor
-2\left\lfloor\frac m{p^j}\right\rfloor
\right).
\]

Each summand is zero or one. There are at most
\(\lfloor\log_p(2m)\rfloor\) possible nonzero summands, which is the exponent
of \(p\) in \(\operatorname{lcm}(1,\ldots,2m)\). Therefore

\[
\binom{2m}{m}\mid\operatorname{lcm}(1,\ldots,2m).
\]

The central binomial coefficient is the largest term in the expansion of
\(2^{2m}\), so

\[
\binom{2m}{m}\ge\frac{4^m}{2m+1}.
\]

Consequently,

\[
\psi(x)\ge\psi(2m)
\ge2m\log2-\log(2m+1)
>(x-2)\log2-\log(x+1).
\tag{9}
\]

If \(K=\lfloor\log_2x\rfloor\), then

\[
\psi(x)=\sum_{k=1}^{K}\vartheta(x^{1/k}).
\]

The elementary estimate \(\vartheta(y)\le y\log y\) gives

\[
\begin{aligned}
\psi(x)-\vartheta(x)
&\le \log x\sum_{k=2}^{K}\frac{x^{1/k}}k\\
&\le \frac12\sqrt{x}\log x
+\frac{x^{1/3}(\log x)^2}{3\log2}.
\end{aligned}
\tag{10}
\]

Combining (9) and (10),

\[
\frac{\vartheta(x)}x>
\log2-
\frac{2\log2+\log(x+1)}x
-\frac{\log x}{2\sqrt x}
-\frac{(\log x)^2}{3\log2\,x^{2/3}}.
\tag{11}
\]

All three subtracted functions decrease for \(x\ge2^{18}\). At
\(x_0=2^{18}\), use the elementary bounds

\[
0.69<\log2<0.70,\quad
\log x_0<13,\quad
\log(x_0+1)<14,\quad
\sqrt{x_0}=512,\quad
x_0^{2/3}=4096.
\]

The right side of (11) is greater than \(0.657\). In particular,

\[
\boxed{\vartheta(x)>\frac6{25}x}
\qquad(x\ge2^{18}).
\]

This proof uses only the central binomial coefficient, the least common
multiple, and the elementary prime-power correction (10).

For \(n\ge21846\),

\[
B=12n\ge262152>2^{18}.
\]

If \(Q_B=\prod_{\ell\le B,\ \ell\ {\rm prime}}\ell\), then

\[
\log Q_B=\vartheta(B)>\frac6{25}B=\frac{72}{25}n.
\]

Since \(N<2^n\) and \(4\log2<2.8<72/25\),

\[
4\log N<4n\log2<\frac{72}{25}n<\log Q_B.
\]

Therefore

\[
\boxed{Q_B>N^4}.
\]

The value \(21846\) is the least integer \(n\) for which
\(12n\ge2^{18}\). The lower range is fixed and finite, so finite trial
division handles it in the stated asymptotic sense.

## 3. Theorem 2: linear-cutoff row reuse

Let

\[
D=\prod_{\substack{\ell\le B\ {\rm prime}\\\ell\mid Nq}}\ell.
\]

This squarefree product divides \(Nq\). Hence

\[
G_B(N,q)=\frac{Q_B}{D}>\frac{N^4}{Nq}.
\]

The strict block cutoff gives \(Nq<N^2/B\). Therefore

\[
\boxed{G_B(N,q)>N^2B}.
\]

Now fix a prime \(r>B\) for which \(v_r(q)\) is odd. Since \(q\) is a unit
modulo \(N\), \(r\nmid N\). Let

\[
S=\{0\}\cup\{A:A\text{ is occupied}\}.
\]

First, \(S\) has at least three elements. If it had at most two, there could
be at most one occupied nonzero digit \(A\). We have

\[
L_0\mid H_0=w<N,\qquad L_A\mid H_A<NB,
\]

with an absent factor interpreted as one. It would follow that

\[
G_B(N,q)=\prod_A L_A<N^2B,
\]

contrary to the boxed lower bound.

Second, \(r\) divides at most one of the integers \(H_A\) with \(A\in S\).
Indeed, if \(r\mid H_A\) and \(r\mid H_C\), then

\[
r\mid H_A-H_C=N(A-C).
\]

Because \(r\nmid N\), this implies \(r\mid A-C\). But distinct digits in
\(S\) satisfy \(0<|A-C|<B<r\), a contradiction.

At least two digits in \(S\) therefore have \(v_r(H_A)=0\). Their distinct
exact values \(qH_A\) have

\[
v_r(qH_A)\equiv v_r(q)\equiv1\pmod2.
\]

The anchor identity shows that these are generated columns, with digit zero
represented by the unary value. Global exact-value deletion cannot identify
values from two different digits. Thus, unless a preceding screen already
returned a factor,

\[
\boxed{\deg(r)\ge2}.
\]

The prose cutoff \(q<N/(12n+1)\) safely weakens the proved cutoff
\(q<N/(12n)\). Likewise, \(r>12n+1\) safely weakens \(r>B=12n\).

## 4. Theorem 3: release or width

Complete refinement names every eligible anchor prime \(\ell\): the stored
first endpoints include both \(q\) and \(\ell q\), and \(\ell\nmid q\). It
also records the full exponent of that named prime in every endpoint. For a
bucket \(A\), define the full removable anchor part and residual by

\[
M_A=\prod_{\ell\in\mathcal L_A}\ell^{v_\ell(H_A)},
\qquad R_A=H_A/M_A.
\]

Every bucket prime divides \(H_A\), so \(M_A\ge L_A\). If \(R_A=1\), the
residual is exhausted. Otherwise every residual block produced by complete
refinement is at most \(R_A\).

For digit zero, \(H_0=w<N\). Hence

\[
L_0>B\quad\Longrightarrow\quad
R_0\le\frac{H_0}{L_0}<\frac NB.
\]

For an occupied nonzero digit, \(A\le B-1\), so \(H_A=w+NA<NB\).
Therefore

\[
L_A>B^2\quad\Longrightarrow\quad
R_A\le\frac{H_A}{L_A}<\frac{NB}{B^2}=\frac NB.
\]

These are the two release claims, including residual exhaustion.

Now assume no bucket releases:

\[
L_0\le B,\qquad L_A\le B^2\quad(A>0).
\]

If \(d\) is the number of occupied nonzero digits, then

\[
G_B(N,q)=\prod_A L_A\le B^{2d+1}.
\tag{12}
\]

For \(n\ge21846\), the proof of Theorem 2 gives the more informative estimate

\[
\begin{aligned}
\log G_B(N,q)
&=\vartheta(B)-\log D\\
&>\frac{72}{25}n-2\log N+\log B\\
&>\left(\frac{72}{25}-2\log2\right)n+\log B.
\end{aligned}
\tag{13}
\]

Combining (12) and (13) gives

\[
d>
\left(\frac{36}{25}-\log2\right)\frac n{\log B}.
\]

The elementary inequality \(\log2<7/10\), together with
\(B=12n<13n\), yields

\[
\boxed{d>\frac{37n}{50\log(13n)}}.
\]

The exact coefficient before weakening is

\[
\frac{36}{25}-\log2=0.7468528194\ldots,
\]

so the stated \(37/50=0.74\) has genuine slack.

For a fixed prime \(r>B\) with odd \(v_r(q)\), at most one occupied nonzero
digit can satisfy \(r\mid H_A\), by the difference argument in Theorem 2.
An odd \(v_r(H_A)\) implies this divisibility. Thus at least \(d-1\)
nonzero-digit columns have even \(v_r(H_A)\), and their values \(qH_A\) have
odd \(r\)-valuation. The values are distinct. Unless a declared screen has
already factored \(N\), at least \(d-1\) retained columns reuse that row.

It follows, for each such large odd row, that one gets:

1. a nontrivial residual block below \(N/B\);
2. complete residual exhaustion; or
3. \(\Omega(n/\log n)\) distinct reused-row columns.

This is a row-width statement. It does not assert that the full parity matrix
has a nonzero binary kernel.

## 5. Theorem 4: conditional composition only

The imported assumption defines

\[
L=\lceil\log_2(n+1)\rceil,\qquad
E=2^{L^2},\qquad T=L^2,
\]

and postulates an adaptive all-block source which already processes every
current block against every integer anchor through \(E\), for \(T\) frozen
rounds, while retaining endpoints and completing refinement and parity decode
in deterministic bit complexity

\[
2^{O((\log n)^4)}.
\]

Because \(2^L\ge n+1\),

\[
E=(2^L)^L\ge(n+1)^L\ge(n+1)^2.
\]

For \(n\ge21846\), certainly \(L\ge2\), and

\[
(n+1)^2>12n=B.
\]

Hence \(B<E\). Every eligible F136 anchor is already one of the imported
source's integer-anchor positions. Selecting or marking those positions does
not enlarge the source enumeration. Its bookkeeping is polynomial in \(n\)
and is absorbed by the imported bound. Thus the composition retains

\[
\boxed{2^{O((\log n)^4)}}.
\]

This conclusion is conditional in two separate senses:

- It assumes the all-block source and its complexity guarantee.
- It only embeds the F136 subbank and preserves complexity. It does not
  establish that final parity decode finds a dependency or a factor.

The values \(T\) and the adaptive-round semantics belong to the imported
guarantee. The proofs of Theorems 1--3 never use them.

## 6. Exact consequence and remaining gap

Define the mod-two squarefree part

\[
\operatorname{sf}_2(q)=\prod_{v_p(q)\ {\rm odd}}p.
\]

For \(q<N/(12n+1)\), one also has \(q<N/B\). If
\(\operatorname{sf}_2(q)\) is \(B\)-smooth, the first stated alternative
holds. Otherwise every prime \(r>B\) in its support has odd \(v_r(q)\), so
Theorem 2 applies separately to every such row and gives degree at least two.
This proves the exact dichotomy in the statement's high-\(n\) range.

Nothing here forces a binary kernel. A collection of columns can have all
selected row degrees at least two while other rows maintain an acyclic
incidence pattern. Claims about the particular P122 or F135 models are not
audited here because those sources were outside the blind boundary.

## 7. Refutation attempts and boundary audit

### Constants

- **\(2^{18}\) and \(6/25\):** The elementary normalized lower bound (11) is
  already greater than \(0.657\) at the threshold, versus the required
  \(0.24\). Its error terms decrease thereafter.
- **\(21846\):** This is exactly \(\lceil2^{18}/12\rceil\).
- **The exponent \(4\):** The proof supplies coefficient \(72/25=2.88\),
  while \(N^4\) needs only \(4\log2=2.77258\ldots\).
- **\(N^2B\):** Removing primes which divide \(Nq\) costs at most
  \(Nq<N^2/B\). The strict direction is correct.
- **Release thresholds \(B\) and \(B^2\):** They match \(H_0<N\) and
  \(H_A<NB\). A strictly larger removed product gives a residual strictly
  below \(N/B\).
- **\(37/50\):** The proof first gives
  \(36/25-\log2=0.7468528\ldots\), then lowers the numerator to \(0.74\) and
  enlarges the denominator from \(\log(12n)\) to \(\log(13n)\). Both changes
  weaken the claim.
- **\(B<E\):** The stated range is more than sufficient. Comparison with
  \((n+1)^2\) proves it immediately in that range.

### Scopes and collision attacks

- All occupied digits satisfy \(A<B<r\). This is exactly what prevents two
  \(H_A\)'s from being divisible by the same \(r>B\).
- Exact-value deletion removes repeated anchors within one bucket, but cannot
  merge two digit columns because
  \(qH_A-qH_C=qN(A-C)\ne0\).
- The unary value supplies digit zero even when no anchor occupies zero. This
  is why the product bound forces at least three candidate digits in Theorem
  2.
- A large prime occurring to an even exponent in \(H_A\) causes no failure:
  odd \(v_r(q)\) plus even \(v_r(H_A)\) is odd. Odd \(v_r(H_A)\) implies
  divisibility, and only one bucket can have that.
- The squarefree-kernel consequence uses the mod-two squarefree part. If
  kernel instead means the radical, the second alternative can be vacuous for
  large primes of even exponent; no false row claim follows, but the
  terminology should be fixed.
- Claims attributed to P121, P122, and F135 were outside the permitted blind
  source and are not independently certified here.

No attempted endpoint-range, exact-value, parity, strict-inequality, constant,
or high-\(n\) scope attack refuted Theorems 1--3. The remaining gap is real:
row degree at least two, even across many columns, does not force a binary
dependency.
