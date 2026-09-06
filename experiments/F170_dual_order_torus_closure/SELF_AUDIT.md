# F170 candidate self-audit

## Verdict

The proof-only candidate survives the internal kill test. The exact new
claim is conditional. It does not supply an all-input source law.

## Attacks checked

1. **A common torus element need not generate the ambient torus.**
   This causes no defect. Its exact order (B) still divides both ambient
   local orders, which is enough to prove (B\mid N+1).

2. **The hidden orientation is unknown.**
   The arbitrary-semiprime search enumerates both CRT signs. The balanced
   sum congruence cancels the orientation and uses one CRT class.

3. **Even orders can make the CRT systems inconsistent.**
   They do not. The common gcd is at most two, and (1,+1,-1) are all odd.
   The sum residues (2) and (0) also agree modulo two.

4. **Strict order growth need not strictly grow the least common multiple.**
   This attack is valid if a channel starts at order one and only acquires
   the factor two. The statement explicitly initializes both channels at
   the public order-two element (-1). Thereafter their gcd is exactly two,
   so an exact update by (\kappa) multiplies the least common multiple by
   exactly (\kappa).

5. **The balanced candidate count used two orientation classes.**
   The final statement instead enumerates (S=p+q). It lies in one public
   CRT class and in an interval of width
   ((3/\sqrt2-2)\sqrt N<\sqrt N/8).

6. **The gap congruence could give a smaller search.**
   It is exact: (A\mid(q-p)) and (B\mid(q-p+2\epsilon)). It has two sign
   branches. The orientation-free sum interval is narrower on the balanced
   promise, so the gap is retained as a verifier rather than the primary
   enumerator.

7. **P154 uses scalar equality, while torus points have two coordinates.**
   Equality in one hidden component means equality of both coefficients.
   The gcd of (N) and both coefficient differences is therefore the exact
   factor-first comparison. The no-factor injectivity proof survives.

8. **The quotient (B)-power map could have a kernel larger than the old
   state.**
   It cannot in a cyclic local torus. The generated local group contains the
   unique subgroup of order (B), and the kernel of its (B)-power map has
   exactly (B) elements.

9. **Hidden-log alignment might be required to make the larger state.**
   It is not required for the group-generic Harvey--Hittmeir/P154 primary
   construction. It remains required for an explicit aligned relation or a
   global presentation of every retained generator. The statement keeps
   this distinction.

10. **A capacity lower bound could be treated as a common order.**
    The (N=143,D=5,t=40,C=3) certificate refutes this. The two local
    generated orders are (5) and (7). Both exceed the cap, but their only
    common divisor is one.

11. **The natural Cayley chart might forbid synchronized large quotients.**
    It does not. Any odd-order local point avoids (-1), so the inverse
    Cayley map exists. CRT produces a clean global parameter whenever the
    two local torus orders share that odd order.

12. **A quasipolynomial cap alone controls cost.**
    It does not. The theorem explicitly caps the complete encoded
    transcript, including source records, coefficients, words, provenance,
    and rebuilt tables.

13. **The theorem might already be a complete QP factoring algorithm.**
    It is not. No result forces a closure or strict growth event in one
    source round. Inert membership and capacity remain valid terminal
    outcomes of the updater.

## Required external audits

Before promotion, this candidate needs:

1. a fresh hostile proof audit of every congruence, CRT count, torus-kernel
   claim, example, monotone-potential claim, and complexity boundary; and
2. an independent statement-only reconstruction.

No research computation supports this candidate.
