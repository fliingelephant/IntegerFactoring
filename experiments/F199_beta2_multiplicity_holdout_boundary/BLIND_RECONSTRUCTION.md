# F199 blind reconstruction

## Verdict and evidence boundary

**PASS.** Each theorem follows from the stated hypotheses and the imported
P171--P175 interface. The conclusions have the narrow scope stated in the
candidate. They do not prove a general lower bound or a factoring algorithm.

Before reading the statement, I computed this SHA-256 digest:

```text
04c309ece29db251826247c6cfee7481b9e0b1a4e17c2ef5839ee06ac73be38c  STATEMENT.md
```

I read only the repository-root `PROMPT.md` and the F199 `STATEMENT.md`.
The F199 directory has no separate `PROMPT.md`. I did not inspect a proof,
self-audit, hostile audit, manifest, candidate message, or durable ledger. I
ran no mathematical computation.

The reconstruction treats the P171--P175 assertions in the opening section as
the imported interface. It does not attempt to reconstruct those earlier
results.

## Preliminary endpoint facts

The assumptions imply

\[
p<\sqrt N<q<2p.
\]

Thus \(p\le B<q<2p\), and the edge \(p-1\) occurs in the range
\(0\le i<B\). Also, \(N\) is odd, so it is a unit modulo every power of
two used below. Since \(p\ne q\), \(N\) is not a square and \(\sqrt N\)
is not an integer. Finally, \(t\ge2\) gives \(m=t-1\ge1\).

## Theorem 1: the public equations form a smooth torsor

Work throughout in \(R=\mathbb Z/2^t\mathbb Z\). For a unit \(u\), the
first two equations in (9) follow directly from
\(P_u=u^{-1}\) and \(Q_u=Nu\). They also give

\[
P_uQ_u=u^{-1}Nu=N.
\]

The definition of \(z\) gives \(Nz=A-1\) in \(R\). Hence

\[
NH_u=N(z+u)=A-1+Q_u.
\]

Conversely, \(PU=1\) forces \(U\) to be a unit and forces
\(P=U^{-1}\). The other two equations then force \(Q=NU\) and
\(H=z+U\). Thus every solution is uniquely parametrized by
\(U\in R^\times\).

More formally, the homomorphism

\[
R[U,P,Q,H]/(PU-1,Q-NU,H-z-U)
\longrightarrow R[U,U^{-1}]
\]

that sends \(P,Q,H\) to \(U^{-1},NU,z+U\) is an isomorphism. Its inverse
is induced by the class of \(U\). This proves (11), and the Laurent
polynomial algebra is smooth over \(R\) of relative dimension one.

For the three displayed defining equations, the Jacobian submatrix in
\((P,Q,H)\) is

\[
\begin{pmatrix}
U&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}.
\]

Its determinant is \(U\), which is a unit at every solution. There are
exactly \(|R^\times|=2^{t-1}\) unit residues. The imported congruence (5)
places \(u_*=p^{-1}\bmod 2^t\) among them. Therefore the target has the
same nonsingular local equation structure as every other candidate.

Here “simple points” means these simple \(R\)-valued solutions, as certified
by the unit Jacobian minor. It must not be read as a claim that the
\(2^{t-1}\) sections are distinct topological points of
\(\operatorname{Spec}R[U,U^{-1}]\). The scheme and Jacobian claims
themselves are exact.

## Theorem 2: the public coefficient word has no transition jet

### Public computability

It is enough to compute \(\binom{N-1}{i}\bmod 2^t\) in time polynomial in
\(\log N\), \(\log(i+1)\), and \(t\). A direct bit-polynomial algorithm
can be reconstructed as follows.

For an integer \(v\), compute \(\nu_2(v!)\) from
\(\sum_{r\ge1}\lfloor v/2^r\rfloor\). Let \(F_s(v)\) be the odd part of
\(v!\) modulo \(2^s\), and let

\[
G_s(v)=\prod_{\substack{1\le r\le v\\r\text{ odd}}}r\pmod {2^s}.
\]

Separating the odd and even factors gives the recursion

\[
F_s(v)=G_s(v)F_s(\lfloor v/2\rfloor).
\]

There are only \(O(\log(v+1))\) recursion levels. To evaluate \(G_s(v)\)
without iterating to \(v\), choose a block length \(L=2^a=O(s)\) with
\(a\ge2\), and split the odd factors into blocks of length \(L\). If

\[
C=\prod_{\substack{1\le r<L\\r\text{ odd}}}r,
\]

then the normalized product in block \(j\) is

