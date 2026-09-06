# F217 hostile audit

## Verdict

**PASS.** I found no false claim, missing premise, quantifier error, or
scope inflation in the frozen candidate. The packet proves conditional
decoders and boundaries for named explicit models. It does not provide the
missing divisor-coefficient evaluator and does not claim an unconditional
factoring algorithm.

## Authentication

I authenticated every frozen input before reading it.

| File | Recomputed SHA-256 | Expected | Result |
|---|---|---|---|
| `STATEMENT.md` | `f6bada7e65dc7c6617760cb1ce1e7b87618953cea6f46d11dc0d1fd8416e384d` | same | PASS |
| `PROOF.md` | `16946a7a8d2c6adc869524b9e27d15b2317bfb4336688a5bc5e960dafce82e5a` | same | PASS |
| `SELF_AUDIT.md` | `b9eb6001d741da1905efae8b363a27306fe25d7da6c0b4732a4fbed5c102ff99` | same | PASS |
| `PROVENANCE.md` | `e266737a3860eff054202d5834836526d3340898ac1200841081c3f0044f7709` | same | PASS |
| `MANIFEST.md` | `c41a76f0faabb51c151e468690a4502fba016e4140db485a9e900c1ee684dee5` | same | PASS |

No external source is cited in the packet. I rederived the standard
eta-quotient, Eisenstein, Ramanujan-sum, and Hecke facts used below. No
computation was needed.

## Hostile checks

### 1. Setup and exact range

From (N=2K+1=pq), one has (pq\equiv1\pmod K), while reduction of
(2K=pq-1) modulo either hidden prime proves that both primes are units
modulo (K). Thus (q\equiv p^{-1}\pmod K) is valid.

The claimed exception is exhaustive. Balance with (p=3) forces
(q=5), hence (N=15). If (p\ge5), then (q\ge7) and

\[
2(K-p-q)=(p-2)(q-2)-5\ge10.
\]

Therefore (0<p+q<K) except at (N=15). Separately,
(2(K-q)=q(p-2)-1>0), so both hidden primes are represented by their
least positive residues modulo (K), including at (N=15).

### 2. The (2r-1) trace decoder

I tried to break the decoder through coordinate degeneracy, independent
sign choices, and insufficient numerical precision.

For one coordinate, two different inversion orbits satisfy

\[
|2\cos(2\pi a/m)-2\cos(2\pi b/m)|
=4|\sin(\pi(a+b)/m)\sin(\pi(a-b)/m)|\ge16/m^2.
\]

Neither sine can vanish unless (a\equiv\pm b\pmod m). Hence monotonic
search on (0\le a\le\lfloor m/2\rfloor) recovers the coordinate orbit
without enumerating (m) points. A certified implementation can treat
overlap with the tested candidate as equality; distinct candidates have
disjoint error intervals at the requested precision.

For two active coordinates, the two relative signs differ by

\[
4|\sin(2\pi a_{i_0}/m_{i_0})
  \sin(2\pi a_i/m_i)|\ge16/(m_{i_0}m_i).
\]

Activity is exactly what makes both factors nonzero. One cross trace per
other active coordinate therefore aligns every sign with the anchor.
Self-inverse coordinates have no sign choice. Reversing the anchor gives
only global inversion.

Since every (m_i<K<2^n), all relevant gaps exceed
(2^{4-2n}). The evaluator error (2^{-4n-20}), with equally accurate
certified cosine values, is more than sufficient. The query count is
(r+(r-1)), and

\[
2^r\le\prod_i m_i=|G|<2^n,
\]

so (2r-1\le2n-1). The supplied forward map then returns the two least
residues (p,q), whose product is checked exactly.

The cyclic decomposition, its inverse coordinate map, succinct character
encodings, and the coefficient evaluator are all explicit additional
premises. The theorem never derives discrete logarithms or characters
from `factor(K)` alone.

### 3. Tautological ring residue

The map ([a]\mapsto a\bmod K) is multiplicative because the basis of
(\mathbb Z[G]) multiplies by the group law. Thus it is a genuine ring
map, not an illicit linear substitution. It gives

\[
\Theta_K(\mathcal A_N)
\equiv1+p+q+N
\equiv2+p+q\pmod K.
\]

The range check above makes the least residue after subtracting two equal
to the integer (p+q), except for the explicitly handled input (15).
The quadratic (X^2-(p+q)X+N) then recovers and verifies both factors.
The theorem identifies an evaluator target but does not evaluate it.

### 4. Moving Eisenstein weight

Because (K>1) is odd, (arphi(K)) is even and
(k=\varphi(K)+2\ge4) is an allowed even level-one weight. Every
(d\mid N) is a unit modulo (K), so Euler's theorem gives

\[
d^{k-1}=d^{\varphi(K)+1}\equiv d\pmod K.
\]

The normalization

\[
\mathcal G_k=-\frac{B_k}{2k}E_k
=-\frac{B_k}{2k}+\sum_{m\ge1}\sigma_{k-1}(m)q^m
\]

therefore has the exact claimed coefficient and residue. No reduction of
the rational constant term is used.

For each odd prime power (ell^e\Vert K),

\[
\frac{\ell^e}{\varphi(\ell^e)^2}
=\frac{\ell^{2-e}}{(\ell-1)^2}\le1,
\]

