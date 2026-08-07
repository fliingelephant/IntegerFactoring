# F54 candidate: the first branch of \(x(x-1)\) can disappear

## Status and scope

**Status:** narrow kill-first result for F29. It has not had a hostile audit
or a proof-blind reconstruction.

This result treats

\[
H(x)=x(x-1)
\]

and its public affine conjugates. It does not give a lower bound for general
polynomial dynamics. In particular, it does not cover unrelated quadratics,
an \(N\)-dependent map designed to defeat the obstruction, extra state,
correlated starts, valuation lifts, or a decoder that uses the full orbit
instead of target-root gcd tickets. It also does not cover arbitrary public
target points that are not roots of the submitted polynomial.

The obstruction is different from P52. P52 uses a rational Newton map that
is conjugate to squaring and has singleton root basins. Here the polynomial
map is noninvertible and has branching preimages. On an infinite prime
family, the first new branch has no point, so the complete basin still has
only two points. P45 does not apply because \(H\) is not a bijection.

## 1. Exact local basin closure

Let \(p\ne5\) be an odd prime. Put

\[
A=\{0,1\}\subset\mathbb F_p.
\]

Assume that \(5\) is a quadratic nonresidue modulo \(p\). Then

\[
\boxed{H^{-1}(A)=A.}
\tag{1.1}
\]

Indeed,

\[
H(x)=0
\quad\Longleftrightarrow\quad
x\in\{0,1\}.
\]

The other possible branch is

\[
H(x)=1
\quad\Longleftrightarrow\quad
x^2-x-1=0.
\]

Its discriminant is \(5\), so it has no solution under the hypothesis.
This proves (1.1).

It follows by induction that, for every \(t\ge0\),

\[
H^t(u)\in A\text{ for some }t
\quad\Longleftrightarrow\quad
u\in A.
\tag{1.2}
\]

Thus repeated composition can have formal degree \(2^t\), but the useful
backward basin does not grow at all.

## 2. Exact semiprime success probability

Let

\[
N=pq,
\]

where \(p\ne q\) are odd primes and \(5\) is a quadratic nonresidue modulo
both primes. Start with a uniform residue \(U\bmod N\). At every iteration,
allow the strongest separate menu for the two public roots:

\[
\gcd(x_i,N),
\qquad
\gcd(x_i-1,N),
\qquad
x_{i+1}=H(x_i)\bmod N.
\tag{2.1}
\]

The number of iterations is arbitrary.

By (1.2), a local orbit reaches a root if and only if its local start is in
\(A\). A proper gcd occurs unless both local starts avoid \(A\), or both
local starts equal the same element of \(A\). Therefore the exact number of
successful CRT classes is

\[
pq-(p-2)(q-2)-2=2p+2q-6.
\]

Hence one raw-residue restart succeeds with probability

\[
\boxed{
\frac{2p+2q-6}{pq}.
}
\tag{2.2}
\]

This is an upper bound for any sub-menu of the two root tickets.

If the start is uniform in
\((\mathbb Z/N\mathbb Z)^\times\), only the local value \(1\) remains in the
root basin. The exact success probability becomes

\[
\boxed{
\frac{p+q-4}{(p-1)(q-1)}.
}
\tag{2.3}
\]

A polynomial-size menu of global roots does not add a factor-free target.
If \(a(a-1)=0\bmod N\), then \(a\) has one of four CRT patterns. The two
mixed patterns give a proper factor through \(\gcd(a,N)\). On the branch
where root construction did not already factor \(N\), only \(a=0,1\)
remain.

## 3. Natural random scaling gives the same process

Let \(c\in(\mathbb Z/N\mathbb Z)^\times\) be fixed or sampled uniformly, and
define

\[
H_c(x)=cH(x/c)=\frac{x(x-c)}{c}.
\tag{3.1}
\]

This is a public quadratic with the public roots \(0,c\). The change of
coordinate \(x=cy\) gives the exact conjugacy

\[
H_c(cy)=cH(y).
\tag{3.2}
\]