\[
\prod_{r\text{ odd}}(1+jLr^{-1})\in1+4\mathbb Z/2^s\mathbb Z.
\]

Its 2-adic logarithm modulo \(2^s\) is a polynomial in \(j\):

\[
\sum_{h\ge1}\frac{(-1)^{h+1}(jL)^h}{h}
  \sum_{r\text{ odd}}r^{-h}.
\]

Only polynomially many terms survive because
\(\nu_2(L^h/h)=ah-\nu_2(h)\). The sum of this expression over any number
of full blocks uses the power sums \(\sum_{j<q}j^h\). All required power
sums can be computed by binary splitting, using the binomial expansion after
splitting \([0,q)\) into two intervals. This takes polynomially many
operations on \(s\)-bit integers. A truncated 2-adic exponential recovers
the normalized product. Modular powering supplies \(C^q\), and the final
partial block contains only \(O(s)\) factors. Hence \(G_s(v)\), and then
\(F_s(v)\), is computable in bit-polynomial time.

The valuation and the three odd factorial parts of
\((N-1)!/(i!(N-1-i)!)\) now give the binomial coefficient modulo
\(2^t\); the odd denominator parts are units. Multiplication by
\((-1)^i\), subtraction of one, and multiplication by \(N^{-1}\) give
\(z_i\). This proves the stated polynomial-time computability without
constructing the exponentially long exact binomial coefficient.

### Recurrence and smoothness

The exact binomial recurrence is

\[
(i+1)A_{i+1}=(i+1-N)A_i.
\]

Substitute \(A_i=1+Nz_i\) modulo \(2^t\), expand, and cancel the unit
\(N\). This gives

\[
(i+1)(z_{i+1}-z_i)+1+Nz_i=0,
\]

which is (14). No division by \(i+1\) is used, so even indices cause no
problem.

The polynomial (15) is linear in \(X,Y\). Its first Hasse derivatives are
therefore the coefficients

\[
N-(K+1),\qquad K+1.
\]

Their sum is the odd number \(N\). Consequently at least one derivative is
odd and hence a unit in \(R\). This proves smoothness modulo 2, and in fact
gives a unit gradient coordinate over \(R\), at every transcript edge. It
also applies to the valid edge \(i=p-1\). Thus that edge is not a
multiplicity outlier for this recurrence hypersurface.

### The unavailable quotient jump

It remains to verify that both branches in (17) are integral. If \(i<p\),
then \(i<p<q\), and reduction of the binomial product modulo either prime
gives

\[
(-1)^i\binom{N-1}{i}\equiv
(-1)^i\binom{-1}{i}=1.
\]

Thus \(N\mid A_i-1\).

Now write \(i=p+a\) with \(0\le a<p\). This covers the second branch
because \(i\le B<q<2p\). Modulo \(q\), the same calculation still gives
\(A_i\equiv1\). Modulo \(p\), use

\[
(1+X)^{pq-1}\equiv
\frac{(1+X^p)^q}{1+X}\pmod p.
\]

Below degree \(2p\), the numerator is \(1+qX^p\). The coefficient of
\(X^{p+a}\) is therefore
\((q-1)(-1)^a\). Multiplication by
\((-1)^{p+a}=-(-1)^a\) gives

\[
A_i\equiv1-q\pmod p.
\]

Hence both \(p\) and \(q\) divide \(A_i-1+q\), proving the integrality of
the second branch.

For \(i<p\), the equations \(NH_i=A_i-1\) and
\(Nz_i=A_i-1\) imply \(H_i-z_i=0\) in \(R\). For \(i\ge p\), they imply

\[
N(H_i-z_i)=q,
\qquad
H_i-z_i=qN^{-1}=p^{-1}
\quad\text{in }R.
\]

This proves (18). Taking consecutive differences proves (19), because the
step function changes only between \(p-1\) and \(p\).

The conclusion is restricted to the displayed public recurrence jet and to
the displayed one-error construction. Equation (14) does not prove that no
other nonlocal transformation of the public word can detect the hidden
edge. The statement expressly excludes that broader claim.

## Theorem 3: the Boolean holdout boundary

First suppose \(0\le d\le m\). Write a nonzero multilinear polynomial as

\[
F(x_1,\ldots,x_m)=G(x_1,\ldots,x_{m-1})
 +x_mH(x_1,\ldots,x_{m-1}).
\]

Induct on \(m\). If \(H=0\), each nonzero value of \(G\) appears twice,
and induction gives

