# F220 frozen manifest

## Family

F220: aggregate primary order certificates, generalized-CRT carry terminal,
and exact Las Vegas progress/source boundary.

## Status

Frozen, self-audited, proof-only candidate. No hostile audit, blind
statement reconstruction, cross-family audit, or human audit has run. This
packet is not an unconditional factoring algorithm. It neither computes the
dyadic residue nor proves an all-input witness-source progress law.

## Frozen candidate files and SHA-256 hashes

- `STATEMENT.md`
  - `d13ee7bfcf291a581c25382f8fc35cea7824edfaa7b7f4d5a198643b18b46184`
- `PROOF.md`
  - `e1561d3be5681500a109ebf568c5f34209e36588388e9723e652af11d35704e7`
- `SELF_AUDIT.md`
  - `a4fd4eb2c5df778d58c65d0dee0728413ea0b8fcb231d0add90cd8747b160201`
- `PROVENANCE.md`
  - `34687ee6e68f399d1f593a514c513a39cb16d05ec2b2f152f6c73c19e95b6472`

## Frozen local source identities

- `PROMPT.md`
  - `a4a85d0fc0cc540af7d2ab410dc8d7b6e6bf8a72dc2037509cb0999ddc9ee938`
- `experiments/F178_coprime_order_normalization/STATEMENT.md` (P160)
  - `8a7cfbc7ea7d3fd2d0df3c31bbd540b9c3ae7a7b62dde2997b143135e5ae6ca4`
- `experiments/F187_fully_factored_nminus1_sampling/STATEMENT.md` (P165)
  - `9434188bf8c35cbd54d0f6f553b7e0698f19470745515bb1fe503fbe8b67f14e`
- `experiments/F198_beta2_carry_inverse_lowbits/STATEMENT.md` (P175)
  - `244e44b2d93fe6f62ef2ceb161b67132a12d3741a54a6ff80a2930e438dce0bb`

## Claims frozen for audit

### I. Primary contribution

1. From a fully factored \(A\), the identity \(a^A=1\pmod N\), and
   \(\gcd(a^{A/\ell}-1,N)=1\), F220 certifies
   \(\ell^{e_\ell}\mid r-1\) for every rational prime \(r\mid N\).
2. The proof works directly modulo \(r\). It does not require equality of
   complete local orders.
3. The lcm of primary blocks from different witnesses retains the universal
   predecessor property.

### II. Aggregate generalized-CRT terminal

1. A supplied residue \(p\bmod2^t\) and \(p\equiv1\pmod M\) combine at
   modulus \(L=\operatorname{lcm}(2^t,M)\), not at the product modulus.
2. Compatibility follows from the hidden true factor, and
   \(\gcd(L,N)=1\) follows from the universal predecessor property.
3. A preliminary gcd handles \(L>p\). On the remaining branch,
   \(1\le s<L<N\), so the imported GFHP interface applies.
4. The deterministic threshold is
   \(L\ge N^{1/4}/S(n)\) for numerical-QP \(S\). Prime powers already
   contained in \(L\), including overlap with \(2^t\), give no growth.

### III. Exact drift theorem

1. The potential is the remaining floored binary-log distance to the least
   power of two above the GFHP threshold.
2. Conditional expected decrement at least \(1/Q(n)\) at every nonterminal
   history gives almost-sure termination and expected numerical-QP total
   cost.
3. For this bounded potential, conditional inverse-QP probability of a
   factor or strict lcm growth is equivalent to that uniform drift condition
   up to an \(O(n)\) factor. Stage independence is unnecessary.
4. No necessity claim is made for sources that can have rare histories with
   smaller conditional drift.

### IV. Exact CRT-uniform primary law

1. For \(N=\prod_j r_j^{f_j}\), the full prime-power root probability is
   \(\Gamma=\prod_j d_j/\varphi(r_j^{f_j})\), whereas complete gcd
   nonreturn has probability
   \(B=\prod_j(1-d_j/(r_j-1))\).
2. Conditioned on full return, the local root-group coordinates and their
   Sylow coordinates are independent.
3. Every \(f_\ell(L)\) case is frozen separately:
   \(c_\ell=0\); \(0<c_\ell<\nu\);
   \(c_\ell=\nu,e_\ell>v_\ell(L)\); and
   \(c_\ell=\nu,e_\ell\le v_\ell(L)\).
4. The exact no-progress law is
   \(B+\Gamma\prod_{\ell\mid A}f_\ell(L)\). It applies to CRT-uniform
   units under \(\gcd(A,N)=1\), not automatically to independent small
   integer witnesses.

### V. Source ceilings and obstructions

1. Every aggregate satisfies
   \(M\mid D_N=\gcd_{r\mid N}(r-1)\), hence
   \(L\mid\operatorname{lcm}(2^t,D_N)\).
2. For a semiprime, \(D_N\mid q-p\). In the P165 uniform
   \(A=N-1\) model, useful probability is at most
   \(d/(p-1)+d/(q-1)\), which is inverse-exponential on balanced
   bounded-gap inputs.
3. In one synchronized cyclic direction, accumulated support never exceeds
   its fixed order \(c\), although the probability that a full
   \(\ell\)-primary part remains absent after \(k\) uniform exponent
   samples is exactly \(\ell^{-k}\).
4. P160 can supply one block on its exact-common-order exit. Its hard-branch
   theorem does not supply the needed annihilator or drift. P165 supplies
   exact uniform-root data but disproves the desired all-input uniform drift
   for that source.

## Exact scope

The packet covers a balanced semiprime terminal after a certified dyadic
factor residue is supplied. It does not handle arbitrary composites, prime
powers, unbalanced factors, carry evaluation, complete recursion, adaptive
source design, nonlinear aggregation, or a different terminal statistic.
The remaining theorem is inverse-QP conditional mass of a proper gcd or new
certified primary support for a specified witness source.

## Highest-risk points for fresh review

1. Reprove the primary certificate directly modulo every rational prime and
   test the case \(\gcd(A,N)>1\) outside Theorem D.
2. Recheck generalized-CRT overlap, \(\gcd(L,N)=1\), and the preliminary
   gcd argument that establishes \(L<N\) before GFHP.
3. Audit the stopped-drift telescoping and the conversion between mean
   decrement and useful-event probability.
4. Independently derive all four \(f_\ell(L)\) cases, including repeated
   rational-prime powers and the different denominators in \(B\) and
   \(\Gamma\).
5. Verify that strict growth always refers to \(L\), not merely to \(M\).
6. Attack the quantifiers in the attainability ceiling, bounded-gap union
   bound, and cyclic-direction model.
7. Reject any inference that independent small integers are CRT-uniform or
   that P160/P165 prove the missing source law.

## Required fresh reviews

1. Recompute the four frozen content hashes before reading the packet.
2. Run a hostile proof audit against `STATEMENT.md` and `PROOF.md`.
3. If it passes, give only `STATEMENT.md` and the frozen P175 GFHP interface
   to a fresh statement-only reconstruction agent.
4. Promote only after both reviews pass and every hash is rechecked.

## Evidence and ledger policy

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. Hashing
was used only for source identity and freeze.

No durable registry, proved ledger, failed ledger, progress ledger, statement
ledger, inspiration file, process-lessons file, or other durable ledger was
changed.
