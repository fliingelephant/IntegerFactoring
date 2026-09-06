# F131 first hostile audit — FAIL AS WRITTEN

The intended theorem survived, but the first statement was not
self-contained enough and two strict inequalities were misstated.

1. The opening said only that (c) was a unit, while it canonicalized only
   (w). If arbitrary integer representatives were allowed, the
   classification was false. For example, with (N=9), take

   \[
   (c_1,w_1)=(847,1),\qquad(c_2,w_2)=(2800,1).
   \]

   Then (P_1=7\cdot11^2), (P_2=7\cdot20^2), all endpoint screens are
   nonproper, and the joint root is (+1\bmod9) although the metric roots
   differ. The corrected statement explicitly requires
   (1\le c<N).
2. The endpoint product can equal ((N-1)^2). The corrected proof uses
   (P_i\le(N-1)^2<N^2).
3. The first parametric range inequality reduces to (t>3/2), not (t>1).
   The standing hypothesis (t\ge11) still implies it.

After these corrections, the auditor found no substantive counterexample.
Both finite certificates, all four resultant bounds, the first four
arithmetic-progression members, and the classification through all odd
composites (N\le175) passed independent checks. A fresh hostile audit of
the corrected files is still required.

