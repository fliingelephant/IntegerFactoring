# Proof of the F240 V2 divisor-lattice carry boundary

V2 changes only the decoder qualification.  It rejects the exact degenerate
case `(a,b)=(0,0)`.  Sections 1 and 3--6 retain the V1 mathematics.

## 1. Preliminary P205 identities

Write

\[
p-1=ds_p,\qquad q-1=ds_q,
\qquad \gcd(s_p,s_q)=1.
\]

Expanding `N-1` gives

\[
M=N-1=d\bigl(s_p+s_q+ds_ps_q\bigr).
\tag{P1}
\]

Thus `d | M`.  Put

\[
A={M\over d}=s_p+s_q+ds_ps_q.
\]

Reduction modulo either residual gives

\[
A\equiv s_q\pmod {s_p},\qquad
A\equiv s_p\pmod {s_q}.
\]

Since `gcd(s_p,s_q)=1`,

\[
\gcd(A,s_p)=\gcd(A,s_q)=1.
\tag{P2}
\]

In particular, for a prime `ell | s_i`,

\[
\ell\mid M\quad\Longleftrightarrow\quad \ell\mid d.
\tag{P3}
\]

The equality includes only support, not equal valuations: (P2) more
precisely gives `v_ell(M)=v_ell(d)` for such an `ell`.

## 2. Generalized centered-carry integrality

Let `B | M`, set `H_B=M/B`, and use the centers and residues from Theorem A.
The round-half-up definition gives

\[
-B/2\le x,y<B/2.
\]

Because `B | N-1`, one has `N congruent 1 mod B`.  Therefore

\[
xy\equiv (up)(uq)=u^2N\equiv u^2\pmod B.
\]

This proves that

\[
c={xy-u^2\over B}
\]

is an integer.

Expand the centered product in the integers:

\[
u^2N=(aB+x)(bB+y)
=abB^2+B(ay+bx)+xy.
\]

Substitute `N=1+BH_B` and `xy=u^2+cB`, cancel `u^2`, and divide by `B`:

\[
u^2H_B=abB+ay+bx+c.
\tag{P4}
\]

On the other hand,

\[
\begin{aligned}
u(aq+bp)
&=a(uq)+b(up)\\
&=a(bB+y)+b(aB+x)\\
&=2abB+ay+bx.
\end{aligned}
\]

Using (P4),

\[
u(aq+bp)=u^2H_B+abB-c.
\]

This proves (2), including divisibility of its numerator by `u` for the
true tuple.

Set `T=aq+bp`.  Since `q=N/p`,

\[
bp^2-Tp+aN=0.
\]

Finally,

\[
\begin{aligned}
T^2-4abN
&=(aq+bp)^2-4abpq\\
&=(aq-bp)^2.
\end{aligned}
\]

This proves (3) and (4).  The decoder first rejects negative `a` or `b`,
then rejects `(a,b)=(0,0)`.  If
`b>0`, it computes

\[
\Delta=T^2-4abN,
\]

requires \(\Delta\ge0\) to be a square, and tests both integer values

\[
X={T\mathbin\pm\sqrt\Delta\over2b}.
\]

It returns only a value with `1<X<N` that divides `N` exactly.  If
`b=0`, the gate gives `a>0`; the decoder requires `T!=0`, tests the
integer value `X=aN/T`, and applies the same proper-range and
exact-divisibility checks.  These rules make every returned answer safe for
an arbitrary guessed tuple.

For a true centered tuple, `a,b>=0`.  Round-half-up and positivity give

\[
a=0\Longleftrightarrow 2up<B,
\qquad
b=0\Longleftrightarrow 2uq<B.
\tag{P5}
\]

Since `p<q`, `b=0` implies `a=0`.  Therefore every true tuple that passes
the nondegeneracy gate has `b>0`, and its quadratic contains the root `p`.
The case `a=0<b` is safe: then `T=bp` and

\[
bX^2-TX=bX(X-p),
\]

so the candidates are `0` and `p`, and the proper-factor check selects
`p`.  A true tuple with `a>0,b=0` cannot occur.  The linear branch is
retained only to make arbitrary guessed tuples harmless.

The excluded case occurs at an allowed endpoint.  Take `B=M,u=1`.  For
distinct odd primes `p<q`, one has `p>=3,q>=5` and

\[
2p<M\Longleftrightarrow p(q-2)>1,
\qquad
2q<M\Longleftrightarrow q(p-2)>1.
\]

Thus (P5) gives `a=b=0`.  Also `x=p,y=q,c=(N-1)/M=1`,
`H_B=1`, and `T=0`.  Equation (3) is the zero polynomial.  It supplies
no candidate and must be skipped.

All remaining zero-center and residue endpoints are nondegenerate:

1. If `a=0<b`, the preceding factorization gives roots `0,p`.
2. If `a,b>0`, then `T=aq+bp>0`; even when the discriminant is zero,
   the repeated quadratic root is `p`.
3. Because `B | N-1`, one has `gcd(B,pq)=1`.  Hence `x=0` is
   equivalent to `B | u`, and then `y=0` also.  Writing `u=tB` gives

   \[
   a=tp,\qquad b=tq,\qquad c=-t^2B,
   \]

   and equation (3) is

   \[
   tq(X-p)^2=0.
   \]

   Thus a zero centered residue never creates a zero center; it gives the
   repeated valid root `p`.
4. The round-half-up negative endpoint `x=-B/2` implies `a>=1`, hence
   `b>=a>=1`.  If only `y=-B/2` is known, then still `b>=1`.
   The positive endpoint `B/2` is excluded by the half-open convention.
   Every residue-endpoint tuple is therefore nondegenerate.

This proves that `(a,b)!=(0,0)` is the necessary correction to every
direct factor-bank claim and is sufficient for every true tuple.

