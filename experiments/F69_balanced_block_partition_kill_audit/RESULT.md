# F69 hostile audit — balanced-block partition kill

## Verdict: PASS

The audited candidate has SHA-256
0501b6f40e150c53b22ffd9119e42f9136bec0f77945ed451fc852f03841fe36.

Every stated theorem and finite example is correct in its declared scope.
The infinite \(F(t)\) construction also satisfies every required condition.
It gives exactly zero useful mass for a sampler whose support is the declared
balanced-canonical whole-block splits.

Two phrases need scope, but neither changes the result:

- In \(H=w+tN\), the integer \(t\) is not computationally hidden after
  \(g\) is chosen; \(H=P/g\), \(w=H\bmod N\), and \(t=(H-w)/N\) are public.
  The valid point is that ordinary magnitude balance does not control this
  modular reduction.
- “Balanced composite” means that \(N=ab\) is composite and has the
  displayed coprime factors \(a,b\) with \(b/a\to1\). It does not assert
  that \(a,b\) are prime or that each is composite.

The PASS verdict concerns the self-contained mathematical claims. It does
not certify the candidate's historical descriptions of other experiments.

## 1. Aggregate magnitude

Let \(g,h\) be positive integers with \(g,h<N\) and

\[
gh=A=1+kN.
\]

Then

\[
1+kN\le(N-1)^2=1+(N-2)N,
\]

so \(k\le N-2\). If \(k=N-2\), equality holds in the product bound. Since
both factors are at most \(N-1\), equality forces

\[
g=h=N-1.
\]

This is the global root \(-1\pmod N\). The first part of Theorem 1 is exact.

Now take at least two nontrivial relation occurrences. Each has value
\(1+k_iN\ge N+1\), so

\[
P=\prod_i(1+k_iN)\ge(N+1)^2>(N-1)^2.
\]

No exact complementary pair can have both entries below \(N\). More
strongly, for any divisor \(1<g<N\),

\[
\frac Pg\ge\frac{(N+1)^2}{N-1}
=N+3+\frac4{N-1}>N.
\]

Thus every legal raw complement is oversized.

Because all source blocks are units modulo \(N\), \(H=P/g\) is also a unit.
It therefore has a unique canonical representative \(w\in\{1,\ldots,N-1\}\)
and

\[
H=w+tN,\qquad t\ge1.
\]

Ordinary partition controls \(g\) against \(H\), while the desired inverse
score controls \(g\) against \(w\). Reduction by \(tN\) is discontinuous in
the ordinary magnitude objective. This proves the claimed domain mismatch.

## 2. A one-relation whole-block split cannot refine a block

Suppose

\[
A=\prod_jq_j^{E_j}
\]

is already retained and the \(q_j\) are pairwise coprime. For a split vector
\(c\),

\[
g=\prod_jq_j^{c_j},
\qquad
h=\prod_jq_j^{E_j-c_j}.
\]

Their product is exactly \(A\), not a new relation value.

Every old value and both new endpoints have exact exponent coordinates on
the same \(q_j\). For any two such integers,

\[
\gcd\!\left(\prod_jq_j^{a_j},\prod_jq_j^{b_j}\right)
=\prod_jq_j^{\min(a_j,b_j)}.
\]

Therefore gcd refinement can change exponent coordinates, but it cannot
extract a proper factor of any \(q_j\), introduce new support, or split one
old block into new coprime blocks. This remains true when a \(q_j\) is
composite or a prime power.

The square-class column of the relation is determined by

\[
(E_1,\ldots,E_s)\bmod2
\]

on the nonsquare rows. Reassigning occurrences between the two endpoints
does not change it. If a second indexed copy of \(A\) is appended, the
difference of the two equal columns is a new dependency, but its selected
exact product is

\[
A^2.
\]

Its unique positive root is \(A\equiv1\pmod N\). Hence the new dependency
has global root label \(1\) and does not enlarge the old decoded-root image.
This verifies the candidate's duplicate-root claim.

An explicitly charged occurrence-capacity increase can make later power
products new. The theorem correctly separates that source rule from
information learned by balancing. With a fixed occurrence box, a
factor-free, public-screen-free split is a factoring no-op even though a
fresh indexed duplicate would increase raw kernel dimension.

## 3. Logarithmic imbalance

Assume \(g\le h\), \(gh=A\), and

\[
\beta=\frac12\log(h/g).
\]

Solving the product and ratio equations gives

\[
g=\sqrt A\,e^{-\beta},
\qquad
h=\sqrt A\,e^\beta.
\]

Therefore

\[
\delta=h-g
=\sqrt A(e^\beta-e^{-\beta})
=2\sqrt A\,\sinh\beta.
\]

