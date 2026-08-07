# F59 repaired-path hostile source re-audit

Date: 2026-08-07

## Verdict

**PASS for the repaired source path and its narrow finite conclusions.**

The final-endpoint defect is repaired. The four new runners preserve the
source exit status and refuse to overwrite an existing output. The corrected
same-seed replay preserves every tested relation, rank, kernel, and root
result. The D02 certificates are exact for the retained finite data.

This is **not** a pass for an asymptotic source law, a factor-correlated
sampler, a polynomial-time factoring algorithm, or a novelty claim about the
seven residual relations. The evidence is finite. All roots in these runs are
global `+1` or `-1` roots. At least four of the seven residual certificate
instances are repeated specializations of one simple symbolic identity that
forces the root `-1`.

There is also one record defect. `RUN_MANIFEST.md` still says that D02,
D01-R2, A02, and A03 have not run, although their output and log files exist.
This does not change the checked arithmetic. It must be corrected before the
experiment is treated as a closed registered run.

## Scope and method

I read the required prompt rules, the full manifest, all repaired sources,
all four runners, all four retained outputs, all four logs, and the old source
audit. I did not rerun a research computation. I used static source analysis,
exact artifact parsing, source diffs, and fresh SHA-256 calculations.

The files in scope were:

- `scripts/F59_replay_core.py`
- `scripts/F59_D01_replay.py`
- `scripts/F59_D02_offset_certificates.py`
- `scripts/F59_A02_offset_audit.py`
- `scripts/F59_A03_replay_audit.py`
- `run_F59_D01_replay.sh`, `run_F59_D02.sh`, `run_F59_A02.sh`, and
  `run_F59_A03.sh`
- outputs and logs for F59-D01-R2, F59-D02, F59-A02, and F59-A03
- the original F59-D01 source, runner, output, and log that A03 uses

## Artifact and hash check

Every preregistered source and runner hash matches. Every old and repaired
artifact hash pinned inside A02 or A03 also matches.

The main retained hashes are:

| Artifact | SHA-256 |
| --- | --- |
| `scripts/F59_replay_core.py` | `7b2b1a1d1b0bc46ccaaec6a178f4ff96aa7ecc26e4eb2a441521128ef14fbec9` |
| `scripts/F59_D01_replay.py` | `a95a28233e05593c00be40a56b957fc1f41cceab3ea7dcf076996eb6ccc1347c` |
| `run_F59_D01_replay.sh` | `a54cb42fa1286f8b6d66fb83db8192a8deb9fa36a80984cf7c919af2947b27cd` |
| `logs/F59-D01-R2.log` | `dc684686e111283c9ee727514b03d333e874cbac02d83a1e9bb3b21866e37bdb` |
| `output/F59-D01-R2.json` | `d6a56efdeb8cdebe5253fc0b26c65b6580deef7acc89e4a40cf227cc0311fe79` |
| `scripts/F59_D02_offset_certificates.py` | `05341e985a0e5c72911d8d118f2f33dda72241e468a190bd3355f481f348cf13` |
| `run_F59_D02.sh` | `c4db954bd60311adc2aebd9fcbca3acaec73a2e46e5b8cc8066c0aadcac780e5` |
| `logs/F59-D02.log` | `50b3db5e8fe8123f334fd395d8c4f3fb05a839d41e8d9b7a644e198bc5cae018` |
| `output/F59-D02.json` | `23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e` |
| `scripts/F59_A02_offset_audit.py` | `8c55170679b5cf5d1f26528cd4c972b00bed75adba05e01eceafd36a0586b0ae` |
| `run_F59_A02.sh` | `479956d3338b5359a603256cb9e7838ade841e90f543ce295de6345a98270c37` |
| `output/F59-A02.json` | `baae2e6069a0ae702038e9b6f91765338c30591507a409a230308ccdda420cc6` |
| `scripts/F59_A03_replay_audit.py` | `d87a925d4c00e83e82b23c926450d612cf1a612429ec6ac069ba1aa525f3b867` |
| `run_F59_A03.sh` | `2c8388ded0c25e7393826b548b82538acb93819ae05283c880563e3f85d41e6f` |
| `output/F59-A03.json` | `10a9c0c1e4da7a9c4ade1cdc7b2fc8c1a102fef62a95e8890fd7b4caea0092f4` |

