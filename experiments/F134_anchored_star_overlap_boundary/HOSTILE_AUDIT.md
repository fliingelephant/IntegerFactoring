# F134 hostile audit — anchored-star overlap boundary

## Verdict

**PASS, with a strict scope interpretation.** The exact theorems are correct.
The three certificates are arithmetically correct. The factor-free kernel
claim and duplicate-value normalization are also correct.

The overlap law applies to the fresh cofactors

\[
H_i=w+NA_i,
\]

not to the full exact values \(P_i=qH_i\). The full values all contain the
common anchor \(q\). Therefore a sentence such as “different arms cannot
share a prime larger than \(B\)” is false if “arms” means the full values
\(P_i\). The precise displayed theorem and proof consistently use \(H_i\),
so this wording ambiguity does not invalidate the candidate.

F134 remains a local pruning theorem. It is not a source-success theorem, a
closure theorem, a non-global-root theorem, or a factoring algorithm.

## Frozen input

The audit read all three input files before testing the claims. It did not
edit them.

- `STATEMENT.md` SHA-256:
  `40354e169ef8632c206bd653819b3d0d117c670f134e18ff2f4558bc191c9483`
- `PROOF.md` SHA-256:
  `ca9fb0dc855fb032258908854e20f85da9851ba0777a5461382438f2839e5f3a`
- `MANIFEST.md` SHA-256:
  `c9ea1ea73dc2979966a4c5d284641eede2e76639c11f321a7c1d635c6041e034`

The statement and proof hashes agree with the hashes declared in the
manifest. The manifest omits its own hash by design.

## Audit protocol

The audit used this sequence.

1. Re-derive the canonical exact-value identity and endpoint normalization.
2. Re-derive the gcd law without using the supplied proof.
3. Rebuild the full star kernel over rational-prime parity rows.
4. Separate even and odd selected-column counts.
5. Test the private-row and factor-free claims.
6. Prove duplicate exact-value deletion at the level of the normalized-root
   map.
7. Recompute every integer, gcd, factor parity, and root in the three
   certificates.
8. Exhaustively check the overlap and square-dependency laws for all odd
   \(3\le N<90\), all unit \(2\le q<N\), and \(1\le B\le7\).
9. Attack the boundary between a literal F133 star, a generalized
   exact-value star, and a later all-block feedback transcript.

The proof verdict does not depend on the finite check.

## Exact mathematical checks

### 1. Canonical exact values and endpoints

Since \(qw=1+kN\),

\[
q(w+NA_i)=1+(k+qA_i)N.
\]

Thus every \(P_i=qH_i\) is positive and is \(1\) modulo \(N\). If

\[
P_i=c_i z_i,
\qquad 1\le c_i,z_i<N,
\]

then \(P_i\) is a unit modulo \(N\). Hence both endpoints are units and
\(c_i z_i\equiv1\pmod N\). The interval \([1,N-1]\) contains one inverse,
so \(z_i=\iota_N(c_i)\).

This is an existence statement for a displayed endpoint presentation. It
does not give a factor-free procedure that discovers an arbitrary new split
\(P_i=c_i z_i\).

### 2. Exact overlap law

For distinct digits,

\[
H_j-H_i=N(A_j-A_i).
\]

Also \(H_i\equiv w\pmod N\), and \(w\) is a unit. Therefore

\[
\begin{aligned}
\gcd(H_i,H_j)
&=\gcd(H_i,N(A_j-A_i))\\
&=\gcd(H_i,A_j-A_i).
\end{aligned}
\]

The digits are distinct in \([0,B]\), so

\[
1\le |A_i-A_j|\le B.
\]

No prime larger than \(B\) divides two different \(H_i\). The large
squarefree kernels of the \(H_i\) are therefore pairwise coprime.

### 3. Even/odd star-kernel law

Let \(a=\nu(q)\) and \(h_i=\nu(H_i)\). The exact-value column is

\[
p_i=a+h_i.
\]

For a selected-column vector \(x\), put \(t(x)=\sum_i x_i\). Then

