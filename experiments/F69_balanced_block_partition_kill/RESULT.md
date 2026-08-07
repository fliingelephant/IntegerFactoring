# F69 balanced-block partition kill

**Family:** F26.

**Status:** proof-only mandatory kill test. No research computation was run.

**Verdict:** multiplicative balance is not a useful-selector theorem.
Even an oracle for the exact closest legal block partition can return a
factor-free or global pair. For one retained relation, a factor-free split
only re-presents the same relation. For an aggregate of two nontrivial
relations, the exact complementary divisor is always larger than \(N\), so
ordinary number partition optimizes the wrong integer.

The main conclusions are exact.

- A complementary canonical pair \(g,w<N\) for \(A=1+kN\) can exist only
  when \(k\le N-2\). Equality forces \(g=w=N-1\), the global root.
- The product of two nontrivial relation values is larger than \(N^2\).
  It has no exact complementary pair with both endpoints below \(N\).
- A whole-block split of one old relation adds no relation value and no
  gcd-free block. Counting it as another occurrence is deliberate source
  amplification, not information learned by balancing.
- At \(N=209\), the unique closest factor pair of
  \(6480=2^4 3^4 5\) is \(80\cdot81\). It survives the direct and
  discriminant screens. The farther legal split \(45\cdot144\) immediately
  exposes \(11\).
- There is an infinite balanced-composite family whose only admissible
  whole-block pair has distance one, survives every named screen, and is
  exactly the old endpoint pair.
- A polynomial-precision approximation in logarithmic imbalance does not
  imply polynomial additive inverse distance when \(A=\Theta(N^2)\).

Thus a log-partition FPTAS can be useful as an optimizer, but balance alone
does not turn it into a factoring sampler. The surviving cross-relation
problem must optimize the canonical residue of an oversized complement or
use another factor-correlated property. That is a modular selection problem,
not ordinary number partition.

## 1. Closest routes and material difference

P69 proves redundancy when one current gcd-free block is fed back. P70
allows a product of blocks from several indexed relation occurrences. Its
raw complementary divisor can exceed \(N\), and its canonical inverse then
creates a new relation. P73 separates creation of a square-class dependency
from creation of a non-global decoded root.

F66 gives inverse-polynomial useful mass for the inverse-distance target on
the **full unit group**. F67 already shows that small positive inverse
distance is not monotone toward a direct factor and that ranking an
exhausted menu matters only through later block or occurrence changes.

This retry is narrower. It uses the integer factorization

\[
 A=\prod_j q_j^{E_j}=1+kN
\]

and tries to partition the logarithms of the available whole blocks so that
two exact complementary divisors are close to \(\sqrt A\). The new question
is whether this numerical partition structure supplies the missing
factor-correlated selector. The answer is no, even if exact optimization is
granted for free.

## 2. Model

Let \(N\ge3\) be odd. Let

\[
 A=1+kN=\prod_{j=1}^s q_j^{E_j},
\]

where the public blocks \(q_j>1\) are pairwise coprime,
\(\gcd(q_j,N)=1\), and all exponents \(E_j\) are retained exactly. The
blocks need not be prime.

For an exponent vector \(c\) with \(0\le c_j\le E_j\), put

\[
 g(c)=\prod_jq_j^{c_j},
 \qquad
 h(c)=\prod_jq_j^{E_j-c_j}=\frac A{g(c)}.
\]

Call \(c\) a **balanced-canonical split** when

\[
 1<g(c)<N,
 \qquad
 1<h(c)<N.
\]

Then \(g(c)h(c)\equiv1\pmod N\), so \(h(c)\) is the canonical inverse of
\(g(c)\). Define

\[
 \delta(c)=|g(c)-h(c)|
\]

and the logarithmic imbalance

\[
 \beta(c)=\left|\log g(c)-\frac12\log A\right|.
\]

The complement map \(c\mapsto E-c\) only reverses the orientation of one
unordered pair.

This model is stricter than P70's legal-state condition. P70 requires only
\(1<g<N\). It does not require the raw complement \(A/g\) to be below \(N\).

## 3. Exact magnitude boundary

### Theorem 1: one relation can fit; a nontrivial aggregate cannot

If a balanced-canonical split exists, then

\[
 A\le(N-1)^2=1+(N-2)N,
 \qquad
 k\le N-2.
\tag{1}
\]

If \(k=N-2\), the only split is

\[
 g=h=N-1.
\tag{2}
\]

