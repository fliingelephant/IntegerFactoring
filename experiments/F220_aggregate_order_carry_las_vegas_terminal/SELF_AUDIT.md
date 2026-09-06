# Self-audit of F220

## Verdict

**PASS at self-audited status.** The packet proves a conditional terminal,
an exact drift theorem, an exact uniform probability kernel, and narrowly
scoped obstructions. It does not prove the required witness-source progress
law and is not an all-input factoring algorithm.

No mathematical computation or web search was used.

## 1. Primary-certificate attacks

1. **Does (g_\ell=1) only prove a statement modulo prime powers?** No.
   Reducing directly modulo every rational (r\mid N) gives
   (o_r\mid A) but (o_r\nmid A/\ell), so the full
   \(\ell^{e_\ell}\)-part of (A) divides (o_r\mid r-1).
2. **Is prime-field torsion injection hidden?** It is optional in Theorem A;
   the proof works directly modulo (r). It is used explicitly and safely
   in the probability law, where (gcd(A,N)=1).
3. **Are whole local orders assumed equal?** No. Each certified primary
   block is proved separately. Uncertified primary coordinates may differ.
4. **What if a gcd is neither (1) nor (N)?** It is returned immediately
   as a verified proper factor, including partial powers of a repeated
   rational prime.
5. **Can lcm aggregation lose the universal predecessor property?** No. An
   lcm of divisors of every (r-1) remains a divisor of every (r-1).

## 2. CRT-terminal attacks

1. **Compatibility:** the true (p) satisfies both congruences, hence
   (b\equiv1\pmod{\gcd(2^t,M)}). The proof also gives an explicit divided
   CRT equation.
2. **Correct modulus:** generalized CRT gives
   (L=\operatorname{lcm}(2^t,M)), not the product. This prevents double
   counting shared powers of two.
3. **Unit modulus:** if a rational prime divided both (M) and (N), the
   universal predecessor property applied to that same prime would be
   impossible. Oddness handles the dyadic part.
4. **Canonical residue zero:** (p) is a unit modulo (L), so its canonical
   residue is nonzero.
5. **Case (L>p):** then the canonical residue is the integer (p) itself,
   and the preliminary gcd factors. If that gcd does not factor, the proof
   correctly concludes (L<p<N).
6. **GFHP premises:** after the gcd screen,
   (1\le s<L<N), (gcd(L,N)=1), and the selected prime divisor obeys
   (p\equiv s\pmod L). The ratio bound is exactly numerical QP under
   (B6). Returned candidates are verified by division.
7. **Hidden carry evaluator:** none is claimed. The dyadic residue is a
   supplied certified premise.

## 3. Drift and Las Vegas attacks