The A02 and A03 output hashes above are current hashes from this re-audit.
The stale manifest does not yet record them. Their current log hashes are
`9322513b3e042295602c4eebb94f3ee565c406656ee2d841ff2b006501933a08`
and `8e569990ffb680571bb22893e8fc148c0786388ece2fcb6fe975332e982d5b7b`.

## Runner and endpoint repair

All four repaired runners use the same safe pattern:

1. Stop with status 2 if the target output already exists.
2. Disable immediate shell exit only around `timeout ... python`.
3. Store `$?` immediately after that command.
4. Print the log.
5. Exit with the stored status.

Thus a timeout or Python failure cannot be changed into a success by `cat` or
`tee`. A failed source can leave an output file that blocks an automatic
retry. This is conservative and does not create a false success. The logs do
not themselves store the shell exit code, but each retained source reached its
final print after writing a valid JSON output.

The mathematical diff from the old D01 core has only two changes:

- an immediate return replaces each old loop `break`;
- after exactly `step_cap` transitions, the new code checks the produced
  endpoint with `gcd` without appending another relation.

The test `N=15`, start `7`, cap `1` records relation `(7,13,6)` and then records
the proper divisor `gcd(6,15)=3`. There is no double count. A state found to be
nonunit before a transition returns immediately. A final state equal to `1`
does not create an event.

## Exact same-seed replay

A03 pins both the old and repaired source, runner, output, and log. Its
assertions check:

- all 12 input records;
- all 192 child seeds, in order;
- every non-direct field in every independent and random-tail trial;
- every non-direct offset field;
- all relation counts, quotient metrics, refinement metrics, ranks, kernel
  dimensions, root counts, and useful certificates;
- exact independent-source direct events; and
- monotone tail and offset direct events, with exact aggregate differences.

The retained A03 output reports zero differences in every direct-event class.
Therefore the old endpoint defect did not occur in these exact sampled paths.
The repaired exact totals are 22 independent rejection events, seven
random-tail events, and two offset events. Every finite rank and root result is
unchanged.

The output field `changed_non_direct_fields` is initialized to zero and is not
incremented. It is redundant. It is not evidence by itself. The explicit
equality assertions listed above are the actual check.

## Decoder proof check

The decoder is correct for the declared finite odd, distinct-semiprime inputs.

1. Each retained column has exact value `A = u*v = N*k+1`.
2. A gcd refinement of values `a` and `b` by `d=gcd(a,b)` replaces their
   square-class data by `d`, `a/d`, and `b/d`. If a column occurs in both
   masks, the old and new products differ by `d^2`. If it occurs in only one
   mask, they are equal. Thus every column square class is preserved.
3. Each nontrivial refinement strictly decreases the sum of active integer
   values. The process terminates. Each final block is coprime to every other
   final block.
4. A square final block contributes no parity condition. A nonsquare final
   block contributes its mask. Pairwise coprimality means that these masks
   describe exactly when a selected product is a square.
5. The binary elimination uses distinct highest pivots. It returns one
   independent solution for each free column. Hence the reported rank and
   kernel basis are exact.
6. The code checks each selected integer product with `isqrt`; it does not
   infer a square from floating-point arithmetic.
7. Testing only a kernel basis is sufficient here. For two dependencies,
   the root of their symmetric-difference product is the product of their
   roots divided by whole relation values. Since every relation value is
   `1 mod N`, the root residues multiply. If every basis root is `+1` or `-1`,
   every kernel root is also global.
8. Removing `k=0` columns removes only `A=1`. Keeping one representative for
   repeated `k` removes only duplicate values `A=N*k+1`. Duplicate pairs add
   global square dependencies and cannot hide a non-global root image.

For a general composite, a non-global square root of one need not make both
`gcd(r-1,N)` and `gcd(r+1,N)` proper. The source assertion is valid here
because every tested input is the product of two distinct odd primes. No
general-input factoring conclusion is valid from this code.

## D02 certificate check

