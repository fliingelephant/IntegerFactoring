# F89 hostile proof audit

## Verdict: PASS

I audited RESULT.md at SHA-256

    03d4d98d26a8f7034564ae77d960f987d960cb0f3525f309e1b1f17027d80af6

The digest matches the requested artifact. I ran no research search or
research computation. I found no counterexample to the coprime-order
theorem, full-product conclusion, separator law, conditional sampling and
enumeration decoders, quotient-size consequence, or either fixed witness.

The pass is conditional. Public generators for \(K\) must already exist.
Random extraction additionally needs one powered local image order to be
polynomially small. Deterministic extraction needs the whole powered image
to fit a public polynomial cap. The theorem proves neither condition from
bare \(N\).

There is one presentation defect in the candidate. In equation (4), both
instances of the command for a fraction contain a form-feed character and
render as “rac” instead of \(\backslash\mathrm{frac}\). The intended formula
is unambiguous and all later arguments use the correct formula. This does
not change the mathematical verdict, but the source should be repaired
before publication.

## 1. Local power-image orders

Let

\[
E=N-1,
\qquad
S=K^E.
\]

Projection commutes with powering:

\[
\pi_p(x^E)=\pi_p(x)^E,
\qquad
\pi_q(x^E)=\pi_q(x)^E.
\]

Since the projections of \(K\) are \(K_p\) and \(K_q\), this gives exact
image equalities

\[
\pi_p(S)=K_p^E,
\qquad
\pi_q(S)=K_q^E.
\]

Both local groups are subgroups of finite-field multiplicative groups, so
they are cyclic. The image of the \(E\)-power map on a cyclic group of order
\(m\) has order \(m/\gcd(m,E)\). Hence the two projection orders are exactly

\[
A=\frac{m_p}{\gcd(m_p,E)},
\qquad
B=\frac{m_q}{\gcd(m_q,E)}.
\]

No assumption about the correlation inside \(K\) is used here.

## 2. The coprimality proof, including valuation cancellation and
\(\ell=2\)

Let \(e=v_\ell(N-1)\). If \(\ell\mid A\), then

\[
v_\ell(m_p)>e.
\]

Because \(m_p\mid p-1\), this implies

\[
p\equiv1\pmod{\ell^{e+1}}.
\]

Similarly, \(\ell\mid B\) would imply

\[
q\equiv1\pmod{\ell^{e+1}}.
\]

If both held, their product would satisfy

\[
N=pq\equiv1\pmod{\ell^{e+1}},
\]

contradicting \(v_\ell(N-1)=e\). Therefore no prime divides both \(A\) and
\(B\), and

\[
\gcd(A,B)=1.
\]

There is no missed valuation-cancellation case. Multiplying two numbers
that are each \(1\) modulo \(\ell^{e+1}\) cannot reduce that divisibility.
The product can acquire still higher valuation, but that also contradicts
the definition of \(e\).

The proof includes \(\ell=2\). If both residual local orders had a factor
two, then both hidden primes would be \(1\) modulo \(2^{e+1}\), which again
would force \(N-1\) to have valuation larger than \(e\). No odd-prime
identity is used.

## 3. Surjective projections force the full rectangle

The group \(S\) is a subgroup of

\[
K_p^E\times K_q^E,
\]

whose order is \(AB\). Each projection from \(S\) onto a local powered image
is surjective. By the first isomorphism theorem,

\[
A\mid|S|,
\qquad
B\mid|S|.
\]

Since \(\gcd(A,B)=1\), it follows that

\[
AB\mid|S|.
\]

But \(|S|\le AB\) because \(S\) is a subgroup of the product. Thus

\[
|S|=AB
\]

and the subgroup equals the full ambient product:

\[
S=K_p^E\times K_q^E.
\]

This proves more than the absence of one particular graph relation: no
cross-coordinate correlation remains. The argument remains valid if one or
both of \(A,B\) equal one.

Each local factor is cyclic, and their orders are coprime. Their direct
product is therefore cyclic of order \(AB\). Every prime in its exponent
occurs on exactly one local side. This statement is vacuous but still true
when \(S\) is trivial.

## 4. Exact positive-separator count and density

In the full product, a positive separator is either

\[
(1,y),\quad y\ne1,
\]

or

\[
(x,1),\quad x\ne1.
\]

