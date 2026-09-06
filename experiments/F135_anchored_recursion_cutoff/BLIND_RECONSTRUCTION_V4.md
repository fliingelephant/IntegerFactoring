# F135 blind reconstruction V4 — PASS

## Isolation record

This audit used one research file.

| File read | SHA-256 |
|---|---|
| `/Users/zhou/autoresearch/IntegerFactoring/experiments/F135_anchored_recursion_cutoff/STATEMENT.md` | `b03002c70c97e38506f6e0c4fc4585e4e5268ec59c2b3557f8f3600dd837ef02` |

The hash matches the expected hash. I did not read a proof, manifest, audit,
ledger, or any other F135 or project file. The task supplied the applicable
workspace instructions directly. I did not open them from disk. All arithmetic
checks used inline programs with no data-file inputs.

I use the canonical meanings forced by the statement:

\[
\iota_N(x)\in\{1,\ldots,N-1\},\qquad
x\iota_N(x)\equiv1\pmod N,\qquad
P_N(x)=x\iota_N(x).
\]

## Common identity

For an eligible prime \(\ell\), put \(A=A_\ell\). The two endpoints satisfy

\[
0<\ell q<N,
\qquad
0<H_\ell=w+NA<\ell N,
\qquad
0<z_\ell=H_\ell/\ell<N.
\]

Moreover,

\[
(\ell q)z_\ell=qH_\ell
=qw+qNA
=1+(k+qA)N.
\tag{A}
\]

Thus \(z_\ell=\iota_N(\ell q)\) and
\(P_N(\ell q)=qH_\ell\). This proves the setup identity without using a
prior result.

## Theorem 1

If \(A=0\), then \(H_\ell=w\). Equation (A) gives

\[
P_N(\ell q)=qw=P_N(q).
\]

This is equality of integers, not only equality modulo \(N\).

If \(A>0\), then \(H_\ell=w+NA>N\). Since \(\ell\le B\),

\[
z_\ell=H_\ell/\ell>N/\ell\ge N/B.
\]

Finally, both \(z_\ell\) and \(\ell q\) lie in the canonical interval.
Equation (A) is symmetric in these endpoints. Hence

\[
\iota_N(z_\ell)=\ell q,
\qquad
P_N(z_\ell)=z_\ell\ell q=P_N(\ell q).
\]

The proof uses the complete endpoint only. It gives no size bound for a
proper factor of \(z_\ell\), and it says nothing about wrapped, powered, or
multi-block input. The stated exclusions are necessary.

**Result:** all parts and both strict inequalities pass.

## Theorem 2

First,

\[
\gcd(H_i,N)=\gcd(w,N)=1.
\]

Therefore

\[
\begin{aligned}
\gcd(H_i,H_j)
&=\gcd(H_i,H_j-H_i)\\
&=\gcd(H_i,N(A_j-A_i))\\
&=\gcd(H_i,A_j-A_i).
\end{aligned}
\]

Every digit lies in \(\{0,\ldots,B-1\}\). Distinct digits therefore give

\[
1\le |A_i-A_j|<B.
\]

If \(d=\gcd(z_i,z_j)\), then \(d\mid H_i\) and \(d\mid H_j\). Hence

\[
d\mid\gcd(H_i,H_j),
\qquad d<B.
\]

No relation between \(\ell_i\) and \(\ell_j\) is used. In particular, the
claim correctly states divisibility rather than equality after division.

**Result:** the identity, constant \(B\), and denominator-free claim pass.

## Theorem 3

### Gcd-free residual claim

For an occupied digit \(A\), every anchor prime in \(\mathcal L_A\) divides
\(H_A\). Complete refinement separates that prime because the retained
presentation contains both \(q\) and \(\ell q\), while
\(\gcd(\ell,q)=1\). Thus all \(\ell\)-adic content for named anchors is
supported on the named anchor-prime blocks. After those blocks are removed,
the reciprocal-side prime-power content is supported on