D02 independently constructs the deterministic offset walks and checks the
final capped endpoint. It keeps the first factor-pair representative of each
nonzero quotient. For every stored basis certificate, it records the selected
columns, full relations, exact product root, root type, endpoint parity, loop
flag, and proper gcds when a root is non-global.

A02 independently regenerates every trajectory and verifies the raw,
duplicate, zero, and direct-event counts. It then verifies every selected
relation, every equality `u*v=N*k+1`, every exact square product, every root
residue and type, every endpoint label, every loop flag, and each aggregate.
The retained totals are:

- full kernel dimension: 19;
- forced `(N-1)^2` singleton certificates: 12, all formal and global `-1`;
- residual certificates: 7, with supports `3,3,6,7,3,3,3`;
- residual roots: six global `-1` and one global `+1`;
- non-global roots: 0;
- kernel dimension after removing global-square singleton relations: 7;
- kernel dimension after removing raw relations from the `c=1` start: 7; and
- direct gcd events: 2.

The seven residual basis quotient supports are identical in all three stored
variants. This is stronger than equal dimensions, but it is still a finite
artifact statement.

A02 does not recompute the gcd-free matrix or its kernel. It checks the stored
certificates and scalar rank-nullity totals. The fresh decoder proof above is
therefore needed for completeness. A02 alone is not an independent
end-to-end reconstruction of the decoder.

## Attempt to kill the structural interpretation

The word `arithmetic-only` has a narrow meaning. It says that the endpoints of
the **retained first representative** have odd incidence. Another factor-pair
representative of the same quotient can have different endpoint parity.
Therefore the report must not say that these dependencies are outside every
endpoint-cycle explanation.

Also, deleting the raw `c=1` trajectory does not isolate the other starts from
its later states. Different offset walks merge. For example, relations first
seen on the `c=1` path can reappear with `start_offset=2`. The variant proves
that the same quotient values remain after raw `c=1` records are deleted. It
does not prove dynamical independence from that path.

Most importantly, four of the seven residual certificate instances are the
same exact three-relation identity. They occur for

`N = 359286023, 120270159983, 18471978008993, 23456464765403`.

Their quotient values are

\[
k_1=\frac{N-8}{15},\qquad
k_2=\frac{2N-7}{3},\qquad
k_3=\frac{2N-11}{5}.
\]

The three relation values are

\[
Nk_1+1=\frac{(N-3)(N-5)}{15},\quad
Nk_2+1=\frac{(N-3)(2N-1)}{3},\quad
Nk_3+1=\frac{(N-5)(2N-1)}{5}.
\]

Their product is identically

\[
\left(\frac{(N-3)(N-5)(2N-1)}{15}\right)^2.
\]

The root is `-1 mod N`. This identity explains four finite certificate
instances without using either hidden prime. It does not invalidate the
certificates. It does invalidate any inference that all seven residual
instances already show factor-correlated source bias. The other three need a
separate symbolic analysis before any novelty claim.

## Conclusions that survive

The following statements are valid and narrowly scoped:

- The endpoint and runner defects from `SOURCE_AUDIT.md` are repaired.
- The repair changes no relation, rank, kernel, or root result in the 192
  seeded random batches or 12 offset batches.
- In the exact tested data, all 96 independent batches and all 96 random-tail
  batches have full square-class rank.
- The 12 offset batches have kernel dimension 19. Every kernel root is global,
  so no tested subset yields a factor through this decoder.
- Twelve offset dependencies are the forced `(N-1)^2` singleton.
- Seven additional exact square certificates remain under both declared
  deletion variants, relative to the retained quotient representatives.
- These seven certificates are genuine exact arithmetic facts. They are not
  evidence of a useful factoring sampler. At least four are known global
  symbolic decoys.

The following statements do not survive:

- that bare `N` has been shown to produce a factor-correlated metric hint;
- that the residual relations avoid all formal or symbolic identities;
- that the offset source has a nonzero useful success probability;
- that any observed rate continues for larger inputs; or
- that F59 currently gives a factoring algorithm or a polynomial expected-time
  bound.

The correct next question is not whether the current seven products are
squares. That is settled. The next question is whether any modified source can
produce a square dependency whose root is not symbolically forced to `+1` or
`-1` modulo `N`.