The function \(\sinh\) is increasing on nonnegative inputs, so an absolute
certificate \(\beta\le\varepsilon\) gives exactly

\[
\delta\le2\sqrt A\,\sinh\varepsilon.
\]

For this certificate alone to guarantee \(\delta\le D\), it is necessary
and sufficient that

\[
\varepsilon\le
\operatorname{arsinh}\!\left(\frac D{2\sqrt A}\right).
\]

Let \(n=\lceil\log_2N\rceil\). If \(A=\Theta(N^2)\) and
\(D=\operatorname{poly}(n)\), then the argument of \(\operatorname{arsinh}\)
is \(2^{-\Omega(n)}\). Since
\(\operatorname{arsinh}x=\Theta(x)\) near zero, the required absolute
precision is \(2^{-\Omega(n)}\). An FPTAS with runtime polynomial in
\(1/\varepsilon\) is exponential at that resolution.

This conclusion applies to an absolute log-imbalance guarantee. It is not a
general hardness theorem for exact partition or for every possible relative
approximation objective, matching the candidate's stated limitation.

## 4. Direct and discriminant screens

For a complementary canonical pair, \(h\equiv g^{-1}\pmod\ell\) at every
prime \(\ell\mid N\). Thus

\[
g(g-h)\equiv g^2-1\pmod\ell.
\]

Since \(g\) is a unit,

\[
\ell\mid(g-h)
\quad\Longleftrightarrow\quad
g^2\equiv1\pmod\ell.
\]

For a squarefree semiprime \(N=pq\), a positive direct-separator distance is
therefore divisible by \(p\) or \(q\), and

\[
\delta\ge\min(p,q).
\]

Also

\[
(g-g^{-1})^2+4=(g+g^{-1})^2
\]

modulo each hidden prime, so the discriminant gcd tests the distinct local
condition \(g^2\equiv-1\). At \(\delta=0\), the endpoint is a square root of
one and can be either global or mixed-sign. These facts support, rather than
contradict, the candidate's non-monotonicity conclusion.

## 5. The global exact optimum

For any odd composite \(N\), take

\[
A=(N-1)^2=1+(N-2)N
\]

with presentation \(q_1=N-1,E_1=2\). The exponent choices are \(0,1,2\).
The choices \(0\) and \(2\) put \(1\) on one side and are inadmissible.
The only balanced-canonical split is

\[
g=h=N-1.
\]

It has \(\delta=0\) but is the global root \(-1\). Its screens are

\[
\gcd(N-2,N)=1,\qquad
\gcd(N,N)=N,\qquad
\gcd(4,N)=1,
\]

where oddness gives the first and third equalities. Removing global roots
leaves no admissible candidate. This infinite obstruction is exact even if
\(N-1\) happens to be a perfect square, because the model retains exact
blocks and exponent data.

## 6. The \(N=209\) closest and farther splits

For

\[
N=209,\qquad
A=6480=2^4 3^4 5,
\]

the pair \(80,81\) is legal and has distance one. The inequalities

\[
80^2<6480<81^2
\]

show that \(80=\lfloor\sqrt A\rfloor\). For any factor pair
\(x,A/x\) with \(x\le\sqrt A\), the distance \(A/x-x\) strictly decreases
as \(x\) increases. Hence \(80,81\) is the unique closest unordered factor
pair even without the block-box restriction.

The pair is factor-free under the named immediate screens:

\[
\gcd(79,209)=\gcd(81,209)=1,
\qquad
\gcd(1^2+4,209)=1.
\]

The inverse endpoint has the same direct-screen outcome.

The same exponent box contains

\[
45=3^2\cdot5,\qquad
144=2^4 3^2,
\]

and \(45\cdot144=6480\). Both endpoints are below \(209\), so this is also a
balanced-canonical split. It is farther, with distance \(99\), but

\[
\gcd(45-1,209)=\gcd(44,209)=11.
\]

Thus the exact closest split fails while a farther admissible split factors.
This is a valid pointwise refutation of monotonic usefulness. The later
infinite family supplies the stronger zero-support sampling obstruction.

## 7. The infinite \(F(t)\) family

Let \(t\ge5\) be any multiple of \(5\), and put

\[
a=t^2+t-1,\qquad
b=t^2+3t+1,\qquad
N=ab.
\]

### Parity, size, coprimality, and balance

Both \(t(t+1)\) and \(t(t+3)\) are even. Hence \(a\) and \(b\) are odd.
They are greater than one for \(t\ge5\).

If \(d\mid a,b\), then \(d\) is odd and

\[
d\mid b-a=2(t+1).
\]

