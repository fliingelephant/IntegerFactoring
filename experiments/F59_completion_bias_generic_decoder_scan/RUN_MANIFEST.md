# F59-D01 preregistered run manifest

- Family: F26, modular-inverse completion bias and whole-batch arithmetic
  decoding.
- Run ID: F59-D01.
- Status: preserved failed first attempt as a complete registered scan. The
  source produced a complete parseable output, and the artifact audit passed,
  but the hostile source-proof audit found an endpoint-counting bug and a
  runner-status bug. Rank and basis-root fields remain valid. Tail and offset
  direct-event totals are lower bounds. A corrected replay is required.
- Purpose: test the remaining source-side candidate after the generic
  gcd-free decoder removed the short-cluster requirement. The test asks
  whether dispersed independent quotient samples, random dependent descent
  prefixes, or deterministic offset descent prefixes create any exact
  square-class rank defect and any non-global basis root.
- Source: `scripts/F59_D01_scan.py`.
- Runner: `run_F59_D01.sh`.
- Declared timeout: 600 seconds, enforced by
  `/opt/homebrew/bin/timeout 600s`.
- Runtime: `/opt/homebrew/bin/python3`, expected Python 3.14.5.
- Log: `logs/F59-D01.log`.
- Output: `output/F59-D01.json`.

## Declared inputs

For each target factor bit count in `10, 14, 18, 22`, let $p$ be the first
prime at least $2^b$. For each exact rational ratio

\[
\frac{21}{20},\qquad\frac43,\qquad\frac74,
\]

let $q$ be the first prime at least both $p+2$ and the ceiling of that ratio
times $p$. Set $N=pq$. The named deterministic Miller--Rabin bases in the
source are valid over this declared sub-64-bit range. The factors are retained
only as finite ground-truth labels. No sampler or decoder step uses them.

For each input, put $n=\lceil\log_2(N+1)\rceil=N.\mathrm{bit\_length}()$.
The polynomial batch cap is $n^2$.

## Declared sources

The master Python PRNG seed is `0xF59D01`. Each random source gets a recorded
64-bit child seed. There are eight trials of each random source per input.

1. **Independent single steps:** draw $n^2$ accepted uniform units in
   $\{1,\ldots,N-1\}$ by exact gcd rejection. For each unit $u$, compute its
   canonical inverse $v$ and $k=(uv-1)/N$.
2. **Random dependent prefixes:** draw $n$ accepted uniform unit starts. From
   each start, follow at most $n$ inverse-quotient transitions, stopping that
   prefix at $1$ or a nonunit. Pool at most $n^2$ relations.
3. **Deterministic offset prefixes:** use starts $N-c$ for
   $c=1,\ldots,n$. Follow at most $n$ transitions from each start under the
   same stopping rule. This source runs once per input.

Every proper gcd found during rejection or at a nonunit endpoint is recorded
as a direct event. The diagnostic continues to build the conditional batch;
an actual factoring algorithm would stop at that event. Direct events are not
credited to the batch decoder.

## Declared preprocessing and decoder

The decoder removes the relation $k=0$, whose value is $1$, and keeps one
representative of each nonempty equal-$k$ class. These removals preserve every
modular root image under P65.

For each retained relation $A_i=Nk_i+1=u_iv_i$, the decoder starts from the
known transcript factors $(u_i,v_i)$, each tagged by column $i$. It repeatedly
uses integer gcd and exact division to refine overlapping blocks. It tracks
only exponent parity. It discards a block only when its complete parity mask
is zero. At termination the surviving integer blocks are pairwise coprime.
It exact-square-tests each block, uses each nonsquare block mask as one binary
row, and computes the complete binary kernel. This is the parity-only form of
the generic gcd-free theorem. It does not factor a block.

For every vector in one computed kernel basis, the source multiplies the
selected $A_i$, verifies that the exact positive square root exists, and tests
the root modulo $N$. It records global $+1$ and $-1$ roots separately. A
non-global root must pass both proper-gcd assertions before it is recorded as
a useful batch event.

