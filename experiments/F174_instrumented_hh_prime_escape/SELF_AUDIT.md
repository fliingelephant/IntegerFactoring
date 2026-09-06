# F174 candidate self-audit

## Central claim

F174 exposes the internal branches of Harvey--Hittmeir Algorithm 3.1. It
adds a smooth-prefix trial scan and P154 absolute/relative screens only when
the published algorithm would return an unknown exact order at line 13.

The output is factor, a factored exact common-order state above the target,
or one polylog-small prime hard block. The hard branch is not progress toward
a factor by itself.

## Exit audit

- The small-input branch is finite preprocessing.
- The even branch is outside the odd promise.
- The early \(2^D<N\) branch is impossible because \(D\ge n\).
- A loop divisor and a prime-divisor order gcd are proper factors.
- The line-19 state is exact globally by the published invariant and exact
  in every prime-power component by the gcd-one screens.
- The final arithmetic progression finds a prime divisor on composite
  inputs.
- Only line 13 needs the new classification.

No published exit is silently discarded.

## Prime-power audit

The HH paper states equality of the exact order modulo every rational prime
on its no-factor exact-order branches. Since the exact order modulo a prime
power is a multiple of the order modulo its prime and a divisor of the exact
global order, it is equal too. Thus the common-state theorem is valid for
arbitrary odd composites, not only squarefree inputs.

The same argument proves that every common order is coprime to \(N\).

## Smooth-prefix audit

At line 13, all earlier integers are annihilated by the current \(M\). This
uses monotonic divisibility of the accumulated lcm state. A nonunit earlier
integer would have had a smaller prime divisor of \(N\), already ending the
run.

For \(y=\beta-1\), every \(y\)-smooth integer below a hidden prime is an
\(M\)-th root. Hence \(\Psi(p,y)\le M\). The exact dyadic definitions
\(X_D=2^{H_D}\) and \(Y_D=H_D^2\) avoid real-number rounding. If
\(y\ge Y_D\), the cited smooth-number lower bound gives

\[
\log\Psi(X_D,y)
\ge\tfrac12\log X_D
>\log M.
\]

Thus every hidden prime is at most \(X_D\). The known congruence
\(p\equiv1\pmod M\) makes the QP arithmetic-progression scan complete.

The inequality \(X_D\ge y\) uses the published
\(\beta\le D^{1/3}+1\) loop range and holds after a finite threshold.

## Absolute and relative screen audit

- \(r\mid\Lambda_D\) exactly when \(\sigma(r)\le D\).
- A global \(\Lambda_D\) return gives a factored annihilating multiple, so
  divisor stripping is legal.
- A common relative return gives the factored multiple \(eM\), so P150 is
  legal.
- In either branch, the original line-13 certificate
  \(\operatorname{ord}_N(\beta)>D\) forces the resulting exact common state
  above \(D\).
- If no relative return occurs, every local quotient order exceeds \(C\).
  This is only capacity.

## QP audit

The new numerical scan bound satisfies

\[
X_D=\exp(O(\log D\log\log D)).
\]

If \(D\) is QP in \(n\), then \(X_D\) is also QP. The cutoff
\(Y_D=(\log D)^{O(1)}\) is polylogarithmic in \(n\). The lcm and all
transcripts have QP bit length.

## Scope risks retained

1. The candidate relies on the explicit Algorithm 3.1 transcript, not only
   Theorem 1.1's black-box output contract.
2. It uses the cited smooth-number lower bound as an external premise.
3. It does not make the hard quotient close.
4. It does not find a multiple of either large hidden local order.
5. It does not transfer ordinary order into a nonsplit torus.
6. It supplies no balanced or all-input success theorem beyond the exact
   trichotomy.
7. It is not a QP factoring algorithm.

These limits are necessary and are explicit in the statement.
