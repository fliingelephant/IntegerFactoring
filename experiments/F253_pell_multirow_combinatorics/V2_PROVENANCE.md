# F253 V2 provenance

## V1 packet

The original packet froze these mathematical files:

- STATEMENT.md:
  a9b32bd8bfdc68da9fb789ffae7640d1ae504b4ba382363a80427626a75bf2a0
- PROOF.md:
  8e4152f81aa709138003317bfc35b713746dbdcc385517284437ad34b59e6b90
- SELF_AUDIT.md:
  d1049f7a678ae51bf9ea8c19eda86604706ae1f7cbad93c73d34f42170b0ccaf
- PROVENANCE.md:
  dbfb371a979b919e383686c125eca1c95d77bc68baf33594191b5d8b17d0dc39
- MANIFEST.md:
  dc12ba42c05adc0c84ab693c99464a9a79887dc73f2b91c2b04229a5be37fa65

The frozen V1 hostile audit has SHA-256

ed2eeaa272cd7a6e85769ec64efab83acd4481993e0f39e4b09ecdf00a51abac.

It returned PASS with two computation qualifications. It authenticated the
rank, subset-count, polynomial, normalized-root, carry, and finite-certificate
arguments as they were stated. It also recorded the absolute temporary-path
defect, post-run stdout transcription, and the frozen source's failure to
reject \(\gcd(x,N)=N\) outside the selected modulus.

## Strict-review failure and repair

A later strict statement-only reviewer authenticated only the frozen V1
statement and returned FAIL. Its frozen reconstruction has SHA-256

05386c64670c09c99b236d668959a5c6ff8428e01aa3095a1c52e06c38b9c906.

The reported defect was exact:

1. V1 allowed odd \(k=1\);
2. it did not require the index-\(j\) and index-\(kj\) rows to be two
   present retained columns;
3. it did not exclude \(y_{kj}=y_j\).

For \(k=1\), the purported pair is one identical row and its binary vector is
\(e_j+e_j=0\). A modular orbit repetition can likewise be removed by
duplicate cleanup rather than survive as two columns. Thus V1's polynomial
identity was valid, but its unconditional conversion into a two-column P66
dependency was overbroad.

V2 makes the minimal exact repair:

- \(k>1\) is odd;
- both index-\(j\) and index-\(kj\) rows must occur and survive cleanup;
- \(y_{kj}\ne y_j\);
- the pair span is defined only from the resulting actual nonzero vectors
  \(e_j+e_{kj}\).

V2 rechecks modular repetitions explicitly. If \(y_{kj}=y_j\), then
\(A_{kj}=A_j\), and the one-coordinate-per-\(D\) cleanup does not retain
both occurrences. Such a repetition is outside the repaired pair set. The
normalized-root homomorphism is trivial on each admitted pair vector, so it
is trivial on exactly their binary span. V2 makes no claim about the rest of
the P66 kernel.

The rank, subset-count, abstract-sharpness, carry, computation, and displayed
\(N=4331\) arithmetic are unchanged. The certificate satisfies the repaired
hypotheses: \(k=3>1\), \(j=17\), \(kj=51\), both rows are present and
retained, and their coordinates \(6\) and \(1746\) are distinct.

## Computation provenance

V2 performs no new computation. It preserves the preregistrations, sources,
outputs, and computation record from V1:

- V1_PREREGISTRATION.md:
  d30118370efb835b4585743499c72629641e74cba5205d8da6d002b9eb7a3f65
- search.py:
  8c037e858a85366932d187bb303d1de204c41da6619621586494ceb73d450d2a
- V1_STDOUT.txt:
  5ec9773a5030051a9dc0c8c7e01de0c065284ab0543fdb4cea8d756add6965ad
- V2_PREREGISTRATION.md:
  a94f5ab913fbc8899d977b65b62c5fa58014121de84588bac2f2afe078bff617
- search_v2.py:
  3dfa9fa6d4d753f76618fb51e219c5aa681f7ae07a24a2518511b04be66d4f89
- V2_STDOUT.txt:
  8b563b359363dac927fa8fd17b3d011c4ec54a6ff2ab25b8ef20a486e344e35e
- COMPUTATION.md:
  9ed4823c56462470b8e816af540e8494331b73560c857a709c35207e95b96415

No remote computation, web search, external theorem lookup, or durable
ledger edit was used for V2.