so (arphi(K)\ge\sqrt K=2^{\Omega(n)}). The dense weight-space state
is therefore numeric-exponential. Also
(N^{k-1}\le\sigma_{k-1}(N)\le4N^{k-1}), which proves the asserted
(\Theta(kn))-bit exact output. The binary weight and a residue modulo
(K) still have only (O(n)) bits. These are correctly separated cost
notions.

### 5. Prime-level eta quotient

For prime (r=K\ge7), the eta exponents are (r_1=r) and
(r_r=-1). Their weight is (w=(r-1)/2), and the two transformation
congruences are

\[
\sum\delta r_\delta=0,
\qquad
\sum(r/\delta)r_\delta=r^2-1\equiv0\pmod{24}.
\]

The eta-quotient character has square class (r^{-1}), which is the
same rational square class as (r). Hence on (Gamma_0(r)) it is

\[
\chi_r(d)=\left(\frac{(-1)^w r}{d}\right).
\]

The expansion at infinity has order zero. Direct application of the eta
transformation under the Fricke matrix gives, up to a nonzero constant,

\[
F_r|_wW_r=\eta(r\tau)^r/\eta(\tau),
\]

whose leading exponent is ((r^2-1)/24>0). Prime level has only these
two cusps, and eta has no upper-half-plane zeros. Thus the modularity and
holomorphy claims have no missing cusp or pole.

The prime-square coefficient congruence also checks exactly. For
(1\le j<r),

\[
\frac{(-1)^j}{r}\binom rj\equiv-j^{-1}\pmod r.
\]

It follows that

\[
\frac{(1-x)^r}{1-x^r}
\equiv1-r\sum_{j=1}^{r-1}\sum_{h\ge0}j^{-1}x^{j+hr}
\pmod{r^2}.
\]

After multiplication over (x=q^a), every product of two nonconstant
corrections vanishes modulo (r^2). If (r\nmid m), each divisor
(a\mid m) gives the unique decomposition
(m/a=j+hr), and
(j^{-1}\equiv a m^{-1}\pmod r). Therefore

\[
-[q^m]F_r/r\equiv m^{-1}\sigma_1(m)\pmod r.
\]

The congruence first establishes divisibility by (r), so the division
uses an integer representative modulo (r^2), not an inverse of (r).
At (m=N=2r+1), (m^{-1}\equiv1\pmod r), giving the claimed factor
transition. The logarithmic derivative also has the correct chain-rule
factor and sign:

\[
-r^{-1}q\frac d{dq}\log F_r=L(q)-L(q^r).
\]

### 6. Twisted Ramanujan channel

For (Re(s)>0), the bound
(|c_m(n)|\le\sigma_1(n)) gives absolute convergence. Expanding
(c_m(n)), writing (m=ek), and using complete multiplicativity of a
Dirichlet character gives

\[
\sum_{m\ge1}\frac{\chi(m)c_m(n)}{m^{s+1}}
=A_{\chi,s}(n)
 \sum_{k\ge1}\frac{\chi(k)\mu(k)}{k^{s+1}}
=\frac{A_{\chi,s}(n)}{L(s+1,\chi)}.
\]

For (m<p), one has ((m,N)=1), hence
(c_m(N)=\mu(m)). At (m=p),

\[
c_p(N)-\mu(p)=(p-1)-(-1)=p,
\]

and (chi(p)\ne0). Thus the first nonzero factor-sensitive term is
exactly (chi(p)p^{-s}). Balance gives (p=2^{\Omega(n)}), so a
sequential termwise evaluation reaches exponentially many positions.
The packet limits the (s=0) nonprincipal statement to an Abel limit or
analytic continuation and makes no ordinary-convergence claim there.

### 7. Named-model, bit-cost, and recursion scope

At good index, the direct upper-triangular Hecke representatives are
indeed indexed by (ad=N) and (0\le b<d), so there are
(sigma_1(N)\ge N) of them. The diamond operator depends only on the
index modulo (K), and is therefore trivial at (N\equiv1\pmod K);
the packet does not confuse it with (T_N).

The standard Manin-symbol presentation has

\[
|\mathbb P^1(\mathbb Z/K\mathbb Z)|
=K\prod_{\ell\mid K}(1+1/\ell)\ge K,
\]

and the standard weight-(k) symmetric-power module has dimension
(k-1). The packet consistently calls these named-model materialization
counts, not general lower bounds.

For a representation factoring through the abelian group (G), the
matrix identity

\[
\sum_{d\mid N}\rho(d)=2I+\rho(p)+\rho(p)^{-1}
\]

is exact. The character-decomposition observation is restricted to a
characteristic-zero splitting field and does not exclude nonabelian
extensions.

Finally, a one-child recurrence

\[
T(n)\le T(n-1)+2^{C(\log(n+1))^k}
\]

has at most (n) summands and remains quasipolynomial after adjusting a
fixed constant. F217 grants `factor(K)` and does not claim an all-input
recursive construction, so no hidden branching bound is needed inside
this packet.

## Residual scope

The surviving gap is exactly as stated: none of the proved identities
constructs a QP random-access evaluator for the relevant divisor
coefficient. Standard dense state and sequential summation are ruled out
only as implementations of the named models. No general circuit lower
bound, no all-input factorer, and no consequence from `factor(K)` alone
is asserted.

