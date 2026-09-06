# Hostile audit of F174 instrumented HH prime escape

## Verdict

**PASS, with the strict interpretations stated below.**

The factor / exact common-order state / hard-block trichotomy is correct for
arbitrary odd composite inputs. The proof covers repeated prime powers. The
smooth-prefix constants are sufficient. Every added operation has
deterministic quasipolynomial bit cost when the numerical targets and the
complete input transcript have quasipolynomial size. The F172 corollary is
also correct.

There are three nonoperative wording points.

1. The heading of Section 5 in `STATEMENT.md` says that the line-13 integer is
   outside *every* old local subgroup. Line 13 alone proves only that it is
   outside at least one of them. The displayed claims in that section say
   exactly this. On the final hard branch, the absolute-gcd-one condition
   proves that the integer is outside every local subgroup. The relative test
   at `e=1` independently proves the same fact. The final trichotomy uses only
   this stronger hard-branch fact.
2. “No exact common quotient order” must mean “no exact common quotient order
   is certified or returned.” The hard branch does not exclude the possibility
   that all unknown quotient orders are equal above the cap.
3. The closing reference to “unequal hidden orders” is valid on the F172
   corollary, where a common order above six is impossible. It is not an extra
   conclusion of the general hard branch.

These points do not alter a displayed hypothesis, displayed outcome, proof
step, cost bound, or corollary. They must remain attached to any use of this
PASS verdict.

## Frozen inputs and source basis

I verified the requested SHA-256 hashes before reading the proof:

- `STATEMENT.md`:
  `6f5ff26ad6e5735d60e85bb394b992b44e05698bee7c9d51d902a240205d5908`;
- `PROOF.md`:
  `614dbb1b0bb538353c2c919a5fa5778c8ff885c031992229ab1877db5a29ec98`;
- `SELF_AUDIT.md`:
  `387146e6cfe3dbfeac9a24fb67e6ea4473399c8cafb2316c6f1eb35daae047f6`.

All three hashes match the hashes supplied for this audit. I read those files
and `MANIFEST.md` in full. The manifest hash at audit time was
`cc415a7d75713e60553489085d7d2eca2ed506571b3b64fd29569e015b6a2eea`.

I checked the primary Harvey--Hittmeir source, arXiv:2601.11131v2,
*Deterministic methods for finding elements of large multiplicative order*:

<https://arxiv.org/html/2601.11131>

In particular, I read Algorithm 3.1, Lemmas 2.1--2.4, the full correctness
proof for Algorithm 3.1, and its complexity analysis. I also checked only the
promoted P150 common-relative-order lift and P154 one-block
absolute/relative-order and capacity interfaces. For the family corollary, I
read the complete F172 statement and proof. Their hashes were

- F172 `STATEMENT.md`:
  `d2ff244f1fb28e00ba262fdb89cd5a23b7b75954586bfb998ffd188db4a8ed9f`;
- F172 `PROOF.md`:
  `b23989a19a23653dab9946dca55888384a2c4493184878a3dfac68ec9c067a21`.

No research computation or factor-assisted check was used. The only local
calculation was the requested SHA-256 verification.

## 1. Primary Algorithm 3.1 exit audit

The candidate uses the published source order and line numbers correctly.

- **Line 2.** Harvey--Hittmeir fix an absolute lookup-table threshold. Their
  correctness proof says that a composite table entry returns a nontrivial
  divisor. F174 can enlarge that absolute threshold to cover its own finite
  inequalities.
- **Line 3.** The even return is outside F174's odd-input promise.
- **Line 4.** This return is unreachable. With
  \(n=\lceil\log_2(N+1)\rceil\) and \(D\ge n\), one has
  \(2^D\ge2^n\ge N+1>N\).
- **Lines 9--10.** The loop is exactly
  \(\beta=2,3,\ldots,\lceil D^{1/3}\rceil\). Above the fixed finite
  threshold, every tested \(\beta\) is smaller than \(N\). Therefore a
  returned divisor \(\beta\mid N\) is proper. A composite nonunit that does
  not itself divide \(N\) cannot reach the order search: one of its smaller
  prime divisors would already have triggered line 10.
- **Line 11.** A skipped value satisfies \(\beta^M=1\pmod N\), so its order
  divides the current exact state order. No state information is lost.