For every hidden prime divisor \(r\mid N\) at which \(5\) is a nonresidue,

\[
H_c^{-1}(\{0,c\})=\{0,c\}
\quad\text{in }\mathbb F_r.
\tag{3.3}
\]

Multiplication by a unit preserves uniform starts and preserves every gcd
ticket. Thus (2.2) and (2.3) hold for every unit \(c\), not only on average.
Uniform random scaling gives no gain.

More generally, every affine state relabeling

\[
S(y)=a+cy,
\qquad
S\circ H\circ S^{-1},
\]

has the same two-point basin for the relabeled target set
\(S(A)=\{a,a+c\}\). If the targets must be literal zeros, (3.1) is the
corresponding root-preserving subfamily.

If \(c\) is first sampled as a raw residue, screening \(\gcd(c,N)\) can itself
factor \(N\). Its one-draw probability is

\[
\frac{p+q-2}{pq},
\]

which is of the same small order. Conditioned on acceptance, \(c\) is a
uniform unit and the conjugacy applies. An extra mixed root of \(H_c\) also
already exposes a factor through \(\gcd(a,N)\) or \(\gcd(a-c,N)\).

## 4. Infinite balanced obstruction family

For every prime \(p\equiv2\pmod5\), quadratic reciprocity gives

\[
\left(\frac{5}{p}\right)
=
\left(\frac{p}{5}\right)
=-1.
\]

The prime number theorem in arithmetic progressions supplies two distinct
primes \(p,q\equiv2\pmod5\) in \([X,2X]\) for every sufficiently large
\(X\). These give an infinite balanced semiprime family.

On this family, (2.2), (2.3), and the random-scaling variant are all

\[
O(N^{-1/2}).
\]

Therefore polynomially many iterations and polynomially many independent
restarts have negligible success probability. Repeat-until-success needs

\[
\Omega(\sqrt N)
\]

restarts in expectation. This is exponential in the input bit length.

## 5. What a surviving basin sampler must prove

For a general public map \(F_N\), a local target set \(A_r\), and an iteration
cap \(t\), define the backward basin

\[
B_{r,t}
=
\{u\in\mathbb F_r:
F_{N,r}^{\,i}(u)\in A_r
\text{ for some }0\le i\le t\}.
\]

With a uniform CRT start, every target-ticket factor event is contained in
the event that at least one local start lies in its backward basin. Hence

\[
\Pr(\text{factor by time }t)
\le
\frac{|B_{p,t}|}{p}
+
\frac{|B_{q,t}|}{q}.
\tag{5.1}
\]

This statement is for the factor-free branch after the map and its targets
have been constructed. A coefficient or target that already has a proper gcd
with \(N\) is an immediate factor and does not need basin dynamics.

For a randomized public map, the same bound holds after averaging over the
public randomness. Thus a proposed sampler needs an inverse-polynomial
average basin density on every balanced semiprime. Exponential formal degree
does not establish this. It must prove that the local inverse tree has enough
actual points even for adversarial hidden primes. This condition is
necessary, not sufficient, because the two local hit-time signatures can
still synchronize.

The fixed map \(x(x-1)\) and its affine-conjugate randomization fail this
condition on the family above. Unrelated quadratics remain open.

## 6. Finite cross-check

The preregistered run F54-D01 checked the formulas through finite ranges:

- 49 primes through 509 with \(5\) a nonresidue;
- 10,954 nonzero scaling parameters;
- 55 distinct semiprime pairs with factors through 79.

It found no counterexample. The source, timeout, log, output, hashes, and
finite-only disposition are recorded in `RUN_MANIFEST.md`. The finite run is
not used to prove any unbounded statement.

## Conclusion

Branching is not enough. For \(x(x-1)\), an infinite balanced input family
removes the first new inverse branch. The entire useful basin then stays at
two points for any number of cheap iterations. Random affine relabeling does
not change this. A new polynomial-dynamics proposal must control actual
backward-basin mass over every hidden prime, not only the degree of the
composed polynomial.