The run records raw and unique relation counts, zero and duplicate counts,
quotient span and minimum gap, coprime blocks, square flags, square-class rank,
kernel dimension, all basis-root types, gcd refinements and pair tests, direct
gcd events, and the first useful certificate if one exists. Built-in exact
self-checks cover the square relation $6\cdot10\cdot15=30^2$ and the factoring
singleton $2\cdot8=4^2$ modulo $15$.

## Decision rule and scope

- Any useful basis root on a larger input is a discovery trigger. Retain its
  exact certificate and seek an unbounded source theorem.
- A nonzero kernel with only global roots is still a source-structure trigger.
- Full rank across the declared batches is kill evidence against these exact
  $n^2$ schedules. It is not evidence against every polynomial batch size or
  every correlated sampler.
- Passing self-checks validate this implementation only. They do not prove the
  generic decoder theorem.
- Every outcome is finite evidence. It cannot prove an all-input probability,
  a polynomial-time factoring theorem, or an asymptotic obstruction.

Preregistered source SHA-256:
`b68a07945899395649a5373f6d321009bb42cf072dfad9342392d2c8fd7c8c0a`.
Preregistered runner SHA-256:
`df5deb3b562c43e87530d6c55ef1543c7f526465f6d1b550f0f3b4199b481504`.
The registry entry was inserted before launch.

## F59-D01 outcome

- Exit status: 0.
- Measured source elapsed time: 229.38828470899898 seconds.
- Source and runner hashes matched the preregistered values.
- Log SHA-256:
  `122d6f779b5089457cf7be43c7dcef98840808052967c5e1846380cc9da3db4c`.
- Output SHA-256:
  `4ea14ef32aa2eed5d829115a12e151d8d6f38f8fa7146f67f46f18bf59120c8f`.
- The output is 223,680 bytes. The log is 2,760 bytes.
- The output's rank and root counts passed F59-A01 below and the later hostile
  source-proof audit. Tail and offset direct-event totals did not pass.

## F59-A01 — completed artifact and consistency audit

- Status: completed successfully with exit status 0 under the declared
  timeout. Every assertion passed.
- Purpose: pin all four D01 source/log/output hashes; parse the complete JSON;
  independently verify every declared semiprime label; check every batch's
  count identity, rank-nullity identity, basis-root partition, factor flag,
  direct-divisor labels, and relation cap; recompute every stored random-source
  summary; and produce exact cross-input totals without changing D01.
- Source: `scripts/F59_A01_audit.py`.
- Runner: `run_F59_A01.sh`.
- Timeout: 60 seconds, enforced by `/opt/homebrew/bin/timeout 60s`.
- Runtime: `/opt/homebrew/bin/python3`, expected Python 3.14.5.
- Log: `logs/F59-A01.log`.
- Output: `output/F59-A01.json`.
- Preregistered source SHA-256:
  `c2433fe5a5cc134ba63563869a165dd92ee0aaa1b4b4e2ec78dd02691fff1bac`.
- Preregistered runner SHA-256:
  `be796a12cb67d34495616e73233e780036073dd5372e46ae168ea7ce330aa270`.
- Disposition: this is an artifact and internal-consistency audit. It can
  validate the retained finite counts. It cannot independently prove the
  decoder theorem or support an asymptotic inference.
- Log SHA-256:
  `c67dc7e4721cd93ba13f6558d7aeb5a5ce12acf09eed1a2268e6c7a26860ddff`.
- Output SHA-256:
  `024d0eb7b5008cafafd71cfd5609136ddb4a9b7f296fc83ba4ecd171023be810`.
- Internally consistent totals: 96 independent batches and 96 random-tail batches had
  square-class rank equal to their unique relation count. All 12 deterministic
  offset batches had nonzero kernels, of total dimension 19. Their basis roots
  were 18 global $-1$ roots and one global $+1$ root. No batch source produced
  a non-global root. Direct unit-rejection or terminal gcd events were counted
  separately: 22 independent, seven random-tail, and two offset events.
- The later hostile source-proof audit accepted every rank and root conclusion,
  but rejected completeness of the random-tail and offset direct-event totals.
  The finite and non-asymptotic disposition is unchanged.

## F59-SA01 — hostile source-proof audit

- Status: FAIL narrowly.
- Report: `SOURCE_AUDIT.md`, SHA-256
  `0f5ca1c8f69d73beacadd2956ab31efba943925a2ccda1419ab64cadff18f6fc`.
