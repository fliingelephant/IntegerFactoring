# Proof of F245 V3

## 1. Inverse-quotient fibres and the adaptive bank

For `0<=k<N`, one has the exact fibre identity

\[
K^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\tag{P1}
\]

Indeed, `K(u)=k` gives `uv=Nk+1`, with `v<N`; hence `u>k` and `u` is a
divisor in (P1).  Conversely, a divisor `u` in (P1) gives
`v=(Nk+1)/u<N`.  Any common divisor of `u` and `N` would divide both
`Nk` and `Nk+1`, so `u` is a unit and `v` is its canonical inverse.

Since `Nk+1<N^2`, (P1) has at most `Delta_N` members.  Uniformity proves
(17).  Replacing zero by one merges at most two atoms and proves (18).  One
residue class modulo `ell` meets the support in at most `ceil(N/ell)`
integers.  Also

\[
{N\over\varphi(N)}={p\over p-1}{q\over q-1}\le {15\over8},
\qquad
\left\lceil{N\over\ell}\right\rceil<{2N\over\ell}.
\]

This proves (19).

For `i<j`, condition immediately before the accepted seed `j` is drawn.
The earlier `K_i` is fixed and the fresh `K_j` retains the residue-mass
bound.  Thus

\[
\Pr(K_j\equiv K_i\pmod\ell\mid\mathcal F_{j-1})
\le\beta_{N,\ell}.
\]

Replacing exact equality by the value `1` removes, rather than adds, odd
prime divisibility.  This proves (20).  Multiplying by the indicator that
seed `j` is actually requested handles stopping times.  There are at most
`B` singleton entries and `binom(B,2)` pair entries.  A union bound proves
(22).  Post-transcript selection and positive multiplicities cannot add
prime support.

The raw unit procedure is exact.  Conditional on `g_R=1`, every canonical
unit has the same original mass `1/N`.  A proper gcd occurs on the disjoint
events “a multiple of `p` but not `q`” and “a multiple of `q` but not `p`”,
so its probability is

\[
{p+q-2\over N}<{1\over p}+{1\over q}.
\tag{P2}
\]

The same calculation applies to a raw discriminant draw.

## 2. Sequential CRT--Linnik marker family

Choose four distinct marker primes in fixed comparable intervals above a
parameter `X`.  The first CRT modulus is

\[
M_1=24\lambda_+\lambda_-\rho_+\rho_-=X^{O(1)}.
\]

Every specified residue is a unit.  Linnik's theorem gives a prime `p` in
the class with `X<p<X^{O(1)}`.  Its residues give both lambda incidences and
both primitive `p` orders at the rho-markers.

Because `p` is primitive modulo each rho-marker and those markers exceed
`3`, neither rho-marker divides `p^2-1`.  After (28) is known, all moduli in
the second CRT system are therefore coprime.  For each `s>=5`, a unit
residue whose reduction is neither sign exists.  At a lambda-marker a
primitive residue is such a choice.  The second CRT class is reduced and
has modulus

\[
M_2=8\,3^{\max(e,2)}
\left(\prod_{s\ge5}s^{e_s}\right)\rho_+\rho_-
=O(p^2X^2).
\]

A second Linnik application gives `X<q<X^{O(1)}`.  The primes are distinct,
for example because `p=5 (mod 8)` and `q=3 (mod 8)`.  The second-stage
residues give both rho incidences and both primitive `q` orders at the
lambda-markers.

The 2-adic valuations are

\[
v_2(p-1)=2,\quad v_2(p+1)=1,
\quad v_2(q-1)=1,\quad v_2(q+1)=2.
\]

The 3-adic overlap occurs only between `p-1` and `q+1`, where its value is
exactly `3`.  Every prime at least `5` in `p^2-1` was excluded from both
signs on the `q` side.  This proves (26) and (30).

Both `p,q` are between `X` and `X^{O(1)}`.  Hence
`n=Theta(log X)`.  Decreasing one absolute constant gives (23) along an
unbounded sequence of `X`, and the resulting semiprimes are distinct.

## 3. Marker exclusion for explicit signed-power words

Modulo `lambda_a`, one has `N=aq`; modulo `rho_b`, one has `N=bp`.  If a
marker `ell` divides `|N^k-sigma|`, squaring gives

\[
q^{2k}=1\pmod\ell
\quad\hbox{or}\quad
p^{2k}=1\pmod\ell.
\]

