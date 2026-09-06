# F187 hostile audit

## Verdict

**PASS.** I found no false formula, omitted branch, hidden squarefreeness
assumption, or unjustified quasipolynomial recurrence in the frozen claim.
The result proves a narrow obstruction for independent uniform-base
sampling after complete factorization of \((N-1)/2\). It does not prove a
factoring algorithm or a lower bound against adaptive or deterministic
bases.

I did not edit a frozen input or a durable ledger. I did not run a
mathematical computation, use an experimental check, or perform the later
blind reconstruction.

## Frozen-input integrity

The files matched `MANIFEST.md` before review:

- `STATEMENT.md`:
  `9434188bf8c35cbd54d0f6f553b7e0698f19470745515bb1fe503fbe8b67f14e`
- `PROOF.md`:
  `0f3790117a8e6ed34fbdaa934b576cbdec2ef248865ef9c5268aeb262f77f7cb`
- `SELF_AUDIT.md`:
  `cc77bd2116d0e2309e1ee20c57dfbf225a814546a20228478ada7cf2b008854b`

The manifest itself had SHA-256
`55f256e01fc6359ce29f2e01b9a1308b9359c81ebe5471402e72501277bc6dee`.

## 1. Arbitrary odd composite and prime-power audit

For a hidden component \(R_i=p_i^{e_i}\), its unit group is cyclic of
order

\[
h_i=p_i^{e_i-1}(p_i-1).
\]

Because \(p_i\mid N\), one has \(p_i\nmid N-1\). Therefore

\[
d_i=\gcd(N-1,h_i)=\gcd(N-1,p_i-1).
\]

The \((N-1)\)-torsion subgroup has order \(d_i\), which is coprime to
\(p_i\). The reduction kernel from units modulo \(p_i^{e_i}\) to units
modulo \(p_i\) is a \(p_i\)-group. Its intersection with this torsion
subgroup is trivial. Thus, after the full-return test, a later tested power
is one modulo \(p_i\) exactly when it is one modulo \(p_i^{e_i}\).

This proves the critical prime-power claim. Every stripping gcd contains
either the whole hidden component \(p_i^{e_i}\) or none of it. A partial
power can occur in the initial gcd, before restriction to the torsion
subgroup, but then it is already a proper divisor. No step assumes that
\(N\) is squarefree.

## 2. Deterministic order-stripping trichotomy

If

\[
\gcd(a^{N-1}-1,N)=1,
\]

then no local residue returns at exponent \(N-1\). A return at any divisor
\(k\mid N-1\) would imply a return at \(N-1\), so every divisor-exponent
gcd is also one. The complete-nonreturn branch is exact.

On the full-return branch, let \(o_i\) be the local orders and let \(R\)
be the maintained factored common multiple. For a prime \(q\mid R\),

\[
\gcd(a^{R/q}-1,N)
=\prod_{o_i\mid R/q}p_i^{e_i}.
\]

A global gcd deletes one copy of \(q\). A proper gcd factors \(N\). A
gcd of one means that every local order needs the current \(q\)-adic
valuation. Processing all prime copies without a proper gcd therefore
forces equal valuations at every prime and hence

\[
o_1=\cdots=o_s=R.
\]

The terminal tests \(a^R=1\pmod N\) and
\(\gcd(a^{R/q}-1,N)=1\) for every prime \(q\mid R\) are also a valid
public certificate of that exact common local order. Its factorization is
inherited from the known factorization of \(N-1\).

These cases exhaust all units. The asserted factor / complete nonreturn /
exact common-order trichotomy is valid for any number of distinct hidden
primes and arbitrary positive prime-power exponents.

## 3. Exact probability formulas

CRT makes the components of a uniform unit independent and uniform. The
fraction whose reduction modulo \(p_i\) is not an \((N-1)\)-root is

\[
\beta_i=1-\frac{d_i}{p_i-1}.
\]

The fraction that is a full root modulo \(p_i^{e_i}\) is

\[
\gamma_i=\frac{d_i}{h_i}.
\]

Thus the products in equations (13) and (14) are exact. Intermediate
prime-power lifts lie in the remaining proper-gcd event; they are not lost
from the partition.

Conditioned on full return, each component is uniform in a cyclic group of
order \(d_i\). Such a group has \(\varphi(r)\) elements of exact order
\(r\) when \(r\mid d_i\). Consequently, equal local order \(r\) has
conditional probability

\[
\frac{\varphi(r)^s}{\prod_i d_i},
\]

and is possible exactly for \(r\mid D=\gcd_i d_i\). Removing the
conditioning changes the denominator to \(\prod_i h_i\). This verifies
equations (15) and (16).

For an accumulated lcm state \(C\), a synchronized return makes no strict
progress exactly when \(r\mid C\). Hence the synchronized no-growth sum is
over \(r\mid\gcd(D,C)\). It is disjoint from complete nonreturn. Every
other case either exposes a proper gcd or strictly increases the lcm. The
event classification and equation (17) are exact.

## 4. Squarefree-semiprime specialization

For \(N=pq\), reduction of \(pq-1\) modulo \(p-1\) and modulo \(q-1\)
gives