\[
R_A=H_A\bigg/\prod_{\ell\in\mathcal L_A}
\ell^{v_\ell(H_A)}.
\]

Every remaining reciprocal-side gcd-free block therefore divides \(R_A\).
This argument does not put a block that occurs only in \(q\) into \(R_A\).
The one-sided scope in the statement is exact.

### Release thresholds

Since \(S_A\ge L_A\), for \(A=0\),

\[
R_0\le H_0/L_0=w/L_0<N/B
\quad\text{when }L_0>B.
\]

For \(A>0\), use \(A\le B-1\) and \(w<N\):

\[
H_A=w+NA<NB.
\]

Consequently,

\[
R_A\le H_A/L_A<NB/B^2=N/B
\quad\text{when }L_A>B^2.
\]

The strict thresholds \(B\) and \(B^2\) are sufficient. They also explain
why the statement makes no claim at or below those thresholds. If \(R_A=1\),
only named anchor-prime powers remain. If \(R_A>1\), its gcd-free pieces are
positive divisors of a number below \(N/B\).

### Reconstruction of the constant 25

Let

\[
\theta(x)=\sum_{p\le x}\log p,
\qquad
\psi(x)=\sum_{p^j\le x}\log p.
\]

The following elementary bound is enough:

\[
\theta(x)>\frac{6x}{25}
\quad (x\ge 64^3).
\tag{B}
\]

To verify it, take \(m=\lfloor x/2\rfloor\). The central binomial
coefficient gives

\[
\frac{4^m}{2m+1}
\le {2m\choose m}
\le e^{\psi(2m)}.
\]

Also, all terms in \(\psi(x)-\theta(x)\) have base prime at most \(\sqrt x\).
Each such prime contributes at most \(\log x\). Thus

\[
\theta(x)
\ge (x-2)\log2-\log(x+1)-\sqrt{x}\log x.
\tag{C}
\]

After subtracting \(6x/25\), the right side of (C) is
\(112387.907\ldots>0\) at \(x=64^3=262144\). Its derivative is
\(0.439006\ldots>0\) there. The two negative derivative terms decrease in
magnitude as \(x\) increases. This proves (B) on the full required range.

Let \(E\) be the product of all eligible primes at most \(B\). The omitted
prime logarithms are at most \(\log\operatorname{rad}(Nq)\le\log(Nq)\).
Since

\[
q<N/B,
\qquad N<2^n,
\qquad B=n^3,
\]

we get

\[
\begin{aligned}
\log E
&=\theta(B)-\sum_{\substack{p\le B\\p\mid Nq}}\log p\\
&>\frac{6B}{25}-2n\log2+\log B.
\end{aligned}
\tag{D}
\]

Under the no-release assumptions, each eligible prime occurs in exactly one
digit bucket, so

\[
E=\prod_A L_A\le B(B^2)^d=B^{2d+1}.
\tag{E}
\]

Combine (D) and (E), use \(B=n^3\), and cancel \(3\log n\):

\[
6d\log n>rac{6n^3}{25}-2n\log2.
\]

Therefore

\[
d>rac{n^3}{25\log n}-\frac{n\log2}{3\log n}.
\]

This reconstructs the exact constant and the strict sign in (12).

### Reused large-prime row

For each occupied nonzero digit, select one anchor and write its exact value
as \(V_A=qH_A\). Distinct digits give distinct positive integers \(V_A\).
If a prime \(r>B\) divides two different \(H_A\), Theorem 2 would give
\(r<B\), a contradiction. Thus at most one occupied nonzero digit has
odd \(v_r(H_A)\); in fact, at most one has positive \(v_r(H_A)\).

If \(v_r(q)\) is odd, then \(v_r(V_A)\) is odd exactly when
\(v_r(H_A)\) is even. At least \(d-1\) distinct deduplicated exact values
therefore retain an odd \(r\)-entry, unless an earlier direct screen ends the
process with a factor.

