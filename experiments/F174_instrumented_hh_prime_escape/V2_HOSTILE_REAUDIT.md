# Fresh hostile re-audit of F174 V2

## Verdict

**PASS.**

The V2 operational trichotomy is correct under the stated Harvey--Hittmeir
Algorithm 3.1 premise. The proof covers arbitrary odd composites, including
repeated odd prime powers. The smooth-prefix constants suffice. The absolute
and relative factor-first classifications are exhaustive. The common-return
branch constructs a certified common-order element without any hidden-log
alignment assumption. The F172 corollary and the deterministic QP cost also
survive audit.

The two defects identified by the preserved blind reconstruction are exactly
repaired:

1. the raw line-13 escape is now claimed to be outside at least one old local
   subgroup, and the every-component claim is delayed until the absolute
   gcd-one branch;
2. the general hard branch now says that this procedure certifies no exact
   common quotient order. It no longer claims that the unknown local or
   quotient orders must differ. The mismatch language is restricted to the
   F172 family.

I found no new operative defect. This PASS proves only the source-and-decoder
trichotomy. Outcome C remains possible, so F174 V2 is not a factoring
algorithm.

## Frozen inputs and preserved failure record

I verified the requested frozen hashes before the mathematical audit:

- `V2_STATEMENT.md`:
  `faca4273e53eb04347c07bde9b0fd2fe429f7b681201bec205916cb49d97cecb`;
- `V2_PROOF.md`:
  `3cf9d9f45a42005d1170203910868d65aca16c1cb5ff61fb04c119c7256277f9`.

I also read the preserved V1 audit records in full. Their hashes are:

- `HOSTILE_AUDIT.md`:
  `f6381875873d53c9a72c07bb51633ff60b351b80f6eebeca7be88a4634f6ddbd`;
- `BLIND_RECONSTRUCTION.md`:
  `086610b9fcedea2af55f7f36b81f7b43ddb5b86798e575eafacec31b2f4240d0`.

A direct V1/V2 diff confirms that V2 changes only the title and the prose
needed to repair those two defects. The displayed theorem, parameters,
algorithms, and quantitative bounds are unchanged.

For the external premise, I checked the current primary source,
Harvey--Hittmeir, arXiv:2601.11131v2, Algorithm 3.1 and Lemmas 2.1--2.4:

<https://arxiv.org/html/2601.11131v2>

The source version is dated 5 June 2026. Its pseudocode and stated cost agree
with Section 2 of the V2 statement.

## 1. Harvey--Hittmeir transcript audit

Algorithm 3.1 has the transcript used by F174 V2.

- The lookup-table and even-input exits occur before the main loop.
- Line 4 returns two only when \(2^D<N\). Here \(D\ge n\) and
  \(2^n\ge N+1\), so that exit cannot occur.
- The loop sets \(B=\lceil D^{1/3}\rceil\) and scans consecutive integers
  \(\beta=2,\ldots,B\).
- Its loop state stores an element \(g\), its exact global order \(M\), and
  the complete factorization of \(M\).
- If \(\beta^M\ne1\), Lemma 2.1 either computes the exact global order
  \(m\le D\), or certifies \(m>D\). The latter is exactly line 13.
- After a successful order computation, line 16 tests
  \(\gcd(\beta^{m/r}-1,N)\) for every prime \(r\mid m\).
- Lemma 2.2 constructs an element of exact global order
  \(\operatorname{lcm}(M,m)\) and retains its factorization.
- Line 19 returns only after this new order exceeds \(D\).
- If the loop ends, the source proof establishes \(M\mid p-1\) and its
  public upper bound for every rational prime \(p\mid N\). The final
  arithmetic-progression scan reaches the least prime divisor of composite
  \(N\).

F174 intercepts only line 13. It does not assume an order or factor that the
source did not compute. The finite-table convention can absorb every fixed
small input needed by the source and by the new cutoff inequalities.

There is no missed nonunit branch. If a loop integer shares a prime with
\(N\), then either it is that prime and line 10 returns it, or one of its
smaller prime divisors had already been scanned and returned. Thus every
integer reaching the order search is a unit.

## 2. Exact common-order invariant for prime powers

Let \(m=\operatorname{ord}_N(\gamma)\) be an exact order found in a loop
iteration. On a no-factor branch, for every prime \(r\mid m\),

\[
\gcd(\gamma^{m/r}-1,N)=1.
\]

Fix a rational prime \(p\mid N\), and let
\(m_p=\operatorname{ord}_p(\gamma)\). Since \(m_p\mid m\), any strict loss
in an \(r\)-adic valuation would give \(m_p\mid m/r\), contradicting the
gcd-one result. Hence \(m_p=m\).

For a full component \(R=p^a\parallel N\), the local order is a multiple of
the order modulo \(p\), and it divides the exact global order \(m\). It is
therefore also \(m\). This proves the repeated-prime-power step, not merely
the squarefree case.

