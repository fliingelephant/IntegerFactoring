# Arithmetic reflection matchings on the F322 parity graph

**Family:** route:F31

The reflection paths propagate the inverse and sign constraints of F322,
so they belong to the retained modular-hyperbola family.

**Status:** exact finite discovery data and instrumentation. No path-length
law, shortcut certification, quasipolynomial bound, or factoring algorithm
is claimed.

## Public construction

F324 imports the unchanged, main-guarded F322 Pairing class. Its state space
has \(3N\) vertices \((e,x)\), where \(e\in\{0,1,2\}\) and \(x\) is the
centered residue modulo odd \(N\).

For public \(C=(C_0,C_1,C_2)\), put
\[
 f_e=\operatorname{rep}(C_e2^{-1}\bmod N).
\]
Away from these points, the second matching is
\[
 s(e,x)=(e,\operatorname{rep}(C_e-x)).
\]
Replace the two fixed points \((0,f_0),(1,f_1)\) by one cross-layer pair and
leave \((2,f_2)\) as the unique fixed point. Starting there, the program
alternates the imported involution \(r\) and \(s\), stopping when \(r\)
fixes the current vertex. A path is censored after
\[
 \min(3N,8192)
\]
calls to \(r\). Every endpoint is passed to Pairing.decode. A decoded root
is retained as a valid oracle endpoint and is not counted as a factor.
Every decoded factor is checked by exact divisibility.

Eight methods use the same public \((a,b)\) in each query:

1. common \(C=1\);
2. common \(C=-1\);
3. common \(C=2\);
4. \(C=(1,1,b)\);
5. \(C=(1,a^{-1},b)\);
6. a fresh uniform common \(C\);
7. the F322 adjacent matching; and
8. \(C=0\), exactly the F322 negation matching.

Parameters use exact uniform residues, gcds, and Jacobi symbols only:
\(a\) is a unit with Jacobi sign \(+1\), and \(b\) is a unit with sign
\(-1\). A proper gcd during generation is recorded separately, then sampling
continues only to complete the common comparison pair. A public execution
could already return that factor. Offline factors only construct inputs,
verify outputs, and label whether \(a\) is a square. They never filter \(a\)
or select \(C\) or a path.

## Matrix instrumentation

Outside zero, swap, auxiliary-port, nonunit, and terminal cases, the imported
involution sends the coordinate to either
\[
 -x\quad\text{or}\quad c/x,\qquad
 c\in\{1,a^{-1},b,b^2,b/a\}.
\]
After reflection, the next coordinate is respectively
\[
 x+C_{\rm dest}\quad\text{or}\quad C_{\rm dest}-c/x.
\]
Every generic step checks this prediction. The corresponding matrices are
\[
 \begin{pmatrix}1&C\\0&1\end{pmatrix},\qquad
 \begin{pmatrix}C&-c\\1&0\end{pmatrix}.
\]
For \(C=c=1\), the inverse matrix cubes to \(-I\), so its projective period
is three. For \(C=2,c=1\), \((M-I)^2=0\). These algebraic identities and
actual consecutive generic-matrix run histograms are retained as
instrumentation. They are not used to skip any path state.

In the pilot, actual \(C=1,c=1\) inverse steps occurred 52 times and
\(C=2,c=1\) steps occurred 115 times. The scale counts were 490 and 407.
Maximum same-matrix generic runs were:

| dataset | common 1 | common -1 | common 2 | layer 1,1,b | layer 1,a^-1,b | uniform common | negation |
|---|---:|---:|---:|---:|---:|---:|---:|
| pilot | 12 | 24 | 21 | 13 | 12 | 19 | 1 |
| scale | 35 | 27 | 17 | 42 | 35 | 29 | 1 |

All 19,509 pilot and 124,582 scale generic coordinate predictions passed.
Only one nonstandard auxiliary cross-port occurred in all retained public
paths, in the pilot common-\(-1\) method. The full port and matrix counts
remain in the JSON output.

## Small exhaustive controls

For every odd \(N\leq31\), every reflection triple
\((C_0,C_1,C_2)\), and every one of its \(3N\) states, the program checked
\(s^2=1\) and exactly one fixed point. This covered 130,815 matchings and
10,033,581 states. The \(C=0\) matching matched the F322 negation formula
on all 765 relevant states.

For every unit pair \(a,b\) at the same moduli, all \(3N\) states checked
\(r^2=1\), and every fixed endpoint decoded and verified. This covered
4,016 pairings, 295,944 states, and 24,048 endpoints.

## Finite path results

The pilot uses \(N=209,1333,10807\), eight parameter pairs each.

| method | completed | factor endpoints | root endpoints | censors | mean r calls | maximum |
|---|---:|---:|---:|---:|---:|---:|
| common 1 | 24 | 24 | 0 | 0 | 15.88 | 63 |
| common -1 | 24 | 24 | 0 | 0 | 21.08 | 84 |
| common 2 | 24 | 24 | 0 | 0 | 32.54 | 180 |
| layer 1,1,b | 24 | 24 | 0 | 0 | 29.42 | 132 |
| layer 1,a^-1,b | 24 | 24 | 0 | 0 | 36.50 | 254 |
| uniform common | 24 | 24 | 0 | 0 | 25.17 | 131 |
| adjacent | 24 | 23 | 1 | 0 | 33.67 | 163 |
| negation | 24 | 16 | 8 | 0 | 661.00 | 3698 |

Generation encountered 12 verified factors separately. Of the 24 retained
Jacobi-positive \(a\) values, 15 were offline squares. No input or action
was removed using that label.

The scale uses \(N=66013,256027\), eight pairs each.

| method | completed | factor endpoints | root endpoints | censors | mean r calls | maximum |
|---|---:|---:|---:|---:|---:|---:|
| common 1 | 16 | 16 | 0 | 0 | 200.44 | 607 |
| common -1 | 16 | 16 | 0 | 0 | 361.38 | 3378 |
| common 2 | 16 | 16 | 0 | 0 | 166.00 | 524 |
| layer 1,1,b | 16 | 16 | 0 | 0 | 152.81 | 576 |
| layer 1,a^-1,b | 16 | 16 | 0 | 0 | 256.31 | 564 |
| uniform common | 16 | 16 | 0 | 0 | 280.88 | 1124 |
| adjacent | 16 | 16 | 0 | 0 | 188.63 | 414 |
| negation | 5 | 2 | 3 | 11 | 6376.50 | 8192 |

No generation factor occurred in the scale pairs. Seven of 16
Jacobi-positive \(a\) values were offline squares. All six reflection
families reached factors in every finite path, but these 240 completed
reflection paths supply no all-input probability or length bound. Negation's
11 cap censors are retained and not treated as failures beyond this cap.

## Resources and evidence

The pilot completed in 2.292173 seconds at 32,325,632 bytes peak RSS. The
scale completed in 0.300202 seconds at 35,520,512 bytes peak RSS. Both used
one process, an internal 28-second alarm, an external 30-second timeout, and
a 512 MiB ceiling.

Evidence:
reflection_pairings.py, pilot_output.json, pilot_status.json, pilot_run.log,
scale_output.json, scale_status.json, scale_run.log, RESOURCE.md, and
SHA256SUMS.txt.
The imported F322 parity_paths.py SHA-256 is
8d06810db2a8008357ef51229e1cacad9900c410295d8ed11419eabcbcd9a581.
