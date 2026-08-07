# F97 run manifest

## Identity

- Experiment: F97_square_inverse_seed_n2_kill.
- Purpose: run the mandatory bounded kill test for the F96 two-block
  \(n^2\) canonical-residue selector.
- Date: 2026-08-08.
- Status: exact bounded counterexample. No audit or promotion ran.
- F95, F96, and durable ledgers edited: none.

## Named artifacts

- Source: search_square_inverse_seed_family.py.
- Hard-timeout runner: run_with_timeout.py.
- Captured log: RUN.log.
- Machine-readable output: OUTPUT.json.
- Human result: RESULT.md.

## Command and timeout

The command issued from this directory was

    python3 run_with_timeout.py

The runner invoked

    python3 search_square_inverse_seed_family.py \
      --x-min 3 --x-max 2001 --control-x 43 \
      --output OUTPUT.json

The runner imposed a hard wall-clock timeout of 120 seconds. The process
finished with exit code zero.

## Declared family and stop rule

- Family: \(N_x=(3x^2-1)/2\).
- Candidate order: odd \(x=3,5,\ldots,2001\).
- Input filter: retain only distinct odd semiprimes.
- Stability filter: for
  \(g=\gcd(p-1,q-1)\), \(A=(p-1)/g\), and \(B=(q-1)/g\), require
  \(\gcd(AB,N_x-1)=1\).
- Stop at the first retained input whose menu returns finite_null.
- If none occurs, stop at \(x=2001\).
- Run \(x=43,\ N=2773\) separately as a mandatory positive control,
  even if the increasing search stops earlier.

## Per-input menu

For each retained \(N_x\):

- compute \(n=\lceil\log_2(N_x+1)\rceil\);
- enumerate all \(0\le a,b\le n^2\);
- order pairs by increasing \(a+b\), then increasing \(a\);
- compute \(c=[3^ax^b]_{N_x}\);
- skip a residue after its first occurrence;
- compute the least positive inverse \(w\) and relation \(P=cw\);
- reject the duplicate seed value \(P=3x^2\);
- test whether \(3x^2P\) is an exact square; and
- accept only when the induced-root gcd is proper.

The menu stops on its first useful closure. It exhausts all declared pairs
before returning finite_null.

## Data separation

Bounded trial factorization is used only to:

- select distinct odd semiprimes; and
- print the stable-condition certificate.

The per-input selector is a separate function. It receives only:

- \(N_x\);
- the public normalized block \(x\), together with the fixed block \(3\);
  and
- the fixed menu rule.

It does not receive \(p,q\), a target endpoint, a target relation value, or
a target word.

## Outcome

- Positive control: \(x=43,\ N=2773\) succeeds at \((a,b)=(99,1)\).
- Increasing family inputs examined: 6.
- Values rejected before the counterexample: five failures of the distinct
  odd-semiprime filter.
- Stable semiprimes tested in the increasing search: 1.
- First counterexample: \(x=13,\ N=253=11\cdot23\).
- Stable certificate:
  \(g=2,\ A=5,\ B=11,\ \gcd(55,252)=1\).
- Menu bound: \(n^2=64\).
- Exponent pairs exhausted: 4225.
- Distinct residues: 110.
- Generated subgroup order: 110.
- Distinct same-class relations: 0.
- Useful closures: 0.

## SHA-256

    859c4d956df08050fdc803249775bdb481b786ee1734633262c63bb3edec84aa  search_square_inverse_seed_family.py
    41f13b22b37facef4a915ad41606f0917e1175bb0853f2946ce4302d49426358  run_with_timeout.py
    00208af4720055de2ce17dcdbef450dff7f961f72b5b3fe6e6aea51ae6ffdf41  RUN.log
    5acc26288f11048a69c5d5f43cc72eaf2178e3f56d25ef3329583c07ab34a659  OUTPUT.json
    c598e7f28cd35e81aba3c92af9232da2605f1a1ed8434ef537339870da860d99  RESULT.md

## Evidence limit

The run stops at the first exact counterexample. It does not estimate failure
frequency through \(x=2001\). It refutes only the declared one-step
two-block \(n^2\) selector law. It is not a general feedback obstruction or
an all-input factoring result. The counterexample has the small factor
\(11<n^2=64\), so it does not obstruct a hybrid algorithm that first removes
polynomially bounded small factors.
