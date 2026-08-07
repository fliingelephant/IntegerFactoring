# F82-D02 preregistration

- Family: F26, canonical feedback and integer refinement.
- Run: F82-D02.
- Status: completed with exit status 0.
- Source: scripts/F82_D02_nonpower_search.py.
- Imported pinned source: scripts/F82_D01_search.py.
- Runner: run_F82_D02.sh.
- Command from the workspace root:
  zsh experiments/F82_canonical_phase_only_feedback_search/run_F82_D02.sh.
- Declared timeout: 120 seconds, enforced by
  /opt/homebrew/bin/timeout 120s.
- Runtime: /opt/homebrew/bin/python3.
- Log: logs/F82-D02.log.
- Output: output/F82-D02.json.

## Exact change from F82-D01

F82-D01 found \(N=703\), but its old endpoint \(27=3^3\) means exact
perfect-power extraction can expose the successful block before feedback.
That run and limitation remain preserved.

F82-D02 repeats the same declared enumeration and success test, with one
additional filter: none of the four old endpoints, the feedback word, or its
canonical inverse may be a nontrivial integer perfect power. The program
constructs the exact set of perfect powers below the largest scanned modulus.

## Decision rule and scope

- A witness survives exact perfect-power extraction on every declared
  endpoint and proves a literal integer phase-branch refinement in this
  finite box.
- A null kills only the stricter declared finite box.
- Hidden factors and orders remain discovery labels only.
- No frequency, asymptotic, complexity, or all-input claim follows.

Preregistered imported D01 source SHA-256:
9dadc2e68a364a2722fe972948dd4d6bf8af3ed3877e6f95b86588c4316b8bd4.

Preregistered D02 source SHA-256:
aeb5d3fe951b8574ee018ee603faef523a29a78ba329f9c73c0447254db3aaf3.

Preregistered runner SHA-256:
f6e100b29748887e44c828f32973af4787ca8cc3d916777da0af0419b95c67fc.

## Outcome

The run completed before the timeout and found

\[
N=2047=23\cdot89,\qquad a=11,\qquad d=2.
\]

The four old endpoints and two feedback endpoints are

\[
11,\ 1861,\ 312,\ 269;
\qquad
1778,\ 1735.
\]

None is an integer perfect power. The overlap
\(\gcd(312,1778)=2\) exposes a block of order \(11\) in both hidden fields.
Every pure power of \(2\) is synchronized, while

\[
2\cdot11=22,
\qquad
\gcd(22+1,2047)=23.
\]

This is finite discovery evidence pending independent audit.

- Imported D01 source SHA-256:
  9dadc2e68a364a2722fe972948dd4d6bf8af3ed3877e6f95b86588c4316b8bd4.
- D02 source SHA-256:
  aeb5d3fe951b8574ee018ee603faef523a29a78ba329f9c73c0447254db3aaf3.
- Runner SHA-256:
  f6e100b29748887e44c828f32973af4787ca8cc3d916777da0af0419b95c67fc.
- Log SHA-256:
  53800a402b47fd95392075882044d79a92edad06210a00e39dc6fd202d5a9983.
- Output SHA-256:
  53800a402b47fd95392075882044d79a92edad06210a00e39dc6fd202d5a9983.
