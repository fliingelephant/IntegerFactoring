# F41 kill-first: inverse-polynomial relative ACD noise is not automatically an LLL-decodable hint

## Verdict

The granted source is substantially stronger than the inverse-graph source in
P49, but the proposed conclusion still does **not** follow at the advertised
precision.

Let

\[
 N=pq,\qquad z_i=p t_i+r_i,\qquad |r_i|\le B,
 \qquad \epsilon:=B/p,
\]

where `p,q` are balanced distinct odd primes and the hidden `t_i` are
independent uniform elements of \(\{0,\ldots,q-1\}\).  The errors may be
adversarial functions of the whole quotient tuple, subject only to the stated
bound and \(0\le z_i<N\).

There are three different decoder scales.

1. **Approximation-denominator isolation.**  To isolate the designated
   denominator \(q\) from small simultaneous rational approximants at
   relative accuracy \(\epsilon\), the coarse inverse-polynomial-noise scale
   is

   \[
   m\asymp \frac{\log q}{\log(1/\epsilon)}.
   \]

   Below this scale, with the dimension-dependent factors stated in
   Proposition 2.2, Dirichlet approximation deterministically creates a
   coefficient not divisible by \(q\) whose lattice vector is shorter than
   the designated \(q\)-vector.  With a strengthened size condition it is
   even coprime to \(N\).  Above the corresponding approximation scale, a
   union bound excludes all smaller competing denominators with high
   probability.  These are not exact matching thresholds in every regime:
   the shorter-vector statement pays a \(\sqrt m\) factor.  For
   \(\epsilon=1/\operatorname{poly}(n)\), where
   \(n=\lceil\log _2N\rceil\), both calculations nevertheless have coarse
   order \(\Theta(n/\log n)\), not constant dimension.

2. **Ordinary LLL decoding.**  A completely explicit simultaneous-
   approximation lattice and the standard \(2^{m/2}\) LLL approximation
   guarantee give a rigorous polynomial-time decoder when, up to polynomial
   factors in `m` and the desired failure probability,

   \[
   \epsilon\lesssim q^{-1/m}2^{-m/2}.
   \]

   Optimizing over `m` gives

   \[
   \log _2(1/\epsilon)\ge (1+o(1))\sqrt{2\log _2q}.
   \]

   On balanced semiprimes this is
   \(\epsilon\le 2^{-(1+o(1))\sqrt n}\).  This is a genuine many-sample
   improvement over the one-sample small-root scale, and its lattice dimension
   is only \(\Theta(\sqrt n)\), so its bit complexity is polynomial.  It is
   nevertheless far smaller than inverse-polynomial relative precision.

3. **External one-sample divisor-Coppersmith benchmark.**  The standard
   univariate divisor-small-root theorem, imported only for comparison and
   not proved or used by the F41 result, recovers from
   \(B\le N^{1/4-\eta}\) for any fixed \(0<\eta<1/4\).  Formal multivariate
   determinant exponents are not, by themselves, a proof at growing
   \(m=\Theta(n/\log n)\): one must also control lattice dimension, LLL loss,
   algebraic independence, and root extraction.  No such claim is made here.

Consequently, the statement

> polynomially many samples with \(B=p/\operatorname{poly}(n)\) are enough for
> a known polynomial-time ACD/LLL decoder

is refuted as an inference from the standard constructions.  This result is
**not** an ACD hardness theorem and does not rule out a different decoder or an
error law with extra exploitable structure.  It is also conditional on being
given the approximate-multiple source; it does not construct that source from
bare `N`.

No computation was used.

---

## 1. Model and quantifiers

Write

\[
 n=\lceil\log _2N\rceil,
 \qquad C^{-1}\sqrt N\le p,q\le C\sqrt N
\tag{1.1}
\]

for a fixed balance constant `C`.  Assume throughout that \(1\le B<p/8\).
The value `B`, or a public upper bound within a constant factor of it, is an
input to the decoder.  A dyadic enumeration removes this convention at only a
polynomial overhead.

The probability space used below is precise:

* \(t_1,\ldots,t_m\) are independent and uniform modulo `q`;
* after seeing the entire tuple, an adversary may choose every `r_i`, provided
  \(|r_i|\le B\) and the displayed integer representative `z_i` lies in
  \([0,N)\);
* LLL and all later arithmetic may be deterministic.

Thus every success probability below is over the hidden quotients alone and is
uniform over all admissible bounded errors.  Independence of the errors is not
used.

Before any lattice work, one should compute

\[
 \gcd(N,z_i),\qquad \gcd(N,z_i-z_j)
\tag{1.2}
\]

for all `i,j`.  A proper gcd ends the algorithm.  These checks often catch
zero errors, equal errors, and other specially structured easy cases.  They
need not do so when the corresponding quotient is also equal: the gcd can be
\(N\) rather than a proper factor.  The lattice theorem does not assume that
these checks succeed.

Factoring `N` and recovering the designated hidden factor are slightly
different wordings.  The lattice naturally recovers the cofactor `q`; the
algorithm then returns \(p=N/q\).  Either proper factor is sufficient.

---

## 2. Approximation-denominator isolation, not factor identifiability

Strictly speaking, `N` already determines the unordered pair \(\{p,q\}\), so
information-theoretic uniqueness of its factors is vacuous.  The meaningful
question for a simultaneous-approximation decoder is whether the true
denominator `q` is isolated from all *publicly representable candidate
denominators*, most of which need not divide `N`.

Put

\[
 \alpha_i=\frac{z_i}{N}
 =\frac{t_i}{q}+\frac{r_i}{N},
 \qquad \|x\|_{\mathbb R/\mathbb Z}
 :=\min_{k\in\mathbb Z}|x-k|.
\tag{2.1}
\]

The true denominator obeys

\[
 \|q\alpha_i\|_{\mathbb R/\mathbb Z}
 =|r_i|/p\le\epsilon.
\tag{2.2}
\]

### Lemma 2.1 — simultaneous Dirichlet approximation with explicit size

For any real \(\alpha_1,\ldots,\alpha_m\) and any real \(A\ge2^m\), there is
an integer \(a\) with

\[
 1\le a\le A,
 \qquad
 \max_i\|a\alpha_i\|_{\mathbb R/\mathbb Z}
 \le 2A^{-1/m}.
\tag{2.3}
\]

**Proof.**  Let \(Q=\lfloor A^{1/m}\rfloor\).  The \(Q^m+1\) points
\(k(\alpha_1,\ldots,\alpha_m)\bmod1\), for
\(0\le k\le Q^m\), occupy `Q^m` equal axis-parallel boxes in the unit cube.
Two lie in one box.  Their index difference `a` is at most \(Q^m\le A\) and
has every circular coordinate at most \(1/Q\).  Since \(A^{1/m}\ge2\),
\(Q\ge A^{1/m}/2\).  This gives (2.3).  \(\square\)

This elementary lemma already locates the first obstruction.

### Proposition 2.2 — below the scale, the designated `q`-vector is not shortest

Let \(d=m+1\).  If

\[
 \left(\frac{2\sqrt d}{\epsilon}\right)^m
 <\frac{q}{2\sqrt d},
\tag{2.4}
\]

then for **every** observed transcript there are integers
\(1\le a<q\) and \(k_1,\ldots,k_m\) such that

\[
 \left\|(aB,az_1-Nk_1,\ldots,az_m-Nk_m)\right\|_2<qB.
\tag{2.5}
\]

In particular `q` does not divide `a`, while the natural factor vector has
length at least `qB`.  If, more strongly, there is an `A` satisfying

\[
 \left(\frac{2\sqrt d}{\epsilon}\right)^m
 <A<\min\!\left(p,\frac q{\sqrt d}\right),
\tag{2.4u}
\]

then the same shorter vector can be chosen with \(\gcd(a,N)=1\).

**Proof.**  Condition (2.4) permits an `A` satisfying

\[
 \left(\frac{2\sqrt d}{\epsilon}\right)^m<A<\frac q{\sqrt d}.
\tag{2.6}
\]

Apply Lemma 2.1 to the `alpha_i` in (2.1).  Choose each `k_i` nearest to
\(a\alpha_i\).  Then