Thus \(d\mid t+1\). But

\[
a=t(t+1)-1\equiv-1\pmod d,
\]

so \(d=1\). Therefore \(a,b\) are coprime and \(N\) is an odd composite.

Moreover,

\[
\frac ba
=1+\frac{2t+2}{t^2+t-1}
\longrightarrow1.
\]

Thus \(a,b\sim t^2\) and each is asymptotic to \(\sqrt N\). This is the
exact sense in which the composite family is balanced.

Because \(5\mid t\),

\[
a\equiv-1\pmod5,\qquad b\equiv1\pmod5.
\]

Consequently \(\gcd(N,5)=1\).

### CRT construction and canonical range

Since \(a,b\) are coprime, CRT gives a unique
\(u\in\{0,\ldots,N-1\}\) satisfying

\[
u\equiv t\pmod a,\qquad
u\equiv t+1\pmod b.
\]

For \(F(z)=z^2+z-1\), these congruences imply
\(F(u)\equiv0\pmod a\) and \(F(u)\equiv0\pmod b\). Hence

\[
F(u)=kN
\]

for an integer \(k\).

The residues \(0,1,-1,-2\pmod N\) are impossible because

\[
F(0)=F(-1)=-1,\qquad
F(1)=F(-2)=1,
\]

while \(N\mid F(u)\). Therefore the canonical representative obeys

\[
2\le u\le N-3.
\]

Now \(F(u)>0\), so \(k\ge1\), and

\[
u(u+1)=F(u)+1=1+kN.
\]

Both endpoints lie strictly between \(1\) and \(N\).

### Blocks and the only admissible split

Use the exact two-block presentation

\[
q_1=u,\qquad q_2=u+1,\qquad E=(1,1).
\]

The blocks are coprime because they are consecutive. Their product is
\(1\) modulo \(N\), so each is individually a unit modulo \(N\).

There are four exponent vectors. The all-zero and all-one vectors give the
inadmissible pair \(\{1,A\}\). The other two vectors are the two
orientations of the sole unordered admissible pair

\[
\{g,h\}=\{u,u+1\}.
\]

Its distance is exactly one, the minimum positive integer distance.

### Every named screen fails

The four direct screens are

\[
\gcd(u-1,N),\quad
\gcd(u+1,N),\quad
\gcd(u,N),\quad
\gcd(u+2,N).
\]

If a divisor \(d>1\) of \(N\) divided one of these four endpoint offsets,
then \(u\) would be congruent modulo \(d\) to \(1,-1,0\), or \(-2\).
The corresponding value of \(F(u)\) would be \(1,-1,-1\), or \(1\) modulo
\(d\), contradicting \(d\mid N\mid F(u)\). All four gcds are therefore
exactly \(1\).

The discriminant ticket is

\[
\gcd(\delta^2+4,N)=\gcd(5,N)=1.
\]

Finally, \(A=u(u+1)\) is not a square. Its two consecutive factors are
coprime; if their product were square, each would be square, but no two
consecutive positive integers at least \(2\) are both squares.

Thus the only admissible whole-block split is factor-free, has no
discriminant hit, and has no singleton exact-square certificate. It is
exactly the old endpoint pair. By the one-relation theorem, appending it
changes no value or block and changes no fixed occurrence box.

Both orientations have the same failed screens. Hence every probability
distribution supported on this admissible split set assigns useful mass
exactly zero. This is a support statement, not merely a limiting or
asymptotic probability claim.

### The \(t=3\) specialization

Although \(t=3\) is outside the convenient infinite subfamily
\(5\mid t\), it gives

\[
a=11,\qquad b=19,\qquad N=209.
\]

The CRT solution is \(u=80\), because
\(80\equiv3\pmod{11}\) and \(80\equiv4\pmod{19}\). This recovers the
distance-one pair \(80,81\). Its discriminant gcd also happens to be one.

## 8. Final assessment

The candidate establishes all five advertised mechanism boundaries:

1. one exact relation fits below \(N\) only up to \(k=N-2\), with equality
   forcing the global pair;
2. two nontrivial occurrences have no raw complementary pair below \(N\);
3. a whole-block split of one retained relation cannot reveal a proper
   factor of an old block or add a new root label;
4. inverse-polynomial absolute log precision does not guarantee polynomial
   additive distance near \(A=\Theta(N^2)\);
5. exact balance can have either a nearer failure than an available success
   or an admissible support with exactly zero useful mass.

Therefore the candidate's overall balanced-block sampler classification is
correct. It rules out balance as a universal factoring selector. It does
not rule out partition algorithms, modular-residue selectors, or explicitly
charged occurrence amplification.
