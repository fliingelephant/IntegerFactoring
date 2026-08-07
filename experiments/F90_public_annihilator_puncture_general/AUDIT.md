# Hostile proof-only audit: PASS

The audited RESULT.md has SHA-256
96275cc1cb5b454722cc4ae18dead7ec8260d8c05e842f71709696afc19cc8f3,
which matches the pinned value.

I found no counterexample to the annihilator equivalence, primary puncture
theorem, exact exponent, rank-two size bound, public scan, fixed
specialization, or combined branch dichotomy. The hidden objects
\(p,q,\lambda,x,\ell,H,C\) occur only in the conditional correctness proof.
They are not used by the executable scan.

## 1. The public annihilator test is equivalent to
\(\lambda\mid N-1\)

Let \(M=N-1\). If every supplied generator satisfies \(g_i^M=1\), then for
every word

\[
y=\prod_i g_i^{a_i}\in K
\]

one has, using commutativity of the unit group,

\[
y^M=\prod_i(g_i^M)^{a_i}=1.
\]

This remains valid for negative word exponents because the generators are
units. Thus \(M\) kills every element of \(K\). By the definition of the
finite-group exponent, this is equivalent to

\[
\lambda=\exp(K)\mid M.
\]

Conversely, \(\lambda\mid M\) implies \(y^M=1\) for every \(y\in K\), and in
particular for every public generator. Redundant generators do not affect
either direction.

The condition is therefore public and exact. It does not require computing
\(\lambda\).

## 2. The primary puncture preserves an exact order-\(\ell\) separator

Let \(x\) be a positive separator and let

\[
\operatorname{ord}(x)=\ell^C s,\qquad \gcd(\ell,s)=1.
\]

Because \(\operatorname{ord}(x)\mid\lambda\mid N-1\), every prime-power
component of \(s\) occurs in \(N-1\) to at least the same valuation. With

\[
e=v_\ell(N-1),\qquad j=e-C+1,\qquad
E=(N-1)/\ell^j,
\]

one has

\[
v_\ell(E)=C-1.
\]

For every prime \(r\ne\ell\),

\[
v_r(E)=v_r(N-1)\geq v_r(s).
\]

Therefore

\[
\gcd(\operatorname{ord}(x),E)=\ell^{C-1}s
\]

and the standard power-order formula gives

\[
\operatorname{ord}(x^E)
=\frac{\operatorname{ord}(x)}
       {\gcd(\operatorname{ord}(x),E)}
=\ell.
\]

The identity coordinate of \(x\) remains the identity after powering. The
other coordinate has order \(\ell\), so it remains nonidentity. Hence
\(x^E\) is still a positive separator, now of exact order \(\ell\).

The inequalities

\[
1\leq C\leq H\leq e
\]

ensure \(1\leq j\leq e\). There is no invalid puncture-depth edge case.

## 3. Exact powered exponent and the rank-two bound

Decompose \(K\) into its primary components. For every prime
\(r\ne\ell\), the exponent \(E\) contains at least
\(r^{v_r(\lambda)}\), so the entire \(r\)-primary component is killed.
Thus \(K^E\) is an \(\ell\)-group.

On the \(\ell\)-primary component, write

\[
E=\ell^{C-1}u,\qquad \gcd(u,\ell)=1.
\]

Powering by \(u\) is an automorphism of a finite \(\ell\)-group. Powering
by \(\ell^{C-1}\) lowers every element order by at most that factor. Since
the original \(\ell\)-primary component has exponent \(\ell^H\), it contains
an element of order \(\ell^H\). Its image has order

\[
\ell^{H-C+1}.
\]

All image elements have order dividing this value. Therefore the exponent
is exactly, not merely at most,

\[
\boxed{\exp(K^E)=\ell^{H-C+1}}.
\]

Each local multiplicative group is cyclic, so its \(\ell\)-primary subgroup
is cyclic. The group \(K^E\) is a subgroup of a product of two cyclic
\(\ell\)-groups. Every such subgroup needs at most two generators. By the
classification of finite abelian \(\ell\)-groups,

\[
K^E\simeq C_{\ell^\alpha}\times C_{\ell^\beta}
\]

with either factor allowed to be trivial and
\(\alpha,\beta\leq H-C+1\). Hence