The residue bound gives

\[
|c|={|xy-u^2|\over B}
\le {|x||y|+u^2\over B}
\le {X\over2}+{u^2\over B},
\]

which is (5).  Conversely, (1) gives

\[
|xy|=|u^2+cB|\le u^2+CB.
\]

For any two real numbers, the smaller absolute value is at most the square
root of the absolute product.  This proves (6).

## 3. The common divisor and the `d=2` tie

Both `p-1` and `q-1` are even, so `d` is even and `d>=2`.

First suppose `d>=4`.  Since

\[
{p\over d}=s_p+{1\over d}
\]

and `0<1/d<1/2`, round-half-up selects `a=s_p`, leaving `x=1`.
The same calculation gives `b=s_q,y=1`.  Hence

\[
c={1\cdot1-1\over d}=0.
\]

Now suppose `d=2`.  The factor lies exactly on a rounding half-tie:

\[
{p\over2}=s_p+{1\over2}.
\]

Round-half-up selects

\[
a=s_p+1,
\]

and therefore

\[
x=p-2a=(2s_p+1)-2(s_p+1)=-1.
\]

Likewise `b=s_q+1,y=-1`, and again

\[
c={(-1)(-1)-1\over2}=0.
\]

This proves (7) and (8) without silently using the wrong representative at
the unique tie.

The window equivalence is immediate from the exact identity

\[
p-1=ds_p:
\qquad
s_p\le R
\Longleftrightarrow
d\ge {p-1\over R}.
\]

Because `d | M` and `d<=p-1`, exclusion of every divisor of `M` from the
displayed interval excludes `d`, and its contrapositive forces `s_p>R`.
An unrelated divisor in the interval gives no converse because nothing
makes that divisor divide both `p-1` and `q-1`.

## 4. Optimality inside the divisor-only grammar

Every prime divisor of a word in (11) divides `M`.  Hence a primary factor
`ell^e || s_i` with `ell` not dividing `M` is coprime to every such word and
survives completely in

\[
r_i(W)={s_i\over\gcd(s_i,W)}.
\]

Multiplying these exterior primary parts proves (13).

It remains to prove that `W_*=M^n` attains the bound.  If `ell | M`, then

\[
v_\ell(M^n)=n v_\ell(M)\ge n.
\]

On the other hand `s_i<N<2^n`, so

\[
v_\ell(s_i)<n.
\]

Thus `M^n` contains the entire `ell`-primary part of `s_i` for every
`ell | M`, while it contains no prime outside the support of `M`.  Exactly
the exterior part (12) remains, proving (15).

The bit length of `M^n` is

\[
\lfloor n\log_2M\rfloor+1=O(n^2).
\]

It can be formed by ordinary exponentiation from `N`; the factorization of
`M` is unnecessary.  Gcd, lcm, multiplication, positive powers, and exact
division cannot create a new prime outside the union of their input prime
supports.  This proves the stated narrow grammar boundary.

If a baseline `L` is allowed, the same support proof applies with `M`
replaced by `ML`.  The exponent `n` saturates every primary part of either
residual because those residuals are below `2^n`.  In particular, `R!`
supplies every prime at most `R`, and the divisor lattice supplies only
primes dividing `M`.

## 5. What additive carry information would have to supply

The definitions give the exact integer identities

\[
aB+x-u=up-u=u(p-1)
\]

and

\[
bB+y-u=uq-u=u(q-1).
\]

Therefore the first integer is divisible by `s_p`, and the second by
`s_q`.  A public word containing either true integer saturates the
corresponding P205 residual.  This proves the positive conditional claim in
Theorem D.

But the carry relation gives only

\[
xy=u^2+cB.
\]

When the right side is nonzero, even factoring its absolute value leaves the
selection of the true signed divisor `x` as a separate task in general.
The zero-product case is publicly recognizable and can be handled as a
degenerate branch.  Complete factorization and complete divisor enumeration
have different costs.  For example, let

\[
F_t=\prod_{j=1}^t \ell_j
\]

be a product of `t` distinct primes.  It has `2^t` positive divisors.  The
standard primorial estimate gives bit length `Theta(t log t)`, so its divisor
count is

\[
2^{\Theta(m/\log m)}
\]

for `m=log_2 F_t`.  This exceeds every numerical quasipolynomial in `m`.
One may avoid the standard estimate and use Bertrand's postulate to obtain
the weaker but still sufficient super-quasipolynomial relation
`m=O(t^2)` and `tau(F_t)=2^t=2^{Omega(sqrt(m))}`.

This divisor-count example is only an enumeration warning.  It is not a
lower bound against a clever selector, and it is not asserted that every
carry child has many divisors.  A semiprime-specific selector with a proved
quasipolynomial guarantee would be a materially new result outside this
boundary.

Finally, if `u=a=1` and `B` is additively close to `p`, then

\[
x=p-B.
\]

Enumerating `|x|<=X` tests `B+x` directly as a divisor of `N`.  Thus a
literal numerical-quasipolynomial near-factor interval is already a direct
factor bank.  Centered carry becomes a new mechanism only if it supplies a
selector or word without paying that hidden-offset enumeration.

## 6. Scope of the boundary

The proof does not say that factoring `K` is useless in every grammar.  It
says exactly that multiplicative reuse of its divisors is support-equivalent
to the simple word `M^n`.  Additive differences, shifted divisors, carry
children, adaptive modular tests, and Archimedean selection lie outside the
theorem.

Nor does the window implication prove an asymptotic counterfamily.  It is a
one-way exact implication: lack of a divisor in the stated hidden interval
makes the corresponding residual numerically larger.  Any theorem forcing
smoothness or a useful additive carry from that absence remains open.