\[
 |a|B<\frac{qB}{\sqrt d},
\]

and

\[
 |az_i-Nk_i|
 \le 2N A^{-1/m}
 <\frac{N\epsilon}{\sqrt d}
 =\frac{qB}{\sqrt d}.
\tag{2.7}
\]

All `d` coordinates have magnitude below \(qB/\sqrt d\), proving (2.5).
Also \(a<q\), so `a` cannot be a nonzero multiple of `q`.  Under (2.4u),
choose `A` in the displayed interval instead.  Then \(1\le a<p,q\), hence
\(\gcd(a,N)=1\).  \(\square\)

The relevant factor vector is

\[
 v_q=(qB,qz_1-Nt_1,\ldots,qz_m-Nt_m)
     =(qB,qr_1,\ldots,qr_m),
\tag{2.8}
\]

and hence

\[
 qB\le\|v_q\|_2\le qB\sqrt d.
\tag{2.9}
\]

Proposition 2.2 says that the designated \(v_q\) is not a shortest vector.
Under (2.4) alone, the shorter coefficient might be a multiple of `p`.  The
unit version (2.4u) supplies a certified nonfactor competitor, but even it
does not rule out a still-shorter factor-bearing vector.  Thus neither
version defeats an SVP algorithm which gcds its output.  Both only refute
identification of the designated \(v_q\) by shortestness; neither is a
hardness result.

Taking logarithms of (2.4) gives the dimension-dependent condition

\[
 m\!\left(\log(1/\epsilon)+\log(2\sqrt d)\right)
 <\log q-\log(2\sqrt d).
\tag{2.10}
\]

For inverse-polynomial \(\epsilon\), this covers every
\(m=o(n/\log n)\), and fixed balance gives the same coarse order for the unit
version.  The \(\tfrac12\log m\) term changes constant factors and is not
discarded in claims outside that regime.

### Proposition 2.3 — random quotients exclude smaller competitors

For \(0<\epsilon<1/8\), define a spurious denominator to be an integer
\(1\le a<q\) satisfying

\[
 \max_i\|a\alpha_i\|_{\mathbb R/\mathbb Z}\le\epsilon.
\tag{2.11}
\]

Uniformly over every admissible adversarial error rule,

\[
 \Pr[\text{a spurious denominator exists}]
 \le q\left(4\epsilon+\frac1q\right)^m.
\tag{2.12}
\]

**Proof.**  Fix `a`.  If (2.11) holds, then

\[
 \left\|\frac{a t_i}{q}\right\|_{\mathbb R/\mathbb Z}
 \le \epsilon+\frac{a|r_i|}{N}
 \le2\epsilon.
\tag{2.13}
\]

Because `q` is prime and \(1\le a<q\), multiplication by `a` permutes
\(\mathbb F_q\).  At most \(4\epsilon q+1\) residues obey (2.13).  The
conditions in (2.13) depend only on the individual `t_i`; hence independence
of the quotients gives probability at most
\((4\epsilon+1/q)^m\), even if the errors were chosen after seeing the whole
tuple.  Union-bound over fewer than `q` choices of `a`.  \(\square\)

Thus a sufficient approximation-denominator-isolation count is

\[
 m\ge
 \frac{\log(q/\delta)}
      {\log(1/(4\epsilon+1/q))}.
\tag{2.14}
\]

For \(\epsilon=n^{-c}\), Propositions 2.2 and 2.3 both point to the coarse
order \(m=\Theta(n/\log n)\).  They are not an exact matching threshold:
the strictly-shorter-vector argument contains the additional \(\sqrt d\)
loss in (2.10).  Both propositions concern approximation-denominator
geometry, not statistical factor identifiability or efficient recovery.

---

## 3. The explicit simultaneous-approximation lattice

Consider the full-rank integer lattice generated by the rows

\[
 \mathcal B=
 \begin{pmatrix}
 B&z_1&z_2&\cdots&z_m\\
 0&N&0&\cdots&0\\
 0&0&N&\cdots&0\\
 \vdots&\vdots&\vdots&\ddots&\vdots\\
 0&0&0&\cdots&N
 \end{pmatrix}.
\tag{3.1}
\]

