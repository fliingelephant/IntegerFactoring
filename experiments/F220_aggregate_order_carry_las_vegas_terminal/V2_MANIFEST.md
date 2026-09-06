# F220 V2 frozen manifest

## Family and status

F220 V2: aggregate primary order certificates, exact generalized-CRT/GFHP
target, Las Vegas drift, CRT-uniform primary law, and corrected source
ceilings.

Frozen, self-audited, proof-only V2 candidate. **Do not promote.** No fresh
hostile reaudit, blind statement reconstruction, cross-family audit, or
human audit has run on V2.

The original five candidate files remain the failed V1 packet.
`HOSTILE_AUDIT.md` remains its frozen FAIL. V2 does not revise either
historical artifact.

## Frozen V2 candidate files and SHA-256 hashes

- `V2_STATEMENT.md`
  - `935ef9a28dff6bfade891ca069eb5d544236977c4c8c20c6d4208ff582b5fe45`
- `V2_PROOF.md`
  - `99ae21becd47b17a288af31670ba5a6df96529164a93c2b39e5704ef520af99d`
- `V2_SELF_AUDIT.md`
  - `4151c2d72201d7c026c432e4543433c98494a56e89979e37b5a0096893bace05`
- `V2_PROVENANCE.md`
  - `91b425bbb7d06f09ebfd83f5accde57bf305fbd173e4f4b33d8475bbc69e6f1d`

## Preserved V1 and hostile-audit identities

- `STATEMENT.md`
  - `d13ee7bfcf291a581c25382f8fc35cea7824edfaa7b7f4d5a198643b18b46184`
- `PROOF.md`
  - `e1561d3be5681500a109ebf568c5f34209e36588388e9723e652af11d35704e7`
- `SELF_AUDIT.md`
  - `a4fd4eb2c5df778d58c65d0dee0728413ea0b8fcb231d0add90cd8747b160201`
- `PROVENANCE.md`
  - `34687ee6e68f399d1f593a514c513a39cb16d05ec2b2f152f6c73c19e95b6472`
- `MANIFEST.md`
  - `63fe3afc6dd56b01f07aec7d36a4aed2738b85e26d2ddd3633c728f0229306c6`
- `HOSTILE_AUDIT.md`
  - `401258c5bcb93d1f68c6fccb233c2be5d7b51ec71b7f18ea6facd96f5b060156`

## Frozen local source identities

- `PROMPT.md`
  - `a4a85d0fc0cc540af7d2ab410dc8d7b6e6bf8a72dc2037509cb0999ddc9ee938`
- `experiments/F178_coprime_order_normalization/STATEMENT.md` (P160)
  - `8a7cfbc7ea7d3fd2d0df3c31bbd540b9c3ae7a7b62dde2997b143135e5ae6ca4`
- `experiments/F187_fully_factored_nminus1_sampling/STATEMENT.md` (P165)
  - `9434188bf8c35cbd54d0f6f553b7e0698f19470745515bb1fe503fbe8b67f14e`
- `experiments/F198_beta2_carry_inverse_lowbits/STATEMENT.md` (P175)
  - `244e44b2d93fe6f62ef2ceb161b67132a12d3741a54a6ff80a2930e438dce0bb`

## V2 repairs frozen for audit

### 1. Exact GFHP target

1. The real threshold is
   \(T_{\rm G}=N^{1/4}/S(n)\).
2. The exact integer threshold is
   \(J_{\rm G}=\lceil T_{\rm G}\rceil\).
3. The dyadic value
   \(R_*=2^{\lceil\log_2J_{\rm G}\rceil}\) is only an envelope.
4. The V2 potential is
   \(\max\{0,\lceil\log_2(J_{\rm G}/L)\rceil\}\), so it reaches zero
   exactly at GFHP.
5. The universal obstruction is
   \(\operatorname{lcm}(2^t,D_N)<J_{\rm G}\).
6. The cyclic-source obstruction is
   \(\operatorname{lcm}(2^t,c)<J_{\rm G}\).
7. A ceiling in \([J_{\rm G},R_*)\) is explicitly non-obstructive for
   GFHP.

### 2. Correct cyclic injection

1. The synchronized common order \(c\) is completely factored and satisfies
   \(\gcd(c,N)=1\).
2. Prime-to-\(r_j\) torsion injects through reduction from units modulo
   \(r_j^{f_j}\) to \(\mathbb F_{r_j}^\times\).
3. Every stripping gcd is consequently \(1\) or \(N\), even for repeated
   rational-prime powers.
4. Every returned order or primary block divides \(c\).
5. For independent uniform exponents, the probability that the full
   \(\ell\)-part remains absent after \(k\) samples is exactly
   \(\ell^{-k}\).

## Surviving claims restated for fresh audit

1. A factored annihilator and one gcd-one primary test certify a full prime
   power in every rational-prime predecessor without whole-order equality.
2. Lcm aggregation and a supplied dyadic factor residue give
   \(p\bmod L\) for \(L=\operatorname{lcm}(2^t,M)\), with
   \(\gcd(L,N)=1\).
3. A preliminary gcd handles \(L>p\); otherwise all imported GFHP premises
   hold.
4. Uniform positive conditional drift gives almost-sure termination and
   expected numerical-QP cost. Useful-event mass and drift are equivalent up
   to \(O(n)\).
5. The exact CRT-uniform no-progress law is
   \(B+\Gamma\prod_{\ell\mid A}f_\ell(L)\), with all four primary cases
   stated separately.
6. Every aggregate satisfies
   \(M\mid D_N=\gcd_{r\mid N}(r-1)\).
7. On P165's balanced bounded-gap family, aggregate support is bounded and
   CRT-uniform useful probability is inverse-exponential.

## Exact scope

V2 is a balanced-semiprime terminal after a certified dyadic residue is
supplied. It does not compute the carry, prove the witness-source drift,
transfer CRT-uniform laws to small integers, handle arbitrary composites in
the terminal, or give complete factoring recursion. P160/P165 do not fill
the missing source premise.

## Highest-risk points for fresh hostile reaudit

1. Verify that every actual-terminal or unreachability claim uses
   \(J_{\rm G}\), never \(R_*\).
2. Prove the exact-target potential drops under every strict divisibility
   update, including a step that crosses \(J_{\rm G}\).
3. Re-run the V1 threshold certificate and confirm that it now lies in the
   explicitly non-obstructive interval.
4. Verify that \(\gcd(c,N)=1\) makes reduction injective on every local
   synchronized subgroup and rules out partial repeated-prime-power gcds.
5. Re-run the V1 \(N=63,c=3\) certificate and confirm that it violates the
   new premise.
6. Reconstruct generalized CRT, the unit-modulus proof, the preliminary gcd,
   and the exact GFHP interface.
7. Independently derive all four \(f_\ell(L)\) cases and both root
   denominators.
8. Attack every quantifier in the universal ceiling, bounded-gap union bound,
   and small-integer scope statement.

## Required next reviews

1. Recompute all four V2 content hashes before reading them.
2. Run a fresh hostile reaudit against `V2_STATEMENT.md` and `V2_PROOF.md`.
3. If and only if V2 passes, run a strict statement-only reconstruction by a
   fresh agent.
4. Do not promote before both reviews pass and every frozen hash is checked.

## Evidence and ledger policy

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. Hashing
was used only to authenticate inputs and freeze V2.

No durable registry, proved ledger, failed ledger, progress ledger, statement
ledger, inspiration file, process-lessons file, or other durable ledger was
changed.
