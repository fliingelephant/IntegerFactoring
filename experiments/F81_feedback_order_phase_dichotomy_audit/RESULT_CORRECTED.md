# Corrected F81 hostile re-audit — order and phase branches

## Verdict: PASS

I re-audited the complete corrected artifact
`experiments/F81_feedback_order_phase_dichotomy/RESULT.md` at SHA-256

```text
1aea866b07229545b14c7dbb34955e6d092adce65ccf8d47b93c2ecbf93dc94e
```

The hash matches the requested corrected candidate. The failed first audit
is retained at
`experiments/F81_feedback_order_phase_dichotomy_audit/RESULT.md` with
SHA-256

```text
059697ec65cb4203f85b5c89473a7d88e4f1e790ea25c997bbf4a307ef893b50
```

That failure remains attached to the earlier pinned candidate. This was a
fresh whole-proof, proof-only re-audit. I ran no research computation.

The terminology defect is repaired. Every bank-completeness claim now uses
the exact condition

\[
\sigma(r)\leq B,
\]

or says “prime-power-bounded.” The corrected artifact no longer replaces
this condition with standard \(B\)-smoothness. All other mathematical and
scope claims also survive fresh re-checking.

## 1. Pure-power separator gate

Let

\[
r=\operatorname{lcm}(r_p,r_q).
\]

Exponents in \(\langle u\rangle\) are residues modulo \(r\). The
\(p\)-identity kernel has \(r/r_p\) residues, and the \(q\)-identity kernel
has \(r/r_q\). Their intersection consists of the single residue divisible
by both local orders, namely \(0\bmod r\).

The positive separators are the symmetric difference of these kernels.
Their exact count and uniform density are therefore

\[
\frac r{r_p}+\frac r{r_q}-2,
\qquad
\frac1{r_p}+\frac1{r_q}-\frac2r.
\]

If \(r_p=r_q\), the kernels coincide. If \(r_p\neq r_q\), then either
\(r_q\nmid r_p\), in which case exponent \(r_p\) gives a one-sided identity,
or \(r_q\mid r_p\) properly, in which case exponent \(r_q\) does. Thus
\(\langle u\rangle\) contains a positive separator exactly when the local
orders differ.

For every specified exponent \(E\),

\[
u^E\equiv1\pmod p\iff r_p\mid E,
\qquad
u^E\equiv1\pmod q\iff r_q\mid E.
\]

Since \(N=pq\), a proper gcd of \(u^E-1\) occurs exactly when one
divisibility holds and the other does not. Equation (1) is exact. The
algorithm can execute a chosen exponent and gcd without knowing either
order.

## 2. Negative-sign synchronization

Suppose \(r_p=r_q=r_0\). If \(r_0\) is odd, neither generated local cyclic
subgroup contains an element of order two, so neither contains \(-1\).

If \(r_0\) is even, exponent \(r_0/2\) gives the unique order-two element in
each generated subgroup. In an odd-prime field that element is \(-1\).
Consequently

\[
u^E\equiv-1\pmod p
\iff E\equiv r_0/2\pmod{r_0}
\iff u^E\equiv-1\pmod q.
\]

Thus no pure power can make either direct sign asymmetric when the local
orders agree.

## 3. Exact prime-power threshold

For every prime \(\ell\),

\[
v_\ell(M_B)
=\max\{e:\ell^e\leq B\}
=\lfloor\log_\ell B\rfloor.
\]

Hence

\[
a\mid M_B
\iff
\ell^{v_\ell(a)}\leq B
\text{ for every }\ell\mid a
\iff
\sigma(a)\leq B.
\]

The correction now preserves this exact condition in the introduction,
algorithmic consequence, and final characterization. In standard terms it
is a prime-power bound, which is stronger than merely requiring all prime
factors to be at most \(B\).

The example \(5,10\) is also correct. Both have
\(\sigma=5\). Before \(B=5\), neither divides \(M_B\); at \(B=5\), both
divide it. A single unpunctured ladder therefore does not separate them.

## 4. Punctured-lcm bank: necessity

Every bank member

\[
M_B/\ell^j
\]

divides \(M_B\). If neither local order divides \(M_B\), neither can divide
any bank member. If the local orders are equal, no exponent can satisfy the
XOR gate.

Conversely, if a bank member succeeds, the order that divides it also
divides \(M_B\), so that order has \(\sigma\leq B\). The two orders must be
unequal. This proves the necessity of equation (4).

## 5. Punctured-lcm bank: sufficiency

Assume the orders are unequal and at least one has \(\sigma\leq B\). If
exactly one order divides \(M_B\), then \(M_B\) itself separates them.

Otherwise both divide \(M_B\). Choose a prime with unequal valuations and
orient the names so that