- No research computation was used.
- Passed: uniform accepted-unit sampling, polynomial source caps, zero and
  duplicate preprocessing, parity-only gcd refinement, zero-mask removal,
  termination, pairwise coprimality, exact kernel, basis-only root testing,
  factor-free scope, and every retained finite rank/root inference.
- Failed source clause: after the last allowed transition, `walk_prefix` does
  not gcd-check the produced endpoint. Thus the stored seven random-tail and
  two offset direct events are only lower bounds. The 22 independent rejection
  events are complete.
- Failed runner clause: the `timeout | tee` pipeline does not preserve the
  timeout/Python exit status without `pipefail`. The complete log and parsed
  output strongly show this launch finished, but the runner is not generally
  valid.
- Required repair: check the final produced endpoint, use a runner that
  explicitly preserves source exit status, replay the same seeds and inputs,
  and compare all rank/root fields with attempt 1.

## F59-D02 — completed deterministic-offset certificate replay

- Status: completed successfully and passed F59-A02 plus the hostile repaired-
  path source re-audit. The source gcd-checks the final produced endpoint. The
  runner preserves the timeout/Python status and refuses to overwrite output.
- Purpose: explain the 19 global-only offset dependencies retained by D01.
  In particular, separate the guaranteed singleton
  $(N-1)^2$ from any additional arithmetic relation, and determine whether
  each basis dependency is already an even endpoint-pair cycle of the type
  treated by P64.
- Inputs: the exact same 12 deterministic semiprimes as D01, constructed by
  the same declared first-prime and rational-ratio rules.
- Source: `scripts/F59_D02_offset_certificates.py`.
- Runner: `run_F59_D02.sh`.
- Timeout: 120 seconds, enforced by `/opt/homebrew/bin/timeout 120s`.
- Runtime: `/opt/homebrew/bin/python3`, expected Python 3.14.5.
- Log: `logs/F59-D02.log`.
- Output: `output/F59-D02.json`.
- Superseded prelaunch source SHA-256:
  `ac77fea0c4e53c65abec85a0187d0b249ca7e844cd8ac7c2c63fde2ae5294358`.
- Superseded prelaunch runner SHA-256:
  `ac0021d1ca5911be2c5bdf753cc579285d3ebe9c487e8832ebfd41020904228a`.
- Authoritative launch source SHA-256:
  `05341e985a0e5c72911d8d118f2f33dda72241e468a190bd3355f481f348cf13`.
- Authoritative launch runner SHA-256:
  `c4db954bd60311adc2aebd9fcbca3acaec73a2e46e5b8cc8066c0aadcac780e5`.
- Authoritative log SHA-256:
  `50b3db5e8fe8123f334fd395d8c4f3fb05a839d41e8d9b7a644e198bc5cae018`.
- Authoritative output SHA-256:
  `23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e`.
- Prelaunch repair scope: one final-endpoint gcd check and explicit runner exit
  propagation only. Inputs, relation lists, decoder, variants, output fields,
  timeout, and decision rules are unchanged.

For each input, D02 reconstructs the deterministic starts $N-c$ for
$c=1,\ldots,n$ and follows at most $n$ transitions. It applies the same
zero-removal, equal-$k$ representative rule, parity gcd refinement, and exact
kernel-basis root tests as D01. It records every kernel-basis support with its
retained $(u,v,k)$ relations, exact root residue and sign, gcd certificate when
non-global, source offset/step provenance, and the set of endpoint labels with
odd incidence.

It runs three declared variants:

1. the complete offset batch;
2. the batch after removing every relation whose integer value is a square
   with global root $+1$ or $-1$ modulo $N$;
3. the batch after removing the complete trajectory started at $N-1$.

The endpoint classification is representation-specific: it describes the
retained first factor-pair representative for each quotient. A dependency is
called formal only when every retained endpoint label has even incidence. A
dependency with odd endpoint labels is an arithmetic-only relation for that
representation.

Decision rule:

- If removing global singleton squares removes the full kernel, D01's offset
  signal was only the direct loop decoy.
- If dependencies survive but all are formal endpoint cycles and global, the
  tested offset source adds no finite signal beyond P64.
