# F225 hostile audit

## Verdict

**PASS for Theorems A--C in their stated scalar scope.** I could not refute
the local decompositions, the root bounds, the exact CRT laws, the BHP
family, or the exponential bank bound.

There is one nonblocking literal defect in the ancillary screening sentence.
After a uniform residue is gcd-screened, the full no-proper-factor branch is
not exactly uniform on `U(N)`: it also contains `x=0`, for which
`gcd(x,N)=N`. The exact unit statement is true after conditioning on
`gcd(x,N)=1`, or after rejecting and resampling `x=0`. This defect does not
change any theorem bound; the `x=0` branch has probability `1/N` and cannot
produce a proper gcd of `H_N(0)=0`.

## 1. Frozen-input authentication

I authenticated the candidate before reading it. All five SHA-256 hashes
match `FROZEN_MANIFEST.md` exactly.

| File | Manifest and computed SHA-256 |
|---|---|
| `STATEMENT.md` | `57a0764b549a79a5a725612b95a6f57b41791760bc6a1a2d188354041d6b1a20` |
| `PROOF.md` | `b6f9feb7d2dfe9cb9a0829e750defdd1a2a1025c7c42523671b4a6a6ea35c03a` |
| `SELF_AUDIT.md` | `8da3567fe6671c7f12604d9557e041815908bb5146ba878f037243e0a6c90dd6` |
| `RESULT.md` | `7ef7c9ee3ecc8620061c75982cc6c3998e5cfb0fe633ceb96e2fdb089fd7c2c8` |
| `PROVENANCE.md` | `6c49d5cfe74bf0af6aa9c416bfa22d04dfa5f4223cbd693305fcf525c02b5416` |

No frozen input was changed.

## 2. Frobenius and exponent reconstruction

Let `N=pq`, `d=q-p`, and `c=2p-q=p-d`.

Modulo `p`, every `a` satisfies

\[
a^{pq}=(a^p)^q=a^q=a^{p+d}=a^{d+1}.
\]

The last equality also holds at `a=0`; it is not a Fermat-only reduction.
Applying it to `a=x+1` and `a=x` gives

\[
H_N(x)=(x+1)^{d+1}-x^{d+1}-1\pmod p.
\]

Modulo `q`, the corresponding identity is

\[
a^{pq}=(a^q)^p=a^p,
\qquad
H_N(x)=(x+1)^p-x^p-1\pmod q.
\]

Both reductions hold at `x=0,-1`. Since `p,q` are odd, `d=q-p` is even,
`d+1` and `p` are odd, and

\[
H_N(0)=0,
\qquad
H_N(-1)=0
\]

in both fields. Also `c=2p-q` is odd. Under `c>=3`,

\[
k=c-2\ge1,
\qquad
s=(c+1)/2\ge2
\]

are integers. There is no hidden parity exception.

## 3. The `p`-side root set

The exponent identity is exact:

\[
d+1=p-c+1=(p-1)-(c-2)=(p-1)-k.
\]

For `x` outside `{0,-1}`, both denominators are nonzero, so Fermat gives

\[
(x+1)^{d+1}-x^{d+1}-1
=(x+1)^{-k}-x^{-k}-1.
\]

Multiplication by `[x(x+1)]^k` is reversible on this domain and gives

\[
P_k(x)=x^k-(x+1)^k-[x(x+1)]^k.
\]

Thus clearing denominators loses no admissible root and introduces no root.
The only excluded field elements are `0,-1`, and both are genuine roots of
the original local scalar.

The product term has degree `2k` and leading coefficient `-1`. The other
terms have degree at most `k<2k`. Hence `P_k` is nonzero and has degree
exactly

\[
2k=2(c-2).
\]

The exact decomposition and bound follow:

\[
A_p=2+\#\{x\notin\{0,-1\}:P_k(x)=0\}
\le 2+2k=2c-2.
\]

## 4. The `q`-side character cells

From `q=2p-c`,

\[
p=(q-1)/2+s,
\qquad s=(c+1)/2.
\]

For nonzero `y`, Euler's criterion gives exactly

\[
y^p=\chi(y)y^s.
\]

Every `x` outside `{0,-1}` has one and only one pair

\[
(\epsilon,\delta)=(\chi(x+1),\chi(x))\in\{\pm1\}^2.
\]

On that cell the local-root equation is exactly

\[
Q_{\epsilon,\delta}(x)
=\epsilon(x+1)^s-\delta x^s-1=0.
\]

The cell conditions make the four counted sets disjoint. A field element
cannot be double-counted even if it happens to be a root of more than one
unrestricted `Q` polynomial. The exceptional points are not in any cell,
because one character argument is zero there; they are added once each as
the two genuine roots proved above.

The degree accounting also survives:

- If `epsilon=-delta`, the `X^s` coefficient is
  `epsilon-delta=+2` or `-2`. It is nonzero because `q` is odd. These two
  polynomials have degree `s`.
- If `epsilon=delta`, the leading terms cancel and the `X^(s-1)`
  coefficient is `epsilon*s`. Since `q>p` implies `c<p`, we have
  `2<=s<q`. Thus this coefficient is nonzero modulo `q`. These two
  polynomials have degree `s-1`.

Bounding each cell by the degree of its polynomial gives

\[
A_q\le2+2s+2(s-1)=4s=2c+2.
\]

This argument does not assume that the four unrestricted polynomial root
sets are disjoint. Only the character-cell subsets must be disjoint, and
they are.

## 5. Exact CRT XOR laws

