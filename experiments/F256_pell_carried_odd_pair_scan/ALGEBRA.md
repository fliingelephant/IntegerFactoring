# F256 algebra — carried odd Pell multiples

Let `D>0`, let `h` be odd, and define the integer polynomials

\[
F_{h,D}(Y)=\sum_{r=0}^{(h-1)/2}
 {h\choose 2r+1}D^rY^{2r+1}(1+DY^2)^{(h-2r-1)/2},
\]

\[
G_{h,D}(Y)=\sum_{r=0}^{(h-1)/2}
 {h\choose 2r}D^rY^{2r}(1+DY^2)^{(h-2r-1)/2}.
\]

If `U^2-DV^2=1`, binomial expansion gives

\[
(U+V\sqrt D)^h=U G_{h,D}(V)+F_{h,D}(V)\sqrt D.
\]

Taking norms, now as a polynomial identity in `Y`, gives

\[
(1+DY^2)G_{h,D}(Y)^2=1+D F_{h,D}(Y)^2. \tag{1}
\]

Fix a Pell power `(S_j,T_j)` and an odd modulus `N`.  Put

\[
y=T_j\bmod N,\qquad y'=T_{hj}\bmod N,
\]

using canonical residues in `[0,N)`.  Since `F` has integer coefficients,
`F(y)=y'+cN` for a unique integer `c>=0`.  Let

\[
A=1+Dy^2,\quad A'=1+Dy'^2,\quad
H=Dc(2y'+cN).
\]

Equation (1) gives the exact carry identity

\[
A G_{h,D}(y)^2-A'=NH. \tag{2}
\]

Let `x=S_j mod N` and `x'=S_{hj} mod N`.  The same binomial identity gives

\[
x'=xG_{h,D}(y)\pmod N,\qquad x^2=A\pmod N,
\qquad x'^2=A'\pmod N. \tag{3}
\]

Assume the public root screens give `gcd(x,N)=gcd(x',N)=1`.  Then
`gcd(A,N)=gcd(A',N)=1`.  From (2),

\[
d:=\gcd(A,A')=\gcd(A,NH)=\gcd(A,H). \tag{4}
\]

Write `A=da` and `A'=db`.  Then `gcd(a,b)=1`, so

\[
AA'\text{ is a square}
\quad\Longleftrightarrow\quad
a\text{ and }b\text{ are squares}. \tag{5}
\]

Indeed, `AA'=d^2ab`, and the coprime factors `a,b` must each have even
prime valuations.  Thus (4)--(5) are an exact factor-free pair screen.  In
particular, two retained nonsquare rows cannot form a square pair when
`d=1`.

If `a=u^2` and `b=v^2`, the positive integer square root is `R=duv`.  The
supplied modular root is

\[
X=xx'=AG_{h,D}(y)\pmod N.
\]

It is a unit, and

\[
\rho=RX^{-1}=v(uG_{h,D}(y))^{-1}\pmod N,
\qquad \rho^2=1\pmod N. \tag{6}
\]

For a product of two distinct odd primes, `rho=+1` or `rho=-1` is a global
root.  Every other `rho` is non-global, and the two public gcds

\[
\gcd(R-X,N),\qquad \gcd(R+X,N)
\]

recover the complementary prime factors.  These statements classify every
carried odd-multiple pair admitted by the frozen scan.  They do not give a
lower bound on how often (5) holds.

