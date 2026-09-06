# Blind reconstruction of F170

## Boundary and verdict

I verified the statement before reading it:

```text
SHA-256  268d55df4968a25eae7d50207c4cde54112706cd8a8e2860b699cc3c5d18ec99
file     STATEMENT.md
```

I did not read any other F170 artifact.

**Verdict: verified as a conditional theorem.** The local group facts, CRT
search bounds, quotient-closure trichotomy, exact order-growth construction,
and monotone least-common-multiple argument all follow from the stated
premises. The theorem does not supply the missing source of strict events, so
it is neither an unconditional factoring algorithm nor an all-input source
theorem.

## 1. Local tori

Let (r) be either hidden prime. Reduction modulo (r) gives

\[
 A_D(\mathbf F_r)=\mathbf F_r[w]/(w^2-D).
\]

If (D) is a square modulo (r), choose (s^2=D). The map

\[
 a+bw\longmapsto (a+bs,a-bs)
\]

identifies the algebra with (mathbf F_r\times\mathbf F_r), and the norm is
the product of the two coordinates. Its norm-one subgroup is

\[
 \{(u,u^{-1}):u\in\mathbf F_r^\times\}\cong\mathbf F_r^\times.
\]

It is cyclic of order (r-1).

If (D) is a nonsquare modulo (r), the algebra is
(mathbf F_{r^2}). Its multiplicative group is cyclic of order
(r^2-1). The norm map is (z\mapsto z^{r+1}), is onto
(mathbf F_r^\times), and has cyclic kernel of order (r+1).

Since (D) is a unit and has Jacobi symbol (-1), its two Legendre symbols
are opposite. If

\[
 \epsilon=\left(\frac Dp\right),
\]

then

\[
 |T_D(\mathbf F_p)|=p-\epsilon,
 \qquad
 |T_D(\mathbf F_q)|=q+\epsilon.
\]

The Chinese remainder theorem also identifies the public torus over
(mathbf Z/N\mathbf Z) with the product of these two hidden local tori.
Equality of torus points locally is equality of both coefficients.

The element (-1) has order two in every ordinary unit group and in every
local norm-one torus because the primes are odd. Thus both channels can start
with exact order two.

## 2. Divisibility, orthogonality, and CRT classes

If (g) has exact order (A) modulo both primes, then

\[
 A\mid p-1,qquad A\mid q-1.
\]

Consequently

\[
 p\equiv q\equiv1\pmod A,
 \qquad A\mid N-1.
\]

If (G) has exact torus order (B) at both primes, local cyclicity gives

\[
 B\mid p-\epsilon,qquad B\mid q+\epsilon.
\]

Hence

\[
 p\equiv\epsilon\pmod B,qquad
 q\equiv-\epsilon\pmod B,qquad
 N\equiv-1\pmod B,
\]

so (B\mid N+1). It follows at once that

\[
 \gcd(A,B)\mid\gcd(N-1,N+1)\mid2.
\]

Put (h=gcd(A,B)) and (L=\operatorname{lcm}(A,B)=AB/h). A generalized
CRT system

\[
 x\equiv\alpha\pmod A,qquad x\equiv\beta\pmod B
\]

is consistent exactly when (h\mid\beta-\alpha), and then it gives one
class modulo (L). One public representative is

\[
 x=\alpha+A\left(
 \frac{\beta-\alpha}{h}
 (A/h)^{-1}\bmod (B/h)
 \right)\pmod L.
\]

For ((\alpha,\beta)=(1,e)), both (e=1) and (e=-1) are consistent
because (h\mid2). The smaller prime occurs in the class with
(e=\epsilon). Adding and subtracting the two hidden prime congruences also
gives

\[
 p+q\equiv2\pmod A,qquad p+q\equiv0\pmod B,
\]

and

\[
 q-p\equiv0\pmod A,qquad q-p\equiv-2\epsilon\pmod B.
\]

All these systems are consistent for the same reason. The sum class is
orientation-free. The gap has the two public sign classes.

## 3. Candidate counts and factor thresholds

For a fixed residue (ho\pmod L), the number of integers in a real
half-open interval ([a,b)) is

\[
 \max\left\{0,
 \left\lceil\frac{b-\rho}{L}\right\rceil-
 \left\lceil\frac{a-\rho}{L}\right\rceil
 \right\},
\]

and is at most ((b-a)/L+1). Thus each of the two prime classes contains at
most

\[
 \frac{\sqrt N}{L}+1
\]

integers in (3\le x<\sqrt N). Since (p<q), one has
(p<\sqrt N), and (p) is in one of these classes. Testing
(gcd(x,N)) over at most