\[
Mx=t(x)a+\sum_i x_i h_i.
\]

This proves the kernel identity. Above \(B\), the supports of the \(h_i\)
are disjoint.

- If \(t(x)=0\), each selected restricted vector \(h_i\) must be zero.
- If \(t(x)=1\), the selected disjoint supports must partition the support
  of \(a\) above \(B\).

Consequently,

\[
\prod_{i:x_i=1}\operatorname{sf}_{>B}(H_i)
=
\operatorname{sf}_{>B}(q)^{t(x)}.
\]

This includes the empty dependency. It also includes higher prime
valuations. Only their parity is used.

### 4. At most one odd coset

The map \(t:K\to\mathbb F_2\) is linear. Its kernel is
\(K_{\rm even}\), and its image has dimension at most one. If an odd
\(x_0\in K\) exists, every odd element is uniquely in

\[
x_0+K_{\rm even}.
\]

Thus the coset statement is exact. It is a statement about one common
anchor vector. It does not apply to a union of stars with different
anchors.

### 5. Private rows and factor-free decoding

Let \(r>B\). If \(v_r(q)\) is even and \(v_r(H_i)\) is odd, the \(r\)-row
of the full star matrix contains one entry: column \(i\). Every star-only
kernel vector therefore has \(x_i=0\).

For an even kernel vector, the common anchor contribution cancels. Any odd
large-prime row of a selected \(H_i\) is then private among the residual
arm vectors. This gives the stated containment for \(K_{\rm even}\).

P66 joint gcd-free refinement preserves the exact rational-prime parity
kernel. It does not need to name or factor \(r\). Thus the kernel statement
is factor-free. If numerical \(B\) is quasipolynomial in the input bit
length, trial removal of all primes at most \(B\), followed by one exact
square test, is also quasipolynomial. After this removal, the cofactor is a
square exactly when \(\operatorname{sf}_{>B}(H_i)=1\).

Old retained columns invalidate star-only privacy exactly as stated. Their
row vector can cancel the single new occurrence.

### 6. Exact-value deletion and normalized roots

Different digits give different exact integers because

\[
P_i=qw+qNA_i
\]

is strictly increasing in \(A_i\).

For an old and a new copy of the same exact value \(P\), merge their two
binary coefficients by addition. This maps the duplicated-column kernel
onto the single-column kernel. The additional kernel direction selects the
two copies. Its exact positive root is \(P\), and

\[
P\equiv1\pmod N.
\]

Its normalized root is therefore \(+1\). Removing the duplicate exact
column preserves the normalized-root image.

This does not authorize removal of the new endpoint presentation before
screens and refinement. A second presentation can expose new endpoint
blocks even when its exact-value column is redundant.

## Scope attack

### 1. Literal F133 unreduced star

For a literal F133 arm,

\[
c_\ell=\ell q,
\qquad
z_\ell=\frac{w+NA_\ell}{\ell},
\qquad
P_N(\ell q)=q(w+NA_\ell).
\]

The digit satisfies \(0\le A_\ell<\ell\le B\). Different retained exact
values have different digits. Therefore, after first-occurrence exact-value
deduplication, the F134 theorem applies to the retained F133 exact-value
star. Dividing \(H_i\) by the small prime \(\ell\) in the endpoint
presentation does not change any exact-value parity conclusion. It also
cannot remove a prime larger than \(B\).

F134 does not inherit the F133 row-reuse theorem. F133 concerns a large row
already present oddly in \(q\). F134 controls the fresh \(H_i\) rows inside
one fixed star.

### 2. Generalized exact-value star

F134 permits any distinct digits in \([0,B]\), provided a retained value
has some canonical endpoint presentation below \(N\). This class is larger
than one literal F133 prime-anchor scan. The overlap and parity laws hold for
this larger class, but the theorem does not prove that a declared source
will generate every such presentation.

