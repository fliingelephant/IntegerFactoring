# F158 candidate — certified quadratic lifts give a factor-or-double win–win

## Status and scope

This is a proof-only decoder and progress-template candidate. It is not a
factoring algorithm because it does not construct the required sequence of
quadratic lifts.

The closest results are P138, F154 V3, and P139. P138 says that a failed
many-relation decoder is one decorated section. F154 turns that section into
public canonical inverse representatives whose squares lie in the old
multiplicative subgroup. P139 supplies certified high order but not the
needed square roots.

The material difference is a monotone capacity law. If the old subgroup is
small enough to enumerate, every supplied quadratic lift either factors
`N`, is already old, or doubles the subgroup in both hidden components. If
the old subgroup has one certified common-order generator, the same test is
compact and does not enumerate the subgroup. A chain of genuine lifts then
doubles a public order until the square-root scale forbids another no-factor
step.

Throughout, let

\[
N=pq,
\qquad
3\le p<q
\tag{1}
\]

with distinct odd primes, and let

\[
U_N=(\mathbf Z/N\mathbf Z)^\times.
\]

All residues below are represented canonically, but the group statements
are modulo `N`.

## 1. Explicit-subgroup lift test

Let `H` be a finite public subgroup of `U_N`, supplied as a complete list.
Let `x` be a public unit such that

\[
x^2\in H.
\tag{2}
\]

Scan

\[
d_h=\gcd(x-h,N),
\qquad h\in H.
\tag{3}
\]

Use the following priority rule.

1. If some `d_h` is proper, return it as a factor of `N`.
2. Otherwise, if some `d_h=N`, then `x=h` modulo `N` and `x\in H`.
3. Otherwise every `d_h=1`. Then the images of `x` lie outside the images of `H` in
   both hidden fields, and

   \[
   |\langle H_r,x\rangle|=2|H_r|,
   \qquad r\in\{p,q\}.
   \tag{4}
   \]

   Also `|\langle H,x\rangle|=2|H|` globally.

The scan takes `|H|` gcds. It is quasipolynomial when the explicit list of
`H` has quasipolynomial size.

The F154 V3 witness is a strict finite instance. For `N=77`, let

\[
H=\langle9\rangle,
\qquad |H|=15,
\qquad x=26.
\tag{4a}
\]

Then

\[
x^2\equiv60\equiv9^{-1}\pmod {77},
\]

so `x^2\in H`, while

\[
\gcd(x-9^2,77)=\gcd(-55,77)=11.
\tag{4b}
\]

Thus the subgroup-membership scan converts that refinement-mediated endpoint
into a factor. This remains a finite capability witness: `x` was already the
public inverse of `3`, and no all-input lift source follows.

For a sequence

\[
H_i=\langle H_{i-1},x_i\rangle,
\qquad
x_i^2\in H_{i-1},
\tag{5}
\]

every no-factor, non-inert step doubles the global subgroup and both local
images. After `t` such steps,

\[
|H_t|=2^t|H_0|,
\qquad
|(H_t)_r|=2^t|(H_0)_r|.
\tag{6}
\]

Explicit enumeration therefore remains quasipolynomial for only a
polylogarithmic number of doublings. This version alone does not reach the
hidden-prime capacity bound in quasipolynomial time.

## 2. Public common-order certificate

Let `g\in U_N`. Let `M\ge1` have a supplied rational-prime factorization.
Assume

\[
g^M\equiv1\pmod N
\tag{7}
\]

and, for every rational prime `ell` dividing `M`,

\[
\gcd(g^{M/\ell}-1,N)=1.
\tag{8}
\]

Then