\[
 2\left(\frac{\sqrt N}{L}+1\right)
\]

candidates therefore finds a factor. If

\[
 L\ge\frac{\sqrt N}{Q(n)},
\]

the count is at most (2(Q(n)+1)), which is quasipolynomial.

Now assume (q<2p), and write (x=q/p\in(1,2)). Then

\[
 \frac{p+q}{\sqrt{pq}}=\frac{1+x}{\sqrt x}
 =\sqrt x+\frac1{\sqrt x}.
\]

This function is strictly increasing for (x>1). Therefore

\[
 2\sqrt N<p+q<\frac3{\sqrt2}\sqrt N.
\]

The interval width is

\[
 c_0\sqrt N,qquad c_0=\frac3{\sqrt2}-2.
\]

Also (c_0<1/8): both sides of (3/\sqrt2<17/8) are positive, and
(9/2<289/64). The single sum class therefore has at most

\[
 \frac{c_0\sqrt N}{L}+1
\]

candidates. The true sum is among them.

For each candidate (S), set (Delta=S^2-4N). If (Delta=d^2\ge0),
then (d) and (S) have the same parity because their squares agree
modulo four. Hence

\[
 (S-d)/2,qquad(S+d)/2
\]

are integers whose product is (N). They can be checked directly. The
condition

\[
 L\ge\frac{c_0\sqrt N}{Q(n)}
\]

gives at most (Q(n)+1) trials. Since (c_0<1/8), the simpler condition

\[
 L\ge\frac{\sqrt N}{8Q(n)}
\]

is sufficient as well. The irrational interval endpoints do not present an
algorithmic issue: integer candidates can be filtered using
(S^2>4N) and (2S^2<9N).

## 4. Why the two-coordinate quotient closure works

Fix (r\in\{p,q\}). Let

\[
 H_r=\langle G_r\rangle,qquad
 K_r=\langle H_r,(U_1)_r,\ldots,(U_t)_r\rangle.
\]

The local torus is cyclic, so (K_r) is cyclic. The subgroup (H_r) has
order (B). Define

\[
 \phi_r:K_r/H_r\longrightarrow K_r,qquad xH_r\longmapsto x^B.
\]

This is well-defined because every element of (H_r) has (B)-th power
one. It is injective: in a cyclic group containing a subgroup of order
(B), the elements killed by the (B)-th power map form exactly that
unique subgroup of order (B). Its image is

\[
 F_r=\langle (U_1)_r^B,\ldots,(U_t)_r^B\rangle.
\]

Thus

\[
 K_r/H_r\cong F_r,qquad |K_r|=B|F_r|.
\]

For two public fingerprints (Y=y_0+y_1w) and (Z=z_0+z_1w), let

\[
 d=\gcd(N,y_0-z_0,y_1-z_1).
\]

The prime (r) divides (d) exactly when (Y_r=Z_r). For globally
distinct fingerprints, (d) is therefore:

- a proper factor if equality holds at exactly one hidden prime; or
- one if the fingerprints differ at both hidden primes.

If the breadth-first table closes without a proper gcd, every equality
relation among generated words is the same globally and in both local
projections. Each projection from the completed global group (F) to
(F_r) is then both injective and surjective. Hence

\[
 F\cong F_p\cong F_q,qquad |F|=|F_p|=|F_q|=\kappa,
\]

and therefore (K_r/H_rcong F) for both primes. Since (F) injects into
a cyclic group, it is cyclic.

If instead the table stores (C+1) distinct fingerprints without a proper
gcd, those fingerprints remain distinct in each local projection. Thus

\[
 |F_p|,|F_q|\ge C+1,qquad
 |K_p|,|K_q|\ge B(C+1).
\]

This proves only a capacity lower bound. It does not identify a common
divisor of the two quotient orders.

### Exact closure gives an exact common order

On the closed branch, select a generator (Y\) of the cyclic group (F).
The completed table permits its order to be checked as (kappa), and word
provenance gives a torus word (V) with

\[
 Y=V^B.
\]

Then (V_rH_r) generates (K_r/H_r) at both primes. Put

\[
 M=B\kappa.
\]

There is a direct prime-primary construction of one public word having
exact order (M) at both primes. For each prime (ell\mid M), let
(m=v_\ell(M)).

- If (ell\mid\kappa), use
  
  \[
  E_\ell=V^{M/\ell^m}.
  \]

- If (ell\nmid\kappa), so (ell\mid B) and
  (m=v_\ell(B)), use
  
  \[
  E_\ell=G^{B/\ell^m}.
  \]

