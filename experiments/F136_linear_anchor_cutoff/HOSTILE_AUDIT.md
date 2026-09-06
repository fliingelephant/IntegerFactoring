# F136 hostile audit — PASS

## Verdict

**PASS.** I found no false quantifier, failed boundary constant, hidden
factoring step, or deduplication gap in the frozen statement and proof.

Audited frozen hashes:

- `STATEMENT.md`:
  `2a456da6341d4a055cf07305d463319b5fbcef3abd5344581b752f0d8aa0fa49`
- `PROOF.md`:
  `a17bfc6bafad8cb1d7fb37e9a4de64f247eb5ad719648a21261154c06306d5e5`

The pre-audit `MANIFEST.md` hash was
`3cf770bc01bc527e40f7d0aa59dda419ef0a4becefef3897141ad2b026aafa59`.
The accepted result is only a linear-cutoff source theorem. It does not
force a binary dependency, a non-global root, or a factor.

## 1. Real-variable primorial bound

Put

\[
h(x)=\left(1-\frac1x\right)\log2-\frac{\log(x+1)}x,
\qquad
g(x)=\frac{(\log x)^2}{\sqrt{x}\log2}.
\]

The central-binomial argument applies to real \(x\ge2\) after taking
\(m=\lfloor x/2\rfloor\):

\[
2m\ge x-1,
\qquad
2m+1\le x+1,
\]

so

\[
\psi(x)\ge2m\log2-\log(2m+1)
\ge(x-1)\log2-\log(x+1).
\]

The exact prime-power decomposition and the elementary bound
\(\vartheta(y)\le y\log y\) give

\[
\psi(x)-\vartheta(x)
=\sum_{k=2}^{\lfloor\log_2x\rfloor}\vartheta(x^{1/k})
\le\frac{\sqrt{x}(\log x)^2}{\log2}.
\]

The derivative used in the proof is correct:

\[
h'(x)=
\frac{\log2+\log(x+1)-x/(x+1)}{x^2}>0
\quad(x\ge2).
\]

