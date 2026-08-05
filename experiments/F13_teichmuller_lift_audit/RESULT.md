# Hostile audit of F13 Teichmuller lift kill

Approach-family ID: F13_teichmuller_lift_audit.

**Verdict: PASS WITH ONE REQUIRED THEOREM CORRECTION.** The principal-kernel
erasure, local twisted-Teichmuller formula, power-map criterion, hidden-
$p+q$ identity, consecutive-iterate probability, additive category formula,
and balanced high-digit upper bound are correct under their exact
unit/uniformity hypotheses. The finite certificate is reproducible and its
recorded hashes are exact.

The exception is substantive but local: the twin-prime theorem as written
claims to cover $q=p+2>3$, which includes $(p,q)=(3,5)$. Its category counts
and probability formula are false there. The theorem must require $p>3$
(equivalently $q>5$). At the exceptional pair, the exact category counts are
$(0,1,1)$ and $(3,0,1)$, and the two-stage success probability is $7/8$,
not $1/2$.

This audit accepts a corrected, carrier-specific obstruction. It does not
accept a factoring lower bound, an untwisting-hardness claim, or a top-level
factoring algorithm.

## 1. Independently derived structural statement

Let $p<q$ be distinct odd primes, $N=pq$, and

\[
\tau_N(a)=a^N\pmod {N^2}.
\]

For a prime $\ell$, write $[x]_\ell=x^\ell\pmod{\ell^2}$. This is the unique
Teichmuller lift of $x\bmod\ell$. Every local unit has a unique decomposition

\[
a=[a]_p(1+pu)\pmod {p^2}.
\]

Raising the principal factor to $pq$ kills it modulo $p^2$, while
$[a]_p^p=[a]_p$. Hence, independently of the author source,

\[
\tau_N(a)\equiv[a]_p^q\pmod {p^2},\qquad
\tau_N(a)\equiv[a]_q^p\pmod {q^2}.                 \tag{A1}
\]

The same formula, with $[0]_\ell=0$, also handles nonunits.

The reduction kernel is exactly

\[
K=\{1+kN\pmod {N^2}:k\bmod N\}.
\]

Its local principal coordinates are $qk\bmod p$ and $pk\bmod q$, a
bijection by CRT. Direct binomial expansion gives

\[
(1+kN)^N\equiv1\pmod {N^2},\qquad
(a+Nt)^N\equiv a^N\pmod {N^2}.                    \tag{A2}
\]

Thus $\tau_N$ erases every input degree of freedom in $K$ and factors
through reduction modulo $N$. This does **not** say its output high digit
contains no information: that digit is a deterministic function of the
residue modulo $N$.

On the Teichmuller subgroup, $\tau_N$ is the exponent-$N$ map on
$C_{p-1}\times C_{q-1}$. With

\[
\lambda=\operatorname{lcm}(p-1,q-1),
\]

it is bijective exactly when $\gcd(N,\lambda)=1$. If
$dN\equiv1\pmod\lambda$, then

\[
\tau_N(a)^d=([a]_p,[a]_q).                        \tag{A3}
\]

For $p<q$, the only possible obstruction is $p\mid q-1$: $q$ cannot divide
either $p-1$ or $q-1$, and $p\nmid p-1$. In particular, every odd balanced
pair $p<q<2p$ has $\gcd(N,\lambda)=1$, because $p\mid q-1$ would force
$q=p+1$, impossible for two odd primes. At $N=3\cdot7$,
$\gcd(N,\lambda)=3$; A01 independently exhibited distinct Teichmuller
elements $1,361\bmod441$ having the same image $1$.

Computing $d$ from the factors is a valid factor-aware untwist. Neither the
author experiment nor this audit proves that every way of untwisting is
equivalent to factoring.

For uniform $k\bmod N$, the exact probability that its explicit kernel
coordinate already yields a proper gcd is

\[
\Pr(1<\gcd(k,N)<N)=\frac{p+q-2}{N}.
\]

This is ordinary random gcd sampling, and (A2) maps all those kernel inputs
to $1$.

## 2. Hidden-sum identity and its exact scope

Let $A=\tau_N(a)$. In each local component, $A$ is either zero or a
Teichmuller unit. Since

\[
(N+1)-(p+q)=(p-1)(q-1),
\]

the corrected strongest scope is

\[
\boxed{A^{N+1}=A^{p+q}\pmod {N^2}}                \tag{A4}
\]