- If an arithmetic-only dependency survives, retain its full certificate and
  derive its exact structure, even if its root is global.
- A non-global root is a discovery trigger.
- Every outcome remains finite deterministic evidence. It cannot prove an
  all-input source law or obstruction.

Observed outcome: the full numeric kernel dimension is 19. Twelve basis
vectors are the forced $(N-1)^2$ singleton. Seven survive both deletion
variants. All 19 basis roots are global; no non-global root was found. F59-D03
later proves that all 19 tested basis vectors are symbolic global decoys.

## F59-D01-R2 — completed corrected same-seed replay

- Status: completed successfully and passed F59-A03 plus the hostile repaired-
  path source re-audit.
- Purpose: repair the two SA01 defects while preserving D01's inputs, PRNG
  order, relation lists, decoder, metrics, and decision rules exactly.
- Inputs, ratios, batch caps, trial counts, master seed, and child-seed order:
  identical to F59-D01.
- Core source: `scripts/F59_replay_core.py`.
- Main source: `scripts/F59_D01_replay.py`.
- Runner: `run_F59_D01_replay.sh`.
- Timeout: 600 seconds, enforced by `/opt/homebrew/bin/timeout 600s`.
- Runtime: `/opt/homebrew/bin/python3`, expected Python 3.14.5.
- Log: `logs/F59-D01-R2.log`.
- Output: `output/F59-D01-R2.json`.
- Preregistered core SHA-256:
  `7b2b1a1d1b0bc46ccaaec6a178f4ff96aa7ecc26e4eb2a441521128ef14fbec9`.
- Preregistered main-source SHA-256:
  `a95a28233e05593c00be40a56b957fc1f41cceab3ea7dcf076996eb6ccc1347c`.
- Preregistered runner SHA-256:
  `a54cb42fa1286f8b6d66fb83db8192a8deb9fa36a80984cf7c919af2947b27cd`.
- Authoritative log SHA-256:
  `dc684686e111283c9ee727514b03d333e874cbac02d83a1e9bb3b21866e37bdb`.
- Authoritative output SHA-256:
  `d6a56efdeb8cdebe5253fc0b26c65b6580deef7acc89e4a40cf227cc0311fe79`.
- Preserved attempt-1 checkpoint: git commit `ec62343` contains the exact
  source, runner, output, log, audits, and failed disposition.

The only mathematical source change is an endpoint gcd check after the final
allowed transition. It records a factor if the produced endpoint is a proper
nonunit. It does not append another relation and cannot change a relation list,
rank, kernel, or basis root. A new self-check fixes the exact counterexample
$N=15,u=7$, one-step cap, whose produced endpoint is $6$ and whose gcd is $3$.

The runner refuses to overwrite an existing R2 output. It redirects the source
log without a pipeline, captures the timeout/Python status, prints the log,
and exits with the captured status.

Required post-run comparison:

- all 192 child seeds and every input label must match D01;
- every relation count, quotient metric, gcd-refinement metric, rank, kernel,
  basis-root count, and useful certificate must match D01;
- the 22 independent rejection events must match;
- random-tail and offset direct-event counts may only stay equal or increase;
- any other difference is a replay failure;
- every result remains finite evidence only.

Observed outcome: every declared non-direct field and every one of the 192
child seeds matches D01. Independent, random-tail, and offset direct-event
counts also match exactly. Thus the endpoint repair changes none of the finite
rank or root evidence in this replay.

## F59-A02 — completed independent offset-certificate audit

- Status: completed with verdict `pass`.
- Audited run: F59-D02.
- Source: `scripts/F59_A02_offset_audit.py`.
- Runner: `run_F59_A02.sh`.
- Timeout: 60 seconds, enforced by `/opt/homebrew/bin/timeout 60s`.
- Runtime: `/opt/homebrew/bin/python3`, expected Python 3.14.5.
- Log: `logs/F59-A02.log`.
- Output: `output/F59-A02.json`.
- Preregistered source SHA-256:
  `8c55170679b5cf5d1f26528cd4c972b00bed75adba05e01eceafd36a0586b0ae`.
- Preregistered runner SHA-256:
  `479956d3338b5359a603256cb9e7838ade841e90f543ce295de6345a98270c37`.
