# F127 V1 failed hostile audit

V1 correctly bounded the P114 residual, but it incorrectly extended the
same (2R^4<h) bound to the ordinary endpoint screens.

The exact counterexample is

\[
N=577\cdot587=338699,
\qquad
(u,a,b)=(4,2,3),
\qquad
R=4.
\]

Here (h=577>2R^4=512), and the residual bound also gives
(h>2uab\max(a,b)=144). However, the fourth corner is (c=24), with

\[
c^2+1=577.
\]

Thus the canonical endpoint plus screen gives

\[
\gcd(c+c^{-1}_{\rm can},N)=577.
\]

The exact V1 version is retracted. V2 separates the residual bound from the
stronger endpoint-screen bound.
