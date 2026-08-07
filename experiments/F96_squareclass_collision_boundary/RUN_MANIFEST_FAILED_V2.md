# F96 run manifest

## Identity

- Experiment: `F96_squareclass_collision_boundary`.
- Purpose: determine the exact theorem boundary behind the F95 square-class
  witness, and test whether the second endpoint or relation is reachable
  from the first normalized state.
- Date: 2026-08-08.
- Status: corrected exact bounded result after the first candidate failed
  hostile audit and proof-blind reconstruction. Fresh audit and
  reconstruction have not run.
- Durable ledgers edited: none.

## Named artifacts

- Source: `analyze_squareclass_boundary.py`.
- Hard-timeout runner: `run_with_timeout.py`.
- Captured log: `RUN.log`.
- Machine-readable output: `OUTPUT.json`.
- Target-free selector: `blind_selector.py`.
- Target-free selector runner: `run_blind_selector_with_timeout.py`.
- Target-free selector log: `BLIND_SELECTOR_RUN.log`.
- Target-free selector output: `BLIND_SELECTOR_OUTPUT.json`.
- Human result: `RESULT.md`.
- Exact failed-v1 source, runner, logs, outputs, result, statement, and
  reconstruction are preserved under `failed_v1/`.
- Failed hostile audit: `HOSTILE_AUDIT.md`.

## Command and timeout

The command issued from this directory was

    python3 run_with_timeout.py

The runner invoked

    python3 analyze_squareclass_boundary.py \
      --n 2773 --block-a 3 --block-b 43 --target 842 \
      --output OUTPUT.json

The runner imposed a hard wall-clock timeout of 120 seconds. The process
finished with exit code zero.

The separate target-free command was

    python3 run_blind_selector_with_timeout.py

Its runner invoked

    python3 blind_selector.py \
      --n 2773 --block-a 3 --block-b 43 --bound 144 \
      --output BLIND_SELECTOR_OUTPUT.json

This runner also imposed 120 seconds and finished with exit code zero.

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

The diagnostic analysis receives \(842\) only for the explicit membership
query. Its menu acceptance path does not consult that target. The separate
target-free selector accepts only \(N\), the blocks \(3,43\), and the bound
144. It receives neither \(842\), \(P_2\), nor the factors of \(N\).

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
- Four raw integer monomials below \(N\) reproduce the old relation \(P_1\)
  and give a global root. None creates a distinct useful same-class relation.
- The complete subgroup census finds six same-class residues. Four reproduce
  \(P_1\). Exactly two give one inverse pair, one distinct relation value,
  and useful roots.
- The first positive word is \(3^{99}43\), which gives residue \(1263\).
- Its canonical inverse is \(1684\), and their product is exactly F95's
  second relation value.
- The \(n^2\) target-free menu has five same-class hits: four old-relation
  repeats and one distinct useful hit. It finds the useful hit at exponent-
  pair ordinal 5150 and unique-residue ordinal 299.
- The complete \(N=2773\) relation census has 634 unique values, 631
  nonsquares, and three same-nonzero-square-class pairs. All three are useful.
- The first global-sign counterexample in the separate bounded semiprime
  scan occurs at \(N=143\).

## SHA-256

    ad58a175d58cc0f726969be58a0d3884c7869fdce027bb39f6763358322754ec  analyze_squareclass_boundary.py
    3fcd569f574cee030ca8406825a407df882003a9cc8bfb730b549379eedc40bb  run_with_timeout.py
    723f4ba60fca5e1d8b0cdd49cf0ddb4e620a0e8a2571620d2837c603801dcf71  RUN.log
    0b0ada4d8cf40155a3758e160d30f272d42fa97d7372c3c40b589c551926f57e  OUTPUT.json
    da82081dd62ba1f13e8b7ddd7b30e0597df3f68381c777c4f9dbd9275648feaa  blind_selector.py
    2432998b7a02678017c05cfc69406a7a1d1adfe5b474c674ad2e760facf3e576  run_blind_selector_with_timeout.py
    617c4c27edb401713a24ca220e958276ee55ae8347aa827279138b4534b96469  BLIND_SELECTOR_RUN.log
    c20e4f9849a025a72e4058298b9dfb7f481ed6168531084b44f06758efb52f42  BLIND_SELECTOR_OUTPUT.json
    3e217e662428055ca8fa7e85eab3bcab8aa3fe7bb201498ca6613abd7baaf858  RESULT.md

## Evidence limit

These runs support the displayed finite certificates and the general
elementary square-class identities in `RESULT.md`. They do not prove that
the \(n^2\) menu succeeds on other inputs. They give no inverse-polynomial
density law and no all-input factoring algorithm.