\[
a=v_\ell(r_p)<v_\ell(r_q)=b.
\]

Let

\[
e=v_\ell(M_B)=\lfloor\log_\ell B\rfloor.
\]

Because both orders divide \(M_B\), \(b\leq e\). Then
\(j=e-a\) satisfies \(1\leq j\leq e\), so

\[
E=M_B/\ell^{e-a}
\]

is in the bank. Its \(\ell\)-valuation is \(a\), and all other valuations
remain those of \(M_B\). Therefore \(r_p\mid E\) and \(r_q\nmid E\).
The opposite orientation is symmetric. The iff in Theorem 2 is complete,
including the order-one convention and \(B=1\).

## 6. Bank size and deterministic cost

The pairs \((\ell,j)\) are in one-to-one correspondence with prime powers
\(\ell^j\leq B\). There are at most \(B\) such pairs, so the bank has at
most \(B+1\) members.

The bound

\[
M_B\leq B!
\]

gives \(\log_2M_B=O(B\log B)\). When
\(B=\operatorname{poly}(\log N)\), elementary prime enumeration, repeated
lcm construction, exact divisions, all modular powers, and all gcds use
polynomial bit complexity. This construction needs no factor of \(N\), no
local order, and no factor-dependent advice.

## 7. Fresh check of the \(N=4033\) orders

Modulo \(37\),

\[
5\equiv2^{23},
\qquad
\operatorname{ord}_{37}(2)=36.
\]

Since \(\gcd(23,36)=1\),

\[
\operatorname{ord}_{37}(5)=36.
\]

Modulo \(109\), direct reductions give

\[
5^4\equiv80,\qquad
5^8\equiv78,\qquad
5^9\equiv63.
\]

Also,

\[
63^2\equiv45,\qquad
63^3\equiv1\pmod{109}.
\]

Thus \(5^{27}=1\), while \(5^9\neq1\). The order divides \(27\) but not
\(9\), so it is exactly \(27\).

The prime-power thresholds are

\[
\sigma(36)=9,\qquad
\sigma(27)=27.
\]

Finally, \(M_9=2520=36\cdot70\) is divisible by \(36\) but not by \(27\).
The unpunctured bank member therefore gives the stated one-sided identity.

## 8. Maximal phase-only expansion

In additive \(\mathbb F_L^2\), every nonzero element has order \(L\).
For distinct nonzero \(a,b\), the element

\[
z=(a,b)
\]

has equal local orders \(L,L\). For every scalar \(A\), either \(A=0\) and
both coordinates of \(Az\) vanish, or \(A\neq0\) and neither vanishes. No
pure power of \(z\) is a positive separator, even under an unbounded
adaptive exponent schedule.

The columns \(g=(1,1)\) and \(z\) have determinant

\[
b-a\neq0.
\]

They span all of \(\mathbb F_L^2\), while the mixed word

\[
z-ag=(0,b-a)
\]

is a positive separator. This is an exact maximal expansion whose useful
information lies in relative phase, not in unequal orders of the new
generator.

In an odd-order realization, local \(-1\) has order two and is absent from
both order-\(L\) projection subgroups. The negative sign gives no hidden
pure-power escape. The example remains abstract; it does not produce a
canonical integer split or reveal \(a\) publicly.

## 9. Algorithmic dichotomy and scope

Equality versus inequality of the two local orders is an exact structural
dichotomy for pure powers of \(u\):

- unequal orders mean that some pure power is a positive separator;
- equal orders mean that neither direct sign can succeed on a pure power.

The bank is a public polynomial decoder only for the unequal-order subcase
with

\[
\min\{\sigma(r_p),\sigma(r_q)\}\leq B.
\]

The bank can be executed without knowing this predicate. Failure does not
identify the phase branch: it can also mean unequal orders with both
\(\sigma\)-values above \(B\). The candidate's sentence that the first
condition is “executable but hidden” is therefore read precisely as: the
bank is executable, while its success predicate is hidden. The surrounding
sentences make this scope explicit and do not claim a public branch
classifier.

Equal orders do not guarantee a useful phase mismatch; Section 4 supplies
an existence example. A pure power of a separately constructed mixed
element is already a mixed-word operation relative to \(u\) and the old
subgroup. Integer refinement, quotient searches, and square-class decoding
remain outside the pure-power classification.

The corrected result is a Pollard-style prime-power-bounded decoder and an
abstract mechanism classification. It supplies no source of suitable local
orders, no public phase selector, no canonical integer phase family, no
inverse-polynomial feedback law, and no all-input factoring algorithm. The
historical references to P78, P79, P80, and P84 are not needed for
these proofs and were not independently re-audited.
