# F286 — Blind reconstruction of the global tangent-cut theorem

Input: RECONSTRUCTION_STATEMENTS.md

Input SHA-256: 3a3356cb1b779a2a40d46fe4f9fde4caad262ab928bc3ae44fba397a901b9e9f

Outcome: **proved**. The stated constant \(4096\) is sufficient. The same
witness also satisfies every ancestral modulus exactly as claimed.

## Proof

Write \(I_w=[L_w,U_w]\) for the interval associated with any residue \(w\)
modulo \(M\). The first integer at least \(B\) in that residue class is less
than \(B+M\), and the last integer at most \(2B\) in that class is greater
than \(2B-M\). Hence every residue interval contains the common core

\[
    [B+M,\,2B-M].
\]

Since \(A\geq 1\), the hypothesis gives \(M\leq B/4096\). Consider the fixed
parameter interval

\[
    J=[5B/4,\,7B/4].
\]

For \(x\in J\), put \(y=N/x\). The bounds on \(N\) give

\[
    \frac{8B}{7}
    =\frac{2B^2}{7B/4}
    \leq y
    \leq \frac{(9/4)B^2}{5B/4}
    =\frac{9B}{5}.
\]

The inequalities \(M\leq B/4096<B/7\) and \(M<B/5\) show that this entire
range for \(y\) lies in the common core. The same is immediate for
\(x\in[5B/4,7B/4]\). Therefore, for every choice of \(u\) and its associated
\(v\), every point

\[
    (x,N/x),\qquad x\in J,
\]

already satisfies \(x\in I_u\), \(y\in I_v\), and \(xy=N\).

It remains to choose one \(x\in J\) that satisfies all tangent cuts. Fix
\(1\leq a,b\leq A\), and set

\[
    r_{ab}=\sqrt{bN/a},
    \qquad
    f_{ab}(x)=ax+\frac{bN}{x}.
\]

The exact excess above the global minimum is

\[
    f_{ab}(x)-2\sqrt{abN}
    =a\frac{(x-r_{ab})^2}{x}.
\]

Let \(E_{ab}\subseteq J\) be the set on which this excess is less than
\(M\). Since \(x\leq 7B/4\) on \(J\), every \(x\in E_{ab}\) satisfies

\[
    |x-r_{ab}|
    <\sqrt{\frac{Mx}{a}}
    \leq \sqrt{\frac{7MB}{4a}}.
\]

Thus \(E_{ab}\) is contained in an interval of length

\[
    2\sqrt{\frac{7MB}{4a}}=\sqrt{\frac{7MB}{a}}.
\]

Summing these containing lengths over all \(a,b\), and using
\(\sum_{a=1}^A a^{-1/2}\leq 2\sqrt A\), gives

\[
\begin{aligned}
    \sum_{a=1}^A\sum_{b=1}^A |E_{ab}|
    &\leq A\sqrt{7MB}\sum_{a=1}^A a^{-1/2} \\
    &\leq 2\sqrt 7\,A^{3/2}\sqrt{MB} \\
    &\leq 2\sqrt 7\,A^{3/2}
       \frac{B}{64A^{3/2}} \\
    &=\frac{\sqrt 7}{32}B
    <\frac B2
    =|J|.
\end{aligned}
\]

Here the penultimate inequality is exactly where
\(M\leq B/(4096A^3)\) is used. Consequently the finitely many sets
\(E_{ab}\) cannot cover \(J\). Choose \(x_*\in J\setminus\bigcup E_{ab}\)
and put \(y_*=N/x_*\). Then, simultaneously for every \(a,b\),

\[
    ax_*+by_*\geq 2\sqrt{abN}+M.
\]

The integers in the residue class \(au+bv\pmod M\) are spaced by \(M\).
By the definition of \(T_{ab}\), its predecessor \(T_{ab}-M\) is strictly
less than \(2\sqrt{abN}\). Therefore

\[
    T_{ab}<2\sqrt{abN}+M,
\]

and hence \(ax_*+by_*\geq T_{ab}\). This proves survival at modulus \(M\)
for every odd \(u\).

## Ancestor consistency

Fix \(j\leq k\), let \(m=2^j\), and reduce \(u,v\) modulo \(m\). The reduced
\(v\) is the unique inverse partner because \(uv\equiv N\pmod M\) implies
\(uv\equiv N\pmod m\), while odd \(u\) is invertible modulo \(m\).

Every integer congruent to \(u\pmod M\) is congruent to the reduced residue
modulo \(m\). Thus the fine interval \(I_u^{(M)}\) is contained in the
ancestor interval \(I_u^{(m)}\); the same holds for \(v\). Therefore
\((x_*,y_*)\) satisfies the ancestor coordinate bounds.

For each \(a,b\), the fine threshold \(T_{ab}^{(M)}\) is itself an integer
at least \(2\sqrt{abN}\) in the required residue class modulo \(m\). Since
\(T_{ab}^{(m)}\) is the least such integer,

\[
    T_{ab}^{(m)}\leq T_{ab}^{(M)}.
\]

The fine-modulus inequalities therefore imply all ancestor inequalities.
The same point \((x_*,y_*)\) works at every level \(2^j\), completing the
claim.
