# F238 V2 corrigendum — proof repair for the multi-support lower bound

## Frozen V1 status

The five V1 inputs remain unchanged.  The squarefree-semiprime statement,
exact formulas, and proof are unaffected.

The final inference in section 6 of `PROOF.md` is invalid as written.  The
two displayed product bounds have opposite useful signs because
`prod_i alpha_i` has a negative coefficient.  They do not directly prove
the second inequality in statement (9).

The inequality itself is correct.  Replace only the final paragraph of
section 6 with the following proof.

## Correct proof

Let

\[
 a=\max_i\alpha_i,
\]

and choose an index `m` with `alpha_m=a`.  Put

\[
 B=\prod_{i\ne m}(1-\alpha_i),
 \qquad
 C=\prod_{i\ne m}\alpha_i,
 \qquad
 \mu=\mu_{\boldsymbol h}.
\]

The lower bound in statement (9) is

\[
 S=1-(1-a)B-(1-\mu)aC.                                \tag{C1}
\]

For each `i!=m`, the inequality `alpha_i<=a` gives

\[
 1-\alpha_i\ge {1-a\over a}\alpha_i.
\]

Multiplying these inequalities, and using `k-1>=1`, gives

\[
 B\ge \left({1-a\over a}\right)^{k-1}C.               \tag{C2}
\]

There are two cases.

If `a<=1/2`, then `B>=C`.  Therefore

\[
 \begin{aligned}
 S-\mu a
 &= (1-\mu)a(1-C)+(1-a)(1-B)\\
 &\ge0.                                                \tag{C3}
 \end{aligned}
\]

If `a>=1/2`, then `B<=1` and `C<=a^{k-1}`.  Hence

\[
 \begin{aligned}
 S-\mu a
 &=(1-a)(1-B)+(1-\mu)a(1-C)\\
 &\ge0.                                                \tag{C4}
\end{aligned}
\]

In fact, identity (C3)--(C4) is the same algebraic identity and does not
require either case-specific product comparison:

\[
 \boxed{
 S-\mu a=(1-a)(1-B)+(1-\mu)a(1-C)\ge0.
 }                                                       \tag{C5}
\]

Thus

\[
 S\ge\mu\max_i\alpha_i\ge {1\over2}\max_i\alpha_i,
\]

which is the claimed second inequality in statement (9).

## Audit note

The case split and (C2) are included to expose the edge regimes, but the
short identity (C5) is sufficient.  No statement changes.  A hostile audit
must authenticate the five frozen V1 inputs plus this corrigendum and use
the corrigendum in place of the invalid final inference.