Its determinant is

\[
 \det L=B N^m,
\tag{3.2}
\]

and every vector has the unique form

\[
 v(a,k_1,\ldots,k_m)
 =(aB,az_1-Nk_1,\ldots,az_m-Nk_m).
\tag{3.3}
\]

The factor vector (2.8) lies in `L`.  The determinant root is

\[
 (BN^m)^{1/d}.
\tag{3.4}
\]

For \(B=\epsilon p\), the ratio of the factor-vector scale `qB` to (3.4)
satisfies the exact identity

\[
 \left(\frac{qB}{(BN^m)^{1/d}}\right)^d=\epsilon^m q.
\tag{3.5}
\]

Thus, for balanced `p,q`, it is also true up to balance constants that

\[
 \frac{qB}{(BN^m)^{1/d}}
 \asymp (\epsilon^m p)^{1/(m+1)}.
\tag{3.6}
\]

This explains the volume heuristic often quoted for this route:
\(\epsilon^m p<1\), or
\(m\gtrsim\log p/\log(1/\epsilon)\), is needed merely to put the factor
vector below the generic determinant scale.  Proposition 2.2 supplies a
deterministic version of the obstruction rather than relying on that
heuristic.

The determinant calculation omits the algorithmic price of recognizing the
right short vector.  That price is decisive here.

---

## 4. A rigorous ordinary-LLL decoder

Use the following algorithm.

1. Perform the gcd checks (1.2).
2. Build (3.1) and run \(\delta=3/4\) LLL.
3. Let its first reduced vector be
   \(b_1=(aB,w_1,\ldots,w_m)\).
4. Compute \(g=\gcd(|a|,N)\).  If \(1<g<N\), return `g` and `N/g`;
   otherwise report failure.

The first coordinate is exactly divisible by `B`, so `a` is publicly
recoverable.  No hidden quotient or error is used.

### Theorem 4.1 — exact success bound

Set

\[
 d=m+1,
 \qquad \Gamma=2^{m/2},
 \qquad T=qB\sqrt d,
 \qquad R=\Gamma T,
 \qquad A=R/B=\Gamma q\sqrt d,
\tag{4.1}
\]

and

\[
 \theta=\min\left(1,\,4\Gamma\epsilon\sqrt d+\frac1q\right).
\tag{4.2}
\]

If

\[
 R<N
 \qquad\text{and}\qquad
 A<N,
\tag{4.3}
\]

then the algorithm returns a proper factor with probability at least

\[
 1-2A\theta^m.
\tag{4.4}
\]

This probability is uniform over all admissible bounded-error rules.

**Proof.**  Standard \(\delta=3/4\) LLL gives

\[
 \|b_1\|_2\le2^{(d-1)/2}\lambda_1(L)
 \le\Gamma\|v_q\|_2\le R.
\tag{4.5}
\]

Suppose a vector (3.3) has norm at most `R`, with \(a\ne0\) and
\(q\nmid a\).  Then \(|a|\le A\), and for every `i`,

\[
 |a p t_i+a r_i-pqk_i|\le R.
\tag{4.6}
\]

Consequently

\[
 \operatorname{dist}(a t_i,q\mathbb Z)
 \le\frac{R+|a|B}{p}
 \le\frac{2R}{p}.
\tag{4.7}
\]

For fixed `a` not divisible by prime `q`, the residue \(a t_i\bmod q\) is
uniform.  The number of centered residues allowed by (4.7) is at most
\(4R/p+1\), so the per-sample probability is at most

\[
 \min\left(1,\frac{4R/p+1}{q}\right)
 =\theta.
\tag{4.8}
\]

As in Proposition 2.3, the implication (4.7) removes the errors entirely, so
the quotient independence yields \(\theta^m\) even for a joint adversarial
error rule.  There are fewer than `2A` nonzero signed choices of `a` in the
range.  Thus, except on an event of probability at most \(2A\theta^m\), every
lattice vector of norm at most `R` has `q | a` or `a=0`.