The primary-part lcm construction remains exact component by component. Each
input has the same exact order in every component. Raising each input by the
published selected primary exponent gives the intended coprime primary
orders in every component. Their product has order
\(\operatorname{lcm}(M,m)\) in every component. Induction from \((1,1)\)
proves the claimed invariant.

The same argument modulo every rational prime gives \(M\mid p-1\). For each
prime \(p\mid N\), this excludes \(p\mid M\). Thus \(\gcd(M,N)=1\). Line 19
also gives \(M\le D\) before a line-13 escape or the loop-end scan.

## 3. The line-13 prefix and escaped prime

At a line-13 escape, the current integer satisfies

\[
\beta^M\ne1\pmod N,
\qquad
\operatorname{ord}_N(\beta)>D.
\]

Every earlier positive integer \(a<\beta\) was either skipped because its
then-current state order annihilated it, or had its exact order merged into a
later state. Since later state orders are multiples of earlier ones,

\[
a^M=1\pmod N
\qquad(1\le a<\beta).
\]

All such integers are units. If \(\beta=uv\) were composite with
\(1<u,v<\beta\), then \(\beta^M=u^Mv^M=1\), a contradiction. Hence
\(\beta\) is prime.

For \(R_j=p_j^{a_j}\), the unit group is cyclic. Since \(M\mid p_j-1\),
the kernel of the \(M\)-power map has exactly \(M\) elements. It is the
unique subgroup \(H_j=\langle g\rangle\). Thus every \(a<\beta\) belongs to
every \(H_j\).

The raw inequality \(\beta^M\ne1\pmod N\) proves only that \(\beta\) is
outside at least one \(H_j\). V2 now says exactly that. On the later absolute
gcd-one branch, every local order has a primary component above \(D\), so
\(\beta\) is outside every \(H_j\). This is the exact repair required by the
V1 blind failure.

## 4. Smooth-prefix cutoff and constants

Put \(y=\beta-1\). A rational prime divisor \(p\mid N\) cannot satisfy
\(p\le y\), because its earlier loop iteration would have returned a factor.
Every \(y\)-smooth positive integer at most \(p\) is therefore a product of
integers below \(\beta\), and hence is an \(M\)-th root of one modulo \(p\).
The integer \(p\) itself is not counted as \(y\)-smooth. The counted values
are distinct nonzero residues, so

\[
\Psi(p,y)\le M.
\]

Assume \(y\ge Y_D=H_D^2\). Since \(X_D=2^{H_D}\),

\[
\log y\ge2\log H_D>2\log\log X_D.
\]

Also \(y<D^{1/3}\), while \(X_D\) is already much larger than \(D^8\), so
\(X_D\ge y\) above one absolute threshold. Harvey--Hittmeir Lemma 2.4 then
gives

\[
\begin{aligned}
\log\Psi(X_D,y)
&\ge \log X_D\left(1-
  \frac{\log\log X_D}{\log y}\right)\\
&>\frac12H_D\log2\\
&=4L_DJ_D\log2\\
&\ge4\log(2D)>\log M.
\end{aligned}
\]

Thus \(\Psi(X_D,y)>M\). If any \(p\mid N\) exceeded \(X_D\), monotonicity
would contradict \(\Psi(p,y)\le M\). Hence every rational prime divisor is
at most \(X_D\). Since \(M\mid p-1\), the scan of \(kM+1\le X_D\) reaches a
proper prime divisor, including when \(N=p^a\).

Therefore a no-factor escape has \(y<Y_D\), hence the exact integral bound
\(\beta\le Y_D\). The displayed constants have ample slack. Finally,

\[
\log_2X_D=O(\log D\log\log D),
\qquad
Y_D=O((\log D\log\log D)^2),
\]

which gives the claimed QP scan bound and the polylogarithmic escaped prime.

## 5. Absolute factor-first classification

Let \(r_j=\operatorname{ord}_{R_j}(\beta)\). The known factorization of

\[
\Lambda_D=\operatorname{lcm}(1,\ldots,D)
\]

has the exact property

\[
r\mid\Lambda_D
\quad\Longleftrightarrow\quad
\sigma(r)\le D.
\]

For \(A_\beta=\gcd(\beta^{\Lambda_D}-1,N)\), a proper result is already a
factor. If \(A_\beta=1\), no local order \(r_j\) divides \(\Lambda_D\), so
\(\sigma(r_j)>D\) in every component.

If \(A_\beta=N\), the exact global order divides the known factored multiple
\(\Lambda_D\). Standard divisor stripping computes that exact order \(m\)
and its factorization. For every prime \(r\mid m\), the subsequent gcd
\(\gcd(\beta^{m/r}-1,N)\) cannot equal \(N\). A non-one value is proper. If
all are one, the prime-power argument of Section 2 gives exact local order
\(m\) in every component and \(\gcd(m,N)=1\). The line-13 certificate gives
\(m>D\). This is Outcome B.

