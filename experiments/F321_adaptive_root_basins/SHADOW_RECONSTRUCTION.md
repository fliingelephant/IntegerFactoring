# Blind reconstruction: capped radical-shadow domination

## Input provenance and status

This reconstruction used only `SHADOW_STATEMENT_ONLY.md` and the applicable
repository instructions. The SHA-256 digest of the statement was

```text
b816f21218b5dab5c1fb6200eacba7864b36077b3de71a9ea568293958c46cc7
```

The squarefree success lower bound in Claim 2 is an assumption. Nothing below
proves that bound for the adaptive process.

## 1. The reduction invariant

Write

\[
N=\prod_{p\mid N}p^{e_p},\qquad R=\operatorname{rad}(N)=\prod_{p\mid N}p,
\]

and let \(\rho:\mathbb Z/N\mathbb Z\to\mathbb Z/R\mathbb Z\) be reduction
modulo \(R\). For integers \(z_N,z_R\) with \(z_R\equiv z_N\pmod R\), the
following facts are immediate from the common set of prime divisors:

1. \(\gcd(z_R,R)=1\) if and only if \(\gcd(z_N,N)=1\).
2. If \(1<\gcd(z_R,R)<R\), then \(1<\gcd(z_N,N)<N\).
3. If \(\gcd(z_R,R)=R\), then \(\gcd(z_N,N)\) is either a proper nontrivial
   divisor or all of \(N\).

For the second fact, some prime dividing \(N\) divides \(z_N\), while another
prime dividing \(N\) does not divide \(z_N\). The exponents \(e_p\) do not
enter this argument. Thus it covers arbitrary unequal repeated exponents.

Represent a state by its parameter list. If corresponding parameters satisfy
\(A_{N,i}\equiv A_{R,i}\pmod R\), then the two represented functions satisfy

\[
H_N(x)\equiv H_R(\rho(x))\pmod R.
\]

This holds initially because both functions are \(X\). It is preserved by an
update because reduction modulo \(R\) commutes with subtraction and
multiplication:

\[
H_N(H_N-A_N)\bmod R
=H_R(H_R-A_R)\bmod R.
\]

## 2. Coupling and the unguarded claim

Before an attempt, sample an infinite independent sequence \(X_{N,1},X_{N,2},
\ldots\), uniform in \(\mathbb Z/N\mathbb Z\), and set
\(X_{R,j}=\rho(X_{N,j})\). Each residue modulo \(R\) has exactly \(N/R\)
lifts modulo \(N\). Hence the \(X_{R,j}\) are independent and exactly uniform
modulo \(R\). The two attempts use the pair with index \(j\) for their
\(j\)-th evaluation.

Induct until the \(N\)-attempt succeeds. The parameter lists are compatible
at the start of a probe, so its outputs satisfy \(Y_N\equiv Y_R\pmod R\).
There are three cases at the \(R\)-attempt.

* A proper gcd at \(R\) is also a proper gcd at \(N\), by Fact 2. Both attempts
  have succeeded by this probe.
* A unit at \(R\) is a unit at \(N\), by Fact 1. They append compatible values
  \(A_R=Y_R\) and \(A_N=Y_N\), and the update preserves the invariant.
* A full-zero gcd at \(R\) gives either a proper gcd at \(N\), in which case
  the \(N\)-attempt succeeds earlier, or a full-zero gcd at \(N\), in which
  case neither list changes.

Treat success at \(N\) as an absorbing flag and continue the pre-sampled
shadow path only for the coupling argument. It follows pathwise that, for
every evaluation index \(j\), success at \(R\) by evaluation \(j\) implies
success at \(N\) by evaluation \(j\). In particular, for every fixed cap
\(B\),

\[
\Pr[\text{success modulo }N\text{ by }B]
\;\geq\;
\Pr[\text{success modulo }R\text{ by }B].
\]

The actual sampler modulo \(N\) only samples residues modulo \(N\), evaluates
its parameter list, and computes gcds. The sampler modulo \(R\) has the same
public operations for its own modulus. Reduction through \(R\) is only a
proof coupling; neither public sampler needs a factorization or computes
\(R\).

## 3. Fixed guard length

Fix \(K\geq 0\). Extend the coupled state during a guard by the pending values
\(A_N,A_R\) and the number of completed unit guard outcomes. They are
compatible because \(A_N\equiv A_R\pmod R\). For a guard evaluation, the
outputs

\[
Z_N=H_N(X_N)-A_N,
\qquad
Z_R=H_R(X_R)-A_R
\]

again satisfy \(Z_N\equiv Z_R\pmod R\). The same three gcd facts apply.
A proper gcd at \(R\) gives a proper gcd at \(N\). Unit outcomes occur
simultaneously and advance both guard counters. A full-zero outcome at \(R\)
either makes \(N\) succeed early or is full-zero at \(N\), in which case both
attempts reject the pending value and make no update. After \(K\) unit guard
outcomes, both append compatible pending values and preserve the polynomial
invariant. For \(K=0\), this last transition occurs immediately.

Main and guard evaluations use one shared evaluation index. Therefore they
consume the cap in lockstep until \(N\) succeeds. If the cap is exhausted
during a guard, both active attempts fail at that same point. Consequently
the same pathwise domination, and hence the same probability inequality,
holds for every fixed \(K\) with the stated total-cap convention.

## 4. Conditional all-input Las Vegas reduction