A nonzero lattice vector with `a=0` has norm at least `N`, contradicting
\(R<N\).  Therefore the LLL output has `q | a`.  Finally \(0<|a|<N\) by
\(A<N\), so `a` cannot be divisible by both `p` and `q`.  Hence
\(\gcd(a,N)=q\).  \(\square\)

The theorem gives an exact, checkable sufficient condition.  For a desired
failure probability `delta`, put

\[
 u=\left(\frac{\delta}{2\Gamma q\sqrt d}\right)^{1/m}.
\tag{4.9}
\]

If \(u>1/q\), it is enough that

\[
 \epsilon\le
 \frac{u-1/q}{4\Gamma\sqrt d},
\tag{4.10}
\]

together with (4.3).  Up to constants, polynomial factors in `m`, and
\(\delta^{1/m}\), this reads

\[
 \boxed{\epsilon\lesssim q^{-1/m}2^{-m/2}m^{-1/2}.}
\tag{4.11}
\]

The two factors in (4.11) have different origins:

* \(q^{-1/m}\) is the simultaneous-approximant/union-bound threshold;
* \(2^{-m/2}\) is the ordinary LLL approximation loss.

Dropping the second factor is precisely the unjustified step that makes
inverse-polynomial relative error appear sufficient.

### Corollary 4.2 — an explicit polynomial-time many-sample regime

Fix \(\eta>0\).  On the balanced family (1.1), if

\[
 \epsilon\le2^{-(1+\eta)\sqrt n},
\tag{4.12}
\]

then taking

\[
 m=\left\lfloor(1+\eta/2)\sqrt n\right\rfloor
\tag{4.13}
\]

makes the failure probability in (4.4) \(2^{-\Omega_\eta(n)}\) for all
sufficiently large `n`.

**Proof.**  Write \(h=\log _2(1/\epsilon)\) and
\(L=\log _2q=n/2+O_C(1)\).  Ignoring only
\(O(m\log m)\) terms, the base-two logarithm of the right side subtracted in
(4.4) is bounded by

\[
 L+\frac{m^2}{2}-mh+O(m\log m).
\tag{4.14}
\]

With (4.12) and (4.13), its order-`n` coefficient is strictly negative;
the margin is \(\Omega_\eta(n)\).  Also
\(\Gamma\epsilon\sqrt d=2^{-\Omega_\eta(\sqrt n)}\), proving `R<N`, while
\(\Gamma\sqrt d<p\) proves `A<N`.  \(\square\)

More generally, (4.11) asks for

\[
 h\ge \frac{L}{m}+\frac m2+O\left(\log m+\frac{\log(1/\delta)}m\right).
\tag{4.15}
\]

The leading expression is minimized at
\(m=\sqrt{2L}\), with minimum \(\sqrt{2L}\).  Since
\(2L=n+O_C(1)\), the optimized ordinary-LLL boundary is

\[
 \epsilon\le2^{-(1+o(1))\sqrt n}.
\tag{4.16}
\]

### Bit complexity

The lattice has dimension \(m+1\), and every input entry has `O(n)` bits.
Classical exact-arithmetic LLL is polynomial in the dimension and input bit
length.  For \(m=\Theta(\sqrt n)\), construction, reduction, the `O(m^2)` gcd
preprocessing, and the final gcd therefore all take polynomial time in `n`.
The factor \(2^{m/2}\) affects the approximation guarantee, not the bit-
complexity class; its logarithm is only `O(m)`.

Every reported factor is verified by the final gcd and division.  Therefore,
if a source supplies fresh independent batches in polynomial time and the
right side of (4.4) is bounded below by an inverse polynomial, repeating
fresh batches gives a Las Vegas algorithm with polynomial expected running
time.  Corollary 4.2 has success tending to one.  This repetition statement
does not supply the missing bare-`N` source.

---

## 5. Why \(B=p/\operatorname{poly}(n)\) does not pass this proof

Let \(\epsilon=n^{-c}\), so
\(h=\log _2(1/\epsilon)=O(\log n)\).

First, Proposition 2.2 shows, in particular, that for

\[
 m\le \kappa_{c,C}\frac{n}{\log n}
\tag{5.1}
\]