The relevant cross residue is primitive, so `ell-1` divides `2k` and
`k>=(ell-1)/2`.  The single factor then has binary length
`Omega(kn)=2^{Omega(n)}`.  This exceeds every fixed numerical
quasipolynomial for sufficiently large family members.  Positive products
cannot cancel size and positive outer powers add no new prime support.  This
proves (31), including the explicit square baseline.

Also

\[
N-ab\equiv a(q-b)\pmod{p-a}.
\]

Thus

\[
\gcd(N-ab,p-a)=\gcd(p-a,q-b),
\tag{P3}
\]

and symmetrically on the `q` side.  The table (26) proves that neither
orientation marker divides `N-ab`.

A valid common order in orientation `(a,b)` divides
`gcd(p-a,q-b)`.  Taking the lcm over any number of tokens and all four
orientations, then using (26), proves

\[
M\mid\operatorname{lcm}(2,12,2,2)=12.
\]

The family primes exceed `3`, so `gcd(M,N)=1`.

## 4. Exact factor-free Hilbert--90 law

For a commutative ring `R`, define

\[
\mathcal A_D(R)=R[w]/(w^2-D),
\qquad
\overline{x_0+x_1w}=x_0-x_1w.
\]

Its norm is `x_0^2-Dx_1^2`.  An element is a unit exactly when its norm is a
unit, and then its inverse is its conjugate divided by the norm.  The screen
(11) therefore certifies the only inverse in (12).  Formula (14) gives all
later arithmetic without division.

Fix an odd prime `r` not dividing `D` and put
`epsilon=(D/r)`.  If `epsilon=+1`, the local algebra is
`F_r x F_r`, conjugation swaps the factors, and

\[
z\longmapsto z/\bar z
\]

maps its unit group onto a cyclic norm-one group of order `r-1`, with every
fibre of size `r-1`.  If `epsilon=-1`, the algebra is `F_{r^2}`,
conjugation is Frobenius, and the same map is `z -> z^{1-r}`.  Its kernel
has order `r-1` and its image is the cyclic norm-one group of order `r+1`.
Again every fibre has size `r-1`.

CRT makes a raw coefficient pair two independent uniform local algebra
elements.  The condition `g_\nu=1` is exactly that both are units.  This
conditioning factors into one local condition at each prime.  The accepted
local units remain independent and uniform, and the constant-fibre maps
produce independent uniform points in the full cyclic tori (34).

For fixed unit `D` modulo `r`, the norm-zero locus has `2r-1` coefficient
pairs when `D` is a square and one pair when it is a nonsquare.  Therefore

\[
\Pr(r\mid A^2-DB^2)<{2\over r}.
\tag{P4}
\]

The coefficient-zero event is a subset.  A union bound shows that one raw
coefficient draw returns a factor through (10) or (11) with probability
less than

\[
{2\over p}+{2\over q}.
\tag{P5}
\]

This is a raw-draw bound.  Rejection does not bias it.

## 5. Clean screens and the two-primary chain

For a uniform element in a cyclic group of order `m`, the kernel of the
`E`-power map has `gcd(E,m)` elements.  Since the grammar fixes `E` before
the fresh coefficient pair, conditioning on the past gives (35).

The coordinate screens are exact.  A hidden prime `r` divides `G_+(Y)`
exactly when the local point is `+1`, and divides `G_-(Y)` exactly when it
is `-1`.  A proper `G_+(V)` therefore implies exactly one local return under
`E`.

The chain is entered only after `V=+1` on both local sides.  More generally,
if a chain screen at `Y_j` is proper, one local component is a signed
identity.  A `+1` component remains `+1` through the remaining squares.  A
`-1` component becomes `+1` after the next square; an actual proper minus
screen cannot first occur at `j=v`, because `Y_v=V=+1` on both sides.
Hence every chain factor implies at least one local return at `Y_v=U^E`.
This proves the containment asserted after (35).

Conditional on a local return, the local point is uniform in the kernel of
the `E`-power map.  Its two-primary coordinate is uniform in the cyclic
group of order `2^{h_i}`.  For a uniform element of `C_{2^h}`, the exponent
`K` of its exact order has law

\[
\Pr(K=0)=2^{-h},
\qquad
\Pr(K=j)=2^{j-1-h}\quad(1\le j\le h).
\tag{P6}
\]

