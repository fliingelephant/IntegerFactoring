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

## F59-D02 — preregistered deterministic-offset certificate replay

- Status: preregistered but not yet authorized for launch. No D02 source
  execution has occurred. Its source and runner inherited the two SA01 defects;
  both will be amended and rehashed before launch.
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
