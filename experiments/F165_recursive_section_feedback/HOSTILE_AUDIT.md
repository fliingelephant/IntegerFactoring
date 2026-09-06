# F165-D01 hostile audit

**Verdict: PASS at the hostile-audit stage.**

The registered finite null result and the proof-only fixed-depth cost theorem
survived this audit. This does not make either claim verifier-backed. An
independent end-to-end reconstruction has not run.

## Audit boundary

I read the computation rules in `PROMPT.md`, every top-level F165-D01 source
and evidence artifact, the imported F157 factor-free core, and the pinned F152
and F156 V2 interfaces. I did not execute `search.py`, the timeout runner, a
replay routine, or any new experimental checker. I made no durable-ledger
edit. The checks below use source inspection, frozen-file hashes, and
read-only accounting of `OUTPUT.json` and `RUN.log`.

## Registration and integrity

The observed SHA-256 values agree with `REGISTRATION.json` and `MANIFEST.md`:

| Artifact | Observed SHA-256 |
|---|---|
| `PROMPT.md` | `a4a85d0fc0cc540af7d2ab410dc8d7b6e6bf8a72dc2037509cb0999ddc9ee938` |
| `QUESTION.md` | `45b42964446c5103c6bb1d81992451a7d4a21f2a8c4f7b7bc62bd03150ca4805` |
| `DESIGN.md` | `ea115dfa9b1a49e5371f758f91743278f02bc6a5d6ec7316c49db18bdad5ef57` |
| `search.py` | `2a7852f8438003f0db1dd49b7721d02ae2c1cfcea8b114f1e58cc69b74f04427` |
| `run_with_timeout.py` | `5530b2604cf3e4029fb8afbd8c72711a0558a5739727cd166b12dd931c4c26ea` |
| `REGISTRATION.json` | `b3bbfc3e8f3acf45c9adc66a0c2444312b4ce279d001e73d5e415f495844fd22` |
| `OUTPUT.json` | `94ca36ee995819d384e260d50213105b58c3b91377b3a8e51ba155fa7b218dcc` |
| `RUN.log` | `4a71dda9953162013810938b0c41556aff6988b44b592e546bddaf78d4b90c9f` |
| `RESULT.md` | `04ff14f6f0664073565c36370308c610569518f84fbd005b8ad3f835edd717d3` |
| `COST_THEOREM.md` | `af7a30f062a178e4f4a77a6c41f552de0ef3817e542395907ef074857777f995` |
| `MANIFEST.md` | `df609f058087c0632e48f2d88192c8abca9d59032d8ad008ca1d74e9dbf8c50c` |

The current post-run `FAILED_RUNS.md` hash is
`106807965c5320841746cc200c1b552d6f96e3cac4e8349a0b99372d252b3f60`,
as stated in the manifest. Its preregistered pre-run hash is
`ed44de769f8b53361768ea1199d9c3ba610d7cb5e2e3dffb0ef0b1bdb63a5ca8`.
The manifest explicitly records this post-run change. All six upstream pins
match their present files, including the imported F157 source hash
`1f9bf511a8a0d5783dfcbca891d7e4022e158382395b3925cb38241ee2d6cb69`.

The normalized registration embedded in `RUN.log` is byte-for-byte
equivalent to the current registration. The log records the named 600-second
timeout, the registered Sage command, exit code `0`, runner elapsed time
`2.2276231659998302`, and final status `PASS`. It contains exactly 64 ordered
instance markers. Each instance reaches a terminal `active=0` refinement for
the base, level-one union, and level-two union: 64 completions for each of the
three decoders. No `RUN_FAILED_*` or unfinished `ATTEMPT_*` file is present.

This is a coherent local registration chain. It is not an external,
tamper-evident timestamp or committed preregistration. That evidence limit
does not contradict the registered computation, but an independent referee
must not describe the local timestamps alone as external attestation.

## Frozen corpus and public-input boundary

The source deterministically constructs primes by trial division, sorts
admissible pairs lexicographically, and takes the first 64. The frozen output
contains `p=10007` and these 64 increasing `q` values:

`10009, 10037, 10039, 10061, 10067, 10069, 10079, 10091, 10093, 10099,
10103, 10111, 10133, 10139, 10141, 10151, 10159, 10163, 10169, 10177,
10181, 10193, 10211, 10223, 10243, 10247, 10253, 10259, 10267, 10271,
10273, 10289, 10301, 10303, 10313, 10321, 10331, 10333, 10337, 10343,
10357, 10369, 10391, 10399, 10427, 10429, 10433, 10453, 10457, 10459,
10463, 10477, 10487, 10499, 10501, 10513, 10529, 10531, 10559, 10567,
10589, 10597, 10601, 10607`.

All satisfy the registered range and `10007 < q < 2*10007`. The 64 output
indices are exactly `0..63`; every recorded `N` equals the disclosed `p*q`.
The corpus hash is consistently recorded as
`bd1d2987d2eaa6d3cfda3fceea72fbd471592a659137df26ae05a3d86cec7fb3`
in the output, result, and manifest.

`construct_corpus()` is the only function that receives `p,q` before an
instance is analyzed. `analyze_public(modulus, core)` receives only `N`.
The imported calls used by it are factor-free integer refinement utilities;
they have no disclosed-factor argument. `factor_assisted_classification()`
runs only after the public result is complete. It checks labels and does not
select candidates. Thus the candidate source, both recursive scans, all
decoder decisions, and every gcd are N-only.

Every modulus has `n=27`. The base loop is exactly `range(2,n+2)`, so it
attempts all 27 seeds `2..28`. Since both disclosed primes exceed 10,000,
every such seed is a unit, as required.