Also, \(g'(x)<0\) when \(\log x>4\). Thus the lower bound
\(h(x)-g(x)\) increases throughout the declared range.

At \(x=2^{18}\), the proof's rational substitutions give exactly

\[
\left(1-2^{-18}\right)\frac{69}{100}
-\frac{133/10}{2^{18}}
-\frac{(126/10)^2(145/100)}{512}
=\frac{31500973}{131072000}.
\]

Its exact excess over \(6/25\) is

\[
\frac{43693}{131072000}>0.
\]

Therefore the strict bound

\[
\vartheta(x)>\frac6{25}x
\]

holds for every real \(x\ge2^{18}\), as claimed.

## 2. Linear cutoff and excluded primes

At the first declared bit length,

\[
n=21846,
\qquad
B=\lceil12n\rceil=262152>2^{18}.
\]

For all larger \(n\), the same inequality remains true. The constants satisfy

\[
\frac6{25}B
\ge\frac{72}{25}n
>\frac{14}{5}n
>4n\log2.
\]

Since \(n=\lceil\log_2(N+1)\rceil\), one has \(N<2^n\). Hence the full
prime product through \(B\) is strictly larger than \(N^4\).

Let \(X\) be the product of primes through \(B\) that divide \(Nq\). The
proof uses only

\[
X\le\operatorname{rad}(Nq)\le Nq<\frac{N^2}{B}.
\]

Removing these excluded primes therefore gives, with the correct strict
inequality,

\[
G_B(N,q)>N^2B.
\]

No estimate assumes knowledge of a factor of \(N\) or \(q\).

## 3. Forced two-column row reuse

Fix \(r>B\) with odd \(v_r(q)\). Because \(q\) is a unit modulo \(N\),
\(r\nmid N\).

If \(r\mid w\), every observed nonzero digit \(A<B<r\) has

\[
w+NA\not\equiv0\pmod r.
\]

If \(r\nmid w\), at most one observed digit can be divisible by \(r\),
because two such digits would give \(r\mid A-A'\) with
\(|A-A'|<B<r\). Thus at most one nonzero bucket can be bad for row \(r\).

The eligible prime product in the zero bucket is below \(N\), and the
product in one nonzero bucket is below \(NB\). If no good nonzero digit
existed, all eligible primes would fit into these two buckets, contrary to
\(G_B(N,q)>N^2B\).

All valuation cases give two distinct odd-row columns.

1. If \(v_r(w)\) is even, the unary value is odd in row \(r\), and one
   nonzero good digit supplies a different odd-row value.
2. If \(v_r(w)\) is odd, then \(r\mid w\). Every nonzero digit is good.
   Zero or one nonzero digit would again put \(G_B(N,q)\) below \(N^2B\),
   so two distinct nonzero digits exist.

Different digits give different exact integers \(q(w+NA)\). Global
first-occurrence deletion cannot remove a distinct integer: either its old
copy remains, or its new first copy remains. Therefore the degree statement

\[
\deg(r)\ge2
\]

is deduplication-safe.

## 4. Release and exhaustion scope

The release argument uses all endpoint presentations before exact-value
deletion. The old block \(q\) separates each eligible anchor prime from
\(\ell q\). Complete gcd-free refinement then removes every named anchor
prime power from the represented \(H_A\)-side.

With

\[
S_A=\prod_{\ell\in\mathcal L_A}
\ell^{v_\ell(H_A)},
\qquad
R_A=H_A/S_A,
\]

every remaining \(H_A\)-side block divides \(R_A\). The two bounds are exact:

\[
R_0\le\frac{w}{L_0}<\frac{N}{L_0},
\]

and, for \(A>0\),

\[
R_A\le\frac{H_A}{L_A}
<\frac{NB}{L_A}.
\]

Thus \(L_0>B\) or \(L_A>B^2\) gives a positive residual below \(N/B\),
unless \(R_A=1\), which is exactly residual exhaustion. The proof does not
claim that the released block is automatically useful or that it closes a
parity cycle.

## 5. Width constant

On the no-release branch, the occupied buckets partition the eligible
primes and give

\[
G_B(N,q)=L_0\prod_{A>0}L_A\le B^{2d+1}.
\]

The excluded-prime estimate retains

\[
\log G_B(N,q)>
\frac6{25}B+\log B-2\log N.
\]

After cancellation,

\[
2d\log B>
\frac6{25}B-2\log N
>\left(\frac{72}{25}-\frac75\right)n
=\frac{37}{25}n.
\]

Since \(B=12n\le13n\), this proves the stated strict inequality

\[
d>\frac{37n}{50\log(13n)}.
\]

For each fixed covered row, at most one nonzero digit is bad. The claimed
\(d-1\) distinct retained odd-row values therefore follows. This is a
per-row statement. It does not say that one common set of \(d-1\) columns
works for all large rows at once.

## 6. Uniformity and source inclusion

For \(n<21846\), ordinary trial division is one fixed uniform program over a
finite input domain. Its worst-case bit-operation count is an absolute
constant. This constant can be absorbed into the quasipolynomial bound; no
nonuniform advice table is required.

For \(n\ge21846\), put

\[
L=\lceil\log_2(n+1)\rceil,
\qquad
E=2^{L^2}.
\]

At the endpoint, \(L=15\). For every later input,
\(n\le2^L-1\), so

\[
B=12n<12\mathbin{\cdot}2^L<2^{L^2}=E.
\]

The F133/P121 all-block source scans every integer anchor through \(E\).
Therefore the primes through \(B\) form a literal subbank of that declared
source. F136 adds no source positions and does not change the existing
transcript or decoder estimate

\[
2^{O((\log n)^4)}.
\]

## Accepted boundary

F136 improves the cutoff from \(n^3\) to \(12n\). It proves release,
exhaustion, or wide row reuse for each small unit block. It does not cover
blocks at least \(N/B\), even valuations, the fresh private rows attached to
the reused columns, closure of the parity matrix, or the normalized-root
image. The expanding-forest obstruction from F135 remains compatible with
all F136 conclusions.