\[
|\operatorname{supp}F|=2|\operatorname{supp}G|
\ge2\,2^{m-1-d}=2^{m-d}.
\]

If \(H\ne0\), then at every point where \(H=1\), at least one of the pair
\((G,G+H)\) is nonzero. Since \(\deg H\le d-1\), induction gives

\[
|\operatorname{supp}F|
\ge|\operatorname{supp}H|
\ge2^{(m-1)-(d-1)}=2^{m-d}.
\]

This proves (21). If \(d>m\), the right side is at most one and the claim
follows simply because a nonzero function has nonempty support.

If \(F\) vanishes outside \(S\), its support is a subset of \(S\), so
(22) follows. A singleton-supported nonzero polynomial cannot have degree at
most \(m-1\), while every multilinear polynomial has degree at most \(m\).
It therefore has degree exactly \(m\). The indicator

\[
\prod_{r=1}^m(1+x_r+a_r)
\]

shows directly that the boundary is attained at any chosen point \(a\).

The kernel of the evaluation map on \(\Omega\setminus S\) consists exactly
of degree-at-most-\(d\) polynomials supported inside \(S\). It is zero when
\(|S|<2^{m-d}\), which proves item 2. If the Reed--Muller feature matrix has
one feature row and one point column, this injectivity is equivalent to the
remaining columns having full row span. Thus deletion does not reduce the
column span, proving item 3.

Under (6), \(m=t-1=\Theta(n)\). If \(d\) is polylogarithmic and \(|S|\)
is numerical QP, then

\[
\log_2|S|=(\log n)^{O(1)}<m-d
\]

for all sufficiently large inputs. This proves the asymptotic conclusion.
An invertible affine change of the free bits preserves support size and the
degree filtration, so the same result holds after such a reparametrization.
“Affine changes” must mean affine automorphisms; no claim follows for a
noninjective or nonlinear encoding.

## Theorem 4: higher-order holdout

The multilinear Taylor expansion at \(x\) is

\[
F(x+y)=\sum_{S\subseteq[m]}D_SF(x)y^S.
\]

Setting \(y=\mathbf1_T\) proves (23), because \(y^S=1\) exactly when
\(S\subseteq T\). Thus (24) makes \(F\) zero at every point
\(x+\mathbf1_T\) with \(|T|<s\). Conversely, Boolean Möbius inversion gives

\[
D_SF(x)=\sum_{T\subseteq S}F(x+\mathbf1_T)
\]

over \(\mathbb F_2\). Vanishing on the radius-\((s-1)\) ball therefore
implies (24). This proves the stated equivalence, including the
order-zero condition \(F(x)=0\).

Let the conditions hold at every point except \(u\), with \(s\ge2\). Since
\(m\ge1\), choose a Hamming neighbor \(v=u+\mathbf1_{\{r\}}\). The
conditions at \(v\) give both \(F(v)=0\) and
\(D_{\{r\}}F(v)=0\). The radius-one Taylor identity then gives

\[
F(u)=F(v)+D_{\{r\}}F(v)=0.
\]

This proves (25) for every degree.

One radius-\((s-1)\) ball contains

\[
\sum_{j=0}^{s-1}\binom mj

\]

points, with \(\binom mj=0\) for \(j>m\). The union bound proves (26).
For numerical-QP \(C\) and polylogarithmic \(s\), the logarithm of this
bound is polylogarithmic in \(n\), while \(|\Omega|=2^m=2^{\Theta(n)}\).
The covered union consequently leaves exponentially many points, not one,
for all sufficiently large inputs.

For the scalar claim, Hasse multiplicity at least \(s\) at \(x_i\) is
equivalent to divisibility by \((X-x_i)^s\). The factors belonging to
distinct field points are coprime. Therefore

\[
\prod_{i\ne j}(X-x_i)^s\mid f(X).
\]

Since \(f(x_j)\ne0\), \(f\) is nonzero, and (27) follows by taking degrees.
This is a degree statement only. It is not a circuit-size lower bound.

## Theorem 5: an explicit target cloud is terminal

Use the total deterministic known-residue-class terminal imported from P175.
For each explicitly listed unit \(u\), the extended Euclidean algorithm
computes \(s=u^{-1}\bmod2^t\) in polynomial bit complexity. When
\(u=p^{-1}\bmod2^t\), this gives \(s=p\bmod2^t\), so the imported terminal
returns a factor. Exact division verifies any returned candidate and prevents
an incorrect output on the other iterations.