The two sets are disjoint, so their exact total is

\[
(B-1)+(A-1)=A+B-2.
\]

Under uniform sampling, the exact density is

\[
\delta_E
=
\frac{A+B-2}{AB}
=
\frac1A+\frac1B-\frac2{AB}.
\]

If \(A=1<B\), every nonidentity point is \((1,y)\), and the same statement
holds with the sides reversed. Its success density is
\((B-1)/B\ge1/2\).

Now suppose \(A,B\ge2\). If, for example, \(A=\min\{A,B\}\le P\), then

\[
\delta_E
=
\frac1A+\frac{A-2}{AB}
\ge
\frac1A
\ge
\frac1P.
\]

The other case is symmetric. Thus inequality (5) is exact, including the
boundary \(A=2\).

## 5. Near-uniform public sampling is executable

Let the powered public generators be

\[
s_i=g_i^{N-1}\pmod N
\qquad(1\le i\le m).
\]

They generate \(S\). Their hidden orders are each less than \(N\), but the
algorithm does not need to know them. Choose independent uniform exponents
from a public power-of-two range of sufficiently many bits. For example,
with

\[
n=\lceil\log_2N\rceil,
\qquad
R=2^{3n+\lceil\log_2(m+1)\rceil},
\]

the reduction of each exponent modulo its generator order is close to
uniform, and the sum of all coordinate errors is less than \(2^{-2n}\).

Exact uniform coefficients modulo the generator orders push forward to the
uniform law on \(S\): the coefficient map is a surjective homomorphism and
all its fibres have equal size. Total variation cannot increase under this
map. Thus the public sampler is within negligible total variation of uniform
on \(S\), without computing a group order or factoring \(N\).

If \(A,B\ge2\) and one is at most a public polynomial \(P\), exact uniform
success is at least \(1/P\). If one order is one and \(S\ne1\), exact uniform
success is at least \(1/2\). The sampling error can be chosen smaller than
half of this public inverse-polynomial bound. Fresh independent trials
therefore have inverse-polynomial success probability.

The algorithm returns only a gcd strictly between \(1\) and \(N\), so every
return is correct. Repetition terminates almost surely and has polynomial
expected bit complexity. This is a valid conditional Las Vegas algorithm.
The hidden values \(A,B\) occur only in the success proof.

The candidate cites the previously proved P83 sampler instead of restating
these parameters. That citation is mathematically sufficient, although an
explicit error target tied to \(P\) would make the executable cost clearer.

## 6. Deterministic capped enumeration

Breadth-first closure from the identity under multiplication by the powered
generators reaches all of \(S\). Explicit inverse edges are unnecessary:
the inverse of a generator is a nonnegative power of it in a finite group.

Maintain a deterministic visited set. Stop a failing trial when the
\((T+1)\)-st distinct residue is discovered. This examines at most
\(O(mT)\) generator edges and stores \(O(T)\) residues, apart from the final
overflow item.

If

\[
1<AB=|S|\le T,
\]

the overflow never occurs. The queue closes after the complete group is
visited. Since \(A+B-2>0\), at least one visited residue is a positive
separator and its gcd gives a factor.

The candidate's phrase “stop after a public cap \(T\)” must be implemented
in this standard overflow form, or by stopping after \(T\) distinct
residues. If \(|S|=T\), those \(T\) residues already are the whole group, so
either reading preserves correctness.

For polynomial \(T\), a polynomial-size generator list, and polynomial
input encodings, modular powering, multiplication, deterministic lookup,
and gcd give deterministic polynomial bit complexity and storage.

## 7. Killing a synchronized graph and the quotient-size bound

Suppose \(K\) contains a diagonal graph subgroup \(H\) of order \(h\). Its
two local images have order \(h\), so

\[
h\mid p-1,\qquad h\mid q-1,
\]

and consequently

\[
h\mid N-1.
\]

Thus every \(h\in H\) satisfies \(h^{N-1}=1\). Because the ambient group is
abelian, the map

\[
K\longrightarrow S,\qquad x\longmapsto x^{N-1}
\]

is a homomorphism, and \(H\) lies in its kernel. It factors through \(K/H\).
The first isomorphism theorem gives

\[
|S|
=
\frac{|K|}{|\ker(x\mapsto x^{N-1})|}
\le
\frac{|K|}{|H|}
=
[K:H].
\]