## Decoder and recursive semantics

The implementation matches the frozen order:

1. Exact values retain first occurrence order. Before a duplicate is
   deleted, `add_record()` compares the supplied roots and tests their ratio
   as a square root of one. It preserves occurrence count and layer
   membership. All supplied roots in this experiment are `1`, so all 14,259
   observed duplicates (968 base and 13,291 recursive) have ratio `1`; the
   non-global duplicate-root branch is implemented but not exercised by this
   corpus.
2. The pinned F157 core removes exact square and odd-perfect-power
   redundancy, repeatedly gcd-refines all endpoints, and terminates with
   pairwise-coprime nonsquare blocks and labelled row masks. F165 then checks
   for every retained record that
   `A = half^2 * product(selected blocks)` exactly, and checks that every
   block and half is a unit modulo `N`. These checks make the parity
   coordinates factor-free and complete for the retained exact values.
3. Gaussian elimination scans columns in first-occurrence order and always
   uses the largest active row as pivot. The selected actual decorated lift
   is stored with each pivot. Every dependent column produces a fundamental
   kernel root. These dependencies form a kernel basis, so testing their
   images determines whether the complete normalized-root image is global.
4. Level one freezes the base basis. Level two freezes the rebuilt
   base-plus-level-one basis. Each level scans all support-one basis entries,
   then every pair `(i,j)` with `i<j`. The star product divides once by each
   common factor-free block. Its least positive inverse is used for both sign
   screens, and the exact positive value `z*w` is offered to root-aware
   deduplication before the next union decoder is built.

The source contains no factor-assisted candidate index, hidden factor call,
or recursive use of a record before its level ends. The candidate, exact
value, block, and selected-column hashes are deterministic commitments to
the in-memory sequences. Their 64-hex shape and all zero-growth hash
linkages are consistent. The underlying sequences are not stored in
`OUTPUT.json`, so these per-sequence hashes cannot be independently replayed
from the frozen summary alone. That is work for the required independent
reconstruction, not evidence supplied by this hostile audit.

## Frozen accounting and null target

All per-instance identities hold: attempts equal new values plus duplicates;
the support-at-most-two count is `r(r+1)/2`; each level's frozen rank equals
the preceding decoder rank; union columns equal old columns plus strict new
values; selected columns equal rank; nullity equals columns minus rank; and
both sign-screen totals equal the attempt count. Rank never decreases. Every
old block is either preserved or certified as strictly split; the
`changed_without_proper_overlap` count is zero throughout.

| Quantity | Level 1 | Level 2 |
|---|---:|---:|
| attempted subsets | 5,020 | 8,896 |
| strict new exact values | 315 | 310 |
| duplicate exact values | 4,705 | 8,586 |
| inputs with positive rank gain | 63 | 57 |
| total rank gain | 251 | 310 |
| inputs with strict old-block splits | 42 | 38 |
| total strictly split old blocks | 67 | 69 |
| proper direct candidates | 0 | 0 |
| duplicate-root splits | 0 | 0 |

The base normalized-root image is non-global on exactly one input and null
on the other 63. The only level-one and level-two non-global images are the
same inherited base root on that first input. All 63 base-null instances
remain null after level one and after level two. Therefore
`first_level_two_only` is correctly `null`, and the registered target count
is zero.

The first level-one refinement witnesses are exactly
`1291243 = 23*56141` and `32284369 = 13*2483413` for `N=100440259`.
The first level-two witness is
`11992913 = 23*521431` for `N=100740469`. The decoder's unit checks ensure
these are integer-block refinements, not factors of `N`.

## Base factor certificate

For the first input,

`N = 100160063 = 10007*10009`

and the retained base relation is

`N+1 = 100160064 = 10008^2`.

Its normalized root is `10008`, so

`gcd(10008-1,N)=10007` and `gcd(10008+1,N)=10009`.

The frozen certificate contains only `N`, the exact relation value, and the
integer root data. It passes the source's N-only replay at the base and is
replayed again, unchanged, in both later union decoders. This is one inherited
base event, not recursive feedback success.

## Fixed-depth cost theorem

The counting recurrence is valid. With
`x_h = log2(max(2,R_h))` and `D <= L^b`,

`R_(h+1) <= 2(D+1) max(2,R_h)^D`

gives

`x_(h+1) <= D*x_h + O(log(D+1))`

and hence, for fixed `H`,

`x_H = O_H(L^(a+bH) + L^(bH))`.

Thus record count is `2^(L^(O_H(1)))`. New modular endpoints have `O(n)`
bits and new canonical exact products have at most `2n` bits. The assumed
base transcript already has quasipolynomial total length. At fixed depth,
provenance expands by at most `D^H`, and standard gcd-free refinement,
perfect-power extraction, elimination, modular arithmetic, inversion, and
gcd work are polynomial in the explicit transcript length. The time and
space conclusion follows.

The theorem correctly stops at fixed `H`. For support two, its own recurrence
permits `log R_H = Theta(2^H)` in the abstract full-rank case. It therefore
does not supply a uniform quasipolynomial bound for growing depth, a success
law, or a factoring algorithm.

## Scope that survived the hostile audit

F165-D01 is only a registered 64-instance capability/null scan plus a
fixed-depth counting theorem. All 64 semiprimes share `p=10007`. The evidence
proves no density, minimum useful depth, stabilization law, all-input
behavior, or asymptotic factoring result. Subject to that exact scope, I
found no refutation, quantifier slip, factor leakage, accounting mismatch, or
cost-recurrence gap.
