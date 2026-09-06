# F196 self-audit

## Scope checks

1. The input promise is exactly the F194 balanced squarefree semiprime
   promise: distinct odd primes with \(p<q<2p\).
2. The proof uses \(q<2p\) only to place \(B\) in \([p,2p)\) for the
   Lucas calculation. It uses oddness to invert \(N\) modulo \(2^n\).
3. The public precision is \(t=n\). This is sufficient because \(q<2^n\).
   No minimal-precision claim is made.
4. The larger factor \(q\) is unique on the promise, so the function
   reductions are well-defined.

## Published-premise checks

5. The only nonstandard external premise is Andreica's 2013 power-of-two
   binomial algorithm and its displayed bit-complexity bounds.
6. The substitution uses the paper's main range
   \(0\le Q\le P\le2^T-1\): \(P=N-1<2^n\). The paper's separate
   large-index extension is not used.
7. Preprocessing is included in (23). It is not treated as free advice or
   nonuniform data.
8. A hostile reviewer must inspect the primary paper itself, including its
   odd-factorial construction and bit-cost accounting. F196 does not
   independently reprove that published algorithm.

## Algebra and sign checks

9. The sign in (27) follows from \(q=1+hN-A\):
   \(hN=q-1+A=q-1+(-1)^BC\).
10. When \(B\) is odd, \(A<0\). Section 5 uses the Euclidean floor quotient,
    not integer division truncated toward zero.
11. The Euclidean remainder is \(N+1-q\), not \(1-q\). Its strict range in
    (30) makes (11) exact.
12. The canonical residue in (25) equals \(q\), rather than only a congruent
    value, because \(0<q<2^n\).
13. The CRT reverse reduction uses \(\gcd(N,2^n)=1\), which follows from
    oddness.

## Complexity and nonclaim checks

14. Polynomial time is stronger than the requested numerical-QP time.
15. The equivalence is a pair of promise-function reductions. It is not an
    unconditional lower bound for factoring or for modular binomial
    evaluation.
16. The exact-output argument applies only to algorithms that materialize
    the full integer. It does not apply to succinct residue algorithms.
17. Naming Kummer carries, odd factorials, \(2\)-adic gamma functions,
    product trees, or base conversion supplies no missing algorithm. The
    exact remaining coordinate is \(h\bmod2^n\), which Theorem 2 identifies
    with the factoring task.
18. No experimental computation, randomized evidence, verifier output, or
    durable-ledger edit supports this packet.