- **Lines 12--13.** Lemma 2.1 returns the exact order when it is at most the
  target and otherwise certifies \(\operatorname{ord}_N(\beta)>D\). F174
  intercepts exactly the latter return.
- **Lines 14--16.** The published loop uses every distinct prime divisor of
  the exact order. Since the order is exact modulo \(N\), the tested gcd can
  never equal \(N\). Every non-one result is therefore proper.
- **Lines 17--19.** Lemma 2.2 constructs an element of exact global order
  \(\operatorname{lcm}(M,m)\) and retains its factorization. Section 2 below
  proves that, on a no-factor branch, the same order is exact in every hidden
  prime-power component. Thus a line-19 return is F174 Outcome B.
- **Lines 20--22.** If the main loop ends, the published correctness proof
  gives \(M\mid p-1\) and \(p\le Z\) for every rational prime \(p\mid N\).
  The increasing arithmetic-progression scan therefore reaches the least
  prime divisor of composite \(N\), which is proper even when
  \(N=p^a\).
- **Line 23.** The published proof shows that this line is unreachable.

No source exit is removed or silently reclassified.

## 2. Exact common order in every prime-power component

Let \(m=\operatorname{ord}_N(\gamma)\) be an exact order found in the HH
loop. For every prime \(\ell\mid m\), a no-factor run has

\[
\gcd(\gamma^{m/\ell}-1,N)=1.
\]

Fix a rational prime \(p\mid N\), and put
\(m_p=\operatorname{ord}_p(\gamma)\). Since \(m_p\mid m\), if
\(v_\ell(m_p)<v_\ell(m)\) for any \(\ell\mid m\), then
\(m_p\mid m/\ell\). This would make the displayed gcd divisible by \(p\).
Hence every valuation agrees and

\[
m_p=m.
\]

Now take a full component \(R=p^a\parallel N\). Its local order is a
multiple of the order modulo \(p\) and a divisor of the exact global order
modulo \(N\). Thus

\[
\operatorname{ord}_{R}(\gamma)=m.
\]

This is the required repeated-prime-power step. It also shows
\(m\mid p-1\), so \(\gcd(m,N)=1\). A possible \(p\)-power order lift cannot
survive the prime-divisor gcd screens: its screen would expose at least a
proper power of \(p\).

The HH lcm word is also local. Its primary-component exponents depend only
on the known factorizations of the two exact orders. When both input orders
are the same in every hidden component, the constructed word has exact order
equal to their lcm in every component. Induction from \((g,M)=(1,1)\) gives

\[
\operatorname{ord}_{R_j}(g)=M,
\qquad
M\mid p_j-1,
\qquad
\gcd(M,N)=1
\]

at every no-factor loop state. Line 19 ensures \(M\le D\) whenever line 13
or the final scan is reached.

## 3. Line-13 prefix and primality attack

Suppose line 13 is first reached at \(\beta\). Every integer
\(2\le a<\beta\) had an earlier loop iteration.

- If line 11 skipped that iteration, the then-current order annihilated
  \(a\).
- Otherwise the exact order of \(a\) was at most \(D\), was found, passed
  the factor screens, and was merged into the accumulated lcm.

All later state orders are multiples of the earlier state orders. Therefore
the current state satisfies

\[
a^M=1\pmod N
\qquad(1\le a<\beta).
\]

Every such \(a\) is a unit. If a rational prime divided both \(a\) and
\(N\), its earlier prime loop iteration would have returned a factor.

If \(\beta=uv\) were composite with \(1<u,v<\beta\), then

\[
\beta^M=u^Mv^M=1\pmod N,
\]

contradicting the line-11 failure that led to the order search. Hence
\(\beta\) is prime. Line 10 also makes it a unit.

For \(R_j=p_j^{a_j}\), the odd prime-power unit group is cyclic. Because
\(M\mid p_j-1\), the kernel of the \(M\)-power map has exactly \(M\)
elements. It is the unique subgroup of order \(M\), namely
\(H_j=\langle g\rangle\). Thus every earlier integer lies in every
\(H_j\).

At this point \(\beta^M\ne1\pmod N\) proves only

\[
\beta\notin H_j
\quad\text{for at least one }j.
\]

It does not prove this for all \(j\). This is the precise qualification to
the Section 5 heading noted in the verdict. If the procedure reaches the
hard branch, then \(G_1=1\), so \(\beta\notin H_j\) for every \(j\).