No public description of \(H\), and no hidden value \(h\), is required to
execute the power. They occur only in this proof-side bound.

If \(S=1\), both local powered images are trivial, so

\[
m_p\mid N-1,\qquad m_q\mid N-1.
\]

Conversely, those divisibilities imply \(S=1\). The test is public: \(S=1\)
if and only if every supplied generator raised to \(N-1\) is one modulo
\(N\).

The statement that pure phase information disappears is structural, not an
extra algorithmic promise. The output is a full product with coprime local
orders, so it has no residual cross-field graph correlation. In the special
case of a strict pure-phase extension, all local orders already divide the
old graph order and hence \(N-1\), so the full image is trivial. A puncture
is needed to preserve that phase.

## 8. The \(N=4033\) witness

The retained certificate gives

\[
N=4033=37\cdot109,
\qquad
\operatorname{ord}_{37}(5)=36,
\qquad
\operatorname{ord}_{109}(5)=27.
\]

Also,

\[
E=N-1=4032,
\qquad
36\mid4032,
\qquad
\gcd(27,4032)=9.
\]

Therefore \(5^E\) has local orders one and three. It is a positive separator,
and

\[
\gcd(5^{4032}-1,4033)=37.
\]

The whole-subgroup orders \(A,B\) are also exactly \(1,3\), not merely lower
bounds from the element \(5\). On the \(37\)-side, \(m_p\mid36\mid4032\),
so \(A=1\). On the \(109\)-side, \(m_q\mid108=2^2\cdot3^3\), while
\(4032\) contains the full \(2\)-part and \(3^2\). Hence \(B\le3\). The
powered image of \(5\) has order three there, so \(B=3\).

The displayed residue is consistent with the certificate:

\[
4032\equiv9\pmod{27},
\qquad
5^9\equiv63\pmod{109}.
\]

The CRT conditions

\[
x\equiv1\pmod{37},
\qquad
x\equiv63\pmod{109}
\]

give \(x=3442\pmod{4033}\). Finally,

\[
3442-1=3441=37\cdot93,
\qquad
4033=37\cdot109,
\]

and \(\gcd(93,109)=1\), confirming the proper gcd \(37\).

This remains a fixed mechanism witness, not a source theorem for the base
five.

## 9. The \(N=2047\) witness

The retained certificate gives

\[
N=2047,
\qquad
K=\langle11,2\rangle,
\qquad
\exp(K)=22.
\]

Since

\[
N-1=2046=22\cdot93,
\]

the public power kills every element of \(K\):

\[
K^{N-1}=1.
\]

Thus both projection orders are one and

\[
A=B=1.
\]

The rectangular image has no separator. The earlier puncture

\[
(N-1)/11=186
\]

instead leaves an order-\(121\) image with \(20\) positive separators, as
claimed. This confirms that the full power and punctured power address
different structural branches.

## 10. Hidden proof data versus executable input

The proof uses the hidden factorization \(N=pq\), the local projection
orders \(m_p,m_q\), and the derived values \(A,B\). The fixed-witness proof
also uses certified local orders. None of these are algorithmic inputs.

The executable operations are only:

1. compute the public exponent \(N-1\);
2. power the supplied public generators modulo \(N\);
3. sample public exponent vectors or perform capped subgroup closure; and
4. compute gcds and return only proper divisors.

The condition \(S=1\) is publicly testable. The conditions
\(\min(A,B)\le P\) and \(AB\le T\) are not publicly tested; they are
conditional guarantees. Each individual trial remains bounded and every
returned factor is verified when those guarantees fail, but repeated random
sampling need not retain polynomial expected time or return a factor.

## 11. Exact scope of the pass

The theorem applies to a supplied public subgroup of the unit group modulo
a squarefree semiprime \(N=pq\) with distinct odd primes. It gives a
canonical public power whose image is a full product of coprime cyclic local
images. The polynomial-cost conclusions also require a polynomial-size
public generator list and polynomial-size encodings.

It does not show that feedback creates a nontrivial powered image, that one
local image has polynomial order, or that the full image has polynomial
order. It does not decode the case where both coprime local orders are
large, create the initial public generators from bare \(N\), handle general
composites, or establish an all-input factoring algorithm or novelty claim.

Within these boundaries, the structural and algorithmic claims pass.
