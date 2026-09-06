# F126 statement — multiplicative-rectangle carry determinant

Let \(u,\alpha,\beta\) be units modulo \(N\). For
\(i,j\in\{0,1\}\), define

\[
x_{ij}=[u\alpha^i\beta^j]_N,
\qquad
y_{ij}=[x_{ij}^{-1}]_N,
\qquad
\kappa_{ij}={x_{ij}y_{ij}-1\over N}.
\]

Order the rows \((1,x_{ij},y_{ij},\kappa_{ij})\) as \(00,10,01,11\), and
call the resulting matrix \(L\). Put

\[
\Omega_{\square}
=(\beta-\alpha)(\kappa_{11}-\kappa_{00})
+(\alpha\beta-1)(\kappa_{10}-\kappa_{01}).
\]

If

\[
\gcd(\alpha\beta(\alpha-1)(\beta-1)(\beta-\alpha),N)=1,
\]

then

\[
\det L\equiv
{(\alpha-1)(\beta-1)\over\alpha\beta}\,
\Omega_{\square}\pmod N,
\]

and

\[
\gcd(\det L,N)=\gcd(\Omega_{\square},N).
\]

The fraction denotes multiplication by the modular inverse of
\(\alpha\beta\).