## 4. Smooth-prefix constants and factor scan

Put \(y=\beta-1\). No rational prime divisor \(p\mid N\) is at most \(y\),
because its prime loop iteration would already have returned it. Every
\(y\)-smooth positive integer at most \(p\) is therefore a product of primes
smaller than \(\beta\). The prefix congruence gives

\[
a^M=1\pmod p
\]

for every such integer. The integer \(p\) itself is not \(y\)-smooth, so the
counted integers give distinct nonzero residues. Since \(X^M-1\) has at most
\(M\) roots over \(\mathbf F_p\),

\[
\Psi(p,y)\le M.
\]

Now use the candidate's exact integers

\[
L=\lceil\log_2(2D)\rceil,
\quad
J=\lceil\log_2(L+1)\rceil,
\quad
H=8LJ,
\quad
X=2^H,
\quad
Y=H^2.
\]

If \(y\ge Y\), then, using natural logarithms,

\[
\log y\ge2\log H
>2\log\log X,
\]

because \(\log X=H\log2<H\). Also \(X\ge y\): the HH loop gives
\(y<D^{1/3}\), while already \(X\ge(2D)^8\). Thus the hypotheses
\(X\ge y\ge2\) and \(X\ge4\) of Harvey--Hittmeir Lemma 2.4 hold.

That lemma gives

\[
\begin{aligned}
\log\Psi(X,y)
&\ge \log X\left(1-\frac{\log\log X}{\log y}\right)\\
&>\tfrac12H\log2\\
&=4LJ\log2\\
&\ge4\log(2D)\\
&>\log D\\
&\ge\log M.
\end{aligned}
\]

The constants therefore have ample slack. If a prime divisor \(p\) exceeded
\(X\), monotonicity would give \(\Psi(p,y)>M\), a contradiction. Hence every
rational prime divisor of \(N\) is at most \(X\).

Section 2 gives \(p\equiv1\pmod M\). Scanning the integers
\(kM+1\le X\) in increasing order reaches the least rational prime divisor
of \(N\). It is a proper divisor, including on a repeated-prime-power input.
Therefore a no-factor escape has \(y<Y\), and integrality gives

\[
\beta=y+1\le Y.
\]

Finally,

\[
\log_2X=H=O(\log D\log\log D),
\qquad
Y=O((\log D\log\log D)^2).
\]

For a fixed QP target, \(\log D=(\log n)^{O(1)}\). Thus \(X\) is a QP
numerical scan bound and \(Y=(\log n)^{O(1)}\). This checks both the
constant calculation and the numerical, exponent-length, and bit-cost
interpretations of the QP claim.

## 5. Absolute-order screen

Let \(r_j=\operatorname{ord}_{R_j}(\beta)\) and

\[
\Lambda_D=\operatorname{lcm}(1,2,\ldots,D).
\]

The prime-power factorization of \(\Lambda_D\) contains exactly the prime
powers at most \(D\). Therefore

\[
r\mid\Lambda_D
\quad\Longleftrightarrow\quad
\sigma(r)\le D.
\]

For

\[
A_\beta=\gcd(\beta^{\Lambda_D}-1,N),
\]

partial equality in one CRT component, or modulo only part of a repeated
prime-power component, makes \(A_\beta\) a proper divisor.

If \(A_\beta=1\), no \(r_j\) divides \(\Lambda_D\). Hence

\[
\sigma(r_j)>D
\qquad\text{for every }j.
\]

If \(A_\beta=N\), the exact global order \(m\) divides the known factored
multiple \(\Lambda_D\). Divisor stripping computes \(m\) and its complete
factorization. Since \(m\) is exact globally,

\[
\gcd(\beta^{m/\ell}-1,N)
\]

cannot equal \(N\) for any prime \(\ell\mid m\). A non-one value is proper.
If all values are one, Section 2 applies again and proves

\[
\operatorname{ord}_{R_j}(\beta)=m
\quad\text{for every }j,
\qquad
\gcd(m,N)=1.
\]

The original line-13 certificate gives \(m>D\). Thus all three absolute
outcomes are exact, and the P154 preconditions are satisfied.

## 6. Relative-order screen and P150/P154 interfaces

Define

\[
e_j=\operatorname{ord}_{(\mathbf Z/R_j\mathbf Z)^\times/H_j}(\beta H_j).
\]