Now let

\[
 P=\prod_{i\in S}(1+k_iN)
\]

be an aggregate containing at least two occurrences with \(k_i\ge1\).
Then

\[
 P\ge(N+1)^2>(N-1)^2.
\tag{3}
\]

Consequently, \(P\) has no exact complementary divisors \(g,h<N\).
Moreover, for every divisor \(1<g<N\),

\[
 \frac Pg
 \ge\frac{(N+1)^2}{N-1}
 =N+3+\frac4{N-1}>N.
\tag{4}
\]

#### Proof

Two positive integers below \(N\) have product at most \((N-1)^2\). This
proves (1). Equality in that product bound forces both integers to equal
\(N-1\), proving (2). Every nontrivial relation value is at least \(N+1\),
which proves (3) and (4). \(\square\)

### Consequence for cross-relation balancing

Write an oversized raw complement as

\[
 H=\frac Pg=w+tN,
 \qquad
 1\le w\le N-1,\quad t\ge1.
\tag{5}
\]

The canonical inverse is \(w\), not \(H\). The desired score is

\[
 |g-w|,
\]

whereas ordinary multiplicative partition optimizes

\[
 |g-H|
 \quad\text{or}\quad
 |\log g-\log H|.
\]

The subtraction of the unknown multiple \(tN\) is the entire modular
problem. P70's identity \(k(g)=K\bmod g\) describes the new canonical
relation after this reduction. It does not identify \(w\) with the raw
complement.

Thus the proposed cross-relation log partition has a domain mismatch. If it
uses one relation, it stays inside an old value. If it uses two nontrivial
relations, the exact complement cannot be a canonical endpoint.

## 4. What a one-relation split can change

### Theorem 2: exact one-relation redundancy

Assume that \(A=1+kN\) is already retained with exponent vector \(E\).
Let \(c\) be any balanced-canonical split.

1. The selected inverse relation is exactly the old value:

   \[
   g(c)h(c)=A=1+kN.
   \tag{6}
   \]

2. Both new endpoints use only the old pairwise-coprime blocks \(q_j\), with
   exponent vectors \(c\) and \(E-c\). Joint gcd refinement introduces no
   new block support and splits no \(q_j\).
3. The square-class column is identical. On nonsquare block rows it is
   \(E\bmod2\); perfect-square blocks are omitted from those rows. If the
   identical value is appended as a new indexed occurrence, the new duplicate
   dependency has positive integer square root \(A\), hence modular root
   \(1\). It adds no new decoded root class.
4. If the selected \(g\) passes a direct gcd screen, it factors \(N\) before
   feedback. If all public screens fail and the block menu uses a fixed
   occurrence box, appending the split is a no-op.

#### Proof

Equation (6) is the definition of exact complementation. Pairwise coprime
block bases have unique exponent coordinates, so gcds among old and new
endpoints only take coordinatewise minimum exponents. They cannot split the
integer support of one \(q_j\).

The relation-value column depends on \(E\), not on which endpoint receives
each occurrence. A duplicate column adds the binary dependency consisting
of the old and new copies. Their product is \(A^2\), whose positive root is
\(A\equiv1\pmod N\). Adding this duplicate vector to another dependency only
multiplies its normalized root by \(1\). The direct-screen statement is
immediate. \(\square\)

An implementation can declare the new copy to be another authorized source
occurrence. Then the exponent capacity increases, and later power products
can be new. P70 shows that deliberate reuse can matter. This is an explicit
multiplicity rule that must be charged in the transcript. It is not new
arithmetic information produced by the balance score.

The theorem does not say that finding a useful legal divisor of one relation
is easy. It says that, after a factor-free choice, the proposed feedback adds
no new value or block unless occurrence amplification is separately declared.

## 5. Logarithmic balance is not additive inverse distance

Assume \(g\le h\), and put

\[
 \beta=\frac12\log\frac hg
 =\left|\log g-\frac12\log A\right|.
\]

Then exactly

\[
 g=\sqrt A\,e^{-\beta},
 \qquad
 h=\sqrt A\,e^\beta,
\]

and

\[
 \boxed{\delta=h-g=2\sqrt A\,\sinh\beta.}
\tag{7}
\]

Therefore a certificate \(\beta\le\varepsilon\) gives only

\[
 \delta\le2\sqrt A\,\sinh\varepsilon.
\tag{8}
\]

