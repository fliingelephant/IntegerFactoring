# F84 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F84 candidate,
audit, later F84 artifacts, or later durable-state entries.

Let \(N=pq\) for distinct odd primes, let \(Q\) be public unit blocks, and
put

\[
H=\langle Q\rangle
\le\mathbb F_p^\times\times\mathbb F_q^\times.
\]

Prove or refute the equivalence of these four conditions:

1. every \(x\in H\) satisfies \(\gcd(x-1,N)\in\{1,N\}\);
2. both projections \(H\to H_p,H\to H_q\) are isomorphisms;
3. \(H\) is the graph of an isomorphism \(H_p\to H_q\);
4. every \(x\in H\) has equal local orders modulo \(p\) and \(q\).

If they hold, prove or refute that negative signs also synchronize for every
\(x\in H\). Also prove or refute that, for every explicit relation list on
\(Q\) and every prime \(\ell\), the two identity kernels of its exact
prime-saturation root map are equal. State whether small-prime saturation
failure is redundant once exhaustive subgroup-wide direct-sign failure is
known.

Separate this exhaustive statement from finite-menu failure. Check the fixed
counterexample

\[
N=35,
\qquad
Q=\{2\}.
\]

The listed generator passes both direct sign screens and an empty relation
list gives no saturation vector, but

\[
\gcd(2^3-1,35)=7.
\]

Now let \(H\) be a graph state and let a residue-neutral canonical feedback
step refine public integer blocks to a larger subgroup \(K\ge H\). Put

\[
h=|H|,
\qquad
c=[K:H],
\qquad
a=[K_p:H_p],
\qquad
b=[K_q:H_q].
\]

Prove or refute:

1. the two quotient projections are surjective, so \(a\mid c\) and
   \(b\mid c\);
2. the exact positive-separator count in \(K\) is

   \[
   \frac ca+\frac cb-2;
   \]

3. \(K\) remains a graph exactly when \(c=a=b\), and the graph breaks
   exactly when \(c>a\) or \(c>b\).

For a single-overlap extension \(K=\langle H,u\rangle\), verify that
\(c,a,b\) are the global and two local orders of the corresponding coset of
\(u\). Prove that every exponent \(0<t<c\) divisible by \(a\) has a unique
old element that cancels \(u^t\) modulo \(p\), producing a positive
separator; state the symmetric \(q\)-claim.

Finally, verify the exact quotient classification of the fixed phase witness

\[
N=2047=23\cdot89,
\qquad
H_0=\langle11\rangle,
\qquad
K=\langle11,2\rangle.
\]

Use the established local orders

\[
\operatorname{ord}_{23}(11)=\operatorname{ord}_{89}(11)=22,
\qquad
\operatorname{ord}_{23}(2)=\operatorname{ord}_{89}(2)=11,
\]

and \(2\notin H_0\). Prove or refute

\[
c=11,
\qquad
a=b=1,
\]

so neither local projection grows although the graph breaks and \(K\)
contains exactly 20 positive separators. Check that \(2\cdot11=22\) is a
negative separator.

State the scope: the theorem does not compute the hidden indices, enumerate
an exponential subgroup, select a cancellation word, or prove that a useful
feedback split occurs on every input. Failure of current finite menus or
small-prime root spaces after a graph break is an access gap, not proof that
the ambient subgroup has no separator.
