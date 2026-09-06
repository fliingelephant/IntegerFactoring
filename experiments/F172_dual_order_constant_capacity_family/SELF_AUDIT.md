# F172 candidate self-audit

## Verdict

The proof survives the internal kill test. The result is a narrow obstruction
to the F170 state-growth terminal branch, not to factoring.

## Checks

1. **The CRT class might not be reduced.** It is reduced. The four moduli are
   pairwise coprime, and the residues $3,1,4,2$ are units in their respective
   rings.

2. **Linnik might return $q\le p$.** The congruence $q\equiv1\pmod p$ rules
   this out. The first positive candidate after one is $p+1$, which is even.
   Hence every prime in the class is larger than $2p$.

3. **The $3$-adic valuation might be uncontrolled when $v=1$.** In that
   case $v_3(p-1)=1$, so the common valuation is one regardless of any higher
   valuation in $q-1$. When $v\ge2$, the residue $4\pmod{3^v}$ makes
   $v_3(q-1)=1$ exactly.

4. **A large odd prime might enter one shifted gcd.** Every odd prime at
   least five dividing either $p-1$ or $p+1$ divides $M$, while
   $q\equiv2$ modulo its full prime power. It divides neither relevant
   $q-1$ nor, for the $p-1$ cross term, $q+1$.

5. **The two-adic parts might grow.** The fixed class $q\equiv3\pmod8$
   gives valuations one for $q-1$ and two for $q+1$. This bounds all three
   shifted gcds exactly as stated.

6. **Different discriminants might evade the bound.** All four local Legendre
   orientation pairs are covered by the four shifted gcds. Keeping many
   discriminants cannot create an exact common order outside the
   corresponding ambient gcds.

7. **The construction might hide exponential input inflation.** It does not.
   The CRT modulus is below $8p^3$, and the absolute Linnik exponent gives
   $q=p^{O(1)}$. Thus the smaller factor remains exponential in the bit
   length.

8. **The family might be balanced.** It is not: $q>2p$. No balanced claim is
   made.

9. **This might be a factoring lower bound.** It is not. An updater can still
   factor through a local equality or order mismatch. Integer relations,
   carries, roots, and other decoders remain outside the theorem.

## Required external checks

Before promotion, a hostile auditor should attack the CRT class, all three
gcd equalities, the Linnik size argument, and the translation from ambient
group orders to exact common-order bounds. A fresh statement-only agent must
then reconstruct the proof without seeing `PROOF.md`.