These three gcd values are disjoint and exhaustive. Partial equality inside
a repeated prime-power component also yields a proper divisor, so no
prime-power case is omitted.

## 6. Relative classification and the common-return branch

In the cyclic local group, \(H_j\) is exactly the subgroup of solutions to
\(x^M=1\). Therefore, for the quotient order \(e_j\),

\[
\beta^{eM}=1\pmod{R_j}
\quad\Longleftrightarrow\quad
e_j\mid e.
\]

A proper \(G_e\) factors \(N\). If the first non-one value is the global
return \(G_e=N\), then every \(e_j\mid e\). Any strict inequality
\(e_j<e\) would have made the earlier test at \(e_j\) non-one. Hence
\(e_j=e\) for every component. Also \(e\ne1\), because line 11 already
gave \(\beta^M\ne1\pmod N\).

This branch does **not** need hidden-log alignment to construct the larger
certified state. The exponent \(eM\) is a known factored annihilator for
\(\beta\). Divisor stripping computes the exact global order \(m\), and the
prime-divisor gcd screens either factor \(N\), or certify

\[
\operatorname{ord}_{R_j}(\beta)=m
\qquad\text{for every }j.
\]

In a cyclic group, a subgroup of order \(M\) intersects a cyclic subgroup of
order \(m\) in the unique subgroup of order \(\gcd(M,m)\). Thus the order of
the image of \(\beta\) modulo \(H_j\) is

\[
e=\frac{m}{\gcd(M,m)},
\]

and consequently

\[
\operatorname{lcm}(M,m)=Me.
\]

The Harvey--Hittmeir primary-part construction now combines \(g\) and
\(\beta\) into one public element of exact order \(Me\) in every component.
The selected primary parts have coprime orders, so this conclusion is
independent of the hidden logarithms in a relation such as
\(\beta^e=g^a\). Since \(m>D\), the new common order \(Me\) is above \(D\).

If all \(G_e=1\) through \(C\), then every \(e_j>C\). Hence the first
\(C+1\) powers of \(\beta^M\) are distinct in every component, and

\[
|\langle g,\beta\rangle_{R_j}|=Me_j\ge M(C+1).
\]

This proves the hard capacity claim. It does not say that the unknown
\(e_j\) differ, and V2 no longer says so.

## 7. F172 specialization

I checked the frozen F172 inputs used by the prior audit:

- F172 `STATEMENT.md`:
  `d2ff244f1fb28e00ba262fdb89cd5a23b7b75954586bfb998ffd188db4a8ed9f`;
- F172 `PROOF.md`:
  `b23989a19a23653dab9946dca55888384a2c4493184878a3dfac68ec9c067a21`.

On that semiprime family,
\(\gcd(p-1,q-1)=6\). Any ordinary element with one exact order in both
hidden fields has order dividing six. Outcome B would give such an order
\(L>D>6\), which is impossible without an earlier factor. Therefore the
instrumented source returns a factor or Outcome C.

On Outcome C, every local order of \(\beta\) is above \(D>6\). If all local
orders were equal, they would contradict the F172 common-order bound. Thus a
hidden mismatch does exist on this family. V2 confines the mismatch claim to
this specialization, which exactly repairs the second V1 defect.

## 8. Deterministic QP cost

Every added numerical and encoded object stays within deterministic QP cost
for QP targets \(D,C\).

- The primary HH transcript has its stated
  \(O(D^{1/2}\log D(\log\log D)^{-1/2}\log N)\) bit cost.
- A sieve through \(D\) constructs the factorization of \(\Lambda_D\). The
  loose bound \(\log\Lambda_D=O(D\log D)\) is QP.
- Modular powering by \(\Lambda_D\), divisor stripping, and all
  prime-divisor screens use QP-many operations on QP-bit exponents.
- Trial division fully factors \(e\le C\) within QP cost. The relative scan
  uses \(C\) modular powers and gcds.
- The smooth-prefix scan uses at most \(X_D=2^{(\log n)^{O(1)}}\)
  candidates.
- The primary-part exponents, exact orders, their factorizations, residues,
  and provenance words have QP encoding length.

No hidden factorization of \(N\), unbounded recursion, exponential-in-\(n\)
table, or hidden-log computation enters the construction.

## Final disposition

F174 V2 establishes the exact operational law

\[
\text{proper factor}
\quad\lor\quad
\text{factored exact common-order state above }D
\quad\lor\quad
\text{polylog-small prime hard block}.
\]

The V1 wording defects are fully repaired. The proof is valid for arbitrary
odd prime-power decompositions, and the common-return construction needs no
hidden-log alignment. The remaining hard block is genuine missing progress;
this audit does not convert the trichotomy into deterministic or Las Vegas QP
factoring.