\[
\boxed{|K^E|\leq\ell^{2(H-C+1)}}.
\]

This is an upper bound, not an assertion that every image has the maximal
size. It is the correct uniform cap without graph or pure-phase structure.

## 4. Requested edge cases

### \(\ell=2\)

Nothing in the order calculation divides by two in the coefficient field or
uses oddness of \(\ell\). The two local \(2\)-primary unit subgroups are
cyclic, their product has generator rank at most two, and the same exponent
and size formulas apply. An order-two powered separator remains nonidentity
in exactly one coordinate.

### \(C<H\)

The puncture removes only \(C-1\) copies of \(\ell\). The residual exponent
is therefore the larger value

\[
\ell^{H-C+1}.
\]

The candidate does not incorrectly collapse it to \(\ell\). Its cap uses
the full square
\(\ell^{2(H-C+1)}\), exactly as required.

### Noncyclic \(K\)

No cyclicity of \(K\) is used. Primary decomposition is valid for every
finite abelian group, and the embedding into two cyclic local groups supplies
the rank-two bound. For example, the maximal possible powered image is a
product of two cyclic groups of the displayed exponent, which attains the
bound.

### Redundant generators

Testing more than a minimal generating set does not change the annihilator
equivalence. After powering, the redundant list still generates \(K^E\).
It adds duplicate breadth-first edges but no correctness problem.

### Extreme punctures

If \(C=1\) and \(e\) is large, then \(j=e\) and \(v_\ell(E)=0\); the
\(\ell\)-primary part is left unpowered up to an automorphism, with exponent
\(\ell^H\), matching \(H-C+1=H\). If \(C=H=e\), then \(j=1\) and the image
has exponent \(\ell\). Both boundary cases agree with the theorem.

## 5. Completeness of the public scan

The executable scan lists every prime \(\ell\leq L\) dividing the public
integer \(N-1\), computes the public valuation
\(e=v_\ell(N-1)\), and tries every \(1\leq j\leq e\). If a hidden separator
and prime satisfy the corollary, the public loop necessarily includes

\[
j=e-C+1.
\]

For this trial, Theorem 1 gives both:

\[
|K^E|\leq\ell^{2(H-C+1)}\leq T
\]

and \(x^E\in K^E\) as a positive separator.

Since the ambient unit group is abelian,

\[
K^E=\langle g_1^E,\ldots,g_m^E\rangle.
\]

A breadth-first multiplication closure from the identity therefore reaches
all of \(K^E\). For the successful exponent, at most \(T\) distinct residues
exist, so the “more than \(T\)” cap never fires. The queue closes after full
enumeration, and the separator is gcd-tested.

For a wrong exponent whose image has more than \(T\) elements, the search
stops on discovery of residue \(T+1\). Before that point, at most \(T\)
residues can have been dequeued and expanded. If the wrong image has at most
\(T\) elements, it is fully enumerated within the same bound. The exact
boundary \(|K^E|=T\) is complete because the stop condition is strict.

Every nontrivial gcd must be checked as

\[
1<d=\gcd(y-1,N)<N.
\]

Such a \(d\) divides \(N\) by construction and is an exact proper factor.
The identity residue merely gives \(d=N\) and is discarded.

## 6. Inverse-free enumeration, lookup, storage, and complexity

Forward multiplication by the powered generators suffices. In a finite
group, a generator's inverse is a positive power of that generator, so the
monoid generated by the list equals the subgroup generated by the list. If
the subgroup is large, the cap stops the traversal; if it is small, every
needed positive-power path has length below the number of group elements.

A deterministic balanced search tree keyed by the canonical residue gives
deterministic membership tests. At most \(T+1\) residues are retained in one
trial, so residue storage is

\[
O(T\log N)
\]

bits, plus polynomial tree and queue overhead.

There are at most \(L\) candidate integers through \(L\), and hence at most
\(L\) scanned primes. For each prime,

\[
e=v_\ell(N-1)<\log_2N.
\]

Thus there are \(O(L\log N)\) public trials. Each exponent is at most
\(N-1\) and has \(O(\log N)\) bits. Each capped traversal performs
\(O(mT)\) modular multiplications, \(O(T)\) gcds, and deterministic
dictionary operations.