To verify the first case, write a local generator of (K_r) as (a_r),
so (|a_r|=M) and (H_r=\langle a_r^\kappa\rangle). If
(V_r=a_r^{v_r}), the fact that (V_rH_r) generates the quotient says
(gcd(v_r,\kappa)=1). Thus (ell\nmid v_r) whenever
(ell\mid\kappa), and (E_\ell) has exact order (ell^m) locally. In
the second case, exact order (B) of (G_r) makes (E_\ell) have exact
order (ell^m).

The factors (E_\ell) have pairwise coprime orders. Therefore

\[
 G'=\prod_{\ell\mid M}E_\ell
\]

has exact order

\[
 \prod_{\ell\mid M}\ell^{v_\ell(M)}=M=B\kappa
\]

at both hidden primes. This construction uses no alignment of the two local
discrete logarithms. Public factor-first order screens either expose a
one-prime equality, hence a factor, or certify the new exact common order.
The factorization of (kappa\le C) can be obtained within a
quasipolynomial cap, for example by trial division, so the new state can
retain a complete factorization.

When (kappa=1), the closure only proves that every source word is locally
in (H_r) at both primes. It supplies no growth and does not align the two
hidden logarithms.

## 5. Monotone least-common-multiple potential

After initialization, both exact orders are even. Every valid updated exact
order remains a multiple of its previous order, so both stay even. Since
their gcd always divides two,

\[
 \gcd(A,B)=2,qquad L=\frac{AB}{2}
\]

on every no-factor branch.

If one channel grows by an integer factor (kappa>1), validity of the new
state again makes the new gcd equal to two. Thus, for either
(A'=A\kappa) or (B'=B\kappa),

\[
 L'=\kappa L.
\]

The order-two initialization matters. Starting one channel at order one
would allow its first strict order growth to duplicate a factor two already
present in the other channel without increasing the least common multiple.

Initially (L=2). After (k) strict events,

\[
 L=2\prod_{i=1}^k\kappa_i\ge2^{k+1}.
\]

Consequently (O(n)) strict factor-or-growth events force the arbitrary or
balanced CRT threshold. If the cap, arithmetic, provenance words, source
rounds, and retained transcript all have quasipolynomial bit complexity,
then (O(n)) such rounds and the final candidate search still have
quasipolynomial total cost.

## 6. Capacity example

The stated example is self-contained. Take

\[
 N=143=11\cdot13,qquad D=5,qquad t=40.
\]

Modulo (11), (5=4^2). Modulo (13), the nonzero squares are
(1,3,4,9,10,12), so (5) is a nonsquare. Hence the Jacobi symbol is
(-1).

The Cayley denominator has norm

\[
 1-Dt^2\equiv1-5\cdot27\equiv9\pmod{143},
\]

whose inverse is (16). Therefore

\[
 \frac{1+tw}{1-tw}
 =\frac{(1+tw)^2}{1-Dt^2}
 =31+136w\pmod{143}.
\]

Modulo (11), this point is (9+4w). Under the split map with (w=4),
its two components are (3) and (4=3^{-1}), so it has order five.

Modulo (13), it is (U=5+6w), with (w^2=5). Direct multiplication
gives

\[
 U^2=10+8w,qquad U^4=4+4w,qquad U^6=5+7w,qquad U^7=1.
\]

Since seven is prime and (U\ne1), its local order is seven. Thus
(1,U,U^2,U^3) are distinct at both primes. With (B=1) and (C=3),
every pair comparison has gcd one and the fourth stored fingerprint triggers
the capacity branch. Yet the two local generated groups have orders five
and seven, so no nontrivial integer is an exact order in both.

The general obstruction is the same. If (m>C) divides both local torus
orders, local cyclicity supplies order-(m) points, and coefficient-wise CRT
combines them into one public point. Its first (C+1) powers have identical
equality patterns at both primes and trigger capacity without a factor. For
odd (m), neither local point is (-1). On a norm-one conic this makes
(a+1) a unit, and the inverse Cayley parameter (t=b/(a+1)) is clean.

## 7. Exact scope

The quotient closure is a synchronization test and, on complete closure, an
exact common-order updater. The new arithmetic leverage comes only from
keeping the ordinary and torus orders separate: one divides (N-1), the
other divides (N+1), and their gcd is at most two.

Nothing here proves that a public source produces a strict closure in the
next round, or ever. A round can factor, close with (kappa=1), or stop on
capacity. The last two outcomes need not increase (L). Capacity cannot be
inserted into the CRT congruences because it gives no exact common modulus.
Therefore the reconstructed result is a correct conditional termination
theorem, not an unconditional semiprime-factoring theorem.