For a uniform residue modulo `N`, CRT gives independent uniform coordinates
in `F_p` and `F_q`. A proper gcd occurs exactly when one local scalar is zero
and the other is nonzero. Therefore the two disjoint XOR events give

\[
\Pr(1<\gcd(H_N(x),N)<N)
=\frac{A_p}{p}\left(1-\frac{A_q}{q}\right)
+\frac{A_q}{q}\left(1-\frac{A_p}{p}\right).
\]

For a uniform unit, CRT instead gives independent uniform coordinates in
`F_p^*` and `F_q^*`. Restriction to a unit removes the root `0` and no other
local point. In particular, `-1` remains. Hence the exact conditioned law is

\[
\frac{A_p-1}{p-1}\left(1-\frac{A_q-1}{q-1}\right)
+\frac{A_q-1}{q-1}\left(1-\frac{A_p-1}{p-1}\right).
\]

Dropping the complementary factors gives the claimed upper bounds:

\[
\frac{2c-2}{p}+\frac{2c+2}{q}\le\frac{4c}{p},
\]

and

\[
\frac{2c-3}{p-1}+\frac{2c+1}{q-1}
\le\frac{4c-2}{p-1}.
\]

The only exactness issue is the separate screening sentence noted in the
verdict. For a uniform residue,

\[
\Pr(1<\gcd(x,N)<N)=\frac{p+q-2}{pq}=O(1/p).
\]

The remaining cases are `gcd(x,N)=1`, which is exactly uniform on `U(N)`,
and `x=0`, which has `gcd(x,N)=N`. Treating `x=0` separately proves the same
`O(c/p)` obstruction without the inaccurate literal identification of the
whole no-proper-factor branch with `U(N)`.

## 6. BHP construction and quantifiers

The cited paper and DOI are correct: Baker, Harman, and Pintz, *The
Difference Between Consecutive Primes, II*, Proceedings of the London
Mathematical Society 83 (2001), 532--562,
[DOI 10.1112/plms/83.3.532](https://doi.org/10.1112/plms/83.3.532).
Its large-`x` conclusion is uniform over every sufficiently large real
endpoint. It is not a statement about a special subsequence of endpoints.

The publisher's abstract phrases the result in the forward form
`[y,y+y^0.525]`. This also gives the frozen backward form without changing a
constant: for a sufficiently large `X`, put `y=X-X^0.525`. Then `y` is
sufficiently large and

\[
y+y^{0.525}<X,
\]

so the guaranteed prime lies in `[X-X^0.525,X]`. The previously authenticated
F222 primary-source audit also records Theorem 1 directly in this backward
form.

Now take any sufficiently large odd prime `p` and put

\[
X_p=2p-\lfloor p^{3/5}\rfloor.
\]

Because `X_p=Theta(p)`, it is above the absolute BHP threshold for every
sufficiently large such `p`. Also

\[
X_p-X_p^{0.525}-p
=p-\lfloor p^{3/5}\rfloor-X_p^{0.525}>0
\]

eventually, while `X_p<2p`. Thus every BHP prime selected from this interval
satisfies `p<q<2p`; it is distinct from `p` and is odd.

The defect has the exact bounds

\[
\lfloor p^{3/5}\rfloor
\le c=2p-q
\le\lfloor p^{3/5}\rfloor+X_p^{0.525}.
\]

Since `X_p^0.525=O(p^0.525)=o(p^0.6)`, these bounds give

\[
c=\Theta(p^{3/5}),
\qquad
d=p-c=p-\Theta(p^{3/5})=\Theta(p).
\]

There is no hidden compatibility assumption on `p`. BHP applies after `p`
is chosen because it applies to every sufficiently large real `X_p`. Letting
`p` range over the unbounded sequence of all odd primes therefore produces
an infinite family. BHP supplies no promised class modulo `4`, and the
candidate correctly makes no such claim.

## 7. Bit length and the fresh-point bank

Balance gives

\[
p^2<N<2p^2.
\]

For `n=ceil(log_2 N)`, this is

\[
\log_2p=n/2+O(1).
\]

Consequently,

\[
p^{-2/5}=2^{-n/5+O(1)}=2^{-\Omega(n)}.
\]

Under the project's fixed numerical-QP convention,
`T(n)=2^{(log n)^{O(1)}}=2^{o(n)}`. Hence

\[
T(n)\,O(p^{-2/5})
=2^{-n/5+o(n)}
=2^{-\Omega(n)}.
\]

Independence between trials is unnecessary. Let `F_(i-1)` be the complete
previous transcript. If the next point is conditionally uniform in
`Z/NZ` or `U(N)` given every reached transcript, then its conditional
proper-gcd probability is bounded by the same `O(p^-2/5)`. For any fixed
numerical-QP trial cap, the conditional union bound gives the display above.

This is the exact adaptive scope. Marginal uniformity alone is insufficient.
The proof does not cover a point selected after inspecting its own scalar
value, a transcript-biased point law, or a bank that is not bounded by a
fixed numerical-QP envelope.

## 8. Scope that the proof does not reach

The proof bounds only the event that an individual scalar value is zero
modulo exactly one hidden prime. It does not justify an obstruction for:

- biased or carry-correlated evaluation points;
- joint processing of several typical nonzero values;
- coefficient vectors, resultants, ranks, or quotient-ring computations;
- a point chosen adaptively from the same value that will be tested;
- variable shifts; or
- any promised residue class modulo `4`.

No such extension is needed for the frozen conclusion, and none can be
inferred from its root counts.
