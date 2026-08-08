# F98 — retained canonical presentations create a genuinely amortized factor

**Status:** candidate. The public replay and small-support diagnosis are exact
and factorization-free. No hostile audit or proof-blind reconstruction has
run. This is one finite mechanism witness, not an all-input factoring law.

## 1. Exact input certificate

The selected input is

\[
N=202{,}537{,}109=10{,}267\cdot19{,}727.
\]

Both displayed factors are prime. Also

\[
g=\gcd(10{,}266,19{,}726)=2,
\quad A=5133,
\quad B=9863,
\]

and

\[
\gcd(AB,N-1)=1.
\]

Thus this is a P98-stable distinct odd semiprime. Its bit length is
\(n=28\), so the declared trial bound is \(B=n^2=784\). The least factor
is \(10{,}267>B\). The input is not removed by that polynomial trial screen.

The factorization was used to select and certify the finite input. The public
replay receives only \(N\).

## 2. Public target-free round

The exact C2T rule is in `DESIGN.md`. On this input, it starts with the 27
canonical-inverse seeds \(2,\ldots,28\). Exact gcd and perfect-power
refinement selects 27 nonzero seed presentations and their public block
pairs. For every pair \((u,v)\), it tests both trajectories

\[
[u^e v]_N,
\qquad
[u v^e]_N,
\qquad 0\le e\le784.
\]

The order, all active pairs, and every retained presentation are determined
from \(N\). No factor, target residue, target exponent, relation value, or
target square class is supplied.

The complete direct screen adds 12,522 first-occurrence relations. Every
test

\[
\gcd(c-w,N),\qquad \gcd(c+w,N),
\quad w=c^{-1}_{\rm can},
\]

is trivial. Thus this input is a direct-screen null. It cannot be explained
by one selected residue hitting a CRT sign.

Together with the 27 seeds, the state retains 12,549 presentations. The
decoder removes one relation value \(P=1\) and 3,134 repeated relation values
only inside its mod-two matrix. It keeps all presentations and provenance in
the source state. This leaves 9,414 distinct relation values.

## 3. Factorization-free amortized decoder

The public executable copies the audited P66 parity-refinement and binary
kernel logic into a self-contained source file. It uses only integer gcd,
exact square tests, exact division, modular arithmetic, and binary linear
algebra. It does not call factorization, primality testing, order finding, a
discrete logarithm, or a target selector.

On the 9,414 distinct relation columns, factor-free refinement gives:

- 11,015 nonsquare parity rows;
- square-class rank 8,926; and
- kernel dimension 488.

The first useful kernel-basis root selected by this public decoder uses 166
columns. All 166 relation values are distinct. Its residue is

\[
R\equiv132{,}013{,}085\pmod N,
\]

and

\[
\gcd(R-1,N)=19{,}727,
\qquad
\gcd(R+1,N)=10{,}267.
\]

The exact replay finished in 53.23 seconds under a 120-second hard timeout.
Runtime is evidence of reproducibility only. It is not asymptotic evidence.

This is a real algorithmic difference from one-scalar feedback. No direct
trajectory hit works. The factor appears only after many nonclosing
canonical presentations are retained, jointly refined, and decoded.

## 4. Small-support boundary

A second factorization-free executable inspects the first 5,616 relations in
the same public order.

- Support one has one trivial \(P=1\) cycle and no useful root.
- Support two has 1,847 parity matches. Every match repeats the same relation
  value, so its connecting root is \(P\equiv1\pmod N\). None is useful.
- For support three, 1,530 matching cases remain after taking the first valid
  right endpoint for each left pair. None is useful.

The support-three compression is exact here. Any two possible right
endpoints for the same left pair are in the same square class. Their
support-two connecting relation has an identical value and root
\(P\equiv+1\pmod N\). Replacing one by the other does not change the triple
root residue.

At relation ordinal 5,616, online Gaussian elimination gives a useful
166-column circuit. All 166 values are distinct, so duplicate-value
cancellation removes zero columns. Its root residue is

\[
70{,}524{,}024,
\]

with gcds 10,267 and 19,727.

This proves that no useful circuit of support at most three occurs in that
pinned prefix. It does **not** prove that 166 is the minimum useful support.
A useful circuit of support 4 through 165 may exist.

## 5. Exact scope

F98 proves one finite positive mechanism:

\[
\boxed{
\text{retained canonical presentations can expose a factor even when every
individual direct sign test fails.}
}
\]

It also shows that the gain can require a genuinely amortized relation
circuit rather than a pair or triple collision.

F98 does not prove:

- success on every input;
- inverse-polynomial success density;
- a useful circuit of polynomial support on every input;
- that later feedback rounds always make progress;
- that support 166 is minimal; or
- a polynomial-time factoring algorithm.

The earlier failed and timed-out discovery runs remain in this directory.
They are not used as proof.
