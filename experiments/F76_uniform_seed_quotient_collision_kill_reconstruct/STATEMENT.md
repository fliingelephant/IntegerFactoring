# Proof-blind reconstruction statement: uniform-seed quotient collisions

Work only from this statement. Do not read any F76 candidate, audit, durable
ledger, or proof. Do not run computation. Reconstruct every claim below from
first principles. Return a self-contained PASS proof or the first exact
failure.

## Setup

Let

\[
n=\lceil\log_2(N+1)\rceil,
\qquad N\ge3.
\]

Run deterministic primality testing and stop if \(N\) is prime. On the
remaining composite input, fix \(B\ge\max(3,n)\), trial-divide \(N\) by all
primes at most \(B\), and stop if a proper factor appears. Thus every prime
divisor of the continuation input exceeds \(B\).

For \(1\le i\le m\), let \(U_i\) be a unit modulo \(N\), uniform in its
canonical representative range \(1,\ldots,N-1\). Put

\[
V_i=\iota_N(U_i),
\qquad
A_i=U_iV_i=1+K_iN.
\]

The samples may be independent, but assume only that each \(U_i\) has the
uniform marginal law. For \(1\le r\le R\), define

\[
C_r=1+rN,
\qquad
P=\prod_{i=1}^mA_i,
\qquad
D_r=\gcd(P,C_r),
\]

and

\[
L=n+\lceil\log_2(R+1)\rceil+1.
\]

## Claims

1. Prove

   \[
   \Pr\!\left(
   \exists r\le R,\ \exists\text{ prime }\ell>B:\ \ell\mid D_r
   \right)
   \le
   \frac{2mRNL}{B\varphi(N)}.
   \]

   The proof must count unit representatives divisible by a fixed external
   prime, use the fact that inversion permutes the units, and justify every
   union. It must explain why no independence assumption is needed.

2. Prove on the continuation branch that

   \[
   \frac N{\varphi(N)}
   \le
   \exp\!\left(
   \frac{n}{B\log_2(B+1)}
   \right)
   \le e.
   \]

   Cover arbitrary composite inputs and prime powers. Combine this with the
   first claim to get the upper bound \(2e\,mRL/B\).

3. Show that the bound remains valid if the final target \(r\) is selected
   adaptively from the declared numerical range \(1,\ldots,R\) after seeing
   the samples and prior transcript.

4. For fixed constants \(a,b,c\ge1\), assume

   \[
   m\le n^a,
   \qquad R\le n^b,
   \qquad B=n^{a+b+c+3}.
   \]

   Prove that the prepass is polynomial in \(n\) and that the probability of
   any prime \(\ell>B\) dividing any \(D_r\) is
   \(O(n^{-c-1})\).

5. On the complementary event, prove that every \(D_r\) is \(B\)-smooth and
   can be completely factored by polynomial trial division. Explain why the
   same prepass can expose the full \(B\)-smooth part of each \(C_r\) and
   remove those primes from every retained endpoint block.

## Required scope

Do not infer that \(D_r\le r\), that a smooth \(D_r\) is useless, or that no
factor-bearing product exists. The conclusion is only that fresh uniform
inverse seeds almost never provide a hard large common prime beyond a larger
polynomial trial bound. A smooth factor pool can still require a difficult
selection step. The theorem does not cover adaptive canonical-residue or
block-feedback seed states, whose marginals can be strongly nonuniform. No
factoring algorithm is claimed.
