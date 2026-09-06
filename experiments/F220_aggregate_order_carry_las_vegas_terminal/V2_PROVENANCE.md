# F220 V2 provenance

## Version origin

F220 V1 froze an aggregate primary-order/carry terminal and exact source
law. Its hostile audit returned **FAIL** while validating Theorems A--D and
the bounded-gap analysis. It found two false obstruction claims in Theorem
E:

1. V1 compared attainable ceilings with a rounded dyadic target \(R_*\),
   although GFHP already applies at the smaller real threshold
   \(N^{1/4}/S(n)\).
2. V1 inferred that equal complete local orders prevent factor-first
   splitting over repeated prime powers. That inference needs the common
   cyclic order to be coprime to \(N\), or a squarefree restriction.

The failed V1 packet and hostile audit are preserved without modification.
V2 is a new proof-only candidate.

## Frozen V1 identities

- `STATEMENT.md`:
  `d13ee7bfcf291a581c25382f8fc35cea7824edfaa7b7f4d5a198643b18b46184`;
- `PROOF.md`:
  `e1561d3be5681500a109ebf568c5f34209e36588388e9723e652af11d35704e7`;
- `SELF_AUDIT.md`:
  `a4fd4eb2c5df778d58c65d0dee0728413ea0b8fcb231d0add90cd8747b160201`;
- `PROVENANCE.md`:
  `34687ee6e68f399d1f593a514c513a39cb16d05ec2b2f152f6c73c19e95b6472`;
- `MANIFEST.md`:
  `63fe3afc6dd56b01f07aec7d36a4aed2738b85e26d2ddd3633c728f0229306c6`;
- `HOSTILE_AUDIT.md`:
  `401258c5bcb93d1f68c6fccb233c2be5d7b51ec71b7f18ea6facd96f5b060156`.

## Exact V2 repairs

### Actual terminal threshold

V2 defines

\[
T_{\rm G}=\frac{N^{1/4}}{S(n)},
\qquad
J_{\rm G}=\lceil T_{\rm G}\rceil.
\]

Since the aggregate modulus is integral, \(J_{\rm G}\) is the exact
discrete GFHP target. The old dyadic value is retained only as

\[
R_*=2^{\lceil\log_2J_{\rm G}\rceil},
\qquad
J_{\rm G}\le R_*<2J_{\rm G}.
\]

The V2 potential is the exact-target quantity

\[
\max\{0,\lceil\log_2(J_{\rm G}/L)\rceil\}.
\]

It reaches zero exactly at GFHP. The universal and cyclic ceiling
obstructions now compare with \(J_{\rm G}\). V2 explicitly records that a
ceiling in \([J_{\rm G},R_*)\) can reach GFHP even though it cannot reach
the rounded envelope.

### Prime-to-input cyclic direction

V2 keeps arbitrary odd prime-power components but adds

\[
\gcd(c,N)=1.
\]

For each \(R_j=r_j^{f_j}\), the reduction kernel from local units to the
residue field is an \(r_j\)-group. It intersects a cyclic subgroup of order
\(c\) trivially. This proves injection of the entire synchronized direction,
so every stripping gcd is \(1\) or \(N\), even for repeated rational-prime
powers. The exact order and \(\ell^{-k}\) accumulation laws are unchanged.

## Restated material result

V2 remains a complete statement/proof packet for five layers:

1. primary certificates from a factored annihilator and gcd-one tests;
2. lcm aggregation with a supplied dyadic factor residue by generalized CRT;
3. the exact GFHP terminal and a uniform conditional-drift theorem;
4. the exact CRT-uniform four-case primary progress kernel; and
5. the common-predecessor, bounded-gap, and corrected cyclic-source
   obstructions.

The unresolved step is still an all-input inverse-QP progress law for a
specified efficiently generated witness source.

## Local predecessor identities

- `PROMPT.md`:
  `a4a85d0fc0cc540af7d2ab410dc8d7b6e6bf8a72dc2037509cb0999ddc9ee938`;
- `experiments/F178_coprime_order_normalization/STATEMENT.md` (P160):
  `8a7cfbc7ea7d3fd2d0df3c31bbd540b9c3ae7a7b62dde2997b143135e5ae6ca4`;
- `experiments/F187_fully_factored_nminus1_sampling/STATEMENT.md` (P165):
  `9434188bf8c35cbd54d0f6f553b7e0698f19470745515bb1fe503fbe8b67f14e`;
- `experiments/F198_beta2_carry_inverse_lowbits/STATEMENT.md` (P175):
  `244e44b2d93fe6f62ef2ceb161b67132a12d3741a54a6ff80a2930e438dce0bb`.

P160 can supply one admissible exact-common-order block but does not supply
the hard-branch annihilator or drift law. P165 supplies the CRT-uniform
root-group framework and the bounded-gap rare-return obstruction. P175
supplies the audited GFHP interface after a factor residue modulo a unit
modulus is known.

## Mathematical dependencies

1. Lagrange's theorem in finite prime fields.
2. Generalized CRT and extended Euclid.
3. The GFHP arithmetic-progression interface frozen in P175.
4. CRT and cyclicity of odd prime-power unit groups.
5. Sylow decomposition of finite cyclic groups.
6. The fact that the kernel of reduction modulo an odd rational prime is a
   prime-power group.
7. Stopped telescoping for a bounded nonnegative drift potential.
8. The standard bounded-prime-gap theorem, used only to obtain an infinite
   family from the elementary fixed-pair obstruction.

No heuristic CRT independence for small integers, smoothness assumption,
prime-tuple conjecture, or unproved progress distribution is used.

## Evidence and ledger policy

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. Hashing is
used only to authenticate the failed V1 inputs, local predecessors, and V2
freeze.

No durable registry, proved ledger, failed ledger, progress ledger, statement
ledger, inspiration file, process-lessons file, or other durable ledger is
edited by V2.
