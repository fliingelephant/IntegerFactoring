# Hostile re-audit of F176 V2

## Verdict

**PASS.**

The V2 trichotomy is correct for every odd composite input, including
arbitrary products of repeated odd prime powers.  The absolute screen, the
small-common-order Mersenne branch, and the relative screen form a complete
standalone deterministic QP procedure.  Outcome C remains a genuine hard
branch, so this is not an integer-factoring theorem.

V2 no longer needs Harvey--Hittmeir or F174 as an external mathematical
premise.  It proves its own factor-first order-stripping lemma and uses only
the public base two, the public state \((-1,2)\), elementary order theory in
odd prime-power unit groups, and standard integer algorithms.  HH/F174 is
needed only to interpret Outcome C as the first possible hard source in the
older transcript.  P145 is also unnecessary; its promoted distinct-
semiprime scope would not by itself justify the all-input prime-power claim,
but V2 proves the sign step directly.

## Frozen inputs

I read the current V2 files in full and verified these SHA-256 hashes:

- `STATEMENT.md`:
  `c7634a4c9a72552ce7d822857abe381623c343e8920dc3a859277913b260aac1`;
- `PROOF.md`:
  `fc135fcb02b13900a5e97b130c80e1596d09841bf2da5382d59739f0095c50b4`;
- `SELF_AUDIT.md`:
  `eebf70ce764bf8baf35f87448330a3ff31c6a9f15bf2b39cfefaf77453b34070`;
- `MANIFEST.md`:
  `939fc2bdf4be1f502dfa08410673dbdc64aaa089252b700a58909d5385af5c97`.

The preserved V1 files and V1 audit were not used as proof of V2.

## 1. Full factor-first stripping lemma

Let

\[
N=\prod_jR_j,
\qquad R_j=p_j^{a_j},
\]

and let \(d\) be a unit with \(d^E=1\pmod N\), where the complete
factorization of \(E\) is known.  At every stage, the current exponent is
an annihilator modulo every \(R_j\).

Fix a prime \(\ell\) dividing the current exponent.  The gcd

\[
H=\gcd(d^{E/\ell}-1,N)
\]

has exactly the required meanings.

- If \(H=N\), every local order divides \(E/\ell\), so replacing \(E\)
  by \(E/\ell\) preserves the global annihilator invariant.
- If \(1<H<N\), it is already a verified proper divisor.  This includes
  a congruence modulo only some CRT components and a congruence modulo only
  \(p_j^b\) with \(b<a_j\) inside one repeated prime-power component.
- If \(H=1\), no rational prime divisor of \(N\) divides the powered
  difference.  Thus no local order can divide \(E/\ell\).  Every local
  order retains the full current \(\ell\)-adic valuation.

Repeat the first case until it no longer occurs, for every prime in the
factored exponent.  On a no-factor branch, let \(m) be the final exponent
and \(m_j=\operatorname{ord}_{R_j}(d)\).  Each \(m_j\mid m\).  For every
prime \(\ell\mid m\), the retained gcd-one result forces

\[
v_\ell(m_j)=v_\ell(m)
\qquad\text{for every }j.
\]

Removing other prime-primary parts later cannot alter this equality.
Hence

\[
m_j=m
\qquad\text{for all }j.
\]

The remaining factorization of \(m\) is known.  Finally, if
\(\gcd(m,N)>1\), this gcd is proper: the common local order satisfies
\(m\le\varphi(R_j)<N\), including when \(N=R_j\) is one prime power.
Otherwise \((d,m)\) is an exact common-order state with
\(\gcd(m,N)=1\).  This proves the full lemma without a squarefree
assumption.

## 2. Absolute screen and the primary-order claim

The public lcm has factorization

\[
\Lambda_n=\prod_{\ell\le n}
\ell^{\lfloor\log_\ell n\rfloor}.
\]

Therefore, for every positive integer \(r\),

\[
r\mid\Lambda_n
\quad\Longleftrightarrow\quad
\sigma(r)\le n.
\]

Let \(r_j=\operatorname{ord}_{R_j}(2)\).  The three values of

\[
A=\gcd(2^{\Lambda_n}-1,N)
\]

are exhaustive.

- A proper value factors \(N\).
- If \(A=N\), every \(r_j\mid\Lambda_n\), so the stripping lemma returns
  a factor or one common exact value \(m\).
- If \(A=1\), no \(r_j\) can divide \(\Lambda_n\).  Otherwise the powered
  difference would be divisible by all of \(R_j\), hence at least by
  \(p_j\), contradicting the gcd-one result.  Thus

  \[
  \sigma(r_j)>n
  \qquad\text{for every }j.
  \]

The last implication is valid for a full prime-power order, not merely for
the reduced order modulo \(p_j\).

## 3. The complete \(m\le n\) branch

Suppose stripping returns the common exact order \(m\le n\).  Then every
prime-power component divides \(2^m-1\), so

\[
N\mid2^m-1.
\]

For odd \(N\) and
\(n=\lceil\log_2(N+1)\rceil\), one has \(N>2^{n-1}\).  If \(m<n\), then

\[
0<2^m-1\le2^{n-1}-1<N,
\]

contradicting divisibility by \(N\).  Therefore \(m=n\).  Also

\[
N\mid2^n-1,
\qquad
0<2^n-1<2N,
\]

so the quotient is one and

\[
N=2^n-1.
\]

If \(n\) is composite, trial division finds a prime \(\ell\mid n\).
Then \(n/\ell\ge2\), \(n/\ell<n\), and

\[
1<2^{n/\ell}-1<N,
\qquad
2^{n/\ell}-1\mid2^n-1=N.
\]

