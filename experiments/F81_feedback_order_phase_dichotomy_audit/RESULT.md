# F81 hostile audit — order and phase branches

## Verdict: FAIL as written; the mathematical core survives

I audited
`experiments/F81_feedback_order_phase_dichotomy/RESULT.md` at SHA-256

```text
4fa0278a3299fe49fc2e60062c562c2ed7c327a0e03cdeb7b44208cfbf64701e
```

The hash matches the requested artifact. This was a proof-only audit. I ran
no research computation.

The two boxed theorems are correct. The pure-power classification, exact
count and density, negative-sign synchronization, punctured-lcm-bank
criterion, cost bound, \(N=4033\) orders, and maximal phase example all
survive.

One later summary claim is false under standard terminology. Section 5 says
that the bank is complete when at least one local order is
“\(B\)-smooth.” Standard \(B\)-smoothness means that every prime factor is
at most \(B\). The proved bank needs the stronger condition

\[
\sigma(r)\leq B,
\]

meaning that every full prime-power divisor is at most \(B\). These
conditions are not equivalent.

The exact repair is to replace “\(B\)-smooth” and the opening phrase
“polynomial-smooth” with “\(B\)-powersmooth,” or simply repeat
\(\sigma(r)\leq B\). No proof change is needed. Because the pinned artifact
makes a mathematically false algorithmic summary under standard
terminology, it does not receive PASS in its present form.

## 1. Exact counterexample to the wording defect

Take \(B=2\) and unequal local orders \(8\) and \(16\). Both integers are
\(2\)-smooth in the standard sense: their only prime factor is \(2\).
However,

\[
M_2=2,\qquad
\mathcal E_2=\{2,1\}.
\]

Neither \(8\) nor \(16\) divides either bank exponent, so no XOR separation
occurs. These local orders are realizable: finite-field unit groups are
cyclic, so one can choose an element of order \(8\) modulo \(17\), an element
of order \(16\) modulo \(97\), and combine them by CRT.

The boxed theorem predicts this failure correctly:

\[
\sigma(8)=8,\qquad \sigma(16)=16,
\]

so \(\min\{\sigma(8),\sigma(16)\}>2\). The defect is confined to the prose
replacement of the exact condition by standard “smoothness.”

## 2. Pure-power existence, count, and density

Let \(r=\operatorname{lcm}(r_p,r_q)\). Exponents in
\(\langle u\rangle\) are residues modulo \(r\). The set giving identity
modulo \(p\) is

\[
\{E\bmod r:r_p\mid E\},
\]

of size \(r/r_p\). The analogous \(q\)-kernel has size \(r/r_q\). Their
intersection is the single residue divisible by
\(\operatorname{lcm}(r_p,r_q)=r\), namely \(E=0\bmod r\).

Positive separators form the symmetric difference of these kernels.
Therefore their exact count and density are

\[
\frac r{r_p}+\frac r{r_q}-2,
\qquad
\frac1{r_p}+\frac1{r_q}-\frac2r.
\]

If \(r_p=r_q\), the two kernels coincide and the count is zero. If the orders
differ, take \(E=r_p\) when \(r_q\nmid r_p\); otherwise \(r_q\) is a proper
divisor of \(r_p\), and \(E=r_q\) works. Thus a positive separator exists
exactly when \(r_p\neq r_q\).

For any specified public \(E\), field-group order gives

\[
u^E\equiv1\pmod p\iff r_p\mid E,
\]

and likewise at \(q\). Since \(N=pq\), a proper gcd of \(u^E-1\) occurs
exactly when one divisibility holds and the other does not. The displayed
XOR gate is correct and uses no hidden-order computation in its execution.

## 3. Negative-sign synchronization

Assume \(r_p=r_q=r_0\). If \(r_0\) is odd, neither local cyclic subgroup
contains an element of order two, so neither contains \(-1\).

If \(r_0\) is even, the unique element of order two in each generated cyclic
subgroup is obtained at exponent \(r_0/2\). In an odd-prime field, the
unique element of order two is \(-1\). Hence

\[
u^E\equiv-1\pmod p
\iff E\equiv r_0/2\pmod{r_0}
\iff u^E\equiv-1\pmod q.
\]

Thus both direct signs are synchronized for every pure power when the local
orders agree. This claim is exact for the stated distinct odd primes.

## 4. The \(\sigma\) criterion

For a prime \(\ell\),

\[
v_\ell(M_B)=\max\{e:\ell^e\leq B\}
=\lfloor\log_\ell B\rfloor.
\]

Therefore

\[
a\mid M_B
\iff
\ell^{v_\ell(a)}\leq B
\quad\text{for every }\ell\mid a
\iff
\sigma(a)\leq B.
\]

This proves equation (2). It also shows precisely why ordinary
\(B\)-smoothness is insufficient: it bounds \(\ell\), not
\(\ell^{v_\ell(a)}\).

## 5. Exact punctured-bank iff

Every \(E\in\mathcal E_B\) divides \(M_B\). If a bank member is divisible by
one local order, that order also divides \(M_B\), so its \(\sigma\)-value is
at most \(B\). Equal local orders can never satisfy XOR. This proves
necessity of