For the displayed certificate alone to guarantee \(\delta\le D\) in the
worst case, it must resolve the log imbalance at the scale

\[
 \varepsilon\le
 \operatorname{arsinh}\!\left(\frac D{2\sqrt A}\right).
\tag{9}
\]

Let \(n=\lceil\log_2N\rceil\). When \(A=\Theta(N^2)\) and
\(D=\operatorname{poly}(n)\), this scale is \(2^{-\Omega(n)}\). An FPTAS
whose cost is polynomial in \(1/\varepsilon\) is not a bit-polynomial method
at that requested additive resolution.

This is a precision boundary, not a hardness proof. A different exact
integer algorithm could exploit extra structure. The counterexamples below
are stronger for the factoring claim: they defeat even a free exact
optimization oracle.

## 6. Balance has no direct-factor monotonicity

For a complementary canonical pair, put \(d=g-h\). For every prime
\(\ell\mid N\),

\[
 \ell\mid d
 \quad\Longleftrightarrow\quad
 g^2\equiv1\pmod\ell.
\tag{10}
\]

Indeed, \(h\equiv g^{-1}\pmod\ell\), and multiplication by \(g\) proves the
equivalence. On a squarefree semiprime \(N=pq\), a nonzero direct separator
therefore has

\[
 \delta\ge\min(p,q).
\tag{11}
\]

Positive distances below the smallest prime factor are guaranteed **not** to
give a direct separator. The discriminant ticket

\[
 \gcd(d^2+4,N)
\]

tests the separate condition \(g^2=-1\) in a hidden component. Exact balance
\(d=0\) gives a square root of one, but that root can be either global or
useful. None of these facts gives a monotone benefit to minimizing a positive
distance.

## 7. Exact counterexamples

### 7.1 Perfect balance can be global on every odd composite

For any odd composite \(N\), take

\[
 A=(N-1)^2=1+(N-2)N
\]

with the one-block presentation \(q_1=N-1,E_1=2\). The only
balanced-canonical split is

\[
 g=h=N-1.
\]

It is the exact optimum with \(\delta=0\), but it is the global root \(-1\).
The direct screens give

\[
 \gcd(N-2,N)=1,
 \qquad
 \gcd(N,N)=N,
\]

and the discriminant gcd is \(\gcd(4,N)=1\). Removing global roots leaves no
candidate. This is an infinite exact obstruction to “perfect balance is
useful.”

### 7.2 The exact closest split can lose to a farther split

Let

\[
 N=209=11\cdot19,
 \qquad
 A=6480=1+31\cdot209=2^4 3^4 5.
\]

Use the factor-free block presentation

\[
 (q_1,q_2,q_3)=(2,3,5),
 \qquad
 E=(4,4,1).
\]

The split

\[
 80=2^4\cdot5,
 \qquad
 81=3^4
\]

has distance one. Since

\[
 80^2=6400<6480<6561=81^2,
\]

it is the unique closest unordered factor pair even among all integer
divisors of \(A\). It is factor-free:

\[
 \gcd(79,209)=\gcd(81,209)=1,
\]

and its inverse endpoint has the same direct outcome. Its discriminant
ticket also fails:

\[
 \gcd(1^2+4,209)=1.
\]

The same block box contains the farther split

\[
 45=3^2\cdot5,
 \qquad
 144=2^4 3^2,
 \qquad
 45\cdot144=6480.
\]

It has distance \(99\), but

\[
 \gcd(45-1,209)=\gcd(44,209)=11.
\tag{12}
\]

Thus exact balance ranks a clean failure strictly ahead of an available
factor. This refutes both deterministic monotonicity and any claim that a
low-temperature balance distribution must favor useful splits.

### 7.3 An infinite distance-one factor-free fixed family

Put

\[
 F(z)=z^2+z-1.
\]

For every multiple \(t\ge5\) of \(5\), define

\[
 a=F(t)=t^2+t-1,
 \qquad
 b=F(t+1)=t^2+3t+1,
 \qquad
 N=ab.
\tag{13}
\]

Both \(a\) and \(b\) are odd and greater than one. They are coprime. Indeed,
if \(d\mid a,b\), then \(d\) is odd and

\[
 d\mid b-a=2(t+1).
\]

Hence \(d\mid t+1\), while

\[
 a=t(t+1)-1\equiv-1\pmod d,
\]

so \(d=1\). The two displayed factors are asymptotically equal, so (13) is
an infinite balanced-composite family. Also,

