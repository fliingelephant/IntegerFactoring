# F165-D01 result — recursive feedback changes the state but gives no new factor

**Status:** completed registered finite computation. Candidate evidence only.
No hostile audit or independent reconstruction has run.

## Verdict

The level-two-only target did not occur.

The corpus has 64 fixed semiprimes. The base decoder was null on 63 inputs.
All 63 stayed null after level one. All 63 also stayed null after level two.
There were no proper direct screens at either recursive level.

Recursive feedback still made real public changes:

- Level one attempted 5,020 section subsets. It added 315 strict new exact
  values. It increased parity rank on 63 inputs, with total rank gain 251.
  It split 67 old factor-free blocks across 42 inputs.
- Level two attempted 8,896 section subsets. It added 310 strict new exact
  values. It increased parity rank on 57 inputs, with total rank gain 310.
  It split 69 old factor-free blocks across 38 inputs.
- Exact-value duplication was dominant. Level one had 4,705 duplicates.
  Level two had 8,586 duplicates.

Thus feedback can enlarge the exact relation state and refine its integer
blocks without producing a factor-correlated square root. On this corpus,
the missing step is not state growth. It is useful root growth.

## The one positive base certificate

The first corpus input is

\[
N=100160063=10007\cdot10009.
\]

It is not a recursive-feedback success. The base source already gives

\[
100160064=N+1=10008^2.
\]

Therefore

\[
\gcd(10008-1,N)=10007,
\qquad
\gcd(10008+1,N)=10009.
\]

The registered N-only replay passed. The same root remains present in the
later union decoders. It does not count as a level-one or level-two gain.

## Exact refinement certificates

The first level-one strict block refinement occurs for

\[
N=100440259.
\]

The union decoder splits

\[
1291243=23\cdot56141
\]

and

\[
32284369=13\cdot2483413.
\]

The first level-two strict block refinement occurs for

\[
N=100740469.
\]

It splits

\[
11992913=23\cdot521431.
\]

These are public integer gcd refinements. They are not factors of `N`.

## Public and private evidence

The public analysis function receives only `N`. It constructs all seeds,
relations, factor-free blocks, decorated lifts, subsets, screens, and union
decoders without `p` or `q`. It uses no factor-assisted selector.

The disclosed corpus factors enter only after each public computation. They
confirm that every returned proper divisor is one of the two prime factors.
Every reported positive factor certificate passed a verifier whose inputs
contain only `N` and public certificate data.

## Frozen run facts

- Corpus hash:
  `bd1d2987d2eaa6d3cfda3fceea72fbd471592a659137df26ae05a3d86cec7fb3`
- Search elapsed time: `1.8571536669987836` seconds.
- Runner elapsed time: `2.2276231659998302` seconds.
- Search status: `PASS`.
- Completed instances: `64/64`.
- Failed or timed-out runs: none.

## Limitations

This is a small finite corpus. All 64 pairs share the first lexicographic
prime `p=10007`. The run proves no density, no minimum depth, no all-input
stabilization law, and no factoring algorithm. It also does not show that a
third or later recursive layer is useless.

The fixed-depth cost theorem in `COST_THEOREM.md` proves only that every
fixed number of recursive layers has QP cost. It does not prove success.
