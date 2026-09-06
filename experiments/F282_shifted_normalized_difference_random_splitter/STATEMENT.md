# F282 — shifted normalized differences give a random balanced-semiprime splitter

## Status

F282 is a proof-only candidate. It is not promoted. It contains no evaluator,
factoring implementation, numerical search, or empirical evidence.

## 1. Promise and public scalar

Let

\[
 N=pq,
 \qquad p<q<2p,
\]

where \(p\) and \(q\) are distinct odd primes, and put

\[
 B=\lfloor\sqrt N\rfloor.
\]

Test the public gcd \(\gcd(B,N)\) first. If it is nontrivial, it is a
factor. On the remaining branch there are integers \(s,h\) such that

\[
 B=p+s,
 \qquad q=B+h,
 \qquad s\ge1,
 \qquad h\ge s+2,
 \qquad p\ge2s+3.
\tag{1}
\]

Let \(\Delta f(X)=f(X+1)-f(X)\). For every integer \(a\), define the exact
integer

\[
 F_B(a)=\frac{\Delta^B X^{2B}|_{X=a}}{B!}.
\tag{2}
\]

The division in (2) is exact over the integers. It is not modular division.

## 2. Exact divided-difference identity

For complete homogeneous polynomials \(h_d\), one has the identity in
\(\mathbb Z[a]\)

\[
 \boxed{F_B(a)=h_B(a,a+1,\ldots,a+B).}
\tag{3}
\]

Thus \(F_B(a)\) is an integer for every integer \(a\).

## 3. Local laws

On the unresolved branch (1), the following congruences hold for every
integer \(a\):

\[
 \boxed{F_B(a)\equiv0\pmod q,}
\tag{4}
\]

and

\[
 \boxed{
 F_B(a)\equiv
 2h_{s+1}(a,a+1,\ldots,a+s)\pmod p.}
\tag{5}
\]

As a polynomial in \(a\) over \(\mathbb F_p\), the right side of (5) has
exact degree \(s+1\). Its leading coefficient is

\[
 2\binom{2s+1}{s}\not\equiv0\pmod p.
\tag{6}
\]

Consequently, at most \(s+1\) residue classes \(a\pmod p\) satisfy
\(p\mid F_B(a)\).

## 4. Random splitter theorem

Choose \(a\) uniformly modulo \(N\), compute \(F_B(a)\bmod N\), and put

\[
 d=\gcd(F_B(a),N).
\]

Equation (4) implies that \(q\mid d\). Outside at most \(s+1\) residue
classes modulo \(p\), equation (5) implies \(p\nmid d\). Therefore

\[
 \Pr[d=q]
 \ge 1-\frac{s+1}{p}
 \ge \frac{p+1}{2p}
 >\frac12.
\tag{7}
\]

On every other trial \(d=N\). Independent repetition has expected trial
count at most

\[
 \frac{2p}{p+1}<2.
\tag{8}
\]

The algorithm outputs only a verified proper divisor. It is therefore Las
Vegas on the stated promise.

## 5. Exact conditional evaluator consequence

Let \(n=\lceil\log_2(N+1)\rceil\). Suppose there is one uniform classical
algorithm which, from the public pair \((N,a)\), returns

\[
 F_{\lfloor\sqrt N\rfloor}(a)\bmod N
\]

in numerical-quasipolynomial bit complexity in \(n\), for every input in the
stated balanced-semiprime branch. It receives no factor, hidden parameter,
field decomposition, or nonunit inverse.

Then the public \(\gcd(B,N)\) screen, exact uniform sampling modulo \(N\),
that evaluator, and one gcd per trial form a uniform classical Las Vegas
numerical-QP factorer for this balanced distinct-odd-semiprime promise. The
expected number of evaluator calls is below two.

Standard exact preprocessing can separately remove even factors, recognize
prime inputs, and reduce perfect powers. F282 does not prove that these
steps turn every residual composite into the promise above. It gives no
success theorem for unbalanced semiprimes, repeated-prime semiprimes, or
integers with three or more prime factors. Any all-input conclusion needs a
separate correct reduction for those cases.

## 6. Evaluator boundary

F282 does not construct the assumed evaluator.

The literal forward-difference formula has \(B+1\) terms and an exact
division by \(B!\). On the unresolved branch,

\[
 \gcd(B!,N)=p,
\]

so \(B!\) has no inverse modulo \(N\). The usual complete-homogeneous
recurrence keeps a characteristic-size coefficient range. Exact
materialization can have \(\Theta(B\log B)\) bits already at \(a=0\).
Since \(B=2^{\Theta(n)}\) on the promise, these literal methods are not
numerical-QP algorithms in \(n\).

More sharply, \(p<B<q<2p\), so \(B!\) contains \(p\) exactly once and no
\(q\). Since \(q\mid F_B(a)\) for every shift, the raw difference
\(B!F_B(a)\) is zero modulo all of \(N\). The useful \(q\)-only residue
appears only after the exact, factor-bearing division by \(B!\). The theorem
supplies the constant-success dispatcher after normalization. It does not
supply that normalization.

These are costs of named representations. They are not arithmetic-circuit,
recurrence, or evaluator lower bounds. A different uniform succinct modular
evaluator remains open.

## Exact exclusions

F282 proves no:

1. construction of a numerical-QP evaluator for (2) or (3);
2. unconditional factoring algorithm, even on the promise;
3. all-input reduction to balanced distinct odd semiprimes;
4. resolution of the F281 central joint-saturation conjecture;
5. lower bound against succinct modular evaluation; or
6. empirical result.