\[
\gcd(pq-1,p-1)=\gcd(pq-1,q-1)=d=\gcd(p-1,q-1).
\]

At \(C=1\), no progress has exactly two disjoint forms:

1. neither local component is an \((N-1)\)-root;
2. both local components are the identity.

If exactly one component is a root, the initial gcd factors \(N\). If both
are roots with unequal orders, stripping factors \(N\). If both have the
same order greater than one, the lcm grows. Subtracting the two no-progress
probabilities gives

\[
\frac d{p-1}+\frac d{q-1}
-\frac{d^2+1}{(p-1)(q-1)},
\]

so equation (20) is correct. Partitioning synchronized tuples into equal
order \(r=1\), equal order \(r>1\), and unequal orders gives equations
(21) and (22).

## 5. Bounded-gap obstruction and sampling model

The divisibility

\[
d=\gcd(p-1,q-1)\mid q-p
\]

is exact. For \(q-p\le H\), every synchronized order and their accumulated
lcm divide the same fixed integer \(d\le H\). Repeated common returns
cannot cross the prime-certificate threshold.

A unit sample can factor or grow the state only if at least one local
component is an \((N-1)\)-root. The union bound gives

\[
\Pr(\text{factor or growth})
\le \frac d{p-1}+\frac d{q-1}=O_H(p^{-1})
\]

for every current state. This remains true after earlier samples change
\(C\).

Sampling uniformly from all residue classes does not evade the bound. The
probability of a nonunit modulo \(pq\) is at most \(p^{-1}+q^{-1}\), and
counting every such sample as a success only adds \(O(p^{-1})\) on a
bounded-gap pair. Conditional on being a unit, the residue is uniform in
the unit group.

For \(q=p+O_H(1)\), one has

\[
p=2^{n/2+O_H(1)}.
\]

Multiplication by any fixed numerical-QP sample bound
\(2^{(\log n)^{O(1)}}\) changes the exponent by only \(o(n)\). Thus the
probability of any factor or strict growth remains \(2^{-\Omega(n)}\).

The only external existence input is the proved bounded-prime-gap theorem,
which supplies one absolute \(H\) and infinitely many distinct prime pairs
with gap at most \(H\). It does not require a prescribed gap, the twin-prime
conjecture, or a density estimate. Therefore the infinite-family quantifier
is sound.

## 6. Prime terminal and contrasting inputs

Every returned common order divides \(N-1\), so it is coprime to each
hidden prime \(p_i\). As an order modulo \(p_i^{e_i}\), it therefore
divides \(p_i-1\). Their lcm \(C\) also divides every \(p_i-1\). If a
composite \(N\) had \(C>\sqrt N\), its least rational prime divisor would
satisfy both

\[
p_i\le\sqrt N
\quad\text{and}\quad
p_i>C,
\]

a contradiction. The stated Pocklington/Lucas terminal is valid, including
for repeated prime powers.

For prime \(N\), the probability calculation for collecting the full
\(q\)-primary part of \(N-1\) is correct: one uniform element misses that
part with probability \(1/q\), so \(k\) independent elements miss it with
probability \(q^{-k}\). The union bound in equation (27) follows.

For squarefree Carmichael \(N\), every unit fully returns. At initial state
one, only the unique CRT identity tuple avoids both a factor and growth.
Equation (28) follows.

For \(N=p^e\), \(e\ge2\), one has \(d_1=p-1\). Every unit returns modulo
\(p\), while a fraction \(p^{1-e}\) returns modulo \(p^e\). Every other
unit yields a proper partial-power gcd. Equation (29) is correct. The
general formulas likewise remain valid when several repeated prime-power
components occur.

## 7. Recursive-cost scope

For the stated bit-length convention,

\[
\operatorname{bitlen}((N-1)/2)\le n-1.
\]

The factorization of this one child gives the complete factorization of
\(N-1\). Each base needs fewer than \(n\) prime-copy stripping tests, and
all modular arithmetic has polynomial bit complexity. A numerical-QP bank
of bases therefore has numerical-QP nonrecursive cost.

If this stage makes no other recursive call, the recurrence

\[
T(n)\le T(n-1)+Q(n)
\]

sums to \(nQ(n)\) after replacing \(Q\), if necessary, by a nondecreasing
QP upper bound. No fixed-ratio contraction is needed for this single chain.

This accounting does not cover recursive completion of a factor split
returned later. Such completion adds both factor children to the recursion
tree, as equation (32) states. The frozen result correctly presents this as
an interface limitation and does not claim QP complete factorization.

## Hostile attacks that did not refute the claim

I checked:

- partial lifts inside repeated prime powers;
- different local orders with the same global lcm;
- multiple hidden CRT components;
- root subgroups of size one;
- stripping one prime with several copies;
- a current lcm state that already contains some returned orders;
- uniform residues rather than preconditioned units;
- accumulating arbitrarily many synchronized bounded-gap returns;
- prime powers at the Pocklington terminal;
- the distinction between one recursive preprocessing child and the
  additional children needed to complete a returned split.

None invalidates the stated theorem. The usual factoring domain convention
\(N>1\) is implicit; if the statement is later polished, writing
"positive odd \(N\ge3\)" would exclude the irrelevant \(N=1\) boundary
explicitly.