The two local coordinates remain independent after conditioning on both
returns.  The chain screens a factor exactly when their exact-order
exponents differ.  If `a_2<=b_2`, their equality probability is

\[
2^{-a_2-b_2}
\left(1+\sum_{j=1}^{a_2}4^{j-1}\right)
={4^{a_2}+2\over3\,2^{a_2+b_2}}.
\]

This proves statement equation (36).  The displayed equality probability
is at most `1/2` because it is largest when `b_2=a_2` and `a_2>=1`.

On every prior history whose current bank misses the four markers,
(31)--(32), (P3), and (7)--(9) show

\[
\lambda_a\nmid E,
\qquad
\rho_b\nmid E.
\]

Since the two markers divide the corresponding group orders,

\[
{\gcd(E,m_p)\over m_p}\le {1\over\lambda_a},
\qquad
{\gcd(E,m_q)\over m_q}\le {1\over\rho_b}.
\tag{P7}
\]

Thus, on every prior history whose current bank misses the six primes used
below, one clean trial has conditional factor probability at most `2/L`.

## 6. Exhaustive stopped-run bound

Let

\[
\mathcal S=\{p,q,\lambda_+,\lambda_-,\rho_+,\rho_-\}.
\]

Every member is a prime below `N` and at least `L`.  In fact, each marker is
strictly smaller than the hidden prime whose shifted order it divides.
Applying (22) and (19) to the six primes gives the safe bound

\[
\Pr(\text{some bank entry meets }\mathcal S)
\le48H_B{\Delta_N\over L}.
\tag{P8}
\]

If a legal direct word gcd is proper, then `p` or `q` divides an inverse
bank entry.  Indeed, every signed-power factor is congruent to a sign modulo
each hidden prime, `(N^2-1)^n` is coprime to `N`, `M|12` is coprime to `N`,
and `N-J` is coprime to `N`.  Hence (P8) covers all direct word-gcd exits.

There are at most `B` raw inverse-unit and discriminant draws of each type,
so (P2) gives a safe total contribution at most
`2B(1/p+1/q)`.  There are at most `B` raw coefficient pairs, so (P5) adds
at most `2B(1/p+1/q)`.  This proves the second term of (38).  There are at
most `B` clean trials.  At each trial, either the current bank has already
hit a prime in the set of (P8), or its history-wise conditional factor
probability is at most `2/L` by (P7).  Thus the clean trials add at most
`2B/L` outside the bank event; no conditioning on a future bank value is
used.

Section 1.5 permits no other factor return.  Common-order tokens themselves
cannot return a factor.  The three contributions therefore prove the
exhaustive bound (38), including adaptive control and unbounded rejection
tails cut off pathwise at `B` operations.

The standard maximum-order divisor estimate

\[
\max_{m\le x}\log\tau(m)=O(\log x/\log\log x)
\]

at `x=N^2` proves (39).  A numerical quasipolynomial and its square are
`2^{o(n)}`.  Equations (23), (38), and (39) therefore give an exponential
upper bound on stopped success.

If a confined Las Vegas factorer had expected running time at most `Q(n)`,
then

\[
\Pr(T\le2Q(n))\ge {1\over2}
\]

by Markov's inequality.  Halting means returning a verified factor, whereas
(38) makes that probability `2^{-Omega(n)}` on all sufficiently large
family members.  This contradiction proves the expected-time conclusion.

## 7. Carry algebra

The definitions in Section 5 of the statement give

\[
X=A_0v-Nq_A,
\qquad
Y=B_0v-Nq_B,
\qquad
gv-1=N\widetilde d.
\]

Direct substitution yields (40).  Also

\[
A_0^2-DB_0^2=(a_0^2-Db_0^2)^2=g^2.
\]

Using `gX=A_0+Nk` and `gY=B_0+Nl`, expand

\[
g^2(X^2-DY^2)
=g^2+2N(A_0k-DB_0l)+N^2(k^2-Dl^2).
\]

Subtract `g^2` and divide by `Ng^2` to obtain (41).  The numerator is an
integer because `X^2-DY^2=1 (mod N)`.  For a signed or noncanonical
`g=r+tN`, with canonical unit residue `r`,

\[
\widetilde d=K(r)+tv.
\]

This does not transfer the fresh canonical atom law to the nonlinear terms
in (40)--(41), which remain outside the grammar.