Listing primes through numerical \(L\), testing divisibility of \(N-1\), and
computing valuations are deterministic polynomial-time operations when
\(L=\operatorname{poly}(\log N)\). If numerical \(T\), the generator count,
and generator encoding lengths are also polynomial in \(\log N\), the
complete scan and its storage are uniformly polynomial.

The condition requires the full value
\(\ell^{2(H-C+1)}\leq T\). Knowing only that \(H-C\) is polynomially bounded
would not control the image if \(\ell\) were numerically large. The
candidate states this restriction correctly.

## 7. Hidden proof data do not enter execution

The following executable values are public:

- \(N-1\);
- the supplied generator list;
- the bounds \(L,T\);
- the list of primes through \(L\) that divide \(N-1\);
- each public valuation \(v_\ell(N-1)\);
- every puncture exponent \((N-1)/\ell^j\); and
- every residue and gcd found during capped traversal.

The procedure neither computes nor branches on

\[
p,\ q,\ \lambda,\ x,\ \operatorname{ord}(x),\ H,\ C.
\]

It also does not select the successful prime or depth from hidden data. It
exhausts the bounded public menu. The hidden quantities appear only in the
existential proof that one menu entry has a small image containing a
separator.

The initial public branch test likewise uses only
\(g_i^{N-1}\bmod N\). It does not compute \(\lambda\).

## 8. The \(N=2047\) specialization

For

\[
N=2047,\qquad K=\langle11,2\rangle,
\]

the generator \(11\) has global order \(22\), and \(2\) has global order
\(11\). Hence

\[
\lambda=\operatorname{lcm}(22,11)=22.
\]

Since

\[
N-1=2046=22\cdot93,
\]

the public annihilator test passes.

The state is the strict pure-phase extension with old graph order \(22\) and
phase index \(11\). Each nonidentity element in either projection kernel has
order \(11\) and is a positive separator, so positive separators of order
\(11\) exist. For one such \(x\),

\[
\ell=11,\qquad
e=v_{11}(2046)=1,\qquad
H=v_{11}(22)=1,\qquad
C=v_{11}(\operatorname{ord}(x))=1.
\]

The successful public exponent is

\[
E=2046/11=186.
\]

The general theorem gives

\[
|K^{186}|\leq11^2=121.
\]

The exact pure-phase decomposition has an old powered graph of order \(11\)
and a retained phase group of order \(11\), with trivial intersection.
Therefore

\[
|K^{186}|=121.
\]

Both local images have order \(11\), so each projection kernel has size
\(11\). Their symmetric difference contains exactly

\[
11+11-2=20
\]

positive separators. The fixed specialization is correct.

## 9. The combined F89/F90 dichotomy

The branch test

\[
K^{N-1}=1
\]

is public and exhaustive.

For completeness, the rectangular claim in the other branch can be checked
directly. Put \(P=p-1\), \(Q=q-1\), and \(d=\gcd(P,Q)\). Since

\[
pq-1=q(p-1)+(q-1),
\]

one has

\[
\gcd(N-1,P)=d,
\qquad
\gcd(N-1,Q)=d.
\]

For each prime \(r\), removing the common minimum of
\(v_r(P),v_r(Q)\) leaves an \(r\)-component on at most one side. Therefore
the two projection orders of \(K^{N-1}\) are coprime. A subgroup of a product
of two finite groups of coprime orders that surjects onto both projection
images is the full product of those images. Hence \(K^{N-1}\) is a
rectangle.

If this rectangle is nontrivial, it contains a positive separator: choose a
nonidentity element in one nontrivial projection and the identity in the
other. If only one projection is nontrivial, the same statement still
holds. Thus the branch \(K^{N-1}\ne1\) has the claimed separator structure,
although efficient enumeration still requires the stated accessibility
condition.

In the branch \(K^{N-1}=1\), \(N-1\) is a public annihilator and the primary
puncture theorem applies conditionally when \(K\) already contains a
separator with a scanned, bounded primary image.

This dichotomy does not claim that either resulting image is polynomially
enumerable on every input. It is a public structural split, not a complete
factoring algorithm.

## 10. Scope judgment

The candidate correctly proves a conditional deterministic decoder for a
supplied subgroup in the annihilated branch. It does not create a separator,
bound a primary image on every input, or make an inaccessible rectangular
branch small. It proves no arbitrary-composite reduction or all-input
factoring algorithm.

Verdict: **PASS**.