The alternatives now follow exactly. A threshold bucket has either a proper
reciprocal-side block below \(N/B\), or \(R_A=1\). If there is no threshold
bucket, (12) supplies the stated number of distinct columns. Column count
and row reuse alone do not imply a dependency.

**Result:** the residual support, thresholds, constant 25, valuation count,
and trichotomy pass.

## Theorem 4

Order rows and columns by the same parent-before-child order. The entry
\((r_v,C_v)\) is one. The only other entry of \(C_v\) is in an earlier row,
namely the parent row. The matrix is therefore upper unitriangular. It is
square, has determinant one over \(\mathbf F_2\), and has zero column kernel.

An internal row occurs in its own column and in its \(b\) child columns. Its
degree is \(b+1\). After the common parent row is removed from one star, the
child columns have distinct singleton child rows. Leaf rows initially have
degree one. Removing their columns makes the parent-level rows degree one.
Induction on the depth deletes every column.

The vertex count is the geometric sum

\[
V=1+b+\cdots+b^T=\frac{b^{T+1}-1}{b-1}.
\]

If \(\log b=O(\log n)\) and \(T=O((\log n)^2)\), then

\[
\log_2 V=O(T\log b)=O((\log n)^3),
\]

which is equivalent to (15).

This is a valid incidence countermodel to any inference based only on the
listed local degrees, fresh-row disjointness, depth, and transcript size.
It has no arithmetic realization, so it cannot refute the complete
canonical source.

**Result:** all five matrix properties, both size formulas, and the stated
scope pass.

## Theorem 5

### CRT compatibility and infinitude

All ten CRT moduli are pairwise coprime. Their product and combined residue
are

\[
M=12522249183293850,
\qquad
a=4364121389770277.
\]

Direct reduction of \(a\) gives, in the order in (18) and (19),

\[
(2,36,86,60,1;\ 2,2,5,4,1).
\]

Also, \(\gcd(a,M)=1\). Thus the CRT class is a reduced odd residue class.

For a direct infinitude construction, choose primes

\[
P\equiv1\pmod M,
\qquad Q\equiv a\pmod M.
\]

The prime number theorem in arithmetic progressions supplies both primes in
\([X,(1+\varepsilon)X]\) for every fixed \(\varepsilon>0\) and all
sufficiently large \(X\). Hence there are infinitely many choices with
\(P/Q\to1\). They are odd and distinct because the two reduced classes are
different. Their product satisfies \(PQ\equiv a\pmod M\). Their least factor
is \(\Theta(\sqrt N)\), so it eventually exceeds any fixed polynomial in the
bit length. This verifies the balanced and trial-hard scope.

As a finite check, the following independently prime pair gives one member:

\[
\begin{aligned}
P&=187833737749407751=15M+1,\\
Q&=154631111589296477=12M+a,\\
PQ&=29044939662163320046609257500793227.
\end{aligned}
\]

Here \(P/Q=1.2147215\ldots\), and \(PQ\bmod M=a\). Primality was checked
both by the deterministic 64-bit Miller--Rabin base set and by OpenSSL's
prime checker.

### Exact inverse certificate

For the five seed rows, the congruences modulo \(q_v^2\) give

\[
1+k_vN\equiv q_v\pmod {q_v^2}.
\tag{F}
\]

Thus \(C_v/q_v\) is integral and \(v_{q_v}(C_v)=1\). Also
\(k_v<q_v\), so \(0<C_v/q_v<N\). For all sufficiently large family
members, \(q_v<N\). It follows that

\[
P_N(q_v)=C_v.
\]

The four edge carries are exact:

\[
2+5(1)=7,
\quad 2+5(3)=17,
\quad 7+11(1)=18,
\quad 17+19(1)=36.
\tag{G}
\]

The edge CRT residues give

\[
1+7(2)=15\equiv0\pmod3,
\quad
1+17(2)=35\equiv0\pmod7,
\]

\[
1+18(5)=91\equiv0\pmod {13},
\quad
1+36(4)=145\equiv0\pmod {29}.
\tag{H}
\]