1. **Does every strict aggregate update decrease the potential?** Yes.
   Since (L\mid L'), strict growth has integer ratio at least two and
   raises the floored binary logarithm by at least one.
2. **Does growth of (M) always count?** No. The event is (c\nmid L), not
   merely (c\nmid M). A primary block already covered by (2^t) gives no
   potential decrease.
3. **Almost-sure termination:** the stopped additive-drift sum bounds
   \(\mathbb E\tau\); finite expectation implies probability one of finite
   termination.
4. **Expected bit cost:** per-stage generation, encoding, exponentiation,
   gcds, and state are explicitly charged. A QP expected number of QP-cost
   stages remains QP.
5. **Independence:** the conditional drift theorem requires none. Independence
   is invoked only for the iid geometric waiting-time restatement and the
   exact uniform law.
6. **Weakest-condition wording:** (C4) is the direct uniform first-moment
   conditional drift condition. The useful-event condition is equivalent to
   it up to a polynomial factor because the maximum decrement is (O(n)). No
   claim is made that a uniform history-by-history bound is necessary for
   every QP expected-time source.

## 4. Exact uniform-law attacks

Let (G_0=\gcd(a^A-1,N)).

1. **Repeated prime powers:** (G_0=N) uses roots in the full cyclic group
   of order (h_j\), whereas (G_0=1) uses nonroots after reduction to the
   prime field. This is why their probabilities have denominators (h_j)
   and (r_j-1), respectively.
2. **Equality (d_j=\gcd(A,r_j-1)):** it uses the explicit hypothesis
   (gcd(A,N)=1), which deletes the principal (r_j)-power part of
   (h_j\).
3. **Conditioning:** only (G_0=N) enters primary stripping. Conditioned on
   this event, CRT components are independent uniform elements of the
   local (A)-root groups.
4. **Local active probability:** when
   (v_\ell(d_j)=e_\ell), exponentiation by (A/\ell) maps the
   \(\ell\)-primary coordinate onto a group of order (ell), giving
   identity probability (1/\ell). If the valuation is smaller, the value
   is identically one.
5. **No partial local gcd inside a primary test:** an active nonidentity has
   order (ell\ne r_j), so it remains nonidentity modulo (r_j); an
   identity holds modulo the full (R_j). Thus each component is wholly
   present or absent.
6. **Independence across (ell):** it follows from the direct product of
   Sylow coordinates in each cyclic root subgroup.

### Audit of every (f_\ell) case

1. (c_\ell=0): all local values are identities, so gcd (=N) with
   probability one. Correct factor: (1).
2. (0<c_\ell<\nu): inactive identities guarantee gcd support. Avoiding a
   proper factor requires all active values also to be identities. Correct
   factor: (ell^{-c_\ell}).
3. (c_\ell=\nu), useful primary: all identities is the only no-progress
   endpoint. All nonidentities certifies growth; a mixture factors. Correct
   factor: (ell^{-\nu}).
4. (c_\ell=\nu), already-covered primary: both synchronized endpoints are
   no-progress; mixtures still factor. Correct factor:
   (ell^{-\nu}+(1-ell^{-1})^\nu).

The product in (D9) is therefore exact, not a union bound.

## 5. Obstruction attacks

1. **Attainability ceiling:** every certificate divides
   (D_N=\gcd_{r\mid N}(r-1)); this is distribution-free and survives
   adaptive witnesses.
2. **Bounded gap:** for (N=pq), (D_N\mid q-p). Thus aggregate growth is
   uniformly bounded on every bounded-gap pair.
3. **Uniform probability upper bound:** in the (A=N-1) model, any factor
   or certificate path requires at least one local (A)-root. The union
   bound (d/(p-1)+d/(q-1)) is valid for every current state. Balance makes
   it inverse-exponential.
4. **Infinite family:** only the existence of infinitely many bounded prime
   gaps is imported; all per-pair algebra is elementary.
5. **Cyclic direction:** synchronized powers have equal local orders, so
   stripping cannot distinguish components. Uniform exponents fill the
   fixed exponent with exact missing-primary probability (ell^{-k}), but
   cannot exceed it.
6. **Small integers:** no CRT-uniformity is inferred from independent draws
   of numerically small witnesses. The exact useful mass is left as
   (pi_\mu(L)).

## 6. P160/P165 and top-level scope

1. P160's exact-common-order exit can contribute a block. Its hard-branch
   theorem does not supply a factored common annihilator and therefore does
   not establish Theorem A's identity premise.
2. P165 supplies the exact uniform root-group framework but also supplies
   the bounded-gap obstruction. It cannot prove the inverse-QP drift.
3. The packet is balanced-semiprime and terminal-scoped. It does not handle
   arbitrary composites, primes, prime powers, unbalanced factors, the
   carry evaluator, complete recursion, or all-input Las Vegas accounting.

## 7. Highest-risk items for fresh audit

1. Re-derive all four lines of (D8), especially the distinction between
   (0<c_\ell<\nu) and (c_\ell=\nu).
2. Check the repeated-prime-power denominators in (B) and (Gamma).
3. Check that strict (M)-growth is never substituted for strict
   (L\)-growth.
4. Check the preliminary gcd argument establishing the remaining GFHP
   hypothesis (L<N).
5. Check that the cyclic-direction statement is only a source-model
   obstruction and not presented as a general lower bound.