- Pinned D02 source SHA-256:
  `05341e985a0e5c72911d8d118f2f33dda72241e468a190bd3355f481f348cf13`.
- Pinned D02 runner SHA-256:
  `c4db954bd60311adc2aebd9fcbca3acaec73a2e46e5b8cc8066c0aadcac780e5`.
- Pinned D02 log SHA-256:
  `50b3db5e8fe8123f334fd395d8c4f3fb05a839d41e8d9b7a644e198bc5cae018`.
- Pinned D02 output SHA-256:
  `23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e`.
- Authoritative audit log SHA-256:
  `9322513b3e042295602c4eebb94f3ee565c406656ee2d841ff2b006501933a08`.
- Authoritative audit output SHA-256:
  `baae2e6069a0ae702038e9b6f91765338c30591507a409a230308ccdda420cc6`.

The audit independently reconstructs all offset trajectories, including the
final capped endpoint. It verifies primality and products, direct gcd events,
deduplication, every basis support, exact integer-square roots, root signs,
endpoint parity, loop flags, gcd certificates, and all aggregate counts. It
also records the complete arithmetic-only certificate summaries. A pass is an
artifact and finite-certificate result only; it is not an all-input theorem.

## F59-A03 — completed corrected-replay comparison audit

- Status: completed with verdict `pass`.
- Audited runs: F59-D01 and F59-D01-R2.
- Source: `scripts/F59_A03_replay_audit.py`.
- Runner: `run_F59_A03.sh`.
- Timeout: 60 seconds, enforced by `/opt/homebrew/bin/timeout 60s`.
- Runtime: `/opt/homebrew/bin/python3`, expected Python 3.14.5.
- Log: `logs/F59-A03.log`.
- Output: `output/F59-A03.json`.
- Preregistered source SHA-256:
  `d87a925d4c00e83e82b23c926450d612cf1a612429ec6ac069ba1aa525f3b867`.
- Preregistered runner SHA-256:
  `2c8388ded0c25e7393826b548b82538acb93819ae05283c880563e3f85d41e6f`.
- Pinned R2 log SHA-256:
  `dc684686e111283c9ee727514b03d333e874cbac02d83a1e9bb3b21866e37bdb`.
- Pinned R2 output SHA-256:
  `d6a56efdeb8cdebe5253fc0b26c65b6580deef7acc89e4a40cf227cc0311fe79`.
- Authoritative audit log SHA-256:
  `8e569990ffb680571bb22893e8fc148c0786388ece2fcb6fe975332e982d5b7b`.
- Authoritative audit output SHA-256:
  `10a9c0c1e4da7a9c4ade1cdc7b2fc8c1a102fef62a95e8890fd7b4caea0092f4`.

The audit pins both executions. It requires all 12 inputs, all 192 child
seeds, relation counts, quotient metrics, refinement metrics, ranks, kernel
dimensions, and root results to match exactly. Independent-source direct gcd
events must also match exactly. Tail and offset direct events may only
increase, and the increase must agree with the recomputed summaries. Any
other difference fails the replay.

## F59-D03 — completed R05 symbolic-specialization classification

- Status: R05 completed successfully. R01 failed during Sage import. R02 timed out while
  factoring already-split quadratics. R03 removed that factorization but still
  timed out because it represented every trajectory step as a Sage object.
  R04 replaced those objects but redundantly lifted every trajectory and was
  stopped at the same limit.
- Purpose: decide whether D02's numeric square dependencies are generic
  algebraic identities or dependencies created only after substituting the
  tested integer $N$.
- Input: the pinned F59-D02 output.
- Source: `scripts/F59_D03_symbolic_specialization.py`.
- Runner: `run_F59_D03.sh`.
- Timeout: 120 seconds, enforced by `/opt/homebrew/bin/timeout 120s`.
- Runtime: `/usr/local/bin/sage -python`, expected SageMath 10.9.
- Log: `logs/F59-D03.log`.
- Output: `output/F59-D03.json`.
- Superseded R01/R02 source SHA-256:
  `abe7bb3783a92d4e3e65c8e86fa65c4337642e76bddb5c4bec33e63670acc42b`.
- Superseded first-launch runner SHA-256:
  `7980ca081b380b1e07b2266741b8b3619ab217db2ea81ce81387d22f0523f3be`.