Certificates A and C are certificates in this generalized sense. At
\(B=1\), there is no F133 prime-anchor bank. Certificate B is also stated
with \(B=1\), although its nonzero value can occur from the literal
\(\ell=3\) anchor when the F133 cutoff is at least \(3\).

### 3. Multi-round all-block reachability

Certificate C begins from the retained canonical presentation

\[
1520=38\cdot40.
\]

Given that presentation, joint refinement exposes \(19\), and feeding
\(19\) creates the second \(19\)-incident value. The certificate does not
prove that a bare-\(N\) source must first generate \(38\cdot40\). It proves
the conditional loss of privacy once that presentation is in the
transcript.

This is sufficient to refute permanent star-only privacy. It is not a
multi-round source-reachability theorem.

### 4. Exact counterexample to the broad overlap wording

At Certificate A,

\[
P_0=126,
\qquad
P_1=576.
\]

Both full values share primes \(2\) and \(3\), although both primes are
larger than \(B=1\). They share them through the common anchor \(q=18\).
In contrast,

\[
H_0=7,
\qquad
H_1=32,
\qquad
\gcd(H_0,H_1)=1.
\]

Thus the correct statement is:

\[
\boxed{
\text{different fresh cofactors }H_i\text{ share no prime larger than }B.
}
\]

The statement's displayed theorems use this correct form. The candidate must
not promote the broader full-value reading.

## Certificate reconstruction

### Certificate A: \(N=25\)

The audit obtained

\[
18\cdot7=126=1+5\cdot25,
\qquad
18\cdot32=576=24^2=1+23\cdot25.
\]

All four endpoint screen gcds are \(1,25,25,1\). Also

\[
q=2\cdot3^2,
\qquad
H_1=2^5.
\]

The odd \(2\)-valuations cancel. The decoded root is
\(24\equiv-1\pmod{25}\). The odd anchor coset can therefore give only a
global root.

### Certificate B: \(N=143\)

The audit obtained

\[
28\cdot46=1288,
\qquad
28\cdot189=84\cdot63=5292=3\cdot42^2,
\]

and

\[
102\cdot136=13872=3\cdot68^2.
\]

The six endpoint screen gcds are all \(1\). The two closing values have
positive joint root

\[
R=3\cdot42\cdot68=8568.
\]

Direct calculation gives

\[
\gcd(R-1,143)=13,
\qquad
\gcd(R+1,143)=11.
\]

Also \(H_1=3^3\cdot7\), so
\(\operatorname{sf}_{>1}(H_1)=21\). The useful dependency is a genuine
old/new closure, not an even star-only dependency.

### Certificate C: \(N=49\)

The audit obtained

\[
16\cdot46=736,
\qquad
16\cdot95=38\cdot40=1520,
\]

and

\[
19\cdot31=589.
\]

The six named endpoint screens all have gcd \(1\) with \(49\). The values
\(1520\) and \(589\) are distinct, and both have odd \(19\)-valuation.
Thus the first-star private row has degree at least two after the stated
second feed. No square dependency is claimed or implied.

## Finite independent check

An independent Python integer-arithmetic pass returned
`ALL ALGEBRA AND CERTIFICATE CHECKS PASSED`.

It checked all displayed certificate products and gcds. It also enumerated
all odd \(3\le N<90\), all unit \(2\le q<N\), all \(1\le B\le7\), every
digit pair, and every subset of the full digit set \(\{0,\ldots,B\}\).
For every square subset product, it verified the exact high-squarefree
identity.

This finite pass is only a regression check. The verdict rests on the exact
proof above.

## Surviving result and remaining gap

The surviving theorem is precise:

\[
\boxed{
\text{one retained fixed-anchor star cannot pair fresh primes above }B
\text{ across different }H_i.
}
\]

This blocks one local large-prime amortization argument. It leaves all of the
important feedback mechanisms open:

1. parity-smooth fresh cofactors;
2. the one odd anchor coset;
3. old/new cross-layer cancellation;
4. presentation-level refinement; and
5. later promotion of a newly exposed block.

No success probability, forced 2-core, forced dependency, useful root, or
all-input factoring result follows.
