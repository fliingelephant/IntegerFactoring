# F227 V2 frozen manifest

## Family and status

F227 V2: factor-cell exponents, an AP mean bound for local return
probabilities, a uniform adaptive obstruction, and a fixed-base residual-order
criterion.

Frozen, self-audited, proof-only V2 candidate. **Do not promote.** No fresh
hostile re-audit, blind statement reconstruction, cross-family audit, or
human audit has run on V2.

The five original candidate files remain the failed V1 packet.
`HOSTILE_AUDIT.md` remains its frozen FAIL. V2 does not revise any historical
artifact.

## Frozen V2 candidate files and SHA-256 hashes

- `V2_STATEMENT.md`
  - `dd905a434ed69fe0fcca5b034666e46444381cf2313176c48d42b38f76e3ad57`
- `V2_PROOF.md`
  - `a660128940d0d2b02907ff5ef476432b06d45d3098b35426a3a19564870a3da5`
- `V2_SELF_AUDIT.md`
  - `78d6f17310b23306bce3392916ccf08519b4fe0d057e522a968fda343d516e4e`
- `V2_PROVENANCE.md`
  - `f492d02486ee670e3fb143d469610a5970c8b7f318ad2677d773b64b821d0548`

## Preserved V1 and hostile-audit identities

- `STATEMENT.md`
  - `2d62d7fdad17f58f4cc6963f6b3f5345effcf70a0e38544ab1e19db08783c7a5`
- `PROOF.md`
  - `16faaa4592a368724f6948c2b19deff5711a134080dbf5c1b17e5ca99c9b6afe`
- `SELF_AUDIT.md`
  - `824e1dc642fd817e8c1ed7ba9bfde36859d7de3ac284df4f500d97d10ab5eeaa`
- `PROVENANCE.md`
  - `a89429adcf4e01b00436b2473de8a07a9bbaf7b1fd2ec7dcc95caed2674d7c39`
- `MANIFEST.md`
  - `8996c5da21be1d3ba4beac30e5ecd7a73ac6a901b46e82e6f80635090a85c244`
- `HOSTILE_AUDIT.md`
  - `4f63552d96acb0d2de9e2e6da7ee27677ba76fcc21ae1090de63e9f40ce46db5`

## Exact V2 repair

V2 defines

\[
n=\lceil\log_2(N+1)\rceil
\]

and fixes one function

\[
\mathcal Q(n)=2^{C_*(\log_2(n+1))^{k_*}}
\]

with constants independent of the input, hidden factors, history, and stage.
The same function bounds every adaptive conditional relative atom `eta H`
and the total bank length. Each base is fresh and conditionally uniform only
after its candidate and public preprocessing are fixed.

Therefore the `p^(-1/2+o(1))` estimate has one uniform `o(1)`, yields fixed
constants `c_0,n_0`, and survives a conditional union bound over the whole
bank. The exact AP inequality, fixed-base progression, stale case, and rough
residual dichotomy are unchanged.

## Frozen material claims

1. For an arithmetic progression `A_j=c+jL` and a law of largest atom
   `eta`,
   \[
   \mathbb E\frac{\gcd(A_j,m)}m
   \le\eta\left(\frac{HL\tau(m)}m+1\right).
   \]
2. A declared factor or new-support exit after exponent `A_x=x-1` has
   probability at most
   \[
   \eta\left[3+HL\left(
   \frac{\tau(p-1)}{p-1}+\frac{\tau(q-1)}{q-1}
   \right)\right].
   \]
3. Every `Q`-diffuse bank in a preterminal balanced state has only
   `2^(-Omega(n))` total useful probability.
4. For a fixed public base, returning candidate indices form one class
   modulo
   \[
   u_p=\operatorname{ord}_p(a)/\gcd(\operatorname{ord}_p(a),L).
   \]
5. Unless the two local orders are equal and already divide `L`, every
   `p`-return factors or grows the aggregate. Its density is at least
   `floor(H/u_p)/H`.
6. On a P161 rough descendant, `u_p` is either one or exceeds the chosen
   roughness cap.

## Exact scope

V2 treats distinct odd balanced semiprimes and the declared per-trial F220
return/primary-test channel. It grants complete factorizations of sampled
`x-1` values in the negative theorem. It does not cover heavy candidate
atoms, deterministic or integer-biased base sources, candidate/base
coupling, joint processing of nonreturns, arbitrary composites, or a source
for the required nonstale base. It is not a complete factoring algorithm.

## Highest-risk points for fresh hostile re-audit

1. Check that one and the same `Q` binds every history, atom, and trial
   count, and that no later `O(1)` hides history-dependent constants.
2. Reconstruct `H=Theta(p/L)` uniformly in the preterminal range.
3. Verify that the divisor bound and fixed `Q` give a uniform exponential
   constant in input length `n`.
4. Check that every declared useful outcome is contained in the direct
   candidate event or one of the two local-return events.
5. Reconstruct factor-first stripping and prove that only
   `o_p=o_q|L` is stale.
6. Verify the recursive QP product over halved input sizes.
7. Keep joint nonreturn processing and heavy candidate laws outside the
   obstruction.

## Required next reviews

1. Recompute all four V2 content hashes before reading them.
2. Run a fresh hostile re-audit against `V2_STATEMENT.md` and `V2_PROOF.md`.
3. If and only if V2 passes, run a strict statement-only reconstruction by a
   fresh agent.
4. Do not promote before both reviews pass and every frozen hash is checked.

## Evidence and ledger policy

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. Hashing
was used only to authenticate V1 and freeze V2.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, process-lessons file, or other durable
ledger was changed.