Assume the squarefree success contract in Claim 2. Factor a positive input
\(M\geq2\) as follows. (The input \(1\) has the empty factorization.)

1. Remove and record its full power of \(2\). If the remaining odd part is
   \(1\), stop.
2. On each remaining odd task \(m\), first run deterministic primality testing.
   If \(m\) is prime, emit it.
3. Run an exact perfect-power test. If \(m=a^k\) with \(a>1\) and \(k\geq2\),
   recursively factor \(a\), then multiply every returned multiplicity by
   \(k\). The root \(a\) is not assumed prime.
4. Otherwise, let \(n=\ell(m)\) be the binary length. Run independent
   unguarded attempts modulo \(m\), each with cap \(B(n)\), until one returns
   a verified \(d\) with \(1<d<m\) and \(d\mid m\). Recursively factor both
   \(d\) and \(m/d\).

The randomized branch is always within the scope of Claim 1. Indeed, an odd
composite with only one distinct prime divisor is \(p^e\) for \(e\geq2\), so
it would have been caught by the exact perfect-power test. Thus a composite
reaching step 4 has at least two distinct prime divisors.

Let \(R=\operatorname{rad}(m)\), and put \(r=\ell(R)\). This \(R\) is odd,
squarefree, and composite. Also \(r\leq n\). Monotonicity of \(B\), prefix
monotonicity of success in the cap, Claim 1, the squarefree hypothesis, and
monotonicity of \(Q\) give

\[
\begin{aligned}
\Pr[\text{one attempt succeeds modulo }m\text{ with cap }B(n)]
&\geq \Pr[\text{success modulo }R\text{ with cap }B(n)]\\
&\geq \Pr[\text{success modulo }R\text{ with cap }B(r)]\\
&\geq \frac1{Q(r)}
\geq \frac1{Q(n)}.
\end{aligned}
\]

This is the required length padding. It uses only \(r\leq n\); it needs no
promise that \(R\) and \(m\) have comparable lengths. The algorithm neither
knows \(r\) nor computes \(R\). It uses only the public value \(B(n)\).

Independent attempts therefore give a geometric waiting time with expectation
at most \(Q(n)\). Every reported divisor is checked by exact gcd, comparison,
and exact division before recursion. Randomness can change the running time,
but it cannot make the output incorrect.

## 5. Circuit and sampling cost

The polynomial must remain a straight-line circuit or, equivalently here, a
parameter list. For parameters \(A_1,\ldots,A_s\), evaluate it at a new \(x\)
by

\[
h\leftarrow x,\qquad h\leftarrow h(h-A_i)\pmod m
\quad(i=1,\ldots,s).
\]

This uses \(O(s)\) modular subtractions and multiplications. The circuit is
not expanded into its exponentially large formal polynomial. Since every
append consumes an evaluation, \(s\leq B(n)\) during a capped attempt. At
most \(B(n)\) evaluations therefore cost \(O(B(n)^2)\) modular operations,
plus \(B(n)\) gcd computations. With \(n\)-bit residues, one attempt has bit
cost

\[
C_{\rm att}(n)\leq n^{O(1)}B(n)^2.
\]

Exact uniform residues require no biased reduction. To sample modulo an
\(n\)-bit \(m\), draw \(n\) independent fair bits as an integer
\(U\in[0,2^n)\), accept when \(U<m\), and repeat otherwise. Since
\(m\geq2^{n-1}\), the acceptance probability is greater than \(1/2\).
Thus each exact uniform sample uses fewer than two candidate blocks in
expectation, hence \(O(n)\) expected bit operations and fair bits. Fresh bit
blocks give independent accepted residues. Sampling all probes contributes
only \(O(nB(n))\) expected work, already covered by the displayed bound.

## 6. Complete recursion and total complexity

Every random split \(m=uv\) has \(2\leq u,v\leq m/2\). Every perfect-power
step has \(m=a^k\), where \(k\geq2\), so \(a\leq\sqrt m\leq m/2\) for the
composite inputs on which this step occurs. Thus every child is at most half
its parent, and each recursion path has length at most \(\log_2 M\).

Let \(\Omega(M)\) denote the number of prime factors counted with
multiplicity. There are at most \(\Omega(M)\leq\log_2 M\) terminal prime
occurrences if multiplicities are expanded. Thus there are at most
\(O(n_0)\) binary split nodes for \(n_0=\ell(M)\). A crude bound of
\(O(n_0^2)\) covers all unary perfect-power nodes as well: there are at most
\(n_0\) leaves and every root-to-leaf path has length at most \(n_0\).

At every randomized node, its length is at most \(n_0\). By monotonicity, its
expected number of attempts is at most \(Q(n_0)\), and its per-attempt cost is
at most \(n_0^{O(1)}B(n_0)^2\). The deterministic primality, perfect-power,
gcd, and division work is polynomial per node. Therefore the whole expected
bit cost is bounded by

\[
n_0^{O(1)}Q(n_0)B(n_0)^2,
\]

where the polynomial factor absorbs the recursion-node bound. Products and
fixed powers of fixed quasipolynomials are quasipolynomial, so this is a fixed
quasipolynomial bound.

Each geometric loop terminates with probability one, and only finitely many
such loops occur on any terminating recursion tree. The algorithm therefore
terminates with probability one and always returns a verified complete prime
factorization. This proves Claim 2 only conditional on its stated squarefree
success contract.