\[
 a\equiv-1\pmod5,
 \qquad
 b\equiv1\pmod5,
\]

and therefore \(\gcd(N,5)=1\).

CRT gives a unique \(u\in\{0,\ldots,N-1\}\) such that

\[
 u\equiv t\pmod a,
 \qquad
 u\equiv t+1\pmod b.
\tag{14}
\]

Equation (14) gives \(F(u)\equiv0\pmod a\) and modulo \(b\), hence

\[
 F(u)=kN
\]

for an integer \(k\). The residues \(0,1,-1,-2\) cannot equal \(u\) modulo
\(N\), because

\[
 F(0)=F(-1)=-1,
 \qquad
 F(1)=F(-2)=1.
\]

Thus the canonical representative satisfies

\[
 2\le u\le N-3,
 \qquad
 k\ge1.
\]

It supplies the exact inverse relation

\[
 A=u(u+1)=1+kN.
\tag{15}
\]

Give (15) the two-block presentation

\[
 q_1=u,\quad q_2=u+1,\quad E=(1,1).
\]

The blocks are coprime consecutive integers. They are units modulo \(N\)
because their product is \(1\) modulo \(N\). The only unordered
balanced-canonical split is

\[
 \{g,h\}=\{u,u+1\}.
\]

The other two divisors are \(1\) and \(A>N\). The gap is the minimum
possible positive value:

\[
 \delta=1.
\]

All four direct endpoint screens fail. A common divisor with \(N\) would
force \(u\) to be one of \(1,-1,0,-2\) modulo that divisor, contradicting
the four displayed values of \(F\). The discriminant screen also fails
because

\[
 \gcd(\delta^2+4,N)=\gcd(5,N)=1.
\]

Finally, \(A\) is not a square. Since \(\gcd(u,u+1)=1\), a square product
would make both consecutive integers squares. This is impossible for
\(u\ge2\).

The exact optimizer therefore returns the old factor-free endpoint pair.
Appending it changes no value, block, or fixed occurrence box. The family
has success probability zero for every sampler supported on its admissible
two-block splits.

The finite \(t=3\) version of the construction is the familiar
\(a=11,b=19,N=209,u=80\) distance-one pair. The restriction \(5\mid t\) in
the infinite family is only a simple way to keep the discriminant ticket
coprime to \(N\).

## 8. Why F66's mass theorem does not transfer

F66 weights every unit of \(U_N\). Its useful-mass lower bound starts from
the fact that the full inverse graph contains the two mixed CRT roots of one.
A legal-divisor box can omit both roots, as section 7.3 does, or contain only
the global root, as section 7.1 does.

The four-point signed-fibre upper bound remains true after restricting to a
subset. The required lower bound on useful states does not. Therefore a
partition Gibbs law such as

\[
 \Pr(c)\ \propto\ \frac1{1+\delta(c)}
\]

can have useful mass exactly zero. Approximating its partition function or
sampling it exactly does not factor the infinite family above.

The \(N=209\) refined presentation shows a second failure mode. Useful mass
can exist in the legal box while the closest state is factor-free. Approximate
number partition and factor correlation are separate theorems.

## 9. Final classification

The proposed selector does not survive the mandatory kill test.

1. **Single relation:** balance can find a direct factor, but after a miss it
   only re-presents the old relation. It gives no block novelty or new decoded
   root class.
2. **Two or more nontrivial relations:** the exact aggregate complement is
   larger than \(N\). Balancing it around \(\sqrt P\) does not optimize the
   canonical inverse residue.
3. **Optimization quality:** polynomial log precision does not imply small
   additive inverse distance near \(A=\Theta(N^2)\).
4. **Factoring signal:** exact closest partitions can be global or
   factor-free, even when a farther legal partition factors immediately.
5. **Sampling:** a legal block box can have zero useful support, so no
   F66-style normalized-mass conclusion follows.

**Overall balanced-block sampler: FAIL.** This is an oracle-level mechanism
failure, not a proof that multiplicative partition lacks an FPTAS and not a
lower bound for every block selector.

A materially new retry must act on the canonical residue

\[
 w\equiv P/g\pmod N,\qquad1\le w<N,
\]

rather than on the oversized integer complement \(P/g\), or it must prove a
different block statistic has inverse-polynomial direct-separator or
non-global-closure probability. It must also declare and charge every
occurrence amplification. Those are precisely the modular and source-law
gaps left by P70 and P73.