This is a proper factor, including when the input has repeated prime
factors.

If \(n\) is prime, the composite-input promise excludes \(n=2\), because
then \(N=3\).  Hence \(n\) is odd.  In every \(R_j\), the literal public
element two has order \(n\), while \(-1\) has order two.  These orders are
coprime and the unit group is abelian, so

\[
\operatorname{ord}_{R_j}(-2)=2n.
\]

Equivalently, \((-2)^n=-1\ne1\) and \((-2)^{2n}=1\), with
\(\operatorname{ord}_{R_j}(4)=n\).  This direct argument works unchanged
for odd prime powers.

The factorization \(2\cdot n\) is public.  Also \(N\) is odd and Fermat's
theorem gives

\[
2^n-1\equiv1\pmod n,
\]

so \(\gcd(2n,N)=1\).  Thus \((-2,2n)\) satisfies every part of Outcome B.

## 4. Relative quotient and first-return identity

Assume \(A=1\).  For every odd prime power \(R_j\), the only solutions of
\(x^2=1\pmod{R_j}\) are \(1\) and \(-1\).  Therefore the squaring map on
the unit group has kernel

\[
H_j=\langle-1\rangle.
\]

If \(e_j\) is the order of \(2H_j\) in the quotient, then

\[
e_j\mid e
\quad\Longleftrightarrow\quad
2^e\in H_j
\quad\Longleftrightarrow\quad
2^{2e}=1\pmod{R_j}.
\]

This proves the exact local interpretation of every relative gcd
\(G_e\).

Suppose the first non-one value in the ordered scan is \(G_e=N\).  Every
\(e_j\mid e\).  If some \(e_j<e\), the earlier scan at that positive
integer would already have been non-one, either a factor or a global
return.  Hence

\[
e_j=e
\qquad\text{for all }j.
\]

Now \(2e\) is a factored annihilating multiple for the literal element two.
The stripping lemma returns a factor or one common exact local order \(m\).
In an odd prime-power unit group, the unique order-two element is \(-1\).
Consequently

\[
e=\frac{m}{\gcd(m,2)}
\]

and therefore

\[
\operatorname{lcm}(2,m)=2e.
\]

If \(m\) is even, the literal element two has order \(m=2e\).  If \(m\)
is odd, the commuting product \(-2\) has order \(2m=2e\).  Thus the
candidate's public choice of \(h\) realizes the exact order in every
component.

The absolute gcd-one branch already gave
\(\sigma(m)>n\), so \(m>n\) and \(L=2e\ge m>n\).  The stripping lemma
either returned \(\gcd(m,N)\) as a factor or certified
\(\gcd(m,N)=1\).  Since \(N\) is odd,

\[
\gcd(L,N)=\gcd(\operatorname{lcm}(2,m),N)=1.
\]

The factorization of \(L=2e\) is known.

If all scanned gcds are one, an \(e_j\le C\) would make the test at
\(e=e_j\) divisible by \(p_j\).  Hence every \(e_j>C\).  Since the
absolute local order is at least its quotient order, every local absolute
order also exceeds \(C\).  This proves Outcome C exactly.

## 5. QP exponent lengths and operation count

The factorization of \(\Lambda_n\) is obtained by a sieve through \(n\).
The loose bound

\[
\log_2\Lambda_n\le\log_2(n!)=O(n\log n)
\]

is enough.  The procedure computes \(2^{\Lambda_n}\bmod N\) by modular
exponentiation; it never materializes the exponentially large exact power.
The number of prime-primary stripping steps and all their exponent bit
lengths are polynomial in \(n\).

The relative scan has

\[
C=2^{(\log n)^{O(1)}}
\]

iterations.  Each exponent \(2e\) has
\(O(\log C)=(\log n)^{O(1)}\) bits.  Trial division through
\(\sqrt e\le\sqrt C\), modular exponentiation, gcd computation, and all
state encodings therefore have deterministic QP bit cost.  The Mersenne
factor and the residue representing \(-2\) have at most \(n\) bits.

## 6. Complete-factor recursion

At a proper-factor exit, both the factor and complementary cofactor are
strictly between one and the current input.  The prime leaves of the full
binary recursion tree multiply to the original \(N\).  Since every leaf is
at least two, their number, counted with multiplicity, is at most

\[
\lfloor\log_2N\rfloor<n.
\]

A full binary tree with \(L\) leaves has \(2L-1<2n\) total nodes.
Deterministic polynomial-time primality testing supplies the leaf test.
At every child, its input length and QP caps are no larger than the original
uniform bounds.  Thus fewer than \(2n\) QP calls remain QP.  This count does
not assume squarefreeness.

## 7. Independence from HH, F174, and P145

The executable V2 procedure consists only of:

1. the absolute gcd with the public factored exponent \(\Lambda_n\);
2. factor-first stripping proved in V2;
3. the elementary Mersenne and sign branch;
4. the relative gcd scan against the public state \((-1,2)\); and
5. the same proved stripping lemma after a first global return.

No step calls HH, uses an HH representative, invokes the F174 smooth-prefix
cutoff, or assumes the disputed F174 statement that a raw escape is outside
every local subgroup.  No step invokes P145.  The phrase “every surviving
F174 hard escape is base two” is a corollary: if this standalone base-two
procedure is inserted before the later HH source loop, it has already
returned a factor, an above-\(n\) common state, or its base-two hard block.

## Final scope

This re-audit certifies the standalone V2 trichotomy and no more.  It does
not eliminate the normalized hard base-two block, localize unequal hidden
orders, or prove deterministic or Las Vegas QP factoring.
