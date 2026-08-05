# F04 proof-blind reconstruction

## Scope

This reconstruction used only the numerical claim, its allowed Frobenius key idea,
`STATEMENT.md`, and the computation rules in `PROMPT.md`.  It did not read
`REGISTRY.md`, `FAILED.md`, `PROVED.md`, `notes/Progress.md`, either pre-existing
F04 experiment directory, or any prior agent proof/certificate/output.

The result below is a finite counterexample to the proposed AKS
pass/fail/coefficient-gcd localization.  It is not a proof of the top-level
integer-factoring statement.

## Arithmetic and AKS parameters

Let

\[
N=20000000499999937,
\quad p=100000007,
\quad q=199999991,
\quad r=2953.
\]

Exact multiplication gives (pq=N).  Fresh deterministic trial division through
the square-root bound proves that (p,q,r) are prime: the respective bounds are
(10000,14142,54).  In particular (p,q>r), and (N) is the product of two
distinct primes.

A 256-bit rigorous real interval computation gives

\[
54.15084955426516859281773810405356 < \log_2N
 <54.15084955426516859281773810405357,
\]

\[
2932.31450744866020806830875641297246
 <(\log_2N)^2<
2932.31450744866020806830875641297247.
\]

Thus (2932<(\log_2N)^2<2933).  Trial division proves (r) prime, so
(phi(r)=2952=2^3 3^2 41).  With (u=N\bmod r=1146), modular exponentiation
gives

\[
u^{2952}=1,
\quad u^{1476}=2952,
\quad u^{984}=800,
\quad u^{72}=1277 \pmod {2953}.
\]

The last three residues are nonidentity residues for the prime divisors
(2,3,41) of (2952).  Hence (operatorname{ord}_{2953}(N)=2952), which is
strictly greater than ((\log_2N)^2).

For minimality, the verifier independently traversed powers of (N) modulo every
candidate (s=2,\ldots,2953), stopping at the first return to (1), and preserved
all exact orders.  The only passing candidate is (2953); the largest order below
it is (2926), at (s=2927).  The complete table is
`output/full_attempt3/orders_2_through_2953.csv`, SHA-256
`e52e0742358504d94a34024f643b83e3334dff252425fe15a3f1f6833430b07d`.

Finally, the rigorous interval

\[
2942.14078962724775554991425362559183
<\sqrt{2952}\log_2N<
2942.14078962724775554991425362559184
\]

proves that the standard shift bound is

\[
A=\left\lfloor\sqrt{\phi(r)}\log_2N\right\rfloor=2942.
\]

## Algebraic reduction

For a fixed integer (a), set

\[
H_a(X)=(X+a)^N-X^N-a,
\qquad
h_{m,a}(Y)=(Y+a)^m-Y^m-a.
\]

In characteristic (p), Frobenius and (a^p=a) give

\[
\begin{aligned}
H_a(X)
&=((X+a)^q)^p-(X^q)^p-a\\
&=(X^p+a)^q-(X^p)^q-a\\
&=h_{q,a}(X^p).
\end{aligned}
\]

Likewise, in characteristic (q), (H_a(X)=h_{p,a}(X^q)).  Since
(gcd(p,r)=gcd(q,r)=1), the maps (j\mapsto pj\bmod r) and
(j\mapsto qj\bmod r) permute all (r) coefficient positions after reducing
modulo (X^r-1).  Therefore it is enough—and is exactly equivalent for
zero/nonzero status—to exhaust all coefficients of (h_{q,a}) modulo (p) and
all coefficients of (h_{p,a}) modulo (q).

## Independent exhaustive computation

The named Sage source `reconstruct_f04.sage` performs exact quotient-ring
arithmetic, not floating-point polynomial arithmetic:

\[
\mathbf F_p[Y]/(Y^{2953}-1),
\qquad
\mathbf F_q[Y]/(Y^{2953}-1).
\]

For every (a=1,\ldots,2942), it extracts all 2953 canonical coefficient
residues.  It records a SHA-256 digest and the product modulo the local prime for
every row.  A row product is nonzero if and only if every coefficient in that row
is nonzero.  It also evaluates the original (H_a) directly at
(a=1,2,1471,2942) in each characteristic and confirms exact equality with the
permuted Frobenius reduction.

The exhaustive results are:

| local family | coefficients | zeros | minimum least residue | product of all coefficients | coefficient-stream SHA-256 |
|---|---:|---:|---:|---:|---|
| (h_{q,a}\bmod p) | 8,687,726 | 0 | 9 at ((a,j)=(1887,17)) | 50,824,481 mod (p) | `c4d12aeb2323ac745c119248f06f9fc0e20ee98a49683052a3f490d1756bd1ab` |
| (h_{p,a}\bmod q) | 8,687,726 | 0 | 27 at ((a,j)=(2566,1574)) | 146,774,171 mod (q) | `d92a9374923b24583a77571f2d9e6e941936040f0c4202c83e5c9012eed047ae` |

The stream hash encodes each shift as a little-endian unsigned 32-bit integer,
followed by its 2953 canonical coefficient residues in the same encoding.  The
compact per-shift certificates are:

- `output/full_attempt3/local_coefficients_mod_p.jsonl`, SHA-256
  `0ea82a9efa81cf1e8b1e19224c2c51cbd8320cee5bd0be670ad95744193a8df0`;
- `output/full_attempt3/local_coefficients_mod_q.jsonl`, SHA-256
  `18962035991d6e81f3c08218f9559cd998bd39689888b7349870373499883672`.

Each file has exactly 2942 sequential rows, every row covers 2953 coefficients,
and every recorded row product is nonzero.  A separate named artifact auditor
rechecked this structure, the empty zero files, the row-file hashes, and the
complete order table; its output is `output/artifact_audit_attempt2.json`.

## Consequence

For every (1\le a\le2942), every coefficient of (H_a) is nonzero modulo (p)
and nonzero modulo (q).  Since (N=pq), each coefficient is therefore a unit
modulo (N).  In particular:

1. every local polynomial identity fails (indeed, at every coefficient);
2. the global AKS identity fails for every tested shift;
3. taking the gcd of any failed coefficient with (N) returns (1), never a
   nontrivial factor;
4. the preliminary gcd checks through (r) also cannot see (p) or (q), since
   both factors exceed (r).

Thus the stated finite counterexample is reconstructed: standard minimal-(r)
AKS pass/fail information does not imply coefficient-gcd localization of a factor.
The claim status of this reconstruction itself is `self-audited`; the root
verification workflow determines whether it advances further.