- Failed pre-source import log: `logs/F59-D03-R01-failed.log`.
- Failed pre-source import log SHA-256:
  `ee03036d9e3a9dad3e5875ca6636ee32453427f13917d984f7f9ceef262cadbe`.
- Corrected launch runner SHA-256:
  `5a3aeebce9e857a47d1091ba066aa1e74dd9f6d450038fb6c82e1b26d1554d3e`.
- Launch-only repair: set Sage's `DOT_SAGE` cache to the writable fixed path
  `/private/tmp/F59-D03-sage-cache`. The source, input, timeout, output,
  mathematical method, and decision rules are unchanged.
- Timed-out R02 log: `logs/F59-D03-R02-timeout.log` (empty because the source
  emits only after completion).
- Timed-out R02 log SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Superseded R03 source SHA-256:
  `90227e01248259d7c9a399a174b547de425b9bac422449ec0a975ce3630ef0e9`.
- R03 optimization: use the two already-known affine endpoint factors for
  every generic squareclass column and exact integer-bitset elimination. Sage
  factorization remains only for the 19 selected products. This is
  mathematically identical to the preregistered factor-and-rank test and does
  not change its inputs or discovery triggers.
- Timed-out R03 log: `logs/F59-D03-R03-timeout.log` (empty because the source
  emits only after completion).
- Timed-out R03 log SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Superseded R04 source SHA-256:
  `cea4fd1419311f54678f9eddd9f15de9d05d3bd77ba3fd7923298fa5a7157fae`.
- R04 optimization: represent all affine polynomials by exact pairs of Python
  rational numbers. Test the complete numeric kernel basis symbolically. If
  all basis vectors are generic and every relation denominator is a unit
  modulo $N$, generic-kernel containment in both directions proves equality,
  so constructing the full generic matrix is redundant. Sage independently
  verifies the resulting 19 selected polynomial identities. This preserves
  the original generic-versus-specialized question and discovery triggers.
- Timed-out R04 log: `logs/F59-D03-R04-timeout.log` (empty because the source
  emits only after completion).
- Timed-out R04 log SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Preregistered R05 source SHA-256:
  `5306268bf01ac569f2c75ca0be635dc1b8ed6bffc0065f6a307bbd6abf515d42`.
- R05 optimization: lift only relations used by D02's complete numeric kernel
  basis. If every basis vector is a square over $\mathbb Q[T]$, the complete
  numeric kernel is contained in the generic kernel. The reverse containment
  follows because a rational polynomial square that specializes to an integer
  has an integer rational square root. Thus the unused trajectories cannot
  change the comparison. Sage still verifies every selected identity.
- Pinned D02 output SHA-256:
  `23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e`.
- Authoritative R05 log SHA-256:
  `7ca87cd0e1255ef7879450bdb50ed0a1b429f4dbefded71e8dcfb20c5d989ebe`.
- Authoritative R05 output SHA-256:
  `9c62739d882055f480b14b0d2d6b271cb894842c9a07b9d2965220d475d20f84`.

For each relation in D02's complete numeric kernel basis, D03 lifts the current
value, its modular inverse, and its quotient to affine polynomials over
$\mathbb Q[T]$. It tests every basis vector symbolically. The two kernel
containments above then decide equality without lifting unused trajectories or
materializing a generic matrix. D03 also reconstructs each exact root
polynomial, checks its constant term and denominator, verifies its
specialization against the stored root, and asks Sage to verify the final
polynomial square identity.

Discovery triggers are: a larger numeric kernel than generic kernel, a D02
basis relation that is not a square over $\mathbb Q(T)$, a nonunit symbolic
root denominator, or a symbolic root that is non-global after specialization.
Every outcome is a finite symbolic certificate. It does not prove an
all-input sampling theorem.

Observed outcome: all 19 numeric kernel-basis vectors are exact squares over
$\mathbb Q[T]$. Their symbolic roots have constant term $1$ or $-1$, and each
coefficient denominator is coprime to its tested $N$. Hence the generic and
numeric kernels agree on all 12 batches, and every tested dependency is a
global-root decoy. The seven residual certificate instances reduce to four
symbolic identities. No discovery trigger fired.