for **every** residue $a\bmod N^2$, not only units. A01 checked (A4) on all
residue classes modulo $N$ for the seven instances through $N=10{,}403$,
and on 258 named residue classes for each larger instance. This suffices
because (A2) makes the choice of lift modulo $N^2$ irrelevant.

For a unit $A$, (A4) supplies only
$p+q\equiv N+1\pmod{\operatorname{ord}(A)}$ from this equality alone. Any
statement that extracting $p+q$ is hard remains outside the proof. The
comparison with an earlier scalar order-spectrum route is descriptive, not
a reduction or lower bound.

## 3. Consecutive iterate differences

For unit $a$ and every $r\ge1$, repeated use of (A1) gives

\[
\tau_N^r(a)\equiv[a]_p^{q^r}\pmod {p^2},\qquad
\tau_N^r(a)\equiv[a]_q^{p^r}\pmod {q^2}.          \tag{A5}
\]

If two local Teichmuller values agree modulo the local prime, uniqueness of
the lift makes them equal modulo its square. Therefore the consecutive
difference $\tau_N^{r+1}(a)-\tau_N^r(a)$ has no valuation-one category.
This conclusion is for these consecutive differences; it must not be
silently generalized to arbitrary linear combinations of iterates.

For a uniform unit, local CRT coordinates are independent. Exact root
counting in the two cyclic groups gives

\[
P_p=\frac{\gcd(q-1,p-1)}{p-1},\qquad
P_q(r)=\frac{\gcd(p^r(p-1),q-1)}{q-1}.            \tag{A6}
\]

Thus the proper-gcd probability is the xor probability

\[
P_p(1-P_q(r))+(1-P_p)P_q(r).                      \tag{A7}
\]

For odd $p<q<2p$, $p\nmid q-1$, so both probabilities reduce using
$g=\gcd(p-1,q-1)$ and (A7) is independent of $r$. A01 enumerated the local
cyclic groups for all nine author instances and reproduced every reported
first-, second-, and third-difference probability. It also reproduced the
fully synchronized zero-success case $3\cdot7$.

## 4. Additive defect and the twin-prime correction

For unit $a,b$, multiplicativity of the Teichmuller lift lets one divide the
local additive defect by a unit and reduce it to the uniform local ratio
$t=a/b$. If $\pi_{\ell,c}$ is the exact probability that

\[
[t+1]_\ell^e-[t]_\ell^e-1
\]

has valuation category $c\in\{0,1,2\}$, then the two local categories are
independent. The first gcd, followed only when it is $N$ by the quotient
gcd, succeeds exactly when the categories differ. Therefore

\[
\Pr(\text{success})=1-\sum_{c=0}^2\pi_{p,c}\pi_{q,c},                \tag{A8}
\]

and the genuinely new second-stage contribution is

\[
\pi_{p,1}\pi_{q,2}+\pi_{p,2}\pi_{q,1}.            \tag{A9}
\]

A01 recomputed all local distributions without importing the author code,
then directly enumerated every ordered pair of global units through
$N=221$. The local formula and direct global computation agreed. All nine
exact probabilities in the author table were reproduced.

For twin primes $q=p+2$ with **$p>3$**, the local exponents reduce to $3$ at
$p$ and $-1$ at $q$. Modulo $p$, the first defect is $3t(t+1)$, so $t=-1$
is its only root; it is an exact Teichmuller equality. Since twin primes
above $(3,5)$ satisfy $q\equiv1\pmod6$, the second component has $t=-1$ and
the two nontrivial cube roots of unity; all three are again exact lift
equalities. Hence the correct counts are

\[
(p-2,0,1),\qquad(q-4,0,3),                        \tag{A10}
\]

and

\[
\Pr(\text{success})=
\frac{4(p-2)}{(p-1)(p+1)}.                        \tag{A11}
\]

At $p=3,q=5$, the factor $3$ in the first defect vanishes modulo $p$, and
$q\not\equiv1\pmod3$. The exact replacement is

\[
(0,1,1),\qquad(3,0,1),\qquad
\Pr(\text{success})=\frac78.                     \tag{A12}
\]

A01 verified (A10)--(A11) for every twin-prime pair below $202$ with $p>3$,
and verified (A12) separately. The author's phrase “the two tested
twin-prime pairs” should also be made explicit: its instance list contains
four $p>3$ twin pairs, plus the exceptional pair $(3,5)$; only two of the
three designated large instances are twin pairs.

## 5. Balanced high-digit theorem