for a sufficiently small fixed \(\kappa_{c,C}>0\), the designated
\(q\)-vector is not
the shortest vector of the natural lattice: Dirichlet supplies a strictly
shorter vector whose coefficient is not divisible by `q`.  Under the
strengthened condition (2.4u), available in the same coarse range on a fixed
balanced family, the competing coefficient is a unit.  The
dimension-dependent \(\sqrt m\) term in (2.10) determines the precise
constant boundary.

Second, at the dimension needed to escape (5.1), ordinary LLL has approximation
factor

\[
 2^{m/2}=2^{\Theta(n/\log n)},
\tag{5.2}
\]

whereas the relative accuracy margin is only polynomial.  The exact success
condition (4.10) is therefore missed by a superpolynomial factor.

The same conclusion follows by optimizing rather than fixing `m`.  The leading
exponent in (4.14) is

\[
 \frac n2+\frac{m^2}{2}-mh.
\tag{5.3}
\]

Its minimum over real `m` is
\(n/2-h^2/2=n/2-O(\log^2n)>0\).  Thus no choice of `m` makes the proved LLL
failure bound nontrivial in this regime.

This establishes two method boundaries:

* the designated low-dimensional \(q\)-vector is not shortest, and with
  (2.4u) a deterministic shorter unit vector exists;
* the stated high-dimensional LLL certificate requires
  \(2^{-\Theta(\sqrt n)}\), not inverse-polynomial, relative noise.

It does **not** establish that LLL can never work outside its worst-case
guarantee on some more special distribution.  It also does not establish that
no polynomial-time algorithm can exploit the samples.  Those would be ACD
average-case hardness claims, and no such claim has been proved here.

Exact SVP does not turn (5.1) into a polynomial-time route.  Known exact
enumeration in dimension `m` costs exponential time in `m`; restricting it to
\(m=O(\log n)\) for polynomial total time leaves the Dirichlet obstruction far
from the inverse-polynomial-noise approximation-isolation dimension.  This is a
complexity accounting statement about that approach, not a lower bound for
all SVP algorithms.

---

## 6. External one-sample small-root benchmark

This section imports the standard divisor form of the univariate Coppersmith
small-root theorem solely for comparison.  It is not proved here, is not used
in Theorem 4.1 or Corollary 4.2, and is not part of the self-contained F41
method boundary.

### Imported theorem 6.1 — linear small root modulo an unknown large divisor

Fix \(0<\beta\le1\) and \(\eta>0\).  Given `N`, a monic linear polynomial
\(f\in\mathbb Z[X]\), and the promise that an unknown divisor
\(p\mid N\) satisfies \(p\ge N^\beta\), every integer `r` satisfying

\[
 f(r)\equiv0\pmod p,
 \qquad |r|\le N^{\beta^2-\eta}
\tag{6.1}
\]

can be found deterministically in time polynomial in \(\log N\) for fixed
\(\beta,\eta\).  This is the imported theorem, not a derivation from an
unspecified shift lattice.

Apply it with \(f(X)=X-z_1\).  Since \(f(r_1)=-pt_1\), the balance constant
must be absorbed with slack rather than by silently taking \(\beta=1/2\).
For a target \(0<\eta<1/4\), set

\[
 \xi=\eta/4,\qquad \beta=1/2-\xi,qquad \eta'=\eta/4.
\]

Fixed balance gives \(p\ge C^{-1}\sqrt N\ge N^\beta\) for all sufficiently
large `N`, and

\[
 \beta^2-\eta'
 =\frac14-\frac\eta2+\frac{\eta^2}{16}
 >\frac14-\eta.
\]