A numerical-QP number of numerical-QP calls still has numerical-QP total
cost: the product of two bounds of the form \(2^{(\log n)^{O(1)}}\) has the
same form. If list generation is Las Vegas, its expected numerical-QP cost
adds to this deterministic postprocessing cost, and its stated guarantee
places the true reciprocal in every completed output list. Thus termination
is almost sure and the expected total time is numerical QP.

If every one of a numerical-QP number of explicit columns has a publicly
enumerable numerical-QP preimage list, enumerate the union and apply the same
argument. The product of the two list-size bounds remains numerical QP. If an
explicit index list contains \(p\), testing \(\gcd(i,N)\) over the list finds
\(p\) directly. These arguments require explicit enumerable candidates. They
do not expand a column whose preimage is an exponentially large prefix cell.

This theorem depends on the imported terminal being a total numerical-QP
procedure on every supplied residue class. That is the operational content
of “deterministic numerical-QP factoring statistic” and of the terminal
invocation in the statement.

## Theorem 6: every one-bit lift is paired

Let \(M=2^{j+1}\). Since \(u_1=u_0+2^j\) and \(u_0\) is odd,

\[
(u_0+2^j)(u_0^{-1}+2^j)
=1+2^j(u_0+u_0^{-1})+2^{2j}
\equiv1\pmod M.
\]

Here \(u_0+u_0^{-1}\) is even, and \(2j\ge j+1\) because \(j\ge1\).
Uniqueness of inverses proves the first congruence in (33). Also, \(N\) is
odd, so

\[
Q_1-Q_0=N2^j\equiv2^j\pmod M,
\]

which proves the second. The three identities in (34) now follow directly
from the definitions. Toggling the top bit of \(U,P,Q\) twice is the
identity, so it is an involution that exchanges the two valid children.

For the balance claim, fix either odd residue class \(P_b\bmod M\). Any
open interval of length \(M\), whose endpoints are not integers in that
residue class, contains exactly one representative. Because \(\sqrt N\) is
irrational, there is therefore a unique odd representative

\[
\sqrt N-M<\widetilde P_b<\sqrt N.
\]

The same argument for \(Q_b\) gives a unique odd representative

\[
\sqrt N<\widetilde Q_b<\sqrt N+M.
\]

If \(3M<\sqrt N\), then

\[
\sqrt N+M<2\sqrt N-2M<2\widetilde P_b.
\]

Combining these inequalities proves all of (36). The lower endpoint is
positive as well. If \(M\le N^{1/4}\), then
\(3M<\sqrt N\) once \(N^{1/4}>3\), so the final asymptotic assertion is
uniformly valid. These representatives need not be prime and need not
multiply to \(N\), exactly as the statement warns.

## The surviving prefix-cell route

For a prefix \(a\), each factor \(1+x_r+a_r\) is one when \(x_r=a_r\)
and zero otherwise. Thus (37) is the exact cell indicator. Its top monomial
\(x_1\cdots x_\ell\) has coefficient one, so its degree is exactly
\(\ell\), and the \(m-\ell\) free suffix bits give support size
\(2^{m-\ell}\).

The degree-at-most-\(\ell\) feature-space dimension satisfies

\[
\sum_{j=0}^{\ell}\binom mj\le(m+1)^\ell.
\]

For polylogarithmic \(\ell\) and \(m=\Theta(n)\), this is numerical QP.
An exact numerical-QP syndrome that chooses the correct child at every stage
would require only \(m=O(n)\) stages. It would recover the target reciprocal
and then invoke Theorem 5. This verifies that the route is not excluded by
the earlier holdout bounds; it does not construct the missing syndrome.

## Scope and quantifier audit

- Theorems 1 and 6 prove symmetry for the displayed public congruences. They
  do not prove that every public polynomial or integer feature respects that
  symmetry.
- Theorem 2 excludes a multiplicity transition only for the public recurrence
  hypersurface. The one-error word uses the unavailable quotient transcript.
- Theorem 3 concerns low-degree multilinear functions of the candidate bits
  and invertible affine reparametrizations of those bits.
- Theorem 4 rules out the stated direct order conditions. It does not rule out
  sparse high-degree circuits with target-correlated parameters.
- Theorem 5 applies to explicit QP-enumerable candidates. It does not apply to
  a succinct aggregate cell with exponentially many members.
- The integer representatives in Theorem 6 satisfy balance only. Primality
  and the exact product equation remain the missing selector.
- No result in F199 excludes a nonlocal integer feature, an aggregate cell
  evaluator, an adaptive prefix syndrome, a nonlinear target-correlated
  embedding, or another factoring algorithm.