For $B_r=\tau_N^r(a)$, let $b_r\in[0,N)$ be its reduction modulo $N$ and

\[
H_r=(B_r-b_r)/N\pmod N.
\]

Assume $a$ is a uniform unit and $p<q<2p$ are odd. The exponent maps in (A5)
permute the two local unit groups, so the pair of local residues of $B_r$ is
uniform and independent for every fixed $r$.

Fix the residue $x\ne0\pmod p$. The canonical CRT representative is
$b=x+pk$ with $k\in\{0,\ldots,q-1\}$, except for the single choice that
makes $b\equiv0\pmod q$. The condition $p\mid H_r$ is equivalent to
$b\equiv[x]_p\pmod{p^2}$, hence selects one class of $k\bmod p$. Because
$q<2p$, at most two of the $q-1$ allowed residues qualify. Therefore

\[
\Pr(p\mid H_r)\le\frac2{q-1}.                    \tag{A13}
\]

Fixing the residue modulo $q$ instead writes $b=y+qk$ with $0\le k<p<q$.
One class modulo $q$ contains at most one such $k$, so

\[
\Pr(q\mid H_r)\le\frac1{p-1}.                    \tag{A14}
\]

The proper-gcd event is contained in the union of these divisibility events.
For any fixed set of $K$ observed iterates, no independence among iterates
is needed:

\[
\Pr(\exists r:1<\gcd(H_r,N)<N)
\le K\left(\frac2{q-1}+\frac1{p-1}\right)
\le\frac{3K}{p-1}.                               \tag{A15}
\]

A01 exhaustively checked the fibre bounds $2$ and $1$ on all 90 odd-prime
pairs $p<q<2p$ with $q<80$, independently reproduced the seven feasible
three-iterate union probabilities, and reproduced the $13/680$ marginal and
$571/10200$ union values at $101\cdot103$.

Bertrand's postulate supplies infinitely many such balanced semiprimes, and
$p=\Theta(\sqrt N)$, so $K=\operatorname{poly}(\log N)$ makes (A15)
exponentially small in the input bit length. This is exactly a theorem for
uniform units and a fixed collection of observed iterates. Uniform residues
with an initial gcd check add only another $O(K/p)$ random-gcd term. The
proof does not cover deliberately engineered, deterministic, or adaptive
bases whose distribution is not uniform.

## 6. Finite reproduction and provenance

A01 was a new standard-library implementation. It did not import the author
source or read the author JSON to recompute any mathematical value. It
performed:

- full structural checks on all residue classes modulo $N$ through
  $N=10{,}403$, including nonunits for (A4), and 258 named residue classes
  on each larger input;
- full kernel-coordinate checks through $N=10{,}403$;
- exact local additive distributions for all nine inputs and direct global
  pair enumeration through $N=221$;
- independent cyclic-group enumeration for all three consecutive
  differences on all nine inputs;
- exhaustive three-iterate high-digit enumeration through $N=10{,}403$;
- the 90-pair balanced high-digit fibre census and all twin-prime pairs below
  $202$.

A02 independently repeated the author's named fixed probes. For every one of
the nine instances it reproduced the number of bases and pairs, every
retained first-20 hit list, and the rounded exponent. All nine rounded
$2\sqrt N$ exponents happened to equal the true $p+q$, so all nine rounded
defects were zero in both components. At the three large inputs, the
additive/iterate/high-digit/rounded hit counts were respectively
$(2,0,4,0)$, $(0,3,2,0)$, and $(0,0,0,0)$, exactly as in the author output.
A03 compared the independently generated A02 certificate byte-addressedly
against the hashed author R01 JSON and passed all eight retained fields on
all nine instances.

Every asserted comparison passed except the deliberately isolated $(3,5)$
correction. The four author artifact hashes in its manifest match the current
bytes exactly, including the source hash embedded in its JSON. The author
recorded one successful run and no failed attempts; the retained wrapper has
a real 180-second hard timeout and its log records PASS.

## 7. Accepted scope

The corrected result establishes:

1. complete erasure of the principal **input** kernel by $\tau_N$;
2. an exact twisted power map on the Teichmuller quotient;
3. exact carrier formulas for consecutive differences and additive defects;
4. an exponentially small uniform-polylog success upper bound for the
   explicit high-digit carrier on an infinite balanced family.

It does not establish classical hardness of orders or untwisting, exclude
all constructions over $\mathbb Z/N^2\mathbb Z$, or satisfy the top-level
factoring goal.