Applying Imported Theorem 6.1 with theorem slack \(\eta'\) therefore gives
the comparison regime

\[
 B\le N^{1/4-\eta}.
\tag{6.3}
\]

For \(0<t_1<q\),
\(\gcd(N,z_1-r_1)=p\).  The endpoint `t_1=0` is detected as an unhelpful gcd
`N`; another independent sample avoids it with probability \(1-1/q\).

The imported theorem needs no random-quotient assumption but asks for
exponentially smaller relative error,

\[
 \frac Bp\le N^{-1/4-\eta+o(1)},
\tag{6.4}
\]

than the many-sample theorem in Corollary 4.2.  This benchmark is contextual;
the promoted F41 claim may simply omit it without changing any proof.

### Why a formal multivariate exponent is not enough

With many samples, the polynomials \(z_i-X_i\) all vanish modulo `p` at the
small error tuple.  Lattice determinant optimizations can suggest improving
exponents as the number of variables grows.  A rigorous decoder additionally
needs all of the following:

1. a lattice of dimension polynomial in `n` at the chosen growing `m`;
2. determinant inequalities including the dimension-dependent LLL factor;
3. enough algebraically independent integer polynomials after reduction;
4. a polynomial-time method to extract their common integer root;
5. quantified success over the quotient/error law.

Fixed-variable asymptotic statements suppress constants that depend on the
number of variables.  Substituting
\(m=\Theta(n/\log n)\) into such a statement without proving items 1–5 does
not yield a polynomial-time theorem.  This artifact therefore does not quote
a multivariate ACD threshold as proved.  Conversely, it does not claim that
all possible multivariate constructions fail.

---

## 7. Scope and surviving routes

What has been proved:

* the exact inequalities (2.4), (2.4u), and (2.12), which give the same coarse
  \(\Theta(n/\log n)\) approximation-isolation order for inverse-polynomial
  noise but not an exact matching threshold in all regimes;
* a deterministic Dirichlet obstruction showing that the designated
  \(q\)-vector is not shortest under (2.4), with a shorter unit coefficient
  only under the strengthened condition (2.4u);
* a complete polynomial-time LLL algorithm with an explicit success
  probability uniform over bounded adversarial errors;
* its optimized relative-error regime
  \(2^{-(1+o(1))\sqrt n}\);
* the failure of the inference that inverse-polynomial relative error alone
  meets this proved worst-case ordinary-LLL certificate.

For context only, the imported standard divisor-Coppersmith theorem yields
the one-sample comparison \(B\le N^{1/4-\eta}\) after the balance slack in
Section 6.  That theorem is not claimed as self-contained work of this
artifact and is not a premise of the F41 result.

What has not been proved:

* hardness of approximate common divisors at
  \(B=p/\operatorname{poly}(n)\);
* failure of BKZ, distribution-specific lattice reduction, nonlinear spectral
  search, robust clustering, or every multivariate small-root construction;
* failure when the errors have helpful algebraic correlations;
* a robust decoder when only an inverse-polynomial fraction of samples are
  inliers;
* construction from bare `N` of even the granted one-sided approximate-
  multiple source.

The source issue is logically prior to a top-level factoring result.  If bare
`N` could produce samples with the much stronger precision (4.12), Theorem
4.1 would turn them into a classical polynomial-time factorization.  At the
weaker proposed precision, this particular decoder test closes negatively but
leaves genuinely different nonlinear or distribution-sensitive decoders
open.

The clean retry criteria are therefore:

1. prove a factor-free bare-`N` sampler with
   \(B/p\le2^{-(1+\eta)\sqrt n}\), then invoke Theorem 4.1;
2. give a fully dimensioned polynomial-time decoder for
   \(B=p/\operatorname{poly}(n)\) that does not discard its guarantee in an
   exponential LLL factor;
3. exploit a specified non-adversarial error law and prove its additional
   structure survives on every balanced semiprime input;
4. for partial inliers, give an explicit robust selection/list-decoding
   theorem rather than assuming the lucky samples can be identified.

This is a conditional method boundary, not a factoring algorithm and not a
general impossibility theorem.

## Amendment record

The first hostile audit found three material issues in the original version:
its short Dirichlet coefficient was only known not to be divisible by `q`,
the term “identifiability” overstated an approximation-denominator result,
and the purported proof of the divisor-Coppersmith benchmark was only a
roadmap and silently used \(p\ge\sqrt N\).  The current version adds (2.4u),
retains the weaker exact conclusion under (2.4), exposes the \(\sqrt m\)
gap, makes the Coppersmith theorem an external non-premise with
\(\beta<1/2\), and corrects the preprocessing endpoints.  The failed audit
is preserved separately; this amended artifact requires a fresh whole-proof
audit before any promotion.