Because \(H_j\) is exactly the kernel of the \(M\)-power map,

\[
\beta^{eM}=1\pmod{R_j}
\quad\Longleftrightarrow\quad
e_j\mid e.
\]

Consider the ordered gcds

\[
G_e=\gcd(\beta^{eM}-1,N),
\qquad 1\le e\le C.
\]

A partial local return gives a proper factor, including when equality holds
modulo only part of a prime-power component. Suppose the first surviving
global return is \(G_e=N\). Then every \(e_j\mid e\). If some \(e_j<e\), the
earlier test at \(e_j\) would have been non-one: it would have been either a
proper factor or an earlier global return. Therefore

\[
e_j=e
\qquad\text{for every }j.
\]

The known factorization of \(M\), together with trial division of the
QP-bounded integer \(e\), gives a factored annihilating multiple \(eM\) for
\(\beta\). P150 divisor stripping and prime-divisor screens either factor
\(N\) or certify one exact order \(m\) for \(\beta\) in every component.
Inside a cyclic local unit group,

\[
e=\frac{m}{\gcd(m,M)},
\]

so

\[
\operatorname{lcm}(M,m)=Me.
\]

This identity allows shared prime divisors of \(M\) and \(m\). The P150
primary-component lcm word therefore has exact order \(L=Me\) in every
component. The line-13 certificate gives

\[
L\ge m>D.
\]

Also \(e\ne1\), because line 11 had already established
\(\beta^M\ne1\pmod N\). This is strict state growth.

If every \(G_e=1\), then \(e_j>C\) for every \(j\). The local fingerprint
\(\beta^M\) has exact order \(e_j\). Hence

\[
1,\beta^M,\ldots,\beta^{CM}
\]

are distinct in every component. Since \(H_j\subseteq\langle g,\beta\rangle\)
and the generated quotient has order \(e_j\),

\[
|\langle g,\beta\rangle_{R_j}|=Me_j\ge M(C+1).
\]

This is exactly the P154 capacity contract. It gives no exact quotient order
and no factor by itself.

## 7. Complete QP cost

The QP claim counts all numerical loops and all encoded integers.

- The primary HH call has the source's stated
  \(O(D^{1/2}\log D(\log\log D)^{-1/2}\log N)\) bit cost.
- The sieve through \(D\), the factorization of \(\Lambda_D\), and the
  encoded exponent have QP size. The loose bound
  \(\log_2\Lambda_D\le\log_2(D!)=O(D\log D)\) is sufficient.
- Divisor stripping uses only QP-many modular powers with QP-bit exponents.
- Trial division of \(e\le C\), the \(C\) relative gcds, and the P150
  primary-component word all have QP cost and QP provenance length.
- Section 4 proves that the new factor scan has at most \(X\) candidates,
  where \(X=2^{(\log n)^{O(1)}}\), and every candidate has polylogarithmic
  bit length. Division into the \(n\)-bit input remains QP.

All QP exponents are fixed independently of \(N\), as the parameter section
requires. No unlimited recursion, unbounded table, or hidden output-size
assumption enters this one-call theorem.

## 8. F172 corollary

For every F172 semiprime \(N=pq\),

\[
\gcd(p-1,q-1)=6.
\]

An ordinary element with exact order \(L\) in both hidden fields must satisfy

\[
L\mid p-1,
\qquad
L\mid q-1,
\]

and therefore \(L\mid6\). F174 Outcome B has exactly such a common local
order. If the target is chosen with \(D>6\), Outcome B is impossible on a
no-factor branch.

For all sufficiently large family members one can, for example, choose a QP
target with \(D\ge n>6\) and \(D<N-1\). The remaining exact output law is

\[
\text{proper factor}
\quad\lor\quad
\text{algorithm-selected polylog-small prime hard block}.
\]

On this family, the hard block's local orders cannot all be equal: equality
would itself give an ordinary common order above \(D>6\). Thus the statement's
family-specific hidden-mismatch wording is justified. The corollary still
does not locate that mismatch or factor the input.

## Final scope

The audit proves no more than the frozen trichotomy and its F172 corollary.
In particular, the hard branch can contain equal unknown local orders on a
general composite, and capacity is not an exact order. Nothing here closes
the hard quotient, transfers order to a torus, reaches the F170 CRT
threshold, or gives deterministic or Las Vegas QP factoring.