\[
\boxed{
\operatorname{ord}_p(g)=\operatorname{ord}_q(g)=M.
}
\tag{9}

Call `(g,M)` a **certified common-order generator**.

Every odd input has the public initial certificate

\[
\boxed{(g_0,M_0)=(-1,2).}
\tag{9a}

Indeed `-1` has exact order two in both hidden fields, and the only
certificate screen is `gcd(-2,N)=1`. Thus the compact tower does not need an
extra starting-generator theorem. Its missing input is the next external
quadratic lift.

## 3. Compact quadratic-lift test

Assume `(g,M)` is a certified common-order generator. Let `x\in U_N` and
let `a` be a public integer such that

\[
x^2\equiv g^a\pmod N,
\qquad
\gcd(a,M)=1.
\tag{10}

Solve the public linear congruence

\[
2k\equiv a\pmod M.
\tag{11}

There are at most two solutions modulo `M`. For each solution, test

\[
\gcd(x-g^k,N).
\tag{12}

Then exactly one of the following occurs.

1. A gcd in (12) is proper and factors `N`.
2. A gcd in (12) equals `N`, so `x\in\langle g\rangle` and the lift is
   inert.
3. Equation (11) has no solution, or every gcd in (12) is one. Then `x`
   lies outside `\langle g\rangle` in both hidden fields and

   \[
   \boxed{
   \operatorname{ord}_p(x)=\operatorname{ord}_q(x)=2M.
   }
   \tag{13}
   \]

   Hence `(x,2M)` is the next certified common-order generator.

The test uses at most two gcds plus modular exponentiation and arithmetic in
the supplied factorization of `M`. Its cost is polynomial in the explicit
bit lengths.

## 4. Compact tower and public capacity cutoff

Start from a certified `(g_0,M_0)`. At level `i`, suppose a public source
supplies

\[
x_i^2\equiv g_{i-1}^{a_i}\pmod N,
\qquad
\gcd(a_i,M_{i-1})=1.
\tag{14}

Apply the compact test. On every no-factor, non-inert branch, put

\[
g_i=x_i,
\qquad
M_i=2M_{i-1}.
\tag{15}

After `t` genuine expansions,

\[
M_t=2^tM_0
\quad\text{and}\quad
M_t\mid p-1,\ q-1.
\tag{16}

Since `p<\sqrt N`, no such branch can satisfy

\[
2^tM_0\ge\sqrt N.
\tag{17}

Therefore a source that supplies a non-inert coprime quadratic lift at every
level up to the first `t` satisfying (17) gives a deterministic
polynomial-time factorization procedure. The decoder and progress proof are
already polynomial. The unproved source statement is the entire missing
algorithmic step.

Starting from the universal pair `(-1,2)`, every coprime exponent `a_i` is
odd and every genuine expansion produces a unit of exact common order
`2^(i+1)`. The first missing source object is a square root of `-1` modulo
`N`. On inputs where no aligned root is publicly supplied, the theorem gives
no way to create one.

## 5. Exact relation to section feedback

In F154 notation, let

\[
H=\langle q_1,\ldots,q_m\rangle.
\]

Every section-completion inverse representative satisfies

\[
s_v^2\equiv Q(v)^{-1}\in H.
\tag{18}

Thus every `s_v` is a legal quadratic lift for the explicit-subgroup test.
If the old named subgroup has quasipolynomial explicit size, F154 completion
now has an exact outcome:

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{old endpoint}
\quad\lor\quad
\text{double both hidden subgroup images}.
}
\tag{19}

If instead `H` has a certified common-order generator `g`, and the source
also supplies the exponent presentation

\[
Q(v)^{-1}=g^a,
\qquad
\gcd(a,M)=1,
\tag{20}

the compact tower applies.

F158 does not prove that F154 or F156 supplies such a vector at every level.
The starting pair `(-1,2)` is free, but a coprime non-inert lift above it is
not. The theorem isolates that lift supply as the exact source-side problem.

## 6. Precise remaining theorem

A complete factoring theorem would follow from this source claim:

> For every surviving composite input and every certified common-order state
> below the square-root capacity, a uniform polynomial- or
> quasipolynomial-time canonical-relation source returns a factor or a
> public non-inert lift `x^2=g^a` with `gcd(a,M)=1`.

No current result proves this claim. Relation count, row reuse, subgroup
expansion without a known order, and arbitrary square roots over a
multigenerator subgroup are insufficient substitutes.
