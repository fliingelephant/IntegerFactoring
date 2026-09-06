# Proof of the F239 binary-spine statements

## 1. Endpoint and size

For an odd semiprime, `n=ceil(log2(N+1))` is its binary length.  Hence

\[
 2^{n-1}<N<2^n.
\]

It follows directly that `K_n=0` and `K_(n-1)=1`.  This proves the literal
endpoint defect and makes (1) the complete nonzero quotient spine.

For `1<=j<n`,

\[
 1\le K_j<2^{n-j}.
\]

Also `1<=R_j<2^j` and `1<=|C_j|<=2^{j-1}` because `N` is odd.  Therefore

\[
 \operatorname{bitlen}(W_K)
 \le n\sum_{j=1}^{n-1}(n-j)
 ={n^2(n-1)\over2},                                  \tag{P1}
\]

\[
 \operatorname{bitlen}(W_R)
 \le n\sum_{j=1}^{n}j
 ={n^2(n+1)\over2},                                  \tag{P2}
\]

and the same upper bound holds for `W_C`.  Every combined word has
`O(n^3)` bits.  Standard product-tree multiplication constructs it in time
polynomial in its output length.  The construction uses only `N`.

More precisely, for any nonzero absolute factors `A_j`,

\[
 1+n\sum_j(\operatorname{bitlen}(A_j)-1)
 \le
 \operatorname{bitlen}\left(\prod_j A_j^n\right)
 \le n\sum_j\operatorname{bitlen}(A_j).              \tag{P3}
\]

This is the size interval used for the named rows.

## 2. Quotient incidence

Write

\[
 N=2^jK_j+R_j,\qquad0\le R_j<2^j.
\]

If `ell | K_j`, reduction modulo `ell 2^j` gives

\[
 N\bmod(\ell2^j)=R_j<2^j.
\]

Conversely, suppose the least residue of `N` modulo `ell 2^j` is below
`2^j`.  It is congruent to `N` modulo `2^j`, so uniqueness in
`[0,2^j)` makes it `R_j`.  Thus `ell 2^j | N-R_j=2^jK_j`, and
`ell | K_j`.  This proves (3), including `ell=2`.

Now let `ell | s_p`.  Then `p=1 mod ell`, so

\[
 N=pq\equiv q\pmod\ell.
\]

Reduction of `N=2^jK_j+R_j` gives

\[
 2^jK_j\equiv q-R_j\pmod\ell.
\]

When `ell` is odd, `2^j` is invertible.  Therefore `ell | K_j` exactly
when `R_j=q mod ell`.  This proves (4).  For `ell=2`, both `q` and `R_j`
are odd, so their congruence is automatic and the converse fails.  This is
why (4) explicitly excludes two.

The `s_q` proof is symmetric.

For odd `ell`, the modulus `ell 2^j` has `ell 2^(j-1)` odd residue classes.
The interval in (3) contains exactly `2^(j-1)` odd classes.  The hit density
is therefore exactly `1/ell`.  Lift every event `1<=j<n` to the common
modulus `ell 2^(n-1)`.  The union bound gives (5).  If `ell>n-1`, the bound
is strictly below one, so an avoiding odd class exists.  No primality or
factorization property follows from this count.

## 3. Suffix incidence and saturation

Formula (6) is the definition `R_j=N mod 2^j`.  Round-half-up gives

\[
 C_j=
 \begin{cases}
 R_j,&R_j<2^{j-1},\\
 R_j-2^j,&R_j\ge2^{j-1}.
 \end{cases}
\]

Divisibility by `ell` gives (7).

Suppose `ell^a | s_i`.  Since `s_i<N<2^n`,

\[
 2^a\le\ell^a<2^n,
\]

so `a<n`.  If one base factor is divisible by `ell`, its `n`-th power is
divisible by `ell^n` and hence by `ell^a`.  If no base factor is divisible
by `ell`, the entire word is coprime to `ell`.  Applying this independently
to every prime power proves (8).

The construction algorithm does not need this factorization.  It is used
only to analyze `gcd(s_i,W)`.

Finally, `d | N-1` follows from

\[
 d=\gcd(p-1,q-1)=\gcd(N-1,p-1).
\]

Every odd prime dividing both `s_i` and `d` therefore divides
`(N-1)/2=K_1`.  This proves the stated overlap removal.

## 4. Power-of-two-neighbor families

If `N=2^m-1`, then `n=m`.  Direct division gives

\[
 K_j=2^{m-j}-1\quad(1\le j<m).
\]

Direct reduction gives `R_j=2^j-1` for `1<=j<=m`.  Every positive suffix is
in the upper half of its dyadic interval, so `C_j=-1`.

Let `ell` be an odd prime not dividing `N`.  The quotient and remainder
lists contain `2^t-1` for all `1<=t<m`; the final remainder `2^m-1=N`
does not add `ell`.  Thus a hit occurs exactly when some `t<m` is divisible
by `ord_ell(2)`, which is equivalent to (9).  The centered list adds only
units.

If `N=2^m+1`, then `n=m+1`.  For `1<=j<=m`,

\[
 K_j=2^{m-j},\qquad R_j=1.
\]

At the final index, `R_n=N`.  The centered suffixes have absolute value one
through index `m`, while

\[
 C_n=N-2^{m+1}=1-2^m.
\]

For an odd `ell` not dividing `N`, the quotient and positive-remainder
lists cannot hit.  The centered list hits exactly when
`ell | 2^m-1`, or equivalently when `ord_ell(2) | m`.  This proves (10).

Neither calculation supplies infinitely many prime factorizations of the
required type.  They are exact conditional family criteria only.

## 5. Finite computation boundary

The numerical claims are direct exhaustive outputs, not deductions from a
probability model.  The scanner factors the small residuals exactly.  For
each residual prime it checks (3), checks (4) only for odd primes, checks
(6)--(7), and independently computes each word modulo the whole residual.
It aborts if the prime-incidence residual and modular-word residual differ.

The F237 row uses its frozen certified residual factorization.  The named
checker uses Python integer arithmetic and does not make a new primality
claim.

The finite scans prove only their displayed bounds.  In particular, a
record that grows like `2^(n/2)` over these ranges is a pattern, not an
asymptotic theorem.
