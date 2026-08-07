# F96 run manifest

## Identity

- Experiment: `F96_squareclass_collision_boundary`.
- Purpose: determine the exact theorem boundary behind the F95 square-class
  witness, and test whether the second endpoint or relation is reachable
  from the first normalized state.
- Date: 2026-08-08.
- Status: exact bounded result. No audit or promotion ran.
- Durable ledgers edited: none.

## Named artifacts

- Source: `analyze_squareclass_boundary.py`.
- Hard-timeout runner: `run_with_timeout.py`.
- Captured log: `RUN.log`.
- Machine-readable output: `OUTPUT.json`.
- Human result: `RESULT.md`.

## Command and timeout

The command issued from this directory was

    python3 run_with_timeout.py

The runner invoked

    python3 analyze_squareclass_boundary.py \
      --n 2773 --block-a 3 --block-b 43 --target 842 \
      --output OUTPUT.json

The runner imposed a hard wall-clock timeout of 120 seconds. The process
finished with exit code zero.

## Exact bounds and ordering

- Fixed modulus: \(N=2773\).
- First public normalized blocks: \(3,43\).
- Membership-query target: \(842\).
- Direct integer feedback: every nonnegative monomial \(3^a43^b<N\), except
  \(1\). There are 12.
- Strict single-relation capacity subscan: \(a\le1,\ b\le2\).
- Small canonical-residue menus: \(0\le a,b\le12\) and
  \(0\le a,b\le144\).
- Menu order: increasing \(a+b\), then increasing \(a\). Duplicate residues
  are tested once.
- Subgroup census: deterministic BFS from \(1\), with multiplication by
  \(3\) before multiplication by \(43\).
- Signed-word census: deterministic BFS with steps
  \(3,3^{-1},43,43^{-1}\) in that order.
- Canonical relation census: every \(g\) with \(2\le g<N\); nonunits are
  skipped after public gcd; inverse-paired relation values are deduplicated;
  records are sorted by \((P,g,w)\).
- Same-class pair census: all pairs of distinct nonsquare relation values in
  nested sorted order.
- Counterexample census: distinct odd semiprimes \(N\le199\), then the same
  canonical relation order.

## Public-data discipline

The \(N=2773\) candidate operations use only:

- \(N\), the first normalized blocks, and the stated membership target;
- gcd and canonical modular inverse;
- modular multiplication and exponentiation;
- exact multiplication, division, and integer square root; and
- the final induced-root gcds.

The target \(842\) is used only for the explicit membership query. The blind
\(n^2\) menu does not use it, \(P_2\), or the factors of \(N\).

The full subgroup BFS and full relation census are public but not polynomial
in \(\log N\). They are certificate-only discovery computations. The bounded
two-block menus and verification of a supplied word are polynomial in
\(\log N\).

The separate \(N\le199\) counterexample census uses public trial
factorization to restrict the finite test set to distinct odd semiprimes.
It is not part of the \(N=2773\) selector and is not a factor-free search.

## Outcome

- \(\operatorname{ord}(3)=667\).
- \(\operatorname{ord}(43)=1334\).
- \(|\langle3,43\rangle|=1334\).
- \(842,2526\notin\langle3,43\rangle\).
- No raw integer monomial below \(N\) creates a same-class closure.
- The complete subgroup census finds two closing residues, one inverse pair,
  and one distinct relation value.
- The first positive word is \(3^{99}43\), which gives residue \(1263\).
- Its canonical inverse is \(1684\), and their product is exactly F95's
  second relation value.
- The \(n^2\) blind menu finds this at exponent-pair ordinal 5150 and unique
  residue ordinal 299.
- The complete \(N=2773\) relation census has 634 unique values, 631
  nonsquares, and three same-nonzero-square-class pairs. All three are useful.
- The first global-sign counterexample in the separate bounded semiprime
  scan occurs at \(N=143\).

## SHA-256

    69dee0fc29ee352d389b501e46820941f2c65f79375ef9378c525991d0df8e06  analyze_squareclass_boundary.py
    3fcd569f574cee030ca8406825a407df882003a9cc8bfb730b549379eedc40bb  run_with_timeout.py
    9d2374d1ee5bc8bb6b70a22f21bb3cf0c97e6f49efffc9da287e9adebb050f5d  RUN.log
    78217eac369f3d09dd3946639e1ba23f56e80ac5701bca6e5c983389d17c681e  OUTPUT.json
    30db80cb70034a71796d36e3d793fe7f2470e67443590016e81a094bb01f3af6  RESULT.md

## Evidence limit

This run proves the displayed finite certificates and the general elementary
square-class identities in `RESULT.md`. It does not prove that the \(n^2\)
menu succeeds on other inputs. It gives no inverse-polynomial density law and
no all-input factoring algorithm.