\[
r_p\neq r_q,\qquad
\min\{\sigma(r_p),\sigma(r_q)\}\leq B.
\]

For sufficiency, if exactly one order divides \(M_B\), the unpunctured
member \(M_B\) separates them. Otherwise both divide \(M_B\) and are
unequal. Choose a prime \(\ell\) with

\[
a=v_\ell(r_p)<v_\ell(r_q)=b.
\]

Let

\[
e=v_\ell(M_B)=\lfloor\log_\ell B\rfloor.
\]

Both orders divide \(M_B\), so \(b\leq e\). The integer
\(j=e-a\) satisfies \(1\leq j\leq e\), and the bank contains

\[
E=M_B/\ell^j.
\]

This exponent has \(\ell\)-valuation \(a\), with every other prime
valuation unchanged. Hence \(r_p\mid E\) and \(r_q\nmid E\). The opposite
valuation ordering is symmetric. The boxed iff is correct, including order
\(1\) and \(B=1\) through the stated convention \(\sigma(1)=1\).

## 6. Bank size and bit complexity

The pairs \((\ell,j)\) index prime powers \(\ell^j\leq B\). There are at
most \(B\) such pairs, so the bank has at most \(B+1\) members.

Also,

\[
M_B\leq B!,
\qquad
\log_2M_B=O(B\log B).
\]

For \(B=\operatorname{poly}(\log N)\), elementary prime enumeration,
repeated lcm computation, exact division by \(\ell^j\), all modular
exponentiations, and all gcds require polynomially many bit operations. No
factor of \(N\), local order, or factor-dependent advice is used to build or
run the bank.

Failure of the bank does not identify the phase branch. It can mean either
equal local orders or unequal orders for which both \(\sigma\)-values exceed
\(B\). The candidate calls the conditions hidden and does not claim an
executable branch classifier.

## 7. The \(N=4033\), \(u=5\) orders

Modulo \(37\), the previous identities give

\[
5\equiv2^{23},
\qquad
\operatorname{ord}_{37}(2)=36.
\]

Since \(\gcd(23,36)=1\),

\[
\operatorname{ord}_{37}(5)
=\frac{36}{\gcd(36,23)}
=36.
\]

Modulo \(109\),

\[
5^4\equiv80,\qquad
5^8\equiv78,\qquad
5^9\equiv78\cdot5\equiv63.
\]

Also,

\[
63^2\equiv45,\qquad
63^3\equiv1\pmod{109}.
\]

Thus \(5^{27}=1\), while \(5^9=63\neq1\). The order divides \(27\) but
does not divide \(9\), so it is exactly \(27\).

Finally,

\[
\sigma(36)=\max\{4,9\}=9,
\qquad
\sigma(27)=27.
\]

The exponent \(M_9=2520\) is divisible by \(36\) and not by \(27\), so the
fixed separation statement is correct.

## 8. Maximal phase-only expansion

In additive \(\mathbb F_L^2\), every nonzero coordinate has exact order
\(L\). For distinct nonzero \(a,b\), the new element

\[
z=(a,b)
\]

therefore has equal local orders \(L,L\). For any scalar \(A\), if \(A=0\)
then both coordinates of \(Az\) vanish; if \(A\neq0\), neither does. No pure
power of \(z\) is a positive separator, even if the exponent is selected
adaptively.

The columns \(g=(1,1)\) and \(z\) have determinant \(b-a\neq0\), so they
span all of \(\mathbb F_L^2\). The mixed word

\[
z-ag=(0,b-a)
\]

is a positive separator. Thus maximal subgroup expansion can carry useful
information entirely in the relative alignment with the old diagonal,
while the new generator's local orders remain equal.

If this odd-order model is embedded into local unit subgroups of order
\(L\), local \(-1\) has order two and lies outside both projections.
Therefore the negative sign supplies no pure-power escape in that modeled
subgroup.

This is an abstract existence example. It does not construct a
canonical-inverse integer split, reveal the hidden coefficient \(a\), or
prove a computational lower bound.

## 9. Dichotomy and scope

Equality versus inequality of \(r_p,r_q\) is an exact structural dichotomy
for pure powers of the newly exposed block:

- unequal orders imply that some pure power is a positive separator;
- equal orders imply that no pure power reaches either direct sign
  asymmetrically.

The punctured bank is a complete public decoder only for the unequal-order
subcase with \(\min\sigma\leq B\). A failed bank does not tell an algorithm
which structural branch it is in. A useful equal-order expansion is also not
guaranteed; the phase example proves only that it can occur.

A pure power of a newly constructed mixed element is already a mixed-word
operation relative to \(u\) and the old subgroup. The theorem does not rule
out integer refinement, quotient searches, square-class decoding, or other
ways to construct such an element.

After correcting the smoothness terminology, the candidate remains a
Pollard-style decoder theorem and an abstract mechanism classification. It
does not provide a smoothness source, a public phase selector, an all-input
feedback law, a canonical integer phase family, or a polynomial-time
factoring algorithm. The historical references to P78, P79, P80, P81, and
P84 are not needed for these proofs and were not re-audited.
