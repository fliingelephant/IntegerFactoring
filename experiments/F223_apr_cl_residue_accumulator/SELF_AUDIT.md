# F223 self-audit

## Verdict

PASS at self-audited candidate status.

No complete factoring algorithm is claimed. The positive theorem is an
interface theorem. The source remains open.

## Mathematical checks

1. **Local versus global exponent.** Theorem A distinguishes local orbit
   membership from the existence of one exponent across the complete bank.
   Generalized-CRT compatibility is explicit.
2. **CL quantifiers.** Theorem B imports the shared `p`-adic exponent from
   Cohen-Lenstra condition (6.4) and Theorems 6.3 and 7.8. It does not infer
   compatibility from unrelated local successes.
3. **APR failure semantics.** A failed identity is described only as a
   compositeness proof. No rational factor is inferred.
4. **Terminal enumeration.** Theorem C enumerates a public QP-size exponent
   set. At least the true exponent survives the compatibility test.
5. **Modulus coprimality.** A prime dividing both `M` and `N` would have to
   divide its own predecessor. The separate hypothesis `gcd(S,N)=1` is
   retained.
6. **Threshold.** The theorem uses the actual inequality
   `L >= N^(1/4)/A(n)`. It does not replace it by a rounded upper envelope.
7. **No common-order overclaim.** Only `M | r-1` is used. The proof does not
   require a single element of order `M` in every hidden component.
8. **Balanced-prime quantifiers.** The fixed bank determines one fixed AP
   modulus. PNT in that AP gives at least two primes in every sufficiently
   large dyadic interval. The result is not asserted for an `N`-dependent
   bank.
9. **Generic model.** Independence and uniformity are assumptions of
   Theorem E, not conclusions about semiprimes. Different exponents are not
   declared independent.
10. **Markov formula.** The weighted moment uses `q^lambda`, because the
    random variable is the logarithm of the accepted prime product.
11. **Primary-2 fibres.** The `+1` fibre always has `gcd(E,u-1)` elements.
    The `-1` fibre has the same size only when the corresponding linear
    congruence is soluble.
12. **Return versus sign gate.** The return-to-one formulas and the wider
    `{+1,-1}` upper bound are kept separate.
13. **The d formula.** The packet proves `g_u|d` and `g_v|d`. Equality is
    used only under an extra explicit hypothesis.
14. **CRT probability.** The union probability in (F5) is not confused with
    the XOR probability for a proper gcd in (F6).
15. **Bounded gap.** `d | v-u` makes both local kernel sizes bounded. Balance
    then converts inverse factor size into `2^(-n/2+O(1))`.
16. **Witness primality.** The verifier uses complete trial division through
    the integer square root for both displayed factors.
17. **Witness orbit.** The exact orbit lists prove that only `q=2` accepts
    both hidden residues.

## Workflow audit

The remote scan was exploratory. No preregistration, frozen source bytes,
output bytes, run log, or artifact hashes were supplied to this packet.
They are not fabricated.

`verify_witness.py` was written after the witness was known. Its output is
therefore a post-hoc exact reconstruction. It is not verifier-backed search
evidence and is not used to establish an asymptotic theorem.

The primary APR and Cohen-Lenstra papers were inspected for the named
theorem and algorithm semantics. No secondary exposition is used as a
mathematical premise.

No hostile audit, blind reconstruction, independent numerical replay, or
human audit has run. No durable ledger is edited by this packet.