For an edge with parent \(u\), (G) also gives

\[
C_v=q_u(w_u+NA),
\]

so \(q_u\ell\mid C_v\). The four endpoint divisors and carries obey

\[
(q_u\ell,k_v)=(15,7),(35,17),(143,18),(551,36).
\]

In every pair, \(k_v<q_u\ell\). Thus \(C_v/(q_u\ell)\) is the canonical
inverse of \(q_u\ell\). This proves every equality in (20).

The carries \(2,7,17,18,36\) are distinct. Hence the five integers
\(C_v=1+k_vN\) are distinct.

### Valuation and rank certificate

Reducing columns \((C_0,\ldots,C_4)\) modulo the squared row primes gives

\[
\begin{array}{c|ccccc}
 &C_0&C_1&C_2&C_3&C_4\\ \hline
5^2  &5&15&10&12&23\\
11^2 &73&11&8&44&87\\
19^2 &173&242&19&105&209\\
23^2 &121&421&492&23&45\\
37^2 &3&8&18&19&37
\end{array}
\]

Every divisible entry is a nonzero multiple of its row prime modulo the
prime square. Its valuation is exactly one. Every other entry has valuation
zero. Reducing these valuations modulo two gives exactly matrix (21). It is
upper triangular with unit diagonal, so its column rank is five.

Within the five selected columns, row 23 has only \(C_3\), and row 37 has
only \(C_4\). Remove those columns. Row 11 then has only \(C_1\), and row
19 has only \(C_2\). Remove those columns. Row 5 then has only \(C_0\).
Additional prime rows in these values do not change any named-row degree.

### Endpoint screens and strict scope

Every left endpoint in (20) belongs to the fixed set

\[
\{5,15,11,35,19,143,23,551,37\}.
\]

If a prime factor \(p\mid N\) divides
\(x-\iota_N(x)\), then \(p\mid x^2-1\). If it divides
\(x+\iota_N(x)\), then \(p\mid x^2+1\). The factors \(P,Q\) in the
family tend to infinity, while all these integers \(x^2\pm1\) are fixed.
The sign screens are therefore one for all sufficiently large members.

The rank certificate applies to the selected columns. It does not control
unselected source columns or their incidence with the named rows. The seeds
are fixed. Nothing here creates growing P121 rows or a non-global normalized
root. All four scope warnings in the statement are valid.

**Result:** the CRT class, infinite semiprime family, nine exact identities,
distinctness, parity matrix, rank, peel order, endpoint screens, and scope
pass.

## Refutation attempts and final gate

I checked the following possible failure modes.

- Boundary digits do not weaken Theorem 2. All digits are below \(B\).
- Empty buckets do not enter \(S_A\) or \(R_A\), and their product convention
  does not affect the counting argument.
- Anchor prime powers cannot leak into the claimed non-anchor residual after
  complete refinement. Retained \(q\) and \(\ell q\) presentations isolate
  \(\ell\).
- The excluded primes dividing \(Nq\) do not break (12). Their total
  logarithmic weight is bounded by \(\log(Nq)\), which produces exactly the
  correction term in (12).
- Extra rows cannot create a kernel among the five selected CRT columns
  because the displayed submatrix already has full column rank.
- Unselected columns can prevent the selected peeling sequence in the full
  source. The theorem explicitly excludes that stronger claim.
- The abstract tree has zero kernel but is not canonical arithmetic data.
  The selected CRT family is canonical arithmetic data but is not a complete
  source. Neither object proves a negative complete-source result.

The remaining-gate list is consistent with these reconstructions. Complete
endpoint recursion is inert by Theorem 1. A positive result must add a
release, a non-unary operation, old-column closure, or another arithmetic
invariant. A negative result must extend the canonical construction to the
complete source.

## Verdict

**PASS.** I found no false theorem, constant, CRT condition, certificate, or
scope claim in the supplied statement.
